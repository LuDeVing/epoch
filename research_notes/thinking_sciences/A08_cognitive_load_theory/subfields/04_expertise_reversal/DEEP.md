# Expertise reversal: deep document

*Subfield A08.04 of cognitive load theory. Written 2026-11-01 from evidence_a-d.jsonl (a01-a32, b01-b30, c01-c25, d01-d32), claims.jsonl (A08.04-K01 to K24) and critique.md. Evidence ids are cited in brackets. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The expertise reversal effect is an interaction. A kind of instructional support helps people who know little about a topic. The same support is wasted, or does harm, for people who already know a lot. The support can be a worked example, extra explanation, a diagram with text built in, a narration, a hint, a prompt, or a quiz. The sign of the support effect depends on prior knowledge. [a01, a03, a05]

The standard explanation comes from cognitive load theory. Working memory is small. A novice has no schema for the topic, so guidance does the organising and cuts the load of searching. An expert already has a schema. The guidance now repeats what the expert holds. The expert must match the guidance against their own schema. That match is extra work (extraneous load). So the same help moves from useful to redundant to harmful as knowledge grows. [a01, a05]

What the evidence says in short:

- The effect is real on average. One meta-analysis (60 studies, 176 effects, 5,924 people) gives novices d = +0.505 and experts d = -0.428. [d01]
- It is asymmetric. Help for novices is worth more than the harm to experts. Many studies show the expert effect near zero, not below zero. "Wasteful" is more common than "harmful". [d01, b06, b08]
- Heterogeneity is very high (I2 about 88 to 91%). The pooled number hides large spread. [d01]
- No registered replication exists. The base is the Sweller and Kalyuga network plus some outside studies. The meta-analysis found no publication-bias signal. [b30, d20]
- For language models, there is no clean test of the effect itself. There is related evidence that help helps weak models and can hurt strong ones, and that help an agent writes for itself hurts. [c08-c11, d22, d26, d27]

Why it matters here: our schema's S0 gate picks a mode from the class's plain pass rate. Reversal says the amount of scaffold should fall as the model's competence on that class rises. SCHEMA.md G7 already says every element must pay for itself at equal tokens. This subfield gives a human basis for G7 and a test design for it.

## 2. History and theories in depth

### 2.1 Roots: aptitude-treatment interaction

The idea that the best instruction depends on the learner is older than cognitive load theory. Cronbach and Snow (1977) summarised aptitude-treatment interaction (ATI) research from the mid-1960s. Many ATI findings did not replicate, and the field lost interest. Tobias (2009) and Schnotz (2009, same issue) argued that expertise reversal is a well-defined ATI case, with prior knowledge as the aptitude. Only titles were confirmed for these two commentaries. [a02, b13, d17]

A 2025 review frames reversal as one ATI case. Worked examples help low-working-memory learners, and high-capacity learners can move to problem solving earlier. It reports no experiment that separates ATI from prior knowledge. [d17]

### 2.2 Founding studies (1998 to 2003)

Kalyuga, Chandler and Sweller ran the first experiments in industrial training. Trainees learned electrical wiring and relay circuits. The key design: the same people were tested as novices, then again after intensive training. [b04]

- 1998: A diagram with text embedded in it helped novices. After training, the diagram alone was better. The text had become redundant. [b04]
- 2000: Narrated animated diagrams helped novices (the modality effect). After training the narration was redundant and the diagram-only group did better. [b05]
- 2001a, 2001b: Worked examples beat problem solving for novices. The advantage vanished with experience, and in one experiment problem solving won for harder circuits. [b06]
- Tuovinen and Sweller (1999) and Kalyuga and Sweller (2004, Exp 3): worked examples beat exploration for novices and lost for the more knowledgeable. [b07]

The 2003 review by Kalyuga, Ayres, Chandler and Sweller in Educational Psychologist gave the effect its name and collected these results under the cognitive load account. Only a Substack summary of it was read. [a01]

### 2.3 The 2007 review and the rapid-assessment idea

Kalyuga (2007, Educational Psychology Review) reviewed the work since the mid-1990s. It covers more than 2,200 students and a table of about 26 studies. It ties the effect to ATI and proposes learner-tailored instruction: measure knowledge, then choose the support level. The table gives effect-size differences (novice d minus expert d) from 0.45 to 2.99, mid-range 1.72. The author reads this as about 0.86 per side if symmetric. [b03]

Kalyuga and Sweller (2004, 2005) built the tailoring step. A rapid test asks the learner to give only the next step of a problem. It correlated up to .92 with a full test (Grades 9 to 10, algebra and coordinate geometry). In 2005 a rapid test plus a rated-effort measure chose the next task in an algebra tutor, and the adaptive group beat a yoked control. These are summary-level reads. [d31, b12]

### 2.4 Independent and extending studies (2004 to 2020)

- Reisslein, Atkinson, Seeling and Reisslein (2006), a different group, found the reversal with circuits (series and parallel), with about 60 per cell. Effects were small: novices +0.33, experts -0.37 for example-problem versus problem-example pairs. [b08, a16]
- Rey and Buchwald (2011) found extra explanation helped novices on retention and transfer and reversed for experts. Results favoured the cognitive-load account over a motivational (boredom) account. N = 104, gradient descent. [a14]
- Oksa, Kalyuga and Chandler (2010): explanatory notes for Shakespeare lowered load for novices and reversed for experts (three experiments). [a15]
- Nuckles et al. (2010): writing prompts helped early in a term and their value faded. Gradual adaptive fading of prompts beat permanent prompts. [a20]
- Salden, Aleven, Schwonke and Renkl (2010): in a Cognitive Tutor, adaptive fading of worked steps beat fixed fading in a lab and a classroom experiment. Fixed fading beat plain problem solving. [a17]
- Kissane et al. (2008): gradual fading beat example-problem pairs for financial-services staff. [a18]
- Renkl, Atkinson and Grosse (2004): learners learn most about the principle whose step is faded. Position of the fade did not matter. [a19]
- Others: Pawley et al. (2005); Leppink et al. (2012); Johnson-Glenberg (2010, N = 178: quizzes helped low-experience tutors more than expert tutors); Jiang et al. (2018, four experiments on listening: read-only helped the more expert, read-and-listen helped novices). [a22, a21, a23, a24]

