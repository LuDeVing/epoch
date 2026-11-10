# Teaching heuristics: deep document

*Subfield E06.07. Scope: does teaching problem-solving heuristics (Polya, Schoenfeld, Mason) improve problem solving, when does it transfer, and what does this mean for one scaffolded language-model agent. Evidence ids (a01..d17) point to evidence_a-d.jsonl; claim ids (K01..K32) to claims.jsonl. Numbers were re-opened in critique.md. Dated 2026-11-10.*

## 1. What it is

A heuristic is a rule of thumb that may help and does not guarantee a solution. Examples: draw a diagram, try a special case, work backwards, solve an easier related problem, look for a pattern, add an auxiliary element. "Teaching heuristics" is the attempt to make students (or models) learn these rules and use them on new problems.

The field question is transfer. Teaching a strategy on problems of type A does not reliably make a person better on problems of type B. Schoenfeld's answer was that heuristics are not enough. A solver also needs a control layer: monitor progress, assess whether the current path works, and curtail a path that does not. He called this managerial or executive behaviour. This is why the SUBFIELDS row says "Needs a control layer."

Three kinds of claim must be kept apart.
1. Heuristics alone: teach a list of strategies. The human record is weak (K01).
2. Heuristics plus management: strategies plus when-to-use and when-to-stop. Strong gains in small human studies, but confounded (K02).
3. Prompting a language model with a heuristic. Large gains from one generic trigger (step by step), small and conditional gains from richer ones, about nothing on current reasoning models (K10, K24, K25).

For our agent: the operators O1-O8 are a heuristic list. G1 and S6 (fired by code) are the control layer. The questions are which operators earn their tokens, and whether control matters more than the list.

## 2. History and theories in depth

**Polya (1945, How to Solve It).** Four phases: understand, plan, carry out, look back, plus a list of heuristic questions. Prescriptive, from teaching practice. No experiment. Our S1, S3, S8 and S9 map to its phases. Polya's "look back" is the origin of S9.

**Newell and Simon (1972).** Human Problem Solving and the General Problem Solver turned heuristics into means-ends analysis: reduce the difference between current and goal state by picking an operator. This is the machine ancestor of our operator tree at S6 and of work-backwards (O5). Not opened this session (c24).

**Lenat (1983) EURISKO.** A program that learned new heuristics. Not opened (c23). Cited only as the AI line of "heuristics as objects the system can improve."

**Schoenfeld (1979, 1982, 1985).** The central body of work.
- 1979 lab study (d13, opened in full): seven upper-division college students, four trained on heuristics, three controls trained for the same time on the same problems. All four trained improved; one of three controls did. All four trained outscoring all three controls has chance probability 1/35, so p < .05. No effect size. A five-minute stop-and-review prompt was used in both arms, so it cannot explain a difference between them.
- The lab result is more nuanced than the headline (K31). Cue-driven strategies were learned: fewer-variables (3 of 4 trained solved vs 1 of 3 controls) and induction (4 of 4 vs 0 of 3). Vague strategies (subgoals, contradiction) were not learned. Knowing a strategy did not mean using it.
- 1982 final report (a03, a07, a08): classroom course with heuristics and a managerial strategy taught together. Course group (N=11) 21 to 73 on the problem test; control group (programming course, N=8) 14 to 24. Interaction F(1,17)=48.2, p<.001. Expert baseline N=9. The score scale is not stated, so treat it as test points. Heuristic fluency rose and correlated with better solving.
- 1983 (a06, b01, b02): protocols of a geometry construction task. No pair of students reasoned to a solution; they guessed for 15-20 minutes with compass in hand. Only one pair justified the answer, and only afterwards. The pretest norm was jumping into one approach. After the course, only 2 of 12 post-test protocols showed the bad pattern (a08; scope of "that type" unclear in the extract).
- 1978 integration study (a04, as cited): the strategy group learned a strategy for SELECTING which technique to use. It studied 7 h vs 9 h for controls and scored significantly higher. No statistic given.
- 1982 review of prior work (a05): little conclusive evidence that students learn heuristics and then improve.
- Schoenfeld's framework (a15): resources, heuristics, control, belief systems. Control explains why students with the knowledge still fail.

**Mason, Burton and Stacey (1982), Thinking Mathematically.** A prescriptive course: specialise, generalise, conjecture, convince; a stuck-and-aha routine; a habit of reflection. Learner-run. No experimental data (a14). Source of our O1 (specialise) and O2 (generalise).

**Perkins (2000).** Four ways a solver gets stuck (a16, as summarised). No data. Relevant to impasse design.

**Rival theory: knowledge, not strategy (Sweller, Clark, Kirschner 2010; b04, b05).** Expertise is a large store of domain schemas. They say no randomised trial shows Polya-type strategy teaching improves problem solving, while worked-example trials exist. De Groot chess recall: masters about 70% vs weekend players about 30% on real positions; both about 30% on random ones. This is the main contest (K08).

