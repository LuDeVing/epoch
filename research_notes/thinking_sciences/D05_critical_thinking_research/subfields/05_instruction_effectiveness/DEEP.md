# Instruction effectiveness: deep document

*Subfield D05.05. Written from evidence_a-d.jsonl (ids a01-a25, b01-b27, c01-c25, d01-d19), claims.jsonl (K01-K36) and critique.md in this folder. Statuses: established = two or more independent sources; single-source; contested. Numbers marked "secondary" come from a summary of the paper, not the paper.*

## 1. What it is

This subfield asks one question: which teaching methods raise thinking performance, and by how much?

Two literatures answer it.

- **Human instruction research.** Meta-analyses of classroom studies (Abrami 2008, 2015; Huber and Kuncel 2016; Alfieri 2011; Barbieri 2023). Outcome: scores on standard critical-thinking tests, or maths performance.
- **LLM "instruction" research.** What happens when a model is shown worked solutions, told to reason step by step, asked to critique itself, argue with copies of itself, or read lessons from past failures. Outcome: benchmark accuracy. This is the machine analogue of teaching methods. Plus a newer strand where an LLM is the teacher (Kestin 2025, Bastani 2025).

Why it matters for our agent. Our agent is a scaffold around one model. The scaffold is a form of instruction: it tells the model what to do, in what order, with what examples and what feedback. The evidence says which of those levers carry weight, which are noise, and which do harm. Guardrail G7 (every element must pay for itself at equal tokens) is the rule this evidence supports most.

Three points frame everything below.

1. A single instructional lever is worth little. In humans about 0.3 SD (a01, b01, b02).
2. The baseline decides the result. Weak control groups and weak baseline prompts inflate gains (b03, b09, b24).
3. In LLMs the lever needs a capable model, a suitable task type, and an outside signal. Without these it does nothing or hurts (b08, b14, d02).

Our agent is the learner or solver, not the tutor. Tutor evidence (Kestin, Bastani, MathDial) is only indirect for us.

## 2. History and theories in depth

**Worked examples and cognitive load (1985 on).** Sweller and Cooper (1985) ran the founding algebra experiments. Studying solved examples replaced part of problem solving and gave faster learning (a21; not opened, from memory only). The theory: novices have limited working memory, and searching for a solution uses it up. A worked example removes the search. Later work found an expertise reversal effect: the help stops paying, or hurts, once the learner can do the steps (cited from the field; Kalyuga numbers not opened). See the working-memory and cognitive-load documents in the A-series folders; not repeated here.

**The guidance debate (2006, 2011).** Kirschner, Sweller and Clark (2006) argued that minimal guidance does not work for novices (a22, b18; not opened). Inquiry researchers contested this. Alfieri et al. (2011) tested it with two meta-analyses and settled most of it (d15, d16; opened in full). Unassisted discovery loses to explicit instruction. Guided discovery wins. Guided discovery equals worked examples. So the real line is not "discovery vs telling" but "unassisted vs assisted". (Scaffolding and guided discovery is a parallel subfield; only the headline is used here.)

**Critical thinking as a teachable skill (2008, 2015).** Abrami et al. (2008) pooled 117 studies, 161 effects, mean g+ 0.341 (b01). The 2015 update pooled 341 effect sizes, mean 0.30 (a01, a07, b02). Their framework: dialogue, authentic (anchored) problems, and mentoring. They argue that explicit teaching of CT principles, then application to content, works best (a05). Huber and Kuncel (2016) pointed the other way: CT rises over a normal college career (about the 50th to 72nd percentile over four years), and programs aimed at CT added nothing long-term (a08). This conflict is not resolved (K29, contested).

**Prompting as instruction (2021 on).** In-context learning made the human analogy literal. Liu 2021 and Rubin 2021 showed that which examples you show matters (c20, c21). Min 2022 showed that format matters more than label correctness (b12). Wei 2022 showed worked solutions with steps lift a large model sharply (a11). Kojima 2022 showed a bare cue is enough for a smaller lift (b07). Zhou 2022 added sequenced easy-to-hard teaching (c07, c08). Lampinen 2022 added explanations on examples (b13).

**Dialogue and feedback as instruction (2023 on).** Du 2023 turned "dialogue" into multi-agent debate (a13). Reflexion and ExpeL turned feedback and mentoring into lesson memory (c18, c19, d10). Huang 2024 and Zhang 2025 then ran the controls and cut most of this back (b08-b10, d04-d06).

**LLM as tutor (2023 on).** MathDial found strong solvers are poor tutors (c15). Kestin 2025 and Bastani 2025 gave randomized human trials with opposite headlines. The difference is design: structured prompts with solutions help, free access harms later unaided performance (a15, d17).

