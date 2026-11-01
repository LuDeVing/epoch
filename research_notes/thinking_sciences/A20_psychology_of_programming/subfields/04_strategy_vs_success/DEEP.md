# Strategy vs success: deep document

*Subfield A20.04. Sources: evidence_a-d.jsonl (ids a01-a02, b01-b28, c01-c28, d01-d17), claims.jsonl (K01-K25), critique.md. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The question: when people (or models) debug unfamiliar code, does the way they search matter, or does what they already know matter more?

The founding study is Ko and Uttl (2003). It had 75 students debug a 4-bug Stata program in 20 minutes. The authors clustered the logged behaviour into three comprehension strategies. No strategy was clearly best. What tracked success on single bugs was bug-specific domain knowledge (statistics, math) and attitude.

A common summary says "no strategy was best, knowledge predicts success". The paper is more careful. The critique corrects the summary in several places (section 3.2). The headline is also single-source. The forward-citation check found 56 citing papers, none a replication, none an LLM test (d16).

Why it matters for our agent. An early draft of the schema leaned on strategy choice (depth-first vs breadth-first, a fixed scientific-debugging routine). This subfield says: procedure is a weak lever unless it brings new true information. Information means real output, tests, runtime values, the right file, or a relevant lesson. The 2023 to 2026 LLM literature mostly agrees (K06, K07, K08, K11, K17). But no study crosses strategy with information at equal tokens (K24). We must run that 2x2 ourselves.

Scope. We cover the human founding studies, their numbers, rivals, and every LLM or agent study found that tests or uses the idea. The LLM studies are analogies. None clusters model behaviour the way Ko and Uttl did with knowledge held fixed.

## 2. History and theories in depth

### 2.1 Roots: expert strategy in familiar systems

Earlier work (Gugerty and Olson; Nanja and Cook, cited in b07) found experts debug with better strategies in systems they know. Ko and Uttl say their result contradicts a pure expert-strategy view. They offer a hypothesis, not a tested contrast: strategy may matter more once the system is familiar. No familiar-vs-unfamiliar condition was run (b07, K19).

### 2.2 Ko's 2002 honors thesis

The thesis is the source of the 2003 paper (b08, b09, b10).
- 86 participants did two Stata tasks: write a program, then debug one.
- On the programming task, clusters predicted success. Cluster p1 (mostly CS majors) generated random numbers in 34 of 41 cases. p2 in 1 of 23. p3 in 3 of 11.
- On the debugging task, clusters did not predict success. They related only to major and to fixing the valueofoutlier bug.
- Conclusion: programming experience, intelligence and statistics competence "played no role" in predicting debugging success. The structure of the program was the gatekeeper.
- Three debugging styles: curious/distracted, hesitant/focused, active/focused. None did better. CS majors showed the same range as psychology majors.
- Those who inspected output first found more bugs. Few did.

The thesis is stronger on "strategy does not matter for debugging" and weaker on "domain knowledge matters". The 2003 paper adds per-bug knowledge results. Same data, different framing (K03, contested).

### 2.3 Ko and Uttl (2003)

Details in section 3. The authors' own cautions: 75 is small for clustering; comparing clusters on the measures that define them is dangerous; strategies depend on Stata-specific measures (b02, b25).

### 2.4 Field data on strategy and experience

Beller et al. (2018): 176 surveyed developers and 723 IDE sessions. Strategy choice (printf vs debugger) did not correlate with experience (b19; K16 [E] together with Ko). Neither study measures fix success in a manipulated design.

Alaboudi and LaToza (2021): live-streamed real work, 11 developers, 89 episodes. Hard bugs needed information gathering before the first edit (b20, K15).

### 2.5 The LLM line

Four lines of LLM work ask a version of the question.
1. Self-repair and self-correction: is a repair loop (procedure) worth its cost, or is feedback quality (information) the bottleneck? Olausson, Huang, Self-Debug (b11, b12, b13).
2. Human-method scaffolds: does copying a human debugging method help? AutoSD and LDB (b16, b18).
3. Fixed pipeline vs free agent: Agentless vs SWE-agent, then the 2025-26 leaderboard analyses (b14, b15, d12).
4. Information on/off: oracle files, requirements text, retrieved lessons, memorisation checks (c22, d02, d04, d05).

## 3. Core findings with exact numbers

