# Piagetian and neo-Piagetian stages: deep document

*Subfield A14.06. Status for the schema: background only. Evidence files: evidence_a-d.jsonl (ids a01-a29, b01-b25, c01-c25, d01-d18). Claims: claims.jsonl (A14.06-K01 to K28). Weak spots: critique.md. Many founding-study numbers are second-hand (Wikipedia or later papers); they are marked as such.*

## 1. What it is

Piaget said children pass through four fixed stages of thinking: sensorimotor, preoperational, concrete operational, formal operational. Each stage is a new way of organising knowledge. Change happens by assimilation (fit new input into an existing schema) and accommodation (change the schema when it fails). [a01]

Neo-Piagetians keep the stages but ask what drives the jump from one to the next. Their answer is a growing processing limit: working-memory units (Pascual-Leone, Case), the number of related dimensions held at once (Halford), skill levels (Fischer), speed and control (Demetriou), or hierarchical complexity of task orders (Commons). [a03, a05]

Why it is in our study: the field gives (1) a vocabulary for load limits and prerequisites, (2) a long record of how task framing changes measured ability, and (3) a set of tasks (conservation, false belief, n-back, balance scale, relational complexity) now used to test language models. It does not give the agent a new operator. It is a source of test items and warnings.

Main message in one line: the age at which a child "has" an ability depends heavily on how the task is built. The same holds for LLMs.

## 2. History and theories in depth

**Piaget (1936 to 1970s).** Stages and approximate ages, from a secondary summary [a01]:
- Sensorimotor, birth to 24 months, six substages (0-6 weeks, 6w-4m, 4-8m, 8-12m, 12-18m, 18-24m).
- Preoperational, about 2 to 7 years.
- Concrete operational, 7 to 11 years.
- Formal operational, from 11, final at 14 to 15.

Classic tasks:
- Object permanence. Stage 3 (4-8 m): reaches for partly hidden objects only. Stage 4 (8-12 m): finds hidden objects but makes the A-not-B error. Stage 6 (18-24 m): errors stop. [a02]
- Conservation. Most children fail number conservation at 4-5 and pass at 6-8. Volume comes around 11. Different quantities fall at different ages (decalage). [a16]
- Three mountains (perspective taking). Child picks from 10 photos what a doll sees. Age 4 picks own view, age 6 knows others differ, ages 7-8 consistent. [a15]
- Balance scale and pendulum (formal reasoning). Ages 3-5 no grasp; 7 balances equal weights; 10 tries location by trial and error; 13-14 some use weight times distance. Most under 12 cannot isolate pendulum variables. [a17]

**Challenges to the stage ages.** Every task was made easier and the age fell:
- Conservation: asking the question once, after the change, helps (Rose and Blank 1974; Samuel and Bryant 1984). A "naughty teddy" makes the change by accident and four-year-olds show conservation (McGarrigle and Donaldson 1974). [a16, b16, b17, b18, d14]
- Perspective taking: with a policeman-doll hiding game 90% of 3.5-5 year-olds succeed (Hughes 1975); Borke (1975) reports 3-year-olds correct 79% and 4-year-olds 93% (snippet, unverified). [a15, d15]
- Object permanence: looking-time studies show surprise at impossible events at 3.5 to 5.5 months (Baillargeon), against Piaget's 9 months for reaching. [a09, a10]

**Core knowledge and nativist reading.** Early looking-time success was read as innate knowledge of objects. This is the main rival to Piaget and is outside this subfield except where it touches the evidence on looking time.

**Neo-Piagetian programmes** [a03, a04, b15]:
- Pascual-Leone: mental power about 1 unit at age 2-3, +1 about every second year, max 7 at age 15.
- Case: four stages: sensorimotor 1-18 m, interrelational 18 m-5 y, dimensional 5-11 y, vectorial 11-19 y; adds efficiency of operations.
- Halford: relational complexity. Unary about age 1, binary 3, ternary 5, quaternary about 10. Soft limit at one quaternary relation (four arguments). Segmentation (serial) and chunking (collapse) work around it. [a06]
- Fischer: skill tiers: single representations about 2 y, mappings 3.5-4.5, systems 6-7, abstractions 10-12, then 14-16 and 18-20.
- Demetriou: spatial WM about 3 units at 6 and 5 at 12; math WM about 2 and 4; WM with executive operations about 1 and 3. Object recognition about 750 ms at 6 vs 450 ms adult; conflict resolution about 2000 ms at 6 vs 750 ms adult. Speed-intelligence links peak near 2-3, 6-7, 11-13 years. [a04]
- Commons: 16 orders of hierarchical complexity. About 20% perform at order 11 (systematic) unaided, about 1.5% above. Contested, authors' own figures. [a05]

**Modelling tradition.** Connectionist and constructive networks show that stage-like jumps can come from continuous learning: McClelland's 1989 balance scale net (Rule I, II, III; no Rule IV without help), Schapiro and McClelland 2009, Shultz's cascade-correlation conservation model (1996). [a13, a14, c21, c22]

