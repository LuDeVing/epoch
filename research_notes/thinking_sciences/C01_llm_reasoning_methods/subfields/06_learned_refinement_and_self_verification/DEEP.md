# Learned refinement and self-verification: deep document

*Subfield C01.06. Key work: ReVISE (arXiv 2502.14565). Schema part: S5 trigger (and S6 weighting). Built from evidence_a-d.jsonl (a01-d19), claims.jsonl (K01-K34) and critique.md in this folder. Cross-check corrections from critique.md are applied here (see section 11 notes).*

## 1. What it is

Self-refinement means a model looks at its own answer and decides whether to rewrite it. The hard part is the decision, not the rewrite. Three questions sit inside it.

1. **Trigger.** Is the first answer wrong? If the model says "wrong" on a right answer, the rewrite can break it. If it says "right" on a wrong answer, a fixable error stays.
2. **Locate.** Where is the error? Models are bad at this on their own text.
3. **Repair.** Given the error, can the model fix it? Usually yes, once the error is shown.

"Learned" means the trigger is trained into the weights, not asked for in a prompt. ReVISE (Lee et al. 2025) adds two special tokens after the first answer: `[eos]` (stop) and `[refine]` (rewrite). The gap in their probabilities is both the stop rule and a confidence score. SCoRe (Kumar et al. 2024) trains with two-turn RL so the second attempt does not break correct first attempts. "Self-verification" is the older, wider idea: score your own answer, with or without training, with or without outside tools.

Why it matters for our agent. Our schema has S5 REVISE and guardrails G1 (doubt only on a signal), G2 (revise only from real output), G5 (code selects). This subfield asks one question: can a model's own read-out ever be the signal? The literature says: not by prompting; barely by training; yes when code or a tool gives the signal. Our agent is a scaffold with no training, so only the ideas transfer: use an external trigger, measure the right-to-wrong rate, and compare against resampling at equal tokens.

Three families of "trigger" appear in the evidence:

| Trigger source | Examples | Verdict |
|---|---|---|
| Prompted self-judgement ("review and fix") | Self-Refine, Huang et al., Reflexion without tests | Net zero or negative on reasoning (K01, K24) |
| Learned self-judgement (token or RL policy) | ReVISE, SCoRe, SPOC, S2R, Xiong et al. | Small net gain, +1 to +5 points, training and labels needed (K08, K10) |
| External signal (tests, tools, sound verifier, separately trained verifier) | Reflexion with unit tests, CRITIC, graph-colouring verifier, GenRM, PRM | The real gains (K17, K18, K06) |

## 2. History and theories in depth

**2.1 Learned verifiers (2021-2023).** Cobbe et al. (2021, a19) trained a separate verifier on GSM8K. Sample many solutions, rank, take the top. A 6B generator plus verifier slightly beat a fine-tuned 175B model on full GSM8K (about a 30x model-size gain). This is the base idea: checking can be easier than writing. Lightman et al. (2023, a20/b18) showed step-level labels (PRM800K, 800,000 human step labels) beat outcome labels: the process reward model solved 78.2% of a MATH subset at best-of-1860. GenRM (Zhang et al. 2024, a31/b19) made the verifier write a chain of thought before judging; best-of-N on GSM8K went 73% to 93.4%. All three use a separate model and many samples. They do not decide "refine or stop".

**2.2 Prompted self-checks and the first wave of self-correction (2022-2023).** Kadavath et al. (2022, b17, abstract only) found large models are partly calibrated: P(True) on their own answers is informative on multiple choice, worse out of distribution. Weng et al. (2023, a21/c17) used backward checks: put the candidate answer back as a condition and see if the model recovers a masked fact. Gains were small (+1.67 average on arithmetic) and came from selecting among candidates, not repair. SelfCheck (Miao et al. 2023, a22) checked step by step and weighted votes: the share of truly correct answers among those predicted correct rose from 67.5 to 76.5 on GSM8K. Self-Refine (Madaan et al. 2023, a13/b16/c18) and Reflexion (Shinn et al. 2023, a17/c21) became the famous prompted loops. Self-Refine helped on taste tasks (sentiment 3.8 to 36.2 with GPT-4) and gave 0.0 on math (64.1 to 64.1). ChatGPT said "everything looks good" on 94% of math items. Reflexion's gains (HumanEval 91 vs 80) came from unit tests as the failure signal.

**2.3 The critical turn (2023-2024).** Huang et al. (2024, a08-a10, c06, c23) showed the earlier positive results used the gold label to stop the loop (oracle), weak first prompts, or unequal compute. Without an oracle, accuracy fell. Stechly et al. (2023, 2024; c15, c16) showed GPT-4 is a poor verifier of its own graph colourings and Game-of-24 answers. Jiang et al. (2024, b15) found models do not discriminate their own outputs better than they generate them. Tyen et al. (2024, a15/a16) split the problem: finding the error is the bottleneck; fixing is easy once the location is given. Kamoi et al. (2024, a14/b10) surveyed it: no prior work shows reliable prompted intrinsic self-correction on general tasks; it works with external feedback, on easy-to-verify tasks, or after large-scale fine-tuning. Olausson et al. (2024, c20) found self-repair in code adds almost nothing once repair cost is counted.