### 3.1 Table

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Design of founding study | N=75 analysed of 86 recruited (11 dropped for poor English). 20 psychology, 24 CS, 31 other majors. 4 seeded bugs, Stata 7 do-file, 20 min, 10-min tutorial, think-aloud | Ko and Uttl 2003 (b01, b24) | [S] |
| Per-bug fix counts | 28 (37.3%), 29 (38.7%), 25 (33.3%), 16 (21.3%) of 75 for valueofoutlier, pvalue, for-loop, inverted axes | b01, critique | [S] |
| Three strategy clusters | n = 20 / 40 / 15. Ward's method on 132 behaviour measures (pooled into 22 groups) from over 33,000 coded actions | b02, c01 | [S] |
| Cluster names | c1 depth-first information seekers; c2 inactive spec-and-output readers; c3 breadth-first inspect-everything guess-and-check | b02 | [S] |
| Bugs fixed per cluster (0 to 4) | c1 1.00 (SD .97), c2 1.65 (.98), c3 2.00 (1.07). c2 and c3 > c1, p<.05. c2 vs c3 tie | b04, c02 | [S] |
| Cluster 1 best on one bug | valueofoutlier fixed by 13 of 20 (65%) in c1, 12 of 40 in c2, 3 of 15 in c3 (chi-square p<.01). Yet c1 worst overall | b04 | [S] |
| Strategy tracks background | Programming experience (0-7): c1 2.52, c2 1.20, c3 3.59 (p<.01). Cluster 2 had the least experience and still beat cluster 1 | b03 | [S] |
| Attitude by cluster | To experiment 4.89 / 4.68 / 5.53 (p<.01). To computers 5.65 / 4.76 / 5.98 | b03 | [S] |
| Per-bug knowledge, valueofoutlier | Fixed vs not: self-rated math 5.07 vs 3.91; computer attitude 5.49 vs 4.82 | b05 | [C] |
| Per-bug knowledge, inverted axes | Fixed vs not: statistics test .40 vs .31; math 5.48 vs 4.41; computer attitude 5.83 vs 5.08 | b05, c03 | [C] |
| Null for general ability | Problem-solving test .60 vs .59; vocabulary .52 vs .54 (first bug). Other three bugs: statistics test .31-.34 vs .31-.32 | b05, c03 | [C] |
| Output inspection | Reading the output graph separated fixers on inverted axes (fixed by 21.3%). In the thesis, output-first inspectors found more bugs; few did | b06, b10, c03 | [S] |
| Surface cue steering | A contradicting comment: valueofoutlier range bug found by nearly twice as many as the pvalue twin. Finding one often exposed the other | b06, c04 | [S] |
| Thesis, programming task | Clusters predicted success: p1 34 of 41, p2 1 of 23, p3 3 of 11 | b08 | [S] |
| Thesis, debugging task | Clusters did not predict success; experience, intelligence, statistics competence "played no role" | b09 | [C] |
| Field: strategy vs experience | 176 survey, 723 sessions (10.3 work years). Debugger in 9% of sessions; debugging under 14% of IDE time; no correlation of experience with debugger or test use | Beller 2018 (b19) | [E] with Ko |
| Hard real bugs need probing | 11 devs, 89 episodes. Long episodes (>=12.3 min, n=23): first edit at 3.2 min. Short (<1 min, n=23): first edit at 6 s. Reported defects 51 (+/-38) min, 5 of 10 unfixed; self-inserted 6 (+/-8) min, 14% unfixed | Alaboudi and LaToza 2021 (b20) | [S] |
| Self-repair with human feedback | GPT-4: 33.30% own feedback vs 52.60% human. Intro 42.64 vs 62.21; interview 19.33 vs 45.67; competition 3.67 vs 14.67. Own feedback inaccurate 32 of 80, human 7 of 80. 16 people, 40 programs | Olausson 2024 (b13, c07) | [E] |
| Self-repair at equal samples | GPT-4 on APPS up to 8% over no repair; GPT-3.5 marginal; up to 34% relative for GPT-3.5 on competition tasks. Stronger-model feedback lets weaker models beat their own self-repair | c05, c06 | [E] |
| Self-correction, no oracle | GPT-3.5 GSM8K 75.9 to 75.1 to 74.7; CommonSenseQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-4 HotpotQA 49 to 49 to 43 | Huang 2024 (b12, c08) | [E] |
| Self-correction, with oracle | GPT-3.5 GSM8K 84.3, CSQA 89.7, HotpotQA 29.0; GPT-4 GSM8K 97.5, CSQA 85.5, HotpotQA 59.0 | b12 | [E] |
| Feedback richness (Self-Debug) | TransCoder (Codex): 80.4 base, 89.3 simple, 91.6 unit tests, 92.5 tests plus explanation, 87.9 tests plus trace. MBPP (GPT-4): 72.8, 78.8, 80.6, 80.4, 80.2. Spider (Codex): 81.3, 81.3, 84.1 with explanation | Chen 2023 (b11, c23) | [E] |
| Real vs imagined debugger | AutoSD: 73% plausible patches with real debugger output vs 63% with model-imagined output | Kang 2023 (b16, c20) | [S] |
| Human method vs plain LLM | Defects4J v1.2: AutoSD 76 vs LLM-Base 87 correct. v2.0: 113 vs 110 | b16, c19 | [S] |
| Confidence signal | Plausible patches: 89% correct with <DONE> vs 82% without. With imagined debugger, <DONE> solutions 11 points less likely plausible | c20 | [S] |
| Explanations for humans | 20 participants, 12 bugs: accuracy higher with explanation on 5 of 6 real bugs, time about equal | c21 | [S] |
| Runtime values | LDB: up to 9.8% over baselines (HumanEval, MBPP, TransCoder; abstract figure) | Zhong 2024 (b18, c24) | [E] with Self-Debug and AutoSD |
| Bug class matters | DebugBench: 4,253 instances, 18 bug types; GPT-4 75.0%, GPT-3.5 62.1%. Runtime feedback helps syntax and reference bugs, not logic | Tian 2024 (b17, c16-c18) | [S] (Fig. 4 values unread) |
| Fixed pipeline on Lite | Agentless 32.00% (96/300) at $0.70; SWE-agent GPT-4o 18.33% at $1.62; SWE-agent Claude 3.5 Sonnet 23.00%; AutoCodeRover 19.00-21.67%; RAG baseline 2.67-4.33% | Xia 2024 (b14, c12) | [C] |
| Benchmark leakage | Exact patch in issue text 4.3% of Lite; misleading solution 5.0%. Lite-S: 84 resolved (33.73%) | c13, b23 | [S] |
| Interface changes result | SWE-agent GPT-4 Turbo 18.0% default; no edit command 10.3; iterative search 12.0; no search 15.7; summarized search 18.0; viewer 100 lines 18.0, 30 lines 14.3, whole file 12.7. Shell-only with demonstration 11.00% | Yang 2024 (b15, c10, c11) | [S] |
| Failed edits compound | 51.7% of runs had at least one failed edit. Chance of eventual success 90.5% overall, 57.2% after a failed edit | b15 | [S] |
| Oracle files | Claude 2: 1.96% with BM25 vs 4.8% with oracle files | Jimenez 2023 (c22) | [E] |
| Agents solve the same issues | 6 top agents: 404 of 500 solved by at least one, 181 by all, 96 by none. Best 64.6% | Meng 2024 (c14, d08) | [E] |
| Localisation tracks rank | Best system hit a buggy file in 448 cases vs 342 for lowest (31.0% more). Given a correct file: Learn-by-interact 281/342 = 82.2%, W&B 69.6% | c15, d08 | [S] |
| Requirements text | SWE-Bench Pro: GPT-5 25.9% with requirements plus interface vs 8.4% problem only; Opus 4.1 22.7% vs 8.2% | Deng 2025 (d05) | [E] with c22 |
| SWE-Bench Pro level | Public N=731: Sonnet 4.5 43.6, Sonnet 4 42.7, GPT-5 (high) 41.8, Haiku 4.5 39.5, Kimi K2 27.7, GPT-OSS-120B 16.2. Commercial N=276: best under 20% | d05 | [S] |
| Memorisation / repo familiarity | File path from issue text alone: up to 76% on Verified (60-76), 57-71% Full, 50-68% SWE-Repo, under 53% outside repositories. Five-gram overlap up to 35% on Verified | Liang 2025 (d04) | [S] |
| Retrieved lesson | SWE-Exp, DeepSeek-V3, Verified: 0 lessons 37.8%, 1 lesson 42.0%, 2 lessons 39.8%, 4 lessons 39.0%. Raw demos (no abstraction) 36.0. Claude 4 Sonnet 73.0 vs 66.6-71.6 baselines | Chen 2025 (d02, d03) | [S] |
| Misleading comments | CodeCrash, 17 LLMs, 1,279 questions: about 24% average relative drop (comments and prints each). With CoT still 13.8% | Lam 2025 (d06) | [S] |
| Guardrail as a sentence | GPT-4o direct: 64.5 vanilla, 45.7 misleading, 45.9 with "ignore comments". DeepSeek-V3 CoT: 92.1, 70.2, 82.1. GPT-4o CoT: 94.4, 87.5, 89.4. Refactor-first pass: 45.7 to 41.1 | d07 | [S] |
| Scaffold by model | SWE-Effi, 50 issues: SWE-Agent 28% with Qwen3-32B (35.5 calls, 440k input tokens) vs 10% with GPT-4o-mini (181 calls, 8.1M tokens). OpenHands 34% vs 11.9%. AutoCodeRover Qwen3-32B 38% with 14.7 calls | Fan 2025 (d09) | [S] |
| Model vs harness, rare DSL | BC-Bench, 101 tasks x 5 runs. Same model, two harnesses: opus-4.5 57.4 vs 58.4 (p=0.728); opus-4.6 68.5 vs 65.1 (p=0.075). Model change in one harness: 65.1 vs 59.8 (p=0.026); 60.8 vs 53.7 (p=0.019) | Sun and Hansen 2026 (d10) | [S] |
| Language gap | SWE-PolyBench, Sonnet 3.5: Python 20-24%, Java 11-16%, TypeScript 5-13%. Agentless edge was Python-only | Rashid 2025 (d11) | [S] |
| Retrieval for rare libraries | CodeRAG-Bench: ODEX-hard retrieved docs improve 20.3-40.1%; GPT-4o gold docs +27.4 points on SWE-Bench; retrieve-and-rerank +21, still 9 under gold | Wang 2024 (d14) | [S] |
| Fixed vs free on leaderboard | Verified: best fixed multi-agent workflow 75.2%; best autonomous single agent 73.2%. Kruskal-Wallis H=19.41, p=0.0070; fixed no-agent pipelines lower (Dunn p=0.0207, 0.0125, 0.0003). Lite: no group difference (p=0.0579) | Martinez and Franch 2026 (d12) | [C] |
| Backtracking search | SWE-Search on Lite: GPT-4o 25.7 to 31.0; GPT-4o-mini 13.0 to 17.0; Qwen-2.5-72B 18.0 to 24.7; DeepSeek-V2.5 16.3 to 21.0; Llama-3.1-70B 13.6 to 17.7; mean +23% relative. Free state transitions alone +1.4% | Antoniades 2025 (d13) | [S] |
| Agent trajectory anti-patterns | 120 trajectories (40 each from RepairAgent, AutoCodeRover, OpenHands), 2,822 iterations. RepairAgent failed runs 40 steps vs 22 successful. Misalignment OpenHands 0.5% vs 1.4%; AutoCodeRover 0% vs 4.8% | Bouzenia and Pradel 2025 (d01) | [S] |
| Failure shape | 52.0% of unresolved SWE-agent runs were wrong or over-specific implementations; unresolved ran 21 vs 12 steps. Multi-agent failures: design 41.8%, misalignment 36.9%, task verification 21.3% (1,600+ traces, kappa 0.88) | b27, c26 | [E] |
| Repro tests as filter | SWT-Bench: SWE-Agent precision on fixes passing its own reproducing tests more than doubled. Ideal ensemble of best four solves 71% more than best single | Mundler 2024 (d15) | [S] |
| Reflexion | HumanEval 91.0 vs GPT-4 80.1; Leetcode Hard 15.0 vs 7.5; MBPP 77.1 vs 80.1 (lower) | Shinn 2023 (c25) | [C] |

