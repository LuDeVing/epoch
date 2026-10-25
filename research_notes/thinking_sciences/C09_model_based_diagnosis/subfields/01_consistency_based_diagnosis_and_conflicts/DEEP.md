# Consistency-based diagnosis and conflict generation: deep document

*Subfield C09.01. Built from evidence_a-d.jsonl (ids a01 to d17), claims.jsonl (C09.01-K01 to K36) and critique.md in this folder. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Two evidence lines (d16, d17) are our own toy simulation, not literature. Related subfields researched in parallel and only linked here: Probing and measurement selection; Verification design; LLM debugging; Accuracy and dissociation of monitoring; Adaptive stopping and metareasoning; Soar impasses.*

## 1. What it is

Consistency-based diagnosis (CBD) finds what is broken in a system by logic, not by symptom lookup. You have a model of how the system should work. You have an observation that disagrees with the model. You ask: which parts could be abnormal so that model and observation fit together again?

The vocabulary in plain words:

- **System description (SD):** rules for how each part behaves when it works.
- **Component:** a part that can be blamed. Each has an "abnormal" flag AB(c).
- **Observation (OBS):** what we actually saw.
- **Conflict set:** a set of components that cannot all be normal, given SD and OBS. At least one of them is broken. A minimal conflict has no smaller conflict inside it.
- **Diagnosis:** a subset-minimal set of components such that assuming only those are abnormal makes SD plus OBS consistent (Reiter 1987, Definition 2.4, d01).
- **Hitting set:** a set that touches every set in a collection. A minimal hitting set has no smaller hitting set inside it.

The one theorem the whole field rests on (Reiter Theorem 4.4): a set is a diagnosis if and only if it is a minimal hitting set of the collection of conflict sets (a02, d01). So the work splits in two. First, find conflicts. Second, compute minimal hitting sets of them. Code can do the second step exactly. The first step needs a reasoner, which is the expensive part (a04, a06).

Why this matters to our agent. Our scaffold has failed attempts and failed checks. A failed check is a conflict: "these steps, taken together, cannot all be right, because this check failed". A hitting set over several such conflicts names the smallest sets of steps that would explain all the failures at once. That is a code-computed answer to "what should I change?", which fits the schema rule that the program decides and the model fills slots (G2, G5).

The honest status: the theory is old, exact and well proven. The LLM evidence is nearly all from 2026, from single groups, with small samples. No study tests the schema's actual bet (section 7, K23). This document separates what is solid theory, what is solid engineering, and what is a hope.

## 2. History and theories in depth

### 2.1 Reiter 1987: the theory

Reiter's "A theory of diagnosis from first principles" (read in full this session, d01 to d04) defines diagnosis from first principles: no fault dictionary, only a model of correct behaviour.

Key points from the full text:

- Definition 2.4: a diagnosis is a subset-minimal set A of components such that SD + OBS + {AB(c) for c in A} + {not AB(c) for c not in A} is consistent.
- Proposition 3.2: the empty set is the only diagnosis if and only if the observation does not conflict with "all components normal".
- Worked example: a full adder. Two minimal conflict sets give three diagnoses: {X1}, {X2,O1}, {X2,A2}.
- The algorithm builds a pruned **HS-tree** breadth-first. Level 1 holds single-component diagnoses, level 2 pairs, and so on. So diagnoses come out in order of increasing size. Reiter says you may stop at level k if bigger diagnoses are highly improbable (d02). A size cap is part of the original design.
- Reiter's theory has **no probabilities and no entropy rule**. His measurement section (Theorems 5.5 to 5.9) is qualitative. Section 7 says de Kleer and Williams (1987) go beyond his theory by computing probabilities and choosing the next measurement (d04, K25).
- Theorem 5.7: after a new measurement, each old diagnosis that predicted the measured value survives. Each that predicted the other value is dropped. Any **new** diagnosis is a strict superset of some old one that was dropped (d03). Example 5.6/5.10 on the Davis device: measuring out(M2)=5 replaced four old diagnoses by four new supersets such as {M1,M2,M3}.

Consequence for us: a size-1 cap that was fine at the start can lose the culprit once evidence accumulates, because the true answer may now be a bigger set (K26).

### 2.2 de Kleer and Williams 1987: GDE

The General Diagnostic Engine (GDE) is the other founding paper: "Diagnosing multiple faults". Our status for it is weak. Only an abstract snippet was seen. The PDF mirror gave 404 and the publisher 403 (a05, b26, K25).

What we know second-hand, from opened papers that describe it (a06, a09, a13, a24):

- Component models give predictions. A discrepancy gives conflicts, as minimal sets of "component works" assumptions that cannot all hold.
- An **ATMS** (assumption-based truth maintenance system, de Kleer 1986) keeps track of which assumptions support which predictions, so conflicts are found and minimised cheaply.
- Candidates are the minimal sets that hit every conflict.
- Candidates are **ranked by prior failure probability**, updated with Bayes' rule as measurements arrive.
- The next measurement is chosen to cut the Shannon entropy of the diagnosis distribution the most, on average. De Kleer et al. (1992) report on ISCAS-85 single faults that costs come close to optimal policies (a09).
- A trade-off reported by de Kleer (1992): computing more diagnoses makes the heuristic more accurate; a short list of probable ones is faster but less accurate (a24).
- GDE assumes all measurements have unit cost, so the aim is the fewest measurements (a24).

**Rule for citing:** use de Kleer and Williams, not Reiter, for probability ranking and entropy probe choice. Treat the entropy rule as unverified until a library copy is read (K25).

### 2.3 Reiter versus GDE on conflicts

Reiter's method accepts non-minimal conflict sets. GDE needs the inference engine to hand over only minimal conflicts. Conflicts come from a theorem prover or ATMS on demand, each call is expensive, and so the algorithms are built to call it as little as possible (a04, b02).

Grastien, Haslum and Thiebaux (2023, a13) give the cleaner reading. Reiter models only correct behaviour (weak fault models), so every superset of a candidate is also a candidate and the minimal set stands for all of them. De Kleer and Williams allow faulty-behaviour models (strong fault models), where that superset rule fails.

### 2.4 Greiner, Smith and Wilkerson 1989: the bug in Reiter's algorithm

Reiter's published HS-tree algorithm was wrong (a02, a03, b01). Three pruning ideas interact badly: reusing node labels, closing nodes, and removing redundant edges when a subset conflict is found. The pruned tree can lose minimal hitting sets, so true diagnoses are missed.

- Counterexample collection: {{a,b},{b,c},{a,c},{b,d},{b}} over 4 components. Reiter's pruning loses the minimal hitting set {a,b}.
- The fix: **HS-DAG**, a graph with node reuse and relabelling, not a tree.
- The bug came from the trick that lets the algorithm accept non-minimal conflicts.
- Reiter's own text, as read this session, says no edge is closed as redundant if the conflict finder returns only minimal conflicts (d02). Rodler (2020) relies on that, and still needs a node-replacement step for completeness, citing Greiner (d05).
- Nobody found an independent bug hunt of the corrected algorithm (Pill et al. 2011/2012/2016 were not opened, b27). **Lesson: property-test any hitting-set code against brute force** (K02).

### 2.5 de Kleer, Mackworth and Reiter 1992: what a diagnosis is

This theory paper (a08, opened, but the OCR copy is garbled so wording is partly reconstructed) shows that minimal diagnosis is inadequate when components also have fault models, because a superset of a faulty set need not be a diagnosis. It proposes **kernel diagnoses**, the prime implicants of the conflict set. A conflict is an AB-clause entailed by SD plus OBS. No experiments.

### 2.6 Scaling and search refinements, 1993 to 2020

