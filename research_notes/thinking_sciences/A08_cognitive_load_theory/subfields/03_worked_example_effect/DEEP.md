# Worked-example effect: deep document

*Subfield A08.03. Sources: evidence_a-d.jsonl, claims.jsonl, critique.md in this folder. Evidence ids (a01 ... d18) refer to those files; claim ids (K01 ... K22) to claims.jsonl. Overlap with sibling documents: 01 intrinsic load and element interactivity, 02 split attention, 04 expertise reversal. Those are only linked here.*

## 1. What it is

The worked-example effect is the finding that novices learn more, or learn the same in less time, from studying solved problems than from solving the same problems themselves. It is the best-known effect of cognitive load theory (CLT).

The core idea is simple. A novice who solves a problem searches. Search holds the goal, the current state and the gap between them in working memory. That leaves little room to build a schema, which is a stored pattern of "this kind of problem, this kind of step". A worked example removes the search. The learner sees states and the operators that link them, so attention goes to the pattern (a07, b07).

Typical design: pairs of items. The first is solved, the second is a problem of the same type. Control group: all problems, no solutions.

What the effect is not:
- It is not a claim that practice is useless. Practice is needed for automation (a15).
- It is not a claim that examples always win. It is bounded by learner expertise and by how many elements interact in the material (a12).
- Its most reliable gain is efficiency (same score, less time), not a large accuracy jump (a23, b10, d13).

Why we care: our agent has a planned subgoal library, a store of solved subgoals offered by similarity (SCHEMA section 5). This subfield asks when stored solutions help, when they hurt, how to format them, and how to retire them.

Important honesty point. No study we found runs the CLT design (solved example vs bare problem, matched load) on an LLM agent (K17, c29). Every LLM result below is an analogy: it varies what is in the prompt, not working-memory load.

## 2. History and theories in depth

**Before 1985.** The common belief was that practice is the way to learn problem solving. Quotes in a14: "The best way to teach children how to solve problems is to give them lots of problems to solve" (Van Engen 1959). Chase and Simon (1973): practice is the major independent variable in skill acquisition.

**Goal-free effect (precursor, early 1980s).** Sweller, Mawer and Ward (1983, kinematics and geometry) and Owen and Sweller (1985, trigonometry) found that a non-specific goal ("find all the angles you can") stops means-ends search and improves schema construction. Ayres (1993): most errors on two-step geometry problems fall in the subgoal phase. Vollmeyer, Burns and Holyoak (1996): means-ends analysis slowed learning in biology problems (a10). Two ways to cut search load: show the solution, or remove the target.

**Founding studies.** Sweller and Cooper (1985, five algebra experiments) and Cooper and Sweller (1987). The 1985 paper and its numbers could not be opened (a25, d17). The only figure we have, "about half the time and one fifth of the errors", is from Wikipedia and is unverified. Do not quote it. Cooper and Sweller (1987), described second-hand (a21): a group with one worked example paired to each problem had a shorter acquisition phase, fewer acquisition errors and better near and far transfer than a group with a few illustrative examples then conventional problems. Cooper and Sweller also separated two gains: schema acquisition helps similar problems, rule automation helps transfer to different problems, and worked examples help both (a26, snippet only).

**Zhu and Simon (1987).** The first large classroom programme, run in Beijing with about 13-year-olds (a01-a05). No control group in Experiment 1 (feasibility only). Later experiments had controls. Their production-system account (a06): pupils compare the unfactored and factored forms, notice what changed, and turn it into a condition-action rule, later split by sign cases. About five productions per pupil.

**Theory statement.** Sweller, van Merrienboer and Paas (1998, a07-a09): means-ends search loads working memory, an example removes the search, extraneous load falls, schema construction rises. The paper calls the prediction counterintuitive. It also lists costs: loss of motivation, stereotyped patterns that block creative solutions, and load from poor design. Completion problems (partial solution, learner finishes it) are the bridge between examples and problems.

**Self-explanation line.** Chi et al. (1989): good physics learners explain unexplained steps and monitor accurately. Renkl et al. (1998): a 15-minute training raised self-explanation by about 2 SD and improved transfer, mostly for low prior knowledge (a18). Atkinson, Derry, Renkl and Wortham (2000) is the main review of principles: subgoal labels, variability, sequencing, fading (a14-a20).

**The failed replications (1988-1990s).** Tarmizi and Sweller (1988), Experiment 3, circle geometry: worked-example pairs gave no gain on any measure and were slower on posttest time. The review quote: the guidance "not only failed to facilitate subsequent performance, it actually retarded learning" (a16). Experiments 4 and 5 integrated the text into the diagram and the effect returned. Ward and Sweller (1990) replicated this in physics (geometric optics). Sweller's own account (2023, a11, b04): the failure lasted several years in geometry and kinematics; the cause was split attention, because text refers to a diagram. Algebra needs no such lookup. This is the author's account of his own programme, given after the fact.

**Boundary theory.** Expertise reversal (Kalyuga, Chandler, Tuovinen and Sweller 2001) and element interactivity (Chen, Kalyuga and Sweller 2015-2017). The effect holds for high element interactivity and novices. For low interactivity or experts, problem solving is equal or better (a12, b05, b13). Sweller argues this means the early mixed results were theory failures, not replication failures. Critique: element interactivity can only be estimated (Chen et al. 2023), so the claim can look unfalsifiable if it is estimated after the result.

**Skill-stage model.** Anderson, Fincham and Douglass (1997), via a15: stage 1 solve by analogy to examples; stage 2 build declarative rules; stage 3 smooth procedural performance; stage 4 retrieve from many stored examples. Examples help most in stages 1 and 2. Stage 3 needs practice.

**Tutored problem solving (2007-2010).** Schwonke, Renkl, Aleven, Salden and colleagues tested examples against a strong control, an intelligent tutor with hints and feedback. Title of the 2009 paper: "not an artefact of lousy control conditions" (a24, d15). Result: similar learning in less time. Fading studies (Salden et al.) compared tutored problem solving, fixed fading and adaptive fading (b11, b12, d13, d14).

**Renkl (2014, a22).** An instructionally oriented theory of example-based learning, joining worked examples, observational learning and analogical reasoning. Hoogerheide and Roelle (2020, a23) summarise open issues: sequencing, long sequences, analogical comparison, learning from errors, individual differences.

