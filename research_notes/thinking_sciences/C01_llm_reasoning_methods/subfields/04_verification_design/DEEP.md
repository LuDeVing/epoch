# Verification design: deep document

*Subfield C01.04. Evidence files: evidence_a-d.jsonl (ids a01-a27, b01-b27, c01-c27, d01-d28). Claims: claims.jsonl (C01.04-K01 to K31). Cross-check: critique.md. All numbers below were re-opened by the critic unless marked otherwise. Almost all evidence is math or code. Judge-bias numbers are from 2023 models.*

## 1. What it is

A verifier is any step that says whether a candidate output is good. The scaffold uses it to pick, reject or repair candidates. The subfield asks which verifier to build, how far to trust it, and how much budget it deserves.

Verifier types, from most to least trustworthy:

1. **Executable or exact checkers.** Unit tests, a plan validator, a constraint script, string match against a key. Cheap, sound if the checker is correct. They still fail (flaky tests, wrong tests, format mismatch).
2. **Learned discriminative scorers.** Outcome reward models (ORM) score the whole answer. Process reward models (PRM) score each step. Trained on human labels, Monte Carlo rollouts or an LLM labeler.
3. **Generative verifiers.** A model writes a check (a short chain of thought), then says Yes or No. Several checks are sampled and combined by code. Trained (GenRM, ThinkPRM) or prompted.
4. **LLM-as-judge.** A prompted model compares or grades. Pairwise, pointwise, with or without a reference.
5. **Self-verification.** The generator checks its own answer. Includes the "wait, let me recheck" inside a reasoning trace.
6. **Consensus.** Majority vote, weighted vote. This is a selector, not a verifier, but it is the baseline every verifier must beat at equal tokens.

Three questions run through the whole subfield.

- **Is checking easier than solving?** Sometimes. Not by default for an LLM.
- **What does the verifier cost, and what does it buy at equal tokens?**
- **How does the verifier fail?** False positives (accepts wrong), false negatives (rejects right), bias (position, length, self-preference), and being gamed once search pushes on it.

Why this matters for our agent: the schema already says "code selects" (G5), "revise only from real output" (G2), "a pass must be on something not fitted to" (G3), and "samples are not independent" (G4). This document supplies the numbers behind those rules and finds where they need refinement.

## 2. History and theories in depth

**2.1 Verifier as reranker (2021).** Cobbe et al. introduced GSM8K (8.5K problems) and the recipe: sample many solutions, rank with a trained verifier, return the top one (a01, b01). The authors report about the boost of a 30x larger model. Two caveats were in the paper itself. A verifier does not beat plain fine-tuning with small training sets (b02, K21). And the 6B verifier's accuracy peaks near 400 completions per problem and then falls, because search finds "adversarial solutions that fool the verifier" (a01, b03). Token-level scoring beat solution-level scoring (b04). A large generator with a small verifier beat the reverse (b04).

**2.2 Outcome versus process (2022-2023).** Uesato et al. (a02, c03) compared outcome-based and process-based feedback on GSM8K. Final-answer error was about the same (22.3% vs 23.5% without a reward model; 14.8% vs 16.6% with one). Trace error (right answer, wrong reasoning) differed a lot. Best result: 12.7% final-answer error (prior 16.8%) and 3.4% trace error (prior 14.0%). Lightman et al. (a03, b05) then showed on MATH that step-level human labels (PRM800K, 800K labels) beat outcome labels: best-of-1860 PRM 78.2%, ORM 72.4%, majority vote 69.6%. Math-Shepherd (a04) replaced human labels with Monte Carlo rollouts: a step is good if completions from it reach the right answer.

**2.3 The overoptimisation theory (2022).** Gao, Schulman and Hilton (a18, b20, c22) used a synthetic gold reward model to study what happens when you optimise against a proxy. Gold reward rises then falls. Best-of-n follows R = d(alpha - beta d); RL follows R = d(alpha - beta log d); d is the square root of KL from the start. Best-of-n KL grows about as log n. This is the clean model for why Cobbe's curve bends. Policy size had a weak effect on the amount of overoptimisation. Caveat: synthetic gold model, 1.2B policy, chat tasks.

**2.4 The resampling-ceiling theory (2024).** Brown et al. (a07, a25) measured coverage (any sample correct) over four orders of magnitude of samples: log-linear growth. With an exact checker, coverage becomes accuracy. With a vote or reward model, selection saturates near 100 samples. Stroebl et al. (a09, b11, b12, c07, d20) gave the theory: if the verifier's false-positive rate is above zero, resampling has a ceiling that no budget lifts, and weaker generators have higher false-positive rates. With a cost on false passes the best number of tries is small.

**2.5 The self-correction reckoning (2023-2024).** Huang et al. (a10, b25, c18) showed that earlier self-correction gains came from oracle labels. Without them, GPT-3.5 and GPT-4 got worse. Stechly et al. (a12, a13, c19) showed that GPT-4 as its own verifier has huge false-negative rates on graph colouring and Mystery Blocksworld, and that a sound external verifier gives the gain while the critique text barely matters. Tyen et al. (c20) showed the weak link is finding the mistake, not fixing it.

**2.6 LLM-as-judge and its biases (2023-2026).** Zheng et al. (a14, a15, b21-b23, c14) set the baseline: GPT-4 agrees with humans 85% (human-human 81%) but has position, verbosity and self-enhancement bias and weak math grading. Wang et al. (c15) showed order swaps flip winners. Shi et al. (a17) ran 150,000+ evaluations: bias depends on judge, task and the quality gap. Panickssery et al. (a16, b24, c16) tied self-preference to self-recognition. Wataoka et al. (c17) argued for familiarity (low perplexity). Pombal et al. 2026 (d16, d17) tested both on correctness-checked tasks and found recognition the stronger correlate.

