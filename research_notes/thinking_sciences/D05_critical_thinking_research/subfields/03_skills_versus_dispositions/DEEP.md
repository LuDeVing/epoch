# Skills versus dispositions: deep document

*Subfield D05.03. Writer pass over evidence_a to evidence_d.jsonl, claims.jsonl (K01 to K33) and critique.md. Evidence ids (a01, b07, d16 ...) point to the jsonl files in this folder. Numbers marked "corrected" follow critique.md.*

## 1. What it is

Critical-thinking research splits good thinking into two parts.

- **Skills (abilities):** what a person can do. Inference, argument analysis, evaluating credibility, interpretation, explanation, self-regulation.
- **Dispositions (habits):** what a person tends to do and when. Inquisitiveness, open-mindedness, fair-mindedness, willingness to revise, persistence, alertness to the occasion for thinking.

The split asks one question: why do people who can reason well often fail to do so? The usual answer is that the ability is there but is not used, or is used one-sidedly. Perkins, Jay and Tishman (1993) named three parts: sensitivity (notice the occasion), inclination and ability. Most failures, they argued, are failures of sensitivity, not of ability (a11, b27, recalled; K18 single-source).

Key authors: Ennis (taxonomy of dispositions and abilities, 1987, 1996), Facione (Delphi report 1990; CCTDI and CCTST tests), Halpern (transfer, 1998), Stanovich and West (actively open-minded thinking, AOT), Perkins (dispositional theory).

Why it matters for our agent. The agent is one language model run inside a scaffold: a fixed set of rules that move the model through states. Two things follow.

1. In a model, skill and disposition come apart even more sharply than in people. Models can critique, and can fix a located error. They do not reliably do it unprompted, and they bend to pressure. That is a disposition failure with skill intact (K07, K08, K10).
2. We do not train. So a "disposition" can only be installed as a rule in code (a trigger) or as a prompt line. The evidence says code triggers work and prompt-level dispositions mostly do not (K05, K06, K09, K24).

Our working mapping (a27, own synthesis, not measured):

| Human disposition | Type | Schema form |
|---|---|---|
| Alertness to the occasion; prudence in altering judgment; abandon a nonproductive strategy | trigger | code-fired signals: G1, S6 impasse |
| Willingness to revise | trigger plus evidence | revise only from real failing output: G2, S5 |
| Fair-mindedness; honesty about own bias | value | model-blind judging G5; input hygiene S1 |
| Open-mindedness | value; without a filter it is gullibility | movement only from checkable output: G2, G3 |
| Persistence | budget | G6, G7, G12 |

## 2. History and theories in depth

**Ennis (1987, 1996).** Critical thinking is reasonable, reflective thinking about what to believe or do. Ennis wrote taxonomies of dispositions (focus on the question, seek reasons, be well informed, care about the dignity of persons) and abilities. His Cornell tests measure abilities: Level X has 76 items, 24 on credibility; Level Z has 52 items (a06). His 1996 paper argues dispositions are hard to assess directly (b28, conceptual, not opened). The primary Ennis texts were not opened.

**Perkins, Jay and Tishman (1993).** A dispositional theory of thinking: sensitivity, inclination, ability. Observed example: students write one-sided "myside" arguments though able to write balanced ones (b27, recalled, no figures). Not opened.

**Facione and the Delphi project (1990)** (a01 to a04, opened). The panel had 46 experts over six rounds (Feb 1988 to Nov 1989). Mix: 52% philosophy, 22% education, 20% social science, 6% physical science. Result:

- Six core skills: interpretation, analysis, evaluation, inference, explanation, self-regulation. Analysis, evaluation and inference were central at above 95% agreement; the other three above 87%.
- 19 affective dispositions in two groups. 12 about life in general: inquisitiveness, staying well informed, alertness to opportunities to use critical thinking, trust in reasoned inquiry, self-confidence, open-mindedness, flexibility, understanding others, fair-mindedness, honesty about own biases, prudence in suspending, making or altering judgments, willingness to reconsider and revise. 7 about specific issues: clarity, orderliness, diligence, reasonableness, care in focus, persistence, precision. 83% consensus that a good thinker shows these.
- 61% said dispositions are part of the meaning of "critical thinking". About one third said it means cognitive skills only.
- The panel itself stated that research on how sub-skills correlate with each other and with dispositions "has yet to be undertaken" (a04).

So the skills-plus-dispositions definition was adopted by expert vote before anyone measured how the two relate. The vote was opinion, not data (K01).

**Facione, Facione and Giancarlo (CCTDI, 2000).** The California Critical Thinking Disposition Inventory. Reported correlations with the skills test are said to be roughly r .1 to .4 (b26, recalled, not opened). The skills test (CCTST) has 34 items, 11 on inference and 5 on argument analysis (a06). Factor-structure criticisms were not read.

