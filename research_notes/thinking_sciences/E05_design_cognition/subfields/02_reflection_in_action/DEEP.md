# Reflection-in-action: deep document

*Subfield E05.02. Key work: Schon 1983. Schema parts: S5 revise, O8 reframe the goal. Sources: evidence_a to d.jsonl, claims.jsonl (K01 to K26), critique.md in this folder. Evidence ids (a01 ...) point to those files. Numbers were re-checked against source text in the critique pass; where the critique corrected an earlier line, the corrected figure is used here.*

## 1. What it is

Reflection-in-action is Donald Schon's name for thinking while acting. A practitioner makes a move, sees what the move did, and changes the next move, without stopping to write a plan. Schon set this against "technical rationality", the view that practice is applying known theory to a clear problem. He drew on cases of architects, planners, engineers, psychotherapists and managers (a01, a02).

Core terms:

- **Reflection-in-action.** Thinking during the act.
- **Reflection-on-action.** Thinking back after the act.
- **Conversation with the situation.** The designer acts as if talking to the material. The material "talks back".
- **Back-talk.** What a move produced beyond what the designer meant. It includes unintended consequences and new features seen in the sketch.
- **Naming, framing, moving, reflecting.** The four activities Schon read in the Quist and Petra studio case (a03, from memory, not opened).
- **Seeing-moving-seeing.** Schon and Wiggins 1992: see something in a sketch, act on it, see again, often noticing something unintended (a04, not opened).

What the theory is, in evidence terms: a descriptive lens built from single narrated cases. It is not a tested model. No study found tests its predictions against an LLM (K16, a30, c28).

Why it matters for our agent: the S5 revise step and the O8 "reframe the goal" operator are machine versions of the loop. The loop is act, read what came back, change the next act. The research that matters most is therefore not the human design studies. It is the large 2023 to 2026 body of work on LLM self-correction, which tests this loop with numbers. The main finding of that work is a rule that Schon's account does not state: the back-talk must come from outside the model.

## 2. History and theories in depth

**Schon 1983, The Reflective Practitioner (a01, a02).** Only secondary summaries were opened (Wikipedia). The book reports narrated cases with no counts. The best known is Quist coaching Petra on a school on a sloping site (a03, not opened). Schon reads it as cycles of naming, framing, moving and reflecting on consequences, including unintended ones. One coach, one student, one interpreting researcher, no inter-rater check. Hard to falsify as stated.

**Schon and Wiggins 1992 (a04, d17).** "Kinds of seeing and their functions in designing." Only the Crossref record was opened (cited by 548 in Crossref, about 958 in Semantic Scholar). A sister 1992 record describes a workshop example from a first-year design project told as an illustration. No source found counts back-talk events in Schon's cases (d17, K25).

**Goldschmidt 1991, "The dialectics of sketching" (a05, not opened).** From memory: designers move between seeing a sketch "as" something and seeing that it has some property. This figural and non-figural back-and-forth is said to drive new ideas. Protocol study of architects, about 1112 citations.

**Suwa and Tversky 1997 (a06).** Abstract only. Architects and students gave retrospective reports of what they read off their own sketches. Retrospective reports can be rebuilt after the fact.

**Dorst and Dijkhuis 1995 (a09, not opened).** The same protocols were described under a rational problem-solving paradigm and under Schon's reflective-practice paradigm. Each captures different features. This is the clearest sign that the theory is a lens, not a model.

**Valkenburg and Dorst 1998 (a07, not opened).** Student design teams coded with Schon's four activities. Teams differ in how they frame. No link shown between reflection and design quality.

**Suwa, Purcell and Gero 1998 (a08, not opened).** A coding scheme with four action types: physical, perceptual, functional, conceptual. It was applied to one architect's protocol. It is a usable logging idea for an agent.

**Suwa, Gero and Purcell 2000 (b21, d18; search summary only).** One practising architect. About half the process showed two-way links between "unexpected discoveries" and the invention of new requirements. About 608 perceptual actions and 173 discoveries (28.5%) per a summary. The 2001 paper reports 606 and 171 (28%), so counts differ by version.

**Suwa, Tversky, Gero and Purcell 2001, "Seeing into sketches: regrouping parts encourages new interpretations" (b19, b20).** Opened in full. The best numbers in the human line. See section 3.

**Later human work.** Mangano and colleagues 2015 (b22): eight pairs of professional software designers at a whiteboard. Mejia and colleagues 2018 (b23): two student protocols, too small to say anything about creativity. Bilda, Gero and Purcell 2006 (d18): same group as Suwa; full text not reached.

