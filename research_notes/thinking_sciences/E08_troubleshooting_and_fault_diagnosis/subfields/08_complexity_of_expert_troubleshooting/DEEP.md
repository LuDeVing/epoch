# Complexity of expert troubleshooting: deep document

*Subfield E08.08. Evidence ids (a01 to d16) point to evidence_a-d.jsonl; claim ids (K01 to K29) to claims.jsonl; critique.md lists the re-checks. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

This subfield asks what makes troubleshooting hard for experts, and how experts handle that difficulty. The core human work is a small interview programme by Sabuncu and colleagues (ASEE papers 2024 and 2026, NSF grant 2422510). They ask senior engineers how they see and manage complexity when a system misbehaves.

Main result: complexity is not only a property of the fault. It sits in the match between the system, the information, the situation and the people involved. Experts name four kinds: system representation, information ambiguity, situational, stakeholder (a01, c01). The authors then propose five "manifolds" (system dynamics, epistemic, normative, divergence, situational/stakeholder). Complexity is a misalignment across layers that blocks progress toward resolution (c01, a03).

Why it matters for our agent: could an agent that first labels why a problem is hard pick a better operator and a better stopping rule? That is an S0 triage idea. The human evidence is thin (9 to 18 interviews, no outcome test). So this document pairs it with the larger body of LLM troubleshooting benchmarks (AIOps, SRE, network, medical diagnosis, debugging). Those give numbers on what goes wrong when a model diagnoses a fault. The interview work gives a vocabulary and a trigger list.

Scope: diagnosability, model-based diagnosis, software and KB debugging, premature closure and cognitive task analysis are covered by sibling subfields. Here they are only linked. Self-correction and anchoring appear only where they bear on troubleshooting agents.

## 2. History and theories in depth

### 2.1 Structured Troubleshooting (2000)
Schaafstal, Schraagen and van Berlo (2000) ran a cognitive task analysis of technicians (Dutch radar and air-defence systems) and built a course, Structured Troubleshooting (ST). ST teaches a domain-independent strategy plus functional decomposition. Reported: ST-trained technicians solved twice as many malfunctions, in less time, and the course was shorter (a13). We hold only the abstract. No N, times or replication (d14). One source.

### 2.2 Hypothesis levels (Jonassen and Hung 2006)
A design architecture for learning to troubleshoot, with hypotheses at four levels: system, subsystem, device, component (a14). Known only from secondary notes. It supports top-down multi-level decomposition, as ST does.

### 2.3 Modelling and prediction loop (Dounas-Frazer et al. 2015)
16 junior electronics students (4 pairs at each of 2 universities) debugged a two-stage amplifier with two faults: R3 at 100 ohm instead of 1 kohm, and a burned-out op-amp. Input 100 mV; expected 2 V inverted at stage 2; measured about 10 mV non-inverted (a15). The authors describe a cycle: model, predict, measure, compare, propose. Split-half testing was the common strategy. Negotiation between partners about when to move on sat outside the model (a15, a16). No counts given.

### 2.4 Industry view of mechanical troubleshooting (Daly et al. 2024)
9 engineers, 10 to 40 years of experience, 30 to 60 minute interviews. The diagnostic-techniques theme appeared in 22 coded instances. Tools named: decision trees, 5 whys, FMEA, root cause analysis, pattern recognition (a09, a12). Single-interviewee examples: in a life-critical medical device case, remote monitoring found an abnormal voltage spike unique to the affected device and avoided a recall (a10). One interviewee described two novice types: those who ask for help at once and those who never ask and get stuck (a11).

### 2.5 Complexity manifolds (Sabuncu, Boyer, High 2026)
18 engineers with over 10 years of experience: 14 industry, 4 academic; 10 PhD, 2 MS, 6 BS; 17 male, 1 female. Domains: manufacturing, medical devices, robotics, defense, power electronics, software/CAD, academia (a01). Overlapping group counts: defense 4, biomedical 8, product design 13 (a05). Think-aloud: 6 run, 2 reported (one expert, one PhD student) on a pneumatic compressor that shuts down after about 2 minutes, hot motor housing, tank pressure 20 to 25 psi below the cut-out threshold. Cues were deliberately incomplete (a04, c02).

