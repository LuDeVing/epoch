# Vygotsky: scaffolding: deep document

*Subfield A14.07. Focus: learning with a more knowledgeable other. Agent link: memory, with lessons as scaffolds for later problems. Evidence: evidence_a to evidence_d.jsonl (a01-a26, b01-b29, c01-c26, d01-d18), claims K01-K30, critique.md. Status marks: [E] established, [S] single-source, [C] contested. "Opened" means the page or PDF text was read in this research run; lines marked [M] were seen only as snippets or recalled from memory and are not quoted as measured.*

## 1. What it is

Two ideas are often fused and should be kept apart.

1. **The zone of proximal development (ZPD).** Vygotsky (1978, *Mind in Society*, ch. 6) said that what a child can do alone shows only finished functions. What the child can do with an adult's guidance shows functions that are still maturing. The gap between the two is the zone. He gave no controlled experiment for it in that chapter. It is a theoretical claim (a01, a02; K01).
2. **Scaffolding.** Wood, Bruner and Ross (1976) coined the word. A tutor takes over the parts of a task the learner cannot yet do, so the learner can work on the parts they can. Six tutor functions: recruit interest, reduce degrees of freedom, keep direction, mark critical features, control frustration, demonstrate (a05). Vygotsky did not write this. The link between the two was added later, and critics say they fit only partly (a08, a24, a07; K02 [E]).

The practical core for an engineer: capability is not one number per task. It is two: solo level and assisted level. Help is useful only when it targets the gap between them, and it should shrink as the learner improves (fading).

For our agent, the "more knowledgeable other" can be:
- a stronger model or a human writing hints or lessons for a weaker solver;
- the agent's own past self, whose verified lessons are stored and shown on later problems (the memory slot of SCHEMA.md section 5);
- a program that checks outputs and decides how much help to give.

The question for this subfield is narrow: **what do the human and AI studies say about how big a hint should be, when to give it, who may write it, and when stored lessons help or hurt?**

## 2. History and theories in depth

**Vygotsky (1930s; English 1978, 1986).**
- Learning leads development. Assisted performance reveals what is about to mature (a01).
- Children can imitate well beyond their solo ability, within limits (a02). The limit is not quantified.
- Mental-age example: two children test at mental age 8. With slight help on harder problems, one reaches about 12 and one about 9. The static score hides this difference. The mental age 8 is confirmed by a snippet; the 12 and 9 are recalled, not verified (a03).
- No formal model. No effect sizes.

**Wood and Middleton (1975).** Mothers teaching 4-year-olds a construction puzzle. The recalled finding: the best help was contingent. More help after failure, less after success. Fixed-level help did worse. From memory only (b15; 12 pairs recalled). The page returned 403 and the DOI in b15 looks wrong (Crossref gives 10.1111/j.2044-8295.1975.tb01454.x) (d17). Treat as unverified [S] (K04).

**Wood, Bruner and Ross (1976).** 30 children aged 3, 4, 5 built a 21-block pyramid with a tutor. Via a secondary study note (not the paper):
- unassisted success about 10%, 50%, 75% by age;
- tutors intervened directly twice as often with 3-year-olds as with 4-year-olds, four times as often as with 5-year-olds;
- children could recognise a correct construction before producing it;
- no 3-year-old built the four-block set; every 4- and 5-year-old did at least once;
- at age 3 children often took their construction apart, and help beyond their grasp did not carry over (a04, a06, a26).
Limits: small, middle-class, one task, no no-tutor control, descriptive. The 1976 PDF returned 403 and no copy could be opened (d18). Do not quote the 10/50/75 figures as measured.

**Cazden, Stone, Wass and Golding, Pea, Jiao and Lantolf.** Cazden (1979) is said to have tied scaffolding to the ZPD (a08, snippet only). Stone (1998), read in full: the metaphor is adult-centred, stresses gradual accumulation, and does not explain how learning happens. He keeps it and adds intersubjectivity, graduated assistance and transfer of responsibility (a07). Wass and Golding (2014): the two are partly alike at best (a24, snippet). Pea (2004): fading and handover should be the defining features, and fading is rarely tested (b17, from memory). van de Pol, Volman and Beishuizen (2010) is the standard decade review (1,414 citations) but was not read (d17).

**Cognitive-load critique.** Kirschner, Sweller and Clark (2006) say minimal guidance is inefficient for novices and worked examples help more (a25, via Wikipedia). Kalyuga et al. (2003) expertise reversal: guidance that helps novices can hurt experts (b16, from memory). These do not attack scaffolding. They set a boundary: help must match the learner (K06 [C]).

**Reciprocal teaching.** Palincsar and Brown. Rosenshine and Meister (1994), 16 studies: median effect 0.88 on experimenter tests, 0.32 on standardised tests (a11, snippet only). The gap suggests teaching to the test (K24 [S]).

**Technology era.** Intelligent tutoring (VanLehn 2011; Ma et al. 2014; b11, b12, both from memory), computer-based scaffolding meta-analyses (Belland; Kim) and, since 2023, LLM tutors and LLM agents with memory. Two direct analogues for our agent:
- hint-giving from a stronger model to a weaker solver (HintMR, SMART, Saha);
- self-scaffolding by stored lessons (Reflexion, ExpeL, ReasoningBank, Dynamic Cheatsheet, ACE, Voyager).

## 3. Core findings with exact numbers

