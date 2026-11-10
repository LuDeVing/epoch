# Readings in model-based diagnosis: deep document

*Subfield C09.09. Standard reference: Hamscher, Console, de Kleer (eds.), Readings in Model-Based Diagnosis, Morgan Kaufmann, 1992. Evidence ids (a01..d17) are in evidence_a-d.jsonl; claim ids (C09.09-K01..K29) are in claims.jsonl; the cross-check is in critique.md. The book itself was NOT opened. Its content is known through Reiter 1987 (opened), later reviews and citations. No number below comes from the book.*

## 1. What it is

Model-based diagnosis (MBD) finds what is broken in a system from two things: a model of how the system should behave, and observations of how it does behave. The model says what each component does when it is normal. A fault is a component that is not normal. No fault dictionary and no past failures are needed. This is called "diagnosis from first principles".

The 1992 Readings volume collects the founding papers of the field: Davis on reasoning from structure and behaviour, Genesereth, de Kleer and Williams on GDE (the General Diagnostic Engine), Reiter's theory, and later work on fault models, probe selection and abstraction. It is the standard reference. Semantic Scholar lists about 703 citations (c01).

The core loop is short.

1. Write a system description SD (components and their normal behaviour).
2. Take observations OBS.
3. If SD plus "all components normal" plus OBS is inconsistent, there is a conflict.
4. Find the sets of components that cannot all be normal (conflict sets).
5. A diagnosis is a minimal set of components that, if abnormal, makes everything consistent again. It is a minimal hitting set of the conflict sets.
6. Choose a new measurement that best splits the remaining diagnoses. Measure. Repeat.

Why it matters for our agent. This is a worked, formal theory of what our schema calls S3 to S6: generate hypotheses, test them, revise, choose the next test. It gives (a) a checkable object (a conflict), (b) a program-side way to turn conflicts into candidates (hitting sets), (c) a way to pick the next probe, and (d) known failure modes of the algorithms. It also has a small, growing body of LLM tests (2023 to 2026). They are mostly negative for free-form use and positive when code holds the state.

## 2. History and theories in depth

**Davis and Genesereth (early 1980s).** Davis showed that troubleshooting can work from structure and behaviour, not from rules of thumb. Genesereth added reasoning about faults from device models. We know them only through Reiter's related-work section (a07). Reiter lists four differences from Genesereth: any logic, multiple faults, a real algorithm, and handling of measurement results (a07).

**de Kleer and Williams, 1987, GDE.** GDE keeps assumptions (each component is normal), records which assumption sets led to a contradiction (using an ATMS, an assumption-based truth maintenance system), ranks candidate faults by prior probability, and chooses the next probe by expected entropy. We know it through Grastien et al. (a10) and citations only (c25 not opened).

**Reiter, 1987, "A theory of diagnosis from first principles"** (opened: a01 to a07, a24, a25, a27).

- A diagnosis for (SD, COMP, OBS) is a minimal set Delta of components such that SD plus OBS plus "components in Delta are abnormal, all others normal" is consistent (Definition 2.4, a02).
- A conflict set is a set of components such that SD plus OBS plus "all of them normal" is inconsistent (a03).
- Theorem 4.4: diagnoses are exactly the minimal hitting sets of the collection of conflict sets (a03).
- Proposition 3.1: a diagnosis exists iff SD plus OBS is consistent. Proposition 3.2: the empty set is the only diagnosis iff there is no conflict (a02).
- Worked full adder: 5 components (X1, X2, A1, A2, O1). Input 1,0,1 gives outputs 1,0 and both outputs are wrong. There are exactly 3 diagnoses: {X1}, {X2,O1}, {X2,A2} (a01, a02).
- The HS-tree (hitting-set tree) algorithm builds diagnoses one conflict at a time and calls a theorem prover only when needed. Example 4.7 (7 sets) yields 6 minimal hitting sets with 13 accesses to the collection. In the full adder only 2 or 3 of 12 possible conflicts were ever computed (a04).
- Measurements (section 5). In the Davis multiplier-adder device (5 components, 4 diagnoses), measuring out(M2)=5 contradicted all 4 old diagnoses and created 4 new ones, all supersets: {M1,M2,M3}, {M1,M2,A2}, {M2,M3,A1}, {M2,A1,A2} (a05). So new evidence can ADD candidates. Diagnosis is nonmonotonic.
- Section 6 links diagnosis to default logic (Theorem 6.1, a06). The theory is not decidable in general because it needs a consistency test (a25). Caching and special-purpose provers help (a27).

**Greiner, Smith, Wilkerson, 1989: a correction** (opened, d01, d02). Reiter's pruning rule can lose minimal hitting sets when conflict sets are not minimal. Worked example: conflict collection {{a,b},{a},{b}}. If the root is not relabelled with the subset {b}, the "b" branch is pruned too (because {a} was already found) and an answer is lost. The fix is HS-DAG (hitting-set directed acyclic graph). Theorem 4.1 has a three-part proof: basic HS-DAG without pruning finds all minimal hitting sets; pruning removes none of them; pruning removes all non-minimal ones (d02). Take-away: a famous, published, hand-checked algorithm had a bug. Do not trust a hand-written version, by a model or a person, without checking it against a vetted solver.

