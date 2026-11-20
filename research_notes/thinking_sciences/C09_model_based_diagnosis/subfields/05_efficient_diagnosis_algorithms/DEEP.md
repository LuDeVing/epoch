# Efficient diagnosis algorithms: deep document

*Subfield C09.05 of model-based diagnosis. Evidence: evidence_a-d.jsonl (ids a01-a29, b01-b28, c01-c27, d01-d17), claims.jsonl (K01-K24), critique.md. Relevance to our agent: background only, with a few small transfer ideas. Almost every number comes from one author (Rodler) on one benchmark family (faulty ontologies, Pellet reasoner). No independent replication was found. Read every "established" mark with that in mind.*

## 1. What it is

Model-based diagnosis (MBD) takes a model of how a system should behave and an observation that contradicts it. It asks which components could be broken. A diagnosis is a minimal set of components whose removal (or repair) makes model and observation consistent.

Reiter (1987) showed how to compute diagnoses. First, find conflicts: sets of components that cannot all work. Then take minimal hitting sets of the conflicts. A hitting set contains at least one element from every conflict. Reiter's HS-Tree builds these sets as a search tree. Greiner et al. (1989) repaired it as HS-DAG. The founding paper had about 4,500 Google Scholar citations by December 2022 (a27).

This subfield is about making that computation efficient. Four problems drive it:

1. **Memory.** A best-first HS-Tree must store every open node. For large ontologies that is millions of nodes and the run dies out of memory (32 GB in several cases, b07).
2. **Time per reasoner call.** A consistency check with a description-logic reasoner can take seconds to minutes. Every algorithm trick aims to save checks.
3. **Many conflicts.** For ontology alignments, conflicts are too many to compute first. Direct methods skip them.
4. **Sequential diagnosis.** After the first set of diagnoses, the debugger asks a query or measurement, gets an answer, and must update. Rebuilding the tree each time is wasteful.

The task brief names "RBFR-HS" and "Jannach et al., IJCAI 2023". Both are slips. The algorithm is RBF-HS (Recursive Best-First Hitting Set Search). The IJCAI 2023 item is Rodler's extended abstract of that paper, not a Jannach paper (b07, critique correction 4).

Why it matters for our agent: an LLM agent rarely lists more than 100 suspects, so exact large-scale enumeration seldom bites. What transfers is a set of design ideas (bounded search state, reuse of state across probes, direct localisation, choice of next probe) and one new LLM line of work (QXR, a 2026 preprint) that runs QuickXplain plus a hitting set with an LLM as the consistency oracle.

## 2. History and theories in depth

**Reiter (1987), "A theory of diagnosis from first principles".** Diagnoses are minimal hitting sets of minimal conflicts. HS-Tree expands nodes labelled with conflicts, pruning supersets and duplicates. Reiter also asked whether the tree built for old diagnoses could be reused after a new measurement (a10, a14). That question stayed open for about 30 years.

**Junker (2004), QuickXplain.** A divide-and-conquer method that finds one minimal conflict in a number of consistency checks that is linear in the conflict size times the log of the input size. It needs a monotone property: if a set is inconsistent, every superset is. It sits inside most conflict-based diagnosers (a26, c21). Rodler (2020) wrote a plain explanation; his thesis notes a study found people still find it hard to understand.

**Direct computation (Shchekotykhin, Fleiss, Rodler, Friedrich 2012; Felfernig et al. FastDiag).** Skip conflicts. Inv-QuickXplain does divide and conquer directly over the set of components to find one diagnosis. Cost is about log2(n/k)+2k checks for a diagnosis of size k (b12, b13, a25). Footnote in MergeXplain: direct encodings such as MaxSAT usually beat HS-Tree when only one diagnosis is wanted; HS-Tree wins when several diagnoses and a black-box reasoner are needed (b16).

**Speed-ups within the HS-Tree family (2015-2017).**
- MergeXplain (Shchekotykhin, Jannach, Schmitz 2015): find several conflicts per call by divide and merge (b10).
- Parallel HS-Tree (Jannach, Schmitz, Shchekotykhin): expand tree nodes on a thread pool (b11).
- Implicit hitting sets for many failing observations (Ignatiev, Morgado, Marques-Silva 2017): alternate between a minimal hitting set solver and a consistency oracle, never storing the tree (b14).
- Related work grouped in b15: exploit structure (hierarchy, distribution), parallelise, solve the dual problem, or approximate with stochastic or greedy search.

**Sequential diagnosis and query selection.** Diagnosis is a loop: compute leading diagnoses, pick the most informative next query or measurement, observe, prune, repeat. Rodler's thesis (2023, a17-a20) and the sampling paper (Rodler and Elichanova, a15, a16) study how to choose queries, how the sample of diagnoses biases the choice, and how to synthesise queries without a pool.

**RBF-HS (Rodler, AIJ 2022; DX short version 2020; IJCAI-23 extended abstract).** Adapts Korf's Recursive Best-First Search to the hitting set tree. It keeps only the current path and a few bookkeeping values, so memory is linear. It returns the same diagnoses in the same best-first order as HS-Tree (b01, b23). A hybrid, HBF-HS, runs HS-Tree first, then switches to RBF-HS when a memory budget is hit (a02).

