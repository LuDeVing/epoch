# Joint cognitive systems: deep document

*Subfield E13.01. Evidence ids (a01-d16) refer to evidence_a-d.jsonl; claim ids (K01-K30) to claims.jsonl; both in this folder. Status tags: [E] established (two or more independent sources, or one very strong one), [S] single-source, [C] contested. Read-state: the core Hollnagel and Woods books were NOT opened; see section 11.*

## 1. What it is

A joint cognitive system (JCS) is a way to describe people plus tools as one system. The unit of analysis is not the person and not the machine. It is the pair, judged by what it does together: keeping control of a process in the face of change. Hollnagel and Woods defined it by function, not by parts. A system is "cognitive" if it can control its own behaviour using experience. A person, a team, or a person with software can all qualify. [a06, a07, b26: books not opened; definition is second-hand]

Cognitive systems engineering (CSE) grew out of process control, aviation and nuclear plants. It asks how to design the pair so that the whole copes with complexity. Its main claims are:

1. Automation does not remove the human. It changes the human's job, usually toward harder, rarer, less practised tasks (Bainbridge, 1983). [a01, E]
2. Judge the system by joint performance, not by each part's accuracy. [a06, S]
3. Control depends on context: time, goals and information shape how the system acts (COCOM control modes). [d12, S]
4. A good machine is a team player: predictable, directable, able to share common ground. [a26, not opened]

Why it matters for our agent. Our schema already splits work between a program (code: orders steps, runs checks, selects) and a model (fills open slots). That split is a joint cognitive system. The JCS literature, and its 2020-2026 LLM descendants, tell us three things:

- When pairing a checker with a generator helps, and when it only adds cost.
- Which side should hold the final say, by item class.
- How the check side fails (it over-trusts, or it wrongly rejects), and what lowers that failure.

Scope. This document does not repeat the bias, debate and self-correction material already in the schema (G1-G12, section 4b). It adds the human-AI team literature as evidence about the checking half of the program/model split, and the multi-agent LLM literature as evidence about how much structure helps. Links to parallel subfields (not covered here): Distributed cognition, Distributed cognition theory, Consensus and premature agreement, Confidence and metacognition, Learned refinement and self-verification, Surprisingly popular method.

## 2. History and theories in depth

### 2.1 Origins (1980s)

- Bainbridge (1983), "Ironies of automation". A position paper with no sample. Opened. [a01-a04]
  - Irony 1: designers automate what they can. The operator keeps "an arbitrary collection of tasks" with little support. [a01]
  - Irony 2 (monitoring): if a decision can be fully specified, the computer does it faster and more accurately. So the human monitor "has been given an impossible task". She cites Mackworth (1950): effective attention to a low-event source fails after about half an hour. [a01, a02]
  - Irony 3 (skill): skills decay without use, yet take-over happens exactly when the process is abnormal and needs the most skill. Operators arrive 15 to 30 minutes early to build a picture of the process. Very fast failures (seconds) need an automatic response. [a03]
  - Irony 4 (advice): she lists four advice types (Thompson, 1981): causes, importance, alternatives, how to implement. Following advice gives slower, less integrated reactions than generating a response yourself. Ephrath (1980) found aided performance worse than unaided because the operator decided anyway and checking added workload. [a02, a04]
- Hollnagel and Woods (1983), "Cognitive systems engineering: new wine in new bottles". Founding paper. Not opened. [a06]
- Woods (1984) visual momentum; Woods (1995) the alarm problem; Rasmussen, Pejtersen and Goodstein (1994); Hutchins (1995, distributed cognition). Names only, via a reference list. [a05]

### 2.2 Consolidation (1993-2012)

- Hollnagel (1993), Human reliability analysis: context and control. Introduced the contextual control model (COCOM). Table reproduced second-hand by Lenat et al. (2025). [d12]
- Hollnagel and Woods (2005), Foundations of CSE; Woods and Hollnagel (2006), Patterns in CSE. Books. Not opened. [a07, c27]
- Klein, Woods, Bradshaw, Hoffman and Feltovich (2004), "Ten challenges for making automation a team player". Position paper. Not opened. The requirements "interpredictability, common ground, directability" are second-hand. [a26]
- Sarter, Woods and Billings (1997), automation surprises. Not opened (the stub opened does not cite it). [a27]
- Hollnagel (2012), Coping with complexity. Not opened. [a28]
- Parasuraman and Manzey (2010), complacency and automation bias. Not opened. Encyclopedia figures only: cancer detected in 46% of cases without aids vs 21% when the aid missed the cancer; accuracy rose 29% to 50% with decision support, but 7% of answers right without it were changed to wrong. No sample sizes. [a08, b25]

### 2.3 COCOM control modes

Four modes, defined by (1) number of goals, (2) subjectively available time, (3) how the next action is chosen, (4) how outcomes are evaluated. Table as reproduced from Hollnagel 1993 p.22 by Lenat et al. (2025). [d12]

| Mode | Goals | Time | Action choice | Evaluation |
|---|---|---|---|---|
| Strategic | several | abundant | prediction-based | elaborate |
| Tactical (attended) | several, limited | limited but adequate | plan-based | normal |
| Tactical (unattended) | | more than adequate | unreflective | imprecise |
| Opportunistic | one or two, competing | short or inadequate | association-based | cursory |
| Scrambled | one | very limited | random | rudimentary |

Mode choice depends on perceived time and familiarity. The only independent human test found is Stanton, Ashleigh, Roberts and Xu (2001): teams in a simulated energy distribution task could be coded into the four modes, and transitions followed the predicted linear progression. Seen as an abstract only; sample size and coding agreement unknown. [d13, S]

