# Debugging strategies: deep document

*Subfield A20.01, psychology of programming. Sources: evidence_a-d.jsonl (a01-a31, b01-b31, c01-c25, d01-d17), claims.jsonl (A20.01-K01 to K26), critique.md. Numbers were re-checked against primary text where the critique says so. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Debugging is the work of going from "the program does the wrong thing" to "the program is fixed and we know it is fixed". Psychology of programming studies how people do this. Vessey (1985) gave the classic breakdown into goals:

- Strategic goals: (1) determine the problem, (2) gain familiarity with the program's function and structure, (3) explore structure and execution, (4) repair the error.
- Tactical goals inside repair: locate the error, then repair it, then confirm the repair.
- Operational goals: the single actions (read a module, compare output with expected output, trace a variable, edit a line, rerun).

Why it matters for our agent: state S5 REVISE. The schema says S5 shows the failing output, names what is wrong in one line, then fixes. The debugging literature asks a sharper question. Should the agent locate the fault as a separate step before it patches, and how good must that location be for the step to pay?

Short answer from this review. Locating the fault is the hard part for people and for models. Models fix well when told where. But for strong 2026 agents, a self-made or tool-made location adds little, while a stated cause helps more. Real execution output is the one ingredient that is solidly established. Everything about goal order is weakly supported.

Scope note. Overlaps with other subfields in this run (impasse-driven subgoaling, spectrum-based fault localisation, self-consistency, cognitive models of troubleshooting, human error and recovery) are only linked here, not covered.

## 2. History and theories in depth

**Gould (1975)** [M]. Early experiments on how people debug. N=10, 12 listings. Median debug time about 7 min. 11% of listings had the bug not found. Assignment-statement bugs were about 3 times harder to find than array or interaction bugs. Only a snippet was read (b07). Gould noted some programmers read source before looking at output.

**Shapiro (1983)** [M]. Algorithmic program debugging: an AI debugger finds the faulty clause by asking an oracle whether sub-results are right. A divide-and-conquer on the computation tree. Background only (c23).

**Vessey (1985)** [V]. The founding process analysis (a01-a10, b01-b06). 16 professional programmers from one state government computer centre, 8 experts and 8 novices, thinking aloud while debugging one COBOL sales-report program with one logic bug. Two versions: a high-level bug (line 299, branch-change flag not reset) and a low-level bug (line 308, customer-change flag not reset), 4 experts and 4 novices per version. Protocols were cut into episodes, then strategy diagrams, then a process model.

- Experts vs novices were classified after the fact, by "chunking": whether the person grouped the program into meaningful units. This ex post label explained 73.7% of variance in debug time. Manager ratings explained 36.1%. Only 10 of 16 subjects got the same class from both methods.
- All 16 protocols fit five building blocks: problem determination, gain familiarity, explore, evaluate a hypothesis, repair. Goals 1 (determine) and 4 (repair) appear in every protocol. Goals 2 and 3 vary a lot. Repair is last "except when subjects make errors".
- Strategy paths come from four binary factors: program vs output first, active vs passive examination, constrained by a hypothesis or not, system view or not. 16 paths are possible; the subjects followed 6.
- Novices were more often constrained by their own early hypothesis. Experts kept more options open and kept a system view.

**Gugerty and Olson (1986/87)** [M] and **Katz and Anderson (1987)** [M]. Contemporaneous studies of skilled vs novice debugging and of bug-location strategies. Only abstracts or secondary summaries were seen (a11, a12, b08, b09). The secondary summary says experts and novices distributed activities in the same way in Gugerty and Olson, which would cut against a pure strategy-difference story. Not verified.

**Parnin and Orso (2011)** [V]. Do ranked suspect lists from automated fault localisation help? Mostly no (a14, a15, b10-b12). **Xia, Bao, Lo and Li (2016)** [V] re-ran the question with professionals and found large gains (b13, b14). This is the main live dispute in the human literature.

**Ko and Myers (2008)** [V]. The Whyline: ask "why did / why didn't" questions about program output. They cite that initial guesses are wrong almost 90% of the time (a18). Pilot: Whyline users median 4 min (range 1 to 12) vs control median 10 min (range 3 to 38), p<.05. Control variation came largely from strategy (text search vs manual dependency following) (a19).

**Alaboudi and LaToza (2020, 2021)** [V]. A controlled study of hypotheses as an aid (b15, b16, d09) and a naturalistic study of professionals (b17, b18, d10). See section 3.

**Beller et al. (2018)** [V]. How developers really debug: the debugger is rarely used (a16, a17).

**LLM era.** Three phases.
1. 2023-2024: self-correction and self-repair papers (Huang, Olausson, Chen, Tyen, Shinn, Madaan, Kamoi). They show that the source of feedback is what matters.
2. 2024-2025: pipelines and agents with localisation steps (Agentless, SWE-agent, OrcaLoca, RepairAgent) and runtime-aware debuggers (LDB, debug-gym, InspectCoder).
3. 2026: studies that ask whether the locate step still pays for strong agents (Shi et al., Loc2Repair, RGFL, SGAgent, Coherence Collapse).

**Competing theories of why locating is hard.**
- Hypothesis-driven: debugging is hypothesis testing. Early hypotheses are mostly wrong. The skill is generating and discarding them (Vessey, Alaboudi, Ko).
- Comprehension-driven: debugging is understanding the program. Novices fail for lack of a mental model (Whalley et al. 2023, N=3, d14).
- Tool-driven: debugging is information access. The right tool or question collapses the search (Whyline, Parnin and Orso, debug-gym).

