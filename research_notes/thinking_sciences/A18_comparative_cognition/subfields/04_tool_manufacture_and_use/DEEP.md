# Tool manufacture and use: deep document

*Subfield A18.04 of comparative cognition. Built from evidence_a-d.jsonl (a01-a29, b01-b27, c01-c25, d01-d20), claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids are in brackets. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Tool use is holding or handling an object to change another object. Tool manufacture is changing or combining objects so they work as a tool. The field asks three questions of animals.

1. Do they make tools to a standard shape (hooked twigs, stepped pandanus leaves)?
2. Do they make a new tool when the old one is missing (Betty and the wire)?
3. Do they plan several tool steps ahead (metatools, compound tools), or do they chain actions by reacting to feedback?

The model animal is the New Caledonian (NC) crow. Other animals appear as controls: rooks, magpies, Hawaiian crows, apes, children.

Why this matters for our agent. A language-model agent that writes a helper program, tests it and reuses it is doing tool manufacture. The animal work gives three things.

- A vocabulary that separates making, choosing and using a tool.
- Tests that separate reasoning from trial-and-error learning: first-trial success, feedback removal, re-skinned transfer, out-of-sight stages. We can copy the tests.
- Warnings. A single success (N=1 Betty) is not a rule. Tool making is a minority skill in controlled replications. Learning from success explains much of what looked like insight.

The LLM side is the "library of helper tools" line: LATM, CREATOR, CRAFT, Voyager, TroVE, ReGAL, SkillCraft, ToolMaker, plus 2026 work on when to build (AllocBench) and whether models notice a tool can be built (Lomekwi).

Scope note. Prospection and planning for future needs (scrub jays) belong to the next subfield. Planning with tools is covered only as far as metatool tasks need it.

## 2. History and theories in depth

### 2.1 Wild tool making
- Hunt 1996 (Nature 379) [a09, M]: first report of free-living non-human hook tools. A hooked twig and a stepped-cut barbed pandanus leaf, both made and used to catch prey.
- Hunt 2000 [a08, abstract only]: pandanus tools show population-level handedness and rule-governed shaping. Hunt called this unprecedented in free-living non-humans, and not tied to symbolic thought or language.
- Hunt and Gray 2003 [b04, M]: 5,550 tools at 21 sites, three standard designs (wide, narrow, stepped) with overlapping ranges and a shared method. The authors infer cumulative change from a common origin.
- Emery and Clayton 2004, Science 306 [a10, a11, V]: the review that frames the subfield. Hook tools are trimmed and sculpted. Stepped tools follow a standard pattern and are carried on foraging trips. The theory is convergent evolution: corvids and apes evolved a similar "cognitive tool kit" (causal reasoning, flexibility, imagination, prospection) despite very different brains. Betty is read as reasoning by analogy from earlier hook experience. The review has no data of its own and rests on N=1 Betty for the key claim.

### 2.2 The Betty episode and its critics
- Weir, Chappell, Kacelnik 2002 (Science 297) [a01, a02, b02]: a captive female, Betty, chose between a hooked and a straight wire to lift a small bucket from a tube. On trial 5 her mate Abel took the hook. Betty wedged the straight wire under tape and bent it with her beak. The authors called it the first new tool made for a specific task without long trial and error. The long paper was cut to a one-page Brevia [a02].
- Weir and Kacelnik 2006 [a03]: Betty was given aluminium strips in three experiments. She tried her old wedge-and-bend method, it failed, and she changed one step. When unbending was needed she modified correctly on 4 of 5 trials. She died before the work was finished.
- Critique [a05]: the first bend may simply be the first manipulation tried and then reinforced (Shettleworth 2009). Field work shows wild crows bend stems routinely: 10 of 18 temporarily captive wild crows bent a new hook shaft (Klump 2015, via van Buuren). So "novel invention" is contested [K02].
- Replication, van Buuren et al. 2021 [a04]: 17 captive crows. Study 1: 3 of 10 made hooks, 1 straightened consistently. Study 2 (Z-shaped tool needing two straightenings): 4 of 10 solved at least once, 2 consistently. One crow succeeded consistently in both unbending tasks. Authors conclude trial-and-error learning prevailed.
- Rooks, Bird and Emery 2009 [a12, a13]: four hand-raised rooks, a species that does not use tools in the wild, all bent wire into a hook. Three did so on trial 1, the fourth by trial 4. Argued as a domain-general causal ability.

### 2.3 Development
- Kenward et al. 2005 (Nature 433) [a06, b03] and 2006 (Anim Behav) [a07]: four hand-reared juveniles kept from adults used and made tools. Two saw a human demonstrate; two did not. The authors saw no qualitative difference: an inherited predisposition with stereotyped object manipulation ("protoprobing").
- Rutz et al. 2016 [b15, M]: Hawaiian crows show species-wide tool use, and juveniles develop it without training.
- Reviews 2020 [b12, b13] argue the field over-weights social learning and propose baseline and social-learning conditions to separate genetic bias, individual learning and copying. Auersperg et al. 2026 [b14] argue flexible and stereotyped tool use is a spectrum, and that an intrinsic urge to combine objects underlies onset.