Status: [E] established, [S] single-source, [C] contested. "Unverified" means not opened.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ZPD is a theory claim, no experiment | No data. Mental-age 12 vs 9 is recalled | Vygotsky 1978 (a01-a03) | [S] K01 |
| Scaffolding term and six functions are Wood et al., not Vygotsky | 6 functions | a05, a07, a08, a24 | [E] K02 |
| Pyramid task: unassisted success rises with age | About 10/50/75% for ages 3/4/5; tutor intervention 2x and 4x; N=30; secondary page only. Unverified | Wood et al. 1976 (a04, a06, a26) | [S] K03 |
| Contingent help beats fixed help | Recalled: 12 pairs, 4-year-olds. Unverified | Wood and Middleton 1975 (b15, d17) | [S] K04 |
| Computer-based scaffolding in STEM helps | g=0.46, 144 studies, 333 outcomes; largest at principles level and adults | Belland et al. 2017 (a09) | [E] K05 |
| Same, Bayesian, problem-based learning | g=0.385 | Kim, Belland, Walker 2018 (b09) | [E] K05 |
| Fading does not matter in the full set | 2017 full: no effect of fading or customisation rule; 2014 preliminary (35 studies, 97 outcomes, mean 0.44): adaptive better than fixed | a09, critique note 4 | [C] |
| Guided inquiry beats unguided | d=0.66 activities (20 studies), 0.71 performance success (17), 0.50 outcomes (60); 72 studies | Lazonder and Harmsen 2016 (b08) | [E] K06 |
| Human tutoring effect | Pooled 0.37 SD; stronger for teacher/paraprofessional tutors, earlier grades, in school | Nickow et al. 2020 (b07) | [S] K07 |
| VanLehn: step-based ITS d=0.76, human 0.79, substep 0.40, answer-based 0.31 | Recalled. Unverified | b11 | [S] |
| LLM scaffolds for human tutors raise mastery | Exit tickets 62% to 66% (+4 pp, p<.01); 900 tutors, 1,800 students, 7 weeks; $20 per tutor per year; treatment-on-treated +14 pp | Tutor CoPilot (a16, b01, c17) | [S] K08 |
| Gain is bigger for weaker tutors | Low-rated 56% to 65% (+9 pp); less experienced 61% to 68% (+7 pp) | b02 | [S] K08 |
| Unguarded GPT-4 helps practice, hurts later exam | Practice +48% (+0.137); exam -0.054 of 1 (-17%); about 1,000 students, about 50 classes, randomised by class | Bastani et al. 2025 (b05, d01) | [S] K09 |
| Guarded GPT tutor removes harm, adds nothing | Practice +127%; exam -0.004 (n.s.) | same | [S] K09 |
| GPT-4 wrong half the time | Correct 51%; 42% logical errors, 8% arithmetic; 57 problems x 10 asks | b06, d01 | [S] K09 |
| PNAS correction changes no number | Affiliation fix only, 20 Aug 2025 | d02 | [E] |
| Purpose-built AI tutor beats in-class active learning | Median post 4.5 (N=142) vs 3.5 (N=174); effect 0.63 (0.73-1.3 ceiling-corrected); enrolled N=233; one course; immediate test only | Kestin et al. 2025 (b04, d16) | [S] K10, K30 |
| Strong solvers are poor scaffolders | Qwen2.5-Math-7B 0.88-0.91 solving, 0.06 scaffolding win rate | MathTutorBench (c01) | [E] K11 |
| General LLM judges miss pedagogy | Judge accuracy below 0.7 on expert vs novice; fine-tuned reward model 0.84 | c02 | [E] K11 |
| Larger models leak more | Qwen2.5 7B to 72B: solve 11.3 to 38.7%, leak 29.3 to 61.0%; GPT-4o 33.1% solve, 35.2% leak; DeepSeek-V3 39.3%, 46.6% | UCO (c06, c07) | [E] K11 |
| Telling a model to scaffold is unreliable | GPT-4o gains on hard split; SocraticLM, LearnLM, Llama flat or down | c03 | [C] K12 |
| Fuzzy-rule prompt improves rubric scores | d=0.41 vs flat, 0.45 vs few-shot; adaptivity 0.41/0.46; 4 models, 200 synthetic scenarios; GPT-4 grader | Figueiredo 2025 (a15, c15) | [C] K12 |
| ZPD reward in RL tutoring | UCO full: solve 30.2%, leak 12.9%; without scaffold reward 23.5%, leak 20.2%; without progress reward 28.6%, 15.6% | c06, c07, b28 | [E] K13 |
| Tutor trained on simulated student | +33% predicted correctness over GPT-4o; AUC 0.76; rater agreement Kendall tau 0.06 | Scarlatos et al. (b27, c19) | [E] K13 |
| Stepwise hints lift small reasoners and cost less than self-consistency | R1-Distill-Qwen-7B MATH-500 64.86% to 82.43% at 1,180 tokens vs SC (K=8) 70.27% at 7,350; AIME-2024 20.69 to 68.97 (SC 20.69) | HintMR (c10, d05) | [E] K14 |
| Gain tracks headroom | MATH-500: Qwen2.5-Math-7B +9.5, R1-Qwen-7B +17.6, Llama-8B 52.70 to 71.62, Phi-4-mini 56.76 to 77.03 | d03 | [E] K14 |
| Bad hints hurt | Same-size untrained hinter: Qwen2.5-Math-7B MATH-500 75.68 to 54.05 (16 of 74 items); NuminaMath 46.67 to 36.00; fine-tuned hints never degraded | d04 | [S] K26 |
| Help only at low confidence | Up to 98.9% of helper accuracy, up to 90.0% fewer helper tokens (MATH500) | SMART (c11, c12) | [S] K15 |
| Gain from help rises with difficulty | Level 5: +39.23% (beam, Llama) and +73.20% (best-of-N, Qwen); level 1: +5.20% | c11, c12 | [S] K15 |
| Demonstrations help only part of the queries | 3 zones; 6 of 8 LLaMA models gain from selective ICL; KATE lags oracle demos by about 20% | Cui and Sachan 2025 (a12, a13) | [S] K16, no independent confirmation |
| LLMs misjudge difficulty | Zero-shot GLM and Qwen-max under 33% (chance 33%); two in-context examples: 30.61% to 62.96% and 26.59% to 68.78% | ZPD-SCA (c13, c14) | [E] K17 |
| Role-play predicts item difficulty | Correlation up to 0.75/0.76/0.82 (grades 4/8/12); direct prediction 0.36, -0.04, 0.30 | c24 | [E] K17 |
| Self-written lessons help on a verified signal | Reflexion HumanEval 91% vs 80%; AlfWorld +22, HotpotQA +20, HumanEval +11 | a19, c23 | [E] K18 |
| ExpeL insights vs retrieval trade by task | HotpotQA 36 vs 31, ALFWorld 50 vs 55, WebShop 37 vs 38; ExpeL 40 vs Reflexion 39 on HotpotQA, 54 vs 59 on ALFWorld | b19, c22 | [E] K18/K19 |
| ReasoningBank on WebArena | Overall 40.5 to 48.8 (+8.3), with MaTTS 51.8; steps 9.7 to 8.3 | b21, d07 | [E] K18 |
| Lessons beat equal-count retries | Shopping, k=5: memory 55.1 vs no-memory 39.0-42.2; memory without aggregation 52.4 | d06 | [S] K27 |
| Lessons beat majority vote | AIME 2024 Sonnet: baseline 23.3, vote of 3 23.33, memory 50.0 | Dynamic Cheatsheet (d09) | [S] K27 |
| Half of that gain is the instruction text | Empty-memory prompt 36.7; AIME 2025 6.7 to 23.3 to 36.7 | d08 | [S] K28 |
| Appending full history can hurt | GPT-4o AIME 2024 20.0 to 6.7 under full history; Sonnet 26.7 vs DC 50.0 | d09 | [S] |
| Small models use stored lessons poorly | Haiku AIME 2024 10.0 to 36.7 (gain) but GPT-4o-mini 16.7 to 13.3 (loss); GPQA 34.3 to 32.3 | d10 | [C] K25 |
| Playbook memory works without labels if an execution signal exists | ACE AppWorld 42.4 to 59.4 (labels), 57.2 (no labels); DC 51.9; ICL 46.0; GEPA 46.4 | ACE (d11, d12) | [S] K29 |
| Self-review without outside signal lowers accuracy | GPT-3.5 kept first GSM8K answer 74.7%; with oracle labels GSM8K 75.9 to 95.5 | Huang et al. 2024 (b22) | [E] K20 |
| Own-success workflows vs 14 human workflows | WebArena 35.5 vs 33.0 vs baseline 23.5; different harnesses | AWM (d13) | [S] K19 |
| Lesson writer strength | HotpotQA gpt-4 writer 39.0, gpt-3.5 writer 32.0, hand-crafted about 32.0, ReAct about 28.0; confounded | ExpeL (d14, b20) | [S] K19 |
| Curriculum just beyond skill drives progress | Voyager random curriculum: -93% items; STRETCH 0.79 vs 0.72-0.73 | b18, c21, b29 | [E] K21 |
| Teacher explanations help weaker LLM and generalise | StrategyQA 58% to 63% (Flan-T5); LLaMA-65B teaching LLaMA-7B about +8%; unexplained items 55% to 61.6%; misaligned teacher drives student to chance | Saha et al. (b24, b25) | [E] K22 |
| Too much teacher help backfires | Accuracy peak 71% at 40% intervention, 69% to 63% beyond 60% | b24 | [S] |
| Distilled chains lift small model | T5-XXL GSM8K 8.11% to 21.99% | Magister et al. (a22) | [E] K22 |
| Least-to-most decomposition | SCAN length 16.7% to 99.7%; GSM8K 60.97% to 62.39%; 5+ steps 39.07% to 45.23% | Zhou et al. (c20) | [S] K23 |
| Self-hints need a capable solver | PHP-Standard on text-davinci-002 49.43 vs 49.91 base (-0.48); gain grows on text-davinci-003 | d15 | [S] K25 |