**Measurement problem (Rott 2015; d15).** What counts as a "heuristic" depends on the coding manual. The same 32 actions are coded 29, 23 and 16 as heuristic by three published manuals (Koichu et al. 2007, Kantowski 1974, Rott 2012). Heuristic-use counts are not comparable across studies (K07).

**Later human work (2000-2022).** Koichu, Berman and Moore (2007, a17, abstract only): 5-month heuristic-literacy experiment, N=92, moderate mean effect, value not seen. Hohn and Frey (2002, a18, abstract): elementary school; persistence not checked. Eisenmann et al. (2015, a20): gains on teachable heuristics. Haenze and Leiss (2022, a21): heuristic worked examples. Kuzle (2019) and Kaitera and Harmoinen (2022): small classroom studies without controls.

**LLM era (2022-2026).** The heuristics returned as prompts: chain-of-thought (Wei, Kojima 2022), least-to-most (Zhou 2023), plan-and-solve (Wang 2023), step-back (Zheng 2024), analogical prompting (Yasunaga 2024), Self-Discover (Zhou 2024), Buffer of Thoughts (Yang 2024), meta-reasoning prompting (Gao 2024). Then control-layer systems (Meta-Reasoner 2025, metacognitive consolidation 2026), and training-time use of heuristic data (Gandhi 2025, RRV 2026, Llama-Polya 2026).

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources, numbers re-opened); S = single source; C = contested. H = human study, L = LLM study.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| H: Heuristics taught with a managerial strategy raise problem solving | Course 21 to 73 vs control 14 to 24 (N 11 vs 8); interaction F(1,17)=48.2, p<.001 | Schoenfeld 1982 (a07) | S (confounded) |
| H: Lab training on heuristics beat controls, tiny N | 4 trained vs 3 controls; all trained beat all controls; 1/35, p<.05; mean net gain 0 vs over 2 problems | Schoenfeld 1979 (d13) | S |
| H: Cue-driven heuristics learned, vague ones not | Induction 4/4 vs 0/3; fewer variables 3/4 vs 1/3; subgoals and contradiction not learned | Schoenfeld 1979 (d13) | S |
| H: Students jump into one approach, no control | Geometry task: no pair reasoned to a solution; 15-20 min guessing. Post-course 2 of 12 protocols showed it | Schoenfeld 1983, 1982 (a06, a08) | S |
| H: Teaching a technique-selection strategy | 7 h vs 9 h study, higher score; no statistic | Schoenfeld 1978 as cited (a04) | S |
| H: Heuristics alone have weak evidence | No conclusive evidence (review); no RCT of Polya-type teaching (rival authors) | a05, b04 | E |
| H: Grade effect of heuristic teaching | Hembree: 487 reports; K-5 none, 6-8 mild, high school distinct; effect sizes not read | Hembree 1992 (d14, abstract) | E on direction only |
| H: Word-problem instruction meta-analyses | g = 0.56 [0.40, 0.72]; g = 0.71 [0.49, 0.92]; older d = 1.848 (group designs) | Lein 2020, Myers 2023, Zhang 2012 (a24-a26, abstracts) | E, but pools schema and other methods |
| H: Classroom gains on easy-to-practise heuristics | Auxiliary element 18% to 74%; kite 13% to 58% (n=98); inscribed square 9% to 20%; odd numbers 21% to 54% (n=109) | Eisenmann 2015 (a20) | S |
| H: Heuristic worked examples by grade | Grade 7 modelling F(2,174)=5.10, eta2=.06 (N=180); grade 5 no modelling effect (N=134) | Haenze and Leiss 2022 (a21) | S |
| H: Heuristic coding unreliable across manuals | Same 32 actions: 29 / 23 / 16 coded heuristic | Rott 2015 (d15) | C |
| H: Small uncontrolled classrooms | Kuzle N=14; Kaitera N=25, mean 6.1 to 8.9 (SD 2.5, 3.6); item 6A 24% to 68% | b07-b09 | S (no control) |
| L: One generic trigger, large gain on older models | MultiArith 17.7 to 78.7; GSM8K 10.4 to 40.7 (text-davinci-002); PaLM 540B GSM8K 17.9 to 56.9 | Kojima, Wei 2022 (b10, b11) | E |
| L: CoT helps mainly math, symbolic, logic | Mean gain symbolic 14.2, math 12.3, logic 6.9; top three 56.9 vs 45.5; others 56.8 vs 56.1 | Sprague 2025 (a37) | S |
| L: Plan-and-solve | GSM8K 56.4 to 59.3 (+2.9, text-davinci-003); avg six math sets PS+ 76.7 vs 8-shot CoT 77.6; missing-step errors 12% to 7%, calculation 7% to 5%, semantic 27% vs 27% | Wang 2023 (a28, b13, c02) | S |
| L: Least-to-most | SCAN length 99.7 vs CoT 16.2; GSM8K 62.39 vs 60.87; 2 steps 74.53 vs 76.68 (worse); 5+ steps 45.23 vs 39.07 | Zhou 2023 (a27, c06) | S |
| L: Step-back | PaLM-2L Physics 66.4 to 73.2, Chem 70.9 to 81.8; GPT-4 Physics 69.4 to 84.5; GSM8K 84.3 vs 84.4 zero-shot CoT; fixes 20.5% of errors, adds 11.9% | Zheng 2024 (a29, b15) | S |
| L: Self-Discover | BBH PaLM 2-L 60 (CoT) to 67; GPT-4 75 to 81; MATH GPT-4 71 to 73; structures 87.5% correct; 74.7% of MATH failures are computation errors | Zhou 2024 (a31, b18) | S |
| L: Analogical prompting | GSM8K GPT-3.5 77.8 vs 75.0/75.8/76.7; MATH about 37.3 vs 33.0 | Yasunaga 2024 (b20, c09) | S |
| L: Buffer of Thoughts | Game of 24 GPT-4: base 3.0, CoT 11.0, ToT 74.0, BoT 82.4; cost about 12% of multi-query | Yang 2024 (c14) | S |
| L: Skill-labelled example retrieval | MATH +11.6 over CoT, +3.5 over topic; GSM8K GPT-4 93.00 to 94.31 | Didolkar 2024 (b24, c17) | S |
| L: Self-correction without outside signal hurts | GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-4-Turbo 91.5 to 88.0 to 90.0; GPT-3.5 CSQA 75.8 to 38.1; oracle labels GSM8K 75.9 to 84.3 | Huang 2024 (b25, c18) | E |
| L: Sound verifier needed | Game of 24: plain 5%, self-critique 3%, sound verifier 36%, resample k=25 42%; judge false-negative 20.7% to 97% | Stechly 2024, Kamoi 2024 (d06, d07) | E |
| L: Reasoning models, heuristic prompts add near nothing | GPQA Diamond (4,950 runs per cell): o3-mini +0.029, o4-mini +0.031, Gemini Flash 2.5 -0.033; non-reasoning +0.044 to +0.135 but 3 of 5 worse on strict 100%-correct | Meincke 2025 (d01) | S |
| L: Equal budget, CoT-SC matches PS and L2M | GPT-3.5, read from plots, no table cells | Wang 2024 Token Economies (d08) | S |
| L: Method selection | GPT-4 MRP 0.772 vs ToT 0.725 vs CoT 0.654; GPT-3.5 MRP 0.433 vs SPP 0.469; GSM8K 83.1 to 78.1 | Gao 2024 (d02, d03) | S |
| L: External controller beats self-selection | Game of 24 GPT-4o-mini: 89 vs 82 (LLM picks) vs 4 (plain CoT); Gemini-Exp 94/87/11 | Meta-Reasoner (d04) | S |
| L: Monitor, control and lessons | MATH-500 GPT-4o-mini: reasoner 72.67; updates only 80.47; monitor+control 79.20; full 85.13 | Zhuang 2026 (d05) | S |
| L: Heuristic diversity at inference | GPT-4 graph colouring DIV-SE 97 vs SC-10 23 vs CoT 15; Blocksworld 3: 94 vs 73 vs 70 | Naik 2024 (d09) | S |
| L: Behaviours predict RL gain | Countdown: Qwen ~60%, Llama ~30%; primed Llama matches Qwen; empty-CoT priming 30-35% | Gandhi 2025 (a32, a33) | S |
| L: Heuristic diversity in training | pass@64 46.30 to 48.17; post-RL 44.21 to 47.62; pass@1 9.25 to 11.50 (STaR 13.02); wrong-answer variant below vanilla RL | RRV 2026 (a34, a35) | S |
| L: Explicit algorithm in context | Error 10x lower parity, 9x addition, 5x multiplication, 2x subtraction | Zhou 2022 (b27, c20) | S |
| L: Instruction drift | Compliance decays within about 8 dialogue rounds (LLaMA2-70B, GPT-3.5) | Li 2024 (d11) | S |

