# Task-type limits: deep document

*Subfield A08.10 of cognitive load theory. Claim under study: worked examples suit well-structured tasks and are less effective for creative or less-structured tasks [V2]. Key work: Nievelstein et al. (2013). Built from evidence_a-d.jsonl, claims.jsonl (K01-K25) and critique.md in this folder. Evidence ids (a01, b14, d06 ...) point to those files. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested.*

**Bottom line in five lines.**
1. The one direct human test (Nievelstein 2013, law students) says the claim is too strong: worked examples still beat solving on a less structured task, even for advanced students. It is a single paper, with small cells, and nobody has replicated it.
2. The limit is real in a different place: what the example is about. Examples teach the skill only when attention is pointed at the principle, not the topic.
3. For language models, no study tests worked examples on ill-structured tasks head to head. All LLM evidence is by analogy (chain of thought, in-context examples, diversity studies).
4. That analogy says: written-out reasoning pays on math, symbolic and logic tasks and gives about nothing elsewhere. Close examples can hurt open tasks and homogenize output. Structure in the request (named steps, stratified directions, regeneration) helps open tasks without examples.
5. So our open mode should use named skill steps, at most one abstracted example, short hidden planning, parallel isolated draws, and a logged routing decision. Every one of these still needs a test on our bench.

---

## 1. What it is

**The claim.** The worked-example effect is the finding that novices learn more from studying a solved problem than from solving a similar problem themselves. It was first shown on algebra, geometry and physics (Sweller and Cooper 1985; Cooper and Sweller 1987; Tarmizi and Sweller 1988; a10). Cognitive load theory explains it: a novice who must solve at once is overloaded, uses weak search or copies an old solution and swaps numbers, and has no spare capacity to learn the structure (a10). A solved example removes the search and frees capacity for learning.

The subfield asks where this stops. Two readings exist.
- **Strong reading (the [V2] claim):** the effect belongs to well-structured tasks (one correct procedure, clear end state). On creative or less-structured tasks, examples help less or even constrain the learner.
- **Weak reading:** the effect extends to less-structured tasks, but the example has to be designed differently.

**What "structured" means.** Renkl (2023) defines ill-structured content as content with no algorithm that guarantees a solution. Only heuristics exist: rules of thumb that help but do not promise success (a09, b04). He also notes that "well-structured vs ill-structured" fits learning content better than whole domains: school math is mostly well-structured, but some math content is not (c05). That matters for routing at S0: the unit to classify is the task, not the field.

**Why it matters for our agent.** The schema has an open mode (S3 open) for tasks with no single right answer. If worked examples, step lists and chain of thought all lose power on such tasks, open mode needs other support. This document checks what the evidence says that support should be, in humans and in language models.

**Two meanings of "example" for an agent.** (a) A solved case placed in the prompt (in-context demonstration). (b) A solved case the agent retrieves from memory. The human literature is about study material shown before practice. The two differ in what they do to generation: examples shown during generation anchor it (fixation), examples studied beforehand teach a skill.

## 2. History and theories in depth

**1985-1990, algebra era.** Sweller and Cooper show that students who study worked algebra examples then solve test problems faster and with fewer errors than students who only solve (a10). The theory is cognitive load: working memory is limited, and weak-method search uses it up.

**Element interactivity.** Later cognitive load theory ties the effect to how many elements must be held in mind at once and how much they interact. Low-interactivity material favours self-generation. High-interactivity material favours worked examples (Chen thesis 2015, b11). This is the theory's own answer to the "generation effect" clash. It predicts that less-structured tasks, which have many interacting variable elements, should still gain from examples, because novices cannot automate the variable parts (the Nievelstein authors' own reading, a05).

**2000s, extension to less-structured skills.** Van Gog and Rummel (2010, a14, b13) note that worked examples came from highly structured tasks, while modelling examples (a video of a person) cover writing and similar skills. They list: instructional design (Hoogveld 2005), argumentation (Schworm and Renkl 2007), concept maps (Hilbert and Renkl 2009), designers' styles (Rourke and Sweller 2009), legal cases (Nievelstein). They warn of heterogeneity across these studies.

**The objection that Nievelstein tests.** Schmidt, Loyens, van Gog and Paas (2007) argued that high-guidance formats shown to work on well-structured tasks might not carry over to less structured ones (a15, read only second-hand). Nievelstein et al. (2013) set up the direct test with law cases.

**The two-level theory (Renkl 2023).** Examples for ill-structured content carry two levels: the learning domain (the skill, e.g. how to build an argument) and the exemplifying domain (the topic that shows it, e.g. lynx or global warming) (a11, b05, c03). If prior knowledge of the topic is low, skill learning suffers (Hilbert et al. 2004, 2008). If prompts aim at the topic, skill learning suffers (Schworm and Renkl 2007). So the boundary is not only task type. It is also where the learner's attention goes.

**Expertise reversal.** The classic corollary is that guidance helps novices and hurts experts. For less-structured tasks the Nievelstein authors expected no reversal, because variable elements cannot be automated (a05). The 2013 data agree (K02).

