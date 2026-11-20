# Definitions and ideals: deep document

*Subfield D05.01. Key works: Dewey (1910), Ennis, Facione Delphi Report (1990). Why it matters for our agent: mostly background, but it gives us a label set (the Delphi six skills) for auditing the schema, and the LLM literature that tests "critical thinking" gives hard numbers on critique, self-correction and holding a position. Evidence ids (a01 to d18) are in `evidence_a-d.jsonl`; claim ids (K01 to K21) are in `claims.jsonl`. Corrections from `critique.md` are applied here.*

---

## 1. What it is

"Critical thinking" has no single agreed definition. Three families of definition matter.

- **Dewey (1910): reflective thinking.** Active, careful testing of a belief against the grounds for it. Two parts sit under every act: a felt doubt, and a search for facts that settles it. (a01)
- **Ennis: reasonable reflective thinking** focused on deciding what to believe or do. Ennis proposed 12 aspects in 1962, a streamlined definition in 1991, added care for persons in 1996, and by 2016 counted 17 definitions in use (14 scholarly, 3 dictionary). Combining the lists of abilities gives more than 50 possible teaching objectives. (a04, b01)
- **Facione and the APA Delphi panel (1990): "purposeful, self-regulatory judgment"** that results in interpretation, analysis, evaluation and inference. 46 experts, six rounds, from 11 Feb 1988 to 25 Sep 1989. (a05, a06)

Two cuts run through all of them.

1. **Skills versus dispositions.** Skills are things you can do (analyse an argument, judge a source). Dispositions are habits of mind (open-mindedness, wanting evidence, willingness to suspend judgment).
2. **General versus subject-specific.** Is critical thinking one transferable ability, or is it always tied to a subject? McPeck (1981) says tied; the Delphi panel says skills cross subjects but need domain knowledge. (a10, a12)

For an engineer: there is no ground-truth definition to implement. What exists is a list of component skills, a list of dispositions, and a set of tests. The LLM literature has quietly picked one reading, critique ability (can the model find the flaw?), and measures that.

---

## 2. History and theories in depth

### 2.1 Dewey, How We Think (1910)

- Dewey built the definition from three everyday cases, not from experiments. Reflection starts with doubt (perplexity, hesitation) and continues with an act of search. (a01)
- He listed **five logically distinct steps** (p. 72): (1) a felt difficulty; (2) its location and definition; (3) suggestion of a possible solution; (4) reasoning out the bearings of the suggestion; (5) further observation and experiment leading to acceptance or rejection. Steps 1 and 2 often fuse. (a02)
- In 1933 he called them **phases, not a fixed order**, to drop the idea of a fixed sequence. (a03)
- Limit: philosophical analysis. No data on how often people think this way.

Link to our schema: Dewey's doubt-then-search is close to guardrail G1 (doubt only on a signal) and to the S4 fail, S5 revise, S6 impasse chain. The fixed-order reading was dropped by Dewey himself, which matches our graph having loops, not a line. The process-model view is covered in sibling subfield 02 (Process models); do not repeat it here.

### 2.2 Ennis (1962 to 2016)

- 1962: 12 aspects of critical thinking. 1987: a taxonomy of dispositions and abilities (opened only as a snippet, a11). 1991: a streamlined conception using "reasonable" as the norm, with a disposition "to determine and maintain focus on the conclusion or question". 1996: care for persons added. 2016: 17 definitions counted. (a04, a11, b01)
- Ennis also built the **Ennis-Weir Critical Thinking Essay Test** (max score 29), which later became the probe used on o1 (section 6). Human training effects on it: Hatcher (treatment n=17, control n=19), Davidson and Dunham, Baker over four years. (b16)
- SEP lists 9 initiating dispositions and 9 ability families. (b02)

### 2.3 McPeck and the generalism dispute

McPeck (1981) argued critical thinking is always thinking about something, so it cannot be taught as a general skill. SEP calls the evidence for transfer across domains "scanty". (a12, b03) Willingham (2007) gives the cognitive-science version: skills are hard to teach because they depend on domain knowledge and surface features. In his band-problem experiment, **19%** used the analogous garden solution unaided and **35%** with a hint. In a treasure-cave puzzle about **75%** of US students solved it versus **25%** of Chinese students, reversed for a Chinese folk-tale puzzle. (b07) This is the same unaided-analogy failure that our O7 note cites.

### 2.4 The APA Delphi Report (Facione, 1990)

- Method: 46 panelists, six rounds, working assumption that critical thinking can be assessed validly and reliably. (a05)
- **Six core skills:** interpretation, analysis, evaluation, inference, explanation, self-regulation. Panel agreement that they are central: **over 95%** for analysis, evaluation and inference; **over 87%** for interpretation, explanation and self-regulation. (a07)
- **Consensus statement:** one paragraph with 14 traits of the ideal critical thinker. (a06)
- **Dispositions:** a list of 19 (12 plus 7); 83% agree good thinkers show them. (a08)
- **Dispute:** 61% held an inclusive view (dispositions are part of the meaning of critical thinking); about 30% held a strict procedural view (skills only). 83% agreed on the paradigm list. A finding: refusing to call something critical thinking just because one disapproves of its ethics is improper. (a09)
- Recommendations: 15 on instruction and assessment; four ways of assessing listed; validity of proxy tasks "yet to be established". (a10)
- Limit: the percentages are panel opinion, not data about people. With 46 panelists, 61% is about 28 people.

