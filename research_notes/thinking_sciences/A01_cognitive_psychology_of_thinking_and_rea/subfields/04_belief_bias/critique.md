# Cross-check critique: belief bias

## Numbers re-opened this session (full text)
1. Trippas et al. 2018 (b01-b03): 22 studies, N=993, BF 7.34 (null on da difference), BF 17.28 and 11.84 (equal variance), BF 69.72 and choice-focus -.03 [-.08,.02], forced-choice .64/.43/.38 for valid. CONFIRMED. Table 1 cell values (.92/.46/.92/.08, interaction -.38) CONFIRMED as printed there.
2. Evans and Curtis-Holmes deadline (a24, a37): OpenAlex abstract says 10 seconds. CORRECTED: it is 10 s; the 2-second figure from Wikipedia is wrong. Not a full-text read.
3. Macchi 2019 (a27, a28): CONFIRMED 94%/96% valid-believable; a27 truncated value now filled: invalid-believable correct 4% untrained, 10% trained (N=130). Exp 2: 66%/77% ("necessarily"), 41%/67% ("criteria of logic"), p=.45 and p=.03 confirmed. Added caveat: ONE syllogism per condition, so this is a demonstration, not a rate.
4. Trippas, Handley, Verde 2014 fluency (a19, b08): t(75)=8.41, 6.72, 2.81 (p=.006), da .92 vs .51, F=6.22, p=.015 CONFIRMED.
5. Trippas, Thompson, Handley 2017 (a23, b14): .68 vs .83 (OR 1.58), complex .71 vs simple .80, 4786 vs 4503 ms (d=0.17), simple/complex cell values CONFIRMED. Exp 1 no-conflict .92 is consistent with cell means .93/.97/.91/.86.
6. Bertolazzi 2024 (c05-c07): LLaMA-3 8B 30.31 overall, 0.83 on invalid, 70.74 valid; 8B-inst 50.00; 70B 30.63; 70B-inst 41.25; human 44.63/40.97; atmosphere 82.97/62.79/92.31 CONFIRMED. The SFT/ICL rows in the text extraction are column-scrambled (e.g. a 96.25 accuracy next to 1.85 on invalid cannot both be right), so c06's SFT figure is flagged "layout garbled", only the 96.25 headline is kept.
7. Dasgupta et al. (c01, c02, c03, b21): item-level t(345)=4.98, response time z=4.44, slowest 15% over 80 s, no interaction in Chinchilla or PaLM 2-M, interaction in humans, PaLM 2-L, Flan-PaLM 2, GPT-3.5 CONFIRMED. Note: the arXiv text also gives t(832)=3.49 for another comparison.
8. Wikipedia figures (a33): 80/33 and 73/41 are the marginal means of the original 89/71/56/10 cells ((89+71)/2, (56+10)/2, etc.). CORRECTED: a33's note that 89 and 56 "look inconsistent" is wrong; Wikipedia garbled the labels (89 = valid-believable, 56 = valid-unbelievable). The original cell 71 (invalid-believable) and 10 were not seen in a primary source this session.
9. Stupple and Ball (a01-a02): taken from the previously opened PDF; not re-opened (time).
10. Trippas 2018 b05/b06 moderator text: agreed with the paper's framing; not re-read in depth.

## Contradictions between sources
- Invalid-believable acceptance: Trippas 2018 Table 1 prints .92 for an invalid-believable cell; Wikipedia (original EBP) 71%; Dasgupta quotes about 90%; Stupple and Ball 71% and 61%; Macchi 96% for plain-wording single item. Different items, populations and definitions. Treat 70-90% as the range, not one number. UNRESOLVED which EBP cell is 92% (the Trippas table may be a simplified example).
- Content effect in LLMs: Bertolazzi 2024 (older open models) say CoT does not fix it; Bertolazzi 2025 (Qwen/Gemma instruction-tuned) say CoT sharply cuts it. Different model generations, so not a true contradiction, but our model sits at the newer end.
- Dube 2010/2011 and Trippas 2013/2018 (curvilinear ROC, bias-only) versus Klauer and Kellen 2011 and Singmann and Kellen 2014 (linear ROC, unidentifiable design). The 2018 meta-analysis answers the aggregation worry, but authors overlap with one camp.
- Time pressure: Evans and Curtis-Holmes supports fast-belief; Trippas 2017 and De Neys-style work does not support strict sequence.

