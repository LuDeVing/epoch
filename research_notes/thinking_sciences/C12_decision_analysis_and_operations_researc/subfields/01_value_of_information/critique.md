# Cross-check critique: C12.01 Value of information

Checker session 2026-10-26. Sources re-opened (full text, not abstracts): Hu 2024 UoT (2402.03271), Laban 2025 (2505.06120), Grand 2024 LIPS (2402.19471), Kobalczyk 2025 (2502.04485), Hay 2012 (1207.5879), Dong 2026 (2601.06407, HTML), Park 2026 SAG (2610.07335, HTML). Abstract records only: Chhikara 2026, Amin 2026, BED-LLM. Wikipedia EVPI example recomputed by hand.

## Corrections made (headline numbers checked)
1. EVPI example (a02): recomputed. Stock 680, fund 590, CD 500; EV|PI 1030; EVPI 350. Confirmed.
2. UoT +38.1 percent, +46.6 for Llama3-70B, beats CoT-SC by 33.8, Reflexion 29.9, Orig-ToT 28.3, Adapted-ToT 12.4 (a19, c07): confirmed in the paper text.
3. UoT token table (a21 vs c08): a21 said pruned UoT used about 4.5k tokens. The paper says 4.7k (Orig-ToT and Adapted-ToT 4.5k, CoT-SC 4.6k). c08 is right; correct a21. The matched comparison at 9.3k (Adapted-ToT D=4) versus 9.2k (UoT D=3) is confirmed.
4. Laban: -39 percent, 15 LLMs, 200,000+ conversations, N=10 per cell (a31): confirmed.
5. Battleship (a22, c23): human mean EIG 1.27, best 3.61, 97 percent informative, N=40 people, 605 question-board pairs, LLM samples 0.65-0.66, p<0.001 and p=0.01: confirmed. The extracted results table is column-misaligned (the Grammar row shows 1.27), so the grammar baseline 0.36 could not be tied to a clean cell; treat as probable. The table also shows GPT-4 zero-shot at 0.77, above few-shot 0.65, which the evidence files do not mention.
6. Kobalczyk (a27, a28, b18): GPT-3.5 HumanEval round 4 binary 70.8 vs 85.6, open 75.9 vs 85.0 and GPT-4o-mini binary 79.6 vs 81.5, open 83.5 vs 83.8 confirmed. Correction: the cell 64.8 vs 75.5 sits in the second (APPS) table, not HumanEval. b18 labels it HumanEval, so that label is wrong. Standard errors there are about 2.0.
7. Dong 2026 (c02, c03): 18 of 20 conditions, up to 1.36, 14.14 vs 11.49 at tau=0.9 and c=0.01: confirmed. The 1.36 is 5.01 vs 3.65 at c=0.05 in one table. Utility, not accuracy.
8. SAG (c15, c16): the full text gives ALFWorld 78.3 percent (an abstract version says 78.4; use 78.3). 74.2 at 341k tokens, 30.2 at 57k (both with online SFT), no-critic 33.0, no entropy 77.6, no margin 74.6, critic calls 2.85 to 1.10 while success 71.0 to 83.0: confirmed. New detail: an "always (no gating)" variant scored 62.0 at 282k tokens, so always-on critique can be worse than gated, not only costlier.
9. Hay 2012 (a08-a11): Theorem 5 (E[N] <= EVPI/c), Theorem 7 (myopic continues implies optimal continues), Theorem 10 bound 1/(4c) - 3, and 64 percent win rate at 10000 samples per ply: confirmed.
10. Amin 2026 (c17): abstract confirms 294,000 USD, 34 percent, gap 22 to 5, shares 51, 43, 20. The abstract says "ablations attribute", so the shares probably overlap and need not sum to 100. Still a single-author preprint on one task.
11. Chhikara 2026 (c18): real title is "Evaluating Confidence-Gated Retrieval with Matched Trajectory Replay"; abstract confirms +41 committed accuracy, +15 and -17 overall. The author name in c18 was not checked.

Not re-opened (rest on earlier agents only): KnowNo 10-24 percent (PDF did not parse), MediQ, BED-LLM numbers, QuestBench tables, De Sabbata row pair, Adaptive-Consistency, ESC, DeLLMa, STaR-GATE, all health-economics items.

## Contradictions and tensions
- Information gain versus probability gain: Nelson 2010 (b09) found humans follow probability gain; every LLM paper uses information gain. No LLM study compares them.
- Stronger model, smaller gain (a28) sits beside large UoT gains on GPT-4 (a19). Probably closed versus open sets and dataset, but no single study tests it.
- Kobalczyk: log-probability weighting hurt, uniform weighting helped (b19); BED-LLM relies on the LLM's own predictive distribution (b16). Different estimators; not reconciled.
- MediQ: free asking hurts (b22), yet UoT and Kobalczyk show asking helps. The difference is a structured selector or gate versus ungated prompting. Nobody ran all arms together.
- Most models are 2023-2024 vintage. QuestBench-type failures may be weaker with 2026 reasoning models.