- **Roos 1993 (a14, b23, b24):** use causal structure. The conflict set of a wrong output is only the components its predicted value depends on. Confirming measurements shrink or cancel components. Worst case O(n^2) in components, linear at low connectivity. Predictions run one way only, which is cheaper than GDE but ignores some information. No empirical tables.
- **Wassermann 2000 (a21, b22):** ties CBD to belief revision. A conflict is a minimal inconsistent subset (a kernel) of SD plus OBS. A diagnosis is a hitting set of the kernels to remove. Restricting to the part of SD relevant to the observation gives smaller conflicts. Theory only.
- **Williams and Ragno 2007 (a26, seen as summary only):** conflict-directed A*. Searches states best-first by probability and removes subspaces around each inconsistent state found.
- **Stern, Kalech, Feldman and Provan 2012 (a06, a07, a23, b06, b07):** duality. A diagnosis is a hitting set of the conflicts, and a conflict is a hitting set of the diagnoses. Their SDE algorithm alternates the two searches.
- **Shchekotykhin et al. 2012 (c28, skimmed):** when faults are many, precomputing conflicts is infeasible, so compute diagnoses directly.
- **Shchekotykhin, Jannach and Schmitz 2015, MergeXplain (b08, b09):** returns several minimal conflicts per run instead of one.
- **Rodler 2020, DynamicHS (a15, d05):** keeps the HS-tree between measurements and reuses it. Answers a question Reiter raised in 1987.
- **Grastien, Haslum and Thiebaux 2023 (a11, a12, a13):** generalises Reiter beyond sets of faults to any hypothesis space with a preference order. A conflict is any object standing for a set of hypotheses proven not to contain the diagnosis, and it can be larger than the hypothesis tested.

### 2.7 Spectrum and software variants

Full model-based diagnosis did not scale to software, so hybrids appeared:

- **Peischl and Wotawa 2003 (b10, b11):** CBD on program source. The true bug was always in the diagnosis set, but so were many others. Complete, not precise.
- **Abreu, Zoeteweij and van Gemund 2009, BARINEL (b12, b13):** a candidate must explain all failing runs (consistency), then is ranked by Bayesian probability. A cheap heuristic hitting-set step (STACCATO) makes it scale. Complexity O(N*M + M log M).
- **Orvalho et al. 2025, CFaults (a16, a28):** each statement is a component with an abnormal switch, failing tests are observations, one MaxSAT formula covers all failing tests at once.

### 2.8 The LLM line, 2024 to 2026

Eight kinds of LLM work touch this subfield. Details in section 6.