**DynamicHS (Rodler 2019 workshop, 2020-22 journal).** The tree is kept across the whole sequential session, with lazy updates and cheaper set operations that replace costly reasoner calls (a10-a14). It answers Reiter's 1987 question.

**Taxonomy (Rodler 2022/2024, a23, a24).** Twelve features classify diagnosis computation algorithms: soundness, completeness, best-first, multiple solutions, conflict computation, stateful or stateless, black-box reasoning, general applicability, space efficiency, and others. Only few space-efficient strategies exist. Dropping soundness, completeness or best-first speeds things up but risks non-minimal outputs or missing the true fault. The paper is qualitative.

**2025-2026 neighbours.**
- Conflict extraction by constraint propagation (G-CSEA, c22): conflict set 94.11% smaller than the original constraint set; with QuickXplain about 40% less minimal-conflict computation time than QuickXplain alone.
- Hitting sets inside LLM agents: QXR (He et al. 2026, b18) and a security paper that certifies actions with a minimum hitting set over evidence dependency sets (Pandey et al. 2026, c24, c25).
- A symbolic generator for minimal unsatisfiable sets with an LLM only verbalising the result (Xu et al. 2026, c23).
- Runtime verification framework that encodes diagnosis as stream specifications (Hipler, Leucker, Rodler 2026, a28, c26).
- A 2026 compression method for minimal hitting set enumeration by an independent group that cites RBF-HS (Lu et al., d15; abstract only).

## 3. Core findings with exact numbers

