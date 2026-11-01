# Self-correction: deep document

*Subfield C01.05. Source files in this folder: evidence_a-d.jsonl (a01 to d21), claims.jsonl (C01.05-K01 to K36), critique.md. Claim ids are written K01 to K36. Evidence ids are a01 to d21. Status words follow claims.jsonl: established, single-source, contested.*

## 1. What it is

Self-correction means a language model changes its own earlier answer after looking at it again. The "look" can be of several kinds. The kind decides almost everything.

- **Intrinsic.** The model gets only its own answer and a prompt like "review and fix". No tool, no label, no second model.
- **Extrinsic with a sound check.** Code runs the answer: unit tests, a plan validator, a recomputation, a constraint list. The model sees the real failing output.
- **Extrinsic with a weak check.** The check can be wrong: a model-written test, a model judge, a retrieval snippet.
- **Oracle.** Code that knows the gold answer decides whether to stop or retry. This is not self-correction. It measures only what a perfect stopper would give.
- **Trained.** The model was fine-tuned or RL-trained to correct itself (RISE, SCoRe, S2R). Prompting alone does not give this.

Three skills are bundled in the word.

1. **Detect**: is there an error?
2. **Locate**: where is it?
3. **Fix**: given the place, write a better answer.

The research (K03, K21) shows these have very different difficulty. Detect and locate are hard for a model that wrote the answer. Fix is easy once the place is known. A fourth issue is **flipping**: how often a correct answer is changed into a wrong one. This decides whether a revise step has net value.

Why it matters for our agent. Guardrail G2 says revise only from real output, located by code. State S5 is the revise step. This subfield is the evidence base for G2 and S5: when does a revise step pay, what signal must feed it, how many rounds, and what to do when the signal can be wrong.

Scope note. Debate is covered only as a comparison (K12, G9). Test-time compute scaling, metareasoning and overthinking are other subfields in this run. Here we only note links.

## 2. History and theories in depth

**Pre-2023: learned correctors and critics.**
- Welleck et al. (2022, a18) trained a separate corrector model. GPT-Neo 1.3B on GSM program synthesis went from 8.57% to 21% (24% when only wrong outputs were corrected). Multiarith 98 to 99%. The corrector was trained, with a check available.
- Saunders et al. (2022, a19) used model critiques to help human raters. Assisted humans found about 50% more flaws, also in deliberately misleading answers. Larger models self-critique better. Here the critique serves a human, not the model's own revision.

**2023: the optimistic wave.** Prompted loops reported large gains.
- RCI (Kim et al., a12): GSM8K zero-shot 77.95 to 85.43. The loop stopped when the output matched the ground truth, so the gain was oracle-assisted.
- Self-Refine (Madaan et al., a07, b11): about 20% absolute average gain across 7 tasks. Gains were in style and constraint tasks. Math was flat (GPT-4 92.9 to 93.1).
- Reflexion (Shinn et al., a10): ALFWorld 130 of 134, HumanEval 91 vs 80. It used an external pass/fail signal from the environment or from tests.
- CRITIC (Gou et al., a17): tool-interactive critique, about +7.7 F1 on QA and +7.0 points on math for ChatGPT.
- Self-Debug (Chen et al., a20, d13): execution feedback, up to +12 with unit tests.

**Late 2023 to mid 2024: the sceptical wave.** Several groups looked at what the loops really did.
- Huang et al. (a01 to a06): without oracle labels, accuracy fell on all three reasoning sets (K01). Gains in earlier papers came from oracle stop signals (K02).
- Stechly et al. (a15) and Valmeekam et al. (a16): on colouring and Blocksworld, GPT-4 cannot check its own work (K04). A sound external checker is what helps (K05).
- Tyen et al. (a13): models cannot find the error but fix it well given the location (K03).
- Kamoi et al. (a25, d15): a critical survey. It lists "unfair settings": oracle stops, weak first prompts, unequal compute against baselines. It finds no fair prompted success in general tasks.

**Mid 2024 onward: training.** RISE (a24), SCoRe (a23), S2R (d16) train the model to correct itself. SCoRe turned a -11.2 change into +4.4 on MATH500 (K16). Plain long-CoT SFT of similar size nearly matched S2R (80.2 vs 81.6), so the gain is mostly training on long reasoning (K30).

**2025 to 2026: reasoning models and budgets.**
- Reasoning-trained models reflect on their own steps. Tsui (a28) shows the "self-correction blind spot" in non-reasoning models and its removal by a "Wait" cue or by reasoning training (K13, K14).
- s1 budget forcing (c19) extends thinking with "Wait" (K15).
- The "aha moment" is disputed (b23, K24).
- Newer tests measure revise vs think-longer at equal tokens (d06, K27), neutral revise on current models (d09, d05), and gated loops (d10, d11).

**Theories offered for why prompted self-correction fails or works.**

| Theory | Claim | Support | Status |
|---|---|---|---|
| Flip noise | A second look changes answers at random. Changes from right to wrong outnumber the reverse when most answers are right. | Huang (a05): GPT-3.5 keeps its GSM8K answer only 74.7% over two rounds. Zhang (b21, d05): 81.3% of answers change more than 6 times in 10 rounds. Stav (d09). | established (K18) |
| Verification gap | Revision pays only when checking is much easier than generating. | Song (b22, d11); CoVe (a22); Stav SAT vs HLE (d09). | single-source for the scaling claim (K23); the task pattern is established (K35) |
| Blind spot (self-attribution) | The model does not fix errors in its own turn that it fixes in the user's turn. | Tsui (a28, d20). | single-source (K13), contested on cause (K34) |
| Self-preference | Models favour their own text, and recognise it (GPT-4 73.5%). | Panickssery (d19). | single-source, links to K33 |
| Feedback bottleneck | The critic fails first: 33% wrong error location and 61% wrong fix suggestion in Self-Refine failures. | Madaan (b12); Olausson (b20): 52.6% repair with human feedback vs 33.3% with GPT-4's own. | established (K09) |
| Overthinking / prompt bias | A critical prompt tells the model "something is wrong", so it changes right answers. | Huang (a04), Li (d01), Zhang (c16). | partly supported (K20) |
| Spectral theory | Blind spot occurs iff a spectral radius is at least 1. | Petrova and Vejsiu (d21). Theory only, no new data. | do not rely on it |

## 3. Core findings with exact numbers

