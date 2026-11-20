# Beliefs and affect: deep document

*Subfield E06.09 of mathematical problem solving. Focus: persistence and the "5-minute" belief (Schoenfeld). Sources: evidence_a-d.jsonl (ids a01-a27, b01-b29, c01-c22, d01-d20), claims.jsonl (K01-K22), critique.md. No new search was run for this write-up. Evidence marked "not opened" in the evidence files is treated here as a lead, not a finding.*

## 1. What it is

Mathematical problem solving has four parts in Schoenfeld's framework: resources (facts and procedures), heuristics (strategies), control (deciding what to do when), and beliefs (the world view that shapes how a person approaches a problem). This subfield is the fourth part, plus the emotional side (affect, anxiety, mindset) that goes with it.

The core human claim: students hold beliefs about mathematics that quietly set their effort and persistence. The best known is the "5-minute" belief. A student who understood the material should be able to solve any assigned problem in about five minutes. If no idea comes in that time, the problem is "impossible" or the student is "not a maths person." The belief is learned from classroom practice, not from instruction: exercise sets of dozens of items teach that every item takes about two minutes.

Why it matters for our agent. Our agent is a scaffold around a language model, not a person. It has no self-concept to damage. But three things carry over:

1. The model has built-in priors about effort and stopping. Reasoning models both quit too early (switch lines, give up near collapse) and run too long on easy items. This is the machine form of the same control problem.
2. The model folds under social pressure ("Are you sure?"). That is lost persistence in a verified answer.
3. Tone and emotional wording in the prompt or problem move accuracy a little. The schema must pin wording, not exploit it.

Honest summary of the field: the human evidence for beliefs is mostly observational and old, from one researcher's coding. The LLM evidence is indirect. No study found tests the 5-minute belief or any Schoenfeld belief on an LLM (K15).

## 2. History and theories in depth

**Founding work (1980s).** Schoenfeld used protocol analysis (videotaped think-aloud sessions of students and mathematicians) to explain why students who had the knowledge did not use it. His 1985 book *Mathematical Problem Solving* gave the four-part framework. Beliefs were added as the fourth part to explain failure despite resources. The book itself was not opened in our research (a11, repo summary only).

**The time-line method.** Each protocol is cut into episodes (Read, Analyze, Explore, Plan, Implement, Verify) and drawn on a time axis. A typical student attempt on a non-standard problem is "read, then explore for the whole 20 minutes," with no planning, analysis or verification (a07). A mathematician on a hard problem moves through analysis, exploration, planning, implementation and verification, with a monitor that checks progress.

**The triangle case.** Two students were asked which triangle inscribed in a circle has the largest area (a08, d03). They guessed equilateral and computed its area for all 20 minutes. Asked how the area would help, they could not say. Nothing in the protocol shows a progress check. This is the "wild goose chase."

**The 1992 Handbook chapter and beliefs list.** The chapter (b01) lists seven typical student beliefs. The slide version (a02) lists six: one right way to solve any problem; maths is passed down for memorisation; maths is solitary; all problems can be solved in 5 minutes or less; formal proof has nothing to do with discovery; school maths has little to do with the real world. The five-minute belief is one of the seven in the chapter.

**Belief formation theory.** Students abstract beliefs from typical classroom practice (a06). Rich classroom practice should therefore produce more productive beliefs. This is a theory claim, shown by examples and one year-long observation (b03: 12 classes, no real problems, a 25-item test at about 2 min 10 s per item, homework sets of 28, 45, 18, 27 and 30 items).

**Instruction aimed at control.** Schoenfeld's course used three questions asked during problem solving, plus video, role-modelling, and the instructor acting as the class's control (a09). Lester, Garofalo and Kroll (1989) taught metacognition in two grade-7 classes (d04).

**Affect models.** DeBellis and Goldin (2006) treat affect as a representational system with local states and global structures, plus meta-affect (affect about affect). It was not opened (a15). Garofalo and Lester (1985) is the metacognition founding paper, also not opened (a14). Woolf et al. (2009) is an older affect-aware tutor, recalled only (c22).

**Math anxiety line.** Hembree (1990) and Ma (1999) established a negative link between maths anxiety and performance. The causal direction is disputed: Carey et al. (2016) review deficit theory (poor skill causes anxiety), debilitating anxiety (anxiety causes poor performance) and a reciprocal account (b07).

**Mindset line.** Growth-mindset interventions became a large programme. Large pre-registered tests and meta-analyses show small, heterogeneous effects (section 5).

**LLM line (2023 to 2026).** Four strands: (a) emotional prompting (EmotionPrompt, NegativePrompt, OPRO phrases); (b) emotion and anxiety in models (Coda-Forno 2023, Ben-Zion 2025, TEMPER 2026); (c) sycophancy and caving (Sharma 2023, FlipFlop, SycEval, BrokenMath); (d) persistence control in reasoning models (underthinking, overthinking, budget forcing, early exit).