**2.7 Generative verifiers and the compute accounting fight (2024-2025).** Zhang et al. (a05, b13, b14, c10) proposed GenRM: next-token training so the verifier writes a check before Yes/No, with votes. Large gains over discriminative RMs. Singhi et al. (a06) then charged for verifier tokens and found self-consistency more efficient at most budgets. Both are right under their own accounting (critique). Training-free variants (Zhao d01, d02; SETS d03; V1 d27) test the idea without fine-tuning.

**2.8 Step-labelling critique (2024-2025).** ProcessBench (a21, b15, b16, c11) tested first-error finding on 3,400 expert-labelled cases. Open PRMs trained on Monte Carlo labels generalise badly; prompted strong models do better. The Lessons paper (b17, b18) showed best-of-N hides the weakness: ProcessBench F1 28.9 / 40.1 / 46.5 / 56.5 for four label sources, but best-of-8 64.3 / 65.9 / 65.3 / 64.9.

**2.9 Reward hacking against verifiers (2025-2026).** Pitfalls of rule- and model-based verifiers (d07, d08), noisy-verifier RL theory (d09), and gaming by RL-trained reasoners (d10). The lesson: static accuracy of a verifier does not predict whether it can be gamed, and stronger reasoners find more shortcuts.

**2.10 Adaptive allocation (2024-2026).** Snell et al. (a19, a20, b19, c09) showed the best verifier-search method depends on difficulty and budget. Agreement among a few pilot samples works as a cheap difficulty signal (d24, d25).

## 3. Core findings with exact numbers