**Hitting-set engineering (2000s to 2017).** Wotawa 2001 gave an HS-tree variant (via b07). Gainer-Dewar and Vera-Licona (2016, b07, b08) benchmarked hitting-set algorithms. HTC-BDD beat close rivals by 4 to 10 times on many inputs but often used up 32 GB of memory and has no cutoff mode. MMCS and RS use little memory and allow cutoff. They found no formal complexity analysis of HS-DAG or HST (b07). Jannach, Schmitz, Shchekotykhin (2016, b09 to b11) parallelised MBD: 4 threads gave speedups of 2.28 to 3.75; up to 5.20 (81 percent shorter run) with more threads on a 12-core server. Sequential versus parallel differed (p<=0.05) in 95 of 100 scenarios.

**Greedy and stochastic search.** Feldman, Provan, van Gemund (2008 AAAI, 2010 JAIR 38; b15 to b18) introduced SAFARI, a greedy stochastic search. On ISCAS85 circuits with weak-fault models it solved 100 percent of tests on every circuit. The complete methods CDA and HA collapsed (c432 CDA 74.1, HA 71.1; c1908 CDA 0, HA 6.1; c3540 HA 1.1; c6288 3.5; c7552 3.9) (b15; critique item 8). The 2008 and 2010 papers are the same group, not independent replications (critique). Quality is a separate question from success: with strong-fault models it worsens from c3540 upward (b16).

**General theory, 2023.** Grastien, Haslum, Thiebaux (a08 to a11, a26) restate diagnosis for any preference relation and give search strategies PLS, PLS+r, PFS, PFS+e, PFS+ec (preferred-first search with conflicts). On 129 power-network alarm instances (2 to 146 alarms) PFS+ec with SAT solved 12 more than BDD and 4 more than PFS with a heuristic solver (a09). Kernel diagnoses can be infinite over multiset fault spaces (a10).

**Multiple observations, 2017.** Ignatiev, Morgado, Marques-Silva (b13, b14): pooling the conflicts of many failing runs (IHSD) solved all 1140 generated instances, the largest in about 0.1 s. At r=500, k=2000 the pooled formula had 6,510 variables; the merged "aggregated" formula had 3,269,512.

**Neighbour traditions that matter for LLM work.** Software fault localisation (Ochiai and relatives), scientific debugging (AutoSD, c17), cloud root-cause analysis (RCA) by LLM agents, and sequential diagnosis in medicine (SDBench) are all MBD-like tasks. Sequential diagnosis is the probe-selection problem again.

## 3. Core findings with exact numbers

