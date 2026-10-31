# Expertise reversal and fading: deep document

*Subfield A05.02. Built from evidence_a-d.jsonl (a01-a30, b01-b27, c01-c29, d01-d30), claims.jsonl (K01-K37) and critique.md in this folder. Evidence ids in brackets. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. "Human-only" means no test on a language-model agent exists.*

**The one-paragraph answer.** In people, help that benefits low-knowledge learners (worked examples, integrated text, narration) loses value or turns harmful as the learner's knowledge in that task class grows. A 2025 meta-analysis puts it at d = +0.505 for assistance in low-knowledge groups and d = -0.428 for withholding assistance in high-knowledge groups, with very high heterogeneity. The effect is graded, often partial, and asymmetric: helping novices is worth more than removing help from experts. In language-model agents, no published study tests this inside one task class with a competence split at equal tokens. What exists is indirect: lesson libraries help on average but hurt on a minority of tasks, model-written lessons hurt, short lessons beat long ones, many examples can lower accuracy, and the benefit of a harness is hump-shaped in model strength. So the idea "show lessons only on weak classes" is plausible, cheap, and untested for our agent. Treat it as a hypothesis for S0 and test it.

---

## 1. What it is

**Definition.** The expertise reversal effect (Kalyuga and colleagues) is an interaction. An instructional method that helps learners with little knowledge of a task class loses its advantage, or becomes worse than a plain alternative, for learners who know the class well. [a01, b01]

**Narrow meaning of "expertise".** Skill on one task class, measured by a domain test. It is not general ability and not years of experience. [a01, d02] The meta-analysis only counted studies with a domain-specific prior-knowledge measure; general intelligence did not qualify. [d02]

**Typical manipulations.**
- Worked example versus problem solving.
- Text integrated into a diagram versus diagram only.
- Narration added to an animation versus none.
- Added icons, definitions or explanatory text.
- Fully worked steps versus steps gradually removed (fading).
- Study an example versus imagine the procedure.

**Fading** is the companion technique. Start with a fully worked example. Remove solution steps one by one (usually from the end, "backward fading") until the learner solves the whole problem. It is the practical way to move a learner along the guidance axis as knowledge grows. [a15, a27]

**Why this matters for our agent.** S0 (the gate) must decide per problem class whether to show a lesson. The human literature gives a direction (lessons for weak classes, none for strong classes), a size (moderate, asymmetric), a shape (graded, three bands), and a warning (the decision must be re-measured as the record changes). It gives no formula for the crossover point and no test on an LLM agent.

**What the agent equivalent is.** A "lesson" is a stored line or short example from past attempts. The "learner's knowledge" is the model's own pass rate on that problem class. The "extraneous load" analogue is extra context the model must reconcile with what it already does well. This mapping is our own; no source tests it. [K29]

---

## 2. History and theories in depth

### 2.1 Roots (1960s to 1990s)
- **Aptitude-treatment interaction (Cronbach 1967).** The older idea that the best method depends on the learner's prior ability. Expertise reversal is a specific, theory-driven case of it. [b19]
- **Cognitive load theory (Sweller).** Working memory is small. Novices carry every element in working memory. Experts fold elements into schemas stored in long-term memory. Worked examples cut novices' load, which gave the worked-example effect. [a02]
- **Redundancy principle.** Information that repeats what the learner already knows adds load and gives no gain.

### 2.2 The founding studies (1998 to 2001)
- **Kalyuga, Chandler and Sweller (1998).** Electrical trainees studied wiring diagrams with embedded text versus diagrams only. Embedded text won for novices. After intensive training, diagram-only won. Same trainees, tested as skill grew. [a03]
- **Kalyuga, Chandler and Sweller (2000).** Narrated animation versus diagram only with mechanical-engineering trainees. Narration helped novices; after several sessions diagram-only won. [a04]
- **Kalyuga, Chandler, Tuovinen and Sweller (2001).** Worked examples versus problem solving for relay-circuit programming and switching equations. The edge vanished or reversed with training. Experiment 2 on switching equations shows no clear novice gain, only a late reversal. [a05, b03]
- **Tuovinen and Sweller (1999).** Database learning. Worked examples beat exploration for novices; no difference for higher-knowledge students. [a08]
- **Yeung, Jin and Sweller (1998).** Fifth graders did better with in-text definitions; university students did better with a separate glossary. Age and expertise are confounded. [a12]

All of these founding numbers come from one table in one review. The primary papers were never opened (paywalled, no open copy). [d29]

### 2.3 Naming and consolidation (2003 to 2010)
- **Kalyuga, Ayres, Chandler and Sweller (2003)** coined the name. [not opened; cited via the 2007 review]
- **Kalyuga (2007) review.** About 40 studies, more than 2,200 students. Conservative effect-size differences (novice effect minus expert effect) from 0.45 to 2.99, mid-range 1.72. Mostly cross-sectional groups formed by a pretest median split. SDs chosen conservatively where missing. No publication-bias check. The author is the main proponent. [b01, a01]
- **Theory in the review.** Knowledge in long-term memory plays an executive role. Novices need outside guidance as a substitute. Experts already have the knowledge, so outside guidance must be reconciled with it, which adds extraneous load. Mid-level learners get complementary value from both sources, so guidance should cover only the unfamiliar parts. [a02, b19]
- **Rey and Buchwald (2011).** Replicated the reversal for the redundancy principle (N = 104; novice or expert-trained by a short session, extra text or none). Cognitive load differences, not motivation, explained it. Abstract only. [a24]
- **Kalyuga (2010) special issue.** Five papers; one partial field replication (Salden et al., Cognitive Tutor, section 5). [b09]

### 2.4 Learner-adapted instruction (2004 to 2010)
- Kalyuga and Sweller built a rapid-assessment system that places a learner on a guidance level, then reassigns as knowledge grows. [a14, b06, b07]
- Salden, Paas and van Merrienboer (2006) and Salden, Aleven, Schwonke and Renkl (2009, 2010) tested adaptive fading in tutoring systems. [a13, b10, c28]
- Reisslein et al. (2006) and Reisslein (2005) tested fading pace by prior knowledge. [a09, a10, b05]

### 2.5 Rival and refining theories (2013 to 2017)
- **Element interactivity (Chen, Kalyuga and Sweller 2017).** Expertise reversal is a variant of the element interactivity effect. Expertise folds interacting elements into one schema, so the number of interacting elements in an item falls and guidance becomes redundant. Prediction: guidance value depends on item complexity for that learner, not on topic labels. Chen's PhD thesis tests this in geometry and trigonometry. [a20, a21, a22; paper itself not opened]
- **Ill-structured domains (Nievelstein 2013; Rourke and Sweller 2009; Kyun et al. 2013).** No reversal in law, art history, literature. The authors' account: in less structured tasks the schema takes longer to build, so "advanced" students are still novices at the schema level. [a17, a18, a19]
- **Generation versus guidance.** Self-explanation and generation can overload novices and help experts (Leppink 2011). [a23, b19]

### 2.6 The meta-analysis (2025)
Tetzlaff, Simonsmeier, Peters and Brod (2025, Learning and Instruction). The first formal meta-analysis. Details in section 3. Authors' own advice: assess knowledge repeatedly as it grows, and fade gradually. They say the meta-analysis cannot choose between theories and does not test fading directly. [d01, d04]

### 2.7 The AI turn (2024 to 2026)
- LLMs used to simulate students (He-Yueya 2024). [a28]
- LLM tutors with fading or escalation (Hou 2026; Sankaranarayanan 2026). [c24, c25]
- Agent "skill" libraries tested at scale (SkillsBench and follow-ups). [c18 to c22, d05 to d24]
Section 6 covers these.