**Critiques.**
- Kokotovich 2015, IASDR, pp. 1115-1128, "A case for reimagining reflection-in-action and co-evolution" (b24). The abstract was read. It says the designer draws on prior pattern and knowledge "in a spontaneous tacit way", that this "has some limitations", and that designers "may limit the field of issues". The offered fix is to map the problem space before solution work. It is conceptual, with no data. An earlier note (a31, c26) said the paper could not be found; b24 found it and the critique confirmed it.
- Eklund, Dixon and Wegener 2023 (a10): Dewey's habit explains how a designer acts well before reflecting. Abstract only; full text returned 403.
- Teacher-education critiques (a11; Shapiro 2010, Ryan, Russell 2013): students are asked to reflect without being taught how; Dewey gave richer notions. Secondary source.
- Timing critique (a12, Eraut, from memory): real-time practice leaves too little time for reflection, so it may be fast tacit action plus short checks.

**Computational descendants.** The functional pieces of the loop were later built and measured in LLM work: Self-Refine (a23), Reflexion (a13), CRITIC (a24), Self-Debug (c17), SCoRe (a27). They are covered in section 6. None of them tests Schon as a hypothesis; Reflexion-type work is the closest functional match.

**New in 2025 to 2026: design with LLMs.** Designers using ChatGPT described "reciprocal reflection-in-action" (c21, 18 designers). The authors note that Schon's account assumes materials that respond predictably and transparently; an LLM interprets and can mislead (c25). Other recent papers are tools or concept papers: DesignMentor (c22, n=25), ChatGraPhT (c23, no sample), "Material for Thought" (c24, no data).

## 3. Core findings with exact numbers

