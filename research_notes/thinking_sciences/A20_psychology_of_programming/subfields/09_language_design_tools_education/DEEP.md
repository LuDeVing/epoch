# Language design, tools, education: deep document

*Subfield A20.09 of the psychology of programming. Priority for our agent: Low, background only. Built from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, b08, c15, d05 ...) point to lines in the evidence files. Claim ids (K01 ... K18) are A20.09-K01 ... in claims.jsonl.*

*Honesty note: the classic core named in the brief (Shneiderman 1980, Weinberg 1971/1998, Sajaniemi 2008 review) was never opened. We hold no numbers from them. The classic language-design experiments (Stefik and Siebert 2013, Hanenberg 2010, Uesbeck 2016, Pea 1986) were paywalled and not opened. Most measured evidence below is from 2022-2026 studies of LLM code assistants in education and from agent tool design.*

## 1. What it is

This subfield asks two linked questions.

1. **Usability of languages and tools.** Does the design of a language (syntax, types, error messages) or a tool (editor, debugger, code generator, agent interface) change how well people, or models, do the task?
2. **Teaching programming.** What teaching aids help novices, and what do new tools such as code-generating AI do to learning?

The field began in the late 1970s and early 1980s. Shneiderman listed research directions (refine languages, build special-purpose languages, build better tools) at the first Empirical Studies of Programmers workshop (a11, secondary source). The ESP and PPIG workshop series followed.

Five strands matter today.

- **Language features and defects.** Does typing, syntax or language choice cause fewer bugs or faster work? Evidence is thin, observational, or not opened.
- **Teaching aids.** Example: Sajaniemi's "roles of variables", a small named vocabulary for how variables are used.
- **Error messages.** Novices meet a small set of messages very often. Making them readable is a six-decade effort (c03).
- **AI code assistants in learning and work.** The bulk of the new evidence: novices with Codex or Copilot, experts in real repositories, tutors with guardrails.
- **Agent-computer interface.** Tool design for a language-model agent treated like usability design for a human (SWE-agent).

Why it matters for our agent: only a little. Our agent is a model inside a scaffold, not a learner. The useful bits are (a) what tool and check design does for an LLM agent, (b) how prompt wording and verification change LLM code results, (c) design warnings about help that lets the user skip thinking. Everything about human learning is background.

## 2. History and theories in depth

**Founding texts (not opened, no numbers).** Weinberg's *The Psychology of Computer Programming* (1971, silver edition 1998) treats programmers as people and teams. Shneiderman's *Software Psychology* (1980) applied experimental psychology to language features and tools. Wikipedia lists both as references (a10, a12). We cite them only as the origin of the field. Sajaniemi's 2008 review (a09) could not be opened either.

**Pea (1986), language-independent conceptual bugs.** Recalled, not opened (b23). The idea: many novice bugs come from a "superbug", the assumption that the computer understands intent like a human. Syntax is not the root. This matches what we see with LLM prompts: tools read literal text, users write intent (K06, K07).

**Language usability experiments (not opened).** Stefik and Siebert 2013 (randomised novice syntax study), Hanenberg 2010 (static vs dynamic types), Uesbeck 2016 (C++ lambdas) were not read (a27, b20-b22, d14, d15). Recalled and unverified: popular syntaxes did not clearly beat a random syntax for novices; static typing showed no clear development-time benefit; lambdas did not help and experience was the strongest factor. Do not cite these as numbers.

**Roles of variables (Sajaniemi and colleagues).** A role is a stereotypic way a variable is used (a counter, a stepper, a most-recent holder). Authors say ten roles cover 99% of variables in novice-level programs; one count in the 2003 paper gives 84% for a smaller set (a01). The idea: tacit expert knowledge becomes a small shared vocabulary for novices. The 2003 experiment (a02-a05, d12) used a five-week Pascal course with three groups: traditional, roles, roles plus the PlanAni animator. Later reports (2004, 2005, 2007) are abstract-only or uncontrolled field reports (a06-a08).

**Error-message research.** "Enhanced error messages" rewrite compiler output for novices. Pritchard 2015 showed the distribution of real novice errors is heavy-tailed (a13), so a small set of rewrites covers most events. Leinonen 2023 is the newest step: use an LLM to rewrite and fix (a14, c01, c03).

**Productivity of assistants.** Two lines: controlled tasks with freelancers (Peng 2023, b10) and real-repository trials with experts (METR 2025, b08). They differ in sign (section 5).

