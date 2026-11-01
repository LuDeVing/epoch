# Fault localisation and repair: deep document

*Subfield E09.07. Key works: Jones and Harrold (Tarantula), Le Goues (GenProg and repair). Built from evidence_a-d.jsonl (a01-a29, b01-b30, c01-c29, d01-d17), claims.jsonl (K01-K26) and critique.md. The cross-check re-opened the LLM-paper numbers. The numbers for Parnin and Orso, Xia 2016, Qi 2015, Pearson 2017, LLM4FL and FlexFL come from earlier agents and were not re-opened.*

## 1. What it is

Fault localisation (FL) answers: which code is wrong? Automated program repair (APR) answers: what edit fixes it? They chain. A repair tool needs a place to edit. A debugger needs a suspect list.

Three FL signal families exist.
- **Spectrum-based (SBFL).** Run the tests. Record which statements each test runs. Statements run mostly by failing tests are suspicious. Tarantula, Ochiai, DStar and the Wong family are scoring formulas on this table.
- **Mutation-based (MBFL).** Mutate a statement. If failing tests start to pass, or passing tests start to fail, the statement is likely involved. Metallaxis is an example. It is precise on some faults and costly.
- **Learning and LLM-based.** A model reads the failing test, error log and code. It either scores lines (LLMAO) or navigates the repo with tools (AutoFL, AgentFL, LocAgent).

Repair has two eras. Search-based repair (GenProg) mutates code under an FL prior and accepts anything that passes the tests. LLM repair prompts a model with buggy code and failing output, then loops.

Why it matters for our agent: guardrail G2 says revise only from real output, and code locates that output. FL is the code that locates. This subfield asks how well locating works, when a suspect list helps or hurts, and what to do after the fault is found.

Scope: human debugging strategy (Gugerty and Olson, hypothesis testing) belongs to other E09 subfields. Only human studies that test ranked fault lists appear here.

## 2. History and theories in depth

### 2.1 Tarantula and the spectrum idea (2002-2009)
Jones and Harrold built Tarantula. Each statement gets X/(X+Y). X is the share of failing tests that run the statement. Y is the share of passing tests that run it. [a01] In the Siemens-suite study, Tarantula examined less code before the first faulty statement than set union, set intersection, nearest neighbour and cause transitions. [a01] Wong et al. added a diminishing-returns principle: the first failing test covering a line counts more than the second, and so on; the same for passing tests. [a04] Ochiai is a later similar formula (background, not opened here).

Known weak spots from the 2009 survey:
- **Coincidental correctness.** A faulty line can run in a passing test by luck. Ball et al. missed the fault in 3 of 15 cases for this reason. Tarantula gets worse when this is frequent. [a02]
- **Missing code.** Spectra point at executed code. They cannot point at code that is absent. [a03]

### 2.2 Search-based repair (GenProg, 2009)
Weimer, Nguyen, Le Goues and Forrest used FL as a search prior. Statements run only by the failing test got weight 1.0. Statements also run by passing tests got a lower weight (WPath). Mutation and crossover then edit weighted statements until all tests pass. [a05]
- Ten C programs, 63,000 lines, under 200 s on average, success 59%, 36.9 fitness evaluations on average. Final patch about 4 lines after minimisation by tree differencing and delta debugging. [a05, a07]
- Success did not depend on fault type (infinite loops 54%, buffer overruns 61%). It fell as weighted path length grew. [a06]

### 2.3 The overfitting correction (2015)
Qi, Long, Achour and Rinard re-checked GenProg, RSRepair and AE by hand. GenProg was reported to fix 55 of 105 defects. A correct patch existed for only 2 of 105. RSRepair was correct for 2 of 24, AE for 3 of 105. For 37 of the 55 GenProg defects, none of the reported patches passed the tests when re-run. [b12] Most plausible patches (those that pass the tests) equal one deletion: 104 of 110 for GenProg, 37 of 44 for RSRepair, 22 of 27 for AE. A system that only deletes (Kali) did at least as well. [b13] Lesson: "passes the tests" is not "correct". This is the root of the plausible vs correct split and of our G3.

### 2.4 Do ranked lists help humans? (2011 and 2016)
Parnin and Orso: two programs (Tetris, NanoXML), 34 graduate students, with and without a Tarantula-style list. [b01]
- No overall speed gain on Tetris: 12:42 vs 14:14 min, not significant. Only high performers (N=10) were faster on the easy task (p<0.05). [b01]
- The tool did not help more on the harder task. [b02]
- Moving the faulty line up or down the list did not change time clearly (10 new participants; NanoXML rank 16 vs 83, yet the rank-16 group was slower, 18:30 vs 15:12). [b03]
- People did not read the list top to bottom: 37% of visits jumped more than one position; 10.3 direction changes per person. [b04]
- Seeing the faulty line did not mean understanding it. Of 10 who clicked it, 9 kept inspecting about 10 more minutes, 61% of their time. [b05]

