# Cross-check critique: Sampling and voting (C01.02)

## Corrections made (10 numbers re-opened in the arXiv PDFs this session)
Confirmed against full text: Wang et al. Table 2/3 (PaLM GSM8K 56.5 -> 74.4, AQuA 35.8 -> 48.3, SVAMP 79.0 -> 86.6, LaMDA GSM8K 17.1 -> 27.7, UL2 GSM8K 4.1 -> 7.3, UL2 Letter 0.0 -> 0.0, PaLM Letter 65.8 -> 70.8, UL2 AQuA beam 23.6 -> 10.2); Brown et al. (82.9 -> 98.44 coverage, 40.50 -> 41.41 vote, 15.9 -> 56%, SOTA 43%); DeepSeek-R1 distill table (1.5B 28.9 -> 52.7, 7B 55.5 -> 83.3, 14B 69.7 -> 80.0, 32B 72.6 -> 83.3, Llama-8B 50.4 -> 80.0, GPT-4o 9.3 -> 13.4, Claude-3.5 16.0 -> 26.7, R1 79.8 -> 86.7); Lightman (PRM 78.2, ORM 72.4, majority 69.6, best-of-1860); Chen et al. scaling (53% easy / 47% hard; wrong answer 56% vs correct 34%); More Agents (13B 59% vs 70B 54%); Snell (4x, 14x).

Errors found and fixed (in claims, not in the jsonl files):
1. b14 and a13 mislabel USC code numbers. In Chen et al. USC, ARCADE (gpt-3.5) is greedy 26.0, random 26.8, SC-Exec strict 29.8, fuzzy 30.3, USC 30.1. BIRD-SQL is greedy 42.4, SC-Exec 45.6, USC 45.5. b14 says "ARCADE greedy 42.4, SC-Exec 45.6, USC 45.5" (those are BIRD) and a13 says "ARCADE SC-Exec 45.6 vs USC 45.5". c22 has it right. Use c22.
2. a03/b02 say ARC-c, StrategyQA etc. correct; but a03 lists PaLM Letter gain only as 65.8 -> 70.8 (+5.0), fine. No change.
3. Not re-opened (still from the evidence files only): Adaptive-Consistency per-model figures (GPT-3.5 4.4x, Vicuna 1.9x) and per-task ratios (the 7.9x, under 0.1% headline text was confirmed); Soft-SC, CISC, ESC, TTRL, Correlated Errors, Hivemind, Inference scaling fLaws, MAD numbers; Snell revision 38%.

## Contradictions and weak spots
- Prompt diversity: DiVeRSe (+3.3 from 5 prompts x 20 samples) vs Wang (40 permutations 19.2 loses to 40 samples 27.7 on LaMDA) vs Fu (complex voting +0.3 to +1.1). Different models and prompt sets, so no clear winner. Marked contested.
- Parallel vs sequential: Snell finds the best mix depends on difficulty; revision hurt 38% of correct answers. Different from vote-only studies.
- USC: improves with 8 samples on some sets but GSM8K fell at 16 samples. Context length, not the idea, may be the limit.
- Brown et al. say vote plateaus; R1 and TTRL show vote still strong on reasoning models. Not a contradiction: Brown used a weak 8B chat model, R1 a long-reasoning model, and AIME has only 30 problems.
- Early work (Wang, Cobbe, Fu, DiVeRSe) uses 2021-22 models; code-davinci-002 is gone. Modern frontier-model numbers at equal tokens are thin. Most reasoning-model vote results rest on AIME (30 items, so one item = 3.3 points).
- Independence: the Condorcet base needs independent voters. Kim et al. correlated-errors is about different models, not repeated samples, so it only supports the direction.
- Token cost: almost no study reports vote at equal total tokens against one long reasoning pass or best-of-n with a verifier; most compare per sample count.
- Exact-match limits: all headline results need a short extractable answer. Free-form uses USC, which adds bias of the selector.
- Only snippets/abstract-level: evidence marked opened:true in the files is trusted except where listed in item 3 above.

## GAPS
1. At equal total tokens, does k short CoT samples with a vote beat one long thinking pass (or one pass plus self-check) on current frontier models? No study found measures this cleanly.
2. Is vote share a calibrated stop/escalate signal for modern models (accuracy by vote-share bin), and what threshold separates "trust the vote" from "send to verifier or search"?
3. For tasks without a runnable check (our hard cases), what is the best code-side selector: plain vote, confidence-weighted (CISC), USC, or a separate verifier call, at equal tokens?
4. How correlated are repeated samples from one model on wrong answers, and which diversity levers (temperature, persona, prompt rewrite, different model) most reduce that correlation?
5. How many samples are enough with adaptive stopping on hard items, where early stopping saves least (MATH -33.8%)?
6. Does vote help on tasks with open or multi-step answers (planning, agents, open-ended writing) beyond Soft-SC on WebShop/Bash/ALFWorld? Artificial Hivemind suggests the vote rewards the mode.
7. Does voting still add value after a strong verifier or PRM exists (Lightman: RM-weighted voting added little)? What is the best hybrid?
8. Do the 2024-25 gains (R1 distills, TTRL) replicate on non-math reasoning (law, biology, causal tasks) with held-out items beyond 30-problem AIME?
9. What does a failed vote look like (wrong plurality) and can a cheap detector (low share, high entropy over answers) catch it before the answer is released?


