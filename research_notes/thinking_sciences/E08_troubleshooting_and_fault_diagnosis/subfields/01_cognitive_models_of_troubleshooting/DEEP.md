# Cognitive models of troubleshooting: deep document

*Subfield E08.01. Focus: problem description, causes, test, validate. Key works: Jonassen and Hung 2006; Schaafstal 1993/2000. Evidence ids (a01-a28, b01-b25, c01-c32, d01-d20) and claim ids (E08.01-K01 to K29) refer to the jsonl files in this folder. Status tags: [E] established, [S] single-source, [C] contested. Read critique.md for the weak spots; the main ones are repeated here where they matter.*

## 1. What it is

Troubleshooting is problem solving where the goal state is known (the system should work) but the information needed to get there is not (what is broken). The solver does not choose a goal. The solver must find the fault.

The cognitive-model literature describes this as a short cycle of four tasks:

1. **Formulate the problem description.** What is the system doing, and what should it do?
2. **Generate causes.** List or recall faults that could produce the symptom.
3. **Test.** Is the proposed cause an actual fault?
4. **Repair and evaluate.** Fix it, then check that the whole system now works.

The cycle is recursive, not linear. A refuted cause sends the solver back to generate a new one. A failed repair sends the solver back too (missed fault, or two faults) (a03, K01).

Why it matters for our agent. The four tasks line up with our states: S1 UNDERSTAND (describe), S2 REPRESENT plus S3 GENERATE (causes), S4 TEST (test), S8 VERIFY (evaluate after repair). The field supplies a human account of why this order works and where people fail inside it. It also supplies a growing set of LLM tests on fault tasks (cloud incidents, networks, forum problems, circuits).

Scope. This document covers the cognitive models of the cycle and the LLM work that tests or uses it. Other subfields in this run cover debugging strategies, spectrum-based fault localisation, human error and recovery, case representation, systematicity and information-theoretic motivation. We link to them and do not repeat them.

Honest summary of the state of evidence. The human side is thin on numbers: the founding field study is known from an abstract only, and the main theory paper is an untested design proposal. The LLM side has many numbers but most come from authors' own harnesses, 2024-era models or very small problem sets, and no study compares an explicit describe-causes-test-verify cycle against a plain loop at equal tokens (K29).

## 2. History and theories in depth

### 2.1 Roots: skill, rule, knowledge (Rasmussen 1983)

Rasmussen split control into three levels: skill (signals), rule (signs), knowledge (symbols and a mental model). Fault diagnosis is a knowledge-based task. Knowledge-based control is slow. It is used only when rules fail. Training moves the boundaries between levels (a20). We read this only through a teaching summary (K16, single source).

Read for an agent: try a fast rule or remembered case first. Fall back to slow model-based reasoning only when the fast route fails. This is the same shape as our G1 (doubt only on a signal).

### 2.2 Model-based diagnosis in AI (Reiter 1987; de Kleer and Williams; Davis 1984)

The AI line asks the same question formally. Compare observed behaviour with a model of the device. Derive minimal conflict sets. Pick the next probe to cut the candidate faults most (GDE). Davis argued for reasoning from structure and behaviour, not only symptoms. MYCIN used rules with certainty factors. We did not open these (c31, c32 snippets only), so no numbers are quoted. They matter because the human finding "no model, no prediction" (2.6) is the human twin of "no device model, no conflict set".

### 2.3 Johnson 1988 and the expert-novice line

Johnson (1988) is cited for the finding that experts use ordered operations that cut the number of possible fault locations (a21, reference list only). Van Gog, Paas and Van Merrienboer (2005) used eye movements and verbal protocols on circuit troubleshooting. The abstract (d03) says higher-expertise people spent relatively more time in problem orientation, had shorter fixations there, and fixated more on a major fault-related component. In problem formulation their fixations were longer. The authors call the differences "relatively small". No N or means were visible. Van Gog 2006 and 2008 (process-oriented worked examples help transfer) were only seen in reference lists (a23).

### 2.4 Schaafstal and structured troubleshooting (1993, 2000)

This is the founding applied study. Schaafstal and Schraagen (1993) is the early version (a19, named in a search result only, not read). Schaafstal, Schraagen and van Berlo (2000, Human Factors 42(1), 75-86) did a cognitive task analysis from two observational studies of real troubleshooting plus a literature review. From it they built **structured troubleshooting**: one general strategy plus a multilevel functional breakdown of each system. Navy radar technicians trained this way fixed about twice as many malfunctions, in less time, than traditionally trained ones. The method also needed less training time and gave a more explicit, uniform approach (a01, a02, d01).

What we do not have: N, error counts, effect size, test statistics. Several attempts (Pure, TNO, Crossref, PubMed) returned the abstract only. No independent replication was found. Do not quote more than "about twice as many malfunctions, in less time" (K02, single source).

A second-hand report (a16) adds that a standard course on content understanding did not prepare Navy students to troubleshoot radar, but adding structured troubleshooting gave significant gains. No numbers.

Reading for the agent. The gain is credited to a method plus a system map, not to more domain facts. A scaffold can supply both.

### 2.5 Jonassen and Hung 2006: a design architecture

*Learning to troubleshoot: a new theory-based design architecture*, Educational Psychology Review 18(1), 77-114. We could not read the full text (paywall). From the publisher page and a blog note (a17, a18, d02):

- Troubleshooting is problem solving with a known goal state and missing information.
- Steps: construct the problem space; identify fault systems; diagnose; generate and verify solutions; remember the experience.
- Four levels of hypothesis: system, subsystem, device, component.
- Six knowledge types: domain, system, procedural, strategic, metacognitive, experiential (a05).
- Three search strategies: exhaustive, topographic (follow the signal path), split-half (a06).
- Proposed design: a multi-layered conceptual model of the system (topographic, function, strategic, procedural views), a simulator where the learner must generate, reconcile, test and repair, and a case library of prior troubleshooting stories used with case-based reasoning.

No participants, no scores, no effect sizes. It is a proposal. We found no test of the case-library design (K24). Treat "ask what an expert did before" as a hypothesis (see 5.3 and 4.10).

### 2.6 Physics-education work on circuits (Dounas-Frazer, Lewandowski and colleagues, 2015-2018)

This is the best-opened human data set, and it is small.

