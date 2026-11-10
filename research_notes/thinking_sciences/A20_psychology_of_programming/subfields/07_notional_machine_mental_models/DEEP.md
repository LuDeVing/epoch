# Notional machine, mental models: deep document

*Subfield A20.07. Evidence files: evidence_a-d.jsonl (ids a01-a30, b01-b28, c01-c29, d01-d16). Claims: claims.jsonl (A20.07-K01 to K29). Critique: critique.md. Written 2026-11-10.*

## 1. What it is

A notional machine (NM) is an idealised machine implied by a programming language. It says what each construct does to state. Variables are boxes, a pointer moves along lines, objects live on a heap. It is not the real hardware. It is a simplified model that a teacher gives a learner so the learner can predict what a program will do. [a01, a02, b27]

A mental model is different. It is the model a learner actually holds in the head. Teachers build an NM. Learners build mental models. Papers often confuse the two. [a04]

A model is "viable" if it matches how the concept really works and keeps matching in every use. A "non-viable" model works on some programs and fails on others. [a09]

Why this matters for our agent. Schema state S2 asks the agent to trace a program on a concrete input. Tracing is running a notional machine by hand. The human literature tells us what goes wrong when the machine in the head is wrong, which written forms of tracing help, and when a teaching aid helps. The LLM literature tells us:
- a model that writes down its machine state after every step beats a model that guesses the output, but only if the model is strong enough;
- a real interpreter beats a model-written trace;
- a right output does not prove a right machine model.

Scope limits of the evidence:
- Origin papers (du Boulay 1981, 1986; Sorva 2013) were not opened. Definitions come through the 2020 working group report (a02). Marked [M] in sources.
- Human evidence on teaching an NM is small and not replicated at scale.
- Almost all LLM studies test output prediction. Very few test whether giving the model an explicit machine description helps.

## 2. History and theories in depth

**1981: coinage.** du Boulay, O'Shea and Monk used "notional machine" in "The black box inside the glass box". They taught Logo to trainee primary teachers (du Boulay) and school children (O'Shea). The idea was to show novices an idealised machine so the real machine stays hidden. Definition as quoted in 2020: "the idealised model of the computer implied by the constructs of the programming language". The founders did not run a controlled comparison of NM teaching against another method. Logo turned out harder to learn than they expected. [a01, a06]

**1986: du Boulay, "Some difficulties of learning to program".** Learners must build the NM, and many build it wrongly. This is the standard citation for the term. [b27, M]

**2001 and 2004: the tracing studies.** McCracken et al. (2001) reported that most first-year students could not write a working program (recalled mean about 22 of 110; not verified [b26, M]). Lister et al. (2004) asked why. They gave 12 multiple-choice code reading questions to novices in 7 countries. Many could not trace simple code or complete near-finished code. So weak problem solving was not the only cause. [a12, b16]

**2006-2014: the "camel has two humps" episode.** Dehnadi and Bornat claimed a short assignment questionnaire split students into those who can and cannot program, via a consistent mental model. A replication attempt (Caspersen et al. 2007) found no link, though a reader argued it was not a true replication [a17, M]. Bornat retracted the strong claim in 2014 and said the test was not an aptitude test. The retracted document was never peer reviewed. [a15, a16] This is a refuted result for "a consistent model predicts success".

**2007-2008: viability of models.** Ma, Ferguson, Roper and Wood tested first-year students on assignment and object reference. They then ran a teaching experiment with visualisation, with and without cognitive conflict (the learner predicts, then sees the real result disagree). [a09, a10, a11]

**2013: Sorva.** Review that made NM a standard term and narrowed it to program execution. It argues for making the NM an explicit learning objective. Not opened [b28, M]. It is cited as often as the original paper, so many later papers inherit the narrow, execution-only view. [a04]

**2017-2018: tutors and strategies.** Nelson, Xie and Ko built PLTutor, which teaches how programs run by stepping through fixed examples, and compared it to Codecademy. Xie, Nelson and Ko tested a 5 to 10 minute memory-table tracing lesson. [b18, b19]

**2020: the ITiCSE working group (Fincher et al., 12 authors).** Redefined NM broadly: "a pedagogic device to assist the understanding of some aspect of programs or programming". Four traits: purpose, function, focus, representation. It frames NMs as "education of attention": an NM draws attention to one aspect and ignores the rest. It separates Aristotelian idealisation (a true simplified model) from Galilean idealisation (a distorting model). It collected 43 example NMs from interviews, papers and tools. It reviewed 226 papers. [a02, a03, a05, b21, b22]

**2021: Rules of Program Behavior (Duran, Sorva, Seppala).** Proposes writing an NM as an explicit ruleset, judged by viability and coverage, in progressions. Notes that a new ruleset can break an earlier understanding and send the learner back a stage (neo-Piagetian view). Proof of concept: five rulesets for Python expressions, variables and functions. No learner experiment. [a07, a08, b23]

**Competing view (fragile skills).** Lister et al. found few errors came from a clear misconception. Only Q6 (the meaning of "return") showed a frequent one. They read most failures as weak tracing and abstraction skill, not a wrong machine. [a14] Crichton et al. (2021) add a mechanism: working memory. People hold about 7 variable-value pairs and swap values under load. [b15]

**LLM era.**
- 2021: Nye et al. scratchpads. The model writes machine state after each step. [c01, c02]
- 2023-2024: benchmarks that test whether models can execute code in the head. CRUXEval, CodeMind, REval, La Malfa et al. [a20, a22, b04, c06]
- 2023-2025: hybrid machines (Chain of Code), trace-trained models (NExT, CodeExecutor, SemCoder, execution tuning, CWM), and traces as repair input. [a28, a26, b08, c20, c16, c17]
- 2025-2026: robustness studies show that high scores hide pattern matching. [c26, c28, d12]

## 3. Core findings with exact numbers

