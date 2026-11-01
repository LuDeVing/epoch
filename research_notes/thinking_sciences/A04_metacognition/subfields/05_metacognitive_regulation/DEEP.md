# Metacognitive regulation: deep document

*Subfield A04.05. Built from evidence_a-d.jsonl, claims.jsonl (K01-K34) and critique.md in this folder. Evidence ids (a01..d17) point to those files. Status marks: [E] established, [S] single-source, [C] contested.*

*Honest warning up front: the founding human studies (Flavell, Brown, Nelson and Narens, Swanson, Perkins and Salomon, Schraw and Dennison, Mevarech and Kramarski) were NOT opened. Their content here comes from secondary summaries. The LLM papers were mostly opened and key numbers were re-checked against the PDFs.*

## 1. What it is

Metacognitive regulation is the control half of metacognition. The learner plans before acting, monitors progress while acting, and evaluates afterwards. Typical self-questions: "What is the task?", "Is it getting me anywhere?", "Did that work?", "Should I switch?"

The other half is metacognitive knowledge: what I know about myself, the task, and which strategy fits which task. Regulation uses that knowledge, but it is the doing part.

For our agent the focus is the S6 trigger (when to stop, switch or review) and the review step itself. The central practical question: does asking a model to monitor and review its own work help, and under what conditions?

Short answer from the evidence:
- Humans: trained regulation raises achievement. Online measures (what a learner does) predict performance better than questionnaires (what a learner says).
- LLMs: unaided self-review without an outside signal does not help and often hurts. It helps when a real check supplies the signal (tests, tools, oracle labels), when the error is framed as someone else's, or when training taught it.
- Stop and switch decisions that work in practice use trace features (answer agreement, confidence, thought-switch counts, repeats), not a prompted self-question. No study tests the self-question head to head (K25).

## 2. History and theories in depth

**Flavell (1979) [a01, not opened].** Coined "metacognition". Four parts: metacognitive knowledge (person, task, strategy variables), metacognitive experiences (feelings such as "this is hard"), goals, actions. Monitoring emerges from their interplay. Vocabulary for us: strategy knowledge is what a class record could hold; a "metacognitive experience" must become a coded signal.

**Brown (1978, 1987) [a02, not opened].** Framed regulation as executive control: planning, monitoring, checking, revising. Learners without these skills fail even with adequate knowledge. Her empirical base is children's reading and memory strategy training. Effects were task-specific. This is the source of the plan / monitor / evaluate triple.

**Nelson and Narens (1990) [a03, not opened].** Two levels. The object level does the task. The meta level holds a model of it. Monitoring sends information up. Control sends commands down: continue, stop, switch strategy, allocate time. Built on memory tasks (judgments of learning, feeling of knowing), where monitoring accuracy is the bottleneck. This is the formal frame for our S6.

**Perkins and Salomon (1989) [a05, not opened].** General strategies, including metacognitive ones, transfer only when taught with real content and with cues to apply them. "Low road" transfer is practised routine. "High road" transfer needs mindful abstraction. Implication: a generic "reflect" prompt should not be expected to carry over; cues and content matter.

**Swanson (1990) [a04, b01, d15; never opened].** 2 x 2 design on children: high or low aptitude crossed with high or low metacognitive knowledge, on pendulum-type problem solving. High-metacognition children beat low-metacognition children at both aptitude levels. This is the origin of "metacognition compensates for low IQ". Exact N and effect sizes are unverified. A later critique says forcing the two factors to be orthogonal by design limits what the study can show. Two attempts to open it failed (APA 403; Crossref has no abstract; 271 citing works). Treat as background only (K05, K34).

**Veenman and colleagues [a07, b08, not opened].** Three rival accounts: intelligence model, independence model, mixed model. The mixed model (metacognitive skill overlaps with ability but adds prediction beyond it) is best supported. Metacognition matters most at the edge of what the learner knows. This partly contradicts the strict independence reading of Swanson. They also argue for online measures (think-aloud, observation) over questionnaires.

**Schraw and Dennison (1994) [a06, not opened].** The 52-item Metacognitive Awareness Inventory. Two factors: knowledge of cognition and regulation of cognition. Regulation has five subprocesses: planning, information management, monitoring, debugging, evaluation. 307 undergraduates over two experiments (179 in Exp. 1); alpha .90, factors correlate near .50 per citing papers. Self-report; one later study found only 25 of 52 items load cleanly.

**Mevarech and Kramarski (1997), IMPROVE [a08, not opened].** Students used cards with metacognitive self-questions (comprehension, connection, strategy, reflection) plus cooperative learning and feedback. N = 265 over a school year. IMPROVE beat controls, most on reasoning. Three components were applied together, so the questions cannot be isolated. A follow-up reported gains in regulation but not knowledge.