## Gap search results (evidence_d.jsonl d01-d18, claims K21-K28 added, K03/K06/K09/K10/K11/K16/K19 revised)
Search note: the WebSearch budget ran out partway through; Semantic Scholar and OpenAlex returned HTTP 429. I read 18 papers in full or in the relevant sections from arXiv PDFs. Gaps 6 and 8 therefore stay open for lack of a search, not for lack of an answer in the literature.

1. Equal tokens, k short samples vote vs one long pass: STAYED OPEN. No paper makes this exact test. Closest: Sharma and Chopra (d01) find sequential refinement beats parallel vote 43/45 at 4096-token chains (Qwen3-235B AIME-2025 76.7 vs 30.0), but the parallel arm is capped at 4096 tokens per chain and no truncation rate is reported, so it may be a cap artefact. Mirzaei (d02) finds the reverse for 1.5B-7B models (vote never reliably beaten at equal measured tokens). Iacobacci (d03) is 30 items. New claim K22 (single-source); K19 stays contested.
2. Vote share as a stop/escalate signal: MOSTLY CLOSED. Usable but weak: Spearman 0.20-0.59 (d05), AUROC 0.836 and ECE 0.090 (d07), conformal threshold on 200 labelled items gives 90.1% vs 82% selective accuracy on GSM8K (d06). Threshold depends on model and task; no universal number. Frontier gpt-4.1 had 48% wrong at C>=0.8 on GPQA. K16 narrowed, K23 added. Still open: a threshold that transfers across tasks.
3. Best selector without a runnable check: PARTLY CLOSED. Plain vote won at N=5 on short-answer math (85.42 vs judges 81.25-82.92, reward models about 80, d08); list-wise judge won on GAIA agent trajectories (63.03 vs vote 56.8, d16); confidence weighting helps in author tests but reverses on over-confident models (d12). Answer: choose by whether answers match exactly. K24 contested.
4. Correlation of wrong answers and diversity levers: PARTLY CLOSED. For short-answer math at T=1.0 prompt diversity is redundant (d09) and independent draws show no cross-question structure (d10); shared seeds, shared few-shot blocks and option-letter bias create fake agreement. Caveat: the near-zero correlation estimate is conditional on each problem's own hit rate, so it does not rule out the real failure (items with chance under 50%). Different-model diversity was not retested. K09 contested, K10 updated, K25 added.
5. Adaptive stopping on hard items: CLOSED enough. At budget 16 the hardest sets save least: ESC 12.88 calls on GPQA and 10.68 on AIME24 vs 5.16 on GSM8K; CGES 11.90 and 7.77 vs 2.41 (d11). Bo-infinity needs about 80 samples (d08). K04 updated, K03 now contested because hard reasoning-model items keep gaining to 512 samples (d12).
6. Open-ended and agent tasks: PARTLY OPEN. One agent study (d16) shows vote is weakest of three merge methods; self-certainty claims for open-ended generation are author-reported only (d15). No study of open-ended writing quality with vote found. K28 added (single-source).
7. Vote after a strong verifier: CLOSED for trained verifiers. Weighted voting beats plain majority at N>=8 (d14) and pessimistic verification reaches 83.3% vs about 70% for vote (d13); voting survives as the grouping term. For off-the-shelf judges and reward models at N=5, vote wins (d08). K11 contested with this split, K26 added.
8. Non-math, held-out generalisation: STAYED OPEN. Only GPQA and MMLU-Pro numbers (d18, d11); smaller gain than math; medical thinking-budget study did not test vote (d17). No law, biology or causal-task voting study opened. K27 single-source.
9. Detecting a failed vote: PARTLY CLOSED. Low vote share plus a calibrated threshold is the best cheap detector (d06, d07), but it fails where the wrong answer is the confident mode (d05: 48% wrong at C>=0.8; d12: over-confident traces). A second-stage check on the top distinct answers (d13) is the fallback. Open: a detector that works for unanimous-but-wrong cases.

New caveats: nearly all new evidence is 2025-2026 preprints on 30-item AIME sets or 150-item sets, and several use small open models. Treat any single number as a lead to test on our own items.
