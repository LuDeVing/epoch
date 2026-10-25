# Critique: adaptive stopping and metareasoning (cross-check)

Claims are in claims.jsonl (K01-K17). Sources re-opened this session (full text): Adaptive-Consistency (2305.11860), ESC (2401.10480), RaM (2410.05563), CISC (2502.06233), Snell et al. (2408.03314), L1 (2503.04697), DeepConf (arXiv HTML 2508.15260v1), s1 (arXiv HTML 2501.19393v3).

## Corrections made

1. RaM model label (a13 vs c10). Table 1 text extraction shows the 50.1% / 170.8 tokens block with row labels "Llama-3.2-3B, Llama-3.2-3B-Instruct, Llama-3.1-8B" stacked around it, so the block cannot be assigned to one model. a13 says Llama-3.1-8B; c10 says Llama-3.2-3B. Neither is safe. Confirmed numbers: 50.1 vs STaR 47.4 vs CoT few-shot 34.8 (tokens 170.8 / 222.7 / 261.9); Llama-3.1-8B-Instruct 63.5 / 61.9 / 56.4 (tokens 146.2 / 215.1 / 253.6). a13 also printed "34.8" as few-shot CoT for the instruct model in its first line; the instruct value is 56.4. Also: accuracy is "rescaled accuracy averaged across datasets", with greedy decoding and 95% intervals of about plus or minus 1.7, so RaM vs STaR accuracy gains (1.6 to 2.7 points) are inside overlapping intervals. Only the token cut is clearly real.
2. DeepConf savings range (a26, b08 say 43-79%; c18, c30 say 43-84%). The paper table shows GPT-OSS-120B AIME25 at -84.7% (97.9% accuracy) and AIME24 -79.9%. The range for the low threshold at B=512 is 43-85%, not 43-79%. a26 and b08 are wrong at the top end.
3. DeepConf headline mixing. 99.9% (DeepConf@512, offline voting, AIME25 GPT-OSS-120B) and 84.7% fewer tokens (online, low threshold, accuracy 97.9%) are different modes. The abstract joins them in one sentence. Full parallel thinking in the online table is 97.1%, majority vote cons@512 is 97.0%. c18's text "99.9 vs 97.0 and up to 84.7% fewer tokens" is accurate only if read as two settings.
4. ESC GPT-4 MATH (a18): confirmed. SC 60.32, ESC 59.98 (-0.34), mean 42.40 of 64 samples. But the table rows are shifted in the text extraction and the model labelled "GPT-4" sits above the row set; a18's reading is consistent with the L=16/40/64 sample counts (13.56 / 28.49 / 42.41), so it stands.
5. Adaptive-Consistency (a16/b01/c02): abstract (7.9x max, "no loss") and averages (math 40 to 13.8 samples) confirmed. a16 gives accuracy deltas as small; some rows in the appendix show AC higher than SC, others lower by up to 0.2 on average. No correction needed. Note: c01 says "accuracy drop under 0.1 point on average"; the per-category deltas are 0.1 (math), 0.2 (commonsense). Say "0.1-0.2".
6. CISC (b06): confirmed. P(True) 46% (SC needs 18.6 samples to match CISC at 10), response probability 31% (14.6), 'verbal binary 10%' not re-read. a20 said "verbal 1-100 30%"; b06 says 0-100. Scale label unresolved, number agrees.
7. Snell: "4x less" is "up to 4x", and the 14x comparison is FLOPs-matched and conditional on inference load. Confirmed. The wording in a22 is ok; do not quote 4x as typical.
8. L1: slope 0.24 vs 0.37 and 100-150% relative / 20-25% absolute confirmed from the paper text.
9. s1: Table 3 confirmed (budget forcing control 100%, scaling 15, AIME24 56.7; token-conditional 40% control, 40.0; step-conditional 60%, 36.7; class-conditional 50%, 36.7; rejection sampling 100% control, scaling -35). b14's "token-conditional 40%" fine. Added limit: AIME24 has 30 problems; 50.0 to 56.7 is two problems. Table 3 shows 50.0 to 56.7 is the SAME benchmark that tuned the method.

## Contradictions between sources

- Length and quality. s1 says more forced thinking helps (+6.7 points, 30 items). Zeng et al., Su et al. and Chen et al. say longer chains are worse within a question and extra revisions rarely fix errors. These are compatible only if forcing helps when the model stopped too early and hurts when it has already answered; no paper tests that split. Treat both as conditional.
- Sequential vs parallel. s1 and Snell favor sequential (revisions) at low difficulty; Zeng et al. favor parallel for R1/QwQ. Different base models (fine-tuned revision model vs distilled reasoners). Not reconciled.
- Savings differ by difficulty, so quoted percentages are not comparable across papers: ESC -80% on GSM8K and -34% on MATH; ReASC accepts 49-61% of GSM8K items but 7% of MATH500 for the 3B model.
- RaM reports "accuracy equal or up" while the out-of-domain table shows an accuracy loss for the 8B model (36.4 vs 40.2 for STaR, from c11). The abstract says "maintaining or improving".

