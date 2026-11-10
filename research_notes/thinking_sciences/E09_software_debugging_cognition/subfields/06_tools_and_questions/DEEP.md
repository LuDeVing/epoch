# Tools and questions: deep document

*Subfield E09.06: why and why-not questions, program slicing. Key works: Ko and Myers (Whyline, 2004-2009); Weiser (1981, 1982). Schema link: O5 (work backwards from the failure). Sources: evidence_a-d.jsonl, claims.jsonl, critique.md in this folder. Evidence ids a01-a28, b01-b28, c01-c26, d01-d24. Claim ids E09.06-K01 to K18. Numbers marked "re-checked" were re-opened from the source PDF in the critique pass.*

## 1. What it is

A programmer sees a wrong output. Two ideas say how to get from that output back to its cause.

1. **Program slicing (Weiser).** A slice is the set of statements that can affect the value of one variable at one point. It is found by following data and control dependence backwards. A static slice covers all inputs. A dynamic slice covers one run and is much smaller. Weiser's claim: programmers already do this in their heads when they debug unfamiliar code.
2. **Why and why-not questions (Ko and Myers).** The programmer picks a question about an output ("why did the line turn blue?", "why didn't Pac resize?"). The tool answers with a dynamic slice, shown as a causal chain. This is the Whyline. The question is the interface. The slice is the engine.

For our agent this is operator O5 (work backwards from the goal or failure). The plain form: given a failing output, ask "what must have happened for this value?", compute the answer from the run, and check it. Three separate ideas hide inside it, and the evidence treats them differently.

- **The question.** Is it useful to force a why / why-not framing?
- **The computed answer.** Is a code-computed backward slice or runtime answer better than the model reading code freely?
- **The check.** Is the model's own causal story reliable, or must it be checked against executed evidence?

Short answer from the evidence: the computed, focused answer helps and the model's own causal story is unreliable. Whether the question wording itself matters has not been tested on LLMs (K17, K15).

## 2. History and theories in depth

**Weiser 1981 and 1982.** Weiser defined the slice formally (ICSE 1981, a19) and argued in CACM 1982 (a01, b27, c07) that programmers debugging unfamiliar code mentally cut slices out of the text. The ACM PDFs returned 403, so the original statistics were never read. Second-hand accounts agree on the design: 21 programmers, 3 programs of 75-150 lines (Algol-W, names replaced by arbitrary symbols, no comments); the Ko 2025 retrospective says 2 programs (a02), Parnin and Orso say 3 (d19). After debugging, people saw slice and non-slice fragments and recognised slice fragments more often. Parnin and Orso point out this tested recognition, not whether slices help debugging (d19). Ko et al. call it a single small study with almost no later validation (a02).

**Later human tests of slicing (second-hand, d19).** Weiser and Lyle: one 100-line program, no improvement from slices; a follow-up on 25 lines with printouts and dicing gave faster work on some bugs. Francel and Rugaber: 17 students, 4 sliced instinctively, and those 4 understood a 200-line program better. Kusumoto: 6 students, mixed. So the founding claim was never confirmed by a clean experiment (K14).

**Ko and Myers, 2003-2005: the cognitive frame.** Their model of programming errors (VL/HCC 2003, cited in a27) says chains of cognitive breakdowns cause bugs. One finding from Alice studies: 50% of all errors came from false assumptions in hypotheses formed while debugging an existing bug. So debugging adds new bugs through wrong guesses. That is the root argument for a tool that replaces guessing with asking. Their question statistics: 68% of questions were why-didn't, 85% concerned a single object (a03, b01, c02). All of these numbers come from the authors' own earlier studies of Alice, not independent data.

**The Whyline, 2004 (Alice).** The menu lists questions built from a database of all output changes plus precise dynamic slices. Design constraints from observation: people only ask why-didn't about code that might plausibly have run, and phrase questions as "why did Pac's direction change" about a failure, not "why is the value X" (a20). A participant said the tool was "useless" when it could not answer a why-didn't question (b04). That one comment drove the design.

**The Java Whyline, 2008-2009.** Static and dynamic slicing, a precise call graph, and an algorithm for "why did this line not run" (static analysis of the call graph for blocking predicates, then slicing on them at the event time, a21). Traces were limited: ArgoUML, 113,117 lines, 35,597 I/O events in about a minute, several times slower than untraced (c04). Coverage check: 8 of 9 real bug reports from 5 open-source programs could be phrased as a Whyline question; the miss was a feature request (b08). Authors call this a best case.

**Information needs and navigation, 2005-2007.** Observational studies that justify the tool. Developers spend 35% of time just navigating dependencies; 42% of dependencies they followed were indirect and unsupported by the IDE (a09, b10); the question "what code caused this program state?" was unsatisfied 61% of the time (a10, b09). These are the best-supported motivation: studies of different samples, one company and one lab.