Status: "established" means two or more independent sources (generously counted; see critique). Claim ids K01 to K29 are in claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A diagnosis is a minimal hitting set of conflicts; conflicts are mechanically checkable | Full adder: 3 diagnoses {X1}, {X2,O1}, {X2,A2} | Reiter 1987 (a01-a03); Grastien 2023 (a08) | established (K01) |
| New measurements can add diagnoses (supersets); elimination is not monotone | Davis device: 4 old diagnoses killed, 4 new supersets appear after out(M2)=5 | Reiter 1987 (a05) | single-source (K02) |
| Reiter's HS-tree pruning can lose minimal hitting sets; HS-DAG repairs it | Example {{a,b},{a},{b}}; 3-part proof | Greiner 1989 (d01, d02); Reiter (a04) | established (K03) |
| Vetted hitting-set solvers beat classic algorithms | HTC-BDD 4-10x faster but 32 GB limit; MMCS and RS low memory | Gainer-Dewar 2016 (b07, b08); Ignatiev 2017 (b13) | established (K04) |
| Pool many failing observations; do not merge into one formula | r=500: 6,510 vars vs 3,269,512 vars; 0.49 s vs about 6.2 s (build time excluded) | Ignatiev 2017 (b13, b14) | established (K05) |
| Greedy or preferred-first search beats exact methods on large circuits | SAFARI 100 percent everywhere vs CDA 0-74.1, HA 1.1-71.1; PFS+ec solved 12 more of 129 than BDD | Feldman 2010 (b15); Grastien 2023 (a09) | established (K06) |
| Weak-fault models search easily; strong-fault models degrade on big circuits | Quality worsens from c3540 up | Feldman 2010 (b16); de Kleer-Williams via a10 | established (K07) |
| LLMs on MBD objects: conflicts good, diagnoses worse, strong models only | o3-mini conflicts F1 0.917 +/-0.249, diagnoses 0.784 +/-0.322; 4o-mini incidence matrix F1 0.47, accuracy 0.00; o1 and o3-mini incidence F1 1.00 | Sztyber-Betley 2025 (b01-b03) | single-source (K08) |
| More domain knowledge in the prompt does not fix it | 4o-mini worst, o1 best across prompt styles; tool use mattered | Sztyber-Betley 2025 (b04, c03) | established (K09), thin |
| Prompt-described algorithm is not followed; an outside controller is | GPT-5.1 maj@3 F1 ReAct 8.6 vs EoG 86.1; GPT-OSS-120B 5.7 vs 79.4; Kimi K2 28.6 vs 83.0; Gemini 3 Flash 74.3 vs 92.1; ReAct told the EoG algorithm: recall maj@3 2.9 / 0.0 / 0.0 | Jha 2026 EoG (c10, c11, a20) | established (K10), shared authors with ITBench |
| Pass@k overstates reliability | GPT-5.1 ReAct pass@3 22.9 vs maj@3 8.6; Gemini 3 Flash 89 percent pass vs 74 percent maj (the "51" in a20 is a different measure; critique) | EoG (c10, a20); Plank 2026 run SDs (c22) | established (K11) |
| Free-form agents are poor at real incident diagnosis | ITBench gpt-4o pass@1 13.81 (Table 4) or 18.10 (Table 19); traces off 9.52 (appendix); OpenRCA perfect 3.9-12.5 percent over 1,675 runs | ITBench (c12, a18); Kim 2026 (c13, a19) | established (K12) |
| RCA agent failure modes | Hallucinated interpretation 71.2, incomplete exploration 63.9, Symptom-as-Cause 39.9, No Cross-Validation 18.6 percent of runs | Kim 2026 (c13) | single-source (K13), LLM-coded |
| Locating the error is hard; fixing it given the location is easy | GPT-4 52.87 location accuracy; true location +18.04 to +43.92; random location +5.16 to +21.57, losses to -15.91 | Tyen 2024 (b23, b24) | single-source (K14) |
| Intrinsic self-correction does not help | GPT-3.5 CSQA 75.8 to 41.8; GPT-4 GSM8K 95.5 to 89.0, HotpotQA 49.0 to 43.0; 2026: strongest model corrects 16.7 percent of its errors | Huang 2024 (b25, b26); CorrectBench (d06); Li 2026 (d07) | established (K15, K27) |
| Real execution output is the strongest localisation signal | Error log removed: Top-1 -25.6 percent; AutoSD plausible patches 73 vs 63 percent with debugger ablated | Wu 2023 (b19, b20); Kang 2023 (a22, c17) | established (K16) |
| LLM localisation collapses with large context | Class level 49.9 percent worse than SmartFL (function level 46.9 percent better) | Wu 2023 (b19); Kang AutoFL (b21) | established (K17) |
| LLM explanations are often wrong even if the location is right | About 20 percent of 300 explanations accurate; 56.7 percent of 60 bugs had at least one | Kang AutoFL (b22, c19); AutoSD human study N=20 (c18) | established (K18) |
| Model size drives hit rate and hallucinated components | Hit rate Gemini 2.5 Flash 79.5, Mistral Large 76.9, Llama 4 Scout 38.5, Mistral 7B 25.6, Phi-2 0.0; hallucination 20.5 and 7.7 for the top two, over 70 for most small models; 1 of 13 models named the double fault | Plank and Wotawa 2026 (c04, a14, a15, c24) | single-source (K19) |
| Familiar textbook circuits inflate scores | Phi-2 powertrain 1.05 weighted score, anomalously high | Plank 2026 (c05, c06) | single-source (K20) |
| LLM on top of an MBD engine (explain or label only) looks good | FLEX Mistral 7B F1 0.99; FaultExplainer GPT-4o 7 of 11, o1-preview 9 of 11 faults | Muehlburger 2024 (c07); Khan 2024 (c09); Dave 2024 (c08) | contested (K21), no ablation |
| Accept-only-if-better loops lift scores | TN-AutoRCA Gemini-2.5-Pro F1 58.99 to 91.79 | Wu 2025 (a21, c15); Gao 2026 (c16) | contested (K22), tuned benchmarks |
| Belief retraction helps weaker models | +6.9 percent (GPT-5.1) to +64.3 percent (GPT-OSS-120B) relative maj@3 recall | EoG ablation (c11) | single-source (K23) |
| Code-ranked next test beats the LLM choosing the test | Three clinical datasets, GPT-4o-mini and GPT-4o, 5 seeds; KL stopping rule cut tests about 50 percent | ACTMED (d11) | single-source (K25) |
| Structured panel (differential, challenger, test chooser, cost steward) cuts cost at equal accuracy | 304 NEJM cases: MAI-DxO 79.9 percent at $2,397 vs bare o3 78.6 at $7,850; 85.5 at $7,184 with ensembling; GPT-4o 49.3 at $2,745; physicians 20 at $2,963 | Microsoft AI 2025 (d09, d10) | single-source (K26), no per-role ablation |
| Execution-grounded trace estimate is cheap | Trace F1 about 90, Hit@3 81 percent on 785 industrial cases, 93 percent fewer tokens | Yaraghi 2026 (d14) | single-source (K28) |
| No test found of LLM conflicts inside a hitting-set loop, GDE-style probe choice, or weak versus strong fault choice | 0 hits in about 10, 8 and several query variants | d04, d13, d17 | unsupported (K24, K29); absence probable, not certain |

## 4. Mechanisms and models

Written so an engineer can build them.

### 4.1 Conflicts and hitting sets

Data: components COMP = {c1..cn}. Each has a behaviour rule: if normal, output = f(inputs). Observations fix some inputs and outputs.

1. Conflict detection. Assume every component is normal. Propagate inputs through the model. Compare with observed outputs. A mismatch is a contradiction. The components whose normal behaviour was used to derive it form a conflict set.
2. Minimality. A conflict is minimal if no proper subset is also a conflict. Non-minimal conflicts are valid but make the tree algorithms fragile (Greiner).
3. Hitting sets. Given conflicts C1..Ck, a hitting set H meets every Ci. A diagnosis is a minimal H.
4. Loop. For a candidate H, assume only H abnormal and test consistency. If inconsistent, the solver returns a new conflict disjoint from H. Add it and recompute.

