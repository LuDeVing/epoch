# LLM metacognitive harness: deep document

*Subfield A04.08. Written 2026-10-26 from evidence_a to evidence_d, claims.jsonl (K01 to K29) and critique.md in this folder. Evidence ids (a01 ... d19) point to the jsonl lines. Status words: established = two or more independent sources; single-source = one paper or one team; contested = sources disagree or the test is weak; untested = nobody has run it.*

*Reading rule for this file: the three evidence files a, b and c cover mostly the same papers. Agreement between them is not independent confirmation. Counts of "independent sources" are by distinct papers or teams.*

---

## 1. What it is

A metacognitive harness is a scaffold around a language model that gives it two things the bare model lacks:

1. **Monitoring.** A read-out of how likely the model is to be right. Examples: a feeling-of-knowing score before solving, a judgment-of-learning score after solving, agreement between samples, a keep-or-withdraw choice, token entropy.
2. **Control.** A rule that uses the read-out to change what happens next: stop, retry, spend more, retrieve, escalate, abstain, or pick among attempts.

The frame comes from Nelson and Narens (1990): an object level (the solver) and a meta level (the monitor and controller), with information flowing up (monitoring) and commands flowing down (control). The central empirical claim of this subfield, from Cao et al. (2026), is that frontier models have usable monitoring but do not use it for control. So control has to be added from outside, in code.

What counts as in scope here:

- Metacognitive prompting (a fixed script of understand, judge, evaluate, decide, rate confidence).
- Self-evaluation gates (P(True), FOK, JOL, keep/withdraw).
- Abstain and escalate policies.
- Knowing when to stop (early-stopping self-consistency, confidence-gated retry, anti-overthinking).
- Uncertainty-triggered retrieval or deliberation (FLARE, Adaptive-RAG, Self-RAG, Reinforcement Inference).
- The 2026 monitoring harness of Cao et al. that raised Claude Sonnet 4.6 pooled accuracy from 48.3 to 56.9, and every test of whether such gains hold at equal compute.

What is out of scope (other subfields in this run): accuracy and dissociation of monitoring in general, adaptive stopping theory, verification design, progress monitoring theory. Links are noted in section 10.

**Why it matters to us.** Our schema already puts the decisions in code (section 1 of SCHEMA.md) and has a gate state (S0), an impasse state (S6) and a selector (S7). This subfield is the closest published template for those three states. It is also the main place where our guardrails G1 (doubt only on a signal), G2 (revise only from real output), G5 (code selects), G6 (never abstain first) and G7 (pay for itself at equal tokens) can be tested against 2026 evidence.

**One-line summary of the state of knowledge.** Confidence-gated control probably helps modestly at fixed cost (plan on +1.5 to +4 points), the +8.6 headline is one team's unreplicated number that never faced an equal-token plain baseline, and the older "self-correction does not work" results are from 2023 models and are being revised for reasoning models.

---

## 2. History and theories in depth

### 2.1 Human roots

- **Nelson and Narens (1990).** Two levels, monitoring up, control down. Cao et al. build directly on it. Their harness gives the meta level an external body (code plus a fitted classifier) because the model's own meta level does not act (a06, a13, c09).
- **Feeling of knowing (FOK) and judgment of learning (JOL).** FOK is a prospective judgment: do I know this, before I try. JOL is a judgment after studying or answering. In the harness FOK is asked with no reasoning allowed, JOL is asked after each attempt and must come with a written reason (a08).
- **Koriat and Goldsmith free-report.** A person who may withhold an answer can trade coverage for accuracy. Cacioli (2026) adapts this: after a forced answer the model chooses KEEP or WITHDRAW, BET or NO_BET (a11). The key metric is the withdraw delta: P(withdraw | wrong) minus P(withdraw | right).
- **Metacognitive knowledge versus regulation.** Knowing your limits is not the same as acting on them. Dissociation of monitoring and control is the main theme of the 2026 LLM work (a13, d07).

### 2.2 LLM timeline

| Year | Work | What it added | Ids |
|---|---|---|---|
| 2022 | Kadavath et al., "Language Models (Mostly) Know What They Know" | Founding paper. P(True): sample an answer, ask the model how likely it is true. P(IK): a trained head that predicts whether the model knows before answering. Large models are calibrated on multiple choice when the format is right. | a16, a17, b16, c14 |
| 2023 | Wang et al., self-consistency | Many paths, vote. Agreement rate predicts correctness, so it is both an answer rule and a confidence signal. | b17 |
| 2023 | Madaan et al., Self-Refine; Shinn et al., Reflexion | Same-model feedback loops. Big gains on subjective tasks; none on math without a real error signal. Reflexion gains rest on executable feedback. | a22, a23 |
| 2023 to 2024 | Xiong et al., confidence elicitation | Verbalized confidence is overconfident; sample agreement is much better. | b15, c15, c16 |
| 2023 | Jiang et al., FLARE | Retrieve only when a token's probability falls below a threshold. | c19 |
| 2024 | Huang et al., "LLMs cannot self-correct reasoning yet"; Kamoi et al. survey; Tyen et al. | Intrinsic self-correction without an oracle lowers accuracy. Models cannot find their own errors but can fix them once the location is given. | a18 to a20, b11, b13, b14, c11, c13 |
| 2024 | Xu et al., self-bias | Models rate their own output higher, and the bias grows with refinement rounds. | a21 |
| 2024 | Snell et al.; Li et al. (ESC); Jeong et al. (Adaptive-RAG); Asai et al. (Self-RAG) | Allocate compute by difficulty; stop sampling when answers agree; route by question complexity. | a24, b18, b20, b22, c20, c22 |
| 2024 | Wang and Zhao, metacognitive prompting; Didolkar et al., skill labelling | Prompt-only metacognition and metacognitive knowledge used for retrieval. | c17, c18 |
| 2024 to 2025 | Kapoor et al.; Chuang et al. (Self-REF); Fu et al. (DeepConf); Chen et al. (overthinking); Muennighoff et al. (s1) | Fine-tuned uncertainty heads; confidence tokens for routing; token-confidence filtering; the overthinking diagnosis; budget forcing. | b19, b21, b24, c21, c24, c25 |
| 2026 | Cacioli, Metacognitive Monitoring Battery (April) | Twenty frontier models; monitoring rank and accuracy rank nearly inverted; Sonnet 4.6 best monitor but rarely acts on it. | a11 to a15 |
| 2026 | Cao et al., metacognitive harness (13 May) | FOK/JOL plus SVM stop rule plus compact-history retry plus forced-choice aggregator. +8.6 pooled on Sonnet 4.6. | a01 to a10, b01 to b10, b25 to b27, c01 to c10, d01 to d05 |
| 2026 | Follow-up tests: Tsui (blind spot), d'Aliberti and Horta Ribeiro (illusion of insight), Nguyen et al. (UAB), Zhai et al., Del et al., Zollo et al., Ding, Dahal et al. (Meta), DosSantos DiSorbo and Ju, AgentAbstain | Partial tests of the pieces: reasoning-model self-correction, adaptive allocation at matched budget, black-box signals, agent-scale control, escalation thresholds. None is a replication of Cao. | d06 to d19 |

### 2.3 The competing theories