### 2.4 Reasoning versus learning
- Taylor et al. 2007 metatool [a17, b05]: 7 wild-caught crows, a short stick that extracts a longer stick that reaches meat. 6 of 7 tried it, 4 of 7 got meat on trial 1.
- Taylor et al. 2009 [b06]: 3 of 6 crows solved a trap-tube task and passed 4 transfers, but failed when a hole and a functional trap were both present.
- Aesop's fable paradigm, Jelbert et al. 2015 [b09, b25]: corvids pass many water-displacement tasks and fail counter-intuitive ones (U-tube). Rivals not ruled out: perceptual-motor feedback and object bias.
- Taylor, Knaebe, Gray 2012, "An end to insight?" [a14]: horizontal string pulling with no visible feedback. Humans 49/50 and 42/50. Crows did not solve it.
- Hennefield, Hwang, Weston, Povinelli 2018 [b10, b24]: pooled meta-analysis of 5 articles, over 32 experiments. Birds learn from success, not failure, and do not transfer. Builds on Ghirlanda and Lind 2017.
- Magpies [b11]: functional choices were above chance only in late trials.
- Evidence for planning: Gruber et al. 2019 [a15, a16, b08, b27] with out-of-sight stages (section 3).
- Compound tools, von Bayern et al. 2018 [b07, b26, d18]: first-trial construction and need-sensitive choice (section 3).

