# Process models: deep document

*Subfield D05.02: stages of thinking critically. Key work: Hitchcock (SEP). Purpose: compare the human stage models with our state graph S1 to S9, and collect every LLM study that tests stages, review, revise or stop steps. Built from evidence_a-d.jsonl (a01-a25, b01-b27, c01-c26, d01-d16), claims K01-K29 and critique.md. Evidence ids are cited in brackets. Where critique.md corrected a number, the corrected number is used here.*

## 1. What it is

A process model of critical thinking says that good thinking is a sequence (or cycle) of identifiable stages: notice a problem, define it, suggest solutions, reason out their consequences, test, accept or reject. The best-known version is John Dewey's five-phase analysis (1910, revised 1933). Hitchcock's Stanford Encyclopedia entry (2022) is the standard modern summary and the key work for this subfield. [a01, a05, b01]

Two questions matter for us.

1. Do stages exist and does their order matter? For people, the evidence is conceptual and introspective. There is no randomised test of stage order (0 order-ablation studies in 12 opened sources [a24, b27]).
2. For a language model, which stage-like steps pay off? Here there is real data, mostly 2023 to 2026. The pattern is clear: stages placed before the answer (plan, restate, choose a structure) give small to medium gains. Stages placed after the answer (self-review) give nothing or harm, unless an outside signal (tool, test, label, verifier) drives them. [c23, c22, K04, K05]

Our schema is a code-driven state graph (S0 to S9). This document checks each state against the process-model literature and says what to add, what to test, and what not to add.

## 2. History and theories in depth

### 2.1 Dewey (1910, 1933)