- Think-aloud study: 8 student pairs (4 at CU Boulder, 4 at Maine) diagnosing a two-fault cascade amplifier (R3 100 ohm instead of 1 kohm, plus a burned-out op-amp). 2-minute interval coding (a07).
- All 8 pairs went through all four tasks. Most moved from formulate to generate about halfway through. Testing ran almost continuously. Repairs came in short bursts (a07).
- 5 of 8 pairs used split-half. All 5 built a two-subsystem model, predicted each stage's output, compared, and isolated Stage 2 (a08). A pilot (a11, 16 students) notes that without the two-subsystem model a student could not make a prediction.
- Pairs A and B used an exhaustive replace-both-op-amps move after checking wiring and resistors (a08).
- Outcomes: 8 of 8 fixed the resistor, 7 of 8 found and replaced the faulty op-amp, and 5 of 8 made needless or wrong changes (replacing R1, rewiring from a bad schematic mapping, replacing the working Stage 1 op-amp). One pair's swap was driven by recall: "last time it was a bad op-amp" (a09).
- Shared monitoring (socially mediated metacognition) clustered right after measurements of the whole circuit or the first subsystem; four episode types (a12).
- Some students did not propose a cause at the first discrepancy. They kept measuring until a cause emerged. This path was not in the framework (a15, 10 interviews, 2 episodes shown).
- Measurement kinds map to tasks: formative (build the description), diagnostic (test a cause), evaluative (check the repair) (a10). This is the authors' own addition.
- Instructor interviews (N=20, 18 institutions, a13/a14): nearly all value troubleshooting, about half do not assess it, and about half say part of the skill is innate. Experts hold that "nothing works the first time", so faults are expected.

Limits: physics majors in pairs, one circuit, author coding with no inter-rater statistic seen, no outcome comparison among strategies.

### 2.7 Human error and bias from the medical diagnosis line

Medical diagnosis is the closest human analogue with controlled experiments. It tests whether forcing a second look fixes bias. See 5.3 and 5.4. The parallel subfields ("Human error and recovery", "Cognitive breakdowns", "Knowledge organisation: illness scripts") are covered elsewhere.

### 2.8 The LLM era (2023-2026)

Three kinds of work arrive.

1. **Benchmarks that mirror the cycle.** AIOpsLab (detect, localize, root-cause, mitigate), ITBench, NIKA, FaulT-Bench, RCAEval.
2. **Agents that encode the cycle.** RCAgent, RCACopilot, Flow-of-Action (SOP-guided), SADE (a phase-gated Cisco method), SIA (evidence-first, competing hypotheses, counterfactual critic), UoT (information-gain questions).
3. **General results that bear on one step.** Self-correction (Huang, Kamoi, Olausson), clarifying questions (MediQ, QuestBench, BED-LLM), multi-turn loss (Laban), bias cues (Schmidgall), failure taxonomy (MAST).

Section 6 gives the numbers.

## 3. Core findings with exact numbers

