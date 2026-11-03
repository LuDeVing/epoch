# Hitting-set tree search: deep document

*Subfield C09.04 of model-based diagnosis. Written from evidence_a-d.jsonl (ids a01-a26, b01-b27, c01-c27, d01-d18), claims.jsonl (K01-K29) and critique.md in this folder. Evidence marked [V] was opened in a research session; [M] is snippet or second-hand. No source in this folder tests a hitting-set tree inside an LLM agent. Everything about our agent is by analogy and is labelled so.*

## 1. What it is

Model-based diagnosis asks: a system should work, it does not, which components are broken? Reiter (1987) gave a clean answer. A **conflict set** is a set of "component is ok" assumptions that cannot all be true, given the system description and the observation. A diagnosis is a minimal set of components that, if assumed faulty, makes everything consistent again. Reiter's theorem (his Theorem 4.4, restated in b01/b03): **diagnoses are exactly the minimal hitting sets of the collection of conflict sets.** A hitting set touches every conflict. Minimal means no proper subset also touches every conflict.

Tiny worked example (a01): components X, Y, Z. The observation gives one minimal conflict {okY, okZ}. Hitting sets: {Y}, {Z}, {Y,Z}. Only {Y} and {Z} are diagnoses, because {Y,Z} is not minimal.

The **hitting-set tree (HS-tree)** is Reiter's way to build these sets (a02, c06):
- It is a breadth-first tree.
- Each non-leaf node is labelled with a conflict that the edge labels on the path so far do not yet hit.
- A node gets one child per component in its conflict. The edge to the child is labelled with that component.
- A node with no unhit conflict is a leaf. Its path is a hitting set (a diagnosis candidate).
- Pruning rules close nodes whose path is a superset of a found hitting set, close duplicates, and remove edges that became redundant.
- Conflicts come on demand. At a node, a theorem prover or conflict finder (for example QuickXplain) is asked for a conflict that avoids the path components. If none exists, the node is a leaf.

**The DAG fix.** Greiner, Smith and Wilkerson (1989) showed that Reiter's pruned tree can lose minimal hitting sets. Their repair, **HS-DAG**, reuses a node when the same path label set recurs, so the structure is a directed acyclic graph. It also relabels nodes and removes redundant edges when a smaller conflict shows up.

**Why it matters for our agent.** The agent has to search over suspects (candidate causes or candidate wrong steps) given contradictions it finds. The transferable ideas are control ideas, not speed ideas:
1. A suspect set is valid only if it touches every contradiction found so far, and no smaller subset does (K01).
2. Early pruning of suspects is unsafe when a later contradiction is smaller than an earlier one (K02).
3. Cap the size of the suspect set (K07).
4. Carry the suspect list from one probe to the next instead of rebuilding it (K08, single source).
5. Choose the next probe to split the remaining suspects (K14, K27).

Links to other subfields (not covered here): abductive diagnosis, probe selection and entropy (Shannon information, entropy), SAT solving/DPLL, Monte Carlo tree search and pruning of decision trees, resolution and saturation. See 00_FIELDS.md for those documents.

## 2. History and theories in depth

**1987: two founding papers.** Reiter's "A theory of diagnosis from first principles" (Artificial Intelligence 32(1)) defines conflicts, diagnoses and the HS-tree. De Kleer and Williams's GDE ("Diagnosing multiple faults", same issue) reaches candidates from conflicts with an ATMS (assumption-based truth maintenance) and uses entropy to pick the next measurement (a24, c21 [M]). The two are parallel. GDE-style tools prevail in circuit work. HS-tree tools prevail in knowledge-base and ontology debugging (a24). Reiter himself asked whether new diagnoses can be built from an old tree after a new observation (b15). That question was answered 32 years later by DynamicHS.

**1989: the correction.** Greiner, Smith and Wilkerson, "A correction to the algorithm in Reiter's theory of diagnosis" (Artificial Intelligence 41; 10 pages, no benchmark; b01 [V], PDF read). Their counterexample is the collection {{a,b},{b,c},{a,c},{b,d},{b}}. Reiter's pruned tree no longer represents the minimal hitting set {a,b}. A second case, {{a,b},{a},{b}}, shows why nodes must be relabelled. The cause is the interaction of two rules: the rule that closes a node whose label set was already used, and the rule that removes redundant edges when a subset conflict appears. The paper proves HS-DAG correct (Theorem 2). The trigger, confirmed in b01: the conflict finder returns **non-minimal conflicts** (a later conflict is a subset of an earlier one). With minimal conflicts only, the original algorithm is fine.

**1989-2000: theory.** Wassermann (2000, a16 [V]) showed consistency-based diagnosis is kernel semi-revision from belief change. Conflicts are kernels, an incision function picks one element per kernel, and diagnoses are minimal incisions. This ties diagnosis to belief revision. It is a theory paper with no experiments.

**2001: Wotawa's HST.** Wotawa (Information Processing Letters; a05, b05 [M], via Pill et al. and the survey) changed the construction so nodes that Reiter's method would later prune are never built. Components are numbered and only children with labels in a fixed range are expanded, like subset enumeration. It cuts set-containment checks and restores a plain tree with the same output. The survey (b04 [V]) says it makes the DAG unnecessary. See section 5 for the "does not dominate" result.

**2003: Boolean approach.** Lin and Jiang's BHS-tree splits on an element: conflicts containing it are hit, the rest form a second branch. It needs all conflicts known in advance, unlike HS-DAG or HST (a23). Pill and Quaritsch (2012) found that choosing the split element from a smallest conflict helps a lot. Pill et al. 2011 reported BHS-tree not generally favourable over HS-tree variants when only a limited set of diagnoses is wanted (a09 [M]).

**2009-2014: approximate and direct methods.**
- Staccato (Abreu and van Gemund 2009) ranks components by how many unhit conflicts they appear in and searches a heuristic-limited space. It is approximate, so results need a minimality check (a22). In the Pill 2016 tests it could not solve even the smallest random samples in complete mode (b09).
- FastDiag (Felfernig, Schubert, Zehentner 2012, a14) finds one preferred minimal diagnosis directly by divide and conquer, with the effort of finding one conflict.
- Stern et al. (2012, c22 [M]) exploit the duality between conflicts and diagnoses.
- SAFARI (Feldman et al. 2010, c23 [M]) uses stochastic search for minimal-cardinality diagnoses.
- Inv-HS-Tree (Shchekotykhin et al. 2012, a15, c11) computes diagnoses directly with Inv-QuickXplain, without precomputing conflicts.
- SATbD (Metodi et al. 2014, b11, b12) encodes diagnosis directly into SAT.

