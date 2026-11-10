# Scaffolding and guided discovery: deep document

*Subfield A05.09. Sources: evidence_a-d.jsonl (ids a01-a31, b01-b29, c01-c25, d01-d16), claims.jsonl (K01-K28), critique.md. Status words: established, single-source, contested, open. Numbers marked "unverified" were not read in the full text.*

## 1. What it is

Scaffolding is temporary, task-specific support that lets a learner do something beyond unaided reach, and that is then withdrawn. Wood, Bruner and Ross (1976) coined the word for adult-child tutoring (a01, a02). Guided discovery is the instructional family in which the learner still searches or constructs, but inside structure: prompts, feedback, worked steps, checkpoints. Its opposite, pure (unassisted) discovery, gives a task and no help.

Three defining features come from later reviews (a02, read in Belland 2017):
- Contingency: the tutor checks what the learner can do and gives just enough.
- Intersubjectivity: tutor and learner share a goal.
- Transfer of responsibility: support is faded until the learner works alone.

The debate has two layers. Layer 1 is "does minimal guidance work?" Kirschner, Sweller and Clark (2006, a05) say no, on cognitive-load grounds. Layer 2 is "does the defining mechanism of scaffolding (contingent support and fading) matter?" Layer 2 is much less supported than Layer 1 (K05, K06).

Why it matters for our agent: the agent is a scaffold around a frozen model. Our schema (guardrails G, states S, operators O) is a guidance structure. We need to know (a) that guidance beats free exploration, (b) which kind, (c) whether to fade it, adapt it, or verify it, and (d) whether the human results carry to a model. The honest answer: (a) yes, (b) metacognitive and strategic better than conceptual, (c) unproven, (d) mostly untested at inference time.

Overlaps in earlier documents (do not repeat): worked examples (A05/01), expertise reversal and fading (A05/02), desirable difficulties (A05/04). This document adds the meta-analytic numbers, the replication failure, and the LLM evidence. Parallel subfields: productive failure, cognitive load/working memory, task-type limits.

## 2. History and theories in depth

**1976, Wood, Bruner, Ross (a01, b26; not opened).** One adult tutor (a paper author) helped 3-, 4- and 5-year-olds build a pyramid of interlocking blocks. Secondary summaries say 30 children (10 per age) and 21 blocks (unverified). Six tutor functions: recruitment, reducing degrees of freedom, direction maintenance, marking critical features, frustration control, demonstration. No control group; descriptive. Key idea: the tutor takes the parts the child cannot do and the child does the rest.

**1978, Wood, Wood, Middleton.** The one experiment that compared contingent instruction with demonstration, verbal instruction and a mixed style. Contingent (help rises after failure, drops after success) won on later independent solving. This was the main empirical base of "contingency". It failed to replicate in 2025 (a03, Section 5).

**1986-2000s, Vygotsky and the zone of proximal development.** Scaffolding is the practical form of working in the zone. Evidence for the zone idea is mostly conceptual, not experimental.

**1999-2012, cognitive load theory (CLT).** Tuovinen and Sweller (1999, a08, second-hand): exploration practice gave much higher load and worse learning than worked examples for low-knowledge learners; high-knowledge learners were not hurt. Kirschner, Sweller and Clark (2006, a05-a11) turned this into an argument against minimal guidance. Mechanism (a06): working memory is small; long-term memory holds schemas; discovery makes novices search the problem space, which loads working memory and builds no schema. Chess recall (De Groot; Chase and Simon 1973) is indirect support. The paper has no pooled effect size and no direct load measure. Clark, Kirschner and Sweller (2012, a13, a14) restate it: skilled learners did better with less guidance, less-skilled with more, in about 70 studies (Clark 1989, not opened). They add: guidance should be faded as skill grows; a practice success rate near 80% is optimal (82% vs 73% correct in best vs least successful fourth-grade classes; a teacher heuristic, not an experiment).

**2007, the reply.** Hmelo-Silver, Duncan and Chinn (a12, b23; not opened): problem-based and inquiry learning are scaffolded, so they are not "minimal guidance". The dispute is partly about definitions (K22). Mayer (2004, b24) proposed a "three-strikes rule" against pure discovery (no figures).

**2004, Klahr and Nigam (a04, b25).** 112 third and fourth graders learned the control-of-variables strategy by direct instruction or by discovery. Many more direct-instruction children mastered it (quoted split 77% vs 23%, unverified). Children who mastered it by either route transferred equally well to evaluating science-fair posters (path independence). Single study; the paper's own text was not opened for the split.

**2007, Koedinger and Aleven (b28).** The "assistance dilemma": when to give help and when to withhold. Not read in full.