**Individual differences.** A re-analysis of Schwaighofer et al. (2016) data (Bichler et al. 2022, N=74) found that the worked-example benefit shrinks as shifting ability and fluid intelligence rise (b08), and that the worked-example effect on self-explanation quality was not significant (b07).

**The LLM arc (2022-2026).** The question reappears in new words. In-context demonstrations act mostly as format and label-space cues (Min 2022, a21). Chain of thought (written-out reasoning, a kind of worked solution) helps on math and symbolic tasks only (Sprague 2025, a17). Deliberation hurts on implicit-learning tasks (Liu 2025, a20). Examples fed to creative generation anchor and homogenize (b14, b15, a23, a24). Newer work shows that near examples can mislead even strong reasoning models, and that turning an example into a principle fixes it (d06). None of these tests the human claim directly. They test its cousins.

## 3. Core findings with exact numbers

Status column: E established, S single-source, C contested. "Human" or "LLM" in the source cell marks the population.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Worked examples beat solving on a law-case task, first-year students | Test (0-100) 58.63 (SD 27.74) vs 8.59 (SD 4.06); F(1,68)=105.22; f=1.24. Learning time 568 s vs 1146 s. Effort (9-pt) 5.46 vs 6.39. N=75, n=18-19 per cell | Nievelstein et al. 2013 (human; a01, a02, b01, c01) | S |
| No expertise reversal in third-year students | Test 82.28 (SD 18.11) vs 37.06 (SD 26.71); F(1,32)=37.03; f=1.02. Prior knowledge 17.12 vs 8.86, d=2.75. Time 427 s vs 976 s. N=36, n=9 per cell | Nievelstein 2013 (a03, a05, b02) | S |
| Process-step checklist alone does not help novices | Problem solving with steps vs without: time 1460.72 s vs 831.58 s (t(34)=4.68, d=1.56); test 8.33 vs 8.88. Steps main effect on test F(1,67)=4.91, f=.24 (Welch p=.05), interaction p=.065; third-year F<1 | Nievelstein 2013 (a04, b03, c02) | S |
| Benefit of examples grows as learner knowledge falls (essay writing) | 3 experiments, Korean university students; Exp 1 most knowledgeable, Exp 3 least; effect grew as knowledge fell. Sample sizes 63 and 62 (Exp 1, 2) came from search summaries | Kyun, Kalyuga, Sweller 2013 (a07, b09, b24; abstract only) | S |
| Examples help recognise designers' styles; second-years gain relatively more than first-years | No statistics seen | Rourke and Sweller 2009 (a06, b10; second-hand) | S |
| Argumentation examples need prompts on the principle, not the topic | N=71 student teachers, 4 prompt conditions; topic-directed prompts hurt skill learning | Schworm and Renkl 2007 (a08, b23; abstract and second-hand) | S |
| Low topic knowledge and topic-level gap filling hurt skill learning | Geometry proof study; no numbers in the chapter | Hilbert et al. 2008 via Renkl 2023 (a11, a26, b05) | S |
| Self-explanation prompts did not help transfer on semi-structured reasoning tasks | N=79, immediate and 2-week delayed tests; instruction plus practice raised performance in both groups, prompts added nothing | van Peppen et al. 2018 (human; a16) | S |
| Worked-example effect on self-explanation quality not significant; benefit shrinks with shifting and fluid intelligence | b=1.78, one-tailed p=.234, CI [-2.58, 5.38]; N=74 | Bichler et al. 2022 (b07, b08) | C |
| Near-domain human studies: null, partial, no reversal | Apprentice diagnosis: no overall gain, n=78; n=118: knowledge and scaffolded skill improved, unaided skill did not; physiotherapy N=61: near transfer p=.010, far p<.001 | d13, d14, d15 (abstract only) | C |
| Conformity to examples in creative generation is real but modest | Exp 1, 80 participants: share of critical features 4.4% (no examples) to 12.1% (nine examples) | Marsh, Landau, Hicks 1996 (human; b14) | S |
| AI-image examples raise design fixation | +0.32 (89% CI [.11, .55]), BF 124; image search +0.27; N=60, 20 per condition; fluency -0.21, variety -0.15 | Wadinambiarachchi et al. 2024 (human + GenAI; b15, c21) | S |
| ChatGPT ideation makes group ideas more alike | Similarity .24 (ChatGPT) vs .28 (card deck); t(32)=2.154, d=.47; N=36; about 15% more ideas per person | Anderson et al. 2024 (a23) | S |
| Co-writing with a feedback-tuned model lowers diversity; base model does not | 300 essays, 10 topics, 3 groups | Padmakumar and He 2024 (a24) | S |
| Strategies from an LLM reduce idea diversity during and after use | N=1,100, two preregistered experiments | Kumar et al. 2025 (b22, b28) | S |
| CoT gains concentrate on math, symbolic and logic | Mean gain symbolic +14.2, math +12.3, logic +6.9; top three categories 56.9 vs 45.5; all others 56.8 vs 56.1; MMLU: up to 95% of gain on questions with "=" | Sprague et al. 2025, 100+ papers, 20 datasets, 14 models (LLM; a17, a18, c10, c11) | E |
| Per-category CoT effect, own runs | Direct vs CoT: commonsense 74.8 vs 75.7; knowledge 73.3 vs 77.5; math 22.6 vs 50.2; symbolic 45.2 vs 56.1; soft reasoning 58.3 vs 60.3 | Sprague 2025 (a18) | E |
| A solver beats CoT at carrying out steps | Plan + tool solver beat Plan + CoT solver and CoT on average on math and logic sets | Sprague 2025 (a19) | S |
| Deliberation hurts implicit statistical learning | GPT-4o 87.50% vs 64.40% with CoT (-23.10, p<.0001); on a 440-item subset GPT-4o 94.0% vs o1-preview 57.7% (36.3 points, relative to GPT-4o) | Liu et al. 2025 (a20, b19) | S |
| Demonstrations act as format and label-space cues | Random labels cost little over 12+ models | Min et al. 2022 (a21, c08) | E |
| More similar context lowers quality on hard open-form questions | 160 questions, 3 difficulty levels, GPT-4, 6 graders; closed-form shows the opposite sign; effect strongest on hard and novel items | Li et al. 2024 (b16, b26, c09) | S |
| Many-shot gains depend on task type | Large on structured constrained-output tasks, small on open generation; MATH accuracy falls after about 125 shots; order shifts results 2-3 points; Banking77 83.4% at 1 per class vs 67.4% at 70 | Agarwal 2024; Upasani 2026 (c06, c14, c25, b17, b27) | E |
| Problems alone match problems with solutions on MATH | Unsupervised many-shot ICL >= ground-truth ICL | Agarwal 2024 (c07) | S |
| Worked-step prompts do not generalise | Blocksworld GPT-4: zero-shot 3.83%, general n-shot 6.13%, universal-algorithm CoT 51.3%, stacking-specific CoT 59.3% (261 instances); gains fall as problem size grows | Stechly et al. 2025 (c12, c13) | S |
| Models and humans use fewer reasoning elements on ill-structured problems | Accuracy 62.4 / 51.7 / 57.5 (well / intermediate / ill); humans 41% fewer elements, models 26% fewer; 192K model traces, 1,346 human traces | Li et al. 2026 (c15) | S |
| Guidance by successful-trace order helps strong models on ill-structured items, hurts weak ones | All models +4.4 (SE 1.2) ill vs +1.6 (1.1) well (not re-checked); strong models +9.7 (1.8) ill, dilemmas +18.8 (3.7), case analysis +8.4 (2.8); weak models lose up to 13.1 | Li et al. 2026 (c16) | S |
| Heuristic classification prompting: cheap, modest | 24 Game (1362 items): IO 5.65%, CoT 9.54%, ToT-BFS 55.65% at 7.28M tokens, HCoT 36.49% at 2.88M; 1D-ARC GPT-4o ToT-prompt 47.61% | Lin et al. 2026 (c22) | S |
| Extra thinking lowers accuracy on some tasks, even for reasoning models | Claude Opus 4 Misleading Math near 100% to 85-90%; DeepSeek R1 with 5 distractors 70% to 30% | Gema et al. 2025 (d01) | C |
| Explicit CoT lowers instruction following | 13 of 14 models drop on IFEval; Llama3-8B 75.2 to 59.0 (-16.2); trained per-item gate recovers most of the loss | Li et al. 2025 (d02) | S |
| Reasoning-model few-shot CoT can be worse than direct; an abstracted principle fixes it | GPT-4.1 AIME'25 34.0 to 48.0; R1-Distill-14B AIME 50.0 to 60.0; open-ended set 57.68 to 66.64 (I2S) and 68.40 (I2S+); small models gain 0-2 on open sets | Wang et al. 2025 (d06) | S |
| On math, CoT still helps R1-distilled models | Gain in 72% of model-by-dataset cells; one-shot beat five-shot; 32B +33% to +333% on hard sets; 1.5B +53% to +475% on easy sets | Ge et al. 2025 (d07) | C |
| Examples peak then decline on a structured task | Peak near 5-20 selected examples across 4 models; LLaMA-3.1-8B reaches 95% weighted F1 with 10-20 | Tang et al. 2026 (d08) | C |
| Few-shot removes spurious-feature inverse scaling | Few-shot examples eliminated it for all Claude models on Grades Regression | Gema 2025 (d01) | S |
| Open-ended output is homogeneous within and across models | Same-model similarity above 0.8 in 79% of cases (26K queries, 70+ models); cross-model 71-82% | Jiang et al. 2025 (d10) | E |
| Sequential regeneration restores diversity | Claude 3 Opus, GPT-4o, Gemini 2.0 Pro over 8 generations match 8 human writers; system-prompt creativity requests only marginal | Zhang et al. 2025 NoveltyBench (d09) | E |
| Verbalized sampling restores diversity | 1.6-2.1x diversity, +25.7% human rating, recovers 66.8% of base-model diversity | Zhang et al. 2026 (c20) | E |
| Population-referential prompts and direction stratification raise diversity | Top-tier pool diversity with quality proxies kept | Ibrahim et al. 2026 (a25) | S |
| Named heuristic steps with no example fix trace failures on dilemmas | Stakeholder collapse 15-31% to under 1%; uncertainty suppression 50-72% to 1-24%; matched budget Cliff's delta +0.79 to +0.90; 100 scenarios, 4 generators | Cooper and Velasquez 2026 (d05) | S |
| A silent step list helps; written-out steps hurt | GPT-4o implicit CoT +5.2 human points over standard prompt; explicit 2.2 below implicit; LLM judge 75.9, 76.5, 70.4 | Jiang et al. 2026 patent drafting (d03) | S |
| Reasoning-trace supervision destabilises creative scoring in small models | Completion 85.9-90.9% vs near 100%; 88.6% of failures are semantic repetition loops | Liu et al. 2026 (d04) | S |
| Gating whether to reason is feasible, task-type gating is not solved | Classifier validation accuracy 0.75-0.92; self-judgement high recall, low precision | d02, d11, d17 | S |
| Ill-defined task benchmarks give weak signal | Trivial fixed-token baseline scores 17.55 on IFEval, GPT-2 19.72; judge-seed variance up to 2% | Zhou and Shbita 2026 (d12) | S |

