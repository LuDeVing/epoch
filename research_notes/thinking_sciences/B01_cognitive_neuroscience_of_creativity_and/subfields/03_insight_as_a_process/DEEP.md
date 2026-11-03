# Insight as a process: deep document

*Subfield B01.03. Written 2026-11-03 from evidence_a-d.jsonl (a01-a27, b01-b27, c01-c26, d01-d18), claims.jsonl (K01-K25) and critique.md in this folder. Evidence ids are in brackets. Where a source was not opened, the text says so. Links to parallel subfields are noted, not covered: Gestalt roots and fixation; Metacognition of insight (B01.05, done); Insight neural signatures; Dual-process view of creativity; Transformational creativity; Learned refinement and self-verification.*

## 1. What it is

Insight is the sudden change from being stuck on a problem to seeing how to solve it. Three claims sit inside that idea.

1. **Impasse.** The solver reaches a point where the current approach gives no progress. The solver may or may not feel stuck.
2. **Restructuring.** The solver then changes how the problem is represented. A goal, constraint or chunk is dropped or re-read. The solution follows quickly.
3. **Staging.** The whole episode is described as four stages: preparation, incubation, illumination (insight), verification. This is the Wallas (1926) model, credited by Wikipedia also to Hadamard (1945) [a01, a07, b21].

For our agent the mapping is direct. S6 (impasse) fires and then an operator is applied. O4 (drop a constraint), O6 (change representation) and O8 (reframe) are the restructuring operators. S8 (verify) matches the fourth stage. Incubation has no clean counterpart, because a model has no continuing brain between calls.

The field is human psychology first. Most numbers come from small lab samples with puzzles such as matchsticks, magic tricks, compound remote associates (CRA) and Mooney images. The LLM literature (2023-2026) is thin. It mostly compares unscaffolded models with humans. It almost never tests an insight-style operator at equal tokens [critique.md].

Two points shape everything below.
- The felt "Aha" is a human feeling. It is a metacognitive judgement inferred from cues, not a readout of restructuring [a12]. It must not be used as a signal in the agent (guardrail G10).
- The four-stage model is descriptive. It came from introspection and was not tested experimentally [b21, K17].

## 2. History and theories in depth

### 2.1 Gestalt roots (Duncker, Maier, Koehler, Wertheimer, Katona)
Insight is restructuring: a sudden shift of the problem representation from an unproductive to a productive one. Impasse (feeling stuck) is part of the story, because the old structure blocks the new one [a24]. Fixation (Einstellung, functional fixedness) is the negative side: a familiar set blocks the new view. Deep treatment belongs to the parallel subfield on Gestalt roots and fixation.

### 2.2 Wallas and Hadamard: four stages
Wallas (1926, The Art of Thought) named preparation, incubation, illumination and verification. Hadamard (1945) brought the model to mathematics. The stages come from self-report of eminent thinkers. They were not derived from experiments [b21, a01]. Sio and Ormerod counted 5,510 articles from 1997 to 2007 on incubation with creativity, insight or problem solving, plus 1,970 more. Earlier narrative reviews covered only about 10 studies [a07].

### 2.3 Special-process vs business-as-usual views
- **Special process (Gestalt, Ohlsson 1992).** Insight needs a distinct restructuring event. Representational change theory: the initial representation is incomplete or wrong, search fails (impasse), then constraint relaxation, re-encoding or elaboration lets search resume [a25; not opened, summarised via a02, a11, a15].
- **Business as usual (Weisberg; MacGregor, Ormerod and Chronicle 2001).** Insight uses ordinary conscious processes. Nine-dot difficulty fits hill-climbing with progress monitoring and look-ahead [b25, not opened]. Weisberg (2015): impasse is not a prerequisite. Restructuring more often precedes insight solutions but also occurs in non-insight ones (one later study N=42, 70 word puzzles, snippet only) [b20].
- **Kaplan and Simon (1990).** Insight as search in a space of representations [c24, not opened].
- **Knoblich et al. (1999).** The testable middle: constraint relaxation (wide scope is hard) and chunk decomposition [a02, a03].

### 2.4 Incubation accounts
Sio and Ormerod weigh three accounts [a07]: unconscious work (spreading activation continues), conscious work (the solver keeps trying quietly), and forgetting of fixation (the wrong set decays). They conclude unconscious work and conscious restructuring each get support, but only for particular problem types [a06]. Gilhooly (2016) judges unconscious work best supported and conscious rehearsal in the break largely ruled out [b17].

### 2.5 Warmth and discrete transitions
Metcalfe (1986) and Metcalfe and Wiebe (1987): on insight problems solvers report little or no progress until shortly before the solution. On algebra, warmth rises smoothly [a09, b22; numbers not verified]. Schooler, Ohlsson and Brooks (1993): talking through insight problems lowered success, with no harm on non-insight problems [b23; not verified]. Metacognition of insight is covered in B01.05.

### 2.6 Dual-process view
In the Davidson and Sternberg framing, insight is a case where a fast associative route finds a new link while the analytic route monitors and verifies. Webb et al. support a version of this: insight is about the solver's experience, not the problem type. Both classic insight and non-insight items can be solved with or without Aha [a10, b16]. No direct Davidson and Sternberg source was opened here. Link only to the dual-process creativity subfield.

### 2.7 Neural signature
Jung-Beeman et al. (2004): right anterior superior temporal gyrus (aSTG) is more active for insight than non-insight CRA solutions, with an EEG gamma burst. Read as a discrete shift in distant semantic integration [a08, K16]. Becker et al. (2025), fMRI, Mooney images, N=31: insight goes with stronger representational change in visual cortex and amygdala and hippocampus activation, and predicts later memory [a14]. Kim (2026) is a theory paper on illumination onset with no numbers [a13]. None of this gives an online signal for a model.

## 3. Core findings with exact numbers

