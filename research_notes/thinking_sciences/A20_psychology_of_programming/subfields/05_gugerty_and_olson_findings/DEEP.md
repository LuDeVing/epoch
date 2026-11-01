# Gugerty and Olson findings: deep document

*Subfield A20.05. Status of the base paper: only the abstract and second-hand accounts were read. The full text of Gugerty and Olson 1986 was blocked (ACM 403, Academia 403). Every number about their sample below is marked unverified. Evidence ids (a01 to d20) and claim ids (A20.05-K01 to K26) refer to evidence_a-d.jsonl and claims.jsonl in this folder.*

## 1. What it is

Gugerty and Olson (1986), "Debugging by skilled and novice programmers", CHI '86, pp. 171-174. Two experiments. Experiment 1 used LOGO programs. Experiment 2 used Pascal programs. The programs were given to the subject and run on a microcomputer. [a01, b01]

The abstract says three things. [a02, a03, a04]
1. Experts debugged faster and more accurately than novices.
2. Experts did this because they made high-quality hypotheses after studying the code less than novices did.
3. Novices often added new bugs while looking for the original one.

The authors add a hedge. For these simple programs, the experts' edge came mainly from better program comprehension, not from a different debugging procedure. [b02]

Secondary snippets (unverified) say the first group was 18 experts and 6 novices, 3 programs, 1 seeded bug. [a06] Treat these figures as a guess until the paper is read.

Why this matters to our agent. The paper is the standard human anchor for two ideas:
- A good first hypothesis beats more reading.
- Edits made while hunting a bug can add bugs, so edits should be limited and the best state kept.

Our schema already has the second idea (S5: keep best-so-far, at most 2 rounds; G6: submit best attempt). This document asks how much human and LLM evidence supports each part, and what is still a guess.

Important limit. The core paper is four pages, has 4 references in Crossref and is cited 15 times by DOI (a05). The famous result is small and old. Most of the support here comes from later work, mostly on LLMs, and is related to the paper by analogy.

## 2. History and theories in depth

**Before 1986.** Gould (1975) gave an early ideal process model of debugging. Jeffries' conference papers on program debugging are two of the four references of the CHI paper. [a05, a10]

**Gugerty and Olson's model (as restated by Kinnunen 2007).** A cycle: read the description and code, form a hypothesis about the bug and the program's purpose, test it (edit, run, or check against the description), and go back to reading if no bug is found. Experts and novices follow the same cycle. Novices are slower, rarely find the bug on the first try, and add new bugs while testing hypotheses. [a07, a08, b03, d02]

**Vessey (1985).** The closest human companion study. Verbal protocols of 16 practising programmers, 8 expert and 8 novice, classed by chunking ability. Experts built a causal model of the whole system early ("system thinking") and searched breadth-first. Novices did not. [b04, b06]

**Katz and Anderson (1987).** Follow-up on bug-location strategies, HCI 3(4) 351-399. Cited 143 times. Only metadata was read. It is not a long version of Gugerty and Olson. [a12, b09, d03]

**Later reviews.** McCauley et al. (2008) review debugging research to 2008, including expert-novice differences, and conclude debugging must be taught. [a10, a13] Spoerer and Michaeli (2025) scoped 36 papers on student debugging; most used qualitative analysis of screen recordings, and they cite Gilmore (1991) for a comprehension-centred model. [a09, a10]

**Competing explanations of the expert edge.**
- Comprehension (Gugerty and Olson): experts understand the program better, so hypotheses are better.
- System model and breadth-first search (Vessey): experts hold a whole-system causal model.
- Chunking (Vessey): experts see larger units. Davies (2000) found experts pull out object-oriented program information faster and more accurately from brief views (N=32, 16 and 16). [b08]
- Strategy does not matter much (Ko and Uttl 2003): no reading strategy gave best debugging in 75 novices. [b07]

**Move to LLMs (2023 to 2026).** The same questions appear as: does the model diagnose well (hypothesis quality), does it break things when it edits (new bugs), does it improve over repeated attempts. The LLM work says diagnosis is the bottleneck and extra rounds decay. [a14, a15, a22]

## 3. Core findings with exact numbers