Xia, Bao, Lo and Li (2016): 36 professionals, 16 real Defects4J bugs, about 80 recorded hours. [b06]
- Time to root cause: 11.38 min (accurate tool, bug in top 5), 16.35 (mediocre, rank 6-10), 26.45 (no tool). Success 98%, 94%, 77%. [b06, b07]
- Accurate vs mediocre was significant (Wilcoxon p=0.0015). Rank mattered, which conflicts with Parnin and Orso's third hypothesis. [b08]
- 23 of 24 tool users did the same: open the top suspects, set breakpoints, run the failing test in a debugger, inspect variables. [b09]

The two studies differ in participants, bugs, tool and design. No clean replication exists. Status: contested.

### 2.5 Artificial faults are a weak proxy (2017)
Pearson et al. replicated 10 literature claims on spectrum and mutation FL, with 2,995 artificial faults (mutants) built from 310 real faults, in six Defects4J programs. On artificial faults 7 claims held statistically but only 3 had non-negligible effect, and results did not carry over to real faults. [b10] A hybrid (mutation plus spectrum) put the real fault in the top 5 in 36% of best-case and 23% of average-case runs. Best single rivals: Metallaxis 29% best case, DStar 30% best case. [b11]

### 2.6 Pre-trained models and LLM repair (2022-2024)
Xia, Wei and Zhang tested nine code models (125M to 20B, no fine-tuning) on five datasets and three languages. They beat older tools; larger was better; code after the buggy line (infilling) helped. On Defects4J 1.2, InCoder 6.7B with 2,000 samples and templates fixed 78 bugs, 32 more than the best prior. [b14, a18] Of 354 fixes, 234 (66%) differed from the developer patch. [a18]

Conversational repair: give ChatGPT the failing test output, then after each failed patch give the new failure and the earlier attempt. 114 correct on Defects4J 1.2, 48 on 2.0, 162 of 337 at about $0.42 per bug. [a19, c23] Sobania et al., 40 QuixBugs Python bugs: ChatGPT 19, Codex 21, CoCoNuT 19; one hint (the expected output) raised ChatGPT to 31. [c25]

### 2.7 LLM localisation and agents (2023-2025)
- **Prompted FL.** Wu et al.: ChatGPT-4 with the failing-test error log reached mean Top-1 23.13 vs SmartFL 15.75 (+46.9%) at function level. [a14, c10]
- **Test-free FL.** LLMAO fine-tunes small adapters on a frozen code model to score lines with no tests. [a16]
- **Tool-using FL.** AutoFL lets the model browse the repo through functions. [a11, c01] AgentFL splits the work into comprehension, navigation and confirmation. [a17]
- **Repair agents.** RepairAgent (state machine plus tools), AutoCodeRover (code search over classes and methods), SWE-agent (custom interface), Agentless (no loop). [a20, a23, a27, a24]
- **Benchmark.** SWE-bench: 2,294 issues, 12 Python repos. Claude 2 with BM25 retrieval solved 1.96%. [a26]

### 2.8 The audit phase (2024-2026)
Benchmarks were then audited for leaks, weak tests and contamination (section 5). The arc repeats GenProg: a headline gain is checked and shrinks.

## 3. Core findings with exact numbers

