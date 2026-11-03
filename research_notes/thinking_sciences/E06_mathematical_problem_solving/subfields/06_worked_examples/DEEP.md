# Worked examples: deep document

*Subfield E06.06. Focus: study before solving (Sweller; Renkl). Why it matters for our agent: the subgoal library. Built from evidence_a-d.jsonl (ids a01-a30, b01-b26, c01-c25, d01-d19), claims.jsonl (K01-K30) and critique.md in this folder. Honest limit up front: the founding human papers (Sweller and Cooper 1985, Cooper and Sweller 1987, Ward and Sweller 1990, Chi 1989, Kalyuga 2001, Renkl/Atkinson fading) were NOT opened. Their numbers are second-hand or absent. The Barbieri 2023 meta-analysis was seen as abstract only. Almost every LLM study is 2022-2024 prompting on older models. No study tests a subgoal library with a frontier reasoning model at equal tokens.*

## 1. What it is

A worked example is a fully solved problem: the problem, every solution step, and the answer. The worked-example effect says that novices learn more from studying such solutions than from solving the same problems themselves. It was first reported by Sweller and Cooper (1985) in algebra [a01, a25].

Why it works, in the standard account (Sweller, van Merrienboer, Paas 2019 [a01-a05]):
- Solving an unfamiliar problem by means-ends analysis is costly. The learner holds the current state, goal state, their differences, operators and sub-goals at once. This uses working memory but builds little long-term schema [a03].
- A worked example removes the search. Attention goes to problem states and operators, so the learner can induce a general solution [a01].
- Working memory is limited only for novel information. Long-term memory holds schemas that lift that limit (de Groot, chess) [a02].

Renkl's account (2017) adds a second route: learners relate principles to several cases and build an interconnected structure that supports transfer [a24].

Four neighbouring terms used below:
- **Example-problem pair**: a worked example followed by a similar problem to solve.
- **Completion problem / fading**: an example with some steps blanked; blanks grow over time (van Merrienboer 1987; Renkl, Atkinson) [a05, a29].
- **Self-explanation**: the learner explains each step to themselves (Chi 1989) [a28]. Sibling subfield: Self-explanation.
- **Subgoal labelling**: each step group is given a named purpose (Catrambone; Margulieux; Morrison) [b15, b16].

For an LLM, the plain translation is: a few-shot exemplar block is a worked example. Chain of thought (Wei 2022) is exactly "eight worked examples in context" [c01]. A subgoal library is a store of solved cases with their subgoal structure, retrieved and shown to the model.

Honest caution: the human theory is about a limited working memory and schema acquisition. An LLM has neither. The transfer is by analogy of function, not mechanism. The LLM literature (Section 6) is therefore the real evidence for the agent. The human literature supplies hypotheses and boundary conditions.

## 2. History and theories in depth

**1982: goal-free effect.** Sweller and colleagues show that removing the specific goal (so no means-ends analysis) helps learning. It is the oldest cognitive-load-theory effect [a03].

**1985: Sweller and Cooper.** Five algebra experiments. Hypothesis: conventional search retards schema acquisition. Learners who studied example-problem pairs did better on later problems than those who solved all problems. A secondary note says that in Experiment 5 the study groups took about half the time and made one fifth of the errors on similar problems. That figure is unverified. The effect did not seem to extend to problems that varied on the posttest [a25]. Status: not opened.

**1987: Cooper and Sweller.** Examples help through schema acquisition and rule automation; far transfer needs schema acquisition [a26]. Not opened. Same year: van Merrienboer proposes completion problems for programming [a05].

**1989: Chi, Bassok, Lewis, Reimann, Glaser.** Better physics solvers explain examples more actively to themselves (inferences, links to prior knowledge, monitoring) [a28]. Observational, not causal. The causal step came later through prompted self-explanation. Not opened.

**1990: Ward and Sweller.** Boundary: under some conditions examples are no better, perhaps worse, than solving. They must be structured to avoid split attention [a27]. Not opened. Split attention: a diagram with separate text forces mental integration; integrating them restores the effect (Tarmizi and Sweller 1988; Chandler and Sweller 1992) [a07].

**1994: Nathan, Mertz, Ryan.** Extension with self-explanation in algebra: n=32, 2x2 (self-explanation x load), 1 to 2 week delay. On story-problem translation, self-explanation main effect F(1,25)=5.9, p<.025; load main effect F(1,25)=6.76, p<.02; interaction F(1,25)=7.1, p<.02. On the procedural task, effects were not significant (interaction t(25)=1.7, p=.1). Non-explainers showed the Sweller and Cooper pattern, but the high-vs-low load gap was not significant after the delay [a10, a11]. The authors also set out two rival accounts of why examples work: learning at study time (self-explanation fills gaps, VanLehn and Jones 1993) versus learning later during knowledge compilation [a12].

**1998 to 2010: cognitive load theory matures.** The 1998 paper listed seven effects, most due to extraneous load; the variability effect is the exception (intrinsic load). Germane load was redefined later. Sweller (2010) unified intrinsic and extraneous load under element interactivity [a04, a23]. The three-load model is contested; see sibling subfield "Critiques of the three-load model".

**2000 to 2003: expertise reversal.** Kalyuga, Chandler, Tuovinen, Sweller (2001; three studies in mechanical diagrams, relay circuits and programming logic per a secondary page): as learners gain knowledge, studying examples becomes worse than solving problems. Exp 3 used 42 Year 9 students in coordinate geometry (via He-Yueya 2024) [a13, a30]. Not opened. Sibling subfield: Expert flexibility and adaptive expertise.

