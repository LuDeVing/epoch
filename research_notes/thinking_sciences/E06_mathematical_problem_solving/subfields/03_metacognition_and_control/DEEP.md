# Metacognition and control: deep document

*Subfield E06.03. Key works: Schoenfeld 1981, 1982, 1983, 1985, 1992; Garofalo and Lester 1985. Why it matters: S6 trigger rules. Built from evidence_a-d.jsonl (a01-a26, b01-b27, c01-c25, d01-d22), claims.jsonl (K01-K28) and critique.md in this folder. Evidence ids below refer to those files. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested.*

Read this first: the human core of this field is small-N and mostly qualitative. The hard numbers come from language-model studies, and almost none of those test Schoenfeld's actual control rules. Many links in this document are our own analogies. They are flagged as such.

---

## 1. What it is

Metacognition and control is the part of problem solving that does not solve anything itself. It watches the solving and decides what happens next. In Schoenfeld's four-part framework (a10, not opened; recalled) the layers are: resources (knowledge), heuristics, control, and belief systems. Control is the manager. It decides which resources and heuristics to use, how long to keep going, and when to quit.

Three functions matter for our agent.

1. **Monitoring.** Is this line making progress? Is the answer reasonable? Do I understand what I am doing and why?
2. **Abandoning.** When monitoring says "no", stop the line, say why, and keep whatever the line taught you.
3. **Committing.** Choosing an approach on purpose, with a reason, rather than by the first thing that comes to mind.

The failure Schoenfeld named is the **wild goose chase**: a quick choice of approach, then long pursuit with no check on progress (a03, a08, b05). The mirror failure, found later in language models, is **underthinking**: dropping promising lines too soon (a21). A third, also found in models, is **overthinking**: carrying on after the answer is already right (a20).

For our agent, S6 (impasse) is the control layer. This document is about when S6 should fire, what it should look at, and what it should do. The schema already says S6 fires on: no pass, two rounds with no change, the same error twice, or a budget fraction spent. This document tests that list against the evidence and suggests additions.

Related subfields researched in the same run (not covered here): Monitoring and control framework, Impasse-driven subgoaling and chunking, Metacognition of insight, Heuristic search, Human error and recovery, Sampling and voting. Where they overlap, see their documents.

---

## 2. History and theories in depth

### 2.1 Flavell and the term (1979)

Flavell (1979) introduced metacognition as knowledge about, and regulation of, one's own cognition, including monitoring experiences and strategy choice (a23). This session did not open it. Do not cite figures from it.

### 2.2 Schoenfeld's episode analysis (1981-1982)

**Method.** Schoenfeld recorded students and experts thinking aloud and cut each protocol into macroscopic episodes: Reading, Analysis, Exploration, Planning, Implementation, Verification, Transition (a01). Managerial decisions are judged at the joints between episodes. Inter-coder reliability between the author and three student coders exceeded 85% (a06). That is agreement on episode parsing. Whether a managerial decision was good stayed a subjective judgment.

**Three loci of control decisions (a02).** A decision is due:
1. at the junction between episodes, when direction changes;
2. when new information or a new idea arrives, even mid-episode;
3. when a run of tactical failures occurs (implementation bogs down, or exploration turns unstructured).

Schoenfeld called the third hard to code in 1981: "no easy way" to detect it. A program can code it as "no change in K steps". The second locus, "a new idea surfaced", is not in our schema yet.

**The founding cases (a03, a04, a05).**
- Circle and triangle. Two students were asked for the largest triangle inscribed in a circle. They guessed equilateral and spent about 20 minutes computing its area. Nobody asked what the area would buy. At least three salvaging ideas (calculus max-min, a rectangle in a circle, varying the shape) surfaced and faded. Neither student could say afterward what the area would be used for (a03).
- Second pair. They casually adopted a symmetry assumption that assumed what had to be proved. That one choice steered more than 60% of the allotted time. They then turned from the failed attempt without asking what could be learned from it (a05).
- Expert contrast. An expert interrupted a half-built solution with "this is too complicated" and stopped. Novices had no such termination rule once a chase began (a04).

Two separate control failures show up: **unjustified commitment** and **abandoning with nothing salvaged**.

**The 7 of 12 figure.** In Schoenfeld (1983), of twelve recorded sessions in a 1981 experiment, seven were of the type "read, then go on a wild goose chase" (a08). That is 58% of N=12 in one lab with college students. This is the number most often retold from this literature. It was read in the 1983 paper only. The 1985 book (a10, b05) was never opened, and no replication of the rate was found.

**Why control failures stay hidden (a09).** College freshmen see their minds as autonomous and just do what comes to mind. The cost of bad control is not immediate, so failure is blamed on something else. Teachers show finished, schema-based solutions, so students never see anyone think. The fix Schoenfeld proposed is a teacher who keeps asking three questions: What exactly are you doing? Why are you doing it? How does it help you? This is a design proposal with classroom anecdotes, not a measured effect.

**Warning on method (a12).** Lone-student think-aloud sessions on a volume-estimation problem gave odd behaviour (very exact body-volume calculation, crude cell-size guesses). About two dozen student pairs on the same problem never showed it. Schoenfeld calls it pathology induced by the setting. So think-aloud can create the control failure it studies.

### 2.3 Problem perception (Schoenfeld and Herrmann 1982)

A card-sort study. After a month-long problem-solving course, novices sorted problems more by deep structure and scored far higher on a test (a07). It is an input to control, not control itself. See Section 3 for numbers.

### 2.4 Beliefs (Schoenfeld 1985)

A questionnaire of 230 grade 9-12 students: almost half view maths as mostly memorising; three quarters think it helps a person think logically (a11). The paper also quotes earlier studies in which over 90% of subjects solved a construction problem by trial and error, accepting or rejecting on empirical grounds only. The 90% figure comes from other studies cited in that paper.

### 2.5 Garofalo and Lester (1985) and the Lester studies (1989)

Garofalo and Lester proposed a four-phase cognitive-metacognitive framework: orientation, organisation, execution, verification (a13, b26; article not opened; phases confirmed only through the 1989 report). Lester, Garofalo and Kroll (1989) ran 12 weeks of metacognition-based instruction in two grade 7 classes (a14, b01, b02). Results were modest and are in Section 3. The authors list insufficient assessment of progress and of reasonableness of results as resistant to change even after explicit instruction. One student became overconfident and stopped rereading. Their reasons for weak change (too little time, regular lessons reinforcing old habits, problem solving seen as separate from maths, tests rewarding old habits) are their own and untested.

### 2.6 Later human work

