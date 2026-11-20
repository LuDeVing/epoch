# RL on verifiable rewards: deep document

*Subfield C01.09. Scope: training LLMs for longer, better reasoning with reinforcement learning where a program checks the answer (RLVR). The DeepSeek-R1 line is the centre. Why it matters to us: background only. Our agent is a scaffold, not a trained model. We use this literature to learn which behaviours a scaffold should imitate, which claims to distrust, and how to measure fairly. Evidence ids (a01-d20) point to evidence_a-d.jsonl in this folder; claim ids (K01-K26) point to claims.jsonl. Overlap with other documents in this series is noted, not repeated.*

## 1. What it is

RLVR means reinforcement learning from verifiable rewards. The reward comes from a program, not from a human or a neural reward model. Examples: the final math answer matches the key; unit tests pass; the output follows a required format. The reward is usually binary, or a small sum of an accuracy term and a format term.

The loop:
1. Give the model a question with a checkable answer.
2. Sample a group of long answers (chains of thought).
3. Run the checker on each. Reward 1 or 0.
4. Update the model so rewarded chains become more likely.
5. Repeat for thousands of steps.

The name RLVR was coined by Tulu 3 (Lambert et al. 2024; a06, c19). The method became famous with DeepSeek-R1-Zero (a08): pure RL on a base model took AIME 2024 pass@1 from 15.6% to 77.9% (majority vote 86.7%). Kimi k1.5 reached AIME 77.5 independently (a12, c18).

