# LLM debugging: deep document

*Subfield E09.09. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K36) and critique.md in this folder. Evidence ids (a01, b05, d12 ...) point to the evidence files. Claim ids (K01 ...) are written without the "E09.09-" prefix. Almost all code-repair numbers come from 2023-2024 models. Where a number was corrected by the cross-check, the corrected number is used.*

Neighbouring subfields researched in parallel (not covered here, links only): Verification design; Adaptive stopping and metareasoning; Progress monitoring theory; Consistency-based diagnosis and conflict generation; Probing and measurement selection; Hypotheses in debugging; Troubleshooting search strategies; LLM metacognitive harness; Accuracy and dissociation of monitoring; Anomaly handling and fixation.

---

## 1. What it is

LLM debugging is the study of how language models find and fix faults in programs, and which loop designs make them better at it. Four threads belong to it.

1. **Self-debugging with execution feedback.** The model writes code, a program runs it, the result goes back to the model, the model fixes the code. Founding paper: Chen et al. (a01).
2. **Self-correction without outside feedback.** The model re-reads its own answer and revises it. This is the control case. It mostly fails (Huang et al., a06).
3. **Fault localisation and repair on real repositories.** SWE-bench (a31), SWE-agent (a24), Agentless (a27), AutoCodeRover (a30), AutoFL (a22). The task is: find where the bug is, edit, pass the tests.
4. **Failure analysis.** What goes wrong in long agent runs: repeated failed edits, test overfitting, thrashing a correct edit, stopping too early (a26, d16, b20, a33).

Why it matters for our agent. Code debugging is the cleanest case of our schema. There is one answer (a patch) and a real check (tests). So it gives hard, countable evidence on three schema parts: revise only from real output (G2), a pass must be on something the answer was not fitted to (G3), and the stop and give-up rules (S5, S6, S8). It also gives the strongest warning in the literature about self-written tests as judges.

Scope limit. The human side (how programmers debug) is covered in other E09 subfields. This document is only about models.

---

## 2. History and theories in depth

### 2.1 Before 2023: repair as search, fault localisation as ranking

Classic automated program repair generated many patches and kept those that passed tests. Classic fault localisation ranked code lines by which passing and failing tests ran them. The best known is spectrum-based fault localisation (SBFL, e.g. Ochiai). Both ideas return later: Agentless is generate-then-filter (a27), and AutoCodeRover uses SBFL as a hint (a30, c18). Test overfitting (a patch passes the given tests and is wrong) was already a known problem in that literature, and it comes back in SWE-bench audits (a33).

### 2.2 2023: the first wave of "let the model check itself"

Three papers set the frame.

- **Self-Debug (Chen, Lin, Schaerli, Zhou).** The model writes code, runs it, reads the result, explains its code line by line ("rubber duck"), and fixes it. Feedback comes in four kinds: simple (right or wrong), unit-test output, code explanation, execution trace (a01, a02). Claim: it works with execution output, and one turn captures most of the gain.
- **Reflexion (Shinn et al.).** The model writes its own unit tests, runs them, writes a verbal lesson after failure, stores it, retries (a10). Claim: 91.0% on HumanEval Python versus 80.1% for GPT-4.
- **Self-Refine (Madaan et al.).** One model gives feedback on its own output, then rewrites, repeated (a14). Claim: about 20% absolute gain on average over seven tasks.

All three reported gains. They differ in one thing that turned out to decide everything: where does the signal that something is wrong come from? Self-Debug on unit-test tasks and Reflexion use real execution. Self-Refine and Self-Debug on Spider use the model's own judgement.

### 2.3 2023-2024: the correction

- **Huang et al. (a06, b09).** Many reported self-correction gains used oracle labels (the correct answer told the loop when to stop). Remove the oracle and accuracy falls. Some "gains" came from a weak first prompt that left out a requirement the feedback prompt then added (a09).
- **Olausson et al. (a16).** Count tokens, not samples. Then self-repair is a small gain over drawing more independent samples, and sometimes no gain. The weak step is the model's own explanation of the bug (a17).
- **Tyen et al. (b11).** Finding the first wrong step is the hard part. Fixing it is easier.
- **Kamoi et al. survey (b14).** No prior work shows success with prompted-LLM feedback outside tasks that suit it. It works with reliable external feedback.

The apparent contradiction between Chen and Huang is not one (c26). Chen's gains come with execution feedback. Huang's losses come with none. Different tasks (code vs math and commonsense) as well.

### 2.4 2024: agents on real repositories

SWE-bench (a31) made the task real: 2,294 GitHub issues in 12 Python repos. At release, the best result with a BM25 retriever was 1.96% (c16). Then:

- SWE-agent (a24): the tool layer designed for the model (viewer, search, linted edits) beat a plain shell by 64% relative with the same model.
- Agentless (a27): no agent, three fixed phases, 32.00% at $0.70 versus 18.33% at $1.62 for SWE-agent with the same base model. Biggest gain was test-based patch selection (a28).
- AutoCodeRover (a30): code-structure search and optional SBFL hints.
- LDB (a19): feed real variable values from a real run, block by block.

### 2.5 2025-2026: stall detection, benchmark hygiene, reasoning models

- Test-time scaling work (S*, CodeMonkeys, Large Language Monkeys: d02, d05, d07): coverage grows with samples; selection is the bottleneck.
- Failure anatomy on thousands of trajectories (d16, d17, c21): the strong-model failure is often not localisation but ruining a correct edit.
- Outside monitors (d13, d14): a stronger or rule-based watcher can break a stall.
- Real debuggers as tools (d15).
- Benchmark audits (a32, a33, d18, d19, d20): public SWE-bench scores are inflated by leakage and weak tests.
- Blind spot work (b13, d12): non-reasoning models fail to fix errors in their own output; reasoning models mostly do not.

### 2.6 Competing explanations that remain

| Question | View A | View B |
|---|---|---|
| Does repair beat resampling at equal cost? | Yes, one debug turn equals 16 samples (Chen, Spider, sample counts; b04) | No, 1.05x and 0.97x at equal tokens (Olausson, a16/b06); often below sampling at equal calls (BESTER, d04) |
| Why does the iterative gain appear when the model gates itself? | Real correction | Re-solving: a fresh attempt at the same problem (d08) |
| Why is explanation useful? | It forces a re-read (rubber duck; b03) | Mostly wrong (about 20% accurate) and never isolated from re-reading (a23, d21) |
| Are runtime values better than model-simulated traces? | Yes, LDB (a19, a20) | Margins are small and from one group (K07) |
| Do small models self-debug? | Yes, StarCoder +6 on MBPP (a02) | No, StarChat 0.26 to 0.26 (a13); StarCoder LDB +0.6 (a20) |

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent groups), **S** single source, **C** contested, **N** not code (math or logic), **O** older models only.