- Calibration of confidence predicts later arithmetic growth (Rinne and Mazzocco 2014; b03).
- Postreflection exercises in physics gave a small difference, better explained by pretest score than by treatment (b04, abstract only).
- Self-regulated-learning training meta-analysis (Dignath and Buettner 2008; d21, abstract page only). Details in Section 3.
- Lester (1994) was expected to judge the 1980s metacognition work promising but thin on training effects (a24; recalled, not opened).

### 2.7 The turn to language models

Since 2022 the same ideas reappear in LLM work under new names.
- **Calibration and "knowing what you know"** (Kadavath 2022; a17, c21).
- **Self-correction** (Huang 2024; Kamoi 2024; Tyen 2024).
- **Overthinking and underthinking** of reasoning models (Chen 2025; Wang 2025).
- **Early exit** from reasoning chains (DEER, Certaindex, answer convergence, probes).
- **Reflexion**: an explicit stuck rule that triggers a written lesson (Shinn 2023).

Almost none of this tests Schoenfeld's rules. It tests relatives: confidence thresholds, answer stability, switch counts. That gap is the main point of Section 10.

---

## 3. Core findings with exact numbers

Status column: E established, S single-source, C contested, H human-only, O older models only.

### 3.1 Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Wild goose chase is common in novice sessions | 7 of 12 sessions (58%) were "read, then wild goose chase"; one lab, college students | Schoenfeld 1983 (a08) | S, H; rate unreplicated, book not opened |
| One casual commitment can eat most of the session | A symmetry assumption steered over 60% of allotted time | Schoenfeld 1981 (a05) | S, H; one case |
| A 20-minute chase can happen with no check | Equilateral triangle area for ~20 min; at least 3 salvaging ideas dropped | Schoenfeld 1981 (a03) | S, H; one protocol |
| Episode coding is reliable at the macro level | Inter-coder reliability above 85% (author plus 3 coders) | Schoenfeld 1982 (a06) | S, H; agreement on parsing, not on decision quality |
| A problem-solving course shifts perception to deep structure | Test mean 21 to 73 (course, n=11) vs 14 to 24 (programming control, n=8); term x group F(1,17)=48.2, p<.001; experts' deep-structure pairs .67 (8 of 12) vs surface .25 (3 of 12) | Schoenfeld and Herrmann 1982 (a07) | S, H; control group paid, course group enrolled |
| Beliefs: maths as memorising | N=230, grades 9-12; almost half "mostly memorising"; three fourths "helps think logically" | Schoenfeld 1985 (a11) | S, H; self-report |
| 12-week metacognitive instruction, grade 7 | Regular class N=22: 4.73 to 6.00; advanced class N=34: 6.74 to 8.38 (max 10, ceiling); no control class; no significant correlations between metacognitive items and test scores | Lester et al. 1989 (a14, b01) | S, H; modest, confounded |
| Orientation phase mattered most | Of four categories, orientation was most related to success | Lester et al. 1989 (a14, b01) | S, H |
| Calibration predicts arithmetic growth | Grade 5 calibration predicts grade 8 minus grade 5 correct count: B=6.92, beta=.269, p=.003, partial r=.25; about 190 children; model R2 about .53 | Rinne and Mazzocco 2014 (b03) | S, H; arithmetic, observational |
| Self-regulated-learning training works on average | 84 studies (49 primary, 35 secondary), 357 effects, mean d = 0.69; higher in maths than in reading; higher when researchers delivered it | Dignath and Buettner 2008 (d21) | S, H; abstract page only; maths-only d not found |
| Reflection after problems | Small significant exam-rubric difference, better explained by pretest score | PRPER 2022 (b04) | S, H; physics; abstract only |

### 3.2 Language models: self-correction and error finding

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Blind self-correction does not help | GPT-3.5 GSM8K 75.9 / 75.1 / 74.7 (standard / round 1 / round 2); CommonsenseQA 75.8 / 38.1 / 41.8; GPT-4 GSM8K 95.5 / 91.5 / 89.0; Llama-2 GSM8K 62.0 / 43.5 / 36.5 | Huang 2024 (a16, b07, c04) | E, O |
| Earlier gains came from oracle labels | With oracle: GPT-3.5 GSM8K 84.3, CSQA 89.7, HotpotQA 29.0; GPT-4 97.5 / 85.5 / 59.0. GPT-3.5 kept its first GSM8K answer 74.7% of the time; changes went more often correct to wrong | Huang 2024 (a16, c03) | S, O |
| Survey: no fair-setting success from prompted self-feedback | Works with reliable external feedback, large-scale fine-tuning, or decomposable answers | Kamoi 2024 (a15, b09, c08, d09) | E, O (to May 2024); abstract and intro read |
| Sound external verifier works; self-critique hurts | Game of 24: standard 5%, LLM critiques LLM 3%, LLM plus sound verifier 36-38%, sampling k=15 28%, k=25 42%. Graph colouring 16% to 2%. Blocksworld 40% to 55% (a rise) | Stechly 2024 (d08) | E, O; 100 items per domain |
| Models bias toward own output | Bias present in all 6 LLMs and tasks (100 MATH items); self-refine raises it. GPT-4 recognises own text 73.5% | Xu 2024 (d04); Panickssery 2024 (d03) | S, O |
| Finding the error is the bottleneck, fixing is easy | BIG-Bench Mistake, 5 tasks, GPT-4 52.87 mistake finding; GPT-3.5 as low as 10.10. With true location: +18.04 to +43.92 points on wrong traces, 0 to -11.43 on right ones. With random location: +5.16 to +21.57, losses to -15.91. Gains held down to ~60-70% location accuracy | Tyen 2024 (b08, c06) | E, O; PaLM 2 traces, symbolic tasks |
| Step-level error finding in maths | ProcessBench average F1: o1-mini 87.9, QwQ-32B-Preview 71.5, GPT-4o 61.9, trained PRM 45.5; Omni-MATH o1-mini 87.2, GPT-4o 51.4, PRM 12.7 | Zheng 2025 (b24, c20, d06) | E |
| Long reasoning chains are much harder to critique | DeltaBench best critic F1 40.76 (GPT-4-turbo); GPT-4o 30.49; R1 24.73; o1-preview 19.89; best PRM 29.22; 27% of sections redundant; R1 self-critique 36% lower than critique of others | He 2025 (d05) | S |
| A thinking verifier beats a plain judge | OlympiadBench / OmniMath F1: R1-Qwen-14B judge 72.8 / 67.8 (13.3% / 18.6% invalid); ThinkPRM 87.3 / 85.7 (2.3% invalid). 1.5B judge: 5.0 / 5.4 (51% / 55% invalid) vs ThinkPRM 76.3 / 75.7 | Khalifa 2025 (d07) | S; needs fine-tuned verifier |
| Own-error blind spot | 14 open non-reasoning models: 64.5% average blind spot; 62.8% outside maths; Claude 3.5 Haiku 52.5%, Sonnet 4 41.4%. On natural errors only 4.3-10.8% caught once shown as external. Appending Wait cut the blind spot 89.3%; fine-tuning on 5,306 traces 76.0% | Tsui 2026 (c17, d01) | S; injected errors mainly |
| Reasoning models have little blind spot | Macro accuracy base / base+Wait / reasoning: DeepSeek-V3 0.567 / 0.902 / 0.908; Qwen3-14B 0.117 / 0.868 / 0.843; Qwen3-32B 0.045 / 0.793 / 0.894; phi-4 0.325 / 0.701 / 0.707 | Tsui 2026 (d02) | S |
| Trace text is not a faithful monitor | Hints verbalised usually under 20%; faithfulness 25% (Claude 3.7 Sonnet), 39% (R1); reward hacks used on over 99% of prompts, verbalised under 2% | Chen 2025b (b17) | S here (schema cites 4 sources for G10) |