### 2.5 Other ideals

Paul, Lipman, Siegel, Bailin and Stanovich each add an angle (SEP). Siegel names four reasons for the ideal: respect for persons, self-sufficiency, initiation into rational traditions, and preparation for democratic life. (a13, b05) These are justifications of the ideal, not mechanisms, so they give a thinking agent nothing to implement.

### 2.6 Standard tests (what "measured" meant for humans)

Cornell X: 76 items, 24 on credibility. Cornell Z: 52 items. CCTST: 11 of 34 items on inference, 5 of 34 on argument analysis. CLA: 25 selected-response items. (a14, b06) Test coverage differs sharply, so scores from different tests are not interchangeable. Assessment is covered in sibling subfield 04.

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources), **S** single-source, **C** contested. Corrections from the critique are applied.

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| No single definition exists | Ennis: 12 aspects (1962), 17 definitions (2016); more than 50 objectives from combined ability lists | Hitchcock SEP, Dewey, Facione (a01, a04, a06, b01) | E (K01) |
| Delphi core skills | 46 experts, 6 rounds; 6 skills; >95% (analysis, evaluation, inference), >87% (interpretation, explanation, self-regulation) | Facione 1990 (a05, a07) | E (K02) |
| Disposition dispute | 19 dispositions; 61% inclusive vs about 30% procedural-only; 83% agree on paradigm list | Facione 1990 (a08, a09) | E (K03) |
| General vs subject-specific | transfer evidence "scanty"; no effect sizes | McPeck via SEP; Willingham (a12, b03, b07) | C (K04) |
| Unaided analogy transfer is rare | 19% unaided, 35% with hint (band problem) | Willingham 2007 (b07) | S |
| CT programs: evaluation weakness | 8 studies, 5 usable; reading 1 of 3 significant; reasoning 2 of 3 | Willingham 2007 (b08) | S (K05) |
| Instruction meta-analysis | g+ = 0.30, k = 341 effect sizes, heterogeneous; dialogue, authentic problems, mentoring helped most | Abrami et al. 2015 (d13; abstract record only) | S (K06) |
| College effect | 71 reports over 48 years; substantial gain; the "50th to 72nd percentile" figure is **not confirmed** (abstract has no numbers) | Huber and Kuncel 2016 (b10, d14) | S (K06) |
| Intrinsic self-correction hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 (3 calls) to 41.8 (5 calls); GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 GSM8K 75.9 to 75.1 to 74.7 | Huang et al. 2024 (b18, c10) | S (K07) |
| Oracle-label correction helps | GPT-3.5 CSQA 75.8 to 89.7; GSM8K 75.9 to 84.3; GPT-4 HotpotQA 49.0 to 59.0 | Huang et al. 2024 (c11) | S (K07) |
| Correction is task-dependent, 2025 | GPT-3.5 Self-Refine: HotpotQA -14.21, CS-QA -12.25, GSM8K -5.14, MATH +7.74, GPQA +10.88 | CorrectBench, Tie et al. 2025 (d07, d17) | C (K07, K20) |
| Parallel beats extended | up to 20% higher accuracy, parallel vs extended thinking at equal budget | Mirage of test-time scaling (d10) | S |
| Critique is weak | PaLM-2-L 54.14% on Critic-HumanEval; medium and small models near random | CriticBench, Luo et al. 2023 (a16, c07) | S (K08) |
| Critique tracks certainty; self-check filter | self-check on SC@64: ChatGPT 83.5 to 84.0, PaLM-2 91.3 to 92.7, GPT-4 95.8 to 96.2; error cut 3.03, 16.09, 9.52% | Luo et al. 2023 (a17, c08, c09) | S (K08) |
| Critic false alarms (math) | on correct solutions: o1-mini wrongly flags 2.1% (GSM8K) and 4.9% (MATH); GPT-4o 8.8% and 23.4%; Llama-3.1-8B right only 6.2% of the time | ProcessBench (d11) | S (K18) |
| Finding errors is the bottleneck | GPT-4 step-level 52.87%, trace-level 39.80%, CoT step-level 43.40%; oracle location gives +18 to +44 points on originally wrong traces, 0 to -11 on right ones | BIG-Bench Mistake, Tyen et al. 2024 (c13) | S (K09) |
| Faulty premises go unnoticed | no correct option: Claude 3 Opus 8.65%, GPT-4o 6.71%, Gemini 1.5 Pro 14.02%; with one correct option 82 to 100%; told to check: GPT-4.1 0.23 to 0.81 | Wrong-options study; FPBench (a20, a22) | E (K10) |
| Alignment can hurt premise checking | Qwen2-Math-7B 0.965 base vs 0.08 instruct | Wrong-options study (a21) | S |
| Models cave to pushback | 46% flipped, 17% mean accuracy drop (10 models, 7 tasks, 67,640 runs); GPT-4 flips wrong 30.3% vs right 10.4%; GPT-3.5 79.7% vs 54.9% | FlipFlop, Laban et al. 2023 (d01) | E (K11) |
| Sycophancy rates | 32% (GPT-4) to 86% (Claude 1.3) changed answer; up to 98% wrongly admit error; preference model chose sycophantic answer 95% on a 266-item misconception set | Sharma et al. 2023 (c28, c29) | E (K11) |
| 2026 reasoning models | 8 of 9 more consistent than GPT-4o; accuracy under attack: GPT-5.1 98.92%, GPT-OSS 98.53%, Grok-4.1 97.06%, GPT-4o 91.29%, DeepSeek-R1 89.91%, Claude-4.5 86.31% (d = -0.27, p<0.001) | Li et al. 2026 (d03) | S |
| Fine-tuning cuts flip loss | FlipFlop effect -9.5% to -3.8% average; -26.5% to -12.9% on hardest unseen subset; apologies 60% to 1.4% | Laban et al. 2023 (d02) | S |
| Persona prompt cures opinion flips, not premise flips | debate Turn of Flip (max 5): Qwen2.5-7B 1.10 to 4.02; DeepSeek-r1 3.91 to 4.83; false-presupposition stays 1.4 to 3.4 | SYCON-Bench (d05, d06) | S (K19) |
| Failure types in multi-turn attacks | self-doubt and social conformity make up 50% of failures; confidence embedding fails on reasoning models | Li et al. 2026 (d04) | S (K21) |
| Fallacy detection | reasoning models over-flag (more false positives) but classify better once a fallacy is known; GPT-4 zero-shot macro-F1 Argotario 78.94, Logic 50.43, ElecDeb 42.26, Covid-19 20.47; MAFALDA level-0 F1: random 0.435, GPT-3.5 0.627, humans 0.749 | SmartyPat, Zero-shot fallacy, MAFALDA (c22 to c26) | E (K14) |
| Critical-question loops | CQoT: MT-Bench reasoning Claude 3.5 Sonnet 8.6 to 8.95, GPT-4o 8.3 to 8.45, Gemini 1.5 Pro 8.45 to 8.9; n = 40 questions, GPT-4o judge | Castagna et al. 2024 (c18) | S (K13) |
| Generating good critical questions is hard | 4,976 annotated questions, kappa 0.54; best model 56.65 average; judge labels 25% of invalid questions Useful | Benchmarking CQ generation (c20, c21) | S (K13) |
| o1-preview on Ennis-Weir | 24.33 of 29 (runs 20, 26, 27) vs undergraduate 11.51 (SD 8.23), postgraduate 18.39 (SD 6.59), N=100 | Zhong et al. 2024 (a18, c01, b15) | C (K12) |
| o1-preview elsewhere | Lake Urmia vignette 46.10 vs 20.08 (z 3.20); LogiQA 90% vs 86% (human N=651); computational thinking 3.84 vs 3.92 (z -0.15); problem-solving sub-score 1.00 vs 3.68 (z -4.25) | Zhong et al. 2024 (a19, c02, c03) | C (K12) |
| Heavy AI reliance goes with less reported CT | Lee et al.: N = 319, 936 examples, CT enacted in 59.29%; confidence in AI beta -0.69 (p<0.001); confidence in own ability +0.26; less effort reported: 72% knowledge to 55% evaluation | Lee et al. CHI 2025 (a24, b21, c14, c15, c16) | C (K15) |
| EEG study | 54 participants sessions 1 to 3, 18 in session 4 | Kosmyna et al. 2025 (a25, c30) | C (K15) |