| # | Finding | Numbers | Source | Status |
|---|---|---|---|---|
| 1 | Real execution output makes the debug loop work. | TransCoder GPT-4: 77.3 base, 80.9 simple, 90.4 unit-test+explanation (+13.1). Codex MBPP: 61.4 base, 68.2 simple, 69.4 UT, 69.8 UT+Expl, 70.8 UT+Trace. | Chen (a02, b01); K01 | E, O |
| 2 | Without execution, self-debug gains shrink and can go negative. | Codex MBPP: 61.4 to 57.6 (simple), 64.4 (explain), 66.2 (trace). GPT-4 MBPP +3.6 best, others about +1. GPT-3.5 TransCoder unchanged at 89.1. | Chen (a03, b02) | E, O |
| 3 | Intrinsic self-correction does not help reasoning and often hurts. | GPT-3.5 CSQA 75.8 to 38.1. GPT-4 GSM8K 95.5, 91.5, 89.0 over two rounds. GPT-3.5 GSM8K 75.9, 75.1, 74.7. Self-Refine math: GPT-4 92.9 to 93.1. | Huang (a06); Madaan (a14); K02 | E, N |
| 4 | Oracle stop labels inflated earlier gains. | With oracle: GPT-3.5 GSM8K 75.9 to 84.3; GPT-4 HotpotQA 49.0 to 59.0; GPT-4 GSM8K 95.5 to 97.5. Reflexion Rust, no tests: 0.52 vs base 0.60. | Huang (c05); Shinn (a12); K03 | E |
| 5 | Model keeps its answer; when it changes, right-to-wrong beats wrong-to-right. | GPT-3.5 GSM8K: 74.7% unchanged after two rounds. | Huang (a07) | E, N |
| 6 | When the model alone gates correction, it breaks more than it fixes. | Single check: 10.9% broken vs 6.2% fixed. Any-of-9: 21.4 vs 8.1. Majority: 12.7 vs 6.3. Unanimous: 6.0 vs 3.5. | Samanta (d10); K31 | E, N |
| 7 | At equal tokens, repair is slightly above or equal to resampling. | GPT-4 APPS: 10 initial + 1 repair each = 1.05x pass@20; 2 initial + 10 repairs each = 0.97x pass@22. Only GPT-4 gains significantly on APPS. | Olausson (a16, b06); K04 | C, O |
| 8 | At matched calls, plain repair can fall below sampling. | 21 calls, APPS DeepSeek: sampling 57.54, execution-feedback repair 53.67, Reflexion 50.67, BESTER 54.67. GPT-4 HumanEval: 82.67, 88.41, 89.02, 90.24. | Song (d04) | S, O |
| 9 | Small frozen models: fresh sampling beats re-showing the failed program. | 290 dead task-model units, 3 models of 0.5B-1.5B. Blind resampling beat bare-code retry by +18 net unlocks (25/7, Holm p=0.0021). Code+facts tied blind resampling (26 vs 26). | d01; K27 | S |
| 10 | On Spider, one debug turn matches many samples (counted in samples). | Debug of greedy output = 16 samples. Debug of 8 samples beats 32 samples. Turns after the first add under 0.1%. | Chen (a04, c02); K09 | C |
| 11 | Gains arrive in the first 1-3 rounds. | Spider: later turns under 0.1%. S* uses 2 rounds after returns flatten. debug-gym: last rewrites add almost nothing. CodeMonkeys: serial and parallel equal-cost mixes similar after the first few iterations. LDB still climbs to 10 iterations (82.9 at best, about 84.1 at iteration 10). | a04, d02, d03, d05, d15; a21, c13; K28 | E for the early flattening, C for LDB |
| 12 | Feedback quality is the bottleneck. | GPT-4 repair success with its own explanation 33.3% vs 52.6% with expert human explanation (16 people, 40 programs). By level: intro 42.64 vs 62.21; interview 19.33 vs 45.67; competition 3.67 vs 14.67. | Olausson (a17, c08); K05 | S |
| 13 | Finding the first wrong step is hard; fixing it given the step is easier. | BIG-Bench Mistake, GPT-4 localisation 52.87. Backtracking with true step on wrong traces: +23.5, +43.9, +36.9, +18.0, +18.1; random step +11.8, +20.4, +21.6, +10.6, +5.2. On correct traces: true step -0 to -11.4, random -6.7 to -15.9. | Tyen (b11, b12); K06 | E (2 groups), N |
| 14 | The model's own location hint can hurt. | GSM8K correction: GPT-3.5 26.8 to 15.5; Claude 29.1 to 12.8; DeepSeek 16.7 to 26.7 (n=30). Iterative 3 rounds: GPT-3.5 67.9, Claude 60.8. | Li (d08); K30 | C, N |
| 15 | Reasoning models locate first errors far better. | ProcessBench F1: o1-mini 87.9 vs GPT-4o 61.9 (3,400 cases). | Zheng (d11) | S, N |
| 16 | Runtime values beat model-simulated traces by small margins. | HumanEval GPT-3.5 seed 73.8: LDB 82.9 vs Self-Debug 81.1. GPT-4 seed 87.2: LDB 89.6 vs 88.4. Reflexion seed 91.5: LDB 95.1 vs 92.1. StarCoder 39.0: SD -0.6, LDB +0.6. | Zhong (a19, a20, c12); K07 | S |
| 17 | Explanation (rubber duck) gives a small gain when no tests exist. | Spider Codex 81.3 to 84.1 (+2.8). GPT-3.5 71.1 to 72.2, GPT-4 73.2 to 73.6, StarCoder 64.7 to 64.9. Extra-hard +9. | Chen (b03); K08 | C |
| 18 | Model explanations of faults are often wrong. | AutoFL: 300 explanations from 60 bugs, 20% accurate, 26.3% with at least one wrong statement, 56.7% of bugs had at least one accurate explanation in 5 runs. No no-explanation arm. | Kang (a23, d21) | S |
| 19 | Fixes are mostly small slips. | Spider fixes: wrong WHERE 25.7%, missing DISTINCT 17.1%, wrong JOIN 14.3%. Output mismatch: TransCoder 61.9%, MBPP 69.2%. Unresolved SWE-agent Lite runs (n=248): wrong or over-narrow implementation 52.0%, cascading failed edits 23.4%. | Chen (a05); Yang (a26, b21); K10 | E |
| 20 | Self-written tests as the lone judge of success are unreliable. | Reflexion false positives: MBPP Py 16.3%, HumanEval Py 1.4%. Pass@1: HumanEval 80.1 to 91.0; MBPP 80.1 to 77.1. SWE-bench: 7.8% of plausible patches fail the full developer tests; 29.6% (260 of 877) behave differently from the true fix. | Shinn (a10, a11); Wang (a33, c20); K11 | E |
| 21 | Agent-written reproduction tests are a strong filter over many candidates. | Agentless Lite: majority vote 77 (25.67%) at $0.00; +regression tests 81; +reproduction tests 96 (32.00%) at +$0.25. Sampling plateaus near 40. Upper bound if best sample picked: 126 (42.0%). | Xia (a28, b23); K12 | S |
| 22 | The same generated tests do not help when real public tests exist. | S* LiveCodeBench: public tests only 53.8, generated tests 53.1, LLM judge 55.6. CodeMonkeys (no public tests): random 45.8, final 57.4, oracle 69.8. | Li (d03); Ehrlich (d06); K29 | C |
| 23 | Tool interface changes results at a fixed model. | SWE-agent GPT-4 Turbo Lite: full 18.0; shell-only 11.0; RAG 2.67. Edit no tool 10.3, edit 15.0, edit with lint 18.0. Viewer 30 lines 14.3, 100 lines 18.0, full file 12.7. Search: summarised 18.0, none 15.7, iterative 12.0. | Yang (a24, a25, b19); K13 | E (run noise about 0.5 to 2 points) |
| 24 | A fixed pipeline matched an open agent at lower cost. | Agentless GPT-4o 32.00% at $0.70 vs SWE-agent GPT-4o 18.33% at $1.62. System-level, not an ablation. | Xia (a27); K14 | S |
| 25 | Failed edits compound. | 51.7% (1,185/2,294) of trajectories had at least one failed edit (31.5% of resolved ones). P(edit eventually works): 90.5% with no failure, 57.2% after one. Recoveries took 2.03 failed attempts; non-recoveries 4.22. Failed runs longer: +12.6% to +82.5%. | Yang (a26, b20); Majgaonkar (c23); K15 | E |
| 26 | Returns drop sharply after about 25 rounds. | Successes: 80% within 19 (Tools Claude) or 25 (OpenHands) rounds. Failures need 54 rounds to cover 80%. Failed agent runs take 3.5x more steps. | Liu (c21, c28) | S |
| 27 | For strong models, failure is often after reaching the right code. | 16,758 trajectories. SWE-agent on Verified, 1,607 failures: edit-quality 56.9% (GPT-5 68.1%). Of 914 of those: coherence collapse 39.7% (22.6% of all failures), wrong branch point 18.6%. Edit-commit checkpoint recovered all 5 exact-gold cases. | Kim (d16); K34 | E |
| 28 | Fault-localisation hints from test coverage help repo-level localisation. | AutoCodeRover Lite: 57 to 66 resolved (19.0% to 22.0%) at $0.43 to $0.47. | Zhang (a30, b30); K17 | S |
| 29 | Repeat-run agreement of a localiser is a confidence signal. | Spearman with Precision@1: 0.57 (Defects4J), 0.52 (BugsInPy). Method acc@1 up to +233.3% over Ochiai (GPT-4, BugsInPy; small base). | Kang (a23); K16 | S |
| 30 | Diverse agents' candidates, picked by a committee, beat the best single agent. | Lite: best single 27.3%, DEI committee 34.3%, union of 9 agents about 53%. | Zhang (c19); K22 | E (weak on equal compute) |
| 31 | An outside monitor can break stalls, if it is strong or rule-based. | Claude Sonnet 4 monitor: 40.0 to 50.6 on Verified at about 9x cost; open monitors 30.0-38.8; action-prescribing feedback 44.8. Rule monitor +6.9 to +23.5 on 86 pre-selected cases. | Gandhi (d13); Liu (d14); K32 | S |
| 32 | A real debugger helps strong models on hard repo bugs. | debug-gym, Lite, Claude 3.7: rewrite-only 37.2, pdb 48.4, pdb after 5 failed rewrites 52.1. Aider: o3-mini 95.2 vs 94.2. | Yuan (d15); K35 | S |
| 33 | Non-reasoning models have a self-output blind spot; reasoning models mostly do not. | 14 non-reasoning models: 64.5% blind spot; "Wait" cut it by 89.3%. R1-Distill-Llama-70B: -0.031 (GSM8K-SC), -0.05 (PRM800K-SC), +0.113 (SCLI5). | Tsui (b13, d12); K19, K33 | E for non-reasoning, S for reasoning, N |
| 34 | Public benchmark scores are inflated. | SWE-Bench+: 32.67% of passes leaked the answer; 31.08% weak-test suspicious; 12.47% to 3.97%. Lite: 4.3% contain the exact patch. SWE-bench-Live: 19.25% vs 43.20% same pair on Verified. SWE-Bench Pro: public 43.6, commercial 17.8. PatchDiff: inflation 6.4 points. | a29, a32, a33, d18, d19, d20; K18, K36 | E |
| 35 | Specific feedback beats generic, which beats none. | Self-Refine code optimisation 27.5 / 26.0 / 24.8; sentiment reversal 43.2 / 31.2 / 0. | Madaan (a15); K25 | E (code spread 2.7 points, maybe noise) |
| 36 | Debate gains are mostly extra sampling. | GSM8K GPT-3.5: self-consistency 82.5 at 3, 85.3 at 6, 88.2 at 9 responses; debate about 83 at the compared count. | Huang (a08, b10); K20 | S here, E in schema G9 |
| 37 | Multi-agent failures are frequently verification and termination. | Premature termination 6.2%, no or incomplete verification 8.2%, incorrect verification 9.1%. 1,600+ traces. | Cemri (b27); K24 | S |
| 38 | Coverage grows with samples; selection converts it into accuracy. | SWE-bench Lite DeepSeek-Coder-V2: 15.9% (1 sample) to 56% (250 samples). Majority vote and reward models plateau near 100 samples (math). | Brown (d07) | E (with d05, a28) |