1. **"Models know but do not act" (Cao, Cacioli).** Confidence self-reports carry signal; models do not steer effort by them. So add control in code. Evidence: a06, a13, c09, b26. Weak point: single team, single solver.
2. **"Models cannot judge their own correctness" (Huang, Kamoi, Tyen, Xu).** Self-evaluation is biased and often wrong, so any gate based on self-report is suspect unless backed by an external check. Evidence: a18 to a21, b11 to b14. Weak point: 2023 models; reasoning models differ (d08, d09).
3. **"It is just more sampling" (Huang on debate, Snell, Nguyen).** Most gains from "smart" scaffolds are extra samples. At equal samples, plain self-consistency often matches them. Evidence: a19, b12, d11. This is the standing threat to the Cao headline (K02, K29).
4. **"Agreement beats self-report" (Xiong, Del, Zollo, Li).** Agreement across a few samples is a better or cheaper confidence signal than one verbalized number. Evidence: b15, b18, d12, d14, d15. Counter: agreement can be confidently wrong when samples share a bias (d19).
5. **"Allocate by difficulty" (Snell, Adaptive-RAG, UAB).** The gain is in not spending on easy items and spending where there is a foothold. Evidence: a24, b20, b22, d11, d13. This is the least contested idea and the one our G12 already holds.

These are not exclusive. A reasonable synthesis: theory 5 is real; the best signal is a mix of self-report and agreement (theory 4); control should be in code (theory 1); revision needs external output (theory 2); and the size of the gain over a plain voting baseline is unknown (theory 3).