**2010-2018, meta-analyses.** Alfieri et al. (2011) gave the numbers (a15-a18). Belland et al. (2017) and Kim et al. (2018) gave the computer-scaffolding numbers (a19-a21, b01-b06). Lazonder and Harmsen (2016, b20) found inquiry works when guided.

**2023-2026, LLM era.** Three strands:
1. Prompt-side decomposition for the model (Zhou et al. least-to-most, a22-a24, d01).
2. Hints used as training scaffolds for RL (Scaf-GRPO, QuestA, SEELE: c01-c06, c22, c25, d16).
3. LLMs as tutors for humans (Bastani, Kestin, Tutor CoPilot, LearnLM, MathTutorBench: a25-a31, c07-c11).
Plus new inference-time hint tests (d07, d08) and tests of prompting methods on reasoning models (d02-d05).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Unassisted discovery loses to explicit instruction | d = -0.38 (95% CI -0.50 to -0.25), 108 studies, 580 comparisons; Q(107)=522.11 | Alfieri 2011 (a15) | established |
| Penalty by comparison type | worked examples -0.63; feedback -0.46; direct teaching -0.29; explanations -0.28 | a16 | established |
| Penalty by domain and age | math -0.16; science -0.39; problem solving -0.48; verbal/social -0.95; adolescents -0.53 vs adults -0.26 | a16 | established |
| Penalty by outcome | acquisition -0.95; post-test -0.35; time to solution -0.21 | a16 | established |
| Assisted discovery beats other instruction | d = 0.30 (CI 0.15-0.44), 56 studies, 360 comparisons; 0.25 without 24 motor comparisons; adults gain more than children | a17 | established |
| Inquiry learning works when guided | learning activities d=0.66; performance success 0.71; outcomes 0.50; 72 studies | Lazonder and Harmsen (b20, snippet) | single-source |
| Computer-based scaffolding, overall | g = 0.46, 144 studies, 333 outcomes; Egger p=.166 | Belland 2017 (a19) | established |
| Bayesian network meta-analysis | 56 studies; g = 3.13 for learning-disabled students (very large, wide) | a21 | single-source |
| Computer scaffolding, Bayesian | g = 0.385, CrI 0.022 to 0.802 | Kim 2018 (b01) | established |
| Scaffold type | metacognitive 0.384; strategic 0.345; conceptual 0.126; question prompts 0.078 | b04 | single-source |
| Scaffold function | expert modelling 0.523; feedback 0.474; hints 0.375; synthesis 0.156; evaluation 0.147 | b04 | single-source |
| Fading | fade+add 0.590; fade 0.429; add 0.443; Belland 2017: no moderator difference | b02, a20 | contested |
| Customisation | self-selected 0.519; performance-adapted 0.434; fixed interval 0.376 | b03 | contested |
| Fading is rare | no customisation in 65% of studies; fading in 9.3% of 43 articles | b05 | established |
| Contingent tutoring did not replicate | N=285 three-year-olds, 4 conditions; tutor accuracy 68.9% vs 70%; effect on later independent solving not reproduced | Smit 2025 (a03) | single-source |
| Direct instruction vs discovery, strategy mastery | N=112; about 77% vs 23% (unverified); equal transfer for those who mastered | Klahr and Nigam (a04) | single-source |
| Guided play | vs direct: shape knowledge g=0.63, task switching 0.40, early maths 0.24; vs free play: spatial vocabulary 0.93; 17 studies, N=3,893 | Zosh 2022 (b29, snippet) | single-source |
| Unrestricted LLM help harms later unaided exam | practice +48% (GPT Base), +127% (GPT Tutor); exam -17% (-0.054, SE 0.022) for Base, -0.004 (ns) for Tutor; about 1,000 students; Base right 51% of the time (42% of errors logic, 8% arithmetic) | Bastani 2025 (a25, b10, d12) | established |
| Step-ordered AI tutor vs active learning | N=194 crossover; 0.63 SD (regression), 0.73-1.3 SD (quantile); median 4.5 vs 3.5; time 49 vs 60 min; engagement 4.1 vs 3.6 | Kestin 2025 (a27, b07, d11) | single-source |
| Prompt order drifted, fixed in code | tutor "would occasionally discuss parts out of sequence"; no ablation | b08, d11 | single-source |
| LLM hints to human tutors | +4 pp mastery (62% to 66%, p<.01); +9 pp for lower-rated tutors; about $20 per tutor per year; 900 tutors assigned, 783 analysed, 1,800 students, 550,000+ messages (latest version; earlier 700+/1,000+/350,000) | Tutor CoPilot (a29, b14, c14) | single-source |
| Guided stepwise LLM use, small study | Quiz 4 no-help: guided beat no-LLM by 23.17 points (g=0.95, p=.022), unrestricted by 16.42 (g=0.73, p=.079); final exam g 0.61/0.71, CI includes 0; 37 analysed of 57, not randomised | b15, c16 | contested |
| Forced independent-first study did not help | N=334; AI access +0.23 SD; unrestricted +0.34 SD; restricted +3.4% (ns); unrestricted 5.1% above restricted | Fischer 2025 (c17) | single-source |
| Decompose-then-solve, length generalisation | SCAN 99.7% vs 16.2% CoT (code-davinci-002, 14 exemplars); last-letter L=12 74.0 vs 31.8 (37.4-38.4 with 4-8 CoT exemplars) | Zhou 2023 (a22, a23, c20) | single-source |
| Decompose-then-solve, GSM8K and DROP | GSM8K 62.39 vs 60.87 (+1.52); 2 steps 74.53 vs 76.68 (CoT better); 5+ steps 45.23 vs 39.07; DROP 82.45 vs 74.77 and 73.42 vs 59.56 | a24, d01 | single-source |
| Hints in RL training | Scaf-GRPO, Qwen2.5-Math-7B, AIME24 30.0 to 43.3 (+44.3% relative); 7-benchmark avg 45.2 to 50.9 | c01 | established |
| Hint ablations (Scaf-GRPO) | no knowledge hint 49.2; no planning 48.6; no solution 48.0; solution only 48.4; no incremental chunking 47.7; scaffold from step 0: -9.2% relative; whole hint at once -6.3% | c02, c03, c25 | established |
| Gain depends on base model | +44% Qwen2.5-Math-7B; +10.3% Llama-3.2-3B; +5.9% R1-Distill-Qwen-1.5B | c03 | single-source |
| QuestA | Nemotron-1.5B avg 53.14 to 63.26; AIME24 61.77 to 72.50 | c04 | single-source |
| 50% success target | SEELE: 3B avg 42.2 vs GRPO 30.4 vs best baseline 40.5; 1.5B 34.2 vs 24.2; 0.5 target best, symmetric fall-off | c06, d16 | single-source (training only) |
| Inference prefix hints | Llama-3.1-8B GSM8K 84.8 to 95.2 over 0-90% hint; 80.6% of items need none; 1B/3B/8B recover 60/81/79% of gap | Dong 2026 (d07) | single-source |
| Next-step hints at inference | Phi-4-mini-reasoning MATH-500 subset (74 items) 56.76 to 77.03; AIME24 R1-Distill-Llama-8B 0.00 to 44.83 | HintMR (d08) | single-source |
| CoT prompt adds little on reasoning models | GPQA: o3-mini +0.029, o4-mini +0.031, Gemini Flash 2.5 -0.033; time +20-80% (reasoning), +35-600% (non-reasoning); "decompose" variant negligible | Meincke 2025 (d02) | contested |
| Exemplars add little on strong models | zero-shot CoT matches or beats 8-shot on Qwen2.5-7B/72B | d03 | single-source |
| CoT still helps distilled reasoning models | improved in 72% of cases; R1-32B thinking tokens -61.4% | d04 | contested |
| Self-correction without oracle fails | GPT-4 GSM8K 95.5 to 89.0 (2 rounds); GPT-3.5 CommonSenseQA 75.8 to 41.8; oracle lifts GPT-3.5 GSM8K 75.9 to 95.5; self-consistency 88.2 vs debate 83.0 at 9 responses | Huang 2024 (d06) | single-source |
| LLM hints equal human hints for learning | N=274; gain control 1.85% (ns), human 11.62%, ChatGPT 17.00%; ChatGPT vs human p=.416; about a third faulty; majority vote of 10 cuts error to 0-13% | Pardos and Bhandari (c18) | contested |
| Pedagogy-tuned tutor beats peers on expert preference | LearnLM +31% over GPT-4o, +11% Claude 3.5 Sonnet, +13% Gemini 1.5 Pro | a31, c10 | single-source |
| Supervised LLM tutoring (Eedi) | remediation: static hints 65.4, human 91.2, LearnLM 93.0; next-unit first question 56.2/60.7/66.2; 74.4% of 3,617 drafts accepted unedited | c11 | single-source |
| Leak penalty trades gain for safety | student solve-rate gain 36.2% (lambda 0) down to 21.2% (lambda 1.5) | c09 | single-source |
| Long dialogs weaken scaffolding | hard split win rate lower than base for most models; LLM tutors reveal answers early (ChatGPT Telling@5 16% vs human under 1%) | c07, c08, a30 | single-source |
| Withholding costs satisfaction | "agent understood me" 2.69 of 5; suggestions useful 2.77 | Cohn 2026 (b13) | single-source |
| Contingent LLM tutor, experience | 131 adults, 393 sessions; full answer given away 1 of 16 sessions vs 1 of 6 (question-only); less frustration than question-only; load equivalent; no delayed test | Hou 2026 (d09) | single-source |

