# Abductive diagnosis: deep document

*Subfield C09.02 of model-based diagnosis. Evidence ids (a01-a27, b01-b26, c01-c29, d01-d17) and claim ids (C09.02-K01 to K32) refer to the jsonl files in this folder. Counts of "independent sources" use distinct papers (see critique.md). Most 2026 numbers are single-run arXiv preprints, many graded by LLM judges. The classic 1987-1992 papers were not opened in print; their formal claims are from secondary sources and the open Dupre and Poole papers.*

## 1. What it is

Abductive diagnosis is the search for the best explanation of abnormal observations, using a model of how the system should behave. The loop is: simulate the model, compare predicted with observed behaviour, and name the parts whose faults would account for the difference.

The central device is the abnormality predicate **Ab**. Each component S carries a rule pair (a01):
- not Ab(S) implies the component behaves normally (internal and observable).
- Ab(S) implies a different, usually weaker or fault-specific, behaviour.

A diagnosis is a set of components marked Ab. The model plus the observations must stay logically consistent with exactly those parts broken and all others healthy. The Ab flag is the unit of hypothesis: it says "this part is the one that is off".

Two logical styles exist and they sit on one spectrum (b01, b02):
- **Abductive diagnosis**: the fault hypotheses, together with the model, must *entail* (explain) the observations. This needs fault models.
- **Consistency-based diagnosis**: the hypotheses must only *not contradict* the observations. This works from a model of correct behaviour alone.

Related logic-based abduction (a03): given theory T and observations O, find E with T plus E entailing O and T plus E consistent. A minimality condition is added because many E qualify. The best one is chosen by simplicity, prior probability or explanatory power. Set-cover abduction (Peng and Reggia, a11) is the same idea in another form: find the smallest irredundant set of disorders that covers all findings.

For our agent this subfield gives a precise shape for operator O8 (reframe) and for the hypothesis record: a hypothesis is "these parts are abnormal", a prediction is what the model says follows, and the check is a diff between predicted and observed. This document asks what is known about whether LLMs can do that loop, and where they fail.

## 2. History and theories in depth

**Peirce and logic-based abduction.** Peirce's 1903 form: a surprising fact C is observed; if A were true, C would follow as a matter of course; so suspect A (c27). Josephson and Josephson (1994, a12) framed it as inference to the best explanation. Wikipedia cites them for fault detection as the most direct application.

**Set-cover era (1980s to 1990).** Peng and Reggia (1990, a11) defined parsimonious covering: a diagnosis is an irredundant set of disorders covering all findings, with a probabilistic extension that ranks covers. Bylander, Allemang, Tanner and Josephson (1991, a10) showed that finding a best explanation is NP-hard in the general set-cover setting and hard to approximate; independent, non-interacting causes are the tractable special case. [from memory, not opened]

**Consistency-based diagnosis from first principles.** Reiter (1987, a06) defined a system as (SD, COMP, OBS). A diagnosis is a minimal set of components whose assumed Ab status is consistent with SD and OBS, all others assumed normal. Diagnoses are the minimal hitting sets of the collection of conflict sets. The HS-tree algorithm computes them. De Kleer and Williams (1987, a07) built the General Diagnostic Engine: an ATMS records minimal conflicts when predictions clash with measurements, candidates are formed from the conflicts, and candidates are ranked by prior failure probability (independent priors; probability is a product of p and 1-p). It also chooses the next measurement by expected entropy. De Kleer, Mackworth and Reiter (1992, a08) unified both views (kernel diagnoses). Crossref citing counts (d14): Reiter 1,986, de Kleer and Williams 1,228, de Kleer-Mackworth-Reiter 322, Bylander et al. 245. None of these was opened in print.

**Bridging the two styles.**
- Console and Torasso (1991, b01, a09): a diagnosis is a mode assignment whose predictions are consistent with OBS and imply OBS+. If OBS+ is empty the diagnosis is consistency-based; if OBS+ equals OBS it is abductive. The parameter OBS+ picks which observations must be explained.
- Poole (1994, b05, b06): for acyclic causal domains, the same problem encoded abductively and consistency-based returns the same base causes (Theorem 3.2). Equivalence needs a different knowledge encoding in each framework. In the abductive encoding, c->s is a fact if s is a necessary symptom, else an assumable hypothesis. Non-strict causes (a cold may cause sneezing) fit both without new machinery.
- Theseider Dupre (2000, b02 to b04): for a fully predictive (deterministic) model, abductive and consistency-based diagnosis give identical answers (Property 1). They diverge when the model is nondeterministic or abstract. Example: a pump fault is consistent with a sign change in a level derivative but does not predict it, so pure abduction under-explains. Kautz's supermarket example: the plan "get food" does not entail "going to this supermarket". Three fixes: parametrised assumptions (flat(B,V) iff V in [0,1.2]), Hobbs-style etc-assumptions, or the weak-abduction idea of Cordier (who warns of hypothesis proliferation). Poole, Reiter and Konolige closure axioms restore equivalence.

**Efficiency work.** Roos (1993/2022, b07): a causal-ancestor focus picks likely broken components and the most informative probe; worst case O(n^2) in components, near linear with low connectivity.

**Why this was a hard problem before LLMs.** Three facts: (1) minimal diagnoses are hitting sets, which blow up with multiple faults; (2) the model must be complete enough to predict; (3) choosing the next probe needs a probability model. The LLM era trades the formal model for a learned, partial one. The open question is what survives.