Status: est = established (two or more independent sources); single = single source; contested; unsupported.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Constraint scope sets difficulty in matchstick arithmetic (value < operator < tautology) | Exp 1A N=20, 5-min limit: order C<B<A and D<A, F(3,57)=7.11, p<.001. Block effect F(1,19)=14.41, p<.01. Type D solved 75% block 1, 90% block 2. Exp 1B N=38 same order. Exp 2 N=78 | Knoblich et al. 1999 [a02] | est (statistics not re-verified, critique 6) |
| Relaxing a hard constraint transfers to later problems of the same type, not by surface similarity | Type x block F(3,57)=3.24, p<.05. Transfer B p<.05, C p<.001, A p=.80, D p=.13. Exp 2: block-2 success 95-99%, no similarity effect (82, 82, 80, 83%) | Knoblich 1999 [a03] | est |
| Interactivity add-on to matchstick insight did not replicate | Exp 1 N=105: interactive 0.91/0.87/0.59/0.67 vs static 0.94/0.80/0.59/0.69 (A/B/C/D). Exp 2 N=88. Exp 3 N=73. Movement hurt relaxing high-level constraints | Spiridonov et al. 2026 [d01] | single (failure of an add-on, not the core) |
| Incubation helps overall, small effect | 117 studies, 3,606 participants, median n=25. Unweighted 0.41 (SD 0.71, CI 0.28-0.54). Capped 0.36 (CI 0.26-0.45). Random-effects weighted 0.29 (SD 0.04, CI 0.21-0.39). Median 0.26 | Sio and Ormerod 2009 [a04] | est |
| Divergent tasks gain more than linguistic or visual insight tasks. Longer preparation helps. High-demand break task shrinks the effect. Low-demand task beats rest | Meta-regressions R2 about .20-.21. Breaks 0.25 to 1,440 min | Sio and Ormerod [a04, a06, b18] | est |
| Misleading cue (fixation) raises incubation gain for linguistic problems, not visual | 29 studies, 25 linguistic. Linguistic: misleading 0.36 (SD .09) vs none 0.17 (SD .06). Visual: 0.18 (SD .39) vs 0.26 (SD .08) | Sio and Ormerod [a05] | single |
| Incubation is smaller in other pooled counts | Eight tests of intermittent work average r=0.11. Strick 2011 g=0.224 (92 decision studies) | Gilhooly 2016 [b17] | est, second-hand |
| 4-min break equals 12-min break; sleep about doubled insight solutions | Segal 2004; Wagner 2004 | via Wikipedia [a01] | single each, not opened |
| A 2-week gap gave an incubation gain on the cheap necklace problem, larger with high interactivity | significant improvement; N not extracted | Vallee-Tourangeau 2020 [a26] | single |
| Aha reports predict accuracy on classic insight and CRA, not on non-insight | Accuracy-Aha r: classic .50/.40/.495; CRA .41/.40/.39; non-insight .02/.24/.19 (Exp 1/1a/2). Accuracy classic .51/.49/.45; non-insight .54/.64/.56; CRA .37/.45/.47. N=184/74/117 | Webb et al. 2016 [a10, b16] | contested (K05) |
| False insights are common | 70 students, 37 tricks shown (35 analysed), 1,778 solutions: 36.8% (654) correct, 63.2% (1,124) wrong. Aha 66.50 vs 52.34, t(69)=10.21. 417 of 1,124 wrong (37%) above correct mean. Certainty 70.55 vs 56.14. Time 35.81 vs 42.46 s | Danek and Wiley 2017 [a11, b13] | est |
| Aha parts differ by correctness | Correct (N=654): pleasure beta .35, suddenness .24, certainty .20, relief .09. Wrong (N=1,124): pleasure .38, certainty .27, suddenness .16, surprise .09 | Danek and Wiley [b14] | single |
| Aha behaves like a cue-based judgement | N=377. Aha-correctness F(1,1091)=112.17, p<.001; effect comes from solutions after a correct first move | Wiley and Miller 2026 [a12, a27] | single |
| Insight memory advantage is mostly correctness, certainty, pleasure | Exp 1 (738 solutions): Aha correct 65.66 vs wrong 51.28, d=0.52. Aha-recall d=0.51. After one week 57.7% of correct vs 35.4% of wrong recalled. Sudden-restructuring measure did not predict recall (Exp 2) | Danek and Wiley 2020 [b15] | est (K06); mechanism contested |
| Generation, not Aha, predicts memory | not read | Kizilirmak 2019 [b27] | single, snippet |
| Right aSTG higher for insight solutions | Exp 1 N=13: 59% solved. Insight on 56% (SD 18.2), non-insight 41% (SD 18.9). Peak difference 0.25% (0.30% at one TR). 12 of 13 subjects | Jung-Beeman 2004 [a08] | single |
| Insight shows stronger visual-cortex representational change and predicts memory | N=31. Ratings (1-4): emotion 2.8, suddenness 3.0, certainty 3.16 | Becker 2025 [a14] | single |
| Reasoning LLMs: mid-trace "Aha" shifts are rare and go with lower accuracy | 1M+ traces (critique: not 11M). Shifts in 6.31%. Formal detector 1.79%. Qwen-1.5B 2.57% vs 16.44% (N=723,200). Pooled accuracy 6.6% with shift vs 29.0% without. Math -22.88 pp (low entropy), -7.40 pp (high entropy). Shift rate Xwords 1.22%, Math 2.65%, Rush Hour 14.32% | d'Aliberti and Ribeiro 2026 [a21, b01, b02] | est (K07) |
| Forced reconsideration under high entropy helps on math only | MATH-500 32.21% to 40.62% (+8.41 pp). 50,574 wrong-to-right vs 23,500 right-to-wrong. Crosswords +0.45, Rush Hour +0.01 pp. Judge kappa .726 | same [b03] | single (no equal-token control) |
| R1-Zero "aha" is a rise in the word "wait" | AIME24 pass@1 15.6% to 77.9% across RL | DeepSeek-AI 2025 [a22, b04] | a claim, not evidence of insight |
| Self-reflection already exists in base models, not tied to accuracy | 500 MATH questions; DeepSeek-V3-Base shows "Aha" and "wait" keywords | Liu 2025 [c11] | est with a21, b05 |
| Aha moments in VLMs are rare and add little | 8.3% of responses. Majority vote +4.5% over greedy. Best-of-N with self-verification limited gain or up to -16.7% | Wu 2025 [b05] | single |
| Intrinsic self-correction does not help | GPT-3.5 GSM8K 75.9/75.1/74.7; CSQA 75.8/38.1/41.8; HotpotQA 26.0/25.0/25.0. GPT-4 GSM8K 95.5/91.5/89.0; CSQA 82.0/79.5/80.0; HotpotQA 49.0/49.0/43.0 (rounds 0/1/2). Oracle labels help | Huang 2024 [c15] | est (K09) |
| LLMs far below humans on insight riddles | Nazonazo: humans 52.9% (n=126, CI 46.6-59.2) on 120 items. 38 LLMs: non-reasoning 7.6%, reasoning 17.6%. Full 201 items 9.42% vs 19.25%, OR 2.29 (1.99-2.64). GPT-5 inside human CI | Mizumoto 2025 [a19, b06, c01] | est (K10) |
| Models write the right answer, then reject it | Verification failures 5.23% (Gemini 2.5 Flash) to 39.34% (Grok 4) of wrong answers. DeepSeek-R1-0528 30.57%, Claude Opus 4 25.00%. Grok 4: 194 answered, 72 correct, 48 VF | Mizumoto [a19, b07, c02] | single (K11) |
| Language of the thought log is not reliably helpful | Grok-4 Japanese 29.5% (33/112) vs English 48.8% (40/82), p=0.0071. Opus 4 36.7% vs 28.7%, p=.356. Gemini 2.5 Flash 0/12 vs 11.7% | Mizumoto [b08, c03] | single |
| Reasoning-inclusive few-shot demos raise riddle accuracy | 4 of 4 models up; significant in 2 | Mizumoto [a20, b07] | single |
| Lateral puzzles: model near chance, human near ceiling | BRAINTEASER 1,100 items: best ChatGPT 53% / 63% vs random 25%, human 92% (3 experts, 102 items: upper bound). A third of models at or below random. Open-ended quality 2.64 vs 2.62 of 5; humans gave up on 18% | Jiang 2023 [a18, c07, b12] | est |
| Situation puzzles | 975 puzzles. GPT-4 41.70% (easy 70.96, medium 36.88, hard 17.27). GPT-4 Turbo 32.91, WizardLM-2 35.45, Llama3-70B 34.50, Llama3-8B 17.05. BrainTeaser Word Llama3-70B 71.20 to 79.54 after SPLAT data | Chen 2024 [b10, c19] | single |
| Interactive lateral thinking | most LLMs show negligible lateral thinking; no tables read | LatEval [c20] | single |
| Red herrings fixate LLMs | Only Connect: humans 285/494 walls. GPT-3.5/4 0 to 7 of 494 walls on the original set; about 280 to 470 on the WordNet set with red herrings removed | Alavi Naeini 2023 [c08, d10] | est (K12) |
| NYT Connections with red herrings | MPNet 11.6%, GPT-3.5 Turbo 6.43%, GPT-4 Turbo 29.2%; with CoT 38.93% (p<6.77e-5) | Todd 2024 [c22] | single |
| Mental set (Einstellung) in LLMs is inconsistent | 6 problems per cell. GPT-4o shortcut alone 0.33, after complex 0.66; complex alone 0.66, after shortcut 0.83. Llama-70B shortcut 0 then 0.16; Llama-8B 0.16 then 0 | Haq 2025 [a23, c21, d09] | contested (K25) |
| Classic insight problems: results differ by study | Orru: ChatGPT 7/15 and 5/15 (12/30), humans n=20 median 0.55 and 0.35. Speed: analytic problems 0 solved by both models (humans 55% and 61%); insight GPT-3.5 1.5-3.5 of 5 over 4 sessions, GPT-4 4.5 of 5 once. Zhang 2025: GPT-4o above humans on several tasks | [a17, b09, c05, c06, a15] | contested (K13) |
| Search with pruning beats linear CoT | Game of 24, GPT-4: CoT 4%, Tree of Thoughts 74% (IO 7.3%) | Yao 2023 [c16] | single (K14) |
| Stall-triggered replanning in agents | ALFWorld, 134 tasks, 10 seeds: Qwen3-8B 35.1% to 75.4%; GPT-5 46.3% to 88.1%. Beats compute-matched 1-shot LATS by 2.7, ToT by 5.7, Self-Refine by 6.7. Trigger = 5 consecutive low-progress scores | Kadu and Krishnan 2026 [c17] | single |
| Context graph at a rule change | 1,085 trials; Sonnet 4.5 acting. Restructuring accuracy 73.3% (22/30) to 93.9% (31/33), +20.6 points, Fisher p=0.038. Graph accounts for 94% of gain | Alderete 2026 [c18] | single (K15) |
| Cross-family verification beats self-verification | 37 models, 9 benchmarks. Self-verification keywords in 96% of Qwen3 and 73% of DeepSeek outputs vs 1-2% for Llama3 and Qwen2.5 | Lu 2026 [d11] | est (K18) |
| Verification vs more samples at fixed budget | Self-consistency better until about 8x compute. Verification gains 3.8% only at about 128x extra | Singhi 2025 [d12] | single (math) |
| Self-consistent errors evade detectors | Inconsistent-error AUROC up to about 90%; drops sharply on self-consistent errors | Tan 2025 [d13] | single |
| Entropy and loop signals as stop-or-intervene triggers | EAT cuts tokens 12-22% (up to 21% AIME-2025) with no accuracy loss. TrigReason matches full-LRM accuracy with 1.70x-4.79x more steps offloaded; latency -43.9%, cost -73.3% | [d05, d06, d07, d08] | contested as impasse detector (K20) |
| Strategy memory | WebArena +8.3, +7.2, +4.6 over memory-free agents; up to 20% relative, 16% fewer steps. Agents often ignore condensed experience (4 frameworks, 13 backbones, 9 environments) | Ouyang 2026 [d15]; Zhao 2026 [d16] | contested (K24) |
| Long chain beats many short chains where state matters | theory plus experiments on graph connectivity | Mirtaheri 2025 [d04] | single, indirect |
| R1 ruminates | Reconstruction cycles re-examine earlier formulations. AIME 2025, 10,247 steps labelled; reflection helps only inside deductive inference | Marjanovic 2025 [c14]; Chen and Wang 2026 [c13] | single each |