**Meta-analysis (2023).** Barbieri et al.: g = 0.48 for math (b02, d11).

**LLM line (2022-2026).** Chain-of-thought exemplars (Wei et al. 2022) are the most direct LLM analogue. Then the many-shot, self-generated example and agent library work. Then, from 2025, reports that reasoning models are hurt by full solutions in context (d01, d03, d04).

## 3. Core findings with exact numbers

Status key: established = several independent sources, confirmed in opened text; single-source; contested; unverified = not opened.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Classroom factoring, school A: examples vs lecture control | 93.13% vs 75.50% post-test, p<.001, 32 pupils per condition, about 40 min each | Zhu and Simon 1987 (a02) | established as a result; one lab's own study |
| Same task, school B | 97.23% vs 95.08%, not significant; 39 vs 38 pupils; about 30 min | Zhu and Simon 1987 (a02) | ceiling null |
| Exponent laws, 1985 replication with control | example group 93.1, 95.4, 90.2 on three laws; mixed tasks 88 vs 73.1; time 180 vs 270 min; significant only for laws 2 and 3 | Zhu and Simon 1987 (a03) | per-group Ns not given |
| Geometry proofs, four schools | example means 76.9, 77.9, 89.1, 83.5%; school M 89.1 vs 85.2% (ns), skill reached 94.6 vs 88% (sig.), time 50 vs 75 min; school N 83.5 vs 83.2% (ns), time 50 vs 70 | Zhu and Simon 1987 (a04) | small, mostly ns on score; time saved |
| One-year retention (factoring) | example class 97.2 then 96.0; control 95.0 then 92.1 | Zhu and Simon 1987 (a05) | slight edge |
| "Three years of maths in two" | single class, no randomisation, authors hedge | Zhu and Simon 1987 (a05) | anecdote, do not cite as result |
| Sweller and Cooper 1985 founding numbers | not retrieved. "Half the time, one fifth the errors" is unverified (Wikipedia) | a25, d17 | unverified |
| Geometry examples with split text and diagram: no gain, slower posttest | Tarmizi and Sweller 1988 Exp 3, six problem pairs, three-item posttest; Exps 4-5 integrated format beat conventional and split | Atkinson et al. 2000 (a16) | established (failed then repaired); exact means not given |
| Pure worked condition: lower extraneous-load scores, better schema construction, higher transfer, better instructional efficiency | Paas and van Merrienboer 1994a, geometry; means not given in review | Sweller et al. 1998 (a08) | review-level |
| Variability helps only with worked examples | 4 groups, 6 lesson problems, six-item transfer post-test; no main effect of variability | Paas and van Merrienboer 1994 (a19) | single study |
| Alternating example-problem beats blocked | 6 pairs, three near-transfer items | Trafton and Reiser 1993 (a19) | single study; rival accounts |
| Subgoal labels: gain on 1 of 4 novel transfer items only | Catrambone and Holyoak 1990, six-item test | a17 | small |
| Self-explanation training | about 2 SD rise in self-explanation, reliable learning gain, near-transfer gain for low prior knowledge | Renkl et al. 1998 (a18) | single study |
| Meta-analysis, math worked examples | g = 0.48, p = 0.01; 43 articles, 55 studies, 181 effect sizes; 8,033 abstracts screened; RVE | Barbieri et al. 2023 (d11, b02) | single source; publication-bias tests unknown |
| Interim version of same analysis | g = 0.43, CI 0.31-0.55; 40 articles, 49 studies, 185 effects; range -1.80 to 4.66; 41 negative, 144 positive; I2 = 94.46%; no moderator significant | poster (b01) | same analysis, earlier; not an extra source |
| Meta-analysis moderators (published) | self-explanation prompts moderate negatively; correct-only examples beat incorrect-only or mixed; medium effect for both practice and initial acquisition | Barbieri 2023 (d11, b02) | fragile (poster found none significant) |
| Instructional explanations added to examples | 21 studies; minimal benefit overall; help conceptual more than procedural; not better than self-explaining | Wittwer and Renkl 2010 (d12) | abstract only |
| Tutored examples (8 studies, Cognitive Tutor) | efficiency gain in 5 of 8; conceptual transfer benefit in 1 of 4 tested; long-term retention benefit in 3 of 3 tested; standard tutor took 21% and 19% more time; examples never raised time or lowered any outcome | Salden et al. 2010 (d13) | review of own group's studies |
| Schwonke 2009 (two geometry tutor studies) | similar learning in less time; deeper conceptual understanding in Exp 2. Ns not retrieved | a24, d15 | abstract / second-hand |
| Adaptive fading vs fixed fading vs problem solving | order adaptive > fixed > problem solving in lab and classroom; classroom gain on delayed transfer only; Ns not retrieved | Salden et al. 2009/2010 (b11, d14) | contested |
| Fading with prompts beat full examples (grade 6 geometry) | N = 114, 3 days; fading largest pre-post effects; only prior knowledge moderated | a31 (2025) | single, abstract |
| Sequence x element interactivity | Exp 1: 52 Year-5 pupils; Exp 2: 96 Year-8 pupils. Example-first better for high interactivity; no difference for low | a29 (2020) | abstract only |
| Timing: problem solving better short-term for high-expectancy pupils, effect gone after 3 months; low-expectancy reversed | N not given | a32 (2019) | abstract only |
| Replication of self-explanation mediation | 115 students, six ill-defined statistics problems; indirect effect through self-explanation stronger for lower prior knowledge and working memory | a30 (2026) | replication that changed an earlier null |
| Counter-result: example-free instruction beat unexplained examples | n = 32, critical-thinking problems | a33 (2021) | tiny sample |
| Relevant vs irrelevant example domain (argumentation) | 142 psychology students; no loss from relevant domain | a28 (2024) | abstract only |
| CoT exemplars, PaLM 540B | GSM8K 17.9 to 56.9 (+39.0) | Wei et al. 2022 (c06) | established |
| CoT exemplars, text-davinci-002 | GSM8K 15.4 to 48.5 | Wang et al. 2023 (b16, c05) | established |
| Zero-shot CoT | MultiArith 17.7 to 78.7; GSM8K 10.4 to 40.7 | Kojima et al. 2022 (c07) | established |
| Random labels in demonstrations | cost 1.7 (multi-choice) and 2.6 (classification) points on average; 12 models; k = 16, 5 seeds | Min et al. 2022 (b17, c04) | single source; classification only. The "0 to 5" range was not re-found |
| Invalid-reasoning exemplars | GSM8K: standard 15.4, CoT 48.5, invalid 39.5 (about 81%), no coherence 23.1, no relevance 11.0. Bamboogle F1: CoT 45.2, invalid 39.4, no relevance 23.9 | Wang et al. 2023 (b16, b27) | single source, one old model |
| Many-shot, MATH500 | Reinforced ICL plateaus near 25 shots, about 5 points above human-solution ICL; human-solution ICL peaks near 125 then declines; unsupervised (problems only) matches or beats solutions; Minerva 4-shot 55.7 (MATH500), 90.6 (GSM8K) | Agarwal et al. 2024 (b18, c10, c11) | single model family |
| Many-shot GPQA | 198 test problems; 125-shot rationales beat zero-shot | Agarwal 2024 (b19) | noisy |
| Skill-matched examples help hard, hurt easy | GSM8K easy 96.3 fixed vs 83.2 skill-based (-13.1); Qwen2.5-1.5B MATH 57.2 (AdaptMI+) vs 53.0; gains up to 3.6 (AdaptMI) and 6 (AdaptMI+); iterative up to 7.2, 7B declines by loop 10 | He et al. 2025 (c01-c03) | single source, small models |
| Self-generated exemplars | GSM8K 5-shot CoT 75.0 vs 75.8-77.8 self-generated (GPT-3.5); davinci-003 retrieved 54 vs 61; curie about 2-3% for all; K=1 76.1 vs K=3-5 about 77-78 | Yasunaga et al. 2024 (c08, c09) | direction firm, cells garbled |
| Complex examples | +5.3 average, up to +18 points (GPT-3, Codex), part from voting | Fu et al. 2023 (c12) | old models |
| Retrieval can copy errors | unresolving error 46.9% (retrieval) vs 25.8% (random); up to 50% wrong demos little harm for Auto-CoT | Zhang et al. 2023 (c13) | MultiArith only |
| Reasoning models hurt by full CoT demos | AIME-2025: 1 demo cost about 6-16 points, 3 demos up to 35; GPQA Diamond: 1-5 and 4-8 points | From Harm to Help (d01) | measured; per-model values in plots only |
| Distilled insights fix the harm | AIME25 R1-Distill-7B 42.00 to 51.33; 14B 50.00 to 60.00; Qwen3-1.7B 35.96 to 42.65; GPQA 7B 51.26 to 55.16; 14B 59.50 to 63.03; GPT-4.1 AIME 34.0 to 48.0; one full demo about 6,142 CoT tokens vs target question 154.5 | d02 | text and table disagree slightly |
| Strong instruct models gain nothing beyond format | Qwen2.5-72B GSM8K 8-shot 95.75 vs zero-shot fixed 95.83; MATH 81.30 vs 81.64; base 72B GSM8K 90.52 vs 90.27 fixed; retrieval selectors at most +0.2; weak models (Llama3.2-1B, Llama2-7B) still gain | Cheng et al. 2025 (d03) | instruct models; ragged threshold |
| Direct beats CoT on pattern induction | direct better by 5.10 points (20.42% rel.) across nine datasets; R1 token cost about 2,432 vs about 190 for direct | Zheng et al. 2025 (d05) | pattern induction, not worked examples |
| DeepSeek-R1 says few-shot degrades | one sentence, no data | d04, c22 | vendor claim |
| Number of examples, classification | 168 runs; most models peak at about 5-20 relevance-selected examples then decline; some keep gaining | Tang et al. 2025 (d06) | classification only |
| Agent skill library | Voyager: diamond pickaxe 19 vs 36 iterations without library, 63 items vs baselines 3.3x fewer; random curriculum -93%, no self-verification -73% | Voyager (c14, c15) | 3 trials |
| Agent workflow memory | +24.6% Mind2Web, +51.1% WebArena; advantage grows from 8.9 to 14.0 points as train-test gap widens | AWM (c16) | abstract page only |
| Self-generated successful trajectories | ALFWorld 0.73 to 0.89 (0.93 curated); InterCode-SQL 0.75 / 0.79 / 0.82; Wordcraft 0.55 / 0.64 / 0.69; gpt-4o-mini; k = 6 (10 Wordcraft); beats upgrading to gpt-4o (0.88) | Sarukkai et al. 2025 (c17, d09) | five seeds |
| Memory gating | fixed / add-all / strict-add: RegAgent 67.53 / 55.48 / 70.95; EHRAgent 16.75 / 13.05 / 38.50; AgentDriver 40.11 / 32.32 / 51.00; CIC-IoT 71.50 / 59.90 / 85.40. History deletion: EHRAgent 42.06 vs 38.67 | Xiong et al. 2025 (d07, d08) | records are task outputs |
| ExpeL | insights from seed few-shot examples only gave no advantage over ReAct; HotpotQA ExpeL 39.0 vs ablations about 28-32 | c18 | table garbled |
| Buffer of Thoughts | +11% Game of 24, +20% Geometric Shapes, +51% Checkmate-in-One; 12% of multi-query cost | c19 | templates from same families |
| LLM-made help for students | N = 274: only ChatGPT group had gains above control; 32% of ChatGPT help failed quality checks (near 0% algebra, 13% statistics after self-consistency). Earlier N = 77: human hints better, about 70% passed checks | Pardos and Bhandari (c24, c25) | snippet; partial non-replication |
| AI tutor RCT with stored step solutions in the prompt | 194 analysed; post-test median 4.5 (n = 142) vs 3.5 (n = 174); 0.63 SD | Kestin et al. 2025 (d18) | not a worked-example manipulation |
| Simulated learner | passive study at least as good as active and constructive until about step 35; then they overtake (50 learners per condition, 20-node graph) | Procedural ABICAP (b14) | model with hand-set parameters |

