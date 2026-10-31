# Sampling and voting (self-consistency): deep document

*Subfield C01.02. Written from evidence_a-d.jsonl (a01-a25, b01-b25, c01-c25, d01-d18), claims.jsonl (K01-K28) and critique.md in this folder. Schema parts refer to research_notes/single_agent/SCHEMA.md (guardrails G1-G12, states S0-S9). Evidence ids in brackets. Most numbers were read in the papers; the few not re-opened are flagged in section 5.6.*

## 1. What it is

Sample many reasoning paths from the same model at a temperature above zero. Pull the final answer out of each path. Count the answers. Return the most frequent one. That is self-consistency (Wang et al. 2022, arXiv 2203.11171) [a01].

Key points:
- It needs no training, no extra model, and no judge. The program counts. This is exactly "code selects" (G5) in state S7, fed by S3 GENERATE.
- It needs a short, parseable final answer ("The answer is X"). Free-form output cannot be counted by exact match. Universal self-consistency (USC) and list-wise judges are the patches for that [a13, d16].
- It marginalises out the path. Many different reasoning routes can lead to the same answer. The answer that most routes reach is taken as the best guess.
- The cost is k times the tokens of one sample. Most of the later literature is about cutting that cost (adaptive stopping), improving the count (weights, verifiers), or finding where it fails.

Where it sits in our schema: S3 makes the k samples, S4 may test each one, S7 picks. It is also the cheap reference arm that every other element must beat at equal tokens (G7). Guardrail G4 says samples from one model are not independent, so agreement is a hint, not proof. G9 says no debate. G11 says several short attempts beat one long one. G12 says spend by difficulty. This subfield gives the numbers behind G4, G5, G9 and G12, and shows that the G11 claim ("short attempts beat one long one") is not directly tested at equal tokens on current models (section 7).

## 2. History and theories in depth

### 2.1 Theory before LLMs: the Condorcet jury theorem
Condorcet (1785) showed that if each voter is right with probability above 0.5 and voters are independent, the majority is right with a probability that rises toward 1 as voters are added. If each voter is below 0.5, the majority gets worse as voters are added [a18, snippet only]. Two conditions matter for LLMs: per-sample accuracy on the item must exceed the chance of any single wrong answer, and errors must not be shared. Both are item-level conditions, not task-level ones. A model at 70% on a task may be at 90% on some items and 20% on others. Voting lifts the first group toward 100% and drives the second toward 0%. Chen et al. 2024 saw exactly this split: 53% of easy queries improved, 47% of hard ones degraded [a17, c09].

Plurality voting is weaker than the theorem assumes in one way and stronger in another. With many wrong answers spread thinly, the correct answer only needs to be the biggest bucket, not above 50%. Wang et al.'s budget-aware comparison notes SC works best when the chance of a correct sample is above 50% [d04]. Wu et al. prove that majority and weighted-majority accuracy converge to a fixed limit set by the model's own answer distribution, at an exponential rate [b12]. More samples cannot beat that ceiling.

### 2.2 The path to self-consistency (2021-2022)
- Cobbe et al. 2021 (GSM8K) [a08, c05]. Train a verifier, sample 100 solutions at T=0.7, rank by verifier. The verifier beat plain finetuning once data was large. Voting among the top 3-5 verifier-ranked answers added a bit (top 30 at 3200 samples). Verifier accuracy rose to about 400 samples, then fell as adversarial solutions fooled it. Finetuning for more epochs raised test@1 but cut diversity: test@100 peaked in the first few epochs [a22]. Lesson: a selector needs diverse samples.
- Wei et al. 2022 (chain of thought) [a07]. Eight CoT examples lifted PaLM-540B to 56.5% on GSM8K (greedy), above finetuned GPT-3 with a verifier. It is emergent at about 100B parameters and up. Gains were negligible on one-step problems. This is the greedy baseline that self-consistency was measured against.
- Wang et al. 2022 [a01-a06, a21, a23, a24]. The main step: replace greedy decoding with sample-and-vote. Reported on four models (UL2-20B, LaMDA-137B, PaLM-540B, GPT-3 code-davinci-002) and arithmetic, commonsense and symbolic sets. Published at ICLR 2023.

### 2.3 Extensions (2022-2024)
- DiVeRSe (Li et al.) [a09, a10]: diverse prompts, a trained step-aware verifier, and verifier-weighted votes. GSM8K 82.3 vs 76.7 for plain SC on code-davinci-002.
- Complexity-based prompting (Fu et al.) [a11, a19, b15]: vote only over the chains with the most steps. A small gain (+0.3 to +1.1) on top of complex prompts.
- Adaptive-Consistency and ESC (Aggarwal; Li) [a12, a20, b17, b18, c11, c12]: stop sampling when the lead is safe.
- Universal self-consistency (Chen et al. 2023) [a13, b14, c10, c22, c25]: the model reads all samples and picks the most consistent one. Allows free-form output and code.
- Scaling studies: More Agents (Li et al.) [b07, b08, c08, c23], Large Language Monkeys (Brown et al.) [a14, a15, a25, b09, b10, c06, c07], Chen et al. "Are more LM calls all you need" [a17, c09], Snell et al. [a16, b11, b25, c17], Wu et al. Inference Scaling Laws [b12, c18].
- Confidence-aware voting: Soft-SC [b19, c14], CISC [b20, c13], CoT-decoding [c15].
- Debate comparisons (Smit et al.; Wang et al. budget-aware) [c20, d04]: debate does not reliably beat plain SC at matched compute.