### 2.8 Competing explanations still open
1. **Redundancy / extraneous load** (Kalyuga). The standard account.
2. **Element interactivity** (Chen). Same data, finer unit. Predicts item-level effects.
3. **Aptitude-treatment interaction** (Cronbach). Statistical description, no mechanism.
4. **Regression to the mean and dichotomisation.** Median-split groups are prone to regression; the meta-analysis authors name dichotomising two continuous variables as a likely cause of the huge heterogeneity. [a07, d04]
5. **Motivation.** Rejected in one study (Rey and Buchwald). [a24]
No study in the review separates these accounts. [b19, d04]

---

## 3. Core findings with exact numbers

Effect sizes are Cohen's d unless stated. "Novice" and "expert" are the study's own groups. Status: [E] established, [S] single source, [C] contested.

### 3.1 Human founding studies (second-hand through Kalyuga 2007 Table 1 unless noted)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Embedded text in wiring diagram: helps novices, hurts after training | Operation/troubleshooting: novices d = 1.67 (N=17), experts -0.44 (N=30), diff 2.11. Fault finding: 1.89 vs -0.88, diff 2.77 | Kalyuga, Chandler, Sweller 1998 [a03, b02] | [S] one review table |
| Narrated animation helps novices, hurts after training | Novices d = 1.18 (N=30), experts -0.62 (N=38), diff 1.80 | Kalyuga et al. 2000 [a04] | [S] |
| Worked examples, relay programs (Exp 1) | Novices 0.90 (N=24), experts 0.23 (N=24), diff 0.67 | Kalyuga et al. 2001 [a05, b03] | [S] |
| Worked examples, switching equations (Exp 2): no novice gain, late reversal | Novices -0.26, experts -0.75 (N=24 each), diff 0.49 | Kalyuga et al. 2001 [a05, b03] | [S] |
| Worked examples vs exploratory learning (full disordinal interaction) | Novices 0.69 (N=17), experts -0.33 (N=17), diff 1.02 | Kalyuga et al. 2001a Exp 2 [a06] | [S] |
| Coordinate geometry, median split on rapid pretest | Novices 1.20 (N=21), experts -0.36 (N=21), diff 1.56. Original: 42 Year 9 students, 8 practice problems | Kalyuga and Sweller 2004 Exp 3 [a07, a28] | [S] |
| Database: examples help novices, no difference for experts | Novices 0.91 (N=17), experts -0.31 (N=15), diff 1.22 | Tuovinen and Sweller 1999 [a08] | [S]; expert side not reliable |
| Example-problem vs problem-example pairs (circuit analysis) | Novices 0.33 (N=62), experts -0.37 (N=60). Example-problem vs faded: 0.28 (N=63) vs -0.26 (N=61) | Reisslein et al. 2006 [a09] | [S]; small effects |
| Pace of fading: slow suits novices, fast suits experts | Slow vs fast: novices 1.30 (N=39), experts -0.47 (N=44), diff 1.77. Fast = one step removed per example; slow = one per two examples | Reisslein 2005 (dissertation) [a10, b05] | [S] |
| Icons in gas-law simulation: helped novices, hurt experts with two parameters; helped all with three | Novices 0.30 (N=48), experts -1.39 (N=63). Listed difference 2.99 does not match 0.30 + 1.39 = 1.69 | Lee, Plass, Homer 2006 [a11, b04] | [S]; table arithmetic unverified (critique) |
| Integrated vs glossary definitions | Expert d -0.53 to -0.79; differences 0.66 to 1.87 | Yeung et al. 1998 [a12, b04] | [S]; age and expertise confounded |
| Imagine vs study: same children flip within two weeks | Study better at first; imagination better two weeks later (Exp 2 stronger). Means not given | Leahy and Sweller 2005 via review [b08] | [S] |
| Adapting guidance to measured skill beats non-adapted | 0.46 (K&S 2004), 0.55 knowledge and 0.69 efficiency (K&S 2005), 0.58 (Salden 2006), 0.25 posttest and 0.37 load (Corbalan 2006) | Review [a13, b06] | [E] for "adapting helps"; rule matters little |
| Rapid first-step or verification test predicts full test | r up to .92; .71 and .75; test time cut 3.2x, 3.5x, 3.7x, up to 4.9x | Kalyuga 2006, 2007 [a14, b07] | [S]; well-defined tasks only |

### 3.2 Human replications and extensions

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Statistics, self-explanation: crossover | Interaction F(3,97) = 2.762, p < .05, eta2 = .079. Low prior: examples best, questions plus arguments worst, d = 0.96. High prior: arguments best, questions only worst, d = 1.06. Examples vs arguments d = 0.51, ns. About 130 recruited, 105 analysed | Leppink et al. 2011 [a23] | [S]; only just significant |
| Redundancy principle, short-training experts | N = 104; novices with extra text higher on retention and transfer, experts reverse | Rey and Buchwald 2011 [a24] | [S]; abstract only |
| Geometry, Grade 4 / 6 / 7 | Grade 4: examples beat problem solving on high-interactivity items; generating beat being shown on low-interactivity (d = .96 Exp 1, .57 Exp 2). Grade 7 (revision): worked-example effect reversed. | Chen 2016 thesis Exp 1-3 [a20] | [S] |
| Trigonometry with delay | Exp 4: no interaction immediately; significant interaction after a week. Exp 5 (more knowledgeable): more guidance hurt on both item types, immediate and delayed | Chen 2016 thesis Exp 4-5 [a21] | [S] |
| Cognitive Tutor field and lab | Adaptive fading beat fixed fading and plain problem solving on immediate and one-week delayed tests in the lab; in the classroom only on the delayed test | Salden et al. 2009, 2010 [b09, b10, c28] | [S]; numbers not read |
| Law: no reversal | Year 1 (N about 75) 58.63 vs 8.59, F(1,68) = 105.2, f = 1.24. Year 3 (N=36) 82.28 vs 37.06, F(1,32) = 37.03, f = 1.02. Prior knowledge Year 3 vs Year 1: 17.12 vs 8.86, d = 2.75. Time: about 570 s vs 1146 s | Nievelstein et al. 2013 [a17] | [E] with art history, literature |
| Art history and literature: no reversal or graded | Art history: examples beat problem solving in years 1 and 2. Literature: none for most expert, retention only for middle, retention plus marginal transfer for least | Rourke and Sweller 2009; Kyun et al. 2013 via thesis [a18, a19] | [S] each; numbers not captured |
| Fading, field study (low-track students) | Near transfer F(1,32) = 4.44, p < .05; far transfer F(1,32) = 2.28, ns | Renkl, Atkinson, Maier 2000 [a15] | [C] |
| Fading, lab (N=54, 27 per group) | Near transfer F(1,51) = 4.58; far transfer F < 1; errors in learning F(1,51) = 7.62 | Renkl et al. 2000 [a15] | [C] |
| Fading plus "name the principle" prompts | Medium to large effects on near and far transfer; no added time | Atkinson, Renkl, Merrill 2003 [a16] | [S]; abstract only |
| Fading did not beat example-problem pairs | N=143 (37 / 35 / 35 / 36). Translation: condition F(3,138) = 2.93, p = .036; fading vs none F(1,138) = 2.34, p = .129. Prior knowledge strongest predictor (partial eta2 .126 to .150) | Grosse 2015 [a26] | [C] against Renkl 2000 |