**2.4 Training the trigger and the repair (2024-2025).** Because prompting fails, the field trained it. SCoRe (Kumar et al. 2024) showed SFT and STaR on correction traces fail (distribution shift, collapse to "no edit") and on-policy two-turn RL works. RISE (Qu et al. 2024, c13, snippet) did iterative on-policy fine-tuning. Snell et al. (2024, a18) trained a revision model; left alone it flipped about 38% of correct answers to wrong, so it needs a verifier or sequential vote. Zhang et al. (2024, b13/c12) showed small models need a strong verifier: a self-trained verifier adds little. ReVISE (Lee et al. 2025) is the cheap version: one sample per training item, about 50,000 generations, a two-stage DPO+SFT curriculum. S2R (Ma et al. 2025, b20/c14) and Xiong et al. (2025, d12) trained verify-then-correct habits with RL; SPOC (Zhao et al. 2025, b21) interleaved solve and verify in one model.

**2.5 Reasoning models and the "Wait" cue (2025-2026).** DeepSeek-R1 (a27) showed self-checking can appear from outcome RL. s1 (a25) forced it by appending "Wait". Then the doubts came. Yue et al. (a28): RLVR narrows the pass@k boundary. Kang et al. (2025, d09): in long-CoT models over 90% of post-answer reflections only confirm. d'Aliberti and Ribeiro (2026, d04-d06): spontaneous mid-trace shifts are rare (about 6 to 8%) and go with lower accuracy. Tsui (2026, a24/c22/c25/d14): non-reasoning models fix an injected error in the user turn but not in their own turn (64.5% blind spot); "Wait" cuts it 89.3%. Mirzaei (2026, d01-d03): at equal tokens, prompted self-inspection methods all lose to repeated sampling for Qwen2.5 1.5B to 7B.

**2.6 Competing explanations.**

| Explanation | Holders | Status |
|---|---|---|
| The model cannot judge its own output | Huang, Jiang, Tyen, Stechly | Strongest: direct tests of judging (b15, a15) agree |
| The set-up was biased (prompt wording, temperature) | Liu et al. (b14) | Weak: fair prompt at T=0 gives +0.08 on CSQA (flat, not a gain) |
| The ability exists but is not activated on own output | Tsui (a24) | Supported on injected errors; natural-error evidence is thin (d14: 18% blind spot on one natural set, Qwen2.5-7B) |
| Gains are just extra samples | Huang (debate), Mirzaei, Olausson | Supported: equal-token tests are negative |
| RL makes the model verify precisely when needed | Chen et al. 2026 (d15) | Single source, interpretation checked on one constructed set |

## 3. Core findings with exact numbers