### 2.5 The rival account: element interactivity

Chen, Kalyuga and Sweller (2017) argue that expertise reversal is a variant of the element interactivity effect. Intrinsic load depends on how many elements must be held and processed together. Expertise lowers the count, because schemas chunk elements. So what looks like "knowledge changes the sign" can be "complexity changes the sign". [a06, a05]

Supporting studies (abstracts only unless noted):

- Blayney, Kalyuga and Sweller (2016), N = 104: isolating elements helped novices. Presenting interacting elements together suited the more knowledgeable, but only for high element-interactivity material. [a07]
- Chen, Retnowati and Kalyuga (2020), Exp 1 N = 52 (Year 5), Exp 2 N = 96 (Year 8): worked-example-first beat problem-first for high interactivity, mostly for novices. At low interactivity the sequences did not differ for the more knowledgeable. [a08]
- Chen et al. (2019): novices gained from worked examples at the hardest step and not at the easiest. The more knowledgeable gained nowhere. [a09]
- Leahy and Sweller (2005): the same children as novices, then two weeks later as relative experts. Experts' effect sizes -0.37 and -0.80 (Exp 1), -0.45 and -0.79 (Exp 2); reversal depends on element interactivity. [b11]
- Lee et al. (2006): icons helped low-knowledge students and hurt high-knowledge students (novices +0.30, experts -1.39), but only with two parameters at a time. With three parameters at once, icons helped. [b10]

The 2017 paper itself stayed paywalled. The 2025 meta-analysis did not code element interactivity. It cites it as one post-hoc reading of the weak primary-school effect. [d02, d19] Status: [S].

### 2.6 Other competing explanations

- Motivation (boredom or loss of interest). Rey and Buchwald (2011) favour load over motivation, but only the abstract was read. [a14, d16]
- Assistance dilemma (Koedinger and Aleven 2007): when to give help and when to withhold it. The 2025 meta-analysis says it cannot choose between this, load theory and motivation. [c22, d21]
- Aptitude-treatment interaction and working memory. [d17]
- Dichotomising artefact. The meta-analysis authors say knowledge and assistance are continuous, and median splits are a likely cause of the heterogeneity. [d21]

### 2.7 The meta-analysis (2025)

Tetzlaff, Simonsmeier, Peters and Brod (2025, Learning and Instruction, open access) is the first formal pooling. It searched PsycINFO and ERIC only, 1992 to 2024, 35 journals. Its numbers are in section 3. Moderators tested: educational status, content area, and how prior knowledge was assessed. Element interactivity and the type of assistance were not coded. [d01, d19, d20]

### 2.8 Carry-over to AI (2023 to 2026)

Three strands. First, researchers use LLMs as simulated learners or tutors (He-Yueya 2024; Macina 2026; Hou 2026). Second, agent-skill and scaffold benchmarks measure help versus no help (SkillsBench 2026; Starace 2026; Mehtiyev 2026). Third, training-time hint schedules in reinforcement learning fade hints explicitly (Scaf-GRPO, QuestA, HATCH). Section 6 has the numbers. None of them manipulates both help and the learner's expertise at a fixed harness and equal tokens. [c25, K21]

## 3. Core findings with exact numbers