HS-DAG in plain steps (Greiner 1989, d02):
1. Make a root. Label it with a conflict from the prover, or "ok" if none exists.
2. For each component c in the label, make an edge labelled c to a child. The child's path set H is the edge labels from the root.
3. If a node with the same path set exists, reuse it (this makes it a DAG).
4. If H is a superset of a diagnosis already found, close the child.
5. Else ask for a conflict disjoint from H. None means H is a diagnosis. Otherwise label the child with it.
6. Pruning: if a new label is a proper subset of another node's label, relabel that node and drop edges whose labels are not in the new label. Reiter's original left this relabel step out (d01).

Engineering rule: do not hand-write this in the agent. Call MMCS or RS from a library (b08), or any tested enumerator. Check model-written routines against a reference on random conflict families.

### 4.2 Measurements and the nonmonotone candidate set

After a measurement, add it to OBS and recompute conflicts. Some old diagnoses die and supersets of them can appear (a05). Never keep one list and cross names off it. Keep the observations and the conflicts, and re-derive the candidates from the conflicts after every observation.

### 4.3 Probe selection

Reiter notes that naive divide-and-conquer on candidates fails because a measurement adds supersets (a05). GDE chooses the next probe by minimum expected entropy (via a10, citation only). Steps:
1. For each candidate d, take a prior p(d) (product of component fault priors, normalised).
2. For each probe point q, predict the value v under each candidate.
3. Group candidates by predicted value. The posterior for value v is that group's weight.
4. Pick q with the smallest expected remaining entropy: sum over v of P(v) times entropy of the posterior given v.
5. Measure q. Update. Go to step 1.

ACTMED (d11) is the LLM analogue. The model only proposes possible outcomes and likelihoods. A program computes expected information gain and picks the test. This beat the model choosing tests itself. A KL stopping rule cut tests about 50 percent.

### 4.4 Preferred-first search with conflicts (anytime)

Exact hitting-set enumeration is too slow for large systems. Preferred-first search (PFS+ec, a08, a09):
1. Keep a priority queue of candidate fault sets, ordered by preference (fewest faults or highest prior).
2. Pop the best. Test consistency with a solver.
3. If consistent, report it as a diagnosis (anytime output).
4. If not, the solver returns a conflict. Push the successors that add one component of that conflict.
5. Stop on budget.

SAFARI (b15) is the greedy stochastic version. Start with all components faulty (always consistent). Flip components to healthy in random order, keep each flip if still consistent, stop after a fixed number of flips and retries.

### 4.5 Fault models

Weak-fault model: a faulty component may output anything. Easy to search. Strong-fault model: the model says what a fault does (stuck-at, bias). It discriminates better and is harder to search (b16). A reasoning problem with unknown failure modes supports only the weak model.

### 4.6 Pooling

With many failing checks, build one conflict family from all of them and hit it once (IHSD, b13, b14). Do not diagnose each alone and merge, and do not conjoin everything into one giant formula.

### 4.7 Graph-guided investigation (EoG)

Jha 2026 (c10, c11). A deterministic controller holds a dependency graph. The LLM sees one node at a time, labels it (cause, symptom, unknown) and explains. The controller does traversal, belief propagation and retraction of earlier labels when new evidence arrives. Cost: a graph and about 5,000 lines of domain code (critique). Portable idea: outside state, local judgement, retraction.

## 5. What holds up

**Holds (two or more independent sources).**
- Diagnoses are minimal hitting sets of conflicts (K01). A proven result, restated in later general theory.
- The original HS-tree pruning was wrong and the correction is proven (K03). The count of two is generous: one paper corrects the other.
- Vetted solvers are much faster than classic algorithms (K04).
- Pooling observations scales (K05).
- Greedy or anytime search finds diagnoses where exact methods time out (K06). Success means "found a diagnosis", not "found the best one" (critique).
- Self-correction without external feedback does not help, from GPT-3.5 in 2023 to reasoning models in 2025 and 2026 (K15, K27). Li 2026 is a single-author preprint. No test on diagnosis tasks with a reasoning model.
- Real execution beats imagined execution for localisation (K16). Large context hurts (K17).
- A prompt that describes the algorithm is not followed; a controller is (K10). Pass@k misleads (K11).

**Failures, boundary conditions, weak spots.**
- Reiter's original algorithm bug (Greiner 1989).
- Divide-and-conquer probing fails because of added supersets (a05).
- Prompt warnings against known RCA pitfalls did not help. A richer tool-error protocol cut pitfall rates by about 14 and 15 points (GPT-5 mini, Claude Sonnet 4) (c14). Mitigation tests had 2 to 3 successes, so they are weak.
- ITBench disagrees with itself (13.81 vs 18.10 for gpt-4o diagnosis). The trace-removal drop is 18.10 to 9.52 in the appendix (critique item 6).
- Sztyber-Betley: one group, OpenAI models only, hand-made small circuits, o1 run once, 4o-mini and o3-mini 10 times, about $30 per o1 iteration. The conflict-score trend rises with complexity only because zero-conflict cases are scored badly (b05).
- Plank and Wotawa: manual single scorer, 3 runs, no frontier models. Phi-2's high score may be textbook memory; untested.
- Independence is generous: EoG and ITBench share authors; AutoSD and AutoFL share authors.
- Small-model hallucination of non-existent components is above 70 percent for most, not all, small models (Mistral 7B 61.5 percent).
- The 1992 book was not read.