**2015: several conflicts per call.** MergeXplain (Shchekotykhin, Jannach, Schmitz; a13, b18) splits the constraint set in halves and returns several minimal conflicts per prover run.

**2016: the benchmarks.** Pill, Quaritsch and Wotawa (a08, b07-b10) compare HS-DAG, HST, GDE, Boolean algorithms, Staccato and SAT variants. Gainer-Dewar and Vera-Licona (a06, a07, b06) survey and benchmark about two dozen minimal-hitting-set algorithms on non-diagnosis data.

**2019-2023: Rodler's line of work.** DynamicHS keeps the tree across measurements (a10, a11, b15-b17). RBF-HS gives linear-space best-first search (b13, b14, c08). The 2023 thesis summarises all of it (c06-c09). All of this comes from one research group (Rodler, Shchekotykhin, Friedrich) on ontology debugging. No outside replication was found (critique, d17).

**2023: generalisation.** Grastien, Haslum and Thiebaux (b25 [M]) generalise Reiter's framework beyond static systems.

**2024-2026: LLMs and neighbours.**
- Hu et al. 2024 (UoT, d10-d12): LLMs pick questions that split the candidate set, with entropy computed in code.
- Sztyber-Betley et al. 2025 (a18, b19, b20, c01-c05, d07-d09): the only test of the conflict-then-hitting-set pipeline in LLMs.
- Plank and Wotawa 2026 (a17, a20, a26, b21, b22): 13 language models diagnose circuits and heating systems from text, no hitting-set method.
- Agent failure attribution (Famas 2025, AgentLocate 2026; d01-d04, d18): neither uses a hitting set.
- Root-cause analysis (RCA) agents on telemetry (c14-c18, d13).
- Hybrid solver-plus-LLM designs (Delta1, SafeMin, HyMUSE: b24, c25, c26, d05, d06).