**Halpern (1998).** Teaching for transfer: skills training plus a disposition to use the skills, structural awareness and monitoring. One disposition she names is willingness to abandon nonproductive strategies and self-correct (a06). The SEP entry calls the evidence for transfer across domains "scanty" (a06). The 1998 paper was not opened (a12).

**Stanovich and West (1997, 2007).** The actively open-minded thinking (AOT) scale and the Argument Evaluation Test (AET), which measures whether people rate arguments independent of prior belief. Disposition is said to predict it beyond cognitive ability (b25, recalled; a09). Neither primary paper was opened (d17, paywalled). Recalled only: AOT-AET correlations around .3 to .4 after ability control; myside bias nearly uncorrelated with ability. Treat as unverified.

**Haran, Ritov and Mellers (2013)** (d16, opened). First primary data on mechanism. See section 4.6.

**Later strands.** Pennycook and Rand (2019, b29): "lazy, not biased". Analytic thinking predicts discernment of false news, supporting a "does not engage" account over a "motivated" one (recalled). Pennycook et al. (2015, b19): analytic disposition and ability both predict lower acceptance of profound-sounding nonsense; four studies, N=279, 187, 114, 232.

**LLM era.** Questionnaires (Zhou 2025), behaviour probes (sycophancy: Sharma 2024, SycEval, SYCON), self-correction studies (Huang 2024, Tyen 2024, Self-Correction Bench) and judge-bias studies (Panickssery 2024) each probe part of the disposition set without calling it that. See section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Expert consensus: CT = skills + dispositions | 46 experts, 6 rounds; 19 dispositions, 83% consensus; 61% say dispositions are part of the meaning | a01-a03 (Facione 1990) | single-source (opinion) |
| Skill-disposition correlation is weak to moderate in teens | T1 disposition-CT r=.29; WM-CT r=.35; WM-disposition r=.10; N=509 (601 at T1) | b01 | established with b02, b26 |
| Working memory predicts later CT more than dispositions do | T1 WM to T2 CT beta=.28; dispositions beta=.15; Wald chi2(1)=7.27, p=.007; CT to later dispositions beta=.10, p=.016 | b02 | single longitudinal study |
| Metacognition correlates strongly with CT skill | r=.649, 95% CI [.593,.704]; 60 effects, 24 articles | b07 | contested (self-report inflation) |
| Dispositions help decision-making in children | CTD to decision-making beta=.65; to problem solving .31; indirect effect .20, CI [.095,.308]; N=285 | b06 | single source, self-report |
| AOT helps by changing information search, not processing | N=183/220/200; AOT-CRT r=.300; AOT-need for cognition r=.355; Study 3 B=.217, R2=.047, p=.002; fixed information: all B<=.112, p>=.10 | d16 | single-source for "beyond ability" |
| Analytic disposition and ability both reduce gullibility to nonsense | BSR with CRT r=-.33; verbal intelligence r=-.37; Raven r=-.26 | b19 | correlational |
| Teaching raises CT modestly | Overall g=.30 (341 studies); disposition outcomes g=.23 (25 studies); content-specific CT g=.57 (97); dialogue+application+mentoring g=.57 (19) | a07 (Abrami 2015, corrected) | established |
| Single quasi-experiments overstate gains | skills d=3.04 to 3.52 (N=114); dispositions d=.44 to 1.12; control no change | b03, b04 | not transferable (test-matched) |
| Reflective skepticism is hardest to move | skills d=.99; openness d=.60; skepticism 15.43 to 16.12, p=.23; n=16, no control, alpha .41/.53 | b05 | single-source, weak |
| LLMs match humans on disposition scales, fail applied tasks | CTDS 0.72 to 0.93, AOT 0.71 to 0.79 (human=1.0); defeasible reasoning accuracy 0.17 to 0.67 | a14, a15, b11, b12 (Zhou 2025) | single-source; no model names attached |
| Intrinsic self-correction does not help reasoning | GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8; GSM8K 75.9 to 75.1 to 74.7; GPT-4 GSM8K 95.5 to 91.5 to 89.0; HotpotQA 49 to 49 to 43 | a19, b15, c01 (Huang 2024) | established (4 sources) |
| With oracle labels it works | GPT-3.5 GSM8K 84.3, CSQA 89.7, HotpotQA 29.0; GPT-4 97.5, 85.5, 59.0 | b16 | established |
| The bottleneck is finding the error | GPT-4 step-level mistake finding 52.87 overall (direct step), 39.80 trace-level, 43.40 CoT step; GPT-3.5-Turbo 14.78 overall | c02 (Tyen 2024, corrected) | established |
| Models fix others' errors more than their own | blind spot 64.5% over 14 non-reasoning models; Haiku 3.5 52.5%, Sonnet 4 41.4%; "Wait" cut it 89.3% and raised mean accuracy 156%; LoRA on 5,306 traces cut it 76.0%; natural errors caught 4.3 to 10.8% | a18 | single-source |
| Tool feedback works, no-tool critique barely | ChatGPT AmbigNQ EM: CoT 51.8, CRITIC 59.8, without tool 55.2; Davinci F1 w/o tool 58.3 vs CoT 58.6 | a25, c17, d12 | established |
| Self-Refine reports gains | about +20% absolute on 7 tasks (open and preference-like tasks) | a24, c25 | contested vs Huang; resolved by task type |
| Models cave under challenge | Claude 1.3 admits mistakes on 98%; "Are you sure?" lowers accuracy up to 27% (Claude 1.3); changes first answer 32% (GPT-4) to 86% (Claude 1.3); a suggested wrong answer lowers accuracy up to 27% (LLaMA 2) | a23, b17, c04 (Sharma 2024) | established |
| Reasoning models still cave | 8 of 9 beat GPT-4o (d=.12 to .40) but a suggested wrong answer is the strongest attack; Self-Doubt (338) and Social Conformity (337) = 50% of failures; reconsideration: mean accuracy 60.4 to 54.2 (-6.3 pp), o3 -7.0, R1 -6.0 | d01, d03 | established (3 sources) |
| FlipFlop effect | flips 46% of the time; mean accuracy drop 17%; fine-tuning cut deterioration 60% | d06 | single-source |
| Update rate is a poor open-mindedness score | after rebuttal: sycophantic 58.19%; progressive (to correct) 43.52%; regressive (to wrong) 14.66%; preemptive 61.75% vs in-context 56.52%, Z=5.87 | c06 (SycEval) | established with a17, b13 |
| Open-mindedness without a filter is gullibility | 222 of 575 model-issue pairs (38.6%) have >=95% prior; Llama 8B shifted 12.2% on one-sided arguments; Opus 4 refusals vanish: abortion 37.8, sanctuary cities 68.9, gun control 83.3% | a16, a17, b13, b14 (MillStone) | contested (no ground truth) |
| Scale and RLHF raise deference | PaLM 8B to 62B +19.8%, 62B to 540B +10.0%; instruction tuning +26.0% on 8B | c05, c20, b18 | established |
| Judges favour own output | GPT-4 self-recognition 73.5%; self-bias GPT-4 0.749; GPT-4 TPR .945 vs TNR .425; bias tracks low perplexity | c15, d14, d15 | single-source |
| Confidence is a weak trigger | confidence-gated defence GPT-5.1 98.50 baseline vs 98.39; flip of correct answers 9.3% in low-confidence vs 6.2% in high; ChatGPT fails to defend correct answers in 22% to over 70% | c19, d02, d07 | established |
| Reasoning text hides causes | biasing features cut accuracy up to 36%, never mentioned; R1 admits the "Stanford Professor" cue 59% vs V3 7% | c14, d05 | single-source (G10 in schema) |
| Reflective habit appears with scale | CRT correct: humans 38%, davinci-003 5%, ChatGPT-3.5 59%, ChatGPT-4 96%; intuitive-wrong 55%, 80%, 15%, 0% | c13 | single-source |
| Awareness prompt weak, restructure better | self-help left 0 to 6% of biased prompts; one bias made the model admit 40.5% more students | c21 | single-source |
| Third-person framing resists flips | Turn of Flip up to +63.8% (debate); anti-sycophancy line up to +28% (unethical queries); 17 LLMs | d09 | single-source |
| "Wait" helps a reasoning model | s1-32B AIME24 50% to 57% | d13 | single-source |
| Auditing needs an instruction | ProcessBench F1 o1-mini 87.9 vs GPT-4o 61.9 | d10 | single-source |
| Critical-question checklist | about +4.61% reasoning, +5.4% math on MT-Bench; 5 LLMs; best in 18 of 20 | d11 | single-source, extra compute |
| LLM grading of CT subskills is unreliable | Krippendorff alpha .23 to .74; GPT-5 few-shot .532 vs fine-tuned Llama 8B .604 | c10, b20 | contested |
| Humans inherit LLM errors | N=24; wrong medium-length explanation caught 54%, short 25%, long 31% | c12 | single-source |
| Our own test | plain 92% vs forced doubt 75% (n and CI not recorded) | a26 | [O], open gap |