1. LLM as conflict or diagnosis generator on circuits (Sztyber-Betley 2025).
2. LLM as consistency oracle inside a real Reiter pipeline (He et al. 2026, QXR).
3. Minimal unsatisfiable core as repair feedback (Sarkar 2026; VERGE, Singh et al. 2026).
4. Symbolic diagnosis feeding an LLM sketch (Orvalho 2025).
5. Hitting-set baseline versus LLM for PDDL repair (Karimi Bavandpour and Bercher 2026).
6. Execution-grounded blame (SemLoc, SBFL on agent traces, REFLECT).
7. Failure attribution in multi-step agent traces (Who&When).
8. Self-correction and test-time scaling baselines that any diagnosis scaffold must beat.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A diagnosis equals a minimal hitting set of the conflicts | Theorem 4.4; full adder: 2 minimal conflicts give 3 diagnoses {X1}, {X2,O1}, {X2,A2} | Reiter 1987 (d01); Greiner 1989 (a02) | [E] |
| Reiter's published HS-tree pruning loses diagnoses with non-minimal conflicts | Counterexample {{a,b},{b,c},{a,c},{b,d},{b}} loses {a,b}; fix is HS-DAG | Greiner et al. 1989 (a02, a03, b01); Gainer-Dewar 2016 (b03); Rodler 2020 (d05) | [E] |
| After a new observation, new diagnoses are strict supersets of dropped ones | Theorem 5.7; Davis device: four old diagnoses replaced by four supersets | Reiter 1987 (d03) | [E] |
| Reiter has no probabilities or entropy rule | Section 7 hands both to de Kleer and Williams | Reiter 1987 (d04) | [E] |
| Exact diagnosis is exponential and conflict search stalls on big circuits | CDA* vs SDE solved within 30 s: 74283 100/99%; 74182 100/100%; 74181 47/79%; c432 33/88%; c499 9/30%; c880 5/14%; c1355 0/9% | Stern et al. 2012 (a07, b06) | [S] (same group, own framework, partial observations) |
| Approximations trade completeness for speed | BARINEL O(N*M + M log M); Roos O(n^2); BDD hitting sets (HTC-BDD) often out of 32 GB; HTC-BDD 4x to 10x faster than rivals where it fits | Abreu 2009 (b12, b13); Roos (a14); Gainer-Dewar (b03) | [E] |
| Size cutoff is the main practical lever | c432 single fault: random probing 92.3 measurements without pruning vs 4.5 with cardinality pruning; sda(ew) 42.0 without pruning; double fault 97.7 vs 36.8; SNIPER hits 32 GB on 73% of TCAS programs | Siddiqi and Huang 2011 (a10); Orvalho 2025 (a28); Gainer-Dewar (b05; cutoffs 5, 7, 10 tested) | [E] |
| More faults mean more candidates and worse ranking | BARINEL wasted effort on print_tokens with 1, 2, 4 faults: 1.2, 2.4, 4.8% vs Tarantula 2.6, 5.3, 11.5%; counter example: 25 single-fault and 66 dual-fault diagnoses map to 8 statements | Abreu 2009 (b12); Peischl 2003 (b10) | [E] |
| DynamicHS saves time over rebuilding the tree | 96% of sessions, median 52%, max 75% saved on 20 real knowledge-base problems | Rodler 2020 (a15, d05) | [E] (also MergeXplain below) |
| MergeXplain helps but with boundary conditions | First 5 diagnoses: 15% to 45% faster on circuits (c432 707.5 vs 503.9 ms); up to 54% on constraint problems; loss 11% on queens-8; synthetic: 54% random, 33% left, 14% right, 75% left-and-right, 58% neighbours, and -8% for 50 components, 15 conflicts of size 4, right | Shchekotykhin 2015 (b08, b09) | [E] |
| Formula-based diagnosis over all failing tests beats per-test methods | CFaults 480/682 = 70.38% vs BugAssist 265 (38.86%), SNIPER 234 (34.31%), HSD 375 (54.99%). The "31, 36, 15" in the paper are absolute points of the benchmark; relative gains about +81%, +105%, +28% | Orvalho 2025 (a16, a28; critique correction 1) | [S] |
| LLM judging a whole claim set over-prunes; conflict localisation plus code hitting set fixes recall | VitaminC recall: Sonnet 4.5 .617 to .957; Opus 4.6 .574 to .968 (F1 .611 to .976); Mistral Large 2 .603 to .978 | He et al. 2026 (a18, c13) | [S] |
| Same method gives little or nothing on easy conflicts | FEVER Opus F1 .989 direct vs .964; RAMDocs Sonnet 4.5 F1 .882 vs .870 | He et al. 2026 (a27, c13) | [S] |
| Pairwise consistency checks are costly | N = 30 to 100 claims needs 435 to 4,950 calls; QuickXplain needs O(k log N) per conflict | He et al. 2026 (c12, a19) | [S] |
| A minimal core as feedback stops fabrication by a weak model | deepseek-v3.2 on 14 infeasible items: fabricated 11/14 (79%) with generic error repair vs 1/14 (7%) with core repair, Fisher p < 0.001; gemma4-31b 0% both ways | Sarkar 2026 (b19, c15) | [S] |
| ...but accuracy gain over generic repair is small, and plain CoT matches the solver route | Typed + core repair 89.6% vs generic 88.3%; pipeline 84.4% first try; direct 74.0% (fabricates 21.4%); CoT 98.7% (fabricates none); repair fixed 4 failures and broke none | Sarkar 2026 (b20, c16; critique correction 5) | [S] |
| Minimal correction subset as feedback helps formal reasoning | GPT-OSS-120B: +18.7% average over single pass; FOLIO 84.7 vs 80.7 without MCS; ProofWriter 89.9 vs 88.7; ZebraLogic 91.0 vs 88.9; AR-LSAT 91.7 vs 83.0 (direction as printed in a20 finding) | Singh et al. 2026, VERGE (a20) | [S] |
| LLMs generate conflicts well, diagnoses worse | o3-mini conflicts F1 0.917 (sd 0.249), diagnoses F1 0.784 (sd 0.322); gpt-4o and 4o-mini "close to zero"; 4o-mini with code interpreter worst of three | Sztyber-Betley et al. 2025 (b14, c04, c05) | [S] |
| LLM PDDL repair can beat the symbolic hitting-set baseline on overlap but not on tests passing | Symbolic F1 .49 (precision .69, recall .41, pass rate 1.0 by construction); best LLM F1 .87, test pass .82; Thoughtful domain .06 | Karimi Bavandpour and Bercher 2026 (b16, c01) | [S] |
| More evidence or effort can hurt | With traces best F1 fell .85 to .78 (default effort); DeepSeek V4 Pro high effort: pass .82 to .92, F1 .74 to .82; GPT-OSS-120B with traces F1 .49 to .15, pass .57 to .09; no-trace table .53 to .37, pass .50 to .40; GPT-OSS-20B with traces F1 .23 to .41 | Karimi 2026 (b17, b18, d14; critique correction 2) | [C] |
| Model progress on the same task is fast | GPT-4o F1 .46; best 2025 model .53; best 2026 model .85 | Karimi 2026 (c03) | [S] |
| Executable grounding beats free-form LLM blame | SemFault-250 (250 programs, one fault each), Claude Sonnet 4.6: Acc@1 42.8%, Acc@3 68.0%; Ochiai 6.4% / 13.2%; Gemini 2.5 Pro LLM-only 37.6% / 44.0%; no counterfactual check 30.8% / 59.6% | Yang et al. 2026, SemLoc (c09, c10) | [S] |
| Localise first | File-level localisation 15 to 17 times over none; best repairs use about 6 to 10 files; 500 SWE-bench Verified items, GPT-5-mini, 61 configs | Sepidband 2026 (c11) | [S] |
| LLMs are poor at naming the failure step in agent traces | Who&When: best 53.5% agent-level, 14.2% step-level; GPT-4o all-at-once 54.33 / 12.50, step-by-step 35.20 / 25.51, random 29.10 / 19.06; reasoning models under 10% (AgenTracer abstract) | Zhang 2025 (c17, c18, c21) | [E] |
| Spectrum blame over replayed runs beats LLM judges | 57.61% agent, 29.35% action vs random 23.71% / 14.36%; hand-crafted logs 41.38% action vs best LLM 8.77% | Ge et al. 2025 (c19) | [S] |
| Intervention beats judging | REFLECT exact-match: WTQ 76.3 vs 55.5; GAIA 39.0 vs 15.7; SWE-bench 70.0 vs 33.3; BBM 34.5 vs 30.3 (a Claude Opus 4.6 judge got 60.1 on BBM) | REFLECT 2026 (c20, abstract only) | [S] |
| Models cannot find their own errors but can fix them when shown | BIG-Bench Mistake, 2,186 traces, 5 tasks; word sorting with oracle location: 23.53% of wrong traces corrected vs 11.11% of right ones broken | Tyen 2024 (c22) | [E] |
| Intrinsic self-correction does not help | GSM8K GPT-3.5: answer kept 74.7% over two rounds; more correct-to-wrong than reverse | Huang 2024 (c23); Kamoi 2024 (c24) | [E] |
| Repair loops flatten fast | 89% fixed first try (mean 1.14 iterations, max 7); Codeflaws Llama 3.1 405b 29.01 to 44.93% over 5 scenarios, GPT-4 CoT 41.32%; self-debug matches baselines with 10x samples | Orvalho (c08); Farzandway (c26); Chen 2024 (c25) | [E] |
| Counterexample adds almost nothing for a small open LLM | CodeGemma: 597 (41.7%) plain; 682 (47.7%) with sketch; 688 (48.1%) sketch + counterexample | Orvalho 2025 (c07) | [S] |
| Portfolio beats best single model | 6 small LLMs 1013/1431 = 70.8% vs 59.1% best single; CLARA 495 (34.6%), Verifix 91 (6.3%) | Orvalho 2025 (a17, c06) | [S] (union over configs, not compute matched) |
| Autonomous repair is token heavy | 164 of 835 Defects4J bugs fixed, about 270,000 tokens per bug | Bouzenia 2024 (c27) | [S] |
| Answer-level checks leave many flawed traces with empty conflicts | Process error in correct-final-answer solutions: GSM8K 3.5% (7/200), MATH 18.8% (94/500), OlympiadBench 32.2% (161/500), Omni-MATH 51.8% (259/500) | ProcessBench (d06) | [S] |
| Prompted critics beat learned PRMs for step blame; all fall on hard sets | Average F1: Math-Shepherd-PRM-7B 31.5; Skywork-PRM-1.5B 36.4; Skywork-PRM-7B 42.1; Qwen2.5-Math-7B-PRM800K 56.5; Llama-3.3-70B 58.0; Qwen2.5-72B 61.2; GPT-4o 61.9; o1-mini 87.9 | ProcessBench (d07) | [S] |
| Same-model oracle collapses a repair loop; a sound verifier helps | Single / LLM+LLM / LLM+sound verifier: Game of 24 5/3/36; Graph Coloring 16/2/38; Blocksworld 40/55/60; Mystery Blocksworld 4/0/10; verifier false negatives up to about 97% | Stechly et al. 2025 (d08) | [S] (GPT-4, 100 items per domain) |
| With a sound checker, plain sampling matches critique loops | Game of 24: binary feedback 36, first-error 38, sampling k=25 42; best-of-N matched or beat feedback in 3 of 4 domains; first-error feedback beat binary by 27 points in one domain | Stechly et al. 2025 (d09) | [S] |
| Naive revision breaks correct answers | About 38% of correct answers turned wrong (PaLM 2-S* finetuned, MATH); compute-optimal mix up to 4x less compute than best-of-N | Snell et al. 2024 (d10) | [S] |
| Selection, not coverage, is the best-of-N bottleneck | MATH Llama-3-8B coverage 82.9% at 100 samples to 98.44% at 10,000; vote or reward model 40.50% to 41.41%; SWE-bench Lite 15.9% (1 sample) to 56% (250) | Brown et al. 2024 (d11) | [E] with d09 and d10 |
| Counterfactual re-runs on prose are costly and uneven | 100 rollouts x 144.2 sentences per trace is about 14,400 rollouts; AOC 0.44 (AQuA) to about 0.02 (ARC-Easy); dependence falls with model size above 13B | Bogdan 2025 (d13); Lanham 2023 (d12) | [S] |
| Longer reasoning can hurt through distraction and framing | Claude Opus 4 counting with distractors: near 100% down to 85 to 90%; R1 with 5 distractors 70% to 30% | Gema et al. 2025 (d15) | [S] |
| Toy: a hitting-set pick has a modest edge over simple blame | n=20 steps, 3,000 trials per cell; top-1 hit rate 44% to 60% for k=1..4 vs 33% to 37% random conflict step vs 38% to 63% for "last step of smallest failed check"; edge over that rule about +6 to -3 points; noise (fn .4, fp .1) cuts to 21% to 44% | Own simulation (d16, d17) | own simulation, shape only |
| Toy: cap vs true error count | Hitting set exists within cap: k=2 cap1 .53, cap2 .93; k=3 cap1 .29, cap2 .84, cap3 .98; cap 3 covered k up to 4 in about 96% at about 7 of 20 candidate steps | Own simulation (d16) | own simulation, shape only |
| Toy: empty conflicts depend on check coverage | m=8 noise-free: .27 (k=1), .07 (k=2), .02 (k=3); m=16, fn=.2: .06 (k=1), .003 (k=3); size-1 conflicts .08 (k=1) to .28 (k=4) at m=8 | Own simulation (d17) | own simulation, shape only |