**Parnin and Orso 2011.** An independent challenge to automated debugging aids (d18, opened from the author PDF). It tested a ranked statement list, not a slice and not a Whyline, but it tests the shared assumption that pointing at the fault equals understanding it. Details in section 5.

**Slice quality tools, 2021-2026.** Soremekun et al. (2021): a simulated programmer following dynamic slices finds faults earlier than one following statistical ranking (d16). Then LLM-era work: can models compute slices (a11), agents that build slices (a12), using slices as context for repair (a13, c15), as a measuring ruler (a14), and as the way to answer "why does this variable have this value" (a15).

**Ko 2025 retrospective (a02).** The authors look back at 2004 and say their data found developers build a fuzzy working set of possibly relevant code, not clean slices. That weakens the pure-slice story and supports a softer form: focus the search by following dependence, expect fuzziness.

## 3. Core findings with exact numbers

Status key: **established** (two or more independent sources), **single-source**, **contested**, **second-hand** (not opened).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Alice debugging questions are mostly why-didn't and about one object | 68% why-didn't; 85% single-object; 50% of errors from false hypotheses | Ko and Myers 2004 (a03, b01, a27), authors' earlier studies | single-source, human, not independently measured |
| Whyline cuts diagnosis time in Alice (small N) | 6 matched scenarios, F(1,5)=12.64, p<.02, average per-scenario ratio 7.8 (330 s vs 38 s in one case); N=4 without, 5 with; re-checked | Ko and Myers 2004 (a04, b02, a24) | single-source; ratio is an average of ratios, post hoc scenarios |
| Whyline users finish more tasks | 3.20 (SD .457) vs 2.25 (SD .500) tasks in 90 min, t(7)=3.0, p<.02 = 40% more; useful for 19 of 24 questions; re-checked | Ko and Myers 2004 (b03) | single-source |
| Java Whyline pilot | 9 users median 4 min (range 1-12) vs 18 experts from an earlier study median 10 min (range 3-38), Wilcoxon p<.05; re-checked. NOT a concurrent control | Ko and Myers 2008 (a05, b05, a26) | single-source, cross-study |
| Java Whyline, controlled | 20 students, 10 per group, two ArgoUML bugs, 30 min each. Task 1: 10/10 vs 3/10 completed (chi2=10.6), twice as fast. Task 2: 4/10 vs 0/10 (chi2=5), no speed difference. Re-checked | Ko and Myers 2009 (a07, a08) | single-source, best-powered Whyline test |
| Why-didn't barely used in the 2009 test | Median 4 why-did questions in task 2; why-didn't rarely asked because analysis took about a minute | Ko and Myers 2009 (a08, a23) | single-source |
| Experts speculate first; novices just ask | Anecdote from the 9-person pilot; experts looked for a question to confirm their guess | Ko and Myers 2008 (a06, b06) | single-source, qualitative |
| Control group failed by dismissing the buggy method | Controls read the buggy method, judged it unimportant, never returned; text search for "color" gave 62 matches in 9 files | Ko and Myers 2009, 2008 (a08, a26) | single-source |
| Developers lack causal-chain support | "What code caused this program state?" unsatisfied 61% (up to 21 min); "What code could have caused this behavior?" 36%; 17 developers, 25 hours, 334 information-seeking instances | Ko, DeLine, Venolia 2007 (a10, b09); the author line in c06 is wrong | established together with a09/b10 |
| Navigation cost | 35% of time on navigation (10 experts, 5 tasks, Eclipse); 42% (SD 20) of about 65 dependencies followed were indirect and unsupported | Ko et al. 2005, 2006 (a09, b10) | established but likely one dataset reported twice |
| Weiser slices recognised | 21 programmers, 3 programs of 75-150 lines (2 per Ko 2025); recognition after the fact | Weiser 1982 via d19, a02 | second-hand, stats unverified |
| Slicing tools in later human tests | Weiser and Lyle none; Kusumoto 6 students mixed; Francel and Rugaber 4 of 17 sliced instinctively | d19 | second-hand |
| Ranked suspect list does not help overall | 24 students, 30 min/task; Tetris successful time A 8:51 vs B 14:28 (high performers, p<.05); no effect on harder NanoXML; moving the fault in the ranking changed nothing; 61% of time continued after seeing the fault; 1 of 10 stopped at the fault; 37% of visits non-linear | Parnin and Orso 2011 (d18) | single-source but independent of the Whyline lab |
| Dynamic slice beats statistical ranking (simulation) | 457 bugs in 46 C programs; dynamic slicing 8 points more effective than best formula on single faults; fault found earlier for 66% of bugs; hybrid best | Soremekun et al. 2021 (d16) | single-source, no human or LLM |
| LLMs cannot compute exact slices | GPT-4o static Accuracy-D 60.84% (one-shot CoT), exact match 7.33%; GPT-3.5 46.43%; Gemma-7B 43.43%; Llama-2 17.57%; dynamic best 59.69% zero-shot, exact match 0%; prompt crafting +4%, iterative +3.9%; 100 LeetCode Java programs | Shahandashti et al. 2024 (a11, b21, b22, c09, a28) | established (a12, a15 also show weakness) |
| LLM agent slicing does much better | SliceBench 2,200 programs; average +15.2% accuracy, +22.1% F1, +10.7% exact match; up to +63.1% accuracy on large programs; verification and refinement agents are the key | Chang et al. 2025 SliceMate (a12, c11, d17) | single-source, own benchmark |
| LLM estimates missing trace steps | 8,300 dynamic dependencies; accuracy 80.3 / 91.1 / 98.3% vs best baseline 39.0 / 82.0 / 59.9%; 16% more regressions located | Pei et al. 2025 (a15, c13) | single-source |
| Accuracy falls with chain size | Below 40% when over 20 independent upstream sources (Claude exempt); cliff past about 600 slice lines and 100 steps; mean slice 393.6 lines, mean chain 93.9 steps; 2,492 tasks, 7 repos, 5 models. Value prediction, not localisation | Li, Su, Lyu 2026 (a14, d15) | established as a trend (with c21); thresholds not switch points |
| Runtime reasoning is weak | Average 44.4% across models; best GPT-4-Turbo 75.0%; Incremental Consistency 10.3 average | REval, Liu et al. 2024 (c21) | single-source |
| Slice context helps repair | Defects4J 483 bugs, DeepSeek-V3: CausalRepair 313 correct vs 157 plain; without source dynamic slice 230 (-26.5%); failing-line-only test side 193 (-38.3%); cost $0.029 per bug | Wu et al. 2026 (a13, d04) | established with BluesFL, SWE-Doctor; see caveats |
| Slice context helps hardware localisation | 19K-line RISC-V core: Top-1 24 bugs vs 13 (Agentless), 7 prior best; without instruction path 5; without signal values checks 88.3 blocks vs 15.4, cost +609% | Liu et al. 2026 BluesFL (b25, c15) | single project, injected bugs |
| Runtime diagnosis helps issue resolution | SWE-bench Verified 75.7% (+2.0, +3.9); Pro 59.4% vs 50.5% / 51.4%; ablation (50 Pro issues, GPT-5.4-mini): removing diagnosis -8.0 points. Cost $0.43 vs $0.23 / $0.22 per issue | Guo et al. 2026 SWE-Doctor (b23, d02) | single-source; not equal cost |
| Tool-computed slices robust to rewrites | Defects4J-Trans: CausalRepair 289 (-7.7%), ReinFix 200 (-15%), plain DeepSeek-V3 97 (-38%) | Wu et al. 2026 (d05) | single-source |
| LLM localisation is fragile to rewrites | 750,013 tasks, 1,307 programs, 10 LLMs; 78% of earlier correct localisations fail after meaning-preserving mutation; misleading names 29.02%, comments 25.63%, dead code 20.38% accuracy | Haroon et al. 2026 (c14, d03) | single-source; no tools, spec only |
| Asking "why?" in a debugger works | ChatDBG, 10 runs, gpt-4-1106: 57% plain "why?", 67% targeted question, 85% after one follow-up with no feedback; C/C++: 36% root-cause fixes, 55% proximate | Levin et al. 2025 (b11, b13, c16) | single-source; student programs |
| Tool navigation beats spectrum-based FL | AutoFL method acc@1 +19.7% (Defects4J), +166.7% / +233.3% (BugsInPy, GPT-3.5 / GPT-4); 798 bugs | Kang et al. 2024 (b14, c18) | single-source |
| Model explanations are mostly not accurate | 300 sampled: 20% accurate, 26.3% with at least one inaccurate statement, 46.7% bland; 56.7% of bugs got at least one accurate explanation | AutoFL (b15) | established with Olausson, LDB (K11) |
| Model feedback is the weak step | GPT-4 repair 33.30% with own feedback vs 52.60% human feedback; introductory 42.64 to 62.21, interview 19.33 to 45.67, competition 3.67 to 14.67; 16 people, 40 programs; self-repair gain vanishes at equal cost | Olausson et al. 2024 (b19, b20, c22) | established |
| Trace feedback is mixed | LDB up to +9.8%; HumanEval 73.8 to 81.1 (SD) to 82.9 (LDB). Breakpoint trace beats resampling on BigCodeBench (29.5% vs 22.4%; text also says 26.7%), ties HumanEval (21 vs 20 of 40), loses LiveCodeBench (4.9 vs 6.5) | Zhong 2024 (a16, b17); Adnan and Kuhn 2026 (a17, d06) | contested |
| Trace token cost break-even | One-trace k=1.15-1.21 needs 13-17% fewer calls; calls fell 16% (BCB), 30% (HE), 3% (LCB); tokens -3.9%, -16.0%, +16.7%. All traces: tokens +28.2%, +19.1%, +48.9% | Adnan and Kuhn 2026 (d07) | single-source |
| Debugger as late tool | SWE-bench-Lite success rewrite / debug / debug(5): GPT-4o 19.1/17.2/23.6; o3-mini 8.5/22.1/19.8; Claude 3.7 37.2/48.4/52.1; o1-preview 10.7/30.2/30.8; Llama-3.3-70B 2.4/4.0/4.8; 3 runs | Lee et al. 2025 debug-gym (c23, d08) | single-source |
| Bounded questions to a debug subagent | GitBug-Java GPT-5 60.2% to 73.1%; Sonnet 4.5 about +13%, Haiku 4.5 about +16%; raw debugger tools flat or worse (for example 64.5, -14.8%) | Garg and Huang 2026 Debug2Fix (d23) | single-source |
| Per-candidate "why this could be it" | SWE-bench Verified file Hit@1 71.4% to 85%; element exact match 36% to 69%; repair +12.8% inside Agentless | Sepidband et al. 2026 RGFL (d22) | single-source |
| Contrast pair beats failing-only | 106 bugs, 3 runs: full 37.00 correct vs no pair 30.67 vs random pair 34.00 | Kong et al. 2024 ContrastRepair (d12) | single-source |
| Hypothesis log with real execution | Real debugger: plausible patch 73% vs 63% imagined; DONE flag with real execution 12.4 points more likely plausible; Defects4J correct fixes v1.2 76 vs 87 plain, v2.0 113 vs 110 | Kang et al. 2023 AutoSD (d11) | single-source |
| Non-witnessing repro tests mislead | SWE-Doctor fail-to-fail tests cost 2-3 issues of 100; VibePass: bottleneck is the fault hypothesis; 12 LLMs, 173 instances | d01, d24 | established (two sources) |
| Where strong agents fail | 16,758 trajectories; 60-69% of failures reached and edited the right functions; Qwen3-8B failures 41.1% at Search | Kim et al. 2026 (d21) | single-source, indirect |
| Graph-guided localisation | SWE-bench-Lite file Acc@5: LocAgent 94.16 vs 90.15 (SWE-agent, OpenHands), Agentless 79.56 | Chen et al. 2025 (d14) | single-source; dependency graph, not a slice |
| Confidence tracks precision | AutoFL Spearman +0.57 / +0.52, five runs per bug; call cap 10 vs 20 (20 halved performance); mean 5.37 calls | Kang et al. 2024 (c18, d09, d10) | single-source; gate costs five runs |