## 3. Core findings with exact numbers

Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts debug faster and err less than novices (one COBOL program) | Mean debug time 15 min 40 s experts vs 28 min 3 s novices (p<0.001). Time to error p=0.005. Novices made more mistakes (p=0.005); all 5 programmers with wrong fixes were novices. Low-level bug took longer (p=0.001). N=16 | Vessey 1985 (a04, b02) | [S] |
| Experts examine more modules; novices re-read the faulty module more | Modules examined P=0.045 (low N). Faulty module B000 examined more by novices; P=0.023 in one table, p=0.007 in another (unresolved) | Vessey (a08, b03) | [S] |
| Novices state more hypotheses and get constrained by them | 19 hypotheses from 9 subjects (1 to 3 each); novices > experts P=0.045. Only one subject (an expert) named the true cause. Constrained: 4 novices; unconstrained: 2 experts, 2 novices | Vessey (a06, a07) | [S] |
| Looking at output first, reading order, a familiarity phase did not separate groups | Table 9: no consistent pattern | Vessey (a02, b05) | [S] |
| Process-based class beats manager rating | R2 0.737 vs 0.361 for debug time | Vessey (a10, b01) | [S] |
| Ranked suspect lists: no gain for students | Tetris 12:42 tool vs 14:14 none; NanoXML 20:16 vs 22:30 (a14 lists the groups the other way); neither significant. N=24 main, 10 follow-up, 34 pilot. High performers (N=10) Tetris 8:51 vs 14:28, p<0.05 | Parnin and Orso 2011 (a14, b10) | [C] |
| Rank change did not matter | Faulty line moved rank 7 to 35 or 83 to 16: same completion fraction .79. 37% of list visits skipped more than one position. Of 10 who clicked the faulty line, only 1 stopped | Parnin and Orso (a15, b11) | [C] |
| Ranked lists: large gain for professionals | N=36 pros, 16 real bugs, 48 sessions per group. Success 98% (accurate tool) vs 77% (no tool). Time 11.38 vs 26.45 min (p=1.3e-10). Mediocre tool (fault at rank 6 to 10): 94%, 16.35 min. 75% of 24 users inspected the top 5 in order; 33% for top 6 | Xia et al. 2016 (b13, b14) | [C] |
| Candidate causes help; locations do not | N=20 analysed (60 sessions). Hypotheses OR 6.24 (p=0.03); fault locations OR 1.4 (p=0.64); one year of experience OR 1.14 (p=0.04). Control hypotheses correct: 3 of 27 at stage 1 (11%), 9 of 35 at stage 2, 15 of 38 at stage 3. Correct hypothesis at stage 2 gives 5x fix odds (p=0.01). 20 of 60 sessions failed | Alaboudi and LaToza 2020 (b15, b16, d09) | [S] |
| Real debugging is mixed, not phased | 11 professionals, 15 sessions, 30 h, 89 episodes. Debugging 48% of session time (13-95%). 80% of debug time came from 25 episodes. After an edit, tested 58% of the time. Logs 70%, debugger 30% for state inspection. Reported defects 51 min vs 6 min self-inserted | Alaboudi and LaToza 2021 (b17, b18, d10) | [S] |
| Developers rarely use the debugger | Not run in 91% of IDE sessions. Debugging 13.7% of IDE time. Reading precedes 51.9% of debug intervals. 132 developers with data, 18,156 h | Beller et al. 2018 (a16, a17) | [E] |
| Whyline speeds a bug | Median 4 vs 10 min, p<.05 | Ko and Myers 2008 (a18, a19) | [S] |
| Diagnosis takes most of the time | 66% of debug time (second-hand, via Kang) | Boehme et al. 2017 via Kang (a28, c15) | [S] |

Language-model studies, self-correction

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Blind self-revision of reasoning hurts | GPT-3.5 CSQA 75.8 to 38.1 (then 41.8); GSM8K 75.9, 75.1, 74.7; GPT-4 GSM8K 95.5, 91.5, 89.0; HotpotQA 49 to 43 | Huang et al. 2024 (a20, c05, c25) | [E] |
| Oracle labels explain reported gains | GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 GSM8K 95.5 to 97.5, HotpotQA 49 to 59 | Huang (c05; b23 had mixed rows) | [E] |
| Prior self-correction results often used oracles or weak baselines | Table 4 audit | Kamoi et al. 2024 (c07) | [E] |
| Self-Refine: no gain on math | 64.1 to 64.1; sentiment 8.8 to 30.4; acronym 41.6 to 56.4 | Madaan 2023 (c09) | [S] |
| Finding the wrong step is hard | GPT-4 best 52.87% (direct step prompt), 5 tasks, 300 traces each, 85% incorrect. GPT-3.5 down to 1.67-19% on some tasks | Tyen et al. 2024 (b21, c06) | [S] |
| Fixing is easy when told where | Gain on originally wrong answers, true vs random location: shuffled objects +23.53 vs +11.76; arithmetic +43.92 vs +20.39; Dyck +36.86 vs +21.57. Loss on correct traces -6.7 to -11.4 (true), -8.9 to -15.9 (random) | Tyen (b22) | [S] |