## 4. Mechanisms and models

This section is written so an engineer can build it. The program does the logic. The model fills slots.

### 4.1 Representation

- **Components.** For our agent a component is a thing that can be wrong and can be blamed. Candidates: a reasoning step, a claim, a constraint, a tool call. No source decides the unit (critique gap 2). Pick one per task class and log it. A component must be something that a check can cover, or it never appears in a conflict.
- **Checks.** Each check is a code-run test that passes or fails and has a **support**: the set of components the check depends on. Examples: a unit test with the steps that produced the tested value; a symmetry test; a held-out example; a constraint verifier on a claim set.
- **Conflict.** For each failed check, the conflict is its support (or a smaller subset of it). Store as a frozenset of component ids. Keep only minimal ones (drop any conflict that contains another).
- **Empty conflict.** If answers are wrong but no check fails, the conflict list is empty and no diagnosis can be made. This is a **coverage** signal, not a result (K28; d06 shows 3.5% to 51.8% of correct-answer solutions still hold a process error).

### 4.2 Minimal hitting sets in code

Inputs: a list of minimal conflicts C, a size cap k.

Plain version (good enough for 20 to 50 components and k up to 3):

```
def minimal_hitting_sets(conflicts, cap):
    conflicts = minimize(conflicts)          # drop supersets
    results = []
    def extend(chosen, remaining):
        if not remaining:
            if not any(r <= chosen for r in results):
                results.append(frozenset(chosen))
            return
        if len(chosen) == cap:
            return
        c = min(remaining, key=len)          # branch on smallest unhit conflict
        for comp in sorted(c):
            extend(chosen | {comp}, [x for x in remaining if comp not in x])
    extend(frozenset(), conflicts)
    return prune_non_minimal(results)
```

Notes:

- Branch on the smallest unhit conflict. This is the standard heuristic and it keeps the tree small.
- Post-filter for minimality (drop any result that has a smaller result inside it). Do not rely on search order alone. That is exactly where Reiter's own pruning went wrong (Greiner 1989).
- Always **property-test against brute force** on random collections, and include the Greiner counterexample {{a,b},{b,c},{a,c},{b,d},{b}} as a fixed test (K02). For this collection the minimal conflicts are {b} and {a,c}, so the minimal hitting sets are {a,b} and {b,c}. Reiter's pruning loses {a,b}. The test should also compare against brute force, not only this hand result.
- For bigger inputs use a library algorithm with a size cutoff. The benchmark of about twenty algorithms (Gainer-Dewar 2016, b03) says MMCS and RS are fast, use little memory and support cutoffs. HTC-BDD is fastest where it fits but often exceeds 32 GB and has no cutoff.
- Order of conflicts changes cost a lot for the Berge algorithm (b04).

### 4.3 The size cap and how to raise it

- Reiter built a breadth-first order in, so diagnoses of size 1 come first, then 2 (d02).
- Rule from Theorem 5.7: after every new attempt, **recompute from all conflicts so far**. Do not carry old diagnoses forward, because new ones are supersets (d03, K26).
- If no hitting set exists within the cap, that is a detectable signal: the true error count exceeds the cap. **Raise the cap by one.** In the toy model with k=3 true errors, a hitting set of size <= 1 existed in 29% of trials, <= 2 in 84%, <= 3 in 98% (d16, K27).
- Do not claim completeness under a token cap. Deciding whether more minimal diagnoses exist is NP-hard (d05, K34).

### 4.4 Ranking

Many diagnoses survive. Rank them in code (G5). Options, cheapest first:

1. **Size.** Smaller first. This is Reiter's order.
2. **Prior fail rate by step type**, from the class record (memory). Best-first search over fault probability returns only minimal diagnoses if each component is more likely normal than faulty, so clamp priors into (0, 0.5) (Rodler, d05, K34).
3. **Count of conflicts hit** by a single component (Roos focuses on components in the most conflicts, a14). This is also what spectrum methods approximate.
4. **Spectrum score** such as Ochiai over a check-by-component matrix (SemLoc c09; BARINEL b12). In SemLoc, Ochiai on a violation matrix with LLM-written constraints reached Acc@1 42.8%.
5. **Bayesian update** as in BARINEL (explain all failing runs, then rank by probability). This is second-hand GDE logic for the priors part (K25).

No LLM study found ranks by anything but a model's own judgment. A cheap prior against stated confidence is untested (K33; ProcessBench d07 gives one negative hint: learned PRMs lost to prompted critics).

### 4.5 Choosing the next probe (link: probing and measurement selection)

GDE picks the measurement that most reduces expected entropy over the current diagnoses (a09). Evidence from circuits (Siddiqi and Huang 2011, a10): on c432, random probing needs 92.3 measurements without pruning and informed choice about 42 (sda(ew)), with cardinality pruning random needs 4.5 for single faults. For our agent a "probe" is one more check or one more run. The cheapest implementable form: pick the check whose pass/fail outcome splits the current top diagnoses most evenly (maximum split, ties by lowest cost). Not LLM-tested.

### 4.6 Conflict generation: three routes

1. **Code check with known support.** Best. Support is known by construction (the code that produced the tested value). Cost is near zero.
2. **Counterfactual toggle.** To decide whether a step is a root cause or a cascade, remove or change it in a re-run and see whether the failure changes (SemLoc: removing this costs 12.0 Acc@1 points; REFLECT replays from a rollback point with a repair injected). Cost is one re-run per suspect on code-checkable components. On prose steps it is far dearer: about 14,400 rollouts per trace in Thought Anchors, and the answer's dependence on stated steps ranges from AOC 0.44 to 0.02 across tasks (d12, d13, K32).
3. **LLM as oracle with QuickXplain.** QuickXplain (Junker) finds one minimal conflict with O(k log N) oracle calls where k is the conflict size and N the set size (c12). He et al.'s pipeline: run QuickXplain to get a minimal unsatisfiable subset, remove it from consideration (or collect it), repeat until consistent, then a greedy hitting set picks what to delete. This works only with a good oracle. A same-model oracle collapses (K29, d08).

Best-first or divide-and-conquer conflict search (MergeXplain) returns several conflicts per run. Its advantage depends on where conflicts sit (b09).

### 4.7 The He et al. loop in detail (a18, a19)

1. Input: N claims, an oracle `consistent(S)` answered by an LLM.
2. While `consistent(all remaining)` is false: use QuickXplain to find a minimal inconsistent subset (MUS); add to the conflict list; mark one member as removed in a probe copy to find the next MUS (or use a standard enumeration).
3. Compute a greedy hitting set of the MUSes; delete those claims.
4. Theorem A.2: a deletion restores consistency exactly when it hits every MUS. Pairwise checks are provably insufficient: a graph-colouring construction gives a set where every pair is consistent but the whole is not.
5. Data: VitaminC cases have 24 to 32 claims with 2 to 6 injected contradictions; mean 4.05 MUSes and minimum hitting set size 4.05. FEVER 33.7 claims, 4.77 MUSes, hitting set 4.01.

Cost: pays extra oracle calls and wins only when the set is mostly coherent with a few local conflicts (a27).

### 4.8 The Sarkar loop (b19, c15)

1. Model writes a constraint program from the problem text.
2. A solver returns "unsatisfiable".
3. Code computes a minimal unsatisfiable core (deletion filtering, QuickXplain family) over the model's own constraints.
4. The model sees the core, and must either justify the constraints in it or change one.
5. Failure case: a conflict core cannot repair what the model cannot express. Local constraints were translated faithfully; global counting (aggregate coverage) was not, and stayed at 0% without repair (b21).