## 4. Mechanisms and models

Each mechanism is written so an engineer could turn it into code.

**M1. Load-reduction (CLT).** Novice working memory overflows when it must both search and learn. Guidance removes search. Implementation: give the model the plan or the next step, so its tokens go to execution. Moderator: prior knowledge. For a model, the analogue is task difficulty relative to capability (see M7).

**M2. Degrees-of-freedom reduction (Wood et al.).** The tutor fixes some choices so the learner faces a smaller space. Implementation: code narrows the action set per state (our S-states already do this). Each constraint should map to a named failing step (a01 relevance).

**M3. Contingent support.** Support level L is a function of the last outcome: raise after failure, lower after success. Pseudocode: `L = min(Lmax, L+1) if fail else max(0, L-1)`. The Hou et al. tutor (d09) uses this at "decision points", with hints rising after failure and fading after take-up. Direct human evidence for learning gain failed to replicate (a03). Treat as a cost and frustration device, not a proven learning device.

**M4. Fading (transfer of responsibility).** Withdraw scaffolds as success rises. Three schedules to implement: fixed (every n items), fade-after-success (after k passes without help), self-selected. Human evidence is mixed (b02, a20, Belland 2015). For an agent the relevant effect is on later unaided items, which needs a held-out batch.

**M5. Hint ladder.** Tiers from least to most revealing: knowledge hint, plan hint, solution chunk, delivered incrementally, only on items where unaided attempts all failed. Scaf-GRPO (c01-c03, c25) ablated each piece: every removal cost 1.3 to 2.5 average points against the full 50.9 (47.7 without incremental chunking, the largest loss of the ablations). Hints from step 0 hurt (hint dependency). A hint-free exemption of 15% of training worked. Training-time result; inference-time ladder is untested (K13, K14).