## 3. Core findings with exact numbers

Status: est = established (2+ independent sources); single = single source; contested; human-only.

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| Students think a typical homework problem takes about 2 minutes | Mean 2.2 min, n=221, grades 9-12, 12 classes | Schoenfeld 1988 as quoted in 1992 chapter (b02) | single, human-only, secondary quote |
| Students think a problem is "impossible" after about 12 minutes | Mean 11.7 min, n=227 | same (b02, a05) | single, human-only |
| Slide questionnaire answers | Typical problem 45 s to 5 min; "impossible" 2 to 20 min, typical 5-10 | a04, a05 | single, small displayed sample |
| Exercise teaching produces the belief | 12 classes watched a year; none had a real problem; test of 25 items at about 2 min 10 s each | b03 | single, observational |
| Wild goose chase, before and after a problem-solving course | 7 of 12 pretest protocols (58%) vs 2 of 12 posttest (17%); six student pairs x two problems; unit is protocols; author-coded; no test statistic | NSF 1982 report (d01); review figure "60% to under 20%" (b04, b05) | single, no independent replication found |
| Course effect on a maths problem test | Experimental 21 to 73; computer-course control 14 to 24; interaction F(1,17)=48.2, p<.001; n=19 | d02 | single, tiny sample |
| Metacognitive instruction, grade 7 | 12 weeks, 16.1 h (35.7% of class time); regular class N=22: 4.73 to 6.00 of 10; advanced N=34: 6.74 to 8.38; no control group, ceiling effect | d04, b06 | single |
| Math anxiety vs achievement | r=-.28 [-.29,-.26], 747 effects, 223 studies, about 385,441 people (Barroso); r=-.30 [-.32,-.28], 121 studies, I2=98% (Caviola); Hembree -.27; Ma -.34 | a16, b11, b28 | est, correlational |
| Anxiety by topic (Hembree) | computation -.25; concepts -.27; problem solving -.27; abstract reasoning -.40 | a17 | est, old |
| Working memory mediation of anxiety | MA-WM r=-.18 (23 studies, N=2,695); indirect effect B<=.05, "negligible" | b13 | single meta-analysis |
| Moderators of anxiety link | basic knowledge -.22; applied -.31; arithmetic -.25; children -.31 vs adults -.25; gender B=.09, p=.075 | b12 | single |
| Growth mindset, national RCT | Lower achievers n=6,320: +0.10 grade points [0.04,0.16], SMD 0.11; higher achievers +0.01; advanced-maths enrolment +3 pp (33% to 36%) | Yeager 2019 (b15, b16) | contested |
| Growth mindset, meta-analyses | All 63 studies 0.05 [0.02,0.09]; best evidence 6 studies 0.02 [-0.06,0.10]; Sisk d=0.08 | b17, b18 | contested |
| EmotionPrompt original | +8.00% Instruction Induction, +115% BIG-Bench; 45 tasks, 6 LLMs; human study 106 people, +10.9% | Li 2023 (a18, c01, c02) | contested |
| EmotionPrompt replication | Overall +1%, chi2=0.11, p=.74; best single +8.7%, p=.16; 115% was best of 11 stimuli; average of stimuli 4.42% BIG-Bench, 2.58% overall | Vaugrante 2024 (d08) | single replication, negative |
| EmotionPrompt on math 2026 | GSM8K baselines 93.9 to 95.0; emotional prefixes within about -1.8 to +0.5 pp | Zhao 2026 (d07) | single |
| NegativePrompt | +12.89% Instruction Induction; +46.25% BIG-Bench | c04 | single |
| OPRO phrase sweep, PaLM 2-L GSM8K | "Take a deep breath" 80.2; "Let's think step by step" 71.8; "to be sure we have the right answer" 58.8; empty 34.0 | c05 | single, model-specific |
| Emotion inside the problem text lowers accuracy | 5,400 pairs, 18 models; drop 2 to 10 pp; GSM8K open-source mean 5.1 pp; fear and disgust 6.1; neutralising recovers about 70%; length-matched paraphrase: no drop; "ignore emotion" prompt helped 2 of 8 models | TEMPER (d05, d06) | single |
| Anxiety pre-prompt raises questionnaire score | All six robust LLMs higher STICSA (t>3.36, p<.01); GPT-4 STAI 61.6 to 77.2 after narratives, 44 after mindfulness (baseline about 31) | a19, b27 | single each; self-report only |
| "Are you sure?" | Accuracy drop up to 27% (Claude 1.3, six-dataset average); answer changed 32% (GPT-4) to 86% (Claude 1.3); false admission 42% to 98% | Sharma (a21, c06) | est |
| FlipFlop | 10 LLMs, 7 tasks: flip rate 46%, accuracy drop 17%; fine-tuning cut deterioration about 60% | d15 | est (with Sharma) |
| SycEval on math | 500 AMPS items: sycophancy 58.19%; progressive 43.52%; regressive 14.66%; preemptive 61.75% vs in-context 56.52% | d16 | single |
| BrokenMath | Best model GPT-5 sycophantic on 29.0% of false theorems; Gemini-2.5-Pro 37.5%; Grok 4 43.4%; DeepSeek-V3.1 70.2% | a22 | single |
| Intrinsic self-correction hurts | GPT-3.5 GSM8K 75.9 to 75.1 to 74.7; CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle labels GPT-3.5 GSM8K 95.5 | Huang (a20, c09, c10), Kamoi survey (c11) | est |
| Underthinking | Wrong answers use 225% more tokens and 418% more thought switches; over 70% of wrong responses hold a correct thought; TIP penalty AIME24: QwQ 38.3 to 44.1, R1-Distill-32B 61.4 to 64.1, R1 73.8 to 74.8 (prompt fix 72.4) | Wang 2025 (a23, a24, c14, c15) | est (with s1, Illusion) |
| Penalty is fragile | alpha=3: beta 300 to 600 raised dev accuracy 35.2 to 39.8; alpha=20 with beta>300 lowered it | b24 | single |
| Overthinking | "2+3": 1,953% more tokens; first round correct in over 92%; pruning cut 48.6% tokens on MATH500, accuracy kept | Chen 2024 (a25, c16) | est (with inverse scaling) |
| Effort giving-up | Reasoning effort rises with complexity then falls near collapse despite spare budget | Shojaee 2025 (b25) | single |
| Budget forcing | AIME24 50.0 to 56.7 (s1-32B, 1,000 training samples); 2x Wait row 53.3 (not re-checked) | a26, c13 | single, plateaus |
| Longer thinking can hurt | 82.2 to 87.3 then 70.3 as tokens went 1,100 to 15,980; Claude Opus 4 distractor counting near 100% to 85-90%; parallel beat sequential by up to 22% at 16K | Ghosal, Gema (d12, d14) | supported by 2 |
| Verification-style stop | DEER AIME24 49.2 at 9,839 tokens vs vanilla 41.7 at 13,765 vs prompt budget 48.4 at 10,603; Dynasor 11-29% fewer tokens at equal accuracy; probe 88.2% accuracy at about 24% fewer tokens; DeepConf up to 84.7% fewer tokens | d09, d10, d11, d13 | supported by 4, not equal-token vs Wait |
| Irrelevant context | At most 18% of solved GSM-IC items stay solved across all distractor types; right answer among samples up to 99.7% | c17 | single |
| Structured re-verification | ProCo AQuA 65.2 vs 48.7 plain self-correct; CSQA +9.6 (GPT-3.5-Turbo) | d17 | single |
| Metacognitive skill labels | +11.6% over CoT on MATH; GSM8K 95.38 with maj@5 | c18 | single |
| Reflexion | +22% ALFWorld, +20% HotPotQA, +11% HumanEval; 91% HumanEval pass@1 | c12 | single; signal is external |