Status key: E = established (2+ independent sources agree), S = single source, C = contested, R = refuted.

**Human findings**

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Novices keep non-viable machine models after a course | N=90 first-years. One third non-viable on value assignment. Only 17% viable on object reference assignment. Viable-model students did better on exam and tasks | Ma 2007 [a09] | E (with a12, b20) |
| Wrong models cluster on few types | Pre-test N=60: 10 held model ME, 12 held M2Ss; only 4 held other wrong models | Ma 2008 [a11] | S |
| Tracing questions fail often | Lister 2004: 941 students gave data, 556 answered all 12. Quartiles: top 10-12 (27%), bottom 0-4 (23%). Q2 right for 65%. Cited work: over 60% wrong on execution questions | [a12, b16, b20] | E |
| Writing the trace down goes with correctness | Blank page 50% right (256 data points); computation 60%; position marks 64%; numbers 70% (189); trace 75% (215); synchronized trace 77% (73). N=56 students | Lister 2004 [a13, b17] | S (observational) |
| Strong students trace, weak students guess | Q2: about 90% of top quartile vs about 30% of bottom quartile right. Chance 25% | [b25] | S |
| Few errors are misconceptions | Frequent misconception in 1 of 12 questions (Q6, return). Guessing in about 10% of answers | [a14, a13] | S |
| Teaching a tracing strategy raised scores | N=24 (13 vs 11). Mean 30.00 (SD 4.91) vs 24.55 (SD 9.16). p=.049, d about 0.72. Many-variable item p=.021, 11 of 13 perfect. Midterm +7%, p=.083 (not significant) | Xie 2018 [b18] | S |
| Visualisation + cognitive conflict repaired assignment models | N=60 volunteers, 18 with wrong assignment models. All 18 changed; 14 (78%) reached the right model. CC+Viz 9/10 (90%) vs Viz 5/8 (62.5%). No significance test reported | Ma 2008 [a10] | S |
| Visualisation failed on execution flow | 12 with wrong flow model; 6 (50%) changed to the right model, 6 did not. Half did not notice the model was wrong | Ma 2008 [a10, a11] | S |
| NM-based tutor (PLTutor) beat Codecademy | 4.33 hours. 18 vs 19 after data loss. SCS1 gain 3.89 vs 2.42 of 27 (60% higher). d=.59 (p<.12); learning gain d=.398 (p<.41). Only PLTutor pre-post significant (p<.0044). Gain predicted midterm R2=.64 vs .18 | Nelson 2017 [b19] | C |
| Independent tutor study: explicit NM gave no benefit | N=48. Both groups learned; no group difference. Abstract only, master's thesis | Carleton 2022 [d14] | S; makes K05 contested |
| Human tracing is working-memory limited | About 7 variable-value pairs (N=15). Substitution errors 70% more common than calculation errors. 9 of 12 used one strategy 70%+ of the time | Crichton 2021 [b15] | S |
| Consistent model predicts programming success | Claim retracted by author 2014 | Dehnadi/Bornat [a15, a16] | R |
| The NM term is loosely used | 226 papers. 116 (under 50%) define it. 72% cite as background. 27% use one in an intervention. Evaluations: 19% qualitative, 17% quantitative, 8% both | Fincher 2020 [a03, b21] | S |

**LLM findings: tracing and execution**

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Scratchpad (write state each step) beats direct execution | Synthetic Python, 200 problems: direct 11% few-shot, 20% fine-tuned; scratchpad 26.5% (relaxed scoring) and 41.5%. Polynomial evaluation: 8.8 to 20.1 few-shot, 31.8 to 50.7 fine-tuned. Addition trained on 1-8 digits fails on 9-10 digits without scratchpad | Nye 2021 [c01, b06] | E |
| Real-program scratchpad is still weak | MBPP-aug 23.4%, CodeNet 25.2%. Best mix: 26.6% final output right, 24.6% perfect on all three examples, about 42% of single traces exact | Nye 2021 [c02, a19] | S |
| Short Python functions are hard without CoT | CRUXEval, 800 functions of 3-13 lines. GPT-4: 63% output, 67% input. Best open model: 44% output, 47% input | Gu 2024 [a20, b01] | E |
| CoT helps the strongest model on output | GPT-4: 63 to 81.9% output, 67 to 74.8% input. Helps Code Llama 34B on both, GPT-3.5 on output only, Code Llama 13B on neither. GPT-3.5 output: 159 items lost, 340 gained (direction partly unresolved) | Gu 2024 [a21, c04, b02] | E |
| GPT-4 with CoT still fails some items | 0/10 on 54 output and 65 input tasks; 22 on both | Gu 2024 [b02] | S |
| Writing skill is not tracing skill | WizardCoder 34B and Phind 34B over 20 points above Code Llama 34B on HumanEval, no matching CRUXEval gain; Phi-1 among the worst on CRUXEval | Gu 2024 [b03, c05] | E |
| Runtime reasoning is weak and inconsistent | REval: average accuracy 44.4%, incremental consistency 10.3. GPT-4-Turbo 75.0% and IC 42.5; GPT-3.5 55.7%; best open 51.0% | Chen 2024 [b04, c11] | S |
| CoT effect flips sign by task | REval CodeLlama-7B-Instruct: path prediction 10.8 to 21.4% with CoT; output prediction fell 6.8 points | [b05, c12] | S |
| Reasoning models beat GPT-4 on execution | CodeMind IER: +14.76 (Claude-Sonnet-4.6), +11.35 (o4-mini), +9.26 (DeepSeek-R1); R1 rate 90.43%. DeepSeekCoder-Inst 6.7b 45.54% to 33b 60.23% | Liu 2026 [a22, b10] | E |
| Straight-line simulation falls with length | 10 to 50 line programs. GPT-4, LLaMA3-70B, GPT-3.5 reliable on mixed ops; Jurassic2-Ultra, LLaMA2-70B, CodeLlama-34B fail on short snippets. GPT-4 skipped the trace in over 95% of cases | La Malfa 2024 [c06, c07] | S |
| Line-by-line simulation prompt flips sign by model | Chain of Simulation helped GPT-4 on straight-line code, hurt it on nested loops, reverse for LLaMA3-70B | La Malfa 2024 [c08] | S |
| Accuracy falls with executed steps | Linear decline with log(array length), R2=0.975. DeepSeek-R1 7.5% at Level 3 (about 1M reasoning tokens) | Ding 2025 [c29] | S |
| Reasoning models still err on computation | 427 snippets x 12 inputs. Accuracy 85-98%. Computation errors most common, then control flow. No aliasing category in the nine types | Abdollahi 2025 [c25, d10] | S |
| A tool fixes computation errors | Computation errors 439 to 181 (58.8% fixed; Claude 131 to 56, R1 155 to 57, Gemini 82 to 36, GPT-4o mini 71 to 32). About 40% remained | Abdollahi 2025 [d11] | S (upper bound, hand-written fix) |
| CoT helps mostly on execution steps | Meta-analysis of 110 papers, 1,218 comparisons. Symbolic +14.2, math +12.3, logic +6.9. Other tasks 56.8 vs 56.1. Tool beats CoT at execution | Sprague 2025 [d01, d02] | E |
| Chain of Code hybrid interpreter | BIG-Bench Hard 84%, +12 over CoT (abstract) | Li 2023 [a28] | S |