### 3.3 The meta-analysis (Tetzlaff et al. 2025, full text read)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pooled effect, low-knowledge groups (high assistance better) | d = 0.505, CI [0.260, 0.750], k = 88, 60 studies, I2 = 90.87% | [d01] | [E] direction; [S] as a single meta-analysis |
| Pooled effect, high-knowledge groups (low assistance better) | d = -0.428, CI [-0.647, -0.209], k = 88, I2 = 87.55% | [d01] | same |
| Difference of differences | d = 0.971, CI [0.631, 1.312]; lower than the 1.72 in the 2007 review | [d01] | same |
| Size of base | 176 effects, N = 5,924, 35 journals, 1992-2024, sample sizes 17 to 357 (median 73) | [d01] | |
| Publication bias | Egger low-PK p = .57, high-PK p = .77. Only PsycINFO and ERIC searched; 3 of 23 authors supplied data | [d02] | Low power; no unpublished work |
| Educational status moderates | Low side R2 = 25.92%, high side 8.47%. Low-PK d: primary about -0.29 (j=2), secondary 0.70, vocational 0.63, higher education 0.99 [0.34, 1.63] (j=18) | [d03] | Few studies per cell |
| Content area moderates low side only | R2 = 20.59%. Crafts/law/business (coded "other") 1.24; humanities and language weaker | [d03] | |
| How knowledge was assessed moderates high side | R2 = 50.00%. Grade-level groups -0.95 [-1.32, -0.58] (j=8). Measured (median-split) groups about -0.21 (j=32, k=48) and intervention groups about -0.20 (j=7) (offsets added by the critique, not printed) | [d03, d27] | [S]; derived |
| Heterogeneity | I2 about 88 to 91% on both sides: the mean is a poor guide to any one setting | [d01] | |

**Reading of section 3.** Direction is solid. Size is moderate and asymmetric. The expert-side effect shrinks to about -0.2 when experts are defined by a measured test, which is how our agent's class pass rate would define them. Plan the main gain from gating as saved tokens, not saved accuracy. [K02, K37]

---

## 4. Mechanisms and models

This section is written so an engineer can build each piece.

### 4.1 The cognitive-load account (verbal model)
- State per learner and task class: `K` = stored knowledge (schema coverage).
- Guidance `G` supplies the steps the learner cannot supply. Benefit rises with the number of steps the learner is missing.
- Cost of guidance: the learner must cross-check `G` against own knowledge. Cost rises with `K`.
- Net effect = benefit(missing steps) minus cost(cross-checking). At low `K`, benefit wins. At high `K`, cost wins. In between the two are complementary: show guidance for the unfamiliar parts only. [a02, b19]
- The model gives no crossover formula. [a02]

### 4.2 Graded, three-band rule (what the data support)
- Least knowledge: guidance helps retention and transfer.
- Middle: guidance helps retention only, or nothing.
- Most: no gain, or a cost.
[a19, a20, a21, K04]

Implementation for the agent: three bands by class pass rate, not one threshold. Suggested starting cut points (our own, to be tuned by test): weak < 40%, middle 40 to 80%, strong > 80% plain pass rate. The numbers are placeholders, not from any source.

### 4.3 Element interactivity (item-level model)
- Define `E(item)` = number of elements that must be held and combined at once to solve the item.
- Expertise reduces `E` for the learner by merging elements into schemas: `E_eff = E / chunking(K)`.
- Guidance helps when `E_eff` is high. It is redundant when `E_eff` is low.
- Prediction: within one class, high-step items still benefit from a lesson even if the class is strong; low-step items do not. [a20, a21, a22]
- Agent version: annotate items with the number of interacting steps (for example the length of the shortest verified solution trace, or count of distinct constraints). Test whether step count adds predictive power over class pass rate (K09, U7). Nobody has measured this on LLMs. [d22 notes that difficulty strata are benchmark labels, not step counts]

### 4.4 Rapid diagnosis of knowledge level (Kalyuga)
The system in the review: [a14, b07]
1. Give a few cheap probes. Either "first step" (show a problem, ask only for the next step) or "step verification" (show a solution step, ask if it is right).
2. Score. Map the score to a guidance level.
3. After each task, take a load rating. Efficiency indicator = performance divided by rated load.
4. Move to less guidance when the probe is passed and the load rating is low. Move back if performance drops.
Validity: r up to .92 with full tests; time cut 3.2x to 4.9x. Well-defined tasks only. Correlations are with the authors' own process measures, not with later learning gains. [b07]

Agent mapping: "first step" probe = run the model on the first move of 3 items; "load rating" has no clean analogue, use tokens spent or number of revisions as proxy (our idea, untested).

### 4.5 Probe size and class estimate (our calculation, not literature)
- Wilson 95% interval for an observed 50%: n=4 about [0.15, 0.85]; n=10 [0.24, 0.76]; n=20 [0.30, 0.70]; n=30 [0.33, 0.67]. [d25]
- Chance of observing a pass rate of at least 0.8 when the true rate is 0.7: 0.34 (n=3), 0.53 (n=5), 0.38 (n=10), 0.24 (n=20). [d25]
- So 3 to 5 items cannot place a class in a band. About 20 items give plus or minus 0.2. Use a smoothed estimate and a wide middle band. Repeating the same item adds less information than new items. [d25, K35]
- One agent study (SkillApt) reached a plateau at about six paired with/without states per skill and failed with 1 to 4. [d10]

### 4.6 Paired with/without evidence (SkillApt model)
- For each lesson and each class, collect pairs: same state run once with the lesson and once without.
- Load the lesson only if its estimated benefit exceeds a threshold. At threshold 0.5: 91.3% success at 26.3% activation; at 0.6: 86.3% at 10.0% activation and 974.8 tokens. [d10]
- A zero-shot LLM controller reached the same 91.3% but activated 98.8% of the time and used 1,811.7 tokens, so the gain is cost, not accuracy. [d10]
- Credit using success-only history makes the policy load nearly everywhere (a skill credited for 204 of its 227 successes). Use paired data. [d10]
- Cost: paired runs double the compute.

### 4.7 Fading as an operator
Backward fading ladder for a worked lesson with steps `s1..sn`:
- Level 0: all steps shown.
- Level k: last k steps removed; the model must produce them.
- Level n: bare problem.
Pace rule from Reisslein: slow ladder (one step per two examples) for the weak band, fast or immediate for the strong band. [a10, b05]
Add-on: for each shown step ask the learner to name the principle used. This raised near and far transfer in humans at no extra time. [a16]
Adaptive version: move down the ladder after the probe is passed, up after a fail. Adaptive fading beat fixed fading on delayed tests. [b09, b10]
Agent analogue: shorten or drop the stored lesson as the class pass rate rises, and prune lessons after a model upgrade. The nearest working model is Cortex: after upgrading the model, a prune pass ran each item's tasks 3 times with and 3 times without the item; 2 of 4 items were flagged removable. [d14]

### 4.8 Gate for lesson admission and scope (agent models)
- Pre-commit gating (VaG): a new lesson enters the pool only after a with/without check. Ungated pools peak at round 3 and fall; gated pool reached 72% pass@1, 10 points above the ungated best, with a pool about 5 times smaller. [d12]
- Scoping: lessons tested on one family hurt other families when applied everywhere. Global memory 0.713 vs no-edit 0.775; same skills scoped to their family 0.816; 0 of 63 accepted scoped updates harmful. [d13]
- Applicability boundary and fast path: harmful skills are mostly relevant ones that make the agent build or verify too much (see section 6). [d08]