## 4. Mechanisms and models

Each is written so an engineer can build it.

**4.1 Cue-action rules (Schoenfeld 1979).** Heuristics that were learned had a recognisable trigger in the problem (a parameter that can be reduced; an integer sequence to find a pattern for). Vague ones (use subgoals) were not learned. Implementation: give each operator O1-O8 a trigger predicate that code can evaluate on the problem or on the failure record, and a fixed template for what the model writes. Example: O5 (work backwards) fires when the goal state is concrete and forward branching is large. Log each time the cue was present and whether the operator was used.

**4.2 Control layer (Schoenfeld 1982-1985).** Three jobs: monitor (what am I doing, is it paying off), assess (should I change), curtail (stop a path). In the schema this is program code, not a model decision. Mechanism: a budget slice per path, a progress counter (check outcomes, distinct candidate answers, repeated error), and a rule that fires S6 when the counter stalls. This agrees with G1 and S6. LLM analogue: Meta-Reasoner (d04) uses a bandit that reads a short progress report and picks continue, backtrack, switch or restart. Ablation: bandit 89 vs the model choosing for itself 82 vs no controller 4 on Game of 24. Caveat: author-run, GPT-4o-mini.

**4.3 Strategy selection (Schoenfeld 1978; MRP; Self-Discover).** The student learns which technique to pick. LLM versions: Self-Discover picks reasoning modules (select, adapt, implement); MRP picks one of several prompting methods. Selection needs a model strong enough to judge the match; GPT-3.5 selection hurt (d03). Implementation: select from the outcome record in code (class record in memory), not by asking the model which it prefers. No selection accuracy has been published (gap 4).