**LLM findings: repair, feedback, trace as input**

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Trace-trained model repairs better | PaLM 2-L +26.1 on Mbpp-R (23.2 to 49.3) and +14.3 on HumanEvalFix-Plus. No trace at test time: 40.8% | Ni 2024 [a26, b09, c13] | E (needs training) |
| Prompted CoT over a trace hurts untuned models | -7.8 on HumanEvalFix-Plus (DeepSeek Coder 57.3 to 30.5; StarCoder 29.3 to 16.5). Removing traces cost -4.8 and -4.3. Only about 30% of rationales explained the error correctly | Ni 2024 [a27, c14] | E |
| Raw traces in repair prompts help few settings | Better in 2 of 6 dataset/model settings. GPT-3.5 no lift; GPT-4 significant on 2 of 3 datasets | Haque 2025 [b13] | S |
| Real trace beats symptoms only | Defects4J, GPT-3.5: 224 correct fixes; symptoms only 165 (-26.3%). 38,000 tokens per bug vs 210,000 and 270,000 for others | Wu 2026 [d05] | S |
| Block-level real values help debugging | Up to +9.8% pass@1. Model-written dry-run traces failed to improve seed programs (StarCoder, HumanEval) | Zhong 2024 [c19] | S |
| Model-written trace adds little to self-debug | MBPP, Codex: baseline 61.4, simple feedback 57.6, +explanation 64.4, +trace 66.2 (1.8 over explanation) | Chen 2023 [c18] | E (with others) |
| Self-repair is uneven at equal budget | APPS: only GPT-4 gains clearly; Code Llama and GPT-3.5 match or lag resampling. Better feedback lifts repair: human feedback 52.6% vs GPT-4 feedback 33.3% (40 programs, 16 people) | Olausson 2024 [d03, d04, d16] | E |
| Self-correction without outside signal hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0. Oracle labels lift (GPT-4 GSM8K 97.5) but leak the answer | Huang 2024 [d06] | E |
| Interpreter feedback helps, self-critique does not | CRITIC GSM8K: +2.1 with tool, -1.8 without | Gou 2024 [d07] | E |
| One I/O example helps code writing | pass@1 +5.36 avg; ClassEval +9.78; HumanEval +0.94. Unused inputs +5.56 | Liu 2026 [a23, b10] | S |

**LLM findings: understanding versus pattern matching**

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Right output, wrong trace | 16 LLMs. 81.42% of simulations coherent; of those 46.92% right output, 53.08% wrong. Consistency across tests 48.87% random, 45.37% weak | Liu 2026 CES [b12] | E |
| Repair is not reasoning | CodeMind: repair not correlated with reasoning except at frontier. 45.00% and 39.58% of successful repairs were shortcuts or lucky hallucination | Liu 2026 [a24, b11, c10] | E |
| Mutation breaks older models | LLM-List: DeepSeek-Coder loses about 54 points; Qwen coder 26-35; QwQ, R1, o3-mini at most 4. Reversion above 50% for DeepSeek-Coder | Yang 2025 [c28] | E |
| Frontier models are not fully robust either | GPT-5.2: 99.24% on CRUXEval, about 76.4% under renaming/transformation (McNemar p<.001), input perturbation about 79.6 to 56.1. PSR 56.14. Gemini 3 Pro 99.24 to 95.79 and 98.37; PSR 97.16. GPT-5 Nano PSR 82.75. R1 family 38-67% but stable | Spiess 2026 [c26, d12] | S |
| One sentence of language rule moves accuracy a lot | GPT-5.2 on exception inputs 15% to 81% when told to track exceptions. Cost: 81 to 76% on non-exception cases (about 4% of right answers became wrong exception predictions) | Spiess 2026 [d13] | S |
| Answers about programs are better than the reasons | GPT-3.5 69%, GPT-4 88% on 399 questions (798 answers). Errors look like novice errors. GPT-4 invents justification for wrong answers. LoopEnd: GPT-3.5 40%, GPT-4 91-100% | Lehtinen 2024 [c22] | S |
| Visual-program trace | ChatGPT TraceCorrect 10.0, GPT-4 60.0; partial 30 vs 70; transitions 10 vs 90 | Singla 2023 [c21] | S |
| CRUXEval is saturated; step counting separates again | o3 78.37% on STEPWISE Hard-Reasoning (504 items) | Yan 2025 [c27] | S |