**LLM-era lines (2019-2026).**
- Commonsense abduction benchmarks: ART / alphaNLI (a04), True Detective (c18), e-CARE, DDXPlus and others surveyed by Salimi et al. (a25).
- Root cause analysis (RCA) of cloud systems, which is diagnosis with a partial model: OpenRCA and descendants (b14, b16, b18, b19, c04, c06, c09, c12).
- Formal generative tests of the simulate-and-compare loop: Elenchos (a13), TempoBench (b11).
- Structured hypothesis tracking: Graph of States (a19), LATS-RCA (b21), HypoAgent (a21), Abduct-Act-Predict (d08).
- Neuro-symbolic pairing: the LLM proposes, a solver verifies (d12, d13, a24).

## 3. Core findings with exact numbers

Status: E = established (two or more independent papers, or a formal result), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Abductive and consistency-based diagnosis coincide for deterministic, fully predictive models | Property 1 (proof); Poole Theorem 3.2 for acyclic causal encodings | b02, b05 (Dupre 2000; Poole 1994) | E (formal; Reiter-era papers not opened) |
| Diagnosis = minimal Ab set consistent with model plus observations; minimal hitting set of conflict sets | Reiter 1987; 1,986 citing works | a06, a01, d14 | E (not opened in print) |
| Best explanation is NP-hard in general | complexity result | a10 | S (from memory) |
| Detect vs attribute gap (Elenchos, 13 LLMs) | detection 0.65 vs exact attribution 0.28; attribution given detection 0.39; per-model gap up to 0.57 (gemini-2.5-pro VK 0.93, VA 0.35) | a13, d01, d15 | E (with b11, b14, b09) |
| Simulate well, attribute badly (TempoBench) | DeepSeek R1 96.0 percent forward simulation vs 32.1 percent minimal necessary causes; over 94.9 percent of wrong steps are overspecification | b11 | S |
| Visibility ablation: attribution copies visible guards | at 25 percent visibility simulation falls 79.5 to 31.8, 66.9 to 28.8, 59.8 to 8.8; attribution moves at most 3.4; guard copied on 96.5 percent of steps | b12 | S |
| RCA: name a service vs the exact set vs a valid path | any correct service 76.0; exact set 20.7; F1 34.1; valid path 61.5; node F1 62.2 vs edge F1 43.4 (11 LLMs, 500 instances) | b14 | S |
| Multi-fault collapse | exact accuracy k=0 0.90 (null-case specificity, not fault finding), k=1 0.32, k=2+ 0.15, interacting pair 0.03 | a14, d04, b14 | E (Elenchos plus OpenRCA 2.0) |
| Premature commitment | 86.5 percent of detect-but-misattribute cases left probe budget (Pmax 50) unused | a15, d04 | S (b15, c05 agree in kind) |
| Fault count known vs unknown | known k raises hallucinated extras; unknown k raises omissions | a15 | S |
| Selecting is easier than generating (DDXPlus) | rank given candidates 79.75 Top-1, 98.7 Hit@3; generate 63.0 Hit@3, 28.1 Set-F1@3 | a25, b09 | E in kind (also True Detective golden chain) |
| True Detective, supplied reasoning chain | GPT-4 0.27 vanilla, 0.38 chain of thought, 0.83 golden chain; GPT-3.5 0.28 to 0.63; humans 47 percent; random 0.24 | c18 | S (2022 models) |
| ART abductive benchmark | best BERT (linear chain) 68.9, GPT-ft 63.1, majority 50.4, human 91.4, hypothesis-only 59.5 | a04, a05 | S (2019 models) |
| Abduction trails deduction across the literature | pooled medians: deduction 79.96, abduction 42.50, induction 28.8; GPT-4 zero-shot syllogism abduction about 42 | b10, a22 | E in direction; pooled number mixes tasks |
| Hypothesis-state structure (Graph of States) | human-judged Match 39.86 vs best baseline about 26.09; LLM judge 31.88; ablations 18.12 (no causal graph), 12.32 (no state machine); fabrication 22.22 to 0 percent; failed backtracking 52.78 to 30.90; $0.12 vs $0.73 per case | a19, a20, d07 | S (LLM-judge heavy) |
| HypoAgent closed loop over knowledge graphs | BioKG Jaccard 0.885 vs CtrlHGen 0.718, best-of-k 0.758, ReAct 0.224, symbolic 0.420 | a21, c25 | S |
| LATS-RCA tree search | 91.3 vs ReAct 39.8 on one small benchmark; 24.1 of 37 (65.1 percent) on real incidents; hypotheses 18.9 vs 5.1; tokens 156K vs 41K | b21, d05, d06 | C (not token-matched) |
| Breadth ablation | no candidate batching -7.0; no backpropagation -6.5; no reflection -3.7 | d05 | S |
| Abduct-Act-Predict scaffold | step accuracy 47.46 vs 16.67 (2.85x) and 29.31 vs 12.07 (2.43x); no prediction step -7.14 and -12.07; no abduction -6.35 and -8.62 | d08 | S (AI-written paper; log attribution) |
| Prompt text does not fix it | hypothesis-driven and pitfall-aware prompts: no gain (Sonnet 4, 70 tasks); discipline rules did not rescue interacting faults (most models 0) | b17, c03, d02 | E |
| Enforced protocol helps a little | pitfalls down about 14-15 points; steps -22.1 percent; perfect detections only 0 to 4.9 and 2.4 to 7.3 percent | b17, c03 | S |
| Domain knowledge beats procedure text | Full Score 14.10 (no rules), 19.23 (label-schema), 24.36 (manual rules), 35.90 (mined rules); removing the five-step procedure raised score, not significant after correction | d11, c11 | S |
| Cloud RCA failure taxonomy | 1,675 runs: hallucinated interpretation 71.2 percent, incomplete exploration 63.9, symptom-as-cause 39.9, no cross-validation 18.6; best perfect detection 12.5 percent | b16, c02 | S |
| Hallucinated causes across studies | ORCA-bench 7 to 40 percent of reports; 4 to 40 percent (ReAct 4, CoT 12, retrieval 40) | b19, c06 | E |
| Agentic loops can hurt small models | Llama 3.2 3B location@3 0.31 to 0.23 to 0.05 (one-shot, ReAct, plan-execute) | c04 | C (vs c06) |
| Failure predictors | anchoring, repetition, arbitrary evidence, failure to update: each at least 15 percent drop, risk ratio below 0.55 | c05 | S |
| Deterministic evidence and scoring raise accuracy | EviRCA 40.6 and 43.9 vs 15.2 baseline, tokens down 15-26x; RCAgent without observation compression -33.54 pass rate | c09, c07 | E in kind |
| Reflex code agent solves the easy cases | Simple Reflex Agent V=1.0 at k=1 and additive sets; no LLM matches | d01 | S |
| Reasoning effort does not rescue | gpt-5.4 attribution low 0.41, medium 0.47, high 0.46; k=2 interacting zero at every effort (n=5, one config) | d03 | S, preliminary |
| Free tools match rich tools | free Python 85.4 vs full diagnosis tools 82.8 top-1; L1 52.7, L2 68.8, L3 82.8 | c12 | S |
| Right label, wrong action | root-cause service 91.4-99.7 percent, recovery validity 36.8-60.3; invalid plans for 39.5-62.0 percent of correct diagnoses | b20 | S |
| Evidence closure | best Joint RCA Accuracy 0.76 / 0.68 but Evidence Closure Rate 0.38 / 0.15; trajectory-as-ICL JRA 0.76 to 0.83 | b18 | S |
| Active evidence gathering is worse | success GPT5.4 0.64, Mistral-Large-3 0.20, Qwen3.6-35B 0.03; single-turn > passive > active | a17, c15 | S |
| Salience capture, presence bias | about 24 points AnySvc shortfall; silence read as health | b15 | S |
| Underdetermination | 70B-class models give about 20 percent consistent hypotheses (GEAR) | b22 | S |
| Leakage inflates diagnosis scores | Recall@1 54.3 to 40.3 (g 0.94); classifiers 42.9 to 16.7 (d 2.01); leakage g 0.94/1.18/1.21 vs agent gain g 0.77/0.81/1.01 | b23, c20 | S |
| Clinical differential | tuned LLM top-10 59.1 vs 33.6 unassisted clinicians (p 0.04); clinicians with LLM 51.7 (table 51.8) vs 36.1 | a27, c19 | S (curated NEJM) |
| Physical system (AUV, 480 trials) | gpt-5.5 top-3 85/90/85, rank-one 75/70/43; nemotron-nano top-3 78/68/60; gemma4:12b 42/30/38; gpt-oss:20b 10/28/25 | d09, d16 | S |
| Solver verification of LLM assumptions | up to 30 percent relative gain; drop under perturbation 2 vs 8.5 percent | d12, a24 | S |
| Self-critique damages; monotone rule fixes | regressions 11.8 vs 1.3 percent; +12.9 points over zero-shot | c24 | S |
| Reasoning tokens track human reaction time | N 120, 160 items, human accuracy 78.8; r 0.552 (GPT-OSS-120B), 0.197 (DeepSeek-V3); R1 vs V3 Fisher z 1.23, p .217 | a23, c16 | S |