## Weak spots
- No study measures true EVPI or payoff-based VoI on an LLM at equal tokens against EIG. Most "VoI" results are information gain. Only Dong 2026 and SAG use cost or payoff, and SAG uses a proxy.
- Simulated answerers (GPT-4 in UoT, LLM oracles in Kobalczyk) may flatter results. UoT checked 10 percent of answers and used 3 repeats.
- Howard 1966 and Raiffa-Schlaifer 1961 were never opened; founding numbers are second-hand (a06, c26).
- Many results come from 20 Questions style tasks with closed hypothesis sets and from overlapping research groups.
- Duplicated evidence: a19/b14/c07 are one paper; a22/a23/b24/c23 one paper; a24/b31/c20 one paper; a17/b25 one paper. Independent-source counts in claims.jsonl collapse these.
- Several numbers came from garbled tables (De Sabbata row pair, LIPS grammar row, BED-LLM ablation columns).
- No test of any VoI rule inside a scaffold with a token budget. Agent claims are inference.

## GAPS
1. Does a payoff-based gate (EVPI cap plus net value minus cost) beat an information-gain-only ranker and a tuned confidence threshold at equal tokens, on closed-hypothesis tasks and on open tasks? No paper compares all three.
2. How much of the EIG gain survives with 2025-2026 reasoning models that already ask well (QuestBench-style and clarification tasks)?
3. When the hypothesis set is open (no explicit candidate list), how should an agent build one cheaply, and how wrong can it be before EIG ranking turns harmful?
4. How can an agent estimate the payoff table and prior for EVPI in free-form tasks (coding, ARC-style puzzles)? Is any LLM-elicited EVPI predictive of the realized gain from one more test?
5. Information gain versus probability gain versus impact: which predicts realized test value in LLM tasks? Humans favour probability gain.
6. Non-myopic selection: how much does a 2-3 test lookahead beat one-step scoring in LLM settings, and what does the lookahead cost in tokens?
7. Does stated or sampled-agreement uncertainty predict, item by item, which cases benefit from another test or check? Chhikara says calibration does not; SAG proxies work on ALFWorld.
8. What is the best stopping rule for a run of noisy tests (Adaptive-Consistency style versus an EVPI/c cap), and what hard cap prevents the unbounded-run case?
9. What do Howard 1966 and Raiffa-Schlaifer 1961 actually prove about nonadditivity and the risk-averse case, and does risk-averse breakdown matter for an agent?

## Gap search results

Gap searcher session 2026-10-27. Web search quota was exhausted and arXiv/OpenAlex/Semantic Scholar APIs returned 429, so papers were found through arXiv listing pages and opened through page fetches and local PDF text. Evidence is in evidence_d.jsonl (d01-d25). Claims K27-K34 are new; K03, K04, K08, K09, K14, K15 were changed (K15 now contested). Several fetched pages covered only the first 100,000 characters, noted in each line's limits.

1. Payoff gate vs information-gain ranker vs tuned threshold at equal tokens: STAYED OPEN. Partial evidence only. A simulation (d01) shows cost-aware selection plus net-value stop beats a tuned entropy threshold by 33 points and that stopping alone recovers at most 4. A real-LLM run of the same stop rule with a sampled-agreement proxy earned less than always retrieving (d02, U 2.20 vs 5.33). A value-per-budget scorer beat four baselines in most cells under hard caps (d03, d04), and its largest ablation effect was the cost term. No paper runs all three arms.
2. How much EIG gain survives with reasoning models: PARTLY CLOSED. Gains shrink with model strength (d06: x2 on 7B, +1.8 to +4.2 on 14B; d09: +2.3 on GPT-5.1 vs +7.8 on R1). Reasoning-on did not help the base questioner (d07). A DeepSeek-R1 agent still gained +4.3 from a trained clarifier (d05). QuestBench has no scored model after o1-preview (d20). Still open: any 2026 frontier reasoning model on QuestBench-type tasks.
3. Open hypothesis sets: PARTLY CLOSED. A working recipe exists for nameable entities (d10, d11). A capped, grow-on-failed-fit pool is used for model discovery (d12). Still open: how often the true answer is missing and how wrong the set can be before EIG ranking hurts. Nobody measured it.
4. Payoff table and prior in free-form tasks: STAYED OPEN. LLM utilities agree with humans 65-70% (d19) and the scaffold beat o1-preview, but no study checks whether an elicited EVPI predicts realized gain. The only proxy test failed on confident wrong answers (d02).
5. Information gain vs probability gain vs impact: STAYED OPEN for LLMs. Humans favour probability gain (d22). In LLM work the cheap halving rule recovers much of the EIG gain with a candidate set (d10), but that is not a probability-gain test.
6. Non-myopic lookahead: PARTLY CLOSED. Huge gain in a constructed combination test (75.0 vs 30.2), small in a natural task (32.7 vs 29.7), depth-2 tree +21.8 points (d07, d08). No natural-task depth ablation and no token price. New claim K27, single-source.
7. Does stated or sampled uncertainty predict item-level benefit of another test: CLOSED AS CONTESTED. Confidence-weighted agreement stops earlier at equal accuracy (d17); calibration does not give the benefit of a new retrieval (d24); agreement missed all confident errors (d02). K15 is now contested.
8. Best stopping rule and hard cap: PARTLY CLOSED. Agreement-based and anytime-valid rules exist with measured savings (d14-d18, K29) and an interior optimum for question counts (d05). None is compared to an EVPI/c cap. Savings are smallest on hard items.
9. Howard 1966 and Raiffa-Schlaifer 1961: STAYED OPEN. Neither source could be opened (IEEE page empty; APIs rate-limited). Only secondary statements on nonadditivity and the risk-averse caveat (d25). K34 records this.

New tensions: UoT results swing 60.4 to 90.1 on 20 Questions with two hyper-parameters (d08), so tuned baselines decide who wins; BED-LLM reimplemented by others fell below baseline on one cell (d06) while the original paper reports large gains (d10), so reimplementation risk is real.