Status: single = one author or group; established = at least two independent groups agree; human-only = no LLM test.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| RBF-HS gives same diagnoses, same best-first order as HS-Tree, in linear space | Time O(n + TPT) for min-cardinality, O(n^2 + TPT) for most-probable; space O(\|K\|); needs a fixed number of diagnoses (2, 6, 10, 20; 100 for scalability) | a01, b23 (Rodler AIJ 2022) | single (formal proof) |
| Min-cardinality memory saving | Mean factor 14.1 (ENT) and 13.8 (SPL); under 8% of HS-Tree memory; factor over 10 in 45% of cases; max 50 / 57; 14 ontologies (42 to 33,203 axioms); 5 sessions per setting | a04, b01 | single |
| Positive space-time trade in min-cardinality | 94% of non-trivial cases (runtime over 1 s); 94-96% across scenarios | a04, b17 | single |
| RBF-HS sometimes faster despite forgetting | Lower time and big memory saving in 35% (ENT), 38% (SPL); worst overhead 10.4x (SPL, ontology O, ld=20) | a05, b02 | single |
| Most-probable-first: trade is about one to one | Median 3.75x less space vs 3.56x more time (73% memory saved, HS-Tree 72% faster); positive in 53% of cases; at ld=100 RBF-HS took hours, HS-Tree minutes | a07, b03, b06 | single |
| Hybrid HBF-HS removes most time overhead | Switch at 400 nodes: median overhead 0% (ENT), 3% (SPL); faster than HS-Tree in 44% / 42% of overhead cases; memory capped at 416 nodes vs over 500,000 | a02, a06, b04 | single |
| Hardest cases (merged ontologies, many independent faults) | Space saved 84% to over 99.9% at ld=100 (min-card); ccc,SPL,6 over 4200x less memory and 15% less time; ccc,SPL,20 99.9% memory and 65% time saved; HS-Tree out of 32 GB in several cases while RBF-HS never held more than 125 nodes in one | a08, b05, a17 | single |
| Boundary: all diagnoses of cardinality one | HS-Tree used slightly less memory in 5 scenarios (ontologies K, C) | b06 | single |
| Earlier short version (DX 2020) | 12 ontology problems (10 cases in an earlier cut): memory saved up to 98%; time saved up to over 88%; RBF-HS faster in 4 of 10 cases; overhead up to 4900% in worst cases | a09, b08, c09 | single (do not mix with the 14-ontology journal set) |
| IJCAI-23 abstract | Average / max memory saving 93% / 98%; lower time and space in 38% of cases; one case 85% runtime and 98% memory saved | b07 | single |
| DynamicHS (reuse tree across a session) | Faster than HS-Tree in 99.4% of scenarios and 96% of sessions; median saving 52%, max 75%; hardest cases median 64%, max 89%; 20 faulty ontologies, 20 sessions per scenario | a11, a12, b09 | single |
| DynamicHS cost | Memory under 2x HS-Tree in 82% of scenarios; less in 14%; under 25% overhead in 35%; no-win scenarios: median -2% and -3%; single sessions up to 86% worse | a13, b24 | single |
| Reasoner calls are the real cost | DynamicHS cut hard operations 57% and medium 44% (for some easy ones); hardest cases avoided median overhead over 175%, max over 800% | c13, a12 | single |
| Sample type for choosing next measurement | Random samples best or second best at estimating elimination rate in 100% of cases (best in 75%); best-first best or second best for probability in all but one case; sample size below 10: best-first | a15, a16, c14, c15 | single |
| Faster sampler is not the one needing fewest measurements | In all but one scenario a different sample type minimised time than minimised measurements | c15 | single |
| Heuristic choice and prior quality | Wrong heuristic costs avg 100%, max 250% extra oracle effort; misleading priors: random best; vague priors: MPS; reasonable priors: BME then entropy | a19 | single |
| Query synthesis | Above 99.999% of optimal query value in under 1 s, under 4% of query space; handled 80 diagnoses vs about 10 for pool-based within an hour | a18 | single |
| MergeXplain | DXC circuits, 5 diagnoses: avg gain 25% (full) and 37% (aggressive); c432 45% / 47%; up to 54% on CSP; random layout 20-30%, clustered up to 75%, some cells negative (-8%, -4%) | b10, b25 | single (group) |
| Parallel HS-Tree | 4 threads: speed-up 1.78 to 3.44 (over 70% less time), significant in 96 of 100 DXC scenarios; 8 threads up to 7.27 | b11, b26 | single (group) |
| Direct diagnosis vs conflict-based | OAEI 2011: 286 alignments, 146 faulty; both finished 133; 13 only the direct method; timings mixed (LogMap ENT 6.60 vs 13.41 s, Lily SPL 82.9 vs 115.2 s, GOMMA-bk 18.34 vs 14.47 s) | a25, b13, b27 | established in direction (3 sources) |
| FastDiag | About log2(n/k)+2k checks; bicycle configuration (34 variables); prediction RMSD 0.95 vs 0.97 best-first HSDAG vs 1.64 breadth-first | b12, b28 | single study; direction agrees with b16 |
| Implicit hitting sets, many observations | 1140 buggy-encoder instances: all solved, largest about 0.1 s; separate enumeration finished 177 (LBX) / 185 (RS) | b14 | single |
| Randomised approximation | Random QuickXplain diagnoses: better in under half the time of a solver in scheduling (25% avg, 60% max fewer cancelled orders); abstract spreadsheet models 1 to over 4 orders faster, exact accuracy in a third of cases | a21, a22 | single |
| Human study: query-based debugging | Manual approach: 37% more time, 117% more clicks, no loss in effectiveness. Second study, 29 students: 77% of 5 injected faults found; 10 of 29 (34.4%) found the full true diagnosis; 10 of 14 with the true diagnosis ranked high kept going | a20, c18, c19 | single (human) |
| LLM as noisy oracle in QuickXplain plus greedy hitting set (QXR) | VitaminC recall direct to QXR: Sonnet 4.5 0.617 to 0.957; Opus 4.6 0.574 to 0.968; Mistral Large 2 0.603 to 0.978; DeepSeek-R1 0.730 to 0.990; Sonnet 3.7 0.854 to 0.975. F1: Opus 4.6 0.611 to 0.976; Sonnet 4.5 0.762 to 0.966 | b18, c02, c03 | single preprint |
| Prompt variants do not fix over-pruning | Recall: zero-shot Sonnet 3.7 .681, CoT .684, decomposition .626, few-shot .658, self-consistency prompt .547; GPT-OSS-120B .876 to .475 with self-consistency; QXR .975 to .995 | c04, d03 | single |
| RAG evidence (RAMDocs, N=30, 10 gold conflicts) | Qwen2.5 32B F1 .845 to .920 (R .839 to .998); Haiku 4.5 .724 to .863; Qwen2.5 7B .741 to .815; Sonnet 4.5 .882 to .870 (slightly lower) | b19, c05 | single |
| QXR cost | Bound O(I*m*(1+k log N)); pairwise baseline would need 435 calls (N=30), 4,950 (N=100); no measured QXR call or token counts | c06, d04 | single (corrected from b20) |
| Greedy vs exact hitting set in agent debugging | Identical supports in 12/12 dev cases; identical planted-fault recovery 9/12; exact-anchor predicates 9/9, after removing anchors 8/9 | b22 | single (small) |
| Error localisation in reasoning chains (indirect) | GPT-4 52.87 on BIG-Bench Mistake; o1-mini 87.9 vs GPT-4o 61.9 average F1 on ProcessBench (3,400 cases); backtracking still helps near 65% location accuracy | d06, d07 | established (2 benchmarks) |
| LLM verbal confidence is poor for ranking | GPT-4 average AUROC 62.7% (random 50%); values mostly 80-100%; GPT-3/3.5/Vicuna ECE above 0.377; verbal beats token probability by over 50% relative ECE | d08, d09, d10 | established (3 sources) |
| Sampling at scale needs a verifier | SWE-bench Lite 15.9% (1 sample) to 56% (250 samples); vote systems can peak then fall as calls grow | d11, d12 | established |
| Long lists: position effect | GPT-3.5-Turbo with answer in the middle of 20 documents fell below its 56.1% closed-book score | d13 | established (indirect) |
| No LLM test of RBF-HS or DynamicHS | 0 found; Semantic Scholar shows 4 citers of RBF-HS, none opened as a replication; 17 Rodler diagnosis papers 2010-2026, none with LLMs in the title | a29, c17, c27, d14 | negative search, weak |

## 4. Mechanisms and models