**2002 to 2003: fading.** Renkl, Atkinson, Maier, Staley; Atkinson, Renkl, Merrill. Fading steps out of examples improved near transfer over example-problem pairs; far transfer was not reliable (snippets only) [a29].

**2011: van Gog, Kester, Paas.** Electrical circuit troubleshooting: worked-example-only and example-problem pairs beat problem-example pairs and pure problem solving, with lower mental effort [a13]. (Second hand via Wikipedia.)

**2015 to 2017: element interactivity as moderator.** Chen, Kalyuga, Sweller: a worked-example effect for high element interactivity maths, and a reverse effect (generating beats studying) for low-interactivity material [a06].

**2015: classroom trial (Booth et al.).** Randomised algebra homework trial, 380 students in 25 classrooms (189 vs 191). Means intervention vs comparison: state-test items 0.49 vs 0.48 (improvement index 15); conceptual 0.51 vs 0.49 (index 11); procedural 0.25 vs 0.25 (index 10). Rated "meets standards with reservations". Means are nearly equal while the index is large [b19]. Developer page (AlgebraByExample): +10 points conceptual for struggling students over a year, +4 procedural while solving half as many problems, +7 on released state items; no effect sizes, no null results listed [b20].

**2019: Sweller, van Merrienboer, Paas review.** Calls the evidence very strong; names expertise reversal and element interactivity as the main boundaries [a01, a05].

**2021 to 2022: the rival, problem solving before instruction (productive failure).** Sinha and Kapur (2021): 53 studies, 166 comparisons, Hedges g 0.36 (95% CI 0.20 to 0.51); higher design fidelity g 0.37 to 0.58; after publication-bias adjustment g 0.87 (as reported by Kapur et al. 2022). Younger learners (grades 2-5) and domain-general skills favoured instruction first (search summary only, unverified). The comparison group is "traditional instruction", not worked examples. No head-to-head experiment was found [b21, b22, b26].

**2023: Barbieri, Miller-Cotto, Clerjuste, Chawla meta-analysis.** Maths only. 8033 abstracts screened; 43 articles, 55 studies, 181 effect sizes; robust variance estimation; average g = 0.48 (p = 0.01), medium. Moderators: correct examples alone gave larger effects than incorrect alone or correct plus incorrect; self-explanation prompts moderated the effect negatively; timing (practice vs skill acquisition) tested. Per-moderator g not read [a08, a09, d17].

**2024: Lechner et al.** Biology observation training, N=62, three groups. Worked-example videos improved application of knowledge (F(2,57)=13.26, p<.001, eta2=.32); faded examples gave no extra advantage; ceiling pretest scores [a14].

**2022 onward: the LLM line.** Wei 2022 (chain of thought as worked examples), Min 2022, Wang 2023, Fu 2022, Zhou 2022/2023, Didolkar 2024, Skills-in-Context 2024, Yasunaga 2024, Chen 2024, Gwak 2026, Cheng 2026, Notes to Self 2026. See Section 6. Links to other subfields: Chain-of-thought prompting; Analogical problem solving; Intelligent tutoring and knowledge tracing; Expertise as chunking.

## 3. Core findings with exact numbers