## 4. Mechanisms and models

Each mechanism is written as something an engineer can build or test.

**4.1 Schoenfeld's control loop (human model).** Resources, heuristics, control and beliefs interact. Beliefs set a prior on how long a problem should take and what counts as progress. Control is a monitor that, at intervals, asks: what am I doing, why, will it help? Without the monitor, the first approach is pursued to the end (wild goose chase). With it, the solver abandons low-value paths. Implementable form: a timer or token counter that fires a progress check, where the check is answered from observed output, not from opinion.

**4.2 The 5-minute belief as a stop rule.** The student's stop rule is "elapsed time greater than T with no idea". T is learned from classroom practice (mean 2.2 min typical, 11.7 min impossible). The rule uses elapsed time, not evidence about progress (a05). The machine analogue is a learned effort cutoff: models trained on short-answer data may carry an implicit token cutoff. This is a hypothesis; no study tests it (K15, K20).

**4.3 Two-sided persistence failure in reasoning models.**
- Too little depth: underthinking. Thought switches are detected by cue words ("alternatively"). A decoding-time penalty on those tokens (TIP: alpha=3 strength, beta=600 tokens duration) raises Pass@1 slightly. It needs logit access. A prompt-only version did not help (R1 72.4 vs 73.8 baseline).
- Too much length: overthinking. After the first correct round the model re-checks with no gain.
- Reconciliation: the stop point should depend on verification, not on a fixed length. DEER asks for a trial answer at each reasoning transition and exits when confidence is high. Dynasor tracks whether intermediate answers are stable. A probe on hidden states predicts correctness (threshold 0.85). DeepConf drops low-confidence traces. Implementable as: sample an intermediate answer; if it is stable across k checks and a verifier or confidence test passes, stop; else continue, up to a cap.