### 3.2 Corrections to the common summary

From the critique, checked against the paper text.
1. "No strategy was best" is a simplification. Clusters 2 and 3 beat cluster 1 (p<.05). Only 2 vs 3 is a tie.
2. "Depth-first did worst" holds only for the total. Cluster 1 was the most successful on valueofoutlier (65%, p<.01).
3. Cluster 2 had the least programming experience (1.20) and still beat cluster 1 (2.52). Experience does not map to success.
4. Cluster definition and outcome are partly circular. The same behaviour measures (for example time on one command) define clusters and separate fixers (b25).
5. Shell-only GPT-4 Turbo on Lite is 11.00% with demonstration (7.33% without). The earlier 7.33% claim was wrong.
6. Exact-patch leakage in Lite is 4.3% (text). The 3.0% chart value is not confirmed.

## 4. Mechanisms and models

These are mechanisms the evidence supports, not fitted formulas. Each is written so an engineer can build it.

### 4.1 Information versus procedure (the core model)

P(fix) depends mainly on the information available at the point of editing. Procedure decides how much of that information the run collects and uses.

- Information sources, strongest evidence first: (1) real execution output on the failing case; (2) the correct file or region; (3) issue text with requirements and interface; (4) a retrieved lesson for the bug class; (5) the model's own critique (weak).
- A procedure helps only if it raises the odds that one of these sources enters the context before the edit. A procedure that only rearranges what the model already knows adds little (AutoSD 76 vs 87; Olausson's cost-counted gains).
- Evidence: K06, K08, K11, K17. [E] for "information beats procedure" on 2023-24 models. The 2x2 that would prove it is missing (K24).

### 4.2 Oracle gap decomposition

Run one model in three conditions and read the gaps. A: own feedback. B: independent critic. C: oracle or human diagnosis.
- A to C is the value of better information (GPT-4: 33.30 to 52.60).
- A to B is the part a cheap second signal captures.
- Self-correction with no new evidence (Huang) is arm A with zero new information. It flips correct answers to wrong. Build a flip counter that logs every correct-to-wrong change.

### 4.3 Signal-gated revision

Revision is allowed only when new tool or test evidence has arrived since the last attempt. This matches G1 and G2. Evidence: Huang (oracle vs none), Self-Debug (tests vs no tests), AutoSD (real vs imagined debugger, 73% vs 63%).

Implementation: after each attempt, code checks a "new evidence" flag (new failing output, new test result, new file read). If false, skip the revise step and put the budget into a new sample or into S6.

### 4.4 Breadth versus depth as coverage control

Cluster 1 chased one command and fixed fewer bugs overall (1.00). SWE-agent's iterative search (inspect each hit one by one) did worse than no search (12.0 vs 15.7). Failed agent runs repeat identical actions (d01).

Mechanism: a fixation counter per hypothesis. Record each edit or probe against a suspect id. After k probes on one suspect with no new evidence, force a move to the next-ranked suspect. This is a test candidate, not a rule. The evidence is a similar shape in two systems, not one controlled link (K14, contested).

### 4.5 Output-first inspection

In humans, reading real output separated fixers on the bug that raised no error. Output-first inspectors in the thesis found more bugs, but few did.

Implementation: a pre-edit step that runs the program, prints the real output, and requires one line stating what the output shows against what the spec says. Only the human link exists (K04).

### 4.6 Surface-cue attention

A contradicting comment made one bug far more findable than its twin. CodeCrash measured the LLM side: misleading comments cut pass@1 about 24% relative. Mechanism: attention follows salient text, not truth. A sentence guardrail did nothing under direct inference (45.7 vs 45.9).

Candidate fix: an action guardrail. Before editing a site that carries a comment or docstring claim, run a check of the claim against behaviour. Untested (K05, K21).

### 4.7 Knowledge retrieval with a cap

One retrieved lesson helped (37.8 to 42.0). More lessons hurt (39.8, 39.0). Forcing the agent to cite the lesson was worse than plain context. Mechanism: a lesson is a prior that can overrule fresh evidence.

Implementation: at most one lesson per class, shown as plain context, never forced as a citation, dropped if the failing output contradicts it. SCHEMA section 5 already shows lessons after the first attempt. SWE-Exp showed its lesson before work. The order effect is unmeasured.

### 4.8 Stop-and-rediagnose trigger

After one failed edit, the chance of eventual success drops from 90.5% to 57.2% (SWE-agent). Unresolved runs ran longer (21 vs 12 steps). Structured backtracking gave +23% relative but with more calls.

Implementation: a failed-edit counter per item. At k failures, discard the current hypothesis, rerun localisation with the failure output added, and keep best-so-far (G6). The schema already has "at most 2 rounds, then S6". The open point is whether k=2 or k=3 beats continued editing at equal tokens (K25).

## 5. What holds up

### 5.1 Human side

- No replication exists. 56 citing papers in Semantic Scholar, none a replication (d16). Google Scholar was not checked. The DOI page (a01) and a 2020 ICPC paper (a02) were never opened.
- The founding result is one exploratory study: N=75, one task, one language, students, 20 minutes, seeded bugs, per-bug univariate tests with no correction, partly circular cluster measures.
- The thesis conflicts with the paper on whether knowledge matters (K03 contested).
- Supported by field data only on one side point: strategy does not map to experience (K16 [E], Beller 2018).
- Ko's own boundary: strategy predicted success when writing new code, not when debugging (b08, K19).

### 5.2 LLM side: solid

- External signal beats self-opinion. Five or more sources: Huang, Olausson, Self-Debug, AutoSD, LDB. [E]
- Diagnosis quality bottlenecks repair. Human diagnosis lifted GPT-4 from 33.30 to 52.60. [E]
- Information handed in dominates. Oracle files more than doubled Claude 2. Requirements text tripled GPT-5 on Pro (25.9 vs 8.4). Six top agents solve mostly the same issues. [E]
- Failure is wrong diagnosis and weak verification more than strategy choice (b27, c26, d09). [E]

### 5.3 LLM side: contested

- Fixed pipeline vs free agent. Agentless won on Lite in 2024 (32.00% at $0.70 vs 18.33% at $1.62). With strong models the gap faded: 75.2% (fixed workflow) vs 73.2% (free single agent) on the Verified leaderboard. Fixed no-agent pipelines are significantly lower. Agentless failed on multi-file edits in SWE-Bench Pro. Its SWE-PolyBench edge was Python-only (d05, d11, d12). Leaderboard data is observational and not leak-filtered. K10 and K23 are [C].
- Rivals to the Agentless result: leaked or misleading issue text (4.3% and 5.0%), base-model strength, and the authors building the filtered set themselves (b23).
- Reflexion: gain on HumanEval, loss on MBPP. Huang attributes such gains to oracle signals.
- Backtracking: +23% relative, but at higher call cost, so not equal tokens.

### 5.4 Interventions that worked

- Real execution feedback (Self-Debug TransCoder 80.4 to 91.6).
- Real debugger output over imagined (73% vs 63%).
- Compact tool output (100-line viewer 18.0 vs whole file 12.7) and a purpose-built edit command (18.0 vs 10.3).
- Independent or stronger-model feedback (b13, c06).
- One retrieved lesson (+4.2 points).
- Reproducing tests as a filter on finished patches (precision more than doubled).

### 5.5 Interventions that did not work

- Self-critique with no new evidence (Huang).
- A sentence telling the model to ignore comments (45.9 vs 45.7).
- A refactor-first pass (45.7 to 41.1).
- Forcing a human method with no new information (AutoSD 76 vs 87 on v1.2).
- Many lessons (4 lessons 39.0 vs 1 lesson 42.0).
- Iterative one-by-one search (12.0 vs 15.7 with no search).
- Adding a trace to unit tests in Self-Debug (87.9 vs 91.6 on TransCoder).

### 5.6 Moderators

- Bug class: runtime traces help syntax and reference bugs, not logic bugs (K13 [S]; Fig. 4 values unread).
- Feedback availability: Self-Debug's large gains need tests. Olausson's modest gains come from counting total samples.
- Difficulty: the human-feedback gap widens with difficulty (42.64 vs 62.21 intro; 3.67 vs 14.67 competition).
- Language rarity: Python 20-24% vs TypeScript 5-13%; retrieval helps most on rare libraries.
- Model strength: strong models shrink the fixed-pipeline advantage.

## 6. Language models

### 6.1 No LLM replication of the cluster analysis

No 2020 to 2026 study clusters LLM debugging behaviour into strategies, holds knowledge fixed, and relates clusters to outcome (c28, d17). The nearest:
- Bouzenia and Pradel (2025): 120 trajectories, action n-grams, anti-patterns. Successful runs balance exploring, explaining and validating. Failed runs repeat identical actions and fix without testing. Agent identity confounds it (three agents, 40 runs each, different built-in procedures).
- SWE-Bench Pro: an LLM judge clusters failure modes from the last 20 turns.

### 6.2 How models behave

- Self-correction without a signal lowers accuracy (GPT-4 GSM8K 95.5 to 89.0). Most harm is correct answers being changed.
- Self-feedback is poor: GPT-4's own feedback was inaccurate in 32 of 80 cases, human in 7 of 80.
- With oracle or human signal the loop works.
- Models follow salient text. Misleading comments cut 17 LLMs by about 24% relative. Reasoning models spend 2 to 3 times more tokens on plausible wrong hints. CoT recovers some (DeepSeek-V3 70.2 to 82.1).
- Models name the buggy file from issue text alone up to 76% on Verified vs under 53% outside, so benchmark scores mix repo knowledge with procedure.
- Failed runs cost more. GPT-4o-mini under SWE-Agent used 181 calls and 8.1M tokens for 10%.

### 6.3 What changed results, by how much

| Change | Size |
|---|---|
| Human diagnosis instead of own (GPT-4 repair) | +19.3 points (33.30 to 52.60) |
| Requirements and interface added (GPT-5, Pro) | +17.5 points (8.4 to 25.9) |
| Oracle files (Claude 2) | 1.96 to 4.8 |
| Unit-test feedback (TransCoder, Codex) | +11.2 (80.4 to 91.6) |
| Real vs imagined debugger (AutoSD) | +10 points plausible (73 vs 63) |
| Edit command removed (SWE-agent) | -7.7 (18.0 to 10.3) |
| Whole-file viewer | -5.3 (18.0 to 12.7) |
| One retrieved lesson | +4.2 (37.8 to 42.0) |
| Backtracking search | +23% relative, at higher cost |
| Same model, two commercial harnesses (rare DSL) | no difference at 0.05 (p=0.728, 0.075) |
| Model upgrade inside one harness (rare DSL) | +5.3 and +7.1 points, p=0.026 and 0.019 |
| Human method, no new information (AutoSD) | -11 on v1.2, +3 on v2.0 |

### 6.4 Coverage gap

Most evidence is 2023 to 2024 models. The 2025 to 2026 sources are SWE-Bench Pro, SWE-Exp, BC-Bench, SWE-Effi, CodeCrash and the leaderboard analysis. No study crosses strategy with information on one model at equal tokens (K24). We do not know whether the 2023 pattern holds for current models.

## 7. What our agent should take

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Prefer new real information over a new procedure. Spend budget on real output, the correct file or region, or requirements text before editing | G2, S5 | [E] | K06, K08, K11; b11, b13, c22, d05 |
| A2 | Revision needs new evidence. A revise step runs only after new tool or test output; otherwise skip it. Log correct-to-wrong flips | G1, G2, S5 | [E] | K07; b12, c08, c09 |
| A3 | Diagnosis comes from code-located failing output, not the model's own critique (self-feedback inaccurate in 32 of 80) | G2, S5 | [E] | K06; b13, c07 |
| A4 | Execution results come from code, never from the model imagining them | G2, G10 | [E] | K08; b16, c20 |
| A5 | Cap tool output: compact viewer, structured edit tool, summarised search | tool layer (O) | [S] on one agent, consistent across studies; keep as design rule | K12; b15, c10 |
| A6 | Do not copy "expert strategy" as a prior. Strategy follows habit and background. Test candidate strategies as arms | G7 | [E] (two human sources, no manipulation) | K16; b03, b19 |
| A7 | Failures come from wrong diagnosis and weak verification. Put weight on the final check (S8), not on strategy variety | S8, G3 | [E] | K17; b27, c26 |
| A8 | Count samples and setup cost in every comparison | G7 | [E] | K06; c05 |

### 7.2 Test first (not yet established)

| # | Item | Schema part | Status | Evidence | Test |
|---|---|---|---|---|---|
| T1 | 2x2: fixed vs free procedure x information on/off, equal tokens | all | [S] (no prior study) | K24, K18 | Test 1 |
| T2 | Fixed locate-fix-validate vs free agent with a strong model | S | [C] | K10, K23; b14, d12 | Test 2 |
| T3 | One retrieved bug-class lesson only; before vs after first attempt | memory | [S] | K20; d02, d03 | Test 3 |
| T4 | Output inspection before the first edit | S5 | [S] human only | K04; b06, b10 | Test 4 |
| T5 | Fixation cap and round-robin over top suspects | S5, S6 | [C] | K14; b04, c11, d01 | Test 5 |
| T6 | Stop-and-rediagnose after k failed edits | S5, S6, G1 | [S] | K25; b15, d13 | Test 6 |
| T7 | Action guardrail for misleading comments | G | [S] | K05, K21; d06, d07 | Test 7 |
| T8 | Bug-class routing of feedback | O | [S] | K13; b17, c17 | Test 8 |
| T9 | Hypothesis-prediction-experiment format | O | [S] | K09; b16 | Test 9 |
| T10 | Strategy effect grows with familiarity | S0 gate | [S] | K19; d04, d10, d11 | Test 10 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup cost counted, G7). Report confidence intervals. Use leak-filtered or post-cutoff items where possible (d04, c13). Add a flip counter (correct-to-wrong changes) wherever there is a revise step.