Models are the 2023-era ones unless the row says otherwise. N is small in many studies (100 to 200 items, no error bars).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Intrinsic revision lowers accuracy on reasoning | GPT-3.5 CSQA 75.8 to 38.1 (1 round, 3 calls) to 41.8 (2 rounds, 5 calls); GSM8K 75.9 to 75.1 to 74.7; HotpotQA 26.0 to 25.0 to 25.0. GPT-4 GSM8K 95.5 to 91.5 to 89.0; CSQA 82.0 to 79.5 to 80.0; HotpotQA 49.0 to 49.0 to 43.0 | Huang 2024 (a02, c01) | established (K01) |
| Same on other models | GPT-4-Turbo GSM8K 91.5 to 88.0 to 90.0; CSQA 84.0 to 81.5 to 83.0. Llama-2 GSM8K 62.0 to 43.5 to 36.5; CSQA 64.0 to 37.5 to 36.5 | Huang (a03) | established |
| Prompt wording changes the size of the loss, not its sign | GPT-4-Turbo GSM8K base 91.5: prompts give 88.0/90.0, 90.0/90.0, 91.0/91.0. CSQA base 84.0: 81.5/83.0, 74.5/81.0, 81.5/83.5 | Huang (a04) | established |
| Oracle stop gives big gains that disappear without it | GPT-3.5 GSM8K 75.9 to 84.3; CSQA 75.8 to 89.7; HotpotQA 26.0 to 29.0. GPT-4 GSM8K 95.5 to 97.5; CSQA 82.0 to 85.5; HotpotQA 49.0 to 59.0 | Huang (a01, c02); critique.md item 1 | established (K02) |
| Self-Refine gain depends on a weak first prompt | CommonGen-Hard: Madaan prompt 44.0 to 67.0; Huang's stronger first prompt 81.8 to 75.1 | Huang (b04, c03) | established (K11) |
| Self-Refine on math is flat | GPT-4 92.9 to 93.1; ChatGPT 74.8 to 75.0; GPT-3.5 64.1 to 64.1; critic says "looks good" on 94% of math items. Oracle feedback: GPT-3 +4.8, GPT-4 +0.7 | Madaan (a07, a08) | established (K10) |
| Self-Refine gains are in style and constraint tasks | Dialogue 25.4 to 74.6; sentiment reversal 3.8 to 36.2; code readability 15.0 to 45.0; code optimisation 27.3 to 36.0. Feedback ablation: sentiment 43.2 specific vs 31.2 generic vs 0 none | Madaan (a07, a09, b11) | established (K10) |
| Self-Refine failure causes | 33% wrong error location; 61% wrong fix suggested; 6% bad execution of good feedback | Madaan (b12) | single paper |
| Debate is a voting effect | GSM8K GPT-3.5: standard 76.7; SC 3/6/9 = 82.5/85.3/88.2; debate 83.2 (round 1) and 83.0 (round 2). The table's response-count column is unclear in the paper | Huang (a06, b03); critique.md item 3 | established (K12) |
| Finding the error is the hard part | BIG-Bench Mistake, GPT-4: 39.80 (direct trace), 52.87 (direct step), 43.40 (CoT step). GPT-3.5-Turbo 10.44/14.78/14.31. PaLM 2 Unicorn 17.09/23.67/24.65 | Tyen (b05) | established (K03) |
| Fix given location helps more than it hurts | Backtracking with true location: correct traces broken 0.00 to 11.43 points; wrong traces fixed +18.04 to +43.92. Random location fixes only +10.59 to +21.57. Word sorting confirmed: -11.11 / +23.53 | Tyen (b06, c09); critique.md item 5 | established (K03) |
| Strong detectors have low recall | 12 LLMs on ReaLMistake; stronger models have higher precision, lower recall; several score below a random baseline in F1. Human F1 95.7 | Kamoi (a26, b10) | established (K21) |
| Reasoning models detect step errors far better | ProcessBench average F1: o1-mini 87.9, QwQ-32B-Preview 71.5, GPT-4o 61.9 (3,400 cases). o1-mini per set about 93.2 / 88.9 / 87.2 / 82.4 | Zheng (b25, d04) | established (K21, K31) |
| Self-verification of colouring fails | 100 instances: baseline 16%; LLM self-critique loop 1 of 100; of 100 optimal colourings only 2 accepted; of 500 colourings (118 correct) it said 30 correct and was right 5 times; 40 instances with an optimal colouring, never recognised | Stechly (a15, b13) | established (K04) |
| Self-verification of plans fails | Generator 40/100; LLM+LLM 55/100 (3.48 iterations); LLM+VAL sound 88/100 (4.18). Verifier accuracy 61/100: 54 of 55 valid accepted, 38 of 45 invalid accepted (84.45% false positive) | Valmeekam (a16, c11) | established (K04) |
| With a sound checker, feedback content matters little | Colouring about 40% across feedback types. Blocksworld binary 37/50 vs 43/50 with first error | Stechly (a15), Valmeekam (a16) | established (K05) |
| Sound verifier equals plain sampling in colouring | Verified backprompting about 40% = top-n (n=15, t=1.0) 40% | Stechly (a15) | single-source (K06) |
| Execution feedback pays | Self-Debug MBPP: Codex 61.4 to 69.4 (UT), GPT-3.5 67.6 to 72.2, GPT-4 72.8 to 80.6. TransCoder GPT-4 77.3 to 88.8. Without execution Codex simple 57.6 (below 61.4). Spider: one greedy sample plus debug matches 16 samples; one turn gives most of the gain | Chen (a20, d13) | established (K07, K35) |
| Self-repair vs fresh samples | GPT-4 on APPS: up to 8% better than baseline; GPT-3.5 marginal. Human explanation 52.60% vs GPT-4 self-explanation 33.30%. The 1.05x pass@20 and 0.97x pass@22 figures were not verified | Olausson (a21, b20); critique.md item 12 | established (K09) |
| CRITIC: tool helps in one model, not in another | ChatGPT +7.7 F1 over QA; +7.0 math. text-davinci-003 GSM8K 70.1 / 72.2 (full) / 68.3 (no tool). ChatGPT GSM8K PoT 72.5, no-tool 78.2 (+5.7), full 77.0 (+4.5) | Gou (a17, b19, c08) | contested (K07 vs K08) |
| Reflexion: external signal required; bad signal costs | ALFWorld 130/134; HumanEval 0.80 to 0.91 (test FP 0.01); MBPP 0.80 to 0.77 (FP 0.16, FN 0.59). Baselines without memory solved none of the trial-1 failures (100 HotPotQA questions) | Shinn (a10, a11, c07, d18) | established (K26) |
| Resampling with imperfect tests has a ceiling | False-positive rate falls as single-sample accuracy rises; best K about 5 at cost ratio 4 | Stroebl (d03) | single-source, in K26 |
| Training fixes the sign | MATH500 Gemini 1.5 Flash: base 52.6 to 41.4 (-11.2); Self-Refine -1.0; STaR +0.4; Pair-SFT +1.8; SCoRe 60.0 to 64.4 (+4.4). Right-to-wrong 15.8% to 1.4%. HumanEval Gemini 1.0 Pro SCoRe +12.2 | Kumar (a23, b17, c12) | established (K16) |
| SCoRe fix-rate numbers are inconsistent | Text says base wrong-to-right 9.5% vs 14.5% SCoRe; table says base 4.6% | Kumar; critique.md item 9 | contested (K17) |
| RISE | GSM8K 5 turns: Llama2-7B +17.7, Mistral-7B +23.9; GPT-3.5 only +4.6. MATH: +4.6, +11.1. Headline numbers use oracle early stop | Qu (a24, b18, c13) | contested (K17) |
| Training explains most of S2R | Qwen2.5-Math-7B MATH500: base 51.0, S2R-BI 81.6, original-solution SFT 58.0, long-CoT SFT 80.2 | Ma (d16) | established (K30) |
| CoVe works on decomposable facts | FACTSCORE 55.9 to 71.4; MultiSpanQA F1 0.39 to 0.48; Wikidata lists 17% correct as listed, 70% when each item verified alone | Dhuliawala (a22) | contested for reasoning (K22) |
| CoVe breaks correct reasoning answers | Sonnet 4.5: CoVe broke 28.9% of correct multistep arithmetic, 35.6% word sorting, 51.1% Dyck. GPT-4o best on arithmetic (95.0 vs DISC 54.0) | Yin DISC (d12) | contested (K22) |
| Blind spot | 14 open non-reasoning models, average 64.5%. Claude 3.5 Haiku 52.5%, Sonnet 4 41.4%. "Wait" cuts it 89.3%; fine-tuning on 5,306 traces cuts it 76.0% | Tsui (a28, b15, c18) | single-source (K13) |
| Wait vs reasoning model | Mean accuracy base / +Wait / reasoning: DeepSeek-V3 0.567/0.902/0.908; phi-4 0.325/0.701/0.707; Qwen3-14B 0.117/0.868/0.843; Qwen3-32B 0.045/0.793/0.894; Qwen3-235B 0.328/0.856/0.876 | Tsui (b16) | single-source (K14) |
| Budget forcing | s1-32B AIME24 50.0 to 56.7; MATH500 92.6 to 93.0 | Muennighoff (c19) | single-source (K15) |
| Neutral prompt at T=0 gives small gains (dissent) | GPT-4 MMLU 83.66 to 84.76; CSQA GPT-3.5 75.92 to 76.00, GPT-4 84.11 to 84.60; HotpotQA GPT-3.5 31.00 to 47.00, GPT-4 88.00 to 89.00. First 200 questions, no error bars | Liu (c14); critique.md item 13 | contested (K19) |
| Confidence gating cancels the loss | GSM8K-100 GPT-3.5: critique hurts confident answers 82.75 to 77.35, helps unconfident 27.69 to 39.23. 5-set average GPT-3.5-0613 standard 70.3 / critical 66.1 / IoE 73.0; GPT-4 85.1 / 82.5 / 86.6 | Li (c15, d01) | single-source (K20) |
| Neutral "are you sure" still flips 2025 models | o1-mini, 4o, V3, R1 overturn correct answers. Llama-3.1-8B -20.4 points, 58.8% overturned. Re-attaching the question: +3.2 to +4.9 ACC, 5.3 to 10.9 fewer overturned | Zhang (c16, d05) | single-source (K32) |
| 2025-26 models: revision pays where checking is easy | T=0, one run. SAT: Mistral Large 34.62 to 64.96; Haiku 4.5 75.64 to 93.59; DeepSeek V3.1 78.63 to 92.74; Gemini Flash Lite 60.68 to 82.91; Gemini 3 Pro 97.0 to 100. C2W at most 2.1% on SAT, up to 13.25% on BBEH/HLE. Gemini Pro HLE 10.56 fixed vs 9.32 broken | Stav (d09) | established (K35, K18) |
| Think longer matches check (4B model) | Qwen3-4B MATH500: 4,096 limit 59.0; always continue 72.0; always verify 75.5 (2.2% harmful flips); selective verify 76.3 (1.0%, 8,125 tokens); first-solve budget 8,192 gives 76.0 with 28% fewer tokens. GSM8K 94.54 vs 94.47. 45.4% truncated at 4,096. CommonsenseQA always-verify -4.17 | Dip (d06) | single-source (K27) |
| Gated loop with a separate strong checker | BIG-Bench Mistake Sonnet 4.5: DISC 81.6% (1,195 improved, 8 degraded), CoVe 58.6, Self-Refine 49.6. Starts from 15% correct traces. GPQA: nano self 54.0 to 54.0; strong verifier+judge on nano 54.0 to 71.6 (+34 net); gpt-5.2 self-check 75.3 to 79.3 (+8) | Yin (d10, d11) | single-source (K33) |
| Round cap | DISC with gate: net +22 (K=1), +34 (K=3), +35 (K=8); without gate I:D falls 2 to 4x. Self-Debug: gain after turn 1 within 0.1%. Song: saturation in 2-3 rounds | Yin (d11), Chen (d13), Song (b22) | single-source (K32), K23 |
| Fine-tuned revision needs a selector | PaLM 2-S* MATH: naive use turns about 38% of correct answers wrong; verifier or sequential vote over the chain fixes it; mix of sequential and parallel up to 4x less compute | Snell (d02) | established (K29) |
| Verify-then-select beats plain voting | Gemini 1.5 Pro: AIME Verification@200 8/15 vs Consistency@200 4/15; MATH 467 vs 460 of 500; LiveBench Math 135 vs 118 of 200; LiveBench Reasoning 97 vs 75 of 140 | Zhao (d14) | single-source (K36) |
| Refine-then-vote for weak models | N=8, D=4: Qwen2.5-1.5B average 25.67 vs Maj@8 13.21, RM best-of-8 14.95. Not compute-matched | Bilal (d07) | single-source (K28) |
| Route by disagreement | Qwen3-8B, 7 math benchmarks: single 61.3, majority 68.9, routing 75.8 (accept if consistent, vote if moderate, rewrite and re-solve if high). Budgets matched at 4 and 8 samples | Lin (d08) | single-source (not in claims.jsonl) |
| Shorter chains win | Shortest of several chains up to 34.5% more accurate than the longest; short-1@k matches majority at low compute with up to 40% fewer thinking tokens | Hassid (d17) | single-source |
| Reflection words do not track accuracy | R1-Zero reflects more, reflection not positively correlated with accuracy | Liu (b23) | contested (K24) |

