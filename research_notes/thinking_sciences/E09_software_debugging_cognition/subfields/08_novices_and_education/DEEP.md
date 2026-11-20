# Novices and education: deep document

*Subfield E09.08 of software debugging cognition. Sources: evidence_a-d.jsonl (ids a01-a26, b01-b25, c01-c27, d01-d20), claims.jsonl (K01-K23), critique.md. Read this first: the founding studies (Murphy et al. 2008, Fitzgerald et al. 2008, McCauley et al. 2008, Qian and Lehman 2017) could NOT be opened. No sample sizes or strategy counts from them appear here. Most numbers are from 2022-2026 LLM-in-education work, and many use obsolete models (GPT-3.5, Codex).*

## 1. What it is

This subfield asks two linked questions.

1. How do human novices debug, and what goes wrong? Anchor works: Murphy et al. 2008 ("the good, the bad, and the quirky": novices' strategies sorted into good, bad and quirky), Fitzgerald et al. 2008 ("finding, fixing and flailing"), McCauley et al. 2008 (a literature review from an educational view) and Qian and Lehman 2017 (a review of novice misconceptions). All four are closed access in this run. Only titles, citation counts and abstract-level or second-hand claims were seen (a01-a04, a25, d01-d04).
2. What happens when language models (LLMs) take the tutor's role or the novice's helper role? Nearly all numbers are here: help-request diagnosis, error-message rewriting, hints, Socratic dialogue, code generators in classes, and fault localisation on novice programs.

Why it matters to our agent. Our agent is one LLM with a scaffold (a thinking schema). Novice debugging is a clean model of what a weak reasoner does wrong: it guesses, trusts fluent text, does not trace code, assumes the computer "understands" intent, and is over-confident. LLMs show the same failure shape in the studies below (false issues, fluent but wrong fixes). The education literature also tests interventions we are considering: an explicit process, a hypothesis before a fix, a separate validator, a forced explanation step, and asking before answering.

Task fit. A bug has one defect and a real check (tests pass). That fits guardrails G2 (revise only from real output) and G3 (pass on something the answer was not fitted to).

Honest limit. The mapping from human novices to an agent scaffold is by analogy. No study here tests a scaffold at equal tokens against free-form on seeded novice bugs (critique gap 2).

## 2. History and theories in depth

**Novice debugging as strategies (2008).** Murphy et al. classified what novices do into good, bad and quirky strategies (a01). We do not have the counts. Fitzgerald et al. ran a multi-institutional study of novice debuggers. The one claim we have, second-hand via Kurniawan et al. 2025 (a03, a12), is that once students find and locate a bug they can generally fix it. So the hard part is finding, not fixing. Not verified from the paper.

**McCauley et al. 2008 review.** From a course handout of extracts (b01, b02, d04; no counts):
- Some, but not most, novice breakdowns come from misconceptions about language constructs.
- Most come from chains of cognitive breakdowns in skill, rule or knowledge. A rule breakdown is a wrong or bad rule, often from fragile knowledge. A knowledge breakdown is fragile knowledge or the "superbug".
- The superbug is the belief that the language or computer has a hidden intelligence that understands what you meant.
- Most novice bugs are missing or malformed code. Some are endemic across languages: off-by-one, operator precedence, code placed in or out of a loop.
- Finding bugs quickly depends on large-scale program comprehension, not small chunks.

**Qian and Lehman 2017.** Novice difficulties fall into syntactic, conceptual and strategic knowledge. Named causes: unfamiliar syntax, natural language, maths background, inaccurate mental models, lack of strategies, programming-environment problems. 127 references, 466 citations (Crossref). No per-misconception counts were obtained (d03, K23).

**Henley et al. 2021 (a10, a21).** Concept paper: an editor that asks the novice questions about program behaviour, and on a wrong answer explains and inserts assertions. It cites (second-hand) that students take substantially longer to fix semantic errors than syntax errors, that many believe a program is correct when there are no compiler errors, and that Whyline users fixed bugs in half the time of a traditional debugger. No new experiment.

**Teaching a debugging process.** Michaeli and Romeike 2019 (b03-b05) review older work, all second-hand: students keep using whichever process they were taught first (Katz and Anderson, LISP); written debugging notes raised bugs fixed but not bugs found (Allwood and Bjorhag); few students kept using a taught Wolf Fence procedure (Boettcher et al.); one hour of LOGO training shifted brute force toward systematic use with no control (Carver and Risinger). Their own classroom study is in section 3.

**Misconception theory, 2021-2026.** The strand that most affects LLM work: novice bugs are caused by misconceptions, meaning false beliefs. A direct contradiction between the belief and observed behaviour should create cognitive dissonance, so the learner updates the belief and keeps the update (a22). The dissonance and durability claims are assumed, not tested, in the LLM papers. Socratic debugging, teachable agents (HypoCompass), and misconception mining (McMining) all build on it.

**LLMs enter the classroom (2022-2026).**
- 2022: Codex error-message rewrites; Copilot on CS1 problems.
- 2023: help-request diagnosis, Codex in a 10-session class, ChatGPT and GPT-4 versus human tutors, CodeHelp guardrails.
- 2024: CodeAid deployment (700 students), Socratic agents, a semester-long field study.
- 2025-2026: fault localisation with reasoning models, misconception simulation by frontier models, randomised studies on over-reliance, tests of Socratic versus direct help.

The arc: early work asked "can the model do it?" Later work asks "does the novice learn, and what does the model's help cost?"

## 3. Core findings with exact numbers

Status key: established = 2 or more independent sources or a randomised design; single = one source; contested = sources disagree; unverified = not opened.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Founding strategy counts (good, bad, quirky) | Not obtained. Crossref 42 citations (d01); Semantic Scholar 152 (a01) | Murphy 2008 (a01, a25, d01) | unverified |
| Once a bug is found and located, novices usually fix it | Qualitative claim, second-hand | Fitzgerald 2008 via Kurniawan 2025 (a03, a12, d02) | unverified |
| Semantic bugs fix slower than syntax bugs; superbug and fragile knowledge underlie many breakdowns | No counts | McCauley 2008 extracts; Henley 2021 (a10, a21, b01, b02) | established (2 sources, both extract or second-hand) |
| Novices' real help requests are mostly logic errors | 150 requests, 275 issues (1.9 per request): logic 108 (72%), I/O 51 (34%), syntax 12 (8.0%), very incomplete 8 (5.3%) | Hellas 2023 (b07, c02) | single |
| GPT-3.5 finds some real issue in help requests but not all, and invents some | 30-response set: at least one real 90%, all real 57%, false issue 40%. 150-request set: 123/150 at least one real; 82 of those named all issues (82/150 = 55%); false issue in 72 (48%) | Hellas 2023 (c01, c02, b06) | single |
| Codex on the same task is worse | At least one real 70%, all 13%, false 40% (English) | Hellas 2023 (c01) | single |
| Accuracy depends on error type | All issues addressed: conditionals 35%, iteration 73%, arithmetic 57%, output formatting 44%, unwanted output 54%, missing output 50%. By exercise 1/10 worst, 10/10 best, with 4/10 false positives even at the best | Hellas 2023 (c03, a18) | single |
| Instruction "give no code" is ignored | Code in 99-100% of GPT-3.5 responses; Codex 33%. 17/150 suggested out-of-course features; all 6 very incomplete programs got unsuitable replies | Hellas 2023 (c04) | single |
| LLM error-message rewrites are readable but often wrong | 162 outputs: comprehensible 88%, has explanation 84%, correct explanation 48% (11% to 83% by message), has fix 70%, correct fix 33% (17% to 56%), better than original 54%, unnecessary content 32%. Temperature 0 beat 0.7 | Leinonen 2022 (c05, b08) | single |
| Readable LLM error messages do not speed repair reliably | N=106, 6 tasks: GPT-4 beat compiler messages in 1 of 6 tasks; 98% fixed overall. Crowd N=103 (38 novices, 65 experts): ratings rose, fix rate, attempts and time not significantly; novice fix rate 46% standard, 54% pragmatic, 42% contingent | Santos and Becker 2024; Moraru 2026 (d15, d16) | established (2 sources) |
| Observational course data: LLM feedback speeds time to success | 111 novice + 38 advanced students; log-time coefficients single-issue -0.214, diagnostic -0.194 | Mihaylova 2026 (d13) | single, observational |
| GPT-4 vs ChatGPT vs tutor, repair | Correct: ChatGPT 68%, GPT-4 88%, tutor 100%. Edit tokens GPT-4 36.6 vs tutor 19.0. 25 instances, 5 problems | Phung 2023 (a13, c06) | single |
| Hints | Overall good: ChatGPT 18%, GPT-4 66%, tutor 92%. Conceal: 38 / 72 / 94. Explanation correct: 40 / 70 / 94 | Phung 2023 (a13, a24) | single |
| Tasks needing a model of the novice's bug | Grading match: ChatGPT 10%, GPT-4 16%, tutor 52%. Task synthesis: 10 / 22 / 74. Pair programming: 38 / 64 / 82. Contextual explanation: 72 / 84 / 92 | Phung 2023 (c07, c08) | single |
| Separate validator raises precision | GPT4Hints-GPT3.5Val: precision 94.7, 97.6, 95.5 on three datasets, coverage 76.0, 87.5, 73.3. Plain GPT-4 hints about 60%. One trial: 91.7 / 48.0; GPT-4 as validator: 89.3 / 56.0 | Phung 2023 (c09, c10) | single (same group) |
| Run-time validation of syntax-error fixes | PyFiXV: Codeforces baseline precision 35.0, at P70 coverage 64.2; TigerJython baseline 5.0; 240 programs per set | Phung 2023 (a14) | single |
| Repair by prompting with peers' code | 286 real student programs: baseline 67.13%, MMAPR no few-shot 86.71%, with few-shot 96.50%; iterative querying 82.87 to 86.71 | Zhang 2022 (c22) | single |
| Code generator in training: large gain | N=69 (33 Codex, 36 baseline) of 90; authoring correctness 80.1% vs 44.4% (d=1.67); time 210 s vs 361 s (d=1.56); errors per task 1.28 vs 2.17 (d=0.74); syntax errors 0.87 vs 1.67 (d=0.88); docs opened 22.1% vs 54.3% (d=1.33) | Kazemitabaar 2023 (a15, a26, b09, c11) | established for the training phase |
| ...but no reliable gain after removal | Immediate post-test authoring 61.3 vs 62.9 (d=0.05). One week: authoring 59.1 vs 49.8 (d=0.28, p=.262); modifying 47.5 vs 34.8 (d=0.41, p=.092); Codex group more errors on retention authoring 1.58 vs 0.99 (d=0.51, p=.042). Pre-test 62.7 vs 60 (p=.67) | Kazemitabaar 2023 (b09, c12) | established (with d10, d14) |
| Unrestricted AI harms later unaided debugging; forced explanation recovers it | Randomised N=78, 26 per arm, Claude 3.5 Sonnet. Repair after AI removed: manual 18/26 (69.2%), unrestricted AI 6/26 (23.1%), gated 61.5%; chi-square(2)=13.8, p=.001. Gate median 14.2 min; gated slower than unrestricted (d=1.52). Manual arm hit the 90-min cap at 42% of requirements; both AI arms reached 100% | Sankaranarayanan 2026 (d10, d11) | single (randomised, one session) |
| Counterbalanced CS1 crossover | Lab time 494.9 s vs 2385.3 s (assignment 1), 868.0 s vs 1934.3 s (assignment 2), p=.0002 and .0011; code quality higher; concept gains mixed | Andleeb 2025 (d14) | single, self-selected groups |
| Semester field study of an LLM tutor | N=50; score change +12.50 vs -3.17; students new to LLM tools g=0.69, p=.03 (n=42) | Lyu 2024 (c19) | single |
| Novices use generators as answer engines | 33 learners, 45 tasks: 46% of tasks start with a prompt (n=760), 92% of those (703) with no own attempt; full task pasted 66% (503); uses: whole solution 43%, new subgoals 37%, fix code 7% (n=110); fix uses localised correctly 61% (73). By task: AI single prompt 46%, manual 29%, hybrid 19%, step-by-step 6%. 1,666 requests, 52% copied from task text | Kazemitabaar 2023b (b10, c13) | single |
| Weak novices gain less or are harmed | N=21 (20 finished): time mean 17.1 min (SD 8.1); metacognitive difficulty vs time r=0.693; grade vs time r=-0.727; grade vs new difficulties r=-0.503; self-efficacy vs grade r=0.553. Struggling students overrated themselves | Prather 2024 (b12, b22, c15) | established (with Codex subgroup; correlational) |
| Copilot behaviours | Shepherding (retyping suggestions) and drifting (adapting wrong code deeper into a rabbit hole); 13 of 19 accepted code unchanged at least once | Prather 2023 (b11, c14) | single, qualitative |
| Deployed tools: debugging features weakest | CodeAid, 700 students, 563 consented, 1,749 samples: overall correct 79%; Explain Code 95%; General Question 91%; Question from Code 66%; Help Fix Code 63% correct (n=340), helpful 42% | Kazemitabaar 2024 (b19, c18) | single |
| CodeHelp guardrailed tool | 52 enrolled, 49 analysed, 45 survey; about 70% used it in 4+ weeks; about 80% sent 10+ queries, about 50% 30+; 7 of 49 over 100, one over 600; $0.002 per query | Liffiton 2023 (a19, c16, c17) | single |
| Explicit debugging lesson | n=13 vs 15, one teacher, BlueJ: median 4 of 9 bugs fixed vs 2 (p=.049); self-efficacy up (d=0.54 experimental, 0.56 pilot n=14), not in control | Michaeli and Romeike 2019 (b03) | single, non-randomised |
| Teachable-agent debugging | N=19, no control: score +11.7% (p=.033), time -13.6% (p=.003), confidence +15% (Wilcoxon p=.007); 90% generation success on 145 programs | Ma 2024 HypoCompass (b13) | single |
| Socratic agent with state tree | Experts preferred about 78% (79.43% vs BRIDGE, 77.43% vs vanilla); student fix +24.55%; 3-bug drop 14.55% vanilla vs 1.53-2.44% TreeInstruct; no-state ablation: success -18.25%, relevance -46.63%, logic -51.39% | Al-Hossami 2024 TreeInstruct (c20, c21) | single, simulated students |
| Socratic AI TA in a randomised trial | N=132, four TAs. Socratic + full context rated worst for task support; full comprehension of the fix: Direct+Full 67% vs Socratic 48% (not significant); queries per problem 11.1 vs 5.1, 4.1, 4.7 | Eastwood 2026 (d12) | contested vs K10 |
| Planner plus verifier | Fine-tuned 7B planner: premature disclosure 1.88% of turns (24/1,276) vs GPT-4o 7.43% (59/794); plan technically valid 11/53 vs 53/53 with verifier; question quality 1.626 vs 1.446 (p<.001); technical correctness 1.789 vs 1.860 (p=.002) | Kopytskyi 2026 (d08, d09) | single, simulated students |
| Reasoning trajectories | 501 problems, 558 solutions, 40 misconceptions, 227 triplets. GPT-5 RT validity about 91.1% (85-91% over 14 configs); conversation validity 98.7%; Haiku 4.5 no reasoning 62.6%. Judge agreement 76.7% on 30 RTs, 96.6% on 88 turns | Al-Hossami 2026 (a05-a07, b16) | single, LLM judge |
| Socratic benchmark, chain of thought | Manual F1: GPT-3.5 22.2, +CoT 8.5; GPT-4 42.6, +CoT 45.9. False positives GPT-4 41 vs GPT-3.5 93 | Al-Hossami 2023 (d18, b14) | single |
| Frontier models simulate misconceptions | 30 misconceptions, 60 questions, 13 LLMs. Diagnosis free text: GPT-5.6 Sol 91.7%, Sonnet 5 88.3%, Opus 5 86.7%, Qwen2.5:7b 55.0%. From list: 98.3 / 96.7 / 53.3. Followed misconception: Opus 5 96.7%, GPT-5.6 Sol 95.0%, Sonnet 5 90.0%, Qwen3-coder:30b 45.0% vs Qwen3:30b 86.7% | Yeltekin and Bauer 2026 (a08, a09, a23) | single |
| Misconception mining | 1,063 samples, 67 misconceptions: multi-instance 82.0% (Sonnet 4.5 reasoning); bags with a misconception 93.3%; correct-only bags 59.3%; syntax confusions above 95% | Al-Hossami 2025 McMining (b15) | single |
| Logic-error classification with error-type text | GPT-3.5: 35% (30/86) to 56% (48/86); Conceptual stayed low | Lee 2024 (d19) | single |
| Novice fault localisation by 13 LLMs | 503 programs per set. o3 Top-1: Codeflaws 19.7% (99), Condefects 62.0% (312), BugT 57.5% (289); Top-5: 291, 409, 449. GPT-4o Top-1: 101, 213, 177. GPT-3.5: 100, 148, 133. DeepSeekR1 on BugT 248. o3 by difficulty on Condefects 71 (hardest) to 91 (easiest). Cost per program: o3 $0.0152 / 52.4 s; GPT-4o $0.0092 / 15.3 s; o1-preview $0.4859 / 96.4 s; GPT-3.5 $0.0034 / 7.3 s | Xu 2025 (d05, d07) | single |
| Prompt ablation on localisation | 50 programs per set. For o3 and DeepSeekR1 removing parts barely mattered. For GPT-4 every removal hurt; without the novice description Top-1 fell by 7, 3 and 5 programs (to 77.77%, 42.8%, 38.36% as reported) | Xu 2025 RQ3 (d06) | single |
| Logic bugs: students vs LLMs | 964 students; correct rate GPT-3 85.3%, GPT-4 85.0%, students 49.1%; GPT-4 found 1.70 more bugs than students (p<.001); GPT-4 still raised false bugs on correct code | MacNeil 2024 (d17) | single |
| Current models on general CS1 questions | 170 questions; educators mean 2.925 of 5; Gemini 3 flash 3.335, 52.35% of answers top-scored; judge r=0.8185 | Van Mullem 2026 (d20) | single |
| Code inside the question hurts the model | 530 MCQs: 59.5% with code vs 77.9% without (p<.0001); overall 65.5%. Student prompts: pass@1 0.0519 for signatures without docstring. Copilot solved 79/166 CS1 problems first try (47.6%); 53 of 87 unsolved fixed by rewording | Savelka 2023; Babe 2023; Denny 2022 (c23, c24, b20) | established for code-in-question; c24 and b20 are about prompting, not debugging |
| LLM code explanations rated better than students' | Easy 4.12 vs 3.75, accurate 4.0 vs 3.78 (about 1,000 students) | Leinonen 2023 (a20, c25) | single, perception |
| Reflection scaffold initiation | N=120, four groups, ten tasks: T-EMME 6.56, L-EMME 6.93, Auto-EMME 4.06; F(3,116)=132.44; expertise vs score r=0.58 in control, not significant in EMME groups | Golrang 2026 (b17, b24) | contested (no replication; d10 shows a forced gate helping) |
| Prompt-writing mistakes | 887 and 876 students; commonest mistake omitting key details; after failure students clarified intent more than traced code or read tests | Padurean 2026 (b18, b25) | single, self-report |
| CodeHinter | N=10; SUS 75 vs 65; satisfaction 89 vs 60; locate-line feature 4.5/5; 6 of 10 still clicked "Provide Code Solution" | Kurniawan 2025 (a11) | single, tiny |

## 4. Mechanisms and models

Each is written so an engineer can build it. All come from human or tutor-system work; transfer is in section 7.

**M1. Failure chain model (McCauley).** A bug is not one wrong belief. It is a chain: a skill slip, a bad rule from fragile knowledge, a knowledge gap (for example the superbug). Implementation as a diagnostic: when a fix fails, log which link failed (read the code wrong / applied a wrong rule / believed something false about the machine). Count by link over a run. Not measured in the sources; a design suggestion.

**M2. Misconception as root cause (Al-Hossami and Bunescu).** Procedure:
1. Hold a list of candidate misconceptions (40 to 67 in their sets; 30 in ProgMiscon).
2. Given buggy code and a failing test, ask which false belief would produce this behaviour.
3. Build a reasoning trajectory: deductive steps from an observable fact in the failed test to a statement that contradicts the belief. Five rules: strictly deductive, consistent with the false belief, aim only to disprove it, start from observables, label steps and cite premises. Example: `x + y / 2` with x=1, y=3 gives 2.5; list both groupings, compute (1+3)/2 = 2.0, show it differs from 2.5.
4. Turn each step into one question (teacher turn).
Success patterns named by the authors: exhaust the alternatives, trace with concrete values (a06). For our agent the trajectory is a counterexample computed by code, which fits G2.

**M3. State tree for tutoring (TreeInstruct).** Keep an explicit tree of the student's misunderstandings (conceptual, syntactic). Each question targets a node; code updates node status. Without explicit state the system lost 18.25% success and 46.63% relevance (c21). Agent analogue: a list of open hypotheses with status, kept by code.

**M4. Plan, verify, then ask (SocraticRepair).** A planner makes a pedagogical plan; a verifier checks it is technically valid before any question. Unverified fine-tuned planner: 11 of 53 valid. GPT-4o with verifier: 53 of 53 (d09). Implementation: plan object, separate checker call, regenerate on failure.

**M5. Generate, then validate with a weaker independent model (GPT4Hints-GPT3.5Val).** A strong model writes a hint from failing tests and a reference fix. A weaker "student" model tries to use the hint. Keep the hint only if the student succeeds. Repeated trials matter (k=1 gave precision 91.7, coverage 48.0). A GPT-4 student validated worse (89.3 / 56.0). Needs failing tests and a reference fix. The acceptance threshold is the precision knob; coverage is what you give up. Run-time validation also worked for syntax errors (PyFiXV, a14).

**M6. Explanation gate.** Before AI-generated code is applied or kept, the learner must explain why it works. Repair after AI removal 61.5% vs 23.1% unrestricted; cost median 14.2 minutes (d10, d11). Implementation: a required `why_it_works` field checked by a second pass or a probe test.

**M7. Reflection initiation.** Help started by the learner or teacher beat automatic triggering (b17). Auto-triggers produced more backward jumps and pauses (b24). A forced gate in d10 pushes the other way, so this stays contested. For an agent the trigger should be a failure or uncertainty signal, not a timer (G1).

**M8. Guardrail pipeline (CodeHelp).** A chain of prompts that withholds solution code; each query is independent and one-shot because the chance of an off-the-rails answer grows with rounds (c17). Needed because "no code" in the prompt failed (code in 99-100%, c04).

**M9. Metacognition gap (widening gap).** Struggling students keep old metacognitive difficulties, gain new ones with AI, and overrate their performance (b12, b22). Agent implementation: log stated confidence against pass or fail and compare.

**M10. Spectrum-based localisation plus LLM hints plus quizzes (CodeHinter).** Rank lines by coverage in failing versus passing runs; the LLM writes a hint about the top line, then a quiz question. Only a pilot (a11).

## 5. What holds up

**Multi-source.**
- AI code help raises training-phase performance and speed. Three sources agree (Kazemitabaar 2023, Sankaranarayanan 2026, Andleeb 2025). The unaided result differs: no reliable change in the Codex study, a large loss in the randomised 2026 study. K05.
- Readable explanations are not correct explanations and do not reliably speed repair: Leinonen (48% correct), Santos and Becker (1 of 6 tasks), Moraru (ratings up, fix rate flat). K17.
- Weaker novices benefit less and can be harmed, with illusion of competence (Prather 2024; Codex subgroup). K07. Small and correlational.
- Code in the question lowers model accuracy (Savelka 2023; StudentEval and Copilot rewording results are about prompts). K15.
- Semantic bugs are harder than syntax bugs; fragile knowledge and the superbug (McCauley extracts; Henley second-hand). K08.

**Single-source but large.** Hellas help-request numbers (40-48% false issues); Phung benchmarks; the validator pipeline; the explanation gate; reasoning-trajectory papers; the fault-localisation survey.

**Failures and nulls.**
- Retention in the Codex study was not significant (authoring p=.262; modifying p=.092).
- Socratic-first did not improve comprehension and was rated worst for support (Eastwood, N=132; comprehension difference not significant).
- Fluent LLM error messages gave no objective gain in two studies.
- Chain of thought hurt GPT-3.5 on Socratic generation (F1 22.2 to 8.5) and helped GPT-4 (42.6 to 45.9). The idea that reasoning helps smaller models more was not supported there.
- Prompt ablations did not matter for o3 and DeepSeekR1 (d06).
- A fine-tuned planner without a verifier produced valid plans in 11 of 53 cases.
- The "coder penalty" for holding a misconception is not uniform: Qwen3-coder:30b 45.0% vs Qwen3:30b 86.7%, but Qwen2.5-coder:7b 53.4% vs Qwen2.5:7b 38.3% (a23).

**Moderators seen.**
- Prior skill: Codex retention gains concentrated in high-prior-skill learners; the EMME effect removed the advantage of prior expertise.
- Model class: structured prompts helped GPT-4 but not o3 or DeepSeekR1.
- Difficulty: o3 Top-1 71 to 91 by bucket on Condefects.
- Leakage risk: o3 62.0% on Condefects but 19.7% on Codeflaws (public, possibly in training data).
- Error type: conditionals 35% versus iteration 73% (all-issues rate, GPT-3.5).
- Temperature: 0 beat 0.7 for error-message rewriting.
- Item format: True/False easier than multiple-choice; free text harder than list.

**Interventions that worked (small samples).** Explicit debugging lesson (n=13 vs 15, p=.049, non-randomised). HypoCompass (N=19, no control). Explanation gate (randomised, N=78). Validator pipeline (precision about 95%). State tree (simulated students).

**Interventions that did not.** Instructing the model not to give code; readable-error-message prompts; unrestricted AI help for retention; Socratic-first with full context (comprehension); fine-tuned planner without a verifier.

**Weaknesses of the evidence (critique).** No claim has two independent replications of the identical effect. Samples are small. Judges are often LLMs (agreement 76.7% on RTs, 96.6% on turns). Most studies measure output quality, not learning. Many use obsolete models.

## 6. Language models

**2022-2023 models (Codex, GPT-3, GPT-3.5, GPT-4, ChatGPT).**
- Help-request diagnosis: false issues in 40-48%; all issues 55-57%; code written despite instructions (c01-c04).
- Error messages: correct explanation 48%, correct fix 33% (c05).
- Repair and hints versus tutors: GPT-4 88% repair, 66% hints; far below tutors on grading feedback (16% vs 52%) and task synthesis (22% vs 74%) (c06-c08).
- Large jump from weak to strong model: ChatGPT 18% to GPT-4 66% on hints; GPT-3.5 22.2 to GPT-4 42.6 Socratic F1.
- Prompting with peers' code plus iteration raised Codex repair from 86.71% to 96.50% (c22).
- Deployed: CodeAid Help Fix Code 63% correct, 42% helpful (b19).
- Code in the question lowers accuracy (59.5% vs 77.9%).

**2024-2025 models.**
- GPT-4 on logic bugs: 85.0% correct, 1.70 more bugs than students (d17), but false bugs on correct code. Not comparable with the Hellas false-issue rate.
- Fault localisation: reasoning models beat older chat models; LLMs beat spectrum and mutation methods. o3 Top-1 62.0% Condefects, 57.5% BugT, 19.7% Codeflaws; GPT-4o matched or beat o3 on Codeflaws Top-1 (101 vs 99). The authors report over-reasoning in some models. Cost per program $0.0034 (GPT-3.5) to $0.4859 (o1-preview).
- Structured prompts help GPT-4 (dropping the novice description cost 3 to 7 of 50 Top-1 hits) but not o3 or DeepSeekR1 (d06).
- Claude 3.5 Sonnet as helper in the N=78 trial: unrestricted use cost later unaided repair (23.1% vs 69.2%) (d10).
- Misconception mining: 82.0% multi-instance (Sonnet 4.5 reasoning); 59.3% on clean code, meaning many false alarms (b15).

**2026 models.**
- Simulating and diagnosing misconceptions: top models 90-96.7% simulation fidelity, 86.7-98.3% diagnosis; Qwen2.5:7b 38.3% and 53.3-55.0% (a08, a09). Small and code-tuned models drop the wrong belief and solve the question correctly.
- Reasoning trajectories: GPT-5 about 91% valid; Haiku 4.5 with no reasoning 62.6%; reasoning mode added +6.6 (Sonnet 4.5), +16.3 (Haiku 4.5) and -0.8 (GPT-5) points of RT validity (a05). Judge is an LLM.
- General CS1 questions: nearly all current models beat the educator mean (2.925 of 5); Gemini 3 flash 3.335 (d20). Not a code-help false-issue test.

**What changed results, by how much.**

| Change | Effect | Id |
|---|---|---|
| Bigger / newer model | Hints 18% (ChatGPT) to 66% (GPT-4); repair 68% to 88% | c06 |
| Independent weak-model validator | Precision about 60% to about 95%, coverage over 70% | c09 |
| Few-shot from peers + iteration | Repair 86.71% to 96.50% | c22 |
| Error-type descriptions in prompt | GPT-3.5 classification 35% to 56% | d19 |
| Reasoning mode on small model | Haiku 4.5 +16.3 points RT validity; GPT-5 -0.8 | a05 |
| Chain of thought (Socratic) | GPT-4 +3.3 F1; GPT-3.5 -13.7 F1 | d18 |
| State grounding removed | Relevance -46.63% | c21 |
| Plan verifier | Valid plans 11/53 to 53/53 | d09 |
| Novice description in prompt | GPT-4 Top-1 falls by 3 to 7 of 50; none for o3 | d06 |
| Temperature 0 vs 0.7 | Improvement over 70% vs up to 50% (Codex) | c05 |
| Prompt rewording | Copilot 47.6% first try; 60% of the rest solved after rewording | b20 |

**Gaps.** No 2026 model was re-run on the Hellas help-request set (K22). No re-measure of validator precision with current models. No equal-token comparison of a staged process against free-form on seeded novice bugs.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Judge a fix only by tests passing, never by how fluent the explanation is.** Schema: G10, G2. [E] K17, K02 (d15, d16, c05, b08). Readable text correlates poorly with correct text: 88% comprehensible but 48% correct explanation; GPT-4 messages sped repair in 1 of 6 tasks. This is support for existing guardrails, not a new one.
2. **Confirm a diagnosis by running code before acting on it.** Schema: G2, S4. Direction [E] (false issues appear in several LLM studies); rate [S]. K01, K13, K22 (c01-c03, b15, d17).
3. **Keep a calibration check on hard items.** Schema: S9, memory (per-class stated confidence vs outcome). [E] K07 (b12, b22, c12).
4. **Do not add an explanation-quality objective.** Schema: candidate for 4b "not to add". [E] K17.
5. **Restate the task and spec before debugging code-heavy items.** Schema: S1. [E] K15 (c23, c24, b20). The S1 restatement exists; this supports keeping it for code items.
6. **Measure gains with the scaffold off on held-out bugs.** Schema: G7 (measurement rule, not a feature). [E] K05 (a15, b09, c12, d10, d14).
7. **A prompt instruction is not a guardrail.** "No code" was ignored in 99-100% of responses; enforce by a code check. Schema: G5. [S] c04, consistent with G5.

### Test first

8. **Hypothesis before edit.** Schema: S1-S5. [S] K06, K09 (c13, b03). 92% of novice prompts came with no own attempt; the classroom lesson gave p=.049. Human evidence only. UNKNOWNS U1.
9. **Cheap independent validator on any diagnosis.** Schema: G2/S6. [S] K04, K21 (c09, c10, d09). U2.
10. **Misconception-diagnosis step ("what false belief produces this bug?").** Schema: S2. [S] K12, K11, K23 (a08, a09, a05, d19). Nobody measured a localisation gain. U3.
11. **Code-computed counterexample.** Schema: O (disconfirm), S5. [S] K11 (a05, a06). U4.
12. **Explain-before-apply gate.** Schema: G/S9. [S] K20 (d10, d11). For an agent the cost is tokens. U5.
13. **Question-first vs answer-first.** Schema: O. [C] K10 (b13, c20, d12). U6.
14. **Reflection on a signal, not always-on.** Schema: S9, G1. [C] K14 (b17, b24, d11). U7.
15. **Use the staged scaffold only for non-reasoning models.** Schema: S1-S5, S0 gate. [S] K18 (d06). U8.
16. **Route conditional-logic faults to execution.** Schema: S4. [S] K01 (c03). U9.
17. **Report accuracy by difficulty stratum.** Reporting rule. [S] K19 (d05, d07).
18. **False-alarm control on correct code.** Schema: G. [S] K13 (b15). U10.
19. **Seeded misconception sets by class (syntax, concept, strategy).** [S] K23. Needs per-class counts, which we lack.

## 8. Concrete tests on our bench

All arms at equal tokens (G7). Report pass rate with a confidence interval and tokens used. Use seeded bugs with known causes and a real check, so a pass is a real run.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Seeded novice-style bugs (off-by-one, `x + y / 2` grouping, loop placement, conditional logic) with tests | (a) free-form debug, (b) staged: hypothesis, test, then edit | Fix pass rate on held-out tests; Top-1 localisation | Gain for a non-reasoning model; null for a reasoning model (d06) |
| T2 | Help-request items: buggy code plus description, "what is wrong?" | (a) plain, (b) plain plus code-run confirmation of the claimed bug | False-issue rate; all-issues rate | False issues fall well below 40%; all-issues rises from about 55% |
| T3 | Same items | (a) one model, (b) generate plus weaker independent validator, keep only validated | Precision at coverage over 70% | Precision up from about 60% toward 90%, with coverage cost |
| T4 | Items with a misconception root cause | (a) plain, (b) "name the false belief" then fix | Top-1, fix pass rate | Unknown; gain only if naming is right |
| T5 | Same | (a) plain, (b) code-computed counterexample step | Localisation accuracy | Gain on semantic bugs |
| T6 | Fix tasks followed by an unaided held-out version | (a) fix freely, (b) "why it works" check before applying | Pass rate on held-out unaided items; token cost | Gate recovers part of any loss |
| T7 | Items where the first answer is uncertain | (a) always-on reflection, (b) reflection triggered by uncertainty or failure | Pass rate at equal tokens | Triggered at least as good |
| T8 | Correct programs | (a) plain, (b) with verification | False-alarm rate | Lower than the 59.3% seen on clean bags in McMining |
| T9 | Items by difficulty bucket | Any arm | Per-stratum Top-1 | Falls with difficulty (o3: 71 to 91) |
| T10 | Code-heavy items | (a) plain, (b) restate the spec | Pass rate | Gain on code-containing items |
| T11 | Two model classes (reasoning, non-reasoning) | Staged vs free-form | Pass rate by class | Gain for the non-reasoning class only |

## 9. What does not transfer, and why

- **Learning gains.** Retention, self-efficacy and dissonance have no counterpart in a stateless agent. Our only carry-over is memory (S9 lessons).
- **Over-reliance on AI.** Humans lose unaided skill when the tool does the work (Sankaranarayanan 2026). Our agent has no unaided phase.
- **Self-efficacy and satisfaction ratings** (CodeHinter SUS, HypoCompass confidence). Not a measure of correct answers.
- **Pedagogical goals.** Withholding the fix is right for teaching, wrong for us. Socratic dialogue matters only as a way to force a hypothesis, which we can do without a dialogue. Disclosure rate (1.88% vs 7.43%) is irrelevant to an agent.
- **Simulated students.** SocraticRepair and TreeInstruct used LLM students; results are about tutor behaviour, not debugging accuracy.
- **Eye-movement modelling and physiological triggers** (Golrang). No analogue.
- **Child learners** (Codex study, ages 10-17) and **crowd workers.** Their gaps differ from an LLM's.
- **Obsolete models.** GPT-3.5 and Codex rates (40% false issues, 33% fix correct) are likely worse than 2026 models. Do not use them as expected effects.
- **Human novice strategies** (random edits, guess and check) come from the founding paper we could not open. We cannot say they are the agent's failure modes.
- **Misconception frameworks** assume a human holds a persistent belief. A sampled model has no stable belief, so "the misconception" is a prompt device, not a diagnosis of the model.

## 10. Open questions

1. What do Murphy 2008 and Fitzgerald 2008 report (sample, strategy counts, share good/bad/quirky)? Needs library copies.
2. Does a staged hypothesis, test, localise process beat free-form at equal tokens on seeded bugs? Only indirect evidence (d06).
3. Do 2026 models still show 40% false issues and 55% all-issues on the Hellas set? (K22)
4. Does a weak-model validator keep about 95% precision with current models and for code fixes?
5. Does a misconception-naming step raise localisation, and does it survive an independent re-measure?
6. Does the unaided loss from AI help persist beyond one session, in a long randomised study with current tools?
7. Is the benefit of reasoning trajectories larger for small models? The Socratic benchmark says no for chain of thought; a counterexample step was not tested.
8. Is "user-triggered beats automatic" replicated, and what is the agent analogue?
9. What are the per-misconception counts in Qian and Lehman 2017 and McCauley 2008?
10. Does Codeflaws accuracy (19.7%) reflect leakage or genuine difficulty?
11. How reliable are LLM judges of Socratic validity (76.7% on RTs)?

## 11. Sources

[V] = opened and read (per the evidence files). [M] = metadata or snippet only.

- [M] Murphy et al. 2008, Debugging: the good, the bad, and the quirky. https://doi.org/10.1145/1352135.1352191 (a01, a25, d01)
- [M] McCauley et al. 2008, Debugging: a review of the literature from an educational perspective. https://doi.org/10.1080/08993400802114581 (a02)
- [V, extracts only] McCauley et al. 2008 course handout. https://www.tech.dmu.ac.uk/~djohns02/notes/modules/education/EDUC2323/2021/content/Week%203%20Guess%20the%20Number/Handout_ExtractsFromMcCauleyEtAl2008.pdf (b01, b02, d04)
- [M] Fitzgerald et al. 2008, Debugging: finding, fixing and flailing. https://doi.org/10.1080/08993400802114508 (a03, d02)
- [M] Qian and Lehman 2017 (abstract via Crossref). https://doi.org/10.1145/3077618 (a04, d03)
- [V] Henley et al. 2021, Inquisitive code editor. https://arxiv.org/abs/2102.06098 (a10, a21)
- [V] Kurniawan et al. 2025, CodeHinter. https://arxiv.org/abs/2509.21067 (a11, a12)
- [V] Hellas et al. 2023, help requests. https://arxiv.org/abs/2306.05715 (a17, a18, b06, b07, c01-c04)
- [V] Leinonen et al. 2022, error messages. https://arxiv.org/abs/2210.11630 (b08, c05)
- [V] Leinonen et al. 2023, code explanations. https://arxiv.org/abs/2304.03938 (a20, c25)
- [V] Phung et al. 2023, benchmark. https://arxiv.org/abs/2306.17156 (a13, a24, c06-c08)
- [V] Phung et al. 2023, PyFiXV. https://arxiv.org/abs/2302.04662 (a14)
- [V] Phung et al. 2023, GPT4Hints-GPT3.5Val. https://arxiv.org/abs/2310.03780 (c09, c10)
- [V] Kazemitabaar et al. 2023, AI code generators and novice learners. https://arxiv.org/abs/2302.07427 (a15, a16, a26, b09, c11, c12)
- [V] Kazemitabaar et al. 2023, how novices use code generators. https://arxiv.org/abs/2309.14049 (b10, c13)
- [V] Prather et al. 2023, Copilot for novices. https://arxiv.org/abs/2304.02491 (b11, c14)
- [V] Prather et al. 2024, widening gap. https://arxiv.org/abs/2405.17739 (b12, b22, c15)
- [V] Prather et al. 2022, Programming is hard. https://arxiv.org/abs/2212.01020 (c26)
- [V] Ma et al. 2024, HypoCompass. https://arxiv.org/abs/2310.05292 (b13)
- [V] Al-Hossami et al. 2023/2024, Socratic method experiments. https://arxiv.org/abs/2310.03210 (b14, d18)
- [V] Al-Hossami et al. 2024, TreeInstruct. https://arxiv.org/abs/2406.11709 (c20, c21)
- [V] Al-Hossami and Bunescu 2025, McMining. https://arxiv.org/abs/2510.08827 (b15)
- [V by first agents; not re-opened in critique] Al-Hossami and Bunescu 2026, Reasoning trajectories. https://arxiv.org/abs/2511.00371 (a05-a07, a22, b16)
- [V by first agents; not re-opened] Yeltekin and Bauer 2026. https://arxiv.org/abs/2610.10656 (a08, a09, a23)
- [V by first agents; not re-opened] Golrang et al. 2026. https://arxiv.org/abs/2605.04868 (b17, b24)
- [V by first agents; not re-opened] Padurean et al. 2026. https://arxiv.org/abs/2607.05034 (b18, b25)
- [V] Liffiton et al. 2023, CodeHelp. https://arxiv.org/abs/2308.06921 (a19, c16, c17; b23 abstract and intro only)
- [V] Kazemitabaar et al. 2024, CodeAid. https://arxiv.org/abs/2401.11314 (b19, b21, c18)
- [V] Denny et al. 2022, Conversing with Copilot. https://arxiv.org/abs/2210.15157 (b20)
- [V] Michaeli and Romeike 2019. https://computingeducation.de/pub/2019_Michaeli-Romeike_WIPSCE19.pdf (b03-b05)
- [V] Lyu et al. 2024, semester-long field study. https://arxiv.org/abs/2404.13414 (c19)
- [V] Zhang et al. 2022, MMAPR. https://arxiv.org/abs/2209.14876 (c22)
- [V] Savelka et al. 2023, MCQs about code. https://arxiv.org/abs/2303.08033 (c23)
- [V] Babe et al. 2023, StudentEval. https://arxiv.org/abs/2306.04556 (c24)
- [M] Misconception-Aware LLM Programming Tutor, 2026 (Crossref title only). https://doi.org/10.1145/3770761.3777289 (c27)
- [V] Xu et al. 2025, novice fault localisation. https://arxiv.org/abs/2512.03421 (d05-d07)
- [V] Kopytskyi et al. 2026, SocraticRepair. https://arxiv.org/abs/2610.15204 (d08, d09)
- [V] Sankaranarayanan 2026, epistemic debt. https://arxiv.org/abs/2602.20206 (d10, d11)
- [V] Eastwood et al. 2026, Guardrails or roadblocks. https://arxiv.org/abs/2609.29995 (d12)
- [V] Mihaylova et al. 2026. https://arxiv.org/abs/2605.16933 (d13)
- [V] Andleeb et al. 2025. https://arxiv.org/abs/2510.00946 (d14)
- [V] Santos and Becker 2024. https://arxiv.org/abs/2409.18661 (d15)
- [V] Moraru et al. 2026. https://arxiv.org/abs/2608.20896 (d16)
- [V] MacNeil et al. 2024. https://arxiv.org/abs/2311.16017 (d17)
- [V] Lee et al. 2024. https://arxiv.org/abs/2404.19336 (d19)
- [V] Van Mullem et al. 2026. https://arxiv.org/abs/2603.28295 (d20)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 4 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E09.08-K15** (reworded: the sources support less). Savelka confirmed (text-davinci-003 59.5% with code vs 77.9% without, p<0.0001), but StudentEval's pass@1 0.0519 is a control for bare function signatures with no docstring, showing problems cannot be solved without the student's description, not a rate for wrongly specified student prompts. Corrected claim: Models degrade when code is in the question: text-davinci-003 scored 59.5% on code-containing MCQs vs 77.9% without (Savelka). StudentEval's 1,749 prompts from 80 novices show output depends heavily on prompt wording: a bare function signature with no docstring gives mean pass@1 of only about 0.05, so the student's description carries the task.