Language-model studies, code repair with execution

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Execution feedback is the active ingredient | MBPP GPT-4: base 72.8, simple 78.8, UT 80.6, UT+expl 80.4, UT+trace 80.2 (critique order). TransCoder GPT-4 77.3 to 88.8 (UT), 90.4 (UT+expl). Spider Codex 81.3 to 84.1 | Chen et al. (c01, c02, b24) | [E] |
| Without execution, gains shrink | GPT-4 MBPP 72.8 to 76.0/76.4; TransCoder 77.3 to 78.4; Codex MBPP simple 61.4 to 57.6, trace 66.2 | Chen (c02, b25) | [E] |
| Debug beats sampling in one setting | Spider: debugging a greedy output = 16 samples; from 8 samples beats 32. Gain after turn 1 within 0.1% | Chen (c03) | [S] |
| Self-repair is not clearly better than resampling | GPT-4 APPS: 10 samples + 1 repair 1.05x pass@20; 2 samples + 10 repairs 0.97x pass@22. GPT-3.5 cells mostly 0.83-1.04 | Olausson et al. 2024 (c04, b19) | [S] |
| Human diagnosis beats model diagnosis | Repair success 33.30% vs 52.60% (intro 42.64/62.21; interview 19.33/45.67; competition 3.67/14.67). 16 participants, 40 failing GPT-4 programs | Olausson (a21, b20) | [S] |
| Runtime values block by block | HumanEval GPT-3.5 73.8 to LDB 82.9 vs Self-Debug 81.1; GPT-4 87.2 to 89.6 vs 88.4; Reflexion seed 91.5 to 95.1 vs 92.1 | LDB (a23, b26, c12) | [S] |
| Real debugger beats simulated | BigCodeBench-R 67.87% vs 58.86% without real debugger (-8.01); LiveCodeBench-R 12.58% vs 7.95% (-4.64). Qwen2.5-Max only | InspectCoder (d08) | [S] |
| Print debugging beats rubber-duck | GPT-4, LeetCode: +1.5% easy, +17.9% medium | Print debugging 2024 (d12) | [S] |
| Hallucinated debugger output hurts | With LLM-made debugger output, <DONE> solutions 11 points less likely plausible vs +12.4 with real execution | Kang et al. 2025 (b30) | [S] |
| Logic bugs do not benefit from tracebacks | Traceback helps syntax and reference bugs; may harm logic bugs. Values only in figures | DebugBench (a25, b29, c19) | [S] |
| Debugging decays over retries | Fitted curve: 60-80% loss in 2 to 3 attempts. Fresh start at threshold: llama3.1:8b 72.56 to 82.82 (table 82.32); deepseek-coder-v2 84.15 to 92.07; mistral 54.27 to 62.80; codegemma 66.46 to 71.95; qwen2.5-coder 94.16 to 95.12; devstral 94.51 to 93.90; codestral 89.02 to 88.41 | DDI (a29, c18, d11) | [S] |

Language-model studies, agents and localisation

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Hierarchical localise-then-fix pipeline is cheap and competitive | Agentless 32.00% (96/300) at $0.70, SWE-bench Lite. Going file straight to lines was worse | Xia et al. (a26, c11) | [S] |
| Location accuracy tracks solve rate, but file level alone is not enough | One tool 23.67% resolved; text says 90.0% file-level, table says 79.0% | Xia (a27) | [E] as a trend |
| SWE-bench Lite has flawed items | 4.3% exact patch in issue, 10.0% missing information, 5.0% misleading | Xia (a26) | [S] |
| Failed runs usually reach the right file | File correct in 72-81% of failed trajectories; successful runs over 90%. Verified: 35-40% of failures miss the file; Lite 20-25% | Majgaonkar et al. 2025 (c16) | [S] |
| Most failures happen after reaching the right code | 16,758 trajectories. Right-location-wrong-patch share: GPT-5 68.1%, GPT-5-mini 69.1%, Qwen3-Coder-480B 66.8%, Qwen3-235B 64.7%, Qwen3-8B 45.5%, Qwen3-32B 37.6%. Five gold-identical patches overwritten later | Coherence Collapse (d06) | [S] |
| Of 209 RGFL failures only 28 were file misses | Gold file fixed 14 (50%); element miss 111, gold element fixed 29 (26%); line miss 175, gold lines fixed 33 (19%); 21 had all correct and still failed | RGFL (d02) | [S] |
| Predicted file location helps pipelines | Verified resolve: none 44.7%; predicted 48.9-49.1%; gold 52.4%. Agentless 51.6% to 55.8% (file) to 58.2% (file+element). Cost 3.7x | Loc2Repair; RGFL (d01, d02) | [S] |
| Predicted location does not help strong bash agents | 16,248 trajectories; pass@1 change -4.45 to +0.40, 17 of 18 settings negative, none significant (Holm). Gold file +0.8 to +4.0; gold symbol 76.2; bug cause 77.8; symbol+cause 80.0 vs 73.4 none. Low-clue issues: 68.4 none, 75.4 cause, 81.4 both | Shi et al. 2026 (d04) | [S] |
| Wrong supplied locations anchor and collapse repair | Top-3 right for 28 of 100 faults; pass@1 15-19% down to 0.3-3.6% (Claude 3.7 19.02 to 2.76; o3-mini 15.02 to 3.64) | Campos et al. 2025 (d05) | [S] |
| Cause step beats location step | Removing the suggest step: 51.3% to 38.0% (154 vs 114 of 300); file accuracy 80.3 vs 81.2 | SGAgent (d03) | [S] |
| Reproduction tests as a reranker | Greedy 37.7, vote 40.3, +regression tests 44.7, +reproduction tests 51.3 | SGAgent (d03) | [S] |
| Debugger tool: timing matters | SWE-bench Lite rewrite / pdb from start / pdb after 5: GPT-4o 19.1/17.2/23.6; 4o-mini 4.0/3.5/6.2; Llama-3.3-70B 2.4/4.0/4.8; o1-preview 10.7/30.2/30.8; o3-mini 8.5/22.1/19.8; Claude 3.7 37.2/48.4/52.1 | debug-gym (c13, d07) | [S] |
| Interface design matters | SWE-agent GPT-4 Turbo 12.47% of 2,294; Lite ablations: summarized search 18.0 vs none 15.7 vs iterative 12.0; edit with linting 18.0 vs 15.0 vs no edit tool 10.3 | SWE-agent (c10) | [S] |
| Location by LLM beats spectrum tools | Method-level acc@1 +19.7% over Ochiai (Defects4J), +166.7% (BugsInPy, GPT-3.5), +233.3% (GPT-4). 798 bugs | Kang et al. 2024 (a28, c15) | [S] |
| Spectrum localisation costs repair | RepairAgent with GZoltar vs perfect: 25% fewer fixes, 81% more cost | RepairAgent (c14) | [S] |
| Trace-driven multi-agent debugger | Removing repair loop: 89.04 to 53.77. Own benchmarks | TraceCoder (c17) | [S] |
| Reflexion false positives | MBPP-Python 80.1 to 77.1 (worse); false positive rate 16.3% MBPP vs 1.4% HumanEval | Shinn et al. (c08) | [S] |
| Explanations help human patch review | Better accuracy in 5 of 6 bugs (U p<0.05), two cases worse; N=20 | Kang 2025 (b31) | [S] |