Status: E = established (2+ independent sources), S = single source, C = contested.

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Prompted self-correction without an oracle lowers accuracy | GPT-3.5 GSM8K 75.9 to 74.7 (2 rounds); CommonsenseQA 75.8 to 41.8; GPT-4 GSM8K 95.5 to 89.0; Llama-2 GSM8K 62.0 to 36.5 | Huang 2024 (a08, b08, c06) | E (K01) |
| Oracle stopping creates the gain | GPT-3.5 GSM8K 75.9 to 95.5; GPT-4 84.3 to 97.5; HotpotQA GPT-3.5 26.0 to 49.0 | Huang (a09, b08) | E (K02) |
| Weak first prompt inflates gains | CommonGen-Hard prior paper 44.0 vs 67.0 self-correct; with a good first prompt 81.8 standard vs 75.1 self-correct | Huang (c23) | E (K02) |
| Debate no better than self-consistency at equal responses | GSM8K GPT-3.5: SC 3/6/9 = 82.5/85.3/88.2; debate 83.2 and 83.0 | Huang (a10, c07); Mirzaei (d01) | S (K03) |
| Models are poor at finding their own reasoning errors | Best 52.87 mistake-location accuracy (GPT-4, BIG-Bench Mistake, 5 tasks, 300 traces per sampled task: 255 wrong, 45 right) | Tyen (a15, b11, c10) | S (K04) |
| Given the true error location, repair gains are large | Wrong traces +18.04 to +43.92 points; right traces 0 to -11.43; random location: wrong +5.16 to +21.57, right -6.67 to -15.91 | Tyen (a16, b12) | S (K05) |
| Discrimination is not better than generation | 54 of 56 tests do not reject the null | Jiang (b15) | E (K06) |
| Own-verifier collapses; sound verifier helps | Graph colouring: baseline 16%; GPT-4 as own verifier 1/100; sound verifier about 40% | Stechly (c15, c16) | E (K06) |
| Intrinsic self-correction at T=0 with fair prompt is flat | CSQA 75.92 to 76.00 at T=0; -1.89 at T=1.0 | Liu (b14) | C (K07) |
| SCoRe: first positive net trained correction | MATH (Gemini 1.5 Flash): 60.0 to 64.4 (+4.4); wrong-to-right 5.8%; right-to-wrong 1.4% vs base 15.8%. Base delta -11.2. HumanEval (Gemini 1.0 Pro): 52.4 to 64.6 (+12.2) | Kumar (a11, a12, b06, b07) | E (K08) |
| Offline SFT/STaR on corrections fails | Deltas -11 to +2: STaR +0.4, Pair-SFT +1.8, Self-Refine -1.0 (MATH) | Kumar (b06, c08) | E (K09) |
| ReVISE beats SFT/RFT/STaR+ at Maj@1 | 1B GSM8K 28.1 vs 26.2; 8B GSM8K 61.6 vs 59.2; 8B MATH-500 33.6 vs 30.8. Gap +1.9 to +2.8; single runs, no CIs | Lee (a02, b01, c02) | S (K10) |
| ReVISE verify signal | AUROC 76.0 vs V-STaR 69.5; 71 without curriculum; stage 2 slightly lowers verification | Lee (a04, b02, c03) | S (K11) |
| ReVISE confidence-weighted vote vs plain | 8 samples: 33.9 vs 33.2 (likelihood 32.7); Maj@64 37.7 vs 33.2 | Lee (a07, b04, c04) | S (K12) |
| ReVISE vs SCoRe cost | Gemma-2-2B MATH-500: 23.2 vs 23.0 at 50k vs about 1.5M generations; +iter2 25.8. SCoRe number copied from its paper | Lee (a07, b05, c05) | S (K13) |
| ReVISE on instruction-tuned base | Llama-3.2-1B-Instruct GSM8K: zero-shot CoT 48.6; SFT 41.9; RFT 44.0; ReVISE 52.3 | Lee (a06, b25, c24) | S (K14) |
| ReVISE out-of-domain edge is small | MATH to GSM8K: 1B 8.8 vs 8.2; 8B 61.5 vs 60.3 (+0.6, +1.2); no CIs | Lee (a06, d13) | S |
| Ablations | No DPO loss: -10.3 points; no curriculum 22.6 vs 28.1 | Lee (a04, b03, c05) | S |
| Independent group, similar learned verdict recipe | Qwen2.5-Math-7B: MATH500 78.6 vs 76.8 single-turn DPO; OlympiadBench 40.1 vs 39.0; Minerva 34.6 vs 31.6. Verdict recognises correct 92.0%, wrong 50.6% | Xiong (d12) | S (supports K08/K10) |
| Small models need a strong verifier | LLaMA-2-13B GSM8K correction contribution 10.8% self vs 15.6% GPT-4 verifier | Zhang (b13, c12) | E (K15) |
| Self-repair in code vs resampling | GPT-4 APPS: 1.05x pass rate vs pass@20; 0.97x vs pass@22 | Olausson (c20) | S (K16) |
| Tests/tool feedback drives gains | HumanEval 91 vs 80 (Reflexion); TabMWP +4.7/+9.4/+16.0 (7B/13B/70B, CRITIC) | Shinn, Gou (a17, c19, c21) | E (K17) |
| Learned verifiers help best-of-N | GSM8K 6B+verifier beats 175B; GenRM 73 to 93.4; PRM 78.2% MATH subset | Cobbe, Zhang, Lightman (a19, a20, a31) | E (K18) |
| Naive revision model flips correct answers | About 38% of correct answers turned wrong (PaLM 2-S revision model) | Snell (a18); Kumar (a11) | E (K19) |
| Probes on hidden states predict correctness | ROC-AUC above 0.7, ECE below 0.1; above 0.9 for R1-Distill-Qwen-32B on AIME; up to 24% fewer tokens | Zhang 2025 (a23) | S (K20) |
| Self-correction blind spot | 64.5% over 14 models; "Wait" cuts 89.3%; SFT on 5,306 traces cuts 76.0% | Tsui (a24, c22, c25) | S (K21) |
| RL for verify-and-correct | Qwen2.5-Math-7B 51.0 to 81.6 (S2R, abstract); RLVR may narrow pass@k | Ma; Yue (a26, a28, b20) | C (K22) |
| Spontaneous solve/verify helps small models | SPOC Llama-3.1-8B MATH500 52.2 to 61.0 (+8.8); AMC23 +10.0 (40 items); AIME24 +3.3 (30 items, one problem) | Zhao (b21) | S (K23) |
| Task type moderates | Self-Refine: sentiment +32.4 (GPT-4); math 0.0 | Madaan (a13, b16) | E (K24) |
| Backward and per-step checks help selection | SelfCheck 67.5 to 76.5 (GSM8K); Weng +1.67 average on arithmetic | Miao, Weng (a22, c17) | E (K25) |
| Prompted inspection loses to resampling at equal tokens | 18 of 18 self-inspection comparisons negative; Qwen2.5 1.5B to 7B; 7B Reflexion (forced) -5.5 pp GSM8K [CI -10.2,-1.2], -10.1 pp MATH-500; Self-Refine -3.6 and -6.3 pp; 150 questions per set | Mirzaei (d01, d02) | S (K26) |
| Self-choice vs counting | Counting beats model-chosen from 8 samples by 8.0 and 11.3 points at 1.5B; 2.0 and 1.3 at 7B | Mirzaei (d03) | S (K26) |
| Spontaneous "Wait" shifts are rare and harmful | 6 to 8% of traces; accuracy 2.57% with shift vs 16.44% without (N=723,200); R1 0 to 0.25% on MATH-500 | d'Aliberti (d04, d06) | S (K27) |
| Forced reconsideration gated on entropy | Pass-1 0.3221 to Pass-2 0.4062 (+8.41 pp); 50,574 fixes vs 23,500 breaks; no equal-token control | d'Aliberti (d05) | S (K28) |
| No-training confidence reaches ReVISE-level AUROC | Verbalized confidence at one sample: 66.4 (AIME) to 78.8 (MMLU-Pro Math); 2-sample hybrid up to +12.9 AUROC in math | Del (d07, d08) | S (K29) |
| Reflection after first answer is mostly confirmatory | Over 90% unchanged; wrong-to-right mostly under 2%; 16.8 to 47.8% of tokens for 1.4 to 3.5 points; truncation saves 24.5% tokens for under 2.9% accuracy | Kang (d09) | S (K30) |
| Cheap uncertainty triggers fail on small code models | Regeneration lowered Pass@1 in 5 of 6 configs (-3 to -10 pp); verification-based correction +6 to +26 pp HumanEval, +8 to +20 pp BigCodeBench at 2.4x to 5.9x latency; HumanEval n=31 | Rakasi (d10, d11) | S (K31) |
| Break-even for a trigger | Needed recall/false-alarm ratio = p*d / ((1-p)*c); 0.14 to 1.58 for d from 1.4% to 15.8% at p=0.6, c=0.15 (assumed) | Own derivation (d19) | S (K32) |
| Verify-trained RL saves tokens | 7B: 1152 vs 4458 tokens, 38.4 vs 38.9 accuracy | Chen (d15) | S (K33) |
| Always-refine still overturns correct answers in 2024-25 models | Llama-3.1-8B: 58.8% of correct overturned (-20.4); o1-mini 34.0%, o1-preview 15.6% (table read uncertain) | Zhang 2025 (d16) | S (K34) |