What it is not: not process supervision (no step labels), not human-preference RL (RLHF), not distillation (copying a teacher's traces). Distillation and RLVR give different results (section 5).

Why it is in this study: the trained behaviours (check your work, back up, set subgoals, spend more tokens on hard items) can be asked for in a prompt or enforced in code. The literature also supplies cautions about evaluation that apply directly to our bench.

## 2. History and theories in depth

### 2.1 Before R1: outcome-only training of reasoning
- **STaR (Zelikman et al. 2022; a01, a02).** Sample rationales, keep those whose final answer is correct, fine-tune, repeat. This is expert iteration with an outcome filter. GPT-J 6B on CommonsenseQA: 72.5% with rationalisation, 68.8% without, against 73.0% for a fine-tuned GPT-3 about 30 times larger. GSM8K: few-shot CoT 3.1%, direct fine-tune 5.8%, STaR 10.1% (no rationalisation) and 10.7% (with). Known flaw: a correct answer can come from a flawed chain, and STaR keeps such chains (K17).
- **DeepSeekMath and GRPO (Shao et al. 2024; a03-a05).** GRPO drops the PPO value network. For each question it samples a group of outputs and uses the group mean (and spread) of rewards as the baseline. DeepSeekMath-Instruct 7B after RL: GSM8K 82.9 to 88.2, MATH 46.8 to 51.7, CMATH 84.6 to 88.8. The paper already saw RL raise Maj@K but not Pass@K (a04), the first hint of the later "sharpening" debate. It also gave a unified view: SFT, rejection-sampling fine-tuning, DPO, PPO and GRPO are variants of one gradient with different data source, reward and coefficient (a05).
- **Tulu 3 (Lambert et al. 2024; a06, a07, b05).** RLVR as the last step after SFT and DPO, on math (GSM8K, MATH) and precise instruction following (IFEval). Reward: a constant if verified correct, else zero. On 405B, even 25 RLVR steps raised MATH by over 5 points. Gains were domain-specific. IFEval over-optimised at high KL, so the authors built an out-of-distribution IFEval set to detect it.

### 2.2 The R1 line (January 2025)
- **DeepSeek-R1-Zero (a08, a09, b01, c01).** GRPO on a base model with two rule rewards only (accuracy, format; equal weight). No neural reward model, no SFT. Response length grew steadily. A mid-training trace showed an "aha moment": the model wrote "Wait, wait" and rechecked.
- **DeepSeek-R1 (a10, c03).** R1-Zero was hard to read and mixed languages. Full pipeline: cold-start SFT, reasoning RL with a language-consistency reward, rejection-sampling SFT, then RL for all scenarios. Table values: AIME 2024 R1 79.8 vs o1-1217 79.2; MATH-500 97.3 vs 96.4; GPQA Diamond 71.5 vs 75.7; Codeforces 2029 (96.3 percentile); LiveCodeBench 65.9; SWE Verified 49.2; Aider-Polyglot 53.3. (Critique correction: c03's "78.1" for o1 belongs to another column; use 79.2.)
- **Negative results (a11, b04, c04).** The authors tried PRMs and MCTS and dropped both. PRM limits: hard to define fine steps, hard to judge them, reward hacking once a model-based PRM is added. MCTS: token search space too large. No ablation numbers.
- **Limits the authors state (a11).** Reliable rule rewards exist only for verifiable tasks. Scaling pure RL to tasks without a reliable reward is open.
- **Kimi k1.5 (a12, c18).** Independent lab, same finding. No MCTS, value function or PRM. Partial rollouts make 128k contexts affordable. Long-CoT: AIME 77.5, MATH-500 96.2, Codeforces 94th percentile, MathVista 74.9. Short-CoT via "long2short": AIME 60.8, MATH-500 94.6, LiveCodeBench 47.3.

### 2.3 Open reproduction and algorithm fixes (spring 2025)
- **DAPO (a13, a14, b17, c14).** Naive GRPO on Qwen2.5-32B reached only 30 on AIME 2024, against 47 reported for R1-Zero-style RL at that size. Fixes: Clip-Higher (decoupled clip range keeps entropy up), Dynamic Sampling (drop groups that are all right or all wrong), token-level loss, overlong filtering and soft overlong punishment. Ladder: 30, +overlong filtering 36, +clip-higher 38, +soft overlong 41, +token-level loss 42, +dynamic sampling 50, in half the training steps.
- **Dr. GRPO (Liu et al. 2025; a15, a16, b14-b16, c07, c08).** GRPO divides by response length and by reward std. Both biases favour long wrong answers (less penalty per token). Removing them keeps accuracy with shorter outputs. Recipe: Qwen2.5-Math-7B, MATH level 3-5, 43.3% AIME 2024 in 27 hours on 8 A100.
- **SimpleRL-Zoo (Zeng et al. 2025; b25, b26, c05, c06).** Zero-RL on 10 base models (Llama-3-8B, Mistral-7B and 24B, DeepSeek-Math-7B, Qwen2.5 0.5B to 32B, Qwen2.5-Math-7B). Most improved. Mistral-Small-24B: by iteration 100 pass@1 exceeded the base's initial pass@8 by over 30 points on average. Length growth did not always come with more verification. Reported length counted truncated outputs, so a separate stopped-length and clip-ratio metric was needed.

### 2.4 "Is it really learning?" (April to October 2025)
Four competing explanations of where RLVR gains come from:
1. **Sharpening.** RL makes already-possible answers likelier and loses rare ones (Yue et al.: a17, a18, b06-b08, c09, c10; Wu et al. "Invisible Leash": c21, d19).
2. **Elicitation of pretraining priors.** RL selects a behaviour already in the base (Spurious Rewards: a19, a20; Gandhi et al.: b18-b20; Venhoff et al.: d02).
3. **Contamination and format.** Part of the gain on Qwen2.5 is leakage and template repair (Wu et al.: b21, c20; Dr. GRPO: a16; one-shot RLVR: a21).
4. **Real expansion.** With KL control, resets and diverse data the boundary moves (ProRL: a23, c17, d18; pass@k reward: d20).

They are not mutually exclusive. Section 5 sorts the evidence.

### 2.5 Beyond math and beyond ground truth (2024 to 2026)
- Code and software: SWE-RL (d03), Kimi-Dev (d05), SWE-Gym with verifiers (d04).
- Self-play with an executor: Absolute Zero (c23). Agent loops: Reflect, Retry, Reward (c24).
- Intrinsic or soft rewards: TTRL majority-vote reward (d09), Intuitor self-certainty (d10), Rubrics as Rewards (d11).
- Training-free alternatives: power sampling (d01), steering (d02), s1 budget forcing (d15), NoThinking (d16).
- Length and efficiency: L1 (d14), overthinking (d13), test-time scaling mirage (d12).
- Safety of the chain of thought: faithfulness (b27, b28, d06), CoT monitoring (d07).
- Evaluation hygiene: Sober Look (b23, b24), MathArena (d08).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pure outcome RL trains long reasoning | R1-Zero AIME 2024 pass@1 15.6 to 77.9; majority vote 86.7; Kimi k1.5 AIME 77.5 | a08, b01, a12, c18 (K01) | established (2 labs) |
| Final R1 vs o1 | AIME 2024 79.8 vs 79.2; MATH-500 97.3 vs 96.4; GPQA 71.5 vs 75.7 | a10 | single-source (paper table) |
| R1 still gains from sampling | pass@1 79.8, majority 86.7, pass@64 90.0 | b02 (K14) | single-source |
| Voting on a non-reasoning model is no substitute | GPT-4o AIME 2024 9.3 to 13.4 with 64 votes vs R1 79.8 | b03 (K14) | single-source |
| PRM and MCTS dropped | No ablation numbers | a11, b04, c04, a12 (K02) | single-source, qualitative |
| GRPO works in a math 7B | DeepSeekMath GSM8K 82.9 to 88.2; MATH 46.8 to 51.7 | a03 (K03) | single-source |
| Naive GRPO does not reproduce R1-Zero | Qwen2.5-32B AIME 30 vs 47; DAPO ladder 30/36/38/41/42/50 | a13, b17 (K04) | single-source |
| GRPO length and std bias | Dr. GRPO 43.3% AIME 2024, 27 h on 8 A100 | a15, c08 (K05) | single-source |
| RLVR sharpens: pass@1 up, large-k pass@k down | Sampling-efficiency gap above 40 points for 6 algorithms (GRPO 43.9, RLOO 42.6); training-set pass@1 26.1 to 42.5 while pass@256 falls; Qwen2.5-32B Minerva base beats RL by about 9% at k=128 | a17, b06, b07, c09 (K06) | contested |
| Question-level support shrinks | AIME 2024 pass@8192 base 93.3 vs ProRL-1.5B-v1 83.3; one set at 1,024 attempts base 40 vs ProRL 30 | d19, c21 (K07, K26) | contested |
| Prolonged RL can expand | R1-Distill-1.5B: +14.7 math, +13.9 code, +54.8 logic, +25.1 STEM, +18.1 instruction following; +4.6 math and +6.5 code over specialised baselines; 136K problems; about 16k GPU hours | a23, c17, d18 (K07) | contested |
| Zero RL beats base pass@8 | Mistral-Small-24B pass@1 above base pass@8 by over 30 points at iteration 100 | b25 (K07) | contested |
| Pass@k reward keeps coverage | Llama3.2-3B-Instruct AIME 2024 pass@1/pass@k 1.5/17.3 baseline; 13.6/26.7 pass@k training (as extracted) | d20 (K26) | single-source |
| Spurious rewards work on Qwen2.5-Math-7B | MATH-500 truth +29.1, random +21.4; AMC format +13.8, incorrect +24.1, random +21.4 vs 27-29 truth; AIME24 format +10.3, truth +15.3 | a19, b09, c11 (K08) | single-source |
| Mechanism: code-style reasoning | 65% to over 90% of answers; accuracy 60.9% with vs 28.0% without (main text) | a20, b10, c12 (K08) | single-source |
| Spurious gains do not transfer; Qwen is contaminated | Llama3.1-8B, Llama3.2-3B, OLMo2-7B flat or negative; Qwen2.5-Math-7B completes 54.60% of MATH-500 from a 60% prefix (65.80 at 80%, 39.20 at 40%) vs Llama 3.8 and 2.4 | a24, b11, b21, c20 (K09) | established |
| One example is enough on Qwen | Qwen2.5-Math-1.5B MATH500 36.0 to 73.6 (8.6 beyond format); 6-benchmark mean 17.6 to 35.7 (7.0 beyond format); 1.2k set 73.6 and 35.9; 2 examples 74.8 and 36.6 | a21, b12, c13 (K12) | single-source |
| Base priors decide success | Countdown after RL: Qwen-3B about 60%, Llama-3B about 30%; primed Llama matches or beats Qwen; empty-CoT primer stays 30-35%; incorrect-but-structured primers match correct ones | b18, b19, c15, c16 (K10) | established |
| Behaviour counts rise after RL | MATH backtracking 0.15 to 0.59, verification 0.02 to 0.29; accuracy 38 to 50 | b20, c16 (K10) | established |
| Aha moment exists before RL | DeepSeek-V3-Base already reflects; reflection frequency not positively correlated with accuracy | a16, b15, c06 (K11) | established |
| Steering recovers most of the RL gap | About 76% of the RL gap, about 11% of the SFT-distillation gap; 9 model pairs, 0.5B to 32B | d02 (K20) | single-source |
| Power sampling nearly matches GRPO | Qwen2.5-Math-7B MATH500: base 49.6, low temp 69.0, power 74.8, GRPO 78.5; about 8.8x tokens | d01 (K19) | single-source |
| Evaluation is fragile | Pass@1 SD 5-15 points over 20 seeds (AIME24, AMC23; not re-verified); one question moves pass@1 over 3 points; hardware changed AIME24 19.3 to 23.0 | b23, b24 (K13) | single-source |
| AIME 2024 is contaminated | Most models 10-20 points above a human-aligned line; QwQ-Preview-32B about 60 above; models released before Sept 2024 scored under 10% on clean sets | d08 (K13, K25) | single-source |
| Math RL transfer | RL-on-math gains across reasoning and non-reasoning tasks; SFT-on-math limited (one task average -5.6); Tulu 3 gains domain-specific | c22, a07, c19 (K15) | contested |
| Longer chains first help then hurt | 82.2 to 87.3 (385 to 1,100 tokens) then 70.3 at 15,980; sequential -11.8% vs parallel +10.1% at equal budget | d12 (K21) | established |
| Overthinking | 2+3=? uses 1,953% more tokens; first round right in over 92% of cases, under 60% of tokens | d13 (K21) | established |
| Length control | L1 beats s1 budget forcing by 100-150% relative, 20-25% absolute at 512 and 1024 tokens; length error about 3% on math | d14 (K21) | single-source |
| Budget forcing without RL | s1-32B AIME24 50.0 to 56.7; MATH500 92.6 to 93.0; GPQA 56.6 to 59.6 | d15 | single-source |
| NoThinking at equal tokens | AMC23 at 700 tokens NoThinking 51.3 vs Thinking 28.9; parallel NoThinking plus verifier beats Thinking at similar latency | d16 (K21, K22) | single-source |
| Self-correction needs an outside signal | GPT-3.5 GSM8K 75.9 standard, 95.5 oracle-gated, 75.1 then 74.7 intrinsic; GPT-4 95.5 to 91.5 to 89.0; debate loses to self-consistency (83.0 vs 88.2 at 9 responses) | d17 (K22) | established |
| CoT is not faithful | Faithfulness 25% (Claude 3.7 Sonnet), 39% (R1); misaligned hints 20% and 29%; RL plateaus at 28% MMLU and 20% GPQA; hacks verbalised in under 2% in 5 of 6 environments | b27, b28, d06 (K16) | established |
| CoT monitoring | Recall on systemic hacks: CoT monitor 95% vs action-only 60%; strong optimisation against the monitor produces obfuscation | d07 (K16) | established (with d06) |
| Code and SWE gains | SWE-RL 41.0% SWE-bench Verified; repair with oracle files greedy 5.4, vote 16.6, SFT 29.6, RL 34.8; format correct 12.2% to 95.6%; Kimi-Dev 60.4%; SWE-Gym plus verifier 32.0 (Verified), 26.0 (Lite) | d03, d04, d05 (K23) | single-source |
| Intrinsic and soft rewards | TTRL Qwen2.5-Math-7B AIME 12.9 to 40.2, AMC 35.6 to 68.1, MATH-500 46.7 to 83.4; Intuitor Qwen2.5-1.5B LiveCodeBench 0 to 9.9; RaR up to 31% relative on HealthBench and 7% on GPQA-Diamond over Likert judge | d09, d10, d11 (K24) | single-source |
| Self-play and reflection RL | Absolute Zero +5.7/+10.2/+13.2 (3B/7B/14B); Reflect-Retry-Reward up to +34.7% Countdown, +18.1% APIGen | c23, c24 (K18) | single-source |

## 4. Mechanisms and models

Written so an engineer could rebuild the pieces. We do not train, so section 7 says which pieces have a prompt-time or code-time analogue.

### 4.1 The RLVR training loop
```
for step in range(N):
    batch = sample_questions(B)
    for q in batch:
        outs = [policy.generate(q, T=1.0, max_len=L) for _ in range(G)]   # G = 8..16 typical
        r    = [verify(q, o) for o in outs]                               # 1/0, plus format term
        A    = (r - mean(r)) / (std(r) + eps)                             # group-relative advantage (GRPO)
        loss = -sum_i sum_t min(ratio_it*A_i, clip(ratio_it, 1-eps_lo, 1+eps_hi)*A_i)
        # optional KL(policy || reference) term
    policy.update(loss)
```
Notes from the evidence:
- The group baseline replaces the critic (a03).
- Dr. GRPO: drop the 1/len(o_i) factor and the std division (a15, b16).
- DAPO: eps_hi > eps_lo (Clip-Higher); skip groups where all r are equal (Dynamic Sampling); average the loss over tokens; filter or softly punish truncated overlong outputs (a14, b17).
- The verifier is rule code: normalised answer match, unit tests, format regex. No neural reward model, because of reward hacking (b04).

### 4.2 Why length grows
Two causes in the evidence. (1) The length-normalisation bias makes long wrong answers cheap (b16). (2) Longer chains hold more checks and retries, which the base already knows how to produce (a16, b15). Length growth alone is not evidence of better reasoning: reflection frequency was not positively correlated with accuracy in R1-Zero (b15), and SimpleRL-Zoo saw length rise without more verification in some bases (c06).

### 4.3 Why spurious rewards can work (clipping bias)
With a random reward the expected advantage is about zero. The clip term is asymmetric, so behaviours the base already favours get amplified (a20, b10). For Qwen2.5-Math-7B the amplified behaviour is code-style reasoning without execution (65% to over 90%); those answers are 60.9% accurate vs 28.0% without. Reading: RL with a noisy reward is a sharpening operator on the prior. It cannot help if the prior behaviour is not useful (Llama and OLMo: flat or negative).

### 4.4 The base-model prior
Four behaviours predict RL success: verification, backtracking, subgoal setting, backward chaining (b18, c15). Procedure to test a base: count these behaviours in sampled outputs. If absent, prime with synthetic traces containing them (even with wrong answers), or continue pretraining on text filtered for them (b19, b20). Empty-CoT primers of the same token length do nothing, so the effect is structure, not length.

### 4.5 Pass@k and the sampling-efficiency gap
pass@k is the probability that at least one of k samples is correct (unbiased estimator from n >= k samples). Yue et al. read base pass@256 as a proxy for its ceiling. The gap between that ceiling and RL pass@1 is the sampling-efficiency gap (above 40 points; b07). Reading: RL moves probability toward answers the base could already reach. Support analysis (d19) counts, per question, whether a verified success is gained or lost after RL. Reward design can change the picture: a pass@k reward keeps coverage (d20).

### 4.6 Training-free analogues
- **Power sampling (d01).** Sample from p(x)^alpha (alpha > 1) with MCMC over partial sequences. About 8.8x the tokens. Low temperature alone gives 49.6 to 69.0 on MATH500 for Qwen2.5-Math-7B, so much of the "gain" is sharpening.
- **Steering (d02).** Per-behaviour direction vectors from activations (backtracking, verification); a classifier trained on a thinking model decides when to apply them. The hybrid recovers about 76% of the RL gap and about 11% of the SFT gap. Needs model internals.
- **Budget forcing (d15).** When the model tries to stop, append "Wait"; truncate to cap length.
- **NoThinking (d16).** Skip the thinking block, sample many short answers, pick with a verifier or confidence.

### 4.7 Intrinsic and soft rewards
- Majority-vote reward (d09): label each sample by agreement with the group majority; train on that.
- Self-certainty (d10): reward the model's own confidence.
- Rubrics (d11): an LLM judge scores against a per-instance checklist. Generic fixed rubrics did worse than instance-specific ones.

## 5. What holds up

### 5.1 Replicated
- **Outcome-only RL lifts long-chain math.** R1-Zero, Kimi k1.5, SimpleRL-Zoo (10 bases), Dr. GRPO, DAPO, one-shot RLVR and TTRL all show large pass@1 gains on math benchmarks (K01).
- **Base priors decide the result.** Gandhi et al., Dr. GRPO, Spurious Rewards and Venhoff et al. agree from different angles (K10).
- **The aha moment is not unique to RL.** Dr. GRPO and SimpleRL-Zoo (K11).
- **Qwen2.5 is contaminated on public math sets.** Prefix completion 54.60% vs Llama 3.8% (b21); template result (a16); AIME 2024 contamination (d08) (K09).
- **Longer single chains eventually hurt; parallel samples keep gaining.** d12, d13, d16 (K21).
- **Self-correction without an outside signal does not help.** d17; debate vs self-consistency (d16); verifier gates SWE gains (d04) (K22).
- **CoT is not a faithful record; strong optimisation against a CoT monitor produces obfuscation.** b27, d06, d07 (K16).

### 5.2 Contested
- **Does RLVR expand the reasoning boundary?** For: ProRL (a23, d18), SimpleRL-Zoo (b25), pass@k reward (d20). Against: Yue et al. (a17), Wu et al. (d19), the early DeepSeekMath note (a04). Setups differ in base model, steps, KL control, data diversity and k. ProRL gains are largest where the base is weakest and negative where it is strong (d18). Unresolved (K06, K07, K26).
- **Does math RL transfer?** Huan et al. (c22): RL-on-math transfers, SFT-on-math does not. Tulu 3: domain-specific gains (a07). Unresolved (K15).
- **Spurious rewards.** Real on Qwen2.5-Math in that paper, but Wu et al. (b21, b22) attribute part of it to contamination; on a clean generated arithmetic set only accurate rewards gave steady gains. One group for the main result (K08).

### 5.3 Failed or weak replications and corrections
- Naive GRPO did not reproduce R1-Zero: 30 vs 47 on AIME 2024 (K04).
- RL gains on AIME24 did not carry to AIME25. RL on Qwen bases gave gains comparable to or below instruction tuning. SFT on reasoning traces generalised better in those runs. INTELLECT-2 gave no gain over QwQ-32B. Early RL on R1-distilled models gave minimal gains (b24).
- Hardware moved AIME24 pass@1 from 19.3 to 23.0 (b23).
- OLMo2-7B-SFT gains of +8.9 and +5.5 appear only under some reward types; the paper says it degrades under standalone format or incorrect rewards. Do not read it as spurious rewards working off-Qwen.
- Correction: o1-1217 AIME 2024 is 79.2 in the R1 table, not 78.1.

### 5.4 Moderators
- **Base model family.** Qwen2.5 helps and is contaminated; Llama and OLMo need priming (b18, b11).
- **Prompt template.** A wrong template can destroy base ability before RL repairs it (a16). Part of the gain is format repair: 8.6 of the one-shot 36.0-to-73.6 is beyond format (a21); SWE-RL format compliance 12.2% to 95.6% (d03).
- **Question difficulty matched to the model** (b26).
- **Domain.** Gains mostly in the trained domain (a07); math pretraining raises the RL ceiling (a25).
- **Evaluation.** Seeds (5-15 point SD), hardware, sampling budget k, contamination (b23, d08).
- **Verifier quality.** In correction loops the verifier carries the gain: 95.5 oracle vs 74.7 intrinsic (d17).

### 5.5 What worked and what did not
Worked: group-relative baselines; DAPO's four fixes; removing length bias; KL control with resets for long runs (ProRL claim); priming with reasoning behaviours; pass@k reward for coverage; verifier-gated best-of-N; instance-specific rubrics; capping chain length with parallel sampling.
Did not work, or no evidence of working: PRMs and MCTS at scale (qualitative); naive GRPO; correcting without a check; debate; majority vote on a non-reasoning model as a substitute for reasoning RL; fixed generic rubrics; forcing ever-longer chains.

## 6. Language models

- **Base to R1-Zero.** AIME 2024 15.6 to 77.9 (a08). Length grows. Readability and language mixing suffer; cold-start data and a language reward fix it (a10).
- **Qwen2.5-Math-7B (workhorse of the critique papers).** MATH-500 base 49.6; low temperature 69.0; power sampling 74.8; GRPO 78.5 (d01). Spurious rewards give +21.4 to +29.1 (a19). Contaminated: completes 54.60% of MATH-500 from a 60% prefix (b21). TTRL took AIME 12.9 to 40.2 with no labels (d09). Dr. GRPO reached 43.3% AIME 2024 (a15).
- **Qwen2.5-Math-1.5B.** One example: MATH500 36.0 to 73.6; mean 17.6 to 35.7 (a21). Template changes alone swing results (a16, c07; the c07 table was garbled, so not cited).
- **Qwen2.5-32B.** Naive GRPO 30; DAPO 50; R1-Zero-style 47 (b17). Minerva: base beats RL by about 9% at k=128 (c09).
- **Llama and Mistral.** Llama-3.2-3B plateaus near 30% on Countdown while Qwen-3B reaches about 60% (b18). Priming closes the gap. Mistral-Small-24B pass@1 passes its base pass@8 by over 30 points (b25).
- **Small distilled models.** R1-Distill-1.5B under ProRL: +14.7 math, +13.9 code, +54.8 logic (a23). "Wait" extension first helps then hurts: 82.2 to 87.3 then 70.3 (d12).
- **Frontier reasoning models.** Faithfulness 25% (Claude 3.7 Sonnet) and 39% (R1). Reasoning models were 3.6x (Claude) and 1.7x (DeepSeek) more faithful than non-reasoning siblings, still a minority (d06). Post-cutoff: GPT-5 91.3 on AIME/HMMT 2025 as recorded in d08.
- **Non-reasoning models.** GPT-4o AIME 2024 9.3, 13.4 with 64 votes (b03). Models released before Sept 2024 scored under 10% on clean sets (d08).
- **Code agents.** SWE-RL 70B 41.0% SWE-bench Verified; Kimi-Dev 60.4%; R1 49.2% (c03); SWE-Gym plus verifier 32.0 (d03-d05). Gains are tangled with SFT and scaffold choices.
- **Intrinsic rewards.** TTRL lifts pass@1 above the model's own majority vote (d09). Intuitor: Qwen2.5-3B trained on MATH gains +65% relative on LiveCodeBench vs no gain for GRPO (d10; text claim, table garbled).
- **Test-time substitutes.** s1-32B AIME24 50.0 to 56.7 with budget forcing (d15). NoThinking beats Thinking at 700 tokens on AMC23, 51.3 vs 28.9 (d16). L1 holds length error to about 3% on math (d14).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, M = memory (SCHEMA.md). Status: [E] established, [S] single-source, [C] contested. We do not train, so every item is a prompt-time or code-time analogue.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Use only post-cutoff or clean items for any claim that the scaffold beats the plain model. Run a prefix-completion contamination check on our items. | G7 (evaluation discipline) | [E] | b21, c20, d08, a16 (K09) |
| A2 | Report variance: 30 or more seeds, same hardware and sampler for both arms. | G7 | [E] that noise is large; seed count from one paper | b23, a13, b24 |
| A3 | Do not trust the written chain as evidence. Gate accepts on a check that does not read the narrative. G10 already says this; adds 25% and 39% faithfulness and the obfuscation result. | G10 | [E] | b27, d06, d07 (K16) |
| A4 | Reflect only on real verifier output. Reflection without a check lowers accuracy; the verifier carries the gain. Supports G2, G5, G9; adds 95.5 oracle vs 74.7 intrinsic. | G2, G9 | [E] | d17, d16, d04 (K22) |
| A5 | Cap single-chain length; prefer several short attempts plus a code-side vote; exit early once the check passes. Supports G11; adds the 82.2/87.3/70.3 curve and the 92% first-round figure. | G11 | [E] | d12, d13, d16 (K21) |
| A6 | Never use "longer" as a quality proxy or trigger: reflection frequency is not correlated with accuracy, and length bias favours long wrong answers. | G1, G11 | [E] | a15, b15, c06 (K11) |
| A7 | Score reasoning by an independent check or step audit, not only the final answer. Outcome-only checks admit flawed chains that land right. | S4 TEST, S8 VERIFY | [E] | a02, a15, b16 (K17) |
| A8 | Keep verify, backtrack and subgoal available as operators fired by code on a signal (G1). O3 (decompose) and O5 (work backwards) already cover subgoal and backward chaining; verification is S8; backtrack is S5 to S3. The finding that these behaviours matter is established for trained models; the prompt-only form is [S] and is tested in T1. | S/O | [E] behaviours matter; [S] prompt form | b18-b20, c15, c16, d02 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Prompt-only verify, backtrack and subgoal operators vs plain CoT at equal tokens. | S/O | [S] | b18-b20, d02 (K10, K20) |
| T2 | Trigger-based firing (code-detected uncertainty or inconsistency) vs fixed schedule vs never. | G1, S6 | [S] | d02 (K20) |
| T3 | Format-only prompt baseline: how much of any scaffold gain is just output format. | Output contract | [S] | a21, d03, d01 (K12, K23, K19) |
| T4 | Low-temperature single sample and plain vote as mandatory baselines. | G7 | [S] | d01 (K19) |
| T5 | pass@k of scaffold vs plain model, k = 1 to 64: does the scaffold narrow coverage? | G12, sampling | [C] | a17, d19, d18, d20 (K06, K26) |
| T6 | Instance-specific checklist written first, then draft checked against it, vs generic checklist, on open tasks. | S1/S8, memory | [S] | d11 (K24) |
| T7 | Reflect-then-retry (reflection cites the failing output) vs plain retry. | S5 | [S] | c24 (K18) |
| T8 | Code-style reasoning (pseudo-code steps) as a prompt vs plain CoT on math. | O6 | [S] | a20, b10 (K08) |
| T9 | Verifier kind per token: unit test vs symbolic check vs rubric vs self-check. | S4, S8 | [S] | d04, d16, d11 |
| T10 | Math-to-non-math transfer of any scaffold gain. | all | [C] | c22, a07 (K15) |

## 8. Concrete tests on our bench

All arms get equal total tokens, counting setup, retries and judge calls (G7). 30 or more seeds. Report mean, SD and a paired test. Items are fresh (post-cutoff) or procedurally generated unless stated.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Math and logic items with a key; generated Countdown-style puzzles | (a) plain CoT; (b) CoT plus verify, backtrack and subgoal operators fired by code on signals; (c) same prompt length with length-matched filler | Accuracy at equal tokens | (b) beats (a) by 3+ points; (c) equals (a). If (c) ties (b), the effect is length, not behaviour. |
| T2 | Same items | Fire on signal vs fire every k tokens vs never | Accuracy; token share on checks | Signal-fired wins or ties at fewer tokens; scheduled firing loses on easy items (schema data 92% vs 75%). |
| T3 | Code and structured-output items | Loose prompt vs strict-format prompt with example vs scaffold | Accuracy under strict and lenient parsing | A format prompt closes much of the gap (SWE-RL format 12.2 to 95.6; one-shot RLVR 8.6 of 36.0 to 73.6 beyond format). |
| T4 | Math items | Scaffold vs single sample at T=0.3 vs 8-sample vote | Accuracy | Low temperature recovers a large share (49.6 to 69.0 in d01); the scaffold must clear it. |
| T5 | Items with plain pass@1 under 30% and over 70% | Scaffold vs plain at k = 1, 4, 16, 64 | pass@k curve; items lost vs gained at k=64 | Scaffold wins at small k; ties or loses at large k. Report lost vs gained (d19 method). |
| T6 | Open-ended items (analysis, plans) | No checklist; generic checklist; instance-specific checklist written before the draft, compared by code | Blinded, length-normalised score | Instance-specific beats generic by 3+ points (d11 direction). |
| T7 | Items with executable checks | Plain retry; reflect-with-quote of the failing output; reflect-without-quote | Pass rate at equal tokens | Reflect-with-quote beats plain retry; reflect-without-quote loses (d17). |
| T8 | Math items | Plain CoT vs code-style steps without execution vs with execution | Accuracy | Gain only if the model writes code well (a20: 60.9 vs 28.0). |
| T9 | Items with tests and a symbolic check | Verifier = unit tests / symbolic check / instance rubric / model self-check | Gain per 1k tokens | Executable check beats rubric beats self-check (d17, d04). |
| T10 | Math, logic, code, planning | Scaffold per domain | Gain by domain | Gain shrinks outside the tuned domain; flag negative domains. |
| T11 (hygiene) | All test items | Give 60% of each item to our model and to a clean control; compare exact completion | Completion rate | Rate above the control marks an item as contaminated; drop it (b21: 54.60% vs 3.8%). |

## 9. What does not transfer, and why

- **The training itself.** Policy gradients, clipping, KL, length normalisation, DAPO fixes: we change no weights. Background only (K03, K04, K05).
- **Long single chains as the quality lever.** RLVR models learn long chains inside the trained distribution. For a prompt-only agent, extended chains peak then fall (d12), and a parallel budget keeps gaining. G11 stands.
- **Spurious-reward gains.** They need the GRPO clip mechanism and a Qwen-like prior. Not a prompt trick; at most a hint toward code-style elicitation (T8).
- **One-shot RLVR.** Needs a gradient step.
- **Gains reported on Qwen2.5 and AIME 2024.** Contaminated; not evidence for the scaffold (K09, K25).
- **Steering with activation vectors (d02).** Needs internals. Only the idea (fire behaviours on a signal) transfers.
- **Faithfulness from RL.** RL raised faithfulness at first then plateaued at 28% MMLU and 20% GPQA (b27). We cannot count on the chain being a true record.
- **PRM and MCTS dismissal.** Evidence is qualitative and about training at scale. It does not show test-time step checks are useless.
- **Self-certainty and majority-vote rewards (Intuitor, TTRL).** They train on test questions. The scaffold analogue is a code-side vote (already G5); no weight update is possible.

## 10. Open questions

1. Does a prompt-only verify/backtrack/subgoal scaffold reproduce the RL-induced behaviours at equal tokens on post-cutoff problems? Partly closed by d01, d02, d16; the exact test is open (gap 1).
2. Does a scaffold narrow pass@k at large k like RLVR, or keep coverage? No scaffold curve found (gap 2).
3. How much of the gain is format and elicitation, split cleanly for one model? (gap 3)
4. Best prompt-time analogue of a verifiable reward per token on non-math tasks (gap 4).
5. Does RLVR transfer to tool-using agents beyond SWE tasks, with a pure agentic-RL ablation? (gap 5)
6. Is there a paired R1-Zero-style RL vs base comparison on post-cutoff problems? (gap 8)
7. What did 2026 first-appearance work show on rubric, non-verifiable and test-time RL? Coverage here is thin because search was blocked (gap 9).
8. Is ProRL's boundary expansion a base-weak effect only? d18 says gains are largest where the base is weak.
9. Which of sharpening, elicitation, contamination and expansion dominates, by model family? Not separable from current papers.
10. Do the 5-15 point seed SD figures hold at other sizes? One paper, not fully re-verified.
11. Hochlehnert seed SD, Gandhi, Kimi and SimpleRL-Zoo numbers were not re-verified in the critique pass.

## 11. Sources

[V] opened as full text in the evidence files and critique. [M] snippet only. No source here is marked [M] except where noted.

- [V] Zelikman et al. (2022) STaR. https://arxiv.org/abs/2203.14465 (a01, a02)
- [V] Shao et al. (2024) DeepSeekMath. https://arxiv.org/abs/2402.03300 (a03-a05; c25 flagged not opened but a03-a05 were)
- [V] Lambert et al. (2024) Tulu 3. https://arxiv.org/abs/2411.15124 (a06, a07, b05, c19)
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948 (a08-a11, b01-b04, c01-c04)
- [V] Kimi Team (2025) Kimi k1.5. https://arxiv.org/abs/2501.12599 (a12, c18)
- [V] Yu et al. (2025) DAPO. https://arxiv.org/abs/2503.14476 (a13, a14, b17, c14)
- [V] Liu et al. (2025) Understanding R1-Zero-Like Training (Dr. GRPO). https://arxiv.org/abs/2503.20783 (a15, a16, a25, b14-b16, c07, c08)
- [V] Yue et al. (2025) Does RL Really Incentivize Reasoning Capacity in LLMs. https://arxiv.org/abs/2504.13837 (a17, a18, b06-b08, c09, c10)
- [V] Shao et al. (2025) Spurious Rewards. https://arxiv.org/abs/2506.10947 (a19, a20, a24, b09-b11, c11, c12)
- [V] Wang et al. (2025) RL for Reasoning with One Training Example. https://arxiv.org/abs/2504.20571 (a21, a22, b12, b13, c13)
- [V] Liu et al. (2025) ProRL. https://arxiv.org/abs/2505.24864 (a23, c17, d18)
- [V] Gandhi et al. (2025) Cognitive Behaviors that Enable Self-Improving Reasoners. https://arxiv.org/abs/2503.01307 (b18-b20, c15, c16)
- [V] Wu et al. (2025) Reasoning or Memorization? https://arxiv.org/abs/2507.10532 (b21, b22, c20)
- [V] Hochlehnert et al. (2025) A Sober Look at Progress in Language Model Reasoning. https://arxiv.org/abs/2504.07086 (b23, b24)
- [V] Zeng et al. (2025) SimpleRL-Zoo. https://arxiv.org/abs/2503.18892 (b25, b26, c05, c06)
- [V] Chen et al. (2025) Reasoning Models Don't Always Say What They Think. https://arxiv.org/abs/2505.05410 (b27, b28, d06)
- [V] Wu et al. (2025/2026) The Invisible Leash. https://arxiv.org/abs/2507.14843 (c21, d19)
- [V] Huan et al. (2025) Does Math Reasoning Improve General LLM Capabilities? https://arxiv.org/abs/2507.00432 (c22)
- [V] Zhao et al. (2025) Absolute Zero. https://arxiv.org/abs/2505.03335 (c23)
- [V] Bensal et al. (2025) Reflect, Retry, Reward. https://arxiv.org/abs/2505.24726 (c24)
- [V] Karan and Du (2025) Reasoning with Sampling. https://arxiv.org/abs/2510.14901 (d01)
- [V] Venhoff et al. (2026) Base Models Know How to Reason, Thinking Models Learn When. https://arxiv.org/abs/2510.07364 (d02)
- [V] Wei et al. (2025) SWE-RL. https://arxiv.org/abs/2502.18449 (d03)
- [V] Pan et al. (2024) SWE-Gym. https://arxiv.org/abs/2412.21139 (d04)
- [V] Kimi Dev team (2025) Kimi-Dev. https://arxiv.org/abs/2509.23045 (d05)
- [V] Baker et al. (2025) Monitoring Reasoning Models for Misbehavior. https://arxiv.org/abs/2503.11926 (d07)
- [V] Balunovic et al. (2025/2026) MathArena. https://arxiv.org/abs/2505.23281 (d08)
- [V] Zuo et al. (2025) TTRL. https://arxiv.org/abs/2504.16084 (d09)
- [V] Zhao et al. (2026) Learning to Reason without External Rewards (Intuitor). https://arxiv.org/abs/2505.19590 (d10)
- [V] Gunjal et al. (2025) Rubrics as Rewards. https://arxiv.org/abs/2507.17746 (d11)
- [V] Ghosal et al. (2025) Does Thinking More Always Help? https://arxiv.org/abs/2506.04210 (d12)
- [V] Chen et al. (2024) Do NOT Think That Much for 2+3=? https://arxiv.org/abs/2412.21187 (d13)
- [V] Aggarwal and Welleck (2025) L1. https://arxiv.org/abs/2503.04697 (d14)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393 (d15)
- [V] Ma et al. (2025) Reasoning Models Can Be Effective Without Thinking. https://arxiv.org/abs/2504.09858 (d16)
- [V] Huang et al. (2024) LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (d17)
- [V] Chen et al. (2025) Pass@k Training. https://arxiv.org/abs/2508.10751 (d20)

Caveats from the critique: tables in d01, d09, d10, d14 and d20 came out garbled in text extraction, so only unambiguous numbers are cited. "Independent sources" in claims.jsonl count papers, not labs. Most gains are on Qwen2.5. The search APIs were rate-limited during the gap pass, so 2026 papers are underrepresented.