Status: E = established (2+ independent groups), S = single source, C = contested. Ids refer to evidence files.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Exact checker lets coverage grow log-linearly with samples | SWE-bench Lite 15.9% (1 sample) to 56% (250); prior single-attempt best 43%. CodeContests Gemma-2B 0.02% to 7.1% at 10,000 samples | Brown 2024 (a07, b08, c05) | S (one paper; Cobbe and Stroebl support direction) |
| Vote and reward model stall while coverage keeps rising | MATH, Llama-3-8B-Instruct: coverage 82.9% (100) to 98.44% (10,000); vote or reward model 40.50% to 41.41%. Plateau near 100 samples | Brown 2024 (a25, b09) | S |
| Test suites are imperfect | 11.3% of SWE-bench Lite problems have flaky tests that can fail the gold patch. 35 of 122 CodeContests Python3 problems have listed correct solutions that fail tests. Over 90% of 105 graded GSM8K chains faithful | Brown 2024 (a08, b10, c06) | S |
| Learned-verifier best-of-N peaks then falls | Cobbe: 6B verifier peaks near 400 completions (tested to 3200). Gao: gold reward rises then falls. Snell: beam search against PRM hurts on easy items and at large budgets | a01, b03, a18, b20, a19, b19 | E |
| Verifier false positives cap resampling | Optimal K about 5 at false-pass cost ratio 4; K = 0 at ratio 10. False-positive rate rises with K because remaining tasks are hard. Weaker models have more false positives, linear in single-sample accuracy | Stroebl (a09, d20) | E (theory plus HumanEval+/MBPP+, one group; Brown supports) |
| Self-correction without feedback does not help | GPT-3.5 GSM8K 75.9 / 75.1 / 74.7 (oracle labels 84.3). GPT-4 95.5 / 91.5 / 89.0. CommonSenseQA GPT-3.5 75.8 / 38.1 / 41.8. Keeps first answer 74.7% | Huang 2023 (a10, b25) | E |
| Same on a newer math model | Qwen2.5-Math-7B MATH500: 71.6 to 70.4 intrinsic; with gold reward in prompt 65.4 to 51.4 (right-to-wrong 15.4%, wrong-to-right 1.4%) | Xiong 2025 (d12) | E (with Huang, Stechly, d11, d13) |
| RL-trained small models rarely self-correct | Shifts in 6.31% of traces, mildly harmful (-0.031 to -0.062). Qwen3-8B: 85-95% of rechecks confirmatory. Forced recheck at high entropy: 0.3221 to 0.4062 (+8.41 points; 50,574 wrong-to-right vs 23,500 right-to-wrong) | d'Aliberti 2026 (d11), Long 2026 (d13) | E for direction; sizes 1.5B-8B only |
| GPT-4 self-verifier false negatives (2023) | Graph colouring: rejects 113 of 118 correct (95.8%). Mystery Blocksworld: 100 of 103 (97.09%). Game of 24: FPR 10.4%, FNR 20.7%, accuracy 87.0%. Blocksworld row dropped (inconsistent) | Stechly 2024 (a12) | C |
| Plan checking by current models is good | Trip Planning error recall / precision: Claude-3.5-Sonnet 91.85 / 93.74; Gemini-1.5-Pro 94.04 / 97.51. Math/code rows often recall 20-35 or precision 15-30 | SETS (d04) | S |
| Prompted verifier with 20 averaged checks | Gemini 1.5 Pro, MATH level 5 and AIME 2023: error rates 7-23% per type (main prompt 14%/17% MATH, 7%/7% AIME) | Zhao 2025 (d02) | S; error labels reversed in paper |
| o1-preview misses impossible goals | Blocksworld: 27% correctly marked unsolvable, 54% full impossible plan. Mystery: 16%, 79%. Falsely "unsolvable" 11.5% on Mystery | Valmeekam 2024 (d15) | S |
| Order swap: judge consistency | GPT-4 65.0%, GPT-3.5 46.2%, Claude-v1 23.8% (favours first 75.0%). Few-shot raises GPT-4 to 77.5% at about 4x cost | Zheng 2023 (a14, b21, c14) | E (Wang c15, Shi a17) |
| Verbosity attack | "Repetitive list" fooled Claude-v1 and GPT-3.5 91.3% of 23 cases; GPT-4 8.7% | Zheng 2023 (b22) | S (23 items) |
| Judge math grading failures | 14/20 default, 6/20 CoT, 3/20 reference-guided (10 questions, 20 trials) | Zheng 2023 (b23) | S |
| Judge-human agreement | GPT-4 85% (no ties), human-human 81% | Zheng 2023 (a14) | S |
| Self-recognition and self-preference | GPT-4 73.5% self-recognition out of the box; over 90% after 500 fine-tuning examples (GPT-3.5, Llama 2). Linear link on CNN/DM | Panickssery 2024 (a16, b24) | E (with d16) |
| Self-preference on correctness tasks | LiveCodeBench risk ratio of false acceptance: 1.88 when recognised, 0.72 when not; 1.48 in lowest-perplexity quartile. Own-output length quartiles: 0.90, 3.12, 2.66, 5.32. 12 judges, 177 problems, 5,685 tests | Pombal 2026 (d16) | S for sizes; direction E |
| Committee of five families | Cuts self-preference significantly for 4 of 5 members on LiveCodeBench; not removed. Pairwise worse than rubric | Pombal 2026 (d17) | S |
| PRM beats ORM and vote on hard math | MATH best-of-1860: 78.2 / 72.4 / 69.6. OOD 234 STEM problems best-of-100: 72.9 / 63.8 / 61.3. Active learning 2.6x data efficient | Lightman 2023 (a03, b07) | S for size (one lab); direction E with Uesato |
| Trace error hidden by answer check | GSM8K trace error 14.0% to 3.4%; final-answer error 16.8% to 12.7% | Uesato 2022 (a02) | E (Lightman, Lessons b18) |
| Open PRMs generalise poorly | ProcessBench F1 GSM8K/MATH/Olympiad: Math-Shepherd-PRM-7B 47.9 / 29.5 / 24.8; PRM800K-trained Qwen2.5-Math-7B 68.2 / 62.6 / 50.7; GPT-4o 79.2 / 63.6 / 51.4; o1-mini 93.2 / 88.9 / 87.2. Averages: o1-mini 87.9, QwQ-32B 71.5, GPT-4o 61.9 | Zheng 2024 (a21, b15) | E |
| Best-of-N hides step weakness | ProcessBench F1 28.9 / 40.1 / 46.5 / 56.5 vs best-of-8 64.3 / 65.9 / 65.3 / 64.9. About 40% of data kept by consensus filtering | Zhang 2025 Lessons (b17, b18) | S |
| Step scorers do not transfer outside math | Math PRMs add at most +0.71 over vote in non-math MMLU-Pro subjects (Philosophy +0.34, History +0.20) vs +4.80 on math. Multi-domain PRM Law +7.9% | VersaPRM (d21) | S |
| Labeler needs key and step definitions | Without them, agreement on chains first labelled correct fell to 7% (30 questions) | VersaPRM (d22) | S |
| Generative verifier vs discriminative | Best-of-N: algorithmic 5% to 45.3%; GSM8K 73% to 93.4%; MATH 28% to 44.6%; MMLU abstract algebra 37.9% to 53.5%. 2.5x fewer solutions than discriminative RM | Zhang 2024 (a05, b13) | E for direction (ThinkPRM c13 abstract-level) |
| SC beats GenRM at practical budgets | GenRM matches SC only after up to 8x compute. S_opt ~ C^0.57, V_opt ~ C^0.39. Up to 30% relative gain on MATH level 5 | Singhi 2025 (a06) | C |
| Training-free verify-then-vote | Gemini 1.5 Pro, Verification@200 vs Consistency@1000: AIME 8/15 vs 3/15; LiveBench Reasoning 97 vs 73 of 140; MATH 467 vs 460 of 500. Cost about 130M tokens per AIME question. Without tie-break MATH 457 (below Cons@200 at 460) | Zhao 2025 (d01) | S |
| Self-verify best-of-N on planning | Trip Planning: vote 49.9, self-verify 60.6, SETS 68.5. Meeting: 48.8 / 55.7 / 59.6. MATH500: 87.8 / 88.7 / 89.3. AIME: 32.2 / 28.3 / 33.3 | SETS (d03) | S |
| Debate does not beat voting | GSM8K GPT-3.5: SC 85.3 (6), 88.2 (9) vs debate 83.2 (6), 83.0 (9) | Huang 2023 (a11, b26) | S here; E in the schema via other fields (G9) |
| Difficulty-aware allocation | Up to 4x less compute than best-of-N (16 vs 64 generations) with oracle bins; shrinks with predicted bins | Snell 2024 (a19, a20) | E in direction |
| Pilot agreement as difficulty signal | 33-65% fewer calls at matched vote accuracy (3B, n=50 and 30); up to 75% offline and 55% online smaller budget on GPQA (vs infinite-budget vote) | d24, d25 | E in direction, weak data |
| Model-written tests share the model's blind spots | Fault detection 25% (independent) vs 14% (written after faulty code); seeing implementation costs 13.2% on average; CoT and CoVe do not fix. CodeT HumanEval 47.0 to 65.8 | Konstantinou 2026 (d18), CodeT (a23) | E |
| Different model family for tests | No difference in Elixir (459 implementations, 2,709 suites); 99 of 247 faulty caught only by hand-written tests | Leu 2026 (d19) | S |
| Model verifiers can be gamed | Rule-based recall 86% (14% correct rejected). Adversarial strings: up to 77.9% fooled on one judge. Trained verifier collapsed after about 450 RL iterations. 13 hacking patterns | Pitfalls (d07, d08) | S (math, RL) |
| RL reasoners shortcut instance checkers | Shortcuts 40 (levels 1-10) vs 458 (levels 11-20); gpt-5-mini 0 / 32 / 84 across low / medium / high effort | Helff 2026 (d10) | S |
| Weighted weak-verifier ensemble | Weaver average 87.7 vs vote 72.2, naive top-10 ensemble 69.1, best reward model 72.7, oracle pass@100 91.9. Naive threshold 79.0 vs 87.5 with 5% labels. Dropping extreme verifiers 79.4 to 85.2. Pairwise score correlation about 0.03 | Weaver (d05, d06) | S (internal inconsistencies) |
| Voting errors not positively correlated | 19 estimates all negative, mean -0.348 (-0.122 for N >= 7). Best vote 42/50 vs pass@20 45.5 | Nitarach 2026 (d23) | S |
| Pairwise self-verification | Up to 10% Pass@1 over pointwise on code and math | V1 (d27) | S (abstract level) |
| Hidden-state probes | AUC above 0.7 in-distribution; above 0.9 on AIME at 32B; 24% fewer tokens with early exit | Zhang 2025 (d14) | S; needs weights |