**M6. Dosage targeting.** SEELE (c06, d16): learning signal peaks when rollout success is about 50%, so hint length is fitted per item from earlier attempts. It is a gradient-signal argument for RL, not shown for prompting. Inference analogue: pick hint level from observed pass rate on earlier attempts. Dong (d07) shows a smooth-ish rise with hint length and 80.6% of items need no hint, which supports "start with none".

**M7. Expertise reversal.** Support that helps novices wastes effort or hurts experts (b18, b19). Implementation: a per-model-class switch in S0. Data conflict (K15, K23): dedicated reasoning models gain about nothing from added CoT or exemplars (d02, d03, d05), while distilled reasoning models still gain in 72% of cases (d04). Run on and off per model.

**M8. Decomposition with feedforward (least-to-most).** Stage 1: ask the model to list easier subproblems. Stage 2: solve them in order, appending each answer to the context for the next. Zhou's authors say hand-made decompositions fix nearly all failures, so the weak point is generating the decomposition (d01). The gain is large where the test is longer than the exemplars (length generalisation) and small on short problems; on 2-step GSM8K problems it hurts slightly.

**M9. Code-enforced sequence.** Kestin (b08, d11): a prompt alone drifted out of order, so code walks the learner through parts. Implementation: the state machine, not the prompt, controls which part is shown. No ablation, no token cost, so this is an observation.

**M10. Answer withholding with an escape.** Rule: no final answer before hint steps; after K failed probes, give the next step. Evidence for the benefit: guardrails remove the -17% harm (d12) but add no gain on the unaided exam. Evidence for the cost: frustration (b13, a30, d09). Evidence for the leakage trade-off: c09. K is untested.

**M11. Hint verification.** A third of ChatGPT hints were faulty (c18). Self-review does not fix it without an outside signal (d06). Fixes with data: vote over fresh samples (error to 0-13%, c18; self-consistency beats debate, d06), or executable checks. Cost is N times tokens.

## 5. What holds up

**Holds (multiple sources):**
- Unguided discovery loses on average, especially against worked examples (K01; d -0.38, -0.63).
- Guided discovery beats other instruction by d 0.25-0.30 (K02). The guidance carries the benefit.
- Computer scaffolding helps on average, g 0.39-0.46, with wide intervals (K03).
- Unrestricted answer-giving AI helps practice and hurts later unaided work; a hint-first tutor removes the harm (K08).
- In RL training, tiered, incremental, late-delivered hints on failed items help (K13), three independent systems.
- Withholding answers raises frustration (K19).