### 4.9 Spectrum and violation-matrix variant

When there are many tests and cheap passes, build a matrix rows = checks, columns = components, entry 1 if the component is in the check's support. Count `ef` (failed checks that include c), `ep` (passed checks that include c), `nf`, `np`. Ochiai(c) = ef / sqrt((ef+nf)(ef+ep)). Spectrum methods assume a single fault. BARINEL adds the multi-fault consistency requirement (b13). This is what Ge et al. 2025 used on replayed agent runs (c19).

### 4.10 What a "failed attempt" means for our scaffold

For one reasoner with several attempts: attempt i has steps s_i1...s_in and a set of checks. Components are the (step type, content) slots shared across attempts, or the claims each attempt makes. A failed check marks as a conflict the claims it used. Across attempts the same claim shows up in several conflicts, and the hitting set names the claim that, if wrong, explains all the failures. This is the schema bet. **It has not been tested** (K23).

## 5. What holds up

### 5.1 Strong, multiple sources

- **Theory.** Diagnosis equals minimal hitting set (a02, a08, a25, b02, b03, d01). Solid.
- **The 1989 bug.** Confirmed by Greiner's counterexample, by the later benchmark survey (b03), and by Rodler (d05). Fix is known; independent bug hunt for the fix not found.
- **Cardinality pruning is a main lever.** Siddiqi and Huang (c432: 92.3 to 4.5), Gainer-Dewar (cutoffs supported by most algorithms), Orvalho (SNIPER out of memory on 73% of TCAS without it).
- **Approximations scale, exact does not.** BARINEL, Roos, BDD limits.
- **Models do not find their own errors; they fix them once shown.** Three sources (Tyen, Huang, Kamoi).
- **Failure attribution by LLM judges is poor.** Who&When, AgenTracer, SBFL beats judges.
- **Repair loops flatten after one or two rounds.** Three sources.
- **Selection is the bottleneck; sound checkers matter.** Brown, Stechly, Snell.

### 5.2 Single-source or contested

- **Conflict-localised input helps LLMs.** He et al. (recall .574 to .968) and Sarkar (fabrication 79% to 7%). Both single group, small items, strong dependence on model strength. Boundary: FEVER and RAMDocs show zero or negative effect for a strong model on easy conflicts.
- **LLM generation of conflicts.** One paper, hand-made examples, large sd (bimodal).
- **Effort and extra evidence.** Contested (K10). Traces lower F1 .85 to .78 for one model and lift others. The authors did not isolate the cause (context limit and unparsable output are confounds). Inverse scaling work gives distraction and framing overfit as mechanisms on other tasks.
- **Counterfactual verification.** SemLoc and REFLECT agree in direction. Both 2026, one group each.
- **Portfolio union.** 70.8% vs 59.1%. Union over configs, not compute matched. It sits uneasily with G4: different models are more independent than samples of one model, but cost is not matched.

### 5.3 Failures, boundary conditions, competing explanations

- **Reiter's own algorithm was wrong** until 1989 (see above).
- **Per-test conflict merging breaks.** Merging minimal correction sets computed separately for each failing test can exhaust memory and does not guarantee a diagnosis consistent across all tests (a28). Remedy: one formula covering all tests.
- **MergeXplain** loses 11% on queens-8 and -8% in one synthetic ordering (b09).
- **Gains concentrate where the model is weak.** QXR gain bigger for Qwen2.5-7B than strong models (a27). Sarkar core helps one model and not the other (gemma 0% fabrication either way).
- **A strong prompt can match the pipeline.** CoT 98.7% vs pipeline 84.4% to 89.6%. The solver's value was certificates and refusal to fabricate, not accuracy (b20). Typed plus core repair beat generic repair by only 1.3 points (89.6 vs 88.3).
- **Prompting tricks do not fix over-pruning.** CoT, decomposition, few-shot and self-consistency all kept high precision and low recall (c14). So the fix is structure, not wording. On VitaminC, Opus 4.6 direct precision was only .654 (Sonnet 4.5 .997), so the over-pruning story is not uniform (critique correction 4).
- **Overlap is not correctness.** Best F1 .87 came with .82 mean test pass (K11).
- **Conflict feedback detail barely mattered against sampling.** Stechly: with a sound verifier, first-error feedback beat binary feedback in 1 of 4 domains (27 points), and sampling at k=25 matched or beat the feedback loops in 3 of 4 (d09). This is the strongest evidence against the schema bet, and it is GPT-4 era.
- **Naive revision harms.** 38% of correct answers turned wrong (d10). Always keep best-so-far by a code check.
- **A same-model oracle is bad.** Game of 24: 5% single, 3% self-critique, 36% sound verifier (d08).
- **Toy simulation warns against over-claiming.** Hitting-set top-1 pick beats a random conflict step by 10 to 25 points but beats a simple "blame the last step of the smallest failed check" rule by only +6 to -3 points. With noise (false negative .4, false positive .1), the pick falls to 21% to 44% (d17).
- **Narrow-checker caveat.** Program-repair numbers use many failing tests per program (up to 131, TCAS). One failed answer gives one conflict at most.
- **No replication anywhere in the 2026 LLM papers.** Every LLM-plus-conflict result is from a single group. This is the main weakness of the whole subfield for our purposes.

### 5.4 Moderators

| Moderator | Direction | Source |
|---|---|---|
| Model strength | gains from conflict feedback shrink or reverse for the strongest model on the easy sets | a27, c13, b19 |
| Conflict density | method wins when set is mostly coherent with few local conflicts | a27 |
| Check coverage | empty conflicts when coverage is low | d06, d17 |
| Number of faults | more faults, more candidates, worse precision | b10, b12 |
| Context length | step attribution accuracy falls | c18 |
| Reasoning effort | helps some models, hurts others, cause unknown | b18, d14, d15 |
| Prompt format | few-shot cured a regression-task failure; a short prompt hurt GPT-4o | d15, b18 |
| Conflict position | MergeXplain gain depends on where conflicts sit | b09 |
| Expressibility | a core cannot fix what the model cannot state (global counting) | b21 |

## 6. Language models

### 6.1 Can LLMs do the steps?

- **Generate conflicts (circuit task, hand-made unseen examples).** o3-mini F1 0.917 (sd 0.249). o1 best at conflicts. Surprisingly good, but sd is large, so results are bimodal (b14, c04).
- **Generate minimal diagnoses.** o3-mini F1 0.784 (sd 0.322). It is the most compute-heavy step and degrades as the number of diagnoses grows (c04, b15). gpt-4o and 4o-mini were close to zero. A broad prompt matched a domain-heavy one. A correct incidence matrix did not help MSO generation much. Authors' conclusion: not good enough to replace algorithms.
- **Our reading:** give conflicts to code and let code do the hitting set (K09).

### 6.2 LLM as consistency oracle (QXR)

- Direct all-at-once judging: high precision, low recall (over-prunes). VitaminC recall .617 (Sonnet 4.5), .574 (Opus 4.6), .603 (Mistral Large 2).
- QXR: recall .957, .968, .978. Opus F1 .611 to .976. Also helps small models more (Qwen 7B and 32B).
- Prompting tricks did not help. Structure did.
- Easy sets: no gain or loss (FEVER Opus F1 .989 vs .964; RAMDocs Sonnet 4.5 .882 vs .870).
- Cost: 435 to 4,950 calls for pairwise vs O(k log N) per conflict for QuickXplain.
- Noisy-oracle problem is open: He et al. flag it, and the same-model verifier results (Stechly) suggest it can be bad.

### 6.3 Conflict as repair feedback