Status: "checked" means the number was re-opened in critique.md. "U" means unverified or abstract-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts debug faster and more accurately, with better hypotheses after less reading | Direction only. Sample 18 experts, 6 novices, 3 programs, 1 bug is from snippets | Gugerty and Olson 1986 [a02, a06] | Direction from abstract; magnitudes U |
| Novices add new bugs while hunting the original | "Frequently"; no count | G&O 1986 [a03] | U (abstract word only) |
| Expert-novice debug time (chunking classification) | Experts 15 min 40 s vs novices 28 min 3 s, N=16 | Vessey 1985 [b04] | checked |
| Same, by manager rating | 20 min 24 s vs 23 min 19 s | Vessey 1985 [b04] | checked |
| Variance in debug time explained | 73.7% by chunking class together with bug level; 36.1% by manager rating | Vessey 1985 [b04, critique] | checked (corrected: not classification alone) |
| Error makers | All 5 programmers with incorrect repairs were chunk-class novices; 8 mistakes, 6 on the low-level bug; manager rating classed 4 of 5 as novices | Vessey 1985 [b05] | checked, but circular (novices defined by chunking seen in the same protocols) |
| Episodes needed | Novice > expert, P=0.003; time per episode no difference | Vessey 1985 [b06] | checked |
| No reading strategy best | 75 novices, 4 bugs. Bugs fixed: depth-first 1.00 (SD 0.97), others 1.65 (0.98) and 2.00 (1.07). Experience means 2.52, 1.20, 3.59 | Ko and Uttl 2003 [b07] | checked; experience confounded |
| LLM self-correction without outside signal hurts | GPT-3.5 CSQA 75.8 -> 38.1 -> 41.8; GSM8K 75.9 -> 75.1 -> 74.7; HotpotQA 26.0 -> 25.0 -> 25.0. GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; CSQA 82.0 -> 79.5 -> 80.0; HotpotQA 49 -> 49 -> 43. 74.7% of GPT-3.5 GSM8K answers unchanged | Huang et al. 2024 [a17, a19, c07] | checked, established (5 sources) |
| Oracle labels inflate gains | GPT-3.5 GSM8K 75.9 -> 84.3; CSQA 75.8 -> 89.7. GPT-4 GSM8K 95.5 -> 97.5, HotpotQA 49 -> 59 | Huang et al. 2024 [a18] | read from extracted table |
| Human feedback beats GPT-4 feedback for repair | Overall 52.60 vs 33.30%. Intro 62.21 vs 42.64; interview 45.67 vs 19.33; competition 14.67 vs 3.67. 16 participants, 40 failing programs, 25 repairs per feedback | Olausson et al. 2024 [a15, b12, c03] | checked, established |
| Self-repair vs resampling at equal budget | GPT-4 APPS: 10 initial + 1 repair = 1.05x of pass@20; 2 initial + 10 repairs = 0.97x of pass@22. Heat-map range about 0.92 to 1.11. More initial samples always helped | Olausson et al. 2024 [a14, b10, b11, c01] | checked, established |
| Finding the mistake is the weak step | BIG-Bench Mistake, 2186 traces. GPT-4 mistake finding 52.87 (direct step prompt; 39.80 and 43.40 for other prompts). GPT-3.5 10.10 and 19.00 on some tasks | Tyen et al. 2024 [a20, b18] | checked |
| Redo at the wrong place breaks good traces | Word sorting: 11.11% of correct traces broken. Shuffled objects: base 50% -> 68.6%; base 99% -> 92.8%. Locator helps once its accuracy is about 60-70% | Tyen et al. 2024 [b19, b20] | checked; locator threshold approximate |
| Execution feedback is what makes self-debug work | Up to +12 (TransCoder, MBPP with unit tests). Spider +2-3, hardest +9. MBPP Codex 61.4 -> 57.6 with simple feedback, 64.4 with explanation, 66.2 with trace. GPT-3.5 67.6 -> 69.2; GPT-4 72.8 -> 76.4 | Chen et al. 2024 [a28, b14, c04, c05] | established |
| Self-Refine: gain falls with model strength | Average +20% overall. Code optimisation: GPT-4 92.9 -> 93.1; ChatGPT 14.8 -> 23.0 | Madaan et al. 2023 [c12] | single-source |
| Reflexion with real test feedback | HumanEval pass@1 91.0 vs 80.1 (GPT-4) | Shinn et al. 2023 [b25, c13] | single-source |
| Debugging decay | Most of 18 models lose 60-80% of effectiveness in 2-3 attempts (HumanEval). Prior work cited: 15 more attempts gave only 2.4% extra | Adnan and Kuhn 2025 [a22, b16, c18] | single-source; small open models |
| Fresh start at decay point | llama3.1:8b 72.56 -> 82.82; deepseek-coder-v2:16b 84.1 -> 92.1; Mistral-Instruct 54.3 -> 62.8 / 57.3. Claude-3.7-Sonnet hit 100% in two attempts, so no test | Adnan and Kuhn 2025 [a23, c19] | checked, single-source |
| Edit linter guard | With lint 18.0% vs 15.0% without; no edit command 10.3% (SWE-bench Lite). Viewer 30 lines 14.3, 100 lines 18.0, whole file 12.7 | SWE-agent [a24, c14] | checked, single-source |
| Failed edits are common and compound | 1185 of 2294 (51.7%) trajectories had 1+ failed edit; median 3, max 33. Recovery 90.5% from any attempt, 57.2% after one failed edit. 12.47% full (286/2294), 18.00% Lite (54/300) | SWE-agent [a25, c14] | checked |
| Less history is as good | Last 5 observations 18.0 vs full history 15.0. Summarised search 18.0 vs iterative 12.0 vs none 15.7. 93.0% of resolved submitted before cost limit | SWE-agent [c15] | single-source |
| Fixed pipeline competitive | Agentless 32.00% (96/300) at $0.70. Majority vote 77 (25.67%); + regression tests 81 (27.00%); + reproduction tests 96 (32.00%). Cost $0.00, $0.01, $0.25 | Xia et al. 2024 [a26, b24, c16, c17] | checked (best open-source, not top overall on Lite) |
| More bugs, lower pass rate | GPT-4 DebugBench: missing colons 93.6, condition 73.1, double bugs 70.7, triple 58.9, quadruple 55.9. Overall GPT-4 75.0, GPT-3.5 62.1. 4,253 instances | Tian et al. 2024 [a27, c23] | single-source |
| Runtime feedback helps syntax, not logic | Figure values not extracted | Tian et al. 2024 [c24] | single-source |
| LLM code review finds issues and invents issues | GPT-3.5 at least one real issue 90%, all issues 57%, non-existent issues 40%. Codex 70% / 13% / 40% | Hellas et al. 2023 [c21] | single-source |
| Blind spot for own errors | 14 open non-reasoning models average 64.5%; Claude 3.5 Haiku 52.5%, Sonnet 4 41.4%; "Wait" cuts it 89.3% | Tsui 2025 [d04, d05] | single-source |
| "Wait" cue vs reasoning sibling | DeepSeek-V3 0.567 / 0.902 with Wait / R1 0.908; phi-4 0.325 / 0.701 / 0.707; Qwen3-14B 0.117 / 0.868 / 0.843 | Tsui 2025 [d05] | single-source |
| Reasoning models still overturn correct answers | Yes/No QA: o1-mini 62.5 after revision, drop 12.1, 34.0% of correct answers overturned; o1-preview 74.1, drop 4.2, 15.6% | Zhang et al. 2025 [d06] | single-source, late-2024 models |
| Read-all scan is affordable | Scan averages 2.94M tokens per problem, under 15% of cost; kept context 74,570 tokens (50.5x cut); 92.6% of instances have needed files in 128k | CodeMonkeys 2025 [d07] | single-source |
| Serial vs parallel compute; selection | Coverage 69.8% (10 state machines x 8 iterations), frontier flat across splits. Oracle selection 69.8%, random 45.8%, their selector 57.4% (about 2300 USD) | CodeMonkeys [d08, d09] | single-source |
| Localization tracks resolution | Six systems rank the same by file F1 and by resolved count (one exception). Best system 255/500 (51%), localized a buggy file in 448 cases, all buggy files in 394. Lowest localized 342 | Meng et al. 2025 [d10] | single-source (same benchmark as d13) |
| Passing tests overstates fix quality | 7.8% of plausible patches fail full developer tests; 29.6% (260 of 877) differ from gold; 11 of 22 confirmed-incorrect patches regressive (50.0%); 11 of 22 not caught by developer tests. UTBoost: 36 under-tested instances, 345 wrong patches accepted | Wang, Pradel and Liu 2026; Yu et al. 2025 [d11, d12, d18] | single-source in effect (same benchmark) |
| Failure taxonomy | 150 failed instances, 3 phases, 9 categories, 25 subcategories. OpenHands 53.0%, Agentless 50.8%, Tools Claude 49.0%. 51.3% of Agentless failures contain a localization error. Agents mostly loop on a failed strategy | Liu et al. 2025 [d13] | single-source |
| Same-model reviewer | Rescued 24 of 108 failed tasks (22.2%); no matched-compute control | Liu et al. 2025 [d14] | single-source |
| Block-level runtime state | HumanEval GPT-3.5: 73.8 baseline, Self-Debug 81.1 (+7.3), LDB 82.9 (+9.1) | Zhong et al. 2024 [d15] | single-source |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