### 2.4 The reasoning-model era (2025-2026)
- DeepSeek-R1 and distils [b21, c16, c24]: voting still helps long-reasoning models. Small distils gain 10-28 points at cons@64.
- Verifiers and PRMs re-enter: Lightman [b16], Heimdall [d13], RL^V [d14], Zhao et al. "Sample, Scrutinize and Scale" [b13].
- Cheap confidence: DeepConf [d12], CGES [d11], self-certainty [d15], binary agreement [d07], conformal aggregation [d06].
- Test-time RL (TTRL) uses majority labels as reward [b23]. Outside our scaffold-only scope.
- Equal-budget tests: Sequential Edge [d01], Sample More, Reflect Less [d02], Increasing the Thinking Budget [d03].
- Independence audits: Correlated Errors [b24], Artificial Hivemind [c21], AIMO 3 lessons [d09], shared-seed structure [d10], agreement audit [d05].

### 2.5 Competing explanations for why voting works
1. Marginalisation. The vote approximates the answer with the highest total probability over paths. The unnormalised sum of path probabilities did worse (59.9 vs 74.4), so the count works better than the model's own likelihood [a04, b03, c03].
2. Mode-seeking. Voting rewards the answer the model produces most often. That is right when the mode is right and wrong when it is not. In open-ended output, it rewards homogeneity [c21].
3. Plain extra compute. Much of the "gain" of debate and other multi-sample methods is extra sampling [c20, d04, d02].
4. Coverage plus selection. The ceiling is coverage (pass@k). Voting captures part of it. A verifier captures more [a14, d09].

## 3. Core findings with exact numbers