**Reasoning-model era (2025).** Models that think by default shift the picture. Step-by-step cues add little (d02). Pasted worked solutions hurt (d12, d14). This is the LLM expertise reversal effect (K31).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| CT instruction in humans, overall | g+ 0.341 (117 studies, 161 effects, N 20,698, SD 0.610, Q 1,767.86). 2015: g 0.30 over 341 effect sizes. About 60% chance a treated student beats a control. | Abrami 2008, 2015 (b01, a01, b02) | Established (2 sources); 2015 secondary summary only |
| Outcome type moderates | Content-specific CT g 0.57 (97 studies); generic 0.30; dispositions 0.23 (25); subject facts 0.33 (140) | Abrami 2015 (a02) | Single-source, secondary |
| Strategy combination | Dialogue + authentic problems + mentoring g 0.57 (19 studies). Teacher questions 0.38 (19); whole-class discussion 0.42 (16); small group 0.41 (14); problem solving 0.35 (31); role play 0.61 (5) | Abrami 2015 (a03, a04) | Single-source |
| Stand-alone vs infused | No significant difference. Explicit principles then application best (exact g not read) | Abrami 2015 (a05) | Single-source |
| Age, subject | 11-15 g 0.37 vs 16-18 g 0.25, ns. STEM vs non-STEM ns | a06 | Single-source |
| College effect without CT programs | 50th to 72nd percentile over 4 years; CT-focused programs no extra long-term gain; 71 reports, 48 years | Huber and Kuncel 2016 (a08) | Contested vs Abrami |
| Non-lecture methods, nursing | Dispositions SMD 0.42 [0.26, 0.57] (8 datasets); skills 0.29 [0.10, 0.48] (6) | PMC5025580 (a09) | Single-source |
| Inquiry learning on CT | g 1.336 [1.061, 1.611], I2 92.09%, 57 studies; 1.527 vs teacher-centered, 0.779 vs other student-centered; Egger p<.001 | Harapan 2026 (b03) | Single-source; likely inflated |
| Worked examples, maths | g 0.48, 55 studies, 181 effects. Correct beat incorrect examples. Self-explanation prompts did worse than examples alone | Barbieri 2023 (a20) | Single-source (abstract read) |
| Discovery vs instruction | Unassisted vs explicit d -0.38 (108 studies, 580 comparisons). Enhanced vs other +0.30 (56 studies). Vs unassisted: worked examples -0.63, feedback -0.46, direct teaching -0.29. Guided discovery 0.50, elicited explanation 0.36, generation -0.15. Enhanced vs worked examples 0.06 ns | Alfieri 2011 (d15, d16) | Single-source (read in full) |
| CoT exemplars, large model | PaLM 540B GSM8K 17.9 to 56.9; SVAMP 69.4 to 79.0; ASDiv 72.1 to 73.9; AQuA 25.2 to 35.8; MAWPS 79.2 to 93.3 | Wei 2022 (a11, c01) | Established |
| Zero-shot cue | MultiArith 17.7 to 78.7; GSM8K 10.4 to 40.7; below few-shot CoT; no gain on one-step tasks | Kojima 2022 (b07, c03) | Established |
| Task-type limit of CoT | Symbolic +14.2, math +12.3, logic +6.9; other categories 56.8 vs 56.1 (+0.7). 1,218 comparisons, 110 papers | Sprague 2025 (b14) | Established |
| Scale limit | CoT helps from about 100B; hurts most models under 10B | Wei 2022 (b06, b27) | Established |
| Example labels | Random labels cost 1.7 (multi-choice) and 2.6 (classification) points, 12 models | Min 2022 (b12) | Established |
| Example selection | Similar-example retrieval over random +41.9% ToTTo, +45.5% NQ | Liu 2021 (c20) | Established |
| Self-generated exemplars | GSM8K GPT-3.5 75.0 / 75.8 / 76.7 / 77.8 (0-shot / 0-shot CoT / 5-shot CoT / self-generated); davinci-003 14.8 / 50.3 / 54.0 / 61.0 | Yasunaga 2023 (c12) | Single-source |
| Sequenced teaching | SCAN at least 99% with 14 exemplars vs 16% CoT; explicit algorithm teaching cuts error about 10x on long parity | Zhou 2022 (c07, c08) | Established |
| Step-back | PaLM-2L Physics +7, Chemistry +11, TimeQA +27, MuSiQue +7 | Zheng 2024 (b16) | Single-source |
| Self-correction, no oracle | GPT-3.5 GSM8K 75.9 to 75.1 to 74.7; CommonSenseQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0. With oracle: 84.3 and 97.5. 74.7% of answers kept | Huang 2024 (b08, c09, c10) | Established |
| Weak-baseline artifact | CommonGen-Hard: original prompts 44.0 vs 67.0 self-correct; strong prompt 81.8 vs 75.1; 7 calls vs 1 | Huang 2024 (b09) | Established |
| Debate, original | 3 agents, 2 rounds. Arithmetic 67.0/72.1/69.0/81.8 (single/reflection/majority/debate); GSM8K 77.0/75.0/81.0/85.0; chess pawn 91.4/102.1/102.2/122.9; MMLU 63.9/57.7/-/71.1; biographies 66.0/68.3/-/73.8 | Du 2023 (a13) | Contested |
| Debate, matched compute | GSM8K GPT-3.5 standard 76.7; SC 3/6/9 samples 82.5/85.3/88.2; debate about 83. 9 benchmarks, 4 models, 6 calls: debate beats CoT in about 15% of configurations; GPT-4o-mini GSM8K CoT 93.60, SC 95.67, SoM 94.93 | Huang 2024; Zhang 2025 (b10, d04, d05) | Established |
| Mixed-model debate | Heter-MAD average over 9 datasets 76.7 vs same-model 74.3 / 69.9 | Zhang 2025 (d07) | Single-source |
| Step cue on reasoning models | GPQA Diamond (198 items x 25 trials): o3-mini +2.9, o4-mini +3.1, Gemini Flash 2.5 -3.3 vs direct; 20-80% more time. Non-reasoning vs default prompt: Flash 2.0 +6.2, GPT-4o +6.9, Sonnet 3.5 -1.9 ns | Meincke 2025 (d01-d03) | Single-source |
| Demos hurt reasoning models | AIME'25 1-shot -6 to -16, 3-shot up to -35; GPQA 1-shot -1 to -5, 3-shot -4 to -8. Insight-to-Solve: R1-Distill-7B AIME'25 42.0 to 48.0 / 51.3 | Wang 2025 (d12, d13); DeepSeek-R1 (d14) | Established (2 sources) |
| Memory: verified vs unverified | Success: fixed 67.53 / add-all 55.48 / strict 70.95 (RegAgent); EHRAgent 16.75 / 13.05 / 38.50; AgentDriver 40.11 / 32.32 / 51.00; CIC-IoT 71.50 / 59.90 / 85.40 | Xiong 2025 (d08) | Established (with Reflexion) |
| Reflexion | HumanEval Python 0.80 to 0.91; MBPP Python 0.80 to 0.77; Rust 0.60 / 0.52 (no tests) / 0.60 (no reflection) / 0.68 (full). False-positive tests: MBPP 16.3%, HumanEval 1.4% | Shinn 2023 (d10, d11) | Established |
| Output copying | Output similarity tracks input similarity (r near 1) under add-all | Xiong 2025 (d09) | Single-source |
| Lost in the middle | U-shaped accuracy; middle placement can fall below closed-book 56.1% | Liu 2023 (c22) | Single-source |
| AI tutor, structured | Harvard physics, 194 students analysed of 233, crossover. Median post 4.5 (142 lesson-level obs) vs 3.5 (174); z=-5.6; 0.63 SD regression, 0.73-1.3 quantile; 49 vs about 60 min | Kestin 2025 (a15, c16, d18) | Single-source |
| AI help, unstructured | Nearly 1,000 students. Practice +48% (GPT Base), +127% (GPT Tutor). Unaided exam: Base -17% (p<.05); Tutor -0.004 ns | Bastani 2025 (a17, d17) | Single-source (no replication) |
| LLM tutors leak | Revealed solution 66%; wrong feedback 59% (MathDial); leakage penalty 0.75 balanced | Macina 2023; Dinucu-Jianu 2025 (c15, a19) | Established |
| Critical questions pipeline | MT-Bench reasoning 6.75 / 6.85 / 7.3; best or joint-best in 19 of 20 tests | CQoT 2024 (c23) | Single-source |
| CoT text unfaithful | Accuracy drop up to 36% with biased option order; hint never mentioned | Turpin 2023 (b15) | Single-source here (schema cites more) |