## 4. Mechanisms and models

### 4.1 The Ab-predicate model (implementable core)
Data: a list of components COMP, a model SD that maps component states to predicted observations, and observed values OBS.

1. For each component c keep a flag in {normal, Ab(mode)}.
2. Predict: run SD with the current flag assignment, get predicted observations P.
3. Compare: diff = {o in OBS : P(o) != o}. An empty diff means the assignment is consistent.
4. A **conflict set** is a set of components that cannot all be normal given the diff. Find one by tracing which components the wrong prediction depended on.
5. A diagnosis is a minimal hitting set of all conflicts found: it contains at least one component from every conflict.
6. Rank diagnoses (smallest first, or by prior failure probability p(c)). With independent priors: P(D) is proportional to the product of p(c) over Ab parts times the product of (1-p(c)) over the others.
7. If several diagnoses remain, choose a **discriminating probe**: the measurement that splits the remaining diagnoses most evenly (de Kleer and Williams use expected entropy). Measure, add the result to OBS, repeat from step 2.

Reiter's HS-tree: build a tree whose nodes carry conflicts and whose edges choose one component from the conflict; a node with no remaining conflict is a diagnosis; prune non-minimal ones. This is a hitting-set loop and runs in code, not in the model.

### 4.2 Abductive vs consistency-based modes
- Abductive mode: require model plus Ab-set to *entail* each observation. Under-explains when the model is vague (b02, b04).
- Consistency mode: require only no contradiction. Over-admits hypotheses when the model predicts little.
- Console-Torasso OBS+ switch: choose which observations must be explained. Practical rule: put observations the model can predict exactly into OBS+; leave vague ones out.
- Fix for vague models: parametrised assumptions (flat(B,V) iff V in [0,1.2]) so a hypothesis states a range that contains the observation.