**Moderators.**
- Model strength (reasoning above non-reasoning) and tool access (code interpreter) matter more than prompt knowledge (b04, c03).
- Problem size: up to 165 diagnoses per example; F1 falls as the count grows (b03).
- Real versus imagined observations (K16, K28).
- Weaker models gain most from retraction (K23).

**Worked.** Outside controller and state (EoG). Code-computed information gain for test choice (ACTMED). Real logs and traces. Accept-only-if-better loops (tuned). Verified location plus model repair (Tyen).

**Did not work.** Prompt algorithm descriptions. More domain knowledge in the prompt. Prompt warnings about pitfalls. Intrinsic reflection. Location hints from the same model (Li 2026).

## 6. Language models

**Off-the-shelf LLMs on MBD objects (Sztyber-Betley et al. 2025; b01-b05, c02, c03).** 23 arithmetic and logic circuits, up to 15 relations, 6 MSOs (minimal structurally overdetermined sets), 6 conflicts, 165 diagnoses. Models: gpt-4o-mini (code interpreter, temperature 0), o1 (once), o3-mini (10 runs).
- Incidence matrix: o1 and o3-mini F1 1.00, accuracy 1.00. 4o-mini F1 0.47 +/-0.15, accuracy 0.00.
- Conflicts: o3-mini F1 0.917 +/-0.249. Diagnoses: F1 0.784 +/-0.322. Large SDs mean big swings across examples and runs.
- gpt-4o and 4o-mini without the code interpreter: accuracy "close to zero on unseen examples" (c03).
- Giving the correct incidence matrix or richer domain text did not rescue the weak model. A stronger model and tools did.

**Small and medium models (Plank and Wotawa 2026; a14, a15, c04, c05, c22, c24).** 7 systems, 13 models, 3 runs each. Weighted score W: Gemini 2.5 Flash 1.846 (hit 79.5, hallucination 20.5), Mistral Large 1.832 (hit 76.9, hallucination 7.7), Llama 4 Scout 17B hit 38.5, Mistral 7B hit 25.6, Phi-2 and TinyLlama 0.0. Mean run-to-run SD: Gemini 0.264, Mistral Large 0.353, Llama 4 Scout 0.467, Mistral 7B 0.653. Only 1 of 13 named a valid double fault. Rank-sum: Gemini 8, Mistral Large 15, Llama 4 Scout 26, TinyLlama 86.

**LLM plus engine (K21).** FLEX (a17, c07): Mistral 7B F1 0.99; Llama3 0.99 with 10 documents but 0.68 with 1. FaultExplainer (c09): of 11 detectable faults GPT-4o classified 7 and o1-preview 9 with a 15-cause list. Dave 2024 (c08): one demonstration. GEMMA-FD heat pumps (d05): macro-F1 0.252 vs 0.69 for supervised XGBoost, detection only. None has an ablation of LLM-as-reasoner against LLM-as-interface.

**Agentic diagnosis in the field.**
- ITBench SRE (a18, c12): 42 SRE, 50 CISO, 2 FinOps scenarios; resolve rates 13.8, 25.2, 0 percent. gpt-4o diagnosis 13.81 +/-1.67, mitigation 11.43 +/-1.52; granite-3.1-8B 3.57; llama-3.3-70B 3.10; llama-3.1-8B 0.99.
- OpenRCA failure analysis (a19, c13, c14): 1,675 runs; perfect detection 3.9 to 12.5 percent. Pitfall rates as in section 3. Code-generation error: Gemini 2.5 Pro 40.0, Claude Sonnet 4 65.5 percent. Failures were LLM-coded.
- TN-AutoRCA (a21, c15): direct Gemini-2.5-Pro F1 58.99; with the accept-only-if-better loop 91.79; best direct baselines below 70.
- EoG (a20, c10, c11): see section 3. Input tokens were higher than ReAct for 3 of 4 models; no equal-token comparison in the paper.
- HypoAgent (a23, c16): removing condition-update candidates lowers Jaccard in 44.2 / 53.0 / 33.6 percent of cases (BioKG, PharmKG8k, DBpedia50); removing direct rewriting 14.0 / 15.6 / 24.0.

**Fault localisation in code (b19-b22, c17-c19).** Wu 2023 on Defects4J: with the error log, ChatGPT-4 mean Top-1 is 23.13 bugs (a count, not a percent), 46.9 percent above SmartFL at function level and 49.9 percent worse at class level. Dropping the log cut Top-1 by 25.6 percent. Run variance fell to 12.00 percent. 52.9 percent on StuDefects. Kang AutoFL: 798 real bugs; acc@1 over Ochiai +19.7 percent (GPT-3.5, Defects4J), +166.7 percent (BugsInPy), +233.3 percent (GPT-4, BugsInPy). About 20 percent of 300 explanations accurate. AutoSD: plausible patches 189 vs 179 for a plain LLM on ARHE, correct 187 vs 177; with <DONE> and plausible, 89 percent correct vs 82 percent without; 10 candidates beat Codex with 200 on Defects4J (a22). Human study N=20 (c18): explanation raised accuracy on 5 of 6 bugs.