1. **The 2x2 (decisive).**
   - Items: debug or repair items with real failing output available.
   - Arms: fixed locate-fix-validate vs free action choice, each with information on (real execution output plus retrieved lesson or correct file) vs off. Same model, same token cap.
   - Metric: fix rate; read the interaction term.
   - Expected: information effect large (several points up to tens of points), strategy effect small, interaction positive (strategy matters more with information on, per the Self-Debug pattern).
2. **Fixed pipeline vs free agent, strong model.**
   - Items: leak-filtered, including multi-file items.
   - Metric: fix rate with CI.
   - Expected: within about 2 points on single-file items (leaderboard); fixed route worse on multi-file.
3. **Lesson store.**
   - Arms: 0, 1, 2 lessons, and one deliberately wrong lesson; lesson before vs after first attempt.
   - Metric: fix rate; rate at which the wrong lesson is followed.
   - Expected: 1 lesson +3 to +4 points; 2 lessons less; wrong lesson loses points unless dropped on contradicting output.
4. **Output inspection first.**
   - Items: bugs that raise no error (silent wrong output).
   - Arms: forced inspect step before first edit vs edit allowed first.
   - Metric: fix rate on those items; tokens to fix.
   - Expected: gain on silent bugs only; null elsewhere.
5. **Fixation cap.**
   - Items: multi-bug items and items with a decoy suspect.
   - Arms: cap of k probes per suspect with round-robin vs unlimited depth.
   - Metric: bugs fixed per item.
   - Expected: gain on multi-bug items; small loss on single-cause items (cluster 1 was best on one bug).