**4.4 Worked example with the strategy named.** Schoenfeld a01: seeing solutions alone did not teach the heuristics; seeing the heuristic behind each step did. Implementation: every retrieved example carries a label line "strategy: work backwards; cue: concrete goal." Didolkar (b24): skill-label indexing beats topic indexing (+3.5 on MATH).

**4.5 Abstraction before solving (step-back).** Ask for the governing principle first, then solve with it. Works where the failure is a missing or misapplied principle (physics, knowledge QA). Nothing on GSM8K. Over 90% of its errors are in the reasoning step; it moves error between stages (fixes 20.5%, breaks 11.9%).

**4.6 Decomposition (least-to-most, plan-and-solve).** Break into subproblems and solve in order. Value rises with solution length: 2 steps worse than plain, 5+ steps better (+6.2 points). Implementation: estimate step count (code or a cheap call), trigger decomposition above a threshold. Plan-and-solve cuts missing-step (12% to 7%) and calculation errors, not misunderstanding (27%).

**4.7 Verification as look-back.** Works only against a sound signal: tests, a program, a checked second route. Not as a "check your answer" prompt (b25). Implementation: S8 uses code checks; a model critique is allowed only when it cites a located failing output (G2).

**4.8 Heuristic diversity.** Sample k attempts under k different named heuristics, not k under one prompt (DIV-SE). Gains on GPT-4 on planning and graph problems. Schema G4 bans persona or strategy voters on single-answer problems. DIV-SE changes the approach, not persona, and a checker verified the gain, but this is single-source and untested on reasoning models, so it stays in the Test list.

**4.9 Behaviour priming for training (Gandhi; RRV).** Reasoning behaviours (verification, backtracking, subgoal setting, backward chaining) in the starting model predict whether RL improves it. Training-time. We do not train. The transferable part is the behaviour list, which maps onto O3, O5 and S8.

**4.10 Cognitive-operation prompts (Kramer and Baumann).** A fixed list of operations (goal clarification, decomposition, filtering, pattern recognition, integration). Mid-size open models gained, up to about 95% on LLaMA 70B GSM8K; strong models are near ceiling.

## 5. What holds up

**Replications and cross-checks.**
- Heuristics alone are weak in humans. Two independent lines agree: Schoenfeld's review and the Sweller group's review (K01, E).
- Self-correction without an outside signal fails. Huang 2024, Stechly 2024 and the Kamoi 2024 survey agree (K18, E). Debate does not beat self-consistency at equal responses (c19, d08).
- A generic trigger gives large gains on non-reasoning models (Kojima, Wei; K10, E).
- Word-problem meta-analyses give g about 0.56 to 0.71 (K09, E), but they do not isolate heuristic teaching.

**Failures and null results.**
- Step-back on GSM8K: no gain (84.3 vs 84.4).
- Least-to-most on 2-step items: worse (74.53 vs 76.68).
- MRP selection with GPT-3.5: GSM8K 83.1 to 78.1; macro below SPP.
- Reasoning models: step-by-step +0.029, +0.031, -0.033 on GPQA Diamond; richer decomposition prompts no better (d01).
- Few-shot prompting degraded DeepSeek-R1 (c22).
- At equal budget, CoT self-consistency matches or beats plan-and-solve and least-to-most (d08, plots only).
- Hembree: heuristic teaching no better in K-5.
- Inscribed square moved only 9% to 20%; some heuristics were not teachable (a20).
- GPT-3.5 CommonSenseQA under self-correction 75.8 to 38.1.
- Wrong-answer Polya-style variants in RRV fell below vanilla RL on all six benchmarks.