**M1. Hypothesis-test cycle (Gugerty and Olson).** State machine: READ -> HYPOTHESISE -> TEST (edit, run, or check spec) -> if no bug found, back to READ. Experts and novices share it. The difference is the quality of the hypothesis at the HYPOTHESISE step, and the number of loops. For an agent: log each loop, and record the hypothesis text and the test result. Loop count and a ranked hypothesis list per round are the measurable variables.

**M2. Comprehension before edit (Vessey, system thinking).** Experts build a causal model of the whole system first, then search breadth-first. Implementation: before the first edit, require a short system summary (inputs, outputs, key functions, data flow) and a ranked list of candidate fault locations. Compare to no summary. This is claim K03, single-source for humans, untested for LLMs.

**M3. Edits add bugs.** Human version: novices test hypotheses by editing and introduce new bugs. LLM version: 11 of 22 confirmed-incorrect plausible patches were regressive [d12]. 51.7% of agent trajectories had a failed edit and recovery fell from 90.5% to 57.2% after one [a25]. Controls:
1. Guard: reject an edit that breaks syntax or a check before it enters the working state (SWE-agent linter, 18.0 vs 15.0).
2. Keep best-so-far: store the state with the best check score; revert to it when a new edit scores lower.
3. Edit cap: at most N edits per round (schema S5 already caps at 2 rounds).
4. Regression check: run pass-to-pass tests, not only the target test (d11: 7.8% fail the full suite).
Items 2 and 3 have no direct controlled test in the sources. Only the guard (1) and the regression problem (4) are measured.