---

## 5. What holds up

### 5.1 Replications and agreements
- **Direction of the interaction.** Founding studies (1998-2001), later independent work (Leppink 2011 statistics, Rey and Buchwald 2011, Chen 2016 geometry and trigonometry, Reisslein circuit analysis), and the 2025 meta-analysis all agree: assistance helps low-knowledge learners (d = 0.505) and withholding it helps high-knowledge learners (d = -0.428). [K01, K02]
- **Adaptation helps.** Effect sizes 0.25 to 0.69 for learner-adapted sequences, and the exact rule matters little. [K11]
- **Delayed tests reveal more.** Trigonometry (no interaction immediately, interaction after a week) and Cognitive Tutor classroom (adaptive fading won only on delayed test). [K10]
- **Short training can create the effect.** A brief earlier session flipped the sign for added text (Rey and Buchwald); the same primary-school children flipped within two weeks (Leahy and Sweller). [K13]

### 5.2 Failures, nulls and partial results
- **Ill-structured domains show no reversal.** Law (Year 3 still did far better with examples: 82.28 vs 37.06), art history, literature. Explanation is the authors' own; no direct test. [K08]
- **Most reversals are partial.** The interaction is significant but the expert side is not, or the novice benefit just vanishes. Clean sign flips are the minority. [K03, b19, b20]
- **Meta-analysis shrinks the size.** Difference of differences 0.971 (CI 0.631 to 1.312), not 1.72. Measured groups about -0.2 on the expert side. [d01, d27]
- **Weak where?** Primary school (low-PK d about -0.29, j=2), humanities, language learning. [d03, d04]
- **Fading is contested.** Renkl 2000: near transfer yes, far transfer null in both studies. Atkinson 2003: adding principle prompts gives medium to large effects (abstract only). Grosse 2015 (N=143): fading no better than example-problem pairs, p = .129; example-first order the only reliable contrast. [K06, K07]
- **Immediate tests can miss it.** Chen 2016 Exp 4. A one-session agent test would also miss it. [a21]
- **Small and noisy.** Many cells have N = 15 to 30. Leppink's main interaction is just significant (p < .05). Largest effect sizes come from the smallest samples. [b04, a23]
- **LLM-simulated students are not human data.** [K25]

### 5.3 Moderators that matter
| Moderator | Direction | Source |
|---|---|---|
| How knowledge was defined | grade level -0.95; measured about -0.21; intervention about -0.20 | [d03, d27] |
| Educational status | higher education 0.99 vs primary -0.29 (low side) | [d03] |
| Domain | well-defined (math, electrical) strong; humanities, law weak | [d03, a17-a19] |
| Task load | When load is very high for everyone, support helps all (icons with three parameters) | [a11] |
| Item complexity | Guidance helps high-interactivity items, even later | [a20, a21] |
| Test timing | Delayed tests show effects immediate tests miss | [a21, b09] |

### 5.4 Interventions that worked
- Worked examples for low-knowledge learners. [a05, a06, a07, a17]
- Slow fading for novices, fast fading or immediate problem solving for experts (Reisslein; small effects). [a10]
- Fading plus principle prompts (abstract-level). [a16]
- Adaptive fading on delayed tests. [b09, b10]
- Rapid probe-based placement. [a14]

### 5.5 Interventions that did not work, or did not show an advantage
- Fading alone for far transfer (Renkl 2000: F < 1 in the lab). [a15]
- Fading over example-problem pairs in a large eighth-grade sample. [a26]
- Fixed fading over plain tutored problem solving (Salden, abstract). [b10]
- LLM-generated faded examples versus standard feedback for 27 teaching assistants: no significant cognitive-load gain (search summary only). [c29, K27]
- Prior knowledge did not predict who benefited from LLM access in a randomised self-study (treatment x pre-exam p = 0.2); skill at using the AI did (three-way p < .05). [c26]

---

## 6. Language models

**Headline.** There is no direct test. No published study splits tasks by a model's own per-class competence and randomises a lesson on or off at equal tokens. Searches in this series found none. [K29, d30] The following is indirect evidence, grouped by what it tells us.

### 6.1 Lessons help on average, but not everywhere
- **SkillsBench (Li et al. 2026, re-opened).** 87 tasks, 8 domains, 18 model-harness configurations. Curated skills raised pass rate from 33.9% to 50.5% (+16.6 pp, normalised gain 25.5%). Per-configuration gain +4.1 to +25.7 pp. 13 of 87 tasks got worse, worst -7.4 pp. [c18, c21, K15]
- **Gain is unrelated to the no-skill pass rate across configurations.** Pearson r = -0.03, Spearman -0.09 (N = 18; our computation from Table 2). The strongest systems were not the biggest gainers (Opus 4.8 45.7 to 54.1, +8.4) but a strong Codex start still gained +19.7. So there is no clean model-level reversal here. [d17, c22, K19 contested]
- **Domain level.** Math and operations research gained only +9.7 pp (among the lowest), where pretraining is strong; top ten tasks gained +67.0 pp on average (for example 1.9% to 94.4%). A domain-level analogue of reversal, confounded by task difficulty. [c20]
- **Hump in model strength (Lin et al. 2026).** SWE-bench Verified base pass and best harness gain over three evolvers: Qwen3-32B 3.6%, +4.4; Qwen3-235B 20.7%, +19.3; GPT-OSS-120B 26.2%, +15.8; Haiku 4.5 66.0%, +2.4; Sonnet 4.6 73.2%, +2.8; Opus 4.6 74.2%, +2.6. Weaker pattern on MCP-Atlas; tiny cells on SkillsBench. The gain is the maximum over three evolvers (biased upward) and the harness is a bundle. [d18, d19, K31]
- **Why the weakest gain little.** They often do not load the lesson or follow it. SkillsBench load rate / following rate: Qwen3-32B 0.251 / 0.142; GPT-OSS-120B 0.446 / 0.442; Haiku 4.5 0.794 / 0.600; Sonnet 4.6 0.959 / 0.730; Opus 4.6 0.957 / 0.757. Weak-model adherence drifts 0.52 to 0.13 over a trajectory. [d20]
- **Same harness, two models (Cortex).** +66.7 points under Haiku 4.5, +5.6 (CI -2.8 to +13.9) under Sonnet 5. Tiny task counts, one repository. A skill listed on every turn was listed in 198 attempts and opened in none. [d14]
- **Agent-written lessons help mainly at low baselines.** 11 models, 3 benchmarks, 33 cells: Spearman rho = -0.55 (text skills) and -0.45 (code skills) between baseline and effect, both p < 0.05. GPT-OSS-120B on AppWorld fell from 27.3 to 17.0 (text) and 1.0 (code); 69% of those code runs ended within two steps. Subtask-level skills averaged 24.8 none, 26.7 text, 25.3 code; task-level 22.1 none, 20.9 text, 18.0 code. [d09, d22, K30]
- **Mismatched memory hurts unsolved items.** ALFWorld A to B: raw trajectory memory gave retention +4.6 on baseline-success items and new learning -26.1 on baseline-fail items. The memory came from a different task, so this tests relevance mismatch, not redundancy. [d11]