## 4. Mechanisms and models

### 4.1 Backward dynamic slice from a failing output (what to build)

Inputs: a failing run (one test or reproduction), the output value or event that is wrong.

1. Run the program under a tracer. Record, per executed statement instance: statement id, variables read with defining instance, variables written, and the predicate instance that controls it. (Python: `sys.settrace` or a dedicated tool such as ipyflow, used by ChatDBG for notebooks, b12. Java: a bytecode tracer. The Whyline recorded I/O events plus a call graph, c04.)
2. Pick the slicing criterion: the wrong value at its output point.
3. Walk backward over data edges (who wrote this value) and control edges (which branch let this run). Stop at inputs. The union is the dynamic slice.
4. For a why-NOT question ("why did X not happen"): X is a statement or output that did not run. Find predicates on the static call or control path that guard X; find which of them evaluated the wrong way at the relevant time; then slice on those predicate values (the Java Whyline method, a21).
5. Hand the model the slice, ordered by dependence distance from the failure, with the runtime values. Not the whole trace. Evidence: focused answers help, whole traces cost tokens and often do not (K10, d07, d23).

### 4.2 Question-answering layer instead of raw tools

Debug2Fix (d23) and ChatDBG (b11) both put a bounded question in front of the runtime. The main agent asks in plain words ("what is V at line L?", "what exception does X raise?"). A subagent or tool runs the debugger and returns a short answer. Raw debugger commands given to the main agent were flat or harmful. Implementation: a function `ask_runtime(question) -> answer` with a hard cap on calls (AutoFL: 5.37 calls on average, cap 10; cap 20 broke a small-context model, d10), a cap on answer length, and the rule that the answer must contain an observed value.