Findings from the 2 reported think-alouds plus interviews:
- Troubleshooting is non-linear and recursive. Experts revisit system understanding, root-cause search and evidence checks (a06). It rests on two temporal codings, no revisit counts.
- Progress at the system layer is judged by change in behaviour, not by how persuasive an explanation is (a03). This matches our guardrail G10.
- Worked example: if the divergence and situational manifolds are misaligned and one cannot tell whether the system is faulty at all, that registers as situational complexity (a02).
- Testing of the mapped scaffolds is future work (a07).

Count conflict: the NSF poster says 22 interviews, the 2026 paper 18; both say 6 think-alouds. Unexplained (a08).

### 2.6 What the human line cannot yet say
No statistics, no inter-rater figures, no counts per category, no outcome test of whether complexity type predicts success or whether the mapped scaffolds help (K24). It is a theory proposal and a vocabulary.

### 2.7 The LLM turn (2023 to 2026)
From 2023 the field moved to LLM agents on cloud incidents (RCACopilot, RCAgent, OpenRCA, AIOpsLab, ITBench, SREGym), network faults (NIKA, FaulT-Bench), clinical diagnosis (Nori et al.) and debugging (DebugBench). The shared finding: difficulty depends on stage (detect, localise, find cause, repair), on scenario (new failure types, bigger systems, more evidence sources) and on framing (vague or false reports).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts name four complexity kinds | 18 senior engineers; no counts per category | a01, c01 | [S] |
| Complexity as misalignment across five layers | Theory proposal; 2 think-alouds shown of 6 | a02, a03, a06 | [S] |
| Experts model normal operation first | 9 interviews (Daly) plus 2 think-alouds | a10, a11, a04 | [E] weak (qualitative) |
| Student loop: model, predict, compare, propose | 16 students, 8 pairs | a15, a16 | [S] |
| Structured Troubleshooting doubled solved faults | Abstract only; no N | a13, d14 | [S] |
| Agent accuracy drops from detection to repair (AIOpsLab) | Detection GPT-4 69.23, GPT-3.5 23.07, ReAct 76.92, FLASH 100; Acc@1 localisation 61.54/53.85/46.15 (GPT-4/ReAct/FLASH); RCA 40.90/9.09/45.45/36.36 (GPT-4/GPT-3.5/ReAct/FLASH); mitigation GPT-4 27.27, GPT-3.5 0, FLASH 36.36; overall 49.15/15.25/55.93/59.32 | a17, b05, b06 | [E] |
| Real SRE incidents rarely solved (ITBench, 94 scenarios) | 13.8% SRE, 25.2% CISO, 0% FinOps; GPT-4o diagnosis 36/7.73/5.0 and mitigation 21/12.27/0.0 for easy/medium/hard; no model mitigated any hard scenario | a19, b07, c16 | [E] |
| New failure types much harder (SREGym) | End-to-end ported (n=34) vs new (n=13): Stratus+Sonnet-4.6 63.7 to 17.9; Claude Code 60.8 to 28.2; Codex 57.8 to 15.4; Stratus diagnosis 70.6 vs 33.3 | c10, c11 | [E] |
| Diagnosis and repair decouple | Scenario 15: wrong cause named yet alert cleared; scenario 13 about 80% diagnosed, none repaired; 10 runs: diagnosed 6/10, 1/10, 8/10 across three scenarios | a20, b08 | [E] |
| Human explanation lifts repair | GPT-4 vs human feedback: overall 33.30 to 52.60; intro 42.64 to 62.21; interview 19.33 to 45.67; competition 3.67 to 14.67; 16 participants, 40 programs | b02 | [S] |
| Self-repair equals resampling at equal compute | 1.05x (10 samples + 1 repair vs pass@20); 0.97x (2 samples + 10 repairs vs pass@22) | b01 | [E] with b03, b04 |
| Self-correction without external signal hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle labels: GPT-3.5 GSM8K 75.9 to 95.5, HotpotQA 26.0 to 49.0 (GPT-4 29.0 to 59.0) | b03, b25 | [E] |
| External tools make correction work | Survey: no prompted-feedback success on general tasks; works with reliable external tools | b04 | [E] |
| Multi-turn underspecified input | Average drop 39%; aptitude -15%; unreliability +112%; 200,000+ conversations, 6 tasks | b16 | [E] |
| Hypothesis tracking plus challenger panel | Physicians 20% at $2,963; o3 78.6% at $7,850; MAI-DxO no budget 81.9% at $4,735; budgeted 79.9% at $2,397; ensemble 85.5% at $7,184; 304 NEJM cases | b09, b10, d01, d02 | [S] |
| No role-level ablation in MAI-DxO | Single vs batched both 83.9%; $3,991 vs $5,084 | d03, K25 | [S] |
| Information-gain question choice | FloDial GPT-4 43.7 to 67.3 absolute; 7.8 questions; average +38.1% over direct prompting (relative or absolute unclear) | b15 | [S] |
| Prompt-level fixes fail on RCA | Baseline perfect accuracy 3.9 to 12.5%; hypothesis/pitfall prompts 0 to 7.3%; hallucinated interpretation 71.2%, incomplete exploration 63.9% | c12, c13, c25 | [S] |
| Symptom taken as cause | Above 45% for GPT-5 mini and GPT-OSS 120B (up to 68.4% in one cell) | c25 | [S] |
| SOP knowledge helps | Flow-of-Action GPT-4-Turbo 64.01 vs ReAct 35.50, CoT 32.61, K8sGPT 11.11; GPT-3.5 ablation: full 54.06, no SOP knowledge 15.39, no SOP flow 27.50, no action set 42.34; 90 incidents, 1 system, 9 fault types | c18, d06, d07 | [E] direction, [S] size |
| Past incidents help | In-context GPT-4 24.8% better than fine-tuned GPT-3, 49.7% better than zero-shot; RCACopilot accuracy up to 0.766 | a25, a22 | [E] |
| Context management stabilises agents | RCAgent 99.38% pass within 15 steps; removing JSON repair -33.54% pass, 70.95% invalid | a23, c17 | [S] |
| Vague report breaks agents | Claude Code .870 to .283 on no-detail ticket; over-diagnosis 17% to 47%; tool calls 13 to 30; tokens read 136k to 549k | c06, c07 | [S] |
| Confident wrong tickets barely matter | Wrong-device +2.5, wrong-cause -2.1 points vs .932; phrasing alone up to 14.5 points | c05, c24 | [S] |
| Agents fail to stop | 366 of 3,960 runs (9%) timed out and used 23% of US$1,525 | c07 | [S]; stop failure [E] with a18 |
| Step plateau | Above about 5 steps did not help non-FLASH agents; tokens rose | b06, c15 | [E] agent-specific |
| Size and evidence demands | Networks of 11/27/101 nodes: localisation and RCA fall, detection stable; GPT-5 detection/loc/RCA 89.0/68.7/55.3, GPT-5-mini 74.0/36.0/22.0, GPT-OSS:20B 19.0/5.5/5.5; 62.5% of 400 cases need 2+ data types | c08, c09, c20, d10 | [E] |
| Debug difficulty scales with bug count | GPT-4: missing colon 93.6, double 70.7, triple 58.9, quadruple 55.9; runtime feedback little help on logic bugs | b11, b12 | [S] |
| Zero-shot agent-trace fault typing is poor | Fault type top-1 best 24.8% (top-3 34.0%); random about 9%; 275 traces | c22 | [S] |
| Extra human discussion text did not help RCA | "Does not yield significant improvements"; machine vs human detected incidents METEOR 9.41 vs 7.65 (592 test) | b23, b24 | [C] |
| LLM on physical circuits: qualitative only | 17 chat logs; one 99%-confident wrong pin claim | d11, d12, d13 | [S] |