**Learning and AI.** Kazemitabaar 2023 (b01-b03): strong gains in training, no clear later gain. Prather 2024 (b04, b05): a widening gap. Shen and Tamkin 2026 (c15, d05): a skill loss. Lehmann 2025 (c17, d08): no overall effect, usage decides.

**Agent-computer interface.** Yang et al. 2024 (SWE-agent, c21-c23, d10) borrowed human-computer-interaction principles for an LLM agent: simple actions, compact actions, informative feedback, guardrails.

**Recurring theories.**
- Dual-mode use: Barke et al. describe an acceleration mode (user knows the next step) and an exploration mode (user is unsure), linked to dual-process thinking (a24, c06).
- Illusion of competence: help makes learners feel they did better than they did (b05, d09).
- Metacognitive difficulty: students who do not monitor progress get worse with AI help (a25, b04).
- Problem-solving stages: telling novices which of six stages they are in raised performance (Loksa 2016, second-hand, b19).

## 3. Core findings with exact numbers

Status: established = 3+ independent sources agree; single-source; contested = sources disagree. All sources marked V were opened (see section 11).

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Novice error messages are heavy-tailed | Python: 640,000 error runs, 283 distinct messages, 42 seen once. Java: about 5 million events, 572 distinct, 127 once. Top Java: cannot find symbol | Pritchard 2015 (a13) | single-source (K13) |
| Roles of variables: weak exam effects | 80 students in 3 groups, 60 sat exam, 44 analysed. No significant difference on simulation, construction, non-variable questions. Only roles vs animation differed on comprehension. Fully correct comprehension grade 4.6 traditional, 5.0 roles, 4.1 animation | Kuittinen and Sajaniemi 2003 (a02, a03) | contested (K09) |
| Students adopt role vocabulary | 35% of roles group and 35% of animation group used role names in the exam; 0% of traditional | a04 | single-source |
| Codex novices, training tasks | Authoring correctness 80.1% vs 44.4% (d=1.67); time 210 s vs 361 s (d=1.56); completion 90.9% vs 79.0% (d=0.68); syntax errors 0.87 vs 1.67 per task (d=0.88); errors 1.28 vs 2.17 (d=0.74). N=69 (33 Codex, 36 baseline) | Kazemitabaar 2023 (b01, c07, a17) | single-source (K01) |
| Codex novices, later no-AI tests | Immediate post-test authoring 61.3% vs 62.9% (d=0.05); modifying 59.7% vs 59.3% (d=0.01). One-week retention authoring 59.1% vs 49.8% (d=0.28, p=.262); modifying 47.5% vs 34.8% (d=0.41, p=.092). Retention authoring errors 1.58 vs 0.99 (d=0.51, p=.042) | b02, c08, a18 | single-source (K01) |
| Codex users skip documentation | Doc access 22.1% vs 54.3% of authoring tasks (d=1.33) | b03 | single-source |
| Novices paste the task as the prompt | 32% of 1646 prompts identical to task text (b03). In a second count 66% copied the full description, 46% of prompts at task start, 92% of those with no manual attempt first (c09, a19). AI code used unmodified in 49% of tasks | b03, c09 | single-source (K07) |
| Single-prompt approach: best authoring, worst modifying | AI Single Prompt on 630 tasks, authoring M=96% (SD 16); lowest later modification scores. Learners who switched between manual and AI had better learning | a19 | single-source, observational |
| Widening gap | 21 CS1 students, 20 finished. 10 struggled, 9 of those used GenAI to reach a solution. Struggling students show illusion of competence. Original study: 11 of 31 did not finish | Prather 2024 (a25, b04, b05, d11) | established (K03) |
| Skill loss when learning a library with AI | N=52 (26 per arm). Quiz d=0.738, p=0.010, 4.15 of 27 points (17% lower). Warm-up-adjusted d=0.725, p=0.016. Task time p=0.391 (no significant gain) | Shen and Tamkin 2026 (c15, d05) | contested (K02) |
| Use pattern predicts learning (post hoc clusters) | Low: Delegation 39% (n=4), Progressive Reliance 35% (n=4), Iterative AI Debugging 24% (n=4). High: Generation-Then-Comprehension 86% (n=2), Hybrid Code-Explanation 68% (n=3), Conceptual Inquiry 65% (n=7) | d06, c16 | single-source, exploratory |
| No overall effect of LLM on learning in two pre-registered labs | Study 3: 72 enrolled, 69 analysed, 78% no prior Python. Field: 6,594 observations. Substituting trades depth for coverage; asking explanations raises understanding | Lehmann 2025 (c17, d08, d09) | contested (K02) |
| Codex explanations of compiler messages | 9 messages x 3 programs x 3 outputs. Explanation understandable 67-100%; correct 11% to 83% by message; fix correct 33% (17-56% by message); judged better than the original message 54% | Leinonen 2023 (a14, c01) | single-source (K05) |
| Prompt variant changes empty answers | Empty responses of 81: 4, 6, 7, 16, 27 for prompts 1-5 | c02 | single-source |
| Copilot on CS1 problems | 79 of 166 solved verbatim (47.6%). Of 87 unsolved, 53 (60.9%) solved after rewording; 34 stayed unsolved. 15 conceptual problems (6 concepts) failed every time | Denny 2023 (a15, c10) | established with a16, b14 (K06) |
| Student prompts weaker than expert descriptions | 80 beginners, 1,749 prompts, 48 problems. Mean pass@1 from signatures alone 0.0519. Best models about 63-65% on first-success prompts, about 7-9% on first-failure prompts, vs about 30% on HumanEval | Babe 2023 StudentEval (a16) | single-source |
| Prompt Problems deployed | Share solving: CS1 76%, 86%, 65%; CS2 75%, 96%, 99%. Successful prompts 18-47.9 words. No control group | Denny 2023 (b14, a22) | descriptive only |
| LLMs weak on code-bearing multiple choice | text-davinci-003: 77.9% text-only (134/172) vs 48.2% with code (53/110) | Savelka 2023 (a20) | single-source (K14) |
| Generated exercises | 120 exercises: 75.0% sensible, 81.8% novel, 76.7% solution matched. 84.6% had a sample solution, 89.7% of those ran, 70.8% had tests, only 30.9% of test sets passed (51 of 165). 67.2% of explanation lines correct | Sarsa 2022 (a21) | established with b16, c25 (K15) |
| Freelancer productivity | 95 developers, HTTP server in JavaScript. 71.17 vs 160.89 min = 55.8% faster (CI 21-89%, p=0.0017). Success-rate difference not significant | Peng 2023 (b10, c12) | contested (K04) |
| Expert slowdown in own repos | 16 developers, 246 tasks (136 AI-allowed, 110 not). +19% completion time. Forecast before -24%, belief after -20%. 44% had prior Cursor experience | METR 2025 (b08, c13) | contested (K04) |
| Where time goes with AI | 143 h screen recordings labelled; 74 recordings (84 h) kept. Less coding and searching; more prompting, waiting, reviewing, idle | b09 | single-source |
| Insecure code with assistant | N=47. Encryption correct 67% vs 79% (p=0.017). Signing secure 3% vs 21% (p=0.039). SQL injection vulnerable 36% vs 7% | Perry 2023 (c14) | single-source (K10) |
| Developer views of AI tools | N=410. Motives: fewer keystrokes 86%, speed 76%, recall syntax 68%. Barriers: requirements not met 54%, hard to control 48%. Acceptance 23.3-28.8% by language | Liang 2024 (a23) | single-source, self-report |
| Guardrailed tutor use | 52 enrolled, 49 analysed; about 70% used it in 4+ weeks; 7 of 49 sent over 100 queries; 71% agreed it helped. Models biased to give full solutions even when told not to; a second pass strips code | Liffiton 2023 (a26, b12, c19) | established with CodeAid (K12) |
| CodeAid deployment | About 700 students, 8,000+ interactions, 563 survey responses, 22 interviews | Kazemitabaar 2024 (c20) | single-source |
| Language vs defects reanalysis | Original: 729 projects, 17 languages, 566k bug-fix commits. Reanalysis: 148 more projects, 27,450 duplicate commits (1.86%) removed, bug-label false positive 36%, false negative 11%. Significant languages 11 down to 4 | Berger 2019 (b06, b07) | single-source (K08) |
| Type-constrained decoding | TypeScript, 2B-34B open models. Compile errors cut 75.3% (HumanEval) and 52.1% (MBPP); syntax-only cut 9.0% and 4.9%. Functional correctness +3.5% to +5.5% relative. Repair +37% relative on average; Gemma 2 2B repaired only 33.5% and 25.8% unaided | Mundler 2025 (d01, d02) | single-source (K16) |
| Static typing of the target language | Codex, 19 languages: typed effect p=0.34 (HumanEval), p=0.23 (MBPP). Removing Python annotations p=0.23. TypeScript types set to Any: -2.5% pass@1 (p<0.001). Skipping the type-check: p=0.14 | Cassano 2022 MultiPL-E (d03, d04) | single-source (K17) |
| Agent interface ablations | SWE-bench Lite, GPT-4 Turbo, full design 18.0%. No edit action 10.3 (-7.7). No linting 15.0 (-3.0). Search: summarized 18.0, none 15.7, iterative 12.0. Viewer: 100 lines 18.0, 30 lines 14.3, full file 12.7. Context: last 5 observations 18.0, full history 15.0. Agent recovered 104 of 135 edit failures | Yang 2024 (c21, c22, d10) | single-source (K11, K18) |
| Think-aloud patterns | 13 participants backtracked at least once; shepherding and backtracking found. Large suggestions overload novices | Prather 2023 (c04, c05) | single-source, qualitative |