---

## 4. Mechanisms and models

Each mechanism is stated so an engineer can implement it. "Code" means plain program logic. "Model" means one slot filled by the language model.

### 4.1 The execute-observe-revise loop (Self-Debug)

```
draft = model(task)
for round in 1..R:
    result = code.run(draft, tests)          # real output
    if result.all_pass_on_held_out: break
    feedback = code.format(result)           # failing input, expected, actual, error text
    draft = model(task, draft, feedback)     # one revision slot
```

What matters, from the evidence:
- The signal must be real output (K01). Unit-test output, error trace, compiler text.
- Richer real feedback helps: failing input plus actual versus expected output. Adding a model-written explanation adds 0-2 points on MBPP (b01), more on cross-language translation (a02).
- R is small. Most of the gain is in rounds 1-3 (K28).
- The loop mostly repairs near-misses: a missing condition, wrong argument order, a wrong JOIN (a05). If the first draft has the wrong design, the loop does not fix it (K10).

### 4.2 Why execution feedback works and self-judgement does not

Execution output is information the model did not have and cannot fake. Self-judgement re-uses the same beliefs that produced the draft. Evidence: GPT-3.5 kept its answer 74.7% of the time (a07); when it changed, it broke more than it fixed (a07, d10). Mechanism candidates: (a) the model is overconfident in its first answer (Chen, a03); (b) its samples are correlated, so a second look repeats the error (schema G4); (c) a prompt asking "is there a mistake?" can push toward changing a right answer (the "any-of-9" gate broke 21.4% of correct answers, d10). The "non-reasoning blind spot" adds that errors in the model's own turn are harder to see than the same errors in the user turn (b13).