## 4. Mechanisms and models

Explained as parts an engineer can build.

**4.1 Sensitivity, inclination, ability (Perkins).** Treat a thinking step as three tests: was the occasion noticed, was the agent moved to act, did it have the skill. In our agent the first two are code: a detector fires and the state machine moves. The third is the model filling a slot. Two failures to measure separately: trigger present and no fire (sensitivity miss), and fire with a wrong repair (ability miss). The sensitivity miss on natural errors has not been measured (GAP 2).

**4.2 Find versus fix (Tyen).** Self-correction has two steps. Locate the first wrong step. Repair it. Models repair well when told where (backtracking with the true location: +18.04 and +18.06 on incorrect traces, but -8.89 and -15.91 on correct traces, so a false alarm costs nearly as much as a true alarm gains; worked example in a20: base accuracy 50% rises to 68.6%, base 99% falls to 92.8%). Implementation: code locates the failing step by running a check; the model only repairs. Never ask the model whether the trace has an error.

**4.3 Trigger quality decides the sign.** From the Tyen example, an alarm helps only if its precision beats the base error rate. Intrinsic "review your answer" has low precision, so it harms (Huang). A code check, test failure or disagreement between independent attempts has higher precision, so it helps (CRITIC; Reflexion 91% HumanEval vs 80%). Implementation: log precision and recall of every trigger per problem class and drop a trigger that fails the break-even test.