## 4. Mechanisms and models

Described so an engineer could implement or test them.

**4.1 Delegation versus comprehension (learning-loss model).** A user who hands the whole task to the generator skips the effortful steps that build memory: forming a plan, reading documentation, debugging. Evidence: documentation use fell from 54.3% to 22.1% (b03); the single-prompt approach had top authoring and worst later modifying (a19); delegation and iterative AI debugging clusters scored 39% and 24% (d06). The protective pattern asks for concepts or explanations before or with code. For the agent this is not learning; it is a proxy for whether the agent restates the problem and checks understanding before generating (S1). Engineer's version: log per run the count of "explain" calls versus "write code" calls, and compare accuracy on held-out variants.

**4.2 Prompt-wording sensitivity.** Same model, same task, different wording: 47.6% vs about 60% of the rest solved (a15); empty-answer rate 4 to 27 of 81 across five prompts (c02); beginner prompts far below expert descriptions (a16). Implementation: a reformulation step that rewrites the problem (plain language, one concept per sentence, explicit input and output), run only after a failed check. Some conceptual problems fail whatever the wording (15 problems, 6 concepts, c10). Reformulation helps with verbose or unclear statements; it does not fix a missing capability.

**4.3 Verify the model's reading of an error.** Codex gave a comprehensible explanation 67-100% of the time but a correct fix only 33% (c01). The failure is correctness, not fluency. Implementation: do not accept the explanation; apply the proposed fix, rerun, read the new output. This follows G2. A small open model repaired only 33.5% and 25.8% of non-compiling programs unaided (d02).