## 4. Mechanisms and models

This section turns the findings into parts an engineer can build. None of it is in SCHEMA.md unless the schema already says so.

### 4.1 Two numbers per item: solo and assisted
For each problem (or problem class) keep:
- `solo`: pass rate of the plain solver, no help;
- `assisted`: pass rate with a hint, demonstration or lesson.

Zones (Cui and Sachan, a12): **easy** (solved alone), **ZPD** (solved only with help), **out of reach** (not solved even with help). Help is worth its tokens only in the middle zone. Zones are per model. Easy items overlap across models; ZPD items do not (a12). So the zone table must be measured per solver, not copied from another model.

The agent already keeps a class record in code (SCHEMA section 5). Adding `assisted` to that record costs little: log pass rate with and without a shown lesson.

### 4.2 Contingent help ladder (the Wood and Middleton rule)
Rule from the human literature, not yet tested on LLMs:
```
level = 0
for attempt in attempts:
    run with help[level]
    if check passes: level = max(0, level-1)   # help less after success
    else:            level = min(L, level+1)   # help more after failure
```
Levels, least to most: (0) nothing; (1) show the failing output or mark the critical feature; (2) a stepwise hint for the next step only; (3) a worked sub-step; (4) the full solution (last resort, for lesson writing, not for scoring).

Mapping of Wood et al.'s functions: "reduce degrees of freedom" maps to O3 (decompose) and O1 (specialise); "mark critical features" maps to showing the failing output (G2); "control frustration" has no counterpart for a model, except that the program stops a branch (G12).

Evidence the idea is sound for models: gain from help rises with difficulty (SMART c12); help given when not needed adds cost with little gain (SMART level 1, +5.20%). Evidence that over-help backfires: Saha b24 (accuracy fell from 69% to 63% beyond 60% intervention).