## 4. Mechanisms and models

Each model is stated so that an engineer could write it.

### 4.1 Representational change (Ohlsson; Knoblich et al.)
State: a problem representation R = (objects, operators, constraints, chunks). Search runs inside R.
1. **Search.** Generate moves allowed by R. Check the goal.
2. **Impasse.** No move improves the state, or states repeat. In matchstick work the blocking constraint is implicit (values are fixed, an operator sign cannot change).
3. **Restructure.** Three mechanisms: constraint relaxation (drop one implicit constraint), chunk decomposition (break a tight perceptual or semantic unit), re-encoding (read the same object another way).
4. **Order.** Narrow-scope constraints are relaxed first. Wide-scope ones (tautology) are relaxed last and cost most [a02].
5. **Learning.** Relaxation carries over to later problems needing the same constraint, not by surface similarity [a03].

Agent form: list the implicit constraints in the task, rank by scope, drop one at a time with the widest last, run a code test after each drop (K03, O4).

### 4.2 Progress monitoring and look-ahead (MacGregor et al.)
Hill-climb on a heuristic distance. A monitor checks whether the heuristic is improving. On failure, switch criterion (look further ahead). No special event is needed [b25]. Agent form: the S6 stall detector is this monitor. Impasse becomes a measurable event, not a feeling.