## 4. Mechanisms and models

Each mechanism below is written so an engineer can build it.

### 4.1 Measure first: the revise ledger
Every revise step logs these numbers. Without them nothing below can be judged (K18, critique.md c27, Kamoi section 8).
- acc@t1 (before revise), acc@t2 (after), delta.
- right-to-wrong count, wrong-to-right count (per item, by gold or by checker).
- tokens used by the revise step.
- best-of-n accuracy with the same total calls.

Rule from Huang and Kamoi: compare against the strongest first-attempt prompt, and never let the gold answer decide stopping.

### 4.2 Checked revise (extrinsic with a sound check)
```
draft = solve(task)
for round in 1..R:                       # R = 1 or 2
    result = run_check(draft)            # code: tests, validator, recompute
    if result.pass: return draft
    line = model("Name what is wrong in one line", task, draft, result.failing_output)
    new = model("Fix it", task, draft, line, result.failing_output)
    if run_check(new) is at least as good as run_check(draft): draft = new   # keep best so far
return best_so_far
```
Evidence: Self-Debug (d13), Valmeekam LLM+VAL 88/100 (a16), Reflexion (a10). Facts that shape the loop:
- Binary pass/fail was close to full error text when the checker is sound (K05). Test a bare retry before building elaborate critiques.
- One debug turn gives most of the gain (Self-Debug: later turns within 0.1%).
- The checker must be sound. A model-written test with 16% false positives made Reflexion lose to no loop (d18). Weight a pass by test coverage, and cap retries near 5 (Stroebl, d03).
- Always keep best-so-far, so a bad revision cannot lower the result (K29).