- Sarkar: fabrication 79% to 7% for deepseek-v3.2 on 14 infeasible items. But CoT alone fabricated 0 of 14 and scored 98.7%. The value is certificates, not accuracy.
- VERGE: MCS feedback beat unsat-core feedback in ablations on FOLIO, ProofWriter, ZebraLogic; with +18.7% average over single pass (GPT-OSS-120B). The AR-LSAT row in the evidence line reads "91.7 down to 83.0 with ..." and was not re-opened. Treat the MCS effect as mixed until the row is re-read.
- PDDL repair (Karimi): the strongest 2026 open-weight LLM reached F1 .87 vs a hitting-set baseline .49, but test pass rate only .82 vs 1.0. The LLM uses names as semantic cues. Handing it failing and passing traces did not help at default effort (F1 .85 to .78).
- Orvalho: giving the localised sketch beat giving the whole program (CodeGemma 41.7% to 47.7%). Adding a counterexample added about 0.4 point (48.1%). 89% of repairs on the first attempt.

### 6.4 Failure attribution

- LLM judges: step-level best 14.2% (Who&When), all-at-once 12.50% vs step-by-step 25.51% for GPT-4o, random 19.06%. Reasoning models o1 and R1 "not practically usable". Accuracy falls with context length.
- Code-based blame: SBFL over replayed runs 29.35% action-level vs random 14.36%; REFLECT's intervention approach 76.3 vs 55.5 on WTQ and 70.0 vs 33.3 on SWE-bench. (REFLECT is abstract-level only.)
- SemLoc: LLM proposes constraints, code runs them. Acc@1 42.8% vs LLM-only 37.6%, Ochiai 6.4%.
- ProcessBench: prompted critics 58.0 to 61.9 F1, o1-mini 87.9, small learned PRMs 31.5 to 56.5.
- Takeaway: the model is weak at blaming by reading, fair at proposing what to check, and strong at fixing once the place is given.

### 6.5 What changed it, by how much

| Change | Effect |
|---|---|
| Conflict localisation (QXR) vs direct judging | recall +.34 to +.39 on VitaminC for three strong models |
| Minimal core vs generic error text | fabrication 79% to 7% for one model (n=14) |
| Localised sketch vs whole program | 41.7% to 47.7% for CodeGemma |
| Counterexample on top of sketch | +0.4 point |
| Counterfactual verification in SemLoc | +12.0 Acc@1 |
| Newer model generation (PDDL) | F1 .46 (GPT-4o) to .85 (best 2026) |
| Test traces in prompt | F1 .85 to .78 at default effort |
| High effort | DeepSeek V4 Pro pass .82 to .92; GPT-OSS-120B F1 .49 to .15 (with traces) |
| Sound verifier vs same-model critic | Game of 24: 36% vs 3% |

### 6.6 What nobody has tested

Reiter-style conflicts and hitting sets over **several failed attempts of one model**, at equal tokens, against best-of-N with the same checker, reflection, or a simple blame rule (K23). Closest evidence (Stechly, Snell, Brown) favours simple sampling when a sound checker exists, and is from GPT-4-era models.

## 7. What our agent should take