## Weak spots

- Almost all stopping results are on maths (GSM8K, MATH, AIME) and short commonsense QA with an auto-checkable answer. Open-ended reasoning and agent tasks have no answer to vote over, so agreement-based stopping does not transfer. Only CaRT touches agent dialogue, and only its recipe was read.
- Every comparison of stop rules is run by the authors of the newest rule (DSC, ReASC, DeepConf). No independent head-to-head found. K03 stays single-source.
- Agreement fails when errors are correlated. No paper measures how often all samples agree on a wrong answer and the stop fires. This is the main failure mode of the best-supported stop rule and it is untested.
- Cost accounting is partial. DSC notes input tokens (846 per question) exceed output tokens (164); sample counts hide the prompt cost. Most papers report samples, not total tokens or dollars.
- Savings are measured against 40 or 64 samples, which is a weak baseline. Against a fixed 5 to 10 samples (the original SC paper says 5-10 captures most of the gain), the savings shrink to a small factor. ESC at w=5 on GSM8K averages near 8 samples, not 40.
- Cross-experiment budgets differ: tokens (s1, L1), samples (AC, ESC, CISC), FLOPs (Snell).
- Rational metareasoning theory (Russell and Wefald, Hay et al.) is for independent computations with known cost; LLM reasoning steps are not independent and the value of a step is unobserved. No paper shows the stop rule from theory outperforming a heuristic on LLM reasoning in an LLM-agent setting; RaM is the only bridge and it trains weights.
- Human studies (Lieder and Griffiths) use MTurk workers on sorting and gambles; they support the framework but not any specific stop threshold for LLMs.

## Seen only in snippets or not opened

- Russell and Wefald (1991) book: not opened (a29, b20, c20). Only second-hand via Russell (1997) and Hay et al.
- Callaway et al. (2018) learning to select computations (a11): abstract only.
- Wang et al. (2022) Self-Consistency original (b05, c28): not opened; a15 numbers are from a separate read and should be checked.
- CaRT (b24 not opened; a28 and c19 opened but recipe-level; exact success rates not recorded).
- ESC appendix table 7 (AC vs ESC cost): exact cells not recorded (c05).
- Hay et al. figure values (a05): not extracted.
- Certaindex (c27): exact values not recorded.
- Items from the "10 checked" list not re-opened this session: Wang et al. DSC, Kim et al. ReASC, Chen et al. overthinking, Su et al., Zeng et al., Brown et al., Gema et al., RouteLLM. These stay at the earlier agents' reading.

## GAPS

1. Does vote-stability stopping fire on wrong consensus? What share of "stopped early" items have all samples agreeing on a wrong answer, on items where the model is overconfident (include non-maths)?
2. What stop signal works when there is no vote, i.e. for free-text reasoning and agent loops? Only CaRT-style trained stoppers were found; is there a prompt-only rule that beats a fixed turn cap?
3. How cheaply can difficulty be estimated before spending the budget (Snell uses 2048 samples per question to define bins, which is not deployable)? What is the pass-rate estimate error with 2-4 samples, and does routing on it keep the 4x saving?
4. Does forcing a re-check (Wait) help only when the first answer was wrong or premature? A paired test splitting items by first-answer correctness would reconcile s1 with Zeng and Su.
5. What is the total-token (input plus output) saving of ESC/AC/DeepConf vs a fixed 5-10 sample baseline rather than vs 40 or 512? The headline factors may shrink a lot.
6. Does the myopic value-of-computation rule from Russell and Wefald (expected change of leading answer vs cost) beat window-based stopping at equal tokens on an LLM? No test found.
7. Do small models and big models stop at different points (ReASC finds 7% acceptance on MATH500 3B vs 61% on 27B)? Should the stop threshold be conditioned on model strength?
8. Is there an independent replication of DeepConf, DSC or ReASC by someone other than the authors, and on non-maths tasks?
9. What do routing methods (RouteLLM: 95% of GPT-4 quality at 50% of calls) give when the cheaper path is a shorter think rather than a smaller model, and can one router handle both?
10. How does the stop rule interact with a verifier? When a checker exists, is stop-on-pass strictly better than stop-on-agreement, and by how much (the pass@k vs majority gap in Brown et al. suggests large)?


## Gap search results