### 2.5 Link to AI
- Yiu, Kosoy, Gopnik 2023 [c13] set LLMs against children on tool innovation.
- Xu et al. 2023 RoboTool [a27] builds on the animal tool-use literature.
- Wang et al. 2024 STE [c14] cites Emery and Clayton for trial, imagination and memory.
- Lomekwi 2026 [c23, c24] maps curiosity, recognition and efficiency onto animal work and Voyager.
- The library line (LATM, CREATOR, CRAFT, Voyager, TroVE, ReGAL, SkillCraft) is engineering. It does not take its design from the crow work, but the questions line up (section 4).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Wild NC crows make hook and stepped tools to standard designs | 5,550 tools, 21 sites, 3 designs | Hunt and Gray 2003 [b04, M] | [E] K01 |
| Betty bent wire into a hook after her mate took the hook | trial 5 of the choice test; N=1; "9 of 10 retrievals" is Wikipedia only, unverified | Weir 2002 [a01, a02] | [C] K02 |
| Wild crows bend stems routinely | 10 of 18 temporarily captive wild crows bent a new shaft | Klump 2015 via van Buuren [a05] | [E] |
| Captive replication of bending and unbending | 17 crows; 3 of 10 made hooks; 1 straightened consistently; Z-tool 4 of 10 at least once, 2 consistently | van Buuren 2021 [a04] | [S] K03 |
| Rooks make hooks with no tool-using ecology | 4 of 4; 3 of 4 on trial 1; bucket retrieved on 35 +/- 2.9% of trials; successful bend 100 +/- 8.5 deg vs 75 +/- 4.5 | Bird and Emery 2009 [a12, a13] | [S] K04 |
| Naive juveniles develop tool manufacture | N=4 hand-reared; 2 tutored, 2 not; no qualitative difference | Kenward 2005, 2006 [a06, a07] | [E] K05 (abstract-level for 2005) |
| Metatool use | 7 crows; 6 tried; 4 of 7 got meat on trial 1 | Taylor 2007 [a17, b05] | [E] K06 |
| Compound tool construction | 8 naive crows; 4 of 8 built in test 1 within about 4-6 min; unrewarded attempts before success 0, 3, 7, 10; transfer to new materials: all 4 within 2 attempts | von Bayern 2018 [b07, b26, d18] | [E] K06 |
| Compound tool need sensitivity | uncombined tool tried first on 70.8% (food close) vs 20.8% (food distant); per-bird Fisher p 0.037, 0.001, 0.100, 0.193 | von Bayern 2018 [d18] | [E] K06 |
| Out-of-sight multi-stage metatool problems | Exp 1 N=14: 4 reached 16/20, stone problem needed 43-69 trials; Exp 2 N=8: 3 solved at 25, 26, 39 trials, a 4th at 69; Exp 3 N=3: stick 18, 17, 16 of 20, stone not passed in 20 | Gruber 2019 [a15, b08, b27] | [S] K06, K07 |
| Strict stick test | Aretha 12/14 (p=0.013), Freddie 14/18 (p=0.031); 2018 crows Saturn 20/20, Triton 16/20 | Gruber 2019 [b08] | [S] |
| Insight claim fails without feedback | horizontal string: 8/11 chose connected string on trial 1 (p=0.11); one crow completed exp 1; humans 49/50, 42/50 | Taylor 2012 [a14] | [E] K08 |
| Aesop's fable tasks | 5 articles, 32+ experiments: learn from success not failure; no transfer; magpies significant only in late trials | Hennefield 2018 [b10]; [b11] | [E] K09 |
| NC crows with no stone experience | 0 of 6 spontaneously dropped stones | Jelbert 2015 [b09] | [S] |
| LATM maker/user, GPT-3.5 user, CoT to LATM | Logical 66.4 to 79.7; Tracking 61.6 to 99.6; Dyck 20.4 to 92.2; Word Sort 59.2 to 98.3; CRT 0 to 100; Schedule 18.9 to 100 | Cai 2024 [a19, b17, c01] | [S] K10 |
| LATM, GPT-4 user, CoT vs LATM | Logical 88.8 vs 86.6; Tracking 100/100; Dyck 63.6 vs 87.5; Word Sort 90.9 vs 99.1; CRT 0 vs 100; Schedule 55.6 vs 100 | [c02] | [S] |
| LATM dispatcher | tool identification 95 +/- 2%, decision to make a new tool 96 +/- 3% (100 mixed samples, 5 sets) | [c03] | [S] |
| LATM weak maker | GPT-3.5 as maker failed 5 of 5 on Logical and Tracking; verification repaired only 2 of 60 trials | [c04, a19] | [S] K11 |
| LATM weak user | same tools, users GPT-3.5 down to ada: Logical 79.7/58.2/11.6/6.5/11.6/3.0; Tracking 99.6/100/62.1/20.7/16.4/5.2 | [a20] | [S] |
| CREATOR (ChatGPT) | TabMWP no-CoT/CoT: entangled 91.6/93.5, CREATOR 90.5/94.7, PoT+rectification 81.2/87.3, standard 68.2/75.2; MATH 59.7; Creation Challenge 75.5 | Qian 2023 [a21, b18] | [S] K12 |
| CREATOR tool transfer | 100 sets of 3 problems; accuracy 63.0 to 78.3; 39 sets improved, 2 got worse | [a22] | [S] |
| CREATOR interface hints | Creation Challenge: no hint 63.8, utility hint 67.2, utility plus input/output 75.7 | [d14] | [S] K28 |
| CRAFT | 43.16% average relative F1 gain; GQA SAcc/F1 (GPT-3.5): ViperGPT 35.0/36.9, LATM 29.4/30.3, CREATOR 34.3/38.4, CRAFT 45.4/48.8; toolset cost about 2,500 USD | Yuan 2024 [a23, c05] | [E] K13 |
| CRAFT ablations | no name view 37.1, no docstring view 42.4; abstraction removal about 8 points on GQA; generic libraries (NumPy, SymPy) did not help | [c06, c07, d13] | [E] K13 |
| CRAFT size sweep | toolsets of 0, 261, 337, 525: accuracy rose at each step on GQA, OK-VQA, A-OKVQA | [d12] | [C] K25 |
| Voyager | 63 items in 160 iterations (3.3x); wooden/stone/iron 15.3x/8.5x/6.4x; 2.3x distance; iron 21 (SD 7) vs AutoGPT 135 (SD 103); diamond 1 of 3 runs | Wang 2023 [a25, b20, c08] | [S] K14 |
| Voyager ablations | random curriculum -93%; no self-verification -73%; GPT-3.5 for code gives 5.7x fewer items; no library: iron 3/3, diamond 0/3 | [c09, d07] | [S] K14 |
| Voyager zero-shot, new world | 19+/-3, 18+/-7, 21+/-5, 18+/-2 iterations (diamond pickaxe, golden sword, lava bucket, compass); without library 2/3, 3/3, 3/3, 3/3 solved and 36, 30, 27, 26 iterations | [a25] | [S] |
| SkillCraft (126 tasks), making cost charged | GPT-5.2 tokens 1.23M to 0.26M (-79%), success 87 to 90%; Claude 4.5 Sonnet -71%; Gemini 3 Pro -54%; DeepSeek-V3.2 -49% (76 to 87 of 126); MiniMax-M2.1 -11% | Chen 2026 [c21, d04] | [S] K15 |
| SkillCraft nested vs flat | success of 126, base/flat/nested: DeepSeek 76/87/92; Claude 119/121/121; GPT-5.2 109/114/100; nested costs more tokens in all three | [d05, c22] | [C] K15 |
| SkillCraft transfer | Claude easy-to-hard 95 to 100%, tokens 1.92M to 1.56M; Gemini hard-to-hard 76 to 100%, 1.30M to 0.75M; transferred skills ran 97-100% | [d06] | [S] |
| TroVE | CodeLlama-7B GQA: no-reuse INSTANCE made 395 functions, 0.21 below primitives; TroVE vs INSTANCE +8.7 to 83.3% correctness with 60-90% fewer tools; trimming cuts its own library 74-90% with small loss; GPT-4 library sizes 16/38/8 vs CRAFT 282/181/525, CREATOR 875/4,595 | Wang 2024 [a29, d10, d11] | [S] K22 |
| ReGAL | CodeLlama-13B LOGO/Date/TextCraft: full 55.0/77.0/34.1; no retry 48.3/51.9/30.4; no curriculum 36.3/56.6/28.8; no prune 52.0/65.5/25.3; no edit 53.3/69.6/27.4; under shift pruning +3.5, relearning +2.3 | Stengel-Eskin 2024 [d08, d09] | [S] K27 |
| Tool documentation vs demos | with docs, 0-shot equals 16-shot (TabMWP) and 12-shot (NLVRv2); demos copy familiar flags (-P for --port) | Hsieh 2023 [c18, c19] | [S] K16 |
| Learned tool use (Toolformer) | 6.7B GPT-J; LAMA 33.8/11.5/53.5 vs GPT-3 175B 26.8/7.0/39.8; Q&A tool used 98.1%, calculator 97.9%; works above about 775M parameters | Schick 2023 [a26, b16, c20] | [S] K17 |
| STE | Mistral-7B 76.8% on ToolBench APIs vs GPT-4 ICL 60.8%; execution feedback, short- and long-term memory and reflection each needed | Wang 2024 [c14, c15] | [S] |
| ToolMaker | 12/15 vs 3/15 (OpenHands); 0.94 USD and 21.8 actions per tool vs 0.15 and 7.5; one tool took 9 repair iterations | Wolflein 2025 [a28, c16, c17] | [S] K21 |
| RoboTool | real-world success 0.1 below simulation; removing Analyzer or Calculator lowered success | Xu 2023 [a27] | [S] |
| Children vs LLMs on tool innovation | children 3-7 (n=42) 85.2%, adults (n=30) 95.7%; LLMs chose the lookalike distractor | Yiu 2023 [c13] | [E] K18 |
| MacGyver, GPT-4 | 1,600+ problems; humans 79.3% vs GPT-4 73.3%; efficient 18.9%, infeasible 37.5%; errors: wrong tool usage 42.4, goal not achieved 17.7, unfaithful to constraints 16.9, wrong spatial 10.8, unavailable tools 9.5 | Tian 2024 [b21, c10, c11] | [E] K18 |
| MacGyver prompts | reflection: infeasible -9.7 points (GPT-4 only); divergent-convergent: efficient +6.5, infeasible -4.3, helped all three models | [c12, d17] | [S] K19 |
| Lomekwi recognition | Qwen3.5 recognition 0.29/0.10/0.05/0.02 (2B-27B), win rate 0.46 to 0.88; no-call episodes 61 to 154 of 180; by-hand wins 35 to 157; Opus builds less than Haiku | Klein-Seetharaman 2026 [c23, d16] | [S] K20 |
| Lomekwi prompt fix | "exactly one tool solves it": Qwen3.5 27B 0.02 to 0.60; Qwen2.5 32B 0.15 to 0.89; Qwen3 32B 0.06 to 0.85 | [d15] | [S] K20 |
| AllocBench first-sight builds | abstract game 28/4/15/24% (Haiku 4.5, Opus 4.8, GPT-5.4-mini, GPT-5.6 Sol); when building means writing a reusable script 100/99/88/100%; PPO fix 74% to 6% in the abstract game did not transfer (score R1 49.2 to 34.8) | Wang and Xu 2026 [d01, d02] | [S] K24 |