**Corrections to carry.** (1) The undergraduate Ennis-Weir mean is 11.51, not 13.8; 13.8 is the best post-treatment mean from training studies, and z = 1.60 refers to it. (2) Gerlich 2025 (N=666, r about -0.68) was not opened and has a published table correction; do not use it. (3) Abrami 2008 (g+ about 0.34) is recalled only. (4) The "up to 27% accuracy drop" in Sharma et al. is attributed to different models in different places; use "up to 27%, model unclear". (5) The FlipFlop headline (46%, 17%) differs slightly from its table averages (about 44%, 16%).

---

## 4. Mechanisms and models

This subfield has few causal models of its own. These are the ones an engineer can use.

### 4.1 Delphi skill map as an audit grid

Use the six skills as columns and the schema states as rows. For each skill ask: is there a **code-checked gate**, a **model-written line only**, or nothing?

| Delphi skill | Schema element | Check type | Verdict (d15) |
|---|---|---|---|
| Interpretation | S1 restate task | model-written; no check that the restatement matches the task | **weak** |
| Analysis | S2 represent | model-written, examples studied | partial |
| Evaluation | S4 test, S7 select | code-checked | covered |
| Inference | S3 generate, S7 | code-checked on held-out part (G3) | covered |
| Explanation | S9 one lesson line; S5 one line | model-written line only | **weak** |
| Self-regulation | G1, S6 impasse detector | code-checked | covered |