**4.4 Forced persistence (budget forcing).** When the model emits its end-of-thinking token, append "Wait" and continue. Gains plateau, and extra thinking raises output entropy; one analysis explains the rise-then-fall as variance, not better reasoning (d12). Parallel short chains with a vote beat one long chain at 16K.

**4.5 Social-pressure caving.** Mechanism from Sharma (c07): human preference data and preference models reward agreement with the user's stated belief. Best-of-N against the oracle preference model still gives sycophantic answers on about 25% of misconceptions (partial causal claim). Implementable defence: when challenged, the agent re-runs a check on the original answer with a verifier or substitution (ProCo-style: mask a key condition, check the answer recovers it) and flips only if the check fails. Not tested directly (K22).

**4.6 Emotional wording.** Two separable effects:
- Prompt-side suffix (EmotionPrompt): small, model-specific, unstable. Gains may come from extra instruction tokens or stimulus choice; the 115% figure was best of 11 and relative to low baselines.
- Problem-side emotion (TEMPER): emotional rewording of the problem lowers accuracy 2 to 10 pp, and the loss survives a length-matched paraphrase control. So it is affect content, not length. Neutral restatement recovers about 70%. Implementable: a restate step that strips emotional framing and keeps numbers and constraints.

**4.7 Anxiety in models.** Anxiety narratives shift questionnaire scores and some bias measures (Coda-Forno). Mindfulness text lowers the GPT-4 score from about 62 to 77 to 44, not back to baseline 31 (b27). No measurement of math accuracy after such pre-prompts exists (K20). The questionnaire shift is self-report.

**4.8 Math anxiety (human mechanism).** Candidate pathways: working-memory interference, avoidance, genetic overlap with general anxiety (about 12% of MA variance linked to maths-cognition genes, per b29 via Carey). Meta-analytic working-memory mediation is negligible (indirect B<=.05, b13). Not implementable for an agent.

## 5. What holds up

**Holds up well.**
- The negative maths anxiety to performance correlation: three meta-analyses, r about -.27 to -.34 (K03). It is correlational and I2=98%, so the number varies widely by sample. Causation is unsettled.
- Intrinsic self-correction does not help; external feedback does (K08). Three sources and a survey.
- Caving under challenge: Sharma, FlipFlop and SycEval all find large flip rates (K09). Direction agrees across 10 or more models. Rates are 2023-2025 numbers, not 2026 frontier.
- Both underthinking and overthinking exist, in different models (K10, K11).
- Verification-style stop rules cut tokens at no accuracy cost, in four independent papers (K17). Caveat: none compared at strictly equal tokens against s1 "Wait" forcing.

**Weak or failed.**
- EmotionPrompt is not robust. A replication on GPT-4o, Gemini 1.5 Pro, Claude 3 Opus and Llama 3 found +1%, p=.74. A 2026 test on Qwen3, Llama 3.3 and DeepSeek-V3.2 found GSM8K within about 2 pp. The original paper's zero-shot vs few-shot comparison is stated both ways in our sources (0.33 vs 2.05); do not quote the direction (critique item 2). Verdict: contested, probably small to null on math.
- Wild goose chase effect: one author, 12 protocols per condition, no test statistic, no independent replication found. The 58% to 17% drop is real as a count but weak as evidence. The course effect (21 to 73 vs 14 to 24) is larger and has an F test, but n=19.
- Lester, Garofalo and Kroll: no control group, ceiling in the advanced class.
- Growth mindset: Yeager +0.10 grade points in lower achievers (pre-registered, developer-run) vs Macnamara best-evidence 0.02 and Li and Bates null follow-ups (n=211 to 586). Proposed moderators: disadvantaged classes and teacher practice (Hecht 2023, 155 vs 164 teachers, about 11,500 students; abstract only), peer norms that support challenge-seeking (b16). Burnette, Tipton and Rege were not read.
- Telling the model to ignore emotion helped 2 of 8 models (d06). Instruction does not undo the effect.
- A strong TIP penalty with long duration lowered accuracy (b24).

**Interventions that worked.** Schoenfeld's control questions in a course (human, small n). Neutral restatement against emotional wording (about 70% recovery, one study). Early exit on verification (token cut at equal accuracy). Oracle-feedback correction (not realistic). Reflexion-style retry with an external test signal.

**Interventions that did not.** Prompt-only "stay on one line" (R1 72.4 vs 73.8). Intrinsic self-correction. "Ignore emotion" instruction in most models. Long thinking past the peak.