Status: E established (two or more independent papers), S single source, C contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Test-passing repair overfits | GenProg reported 55/105; correct 2/105; 104 of 110 plausible = one deletion | Qi 2015 [b12, b13] | E (K01) |
| Ranked lists and human speed | Tetris 12:42 vs 14:14, n.s., N=34; vs 11.38 vs 26.45 min, 36 professionals | Parnin 2011 [b01]; Xia 2016 [b06] | C (K02) |
| List accuracy moderates human benefit | Accurate 11.38 min / 98%; mediocre 16.35 / 94%; none 26.45 / 77% | Xia 2016 [b06-b08] | S (K03) |
| Humans skip around and over-inspect | 37% of visits jump; 10.3 direction changes; 61% of time after the hit | Parnin 2011 [b04, b05] | S (K04) |
| Artificial faults mislead evaluation | 2,995 mutants vs 310 real; 7 of 10 claims hold on mutants, 3 with real effect; hybrid top-5 36% best / 23% average | Pearson 2017 [b10, b11] | S (K05) |
| LLM with tools beats Ochiai at Top-1 | +19.7% Defects4J (353 bugs); +166.7% BugsInPy (GPT-3.5); +233.3% (GPT-4) | AutoFL [a11, b18] | S (K06) |
| Independent LLM systems beat Ochiai | LLMAO 22.3% vs 4.8% (395 bugs); GPT-4 with log 23.13 vs 15.75; AgentFL 157/395; FlexFL 164 vs Ochiai 122 (v1.2 subset) | [a14, a16, a17, c16] | E (K07) |
| Failing-test error log is the key context | Removing log: Top-1 -25.6%; removing test-failure analysis in AgentFL: 157 to 125 (-20%); FuseFL test results alone 187 vs Ochiai scores alone 169 (324 faults) | [c10, c08, d01] | E (K08) |
| Big context hurts LLM FL | Class level Top-1 49.9% below SmartFL (56 classes) | Wu 2023 [c11] | S |
| Rerun agreement predicts correctness | Spearman 0.57 / 0.52 with Precision@1, 5 reruns, p<0.0001 | AutoFL [c03] | S (K09) |
| General code confidence is poorly calibrated | ECE 0.09 to 0.73; token prob above 90% passed 52% | Spiess 2024 [d11] | S |
| Hierarchical localisation helps | Agentless file hit 81.7% (prompt 78.7, embedding 67.7); LLM4FL -23.24% without Division, -16.51% without CodeNav, -11.31% without Reflexion | [a24, c14, c26] | E (K10) |
| Localisation helps repair but is not enough | File hit 90.0% yet 23.67% solved; given a file hit, resolve 82.2% vs 69.6% | [b24, d05] | E (K11) |
| Realistic FL lowers repair | 21 to 16 bugs (-25%), cost +81% (100-bug subset) | RepairAgent [c21, c22] | S |
| Reproduction tests are noisy | 213 of 300 reproduce the issue; 94 pass the true patch | Agentless [c27] | S (K12) |
| Self-repair gain is small at equal samples | 1.05x pass@20 baseline; 0.97x for 2 samples + 10 repairs | Olausson 2024 [a28] | S (K13) |
| Feedback quality limits self-repair | Human feedback 52.60% vs GPT-4 33.30% overall | [a29] | S |
| Serial vs parallel spend similar at equal cost | Coverage similar after a few iterations; 57.4% resolved at about $2,300 | CodeMonkeys [d12] | S |
| Benchmark memorisation | File path from issue alone: 76% Verified vs 53% outside; Defects4J 80% of repos in TheStack; renaming cuts repair 4.1-16.0 points | [b28, d03, d04] | E (K14, K22) |
| Weak benchmarks inflate scores | 63.75% of 251 SWE-agent patches suspicious; 12.47% fell to 3.97% | SWE-Bench+ [b26] | S |
| Plausible patches differ from developer fix | 7.8% fail full developer tests; absolute drop 4.5% on Verified | [b27] | S |
| Industry gap | Human-reported: 25.6% plausible, 17.9% valid; machine-reported 73% / 43% | Rondon 2025 [b29] | S (K15) |
| Wrong-file edits drive human-reported failures | 3.5% (human-reported) vs 53.8% (machine-reported) still edit the correct file | [b30] | S |
| Issue quality separates solved from unsolved | Solution in report 1.95x; symbol location 1.30x; reproduction example 1.01x | Meng 2025 [d06] | S |
| Conversation with failing output beats resampling | 162/337 at $0.42; one hint lifts 19 to 31 of 40 | [a19, c25] | E (K16) |
| Failed runs are longer | RepairAgent 40 vs 22 iterations; write-fix calls 17 vs 6; OpenHands 54 vs 25 rounds to cover 80% | [a20, d08, d16] | E (K17, K23) |
| Overthinking tracks failure | Slopes -7.9 (reasoning), -15.9 (non-reasoning); lower-overthinking sample +30% resolution, -43% cost | Cuadron 2025 [d07] | S |
| Hypothesis-experiment prompt does not raise accuracy | v1.2: 87 base vs 76 AutoSD; v2.0: 110 vs 113; ARHE 177 vs 187 correct; real execution 73% vs 63% plausible | Kang 2023 [d09, d10] | C (K18) |
| LLM fault explanations unreliable | 300 explanations: 20% accurate; 26.3% hold an inaccurate statement; 46.7% bland; 56.7% of bugs had at least one accurate | AutoFL [c04] | C (K18) |
| Multi-file faults defeat tools | Single-file 55-58% vs OpenHands multi-file 25.3% | Liu 2025 [d14] | S (K24) |
| Spectrum hint adds a little to an LLM | +3.7% Top-1 over CoT (169 vs 163); +0.4 to +4.3 points on 3,902 Codeflaws bugs | [d01, d02] | S (K21) |
| File-level scan is cheap | 92.6% gold-file recall at 128k, at 14.6% of spend | [d13] | S (K26) |
| Test-free fine-tuned FL | UniXcoder 50.6% Top-1 of 1,291; LLMAO unseen projects 31.9% | [c18, b22] | E (K19) |

## 4. Mechanisms and models

### 4.1 Spectrum scoring
Build a matrix: for each statement s and test t, did t run s. Let ef(s) = failing tests that run s, ep(s) = passing tests that run s, F and P = total failing and passing tests.
- Tarantula: (ef/F) / ((ef/F) + (ep/P)). [a01]
- Ochiai: ef / sqrt(F * (ef + ep)). (Background formula.)
- Rank by score. Ties need a rule: worst case, average or best. Pearson reports best-case and average-case top-N because ties matter. [b11]
- Do not treat a passing test touching a line as clearing it. [a02] It cannot find missing code. [a03]

### 4.2 Mutation-based scoring
For each candidate statement apply mutants. A statement is suspicious if mutating it flips failing tests to passing, or breaks passing tests in a pattern like the real fault. Costly: the suite runs once per mutant. Pearson's hybrid of mutation and spectrum did best, with a small gain over the best single technique. [b11]

