# Debugging as scientific method: deep document

*Subfield E09.04. Evidence ids (a01 to d16) are lines in evidence_a-d.jsonl. Claim ids (K01 to K30) are in claims.jsonl. Corrections from critique.md are applied: oracle-label numbers use a21 (not b21 or c14); the Wason numbers (a03) and Tyen "52.87" (c15) are not quoted; the classic papers (Gould, Vessey, Gugerty and Olson, Katz and Anderson, Parnin and Orso, Zeller 2009) were not opened and carry no numbers here.*

## 1. What it is

Scientific debugging treats a bug as a puzzle in cause and effect. You do not poke at code. You run a loop:

1. **Hypothesis**: a guess about what causes the failure.
2. **Prediction**: what you will see if the guess is true. Written before the run.
3. **Experiment**: a run that can show it (a print, a breakpoint, a reduced input, a new test).
4. **Observation**: what really happened.
5. **Conclusion**: confirmed, refuted, or refine.

Zeller (2009, *Why Programs Fail*) states this as a method and asks the debugger to keep a log of the five items. A refuted hypothesis is still progress. A confirmed one narrows the cause. [a01, M]

The key point for our agent is step 2 and the order of 2, 3, 4. The prediction is fixed before the observation, so the observation can surprise you. Without it, any output can be read as support.

Our schema has a close fit. S4 TEST and S5 REVISE already say "revise only from real output" (G2). This subfield asks a narrower question: should the agent write down what it expects before each probe, and should code compare the expectation with the result? That is the "predict-then-observe check".

What the evidence says in one paragraph. The method is prescriptive. No controlled trial shows that humans who follow it debug faster (K23). Where it has been built into an LLM loop (AutoSD), the repair rate does not rise reliably (K05). What does help is real execution output (K06, K14), a debugger that the model is forced to use (K26), and outside feedback (K11). The prediction step on its own has never been isolated (K24, gap 1). The model's pre-run predictions are often wrong (K16, K25), which is the main risk.

## 2. History and theories in depth

Only sources marked opened carry numbers. The older papers were not opened this session (M).

**Reasoning about hypotheses (psychology of science).**
- Wason (1960), the 2-4-6 task. People test a rule mostly with cases that fit their guess and rarely try to break it. This is the root of weak experiments. [a03, M, no numbers quoted]
- Klayman and Ha (1987). Positive tests are not irrational. They are informative when the true rule is narrower than the guess. They fail when the guess is too broad, which is common in debugging. [a04, M] This is why K20 is marked contested: "always try to disconfirm" is not a clean rule.
- Klahr and Dunbar (1988). Scientific reasoning is search in two linked spaces, a hypothesis space and an experiment space. In the BigTrak task, people split into theorists and experimenters. [a05, M] This gives a clean model for an agent: keep the two spaces apart and let code manage the experiment space.

**Early debugging psychology (all M).**
- Gould (1975): bugs that need a value traced back took longer than wrong-statement bugs. [a06]
- Vessey (1985): experts keep a system-level view and change strategy when one fails; novices go depth first and stay stuck. [a07]
- Gugerty and Olson (1986): experts build better hypotheses from comprehension, not trial and error; novices add new bugs. [a08] (A sibling subfield covers this.)
- Katz and Anderson (1987): own code is debugged backward from the symptom, other people's code forward by comprehension. [a09]
- Parnin and Orso (2011): ranked fault-localisation lists were not followed in order and helped on an easy bug only. [a10]
None of these were verified (critique, gap 8). Do not quote their numbers.

**Tools that automate one step.**
- Delta debugging (Zeller and Hildebrandt 2002) automates the experiment step. It runs reduced inputs and shrinks to a minimal failing case. It has no model of the cause. [a11, M]
- The Whyline (Ko and Myers 2004, 2008). The programmer asks "why did" or "why didn't" about an output. The tool answers from a recorded trace. Ko and Myers 2004 was read (a13, a14, d15); the 2008 paper was not (a12, M).

**Observation of real practice.**
- Siegmund et al., as cited by Kang et al.: developers without training roughly follow hypothesis then verification. [a02, M, secondary]
- Alaboudi and LaToza (2021): 15 live-streamed sessions show mostly manual run-and-observe, with rare state inspection. [b05, b06, b07]
The two do not agree on how formal real practice is. That is K04, contested.

**LLM era (2023 to 2026).** Self-Debug (2023) and Reflexion (2023) add execution feedback and explanation. AutoSD (2023) is the first full build of Zeller's five-step loop into an LLM with a real debugger. LDB (2024) verifies runtime values block by block. ChatDBG (2025) lets a model drive a real debugger. debug-gym (2025) and Debug2Fix (2026) ask whether debugger access helps agents. DoVer (2025) turns blame hypotheses into interventions. CRUXEval and REval measure the predict half directly.

## 3. Core findings with exact numbers