Status key: established, single-source, contested, human-only, older models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Self-revision without outside signal lowers accuracy on reasoning | GPT-3.5 CSQA 75.8 to 38.1 (round 2) to 41.8; GSM8K 75.9 to 75.1 to 74.7; HotpotQA 26.0 to 25.0 to 25.0. GPT-4 GSM8K 95.5 to 91.5 to 89.0; CSQA 82.0 to 79.5 to 80.0; HotpotQA 49.0 to 49.0 to 43.0. GPT-4-Turbo GSM8K 91.5 to 88.0 to 90.0. Llama-2 GSM8K 62.0 to 43.5 to 36.5 | Huang 2024 (a17, b02, b04, c06) | established, older models only |
| Earlier gains came from oracle labels | Oracle: GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 GSM8K 95.5 to 97.5, CSQA 82.0 to 85.5, HotpotQA 49.0 to 59.0 (b01 mislabels these; use a18, c05) | Huang 2024 (a18, c05) | established |
| Model overturns right answers | GPT-3.5 keeps GSM8K answer 74.7% over two rounds. Llama-3.1-8B: -20.4 points, 58.8% of correct answers overturned. GPT-3.5-turbo changed answer more than 6 times in 10 rounds for 81.3% of questions | Huang (a19); Zhang 2025 (b17, d12) | established |
| Failure patterns in blind revision | Perfectionism 49.0%, cognitive overload 33.3%, overthinking 17.6%. Internal answer changed 14.1% vs 8.3% at first generation. o1-mini: 15.4 "think" steps in failed cases vs 5.3 normal. Accuracy fell on all four tasks including o1 family and R1 | Zhang 2025 (b18, d12) | taxonomy single-source (model-assisted labels); the drop is established |
| Fair prompts shrink the harm | Four models, six datasets; fair prompts improve averages (p<0.05, p<0.003). CSQA before correction: GPT-3.5 75.92, GPT-4 84.11. Per-dataset gains not recorded | Liu 2024 (a28) | contested |
| Multi-agent debate vs vote at matched responses | GSM8K GPT-3.5: single 76.7; debate 6 responses 83.2 vs vote 85.3; 9 responses 83.0 vs vote 88.2 | Huang (a20, c08) | established with G9; layout partly garbled |
| Reflexion with an external signal | ALFWorld (134 tasks): 130 of 134 solved in 12 trials, +22% absolute. HotPotQA +20%. HumanEval Python 91.0 vs GPT-4 80.1. ReAct-only plateaued at about 22% hallucination | Shinn 2023 (a13, a16, b07) | established, GPT-4 era; ALFWorld also uses a hand-made detector |
| Reflexion fails where the tests lie | MBPP Python: Reflexion 77.1 vs GPT-4 80.1. Test false-positive rate 16.3% (MBPP) vs 1.4% (HumanEval). Leetcode Hard Python: 15.0 vs 7.5 (Reflexion wins; b08 is wrong). Rust-50: 0.68 vs 0.60 | Shinn (a14, c11) | single-source |
| Written lesson, inside Reflexion | HumanEval Rust-50: base 0.60, no test generation 0.52, no reflection 0.60, full 0.68 (+8 = 4 problems). HotPotQA, 100 questions: reflection +8 over episodic memory only | Shinn (a15, d08, d09) | contested; tiny N |
| Bare failure flag vs richer feedback in code | MBPP GPT-4: base 72.8, flag only 78.8, with unit tests 80.6, tests+explanation 80.4, tests+trace 80.2. GPT-3.5: 67.6, 70.8, 72.2, 74.2, 72.8 (approximate; table scrambled). TransCoder GPT-4: 77.3, 80.9, 88.8, 90.4, 89.5. Spider GPT-4: 73.2, 73.4, 73.6 | Chen 2024 Self-Debug (d06, c17) | contested (K22) |
| Self-debug without execution is weak | MBPP: Codex 61.4 to 57.6 (flag only, down), 66.2 with trace; GPT-3.5 67.6 to 69.2; GPT-4 72.8 to 76.0 to 76.4. TransCoder GPT-3.5 89.1 unchanged | Chen (d07) | single-source |
| Retry plus explanation, on items known wrong | Nine LLMs, 1000 questions. GPT-4: baseline 0.786, Retry 0.827, Explanation 0.876, Solution 0.925, Composite 0.932, leaked answer 0.971 (all p<0.001, McNemar). Claude 3 Opus 0.792, 0.849 (Retry), 0.947 (Composite). Gemini 1.0 Pro 0.617, 0.724, 0.774. Command R+ 0.641, 0.745, 0.874. Gemini 1.5 Pro 0.751, 0.813, 0.815 | Renze 2024 (b15, b16) | single-source; knowing the item failed is an oracle |
| Finding the error is the bottleneck | BIG-Bench Mistake, 2186 PaLM 2 traces, five tasks. Best model (GPT-4) finds first error in 52.87%. Backtracking with true location: +18.04 to +43.92 points on wrong traces; random location +5.16 to +21.57. Cost on right traces: 0.00 to -11.43 (true), -6.67 to -15.91 (random). 15% of traces correct, 85% wrong | Tyen 2024 (a21, a22, b10, c16) | single-source; task-to-row labels unreliable |
| Self-Refine, stylistic and checkable tasks | About +20 points average over 7 tasks. GPT-4 code optimization 27.3 to 36.0; dialogue preference 25.4% to 74.6%; constrained generation 28.0 to 37.0 (GPT-3.5 column) and 29.0 to 49.7 over 3 iterations (GPT-4); do not compare the two. Math 64.1 to 64.1 | Madaan 2023 (a23, b05, c01, c04) | single-source; GPT-4 as judge on several tasks (82%, 68%, 71% human agreement) |
| Self-Refine: critic cannot see math errors | Feedback said "looks good" for 94% of ChatGPT instances; gain over 5 points with external error signal. Appendix variant 24.18 to 40.5 | Madaan (b06, c02) | single-source |
| Specific feedback beats generic beats none | Sentiment 43.2 / 31.2 / 0. Acronym 56.4 / 54.0 / 48.0. Code optimization 27.5 / 26.0 / 24.8 | Madaan (c03) | single-source |
| Tool critique beats no-tool critique | Free-form QA: CRITIC 50.0 vs without tool 42.0 vs CoT 44.2 (layout garbled). GSM8K PoT 70.1 to 72.2 vs 68.3 without tool. TabMWP 64.6 to 87.6 vs 84.9 without. SVAMP fell 84.0 to 80.7 both ways. Overall +7.7 F1 QA, +7.0% math | Gou 2024 (a24, b13, c13, c14) | established with K03 |
| Self-critique on graph colouring | No backprompt 16% (100 instances). Same-model verifier feedback: 1 of 100. 15 plain samples at t=1.0 about 40%, equal to all four backprompt types | Stechly 2023 (b14, b25) | single-source (one task) |
| Repair vs resampling at matched budget | HumanEval and APPS (300 tasks). GPT-4 on APPS up to +8% over baseline; GPT-3.5 competition up to +34% relative; GPT-3.5 and Code Llama on APPS mostly match or lag. Cells: 1.05x and 0.97x of pass@k baseline | Olausson 2024 (d01) | established as "modest and uneven"; older models |
| Feedback source matters | Repair success with GPT-4 feedback 33.30% (intro 42.64, interview 19.33, competition 3.67) vs human 52.60% (62.21, 45.67, 14.67); factor 1.58x; 16 participants | Olausson (d02) | single-source |
| Sequential revision vs parallel, trained | PaLM 2-S* revision-tuned, MATH: sequential narrowly beats parallel at matched budget; compute-optimal mix beats best-of-N with up to 4x less compute. About 38% of correct answers flipped to wrong by naive revision | Snell 2024 (d03, d04) | established for the 38%; trained model only |
| Training makes self-correction real | MATH Gemini 1.5 Flash: base 52.6 to 41.4 (-11.2); Self-Refine -1.0; STaR +0.4; Pair-SFT +1.8; SCoRe 60.0 to 64.4 (+4.4; +15.6 over base). HumanEval: SCoRe 52.4 to 64.6 (+12.2) vs base +3.0, Self-Refine -1.2 | Kumar 2024 (a27, b12, c18) | established; needs RL |
| Blind spot: own errors vs others' | 14 open non-reasoning models: 64.5% blind spot. "Wait" cut it 89.3% and raised mean accuracy 156%. 5,306 correction traces cut it 76.0%. Claude 3.5 Haiku 52.5%, Sonnet 4 41.4%. DeepSeek-V3 0.567 to 0.902 with "Wait" (R1: 0.908) | Tsui 2026 (c19, c20, d10) | single-source; open models, via prefill |
| "Wait" marker in budget forcing | s1-32B AIME24 after two forced continuations: Wait 53.3, Hmm 50.0, Alternatively 50.0, none 50.0 (30 questions, one question = 3.3 points). MATH500 93.0 for Hmm and Wait, 90.2 none | Muennighoff 2025 (d11) | single-source |
| Human: regrouping and unintended features | One architect, 340 segments: new grouping 136 (40%), previous grouping 182 (54%), no revisiting 22 (6%). 606 perceptual actions, 171 (28%) unintended-feature detections | Suwa 2001 (b19) | human-only, single expert |
| Human: attending to parts doubles interpretations | 36 novices, three self-selected groups. No Parts (n=13) mean 27.2 (SD 12.2); Different Parts (n=12) 44.6 (SD 12.0); Regroup Parts (n=11) 49.6 (SD 30.4). Different vs No F(1,23)=12.9, p<.01; Regroup vs No F(1,22)=5.96, p<.05; Different vs Regroup F(1,21)=0.27. Decay of rate F=11.5 and 24.3, p<.01 | Suwa 2001 (b20) | human-only; groups self-selected |
| Human: sketches carry reasoning | 8 pairs, 14 hours, over 4000 coded events. Over 80% of reasoning activities used sketches; no sketch held beyond about 30 seconds; coder agreement 80.0%, 82.4%, 78.6% | Mangano 2015 (b22) | human-only; observational |
| Human: discoveries and creativity unclear | Two protocols of 81 segments; unexpected discoveries 2 vs 3; segmentation similarity 62% and 71%; N=2, no statistics | Mejia 2018 (b23) | human-only; underpowered |
| LLM as design material | 18 designers; 16 of 18 struggled to make abstract values concrete. DesignMentor: 25 participants, 16 items on 5-point scale | Sinlapanuntakul 2026 (c21); Ahn 2026 (c22) | single-source; qualitative or self-report |