**Moderators found.**
- Task type: math, symbolic, logic gain; knowledge tasks little (a37).
- Problem length: decomposition pays at 5+ steps, not at 2 (c06).
- Model strength: selection and meta-roles help strong models (GPT-4) and hurt weak ones (GPT-3.5); monitor-and-control gains shrink near ceiling (Gemini-2.0-flash 94.93 to 96.73); reasoning models gain nothing from generic heuristic prompts.
- Grade level in humans: none at K-5, mild at 6-8, distinct in high school (Hembree); grade 7 vs grade 5 in a21.
- Cue clarity: cue-driven heuristics learn, vague ones do not (d13).
- Where the error lives: planning prompts remove missing-step errors, not misunderstanding; Self-Discover structures were correct 87.5% of the time yet 74.7% of MATH failures were computation errors.
- Verifier presence: a sound external check turns a loss into a gain.

**Interventions that worked.** Explicit named-strategy worked examples (Schoenfeld lab). Heuristics plus managerial control in a classroom (21 to 73). External controller over strategies (89 vs 82 vs 4). Skill-labelled retrieval (+3.5 over topic). Cue-triggered concrete heuristics. A sound verifier plus resampling.

**Interventions that did not.** A heuristic list without control. Model self-critique. Method selection by a weak model. Heuristic text added to a reasoning model. Debate.

**Weak spots.** Almost all LLM claims are single-paper and 2022-2024 models. Founding human samples are tiny (7; 11 vs 8). Effect sizes for Schoenfeld, Koichu, Hembree were not found. Mason et al. has no data. Equal-token comparisons are rare; only d08, Self-Discover and BoT report cost.

## 6. Language models

**Non-reasoning models (2022-2024).**
- One generic trigger is a very large effect (b10, b11). Human-style heuristic teaching never matched it.
- Richer heuristics add little on top. Plan-and-solve +2.9 on GSM8K over zero-shot CoT and equal to manual 8-shot CoT on average (76.7 vs 77.6). Least-to-most +1.5 on GSM8K. Step-back 0 on GSM8K but +7 to +15 on physics and chemistry. Analogical +1 to +3. Self-Discover +6 to +7 on BBH, +2 on MATH for GPT-4.
- Gains are task-shaped. Structured symbolic problems show huge gains (SCAN 99.7 vs 16.2; Game of 24 82.4 vs 11.0). Word problems show small gains.
- Stacking with sampling: PS+ 58.7 to 73.7 with self-consistency, but plain CoT with SC reaches 70.7 (c03), so PS+ adds about 3 points at 10 samples. At equal budget plain CoT-SC is as good (d08).
- Selecting a method is a capability that appears only with a strong model (MRP).
- Self-verification fails alone (b25) and works with an outside signal (d06).

**Reasoning models (2025-2026).**
- Reasoning behaviours (re-evaluation, "wait") emerged from verifiable-reward RL without taught heuristics (c22). Few-shot hurts R1.
- Meincke 2025: step-by-step prompting changed o3-mini, o4-mini and Gemini Flash 2.5 by +0.029, +0.031, -0.033 on GPQA Diamond at 4,950 runs per cell; richer prompts no better.
- Plan and Budget (d12): decomposition plus token budgets on R1 distills, QwQ and o4-mini kept MATH-500 accuracy while cutting tokens (E3 efficiency +29.4% for DS-LLaMA-70B, +20.3% for o4-mini; TravelPlanner up to +193.8%). This is a cost gain, not an accuracy gain.
- No study tests a Polya-style prompt on a reasoning model at matched tokens on maths. This is the biggest hole.

**Control-layer systems.**
- Meta-Reasoner: 89 vs 82 vs 4 (Game of 24).
- Metacognitive consolidation: monitor and control 79.20, updates alone 80.47, bare 72.67, full 85.13 on MATH-500 GPT-4o-mini. Lesson updates carried most of the gain. Table partly garbled; the abstract quotes a different baseline (78.93).
- Both are author-run on older non-reasoning models.

**Training-time use.**
- Gandhi 2025: behaviour-rich priming closes the 60% vs 30% Countdown gap; empty chain-of-thought stays at 30-35%. Transfer to MATH seen only in Qwen (38 to 50%; backtracking frequency 0.15 to 0.59).
- RRV 2026: up to 64 heuristic variants per question; pass@64 +1.87 average; breadth over depth (about 7% relative); wrong-answer variants hurt.
- Llama-Polya 2026 (a36): about 32,000 Polya-staged tutoring dialogues; stage-annotation error rate 0.0% vs 0.4% (metamath). This measures format adherence, not solving gains.
- Huan 2025 (d16): math RL generalises across domains, math SFT drifts. Prompt-level cross-family transfer is untested.