### 4.3 Equal-token accounting (pass@t)

Olausson's method (a16): count every token, including feedback and repair tokens. Compare:
- np initial samples, then nfr feedback strings per failure, then nr repairs per feedback.
- Against np' = more independent samples with the same total tokens.

Result: ratio near 1.0 for GPT-4 on APPS (1.05x and 0.97x). Implementation: log tokens per state, report pass rate at token budget t, not at sample count. Chen's "1 debug turn = 16 samples" counts samples and ignores explanation and feedback tokens (b04).

### 4.4 Test-guided candidate selection (Agentless, CodeMonkeys)

```
candidates = [model_patch(task) for _ in range(N)]        # fresh context each
repro = model_write_repro_test(task)                      # keep only if it fails on the unpatched repo
for c in candidates: run repro and regression tests on c
rank by (regression pass, repro pass, vote count); shortlist top k
(optional) model invents distinguishing INPUTS; code runs both candidates; real outputs decide
```

Why it works: it uses the model's weak skill (writing a plausible test) as a filter over many candidates, and real execution as the judge. Agentless: 77 to 96 fixes of 300 for +$0.25 (a28). CodeMonkeys: random 45.8, final 57.4, oracle 69.8; selection costs under 10% of total (d06). The version that worked best asked the model for inputs and read real outputs, not predicted outputs (d03). The gate that makes a repro test safe: it must fail on the original code (Agentless condition, a28).

Boundary: generated tests did not help when real public tests existed (S*: 53.1 vs 53.8, d03). Self-written tests as the only stop signal are unsafe (Reflexion MBPP, 16.3% false positives, a11).

### 4.5 First-wrong-step localisation (operator, not yet built for code)

Idea: before rewriting, name the first step that is wrong, with evidence. Tyen: with the true step, backtracking and regenerating gains +18 to +44 points on wrong traces (b12). Model localisation is the limit: GPT-4 52.87 (b11). Reasoning models are much better on math (ProcessBench F1 87.9 for o1-mini, d11). A model's own hint can hurt (d08). Structured thoughts (one complete thought per step) make self-localisation more reliable (Thought-ICS, d09). Implementation sketch: force the draft into numbered steps; ask the model to name the first step contradicted by a specific piece of real output; code checks that the named step exists and that the cited output exists; only then call the revise slot with the step marked. Score the named step against known planted bugs before trusting it (K30 test).

### 4.6 Runtime probing

LDB (a19): split into basic blocks, run, record variable values at block entry and exit, show the values to the model, ask it to mark each block right or wrong. debug-gym (d15): give the agent a pdb tool. Result pattern: small gain on function-level bugs (LDB +1.7 over Self-Debug with GPT-3.5), large gain on hard repo bugs only for strong models, and best when pdb is offered after 5 failed rewrites (37.2 to 52.1 for Claude 3.7). Early pdb could hurt weaker models. Mechanism: concrete values replace simulated values, so the model does not trace wrongly (a20, an explanation by the authors, not isolated).

### 4.7 Stall detection

Observed signs of a stall (d13, d14, a26, c28):
- Repeat cycle: the same action or edit more than once.
- At least 5 navigation steps with no edit (d14 rule).
- A failed edit: after one, P(success) falls from 90.5% to 57.2%.
- More than about 25 rounds.

Intervention that worked: a stronger or rule-based outside monitor names the failure type (taxonomy-guided 50.6 vs unguided 45.8 vs action-prescribing 44.8, d13). Rule monitor: loops cut by over 90%, resolution up (d14). Limits: cost about 9x (d13); selection bias (d14); the monitor must be stronger than the actor. Implementation: code watches the trace; on a trigger, one call with a different prompt and, if possible, a different model sees the last k steps and returns a labelled failure type; the main agent gets that label.

### 4.8 Keep-best checkpoint

Coherence collapse (d16): 22.6% of all failures overwrite or thrash a correct edit; 5 runs had written a patch identical to the gold patch and destroyed it later. Implementation: after every edit, code runs the independent check; if the score on the check is the best so far, snapshot the patch. At the end, if the final patch scores below the best snapshot, submit the snapshot. This costs no model tokens.

### 4.9 Interface guardrails

SWE-agent (a25): lint every edit before applying (+3.0 on Lite), window the file viewer to 100 lines (18.0 vs 14.3 at 30 lines and 12.7 for the full file), show only the last 5 observations (18.0 vs 15.0 full history). Mechanism: remove cheap failure modes (syntax errors from edits), limit context noise. Single runs; noise about 2 points on 300 items.

### 4.10 Localisation agreement as confidence

AutoFL (a23): run the localiser 5 times, agreement correlates with correctness (Spearman 0.57, 0.52). Use: branch to more investigation only when runs disagree. Caution (schema G4): samples from one model are correlated, so agreement is a hint.

---

## 5. What holds up

### 5.1 Replications and independent agreement

| Finding | Groups that agree | Verdict |
|---|---|---|
| Real execution feedback is needed for gains | Chen (a02, a03), Huang (a06, b09), Kamoi survey (b14), Shinn ablation (a12), Olausson (a17) | Established. |
| Intrinsic self-correction does not help | Huang, Kamoi, Madaan (math rows a14), Li (d08), Samanta (d10) | Established. Mostly math and QA. |
| The model's own gate breaks more than it fixes | Huang (a07), Samanta (d10), Li (d08: iterative gain looks like re-solving) | Established. |
| Self-written tests are unreliable as the lone judge | Shinn (a11), Wang (a33), Aleithan (a32), S* (d03) | Established. |
| Failed edits and long runs predict failure | Yang (a26), Majgaonkar (c23), Liu (c21, c28), Kim (d16) | Established as correlation. Hard tasks are both long and failed. |
| Early flattening of serial rounds | Chen (a04), S* (d03), debug-gym (d15), CodeMonkeys (d05) | Established for code. |
| Public SWE-bench inflates | Aleithan, Wang, Xia (a29), SWE-bench-Live, SWE-Bench Pro | Established. |
| Interface design matters | SWE-agent, CodeAct (c24, "up to 20%", abstract only), AutoCodeRover | Established; margins within noise for single ablations. |