Evidence is in evidence_d.jsonl (d01-d21). New claims C01.08-K18 to K27; K01, K02, K03, K06, K07, K09, K10, K11, K16, K17 got extra evidence ids; K01 got a caveat on the baseline. Web search quota ran out, and Semantic Scholar and OpenAlex rate-limited, so forward-citation checks (gap 8) could not be run. Two lines (d12, d13) are my own simulations and are marked type "model", opened:false. Lines d06 and d14 were read through a page-extraction tool, not the PDF.

Status per gap:

1. Wrong consensus under vote stopping: PARTLY CLOSED, still open for vote rules. No paper counts unanimous-wrong stops. Direct data exists only for confidence gates (ReASC, d07): 1.4-8.7% of accepted GSM8K items and 2.7-13.9% of MATH500 items are wrong. Brown et al. (d04) show many problems where the majority answer is wrong and the right answer is rare, and Kim et al. (d06) show models share wrong answers (60% on HELM). My simulation (d13) says the wrong share of 4-unanimous stops runs from under 1% to over 50% depending on how concentrated the wrong answers are. Adaptive-Consistency compares only with SC-40 (d01), so it cannot see this error. Non-maths and overconfident items: nothing found. Claim K18, contested.
2. Stop signal with no vote: CLOSED for a prompt-only baseline, open for a rule that beats a good turn policy. A visible remaining-budget counter beat a hidden cap on BrowseComp, SWE-bench Verified and a conversational set (d17), single paper and the gains on the main table are small against noise. Stopping at the agent's own first verified answer lost 6-8 points (d18). Trained stoppers: probe 24% fewer tokens at equal accuracy but poor transfer (d16), self-calibration (d21). K22, single-source.
3. Cheap difficulty estimate: MOSTLY CLOSED. My simulation (d12): 4 samples give 79-87% easy/hard split accuracy, about the level of a learned probe (72-84%, d10); five-way bins need about 16 samples. Damani (d10) show probe errors can push online allocation below fixed best-of-k at high budget. Whether coarse routing keeps Snell's 4x: not measured. K20, contested.
4. Forced re-check by first-answer correctness: PARTLY CLOSED. Over 90% of reflections are confirmatory, wrong-to-right under 2%, first-candidate accuracy within 1.4-3.5 points of final (d14). That reconciles s1 and Zeng: reflection pays little and mostly on the few items where the first answer was wrong. Prompted self-correction without a label flips right answers to wrong ones (d15). The right-to-wrong rate for forced "Wait" was in a figure and not retrieved; no paired test exactly as asked. K21, established for the aggregate claim.
5. Total tokens against a small baseline: CLOSED in direction, open in size for ESC on reasoning models. Against k=16 the ESC saving is 4-71% (d08). With prompt re-sent each round, ASC +74% and ESC +3% against SC-40 on Mistral-7B GSM8K (d09). A DeepConf total-token figure vs 5-10 samples was not found. K19, established.
6. Myopic VOC rule vs window: STAYS OPEN. Nearest evidence is that Bayesian stability beats raw vote share (d03). No test with a cost term. K26.
7. Stop threshold by model strength: PARTLY CLOSED. Agreement rules adapt by themselves (4.4x vs 1.9x, d02). Confidence gates do not: acceptance 7% to 37% on MATH500 and 49% to 61% on GSM8K across sizes (d07). Calibrate per model. K24.
8. Independent replication: STAYS OPEN. Only the DeepConf bottom-10% signal was reused (AUROC 0.860 vs 0.801, d20). Nothing found for the DeepConf online stop, DSC or non-maths tasks; citation lookups were blocked, so absence is unproven. K27.
9. Routing with think depth: PARTLY CLOSED. One router handled model and strategy together, including think/no-think: Qwen3-4B 83.8% at 1,321 tokens vs 82.4% at 3,113 always-think (d19). Damani routed between decoders (d10). Authors' own baselines, maths-heavy. K25.
10. Verifier pass vs agreement: PARTLY CLOSED. Ceiling is large (98.44% coverage vs 41.41% majority, d04). Checkers leak (d05) and a model's own verification as a stop lost 6-8 points (d18). No head-to-head of stop-on-pass vs stop-on-agreement at equal tokens. K23.

New corrections and cautions from this pass:
- The 2x-5x and 80% savings figures in K01/K02 are against 40 samples. Against 16 samples and counting prompt tokens they can drop to near zero on hard sets.
- ReASC's "7.2% acceptance" (Llama-3.2-3B, MATH500) is the offline gate with accepted accuracy 86.11%; the online gate accepts 17.6%.
- In d11 the paper says the reward model as stop signal is no better than random selection; the adaptive 1.2-sample result is with annealing and a trained self-evaluation head.

Still open after this pass: gaps 1 (for vote rules), 4 (forced Wait paired flips), 6, 8; and the sizing of 3 and 10 on a reasoning model with a real tool-checker.