## 4. Mechanisms and models

**4.1 The break-even model of a trigger (build this first).** Let p be the first-pass accuracy. A trigger flags an item. Let r = P(flag | wrong) (recall), f = P(flag | right) (false alarm). Let c = P(refine fixes | wrong and flagged) and d = P(refine breaks | right and flagged). Refine-on-flag beats never-refine when

    r * c * (1-p)  >  f * d * p        i.e.   r / f  >  p*d / ((1-p)*c)

Example (d19): p=0.6, c=0.15. If d=1.4% (SCoRe) the ratio must exceed 0.14. If d=10% it must exceed 1.0. If d=15.8% (base Gemini on MATH) it must exceed 1.58. At Xiong's operating point (r=0.506, f=0.08, ratio 6.3) with d=0.10 the net is about +2.6 points, flagging about 25% of items. That matches the reported +1 to +3. The point: a weak trigger is fine when damage d is tiny. Damage is the quantity to drive down, which is what SCoRe's training mostly did (right-to-wrong 15.8% to 1.4%). Also compare to "resample once more at the same cost": refinement must beat that, not just never-refine (K16, K26). c and d here are assumptions, not measured for one model.

**4.2 ReVISE as an algorithm.**
1. Sample one reasoning path per training question from the base model.
2. Stage 1: build preference pairs on the token after the answer. Correct answer: prefer `[eos]` over `[refine]`. Wrong answer: prefer `[refine]` over `[eos]`. Train with SFT + beta*DPO.
3. Stage 2: start from the stage-1 model and teach correction (a wrong sample followed by `[refine]` and a correct answer is preferred). Same loss. Stage 2 slightly lowers verification accuracy.
4. Inference: greedy decode the answer, read P([eos]) vs P([refine]). If refine wins, rewrite. Up to 3 rounds help (8B MATH-500 keeps improving, read from a plot).
5. Voting: weight each sampled answer by its `[eos]` confidence (33.9 vs 33.2 at 8 samples).