Status is [E] established, [S] single-source, [C] contested, as in claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Structured troubleshooting (general method + system breakdown) beat content-only training | About 2x malfunctions fixed, less time, less training time. No N or effect size seen | Schaafstal et al. 2000 (a01, a02, d01) | [S] |
| Real troubleshooting follows a four-task recursive cycle | 8 of 8 pairs went through all four tasks; refuted cause and failed repair both loop back | Dounas-Frazer 2016 (a03, a07) | [E] (2 sources, small N) |
| Split-half needs a system model and a stated prediction | 5 of 8 pairs used split-half; 5 of 5 built a two-subsystem model and predicted each stage | Dounas-Frazer 2016, 2015 (a08, a11) | [E] (small N) |
| Recall of a past fault causes needless repairs | 5 of 8 pairs made needless or wrong changes; 7 of 8 found the op-amp; 8 of 8 fixed the resistor | Dounas-Frazer 2016 (a09) | [S] |
| Experts orient longer and fixate on the fault-related part | "Relatively small" differences; no numbers in abstract | Van Gog 2005 (d03) | [S] |
| ReAct agent equals strong baselines on correctness but hallucinates far less | Correct: ReAct 35% vs 39% (CoT, RB k=10). Hallucination: ReAct 4%, CoT 12%, RB 40%. 500 incidents, GPT-4 | Roy 2024 (b01, c06) | [C] |
| Most ReAct failures are too little evidence | 66% of ReAct wrong predictions were "insufficient evidence" | Roy 2024 (b02) | [S] |
| Adding past engineers' discussion comments did not help | C-BLEU -0.13, S-BLEU -0.39, METEOR -0.7, rougeL -1 for one model; +0.1 rougeL for another | Roy 2024 (b03) | [C] |
| Cloud fault accuracy falls from detect to cause to fix | Overall: FLASH 59.32%, ReAct 55.93%, GPT-4 shell 49.15%, GPT-3.5 shell 15.25%. Detection 100/76.92/69.23/23.07. RCA FLASH 36.36, ReAct 45.45, GPT-4 40.90, GPT-3.5 9.09. About 11-13 problems per level, one run | AIOpsLab (c01, c02, b08) | [S] |
| Step budget effects differ by agent | FLASH peaks 59.32% at limit 20; ReAct also improves; GPT-3.5 flat beyond 5 steps | AIOpsLab (c04, d10; corrected in critique) | [S] |
| Agents report faults on healthy systems | AIOpsLab Noop (N=2): 1 of 4 agents correct. FaulT-Bench: over-diagnosis 24% (51/210) SADE, 16% (33/209) ReAct, 11% (21/198) Claude-Code baseline | AIOpsLab (c05, d10); FaulT-Bench (a25, d04) | [E] (2 sources) |
| Over-diagnosis depends on how checkable the ticket is | Same 72 healthy networks: 17% standard, 16% naive, 31% novice, 28% novice-confident, 35% naive-unsure, 47% no-detail. One baseline: 7% to 74% | FaulT-Bench (d05) | [S] |
| Structured, phase-gated diagnosis beats plain ReAct, but not at equal tokens | SADE F1 0.77 vs 0.55 same-backbone vs 0.44 ReAct (0.40 in Fig. 1). Median input tokens 344k vs 189k vs 55k. Flow-of-Action 64.01% vs ReAct 35.50%, CoT 32.61%, Reflexion 29.06% | SADE (b16, d06, d07); Flow-of-Action (c17) | [E] (own harnesses) |
| SIA evidence-first loop beats ReAct, with overlapping intervals | Final /100: SIA 79.2 [72.7, 83.7], ReAct 69.0 [60.5, 77.0], ToT 61.5 [52.5, 70.0], direct 67.3 and 67.5. 100 cases. Other backbones +6.2 and +7.7 | SIA (b12, d08) | [S] |
| Candidate generation limits success more than selection | SIA potential 89.2 vs final 79.2; ToT 84.0 vs 61.5 (gap 22.5). No hypothesis expansion: final 76.5, potential 79.3 | SIA (b13, b14) | [S] |
| Component ablation of the evidence-first loop | Full 79.2; no structured investigation 72.8; no counterfactual critique 74.0; no follow-ups 75.0; no adjudication 76.0; no expansion 76.5; no weight updates 78.5 | SIA (b14) | [S] |
| Information-gain question choice raises success | UoT GPT-4 troubleshooting 43.7% to 67.3% (+23.6 points); beats CoT-SC by 33.8% and Reflexion by 29.9%; average +38.1% across 5 datasets | UoT (a24) | [E] (with BED-LLM, below) |
| Code-computed information gain beats LLM-picked questions | BED-LLM, 20 Questions, 6 LLMs: +37.4 points over prompt-only. Example GPT-4o Animals: 93 (BED-LLM) vs 70 (implicit maximisation, same candidates) vs 83 (equal split) vs 45 (prompt-only); column labels inferred | BED-LLM (d11) | [S] |
| LLMs fail to pick the right clarifying question | 40-50% on Logic-Q and Planning-Q | QuestBench (d13) | [S] |
| Always asking hurts, gated asking helps | Plain asking -11.3%; abstention with rationale + self-consistency +22.3%; 10.3% gap to full information | MediQ (d12) | [S] |
| Observation quality limits diagnosis | GPT-4o diagnosis pass@1 13.81% (appendix says 18.10%) with traces vs 9.52% without; by chain length 36%, 7.73%, 5.0% (Easy, Medium, Hard) | ITBench (b10, b11) | [S] |
| Intrinsic self-correction does not help | GPT-4 GSM8K 95.5 to 91.5 to 89.0 by calls (1, 3, 5); oracle 97.5. GPT-3.5 CSQA 75.8 to 38.1 | Huang 2024 (c19, c20) | [E] |
| Prompted self-feedback shows no fair gain except where checking is easier than generating | Survey, no pooled effect | Kamoi 2024 (d14) | [E] |
| Immunisation exercise helps residents on bias-exposed cases only | N=91: 0.40 vs 0.24 (diff 0.16, CI 0.05 to 0.27, p=0.004); unbiased 0.36 vs 0.41 (p=0.45) | Mamede 2020 (b19, d15) | [S] |
| Disease knowledge predicts bias susceptibility | N=62: biased diagnoses 0.35 vs 0.97 per participant (diff 0.62, CI 0.28-0.95, p=0.001) | Mamede 2021 (b20) | [S] |
| Guided reflection did not raise strict final accuracy | N=186: 0.47 / 0.42 / 0.41 (F(2,173)=0.841); lenient scoring 0.47 / 0.70 / 0.72 (eta-sq 0.18); short condition 16 corrected vs 26 backfired | Lambe 2018 (b21, d16) | [C] |
| Reflection after exposure did not repair availability bias | N=46: control 0.80 vs 0.59; exposed 0.66 vs 0.64 (p=0.756) | PMC7807127 (b22) | [C] |
| Clinician-style prompts do not help a strong model | GPT-4 CoT 76, intuitive 77, differential 78, analytic 78, Bayesian 72 (none significant). GPT-3.5 differential 38 vs CoT 46 (-8, p<0.001) | Savage 2024 (c22, c23) | [S] |
| LLMs commit early under piece-by-piece information | 39% average drop multi-turn vs single-turn (aptitude -15%, unreliability +112%), 15 LLMs | Laban 2025 (d17) | [S] |
| Planted bias cues lower LLM accuracy | 10-26% by model; false consensus 24.9%, frequency 18.2%, recency 12.9%, confirmation 8.1%; GPT-4 unbiased 72.7% | Schmidgall 2024 (d18) | [S] |
| Case libraries cover only part of faults | 163 of 653 incidents (24.96%) had a new root-cause category; 93.80% of recurring incidents reappear within 20 days | RCACopilot (d19) | [S] |
| Retrieval of similar past incidents as examples | RCACopilot Micro-F1 0.766, Macro-F1 0.533 (GPT-4); GPT-4 no examples 0.026 | RCACopilot (c09, d19) | [S] |
| Multi-agent failures are mostly repetition and missed completion | Step repetition 15.7%, no completion recognition 12.4%, ignoring requirements 11.8%, derailment 7.4%, wrong assumptions 6.8%; verification step +15.6% on ProgramDev | MAST (c28, c29) | [E] |
| Fixed pipeline (localize, repair, validate) beat open agents on SWE-bench Lite at the time | 32.00% (96 of 300) at $0.70 per issue | Agentless (c24) | [S] |
| Tool-using prompting often not better than no-tool baselines at far more tokens | Abstract-level; 50-error review: 60% wrong tool input in retrieval | Jacovi 2023 (d20) | [E] |
| Misleading user conjecture mostly absorbed when logged as hypothesis | 10 cases: final 80.0 vs 76.0; wrong cause chosen 2 of 10 | SIA (b15, d09) | [S] |

## 4. Mechanisms and models

Each mechanism is written so an engineer can wire it.

### 4.1 The four-task cycle with back-edges

State machine with four nodes and two required back-edges.

- `DESCRIBE` -> `CAUSES` -> `TEST` -> `REPAIR_EVAL`.
- Back-edge A: `TEST` result "cause refuted" -> `CAUSES` (pick next candidate or generate new ones).
- Back-edge B: `REPAIR_EVAL` result "system still not as expected" -> `CAUSES` (missed fault or multiple faults).
- Exit: `REPAIR_EVAL` passes on a whole-system check, or a "no fault found" verdict is justified by a check (see 4.7).

Implementation: code owns the state and the transitions. The model fills the content of each node. Each node's output is a short structured record, not free text. The three measurement kinds from a10 fit as tags: formative (in DESCRIBE), diagnostic (in TEST), evaluative (in REPAIR_EVAL).

Caveat. The human evidence that people do this is 8 pairs on one circuit. The LLM evidence that imposing it helps is SADE, Flow-of-Action and SIA, none at equal tokens.

### 4.2 Problem description (formulate)

Humans (as coded in a07) spend about the first half of a session in description before the first causes. Experts spend relatively more time orienting and fixate on the fault-related part (d03). Some solvers keep observing until a cause emerges (a15).

Implementation: before any cause list, require three fields. Expected behaviour. Observed behaviour. The nearest checkable difference between them. Ask for a measurable fact when none is given. FaulT-Bench shows why: with the same healthy networks, over-diagnosis rises from 17% (standard ticket) to 47% (no identifiers) (d05). A report with nothing checkable pushes the agent to blame a benign anomaly.

Observation access also bounds quality: ITBench diagnosis fell from 13.81% to 9.52% when traces were removed (b11).

### 4.3 Cause generation: recall route and model route

Two routes (a04, a20). Recall: match symptoms to a past fault. Fast. Wrong on novel faults, and in the circuit study it drove a needless swap. Model: reason from function and structure. Slow. Works without experience.

Implementation: try a memory lookup first (cheap). Accept a recalled cause only as a **hypothesis** that must survive a refuting test (4.5). If the lookup has no hit or the test refutes it, go to the model route. RCACopilot gives the coverage rate to plan for: about a quarter of incidents are new (d19).