Status: established = confirmed by 2+ independent sources or a design that leaves little doubt; single-source = one paper; contested = sources disagree. Statuses follow claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Vote beats greedy CoT on arithmetic, all four models | PaLM-540B GSM8K 56.5 -> 74.4 (+17.9); AQuA 35.8 -> 48.3; SVAMP 79.0 -> 86.6; MultiArith 94.7 -> 99.3. code-davinci-002 GSM8K 60.1 -> 78.0, AQuA 39.8 -> 52.0. LaMDA-137B MultiArith 51.8 -> 75.7. 40 paths, mean of 10 runs | Wang 2022 [a02, b01, c01] | established (K01) |
| More Agents: gain on GSM8K across models | +12 to +24 points; relative gain 28-200% for Llama2-13B vs 8-16% for GPT-3.5 | Li 2024 [b07, c08] | established (K01); size effect single-source (K14) |
| R1 distills at cons@64 on AIME | 1.5B 28.9 -> 52.7; 7B 55.5 -> 83.3; 14B 69.7 -> 80.0; 32B 72.6 -> 83.3; Llama-8B 50.4 -> 80.0; R1 79.8 -> 86.7; GPT-4o 9.3 -> 13.4; Claude-3.5 16.0 -> 26.7 | DeepSeek-AI 2025 [b21, c16, c24] | established (K01, K12) |
| Gain is near zero when the model cannot solve the task, or is at ceiling | UL2-20B Letter 0.0 -> 0.0; UL2 GSM8K 4.1 -> 7.3 (+3.2); LaMDA GSM8K 17.1 -> 27.7 (+10.6); PaLM AddSub 91.9 -> 93.7 (+1.8); PaLM Letter 65.8 -> 70.8 | Wang 2022 [a02, a03, a23, c02] | established (K02) |
| Sampling beats beam search, likelihood ranking, prompt ensembles | UL2 AQuA: beam 23.6 -> 10.2 at 40 beams; sample-vote 19.7 -> 26.9. LaMDA GSM8K: CoT 17.1, 3-prompt ensemble 18.6, 40 permutations 19.2, SC 27.7. PaLM GSM8K: 40 prompt sets 58.9, SC 74.4, SC + prompt sets 75.4 | Wang 2022 [a05, b05] | established (one paper; consistent with later ones) |
| Counting beats likelihood weighting | unnormalised weighted sum 59.9 vs plain vote 74.4 (PaLM GSM8K) | Wang 2022 [a04, b03, c03] | single-source (K05); later work shows better weights can help |
| Most of the gain comes early on easy and mid items | Wang advice 5-10 samples; USC saturates about 5-8; no gain past 5 on SummScreen | [a21, c25] | contested (K03) |
| On hard reasoning-model items gains continue to hundreds of samples | GPT-OSS-120B AIME25 pass@1 91.8 -> cons@512 97.0; DeepSeek-8B HMMT25 58.1 -> 69.6 at 512; about 80 samples for Bo-infinity accuracy | DeepConf, Bo-infinity [d12, d08] | contested (K03) |
| Adaptive stopping cuts samples with tiny accuracy loss | up to 7.9x fewer (average drop under 0.1%); math 3.3x, commonsense 2.9x, symbolic 3.8x, code 2.4x; ESC 33.8-84.2% fewer; CGES 58% fewer calls; DeepConf up to 84.7% fewer tokens. Hard sets save less: ESC at budget 16 uses 12.88 calls on GPQA, 10.68 on AIME24, 5.16 on GSM8K | Aggarwal 2023; Li 2024; Aghazadeh 2026 [a12, b17, b18, d11] | established (K04) |
| Confidence-aware weights help in most author tests | CISC cuts needed samples over 40%; Soft-SC +4.2% avg; DeepConf top-10% filter lifts DeepSeek-8B HMMT25 69.6 -> 79.5-83.9. Exceptions: GPT-OSS-120B HMMT25 fell 92.9 -> 90.5/88.9; self-certainty 75.83 vs 76.25 (random level) in an independent Bo5 test | [b19, b20, d12, d08] | established as "helps in most"; reverses on over-confident models (K06) |
| Coverage keeps rising, vote plateaus | Llama-3-8B MATH: coverage 82.9 -> 98.44% (100 -> 10,000 samples); vote/reward 40.50 -> 41.41%. SWE-bench Lite with a test check: 15.9 -> 56% at 250 samples (prior SOTA 43%) | Brown 2024 [a14, a15, b09, c06, c07] | established (K07) |
| Vote hardens wrong answers on hard items | MMLU-Physics: 53% easy queries improve, 47% hard degrade; example wrong answer 56% vs correct 34% | Chen 2024 [a17, c09] | established (K08) |
| Trained verifiers beat vote at larger N | PRM best-of-1860 78.2 vs ORM 72.4 vs majority 69.6 (MATH); Heimdall AIME2025 majority about 70.0 -> 83.3; RL^V weighted vote above majority at N>=8; compute-optimal allocation about 4x better than best-of-N | Lightman; Heimdall; RL^V; Snell [b16, d13, d14, a16] | contested (K11) |
| Off-the-shelf judges lose to vote at N=5 | AIME-2025, GPT-OSS-20B: majority 85.42 vs LLM judges 81.25-82.92, reward models about 79.8-80.0, self-certainty 75.83 | Komiyama 2026 [d08] | contested (K11, K24) |
| Free-form selection by the model | USC GSM8K 90.2 vs 90.4 SC (PaLM 2-L); ARCADE (gpt-3.5): greedy 26.0, random 26.8, SC-Exec strict 29.8, fuzzy 30.3, USC 30.1; BIRD-SQL: greedy 42.4, SC-Exec 45.6, USC 45.5 | Chen 2023 [a13, b14, c10, c22] | single-source (K13). Use c22 for code numbers (critique fix) |
| On agent tasks counting is weak | GAIA 165 tasks, GPT-4.1, best-of-4: baseline 55.76, voting 56.8, scoring 59.39, list-wise 63.03; naive reflection 55.15 | OPPO 2025 [d16] | single-source (K28) |
| Vote share rises with accuracy but is a fragile signal | TT-SC AUROC 0.836, ECE 0.090 (36 model-dataset combos); conformal threshold from 200 items: 90.1% vs 82% selective accuracy on GSM8K at under 5% abstention; Spearman only 0.20-0.59; gpt-4.1 GPQA: C>=0.8 on 77% of entries, 48% of those wrong | [a06, c04, d05, d06, d07] | established as usable but fragile (K16, K23) |
| Small-model ensemble beats a bigger single model | Llama2-13B ensemble 59% vs Llama2-70B 54% GSM8K; DeepSeek 5 samples beat single GPT-4o or Claude-3.5 on SWE-bench Lite at over 3x lower cost (needs a check) | Li 2024; Brown 2024 [c23, b10] | single-source (K14) |
| Fancier self-inspection loses to repeated sampling at equal tokens, small models | 36 paired comparisons, Qwen2.5 1.5B/3B/7B: 10 reliably worse, none better; best-of-8 pick loses by 8.0 and 11.3 pts at 1.5B, 1.3-2.0 at 7B (not different from 0) | Mirzaei 2026 [d02, d04] | established (K21), small models only |
| Parallel vs sequential at equal tokens | Qwen3-235B AIME-2025 6 chains: sequential 76.7 vs parallel 30.0; 43 of 45 settings favour sequential at 4096-token chains. Snell: revision turned about 38% of correct answers wrong | Sharma 2025; Snell [d01, b25] | contested (K19) |
| Prompt diversity | DiVeRSe 5 prompts x 20 samples 80.0 vs 76.7 (1 prompt x 100); LaMDA 40 permutations 19.2 vs 40 samples 27.7; gpt-oss-120b 50 problems: baseline 39.3, every prompt mix equal or worse | [a09, a05, d09] | contested (K10) |
| Test-time RL from vote labels | Qwen2.5-Math-7B AIME24 12.9 -> 40.2 | Zuo 2025 [b23] | single-source (K20), out of scope |

## 4. Mechanisms and models

Written so that an engineer can build each piece.

### 4.1 Basic sample-and-vote
1. Prompt for a short chain of thought that ends with a fixed line, for example "Final answer: <value>".
2. Call the model k times with temperature near 0.7 to 1.0 (Wang used 0.5 for UL2/LaMDA, 0.7 for PaLM and GPT-3, with top-k 40). Each call gets its own seed. Do not share a seed or a few-shot block across passes in a way that locks them together [d10].
3. Parse the final answer with code. Normalise: strip units, canonicalise numbers and fractions, lowercase strings, sort sets. Bad normalisation splits true agreement into separate buckets and under-counts the mode.
4. Count with a dictionary. Return the key with the highest count. Ties: break by the earliest, or by higher mean confidence, or escalate (see 4.5).
5. Log the vote share (top count / valid samples) and the full count table. These are the signals for stop, trust and escalate.

For multiple choice, shuffle the option order per sample and map back to content before counting. A small model can answer "A" 81% of the time in the original order, which looks like agreement and is not [d10].

