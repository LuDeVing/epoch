# Productive failure: deep document

*Subfield A05.06. Sources: evidence_a-d.jsonl (ids a01-a29, b01-b28, c01-c27, d01-d18), claims.jsonl (K01-K26), critique.md. Status marks: [E] established, [S] single-source, [C] contested. [V] = page or PDF text read this study; [M] = abstract or snippet only. Today: 2026-11-10.*

## 1. What it is

Productive failure (PF) is a teaching design from Manu Kapur. Learners first try a hard, new problem **before** they are taught the method. They mostly fail to reach the correct answer. Then they get instruction that builds on what they produced. The claim: the failed first attempt prepares them to learn the method better than being taught first and practising after.

Two phases (Kapur and Rummel 2012, a06):
1. **Generation.** Learners produce several representations and solution methods (RSMs) for a novel, complex problem. No help. Most fail.
2. **Consolidation.** The teacher compares and contrasts the learners' attempts with the canonical method, and shows what each attempt missed.

The claim is **not** "failure is good" and **not** "no help is good". The claim is about order plus a specific second half (K09, [E]). Attempt without the compare-and-contrast step is not PF.

PF is one case of problem-solving-then-instruction (PS-I) against instruction-then-problem-solving (I-PS). Related names: invention activities and "preparation for future learning" (Schwartz and Martin 2004), generation (Kapur and Rummel 2012), impasse-driven learning, desirable difficulties (Bjork). Kapur (2016, a10, [M]) crosses initial performance (success or failure) with later learning (productive or unproductive) to give four designs. Direct instruction can be an "unproductive success": high practice scores, weak later learning.

**Why it matters for our agent.** The schema (section 5, memory) shows lessons only **after** the first attempt, never before, to avoid fixation. PF is the human-learning source for that rule. The question for us is narrower than for teachers: does an agent that attempts first and then reads a lesson solve later problems better than one that reads the lesson first, at equal tokens? No study has tested that (K23). Everything below is a prior, an analogy, or a boundary condition.

## 2. History and theories in depth

**Roots (before 2004).** Impasse-driven learning (VanLehn; Ohlsson) says a learner who hits a wall and sees the gap learns the repair better. Contrasting cases (Gentner; Schwartz) say comparison exposes deep structure. Desirable difficulties (Bjork) say harder learning gives better retention at the cost of worse immediate performance. PF combines these in one classroom sequence. (These roots were not opened in this study.)

**Schwartz and Martin (2004), Cognition and Instruction 22 (d01-d03 [V]).** Ninth graders in statistics. Invent a reliability index first, then hear a lecture, versus tell-and-practice. Experiment 1 (six intact classes, 95 students with pre and post): on a transfer problem, invention without a worked-example resource at test got 30.4% acceptable solutions vs 32.0% for tell-and-practice. With a resource at test: invention 60.8% vs 29.2%. Experiment 2 (four teachers): without resource 18.2% vs 26.6%; with resource 45.8% vs 21.9%. So the benefit shows only when the test lets the learner learn something new ("double transfer"). The gain was smaller with other teachers. A year-later test of 30 students: mean-deviation computation 5% pre, 86% post, 57% at one year, no control. Classes, not students, were assigned.

**Kapur (2006, ICLS), a01-a02 [V].** 309 11th graders in 7 Indian schools, 103 triads randomly assigned (50 ill-structured, 53 well-structured). Group text chat on kinematics. The ill-structured groups did worse as groups, then beat the well-structured groups on individual post-tests (well-structured chi2=22.82, ill-structured chi2=27.21, both p<.001). Process coding: ill-structured groups did more problem analysis (F=18.20), critique (F=11.91) and criteria talk; well-structured groups did more solution development. Kapur's account used complexity theory ("edge of chaos"), a metaphor and not a tested model. The step from ill- to well-structured problems is part of the treatment.

**Kapur (2008)** is the paper the SUBFIELDS row cites. It was never opened. Treat its numbers as unknown.

**Kapur 2009-2012 core studies.** Seventh-grade Singapore classes on average speed (a03, a04, b15). 75 students, two intact classes; only 11% and 21% of PF groups solved the two group problems; mean confidence 1.22 of 4. A lower-ability school replicated with 114 students in 3 classes. Kapur (2012, variance, 9th grade, 140 students) and Kapur (2014, variance, vicarious failure, 136 eighth graders) are abstract only (d18, a09, c27 [M]). Kapur and Bielaczyc (2012) PF students produced about 6.03 solutions each (quoted in d06).

**Theory consolidation.** Loibl, Roll and Rummel (2017, b03 [V abstract], a28 [M]) name three mechanisms: (1) activation of prior knowledge, (2) awareness of knowledge gaps, (3) recognition of deep features in the instruction. Design features that trigger them: an open task with a rich solution space, and instruction that contrasts or builds on student solutions. The theory was built after the studies. Study effects across PS-I range from d=-0.54 to 1.12 (b03, b12, K02 [E]).