Corrections that apply (critique.md): Kestin counts of 142 and 174 are lesson-level observations, not students. "341 studies" is 341 effect sizes. The Abrami inclusion rule (1 hour to 2 days vs at least 3 hours) is unverified. Huang Table 7 debate row alignment is inferred.

## 4. Mechanisms and models

Each mechanism is stated so it can be coded.

**4.1 Worked example as search removal.** The learner reads a solved case instead of searching. For an LLM, a solved case with steps puts a template in context. Implementation: store solved items as (problem, steps, answer). At S2 or S3, retrieve by similarity (c20) and insert. Gate by model type: for models that already think by default, do not insert full steps (d12). Insert an abstract rule instead (d13).

**4.2 Why exemplars work (format over content).** Gains come mostly from format, label space and input distribution (b12). Implementation check: swap the exemplar's answer for a wrong one. If accuracy barely moves, the lesson works by format, and correctness filtering of exemplars is not the lever. This holds for classification and multi-choice. It was not tested on multi-step reasoning, where the human data say correct beats incorrect (a20).

**4.3 Zero-shot cue and CoT as a router problem.** The gain appears only where the task is symbolic or multi-step (b14). Implementation: S0 gate tags the item. Step-by-step mode on for math, logic, symbolic, and multi-step puzzle items. Off elsewhere. Measure tokens saved.