**Capacity versus control debate.** Cowan (2016): span grows steadily from 4 to 15; adults hold 3-4 chunks, young children 2-2.5. But strategies, knowledge, speed and attention control also grow. Looking tasks credit infants with about 3 items. No decisive experiment separates the accounts. He ends by naming attention control in filling slots as a leading factor. [b12, b13, b14]

## 3. Core findings with exact numbers

Status as in claims.jsonl. "2nd" means second-hand (summary page or later paper).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Stage ages are task-dependent | conservation 6-8 y vs teddy version at 4 y; mountains 7-8 y vs policeman doll 90% at 3.5-5 y; permanence 9 m (reach) vs 3.5-5.5 m (look) | a01, a15, a16, a29 (2nd) | established (K01) |
| One question beats two in conservation | Samuel and Bryant 1984: ages 5-8, mass and volume; one-question condition fewer errors. N=252, 3 conditions per summaries only | d14 (abstract opened), b17 (snippet) | established, means unverified (K02) |
| Drawbridge looking time, 4.5 m | N=24: impossible 29.2 s (SD 20.6) vs possible 17.7 s (SD 13.1), F(1,126)=14.48, p<.001; control about 15-16 s | a10 Baillargeon 1987 | primary, contested reading (K03) |
| Drawbridge, 3.5 m | 40 tested, 12 did not habituate; fast habituators 23.78 vs 14.68 s, F(1,189)=7.38; slow 23.45 vs 27.68, no effect | a10 | primary, post hoc split |
| Bogartz alternative to drawbridge | Exp 1 N=36; Exp 2 N=52, 3 vs 7 familiarisation trials, trial contrast F(1,48)=26.99; model R2=.624; possibility parameter F(1,104)=.0097, p=.92 | a11, d08 | contested (K03) |
| Multi-lab object-permanence replication | none found | d17, d18 | gap |
| A-not-B depends on cue and delay | N=108 nine-month-olds, 2 delays x 3 cues, 18 per cell; cue F(2,102)=7.69 p<.001; delay x cue F(2,102)=3.38 p<.05; A-trial accuracy 90% vs 82% | a12 Clearfield 2009 | established (K04) |
| Infant false-belief VoE fails to replicate | Powell 2018: 21.0 vs 18.3 s, P>0.1; 18.1 vs 16.5 s, P>0.3. Wenzel 2020: chance in 48 17-month-olds and 48 3-year-olds | d06, d07 | established (K28) |
| Helper-hinderer multi-lab replication | 37 labs, 1,018 tested, 567 usable; BF01 over 100 (informative prior), 10.23 (noninformative); prior meta-analysis 0.64 preference | b20 | single-source; social, not Piagetian (K20) |
| Balance scale, continuous not abrupt | 314 children aged 6-10; flags: hysteresis 2.23%, sudden jump 8.28%, Maxwell 3.50%; 30 nets, 1680 sessions, chi2(5)=28.64 | a13 | established (K21) |
| Working-memory growth | span rises from 4 to 15; digit span +24% across school years, low-association words +5% (Dempster 1978) | b12 | contested (K05) |
| Relational complexity fits some tasks | Goswami analogy: age 4 86%, age 3 70%, binary baseline 67%; fractions 4 y 87%, 3 y 54% | a06 | contested (K06) |
| Pascual-Leone M linearity | N=215 aged 5-12; estimates above predicted scale; partly supports linear growth | d16 (snippet) | unverified |
| CogLM: GPT-4 at adult level on text Piaget items | 1,220 items, 10 abilities, 4 stages (150/200/310/560 items). Calibrated acc: GPT-4 84.7 (age 20.0), GPT-3.5 64.0 (16.1), Llama-2-70B 54.6 (14.1), OPT-6.7B 15.5 (6.5), OPT-125M 7.1 (4.8), human 93.7 (21.5). 207 questionnaires, 141 valid, ages 6-20; Spearman 0.7169; held-out 0.9354 | a20, b01, c02 | single-source (K12) |
| CogLM per ability | GPT-4 vs human: constancy 96.0 vs 100; conservation 90.4 vs 98.2; reversibility 78.7 vs 92.0; induction 78.7 vs 91.6; hypothetico-deductive 99.4 vs 100; propositional 61.0 vs 82.0; planning 59.4 vs 95.6; GPT-3.5 planning 6.7; empathy 90.3 vs 84.2 | c03, b02 | single-source (K12) |
| CogLM prompting | GPT-3.5: base 64.0, CoT 64.3, SC 64.4 (T0.3), 63.1 (T0.7). Chain-of-Cognition on Llama-2-chat-7B 31.0 to 38.1 | a21, b03, c04 | single-source (K13) |
| CogLM ability erasure | erasing semiotic function cut GPT-3.5 GSM8K by 25.5 pts (base 59.9); StrategyQA base 65.2 | b04 | single-source; tests prompt compliance, not removal |
| ConserveBench (5 VLMs) | 365 items; GPT-4o 97.44% transformational, 31.22% single-image, 22.11% number; all models at or below 38% | a22, b05, c05 | established with K08 (K11) |
| ConservationBench (112 VLMs) | 23,040 trials; humans 98.35% (6 adults). gemini-2.5-pro conserve 94.33 / control 43.88; gpt-5 91.48 / 35.82; claude-sonnet-4-5 75.43 / 45.39. 82/112 (73.2%) below 10% strict; 3 above chance 33.3%; conserve vs control r=-0.510 | a23, b07, c06 | single-source (K08) |
| Bias to answer "Conserve" | blank image 85.7% Conserve; text only 73.7%; real images about 60%; "don't know" option kept bias (r=0.591 blank, 0.362 text) | c07, d10 | single-source (K22) |
| Scale does not fix conservation | R2=0.019 over 1B-76B for conservation accuracy; R2=0.239 only for non-conserving control items (correction of b08) | c07, critique | single-source (K09) |
| CoT hurts number/length conservation | F(3,333)=18.28, p<.001; frame count p=0.416; volume/size no prompt effect p=0.114 | c07 | established with CoreCognition (K10) |
| CoreCognition | 1,503 items, 12 abilities, 230 models, 11 prompts, 2,530 data points. Human 86.98; GPT-o1 74.91; GPT-4o 69.25; Qwen2.5-VL-72B 68.29. Permanence: human 88.10, InternVL3-78B 64.37, Gemini-1.5-Pro 59.56, GPT-4o 52.86, Qwen2.5-VL-72B 43.38, Claude-3.5-Sonnet 32.43 (not re-checked). Lower-stage gaps 15.91, 21.57, 22.53 | a18, c08 | established (K14) |
| Reasoning models do not help | no significant gain on 10 of 12 abilities; perspective taking worse (P=0.0037); instruction prompt over +6% | c09, a18 | established (K10, K15) |
| Concept Hacking | 45 paired items; almost no model equal on original and flipped | a19, b11, c09 | single-source |
| CogDevelop2K | 2,519 items (1,677 single, 842 multi frame); GPT-family sensorimotor 0.4-0.6, concrete 0.2-0.4, formal 0.6-0.8; concept prompt GPT-4o High 0.555 to 0.636 | c10 | single-source; model count differs 46 vs 48 |
| Working memory: n-back | GPT-3.5 verbal d' about 1 at n=3; H=58.54, p=1.94e-13; GPT-4 H=52.51, above 1 to n=3; 50 blocks of 24 trials per n; open 6-13B no n effect | a24, c18 | single-source (K18) |
| Strong memory, weak control | operation span 0.92-0.99 vs human 0.53; reading span 0.66-0.98 vs 0.48; 3-back 0.67-0.85 vs 0.75; flanker incongruent 0.40-0.60 vs 0.93-0.96; WCST 0.29-0.53 vs 0.77; params vs span r=0.82; backward span d=15 0.21 (Gemma-9B) | a25, c17 | established with a24 (K17) |
| Reasoning fixes interference, not rule switching | flanker Llama-8B 0.471 to 0.910; Qwen2-32B 0.638 to 0.985; WCST no gain; traces often unfinished at 30,000 tokens | d13 | single-source (K24) |
| Private-item working memory | 17 LLMs fail number guessing and yes-no deduction (GPT-4o 173/200 contradicted; GPT-4o-mini 200/200); math magic GPT-4o 2.0% to 20.7% with CoT; o3-mini 96.7%, R1 100% | c16 | single-source |
| Relational complexity in LLMs | Raven/tensor accuracy -45% from RC 3 to 9; phylogeny -93% from RC 5 to 20; biology B1 35% at 4 taxa to 1% at 25; RC explains 24/32/44% of variance (Claude/Gemini/GPT); chemistry 65.7/38.1/26.0 | b24, c19, d11, d12 | single-source (K07, K25) |
| Inference-time fixes for RC | token budgets 4,096 to 16,384: +0.4% (chemistry), +2-3% (A4/A5); one-shot ICL +6.6, +3.4, +6.0; RDKit tool C3 recall 0.094 | c20, d12 | single-source |
| False belief and framing | clean items CoT +22.4 (67.2 to 89.6); perturbed +3.9 (49.9 to 53.8); some perturbations -12.1; 1,088 questions, 6 open chat models | d05 | single-source (K27) |
| Persona simulation | GPT-3.5/GPT-4 as ages 1-6: 1,296 trials; kappa 0.88; GPT-4 tracks child curve better but is hyper-accurate in some prompts | c11, c12 | single-source (K16) |
| Age-label prompting | GPT-5.4 age-label: 0.53 at 7, 0.46 at 13, 0.52 at 16; Spearman -0.40; skill-guided 0.41 to 0.50, Spearman 1.00 | c14 | single-source (K16) |
| Early false-belief LLM tests | Kosinski: davinci 10%, GPT-3.5 35%, GPT-4 90%; Sap: GPT-3 up to 60% (second-hand) | c13 | second-hand |
| Least-to-most vs CoT | SCAN length 99.7 vs 16.2 (CoT) vs 16.7 (standard); GSM8K 62.39 vs 60.87; 5-step GSM8K 45.23 vs 39.07; DROP football 73.42 vs 59.56 | d09 | single-source, 2022 model (K23) |
| Piaget-inspired agent memory | PISA LOCOMO 63.58 vs Mem0 55.51 vs full context 68.47 (first judge); updated judge PISA 74.80 at 2.1k tokens, full context 74.02 at 21.09k, Mem0 64.21; CAM NovelQA 52.3 vs 47.8 | c23, c24, d02 | single-source, own benchmarks (K19) |
| Memory ablations | PISA no-init -14.28; no structure retrieval -17.64; CAM no hierarchy 46.7 vs 52.3, no flexibility 50.3; SCG-Mem no assimilation: multi-hop F1 28.49 to 18.74 (-34.2%), adversarial 52.63 to 34.33; 1B-3B models | d01, d03, d04 | established across 3 systems for parts (K26) |