**4.4 Blind spot and "Wait" (Self-Correction Bench).** Blind spot = 1 - internal accuracy / external accuracy, where external means the same error placed in a user turn. Non-reasoning models almost never learned correction markers (median frequency 0 in their fine-tuning data). Appending "Wait" restores the behaviour. Reasoning-class models show a small or negative blind spot (a18), and "Wait" still helps one (d13). Implementation: when a trigger fires, the revision turn starts with a fixed cue. The cue is never on by default.

**4.5 Open-mindedness as evidence-driven update (two-sided score).** Split belief changes into progressive (wrong to right, caused by real evidence) and regressive (right to wrong, caused by pressure). SycEval gave 43.52% progressive and 14.66% regressive after rebuttal, so a high update rate hides harm. Score design: (a) flip rate on correct answers under challenge with no evidence (bad); (b) fix rate on wrong answers when real evidence is shown (good). Report both. No validated version exists (K29).

**4.6 AOT works through search (Haran).** The disposition did not improve processing of given information. It changed how much information was gathered. A disposition prompt without a search action cannot help. Implementation: make "gather more" an operator that code offers when attempts disagree, not a mood instruction.

**4.7 Authority and form.** Models are moved by argument form more than by source credibility (Xu 2024: logical-sounding false appeals gave the highest misinformed rates; robustness GPT-4 79.3, Vicuna-13B 52.1, ChatGPT 49.9, Vicuna-7B 36.3). Preference data reward agreement (Sharma). Implementation: S1 input hygiene moves stated guesses and appeals to authority into a marked block that attempts do not see. The judge sees no authorship (G5).

**4.8 Self-preference.** A judge prefers text it recognises as its own, and text with low perplexity. Hiding authorship alone is unlikely to be enough. Add a style-neutral rewrite before judging, or let code judge.

## 5. What holds up

**Established.**
- Weak to moderate link between disposition scales and skill tests (K02). Moderator: self-report inflation. The strongest link (metacognition r=.649) uses similar methods.
- Teaching modestly helps. Skills move more than dispositions (g=.57 content-specific vs g=.23 dispositions, Abrami 2015). Mixed approaches are best (g=.57).
- Intrinsic self-correction of reasoning fails; external feedback succeeds (K05, K06; four to five independent sources).
- Sycophancy is the failure mode of "willingness to revise" and is replicated on non-reasoning and reasoning models (K10, K27).
- Scale and RLHF can worsen deference (K13).
- Confidence is a weak trigger (K24).

**Failed or contradicted.**
- Awareness prompts and "be careful" lines: small effect (K23; SCHEMA 4b).
- Reflection loops: -6.3 pp mean (Jittham 2026; single author, 200 true/false items).
- Confidence-gated defence: no gain (98.50 vs 98.39).
- Self-Refine +20% vs Huang no gain: resolved by task type (open or preference tasks vs single-answer reasoning with hidden errors). Huang's oracle success is feedback, not disposition.
- High quasi-experimental d (3.04 to 3.52) matches the test; ignore (K16).
- Reflective skepticism did not rise after training (b05), but the study is n=16 with alpha .41/.53.

**Moderators.**
- Task type: open tasks vs single-answer with a hidden error.
- Model class: reasoning models have a small or negative blind spot and still cave to a suggested wrong answer (d01).
- Scale: larger was more sycophantic in older families (PaLM); SYCON finds scale and reasoning optimisation reduce it.
- Error source: injected errors (64.5% blind spot) vs natural errors (4.3 to 10.8% catch).
- Prompt form: third-person framing and an anti-sycophancy line each helped (d09).
- Explanation length (humans): medium-length wrong explanations were caught most (c12).