### 5.2 Failures, boundary conditions, contradictions

- **Repair vs resampling (K04, contested).** Chen: 1 debug turn = 16 samples (Spider, Codex, sample counts, execution-free for Spider). Olausson: 1.05x and 0.97x at equal tokens (APPS, GPT-4, unit-test feedback). Song: plain repair below sampling for DeepSeek on APPS at 21 calls (d04). d01: blind resampling beat re-showing the code for tiny frozen models. CodeMonkeys: equal-cost serial and parallel similar after the first few iterations. Differences: unit (samples vs tokens vs calls), model, task, feedback. No matched-token test exists for a reasoning model.
- **Model strength (K21, contested).** Reflexion StarChat 0.26 to 0.26 (a13). Chen StarCoder MBPP 47.2 to 53.2 (a02). LDB StarCoder about 0. S* self-debug +12.1 for Qwen-32B but about 0 for reasoning models, and -2.8 for QwQ (d02). debug-gym: helps Claude 3.7, can hurt weaker models (d15). Li: weaker models corrected more of their own errors than the strongest (d08). Gain depends on loop and task, not size alone.
- **Rounds (K09).** Chen: later turns under 0.1% on Spider. LDB: climbs to 10 iterations on HumanEval with runtime values. Resolution: runtime values give new information each round; model-simulated traces do not.
- **Test filters (K29).** Agentless repro tests +19 patches; Reflexion MBPP tests hurt; S* generated tests no gain. Likely resolution: filter over many candidates, yes; lone stop signal, no; extra tests when public tests exist, no. Not tested directly.
- **Rubber duck (K08).** Gain concentrated in Codex on Spider (+2.8); GPT-3.5 +1.1, GPT-4 +0.4 (b03). Explanation is wrong about 80% of the time in AutoFL (a23). No study isolates explanation from re-reading (d21).
- **Corrected numbers.** The cross-check fixed four items (critique.md): Huang oracle rows, Chen MBPP Codex UT 69.4, debate table cells, Reflexion false-negative columns (not used).
- **Cost comparisons across papers.** SWE-agent Lite cost: $1.67 (own paper), $2.51 (AutoCodeRover), about $1.62 (Agentless, GPT-4o). Not comparable.
- **Debate.** Replication on full GSM8K: self-consistency beats debate at equal responses (b10). Original debate paper used 100 examples.

### 5.3 What worked and what did not (interventions)

| Intervention | Worked? | Evidence |
|---|---|---|
| Show real failing test output | Yes | a02, K01 |
| Add a model explanation on top of test output | Small: 0-2 points MBPP; more for translation | b01, a02 |
| Revise with no outside signal | No, usually harms | a06, d10 |
| Trusting the model to decide when to stop | No | a07, d10, a11 |
| Agent-written repro test + many candidates + execution | Yes | a28, d06 |
| Agent-written tests as the only judge | No | a11, a33 |
| Linted edits, windowed viewer | Yes, +3.0 and +3.7 on Lite (single runs) | a25 |
| Iterative search | Worse than no search (12.0 vs 15.7) | a25 |
| Full history in context | Worse than last 5 observations (15.0 vs 18.0) | a25 |
| Stronger outside stall monitor | Yes, at 9x cost | d13 |
| Same-size outside monitor | No (30.0-38.8 vs 40.0 base) | d13 |
| Tell agent the exact next action | Worse than naming the failure type (44.8 vs 50.6) | d13 |
| Debugger after 5 failed rewrites | Yes for strong model (+14.9) | d15 |
| Debugger from the start | Smaller gain for strong model, can hurt weak | d15 |
| "Wait" appended (non-reasoning) | Yes, cut blind spot 89.3% | d12 |
| Multi-agent debate | No better than voting | b10 |
| Stronger model's feedback on weaker coder | Yes | b07 |
| Committee over diverse agents | Yes (+7 points) but union far higher | c19 |
| Supervisor of strategy after failure | 22.2% rescue of prior failures (single source) | c22 |

---

## 6. Language models

### 6.1 Models and eras covered

- **2023 (Codex, GPT-3.5, GPT-4, StarCoder, Code Llama, StarChat):** Chen, Reflexion, Self-Refine, Olausson, Huang, LDB. Few-shot, function-level tasks (HumanEval, MBPP, TransCoder, Spider, APPS).
- **2024 (GPT-4 Turbo, Claude 3 Opus, GPT-4o):** SWE-agent, Agentless, AutoCodeRover, AutoFL.
- **2025-2026 (Claude 3.7, Claude Sonnet 4/4.5, GPT-5, o1-mini, R1-distill, QwQ):** S*, CodeMonkeys, debug-gym, SWE-PRM, coherence collapse, SWE-Bench Pro. The only data on reasoning models.

### 6.2 What the models do

1. **They are overconfident in a first answer** (Chen, a03). GPT-3.5 and GPT-4 rarely changed answers without real feedback.
2. **They fix errors well when told where and what.** Tyen: +18 to +44 with the true step (b12). Olausson: the explanation, not the repair, is the bottleneck (a17).
3. **They write unreliable tests.** Errors in tests correlate with errors in code (same model). Reflexion false positives 16.3% on MBPP.
4. **They loop.** After a failed edit, P(success) drops from 90.5% to 57.2% (a26). Repeated edits of the same snippet after a syntax error are prominent (c15). Failed runs are longer, with much wider spread (c23).
5. **They overwrite what was right.** 22.6% of all SWE-agent failures on Verified (d16).
6. **Strong models find the right place.** 56.9% of failures reach and edit the right function; 72-81% touch the right file (d16, c23).
7. **Reasoning models differ.** Self-debug gain on reasoning models: S* +1.0 (R1-Distill-32B on LiveCodeBench v2: 69.1 to 70.1), +3.4 (o1-mini: 76.5 to 79.9), -2.8 (QwQ-32B-Preview: 62.1 to 59.3), against +12.1 for Qwen2.5-Coder-32B (47.4 to 59.5) (d02). Reasoning models also show no blind spot (d12) and localise errors far better on math (d11). Sampling with majority vote and S* hybrids gain 8-10+ points, but at higher cost.
8. **Tool and loop design moves results as much as model change.** SWE-agent: 11.0 to 18.0 on the same model (a24). Agentless: 32.00% at $0.70 versus 18.33% at $1.62 (a27). Sonnet 4 as policy alone beat every monitored SWE-agent-LM-32B setup (66.6% vs 50.6%, d13).