### 4.3 Search-based repair
Pick a statement with probability proportional to its FL weight (1.0 on the failing-only path, WPath on the shared path). Mutate by delete, insert from the same program, or replace. Run tests. Repeat. Minimise the winner with delta debugging. [a05, a07] Weakness: no semantic check beyond the tests, so deletions win. [b13]

### 4.4 Hierarchical LLM localisation (Agentless)
Step 1: show the repo tree and the issue; the model names files. Add embedding retrieval and combine (81.7% file hit). Step 2: for each file show a skeleton (signatures, class headers); the model names classes and functions. Context falls from over 3,000 to under 800 lines. Step 3: show those bodies; the model names edit lines. File-to-line directly was worse. Whole files cost more than skeletons. [a24, a25, c26]

### 4.5 Tool-using localisation (AutoFL, AgentFL)
Functions given to the model: list covered classes, list covered methods of a class, show a method body, show comments. Mean 5.37 calls per bug. [c01] The model searched longer on hard bugs (0.6 to 0.9 extra calls when the fault was in neither test nor stack trace). [c02] Run five times and count how often each method is named; agreement is the confidence. [c03] AgentFL adds test-behaviour tracking, document-guided search and confirmation, at $0.074 and 97 s per bug. [c07] Ablation on 395 bugs, Top-1: full 157; without test behaviour analysis 148; without method documentation 133; without test failure analysis 125. [c08]

### 4.6 Coverage-group division with re-ranking (LLM4FL)
Sort covered methods into groups by suspiciousness. Agent one works one group at a time. Agent two navigates the call graph. Agent three re-ranks in a Reflexion-style loop. Top-1 327 of 675 on Defects4J v2.0; without Division 251; without CodeNav 273; without Reflexion 290. [c13, c14] A non-LLM learning method (DepGraph) was still higher at Top-1 (359). [c13]

### 4.7 Two-stage candidate shrinking (FlexFL)
Non-LLM tools shrink the candidate list. The LLM agent then double-checks. A Llama3-8B version beat GPT-3.5 agents (Top-1/3/5 350/478/529 on v2.0). [c16] On 28 post-cutoff GHRB bugs it got 19 at Top-1. [c17]

### 4.8 Graph-guided localisation (LocAgent)
Parse the repo into a graph (files, classes, functions, imports, calls, inheritance). The agent does multi-hop search. SWE-bench Lite file Acc@1: BM25 38.69; CodeRankEmbed 52.55; Agentless GPT-4o 67.15; OpenHands Claude-3.5 70.80; LocAgent Claude-3.5 75.91. [c28]

### 4.9 Repair loop on located failing output
Prompt with the buggy function. Run tests. On failure, append the failing test name, message, failing line and previous patch. Cap attempts. Adding test name and message raised plausible patches over the base prompt's 58. [c23] RepairAgent adds a state machine (understand, gather ingredients, validate) and memory. Removing search tools halved fixes and doubled cost; removing the state machine cut fixes and raised cost; one-cycle-only memory made it repeat commands and use wrong names. [c21, a22]

### 4.10 Hypothesis-experiment loop (AutoSD)
Model writes a hypothesis, runs a debugger command, reads the result, writes a conclusion. Repeat until a DONE token, then patch. With a real debugger 73% of runs gave a plausible patch; with imagined output 63%. DONE raised plausibility 12.4 points with real execution and lowered it 11 points with hallucinated execution. [d10] Accuracy did not beat plain prompting; the value is the explanation. [d09]

## 5. What holds up

### Holds up
- **Error log and failing test are the strongest context.** Three ablations agree: -25.6% [c10], -20% [c08], test results 187 vs Ochiai 169 [d01]. K08 established.
- **LLM FL beats Ochiai at Top-1.** Four independent systems [a14, a16, a17, c16]. The gap shrinks at Top-10 (LLM4FL 494 vs 413, +20%, against +169% at Top-1). [c15] Always state the cutoff.
- **Hierarchical narrowing.** Agentless and LLM4FL ablations agree. K10 established.
- **Plausible is not correct.** Qi 2015 has not been refuted; later work reports both. K01 established.
- **Localisation is necessary, not sufficient.** The 90% file hit with 23.67% solved [b24] and the 82.2% vs 69.6% case [d05] agree. K11 established.
- **Feedback beats resampling the same prompt** for repair. K16 established.

### Contested or failed
- **Do ranked lists help humans?** Parnin and Orso (null) vs Xia 2016 (large effect). Neither replicated. Likely moderators: list accuracy, participant skill, bug difficulty. Xia's mediocre arm still beat no tool; Parnin's list did not. K02 contested.
- **Explanations.** AutoSD gained explanation, not accuracy. AutoFL explanations are accurate 20% of the time. [d09, c04] Against that, 20 participants judged patches better on 5 of 6 bugs with explanations, at the same time. [b17]
- **FlexFL reran AgentFL and got 144 vs 157.** Different subset and model version, so weak evidence, but published LLM-FL numbers move. [c09]
- **GenProg "59%" vs 2 of 105.** A difference in what "fix" means, not in arithmetic. [a05, b12]
- **AutoFL 87 s vs SBFL 112 s** compares across papers and hardware. Do not use. [a12, b19]