### 4.3 Incubation as three rules
- Unconscious work: spreading activation continues across the break.
- Forgetting of fixation: activation of the wrong cue decays, so the next try starts from a new retrieval.
- Conscious work: the solver keeps trying quietly.

The misleading-cue moderator (0.36 vs 0.17 for linguistic items) supports forgetting [a05]. The low-demand-task advantage supports unconscious work or forgetting, because a demanding task blocks rehearsal [b18]. For an LLM the only analogue of "forgetting the cue" is dropping the cue from context. No measurement exists [d03].

### 4.4 The Aha as a judgement
Aha rating = f(fluency, certainty, pleasure, surprise, first-move correctness) [b14, a12, a27]. It correlates with correctness at group level (r about .4-.5 on classic insight items) and fails at item level (37% of wrong solutions rated above the correct mean) [b13, a10]. Consequence: never gate S8 on a confidence or fluency signal.

### 4.5 Distant semantic integration (Jung-Beeman)
Right-hemisphere coarse coding activates weak, distant associates. Left-hemisphere fine coding keeps close ones. Insight is a late burst that integrates a distant link [a08]. LLM analogue: sampling distant concepts or retrieved distant analogues (O7). Zhang et al. found AI forward flow lower than human, and wrong RAT answers closer in meaning to the stimulus, which they read as local search near the input [a16].

### 4.6 The four stages in a reasoning trace
- Preparation: read, restate, first attempt.
- Impasse: repeated checks or loops with no state change; hesitation phrases; non-falling entropy [d05, d08].
- "Aha" shift: a "wait" or re-read mid-trace. In most cases not a restructuring [a21].
- Verification: re-check. Weak when done by the same model in the same context [c15, d11].

Mizumoto's verification failure shows the bottleneck is the generation-to-endorsement gap, not generation [a19].

### 4.7 Stall detectors
- Token entropy: gates where forced reconsideration helps (top 20% entropy items gained more) [b03]. EAT stabilises when pass@1 plateaus [d06].
- Loop and hesitation counts: used in TrigReason [d05].
- Consecutive low-progress scores (m=5): ReflexGrad [c17].
- Answer repetition: unreliable under self-consistent errors [d13].
- The model's own "stuck" rating: r=.17 per SCHEMA S6, unreliable.

No signal has reported impasse precision and recall (K20).

## 5. What holds up

### 5.1 Replicates or has several sources
- Constraint-scope difficulty and transfer in matchsticks: two experiments in the original, and no failed replication of the core found [a02, a03, d01]. The Knoblich statistics could not be re-verified from the PDF text.
- Small positive incubation effect: Sio and Ormerod, Gilhooly. Size depends on pooling: weighted 0.29, unweighted 0.41, eight intermittent-work tests r=0.11 [a04, b17].
- Break task moderates incubation: undemanding task beats demanding task or rest [a04, b18].
- False insights exist: Danek and Wiley 2017, 2020 (replicates the Aha-recall link, d=.51), Wiley and Miller 2026 [b13, b15, a12].
- Insight solutions are remembered better, but the cause is correctness, certainty and pleasure, not restructuring itself [b15]. Kizilirmak: generation, not Aha, predicts memory [b27].
- LLM "aha" is rare and not a quality marker: Illusion of Insight, Liu et al., Wu et al., and a blog cited by the DeepSeek paper itself [a21, c11, b05, b04].
- Intrinsic self-correction does not help; external signals do [c15, d11, d13].