6. **Stop-and-rediagnose.**
   - Arms: trigger after k=2 and k=3 failed edits vs continue editing.
   - Metric: fix rate and tokens on failed items.
   - Expected: modest gain, given the 90.5% to 57.2% drop after a failed edit.
7. **Misleading-comment guardrail.**
   - Items: a misleading comment next to the true bug and next to a decoy.
   - Arms: none; sentence guardrail; action guardrail (check the claim against behaviour).
   - Metric: first-edit-at-commented-site rate; fix rate.
   - Expected: sentence guardrail null (45.7 vs 45.9); action guardrail cuts steering.
8. **Bug-class routing.**
   - Items: labelled syntax, reference, logic.
   - Arms: uniform trace feedback vs class-routed feedback.
   - Metric: fix rate by class.
   - Expected: routing helps on logic items.
9. **Scientific-debugging format.**
   - Arms: hypothesis-prediction-experiment vs free-form, real execution in both.
   - Metric: fix rate; precision of the done signal.
   - Expected: no accuracy gain (AutoSD); possible calibration gain.
10. **Familiarity.**
    - Arms: strategy arms on common-language items vs rare-language or unseen-API items.
    - Metric: strategy effect size by stratum.
    - Expected: Ko and Uttl predict a larger strategy effect when familiar. The model evidence hints the reverse: information dominates when unfamiliar.