**Self-correction.** Huang 2024 (b25, b26): GPT-3.5 CSQA 75.8 to 41.8 after two rounds, GSM8K 75.9 to 74.7, HotpotQA 26.0 to 25.0; GPT-4 GSM8K 95.5 to 89.0, CSQA 82.0 to 80.0, HotpotQA 49.0 to 43.0; with oracle feedback rows are higher. Tyen 2024 (b23, b24): 2,186 traces; true location lifts wrong traces by 18.04 to 43.92 points, random location 5.16 to 21.57 with losses up to -15.91; right-answer traces lose 0 to 11.43 with true location. CorrectBench (d06): 11 methods; reasoning models (DeepSeek-R1 88.92, o3-mini 81.24 baseline) gain little. Li 2026 (d07): n=500 per model, 346 errors; strongest model 94 percent accurate, corrects 16.7 percent of its 30 errors; GPT-3.5 corrects 26.8 percent; a location hint harms all three.

**Probe selection and sequential diagnosis.** ACTMED (d11) and SDBench (d09, d10) as in section 3. A search for a role ablation in SDBench found only a single-versus-batched comparison (d10). Case review showed the bare model anchoring.

**What changed results, ranked by size.**
1. Outside controller: maj@3 F1 8.6 to 86.1 (GPT-5.1), 5.7 to 79.4 (GPT-OSS-120B).
2. Model class: hit rate 79.5 down to 0 across models; non-reasoning to reasoning on conflict tasks.
3. Accept-only-if-better loop: F1 58.99 to 91.79 (tuned).
4. Real logs and traces: Top-1 -25.6 percent without; diagnosis 18.10 to 9.52 without traces.
5. Structured panel: about 70 percent lower cost at equal accuracy.
6. Prompt knowledge, pitfall warnings, self-review: near zero or negative.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Treat a conflict as a code-checkable object.** (S4, G2, G3) [E] K01; a02, a03, a08, b01. The model names which assumptions cannot all hold; code checks the claim. The full LLM-proposes, code-hits loop is untested (K24), so the add is the check only.
2. **Never trust model-written set-cover or hitting-set code unverified; call a vetted solver or compare to a reference.** (G3, tools) [E] K03, K04; d01, d02, b07, b08, b13.
3. **Pool all failing checks before generating candidates.** (S4 to S5) [E] K05; b13, b14, a09.
4. **Anytime search under a token budget; report the best candidate so far.** (G6, G12, S6) [E] K06; b15, a09, a11.
5. **Do not rely on a prompt description of the procedure; keep state and traversal in code.** (section 1 split, G3) [E] K10; c10, c11, a20. Already our design; this strengthens it.
6. **Report majority@k, not pass@k, in every diagnosis test.** (G4, log) [E] K11; c10, a20, c22.
7. **Revise only from real tool output; prefer real execution to model-simulated output.** (G2, S4) [E] K16; b19, b20, a22, c17.
8. **Slice the context; do not feed a whole large artefact.** (S1) [E] K17; b19, b21.
9. **No same-model self-review as a check; use a code check of the same cost.** (G1, G2, 4b) [E] K15, K27; b25, d06, d07. Adds 2025-26 evidence to 4b.
10. **No rich domain primers or pitfall warnings in the prompt.** (4b) [E] K09, K13; b04, c03, c14.
11. **Treat a model's explanation of a located fault as unchecked.** (S5, G10) [E] K18; b22, c19.

### Test first

- **Re-derive, do not prune (K02).** (S4/S5, O retract) [S] a05. Plant probes that both kill and add candidates.
- **Weak-fault default when failure modes are unknown (K07).** (S2) [E] for algorithms, no LLM test (K29).
- **Candidate-exists and all-components-considered code check (K19).** (G2, S4) [S] c04, a14, a15.
- **Forced multi-fault candidates (K19).** (S3) [S] a15.
- **Structural alternative-explanation step (K13, K26).** (O, S3) [S] c13, d09. Prompt warnings failed; a code-forced rival is untested.
- **Code-ranked probe choice by entropy over the candidate set (K25).** (S7) [S] d11, d13. Our S7 discriminating test is the same idea; the entropy ranking is new.
- **Locate-then-repair with an external locator (K14).** (G2, S5) [S] b23, b24.
- **Belief retraction operator (K23).** (O retract) [S] c11.
- **Accept-only-if-explains-more revision (K22).** (S5) [C] c15, a21, c16.
- **LLM as interface vs LLM as reasoner (K21).** (G3 split) [C] a16, a17, c07-c09.
- **Execution-trace estimate from a real failure log (K28).** (S4) [S] d14.
- **Unfamiliar or renamed items in all bench tests (K20).** (eval) [S] c05, c06. Costless, so do it at once.

## 8. Concrete tests on our bench