## 4. Mechanisms and models

An engineer can implement these mechanisms from the evidence. Each is a small program, not a prompt idea.

**4.1 The conversation loop (Schon, made computable).**
State: current attempt, intent, history of attempts, check results.
1. Model writes an attempt (move).
2. Code runs the check and returns real output (back-talk).
3. Code compares the output with the stated intent. The difference is the back-talk: what the move did that was not meant.
4. Model gets the attempt plus the located output and writes one line naming what is wrong, then a new attempt.
5. Code stops on pass, on round limit, or on repeated error.
The model never decides whether to continue. This is the SCHEMA S4, S5, S6 path.

**4.2 Detect, locate, fix (Tyen).** Split revision into three jobs. Detect that something failed. Locate the failing step. Fix. Models fix well given a location and locate poorly (52.87%). So code should detect and locate whenever it can (failing test, stack trace, constraint violation, mismatch with a held-out example). Where only a model can locate, use a reasoning-model locator (ProcessBench, d13) and expect weak results.

**4.3 Retry gating by a flag (Renze, Self-Debug).** The cheapest signal is "that answer failed". In code the bare flag gave most of the lift (72.8 to 78.8 against 80.6 with tests). The flag must come from code. Telling a model "you were wrong" when the check has not failed is the oracle leak that inflated earlier papers.

**4.4 Keep the first answer in the pool (Snell).** A revision pass flips correct answers to wrong (38% in a trained revision model; GPT-3.5 changed 25.3% of GSM8K answers over two rounds, with more right-to-wrong than wrong-to-right). Implementation: store original and each revision as candidates. Code picks by held-out check or vote. The last revision is not trusted by default.

**4.5 Source framing and continuation markers (Tsui, s1).** Models correct an error attributed to someone else but miss it when it is their own (64.5% blind spot on 14 open models). A neutral continuation word ("Wait") after the output restores correction on non-reasoning models. Two implementation options: (a) prefill the assistant turn where the API allows it; (b) frame the revise prompt as reviewing a colleague's output, which has not been tested through instruction text alone. Reasoning models show a small or negative blind spot, so this helps non-reasoning models mostly.

**4.6 Problem-space map before revision (Kokotovich).** Untested. Form: before a revise round, code asks the model to list the constraints and the frames it considered, then checks whether the revision uses a different frame. Needs a frame-anchoring metric (see UNKNOWNS).

**4.7 Logging scheme (Suwa).** Tag each step as physical, perceptual, functional or conceptual. A "perceptual discovery" in an LLM trace is: output contained a feature not in the intent. Log it as an observation field. It is descriptive only; the 28% human rate is one architect and not a target.

## 5. What holds up