### 4.3 Set-cover form
Each disorder d has an effect set effects(d). A cover H satisfies: union of effects(d) over H contains all findings. Minimal cardinality or irredundancy picks the answer. Valid when causes are independent (a10, a11). Once faults interact, the effect of a pair is not the union, and this form fails. That matches the Elenchos interacting collapse (a14).

### 4.4 How LLM systems implement the loop
- **Graph of States (a19, a20).** Two parts: a causal graph of hypotheses and evidence with support and refute links, and a state machine that drives the search (which node to expand, when to backtrack). Targets four failure modes: evidence fabrication, context drift, failed backtracking, early stopping. Removing the graph: 31.88 to 18.12 (LLM judge). Removing the state machine: to 12.32, and cost rises to $0.17 per case.
- **LATS-RCA (b21, d05).** Tree search over root-cause hypotheses with candidate batching (many hypotheses per expansion), backpropagation of results, and reflection. Ablations: -7.0, -6.5, -3.7.
- **HypoAgent (a21).** Propose a formula, execute it over a knowledge graph, find which branch fails to cover the observed entities, revise that branch. Adding earlier hypotheses as reference raised BioKG Jaccard 0.892 to 0.910.
- **Abduct-Act-Predict (d08).** Three steps in one pass: infer the hidden cause, define the minimal fix, predict the result of the fix. The predict step is the simulate-and-compare half of the loop. Without step numbering the score fell by 29.68 points.
- **Elenchos reflex agent (d01).** Code replays fixed probes against the reference system and diffs outputs. No reasoning. Perfect on single and additive faults. This is the Ab loop with the model run in code.
- **EviRCA, RCAgent, Agentic4PDM, ontology scoring (c07, c09, c21, c22).** Deterministic code builds evidence cards or scores candidates; the LLM extracts and proposes. EviRCA used 15-26x fewer tokens (c09).
- **NeSy-CTM, PACS (d12, d13).** The LLM abduces missing facts or proof steps; a solver checks consistency; sampled proofs are aggregated.
- **DRAGO (c24).** Deterministic diagnosis of an LLM-written artefact; a rewrite is kept only if the diagnosed error weight strictly falls.

### 4.5 Why LLMs fail at attribution (mechanism candidates)
1. Guard copying: attribution is answered by reading the visible rule, not by simulating (b12).
2. Overspecification: naming all visible conditions rather than the minimal necessary ones (b11, 94.9-99.8 percent of wrong steps).
3. Early stopping on the first plausible story (a15, b15, c05).
4. Salience capture and presence bias: the loudest signal wins; silence is read as health (b15).
5. Hallucinated interpretation of retrieved data (b16).
6. Additive-fault assumption: interacting faults break the union-of-effects intuition (a14).

## 5. What holds up

**Established.**
- Detect-vs-attribute gap: four independent families (Elenchos, TempoBench, OpenRCA 2.0, DDXPlus) show a large gap between noticing, simulating or ranking and naming the minimal cause (K04).
- Selecting among given candidates is much easier than generating (K05).
- Multi-fault and interacting faults collapse accuracy (K08).
- Early commitment and anchoring (K07).
- Prompt-only advice does not repair abductive failures (K11): two independent papers (Kim et al., Elenchos) plus the cleaner Gopal test (d11).
- Hallucinated interpretation of retrieved data is the leading failure (K16).
- Deterministic extraction or scoring beats having the LLM do it (K13).

**Contested.**
- ReAct-style tool loops: fewer hallucinations in c06 (4 vs 12 vs 40 percent) but worse accuracy for a 3B model in c04. Different model sizes and tasks.
- Tree search (LATS-RCA, GoS): large gains, but LATS-RCA used 2.1x to 3.8x tokens and had no best-of-N arm. In GoS, bigger topologies (ToT, GoT, FoT) cost more and lost to the structured method, which hints that structure matters, but baselines are not token-matched.
- Procedure text: c11 shows removing the five-step procedure did not hurt, while Kim et al. show an enforced protocol cut steps and pitfalls. Prompt text gives no help; enforced steps give small help.

**Moderators found.**
- Model class and size dominate in the physical AUV test (d09).
- Known vs unknown fault count shifts error type, not total error (a15).
- Prompt structure information (Elenchos Level 0) gives large gains for weak models (a16).
- Evidence given upfront beats evidence chosen by the agent (a17).
- Visibility of the model: hiding the transition table wrecks simulation, not attribution (b12).
- Rich tools can hurt weak models that rarely invoke them (c12).

**Failures and null results.**
- More reasoning effort: no consistent gain (d03).
- Hypothesis-driven prompting widened exploration without fixing interpretation (c03).
- Pitfall-aware prompts were acknowledged in traces and ignored (b17).
- LLM self-critique damages correct answers (c24).
- More tools are not better (c12).

**Evaluation hazards.**
- Leakage: the leakage effect (g 0.94 to 1.21) exceeded the agent's real gain (g 0.77 to 1.01) in the rare-disease audit (b23).
- Label-only scoring hides ungrounded diagnoses (b14, b18).
- Single gold answers hide underdetermination (b22).
- LLM judges grade GoS and OpenRCA 2.0.
- Numbers corrected by the cross-check (critique.md): ART best is Linear Chain 68.9; the 0.90 in Elenchos is null-case specificity; LATS-RCA 91.3 is one small benchmark and 65.1 on real incidents; GoS 39.86 is human-judged (31.88 LLM-judged).

**Not tested at all.** An explicit Ab-flag table vs free prose on an LLM; a forced rival step; hitting-set loops for multi-fault; entropy-based probe choice for LLMs; token-matched tree vs best-of-N.

