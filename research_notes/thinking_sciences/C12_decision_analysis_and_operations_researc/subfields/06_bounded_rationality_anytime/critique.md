# C12.06 critique (cross-check)

## Re-opened this session (arXiv PDF text; PDFs deleted afterwards)
Confirmed against the text: Chen 2024 (1,953% more tokens; 48.6% cut on MATH500 for QwQ-32B-Preview; over 92% first round correct; first round under 60% of tokens); Gema 2025; Ghosal 2025 (82.2 to 87.3 to 70.3%; 20%, 22%, 47%); DEER (19.1-80.1%, +0.3 to 5.0%, latency 27.9% and 36.3-58.6%); Snell (up to 4x, 14x model); Brown (15.9% to 56% at 250 samples, SOTA 43%); s1 (50.0 to 56.7 AIME24; 655/97/8/3/2/1 tries; 12 of 30 over context at 512 steps; Table 3 rows 100/15/56.7, 40/-24/40.0, 60/3/36.7); AnytimeReasoner (AIME24 16.3/19.0/21.9/22.9, mean 39.8/43.0/44.9/46.0, 40,315 problems).

## Corrections
1. a21 and b05 differ on Opus 4. Source: Misleading Math falls to 85-90%; Misleading Python falls to about 80%. The R1 70% to 30% is accuracy with five distractors in the Natural Overthinking setup, not a fixed-length curve. a21 merges these.
2. a17 says 32.7% vs a prior 30.3% on AIME24 is comparable. In the paper this is AR-linear in a second table (a different base setting, R1-Distill 22.3 AIME24, GRPO 28.9), compared with a number reported by another paper (MRT). Treat as weak. The headline numbers in a17 (16.3/19.0/21.9) are from the other table and are correct.
3. a20 gives 48.6% token cut; b08 gives 22.3% for SimPO. Both are right: the paper's best method gives 48.6% on MATH500, SimPO (the default baseline) gives 22.3%.
4. b02 says token-conditional plus truncation has control 100% and slope 13. The extracted Table 3 row reads "0%, 13, 40.0"; column alignment was unclear. Do not cite b02's pairing until checked in the table image.
5. c02 says no exact factor; a07 gives factor 4 from Zilberstein and Russell 1996. Different papers, no real conflict.
6. Independence: a14/b14/b15/c11/c23 are one paper (Snell). a15/b16/b17/c12 are one paper (Brown). a16/a24/b01/b02/b03/c09/c10 are one paper (s1). Counts in claims.jsonl use this, so several claims dropped to single-source.

## Contradictions between sources
- Parallel voting vs sequential extension: Ghosal (parallel up to 22% better at 16K) vs s1 (sequential extrapolated better than voting over 2-64 samples). Different models, tasks, budgets. Contested.
- Illusion of Thinking (collapse) vs Lawsen (artifact). Lawsen shows only preliminary runs, so neither side is settled.
- Snell: beam search helps hard items but amplifies verifier artifacts on easy ones.

## Weak spots
- The classical theory rests on Zilberstein 1996 plus the Zilberstein-Russell AIJ paper and Dean-Boddy. No empirical test of performance-profile budgeting for LLM agents was found (c26).
- Most LLM evidence is math on 1.5B-32B models. AIME24 has 30 items (one item = 3.3 points); many cells are single runs.
- No independent replication of s1 budget forcing or AnytimeReasoner was found. Many baselines are the authors' own.
- Seen only as snippet, abstract or intro: Manvi 2024, AdaptThink, Answer Convergence (title unclear), Su 2025 (deltas not extracted).
- Not opened: Simon 1955/56, Russell and Wefald 1991, Horvitz, Hansen and Zilberstein 2001 (a11-a13, b24-b28, c04, c05, c24, c25). Satisficing is second-hand only.
- No human-subject data on quality over time (time-pressure or speed-accuracy studies).
- I re-checked 8 papers (about 25 numbers), not the Zilberstein or Dean-Boddy PDFs; their numbers (factor 4, Theorem 5) stand as recorded by agent A.

## GAPS
1. Does stopping on agreement of independent trial answers or a real check beat model self-confidence stopping (DEER) at equal tokens, outside math?
2. Do quality-vs-token curves on agent tasks (code, multi-step) show plateaus and late jumps that break myopic stopping? Any measured concavity test?
3. Parallel k attempts vs one long trace at equal tokens: where is the crossover by difficulty and model, and why do Ghosal and s1 disagree?
4. Does a doubling-budget schedule (factor-4 reduction) work for LLMs, and what is its real waste vs knowing the budget?
5. How should a staged scaffold split a fixed token budget across stages (fixed shares, greedy marginal gain, learned profile)? Any empirical study?
6. Can a cheap difficulty probe predict per-item budget well enough to realise Snell's 4x saving outside MATH and PaLM 2?
7. What does reserving a final-answer segment (E1-style) do on non-trained models when the trace is cut?
8. Has Hansen and Zilberstein 2001 non-myopic monitoring been applied to LLM reasoning, and does it beat threshold rules?
9. Human evidence: how does accuracy vary with allowed time in expert and novice decisions, and does satisficing with aspiration adjustment match anytime stopping?
10. Do the AnytimeReasoner and s1 gains replicate across seeds with confidence intervals and test sets larger than 30 items?