**Fails or is weak:**
- Contingency: the 1978 effect did not replicate at N=285 (a03). The direct test of the central mechanism of scaffolding failed. The average benefit of scaffolding is not touched by this.
- Fading: no benefit shown (a20); small edge in one (b02); unfaded better in a 2015 meta-analysis. Confidence intervals overlap heavily.
- Restricting AI use: a small non-randomised positive (b15) against a larger preregistered null (c17). Designs differ.
- Guardrails: protective, not proven helpful (d12: -0.004 ns).
- Self-correction without outside signal: negative (d06).

**Moderators:**
- Learner prior knowledge (a08, a13, b18): low-knowledge learners need guidance.
- Age: adolescents hurt more by discovery than adults (a16). Adults gain more from guided discovery (a17).
- Domain: discovery penalty smallest in math (-0.16), largest in verbal/social (-0.95) (a16).
- Scaffold type: metacognitive and strategic over conceptual and question prompts (b04, single source).
- Outcome type: acquisition scores penalised most (-0.95).
- Model strength (machine analogue): Scaf-GRPO +44% vs +5.9% by base model (c03); CoT value falls on reasoning models (d02).
- Hint quality: a faulty hint misleads (c18).

**Interventions that worked:** step-ordered tutor in code (b08); LLM hints for weaker human tutors (+9 pp); tiered hints in RL; next-step hints for small reasoning models (d08); least-to-most for long compositional tasks (a22).

**Interventions that did not:** whole-solution hints (c25: -4.9% to -6.3%); hints from step 0 (c03: -9.2%); explicit "decompose" wording on GPQA (d02); few-shot on R1 (d05); intrinsic self-review (d06); forced independent-first study (c17).

**Weak spots in the evidence:** human samples are children or STEM undergraduates; tests are short, not open reasoning; credible intervals wide (CrI 0.022 to 0.802); LLM-learning studies measure human learners; Wood 1976, Klahr and Nigam 77/23, Smit Bayes factors and Hmelo-Silver 2007 not opened.

## 6. Language models

Three questions: how models behave when they are the solver, the learner, and the tutor.

**Model as solver given decomposition.** Least-to-most (a22-a24, d01, code-davinci-002 only): SCAN 99.7 vs 16.2; last-letter at L=12 74.0 vs 31.8 (CoT with matched 4-8 exemplars 37.4-38.4); GSM8K +1.52 overall, +6.16 on 5+ steps, -2.15 on 2-step; DROP +7.7 and +13.9. No test on current models was found. The gain is largest where length exceeds exemplar length.

**Model as solver given generic step-by-step prompting.** GPQA Diamond, 4,950 runs per prompt per model (d02): non-reasoning average up 0.04-0.14, but easy items lost; reasoning models +0.03 (o3-mini, o4-mini), -0.03 (Gemini Flash 2.5); time +20-80% for reasoning models. Zero-shot matches 8-shot on Qwen2.5 (d03). DeepSeek says few-shot lowers R1 (d05). Conflict: distilled reasoning models gain in 72% of cases (d04, probably partly token saving).

**Model as solver given hints.** Prefix hints from a stronger model: Llama-3.1-8B GSM8K 84.8 to 95.2; 80.6% of items need none (d07). Next-step hints without the answer: small reasoning models gain 20 to 48 points on a MATH-500 subset and AIME24 (d08), on small test sets. In both, the hint source is a stronger model, which our agent lacks.

**Model as learner (RL with hints).** Scaf-GRPO: +44.3% relative on AIME24 for a math base model, +5.9% for a long-CoT distilled model (c03). QuestA: avg 53.14 to 63.26 (c04). SEELE: 42.2 vs 30.4 (c06). These change weights; the agent does not train. The transferable part is the schedule logic (late, tiered, incremental, targeted), not the result.

**Model as self-verifier of its hints and plans.** Intrinsic self-correction lowers accuracy (GPT-4 GSM8K 95.5 to 89.0). An oracle signal lifts it (75.9 to 95.5). A fresh-sample vote beats debate at equal responses (d06). A third of ChatGPT hints are faulty; a vote over 10 cuts error to 0-13% (c18). Models tested are 2023-era; newer self-checking models untested.

**Model as tutor.** Pedagogy-tuned LearnLM is preferred over GPT-4o (+31%), Claude 3.5 Sonnet (+11%), Gemini 1.5 Pro (+13%) by expert raters (a31). Solving skill does not make a tutor: LLM tutors reveal answers early and weaken over long dialogs (a30, c07, c08). A leak penalty trades gain for safety (c09). In the field, a step-ordered tutor beat in-class active learning (0.63 SD) (a27); unrestricted GPT harmed unaided exams (-17%) (a25); a hint-first tutor was neutral (-0.004, ns). Hints for human tutors: +4 pp, +9 pp for weaker tutors (a29). A contingent tutor gave fewer answers than an assistant and frustrated less than a question-only tutor (d09).