**4.4 Hard check inside the loop.** Type-constrained decoding allows only well-typed prefixes. Compile errors fall by half or more; correctness rises only 3.5-5.5% relative. Gains are largest for small models and for repair. It needs decoder access. For an API-only agent the nearest equivalent is: compile or type-check every candidate and feed the located error back (S4 then S5). Syntax-only constraining barely helps because syntax errors are only about 6% of TypeScript compile errors (d01).

**4.5 Agent-computer interface.** Four principles (c21): simple actions with few options; compact actions that combine steps; informative feedback after every action; guardrails that block bad actions (a lint check that rejects an edit that breaks syntax). Ablation sizes: edit action -7.7, linting -3.0, search style -6.0, viewer size -3.7 to -5.3 (c22, d10). Implementation for our tools: (a) every tool returns a short structured result, never silence; (b) lint or compile guardrail on write actions; (c) summarised search; (d) a 100-line window rather than a full-file dump. Limits: not at equal tokens, one run per cell, one model, effects may not add.

**4.6 Guardrails enforced outside the generator.** Models give full solutions even when told not to. CodeHelp used a sufficiency check on the question, a main answer, then a second LLM pass that strips code blocks (c19). Implementation: when the agent must not output X, add a regex or classifier check on the output and regenerate or strip on failure. Fits G5 (code selects).

**4.7 Named vocabulary (roles of variables).** A small shared set of names for recurring state uses. Students used role names unprompted (35%) but exam gains were not significant (a03, a04). Idea for memory: tag scratchpad entries with a few fixed roles ("candidate", "check result", "constraint", "lesson"). A hypothesis, not an established effect (K09).

**4.8 Gap-widening.** Stronger users gain more from AI help; weaker users over-rely (b04, b05, c17, d09). Analysis rule: always report scaffold gain by item difficulty, not only the mean.

## 5. What holds up