**4.4 Sequenced decomposition (least-to-most).** Solve the easiest subproblem, feed the result into the next (c07). Implementation: O3 produces ordered subproblems. Code runs them in order and passes each answer forward. The model never sees all subproblems solved at once.

**4.5 Generalise first (step-back).** One call asks for the governing principle. The second call solves with the principle in context (b16). Implementation: O2 as a two-call chain. The principle is a text slot, checked only by whether the final answer passes the check.

**4.6 Outside signal for revision.** Revision helps only when the trigger is real output from a test or oracle (b08, d10). Without tests, Reflexion fell to 0.52 vs 0.60 base. Implementation: S5 receives the failing output located by code. If no check exists, skip S5. Watch for false-positive tests: self-written tests passed wrong code 16.3% on MBPP (d11).

**4.7 Verified lesson memory.** A lesson store has three controls (d08, d09, d10). (a) Add an entry only after an external check passes. (b) Track later outcomes per entry and delete entries that precede failures. (c) Do not retrieve near-duplicate past outputs verbatim, since agents copy them (r near 1); retrieve the rule and re-derive. Size: strict memory was smaller than add-all (2,938 vs 4,100 records on RegAgent) and better.

**4.8 Compute-matched voting instead of dialogue.** At equal calls, k independent samples plus a vote beat debate (b10, d04). Self-consistency scales with budget and debate does not (d05). Implementation: spend the extra calls on independent samples in fresh contexts. Voting is done in code (G5). Keep a critic only if it is gated on an outside check.

**4.9 Guidance ladder (assisted vs unassisted).** From Alfieri: unassisted discovery is the weak arm; worked example, feedback and elicited explanation are the strong ones (d16). For the agent: never run a no-guidance retry. Every retry carries one of: failing output, a worked case, or a named operator.

**4.10 Enforced sequence.** Kestin's prompt could not hold step order, so the platform enforced it (d19). Implementation: the state graph is code, the model fills slots. This is already schema design (section 1 of SCHEMA.md). The evidence is one data point.

**4.11 Unaided-after-help evaluation.** Bastani showed practice scores rise while later unaided scores fall (d17). Implementation: evaluate the agent on held-out items with its memory frozen and with no stored answer for that item. A memory that helps only on seen items is a crutch.

**4.12 Placement.** Put retrieved lessons at the start or end of the context, not the middle (c22). Cheap and testable.

## 5. What holds up

**Holds up (established).**
- Human CT instruction has a small to medium effect, about 0.3 (b01, a01). Two independent meta-analyses agree on size.
- CoT with exemplars helps large models on multi-step symbolic tasks and not elsewhere (a11, b14).
- Scale is a precondition (b06, b27).
- Self-correction without an outside signal does not help (b08).
- Debate does not beat matched-compute voting (d04, b10).
- Unassisted discovery loses (d15).
- Unverified memory hurts (d08, d10).
- Demos hurt reasoning models (d12, d14).

**Failed replications and reversals.**
- Self-Refine "about 20%" (b17) shrinks to a loss with a strong baseline (b09).
- Debate gains (a13) shrink to near zero at matched compute (b10, d04). Debate beat the single direct answer in 34 of 45 GPT-4o-mini conditions, so the gain is from extra sampling, not dialogue.
- Reflection hurt GSM8K and MMLU even in Du's own table (a24).
- Reflexion lost on MBPP Python (0.80 to 0.77) because self-written tests passed wrong code (d11).
- Human side: CT-focused college programs added nothing over general college (a08). Not reconciled with Abrami.