**What changed behaviour and by how much:**

| Change | Effect |
|---|---|
| Decomposition feedforward | +83 points on SCAN length split; +1.5 on GSM8K |
| CoT instruction on reasoning model | about 0 to +3 points, +20-80% time |
| Hint prefix to small model | +10 points GSM8K 8B |
| Next-step hints | +20 to +48 points on small reasoning models |
| Self-review without oracle | -6.5 points GPT-4 GSM8K |
| Guardrails on human tutoring | harm of -17% reduced to ns |

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, memory = M.

### Add now (established)

1. **Do not run free exploration without a plan or checks.** Guided structure beats unguided search. Part: G/S0. [E] K01, K02; a15, a16, a17, a18. The schema already has states and checkpoints; this confirms them rather than adding anything.
2. **No answer copying; hint before answer in any learning or memory path.** Where the agent stores solved items for reuse, store the failing step and the fix, not just the final answer. Part: G, memory. [E] K08; a25, b10, d12. Caveat: protective, not proven to add gain.
3. **Escape rule when probing: after K failed probes, move to the next, more revealing step.** Part: S0 mode. [E] for the cost of withholding (K19; b13, a30, d09); the threshold K is untested (see UNKNOWNS U7).
4. **If hints are ever used (stored hints, library items), deliver them in small tiers, and only after an unaided attempt has failed.** Part: O (hint level), memory. [E] for training-time (K13; c01, c02, c03, c25, c04, c06, c22). Treat as a design rule for how to write the library, not as proof at inference time.
5. **Verify any self-written hint or plan with an outside signal: a code check or a vote over fresh samples, never a re-read by the same model.** Part: G2/G5 (already covered). [E] via existing guardrails; supported here by d06, c18. Cost is N times tokens, so use it only where a hint steers later steps.
6. **State order is enforced by code, not by prompt.** Part: S-graph. Already in the schema; Kestin (b08, d11) agrees, but only as an observation. Do not count it as new evidence.

### Test first

1. **Decompose-then-solve vs plain CoT on current models (O3).** [S] K12; a22-a24, d01. Open gap 1. Highest-value test.
2. **Scaffold on/off by model class (S0 mode).** [C] K15, K23; d02-d05. Expect an interaction.
3. **Strategy hint vs concept hint vs question prompt inserted at one step (G metacognitive check).** [S] K04; b04.
4. **Contingent vs fixed vs no support (S0, O hint level).** [C/S] K06, K26; a03, d09. Do not assume contingency wins.
5. **Fade-after-success vs fixed vs no-fade on an item stream with an unaided later batch (memory write rules).** [C] K05; open K27.
6. **Hint level: knowledge vs plan vs solution, incremental vs whole (O).** [E] in training, open at inference. K13, K14, K24.
7. **Escape threshold K.** Open K28.
8. **Hint verification by vote vs single hint.** [C] K18, K25.
9. **Prompt-only vs code-enforced step order.** [S] K10; open gap 8.
10. **Attempt-first-then-hint vs immediate hint.** [C] K09; b15, c17.
11. **Answer-withholding for a carried-memory agent, then an unaided batch.** Open analogue of K08 (gap 7).

## 8. Concrete tests on our bench

All arms get the same token budget (G7). Setup tokens are counted. Items come from the bench families (ARC-like grids, BrainTeaser-type riddles, NoveltyBench where relevant), split into a scaffold batch and a held-out unaided batch.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Compositional and long multi-step items (5+ steps), plus 2-step controls | plain CoT; least-to-most; best-of-N at matched tokens | accuracy by step count | gain on 5+ steps, none or slight loss at 2 steps (as d01); unknown on current models |
| T2 | Same item set, 3 model classes (reasoning, distilled, non-reasoning) | scaffold on vs off | accuracy, tokens | interaction: about 0 for reasoning (d02), positive for weaker models |
| T3 | Items where the first plain attempt fails | strategy hint; concept hint; neutral question prompt | solved after retry | strategy at least as good as concept (b04 g 0.35 vs 0.13) |
| T4 | Item stream of 30 with 10 held-out | fixed support; fade-after-success; contingent (up after failure, down after pass); none | accuracy on held-out unaided, total tokens | contingent equals fixed on learning (a03), cheaper in tokens |
| T5 | Items failing 3 plain attempts | no hint; knowledge hint; plan hint; solution chunk; incremental ladder; whole hint | pass rate, tokens | incremental ladder > whole hint (c25: -6.3% for whole); hint source must be the same model (no stronger model) |
| T6 | Hard items | escape after K=1, 2, 3 failed probes; never; always tell | solved rate, tokens, later unaided accuracy | moderate K best; never-escape wastes tokens |
| T7 | Self-written plans on 100 items | single plan; plan checked by same model; plan checked by vote of 5; plan checked by code test | plan correctness, final accuracy | same-model check about 0 gain (d06); vote or code gains; costs N times |
| T8 | State-machine items | prompt-only order; code-enforced order | out-of-order transitions, accuracy | code removes drift; size of gain unknown |
| T9 | Item stream with memory writes | write final answer only; write failing step plus fix; write with hint withheld until second attempt | accuracy on next unaided batch | answer-only memory shows a crutch effect (cf. -17% in a25); failing-step memory better |
| T10 | Items with and without "hint before attempt" | attempt first then hint; hint immediately | accuracy, tokens | no clear difference in accuracy (c17); attempt-first cheaper when the plain attempt solves (80.6% need no hint, d07) |