Status key: established = two or more independent sources; single = one source or one group; contested = sources conflict. Model names are the ones the papers used. Many are old models.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Developers hold few, mostly wrong hypotheses early | Control group, 20 developers, 60 sessions in all, 3 tasks. About 2 hypotheses per defect. Correct: 3 of 27 (11%) at stage 1, 9 of 35 (25%) at stage 2, 15 of 38 (39%) at stage 3 | Alaboudi and LaToza 2020 [b01] | single (K01) |
| A correct early hypothesis goes with fixing the bug | Correct at stage 2 gives about 5x odds of a fix, p=0.01, 60 sessions. Correlational | [b02] | single (K02) |
| Supplying candidate hypotheses helped; supplying fault locations did not | Hypotheses OR 6.24, p=0.03. Fault locations OR 1.4, p=0.64 (fix rate p=0.67). Experience OR 1.14, p=0.04 | [b03, b04] | single (K03) |
| Real practice is mostly run-and-observe | 15 sessions, 11 professionals, 30 hours. 2137 debugging and 1407 programming activities. Debugging every 8 min; 13 to 95% of session time (mean 48%). State inspected twice per episode, 8% of time, 53 s each. Logs 70%, breakpoints 30%. Runs 84% manual, 16% automated. Edit after inspection 65% | Alaboudi and LaToza 2021 [b05-b07] | contested vs self-report (K04) |
| Long episodes differ from short | 80% of episodes short. Short: edit and test 88% of time. Long: browsing 1.3% to 18%. Outside resources in 21% of episodes | [b07] | single |
| 50% of errors in formative human studies came from false hypotheses | 68% of questions were "why didn't"; 85% about one object | Ko and Myers 2004 [a13, d15] | single (K22) |
| Whyline sped up humans in a tiny test | 4 users with vs 4 without, 90 min. Tasks done 3.20 (SD .457) vs 2.25 (SD .500), t(7)=3.0, p<.02 (+40%). Debug time over six matched scenarios F(1,5)=12.64, p<.02, mean factor 7.8 | [a14, d15] | single (K22); "7.8x" is soft |
| No controlled trial that following Zeller's protocol speeds humans up | None found in this evidence | [a01, a02, b01] | single (K23) |
| AutoSD: no clear accuracy win over a plain LLM | Defects4J v1.2 correct: plain 87, AutoSD 76. v2.0: 110 vs 113. ARHE (self-built): plausible 179 vs 189, correct 177 vs 187. Recoder 24/11, InCoder 41/28. 10 patches per bug, max 3 iterations | Kang et al. 2023 [a15, b08, c01] | contested (K05) |
| Real execution is what makes it work | Plausible-patch runs 73% (real debugger) vs 63% (model-simulated). DONE flag: +12.4 points as a signal with real output, -11 points with simulated | [a16, b09, c03] | single (K06) |
| DONE flag tracks correctness a little | Among plausible patches 89% correct with DONE vs 82% without. 100 hand-labelled patches per group | [b10, c02] | single (K07) |
| Many "refuted" hypotheses are broken experiments | 25 cases with all hypotheses rejected: 13 breakpoints never hit, 2 invalid expressions, 2 multi-print errors | [c04] | single; second count in DoVer (K08) |
| DoVer: most intervention trials inconclusive | Trials 72/99/63. Validated 15.3/16.2/34.9%, refuted 13.9/21.2/23.8%, partial 4.2/5.1/12.7%, inconclusive 66.7/57.6/28.6% | Ma et al. [d03] | single (K08) |
| Blame from logs alone is unreliable | 29 GAIA cases; 14 with uncertain truth. Step accuracy there GPT-4o 24%, GPT-5 7%. 15 clear cases: GPT-4o 44%, GPT-5 53% | [d04] | single (K28) |
| Explanation helps people judge patches, mildly | N=20 (14 students, 6 professionals), 12 bugs. Accuracy higher with the trace in 7 of 12 cases (5 of 6 real bugs), lower in 2. No significant time difference. 70% wanted explanations | [a17, b12, b13, c05] | single (K09) |
| Own-feedback self-repair is weak | GPT-4 repair 33.30% own feedback vs 52.60% human feedback (1.58x). Intro 42.64 vs 62.21, interview 19.33 vs 45.67, competition 3.67 vs 14.67. 16 people, 40 programs, 25 repairs each | Olausson et al. 2024 [a20, b18, c13] | single (K10) |
| Self-repair about equals equal-budget sampling | 0.97x of pass@22; 1.05x of pass@20 | [b17] | single (K10) |
| Intrinsic self-correction does not help | GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GSM8K 75.9 to 75.1 to 74.7; HotpotQA 26.0 to 25.0. GPT-4 GSM8K 95.5 to 91.5 to 89.0; CSQA 82.0 to 79.5; HotpotQA 49.0 to 43.0 | Huang et al. 2024 [a21, b20] | established (K11) |
| With oracle labels it helps (not realistic) | GPT-3.5 GSM8K 84.3, CSQA 89.7, HotpotQA 29.0. GPT-4 GSM8K 97.5, CSQA 85.5, HotpotQA 59.0 | [a21] (not b21) | established |
| Debugger helps strong models, hurts weak | SWE-bench-Lite, rewrite / debug / debug(5): Claude 3.7 37.2/48.4/52.1; o1-preview 10.7/30.2/30.8; o3-mini 8.5/22.1/19.8; GPT-4o 19.1/17.2/23.6; GPT-4o-mini 4.0/3.5/6.2; Llama-3.3-70B 2.4/4.0/4.8 | debug-gym [a22, c06, d06] | contested (K12) |
| Mini-nightmare (10 hand-made bugs) | o1-preview 100/100/100; o3-mini 100/96.7/100; Claude 3.7 93.3/96.7/93.3; GPT-4o 40.0/40.0/53.3; GPT-4o-mini 13.3/6.7/16.7 | [d07] | single |
| Frontier models under-use an optional debugger | Sonnet 4.5 called the debug subagent in 8% of SWE-Bench-Live instances. Blocking edits until one debug call: about 99% call rate. GitBug-Java GPT-5 60.2 to 73.1 (+21.8% rel.); Sonnet +13%; Haiku +16%. Raw debug tools only: flat for GPT-5 and Haiku, Sonnet 64.5 (-14.8%) | Debug2Fix 2026 [d08, d09] | single (K26) |
| Interactive debugger dialogue | ChatDBG, GPT-4, Python, 10 runs: "why?" 57%; targeted question 67%; plus one follow-up 85%. C/C++: 36% root cause, 55% more proximate. About $0.12 and 25 s per query | [c09, c10] | single (K13) |
| Real runtime values beat model-simulated ones | HumanEval GPT-3.5 73.8: SD 81.1/80.5, LDB 82.9. StarCoder 39.0: SD -0.6/0.0, LDB 39.6. GPT-4 87.2 to 89.6 (+2.4); Reflexion seed 91.5 to 95.1 (+3.6). Up to +9.8 over baseline. SD stalls after 2 to 3 rounds | LDB [a19, b14-b16, c11, d11] | established (K14) |
| Training on trace-reading rationales | PaLM 2-L +26.1 on Mbpp-R, +14.3 on HumanEvalFix+. Zero-shot trace CoT 7.8 points worse on average (DeepSeek Coder 57.3 to 30.5; StarCoder 29.3 to 16.5); rationale correctness about 30% | NExT [a23, c16] | established (K14) |
| Explanation alone: small gain | Spider +2 to 3 (81.3 to 84.1 Codex), +9 on hardest; unit tests up to +12; MBPP Codex 61.4 to 70.8, GPT-4 72.8 to 80.6 | Self-Debug [a18, b22, b23, c12, d12] | single (K15) |
| Predicting program behaviour is weak | CRUXEval GPT-4 no CoT 67% input / 63% output; CoT about 75% / 81%; best open 47% / 44%; Code Llama 34B 50% / 46%. REval, 15 models: mean accuracy 44.4%, consistency 10.3; GPT-4-Turbo 75.0% and 42.5; output prediction above 50% for all; only 8 of 15 above 10% on execution path | [a24, a25, b26, b27, c17-c19, d10] | established (K16, K25) |
| Prediction can serve as a filter, not a verdict | Pairwise ML solution preference 61.5% (DeepSeek-V3.2-Thinking), 58.8% (GPT-5.1), chance 50%. Thinking 61.3% vs direct 55.9%. Listwise top-1 61.3% to 31.1%. ForeAgent about 6x faster convergence | Zheng et al. 2026 [d14] | single (K27) |
| Logic and multi-bug errors are hardest; runtime feedback does not help logic bugs | 4,253 bugs, 18 types. GPT-4-0613 75.0%, GPT-3.5-0613 62.1% overall. Per-type effects only in a figure | DebugBench [b24, c29, d16] | single (K17, K29) |
| Interface design moves results | SWE-bench-Lite: SWE-agent 18.0% vs shell 11.0% vs RAG 2.67%. Lint on 18.0 vs off 15.0 vs no edit tool 10.3. Summarised search 18.0 vs none 15.7 vs iterative 12.0 | SWE-agent [b25, c28] | established (K18) |
| Reflection needs reliable tests | HumanEval Python 0.80 to 0.91; MBPP Python 0.80 to 0.77; Rust 0.60 to 0.68 and 0.71 to 0.75. False-positive rate 0.01 vs 0.16. No written reflection: no gain in the Rust ablation | Reflexion [b29, b30] | single (K19) |
| Closed observe loop cuts hallucination | HotpotQA failures: CoT 56% hallucination, ReAct 0%. ACRE 28.0 direct, 32.0 LLM as interpreter, 45.0 and 59.0 with exact interpreter. Majority vote 29.0 | ReAct, Qiu et al. [c25, c22] | established (K21) |
| Hypothesis loop equals plain retry in test generation | gpt-4o-mini, Python. One shot: coverage ~55%, mutation score ~60%. Iterative, Scientific 0-shot and 1-shot: coverage ~80%, mutation score ~80%, success near 60%. Scientific costs more tokens. Over 15% of mutants flagged equivalent; many were killable | Straubinger et al. 2025 [d01, d02] | single (K05, K24) |
| LLMs are weak at experiment choice | BoxingGym: all systems struggle; prior information often made results worse after 10 experiments. Bandit study: only one configuration (GPT-4, CoT, externally summarised history) explored well. Wason: models and people both poor; both better on realistic rules | [c20, c21, c23, c24] | contested (K20) |
| Calibration of model confidence in code is poor | ECE 0.09 to 0.73 across tasks and GPT-3.5, Codex, CodeGen2-16B | Spiess et al. 2024 [d13] | single (K07) |

