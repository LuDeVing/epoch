# Functional decomposition: deep document

*Subfield E07.02. Source files in this folder: evidence_a.jsonl (a01-a30), evidence_b.jsonl (b01-b27), evidence_c.jsonl (c01-c25), evidence_d.jsonl (d01-d15), claims.jsonl (E07.02-K01 to K31), critique.md. Evidence ids below refer to those files. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Functional decomposition means breaking an overall function ("make popcorn", "hold a liquid and keep it hot", "answer this question") into smaller sub-functions. The parts are then solved one by one and joined back into a whole.

In engineering design it has a specific form. The Stone and Wood school writes each sub-function as a verb plus an object. The object is a flow of material, energy or signal. The result is a "function structure": a graph of sub-functions linked by flows. The Functional Basis (Hirtz et al. 2002) fixes the vocabulary: 3 flow classes and 8 function classes, 53 function terms and 42 flow terms (a13).

Three things get called "functional decomposition", and they must be kept apart.

1. **Analytic decomposition as a search argument.** Simon (1962) and Parnas (1972). Split a task so each piece can be finished and checked alone. Gains are shown by argument and arithmetic, not by experiment.
2. **Function-structure modelling in design.** Stone and Wood, Pahl and Beitz lineage. A representation step before concept generation. Tested on people in a few small studies, mostly at Purdue (Booth et al.), plus Linsey 2005 and Atilola.
3. **Decomposition prompting for language models.** Least-to-most, Decomposed Prompting, ADaPT, Parsel, Atom of Thoughts. Mostly on code, math and agent tasks. Almost never on engineering products.

Why it matters for our agent. It is operator O3 ("Decompose: 2 to 4 sub-problems whose answers combine into the answer"), currently rated [S] in SCHEMA.md. It touches S0 (gate: when to decompose), S6 (when to pick which operator), S7/S8 (recombine and verify), G1 (doubt only on a signal), G7 (pay for itself at equal tokens), G9 (no debate) and G12 (spend by difficulty).

The short verdict from the evidence:

- The theory is strong and old. A split pays only when parts are stable, separately checkable and weakly coupled.
- The human design evidence that function modelling improves designs is thin and mostly null (K05, K21).
- The LLM evidence shows large gains on deep, cleanly separable, checkable tasks with weaker models (SCAN, TextCraft, Parsel). It shows small or zero gains on shallow tasks and on strong reasoning models (K11, K13, K25).
- No study scores LLM function structures against expert Stone-and-Wood structures (K18, K26). Evidence for engineering products is borrowed from code and question answering.

## 2. History and theories in depth

### 2.1 Simon 1962: near-decomposability and the watchmakers (a01-a05)

Simon's parable of Hora and Tempus is the founding quantitative case.