## 6. Language models

**Overall picture.** LLMs behave like good pattern matchers over a partial model. They can follow a model forward and notice that something is off, but they do not reliably reason backwards to the minimal cause.

**Benchmarks and results.**
- *Generative abduction as inverse problem (Elenchos, 13 LLMs, k in {1,2}, 3 prompt levels, 5 reps)*: detection 0.65; exact attribution 0.28; attribution given detection 0.39. The gap is largest in the best detectors (gemini-2.5-pro 0.57 [0.52, 0.63]; gemini-2.5-flash 0.53; gpt-5.4_low 0.52; gpt-5.4 0.50; haiku-4-5 0.44; smallest 0.08 because its detection is only 0.22). Wide panel of 30 LLMs: 0.32 (k=1), 0.15 (k=2+), 0.03 (interacting). Hardest cell 0.02. Random baseline 0.077 (k=1).
- *Simulate and attribute (TempoBench)*: 96.0 vs 32.1 for DeepSeek R1.
- *Cloud RCA*: best exact set 20.7 (500 instances, 11 LLMs); original OpenRCA best perfect detection 12.5 percent (1,675 runs); ORCA-bench 58.7 Easy, 25.3 Medium, 10.0 Hard (Sonnet 4.6); Cloud-OpsBench JRA 0.76/0.68 but evidence closure 0.38/0.15.
- *Commonsense abduction*: ART models of 2019 reached 68.9 vs humans 91.4. Salimi: ART and e-CARE selection best 87.2-88.0; True Detective best 42.9; MuSR murder 68.0; ProofWriter best 21.5.
- *Syllogistic abduction (a22)*: GPT-4 about 42 zero-shot; Llama-3-70B few-shot 75.46 abduction vs 84.72 deduction; belief and negation bias; "Neither" items hardest.
- *Medicine*: DDx top-10 59.1 vs 33.6; DDXPlus rank 98.7 Hit@3 vs generate 63.0. Criminal profiling (c23): scores mostly in the 40s and 50s F1.
- *Physical*: AUV top-3 up to 90 percent for gpt-5.5; local small models 10-78 percent; diagnosis not coupled to action (d16: on a manageable 0.005 m shift gpt-5.5 continued correctly in 93 and 90 percent of trials; gemma4:12b aborted every manageable-fault trial).

**What changed results, and by how much.**

| Intervention | Effect | Id |
|---|---|---|
| Supply the correct reasoning chain | GPT-4 0.38 to 0.83 | c18 |
| Rank given candidates instead of generating | Hit@3 63.0 to 98.7 | a25 |
| Code replays probes and diffs | V 0.28 to 1.0 on easy cases | d01 |
| Deterministic evidence cards | 15.2 to 40.6/43.9, tokens down 15-26x | c09 |
| Mined fault-discrimination rules in prompt | 14.10 to 35.90 | d11 |
| Causal graph + state machine | 18.12/12.32 ablations vs 31.88 | a20 |
| Tree search with candidate batching | 39.8 to 91.3 (small bench), 5.1 to 18.9 hypotheses, 2-4x tokens | b21 |
| Abduce-act-predict prompt | 2.4-2.9x step accuracy | d08 |
| Closed-loop revise over KG | Jaccard 0.718 to 0.885 | a21 |
| Solver check on LLM assumptions | up to 30 percent relative; robust to noise | d12 |
| Monotone accept rule | regressions 11.8 to 1.3 percent | c24 |
| Enforced protocol | pitfalls -14-15 points, steps -22.1 percent, detections +2-5 points | b17 |
| Prompt advice (hypothesis-driven, pitfall-aware, discipline rules) | none | c03, d02 |
| Higher reasoning effort | none | d03 |
| Richer tool set | none to negative | c12 |
| Telling the model k | trades omissions for hallucinated extras | a15 |
| Agentic loop on a 3B model | negative | c04 |

**Reasoning tokens as a signal.** Reasoning token count tracks human reaction time on abductive items (r 0.552 for GPT-OSS-120B, 0.197 for non-reasoning DeepSeek-V3; the R1-V3 difference is not significant, p .217), and items humans find hard are hard for models (a23). This supports using length as a rough difficulty signal, not as a verifier (G10).

**Caveat on generalisation.** 2026 results come from preprints on partial models in software and logic domains. The 2022-2023 numbers (True Detective, DDx) come from older models.

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)
1. **Score detect/simulate and attribute separately on diagnosis items (bench, S9 log).** Never accept "it noticed a fault" as success. [E] K04; a13, b11, b14, b09, d15.
2. **Generate-then-select split (S3/S7, G5).** The model produces candidates; code selects among them. Selection is far easier than open generation. [E] K05; b09, c18, a04, a25.
3. **Do not rely on prompt text for abductive discipline (G10 reinforcement).** Prompt rules about hypothesis breadth, pitfalls or discipline did not change behaviour. Any step we want must be enforced by code. [E] K11; b17, c03, c11, d02, d11. Consistent with section 4b.
4. **Require a grounded evidence chain for every claimed cause, checked by script (S4/S8, G2/G10).** Count unsupported claims; a right label with no valid path is a fail. [E] K12, K16; b14, b18, b16, b19.
5. **Move deterministic evidence extraction, comparison and scoring into code (G5, S4).** The LLM proposes and reads; code diffs and ranks. [E] K13; c09, c07, c21, c22 (and d01 for the easy cases).
6. **Score hypothesis sets on consistency and diversity, not top-1 only (S7 logging).** [E] K18; b22, b03.
7. **Treat multi-fault and interacting-fault items as a failure class (S0 gate, S9 class rate).** Do not spend long reasoning on them until a test shows a scaffold helps. [E] K08; a14, b14, d03 (K27 is [S]). Fits G11/G12.
8. **Isolate evaluation from leakage when we benchmark.** [S] K19 but costless; b23, c20.