## 4. Mechanisms and models

Written so an engineer could implement each as a test harness or a scaffold step. None of these is in SCHEMA.md.

**4.1 Assimilation and accommodation as a memory rule (O / memory).**
- Keep a store of schemas (named structures with slots and a short summary).
- On new input, try assimilation first: ground the input to existing schema nodes and write it into slots. Code checks the match (slot types fit, no contradiction).
- Only if the match fails (a contradiction or no fit), run accommodation: create or edit a schema, citing the input that broke the old one.
- Evidence: removing the assimilation step cut SCG-Mem F1 20-35% on 3B models [d04]. Removing hierarchy in CAM lost 5.6-11 points [d03]. Accommodation alone has never been ablated. [d01]
- This agrees with G2 (revise only from real failing output).

**4.2 Relational complexity (RC) as a load meter (G, O3).**
- RC of a step = number of variables that must be bound at once to get the next result. A step with four jointly bound arguments is at Halford's soft limit.
- Implementation: tag each problem step with its arity. If arity is above a threshold, split it by segmentation: compute a ternary part, store the result, then combine as binary. The balance scale is solved this way: two moment computations, then compare. [a08]
- LLM data: accuracy falls with RC at fixed entity count [d11], but operand complexity also matters (chemistry C1 vs C2 at RC=2: 65.7 vs 38.1) [d12], and extra tokens barely help (+0.4 pts) [c20]. So a decomposition step has to change the structure of the work, not just add words.