- 1910, How We Think, ch. VI: Dewey analyses "a complete act of thought" from three student-written cases: a clock and train choice (practical deliberation), a ferryboat pole (observation with three rival hypotheses), and soap bubbles on a tumbler (an experiment with shaken and mouth-down tumblers and an ice cup). [a01]
- Five logically distinct steps in 1910: (1) a felt difficulty, (2) its location and definition, (3) a suggested solution, (4) reasoning out the bearings of the suggestion, (5) further observation and experiment that lead to acceptance or rejection. [a01]
- Order is not fixed. Steps 1 and 2 often fuse. Observation sits at both ends, with inference and reasoning in the middle. [a02]
- Dewey claims that locating the difficulty is what separates safeguarded inference from uncontrolled inference. Skipping it makes suggested solutions random. He uses a doctor who latches onto a first diagnosis as the example. No numbers; this is a claim, not a finding. [a03]
- The trained mind judges how far each step should be carried. Too much care is as illogical as too little; prompt action can beat a long-delayed conclusion. This is an early statement of "spend by difficulty". [a04]
- 1933 revision: the list begins with suggestion, then problem, hypothesis, reasoning, testing. Dewey replaced "steps" with "phases" to drop the idea of a fixed sequence. So the 1910 and 1933 editions disagree on what comes first. [a05, b01]
- The process may spiral: the problem is redefined when an obstacle appears (Hitchcock's Transit case: "arrive on time" becomes "reschedule"). [b26]

### 2.2 Hitchcock (SEP, 2022)

- Hitchcock turns Dewey into a checklist of about twelve component events (notice a difficulty, define the problem, draw conclusions, ..., accept a solution the evidence supports). The events can occur in any order, selectively and repeatedly. No count of how people actually order them is given. [a06, b01, b03]
- Two criticisms of Dewey's model: it forces accept-or-reject with no option to suspend judgment, and early commitment to a hypothesis is risky. He advises investigators to postpone even tentative hypotheses until evidence rules out all but one. This is in tension with Dewey, who puts suggestion before testing. No empirical test of the tension exists. [b02]
- Paul (1984) objects that checklists are too mechanical; Hitchcock argues for a more dialectical process on multi-sided issues. [a07, b03]
- The SEP text treats Dewey's phases as a normative analysis. It gives no behavioural test of whether people follow them. [a14]
- Skills and tests: SEP groups abilities (observational, questioning, inferential, experimenting, consulting sources, argument analysis, judging). Cornell Level X has 24 of 76 items on credibility; CCTST has 11 of 34 on inference and 5 of 34 on argument analysis. [a08]
- Generalisability: McPeck (1981) said there are no general thinking skills. Critics (Paul, Siegel, Ennis) showed the strong form fails: general abilities exist, but applying them needs domain knowledge. [b04, a10]

### 2.3 Consensus and skills lists

- Facione (1990) APA Delphi report: 46 experts, six rounds (Feb 1988 to Nov 1989), about 52% philosophers. Core skills: interpretation, analysis, evaluation, inference, explanation, self-regulation. Over 95% consensus on analysis, evaluation, inference as central; over 87% on interpretation, explanation, self-regulation. This is a skill list, not a stage order. [a09, a10]
- Ennis (1962): three dimensions (logical, criterial, pragmatic), 12 aspects. Seen in snippet only. [a23]
- Wallas (1926): preparation, incubation, illumination, verification, a rival staged model of creative thought. Not opened. [a22]

### 2.4 Stage models in online discussion (Community of Inquiry)

- Garrison, Anderson and Archer (2001): the Practical Inquiry model has four phases: triggering event, exploration, integration, resolution. 95 messages in three transcripts (13, 6, 4 students). On the third transcript, agreement 83.33%, Cohen's kappa 0.74 after three coder training sessions. Distribution: trigger 8%, exploration 42%, integration 13%, resolution 4%. [b09, b10]
- Rourke and Kanuka (2009) review (snippet only): exploration 41% to 53% of postings, resolution 1% to 18%. Kanuka et al. 2007 reported 20% at the highest phases. [b12, b11]
- The CoI authors (Akyol et al. 2009) answer that low resolution comes from teaching design, not from the model. [b11]
- Reading for us: stage labels are codable by humans, and groups stall in exploration. Integration and resolution are the stuck points.

### 2.5 Other human process models (context)

- Klahr and Dunbar (1988): discovery as dual-space search (hypothesis space and experiment space). Only a search summary was seen (N = 10 in study 2). Numbers unusable. [b13]
- Kuhn, Cheney and Weinstock (2000): absolutist, multiplist, evaluativist epistemic levels. No verified percentages. [b14]

### 2.6 Where Dewey enters LLM work

- Dewey and Hitchcock are not named in any of the 16 opened LLM prompting papers. The stage structure arrives by other routes: Polya (Llama-Polya, the mechanistic paper, Self-Discover as motivation) and Toulmin (Critical-Questions-of-Thought). [c24, K21]
- Exception: Atomic Reasoner (arXiv 2503.15944) maps its atomic reasoning actions onto Dewey's five steps in an appendix and adds a checker stage with named error types. Per-cell results were garbled in extraction, so no numbers are recorded. [a17]

## 3. Core findings with exact numbers

Status key: established = two or more independent sources; single = one source; contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Dewey stages are a non-fixed cycle with fusion and back-steps | five phases in 1910; "phases" not "steps" in 1933; suggestion first in 1933 | Dewey 1910; Hitchcock SEP [a01, a02, a05, b01, b26] | established (K01) |
| No controlled test that stage order causes better thinking (humans) | 0 order-ablation studies in 12 opened sources | SEP, CoI papers [a14, a24, b27] | established as an absence (K02) |
| Step order inside a reasoning chain is causal for LLMs | GSM8K (text-davinci-002): standard 15.4, CoT 48.5, invalid reasoning 39.5, wrong order 23.1, irrelevant 11.0. Bamboogle F1: CoT 45.2, invalid 39.4, wrong order 33.8 | Wang et al. 2023 [d01] | single (K22) |
| Premise order is causal | deduction: permuting costs over 30 points; GPT-4-turbo 96.5 (forward) vs 82.0 (ratio 0) and 76.0 (ratio 0.5); GPT-3.5-turbo and Gemini 1.0 Pro fall from over 65 to below 25 | Chen et al. 2024 [d02] | single (K22) |
| Plan-then-solve prompting gives a small gain | zero-shot, text-davinci-003, six math sets: CoT 70.4, PS 73.5, PS+ 76.7 (average); GSM8K 56.4 / 57.0 / 59.3; MultiArith 83.8 / 92.2 / 91.8; AQuA 38.9 / 43.9 / 46.0 | Wang et al. 2023 PS [c01, c02] | single (K03) |
| Plan prompt barely cuts missing-step errors | 100 failing GSM8K items: missing-step 12% (CoT) vs 10% (PS); calculation 7% vs 7%; semantic 27% vs 26% | Wang et al. 2023 PS [c01] | single (K03) |
| Intrinsic self-correction does not help, often hurts | GPT-3.5 GSM8K 75.9 / 75.1 / 74.7 (rounds 0/1/2); CSQA 75.8 / 38.1 / 41.8; HotpotQA 26.0 / 25.0 / 25.0. GPT-4 GSM8K 95.5 / 91.5 / 89.0; CSQA 82.0 / 79.5 / 80.0; HotpotQA 49 / 49 / 43. GPT-4-Turbo GSM8K 91.5 to 90.0. Llama-2 GSM8K 62.0 to 36.5, CSQA 64.0 to 36.5 | Huang et al. 2024 [a19, b15, b16, b17] | established (K04) |
| Why it hurts: flips | GPT-3.5 keeps its first GSM8K answer 74.7% of the time; among changes, right-to-wrong exceeds wrong-to-right. GPT-3.5-turbo changes 81.3% of answers more than 6 times in 10 rounds | Huang; Zhang 2025 [c05, d15] | established (K04) |
| Oracle signal helps (CORRECTED) | GPT-3.5 GSM8K 75.9 to 84.3; CSQA 75.8 to 89.7; HotpotQA 26.0 to 29.0. GPT-4 GSM8K 95.5 to 97.5; CSQA 82.0 to 85.5; HotpotQA 49 to 59. (Earlier "75.9 to 95.5" is wrong: 95.5 is GPT-4's plain score) | Huang table 2, critique.md fix 1 [a19, c04] | established (K05) |
| Tool-grounded critique works, self-critique alone does not | CRITIC, ChatGPT: +7.7 F1 over three QA tasks, +7.0 points over three math tasks, 79.2% lower toxicity probability; self-critique alone -0.03 and +2.33 F1; gain over ReAct +5.1 and +8.2 F1 | Gou et al. 2024 [a21, c09] | established (K05, K06) |
| Self-verification is a small gain | Instruct-GPT +2.33% average; arithmetic +1.67% and +2.84%; other reasoning +0.62% and +0.78% (K=5 candidates, 10 verification samples each) | Weng et al. 2023 [c11] | established with K06 |
| Self-Refine helps on preference tasks, not math | dialogue 36.4 to 63.6 (GPT-3.5); sentiment 8.8 to 30.4 (GPT-3.5) and 3.8 to 36.2 (GPT-4); code readability 37.4 to 51.3; math 64.1 to 64.1. "Average +20%" is a headline over mostly preference tasks | Madaan et al. 2023 [b19, c06, c07] | contested (K07) |
| Reflexion: external signal plus stored reflection | ALFWorld +22 points (12 steps); HotPotQA +20; HumanEval +11 (pass@1 91% vs GPT-4 80%) | Shinn et al. 2023 [c08] | single (K08) |
| Independent verification questions cut hallucination | Llama 65B, Wikidata lists: precision 0.17 to 0.36; hallucinated answers per question 2.95 to 0.68; correct answers 0.59 to 0.38 (some true answers lost) | Dhuliawala et al. 2023 [c10] | single |
| Sound verifier + resampling matches critique at less cost | GPT-4, Game of 24 (100 instances): standard 5%, LLM+LLM critique 3%, sound-verifier binary feedback 36%, first-error feedback 38%, resampling k=15 28%, k=25 42%, self-consistency over 15 6% | Stechly et al. 2024 [d03] | single (K23) |
| Finding the error is the bottleneck, fixing it is easy | BIG-Bench Mistake, 2,186 CoT traces (PaLM 2): best direct step-level finding by GPT-4, overall accuracy 52.87; backtracking is net-positive with a location classifier at about 65% accuracy; revising correct traces costs accuracy | Tyen et al. 2024 [d04] | single (K24) |
| Correction gain needs base accuracy | CriticBench: 5 domains, 15 datasets, 17 LLMs; in math, correction gains appear only above about 41% direct accuracy; logic tasks more correctable | Lin et al. 2024 [b20, c13] | single (K13); not reproduced on newer models |
| Self-correction blind spot in non-reasoning models | 14 open non-reasoning models: average blind spot 64.5%; Claude 3.5 Haiku 52.5%, Sonnet 4 41.4%; non-math logic 62.8%. Appending "Wait" cuts the blind spot by 89%. Qwen3-14B 0.117 to 0.868 vs 0.843 in reasoning mode. Reasoning models show no gap | Tsui 2026 [d05] | single (K25) |
| Cognitive behaviours predict gain from RL | Countdown, RL: Qwen-2.5-3B about 60% vs Llama-3.2-3B about 30%; priming Llama with verification, backtracking, subgoal setting and backward chaining matches Qwen; empty or length-matched placeholder thinking stays at 30 to 35%; priming on incorrect solutions still works | Gandhi et al. 2025 [d06] | single (K25) |
| Self-chosen structures help | Self-Discover BBH: PaLM 2-L 56 / CoT 60 / PS 61 / SD 67; GPT-4 58 / 75 / 73 / 81. T4D: PaLM 2-L 30 / 40 / 42 / 69; GPT-4 51 / 52 / 53 / 85. MATH: PaLM 2-L 45 / 42 / 49 / 50.5; GPT-4 70.5 / 71 / 70 / 73. Beats direct on 23 of 25 tasks. "+39%" is vs direct on T4D; vs CoT it is +29 | Zhou et al. 2024 [b21, c18] | single (K09) |
| Model-chosen order of cognitive operations | GSM8K, hybrid with few-shot CoT about 95% on Llama 3.1 70B; commonest self-chosen order GC-DC-PR (goal clarification, decomposition, pattern recognition); larger gains for mid-size models | Kramer and Baumann 2024 [a18, c03] | established (K10), but all vs CoT |
| Critical-question checklist | MT-Bench (LLM judge 1 to 10): +4.61% reasoning, +5.4% math over other approaches; best in 18 of 20 comparisons (2 domains, 5 models), joint best in 1; Llama 3.1 70B reasoning 8.05 to 8.4, math 8.95 to 9.55; Nemotron-51b reasoning 6.75 to 7.3; Claude 3.5 Sonnet tied CoT on math; Nemotron lost to CoT on reasoning | Castagna et al. 2024 [b24, c19] | single (K11) |
| CQoT loop rule | need 7 of 8 "yes" for the first five loops, then 5 of 8, proceed after ten loops | CQoT [c20] | single |
| Overthinking on missing premises | QwQ-32B and R1: about 1,000 tokens on well-posed GSM8K vs over 3,000 on missing-premise; non-reasoning models about 200 either way; effect spreads by distillation | Fan et al. 2025 [b22, b23] | single (K12) |
| Overthinking on trivial items | for 2+3, o1-like models used 1,953% more tokens and gave 13 solutions; first round holds the correct answer in over 92% of cases (QwQ, R1, ASDIV, MATH500) | Chen et al. 2025 [d09] | single |
| Stop rules work | DEER: length cut 19.1% to 80.1%, accuracy +0.3 to +5.0 (11 models, 10 benchmarks); R1-Distill-Qwen-7B 64.2 to 69.2 at 61.5% of tokens; Qwen3-14B 82.8 to 83.7 at 57.1%; QwQ-32B 82.6 to 84.0. Answer convergence: final answer reached by about 60% of steps; tokens cut over 40% on NaturalQuestions; Learn-to-Stop cut 46.2% (R1-Qwen-7B) and 47.7% (32B) | Yang 2025; Liu and Wang 2025 [d07, d08] | established (K26) |
| Asking the right clarifying question is hard | QuestBench: 40 to 50% on Logic-Q and Planning-Q; over 80% on GSM-Q and GSME-Q (GPT-4o 84.05% and 99.39%); chain of thought and few-shot gave no significant gain | Li et al. 2025 [d10] | single (K27) |
| Review vs resample depends on difficulty | compute-optimal allocation beats best-of-N with about 4x less compute; easy items gain from sequential revision, hard items need parallel sampling or tree search | Snell et al. 2024 [d14] | single (K29) |
| LLM judge on preference matches humans; on error location needs reasoning models | MT-Bench non-tie: GPT-4 vs human 85%, human vs human 81%. ProcessBench (3,400 cases): F1 o1-mini 87.9, GPT-4o 61.9 | Zheng 2023; ProcessBench 2025 [d12, d13] | single (K28) |
| Humans follow a wrong LLM | N = 24, 15 modified Watson-Glaser items, within subject, LLM text 42 to 150 words. LLM wrong: humans correct 24.5% (short), 54.2% (medium), 30.7% (long). LLM right: 71.5%, 81.1%, 79.5% | Friedman et al. 2026 [a15, c16] | single (K18) |
| LLM scoring of critical-thinking essays is mediocre | 4,115 essays, 500 human-coded; human weighted kappa up to 0.87; fine-tuned Llama 3.1 8B accuracy .604, alpha .606, RMSE .933; ModernBERT .563; GPT-5 zero-shot .543, few-shot .532 | Peczuh et al. 2025 [a16, c17] | single (K19) |
| Stage-tuned models follow stages | Llama-Polya: stage-protocol error 0.0% (polya-v2) vs 0.4% (metamath); base and instruct skip stages and answer in one turn. Measures adherence, not accuracy | Lee et al. 2026 [c15] | single (K20) |
| Reasoning operations are separable in hidden states | spans labelled by GPT-5; 7 humans checked 84 spans: majority agreement 81 of 84 (96.4%, Fleiss kappa 0.666); GPT-5 matched the human majority on 64 (76.2%, kappa 0.715) | Jeong et al. 2026 [c14] | single |
| Critical-thinking teaching works a little (humans) | g+ = 0.30 over 341 effects (867 studies screened, 1930 to 2009); content-specific g = 0.57 (97); dispositions 0.23 (25); subject learning 0.33 (140); by approach mixed 0.38, general 0.26, infusion 0.29, immersion 0.23; dialogue + anchored + mentoring 0.57 (19); teacher questions 0.38 (19); whole-class discussion 0.42 (16); small groups 0.41 (14); problem solving 0.35 (31); role play 0.61 (5) | Abrami et al. 2015 [a11, a12, b05, b06, b08] | established (K14) |
| College gains | about 0.6 SD over four years (50th to 72nd percentile), 71 reports over 48 years, nonlinear, no clear major differences; specific CT instruction added little | Huber and Kuncel 2016 [b07] | single (K15) |
| Glaser 1941 | 10 weeks of instruction improved Watson-Glaser scores more than standard English teaching | SEP [a13, b08] | single, historical |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

### 4.1 Dewey cycle as a state machine

States: DIFFICULTY, DEFINE, SUGGEST, REASON, TEST, ACCEPT. Edges: forward edges between neighbours, fusion of DIFFICULTY and DEFINE, and back-edges from TEST to DEFINE (redefine the problem) and from TEST to SUGGEST (next hypothesis). Hitchcock's version drops edge order entirely: a set of events that may occur in any order, repeatedly. Implementation: represent the stage list as a set plus a transition table; allow any back-edge, but let code, not the model, trigger it. [b01, b03, b26]

Mapping to our graph: DIFFICULTY and DEFINE are S1 (UNDERSTAND) and S2 (REPRESENT); SUGGEST is S3 (GENERATE); REASON is the model's work inside S3 and S5; TEST is S4 and S8; ACCEPT is S7; the redefinition spiral is S5 to S6 to S1/S2. S0 (gate), S6 (impasse operators) and S9 (look back) have no Dewey counterpart; S9 corresponds to Reflexion and Polya's "look back". Gaps against the Facione six skills: interpretation (S1 partly) and self-regulation (S0/S6/G-rules) are the thinly covered ones. [K16]

### 4.2 Plan-then-solve (S1/S2 before S3)

Stage 1 prompt: "devise a plan; extract variables and numbers". Stage 2: "carry out the plan; compute intermediate results; mind calculation". PS+ adds the detail instructions. Expected cost: one extra short generation. Gain: about +3 points average on math (70.4 plain, 73.5 PS, 76.7 PS+). Little effect on missing-step errors (12% to 10%). [c01, c02]

### 4.3 Self-composed structure (Self-Discover)

Three meta-prompts: SELECT reasoning modules from a list of atomic modules (including "critical thinking", "break into sub-tasks"); ADAPT them to the task; IMPLEMENT as an explicit step-by-step JSON structure. Then solve by filling the structure. The plan is made once per task type, not per item, which is why it claims 10 to 40x fewer inference calls than self-consistency-style methods. Gains are biggest on tasks that need world-model or social reasoning (T4D) and small on MATH. [b21, c18]

### 4.4 Model-chosen operation order (Cognitive Prompting)

A list of operations (goal clarification, decomposition, pattern recognition, generalisation, integration). Variant 1 gives a fixed order; variant 2 lets the model pick the order. Log the chosen order. On Llama 70B, GC-DC-PR was most common. [a18, c03]

### 4.5 Critical-question gate (CQoT)

Pipeline: (1) the model writes a plan with premises and conclusion; (2) eight Toulmin-based critical questions (data, warrant, backing) are answered yes or no; (3) accept if the yes-count meets the threshold (7 of 8 for loops 1 to 5, then 5 of 8); (4) after 10 loops proceed anyway. This is a bounded loop that never abstains, which fits G6. Judged by an LLM on MT-Bench, so gains of 4 to 5 points are soft. [b24, c19, c20]

### 4.6 Tool-grounded verify-then-revise (CRITIC, Self-Debug, Reflexion)

Loop: draft; call an external tool (search, code interpreter, unit tests, toxicity API) on the draft; feed the tool output to the model; revise. Reflexion adds: write a verbal reflection after a failed trial, store it, retry with it in context. The gain comes from the tool output. Implementation rule: the revise prompt must contain the tool's actual output. [a21, c08, c09, K05]

### 4.7 Independent verification (Chain-of-Verification, backward verification)

CoVe: draft; plan verification questions; answer them in a fresh context that does not see the draft; write the final answer. Independence of the verify step is the point. Backward verification: mask a condition in the problem, insert the candidate answer, ask the model to recover the condition, rank candidates by match. [c10, c11]

### 4.8 Split review into locate and fix

Output of the review stage: either "no error" or the first wrong step number. Revise only from the located step. Even a roughly 65%-accurate locator makes backtracking net-positive; reviewing correct traces loses accuracy, so the "no error" output matters. [d04]

### 4.9 Equal-compute reviewer vs sampler

k independent samples plus a sound verifier is the strong baseline. At fixed compute, route by difficulty: sequential revision for easy to medium, parallel sampling or search for hard (Snell). [d03, d14]

### 4.10 Stop rules

- Confidence-gated early exit (DEER): at reasoning-transition tokens ("Wait", "Alternatively"), force a trial answer and measure the model's confidence in it; stop if above threshold.
- Answer repetition: stop when k consecutive trial answers are identical; final answers appear by about 60% of steps.
- Trained probe for the stop signal (Learn-to-Stop).
- Rule of thumb: the first solution is correct in over 92% of cases on easy sets, so on easy items stop at once. [d07, d08, d09]

### 4.11 Re-entry cue for non-reasoning models

Append a single word ("Wait") after the model's first answer to trigger review. This lifted Qwen3-14B from 0.117 to 0.868 on the blind-spot benchmark, near its reasoning-mode 0.843. The model fixes an injected error when it is in the user turn but not when it sits in its own turn. [d05]

### 4.12 Premise check

For underspecified items, add a "what is missing" step with a checked output (does the problem give all quantities needed). QuestBench shows models solve fully specified problems but pick the right missing variable only 40 to 50% of the time in logic and planning. No study shows a define stage fixing this; chain of thought did not. So this step is a hypothesis only. [d10, b22, K27]

## 5. What holds up

### 5.1 Established

- Stage lists in the literature are conceptual. Dewey is explicit that order is not fixed; Hitchcock turns it into an any-order checklist. Do not build a rigid forward-only pipeline on Dewey's authority. [K01]
- No randomised test of human stage order exists. Claims that "defining the problem first" helps are claims. [K02]
- Intrinsic self-correction fails across GPT-3.5, GPT-4, GPT-4-Turbo and Llama-2, and across Huang, Kamoi's survey, CRITIC's ablation, Self-Refine's math row, Stechly and Zhang. Three or more independent groups. [K04, K06]
- Correction works with an external signal: oracle label (+8.4 for GPT-3.5 on GSM8K, not +19.6), tools (CRITIC), tests (Self-Debug, up to +12 points per the gap search), sound verifier (Stechly). [K05]
- Stop rules that use trial-answer agreement or confidence cut tokens 19% to 80% with accuracy flat or up, in three independent works. [K26]
- Order inside a chain matters causally for LLMs: wrong step order dropped GSM8K from 48.5 to 23.1; premise order cost over 30 points. Validity of steps mattered less (39.5). [K22]

### 5.2 Moderators and boundary conditions

- Task type: Self-Refine gains are large on preference-judged tasks and zero on math. Caveat: the gains are scored by model-based metrics; GPT-4 preference agreed with humans only 82% (sentiment), 68% (acronym), 71% (dialogue). [b19, K07]
- Base accuracy: critique-correction in math shows gains only above about 41% direct accuracy (CriticBench, one source, older models). [K13]
- Difficulty: sequential revision is better on easy to medium items, parallel sampling on hard items. [K29]
- Model class: reasoning models show no self-correction blind spot; non-reasoning models average 64.5%; a one-word cue closes most of it. Review scaffolds are probably redundant on reasoning models. [K25]
- Model size: Cognitive Prompting gains were larger for mid-size models; stronger GPT-4 degraded less under self-correction but still degraded. [a18, b16]
- Prompt wording: GPT-4-Turbo on CSQA ranged 74.5 to 83.5 across feedback prompts. Huang argues part of Self-Refine's gain comes from weak initial prompts. [b17]
- Oracle-stop confound: earlier positive papers used the true label to decide when to stop. Without it, results vanish. [a19]

### 5.3 Failures, contradictions and corrections

- Huang vs Self-Refine: reconciled by task type and prompt design, still marked contested. [critique.md]
- "Oracle lifts GPT-3.5 GSM8K from 75.9 to 95.5" in evidence a25 and c04 is wrong. The correct row is 84.3. 95.5 is GPT-4's plain score. Do not copy a25 or c04 numbers.
- Self-Refine "average +20%" must not be quoted as a general effect; per-task range is 0 (math) to +32 (sentiment).
- Self-Discover "+39%" is vs direct on T4D (30 to 69); vs CoT it is +29.
- Friedman 2026: long-output, LLM-correct accuracy is 79.5% (CI .542 to .927), not 81%; 81.1% is medium.
- Hitchcock vs Dewey: postpone hypotheses vs suggest early. Untested.
- Dewey 1910 vs 1933 start with different phases. Edition choice changes what "S1" means.
- CQoT: one model (Nemotron-51b) lost to CoT on reasoning; Claude 3.5 Sonnet only tied on math. Judge is an LLM. [b24]
- Human CoI studies: resolution reached rarely (4% in one study, 1 to 18% across reviews). The CoI authors blame task design. [b10, b11]

### 5.4 Interventions that worked

- Tool or test in the loop (CRITIC +7.7 F1 QA and +7.0 math; Reflexion +22, +20, +11).
- Pre-answer structure (Self-Discover T4D 30 to 69 and 51 to 85; PS+ +6.3 average over CoT).
- Independent verification contexts (CoVe precision 0.17 to 0.36).
- Early-exit stop rules (DEER).
- Wait cue on non-reasoning models (0.117 to 0.868).
- Human teaching: mixed explicit-principle plus application instruction; dialogue + anchored + mentoring 0.57. [b06]

### 5.5 Interventions that did not work

- Open-ended self-review without signal (all of 5.1).
- Chain of thought for clarifying-question selection (QuestBench).
- Extra reasoning tokens for finding a missing premise (Fan).
- LLM-as-critic locating errors with non-reasoning models (GPT-4 52.87 overall on BIG-Bench Mistake; GPT-4o 61.9 F1 on ProcessBench).
- LLM self-critique in Game of 24: 3% vs 5% plain.
- Plan prompt on missing-step errors (12% to 10%).

## 6. Language models

### 6.1 Behaviour on stage tasks

- Plain models skip stages. Generic Llama variants "bypass stages and answer in one turn" in tutoring dialogues; a Polya-tuned 8B follows the protocol (0.0% stage error). That fixes adherence; no accuracy gain was reported. [c15]
- Reasoning text shows operation structure. Operations grouped by Polya stage (understanding, planning, execution, look back) are separable in hidden states, and span labelling by GPT-5 agrees with humans (76.2% match to majority, kappa 0.715). This hints that reasoning models already contain stages internally. [c14]
- Gandhi et al. find four behaviours (verification, backtracking, subgoal setting, backward chaining) predict who gains from RL. They are the same operations our schema runs by code. Priming a weak model with them closes the gap (about 30% to the 60% of the stronger family); placeholder tokens do not. [d06]

### 6.2 Review and revise

- Pre-2025 non-reasoning models: self-correction without signal is zero to strongly negative (GPT-3.5 CSQA 75.8 to 41.8; Llama-2 GSM8K 62.0 to 36.5). Right-to-wrong flips exceed wrong-to-right. [a19, b17, c05]
- Instability: GPT-3.5-turbo changes 81.3% of answers more than 6 times in 10 rounds; "Are you sure" prompts bias the model to change. [d15]
- Blind spot: 64.5% average across 14 non-reasoning models; models fix identical errors if the error is in the user turn. [d05]
- Reasoning models: no blind spot. Scaffold effect is likely small or negative. [d05, K25]
- With signal: oracle +8.4 to +10 points; tool +7.7 F1; tests up to +12 points. [K05]
- Locating errors is the bottleneck. Best non-reasoning critic: 52.87 overall; o1-mini F1 87.9 vs GPT-4o 61.9. [d04, d13]
- Review vs more samples at equal compute: with a sound verifier, resampling k=25 reaches 42% vs critique 36 to 38% on Game of 24. Self-consistency over 15 got only 6% there (voting fails when the answer space is large). [d03]

### 6.3 Before-answer structure

- Plan-and-Solve +3.1 average (text-davinci-003). Self-Discover +7 (PaLM 2-L) and +23 (GPT-4) BBH points over direct. Cognitive Prompting about 95% on Llama 70B GSM8K (hybrid). All compared with zero-shot or CoT, not equal-token best-of-N. [c21]
- On MATH the gain over CoT is +1.5 to +3 for Self-Discover. Structure matters more on social and world-model tasks. [c18]
- CQoT: +4.6 and +5.4 on LLM-judged MT-Bench; a small model can beat a bigger baseline on one task. [c19, c20]

### 6.4 Stop and overthink

- Reasoning models overthink trivial and ill-posed items: over 3,000 vs about 1,000 tokens on missing-premise; 1,953% more tokens on 2+3. Non-reasoning models stay near 200 tokens and are less affected. [b22, d09]
- Early exit cut length 19% to 80% with accuracy +0.3 to +5.0. [d07]

### 6.5 Judges

- Preference: GPT-4 vs human 85%, human vs human 81%. Process-quality or stage-adherence judging has no published validation. Critical-thinking essay scoring: GPT-5 zero-shot .543 vs fine-tuned 8B .604. [d12, a16, K28]
- Humans reading LLM text follow it: when the LLM is wrong, only 24.5% to 54.2% are correct. [a15]

### 6.6 Not found

No model scores on Watson-Glaser, CCTST, Cornell or Halpern tests by subskill (searches blocked or empty). No stage-order ablation for LLM agents. [c25, critique gap 7]

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Revise only from located real output, never from the model's own opinion.** G2, S5. [E] K04, K05, K06. Evidence a19, b15, b16, b17, c09, c22, d03, d15. Already in G2; this adds the numbers.
2. **Gate the revise step on an external check** (tool call, unit test, sound verifier, held-out example). S4, S5, S8, G3. [E] K05. Evidence a21, c09, c08, d03, d04. Oracle gain +8 to +10 points; tools +7 to +8; none without them.
3. **Keep the state graph non-rigid: allow back-edges, and let the program trigger them.** Graph edges (S5 to S6 to S1/S2 exist). [E] K01. Evidence a01, a02, a05, b01, b26. Do not cite Dewey as proof that order helps (K02, K21).
4. **Add a stop rule for the test stage: stop after k identical trial answers or a high-confidence trial answer; on easy items stop after the first pass.** G11, S4/S8 exit. [E] K26. Evidence d07, d08, d09. Cuts tokens 19% to 80%.
5. **Log right-to-wrong and wrong-to-right flips for every doubt step.** Section 6 of the schema. [E] K04. Evidence c05, d15.
6. **Keep free self-reflection, a generic "check your answer" step and a model-as-critic out (section 4b).** [E] K04, K06. Evidence c22. Adds the numbers in section 3 to the existing 4b rows.
7. **Never quote Self-Refine's 20% or the a25/c04 oracle numbers.** [E] critique.md fixes.

### Test first

8. **Define-stage ablation (skip vs run) at equal tokens, on clean and underspecified items.** S1, S2. [S] K03, K27. Evidence a03, c01, c02, d10, b22. Dewey claims it matters; the LLM data is +3.1 points, and CoT does not help missing information.
9. **Stage-order permutation of S3 to S8, and skip tests.** Graph order. [S] K22 (chain order matters), K02. Evidence d01, d02. Only our bench can answer it.
10. **Locate-and-fix review output** ("no error" or step index) that protects correct traces. S5, S8. [S] K24. Evidence d04.
11. **Router: sequential revise on easy to medium items, k independent samples plus verifier on hard.** S0 gate, G12. [S] K29, K23. Evidence d14, d03.
12. **Self-composed stage plan per task type vs a fixed plan; log self-chosen operator order.** S0, O1 to O8 ordering. [S] K09, K10. Evidence b21, c18, a18, c03. Expect little on math (+1.5 to +3).
13. **"Wait" re-entry cue on non-reasoning models; scaffold on/off per model class.** S8. [S] K25. Evidence d05, d06.
14. **Critical-question (Toulmin) review with a loop cap and "proceed anyway" at 10 loops.** S8, G6. [S] K11. Evidence b24, c19, c20. Gains are LLM-judged.
15. **Retry with a stored reflection only after an external failure signal.** S9, memory. [S] K08. Evidence c08, c26.
16. **Premise-check step with a checked output for underspecified items.** S1. [S] K12, K27. Evidence b22, d10.
17. **Gate review on first-pass signal (41% threshold).** S0/S8. [S] K13. Evidence b20, c13. Re-measure on current models.
18. **Forced integrate step when the agent stalls (attempts without selection).** S6, S7. [S] K17. Evidence b09, b10, b11, b12. Human-only evidence.
19. **Answer presentation: test whether length and justification change a judge's error detection.** G5 judge design. [S] K18. Evidence a15, c16. Human evidence only.
20. **Validate any stage-adherence judge on 100 human-labelled traces before use.** Section 6 logging. [S] K28, K19, K20. Evidence d12, d13, a16, c15.

## 8. Concrete tests on our bench

All arms use equal tokens (cap per item; setup cost counted, G7). Report accuracy, right-to-wrong flips, wrong-to-right flips, tokens and stage path.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items with a check (ARC-like programs, math with an answer) | (a) review loop with the model's own critique; (b) review loop with failing output located by code; (c) same tokens as k independent samples plus the check | accuracy; flips | (b) and (c) beat (a); (a) at or below plain; (b) vs (c) decided by difficulty |
| T2 | 100 clean and 100 missing-premise math/logic items | (a) define stage on; (b) skipped, with the saved tokens given to a second attempt | accuracy on clean; flag rate on missing-premise; tokens | small gain on clean (+1 to +3); larger on flag rate only if the step helps; CoT alone expected to add nothing |
| T3 | Same items | permute order of S3 to S8 (shuffled, reversed, skip S4) vs graph order | accuracy; tokens | big drop if order carries information (compare Wang: 48.5 to 23.1 for chain order); no drop means stages are decorative |
| T4 | Items with a check | review output "no error" or step index vs free-text review | accuracy on already-correct items; net gain on wrong items | loss on correct items falls; net gain only if locator is above about 65% |
| T5 | Easy, medium, hard bins from plain pass rate | always revise vs always resample vs router by difficulty | accuracy per bin; tokens | revise wins easy and medium, resample wins hard (Snell) |
| T6 | Single-answer items | fixed budget vs stop after k = 2 or 3 identical trial answers vs confidence-gated exit | tokens; accuracy | tokens down 20% to 60%, accuracy flat or +0 to +5 |
| T7 | Non-reasoning and reasoning model | scaffold review on/off, plus "Wait" cue only | accuracy; blind-spot rate on injected-error items | cue matches scaffold on base models; scaffold adds nothing on the reasoning model |
| T8 | Open-ended (judged) and math items | critique loop on open items only vs on all items | judged score; math accuracy | gain on open items, none on math |
| T9 | 50 QuestBench-style underspecified items | what-is-missing step with checked output vs plain vs CoT | % correct clarifying question | baseline 40 to 50%; worth keeping if it adds more than 10 points |
| T10 | Mixed items | self-composed stage plan vs fixed plan vs plain CoT | accuracy; tokens | +10 or more on world-model items, +1 to +3 on MATH-type |
| T11 | 100 human-labelled traces | stage-adherence judge vs human labels | kappa | acceptable if kappa above 0.6 (Peczuh alpha .606 is the reference) |

## 9. What does not transfer, and why

- Human teaching meta-analyses (Abrami g+ 0.30, Huber and Kuncel 0.6 SD): they measure students, not process order. An agent is not "taught" in the same sense; the closest analogue is explicit instruction plus worked examples. [K14, K15]
- Delphi skill list: a list of what to be good at, not a sequence. Use it for coverage gaps (interpretation, self-regulation), not to order states. [K16]
- CoI phase rates (8% trigger, 42% exploration, 13% integration, 4% resolution): group chats, not one thinker. The stall pattern may map to our attempts-without-selection stall, but this is a loose analogy. [K17]
- Humans following LLM text (Friedman, N = 24): about how people judge models, not how models think. Useful only for answer presentation. [K18]
- 2023-vintage evidence (GPT-3.5, text-davinci-003, PaLM 2, Llama-2): most review-stage numbers come from models weaker than ours and without reasoning mode. Reasoning models have no blind spot (d05) and overthink (d09, b22). Numbers will not carry over unchanged.
- Preference-task gains (Self-Refine, CQoT): scored by model judges, which favour longer, more polished text (G5). Not evidence for correctness gains.
- Cognitive Prompting, Self-Discover and Plan-and-Solve gains: measured against zero-shot or CoT, not equal-token best-of-N. Not proof they beat sampling.
- Dewey's "test" phase assumes experiment on the world. For single-answer questions our S4/S8 test is a code check, closer to program repair than to Dewey's inquiry.
- Dewey's felt difficulty and hypothesis spiral fit open inquiry, not exam-like items. Our no-check and direct modes should skip most stages (G11).
- Klahr and Dunbar and Kuhn numbers could not be verified; do not transfer.

## 10. Open questions

1. Does the order or presence of stages change accuracy at equal tokens for current models? No direct study; T3 answers it.
2. Does a define stage help on underspecified or adversarial items? T2, T9.
3. Which review step survives equal-token comparison with k samples on current reasoning models? T1, T7.
4. How much of the oracle gain does a cheap gate recover? T4; no single study measures the share.
5. Is the 41% base-accuracy threshold for correction reproducible on newer models? Not found. Tyen's 65% locator accuracy and Self-Correction Bench give related but different thresholds.
6. Do reasoning models already do Dewey-like back-steps internally, so explicit stages are redundant? Direction is yes (d05, c14); no scaffold on/off test yet.
7. Can a stop rule work at stage level inside a Dewey-stage agent? DEER works inside one chain; stage-level stopping is untested.
8. How reliable is a judge of stage adherence? None validated; Peczuh .54 to .60.
9. Human premature-closure and stage-skipping numbers (Klahr and Dunbar, Kuhn): publisher PDFs could not be retrieved.
10. LLM scores on Watson-Glaser, CCTST and Cornell by subskill: not found.
11. Does postponing hypotheses (Hitchcock) beat early suggestion (Dewey) for an LLM generator? Untested; relates to anchoring in S3.

## 11. Sources

[V] = opened and read; [M] = snippet or summary only.

- [V] Dewey (1910) How We Think. https://www.gutenberg.org/cache/epub/37423/pg37423.txt
- [V] Hitchcock (2022) Critical Thinking, SEP. https://plato.stanford.edu/entries/critical-thinking/
- [V] Hitchcock, SEP methods supplement. https://plato.stanford.edu/entries/critical-thinking/methods.html
- [V] Facione (1990) APA Delphi Report. https://www.qcc.cuny.edu/socialSciences/ppecorino/CT-Expert-Report.pdf
- [V] Abrami et al. (2015) meta-analysis. https://www.clearinghouse.edu.tum.de/wp-content/uploads/2023/12/CHU_KR18_ENG_Abrami_2015.pdf
- [V] Huber and Kuncel (2016) via AERA snapshot. https://www.aera.net/Newsroom/Study-Snapshot-Does-College-Teach-Critical-Thinking
- [V] Garrison, Anderson and Archer (2001). https://www.newdemocracy.com.au/wp-content/uploads/2020/05/Garrison-Anderson-Archer-2001.pdf
- [V] Akyol et al. (2009) response to Rourke and Kanuka. https://ijede.ca/index.php/jde/article/download/630/884
- [M] Rourke and Kanuka (2009). https://www.ijede.ca/index.php/jde/article/view/630
- [M] Klahr and Dunbar (1988). https://doi.org/10.1207/s15516709cog1201_1
- [M] Kuhn, Cheney and Weinstock (2000). https://www.educationforthinking.org/sites/default/files/pdf/03-02DevelopmentOfEpistemology.pdf
- [M] Wallas (1926). https://en.wikipedia.org/wiki/Four-stage_model_of_creativity
- [M] Ennis (1962). https://www.jstor.org/stable/1169209
- [V] Friedman et al. (2026) Not Too Short, Not Too Long. https://arxiv.org/pdf/2603.06878
- [V] Peczuh et al. (2025) automated assessment of critical thinking subskills. https://arxiv.org/pdf/2510.12915
- [V] Atomic Reasoner (2025). https://arxiv.org/pdf/2503.15944
- [V] Kramer and Baumann (2024) Cognitive Prompting. https://arxiv.org/pdf/2410.02953
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/pdf/2310.01798
- [V] Li, Yang, Ettinger (2024) When hindsight is not 20/20. https://arxiv.org/pdf/2404.09129
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes. https://arxiv.org/abs/2406.01297
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Lin et al. (2024) CriticBench. https://arxiv.org/abs/2402.14809
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620
- [V] Fan et al. (2025) Missing premise exacerbates overthinking. https://arxiv.org/abs/2504.06514
- [V] Castagna, Sassoon and Parsons (2024) Critical-Questions-of-Thought. https://arxiv.org/abs/2412.15177
- [V] Wang et al. (2023) Plan-and-Solve. https://arxiv.org/abs/2305.04091
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Dhuliawala et al. (2023) Chain-of-Verification. https://arxiv.org/abs/2309.11495
- [V] Weng et al. (2023) Self-verification. https://arxiv.org/abs/2212.09561
- [V] Jeong et al. (2026) mechanistic study of CoT stages (id as recorded in evidence c14; check before citing). https://arxiv.org/abs/2609.04753
- [V] Lee et al. (2026) Llama-Polya. https://arxiv.org/abs/2602.10597
- [V] Wang et al. (2023) Towards understanding chain-of-thought prompting. https://arxiv.org/abs/2212.10001
- [V] Chen et al. (2024) Premise order matters. https://arxiv.org/abs/2402.08939
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations. https://arxiv.org/abs/2402.08115
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors but can correct them. https://arxiv.org/abs/2311.08516
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778
- [V] Gandhi et al. (2025) Cognitive behaviors that enable self-improving reasoners. https://arxiv.org/abs/2503.01307
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895
- [V] Liu and Wang (2025) Answer convergence. https://arxiv.org/abs/2506.02536
- [V] Chen et al. (2025) Overthinking of o1-like models. https://arxiv.org/abs/2412.21187
- [V] Li, Kim, Wang (2025) QuestBench. https://arxiv.org/abs/2503.22674
- [V] Zheng et al. (2023) LLM-as-a-judge. https://arxiv.org/abs/2306.05685
- [V] Zheng, Zhang et al. (2025) ProcessBench. https://arxiv.org/abs/2412.06559
- [V] Snell et al. (2024) Scaling test-time compute. https://arxiv.org/abs/2408.03314
- [V] Zhang et al. (2025) Dark side of intrinsic self-correction. https://arxiv.org/abs/2412.14959
- [M] Self-Debug: cited only for "up to +12 points with tests" as stated in critique.md; no separate evidence line.