**Replicated or consistent across independent groups.**
- External signal is the active ingredient. Huang (oracle vs none), Reflexion (tests, environment), CRITIC (tool vs no tool), Self-Debug (execution vs none), Tyen (true location), Stechly (sound verifier), Kamoi (survey), Olausson (stronger or human feedback). At least six separate groups (K03).
- Blind self-revision does not help and can hurt on reasoning tasks, for GPT-3.5, GPT-4, Llama and (in 2025) o1-family and R1 blind passes (K01, K23). The harm is from flipping correct answers (K09, K21).
- Plain resampling and voting match or beat self-critique and debate at matched calls (Stechly, Huang, Olausson). Two to three independent groups (K06, K20).
- Self-feedback is biased: models favour their own text (Panickssery, d15) and fail to see their own math errors (Self-Refine 94% "looks good").

**Failed or weak.**
- Reflexion on MBPP (77.1 vs 80.1), because self-written tests passed wrong code (16.3% false positives).
- Self-critique on graph colouring (1 of 100 vs 16% baseline).
- Prompted self-correction on MATH (Gemini base -11.2; Self-Refine -1.0).
- Self-Refine on math (64.1 to 64.1).
- The human 28% rate has no multi-designer replication (d18; the absence is weak because search was limited).
- Mejia 2018 found 2 vs 3 unexpected discoveries and no clear link to creativity.

**Contested.**
- Whether intrinsic correction always hurts. Liu 2024 shows small gains with fair prompts at temperature 0. Wording matters (K10). Huang notes some earlier gains came from better initial prompts or more calls.
- Whether the written lesson adds anything beyond the failure flag. Reflexion: +8 on Rust-50 and HotPotQA (4 problems and 8 of 100). Self-Debug: about +2 over flag. Renze: 0.827 vs 0.876. Net: flag larger, lesson a few points (K22).
- Whether feedback from a different model or role beats same-model feedback on open tasks. Only code evidence (33.3% vs 52.6%).

**Moderators.**
- Task type: checkable or decomposable tasks gain; single-answer reasoning does not (Kamoi).
- Model strength: weaker models lose more under blind revision (Llama-2 -25.5 on GSM8K by round 2; GPT-4-Turbo near flat).
- Starting accuracy: Tyen's 85% wrong traces make backtracking look big; on easy mixes the net shrinks.
- Item difficulty: repair helps most for the strongest model on the hardest items (Olausson); easy items do best sequentially, hard items need a mix (Snell).
- Feedback specificity: specific beats generic beats none (Self-Refine).
- Reasoning-model status: blind spot small or negative (Tsui v3).

**Interventions that worked.** Tool or test output as feedback. Located error. Stronger or human critic. "Wait" on non-reasoning models. Keep-best-and-select over a revision chain. RL training for self-correction (SCoRe).

**Interventions that did not.** Same-model critique on reasoning. Debate. Self-written tests as sole check. Rewording the critique prompt to "find problems" (primes invented problems). Offline SFT variants (collapse to minimal edits).

**Human side.** One expert (Suwa 2001, one coder for the main analysis), one novice experiment with self-selected groups (7 told to regroup could not), one observational whiteboard study. Causal evidence that back-talk improves design outcomes is absent.

## 6. Language models

**Direct tests of Schon.** None found (a30, c28, K16). The search was limited by rate limits and an exhausted web budget, so the absence is weak.

**Blind self-revision.** On 2023-era models, accuracy fell or stayed flat on reasoning tasks (section 3). Size of the fall: GPT-3.5 CSQA -37.7 points by round 2; GPT-4 GSM8K -6.5 by round 2; Llama-2 GSM8K -25.5; Llama-3.1-8B -20.4. In 2025, Zhang found drops on four tasks including o1-family and R1 in a blind pass (d12). Tsui v3 (Aug 2026) finds a small or negative blind spot for reasoning models, which means they can fix a shown error; the harm from blind revision is about unneeded revision (K01). Nobody was found who reran Huang's setup on GPT-5-class or Claude thinking models with thinking budgets varied (gap 2, K23).

**Revision with a signal.** Reflexion ALFWorld 130 of 134. HumanEval 80.1 to 91.0. Self-Debug MBPP 72.8 to 80.6. Tyen +18 to +44 on wrong traces with true location. CRITIC TabMWP 64.6 to 87.6 with tools. All on 2023 to early 2024 models.

**Revision vs more samples.** Olausson: modest, uneven, 0.97x to 1.05x in cells quoted, up to +8% (GPT-4, APPS) and +34% (GPT-3.5, competition). Snell: trained sequential revision narrowly beats parallel on MATH. No test of a prompt-only revision step plus a code selector on a frontier model exists (gap 1, partly closed).

**Locating errors.** Best model 52.87% on BIG-Bench Mistake. ProcessBench (3,400 cases) says even strong critics struggle; o1-mini beats QwQ-32B-Preview, which matches GPT-4o (abstract only).