**The shift to LLMs (2022-2026).** The same ideas reappear as: calibration of "do I know this" (Kadavath 2022 [a21]), plan-then-solve prompts (Wang 2023 [a23]), generate-critique-refine loops (Madaan 2023 [a18]), reflect-and-retry agents (Shinn 2023 [a19]), then the 2023-24 critique that intrinsic review fails (Huang [a15], Kamoi [a16], Tyen [a17]), training that teaches it (Kumar [a20]), and the 2025-26 reasoning-model era where overthinking and underthinking are the new regulation failures (Chen [a24], Wang [c16]), with cheap monitors and early-exit triggers (Meta-R1 [c04], DEER [d10], DeepConf [d12]).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Metacognition correlates with maths performance in 11-16 year olds | r = .37, 95% CI [.29,.44]; 74 effect sizes, 29 studies, 30 populations. I2 up to 99.96% | Muncer 2021 [b02] (opened) | [E] correlational |
| Online measures beat offline | online r = .54 (k=14, I2 79%) vs offline r = .30 (k=60); p = .034. Measured during the task .48 vs not .28 (p = .027) | Muncer 2021 [b02] | [E] correlational |
| Same split in general performance | online .53 (90% CI .45-.61) vs offline .23 (.20-.26); beta .41 metacognition vs .32 intelligence in online studies | Ohtani and Hisasaka 2018, via Muncer and a secondary page [a10, b03] | [E] secondary |
| Task complexity moderates | complex tasks r = .48 (n=12, k=21); simple r = .10 (n=4). The "complex x online" cell .54 (n=13), omnibus only p = .058. (An earlier note said complex = .54; corrected.) | Muncer [a11 corrected] | [S] |
| Metacognitive processes beat plain cognitive strategies | r = .20 vs .11; rote memorising weak or negative | Dent and Koenka [a09] (secondary page) | [E] secondary |
| Teaching metacognition raises achievement | de Boer g = .50 post, .63 follow-up (48 interventions); Theobald g = .37 (49 studies), metacognitive strategies .40; Dignath and Buttner mean .69 (74 studies, 357 effects); Higgins .96 for metacognitive interventions; Eberhart .48 immediate, .29 later | [a12, b04-b07] secondary page only | [E] but numbers unopened |
| Domain moderates | Donker 2014 (58 studies, 180 effects): writing g 1.25, science .73, maths .66, comprehension reading .36 | [b06] abstract-level | [S] |
| Delivery moderates | Researchers deliver larger effects than teachers | Dignath and Buttner [b05] | [S] |
| Small randomised prompt studies often null | Engelmann 2021: 28 vs 29, no clear effect. Klar 2024: 51 prompted vs 150 control, none, half ignored prompts. A 2025 lab study N=110 and a K-12 maths study N=113 also null | [b09] snippets | [S] |
| Intrinsic review hurts (older models) | GPT-3.5 CSQA 75.8 -> 38.1 -> 41.8; GSM8K 75.9 -> 75.1 -> 74.7; HotpotQA 26.0 -> 25.0 -> 25.0. GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; CSQA 82.0 -> 79.5 -> 80.0; HotpotQA 49 -> 49 -> 43. Columns are 1, 3, 5 model calls | Huang 2024 [a15, b10, d01] (opened, re-checked) | [E] |
| Oracle stop signal produces the gains | GPT-3.5 GSM8K 75.9 -> 84.3, CSQA 75.8 -> 89.7, HotpotQA 26.0 -> 29.0; GPT-4 GSM8K 95.5 -> 97.5, CSQA 82.0 -> 85.5, HotpotQA 49 -> 59 | Huang Table 2 [a15, d01] | [E] |
| Changes go the wrong way | GPT-3.5 kept its GSM8K answer 74.7% of the time; changes were more often right-to-wrong | Huang [a15] | [E] |
| Survey: no prompted self-correction on general tasks | Works with reliable external feedback (code run, search) or large-scale fine-tuning. Bottleneck is feedback generation | Kamoi 2024 [a16, b13, c09, d02] | [E] |
| Finding mistakes is the bottleneck | BIG-Bench Mistake, 2,186 traces; GPT-4 best 52.87 (tasks 17.06 to 90.67). Backtracking with true location: wrong traces +18 to +44 (arithmetic +43.9, Dyck +36.9, tracking +23.5), right traces lose 0 to 11. Random location: wrong +5 to +21, right -7 to -16 | Tyen 2024 [a17, b12, c08] | [S] one study, 5 models |
| Training can teach it | Gemini 1.5 Flash MATH500: base 52.6 -> 41.4 (right-to-wrong 15.8%, wrong-to-right 4.6%). SCoRe 60.0 -> 64.4 (+4.4); abstract +15.6 MATH, +9.1 HumanEval. Self-Refine 52.8 -> 51.8; STaR 53.6 -> 54.0; Pair-SFT 52.4 -> 54.2. Part of SCoRe gain is a better first try | Kumar 2024 [a20, b14, c12] | [S] |
| Self-Refine: gains on style, none on maths | ~20% absolute average over 7 tasks; dialogue 36.4 -> 63.6; code readability 37.4 -> 51.3; code optimisation 14.8 -> 23.0; maths 64.1 -> 64.1. Feedback on maths said "everything looks good" for 94% of cases. Failure analysis: new problem introduced 20%, feedback ignored 25% | Madaan 2023 [a18, c07] | [E] with Huang |
| Reflexion works with a real signal | ALFWorld 130/134 over 12 trials (+22%); HotPotQA +20%; HumanEval 91.0 vs 80.1; MBPP 68.0 vs 60.0; LeetcodeHard 77.1 vs 80.1 (below GPT-4). Triggers are code rules: same action and response for >3 cycles, or >30 actions | Shinn 2023 [a19, b15, c06] | [E] with signal |
| Self-verification is unreliable | GPT-4 as own verifier: false positives and negatives. With a sound external verifier, critique content barely matters: ~40% on graph colouring, equal to blind resampling n=15 at t=1.0. 100 instances per domain | Stechly 2023, 2024 [c17, c18] | [E] |
| Tool matters | CRITIC (HotpotQA EM/F1) 38.7/50.5; without tool 34.9/46.1; CoT 33.7/46.1; self-consistency 34.9/47.5 | Gou 2024 [d14] | [E] (row labels partly ambiguous) |
| Self-repair vs equal samples | GPT-4 on APPS: 1.05x over pass@20 at best, some configs 0.97x. Human feedback instead of GPT-4's own explanation: 33.3% -> 52.6% | Olausson 2024 [d03] | [E] |
| Debate does not beat voting | GSM8K GPT-3.5: standard 76.7; self-consistency 82.5 / 85.3 / 88.2 at 3 / 6 / 9 samples; debate about 83 (table garbled) | Huang [b11] | [S] |
| Revise vs resample depends on difficulty | Easy: sequential revision wins. Hard: parallel/tree search wins. Adaptive policy matches best-of-N with ~4x less compute (PaLM 2-S*, MATH) | Snell 2024 [d04] | [S] |
| Blind spot | 14 open non-reasoning models: 64.5% average blind spot. Claude 3.5 Haiku 52.5%, Sonnet 4 41.4%. Non-math 62.8%. Own natural errors caught when shown externally: 4.3-10.8% | Tsui, Self-Correction Bench [b17, c13, d05] | [S] |
| "Wait" cue | Blind spot cut 89.3%, mean accuracy +156%. Qwen3-14B 0.117 -> 0.868 (reasoning twin 0.843); Qwen3-32B 0.045 -> 0.793 (0.894); DeepSeek-V3 0.567 -> 0.902; phi-4 0.325 -> 0.701. SFT on 5,306 traces cut blind spot 76.0% | Tsui [d05, c13] | [S] injected errors, no length-matched filler |
| Overthinking | "2+3": 1,953% more tokens than conventional models; first round correct in over 92% of cases; self-training cut tokens 48.6% on MATH500 (QwQ-32B-Preview), accuracy kept | Chen 2025 [a24, c15, d06] | [S] |
| Underthinking | Wrong answers have more thoughts (e.g. 26.4 vs 12.6 on AIME24). Underthinking score QwQ 58.2 MATH500-Hard, 48.3 GPQA, 65.0 AIME24. TIP: QwQ AIME24 38.3 -> 44.1; GPQA 57.6 -> 59.1; R1-Distill-32B AIME24 61.4 -> 64.1; R1 73.8 -> 74.8. Prompt alone gave little | Wang 2025 [c16, d07] | [S] |
| Budget forcing | s1-32B (1,000 SFT examples) AIME24 50.0 -> 56.7. (57.6 is a GPQA ablation cell; corrected) | Muennighoff 2025 [b18, c14] | [S] trained model |
| Trace triggers save tokens | DEER: CoT 19.1-80.1% shorter, accuracy +0.3 to +5.0 (11 models, 10 benchmarks). Probe: -24% tokens, no accuracy loss, ROC-AUC >0.7, ECE <0.1. DeepConf: up to 84.7% fewer tokens; AIME25 GPT-OSS-120B 99.9 vs 97.0 majority vs 91.8 pass@1. Short chains: up to 34.5% more accurate than the longest; short-1@k up to 40% fewer tokens | [d10, d11, d12, d08] | [E] across 4 sources, open reasoning models |
| NoThinking at equal tokens | ACM23 at 700 tokens: 51.3 NoThinking vs 28.9 Thinking | Ma 2025 [d09] | [S] |
| Cheap separate monitor | Meta-R1 14B backbone: avg 84.0 at 5,691 tokens -> 87.0 at 3,941; AIME24 64.4 -> 70.0. Tokens 15.7-32.7% of vanilla. Larger monitor: 14B gives +0.1 for +18.6% tokens. No self-monitor arm | Dong 2025 [c04, d13] | [C] author benchmarks only |
| MetaRAG | HotpotQA EM/F1 37.8/49.9 vs Reflexion 30.0/43.4, IR-CoT 31.4/40.3, CoT 22.4/34.2; 2Wiki 42.8/50.8 vs Reflexion 31.8/41.7 | Zhou 2024 [c01] | [C] |
| Forced PME prompt hurts weak model | Llama-3-8B GSM8K Std 80.71, CoT 77.98, Ann Brown 69.55. CorrectBench Std 52.91, CoT 75.02, Ann Brown 68.14. CRUXEval-O Std 5.25, Ann Brown 5.12, CoT 25.62. Qwen-3-8B GSM8K 91.72 vs 91.65 flat | Think2 2026 [c02, c23] | [S] 2 small models, preprint |
| Funnel | Error cases: awareness 51.2%, correct diagnosis 27.9%, improvement 16.3%. Forced structure: diagnosis 58.3%, improved 50.0% (12/24) vs CoT 25.0%. 580 human pairs favoured the traces (84%), may reflect style | Think2 [c03] | [S] |
| Skill-label routing | MATH: +11.6% over CoT, +3.5% over complex CoT, +7.52% over PAL, +4.0% over CoT-SC | Didolkar 2024 [a13, b22, c21] | [S] |
| Metacognitive prompting (5 stage) | NLU, 4 models, 10 sets: +4.8 to 6.4% over CoT, +2.8 to 4.1% over plan-and-solve. GPT-4 QQP 89.9/86.2 vs CoT 88.9/84.7 | Wang and Zhao [a14, c10] | [S] no token-matched baseline |
| Plan-first prompting | text-davinci-003, six maths sets: CoT 70.4, PS 73.5, PS+ 76.7. GSM8K 56.4 / 57.0 / 59.3. Self-Discover up to +32% over CoT, avg BBH +11% (PaLM 2-L), +7% (GPT-4), 10-40x less compute than CoT-SC | [a23, a22] | [E] older models |
| Multi-agent failures are monitoring failures | 1,600+ traces, 7 frameworks, kappa .88. Misalignment 36.9%, verification 21.3%, step repetition 15.7%, task-completion not recognised 12.4%, reasoning-action mismatch 13.2%, wrong verification 9.1%, none 8.2%, premature termination 6.2%. Role-spec plus verification fix +9.4% | Cemri 2025 [b16] | [S] |
| Self-knowledge | Up to 52B models calibrated on multiple choice; P(True)>0.5 raises accuracy; P(IK) generalises partly | Kadavath 2022 [a21] | [S] 2022 base models |
| Planning ceiling | GPT-4 ~34% Blocksworld (210/600); Mystery Blocksworld 1/600 | Valmeekam 2023 [c19] | [S] pre-reasoning models |