## 4. Mechanisms and models

### 4.1 Load account (the standard theory)
- Working memory is small. Solving by means-ends analysis keeps goal, state and difference in mind. That is extraneous load for schema building.
- A worked example shows the states and operators. Load on the search drops. Spare capacity goes to schema building.
- Predictions: lower load ratings, faster study, better near transfer. The load measure itself is indirect in most studies (a10).
- Engineer's version: treat "load" as the tokens and structure the model must hold while producing the answer. For an LLM the analogue of search is long generation with no anchor. We have no evidence that this analogy is causal (K17).

### 4.2 Production rule induction (Zhu and Simon, a06)
A procedure to implement for a subgoal library:
1. Store pairs of states: before and after one step.
2. Compare them. Name what changed and what stayed.
3. Write a condition-action rule: IF pattern THEN operator.
4. When a later example shows a variation, split the rule by case (sign cases in algebra).
5. Present examples in an ordered sequence from simple to varied.
Entry shape: condition (pattern seen), action (step), cases, one verified instance.

### 4.3 Skill stages (a15)
Route by stage per skill:
- New skill: study solved cases (stage 1-2).
- Known skill, unsteady: pair a case with a try (stage 2-3).
- Familiar skill: just solve, practice (stage 3).
- Many stored cases: retrieve (stage 4).
Code needs a per-skill stage signal. Cheapest proxy: the recent pass rate on that problem class (the class record already exists in SCHEMA section 5).