**Drift.** Instruction text placed once decays within about 8 rounds (d11). Applies to any heuristic block in a long run.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, memory.

### Add now (established)

1. **No self-review pass without an outside signal.** Part: G2, S8, section 4b. b25, c18, d06, d07, K18. [E]. Action: already in G2 and 4b; cite these ids there. Nothing new to add.
2. **Plain model is the default; heuristic text is not added to the core.** Part: G7, G11. d01, d12, c22 (K24, K25). Status: the direction is consistent across sources but each is [S]; it is justified mainly by G7, which is [O]/[E] already. Action: operators run only at S6 or in open mode (already so).
3. **Control stays in code.** Part: G1, S6, section 1. Heuristics alone are weak (K01 [E]: a05, b04); Schoenfeld control findings (K04, a06, a08 [S]) and external controller over self-selection (K27, d04 [S]) point the same way. Action: no change; record that S6's code-fired trigger is the control layer this literature asks for.
4. **Generic step-by-step trigger is the one large replicated heuristic effect, and only on non-reasoning models.** Part: S0 mode choice. K10 [E]; moderator by model type K11, K25 [S]. Action: S0 picks step-by-step mode only for non-reasoning cores and symbolic or math classes.
5. **Every heuristic arm gets an equal-token plain repeated-attempt arm.** Part: G7. K26 [S] for the finding, principle already [O]. Action: apply in all tests (section 8).

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Cue-triggered operators: each O1-O8 gets a code-evaluable trigger | O, S6 | [S] | d13, K31 |
| T2 | Decomposition (O3) gated by a step-count estimate; off for short problems | O3, S0 | [S] | c06, K13 |
| T3 | Principle/abstraction step only on knowledge-heavy items | O2, S1 | [S] | b15, K14 |
| T4 | Operator selection from outcome record in code vs model self-selection | S6, memory | [S] | d04, d02, d03, K03, K27 |
| T5 | Heuristic x control 2x2 ablation | G, S6 | [S] | K02, d04, d05 |
| T6 | k attempts under k named heuristics vs same-prompt resampling | S3, O | [S] | d09, K29 |
| T7 | Lesson memory labelled by strategy name and indexed by skill | memory | [S] | b24, a01, K22 |
| T8 | Re-inject the active operator text at each step | G, S6 | [S] | d11, K30 |
| T9 | Analogue recall self-generated vs fixed exemplars, shown after first attempt | O7, memory | [S] | b20, c10, K16 |
| T10 | Tool/computation check vs more heuristic structure | S4, S8 | [S] | b18, K15, a38 |
| T11 | Concrete procedure text for arithmetic-like subskills vs generic hint | memory | [S] | b27, K21 |
| T12 | Cross-family transfer of an operator | O | [S] | d16, K32 |
| T13 | Template library (BoT style) built from solved items | memory | [S] | c14, K17 |

Contested and not to be added either way: strategy teaching vs schema/worked examples (K08 [C]); counting heuristic use (K07 [C]).

## 8. Concrete tests on our bench

All arms at equal total tokens, setup included (G7). Use at least 25 trials per cell for rating metrics; for exact-match items use pass rate with a paired bootstrap. Run on the production core and on one small non-reasoning model to expose the moderator.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Heuristic block on/off | math and puzzle items with checks (GSM8K-type, MATH, Game of 24-type, ARC-like) | plain; plain with extra samples at matched tokens; Polya block prompt | pass rate, tokens | reasoning core within +/-0.03; non-reasoning +0.03 to +0.10 (from d01) |
| B2 Heuristic x control 2x2 | same set plus one family with hard impasses | none; heuristic list only; control only (code-fired S6, generic retry); both | pass rate on hard items; tokens to first pass | both > either > none; if heuristics-only equals none, the control claim holds |
| B3 Cue-gated vs always-on operators | items where O3 or O5 clearly apply and items where they do not | always-on O1-O8 at S6; cue-gated; none | pass rate; use rate when cue present; wasted calls when absent | gated >= always-on with fewer wasted tokens |
| B4 Decomposition gate | GSM8K split by gold step count (2, 3-4, 5+) | always decompose; gate at 4 steps; never | pass rate per bucket | helps at 5+ (about +6 points on old models), hurts at 2 |
| B5 Selection by code vs by model | mixed families (symbolic, arithmetic, knowledge) | model picks; code picks from class record; random; best fixed single | pass rate; selection accuracy vs oracle operator | code >= model on weak cores; yields the selection accuracy no paper reports |
| B6 Diversity | graph colouring, Blocksworld-like planning, MATH counting | k samples one prompt; k under k named heuristics; code verifier | pass@k with verifier | +10 to +30 points where a verifier exists; null on a reasoning model drops the idea |
| B7 Look-back variants | items with and without checks | model self-review; code/test check; extra samples | net fixed minus broken; pass rate | self-review <= 0; code check and samples positive |
| B8 Lesson label | repeated-class stream | untagged lessons; strategy-named; skill-indexed | pass on next problems of the class | 0 to +4 points |
| B9 Drift probe | 50-step runs | operator text once; re-injected each step | operator-use rate at steps 5, 20, 50; pass rate | use rate falls without re-injection |
| B10 Transfer | one family held out per operator | build lessons on family A, test on B | gain on held-out vs in-family | held-out gain smaller than in-family; thresholds in UNKNOWNS |
| B11 Heuristic-use rubric | traces from B1-B5 | two raters, or rater plus code detector, fixed written rule | agreement (kappa), use rate | kappa >= 0.7 before any use-rate claim |