Pre-register the metric and the threshold before running (see UNKNOWNS.md "Add if").

## 9. What does not transfer, and why

- **Learner memory and schema building.** Humans with limited working memory gain from load reduction. A model's context is large and it does not build schemas across a run unless we write memory. The CLT mechanism (M1) maps to context clutter at best.
- **Contingency from a tutor's eye.** A human tutor sees the learner's face and error. Our code sees only outputs and checks. Contingency must run on checks (G2, G3), not intuition.
- **Frustration and motivation.** Withholding answers costs satisfaction in humans (b13). A model has no frustration; the cost is tokens and failed attempts. Keep the escape rule for token reasons.
- **Long-term unaided learning.** The crutch effect (-17%) is about a human losing skill. A frozen model does not lose or gain skill from being helped. It transfers only if memory writes the help (T9).
- **Hint source.** Almost all inference-time hint results (d07, d08) use a stronger model for hints. Our agent has no stronger model. Hints must come from the same model (checked by code or votes) or from a stored library.
- **RL-training hints.** Scaf-GRPO, QuestA and SEELE change weights. We do not train. Only schedule logic transfers.
- **Child and early-education evidence.** Guided play, Wood 1976, the 285-child replication: young humans on motor tasks. Little to say about open reasoning by a model (K21).
- **Pure-discovery penalty.** The model never does "unassisted discovery" in the human sense. Our plain arm is the closest analogue; its weakness against a plan is a test, not an assumption.
- **Old-model numbers.** Least-to-most numbers are code-davinci-002. Not assumed to hold.

## 10. Open questions

1. Does least-to-most still beat plain CoT on current reasoning models at equal tokens, and on which tasks beyond length generalisation?
2. Is contingent support better than fixed for an agent, given the failed human replication?
3. Does fading across an item stream help a model or its memory later?
4. What hint level is best at inference (knowledge, plan, solution), and does the 50% dosage rule carry to prompting?
5. Does scaffold benefit reverse for strong models, and where is the break-even?
6. What does hint verification cost in tokens per hint, and what is the best verifier without a stronger model?
7. Does withholding answers improve later unaided accuracy for an agent with memory?
8. How much does code-enforced sequencing beat prompt-only sequencing for our state machine?
9. What is the best escape threshold K?
10. Do the exact numbers hold in full text: Wood 1976 (30 children, 21 blocks), Klahr and Nigam (77/23), Smit Bayes factors, Hmelo-Silver 2007, Lazonder and Harmsen? They were not opened.
11. Is the metacognitive-over-conceptual scaffold ranking (b04) real? Single meta-analysis, overlapping intervals.

## 11. Sources

[V] opened; [M] snippet or memory only.

**Foundations and theory**
- [M] Wood, Bruner, Ross (1976) The role of tutoring in problem solving. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x (a01, a02, b26, d13; publisher PDF blocked twice)
- [V] Smit, de Kleijn, Wicherts, van de Pol (2025) What it takes to tutor: preregistered direct replication. https://doi.org/10.1037/edu0000965 (a03; abstract-level only; d15 could not open full text)
- [V] Klahr and Nigam (2004) Equivalence of learning paths. https://pubmed.ncbi.nlm.nih.gov/15447636/ (a04; abstract; 77/23 from memory, b25, d14)
- [V] Kirschner, Sweller, Clark (2006) Why minimal guidance does not work. https://doi.org/10.1207/s15326985ep4102_1 (a05-a11)
- [M] Hmelo-Silver, Duncan, Chinn (2007) https://doi.org/10.1207/s15326985ep4102_4 (a12, b23)
- [V] Clark, Kirschner, Sweller (2012) Putting students on the path to learning. https://www.aft.org/sites/default/files/GuidedInstruction.pdf (a13, a14)
- [M] Mayer (2004) Should there be a three-strikes rule. https://doi.org/10.1037/0003-066X.59.1.14 (b24)
- [M] van de Pol, Volman, Beishuizen (2010) https://doi.org/10.1007/s10648-010-9127-6 (b27)
- [M] Koedinger and Aleven (2007) https://doi.org/10.1007/s10648-007-9049-0 (b28)
- [V] Kalyuga and Renkl (2010) expertise reversal intro. https://link.springer.com/content/pdf/10.1007/s11251-009-9102-0.pdf (b18, b19; c24 is the same paper, snippet)