**Replication era (2013-2025).** Independent labs (Rummel, Loibl, Renkl, van Gog groups in Germany and the Netherlands; Roll in Canada) found mixed to null results (section 5). The originator's group pooled the literature (Sinha and Kapur 2021). Newer work asks when observing failure is enough (Braas 2025) and whether generative AI can host PF (Puech 2025, Rotter 2026).

**LLM era (2023-2026).** Two separate lines. (a) Agents that learn from their own failed attempts: Reflexion, ExpeL, LEAP. They do not use PF as a design, but they are the machine version of "attempt, fail, extract a lesson". (b) Education studies where an LLM is the tutor and PF is the pedagogy (StratL, access-timing RL, "struggle first, prompt later"). Neither line tests PF as a reasoning scaffold for the model itself.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pooled PS-I over I-PS, conceptual understanding and transfer | Hedges g=0.36 [0.20, 0.51], 53 studies, 166 comparisons; high-fidelity PF g 0.37-0.58; authors' bias-adjusted g=0.87 (model-dependent) | Sinha and Kapur 2021 (a11, b01, c06, d10; abstract only) | [S] one lab pooled it; K01 |
| No gain for procedural knowledge; young children and domain-general skills favour instruction-first | grades 2-5 reversed; study table unread | same (d10) | [S] |
| Extra scaffolds in the problem phase do not help | PS-I vs scaffolded PS-I g=-0.08 [-0.20, 0.04]; PS-I vs sensemaking g=0.22 [-0.06, 0.51]; 33 articles, 118 comparisons | Sinha and Kapur EdArXiv (a12, c07) | [C] preprint; K10 |
| Spread of effects | d from -0.54 to 1.12 | Loibl et al. 2017 via b12 | [E] K02 |
| Original double-transfer result | Exp 1: 60.8% vs 29.2% with resource; 30.4% vs 32.0% without. Exp 2: 45.8% vs 21.9% with; 18.2% vs 26.6% without | Schwartz and Martin 2004 (d01, d02) | [S] K21 |
| Kapur kinematics, group chat | N=309, 103 triads; ill-structured beat well-structured, chi2=22.82 and 27.21, p<.001 | Kapur 2006 (a01) | [S] |
| Singapore average speed | PF vs lecture-practice: MANOVA F(2,71)=5.64, p=.005, partial eta2=.144, N=75. School 2, N=114: complex item PF-B 3.86, PF-A 2.58, LP 1.01, F(2,110)=17.98, eta2=.25; tabular item no difference | Kapur 2009 (a03, a04) | [S] K03 |
| PF groups mostly fail | 11% and 21% of groups solved the two group problems; mean confidence 1.22/4 | a03 | [S] |
| Number of methods predicts learning | RSM count F(1,107)=62.59 and F(1,100)=105.52, both p<.001; prior achievement ns in study 2; N=112 and 105 | Kapur, Saba, Roll 2023 (b13, c09, d04) | [C] association only; K06 |
| Supplied diversity is causal (observing) | N=152; VF-high 1.84, PF 1.47, VF-low 1.25, DI 1.05; VF-high vs VF-low d=0.644; vs DI d=0.648; vs PF d=0.292 ns; PF vs DI d=0.294 ns | Braas et al. 2025 (b08, d05) | [C] one randomised study; K06, K08 |
| Component coverage tracks outcome | PF arm 3.63 solutions, 1.22 canonical components each; components vs conceptual score r=.418, p=.009 | Braas 2025 (d06) | [S] |
| Replication outside STEM, Study 1 (wrong way) | N=212; total F(1,209)=27.46, partial eta2=.12; PF 10.97 vs DI 13.88; transfer F(1,210)=31.11, eta2=.13; canonical solve 24% PF vs 48% DI | Nachtigall et al. 2020 (a16, b05, d07) | [E] with the others; K04 |
| Replication, Study 2 (null) | N=152; total F(1,148)=0.32, p=.57, eta2=.002; BF10=0.23; 9% vs 18% canonical | same (a17) | [E] K04 |
| Bayesian reasoning (null) | N=75, 2x2; order F(1,71)=0.04, p=.84; 31 of 38 made one attempt (original about 4.13) | Loibl and Leuders 2024/25 (a18, b07, d09) | [E] K04 |
| Fifth graders (null) | N=228; timing F(1,224)=1.01, p=.32; posttest alpha=.54 | Mazziotti et al. 2019 (b09) | [E] K04 |
| Pre-service teachers (reversed) | N=44; worked solution beat inventing, F(1,38)=4.95, p=.032, d=-0.72; 2022 repeat N=45, transfer BF+0>313 | Glogger-Frey et al. 2015/2022 (a13, a14) | [E] K04 |
| Delaying instruction alone, no benefit | N=181, 2x2 order x contrasting cases; instruction-first better on procedural fluency | Instr. Sci. 2020 (c11 [M]) | [S] |
| Primary school motor skill (null) | 50 fourth graders; no order effect on throwing distance | Loibl and Leukel 2025 (a19 [M]) | [S] |
| DIY PF in a large biology course | PF section 295 vs 279; Midterm 2 topics b=4.78 points [2.19, 7.36], effect 0.32; final exam b=0.78, p=.668; Low tercile b=8.28, p<.001 | Chowrira et al. 2019 (a15) | [S] K11; PF section had higher baseline |
| University linear algebra, 4 years | exam d=0.38, 0.59, 0.28, 0.54; voluntary participation, cohort comparison, no control | Baumgartner et al. 2025 (b10, b24) | [S] K20 |
| Failure-driven scaffolds beat success-driven | N=221; non-isomorphic conceptual d=0.409 (topic SC), d=0.387 (AQ); isomorphic d=0.586 (AQ only); omnibus mixed | Sinha et al. 2019 (b11); replicated 2021 (c12 [M]) | [S] |
| Perceived competence | PF 3.53 vs DI 3.09 after phase 1 (partial eta2=.08); 3.02 vs 3.92 after phase 2; drop vs learning r=-0.36 | Nachtigall 2020 (b06, d08) | [C] K07 |
| Python, tiny study | DI n=9, PF n=7; first task DI 8/9, PF 2/7; delayed task DI 6/9, PF 7/7; no tests | Suriyaarachchi et al. 2025 (a20, b18, c05) | [S] K19; do not use for decisions |
| Vicarious vs own failure (older) | 136 eighth graders; own failure gave more effort and interest in the canonical solution; numbers unread | Kapur 2014 (a09 [M]) | [C] |
| Earlier smaller meta-analysis | 12 usable experiments of 62 relevant; "moderately positive" | Darabi et al. 2018 (b04) | [S] |