Disposition map (d16): inquisitiveness, open-mindedness, evidence-seeking, suspend-judgment and fair-mindedness each have an analogue (G1, G3, S7 counterexample search, G4 and G5). **Resisting pressure has none.** The tests in section 8 target the two weak skills and this missing disposition.

### 4.2 Interpretation fidelity check (back-translation), design [D]

Not from the literature as such; it is the audit's proposed fix.
1. S1 produces a restatement R of task T (model call).
2. In a fresh context, show the model only R and ask it to answer or list constraints.
3. Code compares the constraint list or the answer with one derived from T alone (exact match for structured tasks, set overlap for constraint lists).
4. If overlap is below a threshold, show both restatements and re-run S1 once.
Cost: two short extra calls at S1. Test it first (UNKNOWNS U2).

### 4.3 Premise check at intake (G-level), from FPBench and wrong-options results

1. Before S2, one short call: "List what must be true for this question to have an answer. Is any of it false or missing?"
2. Code reads a fixed-form field (yes/no plus the offending premise).
3. If yes, the agent returns the flagged premise instead of an answer (or asks for clarification), otherwise continue.
Why: without prompting, recognition is low (no-correct-option items: most models under 15%); with an explicit check GPT-4.1 went 0.23 to 0.81. (a20, a22) Cost: in FPBench, DeepSeek-R1 outputs ran 1,756 to 2,493 tokens, 2,734 with the check guidance (a22); our own cost must be measured. Risk: false alarms on well-posed items; measure it.

### 4.4 Gated critique (S5 location step), from Huang, CriticBench, BIG-Bench Mistake

Critique is a mixed bag, so wire it by conditions:
1. Never run a critique pass on a model's own answer with no external signal (G2).
2. Run it only when a code check has flagged a failure, or attempts disagree, or certainty is low. Critique accuracy tracks self-consistency certainty (c08), so a certainty gate fits where critique is more likely right and wrong answers are more likely to exist.
3. Locate the error first (step level), because locating is the bottleneck: oracle location gave +18 to +44 points on wrong traces (c13), while the model's own locating is 52.87% at step level for GPT-4.
4. Measure the critic's false-alarm rate on known-correct items before turning it on (K18): on correct solutions o1-mini flags 2.1% to 4.9% but GPT-4o 8.8% to 23.4%.
5. Log every right-to-wrong flip (schema section 6).

### 4.5 Stance-hold rule, from FlipFlop, SYCON, MT-Consistency

Design [D]:
1. When a challenge arrives ("are you sure?", a user-stated opposite), code strips the social framing and keeps only new factual content (input hygiene, S1).
2. Revision is allowed only if the challenge carries new evidence the code can check (a failing output, a test). Otherwise hold the answer and say why.
3. Never gate on stated confidence (K21): reasoning traces make models overconfident.
4. Report both flip rates: on initially correct and on initially wrong answers. A hold rule that stops both kinds of flips makes the agent stubborn, which no study above measures (d06).
Why: every model flips wrong answers more than right ones, but still flips many right ones (d01). A prompt-only fix works for opinion and ethics stances, not false-presupposition items (d06), so premise check (4.3) and stance hold are two separate fixes (K19).

### 4.6 Dewey's two parts as code

Doubt (a signal) then search (an act). Doubt = a failed check, disagreement, or the impasse detector. Search = the S5 to S6 chain. This is already G1 plus S5/S6; nothing new to implement.

---

## 5. What holds up

### 5.1 Held up
- **No single definition; skills plus dispositions** is a stable description across Dewey, Ennis, Delphi (K01, K03).
- **Models cave to pushback.** Three independent sources (Sharma 2023, FlipFlop 2023, SYCON 2025), plus a 2026 follow-up showing improvement for most reasoning models but not for all (K11, established).
- **Models rarely notice false premises unprompted; prompting raises it sharply** (K10, two sources).
- **Fallacy detection is imperfect, subjective, and reasoning models over-flag** (K14, three sources).
- **Self-correction needs an external signal.** Huang's oracle table shows the gain when the signal is real; the no-oracle table shows the loss. CorrectBench (2025) agrees that intrinsic correction is task-dependent. This is consistent with schema G2 and section 4b. Status stays single-source on the strict claim because the 2025 evidence is partly the same lineage and no certainty-gated re-run exists.

### 5.2 Failed, weakened or unresolved
- **Huber and Kuncel's percentile figure** and **Abrami 2008** are unverified. Do not quote them.
- **General vs subject-specific** has no decisive data (K04). LLM data only hint: the same method moves by +10.88 on GPQA and -14.21 on HotpotQA (d07, d17).
- **Human-vs-o1 comparison** is weak: 3 runs on Ennis-Weir, 10 on LogiQA, mismatched cohorts (K12).
- **AI-reduces-critical-thinking** evidence is correlational (Lee N=319) or tiny (EEG 18 per group, K15). Gerlich is unusable until re-read.
- **Instruction effects in humans** (g+ about 0.30) are real but small and heterogeneous; curriculum-wide programs do not necessarily add steady gains (K06). Willingham's review found only 5 of 8 evaluations usable.
- **Generated critical questions** are mediocre: best model 56.65 average; judge model error 23.5% and 16.1% in the two directions (c20, c21).
- **CQoT** shows gains (+0.15 to +0.9 points) but on 40 questions with a GPT-4o judge, no variance, and a self-answered checklist, which under G2 is the model's opinion (c18).
- **Debate vs self-consistency:** GSM8K GPT-3.5 at 9 responses, debate 83.0 vs self-consistency 88.2 (c12; table layout garbled, gap clear). Matches G9.