## 4. Mechanisms and models

**M1. Vessey's process model (implementable as a log schema).** Tag each step of an agent run with one goal: DETERMINE, FAMILIARISE, EXPLORE, EVALUATE, REPAIR. Code checks that every run has DETERMINE and REPAIR, and that REPAIR is last unless a repair failed. A hypothesis is a record: text, status (open, supported, refuted), evidence ref. Four flags per run mirror the strategy paths: output-first, active (executed code) vs passive (only read), constrained (keeps the first hypothesis) vs unconstrained, system view (looked at modules beyond the first suspect). The cheap indicators from Vessey: early commitment and repeated re-reading of the same module go with failure. Implement as counters: modules touched, times the same file was re-read, hypotheses opened and closed. These are log metrics, not rules.

**M2. Locate-then-fix as a pipeline with an optional location step.** Hierarchy: file, then function, then line (Agentless, RGFL, OrcaLoca). The benefit depends on the backbone. For pipelines with weaker repair models, predicted file location adds about 4 points (Loc2Repair, RGFL). For strong bash-only agents, gold-file reach without any locator is already 88.6% to 99.4% (Shi), so the step adds nothing. Implementation: make the step conditional. Run it when the task text gives few location clues (Shi: low-clue issues gain most from hints, 68.4 to 75.4 with cause) and when the agent's own first look fails to name a function.

**M3. Cause statement before patch.** One sentence: "The bug is X because Y, shown by output Z". Evidence: SGAgent's suggest stage (+13.3 points), Shi's bug-cause hints (+4.4 to +7.0, more than file or symbol), Alaboudi's candidate causes (OR 6.24 vs 1.4 for locations). This is close to S5's existing "one line naming what is wrong". The addition is that the line must be a testable cause, not a place.

**M4. Execution-grounded evidence loop.** Run, read the real output, form a hypothesis, test it with a probe (print, assertion, pdb command), read the real result. Real beats imagined: LDB, InspectCoder (+8.0, +4.6), Kang (hallucinated debugger output -11 vs real +12.4), Self-Debug with vs without tests. Implementation: code owns the execution. The model only proposes the probe and reads the result. The model's prose about what the code "would" do is never used as evidence (G10).

**M5. Tool gating by failure.** debug-gym: a debugger given from the start hurts GPT-4o-class models and helps reasoning models. Given after 5 failed rewrites it helps all six tested. Implementation: start with rewrite from test output, unlock interactive tracing after N failures (N=1 or 2 in our budget, to be tested; the paper used 5).

**M6. Keep-best and revert.** Coherence Collapse: agents overwrote patches that were bit-identical to gold in 5 cases. Implementation: after each edit run the available checks and store a score. If the new score is not strictly better, revert to the best patch. S5 already says "keep best-so-far"; the gap is making the revert automatic.

**M7. Restart with summary (DDI).** After t attempts fail, drop the context. Keep a short summary of what was tried and what the failures were. Begin again. Support is HumanEval only, mostly small models, gains up to 10 points for weak models and about 0 for strong ones.

**M8. Location confidence check.** Campos shows a wrong location collapses repair. Tyen shows even a random location helps on wrong traces but hurts correct ones (-8.9 to -15.9). So an unchecked self-made location is a risk. Implementation: before editing, run one cheap execution check tied to the location (does the failing input reach this function; does a print there show the wrong value). No break-even accuracy is known.

## 5. What holds up