### 4.3 Late debugger rule (debug(5))

debug-gym (d08): give the debugger only after 5 failed rewrites. It was best or near best for every model tested (GPT-4o 23.6 vs 19.1 rewrite-only; Claude 3.7 52.1 vs 37.2). Weak models given the debugger from the start did worse (GPT-4o 17.2, 4o-mini 3.5). Mechanism guess, not tested: early on, rewrites are cheap and often enough; the debugger is a recovery tool. This maps to the schema: S6 impasse fires after two rounds with no change, so the slice or debugger fits at S6 as an operator, not at S3.

### 4.4 Check the repro before using it

SWE-Doctor and VibePass (d01, d24): a self-made reproduction that does not fail for the reported reason misleads. Code check: run the repro on the unfixed code; compare exception type or the wrong value with the issue text; reject if different (K16).

### 4.5 Per-candidate explanation and contrast

RGFL (d22): for each top-k candidate location, ask the model for a bug-specific "why this could cause the failure, and its limit", then re-rank. ContrastRepair (d12): show the failing test beside the nearest passing test. Both turn on explaining differences, close in spirit to why-not. Neither tested why-not vs why-did.

### 4.6 Confidence gate (not ready)

AutoFL confidence is agreement across five runs, not a token probability (d09). It cannot gate extra steps for free. A cheaper gate would be needed.

