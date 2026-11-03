# Critique: B02.09 Pruning of decision trees (cross-check)

## Numbers re-opened this session (10 checked against source text)
1. Lally 2017 (PMC5647774): 78% vs 37%, t(36)=12.51, d=2.06 confirmed. Table 2 iBIC 3052 / 2549 / 2472 / 2466 and variance 41.7 / 52.5 / 54.4 / 55.3% confirmed. SGC t(36)=3.87, pSVC=0.004 confirmed. State anxiety t(37)=2.12, p=0.042 confirmed. Text confirms "we did not replicate" the depression link.
2. Faulkner 2022 (PMC9811346): gamma_S t(59)=0.320, p=0.750, BF10=0.272 confirmed; money won BF10 is 0.274 (evidence a16 says 0.27, fine). BDI 25.44 vs 3.00 confirmed. Rho +140 7.252 and -140 -2.600 confirmed. Group sizes: table shows 15/16 and 15/15, so 31 healthy and 30 depressed, as recorded.
3. Huys 2012 (PMC3297555): 77% look-ahead, 91% best model, iBIC gain 314, punishment weight about 1.4x reward, specific > general pruning 14/15, 12/16, 14/15 (the order is -70, -100, -140 in the text; evidence a02 listed them without labelling the order) confirmed.
4. Meth use disorder 2025 (PMC12103525): F(1,100)=16.46, 0.33 vs 0.15, d=0.81, points 2034 vs 3145, d=0.77 confirmed. Group x Resistance F(1,90)=5.17, p=0.025 confirmed.
5. Tree of Thoughts: Game of 24 table (IO 7.3, CoT-SC 9.0, b=1 45, b=5 74, best-of-100 IO 33) confirmed in PDF text; abstract says CoT 4% vs ToT 74%.
6. PAC-CF (arXiv 2604.14345): 64.4% / 39.1% / 0/24 / 1/24 and 52.1% vs 64.4% at R=16 confirmed; 97.46% and 99.80% path survival on Game24 and Blocksworld at B100 confirmed.
7. Chen 2026 (arXiv 2605.06840): 2.1%, 32.0%, 4.1% confirmed.
8. Huang 2024 (arXiv 2310.01798): "For GSM8K, 74.7% of the time GPT-3.5 retains its initial answer" confirmed.
9. DeepConf (arXiv 2508.15260): 99.9% is OFFLINE mode (cons@512 97.0, pass@1 91.8); the 84.7% token saving is ONLINE mode. Evidence c14 put both in one line; they are separate settings.
10. Wang 2025 (arXiv 2501.18585): 225% more tokens, 418% more switches confirmed.

## Corrections made (in claims; evidence files left as written)
- DeepConf: do not read 99.9% and 84.7% as one result (c14, claim K17).
- Huys 2012 pruning counts are in order -70, -100, -140 (a02 gave counts without the order).
- Huang 2024: 74.7% is "retained its initial answer after two rounds of self-correction", not "did not change after correction" as one correction step (c11). Wording fixed in K15.
- ToT: report 74% against best-of-100 CoT (49%) as the fair gap; 74 vs 4 mixes compute (K12).
- b17: the Resistance main effect was null but the Group x Resistance interaction was significant (p=0.025); "users pruned slightly less" rests on that interaction only (K08).
- b01/c01 N=46 equals 15+16+15; no participant-count sentence was found by search in the HTML, so N=46 is the sum of group sizes.

## Contradictions between sources
- Depression: Huys 2012 positive; Lally 2017 (healthy), Huys 2015 and Faulkner 2022 (clinical, Bayes factor about 0.27) null. Faulkner notes the 2012 effect was in healthy people, not patients.
- Learned Pavlovian state attraction (a07) was needed in Huys 2012 but did not help in Faulkner 2022 (a17, b13).
- Self-scored pruning: helps in ToT (Game of 24) but Huang 2024 finds no gain without an outside signal. Task type (checkable arithmetic vs open reasoning) may explain this; not tested.
- DeepConf and ThinkPrune cut tokens with no loss, while Wang 2025 shows cutting thoughts too early hurts. Direction depends on what signal triggers the cut.