### 3.3 Language models: when to stop and when to switch

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Overthinking on easy items | "2+3": 1,953% more tokens than conventional models; first round correct in over 92% of cases; QwQ on ASDIV gave 3.5 solutions on average; self-training cut tokens 48.6% on MATH500 at equal accuracy | Chen 2025 (a20, b11, c14) | E (3 sources with Hassid, DEER) |
| Underthinking on hard items | Wrong answers: 225% more tokens, 418% more thought switches; over 70% of wrong responses contain a correct thought; UT score MATH500-Hard QwQ 58.2, R1-Preview 61.5, R1-671B 65.4 | Wang 2025 (a21, b12, c11) | S (one paper) |
| Switch penalty (TIP) | AIME24 Pass@1: QwQ 38.3 to 44.1; R1-Distill-32B 61.4 to 64.1; R1 73.8 to 74.8 (prompt-only 72.4); MATH500-Hard QwQ 83.1 to 83.7; GPQA 57.6 to 59.1 | Wang 2025 (a21, c13) | S; needs logit access |
| Longer is worse within one question | Shortest chain up to 34.5% more accurate than longest; shortest chains 50-67% shorter than random and longest; AIME24 accuracy rises then falls with length | Hassid 2025 (b14, d16); Marjanovic 2025 (b13) | E |
| Short-m@k beats majority | short-1@k matches or beats majority with up to 40% fewer tokens; short-3@k beats majority at all budgets (QwQ-32B +2% at 80k, R1-670B +4% at 100k) | Hassid 2025 (d16) | S; four open models |
| Wait extension then flat or down | s1-32B AIME24 50.0 / 53.3 / 53.3 / 56.7 (none / x1 / x2 / x4); MATH500 flat; s1.1 AIME24 56.7 flat. GSM8K R1-Distill 82.2% to 87.3% then 70.3% at 15,980 tokens | Muennighoff 2025 (b16, c18); Ghosal 2025 (d15) | C |
| Parallel beats Wait at equal tokens (small models) | R1-Distill-1.5B GSM8K at 16K: Wait -11.8, parallel +10.1; parallel beats sequential by up to 22% at 16K | Ghosal 2025 (b15, d15) | C; small distilled models |
| Wait suppression is free | NoWait: chain length cut 27-51% over ten benchmarks, no accuracy loss | Wang 2025b (d22) | S; open R1-style models |
| Answer-probe early exit | DEER: 11 models, 10 benchmarks, length cut 19.1-80.1%, accuracy +0.3 to +5.0; R1-Distill-7B AIME24 41.7 to 49.2 (13,765 to 9,839 tokens), MATH-500 87.4 to 89.8 (3,858 to 2,143); ~75% of samples have an early exit point; threshold 0.95 | Yang 2025 (d13) | E (with d12, d14) |
| Fixed-interval probe | Certaindex: probe every 64 tokens; up to 50% compute saved, no accuracy drop; only ~10% of tokens saved on MATH workload; R1 uses ~3x more tokens than needed | Fu 2025 (d12) | E; stable wrong answers not caught |
| Answer convergence | Final answer reached after ~60% of steps on maths; stop on stable probed answer | Liu and Wang 2025 (d14) | S; abstract and intro only |
| Confidence-triggered abandon | DeepConf: groups of 2,048 tokens; GPT-OSS-120B AIME25 pass@1 91.8, majority@512 97.0, DeepConf@512 99.9, tokens cut up to 84.7%; online DeepConf-low saves 43-79% vs majority, a few small drops (Qwen3-32B BRUMO25 -0.9) | Fu 2025b (d11) | S; baseline is majority, not a single chain |
| Hidden-state probe | ROC-AUC over 0.7 in distribution (over 0.9 for R1-Distill-32B on AIME), ECE under 0.1; early exit at 0.85 kept 88.2% and cut ~24% tokens; at equal savings beat static exit by up to 5 points | Zhang 2025 (b10, c16) | S; white-box only |
| Confidence calibration of reasoning models | Better than non-reasoning twins in 33 of 36 settings; improves along the chain; GLM-Z1 vs GLM-4: accuracy -0.07, ECE -0.037, AUROC +0.078 | Yoon 2025 (d10) | S |
| Difficulty regimes | Easy: answer early, later exploration adds errors. Medium: wrong first, right later. Hard: fixation on early wrong answer. Hanoi: accuracy along trace falls for N=1-4, rises for N=5-7, ~0 for N>=8 | Shojaee 2025 (b18, c15, d18) | C; collapse partly artifact (Lawsen, b19) |
| NoThinking matches thinking on easy items | R1-Distill-1.5B: length cut 50.9 / 63.5 / 44.7% on GSM8K / MATH500 / AIME24 with accuracy +4.1 / +1.4 / +1.6; average length -53%, accuracy +2.4 | Zhang 2025b AdaptThink (d19) | S; learned gate (RL) |