Status key: established (two or more independent sources), single-source, contested, human-only (no LLM test), older-models-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Worked examples beat solving for novices in maths | pooled g = 0.48; 43 articles, 55 studies, 181 effects | Barbieri 2023 [a08] | established (abstract only read) |
| Origin of effect | algebra, 5 experiments; Exp 5 half the time, one fifth the errors (unverified) | Sweller and Cooper 1985 [a25] | human-only, not opened |
| Classroom RCT, algebra homework | 380 students, 25 classes; means .49 vs .48, .51 vs .49, .25 vs .25; improvement index 15, 11, 10 | WWC on Booth et al. [b19] | single-source; small |
| Correct examples beat incorrect or mixed | direction only; per-g not read | Barbieri 2023 [a09] | established with LLM side (K06) |
| Self-explanation prompts add nothing in the maths pooled data | negative moderator | Barbieri 2023 [a09] | contested |
| Self-explanation on translation tasks | n=32; F(1,25)=5.9, p<.025; interaction F(1,25)=7.1 | Nathan 1994 [a10] | single small study; wash-out at delay [a11] |
| LLM-supported open self-explanation, calculus | N=92; transfer explanation quality +11.9 pts (p=.030); overall posttest no effect | 2026 study [c16] | single-source |
| Element interactivity moderates | worked-example effect on high interactivity maths; reverse on low | Chen, Kalyuga, Sweller [a06] | direction only |
| Expertise reversal | example advantage shrinks or reverses with knowledge | Kalyuga 2001 etc. [a05, a30] | human established by reviews; not opened; LLM contested |
| Fading vs example-problem pairs | better near transfer; far transfer unreliable; 2024 trial N=62 no fading gain | Renkl/Atkinson [a29]; Lechner [a14] | contested |
| Productive failure rival | g = 0.36 [0.20, 0.51], 53 studies, 166 comparisons; bias-adjusted 0.87 | Sinha and Kapur 2021 via b21 | contested |
| Primary school maths | no score or load difference; less study time | van Loon-Hillen et al. [b24] | snippet only |
| CoT = worked examples in context | PaLM 540B GSM8K 17.9 to 56.9 (+39.0), 8 exemplars | Wei 2022 [c01] | established, older model |
| Random labels barely hurt (classification) | drop 0-5 pts over 12 models; 1.7 avg multi-choice, 2.6 classification | Min 2022 [c02] | single-source, no maths |
| Invalid reasoning in exemplars keeps most gain | text-davinci-002 GSM8K: standard 15.4, valid CoT 48.5, invalid 39.5, no coherence 23.1, no relevance 11.0 | Wang 2023 [c03, c22] | established |
| Wrong equations keep most gain | PaLM-62B GSM8K: direct 10.11, CoT 27.37, wrong equations 24.39 | Madaan 2022 [d06] | older models |
| Systematic errors in all examples destroy accuracy | addition accuracy near 0% | Zhou 2022 [b08] | established with Wang |
| Explicit algorithm examples generalise to longer inputs | addition length 19: 90.5 vs 9.5; subtraction 14: 65.6 vs 16.7; multiplication 7: 79.7 vs 5.5; parity 20: 95.0 vs 50.0 | Zhou 2022 [b07] | single-source |
| Complex (more-step) examples beat random | Codex GSM8K 66.6 vs handcrafted 61.0 (+5.6); davinci-002 55.4 vs 48.1 (+7.3) | Fu 2022 [b01] | single-source |
| Selection method comparison | GSM8K random/centroid/retrieval/complexity 52.5/52.0/56.0/58.5; MathQA 33.0/32.0/69.5/42.5 | Fu 2022 [b02] | retrieval wins only on near-duplicates |
| Subproblem decomposition in the demo | SCAN length 99.7 vs about 16; GSM8K 62.39 vs 60.87; 5+ steps 45.23 vs 39.07; 2 steps 74.53 vs 76.68 (CoT better) | Zhou 2023 [b04] | established with c13 |
| Skill-matched exemplars | MATH GPT-4: CoT 42.2, Complex 50.30, Topic 50.31, Skill 53.88; GSM8K 93.00 to 94.31 | Didolkar 2024 [b10, b11] | single-source |
| Skills plus grounded examples in one prompt | DP task ChatGPT: CoT 72.0, SKiC 98.0, no skill text 94.0, no grounding 82.0; GSM8K 73.0-74.4 vs 86.9-87.8 | Chen 2024 [b12] | established |
| Subgoal demos with prover check | miniF2F-test 38.9 to 45.5; minus subgoal 40.6; minus both 38.5 | Zhao 2023 [d04, d05] | single-source, formal proofs |
| Subgoal labels in CS1 (human) | N=307; quizzes medium effect, exams small; at-risk exam avg 74% vs 67% | Morrison et al. talk [b15] | single-source; slides only |
| Structure retrieval beats wording retrieval | k=8 six sets: 0.5B 18.6/27.6/34.3 (random/semantic/graph); 8B 59.7/66.2/68.8; 70B 66.3/72.8/74.4 | graph retrieval 2024 [c09] | single-source |
| Similarity-chosen self-made demos repeat mistakes | unresolved 46.9% (retrieval) vs 25.8% (random); zero-shot errors 128/600 = 21.3% | Auto-CoT [b05, d10] | older model |
| Self-made relevant exemplars | GSM8K 75.0 to 77.8; PaLM2 60.8 to 81.7 (Yasunaga); but relevant 71.5 vs N/A 75.5 (Chen) | [c06, c07] | contested |
| Generate-and-solve in one turn beats reuse | GPT-4o GSM8K zero 49.89, integrated 54.59, decoupled 50.49, repeat 52.16 | Gwak 2026 [c05, c23] | single-source, not re-verified |
| One demo can hurt | one-shot failed on 1.83 to 34.96% of problems solved zero-shot; rejection rule helps | Liu 2025 [c08, c24] | single-source |
| Strong instruct models gain nothing from exemplars beyond format | Qwen2.5-72B-Instruct GSM8K 8-shot 95.75 vs zero-shot 95.83; MATH 81.30 vs 81.64 | Cheng 2026 [d01] | contested |
| Gain depends on item mastery | pass@1 change +6.31 (0-50%), +2.46 (50-100%), -2.32 (100%) | Notes to Self 2026 [d14] | single-source, 3B |
| Experience-note libraries are model dependent | Llama-3.2-3B 43.11 to 46.42; Qwen-1.5B 50.23 to 49.14; gemma-2-2B 21.77 to 13.75 | Notes to Self [d13, d15] | contested |
| Template library on a task with a clear algorithm | Game of 24 GPT-4: CoT 11.0, BoT 82.4 (ToT 74.0) | Buffer of Thoughts [c15] | single-source |
| LLM-written worked help is less reliable | 70% passed checks (a22); tutoring dialogs 56.6% fully correct (c12) | Pardos 2023; Gupta 2025 | established |
| Process-rich worked solutions for fine-tuning | AIME 2024: base 6.66, 100 process solutions 18.89, 1000 standard 5.56 | REL 2024 [a17] | single-source; 30 items |
| Correct-then-store records for fine-tuning | LLaMA-2-70B GSM8K 81.4 to 83.5; MATH 23.6 to 25.0 | LEMA 2024 [d12] | single-source |

## 4. Mechanisms and models

Each mechanism is stated so it can be built.