### 4.3 Fading by confidence (SMART)
Run the solver. At each step get a confidence score (token probability or a process reward model). Call the helper only where confidence is low. Result: up to 98.9% of helper accuracy with up to 90.0% fewer helper tokens (c11). Needs a step scorer. Math only, one group. This is a software form of fading.

### 4.4 Stepwise hint, not answer (HintMR, UCO)
- The helper writes one hint for the next step, from the full solution or known answer (oracle-informed in HintMR; GPT-5.2 for AIME-2025). The solver continues. Repeat.
- Quality gate: a hinter that was not trained to hint can lower a good solver by about 20 points (d04). A fine-tuned hinter never degraded.
- Leakage control: stock large models leak answers (GPT-4o 35.2%, DeepSeek-V3 46.6% in UCO). A program check (does the hint contain the final answer?) is cheap. Tutor RL with a leakage penalty cut leak to 12.9% (c06).
- Cost: hint-generation tokens by the helper are not counted in HintMR's table, and wall-clock time was 2 to 3 times higher than no-hint (d05). An equal-token comparison must count helper tokens.

### 4.5 Lessons as self-scaffolds (memory)
Pipeline shared by Reflexion, ExpeL, ReasoningBank, Dynamic Cheatsheet, ACE, AWM:
1. Attempt the task.
2. Get an outside signal (test result, environment outcome, label).
3. Write a short lesson from the real failing or passing output.
4. Store it by problem class.
5. On a later problem, retrieve by similarity and show the lesson after the first attempt (SCHEMA already says this).

Variants:
- **Insights vs raw trajectories** (ExpeL): neither dominates; best is both (b19).
- **From failures as well as successes** (ReasoningBank): Shopping 46.5 (success only) to 49.7 (with failures). Older memories (Synapse, AWM) did not gain from failures (d07).
- **Curate, do not append.** Full-history appending hurt GPT-4o (20.0 to 6.7) (d09).
- **Rewrite across questions** (Dynamic Cheatsheet, ACE): ACE 59.4 vs DC 51.9 on AppWorld (d11).
- **Skill library of verified code** (Voyager): removal plateaus progress (b18).

### 4.6 The validity gate
Every positive memory result has an outside signal: tests (Reflexion), environment success (Voyager, AWM), execution outcomes (ACE). Without it, self-review lowers accuracy (b22) and ACE and Dynamic Cheatsheet can degrade (d12). Rule: write a lesson only on a verified outcome; admit a lesson to the store only after it helps held-out items of its class (K26, K20). This matches G2, G3 and G10.

### 4.7 Curriculum beyond current skill
Voyager's automatic curriculum proposes the next task just beyond current skills. A random curriculum cut discovered items by 93% (b18). STRETCH alternates a Scaffolder that sets tasks at the edge and a Learner (b29). These are training or discovery settings. For a fixed-weights agent, the analogue is the order in which problems are seen and which lessons are written first. Dynamic Cheatsheet's authors suggest related questions early may help, but did not test order (d10).

### 4.8 Cheap simulated learners
Role-play at fixed skill plus item-response theory predicts item difficulty with r up to 0.82 (c24). Assistant-tuned LLMs play weak students too well (c25). A cheap weak model can serve as a proxy student to tune hint size before using it on the real solver, but its realism is limited (K13, K17).

## 5. What holds up

**Held up (several sources).**
- Guidance beats pure discovery for novices (Lazonder and Harmsen d=0.50-0.71; K06).
- Computer-based scaffolding gives small to moderate STEM gains (g=0.385-0.46; K05). These are human-learner numbers and must not be transferred as sizes.
- Strong solvers are not good scaffolders; stock LLMs leak answers (4 sources; K11).
- Models misjudge what is within reach of a learner (3 sources; K17).
- Stored lessons from a verified signal beat no memory (Reflexion, ExpeL, ReasoningBank, DC, ACE; 4 sources; K18).
- Self-review without an outside signal does not help (3 sources; K20).
- A curriculum just beyond current skill drives progress (3 sources; K21).
- Teacher explanations lift weaker LLMs and generalise to unexplained items (K22).

**Contested or weak.**
- Fading. The 2014 preliminary meta-analysis found adaptive fading or adding better than fixed fading. The 2017 full version (144 studies) found no effect of fading or the customisation rule (a09). This challenges a core scaffolding claim. The LLM side has only SMART (K05, K15).
- Prompting to scaffold. MathTutorBench: only GPT-4o gained on the hard split (c03). Figueiredo reports d=0.41-0.46 but the grader is an LLM, and LLM judges are near chance on pedagogy (c02). Weak (K12).
- Expertise reversal and discovery-learning numbers are recalled, not read (b13, b16).
- Hints vs lessons by solver strength (K25): external hints help the weakest solver most; self-hints and lessons need a capable solver. Evidence is 4B-8B only for hints (d03) and one paper family for lessons (d10).

**Failures and harms.**
- Bastani: unguarded GPT-4 lowered unaided exam scores by 17%. Students did not perceive reduced learning (b06). The guarded tutor gave no exam gain either. The 51% error rate was for "What is the answer?", not for hint-giving (d01). The SSRN design critique (4898213) was not read; class-level assignment and a one-shot exam are likely objections.
- HintMR: untrained same-size hints cost about 20 points (d04). AIME-2025 was unchanged for several models (d03).
- Saha: a misaligned teacher drives the student to chance; too much intervention lowers accuracy (b24, b25).
- Dynamic Cheatsheet: GPT-4o-mini fell below baseline; full-history appending hurt GPT-4o (d09, d10).
- ExpeL is below Reflexion on ALFWorld (54 vs 59) without repeats (b19).
- ACE and Dynamic Cheatsheet can degrade without reliable feedback (d12).