### 4.1 Reiter's HS-Tree (the baseline)
Inputs: a model, an observation, a conflict finder (QuickXplain or a reasoner explanation).
1. Call the conflict finder on the full set. If no conflict, the empty set is the only diagnosis.
2. Make a root node labelled with a conflict. For each element e of the label, make a child with path {e}.
3. For each node, check pruning rules: skip a path that is a superset of a known diagnosis; skip duplicates.
4. For a surviving node, ask the consistency check on the model with the path's components removed. If consistent, the path is a diagnosis. If not, get a new conflict (reuse an old one if it is disjoint from the path) and expand.
5. Expand nodes in order of a preference (fewest elements, or highest fault probability). Keep an open list sorted by that preference.

Cost problem: the open list grows exponentially. Best-first guarantees diagnoses arrive in order, so you can stop after ld of them.

### 4.2 RBF-HS (bounded memory, same output)
Idea from Korf's RBFS. Recursion keeps only the current path and, at each level, the best alternative's f-value.
1. Define f(node) = preference value of the path (cardinality or probability bound).
2. Recurse into the best child. Pass down a limit: f of the best alternative sibling so far.
3. When the child's f exceeds the limit, return its new f to the parent and forget its subtree (this is the "mind shift").
4. On return, the parent updates the stored f of that child, then picks the new best.
5. Stop when ld diagnoses are found.

Cost: forgotten subtrees must be re-expanded. With min-cardinality, f-values step by whole numbers, so few mind shifts. With most-probable-first, f-values differ slightly, so mind shifts are frequent and re-expansion is heavy (a07, b03). That is the whole reason for the 53% vs 94% split.

### 4.3 HBF-HS (hybrid)
Run HS-Tree until a budget is reached: an absolute node count (400 tested) or a relative share (60% of available memory). Then hand the tree to RBF-HS. Time stays near HS-Tree on easy cases; memory is capped (416 nodes max vs over 500,000). Worst-case bounds equal the worse of the two parents.

### 4.4 DynamicHS (state across a sequential session)
After each answered query the set of valid diagnoses changes. Standard practice builds a new tree. DynamicHS keeps the tree and:
1. Marks nodes invalidated by the new answer instead of deleting them.
2. Updates lazily when a node is needed.
3. Replaces hard reasoner calls with cheaper set operations (subset checks against stored conflicts and diagnoses).
Result: median 52% less time; costs up to 2x memory in 82% of scenarios.

### 4.5 Direct diagnosis (FastDiag, Inv-QuickXplain)
Divide and conquer over the component set to find one minimal diagnosis directly.
1. Split the constraint list in two halves A and B.
2. If B alone, once removed from consideration, restores consistency, the diagnosis lies inside B; recurse on B.
3. Otherwise some of A is needed; recurse on A with the part of B already fixed.
4. Result: one minimal diagnosis in about log2(n/k)+2k checks.
Inv-HS-Tree runs this n times for several diagnoses.

### 4.6 Implicit hitting sets (many observations)
Alternate between two solvers. A hitting set solver proposes a minimal candidate. A consistency oracle checks it against all observations. If inconsistent, the oracle returns a new conflict (a core). Add it, propose again. The tree is never built, and the aggregated formula over all observations never gets big (b14).

### 4.7 Choosing the next probe
1. Take a sample of leading diagnoses (best-first, random, worst-first, or approximate versions).
2. For each candidate query, partition the sample by the answer it would produce.
3. Score the query: entropy, split-in-half, or minimum probability of survival.
4. Ask the best query.
Pick sample and heuristic by prior quality: bad priors, random probing; vague, MPS; good, BME or entropy (a19). Query synthesis builds the best query by search over the query space rather than scoring a list (a18).

### 4.8 QXR: LLM as the consistency oracle (He et al. 2026)
Setting: a set F of about 30 claims, an LLM that answers "are these claims jointly consistent?" (oracle, temperature 0, one call per query).
1. Ask the oracle about the whole set. If consistent, stop.
2. Run QuickXplain with the oracle to find one minimal inconsistent subset (MUS). Cost O(k log N) calls per MUS.
3. Record the MUS. Remove one claim of it (or ask again on the set minus a greedy hitting set candidate), repeat to find the next MUS.
4. Delete a greedy hitting set of all discovered MUSes. The remainder is consistent when the oracle is monotone and correct.
Greedy hitting set has the standard log-factor approximation guarantee (Lemma A.1). A crossing conflict breaks naive independent halves (b21). Weighted hitting set and graded oracle (p_incons, abstain, re-query near threshold) are proposed but untested (d02).

## 5. What holds up

**Holds up well (formal or multi-source).**
- Soundness, completeness and best-first order of RBF-HS and HBF-HS are proved, not measured (b23).
- Direct computation is needed when conflicts are many or hard to get. Three sources agree in direction: Shchekotykhin 2012 (13 of 146 alignments only solvable directly), MergeXplain footnote, FastDiag (a25, b12, b16). Timings between direct and conflict-based methods are mixed, so "needed on hard cases" is established, "faster in general" is not (b27).
- Per-case error localisation in LLM reasoning is weak but correctable (d06, d07).
- LLM verbal confidence is poorly calibrated (d08, d09, d10), which blocks using LLM-given fault priors for best-first or entropy heuristics.