## Weak spots
- Much of the 1983-2005 primary literature (a05-a12, a24-a26, a34-a35) is only seen through secondary text; many "opened" flags there mean a secondary page, not the paper. a36, a37, b07, b11-b13, b16, b24, b25 were abstract-only.
- Few effect sizes for the classic claims (selective scrutiny, misinterpreted necessity); no failed replication of EBP was found and none was searched exhaustively.
- LLM evidence is mostly 2022-2024 models. Only the 2025 papers cover modern instruction-tuned models, and those are small open models, not frontier ones.
- SDT claims rely on one research group.
- SemEval metric is noisy (c18), so team rankings are weak evidence.
- Macchi 2019 is one item per condition.

## GAPS
1. How large is the belief (content) effect for a current frontier model with plain prompting, on believable-invalid vs unbelievable-valid items, scored with d-prime and bias rather than difference scores?
2. Does chain-of-thought at equal tokens reduce content effect for frontier models, or only for the small Qwen/Gemma models tested in 2025?
3. Is the "necessarily follows" wording effect (4% to 66%) real across many items, and does it transfer to LLM prompts?
4. Does an explicit counterexample search help on indeterminate-invalid items more than on determinately invalid items (misinterpreted necessity vs selective scrutiny test in LLMs)?
5. Does verifying only dissonant conclusions beat verifying all conclusions at equal tokens (selective scrutiny as a design choice)?
6. Does translating to formal logic plus a prover beat prompt-only abstraction at equal tokens, and what is the token cost?
7. What are the original EBP 1983 Exp 1 to 3 cell percentages and N (primary source), and do the mid-century to 2000s replications report the same interaction size?
8. Are there failed replications of the logic-by-belief interaction in raw rates, or of the time-pressure effect (Evans and Curtis-Holmes 2005)?
9. Does a conflict flag (prior belief versus derived verdict) predict LLM errors well enough to route extra verification?
10. How does belief strength (graded plausibility) predict LLM error rate, and does it show the human dose-response (b19)?

## Gap search results (evidence_d.jsonl, d01-d20; claims A01.04-K19-A01.04-K27 added, A01.04-K16 now contested)
Search note: WebSearch quota ran out after about 10 calls; I continued with the arXiv API, OpenAlex and direct PDF downloads. The Semantic Scholar API was rate limited. Several human-literature PDFs (Evans 1983, Evans and Curtis-Holmes 2005, Newstead 1992, Evans 2001) were not obtainable, so those stay abstract-level.

1. Frontier content effect, plain prompt: PARTLY CLOSED. Recent strong models (Gemini 2.5 Pro/Flash, GPT-OSS-20B, GLM-4.6) show only +0.8 to +1.9 pp congruent-minus-incongruent on easy syllogisms; Kimi-K2 and DeepSeek V3.1 about +7.5 to +7.9 (d01). Those are ceiling accuracy differences, not d-prime. The only SDT-style numbers are mine, from GPT-4 (2023) cells in BaRDa: d' 1.21 vs 1.96 and criterion -0.81 vs +0.30 (d05). No current Claude model was tested anywhere I found; Claude-3 models appear only on a valid-only benchmark (d03). Still open for a proper d-prime run on hard items.
2. CoT at equal tokens, frontier: STILL OPEN. Mixed signals: reasoning effort took GPT-5-nano from 69.2 to 98.8 (d03); a CoT prompt rescued 87% of GPT-4o failures (d04, selected failures); CoT did not uniformly cut CE in open models (d10). No equal-token test.
3. "Necessarily follows" across items and LLMs: STILL OPEN, weaker than before. One item per condition (d07); earlier multi-item wordings reported unsuccessful; Newstead Exp 5 83% vs Evans 1994 56% (d06). No LLM transfer test found.
4. Counterexample search by determinacy: STILL OPEN. No LLM study. Human analogue: Newstead 1992 Exp 1-2 (abstract only, d08).
5. Verify only unbelievable conclusions vs all: STILL OPEN. Closest is disagreement-routed Z3 (d11); small gain, different trigger, not equal tokens.
6. Prover vs prompt abstraction at equal tokens: PARTLY CLOSED on direction, OPEN on cost. Prover beats prompting for a 4B model (95.83/2.28 vs 84.17/14.67, d13) but a strong model's plain prompt is already 98.43/2.13 (d14). Predicate-argument abstraction was worse than raw text (d14). Solver-alone is worse than prompting through extraction errors (d12). Costs: about 4,300 tokens/item (d11), $0.30 vs $0.02 (d16). No equal-token comparison.
7. EBP 1983 cells: STILL OPEN. Two sets circulate (92/46/92/8 and 89/56/71/10); Macchi's Table 1 prints 92% and 8% (d06). Primary paper not obtained; no N.
8. Failed replications: PARTLY CLOSED. No direct failed replication of the 10 s deadline found; Trippas 2017 and a 2015 thesis argue against the strict fast-belief story (d17, d20). Instruction effect replicated only partly (Evans 1994, d06). Raw-rate interaction: Newstead 1992 reports it vanishing with only determinate syllogisms (d08, abstract only).
9. Conflict flag predicts LLM errors: STILL OPEN. Only ensemble disagreement was tested (d11). No test of belief-versus-verdict conflict.
10. Graded belief strength in LLMs: STILL OPEN. LLM studies treat plausibility as binary (d18).

