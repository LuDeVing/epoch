# Model-based diagnosis: deep document

*Subfield E08.06. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K27), critique.md in this folder. Evidence ids (a01, b06, c07, d02 ...) point to those files. Duplicate papers are counted once (a24 = b20; a19 = b11; b12 = c03; a23, b13, c04 are versions of CFaults). Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Model-based diagnosis (MBD) finds broken parts of a system from two things only: a description of how the system should work, and what was observed. It needs no fault statistics and no expert rules. The founding contrast is with the experiential approach (MYCIN-style rules) (a01).

The core idea in plain words. Assume every part works. Predict what you should see. If the prediction clashes with the observation, some of the assumed-working parts must be broken. A set of parts that cannot all be working is a conflict. A diagnosis is a smallest set of parts whose being broken removes every clash. Diagnoses are exactly the minimal hitting sets of the conflicts (a03, b01).

Why it matters for our agent. This is a code-run reasoner. The language model should not decide what is consistent. Code can decide it, exactly, from a model. This fits the schema rule that code decides transitions (SCHEMA section 1) and guardrails G2 (revise from real, code-located output), G3, G5 and G10. It also maps onto the schema's S7 step (when two rules still fit, find the input where they differ): choosing the probe that best splits the candidate set is the GDE measurement step (a09).

What the field gives us:
- A precise definition of "smallest set of faulty parts consistent with all evidence" (a02).
- Algorithms for conflicts, hitting sets and next-probe choice (a04, a08, a09, a11).
- Scaling limits and cheap approximate modes (a16, a19, d16).
- Tested uses around LLMs, mostly 2024 to 2026, with a thin direct test (section 6).

The main gap: no study adds a code-run hitting-set step to an LLM agent and compares it to LLM-only diagnosis at equal tokens (critique GAP 1, K19). Everything we take is either established classical algorithm knowledge or indirect LLM evidence.

## 2. History and theories in depth

**Precursors (1970s to 1984).** Davis's constraint suspension and Genesereth's design-description diagnosis started structure-based diagnosis. SOPHIE, DART and LOCAL assumed a single fault and used half-split probing (a10, a14). We know these only second-hand; the 1984 papers were not opened (a14, critique).

**Reiter 1987, "A theory of diagnosis from first principles" (a01-a06, b01, b02, b25).**
- System = description SD + component list + abnormality predicate AB. Observation OBS.
- Definition 2.4: a diagnosis is a subset-minimal set A such that SD + OBS + {AB(c): c in A} + {not AB(c): c outside A} is consistent. Minimal means subset-minimal, not minimum cardinality, and not most probable (a02).
- Theorem 4.4 / Corollary 4.5: diagnoses are the minimal hitting sets of the minimal conflict sets (a03).
- Worked example: full adder (2 XOR, 2 AND, 1 OR). Inputs 1,0,1, outputs 1,0, both wrong. Minimal conflicts {X1,X2} and {X1,A2,O1}. Diagnoses {X1}, {X2,A2}, {X2,O1} (a02, a03).
- HS-tree algorithm (Section 4.2): breadth-first tree, each node labelled with a conflict, each edge removes one suspect. Three savings: reuse labels, close supersets of known hitting sets, prune redundant edges. One worked example found 6 minimal hitting sets with 13 accesses to the conflict collection (a04, b02).
- Measurements (Section 5): a new measurement keeps diagnoses that predicted the observed value, drops the others, and can add new multiple-fault diagnoses. Divide and conquer is justified only among single-fault diagnoses (a05). Reiter poses the probe-selection problem but gives no rule.
- Default logic link (Theorem 6.1): diagnoses are extensions of a default theory "each part is normal unless shown otherwise". Diagnosis is nonmonotonic (a06).
- Limits: first-order logic with a sound and complete prover assumed (consistency is undecidable in general). Weak-fault only: the model says how parts work, not how they fail (b01, b25). No empirical test at all.

**Greiner, Smith and Wilkerson 1989, the correction (a07, d15).** The pruned HS-tree as printed can lose minimal hitting sets. Counterexample: conflicts {{a,b},{b,c},{a,c},{b,d},{b}} lose the hitting set {a,b}. The bug is the interaction of node-closing with redundant-edge pruning. Fix: a directed acyclic graph (HS-DAG) with node reuse and relabelling. This is the first "replication" in the field, and it is a failure of the original. Lesson: validate any solver against brute force (K02).

**de Kleer and Williams 1987, GDE (a08, a09, a10, b04).**
- Separates prediction from diagnosis. An ATMS records which assumptions each prediction depends on. Conflicts are minimal inconsistent assumption sets. Candidates are minimal hitting sets. The candidate space is kept as minimal candidates, not all 2^n (a08).
- Circuit of 3 multipliers and 2 adders: initial space 2^5 = 32. Observed F=10, expected 12, gives conflict {A1,M1,M2}. After G=12 the candidates are [A1], [M1], [A2,M2], [M2,M3] (a08).
- Probe choice by minimum expected entropy of the candidate distribution, using only prior failure probabilities of single components, Bayes and independence (a09). Cascaded inverters, p(fail)=0.01, a=1: expected cost b .98, c .96, d .94, e .93. After e=0 the best probe is c (.31). With no symptom, no probe is worth much (all near 1). Fig 2 with p=.01: P(no fault)=.951 initially; after F=10 three single faults at .323 each (a09).
- Authors' scaling claim, "square or cube of the number of potential faults", is an assertion with no table (a10). Later work shows exact algorithms degrade with cardinality (a16).
- Reiter notes de Kleer and Williams reached the same characterisation independently, with a less formal derivation (a06).