### 4.4 Breadth of candidates

SIA's ablation: without hypothesis expansion, potential fell from 89.2 to 79.3 and final from 79.2 to 76.5 (b14). ToT had a 22.5-point gap between potential (84.0) and final (61.5) (b13). Reading: getting the true cause onto the list is half the job, and picking it is the other half. Report both numbers in any test, as SIA does ("potential" is an oracle over recorded candidates).

Implementation: generate candidates in separate calls (matches S3: each attempt in a fresh context). Log whether the true cause was ever listed. Code merges and de-duplicates.

### 4.5 Test selection: split-half, topographic, exhaustive

Three strategies (a06):

- Exhaustive: test every candidate in turn.
- Topographic: follow the signal path upstream or downstream.
- Split-half: test the midpoint of the chain and keep the bad half.

Split-half works only with a model that predicts the output at the midpoint (a08, a11, K03). Without a model, people fall back to exhaustive replacement.

Information-gain version (UoT, BED-LLM): given candidate faults with weights, pick the probe whose possible outcomes split the weight most evenly (maximum expected information gain). Compute it in code from outcome tables. The LLM's role is to propose candidates and outcome predictions, and to read results. In BED-LLM, code-computed gain beat the LLM picking among the same candidate questions (93 vs 70 in one cell, inferred labels) (d11). Not yet tested on fault graphs (K22).

Implementation sketch.
1. LLM proposes candidate faults with prior weights, and for each probe a predicted outcome per fault.
2. Code computes, for each probe, the entropy of the outcome distribution. Choose the max (or the median split on a chain).
3. Run the probe. Code updates weights by zeroing faults whose prediction mismatched (hard) or down-weighting (soft).
4. Repeat until one fault holds the mass or the budget is hit.

Every refuting test must be real output, not model opinion (G2, G10).

### 4.6 Verify after repair

The evaluative step asks "is the whole apparatus functioning as expected?", not "did my part change?" (a03). Three human findings support a separate step. 5 of 8 pairs made wrong or needless changes (a09). A failed repair loops to causes (a03). Multiple faults occur (the circuit had two).

Implementation: verification is a fresh system-level check on something the repair was not fitted to (G3). Failure re-opens CAUSES with the failing output attached (G2).

### 4.7 The "no fault" exit

Agents report faults on healthy systems: 11-24% of answered runs on FaulT-Bench, up to 74% for one baseline with no-detail tickets, and 3 of 4 agents failed AIOpsLab's 2 no-fault problems (d04, d05, d10). The phase-gated SADE agent was best grounded (0.933 vs 0.845) yet had the highest false-alarm rate (24% vs 16% and 11%) (K21). Structure helped localisation, not the stopping decision.

No study tests a fix. A candidate rule: a fault verdict needs at least one test that distinguishes "fault" from "benign condition". Absent that, return "no fault found, here is what was checked". This rule must be reconciled with G6 (never abstain on the first pass): a "no fault found" answer is a submitted answer, not an abstention, and it applies only to items where a healthy-system outcome is possible.

### 4.8 When to ask or reflect: signal-gated

Evidence converges on gating. Always-asking cost 11.3% (MediQ), confidence-gated asking gave +22.3% (d12). Always-on guided reflection did nothing for strict accuracy in students and backfired 62% of the time in the short condition (d16). Reflection after bias exposure did not repair it (b22). Kamoi finds gains from self-feedback only with external feedback (d14). Mamede and Schmidt report gains for experienced residents on hard cases and harm for novices on hard cases, depending on how reflection is instructed (b23).

Implementation: trigger a structured second look only on a code-detected signal (a test result that contradicts the leading hypothesis, two probes with no change in weights, the same error twice). This is G1. It has not been tested on faults.

### 4.9 Loop and completion control

MAST: step repetition 15.7%, not recognising task completion 12.4% (c28). AIOpsLab shows repeated API calls, invented APIs, apologise-and-retry loops and raw-telemetry dumps (c04). RCAgent needed JSON repair and observation snapshots to stabilise ReAct (b07): pass rate 99.38% in 15 steps with the fixes; sampling alone reached 70.19% pass and 44.80% invalid.

Implementation: code detects repeated identical calls, truncates telemetry to a summary plus a pointer, validates tool-call format before running, and ends the run when a completion test passes.

### 4.10 Case memory

Humans: experiential knowledge is one of six knowledge types (a05), and recall is the fast route (a04). LLMs: past discussion comments did not help (b03), retrieval gave small lexical gains (b05), generic outputs were a failure mode (b06). RCACopilot's retrieval of similar past incidents as few-shot examples produced strong F1 against a no-example prompt (0.766 vs 0.026) but its case base cannot cover the 24.96% of new categories (d19). No human-judged test of a case library exists (K17).

## 5. What holds up

### 5.1 Replicated or supported by more than one source

- The four-task cycle is a good description of human practice, with loop-backs (K01). Sources: Dounas-Frazer 2016, 2017, 2018, plus the cycle taken from Schaafstal. The N is small. The independence is limited because the later papers cite the first.
- Probe choice by information gain helps (K09). UoT, SIA's follow-up ablation and BED-LLM point the same way. All are LLM and simulation work.
- Without an external signal, self-correction does not help (K12). Huang, Kamoi, Olausson, and the clinical-reflection nulls agree.
- Agents give false alarms on healthy systems (K05). AIOpsLab and FaulT-Bench agree. The fix is untested.
- Multi-agent failures are dominated by repetition and missed completion (K18).
- Tool-using prompting is often not better than no-tool baselines at orders of magnitude more tokens (Jacovi 2023, K29).

### 5.2 Single-source or unreplicated

- Structured troubleshooting doubles faults fixed (K02): one abstract.
- Recall causes needless repairs (K04): 8 pairs.
- Insufficient evidence is 66% of ReAct failures (K07): one organisation.
- Candidate breadth matters more than selection (K08): one paper, one backbone for the ablation.
- Observation quality (K11): ITBench, with an internal inconsistency (13.81 vs 18.10).
- The 2026 gains (K28): SADE and FaulT-Bench share authors and use gpt-5-mini as judge. SIA uses its own LLM rubric and user simulator. Its margin over ReAct has overlapping 95% intervals, although it holds on two other backbones (+6.2, +7.7).

### 5.3 Failed or contested results

- ReAct vs simple baselines (K06). Roy: ReAct 35% vs 39%. SIA: ReAct 69.0 vs direct 67.3 and 67.5. Against that, SADE reports ReAct 0.44 F1 vs 0.77 for a structured agent, and Flow-of-Action 35.50% vs 64.01%. Reading: free ReAct is no better than direct prompting, but a phase-gated or SOP-guided agent is far above both. The structure matters, not the tool loop.
- Case retrieval (K17). Small or negative lexical changes (Roy, Ahmed). Strong F1 in RCACopilot. They measure different things.
- Reflection (K13). Mamede 2020 helps (but it is an immunisation exercise, not in-the-moment reflection). Lambe 2018 and PMC7807127 find nothing. The review says the effect depends on instruction.
- Extra steps: GPT-3.5 flat beyond 5 steps; ReAct and FLASH improve to 20.
- Jonassen and Hung's case-library proposal: untested (K24).