## 4. Mechanisms and models

### 4.1 The animal side, as testable mechanisms
Four accounts compete. Each predicts something different, so an engineer can use them as test designs.

1. **Predisposition plus shaping.** Inherited action patterns produce object manipulation. Success reinforces it. Predicts: success appears with experience, first trials are weak, wild-type behaviour is already there [a05, a07]. Evidence: Betty's critics, the 10 of 18 wild bending rate, naive juveniles.
2. **Perceptual-motor feedback chaining.** Each step is chosen because the last step visibly moved the reward closer. Predicts failure when feedback is hidden [a14, b25]. Evidence: horizontal string pulling, cranks, Aesop U-tube.
3. **Learning from success with an initial functional bias** (Hennefield null model) [b10, b24]. Predicts success-driven improvement over trials, no learning from failure, no transfer to a new task. This is the null that a tool-reasoning claim must beat.
4. **Mental representation of goal and sub-goals** (Dennett's Popperian creatures) [a16]. Predicts first-trial success, success when stages are out of sight, resistance to distractor tools. Evidence: Gruber 2019 stick condition, von Bayern first-trial builds and distance-sensitive choice, Taylor metatool trial 1.

The designs discriminate by what they remove or hide. First-trial success favours 4 over 3. Hidden stages favour 4 over 2. Re-skinned transfer separates 4 from 1 and 3 [b22]. Both 2 and 4 may be true in different tasks [critique].

Crow results are mixed. Crows pass first-trial and out-of-sight tests [b05, b07, b08], but need tens of trials in the stone problem [a15], and fail a feedback-free string task [a14]. The stone condition was far harder than the stick condition, so even the strongest planning result is asymmetric.

### 4.2 The LLM side: a make-test-store-retrieve loop
All library systems share one loop. An engineer can build it from these parts.

**A. Gate (should we make a tool?).**
- LATM dispatcher: for each new item, decide if an existing tool fits or a new one is needed. Reported 95% identification and 96% make-decision accuracy [c03]. Cheap.
- AllocBench: models wait for recurrence in the abstract (more than 70% of the time) but build on first sight 88-100% when building means writing a script [d01]. So the gate must be code (a counter of how often a task type recurred), not the model's judgement.
- Lomekwi: large models often do not look for a tool at all; a prompt saying a tool exists restores it [d15]. So the gate also needs a forced "is a tool listed or buildable?" step before hand solving.

**B. Make (maker writes a tool).**
- LATM: a strong maker writes a Python function and wraps it. Training items serve as tests; the failure is a tool that fits only the training samples [a19, c04].
- CREATOR: creation (with docstring), decision (plan the call), execution, rectification (repair from errors). The interface spec helps: no hint 63.8, utility 67.2, utility plus input/output 75.7 [d14].
- CRAFT: solve training items, validate, abstract into a general named function, de-duplicate [a23]. Abstraction and good names are worth about 6.6 to 8 points on GQA [d13].
- Voyager: a skill is executable code plus a description, verified by an in-environment critic before storage [a25, c09].
- ToolMaker: closed-loop self-repair with unit tests as the stop rule [a28].

**C. Verify before store.** Weak makers produce tools that fit only the training samples [c04]. Voyager's self-verification is its most important feedback (-73% without), but that ablation also controls when to move on [d07]. No study isolates test-on-fresh-items before storage [K26 open].

**D. Store with a doc.** Tool docs beat demos for use [c18, c19]. Each entry: name, purpose, inputs, outputs, one test.

**E. Retrieve.** CRAFT multi-view retrieval (problem, function name, docstring) beats single-view [c07]. On a homogeneous task BM25 matched CRAFT (89.2 vs 88.4 on TabMWP) [K13]. Voyager embeds the description [a25].

**F. Maintain.** TroVE: periodic trimming cuts the library 74-90% for a small accuracy cost [d10]. ReGAL: edit and prune each add 3 to 12 points [d08]. Unchecked growth hurts: TroVE's INSTANCE baseline with 395 functions fell below primitives [d10].

**G. Cost model.** LATM cost is O(nc + C) for n items, c the cheap-model cost and C the strong-model cost, versus O(nC) without a tool [c02]. The making cost C is paid once and amortised. The papers do not charge it against held-out items at equal tokens [critique, gap 1]. SkillCraft does charge making inside the run and still saves 49-79% [d04].

### 4.3 What the crow tests look like as LLM tasks
- First-trial compound construction: give parts never shown in use; score the first attempt [b07].
- Out-of-sight stages: hide intermediate output from the agent. Does it still compose helpers? [a15]
- Feedback removal: strip intermediate results from tool chains [a14].
- Aesop null model: compare first-trial success to learned success across repeats, with no-transfer re-skins [b10].
No LLM study runs these [d20, K29].

## 5. What holds up

### 5.1 Animal findings
- **Holds:** wild crows make standard hook and stepped tools [K01]; naive juveniles develop tool use without models [K05]; first-trial metatool and compound-tool success in several labs [K06]; feedback dependence in string tasks [K08]; Aesop results explained by functional bias plus learning from success [K09].
- **Contested:** Betty as invention [K02]. The 17-crow replication found a minority solve rate [K03]. Wild crows already bend stems [a05].
- **Failed or weak:** horizontal string pulling (crows did not solve it, humans did) [a14]; the stone problem needed 43-69 trials [a15]; rooks made a hook on every trial yet retrieved the bucket on only 35% [a12]; no NC crow dropped stones spontaneously [b09].
- **Moderators:** population (hooked-stick tools limited to some populations) [b14]; bend angle (100 vs 75 degrees) [a12]; food distance (70.8% vs 20.8%) [d18]; stone vs stick condition [a15]; visible feedback [a14, b25].
- **Sample sizes are small:** N=1 to 14 per study, wild-caught birds of unknown history [critique].
- **Not verified:** Chappell and Kacelnik 2002 tool selection (only the 2004 abstract opened) [d19]. The "9 of 10 retrievals" for Betty is Wikipedia only [a01].

### 5.2 LLM findings
- **Holds across several sources [E]:**
  - A task-relevant, abstracted, de-duplicated library helps (CRAFT +43.16% relative F1) [K13].
  - Generic libraries do not help [c06].
  - LLMs are poor at innovating tools (children 85.2% vs LLMs choosing the lookalike; MacGyver 37.5% infeasible) [K18].
  - Closed-loop self-repair with tests works for tool building (ToolMaker 12/15 vs 3/15) [K21].
- **Holds in one study [S]:**
  - Maker/user split (LATM) [K10].
  - Rectification (PoT 80.0 to 87.3) [K12].
  - Self-verification and curriculum in Voyager [K14].
  - Skill caching saves tokens (SkillCraft) [d04].
  - Prune and edit (ReGAL) [K27].
  - Docs beat demos [K16].
  - Recognition inversion with size (Lomekwi) [K20].
  - Early-build bias (AllocBench) [K24].
- **Contested [C]:**
  - Library size: TroVE's no-reuse INSTANCE hurt, CRAFT's retrieved libraries rose through 525 [K25].
  - Nested skills: help DeepSeek (87 to 92), tie Claude (121/121), hurt GPT-5.2 (114 to 100) [K15].
- **Failures and boundary conditions:**
  - LATM is flat for GPT-4 as user on Logical (88.8 vs 86.6), and GPT-3.5 as maker fails on hard tasks [c02, c04].
  - LATM scores below vanilla on VQA (GQA 29.4 vs 35.0) [a23]. Library benefit depends on task type [b23].
  - Voyager hides the recognition term because GPT-4 already knows the Minecraft recipes [c24].
  - Reflection helped only GPT-4 among the three 2023 models tested [d17].
  - Toolformer needs finetuning and more than about 775M parameters [b16]. Outside our no-training rule.
- **Interventions that worked:** interface hints (63.8 to 75.7), rectification, tool docs, the "exactly one tool solves it" prompt (recognition 0.02 to 0.60), divergent-convergent prompting (efficient +6.5), pruning (+3.5 under shift), a weak model using a strong model's tool, cross-model skill transfer (Gemini hard-to-hard 76 to 100%).
- **Interventions that did not:** generic libraries; demos instead of docs; hierarchical skills on GPT-5.2 (114 to 100 of 126); PPO to teach waiting (did not transfer from the abstract game to code); paper summaries for ToolMaker (cut repairs, not failures) [c17].

## 6. Language models

**Tool use versus tool making.** Using a given tool is learnable and cheap. A finetuned Toolformer calls tools in about 98% of eligible cases [a26]. Making is harder, and deciding that a tool should exist is harder still.

**Making when told to make.** Strong makers succeed on procedural tasks. GPT-3.5 reaches 79.7 to 100 on five of six LATM tasks with GPT-4's tool [a19]. Weak makers fail because the tool fits only the training samples [c04]. Verification repaired only 2 of 60 trials.

**Reuse across calls.**
- Making inside the run still pays. SkillCraft cuts tokens by 49% to 79% on four of five models with success flat or up [d04]. One model saved only 11%.
- Across held-out items, CRAFT shows large gains (+43.16% relative F1), but only with a task-specific library and multi-view retrieval. Generic libraries failed.

**Choosing to build.**
- Lomekwi: Qwen3.5 recognition drops 0.29 to 0.02 with size while win rate rises 0.46 to 0.88. Large models solve by hand [c23]. Claude models show the same direction (Opus builds less than Haiku) [d16].
- A prompt that says exactly one tool solves the task lifts recognition from 0.02 to 0.60 (27B) [d15].
- AllocBench: in an abstract game models wait for recurrence, but when a commit means writing a reusable script they build on the first instance 88-100% of the time [d01]. PPO training fixed only the abstract frame [d02].

**Innovating with objects.** On the tool innovation task LLMs pick the lookalike, while 85.2% of children pick the right non-obvious object [c13]. On MacGyver GPT-4 gives 18.9% efficient and 37.5% infeasible answers, with wrong tool usage 42.4% of errors [b21]. Reflection cut infeasible answers by 9.7 points for GPT-4 only. Divergent-convergent prompting helped all three models.

**What changed it, and by how much.**

| Lever | Change | Source |
|---|---|---|
| Strong-model tool, weak user | GPT-3.5 CoT 20.4 to 92.2 (Dyck) | [a19] |
| Interface spec | 63.8 to 75.7 | [d14] |
| Rectification | PoT 80.0 to 87.3 | [a21] |
| Tool transfer across scenarios | 63.0 to 78.3 | [a22] |
| Docs instead of demos | zero-shot matches 12-16 shot | [c18] |
| Skill caching | -49% to -79% tokens | [d04] |
| Trim after storage | library -74-90%, small accuracy cost | [d10] |
| "A tool exists" prompt | recognition 0.02 to 0.60 | [d15] |
| Divergent-convergent | efficient +6.5 points | [c12] |

**Caveats.** Most studies use 2023 models (GPT-3.5, GPT-4, ChatGPT). Only SkillCraft, AllocBench and Lomekwi (2026) use current models. None test extended-thinking reasoning models at equal total tokens. Lomekwi and AllocBench are July 2026 preprints from single groups. No LLM study applies the crow paradigms [d20].

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = section 5 of SCHEMA.md (subgoal library).

### Add now (established)

1. **Keep a task-specific, abstracted, named, de-duplicated library of verified helpers; do not stock generic libraries.** Part: memory (subgoal library). [E] K13. Evidence a23, a24, c05, c06, c07, d13.
2. **Retrieve tools by several views (problem text, name, docstring) and show only the top few.** Part: memory, S3. [E] K13 for multi-view; the size curve is [C] K25. Evidence c07, d12, d10.
3. **Store each tool with a short doc (purpose, inputs, outputs), not worked demos.** Part: memory. [E] for the name/docstring effect in CRAFT; the docs-versus-demos result alone is [S] K16. Evidence c07, c18, c19.
4. **Treat a tool as unproven until it passes on items it was not fitted to (G3 applied to tools).** Part: G3, S4, S8. [E] as G3; tool-specific evidence [S]. Evidence a19, c04, c09.
5. **Let model-written helpers do the arithmetic and let code do selection, with self-repair against tests.** Part: G5, S5. [E] K21 (two sources); RoboTool agrees on numeric offsets. Evidence a28, c16, a27.
6. **Do not rely on the model to notice that a tool could help.** Part: S0, O1. [E] in direction K18 (c13, b21, c10); the fix is a fixed S0 question, "is a tool listed or buildable?". Evidence c13, b21, c10, c23.
7. **Use the Aesop null model when judging whether the agent "reasons" about tools.** Part: G10. [E] K09. Evidence b10, b24. First-trial success on a new variant is the signal of reasoning, not improvement over repeats.

### Test first (single-source or contested; ids match UNKNOWNS.md)

1. U1 Maker/user split on held-out items at equal total tokens, making cost charged. [S] K10. Evidence a19, c02, d04. Part: O1/memory.
2. U2 Code-owned "has this class recurred?" gate before making a tool. [S] K24. Evidence d01, d02. Part: S0, S6.
3. U3 Forced "tool exists or buildable" step before hand solving. [S] K20. Evidence c23, d15, d16. Part: S0/O1.
4. U4 Verification-before-storage on fresh items, separated from retrieval. [open] K26. Evidence d07, d08, d03. Part: memory, G3.
5. U5 Periodic prune and edit of the library. [S] K27, K22. Evidence d08, d09, d10. Part: memory.
6. U6 Fixed tool template (name, purpose, inputs, outputs, test) versus free-form. [S] K28. Evidence d14, d13. Part: memory.
7. U7 Flat versus nested skills. [C] K15. Evidence d05, c22. Keep flat by default until tested. Part: memory.
8. U8 Per-action feasibility check and divergent-convergent step. [S] K19. Evidence b21, c12, d17. Part: S4/O1.
9. U9 Library size under top-k retrieval. [C] K25. Evidence d10, d11, d12. Part: memory.
10. U10 Crow-style harness, first-trial versus learned success. [open] K29. Evidence d20, b10, b07. Part: measurement only.

## 8. Concrete tests on our bench

Rules for all tests: both arms get the same total token cap, with making and testing cost counted in the library arm. Report accuracy, tokens and a paired comparison over the same seeds. Use at least 3 task families so a library has something to reuse.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 maker/user split | streams of 20-40 items from one procedural family (sorting, scheduling, simulation, code-checkable transforms); held-out items | (a) plain reasoning model, one pass per item; (b) one maker pass, test on 3 fresh items, then cheap passes per item | accuracy and total tokens including making | gain on procedural families (LATM shape); none on one-off items |
| T2 recurrence gate | mixed stream: 3 hot families, 5 trap families that appear once | (a) model decides when to make; (b) code counter, make on the 2nd occurrence | utility per token; share of built tools that were reused | fewer wasted builds (AllocBench shows near-100% first-sight builds when ungated) |
| T3 recognition step | tasks where a stored or buildable tool beats hand solving | (a) plain; (b) forced "tool exists or buildable? which?" before solving; each with extended thinking on and off | tool-call rate, accuracy, tokens | more tool calls and higher accuracy for strong models; may cost tokens on easy items (G11) |
| T4 verify gate | fixed pool of candidate tools, half wrong on fresh inputs | (a) store all that pass the training items; (b) store only if they also pass fresh items; (c) no library | later-task accuracy, bad-tool store rate | gate removes tools that fit only samples; size unknown |
| T5 prune and edit | task mix shifts at item 50 | (a) grow only; (b) prune low-pass-rate tools every 20 items; (c) prune plus rewrite failing tools | accuracy after shift, context size | small gain under shift (ReGAL +3.5; TroVE small loss) |
| T6 template | tool writing for 5 families | (a) free-form; (b) fixed template with a test slot | pass rate on fresh items, tokens | modest gain (CREATOR hints +11.9) |
| T7 flat vs nested | compositional tasks needing 2-3 levels | (a) flat; (b) skills may call skills | success, tokens, error depth | model dependent; keep flat unless (b) wins on 3 models |
| T8 feasibility check | MacGyver-style object tasks (public set subset) | (a) plain; (b) per-step "is each object available, does it meet the constraint?"; (c) divergent-convergent | infeasible share, efficient share | infeasible down for strong models; uncertain for current reasoners |
| T9 size sweep | 0, 25, 100, 400, 1,000 tools | (a) all listed in context; (b) top-k retrieval | accuracy at fixed token cap | listing declines early; retrieval flat or rising |
| T10 crow harness | (i) assemble a helper from parts not shown in use; (ii) hidden intermediate output; (iii) re-skinned repeat | repeated trials on all tasks | first-trial success vs success after repeats | measurement only: reasoning versus learned |

## 9. What does not transfer, and why

- **Inherited action patterns and development.** Crow juveniles reveal predispositions [a07]. An LLM has none; "protoprobing" has no analogue. The only lesson is that an explicit tool-making prompt is needed.
- **Physical bending and morphology.** Bend angle (100 vs 75 degrees) is bodily and spatial [a12]. The nearest analogue is code correctness, which code can check.
- **The N=1 spectacle (Betty).** One accidental event is not a rule and not a design target [K02].
- **Feedback chaining as a flaw.** In crows, feedback-dependent success limits the insight claim [a14]. For an agent, visible feedback is a feature (G2: revise from real output). We should not remove it, only test whether it is the only thing working.
- **Social learning and population culture.** Pandanus design diversification [b04] has no equivalent in a single agent. Shared libraries across users are a later question (multiplayer).
- **Finetuned tool use.** Toolformer and STE change weights [a26, c14]; excluded by our no-training constraint.
- **Aesop's physical causal reasoning (mass, displacement).** Useful only as a null-model pattern, not as content.
- **Library gains on open exploration.** Voyager's gains came from an environment with a tech tree and a model that already knew the recipes [c24, b23]. Do not expect that on single hard problems.

## 10. Open questions

1. At equal total tokens with making cost charged, does a make-once split beat a current reasoning model on held-out items? (gap 1)
2. Does the recognition inversion hold for current frontier models with extended thinking, and does a forced check fix it? (gap 2; one group, July 2026)
3. How much of library value is verify-before-store and how much is retrieval? (gap 3)
4. Where does library size turn harmful with a fixed budget on a modern model? (gap 4; no sweep above 525)
5. Are flat skills better than nested in general? SkillCraft alone says model dependent. (gap 5)
6. Does a per-action feasibility check still help current models at equal tokens? (gap 6)
7. Do LLMs show crow-style first-trial tool construction, and do they beat the Hennefield null? (gap 7; no study found)
8. Does a fixed tool template beat free-form making? (gap 8)
9. Chappell and Kacelnik 2002 tool selection and the exact Betty trial counts are unverified [d19, a01].
10. Is Betty's wire bending an invention or a normal predisposition? (K02; no agent consequence)

## 11. Sources

[V] = opened (full text or page) by the evidence agents. [M] = snippet or abstract only.

Animal studies
- [V] Weir, Chappell, Kacelnik 2002, Oxford group summary page: https://users.ox.ac.uk/~kgroup/tools/tool_manufacture.shtml ; [M] PubMed abstract: https://pubmed.ncbi.nlm.nih.gov/12169726/
- [V] Kacelnik interview 2018: https://reflectionsonpaperspast.com/2018/02/14/revisiting-weir-et-al-2002/
- [V] Weir and Kacelnik 2006: https://pubmed.ncbi.nlm.nih.gov/17024509/
- [V] van Buuren et al. 2021: https://doi.org/10.26451/abc.08.02.07.2021
- [M] Kenward et al. 2005 Nature: https://www.nature.com/articles/433121a ; https://pubmed.ncbi.nlm.nih.gov/15650729/
- [V] Kenward et al. 2006 Anim Behav: https://users.ox.ac.uk/~kgroup/publications/pdf/kenward_etal_2006_AnimBehav_ontogeny.pdf
- [V, abstract page] Hunt 2000: https://pmc.ncbi.nlm.nih.gov/articles/PMC1690543
- [M] Hunt 1996 Nature 379: https://www.nature.com/nature/journal/v379/n6562/pdf/379249a0.pdf
- [M] Hunt and Gray 2003: https://europepmc.org/article/MED/12737666
- [V] Emery and Clayton 2004 Science: https://chd.ucsd.edu/_files/winter2009/emery.04.pdf ; [M] abstract: https://pubmed.ncbi.nlm.nih.gov/15591194/
- [V] Bird and Emery 2009: https://pmc.ncbi.nlm.nih.gov/articles/PMC2700937
- [V] Taylor, Knaebe, Gray 2012: https://pmc.ncbi.nlm.nih.gov/articles/PMC3497243/
- [V] Gruber et al. 2019: https://pmc.ncbi.nlm.nih.gov/articles/PMC6384166/
- [M] Taylor et al. 2007 metatool: https://pubmed.ncbi.nlm.nih.gov/17702575/ ; https://pure.mpg.de/pubman/item/item_3329768_3/component/file_3329770/
- [M] Taylor et al. 2009 trap-tube: https://europepmc.org/article/PMC/PMC2674354
- [V] von Bayern et al. 2018: https://europepmc.org/article/PMC/PMC6200727
- [V] Jelbert, Taylor, Gray 2015: https://europepmc.org/article/PMC/PMC4594378
- [M] Hennefield et al. 2018: https://pubmed.ncbi.nlm.nih.gov/30132156/
- [V] Azure-winged magpies 2021: https://europepmc.org/article/PMC/PMC7804021
- [V] Individual learning review 2020: https://europepmc.org/article/PMC/PMC7521350
- [V] Baseline and social-learning conditions 2020: https://europepmc.org/article/PMC/PMC7336849
- [V] Auersperg et al. 2026: https://europepmc.org/article/PMC/PMC13149787
- [M] Rutz et al. 2016: https://europepmc.org/article/MED/27629645
- [V, abstract] Chappell and Kacelnik 2004: https://pubmed.ncbi.nlm.nih.gov/15069612/ ; [M] 2002 paper, cited in a18 only

LLM and AI studies
- [V] Cai et al., LATM: https://arxiv.org/abs/2305.17126
- [V] Qian et al., CREATOR: https://arxiv.org/abs/2305.14318
- [V] Yuan et al., CRAFT: https://arxiv.org/abs/2309.17428
- [V] Wang et al., Voyager: https://arxiv.org/abs/2305.16291
- [V] Schick et al., Toolformer: https://arxiv.org/abs/2302.04761
- [V, narrative only] Xu et al., RoboTool: https://arxiv.org/abs/2310.13065
- [V] Wolflein et al., ToolMaker: https://arxiv.org/abs/2502.11705
- [V, full text re-read] Wang, Neubig, Fried, TroVE: https://arxiv.org/abs/2401.12869
- [V] Tian et al., MacGyver: https://arxiv.org/abs/2311.09682
- [V] Yiu, Kosoy, Gopnik: https://arxiv.org/abs/2305.07666
- [V] Wang et al., STE: https://arxiv.org/abs/2403.04746
- [V] Hsieh et al., Tool documentation: https://arxiv.org/abs/2308.00675
- [V] Chen et al., SkillCraft: https://arxiv.org/abs/2603.00718
- [V] Klein-Seetharaman et al., Lomekwi: https://arxiv.org/abs/2607.16961
- [V] Wang and Xu, AllocBench: https://arxiv.org/abs/2607.23332
- [V] Stengel-Eskin et al., ReGAL: https://arxiv.org/abs/2401.16467
- [M, second-hand] Berlot-Attwell, Rudzicz, Si 2024 (library learning claim, read in AllocBench related work): https://arxiv.org/abs/2607.23332
- [M] Europe PMC search log for LLM-on-crow-task studies (none found): https://europepmc.org/