## 4. Mechanisms and models

Each mechanism is written so it can be built. "Code" means the harness; "model" means a filled slot.

### 4.1 The five-line experiment record (AutoSD form)

Per probe, the model fills five fields, one at a time, in this order:
1. `hypothesis`: one cause, stated so a run could refute it.
2. `prediction`: the exact value, line hit, or exception expected if the hypothesis is true. Also what is expected if it is false.
3. `experiment`: one concrete probe (a debugger command, a print, a test). Code, not the model, runs it.
4. `observation`: pasted by code from the real run. The model never writes this field. [K06]
5. `conclusion`: confirmed, refuted, or inconclusive. The model proposes; code checks the validity gate in 4.2 first.

In AutoSD the loop runs up to 3 iterations. A DONE token is emitted only when an experiment confirmed the hypothesis. Then the patch is written. [a15, a16]

### 4.2 The experiment validity gate

Failure analysis shows 13 of 25 all-rejected cases were broken probes (breakpoint never hit). [c04] DoVer shows 57.6 to 66.7% of intervention trials were inconclusive on the hard sets because the intervention was not carried out. [d03] So code must check, before a refutation is accepted:
- Did the probe line or command actually execute? (Coverage, hit counter, non-empty output.)
- Did the probe parse and run without error?
- Did the observation have the type and shape the prediction used?
If any check fails, the conclusion is forced to `inconclusive` and the hypothesis stays alive. Straubinger's equivalent-mutant case is the same error in another form: abandoned hypotheses were often failed searches. [d02]