**Replications.** Huang is corroborated by Kamoi (2024), CRITIC and Tyen. Sharma is corroborated by Wei 2024, Perez 2023, SycEval, FlipFlop, Wang 2023, Li 2026 and Jittham 2026. No replication of the human AOT-beyond-ability claim was found; the one primary read (Haran) qualifies it.

**Interventions that worked (human).** Dialogue plus authentic application plus mentoring (g=.57). Mind maps for skills g=.73, I2=97% (b09, abstract only). GenAI tools g=.544, but the prediction interval [-0.588, 1.677] includes zero (b10).

## 6. Language models

**Stated versus shown disposition.** Zhou 2025 found models at or above human level on disposition scales (CTDS, AOT normalised 0.71 to 0.93; human=1.0) yet failing applied tasks: belief bias, bias blind spot, defeasible reasoning (accuracy 0.17 to 0.67). The column-to-model mapping in their appendix was not confirmed, so no model is named. Models beat humans on regret aversion. Hagendorff (c13) shows reflective answers on the CRT rising from 5% (davinci-003) to 59% (ChatGPT-3.5) to 96% (ChatGPT-4), against 38% for humans.

**Self-correction (skill intact, disposition missing).**
- Huang: blind revision cost GPT-3.5 37.7 points on CommonSenseQA. GPT-4 lost 6.5 points on GSM8K by round 2.
- Tyen: GPT-4 finds the first wrong step only about half the time (52.87 overall) but corrects well once told.
- Self-Correction Bench: 64.5% blind spot; "Wait" removes 89.3% of it.
- Kamoi: no demonstrated success with prompted feedback except on tasks exceptionally suited to it.
- Reflexion: 91% HumanEval vs 80%; the trigger is a test result, an outside signal.

**Willingness to revise gone wrong (sycophancy).**
- Claude 1.3 admitted mistakes on 98%; "Are you sure?" cost up to 27% accuracy.
- SycEval: 58.19% sycophantic; 43.52% progressive; 14.66% regressive.
- FlipFlop: 46% flips; 17% mean drop.
- Reasoning models: Li 2026 mean accuracy over follow-up rounds 95 to 99% vs 91.3% for GPT-4o, but a suggested wrong answer is still the strongest attack. Jittham 2026 mean -6.3 pp. Barkett 2025: truth-bias 59.33% reasoning vs 71.00% non-reasoning.
- Chua and Evans (d05): R1 states using the planted "Stanford Professor" cue 59% vs V3 7%. Reasoning models admit hints more often, still not always.
- Levers: third-person framing (up to +63.8% Turn of Flip), anti-sycophancy line (up to +28%), fine-tuning (-60% deterioration), synthetic-data fine-tuning (Wei 2024). Our agent can use only the prompt-level and code-level ones.

**Open-mindedness (MillStone).** 107 issues, about 106,000 prompts per full model. 38.6% of model-issue pairs have a baseline of at least 95% on one side. Authoritative sources move stance. Refusals dissolve once an argument is given. There is no ground truth on opinion issues, so correct-versus-incorrect movement is unmeasured. Do not use these as a calibrated open-mindedness score.

**Judge fairness.** GPT-4 recognises its own text 73.5%; bias score 0.749, but it tracks perplexity. Reasoning models audit far better when told to (ProcessBench F1 87.9 vs 61.9), but natural-error catch without instruction is low (4.3 to 10.8%).

**Direct tests of the skills-versus-dispositions idea on LLMs.** None manipulates a disposition and measures a skill outcome. CQoT (d11), a critical-questions checklist, gave about +4.61% reasoning and +5.4% math on MT-Bench subsets, with extra compute. o1-preview scored 81.25% on one Ennis-Weir item (c08), author-scored: an anecdote. LLM grading of CT subskills is unreliable (alpha .23 to .74).