### 5.2 Failed replications, boundary conditions, rivals
- Interactivity on matchsticks failed in three experiments (N=105, 88, 73). Movement hurt relaxing high-level constraints [d01]. Do not credit acting on a problem as a restructuring aid.
- The Aha-accuracy link is task-dependent: strong on classic insight and CRA, near zero for non-insight in Exp 1 (r .02) [a10].
- The Aha-correctness effect arises only after a correct first move [a27].
- Incubation is stronger for divergent tasks than insight tasks [a04]. It is stronger with misleading cues for linguistic items only [a05]. High-demand break tasks shrink it. One RAT quasi-experimental study found no incubation effect (snippet only) [d02].
- SCHEMA 4b lists "incubation by distraction (sleep on it)" as not to add, because unconscious-thought effects failed to replicate (F03, F04). The human meta-analysis shows a small effect, so the two claims differ. For an LLM neither has a measured analogue. See section 9.
- Impasse may not be a prerequisite (Weisberg; one later study) [b20, snippet]. Nearly 20% of one sample never reported an insight [a01].
- Small samples: Knoblich Exp 1A N=20, Jung-Beeman N=13, Orru N=20 humans, Alderete 30 vs 33 [critique].

### 5.3 Interventions that worked
Humans: low-demand break (K01); relaxing wide-scope constraints, with transfer (K03).
LLMs: externally triggered reconsideration at high entropy on math (+8.41 pp, two passes, no equal-token control) [b03]; search with pruning on Game of 24 (4% to 74%) [c16]; red-herring removal [c08]; CoT on Connections (29.2% to 38.93%) [c22]; reasoning-inclusive few-shot on riddles [a20]; context graph at rule change (+20.6 points, n=63) [c18]; stall-triggered replanning in ALFWorld [c17]; cross-family verifiers [d11].

### 5.4 Interventions that did not work
Intrinsic self-correction [c15]. Spontaneous "wait" shifts [a21]. Same-model verification at low budget [d12, b05]. Forced reconsideration on crosswords and Rush Hour (+0.45, +0.01 pp) [b03]. Thinking in Japanese vs English [b08]. Interactivity [d01]. Parameter count as a predictor of riddle accuracy (release date did predict) [c01].

## 6. Language models

### 6.1 Performance on insight-type tasks
- **Older, public items (2023).** ChatGPT matched the modal human on 30 verbal insight problems (12/30) [b09]. GPT-4 scored 4.5 of 5 insight items once, while both models failed the analytic items that humans solved 55-61% of the time [c05]. Zhang et al. (GPT-3.5, GPT-4, GPT-4o) found models above humans on divergent and convergent tasks and several insight tasks, but weaker in creative writing and in representational-change process [a15]. These items are public, so contamination is a plausible cause of high scores.
- **Fresh or adversarial items.** BRAINTEASER: 53% / 63% vs 92% human, worse under rewritten forms [c07]. Nazonazo: reasoning 17.6%, non-reasoning 7.6%, human 52.9% [a19]. SPLAT: GPT-4 41.70%, hard 17.27% [c19]. Only Connect and NYT Connections: single digits until red herrings are removed or CoT is used [c08, c22]. LatEval: negligible interactive lateral thinking [c20]. MacGyver: GPT-4 18.9% efficient solutions and 37.5% infeasible; majority-vote correct humans 79.3% vs GPT-4 73.3% [c09].
- **Why studies disagree.** Item age (contamination), tiny N, partial credit, zero-shot retrieval-free protocols [critique]. Treat the older "models are good" results as weak.

### 6.2 What changed performance, and by how much

| Change | Effect | Source |
|---|---|---|
| Reasoning model vs non-reasoning | 7.6% to 17.6% (120 items); OR 2.29 on 201 | [a19] |
| Release date | predicts accuracy; parameter count does not | [c01] |
| Reasoning-inclusive few-shot demos | up in 4 of 4 models, significant in 2 | [a20] |
| CoT on Connections (GPT-4 Turbo) | 29.2% to 38.93% | [c22] |
| Remove red herrings (Only Connect) | single digits to hundreds of 494 walls | [c08] |
| Tree of Thoughts on Game of 24 | 4% to 74% | [c16] |
| Entropy-gated second pass, math | 32.21% to 40.62% | [b03] |
| Same pass, crosswords and Rush Hour | +0.45 and +0.01 pp | [b03] |
| Context graph at rule switch | 73.3% to 93.9% | [c18] |
| Stall-triggered replanning (Qwen3-8B, ALFWorld) | 35.1% to 75.4% | [c17] |
| Training on lateral data (SPLAT) | BrainTeaser Word Llama3-8B 46.20 to 58.07 | [b10] |
| Intrinsic self-correction | CSQA 75.8 to 38.1 (GPT-3.5); GSM8K 95.5 to 89.0 (GPT-4) | [c15] |

### 6.3 The "Aha moment" in reasoning models
DeepSeek-R1-Zero showed a jump in the word "wait" while AIME24 pass@1 rose from 15.6% to 77.9% [b04]. Follow-up work did not support a link between that behaviour and accuracy. Base models already show it [c11]. Shifts appear in 6.31% of traces, but only 0.40-0.60% for DeepSeek-R1 and 2.20-3.00% for GPT-4o [b01]. Yang et al. found "aha" models (R1-distilled 1.5B-14B) use more first-person phrasing, tie uncertainty to difficulty and ruminate less, on Knights and Knaves and Countdown, with no single accuracy headline [c10]. R1 loops through local checks and ruminates [c13, c14].

### 6.4 Verification
The generation-endorsement gap is the clearest insight-stage finding for LLMs: the right candidate appears in the trace, then is rejected (5.23-39.34% of wrong answers) [a19]. Self-verification is the weakest verifier and cross-family the best [d11]. At fixed budget, more independent samples beat verification up to about 8x compute [d12]. Self-consistent errors escape consistency checks [d13]. No verifier has been tested on insight riddles at equal tokens.

### 6.5 What is missing
No LLM incubation, context-reset or parked-subproblem study on RAT or compound RAT was found (about 6 queries; d03). No post-2025 frontier measurement of the red-herring penalty with a drop-the-cue remedy. No equal-token control for any insight-style operator (critique GAPS 1-3). Search tools were rate-limited, so "none found" is weak evidence.