All arms at equal total tokens (setup counted, G7). Report majority@5 and pass@5; at least 3 seeds; unfamiliar or renamed items.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Small circuits and logic networks (8 to 20 components), 1 to 2 faults, observed outputs | A: model lists faults free-form. B: model proposes conflicts, code verifies each, vetted solver returns hitting sets, model ranks | Diagnosis F1 vs exact set; conflict validity rate | B above A by 10 or more F1 points for mid-size models; small gain for the strongest |
| T2 | Synthetic random conflict families | A: model-written hitting-set routine. B: reference solver call | Share of families with the exact minimal hitting sets | A fails on some non-minimal families; B 100 percent |
| T3 | Circuits where one probe kills and adds candidates (Davis style) | A: one-way elimination list. B: keep observations and conflicts, re-derive each step | Final candidate-set accuracy; true diagnoses lost | B above A when superset cases exist; equal otherwise |
| T4 | Multi-step probe selection, 10 to 20 components or text analogues | A: plain "what next?". B: model gives predicted outcomes per candidate; code ranks probes by expected entropy | Probes needed to isolate the fault | B needs 20 to 40 percent fewer probes (extrapolated from ACTMED; unsupported on circuits) |
| T5 | Items with 3 to 5 separate failing checks | A: diagnose each, then merge. B: pool conflicts, hit once | F1 and tokens | B higher F1 or equal at fewer tokens |
| T6 | Items with a true double fault | A: plain prompt. B: code check that forces multi-fault candidates and verifies each named component exists | Double-fault recall; hallucinated-component rate | B cuts hallucination near zero; recall up |
| T7 | Incident-style diagnosis, symptom plus candidate causes | A: plain agent. B: code requires a rival cause plus a distinguishing check | Symptom-as-Cause rate; correct root cause | B lowers Symptom-as-Cause by 10 points or more |
| T8 | Debugging or fault items with real tools | A: model predicts tool output. B: real tool output | Localisation Top-1; tokens | B higher; about the 25 percent Top-1 gap seen by Wu |
| T9 | Items with a given dependency graph | A: free ReAct-style agent. B: controller walks the graph, model labels one node at a time, with retraction. Sub-arm: retraction on or off | maj@3 F1 | B far above A; retraction +7 to +64 percent relative recall in weaker models |
| T10 | Reasoning tasks with a code check | A: always reflect once. B: revise only on a failing check | Right-to-wrong and wrong-to-right flip rates | B no worse; A breaks answers |
| T11 | Any item above | A: bare task. B: bare task plus an MBD primer | Accuracy | No gain from B (confirms 4b) |

## 9. What does not transfer, and why

- **A formal system description.** MBD needs a model saying what each component does. Most reasoning tasks have none, so conflicts cannot be checked by code, only by tests or re-runs.
- **Exact minimality.** Exact hitting-set minimality needs a closed component set. Open problems have unbounded hypothesis spaces; anytime preference search is the closer match.
- **Component failure priors.** GDE ranks by prior failure rates. Reasoning problems have none; the model would invent them, which G5 and G10 distrust.
- **Circuit-size speed results.** Solver timings on ISCAS85 or CNF encoders say nothing about token cost. They only say "use a solver".
- **Clinical probe results (ACTMED, SDBench).** Tabular medicine with known test costs; a vendor system with no ablation. Direction only.
- **EoG numbers.** They need a dependency graph and about 5,000 lines of domain code. The pattern transfers (outside state, local labelling, retraction), not the numbers.
- **Code-debugging results.** Defects4J has real executions and test suites. Text-only tasks have neither.
- **Human diagnostic reasoning.** This body has almost no human experiments. For humans see the naturalistic decision making and premature closure documents; they are not repeated here.
- **The 1992 book.** Not read. Do not assume it supports more than Reiter 1987 and later citations.

## 10. Open questions

1. Does an LLM-proposed, code-verified conflict set fed to a vetted hitting-set solver beat free-form hypothesis lists at equal tokens on unfamiliar systems? No published test (K24).
2. Does the Sztyber-Betley result hold for current non-OpenAI frontier models, larger circuits, and with a code tool for hitting sets?
3. Which probe-selection rule (entropy, minimum cardinality) can an LLM imitate, and does a code-ranked probe beat "what next?" on circuits?
4. Does a candidate-exists and all-components check remove small-model hallucination and the missed double fault?
5. Does a structural alternative-explanation step work where prompt warnings failed? Which role in MAI-DxO carries the gain?
6. Do EoG gains survive an equal-token comparison? Which part ports to a task with no dependency graph?
7. Does an LLM-written hitting-set routine reproduce the Reiter pruning bug?
8. How does the weak versus strong fault distinction map onto reasoning with unknown failure modes?
9. Is the AutoSD result (real debugger output beats model-simulated output) replicated with 2025-26 models, and at what equal-token cost?
10. What is the intrinsic self-review failure rate of reasoning models on diagnosis, not on arithmetic or 100-item HotpotQA?
11. What do the 1992 chapters say about probe selection, abstraction and fault models that Reiter 1987 does not? Needs the book or chapter PDFs.

## 11. Sources

[V] opened and read in the relevant parts; [M] snippet or citation entry only.