### 6.2 Which lessons hurt
- **Model-written lessons.** Self-generated skills fell 8.1, 11.3 and 11.5 pp below no skills on three configurations (for example Claude Code + Opus 4.7: 43.0 none / 34.9 self / 61.2 curated). Causes from a 12-trajectory audit: the solver never opened them (10 of 12), authoring used up the trial, a confident wrong constant ran unquestioned, and the one win was leakage. [c19, d05]
- **Unfiltered induced skills.** Averaged over 11 models and 3 benchmarks: task-level none 22.1, text 20.9, code 18.0. [d09]
- **Writer strength matters little when evidence-based.** Updates written from execution traces differ by at most 3.1 pp across evolvers; a Qwen3.5-9B evolver matched Claude Opus 4.6. [d21]
- **Skill-induced failure types.** 307 failures (differential method): 86 of 125 functional failures (68.8%) were implementation faults, only 2 (1.6%) applicability mismatches; of 182 efficiency regressions, 114 (62.6%) were excessive procedure (67 excessive verification, 30 heavy pipelines), 46 (25.3%) context bloat, 43 of those from mandatory skill text. Harm is mostly from relevant lessons that make the agent do too much. [d08, K33]
- **The agent's own choice to fetch.** 17 LLMs, paired runs: aggregate lift often positive while the same-task effect is negative (Math500 Llama-3.3-70B +14.2 aggregate vs -39.4 paired; MBPP+ DeepSeek-V3.2 +31.6 vs -9.1). Random skills also cost (-10.2 / -5.0) and corrupted skills (-15.1 / -15.4), so part of the cost is the tool call or extra context. Single seeds with sign flips. [d07]
- **Ungated pool decay.** Peak at round 3, then falls; removing source skills recovers only 1.7 pp. [d12]
- **Global versus scoped memory.** 0.713 global vs 0.816 scoped. [d13]
- **Coalition effects.** Bank-level gains hide negative skills; skills that help at the source can reverse at the target. Abstract-level. [d16]

### 6.3 Compact beats exhaustive
- Compact +19.0, standard +21.5, detailed +14.5, comprehensive +0.7 pp. [c21]
- 1 skill +18.0 (23 tasks), 2-3 skills +19.0 (43 tasks), 4+ skills +10.1 (21 tasks); baselines about equal (32.2 to 34.8), so not simply harder tasks. Length is confounded with content; no length-matched control. [d06, K17]
- Gemini 1.5 Pro (Honda et al.): MATH500 8-shot 86.3, 400-shot 82.3, cheat sheet 88.0; GSM8K 94.5 / 95.1 / 94.5; GPQA 57.1 / 56.7 / 60.4 (3 runs; GSM8K and GPQA within noise). Many-shot prompts used about 45,000 to 70,000 tokens. With GPT-4.1 no gain from few to many shot. [c07, c08, b17]
- Agarwal et al.: MATH500 gain up to about 125 examples then decline; GPQA best at 125 shots, worse at 250. [b12]
- Tang et al.: LLaMA-3.2-3B worsened beyond about 80 examples; GPT-4o and GPT-3.5 did not drop significantly. TF-IDF plus stratified selection avoided over-prompting. [b13, b22]
- Zou et al.: harder tasks degrade at shorter contexts (Llama-3.1-70B lost accuracy on level 4-5 symbolic tasks before level 1). [c09, c10]
- Liu et al. 2025: few-shot demonstrations can reduce math accuracy; depends on similarity and the stability of the model's inference on the demonstration. [b18]

### 6.4 Shifted demonstrations and model size
- Qiu et al. 2026 (SST-2, 100 runs): Llama-2-7B 96.4 zero-shot, 100.0 at 0% perturbed, 95.0 at 50%, 80.3 at 75%, 56.9 at 100%. Llama-3.1-8B 98.2 to 66.0. Gemma-4 2B 100.0 to 83.2. [c05]
- Large models robust: Llama-2-13B 97.3; Llama-3.1-70B 100.0; Qwen2.5-72B 99.6; Qwen3.5-27B 99.4. Exception: Llama-2-70B 87.6 (SD 11.8). Math splits: Llama-3.1-8B -6.6 (Medium), 70B -1.4; Hard: Qwen2.5-14B -9.3, 72B -4.9. [c06, b14]
- The perturbation is an input-style change that keeps the answer correct, not a knowledge-redundant example. The perturbed exemplars were still 0.919 cosine-similar to the originals, so a similarity filter would not catch them. Small models over-weight recent exemplars (tail placement 92.3 / 77.6 / 58.1 vs random 94.7 / 88.2 / 72.9). [d15, b23]
- Wei et al. 2023: large models override priors using in-context labels; small models mostly follow priors. This and Qiu are consistent: bigger models follow examples better and are less misled by noise. [c11]
- Reasoning models need fewer shots: DeepSeek-R1 reached 99.31% on IMDB with 5 shots where GPT-4o needed 40 for the same score; shot counts chosen on test curves. [b16, b24]
- Hannan et al. 2026 (vulnerability detection): mistake-targeted or nearest-neighbour examples lifted Gemma-3-4b from F1 0.574 to 0.854 on NodeMedic; GPT-5-mini was already at 0.860 with random few-shot. Failed on PrimeVul and SVENC. Mistake-targeted examples pushed models to predict one class. [b15, b27]

### 6.5 Strong models read lessons selectively
- OpenSkillEval (600+ tasks, 30 skills, 10 models): skill file read in about 48% of cases by default, Claude Opus 4.6 about 20%. Forced reading raised use to 94%, first read from step 4.4 to 3.3; steps still skipped or contradicted. Read rate is not accuracy. [d24]
- With generic retrieved skills only, weaker models fell to or below no skill (Kimi 19.8 vs 21.8; Qwen 19.7 vs 20.5); Claude gained 3.0 over no skill. Gaps are inside noise. [d23]
- Claim from DeepSeek-R1 report: few-shot consistently degrades it, zero-shot advised. Statement only, no table. [c12, K22 contested]

### 6.6 Thinking amount (machine analogue of fading support)
- Meincke et al. (GPQA Diamond, 198 questions, 25 trials, N=4950): CoT average rating change Gemini Flash 2.0 +0.135, Sonnet 3.5 +0.117, GPT-4o-mini +0.044 (p = .067). On the "always correct" metric: Gemini Flash 2.0 -0.131, Gemini Pro 1.5 -0.172 (made worse on questions they always got right). Time cost 35 to 600% for non-reasoning, 20 to 80% for reasoning models. Reasoning models: marginal gains at best. [c13, c14] (critique: the "+0.101 for Sonnet 3.5" figure was not found in the text.)
- Sprague et al.: 110 papers, 1,218 comparisons. CoT gain +14.2 symbolic, +12.3 math, +6.9 logical; top three categories 56.9 vs 45.5; others 56.8 vs 56.1. Compute not matched. [c15, K23]
- AdaptThink (1.5B, lambda 0.05): GSM8K 83.1 vs 79.0, MATH500 82.0 vs 80.6, AIME24 31.0 vs 29.4, average +2.4 points, length -53.0%. NoThinking chosen on 86.9% of GSM8K, 76.8% MATH500, 40.4% AIME24. Forced NoThinking alone was worse (GSM8K 69.8, MATH500 67.2, AIME24 14.0). Needs RL training. [c16, c17, K24]