### 6.3 What changed the numbers, by how much

| Change | Effect |
|---|---|
| Real unit-test output added to repair prompt (Codex MBPP) | +7 to +9 points (61.4 to 69.4-70.8) |
| Same, GPT-4 TransCoder | +13.1 |
| Removing execution (Codex MBPP simple) | -3.8 |
| Edit linting (SWE-agent) | +3.0 |
| Viewer 100 lines vs 30 / full | +3.7 / +5.3 |
| Repro-test selection (Agentless) | +19 patches of 300 (+6.3 points), +$0.25 |
| Selection loop (CodeMonkeys) | random 45.8 to 57.4, +11.6 points |
| Strong stall monitor (Verified) | +10.6 points at about 9x cost |
| Debugger after 5 rewrites (Claude 3.7) | +14.9 (37.2 to 52.1) |
| SBFL hints (AutoCodeRover) | +9 issues (57 to 66) |
| Committee over agents | +7 points (27.3 to 34.3) |
| Oracle stop label (Huang) | +8.4 to +10 on GSM8K, GPT-4 HotpotQA +10 |
| Intrinsic self-correction | -0.8 to -37.7 (GSM8K/CSQA) |
| Fresh private tasks | about half or less of public scores |

### 6.4 Evidence gaps for LLMs

No reasoning-model, long-chain-of-thought data exists for the self-debug question except S* (d02). No matched-token comparison of SWE-bench loop designs exists. Many 2026 items are single preprints (d01, d08, d12, d16).

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established (two or more independent groups), [S] single source, [C] contested. Evidence ids refer to the evidence files; K ids to claims.jsonl. Nothing here changes SCHEMA.md; items under "Test first" go to UNKNOWNS.md.

### 7.1 Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Revise only from real run output.** A revision step must cite a specific failing input and the actual output from code. No revision from opinion alone. Already G2; this evidence strengthens it. | G2, S5 | [E] | K01, K02, K03; a02, a03, a06, b09, a12 |
| A2 | **Never let the model decide to stop correcting.** The accept decision belongs to an independent check. Log broke-vs-fixed counts. If the revised draft does not beat the first draft on the independent check, keep the first. | G2, S5, S8 | [E] | K31, K03; d10, a07, d08, a11 |
| A3 | **Do not use the agent's own tests as the only judge.** Report pass on own tests separately from pass on held-out. Done requires the independent check. Already G3; this adds numbers (16.3% MBPP, 29.6% SWE-bench behaviour difference). | G3, S8 | [E] | K11; a11, a33, a32, c20 |
| A4 | **Cap serial revision on one draft at about 2-3 rounds, then restart or change approach.** Do not fix the exact number yet; use 2 as the default in S5 (already "at most 2 rounds") and keep it. | S5, S6 | [E] for early flattening | K28; a04, d02, d03, d05, d15 |
| A5 | **Keep-best checkpoint.** Snapshot every draft that improves the independent check; at the end restore the best. Costs no model tokens. | S7, S8 | [E] (two sources on the failure; the fix is only observed in 5 cases) | K34; d16, c23 |
| A6 | **Edit guardrail.** Code rejects syntactically broken or failing-lint edits before applying them, and returns the error. Window the file view; show recent observations, not the full history. | S5, tools | [E] | K13; a25, a24, c14 |
| A7 | **Stall triggers from content, not length.** Fire the impasse detector on: same action repeated, same error twice, a failed edit followed by another on the same snippet, 5 steps with no edit. Already S6 "the same error twice"; add "no edit in 5 steps" as a trigger. | S6 | [E] for the pattern as a failure sign; the trigger rule itself is untested | K15, K32; a26, b20, d14 |
| A8 | **Specific feedback to the revise slot.** Name the failing item and the observed vs expected output, not "improve this". | S5 | [E] | K25; a15, a17 |
| A9 | **Measure on held-out, post-cutoff or private items with hidden tests.** Check the answer is not in the task text. Public-set numbers overstate by about 2x. | bench hygiene, G7 | [E] | K18, K36; a32, d18, d19 |
| A10 | **Prefer selection by independent checks over debate and over self-judgement.** Already G5, G9. | G5, G9 | [E] | K20, K22; b10, c19, d05, d07 |
| A11 | **Failure log.** Tag each unresolved run as slip, wrong design, overwritten correct edit, premature stop. Cheap and needed for UNKNOWNS tests. | section 6 logging | [E] as a method | K10, K34; d16, a26 |

### 7.2 Test first

| # | Item | Part | Status | Evidence | Why not now |
|---|---|---|---|---|---|
| T1 | **Repair-after-failure vs a fresh sample at equal tokens.** Is S5 better than another S3 draw? | S5 vs S3 | [C] | K04, K27; a16, b06, d01, d04 | Chen and Olausson disagree; no reasoning-model test. |
| T2 | **Agent-written differential test as a selector across candidates** (model invents inputs, code gets real outputs). | S4, S7 | [C] | K12, K29; a28, d03, d06 | Helps without public tests, not with them; Reflexion case shows risk. |
| T3 | **First-wrong-step operator before rewrite.** | S5 / new O | [C] | K06, K30; b11, b12, d08, d09, d11 | No code study; own hints sometimes hurt. |
| T4 | **Round cap sweep (1, 2, 3, 5) at equal tokens.** | S5, S6 | [C] on the exact number | K09, K28 | Observational. |
| T5 | **Forced relocalise-and-restate after 2 failed edits vs continuing.** | S6 | [S] | K15; a26, b20 | Observational only. |
| T6 | **Runtime probing offered only after the first failed edits.** | S4 / new O | [S] | K07, K35; a19, d15 | Single group; margins small; strong models only. |
| T7 | **Outside stall check (rule trigger, different pass) once per stall.** | S6 | [S] | K32, K23; d13, d14, c22 | Cost 9x in one study; selection bias in the other. |
| T8 | **Rubber-duck explanation vs fix directly, on items with no executable check.** | O explain | [C] | K08; b03, a23, d21 | Gain concentrated in one model; never isolated from re-reading. |
| T9 | **Colleague framing of the agent's own draft (reasoning vs non-reasoning mode).** | G / S1 | [S] for reasoning models | K19, K33; b13, d12 | Probably moot for reasoning models; math only. |
| T10 | **Localiser agreement as a gate for deeper investigation.** | S3 | [S] | K16; a23 | Correlated samples (G4). |
| T11 | **Test coverage hint to the localiser.** | S3 | [S] | K17; a30, c27 | Needs a usable test suite. |
| T12 | **Strategy-level supervisor after a stall (abandon approach).** | S6 / new O | [S] | K23, K10; c22, c21 | One study; no matched compute. |
| T13 | **Fixed phases vs free-form loop at equal tokens.** | architecture | [S] | K14; a27, a29 | System comparison, not ablation. |