### 3.4 Language models: structured control layers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Search with evaluation and backtracking | Game of 24, GPT-4: CoT 4%; ToT breadth 1 45%; breadth 5 74%; GPT-4 generation with GPT-3.5 evaluation 64% | Yao 2023 (c19) | S |
| Reflexion with hand-written stuck rule | Trigger: same action and response over 3 cycles, or over 30 actions. ALFWorld 130 of 134 within 12 trials; ReAct alone stalled trials 6-7, 22% hallucination; HumanEval pass@1 91.0 vs GPT-4 80.1; HotPotQA with ground-truth context: reflection +8 over episodic memory | Shinn 2023 (a22, c09, c10, d20) | E for reliable-signal tasks; not maths; no equal-token control |
| Skill-named exemplar retrieval | MATH GPT-4: plain CoT 42.2, complex CoT 50.30, topic exemplars 50.31, skill-based 53.88 (+3.6 over complex CoT); GPT-3.5 labels 51.9; GSM8K 93.00 / random exemplars 92.87 / skill 94.31 / skill+maj@5 95.38 | Didolkar 2024 (c01, c02) | S; the "+11.6%" in the abstract is 11.6 points over plain CoT, not a fair gain |
| Behaviours predict RL gain | Countdown: Qwen-2.5-3B ~60% vs Llama-3.2-3B ~30%; priming Llama with verification, backtracking, subgoals, backward chaining matched Qwen; empty or filler priming stayed 30-35%; wrong-solution priming worked about as well | Gandhi 2025 (a19, a25, b21) | S; training, one task |
| Reflection words do not track accuracy | R1-Zero reflection keywords more frequent but not positively correlated with accuracy; 231 of 240 dataset-checkpoint pairs showed situational reflection, 154 of 240 self-reflection (OLMo-2) | Liu 2025 (b22); Essential AI 2025 (b23) | E |
| Tool feedback makes self-fix work | Self-Debug gains up to 12% with unit tests, 2-3% from explanation alone; CRITIC: external feedback crucial; retry notes with the correct answer helped significantly on a 1,000-question MC exam | Chen 2024 (c23); Gou 2024 (c24); Renze and Guven 2024 (b20) | E (oracle in b20) |
| Debate does not beat voting | GSM8K GPT-3.5: 1 response 76.7; self-consistency 3 / 6 / 9 = 82.5 / 85.3 / 88.2; debate 6 / 9 = 83.2 / 83.0 (pairing from garbled table) | Huang 2024 (c05) | E (G9) |

---

## 4. Mechanisms and models

This section turns the findings into pieces an engineer can build. Everything is code-side unless stated. The model only fills slots (SCHEMA section 1).

### 4.1 Schoenfeld's control as a state machine

Represent the run as a list of **episodes**. Each episode has a type from {Read, Analyse, Explore, Plan, Implement, Verify, Transition}, a start, an end, and a **progress marker**.

Our schema states already map onto this: S1 Read/Analyse, S2 Analyse, S3 Explore/Implement, S4 Verify, S5-S6 control. The point of the mapping is that the code, not the model, owns the junctions.

**Three trigger rules, one per locus** (a02). These are our translation, not Schoenfeld's code.

| Locus | Rule in code | Notes |
|---|---|---|
| 1. Episode junction | At every state change (S3 to S4, S5 back to S3, S6 exit), run a one-line progress check: "what is the current goal, what did the last attempt establish?" | The check is cheap but is a scheduled doubt. G1 says doubt only on a signal. A state change counts as a signal only if the check is bounded (one line, no revision unless a code check fails). Test before adding. |
| 2. New information | When an attempt raises a candidate answer, a new idea, or a failing output not seen before, log it. Do not act on it unless a check fails. | The "harvest" step in S4 already does the candidate part. The "new idea" part is not coded. |
| 3. Run of failures | Count steps since the last **progress marker**. If the count reaches K, fire S6. | Needs a definition of progress. See 4.2. |

### 4.2 Progress markers (what "progress" can mean in code)

A stall rule needs a signal. Options in order of how well they are backed:

1. **A code check changes.** Number of passing tests, size of the failing set, or the failing output itself. Backed by Reflexion (d20) and Tyen (b08: a located error is fixable). Strong where a check exists.
2. **Answer stability.** Ask for the current best answer at intervals. If it has not changed over several probes, stop (Certaindex, d12; answer convergence, d14; DEER, d13). Backed on open 2025 models. Stable wrong answers are missed.
3. **Confidence.** Token-probability confidence over a sliding window (DeepConf, d11) or confidence of a trial answer (DEER, d13). Needs log-probabilities or a forced trial answer. A closed API may hide logprobs.
4. **Repeat detection.** Same action or same step repeated over 3 cycles (Reflexion, d20). Cheap. Not tested in maths chains.
5. **Switch count.** Number of thought-switch markers ("alternatively", "wait") per window (Wang, c11). Correlational: hard problems cause both switching and errors (b12).

Do not use: reflection phrases as a progress signal (K14: no link to accuracy, b22, b23); the model's own "I'm stuck" statement (SCHEMA S6 notes r = .17); the trace's account of its reasons (K12, b17).

### 4.3 Two opposite stop rules and a gate

Overthinking and underthinking need opposite fixes.

- **Stop rule (anti-overthinking).** After the first answer that passes a check, stop. Without a check: stop when a trial answer is stable across m probes. Evidence: Chen (92% first round correct), DEER, Certaindex.
- **Hold rule (anti-underthinking).** Before abandoning a line, require a stated reason and a minimum probe depth. Evidence: Wang (one source, includes its own mitigation).
- **Gate.** Estimate difficulty first. On easy items use the stop rule; on hard items use the hold rule and force a switch only after fixation (same wrong answer repeated). Evidence: difficulty regimes (Shojaee, d18), AdaptThink (d19, learned gate). A hand-written gate is untested (K27).

Pseudocode:

```
difficulty = S0.estimate(problem)        # class pass rate, or pilot short attempt agreement
loop each step:
    if check_available and check_pass: stop
    if difficulty == easy:
        if trial_answer stable for m probes: stop            # anti-overthinking
    else:
        if steps_since_progress >= K:
            if line.depth < MIN_DEPTH: continue              # anti-underthinking
            fire S6 with reason = last failing output
        if same wrong answer repeated r times: fire S6      # anti-fixation
```

All constants (m, K, MIN_DEPTH, r) are placeholders to tune on the bench.

### 4.4 Abandon with a reason, salvage on exit

Schoenfeld's second failure was abandoning with nothing salvaged (a05, a08). The mechanism: when S6 fires, the model writes one line "line X failed because Y; what it established: Z", and code stores it in the attempt history (S3 history of directions tried). The next attempt gets only the list of failed directions, not the failed text. Reflexion stores verbal lessons the same way (a22; written reflection +8 over episodic memory on HotPotQA, d20). No maths test. Treat as unproven.

### 4.5 The error-location monitor

Tyen showed that fixing is easy once the step is known (b08). So S6 should include a **step-locator**: a separate pass that reads the attempt and returns the first suspect step, with enforced output format.
- Use a reasoning-capable judge. Plain small judges return invalid output up to 55% of the time (d07).
- Do not let the judge see authorship or the proposed answer (G5).
- Do not use self-critique on long reasoning chains: R1 self-critique was 36% worse than critique of others (d05).
- Best available: a different sample or model for the judge, or a tool check. Compare cost.

### 4.6 What not to build

- A scheduled "reflect on your answer" step with no signal (K03, Huang). Already in section 4b of the schema.
- Reflection-phrase counters as progress (K14).
- Probes on hidden states (K11) unless the agent runs on open weights.
- Debate (G9).