Effect sizes are Cohen's d. Positive means more support was better. Kalyuga (2007) recomputed the founding sizes himself.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pooled crossover, novices | d = +0.505, 95% CI [0.260, 0.750], 88 effects | Tetzlaff 2025 [d01] | [E] |
| Pooled crossover, experts | d = -0.428, 95% CI [-0.647, -0.209], 88 effects | Tetzlaff 2025 [d01] | [E] |
| Difference of differences | d = 0.971, CI [0.631, 1.312]; 60 studies, 176 effects, 5,924 people, n per study 17 to 357 (median 73) | Tetzlaff 2025 [d01] | [E] |
| Heterogeneity | Novices Q(87) = 475.2, I2 = 90.87%; experts Q(88) = 284.5, I2 = 87.55% | Tetzlaff 2025 [d01] | [E] |
| Publication bias | Egger z = 0.568, p = .57 (novices); z = 0.299, p = .77 (experts); funnel and trim-and-fill: none | Tetzlaff 2025 [d20] | [E], low power |
| Moderator: education level (novice side) | R2 = 25.92%. Primary -0.29 (2 studies, reference); secondary 0.70; vocational 0.63; higher education 0.99 (22 studies); mixed 1.05. Non-reference values are differences from the reference | Tetzlaff 2025 [d19] | [S] few studies per cell |
| Moderator: content area | R2 = 20.59% novice side; law, business, crafts 1.24 (reference); STEM -0.76 and humanities/language -1.08 relative to it. Not significant on expert side | Tetzlaff 2025 [d19] | [S] |
| Moderator: how groups were made (expert side) | R2 = 50.00%. Grade-level groups -0.95 (CI -1.32 to -0.58); test- or intervention-defined groups about -0.2 net | Tetzlaff 2025 [d19] | [S] |
| Older narrative review | About 26 studies, >2,200 students; difference 0.45 to 2.99, mid 1.72 (about 0.86 per side) | Kalyuga 2007 [b03] | [S] author's recomputation; larger than the meta-analysis |
| Wiring diagrams, operation test | novices d = 1.67 (N 17), experts -0.44 (N 30) | Kalyuga, Chandler, Sweller 1998 [b04] | [S] |
| Wiring, fault-finding test | novices 1.89, experts -0.88 | same [b04] | [S] |
| Narrated animation | novices 1.18 (N 30), experts -0.62 (N 38) | Kalyuga et al. 2000 [b05] | [S] |
| Worked examples, relay circuits | Exp 1 novices 0.90 (N 24), experts 0.23 (N 24), sign did not flip; Exp 2 switching equations -0.26 vs -0.75 (N 24 each) | Kalyuga et al. 2001b [b06] | [S] |
| Examples vs exploration | novices 0.69 (N 17), experts -0.33 (N 17) | Kalyuga et al. 2001a Exp 2 [b06] | [S] |
| Examples vs exploration (two studies) | novices 0.91 (N 17), experts -0.31 (N 15); novices 1.20, experts -0.36 (N 21 each) | Tuovinen and Sweller; Kalyuga and Sweller 2004 [b07] | [S] |
| Independent replication, circuits | example-problem vs problem-example: novices 0.33 (N 62), experts -0.37 (N 60); vs faded: novices 0.28 (N 63), experts -0.26 (N 61) | Reisslein et al. 2006 [b08] | [S] small effects |
| Pace of fading | slow vs fast: novices 1.30 (N 39), experts -0.47 (N 44); slow vs immediate: 0.51 (N 38), -0.42 (N 45) | Reisslein 2005 [b09] | [S] dissertation |
| Largest reported reversal | icons for gas law: novices 0.30 (N 48), experts -1.39 (N 63); difference 2.99, only at two parameters | Lee et al. 2006 [b10] | [S] |
| Imagination vs study | transfer: novices 0.55, experts -1.14 | Ginns et al. 2003 [b11] | [S] |
| Shakespeare notes | Reversal for experts in Exp 2; help for novices in Exp 1 and 3 | Oksa et al. 2010 [a15] | [S] sizes not read |
| Explanatory text, gradient descent | N = 104; novices helped, experts reversed on retention and transfer | Rey and Buchwald 2011 [a14] | [S] |
| Instructional explanations | N = 93; reversal on transfer, not retention | Rey and Fischer 2013 [a13] | [S] |
| Embedded quizzes | N = 178; helped low-experience tutors more than expert tutors | Johnson-Glenberg 2010 [a23] | [S] |
| Adaptive vs fixed instruction | knowledge gain 0.46 (2004), 0.55 and efficiency gain 0.69 (2005), 0.58 (Salden 2006 task selection); Corbalan 2006 posttest 0.25, lower load 0.37 | Kalyuga 2007 table [b12] | [E] small to medium, same network |
| Adaptive fading beats fixed fading | lab and classroom; no numerals in abstract | Salden et al. 2010 [a17] | [S] |
| Fading beats pairs | immediate and delayed tests; significant | Kissane et al. 2008 [a18] | [S] |
| Null: graduate students | N = 136, median split, 2x2 mixed ANOVA; power for eta2 = 0.06 needed 125; concept map and glossary lowered load for everyone | Gorbunova et al. 2025 [b17, b18, d15] | [E] as a null; cannot refute |
| Null: law students | worked examples beat problem solving for both novice and advanced | Nievelstein et al. 2013 [a10] | [S] abstract |
| Null: engineering seniors | N = 36, 3 groups, no differences | Darabi and Nelson 2004 [a11] | [S] |
| Null: engineering graphics | no significant interaction | Binmahfooz 2019 [a12] | [S] |
| Null: vocational | N = 63 apprentices, no group x pretest effect; scenario complexity mattered more | Gure et al. 2026 [c05] | [S] |
| Weak moderation | N = 102; moderation only on comprehension, in a three-way interaction (R2 change 4.36%, p = .031) | 2025 scaffolding study [b21] | [S] |
| Reverse pattern | strategy training helped only high-prior-knowledge learners; N = 30, interaction beta 0.42, p = .04 | Seufert 2019 [b19] | [S] |
| LLM adaptive training field trial | N = 2,574; knowledge d about 0.29; condition x tenure b = 0 | Tang et al. 2026 [b20] | [S] |

Reading the table: trust the pooled sizes. The 1998 to 2001 sizes are large because cells are small and groups are far apart (the same trainees before and after training, or different grades). Test-defined groups, which is how we would split an agent's tasks, show much weaker harm (about -0.2).

## 4. Mechanisms and models

### 4.1 The load model

Split the load a learner carries into parts:

- Intrinsic load: set by the number of interacting elements the learner must hold at once, given their schemas. High knowledge cuts it (chunking). [a05]
- Extraneous load: caused by the way the material is presented. Searching for what to do, integrating split sources, or reconciling redundant guidance all add to it.
- Capacity is fixed. If intrinsic plus extraneous load exceeds capacity, learning or performance fails.

Support S has two effects. It cuts the search cost for a learner who has no schema (benefit B). It adds a reconcile cost R for a learner who already holds the content: the learner must read S, compare it with their own plan, and discard or merge it. Net effect = B(k) - R(k), where k is knowledge. B falls as k rises. R stays or rises with k. The sign flips at a crossover k*. The meta-analysis found harm smaller than benefit, so R is usually smaller than the peak of B. [d01]

### 4.2 Implementable version for an agent

A minimal version an engineer can build:

1. Define competence c(class) as the measured plain pass rate of the model on a problem class (no scaffold), from the class record that S0 already reads.
2. Define scaffold strength s as a discrete level: 0 none, 1 short hint, 2 worked example, 3 full step guide. Count tokens per level.
3. Learn the effect curve per class: effect(s, c) = pass(s) - pass(0), measured from runs.
4. Rule: use the lowest s whose measured effect is not worse than the best within a margin, at equal total tokens.

This is a lookup, not a theory. It needs enough tasks per class to see the difference (section 4.5).

### 4.3 Fading

Fading removes parts of the support as competence grows. Human forms:

- Backward fading of worked steps: the last step is removed first, then the one before. [a19]
- Scheduled (fixed) fading: steps removed on a timetable.
- Performance-adaptive fading: steps removed when the learner shows they can do them. It beat fixed fading in Salden 2010. [a17]
- Reisslein 2006 found faded examples worse than example-problem pairs for experts. Fading is not guaranteed to be the best fix. [b08]
- Pace matters: slow transition helped novices (d = 1.30) and hurt experts (-0.47). [b09]