### 5.4 Moderators

- Expertise: reflection helps experienced residents on hard cases, can hurt novices on hard cases (b23). Novices may already reason analytically (b21).
- Scoring rule: lenient scoring (right cause anywhere in a list) made reflection look useful (0.47 to 0.70-0.72). Strict final accuracy did not move (d16, K26). Always score the final selected cause. Report potential and final separately.
- Ticket quality: over-diagnosis 17% to 47% on the same healthy networks (d05).
- Observability: removing traces cut diagnosis (b11).
- Complexity: propagation-chain length cut diagnosis from 36% to 5% (b11).
- Model strength: GPT-3.5 lost 8 points with a differential-diagnosis prompt, GPT-4 did not change (c23, c22). The AIOpsLab GPT-3.5 shell agent scored 15.25% overall.

### 5.5 Interventions that worked and did not

Worked (with the caveats above): method plus system breakdown in human training (a01); phase-gated or SOP-guided policy (b16, c17); evidence-first loop with counterfactual critic (b14); information-gain question choice (a24, d11); confidence-gated asking (d12); objective verification step (+15.6%, MAST ProgramDev, c29); fixed localize-repair-validate pipeline with reproduction tests (c24); JSON repair and observation snapshots for ReAct stability (b07).

Did not work or hurt: unstructured self-critique (c19); always-on guided reflection (d16); always-asking (d12); adding past discussion comments (b03); clinician-style differential prompt on a weaker model (c23); bias warnings only partly (d18: GPT-4 frequency bias 0.627 to 0.720, below the no-bias level).

### 5.6 Matched-token gap

SADE median input tokens: 344k vs 189k same-backbone baseline vs 55k ReAct (d07). SIA asks 5.2 questions vs 2.8 for ReAct (b12). So the structured arms in both papers spent more. No paper tests the cycle at equal tokens. This is the main reason we cannot call the cycle's benefit established for our agent (G7).

## 6. Language models

### 6.1 Benchmarks and baselines

| Study | Task | Result |
|---|---|---|
| AIOpsLab (c01-c05) | 48 injected faults, 4 levels | Overall FLASH 59.32, ReAct 55.93, GPT-4 shell 49.15, GPT-3.5 shell 15.25. Detection 100 / 76.92 / 69.23 / 23.07. Mitigation GPT-4 27.27, GPT-3.5 0. Localization acc@1: GPT-4 61.54, ReAct 53.85, FLASH 46.15, classic PDiagnose 15.38, RMLAD 7.69. About 11-13 problems per level, one run. |
| ITBench (b10-b11, c12-c14) | 94 scenarios (SRE 42, CISO 50, FinOps 2) | SRE handling 13.8%, CISO 25.2%, FinOps 0%. GPT-4o diagnosis pass@1 13.81%. Nondeterministic: one scenario diagnosed in 1 of 10 runs, another 6 of 10, another 8 of 10. |
| Roy 2024 (b01-b04) | 500 real incidents | ReAct 35% vs 39%; hallucination 4% vs 12% vs 40%; 66% of ReAct errors are insufficient evidence. |
| RCACopilot (c09, c10, d19) | A year of Microsoft incidents | Micro-F1 0.766 (GPT-4), 0.761 (GPT-3.5). |
| RCAgent (b07, c11) | Alibaba Flink Advisor | Pass rate 99.38% in 15 steps; METEOR +8.71 over ReAct, +3.16 without expert agents. |
| FaulT-Bench (a25, d04, d05) | 200 network scenarios, 3 agents, 3,960 runs | Accurate ticket: 0.912 / 0.942 / 0.941. Healthy network, false ticket: mean 0.820. Naive no-detail persona: 0.497 mean (Claude Code 0.283). |
| NIKA (a27) | 54 issues, 640 tasks | Benchmark only; comparison not read. |
| SADE (b16, b17, d06, d07) | 523 held-out incidents | F1 0.77 / 0.55 / 0.44; detection 0.85 / 0.67 / 0.68; no-submission 4.2% / 15.3% / 8.8% (SADE / Claude-Code / ReAct); tool calls per correct submission 27.2 / 51.5 / 49.5; cost per session about $1.44 / $0.83 / $0.20. |
| SIA (b12-b15, d08, d09) | 100 forum cases | Final 79.2 vs 69.0 ReAct vs 61.5 ToT. Other backbones +6.2, +7.7. |
| Flow-of-Action (c17, c18) | Root cause, GPT-4-Turbo | 64.01% vs ReAct 35.50%. Action-set removal hurt most. |
| UoT (a24) | FloDial troubleshooting, 894 dialogues, 153 faults | GPT-4 43.7% to 67.3%; mean 7.8 turns in successes. Simulated user is GPT-4; fault set given. |
| Kang 2024 (c15) | 798 real bugs | Method-level acc@1 up to 233.3% higher than baselines. Software, outside human-cognition core. |
| Agentless (c24, c25) | SWE-bench Lite | 32.00% at $0.70 per issue. |
| Consumer repair (a28) | 991 questions, 6 LLMs | Abstract only. |

### 6.2 What changed the result, and by how much

- **Phase gating or an SOP** on the same backbone: +21.5 F1 points (SADE vs Claude Code baseline); Flow-of-Action +28.5 points over ReAct (64.01 vs 35.50). Cost: more tokens (K10).
- **Evidence-first loop** with competing hypotheses and a counterfactual critic: +10.2 over ReAct (79.2 vs 69.0) on one backbone, +6.2 to +7.7 on two others. Each component removed cost 0.7 to 6.4 points.
- **Information-gain question choice:** +23.6 points on troubleshooting (UoT, GPT-4); +37.4 mean over prompt-only in 20 Questions (BED-LLM).
- **Gated asking:** +22.3% vs a 11.3% loss for always-asking (MediQ).
- **Stability fixes:** pass rate from 70.19% to 99.38% (RCAgent).
- **Objective verification:** +15.6% task success on ProgramDev (MAST).
- **Self-critique alone:** GPT-4 GSM8K 95.5 to 89.0 (Huang).
- **Past case comments:** small or negative (Roy).
- **Ticket vagueness:** over-diagnosis 17% to 47% (FaulT-Bench).
- **Observability:** 13.81% to 9.52% without traces (ITBench).

### 6.3 Behaviours seen in LLM troubleshooters