**What changed the behaviour, by how much.**
- External signal: from flat or negative to +8 to +44 points depending on task.
- True error location vs random: +18 to +44 vs +5 to +22.
- Stronger or human feedback in code: 33.3% to 52.6% repaired.
- "Wait" on non-reasoning open models: blind spot cut 89.3%; DeepSeek-V3 0.567 to 0.902.
- RL training: MATH second-try delta -11.2 to +4.4.
- Reflexion lesson text: +8 in two small tests.
- Retry flag alone (Renze GPT-4): +0.041; full explanation +0.090; leaked answer +0.185.

**Design-with-LLM studies (2025 to 2026).** Qualitative, no effect sizes (c21 n=18; c22 n=25; c23, c24 concept papers). A useful point from c21 and c25: when the material is an LLM, back-talk is itself interpreted and can mislead. For our agent this reinforces that back-talk must come from code.

**Caveats.** Most numbers use GPT-3.5, GPT-4 (2023), Llama-2 and PaLM 2. Reflexion's ALFWorld win used a hand-made hallucination detector, so it is not reflection alone. Many results share benchmarks (GSM8K, CSQA) and prompts, so independent-source counts overstate independence.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Revise only from located real output** (G2, S5). [E] a17, a18, a21, a24, b14, c13, d02, d06 (K02, K03). Already in SCHEMA; keep. The model writes one line naming the failing output and fixes it.
2. **No self-critique round with no trigger** (G1, S5). [E] b02, b17, d12, a19 (K01, K09). Already in SCHEMA 4b; this research adds the 2025 o1/R1 blind-pass evidence and the Tsui note that the harm is from unneeded revision. Keep.
3. **Keep the first answer as a candidate in S7** (G1, G5, S5). [E] d04, a19, b17 (K21). Revision flips right answers. Log every flip; select by code check or vote, not by recency.
4. **Prefer program-located errors over model-located** (G2, S4, S5). [E] a21, d13, b14, d02 (K03; K04 is [S] for the exact numbers). A failing test, stack trace or constraint violation is the locator.
5. **Revision is not free compared with resampling; compare at equal tokens** (G4, G7). [E] d01, b25, a20 (K06, K20). Keep best-of-N with a code selector as the control arm for every S5 element.
6. **Held-out check before accepting** (G3). [E] a14, c11. Self-written tests passed wrong code 16.3% of the time on MBPP.
7. **Do not train for self-correction** (none). [E] a27. Prompting has a ceiling; SCoRe needs RL. No schema change.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code-triggered S5 pass vs best-of-N plus the same selector, equal tokens | G4/S5 | [E] that matched-budget gains are modest; frontier-model effect unknown | d01, d03, K20 |
| T2 | Bare failure flag vs flag plus program error text vs flag plus model-written lesson | S5/O8 and memory (lessons) | [C] | d06, d08, d09, b15, K22 |
| T3 | "Wait" or neutral continuation marker after a failed check | O8 wording | [S] | c20, d10, d11, K12, K19 |
| T4 | Revise prompt framed as reviewing a colleague's output | O8 wording | [S] | c19, d10, d15, K19 |
| T5 | Neutral vs "find problems" wording of the revise prompt | G1/S5 | [C] | a28, a17, K10 |
| T6 | Located error from a program vs model-located vs none | G2/O8 | [S] | a21, c16, K04, K05 |
| T7 | Problem-space map step before revise (Kokotovich fix) | S1/O8 | [C] | b24, K17, K24 |
| T8 | Frontier thinking models: does Huang's harm hold with thinking on? | G1 | [S] | d12, d10, K23 |
| T9 | Re-read external trace of attempts at revise time vs summary only | memory | [S] | b22, K15 |
| T10 | Open tasks: self-critique vs different-prompt critic vs rubric program | G2/S5 | [C] | d02, d15, d16, K26 |
| T11 | Force re-decomposition of the output into parts before revising | O8 | [S] | b20, K14 |
| T12 | Log "unexpected feature" field as an observation fed back | S5 | [S], single human case | b19, K13, K25 |

Each T maps to a row in UNKNOWNS.md.

## 8. Concrete tests on our bench