### Test first (not yet added)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Explicit Ab-flag table (part, predicted, observed, mismatch) in the hypothesis record | O8, S2 | [S] K02 formal side [E], LLM effect untested | a01, a06, d08, a20 |
| Forced rival-hypothesis step before any stop (single rival, signal-triggered, G1) | O8, S6 | [S] failure is [E] (K07), fix untested; ACH matrix null in 4b | a15, d04, d05, b15 |
| Code-side model run and diff tool | S4, G5 | [S] K26 | d01, c09 |
| Hitting-set / minimal-conflict loop in code for multi-fault | O8, S4 | [S] untested | a06, a07, a14 |
| Predict-then-compare line in each hypothesis | O8 | [S] K32 | d08 |
| Discriminating-probe choice by split size or entropy | S7 | [S] K22 | a07, a17, a26, c15 |
| Notebook with support/refute links vs plain chain of thought | S2/S3 | [S] K10 | a19, a21, b21 |
| Mined rule cards of fault-discrimination knowledge | memory | [S] K28, K17 | d11, b18 |
| Monotone accept rule on revisions | S5, G2 | [S] K15 | c24 |
| Solver/consistency verification of proposed assumptions | S4/S8 | [S] K31 | d12, d13 |
| Hide-the-model check that attribution depends on simulation | S8 | [S] K25 | b12 |
| Missing-evidence checklist for silent faults | S1/S2 | [S] K23 | b15 |
| Reasoning length as a trigger for extra hypotheses | G12 | [S] K21 | a23 |
| Token-matched tree vs best-of-N | S3, G7 | [C] K29 | b21, d06, d07 |
| One-shot vs ReAct vs plan-execute at our model size | S3 | [C] K24 | c04, c06 |
| Small vs rich tool set | S4 | [S] K14 | c12 |

Do **not** add (section 4b): free reflection, "be careful" prompts, full ACH matrices, debate. The 86.5 percent unused-budget figure tempts a rule "always think longer"; effort scaling did not help (d03), so only a code-forced, signal-triggered rival step is a candidate.

## 8. Concrete tests on our bench

All arms at equal total tokens (setup cost counted, G7). Report exact attribution, detection, top-3 and unsupported-claim count. At least 5 repetitions per item; paired bootstrap.

1. **Ab table vs prose.** Items: fault-injection puzzles on a small deterministic circuit or rule system, k=1 and k=2 (Elenchos style, 40 items each). Arms: (A) free prose; (B) emit Ab(part) set plus predicted-vs-observed table. Metric: exact attribution; secondary unsupported claims. Expected: B above A by 5+ points at k=1; little change at interacting k=2.
2. **Forced rival step.** Items: 40 single-fault puzzles with a decoy that explains most symptoms. Arms: (A) one attempt; (B) one attempt plus a code-forced rival (one counter-hypothesis plus one discriminating check, fired only when one candidate was named and budget remains); (C) best-of-2 independent. Metric: exact attribution, share stopping with budget left. Expected: B beats A by 5-10 points; C is the bar B must clear.
3. **Code diff tool vs in-model simulation.** Items: the same puzzles with a callable simulator. Arms: (A) the model simulates in prose; (B) a tool runs the model and returns the predicted-vs-observed diff. Metric: attribution and tokens. Expected: B higher and cheaper, as with the reflex agent.
4. **Hitting-set loop for multi-fault.** Items: 40 additive k=2 puzzles and 20 interacting pairs. Arms: (A) single-answer prompt; (B) the model proposes a conflict per failed prediction, code builds minimal hitting sets and the top one is tested. Metric: exact set accuracy and Jaccard. Expected: B lifts additive k=2 from about 0.15 toward 0.4; interacting stays low unless the interaction is modelled.
5. **Notebook vs chain of thought vs best-of-N.** Items: 60 RCA-style incident traces with known causes. Arms: (A) plain CoT; (B) support/refute notebook; (C) best-of-N with code vote at B's token cost. Metric: script match to ground truth (no LLM judge), hypotheses explored. Expected: B above C by 3+ points or drop it (K29).
6. **Selection vs generation.** Items: 60 diagnosis items with a candidate list. Arms: (A) open generation; (B) generate k candidates, rank in code with an authorship-blind model scoring pass (G5); (C) supplied list ranking. Metric: Hit@1, Hit@3. Expected: C much above A; B in between.
7. **Rule cards vs procedure text vs enforced check.** Items: held-out fault set with discriminating rules mined from past solved cases. Arms: cards only; procedure text only; enforced code check only; none. Metric: Full Score. Expected: cards give the largest gain (d11), text none.
8. **Predict-then-compare line.** Items: 50 fault-attribution items. Arms: hypothesis with and without a one-line predicted-observation check. Metric: attribution. Expected: +5 points or more (d08 reports 7-12).
9. **Probe choice.** Items: 40 puzzles with several candidate probes. Arms: free model choice; code ranks probes by split of remaining hypotheses; random probe. Metric: probes to correct diagnosis. Expected: code split uses fewer probes than free choice.
10. **Hide-the-model check.** Items: puzzles whose rule table can be partly masked. Arms: full vs 25 percent visible. Metric: change in simulation and attribution. Expected: attribution moves less than simulation (as b12); if ours differs, simulation is truly used.
11. **Detect/attribute/action decoupling.** Add action-choice scoring to all of the above; do not infer one from another.