### Benchmarks are inflated
- SWE-bench: of 251 resolved SWE-agent patches, 32.67% had the solution leaked and 31.08% passed on weak tests; score fell 12.47% to 3.97%. [b26] About 3.0% of SWE-bench Lite show the exact patch in the description; the filtered Lite-S (249 of 300) changed the ranking only a little. [b25]
- Verified: 7.8% of plausible patches fail all developer tests. [b27]
- Memorisation: file path from issue text alone up to 76% on Verified vs 53% elsewhere. [b28] Defects4J: 80% of repos in TheStack; codegen-multi 6B has 82% 5-gram accuracy. [d03]
- Meaning-preserving edits cut Defects4J repair: Claude-3.7 77.31 to 72.42; GPT-4o 65.93 to 61.92; GPT-4o-mini 57.17 to 51.36; Gemma-2-27B 44.38 to 36.07; Llama-3.1 35.08 to 19.11 (all p<0.001). On post-cutoff GitBug-Java no significant drop for Claude-3.7 (+0.27, p=0.819) or GPT-4o (+1.76, p=0.667). [d04] This is repair with the function given, not localisation.
- Top-1 across benchmarks is not comparable: Defects4J v1.0 (353), v1.2 (395), v2.0 (675 in LLM4FL), function vs line level, with or without tests. [critique]

### Interventions that worked
Error log in prompt; hierarchical narrowing; skeleton in place of full file; real execution in the loop; reruns for confidence; a supervisor agent (22.2% of previously failed issues resolved) [d16]; picking the lower-overthinking sample (+30% resolution, -43% cost) [d07]; a human or stronger-model critic (33.30% to 52.60%) [a29].

### Interventions that did not
Self-repair at equal samples (1.05x) [a28]; AutoSD over plain prompting at 10 samples [d09]; more model size for fine-tuned FL [c18]; spectrum hint over CoT (small, +3.7%) [d01]; repeated identical searches [d08].

### Failure modes after a fault is found
Two opposite ones: stopping with no valid test, and looping. [d08, d16] OpenHands failures need 54 rounds to cover 80% vs 25 for successes. Flawed reasoning (keyword fixation) is about 65% of root causes. [d15] Multi-file faults are the clearest unsolved class. [d14]

## 6. Language models

### 6.1 Localisation
- **Prompt-only, function in context.** GPT-4 with log: Top-1 mean 23.13. GPT-3.5 origin 13.60, with log 14.67. GPT-4 origin 15.93. [a14] Class level Top-1 fell 49.9% below SmartFL. [c11]
- **Run-to-run variance.** GPT-3.5 origin 77-89 Top-1 hits per run; GPT-4 with log 135-145. [a15] Variance of Top-1 averaged 12.00% for GPT-4 with log. [c12] This is why AutoFL reruns five times.
- **Tool use.** AutoFL: +19.7%, +166.7%, +233.3%. Test-GPT3.5 without function use was worse at every k. [c05] GPT-3.5 lagged SBFL at acc@3 and above. [b18] One GPT-4 run beat five merged GPT-3.5 runs. [b19]
- **Agents.** AgentFL 157/183/187; LLM4FL 327/425/473/494 of 675; FlexFL 350/478/529; LocAgent file Acc@1 75.91. [c07, c13, c16, c28]
- **Test-free line scorers.** LLMAO 16B 22.3/37.7/46.3 vs Ochiai 4.8/16.5/25.1; unseen projects 31.9% Top-1; BugsInPy 10.3% Top-1. A 6-layer model from scratch got 1.3%, so pre-training is essential. [b21, b22]
- **Memorised locations.** Up to 76% file-path hit from issue text alone on Verified. [b28] No localisation-only test exists for Defects4J. [critique]
- **Small models.** Llama3-8B in FlexFL found 39 Top-1 bugs GPT-3.5 missed; GPT-3.5 stopped searching earlier (2.82 vs 4.56 second-stage calls). [c17]
- **Brute force.** Scanning every file with an LLM kept the gold files in a 128k context for 92.6% of Verified issues, at 14.6% of spend. [d13]

### 6.2 Repair
- Pre-trained models, no fine-tuning, beat older tools. [b14]
- ChatGPT conversation: 162/337 at $0.42. [a19] RepairAgent: 164/835, 270,000 tokens (14 cents) per bug, 35 tool calls; 39 bugs no baseline fixed; GitBug-Java 19 plausible and 13 correct; only 4 of 81 multi-location bugs fixed. [c20]
- AutoCodeRover on SWE-bench Lite: 19.00% (57) at about $0.43; with SBFL 66 tasks (about 22%); 7 tasks only the SBFL run solved. [a23]
- Agentless: 32.00% (96 of 300) at $0.70. [a24] SWE-agent + GPT-4 Turbo: 12.47% of 2,294. [a27]
- Industry: Passerine on Google bugs, 25.6% plausible (human-reported), 73% (machine-reported). [b29]
- Token cost varies a lot: AutoCodeRover 23K, RepairAgent 220K, OpenHands 1.2M tokens per task (52x). [d08]