### 4.3 The mismatch signal

Code compares prediction and observation.
- Match: the hypothesis gains support. This is weak evidence alone, because the same match may follow from other causes.
- Mismatch with a valid experiment: the prediction was wrong, so either the hypothesis or the model of the program is wrong. This is the useful surprise. It is the trigger the schema wants for doubt (G1, S5).
- Mismatch with an invalid experiment: no information. Go to 4.2.
The comparison can be a string or value match when the prediction is a literal, and a short model-judged match otherwise. Prefer literal predictions.

### 4.4 Why prediction is treated as a filter, not a verdict

CRUXEval, REval and ForeAgent put pre-run prediction accuracy at about 44 to 81% for code and 61.5% for ML outcomes (chance 50%). [a25, d10, d14] So the prediction is a hypothesis about the program, not a fact about it. Use it for two jobs only:
1. Rank candidate probes by expected information (run the one whose predicted outcome best separates the hypotheses).
2. Detect surprise after a real run.
Never replace the run with the prediction. [K06, K25, K27] When the model simulates the run itself, gains are zero or negative on weaker models (StarCoder -0.6 / 0.0) and the DONE signal flips sign (-11 points). [d11, c03]

### 4.5 Forced observation gate

Models under-use an optional debugger (Sonnet 4.5: 8% of instances). Blocking edits until one debug call was made lifted the call rate to about 99% and raised GPT-5 pass rate from 60.2 to 73.1 on GitBug-Java. [d08, d09] Implementation: the patch tool returns an error until the log holds one executed probe whose observation is non-empty. debug-gym's variant (pdb unlocked after 5 failed rewrites) gave the best result for Claude 3.7 (52.1) and GPT-4o (23.6). [d06] The two designs differ: one forces a probe before the first edit, the other opens probes after repeated failure. The second matches G1 (doubt on a signal).

### 4.6 Candidate hypothesis supply

Giving developers candidate hypotheses lifted the fix odds (OR 6.24, p=0.03). Fault locations alone did not (OR 1.4). [b03] Implementation for an agent: a separate call, in a fresh context, lists 3 to 5 distinct causes, each with a different predicted symptom. Code picks the probe that separates them. Not tested with LLM-supplied candidates (gap 6).

### 4.7 Why-not questions (Whyline)

68% of human questions were "why didn't", and half of all errors came from false hypotheses. [a13] Implementation: the model writes "expected X at line L, got Y; why not X?" and code answers from a trace (the last write to the variable, the branch taken). No LLM replication exists (gap 9). ChatDBG's `slice` command (which code produced this value) is the nearest tool. [c10]

### 4.8 The loop as search in two spaces

Following Klahr and Dunbar, keep a hypothesis list and an experiment list. The model proposes in the first; code keeps both and chooses the next experiment by which one splits the live hypotheses. This also fits Soar-style impasse logic: a failing prediction creates a subgoal "find why it failed".

## 5. What holds up