## 4. Mechanisms and models

### 4.1 Nelson-Narens loop (implementable)

```
object level  = the solver (model call, code run)
meta level    = program state: plan, progress counters, class record
monitoring    = signals from object level to meta level (must be observable)
control       = commands from meta to object level: continue, stop, switch operator, resample, review
```
Engineering rule from the evidence: monitoring signals must come from a place that is not the model's own opinion of itself. Candidates, in order of strength:
1. External check output (unit test, tool result, programmatic verifier). Strongest (K06, K07, K20, K27).
2. Agreement among independent samples (not proof, G4, but a hint).
3. Trace features: repeated step, no new fact in last N steps, thought-switch count, answer-at-boundary agreement (K23, K30, K31).
4. Token-level or hidden-state confidence, if the API gives logprobs (DEER, DeepConf, probe).
5. Model-stated confidence or "am I stuck?" (weak; K24 older models; SCHEMA says r = .17).

### 4.2 Two-sided stop/hold rule (design, not yet tested)

Overthinking says stop early when the first answer checks. Underthinking says hold on a path when switches pile up on hard items. Sketch:
```
after each candidate answer A_k at a step boundary:
  if check(A_k) passes or A_k == A_{k-1} == (independent sample answer): STOP
  elif switches_in_last_window >= T_switch and difficulty == hard: HOLD (discourage new direction, spend on current path)
  elif no_new_fact_in_last_N or same_error_twice: S6 (impasse operator)
```
Difficulty comes from class record or first-pass agreement rate (Snell: difficulty decides revise vs resample).