### 6.3 What changed results, and by how much
| Change | Effect |
|---|---|
| Failing-test error log | Removing it: -25.6% Top-1 [c10] |
| Function-call tools | +19.7% to +233% Top-1 over Ochiai [a11] |
| Hierarchical narrowing | Removing it: -23.24% Top-1 [c14] |
| Five reruns merged | GPT-4 single run = GPT-3.5 x5 [b19] |
| Spectrum hint on top of CoT | +3.7% (GPT-3.5, students) [d01]; +0.4 to +4.3 points (Codeflaws) [d02] |
| Real over imagined execution | 73% vs 63% plausible [d10] |
| Self-repair at equal samples | 1.05x [a28] |
| Stronger critic feedback | 33.30% to 52.60% [a29] |
| Realistic instead of oracle FL | -25% fixes, +81% cost [c22] |
| Expected-output hint | 19 to 31 of 40 [c25] |
| Supervisor agent | 22.2% of failed issues resolved [d16] |
| Lower-overthinking sample | +30% resolution, -43% cost [d07] |
| Identifier renaming (Defects4J repair) | -4.1 to -16.0 points [d04] |

### 6.4 Calibration
AutoFL's rerun agreement correlates with correctness (0.57, 0.52). [c03] Spiess found general code confidence poorly calibrated (ECE 0.09 to 0.73). [d11] Gate on reruns or execution, not on the model's stated confidence. A DONE token helped only with a real debugger. [d10]

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **Locate from the failing output, by code.** Pass the failing test name, message, failing line and stack trace verbatim. Largest single prompt effect. Schema: G2, S4/S5. [E] c10, c08, d01, a19, c25 (K08, K16).
2. **Hierarchical localisation.** File, then class or function, then lines; skeletons not whole files. Schema: S1/S5, operator (decompose). [E] a24, a25, c26, c14 (K10).
3. **Two scores: plausible and correct.** A visible-test pass is not a fix; require the held-out check. Schema: G3, S4/S7. [E] b12, b13 (K01).
4. **Localisation is necessary, not sufficient.** Budget tokens for both; do not stop at a correct file. Schema: G7, S0. [E] b24, d05, c22 (K11).
5. **Evaluate on contamination-free bugs.** Post-cutoff or identifier-renamed items; report both. Schema: G7, G11. [E] b26, b28, d03, d04 (K14, K22).
6. **Feedback from real execution, not imagination.** Schema: G2, G10. [E] d10 with a28, a29 (K16; K18 partly).
7. **Detect repeats and cap rounds.** Repeated-identical-action detector triggers S6; keep a round cap. Schema: G1, S6. [E] d08, d16, a20 (K17, K23). The value 25 comes from one agent family; test it (U5).

### Test first
1. **Spectrum hint in the prompt.** Small gain on students and Codeflaws, never at equal tokens, never for repo-scale agents. Schema: operator (tool), S5. [S] d01, d02, a23 (K21).
2. **Hint-accuracy dose-response (anchoring).** Accurate vs mediocre vs wrong vs none. Schema: S1 input hygiene, G1. [C] b06-b08 vs b01-b03 (K02, K03); no LLM study.
3. **Rerun agreement as a gate for extra search.** Schema: G1, G5. [S] c03 vs d11 (K09).
4. **Never clear a line because a passing test touches it** in any suspect ranking built in code. Schema: G2. [S] a02, a03 (K20).
5. **Reproduction-test generation plus filter.** Schema: S4, G3. [S] c27 (K12).
6. **Re-localise after N failed patches vs N more samples.** Schema: S6. [S] d12, d16 (K25).
7. **Hypothesis-experiment prompt with real execution.** Gain is explanation, not accuracy. Schema: operator (hypothesis test). [C] d09, d10, c04 (K18).
8. **Stop on confirmed cause.** Humans kept inspecting 61% extra; agents unmeasured. Schema: S8, G7. [S] b05 (K04).
9. **Coupled-file enumeration after the first fix.** Schema: S5/S8. [S] d14, d15 (K24).
10. **File-level brute scan, then symbol-level spend.** Schema: S0/S1, G12. [S] d13 (K26).
11. **Stronger blind critic for feedback.** Schema: G5. [S] a29, a28 (K13).
12. **Issue clarification for noisy reports.** Schema: S1. [S] d06, b29, b30 (K15).
13. **Graph-guided retrieval for large repos.** Schema: memory/tools. [S] c28.

## 8. Concrete tests on our bench