- Report a fault on a healthy system (K05).
- Commit early and then rely on that answer (39% multi-turn drop, Laban).
- Follow planted cues (10-26% loss, Schmidgall). SIA reduced this by logging user conjectures as hypotheses (wrong cause picked 2 of 10).
- Repeat calls, invent APIs, apologise and retry (AIOpsLab, MAST).
- Fail by lacking evidence, not by inventing it (66%, Roy).
- Do not express uncertainty: GPT-4 0 of 80 vs humans 7 of 80 (Olausson, c27).
- Pick the wrong clarifying question 50-60% of the time on logic and planning tasks (QuestBench).

### 6.4 Quality warnings

All reported gains in 2026 papers come from authors' own harnesses, judges and simulated users (K28). ITBench and SADE contain internal number conflicts (13.81 vs 18.10; 0.40 vs 0.44). The UoT "38.1%" is an average across datasets, not the troubleshooting move (+23.6 points absolute). AIOpsLab has about 11-13 problems per level and one run. Treat sizes as direction, not as effects we can expect.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of the schema. States named: S1 UNDERSTAND, S2 REPRESENT, S3 GENERATE, S4 TEST, S5 REVISE, S7 SELECT, S8 VERIFY, S9 LOOK BACK. No operator (O1-O8) is new here; split-half is a kind of O3 Decompose and could be a code-controlled variant.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Treat the cycle as a loop, not a line: a refuted cause or failed final check re-opens cause generation, with the failing output attached | S4 -> S5/S3, S8 -> S5 | [E] | a03, a07, a12, K01 |
| A2 | No revision from the model's opinion alone: re-open causes only on a real failing output; no intrinsic self-critique round | G2, G10 | [E] | c19, c20, d14, c26, K12 |
| A3 | Do not run always-on reflection, probing or asking; fire them on a signal | G1 | [E] for the rule (consistent with G1); the troubleshooting-specific test is open | d12, d16, b22, d14, K13, K23 |
| A4 | Final check is a system-level test on something the fix was not fitted to | G3, S8 | [E] | a03, a09, c29, c24 |
| A5 | Loop and completion control in code: repeat-call detector, tool-call format check, telemetry truncation, completion test | G2, S4 | [E] | c28, c04, b07, K18 |
| A6 | Score the final selected cause strictly; log "true cause ever listed" (potential) separately | evaluation, G7 | [E] (method) | d16, b13, K26 |
| A7 | Ask for a checkable fact when the description has none; do not accept a vague description as a basis for a fault verdict | S1 | [E] direction (one data set, d05); cheap, so add | d05, K20 |
| A8 | Probe choice among candidates by expected information gain or split-half, computed in code from outcome tables the model supplies | G5, S4 | [E] for the principle (3 sources); not tested on fault graphs | a24, d11, b14, a08, K03, K09 |
| A9 | Cost accounting: every phase-gated structure is compared at equal tokens | G7 | [E] | d07, d20, K29 |

Notes: A8 is established for question choice in 20 Questions and troubleshooting dialogues. The fault-graph version is still a test (U3 in UNKNOWNS.md). A3, A7 and A8 overlap other schema parts; check SCHEMA.md before adding to avoid duplicates. A7 rests on one source (d05) and is listed under Add now only because it costs almost nothing; if the schema owner prefers a strict rule, move it to Test first.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | The four-task cycle as a prompt vs plain ReAct vs direct at equal tokens | S1-S4 | [S]/[C] | b16, c17, b12, K10, K29 |
| T2 | "No fault found" exit plus verify gate: false alarms vs missed faults | G3, S8 (and G6 reconciliation) | [S] problem measured, fix untested | a25, c05, d04, d05, K05, K21 |
| T3 | Code-computed probe choice vs LLM-chosen probe on a component graph | S4, G5 | [S] | d11, d13, a24, K22 |
| T4 | Recall-first with a mandatory refuting test before repair | memory, G3 | [S] | a09, d17, d18, K04, K27 |
| T5 | Signal-triggered vs always-on reflection | G1 | [C] | b19, b21, d12, d16, K13 |
| T6 | A "get more evidence" exit instead of a forced verdict | S4, G6 | [S] | b02, K07 |
| T7 | Candidate breadth at equal tokens (potential vs final) | S3 | [S] | b13, b14, K08 |
| T8 | Method scaffold vs added domain notes | S1-S4 | [S] | a01, a16, K02 |
| T9 | Case library with human-judged output | memory | [C] | b03, b05, d19, K17, K24 |
| T10 | User-supplied conjecture logged as a hypothesis in a marked block | S1 | [S] | b15, d09, d18 |
| T11 | Extended observation before first cause | S1 | [S], 10 interviews | a15, K19 |
| T12 | Per-scaffold step-budget sweep | G11, G12 | [S] | c04, d10, K15 |

Do not add to SCHEMA.md anything in "Test first" until its test passes (see UNKNOWNS.md).

## 8. Concrete tests on our bench

All tests: both (or all) arms get the same token cap per item (sum of input and output, including setup, G7). Run each item at least 3 times per arm because ITBench shows run-to-run swings (1/10 to 8/10 on a single scenario). Use a judge from a different model family than the agent, and check a sample by hand (K28).

Assumed item pool: (a) fault-injection items with a component graph and executable probes (small circuits, service graphs, or network emulations); (b) forum-style diagnosis items with a simulated user; (c) healthy-system items where the right answer is "no fault". If the bench lacks (a) or (c), build a small set first (see UNKNOWNS.md).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| 1 | Fault items with probes (a) | Direct; plain ReAct; four-task cycle with back-edges and code-owned transitions | Final root-cause accuracy (strict); true-cause-listed rate; tokens used | Cycle beats ReAct by 0 to 10 points; direct may tie ReAct (SIA, Roy). If the cycle wins only when given more tokens, drop it |
| 2 | Mixed: 70% faulty, 30% healthy (a)+(c) | Cycle with no "no-fault" exit; cycle with exit plus verify gate | False-alarm rate on healthy items; detection rate on faulty items | False alarms fall from about 20% toward 10% with no more than 3 points of lost detection (assumption, no prior study) |
| 3 | Component-graph items (a) with 8 to 30 components | LLM chooses probe; code-computed split-half or information gain over LLM-supplied outcome tables | Probes to isolation; accuracy at fixed probe count | Fewer probes, same or better accuracy. BED-LLM suggests a large gain on 20 Questions; expect smaller on faults |
| 4 | Items where a past-case memory contains a similar but wrong fault | Recall-then-act; recall-then-refuting-test-then-act | Needless actions per item; final accuracy | Needless actions fall; the human data (5 of 8) suggests the base rate is high |
| 5 | Items with a surprise (test contradicts the lead hypothesis) | Always-on reflection after every step; signal-triggered reflection; none | Accuracy; tokens | Signal-triggered >= none > always-on (MediQ pattern) |
| 6 | Items where the first evidence is insufficient | Forced verdict at step k; abstain-and-probe exit (bounded by G6: final submit still required) | Final accuracy; fraction of forced wrong verdicts | Fewer unsupported verdicts; roughly 66% of ReAct errors are insufficient evidence |
| 7 | Items with a hidden true cause; vary candidate count (3, 6, 12) | Fixed token cap for all | Potential (true cause listed) and final accuracy | Potential rises with breadth; final peaks then falls as selection degrades (ToT pattern) |
| 8 | Domain items with documented procedures | Method scaffold; method-free + added domain notes of equal length | Accuracy | Method wins if the Schaafstal result transfers; domain notes win if the model already knows the method |
| 9 | Items with vague, confident-wrong, and checkable descriptions | Raw description; S1 rewrite that extracts checkable facts and moves guesses into a marked block | Over-diagnosis on healthy items; accuracy on faulty | Over-diagnosis falls on vague descriptions; little change on standard ones |
| 10 | Items with recurring and novel faults (75% / 25%) | No memory; memory lookup as hypothesis only; memory lookup as answer | Accuracy split by recurring vs novel; human-judged answer quality on a sample | Memory helps recurring, hurts novel when taken as an answer |
| 11 | Step-budget sweep (5, 10, 20, 40) on arms from test 1 | Same | Accuracy vs tokens per arm | Plateau point differs per arm (AIOpsLab) |