## 5. What holds up

**Held up across independent sources**
- Developers lack tools for causal-chain questions (61% unsatisfied; 35% navigation; 42% indirect dependencies; a09, a10, b09, b10).
- LLMs do not produce exact slices unaided (a11, a12, c09, a15): even the best has 7.33% exact match.
- LLM accuracy falls as the causal chain grows (a14, c21, d15).
- A code-computed slice or runtime diagnosis in the context helps repair and localisation (a13, c15, b23).
- Model self-explanation is unreliable (b15, b19, b18, c22); human feedback is much better.
- A reproduction that does not witness the fault hurts (d01, d24).

**Contested**
- Human speedups from asking why: strong effects in small builder-run studies (7.8x, 3x success, 2x speed). The one independent study of a neighbouring tool (Parnin and Orso, d18) found no overall benefit. No independent Whyline replication was found anywhere (K02).
- Traces and runtime info for LLM repair: LDB +9.8% on small benchmarks, trace repair wins one benchmark and loses another (Adnan and Kuhn), debug-gym effect depends on model, Debug2Fix raw tools flat or harmful (K10). Best explanation: a focused answer to a question helps, a raw dump does not; model strength and benchmark matter. No controlled test separates these.
- Whether headroom exists: capable agents mostly reach the right functions and fail at edit quality (d21), while weak models fail at search. So a slice may help weak models more.

**Failed or null results**
- Weiser's claim: later tests null or mixed (d19). The 1982 study tested recognition only.
- Whyline hard task: 4 of 10 vs 0 of 10 (a07); the tool often located but did not explain the bug (a23).
- Why-didn't questions were rarely used when analysis took a minute (a08).
- Parnin and Orso: no effect of rank changes; programmers did not use the list as a ranked list; 61% of time after seeing the fault (d18).
- Self-repair gain disappears at equal cost (b20); LDB self-debugging with explanation or trace failed on StarCoder (b18).
- Fail-to-fail reproduction tests (d01); AutoSD hypothesis log did not beat direct repair on Defects4J v1.2 (76 vs 87, d11).
- Trace-guided repair on LiveCodeBench: 4.9 vs 6.5 for resampling; tokens +16.7% (d06, d07).

**Moderators seen**
- Model strength (debug-gym: strong models gain, weak ones lose or do not use pdb).
- Task difficulty and ceiling (Whyline task 2; Aider no effect).
- Whether the context is a focused slice or a whole trace (d07: all traces cost +19% to +49% tokens).
- Expertise: experts guessed first and asked later; novices asked directly (b06). Anecdote only.
- Delay: why-not analysis of about a minute suppressed its use (a08).
- Benchmark contamination (Defects4J, HumanEval) is untested in most studies (critique).

**Corrections from the critique pass**
- The "2x faster" Java pilot is a cross-study comparison with N=9, not a concurrent control. Use the 2009 N=20 study.
- The "7.8x" is an average of six per-scenario ratios on N=4 vs 5. Do not quote it as a general speed-up.
- a09 and b10 likely share one dataset; "factor of 8" (c05) is a rounding of 7.8, not a second study.
- The c06 author line is wrong; the paper is Ko, DeLine, Venolia.
- The BigCodeBench trace number: the paper gives both 29.5% and 26.7% for the same cell (d06).

## 6. Language models

**Can they slice?** Not exactly. GPT-4o: static Accuracy-D 60.84%, exact match 7.33%; dynamic exact match 0% (a11). Prompt tricks add about 4 points. Top failure cause: complex control flow (39 cases); most errors at declarations and assignments (b22). Agentic slicing with synthesis, verification and refinement fixes much of this on SliceBench (+15.2% accuracy on average, up to +63.1% on large programs, a12), but baselines fail on incomplete code, which favours the LLM, and the authors built the benchmark. Execution-estimation of missing trace steps reaches 80-98% dependency accuracy (a15). Implication: do not ask the model to produce the slice; compute it.

**Do they track long causal chains?** No. Accuracy under 40% past 20 upstream sources; cliff at 600 slice lines or 100 steps (a14). Runtime behaviour reasoning averages 44.4% (c21). Mean test chain was already 93.9 steps, so these thresholds describe the benchmark's difficulty, not a safe switch point (d15).

**Does a computed slice in context help?** Yes in four studies, on different tasks: CausalRepair (313 vs 157 plain; removing the dynamic slice -26.5%, a13, d04); BluesFL (Top-1 24 vs 13, ablation 5, b25); SWE-Doctor (+8.0 points, b23); SliceMate downstream (up to +34% over other slicers, but this compares slicers, d17). None controls token budget. SWE-Doctor cost $0.43 vs $0.23 per issue (d02). CausalRepair also shows robustness to rewrites (-7.7% vs -38% for plain, d05).