- Two watchmakers each build a watch of 1,000 parts. Customers interrupt at random. The chance of an interruption on each part added is 1 in 100.
- Tempus builds in one piece. An interruption drops the whole assembly. He finishes an uninterrupted run with probability 0.99^1000, about 44 times per million attempts.
- Hora builds stable sub-assemblies of 10 parts each. An interruption loses at most one small unit. A 10-part unit survives about 9 times in 10.
- Net result: Tempus needs about 4,000 times as long (Simon's working: 1/111 x 20 x 20,000). Hora completes about 111 times as many assemblies.

The safe-cracking example (a02) makes the same point with search. A safe has ten dials with 100 settings each. Blind search needs on average about 50 billion billion tries (100^10 scale). If each dial clicks when correct, the dials are set one at a time: about 10 x 50 = 500 tries.

The two lessons:

- The gain comes from **stable intermediate results** that survive an error.
- The gain needs **separate feedback per part**. With no per-part signal, search stays exponential.

Simon also defines **near-decomposability** (a03). Links inside a component are stronger than links between components. Short-run behaviour of each part is roughly independent of the others. In the long run a part depends on the others only through aggregates. The cost of splitting is the weak cross-links that get dropped (a05). Simon gives no numeric bound on this loss. He also gives no test of how decomposable a given problem is.

Simon argues that people describe complex objects in hierarchic order (outline, then features, then details) and that systems which are not nearly decomposable may escape understanding (a04). This is argument from examples.

### 2.2 Parnas 1972: how you cut matters (a06-a08)

Parnas compares two decompositions of one small program (a KWIC index).

- Version 1 follows **processing steps** like a flowchart. This is the function-style split.
- Version 2 hides **one design decision per module**.

He lists five likely design changes (such as storing all lines in core, packing characters, building a shift index). In version 1 each change touches many modules. In version 2 each touches one. In version 1 the interfaces are shared table formats that must be fixed jointly. In version 2 they are function names and parameter types, so teams can start in parallel.

Parnas also flags a leak in his own version 2: the circular-shift module fixed the order of shifts, which revealed more than needed. He calls this a design error.

Limits: one toy system, judgement stated as subjective, no timing or participant data. Parnas says the flowchart approach was adequate for systems of about 5,000 to 10,000 instructions. So this is K02, single-source and argued, not measured.

### 2.3 Ulrich 1995: architecture as function-to-part mapping (a09, a10)

Product architecture is the scheme that allocates functional elements to physical components, plus the interfaces. A **modular** architecture maps functional elements to components one-to-one with decoupled interfaces. An **integral** one has a complex map or coupled interfaces. The trailer example has 6 functional elements in modular and integral layouts.

Ulrich also notes that function structures at finer levels embed more assumptions about the working principle (a10). Two products that do the same thing may look different when described in detail. A decomposition made too early or too fine fixes the solution type.

### 2.4 The Functional Basis: Stone and Wood, Hirtz et al. (a11-a16)

Stone and Wood (1999/2000) propose a controlled verb-object language for function. Functions are operations on flows of material, energy and signal. It gives a common vocabulary and a fixed stopping level. Reported later (Hirtz 2002): built from a review of over 30 articles and study of over 100 products (a11, secondary).

Hirtz et al. (2002, NIST TN 1447) merged two independent efforts (a12-a15):

- The NIST taxonomy: over 130 functions and over 100 flows, 6 class functions.
- The Stone and Wood basis: 8 function classes, 3 flow classes.
- Merged: 3 flow classes (material, signal, energy) and 8 function classes (branch, channel, connect, control magnitude, convert, provision, signal, support). 53 function terms and 42 flow terms. Energy has 13 secondary categories, material 5, signal 2.
- Convergence check: of 53 function terms, 46 appear in the NIST taxonomy and 47 in the original basis. Of 42 flow terms, 34 and 27 respectively.

The convergence is weaker than it sounds. Both efforts drew on Pahl and Beitz and overlapping literature. The lineage includes value engineering from the 1940s and TRIZ. Validation was by use (NIST modelled power tools, a vacuum transport system and archive encasements; Ford used it in Design for Six Sigma), not by a controlled trial (a15). The authors claim function modelling guides decomposition, architecture, concept generation and team organisation, and give no measurement that it does (a16).

### 2.5 Critiques of the account (a17-a20, a26, b15, a30)

Vermaas (2007) is the sharpest conceptual critic.

- The account holds two notions of function (verb-object phrases and verbs only).
- Listing operations on flows may describe **behaviour**, not intended **function** (a17).
- The main design problem: basis sub-functions need not match small, easily solvable sub-functions (a18). A cup that holds liquid and retains heat breaks into 12 basis sub-functions although a cup is one easy solution. "Convert electrical energy to rotational energy" is hard for motor designers.
- The Concept Generator keeps only models whose sub-functions have stored solutions. That avoids dead ends but cannot recover when the repository lacks a solution for a cluster of functions (a19).
- Proposed fix: a fine decomposition in basis terms for understanding, plus a second coarse decomposition into easily solvable parts (a20). Untested.

Van Eck (2009) surveys seven functional modelling approaches. In four, function is an input-output flow transformation. In three, it is an intended role of behaviour (a26). Van Eck, McAdams and Vermaas (2007) compared three models of functional reasoning and found no consensus (b15). Erden et al. (2008) review function modelling and show a wealth of approaches with different definitions (a30; the "17 criteria" count is second-hand). Chandrasekaran (2005) argues function-representation and function-modelling streams are complementary (a25). Gericke and Eisenbart (2017) benchmark function structures against their own framework on one glue gun, with biased authors (a27), and state that empirical evidence for the benefits of function modelling is only initial (a28).

Take-away: there is no single accepted meaning of "function" and no standard head-to-head test of formats.

### 2.6 Vocabulary level studies (a23, a24)

Caldwell et al. (2010/2011) studied 121 repository models (11 graphical, 110 list-based). They judged the tertiary level too coarse and flow terms not expressive enough. Sen et al. (2010) built an information-theoretic metric (verbs as nodes, objects as edges) and found the secondary level best in information content and density. Both are one research group and one repository, abstract pages only (K24, [C]).

### 2.7 Repeatability: the founding test of the method (a21, a22, d04, d15)

Kurfman et al. (2000, 2001, 2003) ran three experiments with participants of mixed skill, building models of a toaster, a power screwdriver and a toy dart gun at three universities. The abstracts say the method "enhances repeatability" and is "largely successful". We could not read participant counts or agreement percentages (full text behind a bot check). Do not cite any agreement figure (K30). Note that repeatability between modellers is not the same as better designs.

### 2.8 The Purdue studies and human design outcomes (b01-b11, a29)

Section 3 gives numbers. In short:

- Booth, Reid and Ramani (2013): three dissection methods, 26 students, no method effect (b07, b08).
- Booth, Bhasin, Reid and Ramani (2015): Study 1, 25 novice teams, method changes what is listed, not much of what is built (b01, b02, b06). Study 2, 78 industry reports, no link between using decomposition and grade (b03, b04, b05).
- Linsey et al. (2005): a given function list did not raise idea count and may have reduced highly novel concepts (b10, b11).

### 2.9 Fixation (b06, b11, b12, b14, d03)

The worry: a function list fixes the design space. Evidence points both ways (K07, [C]). Section 5 covers it.

### 2.10 Decomposition in language models: a short history

- 2022 to 2023: least-to-most, Decomposed Prompting, Plan-and-Solve, Self-ask, Parsel, Self-planning, ADaPT (b19-b24, c08-c13, c18-c20).
- 2023: limits and costs. Compositionality gap (c12), faith and fate (b25, c14), faithfulness of factored decomposition (b26, c21).
- 2024 to 2025: decomposition as inference-time search and budgeting (PlanSearch d07, DISC d06, Atom of Thoughts d09, Plan-and-Act d12, Self-Discover d11).
- 2025: LLM function-structure generation (Massoudi and Fuge b16/c01, Haddad and Seibel d01), multi-agent scaling studies (c16, c17), the fading value of step-by-step prompting on reasoning models (d08).
- Pre-LLM symbolic route: Rosenthal et al. cast decomposition as planning with 30 Roth functions as PDDL actions (c06, c07).

## 3. Core findings with exact numbers

Status uses the claim file: [E] established, [S] single-source, [C] contested. "Analytic" means argued or modelled, not an experiment.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Splitting into stable sub-assemblies cuts expected build time by orders of magnitude | Tempus 0.99^1000, 44 completions per million; about 4,000 times longer than Hora | Simon 1962 (a01) | [E] analytic (K01) |
| Per-part feedback turns exponential search into linear | 10 dials x 100 settings: about 500 tries versus about 100^10 | Simon 1962 (a02) | [E] analytic (K01) |
| Split by hidden decision beats split by processing step on change cost and parallel work | 5 listed design changes; no participants | Parnas 1972 (a06-a08) | [S] argued (K02) |
| Standard function vocabulary reached by two efforts | 53 function terms: 46 shared with NIST, 47 with original basis; 42 flow terms: 34 and 27 | Hirtz et al. 2002 (a14) | [S] vocabulary only (K03) |
| Method improves repeatability between modellers | 3 experiments; counts not read | Kurfman 2001/2003 (a21, a22, d04) | [S] abstract only (K04, K30) |
| Decomposition shows no reliable benefit for idea count or design quality in people | Linsey: 19.0 vs 19.7 ideas (n=5 vs 7 cells, 54 students); Booth 2013: 26 students, n=78 trees, H1-H4 rejected; Booth 2015 Study 2: n=78, r=0.075, p=0.515 | Linsey 2005 (b10); Booth 2013 (b07); Booth 2015 (b03) | [E] small null studies (K05) |
| Study 1 method effects (novice teams) | 25 teams. ANOVA p: functions 0.037, features 0.027, unmapped features 0.003, unmapped-feature rate 0.001. Functions: top-down 19.7, energy-flow 16.3, enumeration 15.1. Final features: energy-flow 8.8, top-down 7.4, enumeration 5.0. Tukey cells 11/13/16 (functions) and 4/12/9 (features) | Booth 2015 (b01, b02) | [S] one lab (K06) |
| Function list fixes the design space | Unmapped features per team: top-down 0.0, enumeration 0.2, energy-flow 1.3. Linsey: concepts scoring 4 or more on novelty: control 5, functions 2; scoring 3 or more: 26 vs 23 | Booth 2015 (b06); Linsey 2005 (b11) | [C] (K07) |
| Function tree of an example caused no more fixation than control | N=61, 4 cells of 15/15/15/16. Omnibus p=0.083; sketch vs control p=0.038; tree vs sketch p=0.043; tree vs control n.s. Sketch+tree worst. Quality: tree best, p=0.036-0.043 (omnibus p=0.08) | Atilola thesis (d03) | [S] (K27) |
| Novices misuse the method | 51% of industry function diagrams rated very low quality; mean 14.4 functions (SD 9.0); mean 5.88 syntax errors per diagram (SD 6.0); 14 of 26 never learned decomposition | Booth 2015 (b04); Booth 2013 (b08) | [E] (K08) |
| Morphological matrix weakly predicts grade where decomposition did not | Matrix vs total grade r=0.233, p=0.040; vs ideation r=0.293, p=0.009 | Booth 2015 (b05) | [S] many tests (K22) |
| Class level raises abstraction | Sophomore 3.5, junior 4.17, senior 4.84 levels; device effect F=3.63, p=0.0352 | Booth 2013 (b08) | [S] (K23) |
| Basis sub-functions do not match solvable sub-problems | Cup = 12 basis sub-functions | Vermaas 2007 (a18) | [E] with ADaPT (K09) |
| As-needed decomposition beats up-front plan-and-execute (GPT-3.5) | ALFWorld 71.6 vs 43.3 (ReAct), 43.3 (Plan-and-Execute), 57.5 (Reflexion). WebShop 44.0 vs 32.0 / 17.0 / 35.0. TextCraft 52.0 vs 19.0 / 27.0 / 32.0. Second ALFWorld table (Yao executor, test split): ADaPT 79.8, Plan-and-Execute 63.4, Reflexion 67.2, ReAct 56.7 | Prasad 2024 (b23, c10; critique 7) | [S] (K10) |
| Gain grows with depth | TextCraft depth 2: 26.9 to 78.2; depth 3: 1.8 to 38.7. Weak executor: 3.3 to 41.7. GSM8K 5+ steps: 45.23 vs 39.07; 2 steps: 74.53 vs 76.68 (worse) | Prasad (b24, c11); Zhou (b20) | [E] (K11) |
| SCAN length generalisation | Least-to-most 99.7 vs CoT 16.2 vs few-shot 16.7 (code-davinci-002) | Zhou 2023 (b19) | [E] on synthetic task |
| Least-to-most on GSM8K and DROP | GSM8K 62.39 vs 60.87; DROP non-football 82.45 vs 74.77, football 73.42 vs 59.56 | Zhou 2023 (b20) | [E] small gain |
| Weak link is the model's own decomposition | HumanEval pass@1: direct 48.1, code-CoT 53.9, self-planning 60.3, perfect plan 74.4. LLaMA-2-70B 20.4 to 43.3 with GPT-3.5 planner. code-cushman-001: 34.0 direct vs 30.1 planned | Jiang 2023 (c20); Prasad (c11) | [E] (K12) |
| Plan-first gain is small and shrinks with sampling | Plan-and-Solve avg 70.4 / 73.5 / 76.7 (CoT / PS / PS+); GSM8K +0.6 for plain PS. Self-planning pass@10: 76.3 vs 75.0 direct vs 68.6 code-CoT | Wang 2023 (b21); Jiang (critique 11) | [E] (K13) |
| Generic step-by-step adds ~0 on reasoning models | GPQA Diamond, 198 questions x 25 trials. Only o4-mini gained at one threshold (+0.056, p=.003); Flash 2.5 fell (-0.131, p<.001 at 100%). Time +20 to 80% | Meincke 2025 (d08) | [E]/[S] one benchmark (K13, K25) |
| Compositionality gap | About 40% from 1B to 175B; ChatGPT 42.9%, GPT-4 23.0%. 3x3-digit multiplication: ChatGPT 55%, GPT-4 59%. 4x2 digits: 82.3% of final-correct answers held a wrong step | Press 2023 (c12); Dziri 2023 (b25, c14) | [E] (K14) |
| Self-ask with search | Bamboogle: direct 17.6, CoT 46.4, self-ask 57.6, +search 60.0. 2Wiki EM: 25.4 / 29.8 / 30.0 / 40.1 | Press 2023 (c13) | [S] |
| Multi-agent splitting helps only on independent parts | Finance (D=0.41) centralized +80.8% (0.631 vs 0.349). PlanCraft (D=0.42): -39.1 / -50.3 / -70.0% vs 0.568. SWE-bench -2.1 to -14.9% vs 0.522. Aggregate -0.3%, CI -58.7 to +77.2. Error amplification 17.2x / 7.8x / 5.1x / 4.4x | Scaling Agent Systems (c16, c17) | [E] with Massoudi (K15) |
| Nine-agent decomposition: finer graphs, worse runs | 60 runs. Requirement coverage max 20%. JSON valid 100%. R1 two-agent T=0: 1 node, 38.6 s, 100% executable. Llama two-agent T=0.5: 94.7%. MAS about 650 s, 34.8-40.2% executable, Llama MAS 0/5 completions | Massoudi and Fuge 2025 (b16, b17, c01-c03) | [E] with c16 (K15, K18) |
| Separate-context sub-questions raise faithfulness at an accuracy cost | Mistake inserted: answer changed 33.6% vs 9.6%. Suggested-answer drop 9.2 vs 21.3. Accuracy avg 81.8 vs 87.0; HotpotQA 83.0 vs 87.3 | Radhakrishnan 2023 (b26, c21) | [S] (K16) |
| Decompose, implement parts, select by tests | HumanEval 128 samples: direct 84.1 vs Parsel 93.9. APPS pass@8x16: direct-to-Python 6 vs 25.5 (100 problems). HumanEval pass@1 85.1 | Zelikman 2023 (c18, c19) | [S] (K17) |
| Adaptive splitting beats best-of-N at equal tokens | Pass@10 error: APPS 0.50 to 0.475, MATH500 0.15 to 0.14, LiveCodeBench 0.57 to 0.51. R1 +33% relative at one-sample token budget | DISC (d06) | [S] (K17) |
| Plan search needs large budgets | Sonnet 3.5 LiveCodeBench pass@200 77.0 vs 60.6 repeated sampling vs 41.4 best single. About 1,428 vs 244 tokens per completion. Wins only above about 10,000 tokens per problem; often lowers pass@1 | Wang 2024 PlanSearch (d07) | [S] (K28) |
| Decompose-and-contract on reasoning models | o3-mini AIME 79.6 to 83.0; LiveCodeBench 23.6 to 32.2; LongBench 56.3 to 65.3; R1 AIME 78.3 to 81.7. Cost not matched | Atom of Thoughts (d09) | [S] unreplicated (K25) |
| Half-enforced decomposition can be worse than none | Dropping DAG contraction hurt more than dropping decomposition; accuracy falls with depth and sub-question count; typical 3-4 parts at depth 3 | AoT ablation (d10) | [S] figure only (K29) |
| Replanning beats a static plan | Plan-and-Act WebArena-Lite: +10.31 over static planner (53.94); untrained planner did not help trained executors | Erdogan 2025 (d12) | [S] trained planner (K28) |
| LLM function graphs on 50 products | Plain GPT-4o: 100% format, 44% connected, 16% error-free. +MCTS-FD: 72% connected, 42% error-free, 0.9 errors per graph. Llama 405B: 40% connected, 10% error-free. Llama 8B: 0% error-free | Haddad and Seibel 2025 (d01) | [S] (K26) |
| Search variant rated worse by humans | Completeness GPT-4o 3.96, students 3.91, MCTS-FD 3.53. Logic 4.00 / 3.87 / 3.69. Creativity students 3.48, MCTS-FD 3.32, GPT-4o 3.12. 12 student entries rated of 20 | Haddad and Seibel 2025 (d02) | [S] peer-rated (K18) |
| Untuned part-function classification is near useless | 8 classes: GPT-3.5 0.04, GPT-4o mini 0.20, GPT-4 Turbo 0.27; fine-tuned 0.89 at 681 samples, 0.63 at 6,130 | Elhambakhsh 2025 (b18, c04) | [S] labelling only (K19) |
| Symbolic planner solves decomposition over a fixed library | 30 Roth functions as PDDL actions; 2 worked examples (coffee maker, siege engine); no benchmark | Rosenthal 2023/24 (c06, c07) | [S] (K20) |
| One cached structure per task is cheap | 1 call per instance plus 3 task-level calls vs 10 (CoT-SC) to 40 (voting) | Self-Discover (d11) | [S] calls not tokens (K31) |

## 4. Mechanisms and models

Each mechanism below is written so an engineer can implement it in the harness.

### 4.1 Reliability arithmetic of chunking (Simon)

Model. A task has N steps. Each step fails with probability p, and a failure forces a restart from the last saved state.

- Without saved intermediate results: P(success per attempt) = (1-p)^N. Expected attempts are 1/(1-p)^N.
- With sub-assemblies of size k, each saved and checked: expected attempts per unit are 1/(1-p)^k. Total work is about (N/k) x 1/(1-p)^k.
- At p = 0.01, N = 1000: unsplit success is 0.99^1000 = 4.4e-5. With k = 10, a unit succeeds about 0.904 of the time.

Implementation for the agent. A sub-answer is **kept** once code has passed it. A later failure must not discard it. This is the real content of O3. Splitting without keeping and checking yields nothing.

Search-side version. With per-part checks, expected tries fall from product to sum (10 dials: 500 vs 100^10). Rule: **count a decomposition as useful only if each part has its own code check.** If a part has no separate check, merge it with a neighbour.

### 4.2 Near-decomposability test (Simon, Parnas, Ulrich)

Split where cross-links are weak. A cheap proxy the harness can compute:

1. After the model proposes 2 to 4 sub-problems, ask for each its inputs, output form, and "what it needs from the other parts".
2. Build a dependency list. Code marks a split as *independent* if no part's inputs depend on another part's unfinished output.
3. Independent: parts may run in fresh contexts in parallel and be combined. Chained: run in order, feeding each answer forward (least-to-most style), or do not split.

Interface rule (Parnas). Each sub-problem gets a short written interface: inputs, output form, what must hold. Specify what must hold, not how (a08: over-specifying leaks a decision and blocks good solutions).

Hiding rule for code tasks. Split by the decision to hide (data format, algorithm choice), not by processing step, when later change requests are likely (K02, [S]).

### 4.3 As-needed recursive decomposition (ADaPT)

ADaPT pseudo-code, as described in b23, b24, c10, c11:

```
solve(task, depth):
    result = executor(task)           # try directly first
    if success(result): return result
    if depth == d_max: return result  # d_max = 3 or 4
    subtasks, logic = planner(task)   # AND / OR over subtasks
    results = [solve(s, depth+1) for s in subtasks]
    return combine(results, logic)
```

Features that matter:

- Try first, split on failure. That matches G1.
- Depth is capped (d_max 3 or 4). Max depth actually used rose with recipe depth (1.9 at depth 2, 2.8 at depth 3).
- Planner and executor may be different models. A stronger planner lifted LLaMA-2-70B from 20.4 to 43.3 and GPT-3.5 from 38.4 to 58.3 on ALFWorld dev (c11).
- The success signal came from the LLM executor. On WebShop its self-judgement was over 30 points above the real reward. So a model-only stop rule can end decomposition too early (c10). Our agent should use a code check as the failure signal where it exists.

Caveats: GPT-3.5 executors, three text environments, extra calls not cost-matched, and the headline gain over plan-and-execute is 28.3 points on one table and 16.4 on the other (critique 7).

### 4.4 Decompose, implement, select by test (Parsel)

Parsel pseudo-code from c18, c19:

```
spec = hierarchy of function descriptions (plain language + examples as tests)
for each leaf function f:
    candidates[f] = sample K implementations
combos = product over leaves, filtered by passing the tests
choose the combination that passes the most tests
```

What matters: parts are implemented separately, then **combinations are selected by running tests**, not by a model opinion. The ablation that turned the same plans straight into Python lost most of the gain (6% vs 25.5% on 100 APPS problems). So per-part search with checks adds value on top of the plan. Needs tests. A 2.7B model solved 0 of 25 APPS problems, so the base model must be able to do the parts.

### 4.5 Budget allocation by splitting the trace (DISC)

DISC (d06) splits a solution into a prefix and suffix, then spends more samples on the steps that matter. It beat best-of-N at matched token budgets, with small absolute gains on gpt-4o-mini (1 to 6 points) and larger relative gains on weaker models. It needs a reward signal (tests, a reward model, or LLM-written tests). It decomposes the solution, not the problem. Use: a way to put extra samples where the model is uncertain, rather than an up-front plan.

### 4.6 Decompose and contract (Atom of Thoughts)

AoT (d09, d10): break the question into a dependency graph; solve the independent leaves; contract the result into a smaller equivalent question; repeat up to a small cap (max transition count 3). Ablations: removing decomposition hurts, and keeping decomposition but dropping DAG-guided contraction hurts more. Practical size rule from the paper: most problems split into 3 to 4 parts at depth 3, and accuracy falls with more depth or more sub-questions.

Reading: a half-applied structure may be worse than none. Treat the contraction (the combine step) as part of O3, not an add-on.

### 4.7 Plan search over diverse plans (PlanSearch)

PlanSearch (d07): sample short natural-language observations, combine them into plans, code each plan. Diversity of plans predicts the gain. A correct sketch, even 10 tokens, greatly raises solve rate. Token-matched, it wins only above about 10,000 tokens per problem and often lowers pass@1. Reading: use plan variation only when the budget is large.

### 4.8 Planning formulation (Rosenthal)

Decomposition as classical planning (c06, c07):

- Actions: the 30 Roth functions, each with preconditions and effects on flows.
- Start state: the input flows. Goal state: the output flows.
- Solver: a partial-order planner. The output is an ordered set of steps with parallel groups (for the coffee maker: guide water and guide energy in parallel, then convert energy, then add).

Value for the agent: code can check preconditions and effects of each proposed sub-function, so a model-proposed decomposition can be validated without a model judge. Needs start and goal states already written in verb-noun form. No benchmark exists.

### 4.9 Rule checks on a function graph (Haddad and Seibel)

Checks the harness can run in code on a model-written graph (d01):

- Node arity (a function like "add" needs at least two inputs).
- Connectivity (no disconnected nodes).
- Valid format (JSON).
- Every requirement maps to at least one sub-function (suggested by b16, coverage max 20%).
- Flow consistency between linked parts (c02: flows were declared but not coherently connected).

The loop (MCTS with self-refinement) raised connected graphs from 44% to 72% and error-free graphs from 16% to 42%. Blind human raters did not prefer it (d02). So a checker raises rule validity, not necessarily quality.

### 4.10 Why sub-answers right does not mean whole answer right

Press (c12) and Dziri (b25, c14) show a recombination error source. Dziri's account: errors propagate through the computation graph; models match remembered sub-graphs rather than run an algorithm. Fix in the schema: a code-owned **combine** and a final check on the **composed** answer (S8), not only on parts.

### 4.11 Faithfulness through separate contexts (Radhakrishnan)

Factored decomposition (b26, c21): each sub-question is answered in a separate context that does not see the reasoning chain. Because the final answer depends on the sub-answers only, the stated reasoning is a truer record. Cost: about 5 accuracy points on average. Use only where faithfulness matters.

### 4.12 Two-level decomposition (Vermaas proposal)

A fine functional list for understanding plus a coarse list of 2 to 4 sub-problems that are directly solvable (a20). Fits S2 (represent) then S6 (subgoals). Untested.

## 5. What holds up

### 5.1 Replications and failures

There are almost no true replications in this subfield.

- **Human null results across three independent designs.** Linsey 2005 (given function list vs control), Booth 2013 (three analysis methods, within subject), Booth 2015 Study 2 (observational, industry). All point to no clear benefit. They are small (cells of 5 to 16, n=26 trees of 78, 78 reports) and the second and third are from the same lab. A small benefit is not excluded (K05).
- **Booth 2015 internal problems.** The Tukey cell sizes (11, 13, 16 for functions; 4, 12, 9 for features) do not sum to the 25 teams for the function metric and the paper does not explain the 40 (critique 2). The energy-flow feature cell has 4 teams. Diagram-type percentages disagree between figure and text (b04). Quality was rated by the authors.
- **Booth 2013 limits.** Reverse engineering of existing products, task maybe too simple, device order confounded with time, no effect size reported because n<100 (critique 4).
- **Kurfman repeatability** was never independently replicated and its numbers are unavailable to us.
- **ADaPT gap shrinks across tables.** 28.3 points over plan-and-execute in one table, 16.4 in another (critique 7).
- **Self-planning gain shrinks with sampling.** pass@1 60.3 vs 48.1 but pass@10 76.3 vs 75.0 (critique 11).
- **Atom of Thoughts** is one group's report with a very regular pattern of baseline gaps and LLM-judged quality checks. Unreplicated (d09).
- **Haddad and Seibel** rule-validity gain did not carry to human ratings (d02).
- **Scaling Agent Systems.** The paper's own regression shows the error-amplification term not significant (p=0.658). Cross-validated R2 is only 0.373. Aggregate multi-agent effect -0.3% with a wide interval (critique 9, c16, c17).

### 5.2 Moderators that recur

| Moderator | Direction | Evidence |
|---|---|---|
| Task depth or length | Gain grows with depth, reverses at 2 steps | b20, b24, c11, b22 (K11) |
| Independence of parts | Independent parts gain, chained parts lose | c16, c01 (K15) |
| Separate check per part | Needed for Simon's gain and for Parsel selection | a02, c18 (K01, K17) |
| Quality of the decomposition | Poor plan hurts; perfect plan +14.1 points on HumanEval | c20, d12, b04 (K12, K29) |
| Who writes the plan | Strong separate planner helps weak executor; small model planning for itself loses | c11, c20 (K12) |
| Base-model strength | Weak models gain most; reasoning models gain about zero from generic stepping | b24, d08 (K13, K25) |
| Sampling budget | Plan gains shrink at larger k; plan search needs about 10,000 tokens | critique 11, d07 (K13, K28) |
| Skill and fatigue (humans) | Class level and order beat method | b08 (K23) |
| How the function view is used | Shown example tree safer than sketch; given list may reduce novelty; stimuli may raise novelty | b11, d03, b14 (K07) |

Reconciling the planner and executor findings: ADaPT says a weak executor gains most; self-planning says a small model loses when planning for itself. The reconciliation in K12 is that it matters who writes the plan. This is an interpretation, not a tested result.

### 5.3 What worked

- As-needed (failure-triggered) recursive decomposition on deep, rule-based tasks (ADaPT).
- Hand-made or strong-planner decomposition with a weak executor (c11).
- Decompose, implement in parallel, select by running tests (Parsel).
- Budgeting samples at uncertain steps (DISC).
- A cheap rule check plus refinement loop on function graphs, for rule validity only (d01).
- Replanning on failure (+10.31 points in Plan-and-Act; d12).
- Plain thin loops with a code check beat nine-role pipelines (Massoudi, c01).

### 5.4 What did not work

- Up-front static plan-and-execute with a weak model: WebShop 17.0 vs ReAct 32.0 (b23).
- Generic step-by-step prompting on reasoning models (d08).
- Nine-agent splitting on tightly chained tasks (PlanCraft -39.1 to -70.0%; c16).
- Multi-agent role pipelines for function structure: coverage at most 20%, up to 100% non-completion for one model (b16, c01).
- Enumeration as a decomposition method for novices: weakest in Booth Study 1 ("We would recommend not using an enumeration approach for early design", b02).
- Self-planning for a small model (30.1 planned vs 34.0 direct; c20).
- Search-refined function graphs on human-rated quality (d02).

### 5.5 Fixation: the conflict

| Study | Manipulation | Result |
|---|---|---|
| Linsey 2005 (b11) | Given function list vs control | Control 5 vs functions 2 concepts scoring 4+ on novelty; counts raw, no test, preliminary |
| Booth 2015 (b06) | Own decomposition before concept | Nearly all final features map to listed functions; authors give three readings the data cannot separate |
| Atilola thesis (d03) | Example shown as tree, sketch, both, none | Tree: no more fixation than control; sketch+tree worst; omnibus p=0.083; pairwise statistics look inconsistent |
| 2018 CIE (b14) | Function terms as stimuli, 20 novices | More usefulness, novelty, variety; abstract only, no control details |

Reading. The manipulations differ: a given list, one's own list, a shown example's tree, and words as stimuli. So the claim "decomposition fixates" is [C], not refuted. There is no LLM test (K27). A shown decomposition of an example is a lower-risk anchor than the example; both together are worst. This is human evidence on someone else's decomposition (d03).

## 6. Language models

### 6.1 Summary by task family

| Task family | Models | Result | Evidence |
|---|---|---|---|
| Synthetic compositional (SCAN length) | code-davinci-002 | 99.7 vs 16.2 CoT. text-davinci-002: 76.0 vs 0.0. code-davinci-001: 60.7 vs 0.0 | b19 |
| Math word problems | code-davinci-002 / davinci-003 | GSM8K +1.5 (least-to-most), +0.6 plain Plan-and-Solve, +2.9 PS+. 2-step problems worse; 5+ steps +6.2 | b20, b21 |
| Reading numeric (DROP) | code-davinci-002 | +7.7 non-football, +13.9 football | b20 |
| Long-sequence toys | davinci era | kth-letter concatenation stays near 100% while CoT falls with length | b22 |
| Interactive agents | GPT-3.5, up to GPT-4 | ADaPT up to +37 points on GPT-4; ALFWorld 71.6 vs 43.3 | b23, b24, c10 |
| Code, with tests | Codex, GPT-4 | Parsel 85.1 pass@1; 93.9 vs 84.1 at 128; 18 HumanEval tasks GPT-4 missed solved, 2 lost | c18 |
| Code, plan only | code-davinci-002 | 60.3 vs 48.1 pass@1; perfect plan 74.4 | c20 |
| Reasoning models, generic steps | o3-mini, o4-mini, Flash 2.5 | About zero; time +20 to 80% | d08 |
| Reasoning models, decompose and contract | o3-mini, R1 | +3.4 AIME, +8.6 LiveCodeBench for o3-mini, unmatched cost | d09 |
| Engineering function structure | GPT-4o, Llama, R1 | See 6.3 | b16, d01, d02 |
| Multi-agent splitting | three LLM families | Task-dependent, aggregate -0.3% | c16 |

### 6.2 What changed behaviour, and by how much

- **Giving the model a plan.** +12.2 points pass@1 for self-planning on HumanEval with a large model (48.1 to 60.3). A correct plan adds another 14.1 (to 74.4). Small models lose 3.9 (34.0 to 30.1). The gain nearly vanishes at pass@10 (76.3 vs 75.0).
- **Better planner for a weak executor.** LLaMA-2-70B: 20.4 to 43.3 (+22.9). GPT-3.5: 38.4 to 58.3 (+19.9). Both on ALFWorld dev (c11).
- **Splitting only on failure.** ALFWorld +28.3 points over plan-and-execute in one table and +16.4 in another; TextCraft depth 3 from 1.8 to 38.7.
- **Replan.** +10.31 points (WebArena-Lite) when adding replanning to a static planner; training required.
- **Separate calls per sub-task.** Decomposed Prompting held near 100% on long letter concatenation where CoT fell.
- **Tools for sub-questions.** Self-ask plus search: Bamboogle 57.6 to 60.0; 2Wiki EM 30.0 to 40.1.
- **Code selection among implementations.** HumanEval 84.1 to 93.9 at 128 samples; the only paper matching sample counts.
- **Token-matched adaptive splitting.** DISC: pass@10 error 0.50 to 0.475 (APPS), 0.57 to 0.51 (LiveCodeBench).
- **Scale.** Compositionality gap stays near 40% from 1B to 175B; 42.9% for ChatGPT; 23.0% for GPT-4. Scale alone does not close it.
- **Structure quality.** Removing the contraction step in AoT hurt more than removing decomposition.

### 6.3 LLMs on function structures of products

Evidence is thin and all weak models or small studies.

- **Massoudi and Fuge (b16, b17, c01-c03).** Task: requirements, function decomposition and simulator code for a solar water filter. 60 runs (2 models x 2 systems x 3 temperatures x 5 seeds). JSON validity 100% everywhere. Requirement coverage 0% in nearly all cells, best 20% (R1, nine-role system, T=0). Nine-role system: 5 to 6 nodes (6.0 +/- 1.9 at T=1.0), about 650 s, 34.8 to 40.2% executable code, many crashes (recursion limit 30 or over 60,000 tokens; Llama completed 0 of 5). Two-agent loop: R1 collapsed to 1 node at T=0 in 38.6 s with 100% executable code; Llama two-agent T=0.5 gave 94.7%. Best nine-role graph: 8 nodes (power, filtration, pump, storage, control, sensors, UI, housing) with physics errors (solar model without panel area; pump with specific gravity instead of density). Flow edges often declared but not connected. Main failure modes were non-termination and context overflow, not wrong content.
- **Haddad and Seibel (d01, d02).** 50 products, GPT-4o prompted with Roth's 21 functions, rules and 3 worked examples. Plain: 100% format, 44% connected, 16% error-free. With MCTS-FD: 72% connected, 42% error-free, 0.9 errors per graph, about 21 nodes and 19 edges. Llama 3.1 405B: 86% format, 40% connected, 10% error-free. Llama 8B: 0% error-free. Blind student ratings (12 of 20 student entries): plain GPT-4o completeness 3.96 and logic 4.00, equal to or above students (3.91, 3.87); MCTS-FD lower (3.53, 3.69). No comparison with expert Stone-and-Wood structures. MCTS-FD uses many more calls, tokens not matched.
- **Elhambakhsh et al. (b18, c04).** Not decomposition but labelling the function class of a single part. 8 classes. GPT-3.5 0.04, GPT-4o mini 0.20, GPT-4 Turbo 0.27 untuned. Tuned GPT-3.5 reached 0.89 test accuracy at 681 samples and 0.63 at 6,130. So function vocabulary is not in the model by default, and the fine-tuning curve is odd (overfitting or class imbalance suspected).
- **Sources not read.** The 2024 Function-Behavior-Structure prompting paper (b27) was seen only in summaries.

What is missing: sub-function recall and flow accuracy against expert structures, the effect of the verb-object vocabulary versus free wording, and any run with a 2025 to 2026 reasoning model (K18, K26).

### 6.4 Strong reasoning models

No direct test exists of an explicit decomposition step at equal tokens on a current reasoning model (K25).

- Generic step-by-step: about zero on o3-mini, o4-mini, Gemini Flash 2.5 (GPQA Diamond, 198 questions x 25 trials), with 20 to 80% more time (d08). One benchmark, early 2025 models, generic cue.
- Atom of Thoughts: +3.4 on AIME (o3-mini), +8.6 on LiveCodeBench, +3.4 on AIME for R1 (78.3 to 81.7). Unreplicated, cost not matched.
- DISC: +33% relative at the token budget of one base sample for R1 (d06), one figure.
- PlanSearch on o1-mini: trails repeated sampling at low k, slightly ahead at high k (d07).
- Massoudi: R1 two-agent run collapsed to one node. The model may already decompose internally.
- A second-hand small-model result (d13, not opened) says forced multi-step prompting scored 24% against 78% direct before fine-tuning.

### 6.5 Matching tokens

Most LLM decomposition studies spend more calls than their baselines (ADaPT, Parsel except at 128, Scaling Agents, MCTS-FD, AoT). Only Parsel at 128 samples and DISC match budgets. Self-Discover reports calls (1 plus 3 per task vs 10 to 40) but not tokens. Under G7 this is the main weakness of the evidence.

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. **Decompose only when a check exists for each part, or can be made.** Gain comes from kept, checked intermediate results (Simon). Without a separate check the saving is zero. | O3, S4, G3 | [E] | a01, a02, c18 (K01)
2. **Fire O3 on a failure signal, not on a schedule.** Failure-triggered recursion beat up-front plans on ALFWorld, WebShop and TextCraft with GPT-3.5, and static plan-and-execute was no better than ReAct on ALFWorld and worse on WebShop (17.0 vs 32.0). Keep O3 as an operator at S6 (already so in SCHEMA). | O3, S6, G1 | [E] direction; effect size [S] | b23, c10, b24 (K09, K10)
3. **Cap depth and size.** Depth 3 to 4 maximum, 2 to 4 parts. Accuracy falls with depth and sub-question count; most problems split into 3 to 4 parts at depth 3. | O3, G12 | [E] direction | b24, d10, b25 (K11, K29)
4. **Do not decompose short problems.** 2-step GSM8K 74.53 vs 76.68 (worse); gains only at 5+ steps. The S0 gate should route by expected step count. | S0, G12 | [E] direction; threshold unmeasured on current models | b20, b22, c11 (K11)
5. **Check the composed answer, not only the parts.** The compositionality gap stays about 40% even when sub-answers are right (GPT-4: 23.0%). Code recombination and a final S8 check. 82.3% of correct final answers in a 4x2 digit test held a wrong step, so check sub-results as well. | S7, S8, G3 | [E] | c12, c14, b25 (K14)
6. **Plan quality is the bottleneck, so check the decomposition itself with code.** Reject sub-problems that name a solution or a part instead of a need; require each requirement to map to a sub-problem; check input and output of each part; check flow or interface consistency. The human diagrams were 51% very low quality and LLM graphs gave coverage at most 20%. | O3, G2, G5 | [E] that quality matters; the specific gate is untested | b04, b09, b16, c20, d01 (K08, K12)
7. **Keep the structure thin.** Nine-role decomposition produced finer graphs with less runnable code and 0/5 completions; a two-agent loop with a code check was better. Hard budget and program-owned stop rule. | G7, G9, O3 | [E] | c01, c03, c16, c17 (K15)
8. **Split into parallel sub-agents only for independent parts.** Independent parts can gain (Finance +80.8%); chained parts lose (PlanCraft -39.1 to -70.0%). The agent stays single-threaded by default. | G9, G7 | [E] | c16, c01 (K15)
9. **Treat O3 as unproven by default.** Human evidence is null, LLM evidence is weak-model and unmatched-cost. Every O3 test runs at equal tokens (G7). | G7 | [E] | b03, b07, b10, a28 (K05, K21)
10. **Do not add a generic plan-first or step-by-step cue for strong reasoning models.** Value is about zero and time rises 20 to 80%. | G11 | [E] | d08, b21 (K13)
11. **A decomposition made by the model is the weak step; a strong or hand-made one helps.** If a separate stronger planner exists, use it for the plan only. | O3, S1 | [E] | c20, c11, b20 (K12)
12. **Re-decompose after a failed check.** A first split can bound all later search (function-list fixation) and replanning was worth +10.31 points in Plan-and-Act. | O3, G1, S6 | [E] for the need; effect size [S] | b06, d12 (K07, K28)

### Test first

Each of these is single-source, contested, human-only or older-model-only. None goes into SCHEMA.md until the test passes. The full list with thresholds is in UNKNOWNS.md.

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| O3 forced step versus none on a current reasoning model at equal tokens | O3, S0 | [S] indirect | d08, d09, d06 (K25) |
| Failure-triggered O3 versus up-front O3 versus plain with a retry at equal tokens | O3, S6, G1 | [S] | b23, c10 (K09, K10) |
| Route by expected step count in S0 gate | S0, G12 | [E] direction, [S] threshold | b20, c11 (K11) |
| Decompose, implement parts separately, select by tests versus flat sampling at equal samples | O3, S4, G5 | [S] | c18, d06, d07 (K17) |
| Decomposition quality gate on versus off | O3, G2 | [S] | d10, b04, d01 (K29, K08) |
| Show decomposition before generation versus after a free first attempt (diversity) | O3, G8, S3 | [C] | b11, d03, b06 (K07, K27) |
| Verb-object vocabulary versus free wording for sub-problems | O3 | [S] | a14, b18 (K03, K26) |
| Interface-first sub-problem specs (inputs, output form, what must hold) | O3 | [S] | a06-a08 (K02) |
| Split by decision versus by step on multi-file code with a change request | O3 | [S] | a06, a07 (K02) |
| Factored (separate context) sub-answers where faithfulness matters | G10, O3 | [S] | b26, c21 (K16) |
| Combine step (function-by-solution table) added to O3 | O3, O6 | [S] | b05 (K22) |
| One cached decomposition per task class versus per attempt | O3, S0, memory | [S] | d11 (K31) |
| Symbolic planner over proposed sub-goals versus free-text ordering | O3, S4 | [S] | c06, c23 (K20) |
| Memory: store the decomposition that worked, with its class and outcome | memory, S9 | [S] | d11 (K31) |

## 8. Concrete tests on our bench

All arms get equal total tokens (generation, setup, retries, decomposition calls). Report pass rate, tokens, and calls. Use at least 100 items per arm where the item type allows. Report intervals; the literature here rarely does.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 100 code-checked tasks, mixed difficulty (ARC-style programs and short coding tasks with tests), on a current reasoning model | (a) plain; (b) forced decomposition before solving; (c) decomposition at matched total tokens (fewer retries) | Pass rate at equal tokens | About zero or negative for (b) and (c) on easy items; small gain only on hard items. Prior from d08. |
| T2 | Same set, split into shallow (1 to 2 steps) and deep (5 or more steps) by gold step count | Always decompose vs route-by-length (S0 gate) vs never | Pass rate at equal tokens, by depth bucket | Always-decompose loses on shallow items (GSM8K 2-step -2.15); route-by-length ties or beats it. |
| T3 | Deep compositional tasks with a per-step check (multi-step planning, TextCraft-like crafting, multi-hop with tools) | Up-front plan-and-execute vs failure-triggered O3 (ADaPT-style) vs plain with retry on the same call budget | Success rate | Failure-triggered > up-front by a margin smaller than the published 16 to 28 points once the retry baseline is given the same budget. |
| T4 | Code tasks with tests | Flat sampling (k samples) vs decompose into function specs, sample implementations per part, select by tests, at equal total samples | pass@k at equal tokens | Gain at larger k only; below about 10,000 tokens per problem expect no gain (PlanSearch). |
| T5 | Tasks with clean independent sub-parts vs tightly chained parts (build both sets) | O3 on vs off, each on both sets | Pass rate | Gain only on independent set (K01 prediction). |
| T6 | Composed items where sub-answers are right (multi-hop trivia, multi-digit arithmetic) | Free composition vs code recombination plus S8 check on the composed answer | Fraction of composed items right; compositionality gap | Gap narrows; larger for weaker models. |
| T7 | 200 open-ended generation items scored by code-checkable constraints plus diversity of final answers | (a) free answer; (b) decomposition shown first; (c) free first attempt then decomposition | Constraint success; answer diversity (distinct clusters) | (b) narrows diversity (K07 prediction); (c) avoids the narrowing. If no narrowing appears, drop the fixation concern. |
| T8 | 10 or more products with expert Stone-and-Wood function structures built by hand | Plain model, model with Functional Basis verbs, model with free wording | Sub-function recall, flow edges correct, parts-versus-functions confusion rate, agreement across 5 runs | Vocabulary raises agreement across runs (K04 analogue); recall against experts is unknown. This is the missing replication. |
| T9 | Same decompositions as T1 | Quality gate on vs off (reject solution-naming sub-problems, check coverage of requirements, check part inputs and outputs) | Pass rate; gate rejection rate | Gate on beats half-enforced structure (AoT ablation). |
| T10 | Multi-file coding task followed by a change request | Split by step vs split by hidden decision | Files touched, tests broken after the change | Hiding split touches fewer files (Parnas). |
| T11 | Tasks with a plan score against a held-out solution | Free plan vs best-of-5 plans chosen by code | Plan quality (against held-out solution), final success, correlation | Plan quality predicts success; best-of-5 by code lifts both. |
| T12 | Same tasks, repeated by task class | One cached decomposition per class vs fresh per attempt | Pass rate and tokens | Cached ties at lower tokens (Self-Discover prior). |
| T13 | Tasks where parts need different contexts | Single thread vs separate-context sub-answers vs parallel sub-agents | Pass rate, answer-change rate when a mistake is inserted | Faithfulness up, accuracy about -5 points (Radhakrishnan). |

## 9. What does not transfer, and why

- **The Purdue results are about people on design problems.** Novices, one lab, small cells. The null for people (no gain in idea count or grade) may reflect poor diagram quality (51% very low quality), not a weak method. An LLM gets neither practice effects nor fatigue, and makes fewer syntax errors, so the human null cannot be read straight across.
- **Fixation by one's own function list.** In humans it may come from commitment and effort. An LLM sampling in fresh contexts has no memory of a plan unless we put it in the prompt. The risk exists only if the decomposition is shown to the generator.
- **Verb-object vocabulary.** Built for hardware (material, energy, signal flows). Hirtz et al. say nothing about reasoning tasks. The 46 or 47 of 53 overlap shows agreement on hardware terms, not usefulness.
- **Simon's arithmetic.** It assumes independent parts with stable results and an exact check. Open-ended tasks have neither. For tasks with a single answer and no per-part check, the saving is not available.
- **Parnas's module split.** A software-engineering result with 5,000 to 10,000 instruction systems. It informs how to cut code tasks, not word problems.
- **SCAN, kth-letter, list reversal.** Synthetic tasks with a clean recursive structure. Gains of 99.7 vs 16.2 will not appear on messy tasks.
- **ADaPT numbers.** Text environments with rule-based, cleanly decomposable structure and a GPT-3.5 executor; the authors built TextCraft themselves. Current models and open tasks may differ.
- **Planner-trained results** (Plan-and-Act) involve fine-tuning on synthetic plans. We scaffold, we do not train.
- **Multi-agent results.** Our schema is single-agent with code-owned hand-offs. The multi-agent failure evidence supports staying there, but the gain case (Finance +80.8%) is also a reminder that independent parts can pay.
- **Function-class labelling** (Elhambakhsh) is classification of single parts, not decomposition.
- **Self-Discover and AoT** rewrite or compose reasoning structures, not function structures. Their evidence applies to O3 only as "decompose then contract".
- **Rating studies** with peer raters and no significance tests (Haddad and Seibel) cannot settle quality questions.

## 10. Open questions

1. Does an explicit decomposition step help a 2025 to 2026 reasoning model at equal tokens, on code-checked tasks? No direct test exists (K25).
2. How well do LLMs reproduce expert Stone-and-Wood structures (sub-function recall, flow connectivity), and does a verb-object vocabulary change that? Unmeasured (K18, K26).
3. What were the participant counts and agreement percentages in Kurfman 2001 and 2003? Without them the founding test of the method cannot be weighed (K30).
4. Does showing an LLM its own decomposition before generation narrow its final answers, and does decomposing after a free attempt avoid it? (K27)
5. Is the gain from decomposition better plans or more tokens? Plan quality scored against a held-out solution and correlated with success is missing outside PlanSearch (K28).
6. What is the break-even step count or depth on current models? GSM8K shows a loss at 2 steps and gain at 5+; no threshold on current models.
7. Is the Booth null caused by poor use (51% very low quality) or a weak method? A study where experts or a checker enforce diagram quality has not been run. An LLM analogue exists (partial structure worse than none in AoT, d10), but it is one figure.
8. Do separate-context sub-answers keep their faithfulness gain on current models and lose less accuracy? Can code recombination close the compositionality gap?
9. How should sub-problems be sized so each is solvable (Vermaas)? Is there a stopping rule that works without an environment reward (ADaPT self-judgement overstated WebShop success by over 30 points)?
10. Does the combine step (morphological matrix, r=0.233 and 0.293) add value that decomposition alone does not? One observational sample.
11. Does a single stored decomposition per task class (Self-Discover style) hold at equal tokens?
12. Is Atom of Thoughts' reported lift on reasoning models real? No replication.
13. How much does the choice of fine versus coarse grain (secondary vs tertiary vocabulary level) matter for LLMs? (K24, [C])

## 11. Sources

[V] = opened and read this session. [M] = search snippet or summary only. Where a [V] source was only an abstract page, it is noted.

Founding theory and design methods

- [V] Simon (1962) The architecture of complexity. https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf (a01-a05)
- [V] Parnas (1972) On the criteria to be used in decomposing systems into modules. https://www.win.tue.nl/~wstomv/edu/2ip30/references/criteria_for_modularization.pdf (a06-a08)
- [V] Ulrich (1995) The role of product architecture in the manufacturing firm. https://me.psu.edu/simpson/courses/me546/ulrich.RP95.prod-arch.pdf (a09, a10)
- [V] (abstract page only) Stone and Wood (1999/2000) Development of a functional basis for design. https://scholarsmine.mst.edu/mec_aereng_facwork/5683 (a11)
- [V] Hirtz, Stone, McAdams, Szykman, Wood (2002) A functional basis for engineering design (NIST TN 1447). https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=821676 (a12-a16)
- [V] Vermaas (2007) The functional modelling account of Stone and Wood: some critical remarks. https://www.designsociety.org/download-publication/25753/The+Functional+Modelling+Account+of+Stone+and+Wood:+Some+Critical+Remarks (a17-a20)
- [V] (abstract page only) Kurfman et al. (2003) Experimental studies assessing the repeatability of a functional modeling derivation method. https://scholarsmine.mst.edu/mec_aereng_facwork/5738 (a21, d04)
- [V] (abstract page only) Kurfman et al. (2001) Functional modeling experimental studies. https://scholarsmine.mst.edu/mec_aereng_facwork/5650 (a22)
- [M] Kurfman et al. (2000) Theoretical underpinnings of functional modeling: preliminary experimental studies. https://scholarsmine.mst.edu/mec_aereng_facwork/5673 (d15)
- [V] (abstract page only) Caldwell, Sen, Mocko, Summers (2010/2011) An empirical study of the expressiveness of the functional basis. https://www.cambridge.org/core/journals/ai-edam/article/an-empirical-study-of-the-expressiveness-of-the-functional-basis/1ED3460B25E3C6972849DA2E0B02B037 (a23)
- [V] (abstract page only) Sen, Caldwell, Summers, Mocko (2010) Evaluation of the functional basis using an information-theoretic approach. https://www.cambridge.org/core/journals/ai-edam/article/evaluation-of-the-functional-basis-using-an-information-theoretic-approach/ABACE590FEB78A2289B0A750C8982BD5 (a24)
- [V] (abstract only) Chandrasekaran (2005) Representing function. https://www.cambridge.org/core/product/identifier/S0890060405050079/type/journal_article (a25)
- [V] van Eck (2009) On relating functional modeling approaches. https://biblio.ugent.be/publication/5972925/file/5974181 (a26)
- [V] Gericke and Eisenbart (2017) The integrated function modeling framework and its relation to function structures. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BB9DF7B9461E4257E9EF2145C8AD30E3/S089006041700049Xa.pdf/the-integrated-function-modeling-framework-and-its-relation-to-function-structures.pdf (a27, a28)
- [V] (abstract page only) Erden et al. (2008) A review of function modeling. https://www.cambridge.org/core/journals/ai-edam/article/review-of-function-modeling-approaches-and-applications/8B6BC6B83D6E2AC4AA62BD9020E36848 (a30)
- [V] (abstract only) Van Eck, McAdams, Vermaas (2007) Functional decomposition: three models of functional reasoning compared. https://scholarsmine.mst.edu/mec_aereng_facwork/5841 (b15)

Human studies

- [V] Booth, Bhasin, Reid, Ramani (2015) Empirical studies of functional decomposition in early design. https://engineering.purdue.edu/cdesign/wp/wp-content/uploads/2015/08/IDETC2015-47865-Empirical-Studies-of-Functional-Decomposition-in-Early-Design.pdf (b01-b06; abstract page a29: https://pure.psu.edu/en/publications/empirical-studies-of-functional-decomposition-in-early-design/)
- [V] Booth, Reid, Ramani (2013) Understanding abstraction in design. https://engineering.purdue.edu/cdesign/wp/wp-content/uploads/2013/08/IDETC2013-13130.pdf (b07-b09)
- [V] (read by first agent; not re-opened by the checker) Linsey, Green, Van Wie, Wood, Stone (2005) Functional representations in conceptual design. https://peer.asee.org/14271 (b10, b11)
- [M] Atilola, Tomko, Linsey (2016) Design Studies 42:110-136. https://core.ac.uk/works/38533177 ; https://doi.org/10.1016/j.destud.2015.10.005 (b12, d05)
- [V] Atilola (2014/2015) PhD thesis, Georgia Tech, Study 3. https://repository.gatech.edu/entities/publication/bfa38752-1fe9-4cbb-afa7-e55784dec540 (d03)
- [V] (abstract only) Clemson dissertation, Function models, interaction models and pruned function models. https://open.clemson.edu/all_dissertations/875 (b13)
- [V] (abstract only) Exploring the impact of functional terms on idea generation in design (CIE 2018). https://pure.bit.edu.cn/en/publications/exploring-the-impact-of-functional-terms-on-idea-generation-in-de/ (b14)

LLM and AI studies

- [V] Massoudi and Fuge (2025) Agentic LLMs for conceptual systems engineering and design. https://arxiv.org/html/2507.08619v2 ; https://arxiv.org/pdf/2507.08619 (b16, b17, c01-c03)
- [M] Gap record, FBS prompting paper and MCTS summaries. https://arxiv.org/pdf/2507.08619 (b27)
- [V] Elhambakhsh, Grandi, Ko (2025) Domain adaptation of LLMs for classifying mechanical assembly components. https://arxiv.org/pdf/2505.01627 ; https://arxiv.org/html/2505.01627v1 (b18, c04)
- [V] Haddad and Seibel (2025) Functional decomposition of technical products based on LLMs and Monte Carlo tree search (ICED25). https://doi.org/10.1017/pds.2025.10205 ; https://fis.leuphana.de/en/publications/functional-decomposition-of-technical-products-based-on-large-lan/ (c05, c25, d01, d02, d14)
- [V] Rosenthal, Demke, Mantwill, Niggemann (2023/24) Plan-based derivation of general functional structures in product design. https://arxiv.org/abs/2302.04600 (c06, c07, c23)
- [V] Zhou et al. (2023) Least-to-most prompting. https://arxiv.org/pdf/2205.10625 ; https://arxiv.org/abs/2205.10625 (b19, b20, c08)
- [V] Wang et al. (2023) Plan-and-Solve prompting. https://arxiv.org/pdf/2305.04091 ; https://arxiv.org/abs/2305.04091 (b21, c22)
- [V] Khot et al. (2023) Decomposed prompting. https://arxiv.org/pdf/2210.02406 ; https://arxiv.org/html/2210.02406v2 (b22, c09)
- [V] Prasad et al. (2024) ADaPT. https://arxiv.org/abs/2311.05772 ; https://arxiv.org/html/2311.05772 (b23, b24, c10, c11)
- [V] Dziri et al. (2023) Faith and fate. https://arxiv.org/pdf/2305.18654 ; https://arxiv.org/html/2305.18654 (b25, c14)
- [V] Radhakrishnan et al. (2023) Question decomposition improves the faithfulness of model-generated reasoning. https://arxiv.org/pdf/2307.11768 ; https://arxiv.org/html/2307.11768 (b26, c21)
- [V] Press et al. (2023) Measuring and narrowing the compositionality gap. https://arxiv.org/html/2210.03350v3 (c12, c13)
- [V] (abstract page only) Cemri et al. (2025) Why do multi-agent LLM systems fail? (MAST). https://arxiv.org/abs/2503.13657 (c15)
- [V] Towards a science of scaling agent systems (2025). https://arxiv.org/html/2512.08296v3 (c16, c17)
- [V] Zelikman et al. (2023) Parsel. https://arxiv.org/html/2212.10561v3 (c18, c19)
- [V] Jiang et al. (2023) Self-planning code generation. https://arxiv.org/html/2303.06689 (c20)
- [V] Light et al. (2025) DISC. https://arxiv.org/abs/2502.16706 (d06)
- [V] Wang et al. (2024) PlanSearch. https://arxiv.org/abs/2409.03733 (d07)
- [V] Meincke, Mollick, Mollick, Shapiro (2025) The decreasing value of chain of thought in prompting. https://arxiv.org/abs/2506.07142 (d08)
- [V] Teng et al. (2025) Atom of Thoughts. https://arxiv.org/abs/2502.12018 (d09, d10)
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620 (d11)
- [V] Erdogan et al. (2025) Plan-and-Act. https://arxiv.org/abs/2503.09572 (d12)
- [M] Dual-CoT for small language models (arXiv 2604.25039). https://arxiv.org/pdf/2604.25039 (d13)

Cross-readings in the evidence files (c23, c24, c25) are the first agent's synthesis, not separate sources.

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 9 established claims: 5 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E07.02-K05** (reworded: the sources support less). Booth 2013 (26 students, n=78 trees, no method effect) and Booth 2015 study 2 (n=78, r=0.075, p=0.515) match, but Booth 2013 compares three decomposition methods with each other and measures functions, errors and abstraction levels, not idea count or design quality against a no-decomposition control; Booth 2015 study 2 is observational; the Linsey 2005 figures (n=54, 19.0 vs 19.7) could not be opened (ASEE page blocked; only an abstract saying function modelling was indistinguishable from control was reachable) and the quoted evidence line itself lists group sizes of 5 and 7. Corrected claim: In human studies, evidence that a functional decomposition step improves ideas or design quality is absent: a first controlled test (Linsey et al. 2005) reported no difference from a control group, a within-subject comparison of three decomposition methods (Booth 2013, 26 students) found no method effect on its measures, and an observational study of 78 industry reports (Booth 2015 study 2) found no correlation between using decomposition and design grade (r=0.075, p=0.515). All tests are small, observational or preliminary, so a small benefit is not excluded.
- **E07.02-K11** (reworded: the sources support less). GSM8K step-wise numbers, TextCraft depth 2 and 3 numbers and the kth-letter result all match, but the TextCraft numbers cited do not show a gain growing with depth: the absolute ADaPT gain shrinks from +51.3 points at depth 2 (26.9 to 78.2) to +36.9 at depth 3 (1.8 to 38.7), and the comparison is against ReAct, not chain of thought. Corrected claim: Decomposition helps more on longer problems in least-to-most (GSM8K 5+ steps 45.23 vs 39.07 for chain of thought) and in decomposed prompting (kth-letter concatenation stays near 100% while chain of thought falls with length), and was worse on 2-step GSM8K (74.53 vs 76.68); ADaPT still lifts TextCraft at depth 3 (ReAct 1.8 to 38.7) though its absolute gain is smaller than at depth 2 (26.9 to 78.2).
- **E07.02-K13** (number corrected). Plan-and-Solve numbers are mislabeled: in the PS paper's table 56.4/57.0/59.3 on GSM8K are Zero-shot-CoT/PoT/PS+; plain PS is 58.2 on GSM8K (+1.8 over CoT, not +0.6) and its six-dataset average is 72.9 (not 73.5, which is PoT). Least-to-most +1.5, self-planning pass@10 76.3 vs 75.0 and pass@1 60.3 vs 48.1, and the Meincke GPQA results (o4-mini +0.056 at one threshold, 20 to 80% more time) match; PS models were text-davinci-003, not strong models. Corrected claim: Plan-first prompting gives small gains over plain chain of thought (about 1 to 7 points; plain Plan-and-Solve +1.8 on GSM8K, 56.4 to 58.2, and PS+ +2.9; least-to-most +1.5 on GSM8K), mainly by cutting missing-step errors. Self-planning gains shrink with sampling: pass@10 is 76.3 vs 75.0 direct, against pass@1 60.3 vs 48.1. For reasoning models generic step-by-step prompting added almost nothing on GPQA Diamond (only o4-mini +5.6 points at one threshold) and cost 20 to 80% more time.
- **E07.02-K21** (reworded: the sources support less). Hirtz et al. (no measured benefit; repeatability study cited), Gericke and Eisenbart ('initial empirical evidence') and the Clemson abstract ('little experimental evidence' for ideation) match, but 'only repeatability and usage-frequency studies exist' is wider than the sources: Gericke cites further empirical studies (Caldwell 2011, Srinivasan 2012, Sen 2013) and the same dissertation and the Linsey and Booth experiments in this note are ideation experiments. Corrected claim: Evidence that function modelling helps designers is thin: the functional-basis authors report no measurement of benefit beyond a repeatability study, a 2017 review calls the empirical evidence for its benefits 'initial' (citing Kurfman, Caldwell, Srinivasan and Sen studies), and a Clemson dissertation abstract says there is little experimental evidence that function models help concept generation (the few experiments on it show no reliable gain).
- **E07.02-K08** (now single-source: only one opened source, code check).