### 4.2 Why temperature and not beam search
Beam search is an optimiser and drifts to one mode, so beams repeat each other. UL2 AQuA fell from 23.6 to 10.2 as beams went from 1 to 40, while sampling rose from 19.7 to 26.9 [a05]. The vote needs diverse paths that reach the answer by different routes.

### 4.3 Sequential stopping (Adaptive-Consistency, ESC, CGES, DeepConf online)
Draw samples one at a time (or in small windows). After each draw, ask: is the leader safe?
- Beta rule (Adaptive-Consistency): treat the top answer's share as a rate with a Beta posterior; stop when the probability that the top answer leads the second exceeds a threshold, for example 0.95 [a12, a20].
- Window rule (ESC): sample in windows of size w; stop when a whole window agrees [b18].
- Confidence-guided (CGES): use the model's own token confidence in the stop rule; saves 58% of calls, but on GPQA it loses about 2 pp where the signal is uninformative [d11].
- Online filtering (DeepConf): drop low-confidence traces early and stop when the weighted vote is decided; up to 84.7% fewer tokens [d12].
Always set a maximum k. On hard items savings are small (ESC 12.88 calls of 16 on GPQA). That is correct behaviour: those are the items where the agreement signal is weak.

### 4.4 Weighted voting
- Confidence-weighted (CISC): ask the model for a confidence per path, normalise within the question, weight votes by it. Cuts needed samples by over 40% [b20, c13]. Use within-question ranking, not absolute values.
- Soft-SC: score an answer by the mean probability mass rather than a hard count; works on agent trajectories where answers do not match exactly (+4.2% average) [b19, c14].
- Trace confidence (DeepConf): weight or filter by token-level group confidence; keep the top 10%. Fails when wrong traces are over-confident (GPT-OSS-120B HMMT25 92.9 -> 90.5) [d12].
- Verifier weights (DiVeRSe, RL^V): sum of verifier scores per answer. Needs a trained verifier [a09, d14].
- Inverse-entropy weights (Sequential Edge): weights from the entropy of the chain; beat plain majority in both modes [d01].
Rule from the evidence: weighting helps most with varied confidence signals, and can reverse with over-confident models. Always compare with the plain vote at equal samples.

### 4.5 Escalate on low agreement
A plurality of wrong answers is the main failure (K08), and vote share is an imperfect trust signal (K23). A safe design:
1. Draw k samples (adaptive).
2. If top share is at or above a calibrated threshold, release the plurality.
3. If below, do not draw more of the same. Send the top 2-3 distinct answers to a check (a runnable test, a step-level verifier, or an independent re-derivation). Heimdall's selection falls back to the vote when verification counts are small [d13].
4. If there is no check, escalate to other states (S4/S5 search, S6 control).
The threshold is fit by binning accuracy against vote share on about 200 labelled items per model and task [d06]. Do not reuse one number across tasks.

### 4.6 Selecting from free-form samples
- Exact-match fields: vote by code.
- Code: run each sample on tests, group by output, vote over output groups (SC-Exec); on ARCADE this gave 29.8-30.3 vs USC 30.1 [c22].
- Free-form text: USC. Put k samples (about 8) in one prompt, ask for the most consistent one. Shuffle the order. It is limited by context length and order/length bias; GSM8K fell at 16 samples [c25].
- Agents: a list-wise judge that sees all candidates gave 63.03 vs vote 56.8 on GAIA [d16].

### 4.7 The formal ceiling
Majority accuracy converges at an exponential rate to a limit set by the model's answer distribution [b12]. If the correct answer is not the mode of that distribution for an item, no sample count fixes it. The only ways out are a different generator distribution (other model, prompt or tool), a selector with outside information (a test or verifier), or a search that changes the distribution (S4/S5).

## 5. What holds up

### 5.1 Replications and consistent results
- The core gain (vote > greedy CoT) shows up in Wang's own 4 models, in More Agents across Llama2, GPT-3.5 and GPT-4 [b07], in the R1 distills [c24], and in GPT-OSS and Qwen3 models up to 2026 [d11, d12]. Four independent sources. [E]
- Gain tracks headroom in the middle of the accuracy range. Near-zero cases and ceiling cases are both seen [a23, c02]. [E]
- Coverage vs selection: Brown, Cobbe, Zhao and Heimdall all show the gap between pass@k and a count-based selector, and show that it closes only with an outside check [a14, a08, b13, d13]. [E]
- Adaptive stopping works in four separate papers [a12, b18, d11, d12]. [E]
- Debate and other multi-agent schemes do not beat plain SC at matched compute: Smit, Wang budget-aware, Mirzaei, More Agents [c20, d04, d02, b07]. [E for 2023-24 and small models]

### 5.2 Failures and boundary conditions
- Model cannot do the task: UL2 Letter 0.0 -> 0.0 [a23]. Ceiling: AddSub +1.8 [c01].
- Wrong plurality: hard items degrade with more samples [a17]. Gemini 1.5 Pro on AIME Problem 11: the correct answer appeared in 1 of 200 samples; the vote picked another, more common answer [b13].
- Vote plateaus near 41% on Llama-3-8B MATH while coverage reaches 98% [a14].
- Incomplete tests turn resampling into false-positive acceptance: best attempts under 10 on HumanEval/MBPP [c19].
- Shared errors across and within models: wrong answers agree about 60% vs 1/3 by chance across 349 and 71 models [b24]; open-ended same-prompt responses have similarity above 0.8 [c21].
- Fake agreement from shared seeds, shared few-shot blocks and option-letter bias [d10].
- Over-confident frontier models: gpt-4.1 had 48% wrong among entries with consistency >= 0.8 on GPQA [d05]. Gemini 1.5 Pro consistency@200 was 4 of 15 on AIME vs verification@200 of 8 [b13].
- USC: GSM8K fell at 16 samples because of context length [c25]. Order and length bias.
- Complexity-based voting adds only +0.3 to +1.1 [a11].
- Naive revision is harmful: about 38% of correct answers turned wrong [b25]. Naive reflection scored 55.15 vs baseline 55.76 on GAIA [d16].