**Moderators.**
- Model scale (b06). Task type (b14). Baseline strength (b09, b24). Control group (b03: 1.53 vs 0.78). Outcome closeness to taught content (a02: 0.57 vs 0.30). Presence of an outside signal (b08, d10). Model type: reasoning vs not (d02, d12). Publication tier (d15: first-tier -0.67 vs second -0.24 vs unpublished -0.01). Learner age (adults gained more from enhanced discovery than children, d16).

**Competing explanations.**
- Does CoT teach or just elicit? The ablations (a12) say natural-language steps matter, not extra compute alone. But Meincke (d03) says part of the non-reasoning gain is from a baseline told not to reason.
- Is the human combination effect (0.57) real or confounded? Strategies co-occur in real programs (a03). Treat as a hint.
- Is Kestin's gain from pedagogy or from expert-written solutions in the prompt? Not ablated (a25, d18).
- Bastani's tutor removed harm but gave no gain over control on the exam (d17). So "structure" prevented harm. It did not prove learning.

**Interventions that worked.** Worked examples with steps (large models). Sequenced decomposition. Outside-signal feedback. Verified memory. Self-consistency voting. Guided discovery. Dialogue in human classes.

**Interventions that did not.** Intrinsic self-correction. Debate at matched cost. Persona voters (Multi-Persona never beat CoT in Zhang). Ungated memory. Few-shot on reasoning models. Free AI help for learners. Self-explanation prompts on top of worked examples in humans (a20, abstract only). Generation tasks (d = -0.15, d16).

## 6. Language models

**Few-shot and step-by-step on non-reasoning models (2022-2024).** Large effects on math and symbolic tasks only. Sprague: +12 to +14 points there, +0.7 elsewhere (b14). Needs about 100B parameters (b06). Zero-shot cue is weaker than hand-written steps (b07). Format and label space carry most of in-context learning (b12). Similar-example retrieval beats random by 40+% relative (c20).

**On current reasoning models.** The gain collapses. On GPQA Diamond, a step cue adds +2.9 (o3-mini) and +3.1 (o4-mini) and -3.3 (Gemini Flash 2.5), at 20-80% more time (d02). For non-reasoning models, default prompting already contains short reasoning, so the real gain over default is +6 to +7 on two models and not significant on two others (d02, d03). Different cue wordings changed almost nothing. The test covered one benchmark (K30, single-source).

**Demonstrations on reasoning models.** Worse than none. AIME'25 drops 6-16 points at 1-shot and up to 35 at 3-shot (d12). The model copies steps verbatim (semantic misguidance) or fails to transfer the strategy. DeepSeek-R1's authors advise zero-shot (d14). Converting demos to abstract insights gives gains: R1-Distill-7B AIME'25 42.0 to 48.0 (insights) and 51.3 (insights plus); 14B 50.0 to 54.0 / 60.0 (d13). Self-Refine and Progressive-Hint gained less on the same setup.

**Self-correction and reflection.** Does not help without an outside signal (b08). GPT-4 GSM8K falls 95.5 to 89.0 over two rounds. With oracle labels it rises (84.3, 97.5). With tests, Reflexion adds 8 points on Rust (d10) and 11 on HumanEval Python (d11), but self-written tests can mislead (d11).

**Multi-agent dialogue.** Original gains of +8 to +15 points (a13) vanish at matched compute (b10, d04). Debate corrects some wrong answers and breaks some right ones; aggressive variants change many correct answers (d06). Mixed base models help (d07), but our agent has one model.

**Memory as feedback.** Add-all memory is worse than a small fixed memory (d08). Agents copy retrieved outputs (d09). Gating by a strict check is best. A judge fine-tuned on 300 labels recovers most of the gap (C3: 67.35 / 34.66 / 47.37 / 79.50 vs strict 70.95 / 38.50 / 51.00 / 85.40).

**LLM as tutor.** Strong solvers leak answers (66%) and give wrong feedback (59%) (c15). Kestin's structured GPT-4 tutor beat active learning (0.63 to 1.3 SD) on first-exposure physics. Bastani's free-access GPT-4 cut later unaided scores 17%, and a hint-and-solution prompt removed the cut (d17). Students misjudged their own learning in both studies (a18).

**Faithfulness.** Written reasoning can hide the real cause (b15). Do not treat the reasoning text the model writes as evidence of what drove its answer (G10).

**Honest limit.** Almost all of this is 2022-2023 models. Only d01-d03, d08, d12-d14, and the Kestin and Bastani trials use 2024-2025 systems. Reasoning-model coverage is thin.

## 7. What our agent should take