**Single-source, large effects.**
- RBF-HS memory factor and DynamicHS time saving. All from Rodler, one benchmark family, Pellet reasoner, wall-clock time. No independent replication found (critique). Treat as strong but unconfirmed.
- QXR recall gains. One preprint, one oracle call per query, temperature 0, claim sets of about 30, no repeats.

**Failures, boundary conditions and tensions.**
- The same algorithm, opposite verdicts: min-cardinality saves memory at positive trade in 94% of cases; most-probable-first only 53%, with hours vs minutes at ld=100 (b17). "RBF-HS saves 14x memory" is a min-cardinality claim only.
- Memory factor 14.1 is from the 5-session main test; the "avg 18, max 158" in b03 is from an appendix single-run test. Do not quote 158 as the headline (critique correction 3).
- When every diagnosis has cardinality one, trees are tiny and HS-Tree can use less memory (b06).
- DynamicHS wins on time but costs memory; RBF-HS wins on memory but can cost time. They were not compared head to head (critique).
- MergeXplain gains depend on conflict position: 20-30% random, up to 75% clustered, negative in some cells (b25). Parallel speed-up grows with check time and conflict size; falls with more components (b26).
- Sample choice: larger samples improve statistical representativeness but gave no general practical gain in the number of measurements; in some MPS cases more diagnoses meant more measurements (c14).
- Priors drive heuristic choice. A wrong heuristic costs up to 250% extra effort (a19).
- Humans: in the 29-student study only 34.4% found the full true diagnosis, and 10 of 14 ignored a stop instruction even when the true diagnosis was ranked high (c18, c19). A good ranker does not make the user stop.
- QXR: Sonnet 4.5 F1 fell slightly on RAMDocs (.882 to .870) while rising on VitaminC. Gains are model- and dataset-dependent; on FEVER gains were small because direct judging already works (c03, c05).
- Self-consistency prompt lowered recall for 5 of 5 judges (d03). Budgets were not matched to QXR, so this is not an equal-token test.
- A better solver adds nothing when the verifier already encodes the answer: exact and greedy hitting set identical (b22, small study).

**Interventions that worked:** keep state across probes (DynamicHS); cap memory with a hybrid (HBF-HS); direct localisation when conflicts are many; joint treatment of all observations (IHS); localise-then-delete with an LLM oracle on claim sets (QXR).

**Did not work or did not help:** stronger direct prompts (CoT, decomposition, few-shot, self-consistency) for over-pruning; exact hitting set over greedy in the one agent study; larger samples for measurement count.

## 6. Language models

Direct LLM tests of this subfield's algorithms: none. No study tests RBF-HS, DynamicHS or MergeXplain with an LLM (a29, c17, c27, d14-d17). The search was weak because APIs were rate limited, so the negative is soft. The checked parts: Rodler's thesis has 0 hits for LLM or GPT (c17); of 17 Rodler papers on arXiv none has LLMs in the title (c27).

Nearest tests, in order of relevance:

1. **QXR (He, Kirschbaum, Kasiviswanathan 2026; b18-b21, c01-c07, d01-d05).** Seven judges: Sonnet 3.7, Sonnet 4, Sonnet 4.5, Opus 4.6, DeepSeek-R1, GPT-OSS-120B, Mistral Large 2. Three benchmarks of claim sets: VitaminC (24-32 claims, 2-6 injected contradictions), FEVER, RAMDocs (N=30, 10 gold conflicts).
   - Direct all-at-once judging has high precision and low recall: it detects trouble, then deletes too much. Recall of valid claims on VitaminC: Sonnet 4.5 0.617, Opus 4.6 0.574, Mistral Large 2 0.603.
   - QXR lifts recall to 0.957, 0.968, 0.978. F1 for Opus 4.6 goes 0.611 to 0.976.
   - Stronger prompts on the direct baseline do not help: recall .547 to .684 for Sonnet 3.7 variants.
   - Weaker or cheaper models gain most on RAG evidence (Qwen2.5 32B recall .839 to .998; Haiku 4.5 F1 .724 to .863). Sonnet 4.5 F1 fell slightly (.882 to .870).
   - Limits: temperature 0, one call per query, no repeats, no noise test, no call or token counts, only claim sets. The cost is many more calls, so equal-token comparison against best-of-N or voting is missing (K20). Sampling literature says verifier-free voting plateaus and can even decline with more calls (d11, d12).
2. **Error localisation in chains (d06, d07).** Models find the first wrong step poorly (GPT-4 52.87 on BIG-Bench Mistake across 5 tasks, 300 traces per task, 85% wrong traces) but fix it well when told where. On ProcessBench (3,400 cases) o1-mini scores 87.9 average F1 and GPT-4o 61.9. Backtracking helps even at about 65% location accuracy. This is the closest test of a "localise by bisection" idea, but bisection itself was not tested there.
3. **Confidence (d08-d10).** Verbalised confidence is overconfident; GPT-4 AUROC 62.7% across 8 tasks. Verbal probabilities beat token probabilities (over 50% relative ECE reduction). An agent cannot supply calibrated fault priors; entropy and best-first heuristics would run on bad priors, where random probing was best (a19).
4. **Hitting sets in agent loops.** Pandey et al. (c24, c25): a minimum hitting set over evidence dependency sets stops copies of one source faking agreement. Five models, 80 episodes each (54 with an injection, 26 clean): injection followed in 100% for several models. Sanctions list: 70,966 entities, about three quarters rest on one domain. Zhu and Chang (b22): exact and greedy hitting set identical in a small agent-debugging study.
5. **Context (d13).** Position effects on long lists (GPT-3.5-Turbo below closed-book 56.1% when the answer is mid-context of 20 documents). Indirect support for bounded suspect lists.