**Replicated or supported by several sources.**
- External signal beats self-opinion. Huang et al. (intrinsic correction hurts), Olausson et al. (own feedback 33.3% vs human 52.6%), CRITIC (tool checking works), Reflexion (needs reliable tests), Tyen et al. (find errors poorly, fix well when told where; no number quoted). Established (K11).
- Real traces beat model-imagined traces. AutoSD (DONE flips sign), LDB (StarCoder), NExT (zero-shot trace CoT -7.8). Established in direction; effect size depends on model (K14, K25).
- Predicting program behaviour is hard. CRUXEval, REval, CodeMind agree. Established (K16).
- A closed reason-act-observe loop beats pure reasoning on ungrounded claims. ReAct and Qiu et al. (K21).
- Interface design matters. SWE-agent, AutoCodeRover, RepairAgent (K18).

**Single-source or single-group.**
- All human hypothesis numbers (K01 to K03) come from one group, with 20 per condition and correlational analysis. The 5x odds ratio is not causal.
- AutoSD is one author group with a self-built benchmark (ARHE). No independent replication found.
- Debug2Fix (2026) is one group. ChatDBG is one model family.
- Whyline: eight users total.

**Failures and null results.**
- AutoSD loses on Defects4J v1.2 (76 vs 87) and is level on v2.0 (113 vs 110). The repair rate is not the benefit; auditability and the confidence flag are.
- The hypothesis loop matched plain iterative retry at higher cost (Straubinger). [d01]
- Reflexion on MBPP Python went down (0.80 to 0.77) because of false-positive tests. [b29]
- Self-Debug without tests: correct/wrong feedback alone gave no gain on Spider. [d12]
- Explanations can mislead: on ARHE105 wrong answerers accepted the trace without scrutiny. [b13]
- Debugger access hurt GPT-4o (19.1 to 17.2) and GPT-4o-mini (4.0 to 3.5). Raw debug tools hurt Sonnet 4.5 (-14.8%). [d06, d08]
- Debugger gave no clear gain on Aider's 133 simple tasks (GPT-4o 76.4/69.7/72.9). [a22]
- Runtime feedback does not help logic bugs (DebugBench). [d16]
- Prior information made experiment design worse in BoxingGym. [c21]

**Moderators.**
- Model strength: AutoSD rises toward plain LLM as models improve; CodeGen-6B zero-shot failed outright. [b11, a27] Debugger helps o1, o3-mini, Claude 3.7; not GPT-4o. [d06]
- Adoption and tool design: optional use is low; gating raises use. [d09]
- Test quality: Reflexion's gain tracks false-positive rate. [b29]
- Task difficulty: Mini-nightmare near ceiling for reasoning models, so no room to gain. [d07]
- Bug type: logic and multi-bug harder; runtime feedback useless for logic. [d16]
- Human experience: OR 1.14 per year. [b03]

**Interventions that worked.** Real debugger output; forced first probe; one follow-up round (ChatDBG 67 to 85%); block-level verification of real values (LDB); outside diagnosis from a stronger model (Olausson). **That did not.** Self-simulated execution; intrinsic self-review; fault-location hints to humans; raw optional debug tools on weaker models; zero-shot trace CoT.

**Disagreements.** Self-report vs direct observation of how formal human debugging is (K04). Unresolved. Also debug-gym's prose says debugging hurts Llama-3.3-70B while its table shows 2.4 to 4.0 (near noise); treat as unclear.

## 6. Language models

**Baseline behaviour.**
- Left alone, models skip experiments. In debug-gym the authors say agents are "far from capable of using those tools in a meaningful way" and suspect debugging trajectories are scarce in training data. [c08] Optional debugger call rate was 8% (Sonnet 4.5, SWE-Bench-Live) to above 60% (GPT-5). [d09]
- They can follow the five-step form with a strong enough model. With CodeGen-6B zero-shot, AutoSD returned the original code; few-shot it fixed 44. [b11]

**What the structured loop did.**
- AutoSD with ChatGPT-era models: level with plain prompting (113 vs 110 on v2.0; 76 vs 87 on v1.2). DONE flag: 89% vs 82% correct among plausible patches.
- Hypothesis loop in test generation (gpt-4o-mini): same success as plain retry, more tokens. [d01]

**What changed outcomes, and by how much.**
- Real debugger for strong models: Claude 3.7 +11.2 points (37.2 to 48.4), +14.9 with delayed unlock (52.1); o1-preview +19.5 (10.7 to 30.2). [d06]
- Forced debug call: GPT-5 +12.9 points (60.2 to 73.1) on GitBug-Java. [d08]
- Follow-up probe: ChatDBG 67% to 85%. [c09]
- Real traces: LDB +9.1 on GPT-3.5, +2.4 on GPT-4, +3.6 to +6.6 on strong Reflexion seeds. [b15, d11]
- Better feedback author: human feedback 1.58x over GPT-4 own feedback. [b18]
- Interface: SWE-agent shell-only 11.0 to 18.0. [b25]
- Exact interpreter vs LLM as interpreter: ACRE 32.0 to 59.0. [c22]