**Controls missing in the original papers.**
- Dynamic Cheatsheet: about half of the Sonnet AIME 2024 gain (23.3 to 36.7, of 23.3 to 50.0) came from the empty-memory instruction text (d08). Every lesson test needs an instruction-only arm (K28).
- Equal-compute baselines: ReasoningBank's no-memory best-of-5 was flat (39.0-42.2) while memory reached 55.1 (d06). DC's majority vote of 3 gave no gain (d09). Neither is token-matched, and both authors built their own method. A token-matched retry loop with a verifier has not been tested (K27).

**Small samples.** AIME sets are 30 or 15 items; one item is 3.3 to 6.7 points. HintMR sets are 15 to 75 items. Kestin: one course, one test. Tutor CoPilot: one provider and district.

## 6. Language models

**As tutors (human-learner outcomes).**
- Tutor CoPilot: an LLM giving suggestions to human tutors raised mastery +4 pp overall and +9 pp for lower-rated tutors. The effect shrinks as skill rises, like expertise reversal (b02).
- Kestin: a purpose-built step-by-step, answer-withholding AI tutor beat active learning, effect 0.63 (d16). No delayed test.
- Bastani: unguarded GPT-4 hurt later performance (-17%); a guarded one did not help (d01).
- A rule that fits all three: help must withhold the answer and rest on correct content. The studies differ in who receives the help (tutor vs student), so this is a pattern, not a proof.

**As tutors (benchmarks and simulation).**
- MathTutorBench: solving skill and scaffolding trade off (0.88-0.91 vs 0.06 win rate) (c01). Judge models near chance; a fine-tuned reward model reaches 0.84 (c02).
- GuideEval: SocraticLM perception-of-error 0.1411 vs roughly 0.4-0.78 for general models; some general models affirm correct reasoning at 0.9+ but flag errors at under 0.5 (c04). Judge-human agreement 89.0-97.0%.
- UCO: a ZPD-style scaffold reward lifted solve rate from 23.5% to 30.2% and cut leakage from 20.2% to 12.9% (c07). Removing it cost -3.4 (expertise), -9.0 (student understanding), -10.6 (pedagogy) on MathTutorBench.
- LearnLM: expert preference +31% over GPT-4o (a23) but solve gain only 1.5-4.3 points (b26). Qwen2.5-72B, DeepSeek-V3 and GPT-4o raise solve rates 33-39 points but leak.
- Inquizzitor: ZPD-faithful feedback 78.22-88.57% in real classroom data; gave in to off-task tricks in 4-5% of utterances (c16).

**As helpers for small solvers.**
- HintMR: see section 3. Gains are largest for the weakest solvers; AIME-2024 Llama-8B 0.00 to 44.83; AIME-2025 Llama-8B 6.67 to 6.67 (no gain).
- SMART: up to 98.9% of helper accuracy at up to 90.0% fewer helper tokens.
- Saha: explanations from a stronger model help; a smaller teacher did not help a larger student.
- Weak-to-strong (Burns): performance gap recovered above 20% on NLP tasks, often above 50% for the largest students; near zero on chess puzzles for the weakest supervisors; poor on reward modelling (b23). Fine-tuning, not in-context.

**As self-scaffolders (memory).** See sections 3 and 4.5. Gains of 8 to 27 points on agent and reasoning benchmarks when an outside signal exists. Part of the gain is prompt text (d08). Small models gain little or lose (d10). ExpeL: gpt-4 writer 39.0 vs gpt-3.5 writer 32.0 (d14).

**As judges of difficulty.** Zero-shot level labels at or below chance for some models; raised to 62-69% by two examples (c13, c14). Simulators over-perform as weak students (c25). Direct difficulty prediction is poor; role-play plus IRT is far better (c24).

**Decomposition.** Least-to-most: SCAN 16.7% to 99.7%; GSM8K 60.97% to 62.39% (c20). The gain tracks how compositional the task is.

**What changed results most.** (1) An outside verifier or execution signal. (2) Hint quality (fine-tuned vs untrained hinter: roughly 20 points apart). (3) Solver headroom. (4) Answer withholding. (5) Curating rather than appending memory.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Write lessons only from a verified outcome (test, held-out check, execution result), never from the model's own opinion. Already fits G2 and G10; make it an explicit rule on the memory write path. | G2, G10 / memory | [E] | K20, K18; b22, a19, d11, d12 |
| A2 | Keep lessons shown after the first attempt, never before (already in SCHEMA). Add a code check that no lesson or hint contains the final answer when a stronger model wrote it. | memory / G2 | [E] | K11, K13; c06, c07, b26 |
| A3 | Do not assume a stronger model writes good lessons. Strong solving does not mean good scaffolding (0.88-0.91 vs 0.06). Lessons from a stronger model pass the same held-out gate as own lessons. | G3 / memory | [E] | K11, K26; c01, d04, b25 |
| A4 | Curate lessons; do not append whole history. One line per lesson, by problem class (already in SCHEMA). | memory | [E] | K18; d09 |
| A5 | Lessons from failures are allowed if the failure has an external signal. | memory | [E] for direction; effect size [S] | d07 |
| A6 | Keep a per-model solo/assisted table in the class record. Zones are model-specific. | S0 / class record | [E] model-specificity; size [S] | K16, K17; a12 |
| A7 | Never ask the model to rate item difficulty directly; use measured pass rates from the class record. | S0 / G5 | [E] | K17; c13, c14, c24 |
| A8 | Every memory test includes an instruction-only arm with an empty store. | G7 | [E] for the control need | K28; d08 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Contingent hint ladder (more after failure, less after success) vs fixed full hint at equal tokens | O1, O3, G12 | [S] Wood and Middleton, unverified; no LLM test | K04; b15, d17 |
| T2 | Fading by confidence: helper only at low-confidence steps | G12 / S | [S] SMART | K15; c11, c12 |
| T3 | Stepwise hint from stronger model vs self-consistency at equal tokens, helper tokens counted | O3 | [E] in HintMR, but helper tokens uncounted | K14; c10, d05 |
| T4 | Verified-lesson memory vs plain retry or best-of-N at equal tokens, with instruction-only control | memory | [S] | K27, K28; d06, d09, d08 |
| T5 | Lesson source: own failures vs stronger-model vs hand-written | memory | [S] | K19; d13, d14 |
| T6 | Validity gate: held-out admission test vs admit all | G3 / memory | [S] | K26, K29; d04, d12 |
| T7 | Problem ordering by measured difficulty vs random, for building the lesson store | S / memory | [S] | K21; b18, d10, a13 |
| T8 | Selective retrieval: show lessons only for classes the agent fails alone but solves with help | memory | [S] | K16; a12 |
| T9 | Solver-size ladder: gain of hints and of lessons at three or more sizes | G12 | [C] | K25; d03, d10, d15 |
| T10 | Self-estimate of ZPD: can the agent predict what it solves with a hint | S0 | [S], unverified | K16, K17; a12, c13 |
| T11 | Decompose-first (least-to-most) by task composition | O3 | [S] | K23; c20 |
| T12 | Persistence harm check: performance after the store is removed | memory | [S] | K09, K30; d01 |
| T13 | Cap hint size by solver strength (strong solver gets light help) | G12 | [C] | K25, K06; d03, b02 |