### 4.3 Locate then fix (Tyen)

Split review into finding and fixing. Finding is weak (52.87 at best). Fixing with a true location is strong. So code must supply the location: failing test line, differing output, first step where a recomputation disagrees. A random location hurts correct traces (-7 to -16). This matches schema guardrail G2.

### 4.4 Why intrinsic review hurts

Huang: the model cannot tell right from wrong, so a revise prompt acts like a nudge to change a correct answer. Without a stop signal it flips right to wrong more than the reverse (SCoRe base: 15.8% vs 4.6%). Self-Refine's maths feedback said "all good" 94% of the time. Remedy: change only on a real failing signal; otherwise keep the first answer.

### 4.5 Blind spot and the Wait cue

Tsui traces the blind spot to training data with almost no correction sequences. Reasoning-trained twins do not show it. Appending "Wait" restores correction behaviour in non-reasoning models. The mechanism is a cue that switches the model into a correction mode, not new information. Limits: errors were injected by prefill, tasks simple, no length-matched filler arm. The cheap test is to compare "Wait", neutral filler of equal length, and "a colleague wrote this".

### 4.6 Separate cheap monitor (Meta-R1)

A 1.5B-3B model reads the last chunk of reasoning and injects advice when token-type frequencies cross a threshold. Removing online regulation cost most in ablation. Larger monitors added little. The monitor works on frequency features and logit control, so it is nearer a trace trigger than a prompted self-question. It never competed with same-model self-monitoring.

### 4.7 Planning and skill typing

Planning once per task is cheap (Self-Discover: 10-40x less compute than CoT-SC). Skill labelling selects exemplars (Didolkar). Both are conditional knowledge: which method fits which problem. In our terms: the class record in S0 plus operator choice in S6.

## 5. What holds up

**Holds up (agreed across sources):**
- Intrinsic prompted review does not reliably help reasoning (Huang, Kamoi, Tyen, Stechly, Olausson, Gou). [E]
- Review with a good external signal helps (Reflexion, CRITIC with tool, oracle in Huang, Tyen with true location). [E]
- Token-matched sampling controls often erase review gains (K33). [E]
- Trace or internal-signal triggers save tokens at equal or better accuracy (4 sources). [E]
- Humans: online measures correlate more than questionnaires (Muncer, Ohtani, Dent). [E but correlational]
- Human training of metacognition has positive effects in meta-analyses, though numbers shrink with follow-up and non-researcher delivery. [E secondary]