## 4. Mechanisms and models

Each is written so an engineer could implement it. These are our readings; status is stated.

### 4.1 Complexity triage at S0 (untested proposal, K01, K28)
Input: problem statement and available tools. Output: one label from {representation, ambiguity, situational, stakeholder} plus a one-line reason.
- Representation: the agent cannot say how the system normally behaves or is connected. Next: build a short normal-behaviour model (components, flows, expected values) before any hypothesis.
- Ambiguity: data are missing, conflicting or noisy. Next: pick the cheapest observation that splits the hypotheses; quote raw data before interpreting.
- Situational: unclear whether a fault exists, or the report may be wrong or vague (a02). Next: no-fault gate; ask what would refute the report.
- Stakeholder: conflicting goals or limits (cost, safety, uptime). Next: record the constraint list and check any repair against it.
The program routes on the label; the model only fills the slot. No study shows this helps. The label is a hypothesis.

### 4.2 Normal-behaviour model first (K03)
Slot: "List 3 to 6 things that should be true when the system works, with expected values." Store in a table. Compare later observations to this table in code where possible. This is the model-predict-compare loop (a15) made explicit.

### 4.3 Predict-then-observe loop (K04)
Before each tool call the model writes a predicted outcome for at least two hypotheses. After the call, code diffs the real output against the predictions. Count wasted calls (calls whose result would be the same under every live hypothesis). Same idea as information gain (b15): choose the test that splits the hypothesis set most.