---

## 5. What holds up

### 5.1 Holds up (multiple sources)

1. **Blind self-correction does not help.** Huang (a16), Kamoi (a15), Stechly (d08), Xu (d04), DeltaBench (d05). Prompted models change right answers to wrong ones more than the reverse. [E] but all on 2023-2024 models.
2. **External feedback is what makes revision work.** Kamoi, Stechly (sound verifier 36-38% vs 5% on Game of 24), Self-Debug, CRITIC, Reflexion code results. Even a retry note helps when the model is told the answer was wrong (b20), which is an oracle.
3. **Error location is the bottleneck.** Tyen, ProcessBench, DeltaBench, ThinkPRM agree that finding the wrong step is the hard part and is worse on long reasoning chains.
4. **Overthinking is real on easy items.** Chen, Hassid, DEER, Certaindex, AdaptThink. The first correct answer comes early and later rounds add little.
5. **Longer is not better within one question.** Hassid (34.5% gap), Marjanovic (rise then fall).
6. **Reflection phrases are not evidence of reflection.** Liu, Essential AI.
7. **Answer-stability and confidence signals shorten chains at no accuracy cost on open 2025 models.** DEER, Certaindex, DeepConf, answer convergence.

### 5.2 Failures, contested, and weak spots

- **Wait and budget forcing is contested.** s1 shows +6.7 points on AIME24 at four Waits (50.0 to 56.7) but MATH500 is flat and s1.1 shows none (b16). Ghosal calls the gain variance (d15). NoWait removes 27-51% of tokens with no loss (d22). Tsui shows appended Wait makes a non-reasoning model nearly equal to its reasoning sibling on injected errors (d02). These do not strictly conflict if Wait helps models that lack a checking habit, on errors planted by someone else, and adds little for models trained to reason. That resolution is untested. [C]
- **Underthinking has one source.** Wang's three results (UT score, 418% switches, TIP) all come from one group. The effect of TIP is 1-6 points and the prompt-only version did not help (c13). Switching is correlated with difficulty (b12).
- **"Illusion of Thinking" collapse is partly an artifact** (b19): token limits and impossible river-crossing instances (N >= 6). The three-regime shape is likely; the collapse point is not reliable.
- **Self-correction on Blocksworld went up** (40% to 55%; d08), so the drop is not universal.
- **Human training effects are thin.** Lester 1989 had no control class and a ceiling effect. Physics postreflection gains were explained by pretest (b04). The only large number is a general SRL meta-analysis (d21), abstract only.
- **Wild goose chase rate is unreplicated.** 7 of 12 is from one lab.

### 5.3 Moderators

| Moderator | Direction | Source |
|---|---|---|
| Existence of a reliable external check | Revision helps only with it | Kamoi, Stechly, Self-Debug |
| Model type (reasoning vs not) | Reasoning models have little own-error blind spot; non-reasoning ones have a large one | Tsui (d02) |
| Item difficulty | Overthinking on easy; underthinking and fixation on hard | Chen, Wang, Shojaee, AdaptThink |
| Model size | Small distilled models: Wait hurts, parallel helps. Larger: unknown | Ghosal (d15) |
| Judge quality | Self-verification pays only where verification F1 is high (Gemini 1.5 Pro trip planning verification F1 95.74); weak where it is low (Claude 3.5 Sonnet, LiveBench reasoning) | SETS (d17) |
| Who delivers a human intervention | Researchers get larger effects than teachers | Dignath (d21) |
| Setting of think-aloud | Lone student can induce the failure | Schoenfeld (a12) |

### 5.4 Interventions that worked and did not

**Worked (with conditions):**
- Tool or unit-test feedback plus revision (Self-Debug, Reflexion code).
- Search with evaluation and backtracking on puzzles with judgeable partial states (ToT 4% to 74%).
- Early exit on answer stability or confidence (open 2025 models).
- Parallel short samples plus vote (short-3@k).
- Skill-named exemplars (+3.6 over complex CoT; single source).
- Role-neutral "Wait" on non-reasoning models for injected errors.

**Did not work or unproven:**
- Prompted intrinsic self-correction (Huang).
- Debate (Huang; G9).
- Self-critique of long chains (DeltaBench).
- Reflection-phrase rewards (Liu).
- Role reframe on natural errors: only 4.3-10.8% rescued (d01).
- Human instruction for monitoring: modest at best (Lester).

---

## 6. Language models

### 6.1 How they behave

**Non-reasoning models (2023-2024).** They keep their first answer most of the time (GPT-3.5 kept 74.7% on GSM8K). When they change, they do so wrongly more often (a16). On CommonsenseQA the self-correction prompt itself pushes the model to change answers because wrong options look partly relevant (a26). They favour their own text (d03, d04). They miss errors in their own turn but fix the same errors when the user wrote them: 64.5% average blind spot over 14 open models, Sonnet 4 at 41.4% (d01).

**Reasoning models (2025).**
- They overthink easy items: 1,953% more tokens for "2+3", with 92% of first rounds already correct (a20).
- They also switch too much on hard ones: wrong answers carry 418% more switches (a21).
- They ruminate: re-examine earlier ideas with no new progress, more on harder problems (b13).
- Their accuracy along the chain depends on difficulty: early on easy, late on medium, fixated-wrong on hard (d18).
- They encode whether an intermediate answer is right but keep going (b10).
- Their verbal confidence is better calibrated than non-reasoning twins in 33 of 36 settings and improves along the chain (d10).
- They largely lose the own-error blind spot (d02).
- Their written reasoning rarely admits the real cause (hints verbalised under 20%; b17).
- Critiquing a long reasoning chain is hard even for strong critics (best F1 40.76; d05).

### 6.2 What changed behaviour, by how much

| Change | Effect | Cost or condition |
|---|---|---|
| Oracle stop signal in self-correction | GPT-3.5 GSM8K 75.9 to 84.3 | Unavailable in real use |
| Intrinsic self-correction | GPT-4 GSM8K 95.5 to 89.0 | None; it hurts |
| Sound external verifier | Game of 24 5% to 36-38% | A checker must exist |
| ToT search with evaluation | 4% to 74% on Game of 24 | Many calls |
| Gold error location + backtrack | +18 to +44 points on wrong traces | Location must be given or found |
| Appended Wait, non-reasoning model | Qwen3-14B 0.117 to 0.868 on injected errors | Injected errors only |
| Budget forcing Wait x4 | s1-32B AIME24 50.0 to 56.7 | Flat on MATH500; none on s1.1 |
| Answer-probe early exit (DEER) | R1-Distill-7B AIME24 41.7 to 49.2 and tokens 13,765 to 9,839 | Forced trial answer at each Wait; open model |
| Confidence abandon (DeepConf-low) | 43-79% fewer tokens than majority | Needs logprobs |
| Hidden-state probe exit | 24% fewer tokens, accuracy 88.2% kept | White-box |
| Switch penalty (TIP) | QwQ AIME24 38.3 to 44.1 | Needs logits |
| Short-3@k vote | +2 to +4 points over majority@k | Parallel runs |
| Skill-named exemplars | MATH 50.30 to 53.88 | Needs labelled training set |
| Verifier fine-tune (ThinkPRM) | F1 72.8 to 87.3 (14B judge vs ThinkPRM, OlympiadBench) | Fine-tune with 1K chains |
| NoThinking gate (AdaptThink) | Length -53%, accuracy +2.4 | RL-learned gate |