## 9. What does not transfer, and why

- **Hitting-set theory as a guarantee.** It assumes a complete, correct model and independent priors. The LLM's internal model is partial and its fault probabilities are uncalibrated. Use the structure, not the guarantee.
- **Entropy-based probe choice.** Needs a probability model over candidates; stated LLM probabilities are weak (G5, section 4b on verbal confidence). Use code-side split counts.
- **Cloud RCA numbers (most of the evidence).** Faults are software, telemetry is noisy and incomplete, and "root cause" labels are partial. Do not read 20.7 or 12.5 percent as a universal ceiling.
- **Tree-search gains (LATS-RCA, GoS).** They may come from sampling more hypotheses at 2-4x cost; our bench demands equal tokens.
- **Human clinical results (DDx).** Curated NEJM cases and a tuned model; a ceiling for list-style differentials only.
- **Classic domain models (circuits, valves).** Our bench items may have no executable model. Where no simulator exists, step 2 of the loop cannot move into code.
- **Reasoning-token / reaction-time alignment (a23).** Correlational, forced-choice story items; not a stopping rule.
- **NP-hardness.** Informs a cap on hypothesis enumeration, nothing more.
- **Fine-tuning results (TempoBench b13).** We do not train.
- **Active evidence-gathering results (a17).** Hidden-function game with four models; limited fit to our format.

## 10. Open questions

1. Does an explicit Ab-flag table beat free prose at equal tokens? No direct study.
2. Does a forced rival step fix premature commitment, and at what token cost?
3. Can a code-side hitting-set loop rescue the 0.15 and 0.03 multi-fault results? Interacting faults need a model that is not additive.
4. Is the detect-vs-attribute gap closed by running the simulation in code? d01 says yes for easy cases; unknown for interacting ones.
5. At equal tokens, do tree and graph methods beat best-of-N or self-consistency (K29)?
6. Which probe-selection rule works for LLMs?
7. Do prompt-text guardrails ever help, or only enforced code checks? No clean three-arm test.
8. Do the deficits hold on the newest frontier models and on non-software physical systems with leakage controls?
9. The classic papers (Reiter, de Kleer-Williams, Console-Torasso) were not opened in print; K01-K03 rest on secondary sources.
10. How much agentic diagnosis gain survives strict leakage isolation?
11. Is the 86.5 percent unused-budget finding a stopping problem or a "cannot think of the answer" problem? Extra effort (d03) did not help, so forced breadth may not either.
12. Does the model that keeps competing hypotheses (best AUV model, d10) do better because of the hypotheses or because it is simply the better model?

## 11. Sources

[V] = opened and read this session (full text or page). [M] = snippet, listing, memory or secondary mention only.