- [V] Reiter (1987), A theory of diagnosis from first principles. https://cse.sc.edu/~mgv/csce580sp17/reiter-diagnosis.pdf (a01-a07, a24, a25, a27; OCR scan, not re-opened in critique)
- [V] Greiner, Smith, Wilkerson (1989), A correction to the algorithm in Reiter's theory of diagnosis. https://www.cs.ru.nl/%7Epeterl/teaching/KeR/Theorist/greibers-correction.pdf (d01, d02; URL as truncated in the evidence file, check before citing)
- [V] Grastien, Haslum, Thiebaux (2023), A More General Theory of Diagnosis from First Principles. https://arxiv.org/pdf/2309.16180 (a08-a11, a26)
- [V] Sztyber-Betley et al. (2025), Are Diagnostic Concepts Within the Reach of LLMs? DX 2025. https://doi.org/10.4230/OASIcs.DX.2025.2 (a12, a13, a28, b01-b06, c02, c03, c20, c23)
- [V] Plank and Wotawa (2026), Using SLMs and LLMs for Diagnosis, DX 2026. https://doi.org/10.4230/OASIcs.DX.2026.14 (a14, a15, c04-c06, c21, c22, c24)
- [V] Dave, Nguyen, Vilim (2024), Integrating LLMs for Explainable Fault Diagnosis. https://arxiv.org/abs/2402.06695 (a16, c08)
- [V] Muehlburger and Wotawa (2024), FLEX, DX 2024. https://doi.org/10.4230/OASIcs.DX.2024.25 (a17, c07)
- [V] Khan et al. (2024), FaultExplainer. https://arxiv.org/pdf/2412.14492 (c09)
- [V] Jha et al. (2025), ITBench. https://arxiv.org/abs/2502.05352 (a18, c12)
- [V] Kim, Park, Yun, Lee (2026), Why do AI agents systematically fail at cloud root cause analysis. https://arxiv.org/abs/2602.09937 (a19, c13, c14)
- [V] Jha et al. (2026), Think Locally, Explain Globally (EoG). https://arxiv.org/abs/2601.17915 (a20, c10, c11)
- [V] Wu et al. (2025), TN-AutoRCA. https://arxiv.org/abs/2507.18190 (a21, c15)
- [V] Kang, Chen, Yoo, Lou (2023), AutoSD. https://arxiv.org/abs/2304.02195 (a22, c17, c18)
- [V] Gao et al. (2026), One Hypothesis Is Not Enough (HypoAgent). https://arxiv.org/abs/2605.31370 (a23, c16)
- [V] Gainer-Dewar and Vera-Licona (2016), The minimal hitting set generation problem. https://arxiv.org/pdf/1601.02939 (b07, b08)
- [V] Jannach, Schmitz, Shchekotykhin (2016), Parallel MBD on multi-core computers, JAIR 55. https://jair.org/index.php/jair/article/download/10996/26151/20495 (b09-b12)
- [V] Ignatiev, Morgado, Marques-Silva (2017), MBD of multiple observations. https://arxiv.org/pdf/1707.01972 (b13, b14)
- [V] Feldman, Provan, van Gemund (2010), Approximate MBD using greedy stochastic search, JAIR 38. https://arxiv.org/pdf/1401.3848 (b15-b17)
- [V] Feldman, Provan, van Gemund (2008), AAAI. https://cdn.aaai.org/AAAI/2008/AAAI08-145.pdf (b18; abstract and intro)
- [V] Wu et al. (2023), LLMs in fault localisation. https://arxiv.org/pdf/2308.15276 (b19, b20)
- [V] Kang, An, Yoo (2024), AutoFL. https://arxiv.org/pdf/2308.05487 (b21, b22, c19)
- [V] Tyen et al. (2024), LLMs cannot find reasoning errors but can correct them. https://arxiv.org/pdf/2311.08516 (b23, b24)
- [V] Huang et al. (2024), LLMs cannot self-correct reasoning yet. https://arxiv.org/pdf/2310.01798 (b25, b26)
- [V] Tie et al. (2025), CorrectBench. https://arxiv.org/pdf/2510.16062 (d06)
- [V] Li (2026), Decomposing LLM self-correction. https://arxiv.org/html/2601.00828 (d07)
- [V] Microsoft AI (2025), Sequential diagnosis with language models. https://arxiv.org/pdf/2506.22405 (d09, d10)
- [V] ACTMED (2025), Bayesian experimental design with LLM-simulated outcomes. https://arxiv.org/pdf/2510.18988 (d11, d13)
- [V] Yaraghi et al. (2026), Efficient black-box fault localization for system-level test code. https://arxiv.org/pdf/2506.19045 (d14)
- [V] Beck et al. (2026), Towards a neural debugger for Python. https://arxiv.org/pdf/2603.09951 (d15)
- [V] DX 2025 proceedings listing (GEMMA-FD). https://drops.dagstuhl.de/entities/volume/OASIcs-volume-136 (d05)
- [V] Gap-search negative results via OpenAlex and arXiv. https://api.openalex.org/works (d04, d13, d17)
- [M] Hamscher, Console, de Kleer (eds., 1992), Readings in Model-Based Diagnosis. https://www.sciencedirect.com/book/9781558602496/readings-in-model-based-diagnosis ; Semantic Scholar record (b27, c01)
- [M] de Kleer and Williams (1987), Diagnosing multiple faults, AI 32. https://doi.org/10.1016/0004-3702(87)90062-2 (c25)
- [M] Wotawa (2001), HST variant (via b07)
- [M] Search summaries only: arXiv 2606.23196 (d08); LDTL arXiv 2604.05116 and CuriosiTree (d12); AutoSD journal version https://coinse.github.io/publications/pdfs/Kang2025sn.pdf (d16); hitting-set survey summary (d03)
- [M] Citation entries only: Merkelbach 2024, FD-LLM, AAD-LLM, LLMAO, Qaid, Lukens (critique.md)