### 4.4 Element interactivity and expertise reversal (a12, b05)
Rule: use a solved case when the step has many interacting parts and the learner is a novice at it. Skip it when the step is simple or already mastered. For the agent, estimate "interactivity" by number of dependent sub-steps and "expertise" by past pass rate. Both estimates are rough. See sibling subfields 01 and 04.

### 4.5 Split-attention format rule (a11, a16)
Keep each step next to the thing it refers to. In prompts: state the data, the diagram description or the code line inside the step, not in a separate block that the step points to. A badly formatted example can be worse than none (Tarmizi and Sweller 1988).

### 4.6 Fading and completion problems (a09, a20, b11, d14)
Schedule as code:
1. Full solution of subgoal type T.
2. Same type, last step blanked. The agent fills it. Code checks.
3. Same type, last two steps blanked.
4. Bare problem.
Move forward only when the check passes. Move back when it fails (adaptive). Human evidence: adaptive fading > fixed fading > problem solving in lab, partial in classroom (b11); fading beat full examples in one 2025 study (a31). Human gains from fading are mostly long-term retention and time, not transfer (d13).

### 4.7 Self-explanation (a18, a30)
Learners who explain why each step is taken learn more. The 2026 replication found the benefit runs partly through case-specific justification. But the meta-analysis found added prompts moderate the effect negatively (d11), and added instructional explanations have minimal benefit (d12). Net: contested. Implementation if tested: after reading a stored solution, the model writes one line per step naming why. Code compares the cost.

### 4.8 What examples do inside an LLM (analogy only)
- Format, label space and input distribution carry much of the gain (Min et al., b17).
- Relevance and order of steps matter more than step validity (Wang et al., b16): no relevance dropped GSM8K to 11.0, invalid steps kept 39.5.
- Strong models already have the skill. Examples add format only (d03, c11).
- Reasoning models treat a long demo as a trace to imitate or be anchored by. A 6,142-token demo against a 154-token question is a large load, and accuracy drops (d01, d02).
- Fix that worked: compress the demo to a short insight (d02).

### 4.9 Library maintenance as a mechanism
Admit only what passes a check. Score each entry by whether it helped. Retire entries by outcome history (d07-d09, c17, c14). Details in section 7.

## 5. What holds up

### Replications that worked
- Algebra examples beat problems in repeated experiments (Sweller and Cooper, Cooper and Sweller, Zhu and Simon school A). The effect is large in school A (93.1 vs 75.5).
- Efficiency gain in tutored settings: 5 of 8 studies, with the control spending 19-21% more time (d13).
- Long-term retention for fading: 3 of 3 studies that tested it (d13).
- Meta-analysis g = 0.48 over 55 studies, with correct-only examples best (d11).
- A 2026 replication of the self-explanation mechanism found mediation that the original missed (a30).

### Failures and nulls
- Geometry and kinematics for several years (a11, a16): no effect or negative with split text and diagram. Repaired by integration. The repair is credible because later integrated-format tests found the effect, but the account is the founder's.
- Zhu and Simon school B: 97.23 vs 95.08, ceiling, not significant.
- Zhu and Simon geometry: mostly not significant on score.
- Meta-analysis: 41 of 185 contrasts went the wrong way in the interim version; I2 = 94.46%; effects ranged -1.80 to 4.66 (b01). The mean hides wide spread.
- Moderator findings are fragile: the poster found no significant moderator, the paper found some (b21).
- Against a strong tutor, transfer benefit appeared in only 1 of 4 studies that tested it (d13). Reed et al. (2012), per a search snippet not opened, say the Experiment 1 transfer advantage did not replicate in Experiment 2 or in Schwonke 2011 (a24).
- Quilici and Mayer (1996): three examples per type did not beat one. Paas (1992): completion problems matched full examples (b09, b23; Wikipedia only, unverified).
- Pardos and Bhandari: the N = 77 study favoured human hints, the N = 274 study did not (c24, c25).
- Example-free instruction beat unexplained examples in n = 32 (a33).

### Moderators with support
- Prior knowledge / expertise (a12, a29, b13, a31). Established in direction. No pooled numbers.
- Element interactivity (a12, a29). Established in direction, hard to measure.
- Format: integrated vs split (a11, a16). Established.
- Correctness of examples: correct-only larger than mixed (d11).
- Sequence: example-then-problem better for novices on high-interactivity material (a29); alternating beat blocked (a19).
- Time of test: effects can flip with delay (a32).

### Interventions that worked
- Integrate text and diagram (a16).
- Pair each example with a matched problem (a21, b22: IES guide gave moderate evidence for interleaving).
- Subgoal labels or visual grouping: small, one transfer item of four in the founding study; later studies reported without numbers (a17).
- Completion problems as a bridge (a09).
- Adaptive fading (b11, d14, a31).

### Interventions that did not clearly work
- Added self-explanation prompts in the meta-analysis (negative moderator).
- Added instructional explanations (minimal).
- Letting the learner fail first, then showing the answer: still worse than study-only (Paas 1992, a08). Authors' explanation: the failed solution enters the schema.
- Fixed fading in the classroom (b11).
- Lecture-free instruction for example-free critical thinking: the n = 32 counter-result.