**What the models are bad at (the predict and design half).**
- Output prediction 63 to 81% (GPT-4), best open under 50%. Intermediate state much worse (REval mean 44.4%). [b26, d10]
- Log-based blame: 24% (GPT-4o) and 7% (GPT-5) when truth is ambiguous. [d04] GPT-5 is not better than GPT-4o on the ambiguous set; the sample is 14 cases.
- Experiment design and exploration: BoxingGym, bandits. [c20, c24]
- Confidence: poorly calibrated for code (ECE 0.09 to 0.73), tested on older models. [d13]
- Wason-style content effects like humans. [c23]

**Not measured.** Nobody has isolated the written pre-run prediction on a modern reasoning model at equal tokens (gap 1). No LLM study varies confirm vs disconfirm tests (gap 5). Most numbers use models from 2022 to 2024, except debug-gym (o1, o3-mini, Claude 3.7), Debug2Fix (GPT-5, Sonnet 4.5, Haiku 4.5) and DoVer (GPT-5).

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Observations come only from real execution. The model never writes the observation field and never simulates a run in place of one. G2 already says "revise only from real output"; extend it to "no simulated observation". | G2 (sharpen) | [E] in direction (3 sources: AutoSD, LDB, NExT); size is model-dependent | b09, c03, d11, c16 (K06, K14, K25) |
| A2 | No self-verdict without an outside check. Already in 4b and G2; record this subfield's extra sources (Huang, Olausson, CRITIC, Reflexion). | G2, 4b | [E] | a21, b20, b18, a26, b29 (K11) |
| A3 | Do not treat the model's own prediction of program behaviour as a fact. Use it as a hypothesis, trusted only after the run confirms it. | G10 (text is not evidence) | [E] | a25, d10, b26 (K16, K25) |
| A4 | Closed observe loop for any claim about runtime behaviour: act, observe, then conclude, rather than reason alone. | S4, S5 | [E] | c25, c22 (K21) |
| A5 | Where a probe tool exists, tool and interface design are part of the schema and must be logged and tested, not assumed. | tooling | [E] | b25, c28 (K18) |

### Test first (single-source or contested; see UNKNOWNS.md)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Required written prediction before each probe, with code comparing it to the observation; mismatch on a valid probe triggers S5 doubt. | O (predict-then-observe), G1 trigger | [C] | a15, c01, d01 (K05, K24) |
| T2 | Experiment validity gate: a refutation counts only if the probe ran (hit counter, non-empty output). | G (new) | [S] | c04, d03, d02 (K08) |
| T3 | Forced first probe: no patch before one executed probe (vs probe unlocked after N failed rewrites vs optional). | S4/S5, O | [S] | d08, d09, d06 (K26, K12) |
| T4 | Hypothesis supply: a separate call lists 3 to 5 distinct causes with different predicted symptoms. | S2/S3 | [S] | b03 (K03) |
| T5 | Commit signal: "hypothesis confirmed by an observation" as the stop token (AutoSD DONE) in S7/S9. | S9 | [S] | b10, c02, d13 (K07) |
| T6 | Disconfirming test: force one probe designed to break the leading hypothesis. | O | [C] | a03, a04, c23 (K20) |
| T7 | One follow-up probe round after the first answer. | O | [S] | c09 (K13) |
| T8 | Why-not question against the expected output, answered from a trace. | O | [S] | a14, d15 (K22) |
| T9 | Prediction as a probe ranker (run the probe the prediction says is most informative), never as a replacement. | S4 | [S] | d14 (K27) |
| T10 | Bug-type routing: for logic bugs require an explicit expected-behaviour statement before reading output. | S0 gate | [S] | d16 (K17, K29) |
| T11 | Line-by-line explanation when no tests exist. | O | [S] | a18, d12 (K15) |

Not for the agent: the patch-review explanation result (K09) is for human readers. It also warns that a tidy trace can be accepted without scrutiny.

## 8. Concrete tests on our bench