Training-time analogues in RL for LLMs follow the same logic. QuestA gives 50% of a reference solution for 100 steps then 25% for 1,900 steps on problems with near-zero pass rate. The faded run beat fixed 50% hints at equal steps (avg 63.26 vs 60.26). Fading further to 0% gave no gain. Training without any hint reached 60.44 but needed about twice the steps. [d05, d06] Scaf-GRPO releases hints in three tiers only after a no-hint period; hints from step 0 were 9.2% worse relative. [d03, d04] HATCH finds training with hints teaches the model to solve with hints, and anneals them. [c13, c14]

### 4.4 Adaptive triggers

Human template (Kalyuga and Sweller): test the learner's current knowledge with a short probe, then choose the level. Better still, use performance plus a load rating, and repeat the assessment. [d31, d21] The meta-analysis authors argue for repeated assessment. They note that an ordinal interaction in the observed range becomes disordinal over a wider range, and if the relation is linear the crossover point can be estimated. [d21]

For an LLM loop the candidate signals are: running class pass rate; a per-item probe (try one step without help); verifier outcomes; agreement across samples (a hint only, G4). No rule was tested on LLMs. [K22]

### 4.5 The measurement problem

A class pass rate from few tasks cannot place a threshold. Wilson 95% interval width for an observed 80%: n=5 0.59; n=10 0.45; n=20 0.34; n=50 0.22; n=100 0.16. A rule "fade when pass rate >= 0.8" fires at n=10 with probability 0.17, 0.38, 0.68, 0.93 when the true rate is 0.6, 0.7, 0.8, 0.9. At n=50 the same probabilities are 0.00, 0.08, 0.58, 0.99. [d14] So the fade trigger needs at least 20 to 50 tasks, or a Bayesian estimate with a prior, or a hysteresis rule (two consecutive batches). Real classes mix easy and hard tasks, which makes this worse.

### 4.6 Element interactivity as an alternative gate

Count the number of constraints or dependent steps that must be held jointly. CogniLoad sets this count by construction; accuracy falls with it in all 22 models tested, each with its own threshold. [d29] A task-complexity gate would use the count rather than the pass rate. No one has shown it predicts scaffold benefit in agents. [K23]

## 5. What holds up

### 5.1 Replications and meta-analysis

- Pooled effect: supported by one meta-analysis; novice benefit +0.505 and expert harm -0.428, both with CIs excluding zero. The effect is asymmetric. [d01] [E]
- Outside replication: Reisslein et al. (2006) used a different group and about 60 per cell; the reversal appeared but with small sizes. [b08]
- Rey and colleagues (2011, 2013) found reversals in text-and-computer settings. [a13, a14]
- Publication bias: none detected (Egger null), but the test has low power at this heterogeneity and only published work in two databases was searched. [d20]
- No registered or Many Labs-style replication exists. [b30, K19]

### 5.2 Failures and nulls

Gorbunova 2025 (N=136), Nievelstein 2013, Darabi and Nelson 2004 (N=36), Binmahfooz 2019, Gure 2026 (N=63), the 2025 scaffolding study (N=102) and Tang 2026 (N=2,574) all failed to show the interaction cleanly. Most are small, use median splits or narrow groups, and cannot refute the effect. Tang 2026 is large, but its "adaptive" arm was a different manipulation than a support level. [K06, K18]

Read together: the interaction is not reliable in single studies. It appears in aggregate. Plan on it as a prior, not a law.

### 5.3 Moderators

- Age and education: strongest in higher education; weak in primary school. [d19]
- Domain: weaker in language and humanities. [d19]
- How experts are defined: grade-level or profession gaps give a big reversal; one-sample test splits give about -0.2. [d19]
- Element interactivity: reversal only for high-interactivity material in several small studies. [a07, a08, b10, b11] [S]
- Retention versus transfer: reversal on transfer but not retention in Rey and Fischer. [a13]
- Strategy training can show the opposite pattern: help needs knowledge to use. [b19]

### 5.4 Interventions that worked and that did not

Worked:
- Adaptive selection from a rapid test: knowledge gains 0.46 to 0.58, load reduction 0.37. [b12] [E]
- Performance-adaptive fading over fixed fading (Salden 2010). [a17]
- Slow transition for novices (d 1.30), at the cost of experts (-0.47). [b09]
- Gradual fading of writing prompts. [a20]

Did not work, or not better:
- Faded examples vs example-problem pairs for experts (Reisslein 2006). [b08]
- Fading from 25% to 0% hints in RL (QuestA): no gain. [d06]
- Personalising hints by student features on a large platform: individual differences were too small for contextual bandits to beat a good one-for-all policy (CK-12, 166,000 sessions). [c19]
- On-demand LLM feedback helped some learners only; after propensity adjustment two of seven lessons (d = 0.28 and 0.33). [c20]

## 6. Language models

No study gives the same help to models of different ability in a randomised, fixed-harness design and reports a reversal. [c25, K21] What exists falls into six groups.

### 6.1 LLMs as simulated learners

- He-Yueya et al. (2024): GPT-3.5 as a simulated expert predicting post-test scores for 120 personas (skill levels 1 to 5) reproduced the crossover (worked examples better at low skill, practice better at high skill). Plots only, no table. A GPT-4 optimiser then wrote worksheets for a persona, with a predicted score that started at 20 for a level-1 persona and rose over about 18 steps. [a26, a27] The simulated learner is also the judge. This shows the model has learned the folk effect, not that the effect holds for models.
- SLATE (Wu 2026): slides raised learning gain for 3 of 4 student models; the smallest (Qwen2.5-VL-3B) fell about 1.4 points. Positives 4.3, 4.0, 5.0 percent (signs inferred from the text). Two decks at high baseline lost heavily (a Dutch deck 70% to 40%; Jahai pretest 72%, gain about -50). The authors suspect a format-induced response shift, not reversal. [a28, a29] [S]
- EduClaw-Bench: in 30-day simulated tutoring across 10 adapters, nothing sustained good tutoring; one Help score fell 3.19 to 2.30. [c24]

### 6.2 LLM tutors and fading