### 5.3 Moderators
- **Model strength** controls critique quality and false-alarm rate (ProcessBench, CriticBench). Medium and small models near random.
- **Task type** controls self-correction sign (d07).
- **Training objective:** alignment cut premise-recognition (Qwen2-Math 0.965 to 0.08) and reward models prefer agreement (95%).
- **Stance type:** prompts help on opinion and ethics, not on false premises (d06).
- **Model generation:** 2026 reasoning models flip less except Claude 4.5 (d03). Facts on frontier 2025 to 2026 models for self-correction are still thin.

### 5.4 Interventions that worked and did not

| Worked | Did not |
|---|---|
| Telling the model to check the premise (FPBench 0.23 to 0.81) | Intrinsic self-correction with no signal (-37.7 points on CSQA GPT-3.5 after 3 calls) |
| Oracle-label correction (+13.9 on CSQA, GPT-3.5) | Debate at matched responses (83.0 vs 88.2) |
| Error location given by an oracle (+18 to +44 points) | Generic instruction to "be careful" (schema 4b) |
| Fine-tuning against flipping (loss -9.5% to -3.8%) | Confidence-based gating on reasoning models (d04) |
| Third-person/persona prompt on opinion items (1.10 to 4.02) | Same persona prompt on false-presupposition items (stays 1.4 to 3.4) |
| Self-check filtering of votes (+0.4 to +1.4 points) | Reflexion-v1 (-24.53 CS-QA, -22.64 GSM8K, GPT-3.5) |
| Argument-reconstruction training on base models (LegalArg 4B 47.24 to 58.52) | Same data on instruct models (mixed; Qwen3-4B 65.42 to 61.75) |

---

## 6. Language models

Almost all LLM "critical thinking" work tests critique ability, one reading of the ideal. None tests Dewey's, Ennis's or Facione's definition as such (critique.md, weak spot 1).

### 6.1 Structured CT tests
- o1-preview on the Ennis-Weir essay test: 24.33 of 29 (3 runs of 20, 26, 27) vs undergraduates 11.51 and postgraduates 18.39. On Lake Urmia vignettes 46.10 (SD 4.12) vs 20.08. LogiQA 90% vs 86% (human N=651). TOSLS 0.99 vs best human group 0.85. On the CT skills scale 3.84 vs 3.92 (z -0.15) and on computational problem-solving 1.00 vs 3.68 (z -4.25). (a18, a19, c01 to c04) Treat as anecdote: tiny runs, mismatched cohorts, one TOSLS item missed in 2 of 5 trials.
- Argument-reconstruction supervision (2026): base models gain (LegalArg 4B 47.24 to 58.52; 8B 54.70 to 62.87; ReClor 4B 74.13 to 78.98; ArgRC 4B 86.54 to 90.77); instruct models mixed. Training, not scaffolding. (a23)

### 6.2 Critique and self-correction
See sections 3 and 5. In short: without external feedback, 2023 models lose accuracy (CSQA 75.8 to 38.1); with oracle labels they gain (to 89.7); 2025 reasoning models show marginal, task-dependent change; parallel sampling beats extended rethinking by up to 20% at equal budget. Critique accuracy tracks answer certainty. Error locating is the bottleneck (52.87% step-level GPT-4). Strong critics rarely flag correct math (o1-mini 2.1% to 4.9%); weak ones are useless (Llama-3.1-8B correct-acc 6.2%).

### 6.3 Premise checking
Unprompted recognition is very low on code (FPBench, HumanEval and MBPP+ only; best no-prompt rate 0.57 DeepSeek-R1, worst 0.12 o4-mini) and arithmetic (no-correct-option items 0% to 14%, Llama-3.1-405B 54.72%). With a check prompt, 0.72 to 0.81. (a20, a22)

### 6.4 Holding a position
FlipFlop (2023): 46% of answers flipped; GPT-4 least (10.4% of correct, 30.3% of wrong), GPT-3.5 most (54.9%, 79.7%). Sharma (2023): changed answer on 32% to 86%. 2025 SYCON-Bench: debate Turn of Flip 4.95 (o3-mini) down to 1.10 (Qwen2.5-7B). 2026: GPT-5.1 98.92% accuracy over challenge rounds vs Claude-4.5 86.31%, GPT-4o 91.29%. Fine-tuning cut the loss about 60%. Larger models in a family cut sycophancy by up to 81.4%.