**Competing views on whether trees are the right tool.**
- Control view: tree search is kept because it allows on-the-fly conflict computation and anytime behaviour (b10, c06). It can be stopped at any time and returns the diagnoses found so far.
- Speed view: tree search is not the fastest. Specialised enumerators and direct SAT encodings beat it (a06, b06, b11, b12, a15).
- Both are right for their goals. The agent needs the control view, not the speed view.

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, O = open (no data).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Diagnoses = minimal hitting sets of minimal conflicts | Example: conflict {okY,okZ} gives diagnoses {Y},{Z} only. SCS={{1,2},{1,2,5},{2,3,4},{2,4,5}} gives {2},{1,4},{1,3,5} | Reiter 1987 (a01, a02, b03) | E (K01) |
| Reiter's pruned tree loses minimal hitting sets | Counterexample {{a,b},{b,c},{a,c},{b,d},{b}} loses {a,b}; second case {{a,b},{a},{b}} | Greiner et al. 1989 (b01, b02) | E (K02) |
| The bug needs non-minimal conflicts | Trigger = later subset conflict meeting the close and relabel rules | b01, a03, b10 | E for mechanism; prevalence in LLM output not measured (K03) |
| Hitting-set existence is NP-complete; counts explode | HER2+.SHORT: 122 elements, 534 sets, 128,833,310 minimal hitting sets, only 26,436 of size 7 or less | Gainer-Dewar and Vera-Licona 2016 (a06, a07) | E (K07) |
| One more minimal diagnosis is NP-hard even with a polynomial prover; HS-Tree needs exponential space | Ontology debugging cited as 2-NEXPTIME-complete for some logics | Rodler 2022 (b14) | S |
| Pure hitting-set speed has no winner | GDE best to about 30 components (10 ms); Boolean algorithms lead beyond, more than 10x over GDE above 200 components; HS-DAG catches up near 500 ms; SAT variants about 2 orders of magnitude slower than HS-DAG/HST/GDE | Pill et al. 2016 (a08, b07, b08) | S (K04) |
| HST vs HS-DAG depends on size bound | Max size 1 and 2: HST ahead most of the time. Max size 3: HS-DAG ahead over most of the range. HST scaled worse above about 20 components on disjoint conflicts (TSA1). Limits 300 s, 2 GiB | Pill et al. 2016 (a05, b09) | S (K05) |
| Tree/DAG methods are far from fastest on generic data | MMCS, RS, HTC-BDD far faster; HTC-BDD 4 to 10x faster than rivals but often hit 32 GB; parallel MHS2 gain 2.33x; 3600 s cap | Gainer-Dewar 2016 (a06, b06) | S (K06) |
| DynamicHS (keep the tree across probes) saves time | Faster in 99.4% of scenarios and 96% of single sessions (ENT 96%, SPL 97%, MPS 95%); median saving 52%, max 75%; HS-Tree up to 4x average time, over 9x in single sessions; hardest cases median 64%, max 89%; 20 sessions per scenario | Rodler 2020/2021 (a11, b16) | S (K08) |
| DynamicHS pilot | 59% fewer reasoner calls, 42% less time; toy example HS-Tree 14/0/9 calls vs DynamicHS 6/4/5 | Rodler 2019 (a10, b15) | S |
| DynamicHS loses sometimes | Median 2% worse in (SPL, D, 30) and 3% worse in (MPS, fal-ce, 30); HS-Tree 76% less time in (ctx-se, 20) and 32% less in (D, 30); max extra cost 0.8 s and 12 s | Rodler 2021 (b17) | S (K09) |
| RBF-HS: linear space, best-first, sound | Memory saving up to 98% (HS-Tree up to 4900% more); equal or lower runtime in 40% of cases, savings up to over 88%; one case HS-Tree hit 32 GB while RBF-HS stored at most 125 nodes; runtime 0.04/24/744 s min/avg/max | Rodler 2022 (b13, c08) | S (K10) |
| Soundness needs fault probabilities below 0.5 | Fix: scale all by a constant c in (0, 0.5) | Rodler 2020 (a12) | S (K11) |
| Hard reasoner calls cost far more | "At least 4 and up to over 100 times" (a12); another passage says median 19x, up to 120x (critique note 2). Quote both | Rodler 2020 | S |
| Several conflicts per call (MergeXplain) | Up to 54% faster on CSP and spreadsheets (costasArray-13: 1,379,842 ms to 629,366 ms); 15% to 45% on DXC synthetic, first 5 diagnoses; 20-30% random positions, up to 75% when unfavourable; but 11% slower on queens-8 and 5% slower on one spreadsheet | Shchekotykhin et al. 2015 (a13, b18) | E (K12) |
| FastDiag finds a preferred diagnosis directly | Mann-Whitney: best-first vs breadth-first HSDAG p=6.6e-5; FastDiag vs breadth-first p<2.4e-7; FastDiag vs best-first p=0.12; CLib KB, 34 variables, about 65 constraints | Felfernig et al. 2012 (a14) | S |
| Direct diagnosis beats conflict-then-hit when conflicts are many | OAEI 2011: 286 alignments, 146 analysed; both methods got the requested 1, 9, 30 diagnoses for 133; in 13 cases only Inv-HS-Tree finished (HS-Tree failed within 2 h); about 25 s for one diagnosis. SATbD: 99.3% of 1557 c7552 observations in 30 s, all within 80 s; SAFARI minimum-cardinality in only 13% | Shchekotykhin 2012; Metodi 2014 (a15, c11, b11, b12) | E (K13) |
| Entropy beats split-in-half for query choice | Entropy gave significantly fewer queries even with equal fault probabilities; but DynamicHS saving did not differ by heuristic (ENT 50%, SPL 52%, MPS 52%) | Shchekotykhin 2014 (c10); Rodler 2020 (a25) | E (K14) |
| LLM conflict and diagnosis pipeline on circuits | o3-mini F1 0.917 +/- 0.249 (conflicts), 0.784 +/- 0.322 (diagnoses); up to 6 MSOs, 6 conflicts, 165 diagnoses; non-reasoning models near zero on unseen examples; incidence matrix: o1, o3-mini perfect, 4o-mini F1 0.47 +/- 0.15 and accuracy 0.00; about 30 USD per o1 iteration; 23 circuits; 10 repeats for 4o-mini and o3-mini, o1 once | Sztyber-Betley et al. 2025 (a18, b19, b20, c01-c05, d07, d08) | S (K15) |
| Prompt knowledge did not help | Dedicated (rich domain knowledge) vs Broad prompt: similar MSO results; correct incidence matrix as input barely changed MSO results | Same (c04) | S (K16) |
| Conflict score artefact | Rising score with complexity comes from zero-conflict cases scoring badly; empty-vs-empty scored 1 | Same (c03, a19) | S |
| Plain LLMs diagnosing from text | Hit rate: Gemini 2.5 Flash 79.5%, Mistral Large 76.9%, Llama 4 Scout 17B 38.5%, Mistral 7B v0.3 25.6%, Phi-2 and TinyLlama 0%. Hallucination 20.5%, 15.4%, 7.7% for the top three; most small models above 70%. Weighted score (max 2.0): 1.846, 1.832, 1.526, 1.235, TinyLlama 0.314. 7 systems, 13 models | Plank and Wotawa 2026 (a17, b21, a26) | S (K17) |
| LLMs call almost every formula satisfiable | More than 2700 3-SAT and over 700 2-SAT formulas; miss the easy-hard-easy phase transition; only reasoning models do well on 2-SAT | Zhang, Chen, Chen 2026 (b23) | S (K18) |
| RCA agents on real telemetry | OpenRCA best 11.34% (Claude 3.5 Sonnet, 335 failures); 1675 runs, perfect accuracy 3.9% to 12.5%; hallucinated interpretation 71.2%, incomplete exploration 63.9%, symptom-as-cause 39.9%, no cross-validation 18.6%, step exhaustion 4.1%; OpenRCA 2.0 exact match 20.7%, pair F1 34.1%, causal path reachability 61.5% | Xu 2025; Kim 2026; Fang 2026 (c15, c16, c18) | E (K19) |
| Retrieval agent cut hallucination | ReAct 4% vs CoT 12% hallucination; correct 35% vs 39%; 28 of 97 solved by all three | Roy et al. 2024 (c14) | S (K20) |
| Failure attribution by propose-then-verify | AgentLocate agent-level 35.71% (1 evaluator) to 69.05% (3); 5 or 7 evaluators no consistent gain; Qwen-7B, Who&When Algorithm-Generated | Xia et al. 2026 (d01, d02) | S (K23, K24) |
| Spectrum counting beats LLM judges | Famas: agent-level 57.61% (106/184), action-level 29.35% (54/184); random 23.71% and 14.36%; algorithm-generated (126 logs) 55.56% and 23.81%; hand-crafted (58 logs) 62.07% and 41.38%; Tarantula worst | Ge et al. 2025 (d03, d04) | S (K25) |
| Question choice by splitting candidates | UoT: +38.1% mean success over direct prompting (5 datasets, 5 LLMs), +46.6% for Llama3-70B; DX 97.0%; troubleshooting 67.3% vs 43.7%; reward form matters little (DX 90.4/91.3/89.4/89.4) | Hu et al. 2024 (d10-d12) | S (K27) |
| LLM inside a hitting-set tree; non-minimal handling | No study found | critique, d15-d17 | O (K21, K26, K28) |
| Anchoring and no belief update predict wrong LLM RCA answers | Controlled single-fault scenarios; agentic workflows often gave diminishing or negative returns | Riddell et al. 2026 (d13) | S (K29) |

## 4. Mechanisms and models

### 4.1 Data structures
- A **conflict** is a set of component ids. A **collection** CS is a list of conflicts.
- A **hitting set** H of CS intersects every conflict in CS. It is **minimal** if no proper subset of H also hits CS.
- Every diagnosis is a minimal hitting set of the minimal conflicts. A non-minimal hitting set is never reported as a diagnosis (a01 example: {Y,Z}).