## 4. Mechanisms and models

Each mechanism is written so an engineer can wire it.

**M1. Load model of the worked-example effect.** Input: a learner (or model) with low skill in the target schema. Solving cold forces search, which fills working memory with search state, so the schema is not stored. Studying a solution removes search. Implementation analogue: when the agent lacks a procedure, supply the procedure as a fixed artifact (a named step list or one worked case) so generation tokens go to execution, not to inventing the method. This only matters when the model does not already know the method (K04: benefit rises as knowledge falls). Gate on "does the model's plain pass rate on this class sit low".

**M2. Two content levels (skill vs topic).** Represent every example as two fields: `skill` (the named heuristic, e.g. "state the strongest counter-argument, then answer it") and `topic` (the case content). The evidence says learning follows the skill when attention is directed there (a08, a11) and that a near-identical topic makes strong reasoning models copy steps (d06). Implementation: store skill lines separate from case content. In the prompt, show the skill line and at most one case whose topic is distant. Never prompt about the topic content (K05, K22).

**M3. Abstract-then-solve (I2S, d06).** Step 1: given an example, have the model write the principle behind it in one or two lines. Step 2: remove the example from context. Step 3: solve the new item with the principle only. This turned a harmful example into a helpful one for GPT-4.1 on AIME'25 (+14.0). Cost: one extra short call. Measured on math and open sets, not on our tasks.