All arms get the same token budget. Report tokens, Top-1/3/5 for localisation, plausible and correct for repair, with bootstrap intervals over items. Use post-cutoff or private bugs and add an identifier-renamed copy of one public subset.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 80 bugs with failing test | (a) failing output only; (b) + Ochiai top-5; (c) + degraded list (fault at rank 6-10); (d) + wrong list (fault absent) | Top-1/3, tokens to root cause, correct rate | (b) +0 to +4 points over (a) [d01, d02]; (c) near (a); (d) below (a) if anchoring exists |
| T2 | Same bugs | Flat vs hierarchical localisation prompt | Top-1, tokens | Hierarchical better, order of 10-20% Top-1 [c14, a25] |
| T3 | 50 bugs | Repair judged on visible tests only vs held-out check | Plausible and correct rates | Gap of 5-15 points [b13] |
| T4 | 60 bugs, 5 reruns | Gate: rerun when agreement under 3 of 5; always 1 run; always 5 runs | Top-1 per token | Gate matches 5-run accuracy at about half the tokens if rho near 0.5 [c03] |
| T5 | 60 bugs failing after 3 patches | (a) N more samples; (b) re-localise then N/2 samples; (c) (b) + coupled-file enumeration | Solved fraction | Untested; hypothesis (b) beats (a) by 5+ points [d12] |
| T6 | 40 multi-file bugs | With vs without coupled-file enumeration | Multi-file resolve rate | +5 to +10 points from the 25.3% baseline [d14] |
| T7 | 50 bugs | Real vs simulated execution in hypothesis loop | Plausible and correct rate | 73% vs 63% plausible [d10] |
| T8 | 60 bugs | Verify-once-and-stop vs unconstrained | Tokens after first correct fix; final correctness; premature stops | Fewer tokens, same correctness [d08] |
| T9 | Same bugs, original vs renamed identifiers | Localisation only | Top-1 drop | Memorisation gap; small for frontier models [d04] |
| T10 | 40 noisy-report bugs | Raw report vs agent-written clarification | Resolve rate | Gain only if solution quality is the bottleneck [d06] |
| T11 | 60 bugs | File scan then symbol checks vs agent-style search | Top-1 symbol per token | Scan saves tokens [d13] |

## 9. What does not transfer, and why

- **Human list-following results.** Humans treat a ranked list as a queue, zigzag and over-inspect. [b04, b05] An agent reads the whole list at once. The accuracy effect may carry over; the behaviour does not.
- **Search-based repair (GenProg).** It needs thousands of fitness evaluations [a05]; we have a few model calls. Only the lessons (overfitting, deletion) transfer.
- **Training-based FL (LLMAO, UniXcoder, DeepFL).** We do not train. K19 is low priority. [b21, c18]
- **Mutation-based FL.** Costly in test runs. An agent can run a few targeted experiments instead. Pearson's hybrid gain was small. [b11]
- **Defects4J numbers.** Likely memorised, Java, pre-cutoff. [d03, d04] Do not copy Top-1 figures as targets.
- **Student-code results (FuseFL, Codeflaws).** Small programs with strong tests. [d01, d02]
- **Industrial gap.** One study, Gemini 1.5 Pro, Google tracker bugs. [b29]
- **Cost figures.** Dollars, seconds and tool calls differ across papers. Equal-token studies are rare. [critique]

## 10. Open questions

1. Does a spectrum hint help, harm or do nothing for a tool-using agent at equal tokens? No study isolates it (K21).
2. Does an inaccurate suspect list anchor an LLM agent? No LLM study varies list accuracy. Liu et al. saw keyword fixation. [d15]
3. How much of Defects4J localisation is memorised? Repair-side tests exist; localisation-only tests do not. [d03, d04]
4. After the fault is found, do agents over-verify or under-verify? Both failure modes appear; extra checking after the fault is located is unmeasured. [d08, d16]
5. Can rerun agreement or stated confidence gate extra search, given the calibration warning? [c03, d11]
6. When does re-localising beat resampling at matched tokens? [d12, d17]
7. Which scaffold step fixes multi-file and missing-code faults? RepairAgent fixed 4 of 81 multi-location bugs. [c20, d14]
8. Does test-free localisation add anything once an error log exists? [d13, d01]
9. How much of the industrial gap is report quality and how much is localisation? [d06, b30]
10. Do hypothesis-then-experiment prompts help at equal tokens with real execution? Accuracy was equal at 10 samples; a token-matched run is missing. [d09]
11. Why do Parnin and Orso and Xia et al. disagree? Tool accuracy, skill and task are confounded; no replication.

## 11. Sources

[V] opened and read. [M] snippet only. Some [V] rest on earlier agents (see header note).