**Caveats.** Most models are 2023 to 2024 era. Many probes are multiple-choice or true/false. Several are preprints. Reasoning-class conclusions rest on d01 to d03 and d13.

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Treat disposition as a code trigger, not a prompt line. Doubt and revision fire only when a check fails, attempts disagree or the impasse detector fires. Already G1; K05 and K09 add support. | G1 | [E] | K05, K06, K24; a19, b15, d03, d02, d07 |
| A2 | Revision shows the failing output. Code locates the failing step; the model only repairs. | G2, S5 | [E] | K06, K07; c02, b16, a25, c18 |
| A3 | Never use model confidence as a trigger or stopping rule. | G1 | [E] | K24; d02, d07, c19 |
| A4 | A challenge never changes an answer unless code finds a failing check. A stated wrong answer, "are you sure" or an appeal to authority goes to a marked block. | S1, G2 | [E] | K10, K27; a23, c06, d01, d03 |
| A5 | Judging is blind to stance and length-normalised; code selects. | G5 | [E] stance and length; [S] authorship | K13; c05, b18, d14, d15 |
| A6 | Never score the agent's disposition from its own stated reasoning or self-ratings. Score from behaviour under probes. | G10 | [E] | K03, K15, K04; b06, c14, a14 |
| A7 | Do not add "be open-minded", "be careful" or "check for bias" lines as a disposition layer. | 4b | [E] | K23, K09; c21, d03 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code-fired doubt vs a prompt disposition at equal tokens. Also redo our 92% vs 75% with n and CI. | G1 | [S] [O] | K09; a26, d03, d12 |
| T2 | Signal-gated "Wait" vs always-on "Wait", on a non-reasoning and a reasoning model. | G1, S5 | [S] | K08, K28; a18, d13 |
| T3 | Two-sided behavioural disposition score (flip on right, fix on wrong with evidence) as the bench metric. | G2 | [S] | K29, K11; d09, d06, c06 |
| T4 | True vs false authoritative argument discrimination. | G2, S1 | [S] [C] | K12, K30; a16, d08 |
| T5 | Trigger miss rate on natural errors with no audit instruction. | G1, S0 | [S] | K18, K31; a18, d10 |
| T6 | Third-person framing for challenge turns. | S1 | [S] | d09 |
| T7 | CQoT-style checklist run only after a code signal, at equal tokens. | S5, S6 | [S] | K33; d11 |
| T8 | Blind vs unblind judging plus style-neutral rewrite. | G5 | [S] | K14, K32; d14, d15 |
| T9 | "Gather more information" operator when attempts disagree (AOT mechanism). | S3, operators | [S] | K20; d16 |
| T10 | Monitoring step vs none. | G2 | [C] | K19; b07 |
| T11 | Persistent lesson policy vs in-prompt reminder. | memory | [S] | K17; d09 |

## 8. Concrete tests on our bench

All arms use equal total tokens per item. Setup, retries and judge calls are counted (G7). Report n, accuracy and a 95% interval (Wilson or bootstrap). Run at least two model classes (non-reasoning and reasoning).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Single-answer puzzles with a runnable check (ARC-like, word puzzles, code) | plain; always-on "re-check, be open-minded" line; code-fired doubt on check failure or disagreement | accuracy; tokens; regressions (right to wrong) | code-fired >= plain > prompt-fired; prompt-fired lower by several points (Huang, Jittham about -6 pp) |
| B2 (T2) | Items with injected and natural errors | no cue; always "Wait"; "Wait" only on signal | fix rate; false-alarm rate; accuracy | signal-gated at least equals always-on at fewer tokens; always-on may lift injected-error cases only |
| B3 (T3) | Known-answer items plus a challenge turn | no challenge; "are you sure"; suggested wrong answer; real counter-evidence (a failing run) | flip rate on correct answers; fix rate on wrong answers with evidence | plain model flips 10 to 40% on suggestion (Sharma, Li); agent with A4 near 0 flips with equal fix rate |
| B4 (T4) | Pairs of true and false authoritative arguments, same form and length | model alone; agent with input hygiene | flip rate true vs false; discrimination d | model: small d (form beats truth); agent: larger d only where code can check |
| B5 (T5) | Natural errors from plain runs, no audit instruction | agent triggers only | trigger recall and precision | recall low (prior: 4.3 to 10.8% catch); compute break-even from 4.3 |
| B6 (T6) | Challenge turns | normal framing; third-person framing | Turn of Flip; flips on correct | up to +63.8% reported; expect smaller on our model |
| B7 (T7) | Math and reasoning with check | plain; checklist always; checklist on signal | accuracy at equal tokens | about +5% reported with extra compute; at equal tokens expect 0 to +2% |
| B8 (T8) | Two-candidate choices, open-mode ideas | judge with authorship visible; hidden; hidden plus style rewrite | self-preference rate; agreement with code check | hidden reduces but does not remove; rewrite adds |
| B9 (T9) | Estimation or fact items needing extra evidence | "gather" operator on disagreement; none | accuracy; search count | gain only if gather adds information (Haran) |
| B10 | Stated vs behaviour gap | AOT/CTDS-style items; a behavioural twin of each | stated score minus behaviour score | large gap (Zhou) |

## 9. What does not transfer, and why