### 4.3 Locate then fix (Tyen)
```
step = locate_first_wrong_step(task, trace)       # code, process checker, or model
for try in 1..8:
    new_step = model(regenerate step, temperature=1)
    if new_step != step: break                      # must differ
trace2 = continue_from(trace[:step] + new_step)
```
Evidence: b06 and c26. True location fixes +18.04 to +43.92 and breaks 0 to 11.43; random location fixes +10.59 to +21.57. GPT-4 locates only 52.87 with the best prompt (b05). A reasoning model does much better (o1-mini F1 87.9, d04). A trained classifier on held-out tasks ranged -0.67 to +22.59 points over a 3-shot baseline (b07). Locate quality is the limit. Location from code (a failing test line, a diff against a recomputation) beats a model guess.

### 4.4 Gate the revise step
Five gates have evidence. Use them to cut right-to-wrong flips.
- **Signal gate.** Revise only if a check fails (G1/G2). Mechanically the safest rule.
- **Confidence gate (If-or-Else).** Prompt: keep the answer if very confident, otherwise update. Gains over no revise were 1 to 3 points, single run (d01).
- **Judge gate (DISC).** A verifier lists errors. A separate judge answers binary: is this error real? Only then correct. Net +22 to +35 over 1 to 8 iterations (d11). The judge and verifier must be strong, and a different model from the generator works best (+34 vs +8 net, d11).
- **Disagreement gate (Lin).** If independent attempts agree, accept. If moderately split, vote. If split heavily, rewrite the problem and solve again (d08).
- **Selective verify (SEVRA).** Verify only when the first answer looks uncertain. Harmful flips 2.2% down to 1.0% (d06).

### 4.5 Cue-based check ("Wait")
Append a short continue-checking cue ("Wait") before the final answer. Tsui: the blind spot falls 89.3%, mean accuracy up 156% on injected errors in non-reasoning models (c18). Reasoning-trained models reach the same level without the cue (b16). Budget forcing uses the same idea to extend thinking (c19, AIME24 +6.7). Hypothesis (a): SFT data has almost no correction sequences, so the cue activates a behaviour the model has but does not start (d20). Hypothesis (b): a "conversational-role direction" in activations separates user text from assistant text. The cue test uses injected errors, not natural ones, and has not been run in a scaffold.

### 4.6 Re-present the draft as external
Tsui's blind spot is tied to the chat role header: the same error in the user turn is fixed, in the assistant turn it is not (d20). A scaffold version: in S5, put the draft in a user message as "a solution from another solver", with the task restated at the end (Zhang: re-attaching the question gave +3.2 to +4.9 ACC, d05). Counter-evidence: models recognise their own text (GPT-4 73.5%, d19), so a relabel may be seen through. A style rewrite of the draft is one way to remove the cue. None of this has been tested at equal tokens (critique GAP 2).

### 4.7 Isolated item verification (CoVe)
```
draft = solve(task)
claims = split(draft)                    # independent checkable parts
for c in claims: answer_c = model(question_about(c))   # draft hidden
revised = model(task, draft, answers)
```
Works on lists and fact claims (Wikidata 17% to 70%, a22). On multi-step reasoning it can break correct answers (28.9% to 51.1% on BIG-Bench Mistake tasks with Sonnet 4.5, d12). Use it only when the answer decomposes into independent claims.

### 4.8 Verify across drafts
Sample several drafts, have the model verify each, select by verification score (d14). Gemini 1.5 Pro: Verification@200 beat Consistency@200 on four sets; comparing across drafts helps locate errors. This is a selection operator, not a revision. It fits S7 more than S5.

### 4.9 Memory of failures (Reflexion)
After a failed trial, the model writes a short reflection; 1 to 3 reflections go into the next attempt (a11). Plain retries without memory solved none of the trial-1 failures on HotPotQA; Reflexion did. The trigger was an external pass/fail. Caution: a false pass ends the loop on a wrong answer (K26).

### 4.10 Why training works and prompting does not
Training (SCoRe) rewards the improvement between try 1 and try 2, and a first stage keeps the first try near the base model's, so the second try learns to repair rather than to ignore (a23). Result: right-to-wrong 15.8% to 1.4%. Prompting cannot change that prior. For a scaffold-only agent, the lesson is to supply signals from outside, not to hope for self-detection (K30).

## 5. What holds up