- [V] Wong and Debroy (2009), A Survey of Software Fault Localization. http://www.utdallas.edu/~ewong/fault-localization-survey.pdf (a01-a04)
- [V] Weimer, Nguyen, Le Goues, Forrest (2009), Automatically Finding Patches Using Genetic Programming. https://web.eecs.umich.edu/~weimerw/p/weimer-icse2009-genprog.pdf (a05-a07)
- [M] Qi, Long, Achour, Rinard (2015), Is the cure worse than the disease? https://doi.org/10.1145/2786805.2786825 (a08; confirmed by b12)
- [V] Qi, Long, Achour, Rinard (2015), An analysis of patch plausibility and correctness. https://people.csail.mit.edu/rinard/paper/issta15.pdf (b12, b13)
- [M] Pearson et al. (2017), DOI record. https://doi.org/10.1109/ICSE.2017.62 (a09)
- [V] Pearson et al. (2017), Evaluating and improving fault localization. https://homes.cs.washington.edu/~mernst/pubs/fault-localization-icse2017.pdf (b10, b11)
- [M] Parnin and Orso (2011), DOI record. https://doi.org/10.1145/2001420.2001445 (a10)
- [V] Parnin and Orso (2011), full text. https://web.eecs.umich.edu/~weimerw/2018-481/readings/debugging-helping.pdf (b01-b05)
- [V] Xia, Bao, Lo, Li (2016), Automated debugging considered harmful considered harmful. https://baolingfeng.github.io/papers/ICSMEmain.pdf (b06-b09)
- [V] Kang, An, Yoo (2024), AutoFL. https://arxiv.org/abs/2308.05487 (a11-a13, b18-b20, c01-c05); [M] preliminary-result snippet (c06)
- [V] Wu et al. (2023), LLMs in Fault Localization. https://arxiv.org/abs/2308.15276 (a14, a15, c10-c12)
- [V] Yang, Le Goues, Martins, Hellendoorn (2024), LLMAO. https://arxiv.org/abs/2310.01726 (a16, b21, b22, c19)
- [V] Qin et al. (2025), AgentFL. https://arxiv.org/abs/2403.16362 (a17, c07, c08)
- [V] Xu et al. (2025), FlexFL. https://arxiv.org/abs/2411.10714 (c09, c16, c17)
- [V] Rafi et al. (2025), LLM4FL. https://arxiv.org/abs/2409.13642 (c13-c15)
- [V] Ji et al. (2024), Impact of LLMs of Code on Fault Localization. https://arxiv.org/abs/2408.09657 (c18)
- [V] Chen, Tang, Deng et al. (2025), LocAgent. https://arxiv.org/abs/2503.09089 (c28, c29)
- [V] Xia, Wei, Zhang (2023), Practical Program Repair in the Era of Large Pre-trained Language Models. https://arxiv.org/abs/2210.14179 (a18, b14, c24)
- [V] Xia and Zhang (2024), Keep the Conversation Going. https://arxiv.org/abs/2304.00385 (a19, c23)
- [V] Bouzenia, Devanbu, Pradel (2024/2025), RepairAgent. https://arxiv.org/abs/2403.17134 (a20-a22, c20-c22)
- [V] Zhang et al. (2024), AutoCodeRover. https://arxiv.org/abs/2404.05427 (a23)
- [V] Xia, Deng, Dunn, Zhang (2024), Agentless. https://arxiv.org/abs/2407.01489 (a24, a25, b23-b25, c26, c27)
- [V] Jimenez et al. (2024), SWE-bench. https://arxiv.org/abs/2310.06770 (a26)
- [V] Yang et al. (2024), SWE-agent. https://arxiv.org/abs/2405.15793 (a27)
- [V] Olausson et al. (2024), Is Self-Repair a Silver Bullet for Code Generation? https://arxiv.org/abs/2306.09896 (a28, a29)
- [V] Kang, Chen, Yoo, Lou (2023), AutoSD. https://arxiv.org/abs/2304.02195 (b15-b17, d09, d10)
- [V] Aleithan et al. (2024), SWE-Bench+. https://arxiv.org/abs/2410.06992 (b26)
- [V] Wang, Pradel, Liu (2025), Are solved issues in SWE-bench really solved correctly? https://arxiv.org/abs/2503.15223 (b27)
- [V] Liang, Garg, Moghaddam (2025), The SWE-Bench illusion. https://arxiv.org/abs/2506.12286 (b28)
- [V] Rondon et al. (2025), Evaluating agent-based program repair at Google. https://arxiv.org/abs/2501.07531 (b29, b30)
- [V] Sobania et al. (2023), An Analysis of the Automatic Bug Fixing Performance of ChatGPT. https://arxiv.org/abs/2301.08653 (c25)
- [V] Widyasari et al. (2024), FuseFL. https://arxiv.org/abs/2403.10507 (d01)
- [V] Farzandway and Ghassemi (2025), Automated Repair of C Programs Using LLMs. https://arxiv.org/abs/2509.01947 (d02)
- [V] Ramos et al. (2025), Are LLMs Memorizing Bug Benchmarks? https://arxiv.org/abs/2411.13323 (d03)
- [V] De Koning et al. (2026), Metamorphic testing to diagnose memorisation. https://arxiv.org/abs/2604.21579 (d04)
- [V] Meng et al. (2025), LLM-based Agents for Automated Bug Fixing: How Far Are We? https://arxiv.org/abs/2411.10213 (d05, d06)
- [V] Cuadron et al. (2025), The Danger of Overthinking. https://arxiv.org/abs/2502.08235 (d07)
- [V] Bouzenia and Pradel (2025), Understanding Software Engineering Agents. https://arxiv.org/abs/2506.18824 (d08)
- [V] Spiess et al. (2024), Calibration and Correctness of Language Models for Code. https://arxiv.org/abs/2402.02047 (d11)
- [V] Ehrlich et al. (2025), CodeMonkeys. https://arxiv.org/abs/2501.14723 (d12, d13)
- [V] Liu et al. (2025), An Empirical Study on Failures in Automated Issue Solving. https://arxiv.org/abs/2509.13941 (d14-d16)
- [M] Antoniades et al. (2025), SWE-Search. https://arxiv.org/abs/2410.20285 (d17; abstract level only)