## 9. What does not transfer, and why

- **Human classroom gains do not map to a model.** Humans lack the heuristic and must learn it. Models already hold heuristics in weights and have a generic trigger. The model effect is activation, not learning.
- **"Teach a long heuristic list."** Evidence for lists alone is weak in humans (K01) and small in LLMs on strong cores. Do not keep an operator because Polya listed it; O1-O8 are all [S].
- **Grade and age moderators** (Hembree) do not map to model size one to one. The LLM parallel is the weaker-model gain, not a developmental stage.
- **Self-check by reflection.** The human look-back habit pays because a person can re-derive and notice an error. A model checking its own text shares its blind spots (b25). So S8 uses code and S9 records a lesson.
- **Belief systems and motivation** (Schoenfeld's fourth component) have no analogue.
- **Heuristic fluency measured by coding manuals** is unstable even for humans (d15). A count of "heuristic words" in a model trace is not evidence of use (G10).
- **Training-time findings** (Gandhi, RRV, Llama-Polya) do not apply because we do not train. Their value is as a hint about which behaviours matter.
- **Puzzle-only gains** (Game of 24, SCAN) where a trick exists do not carry to open problems; BoT's gain is largest where a known trick exists.
- **Prompt text on reasoning models.** Few-shot hurt R1; step-by-step added about nothing.

## 10. Open questions

1. Does any Polya-style prompt beat plain output on a reasoning model at matched tokens on maths? No measured study; d01 covers GPQA only.
2. Does a control layer add effect beyond heuristics? No clean 2x2 exists.
3. Do heuristics transfer across problem families at prompt level? Open.
4. What is operator-selection accuracy, and what does a wrong selection cost? Not reported anywhere found.
5. What are the true effect sizes in Schoenfeld-type studies and Hembree 1992? 1979 gave none; Hembree not read beyond the abstract.
6. Are gains larger for weaker solvers (human Koichu result unknown), and does that match small vs frontier models? Partial LLM support only.
7. When does verification pay at equal tokens on a reasoning model with a tool signal? Not tested.
8. Does heuristic diversity beat same-prompt resampling at equal tokens on reasoning models?
9. Do gains persist? Human delayed tests (Hohn and Frey) not opened. LLM analogue is drift (d11).
10. How should heuristic use be measured in agent traces? Rott's coding problem; no LLM-trace study.
11. Koichu sample: N=92 vs 37 eighth graders in Rott's summary. Unresolved.
12. Heuristic vs schema/worked-example effect at equal tokens (K08).

## 11. Sources

[V] opened and read this session; [M] snippet or abstract only.

**Human studies and reviews**
- [V] Schoenfeld (1979) Explicit heuristic training as a variable in problem-solving performance (d13). https://www.ime.usp.br/~alpereir/cursosdosemestre/resprob/schoenfeld_heuristics_79.pdf
- [M] Schoenfeld (1979) ERIC record. https://eric.ed.gov/?id=EJ202121
- [V] Schoenfeld (1982) Expert and novice mathematical problem solving, NSF final report. https://files.eric.ed.gov/fulltext/ED218124.pdf
- [V] Schoenfeld (1983) Theoretical and pragmatic issues in the design of mathematical problem-solving instruction. https://files.eric.ed.gov/fulltext/ED228045.pdf
- [M] Schoenfeld (1978) Presenting a strategy for indefinite integration, as cited in ED218124.
- [V] Liljedahl, Santos-Trigo, Malaspina, Bruder (2016) Problem Solving in Mathematics Education (summaries of Mason, Perkins, Schoenfeld). https://link.springer.com/content/pdf/10.1007/978-3-319-40730-2.pdf
- [V] Sweller, Clark, Kirschner (2010) Mathematical ability relies on knowledge. https://files.eric.ed.gov/fulltext/EJ909939.pdf
- [V] Rott (2015) Rethinking heuristics. https://journals.helsinki.fi/lumat/article/view/1055
- [V] Eisenmann et al. (2015) Impact of heuristic strategies. https://www.eriesjournal.com/index.php/eries/article/download/114/117
- [V] Haenze and Leiss (2022) Heuristic worked examples. https://link.springer.com/content/pdf/10.1007/s11251-022-09583-8.pdf
- [V] Kuzle (2019). https://files.eric.ed.gov/fulltext/EJ1239972.pdf
- [V] Kaitera and Harmoinen (2022). https://files.eric.ed.gov/fulltext/EJ1358674.pdf
- [V] Hembree (1992) abstract page only. https://doi.org/10.2307/749120
- [M] Lucas (1974) https://eric.ed.gov/?id=ED072940
- [M] Charles and Lester (1984) https://eric.ed.gov/?id=EJ290486
- [M] Kantowski (1977) https://eric.ed.gov/?id=EJ161029
- [M] Koichu, Berman, Moore (2007) https://eric.ed.gov/?id=EJ753950
- [M] Hohn and Frey (2002) https://eric.ed.gov/?id=EJ660159
- [M] Eisenmann et al. (2015, culture) https://eric.ed.gov/?id=EJ1082974
- [M] Higgins (1993) https://eric.ed.gov/?id=ED365521
- [M] Pereira-Mendoza (1979) https://eric.ed.gov/?id=EJ216587
- [M] Lein et al. (2020) https://eric.ed.gov/?id=EJ1269779
- [M] Myers et al. (2023) https://eric.ed.gov/?id=EJ1379174
- [M] Zhang and Xin (2012) https://eric.ed.gov/?id=EJ974918
- [M] Lenat (1983) https://doi.org/10.1016/S0004-3702(83)80005-8
- [M] Newell and Simon (1972) https://en.wikipedia.org/wiki/General_Problem_Solver
- [M] Hembree (1992) mirror https://www.bohrium.com/paper-details/experiments-and-relational-studies-in

**LLM studies**
- [V] Wei et al. (2022) Chain-of-thought prompting. https://arxiv.org/abs/2201.11903 (b11 opened; c25 not extracted)
- [V] Kojima et al. (2022) Zero-shot reasoners. https://arxiv.org/abs/2205.11916
- [V] Zhou et al. (2023) Least-to-most. https://arxiv.org/abs/2205.10625
- [V] Wang et al. (2023) Plan-and-solve. https://arxiv.org/abs/2305.04091
- [V] Zheng et al. (2024) Step-back. https://arxiv.org/abs/2310.06117
- [V] Yasunaga et al. (2024) Analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271
- [V] Suzgun and Kalai (2024) Meta-prompting. https://arxiv.org/abs/2401.12954
- [V] Kramer and Baumann (2024) Cognitive prompting. https://arxiv.org/abs/2410.02953
- [V] Didolkar et al. (2024) Metacognitive capabilities. https://arxiv.org/abs/2405.12205
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Zhou et al. (2022) Algorithmic reasoning in context. https://arxiv.org/abs/2211.09066
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183
- [V] Gandhi et al. (2025) Cognitive behaviors. https://arxiv.org/abs/2503.01307
- [V] RRV et al. (2026) Mid-training with self-generated data. https://arxiv.org/abs/2605.08472
- [V] Lee et al. (2026) Llama-Polya. https://arxiv.org/abs/2602.10597
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948
- [V] Meincke, Mollick, Mollick, Shapiro (2025) Prompting Science Report 2. https://arxiv.org/abs/2506.07142
- [V] Gao et al. (2024) Meta reasoning prompting. https://arxiv.org/abs/2406.11698
- [V] Sui et al. (2025) Meta-Reasoner. https://arxiv.org/abs/2502.19918
- [V] Zhuang et al. (2026) Metacognitive consolidation. https://arxiv.org/abs/2604.17399
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations. https://arxiv.org/abs/2402.08115
- [V] Kamoi et al. (2024) When can LLMs correct their mistakes. https://arxiv.org/abs/2406.01297
- [V] Wang et al. (2024) Reasoning in token economies. https://arxiv.org/abs/2406.06461
- [V] Naik et al. (2024) Diversity of thought. https://arxiv.org/abs/2310.07088
- [V] Hegazy (2024) Diversity of thought in debate. https://arxiv.org/abs/2410.12853
- [V] Li et al. (2024) Instruction drift. https://arxiv.org/abs/2402.10962
- [V] Lin et al. (2026) Plan and Budget. https://jshun.csail.mit.edu/PlanBudget.pdf
- [V] Huan et al. (2025) Does math reasoning improve general LLM capabilities. https://arxiv.org/abs/2507.00432
- [M] Breaking barriers: RL post-training transfer (2026). https://arxiv.org/abs/2506.19733