Controls the authors ran: First (stop at first answer) and Retry (resample on refine). ReVISE beat both, so the gain is more than resampling, but Retry used T=0.7 and First/ReVISE greedy, so tokens are not exactly equal (a05). Bar values are only in a figure.

**4.3 SCoRe as an algorithm.** Stage I: train the model to give a good second attempt while keeping the first attempt close to the base, to avoid collapse. Stage II: joint RL on both attempts with a reward bonus for progress (second right minus first right). Offline SFT variants fail because the first-attempt distribution at train time differs from test time and because the model learns to copy its first answer. (Description from the paper's ablations a12/b06; ablation deltas: single-turn training -2.4, no stage I +2.2, no reward shaping +2.6, versus full +4.4.)

**4.4 Split trigger design (Tyen).** Two parts: a locator and a repairer. Repairer: regenerate from the flagged step (8 samples at the step, keep one). A trained locator at about 60 to 70% accuracy was enough for net gain (a16). Prompted locator was at best 52.87.

**4.5 No-training triggers an engineer can build now.**
- Verbalized confidence from one sample: AUROC 66 to 79 on math (d07).
- Two-sample agreement plus verbalized confidence: up to +12.9 AUROC over one-sample (d08). Cost: a second full chain.
- Token-entropy gate: top 20% sequence entropy marked where a forced re-check paid (d05, d06). Weak or negative on small code models (d10).
- Code or test execution: the only trigger that reliably paid in code (d11, a17).
- Hidden-state probe (a23): needs open weights.
- Entropy after a stop-thinking token (EAT, d17): 12 to 22% fewer tokens at equal accuracy. A stop signal, not a refine signal.

**4.6 "Wait" re-entry (Tsui).** Append "Wait" (or a short re-check cue) to the model's own output and let it continue. On injected errors this cut the blind spot 89.3%. As a prompted re-entry in a scaffold it is cheap, but its cost on correct answers is not reported by Tsui (d14), and d'Aliberti's cue had 23,500 breaks against 50,574 fixes with no matched-token resample control.

## 5. What holds up

**Replicated / multi-source**
- Prompted intrinsic self-correction on reasoning does not help (Huang, Kamoi, Zhang 2025, Mirzaei, Rakasi). Magnitude varies by model; it is never reliably positive.
- Oracle-stop and weak-prompt inflation of earlier gains (Huang, Kamoi).
- External signals (tests, tools, sound verifiers) deliver real gains (Reflexion, CRITIC, Stechly, Rakasi).
- Models are poor judges of their own output (Jiang, Tyen, Stechly).
- Trained revision needs on-policy RL, and needs a verifier or sequential vote to avoid flipping right answers (Kumar, Snell, Zhang 2024).
- Learned verifiers help best-of-N (Cobbe, Lightman, Zhang).
- Task type moderates: preference tasks gain, verifiable math does not.

**Single-source or thin**
- ReVISE itself: one paper, Llama 1B/8B and Gemma-2B, gains +1.9 to +2.8 at Maj@1, single runs, no CIs, SCoRe number copied. The headline 27.1 to 31.1 (Maj@3) mixes refinement with voting (critique correction 4). Use Table 1 Maj@1 gaps. The nearest independent result (Xiong, d12) is a related recipe, not a re-run.
- Mirzaei 2026: one author, 150 questions per benchmark, Qwen2.5 only, prompted methods only.
- Tsui 2026, d'Aliberti 2026, Rakasi 2026 (HumanEval n=31), Del 2026: single sources.

**Failures and boundary conditions**
- Out-of-domain transfer of ReVISE shrinks to +0.6 to +1.2 (no CIs).
- On instruction-tuned bases, plain fine-tuning drops below zero-shot CoT (48.6 vs 41.9 SFT); the authors' explanation (forgetting, contamination) is untested.
- Stage 2 lowers verification accuracy slightly (forgetting).
- Model-size moderator: Llama-2 drops 25 points (62.0 to 36.5); GPT-4-Turbo drops 1.5 to 3.5 (b24). Large models are right at turn 1, so the trigger fires rarely (K23).
- Reasoning models: reflection is >90% confirmatory (d09); spontaneous shifts rare and harmful (d04).
- Do not quote "+15.6% absolute on MATH" for SCoRe: it is the delta-of-deltas (+4.4 minus -11.2), not an accuracy gain (critique correction 3).

**Moderators that matter:** task type, base accuracy p, model size, verifier strength, temperature (small), whether an external check exists, whether tokens are matched.

**Contested:** Liu et al. (T=0, fair prompt) vs Huang. Liu's own numbers are flat (+0.08), so they show no harm, not gain (K07). Tsui vs Tyen/Jiang: models fix user-attributed errors but not their own; a possible reconciliation is that injected obvious errors are easier to see than natural ones. Unresolved. RL (S2R, R1) gains at pass@1 vs Yue's narrowing at pass@k: both can be true.

## 6. Language models

**Prompted, 2023-era (GPT-3.5, GPT-4, Llama-2).** Review-and-fix lowers accuracy on GSM8K and commonsense. Round 2 is typically worse than round 1 for GPT-4 (95.5, 91.5, 89.0). Self-Refine on math is flat. ChatGPT declared nothing wrong on 94% of math items.

**Prompted, 2024-2025 models.** Zhang et al. 2025 (d16): "Are you sure?" on yes/no QA still overturns correct answers: Llama-3.1-8B 58.8% (accuracy -20.4); o1-mini 34.0% and o1-preview 15.6% (table cells garbled; approximate). Stronger models overturn fewer but not zero.

**Small open models at equal tokens (2026).** Qwen2.5 1.5B to 7B: every self-inspection method loses to repeated sampling. Reflexion as published never retried at 1.5B because the model said "correct" on every question. Self-choice from 8 samples trails counting by 8 to 11 points at 1.5B, only 1 to 2 at 7B: self-judgement improves with scale but is still not better than counting.

**Trained correctors.** SCoRe +4.4 (MATH, Gemini 1.5 Flash), +12.2 (HumanEval, Gemini 1.0 Pro). ReVISE +1.9 to +2.8 over the strongest baseline. Xiong +1 to +3. SPOC +8.8 on Llama-3.1-8B MATH500 (compared with an untrained base, so not comparable to the others). S2R 51.0 to 81.6 on Qwen2.5-Math-7B (part is format and length; base starts weak). All need labels and training.

**Reasoning-RL models (R1-style).** Spontaneous shifts 0 to 0.25% on MATH-500 for R1. Reflection after the first answer uses 16.8 to 47.8% of tokens for 1.4 to 3.5 points; truncation saves 24.5% tokens for under 2.9% accuracy. A learned refine-trigger test on R1-style models: none found. Probes on hidden states reach ROC-AUC above 0.9 (AIME, 32B distill) and cut tokens up to 24%.

**Forced cue ("Wait"):** non-reasoning models: blind spot cut 89.3% (injected errors). 1.5B math: +8.41 pp, with 23,500 breaks and no matched-token control. Reasoning models have a much smaller blind spot.

**Confidence read-outs:** reasoning models' verbalized confidence: AUROC 66 to 79 on math; 2-sample hybrid up to +12.9. Small code models: weak or negative correlation with pass/fail (mean token entropy -0.416, -0.234, -0.216; P(True) 0.842, 0.782, 0.303); acting on them cut Pass@1.

**Code:** verification-based correction +6 to +26 pp (HumanEval), +8 to +20 pp (BigCodeBench), at 2.4x to 5.9x latency. Self-repair vs equal-budget resampling 0.97x to 1.05x.

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. **Never refine unconditionally, never from the model's opinion.** S5 fires only on a code-observed failing output. Matches G1, G2. | G1, G2, S5 | [E] | K01, K02, K19, K24, K34; a08, b08, c06, d16, a18
2. **Code or tool outcomes are the S5 trigger where a check exists.** Tests, executed outputs, sound verifiers. | S4/S5, G5 | [E] | K06, K17; c15, c16, a17, c19, d11
3. **Accept a revision only through a selector.** Keep best-so-far; a revised answer replaces the first only if a code check or vote supports it. A naive reviser flips about 38% of correct answers. | S5/S7, G5 | [E] | K19; a18, a11
4. **Log fix and break counts for every revise step** (wrong-to-right, right-to-wrong). Target right-to-wrong under 2%. | logging (SCHEMA section 6), G7 | [E] | K08; a11, b07
5. **Compare every revise round against extra sampled votes at equal tokens.** Prompted inspection loses to repeated sampling; self-repair is about 1.0x of resampling. | G7, S6 | [E] for the principle, [S] for the size | K03, K16, K26; a10, c20, d01
6. **Enable refinement only for task types with a checkable metric.** | S0 GATE | [E] | K24; a13, b16
7. **For small base models, use a code check or a stronger external judge, never the same small model.** | S5, G5 | [E] | K15; b13, c12
8. **Backward and per-step checks only as vote weights, with small expected gain.** | S6/S7 | [E] | K25; a22, c17
9. **A model judge, if any, gets no authorship, and counting beats model self-choice.** | G5 | [E] | K06; b15, d03

### Test first (single-source or contested)

1. **Break-even trigger model (4.1).** Measure p, c, d, r, f on our agent. Gate S5 only if r/f clears the formula. | S5 | [S] | K32; d19, d12
2. **Cheap no-training trigger: verbalized confidence plus 2-sample agreement** as an S0/S5 gate on no-check items. AUROC target at or above 0.76. Note: SCHEMA section 4b lists "verbal confidence to stop" as not to add; this test asks whether the combined signal changes that. | S5, S0 | [S] | K29, K11; d07, d08, a04
3. **"Wait" re-entry after the first answer**, gated on high entropy or failed 2-sample agreement, against a matched-token resample arm. | S5 | [S] | K21, K28; a24, d05, d14
4. **Reasoning-model backends: cap or skip the second pass after the first candidate.** | G11, S5 | [S] | K30; d09
5. **Locator accuracy before any step-level trigger.** Measure our agent's error-location accuracy on labelled traces. | S5 | [S] | K04, K05; a15, a16
6. **Trigger precision sweep** (high damage needs high precision). | S5 | [S] | K05; a16
7. **Code-check trigger vs entropy trigger on small code models.** | S4/S5 | [S] | K31; d10, d11
8. **Confidence-weighted votes** vs unweighted. | S7 | [S] | K12; b04
9. **Trigger robustness on shifted items.** | S0 | [S] | K14; d13
10. **Training-only ideas (ReVISE, SCoRe, S2R, verify-first RL):** not available to a scaffold. Park. | memory | [S]/[C] | K09, K10, K13, K22, K33

## 8. Concrete tests on our bench

All arms at equal total tokens (count every generated token, including the review pass). Report paired CIs and log the trigger rate.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Math / word puzzles with no check (single answer) | A: first answer. B: review-and-fix pass. C: first answer plus extra sampled vote at same tokens | Accuracy; wrong-to-right and right-to-wrong rates | B <= A; C > B (K01, K26) |
| T2 | Items with a runnable check (code, ARC programs) | A: resample k. B: revise from failing output (S5). C: revise from model opinion | Pass rate at equal tokens; fix and break counts | B >= A by 0 to 5 points; C below B (K16, K17) |
| T3 | No-check items | Gate = verbalized confidence + 2-sample agreement; refine only if flagged. vs always-refine vs never-refine vs resample | AUROC of gate; net accuracy | AUROC about 0.70 to 0.78; net +0 to +3 (K29, K32) |
| T4 | Items with known wrong first answers (from our logs) | "Wait" cue vs neutral continuation vs fresh resample | Net accuracy; breaks; tokens | Small positive net only where entropy is high (K21, K28) |
| T5 | Labelled step-error traces | Prompted locator vs code locator | Location accuracy | Prompted about 50% (K04) |
| T6 | Break-even sweep (simulation on logged data) | Vary r/f from 0.5 to 10 | Net gain | Matches formula; positive above threshold (K32) |
| T7 | Reasoning-model backend | Full reflection vs truncated after first answer | Accuracy, tokens | Save about 20 to 25% tokens, lose under 3 points (K30) |
| T8 | Weighted vote | Confidence-weighted vs plain at 4 and 8 samples | Accuracy | +0 to 1 point (K12) |

## 9. What does not transfer, and why

- **Token-level `[eos]/[refine]` training.** Needs weights, labels, DPO. Our agent is a scaffold. Only the read-out idea transfers (as a proxy such as verbalized confidence).
- **SCoRe two-turn RL.** Large compute (about 1.5M generations); in-lab Gemini models; not reproducible.
- **ReVISE numbers on Llama 1B/8B math.** Small models, in-domain, trained on gold GSM8K/MATH. Our tasks differ.
- **Self-Correction Bench injected errors.** The blind spot is measured on inserted errors in non-reasoning models; our agent's errors are natural.
- **Verify-trained RL token savings (d15).** Needs training.
- **Hidden-state probes (a23).** Not available for API models.
- **Debate-style critique.** Excluded by G9; confirmed (K03).
- **Self-Refine gains on taste tasks.** Scored by GPT-4 as judge (self-preference); our bench has metrics.
- **AUROC comparisons across papers.** Different tasks, models, definitions; 76 is not special (K11).

## 10. Open questions

1. Does any learned [stop/refine] trigger replicate on other families (Qwen, Mistral) or larger models, against best-of-N at equal tokens? Not found.
2. What are c and d (fix and damage rates) for our own agent at its first-pass accuracy?
3. Do no-training triggers (verbalized confidence plus 2-sample agreement) reach AUROC near 0.76 for code and for small models? Math with reasoning models: yes. Small code models: no (d10).
4. Does a prompted "Wait" cue give a net gain on natural errors, with right-to-wrong cost, versus a matched resample arm?
5. Does a checker-based trigger dominate learned triggers in cost-adjusted accuracy, and on which tasks is there no checker?
6. Is the refine pass redundant on R1-style models? Direction yes (d09); no learned-trigger test.
7. Out-of-domain robustness on AIME or GPQA: no data.
8. Learned stop-or-refine vs adaptive compute (early exit, budget forcing) at matched tokens: no comparison.
9. Does the Huang negative result hold for 2026 frontier models? Partly (d16 on the o1 family).
10. Why do models fix user-attributed errors but not their own? Post-training data lacks correction traces (Tsui); mechanism tested only at 7B to 8B.

## 11. Sources

[V] = opened and read this session (PDF or page text; some read in passages only, limits are in the evidence lines). [M] = snippet or abstract-level only.

Cross-check notes (critique.md): SCoRe MATH is Gemini 1.5 Flash and SCoRe HumanEval is Gemini 1.0 Pro (evidence lines a11 and a12 swap the labels; b06 and b07 are right). SCoRe "+15.6" is a delta of deltas. ReVISE intro numbers (27.1 to 31.1) are Maj@3 vs a vote baseline.

- [V] Lee, Oh, Kim, Shin, Tack (2025) ReVISE. https://arxiv.org/abs/2502.14565 (a01-a07, b01-b05, b25, c01-c05, c24, d13)
- [V] Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798
- [V] Kumar et al. (2024) SCoRe. https://arxiv.org/abs/2409.12917
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Kamoi et al. (2024) When Can LLMs Actually Correct Their Own Mistakes? https://arxiv.org/abs/2406.01297
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Snell et al. (2024) Scaling LLM Test-Time Compute Optimally. https://arxiv.org/abs/2408.03314
- [V] Cobbe et al. (2021) Training Verifiers. https://arxiv.org/abs/2110.14168
- [V] Lightman et al. (2023) Let's Verify Step by Step. https://arxiv.org/abs/2305.20050 (abstract-level figures only)
- [V] Weng et al. (2023) Self-Verification. https://arxiv.org/abs/2212.09561 (per-dataset gains not extracted)
- [V] Miao, Teh, Rainforth (2023) SelfCheck. https://arxiv.org/abs/2308.00436
- [V] Zhang et al. (2025) Reasoning Models Know When They're Right (probing). https://arxiv.org/abs/2504.05419
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778
- [M] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393
- [M] Ma et al. (2025) S2R. https://arxiv.org/abs/2502.12853
- [M] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948
- [V] Yue et al. (2025) Does RL Really Incentivize Reasoning Capacity. https://arxiv.org/abs/2504.13837 (does not test self-verification directly)
- [M] Lin et al. (2024) CriticBench. https://arxiv.org/abs/2402.14809
- [M] Gou et al. (2023/24) CRITIC. https://arxiv.org/abs/2305.11738
- [M] Zhang et al. (2024) Generative Verifiers. https://arxiv.org/abs/2408.15240
- [V] Zhang et al. (2024) Small Language Models Need Strong Verifiers. https://arxiv.org/abs/2404.17140
- [V] Liu et al. (2024) Intrinsic Self-Correction Ability. https://arxiv.org/abs/2406.15673
- [V] Jiang et al. (2024) Self-[In]Correct. https://arxiv.org/abs/2404.04298
- [M] Kadavath et al. (2022) Language Models (Mostly) Know What They Know. https://arxiv.org/abs/2207.05221
- [V] Zhao et al. (2025) SPOC. https://arxiv.org/abs/2506.06923
- [M] Qu et al. (2024) RISE. https://arxiv.org/abs/2407.18219
- [V] Stechly, Marquez, Kambhampati (2023) GPT-4 Doesn't Know It's Wrong. https://arxiv.org/abs/2310.12397
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-Verification Limitations. https://arxiv.org/abs/2402.08115
- [V] Olausson et al. (2024) Is Self-Repair a Silver Bullet? https://arxiv.org/abs/2306.09896
- [V] Mirzaei (2026) Sample More, Reflect Less. https://arxiv.org/abs/2607.28576
- [V] d'Aliberti and Ribeiro (2026) The Illusion of Insight. https://arxiv.org/abs/2601.00514
- [V] Del et al. (2026) How Uncertainty Estimation Scales with Sampling. https://arxiv.org/abs/2603.19118
- [V] Kang et al. (2025) First Try Matters. https://arxiv.org/abs/2510.08308
- [V] Rakasi et al. (2026) When Uncertainty Isn't Enough. https://arxiv.org/abs/2608.14659
- [V] Xiong et al. (2025) Self-rewarding correction for mathematical reasoning. https://arxiv.org/abs/2502.19613
- [V] Chen et al. (2026) Learning to Self-Verify. https://arxiv.org/abs/2602.07594
- [V] Zhang et al. (2025) Understanding the Dark Side of LLMs' Intrinsic Self-Correction. https://arxiv.org/abs/2412.14959
- [V] EAT (2025) Entropy After </Think>. https://arxiv.org/abs/2509.26522 (abstract and intro only)
- [V] Bilal et al. (2026) What If We Allocate Test-Time Compute Adaptively. https://arxiv.org/abs/2602.01070 (abstract, intro, results prose)
- Own derivation (d19): arithmetic on numbers from d12 and K08. Not a source paper.

Links to other parallel subfields (not covered here): Confidence and metacognition; Learned termination; Chain-of-thought prompting; Monte Carlo tree search; Pruning of decision trees; Active inference decision theory.