## 8. Concrete tests on our bench

Common rules. Both arms get the same total token budget, including setup, helper, hint and lesson-writing tokens (G7). Use a non-LLM scorer (code check or exact match) where possible (G5). Include a plain arm and, for memory tests, an instruction-only arm (K28). Report items solved per 1,000 tokens as well as pass rate. Use at least 100 items for rates; AIME-size sets (15-30 items) are noise (one item = 3.3-6.7 points).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Math or code items with a program check; pool where plain solve rate is 20-80% | (a) fixed full hint after first fail; (b) contingent ladder 0-4; (c) plain retry | Pass rate at budget; mean hint level used | Ladder ties full hint at fewer tokens. Guess +2 to +5 points. If no better than plain retry, drop |
| T2 | Same pool, small solver with step confidence | (a) always-on helper; (b) helper at low-confidence steps only; (c) no helper | Accuracy and helper tokens | About 90% of (a)'s accuracy at far fewer helper tokens (SMART). Not shown outside math |
| T3 | Hard split (plain rate under 40%) | (a) stepwise hints from stronger model, hint tokens counted; (b) self-consistency matched in tokens; (c) plain | Pass rate | Hints beat SC on hard items (HintMR AIME 68.97 vs 20.69); gap shrinks once helper tokens are counted |
| T4 | Sequence of 100+ related problems in 5-10 classes (ARC subset, BrainTeaser, math) | (a) verified lessons; (b) retry only; (c) best-of-N with verifier; (d) instruction text only with empty store | Pass rate on later problems; tokens per solved item | Memory beats (b) and (c) only if lessons are reused. Published gains +8 to +27 points, part of it instruction text |
| T5 | Same sequence; fixed writer budget | (a) own-failure lessons; (b) stronger-model lessons; (c) hand-written; (d) none | Later-item pass rate | Stronger-model lessons good on first pass, bad ones removed by gate; own-failure is cheapest |
| T6 | Same sequence with 20% injected wrong lessons and a clean store | (a) admit all; (b) held-out admission gate; (c) no memory | Pass rate; harm rate (items solved by plain but lost) | Gate prevents most harm; guess 10-20 points of protection (HintMR bad hint = -21.6) |
| T7 | Sequence ordered by measured plain solve rate vs random | (a) easy-to-hard stretch order; (b) random; (c) hard first | Later-item pass rate | Small (0 to 3 points); keep the cheaper arm |
| T8 | Items split by solo/assisted status from a pilot | (a) lessons shown for all; (b) shown only for ZPD-zone classes; (c) none | Pass rate and tokens | (b) matches (a) at lower tokens; no gain on easy classes |
| T9 | Three solver sizes (small, mid, frontier) | hints, lessons, plain at each size | Gain vs plain accuracy, per size | Hint gain falls with strength. Lesson gain flat or negative at the smallest size |
| T10 | 200 items | Agent predicts "solvable alone / with hint / neither" vs measured zones | Agreement with measured zone | Likely near chance without examples (ZPD-SCA). If under 60% accuracy, A7 stays |
| T11 | Compositional vs non-compositional items | Decompose-first vs direct | Pass rate by composition | Gain only on compositional items (SCAN 16.7 to 99.7; GSM8K +1.4) |
| T12 | Last 50 items of T4 with the store emptied | (a) store used then emptied; (b) never had store | Pass rate | No persistence for a fixed model; a harm check, not a learning test |
| T13 | Items at three plain-solve-rate bands | Heavy hint vs light hint vs none, per band | Pass rate by band | Heavy hint helps the low band, ties or hurts the high band |

## 9. What does not transfer, and why

- **Development.** Human learners mature; the model's weights are fixed. The ZPD is about functions that are about to mature. For our agent nothing matures inside a session. "Zone" can only mean "solves with help now". Transfer of responsibility (handover) has no counterpart without training. Only the memory store grows.
- **Effect sizes.** g=0.46 and d=0.37 are for children and students over weeks. They say nothing about size for a model.
- **Affect and motivation.** Recruit interest and control frustration are two of the six functions. A model has no frustration. Drop them.
- **The Wood et al. numbers.** 30 children, one task, no control, secondary source. Not a quantitative guide.
- **Human tutoring bundles time and attention** with scaffolding (b07). Not separable.
- **Simulated students.** Many LLM-tutor results use LLM students and LLM judges whose realism is weak (K13, K17). Treat them as method checks, not outcome evidence.
- **Training-based results.** UCO, Scarlatos, GuideEval SFT/DPO, Weak-to-strong, Magister, ZPD-ordered fine-tuning are outside our no-training constraint. Use only as evidence that the signal (leakage penalty, ZPD zone) is real.
- **Human in the loop.** Tutor CoPilot gives suggestions to a human who chooses. Our agent has a program filter instead.
- **Oracle hints.** HintMR hints are built with the known solution. At test time we have none, so the upper bound does not apply.
- **Reciprocal teaching, peer learning, Socratic dialogue.** Multi-turn teaching between two minds. A single-agent loop has no second mind, and G9 bans debate.
- **Persistence claims.** Kestin has no delayed test; Bastani measured one exam. No persistence data exist for AI scaffolding (K30).