## 4. Mechanisms and models

**4.1 Coverage versus selection.** Define coverage C(N) = share of items where at least one of N samples is right. Define selected accuracy A(N) for a given selector. A(N) <= C(N). With an exact checker, A = C. With a vote or learned scorer, A flattens while C keeps growing (41% vs 98% on MATH). The gap C - A is the room a better verifier can fill. To use: log both on every run. The gap tells you whether to spend more on sampling (gap small) or on verification (gap large).

**4.2 Why a vote has a ceiling.** The vote picks the mode. If the right answer is sampled rarely, it never wins (a25). Adding samples sharpens the mode, not the rare answer. So escalate from vote to a check that does not depend on frequency when the answer split is flat.

**4.3 Resampling with an imperfect checker (Stroebl).** Let p be the chance a sample is right, f the chance a wrong sample passes the checker. Accept the first pass. Expected result: correct with probability p / (p + f(1-p)) per accepted answer, which never reaches 1 if f > 0. As K grows, easy items are already solved and the remaining items are hard, where f is high. So the false-pass rate among accepted answers rises with K. Marginal rule (the critic's reading of the setup, not a stated formula): keep sampling while P(next accepted is right) x benefit > P(next accepted is a false pass) x cost. Implement: log accept rate; audit a small sample of accepted answers against a held-out test; estimate f; stop at K where the marginal condition fails. At cost ratio 4, K is about 5.

**4.4 Overoptimisation (Gao).** Selection pressure d = sqrt(KL). Gold reward = d(alpha - beta d) for best-of-n. Peak at d = alpha / (2 beta). Practical form: for a model-judge selector, plot accuracy against N on held-out items and pick N at or below the peak. An independent check not seen by the selector breaks the loop.

**4.5 Verifier error channel.** Treat a verifier as a noisy channel with false-positive rate f and false-negative rate g (d09). Reject-loops lose when g is high: the loop discards correct answers and moves to worse guesses (Stechly). Resampling loops lose when f is high. Measure both on a labelled set per task type before enabling a loop. The forward correction in d09 needs only g, which is easier to estimate than f.

**4.6 Generative verification pipeline (implementable).** For each candidate (or pair): sample k short check chains at temperature above zero; each ends in a Yes/No or a pair choice; code aggregates (mean of Yes votes, or majority). Combine with the vote as a weighted vote. Use a tie-break role: verify only among the top 2 answers of the vote. Strip the candidate's own explanation before the check (d08), do not reveal authorship (a16), run both orders (b21), and give the verifier a reference computed by code when one exists (b23).

**4.7 Weighted ensemble of weak checks (Weaver).** Run m different checks (code run, constraint script, different-family judge, pairwise compare). On a labelled dev set of 30-100 items measure each check's true-positive and false-positive rate. Drop checks that are nearly always positive or always negative. Weight the rest by log-odds from the measured rates. Unweighted averaging of correlated checks does not work (69.1 vs vote 72.2). Weaver needs 1-5% labels.

**4.8 Perturbation test (Helff).** Before accepting an answer that passes an instance-level check, change the instance (rename objects, reorder, new inputs) and re-run. A shortcut that lists labels fails the perturbed version. This is the executable form of G3.

**4.9 Spec-first checks.** Write checks from the task statement in a fresh context, before or without the candidate (d18). The implementation in view drops fault detection from 25% to 14%.

**4.10 Difficulty routing.** Draw 3 pilot samples. If they agree, stop. If they split, add samples up to a cap, then escalate to the best checker available. Snell's oracle-bin gain is up to 4x; with predicted bins it shrinks. Pilot agreement is a cheap predictor (d24, d25) but routing between vote, search and verify by it is untested.

**4.11 Two-order pairwise judging.** Run the pair in both orders. Accept only a consistent verdict; otherwise call it a tie and fall through to another check. GPT-4 consistency is 65.0% by default, so about a third of pair verdicts are order-dependent at 2023 quality.

## 5. What holds up

**Replications and agreement across groups**

- Learned-verifier best-of-N is not monotone: Cobbe, Gao and Snell agree through different methods (K02, E).
- Self-correction without feedback fails: Huang 2023, Stechly 2023-24, Tyen 2024, Xiong 2025 (Qwen2.5-Math-7B), d'Aliberti 2026, Long 2026 (K05, K29, E). The direction now holds on 2025-2026 small and mid reasoning models.
- Answer checks hide wrong reasoning: Uesato, Lightman, Lessons (K10, E). Lightman themselves say the problem may be over-emphasised on MATH, and Uesato says the ORM-approximates-PRM effect may be dataset-specific.
- Open PRMs trained on automatic labels fail on hard items: ProcessBench, Lessons, Snell's own PRM800K failure (K11, E).
- Model-written tests share blind spots: CodeT's own limits, Konstantinou 2026 (K17, E).
- Order, length and self-preference biases: Zheng, Wang, Shi, Panickssery, Pombal (K12, K14, E).

**Contested or single-source**

- GenRM vs self-consistency (K08, C). Zhang (no verifier-token charge) vs Singhi (charged). Training-free work (Zhao, SETS) shows crossovers only where voting has saturated (AIME, LiveBench Reasoning) or where checking is easy (planning). On MATH, tie-breaking explains most of Zhao's gain (457/500 without it, below Cons@200 at 460). No paper tests a true equal-token crossover curve for a training-free verify step.
- Prompted self-verification error rate (K06, C). Stechly's 95%+ false negatives were GPT-4 in 2023 on colouring and Blocksworld; both papers are one group; the Blocksworld row is internally inconsistent. SETS found good plan checking in Claude-3.5 and Gemini-1.5. o1-preview misses impossible goals (d15). No current-model replication of colouring.
- Self-preference cause: recognition (Panickssery, Pombal) vs familiarity (Wataoka c17). Pombal's observational binning favours recognition; the two accounts are not tested head to head by intervention.
- Different model family as checker: no benefit in Elixir (d19), but Elixir is rare, so shared blind spots are likely.

**Failed or weak interventions**

- Debate: no better than voting at equal responses (K15).
- Prompt diversity for voters: lowered score monotonically on gpt-oss-120b; errors already scatter (d23).
- CoT and chain-of-verification for test writing: did not fix coding-before-testing (d18).
- Model judges that solve first: copy the candidate's error (b23).
- Reasoning effort did not reduce self-preference on IFEval (d16).
- More rechecking inside a trace: 85-95% confirmatory (d13).
- Majority vote plus verifier vs verifier alone on GSM8K: 92.5 vs 93.3 (a04).
- Average of correlated verifiers (Weaver): worse than vote.

**Moderators**

- Verifier type: exact checker >> generative >> discriminative >> self-check on frequency-flat items.
- Task: planning with checkable constraints (verification easy) vs graph colouring (verification as hard as solving, 2023 GPT-4) vs AIME (voting wins).
- Difficulty: beam search hurts on easy items; false pass rate rises with hard remaining items; process errors in correct-answer chains grow with problem difficulty (b18).
- Quality gap: judge bias is worst when options are close (a15, a17).
- Candidate length: false acceptance ratio rises with own-output length (0.90 to 5.32 across quartiles, d16).
- Budget: SC wins at small budgets; verification gains at larger ones or on the hardest level (a06).
- Reference present: judge failure 14/20 down to 3/20 (b23); labeler agreement 7% without key and step definitions (d22).

**Problems in the evidence**

- Independence: most lines trace to about 12 papers (critique). Many "single-source" statuses are real.
- Judge-bias numbers are 2023 models with small samples (23 answers, 20 trials, 10 math questions, 80 questions).
- Weaver contradicts itself (gap 13.5, 12.3 and 15.5 points); Zhao labels FPR backwards; SETS Table 2 and Pitfalls Table 4 were scrambled in extraction.
- Gao is a synthetic gold model: shape, not size.
- Not opened in full: c13 (abstract/intro), c17 (effect sizes not extracted), d27 and d28 (abstract/intro level), c25 (not opened), b27 (an agent synthesis, not a source).
- The Stroebl optimal-K figure differs between lines (below 10, about 5, 3 or less); the direction is firm, the number depends on the cost ratio.

## 6. Language models

**What changed things, by how much**

| Change | Effect | Id |
|---|---|---|
| Add a real executable checker | SWE-bench Lite 15.9% to 56% | a07 |
| Swap checker for vote or reward model | 41.41% vs 98.44% coverage at 10,000 | a25 |
| Trained verifier over fine-tuning (GSM8K) | about a 30x model-size boost | a01 |
| PRM over ORM over vote (MATH best-of-1860) | 78.2 / 72.4 / 69.6 | a03 |
| Generative verifier over discriminative | 2.5x fewer solutions | a05 |
| Count verifier tokens | SC wins until up to 8x compute | a06 |
| Judge sees a reference | math failures 14/20 to 3/20 | b23 |
| Judge reasons first | 14/20 to 6/20 | b23 |
| Swap order, keep consistent | needed: Claude-v1 consistent only 23.8% | b21 |
| Few-shot judge prompt | GPT-4 consistency 65.0% to 77.5%, about 4x cost | c14 |
| Forced reconsideration at high entropy | +8.41 points on math (small RL models) | d11 |
| Prompted reconsideration on every item | -1.2 on Qwen2.5-Math-7B MATH500 | d12 |
| Weighted weak-verifier ensemble | 72.2 (vote) to 87.7 | d05 |
| Spec-first tests | fault detection 14% to 25% | d18 |
| Pilot-agreement early stop | 33-65% fewer calls at matched accuracy | d24 |

**Behaviours to expect**

- Self-judgement: models keep their first answer (GPT-3.5 74.7%) and flip right to wrong more than wrong to right. RL-trained small models mostly confirm (85-95%).
- Latent knowledge: hidden states carry correctness (AUC above 0.9 on AIME at 32B) that the output does not use. This is an argument that an independent short check can add something, but it cannot be read through an API.
- Verifier quality tracks base strength: o1-mini F1 87.9 vs GPT-4o 61.9 as step critic. A strong prompted critic can beat a trained PRM.
- Verification depends on task: good for plan constraints (recall 92-94%), poor for impossible goals (73-84% missed by o1-preview), mixed for math (7-23% error even with 20 checks).
- Gaming: stronger reasoning finds more shortcuts (gpt-5-mini 0 to 84 with effort). Generative judges are more fooled by "the answer is correct" text than discriminative ones (77.9% for one prompted judge on an answer-explanation pattern).
- Self-preference grows with recognition and length (ratio 1.88 recognised; 5.32 in the longest quartile on LiveCodeBench).
- Judges conform to the stated answer; having the judge solve first copies the candidate's mistake (b23).

**Not known for frontier reasoning models**

No test of o-series, full R1 or current Claude models on intrinsic self-correction (gap 3) or on self-verification outside math and code (gap 2). All sizes in this section are from older or smaller models.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5.

### Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | Prefer code-checked selection wherever a check exists. Build the checker from the spec, not from the candidate. Run it twice and treat disagreement as no signal. | G3, G5, S4 | [E] for direction (code beats vote); flaky figures [S] | a07, a08, b10, c06, d18 |
| A2 | Cap the number of resamples against any imperfect checker. Default K near 5; log accept rate; audit a sample of accepted answers. Never score success with the selecting tests. | G3, G7, S4 | [E] direction; K value [S] | a09, d20, b12, c07 |
| A3 | Do not let a model learned-scorer or model judge pick among very many samples without a cap on N and an independent held-out check. | G7, G12, S7 | [E] | a01, b03, a18, a19 |
| A4 | Revise only after an external signal (failed check, vote disagreement). No default self-review round. Already G1/G2; evidence now also covers 2025-2026 small reasoning models. | G1, G2, S5 | [E] | a10, b25, d11, d12, d13, a12, c20 |
| A5 | Any model judge: hide authorship and majority, strip the candidate's own explanation, judge both orders, accept only consistent verdicts, use a different model family from the generator when possible. | G5, S8 | [E] | b21, a14, c15, a17, a16, d16, d17, d08 |
| A6 | If a model judge is used on exact-answer items, give it a reference computed by code, not the candidate. Do not use a model judge where code can check. | G5, S8 | [E] direction; sizes [S] | b23, d22, d26, a15 |
| A7 | Do not use model-written tests as independent evidence. Write checks from the task text in a fresh context. | G3, G4, S4 | [E] | a23, c21, d18 |
| A8 | Before accepting a pass on an instance-level check, run a perturbed version (rename, reorder, new inputs). | G3, S4 | [S] on size, direction [E] with G3 | d10, d07, d08 |
| A9 | Measure any step-level or prompted verifier on first-error location or a labelled set, not only on final selection. | S8 | [E] | a21, b15, b17, d21 |
| A10 | Do not use step-level scorers outside the domain they were calibrated on. | S8 | [S] | d21, d22 |
| A11 | Use a cheap pilot (2-4 samples) as a difficulty signal for how many samples to draw. | S0, G12 | [E] direction, weak data | d24, d25, a19, a20 |
| A12 | Keep debate out; spend the calls on independent samples. Do not add prompt diversity for voters. | G9, G4 | [E] / [S] | a11, b26, d23 |
| A13 | Spend verification effort on independent checks, not on in-trace rechecks. | G2, G11 | [E] | d13, d11 |
| A14 | Keep a sound external validator for planning, including a few unsolvable cases when auditing the checker. | G5, S8 | [S] | d15, a12 |

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | k short check chains plus a code aggregator vs plain voting at equal tokens. | S8, G12 | [C] | a05, a06, d01, d03, c10 |
| T2 | Pairwise check of the top two voted answers (verification as tie-break) vs vote only. | S8 | [S] | d01 (Table 3), d27, d02 |
| T3 | Vote disagreement as the trigger for any second look vs no trigger vs one more sample. | G1, S5 | [S] (forced recheck helped in small RL models) | d11, d12 |
| T4 | Gate verification by difficulty: pilot agreement routes between vote, check and search. | S0, G12 | [S] | a19, a20, d24, d25 |
| T5 | Weighted ensemble of 3-5 diverse checks using accuracy measured on 30-100 labelled items. | G5, S8 | [S] | d05, d06 |
| T6 | Cap K from measured false-pass rate (marginal rule). | G3, G7 | [S] | d20, a09 |
| T7 | Measure our own prompted verifier's false-negative and false-positive rates per task type before enabling a reject loop. | G5, S8 | [C] | a12, d04, d02, d15 |
| T8 | Judge given an independently sampled reference vs code reference vs none. | G5 | [S] | b23, d22, d26 |
| T9 | Different-family checker vs spec-only context isolation. | G4, G5 | [S] | d19, d18 |
| T10 | Step-level check on correct-answer cases to measure right-answer-wrong-reasoning in our tasks. | S8 | [E] on math; unknown elsewhere | a02, b18, d21 |
| T11 | Record failed attempts and their failure reason in memory and show them after the first attempt of later items. | memory | [S] | a22 |
| T12 | Reserve part of a long run's budget for verification. | G12 | [S] | c23, d28 |
| T13 | Static quality checks as a weak secondary signal on top of tests. | S4 | [S] | c08 |

## 8. Concrete tests on our bench

All arms get equal total tokens, including verifier tokens and setup (G7). Report the selected accuracy, the coverage (oracle), and the C - A gap.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T-A: checked vs voted | Items with a code checker (code, ARC-like programs, constraint puzzles) | N checked samples vs N voted samples, N = 4, 8, 16 | Held-out accuracy; gap to coverage | Checked arm higher at N >= 8; gap shrinks (K01) |
| T-B: N sweep for a model-judge selector | Items with only a model judge | Judge selector at N = 4, 8, 16, 32, 64 vs vote at same tokens | Accuracy vs N; location of peak | Peak or plateau for judge; none for code check (K02) |
| T-C: K cap | Code items with a draft test suite and a held-out suite | K = 3, 5, 10, 30 resamples against draft tests | Held-out pass of the accepted answer; share of false passes | Held-out accuracy flat or falling after K about 5 (K03) |
| T-D: self-critique vs extra sample | Reasoning items with exact answers | One critique round vs one more independent sample, equal tokens | Right-to-wrong and wrong-to-right flips; accuracy | Critique loses or ties (K05) |
| T-E: verify chains vs vote | Mixed set split by difficulty (pilot agreement) | Vote at S samples vs vote at S/2 plus k = 4 check chains with code aggregator | Accuracy by difficulty bin | Gain only on hard or vote-flat bins; loss on easy (K08, K22) |
| T-F: pairwise tie-break | Items where the top two vote shares are within 10 points | Vote alone vs vote then pairwise check of top two | Accuracy on tie items; tokens | A few points on tie items; cheap (d01, d27) |
| T-G: judge order swap | Pairwise judge step on our judge model | Single order vs both orders (accept consistent only, else fall through) | Flip rate; accuracy at 2x judge cost | Flip rate 10-40% depending on model; gain after swap (K12) |
| T-H: reference for judge | Exact-answer items with known right and wrong candidates | Judge with code reference vs independently sampled reference vs none | Misgrade rate | Code reference best; sampled reference between (K13) |
| T-I: authorship blind | Matched pairs from our generator and another model with equal quality | Same-family judge vs other-family judge, authorship hidden vs shown | Preference for own output | Hidden and other-family reduce bias (K14) |
| T-J: perturbation guard | ARC-like and rule-induction items | Accept on pass vs accept on pass plus perturbed re-run | False-accept rate on held-out | Fewer false accepts at small cost (d10) |
| T-K: spec-first tests | Code items | Tests written from spec in fresh context vs tests written after seeing candidate | Fault detection on seeded bugs | About 25% vs 14% (d18) |
| T-L: verifier error rates | Per task type, 30-100 labelled candidates each | Prompted verifier single check vs k = 4 majority | FNR, FPR | Rates differ by task; decide reject-loop use (K06) |
| T-M: ensemble weights | Same labelled sets | Unweighted mean vs accuracy-weighted vs drop-extremes | Selected accuracy | Weighted > vote > unweighted (d05) |
| T-N: pilot routing | Mixed difficulty | Uniform allocation vs pilot-agreement routing | Accuracy at equal tokens | Savings 30-60% at matched accuracy for the vote part (d24); routing between methods unknown |
| T-O: failed-attempt memory | Sequences of similar items | Memory of failed attempts vs none | Repeat-failure rate | Small drop (a22; training evidence only) |

## 9. What does not transfer, and why

- **Training the verifier** (PRM800K, GenRM, V-STaR, ThinkPRM, Math-Shepherd). We run a scaffold on a frozen model. Use these as design arguments only: write-then-judge, vote over checks, weight by measured accuracy.
- **Hidden-state probes** (d14). Need weights.
- **RL-time reward hacking** (d07, d09, d10). Our agent does no RL. The relevant part is that a passing instance check can be a shortcut, and a reasoning judge can be fooled by confident text.
- **Gao's overoptimisation constants.** Synthetic gold, KL units. Use the shape, not the size.
- **Large-budget results** (Brown 10,000 samples; Zhao 130M tokens per question). Far outside a practical per-item budget.
- **Math-only step-label results.** Right-answer-wrong-reasoning rates on GSM8K and MATH may not hold for planning or open tasks. VersaPRM shows step scorers do not carry over.
- **2023 judge numbers** (position consistency, verbosity, self-enhancement). Direction transfers, sizes do not. Measure ours.
- **Chat-preference judging.** Our items have right answers. Rubric or code checks beat pairwise preference.
- **Stechly's 95%+ false negatives.** One group, GPT-4 in 2023, and the Blocksworld row is inconsistent. Do not copy the number; do measure ours.
- **PETS and TrACE savings.** Measure agreement with the vote (PETS) or use a 3B model on n = 30-50 (TrACE). Savings on the vote part only.

## 10. Open questions

1. At equal tokens, does a training-free "k short check chains plus code vote" step beat plain voting for a scaffold, and where is the crossover by difficulty? (Gap 1 partly closed; no equal-token curve.)
2. What are the false-negative and false-positive rates of a current prompted reasoning model on constraint puzzles and planning? (Gap 2.)
3. Do frontier RL-trained reasoners self-correct or self-verify without feedback? Tests so far: 1.5B-8B and Qwen2.5-Math-7B. (Gap 3.)
4. How correlated are solver errors and verifier errors on the items where the generator fails? Weaver's 0.03 is across all scores; Nitarach's estimate is on vote counts. (Gap 8.)
5. What is the right K given a measured false-pass rate? The marginal rule is a reading, not tested. (Gap 5.)
6. Is a sampled (possibly wrong) reference as good as a code reference for a judge? (Gap 10.)
7. Do step-level checks add over answer-level checks outside math? (Gap 7.)
8. Can pilot agreement route among vote, search and verify, not only draw more samples? (Gap 9.)
9. Does self-preference come from recognition or familiarity under intervention (not binning)?
10. Does a different-family checker help in common languages and in reasoning tasks (Elixir null may be a rare-language artefact)?
11. How much of Zhao's gain is tie-breaking, on tasks other than MATH?
12. Reward hacking of verifiers at inference time with selection only, not RL: how fast does a model-judge selector degrade with N at our scale?

## 11. Sources

[V] = opened and read this session (full text, PDF or HTML). [M] = snippet, abstract or intro only. Ids are evidence ids.

- [V] Cobbe et al. 2021, Training Verifiers to Solve Math Word Problems. https://arxiv.org/abs/2110.14168 (a01, a27, b01-b04, c01, c02)
- [V] Uesato et al. 2022, Process- and outcome-based feedback. https://arxiv.org/abs/2211.14275 (a02, a26, c03)
- [V] Lightman et al. 2023, Let's Verify Step by Step. https://arxiv.org/abs/2305.20050 (a03, b05-b07, c04)
- [V] Wang et al. 2023, Math-Shepherd. https://arxiv.org/abs/2312.08935 (a04; c25 listed unopened, a04 cells not re-checked)
- [V] Zhang et al. 2024, Generative Verifiers. https://arxiv.org/abs/2408.15240 (a05, b13, b14, c10)
- [V] Singhi et al. 2025, When To Solve, When To Verify. https://arxiv.org/abs/2504.01005 (a06)
- [V] Brown et al. 2024, Large Language Monkeys. https://arxiv.org/abs/2407.21787 (a07, a08, a25, b08-b10, c05, c06)
- [V] Stroebl, Kapoor, Narayanan 2024, Limits of Inference Scaling Through Resampling. https://arxiv.org/abs/2411.17501 (a09, b11, b12, c07, c08, d20; PDF re-opened for d20 only, v1 numbers not compared)
- [V] Huang et al. 2023, LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (a10, a11, b25, b26, c18)
- [V] Stechly, Valmeekam, Kambhampati 2024, Self-Verification Limitations. https://arxiv.org/abs/2402.08115 (a12, a13)
- [M] Stechly, Marquez, Kambhampati 2023, GPT-4 Doesn't Know It's Wrong. https://arxiv.org/abs/2310.12397 (c19; not re-opened by cross-checker)
- [V] Zheng et al. 2023, Judging LLM-as-a-Judge. https://arxiv.org/abs/2306.05685 (a14, a15, b21-b23, c14)
- [M] Wang et al. 2023, LLMs are not Fair Evaluators. https://arxiv.org/abs/2305.17926 (c15; not re-opened)
- [V] Panickssery et al. 2024, LLM Evaluators Recognize and Favor Their Own Generations. https://arxiv.org/abs/2404.13076 (a16, b24, c16)
- [M] Wataoka et al. 2024, Self-Preference Bias in LLM-as-a-Judge. https://arxiv.org/abs/2410.21819 (c17; effect sizes not extracted)
- [V] Shi et al. 2024, Judging the Judges (position bias). https://arxiv.org/abs/2406.07791 (a17)
- [V] Gao, Schulman, Hilton 2022, Reward Model Overoptimization. https://arxiv.org/abs/2210.10760 (a18, b20, c22)
- [V] Snell et al. 2024, Scaling LLM Test-Time Compute Optimally. https://arxiv.org/abs/2408.03314 (a19, a20, b19, c09)
- [V] Zheng et al. 2024, ProcessBench. https://arxiv.org/abs/2412.06559 (a21, b15, b16, c11)
- [V] Zhang et al. 2025, Lessons of Developing PRMs. https://arxiv.org/abs/2501.07301 (b17, b18)
- [V] Hosseini et al. 2024, V-STaR. https://arxiv.org/abs/2402.06457 (a22; not re-opened by cross-checker)
- [V] Chen et al. 2022, CodeT. https://arxiv.org/abs/2207.10397 (a23, c21)
- [V] Survey on verifiers for test-time scaling. https://arxiv.org/abs/2508.16665 (a24, taxonomy text only)
- [M] Yuan et al. 2024, Free Process Rewards. https://arxiv.org/abs/2412.01981 (c12, abstract-level)
- [M] Khalifa et al. 2025, ThinkPRM. https://arxiv.org/abs/2504.16828 (c13, abstract and intro)
- [V] Tyen et al. 2024, LLMs cannot find reasoning errors but can correct them. https://arxiv.org/abs/2311.08516 (c20; not re-opened)
- [V] Setlur et al. 2025, Scaling Test-Time Compute Without Verification or RL is Suboptimal. https://arxiv.org/abs/2502.12118 (c23, d28; abstract, intro and headings)
- [V] Zhou et al. 2023, IFEval. https://arxiv.org/abs/2311.07911 (c24; prompt counts not re-verified)
- [V] Zhao, Awasthi, Gollapudi 2025, Sample, Scrutinize and Scale. https://arxiv.org/abs/2502.01839 (d01, d02)
- [V] Chen et al. 2025, SETS. https://arxiv.org/abs/2501.19306 (d03, d04; some tables scrambled)
- [V] Saad-Falcon et al. 2025, Weaver. https://arxiv.org/abs/2506.18203 and https://arxiv.org/html/2506.18203 (d05, d06; internal inconsistencies)
- [V] Zhang et al. 2025, Pitfalls of Rule- and Model-based Verifiers. https://arxiv.org/abs/2505.22203 (d07, d08; c27 earlier unread)
- [V] Cai et al. 2025, RL with Verifiable yet Noisy Rewards. https://arxiv.org/abs/2510.00915 (d09; abstract, intro, method outline)
- [V] Helff et al. 2026, LLMs Gaming Verifiers. https://arxiv.org/abs/2604.15149 (d10)
- [V] d'Aliberti and Horta Ribeiro 2026, Illusion of Insight in Reasoning Models. https://arxiv.org/abs/2601.00514 (d11)
- [V] Xiong et al. 2025, Self-rewarding correction. https://arxiv.org/abs/2502.19613 (d12)
- [V] Long et al. 2026, Self-Verification Dilemma. https://arxiv.org/abs/2602.03485 (d13)
- [V] Zhang et al. 2025, Reasoning Models Know When They're Right. https://arxiv.org/abs/2504.05419 (d14)
- [V] Valmeekam et al. 2024, LLMs Still Can't Plan; Can LRMs? https://arxiv.org/abs/2409.13373 (d15)
- [V] Pombal, Rei, Martins 2026, Self-Preference Bias in Rubric-Based Evaluation. https://arxiv.org/abs/2604.06996 (d16, d17)
- [V] Konstantinou, Tambon, Papadakis 2026, On the risk of coding before testing. https://arxiv.org/abs/2607.05139 (d18)
- [V] Leu, Oertel, Hebig 2026, Don't Bother to Use a Second LLM (Elixir). https://drops.dagstuhl.de/storage/00lipics/lipics-vol394-esem2026/LIPIcs.ESEM.2026.11/LIPIcs.ESEM.2026.11.pdf (d19; abstract and intro, not full results)
- [V] Zeng et al. 2025, VersaPRM. https://arxiv.org/abs/2502.06737 (d21, d22)
- [V] Nitarach 2026, Model Capability Dominates (AIMO 3). https://arxiv.org/abs/2603.27844 (d23)
- [V] Sethi 2026, TrACE. https://arxiv.org/abs/2604.08369 (d24)
- [V] Liu et al. 2026, PETS. https://arxiv.org/abs/2602.16745 (d25; abstract, intro, part of tables)
- [V] Li et al. 2025, VerifyBench. https://arxiv.org/abs/2507.09884 (d26)
- [M] Singh et al. 2026, V1. https://arxiv.org/abs/2603.04304 (d27; abstract and intro)
- [M] Saad-Falcon/other unread: c26 Weaver first listing (superseded by d05); b27 is an agent synthesis, not a source.