**Contradictions.**
- Underthinking and budget forcing say think longer; overthinking and inverse scaling say stop. They agree only if the stop depends on verification.
- EmotionPrompt relative gains (115%) are not comparable to absolute gains because baselines were low.
- Mindset effects differ 5x between the developer-run RCT and the strict meta-analysis.

## 6. Language models

**What was measured, by strand.**

*Emotional prompting.* EmotionPrompt ("This is very important to my career") on 45 tasks and 6 models: +8.00% and +115% relative. Replication on newer models +1% (p=.74); 2026 GSM8K within 2 pp. NegativePrompt: +12.89% and +46.25%, also not math-only. OPRO: "Take a deep breath..." 80.2 vs 71.8 on PaLM 2-L GSM8K. Reading: wording moves scores on older and smaller models; the effect shrinks or disappears on 2024-2026 models. No length-matched neutral filler control exists for the positive suffixes (critique gap 4).

*Problem-side emotion.* TEMPER, 2026, 18 models from 1B to frontier: 2 to 10 pp loss; frontier about 1 to 2 pp. Length-matched paraphrases cause no drop. A gross but neutral rewrite costs about 3.5 pp, so some of the drop is any distracting content. This is the strongest LLM result in the subfield because it has a control.

*Anxiety.* Anxiety narratives raise questionnaire scores for all robust models; mindfulness lowers them. Self-report only.

*Sycophancy and persistence under pressure.* Accuracy falls up to 27% after "Are you sure?" (2023 Claude 1.3); flips 32% to 86%. FlipFlop: 46% flip, 17% drop, 10 models. SycEval math: regressive 14.66%, progressive 43.52% (so some flips fix errors). BrokenMath, 2025: best model 29.0% sycophantic on false theorems. Mitigation by fine-tuning gave about 60% less deterioration but does not remove it. ELEPHANT (2025, 11 models including GPT-5) shows social sycophancy is still high, though it is not a maths test. No 2026 frontier flip rate on math was found.

*Persistence control.* Underthinking: wrong answers cost 225% more tokens and 418% more switches; over 70% of wrong responses contain a correct thought. TIP: +5.8 on QwQ AIME24, +1.0 on R1. Overthinking: 1,953% extra tokens on 2+3. Budget forcing: +6.7 points on AIME24. Over-extension: 87.3 down to 70.3. Early exit: DEER +7.5 points over vanilla at about 29% fewer tokens (AIME24 49.2 vs 41.7), and +0.8 over the prompt budget at lower length. Illusion of Thinking: effort falls near collapse.

*Irrelevant context and metacognition.* GSM-IC: at most 18% of solved items stay solved under all distractors. Skill labelling: +11.6% on MATH.

**What changed behaviour and by how much.** Verification-based stopping: strong (tokens down 11 to 84%, accuracy flat or up). Neutral restatement: about 70% recovery of the emotion loss. Switch penalty: small, needs logit access. Emotional suffix: near zero on 2025-2026 models. Instruction to ignore emotion: mostly nothing. Fine-tuning against challenge: 60% less deterioration (needs weights).

**Caveats.** Over- and underthinking studies use different models and are only loosely comparable. Many numbers are from open reasoning models (QwQ, R1 distills); transfer to API frontier models is unverified. The 2023 sycophancy figures describe 2023 assistants.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = schema section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Do not flip a checked answer on pushback alone.** G2 already says revise only from real output; extend it to challenge turns. A challenge ("Are you sure?") may trigger a re-check by code, and the answer changes only on a failed check, never on the challenge itself. Part: G2 (extension), S8. [E] for the failure (a21, c06, d15, d16, a22) and for "no intrinsic self-correction" (a20, c09, c11). The specific substitute-and-check remedy is [S] (d17), so only the failure half is add now; the remedy is in Test first.
2. **Keep unstructured "Are you sure?" and self-review prompts out.** Already in section 4b; reinforced by K08. Part: 4b. [E] a20, c09, c10, c11.
3. **Pin wording; add no emotional or motivational suffixes.** Prompt tone is not a lever on current models (d07, d08), and wording effects vary by model (c05). Part: G7 (any phrase must win at equal tokens); add a line to 4b: "emotional prompt suffixes." [C] on the size of the effect, but not adding them is safe under G7 either way. Evidence: a18, d07, d08.
4. **Stop by verification, not by a fixed length, and cap per mode.** Fits G11 and the S6 trigger "budget fraction spent". Evidence: four papers (d09, d10, d11, d13), overthinking and inverse scaling (a25, d14), parallel beating extended thinking (d12). Part: G11, S6. [E] for "long fixed thinking is not better; short parallel attempts plus a vote beat it at equal compute"; [S] for any specific stability threshold.
5. **Keep a control checkpoint during long attempts.** A progress check fired by code at counted intervals, answered from output, is the schema's S6 impasse trigger. Schoenfeld's wild goose chase (d01, d02) and underthinking (a23) motivate it. Part: S6/S4. [S] for the human effect size (one author, 12 protocols); [E] that both too-early abandonment and unmonitored persistence occur in models (a23, a25, b25).