## 9. What does not transfer, and why

- **The cluster result itself.** Human clusters came from Stata-specific behaviour (time on a command, help use) with think-aloud. A model has no equivalent. Trajectory n-grams are a different construct.
- **Experience and attitude.** Predictors of human fixing (math 5.07 vs 3.91, computer attitude) have no model counterpart. Model "knowledge" is parametric repo or library knowledge (d04), probed through memorisation checks.
- **20 minutes and fatigue.** The human time limit and think-aloud load do not exist for a model. Token budget is the analogue.
- **Seeded bugs.** Seeded bugs are not natural. DebugBench bugs are implanted by GPT-4 (b17). Real bugs differ: half of reported defects were unfixed in live work (b20).
- **Novice sample.** 31 of 75 were "other majors", 20 were psychology. Expert effects in familiar systems may differ.
- **Attitude as motivation.** Attitude to the experiment (4.89 / 4.68 / 5.53) is motivation. For a model, prompt-level equivalents ("be careful") were found not to work (SCHEMA 4b).
- **Leaderboard data.** Cross-system comparisons mix model, scaffold, spend and cherry-picked runs (d12). They cannot isolate strategy.
- **Cost accounting.** Several agent results compare unequal calls (SWE-Search uses many more). Do not carry them into equal-token claims.
- **Reasoning, not code.** Huang's self-correction numbers are on reasoning tasks. Carry the direction, not the sizes.