### 4.4 Hypothesis table with a forced second hypothesis (K11, K12)
Fields: hypothesis, evidence for (quoted), evidence against (quoted), cheapest disconfirming test, status. Rule: before commit, at least 2 live hypotheses and one disconfirming test run on the leader. MAI-DxO did this with roles (b10) but no ablation isolates it (K25). In our schema it is a table kept by code with a model slot per row, not a debate (G9).

### 4.5 Multi-level decomposition (K05, K22)
Levels: system, subsystem, device, component (a14). Use split-half tests (a15): each test should halve the candidate set. Isolate one fault at a time (b11: pass rate falls with bug count).

### 4.6 SOP and incident retrieval (K15)
Store solved faults as records: symptom signature, confirmed cause, fix, the check that proved it. At S0 retrieve similar records by symptom and offer them as hypotheses to test, never as answers. Shown after the first attempt, per the lessons rule in SCHEMA, to limit fixation. Flow-of-Action tested only repeated fault families (d06, d07).

### 4.7 Verify before repair (K08, K09)
Before submitting a mitigation, code checks that it is consistent with the stated cause and that the fault signal actually changed after the fix (behaviour change, a03). Diagnosis and repair decouple (b08): a correct label is not proof, and a cleared alert is not proof of the right cause.

### 4.8 No-fault gate and stop rules (K17, K18, K28)
First action: look for evidence that a fault exists. If none after k observations, exit with "no fault found". Step cap per difficulty class. Reason: false-premise tasks drop outcome to .820, a vague ticket pushes over-diagnosis to 47% (c05, c06), and timeouts took 23% of spend (c07).

### 4.9 Enforced grounding (K14)
Before interpreting, the model must quote the exact line or value from the tool output, and code checks the quote is a substring of the output. Prompt warnings did not cut hallucinated reading (c12, c13). Cai et al. score evidence checkpoints deterministically (d09), which gives a way to measure grounding.

### 4.10 Reference trace (K23)
Give a known-good run or normal-behaviour record for comparison. It helped somewhat in agent-trace fault typing (c22).

## 5. What holds up

**Established or well supported**
- Stage ordering for agents: detection easier than localisation, RCA and repair, for stronger models (AIOpsLab, NIKA, ITBench, SREGym). GPT-3.5 got only 23% on detection, so the order holds for stronger agents (critique).
- Self-correction without an external signal does not help (b03, b04, b01). Gains need tools, oracle signal, retrieved procedure or a role with different information.
- Anchoring on first impressions or the first anomaly harms diagnosis (b16, b10, c12, c25).
- Agents do not know when to stop on healthy systems (c05, c07, a18).
- Retrieved SOPs and similar incidents help (c18, a25, a22), on known fault families at least.
- Plateau near 5 steps for non-FLASH agents while tokens rise (b06, c09).