**Follow-ups by de Kleer.**
- 1989 Sherlock: behavioural modes (ok, known faults, and an "unknown" mode that predicts nothing and never conflicts). Fault models sharpen probe choice; the unknown mode keeps unforeseen faults diagnosable. Tested up to 400-gate ALUs with 4 modes each (a12).
- 1990 crude probabilities: if faults are rare, independent and equally likely, entropy reduces to S(x) = sum over outcomes of c_k ln c_k, with c_k the count of smallest diagnoses predicting value k. Lower is better. No numeric priors needed (a11).
- 1992 with Mackworth and Reiter: not every superset of a diagnosis is a diagnosis; kernel diagnoses; minimal diagnoses suffice under weak fault models (a13, badly OCR'd, abstract-level only).
- 2011 intermittent faults: each part gets p(c) (prior faulted) and g(c) (chance it works when faulted) (d14).

**Complexity.** Finding a diagnosis with at most k faults is NP-hard for arbitrary propositional models (Bylander et al. 1991, second-hand via a15, d16). Computing a further minimal diagnosis is NP-hard in general (a03). Roos (1993/2022): focus-then-probe for causal feed-forward networks is O(n^2), linear when connectivity is low (b21).

**Scaling era (2010 to 2023).**
- Feldman, Provan, van Gemund 2010: SAFARI, greedy stochastic search, gives up minimality for speed (a16, b06, c05). Their FRACTAL work adds active testing with chosen inputs (a17, b07).
- Pattipati and Alexandridis 1990: one-step lookahead optimal under unit costs and equal priors (cited in a17).
- Ignatiev, Morgado, Marques-Silva 2017: implicit hitting sets with MaxSAT, all failing observations at once (a19, b11).
- Rodler 2016 onwards: interactive ontology debugging with HS-tree + QuickXplain, entropy query selection, user studies (a20, b22, d12, d13); RBF-HS linear-memory search (a21, b09, b10); biased sampling study (a22, b08). Rodler 2023 habilitation (a31, snippet only).
- Orvalho et al. 2024 to 2025: CFaults, programs as circuits, statements as components (a23, b12, b13, c03, c04).
- Grastien, Haslum, Thiebaux 2023: generalises Reiter to dynamic systems and arbitrary preference orders; conflicts become sets of diagnostic properties (a18, b05, b26).
- Bertossi 2026: an abnormality atom is an actual cause iff it belongs to a minimal diagnosis (propositional case) (c19).

**LLM era (2023 to 2026).** See section 6. Two lines: (1) MBD-style code steps wrapped around an LLM (DRAGO, Matei, SemLoc, TypoNet, Nakos and Forbus); (2) LLM agents diagnosing without a structural model (AIOpsLab, CoffeeBench, OncoRounds, AutoFL).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Diagnoses = minimal hitting sets of minimal conflicts; Reiter and GDE coincide | Adder: conflicts {X1,X2}, {X1,A2,O1}; diagnoses {X1}, {X2,A2}, {X2,O1} | a02, a03, a08, b01 | [E] (theory) |
| Original HS-tree was wrong | Counterexample {{a,b},{b,c},{a,c},{b,d},{b}} misses {a,b}; fixed 1989 with HS-DAG | a07, d15 | [E] |
| Exact algorithms fail on mid-size circuits | In 1 min, share of observations solved: c880 CDA 11.6%, HA 12.4%, SAFARI 100%; c1908 CDA 0%, HA 6.1%, SAFARI 100%; c2670 CDA 0%, HA 5%, SAFARI 100%; c432 CDA 74.1%, HA 71.1%. SAFARI 100% on all 14 circuits, max run 32.2 s (c7552) | a16, b06, c05 | [E] |
| SAFARI quality | Minimal-cardinality diagnosis in 78-100% of cases; at least one order of magnitude faster than CDA/HA; quality fell for strong-fault models from c3540 up | a16 | [S] (one group) |
| Pool all failing observations in one formulation | 1140 of 1140 benchmarks solved (largest about 0.1 s); per-observation LBX/RS enumerated all diagnoses for only 177 and 185 instances | a19, b11 | [E] |
| Same for C programs | C-Pack-IPAs: 31% more programs localised than BugAssist, 36% more than SNIPER, 15% more than HSD (2025 version); 2024 version: 483/486 (99.38%) vs BugAssist 454 (93.42%) vs SNIPER 446 (91.77%); TCAS: CFaults 41/41, SNIPER 7/41 (34 memouts); on ISCAS85 CFaults localises 6% fewer circuits than HSD. Do not mix versions | a23, b12, c03 | [E] |
| Entropy probe choice beats split-in-half and random | More than 50% fewer queries at diagnosis cardinality 2; up to 60% fewer in the robustness runs; about 8 s per query | a20, d12 | [E] |
| Entropy tolerates bad priors | Split-in-half saved at most about 1 query with a very vague prior and few needed queries; beyond 10 queries entropy won even with bad priors; 33,000-axiom ontology solved in 190 s with 5 queries | d12 | [E] (one group) |
| Active testing shrinks candidates geometrically | Average decay p = 0.7, R2 = 0.88; estimate-vs-true correlation avg .972 (min .834) on reduced c880; optimising a scenario took 1 s (74182) to 40 min (c6288) | a17, b07 | [S] |
| Best-first samples biased but fewest measurements | Median estimate correlation best-first vs worst-first: k=6 .76/.50, k=10 .83/.52, k=20 .95/.70, k=50 .98 (best-first). Random best at estimation (75% best, 25% second); best-first best at practical estimates (63% best, 25% second). One case 58 measurements best-first vs 25 random at sample 50 | a22, b08 | [C] (depends on assumed measurement time) |
| RBF-HS memory | Up to 98% less memory; HS-tree up to about 49x more memory; faster in 4 of 10 cases, up to 88% less time | a21, b09, b10 | [S] |
| No reasoner wins everywhere | Power network, 129 instances: junction tree solved 23; SAT preferred-first solved most; BDD 4-12 fewer; software-process set up to 450 minimal candidates | a18, b05, b26 | [E] |
| Intermittent faults cost far more | ISCAS85 g=0.9: persistent 2.7 (c17), 5.5 (c432), 5.4 (c499), 5.3 (c880); intermittent 29-126 observations | d14 | [S] |
| Oracle errors | At least one wrong answer from a quarter of participants; manual test entry cost +37% time, +117% effort; algorithm cannot detect wrong answers | b22, d13 | [C] |
| NetDx | 100% injected faults; 30 of 33 in-scope real faults (33 mapped to 8 classes, one fault injected per class, 3 intermittent counted as failures); humans 14:44 to 33:48 min, NetDx 1:38 min (77 primitives) | a24 = b20 | [S] |
| LLM self-diagnosis breaks correct work | LLM-diagnostic repair broke 11.8% of correct artifacts (1,006 of 8,559); DRAGO 1.3% (110 of 8,528); +12.9 points over zero-shot, +8.7 over LLM-diagnostic repair; PDDL: DRAGO 104 fixes vs 12 regressions, self-review 159 fixes vs 254 breaks | a26 | [S] for gating; regression pattern [E] with d05 |
| Self-revision without oracle regresses | GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-4 HotpotQA 49 to 43; with oracle labels GPT-4 GSM8K 97.5 | d05 | [E] (2023 models) |
| Diagnosis quality limits repair | GPT-4 repair with GPT-4 feedback 33.30% vs human feedback 52.60%; introductory 42.64/62.21, interview 19.33/45.67, competition 3.67/14.67; 16 participants, 40 programs | c13 | [E] |
| Real tool output beats imagined | AutoSD: 73% plausible with real debugger vs 63% ablated; Defects4J v1.2 76 vs LLM-base 87 (v2.0 113 vs 110) | c12 | [S] |
| Verbal confidence is a weak trust signal | Confidence at least 0.9 on 76.2% of answers, only 84.1% correct; GPT-4 failure-prediction AUROC 62.7%; ECE of GPT-3/3.5/Vicuna above 0.377 | c07, d10 | [C] (calibration over explicit options is good, d11) |
| Structured scaffold gives safety, not accuracy | SemLoc 81.4% vs LLM with same inputs 82.0%, no significant difference over 4 LLMs; violations alone rank fault first in 40.9% of tied cases vs 2.2% SBFL, 7.0% Daikon; 68.4% of top answers carry a confirmed patch, 93.6% of those correct; 99.4% of constraints became runtime checks | c06, c07 | [S] |
| LLMs choose next information poorly | OncoRounds: best of 32 models 68%, 1,896 runs; information use R = 0.69 with accuracy, falls 57% to 26% in final round; 91% of reasoning traces above rubric yet decorrelated from accuracy | c10, c11 | [S] |
| Same in QuestBench | o1-preview Logic-Q 49.91%, Planning-Q 42.31% vs GSME-Q 98.01%; Claude 3.5 Sonnet zero-shot 30.09% and 7.53%; GPT-4o 27.39%, 24.49% | d04 | [S] |
| Information-gain question choice beats direct prompting | UoT: +38.1% average; GPT-4 closed-set FloDial troubleshooting 42.5 to 67.8 (main table 43.7 to 67.3), DX 89.4 to 97.0, MedDG 74.9 to 87.9; Llama3-70B FloDial 28.8 to 47.1; p<0.05, 3 repeats; LLM self-evaluation reward lost 5.9%. BED-LLM: +37.4 points on 20 Questions, never fell | d02, d03 | [E] (LLM-simulated probabilities) |
| LLM agents on cloud faults | AIOpsLab acc@1: GPT-4 shell 61.54%, ReAct 53.85%, FLASH 46.15%, GPT-3.5 30.77%, PDiagnose 15.38%, RMLAD 7.69%; RCA ReAct 45.45%, GPT-4 40.90%, GPT-3.5 9.09%; detection ReAct 76.92%. FLASH 59.32% overall. About 11-13 problems per type (one problem = 8 points) | b18, b19 | [E] (inconsistent) |
| Appliance faults | CoffeeBench: Gemini 2.5 Pro 61.1%, Gemini 3.5 Flash 56.8%, Claude 4.5 Sonnet 56.8%; three of 12 models no better than guess-and-eliminate; episode-state tracker cut timeouts below 8% | a25 | [S] |
| Fault localisation vs tokens | Accurate locations cut repair tokens by up to 39.2%; many FL methods cost more than they save; 16,248 trajectories | a29 | [C] |
| LLMs doing GDE steps | 24 hand-made circuits: o3-mini conflicts F1 0.917 +/- 0.249, diagnoses F1 0.784 +/- 0.322; o1 and o3-mini perfect on incidence matrix; gpt-4o and 4o-mini without code interpreter near zero on unseen examples | d01 | [S] |
| Solver-backed LLM pipelines | Logic-LM: +39.2% vs standard, +18.4% vs CoT; GPT-4 ProofWriter 52.67/68.11/79.66, FOLIO 69.11/70.58/78.92, LogicalDeduction 71.33/75.25/87.63, AR-LSAT 33.33/35.06/43.04; PrOntoQA 77.40/98.79/83.20 (CoT wins). SatLM GSM-Sys 21.0/46.5/43.4/69.4; plain GSM no gain (72.7 vs 71.8) | d08, d09 | [C] |
| LLM-built models are flawed | GPT-4 PDDL: 53, 2, 4 errors in 3 domains; GPT-3.5 218+/38/94+; 59 messages fixed 56 factual errors, 3 corrections added errors; LLaMA-2-70b valid PDDL in 94%, behaviourally matching 25% | d06, d07 | [E] |
| Adversarial model check | Detractor off: agreement 97.4% to 41%; 48 of 50 planted wrong rules caught; 128 rules, 3 h, $18.6; 92% reused on a network twice the size; Sonnet 4.6 + TypoNet F1 0.83 on hardest incidents | a30 | [S] (preprint) |
| Mode collapse in LLM hypotheses | 200 samples: Van Gogh 93, Dali 44, Kahlo 37 | d03 | [S] |

## 4. Mechanisms and models

This section is written so an engineer can build the code-run reasoner.

### 4.1 Data structures
- **Components**: list of parts that can fail (gates, rules, code statements, services, input facts).
- **Model**: for each component, a rule giving its output when it is normal (weak-fault model). Optional fault modes per component (Sherlock): known fault behaviours plus an "unknown" mode that predicts nothing (a12).
- **Observation**: known inputs and observed outputs or probe values.
- **Conflict**: set of components that cannot all be normal.
- **Candidate/diagnosis**: set of components assumed faulty.

### 4.2 Step 1: get conflicts
Two ways.
1. **Propagation with dependency tracking (GDE/ATMS)** (a08). Each predicted value stores the set of components used to derive it. When two predictions, or a prediction and an observation, disagree, the union of their dependency sets is a conflict. Keep only minimal conflicts.
2. **Solver-based**: encode model + observation in SAT/SMT with one selector variable per component; an unsatisfiable core is a conflict. Deletion-based minimal-unsatisfiable-subset extraction makes it minimal (used by DRAGO in spirit, a26). QuickXplain is the standard conflict finder in knowledge-base debugging (a20).

### 4.3 Step 2: hitting sets
- **Reference algorithm**: HS-DAG (Greiner correction), breadth first, so smallest diagnoses come first (a04, a07). Memory is exponential in diagnosis size.
- **Memory-limited**: RBF-HS, recursive best-first, linear memory, sound and complete, up to 98% memory saved (a21).
- **Pooling many failing observations**: do not diagnose each failing case separately and intersect. Put all into one MaxSAT / implicit-hitting-set problem (a19, K04). Implicit hitting set: alternate a MaxSAT call that gives a minimum hitting set of the conflicts found so far with a consistency check that returns a new conflict.
- **Anytime mode**: SAFARI-style greedy stochastic search. Start from "all components faulty" (consistent but trivial) and try to flip each to normal, keeping the set consistent via unit propagation; repeat with random orders (a16). It returns a subset-minimal diagnosis for weak-fault models in polynomial time, with no cardinality guarantee. Use when exact fails or a time cap hits.
- **Validation**: brute-force all subsets on random small conflict collections and compare (K02).

### 4.4 Step 3: rank candidates
- Fault prior p per component (one number). Candidate probability under independence: product of p over faulty parts times (1-p) over the rest, then normalise over the candidate set (a09).
- If priors are unknown: all equal and small. Then rank by cardinality and use the crude score of a11. This is the safe default (K27): stated LLM confidence is a poor prior (d10), and entropy selection tolerates a bad prior (d12).
- GDE approximates the chance that a candidate predicts no value at 1/m; the paper calls this suspect (a09).

### 4.5 Step 4: choose the next probe
For each possible probe point (or test input), compute for each possible outcome value the candidates that predict it, then the expected entropy of the posterior. Choose the lowest expected entropy (a09). With equal small priors use S(x) = sum c_k ln c_k (a11). With control inputs, choose test vectors greedily to reduce expected remaining diagnoses (FRACTAL, a17). After the answer: keep candidates that predicted it, drop the others, and recompute conflicts, since new multiple-fault diagnoses can appear (a05). Stop when one diagnosis is left, or the expected gain per cost falls below a cutoff. With n equally likely diagnoses the ideal is log2 n queries (a20).

When the probe is a question to a user or tool (Nakos and Forbus), the same loop works if each question has a predicted answer per candidate (c02, a27).

### 4.6 Step 5: sampling for big candidate sets
When the candidate set is too large, estimate probabilities from k sampled diagnoses. Best-first samples are biased but often need the fewest measurements; random samples estimate better (a22, b08). Pick by whether tests are cheap (random) or expensive (best-first). [C]

### 4.7 Step 6: intermittent and multiple faults
Give every component two numbers: p(c), prior it is faulted, and g(c), chance it works when faulted. Update by Bayes over repeated observations and repeat the probe (d14). Cost is about 10x to 20x that of persistent faults at g=0.9. Eight assumptions apply (one observed variable per instant, inputs known, no memory components, no measurement error, probe does not disturb the system, independent failures, stationary process).

### 4.8 The LLM and the model
Three roles for the LLM, all with evidence:
1. **Translator**: text to formal model (Logic-LM, SatLM, TypoNet) (d08, d09, a30).
2. **Proposer**: writes constraints or models that code runs (SemLoc, Matei) (c06, c01).
3. **Repairer**: edits only the located part after code diagnosis (DRAGO, Matei) (a26, c01).

Never: judge consistency or say which hypothesis is left. LLMs doing the GDE steps reached F1 0.784 on diagnoses and decay with the number of diagnoses (d01).

Model checking: a second pass tries to break each rule with a counterexample; accept only rules that survive (Detractor, a30). Validator feedback fixes LLM-built models: GPT-4 fixed all 56 factual errors with 59 messages (d06).

### 4.9 Acceptance rule
Accept an LLM edit only if the code-measured error weight (conflict count, failed checks) strictly falls (DRAGO, a26). This is the form of G2 we can implement directly.

## 5. What holds up

**Holds up (replicated or several independent sources).**
- Hitting-set characterisation: two independent derivations (Reiter; de Kleer and Williams) agree; Greiner 1989 confirmed the structure but found a bug in the algorithm (a06, a07). [E]
- Exact algorithms do not scale; anytime and SAT-based ones do. Two lines: Feldman 2010, and Ignatiev 2017 with Orvalho 2025 (K03, K04, K24). [E]
- Entropy probe choice beats split-in-half and random: de Kleer 1987/1990 (analysis), Rodler (simulation, 50% to 60%), Feldman (active testing) (K05). [E]
- Information-gain question choice beats direct LLM choice: UoT and BED-LLM are independent and agree; QuestBench and OncoRounds independently show LLMs choose poorly (K11, K20). [E], with the caveat that the probabilities were LLM-simulated.
- LLM self-revision without a trustworthy signal regresses (a26, d05; Huang et al. ICLR 2024 is the d05 source). [E]
- LLM-built models contain errors and need checking (d06, d07, a30) (K21). [E]

**Single-source or contested.**
- Geometric decay of candidates: one group, simulated circuits. [S]
- Scaffold vs plain LLM: SemLoc found no accuracy gain (81.4 vs 82.0); DRAGO found a large regression drop. These fit if the benefit is safety, not accuracy (critique). [C]
- Best-first vs random sampling: ranking flips with assumed measurement time (1 or 10 min) (a22). [C]
- Fault localisation before repair: up to 39.2% fewer tokens, but often costs more than it saves (a29). [C]
- Solver-backed pipelines win on 4 of 5 logic sets, lose on PrOntoQA (d08) and plain arithmetic (d09). [C]
- NetDx: one paper, emulated network; "30 of 33" counts classes (K13). [S]
- Verbal confidence: poor ranking (AUROC 62.7%; 84.1% right at 0.9+) but good over explicit options (c07, d10 vs d11). [C]

**Failures and boundary conditions.**
- The original algorithm was wrong (a07).
- Weak-fault models give many candidates (up to 450 minimal in the software-process set, "too many to be useful") (b05).
- A wrong model gives a wrong or empty diagnosis (b25, K17). No study measured the harm of a 5-10% wrong model (K21).
- Oracle errors: a quarter of human users erred at least once; the algorithm cannot detect it (b22, d13). An empty candidate set after a contradiction is the cheap signal.
- Roy 2024: ReAct correctness 35% vs CoT 39%, but hallucination 4% vs 12% (b16). Adding incident discussions did not help (b17).
- The de Kleer and Williams square/cube scaling claim is unmeasured (a10).
- CFaults is slower than HSD on ISCAS85 and localises 6% fewer circuits (b12).
- Intermittent faults: NetDx counted 3 as failures; cost is about 10x higher (d14, b20).

**Interventions that worked.** Pooling observations (a19); anytime solver with time cap (a16); entropy probe choice (a20, d02, d03); conflict-gated acceptance (a26); validator feedback on LLM models (d06); adversarial model check (a30, preprint); real execution feedback (c12); episode-state tracker (a25: timeouts under 8%).

**Interventions that did not.** More incident text (b17); more steps when feedback is only environment output (accuracy saturates, b19); LLM self-evaluation reward in place of information gain (lost 5.9%, d02); ranking the true fault higher in Rodler's user study (did not make debugging more effective, b22). Prompt ordering moved LLM4FL Top-1 by up to 22%, which signals fragility (c08).

**Evidence quality notes.** Most numbers are circuits or code with simulated faults. Defects4J has contamination risk (b14, c08). AIOpsLab has about 11-13 items per task. The founding papers have almost no empirical tables.

## 6. Language models

**A. LLMs doing the diagnosis steps themselves.**
- d01 (DX 2025): 24 hand-made Boolean and arithmetic circuit examples, each step fed the correct input. o1 and o3-mini perfect on the incidence matrix. o3-mini conflicts F1 0.917 +/- 0.249, diagnoses F1 0.784 +/- 0.322; falls with more diagnoses (examples up to 29 relations, 153 minimal diagnoses). gpt-4o and 4o-mini without code interpreter near zero on unseen examples. Results vary strongly run to run. Errors would compound in a chain. The authors do not present it as a replacement for algorithms.
- Reading: a reasoning model can imitate GDE on small cases. A solver is exact by construction. This supports the code-run reasoner but is not an equal-token test.

**B. LLM + code reasoning (neuro-symbolic).**
- Logic-LM (d08): +39.2% vs standard, +18.4% vs CoT on average. GPT-4: ProofWriter 79.66, FOLIO 78.92, LogicalDeduction 87.63, AR-LSAT 43.04. PrOntoQA: CoT 98.79 beat Logic-LM 83.20. Failures concentrate in the translation step.
- SatLM (d09): GSM-Sys 69.4 vs CoT 46.5 vs ProgLM 43.4 (code-davinci-002); BoardgameQA 79.4 vs 60.7; CLUTRR 68.3 vs 58.9; ProofWriter 99.7 vs 83.7. On plain GSM no gain (71.8 vs 72.7). Wins are larger on search-heavy problems.
- TypoNet (a30, preprint): LLM translates network artefacts to rules, solver reasons, Detractor attacks rules. 97.4% held-out agreement; Detractor off 41%. Sonnet 4.6 with the tool: F1 0.83 on the hardest incidents. A fault-to-symptom theory as a tool improved F1 for every LLM tested.
- DRAGO (a26): five benchmarks, four models, three formalisms. Self-diagnosis broke 11.8% of correct artifacts vs 1.3%. +12.9 points over zero-shot, +8.7 over LLM-diagnostic repair. MUS-style conflict finding, not full hitting sets.
- SemLoc (c06, c07): 809 real bugs from 750 projects. Same accuracy as a plain LLM with the same inputs (81.4 vs 82.0) but checkable. Confidence 0.9+ on 76.2% of answers, 84.1% right.
- Matei 2026 (c01, a28, b24): GPT-5.1 writes BPMN models; code simulates KPIs; MBD with hitting sets over gateways points to a gateway, then a sentence; GPT-5.1 rewrites only that text. After repair, over 90% of 100 regenerated models agreed (city 1), 70% (city 2). Two cases, no baseline, no ground truth.
- Nakos and Forbus (c02, a27, b23): GDE for a semantic parser; synthetic only.
- Not LLM methods but related: Discret2Di (c17) and Steude (c18) feed learned logic or anomaly detectors into consistency-based diagnosis.

**C. LLM agents without a structural model.**
- AIOpsLab (b18, b19): 48 problems. GPT-4 with shell acc@1 61.54%; ReAct 53.85%; FLASH 46.15%; GPT-3.5 30.77%. RCA best 45.45%. Accuracy saturates after a few steps when feedback is only environment output.
- CoffeeBench (a25): 12 models; best one-turn 61.1%; three models at or below guess-and-eliminate; a state tracker helps.
- Roy 2024 (b16): ReAct hallucination 4%, CoT 12%, retrieval 40%; correctness 35%/39%/39%.
- OncoRounds (c10, c11): 32 models, 20 cases, 1,896 runs; best 68%. Dominant errors: search satisficing, anchoring, premature closure.
- AutoFL (b14, b15): 798 bugs; acc@1 up 19.7% over Ochiai on Defects4J (GPT-3.5), 166.7% on BugsInPy with GPT-3.5 and 233.3% with GPT-4; about 20% of 300 explanations described the bug correctly; one GPT-4 run beat five GPT-3.5 runs.
- LLM4FL (c08): Defects4J 675 faults; Top-1 326 vs AutoFL 275 vs Ochiai 121; gain over SoapFL 4.82%.
- Xu 2025 (c09): 13 LLMs on novice programs. Condefects Top-1: o3 312, GPT-4 200, GPT-3.5 148. Reasoning models need little prompt engineering; over-reasoning hurts clarity.
- Shi 2026 (a29): 16,248 trajectories; FL does not consistently raise repair success.
- Olausson (c13), AutoSD (c12), LDB (c14: up to 9.8%), Self-Debug (c15: +2-3% Spider, +9% hardest level, up to +12% elsewhere).
- Kumar 2025 (c20): 3B model tuned on automotive diagnosis 45.32% vs base 27.05% on 876 multiple-choice items. Knowledge, not fault search.

**D. What changed LLM results, by how much.**

| Change | Effect |
|---|---|
| Information-gain question selection | +38.1% (UoT), +37.4 points (BED-LLM) |
| Solver for reasoning | +18.4% over CoT (Logic-LM average); large on search, none on arithmetic |
| Conflict-gated acceptance | regressions 11.8% to 1.3% |
| Adversarial model check | 41% to 97.4% agreement (preprint) |
| Real debugger output | 63% to 73% plausible |
| Human vs LLM diagnosis feed | 33.3% to 52.6% repair success |
| State tracker | timeouts under 8% |
| Accurate fault location | up to 39.2% fewer tokens |
| Reasoning model vs non-reasoning | o3-mini diagnoses F1 0.784 vs near zero for 4o without code interpreter |

**E. Summary of LLM behaviour.** Fluent reasoning is not accuracy (91% of traces above rubric, decorrelated, c11). LLMs are overconfident (d10). They pick the next probe poorly (c10, d04). They break correct work when they self-diagnose (a26, d05). They translate text to formal models with errors (d06, d07). They do well when code does the consistency work and the LLM does translation or located repair. Many LLM figures are from 2023 to 2024 models; 2026 models appear in DRAGO, SemLoc, OncoRounds, CoffeeBench, TypoNet.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, M = memory.

### Add now (established)

1. **Code decides consistency and hits; the LLM never does** (G2/G5, S4, S5). When a task has a model (rules, circuit, code with tests), code computes conflicts and diagnoses; the LLM sees only the located conflict. [E] K01, K07, K08, K23. Ev: a02, a03, a26, c13, d05. Extends G2 and G5; adds no state.
2. **Accept an edit only when a code-measured error count falls** (G2, S5). [E] K07, K23. Ev: a26, d05.
3. **Validate any home-built hitting-set code against brute force; use the Greiner-corrected algorithm** (code hygiene, not schema). [E] K02. Ev: a07.
4. **Anytime solver with a time cap; label non-minimal results** (O). [E] K03, K24. Ev: a16, b06, a19, d16.
5. **Keep the whole evidence set together** (S2/S4): diagnose all failing cases in one pass, not per case. [E] K04. Ev: a19, a23, b12.
6. **Choose the next probe by information gain over an explicit hypothesis set, not by the LLM's pick** (S7 discriminating test, S6 subgoal choice). [E] K05, K11, K20. Ev: a09, a20, d02, d03, d04, c10. Caveat: measured gains used LLM-simulated probabilities.
7. **Use uniform or structure-based priors, not stated LLM confidence** (S, memory). [E] K27. Ev: d10, d03, d12, a11.
8. **State model assumptions and check any LLM-built model before diagnosing** (G, S2). [E] K17, K21. Ev: b25, d06, d07.
9. **Ground in real tool output, not imagined output** (G2). [E] K09. Ev: c12, b19.

### Test first

| Item | Part | Status | Evidence ids | Why test |
|---|---|---|---|---|
| LLM + code conflict/hitting-set vs LLM-only at equal tokens | O (code-run reasoner), S4 | [C] K19 | d01, d08, d09, a26 | No direct test exists; Logic-LM loses on PrOntoQA |
| Code-computed entropy probe vs LLM-simulated EIG vs LLM free choice | O, S7 | [S] for the code form, K20 | d02, d03, d04, c10 | Gain known only for LLM-simulated probabilities |
| LLM writes the model, code reasons, adversarial model check | S2, G | [S] K22, [C] K14 | a30, d06, d07 | One preprint |
| Conflict-based gating beyond specs and PDDL | G2 | [S] K23 | a26, d05 | Only specs and PDDL |
| Effect of 5-10% wrong rules on diagnosis | G | open K21 | b25, d06 | No source measured it |
| Repeat probes under intermittent faults | S, O | [S] theory, no LLM study, K25 | d14 | LLM cost unknown |
| Re-ask on empty candidate set (wrong probe answers) | G, S6 trigger | [C] K26 | d13, b22 | No LLM measurement |
| Localise before repair (token ledger) | O | [C] K15 | a29, b14 | Costs often exceed savings |
| Sample agreement as hint of correctness | G4 | [S] K16 | b15 | Samples correlated |
| Solver choice by instance features | O | [E] in principle K18, unknown for our sizes | a18, b26 | No single winner |
| Fault-mode set with an "unknown" mode | S2, O | [S] | a12 | Classical circuits only |

## 8. Concrete tests on our bench

All arms get equal total tokens; setup and code-call cost counts (G7). Run 3 seeds. Log per SCHEMA section 6.

**T1. Code-run hitting set vs LLM-only (K19).**
- Items: generated circuit puzzles (adders, small ALUs, 8 to 40 gates, 1 to 3 faults) and rule-base fault puzzles with labelled ground truth. About 60 items per size band.
- Arms: (A) plain LLM in reasoning mode gives the diagnosis set; (B) LLM translates to a model, code computes conflicts and minimal hitting sets, LLM only reports; (C) LLM does the GDE steps with a code interpreter.
- Metric: exact match of the minimal-diagnosis set; F1 over diagnoses; tokens.
- Expected: B above A by more than 10 points at 3 or more faults; no gain on tiny single-fault items; translation errors are the main loss (from d08).

**T2. Probe selection (K20).**
- Items: circuits with a hidden fault and a probe budget; plus a device-style troubleshooting dialogue with an explicit candidate list.
- Arms: LLM free pick; LLM-simulated EIG (UoT style); code entropy over the candidate set with uniform prior; code crude score (a11).
- Metric: probes to unique diagnosis; success within budget.
- Expected: code entropy at or above LLM-simulated EIG; both far above free pick (about +35 points, from d02, d03).

**T3. Gated acceptance (K07, K23).**
- Items: our BrainTeaser-style puzzles and ARC items with a held-out check; code tasks with partial checks.
- Arms: LLM self-revision; LLM revision accepted only when the code error count strictly falls; no revision.
- Metric: regression rate (right to wrong), fix rate, final accuracy.
- Expected: regression under 3% vs 10% or more for self-revision (a26).

**T4. Wrong-model harm (K21).**
- Items: T1 circuit set with 0, 5, 10, 20% of component rules corrupted.
- Arms: no check; counterexample model check (Detractor style); validator feedback.
- Metric: top-1 diagnosis correct; empty-set rate.
- Expected: accuracy falls with corruption; the check recovers most of it; empty-set rate is a usable signal.

**T5. Model building (K22).**
- Items: 30 rule sets described in text with 5 to 20 planted wrong rules.
- Arms: LLM writes model alone; plus adversarial counterexample step; plus validator feedback.
- Metric: share of planted errors caught; agreement with ground truth.
- Expected: about 48 of 50 caught as in a30; agreement 90% or more vs about 40% without the check.

**T6. Wrong probe answers (K26).**
- Items: T2 items with injected answer-error rate of 0, 5, 10, 20%.
- Arms: no recovery; re-ask on empty candidate set; ask twice and compare.
- Metric: final diagnosis accuracy; extra probes.
- Expected: re-ask on contradiction recovers more than half of the loss.

**T7. Intermittent faults (K25).**
- Items: circuits with one intermittent fault (g = 0.9).
- Arms: single observation; fixed repeat count; Bayesian update with p and g (d14).
- Metric: correct diagnosis; observations used.
- Expected: single pass fails often; Bayes uses fewer observations than a fixed repeat count.

**T8. Pooling (K04).**
- Items: multi-failure code tasks with 3 to 20 failing tests.
- Arms: per-failure diagnosis then intersect; all failures in one conflict step.
- Metric: share with a diagnosis consistent with all failures; tokens.
- Expected: pooled better, as in a19, a23.

**T9. Solver mode (K24).**
- Items: generated circuits at 10, 40, 150, 500 gates.
- Arms: exact HS-DAG; anytime stochastic; MaxSAT implicit hitting set; 60 s cap.
- Metric: solved share; cardinality gap; wall time.
- Expected: exact fails past a few hundred gates (a16); anytime always answers.

## 9. What does not transfer, and why

- **Needs a model.** Many of our items (ARC, word puzzles, open ideas) have no component model, so MBD does not apply directly. It applies to rule systems, circuits, programs with tests and plans with checks.
- **Weak-fault models give too many candidates.** Up to 450 minimal candidates (b05). The agent must rank, not list.
- **Parsimony is subset-minimal, not probable.** A real multi-fault case can hide behind a smaller diagnosis (a02, a13).
- **Founding results are theory.** Reiter and GDE ship no benchmark tables. Do not cite them as effect sizes.
- **Circuit and code benchmarks use simulated faults.** Defects4J, TCAS and ISCAS85 faults are seeded or student bugs; contamination risk for LLM results (b14, c08).
- **NetDx**: emulated P4 network, 33 faults mapped to 8 classes; needs a hand-built domain model (a24).
- **Interactive debugging needs a competent oracle.** Humans err; LLM oracle error is unmeasured (b22, d13).
- **UoT and BED-LLM probabilities come from the LLM.** Hypothesis spaces are medical conditions, entities and dialogue flows, not device models (d02, d03).
- **Logic-LM and SatLM are not diagnosis** and used older models (d08, d09).
- **Verbal confidence studies used 2022 to 2023 models** (d10, d11); current models may differ.
- **OncoRounds** is hematologic oncology, cases by one clinician (c10).
- **Dynamic and sequence hypothesis spaces** (Grastien) are harder than sets and mostly beyond our items (a18).
- **Nakos and Forbus**: synthetic, no user data (a27).

## 10. Open questions

1. Does a code-run conflict and hitting-set step added to an LLM agent beat LLM-only at equal tokens, and for which fault counts? (K19)
2. Fully code-computed entropy on a device model vs LLM-simulated EIG: how big is the gap?
3. What does a 5-10% wrong model do to top-1 diagnosis, and how often does it give an empty set? (K21)
4. Can an LLM produce a good enough model from text, and what share of tasks have a usable model? Only 25% of valid LLM PDDL domains matched reference behaviour (d07).
5. Does conflict-based gating transfer outside specifications and PDDL? (K23)
6. How often do LLM oracles give wrong probe answers, and how robust are diagnoses to them? (K26)
7. Which solver mode should a token-limited agent call, and at what size does exact fail inside an LLM loop? No LLM-agent timing study exists (K24).
8. Multiple and intermittent faults in LLM agents: no LLM study (K25).
9. Is sample agreement a better prior than stated confidence? (K27, K16)
10. What do Bylander 1991, Davis/Genesereth 1984 and de Kleer 1992 add as boundary conditions? Not read in full; abduction hardness stays secondary-sourced.
11. Do 2026 reasoning models (o3-mini diagnoses F1 0.784) close the gap with exact solvers at 5 or 20 diagnoses? (d01)
12. Why do ReAct agents hallucinate less but score lower than CoT (b16)? Would a model step fix that?

## 11. Sources

[V] = opened and read this session. [M] = snippet or listing only.

- [V] Reiter (1987) A theory of diagnosis from first principles. https://cse.sc.edu/~mgv/csce580sp14/reiter-diagnosis.pdf (a01-a06, b01, b02, b25)
- [V] Greiner, Smith, Wilkerson (1989) A correction to the algorithm in Reiter's theory of diagnosis. https://cse.sc.edu/~mgv/csce580sp14/greinerCorrectionReiter.pdf (a07; d15 restates it; b03 citation-only [M])
- [V] de Kleer, Williams (1987) Diagnosing multiple faults. AIJ 32(1):97-130 (a08-a10); b04 listing only [M] https://portal.mardi4nfdi.de/wiki/Publication:1101418
- [V] de Kleer (1990) Using crude probability estimates to guide diagnosis (a11).
- [V] de Kleer, Williams (1989) Diagnosis with behavioral modes, IJCAI-89 (a12).
- [V, OCR-poor] de Kleer, Mackworth, Reiter (1992) Characterizing diagnoses and systems (a13).
- [V] de Kleer (2011) Diagnosing multiple persistent and intermittent faults. http://www.dekleer.org/Publications/interm-ijcai-final.pdf (d14)
- [M] Davis (1984) and Genesereth (1984), via de Kleer and Williams and Reiter (a14).
- [M] Bylander, Allemang, Tanner, Josephson (1991) complexity of abduction, via a15 and d16. https://www.sciencedirect.com/science/article/pii/000437029190062X
- [V] Feldman, Provan, van Gemund (2010) SAFARI. https://arxiv.org/abs/1401.3848 (a16, b06, c05)
- [V] Feldman, Provan, van Gemund (2010) FRACTAL active testing. https://arxiv.org/abs/1401.3850 (a17, b07)
- [V] Grastien, Haslum, Thiebaux (2023) A more general theory of diagnosis from first principles. https://arxiv.org/abs/2309.16180 (a18, b05, b26)
- [V] Ignatiev, Morgado, Marques-Silva (2017) MBD of multiple observations with implicit hitting sets. https://arxiv.org/abs/1707.01972 (a19, b11)
- [V] Rodler (2016) Interactive debugging of knowledge bases. https://arxiv.org/abs/1605.05950 (a20, d12, d13)
- [V] Rodler (2020/2022) RBF-HS. https://arxiv.org/abs/2009.12190 and https://arxiv.org/abs/2010.04282 (a21, b09, b10)
- [V] Rodler, Elichanova (2020/2022) Do we really sample right in model-based diagnosis? https://arxiv.org/abs/2009.12178 (a22, b08)
- [M] Rodler (2023) Don't treat the symptom, find the cause! https://arxiv.org/abs/2306.12850 (a31 listing only; b22 thesis summary read [V])
- [V] Orvalho, Janota, Manquinho (2024) CFaults. https://arxiv.org/abs/2407.09337 (a23, b13, c04); Orvalho et al. (2025) https://arxiv.org/abs/2512.02898 (b12, c03)
- [V] Wu, Yu, Lee, Srinivasa, Zhai, Varghese, Tamir (2025) NetDx. https://arxiv.org/abs/2506.23083 (a24 = b20)
- [V] McCabe, Lukens, Huang (2026) CoffeeBench (a25; URL in evidence_a.jsonl).
- [V] Vaccarino et al. (2026) DRAGO (a26; URL in evidence_a.jsonl).
- [V] Nakos, Forbus (2024) Interactively diagnosing errors in a semantic parser. https://arxiv.org/abs/2407.06400 (a27, b23, c02)
- [V] Matei et al. (2026) Ambiguity detection and elimination in automated executable process modeling. https://arxiv.org/abs/2604.10884 (a28, b24, c01)
- [V, body skimmed] Shi, Yang, Chen (2026) From finding to fixing (a29; URL in evidence_a.jsonl).
- [V] He, Apostolaki (2026) TypoNet (a30; URL in evidence_a.jsonl).
- [V] Roos (1993/2022) Efficient model based diagnosis. https://arxiv.org/abs/2209.09819 (b21)
- [V] Kang, An, Yoo (2024) AutoFL. https://arxiv.org/abs/2308.05487 (b14, b15)
- [V] Roy et al. (2024) Exploring LLM-based agents for root cause analysis. https://arxiv.org/abs/2403.04123 (b16, b17)
- [V, tables garbled] Chen et al. (2025) AIOpsLab. https://arxiv.org/abs/2501.06706 (b18, b19)
- [V] Yang et al. (2026) SemLoc. https://arxiv.org/abs/2603.29109 (c06, c07)
- [V] Rafi et al. (2025) LLM4FL. https://arxiv.org/abs/2409.13642 (c08)
- [V] Xu et al. (2025) novice program fault localisation. https://arxiv.org/abs/2512.03421 (c09)
- [V] Braitsch et al. (2026) OncoRounds. https://arxiv.org/abs/2607.10275 (c10, c11)
- [V] Kang, Chen, Yoo, Lou (2023) AutoSD. https://arxiv.org/abs/2304.02195 (c12)
- [V] Olausson et al. (2024) Is self-repair a silver bullet? https://arxiv.org/abs/2306.09896 (c13)
- [V] Zhong, Wang, Shang (2024) LDB. https://arxiv.org/abs/2402.16906 (c14)
- [V] Chen et al. (2024) Self-Debug. https://arxiv.org/abs/2304.05128 (c15)
- [V] Englhardt et al. (2023) LLMs for embedded systems. https://arxiv.org/abs/2307.03817 (c16)
- [V] Moddemann et al. (2023) Discret2Di. https://arxiv.org/abs/2311.03413 (c17)
- [V] Steude et al. (2023) Diagnosis-driven anomaly detection. https://arxiv.org/abs/2311.15924 (c18)
- [V] Bertossi (2026) Consistency-based diagnosis and actual causality. https://arxiv.org/abs/2605.08688 (c19)
- [V] Kumar et al. (2025) Domain-specific small LMs. https://arxiv.org/abs/2511.21748 (c20)
- [V, abstract only] Yang et al. (2025) PHM-Bench. https://arxiv.org/abs/2508.02490 (c21)
- [M] AutoCodeRover https://arxiv.org/abs/2404.05427; Automated repair of C programs https://arxiv.org/abs/2509.01947; FuseFL https://arxiv.org/abs/2403.10507; SiblingRepair https://arxiv.org/abs/2605.06209; LogEval https://arxiv.org/abs/2407.01896; Probabilistic ML for industrial diagnosis https://arxiv.org/abs/2509.18810; Integrated novelty detection https://arxiv.org/abs/2610.19347 (c22-c28)
- [V] Sztyber-Betley et al. (2025) Are diagnostic concepts within the reach of LLMs? DX 2025. https://drops.dagstuhl.de/entities/document/10.4230/OASIcs.DX.2025.2 (d01)
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271 (d02)
- [V] Choudhury et al. (2026) BED-LLM. https://arxiv.org/abs/2508.21184 (d03)
- [V] Li, Kim, Wang (2025) QuestBench. https://arxiv.org/abs/2503.22674 (d04)
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d05)
- [V] Guan et al. (2023) LLMs to construct and use world models. https://arxiv.org/abs/2305.14909 (d06)
- [V] Oswald et al. (2024) LLMs as planning domain generators. https://arxiv.org/abs/2405.06650 (d07)
- [V] Pan et al. (2023) Logic-LM. https://arxiv.org/abs/2305.12295 (d08)
- [V] Ye et al. (2023) SatLM. https://arxiv.org/abs/2305.09656 (d09)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (d10)
- [V, partly read] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (d11)
- [M] d16 status note (Bylander, de Kleer 1992 second copy, Davis/Genesereth not opened).