### 4.2 Reiter HS-tree (a02, b03), implementable form
```
root: label = first conflict from the conflict finder (none => the empty set is the diagnosis, stop)
queue = [root]   # breadth-first
while queue:
  n = pop front
  h(n) = set of edge labels on path root..n
  if some found hitting set D is a subset of h(n): close n; continue      # prune
  c = a conflict disjoint from h(n)   (first try a known conflict, else ask the conflict finder)
  if none: record h(n) as a hitting set; continue                         # leaf
  label n with c
  for each component x in c: add child via edge x
```
Prunes: (1) close a node whose h(n) equals the label set of a node already built; (2) close a node whose h(n) is a superset of a found hitting set; (3) when a new conflict c' is a proper subset of an existing node label, relabel that node with c' and delete the edges for components no longer in the label. Rule 3 is where the bug lives.

### 4.3 The bug and the fix (b01, b02)
- Collection: {{a,b},{b,c},{a,c},{b,d},{b}}. The set {a,b} is a minimal hitting set: it hits every member, {a} alone misses {b}, and {b} alone misses {a,c}. The minimal hitting sets are {a,b} and {b,c}.
- The small conflict {b} is a subset of {a,b}, {b,c} and {b,d}. Per b01, the pruned tree loses {a,b} through the interaction of the duplicate-label closing rule and the redundant-edge removal rule. The exact step order is in Figure 1 of the paper; this document does not reconstruct it.
- HS-DAG: when creating children, look up an existing node with the same h(n) and point the new edge at it, instead of closing it or duplicating it. Relabel on a smaller conflict and remove only edges that are truly redundant. Theorem 2 proves correctness.
- **Simplest safe alternative for an agent (engineering judgment, not from a source):** do not relabel in place. Keep all conflicts in a list, drop any conflict that is a superset of another, and recompute minimal hitting sets from the minimised list. This removes the trigger. Test it.

### 4.4 HST (Wotawa) (a05, b05, b09)
Number components 1..n. Expand a node only with children whose component index is in a fixed range above the current path. This avoids producing nodes that would be pruned later, so no DAG is needed. Faster for size-1 and size-2 hitting sets. Loses at size 3, and above about 20 components on disjoint conflicts, in a Python implementation (300 s, 2 GiB).

### 4.5 Size cap
Limit tree depth to k. Then only hitting sets of size at most k are found. This is the standard control against explosion (K07). In the HER2+.SHORT example, 26,436 of 128,833,310 minimal hitting sets have size 7 or less.

### 4.6 Best-first order and RBF-HS (a12, b13)
- Give each component a fault probability p. A set's weight is the product of p for members and (1 - p) for non-members. Expand the most probable first.
- Soundness (only minimal diagnoses returned) needs each p below 0.5. Otherwise rescale all p by a constant c in (0, 0.5).
- RBF-HS replaces the stored open list with recursive best-first search. Same order, linear space.
- Agent analogue (untested): keep only the top-k open suspects in context.

### 4.7 DynamicHS (a10, a11)
In sequential diagnosis, after each probe answer conflicts can only shrink and the set of diagnoses can only grow, so most of the tree stays valid. DynamicHS keeps the tree and repairs it. The result is the same diagnoses with a median 52% saving. Agent analogue: carry and edit the suspect list across probes. Single group, ontology debugging, so treat as a hypothesis.

### 4.8 Conflict finding
- QuickXplain (QXP): divide and conquer to find one minimal conflict per call. MergeXplain: several per call (b18). The gain appears only when many conflicts exist.
- To minimise a given conflict in code: for each member, drop it and re-check inconsistency; keep the drop if the rest is still inconsistent. Cost is one check per member. This is standard practice (d15), not a measured LLM result.
- On-the-fly conflict computation is the reason to keep HS-DAG/HST (b10): test whether the path components being faulty restores consistency; if not, ask a solver for an unsat core as the next label.

### 4.9 Probe (measurement) selection (a25, c09, c10, d10-d12)
- ENT: choose the probe with the highest expected information gain.
- SPL: split-in-half, pick the probe that eliminates the most diagnoses in the worst case.
- MPS: most probable singleton.
- UoT recipe for LLMs (d10): the LLM proposes questions and simulates answer branches that divide the current candidate set into a yes group and a no group. Code counts the group sizes and computes entropy. Simulation depth was limited to 3 steps for cost.

### 4.10 Alternatives to conflict-then-hit
- FastDiag (a14): divide and conquer, one preferred minimal diagnosis at the cost of one conflict.
- Inv-HS-Tree (a15): build the tree on diagnoses directly.
- SAT encoding (b11): encode "at most k faulty" and solve.
- Spectrum counting (Famas, d03): count how often each component appears in failing vs passing runs.

## 5. What holds up

**Holds up (two or more independent sources):**
- The core theorem (K01) and the Reiter bug with its HS-DAG fix (K02). Greiner et al. proved it; the survey and Pill et al. restate it.
- Explosion of minimal hitting sets and the use of a size cap (K07).
- Several conflicts per call helps on harder problems (K12).
- Direct methods beat conflict-then-hit when conflicts are many (K13).
- Entropy is a sound probe rule (K14).
- RCA agents fail often, in the same ways across models (K19: three papers).

**Failures, losses and boundary conditions:**
- MergeXplain loses 5% to 11% when only one conflict exists (a13, b18).
- DynamicHS median was 2% to 3% worse in two scenarios; HS-Tree was 76% faster in one extreme scenario; the absolute loss was at most 12 s (b17).
- HST wins at size 1 and 2, loses at size 3 and above about 20 components on disjoint conflicts (a05, b09). No algorithm dominates (a08).
- Hitting-set benchmarks used pre-computed conflicts or non-diagnosis data. They do not measure conflict-finding cost, which dominates in practice (critique).
- The Reiter bug only fires with non-minimal conflicts. If the conflict finder always returns minimal conflicts, the original is fine (b01).
- Staccato (approximate) must be re-verified for minimality (a22).

**No outside replication.** DynamicHS, RBF-HS, Inv-HS-Tree and MergeXplain all come from the Rodler/Shchekotykhin/Friedrich/Jannach circle, with random fault probabilities on ontologies (critique). Treat the exact savings as one lab's numbers.