**M4. Element-interactivity routing.** Low-interactivity tasks (each part independent) favour self-generation. High-interactivity tasks (parts depend on each other) favour worked support (b11). Feature for S0: count how many sub-decisions depend on each other. This is a design guess for LLMs, not tested.

**M5. Execution vs planning split (Sprague).** CoT gains come from carrying out symbolic steps, not from planning (a19). Route: for computational sub-steps use a tool or code; for judgement sub-steps do not add visible step-by-step text, which gave +2 on soft reasoning at most (a18).

**M6. Silent vs written steps (d03).** A step list followed without being written out helped (+5.2); writing it out hurt (-2.2 vs implicit). Implementation: give the step list in the system prompt as "apply these in your head, output only the result", or use a hidden planning call with a length cap, and measure both.

**M7. Fixation by shown examples.** Shown examples raise the share of their features in new ideas (4.4% to 12.1% with nine examples, b14; +0.32 with AI images, b15) and cut variety. Mechanism: the examples set the search region. Implementation: in open mode generate the first drafts from the bare task in isolated contexts; show examples only after, if at all. This agrees with the schema's S3 rule.

**M8. Structure in the request restores diversity (K14, K24).** Options, ordered by evidence: (a) sequential regeneration, show earlier outputs and ask for a different one (matched humans, higher token cost); (b) verbalized sampling, ask for several answers with stated probabilities (1.6-2.1x); (c) direction stratification, one planning call lists broad directions, then parallel draws each take one direction (a25); (d) population-referential instruction. Plain creativity requests in the system prompt barely help.