Report with every test: n items, runs per arm, judge family, strict and potential scores, tokens per arm, and a paired confidence interval.

## 9. What does not transfer, and why

- **Hardware replacement as a repair.** Humans swap parts and see the effect. In software or text tasks, a fix has a different cost model, and "needless repair" means something else.
- **Eye-movement and orientation findings (Van Gog).** The measure is human gaze. The cue that matters for the agent (spend explicit effort on description first) is a design choice, not a measured effect, and the effect was "relatively small".
- **Pair talk and socially mediated metacognition (Dounas-Frazer 2017).** Our agent is one model. G9 rules out debate between agents. The monitoring role must be played by code checks, not a second voice.
- **Case-based learning from experience.** Humans build experiential knowledge across years (the Azure team said RCA needs over 1.5 years of experience, b04). An agent has a library and a lookup. The library covers the recurring part only; 24.96% of incidents were new (d19).
- **Instructor beliefs ("nothing works the first time").** Self-report from 20 instructors. No performance link.
- **Medical reflection studies.** Residents and students on fictional vignettes. They show the shape (conditional, scoring-sensitive) but not the size for a model.
- **Clinician-style prompts.** No reliable gain for GPT-4 on MedQA; negative for GPT-3.5. Do not assume reasoning-style prompts carry over.
- **Working-memory reasons for sequencing.** An LLM can hold all four tasks in context at once. The human reason for sequencing (limited working memory) may not apply. The sequencing may still help by forcing outputs to be checkable, but that is a separate reason and needs the test in 8.1.
- **Software fault localisation (Kang, Agentless).** Code has tests and compilers that give strong feedback. AIOpsLab authors note operations feedback is weak by comparison. Gains there will not carry over to settings without an executable check.
- **LLM-judged forum diagnosis.** SIA's score is an LLM rubric and a simulated user. It measures how the agent talks to a simulator as much as diagnosis.

## 10. Open questions

1. Does an explicit describe-causes-test-verify cycle beat a plain ReAct loop at equal tokens on the same fault set? (K29, the missing direct test.)
2. Does a "no fault" exit plus verify gate cut over-diagnosis without losing true detections? Phase-gated structure alone raised false alarms (24% vs 11%).
3. Does code-computed split-half or information gain beat LLM-chosen probes on realistic fault graphs?
4. What are the exact N, error counts and effect sizes in Schaafstal et al. 2000? Did anyone replicate? Could not be reached.
5. What does Jonassen and Hung 2006 report in its body? Has its case-library design been tested?
6. When is forced reflection helpful vs harmful for LLMs? Signal-triggered vs always-on has not been tested on faults.
7. Do case libraries help LLM agents when judged by humans rather than lexical metrics?
8. How much does recall-first diagnosis cause needless repairs in LLMs compared with humans (5 of 8 pairs)?
9. What numbers do Van Gog 2005-2008 give for orientation time and worked examples?
10. Are SADE, SIA and FaulT-Bench results reproducible with independent judges and a different author group?
11. Is the "insufficient evidence" share of ReAct failures (66%) stable across models released after 2024?
12. Does the benefit of the cycle shrink as the base model gets stronger (GPT-4 did not gain from clinician prompts)?
13. Do the six knowledge types (a05) predict anything separately, or is the taxonomy only descriptive?

## 11. Sources

[V] = opened and read this session (page, abstract page or full text, as the evidence file records; for several human-study sources only the abstract was available, noted). [M] = snippet or reference list only.

Human and theory
- [V] Schaafstal, Schraagen, van Berlo (2000) Cognitive task analysis and innovation of training: the case of structured troubleshooting. https://research.utwente.nl/en/publications/cognitive-task-analysis-and-innovation-of-training-the-case-of-st/ (abstract only)
- [V] Same, PubMed abstract. https://pubmed.ncbi.nlm.nih.gov/10917147/
- [M] Same, DOI not verified. https://doi.org/10.1518/001872000779656624
- [M] Schaafstal and Schraagen (1993) Training of systematic diagnosis: a case study in electronics (pp 529-533). No URL.
- [V] Jonassen and Hung (2006) Learning to troubleshoot, publisher page and abstract only. https://link.springer.com/article/10.1007/s10648-006-9001-8
- [V] Jonassen and Hung (2006), blog note. https://peixian.github.io/posts/jonassen_and_hung_learning_to_troubleshoot_a_new_theory_based_design_architecture
- [V] Rasmussen (1983) Skills, rules and knowledge, teaching summary. https://www.smithsrisca.co.uk/PSYrasmussen1983.html
- [M] Johnson (1988) Cognitive analysis of expert and novice troubleshooting performance. No URL.
- [V] Van Gog, Paas, Van Merrienboer (2005) abstract via Crossref. https://doi.org/10.1002/acp.1112
- [M] Van Gog et al. (2006, 2008) worked examples for troubleshooting. No URL.
- [V] Dounas-Frazer et al. (2016) Investigating the role of model-based reasoning while troubleshooting. https://arxiv.org/abs/1603.03684
- [V] Dounas-Frazer et al. (2015) The role of modeling in troubleshooting. https://arxiv.org/abs/1507.03939
- [V] Dounas-Frazer et al. (2015) The role of metacognition in troubleshooting. https://arxiv.org/abs/1507.03941
- [V] Dounas-Frazer et al. (2017) Socially mediated metacognition. https://arxiv.org/abs/1701.02267
- [V] Dounas-Frazer and Lewandowski (2016) Electronics lab instructors' approaches. https://arxiv.org/abs/1610.01564
- [V] Dounas-Frazer and Lewandowski (2016) Nothing works the first time. https://arxiv.org/abs/1606.05389
- [V] Dounas-Frazer et al. (2018) Pathways to proposing causes. https://arxiv.org/abs/1806.06042
- [M] Reiter (1987) A theory of diagnosis from first principles. https://doi.org/10.1016/0004-3702(87)90062-2
- [M] Davis (1984) Diagnostic reasoning based on structure and behavior. https://doi.org/10.1016/0004-3702(84)90048-0