### 5.3 Moderators
- Model size: gain grows with scale to a point (UL2 +3, LaMDA +10 to +24, PaLM +18) [a02]. In relative terms weaker models gain more (Llama2-13B 28-200%) [b08].
- Difficulty: relative gains larger on MATH (34-200%) than GSM8K (16-69%) [b08]; but on a hard item with no foothold, voting is worse than useless [a17].
- Task type: smaller gain on GPQA than on math (cons@512 vs pass@1 +9.7 DeepSeek-8B, +3.3 Qwen3-32B, vs +11.5 on HMMT25) [d18].
- Model type: reasoning models gain from voting but need more samples on hard items (to 512) [d12].
- Prompt quality: voting repairs weak prompts (LaMDA 14.9 -> 23.4; zero-shot CoT PaLM 43.0 -> 69.2) [a24, c04].
- Answer format: needs extractable answers. Multiple choice needs shuffling.
- Check availability: with an automatic check the budget scales to hundreds of samples (SWE-bench Lite 15.9 -> 56% at 250) [a14].

### 5.4 Interventions that worked
Temperature sampling (vs beam); adaptive stopping; confidence-weighted votes (most authors' tests); a verifier on the top few answers at large N; separate seeds and shuffled option order; sequential refinement in some long-chain settings [d01]; execution-based grouping for code; a list-wise judge for agents [d16].

### 5.5 Interventions that did not work, or are unproven
Prompt-diversity mixes on top of T=1.0 (equal or worse in AIMO 3) [d09]; persona or strategy voters (G4); debate [c20]; reflect/critique/self-refine at equal tokens on small models [d02]; likelihood-weighted vote (K05); self-certainty in one independent test [d08]; unshuffled model-ranks-own-samples [c25]; extremizing.

### 5.6 Items not re-opened this session (still from the evidence files)
Adaptive-Consistency per-model figures (GPT-3.5 4.4x, Vicuna 1.9x) and per-task ratios (the 7.9x and under-0.1% headline was confirmed); Soft-SC, CISC, ESC, TTRL, Correlated Errors, Hivemind, Inference Scaling fLaws, MAD numbers; Snell's 38% revision figure. Treat these as leads. Also, the critique found that b14 and a13 mislabel USC code numbers (BIRD-SQL figures given as ARCADE); this document uses c22.

## 6. Language models

| Era / model class | Behaviour under voting | Change vs greedy |
|---|---|---|
| 2021-22 base LMs (UL2-20B, LaMDA-137B) | Small gain below about 100B; LaMDA +10 to +24 | UL2 +3 to +6 on arithmetic |
| 2022 PaLM-540B, code-davinci-002 | Large gain on GSM8K, AQuA, SVAMP | +12 to +18 pts on hard sets |
| 2023-24 chat models (GPT-3.5, GPT-4, Llama2) | Relative gain larger for weaker models; small-model ensemble beats a bigger single model | Llama2-13B ensemble 59 vs 70B 54 (GSM8K) |
| 2024 Llama-3-8B coverage study | Coverage near 98% but vote stuck near 41% | gap closes only with a verifier |
| 2025 R1 distills (1.5B-32B) | Strong gain at cons@64 on AIME | +10 to +28 pts (1.5B 28.9 -> 52.7) |
| Frontier chat models | Smaller gain, and more over-confident | GPT-4o +4.1, Claude-3.5 +10.7 on AIME; gpt-4.1 GPQA 48% wrong at C>=0.8 |
| 2025-26 open reasoning (GPT-OSS-120B, Qwen3) | Gain continues to hundreds of samples on hard items; confidence filters help or hurt by model | AIME25 91.8 -> 97.0 at 512 |

Points to carry:
- Models that reason at length (R1, o1 style) change the equation. One long pass already contains self-checking; the vote adds on top but at k times the long-pass cost. No study measures this at equal total tokens (K22). The nearest are Sharma [d01] (cap-limited), Mirzaei [d02] (small models) and Iacobacci [d03] (30 items).
- Agreement and accuracy are linked differently per model. A more consistent model is not necessarily more accurate (gpt-4.1 C=0.89 vs mini 0.82, no accuracy gain) [d05].
- Selection loss is large: gpt-oss-120b best vote 42/50 vs pass@20 45.5 [d09].
- Most 2025-26 reasoning-model results rest on 30-problem AIME sets, where one item is 3.3 points. Treat single numbers as leads.
- No clean evidence on law, biology or causal tasks. Medical thinking-budget gains saturate near 4K tokens and voting was not tested [d17].

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Evidence ids in brackets. Schema part: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Closed-answer items: sample k short CoT paths and vote in code (S3 + S7, G5, G11).** [E] [a02, b01, b07, c16, c24] (K01). Use a small default k; the stop rule below sets the real k.
2. **Count in code. Never ask a model which answer is most common when answers can be matched (G5).** [E] [a04, b03] (K05); USC only for free-form [S] [a13] (K13). Normalise answers before counting.
3. **Use temperature sampling with a separate seed per sample, not beam search (S3).** [E] for beam loss [a05]; seed independence [S] [d10] (K25).
4. **Skip voting when the item is unsolvable or near-certain by one sample (S0 gate, G12).** [E] [a23, c02] (K02). Gate by single-sample pass rate.
5. **Adaptive stopping with a cap (S3, G7, G12).** [E] [a12, b18, d11, d12] (K04). Window or Beta rule. Expect 2-5x fewer samples on easy items and little saving on hard ones.
6. **Treat vote share as a hint, never proof (G4).** [E] [a17, d05, d06, d07] (K16, K23). Record share; calibrate per task; escalate below the threshold.
7. **Where a runnable check exists, select by the check, not the vote (S4 + S7).** [E] [a14, a15, a22, c06] (K07). Vote is the fallback when no check exists.
8. **When top share is low, send the top 2-3 distinct answers to a check or to search instead of drawing more samples (S7 -> S4/S5).** [E] [a17, c09, b13, d13] (K08, K26). More of the same hardens a wrong plurality.
9. **No debate, no persona voters, no extremizing (G4, G9).** [E] [c20, d04, d02, b24] (K17 is contested for tuned debate; the default stays no).
10. **Do not add self-refine, reflexion or model-picks-best at equal tokens on small models without a paired win over vote-of-k (G7).** [E for small models] [d02, d04] (K21).
11. **Keep a vote record (memory):** count table, share, k used, tokens. Needed for calibration and for a failed-vote detector.
12. **A weak check caps the gain from more samples (S4).** [S] [c19] (K18). Measure the check's false-accept rate before scaling samples.

### Test first

| Item | Schema part | Status | Evidence | Note |
|---|---|---|---|---|
| k short samples + vote vs one long thinking pass at equal tokens | S3/S7, G11 | [C]/[S] | d01, d02, d03, b22 (K19, K22) | G11 relies on this; not directly tested |
| Confidence-weighted vote (CISC style) | S7 | [C] | b19, b20, d12, d08 (K06) | Helps in author tests; reverses on over-confident models |
| Calibrated share threshold that routes to escalation | S7, G1 | [E] direction, threshold untested | d05-d07 (K16, K23) | Fit per task on about 200 items |
| Wrong-plurality detector (share, entropy, singleton count) | S7 | [S] | d05, d06, d10 (K23) | Fails when the wrong answer is a confident mode |
| Escalation vs bigger vote on hard items | S7, S4/S5 | [E] problem, [S] fix | a17, d13 (K08, K26) | |
| Prompt, persona or rewrite diversity | S3 | [C] | a09, d09, a05 (K10, K25) | G4 already bans persona voters on single-answer problems |
| USC or list-wise judge on free-form items | S7 | [S] | a13, d16 (K13, K24, K28) | Only where answers cannot be matched |
| Verifier or judge on top-N answers vs plain vote | S7 | [C] | b16, d08, d13, d14 (K11) | Off-the-shelf judges lost at N=5; trained verifiers won at larger N |
| Small-model many-sample vs large-model single | S3 | [S] | b10, c23 (K14) | Needs a check to pick |
| Sequential refinement vs parallel vote by difficulty | S3/S8 | [C] | d01, d02, b25 (K19) | |
| Samples-needed curve per difficulty bin | S3, G12 | [C] | d08, d11, d12 (K03) | Fixes the default k |
| Non-math held-out generalisation | S3 | [S] | d11, d17, d18 (K27) | |

## 8. Concrete tests on our bench

All arms get the same total token budget (prompt + all samples + selector calls). Report tokens per arm. Use at least 100 items per set. Use paired comparisons with 95% CI.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Closed-answer items (math, logic puzzles, multiple choice) | A: one long thinking pass. B: k=5 short samples + mode. C: k=10 short samples + mode | Accuracy | B/C beat A on mid-difficulty items by a few points; may lose on hard items |
| T2 | Same items | k=5 samples; log vote share; bin accuracy by share | Accuracy per bin; precision of the above-threshold subset | Monotone rise; a threshold with 95% precision on at least half the items |
| T3 | Same items | Fixed k=10 vs Beta 0.95 vs window w=5 | Tokens and accuracy | Over 30% tokens saved, accuracy within 0.5 pt |
| T4 | Wrong-plurality cases from T1 | Share, entropy, singleton count as predictors | AUC; recall at 20% false alarms | AUC near 0.75 |
| T5 | Hard bin (single-sample pass rate under 40%) | k=5 then S4/S5 on low share vs k=20 vote | Accuracy | Escalation wins by 3 or more points |
| T6 | Items with a runnable check | Vote vs select-by-check at same k | Accuracy | Check wins where tests are complete |
| T7 | Same items, confidence available | Plain vote vs CISC-style weighted at k=3, 5, 8 | Accuracy | Small gain at low k; may reverse on over-confident cases |
| T8 | Items with step-checkable structure | Vote vs verifier on top-3 distinct answers | Accuracy | Verifier wins at larger N, ties at N=5 |
| T9 | Free-form items | Plain vote on matchable fields vs USC (order shuffled 5 times) vs list-wise judge | Accuracy; selector stability | List-wise judge wins on open tasks |
| T10 | Same items | Same-prompt T=1.0 vs prompt-rewrite mix at equal k | Accuracy; pairwise agreement on wrong items | No gain; keep same-prompt |
| T11 | Multiple choice | Fixed option order vs shuffled per sample | Accuracy; agreement on wrong items | Shuffled has less fake agreement |
| T12 | All items by difficulty bin | Vote vs one-pass-plus-revise vs repeated sampling | Accuracy by bin | Vote wins on small models; mixed on large |
| T13 | Held-out non-math set (at least 100 items) | Greedy vs vote at k=5 | Gain in points | Smaller than the math gain |

## 9. What does not transfer, and why

- Numbers from 2021-22 base models (PaLM, LaMDA, code-davinci-002). Those models are retired. A gain of +18 points reflects 56% single-sample accuracy on GSM8K, which modern models have passed. Expect smaller gains where one sample is near ceiling.
- The AIME gains of R1 distills. 30 items, so one item is 3.3 points. The same sets serve R1, TTRL, DeepConf, Heimdall and RL^V.
- Large k (64 to 512). Fine for a benchmark paper, not for a scaffold that must pay for itself (G7). The knee depends on difficulty.
- Trained verifiers, PRMs, RL^V, TTRL. They need training; we only build the scaffold. They show a ceiling, not a design.
- Condorcet independence. Same-model samples are not independent in open-ended output (similarity above 0.8) [c21]. For short-answer math at T=1.0 the measured within-question correlation was already at or below zero [d09], but that estimate cannot see items whose per-sample chance is below 50%. Between-model correlation [b24] only supports the direction.
- Exact-match math results do not carry over to free-form, planning or agent tasks. Voting rewards the mode there.
- Test-based selection (SWE-bench 15.9 -> 56%) needs a complete test suite. With incomplete tests, false positives cap the gain [c19].
- Fine-tuned model behaviour (Cobbe's diversity loss with epochs) [a22]: prompted models behave differently.
- Debate comparisons were on 2023-24 models; they say nothing about reasoning models.
- Small-model results (Mirzaei, 1.5B-7B) may not hold for frontier long-thinking models.

## 10. Open questions

1. At equal total tokens, do k short CoT samples with a vote beat one long thinking pass on current frontier models? Nothing clean found (K22).
2. Is there a vote-share threshold that transfers across tasks? Current evidence says no; fit per model and task (K23).
3. Which code-side selector is best when there is no runnable check: plain vote, confidence-weighted, USC or a separate verifier call (K24)?
4. How correlated are errors in the failure region (items with chance under 50%), and which lever (temperature, persona, rewrite, other model) lowers it? Existing estimates are conditional on each item's hit rate [d09, d10].
5. How many samples are enough on hard items under adaptive stopping? Savings are smallest there.
6. Does voting help on open or multi-step tasks (planning, agents, open writing) beyond GAIA and Soft-SC? Hivemind suggests it rewards the mode [c21].
7. After a strong verifier exists, what does voting add? Trained verifiers beat it at larger N; off-the-shelf ones lose at N=5.
8. Do 2024-25 gains replicate on non-math reasoning (law, biology, causal tasks) on held-out sets beyond 30-item AIME?
9. Can a detector catch a unanimous but wrong vote? Share and entropy cannot.
10. Does the sequential-vs-parallel result of Sharma [d01] survive without the 4096-token cap and with truncation reported?
11. Are self-certainty and DeepConf-type filters safe on over-confident frontier models, or must they be gated per model?

## 11. Sources

[V] = opened and read this session (full paper or the relevant sections). [M] = snippet only.

- [V] Wang et al. 2022, Self-consistency improves chain of thought reasoning. https://arxiv.org/abs/2203.11171 [a01-a06, a21, a23, a24, b01-b06, c01-c04]
- [V] Wei et al. 2022, Chain-of-thought prompting. https://arxiv.org/abs/2201.11903 [a07]
- [V] Cobbe et al. 2021, Training verifiers to solve math word problems. https://arxiv.org/abs/2110.14168 [a08, a22, c05]
- [V] Li et al. 2022, DiVeRSe. https://arxiv.org/abs/2206.02336 [a09, a10]
- [V] Fu et al. 2022, Complexity-based prompting. https://arxiv.org/abs/2210.00720 [a11, a19, b15]
- [V] Aggarwal et al. 2023, Adaptive-Consistency. https://arxiv.org/abs/2305.11860 [a12, a20, b17, c11]
- [V] Chen et al. 2023, Universal self-consistency. https://arxiv.org/abs/2311.17311 [a13, b14, c10, c22, c25]
- [V] Brown et al. 2024, Large language monkeys. https://arxiv.org/abs/2407.21787 [a14, a15, a25, b09, b10, c06, c07]
- [V] Snell et al. 2024, Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314 [a16, b11, b25, c17]
- [V] Chen et al. 2024, Are more LLM calls all you need? https://arxiv.org/abs/2403.02419 [a17, c09]
- [M] Condorcet jury theorem (1785). https://en.wikipedia.org/wiki/Condorcet%27s_jury_theorem [a18]
- [V] Li et al. 2024, More agents is all you need. https://arxiv.org/abs/2402.05120 [b07, b08, c08, c23]
- [V] Wu et al. 2024, Inference scaling laws. https://arxiv.org/abs/2408.00724 [b12, c18]
- [V] Zhao et al. 2025, Sample, scrutinize and scale. https://arxiv.org/abs/2502.01839 [b13]
- [V] Lightman et al. 2023, Let's verify step by step. https://arxiv.org/abs/2305.20050 [b16]
- [V] Li et al. 2024, Early-stopping self-consistency. https://arxiv.org/abs/2401.10480 [b18, c12]
- [V] Wang et al. 2024, Soft self-consistency. https://arxiv.org/abs/2402.13212 [b19, c14]
- [V] Taubenfeld et al. 2025, Confidence improves self-consistency. https://arxiv.org/abs/2502.06233 [b20, c13]
- [V] DeepSeek-AI 2025, DeepSeek-R1. https://arxiv.org/abs/2501.12948 [b21, c16, c24]
- [V] Muennighoff et al. 2025, s1. https://arxiv.org/abs/2501.19393 [b22]
- [V] Zuo et al. 2025, TTRL. https://arxiv.org/abs/2504.16084 [b23]
- [V] Kim et al. 2025, Correlated errors in LLMs. https://arxiv.org/abs/2506.07962 [b24]
- [V] Wang and Zhou 2024, CoT-decoding. https://arxiv.org/abs/2402.10200 [c15]
- [V] Stroebl et al. 2024, Inference scaling fLaws. https://arxiv.org/abs/2411.17501 [c19]
- [V] Smit et al. 2024, Should we be going MAD? https://arxiv.org/abs/2311.17371 [c20]
- [V] Jiang et al. 2025, Artificial Hivemind. https://arxiv.org/abs/2510.22954 [c21]
- [V] Sharma and Chopra 2025, The Sequential Edge. https://arxiv.org/abs/2511.02309 [d01]
- [V] Mirzaei 2026, Sample more, reflect less. https://arxiv.org/abs/2607.28576 [d02]
- [V] Iacobacci et al. 2025, Increasing the thinking budget is not all you need. https://arxiv.org/abs/2512.19585 [d03]
- [V] Wang et al. 2024, Reasoning in token economies. https://arxiv.org/abs/2406.06461 [d04]
- [V] Ding 2026, When LLMs agree, are they right? https://arxiv.org/abs/2607.08065 [d05]
- [V] Gu et al. 2026, Pause and Reflect (conformal aggregation). https://arxiv.org/abs/2605.14098 [d06]
- [V] Zollo et al. 2026, Binary agreement for unsupervised confidence calibration. https://arxiv.org/abs/2604.19444 [d07]
- [V] Komiyama et al. 2026, Best-of-infinity. https://arxiv.org/abs/2509.21091 [d08]
- [V] Nitarach 2026, Model capability dominates (AIMO 3). https://arxiv.org/abs/2603.27844 [d09]
- [V] Ali 2026, Where cross-question structure in LLM errors comes from. https://arxiv.org/abs/2607.20464 [d10]
- [V] Aghazadeh et al. 2026, CGES. https://arxiv.org/abs/2511.02603 [d11, d18]
- [V] Fu et al. 2025, Deep Think with Confidence. https://arxiv.org/abs/2508.15260 [d12, d18]
- [V] Shi and Jin 2025, Heimdall. https://arxiv.org/abs/2504.10337 [d13]
- [V] Sareen et al. 2025, Putting the value back in RL (RL^V). https://arxiv.org/abs/2505.04842 [d14]
- [V] Kang et al. 2025, Self-certainty best-of-N. https://arxiv.org/abs/2502.18581 [d15]
- [V] OPPO AI Agent Team 2025, Scaling test-time compute for LLM agents. https://arxiv.org/abs/2506.12928 [d16]
- [V] Huang et al. 2025, m1 medical test-time scaling. https://arxiv.org/abs/2504.00869 [d17]

Links to other subfields (not covered here): adaptive stopping and metareasoning (08), verification design (04), wisdom of crowds: conditions, expected value of sample information, scoring rules and calibration, heuristic search.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 9 established claims: 7 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C01.02-K01** (number corrected). R1 Table 15: distilled models gain 10.3 to 29.6 points at cons@64 on AIME 2024 (Distill-Llama-8B 50.4 to 80.0 is +29.6), not 10-28; other numbers (56.5 to 74.4; 60.1 to 78.0; More Agents GSM8K 12-24 points) match. Corrected claim: Majority vote over 5-40 sampled CoT paths raises accuracy on math and reasoning for capable models; e.g. PaLM-540B GSM8K 56.5 -> 74.4, code-davinci-002 60.1 -> 78.0, More Agents GSM8K +12 to +24 points, and R1-distilled models gain 10 to 30 points on AIME 2024 at cons@64 (Distill-Qwen-14B +10.3 to Distill-Llama-8B +29.6).
- **C01.02-K07** (reworded: the sources support less). Numbers match Brown et al. 2024, but 'only closed by an automatic verifier' is stronger than the paper (it says coverage turns into accuracy where verifiers exist and warns that even unit-test verifiers are imperfect, Sec 4.2); five of six evidence lines are the same paper, with Cobbe 2021 not bearing on the voting result. Corrected claim: In Large Language Monkeys (Brown et al. 2024), coverage keeps rising with sampling while voting and reward-model selection plateau near 100 samples (Llama-3-8B-Instruct MATH: coverage 82.9 to 98.44% from 100 to 10,000 samples; majority vote or reward model 40.50 to 41.41%); in domains with automatic verifiers (tests, proof checkers) coverage translates into accuracy (SWE-bench Lite with DeepSeek-Coder-V2 15.9% to 56% at 250 samples), though the authors note even such verifiers are imperfect. Single-paper evidence.
- **C01.02-K02** (now single-source: only one opened source, code check).
- **C01.02-K08** (now single-source: only one opened source, code check).