What changed LLM behaviour on these tasks: replacing one global judgment with a search of small judgments plus a code-run hitting set (large recall gain); lower model tier (bigger gain); dataset where direct judging is already strong (smaller gain). Prompt tricks did not change over-pruning.

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| Item | Schema part | Mark | Evidence |
|---|---|---|---|
| Do not use LLM-stated fault probabilities as priors for entropy or best-first probing. Rank suspects with code-checked evidence; where no prior exists, probe at random or by cheapest check. | G5 (code selects) / S3 ranking | [E] | d08, d09, d10, a19 (K23) |
| For a one-fault task, localise directly with a divide-and-conquer probe (check half the suspects at once). For several faults, use conflict plus hitting set. Use direct localisation when conflicts are hard to compute. | O (localise fault) | [E] on direction; timings mixed | a25, b12, b13, b16, b27 (K08) |
| Locating a fault in a reasoning chain is weak; always revise from the located real output, and do not trust the model's "first error" claim without a check. Already G2/G10; this adds a number. | G2, G10 | [E] | d06, d07 |

Nothing else from this subfield meets the established bar. The rest is single-source.

### Test first

| Item | Schema part | Mark | Evidence |
|---|---|---|---|
| Localise-then-delete (QuickXplain with the model as a noisy consistency oracle, then a greedy hitting set in code) instead of one-shot "which claims are bad". | O (localise conflict) + S4 | [S] | b18, c02, c03, d01-d03 (K14, K15) |
| Keep the suspect set between observations (DynamicHS idea) instead of regenerating it each step; test with a window limit. | memory / S5 | [S] | a11, a12, b09, d13 (K05, K24) |
| Hybrid frontier: keep a full suspect list while it is short; when it passes a size or token cap, switch to a bounded top-k with re-expansion. | G (budget) / memory | [S] | a02, a06, b04 (K04, K24) |
| Joint diagnosis over all failing observations rather than one failure at a time. | S4 | [S] | b14 (K09) |
| Batch several independent consistency checks in one call (MergeXplain idea). | O (extract conflicts) | [S] | b10, b11 (K07) |
| Next-probe choice with random vs top-k candidate samples when the model proposes the candidates. | O (choose probe) | [S] | a15, a16, a19 (K10) |
| Let the agent write the discriminating probe directly instead of ranking a pre-listed pool. | O (probe design) | [S] | a18 (K11) |
| Apply localisation only to cheaper or weaker executors. | S0 gate / G12 | [S] | b19, c05 (K16) |
| Greedy hitting set before any exact solver. | S4 | [S] | b22 (K18) |
| Weighted hitting set and re-query near the boundary for a noisy oracle. | G / S6 | [S] | d02 (K21) |

## 8. Concrete tests on our bench

All arms at equal total tokens (count every call, including setup). Run each item with at least 3 seeds. Bench item types: claim-set repair (30 claims, 2-6 planted contradictions), faulty-program debugging with a test oracle, planted-error reasoning chains, ARC-style rule candidates with one planted bad example.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Claim sets, 30 claims, 2-6 planted contradictions (K14, K20) | A: one-shot "keep valid claims". B: QXR (QuickXplain + greedy hitting set, one call per query). C: best-of-N with a code verifier. D: majority vote. Each to the same token cap. | Recall of valid claims, F1, tokens | QXR recall above one-shot by 0.2 or more on mid-tier models; unknown versus C and D. Expect smaller gain on models strong at direct judging |
| T2 | Same claim sets, with oracle answers flipped at 5, 10, 20% (K21) | QXR plain; QXR with re-query near the boundary; QXR with weighted hitting set | Recall loss against the 0% case | Plain QXR loses more than 0.1 recall at 10% noise; re-query halves the loss |
| T3 | Wrong reasoning chains (planted first error), 10-40 steps (K22) | A: direct "find first wrong step". B: bisection with a model-judged consistency check on the prefix. C: code-run check where available | First-error accuracy; final fix rate | Bisection beats direct judging on long chains; no gain on short ones |
| T4 | Faulty-program debugging with 5-100 suspect functions (K24) | A: regenerate suspect list each probe. B: carry the list forward (DynamicHS idea). C: carry forward plus cap at top-k with a refresh | Probes to isolate the fault; rank of true fault; tokens | B saves tokens over A when the list is above 20; no gain under 10 suspects; C helps above 50 |
| T5 | Suspect-list length sweep 5, 10, 20, 50, 100 (K24) | Full list in context vs bounded top-k | Rank of true fault; position of true fault in list | Mid-list loss appears at 50 or more |
| T6 | Multi-failure tasks with 3 or more failing tests (K09) | A: diagnose each failure separately. B: joint diagnosis of all failures with a code-built hitting set | Fault found; tokens | B finds shared causes with fewer tokens when failures share a cause |
| T7 | One-fault tasks (K08) | A: conflict plus hitting set. B: direct divide-and-conquer probe | Probes to isolate; tokens | B uses about log2(n) checks, fewer than A when one fault |
| T8 | Probe choice with unknown priors (K10, K23) | A: random probe. B: model-ranked probe. C: model-stated probabilities then entropy. D: cheapest check first | Probes to isolation | C no better than A; D best when check costs differ |
| T9 | Batching of checks (K07) | One model call per check vs 3-5 checks per call | Accuracy of each check; tokens | Saves tokens; accuracy of each check drops when over about 5 per call |
| T10 | Greedy vs exact hitting set on agent-debugging cases (K18) | Greedy; exact | Fault recovery; time | Identical results on most items |