**Replicated and robust.**
- Intrinsic prompted revision of a reasoning answer does not help and often hurts, across GPT-3.5, GPT-4, GPT-4-Turbo, Llama-2 (Huang), and again in 2025 models under a neutral "are you sure" (Zhang). Independent sources: 3 (K01, K18).
- Oracle stops inflate published gains (K02). Weak first prompts inflate them too (K11).
- Self-verification on planning and colouring fails; a sound checker works (Stechly, Valmeekam, K04).
- Where a cheap sound check exists, revision pays: code with tests, SAT constraints, recomputable arithmetic (K35). For 2025-26 models this gain is large (Haiku 4.5 SAT 75.64 to 93.59).
- Locating is the weak step; fixing is strong (K03).
- Debate is not better than voting (K12; matches G9).
- Fine-tuned revision needs a selector: naive use turned 38% of correct answers wrong (K29).

**Failed or contested.**
- Liu 2024 (c14) finds small gains with a neutral prompt at T=0, against Huang. Differences: prompt, temperature, model version (gpt-3.5-0613 vs 0301), grading. Liu's GPT-4 HotpotQA baseline is 88 vs Huang's 49, so the two cannot be compared directly. Not resolved (K19).
- CRITIC tool vs no tool: tool better for text-davinci-003, no-tool better for ChatGPT GSM8K (78.2 vs 77.0). Model-dependent (K08).
- Chain-of-Verification works on facts, breaks reasoning (K22).
- SCoRe's own fix-rate numbers disagree (4.6% table, 9.5% text). RISE headline uses an oracle early stop (K17).
- The "aha moment" as an RL-learned skill is disputed (K24).
- Self-attribution cause: authorship or role? The author says role. Not tested in a scaffold (K34).

**Moderators (what decides the outcome).**

| Moderator | Direction | Evidence |
|---|---|---|
| Sound external check | large gain | a16, d13, d09 |
| Check cheaper than generation | gain | d09 (SAT vs HLE), a22, b22 |
| Task has independent claims | CoVe helps | a22, d12 |
| Weak first prompt | inflates measured gain | b04 |
| Oracle stop | inflates measured gain | a01, a12, b18 |
| Prompt says "find the error" | induces flips | a04, d01 |
| Temperature 0 and neutral prompt | smaller loss, maybe tiny gain | c14, d09 |
| Model has reasoning training | blind spot gone, detect better | b16, b25 |
| Checker is a different, stronger model | more fixes (+34 vs +8 net) | d11 |
| Model-written tests | false pass 16% on MBPP | d18 |
| Number of rounds | beyond 1 to 3, flips dominate unless gated | d05, d11, d13 |
| Small model | needs a strong verifier | c17 (K25) |
| Item already correct and confident | critique hurts | d01 |

**Interventions that worked.** Real tests or validators; located errors; "Wait" cue (injected errors); judge gate; question re-attached to the refine prompt; confidence gate (small); training; verify-then-select across many drafts; a larger first-solve budget (4B).

**Interventions that did not.** Self-critique by the same model with no signal; debate; extra rounds without a gate; model-written tests as sole gate; feedback elaboration when a sound checker exists (binary was enough); CoVe on multi-step arithmetic and word sorting.

**Weak spots in the evidence** (critique.md).
- Most hard numbers are from 2023 models. 2025-26 data come from a few 2026 preprints (d05, d06, d09, d10, d11), mostly single-run.
- Many studies use 100 to 200 items with no error bars.
- The independent source count is lower than the evidence line count: Huang supplies 14 lines.
- Planning and colouring tasks are synthetic.
- No study measures self-correction at equal tokens against best-of-n for frontier long-CoT models.

## 6. Language models

**Behaviour by period.**

| Period / model class | Intrinsic revise, reasoning | With sound check | Finding errors |
|---|---|---|---|
| 2023 GPT-3.5, GPT-4, Llama-2 | down 0 to 37 points (CSQA 75.8 to 38.1; Llama-2 GSM8K 62.0 to 36.5) | up (Self-Debug +8 to +12; VAL 40 to 88) | poor (GPT-4 52.87 at best) |
| 2024 trained (SCoRe, RISE, S2R) | up (SCoRe +4.4; Gemini Flash base -11.2) | not the point | trained to detect |
| 2025-26 non-reasoning (V3, Haiku 4.5, Mistral Large) | mixed: large gain on SAT, small or negative on HLE; blind spot large without cue | up | moderate |
| 2025-26 reasoning (o1-mini, R1, Qwen3 thinking) | neutral "are you sure" still overturns correct answers; blind spot nearly gone | up | strong (ProcessBench F1 87.9) |

**What changed behaviour, and by how much.**
- *A sound checker*: 40 to 88 on Blocksworld (a16); MBPP 72.8 to 80.6 for GPT-4 (d13); SAT +15 to +34 points for 2025 models (d09).
- *Reasoning training*: blind spot accuracy 0.567 to 0.908 (DeepSeek-V3 vs reasoning); locate F1 61.9 to 87.9 (d04).
- *A cue*: "Wait" cuts the blind spot 89.3%.
- *Fine-tuning*: SCoRe flips a -11.2 loss into +4.4; fine-tuning on correction traces cuts the blind spot 76.0%.
- *A different, stronger checker*: +34 vs +8 net (d11).
- *A gate*: harmful flips 2.2% to 1.0% (d06); net +22 to +35 (d11).
- *Prompt choice*: moves a GPT-4-Turbo GSM8K loss from -3.5 to -0.5 (a04) but does not make it positive.

**Behaviours to expect.**
1. Flipping. GPT-3.5 changes 81.3% of answers more than 6 times in 10 rounds (b21). Llama-3.1-8B overturns 58.8% of correct answers (c16).
2. Agreement with a "looks good" critic: 94% on math (a08).
3. Hallucinated edges in colouring verification (39 of 40 missed cases).
4. Self-preference and self-recognition (d19).
5. "Fixing" by finishing: on a 4B model many fixes were truncated attempts completed (45.4% truncated at 4,096 tokens; d06).
6. Overthinking failures: in the agent task, 17.6% (c16). o1-mini wrote "think" 15.4 times in failed runs vs 5.3 in normal runs (b21).

**Size and class limits.** Small models need a strong verifier (c17, K25). Most models fail to self-improve even on easy-to-check 4x4 Sudoku (b22). The generation-verification gap grows with pre-training compute (relative, not absolute) and saturates in 2-3 rounds (K23).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = S9 and memory lines. Status: [E] established, [S] single-source, [C] contested. Ids are claim ids (K) with the main evidence ids.

### Add now (established)