**Meta-analyses**
- [V] Alfieri, Brooks, Aldrich, Tenenbaum (2011). https://doi.org/10.1037/a0021017 (a15-a18; b21 memory duplicate)
- [V] Belland, Walker, Kim, Lefler (2017). https://doi.org/10.3102/0034654316670999 (a19, a20)
- [V] Belland, Walker, Kim (2017) Bayesian network meta-analysis. https://doi.org/10.3102/0034654317723009 (a21)
- [V] Kim, Belland, Walker (2018). https://link.springer.com/content/pdf/10.1007/s10648-017-9419-1.pdf (b01-b06, c21)
- [M] Lazonder and Harmsen (2016). https://doi.org/10.3102/0034654315627366 (b20)
- [M] Zosh et al. (2022). https://doi.org/10.1111/cdev.13730 (b29)

**LLM for humans**
- [V] Bastani et al. (2025) PNAS. https://doi.org/10.1073/pnas.2422633122 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ (a25, a26, b10, b11, c12, d12)
- [V] Kestin et al. (2025) Sci Rep. https://www.nature.com/articles/s41598-025-97652-6 (a27, b07-b09, c13, d11)
- [V] Lehmann, Cornelius, Sting (2025) https://arxiv.org/abs/2409.09047 (a28)
- [V] Wang et al. Tutor CoPilot. https://arxiv.org/abs/2410.03017 (a29, b14, c14)
- [V] Macina et al. (2023) MathDial. https://arxiv.org/abs/2305.14536 (a30)
- [V] LearnLM Team (2024). https://arxiv.org/abs/2412.16429 (a31, b17, c10)
- [V] Eedi and LearnLM (2025). https://arxiv.org/html/2512.23633v1 (c11)
- [V] Macina et al. (2025) MathTutorBench. https://arxiv.org/abs/2502.18940 (c07, c08)
- [V] Dinucu-Jianu et al. (2025). https://arxiv.org/abs/2505.15607 (c09)
- [V] Cohn et al. (2026) Evidence-Decision-Feedback. https://arxiv.org/abs/2602.01415 (b12, b13, c15, d10)
- [V] Amanlou et al. / Beyond Access (2026). https://arxiv.org/pdf/2606.01375 ; https://github.com/MohammadAmanlou/Guided-LLM-Scaffolding (b15, c16)
- [V] Fischer, Rau, Rilke (2025). https://docs.iza.org/dp18338.pdf (c17)
- [V] Pardos and Bhandari (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11125466/ (c18)
- [V] Hou et al. (2026) CoMeT. https://arxiv.org/abs/2609.22993 (d09)

**LLM as solver or learner**
- [V] Zhou et al. (2023) least-to-most. https://arxiv.org/abs/2205.10625 (a22-a24, b16, c19, c20, d01)
- [V] Zhang et al. (2025) Scaf-GRPO. https://arxiv.org/abs/2510.19807 (c01-c03, c22, c25)
- [V] Li et al. (2026) QuestA. https://arxiv.org/abs/2507.13266 (c04, c05)
- [V] SEELE (2025). https://arxiv.org/abs/2509.06923 ; https://arxiv.org/html/2509.06923v1 (c06, d16)
- [V] Meincke et al. (2025) Prompting Science Report 2. https://arxiv.org/abs/2506.07142 (d02)
- [V] Revisiting CoT: zero-shot can be stronger than few-shot (2026). https://arxiv.org/abs/2506.14641 (d03)
- [V] Innate reasoning is not enough (2025). https://arxiv.org/abs/2503.19602 (d04)
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948 (d05; read to char 100,000 of 142,000)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d06)
- [V] Dong et al. (2026) Pay for hints, not answers. https://arxiv.org/abs/2601.22132 (d07)
- [V] HintMR (2026). https://arxiv.org/abs/2604.12229 (d08)

**Not opened:** Wood et al. 1976 (numbers), Klahr and Nigam full text, Smit Bayes factors, Hmelo-Silver 2007, Lazonder and Harmsen, Zosh, Mayer 2004, van de Pol, Koedinger and Aleven, Tuovinen and Sweller 1999, Clark 1989, Belland 2015.