**Failures and tensions**
- Human discussion text did not help RCA predictions (b23, b24) [C].
- FaulT-Bench: confident wrong tickets barely hurt but vague tickets hurt a lot. This is the opposite of a human anchoring story and is single-paper (c24).
- Detection "easiest" vs "most agents did not solve detection" (a17): only FLASH got 100%.
- Interview counts differ across Sabuncu sources (18 vs 22).
- Self-correction fails (Huang, Kamoi) yet MAI-DxO and Flow-of-Action gain from structured critique and procedure. Our reading: the gain comes from outside information, not re-reading. Not tested.
- MAI-DxO ensemble gain (85.5 vs 81.9) may be sampling, not role-play (d04, K26).

**Moderators seen:** model size and family (NIKA GPT-5 vs mini vs 20B); topology size; number of evidence types; ticket wording; novelty of the failure (ported vs new); bug count. Repeated vs unseen fault families is untested.

**Interventions that worked:** human-quality explanation before repair (b02); information-gain question choice (b15); SOP knowledge (d07); context management (a23); hypothesis plus challenger roles with ensembling (d02).
**Interventions that did not:** self-repair at equal compute (b01); intrinsic self-correction (b03); prompt-level pitfall warnings (c13); adding discussion text (b23); steps beyond about 5 (b06).

**Weak spots:** run-to-run variance (ITBench 1/10 to 8/10 on one scenario); LLM judges in places (SREGym kappa 0.90 vs human oracle; RCAgent G-correctness); 1 to 3 passes per cell. Most agent studies vary the model, not the scaffold. Not re-opened in the critique, so one-read: FaulT-Bench, SREGym, Kim et al., NIKA, RCAgent, Flow-of-Action, DebugBench, Sabuncu and Daly.

## 6. Language models

- On cloud and network faults, frontier agents solve a minority end to end. ITBench SRE 13.8%. OpenRCA best about 11.34% correct (snippet only, c14). Kim et al. baseline perfect answers 3.9 to 12.5% (c12). SREGym is higher (about 54.8 to 60.7% end to end for the best agents) but falls to 15.4 to 28.2% on newly written failures (c10, c11).
- Bigger or newer models help a lot. NIKA RCA: 5.5% (GPT-OSS:20B), 22.0% (GPT-5-mini), 55.3% (GPT-5), at about 50% more runtime for GPT-5 (c08, c09).
- Scaffold effects come mostly from external information: SOP knowledge (15.39 to 54.06 on GPT-3.5, +38.7 points), past-incident retrieval (+24.8% over fine-tuned), tool-use context management (RCAgent), information-gain question choice (+23.6 points on FloDial).
- Changes inside the model do not help: intrinsic self-correction lost 37.7 points on one task (b03); prompt-level fixes left RCA near 0 to 7% (c13).
- Medical sequential diagnosis: o3 78.6% vs physicians 20%; MAI-DxO 81.9% at 60% of o3's cost (b09). The physician baseline had no outside help and 11.8 min per case (d05), so it is not typical practice.
- Failure modes: symptom-as-cause (above 45% for two models), hallucinated reading of data (above 66%), incomplete exploration (above 60%), over-diagnosis on false reports (17% to 47% with vagueness), repair without verification, stop failures (9% of runs, 23% of cost).
- Multi-turn underspecified input costs 39% on average; aptitude down 15%, unreliability up 112% (b16). Vague tickets act the same way.
- Physical hardware (analog circuits): only qualitative evidence. Models often named the true cause but misread wiring photos and once stated 99% confidence on a wrong reading (d12).
- Zero-shot fault typing on agent traces is weak: 24.8% top-1 (c22).
- Scoring: outcome-only scoring can reward luck; deterministic evidence checkpoints exist (d09); no human re-score of agent benchmarks was found.