1. **Keep G2 as written; make S5 depend on a real failing output.** Intrinsic revise lowers accuracy and flips correct answers. [E] G2/S5; K01, K02, K18; a02, a01, d05, d09.
2. **Route S5 by the S0 gate.** Run S5 where a cheap sound check exists: code with tests, recomputable arithmetic, constraint lists, validators. Skip it, or stop at best-so-far, on single-answer reasoning with no check. [E] S0/S5; K35, K10; d09, d13, a07.
3. **Keep best-so-far through every revise round.** A revision is accepted only if the checker rates it at least as good. Naive revision turned 38% of correct answers wrong in a trained reviser. [E] S5/S8; K29; d02.
4. **Log at every S5 step:** acc before and after, right-to-wrong, wrong-to-right, tokens, and best-of-n at equal calls. [E] G7; K18, K12; c27.
5. **Never let code with gold answers stop a loop in tests.** Audit every bench run for leaked stop signals. Compare against the strongest first prompt. [E] G7; K02, K11; a01, b04.
6. **A model's own verdict is not a check on planning or constraint outputs.** Use code (validator, recomputation). [E] G2/G3; K04; a15, a16.
7. **With a sound checker, send the plain failure, not an elaborate critique.** Binary or first-error feedback was near full text. Test a bare retry first. [E] S5; K05; a15, a16.
8. **Treat a self-written test as weak evidence.** Weight a pass by coverage and add tests for the unfitted part (G3). Cap retries near 5. [E] G3/S4/S8; K26; d18, d03.
9. **No debate; no multi-agent critique as a revision method.** [E] G9; K12; a06, b03.
10. **Keep S5 tied to checkers; do not plan on prompt-only self-detection.** No fair prompted success in general tasks; training is not available to the scaffold. [E] S5; K30, K16; d15, d16.
11. **Locate with code when possible, then fix.** Locating is the bottleneck; fixing given the place works. [E] S5; K03; b05, b06. (Whether a model locator beats one-shot critique at equal tokens is in Test first.)

### Test first

| # | Candidate | Part | Status | Claims / evidence |
|---|---|---|---|---|
| T1 | Spend tokens on a larger first-solve budget before adding a check call; gate the check. | S5/G11/G12 | [S] | K27; d06, d17 |
| T2 | Present the draft as another solver's answer in the user turn vs "your previous answer". | S5/G2 | [S]/[C] | K13, K34; a28, d20, d19 |
| T3 | Append a short continue-checking cue ("Wait") before the final answer. | S5 | [S] | K14, K15; a28, c19 |
| T4 | Neutral T=0 check vs no check, with seeds and error bars, on a 2025-26 reasoning model. | G2 | [C] | K19, K18; c14, d09, d05 |
| T5 | Keep-unless-you-name-the-error wording in the check step. | G2/S5 | [S] | K20; d01 |
| T6 | Cap rounds at 1 ungated and up to 3 gated; end every check prompt with the task restated. | S5 | [S] | K32; d05, d10, d11 |
| T7 | Locate-then-fix with a reasoning model vs one-shot critique. | S5 | [S] | K31, K03; d04, b06 |
| T8 | A different, stronger model (or fresh context) as checker vs the same model. | G5/S5 | [S] | K33; d11, d19 |
| T9 | Verify across 2+ drafts instead of one; select by verify score. | S7 | [S] | K36; d14 |
| T10 | Vote over checked drafts vs vote over raw drafts at equal tokens. | S7 | [S] | K28; d07 |
| T11 | Disagreement-guided routing: accept when attempts agree, vote when split, rewrite the problem when widely split. | S0/S6 | [S] | d08 (not in claims.jsonl) |
| T12 | Isolated item checks (CoVe) where the answer splits into claims. | S5 | [C] | K22; a22, d12 |
| T13 | Tool vs no-tool critique on our model. | S5 | [C] | K08; b19 |
| T14 | Measure the generation-verification gap per task class before adding a revise loop. | S0 | [S] | K23; b22 |
| T15 | Do not reward reflection words in traces; count phrases against accuracy. | G10 | [C] | K24; b23 |
| T16 | Stored reflection (Reflexion memory) vs bare retry at equal calls, gated by a test. The effect with an external signal is [E]; the gain from the reflection text itself is untested. | S9/memory | [S] | K26; a11, d18 |

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens. Report the ledger numbers from 4.1 and a bootstrap interval over at least 3 seeds. Use at least 100 items per cell, 200 for rare events. "Plain" means the plain model with the same total tokens spent on a longer or repeated first solve.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Items with a sound checker (code with tests, arithmetic recompute, constraint list) | plain best-of-n vs check-and-fix (4.2) vs bare retry on fail | pass rate at equal calls; flips | check-and-fix at least equal to best-of-n; bare retry close to full critique |
| B2 | Items without a checker (single-answer reasoning) | plain vs neutral revise vs no revise | right-to-wrong, wrong-to-right, net | net about 0 or negative for neutral revise; supports routing |
| B3 | Math with a long-CoT reasoning model | (a) larger first-solve budget (b) first solve plus gated verify (c) always verify | accuracy, harmful flips, tokens | (a) about equal to (b) with fewer tokens; (c) worse than (b) |
| B4 | Math and code items with injected errors in the draft | draft as "your previous answer" vs draft as another solver's answer in the user turn vs neutral rewrite of the draft | fix rate; keep rate for correct drafts | external framing fixes more if role matters; neutral rewrite tests style recognition |
| B5 | Same | with vs without "Wait" cue | fix rate; harmful flips | cue helps non-reasoning models; small effect on reasoning models |
| B6 | Items with a planted first wrong step (BIG-Bench Mistake style, our own traces) | locate-then-fix vs one-shot critique; locator = reasoning model vs base model vs code | locate accuracy; fix rate given location; net | locate accuracy rises with reasoning model; fix given location positive |
| B7 | Mixed correct and wrong drafts | neutral check wording vs "keep unless you name the error" vs critical wording | right-to-wrong; wrong-to-right | gate wording cuts right-to-wrong by a few points; critical wording worst |
| B8 | Items with a checker and wrong first answers | rounds = 1, 2, 3, 5; ungated vs gated | net gain per round | gain stops after 1 to 3 rounds; ungated rounds add flips |
| B9 | Items with a model-written test as the only gate | test-gated retry vs no loop vs test plus held-out test | pass rate; false-positive rate | model-written tests alone can lose to no loop where false positives are high |
| B10 | Hard reasoning items | check by same model vs separate stronger model vs fresh context | net fixes; degraded | separate stronger checker fixes more |
| B11 | Reasoning items | vote over raw drafts vs verify-then-select across drafts vs vote over revised drafts | accuracy at equal total tokens | verify-select at least equal to vote on hard items; revise-then-vote helps only weak models |
| B12 | Reasoning items of mixed difficulty | disagreement routing vs majority vote vs single | accuracy at 4 and 8 samples | routing beats majority on hard items |
| B13 | Answers that split into independent claims vs chained steps | CoVe vs whole-draft critique vs no revise | net; degradation of correct | CoVe wins on claims; loses on chained steps |
| B14 | Same tasks as B1 and B2 | measure generation accuracy vs verification accuracy | gap vs gain from revise | revise pays where verify accuracy clearly exceeds generate accuracy |