**4.3 Capacity versus control (G).**
- Model of a trial: items held (capacity) plus a filter that decides which held items drive output (control).
- Models store well (span 0.99) and filter badly (flanker 0.40-0.60) [a25]. A written conflict check lifts flanker to 0.91-0.985 but costs thousands of tokens. [d13]
- Rule switching (WCST) did not improve with reasoning. A candidate fix is an explicit "current rule" register updated by code when feedback arrives. Untested. [K24]

**4.4 Prerequisite-ordered prompting (O).**
- Chain-of-Cognition: answers to earlier-stage questions (written by a stronger model) are prepended to later-stage questions. Llama-2-chat-7B 31.0 to 38.1. [b04]
- Least-to-most: solve easier sub-problems first, pass answers forward; strong on length generalisation, small on GSM8K. [d09]
- Neither is equal-token tested on a modern reasoning model. Gap 1 stays open.

**4.5 Response-bias control (G).**
- Run each item as a matched pair: the item and a version where the right answer differs. Score both. A model that answers "Conserve" on blank input is using a prior. [d10]
- Report accuracy only on pairs, never on single items. ConservationBench: a model can look good on conserving items (94%) and fail controls (44%). [c06]

**4.6 Dynamic field account of A-not-B (background).**
- Reach choice = competition between a memory trace of past reaches and the strength of the new cue. Stronger cue or shorter delay lets the new cue win. [a12]
- Lesson for agents: perseveration on a previous answer is a memory-versus-cue balance. Showing fresh evidence strongly, and delaying less, shifts it.

**4.7 Connectionist stage model (background).**
- Three-layer network on weight and distance inputs. The Rule I to Rule II shift appears gradually and matches children better than abrupt rule switching. [a13] Stages can be a description of a smooth process.

## 5. What holds up

**Holds up well**
- Task framing shifts measured ability by years: one-question conservation, teddy, policeman doll, cue strength in A-not-B. [K01, K02, K04]
- Infant false-belief looking-time and interactive tasks mostly fail to replicate. [K28]
- Stages as sharp, simultaneous steps do not hold; continuous models fit better. [K21]
- LLM capacity is high, control is low. [K17]
- CoT is not a general improvement, especially on perceptual tasks. [K10]
- LLM developmental order differs from the human one. [K14]