**M4. Self-correction needs an outside signal.** Rule: a revision is allowed only if it cites output produced by code (failing test, error, trace). Why: the model cannot judge its own reasoning well (Huang), and mistake finding is the weak step (Tyen 52.87). Block-level traces improve feedback quality (LDB +9.1 vs Self-Debug +7.3).

**M5. Diagnosis vs repair split.** Olausson: feedback quality is the bottleneck. A stronger model or a human writing the diagnosis raised repair (33.30 -> 52.60). Implementation: a separate DIAGNOSE call that outputs a located, evidenced explanation; a REPAIR call that sees it. Give DIAGNOSE the larger budget. Untested at equal tokens against joint repair.

**M6. Budget: resample vs repair.** At equal total tokens, more initial samples beat more repair rounds (1.05x vs 0.97x; more initial samples always helped). Implementation: for a fixed budget B, compare N fresh candidates against k repair rounds on fewer candidates.

**M7. Decay and fresh start.** Effectiveness follows an exponential curve over attempts: E(n) = E0 * exp(-lambda * n). The paper picks a restart point where the fitted curve crosses a threshold. Implementation: after 2 failed rounds, discard the conversation and restart with the problem plus best-so-far. Only small open models were tested. The reasoning model started lower (59.1 vs 83.5) but decayed more slowly (table 0.60 vs 0.76, text 0.591 vs 0.711; the paper is inconsistent). [b17, c20]

**M8. Own-output blind spot.** Present the model's own draft as someone else's patch to review. Appending "Wait" nearly closes the gap to reasoning siblings (Qwen3-14B 0.117 -> 0.868). This is a prompt-level operator, tested on injected errors and open models, not on repo-level debugging.

**M9. Patch selection by tests.** Generate several candidates, select by regression tests and reproduction tests (Agentless 25.67 -> 27.00 -> 32.00). Good selection is worth more than more generation (CodeMonkeys: random 45.8 vs oracle 69.8). Aligns with schema G5 (code selects).