### Competing explanations
- Not load but time-on-task or motivation. Zhu and Simon note the control group sometimes spent more time (a02).
- Not a worked-example effect but a lousy-control artifact. Schwonke 2009 addressed this by using a tutored control and still found efficiency (a24).
- Not schema building but knowledge compilation (Trafton and Reiser's reading of the alternating result, a19).
- The author-run nature of most evidence: Sweller 2011, 2023 and the 1998 review are written by the theory's own authors (critique).

## 6. Language models

Reminder: all of this is analogy. No study tests the CLT effect in an LLM with matched load (K17, c29). The studies vary what stored solutions are shown.

### 6.1 Solved steps vs bare answers: big gains on older and weaker models
- PaLM 540B on GSM8K: 17.9 to 56.9 with CoT exemplars (+39.0) (c06). Emerges only at about 100B parameters.
- text-davinci-002 on GSM8K: 15.4 to 48.5 (b16).
- A phrase alone does a lot: zero-shot CoT, GSM8K 10.4 to 40.7, MultiArith 17.7 to 78.7 (c07).
- Elaborated multi-step examples beat simple ones by +5.3 on average (c12).

### 6.2 What inside the example matters
- Relevance and coherent order matter most. Without relevance GSM8K fell to 11.0; without coherence 23.1; with invalid steps 39.5 (about 81% of the 48.5) (b16).
- Random labels cost only 1.7 to 2.6 points on classification and multi-choice (b17).
- Wrong demonstrations are not free. Invalid steps cost about 9 points on GSM8K, and human data say correct-only examples are best (d11).
- Nearest-neighbour retrieval can import the same error: 46.9% unresolving errors vs 25.8% for random (c13).

### 6.3 Strength of the model changes the sign
- Weak and base models gain from exemplars (Llama3.2-1B, Llama2-7B, base Qwen72B GSM8K 84.69 to 90.52) (d03).
- Strong instruct models gain nothing: Qwen2.5-72B GSM8K 95.75 vs 95.83, MATH 81.30 vs 81.64. Retrieval selectors added at most 0.2 (d03).
- The threshold is ragged. Llama3.2-3B and Qwen2.5-1.5B do better zero-shot, so size alone does not decide (d03).
- Self-generated exemplars equal or beat retrieved ones only on strong models; curie stayed at about 2-3% (c09).
- Where the model lacks the skill (GPQA), rationales help consistently; where it has the skill (MATH), problems alone match solutions (b19, c11).

### 6.4 Reasoning models: full solutions hurt
- One retrieved full demo cost about 6-16 AIME-2025 points; three cost up to 35. GPQA Diamond: 1-5 and 4-8 (d01).
- A full demo is about 6,142 tokens; the target question 154.5 (d02).
- Same content as a short insight gave gains: R1-Distill-14B AIME 50.00 to 60.00; 7B 42.00 to 51.33; GPT-4.1 34.0 to 48.0 (d02). Gains on general reasoning sets were mixed and some variants fell below direct.
- DeepSeek-R1 authors: few-shot "consistently degrades" it. No data (d04).
- Pattern induction: direct beats CoT by 5.10 points across nine datasets; long-CoT reasoning models use about 12 times more total tokens (d05).
- Limits: only k = 1 and 3 tested; no matched example-vs-bare-problem control; the d02 text and table disagree for R1-Distill-7B (text +12.0 / +4.8, table +9.33 / +3.90).

### 6.5 How many examples
- MATH500 with human solutions: peak near 125 shots, then decline. Model-written solutions plateau near 25 without a drop (b18).
- Classification: 5-20 relevance-selected examples is the peak for most models; some keep gaining (d06).
- Analogical prompting: K = 1 gave 76.1, K = 3-5 about 77-78 (c09).
- Agents used k = 6 to 10 with no sweep (d09). No source sweeps k = 1, 2, 4 for a subgoal library.

### 6.6 Easy vs hard: the expertise reversal in a model
Skill-matched examples lifted hard questions by about +3 to +10 and lowered easy ones by about 5 to 13 (GSM8K easy 96.3 vs 83.2). Giving examples only after a failure recovered gains of up to 3.6 points (AdaptMI) and 6 (AdaptMI+) (c01, c02). Iterating the selection up to four times helped (up to 7.2 total); the 7B model declined by loop 10 (c03).

### 6.7 Agent libraries
- Voyager: diamond pickaxe 19 vs 36 iterations without the library; golden sword 18 vs 30; lava bucket 21 vs 27; compass 18 vs 26; no self-verification -73% items (c14, c15).
- AWM: +24.6% Mind2Web, +51.1% WebArena; the gap grows from 8.9 to 14.0 points as train-test distance grows (c16).
- Self-generated successful trajectories: ALFWorld 0.73 to 0.89, to 0.93 with curation. This beat a bigger model (gpt-4o fixed 0.88) (d09).
- Memory quality: add-all fell below a small fixed memory (EHRAgent 16.75 to 13.05); strict-checked adds reached 38.50 (d07). History-based deletion added a further 3.4 on EHRAgent (42.06 vs 38.67) (d08).
- ExpeL: insights taken only from the seed examples gave no advantage over ReAct (c18). New experience is what pays.
- Buffer of Thoughts: templates retrieved after distilling the problem (c19).
- Tool making: strong model writes, cheap model reuses (c20).

### 6.8 LLM-made worked examples for people
- N = 274: ChatGPT-help group gains above control, equal to human tutor help. 32% of generated help failed quality checks (c24). N = 77 earlier: humans better (c25).
- WorkedGen: about 400 students rated usefulness; no learning scores (c26).
- Kestin et al.: AI tutor 0.63 SD better than active learning (194 analysed), with step-by-step solutions in the prompt. Not a worked-example manipulation (d18).

### 6.9 Evidence quality warning
Most LLM numbers are from 2022 models. Only d01-d05 cover reasoning-class models, and several of those numbers come from plots. The Substack toy test (c23) is secondary and not used for any claim.

## 7. What our agent should take

Parts: G = guardrail, S = state, O = operator, memory = SCHEMA section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Take | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Subgoal library entries are verified only. Admit an entry only after a held-out or code check passes. Never add everything. | memory (subgoal library), G3 | [E] | K20: d07, d08, d09, d11, c14 |
| 2 | Entries hold the clean solved path, not the failure trail. | memory | [E] (human; weak) | a08 |
| 3 | Keep every step self-contained: the data or diagram description a step refers to is written inside the step. | memory, S2 format | [E] | K03: a11, a16, b04 |
| 4 | Do not inject examples by default. Gate by difficulty and prior success: show a stored case on a new, multi-part subgoal, or after the first attempt fails; skip it on routine items. | S0 gate, S3, memory | [E] for the direction (humans: a12, a29; LLMs: c01, c02, d03) | K04, K12, K19 |
| 5 | Reasoning-class models: store short distilled subgoal notes, not full traces. | memory | [E] | K18: d01, d02, d04 |
| 6 | Cap the number of retrieved cases. Start at small k (1 to 3, relevance-ranked). No whole-library dumps. | memory | [E] direction; best k unknown | d06, b18, c09 |
| 7 | Retrieve for relevance and step order first, correctness second, and also check correctness. | memory | [E] | b16, c13, d11 |
| 8 | Fill the library from the agent's own verified solves where possible, and refresh from new experience, not from the seed prompt. | memory, S9 | [E] | c17, d09, c18, c14 |
| 9 | Retire entries by outcome history (drop entries whose use led to poor results). Score each entry by whether it helped. | memory, S9 | [E] direction | d08, c17 |
| 10 | Log tokens and time, not only accuracy. The reliable human gain is efficiency, and a strong scaffold turns example gains into efficiency gains. | G7 | [E] | d13, a23, b10 |
| 11 | Limit fetch-try-check loops to about 4. | S5/S6 | [S] | c03 |
| 12 | Use a delayed or fresh-item check when judging the library, not only the immediate score. | G3, G7 | [E] (human) | a32, d13 |

Note on item 4: the gate rests on human expertise reversal (see subfield 04) and on three LLM sources. It does not give a threshold. The threshold comes from our own data, so the gate is a test target too (U1 in UNKNOWNS.md).

### Test first (single-source or contested)

| # | Candidate | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Example-after-failure vs example-first vs no example, at equal tokens | S0, S3, memory | [S] | K12: c01-c03; K19 |
| T2 | Explain-then-use: one line per step on a stored solution | S2, new operator | [C] | K06: a18, a30, b02, d11, d12 |
| T3 | Adaptive fading of stored solutions (blank last step, then more) | memory, S3 | [C] (human); no LLM test | K05: b11, d14, a31 |
| T4 | Completion problems as a library mode (partial solution, agent finishes) | memory | [S] human only | a09, a20, b09 |
| T5 | Distilled note vs full trace vs bare problem, by model class | memory | [S] | d01, d02 |
| T6 | k sweep 0, 1, 2, 4, 8 with relevance ranking | memory | [C] | K11, K21 |
| T7 | Self-generated analogous examples before solving, by model strength | S2/S3 | [S] | c08, c09 |
| T8 | Format-only stub vs full solution (how much is format) | memory | [S] | b17, c04, d03 |
| T9 | Corrupt correctness vs corrupt relevance in stored cases | memory | [S] | b16 |
| T10 | Diverse vs nearest retrieval | memory, G4 | [S] | c13 |
| T11 | Ordered sequence / alternating example-then-try vs batch | memory | [S] | a19, a29 |
| T12 | Subgoal labels (grouping) in stored solutions | memory | [S] small effect | a17 |

Placement reminders:
- Lessons stay shown after the first attempt (SCHEMA section 5). This fits the evidence for fixation on early exposure (a09) but conflicts with the human finding that examples first are better on high-interactivity items (a29). The conflict is a test target (T1).
- Section 4b lists "unstructured self-reflection" as not to add. Explain-then-use on a stored case is structured and different, but it must still pass its test.

## 8. Concrete tests on our bench

Arms are always at equal tokens (G7). If an arm uses more prompt tokens, give the other arms matching attempts or sampling budget. Report accuracy, tokens and attempts. Run at least 5 seeds and report the spread. Include one model weaker than the main model and one reasoning-class model, because the sign flips with model class (d01, d03).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Gate by failure | held-out problems from classes with a library, split easy/hard by plain pass rate | (a) no examples; (b) always inject 3 cases; (c) inject only after a failed first attempt | accuracy by easy/hard, tokens | (b) hurts easy items by several points; (c) matches or beats (a) on easy and beats it on hard. AdaptMI-sized: up to +3.6 to +6 on small models; none on strong ones |
| T2 Explain-then-use | procedural tasks with a check | stored case read as is vs plus one line "why this step" per step, tokens matched by giving the first arm extra samples | accuracy, tokens | small or none; meta-analysis suggests it may hurt. Add only if it wins |
| T3 Fading | repeated subgoal types, 4+ exposures each | full case each time; fixed fade; adaptive fade (blank last step if last attempt passed); bare problem | accuracy at exposure 4 and on fresh items; tokens | adaptive keeps accuracy at lower tokens; human effect is long-term retention, so measure on fresh items later |
| T4 Completion | same | full case vs partial case with last step blank vs bare | accuracy, tokens | partial equals full at fewer tokens (Paas 1992 pattern, unverified) |
| T5 Trace vs note | hard math (AIME-like), reasoning-class model, plus a non-reasoning model | no demo; 1 full trace; 1 distilled note; 3 notes | accuracy, tokens | full trace below no demo; notes above (d02: +9 to +10 on distilled models). Check the weaker model gets the opposite or smaller sign |
| T6 k sweep | subgoal library with relevance ranking | k = 0, 1, 2, 4, 8 | accuracy, tokens | peak at small k (1-4); decline past it, earlier for reasoning models |
| T7 Self-generated | same tasks | model writes 3 analogous solved problems first vs retrieved cases vs none | accuracy | helps strong model, not weak one (c09) |
| T8 Format-only | classification-like and multi-step items | full verified solution vs stub with right format and wrong content vs none | accuracy | stub keeps most of the gain on simple items (b17: 1.7 to 2.6 points cost) and loses more on multi-step items (b16) |
| T9 Corruption | multi-step math | clean; step values corrupted; relevance corrupted; order shuffled | accuracy | relevance and order corruption worse than value corruption (b16: 11.0 and 23.1 vs 39.5 against 48.5) |
| T10 Diversity | library with clusters | nearest 3 vs one per cluster | accuracy and error repeat rate | diverse lowers repeated errors (c13) |
| T11 Admission gate | repeated tasks over a stream | add all; add verified only; add verified plus outcome-based retirement | accuracy over the stream | verified beats add-all by many points; retirement adds a few (d07, d08: 38.50 vs 13.05; +3.4) |
| T12 Split attention | tasks with diagram or table referents | referent in a separate block vs inline in the step | accuracy | inline better when the step needs the referent; no change otherwise (a16) |
| T13 Order | high-difficulty items | case then try vs try then case | accuracy | case-first better on hard, no difference on easy (a29); conflict with "lessons after the first attempt" |
| T14 Delayed | same items 100+ items later | any library arm vs none | accuracy on fresh items | tests persistence; human timing effects can flip (a32) |

## 9. What does not transfer, and why

- **Working-memory load itself.** A language model has no working memory limit of the human kind. It has a context and attention budget. "Extraneous load" has no measured analogue. CoThinker uses CLT as a design lens, not a test (b20, c28). Do not cite it as support.
- **Novice vs expert as a person trait.** The model is not a novice in general. It is a novice per skill, and that varies unevenly (threshold ragged, d03). The agent must measure it per class from its own pass rate.
- **Self-explanation as an engine.** Humans generate inferences while explaining. A model asked to explain a step often writes plausible text (G10). The human benefit may not appear. Barbieri's negative moderator is also a warning.
- **Motivation and fixation by habit.** The stereotyped-pattern cost (a09) is about human creative blocking. LLM fixation is a separate effect (SCHEMA S3, F06).
- **Time on task.** Human tests control study time. LLM tests control tokens. The human efficiency finding maps to tokens only loosely.
- **Instructional explanations written by teachers.** Human learners read them. A model reads all text in the context equally. Extra explanation text costs tokens and may crowd out the task.
- **Classroom effects (school, teacher, homework).** Zhu and Simon's differences between schools are class-level, not item-level. No analogue.
- **Full-trace examples for reasoning models.** The human effect says "show the solved path". For o1/R1-class models, the measured result is the opposite for full traces (d01). The idea transfers only in compressed form (d02).
- **Randomised comparisons with strong baselines.** For strong instruct models there is nothing to gain over format (d03), which is the human ceiling null (school B) in another form.
- **Human-only moderators:** performance expectancies (a32), fluid intelligence, shifting ability (a30).

## 10. Open questions

1. Exact numbers for Sweller and Cooper (1985), Cooper and Sweller (1987), Schwonke et al. (2009) and Salden et al. (2009). All paywalled or blocked (d15-d17).
2. Publication bias in the Barbieri meta-analysis. Funnel, Egger and trim-and-fill tests could not be checked (d11). Crissman (2006) not found.
3. Does any matched-token LLM study put worked examples against bare problems with a transfer test? We found none (K17).
4. Where exactly is the model-strength crossover, per task difficulty? We have ragged points (d03, c01), not a curve.
5. Does k = 1, 2, 4 matter for a subgoal library? Untested (d01 used k = 1 and 3 only).
6. Does explain-then-use help LLM agents reading a stored solution? Untested. Own-voice explanations beat human ones in one abstract (d10); the human meta-analysis moderator is negative.
7. Is there an LLM analogue of adaptive fading? Not found. Only human results and the CoMeT tutor (b15), which measures behaviour, not learning.
8. Does the reasoning-model harm hold at larger k, other tasks, and newer models? One preprint, plots only (d01).
9. Do tests of learner gains from LLM-generated worked examples exist? Ratings only (c26) or a different manipulation (d18).
10. How much does solution correctness matter inside subgoal records, as opposed to task-output records? Xiong's records are task outputs (d07).
11. Can element interactivity be estimated in advance for agent subgoals, without circularity (a12 critique)?
12. Do effects persist? Human timing flips (a32); no LLM delayed test.
13. Task types without a fixed procedure: does the efficiency benefit survive (Nievelstein 2013, Rourke and Sweller 2009 are snippets only, b24, b25)? A 2024 argumentation study found relevant content did not hurt (a28).
14. Independence of the evidence. Most CLT sources are by the theory's authors (critique). Few independent replications with Ns.

## 11. Sources

[V] = opened this session or in the research run. [M] = snippet, abstract summary or second-hand only. Numbers from [M] sources are not used in claims unless flagged.

Founding and classic human studies
- [V] Zhu and Simon (1987) Learning mathematics from examples and by doing (tech report) https://kilthub.cmu.edu/articles/journal_contribution/Learning_mathematics_from_examples_and_by_doing/6616958/1 (a01-a06)
- [M] Sweller and Cooper (1985) https://doi.org/10.1207/s1532690xci0201_3 (a25, d17; not opened)
- [M] Cooper and Sweller (1987) https://doi.org/10.1037/0022-0663.79.4.347 (a26; snippet; described second-hand in a21)
- [V] Van Merrienboer and Paas (1990) https://ris.utwente.nl/ws/files/6709930/Merrienboer90automation.pdf (a21)
- [V] Sweller, van Merrienboer and Paas (1998) https://link.springer.com/article/10.1023/A:1022193728205 (a07-a10)
- [V] Atkinson, Derry, Renkl and Wortham (2000) https://doi.org/10.3102/00346543070002181 (a14-a20)
- [V] Sweller (2011) chapter https://www.emrahakman.com/wp-content/uploads/2024/10/Cognitive-Load-Sweller-2011.pdf (b07, b08)
- [V] Sweller (2023) The development of cognitive load theory https://link.springer.com/article/10.1007/s10648-023-09817-2 and https://d-nb.info/1312633387/34 (a11-a13, b04-b06, b13)
- [V] Renkl (2014) abstract https://pubmed.ncbi.nlm.nih.gov/24070563/ (a22)
- [V] Hoogerheide and Roelle (2020) editorial https://dspace.library.uu.nl/handle/1874/410634 (a23)
- [M] Rourke and Sweller (2009), Nievelstein et al. (2013), Quilici and Mayer (1996), Paas (1992), Pillay (1994) via Wikipedia https://en.wikipedia.org/wiki/Worked-example_effect (b09, b10, b23-b25; b09 and b10 are tertiary)

Tutored problem solving and fading
- [M] Schwonke et al. (2009) abstract page https://researchportal.hw.ac.uk/en/publications/the-worked-example-effect-not-an-artefact-of-lousy-control-condit/ (a24); article https://doi.org/10.1016/j.chb.2008.12.011 (d15, not opened)
- [V] Salden, Aleven, Schwonke, Renkl (2009) ISLS short paper https://repository.isls.org/bitstream/1/3215/1/119-120.pdf (b11, b12)
- [V] Salden et al. (2010) Instructional Science, abstract https://link.springer.com/article/10.1007/s11251-009-9107-8 (d14)
- [M] Salden et al. (2009) Topics in Cognitive Science https://doi.org/10.1111/j.1756-8765.2008.01011.x (d16, not opened)
- [V] Salden, Koedinger, Renkl, Aleven, McLaren (2010) review http://pact.cs.cmu.edu/pubs/SaldenEtAl-BeneficialEffectsWorkedExamplesinTutoredProbSolving-EdPsychRev2010.pdf (d13)

Meta-analyses
- [V] Barbieri et al. (2023) abstract https://link.springer.com/article/10.1007/s10648-023-09745-1 (d11, b03; full text paywalled)
- [V] Barbieri et al. interim poster https://www.cehd.udel.edu/wp-content/uploads/2022/02/Worked-Examples-Meta-Poster_022722_SC.pdf (b01, b21, b22)
- [M] Barbieri summary blog https://www.learningandthebrain.com/blog/using-worked-examples-in-mathematics-instruction-a-new-meta-analysis/ (b02)
- [V] Wittwer and Renkl (2010) abstract https://link.springer.com/article/10.1007/s10648-010-9136-5 (d12)

Recent human studies (abstract only)
- [V] Udvardi-Lakos et al. (2024) https://pubmed.ncbi.nlm.nih.gov/39377055/ (a28)
- [V] Element interactivity and sequences (2020) https://pubmed.ncbi.nlm.nih.gov/31465546/ (a29)
- [V] Self-explanation replication (2026) https://pubmed.ncbi.nlm.nih.gov/42171417/ (a30)
- [V] Working memory and fading (2025) https://pubmed.ncbi.nlm.nih.gov/40329570/ (a31)
- [V] Performance expectancies (2019) https://pubmed.ncbi.nlm.nih.gov/31496963/ (a32)
- [V] Example-free instruction (2021) https://pubmed.ncbi.nlm.nih.gov/34458621/ (a33)

Models of learning
- [V] Procedural ABICAP (2025) https://arxiv.org/pdf/2408.13364 (b14)

LLM and AI studies
- [V] Wei et al. (2022) https://arxiv.org/abs/2201.11903 (c06)
- [V] Kojima et al. (2022) https://arxiv.org/abs/2205.11916 (c07)
- [V] Min et al. (2022) https://arxiv.org/abs/2202.12837 (b17, c04)
- [V] Wang et al. (2023) Towards understanding CoT https://arxiv.org/abs/2212.10001 (b16, b27, c05)
- [V] Fu et al. (2023) https://arxiv.org/abs/2210.00720 (c12)
- [V] Zhang et al. (2023) Auto-CoT https://arxiv.org/abs/2210.03493 (c13)
- [V] Yasunaga et al. (2024) https://arxiv.org/abs/2310.01714 (c08, c09)
- [V] Agarwal et al. (2024) Many-shot ICL https://arxiv.org/abs/2404.11018 (b18, b19, c10, c11)
- [V] He et al. (2025) AdaptMI https://arxiv.org/abs/2505.00147 (c01-c03)
- [V] From Harm to Help (2025) https://arxiv.org/abs/2509.23196 and https://arxiv.org/html/2509.23196 (d01, d02)
- [V] Cheng et al. (2025) https://arxiv.org/html/2506.14641v3 (d03)
- [V] DeepSeek-AI (2025) DeepSeek-R1 https://arxiv.org/abs/2501.12948 (c22, d04)
- [V] Zheng et al. (2025) Curse of CoT https://arxiv.org/html/2504.05081 (d05)
- [V] Tang et al. (2025) Few-shot dilemma https://arxiv.org/html/2509.13196 (d06)
- [V] Xiong et al. (2025) memory management https://arxiv.org/html/2505.16067v2 (d07, d08)
- [V] Sarukkai et al. (2025) https://arxiv.org/abs/2505.00234 and https://arxiv.org/html/2505.00234 (c17, d09)
- [V] Zhao et al. (2024) in-context teachers (abstract) https://arxiv.org/abs/2311.06985 (d10)
- [V] Voyager https://arxiv.org/abs/2305.16291 (c14, c15)
- [V] Agent Workflow Memory (abstract page) https://arxiv.org/abs/2409.07429 (c16)
- [V] ExpeL https://arxiv.org/abs/2308.10144 (c18)
- [V] Buffer of Thoughts https://arxiv.org/abs/2406.04271 (c19)
- [V] LLMs as Tool Makers (abstract) https://arxiv.org/abs/2305.17126 (c20)
- [V] Reflexion https://arxiv.org/abs/2303.11366 (c21)
- [V] CoThinker https://arxiv.org/abs/2506.06843 (b20, c28)
- [V] CoMeT tutor (2026) https://arxiv.org/pdf/2609.22993 (b15, b26)
- [M] Pardos and Bhandari (2024) https://doi.org/10.1371/journal.pone.0304013 (c24); [V] preprint https://arxiv.org/abs/2302.06871 (c25)
- [M] WorkedGen https://dl.acm.org/doi/10.1145/3636243.3636252 (c26)
- [V] Hassany et al. (2024) abstract https://arxiv.org/abs/2402.16235 (c27)
- [V] Kestin et al. (2025) https://www.nature.com/articles/s41598-025-97652-6 (d18)
- [M] Substack toy test https://tnn1t1s.substack.com/p/few-shot-prompting-does-it-really (c23; not used for any claim)
- [V] Wikipedia, Worked-example effect https://en.wikipedia.org/wiki/Worked-example_effect (b09, b10; tertiary, pointer list only)