**Holds (multiple sources, re-checked).**
- Without a real checker, LLM self-revision does not help and often hurts (Huang; Kamoi audit; Self-Refine null on math; Reflexion MBPP drop). K03, [E].
- Real execution output is what makes code self-debugging work: gains of +8 to +12 with unit tests, +1 to +4 without. K04, [E].
- Location quality tracks resolve rate across agent pipelines (Agentless, OrcaLoca, RGFL, Loc2Repair). K07 [E] as a trend, with the caveat below.
- Most agent failures on Verified for capable models happen after the right code is reached (Coherence Collapse, RGFL, Majgaonkar). K09 [E].
- Developers rarely use debuggers; reading dominates (Beller; Alaboudi). K19 [E], descriptive.

**Fails or shrinks.**
- Vessey has no replication. N=16, one program, one site, ex post expert label, authors call it exploratory. The gap search found no eye-tracking or think-aloud replication. Naturalistic data show no clean phase order (d10).
- Parnin and Orso vs Xia et al.: direct conflict, unresolved. Candidate causes: tool accuracy (98% vs weak lists), professionals vs students, real vs seeded bugs, task size. Full texts were not re-opened for this pass.
- Predicted location on strong agents: 17 of 18 settings slightly negative (Shi). So the Loc2Repair and RGFL gains do not carry over to strong bash agents. These look like two regimes, not a contradiction. In pipelines a separate locator supplies the location. Strong agents already find the file.
- Self-repair vs resampling: Olausson found no clear win at matched compute for GPT-4 and GPT-3.5. Chen found debug-from-8-samples beating 32 samples on Spider. Different tasks and ways of counting. No 2025-2026 reasoning-model replication found.
- DDI fresh-start: gains only for weak models. Text and tables disagree on the count of improved models (six vs nine) and on one number (82.82 vs 82.32). Token neutrality is unsupported beyond two examples.

**Moderators.**
- Bug type: runtime feedback helps syntax and reference bugs, and is neutral or harmful for logic bugs (DebugBench).
- Model strength: a debugger from the start hurts weaker models and helps reasoning models (debug-gym). Dynamic info helps Qwen2.5-Max much more than GPT-4o (InspectCoder).
- Seed strength: LDB gains are +9.1, +2.4, +3.6 as seeds go from weak to strong. Gaps shrink near saturation.
- Task clue level: location hints help most when the issue text gives few clues (Shi).
- Benchmark noise: SWE-bench Lite has 4.3% leaked patches, 10.0% missing info, 5.0% misleading. The StarShip 90.0 vs 79.0 file-level contradiction shows how fragile reported numbers are.

**Interventions that worked.** Real execution output. Block-level runtime values. A real debugger over a simulated one. A cause-statement stage. Reproduction-test reranking. Gating the debugger after failures. Hierarchical localisation in a pipeline for weaker backbones. Human-written diagnoses (outside our reach).

**Interventions that did not.** Blind self-critique. Model-imagined execution. Supplying ranked or predicted locations to strong agents. Tracebacks on logic bugs. "Simple feedback" without execution (Codex MBPP 61.4 to 57.6). A debugger from the start for weak models. Explanations for human reviewers on 2 of 6 bugs.

**Overlap warning.** Evidence files a, b and c overlap. The Chen, Olausson, Huang, Tyen and LDB papers were read by two or three agents. They count as one source each. Claims count independent sources, not lines.

## 6. Language models

**Self-diagnosis is the bottleneck.** GPT-4 finds the wrong reasoning step only 52.87% of the time (Tyen). Given the true location, originally wrong answers improve by +23.5 to +43.9 points. Human diagnoses lift GPT-4 repair success from 33.3% to 52.6% (Olausson), with the biggest relative gain on hard problems (competition 3.67 to 14.67).

**Feedback source decides.** Same model, same task: oracle label 95.5 to 97.5 vs blind revision 95.5 to 89.0 (GPT-4 GSM8K). With code, real tests give +8 to +12. No execution gives +1 to +4 or a loss.

**Real vs imagined tracing.** LDB and InspectCoder use real runtime values. The gains over simulated tracing are +8.0 and +4.6 points. Kang found hallucinated debugger output made a completion signal less reliable (-11 vs +12.4). Print debugging beat rubber-duck by 17.9% on medium LeetCode (GPT-4, abstract only).

**Location for agents has two regimes.**
- Pipelines (Agentless-style), weaker repair: predicted file location +4 points (44.7 to 48.9-49.1), gold +7.7. Better reasoning on location lifted 51.6 to 58.2 at 3.7x cost.
- Strong bash-only agents (2026): predicted location -4.45 to +0.40, none significant. Gold cause +4.4 to +7.0. Repair-stage tokens fell 11.3% to 39.2% with gold hints, but end-to-end tokens often rose with predicted location.
- When the supplied location is mostly wrong, repair collapses (Campos: 28 of 100 right in top 3; pass@1 down about 5x to 50x). Misleading locations anchor agents, but about half still reach the gold file later.

**Failure shape.** 60.8% to 69.1% of failed runs by capable models reached the right functions. The loss is in the patch, or in later overwriting of a good patch, not in finding the file. Small models fail earlier (37.6% to 45.5% in the right-location bucket). Search loops are the most stable failure signal in a 2,500-trajectory study (TraceProbe, abstract only).

**Retry dynamics.** Fitted decay: 60-80% of debugging power lost in 2-3 attempts for small open models. Claude 3.7 Sonnet reached 100% on HumanEval within about two attempts, so no curve could be fit. This is a fit on a near-saturated benchmark.

**Pipelines vs agents.** Agentless at 32.00% for $0.70 matched open agents in 2024. Interface design mattered a lot in SWE-agent (linting on edit +3.0, no edit tool -7.7 points).