---

## 8. Concrete tests on our bench

Every test uses the same base model, the same token cap per item, and both arms at equal total tokens (count every call, including feedback, test generation and setup). Report pass rate on a held-out check, plus the broke-vs-fixed counts (right to wrong, wrong to right) for any arm that revises. Items need a real, hidden check. Sample sizes below are minimums; with 100 items a 5-point gap is about one standard error of 4.5 points, so smaller gaps are noise.

| # | Question | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| B1 | Does repair from real output beat a fresh sample? (T1) | 100+ code items with unit tests, plus ARC program-synthesis items with held-out examples; only items where the first draft fails the visible check | A: S5 repair from located failing output (1 round). B: a fresh S3 draw with the same tokens. C: mixed (half each). | Held-out pass rate on first-failed items, per 10k tokens | Chen/Olausson predict A about equal to B (ratio 0.97-1.05). Add repair-first only if A beats B by 5 points or more. |
| B2 | Real output vs self-check only (K01 control; also confirms the base) | Same items | A: revise with real failing output. B: revise with "check your answer" only. | Held-out pass rate; broke-vs-fixed | A above B by 8 points or more; B at or below no-revise. Confirms G2 on our stack. |
| B3 | Selector comparison (T2) | Items where we sample 8-16 candidates; some with no visible tests | A: model's own asserts. B: differential inputs with real outputs. C: held-out test (upper bound). D: majority vote. | Final held-out pass rate; false-pass rate per selector | B above D by 5 points; A has the highest false-pass rate. |
| B4 | First-wrong-step operator (T3) | Items with planted bugs where the first wrong step is known (mutate correct solutions) | A: rewrite with step named by the agent and the output cited. B: rewrite without. C: rewrite with the true step (ceiling). | Localisation accuracy (A vs truth); pass rate | Wire in only if localisation at least 70% and A beats B by 5 points. |
| B5 | Round cap (T4) | Items with a check | Caps 1, 2, 3, 5 on one draft, then restart from a fresh draft at the budget end | Marginal gain per round, pass rate at fixed tokens | Flat after round 2-3. Chen suggests round 1 holds most of the gain. |
| B6 | Stall rule (T5, T7) | Multi-step repair items (repo-style or long puzzles) where the agent can edit repeatedly | A: continue. B: after 2 failed edits force relocalise-and-restate. C: B plus a one-shot strategy critic by a different pass. | Pass rate; steps to solve | B above A by 3+ points on items with 2+ failed edits. C above B only on wrong-design items. |
| B7 | Keep-best checkpoint (A5) | Multi-edit items | A: submit the final draft. B: submit the best-scoring checkpoint. | Share of runs where final is worse than a past draft; pass rate | A worse than B in 10-20% of runs per d16. Costs 0 tokens. |
| B8 | Runtime probing (T6) | Hard multi-edit items | A: read-only plus pass/fail. B: probes always on. C: probes after 2 failed edits. | Pass rate | C above A by 5+ on hard items; no gain on easy items. |
| B9 | Explanation vs direct fix (T8) | Items with no executable check (open code review, spec-only) | A: explain then fix. B: fix directly. C: re-read then fix (control for re-reading). | Held-out judge-free check or hidden tests; explanation accuracy | A above C by 3+ points or drop it. |
| B10 | Colleague framing (T9) | Code items with an injected bug in the agent's own draft | A: draft shown as agent's own. B: shown as a colleague's. C: "Wait" appended. | Catch rate of the injected bug | Non-reasoning mode: B and C above A. Reasoning mode: near zero difference. |
| B11 | Fixed phases vs loop (T13) | Items spanning localise, repair, select | A: fixed three phases (localise, N candidates, select). B: free loop. | Pass rate | A at least equal at lower cost (Agentless: 32.00% at $0.70 vs 18.33% at $1.62). |
| B12 | Public vs private gap | A public item set and a fresh set made after the model cutoff with hidden tests | Same agent | Pass rate ratio | Expect private at half or less of public (d18, d19). Use as a sanity check on the bench. |

---

## 9. What does not transfer, and why

- **Pass-the-visible-tests success as truth.** On SWE-bench, passing the benchmark tests is not proof of a correct fix (a33, a32). Our own items need hidden stronger tests.
- **Self-Debug gains on Codex and GPT-3.5.** They come from a 2023 few-shot setting on short functions. Reasoning models gain about 0 to +3.4 and sometimes lose (d02).
- **"One debug turn equals 16 samples."** Counted in samples, not tokens, on Spider with Codex. At equal tokens Olausson finds 0.97x to 1.05x (a16).
- **Math and QA self-correction numbers (Huang, Tyen, Li, Samanta, Tsui, ProcessBench).** They support the principle (no outside signal means no gain) but are not code. The size of the effect on code is unknown. Tsui's blind spot and ProcessBench localisation figures come from math or logic with injected errors.
- **Model-only bug explanations.** A rubber-duck step helped only one model on one task and is about 20% accurate in AutoFL (b03, a23). Do not transfer it to settings with a real check.
- **SWE-bench resolve rates across papers.** Different model versions, cost accounting, tool versions, leaky items. A system comparison (Agentless vs SWE-agent) is not an ablation.
- **Outside monitor results.** The 9x cost (d13) breaks equal-token. d14 is selection biased.
- **Human feedback (Olausson 52.6%).** We have no human in the loop. It only shows that diagnosis is the bottleneck; a stronger model might stand in, but a single-model scaffold cannot copy it (b07).
- **Multi-agent frameworks.** MAST (b27) is about multi-agent frameworks; our schema is single agent. Only the verification and termination share is relevant.
- **Debugger tools.** Our bench items are puzzle-sized. pdb-style probing helped on repo bugs for strong models and not on Aider-size tasks (o3-mini 95.2 vs 94.2).
- **Test generation without a public test.** CodeMonkeys-style selection loops (about 2,300 USD for 500 items) were not run at equal cost against plain sampling. Only the cost shares are usable (selection under 10% of total).

---

## 10. Open questions