**Do they ask good why-questions themselves?** One result: ChatDBG, plain "why?" 57%, targeted 67%, plus one follow-up 85% (b11). The follow-up gave no feedback, so a second look alone may explain part of the gain. Only 36% of C/C++ fixes hit the root cause (b13). RGFL: per-candidate explanations raised file Hit@1 from 71.4% to 85% (d22). No study compares why-not vs why-did vs a hypothesis list. This is the central gap (K17).

**Does runtime information help?** Mixed, see section 5. A pdb tool helps strong models and hurts some weak ones; late availability was best (d08). Raw debugger tools to the main agent: flat or worse; a question-answering subagent: +13% to +22% (d23). Traces cost tokens, and one-trace repair pays back only if calls fall at least 13-17% (d07).

**Do their explanations deserve trust?** No. 20% of AutoFL explanations were accurate (b15). Human feedback lifted GPT-4 repair from 33.3% to 52.6% (b19). Wrong explanations misled StarCoder (b18). Real execution results made the done-signal more reliable (AutoSD, d11).

**Are they robust?** 78% of correct localisations fail after meaning-preserving rewrites, in a no-tools, spec-only setting (d03). A tool-computed slice kept 92.3% of its score (d05). One benchmark each.

**Strong models.** Capable agents mostly reach the right functions and fail on the patch (60-69% of failures, d21). So localisation help has limited headroom for them. The benefit is likely largest for weak models and on long chains. Untested.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Evidence ids in brackets. "Memory" means the S9 lesson or class record.

### Add now (established)

1. **Compute dependence, do not ask the model to guess it.** Where a failing run exists, code computes the backward dynamic slice of the wrong value and passes a short, ordered slice with runtime values to S5. Schema: O5 and S5 (code locates the failing output; matches G2). [E] K06, K08, K05. Evidence a11, a12, a13, d04, b25, b23, a10, b09, b10. Caveat: no equal-token test yet, so gate this behind T1 in section 8 before it becomes default.
2. **Never trust the model's own causal story without an executed check.** A causal claim used in S5 must be backed by an observed value from the run. Schema: G2 and G10, S5. [E] K11. Evidence b15, b19, b18, c22, d11.
3. **A reproduction must witness the reported fault.** Before using a self-made failing test, code compares its failure (exception type or wrong value) with the report. Schema: G3 and S4. [E] K16. Evidence d01, d24.
4. **Expect degradation on long chains.** When a bug's dependence chain is long, do not rely on the model to hold it. Use the computed slice and chunk it. The thresholds (20 sources, 600 lines, 100 steps) are not usable as switches. Schema: O5, S0 gate. [E] K07 as a trend. Evidence a14, c21, d15.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Why-not vs why-did vs hypothesis-list question at S5 | O5, S5 | [S] | K17, K09; d22, b11; no head-to-head |
| Slice vs free exploration at equal tokens | O5 | [C] | K15; d02, d14, d21 |
| Slice as an S6 operator (late) rather than at S3 | S6, O5 | [S] | d08 debug(5); Claude 52.1 vs 37.2 |
| Bounded `ask_runtime` question tool vs raw debugger | S5, S6 | [S] | d23 |
| Per-candidate explanation re-rank | S4, S7 | [S] | d22 |
| Contrast pair (failing vs nearest passing) | S5 | [S] | d12 |
| Confidence-gated extra backward steps | S6 | [S] | K13; c18, d09 |
| Robustness: same bug in mutated copies | G, S7 | [S] | K12; d03, d05 |
| Follow-up turn without new information | S5 | [S] | b11 (57 to 67 to 85) |
| Model-computed slice (SliceMate style) when no tracer is available | O5 | [S] | a12 |
| Required "causal path from suspect to failing output" field | S5 | [S] | K18; d18 (human, one study) |

### Memory

S9 lesson line for this class: record whether the slice or the question changed the outcome, the chain length, and whether a reproduction was needed. Feeds S0 (when to enable O5). [S], no direct evidence.

## 8. Concrete tests on our bench