## 7. What our agent should take

### Add now (established)
| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Revise only from a tool output or test result; ban pure re-reading revisions in diagnosis | G2 / G10 | [E] | b01, b03, b04, b25 |
| Normal-behaviour model step before hypotheses on fault tasks (one slot) | S0 / O6 | [E] weak: qualitative human data plus indirect agent support | a04, a09, a10, c26, c18, d07 |
| Report accuracy by stage (detect, localise, cause, repair) and by difficulty | eval / G12 | [E] | a17, b05, a19, c10 |
| Step and token cap by difficulty; about 5 steps as plateau to confirm; stop on timeout | G12 | [E] | b06, c07, c09, a18 |
| Absence of a fault is an allowed answer (need established; the gate itself is untested) | S0 / S9 | [E] need | c05, c06, a18 |
| Check mitigation fits stated cause and that the signal changed | G2 / S6 | [E] | b08, a20, a03 |
| Repeat runs; do not trust one pass on high-variance items | G7 / G3 | [E] | a20, c27 |
| Retrieve similar solved faults and SOPs as hypotheses, shown after first attempt | memory | [E] repeated families only | c18, a25, a22, d07 |

### Test first
| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Complexity-type triage at S0 routing to different first operators | S0 / G1 | [S] | a01, c01, d16 |
| Forced second hypothesis and one disconfirming test before commit | O-challenge / G-anchor | [S] | b10, d01, d02, c25 |
| Predict-then-observe step with code diff | O-test | [S] | a15, a16 |
| Information-gain test choice | O-select-test | [S] | b15 |
| Back-edge from any state to system modelling | S-loop | [S] | a06, a04 |
| Multi-level decomposition and single-fault isolation | O3 | [S] | a13, a14, b11 |
| Enforced quote-the-data grounding | G10 | [S] untested | c12, c13, d09 |
| No-fault gate before diagnosis | S0 | untested | c05, c06, d16 |
| Cross-source evidence fusion on multi-source cases | S-evidence | need [E], fix untested | c20, d10 |
| Role ablation: tracker vs challenger vs ensemble | O-roles | [S]/[C] with G9 | d02, d03, d04 |
| Known-good reference trace at S0 | memory | [S] | c22 |
| Extra unstructured context, with and without a filter | S0 | [C] | b23, b24 |

Do not replace plain sampling and voting with role-play voters. G4 and G9 say one model's samples are not independent and debate is mostly extra sampling. The MAI-DxO ensemble gain (d04) counts as sampling plus aggregation until a role ablation says otherwise.

## 8. Concrete tests on our bench

All tests are at equal tokens: the scaffold arm's total including setup; the plain arm spends the same on extra samples with code-based voting. At least 3 runs per item.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Fault diagnosis items (SREGym/AIOpsLab style or our own multi-step fault puzzles) | Triage-routed vs no triage vs random label | RCA accuracy; tokens | +3 to 8 points, or null; label accuracy matters |
| T2 | Same, hard split | Normal-behaviour step vs none | Localisation and RCA accuracy | Small gain on representation-heavy items |
| T3 | False-premise items mixed with real faults | No-fault gate vs none | False-alarm rate; detection rate; tokens | False alarms down over 10 points, detection within 3 |
| T4 | Faults with a misleading first anomaly | Forced second hypothesis plus disconfirming test vs none vs best-of-k vote | Symptom-as-cause rate; accuracy | Symptom-as-cause down; accuracy not below vote |
| T5 | Multi-tool diagnosis | Code-checked quote-before-interpret vs prompt warning vs none | Hallucinated reading rate; RCA accuracy | Hallucination down 20% relative |
| T6 | Diagnose-then-repair tasks | Consistency check vs resample | Repair success; cause-repair mismatch | Mismatch down; repair up |
| T7 | Items with 1 to 3 simultaneous faults | Single-fault isolation vs fix-all | Pass rate by fault count | Gain grows with fault count |
| T8 | Diagnosis dialogue items | Information-gain test order vs arbitrary | Success within turn cap; questions used | Fewer tests, success up |
| T9 | Repeated and unseen fault families | Retrieval of solved faults and SOPs vs none | Accuracy on repeated vs unseen split | Large gain on repeated; null or negative on unseen |
| T10 | Vague vs precise ticket rewrites of one fault | Clarify-first step vs none | Outcome; over-diagnosis; tokens | Loss from vagueness cut by half |
| T11 | Difficulty-stratified items | Step caps 3, 5, 10, 20 | Accuracy vs tokens | Plateau near 5 on easy, later on hard |
| T12 | Medical or other diagnostic cases | Single panel vs role panel vs k samples with vote | Accuracy at equal cost | Role panel beats k-vote only if roles carry the gain |