**Failures, nulls and boundary conditions:**
- Small prompt-only human studies often null (Engelmann, Klar, others). Prompt uptake poor.
- Swanson compensation not verified. Meta-analyses show moderators of measure type and task complexity, not learner ability (K05, b23). Theobald found lower performers gained more only in resource management.
- Think2 forced PME structure hurt a weak model and was flat on a reasoning-native one.
- Self-Refine and Reflexion gains do not contradict Huang: environment signal vs none. Gains on style tasks are preference-judged.
- Debate ties voting at equal samples.
- Intrinsic review got worse with more rounds (GPT-4 HotpotQA 49 -> 43).
- "Wait" cue: strong on non-reasoning open models, Sonnet 4 still 41.4%; not tested on reasoning models.
- Overthinking fix helps easy items, not hard ones: later rounds do help on hard items (d06 limits). TIP gains 0.6 to 5.8 with large spread.
- Meta-R1 and MetaRAG: author benchmarks, no independent replication.

**Moderators:**
- Humans: measure type (.54 vs .30), task complexity, domain (writing 1.25 vs reading .36), delivery (researchers > teachers), follow-up (Eberhart .48 -> .29, but de Boer .50 -> .63).
- LLMs: external signal quality, model type (reasoning vs non-reasoning), item difficulty, attribution framing (mine vs other's), whether training included correction sequences.

**Interventions that worked:** external tests, tools, true error location, "Wait" on non-reasoning models, RL training for correction (SCoRe), trace/confidence early exit, difficulty-adaptive allocation, small monitor model.

**Interventions that did not:** generic "review your answer" prompts, debate, forced three-phase prompts on weak models, larger monitor models, model-stated critique when a sound verifier exists (content irrelevant), prompt instruction to stay on one path (TIP prompt alone small).

**Reconciled contradictions (from critique):** human effect sizes (g .37 to .69) come from different samples, outcomes and moderators; no source reconciles them. Meta-R1/MetaRAG (cheap monitoring helps) versus Huang/Tyen/Stechly (self-monitoring fails) are compatible only if the monitor is separate or grounded. Think2 accuracy and funnel results disagree in direction (accuracy down, diagnosis up).

## 6. Language models

**Old models (2022-2024: GPT-3.5, GPT-4, PaLM 2, Gemini 1.x).**
- Intrinsic review: down 1 to 12 points on GSM8K over 2-3 extra rounds; CSQA collapses on GPT-3.5 (75.8 -> 38.1).
- With oracle stop: +8 to +14 on GPT-3.5, +2 to +10 on GPT-4.
- Mistake finding: 52.87 best (GPT-4). Fixing with location: +18 to +44 on wrong traces.
- Self-verification: false positives; with a sound verifier the critique content is irrelevant.
- Planning prompts: +3 on GSM8K, +6 average over CoT (text-davinci-003).
- Calibration: 52B base models answer P(True) usefully on multiple choice.

**Non-reasoning open and closed models (2025).**
- Blind spot 64.5%; Sonnet 4 41.4%, Haiku 3.5 52.5%.
- "Wait" nearly closes the gap to the reasoning twin (Qwen3-14B 0.117 -> 0.868).
- Forced three-phase prompt: Llama-3-8B GSM8K -11.2 points vs Standard.

**Reasoning models (2025-2026: QwQ, R1 distills, GPT-OSS, Qwen3).**
- Overthinking: first round right >92%; 48.6% token cut with accuracy kept after self-training.
- Underthinking: wrong answers show more switches; TIP +0.6 to +5.8 Pass@1.
- Early-exit triggers: DEER -19.1% to -80.1% tokens; probe -24%; DeepConf up to -84.7%, AIME25 99.9% at 512 traces.
- NoThinking beats thinking at 700 tokens (51.3 vs 28.9).
- Separate monitor: Meta-R1 14B 84.0 -> 87.0 with about 31% fewer tokens.
- Forced PME: flat on Qwen-3-8B.
- Short chains more accurate (up to 34.5%).

**Agents.** Multi-agent failures: verification and misalignment account for about 58%. Step repetition 15.7%. Reflexion triggers are code counters (repeat >3, >30 actions).

**What changed it, by how much.** External signal: +8 to +14 points (GPT-3.5 oracle). True location: +18 to +44 on wrong traces. Training: +4.4 net on second turn (SCoRe, plus a better first try). Cue "Wait": +156% mean accuracy on injected errors. Trace trigger: 19-85% fewer tokens at equal or better accuracy.

**What is not known.** No clean token-matched intrinsic-review arm exists for 2025-26 frontier models. Sonnet 4 and Haiku 3.5 rows are the only recent closed-model data. The reasoning-model era may have removed the Huang effect; nobody has measured it against extra-sample controls (gap 2).

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | Review (S5/S6) fires only on an external failing signal (test, tool, differing output, disagreement). No unconditional "check your answer" step. | G1, G2, S5 | [E] | a15, b10, d01, a16, d02, c05 (K06, K07, K26) |
| 2 | When the signal is weak, keep the first answer and do not revise. Intrinsic revision flips right to wrong more often than the reverse. | G2, S5 | [E] | a15, b14, c12 |
| 3 | Locate with code, then ask the model to fix only that location. Random or model-chosen locations hurt correct traces. | G2, S5, O | [E] for the rule; numbers [S] | a17, b12, c08 (K08) |
| 4 | Monitor from the trace, not from what the model says about itself: repeated step, no new fact, same error twice, thought-switch count, answer agreement at step boundaries. Stated confidence is not a trigger until calibrated on our items. | S6 trigger, G10 | [E] | b02, b03, a10, d08, d10, d11, d12, c16, b16 (K02, K31) |
| 5 | Code-checked early stop: stop when the first candidate passes the check or independent samples agree. First rounds are right >92% of the time on easy items. | S6 stop, G11 | [E] for trace triggers, [S] for the 92% | c15, d06, d10, d12 (K11, K30, K31) |
| 6 | Use a programmatic verifier where one exists. Model self-verification gives false positives; with a sound verifier the critique text does not matter. | G5, S4, S8 | [E] | c17, c18, d14, d03 (K20, K27) |
| 7 | Reflect-and-retry with memory only where an external success signal exists. Keep a short memory of reflections (last 3). | S5/S6 retry, memory | [E] | a19, b15, c06 (K19) |
| 8 | No debate; every new regulation element gets an equal-token extra-sample arm. | G9, G7 | [E] | b11, d17, d03, d04, d09, d14 (K21, K33) |
| 9 | Budget review by difficulty: easy items favour sequential revision, hard items favour parallel resampling. | G12, S0 | [S] here, already [E] in G12 | d04 (K28) |
| 10 | Treat human training effects as human-trained skill; do not expect a prompt to reproduce them. | background | [E] | b09, a05, a12 (K03, K04) |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | The prompted self-question "Is it getting me anywhere?" at S6 against a trace-feature trigger against a fixed budget. | S6 | [C] untested (K25) | c26, d16 |
| T2 | "Wait" / "a colleague wrote this" cue at the review step against equal-length neutral filler. | S5 wording | [S] (K10, K29) | b17, c13, d05 |
| T3 | Two-sided stop/hold rule (stop when first answer verifies; hold when switches pile up on hard items). | S6 | [S] (K30) | d06, d07, d04 |
| T4 | Cheap separate monitor against same-model monitor at equal total tokens. | S6 controller | [C] (K22, K32) | c04, d13, c01 |
| T5 | Does intrinsic review still lower accuracy on the current backbone, at equal tokens versus an extra sample? | G1, S5 | [E] for old models; open for new (K26) | a15, d01 |
| T6 | Plan-first step (once per task) against the same tokens on extra CoT samples. | S2/O | [E] for old models (K15) | a23, a22, c11 |
| T7 | Skill/problem-type label then retrieve exemplars, against the same tokens as extra CoT samples. | S0/S1 | [S] (K14) | a13, b22, c21 |
| T8 | Forced plan-monitor-evaluate on every step versus trigger-only, on a weak and a strong model. | S6 | [S] (K17) | c02, c23 |
| T9 | Diagnosis step (aware / diagnosed / fixed rates) on our own failed runs. | S5/S6 | [S] (K18) | c03 |
| T10 | Step-repetition detector: how often it fires, whether stopping saves tokens. | S6 | [S] (K23) | b16 |
| T11 | Calibration check: does stated confidence predict error on our items? | S6 | [S] (K24) | a21 |

## 8. Concrete tests on our bench

All tests: all arms at equal total tokens, including trigger and setup cost (G7). Report accuracy with a paired comparison over the same items.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Items with a programmatic check (code with tests, ARC-style verifiable) and items without (open maths) | (a) no review; (b) always review; (c) review only when external check fails; (d) extra independent sample | Accuracy; right-to-wrong and wrong-to-right counts | (c) best or tied with (d); (b) below (a) on no-check items. Huang pattern may persist or shrink on frontier models |
| B2 | Mixed easy/hard items, reasoning backbone | (a) fixed budget; (b) trace trigger (answer agreement at step boundary, repeats, switches); (c) prompted self-question "Is it getting me anywhere?" every N steps | Accuracy per token; tokens to first correct answer | (b) saves 20-50% tokens at equal accuracy; (c) no better than (a), possibly worse |
| B3 | Injected or natural errors in earlier steps | (a) "Review your step"; (b) "Wait"; (c) equal-length neutral filler; (d) "a colleague wrote this step" | Fix rate on wrong traces; damage rate on right traces | (b) and (d) beat (a) and (c) on non-reasoning models; small or no effect on reasoning models |
| B4 | Easy vs hard split | (a) always continue; (b) stop if first answer verifies; (c) two-sided rule with hold on hard items | Tokens; accuracy on each split | (b) cuts tokens on easy items; (c) beats (b) on hard items by about 1-3 points |
| B5 | Tasks with a localisable error | (a) model locates and fixes; (b) code locates, model fixes; (c) random location | Localisation accuracy; fix rate; damage to right traces | (b) > (a) > (c); model-only localisation near 50% |
| B6 | Multi-step tasks | (a) no monitor; (b) same-model monitor; (c) cheap-model monitor | Accuracy; total tokens including monitor | (c) saves tokens; accuracy gain unproven |
| B7 | All item types | (a) plan-first once; (b) skill label + exemplars; (c) same tokens as extra CoT samples | Accuracy | Gains shrink on strong models; may vanish vs (c) |
| B8 | Weak and strong model | (a) forced PME every step; (b) trigger-only PME; (c) plain CoT | Accuracy; tokens | (a) hurts weak model, flat on strong; (b) at least ties (c) |
| B9 | Our own failed runs | Log awareness, diagnosis, fix separately | Funnel rates | Diagnosis well below awareness; fix below diagnosis |
| B10 | Agent traces | Step-repeat detector: fire count and tokens saved on stop | Fires per run; tokens saved; false stops | Fires in about 10-15% of failing runs (MAST 15.7%); saves tokens with few false stops |
| B11 | Held-out items | Calibration curve of stated confidence vs correctness | AUROC, ECE | Decide whether confidence may trigger anything |

## 9. What does not transfer, and why

- **Human training effects (g .37 to .96).** They come from months of instruction in schools, mostly with researcher delivery. A prompt is not training. Small prompt-only human trials were null. Only SCoRe-style training in the model gives a comparable effect, and our scaffold cannot train.
- **Swanson compensation.** Unverified, human, age-specific, and our agent has no "low-IQ" mode to compensate. A weak-vs-strong backbone pair would be a different test.
- **Feelings of knowing, fluency illusions, self-efficacy, motivation.** About people. A model has no felt sense of knowing; build signals in code.
- **Questionnaires (MAI).** Self-report instruments for humans. Our analogue of the online-over-offline result is: trust trace behaviour, not self-description.
- **Correlational r values.** They show association with school performance. They do not say that adding a monitor causes gains. Use only as a prior for what to log.
- **Gains on style tasks (Self-Refine, preference-judged).** No ground truth and model judges. Reasoning tasks differ.
- **Trained or decoding-level methods (SCoRe, s1, Meta-R1 training, self-training for brevity, TIP, DEER, probes).** Need weights, logits or decoding access. Use the idea (what signal to watch), not the implementation, unless the API gives logprobs.
- **Old-model numbers (GPT-3.5, davinci-003).** Plan-and-Solve gains and Huang collapses may be smaller or larger on current models.
- **Think2 and Meta-R1 numbers.** Two 8B models and authors' own benchmarks. Directional only.
- **Human-rated trace quality (Think2, 580 pairs).** Rewards style and verbosity.

## 10. Open questions

1. Does "Is it getting me anywhere?" work as a stop-or-switch trigger for a current LLM, against a trace-feature trigger and a fixed budget at equal tokens? No study found (K25).
2. Has post-training removed the Huang effect on 2025-26 frontier models? Need token-matched arms (K26).
3. Which cheap external signals can a general agent get on tasks without tests or tools (unit tests, re-derivation, tool checks, independent sample agreement), and which gate review well?
4. Does the other-person framing and "Wait" cue help on reasoning models, long agent traces and natural (not injected) errors, with a length-matched control?
5. Is there a single trigger that handles both overthinking and underthinking without hurting hard items?
6. Is a separate cheap monitor better than same-model monitoring at equal total tokens, and does it replicate outside the authors' benchmarks?
7. Did Swanson compensation replicate? Any prompt-only version? The original must be read.
8. How much of the human online-vs-offline gap is measure versus task (I2 up to 99.9%)? Does it predict which agent signals to trust?
9. Do token-matched controls erase gains of metacognitive prompting and Plan-and-Solve on current models?
10. Does forced Planning-Monitoring-Evaluation hurt only weak non-reasoning models, or also strong ones on easy tasks?
11. Is a prompted self-question just more thinking tokens, so any gain is compute rather than monitoring?

## 11. Sources

[V] = opened (page or PDF text read). [M] = snippet or secondary summary only.

| Mark | Source | URL |
|---|---|---|
| [M] | Flavell (1979) Metacognition and cognitive monitoring (a01) | https://doi.org/10.1037/0003-066X.34.10.906 |
| [M] | Brown (1978, 1987) (a02) | https://doi.org/10.4324/9780203056899 |
| [M] | Nelson and Narens (1990) Metamemory (a03) | https://doi.org/10.1016/S0079-7421(08)60053-5 |
| [M] | Swanson (1990) (a04, b01, d15; open attempts failed) | https://doi.org/10.1037/0022-0663.82.2.306 |
| [M] | Perkins and Salomon (1989) (a05) | https://doi.org/10.3102/0013189X018001016 |
| [M] | Schraw and Dennison (1994) (a06) | https://doi.org/10.1006/ceps.1994.1033 |
| [M] | Veenman, Van Hout-Wolters, Afflerbach (2006) (a07) | https://doi.org/10.1007/s11409-006-6893-0 |
| [M] | Veenman and colleagues, mixed model (b08) | https://springerlink.bibliotecabuap.elogim.com/content/pdf/10.1007/s11251-004-2274-8.pdf |
| [M] | Mevarech and Kramarski (1997) IMPROVE (a08) | https://doi.org/10.3102/00028312034002365 |
| [V] | Ten meta-analyses summary page: Dent and Koenka, Ohtani and Hisasaka, Muncer, de Boer, Theobald, Higgins, Dignath (a09-a12, b04); secondary page, not the papers | https://globalmetacognition.com/post/metacognition-learning-educational-attainment-evidence-based-on-ten-meta-analyses |
| [V] | Muncer et al. (2021) metacognition and maths meta-analysis (b02, b03, b23, b25) | https://eprints.soton.ac.uk/449631/1/Accepted_Manuscript_Muncer_et_al._2021_.pdf |
| [M] | Dignath and Buttner (2008) (b05) | https://doi.org/10.1007/s11409-008-9029-x |
| [M] | Donker et al. (2014) (b06) | https://www.sciencedirect.com/science/article/pii/S1747938X13000420 |
| [M] | de Boer et al. (2018) (b07) | https://doi.org/10.1016/j.edurev.2018.03.002 |
| [M] | Small metacognitive prompt studies, Engelmann 2021, Klar 2024 (b09) | https://rptel.apsce.net/index.php/RPTEL/article/view/2021-16003 |
| [V] | Kadavath et al. (2022) LMs mostly know what they know (a21) | https://arxiv.org/abs/2207.05221 |
| [V] | Huang et al. (2024) LLMs cannot self-correct reasoning yet (a15, b10, b11, c05, d01) | https://arxiv.org/abs/2310.01798 |
| [V] | Kamoi et al. (2024) When can LLMs correct their own mistakes (a16, b13, c09, d02) | https://arxiv.org/abs/2406.01297 |
| [V] | Tyen et al. (2024) LLMs cannot find reasoning errors (a17, b12, c08) | https://arxiv.org/abs/2311.08516 |
| [V] | Madaan et al. (2023) Self-Refine (a18, c07) | https://arxiv.org/abs/2303.17651 |
| [V] | Shinn et al. (2023) Reflexion (a19, b15, c06) | https://arxiv.org/abs/2303.11366 |
| [V] | Kumar et al. (2024) SCoRe (a20, b14, c12) | https://arxiv.org/abs/2409.12917 |
| [V] | Zhou et al. (2024) Self-Discover (a22) | https://arxiv.org/abs/2402.03620 |
| [V] | Wang et al. (2023) Plan-and-Solve (a23, b21, c11) | https://arxiv.org/abs/2305.04091 |
| [V] | Didolkar et al. (2024) Metacognitive capabilities of LLMs in maths (a13, b22, c21) | https://arxiv.org/abs/2405.12205 |
| [V] | Wang and Zhao (2024) Metacognitive prompting (a14, c10; b20 local file lost) | https://arxiv.org/abs/2308.05342 |
| [V] | Chen et al. (2025) Do not think that much for 2+3 (a24, b19, c15, d06) | https://arxiv.org/abs/2412.21187 |
| [M] | Nezhurina et al. (2025) Alice in Wonderland (a25, title page only) | https://arxiv.org/abs/2406.02061 |
| [V] | Cemri et al. (2025) Why do multi-agent LLM systems fail (b16) | https://arxiv.org/abs/2503.13657 |
| [V] | Tsui, Self-Correction Bench (b17, c13, d05) | https://arxiv.org/abs/2507.02778 |
| [V] | Muennighoff et al. (2025) s1 (b18, c14) | https://arxiv.org/abs/2501.19393 |
| [V] | Zhou et al. (2024) MetaRAG (c01) | https://arxiv.org/abs/2402.11626 |
| [V] | Elenjical, Kavuri, Varma (2026) Think2 (c02, c03, c23) | https://arxiv.org/abs/2602.18806 |
| [V] | Dong et al. (2025) Meta-R1 (c04, c25, d13) | https://arxiv.org/abs/2508.17291 |
| [V] | Wang et al. (2025) Underthinking of o1-like LLMs (c16, d07) | https://arxiv.org/abs/2501.18585 |
| [V] | Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations (c17) | https://arxiv.org/abs/2402.08115 |
| [V] | Stechly, Marquez, Kambhampati (2023) GPT-4 doesn't know it's wrong (c18) | https://arxiv.org/abs/2310.12397 |
| [V] | Valmeekam et al. (2023) Planning abilities of LLMs (c19) | https://arxiv.org/abs/2305.15771 |
| [V] | Kambhampati et al. (2024) LLM-Modulo (c20) | https://arxiv.org/abs/2402.01817 |
| [V] | Olausson et al. (2024) Is self-repair a silver bullet (d03) | https://arxiv.org/abs/2306.09896 |
| [V] | Snell et al. (2024) Scaling test-time compute (d04) | https://arxiv.org/abs/2408.03314 |
| [V] | Hassid et al. (2026) Don't overthink it (d08) | https://arxiv.org/abs/2505.17813 |
| [V] | Ma et al. (2025) Reasoning models can be effective without thinking (d09) | https://arxiv.org/abs/2504.09858 |
| [V] | Yang et al. (2025) DEER (d10) | https://arxiv.org/abs/2504.15895 |
| [V] | Zhang et al. (2025) Reasoning models know when they're right (d11) | https://arxiv.org/abs/2504.05419 |
| [V] | Fu et al. (2025) DeepConf (d12) | https://arxiv.org/abs/2508.15260 |
| [V] | Gou et al. (2024) CRITIC (d14) | https://arxiv.org/abs/2305.11738 |
| [M] | Syntheses c22, c24, c26, d16, d17: agent notes built from the sources above, not independent sources | see source rows above |