## 9. What does not transfer, and why

- **Memory factors and time factors.** They are tree nodes and reasoner seconds on ontologies of 42 to 33,203 axioms. An LLM agent lists tens of suspects, not millions of nodes. A 14x memory saving has no direct meaning for tokens.
- **RBF-HS proofs.** They need a sound and complete conflict finder and a fixed number ld of diagnoses (b23). An LLM oracle is neither sound nor complete.
- **QuickXplain guarantees.** They need a monotone, noise-free oracle. LLM judgments are noisy, prompt-sensitive and possibly non-monotone (c07, d02).
- **Wall-clock results.** Time depends on a Pellet reasoner call (seconds to minutes). LLM calls have different cost structure: cost scales with tokens and call count.
- **Priors.** Best-first and entropy heuristics need calibrated fault probabilities. LLMs do not give them (d08).
- **Parallel speed-ups.** Thread speed-ups (1.78-3.44x) are about CPU time; for LLMs the cost is tokens, which parallel calls do not reduce.
- **Ontology alignment scale.** The "hardest cases" came from merged ontologies with many independent faults. Agent tasks seldom look like that.
- **User-study results.** Human error in oracle answers (c18, c19) is a different failure from a model oracle's noise.
- **Exact enumeration of all minimal diagnoses.** An agent needs one good fix, not the full list (b22: exact solver added nothing).

## 10. Open questions

1. Does any independent group replicate RBF-HS or DynamicHS on circuits, software or configuration? Four citers are indexed; none was opened as a replication (d14, d15).
2. Does QXR keep its recall gain at equal total tokens against self-consistency or best-of-N? The paper reports no call or token counts (d04).
3. How does QXR degrade with a noisy or non-monotone oracle? Does the weighted hitting set fix it?
4. Do QXR gains hold on diagnosis tasks (faulty code, reasoning chains) rather than claim sets of about 30?
5. Can an LLM give fault probabilities usable for best-first or entropy heuristics, and how wrong may they be before random probing wins (a19)?
6. Does carrying the suspect set across observations help a window-limited agent, versus re-deriving?
7. At what suspect-list length does a bounded frontier start to matter for an LLM?
8. Which 2023-2026 diagnosis papers use LLMs? The targeted search was not completed (d17).
9. Are random or worst-first samples better than best-first when the LLM proposes the candidate sample?
10. Does RBF-HS memory saving hold up beyond one benchmark family and one reasoner?

## 11. Sources

Opened = [V], snippet or metadata only = [M].