All tests keep both arms at equal total tokens and equal number of model calls. Log right-to-wrong and wrong-to-right flips for every revise step (SCHEMA section 6).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | ARC items with a checkable held-out example; word puzzles with a checker | (A) S5 revise after code check fails, keep original in pool; (B) best-of-N with same code selector | Final accuracy; flips right to wrong | Gain within plus or minus 3 points. Olausson suggests about 1.0x of resampling. Revise wins only on hardest items |
| B2 | Same items, items where first attempt failed the check | (A) flag only; (B) flag plus program error text; (C) flag plus written lesson | Pass rate on failed items | A gets most of the lift; B adds a few points; C adds up to 2 to 8 points (contested) |
| B3 | Same items | (A) neutral revise wording; (B) "find problems" wording; (C) no revise | Accuracy; flips | B below A by a few points; A close to C |
| B4 | Items with sound checker, revise after failure | (A) "Wait" marker after failed check; (B) none | Pass rate on failed items | Gain if the model is non-reasoning; near zero for thinking models |
| B5 | Same | (A) "review this colleague's attempt"; (B) "revise your attempt" | Fix rate on failed items; right-to-wrong flips on correct items | A higher fix rate on non-reasoning models; watch flips on correct items |
| B6 | Multi-step reasoning items, failing step known from checker | (A) code gives step location; (B) model locates; (C) no location | Fix rate on wrong traces; loss on right traces | A beats B by 10 to 25 points; loss on right traces up to 11 |
| B7 | Items where the first frame is wrong (built by design) | (A) problem-space map then revise; (B) revise only | Share of revisions that change frame; final accuracy | A raises frame change; accuracy gain unknown, may be zero |
| B8 | Any set, thinking mode on vs off | (A) blind "are you sure" pass; (B) none | Right-to-wrong flips | A flips some correct answers; size unknown on current models |
| B9 | Multi-round tasks | (A) full trace of attempts re-read; (B) one-line summaries only | Repeat-error rate; accuracy | A lowers repeat errors; keep only if it wins at equal tokens |
| B10 | NoveltyBench-type open items | (A) self-critique; (B) different-prompt critic; (C) rubric program | Blind-rated novelty and quality | Unknown; self-critique expected weakest |

## 9. What does not transfer, and why

- **Tacit experience and habit.** Schon's practitioners act from years of habit (Eklund 2023, Kokotovich 2015). A prompt cannot hold habit. Expect a weaker loop than a trained designer's.
- **Physical and visual material.** Sketches let a designer see unintended features and regroup parts. A text agent sees only text and execution output. Suwa's 28% rate is a rate of visual detections by one architect, not a target for tokens.
- **Real-time pressure.** Schon's "in action" implies live pace. An agent has a call budget, not a clock. Reflection must be bought with calls and gated by a trigger (G1).
- **Free "reflection".** A human reflecting on his own work has new information (the sketch). A model reflecting on its own text has none. This is why same-model critique fails (Huang, Stechly, Self-Refine math).
- **Single-designer protocols.** Quist and Petra, Suwa's architect, Mejia's two students. They give no effect sizes to reuse.
- **Style tasks.** Self-Refine's biggest gains (dialogue 25.4% to 74.6%) used GPT-4 as judge and tasks where checking is easy. They do not carry to single-answer reasoning.
- **Trained correction.** SCoRe and the 5,306-trace fine-tune need training. We do not train.
- **Prefill tricks.** The "Wait" effect uses assistant-turn prefill, which most closed APIs do not allow. Only an instruction-text version could be used, and it is untested.
- **Back-talk from an LLM material.** In design-with-LLM studies the back-talk is itself interpretive (c25). For our agent, back-talk must come from a program.

## 10. Open questions

1. At equal tokens, does a prompt-only S5 revise pass triggered by a code check beat best-of-N with a code selector on frontier models? (gap 1, partly closed)
2. Does Huang's result hold on GPT-5-class and Claude thinking models with budgets varied? (gap 2)
3. Does the written lesson add anything beyond the failure flag at equal calls? Three-arm test missing. (gap 3)
4. What does a program locator (test, trace, constraint) gain on wrong traces and cost on right ones? Tyen's numbers use a gold location. (gap 4)
5. Is Kokotovich's narrowing measurable as anchoring on a first frame, and does a problem-space map reduce it? (gap 5)
6. Does a neutral marker or other-author framing work through instruction text, without prefill, on frontier models? (gap 6)
7. What do Schon's original cases count? No tally found. (gap 7)
8. Has the unexpected-discovery rate been replicated with several designers, and does it predict outcome quality? (gap 8)
9. For open tasks with no checker, which feedback source works? (gap 9)
10. Does reading back an external trace beat summaries for revise quality? Software-design evidence is observational (Mangano 2015).

## 11. Sources

[V] = opened and read (full text or page) in this research. [M] = snippet, abstract only, search summary, record, or from memory.