**Contested**
- Infant looking time as proof of object permanence. The Bogartz account (familiarity and novelty, trial number flipping the direction) fits data with the possibility parameter at p=.92. Knowledge-account researchers dispute it; no multi-lab replication exists. [K03]
- Whether growth in working-memory capacity drives stage change, or attention control, strategies and knowledge do. [K05]
- Whether neo-Piagetian ladders are real. The arity of each task is assigned by theorists and binary shortcuts can solve some tasks. [K06]
- Stage labels in LLM benchmarks (CoreCognition and CogDevelop2K give reversed orders; both use authors' own mapping). [K14]

**Failed or weak**
- The infant helper-preference claim failed a 37-lab replication. [K20]
- CoT and self-consistency gave no gain on CogLM GPT-3.5. [K13]
- Reasoning models gave no gain on 10 of 12 CoreCognition abilities, and worse perspective taking. [K10]
- Extra test-time compute did not fix relational complexity limits. [c20]
- Age-label prompting (tell the model it is 7) gave flat or wrong trajectories, Spearman -0.40. [c14]

**Moderators**
- Number of questions asked; who makes the change (teddy); cue salience; delay; habituation speed; trial number; perturbation of task wording (LLM false belief); blank vs real images; scoring rule (strict pairwise vs average).

**Interventions that worked**
- Concept-explanation or cognitive-instruction prompt: over +6% (CoreCognition); GPT-4o High 0.555 to 0.636 (CogDevelop2K). [K15]
- Chain-of-Cognition on a small model (+7.1). [b04]
- Reasoning trace for flanker (+0.44 absolute for Llama-8B). [d13]
- Assimilate-first schema memory (ablation: 20-35% F1 loss when removed). [d04]
- Least-to-most for length generalisation. [d09]

**Interventions that did not work**
- CoT and self-consistency on CogLM GPT-3.5. Reasoning models on most CoreCognition abilities. CoT on number and length conservation (worse). Test-time compute on RC (+0.4). Reasoning on WCST. "I don't know" option on conservation bias. Frame count, prompt variants and parameter scale on conservation. RDKit tool on the highest-RC chemistry task.

## 6. Language models

**Text benchmarks (CogLM).** GPT-4 reaches about the 20-year-old level (84.7 vs 93.7 for adults). It is far below humans on planning (59.4 vs 95.6) and propositional operations (61.0 vs 82.0), and above on empathy (90.3 vs 84.2). Scores rise with parameter count and chat tuning (OPT 125M 7.1, Llama-2-7B 20.5, GPT-3.5 64.0). The reported Llama-2-70B base and chat value are identical (54.6), a likely table error. The human sample (141, ages 6-20) is small and the age scale is extrapolated beyond 20. [a20, c02, c03]

**Vision-language conservation.** Two studies from related authors point the same way: models pass tasks where the change is shown (GPT-4o 97.44%) and fail static judgments (31.22%; number 22.11%). In 2026, across 112 VLMs, top models score 94% on conserving and 36-45% on non-conserving videos. The failure is mostly a prior: blank images give 85.7% "Conserve", text only 73.7%, real images about 60%. So it appears without images. Pure perception is not separated. Scale gives R2=0.019. [a22, a23, d10]

**Core knowledge.** CoreCognition: 230 models, human mean 86.98, best model 74.91. Weakest are low-stage abilities (permanence: GPT-4o 52.86 vs human 88.10). Perspective taking gets worse with scale and with reasoning training. Concept Hacking shows shortcuts: few models are equal on flipped items. In people early abilities support later ones. In models, sensorimotor abilities correlate weakly with later ones (many correlations under 0.4), so the dependency is missing. [a18, a19, b10]

**Working memory and executive control.** n-back limit near 3 for GPT-3.5; GPT-4 stays above d'=1 to n=3. Span tasks beat humans (operation span 0.92-0.99 vs 0.53). Control is weak: flanker incongruent 0.40-0.60, WCST 0.29-0.53. Reasoning fixes flanker, not WCST. LLMs also fail tasks needing a private held item (yes-no deduction, GPT-4o 173/200 contradicted), unless CoT or external memory is used or the model is a reasoning model (o3-mini 96.7% on math magic). [a24, a25, d13, c16]

**Relational complexity.** Accuracy falls with arity in three frontier models; compute and tools do not remove it; one-shot examples add 3-7 points; operand complexity is a second driver. [d11, d12]

**Theory of mind.** CoT gives +22.4 on clean false-belief items but +3.9 on perturbed ones, and hurts on some. Only older open chat models were tested; newer reasoning models are untested. [d05] Earlier generations: davinci 10%, GPT-3.5 35%, GPT-4 90% (second-hand). [c13]

**Persona and age steering.** GPT-4 playing 1-6 year olds downplays knowledge; corpus-primed prompts match age best. Telling a model "you are 13" does not produce a monotone age curve; skill-guided prompts do (Spearman 1.00). [c11, c12, c14]

**Agents inspired by Piaget.** PISA, CAM and SCG-Mem add schema memory. PISA matches full context on LOCOMO with a loose judge (74.80 vs 74.02) at one tenth of the tokens (2.1k vs 21.09k). Part ablations show gains; the accommodation step has no ablation. [d01-d04]

**What no study has done.** No LLM and child tested on the same conservation or seriation task. No equal-token test of a stage-ordered scaffold. No test of RL-trained reasoning models on false-belief perturbations. A November 2025 preprint linking LLM cognition to developmental theory was not opened (403). [a27]

## 7. What our agent should take

This subfield is background only. Items below are mostly confirmations of existing rules plus a few cheap tests. Evidence ids in brackets.

### Add now (established)

1. **Do not assume CoT is better on every item type.** Perceptual and state-judgment items can get worse with long reasoning. Matches G11 and G12; add item type as a reason to route to direct mode in S0. Schema part: G11 / S0. [E] K10. Evidence c07, b09, c09.
2. **State the governing concept in one line before answering, where the item has a named concept.** Modest gain (over +6%; +0.081 for GPT-4o). Schema part: O / S2 (REPRESENT already restates the task; add "name the principle"). [E] K15. Evidence b09, c09, c10. Gains are on multimodal QA; confirm size on our bench before relying on it.
3. **Assimilate-first memory.** Lessons and subgoal-library entries are first matched to an existing entry; only a failed match creates or edits one. Schema part: memory (section 5, S9). [E] K26 (three systems, own benchmarks, small models). Evidence d01, d03, d04. Fits G2.
4. **Probe low-level skills directly; do not assume them.** A strong model can fail a simple conservation or permanence check. Add to the section 6 logging rule: record failures on the simplest item of each class. Schema part: G (S0 class record). [E] K14. Evidence a18, b10, c08, c10.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Prerequisite sub-answers fed in order vs plain CoT at equal tokens on a strong model | O3 Decompose | [S] K13, K23 | b04, d09 |
| One-line conflict check on flanker-like items (reasoning fixes it but costs thousands of tokens) | G11 / S2 | [E] direction K17, [S] fix K24 | d13, a25 |
| Explicit "current rule" register for rule-switching tasks | S5/S6 state line | [S] K24 | d13, a25 |
| Split high-arity steps into ternary then binary parts, log RC | O3 / S2 | [S] K07, K25 | d11, d12, a08 |
| External scratch list for n-back-like dependency tracking | memory | [S] K18 | a24, c16 |
| Accommodation-only vs assimilate-first vs always-write memory | memory | [S] K26 (gap) | d04 |
| Perturbed social-reasoning items in the bench | G | [S] K27 | d05 |
| Ask-once vs repeated-clarify loop; count answer flips | G1 / S1 | [S] K02 (human data only) | a16, d14 |
| Answer-bias check: blind (no evidence) "no change" rate; paired scoring | G3 / bench | [S] K22 | d10 |

## 8. Concrete tests on our bench

All arms at equal total tokens. Report per class and log per-state tokens.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Multi-step problems with a chain of prerequisites (GSM8K-hard, multi-hop) | A: plain CoT. B: prerequisite sub-answers first, each fed forward. Equal tokens | Accuracy, tokens per correct | Small on easy items (about +1.5 on GSM8K per d09); larger on 5+ step items (+6) and length generalisation. A null is likely on a strong model. |
| T2 | Rule-switching items (WCST-style, rule changes mid-item) | A: plain reasoning. B: code-held current-rule register shown at each step | Accuracy vs 0.29-0.53 baseline | Medium if the failure is state tracking; none if it is a model limit |
| T3 | Interference items (distractors, misleading cue) | A: direct. B: one-line conflict check. C: long reasoning | Accuracy, tokens | B near C accuracy at far fewer tokens if the check is the active part |
| T4 | High-arity relation items (n bound variables, fixed entity count) | A: direct. B: stepwise binary decomposition; both capped at the same tokens | Accuracy by RC | Flatter slope with RC in B. Extra words alone (A with more tokens) should give about +0.4 |
| T5 | State-judgment items with "no change" answers (text ConservationBench analogue) | A: single items. B: paired items with blind control | Share answering "same" blind; paired accuracy | Expect strong bias toward "same"; test whether an evidence-first step lowers it |
| T6 | Multi-session memory tasks | A: always-write. B: assimilate-first. C: B plus accommodation on mismatch | F1, tokens | B and C beat A by 10%+ if d04 transfers; C over B unknown |
| T7 | Social-reasoning items, clean and perturbed | A: plain. B: CoT. C: scaffold | Accuracy by perturbation type | CoT gain shrinks from +22 to +4 under perturbation |
| T8 | Named-concept items (physics or maths with a core principle) | A: no hint. B: concept stated first, same total tokens | Accuracy | +3 to +8 |
| T9 | Dependency tracking (n-back style over long context) | A: in-context only. B: external list updated by code | d', accuracy by n | Large at n>=3 if memory is the limit |

## 9. What does not transfer, and why

- **Stage order as a curriculum.** Children need early abilities to build later ones. LLM abilities do not stack that way; low-level correlations with high-level are weak (many under 0.4). A stage-ordered syllabus is not warranted. [b10]
- **Age labels.** Prompting "you are 7" does not yield a stable age profile (Spearman -0.40). Our agent has no developmental age. [c14]
- **Infant looking-time claims.** Contested and partly failed to replicate; no agent analogue. [K03, K28]
- **Maturation as capacity growth.** Our context window is not a working-memory growth process. LLM span is near perfect on digits and fails on control. Neo-Piagetian capacity numbers (1 to 7 units) do not map to tokens. [a25]
- **Ability erasure by prompt.** CogLM erasure tests prompt compliance, not removal of a capacity. [b04]
- **Human-calibrated age scores for LLMs.** The age map is a regression fit on ages 6-20, extrapolated to 20+. Do not quote "GPT-4 is 20 years old". [a20, c02]
- **Stage labels for adult sentence completion (Kegan DSCT).** Different theory; larger models write text rated at higher stages; no person-level claim. [b25]
- **Commons' orders as a measure of the agent.** Contested measure, authors' own percentages. [a05]
- **Safety by child stage (ChildSafe).** Internal inconsistencies in counts and scores (240 vs 1,200 responses). Not reliable. [c15]

## 10. Open questions

1. Does a stage-ordered scaffold beat plain CoT at equal tokens on a strong model? Only a small-model result (31.0 to 38.1) and a 2022 non-token-matched result exist.
2. Is the conservation failure a perceptual deficit or only a response prior? Text-only 73.7% says mostly prior; no shuffled-image control.
3. What is the token cost of the conflict check that fixes flanker items, and is there a shorter form?
4. How much of the RC drop is arity itself versus operand complexity? C1 and C2 share RC=2 and differ by 27.6 points.
5. Does schema revision (accommodation) alone add anything? No ablation exists.
6. What are the original numbers for the 1956 mountains study, Samuel and Bryant means (N=252 unverified), and Pascual-Leone M-power tables?
7. Does the drawbridge result survive a multi-lab replication? None found.
8. How do RL-trained reasoning models behave on perturbed false-belief items? Perspective taking worsens with reasoning in CoreCognition (P=0.0037).
9. Why do CoreCognition and CogDevelop2K give reversed stage orders? Mapping, item format, or real?
10. Does a model and child result on one shared conservation task agree? No study exists.
11. What does the November 2025 Demetriou preprint show? Not opened.

## 11. Sources

[V] opened, [M] snippet or search summary only.

**Founding and human studies**
- [V] Piaget's theory of cognitive development (summary): https://en.wikipedia.org/wiki/Piaget%27s_theory_of_cognitive_development (a01, a17)
- [V] Object permanence (summary): https://en.wikipedia.org/wiki/Object_permanence (a02)
- [V] Neo-Piagetian theories (summary; Pascual-Leone, Case, Halford, Fischer, Demetriou, Commons): https://en.wikipedia.org/wiki/Neo-Piagetian_theories_of_cognitive_development (a03-a05, b15)
- [V] Three mountain problem (Hughes, Borke): https://en.wikipedia.org/wiki/Three_mountain_problem (a15)
- [V] Conservation (psychology): https://en.wikipedia.org/wiki/Conservation_(psychology) (a16, a29, b16)
- [V] Halford, Wilson and Phillips 1998: https://www.cmu.edu/dietrich/psychology/memorylab/publications/98_jra_cl_mcl_lmr.pdf (a06-a08); [M] Cambridge page: https://core-cms.cambridgecore.org/core/journals/behavioral-and-brain-sciences/article/processing-capacity-defined-by-relational-complexity-implications-for-comparative-developmental-and-cognitive-psychology/D2388E89B8614A0605D9EE55C6E47F18 (b21)
- [V] Baillargeon 1987 (and 1985 as described): https://princetonuniversity.github.io/NEU-PSY-502/_static/pdf/Class%2021/baillargeon1987.pdf.pdf (a09, a10)
- [V] Bogartz, Shinskey and Schilling 2000: https://repository.royalholloway.ac.uk/items/2311a455-f0fe-6428-1aa0-34d93e2a33eb/1/2000_Bogartz_Shinskey_&_Schilling.pdf (a11, d08)
- [V] Clearfield et al. 2009: https://pmc.ncbi.nlm.nih.gov/articles/PMC2888518 (a12)
- [V] Schapiro and McClelland 2009: https://stanford.edu/~jlmcc/papers/SchapiroMcC09BalScale.pdf (a13, a14, a28)
- [V] Shultz 1996 abstract: https://www.psych.mcgill.ca/perpg/fac/shultz/personal/Recent_Publications_files/conserve96_abs.htm (c21); [M] Shultz constructive networks: https://www.psych.mcgill.ca/perpg/fac/shultz/cdp/Ch4.PDF (c22)
- [V] Cowan 2016: https://memory.psych.missouri.edu/assets/doc/articles/2016/cowan-pps-2016-working-memory-maturation.pdf (b12-b14)
- [V] Anderson et al. 1998 commentary: https://www.andrew.cmu.edu/user/reder/publications/98_jra_cl_mcl_lmr.pdf (b22)
- [V] Andrews, Birney and Halford 2006: https://link.springer.com/content/pdf/10.3758/BF03193275.pdf (b23)
- [V] Samuel and Bryant 1984 (abstract only): https://doi.org/10.1111/j.1469-7610.1984.tb00152.x (d14); [M] https://scilit.com/publications/7bba97ba5b5f5f82559681158513ab62 (b17, b18)
- [M] Borke 1975: https://doi.org/10.1037/h0076459 (d15)
- [M] Neo-Piagetian M-capacity, N=215: https://doi.org/10.1016/s0160-2896(96)80006-7 (d16)
- [M] Sirois and Jackson drawbridge replication coverage: https://www.bps.org.uk/research-digest/do-babies-understand-things-exist-when-theyre-out-sight-or-dont-they (d17)
- [V] Powell et al. 2018: https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/0/2045/files/2018/11/Powell_Hobbs_Bardis_Carey_Saxe_2017.pdf (d06)
- [V] Wenzel et al. 2020: https://pmc.ncbi.nlm.nih.gov/articles/PMC7657934 (d07)
- [V] Frank et al. 2017 ManyBabies framework: https://pmc.ncbi.nlm.nih.gov/articles/PMC6879177/ (b19)
- [V] Lucca et al. 2025: https://psych.uni-goettingen.de/de/development/pdfs/developmental-science-2024-lucca-infants-social-evaluation-of-helpers-and-hinderers-a-large2010scale-multi2010lab.pdf (b20)
- [M] ManyBabies4 coverage: https://osf.io/vmnnn (d18)

**LLM studies**
- [V] CogLM (arXiv 2408.09150): https://arxiv.org/html/2408.09150v3 (a20, a21, b01-b04, c01-c04)
- [V] ConserveBench (arXiv 2410.00332): https://arxiv.org/html/2410.00332v6 (a22, b05, b06, c05)
- [V] ConservationBench (arXiv 2603.07109): https://arxiv.org/html/2603.07109v1 (a23, b07, b08, c06, c07, d10)
- [V] CoreCognition and CogDevelop2K (arXiv 2410.10855): https://arxiv.org/html/2410.10855v4 and v1 (a18, a19, b09-b11, c08-c10)
- [V] Gong et al. n-back (arXiv 2305.03731): https://arxiv.org/html/2305.03731v4 (a24, c18)
- [V] Strong Memory, Weak Control (arXiv 2504.02789): https://arxiv.org/html/2504.02789v2 (a25, c17, d13)
- [V] Language Models Do Not Have Human-Like Working Memory (arXiv 2505.10571): https://arxiv.org/html/2505.10571v3 (c16); [M] v2 search level (a26)
- [M] Demetriou et al. preprint: https://www.preprints.org/manuscript/202511.0207/v1 (a27, 403)
- [V] REL, relational reasoning (arXiv 2604.12176): https://arxiv.org/html/2604.12176v2 (b24, c19, c20, d11, d12)
- [V] Kegan-based DSCT (arXiv 2605.08549): https://arxiv.org/pdf/2605.08549 (b25)
- [V] Milicka et al. 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC10936766/ (c11-c13)
- [V] ChildAgentEval (arXiv 2605.17894): https://www.alphaxiv.org/abs/2605.17894.md (c14)
- [V] ChildSafe (arXiv 2510.05484): https://arxiv.org/html/2510.05484v1 (c15)
- [V] PISA (arXiv 2510.15966): https://arxiv.org/html/2510.15966 (c23, d01, d02)
- [V] CAM (arXiv 2510.05520): https://arxiv.org/html/2510.05520 (c24, d03)
- [V] SCG-Mem (arXiv 2604.20117): https://arxiv.org/html/2604.20117 (d04)
- [V] Nickel et al. 2026 perturbed ToM (arXiv 2602.22072): https://arxiv.org/html/2602.22072 (d05)
- [V] Zhou et al. least-to-most (arXiv 2205.10625): https://arxiv.org/pdf/2205.10625 (d09)
- [M] Backward digit span benchmark: https://escholarship.org/content/qt28m3k4g4/qt28m3k4g4.pdf (c25)

Note on duplicates: CogLM appears under three author names (Zhu, Wang, Zhao), ConserveBench under Su and Luo, CoreCognition under Li. These are one independent source each; use arXiv ids. Author names could not be rechecked.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 9 established claims: 6 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A14.06-K17** (now single-source: the sources are not independent). All numbers (operation span, flanker, WCST, flanker 0.471 to 0.910) come from one paper, de Langis et al. arXiv 2504.02789, listed three times; they match, but the other cited sources (Gong 2023, Huang 2025) do not report these figures. The tested models are open 7-70B models.
- **A14.06-K21** (reworded: the sources support less). Schapiro and McClelland model only the Rule I to Rule II transition and conclude it is typically continuous rather than discrete (a few children show larger jumps than the model); Shultz 1996 abstract lists five conservation phenomena and does not mention stage-like jumps. The N=314 and 2-8% flag percentages could not be re-read (PDF unreachable). Corrected claim: A connectionist model of the balance scale task (Schapiro and McClelland 2009) reproduces the Rule I to Rule II transition and the 'catastrophe flags' seen in Jansen and van der Maas's child data, and accounts for nearly all of it with continuous processes, consistent with the transition being typically continuous rather than discrete; a cascade-correlation network (Shultz 1996) reproduces five conservation phenomena.
- **A14.06-K26** (reworded: the sources support less). SCG-Mem's 'w/o Evolutionary Update' removes assimilation and retains only accommodation, so accommodation-alone is effectively tested (it is assimilation-alone that is untested); SCG-Mem ablation is on one model (Qwen2.5-3B), F1 drops 20.1-34.8%; CAM w/o Hierarchy drop on ODSum-S is 5.3 not 5.6, so the range is 5.3-11.0. Corrected claim: In SCG-Mem, disabling assimilation (keeping only accommodation) lowers F1 by 20.1-34.8% on Qwen2.5-3B; CAM without hierarchy loses 5.3-11.0 ACC-L points (NovelQA 5.6, QMSum 11.0, ODSum-S 5.3). PISA ablates only its initialization module and hierarchy-aware retrieval, with no ablation of its Piagetian update, and assimilation-only (without accommodation) is untested in SCG-Mem.
- **A14.06-K14** (now single-source: only one opened source, code check).
- **A14.06-K15** (now single-source: only one opened source, code check).