- [V] Wikipedia, Diagnosis (artificial intelligence) - https://en.wikipedia.org/wiki/Diagnosis_(artificial_intelligence) (a01)
- [V] Wikipedia, Model-based reasoning - https://en.wikipedia.org/wiki/Model-based_reasoning (a02)
- [V] Wikipedia, Abductive reasoning - https://en.wikipedia.org/wiki/Abductive_reasoning (a03, b08, c27)
- [V] Bhagavatula et al., Abductive Commonsense Reasoning (ART) - https://arxiv.org/abs/1908.05739 (a04, a05)
- [M] Reiter (1987), A theory of diagnosis from first principles - https://doi.org/10.1016/0004-3702(87)90062-2 (a06, d14 Crossref)
- [M] de Kleer and Williams (1987), Diagnosing multiple faults - https://doi.org/10.1016/0004-3702(87)90063-4 (a07)
- [M] de Kleer, Mackworth, Reiter (1992), Characterizing diagnoses and systems - https://doi.org/10.1016/0004-3702(92)90027-U (a08)
- [M] Console, Dupre, Torasso (1991), abduction and deduction in model-based diagnosis - https://doi.org/10.1093/logcom/1.5.661 (a09)
- [M] Bylander et al. (1991), Computational complexity of abduction - https://doi.org/10.1016/0004-3702(91)90005-5 (a10)
- [M] Peng and Reggia (1990), Abductive Inference Models - https://doi.org/10.1007/978-1-4419-8682-5 (a11)
- [M] Josephson and Josephson (1994), Abductive Inference - via Wikipedia (a12)
- [M] Console and Torasso (1991), A spectrum of logical definitions - https://doi.org/10.1111/j.1467-8640.1991.tb00396.x (b01, c29)
- [V] Theseider Dupre (2000), Abductive and Consistency-Based Diagnosis Revisited - https://arxiv.org/abs/cs/0003016 (b02-b04)
- [V] Poole (1994), Representing Diagnosis Knowledge - https://www.cs.ubc.ca/~poole/papers/rep.pdf (b05, b06)
- [V] Roos, Efficient Model Based Diagnosis - https://arxiv.org/abs/2209.09819 (b07)
- [V] Steiglechner, Mahler, Lohmann (2026), Elenchos / LLMs Can See the Smoke but not the Fire - https://arxiv.org/abs/2607.12733 (a13-a16, c13, c14, d01-d04, d15)
- [V] Mohiuddin et al. (2026), Don't Let Me Ask for It - https://arxiv.org/abs/2608.03388 (a17, a18, c15)
- [V] Luo et al. (2026), Graph of States - https://arxiv.org/abs/2603.21250 (a19, a20, d07)
- [V] Gao et al. (2026), HypoAgent - https://arxiv.org/abs/2605.31370 (a21, c25)
- [V] Abe et al. (2026), Abductive reasoning with syllogistic forms - https://arxiv.org/abs/2603.06428 (a22)
- [V] Arthur (2026), Thinking effort aligns between humans and reasoning models - https://arxiv.org/abs/2609.01867 (a23, c16)
- [V] Quan et al. (2026), Inferring Latent Intentions - https://arxiv.org/abs/2601.08742 (a24)
- [V] Salimi et al. (2026), Wiring the Why - https://arxiv.org/abs/2604.08016 (a25, a26, b09, b10)
- [V] Google DDx study (2023) - https://arxiv.org/abs/2312.00164 (a27, c19)
- [V] Holzer et al. (2026), TempoBench - https://arxiv.org/abs/2510.27544 (b11-b13)
- [V] Fang et al. (2026), OpenRCA 2.0 - https://arxiv.org/abs/2606.27154 (b14, b15, c10)
- [V] Kim et al. (2026), Why do AI agents systematically fail at cloud RCA - https://arxiv.org/abs/2602.09937 (b16, b17, c01-c03)
- [V] Wang et al. (2026), Cloud-OpsBench - https://arxiv.org/abs/2603.00468 (b18)
- [V] Gong et al. (2026), ORCA-bench - https://arxiv.org/abs/2607.28545 (b19)
- [V] Qi et al. (2026), R2Act - https://arxiv.org/abs/2607.04623 (b20)
- [V] Constantinov / Naakka et al. (2026), LATS-RCA - https://arxiv.org/abs/2605.03505 (b21, d05, d06)
- [V] He et al. (2025), GEAR - https://arxiv.org/abs/2509.24096 (b22)
- [V] Yang et al. (2026), Auditing leakage in rare-disease LLM diagnosis - https://arxiv.org/abs/2610.33592 (b23, c20)
- [V] Halba, Cooper, Bellingham (2026), SPAR AUV fault recovery - https://arxiv.org/abs/2609.20620 (b24 listing; d09, d10, d16 opened)
- [V] Cotnareanu et al. (2026), PACS - https://arxiv.org/abs/2605.08011 (b25 listing; d13 opened)
- [V] Weng et al. (2025), Abduct, Act, Predict - https://arxiv.org/abs/2509.10401 (b26 listing; d08 opened)
- [V] Stalled, Biased, and Confused (2026) - https://arxiv.org/abs/2601.22208 (c04, c05)
- [V] Exploring LLM-based Agents for Root Cause Analysis (2024) - https://arxiv.org/abs/2403.04123 (c06)
- [V] RCAgent (2023) - https://arxiv.org/abs/2310.16340 (c07)
- [M] OpenRCA (ICLR 2025) - https://openreview.net/forum?id=M4qNIzQYpd (c08, known via citing papers)
- [V] EviRCA (2026) - https://arxiv.org/abs/2609.19825 (c09)
- [V] Gopal and Krishnan (2026), How Far Can RCA Go - https://arxiv.org/abs/2607.13548 (c11 partial; d11 opened)
- [V] Rethinking Tool Design for Agentic RCA (2026) - https://arxiv.org/abs/2610.05009 (c12)
- [M] Abductive Commonsense Reasoning title page (c17)
- [V] True Detective (2022) - https://arxiv.org/abs/2212.10114 (c18)
- [V] Ontology-guided multi-agent differential diagnosis (2026) - https://arxiv.org/abs/2610.36325 (c21)
- [V] Agentic4PDM (2026) - https://arxiv.org/abs/2610.17786 (c22)
- [V] Before the Arrest, criminal profiling (2026) - https://arxiv.org/abs/2609.19965 (c23)
- [V] DRAGO (2026) - https://arxiv.org/abs/2610.22568 (c24)
- [V] Qu et al. (2026), NeSy-CTM - https://arxiv.org/abs/2606.20895 (c26 listing; d12 opened)
- [M] Crossref bibliographic records for the classic papers (d14)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 13 established claims: 10 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C09.02-K02** (now contested: a source does not say this). Neither source gives the definition: Wikipedia's section mentions Ab(S) but not minimality or consistency, and Theseider Dupre uses mode assignments, not minimal Ab sets.
- **C09.02-K16** (reworded: the sources support less). Only Kim et al. rank interpretation hallucination as the most frequent pitfall (71.2 percent of runs); ORCA-bench (7-40 percent of reports) and Roy et al. (4-40 percent of predictions, only 4 percent for ReAct) report hallucination rates but not that it is the leading failure. Corrected claim: Hallucinated interpretation of retrieved data is the most frequent pitfall in Kim et al. (71.2 percent of runs); ORCA-bench finds invented root causes in 7 to 40 percent of reports and Roy et al. find hallucination in 4 to 40 percent of predictions depending on the agent.
- **C09.02-K18** (reworded: the sources support less). GEAR's 20 percent consistent hypotheses for 70B-class models is verified, but Theseider Dupre says Cordier rejected parametrised assumptions for possible hypothesis proliferation in a methodology, not that weak models proliferate hypotheses. Corrected claim: Single gold answers hide underdetermination: in GEAR, 70B-class models give only about 20 percent consistent hypotheses (consistent ones cover about 95 percent of the sample space); separately, in model-based diagnosis Cordier rejected parametrised assumptions because of potential proliferation of hypotheses.
- **C09.02-K17** (now single-source: only one opened source, code check).