### 2.4 The modern strand (2020-2026)

The JCS question was rebuilt as "human-AI complementarity" and then as "how should a program coordinate model calls". Three lines:

- Human-AI team experiments (Bansal 2021, Bucinca 2021, Vasconcelos 2023, Hemmer 2024, Kim 2024, Si 2024, Steyvers 2025). Do explanations, confidence and forcing functions make the team better than its best part?
- Field and trial studies of AI assistance (Peng 2023, METR 2025, Brynjolfsson 2023, Dell'Acqua 2023, Mozannar 2022, Lee 2025). Does assistance help in practice, and who gains?
- LLM-to-LLM structure (Kim 2025 scaling, Cemri 2025 MAST, Stechly 2023-24, Huang 2024, Panickssery 2024, Laban 2025). When one model checks or coordinates another, what happens?

Vaccaro, Almaatouq and Malone (2024) is the pivotal synthesis. [a09, b01]

## 3. Core findings with exact numbers

Status is the claim status from claims.jsonl unless noted. Evidence ids in brackets.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Human-AI pairs do worse than the better of human or AI alone | Hedges g = -0.23 (95% CI -0.39 to -0.07, p = 0.005); 106 experiments, 370 effect sizes; I2 = 97.7%; 5126 papers screened, 74 kept (Jan 2020-Jun 2023) | Vaccaro 2024 [a09, b01] | [E] on average; one meta-analysis |
| Pairs beat the human alone | g = 0.64 (CI 0.53-0.74); 0.63 in one table row | Vaccaro 2024 [a09, b01] | [E] |
| Task type moderates | Decision tasks g = -0.27 (CI -0.44 to -0.10); creation tasks g = +0.19 (CI -0.09 to 0.48, n = 34, not significant); difference p = 0.006 | Vaccaro [a10, b02] | [S] K02 |
| Who is better alone moderates | Human better: g = +0.46 (CI 0.28-0.66). AI better: g = -0.54 (CI -0.71 to -0.37). Augmentation over human when AI better: g = 0.74. Over 95% of systems gave the human the final say | Vaccaro [a10, b03] | [S] K03 |
| Explanation, confidence display, participant type, division of labour are not significant moderators | not significant for synergy or augmentation | Vaccaro [b04] | [S] |
| Explanations do not beat a confidence display; they raise acceptance of wrong AI answers | Beer: human 0.82, AI 0.84, team+confidence 0.89, team+Explain-Top-1 0.88 (t = -1.18, p = .24). LSAT (20 items): AI 65%, human 67%, confidence team +20.1% relative. Amzbook only +2.2%. About 100 per condition; 3 datasets | Bansal 2021 [a11, b05, b06, c16] | [E] K04 |
| Prior studies: team below AI | deception detection: human 51.1%, AI 87.0%, team 74.6% (another 54.6 / 86.3 / 74.0); income 65 / 75 / 73; nutrition 0.46 / 0.75 / 0.74 | Bansal Table 1 [b07] | [E] pattern |
| Overreliance is a cost-benefit choice | 5 studies, N = 731 (340, 340, 286, 114, 76). Easy maze: explanation no effect; harder mazes: overreliance lower; higher pay cut overreliance; Study 5: utility higher for easy-to-read explanations and hard tasks. Simulated AI 80% accurate | Vasconcelos 2023 [a13, b10, b11] | [S] K05 |
| Forcing functions reduce overreliance, do not remove it | N = 199 analysed (260 recruited); simulated AI 75% accurate. Correct when AI wrong: no AI 0.18, simple XAI 0.03, forcing 0.09 (carb source 0.49, 0.08, 0.27). d = 0.37 overall, 0.66 carb. chi2(2, N = 663) = 13.30, p = .0013. High need-for-cognition people gained (0.44 vs 0.23 overall) | Bucinca 2021 [a12, b08, b09, c15] | [S] K06 |
| Complementary AI realises more potential | inherent potential 0.2480 vs 0.0640 (d = 3.81); share of inherent potential realised 58% vs 89% (d = 3.43) | Hemmer 2024 [a14] | [S] |
| Hedged LLM output lowers over-agreement | N = 404, medical QA, pre-registered. Accuracy with unhedged AI 63.9% vs no AI 74.2%. AI correct: 88.5% vs 77.9%. AI wrong: 33.0% vs 64.7%. First-person hedges raised accuracy | Kim 2024 [b12, b13] | [E] K07 (with Steyvers) |
| Users overestimate LLM accuracy; longer explanations raise confidence, not accuracy | 301 participants (284 analysed); example item: model confidence 0.46 vs human confidence 0.95 | Steyvers 2025 [c18] | [E] K08 |
| Convincing wrong explanation misleads | 80 crowdworkers. Hard claims: no aid 59%, retrieval 73%, explanation 74%. Time 1.01 vs 2.53 min per claim. When explanation wrong: 0.35 (+/-0.22) vs 0.56 (+/-0.24) with contrastive explanation (p = 0.009) | Si 2024 [c17] | [E] K08 |
| Felt vs measured productivity can differ in sign | METR: 16 developers, 246 tasks (136 AI-allowed, 110 not), about 2.0 h each. Forecast 24% faster, post-hoc estimate 20% faster, measured 19% slower. Economists forecast 39%, ML experts 38%. Fewer than 44% of generations accepted | METR 2025 [a18, b15-b17, c08] | [S] K09 |
| Coding trials give opposite signs | Peng: N = 95 (45 treated, 50 control), 71.17 vs 160.89 min, 55.8% faster, CI 21-89%, p = 0.0017; both groups predicted about 35%. METR: 19% slower | Peng 2023 [a17, b14]; METR | [E] K10 |
| Weaker partner gains most | 5,179 agents; +14% issues per hour on average; +34% for novices and low-skilled; minimal for experienced. Workers followed suggestions 35% of the time. Consultants: bottom half gained more | Brynjolfsson 2023 [a19, b19]; Dell'Acqua [b21] | [E] K11 |
| Frontier effect | Inside (18 tasks): +12.2% tasks (control 82%, GPT 91%, GPT+overview 93%), 25.1% faster. Outside (one task): correct 84.5% control vs 60% and 70.6% with AI, about 19 points lower | Dell'Acqua 2023 [b20]; a25 and c25 are recalled, "over 40% quality" not verified | [S] K12 |
| Verification is a hidden cost | 21 programmers; "I don't know" segments 6.5% of time; after accepting without checking, verified afterward 53.2% of the time; mean verification 15.21 s (median 6.48 s), nearly 5x the naive figure. METR: about 9% of time reviewing AI output (44 valid recordings) | Mozannar 2022 [a16]; METR [b17] | [E] K18 |
| Critical thinking shifts to checking | 319 workers, 936 examples; creation 39.96%, information 32.37%, advice 27.67%; critical thinking enacted in 59.29% | Lee 2025 [a20, b22] | [S] survey |
| Multi-agent gain depends on decomposability | 260 configurations, 6 benchmarks, 5 architectures, 3 LLM families. Best multi-agent change from +80.8% (decomposable finance, centralized) to -70.0% (sequential planning, independent). Cross-validated R2 = 0.373 | Kim 2025 [c01] | [S] K13 |
| Single-agent saturation | beta = -0.236, p = 0.004; 45% threshold matches 94% of cells (binomial p < 0.001) | Kim 2025 [c02] | [S] K13; no replication |
| Planning degrades under multi-agent | PlanCraft: -39% to -70%; dynamic web navigation: decentralized +9.2%; tool-count x coordination beta = -0.096, p = 0.002 | Kim 2025 [c04] | [S] |
| Error amplification by topology | Trace-level: single 1.0, centralized 4.4, hybrid 5.1, decentralized 7.8, independent 17.2; the amplification term was not significant after controls (p = 0.658) | Kim 2025 [c03] | [C] K14 |
| Multi-agent failure taxonomy | 1642 traces, 7 frameworks, 14 modes; kappa 0.88 (humans, 150 traces); LLM judge accuracy 94%, kappa 0.77. Shares: design 41.8%, misalignment 36.9%, verification 21.3%. Reasoning-action mismatch 13.2%, incomplete verification 8.2%, incorrect verification 9.1%, no clarification 6.8%. Failure rates 41% to 86.7% by framework | Cemri 2025 [c05, c06] | [S] K15 |
| Interventions in MAST | ChatDev, GPT-4o: role specification +9.4% success; high-level objective verification +15.6% on ProgramDev | Cemri 2025 [c07] | [S] |
| Collaborative agents win with real users | Win rates over autonomous: 86% travel, 74% tabular, 66% related work; 150 real trajectories. Failures: communication 65%, situational awareness 40% (real); simulated 80% and 47%. Agent ignored human messages 46%, repeated messages 26%, repeated or omitted actions 33%. Users spent 21-32% of actions on direct control | Shao 2026 [a22, c10-c12] | [S] K16 |
| Asking for help | Autonomous 30.3% completion; with a simulated user holding side information 51.9% (+71%); agent asked in 10% of tasks. Smarter simulated user: 42.6%, help asked in 4.3%. SUS 74.58; 41.7% would use frequently | Magentic-UI [c13, c14] | [S] |
| LLMs presume common ground | GPT-3.5 follow-ups down 64.3%, acknowledgments down 83.4%, clarification down 84.8% on one set and never produced on two others. Mistral 7B: PPO cut base rate 7.0% and agreement 39.0%; DPO 12.1% and 42.5%. Grounding acts present in 11.83% of utterances (human data) | Shaikh 2024 [a21] | [S] K17 |
| LLM self-verifier under-accepts | 500 colorings, 118 correct; GPT-4 called only 30 correct, right 5 times. Of 100 optimal colorings it accepted 2. Back-prompting produced a correct colouring in 40 of 100 runs; verifier missed all 40. Verifier FNR 20.7% (Game24) up to 97%; FPR 6.5% to 18.6% | Stechly 2023, 2024 [d01, d02] | [E] K23 |
| Sound program verifier turns samples into accuracy | Game of 24: standard 5%, LLM+LLM 3%, LLM+sound verifier 36-38%, k = 25 sampling 42%. Graph colouring 16 / 2 / 34-38 / 44. Blocksworld 40 / 55 / 60-87 / 72. Mystery Blocksworld 4 / 0 / 6-10 / 14 | Stechly 2024 [d02] | [E] K23, K26 |
| Self-correction without feedback hurts | GPT-3.5: GSM8K 75.9 to 74.7; CSQA 75.8 to 38.1 (round 1), 41.8 later; HotpotQA 26.0 to 25.0. GPT-4: GSM8K 95.5 to 89.0; CSQA 82.0 to 80.0; HotpotQA 49.0 to 43.0. With oracle labels GPT-4 GSM8K 97.5, HotpotQA 59.0 | Huang 2024 [d03]; Kamoi 2024 survey [d04] | [E] |
| Judges favour their own text | GPT-4 picks itself out 73.5%; GPT-3.5 and Llama 2 over 90% after fine-tuning on 500 examples; self-recognition vs self-preference Kendall tau = 0.41; bias tracks low perplexity; MT-Bench judges agree over 80% with humans | Panickssery 2024 [d05]; Wataoka 2024 [d06]; Zheng 2023 [d07] | [E] K24 |
| Mixed model families help debate | Debate beat CoT in about 15% of comparisons; Heter-SoM +6.4%, Heter-EoT +8.2% over single-model averages; up to +5.8% over CoT average; MATH +29 to +33 points but MBPP -2 to -10% for some methods | 2502.08788 [d08] | [S] K25 |
| Sampling plus exact verifier vs model selection | MATH, Llama-3-8B-Instruct: coverage 82.9% at 100 samples to 98.44% at 10,000; majority vote or reward model only 40.50% to 41.41% | Brown 2024 [d10] | [E] K26 |
| More calls help easy items, hurt hard | optimal call count predictable from a small sample | Chen 2024 [d09] | [S] K27 |
| Multi-turn underspecified tasks lose accuracy | Average drop 39%; aptitude -15%; unreliability +112%; 6 tasks, 200,000+ simulated conversations; o3 and DeepSeek-R1 degrade similarly; recap helps partly | Laban 2025 [d11] | [S] K28 |

## 4. Mechanisms and models

Each is written so an engineer can build it.

### 4.1 The program/model split as a joint system (CoALA frame)

Program owns: state, step order, memory, checks, selection. Model owns: filling open slots (restate, propose, repair). This matches CoALA, where the language model is a callable component inside a program-controlled decision loop, and Shneiderman's point that automation level and human control are two separate axes. [a23, a24, K19, E]

Implementation: every model call gets (a) a typed input assembled by code, (b) a typed output slot, (c) a code-side parser. Nothing the model says is read as a decision unless code can check it.

### 4.2 The checker's job and its two failure directions

Human checkers over-accept (they follow the AI when it is wrong). LLM self-checkers mostly under-accept (GPT-4 accepted 30 of 500 colorings, 5 right) and miss correct answers. A same-family judge also leans toward familiar text. [d01, d05, d06] So a model checker has two errors, false reject and false accept, and both are high in the families tested. Build:

1. Prefer a program check (run, test, symbolic verify, counterexample). Result is a structured object: pass/fail, failing input, observed vs expected.
2. If a model must judge, give it no authorship, no majority, no proposed final answer (G5), and make the judgment narrow and cheap (diff, one test, one claim).
3. Have the model produce its own answer before it sees the candidate (independent first pass), then compare in code. Human evidence: forcing a commit raised the correct rate on AI-wrong items from 0.03 to 0.09 (still far below the no-AI 0.18 in that cell). [c15]
4. Never feed rationale prose alone. Explanations raise acceptance of wrong answers. If used, supply a for-argument and an against-argument (contrastive: 0.35 to 0.56 on wrong-explanation items). [c17]

### 4.3 Cost-benefit view of reliance

Vasconcelos' framework: a person checks when the cost of checking is below the benefit of being right. Explanations reduce overreliance only when they make checking cheaper than redoing the task. For an agent: the check must cost fewer tokens than regenerating. Design the check as a structured diff or test, not a re-derivation. [b10, b11, K05]

### 4.4 Complementarity condition

Synergy needs the two parts to be right on different items (Hemmer: inherent potential 0.2480 vs 0.0640). If one part dominates, the pair collapses toward the better part and any extra step is cost (Vaccaro: AI-better g = -0.54). Implementation: log per-class accuracy of the model alone and of the program check; give the final say to the stronger side per class. [a14, b03]

### 4.5 Multi-agent structure as topology choice

Kim 2025 predicts multi-agent gain from task properties (decomposability, tool count, baseline). Rules derived from the reported data: (1) do not split sequential tasks across model roles; (2) above about 45% single-agent accuracy, extra coordination goes negative in their data; (3) a central check showed lower trace-level error amplification than other topologies (not significant after controls). [c01-c04]

### 4.6 COCOM as a budget rule (hypothesis only)

Map perceived time to token budget and familiarity to class pass rate. Abundant budget, unfamiliar class: strategic (plan, predict, elaborate evaluation). Moderate: tactical (plan-based, normal evaluation). Short: opportunistic (association answer, cursory check). Very short: scrambled (one answer, no check). This is a design hypothesis, not a finding. Schema S0 already chooses a mode from the class pass rate. [d12, K29]

### 4.7 Hand-back state

Bainbridge: the human needs 15-30 minutes to rebuild the picture before take-over. Laban: LLMs lock onto early assumptions and earlier own attempts in multi-turn work. Implementation: after a failed check, pass a clean state summary built by code (task, failing output, what was tried and why it failed), not the full history. Not yet tested against full history at equal tokens. [a03, d11]

## 5. What holds up

### 5.1 Replicated or multi-source

- Explanations do not reliably improve complementary performance; they raise acceptance. Bansal (3 datasets), Vaccaro (not a significant moderator across the corpus), Si (convincing wrong explanations), Steyvers (length raises confidence). Different labs and tasks. [E]
- Verification cost is real. Mozannar (53.2% post-hoc verification), METR (about 9% of time reviewing AI output), Lee (checking replaces production), Simkute (review). [E] on direction.
- Weaker partner gains most. Brynjolfsson (+34% novices), Dell'Acqua (bottom half), Peng (less experienced gained more). [E]
- Coding trials have opposite signs by task and expertise. Peng (+55.8%, greenfield, N = 95) vs METR (-19%, mature repos). [E] that both occur; the cause is not isolated.
- LLM self-verification fails where no external signal exists. Huang, Stechly (two papers), Kamoi survey. [E]
- Sound external verifier plus sampling works. Stechly, Brown. [E]
- Same-family judges are not independent. Panickssery, Wataoka. [E]

### 5.2 Single-source or weak

- The synergy-loss meta-analysis is one study with I2 = 97.7%, so the pooled mean hides large spread; the moderators matter more. Coverage ends mid-2023 and over 95% of systems gave the human the final say, so it says little about program-final designs.
- The 45% saturation and the amplification numbers: one paper, one lab, no replication. The amplification term was not significant (p = 0.658), so K14 is contested. [c02, c03]
- The frontier effect rests on one task outside the frontier. [b20]
- METR has 16 developers. The abstract says about 20 candidate factors (evidence rows say 21: 5 supported, 10 mixed, 6 against). Recording shares (143 h of video, 44 valid recordings, 29% of hours) are different cuts; do not quote a total. [critique]
- Collaborative Gym and Magentic-UI use simulated users in part.
- Dell'Acqua "over 40% quality" is a recalled figure, not verified.

### 5.3 Reconciled conflicts

- Bansal (explanations add nothing) vs Vasconcelos (explanations help when checking is cheap): reconciled by task difficulty. The reconciliation comes from one lab.
- Peng vs METR: differences in task, expertise and tools; no controlled test separates them.
- Vaccaro (pairs lose on decisions) vs Bansal (pairs beat both when accuracies are matched): fits the moderator "who is better alone".

### 5.4 Interventions that worked, partly worked, or did not

| Intervention | Result | Verdict |
|---|---|---|
| Confidence display | Beer team 0.89 vs 0.88 with explanations | As good as explanation; cheaper |
| Cognitive forcing | Correct on AI-wrong items 0.03 to 0.09; below no-AI 0.18; helped only high need-for-cognition people | Partial |
| Hedged first-person output | Accuracy up in medical QA | Worked |
| Contrastive explanation | 0.35 to 0.56 on wrong-explanation items | Worked |
| Higher pay for accuracy | Lower overreliance | Worked (humans only) |
| Role specification (MAST) | +9.4% | Worked, one framework |
| High-level objective verification (MAST) | +15.6% | Worked, one framework; many verifiers "only superficial checks" |
| Model self-critique without feedback | CSQA 75.8 to 38.1 | Failed |
| Same-family LLM judge | Self-preference, tau 0.41 | Failed as an independent checker |
| Multi-agent on sequential tasks | -39% to -70% | Failed |
| Recap of earlier turns | Helps, stays below single-turn | Partial |

### 5.5 Known gaps (read before trusting this section)

- Almost no human-AI evidence uses an LLM checking an LLM. Most use crowd workers, simulated AI or small classifiers.
- Original CSE texts (Hollnagel and Woods, Klein et al., Sarter et al.) were not opened.
- No token-cost comparison of verify vs plain loops exists in the sources read. [d15]

## 6. Language models

How they behave on joint-system tasks, and what moved the results.

1. As the AI half of a human team. Unhedged LLM output lowered human accuracy below no-AI (63.9% vs 74.2%). First-person hedges raised accuracy. Users overestimate LLM accuracy; longer explanations raise confidence without accuracy; a convincing wrong explanation cut accuracy to 0.35. [b12, c17, c18]
2. As their own checker. GPT-4 under-accepts correct colorings (30 of 500 called correct, 5 right; 2 of 100 optimal colorings accepted). Verifier FNR 20.7% to 97%; FPR 6.5% to 18.6%. LLM+LLM gave 3% on Game of 24 vs 5% standard; a sound verifier gave 36-38%. [d01, d02]
3. Self-correction without a real signal. GPT-3.5 CSQA fell from 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0; with oracle labels GPT-4 GSM8K reached 97.5. The gain comes from the label, not the reflection. [d03]
4. Self-preference. GPT-4 recognises its own output 73.5%; bias follows familiarity (low perplexity). [d05, d06]
5. Heterogeneity. Mixing families in debate: +6.4% and +8.2% over single-model averages. Same-model debate beats CoT in about 15% of comparisons. No equal-token checker-family test exists. [d08]
6. Multi-agent systems. Gains from +80.8% to -70.0% depending on decomposability; above 45% single baseline, coordination goes negative (single paper). Failure shares 41.8 / 36.9 / 21.3%. [c01, c06]
7. Agents with real users. Collaboration wins 66-86%, yet 65% of cases show communication failures and 40% situational-awareness failures. Agents ignore human messages (46% in simulation). [c10-c12]
8. Grounding. GPT-3.5 produces 84.8% fewer clarification acts than humans in one set; preference tuning made it worse (PPO -39.0% agreement, DPO -42.5% on Mistral 7B). Magentic-UI agents asked for help in only 10% of tasks (4.3% with a smarter user). [a21, c13]
9. Multi-turn. 39% average drop, mostly unreliability (+112%). [d11]
10. Sampling plus selection. Coverage 82.9% to 98.44% with samples; majority vote or reward model only 40.50% to 41.41%. A program verifier turns coverage into score. [d10]
11. Difficulty split. More LM calls help easy queries and hurt hard ones. [d09]

What changed outcomes, by measured size: an exact external verifier (3% to 36-38%) > dropping extra roles on sequential tasks (avoids -39% to -70%) > mixed-family debate (+6.4 to +8.2%) > added objective verification (+15.6%, one framework) > role clarity (+9.4%) > recap (partial). Model-side judging added nothing in the tests read.

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. **Keep the program/model split; the program holds the final say wherever a program check exists.** Schema part: architecture, G5. [E] K19, K23, K26. Evidence a23, a24, c23, d01, d02, d10. Already in the schema; this confirms it with size: 36-38% vs 3% on Game of 24.
2. **Never use a model as a free-standing verdict on its own or a same-family candidate.** Schema part: G4, G5. [E] K23, K24. Evidence d01-d07. Already consistent with G5 and 4b; the new numbers (FNR up to 97%, tau 0.41) can be cited under G5.
3. **Do not feed rationale prose to a checker as evidence; judge from outputs.** Schema part: G10, S8 input. [E] K04, K08. Evidence a11, b05, b06, c16, c17, c18. G10 already covers the model's own reasoning; this adds the human-team confirmation.
4. **Count checking tokens in the budget.** Schema part: G7. [E] K18. Evidence a15, a16, a20, b17, c20. G7 counts setup cost; extend to check cost.
5. **State the task class with every scaffold claim; never accept felt improvement as the score.** Schema part: measurement, G7. [E] K10 (K09 [S]). Evidence a17, a18, b14, b15.
6. **Pass full failing output on hand-back to the model.** Schema part: G2, S5. [E] K20 for the direction. Evidence a01, a03, d11. The clean-summary vs full-history choice is untested (Test first).
7. **Do not split sequential items across model roles.** Schema part: 4b. [S] K13 plus G9 [E]. Evidence c01, c04, d08. Consistent with G9; no schema change.

### Test first

| # | Candidate | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Independent first pass by the checker, then code compares | S8, G4 | [S] K06 | a12, b08, b09, c15 |
| T2 | Different-family model as the only model checker where no program check exists | G5, G4 | [S] K25; problem itself [E] K24 | d05, d06, d08 |
| T3 | Per-class final say: model answer stands where model alone beats the check; veto only where the check is stronger | S0, S8 | [S] K03 | a10, b03 |
| T4 | Routing by item type: extra checking only on generative items | S0 | [S] K02 | a10, b02, d03, d09 |
| T5 | Scaffold gain by model size: bigger on the smaller model | S0, G12 | [E] for humans K11; untested for LLM scaffolds | a19, b19, b21 |
| T6 | Scaffold gain by difficulty tier; check for loss on the hardest tier | G12, S0 | [S] K12, K27 | b20, d09 |
| T7 | Clean state summary vs full history after a failed check | G2, S5 | [S] K28 | d11, a03 |
| T8 | Assumption-listing step on ambiguous items | S1 | [S] K17 | a21, c13 |
| T9 | Candidate carries a calibrated confidence into the checker | S7 | [E] for humans K07 | b12, b13, c18 |
| T10 | Contrastive input to a checker (for plus against) | S8 | [E] for humans K08 | c17 |
| T11 | Cheap structured check (diff, test result) vs prose check | S8 | [S] K05 | b10, b11 |
| T12 | COCOM-style budget-driven mode choice vs one fixed prompt | S0 | [S] K22, K29 | d12, d13 |
| T13 | Coordination only below the 45% single-agent threshold | S0, G12 | [S] K13 | c02 |
| T14 | MAST 14-mode checklist on our own failure logs (logging aid, not a schema change) | S6, logs | [S] K15 | c05, c06, c07 |

## 8. Concrete tests on our bench

All arms at equal tokens (count setup, check and retry tokens). Metric: pass rate on held-out items, paired over the same items (McNemar or paired bootstrap). Always include the plain model and the current schema as arms. "Wrong-candidate acceptance" = share of known-wrong candidates a checker lets through.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 independent first pass | Items with an exact check; candidate pool has wrong and right answers | A: checker sees candidate, then judges. B: checker answers alone first, code compares. C: plain | Wrong-candidate acceptance; final pass rate | B lowers wrong acceptance (human analogue 0.03 to 0.09); small net gain, may not beat plain |
| T2 checker family | Items without an exact check | A: same-family checker. B: other-family checker. C: majority vote in code | False-accept and false-reject rate at fixed tokens | B lowers false accept by a few points; both stay below a program check |
| T3 per-class final say | Mixed classes (ARC-like, puzzles, QA) | A: model always final. B: program always final. C: per-class by logged accuracy | Pass rate per class and overall | C at least equals the better of A/B in each class; B loses where the check is weak |
| T4 task-type routing | Decision (pick among options) vs generative items | A: extra checks everywhere. B: checks only on generative. C: plain | Pass rate by type | A hurts on decision items (Vaccaro -0.27 vs +0.19); B best |
| T5 size routing | Same items on a small and a large model | scaffold vs plain on each | Gain per size | Larger gain on the smaller model |
| T6 difficulty tier | Items binned by plain pass rate (easy / mid / hard) | scaffold vs plain per tier | Gain per tier | Gain on easy and mid; zero or negative on the hardest |
| T7 hand-back state | Items that fail the first check | A: bare retry. B: failing output only. C: failing output plus code-built summary. D: full history | Repair rate in 1-2 rounds | C >= B > A; D not better than C at higher tokens |
| T8 assumptions | Ambiguous or underspecified items | A: list assumptions then answer. B: answer directly | Accuracy; tokens | Gain only on ambiguous items; a cost on clear ones |
| T9 confidence into checker | Mixed right and wrong candidates | A: candidate only. B: candidate plus calibrated confidence from sample agreement | Checker error on wrong candidates | Lower error with B |
| T10 contrastive input | Items with convincing wrong candidates | A: candidate rationale. B: for plus against arguments. C: none | Checker accuracy on wrong candidates | B > A (human: 0.35 vs 0.56) |
| T11 check cost | Items with a test suite | A: structured diff or test result. B: prose critique | Accuracy and tokens of the check step | A cheaper, as accurate |
| T12 mode by budget | Items from easy to hard | A: fixed prompt. B: mode chosen by class pass rate and remaining budget | Pass rate at equal tokens | Gain only if S0 modes differ in cost; may equal current S0 |
| T13 saturation | Classes with plain pass rate below and above 45% | scaffold depth vs plain | Gain by class pass rate | Gain below, none or loss above |
| Felt vs measured | Any | Model self-rates its scaffolded output vs program score | Sign of gap | Self-rating above measured (METR analogue); a measurement caveat, not a schema change |

## 9. What does not transfer, and why

- Human vigilance decay (Mackworth, half an hour). Our checker is a program or a fresh call; it does not tire. The design lesson holds (do not put a monitor on a task the code can do); the fatigue mechanism does not. [a01, a02]
- Operator skill decay. The model has no skill that fades through disuse. What survives is the need for a good state at hand-back. [a03]
- Trust and complacency as attitudes. The model has no trust. Its analogue is conformity to a stated answer (G5), already in the schema.
- Explanations as persuasion. In humans, explanations raise acceptance. The analogue in an LLM checker is rationale text in the prompt; it may bias the same way, but no direct LLM test was found.
- Pay and incentives (Vasconcelos Study 4). Not applicable; token budget is the nearest analogue.
- Need for cognition. A person trait; "be careful" prompts did not work (4b).
- Crowd-worker results with simulated AI at 75-80% accuracy. The checker's accuracy and error structure differ; numbers cannot be reused.
- Productivity trials (Peng, METR, Brynjolfsson). These measure human speed; our bench measures pass rate at equal tokens. Use only the pattern: sign depends on task and expertise.
- Collaborative Gym and Magentic-UI. They need a live user, and our bench has none. The failure modes (ignoring messages, missing situational awareness) show what a single agent does not track, not what to add. [K16]
- Klein's team-player requirements (interpredictability, directability). Defined for human-machine teams; no measured LLM analogue found. [critique gap 9]
- Multi-agent topologies. G9 and 4b exclude extra agents. Kim's results serve as a warning against structure, not a design to adopt.

## 10. Open questions

1. Does an LLM checker over-accept wrong LLM candidates as humans do? Partly closed: GPT-4 mostly under-accepts. No study varies checker family at equal tokens. [gap 1]
2. What is the per-item split on our benchmarks of where the model beats the program check, and the reverse? Not in the literature. [gap 2]
3. What do Hollnagel and Woods say about COCOM beyond the second-hand table, and does a token-budget map beat a fixed prompt? [gap 3, d12, d13]
4. Does extra checking help only on generative items and hurt on decision items for a scaffolded single model? [gap 4]
5. Is the 45% threshold reproduced outside Kim et al., and does it apply to program-loop scaffolds? No replication found. [gap 5, d14]
6. What is the token cost of a verify loop vs plain per solved item? No source reports it. [gap 6, d15]
7. Is there a controlled hand-back study with LLM agents? Laban is the nearest analogue. [gap 7]
8. Does the frontier effect show up as a scaffold-induced loss on the hardest tier? Indirect support only. [gap 8, d09]
9. Which of Klein's team-player requirements have measurable LLM analogues? [gap 9]
10. Does an LLM judging its own scaffolded output show the METR felt-vs-measured gap? No direct study. [gap 10, d16]
11. Is the Vaccaro task-type split robust for post-2023 LLM systems? Its coverage stops mid-2023.
12. Do results change if the model, not a human, holds the final say? Over 95% of systems in the meta-analysis gave the human the final say.

## 11. Sources

[V] = opened and read this session (full text, or an abstract page with the numbers confirmed). [M] = snippet, abstract only, recalled, or not opened.

| Source | Mark | URL |
|---|---|---|
| Bainbridge (1983) Ironies of automation | [V] | https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf |
| Wikipedia: Cognitive systems engineering (references) | [V] | https://en.wikipedia.org/wiki/Cognitive_systems_engineering |
| Wikipedia: Automation bias (figures) | [V] | https://en.wikipedia.org/wiki/Automation_bias |
| Hollnagel and Woods (1983) CSE: new wine in new bottles | [M] | https://doi.org/10.1016/S0020-7373(83)80034-0 |
| Hollnagel and Woods (2005) Joint Cognitive Systems: Foundations | [M] | https://doi.org/10.1201/9781420038194 |
| Woods and Hollnagel (2006) Patterns in CSE | [M] | https://www.routledge.com/Joint-Cognitive-Systems-Patterns-in-Cognitive-Systems-Engineering/Woods-Hollnagel/p/book/9780849339332 |
| Klein et al. (2004) Ten challenges for making automation a team player | [M] | https://doi.org/10.1109/MIS.2004.74 |
| Sarter, Woods, Billings (1997) Automation surprises | [M] | https://en.wikipedia.org/wiki/Automation_surprise |
| Hollnagel (2012) Coping with complexity | [M] | https://doi.org/10.1007/s10111-011-0202-6 |
| Parasuraman and Manzey (2010) Complacency and bias | [M] | https://doi.org/10.1177/0018720810376055 |
| Vaccaro, Almaatouq, Malone (2024) When are combinations of humans and AI useful? | [V] | https://arxiv.org/abs/2405.06087 |
| Vaccaro et al., Nature Human Behaviour version | [M] | https://www.nature.com/articles/s41562-024-02024-1 |
| Bansal et al. (2021) Does the whole exceed its parts? | [V] | https://arxiv.org/abs/2006.14779 |
| Bucinca, Malaya, Gajos (2021) To trust or to think | [V] | https://arxiv.org/abs/2102.09692 |
| Vasconcelos et al. (2023) Explanations can reduce overreliance | [V] | https://arxiv.org/abs/2212.06823 |
| Hemmer et al. (2024) Complementarity in human-AI collaboration | [V] | https://arxiv.org/abs/2404.00029 |
| Simkute et al. (2024) Ironies of generative AI | [V] | https://arxiv.org/abs/2402.11364 |
| Mozannar et al. (2022) Reading between the lines | [V] | https://arxiv.org/abs/2210.14306 |
| Peng et al. (2023) GitHub Copilot productivity | [V] | https://arxiv.org/abs/2302.06590 |
| Becker et al. (METR, 2025) Early-2025 AI and experienced developers | [V] | https://arxiv.org/abs/2507.09089 |
| Brynjolfsson, Li, Raymond (2023) Generative AI at work | [V] | https://www.nber.org/papers/w31161 |
| Lee et al. (2025) GenAI and critical thinking survey | [V] | https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf |
| Shaikh et al. (2024) Grounding gaps in language model generations | [V] | https://arxiv.org/abs/2311.09144 |
| Shao et al. (2026) Collaborative Gym | [V] | https://arxiv.org/abs/2412.15701 |
| Mozannar et al. (2025) Magentic-UI | [V] | https://arxiv.org/abs/2507.22358 |
| Sumers et al. (2024) CoALA | [V] | https://arxiv.org/abs/2309.02427 |
| Shneiderman (2020) Human-centered AI | [V] | https://arxiv.org/abs/2002.04087 |
| Dell'Acqua et al. (2023) Jagged technological frontier (full-text mirror) | [V] | https://digital-fluency.pages.dev/research/foundational/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier.pdf |
| Dell'Acqua et al. (SSRN abstract; recalled figures not used) | [M] | https://papers.ssrn.com/abstract=4573321 |
| Kosmyna et al. (2025) Your brain on ChatGPT | [V] | https://arxiv.org/abs/2506.08872 |
| Kim et al. (2024) I'm not sure, but | [V] | https://arxiv.org/abs/2405.00623 |
| Si et al. (2024) LLMs help humans verify truthfulness, except when convincingly wrong | [V] | https://arxiv.org/abs/2310.12558 |
| Steyvers et al. (2025) What LLMs know and what people think they know | [V] | https://arxiv.org/abs/2401.13835 |
| Zhou et al. (2024) REL-A.I. | [M] | https://arxiv.org/abs/2407.07950 |
| Tomasev, Franklin, Osindero (2026) Intelligent AI delegation | [V] | https://arxiv.org/abs/2602.11865 |
| Kim et al. (2025) Towards a science of scaling agent systems | [V] | https://arxiv.org/abs/2512.08296 |
| Cemri et al. (2025) Why do multi-agent LLM systems fail? | [V] | https://arxiv.org/abs/2503.13657 |
| Stechly, Marquez, Kambhampati (2023) GPT-4 doesn't know it's wrong | [V] | https://arxiv.org/abs/2310.12397 |
| Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations | [V] | https://arxiv.org/abs/2402.08115 |
| Huang et al. (2024) LLMs cannot self-correct reasoning yet | [V] | https://arxiv.org/abs/2310.01798 |
| Kamoi et al. (2024) When can LLMs correct their own mistakes? | [V] | https://arxiv.org/abs/2406.01297 |
| Panickssery, Bowman, Feng (2024) Evaluators recognize and favor own generations | [V] | https://arxiv.org/abs/2404.13076 |
| Wataoka, Takahashi, Ri (2024) Self-preference bias in LLM-as-a-judge | [V] | https://arxiv.org/abs/2410.21819 |
| Zheng et al. (2023) Judging LLM-as-a-judge | [V] | https://arxiv.org/abs/2306.05685 |
| Stop overvaluing multi-agent debate (2025) | [V] | https://arxiv.org/abs/2502.08788 |
| Chen et al. (2024) Are more LM calls all you need? | [V] | https://arxiv.org/abs/2403.02419 |
| Brown et al. (2024) Large language monkeys | [V] | https://arxiv.org/abs/2407.21787 |
| Laban et al. (2025) LLMs get lost in multi-turn conversation | [V] | https://arxiv.org/abs/2505.06120 |
| Lenat et al. (2025) A novel skill modeling approach (COCOM table) | [V] | https://arxiv.org/abs/2509.12851 |
| Stanton, Ashleigh, Roberts, Xu (2001) Testing Hollnagel's COCOM | [M] | https://bura.brunel.ac.uk/handle/2438/1680 |

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 12 established claims: 11 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E13.01-K10** (reworded: the sources support less). Numbers match (95 developers, 55.8% less time, p=0.0017; 16 developers, 246 tasks, 19% more time), but the trials also differ in year, tool, population and task, and neither paper tests that task or expertise explains the sign difference (Peng only reports larger gains for less experienced developers). Corrected claim: Two randomised trials point in opposite directions: GitHub Copilot cut completion time 55.8% on a self-contained HTTP-server task (95 developers, Peng et al. 2023), while allowing AI made 16 experienced developers 19% slower on 246 real issues in mature repos (METR 2025); the studies differ in tool, year, task and population, so the cause of the difference is not established.