## 7. What our agent should take

Marks follow SCHEMA: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not treat any "Aha", sudden confidence or mid-trace "wait" as a sign that an answer is right or that a restructuring happened. Do not reward restructuring phrases in selection. | G10, S6 | [E] | K04, K07; a11, b13, a21, b01, c11, b05 |
| A2 | S8 uses a check independent of the solving context: a tool, a constraint test, a fresh second context, or a different-family verifier. Same-context re-reading is not verification. | S8, G2, G3 | [E] | K09, K18; c15, d11, d13 |
| A3 | Restructuring operators stay at impasse only (already G1/S6). Spontaneous shifts do not help and unprompted reflection hurts. | G1, S6 | [E] | K07, K09; a21, c15 |
| A4 | Misleading cues carry a measured penalty on insight-style items. S1 input hygiene should move suggestive or plausible-but-wrong cues out of the attempt context. | S1 | [E] penalty; remedy [S] | K12; c08, c22 |
| A5 | S9 stores the checked solution plus the restructuring step plus the outcome. Do not store a "felt insight" flag. The human memory advantage tracks correctness and certainty. | memory, S9 | [E] human effect; format [S] | K06; b15, b27, d15 |
| A6 | Constraint listing as the body of O4: name implicit constraints, rank by scope, relax one at a time, widest last, test after each. Human basis [E]; LLM effect untested. | O4 | [E] human, [S] LLM | K03; a02, a03 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Stall- or entropy-triggered second pass vs matched best-of-2 and continued CoT at equal tokens | S6, O6 | [S] | K08; b03, d12 |
| T2 | Drop the misleading context at impasse (fresh context, no hint text) vs keep it | S6, O6, S1 | [S] | K02, K25; a05, c08, d09 |
| T3 | Incubation analogue: park the impasse, do an unrelated low-load subtask, retry in a fresh context. SCHEMA 4b excludes "incubation by distraction"; this test is for the context-reset form only | S6 | [C] | K01, K23; a04, d03, d04 |
| T4 | Stall detector precision and recall: entropy, repetition, hesitation words, step count | S6 | [C] | K20, K21; d05-d08, d13 |
| T5 | Harvest all candidates plus independent scoring vs last answer | S4, S8 | [S] | K11; a19, d11 |
| T6 | Cross-family verifier vs same-model re-check on wrong-then-rejected cases | S8 | [E] direction, [S] on riddles | K18, K19; d11, d12 |
| T7 | Backtrack-on-stall search vs linear CoT | S6, O6 | [S] | K14; c16, c17 |
| T8 | Constraint-graph scaffold at a rule change | O6 | [S] | K15; c18 |
| T9 | Ablate the impasse trigger: restructure at fixed intervals vs only on detected stall | S6, G1 | [C] | K17; b20 |
| T10 | Is the stored restructuring note causally used? Perturb the note | memory | [C] | K24; d15, d16 |
| T11 | Distant retrieved analogue or concept at impasse (the aSTG analogue) | O7 | [S] | K16; a08, a16 |

## 8. Concrete tests on our bench

All arms get the same total tokens, counting setup and any second pass. Report item-level variance. Use fresh, post-cutoff items only (K13).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | MATH-500-style math; Rush Hour-style planning; cryptic crosswords | (a) one long CoT; (b) best-of-2 plus vote; (c) entropy-gated reconsideration; (d) fixed-interval reconsideration | solve rate; wrong-to-right vs right-to-wrong counts | (c) beats (a); (c) vs (b) is the real question. Prior: gain on math only [b03] |
| B2 (T2) | Nazonazo-style riddles, Only Connect, BrainTeaser, each with a planted plausible red herring | (a) keep hint; (b) O6 drop-the-hint at impasse; (c) hint never shown (ceiling) | accuracy drop vs clean item; share of drop recovered | (c) > (b) > (a). Expect partial recovery |
| B3 (T3) | Compound RAT, 3-word problems, with a misleading-cue subset | (a) continue; (b) fresh-context resample; (c) park, 100-300 token unrelated task, then fresh retry; (d) same-length continued CoT | solve rate; items solved only by one arm | small effect at most (human d about .29; 0.36 vs 0.17 with misleading cue) |
| B4 (T4) | Traces labelled stalled vs productive on held-out items | entropy, repetition, hesitation words, step count, combined | precision, recall, AUC for "no new answer in next k tokens" | entropy and loops best; repetition fails on self-consistent errors [d13] |
| B5 (T5, T6) | Nazonazo and BrainTeaser items with logged candidates | (a) last answer; (b) harvest plus same-model verifier; (c) harvest plus cross-family verifier; (d) N samples plus vote | accuracy; verification-failure rate | (c) > (b); (d) strong at low budget [d12] |
| B6 (T7) | Game of 24 style, small search tasks | CoT; backtrack-on-stall; ToT-style search | solve rate | stall-triggered search wins where dead ends exist |
| B7 (T8) | Rule-switch tasks (blicket-type) | base; constraint-graph scaffold; list-constraints prompt | accuracy after the switch | up to +20 points if it replicates |
| B8 (T9) | Mixed insight and routine items | stall-only; fixed-interval; never | accuracy; token cost | G1 predicts stall-only wins on routine items |
| B9 (T10) | Sequences of related tasks | memory: answer only; answer plus restructuring note; note perturbed | later-task accuracy; behaviour change on perturbation | note helps only if causally used |

## 9. What does not transfer, and why