**M10. Context trimming.** Keep the last 5 observations and summarised search (18.0 vs 15.0). Full history can hurt, which is consistent with decay (M7).

## 5. What holds up

**Holds up (two or more independent sources).**
- Without an outside signal, LLM self-revision does not help and often hurts (K06, 5 sources). [a17, a21, b23, d04-d06]
- Diagnosis is the bottleneck, not repair (K08; Olausson, Tyen, and indirectly Meng and Liu). [a15, a20, d10, d13]
- At equal compute, self-repair gives little over resampling (K09; Olausson, with heat maps). [a14, b10, b11]
- Execution feedback is what makes self-debug work (K14; Chen, Reflexion, Kamoi). [a28, c05, c13, b23]

**Contested.**
- "Novices add bugs" (K02). Vessey supports it but the novice label is partly circular. Kinnunen restates it second-hand. An LLM analogue exists at patch level (d12) but not per edit.
- "Less reading is better" (K05). Ko and Uttl (n=75) found reading strategy did not predict success, with experience confounded. CodeMonkeys shows reading everything is cheap when shared. [b07, d07]

**Single-source and not replicated.**
- The fresh-start result (K10). No replication on strong or reasoning models found. CodeMonkeys supports fresh starts over added iterations at equal cost, indirectly. [d08]
- Linter guard (K11), history trimming (K12), pipeline vs agent (K13), localization-tracks-resolution (K22), same-model reviewer (K25), LDB (K26).

**Failed or null results.**
- Self-Correct on CSQA lowered GPT-3.5 from 75.8 to 38.1. [a17]
- Simple feedback lowered Codex on MBPP from 61.4 to 57.6. [c05]
- Self-Refine on code optimisation: GPT-4 +0.2. [c12]
- 2 initial + 10 repairs fell below resampling (0.97x). [c01]
- No eye-tracking or modern-cohort replication of the expert-novice finding was found; two titles seen, none opened. [d19]

**Moderators.**
- Model strength: Self-Refine gain falls as base strength rises. In Tyen, redoing a step helps at 50% base accuracy (68.6) and hurts at 99% (92.8).
- Bug type: runtime feedback helps syntax and reference bugs, not logic bugs. [c24]
- Bug count: DebugBench GPT-4 falls from 73.1 (single logic) to 55.9 (four bugs). [c23]
- Task difficulty: human feedback gain (points) is +19.6 intro, +26.3 interview, +11.0 competition. [a15]
- Reasoning training: small blind spot, but o1-mini still overturns 34.0% of correct answers. [d05, d06]

**Interventions that worked:** outside tests or traces; stronger-model or human diagnosis; fresh start (small models); linter guard; reproduction tests in selection; "Wait" cue (on blind-spot tasks).

**Interventions that did not:** intrinsic self-correction; extra repair rounds at equal tokens; generic feedback (26.0 vs 27.5 for specific in Self-Refine); whole-file viewer (12.7 vs 18.0 at 100 lines).

## 6. Language models

No study found tests "experts form better hypotheses from less reading" directly on an LLM. The LLM evidence is indirect and falls in four groups.

**Self-correction (hypothesis quality as self-judgment).** Huang 2024: GPT-3.5 CSQA 75.8 -> 38.1; GPT-4 GSM8K 95.5 -> 89.0. Reasoning models reduce the harm but do not remove it: o1-mini overturns 34.0% of correct answers, o1-preview 15.6% (d06). The own-output blind spot averages 64.5% for open models; "Wait" cuts it by 89.3%; reasoning models show a small or negative blind spot (d04, d05). No 2026 model was tested.

**Repair loops.** Olausson: equal-budget repair is 0.97x to 1.05x of resampling for GPT-4. Human diagnosis lifts 33.30 -> 52.60. Self-Debug: up to +12 with tests; Codex MBPP loses 3.8 points with simple feedback. Decay: 60-80% lost in 2-3 attempts for most models; fresh start gave +10.26 (llama3.1:8b) and +8.0 (deepseek-coder-v2).