Scoring: LLM judges only with a human re-score of a sample. Prefer deterministic checks and evidence-checkpoint scoring (d09).

## 9. What does not transfer, and why

- The interview results come from engineers on physical systems (compressors, devices) with tools, time and colleagues. Our agent has no tactile, social or career knowledge. Stakeholder complexity may have no analogue in single-item benchmarks.
- Experts pick knowledge types from years of schemas. An agent without schemas cannot choose among them; retrieval has to stand in.
- The students' modelling loop (a15) is from a two-stage amplifier. Transfer to open-ended software or cloud systems is untested.
- The ST doubling (a13) is for Dutch military technicians with a trained domain strategy, abstract only.
- MAI-DxO used a paid test-ordering simulation on NEJM cases with a physician baseline that could not look anything up (d05). Real clinical effect is not shown.
- Cloud benchmarks are mostly microservice systems with injected faults. Real faults are messier. Flow-of-Action had 1 system and 9 fault types (d06).
- Human anchoring on confident wrong tickets did not appear in FaulT-Bench (c24), so human bias findings may not map onto agents.
- Step plateau and token numbers belong to specific agents and change with model version.
- Prompt-level fixes failing on RCA does not mean schema-level enforced steps fail: the schema puts code between the steps.

## 10. Open questions

1. Does complexity-type triage at S0 change the path and improve RCA at equal tokens? No study (d16).
2. Which role in MAI-DxO carries the gain: tracker, challenger, cost checker, ensemble? No ablation (d01 to d04).
3. Real N, times and solve rates in Schaafstal et al. (2000), and replications outside Dutch technicians (d14).
4. Do expert-vs-novice differences in order of work predict success in larger samples? Hu and Ash is chat logs, not think-aloud (d11).
5. How do LLM agents do on non-IT fault domains? No measured benchmark (d15).
6. Does a no-fault gate cut over-diagnosis without lowering detection? Untested.
7. Does enforced grounding cut hallucinated readings? Cai et al. give a metric but no agent results were read (d09).
8. Do past incidents plus SOPs help on unseen fault families (d06)?
9. What step or token budget fits each difficulty level, given the 5-step plateau and 0% hard mitigation?
10. How much reported agent gain is judge or benchmark artefact? No human re-score found.
11. Why do Sabuncu sources report 18 vs 22 interviews?
12. Is the AIOpsLab plateau a property of agent design or of the tasks?
13. Does a challenger role beat plain resampling at equal cost, given G9?

## 11. Sources

[V] opened and read; [M] snippet or abstract only.