### 6.3 Caveats on the model evidence

Most results are on GPT-3.5, GPT-4, QwQ-Preview, R1-distills and similar. Only the Tsui paper (v3, 2026) includes current closed models (Claude Sonnet 4). No 2026 frontier test of overthinking, underthinking, or stall rules was found (critique, gap 3). Treat model-behaviour numbers as direction, not as the size of effect on our agent.

---

## 7. What our agent should take

Marks: schema part G/S/O/memory; status [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **No blind self-review.** A revision must rest on a real check output (code run, tool, independent sample, held-out test). Never "re-read and fix". Already G2 and section 4b; this adds weight. | G2 | [E] | a15, a16, b07, c04, d08, d04; K03 |
| A2 | **Gate every S5/S6 revision on an executable check where one exists.** | S5/S6, O | [E] | K05; d08, c23, c24, a22 |
| A3 | **Do not use reflection phrases ("wait", "aha", "let me recheck") as a progress or success signal.** Count outputs and checks only. | G10 | [E] | K14; b22, b23 |
| A4 | **Stop after the first verified answer on easy items.** Overthinking is robust: later rounds add little. | S6 stop rule / G11 | [E] | K08; a20, b11, d12, d13, d19 |
| A5 | **Prefer short parallel attempts to one long chain; the shortest chains are more often right.** Already G11; the new part is "do not extend a chain just because it is short of the cap". | G11 | [E] | K10; b14, b15, d16 |
| A6 | **Add an answer-stability stop.** Probe the current best answer at each wait or at fixed intervals; stop when it repeats m times. Caveat: stable wrong answers pass. Pair with A2's check. | S6 | [E] for savings, not for accuracy gain | K22; d12, d13, d14 |
| A7 | **Use a separate step-locator (not the same context) when a revision is needed and there is no tool check.** Output format enforced. The locator never sees authorship or the proposed answer. | S5/S6, G5 | [E] that location is the bottleneck; [S] for locator design | K06, K25; b08, b24, d05, d07 |
| A8 | **Do not trust the trace as a monitor** of why the model chose something. | G10 | [E] (schema) | K12; b17 |
| A9 | **Keep the stuck rule hand-written and code-evaluated.** Reflexion's rule (same action over 3 cycles or over 30 actions) shows a code trigger can work in an environment with a real signal. The numbers (3, 30) are not for maths; use as shape only. | S6 | [E] outside maths | K18; a22, c09, d20 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Stall rule on progress markers** (steps without change in a check or in the probed answer) vs no trigger, at equal tokens. | S6 | [S] (nearest: DEER, DeepConf) | K02, K23; d11, d13, d20 |
| T2 | **Fixed-interval progress check vs stall-triggered check.** Schoenfeld locus 3 vs a schedule. G1 says doubt only on signal; this tests that rule on maths. | S6, G1 | open | K22 |
| T3 | **Difficulty gate:** stop-after-first-verified on estimated easy items; force a switch after fixation on hard items. | S0/S6 | [S] | K27; d18, d19 |
| T4 | **Hold rule before abandoning** (stated reason plus a minimum probe depth). | S6 | [S] | K09; a21 |
| T5 | **Abandon-with-reason memory:** write why the line failed and what it established; list failed directions in the next attempt. | S6, memory | [S] (non-maths) | K18; a05, d20 |
| T6 | **Episode-junction progress check** (one bounded line at each state change). Risk: scheduled doubt. | S6 | [S] | K01, K02 |
| T7 | **"New idea surfaced" trigger** (Schoenfeld locus 2): log and test any new candidate raised mid-attempt. Partly covered by S4 harvest. | S4/S6 | [S] | K02; a02 |
| T8 | **Parallel samples with vote vs Wait extensions at equal tokens** on a current model. | S6, O | [C] | K13, K26; b15, d15, d16 |
| T9 | **Verbalised confidence as a stop or switch trigger, used only after the midpoint of a chain.** Schema 4b currently says not to use verbal confidence to stop; this tests whether that holds for reasoning models. | S6 | [S] | K24; d10 |
| T10 | **Skill-named retrieval** (name the skill, retrieve exemplars by skill). | O, memory | [S] | K17; c01, c02 |
| T11 | **Role reframe** (present own earlier step as another party's). Weak: only 4.3-10.8% rescued on natural errors. Lower priority. | S6 | [S] | K07, K28; d01, d03 |
| T12 | **Structure-first problem sort** before choosing an approach (human deep-structure shift). | S0/S1 | [S], human | K21; a07 |
| T13 | **Search layer with evaluation and backtracking** (ToT-like) vs CoT plus self-consistency at equal tokens, on puzzle-type items. | O | [S] | K16; c19 |
| T14 | **Seed prompts with the four behaviours** (verification, backtracking, subgoals, backward chaining). Evidence is from training, not prompting. | S3 | [S] | K15; a19, b21 |

### 7.1 Conflicts with the current schema, to resolve

- **Schema 4b says "Using a model's verbal confidence to stop: not to add."** Newer evidence (Yoon, d10) says reasoning models are better calibrated, but no one has tested it as a trigger. Keep 4b as is until T9 passes.
- **S6 notes the model's own "stuck" signal is unreliable (r = .17).** That is a finding about the model's self-report. It does not rule out a code-measured stall.
- **G1 vs T2 and T6.** Fixed-interval or junction checks look like scheduled doubt. They must be bounded (no revision unless a check fails) or be dropped.

---

## 8. Concrete tests on our bench

All arms get equal token budgets, counting setup, judge calls and probes (G7). Report accuracy, tokens, and the number of S6 firings. Use at least 2 seeds per item because AIME-size sets have 30 items and one item is 3.3 points (b16).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 stall rule | Competition maths with exact answers (MATH-hard, AIME-style) and our bench's maths items | (a) no trigger, one long chain; (b) stall rule: no change in probed answer or check for K steps, then S6; (c) DEER-style probe at each wait | Accuracy; tokens to first correct answer; S6 firings | (b) and (c) save tokens with equal accuracy (+0 to +3 points); (b) vs (c) unknown |
| T2 interval vs stall | Same | (a) probe every N tokens, act on stable answer; (b) probe only on stall | Accuracy at equal tokens; tokens spent after the last correct answer | Both stop early; stall rule triggers fewer false aborts; stable wrong answers pass in both |
| T3 difficulty gate | Mixed easy/hard maths; label by plain model pass rate | (a) ungated stop and hold rules; (b) gated by S0 difficulty estimate | Accuracy per difficulty bin; tokens | Gate saves tokens on easy items without loss; on hard items the switch-after-fixation lifts accuracy by 1-3 points |
| T4 hold before abandon | Hard items where a first correct thought is dropped | (a) free switching; (b) switch only with stated reason and probe depth >= D | Accuracy; share of wrong runs with a correct early thought (Wang's 70%) | +1 to +3 points; effect near zero on easy items |
| T5 abandon with reason | Multi-attempt maths (up to 3 S3 attempts) | (a) fresh attempts, no history; (b) attempts see the list of failed directions; (c) list plus one-line lesson | Repeated dead-end rate (same approach tried twice); final accuracy | (b) and (c) cut repeats; (c) vs (b) +0 to 2 points (Reflexion +8 was HotPotQA with context) |
| T6/T7 junction and new-idea checks | Maths with a check | (a) none; (b) bounded one-line check at each junction; (c) new-idea harvest only | Accuracy; false revisions (right answer changed to wrong) | (b) risks harm (scheduled doubt); (c) small gain |
| T8 Wait vs parallel | AIME-level | (a) 1 chain with 0/1/2/4 forced rechecks; (b) k short parallel chains + vote; (c) short-3@k | Accuracy at equal tokens | (b)/(c) >= (a) by 2-4 points; may reverse on a frontier model |
| T9 verbalised confidence | Maths with a check | (a) no confidence; (b) ask confidence at midpoint and at end, stop if above threshold; (c) abandon if below | AUROC of confidence for final correctness; accuracy at equal tokens | AUROC above 0.7 after midpoint; if below 0.6 reject |
| T10 skill retrieval | MATH-type items with a training pool | (a) topic exemplars; (b) skill-named exemplars; (c) random | Accuracy | (b) over (a) by +2 to +4 points; (c) = baseline |
| T11 role reframe | Items where the model's own natural error is known | (a) own-turn review; (b) reframed as another party's step; (c) independent second sample compared | Share of natural errors caught | (b) small (5-11%); (c) larger |
| Error locator | Wrong traces from our own runs, with gold first-error labels | (a) whole-answer review; (b) step-locator by same model; (c) step-locator by separate model; (d) tool check | Location F1; downstream fix rate; cost | (c) and (d) over (a), (b) |
| Gate on tool check | Items with executable checks | (a) revision without check; (b) revision gated on check | Rate of right-to-wrong flips | (b) removes most flips |

Design notes. (1) Measure flips (right to wrong and wrong to right) separately; Huang's finding is about flips (a16). (2) Split by difficulty always; overthinking and underthinking cancel in averages. (3) Count probe tokens as spent. (4) Include trivial items to detect the 1,953% effect.

---

## 9. What does not transfer, and why

- **Schoenfeld's human protocols.** Think-aloud on college calculus students over 20-minute sessions. Our agent has no beliefs about maths, no social setting, no fatigue. What transfers is the structure of failure (no progress check, no salvage), not the rates.
- **Teaching effects (Lester, Dignath).** Instruction changes human habits over weeks. Our agent has a fixed scaffold per run. The human training literature is weak support only.
- **Beliefs and the three questions** ("what are you doing, why, how does it help") are teaching tools. The agent version, a code-posed question at S6, is our own idea and has no direct test.
- **Hidden-state probes (b10, c16, c22) and logit penalties (TIP, DeepConf).** Need white-box or logprob access. Not usable on a closed-API agent unless logprobs are exposed.
- **Training results (s1, Gandhi, AdaptThink, self-training, ThinkPRM fine-tune).** They change weights. Our agent changes the scaffold. A behaviour that helps when trained may not help when prompted (Gandhi's priming was on pretraining/RL, not inference).
- **Reflexion numbers.** ALFWorld and HumanEval have real success signals. Maths often has none at inference time. Reflexion's QA gains partly rest on oracle labels (Huang).
- **Game of 24 and puzzle results (ToT, Stechly, Shojaee).** Partial states are easy to judge. In open proof-style maths they are not.
- **Injected-error benchmarks (Tsui, Essential AI).** Natural errors are caught far less often (4.3-10.8%).
- **Multiple-choice self-reflection gains (Renze and Guven).** Told the answer was wrong, a retry has a fair chance on multiple choice. Not an unaided test.
- **Open 2025 distilled models.** Effects (Wait harms, parallel helps) were on 1.5B-32B models. A frontier 2026 model may differ.

---

## 10. Open questions

1. Does a hand-written stall rule (repeated step or step cap plus no new progress marker) beat no trigger at equal tokens on competition maths with a current model? No paper tests it. (T1)
2. Is a fixed-interval progress check better than a stall-triggered one (Schoenfeld locus 3 vs a schedule)? (T2)
3. Do overthinking and underthinking hold for 2026 frontier models? Does a hand-written easy/hard gate work? (T3)
4. Best error monitor without ground truth: separate judge, disagreement between independent samples, or tool check? No cost per call is compared. (error-locator test)
5. Is "Wait" worth more than the same tokens in parallel samples on a current model? s1, Ghosal and Hassid disagree in setting.
6. What were Schoenfeld's original coded rates? The 1985 book and 1992 chapter were not read; 7 of 12 is unverified beyond the 1983 paper.
7. How large is the maths-specific human effect of metacognitive instruction? Dignath's maths-only d and Donker 2014 were not found.
8. Does abandon-with-reason memory cut dead ends in maths?
9. Does verbalised confidence from a current reasoning model work as a stop or switch trigger?
10. Why do reflection phrases fail to track accuracy while behaviours (Gandhi) predict RL gains? Are the behaviours present where the phrases are not?
11. What is the best progress marker for open maths?
12. Do stable wrong answers (the main hole in answer-stability stops) occur often enough in our bench to matter?

---

## 11. Sources

[V] opened this session (page or PDF text read); [M] snippet or recalled only. Where a source was opened only in part, the limit is noted.

**Human work**
- [V] Schoenfeld (1981) Episodes and executive decisions in mathematical problem solving. https://files.eric.ed.gov/fulltext/ED201505.pdf (a01-a05)
- [V] Schoenfeld (1982) Expert and novice mathematical problem solving, final project report; Schoenfeld and Herrmann (1982). https://files.eric.ed.gov/fulltext/ED218124.pdf (a06, a07)
- [V] Schoenfeld (1982) Beyond the purely cognitive. https://files.eric.ed.gov/fulltext/ED219433.pdf (a12)
- [V] Schoenfeld (1983) Theoretical and pragmatic issues in the design of mathematical problem-solving instruction. https://files.eric.ed.gov/fulltext/ED228045.pdf (a08, a09)
- [V] Schoenfeld (1985) Students' beliefs about mathematics. https://files.eric.ed.gov/fulltext/ED259950.pdf (a11)
- [M] Schoenfeld (1985) Mathematical Problem Solving (book). https://www.sciencedirect.com/book/9780126288704/mathematical-problem-solving (a10, b05); Schoenfeld (1992) Learning to think mathematically. https://doi.org/10.1016/C2013-0-11437-0
- [M] Garofalo and Lester (1985) Metacognition, cognitive monitoring, and mathematical performance. https://doi.org/10.5951/jresematheduc.16.3.0163 (a13, b26)
- [V] Lester, Garofalo and Kroll (1989) NSF final report. https://files.eric.ed.gov/fulltext/ED314255.pdf (a14, b01, b02)
- [M] Flavell (1979) Metacognition and cognitive monitoring (a23); Lester (1994) Musings (a24); no URL recorded
- [V] Rinne and Mazzocco (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4079261/ (b03)
- [V] Metacognitive postreflection exercises (2022), abstract only. https://journals.aps.org/prper/abstract/10.1103/PhysRevPhysEducRes.18.010109 (b04)
- [V] Dignath and Buettner (2008), abstract page only. https://link.springer.com/article/10.1007/s11409-008-9029-x (d21)
- [M] Donker et al. (2014) meta-analysis (b06; paywalled, not opened). https://doi.org/10.1007/s11409-008-9029-x (the link recorded in b06 is the Dignath paper)

**Language models**
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (a16, a26, b07, c03-c05)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (abstract and intro only; a15, b09, c08, d09)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516 (b08, c06, c07)
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations. https://arxiv.org/abs/2402.08115 (d08)
- [V] Xu et al. (2024) Pride and prejudice. https://arxiv.org/abs/2402.11436 (d04)
- [V] Panickssery et al. (2024) LLM evaluators recognize and favor their own generations. https://arxiv.org/abs/2404.13076 (d03)
- [V] Tsui (2026) Self-Correction Bench, v3. https://arxiv.org/abs/2507.02778 (c17, d01, d02)
- [V] Essential AI (2025) Rethinking reflection in pre-training. https://arxiv.org/abs/2504.04022 (b23)
- [V] Liu et al. (2025) Understanding R1-Zero-like training. https://arxiv.org/abs/2503.20783 (b22)
- [V] Gandhi et al. (2025) Cognitive behaviors that enable self-improving reasoners. https://arxiv.org/abs/2503.01307 (a19, a25, b21)
- [V] Chen et al. (2025) Do not think that much for 2+3=? https://arxiv.org/abs/2412.21187 (a20, b11, c14)
- [V] Wang et al. (2025) Thoughts are all over the place. https://arxiv.org/abs/2501.18585 (a21, b12, c11-c13)
- [V] Marjanovic et al. (2025) DeepSeek-R1 Thoughtology. https://arxiv.org/abs/2504.07128 (b13)
- [V] Hassid et al. (2025) Don't overthink it. https://arxiv.org/abs/2505.17813 (b14, d16)
- [V] Ghosal et al. (2025) Does thinking more always help? https://arxiv.org/abs/2506.04210 (b15, d15)
- [V] Muennighoff et al. (2025) s1: simple test-time scaling. https://arxiv.org/abs/2501.19393 (b16, c18; see critique for the AIME24 vs AIME25 row correction)
- [V] Chen et al. (2025) Reasoning models don't always say what they think. https://arxiv.org/abs/2505.05410 (b17)
- [V] Shojaee et al. (2025) The illusion of thinking (v3). https://arxiv.org/abs/2506.06941 (b18, c15, d18)
- [V] Lawsen (2025) The illusion of the illusion of thinking. https://arxiv.org/abs/2506.09250 (b19; short, preliminary)
- [V] Zhang et al. (2025) Reasoning models know when they're right. https://arxiv.org/abs/2504.05419 (b10, c16)
- [V] Ma et al. (2025) LLMs have intrinsic meta-cognition, but need a good lens. https://arxiv.org/abs/2506.08410 (c22; abstract level)
- [V] Zheng et al. (2025) ProcessBench. https://arxiv.org/abs/2412.06559 (b24, c20, d06)
- [V] He et al. (2025) DeltaBench. https://arxiv.org/abs/2502.19361 (d05)
- [V] Khalifa et al. (2025) ThinkPRM. https://arxiv.org/abs/2504.16828 (d07)
- [V] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489 (d10)
- [V] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (d11)
- [V] Fu et al. (2025) Certaindex. https://arxiv.org/abs/2412.20993 (d12)
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895 (d13)
- [V] Liu and Wang (2025) Answer convergence. https://arxiv.org/abs/2506.02536 (d14; abstract and intro only)
- [V] SETS (2025). https://arxiv.org/abs/2501.19306 (d17; maths rows garbled)
- [V] Zhang et al. (2025) AdaptThink. https://arxiv.org/abs/2505.13417 (d19)
- [V] Wang et al. (2025) Wait, we don't need to wait (NoWait). https://arxiv.org/abs/2506.08343 (d22; per-benchmark table not read)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (a22, c09, c10, d20)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c19)
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (a17, c21 opened; b27 is an abstract-level line)
- [V] Didolkar et al. (2024) Metacognitive capabilities of LLMs. https://arxiv.org/abs/2405.12205 (a18, b25, c01, c02)
- [V] Renze and Guven (2024) Self-reflection in LLM agents. https://arxiv.org/abs/2405.06682 (b20)
- [V] Chen et al. (2024) Teaching LLMs to self-debug. https://arxiv.org/abs/2304.05128 (c23)
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (c24; per-task numbers not copied)
- [V] Wang and Zhao (2024) Metacognitive prompting. https://arxiv.org/abs/2308.05342 (c25; not maths)

Notes: several evidence lines duplicate one paper (a16=b07=c03/c04; a20=b11=c14; a21=b12=c11-13; a19=a25=b21; a15=b09=c08; a14=b01). They count as one source each. The b16 s1 row in evidence_b is AIME 2025, not AIME24; the AIME24 numbers used here are from the critique correction. The "11.6%" in b25/a18 is points over plain CoT, not a gain over a fair baseline.