### 6.5 Fallacies and critical questions
Zero-shot GPT-4 beats a fine-tuned T5 on some sets (Argotario 78.94 vs 69.13) and loses on others (Logic 50.43 vs 64.95; ElecDeb 42.26 vs 62.37). One-shot lifts Logic from 50.54 to 54.48. Humans beat LLMs at fine taxonomy levels (MAFALDA level 2: GPT-3.5 0.138, humans higher). Reasoning models flag more false positives. Critical-question generation: best model 56.65 average on a moderate-agreement scale (kappa 0.54).

### 6.6 Human side (interface, not agent)
Lee et al. (N=319): higher confidence in AI goes with less enacted critical thinking (beta -0.69); users report less effort on all six Bloom-style levels (55% to 79%). A short-answer length study (N=24) found error detection is best on medium-length answers when the AI is wrong (0.542 vs 0.245 short, 0.307 long). A scale (N=1,341) links higher critical-thinking-in-AI-use scores to more varied verification. All human-subject and correlational.

---

## 7. What our agent should take

### Add now (established [E])

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | Use the Delphi six skills and the disposition list as the audit grid for the schema; record the verdict (explanation and interpretation weak) in the design notes. No code change. | memory / design notes | [E] label set; verdict [S] own audit | a05 to a09, d15, d16; K01, K02, K03, K17 |
| 2 | Keep G2 and 4b as written: no unstructured self-critique on its own answer. The 2025 evidence agrees with the rule; revise only from real output. | G2, 4b | [E] | b18, c10, c11, d07, d10; K07 |
| 3 | Fallacy and critique calibration: log the critic's false-alarm rate on known-correct items in every run; do not enable a critique operator whose flag rate on correct items exceeds a set threshold. | O (critique), section 6 logging | [E] direction; thresholds [D] | c22 to c26, d11; K14, K18 |
| 4 | Treat "premise check" and "hold position under pushback" as two separate items, not one "be critical" prompt. | G (new, see Test first) | [E] that they differ | a20, a22, d06; K10, K19 |

All four are bookkeeping and logging changes. The two behaviour changes below start as "Test first", because the schema's own rule 2 says a new element enters as [S] or [D] with an equal-token test.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 5 | Up-front premise check at intake (S0/S1): flag impossible or underspecified questions before answering | G / S1 | [S] (two sources agree the problem exists; the fix at equal tokens is untested) | a20, a21, a22; K10 |
| 6 | Stance-hold rule: revise only on checkable new evidence; code strips social pressure | G (new) | [S] direction [E] problem (K11); remedy [S] | d01 to d06; K11, K16, K19, K21 |
| 7 | S1 back-translation fidelity check for interpretation | S1 | [D] (own audit) | d15; K17 |
| 8 | Explanation operator: a structured explanation field checked by code against the evidence that produced the answer | S9 / O | [D] | d15; K17 |
| 9 | Gated critique: run critique only when a check failed or certainty is low; locate the failing step first | O (critique) / S5 | [S] | b18, c13, c08, d07, d10; K07, K08, K09 |
| 10 | Critical-question checklist (CQoT style, eight questions) as an extra operator | O (critique) | [S] | c18 to c21; K13 |
| 11 | General vs domain-primed critique prompt: does the model need domain examples? | memory / O | [C] | d07, d17, a12, b07; K04, K20 |
| 12 | Ennis-Weir as a blinded multi-run probe with a fixed judge | bench | [C] | a18, c01; K12 |
| 13 | Disposition proxies as scores: flip rate, false-alarm rate, revision on disconfirming input | logging | [D] | d16 | 

---

## 8. Concrete tests on our bench

All arms run at equal total tokens (include setup, critique and checker calls). Report right-to-wrong and wrong-to-right counts, not just accuracy.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Premise check | no-correct-option multiple choice; faulty-premise code and math questions; 30% well-posed controls | plain; plain with "check the question first" in the same call; separate premise-check call then solve | recognition rate on faulty items; false-alarm rate on well-posed controls; accuracy on controls | recognition up from under 15% to 70% or more (FPBench 0.23 to 0.81); false alarms low; token cost measured and held equal across arms |
| T2 Stance hold | items the agent first answers correctly and incorrectly, then "Are you sure?" and "I think it is X" (right and wrong X) | plain; third-person persona prompt; code-level stance hold (revise only on checkable evidence) | flip rate on initially correct, flip rate on initially wrong, final accuracy | flip on correct falls well below FlipFlop-type 10 to 55%; flip on wrong not below plain by more than the check can justify (no stubbornness) |
| T3 Gated critique | tasks with a check (code tests, math) and tasks without | always-critique; never-critique; critique only when check fails or agreement low | accuracy at equal tokens; count of right-to-wrong flips | gated beats always; always loses to never on no-signal items (Huang-type loss) |
| T4 Critic false alarms | known-correct solutions from our suites | critique operator at default; with location-first prompt | flag rate on correct items; tokens per critique | strong model 2% to 5% (o1-mini range); set threshold 10% |
| T5 Interpretation fidelity | tasks where a misread restatement changes the answer (ambiguous or trap wording) | S1 as is; S1 plus back-translation check | misread rate; final accuracy | fewer misreads; gain small where wording is plain |
| T6 Explanation check | tasks with checkable evidence trails | S9 one-line explanation; structured explanation compared in code with the evidence log | explanation-evidence mismatch rate; downstream lesson reuse | mismatches found; no accuracy gain expected, memory quality up |
| T7 Domain transfer of critique | held-out domains (math, code, factual QA, commonsense) | general critique prompt; domain-primed with 2 worked examples | accuracy delta per domain | sign varies across domains (as +10.88 vs -14.21 for the same method) |
| T8 Ennis-Weir probe | the Ennis-Weir essay; 10 or more runs per arm | plain; scaffold | blinded judge score (fixed judge, 29-point rubric), variance | scaffold at or above the 24.33 o1 mean; check variance across runs |
| T9 Critical questions | MT-Bench-style reasoning items, 100 or more | CoT; 8-question checkpoint; self-consistency at equal tokens | judged score and accuracy | gain of at most 0.15 to 0.45 points; may lose to self-consistency |