### 6.7 LLMs as simulated learners and tutors
- He-Yueya et al. 2024: GPT-3.5 as a simulated expert predicted post-test scores for 120 personas. Reproduced the Kalyuga and Sweller pattern: examples helped low-skill personas, no difference for high-skill. Also reproduced the variability effect. A null, not a true reversal; the model may have seen the original papers; direct simulation failed because the model could not hold a stable knowledge level. [a28, c01, c02, c03]
- Song et al. 2026: prompting an LLM to act as a novice does not keep it novice; unlearning did better. Direction only. [c04]
- Unrestricted AI help: 77% failed a 30-minute no-AI maintenance task vs 39% for scaffolded; a teach-back gate cut epistemic debt by 41.7 points at 14.2 minutes cost (N=78, Claude 3.5 Sonnet). The paper names expertise reversal as the reason to fade friction but does not test fading. [c23, c24]
- Contingent tutor that escalates after failure and fades after take-up (131 adults, 3 Python tasks, 3 tutors): full answer surrendered in 1 session in 16 vs 1 in 6 for the question-only tutor. [c25]
- Socratic tutors drift to the answer under pressure: Qwen3-8B collapse rate 36.0% (full method) vs 47.0% SFT only, 63.5% online-updated reference; judge changes the rate (Claude-Haiku-4.5 judge 84.5%, human 35.2%). [c27]
- Xu and Wu 2026: a worked example inside a medium-guidance skill. GPT-5.5: no skill 31.3%, medium no example 61.3%, with example 62.0%. DeepSeek V4-Flash: 26.0%, 44.0%, 45.3%. Example effect +0.7 pp [-5.3, +6.0] and +1.3 pp [-6.0, +9.3]; Holm p 1.0 and 0.87; 150 trials per cell; detectable 8.3 to 16.0 pp. Tasks not split by competence. [a29, d28, K18]

### 6.8 What changed behaviour, ranked by size
1. Lesson on versus off, curated: +16.6 pp average (+4.1 to +25.7 across configurations). [c18]
2. Model-written versus none: -8.1 to -11.5 pp. [c19]
3. Compact versus comprehensive: +19.0 vs +0.7 pp. [c21]
4. Scoped versus global memory: 0.816 vs 0.713. [d13]
5. Gated versus ungated pool: +10 points at 72%. [d12]
6. Same harness, weak vs strong model: +66.7 vs +5.6 points (single repository). [d14]
7. Worked example inside a skill: +0.7 to +1.3 pp, not detectable. [a29]

### 6.9 What we cannot say from the LLM data
- None of the studies tests lesson value inside one class split by competence. [K29]
- Lin et al. and Feng et al. show correlations across models and benchmarks (baseline confounded with model and benchmark). [d09, d18]
- Thinking on/off was not isolated from model size. [critique gap 3]
- Preprint status: Xu and Wu, Qiu, Li, Hou, Song, Sankaranarayanan, Anand and Idan and others are arXiv preprints. The critique re-opened five and found them accurate. [critique 4]

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = section 5 of SCHEMA.md. Statuses: [E] established, [S] single-source, [C] contested. For human-only items, [E] refers to the human literature.

### 7.1 Add now (established)

| # | Take-away | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep only lessons verified by a paired with/without check (or written from real failing output). Do not let the model write lessons from imagination. | memory | [E] | K16, K34; c19, d05, d09, d12, d21 |
| A2 | Scope every lesson to its problem class. Never apply a lesson learned on one class to others. | memory | [E] | K34; d13, d16, d11 |
| A3 | Keep lessons compact: one line or a short paragraph, 1 to 3 shown per problem, never 4 or more. | memory | [E] | K17; c21, d06, b17, c07 |
| A4 | Gate new lessons into the pool: a lesson must win a paired with/without check before it enters; cap the pool size. | memory | [E] | K34; d12, d13 |
| A5 | Re-measure the class record as it changes. Do not freeze a "lessons on" list. | S0, memory | [S] for the exact timing, [E] that value flips with skill in humans | K05, K10, K13, K11; a03, a04, a06, b08 |
| A6 | Class record is per model. A threshold tuned on one model size is not valid for another. | S0, memory | [E] | K21; c05, c06, b14, d18 |
| A7 | In open or ill-defined classes, do not drop lessons only because the plain pass rate is high. | S0 | [E] (human) | K08; a17-a19 |
| A8 | Lessons carry an applicability boundary and a fast path ("if the check already passes, stop"). | memory | [E] | K33; d08, c21 |
| A9 | Extra reasoning (G11) and lessons are gated by task type, not applied uniformly. Consistent with G11 and G12. | G11, G12 | [E] | K23, K20; c15, c13 |
| A10 | Offer lessons after the first attempt (already in memory section 5). The data on over-help support not giving the answer before the attempt. | memory | [E] (consistent) | K26 (single-source, human); d11, d14 |

### 7.2 Test first (not yet in the schema)

| # | Candidate | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Show lessons only on weak classes (three bands by plain pass rate; drop, do not invert). | S0 | [S]: human [E], agent untested | K01-K04, K29, K30; d09, d17 contradicts at model level |
| T2 | Code gate (probe pass rate, threshold) beats always-on lessons at equal tokens. | S0 | [S] | K11, K15, K33; a13, b06, d10 |
| T3 | Probe size: how many items per class give a stable band (3, 5, 10, 20). | S0 | [S] calculation only | K35, K12; d25, d10 |
| T4 | A floor as well as a ceiling: below a minimum, a lesson is not followed, so use a different mode (worked example near the point of use, or a stronger model). | S0 | [S] | K31; d18, d19, d20, d14 |
| T5 | Fading for mid-band classes: full lesson vs shortened (last step removed) plus "name the rule" vs none. | S0, O, memory | [C] | K06, K07; a15, a16, a26, d14 |
| T6 | Lesson value predicted by item complexity (interacting steps) beyond class pass rate. | S0 | [S] | K09; a20-a22, d22 |
| T7 | Delayed or held-out scoring: score lessons on fresh items in a later session. | memory | [E] human; untested on agents | K10; a21, b09, b10 |
| T8 | Strong classes: lessons as an optional lookup, weak classes: forced. | S0 | [E] behaviour, [S] benefit | K32; d23, d24 |
| T9 | Number of lessons per class: 0, 1, 3, 10 and look for a hump. | memory | [E] hump in demonstrations, [S] for lessons per band | K20, K17; b12, b13, c07 |
| T10 | Lessons derived from verified failing outputs beat model-written lessons at equal tokens. | memory | [E] that model-written hurt, [S] on the exact contrast | K16; d05, d21 |
| T11 | Does the lesson effect flip after in-run exposure (a few solved items of the class in context)? | S0, memory | [E] human | K13; a24, b08 |
| T12 | Very hard band keeps lessons regardless of class pass rate. | S0 | [S] | K14; a11 |
| T13 | A code-run difficulty router (thinking budget by difficulty) beats uniform budget at equal tokens. | G12, S0 | [S] machine analogue | K24; c16 |
| T14 | Thinking mode on or off after controlling pass rate. | G11, S0 | [C] | K22; c12-c14 |

Expected size, for planning: human meta-analysis suggests about +0.5 on the weak side and about -0.4 on the strong side (about -0.2 for measured groups), with very wide spread. For the agent, plan the main gain from gating as tokens saved. [K02, K37]

---

## 8. Concrete tests on our bench

All arms run at equal total tokens (lesson tokens count against the budget; setup and probe cost count, G7). Items from our existing suites; classes defined by task type. Paired design: the same items with and without the lesson, three or more seeds.

**Test 1: Band x lesson on/off (T1, U1).**
- Item type: 20 or more problem classes, 30 or more items each, from our current benches (word puzzles, ARC-style, brain-teasers).
- Arms: (a) plain, (b) plain + one-line lesson shown after the first attempt. Bands set from plain pass rate on a separate probe set.
- Metric: pass-rate difference per band with 95% intervals; share of classes where the lesson hurts; tokens per item.
- Expected: weak band +5 pp or more; strong band about 0 and some negatives (Li et al.: 13 of 87 tasks worse). A 5 pp effect needs about 560 to 1570 unpaired trials per arm; paired designs with seeds are mandatory. [d26]