---

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single-source, C = contested, U = untested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Control harness lifts Sonnet 4.6 pooled accuracy | 48.3 to 56.9 (+8.6); N 1,859 (HLE-Verified 668, LiveCodeBench v6 388, R-Bench-V 803); 2.4 attempts; $0.78 vs $0.29 per question | Cao 2026 (a01, a02, b01, c02) | S |
| Per-benchmark gain | HLE 48.0 to 60.0; LCB 74.3 to 84.3 (Easy -0.7, Medium +1.1, Hard +19.6); R-Bench-V 36.1 to 41.1 | Cao 2026 (b03, c03) | S |
| Cost is about 2.7x pass@1, not equal compute | Pass@1 $0.29; Self-Refine $0.45 (52.4); Budget forcing $0.67 (51.5); Verifier rerank $1.32 (49.8, K 4.0); Aggregator $1.42 (53.7, K 4.0); Harness $0.78 (56.9) | Cao 2026 (a02, b02, d03) | C (no plain best-of-K or vote arm) |
| On code the 4-attempt aggregator nearly matches the harness | LCB: Aggregator 83.4 at $0.94 vs Harness 84.3 at $0.56 (K 2.6). HLE: Aggregator 57.0 at $2.31 vs Harness 60.0 at $0.98 (K 1.4) | Cao 2026 (b25, d03, critique) | S |
| Harness candidate set is better than 4 independent samples | Oracle accuracy 62.2 (harness, K 2.4) vs 60.5 (parallel, K 4.0) | Cao 2026 (a02, d03) | S, unexplained |
| Gain is concentrated at low or medium confidence | JOL band accuracy: low 0.16 to 0.42; medium 0.36 to 0.55; high 0.67 to 0.64 | Cao 2026 (a03, b06, c05) | S; regression to the mean not excluded |
| Ablation on N=100: all arms inside noise | Pass@1 44.0; oracle@4 53.0; Full 47.0 [37,57] K 2.58; random retry matched K 45.7 [43,48]; no FOK 45.0; no JOL 42.0; hand rule (1-JOL)xFOK 42.0 (K 2.40); FOK-only 42.0; last answer 40.0; max-JOL 44.0; no prior state (K=4) 45.0; full prior reasoning 40.0 (K 3.09) | Cao 2026 (a04, b04, c04, d02) | C |
| Compact retry history beat full prior reasoning | 47.0 vs 40.0 (N=100). Opposite sign in another study: sequential with full prior reasoning beat parallel in 43 of 45 matched-token cells (4,096-token cap per step) | Cao 2026 (b10, c07); Sharma and Chopra 2025 (d16) | C |
| Confidence works across problems, not within | Within-problem JOL SD median 0.048 vs across 0.270 (5.6x); max-JOL selection 44.0 = pass@1 | Cao 2026 (a07, b05, c06) | S |
| Signal quality varies by model | Sonnet 4.6 (anchor acc 0.58): FOK AUROC 0.612 / ECE 0.132; JOL 0.745 / 0.112; joint 0.757 / 0.087. Gemini-3-Flash FOK AUROC 0.818 but ECE 0.465. Gemma-4 FOK AUROC 0.534 (fail). Bars: AUROC at least 0.60, ECE at most 0.15. Only 1 of 9 models passed every row. Anchor N=100 | Cao 2026 (a05, b07, c08, d04) | S |
| Raw verbalized confidence in open reasoning models fails the bar | Over 36 model-dataset pairs: ECE 0.268, Brier 0.281, AUROC 0.635; token probabilities ECE 0.197, AUROC 0.655; test-time self-consistency ECE 0.090, AUROC 0.836; supervised recalibration ECE 0.051, AUROC 0.732; 2-sample label-free recalibration (BASC-L) ECE 0.083, AUROC 0.685 | Zollo 2026 (d15) | E with K08/K09 (different model families) |
| Verbalized confidence plus 2-sample agreement beats either alone | Math AUROC: verbalized@1 71.3, @8 81.4; SC@2 70.5; combined@2 84.2 (+12.9 over VC@1); STEM and humanities +6.4 | Del 2026 (d14) | C (open models, AUROC only) |
| GPT-4 verbalized confidence is weak; agreement helps | GPT-4 vanilla AUROC 62.7 (chance 50); GPT-3/3.5/Vicuna ECE above 0.377; GSM8K AUROC 54.8 to 92.7 with 5-sample consistency | Xiong 2024 (b15, c15) | E (with d14, d15) |
| Prompted self-correction without oracle hurts (2023 models) | GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 HotpotQA 49 to 43. With oracle: GPT-4 GSM8K 97.5, HotpotQA 59. GPT-3.5 kept first GSM8K answer 74.7% | Huang 2024 (a18, a20, b11, c11) | E for 2023-era instruction models |
| Models cannot find errors but can fix them given the location | BIG-Bench Mistake, 2,186 traces, 5 tasks; best model GPT-4 52.87% on step-level mistake finding | Tyen 2024 (b14) | S, backed by Kamoi (b13) |
| Reasoning models correct errors in their own context | Blind spot 64.5% average over 14 open non-reasoning models; near zero or negative in reasoning models; 'Wait' cuts it by 89.3%; DeepSeek-V3 0.567 to 0.902 with 'Wait' vs R1 0.908; 5,306-trace fine-tune cuts 76.0% | Tsui 2026 (d08) | C |
| Spontaneous pivots are rare and go with lower accuracy; cued second pass helps | Shifts in 6.31% of traces; correct 2.57% with vs 16.44% without (N=723,200, 1.5B model). Forced reconsideration on Math, paired N=320,000: 0.3221 to 0.4062 (+8.41 pp; 50,574 wrong-to-right vs 23,500 right-to-wrong). Cue variants N=500: Qwen2.5-7B +5.97, Llama 3.1-8B -4.19 | d'Aliberti 2026 (d10) | C (no plain re-ask arm seen) |
| Prompted revision adds little for reasoning models at its token price | MATH: Base 68.5 at 791 tokens; CoT 69.5 at 1,804; CoVe 75.0 at 2,019; RCI 70.2 at 1,780; RATT 78.7 at 2,185 | Tie 2025 (d09) | C (150 samples; tokens not matched) |
| Self-bias grows over refinement | Present in all six LLMs tested; grows over iterations; larger models and external feedback reduce it | Xu 2024 (a21) | E with Huang (a18) |
| Debate does not beat self-consistency at matched responses | GSM8K GPT-3.5: standard 76.7; SC 3/6/9 = 82.5/85.3/88.2; debate round 1 (6 responses) 83.2; round 2 (9 responses) 83.0 | Huang 2024 (a19, b12, c12; corrected in critique) | S here; E as guardrail G9 |
| Early-stopping self-consistency | Sample cuts: MATH 33.8%, GSM8K 80.1%, StrategyQA 76.8%, CSQA 78.5%, Coin Flip 84.2%, Last Letters 67.4%. GPT-4 accuracy change 0.00 on MATH, GSM8K, CSQA. GPT-3.5 StrategyQA -0.19; Llama-2 7B -0.14 | Li 2024 (b18, c22) | E (with d11) |
| Adaptive allocation by disagreement at equal total samples | Budget 4: Qwen2.5-1.5B Uniform SC 45.0, ASC 45.2, UAB 47.0; Llama3.2-3B 45.5 / 47.0 / 47.9. UAB beats Uniform in 14 of 15 settings, average +2.5, p<0.05 in 9 of 15. MATH500: +1.8 at N=4 falls to +0.5 (p=0.42) at N=16. GPT-OSS-20B +2.7, Gemma3-27B +1.5, but ASC edges UAB on both | Nguyen 2026 (d11, d12) | E (with d13) |
| Directed allocation beats random at same mean cost | MATH N=200, DeepSeek-V3 at B 1.5/2.0/3.0: random 0.519/0.517/0.534 vs learned 0.550/0.562/0.575; oracle 0.555/0.571/0.586. GPT-4o-mini B=3.0 0.487 to 0.526; Qwen2.5-7B 0.515 to 0.554 | Zhai 2026 (d13) | S (N=200, math only, voting only) |
| Disagreement of two samples is the best allocation signal | Qwen2.5-1.5B, N=4: NLL 44.4 / AUROC 0.742; token variance 44.8 / 0.672; max token NLL 45.0 / 0.688; vote entropy (K=2) 47.0 / 0.780. Allocation alone is at least half the gain | Nguyen 2026 (d12) | S |
| Agreement can mislead | Spearman of agreement with majority-correct is positive in all 12 cells, none above 0.6; gpt-4.1 -0.18 [-0.31,-0.03] GPQA and -0.26 [-0.40,-0.12] AIME; 48% wrong [0.40,0.56] when agreement is at least 0.8; mean agreement 0.89, ECE 0.41 | Ding 2026 (d19) | S |
| Compute by difficulty | Compute-optimal revisions or PRM search match best-of-N with about 4x less compute (64 vs 256 samples; 16 vs 64 generations). Easy: sequential revisions best; medium to hard: beam search; hardest: no method helps | Snell 2024 (a24, b20) | E (with d11, d13) |
| Reasoning models overthink easy items | "2+3": 1,953% more tokens; over 92% of cases first solution already correct; self-training cut 48.6% of tokens on MATH500 at kept accuracy | Chen 2025 (b21, c23) | S |
| Budget forcing flattens | s1-32B AIME24 50.0 to 53.3 with 2x Wait, up to 57 at best setting; flat near 6x; AIME24 has 30 questions (one item = 3.3 points). In Cao: +3.2 pooled at $0.67 | Muennighoff 2025 (a25, b24) | E |
| Token-confidence filtering helps in most but not all settings | DeepConf: GPT-OSS-120B AIME25 512 traces 99.9 vs vote 97.0 vs pass@1 91.8; online cuts tokens up to 84.7%; top-10% filtering helps in 12 of 20 offline settings (+1.22 avg), hurts in 8 of 20 (up to -4.69) | Fu 2025 (b19) | S; needs logprobs |
| Triggered retrieval beats always-retrieve | FLARE: best at 40 to 80% of sentences triggering; StrategyQA drops above 50%. Adaptive-RAG GPT-3.5 F1 50.91 vs multi-step 50.87; oracle router 62.80; router accuracy 54.52% | Jiang 2023; Jeong 2024 (b22, c19) | E |
| Monitoring rank and accuracy rank are nearly inverted | 20 frontier LLMs, 524 items, 10,480 evaluations. Haiku 4.5 accuracy rank 13, monitoring rank 2. GLM-5 accuracy 1, monitoring 9. Gemini 3.1 Pro accuracy 6 (critique correction), monitoring last (-1.0). Sonnet 4.6 +39.4 withdraw delta, Haiku 4.5 +31.6, GPT-5.4 +27.9 | Cacioli 2026 (a11, a12) | S |
| Detecting is not acting | Sonnet 4.6 answered directly on 98.6% of T6 items (72) despite top withdraw delta; r = .17, CI [-.29,.57], n = 20; alpha 0.54; 17 of 20 models scored 0% on adversarial foils, always KEEP+BET | Cacioli 2026 (a13, a14) | C (underpowered) |
| Scaling does not reliably improve monitoring | T2 withdraw delta: Qwen 80B/235B/480B +30.1/+21.8/+11.2 (falls); GPT-5.4 nano/mini/full +17.1/+22.4/+27.7 (rises); Gemma 1B/12B/27B +18.3/+18.3/+16.7 (flat) | Cacioli 2026 (a15) | S |
| Agent-scale controller with compact state | 12 of 12 matched comparisons won vs flat-history direct control; ProgramBench GPT-5.5 71.5 vs 63.7; Opus 4.8 at 400 calls loses 56.6 vs 62.7; direct agent uses about 18% of its 1,200 calls | Dahal 2026 (d06) | S; matched on calls, not tokens |
| Escalation thresholds are unstable | Qwen3.5-9B 56% vs 397B 81%; GPT-5-nano 91% vs GPT-5-mini 53%; Qwen 9B cost-optimal 62.0% baseline, 78.8% with thinking plus cost framing | DosSantos DiSorbo 2026 (d17) | S |
| Abstention is independent of solving | 263 paired tasks, 42 sandboxes, 17 LLMs; best paired accuracy 59.5% (Gemini 3.1 Pro); abstention often after an irreversible step | AgentAbstain 2026 (d18, abstract only) | S |
| Prompt-only metacognition gives modest NLU gains | MP relative gain over CoT 4.8% to 6.4% and over plan-and-solve 2.8% to 4.1% (10 NLU datasets, 4 models); MedNLI 70.9 vs 67.1 | Wang and Zhao 2024 (c17) | S; no equal-token arm |
| Skill labelling as retrieval | MATH +11.6% over CoT; PAL +7.52% | Didolkar 2024 (c18) | S |
| Gate vs always re-ask, one-shot baseline | MMLU-Pro 12,032 questions, DeepSeek-v3.2: 60.72 to 84.03 with 61.06% extra calls; re-ask all 84.35 | Sun 2026 (a27) | S; baseline weak |
| No independent replication of Cao | arXiv lists v1 only; no code link; both citers read (Yale survey, Meta paper), neither a replication | d01, d06, d07 | fact as of 2026-10-26 |

---

## 4. Mechanisms and models

This section is written so an engineer can build each part. Pieces marked (Cao) are the 2026 harness; others are from the related work.

### 4.1 The Cao pipeline (a01, a08, b27, c01)