Medical diagnosis (human reflection and bias)
- [V] Mamede et al. (2020) Immunising physicians against availability bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC7362774/
- [V] Mamede et al. (2021) Disease knowledge predicts susceptibility to availability bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC7947124/
- [V] Lambe, Hevey, Kelly (2018) Guided reflection shows no effect on diagnostic accuracy. https://pmc.ncbi.nlm.nih.gov/articles/PMC6265413/
- [V] Availability bias and reflection in internal medicine residents (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7807127/
- [V] Mamede and Schmidt (2023) Deliberate reflection and clinical reasoning. https://pmc.ncbi.nlm.nih.gov/articles/PMC10083910/ (authorship from memory, verify)

LLM and AI studies
- [V] Chen et al. (2025) AIOpsLab. https://arxiv.org/abs/2501.06706
- [V] Jha et al. (2025) ITBench. https://arxiv.org/abs/2502.05352
- [V] Roy et al. (2024) Exploring LLM-based agents for root cause analysis. https://arxiv.org/abs/2403.04123
- [V] Ahmed et al. (2023) Recommending root-cause and mitigation steps for cloud incidents. https://arxiv.org/abs/2301.03797
- [V] Wang, Liu et al. (2024) RCAgent. https://arxiv.org/abs/2310.16340
- [V] Chen et al. (2023/2024) RCACopilot. https://arxiv.org/abs/2305.15778
- [V] Pei et al. (2025) Flow-of-Action. https://arxiv.org/abs/2502.08224
- [V] Tseng et al. (2026) SADE. https://arxiv.org/abs/2605.04530
- [V] FaulT-Bench (2026). https://arxiv.org/abs/2608.27021
- [V] NIKA (2025). https://arxiv.org/abs/2512.16381 (benchmark description only)
- [V] Marozzo and Lio (2026) LLM-as-an-Investigator (SIA). https://arxiv.org/abs/2606.13220
- [V] Li et al. (2026) QoEReasoner. https://arxiv.org/abs/2606.01925 (partly garbled)
- [M] Evaluating LLMs on consumer device repair questions (2026). https://arxiv.org/abs/2606.03331
- [V] Uncertainty of Thoughts (UoT). https://arxiv.org/abs/2402.03271
- [V] Choudhury et al. (2026) BED-LLM. https://arxiv.org/abs/2508.21184
- [V] Li et al. (2024) MediQ. https://arxiv.org/abs/2406.00922
- [V] Li, Kim, Wang (2025) QuestBench. https://arxiv.org/abs/2503.22674
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297
- [V] Olausson et al. (2024) Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896
- [V] Savage et al. (2024) Diagnostic reasoning prompts. https://arxiv.org/abs/2308.06834
- [V] Schmidgall et al. (2024) Addressing cognitive bias in medical language models. https://arxiv.org/abs/2402.08113
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120
- [V] Cemri et al. (2025) MAST. https://arxiv.org/abs/2503.13657
- [V] Xia et al. (2024) Agentless. https://arxiv.org/abs/2407.01489
- [V] Kang, An, Yoo (2024) LLM-based explainable fault localization. https://arxiv.org/abs/2308.05487
- [V] Pham et al. (2025) RCAEval. https://arxiv.org/abs/2412.17015
- [V] Jacovi et al. (2023) Tool-assisted generation strategies. https://arxiv.org/abs/2310.10062

Notes on opening: critique.md records that Mamede, Lambe, PMC7807127, Savage, Flow-of-Action, MAST and UoT were read by earlier agents and not re-opened in the audit pass. Eight arXiv full texts were re-checked in the critique pass (the critique lists AIOpsLab, ITBench, SIA, SADE, FaulT-Bench, Roy, Huang and UoT-related checks; the exact eighth is not named).

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 6 established claims: 3 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E08.01-K05** (reworded: the sources support less). FaulT-Bench (SADE 24%, ReAct 16%, Claude Code 11% over-diagnosis on answered runs; 74% in one agent/vague-ticket cell) and AIOpsLab (only GPT-4-W-SHELL passed the 2 Noop problems, 3 of 4 agents false-positive) check out, but 'has not been tested by anyone' is an unsupported universal negative. Corrected claim: A separate evaluate-after-repair check is needed and the agent must be allowed to conclude 'no fault': on healthy networks agents report a fault in 11-24% of answered runs (FaulT-Bench, standard ticket; up to 74% for one agent with a vague ticket), and 3 of 4 agents did so on AIOpsLab's 2 no-fault problems. We found no study that tests a no-fault exit plus verify gate as a fix.
- **E08.01-K12** (reworded: the sources support less). GPT-4 GSM8K 95.5 to 89.0 (5 self-correction calls) and the Kamoi et al. 'no fair demonstration except tasks where verification is much easier' are verified, but 'gains appear only with an oracle or external feedback' omits that Kamoi et al. also report large-scale fine-tuning enabling self-correction. Corrected claim: Intrinsic self-correction without an external signal does not help and can hurt (GPT-4 GSM8K 95.5 to 89.0 after five rounds); gains appear with an oracle, reliable external feedback, or large-scale fine-tuning. Kamoi et al. survey: no prior work shows successful self-correction with feedback from prompted LLMs except in tasks where verification is much easier than generation.
- **E08.01-K18** (reworded: the sources support less). MAST percentages are right (step repetition 15.7, unaware of termination 12.4, wrong assumptions 6.8) and AIOpsLab does show repeated API calls and apologise-retry loops, but no failure mode dominates: reasoning-action mismatch (13.2%) and disobeying task specification (11.8%) are larger than wrong assumptions, and task derailment (7.4%) is larger than 6.8%. Corrected claim: Multi-agent LLM failures are spread over many modes; among the most frequent in MAST are step repetition (15.7 percent), reasoning-action mismatch (13.2), not recognizing task completion (12.4) and disobeying the task specification (11.8), with proceeding on wrong assumptions at 6.8; AIOpsLab shows repeated-call and apologise-retry loops.
- **E08.01-K01** (now single-source: only one opened source, code check).
- **E08.01-K03** (now single-source: only one opened source, code check).