New cautions: (a) accuracy-gap metrics at 99% ceiling hide the bias; (b) valid-only benchmarks (BIS) cannot separate skill from a response-criterion shift; (c) the Poddar, FregeLogic and SemEval numbers are preprints tuned on small sets.

## Gap search results, second pass (evidence_d.jsonl d21-d30; claims A01.04-K26 resolved, A01.04-K28-A01.04-K31 added)
Search note: WebSearch worked for about eight queries; arXiv API and OpenAlex covered the rest. Evans and Curtis-Holmes 2005, Newstead 1992 and Evans 2001 still have no open PDF.

CLOSED
- Gap 8 (original EBP cells): CLOSED. The primary paper (Memory & Cognition 11(3), 295-306) was downloaded and read. Exp 1 N=24: 92/46/92/8. Exp 2 N=64: 86/62/66/13. Exp 3 N=32: 91/53/67/6, interaction p=.067 (p<.01 in Exp 2). Correct when logic agrees vs conflicts with belief: 92 vs 27, 87 vs 48, 97 vs 43. The 89/56/71/10 set on Wikipedia matches no cell; closest is Exp 2 A-C conclusions (88/56/72/13). Interaction size is consistent in direction across all three; later replications' sizes were not re-extracted.

PARTLY CLOSED
- Gap 3 (necessarily wording): the original Exp 1 instruction already said the conclusion must necessarily follow and 92% still accepted invalid-believable items; Exp 3's stronger wording gave 67%. This agrees with the view that Macchi's 4% to 66% is a one-item effect. Not tested on many items and not in LLMs. Still open for LLM transfer.
- Gap 9 (failed replications): no direct failure of the 10 s deadline. Boundary conditions found: no change from speeding in conditional inference (Evans, Handley, Bacon 2009) and vanishing accuracy cost of belief under time pressure in ROC analysis (Trippas, Handley, Verde 2013), both abstract level. Raw-rate interaction: Exp 3 of the original paper itself was only p=.067.
- Gap 1 (frontier effect size): NeuBAROCO shows GPT-4 (2023) 82.92 vs 67.23 congruent vs incongruent on NLI, but no drop in easy multiple choice. Still no Claude or GPT-5 d-prime anywhere.

STILL OPEN (need our own experiments)
- Gap 2 (CoT or effort at equal tokens), gap 4 (counterexample search by determinacy), gap 5 (verify only conflicts vs all), gap 6 (conflict flag as predictor), gap 7 (prover vs prompt at equal tokens; only note: a predicate-logic translation inside one GPT-4 prompt lifted accuracy 77.78 to 96.67, d25, no token count), gap 10 (graded belief strength in LLMs). The original authors proposed gaps 4 and 5 as competing explanations in 1983 and could not separate them (d24).

New caution: cell percentages quoted from Wikipedia should not be used; use the primary values above.