**Holds up (several independent sources).**
- AI help widens the gap between strong and weak learners (K03): Prather 2024 (small replication), Lehmann 2025, Kazemitabaar subgroup, Peng 2023 interactions. Caveat: subgroup splits are post hoc and small.
- Prompt wording decides success on code tasks (K06): Denny 2023, StudentEval, Leinonen prompt variants, Prompt Problems deployment.
- Tutors told not to give solutions still do unless filtered (K12): CodeHelp, CodeAid.
- Generated artifacts are often usable but fail checks (K15): only 30.9% of generated test sets passed.

**Contested.**
- Productivity (K04). Peng: 55.8% faster (freelancers, new task). METR: 19% slower (experts, own repos, early-2025 tools). Not a true contradiction: task type, expertise and tool differ. Both groups mis-forecast their own speed (Peng: both guessed 35% gain; METR: forecast 24% faster, observed 19% slower). No METR follow-up on the blog listing (d13); absence on one page is not proof.
- Skill loss (K02). Shen and Tamkin d=0.738; Lehmann no overall effect; Kazemitabaar no immediate effect and a weak retention trend favouring Codex. Designs differ (ages, tasks, tools, no-AI tests). Usage pattern may decide, but the clusters are small (n=2 to 7) and observational.
- Roles of variables (K09). Mostly null on exams. Only roles vs animation differed. No outside replication found.

**Failed or weakened results.**
- Berger 2019 reanalysis of language vs defects: significant languages 11 down to 4, effects tiny, bug labels 36% false positive. Many citing authors restated an association as a cause (b07).
- Static typing: no overall effect on Codex pass@1 (p=0.34, p=0.23); small effect when TypeScript types are weakened (-2.5%).
- Kazemitabaar immediate transfer: null (d=0.05 and 0.01).

**Moderators.** Prior skill (high-prior learners gained more: b02, c08, d09). Usage pattern (explanation-seeking vs delegating: d06, c17). Task (new greenfield vs mature repo: K04). Model size (small models gain most from type constraints: d02). Error message type (explanation correct 11% to 83%: c01).

**Interventions that worked.** Reword the prompt (about 60% of unsolved CS1 problems rescued). Hard checks in a loop (type constraints, linting guardrail). Compact, feedback-rich agent tools. A separate code-stripping pass for tutors. Explanation-first use (post hoc only).

**Not shown to work.** Roles of variables on exam scores. Syntax-only constrained decoding (9.0% and 4.9% fewer compile errors). Instruction-only "do not give the solution". Trusting self-report: developers over-predicted speedup.

**Methodological limits.** N of 20 to 69 is common; attrition is heavy (90 to 69 in Kazemitabaar; 80 to 44 in the roles experiment); Codex-era models dominate; most claims are single-source.

## 6. Language models

**Novice-level tasks (2022-2023 models).**
- Codex explaining error messages: understandable 67-100%, correct 11% to 83%, fix correct 33% (c01). Prompt choice moved empty answers from 4 to 27 of 81 (c02).
- Copilot on 166 CS1 problems: 47.6% solved verbatim; rewording rescued 60.9% of the unsolved; conceptual problems failed every time (c10).
- StudentEval: from signatures alone mean pass@1 0.0519; student prompts that fail first give 7-9% for the best models. Under 3% of successful prompts were unreliable for large models, nearly 10% for small (a16).
- Codex scored about 78% on two CS1 exams (15.7/20, 19.5/25) and beat almost 80% of students on exam questions (b15, b16, second-hand).
- Code-bearing multiple choice: 48.2% vs 77.9% text-only (davinci-003, a20).
- Generated exercises: 75-82% sensible and novel; only 30.9% of generated test sets passed (a21).

**Language design.**
- Codex across 19 languages: language frequency in training data tracks accuracy; static typing has no overall effect (d03). Dropping Python annotations: no effect; weakening TypeScript types: -2.5% (d04).
- Type-constrained decoding on 2B-34B open models: compile errors -75.3% and -52.1%, correctness +3.5 to +5.5% relative, repair +37% relative (d01, d02).
- No frontier 2025-26 data on syntax or type effects. A gap.

**Agent tool design.** SWE-agent interface and per-part ablations are in section 3. The agent recovered from 104 of 135 edit failures thanks to lint feedback (c22). Tool details moved results by 3 to 8 points; not measured at equal tokens (d10).

**Guardrails.** Models lean toward full solutions even when told not to; a second pass is needed (c19). No 2025-26 leak-rate data found (d17).