- [V] Sabuncu, Boyer, High (2026) BCSER ASEE 52353 - https://peer.asee.org/59400 ; https://peer.asee.org/bscer-capacity-building-for-developing-a-troubleshooting-learning-environment.pdf (a01 to a07, c01 to c03)
- [V] Sabuncu (2026) NSF ECR PI poster - https://ecrhub.org/sites/default/files/PI-meeting-26/LR-Infographics/Emerging-Competencies-and-Workforce-Pathways-in-STEM/Ahmet-Can-Sabuncu.pdf (a08)
- [V] Daly, Anand, Abel, Sabuncu (2024) ASEE 47617 - https://peer.asee.org/47617.pdf (a09 to a12, c04, c26)
- [M] Schaafstal, Schraagen, van Berlo (2000) - https://doi.org/10.1518/001872000779656570 ; https://research.utwente.nl/en/publications/cognitive-task-analysis-and-innovation-of-training-the-case-of-st/ (abstract only; a13, d14)
- [M] Jonassen and Hung (2006) - https://doi.org/10.1007/s10648-006-9001-8 (a14)
- [M] Gugerty (2007) - https://doi.org/10.1080/13546780600750641 (b21, not read)
- [V] Dounas-Frazer et al. (2015) - https://arxiv.org/abs/1507.03939 (a15, a16)
- [V] Chen et al. (2025) AIOpsLab - https://arxiv.org/abs/2501.06706 (a17, a18, b05, b06, b22, c15)
- [V] Jha et al. (2025) ITBench - https://arxiv.org/abs/2502.05352 (a19, a20, b07, b08, c16)
- [V] Roy et al. (2024) RCA agents - https://arxiv.org/abs/2403.04123 (a21, b13, b23)
- [V] Gao et al. (2023) RCACopilot - https://arxiv.org/abs/2305.15778 (a22)
- [V] Wang et al. (2024) RCAgent - https://arxiv.org/abs/2310.16340 (a23, c17)
- [V] Pham et al. (2025) RCAEval - https://arxiv.org/abs/2412.17015 (a24)
- [V] Zhang et al. (2024) In-context RCA - https://arxiv.org/abs/2401.13810 (a25)
- [V] Olausson et al. (2024) Self-repair - https://arxiv.org/abs/2306.09896 (b01, b02)
- [V] Huang et al. (2024) Self-correction - https://arxiv.org/abs/2310.01798 (b03, b25)
- [V] Kamoi et al. (2024) - https://arxiv.org/abs/2406.01297 (b04)
- [V] Nori et al. (2025) Sequential diagnosis - https://arxiv.org/abs/2506.22405 (b09, b10, d01 to d05)
- [V] Liu et al. (2024) DebugBench - https://arxiv.org/abs/2401.04621 (b11, b12)
- [V] Ahmed et al. (2023) - https://arxiv.org/abs/2301.03797 (b14, b24, c19)
- [V] Hu et al. (2024) Uncertainty of Thoughts - https://arxiv.org/abs/2402.03271 (b15)
- [V] Laban et al. (2025) - https://arxiv.org/abs/2505.06120 (b16)
- [V] Cemri et al. (2025) - https://arxiv.org/abs/2503.13657 (b17)
- [V] Tseng et al. (2026) FaulT-Bench - https://arxiv.org/abs/2608.27021 (c05 to c07, c24)
- [V] NIKA (2025) - https://arxiv.org/abs/2512.16381 (c08, c09)
- [V] Clark et al. (2026) SREGym - https://arxiv.org/abs/2605.07161 (c10, c11, c27)
- [V] Kim et al. (2026) - https://arxiv.org/abs/2602.09937 (c12, c13, c25)
- [M] OpenRCA (2025) - https://microsoft.github.io/OpenRCA (c14, snippet)
- [V] Pei et al. (2025) Flow-of-Action - https://arxiv.org/abs/2502.08224 (c18, d06 to d08)
- [V] Cai et al. (2026) multi-dataset benchmark - https://arxiv.org/abs/2606.29193 (c20, d09, d10, d16)
- [V] Wu et al. (2025) TN-AutoRCA - https://arxiv.org/abs/2507.18190 (c21)
- [V] Zhang et al. (2026) agentic execution faults - https://arxiv.org/abs/2608.14680 (c22)
- [V] Hu and Ash (2026) Chat Debugging - https://arxiv.org/abs/2608.02955 (d11, d12; earlier b19 and c23 were [M])
- [V] Ash and Hu (2026) WIP - https://arxiv.org/abs/2608.02420 (d13)
- [M] arXiv search note, electronics fault benchmarks - https://arxiv.org/search/?query=LLM+electronic+hardware+fault+diagnosis+benchmark (d15, zero hits)