**Test 2: Gate versus always-on versus none (T2, U2).**
- Arms: none, always-on, code gate (band by probe).
- Metric: pass rate and total tokens.
- Expected: gate within 1 pp of always-on at 15% or more fewer tokens, above none on weak classes. Several gate rules should tie (K11).

**Test 3: Probe size (T3, U5).**
- Item type: 12 or more classes with 40 or more items each as ground truth.
- Subsample 3, 5, 10 and 20 probe items; compare the assigned band to the full-class band.
- Metric: band agreement rate, Spearman correlation, token cost.
- Expected: 3 to 5 items unstable (calculated); about 20 stable.

**Test 4: Floor check (T4, U3).**
- Same lesson on a small and a large model of ours. Log lesson read rate and following rate (judged by code where possible).
- Metric: gain by plain pass rate; read and follow rate.
- Expected: hump-shaped (Lin et al.: +4.4, +19.3, +15.8, then about +2.5).

**Test 5: Fading ladder on the middle band (T5, U4).**
- Arms: full lesson, last step removed plus "name the rule", bare problem, plus an example-first-only control.
- Item sets: near (same template) and far (new template).
- Metric: pass rate near and far, tokens.
- Expected: human results split. Do not expect a win; include the example-first control (Grosse).

**Test 6: Item complexity (T6, U7).**
- Annotate each item with the number of interacting steps (shortest verified trace length).
- Fit lesson gain on class pass rate alone, then add steps. Metric: change in explained variance or AUC for predicting which items benefit.
- Expected: step count adds power inside strong classes.

**Test 7: Lesson count and length (T9, U10).**
- Arms at equal total tokens: 0 lessons, 1 one-line, 3 one-line, 1 paragraph, 10 lines.
- Metric: pass rate by band. Expected: hump; one to three best; 10 equal or worse.

**Test 8: Verified versus model-written lessons (T10, U11).**
- Arms: no lesson, model-written lesson before attempt, lesson from a verified failing output, both at equal tokens.
- Metric: pass rate per step type; share of items made worse. Expected: model-written negative or zero; verified positive on weak classes.

**Test 9: Delayed held-out scoring (T7, U8).**
- Score the same lesson on in-session items and on fresh items in a new session with no shared context.
- Metric: delta in-session vs fresh. Expected: delayed effect differs in sign or size from immediate.

**Test 10: Optional versus forced lookup (T8, U9).**
- Strong classes: lesson forced in prompt vs lesson available as a tool call. Metric: accuracy and tokens. Expected: equal accuracy, fewer tokens for optional.

**Test 11: Prune after upgrade (T5, T2).**
- After a model upgrade run 3 with and 3 without per lesson (Cortex style). Metric: share of lessons removable at no loss; tokens saved. Expected: about half removable.

---

## 9. What does not transfer, and why

1. **Cognitive load in working memory.** The mechanism is a human working-memory limit. An LLM has no equivalent of "extraneous load"; it has a context window and attention dilution. Harm from extra examples in LLMs often arises from length, position, shifted style or conflict, not redundancy. [b13, b14, c09, d15]
2. **"Expert" as long practice.** In humans experts got their schemas over years. In the studies "experts" are often created by a short session. A model's pass rate is not a schema measure; two classes with the same pass rate may differ in reliability. [a24]
3. **Learning from the lesson.** Humans keep what they study (retention, delayed transfer). A stateless agent keeps nothing between runs, so the retention half of the human literature (delayed tests, fading as a learning path) has no direct counterpart. [K10]
4. **Generation and self-explanation effects.** These need a learner who benefits from effort. In a model, "generate it yourself" is just fewer tokens of guidance; no learning follows. Relevant only as sampling, not learning.
5. **Motivation and frustration.** AI tutor results (over-help, frustration, epistemic debt) concern human learners using AI. They are a design caution only. [c23, c25, c26, K26]
6. **Simulated learners.** LLMs cannot hold a stable novice level, and have likely seen the original studies. Do not tune the gate with simulated learners. [c03, c04, K25]
7. **Perturbation studies.** Qiu et al. test shifted but correct demonstrations. That is a different harm than redundancy; larger models are robust, which is the opposite direction from "strong models are hurt". [b14, c06]
8. **Cross-cell agent correlations.** Baseline is confounded with model and benchmark. [d09, d18]
9. **Ill-structured domains.** The human data say "advanced" students still lack the key schema, so lessons stay useful. For an LLM the equivalent is that high pass rate on open tasks can be a verbosity or style artefact. [a17, K08]
10. **Probe tests.** Kalyuga's probes (r .71 to .92) were validated on well-defined tasks against the authors' process measures. [b07]

---

## 10. Open questions

1. **Within-class reversal in an agent.** Does a lesson shown on a class where the model already passes a high share of items lower accuracy, or just waste tokens? No study. (critique gap 1)
2. **Where is the cut?** Weak/middle/strong boundaries per model and the number of probe items for a stable estimate. (gap 2, K35)
3. **Model size or reasoning mode?** Does the lesson effect depend on size or on thinking on/off after controlling for class pass rate? (gap 3)
4. **Fading in agents.** Is a shortened lesson better than full or none on mid-skill classes? Nothing found. (gap 4)
5. **Delayed effect.** What delayed test fits an agent with no memory between runs? (gap 5)
6. **Item complexity versus class pass rate.** (gap 6)
7. **Per-band lesson size.** SkillsBench says 1 to 3 compact skills, no band breakdown. (gap 7)
8. **Gate for self-generated lessons.** Does a gate on verified failing outputs avoid the -8 to -11 pp penalty and cut the 13 of 87 negative tasks? Partly closed. (gap 9)
9. **Same library, several model sizes, per-task pass rates.** Lin et al. is the best curve but uses an evolved harness. (gap 10)
10. **Human open items.** Primary-paper numbers for Kalyuga 1998, 2000, 2001 were never seen. The Lee et al. 2006 table arithmetic is inconsistent. Chen et al. 2017 not opened. The Salden classroom numbers were not read.
11. **Is the asymmetry real?** Meta-analysis cannot separate theories, and median-split artefacts could produce the weak expert side.
12. **Effect of the writer.** Writer strength matters little for evidence-based updates (d21); whether this holds for per-class lessons is open.
13. **Lesson placement.** Our schema shows lessons after the first attempt. No source compares before versus after for a competence-split agent.
14. **Seed variance.** Cho and Park report sign flips between seeds; per-class estimates need several seeds. [d07]

---

## 11. Sources

[V] = opened and read this session (full text, HTML or PDF, unless noted). [M] = snippet, abstract or secondary report only.