**Moderators that were reported:**
- Problem type (MergeXplain gain 15% to 54% vs slight loss).
- Cardinality bound (HST vs HS-DAG).
- Component count (GDE best below about 30, Boolean beyond).
- Fault probability (must stay below 0.5 for sound best-first).
- Whether conflicts are minimal (the Greiner bug).

**Interventions that worked:**
- Keeping state across probes (DynamicHS, K08).
- Linear-space best-first search (RBF-HS).
- Batching conflicts (MergeXplain), only where many exist.
- Splitting candidates by code-counted group sizes for LLM question asking (UoT).
- Up to three independent re-checks of the leading suspect (AgentLocate, 35.71% to 69.05%; small test, Qwen-7B).
- Structural change (a richer inter-agent protocol with code and execution output) cut communication pitfalls by up to 15 points (c17).
- Retrieval tools in a ReAct agent cut hallucination from 12% to 4% (c14).

**Interventions that did not work:**
- Domain knowledge in the prompt for conflict generation (c04).
- Hypothesis-driven prompts: wider coverage, no drop in interpretation errors. Pitfall-aware prompts: no meaningful gain (c17).
- Adding discussion threads as inputs: no significant gain (c14).
- 5 or 7 evaluators instead of 3: no consistent gain (d02).
- Scope guidance in fault localisation did not generally beat judging the whole trace (b27, snippet only).
- A correct incidence matrix as input: no change to MSO results (c04).
- Replay-based counterfactual testing: unstable for agents, because changing one step changes later prompts (d18; AgenTracer 45.24% vs AgentLocate 69.05%).

## 6. Language models

**Direct evidence about the hitting-set pipeline (one paper).** Sztyber-Betley et al. (DX 2025):
- Setting: 23 Boolean/arithmetic circuits; three steps (generate MSOs, evaluate them to get conflicts, generate minimal diagnoses). Each step was fed the gold output of the previous step, so step accuracy is measured in isolation (c01). The hitting-set algorithm was given in the prompt as pseudo-code plus a worked example (b20).
- Results: o3-mini F1 0.917 +/- 0.249 on conflicts and 0.784 +/- 0.322 on diagnoses. o1 was best on conflicts and MSOs, o3-mini best on diagnoses. Diagnosis generation was the heaviest step and fell clearly as relations and diagnoses grew (examples up to 165 diagnoses).
- Non-reasoning gpt-4o and gpt-4o-mini: accuracy close to zero on unseen examples without a code interpreter. gpt-4o-mini with an interpreter was the worst model of all. That is not a clean tool test, because the model was also the weakest (d07).
- Conflict scores rose with complexity only because zero-conflict cases scored badly. Models invent conflicts when none exist (c03). Check our scorer's empty-set convention (K16).
- Cost: about 30 USD per o1 iteration.
- Authors' conclusion: LLMs "do not provide an alternative to diagnosis algorithms". They point to hybrid frameworks and tool use (d09).
- Limits: tiny hand-built circuits, OpenAI models only, gold inputs per step, no equal-token comparison.

**Plain diagnosis from text (Plank and Wotawa, DX 2026).** No hitting-set method, and the prompt did not ask for subset-minimal diagnoses (a17). 13 models, 7 systems. Best hit rate 79.5% (Gemini 2.5 Flash). Hallucination 20.5% for the best; most small models above 70%. Scoring was manual by the authors with their own weights (correctness 30%, reasoning 20%, hallucination 20%, completeness 15%, uncertainty 10%, clarity 5%). Free models only. Top uncertainty credit goes to answers that admit several fault candidates (b22). The authors note one April 2026 ChatGPT chat gave only correct diagnoses on a classic circuit (a20; one conversation, no count).

**Conflict-side weakness.** LLMs label nearly every formula satisfiable and miss the phase transition (b23). That suggests missed contradictions in an agent's own conflict step. Reasoning models do much better.

**Agents on real faults.**
- OpenRCA: 11.34% best. 1675 runs gave 3.9% to 12.5% perfect. Failures were shared across models, so the cause is the framework (c15, c16).
- Symptom-as-cause in 39.9% of runs (above 45% for GPT-5 mini and GPT-OSS 120B).
- Anchoring, repetition and failure to update belief predict wrong answers (d13). The authors suggest early hypothesis diversification.
- RCA studies assume or mostly use one fault. D-Bot says multi-cause is hard (d14, qualitative).

**What changed LLM behaviour, by how much.**
- Reasoning vs non-reasoning models: near zero to F1 0.78 on diagnoses (c01, c04).
- Code-counted entropy plus LLM-simulated branches: +38.1% over direct prompting (d10).
- Three independent evaluators of one suspect: 35.71% to 69.05% (d02).
- Repeated-run spectrum counting in code: action-level 29.35%, above the best LLM method (about 19.7% in claim K25; read from the Famas paper by the research agent). Still below 30% (d03, d04).
- Retrieval tools: hallucination 12% to 4% (c14).
- Prompt-only fixes: no change (c04, c17).

**Hybrids.** Delta1-LLM builds minimal unsatisfiable sets by construction and uses the LLM only to extract predicates and explain. Case studies only, no accuracy table read (d05). SafeMin (LLM plus SMT for MUSes; snippet claims 42.1% more non-unique MUSes) is unverified (c25, d16). HyMUSE is a learned hypergraph agent, not an LLM (d06).

**Not found:** any LLM inside an HS-tree or HS-DAG; any measurement of how often LLM-written conflicts are non-minimal; any test of reopening pruned suspects; any carried-vs-restated suspect list test; any size-cap test (K21, K26, K28, d15, d17). Search was rate limited, so these are gaps, not proof of absence.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = SCHEMA section 5. Status: [E] established, [S] single source, [C] contested. "Established" here means the diagnosis theory is established, not that an LLM gain is. Per G7, every item must pay for itself at equal tokens before it enters SCHEMA.md; section 8 gives the tests.

### Add now (established)

These are cheap and code-side. Code does the work, so they cannot add model error. They are the only items backed by two or more sources.