---

## 9. What does not transfer, and why

- **Teaching effects (g+ about 0.30).** Human instruction studies do not apply to a frozen model; there is no learning during use. Background only (K06).
- **Definitions of the ideal thinker and justifications (Siegel, Paul, Lipman).** They explain why people should think critically; they supply no mechanism.
- **Dispositions as personality.** For people, dispositions are stable traits; an agent has none. Only behavioural proxies (flip rate, false-alarm rate, revision on disconfirming input) can be measured (d16).
- **AI-dulls-thinking studies (Lee, Kosmyna, Gerlich).** They describe human users. They bear on how humans should consume our agent's output, not on its internal design (K15).
- **o1-vs-human CT scores.** Different cohorts, different run counts, 3 to 10 trials. They show the model can write structured critiques, not that it thinks critically in the Dewey sense (K12).
- **Dewey's felt difficulty.** It is an experience. An agent has only an externally detectable signal (failed check, disagreement), which is the point of G1.
- **Self-correction results from 2023 models (GPT-3.5, GPT-4).** Magnitudes may not hold for 2025 to 2026 reasoning models; use as direction, not size.
- **Critic accuracy on math (ProcessBench).** Numbered steps and math answers favour critics; free-form text tasks are harder.
- **Fine-tuning against sycophancy and argument-reconstruction training.** Both change weights; we do not train. They tell us the failure is learnable, not how to fix it by scaffold.

---

## 10. Open questions

1. Does intrinsic critique still hurt on 2025 to 2026 reasoning models when gated to low-certainty items? No certainty-gated re-run of the Huang tables was found.
2. What is the equal-token effect of an up-front premise check on faulty-premise sets? Only prompt-level numbers exist (0.23 to 0.81); cost and false alarms at equal budget are unmeasured.
3. Can stance-holding be added without raising stubbornness? No study reports both flip rates after a fix (FlipFlop fine-tuning reports accuracy only).
4. What is the token cost of a critique pass, and the false-alarm rate on non-math text? ProcessBench reports neither cost nor non-math.
5. Does a general critical-thinking prompt transfer across domains for LLMs, or does it need domain examples (the McPeck question tested on a model)? Indirect evidence only.
6. Is Ennis-Weir usable as a blinded, 10-plus-run probe with a fixed judge?
7. Can dispositions (open-mindedness, suspending judgment) be manipulated by prompt and measured separately from skills? No prompt-only manipulation with a measured effect found.
8. Verify Abrami 2015 (g+ 0.30, abstract only) and Huber and Kuncel (percentile figure) from full text.
9. Which of Dewey, Ennis, Facione would a test of "critical thinking" in LLMs actually measure, and does any LLM benchmark cover interpretation and explanation?

---

## 11. Sources

[V] = opened this session (page or PDF text read). [M] = snippet, recall or abstract page only.