Evidence ids in brackets. Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Route step-by-step mode by task type.** Use it on symbolic, math, logic and multi-step items; skip elsewhere. Part: S0 and G12. [E] (K07; b14, a11, d02, d03)
2. **Tune the plain baseline before measuring any element.** Report each gain against a tuned plain arm. Part: G7. [E] (K15, K16; b09, b24)
3. **Revise only from a real failing output.** No revision from opinion. If no check exists, do not run S5. Part: G2, S5. [E] (K12; b08, c10, d10)
4. **Spend extra compute on independent samples and a code vote, not debate.** Part: G9, G5, S3. [E] (K13; b10, d04, d05)
5. **Write a lesson only after an external check passes; delete lessons whose later outcomes fail.** Part: memory, S9. [E] (K32, K25; d08, d10, d11)
6. **Do not paste full worked solutions into context for a model that already reasons by default.** Use abstract rules. Part: O2, memory. [E] (K31; d12, d13, d14)
7. **Re-measure every element on the actual base model.** Scale and model type flip signs. Part: G7. [E] (K08; b06, d12)
8. **Never run a no-guidance retry.** Every retry carries a failing output, a named operator, or a worked case. Part: S5, S6. Human evidence [S] (Alfieri, K34; d15, d16); the machine analogue is unmeasured, so this is a design rule consistent with G2, not a measured result.
9. **Treat model-reported confidence and reasoning text as non-evidence.** Part: G10. [E] in the schema; here [S] (K23, K17; a18, b15)
10. **Enforce state order in code, not in the prompt.** Part: S0-S9. [S] here (K36; d19), but already a schema principle.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| State the principle, then apply (vs application alone) | O2 | [S] | K04, K18; a05, b16 |
| Retrieve similar solved items vs random vs self-generated analogues | O7, memory | [E] on non-reasoning; untested on reasoning | K11; c20, c12, c21 |
| Lessons as abstract rules vs full worked cases on a strong model | memory, O2 | [E] direction; our model unknown | K31; d13 |
| Sequenced decomposition vs flat CoT on length-generalisation items | O3 | [E] older models | K19; c07, c08 |
| Lessons at start or end of context vs middle | memory | [S] | K27; c22 |
| Unaided held-out scoring after memory use (does memory create a crutch?) | G6, memory | [S] | K35; d17 |
| Do not retrieve near-duplicate past outputs; retrieve the rule | G12, memory | [S] | K33; d09 |
| Correct vs flawed exemplars in the solved-problem store | memory | [S]; human only | K05; a20 |
| Critical-questions pass vs plain check pass at equal tokens | G1 | [S] | K26; c23 |
| Matched-task vs held-out-task gain from a taught operator | G7 | [S] | K02; a02 |
| Worked case + outside critic + lesson memory vs each alone | G7 | [S] | K03; a03 |
| Step cue on current reasoning model at equal tokens vs default thinking | G7, G11 | [S] | K30; d02 |

## 8. Concrete tests on our bench

All arms get the same token budget. Report accuracy per token and per call. Use a tuned plain arm.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Step cue vs default thinking | Mixed bench: math/logic and non-symbolic items | (a) default; (b) "step by step" cue; (c) cue only on items tagged symbolic by S0 | Accuracy, tokens per item | (b) vs (a) within +-3 points; (c) saves tokens at equal accuracy |
| T2 Rule vs full case in memory | Items with a stored solved neighbour | (a) no memory; (b) full worked case; (c) abstract rule | Accuracy on held-out items | (c) above (a); (b) at or below (a) if the model reasons by default |
| T3 Verified vs ungated lessons | Items with a code check | (a) no lessons; (b) lessons from all runs; (c) lessons only from passing runs, pruned on later failure | Accuracy on later items | (c) > (a) > (b), echoing d08 |
| T4 Revise on output vs on opinion | Items with a check | (a) revise from failing output; (b) "review your answer" | Accuracy, calls | (a) > plain; (b) <= plain |
| T5 Samples plus vote vs critic | Single-answer items | (a) k independent samples, code vote; (b) one answer plus gated critic; (c) debate | Accuracy at equal calls | (a) >= (b) >= (c) |
| T6 Retrieval of exemplars | Items with a solved pool | (a) random; (b) similar; (c) self-generated analogues | Accuracy | (b) > (a) by several points; (c) near (b) |
| T7 Principle then application | Hard STEM/multi-hop | (a) direct; (b) principle first then solve | Accuracy | +3 to +10 on hard items; none on easy |
| T8 Decomposition order | Length-generalisation items | (a) flat CoT; (b) ordered subproblems passed forward | Accuracy by length | (b) above (a) as length grows |
| T9 Lesson placement | Many-lesson prompts | (a) start; (b) middle; (c) end | Accuracy | (b) lowest |
| T10 Unaided after memory | Held-out items, memory frozen | (a) agent never saw the stored answers; (b) agent with memory of seen items | Accuracy on unseen items | (b) not below (a); a drop would signal a crutch |
| T11 Wrong-label exemplars | Format-sensitive items | (a) correct; (b) wrong-answer exemplars | Accuracy | small gap (1-3 points) on classification; larger on multi-step |
| T12 Near-duplicate retrieval | Items whose near-copy neighbours hold wrong answers | (a) retrieve answer; (b) retrieve rule and re-derive | Error rate | (b) lower |