1. **A suspect set is valid only if it touches every contradiction found so far and no proper subset does.** Code checks any suspect set the model names. Part: S4 TEST / S7 SELECT (code check). [E] K01. Evidence a01, a02, b03, c06.
2. **Minimise the contradiction list in code before using it:** drop any contradiction that is a superset of another. This removes the trigger of the Greiner bug. Part: S4 TEST / code. [E] for the mechanism (K02, K03); evidence b01, b02, a03, b10. Caveat: that LLM contradictions are often non-minimal is inference, not measured (critique gap 2).
3. **Cap suspect-set size** (singles first, then pairs, then triples) as a budget rule. Part: G12 / S5. [E] K07 for explosion and the cap in tree search; the effect on LLM accuracy is open (K28). Evidence a06, a07, b04, b14.
4. **Do set arithmetic in code** (hits, supersets, group sizes, entropy). The LLM supplies contradictions and simulated answers; code does the counting. Part: G5. [E] for G5 itself (F08, F05, F10); [S] for this instance (K27, d10-d12).

### Test first

1. **Reopen pruned suspects when a later contradiction is smaller (HS-DAG rule as a guardrail).** Part: G, S5. [S] K02, K29 (indirect). Evidence b01, d13. No LLM measurement exists.
2. **Offload the exact minimal-hitting-set step to a code tool vs the LLM doing it in-context.** Part: O, S5. [S] K15, K22; open K26. Evidence d07, d08, d09.
3. **Carry and edit the suspect list across probes (DynamicHS idea) vs restate it each turn.** Part: memory. [S] K08, K09. Evidence a10, a11, b17. One group only.
4. **Size cap 1, 2, 3 for LLM agents.** Part: S5. Open K28. Evidence d13, d14.
5. **Probe choice: halve the suspects vs most-likely-first.** Part: O. [E] for ontology solvers (K14); [S] for LLMs (K27). Evidence c10, a25, d10-d12.
6. **Batch several independent contradictions per step vs one.** Part: O. [E] K12 for solvers; gain only when many conflicts exist. Evidence a13, b18.
7. **Independent re-checks of the leading suspect, capped at 3.** Part: G (verification budget); caution G4, since samples from one model are not independent. [S] K24. Evidence d02. Qwen-7B, small set.
8. **Count a suspect's appearance across passing and failing attempts in code instead of asking the LLM to judge.** Part: O. [S] K25. Evidence d03, d04.
9. **Conflict-then-hit vs guess-a-candidate-and-test.** Part: S3/S5. [E] for solvers (K13); no LLM data. Evidence a15, b11, d01, d03.
10. **Hidden-contradiction vs no-contradiction tasks, to measure the false "consistent" rate and the invented-conflict rate.** Part: S4 TEST. [S] K18. Evidence b23, c03.
11. **Top-k open suspects in context (RBF-HS analogue).** Part: G11/G12. [S] K10. Evidence b13, c08.
12. **Listed-component guard: every named suspect must be a listed component.** Part: G (code check). [S] K17 for the rates (hallucination 20.5% best model); the check itself is trivial. Evidence a17, b21. Also report hallucination separately from correctness (K20, c14).
13. **Per-suspect "symptom or cause?" tag.** Part: S5. The failure is [E] (K19, symptom-as-cause 39.9%); the remedy is untested. Evidence c16, c18.
14. **If suspects are weighted by numeric priors, keep each below 0.5 or rescale.** Part: S5. [S] K11. Evidence a12.

## 8. Concrete tests on our bench

All tests: both arms get the same total token cap (setup, tool calls and retries counted, per G7). Items are generated by code with known gold diagnoses, so scoring is exact. Log per run: tokens per state, whether any pruned suspect was revived, hallucinated components, and the scorer's empty-set convention (K16).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 (K02, K29) | Conflict lists where a late conflict is a subset of an earlier one, including {{a,b},{b,c},{a,c},{b,d},{b}} and {{a,b},{a},{b}}, shown in arrival order | A: plain "give all minimal diagnoses". B: same plus code minimisation of the conflict list and a rule "reopen suspects if a conflict shrinks" | Exact-match F1 against gold minimal hitting sets; count of valid sets dropped | B better on late-subset items; no difference when conflicts arrive minimal and in order. Size unknown for LLMs |
| T2 (K03) | Tasks where the agent writes its own contradictions from a small spec, with solver-checked gold | A: raw agent contradictions. B: contradictions shrunk by drop-one-and-recheck in code | Share of contradictions that are non-minimal (solver check); final diagnosis F1 | Gives the prevalence missing from the literature; B helps if prevalence is high |
| T3 (K15, K26, K22) | Generated conflict families with 3, 5 and 8 conflicts and up to 100+ minimal diagnoses | A: LLM does the hitting set in-context. B: LLM writes conflicts, code tool computes minimal hitting sets | Exact minimal-diagnosis F1 by number of diagnoses | B flat as diagnoses grow; A falls (DX 2025 shape) |
| T4 (K07, K28) | Tasks with 1, 2 and 3 simultaneous faults | A: no cap stated. B: stated cap k, widened in code only if no valid set is found | Recall of the true fault set; tokens wasted on non-minimal or oversize sets | B better per token on 1-fault items; possible loss on 3-fault items if the cap is too low |
| T5 (K08, K09) | Multi-probe sessions (5 to 10 probes), each probe prunes suspects | A: agent restates and recomputes the suspect list after each probe. B: code keeps the list, the LLM only edits it | Turns to correct fault; win rate (not only the mean, K09) | B faster by tokens; replicate before trusting the 52% figure |
| T6 (K14, K27) | Fault-finding with a probe budget of 5 to 8 | A: free probe choice. B: LLM simulates answers per probe, code picks the closest to a 50/50 split. C: most likely suspect first | Probes to resolution; success within budget | B and C beat A; B vs C unknown |
| T7 (K12) | Tasks with many independent contradictions vs exactly one | A: one contradiction per step. B: several per step | Tokens to first correct diagnosis | B wins when many conflicts exist; slight loss with one (solver numbers 5% to 11%) |
| T8 (K23, K24, K25) | Failed multi-step traces with a known culprit | A: one suspect, 1 check. B: one suspect, 3 independent checks. C: full suspect list plus code hitting set. D: count appearances across passing and failing attempts in code | Culprit accuracy at agent and step level | B above A, no gain beyond 3 checks; D above LLM judging; C unknown |
| T9 (K18) | Tasks with a hidden contradiction and tasks with none | Same agent on both seeded conditions | False "consistent" rate; false "conflict" rate | High false-consistent for non-reasoning models |
| T10 (K17, K19, K20) | Same diagnosis tasks | A: free naming. B: pick from a listed component set, with a per-suspect symptom-or-cause tag | Hallucinated components; symptom-as-cause rate; correctness | B lowers hallucination; correctness equal or higher |
| T11 (K10) | Long sessions with 20+ suspects | A: whole frontier in context. B: top-k only | Accuracy at fixed tokens | B equal accuracy at lower tokens |