All arms get the same total token budget, counting setup, tool output and extra calls. Items are failing-run items where a trace is available (ARC program repair items with failing examples; code-puzzle items with unit tests). Metric is pass on held-out checks (G3) unless stated. Use 3 seeds, paired comparison, report CI.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 slice vs free | bugs with a failing test | A: plain agent; B: agent plus code-computed dynamic slice in S5 context; C: agent plus whole trace | Held-out pass; tokens per fix | B over A by 5-10 points on a weak model, near zero on a strong one; C at or below A (d07) |
| T2 question type | same | A: "why did the wrong value occur?"; B: "why did the expected thing not happen?"; C: "list 3 hypotheses, test one"; D: free | Root-cause hit (location and cause match the true fault, not the proximate one) | Unknown. Prediction: B over A for missing-output bugs; C at least equal to A overall (d11) |
| T3 late slice | same | A: slice at S3; B: slice only at S6 after two failed revisions; C: none | Pass; tokens | B at or above A for strong model; A below B for weak (d08) |
| T4 bounded question tool | multi-file bugs | A: `ask_runtime` with answer cap; B: raw debugger commands; C: none | Pass; calls | A over B by 10 points or more (d23) |
| T5 repro witness check | items where agent writes its own repro | A: witness check; B: none | Pass; share of misled runs | A over B by 2-3 points (d01) |
| T6 follow-up turn | items with a first answer | A: re-ask with the same information; B: second independent sample | Pass | Honest control: ChatDBG's follow-up gain may be resampling (b11) |
| T7 robustness | bug plus 3 mutated copies (names, dead code, comments) | A: slice; B: none | Outcome agreement across copies; pass | A loses under 10% vs B over 15% (d05) |
| T8 chain bins | bugs binned by chain length (under 20, 20-100, over 100 steps) | A: slice; B: free | Pass by bin | Gap widens with length (a14) |
| T9 candidate explanation | localisation items | A: per-candidate why plus re-rank; B: re-rank by score only | Hit@1 | A over B by 5 points or more (d22) |
| T10 causal-path field | any | A: require path from suspect to output; B: no field | Pass; wrong-patch rate | Lower wrong-patch rate; cost under 5% tokens (d18) |

## 9. What does not transfer, and why

- **Human speed-ups (7.8x, 3x, 2x).** They come from tiny builder-run samples, students, a cross-study control, and a menu interface for people who cannot see the whole trace. An LLM reads the whole slice at once and has no search-time cost. Do not use them to predict LLM gains.
- **The question menu.** The Whyline restricts questions to what the tool can answer. That is a user-interface fix for people. For an agent the benefit is bounded answers, not menu choice (d23).
- **Novice-expert difference.** Experts speculating before asking (b06) is anecdote and about trust, not a mechanism for models.
- **Weiser's recognition result.** It says programmers recognise slice code. It does not say slicing helps. Not evidence for an agent.
- **Chain-length thresholds.** The 20/600/100 values come from value prediction in Python repos. They are not switch points.
- **Hardware and one-project gains (BluesFL).** Injected bugs in one RISC-V core. The pattern transfers (use the executed path), the numbers do not.
- **Alice, a small educational language.** Bugs in a 3D animation world look little like repository issues.
- **Trace tool timings (2008).** Overhead numbers are from 2008 hardware.
- **Localisation help for strong agents.** They mostly reach the right place (d21); a better localiser has limited headroom.

## 10. Open questions

- Head-to-head at equal tokens: code-computed slice vs the agent's own free exploration on SWE-bench-style tasks (K15). Not found anywhere.
- Does why-not beat why-did beat a plain hypothesis list for an LLM? No ablation of question type exists (K17).
- Independent replication of the Whyline human results. None found in 20 years.
- Original Weiser 1982 statistics (N, tests) remain unread; second-hand accounts disagree on 2 vs 3 programs.
- Why do trace results disagree: focused vs raw, model strength, or benchmark? No controlled split.
- Does the ChatDBG follow-up gain survive an equal-sample control (85% vs 57%)?
- Can a cheap single-run confidence gate replace five-run agreement?
- How often must the agent build the reproduction first, and how is a non-witnessing one detected without ground truth?
- Does tool-computed slicing stay robust to semantic-preserving rewrites on more than one benchmark and model (K12)?
- Contamination: Defects4J, HumanEval and SWE-bench may be in training data; most 2024-2026 results are untested for it.
- "Do Coding Agents Still Need a Debugger?" (2026, d20): title only, could not be opened. May bear on K15.
- Related subfields researched in parallel (links only): Notional machine, mental models; Diagnosability; Readings in model-based diagnosis; Cognitive conflict and impasse; Epistemic value and curiosity; Cognitive biases in software work; Software, spreadsheet, KB debugging; Pre-mortem; Debiasing and cognitive forcing.

## 11. Sources

[V] opened and read; [M] snippet, citation or abstract only.