- Hou et al. (2026): 131 adults, 3 Python tasks, 393 sessions. A contingent tutor escalated support after failure and faded on take-up. Of 515 coded fading episodes only 282 followed a direct answer. Later concessions: 30.3% after full demonstration, 25.9% after pasted artifact, 20.4% after bare assertion, 33.7% after build request. [a30] Fading in LLM tutors is poorly contingent. [K14]
- Macina, Kapur and Sachan (2026): RL against a frozen Llama-3.1-8B student. 4B ablation: full recipe transfer gain +0.25, answer leak 31%; without gates +0.23 and leak 61%; without masking +0.24 and leak 13%; base Qwen3.5-4B +0.10 and leak 17%. Gain barely moved while leakage doubled. Moves: "ask for independent work" fell to 0.0%; supplying answers 15.5% to 2.2%; prompting justification 9.0% to 21.8%. A single-problem horizon trained fading out. [c01-c04] [S]
- EPFL robotics course: Socratic-guidance students started lower and gained more (interaction beta 0.72, p = .01). The paper does not discuss reversal. [a31]
- LearnLM RCT (N=165): 66.2% vs 60.7% novel problems solved, every message supervised. [c18]
- Singh et al. (2026), N=97: deferred AI help gave better hints than on-demand (beta 1.096 vs 0.75). Significant in week 1, not in week 2. [c17] [S]

### 6.3 Agents: skills and scaffolds

SkillsBench (Li et al. 2026, version 4 of 14 June 2026; always cite the version): 87 tasks, 8 domains, 3 trials, 18 model-harness setups. [c08-c11, d22-d25]

| Result | Number |
|---|---|
| No skills vs curated skills | 33.9% to 50.5% (+16.6 pp); range +4.1 to +25.7 |
| Largest lifts | OpenHands+GLM 5.1 +25.7; Gemini CLI+Gemini 3.1 Pro +24.8; OpenHands+DeepSeek V4 Pro +23.2 |
| Strong baseline, small lift | OpenHands+Gemini 3.5 Flash 41.1% baseline, +7.1 |
| Lower baseline, large lift | Gemini 3.1 Pro 36.0% baseline, +24.8 |
| Tasks that got worse | 13 of 87; largest -7.4 pp (exam-block-sequencing, suricata-custom-exfil); one trial of three is 5.6 pp |
| Self-written skills | Opus 4.7 43.0 to 34.9 (-8.1); GPT-5.5 46.8 to 35.5 (-11.3); Gemini 3.1 Pro 36.0 to 24.5 (-11.5). Curated: +18.2, +19.7, +24.8 |
| Skills per task | 1: +18.0; 2-3: +19.0; 4+: +10.1 |
| Skill length | compact +19.0; standard +21.5; detailed +14.5; comprehensive +0.7 (observational) |
| Small model with skills | MiniMax M2.7 with skills 34.9% beat GLM 5.1 without 32.7% and MiniMax M3 without 29.7% |