**Founding and review (human)**
- [V, abstract-level for the 2007 review in the critique's view; Table 1 read via the handle copy] Kalyuga (2007) Expertise reversal effect and its implications for learner-tailored instruction. http://handle.unsw.edu.au/1959.4/50601 ; https://link.springer.com/article/10.1007/s10648-007-9054-3
- [V] Kalyuga (2010) Special issue introduction. https://link.springer.com/article/10.1007/s11251-009-9102-0
- [M] Kalyuga, Chandler and Sweller (1998) Levels of expertise and instructional design. https://doi.org/10.1518/001872098779480587 (via review table)
- [M] Kalyuga, Chandler and Sweller (2000) animated diagram with narration (via review table)
- [M] Kalyuga, Chandler, Tuovinen and Sweller (2001) Learner experience and efficiency of instructional guidance (via review table)
- [M] Kalyuga and Sweller (2004, 2005) rapid assessment and adaptive instruction (via review)
- [M] Tuovinen and Sweller (1999) (via review table)
- [M] Reisslein, Atkinson, Seeling and Reisslein (2006); Reisslein (2005) (via review)
- [M] Lee, Plass and Homer (2006); Yeung, Jin and Sweller (1998) (via review)
- [V, secondary] Cooper et al. (2001), Ginns et al. (2003), Leahy and Sweller (2005) as described in the review. https://link.springer.com/article/10.1007/s10648-007-9054-3
- [M] Salden, Paas and van Merrienboer (2006); Camp et al. (2001) (via review)
- [M] Salden, Aleven, Schwonke and Renkl (2009). https://doi.org/10.1111/j.1756-8765.2008.01011.x
- [M] Salden et al. (2010). https://researchportal.hw.ac.uk/en/publications/the-expertise-reversal-effect-and-worked-examples-in-tutored-prob/
- [M] Rey and Buchwald (2011). https://doi.org/10.1037/a0022243
- [V] Renkl, Atkinson and Maier (2000) Research Report 140. https://www.psycharchives.org/handle/20.500.11780/196
- [M] Atkinson, Renkl and Merrill (2003). https://doi.org/10.1037/0022-0663.95.4.774 (abstract only)
- [V] Nievelstein, van Gog, van Dijck and Boshuizen (2013). https://repository.tilburguniversity.edu/bitstreams/0d52fd41-5fe8-4095-a7c2-22e15bfc7165/download
- [M] Rourke and Sweller (2009); Kyun, Kalyuga and Sweller (2013) (via Chen 2016 thesis review chapter)
- [V] Chen (2016) PhD thesis, UNSW. https://unsworks.unsw.edu.au/bitstreams/4835a79e-b19a-4e55-bb40-168112a51706/download
- [M] Chen, Kalyuga and Sweller (2017) The expertise reversal effect is a variant of the more general element interactivity effect. https://doi.org/10.1007/s10648-016-9359-1
- [V] Leppink, Broers, Imbos, van der Vleuten and Berger (2011). https://link.springer.com/content/pdf/10.1007/s10734-011-9476-1.pdf
- [V] Tetzlaff, Simonsmeier, Peters and Brod (2025) A cornerstone of adaptivity. https://doi.org/10.1016/j.learninstruc.2025.102142 ; full text https://www.pedocs.de/volltexte/2026/34113/pdf/Learn_and_Instr_2025_Tetzlaff_u.a._A_cornerstone_of_adaptivity.pdf
- [V] Grosse (2015) Fostering modeling competencies. https://www.scimath.net/download/fostering-modeling-competencies-benefits-of-worked-examples-problems-to-be-solved-and-fading-9444.pdf
- [V] Retnowati (2017) Faded-example. https://iopscience.iop.org/article/10.1088/1742-6596/824/1/012054/pdf

**Language models and agents**
- [V] He-Yueya, Goodman and Brunskill (2024). https://arxiv.org/abs/2403.02795
- [V] Song et al. (2026) Knowledge-level simulation of novice AI students. https://arxiv.org/abs/2603.26142
- [V] Xu and Wu (2026) Skill availability and presentation granularity. https://arxiv.org/abs/2605.31408
- [V] Qiu et al. (2026) When correct demonstrations hurt. https://arxiv.org/abs/2605.26350
- [V] Agarwal et al. (2024) Many-shot in-context learning. https://arxiv.org/abs/2404.11018
- [V] Tang et al. (2025) The few-shot dilemma. https://arxiv.org/abs/2509.13196
- [V] Hannan et al. (2026) Selecting few-shot examples for vulnerability detection. https://arxiv.org/abs/2510.27675
- [V] Explainable sentiment analysis with DeepSeek-R1 (2025, authors not recorded). https://arxiv.org/abs/2503.11655
- [V] Honda et al. (2025) Distilling many-shot ICL into a cheat sheet. https://arxiv.org/abs/2509.20820
- [V] Liu et al. (2025) What makes ICL effective for mathematical reasoning. https://arxiv.org/abs/2412.12157
- [V] Zou, Khalifa and Wang (2024) Many-shot ICL for long-context evaluation. https://arxiv.org/abs/2411.07130
- [V] Wei et al. (2023) Larger language models do in-context learning differently. https://arxiv.org/abs/2303.03846
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948
- [V] Meincke, Mollick, Mollick and Shapiro (2025) Decreasing value of chain of thought. https://arxiv.org/abs/2506.07142
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183
- [V] Zhang et al. (2025) AdaptThink. https://arxiv.org/abs/2505.13417
- [V] Li et al. (2026) SkillsBench. https://arxiv.org/abs/2602.12670
- [V] Sankaranarayanan (2026) Epistemic debt. https://arxiv.org/abs/2602.20206
- [V] Hou et al. (2026) Adaptive scaffolding needs contingency. https://arxiv.org/abs/2609.22993
- [V] Anand and Idan (2026) Generative AI and the productivity divide. https://arxiv.org/abs/2605.18143
- [V] Scaffolding collapse in Socratic tutors (SPRA, 2026). https://arxiv.org/abs/2607.19371
- [M] Gonzaga, Vassar and Jiang (2026) CS TA perceptions on LLM-generated faded worked examples. https://sigcse2026.sigcse.org/details/sigcse-ts-2026-Papers/101/CS-Teaching-Assistant-Perceptions-on-LLM-Generated-Faded-Worked-Examples-for-Feedback
- [V] Cho and Park (2026) Skill following. https://arxiv.org/abs/2609.00549
- [V] Dong et al. (2026) Agent skills can be harmful. https://arxiv.org/abs/2608.11888
- [V] Feng et al. (2026) Break it down, pass it on. https://arxiv.org/abs/2608.20274
- [V] Guo et al. (2026) SkillApt. https://arxiv.org/abs/2609.26863
- [V] Hu, Long and Wang (2026) When continual learning moves to memory. https://arxiv.org/abs/2604.27003
- [V] Shang et al. (2026) When self-evolution backfires (VaG). https://arxiv.org/abs/2608.05810
- [V] Cheng et al. (2026) Scope before you persist. https://arxiv.org/abs/2609.29144
- [V] Giampieri (2026) Cortex. https://arxiv.org/abs/2610.14216
- [V, abstract and audit sections] Zhao et al. (2026) Coalition-aware skill reliability. https://arxiv.org/abs/2608.22610
- [V] Lin et al. (2026) Harness updating is not harness benefit. https://arxiv.org/abs/2605.30621
- [V] Liu et al. (2026) How well do agentic skills work in the wild. https://arxiv.org/abs/2604.04323
- [V] Ying et al. (2026) OpenSkillEval. https://arxiv.org/abs/2605.23657

**Own calculations (not literature)**
- [V] Probe-size and sample-size calculations (d25, d26), based on standard binomial methods. https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval ; https://en.wikipedia.org/wiki/Sample_size_determination
- Negative search result for agent expertise-reversal studies (d30). https://arxiv.org/search/

**Series cross-links** (not covered here): worked-example research (A05/01); extraneous load and split attention; Einstellung effect; monitoring and control; metacognition and control; spend-by-difficulty (G12); self-consistency; exploration versus exploitation; case representation; generalisability and transfer.