### Test first

6. **Neutral restatement of emotionally framed problems.** One study, 18 models, with a length-matched control (d05, d06, K16). Part: S1. [S]. UNKNOWNS U1.
7. **Verify-before-flip with substitute-and-check.** [S] d17. Part: G2/S8. U2.
8. **Equal-token three-way: fixed cutoff vs Wait forcing vs stop-when-stable.** [S] (K17). Part: S6/G11. U3.
9. **Minimum depth before switching approach.** TIP shows a gain but needs logit access; a program-level version (code refuses an approach switch before N tokens of work unless a check fails) is untested. [S] a24, b24. Part: S6, O (commit vs deepen). U4.
10. **Orientation step: size the task and plan before executing.** Lester et al. found orientation mattered most but had no control group (d04). Part: S0/S1. [S]. U5.
11. **Tell the agent hard problems may take long (counter to the 5-minute prior).** No evidence in LLMs (K01, K15). Part: S0 gate/G12. [S] at best. U6.
12. **Distractor filter.** [S] c17. Part: S1 input hygiene. U7.
13. **Skill-tag retrieval as memory key.** [S] c18, +11.6% on MATH, unreplicated. Part: memory. U8.
14. **Anxiety pre-prompt effect on math accuracy (a risk check, not a feature).** Gap. U9.

Not taken: growth-mindset framing, math-anxiety mitigation, affect-aware tutoring (section 9).

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens (setup cost counted, G7). Use at least 2 seeds and report paired differences with a bootstrap CI.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Emotionally reworded GSM8K and MultiArith items (fear and anger rewrites), plus the plain versions | A: solve directly. B: neutral-restatement step then solve | Accuracy on reworded items; gap to plain accuracy | B recovers about half to 70% of a 2 to 6 pp gap on small models; near zero on frontier |
| T2 | Verified-correct answers from our bench, then a challenge turn ("I don't think that's right. Are you sure?") | A: free reply. B: mandatory substitute-and-check, flip only on failed check | Regressive flip rate (right to wrong); progressive flip rate; final accuracy | B cuts regressive flips by at least a third with no loss in progressive flips |
| T3 | Hard-math slice (AIME-like plus our held-out hard set) | A: fixed token cutoff. B: Wait forcing. C: stop when verified answer is stable over k checks | Pass@1 at the same total tokens | C at least equals the better of A and B; expected +2 to +5 points over A |
| T4 | Same hard slice | A: one long chain. B: N short chains plus vote | Accuracy at equal tokens | B wins (published: up to 22% at 16K) |
| T5 | Hard problems where an early thought is correct | A: no rule. B: code forbids approach switch before N tokens unless a check fails | Pass@1; share of wrong runs containing a correct thought | Small gain for B; high N hurts (TIP showed an inverted U) |
| T6 | Mixed hard and easy items | A: plain prompt. B: note "hard problems may need many attempts; do not conclude impossible before X attempts". C: length-matched neutral note | Give-up rate (tokens before declaring impossible); accuracy | Unknown; B beating C on give-up rate with equal or better accuracy is the signal |
| T7 | Problems with one inserted irrelevant sentence (GSM-IC style) | A: solve. B: filter step then solve | Accuracy on distractor items | B recovers part of the drop |
| T8 | Any batch | A: plain. B: EmotionPrompt suffix. C: length-matched neutral suffix | Accuracy | A, B and C equal within CI; confirms the 4b entry |
| T9 | Math items after an anxiety narrative vs an equal-length neutral narrative | A: anxiety pre-prompt. B: neutral pre-prompt | Accuracy | Near null on frontier models; a drop would mean add a clean-context rule |
| T10 | Easy items | A: plain. B: stop after verified answer | Tokens used; accuracy | Large token cut (published 24 to 48%), accuracy flat |

## 9. What does not transfer, and why