- [M] Weiser (1982) Programmers use slices when debugging, CACM 25(7). https://doi.org/10.1145/358557.358577 (a01, b27, c07)
- [M] Weiser (1981) Program Slicing, ICSE. https://dl.acm.org/doi/10.5555/800078.802557 (a19)
- [V] Ko and Myers (2004) Designing the Whyline, CHI. https://faculty.washington.edu/ajko/papers/Ko2004Whyline.pdf (a03, a04, a20, a24, a27, b01-b04, c01, c02)
- [V] Ko and Myers (2008) Debugging Reinvented, ICSE. https://faculty.washington.edu/ajko/papers/Ko2008JavaWhyline.pdf (a05, a06, a21, a26, b05-b08, c03, c04, c26)
- [V] Ko and Myers (2009) Finding Causes of Program Output with the Java Whyline, CHI. https://faculty.washington.edu/ajko/papers/Ko2009JavaWhylineUI.pdf (a07, a08, a23)
- [V] Ko, Aung, Myers (2005) Eliciting design requirements for maintenance-oriented IDEs. https://faculty.washington.edu/ajko/papers/Ko2005MaintenanceTasks.pdf (a09, a22)
- [V] Ko, Aung, Myers, DeLine, Venolia (2006) How developers seek, relate and collect. https://faculty.washington.edu/ajko/papers/Ko2006SeekRelateCollect.pdf (b10)
- [V] Ko, DeLine, Venolia (2007) Information needs in collocated software development teams. https://faculty.washington.edu/ajko/papers/Ko2007InformationNeeds.pdf (a10, b09, c06)
- [V] Ko and Myers (2005) A framework and methodology for studying the causes of software errors. https://faculty.washington.edu/ajko/papers/Ko2004SoftwareErrorsFramework.pdf (c05)
- [V] Ko, Myers, Coblenz, Aung (2025) Retrospective on seek, relate, collect. https://faculty.washington.edu/ajko/papers/Ko2025SeekRetrospective.pdf (a02)
- [V] Parnin and Orso (2011) Are automated debugging techniques actually helping programmers? ISSTA. https://chrisparnin.me/pdf/parnin-issta11.pdf (d18, d19); the ACM-page lines a25, b28, c08 were [M]
- [V] Soremekun, Kirschner, Boehme, Zeller (2021) Locating faults with program slicing. https://arxiv.org/pdf/2101.03008 (d16)
- [V] Shahandashti et al. (2024) Program slicing in the era of LLMs. https://arxiv.org/pdf/2409.12369 (a11, a28, b21, b22, c09, c10)
- [V] Chang et al. (2025) SliceMate. https://arxiv.org/pdf/2507.18957 (a12, c11, c12, d17)
- [V] Pei et al. (2025) LLM as an execution estimator (RecovSlicing). https://arxiv.org/pdf/2508.18721 (a15, c13)
- [V] Wu et al. (2026) CausalRepair. https://arxiv.org/pdf/2608.10613 (a13, d04, d05)
- [V] Li, Su, Lyu (2026) RepoReason benchmark. https://arxiv.org/pdf/2601.03731 (a14, d15)
- [V] Liu et al. (2026) BluesFL. https://arxiv.org/pdf/2605.17290 (b25, c15)
- [V] Guo et al. (2026) SWE-Doctor. https://arxiv.org/pdf/2607.00990 (b23, b24, d01, d02)
- [V] Levin et al. (2025) ChatDBG. https://arxiv.org/pdf/2403.16354 (b11-b13, c16, c17)
- [V] Kang, An, Yoo (2024) AutoFL. https://arxiv.org/pdf/2308.05487 (b14-b16, c18, c19, d09, d10)
- [V] Kang et al. (2023) AutoSD. https://arxiv.org/pdf/2304.02195 (d11)
- [V] Zhong, Wang, Shang (2024) LDB. https://arxiv.org/pdf/2402.16906 (a16, b17, b18, c20)
- [V] Olausson et al. (2024) Is self-repair a silver bullet? https://arxiv.org/pdf/2306.09896 (a18, b19, b20, c22)
- [V] Adnan and Kuhn (2026) Limits of execution traces. https://arxiv.org/pdf/2611.09212 (a17, d06, d07)
- [V] Lee et al. (2025) debug-gym. https://arxiv.org/abs/2503.21557 (c23, c24, d08)
- [V] Haroon et al. (2026) Robustness of LLM fault localisation to semantic-preserving mutations. https://arxiv.org/abs/2504.04372 (c14, d03)
- [V] Liu et al. (2024) REval. https://arxiv.org/abs/2403.16437 (c21)
- [V] Chen et al. (2025) LocAgent. https://arxiv.org/pdf/2503.09089 (d14)
- [V] Kong et al. (2024) ContrastRepair. https://arxiv.org/pdf/2403.01971 (d12)
- [V] Chen et al. (2023) Teaching LLMs to self-debug. https://arxiv.org/pdf/2304.05128 (d13)
- [V] Kim et al. (2026) Coherence collapse in code agents. https://arxiv.org/pdf/2603.24631 (d21)
- [V] Sepidband et al. (2026) RGFL. https://arxiv.org/pdf/2601.18044 (d22)
- [V] Garg and Huang (2026) Debug2Fix. https://arxiv.org/pdf/2602.18571 (d23)
- [V] Bansal et al. (2026) VibePass. https://arxiv.org/pdf/2603.15921 (d24; abstract-level numbers)
- [V] Beck et al. (2026) Towards a neural debugger for Python. https://arxiv.org/pdf/2603.09951 (b26)
- [V] Chang et al. (2025) BugCerberus. https://arxiv.org/abs/2502.15292 (c25; abstract numbers)
- [M] Semantic Scholar citation list for Parnin and Orso. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/2001420.2001445/citations (d20)