## Weak spots
- All human "replications" are the same task from one lab lineage (Huys, UCL/Zurich); only the methamphetamine and depression studies add new populations. Independent task paradigms are absent.
- Loss-size dependence was varied in only one paper (N=15-16 per group).
- The SGC result is small-volume corrected in one sample (N=37).
- The meth study reports F(1,100) with 89 participants, which suggests repeated-measures df; not explained.
- LLM evidence is about value-based pruning (ToT, LATS, RAP), not loss-triggered pruning. No direct LLM replication of the Huys task was found (K21).
- ThinkPrune, DeepConf and TIP changed training or decoding, not a prompt scaffold.

## Seen only in snippets or not opened
- Knuth and Moore 1975, Buro 1999 (c23, c24, opened:false); Huys 2015 PNAS page (c25, 403, content came via PMC elsewhere); Callaway 2022 (c26, login wall).
- LLM papers cited in c08 to c10, c13, c15 to c22 were not re-opened by me; their numbers are as recorded by the searchers.

## GAPS
1. Does an LLM shown the Huys maze in text prune after a large early loss, and how much does the optimal-path rate drop (loss vs no-loss path) compared with the human 41-point gap?
2. Does pruning in LLMs grow with depth and token budget the way it does in humans (34/40/49% gap at depth 3/4/5)?
3. Is a prune triggered by a failing code check (not self-score) better than self-score pruning at equal tokens on the same tree, and does a revival rule recover the lost branches? (K15, K13)
4. How often does a ToT-style evaluator discard the eventually correct branch in tasks other than Game of 24 and crosswords, and does the rate rise with evaluator noise as PAC-CF suggests?
5. Is the human cost-insensitivity of pruning (K02) replicated by anyone, with more than one group per loss size?
6. Does the benefit of ToT pruning survive an equal-token comparison against best-of-N and self-consistency on newer models (2025-2026), not only GPT-4?
7. How should the "bad first step" cut interact with underthinking (K16): what minimum hold time for a thought avoids both over-pruning and over-switching?
8. Do emotional or anxiety framings in a prompt change the pruning rate of an LLM, given the weak human anxiety link (K08) and mixed LLM anxiety results (c19)?
9. What do resource-rational planning models (Callaway 2022, unread) predict about the optimal prune threshold, and does it match the human fitted gamma_S of about 0.6?


## Gap search results

Evidence in evidence_d.jsonl (d01-d15). Limits this session: the web search budget ran out after one query, and the arXiv, OpenAlex and Semantic Scholar APIs returned rate-limit errors, so sources came from direct page fetches of known papers. Closing a gap here means partly answered; none is fully closed.

1. Open. No LLM run of the Huys maze was found (d13). The human 78% vs 37% gap remains the target; run it ourselves.
2. Open, partly informed. Chen 2026 (d09): LLM trees widen with effort, mean depth 1.78 plies, depth does not predict wins. No depth-by-loss test.
3. Partly closed. CodeTree (d07) shows test plus critic abort beats execution output alone (94.5 vs 92.7 HumanEval) and abort returns to siblings, but no equal-token test-trigger vs self-score test and no explicit revival rule test. K25 added, single-source.
4. Partly closed. PAC-CF TSP50 (d04): the correct step is removed 52-64% at K=4 and 16 repeats do not cure a biased scorer. No second task family with a measured discard rate; noise sweep not done. SSDP (d01) offers duplicate-merging as a safer prune.
5. Open. No replication with several groups per loss size found (d14, search failure). K02 stays single-source.
6. Partly closed, status contested (K23). Snell 2024, Wu 2024 and s1 give mixed equal-compute results on 2024-25 models: search wins on medium-hard items at low budget, loses on easy items and at high budget; MCTS lost to sampling. No GPT-4-class ToT vs best-of-N test on 2025-26 models.
7. Partly closed (K24). TIP: 600-token mild hold raised AIME2024 pass@1 by 2.7 to 5.8 points; strong penalty with windows over 300 lowered accuracy; prompt-only did not work. Only one lab, decoding-level.
8. Open. Coda-Forno abstract re-checked (d10); no study of anxiety or loss framing on pruning.
9. Open. Callaway 2022 is paywalled and the preprint page was empty (d11); no threshold comparison with gamma_S about 0.6 (d15).

Reading caution: several numbers above (Snell, Wu, s1) come from page text where exact accuracies were in figures only; the table values quoted are those in text.