## 10. Open questions

1. Does contingent hint escalation beat fixed-size help for an LLM at equal tokens? No LLM paper tests it, and Wood and Middleton is unverified.
2. Do stored lessons beat a token-matched retry loop with a verifier? Existing baselines are no-memory and author-built.
3. Which lesson source is best at fixed writer strength: own failures, a stronger model, or hand-written? ExpeL confounds writer strength with experience; AWM compares different harnesses.
4. Can a model predict its own ZPD? Cui and Sachan is not independently confirmed; ZPD-SCA shows LLMs misjudge difficulty.
5. Does fading help outside math? Does adaptive fading beat fixed fading (2014 preliminary) or make no difference (2017 full)?
6. How do hint and lesson gains vary over at least three solver sizes up to frontier?
7. What are the true Wood, Bruner and Ross pyramid numbers? The 1976 paper must be opened.
8. Does Kestin replicate in other courses, and do gains persist?
9. Do ZPD-ordered curricula beat random order for in-context lessons?
10. What does the SSRN critique of Bastani's design say, and does it change the harm estimate?
11. What are Cui and Sachan's exact gains (figures were not extracted)?
12. How much of the lesson gain is the instruction text on other benchmarks and models (Dynamic Cheatsheet's half is one paper)?

## 11. Sources

[V] = opened in the research run. [M] = snippet or memory only.

**Foundations**
- [V] Vygotsky (1978) Mind in Society ch. 6, via secondary page. https://newlearningonline.com/new-learning/chapter-8/vygotsky-on-the-zone-of-proximal-development (a01, a02)
- [M] Vygotsky mental-age example, Thought and Language (a03). Same URL.
- [V, secondary] Wood, Bruner and Ross (1976), via study note. https://cognito.org/courses/alevel/psychology/ocr/notes/TVVOTnlPTHA/13.8-wood-et-al.-1976-tutoring-problem-solving (a04-a06, a26). Original [M]: https://doi.org/10.1111/j.1469-7610.1976.tb00381.x (b14, c26, d18)
- [V] Stone (1998) The metaphor of scaffolding. https://www.sfu.ca/~jcnesbit/EDUC220/ThinkPaper/Stone1998.htm (a07)
- [M] Cazden (1979), via Stone snippet (a08). Same URL.
- [M] Wass and Golding (2014). https://www.bohrium.com/paper-details/scaffolding-and-the-zone-of-proximal-development-a-problematic-relationship/812561405390618629-7328 (a24)
- [M] Wood and Middleton (1975). https://doi.org/10.1111/j.2044-8295.1975.tb01454.x (b15, d17)
- [M] Pea (2004). https://doi.org/10.1207/s15327809jls1303_6 (b17)
- [M] van de Pol, Volman, Beishuizen (2010). https://doi.org/10.1007/s10648-010-9127-6 (d17)
- [V, via Wikipedia] Kirschner, Sweller, Clark (2006). https://en.wikipedia.org/wiki/Instructional_scaffolding (a25)
- [M] Kalyuga et al. (2003) expertise reversal. https://doi.org/10.1207/S15326985EP3801_4 (b16)
- [M] Rosenshine and Meister (1994). https://data.zhenzhi.com/details/1/1004933186 (a11)

**Human meta-analyses and trials**
- [V] Belland et al. (2017), Europe PMC. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC5347356&format=json&resultType=core (a09); journal page [M] https://journals.sagepub.com/doi/abs/10.3102/0034654317723009 (b10)
- [V] Belland et al. (2017) Bayesian network meta-analysis. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC5673014&format=json&resultType=core (a10)
- [V] Kim, Belland, Walker (2018). https://pure.psu.edu/en/publications/effectiveness-of-computer-based-scaffolding-in-the-context-of-pro/ (b09)
- [V] Lazonder and Harmsen (2016), via German summary. https://www.clearinghouse.edu.tum.de/wp-content/uploads/2018/12/CHU_KR-5_Lazonder-Harmsen_2016_Forschendes-Lernen.pdf (b08)
- [V] Nickow, Oreopoulos, Quan (2020). https://www.nber.org/papers/w27476 (b07)
- [M] VanLehn (2011). https://doi.org/10.1080/00461520.2011.611369 (b11)
- [M] Ma et al. (2014). https://doi.org/10.1037/a0037123 (b12)
- [M] Alfieri et al. (2011). https://doi.org/10.1037/a0021017 (b13)
- [V] Wang et al., Tutor CoPilot. https://arxiv.org/pdf/2410.03017 (a16, a17, b01-b03, c17)
- [V] Bastani et al. (2025) PNAS. https://www.pnas.org/doi/10.1073/pnas.2422633122 (b05, b06); SSRN https://papers.ssrn.com/abstract=4895486 (c18); full text https://doi.org/10.1073/pnas.2422633122 and correction https://doi.org/10.1073/pnas.2518204122 (d01, d02)
- [V] Kestin et al. (2025). https://www.nature.com/articles/s41598-025-97652-6 and https://doi.org/10.1038/s41598-025-97652-6 (b04, d16)

**LLM tutoring and hints**
- [V] Macina et al., MathTutorBench. https://arxiv.org/abs/2502.18940 (c01-c03)
- [V] Liu et al., GuideEval. https://arxiv.org/abs/2508.06583 (c04, c05)
- [V] Dinucu-Jianu et al. https://arxiv.org/pdf/2505.15607 (b26)
- [V] Scarlatos et al. https://arxiv.org/abs/2503.06424 (b27, c19)
- [V] Wei et al., UCO. https://arxiv.org/abs/2511.08873 (b28, c06, c07)
- [V] Yu, Lee, Feng, STRETCH. https://arxiv.org/pdf/2609.18642 (b29)
- [V] Hossain et al., HintMR. https://arxiv.org/abs/2604.12229 (c08-c10, d03-d05)
- [V] Kim et al., SMART. https://arxiv.org/abs/2504.09923 (c11, c12)
- [V] Dong et al., ZPD-SCA. https://arxiv.org/abs/2508.14377 (c13, c14)
- [V] Figueiredo (2025). https://arxiv.org/abs/2508.06754 (a15, c15)
- [V] Cohn et al., Inquizzitor. https://arxiv.org/abs/2508.01503 (c16)
- [V] Cui and Sachan (2025). https://arxiv.org/pdf/2502.06990 (a12, a13); not independently confirmed by any API
- [V] Liu et al. (2024) multimodal tutoring. https://arxiv.org/pdf/2404.03429 (a14)
- [M] Zhao, Hsu, Huang (2024). https://ira.lib.polyu.edu.hk/bitstream/10397/108326/1/zhaohsuhuang.pdf (a18)
- [V, abstract] Jurewicz et al., LearnLM. https://arxiv.org/abs/2412.16429 (a23)
- [V] Acquaye et al. https://arxiv.org/abs/2601.09953 (c24)
- [V] Wu et al. https://arxiv.org/abs/2505.19997 (c25)
- [V] Saha, Hase, Bansal. https://arxiv.org/pdf/2306.09299 (b24, b25)
- [V] Burns et al. https://arxiv.org/pdf/2312.09390 (b23)
- [V, abstract] Magister et al. https://arxiv.org/abs/2212.08410 (a22)
- [V] Zhou et al., least-to-most. https://arxiv.org/abs/2205.10625 (c20)
- [V] Zheng et al., Progressive-Hint Prompting. https://arxiv.org/abs/2304.09797 (d15)

**LLM memory and lessons**
- [V] Shinn et al., Reflexion. https://arxiv.org/abs/2303.11366 (a19, c23)
- [V] Zhao et al., ExpeL. https://arxiv.org/abs/2308.10144 (a20, b19, b20, c22, d14)
- [V] Wang et al., Voyager. https://arxiv.org/abs/2305.16291 (a21, b18, c21)
- [V] ReasoningBank. https://arxiv.org/abs/2509.25140 (b21, d06, d07)
- [V] Suzgun et al., Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (d08-d10)
- [V] Zhang et al., ACE. https://arxiv.org/abs/2510.04618 (d11, d12)
- [V] Wang et al., Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (d13)
- [V] Huang et al., self-correction. https://arxiv.org/pdf/2310.01798 (b22)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 10 established claims: 6 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A14.07-K05** (now single-source: the sources are not independent). g=0.46 (144 studies, 333 outcomes), g=0.385 and the 2017 no-fading-effect finding are confirmed, but both meta-analyses are by the same Belland/Walker/Kim group, and no listed source mentions a 2014 preliminary version finding adaptive fading better.
- **A14.07-K11** (number corrected). UCO reports answer leakage of 35.2% for GPT-4o (33.1% is its solve rate), 46.6% for DeepSeek-V3 and 61.0% for Qwen2.5-72B, not 33-35% for large general models. Corrected claim: Strong problem solvers are poor scaffolders and stock LLMs leak answers: Qwen2.5-Math-7B scores 0.88-0.91 on problem solving but only 0.06 win rate on scaffolding generation (MathTutorBench); large general models leak the solution in 35-61% of tutoring dialogues in UCO (GPT-4o 35.2%, DeepSeek-V3 46.6%, Qwen2.5-72B 61.0%); education-tuned SocraticLM scores low on error perception (0.14 in GuideEval).
- **A14.07-K18** (reworded: the sources support less). Small-model clause is wrong for Claude 3.5 Haiku (AIME 2024 10.0 to 36.7 with DC-Cu, AIME 2025 0.0 to 13.3); only GPT-4o-mini falls below baseline and Haiku's GPQA gain is small. Corrected claim: Stored lessons act as self-scaffolds: Reflexion HumanEval 91% vs 80% (GPT-4 baseline); ExpeL insights and retrieved trajectories combine; ReasoningBank +8.3 points on WebArena overall (40.5 to 48.8, Gemini-2.5-flash) and 55.1 vs about 42 for no-memory best-of-5 on Shopping; Dynamic Cheatsheet doubled Claude 3.5 Sonnet on AIME 2024 (23.3 to 50.0) but about half of that came from the empty-memory prompt (36.7); Voyager skill library. Majority vote of 3 gave no gain (23.3). Smaller models are mixed: GPT-4o-mini falls below baseline on AIME 2024 (16.7 to 13.3), while Claude 3.5 Haiku gains on AIME but little on GPQA.
- **A14.07-K20** (reworded: the sources support less). ACE gains persist without ground-truth labels when execution outcomes supply feedback (57.2 vs 42.4), so gains do not require oracle labels; they require a reliable external signal. Corrected claim: Intrinsic self-review without an outside signal does not help and lowers accuracy (Huang et al.: GPT-3.5 gains only with oracle labels, e.g. GSM8K 75.9 to 95.5); in agent settings ACE and Dynamic Cheatsheet gain with execution feedback even without ground-truth labels but may degrade without any reliable feedback signal, so lessons need an external signal.