- **The felt Aha.** A feeling in a human, reported afterwards. Not a cause (G10). Its link to correctness holds on average and fails per item [b13, K04].
- **Neural signatures (right aSTG, gamma burst).** About brains. N=13, no online signal for a model [a08, K16].
- **Incubation as rest.** A model has no continuing process between calls. Human mechanisms (activation decay, mind wandering, sleep) have no direct analogue. Only context reset and an interpolated low-load task can be modelled, and both are untested. SCHEMA 4b excludes distraction-based incubation. Keep that until T3 passes.
- **Sleep and break-length findings** (Segal 2004, Wagner 2004) [a01]. Human physiology.
- **Matchstick interactivity.** Failed replication even in humans [d01]. The agent has no physical interaction.
- **Mooney-image and visual insight.** Visual cortex results [a14] do not map to text tasks. Incubation gain is clearer for linguistic than visual problems [a05].
- **Human insight items as LLM tests.** Old public items (Ansburg and Dominowski, Duncker, Maier) are probably in training data. Orru and Speed may measure retrieval [critique].
- **Individual differences and mood.** No agent counterpart.
- **The human ceiling in BRAINTEASER.** 92% is three experts on 102 items: an upper bound, not a typical human [critique 4].
- **Small-model GRPO findings.** Illusion of Insight trains Qwen 1.5B/7B and Llama 8B. Transfer to frontier models is unknown [critique].

## 10. Open questions

1. Does an entropy- or stall-triggered O6 beat best-of-2 and continued reasoning at equal tokens? No paper has this control.
2. What does an LLM incubation analogue do on RAT or compound RAT? Nothing measured.
3. What is the fixation penalty on post-2025 frontier reasoning models, and does dropping the cue recover it?
4. Which stall detector works, with what precision and recall? Partly closed: signals exist for stopping, none validated for impasse.
5. Can S8 be made reliable when the same model produced and rejected the right answer? Does an independent verifier fix it on insight items?
6. Are verbal-confidence jumps in LLMs predictive of correctness? Trace shifts say no; verbal confidence is untested.
7. Do human boundary conditions (verbal vs visual, break demand, length, individual differences) carry over to LLM tasks?
8. Is the Knoblich result safe from replication failure? None found for the core, but the search was limited.
9. Does storing the restructuring step help reuse in an agent, given agents ignore condensed notes?
10. Does Alderete's context-graph result replicate beyond one model family and 63 trials?
11. Is impasse a prerequisite for insight, or only a common antecedent (Gestalt vs Weisberg)?
12. Is there any LLM signal that mirrors the human Aha-accuracy link (r .4-.5)?

## 11. Sources

[V] = opened (evidence line opened:true). [M] = snippet only or not opened.