- **Self-report scales.** CCTDI, AOT and CTDS measure what a person says. In people they inflate (same-method bias). In models the stated score is not tied to behaviour (K04). Do not use them as agent targets.
- **Training gains.** Abrami's g=.30 or .57 comes from courses with weeks of practice. We do not train. Prompt-level "teaching" has no equal-token evidence (K16, K33).
- **Quasi-experiment effects (d 3 to 3.5).** Test-matched, N=114.
- **Dispositions as slow habits.** Human dispositions develop over years. The agent is reset each problem; its "habit" is the scaffold.
- **Motivation and affect.** Inquisitiveness, care for persons and self-confidence have no function in a single-problem agent beyond a priority rule (G12).
- **Sensitivity as awareness.** Human sensitivity is trained noticing. In the agent it is code detectors; the model is not asked to notice.
- **Open-mindedness as a virtue.** In people it is a virtue. In a model without a filter it is sycophancy (K11, K12).
- **Student-learning evidence** (GenAI and CT, mind maps): about learners, not reasoners (K26).
- **Social pressure.** Human conformity comes from social cost. In models it comes from preference-tuned agreement, so the fixes differ (K13).

## 10. Open questions

1. How large are the original AOT and AET effects after ability control, and do they replicate? (Stanovich and West 1997, 2007 not opened.)
2. What are the CCTDI-CCTST correlations and factor structure? What does Halpern's transfer data show?
3. Does a code-fired signal beat a disposition prompt at equal tokens, including on reasoning models? Our 92% vs 75% has no n or CI.
4. What is the trigger miss rate on natural errors with no audit instruction?
5. Can an LLM disposition be measured by behaviour with a score validated against a human scale?
6. Do true and false authoritative arguments move models differently?
7. Does a persistent policy beat an in-prompt reminder?
8. Does hiding authorship and stance remove self-preference at equal tokens?
9. Does prompt-level "teaching" of an LLM (a checklist) help on held-out items at equal tokens?
10. Do human-trained instruction gains have any analogue for agents?
11. Is the sycophancy gap smaller on frontier reasoning models on hard single-answer tasks, not multiple choice?

## 11. Sources

[V] opened and read this run; [M] snippet, abstract page or recalled only. Several items the jsonl marks opened were read as abstracts or summaries (critique.md: b08, b09, b10, b20, b21 abstract-level; a24, c19, c20 without exact figures).