- [M] Schon (1983) The Reflective Practitioner; secondary summaries, https://en.wikipedia.org/wiki/Reflective_practice and https://en.wikipedia.org/wiki/Donald_Sch%C3%B6n (a01, a02, a03; the book itself not opened)
- [M] Schon and Wiggins (1992) Kinds of seeing, https://doi.org/10.1016/0142-694X(92)90268-F (a04, d17; Crossref record only)
- [M] Goldschmidt (1991) The dialectics of sketching, https://doi.org/10.1080/10400419109534381 (a05)
- [M] Suwa and Tversky (1997) What do architects and students perceive, https://doi.org/10.1016/s0142-694x(97)00008-2 (a06; abstract)
- [M] Valkenburg and Dorst (1998), https://doi.org/10.1016/S0142-694X(98)00011-8 (a07)
- [M] Suwa, Purcell and Gero (1998), https://doi.org/10.1016/S0142-694X(98)00016-7 (a08)
- [M] Dorst and Dijkhuis (1995), https://doi.org/10.1016/0142-694X(95)00003-6 (a09)
- [M] Suwa, Gero and Purcell (2000) Unexpected discoveries, https://dx.doi.org/10.1016/S0142-694X(99)00034-4 (b21, d18; summary and Crossref)
- [M] Bilda, Gero and Purcell (2006) To sketch or not to sketch (d18; record only)
- [V] Suwa, Tversky, Gero and Purcell (2001) Seeing into sketches, https://www.tc.columbia.edu/faculty/bt2158/faculty-profile/files/es_Regroupingpartsencouragesnewinterpretations.pdf
- [V] Mangano, LaToza, Petre and van der Hoek (2015) software designers at the whiteboard, https://people.cs.gmu.edu/~tlatoza/papers/tse15-sketching.pdf
- [V] Mejia, Arango and Chan (2018) Unexpected discoveries, https://creativity.designsociety.org/download-publication/40769/UNEXPECTED+DISCOVERIES+AND+THEIR+ENHANCEMENT+OF+THE+DESIGN+PROCESS
- [M] Kokotovich (2015) A case for reimagining reflection-in-action, https://opus.lib.uts.edu.au/handle/10453/41435 (abstract record only)
- [M] Eklund, Dixon and Wegener (2023) Pre-Reflection-in-Action, https://pure.ulster.ac.uk/en/publications/d1d31393-0902-426b-9483-04c6fae0bd1a (abstract; full text 403)
- [M] Critiques of Schon (Shapiro 2010; Ryan; Russell 2013), https://en.wikipedia.org/wiki/Reflective_practice (a11)
- [M] Eraut and others, timing critique, from memory (a12)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet, https://arxiv.org/abs/2310.01798
- [M] Liu et al. (2024) Intrinsic self-correction is not a mirage, https://arxiv.org/abs/2406.15673 (partial; a28)
- [V] Shinn et al. (2023) Reflexion, https://arxiv.org/abs/2303.11366
- [V] Madaan et al. (2023) Self-Refine, https://arxiv.org/abs/2303.17651
- [V] Gou et al. (2024) CRITIC, https://arxiv.org/abs/2305.11738
- [V] Chen et al. (2024) Self-Debug, https://arxiv.org/abs/2304.05128
- [V] Tyen et al. (2024) BIG-Bench Mistake, https://arxiv.org/abs/2311.08516
- [V] Stechly, Valmeekam and Kambhampati (2023) GPT-4 doesn't know it's wrong, https://arxiv.org/abs/2310.12397
- [V] Renze and Guven (2024) Self-reflection in LLM agents, https://arxiv.org/abs/2405.06682
- [V] Zhang et al. (2025) Dark side of intrinsic self-correction, https://arxiv.org/abs/2412.14959
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes, https://arxiv.org/abs/2406.01297
- [V] Kumar et al. (2024) SCoRe, https://arxiv.org/abs/2409.12917
- [V] Tsui (2026) Self-Correction Bench, https://arxiv.org/abs/2507.02778 (read to character 100000 of 134709)
- [V] Olausson et al. (2024) Is self-repair a silver bullet, https://arxiv.org/abs/2306.09896
- [V] Snell et al. (2024) Scaling test-time compute, https://arxiv.org/abs/2408.03314
- [V] Muennighoff et al. (2025) s1, https://arxiv.org/abs/2501.19393
- [M] Zheng et al. (2025) ProcessBench, https://arxiv.org/abs/2412.06559 (abstract only)
- [M] Gandhi et al. (2025) Cognitive behaviors that enable self-improving reasoners, https://arxiv.org/abs/2503.01307 (abstract only)
- [M] Panickssery, Bowman and Feng (2024) LLM evaluators favor their own generations, https://arxiv.org/abs/2404.13076 (abstract only)
- [V] Sinlapanuntakul et al. (2026) How designers envision value-oriented AI design concepts, https://arxiv.org/abs/2605.00280
- [V] Ahn et al. (2026) From answer givers to design mentors, https://arxiv.org/abs/2601.19053
- [V] Kimm and Tan (2025) ChatGraPhT, https://arxiv.org/abs/2512.22790
- [V] Material for Thought: generative AI as an active creative medium (2026), https://arxiv.org/abs/2605.19832

**Links to parallel subfields (not covered here):** Productive failure; Cognitive conflict and impasse; Search over thoughts; Tree of Thoughts; Language Agent Tree Search; Debiasing and cognitive forcing; Belief updating; Metacognition and higher-order representation; Calibration and overconfidence; Protocol analysis; Conceptual change and revolutions; Anomalies and paradigm change; Software, spreadsheet, KB debugging; Proof planning and repair.