**Models and dates.** Most results use GPT-3.5, GPT-4, Codex, Qwen2.5 and Llama (2023-2025). The 2026 results (Shi, Loc2Repair, RGFL, SGAgent, Coherence Collapse, TraceCoder) use newer models but are preprints. Several use unusual model names and several have internal number errors (SGAgent 154 vs 152; Campos text vs table).

**What no LLM study has tested.** Vessey's goal order directly. Candidate-cause lists vs location lists head to head. False-positive fixes before and after a reproduction rerun. Matched-token self-repair vs resampling for reasoning models. A break-even location accuracy.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Every S5 revision cites real failing output produced by code; no revision from the model's opinion | G2 / S5 | [E] | K03, K04; a20, c05, c07, c01, c02, b24, b25 |
| In the revise loop, executed output (tests, run results, probe prints) replaces any model-written "what the code would do" | G2, G10 / S5 | [E] | K04, K05, K25; c01, c02, d08, b30 |
| Runtime feedback is strong for syntax, reference and crash errors and weak for logic errors; for logic bugs use value probes, not traceback text | S5 | [E] for the split, [S] for the probe | K11, K04; a25, b29 |
| Log where each failure occurred: wrong file, wrong function, right function wrong patch, good patch overwritten | memory, S9 | [E] (failures cluster after location) | K09, K24; c16, d06, d02 |
| Keep the best-so-far patch (already in schema) | S5, G6 | [E] for keep-best; automatic revert is [S] | K24; d06 |
| Do not treat the model's own location as unchecked fact | G2, G10 | [E] direction | K02, K21; b22, d05 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| One-sentence testable cause statement before the first patch (cause, not place) | S5 | [S] | K23, K13, K20; d03, d09, d04 |
| Conditional location step, only when the task has few location clues | S5 / S0 | [S] | K20, K22; d04, d01, d02 |
| Cheap execution check on a self-made location before editing | S5 / G2 | [S] | K21, K02; d05, b22 |
| Gate the interactive debugger or value probe until after the first failed rewrite | S5 / O-trace | [S] | K12; c13, d07 |
| Block-level value tracing (print locals) vs prose reasoning on logic bugs | S5 | [S] | K05, K25; a23, d08, d12 |
| Automatic revert to best patch | S5 | [S] | K24; d06 |
| Restart with summary after 2 failed rounds | S5 / S6 | [S] | K10; a29, d11 |
| Hold two hypotheses open before the first edit | S5 / S4 | [S], human only | K15; a06, a07 |
| Reproduction-script rerun as last check, counting false-positive fixes | S8 | [S] | K26; d03, c08 |
| Self-repair vs resample at equal tokens | S5 budget / G7 | [S], older models | K06; c04 |
| Candidate-cause list vs location list | S5 | [S], human only | K13, K23; d09, b16 |

Leave out: ranked suspect lists as a rule (K14 [C]); strict phase order from Vessey (no replication); K16, K18, K19 (no test or descriptive only).

## 8. Concrete tests on our bench

All tests use equal total tokens across arms, set by the cap of the smaller arm and measured, not estimated. Setup cost counts (G7). The pass criterion is the item's own hidden test, never a model judge.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Repo bug-fix items with a failing test, a mix of high-clue and low-clue issue text | A: direct patch. B: forced locate (file, function) then patch. C: conditional locate (only when clue count is low) | Resolve rate; location accuracy logged separately; tokens | B <= A on high-clue; C >= A. Gain on low-clue about +3 to +5 points |
| T2 | Same items | A: locate then patch. B: one-sentence cause, tested by a probe, then patch | Resolve rate; share of fixes at the wrong location | B > A by about 3 to 7 points (Shi range) |
| T3 | Bug items with a supplied location that is wrong 40% of the time | A: edit at the given location. B: one execution check on the location first | Resolve rate; right-to-wrong harm | B recovers most of the harm from wrong locations |
| T4 | Logic-bug items (wrong output, no crash) | A: prose reasoning about execution. B: executed print probes read back | Fix rate | B > A by 4 to 8 points |
| T5 | Items with a real check | A: revise with real test output. B: revise with model self-critique only | Right-to-wrong flips; final pass | A clearly better; confirms G2 |
| T6 | Mixed difficulty | A: debugger/probe tool from the start. B: tool unlocked after the first failed rewrite | Resolve rate by model strength | B >= A for the mid-strength model |
| T7 | Items where rounds 1 and 2 fail | A: keep revising. B: restart with a 5-line summary | Final pass at equal tokens | Gain only on the weaker setting; about 0 for strong |
| T8 | Items with a spare sample budget | A: N independent samples. B: N/3 samples, each with 2 diagnose-repair rounds | Pass at matched tokens | Olausson says ratio near 1.0 |
| T9 | Items with a reproduction script | A: stop when the check passes. B: also rerun the reproduction script | False-positive rate (passes check, fails hidden test) | B lowers false positives |
| T10 | Agent runs with checkpoints | A: free edits. B: score every edit, revert to best | Resolve rate; overwritten-good-patch count | B recovers part of the 60-69% right-location failures |

Log a failure taxonomy in all runs: file miss, function miss, right location wrong patch, patch overwritten, search loop.

## 9. What does not transfer, and why

