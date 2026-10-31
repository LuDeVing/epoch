# Cognitive breakdowns: deep document

*Subfield E09.01, "Chain from slip to defect". Key work: Ko and Myers 2005. Schema parts: G2, G3. Evidence: evidence_a.jsonl (a01-a37), evidence_b.jsonl (b01-b30), evidence_c.jsonl (c01-c27), evidence_d.jsonl (d01-d26). Claims: E09.01-K01 to K42 (claims.jsonl). Cross-check: critique.md. The gap search ran with limited tools (web-search quota used up, arXiv and OpenAlex rate-limited), so "no study found" means "not found by that route", not "does not exist".*

## 1. What it is

A software error is not one random slip. In the Ko and Myers model, an error is the end of a chain. A programmer has a cognitive breakdown (a failure of skill, rule or knowledge). The breakdown puts an error in the code. The error causes a fault and a failure at run time. The programmer then reads the failure wrongly, and that misreading is the next breakdown. The chain repeats until the defect is gone or the person gives up (a01).

Three breakdown classes come from Reason (1990), who took them from Rasmussen:
- **Skill:** a lapse of attention in a routine action. Inattention (strong habit intrusion, interruption, delayed action, interleaving) and overattention (omission, repetition after an attentional check) (a02).
- **Rule:** a wrong or bad rule applied to a familiar situation (favoured rule, problematic signs, information overload).
- **Knowledge:** bounded rationality or a faulty model of the problem. Named biases: selectivity, biased reviewing, availability, simplified causality, illusory correlation, overconfidence, confirmation bias (a03).

Three terms to keep apart:
- **Breakdown:** the cognitive failure (a wrong belief, a lapse).
- **Error:** the wrong thing left in the code or the plan, caused by a breakdown.
- **Failure:** the wrong behaviour seen when the code runs.

The mapping to our agent is direct. A wrong final answer is the end of a chain. The first wrong step (the root) is what we want to find (G2: revise only from real output). Every later step may be a clean repair of a bad premise, so fixing the last visible step can be fixing the wrong thing. A check must come from outside the reasoning (G3: a pass must be on something the answer was not fitted to).

What is human evidence and what is our analogy:
- The chain model is a human finding from 7 novices in one tool (Alice), coded by one analyst, with no replication found (K01, K18).
- That LLM agent failures have the same shape is our reading. A 2026 preprint (TrajDebug, a36) finds a similar pattern: one critical early error, many local errors, most repaired later. No study codes LLM failures with the Ko and Myers scheme (K25, d26).
- The skill/rule/knowledge split was never tested on a model. Treat it as a vocabulary, not a measurement.

Why this subfield matters for the schema: the research that is solid is not about the taxonomy. It is about what feeds the repair step. Repair quality is set by the diagnosis, and the diagnosis is only as good as the signal it is tied to (sections 4.3, 5). That supports G2 and G3 as written, and it adds a few operational rules (section 7).

## 2. History and theories in depth

**Rasmussen and Reason (1990).** The skill, rule, knowledge split and the Generic Error-Modelling System (GEMS). Slips and lapses sit at skill level. Mistakes sit at rule and knowledge level. Active errors (at the sharp end) are separated from latent errors (set up earlier). Not opened this session; known through Ko and Myers (a20, secondhand [M]).

**Earlier debugging literature (secondhand, not opened).**
- Vessey (1985) and Gilmore (1991): debugging searches an unconstrained space. People consider few hypotheses and usually favour one (a22).
- Perkins and Martin (1986): novice Pascal errors were mostly "fragile knowledge", present but not retrieved or applied (a21).
- Ko and Myers cite "almost 90%" wrong initial guesses. This is a cited figure, not a measured one (K03).

**Ko and Myers 2003 (a13, a14).** First version of the model, labelled attentional, strategic and knowledge problems. Same two Alice studies. Only quantitative links in the data, with 7 people: debugging time vs programming time r=.96; errors vs breakdowns r=.95; errors vs chains r=.90; breakdowns vs debugging time r=.84. With n=7 these are fragile.

**Ko and Myers 2004, Whyline design (a15, a16).** Formative studies: about 50% of errors came from false assumptions in hypotheses formed while debugging earlier errors. 68% of questions were "why didn't", 32% "why did". The Whyline lets the person pick such a question and see the runtime events that answer it. Test: six scenarios, with and without the tool, 7.8x faster from failure to diagnosis (F(1,5)=12.64, p<.02).

**Ko, Myers and Aung 2004 (a19).** Different data, same group: 40 non-programmers learning Visual Basic, 130 barriers. Understanding barriers (what the program did, or why) were the largest class: 38 of 130, and 34 of those 38 were insurmountable.

**Ko and Myers 2005 framework paper (a01-a12).** Method: think-aloud video. An analyst finds each runtime failure, traces back to the software errors, then to the breakdowns, with timestamps. Output: ten design heuristics (Table 13). Among them: help programmers consider all relevant hypotheses, help them find causal relations, prevent overconfidence by testing assumptions.

**Ko and Myers 2008 Java Whyline (a17, a18).** A pilot (9 people, median 4 min vs a median of 10 min for 18 Eclipse experts from an earlier study, not concurrent) and a controlled test with 20 people. These are the only experiments that act on the model's main prediction: bad hypotheses drive bad fixes.

**Atoms of confusion (b01-b03, b30).** A parallel human line on reading slips. Gopstein et al. (2017, C, 73 programmers, abstract only [M]) showed small code patterns mislead readers. Langhout and Aniche (2021, Java) replicated about half. See section 5.

**Cognitive bias in software engineering (b04-b09).** Mohanani et al. (2020) mapped 65 studies to 2016. No replications, no families of experiments, no meta-analyses, and no strong evidence for any debiasing technique. Fixation had one study. Wyrich et al. (2022) found anchoring in code-understandability ratings even among professionals.

**Biases in LLMs and in LLM-assisted work (b10-b27).** Jones and Steinhardt (2022) used human bias designs on Codex. Sovrano et al. (2025) built a software-dilemma bias test. Zhou et al. (2026) replicated a human developer bias study with LLM use added.

**2023-2026 LLM line.**
- Self-correction: Huang, Tyen, Kamoi, CRITIC, Tsui.
- Self-repair and self-debug: Chen, Olausson, Zhong (LDB), Ni (NExT), Kang (AutoSD), Arimbur.
- Agent failure analyses: SWE-agent, Majgaonkar, Meng, Mehta, Kim (Coherence Collapse), Liu, TrajDebug, MAST, Who&When, AgentRx, DoVer.
- Pipelines and search: Agentless, AutoCodeRover, SWT-Bench, SWE-Search.
- Only one paper (CogniGent, Samir and Rahman 2026) builds on human-debugging cognition, and it tests localisation only. None uses the breakdown model as a design basis for repair.

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested. Ids refer to the evidence files; K-numbers to claims.jsonl.