**People using the models.** Training correctness 80.1% vs 44.4% with Codex (b01); no immediate later effect; quiz 17% lower with AI for a new library (d05); security 67% vs 79% correct (c14). Usage pattern moderates.

**Missing.** Newer models (2025-26) on error-message repair, guardrail leaks and language-design effects; larger-N replication of Kazemitabaar and Shen-Tamkin. The gap search hit rate limits, so this is a search failure, not evidence of absence (d17).

## 7. What our agent should take

The brief says background only. Nothing here is large. Parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Enforce "do not output X" with an external check (regex or second pass), not only an instruction | G5 (code selects) | [E] | c19, c20, a26, b12, b13 (K12) |
| Verify generated artifacts (tests, exercises) by running them, not by accepting them | G3 / S4 | [E] | a21, b16, c25 (K15) |
| Report scaffold gain split by item difficulty or class, not only the mean | G7, S9 log | [E] | b04, b05, c17, d09, a25 (K03) |
| Reformulate only after a failed check; do not loop on reformulation for conceptual failures, escalate to O3 or O1 | O8 / S5 | [E] | a15, c10, a16, b14 (K06) |

Note on the last item: S1 and O8 already cover restating. The new part is a measured boundary: rewording rescued about 60% of verbatim failures, and some conceptual problems fail whatever the wording.

### Test first (not established; see section 8 and UNKNOWNS.md)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Apply the proposed fix and rerun instead of trusting the model's explanation of an error | G2 / S5 | [S] | a14, c01, d02 (K05) |
| Compile or type-check gate inside the repair loop | G3 / S4 | [S] | d01, d02 (K16) |
| Tool interface: structured feedback, lint guardrail on writes, summarised search, 100-line viewer | S4/S5 tools | [S] | c21, c22, d10 (K11, K18) |
| Explain-first versus delegate-first on unfamiliar APIs | S1 / G | [C] | c15, d05, d06, c17 (K02) |
| Small fixed vocabulary of scratchpad roles | memory | [C] | a01, a03, a04, d12 (K09) |
| Restate before generating, do not echo the task text | S1 | [S] | b03, c09 (K07) |
| Independent security-check pass on generated code | G / S8 | [S] | c14 (K10) |
| Report scaffold effect by task familiarity | G7 | [C] | b08, b10 (K04) |

## 8. Concrete tests on our bench