Status marks as in the header. "Part" = schema part. Evidence ids refer to evidence_a-d.jsonl; K ids refer to claims.jsonl (prefix C09.01-).

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Compute hitting sets in code, never by the model.** When blame must be assigned over several failed checks, the program builds minimal conflicts and the minimal hitting sets. The model never does the hitting-set step. | G5, S5/S6 | [E] (theory) and [S] (LLM data: generate diagnoses F1 .784, sd .322) | a02, d01, b14; K01, K09 |
| A2 | **Property-test any hitting-set code against brute force**, including the Greiner counterexample. Do not trust a published algorithm by reading it. | G5 (engineering rule) | [E] | a02, a03, b01, d05; K02 |
| A3 | **Bound the size.** Use a cap (start at 2) and iterate it upward only if no hitting set exists within the cap. Recompute from all conflicts after each new attempt. | S6 | [E] (Reiter's own design plus 3 sources on pruning) | d02, d03, a10, b05, a28; K05, K26 |
| A4 | **Revise from a located failure, not from the model's opinion.** Show the failing check output, not a self-review. Already G2. This line reinforces it with 3 independent sources: models cannot find their errors but can fix them once shown. | G2 | [E] | c22, c23, c24; K15 |
| A5 | **Do not use model-only blame for a failed multi-step chain.** Step-level accuracy 14.2% at best; reasoning models under 10%. Use code-located blame. | G2, G10 | [E] | c17, c18, c19, c21; K14 |
| A6 | **Never use the same model as the consistency oracle.** Oracle must be code or a sound checker. | G2/G3 | [E] in direction (Stechly d08 plus the three self-correction papers), [S] for numbers | d08, c23, c24; K29 |
| A7 | **Keep best-so-far by a code check on every revision.** Naive revision turns about 38% of correct answers wrong. | S5, S9 | [E] with c23 and c22 (correct-to-wrong exceeds reverse) | d10, c23, c22; K30 |
| A8 | **Cap revision rounds at 2.** 89% of repairs on the first try; gains flatten after about 4 iterations. | S5 | [E] | c08, c25, c26; K16 |
| A9 | **Count conflict-computation tokens inside the budget.** RepairAgent about 270,000 tokens per bug; pairwise oracle checks 435 to 4,950 calls. | G7 | [E] by schema rule; numbers [S] | c27, c12; K20, K21 |
| A10 | **Baseline fairness.** In every test give best-of-N the same code checker the scaffold uses. Coverage 98.44% vs vote 41.41% shows selection is the bottleneck. | G7 | [E] | d09, d10, d11; K31 |
| A11 | **Score by running, not by overlap.** F1 .87 with test pass .82. | G3 | [E] by schema, [S] here | b16, c01; K11 |
| A12 | **Use an approximate ranker first, exact hitting set only on small step counts.** | G12 | [E] | b12, b13, a14, b03, a28; K04 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Conflict set + hitting set over several failed attempts picks the step to change better than model blame, best-of-N, or "blame the last step of the smallest failed check".** This is the whole bet. | S5/S6 | [S] (no direct test; toy sim shows only a +6 to -3 point edge over the cheap rule) | d09, d16, d17, b28; K23, K36 |
| T2 | **Feeding a minimal failing-check set rather than raw error text improves revision** on strong current models. | G2, S5 | [S] (Sarkar, He, older GPT-4 first-error result) | b19, c15, a18, d09; K07, K08 |
| T3 | **Measure empty and size-1 conflict rates** on real traces before building anything. | S5/S6 | [S] | d06, d17; K28 |
| T4 | **Size cap recall.** Does cap 2 or 3 keep the culprit on real traces? | S6 | [S] | d16; K27 |
| T5 | **Cheap prior on step type vs model-stated confidence** for ranking. | S6, memory | [S] | d07, d05; K33, K34 |
| T6 | **Counterfactual toggle on code-checkable components** (does flipping this step change the failure?). | S5 | [S] | c09, c10, c20; K12, K32 |
| T7 | **Probe by maximum split of top diagnoses vs random** (link: probing subfield). | S6 | [S] | a09, a10; K24 |
| T8 | **Effort ladder per model**, logging overflow, parse failures and wrong answers separately, to set G11 caps. | G11 | [C] | b18, d14, d15; K10, K35 |
| T9 | **Show 1, 3 or all suspect steps at revision.** | S5 | [S] | c11; K13 |
| T10 | **Union of different strategies vs N samples of one strategy at matched tokens.** | G4, G7 | [S] | a17, c06; K18 |
| T11 | **Typed conflict (minimal correction subset) vs core.** | S5 | [S] | a20, b20; K07 |

Items from this subfield that must NOT go to the schema now: ranking by probability, entropy probe choice, and "assume normal" for text steps. Section 9 gives the reasons.

## 8. Concrete tests on our bench

All tests give both arms the same token budget. Count conflict computation inside the budget. The baseline always has the same code checker as the scaffold. Use the harness conventions of the bench skill (`/bench`, arm list, batch).

| # | Item type | Arm A (diagnosis) | Arm B (baseline) | Metric | Expected effect |
|---|---|---|---|---|---|
| E1 | Checkable tasks where one attempt chain has seeded step errors (ARC-style programs; math chains with injected wrong steps). 100 items, 1, 2 and 3 errors | Code-run checks give conflicts; hitting set (cap 2, raise on empty) names suspects; model revises the top suspect with the failing output | (B1) model names the faulty step itself; (B2) blame the last step of the smallest failed check; (B3) best-of-N with the same checker | Rate that the named step is a true error step (hit@1); final pass rate at equal tokens | Beats B1 by 20+ points; beats B2 by 0 to 6 points (toy says small). If edge over B2 is under 3 points, ship B2 |
| E2 | Same items as E1 | Hitting set from all conflicts so far, recomputed per attempt | Hitting set from the latest attempt only | hit@1 and tokens to pass | Recompute wins as errors accumulate (Theorem 5.7); small on k=1 |
| E3 | 100 dev traces from our own runs, hand-labelled error steps | Log only: empty conflict rate, size-1 rate, culprit recall at cap 1, 2, 3, candidate-set size | none | rates | Predict 6% to 27% empty with weak checks; real may be higher on prose. If empty over 50%, build step-level checks first |
| E4 | Infeasible and contradictory items (unsatisfiable constraint sets, contradictory fact sets), at least 40 items | Revise from minimal failing core | Revise from raw error text; best-of-N | fabrication rate on infeasible items; accuracy on feasible items | Replicate Sarkar on strong models. Expect fabrication gap to shrink for strong models. Expect near zero accuracy gain |
| E5 | Contradictory claim sets of 24 to 32 claims with 2 to 6 contradictions (VitaminC-style, own data) | QuickXplain via model oracle, code hitting set | One-shot "remove inconsistent claims" | recall and F1 of kept valid claims; oracle calls | Replicates recall gain (+.3) on the model we use. Expect no gain on easy sets |
| E6 | E5 items | Same QXR loop with a code oracle where possible | Same loop with the same-model oracle | final consistency; call counts | Same-model oracle worse (Stechly pattern) |
| E7 | Items from E1 | Counterfactual toggle on code components before blame | Hitting set alone | hit@1; extra tokens | +5 to +12 points hit@1 if SemLoc generalises; skip if cost over 1.5x |
| E8 | Items from E1 | Rank diagnoses by prior step-type fail rate (clamped to (0, 0.5)) | Rank by size; rank by model confidence | hit@1 | Prior beats confidence; small gain over size alone |
| E9 | Revision step on E1 | Show 1, 3 or all suspect steps | each other | pass rate at equal tokens | 1 to 3 beat all |
| E10 | Effort ladder | per model, low/medium/high | none | pass rate with overflow, parse failure, wrong answer logged separately | A collapse on some models; set caps from curve |
| E11 | All | Hitting-set unit test against brute force (property test, 1,000 random collections, Greiner collection fixed) | none | exact match | 100% required before any other test counts |

Reporting: for every arm log hit@1, final pass, tokens by state (S5, S6), and the number of flips right-to-wrong and wrong-to-right (schema section 6). Report bootstrap intervals; with n=100 a 6-point edge is not detectable, so decide thresholds up front (see UNKNOWNS.md).

## 9. What does not transfer, and why

1. **"Assume normal" has no sound meaning for reasoning steps.** In circuits each component has a fixed model, the observations are exact, and independent failure is plausible. Steps in a chain are produced by one model, have correlated errors (G4), and have no model of correct behaviour except a checker. The benchmarks (ISCAS85, 74XXX) are exact circuits (critique, weak spots).
2. **Probabilities of failure.** Priors for circuit gates come from hardware reliability. We have no such priors. Rodler's soundness needs priors below 0.5; a step-failure-rate prior above 0.5 breaks the guarantee (d05). Use prior ranking only after a class record exists, and clamp.
3. **Entropy-guided probing.** It rests on a distribution over diagnoses that we cannot yet justify, and the founding paper was not read (K25). Not added.
4. **Many failing tests.** CFaults and SNIPER results use up to 131 failing tests per program (TCAS). One failed answer gives one conflict at most. Gains from joint consistency across all failing tests (480/682) do not transfer to a one-conflict problem.
5. **Exponential scaling results.** CDA*, SDE and BDD limits matter for 160-gate circuits. Our component count is 5 to 30. The cap makes the problem small. Efficiency work (DynamicHS, MergeXplain, HS-DAG tuning) is low priority (K22).
6. **Strong-fault models and kernel diagnoses.** Needed when components also have fault models (de Kleer, Mackworth, Reiter 1992). We do not model how a step is wrong, only that it is.
7. **Counterfactual rollouts on prose.** About 14,400 rollouts per trace; AOC falls with model size (d12, d13). Use only on code components, or on a few coarse steps.
8. **Per-test merging.** Not relevant to us as long as we compute one hitting set over all conflicts.
9. **Completeness.** NP-hard. Under a token cap we can only claim "all diagnoses up to size k given the conflicts found". Say so in the log.
10. **LLM-only repair benchmarks (PDDL, program repair).** Model names act as semantic cues and F1 overlap is not pass rate. Results do not carry to puzzle reasoning where no reference repair exists.
11. **Learned process reward models.** ProcessBench shows small PRMs lose to prompted critics. This does not support training anything for us; we do not train.

## 10. Open questions

1. Does a conflict set plus hitting set over the failed checks of several attempts pick the step to revise better than model blame or best-of-N at equal tokens? No paper tests it. (Gap 1.)
2. What is the right component for text reasoning: step, claim, constraint, tool call? How often are conflicts empty or size 1 on real traces? (Gap 2.)
3. How far can the cap be pushed (1 or 2) before the culprit is lost on real multi-error traces, and what does it save in tokens? (Gap 3.)
4. Does a minimal conflict beat raw error text on strong current models, and by how much with more than 14 infeasible items? (Gap 4.)
5. Can a cheap prior beat model-stated confidence for ranking? (Gap 5.)
6. What does de Kleer and Williams 1987 actually prove about priors, Bayes updating and entropy? Needs a library copy. (Gap 6.)
7. Why does high effort help some models and collapse others on repair? Overthinking, context length or prompt format? (Gap 7.)
8. Does QXR over-pruning repair hold when the oracle is the same model that makes errors, and with noisy calls? (Gap 8.)
9. How do diagnosis methods compare to delta debugging and spectrum baselines on reasoning text, and do counterfactual re-runs transfer? (Gap 9.)
10. Are there known bugs left in HS-DAG variants? (Pill et al. unopened.) (Gap 10.)
11. Does the 70.8% vs 59.1% portfolio gain survive a matched-compute control?
12. Does the Sarkar result (fabrication 79% to 7%) replicate with more than 14 infeasible items and other model families?
13. Does the AR-LSAT drop in VERGE's ablation (a20) mean MCS feedback can hurt, and when?
14. Is there a better unit than a step: for example a claim with a support set recorded by code?

## 11. Sources

[V] = opened and read this session (full text or substantial pages). [M] = snippet, abstract or landing page only.

| Mark | Source | URL | Evidence ids |
|---|---|---|---|
| [V] | Reiter (1987) A theory of diagnosis from first principles. Artificial Intelligence 32 | https://cse.sc.edu/~mgv/csce580sp14/reiter-diagnosis.pdf (DOI 10.1016/0004-3702(87)90062-2) | d01 to d04 (a01, a25, b25 were the earlier unread attempts) |
| [V] | Greiner, Smith, Wilkerson (1989) A correction to the algorithm in Reiter's theory of diagnosis | https://www.cse.sc.edu/~mgv/csce580sp14/greinerCorrectionReiter.pdf | a02, a03, a04, b01, b02 |
| [M] | de Kleer, Williams (1987) Diagnosing multiple faults. Artificial Intelligence 32 | https://doi.org/10.1016/0004-3702(87)90063-4 | a05, b26 |
| [V] | de Kleer, Mackworth, Reiter (1992) Characterizing diagnoses and systems (garbled OCR) | https://www.cs.ubc.ca/~mack/Publications/AI92-KM.pdf | a08 |
| [V] | Stern, Kalech, Feldman, Provan (2012) Exploring the duality in conflict-directed model-based diagnosis. AAAI | https://ojs.aaai.org/index.php/AAAI/article/download/8231/8089 | a06, a07, a23, b06, b07 |
| [M] | Stern et al. 2012 landing page | https://ojs.aaai.org/index.php/AAAI/article/view/8231 | c30 |
| [V] | Siddiqi, Huang (2011) Sequential diagnosis by abstraction. JAIR | https://arxiv.org/pdf/1401.3892 | a09, a10, a24 |
| [V] | Grastien, Haslum, Thiebaux (2023) A more general theory of diagnosis from first principles | https://arxiv.org/pdf/2309.16180 | a11, a12, a13 |
| [V] | Roos (1993) Efficient model based diagnosis | https://arxiv.org/pdf/2209.09819 | a14, b23, b24 |
| [V] | Rodler (2020) DynamicHS | https://arxiv.org/pdf/2012.11078 | a15, d05 |
| [V] | Wassermann (2000) Local diagnosis | https://arxiv.org/pdf/cs/0003051 | a21, b22 |
| [M] | Williams, Ragno (2007) Conflict-directed A* | https://groups.csail.mit.edu/mers/old-site/abstracts/jdam.html | a26 |
| [V] | Gainer-Dewar, Vera-Licona (2016) The minimal hitting set generation problem | https://arxiv.org/pdf/1601.02939 | b03, b04, b05 |
| [V] | Shchekotykhin, Jannach, Schmitz (2015) MergeXplain. IJCAI | https://web-ainf.aau.at/pub/jannach/files/Conference_IJCAI_2015.pdf | b08, b09 |
| [V, skimmed] | Shchekotykhin, Fleiss, Rodler, Friedrich (2012) Direct computation of diagnoses | https://arxiv.org/pdf/1209.0997 | c28 |
| [M] | Pill, Quaritsch, Wotawa (2016) On the practical performance of minimal hitting set algorithms (download damaged) | https://papers.phmsociety.org/index.php/ijphm/article/view/2363 | b27 |
| [M] | Hofer, Wotawa (2012) Combining slicing and spectrum-based fault localization | https://ebooks.iospress.nl/pdf/doi/10.3233/978-1-61499-098-7-420 | c29 |
| [V] | Peischl, Wotawa (2003) Modeling state in software debugging of VHDL-RTL designs | https://arxiv.org/pdf/cs/0311001 | b10, b11 |
| [V] | Abreu, Zoeteweij, van Gemund (2009) Spectrum-based multiple fault localization (BARINEL). ASE | https://webarchive.di.uminho.pt/haslab.uminho.pt/ruimaranhao/files/ase09-1.pdf | b12, b13 |
| [V] | Orvalho, Kwiatkowska, Janota, Manquinho (2025) Model-based diagnosis with multiple observations (CFaults) | https://arxiv.org/pdf/2512.02898 | a16, a28 |
| [V] | Orvalho, Janota, Manquinho (2024/2025) Counterexample guided program repair using zero-shot learning and MaxSAT-based fault localization | https://arxiv.org/pdf/2502.07786 | a17, c06, c07, c08 |
| [V] | He, Kirschbaum, Kasiviswanathan (2026) Global consistency repair for natural-language claim sets (QXR) | https://arxiv.org/pdf/2601.13600 | a18, a19, a27, c12, c13, c14 |
| [V] | Singh, Cassel, Weir, Feng, Bayless (2026) VERGE | https://arxiv.org/pdf/2601.20055 | a20 |
| [V] | Sztyber-Betley et al. (2025) Are diagnostic concepts within the reach of LLMs? DX 2025 (OASIcs 136) | https://drops.dagstuhl.de/storage/01oasics/oasics-vol136-dx2025/OASIcs.DX.2025.2 | a22, b14, b15, c04, c05 |
| [V] | Karimi Bavandpour, Bercher (2026) LLM-only PDDL domain repair with open-weight models | https://arxiv.org/pdf/2608.17341 | b16, b17, b18, c01, c02, c03, d14 |
| [V] | Sarkar (2026) From errors to proofs: minimal-core-guided repair | https://arxiv.org/pdf/2608.14771 | b19, b20, b21, c15, c16 |
| [M] | Gap note on LLM agents using Reiter-style conflicts (not a source; a search record) | https://arxiv.org/pdf/2608.14771 | b28 |
| [V] | Yang et al. (2026) SemLoc | https://arxiv.org/pdf/2603.29109 | c09, c10 |
| [V] | Sepidband, Pham, Hemmati (2026) On the role of fault localization context for LLM repair | https://arxiv.org/pdf/2604.05481 | c11 |
| [V] | Zhang et al. (2025) Which agent causes task failures and when? (Who&When) | https://arxiv.org/pdf/2505.00212 | c17, c18 |
| [V] | Ge et al. (2025) Who is introducing the failure? | https://arxiv.org/pdf/2509.13782 | c19 |
| [M] | REFLECT (2026), abstract via alphaxiv | https://www.alphaxiv.org/abs/2606.09071 | c20 |
| [M] | Zhang et al. (2025) AgenTracer, abstract | https://arxiv.org/abs/2509.03312 | c21 |
| [V] | Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location | https://arxiv.org/pdf/2311.08516 | c22 |
| [V] | Huang et al. (2024) Large language models cannot self-correct reasoning yet. ICLR | https://arxiv.org/pdf/2310.01798 | c23 |
| [V] | Kamoi et al. (2024) When can LLMs actually correct their own mistakes? TACL | https://aclanthology.org/2024.tacl-1.78.pdf | c24 |
| [V] | Chen et al. (2024) Teaching large language models to self-debug. ICLR | https://arxiv.org/pdf/2304.05128 | c25 |
| [V] | Farzandway, Ghassemi (2025) Automated repair of C programs using LLMs | https://arxiv.org/pdf/2509.01947 | c26 |
| [V] | Bouzenia, Devanbu, Pradel (2024) RepairAgent | https://arxiv.org/pdf/2403.17134v2 | c27 |
| [V] | Zheng et al. (2024) ProcessBench | https://arxiv.org/pdf/2412.06559 | d06, d07 |
| [V] | Stechly, Valmeekam, Kambhampati (2025, TMLR) On the self-verification limitations of LLMs | https://arxiv.org/pdf/2402.08115 | d08, d09 |
| [V] | Snell, Lee, Xu, Kumar (2024) Scaling LLM test-time compute optimally | https://arxiv.org/pdf/2408.03314 | d10 |
| [V] | Brown et al. (2024) Large language monkeys | https://arxiv.org/pdf/2407.21787 | d11 |
| [V] | Lanham et al. (2023) Measuring faithfulness in chain-of-thought reasoning | https://arxiv.org/pdf/2307.13702 | d12 |
| [V, first 100,000 of 124,053 characters via fetch summary] | Bogdan, Macar, Nanda, Conmy (2025) Thought Anchors | https://arxiv.org/html/2506.19143 | d13 |
| [V] | Gema et al. (2025, TMLR) Inverse scaling in test-time compute | https://arxiv.org/pdf/2507.14417 | d15 |
| own | Toy Monte Carlo simulation, session scratchpad (not literature) | n/a | d16, d17 |