## 4. Mechanisms and models

Each mechanism is written so an engineer could turn it into a loop.

**M1. Prior-knowledge activation.** During the attempt the learner pulls up everything related and tries it. The later lesson then attaches to those items. Machine form: before the lesson is shown, the model writes its own candidate approaches; the lesson is then compared against them. Evidence: Nachtigall found activation present yet no gain (b21, a28). So activation looks necessary but not sufficient.

**M2. Gap awareness.** The learner sees that their method fails or is incomplete. Machine form: a code check fails, or two attempts disagree (already G1's trigger). The model must name what the failing output shows (G2). Human data: gap awareness had small positive links to posttest (beta=.112 and .172, b26). Counter-data: PF students felt more competent after the attempt and did not notice failure (b06). Awareness needs an outside signal. In a machine that signal is the verifier.

**M3. Deep-feature recognition (compare and contrast).** The consolidation step lays learner attempts beside the canonical method and marks which component each attempt covers or misses. Machine form: given K attempts and one reference solution, code builds a table "component x attempt", and the model writes one line per missing component. Evidence that coverage is the active ingredient: VF-high, covering all four canonical components, beat VF-low (d=0.644); component count tracked score (r=.418) (d05, d06). Attempt quantity did not (quantity vs posttest r=.11 ns; quality r=.33 individual, r=.55 group; b06).

**M4. Diversity of candidate methods.** Many distinct methods in the attempt phase go with learning more than prior achievement does (F=62.6, 105.5). Machine form: count **distinct** approaches by code, not by model opinion, not tokens. Causal when supplied (Braas), unproven when self-generated. The originator lab's students produced 6+ solutions each; other labs got 3-4 (d06). But Nachtigall's 3.93 ideas per group still failed, so count is not the cause (K05, K24).

**M5. Motivation and effort.** Kapur 2014: PF raised effort and interest in the canonical solution [M]. Glogger-Frey: inventing raised curiosity and felt gaps, yet a worked solution still taught more (a13). Motivation does not carry the learning.

**M6. Unproductive success.** Direct instruction then practice can give success that does not last (Suriyaarachchi's authors, c25; Bastani's unrestricted GPT group, a24). Machine analogue: a model shown the lesson first copies it and does well on near items, with no representation of why alternatives fail. This is a hypothesis, untested on LLMs.

**M7. Verifier-gated lesson extraction (the agent form).** Loop: attempt, check against ground truth or reliable tests, on failure write a short verbal reflection, store it, retry or use it on later items (Reflexion, ExpeL, LEAP). Reliability of the check decides the sign: reliable tests HumanEval 0.80 to 0.91 (+11); noisy tests (16.3% false pass) MBPP 0.80 to 0.77 (-3); no tests Rust hard-50 0.60 to 0.52 (-8) (d14; K17 [E]). Without an outside label, self-correction lowers accuracy (GPT-4-Turbo GSM8K 91.5 to 88.0; CommonSenseQA 84.0 to 81.5; c17 [V]). This is the key engineering fact: the "lessons" half is only as good as the verifier.

**M8. Timing policy (access control).** Rotter et al. encode PF as a reward: penalise help before any effort, reward help after struggle, penalise long unproductive struggle (b27, c24). Machine form: do not show the stored lesson until at least one attempt has been made and failed or disagreed; if attempt count or budget hits a cap, release the lesson. This matches schema G1, S5/S6 and the memory rule.

**M9. Steering a model along a plan (StratL).** A hand-built transition graph, a student-state tracer (micro F1 0.77) and an intent injected into the prompt. Letting the LLM choose the intent from a written description was worse than the graph (PF score on Country 3.11 vs 4.00; RSMs 1.34 vs 2.34; c02). Plain prompting with the strategy text failed to hold the plan (b16). Lesson: the program, not the model, runs the order of phases. This agrees with schema section 1.

## 5. What holds up

**Holds with moderate confidence.**
- The average in the originator-led pool is positive but small (g=0.36). It is contradicted at study level often enough that the sign depends on design and domain (K02 [E]).
- Consolidation matters. Attempt alone is not the claim (K09 [E]). PS-I helps only when the instruction contrasts cases or builds on student solutions (b03).
- Quality and coverage of attempts matter more than raw count (b06, d06).
- Without a verifier the lesson step does not help and can hurt (K17 [E], four sources).

**Replication failures (K04 [E], five independent sources).** Nachtigall Study 1 went the wrong way (partial eta2=.12); Study 2 null with BF10=0.23. Loibl and Leuders null. Mazziotti null in 5th grade. Glogger-Frey: worked solution better, twice. Loibl and Leukel null in primary school. Braas: PF vs DI d=0.29, ns (underpowered for d near 0.3, as the authors say).

**Why they failed: no single cause (K24 [C]).** Loibl and Leuders: one attempt per student (31 of 38), perhaps because the data display let students keep one method (b23, post hoc). Nachtigall: about 4 ideas per group, so "few attempts" is wrong; but typical errors were missing in many groups (pretest absent 93%, variable variation violated 82%), the domain was non-STEM, work was in groups, and the best attempt used 5.07 of 8 principles with no group solving canonically (b22, d07). Braas: 3.63 solutions with low component coverage. Mazziotti: young age; the "experimental dilemma" is that a problem hard enough to make older students fail is too hard for children (b25). All of these are post hoc; nobody manipulated them.

**Moderators.**
- Age: grades 2-5 reversed in the meta-analysis abstract; fifth graders null; fourth graders null. Older learners and longer interventions gain more.
- Domain: STEM concept learning (variance, rate) holds the wins. Knowledge ABOUT how a domain works (research methods) failed (conjecture, b21). Domain-general skills favoured instruction-first.
- Prior knowledge: low-prior students gained most in a large biology course (b=8.28), but the final exam showed no effect (a15). Not clean: the PF section had a higher baseline.
- Support in the problem phase: failure-driven scaffolds beat success-driven ones in two conference-level studies (b11, c12); meta-analytic extra scaffolding added nothing (g=-0.08). Roll et al.: metacognitive prompts raised conceptual quality of invented methods (a08). Westermann and Rummel: a role script let PF groups beat DI in weeks 2-4 of a university study (a07).
- Test type: the Schwartz and Martin win appears only when the test supplies a resource to learn from (d01, d02).
- Lab: originator designs are mostly quasi-experimental intact classes. Lab share in the meta-analysis is unknown (gap 1 open). The pooled g=0.36 against mostly null independent replications is consistent only if the pool leans on originator studies (critique).

**Interventions that worked (human).** Supplying a high-diversity set of failed attempts (Braas); failure-driven scaffolding (b11); contrast-based consolidation (Kapur designs); script support in a university course (a07); a do-it-yourself version by ordinary instructors, partially (a15).

**Interventions that did not.** Merely delaying instruction (c11); building the instruction on typical student solutions in Bayesian reasoning (a18); collaboration for young children (b09); extra scaffolding (a12); adaptive questions over fixed ones in AI pretesting (Study 2 of a25, t(76)=1.002, p=.319).

**Retention.** Untested against a control beyond a week in the sources opened (K25). Schwartz and Martin's one-year result has no control. The Python delayed-task result has n=16 and no tests.

**Calibration.** PF students felt more competent after the attempt (3.53 vs 3.09), then less after instruction (3.02 vs 3.92); a bigger drop went with lower learning (r=-0.36). In Kapur's Singapore classes PF confidence was low (1.22/4). Not reconciled (K07 [C]).

**Evidence-quality warnings.** Kapur 2008, 2011, 2012, 2014 and the full text of Sinha and Kapur 2021 were not read. Records a05, a09-a12, a14, a19, a27, b20, c06, c08, c10-c12, c19, c22, c27 are abstract or snippet level. The same studies appear several times in the files (a21/a22/b16/b17/c01-c03 are two studies; a11/b01/c06 are one meta-analysis). Count them once.

## 6. Language models

**No direct test.** No study found compares attempt-first with instruction-first on **LLM task accuracy** at equal tokens (K23). This is absence in a limited search: the shared search budget ran out and the APIs were rate limited. Everything below is an analogy or a different object.

**A. Agents that learn from their own failed attempts (the machine analogue).**
- **Reflexion** (Shinn et al. 2023; c13, c14, c26 [V]). ALFWorld ReAct+Reflexion solved 130 of 134 tasks over 12 trials (+22 points absolute); HotPotQA +20; HumanEval Python up to +11. The written reflection is the active part: reflection beat plain last-trajectory memory by 8 points on HotPotQA; removing the explanation gave no gain; baselines fixed no failed task on retry at temperature 0.7. WebShop: no gain after 4 trials over 100 environments. Gains need a success signal.
- **Verifier quality** (d14). HumanEval 0.80 to 0.91 with reliable tests (1% false pass); MBPP 0.80 to 0.77 with 16% false pass; Rust hard-50 base 0.60, no test generation 0.52, tests but no reflection 0.60, both 0.68. So tests alone gave nothing on Rust; the reflection text added +8 on top of tests.
- **ExpeL** (Zhao et al. 2024; c15, c16). Cross-task insights from comparing failures and successes. ALFWorld: ReAct 40.0, random examples 42.5, similarity retrieval 48.5, ExpeL 59.0; HotpotQA 28.0 to 39.0. Insights-only vs retrieval-only: HotpotQA 36% vs 31%, ALFWorld 50% vs 55%. ExpeL plus Reflexion reached 64.2 at round 3. Rounds R1-R3 started from failed R0 states, so not a clean test.
- **LEAP** (Zhang et al. 2024; d12, d13). The closest attempt-first test. The model answers few-shot examples, sees the ground truth, explains its errors, and uses the principles on new questions. Few-shot CoT vs LEAP high-level (low-level): DROP GPT-4 72.05 to 78.60 (79.55); HotpotQA GPT-4 36.35 to 39.65; GSM8K GPT-4 93.6 to 93.8 (94.2); MATH GPT-4 63.5 to 64.0 (64.5); DROP GPT-4-turbo 83.40 to 80.00; HotpotQA Gemini Pro 28.25 to 25.50. Llama-2-chat-70B got worse: GSM8K 52.5 to 50.6 or 47.0, MATH 16.2 to 13.8. It wrote sensible principles but did not follow them. Not token matched, no intervals. The gain is real on reading and multi-hop tasks, near zero on math, negative for weak models. It uses ground truth.
- **Other** (c19 [M], 2026). Experiential Reflective Learning, Gaia2 +7.8% over ReAct, abstract only.

**B. Boundary: self-correction without a label.** Huang et al. 2024 (c17 [V]): with oracle labels GPT-3.5 GSM8K 75.9 to 84.3, CommonSenseQA 75.8 to 89.7; without, GPT-4-Turbo GSM8K 91.5 to 88.0, CommonSenseQA 84.0 to 81.5. GPT-3.5 kept its first answer 74.7% of the time on GSM8K and changed right to wrong more than wrong to right. Kamoi et al. 2024 (d15): no reliable prompted self-correction without external feedback, except where checking is easier than solving. This matches schema 4b.

**C. Learning from others' mistakes vs own (training).** LeMa (d16): GPT-4 corrected 8.0% (217 of 2,696) of its own wrong MATH paths, 37.5% of LLaMA-2-70B's and 26.9% of GPT-3.5-Turbo's. This is confounded with difficulty. Fine-tuning on corrected mistakes beat CoT-only; dropping the corrected solution or the explanation hurt. Wang et al. 2024 (c18): failed trajectories help if marked as negative (NAT, +8.74% with a 7B model and 2k positives; +0.52% at 13B and 5k), and hurt if mixed in as good ones (NUT). Multi-attempt RL (d17): Qwen 2.5 Math 1.5B 45.6% with one attempt to 52.5% with two; single-turn trained 42.3% to 43.2%. All of these change weights, use oracle feedback and are not equal-token.

**D. LLMs as PF tutors (the model teaches humans).**
- **StratL** (a21, a22, b16, b17, c01-c03 [V]; re-checked in critique). Simulated students, 3 conversations x 2 problems per version. Mean student RSMs: StratL 2.34, no-intent baseline 1.00, constant intent 1.34, LLM-chosen intent 1.34. PF score on Consistency (max 4): 3.67, 1.33, 4.00, 3.67; on Country: 4.00, 0.44, 4.00, 3.11. State tracing micro F1 0.77. Field study N=17 ninth graders, 15 minutes: PF score p=.046, RSMs 2.6 vs lower, p=.05, but helpfulness 1.20 vs 2.00 on Consistency. No learning measure. A tutor that never hints can game the PF score (b17). Without steering the LLM tutor gives away solutions (c01).
- **Rotter et al. 2026** (a23, b19, c04 [V]). N=105; post-test (0-8) Always 4.03, RL 5.11, Never 5.25. RL vs Always t(71)=2.51, p=.014, d=0.59; RL vs Never d=-0.07. AI requests 11.25, 2.46, 0. Metacognitive accuracy RL vs Always d=0.54. Metacognitive gain no condition effect (F(2,87)=0.86). A secondary "fewer mistakes" result vanished after controlling for gender. Pilots n=9 and 7; the policy was trained on a simulated student. Timed access did not beat no access.
- **Bastani et al. 2025** (a24 [V PDF]; b20, c22 [M]). About 1,000 students; practice +48% (GPT Base) and +127% (GPT Tutor); unaided exam GPT Base -17% (-0.054), GPT Tutor -0.004 (null). Guardrailed hints removed the harm; students did not notice they had learned less. Prompt length is confounded.
- **Akgun and Toker 2025** (a25 [V]). Pretest then ChatGPT; final test 91.85 vs 78.59, t(58)=5.979, d=1.543, N=60, one session, preprint. Adaptive questions no better than fixed (n=78, p=.319); Study 3 F(1,85)=5.839, p=.018.
- **Lehmann et al. 2025** (a26): asking the LLM for solutions substituted for work; 42% of solution requests came with no student attempt. **Oreopoulos et al. 2026** (c21): 6,000+ students; AI students attempted fewer questions with higher accuracy per attempt; delayed gains marginal. **Small vs large models writing PF problems** (c20): GPT-4o 13.38 vs Phi-3 10.67, d=1.16 on rater scores.

**What changed outcomes, by how much.** Reliable verifier: +11 vs -3 (noisy) and -8 (none) in Reflexion. Reflection text over tests alone: +8 (Rust). Distilled cross-task insights over similarity retrieval: 59.0 vs 48.5 on ALFWorld, but insights-only vs retrieval-only was mixed. Model strength: LEAP helps GPT-4 on DROP (+6.5 to +7.5) and hurts Llama-2-70B and sometimes GPT-4-turbo. Steering by program vs by prompt: RSMs 2.34 vs 1.34.

**Not found.** No study measured LLM confidence or calibration after a failed-then-lessoned cycle (K26). No study tested supplied failure vs own failure in prompting; only LeMa in fine-tuning.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **A lesson is written only from a code-observed failure or pass-fail contrast; with no check, store no lesson.** Part: G2/G3, memory (S9). Status [E]. Evidence: K17; c13, c14, c17, d14, d15. This extends G2 and schema 4b: make S9's lesson line conditional on a verified signal.
2. **The lesson is a comparison, not a verdict.** It names what the failing attempt missed relative to a checked-correct one. Part: S5/S9. Status [E] for "consolidation by contrast is the second half" (K09: a01, a02, a28, b03, c11); the written explanation being the active part in agents is [S] (c14, one paper).
3. **Do not use attempt count as the signal.** Log attempts, distinct methods and component coverage per item; do not gate the lessons on count. Part: logging (schema section 6), S3. Status [E] that count alone does not decide outcome (K05, K24: b06, d06, d07).
4. **Keep "lessons after the first attempt, never before".** Part: memory. The PF-order benefit is [S]/[C] (K03, K04), so this is kept as a harmless default, not as a proven gain. Do not claim more than "no harm known".

### Test first (single-source or contested)

1. **Attempt-then-lesson vs lesson-then-attempt at equal tokens.** Part: memory/S9. [S]/[C] K03, K04, K23. No LLM test exists.
2. **Verifier dependence: oracle, noisy, none, one lesson step, one task.** Part: G/S9. [E] for the direction (K17), never run in one design. Evidence d14, c17.
3. **Own failed attempt vs supplied failed attempt as the lesson source.** Part: memory. [C] K08; human a09, d05; LLM only fine-tuning d16.
4. **Component coverage of the attempt set as a gate or trigger.** Part: S3/O. [C] K06; d04, d05, d06.
5. **Calibration log: stated confidence before and after the lesson.** Part: G calibration. [S] K07, K26; d08.
6. **Scaffold level during the attempt (unguided vs guided).** Part: S3. [C] K10; a12, c07, a08.
7. **Failure-driven vs success-driven framing of the attempt.** Part: S3. [S] b11, c12.
8. **Timing rule: release the lesson only after a failed check or a budget cap (Rotter reward as code).** Part: S9/G1. [S] K14; b27, c24.
9. **Weak vs strong model.** Part: S0 mode choice. [S] K11 (low-prior students gain more) against LEAP's negative result for Llama-2 (d13). Check per model.

## 8. Concrete tests on our bench

Rule for all tests: both arms use the same total token budget, setup cost counted (G7). Report per item type, not pooled, because the sign depends on type (K02). Use at least 3 seeds per cell with intervals (LEAP seems to have used single runs). Drop items the plain model solves on its first attempt (no lesson step reached) and report the fraction dropped.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style items with a held-out check; BrainTeaser puzzles with a known answer | A: attempt (S3-S4), then lesson from class memory, then re-attempt. B: lesson first, then attempt, then re-attempt | Pass rate on held-out inputs; second-attempt gain over first | Small if any (0 to +3 points); sign varies by type |
| T2 | Same items | Lesson step with (i) oracle check, (ii) noisy check (about 16% false pass), (iii) no check | Net change in pass rate vs no-lesson baseline | (i) about +5 to +10; (ii) about -3 to 0; (iii) about -8 to 0 |
| T3 | Items where a failing and a correct attempt both exist | Lesson from agent's own failed attempt vs a supplied failed attempt from another run vs a correct example only | Pass rate on a sibling class | Own about equal to supplied, both at or above correct-only |
| T4 | Items with several canonical components (multi-rule ARC) | Code-forced diverse attempts (untried directions, S3 open mode) vs plain independent samples | Distinct methods (by code); pass rate; correlation of component coverage with lesson gain | Diversity raises coverage; small pass-rate gain; separates cause from correlate |
| T5 | Mixed items | Log stated confidence before and after the lesson in arm A of T1 | Brier score; confidence-minus-accuracy gap | If confidence rises while accuracy falls, calibration is damaged (Nachtigall pattern) |
| T6 | Same items | Unguided attempt phase vs guided (one line per attempt naming what the failing output shows) | Pass rate; tokens used | Little difference (meta-analytic g=-0.08) |
| T7 | Same items | Lesson released only after a failed check vs always after the attempt vs before the attempt | Pass rate; lesson-use rate | After-fail at or above always; before worst (fixation) |
| T8 | Strong and weak base models | T1 arm A vs plain, per model | Net gain by model | Weak model gains less or loses (LEAP, Llama-2) |

## 9. What does not transfer, and why

- **Effort, interest and persistence effects.** Humans may learn from struggle because they are motivated or because it activates prior knowledge. A model has no motivation; its "prior knowledge" is fixed in weights and context. Effort gains (Kapur 2014 [M]) are not a mechanism for us.
- **Confidence drop after instruction** (Nachtigall) is a human metacognition effect. For the agent it matters only as a calibration log item.
- **Group chat and classroom collaboration** (Kapur 2006, Mazziotti): the schema bans debate (G9) and treats samples from one model as correlated (G4).
- **Teacher-run consolidation with a canonical solution.** The agent has a reference only when a check or gold answer exists, which is the verifier question.
- **Tutor-fidelity and student-outcome results (StratL, Rotter, Bastani, Akgun).** They measure how a model teaches humans, not how a model reasons. Do not cite them as evidence that the lessons step improves accuracy (K12-K14).
- **One-year retention** (Schwartz and Martin): the agent's memory is a file, not a decaying trace.
- **Age and domain boundaries** (below grade 6; non-STEM): they say the effect depends on task type. We have no map from our item types to theirs.
- **Fine-tuning evidence (LeMa, NAT, multi-attempt RL).** It changes weights. Our aim is a scaffold, not training.
- **Reflexion-style free retries with feedback at test time.** Our tasks seldom allow them. ExpeL and LEAP (lessons from other items) are the right analogues.

## 10. Open questions

1. Lab share, study-level effects and domain splits in Sinha and Kapur (2021) (gap 1). The full text returned 403.
2. Does attempt-first beat lesson-first for an LLM at equal tokens (gaps 2 and 7)? Not tested anywhere found.
3. How strongly does the lesson step depend on the verifier when the same step runs under oracle, noisy and no check (gap 3)? Reflexion has three levels but on different tasks.
4. Is own-generation diversity causal (gap 4)? Only supplied diversity was manipulated. Can an agent be forced to diversify, and does that help?
5. Is a supplied failed attempt as good as the agent's own for a lessons memory (gap 5)? Brand et al. 2024 and Kapur 2014 numbers are unread.
6. Exact numbers for Kapur 2008, 2012 and 2014 (gap 6) are unknown.
7. Does a lessons cycle damage calibration in LLMs (gap 9)? Only Nachtigall's student data exist.
8. Retention beyond a week against a control (gap 10). Suriyaarachchi has n=16.
9. Why do originator studies show about 6 solutions per student and others 3-4, and does it matter? Observed (d06), not tested.
10. Does the effect on LLMs depend on model size? LEAP hints yes, from one open model.
11. Is the Schwartz and Martin pattern (benefit only when the test supplies a resource) the right analogue for an agent with retrieval at test time? Untested.

## 11. Sources

[V] opened this study; [M] abstract or snippet only.

**Primary and replication, human**
- [V] Kapur (2006) ICLS paper. https://escholarship.org/uc/item/5f26n97z
- [V] Kapur (2009) CogSci, Studies 1 and 2. https://escholarship.org/uc/item/7bj6f9rz
- [M] Kapur (2009) Instr. Sci. 38 (abstract page). https://link.springer.com/article/10.1007/s11251-009-9093-x
- [M] Kapur (2012) Instr. Sci. 40 (abstract only). https://link.springer.com/article/10.1007/s11251-012-9209-6
- [M] Kapur (2011) J. Learning Sci. https://doi.org/10.1080/10508406.2011.591717
- [M] Kapur (2014) J. Learning Sci., vicarious failure. https://doi.org/10.1080/10508406.2013.819000
- [M] Kapur (2014) Cognitive Science. https://doi.org/10.1111/cogs.12107
- [M] Kapur (2016) Educ. Psychologist. https://doi.org/10.1080/00461520.2016.1155457
- [V] Kapur and Rummel (2012) editorial, with Westermann and Rummel, Roll, Wiedmann as summaries. https://link.springer.com/content/pdf/10.1007/s11251-012-9235-4.pdf
- [V] Schwartz and Martin (2004). http://aaalab.stanford.edu/papers/CI2202pp129-184.pdf
- [V] Kapur, Saba, Roll (2023) npj Sci. Learn. https://www.nature.com/articles/s41539-023-00165-y ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10185511
- [V] Chowrira et al. (2019). https://www.nature.com/articles/s41539-019-0040-6.pdf
- [V] Nachtigall, Serova, Rummel (2020). https://link.springer.com/article/10.1007/s11251-020-09525-2
- [V] Loibl and Leuders (2024/25). https://link.springer.com/article/10.1007/s11251-024-09670-y
- [M] Loibl and Leukel (2025) javelin. https://doi.org/10.1007/s11251-024-09700-9
- [V] Mazziotti et al. (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6435728/
- [V] Glogger-Frey et al. (2013/2015). https://escholarship.org/uc/item/78d7k1zs
- [M] Glogger-Frey et al. (2022). https://doi.org/10.1007/s11251-022-09577-6
- [V] Braas et al. (2025). https://link.springer.com/content/pdf/10.1007/s11251-025-09706-x.pdf
- [M] Brand et al. (2024). https://doi.org/10.1016/j.learninstruc.2024.102052
- [V] Baumgartner et al. (2025). https://link.springer.com/article/10.1007/s11251-025-09709-8
- [V] Sinha et al. (2019) CogSci. https://escholarship.org/uc/item/4t91d604
- [M] Robust effects of explicit failure-driven scaffolding (2021). https://doi.org/10.1016/j.learninstruc.2021.101488
- [M] Contrasting cases prior to and after instruction (2020). https://doi.org/10.1007/s11251-020-09504-7
- [V] Suriyaarachchi, Denny, Nanayakkara (2025). https://arxiv.org/abs/2411.11227

**Meta-analyses and reviews**
- [M] full text; abstract read via Crossref: Sinha and Kapur (2021) RER. https://doi.org/10.3102/00346543211019105 ; https://api.crossref.org/works/10.3102/00346543211019105
- [M] Sinha and Kapur (EdArXiv) preparatory approaches, repository summary page. https://research-collection.ethz.ch/handle/20.500.11850/492056
- [M] Darabi et al. (2018), abstract page. https://link.springer.com/article/10.1007/s11423-018-9579-9
- [M] Loibl, Roll, Rummel (2017), abstract page. https://link.springer.com/article/10.1007/s10648-016-9379-x
- [V] Kapur, Hattie, Grossman, Sinha (2022), first 100,000 characters. https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2022.956416/full
- [V] phys.org press summary (2021). https://phys.org/news/2021-09-productively-wiser.html

**LLM and AI**
- [V] Puech et al. (2025) StratL, arXiv 2410.03781. https://arxiv.org/abs/2410.03781
- [V] Rotter et al. (2026), arXiv 2605.15850. https://arxiv.org/abs/2605.15850
- [V] Bastani et al. (2025) PNAS, PDF copy. https://nmdprojects.net/teaching_resources/bastani_generative_ai_can_harm_learning.pdf ; [M] publisher page https://www.pnas.org/doi/10.1073/pnas.2422633122
- [V] Akgun and Toker (2025), arXiv 2504.10249. https://arxiv.org/abs/2504.10249
- [V] Lehmann, Cornelius, Sting (2025), arXiv 2409.09047. https://arxiv.org/abs/2409.09047
- [M] Oreopoulos et al. (2026) NBER 35621 (abstract page). https://www.nber.org/papers/w35621
- [M] Small vs Large LMs generating PF problems (2026), abstract via OSF. https://doi.org/10.22318/icls2026.113185
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Huang et al. (2024) cannot self-correct. https://arxiv.org/abs/2310.01798
- [V] Zhang et al. (2024) LEAP. https://arxiv.org/abs/2402.05403
- [V] Kamoi et al. (2024) survey. https://arxiv.org/abs/2406.01297
- [V] An et al. (2024) LeMa. https://arxiv.org/abs/2310.20689
- [V] Wang et al. (2024) negative examples. https://arxiv.org/abs/2402.11651
- [V] Chung, Du, Fu (2025) multi-attempt RL. https://arxiv.org/abs/2503.04808
- [M] Experiential Reflective Learning (2026), arXiv 2603.24639. https://doi.org/10.48550/arxiv.2603.24639
- Not opened and not recorded: Kapur (2008) Cognition and Instruction; Bjork and Bjork (2011); VanLehn impasse papers.