All arms get equal tokens, setup and verification calls counted (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Verified fix vs trusted explanation | Code tasks with a failing run and an error message | A: model explains error and fix, accepted. B: fix applied, rerun, new output fed back (S5) | Fraction fixed after one round | B beats A. Prior: 33% correct-fix rate in 2022 (c01). Expect B +10 points on small or older models, less on frontier |
| T2 Compile or type gate | Code generation in a typed language (TypeScript) | A: plain. B: generate, compile, one repair round with located error | Compile-error rate; pass@1 | Compile errors down a third or more; pass@1 up a few percent (constrained decoding gave +3.5 to +5.5% relative; a prompt-level gate is weaker) |
| T3 Reformulation after a fail | CS1-style problems, tagged verbose vs conceptual | A: retry same prompt. B: plain-language restatement, then retry | Solve rate on first-failed items | B higher on verbose; no gain on conceptual (a15, c10) |
| T4 Interface ablation | Repository bug-fix tasks | Full tool set vs no lint guardrail vs no summarised search, same token cap | Resolve rate | Lint about +3 points, search style about +6, if SWE-agent effects hold at equal tokens |
| T5 Explain-first vs delegate | Tasks on an unfamiliar library | A: write code directly. B: concept summary, then code, then check | Held-out variant pass rate | B >= A at equal tokens. Not established; clusters were post hoc |
| T6 External filter | Hint-mode items where the final answer is withheld | A: instruction only. B: instruction plus answer filter | Leak rate | B near 0; A leaks (c19). Low priority for our single-answer bench |
| T7 Role vocabulary | Multi-step tasks with scratchpad | A: free notes. B: notes tagged with 4-6 fixed roles | Accuracy, tokens | Small or null (a03). Run only if cheap |
| T8 Security pass | Code tasks with a weak spot (crypto, SQL) | A: plain. B: plain plus independent check | Insecure-output rate | B lower; human gap was 67% vs 79% correct |
| T9 Strata report | Any bench run | Split gain by item difficulty and by familiar vs novel class | Gain per stratum | Larger gain on easy items if gap-widening transfers (K03) |

## 9. What does not transfer, and why

- **Human learning outcomes.** Skill loss, retention, illusion of competence and the widening gap describe people. Our agent has no practice memory. The only transferable piece is a proxy: skipping a restate-and-understand step may lower accuracy on variants.
- **Roles of variables as teaching.** The effect was on student exams. The only analogue is a scratchpad tag vocabulary, which is a guess.
- **Developer productivity (Peng, METR).** Time-to-finish for people. We measure accuracy at equal tokens. The one lesson: self-forecasts are unreliable, so trust measured runs, never the agent's own claims (G10).
- **Self-reported usability (Liang 2024, CodeHelp surveys).** Human attitudes.
- **Tutor deployments.** Usage counts with no learning outcome versus a control.
- **Type-constrained decoding.** Needs decoder access; API-only agents can only imitate it with compile gates.
- **Language-versus-defects repository studies.** Observational and noisy (Berger 2019). We do not choose a language by this.
- **Classic usability experiments (syntax, typing).** Human novices, small student samples, not opened.
- **Codex-era numbers.** Davinci-003 and Codex are far weaker than 2025-26 models. Use direction, not size.

## 10. Open questions

1. Exact effect sizes in Stefik and Siebert 2013, Hanenberg 2010, Uesbeck 2016; did any replicate?
2. Does the Kazemitabaar null immediate transfer replicate with 2025-26 models and larger N? (Lehmann 2025, N=69, 2024 models, agrees on a null overall effect.)
3. Does the Shen and Tamkin skill loss replicate, and does an explain-first scaffold remove it? Only post hoc clusters exist.
4. Do Weinberg 1971/1998 and Shneiderman 1980 contain citable empirical numbers?
5. Do 2025-26 models still fail at compiler-message repair (33% in 2022) or at conceptual prompt classes?
6. Was roles of variables replicated outside the Finnish group, with effect sizes?
7. How does language choice (typed vs untyped, syntax) change frontier LLM accuracy?
8. Does the METR slowdown persist with later tools?
9. Which interface features matter most at equal tokens?
10. Do guardrail leaks fall with 2025-26 models?

## 11. Sources

[V] opened and read this session. [M] snippet, second-hand or recalled only.

- [V] Kuittinen and Sajaniemi (2003) First results of an experiment on using roles of variables in teaching. https://ppig.org/files/2003-PPIG-15th-kuittinen.pdf and https://www.ppig.org/papers/2003-ppig-15th-kuittinen/ (a01-a05, d12)
- [V, abstract only] Kuittinen and Sajaniemi (2004). https://saja.kapsi.fi/var_roles/abstracts/iticse04_kuit_saja.html (a06)
- [V, abstract only] Sajaniemi and Kuittinen (2005). https://saja.kapsi.fi/var_roles/abstracts/cse05.html (a07)
- [V, summary only] Nikula, Sajaniemi, Tedre and Wray (2007). https://saja.kapsi.fi/var_roles/abstracts/jite07.html (a08)
- [M] Sajaniemi (2008) Psychology of programming: looking into programmers' heads. https://humantechnology.jyu.fi/archive/vol4/issue1/psychology-of-programming-looking-into-programmers-heads (a09)
- [M] Weinberg (1971, 1998); Shneiderman (1980). Via https://en.wikipedia.org/wiki/Psychology_of_programming (a10, a12, d16)
- [V] Wikipedia, Psychology of programming (a11). https://en.wikipedia.org/wiki/Psychology_of_programming
- [V] Pritchard (2015) Frequency distribution of error messages. https://arxiv.org/pdf/1509.07238 (a13)
- [V] Leinonen et al. (2023) Using LLMs to enhance programming error messages. https://arxiv.org/abs/2210.11630 (a14, c01-c03)
- [V] Denny, Kumar and Giacaman (2023) Conversing with Copilot. https://arxiv.org/abs/2210.15157 (a15, c10)
- [V] Babe et al. (2023) StudentEval. https://arxiv.org/abs/2306.04556 (a16)
- [V] Kazemitabaar et al. (2023) Studying the effect of AI code generators on supporting novice learners. https://arxiv.org/abs/2302.07427 (a17, a18, b01-b03, c07, c08)
- [V] Kazemitabaar et al. (2023) How novices use LLM-based code generators. https://arxiv.org/abs/2309.14049 (a19, c09)
- [V] Savelka et al. (2023) GPT struggles with multiple-choice questions about code. https://arxiv.org/abs/2303.08033 (a20)
- [V] Sarsa et al. (2022) Automatic generation of programming exercises and code explanations. https://arxiv.org/abs/2206.11861 (a21, c25)
- [V] Denny et al. (2023) Promptly and Prompt Problems. https://arxiv.org/abs/2307.16364 and https://arxiv.org/abs/2311.05943 (a22, b14)
- [V] Liang, Yang and Myers (2024) Usability of AI programming assistants. https://arxiv.org/abs/2303.17125 (a23)
- [V] Barke, James and Polikarpova (2023) Grounded Copilot. https://arxiv.org/abs/2206.15000 (a24, c06)
- [V] Prather et al. (2024) The Widening Gap. https://arxiv.org/abs/2405.17739 (a25, b04, b05, b25, c18, d11)
- [V] Prather et al. (2023) "It's weird that it knows what I want". https://arxiv.org/abs/2304.02491 (c04, c05)
- [V] Liffiton et al. (2023) CodeHelp. https://arxiv.org/abs/2308.06921 (a26, b12, b13, c19)
- [V] Kazemitabaar et al. (2024) CodeAid. https://arxiv.org/abs/2401.11314 (c20)
- [V] Berger et al. (2019) On the impact of programming languages on code quality. https://arxiv.org/abs/1901.10220 (b06, b07)
- [V] Becker et al. / METR (2025) Early-2025 AI and experienced open-source developers. https://arxiv.org/abs/2507.09089 (b08, b09, c13)
- [V] Peng et al. (2023) Impact of AI on developer productivity. https://arxiv.org/abs/2302.06590 (b10, b11, c12)
- [V] Perry et al. (2023) Do users write more insecure code with AI assistants. https://arxiv.org/abs/2211.03622 (c14)
- [V] Shen and Tamkin (2026) How AI impacts skill formation. https://arxiv.org/abs/2601.20245 (c15, c16, d05-d07)
- [V] Lehmann, Cornelius and Sting (2025) AI meets the classroom. https://arxiv.org/abs/2409.09047 (c17, d08, d09)
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/abs/2405.15793 (c21-c23, d10)
- [V] Mundler et al. (2025) Type-constrained code generation. https://arxiv.org/abs/2504.09246 (d01, d02)
- [V] Cassano et al. MultiPL-E. https://arxiv.org/abs/2208.08227 (d03, d04)
- [V] METR blog listing. https://metr.org/blog/ (d13)
- [V, reviews] Becker et al. (2022/2023) Programming is hard or at least it used to be. https://arxiv.org/abs/2212.01020 (b15, c11); Denny et al. (2023) Computing education in the era of generative AI. https://arxiv.org/abs/2306.02608 (b16); Sarkar et al. (2022) What is it like to program with AI. https://arxiv.org/abs/2208.06213 (b17)
- [M] Margulieux et al. (2024) and Loksa et al. (2016), via Prather 2024 (b18, b19). Finnie-Ansley et al. (2022) https://dl.acm.org/doi/10.1145/3511861.3511863 (c24). Prather et al. (2023) The robots are here https://arxiv.org/abs/2310.00658 (c26).
- [M] Stefik and Siebert (2013) https://doi.org/10.1145/2534973; Hanenberg (2010) https://doi.org/10.1145/1932682.1869462; Uesbeck et al. (2016) https://doi.org/10.1145/2884781.2884849; Pea (1986) https://doi.org/10.2190/689T-1R2A-X4W4-29J2 (a27, b20-b23, d14, d15; not opened; recalled summaries unverified)
- [M] Sajaniemi roles literature, Aalto repository. https://aaltodoc.aalto.fi/handle/123456789/3534 (b24)

Links to subfields researched in parallel (not covered here): Novices and education; Expert-novice differences; Debiasing; Verbal confidence; Heuristics and biases; Research methods.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 4 established claims: 3 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A20.09-K15** (reworded: the sources support less). Sarsa et al. report 75.0% sensible and 81.8% novel, but 30.9% is 51 of 165 exercises that had both a sample solution and tests whose solution passed the tests (not 30.9% of all generated test sets); the second source (Denny review, same group) mislabels 30.9% as statement coverage and cannot be counted as independent. Corrected claim: In a Codex study of 240 generated CS1 exercises, 75.0% were rated sensible and 81.8% novel, but only 30.9% (51 of 165) of the exercises that had both a sample solution and automated tests had a sample solution that passed those tests.