- **Vessey's expert/novice contrast.** Models are not novices in the human sense. The "chunking" labels were made after the fact on 16 people. The finding about early-hypothesis constraint may relate to anchoring, but an LLM anchors differently (its first output sits in its context). Use as a log metric, not a rule.
- **Phase order.** Real developers mix activities and show no clean locate-then-fix order (d10). Enforcing a strict order is not supported by human data. Only the dependency "do not patch before you have evidence" carries over.
- **Ranked suspect lists.** The human dispute (Parnin vs Xia) concerns how people read lists (75% inspected the top 5 in order). A model reads the whole list at once, so order effects differ. Strong agents also found no gain from predicted locations.
- **Debugger-usage statistics.** Developers avoid debuggers (91% of sessions without). That reflects the human cost of tool setup, not the value of tracing for an agent.
- **Time and effort measures.** Minutes per bug are not our metric. Tokens and resolve rate are.
- **Older-model self-repair results.** GPT-3.5, GPT-4 and Codex numbers on near-saturated HumanEval and MBPP may not hold for reasoning models, which already test hypotheses inside their own reasoning.
- **Fresh-start threshold (DDI).** Fitted on small open models. Strong models showed no decay.
- **Human-written diagnoses.** The strongest lever in Olausson (33.3% to 52.6%) needs a person. Not available inside the agent.
- **Human explanation-review studies.** Patch review accuracy for people (Kang 2025) does not bear on agent behaviour.

## 10. Open questions

1. Does an explicit locate step beat direct patching at equal tokens for current reasoning models, and does it survive 40% wrong locations? No break-even accuracy has been measured anywhere.
2. Is there a matched-token self-repair vs resample result for 2025-2026 reasoning models? Not found. Search was rate-limited, so absence is not proven.
3. Why do Parnin and Orso and Xia et al. disagree? Full texts were not re-opened in the gap pass. a14 and b10 even list the NanoXML groups in opposite order.
4. Does Vessey replicate? No modern eye-tracking or think-aloud replication found. The faulty-module re-examination p-value differs inside our own source set (0.023 vs 0.007).
5. Do candidate-cause lists beat location lists for LLM agents? No head-to-head test. Human OR 6.24 vs 1.4 and SGAgent's +13.3 are indirect.
6. Does a reproduction rerun reduce false-positive fixes? Reflexion shows 16.3% false positives on MBPP. Nobody measured before and after.
7. Does the debug-gym pattern (tool after failures) hold for newer reasoning models with tokens counted? The Llama-3.3-70B text vs table conflict remains.
8. Is the "right location, wrong patch" share (60.8-69.1%) inflated by the loose test (function recall at least 0.5)?
9. Does the fresh-start rule work on frontier agents in real repos with token cost counted?
10. Do the 2026 preprints replicate? Shi, Coherence Collapse, Loc2Repair, RGFL and SGAgent are single sources, some with internal inconsistencies.

## 11. Sources

[V] opened and read this session. [M] snippet, abstract page or metadata only.

Human studies
- [V] Vessey (1985), Expertise in debugging computer programs: a process analysis. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/vessey85.pdf (DOI 10.1016/S0020-7373(85)80054-7)
- [M] Gould (1975), Some psychological evidence on how people debug computer programs. https://research.ibm.com/publications/some-psychological-evidence-on-how-people-debug-computer-programs
- [M] Katz and Anderson (1987), Debugging: an analysis of bug-location strategies. https://www.ets.org/research/policy_research_reports/publications/article/1987/icwz.html
- [M] Gugerty and Olson (1986/87), Debugging by skilled and novice programmers. https://www.academia.edu/102488941/Debugging_by_skilled_and_novice_programmers
- [M] Shapiro (1983), Algorithmic Program Debugging. https://mitpress.mit.edu/9780262192187/algorithmic-program-debugging/
- [M] Boehme et al. (2017), Where is the bug and how is it fixed? Cited in https://www.spinellis.gr/pubs/conf/2018-ICSE-debugging-analysis/html/BSSZ18.pdf
- [V] Parnin and Orso (2011), Are automated debugging techniques actually helping programmers? https://web.eecs.umich.edu/~weimerw/2018-481/readings/debugging-helping.pdf
- [V] Xia, Bao, Lo, Li (2016), "Automated debugging considered harmful" considered harmful. https://baolingfeng.github.io/papers/ICSMEmain.pdf (re-fetch failed in the gap pass; DOI link https://doi.org/10.1109/icsme.2016.67 is [M])
- [V] Ko and Myers (2008), Debugging reinvented. https://faculty.washington.edu/ajko/papers/Ko2008JavaWhyline.pdf
- [V] Alaboudi and LaToza (2020), Using hypotheses as a debugging aid. https://arxiv.org/abs/2005.13652
- [V] Alaboudi and LaToza (2021), An exploratory study of debugging episodes. https://arxiv.org/abs/2105.02162
- [V] Beller, Spruit, Spinellis, Zaidman (2018), On the dichotomy of debugging behavior among programmers. https://www.spinellis.gr/pubs/conf/2018-ICSE-debugging-analysis/html/BSSZ18.pdf
- [M] Whalley, Settle, Luxton-Reilly (2023), A think-aloud study of novice debugging. https://doi.org/10.1145/3589004
- [V] Bo et al. (2025), Who's the Leader? Novice workflows in LLM-assisted debugging. https://arxiv.org/abs/2505.08063
- [M] ICER 2024, Debugging with an AI tutor. https://icer2024.acm.org/details/icer-2024-papers/2/Debugging-with-an-AI-Tutor-Investigating-Novice-Help-seeking-Behaviors-and-Perceived