```
for each question q:
    fok = model.call(FOK_prompt, q)            # score in [0,1], no reasoning allowed
    attempts = []
    for k in 1..K_max (K_max = 4):
        context = compact_history(attempts)    # prior answers, JOL scores, one-line reasons; NOT prior reasoning
        a = model.call(solve_prompt(q, fok, context))   # returns reasoning, answer, jol, jol_reason
        attempts.append(a)
        p_stop = controller.predict_proba(fok, a.jol)   # per-model SVM, calibrated
        if p_stop >= 0.7: break
    if len(attempts) == 1: return attempts[0].answer
    idx = model.call(aggregator_prompt(q, attempts_without_scores))   # forced to return an index
    return attempts[idx].answer                # copied verbatim, no synthesis
```

Details that matter:

- **FOK prompt forbids computing.** It is a snap judgment of familiarity, so it stays cheap. (b09)
- **JOL must come with a written reason.** The reason is there to stop the score collapsing to a default like 0.8. Not tested alone. (a08)
- **Controller.** An SVM on two features (FOK, JOL) with an output calibrated by isotonic regression (7 of 9 models) or sigmoid (2 of 9). Chosen from 134 configurations per model (67 estimator configs times 2 calibrators) by out-of-fold AUROC, 5-fold times 3 repeats, on a 100-item anchor set disjoint from the test data. Sonnet 4.6 ended with a polynomial kernel of degree 3 and stop threshold p = 0.7, with balanced class weights. (a08, c01)
- **Retry prompt** says: try a different approach and address the earlier concerns. (a08)
- **Aggregator is forced to pick an index.** A free-form synthesizer tended to re-solve and invent a new wrong answer. It sees reasoning and answers but not the scores. (a08, b27)
- **Each step is a separate tool call** (FOK, solve plus JOL, retry, aggregate) with a JSON schema, packaged as MCP tools. (a08)
- **Diagnosis first.** Before using any model, run it on 100 anchor items and measure AUROC and ECE for FOK, JOL and the joint SVM output. Pass bars: AUROC at least 0.60 and ECE at most 0.15. (a05, d04)

Measured behaviour of the pipeline: early-stop hit rate 76.7% for the learned controller against 42.6% for random retry at the same mean K of 2.58 (d02). Attempts fall monotonically from low to high confidence band (a03, b26). Appendix F gives K per benchmark: HLE 1.4, LCB 2.6, R-Bench-V 3.2 (b25).

### 4.2 The monitoring signals and what each is good for