**Trained-in tracing (outside our scaffold; shows the ceiling)**

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Trace pre-training | CodeExecutor: tutorial set 76.42% vs Codex 13.07%; real set 48.06% output, 33.38% exact trace; no curriculum 45.93 and 30.98 | Liu 2023 [b08, c15] | S |
| Execution tuning | Llama3.1 8B prompted Line-1: 53.8% control flow, 10.6% full state; fine-tuned 99.5% and 96.3%. Traces up to 14k steps | Markosyan 2025 [c16] | S |
| Trace format matters (tuned models) | CRUXEval output: full scratchpad 78.7, compact diff 79.7. Nested-loop MBPP (58-74 lines): direct 47.3, full 64.5, compact 77.4, compact+step-in 80.6. Process accuracy 76.3 vs 64.5 | Markosyan 2025 [d08, d09] | S |
| Monologue beats raw trace as training data | CRUX-I/O/LCB-Exec: few-shot 39.5/41.2/36.1; scratchpad 48.8/50.6/39.9; concise trace 52.1/55.6/35.9; monologue 61.8/63.5/58.5. SemCoder 6.7B CRUXEval-O 63.9 (GPT-3.5 59.0) | Ding 2024 [c20] | S |
| World-model mid-training | CWM 32B, over 120M traced functions: 94.3% CruxEval-O, 65.8% SWE-bench Verified | Meta 2025 [c17] | S |

**LLMs on misconceptions**

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Frontier models solve CS1 tracing items | 60 items, 13 LLMs. MC/true-false 100% for four frontier families; Qwen2.5 7B 83.3%. Following a given misconception: Opus 5 96.7%, Qwen3-coder 30B 45.0% (53.3% answered correctly instead), Qwen2.5 7B 38.3%. Diagnosing from a wrong answer 55.0 to 91.7% | Yeltekin 2026 [b14] | S |
| Misconception mining finds real ones but false-alarms | 1,063 samples, 67 misconceptions. Best multi-sample 82.0% vs single 78.5%. Bags with misconceptions 93.3%; correct-only 59.3% | Al-Hossami 2025 [a29] | S |
| Gap detection invents problems | 2,888 explanations. Fabricated problems 27% on fully correct input; 34% on mostly correct | Oli 2024 [a30] | S |
| Older GPT worse with code in MCQs | 59.5% with code vs 77.9% without (530 MCQs) | Savelka 2023 [d15] | S |

## 4. Mechanisms and models

**4.1 The notional machine as a ruleset.** An NM is a state plus rules. State: names, values, references, call stack, current line. Rules: what each construct does to the state. Duran et al. write rules as "rules of program behavior" and score a ruleset by viability (never predicts wrongly on programs in scope) and coverage (share of programs it handles). [a07]

Implementation for an agent:
1. Keep a short list of rules per language feature (assignment copies a value or a reference; `+=` mutates in place or not; when default arguments are evaluated).
2. A trace step is: (line, rule used, state before, state after).
3. A rule that predicts wrongly on any test program is non-viable and is replaced. Code can check this: run the real program and compare.

**4.2 Why wrong models persist.** Learners infer their own rules, often too restrictive. A rule that works on early examples is kept. A new ruleset can break an old one and push the learner back. [a08, b23] Half of Ma's learners with a wrong flow model did not notice it was wrong after the intervention. [a11] Mechanism: a wrong model is not tested until a program disagrees with it, and learners rarely check. For an LLM the analogue is a loose habit that works on common programs and fails on edge cases (exceptions, aliasing). This analogy is our inference, not a measured result.

**4.3 Cognitive conflict.** Predict, then see the real result disagree. Repair rate 90% with conflict vs 62.5% without, cells of 8 and 10, no test. [a10] The agent version is S5/G2: show the real output next to the agent's prediction. The outside signal is what works. Self-judgement without it does not. [d06, d07, d05]