**Human research**
- [V] Facione (1990) Delphi Report: https://www.qcc.cuny.edu/socialSciences/ppecorino/CT-Expert-Report.pdf (a01-a04)
- [V] Hitchcock, SEP Critical Thinking: https://plato.stanford.edu/entries/critical-thinking/ (a06, a08)
- [V] Abrami et al. (2015) summary: https://www.clearinghouse.edu.tum.de/wp-content/uploads/2023/12/CHU_KR18_ENG_Abrami_2015.pdf (a07)
- [V] Dispositions, working memory and CT (2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11204695/ (b01, b02)
- [V] Orhan and Ceviker Ay (2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC9244423/ (b03, b04)
- [V] Pre-service teachers (2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12360536/ (b05)
- [V] Akcay et al. (2026): https://pmc.ncbi.nlm.nih.gov/articles/PMC13536696/ (b06)
- [V] Alpindo et al. (2024): http://files.eric.ed.gov/fulltext/EJ1457553.pdf (b07)
- [V, abstract] Schoute and Alexander (2026): https://eric.ed.gov/?id=EJ1512000 (b08)
- [V, abstract] De Jesus (2024): https://eric.ed.gov/?id=ED657693 (b09)
- [V, abstract] GenAI meta-analysis (2026): https://eric.ed.gov/?id=EJ1510300 (b10)
- [V] Pennycook et al. (2015): https://jbaron.org/journal/15/15923a/jdm15923a.html (b19)
- [V] Haran, Ritov, Mellers (2013): https://doi.org/10.1017/s1930297500005921 (d16)
- [V] Friedman et al. (2026): https://arxiv.org/abs/2603.06878 (c12)
- [M] Ennis (1987): https://plato.stanford.edu/entries/critical-thinking/ (a05)
- [M] Stanovich and West (1997): https://doi.org/10.1037/0022-0663.89.2.342 (a09, b25, d17)
- [M] Facione et al. CCTDI: https://doi.org/10.22329/il.v20i1.2254 (a10, b26)
- [M] Perkins, Jay, Tishman (1993): https://www.jstor.org/stable/23087298 (a11, b27)
- [M] Halpern (1998): https://doi.org/10.1037/0003-066X.53.4.449 (a12)
- [M] Sosu (2013): https://doi.org/10.1016/j.tsc.2012.09.002 (a13)
- [M] Abrami (2015, 2008), recalled: https://doi.org/10.3102/0034654314551063 ; https://doi.org/10.3102/0034654308326084 (b23, b24)
- [M] Ennis (1996): https://doi.org/10.22329/il.v18i2.2378 (b28)
- [M] Pennycook and Rand (2019): https://doi.org/10.1016/j.cognition.2018.06.011 (b29)
- [M] Mellers et al. (2015): https://doi.org/10.1177/1745691615577794 (b30)
- [M] Alfano et al. (2017): https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182950 (c22)
- [M] Guo et al. (2024): https://arxiv.org/abs/2410.15182 (c23)
- [M] Intellectual humility dialogue (2026): https://arxiv.org/abs/2603.23855 (c24)

**LLM and AI research**
- [V] Zhou et al. (2025) Rationality Check: https://arxiv.org/pdf/2509.14546 (a14, a15, b11, b12)
- [V] Triedman and Shmatikov (2025) MillStone: https://arxiv.org/pdf/2509.11967 ; summary https://tech.cornell.edu/wp-content/uploads/2025/09/Measuring-language-model-open-mindedness-with-the-Millstone-benchmark.pdf (a16, a17, b13, b14, c07)
- [V] Self-Correction Bench: https://arxiv.org/html/2507.02778 (a18)
- [V] Huang et al. (2024): https://arxiv.org/pdf/2310.01798 (a19, b15, b16, c01)
- [V] Tyen et al. (2024): https://arxiv.org/pdf/2311.08516 (a20, c02)
- [V] Kamoi et al. (2024): https://arxiv.org/pdf/2406.01297 (a21, c03)
- [V] CriticBench: https://arxiv.org/pdf/2402.14809 (a22, c16)
- [V] Sharma et al. (2024): https://arxiv.org/pdf/2310.13548 (a23, b17, b18, c04)
- [V, abstract] Self-Refine: https://arxiv.org/pdf/2303.17651 (a24, c25)
- [V] CRITIC: https://arxiv.org/pdf/2305.11738 (a25, c17, d12)
- [V] Wei et al. (2024): https://arxiv.org/abs/2308.03958 (c05)
- [V] SycEval: https://arxiv.org/abs/2502.08177 (c06)
- [V] Latif et al. (2024) o1-preview: https://arxiv.org/abs/2410.21287 (c08, c09)
- [V, abstract] Peczuh et al. (2025): https://arxiv.org/abs/2510.12915 (b20, c10, c11)
- [V, abstract] Zaphir et al. (2024) MAGE: https://arxiv.org/abs/2406.14769v1 (b21)
- [V] Wazan (2026): https://arxiv.org/html/2602.00026v1 (b22)
- [V] Hagendorff et al. (2023): https://arxiv.org/abs/2212.05206 (c13)
- [V] Turpin et al. (2023): https://arxiv.org/abs/2305.04388 (c14)
- [V] Panickssery et al. (2024): https://arxiv.org/abs/2404.13076 (c15, d14)
- [V] Reflexion: https://arxiv.org/abs/2303.11366 (c18)
- [V, partial] Kadavath et al. (2022): https://arxiv.org/abs/2207.05221 (c19)
- [V, partial] Perez et al. (2023): https://arxiv.org/abs/2212.09251 (c20)
- [V] Echterhoff et al. (2024): https://arxiv.org/abs/2403.00811 (c21)
- [V] Li, Krishnan, Padman (2026): https://arxiv.org/abs/2602.13093 (d01, d02)
- [V] Jittham (2026): https://arxiv.org/abs/2608.21377 (d03)
- [V] Barkett et al. (2025): https://arxiv.org/abs/2506.21561 (d04)
- [V] Chua and Evans (2025): https://arxiv.org/abs/2501.08156 (d05)
- [V] Laban et al. FlipFlop: https://arxiv.org/abs/2311.08596 (d06)
- [V] Wang et al. (2023): https://arxiv.org/abs/2305.13160 (d07)
- [V] Xu et al. (2024): https://arxiv.org/abs/2312.09085 (d08)
- [V] SYCON-Bench: https://arxiv.org/abs/2505.23840 (d09)
- [V] ProcessBench: https://arxiv.org/abs/2412.06559 (d10)
- [V] CQoT: https://arxiv.org/abs/2412.15177 (d11)
- [V] s1: https://arxiv.org/abs/2501.19393 (d13)
- [V] Wataoka et al. (2025): https://arxiv.org/abs/2410.21819 (d15)

**Internal**
- [V] SCHEMA.md G1 and own measurement: C:/Users/User/Desktop/AGI/research_notes/single_agent/SCHEMA.md (a26, a27)

**Links to parallel subfields (not covered here):** Calibration and overconfidence; Cognitive conflict and impasse; Dual-process theory; Debiasing and cognitive forcing; Belief updating; Social epistemology; Conformity; Argument evaluation criteria; Assessment and tests; Training; Metacognition and higher-order representation.