LLM studies
- [V] Huang et al. (2024), LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Kamoi et al. (2024), When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297
- [V] Shinn et al. (2023), Reflexion. https://arxiv.org/abs/2303.11366
- [V] Madaan et al. (2023), Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Tyen et al. (2024), LLMs cannot find reasoning errors, but can correct them given the error. https://arxiv.org/abs/2311.08516
- [V] Olausson et al. (2024), Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896
- [V] Chen et al. (2024), Teaching LLMs to self-debug. https://arxiv.org/abs/2304.05128
- [V] Zhong, Wang, Shang (2024), LDB: Debug like a human. https://arxiv.org/abs/2402.16906
- [V] Tian et al. (2024), DebugBench. https://arxiv.org/abs/2401.04621
- [V] Xia et al. (2024), Agentless. https://arxiv.org/abs/2407.01489
- [V] Yang et al. (2024), SWE-agent. https://arxiv.org/abs/2405.15793
- [V] Kang, An, Yoo (2024), LLM-based explainable fault localization (AutoFL). https://arxiv.org/abs/2308.05487
- [V] Kang, Chen, Yoo, Lou (2025), Explainable automated debugging via LLM-driven scientific debugging. https://doi.org/10.1007/s10664-024-10594-x
- [V] Bouzenia, Devanbu, Pradel (2025), RepairAgent. https://arxiv.org/abs/2403.17134
- [V] Yu et al. (2025), OrcaLoca. https://arxiv.org/abs/2502.00350
- [V] Meng et al. (2025), LLM-based agents for automated bug fixing: how far are we? https://arxiv.org/abs/2411.10213
- [V] Majgaonkar et al. (2025), Understanding code agent behaviour. https://arxiv.org/abs/2511.00197
- [V] Adnan and Kuhn (2025), The Debugging Decay Index. https://arxiv.org/abs/2506.18403
- [V] Yuan et al. (2025), debug-gym. https://arxiv.org/abs/2503.21557
- [V] Wang et al. (2025), InspectCoder. https://arxiv.org/html/2510.18327
- [V] Campos et al. (2025), Exploring generalizable APR with LLMs. https://arxiv.org/html/2506.03283
- [V] Leveraging print debugging to improve code generation in LLMs (2024), abstract only. https://arxiv.org/abs/2401.05319
- [V] Huang et al. (2026), TraceCoder. https://arxiv.org/abs/2602.06875
- [V] Al Awad and Ivanov (2026), Loc2Repair (abstract page). https://arxiv.org/abs/2606.30963
- [V] Sepidband et al. (2026), RGFL. https://arxiv.org/html/2601.18044v1
- [V] Zhang et al. (2026), SGAgent. https://arxiv.org/html/2602.23647v1
- [V] Shi, Yang, Chen (2026), From finding to fixing. https://arxiv.org/html/2610.25826
- [V] Coherence Collapse (2026). https://arxiv.org/html/2603.24631
- [V] CogniGent (2026), abstract only. https://arxiv.org/abs/2601.12522
- [V] TraceProbe (2026), abstract only. https://arxiv.org/abs/2607.06184
- [M] D4C, Aligning the objective of LLM-based program repair (ICSE 2025), snippet only; unverified. https://conf.researchr.org/details/icse-2025/icse-2025-research-track/148/Aligning-the-Objective-of-LLM-based-Program-Repair

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 5 established claims: 2 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A20.01-K04** (now single-source: the sources are not independent). All with/without-execution numbers (72.8 to 80.4-80.6, 77.3 to 88.8-90.4, 61.4 to 57.6, no-execution +1 to +4) come from the single Self-Debug paper (the many listed lines are one paper); LDB (Zhong et al.) is a different method and does not run the no-execution ablation. Numbers themselves match.
- **A20.01-K07** (reworded: the sources support less). Agentless text states 90.0% file-level match and 23.67% resolved for StarShip (the '79.0% in its table' could not be tied to that row); the -4.45 to +0.40 pass@1 range is real (17 of 18 settings negative, none significant after Holm) but comes from mini-swe-agent with GPT-5.6 Luna / DeepSeek-v4 Flash / Gemini 3.1 Flash Lite, and the paper does not show that the benefit 'shrinks as agents get better'. Corrected claim: Repair benefit depends on correct location and diagnosis: in agentic pipelines the correct-location rate tracks solve rate, but file-level location alone is not enough (Agentless reports OpenCSG StarShip at 90.0% file-level match yet only 23.67% resolved on SWE-bench Lite). A 2026 study of mini-swe-agent with three recent LLMs found that adding fault-localization output changed pass@1 by -4.45 to +0.40 points (negative in 17 of 18 settings, none significant after Holm correction), so predicted locations did not reliably help such agents.
- **A20.01-K19** (reworded: the sources support less). Beller et al.'s 91%, 13.7% and 51.9% match, but they measure IDE-debugger use by Eclipse/IntelliJ developers (13.7% is time in debugger intervals, 132 of 458 users ever used the debugger), not all debugging; Alaboudi and LaToza find debugging episodes take about 48% of live-streamed session time, so 'debugging is 13.7% of IDE time' and 'mostly not done with debugger tools' are wider than the data. Corrected claim: Debugging is frequent and uneven (about once every 8 minutes of programming, 13-95% of session time per session; Alaboudi and LaToza 2021), while in Java IDEs (Eclipse/IntelliJ, Beller et al. 2018) developers did not start the debugger in 91% of sessions, time in debugger intervals was 13.7% of active IDE time, and reading preceded 51.9% of debug intervals.