- [V] Wikipedia, Insight. https://en.wikipedia.org/wiki/Insight (a01)
- [V] Knoblich, Ohlsson, Haider, Rhenius (1999) Constraint relaxation and chunk decomposition in insight problem solving. https://www.kognition.uni-koeln.de/literature/ (a02, a03; statistics not re-verified)
- [V] Sio and Ormerod (2009) Does incubation enhance problem solving? Psychological Bulletin. https://www.Gwern.net/doc/psychology/writing/2009-sio.pdf ; https://pubmed.ncbi.nlm.nih.gov/19210055/ (a04-a07, b19)
- [V] Jung-Beeman et al. (2004) Neural activity when people solve verbal problems with insight. https://pmc.ncbi.nlm.nih.gov/articles/PMC387268/ (a08, a09)
- [V] Webb, Little, Cropper (2016) Insight is not in the problem. https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01424 (a10, b16)
- [V] Danek and Wiley (2017) What about false insights? https://pmc.ncbi.nlm.nih.gov/articles/PMC5247466/ (a11, b13, b14)
- [V] Danek and Wiley (2020) What causes the insight memory advantage? Cognition. https://www.gwern.net/doc/psychology/ (b15)
- [V] Wiley and Miller (2026) Aha ratings as metacognitive judgments. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608503/ (a12, a24, a27)
- [V] Kim (2026) Illumination onset. https://pmc.ncbi.nlm.nih.gov/articles/PMC13701766/ (a13)
- [V] Becker et al. (2025) Insight predicts subsequent memory via cortical representational change. https://pmc.ncbi.nlm.nih.gov/articles/PMC12064812/ (a14)
- [V] Zhang et al. (2025) AI delivers creative output but struggles with thinking processes. https://arxiv.org/abs/2503.23327 (a15, a16)
- [V] Orru et al. (2023) Human-like problem-solving abilities in LLMs using ChatGPT. https://pmc.ncbi.nlm.nih.gov/articles/PMC10244637/ (a17, b09, c06)
- [V] Jiang et al. (2023) BRAINTEASER. https://arxiv.org/abs/2310.05057 (a18, b12, c07)
- [V] Mizumoto et al. (2025/2026) The metacognitive bottleneck: Japanese riddles. https://arxiv.org/abs/2509.14704 (a19, a20, b06-b08, c01-c04)
- [V] d'Aliberti and Ribeiro (2026) The illusion of insight in reasoning models. https://arxiv.org/abs/2601.00514 (a21, b01-b03)
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948 (a22, b04); c12 is [M]
- [V] Haq et al. (2025) Is your LLM trapped in a mental set? https://arxiv.org/abs/2501.11833 (a23, c21, d09)
- [M] Ohlsson (1992) Information-processing explanations of insight (a25)
- [V] Vallee-Tourangeau et al. (2020) Incubation and interactivity in insight problem solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC6994426/ (a26)
- [V] Wu et al. (2025) Aha Moment Revisited. https://arxiv.org/pdf/2506.17417v3 (b05)
- [V] Chen et al. (2024) SPLAT. https://arxiv.org/abs/2410.06733 (b10, c19)
- [M] McCoy (2025) Creativity or brute force? https://arxiv.org/abs/2505.10844 (b11, abstract only)
- [V] Gilhooly (2016) Incubation and intuition in creative problem solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC4956660 (b17, b18)
- [M] Weisberg (2015) Toward an integrated theory of insight. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6352738/ (b20)
- [M] Wallas (1926) The Art of Thought (b21); Metcalfe and Wiebe (1987) (b22); Schooler, Ohlsson, Brooks (1993) (b23); MacGregor, Ormerod, Chronicle (2001) (b25); Becker, Kuhn, Sommer (2021) (b26); Kizilirmak et al. (2019) (b27)
- [V] Alavi Naeini et al. (2023) LLMs are fixated by red herrings. https://arxiv.org/abs/2306.11167 (c08, d10)
- [V] Tian et al. (2023) MacGyver. https://arxiv.org/abs/2311.09682 (c09)
- [V] Yang et al. (2025) Understanding aha moments. https://arxiv.org/abs/2504.02956 (c10)
- [V] Liu et al. (2025) Understanding R1-Zero-like training. https://arxiv.org/abs/2503.20783 (c11)
- [V] Chen and Wang (2026) Anatomy of human and DeepSeek-R1 mathematical reasoning. https://arxiv.org/abs/2606.07410 (c13)
- [V] Marjanovic et al. (2025) DeepSeek-R1 Thoughtology. https://arxiv.org/abs/2504.07128 (c14)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c15)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c16)
- [V] Kadu and Krishnan (2026) ReflexGrad. https://arxiv.org/abs/2511.14584 (c17)
- [V] Alderete et al. (2026) Separable pathways for causal reasoning. https://arxiv.org/abs/2604.20039 (c18)
- [V] Huang et al. (2024) LatEval. https://arxiv.org/abs/2308.10855 (c20)
- [V] Todd et al. (2024) Missed Connections. https://arxiv.org/abs/2404.11730 (c22)
- [V] Gao et al. (2024) Creativity in AI survey. https://arxiv.org/abs/2410.17218 (c23)
- [V] Speed (2023) Assessing the nature of LLMs: a caution against anthropocentrism. https://arxiv.org/abs/2309.07683 (c05)
- [M] Kaplan and Simon (1990) In search of insight. https://doi.org/10.1016/0010-0285(90)90023-5 (c24)
- [V] Spiridonov et al. (2026) Interactivity and matchstick problems, Frontiers in Psychology. https://www.frontiersin.org/journals/psychology/ (d01)
- [M] Collier and Beeman; Valueva 2024 on incubation and RAT (d02). https://psyjournals.ru/en/journals/chp/archive/2024_n4/
- [V] Mirtaheri et al. (2025) Let me think! https://arxiv.org/abs/2505.21825 (d04)
- [V] Zhao et al. (2026) TrigReason. https://arxiv.org/abs/2604.14847 (d05)
- [V] Wang et al. (2026) EAT: Entropy after think. https://arxiv.org/abs/2509.26522 (d06)
- [V] Guan et al. (2026) Mitigating overthinking via path deviation. https://arxiv.org/abs/2603.14251 (d07, abstract and intro only)
- [M] NeuReasoner. https://arxiv.org/abs/2604.02972 (d08)
- [V] Lu et al. (2026) When does verification pay off? https://arxiv.org/abs/2512.02304 (d11)
- [V] Singhi et al. (2025) When to solve, when to verify. https://arxiv.org/abs/2504.01005 (d12)
- [V] Tan et al. (2025) Too consistent to detect. https://arxiv.org/abs/2505.17656 (d13)
- [V] Ouyang et al. (2026) ReasoningBank. https://arxiv.org/abs/2509.25140 (d15)
- [V] Zhao et al. (2026) LLM agents are not always faithful self-evolvers. https://arxiv.org/abs/2601.22436 (d16)
- [V] Liu, Karimnazarov, White (2025) Trapped by expectations. https://arxiv.org/abs/2504.02074 (d18; human users, not model fixation)
- [M] Segal (2004); Wagner et al. (2004); Ovington et al. (2015); Strick et al. (2011): known only via Wikipedia and Gilhooly.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 9 established claims: 6 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B01.03-K01** (reworded: the sources support less). Sio and Ormerod verified (117 studies, 3,606 participants, weighted mean d 0.29 CI 0.21-0.39, unweighted 0.41; Gilhooly 2016 confirms), but the pooled effect spans insight and divergent-thinking tasks, with divergent thinking benefiting MORE than linguistic and visual insight; the low-demand-beats-rest result holds specifically for linguistic insight problems. Corrected claim: Incubation breaks give a small, reliable benefit on problem solving overall (weighted d about 0.29; unweighted 0.41), larger for divergent-thinking than for insight tasks; the effect depends on the break task: high-demand fillers reduce it, and undemanding interpolated tasks beat rest for linguistic insight problems.
- **B01.03-K06** (reworded: the sources support less). Danek and Wiley 2020 give 57.7% vs 35.4% recalled after one week, but for correct vs incorrect solutions, and conclude that the advantage comes from correctness, certainty and pleasure and did not seem to rely on sudden restructuring; the 'partly via surprise and restructuring' part is not supported by that paper (only the Becker et al. 2025 fMRI study links representational change to later memory). Corrected claim: Correct solutions are remembered better one week later than incorrect ones (57.7% vs 35.4% recalled), mainly through correctness, certainty and pleasure rather than sudden restructuring (Danek and Wiley 2020); an fMRI study (Becker et al. 2025) links representational change and hippocampal activity to later memory.
- **B01.03-K09** (number corrected). Huang et al. Table: GPT-3.5 CommonSenseQA 75.8->38.1 is round 1 (round 2 is 41.8), while GPT-4 GSM8K 95.5->89.0 is round 2; 'by round 2' misattributes 38.1. Also oracle gain is real (GPT-3.5 GSM8K 75.9->84.3, CSQA 89.7). Corrected claim: Intrinsic self-correction without external feedback does not help and often hurts (GPT-3.5 CommonSenseQA 75.8 to 38.1 after round 1 and 41.8 after round 2; GPT-4 GSM8K 95.5 to 89.0 by round 2); oracle labels help, so the gain comes from the external signal.