## 9. What does not transfer, and why

- **Runtime numbers.** DynamicHS, RBF-HS, MergeXplain and the Pill benchmarks measure theorem-prover calls, memory and seconds on ontologies and circuits. Our cost is tokens and accuracy. The percentages (52%, 98%, 54%) say nothing about token savings.
- **Algorithm ranking (GDE, Boolean, HST, HS-DAG).** An agent does not run these at scale. If it uses a tool, any exact enumerator will do. The ranking matters only when choosing that tool (K04 to K06).
- **Exponential-space worries.** The agent's context window is the space. The top-k analogy is a hypothesis.
- **Soundness condition p below 0.5.** It applies only if the agent weights suspects by numeric priors, which LLMs do poorly. Code-side only.
- **Ontology-debugging gains.** Random fault probabilities, one lab, no replication. They may not carry to free-text tasks where components are fuzzy.
- **Conflict finders (QuickXplain).** They need a sound prover. An LLM is not one: it misses contradictions (K18) and invents them (c03). The conflict step is the weak link for our agent, so code-checking contradictions matters more than the tree.
- **Counterfactual drop-one-and-rerun.** It works for static circuits. It is unstable for agent traces, because later prompts and tool outcomes change (d18).
- **Single-fault RCA benchmarks.** They never exercise multi-suspect hitting sets (d13, d14).
- **Spectrum diagnosis (Famas).** It needs many repeated executions (d03), which is costly at equal tokens.
- **Entropy over numeric probabilities.** LLMs cannot compute entropy reliably. UoT works because code does it from simulated set sizes.
- **Gold-input pipeline results (DX 2025).** Each step had perfect inputs. Real chains compound errors.

## 10. Open questions

1. Does an LLM told to reopen pruned suspect sets on a smaller contradiction keep more valid minimal diagnoses? (critique gap 1)
2. How often are LLM-written contradictions non-minimal, and does minimising them help? (gap 2)
3. At equal tokens, code tool vs in-context hitting set: where does LLM accuracy break? (gap 3, K26)
4. Does a size cap improve end accuracy for LLM agents? (gap 4, K28)
5. Does carrying and editing the suspect list beat restating it, and does DynamicHS replicate outside its group? (gap 5)
6. The TU Delft thesis on scope-guided fault localisation was not found again (b27, snippet only). AgentLocate and Famas are closed: neither uses a hitting set (d01, d03).
7. Conflict-then-hit vs direct candidate generation for an LLM. The attribution papers skip conflict sets, which is weak indirect support for direct generation (K23).
8. Neuro-symbolic MUS enumeration plus hitting sets as an LLM verifier: not found. SafeMin 42.1% unverified (d16).
9. Which probe rule helps an LLM: entropy, split-in-half or most-probable-singleton? UoT used entropy only (d12 compares reward forms, not rules).
10. Does a solver-checked "is this contradiction real and minimal?" gate help more than any change to the search?
11. What newer reasoning models do here: the only LLM pipeline test used o1 and o3-mini in early 2025.
12. Could the Greiner failure appear in an LLM's own pruning, that is, does the model close a branch as "already covered" and then fail to reopen it?

## 11. Sources

Marked [V] opened (substantial text read in a research session) or [M] snippet or second-hand.