All tests compare arms at equal tokens (total input plus output across all calls, setup included, G7). At least 3 runs per item. Report pass rate, tokens, and a paired difference with a bootstrap interval. Use a weak and a strong model where stated, because strength flips several effects.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 prediction step (T1, gap 1) | Bugs with an executable test (code-repair items; hold-out set of 100 or more) | A: plain iterate with real test output. B: same plus required pre-run prediction and code-checked mismatch. C: B but the prediction is only logged, never used | Fix rate at equal tokens; share of mismatches followed by a changed hypothesis | Small or none on fix rate (AutoSD and Straubinger priors); possible gain on wrong-fix rate and a useful log. Add only if B beats A by 3 points or more |
| B2 prediction accuracy log | Same items | Observe only: log predicted vs observed on every probe | Match rate overall; match rate on runs ending in a correct vs wrong fix | If the match rate is under 60% on valid probes, keep prediction out of verdict use (A3). Tests whether prediction error precedes wrong fixes (gap 2) |
| B3 validity gate (T2) | Items with at least one wrong rejected hypothesis, from B1 logs | A: ungated. B: gate forces inconclusive when the probe did not run | Wrong rejections per run; fix rate | Fewer wrong rejections (13 of 25 prior); fix-rate gain 2 to 5 points |
| B4 forced probe (T3) | Same items, weak and strong model | A: no probe tool. B: probe optional. C: no edit before one executed probe. D: probe unlocked after 2 failed attempts | Fix rate; probe call rate | C or D above B for the strong model; the weak model may fall below A (debug-gym) |
| B5 hypothesis supply (T4) | Items with a hidden cause (several plausible candidates) | A: one plain hypothesis. B: 3 to 5 candidate causes, probe splits them | Correct first-hypothesis rate; probes to fix | Higher correct-hypothesis rate (OR 6.24 human prior) at equal tokens |
| B6 stop signal (T5) | Items with partial tests | A: stop on first plausible patch. B: stop only on DONE (hypothesis confirmed by observation) | Precision of "stop" against a held-out test | DONE group about 7 points more correct (89 vs 82). Add if the gap is 5 points or more |
| B7 disconfirm (T6) | Items with two competing hypotheses | A: free test choice. B: one test chosen to break the leading hypothesis | Fix rate; probes to the correct cause | Unknown; could help broad-hypothesis cases |
| B8 follow-up (T7) | Items where the first answer fails | A: one extra independent attempt. B: one follow-up probe round | Fix rate at equal tokens | ChatDBG 67 to 85% prior; check it is not just extra sampling (Olausson: 0.97x to 1.05x) |
| B9 logic vs syntax (T10) | Mixed set with a bug-type tag | A: plain feedback. B: expected-behaviour statement first | Fix rate by bug type | Gain only on logic bugs, if at all |
| B10 simulated vs real | Same items | A: real tool output. B: model-simulated output | Fix rate; DONE precision | A above B (prior: 73% vs 63%, DONE sign flip) |

## 9. What does not transfer, and why

- **Human protocols (Zeller log, Whyline UI).** They are aids for memory and attention. A model has neither limit in the same form. For people a log may slow impulsive edits; for a model the same effect needs a code gate.
- **Human hypothesis counts (11, 25, 39% correct).** Developers work in unfamiliar large codebases over hours. Our items are shorter. The numbers show a shape (early hypotheses are mostly wrong), not a rate.
- **The 5x odds ratio.** Correlational. Stronger debuggers likely both guess better and fix more. It does not show that forcing a hypothesis causes success.
- **"Debuggers help."** Holds for o1, o3-mini, Claude 3.7; fails for GPT-4o. It also depends on tool design. Do not assume it for any new model.
- **Patch-review explanation gains (K09).** Written for people judging patches. Not an agent test.
- **Whyline 7.8x.** Four users per arm, a teaching language (Alice). Do not plan on that size of effect.
- **Repository-scale bug hunting.** Most positive LLM results are on short functions (HumanEval, MBPP) with strong tests. The Reflexion MBPP drop shows how weak tests remove the gain.
- **Multi-agent blame (DoVer).** Its inconclusive rates come from agent systems that do not carry out interventions. The lesson (validate the experiment) transfers; the numbers do not.
- **Test generation (Straubinger).** A different task from repair; used only as the nearest ablation.
- **Old-model results.** GPT-3.5, Codex and GPT-4 Turbo numbers may not hold for reasoning models, which already reason about code well (Mini-nightmare near 100% for o1 and o3-mini).

## 10. Open questions

1. Does a written pre-run prediction raise the fix rate for a reasoning model at equal tokens? (gap 1)
2. How often is the pre-run prediction wrong on realistic repository bugs, and does the error precede a wrong hypothesis? (gap 2; REval is function-level only)
3. What share of refutations in current agents are invalid experiments? Only two counts exist (13 of 25; 57.6 to 66.7% inconclusive).
4. Where is the model-strength crossover for debugger help, and is it really about adoption? (gap 4)
5. Do disconfirming tests beat confirming ones for LLM debugging? (gap 5)
6. Is the 5x result causal? Do LLM-supplied candidate hypotheses help as human-supplied ones did? (gap 6)
7. Is the confirmation token (DONE) calibrated on current models? 89 vs 82% is a small gap on hand-labelled samples. (gap 7)
8. Do the classics (Gould, Vessey, Gugerty and Olson, Katz and Anderson, Parnin and Orso, Zeller 2009) say what we summarise? Never opened. (gap 8)
9. Does the Whyline or AutoSD result replicate in an LLM agent, independently? (gap 9)
10. How do results vary by bug type under a predict-observe loop? (gap 10)
11. Do humans who follow Zeller's protocol debug faster? No controlled trial found (K23).
12. In debug-gym's delayed unlock (debug(5)), does the gain come from the delay or from the failed attempts that supply context?

## 11. Sources

[V] = opened and read this session (full text unless noted). [M] = snippet or secondary citation only.