**Agents on repos.** SWE-agent: linting +3.0; 51.7% of runs had a failed edit; recovery 57.2% after one. Agentless 32.00% at $0.70. CodeMonkeys: selection 45.8 random vs 57.4 their method vs 69.8 oracle. Localization F1 order matches resolve order. Patch-level regression: 11 of 22 confirmed-incorrect patches broke existing behaviour; 7.8% of plausible patches fail the full suite. Failure taxonomy: agents mostly loop on a failed strategy; Agentless fails at localization (51.3%). A same-model reviewer rescued 24 of 108 (no matched control).

**Debugging by bug count and type.** GPT-4 falls from 93.6 on missing colons to 55.9 on four simultaneous bugs. LLM review of novice code finds a real issue 90% of the time but invents non-existent issues 40% of the time (GPT-3.5).

**Caveats for all of the above.** Many are preprints on GPT-3.5 and GPT-4. Few hold tokens equal. Search access ran out mid-run, so coverage of 2025-2026 work is partial (d20).

## 7. What our agent should take

Status marks follow SCHEMA.md: [E] established (2+ independent sources), [S] single-source, [C] contested.

### Add now (established)

Most of these confirm rules already in SCHEMA.md. None is new. Keep them as they are.

1. **Revise only from real output.** Schema part: G2, S5. [E] K06, K14. Ids: a17, a21, b23, c05, c13, d04, d05, d06. A revision must cite a failing test or trace produced by code.
2. **Give the care to diagnosis, not repair.** Schema part: S5/S6 (one line naming what is wrong before the fix). [E] K08. Ids: a15, a20, c03, c09, d10, d13. Located, evidenced diagnosis before any edit.
3. **Prefer fresh samples over many repair rounds at equal tokens.** Schema part: S3, G11, G12. [E] K09. Ids: a14, b10, b11, c01. The existing cap of 2 rounds in S5 is consistent with this.
4. **Use execution feedback in the loop.** Schema part: S4, S5. [E] K14. Ids: a28, c04, c05, c13. No tests means no gain; do not run reflection without a check.

### Test first (single-source or contested)