## 9. What does not transfer, and why

- **Class-size and teacher effects.** Mentoring, wait time (a10, no source), role play (a04, 5 studies) assume a human learner and a human teacher. Our agent has a harness and a checker.
- **Dispositions (g 0.23).** Humans have attitudes that instruction shifts. A model has no persisting disposition across calls. Not testable apart from skill outcomes (gap 9).
- **Motivation and engagement** (a16). No analogue.
- **College maturation (Huber and Kuncel).** Human development over four years has no agent counterpart.
- **Tutor design (Kestin, Bastani, MathDial).** The agent is the learner or solver, not the tutor. Leakage penalties and pedagogy prompts matter only if the agent explains to users.
- **Mixed-model debate (Heter-MAD).** Needs several different base models. A single-model agent cannot copy it.
- **Persona diversity.** Persona changes style, not evidence. Gain of 71.1 to 74.2 on MMLU (a14) is one dataset and conflicts with G4.
- **Inquiry g 1.34.** Biased and heterogeneous (b03). Not a planning number.
- **Human expertise reversal values.** Not read here; do not import numbers.
- **Self-report.** Students overrate learning (a18). Model self-ratings do the same; use checks.
- **2022-era results on a model that thinks by default.** Scale and task-type findings were measured on models without built-in reasoning. They may overstate what a prompt can add now.

## 10. Open questions