**4.4 Externalised state (why tracing tables help).** Working memory holds about 7 variable-value pairs. Errors are mostly substitution (reading the wrong variable's value), 70% more than calculation errors. [b15] A written table moves state out of memory. In students: synchronized trace 77% vs blank 50%. [b17] In LLMs, the context window plays the same role and the "scratchpad" is the table. A model that outputs only the final value skips the table. GPT-4 did so in over 95% of cases in La Malfa unless forced. [c06]

**4.5 Trace formats (engineering detail).** Tuned-model data only:
- Full state dump at every step: accuracy drops on long loops (64.5% on nested-loop MBPP).
- Diff trace (write only variables that changed per line): 77.4%; with step-in into calls 80.6%. [d08]
- Dynamic scratchpad (state rewritten, history dropped): wins on very long runs (up to 14k steps), loses on short ones. [d09]
- Natural-language monologue beat raw traces as training data. [c20]
- Per-step errors compound. Process accuracy 74-77% per trace means one wrong step out of 20 breaks the answer. [d09]
- Trace length grows with executed lines (avg 73.9 lines for loops). [d09]
No prompted free-form versus structured-table comparison exists.

**4.6 Hybrid machines.** Chain of Code: the model writes code, an interpreter runs what it can, and the model emulates lines it cannot run while tracking state. [a28] Sprague split tasks into plan and execution. CoT helps at execution. A tool at execution beats CoT in most models and datasets. [d02] Abdollahi: replacing a faulty arithmetic step with the real value fixed 58.8% of computation errors. [d11]

**4.7 Trace as repair input.** Real values per line, shown to the repairing model. Helps after trace-aware training (NExT) and for GPT-4, not GPT-3.5 or untuned code models with CoT. [a26, a27, b13] Block-level breakpoints with verification help (+9.8%). [c19] A symptoms-only ablation lost 26.3% of fixes. [d05] Raw traces can swamp the context when long; LLM-optimised formats help more consistently. [b13]

**4.8 Understanding versus pattern matching.** Three checks exist.
- Coherence: judge each step of the model's trace. 81% coherent, but only 47% of those had the right output, and many correct outputs came from shortcuts. [b12]
- Perturbation: rename, transform, change input. Accuracy falls for non-reasoning coders and for GPT-5.2. [c28, d12]
- Consistency: all nearby inputs right. PSR was 56% for GPT-5.2. [c26]

**4.9 Model-strength gate.** CoT, revision and trace prompts help above a strength threshold and hurt below it. GPT-4 gained from CoT on CRUXEval; GPT-3.5 and Code Llama 13B lost items; revision paid off only for GPT-4 on APPS. [a21, d16, b13] No tested detector exists. A pilot (a handful of items, equal-token resample vs trace) is the obvious one.

## 5. What holds up

**Held up (two or more independent sources).**
- Written tracing goes with correct answers in humans and helps strong LLMs. Human evidence is observational. [a13, b17, c01, a20]
- Weak models lose items under CoT. [a21, a27, c12, c04]
- Real execution output helps revision; model self-review does not. Four independent sources. [d03, d05, d06, d07]
- Model-written traces are often unfaithful. 81% coherent, 47% of those correct; 30% of rationales correct. [b12, a27]
- Success on a benchmark is not understanding. Mutation, renaming and input perturbation cut accuracy for older and some frontier models. [c28, d12, c26, c06]
- Code writing and code tracing are separable skills. [b03, c05, b11]
- Reasoning accuracy falls with complexity, length and executed steps. [b11, c25, c29, c06]
- A tool fixes computation errors that simulation makes. [d11, d02, c25]

**Failed, refuted or contested.**
- Camel has two humps: retracted in 2014. The 2007 replication attempt was disputed and was seen only as a snippet. [a15, a16, a17]
- Teaching the NM directly: PLTutor was 60% better in gain, but N=18 vs 19, d=.398 (p<.41) on learning gain, and the group difference was not significant. [b19] The only independent test (N=48, abstract only) found no benefit. [d14] Status: contested. No test with N above 100 exists.
- Visualisation alone failed for half of execution-flow misconceptions. [a10, a11]
- Prompted CoT over traces hurt untuned code models (-7.8). [a27]
- Model-written trace adds only 1.8 points over explanation in self-debug. [c18]
- The misconception account is weak: Lister found few real misconceptions. [a14]
- Raw traces in repair prompts helped only 2 of 6 settings. [b13]
- Intrinsic self-correction lowered accuracy. [d06]

**Moderators.**
- Model strength is the main moderator. GPT-4 and reasoning models gain from tracing; GPT-3.5, Code Llama 13B and untuned small coders do not.
- Task: output prediction gains from CoT; input prediction and repair gain less or lose. [a21, c12]
- Program complexity: nesting, loops, non-primitive types, long runs lower accuracy. [b11, c29]
- Prompt wording: one exception sentence changed accuracy from 15% to 81% (with a 5 point cost on ordinary cases). [d13]
- Trace length and format: on short programs formats tie; on long loops compact beat full by 12.9 points (tuned models). [d08]
- Human trace form: a synchronised trace beat a blank page; loose number jotting was in between. [b17]

**Interventions that worked.**
- Humans: a 5-10 minute tracing strategy (d about 0.72, N=24). Visualisation plus conflict for assignment models (90%, N=18). PLTutor gain (underpowered).
- LLMs: scratchpad for strong models; real interpreter output in the revision slot; a tool for arithmetic; trace-aware training (outside our scope).

**Interventions that did not work.**
- Visualisation alone for execution flow. Prompted trace CoT on weak models. Self-review with no outside signal. Raw long traces for GPT-3.5.

## 6. Language models

**Without CoT (2023-2024 models).** Output prediction on short functions is poor. GPT-4 63%, best open 44% on CRUXEval. GPT-3.5 69% and GPT-4 88% on questions about their own code. Many errors look like novice errors: not tracing, tracing wrongly, wrong line numbers. [a20, c22]

**With CoT or a scratchpad.** GPT-4 goes from 63 to 81.9% on output. Weak models lose items. The meta-analysis says the CoT gain is concentrated on symbolic (+14.2), math (+12.3) and logic (+6.9) and is about zero elsewhere. [a21, d01]

**Reasoning models (2025-2026).** CodeMind IER: Claude-Sonnet-4.6 +14.76 over GPT-4, o4-mini +11.35, R1 +9.26; R1 90.43%. Reasoning models reach 85-98% on traces of HumanEval+/LiveCodeBench snippets across regular, edge and invalid inputs. They are stable under mutation (o3-mini loses at most 4 points). CRUXEval is saturated (over 95%), so harder step-counting benchmarks are needed. o3 reaches 78.37% on STEPWISE-CODEX Hard. R1 gets 7.5% at Level 3 on LongReasonArena. [a22, c25, c28, c27, c29]

**Where they still fail.**
- Computation errors first, control flow second. [c25, d10]
- Edge and invalid inputs raise error counts (HumanEval+ computation errors per model go from 16/20/7/10 on regular inputs to 27/28/34/47 on edge inputs; LiveCodeBench edge 101/114/59/69). [d10]
- Exceptions: GPT-5.2 15% unless told. [d13]
- Perturbation: GPT-5.2 about 76.4% from 99.24%; PSR 56.14. Gemini 3 Pro stable. [d12, c26]
- Long runs: accuracy falls linearly with log of required steps (R2=0.975). [c29]
- Shortcuts: 53% of coherent simulations had a wrong output; GPT-4 and R1 had the most incoherent reasoning, from natural-language shortcuts. [b12]
- Unfaithful explanation: GPT-4 invents justifications for wrong answers. [c22]

**What changed results, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Scratchpad instead of direct (2021, fine-tuned) | 20 to 41.5% | [c01] |
| CoT on GPT-4 | +18.9 points output | [a21] |
| CoT on weak coders | negative (-7.8 on repair; -6.8 on output for CodeLlama-7B) | [a27, c12] |
| Real runtime trace removed (symptoms only) | -26.3% of fixes (GPT-3.5, Java) | [d05] |
| Tool for arithmetic | 439 to 181 errors | [d11] |
| Execution fine-tuning | 10.6 to 96.3% full-state (8B) | [c16] |
| One-sentence exception rule | 15 to 81% on exception cases; -5 on others | [d13] |
| One I/O example for code writing | +5.36 pass@1 avg | [a23] |
| Model strength (reasoning) | +9 to +15 over GPT-4 | [a22] |
| Mutated programs | -54 (older coder), -4 (o3-mini) | [c28] |

**Notional machine given to the model.** No paper tested a full semantics ruleset in the prompt versus plain CoT at equal tokens. The nearest result is the one-sentence exception rule (d13). The execution-tuned models (SemCoder, CWM, Markosyan) in effect bake an NM in by training. [c20, c17, c16]

**Misconceptions and teaching tasks.** Frontier models trace CS1 items at 100% and can follow a stated misconception (Opus 5 96.7%), but code-tuned models often slip back to correct execution (Qwen3-coder 30B: 53.3% answered correctly instead of as the bug). They name misconceptions in code (82.0% best) but false-alarm (59.3% on correct-only bags; 27% fabrication on correct explanations). [b14, a29, a30]

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single source, [C] contested. Claim ids are A20.07-K##.

### Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| 1 | In S2/S4, when the problem includes code and a concrete input, execute the code. Do not accept the model's in-head output as the check. Real run output is the source of truth. | S2/S4, G2, G10 | [E] | K10, K14, K19, K26; b12, c25, d11, d02 |
| 2 | In S5, put the real failing output (and, where cheap, the real run state) in the revision slot. Do not let the model critique its own trace alone. | S5, G2 | [E] | K13, K26; d03, d05, d06, d07, c19 |
| 3 | Never treat a model-written trace as evidence. A coherent trace is right under half the time. Compare to code-run or a held-out check. | G10 | [E] | K14, K22; b12, a27, c22 |
| 4 | A right answer on the given example is not proof of a right machine. Check on a mutated or renamed input. | G3, S8 | [E] | K15; c28, d12, c26, c06 |
| 5 | Gate trace-style prompts by model strength: pilot first, trace only if gain shows. Pure execution (long loops, arithmetic) goes to code-run, not in-head simulation. | S0, G11, G12 | [E] direction; detector [S] | K11, K17, K27; a21, d01, c29, c25 |
| 6 | Allocate execution budget by program complexity (nesting, loops, executed lines). Long runs go to code. | G12 | [E] | K17; b11, c29, c06 |
| 7 | Do not infer correct code from good trace skill, or a right repair from a passing run alone. Check on held-out input. | G3, G7 | [E] | K16; b03, b11, c10 |
| 8 | When tracing in text, make the trace a required output slot with a state after each step. Strong models skip it when not forced (GPT-4 over 95%). | S2 | [E] for strong models | K02; c06, c01, a20 |
| 9 | Do not use an LLM misconception check as a gate. It false-alarms (27% fabrication on correct input). | S9 | [E] | K21; a30, a29 |
| 10 | Do not treat internal consistency of the agent's stated rules as a sign of correctness. | none | [E] (claim refuted) | K07; a16 |

### Test first (not established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | A written rule sheet for language semantics in S2 (aliasing, mutation, exceptions, default args, integer division, scope) vs plain CoT. | S2 | [S] | K08, K25; d13, a07 |
| T2 | Structured per-line state table (diff form) vs free-form tracing. | S2 | [S]; tuned models only | K03, K23; b17, d08, b15 |
| T3 | Prediction next to true output (cognitive conflict) vs rule restatement, for repeat-error reduction. | S5, O3, G2 | [S] human only | K06; a10, d06 |
| T4 | One concrete worked I/O example at S2. | S2/S4 | [S] | K18; a23 |
| T5 | Pilot gate (equal-token resample vs trace) to detect the CoT crossover per task class. | S0, G11 | [S] | K28; d16, a21 |
| T6 | Perturbation check inside S8 (mutated input of the same program). | S8, G3 | [E] for plain prompting; [S] for scaffold | K15; d12, c28 |
| T7 | Alias, reference and mutation probe set. | S2 | open | K29; d10, a09 |
| T8 | A tracing-strategy prompt (memory table) on many-variable programs. | S2 | [S] human only | K04; b18 |
| T9 | Memory: store per-class "trace rules that failed" lessons from S9 as a growing rule sheet. | memory, S9 | [S] hypothesis | K08, K06 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (count setup and rule-sheet tokens). At least 3 seeds. Score ordinary items too, so over-triggering is caught (d13).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 rule sheet | Python programs with edge semantics (shared lists, copy vs reference, in-place vs new object, exceptions, default args, integer division) plus ordinary programs | A: plain CoT. B: CoT plus 300-token semantics sheet. C: sheet only for flagged items | Exact output accuracy on edge items and on ordinary items, separately | +5 to +15 on edge items; up to 5 points loss on ordinary items if over-triggered (from d13) |
| T2 table vs free | Nested-loop programs, 5 to 30 executed lines, many variables | A: free tracing. B: per-line table of all variables. C: diff table (changed variables only) | Final output accuracy; step accuracy by code check | Diff >= full on long loops, tie on short (d08). Prompted effect unknown |
| T3 conflict | Items where the agent's first prediction is wrong (from an A run) | A: error message only. B: its own wrong prediction next to the real output, one line asked. C: rule restatement | Fix rate in revision; repeat-error rate on the next paired item of the same class | B above A by a few points if the real output is the active ingredient (d05: -26% fixes when removed) |
| T4 worked example | Code-writing tasks with ambiguous specs (ClassEval-like) and clear specs (HumanEval-like) | A: none. B: one I/O example | pass@1 | +5 average, +10 on ambiguous, +1 on clear (a23) |
| T5 pilot gate | 40 code-output items; 3 model strengths | A: always trace. B: always direct. C: pilot on 8 items picks the arm | Accuracy at equal tokens | C at least max(A, B) minus 1 point. Pays only if arms differ by more than pilot noise |
| T6 mutation | Items where the model gets the original right | A: plain. B: scaffold with S2 trace plus mutated-input check | Rate of lucky correct answers caught; final accuracy on mutated set | Catch rate positive; accuracy unchanged or higher |
| T7 alias probe | 40 alias and mutation items vs 40 value-assignment items of matched length | Plain CoT vs code-run | Accuracy gap between classes | If gap above 10 points, add a T1 sheet targeted to aliasing |
| T8 interpreter vs in-head | Long-loop and arithmetic-heavy programs | A: in-head trace. B: write code and run it. C: hybrid (code runs, model emulates the rest) | Accuracy, tokens per item | B above A by 20+ points on long loops (c29, d11); B cheaper at 70+ executed lines |
| T9 lesson memory | Repeated class of programs with a known trap | A: no memory. B: S9 lesson line in context | Error rate on second and third items of the class | Positive only if the lesson names the rule; null otherwise |

## 9. What does not transfer, and why

- **Teaching a human the NM.** The human benefit is on learning, not on solving once. The agent carries nothing from one item to the next except through memory. PLTutor gains (60%, N=18 vs 19, not significant) do not map to a prompt effect. [b19]
- **Human misconception repair.** The 90% vs 62.5% result concerns revising a held belief. A model with no stable belief across calls has no "model" to repair, only a response habit. [a10]
- **Camel has two humps.** Refuted for humans. Not applicable to agents. [a16]
- **Working memory limit of 7.** An LLM has a context window, not a 7-item store. The mechanism (externalising state reduces substitution errors) may still help, but it is untested. [b15]
- **Doodle result.** Observational; better students may doodle more. Trace-and-correct is correlated in humans without causal proof. [a13]
- **Visual and spatial NMs** (Hour-of-Code mazes, parking-lot analogies). The one LLM data point is from 2023 models on a small task set. [c21, a05]
- **Trace training results.** NExT, CodeExecutor, SemCoder, execution tuning and CWM improve tracing a lot, but they are training. We do not train. They are an upper bound only. [K20]
- **Misconception-simulation tasks.** Useful for tutoring tools, not for solving. The agent should not model novices. [b14, a29]
- **Human pedagogical vocabulary.** "Education of attention", Aristotelian vs Galilean idealisation. Interesting, but not measured on agents. [a05]
- **Weak-model numbers.** Most trace-gain numbers come from 2021-2024 models and weak coders. Reasoning models change what is true. Re-measure before trusting. [a22, c28]

## 10. Open questions

1. Does an explicit written semantics ruleset in the prompt raise trace accuracy at equal tokens, on edge-case programs, for modern models? (Nearest data: one rule sentence, 15% to 81%, -5 on ordinary.) [d13]
2. Does a real execution trace in the revision slot beat the error message alone for untuned frontier models at equal tokens? (Partial: GPT-3.5 Java, -26.3% when removed.) [d05]
3. At what model strength does a model-written trace stop being worse than answering directly, and can a short pilot detect it? [d16]
4. Does a structured state table beat free-form tracing in prompted LLMs? (Only tuned-model data.) [d08]
5. Does showing the model its own wrong prediction next to the true output reduce repeat errors? [a10, d06]
6. How large are LLM errors on reference, aliasing and mutation compared with value assignment? (Not measured.) [d10, d15]
7. Is there any independent replication of NM teaching effects with N above 100? (None; one null, N=48.) [d14]
8. Do perturbation results hold for scaffolded tracing? (Only plain prompting tested.) [d12]
9. What is the token cost of a state-table trace compared with running code, and where is code-run strictly better? (No head-to-head table; trace length grows with executed lines.) [d09]
10. Does an LLM misconception checker help or harm the agent's own trace review? (27% fabrication on correct input.) [a30]
11. Origin papers (du Boulay 1981 and 1986, Sorva 2013) were not opened. Verify definitions before quoting.
12. Several 2026 results (Spiess GPT-5.2, Yeltekin 2026, LongReasonArena, STEPWISE) were read once and not cross-opened. Tables from Spiess, Abdollahi and CRITIC came from garbled text extraction. Treat headline numbers as firmer than cell values.

## 11. Sources

[V] opened (full text or page read). [M] snippet or secondhand only.

- du Boulay, O'Shea, Monk (1981) The black box inside the glass box. https://doi.org/10.1016/S0020-7373(81)80008-5 [M] (a01)
- du Boulay (1986) Some difficulties of learning to program. https://doi.org/10.2190/3LFX-9RRF-67T8-UVK9 [M] (b27)
- Sorva (2013) Notional machines and introductory programming education. https://doi.org/10.1145/2483710.2483713 [M] (b28)
- Fincher et al. (2020) Notional Machines in Computing Education: The Education of Attention. https://acris.aalto.fi/ws/portalfiles/portal/76828957/SCI_Hellas_Notional_Machines_in_Computing_Education_The_Education_of_Attention.pdf [V] (a02-a06, b21, b22)
- Duran, Sorva, Seppala (2021) Rules of Program Behavior. https://acris.aalto.fi/ws/portalfiles/portal/76041477/Rules_of_Program_Behavior.pdf [V] (a07, a08, b23)
- Ma, Ferguson, Roper, Wood (2007, 2008) viability and improvement of mental models. https://strathprints.strath.ac.uk/32280/1/10.1.1.105.1767_1_.pdf [V] (a09-a11, a15)
- Lister et al. (2004) A multi-national study of reading and tracing skills. https://www.cs.auckland.ac.nz/~j-hamer/ITiCSE04-wg.pdf [V] (a12-a14, b16, b17, b25)
- McCracken et al. (2001) A multi-national, multi-institutional study of assessment of programming skills. https://doi.org/10.1145/571922.572137 [M] (b26)
- Bornat (2014) retraction, Retraction Watch. https://retractionwatch.com/?p=21616 [V] (a16)
- Caspersen, Bennedsen, Larsen (2007) Mental models and programming aptitude. https://mail-archive.com/discuss@ppig.org/msg01296.html [M] (a17)
- Xie, Nelson, Ko (2018) An Explicit Strategy to Scaffold Novice Program Tracing. https://faculty.washington.edu/ajko/papers/Xie2018TracingStrategies.pdf [V] (b18)
- Nelson, Xie, Ko (2017) Comprehension First: PLTutor. https://faculty.washington.edu/ajko/papers/Nelson2017PLTutor.pdf [V] (b19, b20, b24)
- Carleton University thesis (2022) Investigating the Utility of Notional Machine Instruction in an Intelligent Tutor. https://carleton.scholaris.ca/handle/20.500.14718/41641 [V abstract page only] (d14)
- Crichton, Agrawala, Hanrahan (2021) The Role of Working Memory in Program Tracing. https://arxiv.org/abs/2101.06305 [V] (b15)
- Nye et al. (2021) Show Your Work: Scratchpads. https://arxiv.org/abs/2112.00114 [V] (a18, a19, b06, b07, c01, c02)
- Gu et al. (2024) CRUXEval. https://arxiv.org/abs/2401.03065 [V] (a20, a21, b01-b03, c03-c05)
- Liu, Chen, Jabbarvand (2026, v6) CodeMind. https://arxiv.org/abs/2402.09664 [V] (a22-a25, b10, b11, c09, c10)
- Chen et al. (2024) REval. https://arxiv.org/abs/2403.16437 [V] (b04, b05, c11, c12)
- La Malfa et al. (2024) Code Simulation Challenges for LLMs. https://arxiv.org/abs/2401.09074 [V] (c06-c08)
- Ni et al. (2024) NExT. https://arxiv.org/abs/2404.14662 [V] (a26, a27, b09, c13, c14)
- Li et al. (2023) Chain of Code. https://arxiv.org/abs/2312.04474 [V abstract and framing] (a28)
- Liu et al. (2023) CodeExecutor. https://arxiv.org/abs/2305.05383 [V] (b08, c15)
- Markosyan et al. (2025) What I Cannot Execute, I Do Not Understand. https://arxiv.org/abs/2503.05703 [V] (c16, d08, d09)
- Meta FAIR CodeGen Team (2025) CWM. https://arxiv.org/abs/2510.02387 [V partial] (c17)
- Ding et al. (2024) SemCoder. https://arxiv.org/abs/2406.01006 [V] (c20)
- Chen et al. (2023) Self-Debug. https://arxiv.org/abs/2304.05128 [V] (c18)
- Zhong et al. (2024) Debug like a Human (LDB). https://arxiv.org/abs/2402.16906 [V] (c19)
- Haque et al. (2025) Leveraging Execution Traces for Program Repair. https://arxiv.org/abs/2505.04441 [V] (b13)
- Liu et al. (2026) Coherency and Consistency of Code Execution Reasoning (CES). https://arxiv.org/abs/2510.15079 [V] (b12)
- Abdollahi et al. (2025) Demystifying Errors in LLM Reasoning Traces. https://arxiv.org/abs/2512.00215 [V] (c25, d10, d11)
- Spiess, Devanbu, Barr (2026) How Robustly do LLMs Understand Execution Semantics? https://arxiv.org/abs/2604.16320 [V] (c26, d12, d13)
- Yang et al. (2025) Generalization Capabilities of LLMs on Code Reasoning. https://arxiv.org/abs/2504.05518 [V] (c28)
- Yan et al. (2025) STEPWISE-CODEX-Bench. https://arxiv.org/abs/2508.05193 [V] (c27)
- Ding et al. (2025) LongReasonArena. https://arxiv.org/abs/2508.19363 [V] (c29)
- Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 [V] (d01, d02)
- Olausson et al. (2024) Is Self-Repair a Silver Bullet? https://arxiv.org/abs/2306.09896 [V] (d03, d04, d16)
- Wu et al. (2026) DebugRepair. https://arxiv.org/abs/2604.19305 [V] (d05)
- Huang et al. (2024) LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 [V] (d06)
- Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 [V] (d07)
- Savelka et al. (2023) GPT Struggle to Answer MCQs about Code. https://arxiv.org/abs/2303.08033 [V] (d15)
- Lehtinen, Koutcheme, Hellas (2024) Let's Ask AI About Their Programs. https://arxiv.org/abs/2404.11734 [V] (c22)
- Singla (2023) Evaluating ChatGPT and GPT-4 for Visual Programming. https://arxiv.org/abs/2308.02522 [V] (c21)
- Fan et al. (2023) LLMs generating code-tracing questions. https://arxiv.org/abs/2310.15317 [M] (c23)
- Jain et al. (2026) A Plan-Tracing Interface for AI-Supported Algorithm Planning. https://arxiv.org/abs/2602.03197 [V] (c24)
- Yeltekin, Bauer (2026) Can LLMs Simulate Novice Programmers' Misconceptions? https://arxiv.org/abs/2610.10656 [V] (b14)
- Al-Hossami, Bunescu (2025) McMining. https://arxiv.org/abs/2510.08827 [V] (a29)
- Oli et al. (2024) Can LLMs identify gaps and misconceptions in students' code explanations? https://arxiv.org/abs/2501.10365 [V] (a30)

Links to other subfields (not covered here): Working memory; Cognitive artifacts; Program comprehension models (A20.03); Debugging strategies (A20.01); Systematic review of SAT evidence; Debiasing and cognitive forcing; Search over thoughts; Cognitive conflict and impasse; Training; Interactive theorem proving.