- [V] Rodler (2022) RBF-HS, AIJ 305 (arXiv tech report). https://arxiv.org/abs/2010.04282 (a01-a08, b01-b06, b17, b23)
- [V] Rodler (2020/2022) Sound, complete, linear-space, best-first diagnosis search (DX short version). https://arxiv.org/abs/2009.12190 (a09, b08, c08-c10)
- [V] Rodler (2023) Memory-limited model-based diagnosis, IJCAI-23 extended abstract. https://www.ijcai.org/proceedings/2023/0789.pdf (b07)
- [M] Same abstract page, snippet: https://ijcai.org/proceedings/2023/789.md (c11, superseded by b07)
- [V] Rodler (2020/2022) DynamicHS. https://arxiv.org/abs/2012.11078 (a10-a13, b09, b24, c12, c13)
- [V] Rodler (2019) Towards optimizing Reiter's HS-Tree for sequential diagnosis. https://arxiv.org/abs/1907.12130 (a14)
- [V] Rodler and Elichanova (2020/2022) Do we really sample right in model-based diagnosis? https://arxiv.org/abs/2009.12178 (a15, a16, c14, c15)
- [V] Rodler (2023) Don't treat the symptom, find the cause! Habilitation thesis. https://arxiv.org/abs/2306.12850 (a17-a22, a26, a27, c17)
- [V] Rodler (2022/2024) How should I compute my candidates? A taxonomy and classification of diagnosis computation algorithms. https://arxiv.org/abs/2207.12583 (a23, a24, c16)
- [V] Shchekotykhin, Fleiss, Rodler, Friedrich (2012) Direct computation of diagnoses for ontology debugging. https://arxiv.org/abs/1209.0997 (a25, b13, b27, c20)
- [V] Shchekotykhin, Jannach, Schmitz (2015) MergeXplain. https://web-ainf.aau.at/pub/jannach/files/Conference_IJCAI_2015.pdf (b10, b15, b16, b25)
- [V] Jannach, Schmitz, Shchekotykhin (2016) Parallelized hitting set computation. https://web-ainf.aau.at/pub/jannach/files/Conference_AAAI_2015.pdf (b11, b26)
- [V] Felfernig, Schubert, Zehentner (2012/2021) FastDiag. https://arxiv.org/abs/2102.09005 (b12, b28)
- [V] Ignatiev, Morgado, Marques-Silva (2017) Model based diagnosis of multiple observations with implicit hitting sets. https://arxiv.org/abs/1707.01972 (b14)
- [V] Rodler, Jannach, Schekotihin, Fleiss (2019) Are query-based ontology debuggers really helping? https://arxiv.org/abs/1904.01484 (c18, c19)
- [M] Rodler (2020) Understanding the QuickXPlain algorithm. https://arxiv.org/abs/2001.01835 (c21; downloaded, not read in detail)
- [V] He, Kirschbaum, Kasiviswanathan (2026) Global consistency repair for noisy LLM judgments (QXR). https://arxiv.org/abs/2601.13600 (b18-b21, c01-c07, d01-d05)
- [V] Zhu and Chang (2026) A verifier can leak the answer. https://arxiv.org/abs/2610.00126 (b22)
- [V] Garg et al. (2025) G-CSEA. https://arxiv.org/abs/2509.13203 (c22)
- [V] Xu et al. (2026) Delta1 with LLM. https://arxiv.org/abs/2603.12953 (c23)
- [V] Pandey et al. (2026) Certified multi-source integrity. https://arxiv.org/abs/2609.34245 (c24, c25)
- [V] Hipler, Leucker, Rodler (2026) A unified framework for runtime verification and diagnosis. https://arxiv.org/abs/2606.23720 (a28, c26; abstract and introduction only)
- [V] arXiv author and title searches, Nov 2026. https://arxiv.org/search/?query=Rodler+diagnosis&searchtype=all (c27); [M] a29 search note, https://arxiv.org/search/
- [V] Zheng et al. (2025) ProcessBench. https://arxiv.org/abs/2412.06559 (d06)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516 (d07)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (d08)
- [V] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975 (d09)
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (d10)
- [V] Bailis, Stoica, Zaharia, Zou (2024) Are more LM calls all you need? https://arxiv.org/abs/2403.02419 (d11)
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 (d12)
- [V] Liu et al. (2024) Lost in the middle. https://arxiv.org/abs/2307.03172 (d13)
- [V] Semantic Scholar citation list of RBF-HS. https://api.semanticscholar.org/graph/v1/paper/arXiv:2010.04282/citations (d14)
- [M] Lu et al. (2026) EC-MHS, Symmetry 18. https://doi.org/10.3390/sym18081379 (d15; abstract only)
- [M] Rodler, Hofer, Jannach, Nica, Wotawa (2025) Choosing abstraction levels for model-based software debugging, AIJ. https://doi.org/10.1016/j.artint.2025.104399 (d16; metadata only)
- [M] Search log, Semantic Scholar and OpenAlex keyword searches. https://api.semanticscholar.org/graph/v1/paper/search (d17; rate limited)
- Reiter (1987) A theory of diagnosis from first principles; Greiner et al. (1989) HS-DAG; Junker (2004) QuickXplain; Korf (1993) RBFS. [M] known through the thesis and papers above (a27, a26), not opened separately.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 2 established claims: 0 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C09.05-K08** (reworded: the sources support less). In the 13 cases HS-Tree within 2 hours could not return all the requested (1, 9, 30) leading diagnoses, but it did return 1 for csa-ekaw and 1 and 9 for ldoa-confof, so 'diagnosable only by the direct method' is too strong; 133/146 and mixed timings and FastDiag log2 checks are verified. Corrected claim: Computing diagnoses directly, without conflict sets, helps when conflicts are hard to get: on 146 faulty OAEI-2011 alignments, HS-Tree could not return all requested leading diagnoses within 2 hours in 13 cases where the direct INV-HS-Tree could; timings elsewhere are mixed. Direct encodings are reported to beat HS-Tree when only one diagnosis is needed (FastDiag: about log2 consistency checks).
- **C09.05-K23** (reworded: the sources support less). Numbers verified (Xiong GPT-4 average AUROC 62.7%, values mostly 80-100%, GPT-3/3.5/Vicuna ECE >0.377; Tian verbalised cuts ECE by over 50% relative), but both studies test QA/classification confidence, not fault-probability priors for diagnosis, so the closing 'should not rely on LLM fault priors' is an extrapolation. Corrected claim: LLM-verbalised confidence on QA-style tasks is overconfident and weak at separating right from wrong answers (GPT-4 average AUROC 62.7 percent, values mostly 80 to 100 percent), though for RLHF models verbalised probabilities cut expected calibration error by over 50 percent relative to token probabilities; by extension, LLM-supplied fault priors for entropy or best-first heuristics should be treated as untested and not relied on.