**M9. Gate by baseline strength (K15, K25).** Scaffold intensity should follow model strength: trace-order guidance gave +9.7 for strong models and up to -13.1 for weak ones. Implementation: store per-model per-class plain pass rate (the schema's class record) and switch the scaffold on only above a threshold, or measure both arms and keep the winner (G7).

**M10. S0 routing with logged misroutes.** Three gate types exist: model self-judgement (high recall, low precision), a trained classifier (accuracy 0.75-0.92), a difficulty router (d17). None separates well from ill-structured. Cheapest implementation: a short label rule on features (is there a check; is the answer exact; how many valid answers) plus logging of the route so that misrouting cost can be measured after the fact.

**M11. Dose control.** Cap examples at a few; shuffle order across attempts; report variance. Order moves results 2-3 points (c25, b17). Near-example selection scales worse than diverse selection as shots grow (b27).

## 5. What holds up

**Replications and corroboration.**
- No direct replication of Nievelstein (2013) exists. A citation scan of 93 citing records found none (d16). Treat K01 and K02 as single-source. The 36-student third-year arm has n=9 per cell, so "no reversal" is weakly powered, though the effect size (f=1.02) is large.
- The wider claim that the example benefit grows as knowledge falls in ill-structured domains has several studies (essay writing, design history, music, argumentation), but mostly one research network (Sweller, Kalyuga, Renkl) and mostly seen only as abstracts or second-hand. K04 is labelled established, but the critique notes it counts three sources that are close to one group.
- Strongest LLM result: Sprague et al. 2025, a meta-analysis of over 100 papers with own tests, numbers re-opened and confirmed in the critique. CoT helps math, symbolic and logic. This is [E].
- Diversity collapse and its remedy are corroborated by several independent groups (d09, d10, c20, a25, b20, b21, a23, a24).

**Failures, nulls and moderators.**
- Self-explanation prompts: no transfer gain in N=79 (a16). Worked-example effect on self-explanation: not significant, p=.234, N=74 (b07).
- Process checklist without solutions: no learning gain, more time (b03). But for LLMs, silent step lists did help in two studies (d03, d05), so the novice null does not carry over.
- Apprentice diagnosis: no overall advantage of examples over open problems (n=78); with n=118 only scaffolded skill improved, not unaided skill (d13, d14). These are abstract-level reads.
- Moderators: prior knowledge (benefit up as it falls), topic knowledge (low topic knowledge hurts skill learning), prompt target (skill good, topic bad), shifting ability and fluid intelligence (benefit shrinks as they rise), format (text and graphic novel faster than video, no learning difference, Hefter 2019, b06), prompt structure (pre-structured prompts before open ones, a12).
- LLM moderators: task type (math and symbolic vs soft), item novelty and difficulty (open-form harm strongest there, b26), model strength (guidance helps strong, hurts weak), number of examples (peak then fall), example similarity (near helps closed, hurts open, near copying in reasoning models), output format (instructions), reasoning length.

**Interventions that worked.**
- Examples plus principle-directed prompts (humans).
- Abstract-then-solve for reasoning models (d06).
- Named narrative steps without example on dilemmas (d05).
- Silent step list in patent drafting (d03).
- Sequential regeneration, verbalized sampling, direction stratification for diversity.
- A trained per-item gate for whether to reason (d02).
- Few-shot examples removing spurious-feature inverse scaling (d01).

**Interventions that did not work.**
- Topic-directed prompts; gap-filling in the topic; generic step list given alone to novices.
- Plain "be creative" system-prompt requests; sampling from several models (cross-model similarity 71-82%).
- Explicit CoT on instruction following and on implicit learning.
- Many shots beyond a modest number; near-identical examples for reasoning models.
- Reasoning-trace supervision for a creativity rubric (loops, d04).

**Contested.** Does extra reasoning hurt reasoning models? Harm on distractor and instruction tasks (d01, d02), but help on math (d07), and in d06 few-shot CoT hurt while a principle helped. The effect depends on task and model, so we have no single rule. K19 stays [C].

## 6. Language models

**There is no LLM test of the human claim.** No study gives a model a worked case, or a solved analogous case, on an ill-structured task and compares against solving cold at equal tokens. The closest is d06: open-ended sets gained 0-2 points on small models and up to 11 on one 14B model (57.68 to 68.40), judged by GPT-4.1. This is the first gap in critique.md.

**What the analogues say.**
1. *Written-out reasoning follows task type.* Gains are large where steps are symbolic and near zero elsewhere: symbolic 45.2 to 56.1, math 22.6 to 50.2, soft reasoning 58.3 to 60.3, commonsense 74.8 to 75.7 (a18). Most non-math gains were not significant under Bonferroni correction.
2. *Deliberation can hurt.* Implicit statistical learning: GPT-4o 87.5 to 64.4 with CoT (a20). Instruction following: 13 of 14 models drop, Llama3-8B by 16.2 points (d02). Distractor tasks: R1 70% to 30% (d01). Patent drafting: written steps 2.2 below silent ones (d03). Whether the implicit-learning harm holds in 2025-2026 thinking models is untested (critique gap 5).
3. *Examples as cues, not teachers.* For classification and multiple choice, demonstrations mostly show format and label space; random labels cost little (a21). For math, problems alone matched problems with solutions (c07). So where the model already knows the procedure, examples add little.
4. *Similar examples can hurt open tasks.* GPT-4 on 160 hard open-form questions: more relevant context scored lower than none, while closed-form benchmarks showed the reverse (b16, c09). Reasoning models copy steps from a similar example (d06).
5. *Examples narrow output.* Shown examples and LLM help raise fixation and homogenize ideas in humans (b15, a23, b22); LLMs themselves are homogeneous across models (d10) and the chat template adds collapse (b20, c18).
6. *Dose.* Structured classification peaks at about 5-20 selected examples (d08); reasoning-distilled models prefer one-shot over five-shot (d07); MATH accuracy falls after about 125 shots (c25). No dose data exist for open-form tasks.
7. *Ill-structured problems change how models reason.* Models drop 26% of reasoning elements on ill-structured items (humans 41%), and often start building a solution before representing the problem (c15, c17). Accuracy 62.4 (well), 51.7 (intermediate), 57.5 (ill) is not monotone, so structuredness is not simply difficulty.
8. *What changed open-task results.* Named heuristic steps without examples (d05: collapse to under 1%; d03: +5.2) and trace-order guidance for strong models (c16: +9.7, dilemmas +18.8). Diversity structure in the request (c20: 1.6-2.1x). A principle written out and the example removed (d06: +14.0 on AIME'25). Tool use instead of CoT on symbolic steps (a19).
9. *Model strength flips signs.* Guidance cost weak models up to 13.1 points (c16). Self-reflection helped most models on IFEval but hurt 1.5B and 1B models (d02). On math, relative CoT gain was larger for 32B on hard sets and for 1.5B on easy sets (d07).

**Caveats.** Many results use 2022-2024 models (Min, Stechly, Li 2024). Several 2026 results are preprints (d03, d04, d05, d08, c22). d05 and d03 measure trace features or small human samples, not verified answer quality. Li 2026 uses a GPT-4.1 judge. Zhou and Shbita show ill-defined benchmarks give weak signal, so our own judged scoring needs care (d12).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = section 5 of SCHEMA.md.

### Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| N1 | Do not use visible step-by-step text for soft or judgement sub-steps. Use step-by-step reasoning only for symbolic or computational sub-problems; use a tool for the execution part where one exists. Consistent with G11. | G11, S0 (mode), O# | [E] | a17, a18, a19, c10, c11 (K07) |
| N2 | Treat shown examples as format cues, not teachers. Example content need not be correct to serve format. Do not spend tokens polishing demonstrations. | S3, memory | [E] | a21, c08, c07 (K10) |
| N3 | Cap shots at a few, shuffle example order across attempts, and report variance. Do not use many-shot on open tasks. | S3 | [E] | c06, c14, c25, b17, d08 (K12) |
| N4 | In open mode, generate the first attempts from the bare task in isolated contexts. Show examples only after the first drafts. | S3 open, memory lessons | [E] | b14, b15, a23, a24, b22, d10 (K13, K24) |
| N5 | In open mode get variety by structure, not by plain "be creative" and not by mixing models: stratify directions in code, and use sequential regeneration or verbalized sampling. Compare costs at equal tokens. | S3 open, S7 | [E] | c20, d09, d10, a25 (K14, K24) |
| N6 | Log the S0 route (mode chosen, plain pass rate, features) so misrouting can be measured after the fact. | S0, section 6 | [E] on the logging need; routing itself [S] | d02, d17 (K20) |
| N7 | Do not cite the human "checklist alone does not help" null as a reason to drop step lists. It does not transfer to LLMs. | O1, S2 | [E] that it does not transfer | b03, d03, d05 |

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | One worked, distant solved case versus solving cold on open and ill-structured items at equal tokens. | S2, S3 open, memory | [S] | a01-a03 (K01, K02, K18) |
| T2 | Skill-level named steps (no example) versus example only versus both. | S2, O1 | [S] | d05, d03, a08, a11 (K05, K21) |
| T3 | Abstract-then-solve: write the principle, drop the example, then solve. | S2, memory | [S] | d06 (K22) |
| T4 | Silent step list (or hidden capped planning) versus written-out steps on open items. | G11, S3 | [S] | d03, d05 (K21) |
| T5 | Gate scaffold intensity by model baseline on the class. | G7, S0 | [C] | c16, d02, d07 (K15, K25) |
| T6 | Example similarity and dose on open items: 0, 1, 3, 5 examples, near vs distant. | memory, S3 | [C] | b16, b26, d08 (K11, K23) |
| T7 | Task-type classifier at S0 (well vs ill structured) and cost of misrouting. | S0 | [S] | d02, d11, d17 (K20) |
| T8 | Fast-answer path versus deliberate path on pattern-perception tasks. | S0, G11 | [S] | a20, b19 (K09) |
| T9 | Equal-token comparison of the pattern-listing scaffold (HCoT-style) against search. | O# | [S] | c22 (K17) |
| T10 | Forced self-explanation step versus none on reasoning items. | S2 | [S] | a16 (K06) |
| T11 | Scaffold on out-of-distribution problem size. | S2, O1 | [S] | c12, c13 (K16) |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup, planning and all attempts counted, G7). At least 3 seeds. Open-task quality scored by a held-out judge that sees no arm labels, no authorship, length-normalised (G5), plus a small human-checked sample. Report variance and per-item flips, not only means.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Open and ill-structured: dilemmas, case analysis, design briefs; 40+ items each | (a) cold; (b) one distant solved case; (c) one near solved case | Judged answer quality; distinctness; tokens | Distant case beats cold by a small margin for weak models; near case is equal or worse (K11, K22). No gain for strong models on familiar domains (K04). |
| B2 (T2) | Same open items | (a) cold; (b) 4-5 named skill steps, no example; (c) example only; (d) both | Judged quality; trace-feature checks (stakeholders, uncertainty) | Steps alone beat cold (d05, d03); both is not clearly above steps alone. |
| B3 (T3) | Open items plus a well-structured control set | (a) example in context; (b) principle only; (c) example then principle, example removed | Quality; copy rate of example steps | Principle-only >= example in context on open items; tests whether near copying (d06) appears. |
| B4 (T4) | Drafting and dilemma items | Silent step list vs written steps vs hidden planning capped at N tokens | Judged quality, repetition rate | Silent >= written by 2-5 judged points (d03). |
| B5 (T5) | Open items, two or three model sizes | Scaffold on vs off per model | Quality delta by model | Gain for strong, null or loss for weak; find the flip point (c16: -13.1 to +9.7). |
| B6 (T6) | Open-form items from a known and an unknown domain | 0, 1, 3, 5 examples; near vs distant | Quality vs similarity curve | Quality falls as similarity rises on hard novel items (b16); peak at 1-3 examples. |
| B7 (T7) | Mixed set of structured and open items, labelled by hand | S0 gate variants: own judgement, rule on features, trained classifier | Gate accuracy; quality loss on misrouted items | Misrouting an open item to checked mode costs more than the reverse; target gate accuracy above 0.85. |
| B8 (T8) | Pattern-perception items (artificial grammar, exception-laden labels) | Fast vs deliberate | Accuracy | Deliberate drops accuracy on non-reasoning models (a20); unknown for thinking models. |
| B9 | Open items with parallel draws | Parallel isolated draws vs direction stratification vs verbalized sampling vs sequential regeneration | Distinct clusters per 100k tokens; judged quality | Stratification and VS beat plain parallel; regeneration is best on diversity at higher cost (d09, c20). |
| B10 | Symbolic items | CoT vs plan + tool | Accuracy | Tool > CoT (a19). Cheap sanity check of N1. |

## 9. What does not transfer, and why

- **The learning measure.** Nievelstein measures what students learn from a study phase and show later on a new case. An inference-time prompt teaches nothing that persists. We want better output now. Gains in learning do not imply gains in output.
- **Study time.** Humans in the example condition saved half the learning time (568 s vs 1146 s). A model's example costs input tokens, and saves nothing unless it replaces reasoning tokens.
- **Cognitive load itself.** The model has no working-memory bottleneck of the human kind. Long examples can still distract, but the mechanism is attention dilution and copying, not capacity overflow.
- **Expertise reversal.** The human variable is prior knowledge, measured by a test. The model analogue is the plain pass rate on a class, which varies by item and cannot be assumed to behave like a person's knowledge. Li 2026 shows a flip with model strength, but that is not a clean reversal design.
- **Novice checklist null.** Novices got a step list but no way to apply it. A model can follow a list silently and well (d03, d05).
- **Generation effect.** In humans, generating material helps memory. For a model, generation just costs tokens.
- **Creativity fixation in people.** Fixation tests (b14, b15) measure human ideas after seeing examples. A model's fixation depends on context position, not memory. The structural remedy (isolated draws) is similar, but effect sizes do not carry over.
- **Population.** Law students, student teachers and apprentices are not a proxy for a reasoning model's skill distribution.
- **Sample and replication.** Nievelstein has n=9 per cell in the advanced arm and no replication. Do not let it justify a schema element alone.

## 10. Open questions

1. Does a worked or analogous solved case improve a strong LLM on ill-structured tasks, versus solving cold, at equal tokens? No study exists (critique gap 1).
2. Is there an LLM expertise-reversal point on open tasks: at what baseline does an example or scaffold stop helping? (gaps 2, 10)
3. Does Nievelstein replicate with larger third-year samples, or in medicine and ethics? (gap 3)
4. Which scaffold part carries open-task gain: named skill steps or example content? (gap 4)
5. Do reasoning models still show CoT-neutral or CoT-harmful behaviour on soft and implicit tasks? Is the Liu implicit-learning result replicated with 2025-2026 models? (gap 5)
6. How should S0 classify well versus ill-structured at low cost, and what does misrouting cost? (gap 6)
7. Does stratified or verbalized diversification beat example-fed ideation at equal tokens in a multi-sample agent? (gap 7)
8. Dose and similarity for open-form tasks; is distant better than near? (gap 8)
9. Do process-step checklists without examples help LLMs on novel open tasks, beyond trace features? (gap 9)
10. Do shifting ability and fluid intelligence have an LLM analogue, such as sensitivity to representation change?
11. Is the structuredness label best applied per task or per sub-step (Renkl footnote, c05)?

## 11. Sources

Marks: [V] opened this research run (full text, HTML or PDF text); [M] snippet, abstract or second-hand only. Nievelstein 2013 was opened by the search agents; the critique pass could confirm only title and DOI, so its numbers are labelled single-source.

- [V] Nievelstein, van Gog, van Dijck, Boshuizen (2013), The worked example and expertise reversal effect in less structured tasks: learning to reason about legal cases. Contemp. Educ. Psychol. https://repository.tilburguniversity.edu/bitstreams/0d52fd41-5fe8-4095-a7c2-22e15bfc7165/download ; https://research.ou.nl/en/publications/the-worked-example-an ; DOI 10.1016/j.cedpsych.2012.12.004
- [V] Renkl (2023), Using worked examples for ill-structured learning content. https://www.unh.edu/teaching-learning-resource-hub/sites/default/files (chapter)
- [V] Van Gog and Rummel (2010), Example-based learning. https://link.springer.com/content/pdf/10.1007/s10648-010-9134-7.pdf
- [V] van Peppen et al. (2018), self-explanation on reasoning tasks. https://www.frontiersin.org/articles/10.3389/feduc.2018.00100/pdf
- [V] Bichler et al. (2022), ill-defined statistics problems, re-analysis. https://doi.org/10.1007/s11251-022-09579-4
- [V] Marsh, Landau, Hicks (1996), How examples may (and may not) constrain creativity. https://link.springer.com/content/pdf/10.3758/BF03201091.pdf
- [V] Wadinambiarachchi et al. (2024), GenAI and design fixation. https://arxiv.org/abs/2403.11164
- [V] Chen thesis (2015, UNSW). https://unsworks.unsw.edu.au/bitstreams/4835a79e-b19a-4e55-b
- [V] Sprague et al. (2025), To CoT or not to CoT. https://arxiv.org/abs/2409.12183
- [V] Liu et al. (2025), Mind your step (by step). https://arxiv.org/abs/2410.21333
- [V] Min et al. (2022), Rethinking the role of demonstrations. https://arxiv.org/abs/2202.12837
- [V] Xiao, Zhao, Huang (2025), Role of diversity in ICL. https://arxiv.org/abs/2505.19426
- [V] Anderson, Shah, Kreminski (2024), Homogenization effects. https://arxiv.org/abs/2402.01536
- [V] Padmakumar and He (2024), Does writing with LMs reduce content diversity. https://arxiv.org/abs/2309.05196
- [V] Ibrahim, Azad, Baten (2026), Anchorless diversification. https://arxiv.org/abs/2605.30150
- [V] Li et al. (2024), Why does ICL fail sometimes. https://arxiv.org/abs/2407.02028
- [V] Upasani et al. (2026), Test-time adaptation via many-shot prompting. https://arxiv.org/abs/2603.05829
- [V] Yun et al. (2025), Price of format. https://arxiv.org/abs/2505.18949
- [V] Wenger and Kenett (2025). https://arxiv.org/abs/2501.19361
- [V] Kumar et al. (2025), Human creativity in the age of LLMs. https://arxiv.org/abs/2410.03703
- [V] Agarwal et al. (2024), Many-shot ICL. https://arxiv.org/abs/2404.11018
- [V] Stechly, Valmeekam, Kambhampati (2025), Chain of thoughtlessness. https://arxiv.org/abs/2405.04776
- [V] Li et al. (2026), Cognitive foundations for reasoning. https://arxiv.org/abs/2511.16660
- [V] Zhang et al. (2026), Verbalized sampling. https://arxiv.org/abs/2510.01171
- [V] Lin et al. (2026), Heuristic classification of thoughts. https://arxiv.org/abs/2604.12390
- [V] Gema et al. (2025), Inverse scaling in test-time compute. https://arxiv.org/abs/2507.14417
- [V] Li et al. (2025), When thinking fails. https://arxiv.org/abs/2505.11423
- [V] Jiang, Sun, Goetz (2026), When reasoning hurts legal drafting. https://arxiv.org/abs/2607.10480
- [V] Liu, Bahja, Lee (2026), When reasoning supervision hurts. https://arxiv.org/abs/2605.20364
- [V] Cooper and Velasquez (2026), Narration-of-Thought. https://arxiv.org/abs/2606.26366
- [V] Wang et al. (2025), From harm to help. https://arxiv.org/abs/2509.23196
- [V] Ge et al. (2025), Innate reasoning is not enough. https://arxiv.org/abs/2503.19602
- [V] Tang et al. (2026), The few-shot dilemma. https://arxiv.org/abs/2509.13196
- [V] Zhang et al. (2025), NoveltyBench. https://arxiv.org/abs/2504.05228
- [V] Jiang et al. (2025), Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Wang et al. (2025), Route to Reason. https://arxiv.org/abs/2505.19435
- [V] Zhou and Shbita (2026), Evaluating ill-defined tasks in LLMs (read through a fetch summary). https://arxiv.org/abs/2603.17067
- [V] Semantic Scholar citation list of Nievelstein 2013 (93 records scanned). https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.cedpsych.2012.12.004
- [M] Rourke and Sweller (2009), worked-example effect with ill-defined problems. https://doi.org/10.1016/j.learninstruc.2008.03.006
- [M] Kyun, Kalyuga, Sweller (2013), essay writing. https://doi.org/10.1080/00220973.2012.727884
- [M] Schworm and Renkl (2007), argumentation skills. https://doi.org/10.1037/0022-0663.99.2.285
- [M] Schmidt, Loyens, van Gog, Paas (2007), PBL critique. https://doi.org/10.1080/00461520701263350
- [M] Hilbert, Renkl, Kessler, Reiss (2008), learning to prove in geometry (via Renkl 2023)
- [M] Hefter et al. (2019), video vs text examples (via Renkl 2023)
- [M] Instructional Science (2023), self-explaining backwards or forwards, apprentices. https://doi.org/10.1007/s11251-023-09651-7
- [M] J. Comput. Assist. Learn. (2024), video-based modelling examples. https://doi.org/10.1111/jcal.12991
- [M] BMC Med. Educ. (2017), clinical reasoning in physiotherapy. https://doi.org/10.1186/s12909-017-1076-z
- [M] Sweller and Cooper (1985); Cooper and Sweller (1987); Tarmizi and Sweller (1988): cited via Renkl 2023 only.