Why self-written help hurt (audit of 12 trajectories): packs went unused (10 of 12 never mention them); authoring displaced solving (same context); used packs locked in confident wrong content (a 1000x unit error on 3d-scan-calc); the best win was leakage (the pack was written in the graded sandbox and named the verifier's checks). The v1 protocol (same-session writing, 84 tasks, other models) gave only -1.3 pp, so the two are different measurements, not a revision. The creator step costs tokens, so these arms are not equal-token. [d22-d24] The high-baseline hypothesis (negative tasks are the easy ones) is untested; the paper explains negatives by skill design. [K08, K09]

Scaffold structure and model strength:

- Starace (2026, pre-registered, 3 scaffolds x 5 models, GAIA L1 and L2, 3 attempts): scaffold choice moved accuracy by up to 28 points within one model. Best-minus-worst gap Level 1: Opus 0.13, Gemini 0.06, GPT-5.5 0.04, Haiku 0.23. Level 2: Haiku 0.20, Sonnet 0.10, Opus 0.14, Gemini 0.17, GPT-5.5 0.06; robust slice Opus 0.28. The prediction that stronger models are less scaffold-sensitive was rejected at Level 2. Scaffolds differ in architecture, not amount of help; tokens not matched; single-author preprint. [d26]
- Mehtiyev and Assuncao (2026): 9,374 trajectories, 19 agents. Swapping the LLM moves resolution 51.5 pp (SWE-agent) and 31.5 pp (OpenHands). With the LLM fixed, the framework effect shrinks 19.4 to 3.8 to 0.9 pp across three Claude generations. Observational. [d27]
- Rodionov (2026): seven tutorial levels before the target lowered AGI Maze scores for both GPT-5.5 variants at both effort settings; helped GPT-5.6-sol at xhigh; mixed at max. A one-line "stop and report" change raised scores in 7 of 8 comparisons (-0.20 to +5.23 pp). Gains cost more tokens. [d28] [S]

The evidence points both ways. The shrinking framework effect over model generations looks like reversal across time. The GAIA result does not.

### 6.4 Chain-of-thought as "help"

- Sprague et al. (2025): CoT average gain 14.2 (symbolic), 12.3 (math), 6.9 (logic). Top three categories 56.9 vs 45.5; others 56.8 vs 56.1. Up to 95% of the MMLU gain came from questions with an equals sign. These figures come from the full text read earlier and were not re-confirmed in the abstract this session. [b22]
- Liu et al. (2025): up to 36.3 pp lower for o1-preview than GPT-4o on a task where deliberation hurts people; three of six tasks significant drops. [b23]
- Wei et al. (2022): CoT hurt models under about 100B parameters. [b24]
- Meincke et al. (2025), GPQA Diamond, 198 questions x 25 trials: step-by-step raised the average for non-reasoning models (Gemini Flash 2.0 +0.135, Sonnet 3.5 +0.117, GPT-4o-mini +0.044) but raised errors on questions they otherwise always got right (strict 25/25: Gemini Flash 2.0 -0.131, Gemini Pro 1.5 -0.172, p<.001). For reasoning models the change was small (o3-mini +0.029, o4-mini +0.031, Flash 2.5 -0.033) at 20 to 80% more time. [d07, d08]
- DeepSeek-R1 report: few-shot examples lowered performance for the reasoning model; zero-shot recommended; no ablation table. [b25, d30]
- Cheng and Mastropaolo (2026), Java pass@1, T=0: Qwen-1.5B Base 32.61 vs Robust 27.39; Qwen-32B flat 35.2 to 37.4 across prompts. Fixed 3-shot dropped Qwen-32B from 37.39 to 6.96 and Qwen-7B to 13.04; richer system prompts recovered. The 1.5B model was stable. The collapse is probably a format issue. [d09, d10]
- Tang et al. (2025): few-shot gains peak then fall; GPT models showed no significant drop, small open models fell sharply. [c16]
- Commey (2026): generic rules appended cut Qwen 2.5 7B on RAG citation from 26/30 to 9/30; 30 cases per cell. [c15]

### 6.5 Extra context and capacity

- Irrelevant context lowers accuracy (GSM-IC). [b26] The same task padded to 3,000 tokens: mean accuracy 0.92 to 0.68. [d11]
- Reasoning models rarely follow instructions about how to reason (highest score below 0.25). Instructions inside the scaffold may be ignored. [d18]
- Small models (3B and below) do not gain from long CoT distilled from strong teachers. This is a capacity limit, not reversal. [d12]
- LUFFY mixes expert traces only on failed rollouts: +6.4 average on six benchmarks; +8.0 on Qwen2.5-Math-1.5B. [d13]

### 6.6 What the LLM evidence says in total

Help helps on average (SkillsBench +16.6 pp). It does not help every task (13 of 87 negative). More is not better (4+ skills +10.1 vs +19.0). Help the model writes itself hurt (-8 to -11.5 pp). Whether a stronger model gains less from help is not settled (SkillsBench weak, GAIA no, coding agents yes). Deliberation as help hurts where the model already does it by default. Nothing here is a test of reversal, because a weak model hurt by help shows a capacity limit.

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Treat scaffold as a cost, not a free extra. Every scaffold element must show a gain over the plain model on its problem class at equal tokens. This repeats G7 and adds the reason: redundant help adds load and can lower accuracy. | G7 | [E] | K01, K11; d01, c08, c11 |
| A2 | Expect asymmetry. Where the plain pass rate is high, treat the scaffold as unneeded and use the direct mode. Expect small harm, not large. | S0 | [E] | K01, K03; d01, b06, b08 |
| A3 | Keep help short and focused. More skills or longer text lowered the lift. Compact beats exhaustive. | S0, memory | [E] | K11; c11, c15, c16 |
| A4 | Use deliberation (CoT or step-by-step) only where a calibration set shows it pays. Math and symbolic yes; elsewhere little; it can hurt strong or reasoning models. | S0 mode choice | [E] | K12; b22, b23, d07, d08 |
| A5 | Prefer adaptive over fixed help: the amount of help depends on measured performance. | S0, S9 class record | [E] | K05, K04; b12, a17 |
| A6 | Do not let the agent author its own scaffold without a verifier. Self-written help hurt in one protocol. Lessons stay one line, shown after the first attempt (matches the existing memory rule). A guard only. | memory | [S] | K10; c10, d22, d23 |
| A7 | Do not use the scaffold's reasoning text or verbal confidence as a trigger. Use outputs. | G10 | [E] | K12; d18 |
| A8 | Log per-class plain pass rate and scaffold-on pass rate, with tokens, in the class record, so the effect can be measured. | S9 | [E] (measurement practice) | K22; d14 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Fade the scaffold by running class pass rate (more direct mode as pass rate rises). | S0 fade rule | [S] | K22, K04; d31, d14, a17 |
| T2 | Show help only after a failed first attempt (withhold first). | S0, S3, S5 | [S] | K17; c17, d03, d05 |
| T3 | Gate by element interactivity (count of jointly held constraints) instead of or beside pass rate. | S0 | [S] | K07, K23; a06-a08, d29 |
| T4 | Exemplars per model and per effort setting, not once. | memory exemplars | [S] | K24, K13; d28, b25 |
| T5 | Scaffold length ablation: each guardrail on and off at equal tokens. | all G | [S] | K11; c11 |
| T6 | Adaptive vs scheduled vs fixed fading at matched tokens. | S0 | [C] | K04, K21; b08, a17, d26, d27 |
| T7 | Leakage of the answer into the scaffold; measure it. | S8 | [S] | K15; c02 |
| T8 | Test whether the scaffold effect changes sign with capability gap (small vs frontier model), not within one model. | S0 | [C] | K20, K21; d19, d26, d27 |

## 8. Concrete tests on our bench

All arms get the same total token budget, including help text, class-record lookup and any creator step. Report accuracy and accuracy per 1,000 tokens. Use 3 or more seeds. Use a continuous baseline, not a median split.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Our ARC and BrainTeaser items, split into terciles by the model's plain pass rate | plain; full schema; schema with only the cheapest elements | scaffold effect (pass(s) minus pass(0)) per tercile with 95% CI | Positive in the bottom tercile; near zero or slightly negative in the top. Meta-analysis scale is about +0.5 d low and -0.4 d high; for pass rate expect a few points |
| B2 | Same items | fixed scaffold vs scheduled fade vs fade triggered by running class pass rate (two consecutive batches of 20 or more) | accuracy, tokens | Triggered fade at least ties fixed and saves tokens; Salden 2010 suggests adaptive beats fixed |
| B3 | Items with a check | help-first vs attempt-first (help after a failed attempt) | accuracy, tokens to success | Attempt-first matches or beats help-first on high-baseline items; no loss on low |
| B4 | Same items on a small and a frontier model | schema strength at 3 levels (none, short, full) | lift by model; interaction test | Lift larger for the small model; no lift or loss at full strength for the frontier model would be the capability-gap reversal |
| B5 | Items tagged by jointly-held constraint count | scaffold on vs off | fit scaffold benefit on constraint count vs on baseline pass rate; compare AIC | If constraint count fits better, use it as the gate |
| B6 | Items with exemplars | zero-shot vs 1-shot vs 3-shot of our own solved problems, per model | accuracy, format errors | Strong reasoning model: zero-shot at least as good; weak model: few-shot helps |
| B7 | Items | fixed hand-written hint vs hint the agent writes itself (verifier-checked) vs none | accuracy including creator tokens | Self-written below fixed, as in SkillsBench |
| B8 | Items with a check | scaffold with and without a rule that forbids naming the answer | answer-leak rate, accuracy | Leak falls with no loss in accuracy (Macina: gain 0.25 vs 0.23 while leak 31% vs 61%) |

Power: with n=50 items per cell a 10 point difference at 50% pass rate is borderline. Plan for 100 or more items per tercile, or use paired comparisons on the same items. [d14]

## 9. What does not transfer, and why

- The mechanism. The load model assumes a limited human working memory and a schema-match cost. An LLM has no working-memory limit of that kind. Its failures with long or redundant context are distraction and format shift. [b26, d11, d10]
- The label "expert". Human experts are made by years of training. A model's competence is a fixed property per class, not a state that grows during a session. Fading inside one run needs another meaning (fade across tasks, using the class record). Macina found RL on single problems trained fading out. [c03]
- Median-split groups. Our competence measure is continuous and can be exact per class. The weak -0.2 expert effect for test-defined groups suggests a within-model split may show little. [d19]
- Large founding effect sizes. These came from different grades or the same trainees before and after training, small N, one network. Do not plan around d = 0.9 per side. [b03, K02]
- Fading as a certain fix. It lost to example-problem pairs for experts (Reisslein 2006) and to adaptive selection (Salden 2010). [b08, a17]
- Human motivation or boredom explanations. Not applicable to models.
- Training-time results (QuestA, Scaf-GRPO, HATCH, LUFFY). Hints there shape the weights. We do not train. They show that withholding or fading help is useful for learning, not for inference. [d03-d06, c13, d13]
- LLM-simulated learners. They show what a model believes about learners, not what happens. [a26, c04]
- Skill-library results as a test of reversal. A weak model that fails with help may be showing a capacity limit. [d12, K21]

## 10. Open questions

1. Does the scaffold effect in LLM agents cross zero as the model's plain pass rate rises, with the harness fixed and tokens matched? (K21)
2. Is element interactivity a better predictor than baseline pass rate? (K07, K23)
3. What fade trigger works in an LLM loop, and how many tasks does it need? (K22, d14)
4. Which SkillsBench tasks got worse, and are they the high-baseline ones? Per-task data exist only in heat maps. (K08)
5. Why do self-written scaffolds hurt: unused packs, displaced solving, or locked-in errors? Which of our guardrails are the "self-written" kind? (K10)
6. Is there a same-configuration comparison of the early (-1.3 pp) and later (-8 to -11.5 pp) SkillsBench self-written protocols? None exists. (d24)
7. Is there a registered replication of the founding studies? None found. (K19)
8. Does R1-style "few-shot hurts" hold across model strengths with numbers? (b25, d30)
9. How should "equal tokens" be defined when fading shortens prompts or a creator step is needed? Our proposal (not from a source): total tokens per item including help text and creator steps, reported as accuracy per token as well as accuracy.
10. Does the reversal appear on transfer but not on retention, as in Rey and Fischer? Is there an LLM analogue (same-task versus new-task generalisation)?
11. Does help in a prompt behave like help during training (hint fading in RL)?

## 11. Sources

[V] = opened and read this session or in the evidence pass. [M] = snippet, abstract or second-hand only.

**Human studies and reviews**

- [V] Tetzlaff, Simonsmeier, Peters, Brod (2025), Learning and Instruction 102142, open copy: https://www.pedocs.de/volltexte/2026/34113/pdf/Learn_and_Instr_2025_Tetzlaff_u.a._A_cornerstone_of_adaptivity.pdf (record https://doi.org/10.1016/j.learninstruc.2025.102142; blog summary https://www.learningandthebrain.com/blog/one-size-doesnt-fit-all-teaching-experts-and-novices/)
- [V] Kalyuga (2007), Educational Psychology Review, copy: https://www.uky.edu/~gmswan3/EDC608/Kalyuga2007_Article_ExpertiseReversalEffectAndItsI.pdf (DOI http://dx.doi.org/10.1007/s10648-007-9054-3)
- [V] Kalyuga, Ayres, Chandler, Sweller (2003), via summary: https://csed.substack.com/p/the-expertise-reversal-effect-2003
- [V] Wikipedia, Expertise reversal effect: https://en.wikipedia.org/wiki/Expertise_reversal_effect
- [V] Leppink and van den Heuvel (2015): https://pmc.ncbi.nlm.nih.gov/articles/PMC4456454/
- [V] Gorbunova, Kapuza, Chen, Costley (2025), Frontiers in Psychology: https://pmc.ncbi.nlm.nih.gov/articles/PMC12367772/
- [V] Seufert (2019): https://pmc.ncbi.nlm.nih.gov/articles/PMC6374309/
- [V] Salden, Aleven, Schwonke, Renkl (2010), abstract page: https://researchportal.hw.ac.uk/en/publications/the-expertise-reversal
- [V] Tang et al. (2026) utility employees trial: https://pmc.ncbi.nlm.nih.gov/articles/PMC13626984/
- [V] Scaffolding study, system vs self regulation (2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12135206/
- [V] Working memory and ATI review (2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12189472/
- [V] Ophthalmic anatomy AI exercise (2026): https://pmc.ncbi.nlm.nih.gov/articles/PMC13416949/
- [V] GenAI in higher education meta-analysis (2026): https://pmc.ncbi.nlm.nih.gov/articles/PMC13219050/
- [V] Europe PMC search note: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22expertise%20reversal%22
- [M] Chen, Kalyuga, Sweller (2017): https://doi.org/10.1007/s10648-016-9359-1
- [M] Blayney, Kalyuga, Sweller (2016): http://dx.doi.org/10.1080/01443410.2015.1051949
- [M] Chen, Retnowati, Kalyuga (2020): http://dx.doi.org/10.1111/bjep.12317
- [M] Chen, Retnowati, Kalyuga (2019): http://dx.doi.org/10.1080/01443410.2018.1515891
- [M] Nievelstein et al. (2013): http://dx.doi.org/10.1016/j.cedpsych.2012.12.004 (also https://repub.eur.nl/pub/38893)
- [M] Darabi and Nelson (2004): https://eric.ed.gov/?id=ED485099
- [M] Binmahfooz (2019): https://eric.ed.gov/?id=ED637968
- [M] Rey and Fischer (2013): http://dx.doi.org/10.1007/s11251-012-9237-2
- [M] Rey and Buchwald (2011): http://dx.doi.org/10.1037/a0022243
- [M] Oksa, Kalyuga, Chandler (2010): http://dx.doi.org/10.1007/s11251-009-9109-6
- [M] Reisslein et al. (2006): http://dx.doi.org/10.1016/j.learninstruc.2006.02.008 (sizes via the Kalyuga 2007 table)
- [M] Kissane et al. (2008): http://www.informaworld.com/openurl?genre=article&id=doi:10.1080/01443
- [M] Renkl, Atkinson, Grosse (2004): http://dx.doi.org/10.1023/B:TRUC.0000021815.74806.f6
- [M] Nuckles et al. (2010): http://dx.doi.org/10.1007/s11251-009-9106-9
- [M] Leppink et al. (2012): http://dx.doi.org/10.1007/s10734-011-9476-1
- [M] Pawley et al. (2005): https://eric.ed.gov/?id=EJ691099
- [M] Johnson-Glenberg (2010): http://www.informaworld.com/openurl?genre=article&id=doi:10.1080/09523
- [M] Jiang, Kalyuga, Sweller (2018): http://dx.doi.org/10.1007/s10648-017-9427-1
- [M] Tobias (2009) and Schnotz (2009): https://doi.org/10.1007/s11251-009-9103-z
- [M] Kalyuga and Sweller (2004, 2005) rapid assessment: https://doi.org/10.1007/bf02504800
- [M] Koedinger and Aleven (2007): https://doi.org/10.1007/s10648-007-9049-0
- [M] Kalyuga, Chandler, Sweller (1998, 2000, 2001); Tuovinen and Sweller (1999); Lee et al. (2006); Leahy and Sweller (2005); Reisslein (2005); Ginns et al. (2003): numbers via the Kalyuga (2007) table only

**LLM and AI studies**

- [V] He-Yueya, Goodman, Brunskill (2024): https://arxiv.org/pdf/2403.02795
- [V] Wu et al. (2026) SLATE: https://arxiv.org/pdf/2609.06212
- [V] Hou et al. (2026) adaptive scaffolding needs contingency: https://arxiv.org/pdf/2609.22993
- [V] EPFL Socratic vs prompt refinement: https://www.alphaxiv.org/abs/2607.03303.md
- [V] Macina, Kapur, Sachan (2026) The Assistance Dilemma: https://arxiv.org/pdf/2610.06446
- [V] Gure et al. (2026): https://arxiv.org/pdf/2604.09158
- [V] Nazaretsky (2026), proposal only: https://arxiv.org/pdf/2605.04996
- [V] Li et al. (2026) SkillsBench v1 and v4: https://arxiv.org/pdf/2602.12670 (v4: https://arxiv.org/pdf/2602.12670v4)
- [V] HATCH hint annealing: https://arxiv.org/pdf/2609.34975
- [V] Commey (2026): https://arxiv.org/pdf/2601.22025
- [V] Tang et al. (2025) Few-shot dilemma: https://arxiv.org/pdf/2509.13196
- [V] Singh et al. (2026) deferred AI hint writing: https://arxiv.org/pdf/2604.19931
- [V] LearnLM Team and Eedi (2025): https://arxiv.org/pdf/2512.23633
- [V] Schmucker et al. (2025): https://arxiv.org/pdf/2508.00270
- [V] Thomas et al. (2025): https://arxiv.org/pdf/2506.17006
- [V] Lee et al. (2026) EduClaw-Bench: https://arxiv.org/pdf/2608.03206
- [V] Sprague et al. (2025) To CoT or not to CoT: https://arxiv.org/pdf/2409.12183
- [V] Liu et al. (2025) Mind your step: https://arxiv.org/pdf/2410.21333
- [V] Wei et al. (2022): https://arxiv.org/pdf/2201.11903
- [V] DeepSeek-AI (2025) R1: https://arxiv.org/pdf/2501.12948
- [V] Shi et al. (2023): https://arxiv.org/pdf/2302.00093
- [V] Scaf-GRPO: https://arxiv.org/abs/2510.19807
- [V] QuestA: https://arxiv.org/abs/2507.13266
- [V] Meincke et al. (2025) Prompting Science Report 2: https://arxiv.org/abs/2506.07142
- [V] Cheng and Mastropaolo (2026): https://arxiv.org/abs/2602.15228
- [V] Levy et al. (2024): https://arxiv.org/abs/2402.14848
- [V] Li et al. (2025) Small models struggle: https://arxiv.org/abs/2502.12143
- [V] LUFFY: https://arxiv.org/abs/2504.14945
- [V] Kwon et al. (2025) ReasonIF: https://arxiv.org/abs/2510.15211
- [V] Starace (2026) GAIA scaffold effects: https://arxiv.org/abs/2606.08529
- [V] Mehtiyev and Assuncao (2026): https://arxiv.org/abs/2604.02547
- [V] Rodionov (2026): https://arxiv.org/abs/2610.22289
- [V] Kaiser et al. (2025) CogniLoad: https://arxiv.org/abs/2509.18458
- [V] Our own Wilson-interval computation (local script under D:/research_scratch/A08.04), not a literature source
- [M] Prather et al. (2024) The Widening Gap: https://arxiv.org/pdf/2405.17739
- [M] Dinucu-Jianu et al. (2025): https://arxiv.org/abs/2505.15607
- [M] LLM formative-feedback prompts (2023): https://arxiv.org/pdf/2311.13984
- [M] R1 few-shot ablation search: https://arxiv.org/abs/2501.12948