## Gap search results (evidence_d.jsonl, d01-d20)
Search limits: WebSearch quota ran out after one call and arXiv API, Semantic Scholar and OpenAlex returned HTTP 429, so papers were found from memory of arXiv ids and opened as PDFs. Coverage is therefore narrower than a full search. Twelve PDFs were read in full or in the relevant sections; Heitz 2014 was read through a page-reading tool; Chabris and Hearst through the saved PDF.

1. Agreement or real-check stopping vs self-confidence (PARTLY CLOSED). Agreement stopping is well supported: Adaptive-Consistency (2.4-3.8x fewer samples, accuracy within 0.2, code +0.4), ESC (-34% to -84% samples, MBPP -23% at no loss), DeepConf consensus stop (-52.8% tokens at K=512, same accuracy) (d01-d03, new claim K23). No paper compares agreement stopping with DEER-style self-confidence at equal tokens; this stays open (K24). Non-math evidence is only MBPP, code in Adaptive-Consistency and GPQA-D.
2. Plateaus and late jumps on agent tasks (PARTLY CLOSED). S* shows coverage plateau past N=32 (QwQ-32B-Preview); R2E-Gym shows verifier-selected plateaus at 42-44% then 51% with a hybrid signal; MRT shows later episodes can lower accuracy. No paper runs a concavity test on agent tasks; MRT's cumulative regret is the closest metric (K26).
3. Parallel vs sequential crossover (PARTLY CLOSED, still contested for trained models). Zeng 2025 shows Wait extension on untuned QwQ/R1/LIMO flips correct to wrong more than the reverse; Balachandran shows sequential wins only when the critic is informative (TSP-easy), parallel on AIME; Hassid shows parallel with early halting saves up to 40% tokens. Likely reason for the Ghosal vs s1 split: s1's model was fine-tuned for continuation. Not tested directly (K12, K28).
4. Doubling schedule for LLMs (OPEN). No LLM study found. Own arithmetic only: a doubling schedule with banked best-by-check answer spends at most about 2x the final attempt's budget plus earlier ones, so the factor-4 bound is a worst case; the real waste is unmeasured (K31).
5. Splitting a budget across stages (PARTLY CLOSED). Plan and Budget (ICLR 2026): per-stage budgets beat a global cap (E3 +14% to +33%); schedule shape matters little. R2E-Gym: 5 extra test-writing rollouts gave +1.7 points vs +0.8 for 5 extra editing rollouts. No greedy-marginal-gain or learned-profile comparison (K27).
6. Cheap difficulty probe (CONTESTED). Certaindex stability correlates r=0.52 with steps-to-solution and saves 9-52% tokens, but Plan and Budget's run of the Certaindex baseline lost 8 points on MATH-500. Learned predictors (SelfBudgeter, OSCA) need training or a calibration set. Snell's 4x not reproduced elsewhere (K30).
7. Reserving a final-answer segment on untrained models (PARTLY CLOSED). Interruptible-LRM paper: on Qwen3-8B, GPT-OSS-20B, Magistral, hard cuts show anytime behaviour but answers leak reasoning (up to 10x longer), and panic under speed-up causes over 90% of new errors. Lanham: truncated chains show task-specific flatness. No test of a reserved-segment rule on untrained models (K16 updated).
8. Hansen-Zilberstein monitoring on LLMs (OPEN). Not found. Nearest: Certaindex per-step curve fitting saves only 1-3.4% tokens beyond a static threshold; MRT optimises regret by training (K31).
9. Human evidence (MOSTLY OPEN). Heitz 2014 gives the saturating SAT form (simulation numbers only). Chabris and Hearst 2003: 23 grandmasters, 1,188 games, blunders per 1,000 moves 5.02 classical vs 6.85 rapid (+36.5%) vs 7.63 blindfold. No expert-vs-novice time-limit data and no test of aspiration adjustment against anytime stopping were reachable (K32).
10. Replication with seeds and larger sets (PARTLY CLOSED). Hochlehnert 2025: seed SD 5-15 points on 30-item sets, about 30 seeds needed, most RL gains not significant under paired tests, s1.1-7B included only as a model. AnytimeReasoner and s1 budget forcing were not directly replicated by anyone found (K29). Their reported gains stay single-run and should be treated as unconfirmed.

Corrections noted: the Certaindex claim is contested between the original authors and one reproduction; DeepConf uses log-prob confidence, not verbalised confidence, so it does not answer the DEER comparison.