## 10. Open questions

1. Does strategy matter more once the system is familiar? Nobody varied strategy across familiarity.
2. Does a fixed route still beat a free agent for a strong model on a controlled, leak-filtered set at equal tokens?
3. Does output-first inspection raise fix rates for silent bugs in models?
4. Does a failure-count trigger beat continued editing at equal tokens?
5. What does a deliberately wrong retrieved lesson cost, and does showing it before or after the first attempt change that?
6. Do misleading comments steer first-edit location in repair tasks, and does an action guardrail work?
7. Does bug class moderate feedback usefulness at current model strength? (Fig. 4 values unread.)
8. Is the human domain-knowledge finding real? The thesis and paper disagree and nobody replicated it.
9. Does trajectory clustering with agent identity held fixed show strategy effects?
10. Do 2025-2026 frontier models still show the 2023 pattern (self-correction without a signal hurts)?
11. Did the forward-citation check miss replications? Google Scholar was not checked.

## 11. Sources

[V] = opened and read this run. [M] = snippet or metadata only.

- [V] Ko and Uttl (2003) Individual differences in program comprehension strategies in unfamiliar programming systems. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/Ko'03.pdf (b01-b07, b24, b25, c01-c04)
- [M] Ko and Uttl (2003), DOI page, paywalled. https://doi.org/10.1109/wpc.2003.1199201 (a01)
- [M] Graduate computing students and an unfamiliar programming language (ICPC 2020), title match only. https://doi.org/10.1145/3387904.3389274 (a02)
- [V] Ko (2002) Honors thesis: Individual differences in programming, testing and debugging strategies. https://faculty.washington.edu/ajko/papers/Ko2002HonorsThesis.pdf (b08-b10)
- [V] Beller et al. (2018) On the dichotomy of debugging behavior among programmers. https://www.spinellis.gr/pubs/conf/2018-ICSE-debugging-analysis/html/B (b19, b28)
- [V] Alaboudi and LaToza (2021) An exploratory study of debugging episodes (read through a summarising tool). https://ar5iv.arxiv.org/html/2105.02162 (b20)
- [V] Chen et al. (2023) Teaching large language models to self-debug. https://arxiv.org/abs/2304.05128 (b11, b26, c23)
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b12, c08, c09)
- [V] Olausson et al. (2024) Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896 (b13, c05-c07)
- [V] Xia et al. (2024) Agentless. https://arxiv.org/abs/2407.01489 (b14, b23, c12, c13)
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/abs/2405.15793 (b15, b27, c10, c11)
- [V] Kang et al. (2023) Explainable automated debugging via LLM-driven scientific debugging (AutoSD). https://arxiv.org/abs/2304.02195 (b16, c19-c21)
- [V, Fig. 4 unread] Tian et al. (2024) DebugBench. https://arxiv.org/abs/2401.04621 (b17, c16-c18)
- [V, abstract and parts] Zhong et al. (2024) LDB. https://arxiv.org/abs/2402.16906 (b18, c24)
- [V] Jimenez et al. (2023) SWE-bench. https://arxiv.org/abs/2310.06770 (c22)
- [V] Meng et al. (2024) LLM-based agents for automated bug fixing: how far are we? https://arxiv.org/abs/2411.10213 (c14, c15, d08)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c25)
- [V] Cemri et al. (2025) Why do multi-agent LLM systems fail? https://arxiv.org/abs/2503.13657 (c26)
- [V] Bouzenia and Pradel (2025) Understanding software engineering agents. https://arxiv.org/abs/2506.18824 (d01)
- [V] Chen et al. (2025) SWE-Exp. https://arxiv.org/abs/2507.23361 (d02, d03)
- [V] Liang, Garg and Moghaddam (2025) The SWE-Bench Illusion. https://arxiv.org/abs/2506.12286 (d04)
- [V] Deng et al. (2025) SWE-Bench Pro. https://arxiv.org/abs/2509.16941 (d05)
- [V] Lam et al. (2025) CodeCrash. https://arxiv.org/abs/2504.14119 (d06, d07)
- [V] Fan et al. (2025) SWE-Effi. https://arxiv.org/abs/2509.09853 (d09)
- [V] Sun and Hansen (2026) BC-Bench. https://arxiv.org/abs/2608.20851 (d10)
- [V] Rashid et al. (2025) SWE-PolyBench. https://arxiv.org/abs/2504.08703 (d11)
- [V] Martinez and Franch (2026) Dissecting the SWE-Bench leaderboards. https://arxiv.org/abs/2506.17208 (d12)
- [V] Antoniades et al. (2025) SWE-Search. https://arxiv.org/abs/2410.20285 (d13)
- [V] Wang et al. (2024) CodeRAG-Bench. https://arxiv.org/abs/2406.14497 (d14)
- [V, exact precision values not extracted] Mundler et al. (2024) SWT-Bench. https://arxiv.org/abs/2406.12952 (d15)
- [V, citing-paper titles only] Semantic Scholar citation graph of Ko and Uttl (2003). https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/WPC.2003.1199201 (d16)
- [M] Absence check for a strategy x information 2x2. https://arxiv.org/abs/2509.09853 (d17, b21, c28; absence of evidence, searches limited by quota)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 4 established claims: 3 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A20.04-K16** (reworded: the sources support less). Beller et al. found no correlation between experience and use of an IDE debugger or tests, but Ko and Uttl found comprehension strategies WERE related to programming experience (and not to success), so the two do not agree on experience; the b28 synthesis is the same Beller PDF listed twice. Corrected claim: Beller et al. (176 developers surveyed, 723 IDE sessions) found no correlation between developer experience and use of an IDE debugger or unit tests for debugging, with printf debugging common; Ko and Uttl (2003, lab study) found that three comprehension strategies were related to programming experience but no strategy gave better debugging performance (domain knowledge of the bug and computer attitudes predicted success). Both suggest strategy choice is not the main driver of debugging success, but they differ on whether strategy tracks experience. Neither manipulated strategy experimentally.
- **A20.04-K06** (now single-source: only one opened source, code check).
- **A20.04-K07** (now single-source: only one opened source, code check).