1. Does stepwise instruction add anything on current reasoning models at equal tokens beyond GPQA? Step-back and least-to-most were not re-measured on reasoning models.
2. Abrami 2015 exact moderator values and the inclusion rule (1 hour vs 3 hours). Journal text was not reachable.
3. Which part of the Kestin tutor drives the gain: expert solutions, enforced order, or self-pacing? No ablation or replication found.
4. Debate vs voting on reasoning models, code and factuality (Du's biographies were not tested against voting).
5. Verified lessons vs unverified at equal tokens against a no-memory arm. Xiong gates against an oracle or a fine-tuned judge, not token-matched.
6. Is there a model-side expertise reversal beyond demos (e.g. rules also hurting strong models)?
7. Do Sweller and Cooper (1985) and Kirschner et al. (2006) report what the secondary account says? Neither was opened.
8. Does the Bastani result replicate, and does an agent that stores solutions do worse on unaided runs?
9. Can critical-thinking dispositions be taught to a model separately from skills?
10. Why do human CT-program studies (Abrami) and the longitudinal data (Huber and Kuncel) disagree?
11. Does the combination effect (dialogue + authentic problems + mentoring, g 0.57) have an agent version (worked tasks + outside critic + lessons) that is more than the sum of parts?

Links to parallel subfields (not covered here): Scaffolding and guided discovery; Productive failure; Working memory; Training; Debiasing and cognitive forcing; Tools and questions; Teaching heuristics; Multi-agent and aggregation topics.

## 11. Sources

[V] = opened and read this session. [M] = snippet or citation only. Abrami 2015 was read through a secondary summary and an abstract.

- [V] Abrami et al. (2015) Strategies for teaching students to think critically (summary, SR 18). https://www.clearinghouse.edu.tum.de/wp-content/uploads/2023/12/CHU_KR18_ENG_Abrami_2015.pdf (a01-a06). Journal abstract: https://api.crossref.org/works/10.3102/0034654314551063 (b02). Journal full text [M], blocked (403).
- [V] Abrami et al. (2008) abstract via Crossref. https://api.crossref.org/works/10.3102/0034654308326084 (b01). Full text [M] (a23).
- [V] Hitchcock, Stanford Encyclopedia of Philosophy, Critical Thinking. https://plato.stanford.edu/eNtRIeS/critical-thinking/methods.html (a07)
- [V] Huber and Kuncel (2016), AERA snapshot. https://www.aera.net/Newsroom/Study-Snapshot-Does-College-Teach-Critical-Thinking (a08)
- [V] Nursing meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC5025580/ (a09)
- [V] Insight Assessment handout. https://insightassessment.com/wp-content/uploads/2023/12/Teaching-for-Critical-Thinking-1.pdf (a10)
- [V] Harapan et al. (2026) inquiry meta-analysis. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13562932/fullTextXML (b03)
- [V] Alhur et al. (2026) AI-supported education review. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13570614/fullTextXML (b04)
- [V] Review of ChatGPT-type effects on medical students. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12954715/fullTextXML (b05)
- [V] Barbieri et al. (2023) worked examples meta-analysis, abstract and preview. https://link.springer.com/article/10.1007/s10648-023-09745-1 (a20; b20 [M])
- [V] Alfieri et al. (2011) discovery meta-analysis, full text. https://www.fisme.science.uu.nl/publicaties/literatuur/2011_alfieri_discovery_learning.pdf (d15, d16). DOI https://doi.org/10.1037/a0021017
- [M] Sweller and Cooper (1985). https://doi.org/10.1207/s1532690xci0201_3 (a21)
- [M] Kirschner, Sweller and Clark (2006). https://doi.org/10.1207/s15326985ep4102_1 (a22, b18)
- [V] Wei et al. (2022) Chain-of-thought. https://arxiv.org/abs/2201.11903 (a11, a12, b06, c01, c02)
- [V] Kojima et al. (2022) zero-shot reasoners. https://arxiv.org/abs/2205.11916 (b07, c03)
- [V] Min et al. (2022) rethinking demonstrations. https://arxiv.org/abs/2202.12837 (b12, c04)
- [V] Lampinen et al. (2022) explanations in context. https://arxiv.org/abs/2204.02329 (b13, c05, c06)
- [V] Zhou et al. (2022) least-to-most. https://arxiv.org/abs/2205.10625 (c07)
- [V] Zhou et al. (2022) algorithmic reasoning. https://arxiv.org/abs/2211.09066 (c08)
- [V] Du et al. (2023) multiagent debate. https://arxiv.org/abs/2305.14325 (a13, a14, a24, b11, c11)
- [V] Huang et al. (2024) self-correction. https://arxiv.org/abs/2310.01798 (b08-b10, c09, c10)
- [V] Zhang et al. (2025) multi-agent debate controls. https://arxiv.org/abs/2502.08788 (d04-d07)
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 (b14)
- [V] Turpin et al. (2023) unfaithful explanations. https://arxiv.org/abs/2305.04388 (b15)
- [V] Zheng et al. (2024) step-back. https://arxiv.org/abs/2310.06117 (b16)
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651 (b17)
- [V] Yasunaga et al. (2023) analogical reasoners. https://arxiv.org/abs/2310.01714 (c12)
- [V] Chang (2023) Socratic prompting. https://arxiv.org/abs/2303.08769 (c13, c14)
- [V] Macina et al. (2023) MathDial. https://arxiv.org/abs/2305.14536 (c15, c25)
- [V] Dinucu-Jianu et al. (2025) from problem-solving to teaching. https://arxiv.org/abs/2505.15607 (a19)
- [V] Kestin et al. (2025) AI tutoring RCT. https://www.nature.com/articles/s41598-025-97652-6 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/ (a15, a16, a25, c16, d18, d19)
- [V] Bastani et al. (2025) PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ ; https://doi.org/10.1073/pnas.2422633122 (a17, a18, c17, d17)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c18, d10, d11)
- [M] Zhao et al. (2023) ExpeL. https://arxiv.org/abs/2308.10144 (c19; the 40% vs 39% figure was not re-opened)
- [V] Liu et al. (2021) good in-context examples. https://arxiv.org/abs/2101.06804 (c20)
- [M] Rubin et al. (2021) retrieval of prompts. https://arxiv.org/abs/2112.08633 (c21; exact gains not extracted)
- [V] Liu et al. (2023) lost in the middle. https://arxiv.org/abs/2307.03172 (c22)
- [V] Critical-Questions-of-Thought (2024). https://arxiv.org/abs/2412.15177 (c23, c24)
- [V] Meincke et al. (2025) Prompting Science Report 2. https://arxiv.org/abs/2506.07142 (d01-d03)
- [V] Xiong et al. (2025) memory management. https://arxiv.org/abs/2505.16067 (d08, d09)
- [V] Wang et al. (2025) From Harm to Help. https://arxiv.org/abs/2509.23196 (d12, d13)
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948 (d14)
- Lines b21-b27 are cross-paper syntheses by the earlier agents, not independent sources.