### 3.1 Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Errors come from chains of breakdowns | 7 novices, 895 min, 159 breakdowns, 69 roots, 102 errors; 33 errors led to new errors; mean chain 2.3 breakdowns (SD 2.3) and 1.5 errors; 46.4% of time debugging | Ko and Myers 2005 (a04, a05) | S (K01) |
| Coder agreement | about 93% on skill/rule/knowledge on a random 10% of failures; lower on sub-type; one analyst coded all | a04 | S |
| Where breakdowns happen | Implementation 77.4% (skill 22.0, rule 28.3, knowledge 27.0); runtime/debugging 18.2% (skill 8.1, rule 0.0, knowledge 10.1); specification 4.4% | Table 10 (a06) | S |
| Debugging breakdowns drive wrong fixes | the 18% made while forming hypotheses about a failure were behind nearly all of the 24% rule and skill breakdowns in modifying code (authors' reading, not a computed attribution) | a07 | S (K02) |
| False hypotheses cause about half of errors | about 50% of errors tied to false hypotheses while debugging | Ko and Myers 2004 (a15) | S |
| Initial guesses mostly wrong | "almost 90%" wrong; cited, not measured | a17, a22 | S, secondhand (K03) |
| Complex Booleans top cause | 33% of all breakdowns involved numerical and Boolean expressions; algorithms 37 (23.3%), language constructs 35 (22.0%) | a09 | S |
| Copy-paste reuse breakdowns hide | 7% of breakdowns; with understanding breakdowns, the longest debugging times | a10 | S |
| Hidden failure keeps a wrong fix alive | P2 bounce bug unnoticed about 20 min after the camera moved | a08 | S (anecdote) |
| Understanding barriers dominate for learners | 38 of 130 barriers; 34 of 38 insurmountable (40 non-programmers) | Ko, Myers, Aung 2004 (a19) | S |
| Whyline speeds diagnosis (scenarios) | 7.8x faster failure-to-diagnosis, 6 scenarios, F(1,5)=12.64, p<.02; 40% more tasks (3.20 vs 2.25, p<.02); 330 s vs 38 s example | a16 | S (K04) |
| Whyline, Java pilot | median 4 vs 10 min; 9 people vs 18 Eclipse experts from an earlier study, p<.05 | a17 | S |
| Whyline, controlled | Task 1: 10/10 vs 3/10 solved (chi2=10.6); task 2: 4/10 vs 0/10; Whyline users opened a median of 3 files, controls hundreds | a18 | S |
| Seeing the fault line is not understanding it | 34 students. Of 10 who clicked the fault line, 9 kept inspecting about 10 more minutes (61% of their time). Tetris mean 12:42 (tool) vs 14:14 (no tool), significant; NanoXML no effect. Moving the fault from rank 7 to 35, or 83 to 16, changed nothing significant | Parnin and Orso 2011 (d24) | S (K42) |
| Atoms of confusion raise novice misreading (Java) | 132 started, 96 finished; 80 snippets, 14 atoms; pooled odds ratio 3.82 (95% CI 2.69-5.42); 7 of 14 atoms individually significant; rated harder in 10 of 14; infix precedence not significant; 7 C atoms had no Java form | Langhout and Aniche 2021 (b01, b02) | E (K26) |
| Anchoring survives expertise | N=256 (206 students, 50 professionals); path 0.165, p<.001, R2 .223; role and scenario-by-role not significant | Wyrich et al. 2022 (b08, b09) | S (K31) |
| Bias share in LLM-era developer work | 14 developers, 2,013 actions: 47.14% biased vs 45.72% of 2,084 earlier; reversals 25% (505/2013) vs 52.9% (1104/2084) earlier | Zhou et al. 2026 (b15) | S (K30) |
| LLM-use actions: more biased, more reversed | 808 LLM actions: 53.7% biased, 29.4% reversed (238/808); 15-category scheme 56.4% biased | b16 | S |
| Fixation is the worst | 76 LLM actions, 33 reversed (43.4%), 7 participants; instant gratification 46/156 (29.5%); suggester preference 22/102 (21.5%); memory bias 26/80 (32.5%) | b17 | S |
| Sleep loss halves novice correctness | N=45 (23 vs 22); correctness -49.73%, CI -1.58 to -0.20; syntax-fix edits +54%; engagement CI -1.31 to 0.04 and process CI -1.18 to 0.15 include zero | Fucci et al. (b28, b29) | S (K33) |
| SE bias literature is thin | 65 studies to 2016, 37 biases, 47 empirical; debiasing covered 6 of 37; zero replications, families or meta-analyses; none gave strong evidence for any debiasing technique | Mohanani et al. 2020 (b04-b07) | S (K32) |

### 3.2 Language-model studies: self-correction and repair

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Self-review without a signal hurts | GPT-3.5: CommonSenseQA 75.8 to 41.8, GSM8K 75.9 to 74.7, HotpotQA 26.0 to 25.0. GPT-4: GSM8K 95.5 to 89.0, CSQA 82.0 to 80.0, HotpotQA 49.0 to 43.0 (five-call row) | Huang 2024 (a26, c04, c05) | E (K05) |
| Models flip right answers to wrong | correct-to-wrong changes outnumber wrong-to-correct | c05 | E |
| Survey: only external feedback works | no prior work shows success with feedback from a prompted LLM outside suited tasks; works with reliable external feedback (code interpreter); fine-tuning enables it; papers to May 2024 | Kamoi 2024 (d03) | E |
| Tool-grounded critique helps, ungrounded is unstable | CRITIC w/o tool -1.8 on one set (text-davinci-003); 2-3 rounds give most of the gain; self-evaluation of own answers 54% on HotpotQA, near chance | Gou 2023 (d04) | E |
| Finding the faulty step is the weak part | GPT-4 52.87 best step-level accuracy (2,186 traces, 5 tasks) | Tyen 2024 (c06) | E (K06) |
| Locate then fix works | gain on wrong traces, true vs random location: arithmetic +43.92 vs +20.39; Dyck +36.86 vs +21.57; shuffled objects +23.53 vs +11.76; loss on correct traces -11 to -15 | Tyen (c07) | E |
| Self-repair bounded by diagnosis | at equal cost 1.05x of pass@20 and 0.97x of pass@22 (GPT-4, APPS) | Olausson 2024 (a24) | S (K07) |
| Human diagnosis beats model diagnosis | repair success 52.60% vs 33.30% (intro 62.21 vs 42.64; interview 45.67 vs 19.33; competition 14.67 vs 3.67); GPT-4 feedback inaccurate 32/80 vs 7/80 for humans; uncertainty expressed 0/80 vs 7/80; 40 programs, 16 people | a25, c09 | S |
| Stronger feedback model lifts repair | GPT-4 feedback for Code Llama, and for GPT-3.5, beat self-repair | c08 | S |
| Execution feedback is the carrier | MBPP baseline Codex/GPT-3.5/GPT-4/StarCoder 61.4/67.6/72.8/47.2; unit tests 69.4/72.2/80.6/52.2; +explanation 69.8/74.2/80.4/52.2; +trace 70.8/72.8/80.2/53.2 | Chen 2024 (a29) | E (K08) |
| Explanation alone adds little | Spider: Codex 81.3 to 84.1; GPT-3.5 71.1 to 72.2; GPT-4 73.2 to 73.6; StarCoder 64.7 to 64.9 | c02 | E |
| Debugging saves samples | one debugged greedy program on TransCoder beats 5 baseline samples | c03 | S |
| Real state beats imagined state | LDB: HumanEval GPT-3.5 73.8 to 82.9 vs 81.1 for Self-Debugging; Reflexion seeds 91.5 to 95.1 vs 92.1; up to +9.8%; model-written traces did not help StarCoder | Zhong 2024 (c12, c13) | E (K09) |
| Trained trace reasoning | NExT: +26.1 absolute MBPP-R, +14.3 HumanEval-R (needs training) | Ni 2024 (a31) | S |
| Real vs imagined debugger output | real: DONE bugs 12.4 points more likely to have a plausible patch; imagined: 11 points less likely. Human study 20 people (6 professionals): explanations raised accuracy in 5 of 6 bugs | Kang 2023 AutoSD (d05) | S (K20) |
| Models cannot simulate execution | REval 44.4% average accuracy at runtime behaviour; incremental consistency 10.3 | Chen 2024 (c26) | S |
| Signal comparison (provisional) | failing message vs bare pass/fail +12.9 to +13.4 points (abstract only); "code must change" instruction +0.8 to +1.9 repair; 9,790 programs, 6 models; only about 16% of failing programs repaired | Kim 2026 (d23) | S, abstract only (K41) |
| Variable-state traces carry a repair loop | BigCodeBench Pass@1: full 89.04; without instrumentation 78.51 (-10.5); without iterative repair 53.77; without rollback 84.55 (-4.5); without lesson memory 86.75 | TraceCoder (d21) | S, confounded |
| Raw error text helps every modern model | 7 models; HumanEval +4.9 to +17.1 pp; MBPP +16.0 to +30.0 pp; name errors repaired about 77%, assertion errors about 45%; two rounds capture 76-95% of gain; self-repair matches or beats resampling in tokens except at 8B | Arimbur 2026 (d22) | S |
| Reflection needs tests | Rust, 50 problems: base 0.60; no tests 0.52; no reflection 0.60; full 0.68; HumanEval 91.0 | Reflexion (c14, c15) | S (K17) |
| Reasoning models have a small blind spot | 14 non-reasoning models: blind spot 64.5% average; "Wait" cut it 89.3%; DeepSeek-V3 0.567 to 0.902 with Wait vs R1 0.908; Qwen3-32B 0.045 / 0.793 / 0.894; fine-tuning on 5,306 traces cut it 76.0% | Tsui 2025 (d01, d02) | S (K19) |

### 3.3 Language-model studies: bug types, agents and failure analysis

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Defect type sets difficulty | GPT-4: missing colons 93.6%, undefined objects 81.7%, operation error 68.6%, variable error 63.1%, triple bugs 58.9%, quadruple 55.9%. GPT-3.5: 80.9 / 49.5 / 38.7 (colons / operation / quadruple). 4,253 instances | DebugBench (a27, c10) | E (K10) |
| Tracebacks help surface bugs, not logic | traceback improves syntax and reference bugs, lowers logic resolution (gpt-4-0613, gpt-3.5) | a28, c11 | S (K11) |
| Model-made defects are structural | over 40% of syntactic characteristics are missing or wrong code blocks; commonest semantic error is a wrong or missing condition | Wang 2025 (c24) | S |
| Most common bug in LLM code is misreading | misinterpretation 20.77% of 333 bugs; 80% of 34 practitioners often or always meet bugs in LLM code | Tambon 2024 (b27) | E with a33, a34 (K35) |
| Agents find the file, miss the fix | 72-81% of failing trajectories located the file; successes over 90%; failures longer by 12.6% / 18.5% (SWE-agent Lite / Verified), 31.0% / 82.5% (OpenHands) | Majgaonkar 2025 (a33) | E (K12) |
| Failure is wrong implementation | 248 unresolved: 52.0% wrong or over-specific implementation, 23.4% failed-edit recovery. Resolved median 12 steps, $1.21; unresolved mean 21 steps, $2.52 | SWE-agent (c18, d08) | E |
| Strong models fail after the right edit | 16,758 trajectories, 7 models. SWE-Agent failures: right functions edited but patch wrong GPT-5 68.1% (n=163), GPT-5-mini 69.1%, Qwen3-Coder 66.8%, Qwen3-235B 64.7%; weighted 56.9% of 1,607 vs 19.3% search failures. Weak Qwen3-8B fails upstream (Search 41.1%) | Kim 2026 Coherence Collapse (d16) | S (K36) |
| Correct patch written, then destroyed | 39.7% of Edit-Quality failures on SWE-bench (n=914); 5 of 5 mid-run edits passed the full suite when re-run; GPT-5 on 500 instances: baseline 66.0%, oracle trigger 70.6% (+4.6, p<.001), consensus-of-3 trigger 69.0% (+3.0, McNemar p=0.08, precision 52.4%) | d17 | S (K37) |
| Flawed reasoning and strategy fixation | 150 hand-coded failures; about 65% flawed reasoning, 25% knowledge, 10% environment; flawed-reasoning runs took 3.5x more steps; OpenHands 80% of successes within 25 rounds, 80% of failures need 54; kappa 0.72-0.77; Expert-Executor resolved 24 of 108 previously failed (22.2%) | Liu 2025 (d18) | S (K38) |
| Right file is not a right fix | repair after a file hit 82.2% and 69.6% (two systems); 96 of 500 unsolved by any tool; 181 solved by all | Meng 2025 (d15) | S |
| Silent semantic failure | 1,750 trajectories, 50 tasks, 4 models. GPT-5 submits 100%, resolves 44%; Llama 4 99% / 18%; Gemini 70% / 50%. Silent semantic failure in 80% (Llama 4) and 68% (GPT-5) of failing runs | Mehta 2026 (a34) | S |
| Interpretation prompt guard did nothing | Claude 65.2 to 64.8 | a34 | S |
| Action bias | pre-fixed bug: models still edit correct code in about 60-90% of runs (range not checked at figure level); GPT-5 abstains cleanly 40% | a35 | S (K13) |
| Best-of-3 | Claude 65 to 74; GPT-5 44 to 58 | a35 | S |
| Loop detector | 3-gram detector caught 100% of Gemini's no-submit tasks, no false positives | a35 | S |
| Local errors mostly repaired | 50 failed trajectories: 381 local errors (7.62 each); of 331 non-critical, 205 (61.9%) repaired, 104 (31.4%) persist, 22 (6.6%) dormant | TrajDebug (a36) | S (K14) |
| Finding the critical step is hard | TrajDebug 34.11% macro accuracy vs 25.69% direct prompting | a36 | S |
| Log readers are poor | Who&When best step accuracy 14.2%; all-at-once 12.50 (below random 19.06); step-by-step 25.51; binary search 23.98; hand-crafted systems 5.26-7.02 vs random 4.16 | Zhang 2025 (d11) | S (K23) |
| Constraint checks improve step location | tau-bench 18.8 to 42.7; Magentic-One 22.7 to 36.4; RelWork 32.6 to 61.5; ablation 29.9 to 42.7; still under 50% on tau-bench. The 18.8 baseline was re-run by the AgentRx authors with a modified prompt; it is not the original 14.2 | AgentRx 2026 (d19) | S (K39) |
| Intervention beats log reading | 18-28% of failed trials flipped to success; 30-60% of hypotheses validated or refuted; GSMPlus with AG2 49% recovered; several different single-step fixes can each repair one failure | DoVer 2026 (d20) | S (K40), abstract-level |
| Backtracking with a value signal helps | SWE-Search: 23% average relative gain over five models; value function 73% accurate; debate selection 84%; free jump without search +1.4% | d12 | S |
| Syntax edit gate | SWE-agent Lite: edit with lint 18.0%, without 15.0%, no edit tool 10.3%. 51.7% of 2,294 runs had a failed edit. Eventual success 90.5%, but 57.2% after one failed edit | d09, c17 | S (K24) |
| Reproduction tests as selector | Agentless Lite: majority vote 77 (25.67%), +regression 81 (27.00%), +reproduction 96 (32.00%); $0.70 mean; upper bound 126. SWT-Bench filter precision 47.8%, recall about 20% | c19, d06, d14 | E (K21) |
| Reproduction tests are often wrong | 213 of 300 reproduced the issue; only 94 also passed on the golden patch. Of 500 scripts, 384 (76.8%) changed status with the golden patch (80.4% when the issue has repro steps; 64.0% with too little info) | d07, c21 | E |
| Pipeline vs agent | Agentless 32.00% Lite; AutoCodeRover 19.00% one run, 26.00% best of 3, SBFL variant 22.00% | c19, c27 | C (K16) |
| Passing tests is not proof | 7.8% of "correct" SWE-bench patches fail developer tests; 29.6% of plausible patches behave differently; 32.67% leakage; 31.08% weak tests; 12.47 to 3.97% after filtering, 0.55% on newer issues | c22, c23, c20 | E (K15) |
| Overthinking | 4,018 SWE-bench Verified trajectories; reasoning models about 3x higher overthinking score; lowest-overthinking of k=2: 27.3% at 43% less cost; k=3: 30.3%, 15% less cost | Cuadron 2025 (d13) | S (K22) |
| Cognitive-style localiser | CogniGent: MAP +23.33-38.57%, MRR +25.14-53.74% on 591 bug reports; no-investigation ablation MAP 0.183 (-19.02%) | a32, d25 | S, preprint |
| Failure taxonomy is reliable | MAST: 14 modes, kappa 0.88 (150 traces), 1,600+ traces, LLM annotator 94% (kappa 0.77); failure rates 41-86.7% across 7 systems; wrong assumption 6.8%, premature termination 6.2%, incorrect verification 9.1% | d10, c25 | S for our purpose |

### 3.4 Language-model studies: human-like slips and biases

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Framing lines are copied | Codex accuracy down 22.3-30.5 points; framing line copied in 81% (Codex) and 70.7% (CodeGen) vs 4.5% and 0.0% on clean prompts | Jones and Steinhardt 2022 (b10) | E (K27) |
| A wrong cue beats the spec | conflicting function name: 100% to 4.4-4.6%; order flip 50% to 17% (75% of flipped errors unary-first) | b12 | E |
| A prepended near-correct function anchors | anchor functions lowered accuracy at every tested prompt size (read from figures); renaming the anchor changed little | b11 | E |
| A rare, costly slip | Codex deleted files on at least 80% of prompts with 3 or more imports, vs correct on 90% with 2 or fewer | b13 | S |
| GPT-3 anchoring replication | 14 of 15 questions; when the estimate moved it equalled the anchor 67% of the time; about 41% gibberish | b14 | S |
| Bias cues flip correct answers | 16 seed tasks, 8 biases, 6 systems; average sensitivity 5.9% (anchoring) to 35.3% (hindsight); rises with inference depth for 5 of 8 biases, up to 49% | Sovrano 2025 (b19, b20) | E (K27, K28) |
| Awareness is weak | bias-awareness score 0.5-0.8 yet high sensitivity; awareness prompts reduced primacy slightly (GPT-4, Llama-2 7B); rewriting the prompt to remove the bias cue worked best (GPT-4 left 0% group-attribution, 2.7% framing) | Echterhoff 2024 (b21, b22) | E (K28) |
| Tuning raises bias | Flan-T5, Mistral-Instruct, GPT-3.5, GPT-4 show more decoy, certainty and belief bias than base counterparts | Itzhak 2023 (b23) | S (K29) |
| One irrelevant sentence breaks math solving | of greedy-solved problems no more than 18% solved for all irrelevant-context types; under 30% of base problems consistently solved; self-consistency with 20 samples +11 points micro (zero-shot CoT +35.5); right answer among 20 samples for 99.7% | Shi 2023 (b24) | E |
| Model surprise tracks human confusion | 24 people, 72 Java snippets; Spearman rho 0.47 (confusing) vs 0.05 (clean); perplexity detector found 64% of labelled atoms, 227 regions flagged | Abdelsalam 2025 (b25, b26) | S (K34) |

## 4. Mechanisms and models

**4.1 Chain model as a data structure.** Each step has a type (decision, edit, observation, belief update), a parent and evidence. A breakdown is a step whose belief is wrong. An error is an edit that follows from it. A failure is an observed result. A misread failure creates a new breakdown. For the agent: log per step a "belief about the cause" and the "observation that tests it". Chain length is the count of dependent steps after the first wrong belief. Root = the first wrong belief with no wrong parent (a05). TrajDebug (a36) uses the same idea with different names: local errors (381 in 50 trajectories), one critical error, and an error lifecycle (repaired, persistent, dormant).

**4.2 Why a wrong hypothesis is reinforced.** The path in a07: see failure, form one hypothesis (biased reviewing), edit (wrong modification), then problematic signs (the failure is hidden, so the fix seems to work) and illusory correlation (belief it is fixed). Agent version: one hypothesis, a patch, a test that does not exercise the defect, a "done" claim. This is the silent semantic failure of Mehta (a34): a plausible patch on every run, the same misreading each time. Strategy fixation is the same loop seen from outside: flawed-reasoning runs took 3.5x more steps (d18), and in human LLM-assisted work developers re-pasted the same fix after an error (43.4% of those actions reversed, b17).

**4.3 Signal quality model.** A repair step is new code = f(old code, diagnosis). The gain depends on diagnosis accuracy.
- Diagnosis from the same model, no signal: gain around zero or negative (Huang; Olausson 0.97-1.05x; CRITIC without tool -1.8).
- Diagnosis from real execution: about +7 to +8 points on MBPP (Chen); up to 9.8% (LDB); raw error text +4.9 to +30 pp (Arimbur).
- Diagnosis from the failing message rather than bare pass/fail: about +13 points (Kim 2026, abstract only).
- Diagnosis from a human or stronger model: 33.3% to 52.6% (Olausson).
- Diagnosis from imagined execution: negative (-11, Kang) or no help (Zhong).
The variable is the reliability of the signal, not the existence of a reflection step. Implement: a repair step accepts only a diagnosis tied to an observed output (a failing test message or real variable values). This is G2 stated as an interface rule.

**4.4 Locate then repair.** Split self-correction into two calls (Tyen). Step 1 finds the faulty step. Step 2 regenerates from there. Step 1 is the bottleneck (best 52.87). A wrong location costs 11-15 points on traces that were right. So the location must come from a check (test, trace, diff), not a vote of the same model. LLM log readers are weak (Who&When 14.2%, TrajDebug 34.11%), so an LLM reading the log is not a safe rollback trigger on its own.

**4.5 Hypothesis-experiment loop (AutoSD, CogniGent).** Write a hypothesis and a prediction, run an experiment (debugger command), read the real output, then conclude. The value is in the real output (d05: +12.4 with real output, -11 with imagined). In CogniGent, removing hypothesis testing costs the most among its parts (a32, localisation only). Loop: H, predict, run probe, compare, keep or drop H.

**4.6 Whyline mechanism.** After a failure, take the question the person asks ("why didn't X happen?"), find the unchecked assumption inside it, and show the runtime events that answer it. Agent version: after a failed test, state "why did this fail / why did X not happen", list the assumption inside, and run a probe on it. Untested on LLMs (K04, gap 7). The Parnin and Orso result adds a warning: seeing the right line is not the same as understanding it (d24), so the probe must test the causal story, not just point at a location.

**4.7 Gates.** SWE-agent's lint gate rejects a syntax-breaking edit and shows the error: 15.0 to 18.0. After one failed edit the chance of eventual success drops from 90.5% to 57.2%, so a failed edit needs an immediate recovery rule (revert, re-read). An "is a change needed" gate would run the failing test first and stop if it passes (K13, untested).

**4.8 Stop rule in both directions.** Action bias (editing correct code, a35) and analysis paralysis (planning without acting, d13) are opposite faults. One rule fits both: act only on an observed failure, and stop when the test passes. A 3-gram loop detector gave 100% recall with no false positives on Gemini's no-submit tasks (a35). Early submits also succeed more (93.0% of resolved runs submitted before budget exhaustion vs 69.0% overall, d09).

**4.9 Reproduction as selector.** Generate a fail-to-pass test. Use it to rank candidate patches (Agentless +15 fixes from 81 to 96). Check that the test fails on the original and passes on the candidate. A test can reproduce a symptom and still not verify the fix (94 of 213), so it is itself a hypothesis and can be a wrong first belief that then gets trusted (d07). An unrelated reproduction script can derail a run (d15).

**4.10 Freeze a verified state (new).** Coherence Collapse (d17): some agents write a patch that passes the full tests mid-run, then change it into a wrong one (39.7% of edit-quality failures). Mechanism: keep the last state that passed the failing test. Allow a change only with a stated reason and a passing test on the new state. The oracle trigger gave +4.6 points (p<.001). A cheap consensus trigger gave +3.0 (p=0.08, not significant). Only 5 cases were tested for recovery.

**4.11 Trigger from checks, not from reading (new).** AgentRx (d19) turns tool schemas and policies into step constraints, runs them, and gives the violations to the judge. Step accuracy rose from 18.8 to 42.7 on tau-bench. For code, the analogue is failing tests, syntax checks and diff-size checks. DoVer (d20) goes one step further: test a root-cause guess by changing one step and re-running, instead of reading the log. It also warns that several different single-step changes can each repair one run, so "the" error step may not be unique.

**4.12 Slip flag from model surprise (new, speculative).** The model's own token surprise is higher on confusing code (rho 0.47 vs 0.05 on clean code, b25) and a peak detector found 64% of labelled atoms (b26). The false-alarm rate is unknown. This could be a cheap flag for "read this part again with a tool", but no one has tested it on agent plans or patches.

**4.13 Cue discipline (new).** Models copy irrelevant or misleading context (81% copied framing lines, 100% to 4.4% with a conflicting function name, b10, b12). Awareness instructions do little (b21, b22, K28). What worked in a human-bias test for LLMs was rewriting the prompt to remove the cue (b21) and sampling many times (b24). Structural steps (restate the spec in own words from the original text, check the name against behaviour) are the natural candidates. Not yet tested on debugging.

## 5. What holds up

**Replications and failed replications.**
- Ko and Myers 2005: no independent replication and no failed replication found (K18). The skill/rule/knowledge shares are one sample of 7 novices in Alice, coded by one analyst. A systematic map found zero replications in software-engineering bias research to 2016 (b05). Reason, Gilmore, Vessey and Perkins and Martin were not opened. Parnin and Orso 2011 was opened but studies a localisation tool and does not re-measure the shares.
- Atoms of confusion (the one clean replication in this subfield): the C finding (73 programmers, abstract only) was replicated in Java. Pooled odds ratio 3.82, but only 7 of 14 atoms individually significant, 7 C atoms had no Java form, and perceived confusion and actual error disagreed for some atoms (b02). So the effect exists, and it is language specific. Experts untested.
- Zhou et al. 2026 partly replicated Chattopadhyay et al. 2020: the biased-action share matched (47.14% vs 45.72%) but the reversal rate did not (25% vs 52.9%). Different samples and tools, so this is a partial replication, not a clean failure.
- Anchoring in Wyrich 2022 is a conceptual replication with a weaker anchor. It held, and expertise did not protect.

**What converges across independent work.**
- Without an external signal, self-review does not help (Huang, Tyen, Olausson, Kamoi, CRITIC). Established.
- Real execution output is what moves the numbers (Chen, LDB, AutoSD, Reflexion ablation, Arimbur, TraceCoder). Established.
- Agents mostly locate the file and miss the fix (Majgaonkar, SWE-agent, Mehta, Meng, Kim). Established. For strong models the wrong patch after the right edit is the main failure (56.9% vs 19.3% search, d16).
- Logic and multi-bug cases are harder than surface slips (DebugBench, Wang, Arimbur: name errors 77%, assertion errors 45%). Established.
- Test-based success claims overstate real fixes (Wang 2026, SWE-Bench+, Agentless Lite-S). Established.
- Models are pulled by misleading cues (Jones, Sovrano, Shi, Echterhoff). Established across tasks, but measured mostly on non-debugging tasks.

**Tensions and moderators.**
- Self-correction hurts (Huang) vs self-debugging helps (Chen, Reflexion). Resolved by the signal: execution feedback or tests.
- Reasoning models have a small or negative self-correction blind spot on injected errors, and "Wait" restores most of it for base models (Tsui). So the 2023-2024 negative result is tied to non-reasoning models. Not tested on real code defects at equal tokens (K19). This also touches G1 (doubt only on a signal): a forced Wait is a scheduled doubt, so it would need to pass a test before it enters the schema.
- Tracebacks help syntax and reference bugs but not logic bugs (DebugBench, K11), yet raw error text helps assertion failures less than name errors (Arimbur). Moderator: bug class.
- Explanation alone: +2-3 points on Spider, none on strong models (Chen). Model-written traces: no help (Zhong).
- Reproduction-first vs open agent choice: contested (K16). Agentless got 32.00% in 2024; AutoCodeRover's SBFL gain was small. SWE-agent's interface effects (3.0 to 7.7 points) mean pipeline vs agent gaps are confounded with model and harness. Localisation is not the main failure for strong agents (d16, d18), which also weakens the pipeline story.
- Where do failures start? Pipelines fail early (wrong localisation), agents fail late (looping on a failed strategy) (d18). Both are in the data.
- Anchoring: weakest effect in Sovrano (5.9%), yet lowers code accuracy in Jones. Different tasks and measures. Not reconciled.
- Zhou: biased actions are as frequent as in 2020 but reversals halved. Either LLMs help recovery, or the samples differ. Not separated.
- Whyline results: all from the creators, small samples; the Java pilot compared against a different, earlier group of 18 Eclipse users.
- Contamination: over 94% of SWE-bench issues pre-date model cutoffs (c23). All SWE-bench numbers carry that doubt.
- Evidence age: most LLM results use 2023-2024 models. 2025-2026 items (Mehta, TrajDebug, Majgaonkar, Samir, Tsui, Cuadron, Kim, Liu, AgentRx, DoVer, Arimbur, TraceCoder, Zhou, Sovrano) are mostly single preprints.

**Interventions that worked.**
- Real execution feedback; real variable state per block; failing message over bare pass/fail (provisional).
- A stronger or human diagnosis; locator then repair with a true location.
- A syntax-lint edit gate; reproduction tests as selector.
- "Wait" recheck on non-reasoning models (injected errors only).
- Best-of-3; backtracking with a value signal (+23% relative); lowest-overthinking selection.
- Rewriting the prompt to remove a bias cue (b21); sampling many times against distractors (b24).
- Oracle freeze of a passing patch (+4.6, p<.001; oracle needs a reference).
- Constraint-check triggers for step location (18.8 to 42.7, not code).
- Expert-Executor review on previously failed issues (22.2%; regression to the mean possible).

**Interventions that did not work.**
- Reflection with no tests (Reflexion Rust 0.60 vs 0.60).
- Explanation alone on strong models; model-written dry-run traces.
- A pre-edit "state your interpretation" guard (Claude 65.2 to 64.8).
- An LLM reading logs to find the decisive step (Who&When 14.2%, below random in one setting).
- Tracebacks on logic bugs.
- Unrelated reproduction scripts (can derail a run).
- A "code must change" instruction (+0.8 to +1.9 repair only).
- Bias-awareness instructions (small, inconsistent).
- Human debiasing: no technique had strong evidence in 65 studies (b06).
- Consensus-based rollback trigger (+3.0, p=0.08, not significant).

## 6. Language models

**How they behave.**
- Surface slips are easy: GPT-4 93.6% on missing colons, 81.7% on undefined objects (a27). Newer models repair name errors about 77% (d22).
- Logic and multi-bug cases are hard: 68.6% on operation errors, 55.9% on quadruple bugs; GPT-3.5 38.7% on quadruple bugs. Assertion errors about 45% (d22).
- Their own diagnosis is unreliable and never uncertain: GPT-4 feedback inaccurate in 32 of 80 cases, uncertainty in 0 of 80; humans inaccurate in 7 of 80 and uncertain in 7 of 80 (a25).
- Repair at equal cost gives 1.05x and 0.97x of drawing fresh samples (a24). Repair is not a free gain. Arimbur (2026) finds self-repair matches or beats resampling in tokens for 6 of 7 modern models, with the first two rounds carrying most of the gain.
- Self-review without a signal flips right answers to wrong: GPT-3.5 CommonSenseQA fell 33.9 points; GPT-4 GSM8K fell 6.5.
- Runtime prediction is poor: 44.4% average accuracy, consistency 10.3 (REval). This agrees with the -11 point result for imagined output (d05).
- Agents find the file (72-81% of failing runs still located it) and then submit a plausible wrong patch. Silent semantic failure covers 68-80% of failing runs (a34). Failing runs are longer and do not abandon wrong paths (a33).
- Strong agents often have the right function edited when they fail (56.9% weighted), and 39.7% of those had a correct patch at some point (d16, d17).
- Many failed trajectories contain many local errors, mostly repaired (61.9%); the failure is decided by one early critical error (a36).
- Action bias: they edit correct code in roughly 60-90% of already-fixed cases (a35). Reasoning models also plan too long without acting (d13).
- Failed edits cascade: success falls from 90.5% to 57.2% after one failed edit (d09).
- Cue sensitivity: framing lines copied by 81% (Codex), a conflicting function name cuts accuracy from 100% to 4.4%, a wrong first operation order cuts 50% to 17% (b10, b12). Newer models still flip 5.9-35.3% of correct answers under bias cues, more with deeper reasoning (b19, b20).
- Tuning does not remove bias and may raise it (b23).
- Reasoning models: almost no self-correction blind spot on injected errors, and "Wait" brings base models near them (d01, d02). On real code defects this is untested.

**What changed behaviour, and by how much.**

| Change | Effect |
|---|---|
| Unit-test results to the model | +7 to +8 points on MBPP (GPT-4 72.8 to 80.6; Codex 61.4 to 69.4) |
| Raw error message, modern models | +4.9 to +17.1 pp HumanEval, +16.0 to +30.0 pp MBPP (7 models) |
| Failing message vs bare pass/fail | +12.9 to +13.4 points (abstract only) |
| Real per-block state (LDB) | HumanEval GPT-3.5 73.8 to 82.9; up to +9.8% |
| Instrumented traces in a repair loop | -10.5 when removed (confounded) |
| Human instead of GPT-4 diagnosis | 33.3% to 52.6% repair |
| True fault location | +43.92 vs +20.39 random (arithmetic) |
| Lint edit gate | 15.0% to 18.0% |
| Reproduction-test selector | 77 to 96 fixes of 300 (81 with regression tests alone) |
| "Wait" recheck (non-reasoning) | DeepSeek-V3 0.567 to 0.902; blind spot cut 89.3% on average |
| Tree search with value signal | +23% relative (five models) |
| Best-of-3 | Claude 65 to 74; GPT-5 44 to 58 |
| Lowest-overthinking pick of 2-3 | 27.3-30.3% at lower cost |
| Oracle freeze of a passing patch | GPT-5 66.0 to 70.6 (p<.001); consensus trigger 69.0 (p=0.08) |
| Constraint-check trigger | step accuracy 18.8 to 42.7 on tau-bench (not code) |
| Cognitive-style multi-agent localiser | MAP +23.33-38.57% (localisation only) |
| Prompt-only interpretation guard | Claude 65.2 to 64.8 (no change) |
| "Code must change" instruction | +0.8 to +1.9 repair |
| Prompt rewrite to remove bias cue | GPT-4 group-attribution bias to 0%, framing to 2.7% (not code) |

**Not in the evidence.** No LLM test of the skill/rule/knowledge taxonomy; no measured rate of unrevisited wrong first hypotheses; no controlled one-vs-three hypothesis test; no Whyline-prompt test; no is-a-change-needed gate test; no token-surprise slip flag test. Most results use non-reasoning 2023-2024 models.

## 7. What our agent should take

Status: [E] established (two or more independent sources), [S] single-source, [C] contested. Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Ids are evidence ids; K-ids are in claims.jsonl.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Treat a failure as the end of a chain. On a wrong or failed result, look for the first wrong belief, not only the last wrong step. Log per step the belief about the cause and the observation that tests it. | G2 | [E] for the failure pattern in agents (wrong fix after right place); the human chain model itself is [S] | K12, K01; a05, a33, d08, a34, d16, d18 |
| A2 | Never accept self-review as verification. A check must use something outside the reasoning: a test, a run, a lookup, a computed value. | G3 (confirms G2, G10, section 4b) | [E] | K05; a26, c04, c06, a25, d03, d04 |
| A3 | In code debugging, run the code and read real output before repair. Do not imagine execution. A repair step must cite the failing output or a real variable value. | G2, O (run, observe) | [E] | K08, K09; a29, c13, c12, d05, d22, c26 |
| A4 | Locate first, then repair. Take the location from a check (failing test, trace, diff), not from a vote of the same model. | G2, G3 | [E] | K06; c06, c07, a24, d11 |
| A5 | Scale effort to defect type. Surface slips: one pass with a tool check. Logic and multi-part bugs: more probes and verification. Consistent with G12. | G12, G2 | [E] for the direction | K10; a27, c10, c24, a33, d22 |
| A6 | Judge a claimed fix by a check the agent did not write alone; mark self-made test results as weaker. A reproduction test is itself a hypothesis: confirm it fails before and passes after. | G3 | [E] | K15, K21; c22, c23, c20, d07, d14 |
| A7 | A failed edit is a trigger: revert or re-read before the next edit; add a cheap gate (syntax, parse, test run). | G2, O | [E] for the tool-feedback principle; the 15.0 to 18.0 figure is [S] | K24; d09, c17 |
| A8 | Put verification effort after the edit too. Finding the right place is not the main failure for strong models; the wrong patch at the right place is. | G3 | [E] for the pattern; the exact shares are [S] | K12, K36; a33, d08, d15, d16, d18 |
| A9 | Do not rely on instructions to "be aware of bias" or "be careful". Use structural steps. (Already in section 4b; this subfield adds code-specific evidence.) | 4b | [E] | K28; b21, b22, b19, b20, a34 |

### Test first (not yet established; each is a row in UNKNOWNS.md)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Three competing root-cause hypotheses before the first edit, each with a cheap probe. Caution: a full competing-hypotheses matrix (ACH) showed no gain in section 4b, so this must be a cheap, probe-based version. | G2 | [S] | K03, K02; a07, a15, a22, d05, a32, d25 |
| T2 | Whyline step: state the why / why-didn't question after a failure, name the unchecked assumption, probe it. | G3 | [S] | K04; a16, a17, a18 |
| T3 | Same-hypothesis detector: if the second patch has the same diagnosis as the first, force a new hypothesis. A bare "must change" instruction adds only +0.8 to +1.9. | G2 | [S] | K12, K30, K38; a34, b17, d18, d23 |
| T4 | Is-a-change-needed gate by tool (run the failing test first; stop if it passes). | G2 stop rule | [S] | K13, K22; a35, d13, d09 |
| T5 | "Wait"-style recheck of own diagnosis, for non-reasoning models only. Conflicts with G1 unless triggered by a signal. | G3 | [S] | K19; d01, d02 |
| T6 | Rollback to the earliest critical step, triggered by a test or diff, not by a log reader. | G3, memory | [S] | K14, K23, K39; a36, d11, d12, d19, d20 |
| T7 | Reproduce first, then fix, vs open choice. | G3, O | [C] | K16, K21; c19, c27, d06, d14, d15 |
| T8 | Real variable state for logic bugs, not tracebacks only. | O (observe) | [E] in code benchmarks; new at equal tokens | K09, K11, K41; c12, a28, d21 |
| T9 | Log failures in chain form (root belief, later errors) as a memory item for the next attempt. | memory | [S] | K01, K25, K14; a36 |
| T10 | Freeze the last state that passed the failing test; a later change needs a stated reason and a passing test. | G3 | [S] | K37; d17 |
| T11 | Choose the repair signal: failing message vs bare pass/fail vs variable state. | G2, O | [S] | K41; d23, d21, d22 |
| T12 | Restate the task from the original text before editing, and check names and cues against behaviour (cue discipline). | G2 | [S] for debugging; [E] for the susceptibility | K27, K35; b10, b12, b27, b24 |
| T13 | Require a stated causal story (why this cause produced this failure) before accepting a patch; a vanished symptom is not a fix. | G3 | [S] | K42; d24, d07 |
| T14 | Probe a root-cause hypothesis by one cheap intervention instead of reading the log. | G2 | [S] | K40; d20, d05 |
| T15 | Token-level surprise on own plan or patch as a cheap slip flag. | G2, O | [S] | K34; b25, b26 |
| T16 | Cap pure-thinking turns without a tool call (for reasoning models). | G11, G2 | [S] | K22; d13 |

## 8. Concrete tests on our bench

For every test: both arms get equal total tokens (thinking, tool output, retries). Report accuracy per 1,000 tokens as well as raw accuracy. At least 3 seeds. The metric uses a held-out stricter test, not the agent's own tests (K15). Setup cost is counted (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 chain audit (T9, A1) | 50-100 failing coding or reasoning runs from our bench | No arms. Code each failure: first wrong belief, revisited or not, number of dependent steps; also whether the right place was edited | Share with an unrevisited wrong first hypothesis; mean chain length; share with right-place wrong-patch | A large share (above 40%) unrevisited; right-place wrong-patch above 50% for strong models (d16) |
| B2 signal ablation (A3, T11) | Bugs with a runnable test, mixed classes | (a) model-only diagnosis; (b) pass/fail only; (c) failing message; (d) real variable state; (e) human hint as ceiling | Fixed rate on held-out tests | (d) >= (c) > (b) > (a); (a) near or below no repair; gap to (e) shows headroom |
| B3 hypotheses (T1) | Logic-class bugs only, 80 items | One hypothesis plus checks vs three hypotheses each probed, then edit | Fixed rate; first-listed cause correct; tokens | A few points gain on logic bugs; may lose on surface slips |
| B4 Whyline prompt (T2) | Logic bugs after a failed first attempt | Free retry vs retry with "why did this fail, which assumption, probe it" | Fixed at second attempt; repeated-diagnosis rate | Lower repeat rate; small gain |
| B5 same-hypothesis rule (T3) | Items where the first patch fails | Plain retry vs "must change" instruction vs forced new hypothesis when the diagnosis repeats | Fixed after retry; diagnosis-repeat rate; near-identical patch rate | Forced new hypothesis beats "must change" (+1-2 only); gain where silent semantic failure is common |
| B6 action gate (T4) | 50% already-fixed, 50% broken | None vs prompt-only guard vs tool gate (run test first) | False edits on fixed items; fix rate on broken items | Gate cuts false edits sharply; guard alone does not (a34) |
| B7 Wait recheck (T5) | Own-diagnosis review on logic bugs; one non-reasoning and one reasoning model | No recheck vs Wait vs separate-call review | Correct-to-wrong flips; net accuracy | Helps the non-reasoning model; none for the reasoning model |
| B8 rollback (T6) | Failed long runs | Continue vs rollback at a test-triggered point vs at an LLM-log-chosen point | Fixed rate at equal tokens | Test-triggered > continue > LLM-log-chosen |
| B9 reproduce-first (T7) | Bug reports with ambiguous cause | Open choice vs reproduce-first, same model and interface | Fixed rate; share of repro tests valid on the true fix | Unknown; gain only when the report is ambiguous |
| B10 traceback by class (T8) | Mixed bug classes | Traceback vs withheld vs variable trace | Fixed rate per class | Traceback helps syntax and reference; flat or worse on logic; variable trace best on logic |
| B11 freeze (T10) | Long runs where a mid-run patch passes the failing test | Free editing vs freeze with reason-and-test rule | Lost-fix rate; final fixed rate | Fewer lost fixes; gain a few points |
| B12 cue discipline (T12) | Debug tasks with an added misleading cue (wrong function name, irrelevant line, earlier wrong patch) | No step vs "avoid bias" instruction vs restate-spec-and-check step | Fix rate under cue; copy rate of the cue | Structural step beats instruction; instruction near zero |
| B13 causal story (T13) | Tasks where a symptom-only patch passes the visible test | No requirement vs stated causal story checked by a held-out test | Rate of symptom-only patches | Lower symptom-only rate |
| B14 intervention probe (T14) | Failed runs with a candidate root cause | Read the log vs one cheap intervention vs plain resampling | Share of hypotheses correctly confirmed or refuted; fixed rate | Probe beats log reading; check it also beats resampling |
| B15 surprise flag (T15) | Agent patches with known seeded slips | Flag from token surprise vs none vs random flag | Recall and false-alarm rate of the flag; fixed rate | Recall above random with false alarms low enough to pay for the extra read |
| B16 thinking cap (T16) | Reasoning model on repair tasks | Uncapped vs cap on thinking turns without a tool call | Fixed rate; tokens | Cap helps reasoning models, not others |

## 9. What does not transfer, and why

- **Skill-level slips.** Human attention lapses, interruption and habit intrusion have no direct counterpart in a model. LLM equivalents (copy errors, dropped context, copying a framing line) exist in part (b10) but were not tied to the skill category. Do not add skill-slip guards on this basis.
- **The 22/28/27 class shares.** One sample of 7 novices, one tool (Alice), one analyst. They say nothing about our agent's mix. Measure our own (B1).
- **Whyline as an interface.** The human gain came from a visual tool showing runtime events. A prompt is not that tool. It may carry only the "name the assumption" part (K04).
- **Think-aloud timing.** 20 minutes lost on a hidden bug and 46.4% of time spent debugging are human time, not tokens.
- **Training-based gains.** NExT (+26.1) and fine-tuning on 5,306 error-correction traces change weights. Our agent is scaffold-only.
- **Multi-agent logs.** MAST, Who&When, AgentRx and DoVer cover multi-agent or tool-use systems (tau-bench, web, math). The step-finding results may not match single-agent coding logs.
- **Injected errors.** DebugBench and Self-Correction Bench inject bugs. Real model-made bugs are structural and multi-line (c24).
- **SWE-bench absolute numbers.** Contamination and weak tests (c22, c23). Use directions, not levels.
- **The human 90% wrong-first-guess figure.** Cited, not measured. Do not assume the same rate for an LLM.
- **Prompt-only guards.** The one direct test of a pre-edit prompt guard showed no change (a34). Do not rely on wording alone.
- **Human sleep loss and anchoring on ratings.** Sleep loss (b28) has no agent analogue. The anchoring study (b08) rated understandability, not debugging. Neither is a design input.
- **Oracle triggers.** The +4.6 freeze result used a reference patch (d17). Our agent has no reference, so only the consensus-type result (+3.0, p=0.08) is relevant, and it is not significant.
- **Human debiasing training.** No technique had strong evidence (b06). Do not borrow human debiasing tricks as prompts.

## 10. Open questions

1. What share of failed agent runs have a wrong first hypothesis that is never revisited? Nobody has coded this in the Ko and Myers form. Nearest data: strong models mostly edit the right place (d16) and about 65% of failures are flawed reasoning with strategy fixation (d18). Weak models fail upstream.
2. Do three hypotheses before the first edit beat one plus checks at equal tokens, on logic bugs only? Only CogniGent (localisation) uses multiple hypotheses, with no isolated ablation read.
3. Which signal carries the gain: pass/fail, failing message or real variable state? Partly closed: message beats pass/fail by about 13 points (abstract only), variable state gave the largest ablation drop (confounded). No controlled three-arm test, and no comparison with the human 52.6%.
4. Can a test- or diff-triggered rollback beat continuing at equal tokens? Partly closed: constraint checks help (not code), consensus trigger not significant.
5. Does naming the unchecked assumption help an LLM? Nothing found.
6. Are there independent replications of Ko and Myers 2005, or of Reason's split in software? Reason, Gilmore, Vessey unopened.
7. How much of the action bias does a tool gate remove compared with a prompt guard? Nothing found on the gate.
8. Do current long-thinking models self-correct code errors at equal tokens, or does the 2023-2024 negative result still hold? Tsui tests injected errors only.
9. Reproduction-first vs open choice with model and interface held fixed.
10. Does the skill/rule/knowledge split say anything about LLM errors at all?
11. Does the Wait effect hold on code, and does it earn more than it costs in tokens?
12. Is there a single "decisive step" in an agent failure? DoVer suggests several different fixes can each work.
13. Does token-level surprise work as a slip flag, and what is its false-alarm rate?
14. Does the Zhou finding (reversals halved) mean LLMs help recovery, or is it sample difference?
15. Do the atoms of confusion that mislead novices also mislead models, and which?

## 11. Sources

[V] = opened (full text read in this series). [M] = snippet or abstract only, or cited secondhand.

**Human studies and theory**
- [V] Ko and Myers (2005) A framework and methodology for studying the causes of software errors in programming systems. https://faculty.washington.edu/ajko/papers/Ko2004SoftwareErrorsFramework.pdf
- [V] Ko and Myers (2003) Development and evaluation of a model of programming errors. https://faculty.washington.edu/ajko/papers/Ko2003ModelOfErrors.pdf
- [V] Ko and Myers (2004) Designing the Whyline. https://faculty.washington.edu/ajko/papers/Ko2004Whyline.pdf
- [V] Ko and Myers (2008) Debugging reinvented. https://faculty.washington.edu/ajko/papers/Ko2008JavaWhyline.pdf
- [V] Ko and Myers (2008) Source-level debugging with the Whyline. https://faculty.washington.edu/ajko/papers/Ko2008SourceLevelDebugging.pdf
- [V] Ko, Myers and Aung (2004) Six learning barriers in end-user programming systems. https://faculty.washington.edu/ajko/papers/Ko2004LearningBarriers.pdf
- [M] Reason (1990) Human Error. https://doi.org/10.1017/CBO9781139062367
- [M] Perkins and Martin (1986) Fragile knowledge and neglected strategies in novice programmers (via Ko and Myers; no URL)
- [M] Gilmore (1991) and Vessey (1985) on debugging hypotheses (via Ko and Myers; no URL)
- [V] Parnin and Orso (2011) Are automated debugging techniques actually helping programmers? https://doi.org/10.1145/2001420.2001445
- [M] Gopstein et al. (2017) Understanding misunderstandings in source code. https://pure.psu.edu/en/publications/understanding-misunderstandings-in-source-code/
- [V] Langhout and Aniche (2021) Atoms of confusion in Java. https://arxiv.org/abs/2103.05424
- [V] Mohanani, Salman, Turhan, Rodriguez, Ralph (2020) Cognitive biases in software engineering: a systematic mapping study. https://arxiv.org/abs/1707.03869
- [V] Wyrich, Merz, Graziotin (2022) Anchoring code understandability evaluations through task descriptions. https://arxiv.org/abs/2203.13705
- [V] Fucci, Scanniello, Romano, Juristo (2018/2020) Need for sleep. https://arxiv.org/abs/1805.02544
- [M] Chattopadhyay et al. (2020) A tale from the trenches: cognitive biases and software development (ICSE; cited via Zhou, no URL)

**Self-correction and repair (LLM)**
- [V] Olausson et al. (2024) Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297
- [V] Gou et al. (2023) CRITIC. https://arxiv.org/abs/2305.11738
- [V] Tsui et al. (2025) Self-correction bench. https://arxiv.org/abs/2507.02778
- [V] Chen et al. (2024) Teaching large language models to self-debug. https://arxiv.org/abs/2304.05128
- [V] Zhong et al. (2024) Debug like a human (LDB). https://arxiv.org/abs/2402.16906
- [V] Ni et al. (2024) NExT. https://arxiv.org/abs/2404.14662
- [V] Kang et al. (2023) Explainable automated debugging via LLM-driven scientific debugging (AutoSD). https://arxiv.org/abs/2304.02195
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Huang et al. (2026) TraceCoder. https://arxiv.org/abs/2602.06875
- [V] Arimbur (2026) How many tries does it take? https://arxiv.org/abs/2604.10508
- [M] Kim (2026) Inducing code change in LLM self-debugging, AI 7(10):392. https://doi.org/10.3390/ai7100392 (abstract only; full page 403)
- [V] Chen et al. (2024) REval. https://arxiv.org/abs/2403.16437

**Benchmarks, bug types and agent failure analysis**
- [V] Tian et al. (2024) DebugBench. https://arxiv.org/abs/2401.04621
- [V] Jimenez et al. (2024) SWE-bench. https://arxiv.org/abs/2310.06770
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/abs/2405.15793
- [V] Xia et al. (2024) Agentless. https://arxiv.org/abs/2407.01489
- [V] Zhang et al. (2024) AutoCodeRover. https://arxiv.org/abs/2404.05427
- [V] Meng et al. (2025) LLM-based agents for automated bug fixing: how far are we? https://arxiv.org/abs/2411.10213
- [V] Mundler et al. (2024) SWT-Bench. https://arxiv.org/abs/2406.12952
- [V] Wang, Pradel, Liu (2026) Are solved issues in SWE-bench really solved correctly? https://arxiv.org/abs/2503.15223
- [V] Aleithan et al. (2024) SWE-Bench+. https://arxiv.org/abs/2410.06992
- [V] Wang et al. (2025) Towards understanding the characteristics of code generation errors. https://arxiv.org/abs/2406.08731
- [V] Tambon et al. (2024) Bugs in LLM generated code. https://arxiv.org/abs/2403.08937
- [V] Majgaonkar et al. (2025) Understanding code agent behaviour. https://arxiv.org/abs/2511.00197
- [V] Mehta (2026) Confident and wrong: silent semantic failures in coding agents. https://arxiv.org/abs/2603.25764
- [V] Qi et al. (2026) TrajDebug. https://arxiv.org/abs/2608.06346
- [V] Kim et al. (2026) Coherence Collapse (TrajEval). https://arxiv.org/abs/2603.24631
- [V] Liu et al. (2025) An empirical study on failures in automated issue solving. https://arxiv.org/abs/2509.13941
- [V] Cemri et al. (2025) Why do multi-agent LLM systems fail? (MAST). https://arxiv.org/abs/2503.13657
- [V] Zhang et al. (2025) Which agent causes task failures and when? (Who&When). https://arxiv.org/abs/2505.00212
- [V] Barke et al. (2026) AgentRx. https://arxiv.org/abs/2602.02475
- [V] Ma et al. (2026) DoVer. https://arxiv.org/abs/2512.06749 (abstract and introduction values; per-dataset table not re-read)
- [V] Antoniades et al. (2025) SWE-Search. https://arxiv.org/abs/2410.20285
- [V] Cuadron et al. (2025) The danger of overthinking. https://arxiv.org/abs/2502.08235
- [V] Samir and Rahman (2026) CogniGent. https://arxiv.org/abs/2601.12522 (abstract and introduction; ablation table not read)

**Biases and slips in LLMs**
- [V] Jones and Steinhardt (2022) Capturing failures of large language models via human cognitive biases. https://arxiv.org/abs/2202.12299
- [V] Zhou, Saghi, Sabouri et al. (2026) Cognitive biases in LLM-assisted software development. https://arxiv.org/abs/2601.08045
- [V] Sovrano et al. (2025) Is general-purpose AI reasoning sensitive to data-induced cognitive biases? https://arxiv.org/abs/2508.11278
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811
- [V] Itzhak et al. (2023) Instructed to bias. https://arxiv.org/abs/2308.00225
- [V] Shi et al. (2023) Large language models can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093
- [V] Abdelsalam, Toneva, Apel (2025) How do humans and LLMs process confusing code? https://arxiv.org/abs/2508.18547

Notes on verification: the critique re-opened the Ko and Myers, Olausson, Huang, Tyen, DebugBench, Chen, Mehta, TrajDebug, Majgaonkar, Langhout, Jones, Zhou and Fucci numbers in full text. Seen at snippet or abstract level only: a32 and d25 ablations, the 60-90% action-bias range, b22 and b23 figures, b30, c14, c16, c21, c25, c26 and c27 detail numbers, d20 per-dataset values, d23. Corrections applied here: Chen UT-only is 80.6 (GPT-4) and 69.4 (Codex); the atoms paper lists "remove indentation atom" among the 7 significant atoms, so per-atom odds ratios are not used; the AgentRx baseline was re-run by its authors.