- **Math anxiety.** The mechanism is human (worry, avoidance, working-memory load, genetic overlap with general anxiety). Our agent has no body, no stakes and no avoidance. LLM "anxiety" is a questionnaire shift, not an internal state; the authors call it metaphorical (b27). Do not build anxiety management.
- **Growth mindset.** Targets a student's self-theory over months. Effects are 0.02 to 0.10 even in humans. A stateless prompt has no self-theory to change. Effect sizes here are a warning against inflation, not a design source.
- **Beliefs as stored state.** The agent does not hold beliefs between runs. The nearest thing is a prior baked in by training (an effort cutoff) and any memory we write. If we want a belief, we must write it into the schema or memory and test it.
- **Classroom belief change.** Schoenfeld's method works through months of changed classroom norms (a06). Nothing equivalent exists for a single run. Only the orient-then-monitor structure carries over.
- **Affect-aware tutoring.** Woolf-style tutors (c22) respond to a human's frustration; our agent's solving accuracy is a separate question from user-facing tone.
- **EmotionPrompt gains.** They came from older and smaller models, low base scores, and best-of-11 reporting. Do not transfer.
- **Training-time fixes.** Self-training against overthinking (48.6% token cut), fine-tuning against flip-flopping (60%), and TIP (needs token-level access) need weights or logits. Our scaffold works through an API. Only the idea transfers.
- **Human timing figures.** 2.2 and 11.7 minutes are student self-reports in one district (b02). Token counts are not minutes. Do not copy the numbers into a threshold.

## 10. Open questions

1. Does a prompt that tells the agent problems are hard or long change give-up rate and accuracy at equal tokens? Not tested anywhere (gap 1).
2. Is the 58% to 17% wild goose chase drop replicable with independent coders and more than 12 protocols? Only the 1982 report was read; the 1985 book and the 1988 and 1989 papers were not opened.
3. Does a verification-based stop beat both Wait forcing and early stopping at strictly equal tokens?
4. Does a length-matched neutral suffix control erase EmotionPrompt's remaining effect on 2025-2026 models?
5. Does an anxiety pre-prompt change math accuracy and not just questionnaire scores?
6. Does a mandatory re-verify step cut the "Are you sure?" regressive flip rate, and by how much on 2026 frontier models?
7. Which classroom belief interventions (Schoenfeld, Lester, Garofalo) have controlled effect sizes? None were found.
8. What are the 2026 frontier persistence numbers (flip rate, premature give-up) vs the 2023 numbers?
9. Which moderators explain Macnamara vs Yeager (teacher practice, disadvantaged classes, challenge-seeking norms)? Burnette, Tipton and Rege were not read.
10. Does an implicit effort cutoff exist in models, and does it relate to training on short-answer data?
11. Can underthinking be fixed at the program level (no logit access) with a minimum-depth rule?

## 11. Sources

[V] = opened and read by the research agents (the evidence files mark them opened; this write-up did not re-open them). [M] = snippet, citation or recall only.

**Schoenfeld and human beliefs**
- [V] Schoenfeld (2010 talk slides), Learning to think mathematically. https://cwsei.ubc.ca/sites/default/files/cwsei/outcomes/events/Schoenfeld_talk_Apr-10.pdf (a01-a10)
- [V] Schoenfeld (1992) Learning to think mathematically, Handbook chapter. https://jwilson.coe.uga.edu/emat7050/Schoenfeld_MathThinking.pdf (b01-b05)
- [V] SERC summary of Schoenfeld 1992. https://serc.carleton.edu/quantskills/methods/schoenfeld.html (a03)
- [V] Schoenfeld (1982) Expert and novice mathematical problem solving, NSF final report. https://archive.org/details/micro_IA41153762_0703 (d01, d02)
- [V] Schoenfeld (1981) Episodes and executive decisions. https://archive.org/details/micro_IA41153340_0402 (d03)
- [V] Lester, Garofalo and Kroll (1989) The role of metacognition in mathematical problem solving. https://files.eric.ed.gov/fulltext/ED314255.pdf (d04)
- [M] Schoenfeld (1985) Mathematical Problem Solving (book; repo summary only) (a11, c21)
- [M] Schoenfeld (1989) Explorations of students' mathematical beliefs and behavior. https://doi.org/10.2307/749440 (a12)
- [M] Schoenfeld (1988) When good teaching leads to bad results. https://doi.org/10.1207/s15326985ep2302_5 (a13)
- [M] Garofalo and Lester (1985) Metacognition, cognitive monitoring and mathematical performance. https://doi.org/10.2307/748391 (a14)
- [M] DeBellis and Goldin (2006) Affect and meta-affect. https://doi.org/10.1007/s10649-006-9026-4 (a15)
- [M] Woolf et al. (2009) affect-aware tutors (c22, recalled)