- [M] Zeller (2009) Why Programs Fail, 2nd ed. https://www.whyprogramsfail.com/ (a01)
- [M] Siegmund et al., as cited in Kang et al. 2023. https://arxiv.org/abs/2304.02195 (a02)
- [M] Wason (1960) 2-4-6 task. https://doi.org/10.1080/17470216008416717 (a03)
- [M] Klayman and Ha (1987). https://doi.org/10.1037/0033-295X.94.2.211 (a04)
- [M] Klahr and Dunbar (1988) Dual space search. https://doi.org/10.1207/s15516709cog1201_1 (a05)
- [M] Gould (1975). https://doi.org/10.1016/S0020-7373(75)80005-8 (a06)
- [M] Vessey (1985). https://doi.org/10.1016/S0020-7373(85)80054-7 (a07)
- [M] Gugerty and Olson (1986). https://doi.org/10.1145/22339.22367 (a08)
- [M] Katz and Anderson (1987). https://doi.org/10.1207/s15327051hci0304_2 (a09)
- [M] Parnin and Orso (2011). https://doi.org/10.1145/2001420.2001445 (a10)
- [M] Zeller and Hildebrandt (2002) delta debugging. https://doi.org/10.1109/32.988498 (a11)
- [M] Ko and Myers (2008) Debugging reinvented. https://doi.org/10.1145/1368088.1368130 (a12)
- [V] Ko and Myers (2004) Designing the Whyline. https://faculty.washington.edu/ajko/papers/Ko2004Whyline.pdf (a13, a14, d15)
- [V] Kang, Chen, Yoo, Lou (2023) AutoSD. https://arxiv.org/abs/2304.02195 (a15 to a17, a27, b08 to b13, c01 to c05)
- [V] Chen, Lin, Schaerli, Zhou (2023/2024) Self-Debug. https://arxiv.org/abs/2304.05128 (a18, b22, b23, c12, d12)
- [V] Zhong, Wang, Shang (2024) LDB. https://arxiv.org/abs/2402.16906 (a19, b14 to b16, c11, d11)
- [V] Olausson et al. (2024) Is self-repair a silver bullet. https://arxiv.org/abs/2306.09896 (a20, b17 to b19, c13)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (a21, b20, b21, c14)
- [V] Yuan et al. (2025) debug-gym. https://arxiv.org/abs/2503.21557 (a22, c06 to c08, d06, d07)
- [V] Ni et al. (2024) NExT. https://arxiv.org/abs/2404.14662 (a23, c16)
- [V] Chen/Liu et al. (2024) Reasoning runtime behavior (REval). https://arxiv.org/abs/2403.16437 (a24, c18, d10)
- [V] Gu et al. (2024) CRUXEval. https://arxiv.org/abs/2401.03065 (a25, b26, b27, c17)
- [V, abstract and summaries only] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (a26)
- [V] Alaboudi and LaToza (2020) Using hypotheses as a debugging aid. https://arxiv.org/abs/2005.13652 (b01 to b04)
- [V] Alaboudi and LaToza (2021) Exploratory study of debugging episodes. https://arxiv.org/abs/2105.02162 (b05 to b07)
- [V] Tian et al. (2024) DebugBench. https://arxiv.org/abs/2401.04621 (b24, c29, d16)
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/abs/2405.15793 (b25, c28)
- [V] Yang et al. (2023) InterCode. https://arxiv.org/abs/2306.14898 (b28)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (b29, b30)
- [V] Levin et al. (2025) ChatDBG. https://arxiv.org/abs/2403.16354 (c09, c10)
- [V] Liu et al. (2024) CodeMind. https://arxiv.org/abs/2402.09664 (c19)
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540 (c20, c21)
- [V] Qiu et al. (2024) Phenomenal yet puzzling. https://arxiv.org/abs/2310.08559 (c22)
- [V] Lampinen et al. (2024) Content effects on reasoning. https://arxiv.org/abs/2207.07051 (c23)
- [V] Krishnamurthy et al. (2024) LLMs and exploration (bandits). https://arxiv.org/abs/2403.15371 (c24)
- [V] Yao et al. (2023) ReAct. https://arxiv.org/abs/2210.03629 (c25)
- [V] Bouzenia, Devanbu, Pradel (2024) RepairAgent. https://arxiv.org/abs/2403.17134 (c26)
- [V] Zhang et al. (2024) AutoCodeRover. https://arxiv.org/abs/2404.05427 (c27)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors. https://arxiv.org/abs/2311.08516 (c15; no number quoted)
- [V] Straubinger et al. (2025) Mutation testing via iterative LLM-driven scientific debugging. https://arxiv.org/abs/2503.08182 (d01, d02)
- [V] Ma et al. (2025/2026) DoVer. https://arxiv.org/abs/2512.06749 (d03 to d05)
- [V] Garg and Huang (2026) Debug2Fix. https://arxiv.org/abs/2602.18571 (d08, d09)
- [V] Spiess et al. (2024) Calibration and correctness of LMs for code. https://arxiv.org/abs/2402.02047 (d13)
- [V] Zheng et al. (2026) ForeAgent. https://arxiv.org/abs/2601.05930 (d14)