| Signal | How to get it | Needs | Good for | Bad for | Ids |
|---|---|---|---|---|---|
| FOK (pre-solve verbal) | One short call, no reasoning | Black box | Cheap triage; weakest of the two (AUROC 0.612 on Sonnet, 0.534 on Gemma 4) | Anything alone; ablation cost only 2 points (inside noise) | a05, b09 |
| JOL (post-solve verbal, with reason) | Asked inside the solve call | Black box | Across-problem allocation (AUROC 0.745 on Sonnet) | Choosing among attempts of one problem (within-problem SD 0.048) | a05, a07 |
| Joint (FOK, JOL) through calibrated SVM | Fit on anchors | 100+ labelled items | Fixes miscalibration (GPT-OSS JOL AUROC 0.87 but ECE 0.41; joint ECE 0.06) | Distribution shift; overfitting to anchors | b07 |
| Sample agreement (K=2 to 5) | Extra samples | Black box | Cheap, strong AUROC (GSM8K 92.7 with 5 samples on older GPT-4; SC@8 0.836 average on open reasoning models) | Over-confident models whose agreement is uncorrelated with truth (gpt-4.1 GPQA 48% wrong at agreement 0.8 or more) | b15, d15, d19 |
| Verbalized plus 2-sample agreement | Both | Black box | Best cost trade (math AUROC 84.2) | Not tested on Claude | d14 |
| Two-sample vote entropy | Two probes | Black box | Allocation (AUROC 0.780 vs logprob signals 0.66 to 0.74) | Small model only | d12 |
| Token logprobs / entropy | Model API | White box | Stop and filter (DeepConf up to 84.7% fewer tokens); gate for a second pass (Sun; d'Aliberti) | Confident-wrong traces; hurt in 8 of 20 DeepConf settings | b19, a27, d10 |
| Keep/withdraw after a forced answer | One extra call | Black box | Retrospective check; Claude models strong | Domain-specific; model may not act on it | a11, a14 |
| Self-generated tests | Model writes tests | Code execution | Revision from real output | False negatives (Reflexion on MBPP) | a23 |

### 4.3 Stop rules (when to stop sampling or stop retrying)

1. **Window agreement (ESC).** Draw answers in windows of 5 (8 for MATH). Stop when a window is unanimous. Max 40 (64 for MATH) samples. (b18)
2. **Calibrated confidence threshold (Cao).** Stop when calibrated joint confidence is at least 0.7.
3. **Probe-and-allocate (UAB).** Draw 2 probes per question. Questions whose probes agree get no more. The remaining budget is split among questions whose probes disagree, to meet a fixed total budget exactly. (d11)
4. **Learned budget classifier (Zhai).** A gradient-boosted classifier on 16 cheap text features assigns a sampling budget per question, trained with a cost constraint. (d13)
5. **Entropy-gated second pass.** Run one greedy pass; if entropy or max-softmax says low confidence, run one more deliberate pass. (a27, d10)

All five save compute on easy items. The measured advantage over a plain uniform baseline at equal total samples is small (+1.5 to +4) and shrinks with budget (d11, d13). A simple window rule is as good as the fancy one for larger models (d11).

### 4.4 Retry context

Three options, with the Cao ablation numbers (N=100, pass@1 44.0): none (independent sampling) 45.0; compact (answers, JOL, reasons) 47.0; full prior reasoning 40.0 (a04, d02). Authors' explanation: anchoring on a failed trajectory. Counter-result: sequential full-context chains beat parallel ones in 43 of 45 matched-token cells (d16), but with a 4,096-token cap that may favour sequential. Both are single-seed or N=100. Treat retry context as a variable to test, not a rule.

### 4.5 Abstain and escalate

- **Abstain** means decline to answer. Our G6 forbids it on the first pass (a scaffold that abstained scored 0%).
- **Escalate** can mean: spend more compute, call a stronger model, call a tool or retrieval, or hand to a human.
- Evidence says the model's own act-or-escalate stance is unstable: thresholds from 53% to 91% accuracy within one model family, unrelated to scale (d17); abstention is independent of solving ability in agents and often late (d18). So the cut goes in code, with a threshold fitted on labelled cost ratios, placed before irreversible steps.
- Metrics that avoid fooling yourself: coverage, abstain accuracy, over-abstention rate, area under the risk-coverage curve (b23). ECE alone can pass a nearly empty signal (Gemma 4 joint ECE 0.044 with FOK AUROC 0.534; d04).
- Uncertainty type matters: a principled trigger for abstain-or-deliberate is high epistemic and low aleatoric uncertainty, estimated by iterative prompting that repeats the question with earlier answers (a26). Needs many calls. Snippet-level work on judge-retrieve-abstain, escalation meta-models and answer-instability signals exists (a28 to a30) but was not opened.

### 4.6 Uncertainty-triggered retrieval

- **FLARE:** draw the next sentence; if any token probability is below a threshold, retrieve with that sentence and redraw. Best when 40% to 80% of sentences trigger; more is not better (c19).
- **Adaptive-RAG:** a small classifier routes to no retrieval, one-step or multi-step. Matches multi-step quality at about half to a third of the time. Router accuracy is only 54.52% (No 30.52, One 66.28, Multi 65.45); a perfect router would give F1 62.80 against 50.91 (b22). Time units in the table are ambiguous (critique item 3), so treat the cost ratio as approximate.
- **Self-RAG:** a fine-tuned model emits reflection tokens. Always retrieving the top passage hurts on PopQA and ASQA (c20). Needs training; not a scaffold.
- **P(IK):** the model's know-it-or-not signal rises with relevant source text and falls with misleading hints (a17).
- **Lesson:** the gate beats both extremes, and gate quality is the limit.

### 4.7 Metacognitive prompting (no code gate)

A fixed script in one pass: understand the text, form a first judgment, critically evaluate it, decide with explanation, rate confidence. Gains of 4.8% to 6.4% relative over zero-shot CoT on language understanding, averaged over four models (c17). It runs the self-critique on every item, so it conflicts with G1, and it has no equal-token comparison.

---

## 5. What holds up

### 5.1 Holds up (two or more independent sources)

- **Spend by difficulty.** Snell (4x compute efficiency), Adaptive-RAG, UAB, Zhai all agree. Easy items need little; the hardest items gain from nothing (a24, b20, b22, d11, d13).
- **Stopping on agreement saves tokens for strong models at near-zero accuracy cost.** ESC on GPT-4: accuracy change 0.00 on MATH, GSM8K, CSQA with 33.8% to 80.1% fewer samples (b18); ASC matches UAB for the large models (d11).
- **Raw verbalized confidence is not enough.** GPT-4 AUROC 62.7 (b15); open reasoning models ECE 0.268, AUROC 0.635 (d15); only 1 of 9 models in Cao passes every row (b07).
- **Agreement is a better signal than one self-report, but not safe alone.** b15, d14, d15 for; d19 against.
- **Prompted self-critique without external feedback does not help 2023-era instruction models.** Huang, Kamoi, Tyen, Xu, Self-Refine's own math rows (a18 to a22, b11 to b14).
- **Models do not notice their own errors but fix them when told where they are.** Tyen (b14) and Tsui's user-versus-self blind spot (d08).
- **Debate is not better than voting at equal responses.** Huang (a19) and the guardrail research behind G9.
- **Self-bias grows with refinement.** Xu (a21) and Huang (a18).
- **Forced extra thinking flattens quickly.** s1 (b24), Cao's budget-forcing arm (a02).
- **Triggered retrieval beats always-retrieve.** FLARE, Adaptive-RAG, Self-RAG ablation (b22, c19, c20).
- **Act-or-escalate thresholds are not stable across models.** d17 and d18.

### 5.2 Does not hold up, or is not yet shown

- **The +8.6 as an equal-compute result.** Not shown. No plain best-of-2.4 or majority-vote arm (K02). Adjacent matched-budget tests found +1.5 to +4 (K29, d11, d13).
- **Directed beats random retry.** Cao: 47.0 vs 45.7 on N=100 with CIs 20 points wide, and the random arm's CI [43,48] looks like a different kind of interval (d02). Zhai found +3 to +4 on N=200 but for sampling allocation, not retry with feedback (d13).
- **The hand-built controller.** (1-JOL)xFOK scored 42.0 and FOK-only 42.0, both below pass@1 44.0. The harness is fragile to controller choice (a04).
- **Compact beats full context.** One study says yes at N=100 (b10); one says the opposite at matched tokens (d16).
- **FOK as a necessary piece.** Removing it cost 2 points, inside noise (b09).
- **Cacioli's correlation between monitoring and control.** r = .17, n = 20, power 0.25 for r = .3 (a13). Cannot say they are unrelated.

### 5.3 Moderators and boundary conditions

| Moderator | Direction | Ids |
|---|---|---|
| Model generation | 2023 instruction models: self-correction hurts. 2026 reasoning models: in-context correction near zero blind spot, prompted revision adds little for the token price | a18, d08, d09 |
| Model identity | Only Sonnet 4.6 of 9 passed all diagnosis rows; Gemma 4 FOK fails | b07, c08 |
| Model scale | Monitoring does not reliably improve with size; three families show three trends | a15 |
| Domain | Sonnet 4.6 withdraw delta ranges from +8.3 (learning) to +93.0 (executive); verbal confidence AUROC varies by domain in a 33-model atlas (abstract only, in critique) | a14, critique |
| Task difficulty | Gain at hard code (+19.6), none or slight loss at easy (-0.7); confident band 0.67 to 0.64 | b03, a03 |
| Compute budget | Adaptive allocation gain shrinks with budget (+1.8 at N=4 to +0.5 at N=16); controller loses at small budgets (56.6 vs 62.7 at 400 calls) | d11, d06 |
| Feedback type | Gains need an external signal: oracle, code run, tool. Without it, nil or negative | a22, a23, b13 |
| Baseline strength | A one-shot baseline makes any second pass look good; MMLU-Pro 60.72 to 84.03 is mostly "think again" | a27 |
| Signal source | Logprob signals fail when the model is confidently wrong (DeepConf, 8 of 20 settings hurt) | b19 |
| Over-confident model | Agreement can be uncorrelated or negatively correlated with truth | d19 |
| Sign of cued reconsideration | +5.97 for Qwen2.5-7B, -4.19 for Llama 3.1-8B | d10 |

### 5.4 Interventions that worked and that did not

Worked (with a caveat each): window-agreement stop (ESC); probe-and-allocate (UAB, +2.5 average); learned budget classifier (+3 to +4 over random); verbalized plus agreement (AUROC 84.2); compact retry history (47.0 vs 40.0, N=100); forced-index aggregator over a free-form synthesizer (design note); 'Wait' appended for non-reasoning models (blind spot -89.3%); oracle or code feedback revision (Huang, Reflexion on HumanEval 91 vs 80); gated second pass with a cue and entropy gate (d10).

Did not work: forced doubt on every item (our word puzzles 92% plain vs 75% forced); unstructured self-refine on math (GPT-4 92.9 to 93.1); debate at matched responses; max-JOL selection (44.0, no gain); last-answer selection (40.0); full prior reasoning in retry (40.0 on N=100); self-written tests as a gate (Reflexion MBPP); prompt-only ablation of a gated second pass (below baseline in Sun, a27); fixed hand rules.

---

## 6. Language models

### 6.1 How they behave

1. **Claude Sonnet 4.6 has real monitoring.** Joint FOK/JOL AUROC 0.757, ECE 0.087 on a 100-item anchor set (a05). On Cacioli's battery its withdraw delta is the largest of 20 (+39.4) (a11). Haiku 4.5 is second-best monitor despite accuracy rank 13 (a12).
2. **It rarely acts on it.** Answered directly on 98.6% of exploratory prospective items (a13). Unharnessed reasoning length does not rise with low confidence; Anthropic models often shorten on high confidence (a06, b26).
3. **Monitoring is domain-specific.** +8.3 to +93.0 inside one model (a14). Adversarial foils fooled 17 of 20 models; they stayed confident (a14).
4. **Monitoring is not accuracy.** Ranks nearly invert (a12).
5. **Other families differ.** Gemini 3 models are "blanket confidence" (KEEP at 95% or more); DeepSeek R1 withdraws 91% to 99% of items while near 100% accurate (a11, a15). Gemma 4 gives chance-level FOK (a05).
6. **Open reasoning models report poorly calibrated confidence** (ECE 0.268, AUROC 0.635) but agreement-based signals are good (SC@8 AUROC 0.836) (d15).
7. **Non-reasoning models have a self-correction blind spot** (64.5% average); reasoning-trained models do not (d08). Claude 3.5 Haiku 52.5% and Claude Sonnet 4 41.4% were in the 14-model set.
8. **Reasoning models overthink easy items** (1,953% more tokens on "2+3", first solution right in over 92% of cases) (b21, c23).
9. **Self-bias.** Models rate their own output above human scores, more so after each refinement round (a21).
10. **Escalation behaviour is model-specific.** Thresholds 53% to 91%, self-estimated accuracy 76% to 97% against actual 75% to 80% (d17).

### 6.2 What changed behaviour, and by how much

| Intervention | Model and task | Change | Ids |
|---|---|---|---|
| Full harness | Sonnet 4.6, pooled 1,859 | +8.6 (48.3 to 56.9) at 2.7x cost | a02 |
| Same, N=100 ablation subset | Sonnet 4.6 | +3.0 (44.0 to 47.0) | a04 |
| Harness on hard code | Sonnet 4.6 LCB Hard | +19.6 | b03 |
| Harness on easy code | Sonnet 4.6 LCB Easy | -0.7 | b03 |
| Harness on confident band | Sonnet 4.6 | 0.67 to 0.64 | a03 |
| Random retry, matched K | Sonnet 4.6, N=100 | 45.7 (1.3 below harness) | a04 |
| Independent 4-sample plus aggregator | Sonnet 4.6, N=100 | 45.0 | a04 |
| Budget forcing | Sonnet 4.6 pooled | +3.2 | a02 |
| Self-Refine | Sonnet 4.6 pooled | +4.1 (52.4) at $0.45 | a02 |
| Gated second pass | DeepSeek-v3.2, MMLU-Pro | 60.72 to 84.03; re-ask all 84.35 | a27 |
| 'Wait' appended | DeepSeek-V3-0324 | 0.567 to 0.902 on blind-spot set | d08 |
| Cued reconsideration | Small open models, Math | +8.41 pp paired (N=320,000) | d10 |
| UAB allocation | Qwen/Llama/GPT-OSS/Gemma, budget 4 | +1.5 to +2.7 average over uniform SC | d11 |
| Learned budget classifier | DeepSeek-V3 MATH N=200 | +3 to +4 over random at same cost | d13 |
| ESC | GPT-4 | 0.00 accuracy change, 33.8% to 80.1% fewer samples | b18 |
| Self-correction, no oracle | GPT-4 GSM8K | 95.5 to 89.0 over two rounds | a18 |
| Controller with compact state | GPT-5.5 ProgramBench | 71.5 vs 63.7 | d06 |
| Cost framing plus thinking | Qwen3.5-9B escalation | 62.0% to 78.8% cost-optimal | d17 |
| DeepConf | GPT-OSS-120B AIME25 | 99.9 vs vote 97.0 vs pass@1 91.8 | b19 |

### 6.3 Which results apply to Claude

Direct Claude evidence: Cao (Sonnet 4.6 harness), Cacioli (Sonnet 4.6, Haiku 4.5 profiles), Tsui (Claude 3.5 Haiku and Sonnet 4 blind spot). Every other number is from GPT-3.5/4, PaLM, open models of 1.5B to 235B, or DeepSeek. Treat those as direction, not size.

---

## 7. What our agent should take

Format: item | schema part | status | evidence | what to do. Status is [E] established, [S] single-source, [C] contested. Items marked [E] are safe as wording; items still needing our equal-token result go in "Test first" even where the idea is well-known. Under rule 3 of SCHEMA.md section 8, nothing here changes the schema until our own measurement agrees.

### 7.1 Add now (established)

1. **Allocate effort by difficulty, with a cheap difficulty signal; stop early on easy items.** Part: G12 and S0. [E] a24, b20, b22, d11, d13, b18. Already in G12. Add to S0 the concrete mechanism: a cheap pre-signal (class pass rate from memory, or a 2-probe agreement) decides how many attempts S3 draws.
2. **Never trust a raw verbalized confidence as a gate without measuring it.** Part: G1/S0 precondition and memory (class record). [E] b15, d15, b07, d04. Rule: before any gate is turned on, compute AUROC and ECE on labelled items, with a bootstrap lower bound on AUROC above 0.6 and ECE below 0.15, both together. Never accept ECE alone.
3. **Use agreement across a few short samples as a signal, and combine it with one other signal.** Part: S4 (no-check mode) and S7. [E] b15, d12, d14, d15; limit d19. Already close to the schema's G4 note that agreement is a hint. Add: agreement alone never approves an answer when the other signal is low.
4. **Stop-on-agreement window rule for repeated sampling.** Part: S3/S6. [E] b18, c22, d11. Stop drawing when a window of answers agrees. Saves 34% to 84% of samples at near-zero loss for strong models.
5. **Do not select among a model's own attempts by its stated confidence.** Part: G5/S7. [E] a07, b05, c06 plus a21 self-bias. The model's confidence is for deciding whether to spend, not for choosing.
6. **Do not use prompted self-critique without external output on non-reasoning or short-trace settings.** Part: G1, G2, G3. [E] for 2023-era models: a18, a22, b11, b13, b14. Scope wording: keep G1/G3 as is, but note "established for non-reasoning models; reasoning models are being tested" (see Test first, U7).
7. **Locate the error with code, then ask the model to fix it.** Part: S5 and G2. [E] b14, b13, a23.
8. **Debate is not worth adding.** Part: G9. [E] a19 plus guardrail research.
9. **Triggered beats always-on for retrieval or tool calls.** Part: S6 (impasse operators that call retrieval, O7). [E] b22, c19, c20.
10. **Code owns the act-or-escalate cut, and sits before irreversible actions.** Part: S8 and G6 (the cut is for escalation, never for first-pass abstention). [E] d17, d18. The threshold is set from labelled cost ratios, not from the model's stance.
11. **Log monitoring quality per run.** Part: section 6 logging. [E] as practice. Log the confidence the model gave, the outcome, the gate decision and the tokens, so AUROC, ECE and the per-band retry gain can be computed per class.

### 7.2 Test first (single-source, contested or untested)

| # | Item | Part | Status | Ids | Why test |
|---|---|---|---|---|---|
| T1 | Confidence-gated retry beats plain best-of-K plus majority vote at the same tokens | S0/S6/S7 | [S] | K01, K02, K29; a02, d03, d11 | Headline claim; no equal-token arm exists; adjacent tests give +1.5 to +4 |
| T2 | Directed retry beats random retry at matched K | S0/S6 | [C] | K04; a04, d02, d13 | 1.3 points on N=100 is noise |
| T3 | Stop decision versus extra attempts: which gives the gain | S0 vs S6/S7 | [U] | K29; d06 | No factorial ablation anywhere |
| T4 | FOK/JOL AUROC and ECE on our model and classes | S0 | [S] | K08, K26; a05, d15 | Precondition for any gate |
| T5 | Verbalized JOL vs 2-sample agreement vs both vs a verifier as the stop signal | S0/S3 | [C] | K25; d14, d19 | Only open models were tested |
| T6 | Compact history vs full trace vs none for retry | S6 | [C] | K06; a04, d16 | Opposite signs in two studies |
| T7 | Huang protocol (answer, then "review and revise", no feedback) on our reasoning model | G1/G3 | [C] | K10, K23; d08, d09, d10 | Guardrails rest on 2023 evidence |
| T8 | Regression-to-the-mean placebo for the low-confidence gain | S0 | [S] | K03; d10 | Gain may be inflated |
| T9 | Route by first-pass confidence to one of three strategies | S0 | [E] idea, untested here | K14; a24, a03 | Cost of estimating difficulty is not counted |
| T10 | Per-class diagnosis: switch the gate off in classes where AUROC fails | S0 | [S] | K17; a14, a15 | Monitoring is domain-specific |
| T11 | Entropy- or confidence-gated cued second pass ("Wait") | S5/S6 | [C] | K23; d08, d10, a27 | Sign flips across models |
| T12 | Audit false-negative rate of self-generated checks | G3 | [S] | K22; a23 | A bad check misleads a gate |
| T13 | Break-even budget of control overhead in agent tasks | S6/S8 | [S] | K27; d06 | Controller lost at small budgets |
| T14 | JOL with a written reason vs bare number | S0 | [S] | a08 | Cheap detail from Cao |
| T15 | Forced-index model aggregator vs code selection, with authorship hidden | S7/G5 | [S] | a08, b27, a21 | Aggregator is still a model judge |
| T16 | Skill-label retrieval from a solved-problem memory | S0/memory | [S] | c18 | Maps to class record and lessons |

Do not carry over: any numeric effect from the older studies (2022 to 2024 models) to Sonnet-class models.

---

## 8. Concrete tests on our bench

All arms get the same total token budget per item (include FOK, JOL, probe and aggregator tokens, and setup cost, per G7). Report accuracy per 1,000 tokens as well as accuracy. Use at least 500 items per suite where possible, 3 seeds, and a paired bootstrap on per-item differences. Planning number for the effect: +1.5 to +4 points over the matched plain baseline, not +8.6.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| E1. Headline at equal tokens (T1) | Mixed: ARC items with a check, BrainTeaser-type word puzzles, a hard code or science subset | (a) plain pass@1; (b) best-of-K plus majority vote at the harness's measured mean tokens; (c) harness (FOK, JOL, calibrated stop, compact retry, code or forced-index select); (d) ESC window stop with the same cap | Accuracy; accuracy per 1,000 tokens; paired difference (c) minus (b) | +0 to +4 over (b); more on hard items, none or slightly negative on easy |
| E2. Directed vs random retry (T2) | Same 500+ items | Gated retry vs random retry with the same mean K and same tokens | Paired bootstrap on per-item difference | +1 to +3; drop the gate if CI includes 0 |
| E3. Factorial (T3) | Same | Stop gate on/off x retry-with-compact-history on/off x selector on/off, plus plain best-of-K at the measured total | Main effect of each factor | Stop gate mostly saves tokens; the retry and selector carry the accuracy |
| E4. Signal audit (T4, T5, T10) | 300+ labelled items per problem class | JOL alone; FOK alone; joint; 2-sample agreement; JOL plus agreement; a verifier or code check where one exists | AUROC with bootstrap CI, ECE, accuracy of the stopped-at-first set | JOL plus agreement best; FOK weakest; some classes fail the 0.6 bar |
| E5. Retry context (T6) | Items whose first attempt failed | Compact summary vs full prior trace vs nothing, uncapped reasoning | Accuracy of the retry; tokens | Compact at least equal to nothing; full trace worse if anchoring is real |
| E6. Huang protocol (T7) | 500+ items with a known answer, short and long reasoning | (a) answer then "review and revise" with no feedback; (b) second independent sample; (c) tool-checked revision | Right-to-wrong and wrong-to-right counts; net accuracy at equal tokens | (a) near zero net or negative; (c) positive; if (a) is positive, narrow G1/G3 |
| E7. Regression placebo (T8) | Bands cut by an independent first read | Retry vs fresh independent re-ask in the same band, plus a no-retry arm | Gain in the low band over placebo | Placebo recovers part of the gain; real gain is what remains |
| E8. Routing (T9) | Easy, medium and hard strata by first-pass confidence | Fixed strategy vs route to {stop, sequential revise, parallel search} | Accuracy at equal total tokens | +1 to +3 total, mostly from token savings on easy items |
| E9. Cued second pass (T11) | Items with high first-pass entropy or low JOL | Cue ("Wait, recheck") vs plain re-ask vs none | Wrong-to-right minus right-to-wrong | Helps on reasoning models if gated; may hurt if applied to all |
| E10. Check false negatives (T12) | Code or rule tasks with self-written tests | Self-written tests as gate vs given tests | False-negative rate; accuracy under each | Some false negatives; set an audit threshold |
| E11. Agent break-even (T13) | Multi-step tasks with an external check | Flat-history agent vs agent with a code controller and compact state, at 100, 400, 1,200 calls, controller tokens charged to the budget | Success vs budget curve | Controller loses at small budgets; find the crossover |
| E12. Aggregator bias (T15) | Candidate pools with known best | Forced-index model aggregator vs code selection vs aggregator with authorship hidden and length-normalised | Pick versus best available | Code at least equal when a check exists |

---

## 9. What does not transfer, and why

| Result | Why it does not transfer directly |
|---|---|
| Cao's +8.6 | Single team, single solver, one run per cell on the full benchmarks, no seeds, code not released; tasks are single-turn QA and code, not agent loops |
| The SVM controller | Fitted per model on 100 anchors and picked from 134 configs; may overfit; FOK also enters the solve prompt, so it may change the solve, not only gate it |
| Cao's low-band gain | Bands cut by the same signal that drives control; regression to the mean not excluded |
| The 2023 self-correction failures | GPT-3.5/4 era. Reasoning models differ in blind spot (d08) and in value of revision (d09) |
| Older confidence numbers (Xiong, Kadavath) | 2022 to 2023 models; format effects (logprob P(True) vs verbalized) |
| DeepConf, FLARE, Self-REF, P(IK) | Need logprobs or fine-tuning; a black-box scaffold on the API has neither |
| Self-RAG, Self-REF, Kapoor, early-stopping training | Training-based; we do not train |
| ESC savings | Measured on GPT-3.5/4 and Llama-2; works less for weak models and hard tasks (MATH saved only 33.8%) |
| UAB and Zhai gains | Small open models, math, short outputs, voting only; no feedback retry; N=200 in Zhai |
| Adaptive-RAG cost ratio | Time units ambiguous; router only 54.5% accurate |
| Cacioli's profiles | Single administration, alpha 0.54, n = 20, thresholds are conventions (a 5-point shift reclassifies 9 or 10 of 20 models) |
| Meta agentic controller (d06) | Matched on calls not tokens; direct agent uses 18% of its calls; no component isolated; not uncertainty-gated |
| Escalation studies (d17, d18) | One-step recorded decisions or an abstract page only; no Claude |
| Metacognitive prompting | Understanding tasks, not hard reasoning; always-on self-critique conflicts with G1 |
| Human metacognition effects | The human FOK/JOL literature is not evidence for LLM behaviour; the 2026 LLM studies are the only relevant data |

---

## 10. Open questions

1. Does the harness beat plain best-of-K plus majority vote at equal tokens on a 2026 frontier model, with seeds and paired tests? (U1)
2. Is directed retry better than random retry on N of 500 or more? (U2)
3. How much of any gain comes from the stop decision and how much from extra attempts plus the selector? (U3)
4. How many labelled anchor items are needed before a controller stops overfitting? Is AUROC at least 0.6 on 100 items stable? (U4)
5. Does the low-confidence gain survive correction for regression to the mean? (U8)
6. Does compact history beat full and none at equal tokens, and is the anchoring story real? (U6)
7. Does intrinsic self-correction still fail on Sonnet 4.6 and similar? (U7)
8. Which stopping signal works best without logprobs on Claude: JOL, agreement, both, or a verifier? (U5)
9. Does any confidence-gated stop help on multi-step agent tasks with external feedback? (U10, U11)
10. Is there an independent replication of Cao? None as of 2026-10-26.
11. Why is the harness candidate set better (oracle 62.2) than four independent samples (60.5)? Compact feedback, FOK in the solve prompt, or something else? (d03)
12. Do the 33-model atlas findings (verbal-confidence monitoring depends on domain, Anthropic profile shape varied over four generations; abstract only) change the gate design? Read the full paper.
13. What is the cost of the cheap difficulty estimate, and does it eat the savings? Snell does not count it. (b20)
14. Links to parallel subfields in this run (not covered here): Accuracy and dissociation of monitoring (calibration and the monitoring-control gap in depth); Adaptive stopping and metareasoning (formal value-of-computation rules); Verification design (what checks to run in S4/S8); Progress monitoring theory (when to leave an approach); Soar impasses (the S6 trigger set); LLM debugging (revision from real output).

---

## 11. Sources

[V] = opened and read this session or by the research agents (evidence line has opened:true). [M] = snippet or abstract-level only. Where the critique re-opened a PDF, that is noted.

**Core 2026 monitoring and harness work**

- [V] Cao, Wang, Qin, Zhang, Xie (2026). LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling. https://arxiv.org/abs/2605.14186 (PDF https://arxiv.org/pdf/2605.14186). Re-opened in cross-check and in d01 to d05.
- [V] Cacioli (2026). The Metacognitive Monitoring Battery. https://arxiv.org/abs/2604.15702. Re-opened in cross-check.
- [M] 33-model monitoring atlas, https://arxiv.org/abs/2605.06673 (abstract only; found in cross-check).
- [V] Dahal, Bakhtin, Cohen et al. (2026). Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning. https://arxiv.org/abs/2609.38147
- [V] Liu, Gani, Lu, Thomas, Steyvers, Cohan (2026). Metacognition in LLMs: Foundations, Progress, and Opportunities. https://arxiv.org/abs/2607.11881
- [V] Sun (2026). Reinforcement Inference. https://arxiv.org/abs/2602.08520

**Self-correction and self-evaluation**

- [V] Huang et al. (2024). Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (re-opened in cross-check; Table 7 numbers corrected)
- [V] Kamoi et al. (2024). When Can LLMs Actually Correct Their Own Mistakes? https://arxiv.org/abs/2406.01297 (abstract and introduction only, per b13)
- [V] Tyen et al. (2024). LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516
- [V] Xu et al. (2024). Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement. https://arxiv.org/abs/2402.11436
- [V] Madaan et al. (2023). Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Shinn et al. (2023). Reflexion. https://arxiv.org/abs/2303.11366
- [V] Tsui (2026). Self-Correction Bench. https://arxiv.org/abs/2507.02778
- [V] Tie et al. (2025). Can LLMs Correct Themselves? (CorrectBench). https://arxiv.org/abs/2510.16062
- [V] d'Aliberti and Horta Ribeiro (2026). The Illusion of Insight in Reasoning Models. https://arxiv.org/abs/2601.00514

**Confidence, calibration and uncertainty**

- [V] Kadavath et al. (2022). Language Models (Mostly) Know What They Know. https://arxiv.org/abs/2207.05221
- [V] Xiong et al. (2024). Can LLMs Express Their Uncertainty? https://arxiv.org/abs/2306.13063 (re-opened in cross-check)
- [V] Kapoor et al. (2024). Large Language Models Must Be Taught to Know What They Don't Know. https://arxiv.org/abs/2406.08391
- [V] Abbasi Yadkori et al. (2024). To Believe or Not to Believe Your LLM. https://arxiv.org/abs/2406.02543
- [V] Zollo, Wang, Zemel (2026). Binary Agreement for Efficient Unsupervised Confidence Calibration of Reasoning LLMs. https://arxiv.org/abs/2604.19444
- [V] Del et al. (2026). How Uncertainty Estimation Scales with Sampling in Reasoning Models. https://arxiv.org/abs/2603.19118
- [V] Ding (2026). When LLMs Agree, Are They Right? https://arxiv.org/abs/2607.08065
- [V] Ma, Yuan, Wang, Zhou (2025). LLMs Have Intrinsic Meta-Cognition, but Need a Good Lens. https://arxiv.org/abs/2506.08410

**Stopping and allocation**

- [V] Wang et al. (2023). Self-Consistency Improves Chain of Thought Reasoning. https://arxiv.org/abs/2203.11171
- [V] Li et al. (2024). Escape Sky-high Cost: Early-stopping Self-Consistency. https://arxiv.org/abs/2401.10480 (re-opened in cross-check)
- [V] Fu et al. (2025). Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (first 100k of 107k characters of the HTML)
- [V] Snell et al. (2024). Scaling LLM Test-Time Compute Optimally. https://arxiv.org/abs/2408.03314 (first 100k of 111k characters)
- [V] Muennighoff et al. (2025). s1: Simple test-time scaling. https://arxiv.org/abs/2501.19393
- [V] Chen et al. (2025). Do NOT Think That Much for 2+3=? https://arxiv.org/abs/2412.21187
- [V] Nguyen, Gupta, Le (2026). Uncertainty-Aware Budget Allocation for Adaptive Test-Time Reasoning. https://arxiv.org/abs/2605.26849
- [V] Zhai et al. (2026). Adaptive Test-Time Compute Allocation via Constrained Policy Optimization. https://arxiv.org/abs/2604.14853
- [V] Sharma and Chopra (2025). The Sequential Edge. https://arxiv.org/abs/2511.02309

**Retrieval, routing, prompting**

- [V] Jiang et al. (2023). Active Retrieval Augmented Generation (FLARE). https://arxiv.org/abs/2305.06983
- [V] Asai et al. (2024). Self-RAG. https://arxiv.org/abs/2310.11511 (table cells garbled, none copied)
- [V] Jeong et al. (2024). Adaptive-RAG. https://arxiv.org/abs/2403.14403 (re-opened in cross-check; time ratio flagged approximate)
- [V] Chuang et al. (2025). Learning to Route LLMs with Confidence Tokens. https://arxiv.org/abs/2410.13284
- [V] Wang and Zhao (2024). Metacognitive Prompting Improves Understanding in LLMs. https://arxiv.org/abs/2308.05342
- [V] Didolkar et al. (2024). Metacognitive Capabilities of LLMs: An Exploration in Mathematical Problem Solving. https://arxiv.org/abs/2405.12205

**Abstain, escalate, agents**

- [V] Wen et al. (2024). Know Your Limits: A Survey of Abstention in LLMs. https://arxiv.org/abs/2407.18418 (first 100k of 136k characters)
- [V] DosSantos DiSorbo and Ju (2026). Act or Escalate? https://arxiv.org/abs/2604.08588
- [V, abstract page only] Liu et al. (2026). AgentAbstain. https://arxiv.org/abs/2607.10059
- [M] Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees. https://arxiv.org/abs/2608.17994
- [M] Learning When to Escalate (AAMAS 2026). https://arxiv.org/abs/2601.07006
- [M] Answer instability as a black-box signal (ACL 2026 SRW). https://aclanthology.org/2026.acl-srw.72.pdf

**Search notes**

- [M] Search note on replication of Cao (c26): no independent replication found on 2026-10-25 or 2026-10-26 (WebSearch and arXiv API; quota ran out partway through the second pass).