## 9. What does not transfer, and why

- **Oracle-stop gains (RCI, Reflexion HotPotQA, RISE headline).** They use the gold answer to stop. Our agent has no gold answer.
- **Training results (SCoRe, RISE, S2R).** We do not train. They show a ceiling, not a method (K30, K16).
- **Colouring and Blocksworld results.** Synthetic, small (n=100), and very hard for GPT-4. They show verifier failure, not the size of the loss on open tasks.
- **Self-Refine style-task gains.** Sentiment, dialogue preference and acronyms have no single right answer and the rater is a model. Little overlap with exact-answer bench items.
- **DISC's 149:1 ratio.** It starts at 15% correct traces, so there are few correct answers to break. Not a general flip rate.
- **Refine-then-vote (Bilal).** Not compute-matched, small base models. Not an equal-compute win.
- **SEVRA's gain.** One 4B model; much of the "fix" is finishing truncated answers.
- **Injected-error results (Tsui).** The errors are planted and off-policy. Natural errors are caught far less (4.3% to 10.8% of a model's own natural errors, c18). The size of the effect on our drafts is unknown.
- **ProcessBench locate scores.** Math step labels. Open-ended agent steps have no gold step labels.
- **2023-era models (Huang, Stechly, Valmeekam, Tyen).** The direction transfers; sizes do not. Treat sizes as upper bounds on the loss.
- **Human feedback (Olausson 52.6% vs 33.3%).** Our agent has no human in the loop. The lesson is only that feedback quality is the bottleneck.
- **Self-Debug on Spider (no tests).** Gain of 2 to 3 points; this setting is closer to intrinsic revise.

## 10. Open questions

1. Does a check step help a 2025-26 long-CoT model at equal tokens against simply thinking longer or sampling more? Only one 4B model tested (K27).
2. Does the Tsui framing effect (another solver's answer vs your previous answer) matter in a scaffold at equal tokens? Does style recognition (GPT-4 73.5%) undo it?
3. What are right-to-wrong and wrong-to-right rates for a neutral T=0 check on current models over several seeds? Liu vs Huang is unresolved.
4. Which task classes have a cheap sound checker, and how large is the gain over best-of-n at equal calls on a 2025 model?
5. How much does a wrong pass signal cost, compared with no signal? Data: Reflexion MBPP (-3 points) only.
6. Does locate-then-fix beat one-shot critique with a 2025 reasoning model at equal tokens?
7. Is one ungated round optimal, or do up to 3 gated rounds pay on reasoning models?
8. Does confidence gating cut flips without cutting fixes? Li's Figure 4 flip numbers were unreadable.
9. Does CoVe-style isolation work on multi-step reasoning claims if a keep/change judge is added?
10. Is there any prompt-only match for SCoRe or RISE on open models? Nothing found.
11. Is the SCoRe base fix rate 4.6% or 9.5%? Is RISE's no-oracle number reported anywhere?
12. Does the generation-verification gap predict our per-class gain from revise?
13. Do natural errors behave like injected errors (Tsui)?

## 11. Sources

[V] = opened this session as PDF or full text. [M] = snippet or title only.

1. Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 [V] (a01 to a06, b01 to b04, c01 to c03)
2. Kamoi et al. (2024) When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey. https://arxiv.org/abs/2406.01297 [V] (a25, b08, b09, c04, c05, c25, c27, d15)
3. Kamoi et al. (2024) Evaluating LLMs at Detecting Errors in LLM Responses (ReaLMistake). https://arxiv.org/abs/2404.03602 [V] (a26, b10)
4. Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651 [V] (a07 to a09, b11, b12, c06)
5. Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 [V] (a10, a11, c07, c26, d18)
6. Kim, Baldi, McAleer (2023) Language Models Can Solve Computer Tasks (RCI). https://arxiv.org/abs/2303.17491 [V] (a12; c23 lists it as not opened; the a12 table was garbled)
7. Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 [V] (a17, b19, c08)
8. Chen et al. (2024) Teaching LLMs to Self-Debug. https://arxiv.org/abs/2304.05128 [V] (a20, d13)
9. Olausson et al. (2024) Is Self-Repair a Silver Bullet for Code Generation? https://arxiv.org/abs/2306.09896 [V] (a21, b20; the 1.05x / 0.97x figures unverified)
10. Welleck et al. (2023) Generating Sequences by Learning to Self-Correct. https://arxiv.org/abs/2211.00053 [V] (a18)
11. Saunders et al. (2022) Self-critiquing models for assisting human evaluators. https://arxiv.org/abs/2206.05802 [V] (a19)
12. Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516 [V] (a13, b05 to b07, c09); trained-classifier tables (a14) [M]
13. Stechly, Marquez, Kambhampati (2023) GPT-4 Doesn't Know It's Wrong. https://arxiv.org/abs/2310.12397 [V] (a15, b13, c10)
14. Valmeekam, Marquez, Kambhampati (2023) Can LLMs Really Improve by Self-critiquing Their Own Plans? https://arxiv.org/abs/2310.08118 [V] (a16, b14, c11)
15. Dhuliawala et al. (2024) Chain-of-Verification Reduces Hallucination. https://arxiv.org/abs/2309.11495 [V] (a22)
16. Kumar et al. (2024) SCoRe. https://arxiv.org/abs/2409.12917 [V] (a23, b17, c12)
17. Qu et al. (2024) RISE. https://arxiv.org/abs/2407.18219 [V] (a24, b18, c13)
18. Zhang et al. (2025) Understanding the Dark Side of LLMs' Intrinsic Self-Correction. https://arxiv.org/abs/2412.14959 [V] (a27, b21, c16, d05; some tables scrambled)
19. Tsui (2026) Self-Correction Bench: the Self-Correction Blind Spot. https://arxiv.org/abs/2507.02778 [V] (a28, b15, b16, c18, d20)
20. Song et al. (2025) Mind the Gap. https://arxiv.org/abs/2412.02674 [V] (b22)
21. Liu et al. (2025) Understanding R1-Zero-Like Training. https://arxiv.org/abs/2503.20783 [V] (b23)
22. Zheng et al. (2024) ProcessBench. https://arxiv.org/abs/2412.06559 [V] (b25, d04)
23. Liu et al. (2024) Large Language Models Have Intrinsic Self-Correction Ability. https://arxiv.org/abs/2406.15673 [V] (c14). Note: arXiv 2406.02378 is a different paper.
24. Li et al. (2024) Confidence Matters (If-or-Else). https://arxiv.org/abs/2402.12563 [V] (c15, d01)
25. Zhang et al. (2024) Small Language Models Need Strong Verifiers to Self-Correct Reasoning. https://arxiv.org/abs/2404.17140 [V] (c17; per-dataset numbers not extracted)
26. Muennighoff et al. (2025) s1: Simple test-time scaling. https://arxiv.org/abs/2501.19393 [V] (c19)
27. DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948 [V] (c20, qualitative)
28. Weng et al. (2023) LLMs are Better Reasoners with Self-Verification. https://arxiv.org/abs/2212.09561 [V] (c21; table garbled, conditions not confirmed)
29. Du et al. (2023) Improving Factuality and Reasoning through Multiagent Debate. https://arxiv.org/abs/2305.14325 [M] (c24; known through Huang)
30. Pan et al. (2023/2024) Automatically Correcting LLMs: Surveying the Landscape. https://arxiv.org/abs/2308.03188 [M] (a29, b24, c22; title only)
31. Snell, Lee, Xu, Kumar (2024) Scaling LLM Test-Time Compute Optimally. https://arxiv.org/abs/2408.03314 [V] (d02)
32. Stroebl, Kapoor, Narayanan (2024; v3 2026) The Limits of Inference Scaling Through Resampling. https://arxiv.org/abs/2411.17501 [V] (d03)
33. Dip, Zhou, Zhang (2026) Think Again or Think Longer? Selective Verification. https://arxiv.org/abs/2606.19808 [V] (d06)
34. Bilal et al. (2026) Refining Over Resampling. https://arxiv.org/abs/2608.05643 [V] (d07)
35. Lin et al. (2026) When to Vote, When to Rewrite. https://arxiv.org/abs/2604.26644 [V] (d08)
36. Stav, Berlowitz, Orner, Kraus (2026) When Does Intrinsic Self-Correction Help? https://arxiv.org/abs/2606.23196 [V] (d09)
37. Yin, Ken, Stremmel (2026) Denoising Iterative Self-Correction (DISC). https://arxiv.org/abs/2606.21724 [V] (d10 to d12)
38. Zhao, Awasthi, Gollapudi (2025) Sample, Scrutinize and Scale. https://arxiv.org/abs/2502.01839 [V] (d14)
39. Ma et al. (2025) S2R. https://arxiv.org/abs/2502.12853 [V] (d16)
40. Hassid et al. (2025) Don't Overthink it. https://arxiv.org/abs/2505.17813 [V] (d17)
41. Panickssery, Bowman, Feng (2024) LLM Evaluators Recognize and Favor Their Own Generations. https://arxiv.org/abs/2404.13076 [V] (d19)
42. Petrova, Vejsiu (2026) Spectral Origins of the Self-Correction Blind Spot. https://arxiv.org/abs/2607.09803 [V] (d21)

Internal files: SCHEMA.md (research_notes/single_agent), SUBFIELDS.md (C01), critique.md, claims.jsonl, evidence_a-d.jsonl in this folder.

Links to parallel subfields (not covered here): test-time compute scaling, overthinking, metareasoning and value of computation, fault localisation and repair, debugging as scientific method, meta-reasoning, noise and judgement, judgment and credence aggregation.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 15 established claims: 11 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C01.05-K04** (now single-source: the sources are not independent). Numbers verified (2 of 100 optimal colourings accepted, 1/100 self-critique, 84.45% false positives, 55 vs 88/100), but both papers are from the same lab (Stechly/Valmeekam/Kambhampati), so the two domains count as one source group.
- **C01.05-K05** (now single-source: the sources are not independent). Binary vs richer feedback results (colouring ~40% in all variants, Blocksworld 37/50 vs 43/50) verified, but both come from the same Kambhampati-lab papers, and colouring plain top-n sampling also reaches 40%.
- **C01.05-K07** (reworded: the sources support less). Figures verified (CRITIC +7.7 F1 and +7.0 math, Self-Debug up to +12, Reflexion HumanEval 91.0 vs 80.1) but 'reliable gains' is too strong: Self-Debug gains are +2-3 on Spider, Reflexion trails GPT-4 on MBPP (77.1 vs 80.1), and Olausson shows self-repair gains are modest and uneven per compute budget. Corrected claim: Tool or execution feedback (code interpreter, unit tests, search) often gives gains in correction loops, though uneven: CRITIC adds about 7.7 F1 on QA and 7.0 points on math for ChatGPT; Self-Debug up to +12 with unit tests (+2-3 on Spider without them); Reflexion HumanEval 91.0 vs 80.1 but MBPP 77.1 vs 80.1.
- **C01.05-K35** (reworded: the sources support less). Stav SAT numbers, Self-Debug 61.4 to 69.4, 72.8 to 80.6, TransCoder 77.3 to 88.8 and Stroebl are right, but 'without execution the code gain vanishes' is too strong: without execution MBPP gains shrink (Codex simple 57.6 vs 61.4 but +Expl 64.4 and +Trace 66.2; GPT-4 76.0 to 76.4 vs 72.8; TransCoder Codex 83.4-83.9 vs 80.4). Corrected claim: Where a cheap sound check exists, intrinsic revision pays: SAT revision at T=0: Mistral 34.62 to 64.96, Haiku 4.5 75.64 to 93.59, DeepSeek V3.1 78.63 to 92.74, with correct-to-wrong at most 2.1%. Code with real tests: Self-Debug MBPP Codex 61.4 to 69.4, GPT-4 72.8 to 80.6; TransCoder GPT-4 77.3 to 88.8. Without execution the code gain shrinks to about +3 to +5 points and for MBPP Codex simple feedback is below baseline (57.6 vs 61.4). No study compares check-and-fix with best-of-n at equal calls on a 2025 model.
- **C01.05-K10** (now single-source: only one opened source, code check).
- **C01.05-K12** (now single-source: only one opened source, code check).