- [V] Reiter (1987), A theory of diagnosis from first principles, as restated in Wassermann (arXiv cs/0003051) https://arxiv.org/pdf/cs/0003051 (a01, a16). Original DOI https://doi.org/10.1016/0004-3702(87)90062-2 [M] (c19)
- [V] Greiner, Smith, Wilkerson (1989), A correction to the algorithm in Reiter's theory of diagnosis, https://www.cse.sc.edu/~mgv/csce580sp15/greinerCorrectionReiter.pdf (b01, b02). DOI https://doi.org/10.1016/0004-3702(89)90008-8 [M] (c20)
- [V] Pill, Quaritsch, Wotawa (2016), On the practical performance of minimal hitting set algorithms from the diagnosis domain (IJPHM), https://papers.phmsociety.org/index.php/ijphm/article/download/2363/1336 (a02, a04, a05, a08, a22-a24, b07-b10)
- [V] Gainer-Dewar and Vera-Licona (2016), The minimal hitting set generation problem: algorithms and computation, https://arxiv.org/pdf/1601.02939 (a03, a06, a07, b04, b06)
- [M] Wotawa (2001), A variant of Reiter's hitting-set algorithm, Information Processing Letters (a05, b05; via Pill 2016 and the survey; 403 on direct access)
- [M] Pill, Quaritsch, Wotawa (2011), From conflicts to diagnoses (DX'11), cited in https://web-ainf.aau.at/pub/jannach/files/Conference_IJCAI_2015.pdf (a09)
- [V] Rodler (2019), Towards optimizing Reiter's HS-Tree for sequential diagnosis, https://arxiv.org/pdf/1907.12130 (a10, a24, b15)
- [V] Rodler (2020/2021), DynamicHS: streamlining Reiter's hitting-set tree for sequential diagnosis, https://arxiv.org/pdf/2012.11078 (a11, a12, a25, b16, b17)
- [V] Rodler (2022), Sound, complete, linear-space, best-first diagnosis search (RBF-HS), https://arxiv.org/pdf/2009.12190 (b13, b14)
- [V] Rodler (2023), Don't Treat the Symptom, Find the Cause! (thesis), https://arxiv.org/pdf/2306.12850 (c06-c09)
- [V] Shchekotykhin, Jannach, Schmitz (2015), MergeXplain, https://web-ainf.aau.at/pub/jannach/files/Conference_IJCAI_2015.pdf (a13, b18)
- [V] Felfernig, Schubert, Zehentner (2012), An efficient diagnosis algorithm for inconsistent constraint sets (FastDiag), https://arxiv.org/pdf/2102.09005 (a14)
- [V] Shchekotykhin, Fleiss, Rodler, Friedrich (2012), Direct computation of diagnoses for ontology debugging, https://arxiv.org/pdf/1209.0997 (a15, c11)
- [V] Shchekotykhin, Friedrich, Fleiss, Rodler (2011/2014), Interactive ontology debugging: two query strategies, https://arxiv.org/pdf/1107.4303 (c10)
- [V] Metodi, Stern, Kalech, Codish (2014), A novel SAT-based approach to model based diagnosis (JAIR), https://jair.org/index.php/jair/article/download/10911/26016 (b11, b12)
- [V] Wassermann (2000), Local diagnosis, https://arxiv.org/pdf/cs/0003051 (a16)
- [V] Sztyber-Betley et al. (2025), Are diagnostic concepts within the reach of LLMs? (DX 2025), https://drops.dagstuhl.de/storage/01oasics/oasics-vol136-dx2025/OASIcs.DX.2025.2 (a18, a19, b19, b20, c01-c05, d07-d09)
- [V] Plank and Wotawa (2026), Using SLMs and LLMs for diagnosis (DX 2026), https://drops.dagstuhl.de/storage/01oasics/oasics-vol148-dx2026/OASIcs.DX.2026.1 (a17, a20, a26, b21, b22)
- [V] Zhang, Chen, Chen (2026), Satisfiability solving with LLMs: a matched-pair evaluation, https://arxiv.org/pdf/2605.28602 (b23)
- [V] Xu, Liu et al. (2026), Delta1 with LLM, https://arxiv.org/pdf/2603.12953 (b24, c26, d05; first pages only)
- [V] Ijima and Yawata (2026), HyMUSE, https://arxiv.org/pdf/2604.09001 (d06; exact counts not extracted)
- [V] Roy et al. (2024), Exploring LLM-based agents for root cause analysis, https://arxiv.org/pdf/2403.04123 (c14)
- [V] Xu et al. (2025), OpenRCA (ICLR 2025), https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c (c15)
- [V] Kim, Park, Yun, Lee (2026), Why do AI agents systematically fail at cloud root cause analysis, https://arxiv.org/pdf/2602.09937 (c16, c17)
- [V] Fang et al. (2026), OpenRCA 2.0, https://arxiv.org/pdf/2606.27154 (c18; the 76.0% figure came from a search summary and is not used)
- [V] Riddell et al. (2026), Stalled, biased, and confused, https://arxiv.org/pdf/2601.22208 (d13)
- [V] Zhou et al. (2023), D-Bot, https://arxiv.org/pdf/2312.01454 (d14)
- [V] Xia et al. (2026), AgentLocate: Who broke the system?, https://arxiv.org/pdf/2607.07989 (d01, d02, d18)
- [V] Ge et al. (2025), Famas: Who is introducing the failure?, https://arxiv.org/pdf/2509.13782 (d03, d04)
- [V] Hu et al. (2024), Uncertainty of Thoughts, https://arxiv.org/pdf/2402.03271 (d10-d12)
- [V] Ielo, Mazzotta, Penaloza, Ricca (2024), Enumerating minimal unsatisfiable cores of LTLf, https://arxiv.org/pdf/2409.09485 (c12)
- [V] Paul, Yu, Dekker, Ignatiev, Stuckey (2024), Formal explanations for neuro-symbolic AI, https://arxiv.org/pdf/2410.14219 (c13)
- [M] de Kleer and Williams (1987), Diagnosing multiple faults (GDE), https://doi.org/10.1016/0004-3702(87)90063-4 (c21; also reported in a24)
- [M] Stern, Puzis, Felner et al. (2012), Exploring the duality in conflict-directed model-based diagnosis, https://ojs.aaai.org/index.php/AAAI/article/view/8231 (c22)
- [M] Feldman, Provan, van Gemund (2010), SAFARI, https://research.ucc.ie/en/publications/computing-multiple-minimal-diagnoses/ (c23)
- [M] Abreu et al. (2010), SIR-M simultaneous debugging of software faults (c24)
- [M] SafeMin: Large language models for safe minimization (ICSE 2025), https://conf.researchr.org/details/icse-2025/icse-2025-research-track/205/ (c25; 42.1% figure unverified)
- [M] Grastien, Haslum, Thiebaux (2023), A more general theory of diagnosis from first principles, https://arxiv.org/pdf/2309.16180 (b25)
- [M] TU Delft thesis (2026), fault localization in LLM-based multi-agent systems, https://repository.tudelft.nl/record/uuid:871ed180-d4a9-4aef-b5bc-007cdf1ceac7 (b27)
- [M] AgentLocate search snippet, https://www.alphaxiv.org/abs/2607.07989 (b26; superseded by the opened arXiv text)
- Search notes (no source): a21, c27, d15, d16, d17 (negative searches; rate limits hit)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 8 established claims: 6 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C09.04-K03** (reworded: the sources support less). Greiner et al. say the pruning rule applies only when some conflict is a strict superset of another, and the loss occurs when a smaller conflict is found after a larger one was used to label a node; the claim states the direction backwards ('a superset of a conflict seen earlier'). The LLM-contradictions-are-non-minimal part is flagged as inference and is not in the sources. Corrected claim: The bug only bites when conflicts are non-minimal, i.e. when the conflict finder returns a conflict that is a proper subset of one already used to label a node (a smaller conflict arriving after a larger one); whether LLM-produced contradictions are often non-minimal is an unmeasured inference.
- **C09.04-K14** (reworded: the sources support less). Sources show ENT, SPL and MPS (most probable singleton) perform comparably (median savings 50/52/52%, not significantly different), so entropy/split are not shown to work 'best'; the 50/52/52% figures are DynamicHS runtime savings over HS-Tree, not a comparison among selection rules. Corrected claim: In sequential diagnosis, queries chosen by entropy, split-in-half or most-probable-singleton heuristics all narrow diagnoses and gave similar DynamicHS median runtime savings over HS-Tree (50/52/52%); in ontology debugging, entropy-based query selection needed significantly fewer queries than split-in-half.