1. At equal total tokens, does test-guided repair beat best-of-N plus test-based selection for a current reasoning model? (Chen vs Olausson; no matched modern test.)
2. Does an explicit "name the first wrong step, with evidence" operator raise repair rates for code, and how accurate is our agent at that naming?
3. What round count or failed-edit count should force relocalisation or a new approach, and does that beat continuing at equal tokens?
4. When is an agent-written test a good filter and when a bad stop signal? We need a false-positive-versus-gain curve across tasks.
5. Does re-presenting the draft as external text fix the self-output blind spot on code for reasoning models?
6. Does the self-debug gain depend on base-model strength once models are strong?
7. Do runtime probes beat reading code plus pass/fail on our task types?
8. What share of unresolved failures are wrong design versus slip, and does an abandon-approach operator or a strategy supervisor help on the wrong-design share (Liu 22.2%)?
9. Does rubber-duck explanation add anything beyond re-reading when a test exists, and does a wrong explanation hurt?
10. How do we build held-out, hidden-test items cheaply, given leakage and weak tests?
11. Is the "iterative gain" (Li, 60.8-67.9%) real correction or re-solving? Would a fresh sample at equal tokens match it?
12. Does an outside stall monitor still help when it is the same model with a different prompt?

---

## 11. Sources

[V] opened (PDF or HTML text read in this run or the cross-check). [M] snippet only. Re-opened by the cross-checker: Chen, Olausson, Huang, SWE-agent, Agentless, LDB, Reflexion, Tyen, PatchDiff, plus in the gap pass SWE-Bench+, AutoFL, Tsui, Majgaonkar. The following were not re-opened by the cross-checker and their numbers are single-read: SWE-Bench+ (re-opened in gap pass, now confirmed), Kang (confirmed in gap pass), AutoCodeRover, DEI, Liu failures study, Cemri, MINT, CodeAct, Self-Refine, Kamoi.

| Source | Marker | URL |
|---|---|---|
| Chen, Lin, Schaerli, Zhou (2023/2024) Teaching Large Language Models to Self-Debug | [V] | https://arxiv.org/abs/2304.05128 |
| Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet | [V] | https://arxiv.org/abs/2310.01798 |
| Shinn et al. (2023) Reflexion | [V] | https://arxiv.org/abs/2303.11366 |
| Madaan et al. (2023) Self-Refine | [V] | https://arxiv.org/abs/2303.17651 |
| Olausson et al. (2024) Is Self-Repair a Silver Bullet for Code Generation? | [V] | https://arxiv.org/abs/2306.09896 |
| Zhong, Wang, Shang (2024) Debug like a Human: LDB | [V] | https://arxiv.org/abs/2402.16906 |
| Kang, An, Yoo (2024) AutoFL | [V] | https://arxiv.org/abs/2308.05487 |
| Yang et al. (2024) SWE-agent | [V] | https://arxiv.org/abs/2405.15793 |
| Xia et al. (2024) Agentless | [V] | https://arxiv.org/abs/2407.01489 |
| Zhang et al. (2024) AutoCodeRover | [V] | https://arxiv.org/abs/2404.05427 |
| Jimenez et al. (2024) SWE-bench | [V] (abstract, appendix, c16 results) | https://arxiv.org/abs/2310.06770 |
| Aleithan et al. (2024) SWE-Bench+ | [V] | https://arxiv.org/abs/2410.06992 |
| Wang, Pradel, Liu (2025/2026) Are Solved Issues in SWE-bench Really Solved Correctly? | [V] | https://arxiv.org/abs/2503.15223 |
| Wang et al. (2024) MINT | [V] (abstract only) | https://arxiv.org/abs/2309.10691 |
| Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location | [V] | https://arxiv.org/abs/2311.08516 |
| Tsui (2026) Self-Correction Bench | [V] | https://arxiv.org/abs/2507.02778 |
| Kamoi et al. (2024) When Can LLMs Actually Correct Their Own Mistakes? | [V] (abstract and introduction) | https://arxiv.org/abs/2406.01297 |
| Gou et al. (2024) CRITIC | [V] (introduction only, no numbers) | https://arxiv.org/abs/2305.11738 |
| Cemri et al. (2025) Why Do Multi-Agent LLM Systems Fail? | [V] | https://arxiv.org/abs/2503.13657 |
| Wang et al. (2024) Executable Code Actions Elicit Better LLM Agents (CodeAct) | [V] (abstract and method) | https://arxiv.org/abs/2402.01030 |
| Pan et al. (2024) Automatically Correcting LLMs: Surveying the Landscape | [V] (taxonomy only) | https://arxiv.org/abs/2308.03188 |
| Zhang et al. (2024) Diversity Empowers Intelligence (DEI) | [V] | https://arxiv.org/abs/2408.07060 |
| Liu et al. (2025) An Empirical Study on Failures in Automated Issue Solving | [V] | https://arxiv.org/abs/2509.13941 |
| Majgaonkar et al. (2025) Understanding Code Agent Behaviour | [V] | https://arxiv.org/abs/2511.00197 |
| SWE-ABS (2026) Adversarial Benchmark Strengthening | [M] (not used in claims) | https://arxiv.org/abs/2603.00520 |
| Agent behaviour study, repetitive loops (2026) | [M] (not used in claims) | https://arxiv.org/abs/2604.02547 |
| Mehmet can (2026) Falsification, Not Exposure | [V] | https://arxiv.org/abs/2606.31511 |
| Li et al. (2025) S*: Test Time Scaling for Code Generation | [V] | https://arxiv.org/abs/2502.14382 |
| Song, Raiman, Catanzaro (2024) Effective LLM Debugging with Best-first Tree Search | [V] | https://arxiv.org/abs/2407.19055 |
| Ehrlich et al. (2025) CodeMonkeys | [V] | https://arxiv.org/abs/2501.14723 |
| Brown et al. (2024) Large Language Monkeys | [V] | https://arxiv.org/abs/2407.21787 |
| Li (2026) Decomposing LLM Self-Correction | [V] | https://arxiv.org/abs/2601.00828 |
| Samanta et al. (2026) Structure Enables Effective Self-Localization of Errors (Thought-ICS) | [V] | https://arxiv.org/abs/2602.02416 |
| Zheng et al. (2025) ProcessBench | [V] | https://arxiv.org/abs/2412.06559 |
| Gandhi et al. (2025) When Agents go Astray (SWE-PRM) | [V] | https://arxiv.org/abs/2509.02360 |
| Liu et al. (2026) Process-Centric Analysis of Agentic Software Systems | [V] | https://arxiv.org/abs/2512.02393 |
| Yuan et al. (2025) debug-gym | [V] | https://arxiv.org/abs/2503.21557 |
| Kim et al. (2026) Coherence Collapse | [V] | https://arxiv.org/abs/2603.24631 |
| Zhang et al. (2025) SWE-bench Goes Live! | [V] | https://arxiv.org/abs/2505.23419 |
| Deng, Da et al. (2025) SWE-Bench Pro | [V] | https://arxiv.org/abs/2509.16941 |