| Item | Schema part | Status | Ids |
|---|---|---|---|
| Edit guard: reject an edit that breaks syntax or a check before keeping it | G5, S5 | [S] K11 | a24, a25, c14 |
| Keep best-so-far and revert on regression | G6, S5, memory | [S] analogue of K02, no direct test | b05, d12, d11 |
| Edit cap per round | S5 | [C] K02 | b05, a25 |
| Fresh start (clear history, keep problem plus best-so-far) after 2 failed rounds | S5/S6, memory | [S] K10 | a23, b16, c19, d08 |
| Run pass-to-pass (regression) tests before accepting a patch | G3, S8 | [S] K23 | d11, d12, d18 |
| Separate diagnosis call, larger budget on diagnosis | S5, S6 | [S] K08 (equal-token form untested) | a16, b13, c02, d14 |
| Present own draft as a third party's patch ("Wait" cue) | S5 | [S] K19 | d04, d05 |
| Capped read, then forced ranked hypothesis, before first edit | S1/S2 | [C] K01, K05 | a02, b07, d07 |
| System summary before first edit | S1/S2 | [S] K03 | b06, a07 |
| Force a new hypothesis after a failed round (stall rule) | S6 | [S] K24 | d13 |
| Last-5-observations history trimming | memory | [S] K12 | c15 |
| Require reproducing evidence for any claimed bug | G2 | [S] K17 | c21, c22 |
| Fix one bug at a time vs all at once | S6/O3 | [S] K16 | a27, c23 |
| Fixed localise-repair-validate pipeline vs free-form | S-validate | [S] K13 | a26, c17 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, same items, same seeds; setup cost counted (G7). Use items with a code check (hidden tests plus visible tests). Report resolved rate and regression rate.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Short bug-fix tasks with a seeded single bug and hidden tests (HumanEval-style plus a repo-level subset) | A: free edits, keep last state. B: edit guard plus keep best-so-far with revert, cap 2 edits per round | Resolve rate; regression rate (new failing tests per edit) | B higher by 2 to 4 points; regressions down |
| T2 | Same items, tasks where round 1 fails | A: continue conversation for rounds 2 and 3. B: fresh start after round 2 with problem plus best-so-far | Final pass rate at equal tokens | B +3 to 8 points on weaker models; near 0 on strong models (no decay seen in Claude 3.7) |
| T3 | Same items | A: capped read (e.g. 25% of files or lines) then forced ranked hypothesis list. B: full read then hypothesis | Hypothesis hit rate (blind-rated or located-file F1); final fix rate | Small or null (Ko and Uttl null; CodeMonkeys says reading is cheap). A null removes the idea |
| T4 | Same items | A: joint repair. B: separate diagnosis call with 2x budget, then repair | Fix rate | B +3 to 6 points (Olausson's 33.30 -> 52.60 used human feedback, so expect less) |
| T5 | Same items | A: repair rounds on 2 candidates. B: 4 to 5 fresh candidates, test-based selection | Pass rate at fixed total tokens | B higher or equal (0.97x to 1.05x in Olausson) |
| T6 | Same items | A: standard review of own draft. B: draft shown as a third party's patch plus "Wait" cue | Fix rate on injected errors; rate of correct answers overturned | B lowers blind spot; check it does not raise overturn rate |
| T7 | Accepted patches from T1 to T5 | A: accept on target test only. B: accept only if regression tests also pass | Regressions shipped; false accept rate | B cuts wrong accepts (7.8% fail full suite) |
| T8 | Multi-bug items (1, 2, 3 seeded bugs) | A: fix all at once. B: one bug at a time with a test after each | Pass rate by bug count | B better at 3 or more bugs (GPT-4 55.9 at four) |
| T9 | Failed-round traces | A: no stall rule. B: after a failed round require a hypothesis different from all earlier ones | Fix rate; share of looping traces | B fewer loops |
| T10 | Logged traces | Correlate blind-rated hypothesis quality per trace with final fix rate | Spearman correlation | Positive (system-level F1 tracks resolution); needed to justify T3 and T4 |

## 9. What does not transfer, and why

- **Human reading effort.** Experts reading less saves human time and attention. An LLM reads a file in seconds, and CodeMonkeys scans every file for under 15% of cost. A hard reading cap may save nothing.
- **Novice labels.** Vessey defined novices by chunking observed in the same protocols, so "novices make more errors" is partly circular. We have no clean LLM equivalent of "novice".
- **Expertise as accumulated knowledge.** Expert comprehension comes from years of practice. A model with fixed weights cannot gain it from a scaffold. The scaffold can only add checks and structure.
- **Simple programs.** The authors hedge to simple LOGO and Pascal programs. Large repos with hard bugs may differ.
- **Why humans add bugs.** Humans lose track of memory and intent while editing. LLMs add bugs by misreading code, not through fatigue. Remedies (guards, tests) are shared, but the cause differs.
- **Decay across attempts.** Humans learn from failed attempts. LLMs in a long context may anchor on them. Fresh start has no human analogue as stated.
- **Small, old models.** Many results are on GPT-3.5, GPT-4, Code Llama and small open models. Claude 3.7 hit 100% in two attempts, so the decay fix had nothing to fix there.
- **Blind-spot tasks.** The blind-spot study injected errors into reasoning. Repo-level bugs are different.

## 10. Open questions

1. What were the real figures in Gugerty and Olson 1986 (sample, times, accuracy, bug-addition counts)? Needs a library copy or the Ablex chapter.
2. Does a capped read plus forced ranked hypothesis beat full read at equal tokens for an LLM?
3. What is the per-edit regression rate for LLM agents, and do an edit cap and keep-best reduce it?
4. Does the fresh-start result replicate on 2025-2026 strong and reasoning models and on repo-level tasks?
5. Does stronger-model diagnosis beat joint repair at equal tokens?
6. Katz and Anderson 1987: do forward and backward search strategies differ in success, and does that apply to agents?
7. Are there eye-tracking or modern-cohort replications of "experts form hypotheses from less code"?
8. How well does blind-rated hypothesis quality correlate with the final fix rate?
9. Do current (2026) reasoning models still show Huang-style harm from intrinsic self-correction?
10. Does the "Wait" cue help on repo-level debugging, or only on injected-error reasoning tasks?

## 11. Sources

Marked [V] opened (full text or page read) or [M] snippet or metadata only.

- [M] Gugerty and Olson (1986), Debugging by skilled and novice programmers. https://dl.acm.org/doi/10.1145/22339.22367 (abstract read via Crossref https://api.crossref.org/works/10.1145/22339.22367; full text blocked). Snippet: https://www.bohrium.com/paper-details/debugging-by-skilled-a ; copy: https://www.academia.edu/102488941/Debugging_by_skilled_and_novice_programmers
- [V] Kinnunen (2007) MSc thesis, Univ. of Eastern Finland. https://cs.uef.fi/pub/Theses/2007_MSc_Kinnunen_Maria.pdf
- [V] Spoerer and Michaeli (2025) scoping review of student debugging processes. https://computingeducation.de/pub/2025_Spoerer-Michaeli_Koli
- [V] Vessey (1985) Expertise in debugging computer programs. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/vessey85 (metadata: https://api.crossref.org/works/10.1016/S0020-7373(85)80054-7)
- [M] Katz and Anderson (1987) Debugging: an analysis of bug-location strategies. https://doi.org/10.1207/s15327051hci0304_2
- [M] McCauley et al. (2008) Debugging: a review of the literature. https://api.crossref.org/works/10.1080/08993400802114581
- [V] Ko and Uttl (2003) Individual differences in program comprehension strategies. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/Ko'03.pdf
- [V] Davies (2000) Expertise and the comprehension of object-oriented programs. https://ppig.org/files/2000-PPIG-12th-davies.pdf
- [V] Olausson et al. (2024) Is Self-Repair a Silver Bullet for Code Generation? https://arxiv.org/abs/2306.09896
- [V] Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516
- [V] Kamoi et al. (2024) When Can LLMs Actually Correct Their Own Mistakes? https://arxiv.org/abs/2406.01297
- [V] Adnan and Kuhn (2025) The Debugging Decay Index. https://arxiv.org/abs/2506.18403
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/abs/2405.15793
- [V] Xia et al. (2024) Agentless. https://arxiv.org/abs/2407.01489
- [V] Tian et al. (2024) DebugBench. https://arxiv.org/abs/2401.04621
- [V] Chen et al. (2024) Teaching Large Language Models to Self-Debug. https://arxiv.org/abs/2304.05128
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Hellas et al. (2023) Responses of LLMs to Beginner Programmers' Help Requests. https://arxiv.org/abs/2306.05715
- [V] Tsui (2025) Self-Correction Bench. https://arxiv.org/abs/2507.02778
- [V] Zhang et al. (2025) Understanding the Dark Side of LLMs' Intrinsic Self-Correction. https://arxiv.org/abs/2412.14959
- [V] Ehrlich et al. (2025) CodeMonkeys. https://arxiv.org/abs/2501.14723
- [V] Meng et al. (2025) LLM-based Agents for Automated Bug Fixing: How Far Are We? https://arxiv.org/abs/2411.10213
- [V] Wang, Pradel and Liu (2026) Are "Solved Issues" in SWE-bench Really Solved Correctly? https://arxiv.org/abs/2503.15223
- [V] Liu et al. (2025) An Empirical Study on Failures in Automated Issue Solving. https://arxiv.org/abs/2509.13941
- [V] Zhong et al. (2024) Debug like a Human (LDB). https://arxiv.org/abs/2402.16906
- [V] Antoniades et al. (2025) SWE-Search. https://arxiv.org/abs/2410.20285
- [V] Wang et al. (2025) Thoughts Are All Over the Place (underthinking). https://arxiv.org/abs/2501.18585 (abstract only in detail)
- [V] Yu et al. (2025) UTBoost. https://arxiv.org/abs/2506.09289
- [M] Eye-tracking and modern cohort titles (Crossref, 2015-2026), none opened. https://api.crossref.org/works?query.bibliographic=eye+track

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 3 established claims: 2 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A20.05-K14** (reworded: the sources support less). Chen et al. show self-debug also helps without execution when the model explains its code (Spider +2-3%, MBPP Codex 61.4 -> 64.4 with explanation, 66.2 with trace); only simple yes/no feedback hurt (Codex MBPP 57.6), so execution feedback is not the sole driver. Corrected claim: Self-debug gains are largest with unit-test execution feedback (up to +12 on TransCoder and MBPP), while without execution plain pass/fail feedback can hurt (Codex MBPP 61.4 -> 57.6) but code explanation or trace feedback still helps (Codex MBPP 64.4 and 66.2; Spider +2-3%).
- **A20.05-K09** (now single-source: only one opened source, code check).