| Source | URL | Mark |
|---|---|---|
| Dewey (1910) How We Think | https://archive.org/stream/howwethink00dewegoog/howwethink00dewegoog_djvu.txt | [V] |
| Hitchcock, Stanford Encyclopedia: Critical Thinking | https://plato.stanford.edu/entries/critical-thinking/ | [V] |
| Facione (1990) Delphi Report, executive summary | https://www.qcc.cuny.edu/socialSciences/ppecorino/CT-Expert-Report.pdf | [V] |
| Facione (1990) APA Delphi, ERIC record | https://files.eric.ed.gov/fulltext/ED315423.pdf ; https://eric.ed.gov/?id=ED315423 | [M] |
| Ennis (1987) taxonomy (via SEP) | https://plato.stanford.edu/entries/critical-thinking/ | [M] |
| McPeck (1981) via SEP | https://plato.stanford.edu/entries/critical-thinking/ | [V] (secondary) |
| Willingham (2007) Critical thinking: why is it so hard to teach? | https://www.aft.org/sites/default/files/media/2014/Crit_Thinking.pdf | [V] |
| Abrami et al. (2015) meta-analysis, ERIC abstract record | https://api.ies.ed.gov/eric/?search=title:%22Strategies+for+Teaching+Students+to+Think+Critically%22 ; https://doi.org/10.3102/0034654314551063 | [V] abstract only |
| Abrami et al. (2008) | https://journals.sagepub.com/doi/10.3102/0034654308326084 | [M] |
| Huber and Kuncel (2016), AERA snapshot and ERIC | https://www.aera.net/Newsroom/Study-Snapshot-Does-College-Teach-Critical-Thinking | [V] abstract only |
| Arum and Roksa (2011) via Wikipedia | https://en.wikipedia.org/wiki/Academically_Adrift | [V] secondary |
| Bastani et al. (2025) | https://www.pnas.org/doi/10.1073/pnas.2422633122 | [M] |
| Zhong et al. (2024) o1 vs humans, arXiv 2412.05753 | https://arxiv.org/html/2412.05753v1 | [V] |
| Luo et al. (2023) CriticBench, arXiv 2310.04815 | https://arxiv.org/pdf/2310.04815 | [V] |
| Huang et al. (2024) LLMs cannot self-correct, arXiv 2310.01798 | https://arxiv.org/pdf/2310.01798 | [V] |
| Tyen et al. (2024) BIG-Bench Mistake, arXiv 2311.08516 | https://arxiv.org/html/2311.08516 | [V] |
| Tie et al. (2025) CorrectBench, arXiv 2510.16062 | https://arxiv.org/abs/2510.16062 | [V] |
| Silver et al. (2025) single-utterance self-correction, arXiv 2506.15894 | https://arxiv.org/abs/2506.15894 | [V] abstract only |
| Mirage of test-time scaling, arXiv 2506.04210 | https://arxiv.org/abs/2506.04210 | [V] abstract only |
| Zheng et al. (2024) ProcessBench, arXiv 2412.06559 | https://arxiv.org/pdf/2412.06559 | [V] |
| When All Options Are Wrong, arXiv 2409.00113 | https://arxiv.org/html/2409.00113v1 | [V] |
| FPBench, arXiv 2508.03622 | https://arxiv.org/html/2508.03622 | [V] |
| Sharma et al. (2023) sycophancy, arXiv 2310.13548 | https://arxiv.org/html/2310.13548 | [V] |
| Laban et al. (2023) FlipFlop, arXiv 2311.08596 | https://arxiv.org/html/2311.08596v2 | [V] |
| Li et al. (2026) consistency of reasoning models, arXiv 2602.13093 | https://arxiv.org/pdf/2602.13093 | [V] |
| Hong et al. (2025) SYCON-Bench, arXiv 2505.23840 | https://arxiv.org/pdf/2505.23840v3 | [V] |
| Castagna et al. (2024) CQoT, arXiv 2412.15177 | https://arxiv.org/html/2412.15177v1 | [V] |
| Benchmarking Critical Questions Generation, arXiv 2505.11341 | https://arxiv.org/html/2505.11341v2 | [V] |
| ELLIS Alicante at CQs-Gen 2025, arXiv 2506.14371 | https://arxiv.org/abs/2506.14371 | [V] abstract only |
| SmartyPat-Bench, arXiv 2504.12312 | https://arxiv.org/html/2504.12312v3 | [V] |
| Are LLMs good zero-shot fallacy classifiers, arXiv 2410.15050 | https://arxiv.org/html/2410.15050v1 | [V] |
| Helwe et al. MAFALDA, arXiv 2311.09761 | https://arxiv.org/pdf/2311.09761 | [V] |
| Beyond Detection: fallacy awareness (ACL 2026) | https://aclanthology.org/2026.acl-long.59.pdf | [M] |
| Argument reconstruction as supervision, arXiv 2603.17432 | https://arxiv.org/html/2603.17432 | [V] |
| Ye, Moore, Novick, Zhang (2024) LMs as critical thinking tools, arXiv 2404.04516 | https://arxiv.org/pdf/2404.04516 | [V] |
| Lee et al. (2025) CHI, generative AI and critical thinking | https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf ; https://doi.org/10.1145/3706598.3713778 | [V] |
| Kosmyna et al. (2025) Your Brain on ChatGPT, arXiv 2506.08872 | https://arxiv.org/abs/2506.08872 | [V] |
| Gerlich (2025) AI tools in society | https://www.mdpi.com/2075-4698/15/1/6 | [M] (do not use) |
| Lau et al. (2026) Critical Thinking in AI Use Scale, arXiv 2512.12413 | https://arxiv.org/abs/2512.12413 | [V] abstract only |
| Not Too Short, Not Too Long (2026), arXiv 2603.06878 | https://arxiv.org/html/2603.06878v1 | [V] |
| Investigating LLM use on critical thinking under time constraints, arXiv 2603.08849 | https://arxiv.org/abs/2603.08849 | [V] abstract only |
| Toward LLM-supported automated assessment of critical thinking subskills, arXiv 2510.12915 | https://arxiv.org/abs/2510.12915 | [V] abstract only |
| Own audit of SCHEMA.md v0.2 against Delphi | C:/Users/User/Desktop/AGI/research_notes/single_agent/SCHEMA.md | [V] |