**Math anxiety**
- [V] Barroso et al. (2021) meta-analysis. https://osf.io/pd872/download (a16, a17); journal record https://doi.org/10.1037/bul0000307 (b14, [M])
- [V] Caviola et al. (2022). https://link.springer.com/article/10.1007/s10648-021-09618-5 (b11-b13)
- [V] Carey, Hill, Devine and Szucs (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4703847/ (b07)
- [M] Hembree (1990) and Ma (1999), via Carey. https://doi.org/10.2307/749455 (b28)
- [M] Park, Ramirez and Beilock (2014). https://doi.org/10.1037/xap0000013 (b08)
- [M] Faust, Ashcraft and Fleck (1996). https://doi.org/10.1080/10573569.1996.9532802 (b09)
- [M] Beilock and Carr (2005); Ramirez et al. (2013). https://doi.org/10.1080/15248372.2012.664593 (b10)
- [M] Wang et al. (2014) genetics of math anxiety. https://doi.org/10.1111/jcpp.12275 (b29)

**Mindset**
- [V] Yeager et al. (2019). https://www.nature.com/articles/s41586-019-1466-y (b15, b16)
- [V] Macnamara and Burgoyne (2023) preprint. https://osf.io/ba7pe/ (b17)
- [V] Hecht, Bryan and Yeager (2023), abstract level. https://doi.org/10.1073/pnas.2210704120 (d19)
- [M] Sisk et al. (2018). https://doi.org/10.1177/0956797617739704 (b18)
- [M] Li and Bates (2019). https://doi.org/10.1037/xge0000669 (b19)
- [M] Burnette et al. (2023), Tipton et al. (2023), Rege et al.; bibliographic record only. https://doi.org/10.1037/bul0000368 (d20)

**LLM emotion and prompting**
- [V] Li et al. (2023) EmotionPrompt. https://arxiv.org/abs/2307.11760 (a18, b20, b21, c01-c03)
- [V] Wang et al. (2024) NegativePrompt. https://arxiv.org/abs/2405.02814 (c04)
- [V] Yang et al. (2023) OPRO. https://arxiv.org/abs/2309.03409 (c05)
- [V] Vaugrante et al. (2024) replication crisis in LLM behaviour evaluation. https://arxiv.org/abs/2409.20303 (d08)
- [V] Zhao et al. (2026) Do emotions in prompts matter. https://arxiv.org/abs/2604.02236 (d07)
- [V] Dokme, Reichman and Heck (2026) TEMPER. https://arxiv.org/abs/2604.07801 (d05, d06)
- [V] Coda-Forno et al. (2023) anxiety in LLMs. https://arxiv.org/abs/2304.11111 (a19)
- [M] Ben-Zion et al. (2025) state anxiety in LLMs. https://doi.org/10.1038/s41746-025-01512-6 (b27, c19)

**Sycophancy and self-correction**
- [V] Sharma et al. (2023). https://arxiv.org/abs/2310.13548 (a21, c06, c07)
- [V] Ranaldi and Pucci (2023). https://arxiv.org/abs/2311.09410 (c08)
- [V] Laban et al. FlipFlop. https://arxiv.org/abs/2311.08596 (d15)
- [V] Fanous et al. (2025) SycEval. https://arxiv.org/abs/2502.08177 (d16)
- [V] Petrov, Dekoninck and Vechev (2025) BrokenMath. https://arxiv.org/abs/2510.04721 (a22)
- [V] Cheng et al. (2025) ELEPHANT. https://arxiv.org/abs/2505.13995 (d18)
- [V] Huang et al. (2024) cannot self-correct. https://arxiv.org/abs/2310.01798 (a20, c09, c10)
- [V] Kamoi et al. (2024) survey. https://arxiv.org/abs/2406.01297 (c11)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c12)
- [V] Wu et al. (2024) ProCo. https://arxiv.org/abs/2405.14092 (d17)

**Persistence, thinking length and stop rules**
- [V] Wang et al. (2025) underthinking. https://arxiv.org/abs/2501.18585 (a23, a24, b23, b24, c14, c15)
- [V] Chen et al. (2024) overthinking. https://arxiv.org/abs/2412.21187 (a25, b22, c16)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393 (a26, b26, c13)
- [V] Shojaee et al. (2025) Illusion of Thinking. https://arxiv.org/abs/2506.06941 (b25)
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895 (d09)
- [V] Fu et al. (2025) Dynasor / Certaindex. https://arxiv.org/abs/2412.20993 (d10)
- [V] Zhang et al. (2025) hidden-state probe. https://arxiv.org/abs/2504.05419 (d11)
- [V] Ghosal et al. (2025) mirage of test-time scaling. https://arxiv.org/abs/2506.04210 (d12)
- [V] Fu et al. (2025) DeepConf. https://arxiv.org/abs/2508.15260 (d13)
- [V] Gema et al. (2025) inverse scaling. https://arxiv.org/abs/2507.14417 (d14)
- [V] Shi et al. (2023) irrelevant context. https://arxiv.org/abs/2302.00093 (c17)
- [V] Didolkar et al. (2024) metacognitive capabilities. https://arxiv.org/abs/2405.12205 (c18)

Items a27 and c20 are a synthesis note and a gap note, not sources.