**4.1 Load model (human).** Total load = intrinsic (element interactivity of the material, relative to the learner's schemas) + extraneous (set by the instruction). Examples cut extraneous load from search. Rule: show a full example when the learner has no schema for the type; when schemas exist, interactivity is low and the example becomes redundant [a04, a05, a23]. LLM analogue: no direct measure of "load". The best proxy found is per-item self-accuracy (Notes to Self): hints helped items solved under 50% of the time and hurt fully solved ones [d14].

**4.2 Schema induction through variation.** Examples must differ in surface while keeping structure; the learner extracts what changes and what stays. This is the same move as schema S2 "study every example". Engineering form: store 2 to 3 examples per class that differ in surface features and share a subgoal list; show them together. (This is our design reading; not directly tested in the LLM papers.)

**4.3 Subgoal labelling.** Group solution steps under named purposes. Human data: medium effect on quizzes, small on exams; arrangement mattered (given labels with a far gap, or self-written labels with a near gap) [b15, b16]. LLM analogue: Zhao 2023 subgoal-numbered proofs +4.9 to +5.8 points with a verifier [d05]. Least-to-most shows the decomposition in the demo [b04]. Implementation: every library entry is {problem class, subgoal list (names), per-subgoal step text, answer, code check}.

**4.4 Fading.** Sequence: full example, then example with 1 blank, then more blanks, then full problem. Human result: better near transfer, far transfer unreliable [a29]. Controller design for the agent: fade driven by code-checked success on that class (no human equivalent; untested, see UNKNOWNS).

**4.5 Skill-indexed retrieval.** Didolkar: a strong model labels each training problem with one skill; labels are clustered to 22 (GSM8K) or 117 (MATH); at test time the model names the skill needed, and exemplars carrying that skill are shown. Gain +3.5 over topic matching on MATH with GPT-4, +1.3 on near-ceiling GSM8K [b10, b11, c10]. Skills-in-Context shows the skill definitions and the examples must share a prompt [b12].

**4.6 Retrieval by structure, diversity and complexity.**
- Pick by step count when difficulty is known (Fu): longer chains win mainly on multi-step items; on easy items simpler ones do as well [b01, b03].
- Retrieve by solution structure rather than wording (computational-graph retrieval; gap to semantic shrinks with model size, +6.7 to +1.6) [c09].
- Pure similarity retrieval is only the best choice when the test set nearly duplicates the library (MathQA 69.5 vs 42.5) [b02].
- Mix in diversity: Auto-CoT clusters, one demo per cluster, and tolerated up to 50% wrong demos on MultiArith; in-cluster sampling did not [b06, d11].

**4.7 Gate and rejection.** Liu 2025: score demos by semantic similarity and model stability; fall back to zero-shot when the best demo is not in the top slice (about top 10%, lambda within 10%). Without rejection, accuracy sometimes fell below zero-shot [c08, c24]. Implementation: if retrieval similarity is below a threshold, show nothing.

**4.8 Generate-and-solve (self-generation).** Prompt: "recall relevant problems, solve each, then solve the target." Gwak found the gain comes from creating and solving inside the same turn; reusing the same text as a plain demo gave almost nothing [c05, c23]. Yasunaga found self-made exemplars beat hand-written few-shot on large models [c06]. Chen found relevance made no difference but correctness did [c07]. Treat as contested.

**4.9 Admission control (verify before storing).** LLM-written examples are often wrong: 70% passed checks; dialogs 56.6% fully correct [a22, c12]. Answer-only filters (STaR, OpenMathInstruct) keep right-answer-wrong-reasoning solutions, and models copy the reference answer when shown it [d08, d09, d16]. Proposed admission rule: (1) code reproduces the answer from a masked statement; (2) re-derivation from the stored subgoals gives the same answer; (3) log the rejection rate. Not tested.

**4.10 Format versus content split.** Part of an exemplar's effect is format: step pattern, readable text, which symbols to copy [d06, d07, c02]. Solution content (valid reasoning) matters less for prompting than for training, except systematic errors [b08]. Test with a format-only stub.

**4.11 Correct-then-store (training side).** Record: wrong attempt, error step, fix. LEMA: +2.1 GSM8K and +1.4 MATH on LLaMA-2-70B; REL: process traces 18.89 vs 5.56 [d12, a17]. These are fine-tuning results. For an agent that does not train, the analogue is storing repair traces in the library (untested).

## 5. What holds up

**Holds up (human).**
- Pooled benefit for novices in maths, g = 0.48 across 55 studies [a08]. Caveat: abstract only.
- Expertise boundary: the reviews treat it as well replicated, but first-hand numbers were not seen [a05, a13, a30].
- Element interactivity as a moderator, direction only [a06].
- Correct examples beat incorrect or mixed [a09].

**Weaker or failed.**
- Self-explanation prompts: negative moderator in the maths meta-analysis [a09]. Nathan 1994 effect on translation did not carry to the procedural task and washed out at delay [a10, a11]. The 2026 calculus study found a gain on explanation quality but not on overall posttest, and explainers solved fewer practice problems [c16].
- Fading: near transfer yes, far transfer unreliable; the 2024 N=62 trial found no extra gain (ceiling pretest) [a14, a29].
- Delay: the example advantage can wash out (Nathan) and may be absent in primary school or ill-structured settings (van Loon-Hillen: no score difference, less time) [a11, b24].
- Classroom trial: tiny mean differences (0.49 vs 0.48) with a large improvement index. Check before citing as large [b19].
- Developer claims (SERP) lack effect sizes and null results [b20].
- Productive failure (g = 0.36) is a live rival; moderators unverified [b21, b22].

**Holds up (LLM).**
- Relevance and coherent order matter more than validity [c03, c22].
- Systematic errors hurt; random errors are tolerated [b08, c03] (K06).
- Complexity helps on multi-step items, little on easy ones [b01, b03, a19].
- Decomposition in the demo helps most where length generalisation is needed [b04].
- Similarity retrieval repeats errors, and wins mainly on near-duplicates [b02, b05].
- LLM-authored worked help needs verification [a22, c12].

**Moderators that flip results.**
- Model strength: instruct models at 72B scale and R1-style reasoning models show no gain or a loss from exemplars [d01, d02, d03]. Base and weaker models still gain (Qwen2.5-72B-Base GSM8K 8-shot 90.52 vs zero-shot 84.69 [d01]). Small models gain more from skill-matched examples [b11] and structure retrieval [c09].
- Item mastery: hints help items failed often, hurt items always solved [d14].
- Model family: Llama up, Qwen and Gemma down for the same note library; Gemma lost even with a blank template [d13, d15].
- Task type: Game of 24 and algorithm tasks gain hugely from templates [c15, b07]. GSM8K on near-ceiling models gains about 1 point [b11].

**Interventions that did not work.**
- Self-explanation prompt on top of examples (maths pooled) [a09].
- Fixed 8-shot retrieval variants against zero-shot on strong models [d02].
- Few-shot for R1 [d03].
- Retrieval with rejection switched off: below zero-shot at times [c24].
- Putting an addition algorithm example in context as a tool cost 12.9 points of logic accuracy through interference, though addition rose 61.9 to 98.4 [b09].

**Unreplicated or unverified.** Gwak 2026 (could not be re-found); Buffer of Thoughts (not re-verified); Barbieri moderators; Sinha and Kapur moderators. Notes to Self numbers were re-opened and confirmed.

## 6. Language models

**Few-shot exemplars as worked examples (2022).**
- Wei 2022: PaLM 540B GSM8K 17.9 to 56.9 (+39.0) with eight exemplars. Gain largest on hard sets; SingleOp showed negative or tiny gains. Emerges only above about 100B parameters [c01, a19].
- Min 2022: random labels cost 0 to 5 points across 12 models on classification [c02].
- Wang 2023: invalid steps kept 39.5 of 48.5 (81% of the answer-accuracy gain); the "over 90%" figure applies to intrinsic recall (39.8 vs 43.9), a different metric. No relevance dropped GSM8K to 11.0, below the 15.4 baseline; no coherence 23.1 [c03, c22; critique item 3].
- Madaan 2022: wrong equations 24.39 vs 27.37 on PaLM-62B; no-pattern prompts fall to direct level; concise CoT with 20%+ fewer tokens matched full CoT [d06].
- Fu 2022: complexity selection raises GSM8K by +5.6 (Codex) and +7.3 (davinci-002) [b01].
- Zhou 2022: explicit algorithm examples; systematic errors to near 0% [b07, b08]. Shi 2023: exemplars containing irrelevant sentences improved robustness (macro accuracy 6.0 to 14.0 on code-davinci-002) [b14].
- Least-to-most: 99.7 vs about 16 on SCAN length; weaker at 2 steps [b04].
- Auto-CoT: diverse self-made chains matched manual (MultiArith 92.0 vs 91.7; GSM8K 47.9 vs 46.9) [b05].

**Example selection (2022-2025).**
- Skill-matched: MATH 53.88 vs 50.31 (topic) and 42.2 (CoT), GPT-4 [b10]. GSM8K 93.00 to 94.31 [b11].
- Skills-in-Context: DP 98.0 vs 72.0 [b12]. A GSM8K prompt applied to MATH gained only +3.1 (28.2 to 31.34) [b13].
- Graph retrieval [c09]. Liu 2025: one-shot LMS3 raised Llama2-13B GSM8K 0.414 to 0.447 and Llama3-8B 0.820 to 0.837, but GPT-4 MATH was 0.758 zero-shot vs 0.752 [c08].
- Self-generation: Yasunaga +2.8 GSM8K (GPT-3.5) and +20.9 (PaLM2 60.8 to 81.7) [c06]. Chen: relevant 71.5 vs unrelated 75.5 [c07]. Gwak: integrated beats decoupled [c05].

**Subgoals with a verifier.** Zhao 2023: +4.9 (with organiser) and +5.8 (without) miniF2F-test points from subgoal-formatted demos; reaches the old best with 20 calls instead of 100 [d04, d05].

**Modern strong models (2025-2026).** Cheng 2026: Qwen2.5-72B-Instruct 8-shot equals zero-shot once the answer extractor is fixed (95.75 vs 95.83; 81.30 vs 81.64). Zero-shot first scored 91.58 only because of answer formatting, so exemplars were buying format. Retrieval variants mostly fell below zero-shot on MATH; the best was +0.2 for complexity retrieval at 4 or 6 shots on GSM8K [d01, d02]. DeepSeek-R1: few-shot consistently lowers accuracy; no numbers [d03]. No test exists on frontier closed reasoning models at equal total tokens.

**Notes and templates libraries.** Notes to Self (small models): Llama 43.11/70.57 to 46.42/72.80 (pass@1/pass@8); Qwen 50.23/76.47 to 49.14/75.09; gemma-2-2B 21.77 to 13.08 with a blank template and 13.75 with notes; Phi-3.5-mini 40.62 to 43.60 [d13, d15]. Bucket effects in Section 3 [d14]. Buffer of Thoughts: Game of 24 82.4 vs CoT 11.0, but MGSM 84.4 vs 89.2 shows gains depend on the task [c15].

**Reliability of LLM-authored examples.** 70% of ChatGPT hints passed checks. Human hints raised pre-post scores in both lessons (gains 24.63 and 23.65 points); ChatGPT hints raised only the Elementary lesson (11.14) and not Intermediate (1.7, pretest ceiling confound) [a22]. Tutoring dialogs: 90% high quality but only 56.6% fully correct [c12]. LLM Java explanations: high correctness, lower completeness (search summary) [c20].

**Training with worked solutions.** REL, LEMA, OpenMathInstruct, STaR (GSM8K GPT-J few-shot CoT 3.1 to 10.1 with filtering) [a17, d12, d08, d16]. These show process-rich and corrected worked solutions are worth more than clean ones for training. They are outside the agent's prompting scope.

**Simulation.** GPT-3.5 personas reproduced expertise reversal and the variability effect on 120 simulated students. These are judgments, not learning [a15]. LLM-as-simulated-learner is weak evidence.

**TutorGym.** LLM agents given tutor feedback in context produced error curves similar in shape to human learning curves (qualitative); the authors think examples teach interface order [c11].

## 7. What our agent should take

Part codes: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Library entries must be verified by code before admission; log the rejection rate. LLM-written solutions fail often. | G5 / M | [E] | a22, c12, b08, c03, K06, K20 |
| A2 | Retrieve library entries by relevance to this item's structure and keep step order and bridging objects intact. Irrelevant exemplars are worse than none. | M | [E] | c22, c03, b05, b02, c09, K07, K13 |
| A3 | Store each entry as an explicit subgoal list with unambiguous step text, not a vague summary. | M / O3 | [E] | b04, c13, b07, b12, K10, K14 |
| A4 | Never retrieve by wording similarity alone; report the near-duplicate rate in any library test. | M | [E] | b02, b05, c08, K13 |
| A5 | Skill definitions and the examples that cite them travel together in one library entry. | M / O1 | [E] | b12, b13, K10 |
| A6 | Exemplar use is worth most on multi-step items and little on the easiest. Use the S0 class pass rate to decide. | S0 | [E] | a19, b01, b03, b04, K02 |
| A7 | Keep a clear step pattern and readable text in any stored example; content alone is not the active part. | M | [E] | d06, d07, K27 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| B1 | Gate example injection on k-sample self-accuracy: inject only when the solver is often wrong; skip when it agrees with itself. | S0 / G7 | [S] | d14, c08, c24, d01, K18, K24, K25 |
| B2 | Retrieval rejection: show nothing when top similarity is below a threshold. | M | [S] | c08, c24, K18 |
| B3 | Attempt first, then show the example (productive failure) vs example first. | S0 | [C] | b21, b26, d12, d19, K22, K29 |
| B4 | Subgoal labels in stored entries vs unlabelled. | M | [S] | d05, b15, b16, K15, K26 |
| B5 | Fade by code-checked success: full example, then blank-step completion, then none. | S0 / M | [C] | a29, a14, K03, K04 |
| B6 | Generate-and-solve in the same turn vs paste-in demo. | O7 / O1 | [S] | c05, c06, c07, K16, K17 |
| B7 | Skill-indexed retrieval. | M | [S] | b10, b11, c10, K09 |
| B8 | Diversity plus complexity in selection. | M | [S] | b01, b06, d11, K12, K30 |
| B9 | Strict admission: code reproduces the answer from a masked statement and re-derives from subgoals. | G5 / M | [C] | d08, d09, K28 |
| B10 | Self-explanation instruction on top of examples. | none / O | [C] | a09, a10, c16, K05 |
| B11 | Store repair traces (wrong attempt, error, fix) in the library. | M | [S] | d12, a17, K21, K29 |
| B12 | Multi-model check: keep the library only where it wins, per model. | M | [C] | d13, d15, K19 |

Note on fit with SCHEMA: lessons are shown after the first attempt (section 5). That loosely matches the productive-failure side, but nothing here tests it for an LLM (see B3). The subgoal library stays [D] until B1, B2 and B4 pass.

## 8. Concrete tests on our bench

All arms at equal total tokens (G7): the arm with an example gets a smaller reasoning budget by the example length plus setup. Report accuracy, tokens, and rejection or fallback rates. Use the same answer extractor in every arm (Cheng 2026 showed that format fixes alone can erase an exemplar gain).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Example vs none (K24) | Held-out maths items with gold step counts, plus ARC-style rule tasks | zero-shot; one stored verified example of the same class; format-only stub of that example | accuracy at equal tokens, by gold step count | Near zero on easy items; small gain on 5+ step items; the stub recovers most of any gain if format drives it |
| T2 Self-accuracy gate (K25) | Items bucketed by k=4 self-agreement | inject always; inject only if self-accuracy below 50%; never | accuracy and tokens | Gate beats always by 1 to 2 points; always hurts the fully solved bucket (about -2) |
| T3 Retrieval ablation (K07, K13) | Library of verified examples; deduplicated test set | relevant vs shuffled-order vs irrelevant vs none; surface vs structure retrieval | accuracy | Irrelevant below none; shuffled loses much of the gain; structure beats surface by 1 to 3 points on smaller models |
| T4 Subgoal labels (K15, K26) | Code or proof tasks with an executable check; near and far transfer sets | labelled subgoal entries vs unlabelled; same facts | pass rate at equal tokens | +3 to 5 points, as in Zhao; larger on far transfer if the Margulieux pattern holds |
| T5 Attempt-first vs example-first (K22) | Novel-concept items and routine-procedure items | example first; attempt then example; no example | accuracy at equal tokens | Example-first wins on routine procedures; attempt-first at best equal on novel concepts (uncertain) |
| T6 Fading by success (K03, K04) | Repeated items from one class, then a new type | always full; fade after code-checked success; never | accuracy on same type and new type; tokens spent | Fading saves tokens with equal near-transfer accuracy; far transfer equal or lower |
| T7 Admission control (K06, K20, K28) | Library built by an LLM from solved items | unfiltered; answer-checked; answer plus masked reproduction plus re-derivation | downstream accuracy; rejection rate | Rejection rate 10 to 30% (older tutoring data); downstream gain small but removes error propagation |
| T8 Error injection (K06) | Library of 3 examples | all correct; 1 random wrong step; systematic error in all | accuracy drop | Random: small; systematic: large drop |
| T9 Generate-and-solve (K16, K17) | GSM8K-like and MATH-like | self-generate and solve in one turn; retrieved verified exemplar; reuse generated text as demo | accuracy at equal tokens | Integrated above decoupled by about 2 to 5 points; verified retrieved exemplar matches or beats self-generated |
| T10 Model sweep (K19, K24) | Same items on at least 3 models, including one reasoning model | library on vs off per model | accuracy per model | Sign differs by model; keep only where it wins |

## 9. What does not transfer, and why

- **Working-memory relief.** The core mechanism is human working-memory limits. An LLM reads its whole context; its gain comes from conditioning, not load relief [a02].
- **Schema construction over weeks.** The human effect builds over practice and is tested after a delay. A stateless LLM call learns nothing durable; the library is the only memory.
- **Expertise reversal as a learner-state variable.** In humans knowledge changes slowly. For an LLM, "expertise" is item-level and model-level. The nearest signal is per-item self-accuracy [d14].
- **Self-explanation.** Human self-explanation builds links to prior knowledge. LLM chain text is not evidence of its process (G10), so explanation prompts need their own test; the maths meta-analysis finds no extra benefit [a09].
- **Split attention.** Diagram-text integration is a visual problem. Text-only items have no direct analogue.
- **Motivation and effort.** Several human effects pass through effort and interest. Not relevant.
- **Productive failure.** The human benefit rests on activating prior knowledge in struggling attempts. An LLM that attempts first may only anchor on its own wrong approach (G4, S3 fixation). Untested.
- **Fine-tuning results** (REL, LEMA, OpenMathInstruct, STaR) show that process-rich data teaches. They do not show the same data helps in the prompt [a17, d12].
- **Simulated learners** (He-Yueya) test the LLM's memory of the literature, not learning [a15].
- **Old-model prompting results.** The 2022 gains (Wei, Fu, Wang, Madaan) came from models that needed the format. Modern instruct models already have it [d01].

## 10. Open questions

1. Do retrieved worked examples help a frontier reasoning model at equal total tokens? Evidence points to no for instruct models at 72B and to a loss for R1 (d01-d03). No test with closed frontier models.
2. Is example-first better than attempt-first for an LLM on novel items? No study found (d19).
3. Does fading driven by code-checked success beat always-full examples, including on far transfer? No study.
4. Do natural-language subgoal labels beat unlabelled examples for LLMs on maths? Only formal proofs tested (d05).
5. What are the first-hand effect sizes of Sweller and Cooper 1985, Cooper and Sweller 1987 and Kalyuga 2001? Paywalled.
6. Do self-generated exemplars help (Yasunaga) or not (Chen) when correctness is fixed by a verifier?
7. What are the Barbieri per-moderator g values (incorrect examples, self-explanation, grade level)?
8. What predicts the sign of the library effect across model families? Notes to Self suggests baseline strength on the item, format fragility and retrieval fit.
9. How much of the in-context gain in maths comes from format and distribution versus content, on modern models?
10. What share of LLM-generated examples fail a code check, and does admitting only verified ones change downstream accuracy? (32% appears in a snippet only.)
11. Does Gwak 2026's integrated-versus-decoupled result replicate on other models and with reasoning models?
12. Is skill labelling by a weaker model good enough? Didolkar saw weaker labellers do worse.

## 11. Sources

[V] opened (page or PDF text read). [M] snippet, abstract-only or not opened.

- [V] Sweller, van Merrienboer, Paas (2019) Cognitive architecture and instructional design: 20 years later. https://link.springer.com/article/10.1007/s10648-019-09465-5 (a01-a07)
- [V, abstract only] Barbieri, Miller-Cotto, Clerjuste, Chawla (2023) Meta-analysis of the worked examples effect on mathematics performance. https://link.springer.com/article/10.1007/s10648-023-09745-1 (a08, a09, b23, d17)
- [V] Nathan, Mertz, Ryan (1994) Learning through self-explanation of mathematics examples. https://website.education.wisc.edu/~mnathan/Publications_files/1994_Nathan_AERA94_SExplnCogLoad.pdf (a10-a12)
- [V, secondary] Wikipedia, Worked-example effect. https://en.wikipedia.org/wiki/Worked-example_effect (a13)
- [V] Lechner et al. (2024) Learning scientific observation with worked examples. https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2024.1293516/pdf (a14)
- [V] He-Yueya, Goodman, Brunskill (2024) Evaluating and optimizing educational content with LLMs. https://arxiv.org/abs/2403.02795 (a15, a16)
- [V] Simonds, Lau, Bandi (2024) REL: Working out is all you need. https://arxiv.org/abs/2412.04645 (a17, a18)
- [V] Wei et al. (2022) Chain-of-thought prompting. https://arxiv.org/abs/2201.11903 (a19, c01)
- [V] Min et al. (2022) Rethinking the role of demonstrations. https://arxiv.org/abs/2202.12837 (a20, c02)
- [V] Wang et al. (2023) Towards understanding chain-of-thought prompting. https://arxiv.org/abs/2212.10001 (a21, c03, c22)
- [V] Pardos and Bhandari (2023) Learning gain differences between ChatGPT and human tutor generated algebra hints. https://arxiv.org/abs/2302.06871 (a22)
- [V, abstract] Sweller (2010) Element interactivity and intrinsic, extraneous, and germane cognitive load. https://link.springer.com/article/10.1007/s10648-010-9128-5 (a23)
- [V, abstract] Renkl (2017) Learning from worked-examples in mathematics. https://link.springer.com/article/10.1007/s11858-017-0859-3 (a24)
- [M] Sweller and Cooper (1985). https://doi.org/10.1207/s1532690xci0201_3 (a25)
- [M] Cooper and Sweller (1987). https://doi.org/10.1037/0022-0663.79.4.347 (a26)
- [M] Ward and Sweller (1990). https://doi.org/10.1207/s1532690xci0701_1 (a27)
- [M] Chi et al. (1989). https://doi.org/10.1207/s15516709cog1302_1 (a28)
- [M] Renkl, Atkinson et al. fading. https://link.springer.com/article/10.1007/s11251-009-9107-8 (a29)
- [M] Kalyuga, Chandler, Tuovinen, Sweller (2001). https://doi.org/10.1037/0022-0663.93.3.579 (a30, d18)
- [V] Fu et al. (2022) Complexity-based prompting. https://arxiv.org/abs/2210.00720 (b01-b03, c04)
- [V] Zhou et al. (2023) Least-to-most prompting. https://arxiv.org/abs/2205.10625 (b04)
- [V] Zhang et al. (2022) Auto-CoT. https://arxiv.org/abs/2210.03493 (b05, b06, d10, d11)
- [V] Zhou et al. (2022) Teaching algorithmic reasoning via in-context learning. https://arxiv.org/abs/2211.09066 (b07-b09)
- [V] Didolkar et al. (2024) Metacognitive capabilities of LLMs. https://arxiv.org/abs/2405.12205 (b10, b11, c10, c25)
- [V] Chen et al. (2024) Skills-in-Context. https://arxiv.org/abs/2308.00304 (b12, b13)
- [V] Shi et al. (2023) LLMs can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 (b14)
- [V, slides] Morrison, Margulieux, Decker (2020) Using subgoal labels to reduce cognitive load. https://www.raspberrypi.org/app/uploads/2020/07/Using-subgoal-labels-to-reduce-cognitive-load-in-introductory-programming.pdf (b15)
- [V, abstract] Morrison, Margulieux, Decker (2020) The curious case of loops. https://researchconnect.buffalo.edu/en/publications/the-curious-case-of-loops/ (b16)
- [M] Morrison et al. replication, "Learning loops". https://core.ac.uk/download/215174894.pdf (b17)
- [M] Margulieux, Catrambone, Schaeffer (2018) subgoal-labelled expository text. https://informahealthcare.com/doi/epub/10.1080/08993408.2019.1707544 (b18)
- [V] What Works Clearinghouse record, Booth et al. https://ies.ed.gov/ncee/WWC/Study/92843 (b19)
- [V, developer page] SERP Institute AlgebraByExample summary. https://www.serpinstitute.org/algebra-by-example/ (b20)
- [V] Kapur, Hattie, Grossman, Sinha (2022) Fail, flip, fix and feed. https://doi.org/10.3389/feduc.2022.956416 (b21, b26)
- [M] Sinha and Kapur (2021) When problem solving followed by instruction works. https://journals.sagepub.com/doi/10.3102/00346543211019105 (b22)
- [M] van Loon-Hillen, van Gog, Brand-Gruwel, primary school maths. https://www.tandfonline.com/doi/abs/10.1080/01443410.2023.2273762 (b24; DOI may not match)
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 (c06, c21)
- [V] Chen et al. (2024) Relevant or random. https://arxiv.org/abs/2404.12728 (c07)
- [V] Liu et al. (2025) What makes in-context learning effective for mathematical reasoning. https://arxiv.org/abs/2412.12157 (c08, c24)
- [V] Learning by analogy: computational-graph retrieval (2024). https://arxiv.org/abs/2411.16454 (c09)
- [V] Weitekamp et al. (2025) TutorGym. https://arxiv.org/abs/2505.01563 (c11)
- [V] Gupta et al. (2025) Beyond final answers. https://arxiv.org/abs/2503.16460 (c12)
- [V] Zhao, Li, Kong (2023) Decomposing the Enigma. https://arxiv.org/abs/2305.16366 (c13, d04, d05)
- [V] Liu, Li, Dubrawski (2026) Notes to Self. https://arxiv.org/abs/2607.20372 (c14, d13-d15)
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271 (c15)
- [V] Practice less, explain more: LLM-supported self-explanation in calculus (2026). https://arxiv.org/abs/2604.00142 (c16)
- [M] ChatGPT-generated vs human help (PLOS). https://ouci.dntb.gov.ua/works/4Eeqy1K4 (c17)
- [M] LLM-generated worked examples in intro programming. https://ouci.dntb.gov.ua/works/9Q6bEDo7/ (c18)
- [M] TeachBench (2026). https://arxiv.org/abs/2601.21375 (c19)
- [M] LLM-drafted explanations of Java worked examples. https://par.nsf.gov/biblio/10613692 (c20)
- [V, not re-verified] Gwak et al. (2026) Not the example, but the process. https://arxiv.org/abs/2602.15863 (c05, c23)
- [V] Cheng et al. (2026) Revisiting chain-of-thought prompting: zero-shot can be stronger. https://arxiv.org/abs/2506.14641 (d01, d02)
- [V] DeepSeek-AI, DeepSeek-R1. https://arxiv.org/abs/2501.12948 (d03)
- [V] Madaan and Yazdanbakhsh (2022) Text and patterns. https://arxiv.org/abs/2209.07686 (d06, d07)
- [V] Toshniwal et al. (2024) OpenMathInstruct-1. https://arxiv.org/abs/2402.10176 (d08, d09)
- [V] An et al. (2024) LEMA, Learning from mistakes. https://arxiv.org/abs/2310.20689 (d12)
- [V] Zelikman et al. (2022) STaR. https://arxiv.org/abs/2203.14465 (d16)
- [M] Gap-search attempts d17, d18, d19: no source found.
