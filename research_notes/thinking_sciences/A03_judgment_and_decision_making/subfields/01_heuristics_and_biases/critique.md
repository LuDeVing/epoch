# Cross-check critique: A03.01 Heuristics and biases

Checker pass over evidence_a (37 lines), evidence_b (28), evidence_c (27). 92 evidence lines, 31 claims (A03.01-K01 to K31).

## 1. Sources re-opened this session (full text, pdftotext)

| Source | Numbers checked | Result |
|---|---|---|
| Hagendorff, Fabi, Kosinski arXiv 2212.05206 v2 | CRT: humans 38 correct / 55 intuitive; davinci-003 5 / 80; ChatGPT-3.5 59 / 15; ChatGPT-4 96 / 0; CoT 80 to 29; semantic illusions 72 / 18 / 74 / 88 | Confirmed (a26, c05, c06) |
| Suri et al. arXiv 2305.04400 | Anchor means 20.83 vs 105.97 (human 22.5 vs 80.50), t(58)=8.78; conjunction 18 of 20; GPT-4 94.33 | Confirmed (a24, b12, c08) |
| Macmillan-Scott and Musolesi arXiv 2402.09193 | 69.2, 55.0, 77.5, 21.7, 50.8, 73.3, 8.3 percent | Confirmed (a30, b17, c07) |
| Lou and Sun arXiv 2412.06593 | 62 questions, 11 exceptions of 162 (9 from GPT-3.5), 12 of 12 PTF questions no exception, GPT-4 anchoring index 0.45 vs 0.61 human | Confirmed (b14, c11). a28 says "60-plus questions": the paper says 62. |
| Huang et al. arXiv 2604.01366 (CogBias) | Judgment shift -4.3/-7.7/-2.7; debias -4.4 percent judgment, +40.5 percent response; Qwen -19.0 points | Confirmed (a35, b19, c18) |
| Knipper et al. arXiv 2509.22856 | 2.8 million, 17.8 to 57.3 percent, 39.5 percent, 14.9 percent; QwQ-32B anchoring 0.776, representativeness 0.587; Qwen2.5-72B 0.405 | Confirmed (b18, c15) |
| Wang et al. arXiv 2404.01461 (REHEAT) | 34.7, 31.2, 27.2, 14.8; 153 Prolific humans; GPT-4 CoT +3.9, one-shot +5.2 (36.4); LLaMA one-shot +14.5; specific hint 46.5 (+15.3) | Confirmed. The extracted table is column-misaligned, so c09's reading (GPT-4 +5.2, LLaMA +14.5) was checked by arithmetic (31.2+5.2=36.4; 27.2+14.5=41.7). |
| Kraishan arXiv 2610.10049 | 12,350 calls, delta +0.031, t(29)=1.45, p=.157, anchoring d=1.89, restate p=.057 | Confirmed (a34). |
| Jones and Steinhardt arXiv 2202.12299 | Codex 32.9 baseline; 22.3 to 30.5 point drop; 81 vs 4.5 percent; 67 percent exact anchor; save frame 11.3 vs die frame 60.0 | Confirmed (a27, b13, c03, c04). |
| Binz and Schulz arXiv 2206.14576 | Linda, hospital, cab and CRT patterns | Confirmed in text (a25, b10, c01, c02). |

## 2. Corrections made or required

1. b11 (Hagendorff, published-version numbers: 84.5 percent intuitive, 86.7/5.3/8 percent on 150 CRT tasks, 10.5 / 79.5 / 97 percent correct on 200 tasks) does not match the arXiv v2 text (80 percent intuitive, 5 percent correct on 150 CRT tasks). These are different versions. Use the arXiv v2 numbers (a26, c05) for anything citable; treat b11 as a second version, not a second experiment. Claim K17 notes this.
2. a28 "60-plus questions" corrected to 62 (b14, c11 right).
3. a21 (Gigerenzer 1991: Linda 85 vs 20 percent) rests on a Wikipedia summary and is opened:false in substance. Replaced in the claims by the first-hand figures in b02/b03 (Hertwig and Gigerenzer: 82 to 88 percent standard, 0 to 13 percent with frequencies).
4. a15 (Stock, Fisk, Montgomery) has an approximate year and only an abstract; used only as a boundary note (K06).
5. Duplicates inflate the evidence count. The same papers appear two or three times: Suri (a24, b12, c08), Lou and Sun (a28, b14, c11), Macmillan-Scott (a30, b17, c07), Echterhoff (a29, b16, c16, c24), CogBias (a35, b19, c18), Knipper (b18, c15), Hagendorff (a26, b11, c05, c06, c23), Binz and Schulz (a25, b10, c01, c02), Jones and Steinhardt (a27, b13, c03, c04, b27), Araya (a37, b23, c21), Saeedi (b22, c20), Sumita (a31, b20, c19), Itzhak (a32, b15, c26), Owusu (a33, b21), Klein (a19, b01, b24). The `independent_sources` field in claims.jsonl counts papers, not lines.
6. c23 and c27 are commentary lines, not sources (c27's "source" field is a placeholder). Not used as evidence.
7. Many Labs 1 (Klein 2014), Hertwig and Gigerenzer 1999 and Tversky and Kahneman 1983 could not be re-opened: the open copies returned HTML or were blocked. Their numbers were consistent across lines a19/b01/b24 and a09/b02/b03 but are not re-verified by this checker.
8. c14 (Malberg et al.) and c12 (Huang et al. anchoring) were not re-opened; ranges are as the workers recorded.

## 3. Contradictions between sources

- Reasoning models and anchoring: c12 finds reasoning models lowest (DeepSeek-R1 25 percent, Qwen3 thinking 22 percent anchored); a34 finds reasoning siblings no less biased (delta +0.031, ns) and anchoring d = 1.89; a28 finds stronger models more consistently anchored by expert hints. Different metrics, items and models. Unresolved (K15).
- Tuning: b15 says instruction tuning and RLHF raise biases (belief-invalid 0.00 to 0.55 to 0.65); a26 shows tuning removes the CRT trap. Both can hold: the direction depends on the bias (K20).
- Human-likeness: a30 says LLM errors are mostly not human-like; a23, a24 say they match humans on coherence and anchoring. The first measures wrong-answer types across tasks, the others measure effect direction.
- Frequency format: b02 reports 0 to 13 percent violations with frequencies; b03 reports Jones et al. 85 vs 81 percent (no effect); a15 reports no help for base-rate neglect in older adults; a14 says the gain is for the numerate. K04 and K06 are contested for this reason.
- Debiasing prompts: c18 says a generic reminder backfires for judgment biases; c19 and a29 say awareness prompts help some; c17 says iterative rewriting helps strongly. All were tested on different models and metrics (K21, K22).

## 4. Weak spots

- Almost all LLM work uses single prompts at temperature 0 or one sampled run per cell, with small item sets. Effects on named models will date quickly (GPT-3.5 and Llama-2 results do not describe current agents).
- Very few LLM studies test the original base-rate-neglect task with a human control at the original N; Linda and cab results come from one prompt each (Binz and Schulz).
- No LLM study of the 1974 calibration result (98 percent intervals) was found.
- Anchoring scoring differs across papers (logit difference, anchoring index, anchored ratio, utility), so numbers cannot be compared across studies.
- Debiasing results are mostly measured as bias score, not as accuracy at equal tokens. Token cost of SACD and CoT is not reported in the lines.
- Human literature is thin on post-2015 replications of the Linda problem outside Hertwig and Gigerenzer; Many Labs covers anchoring and framing only. No failed replication of Linda itself was recorded.
- Only seen in snippets or not opened: a20 (Kahneman and Frederick), a21 (Gigerenzer 1991), a22 (Epley and Gilovich abstract), a31, a32, a36, a37, c26.

## GAPS

1. Does a stripping or restating step at equal tokens beat extra thinking budget on anchored numeric items for current models (the only direct evidence, a34, is p = .057 on five items)?
2. Does an explicit "name the base rate and sample size first" step help current LLMs on base-rate and sample-size items, and at what token cost (REHEAT hints helped, but only on a 2024 dataset with older models)?
3. Do frozen vignette results (Linda, cab, hospital) hold on perturbed or novel vignettes for 2025 to 2026 models; is any apparent success contamination?
4. Does a counts-format rewrite (natural frequencies) help LLMs on conjunction and Bayes items, and does it depend on arithmetic difficulty as in people (Chapman and Liu)?
5. Which debiasing prompt wins on judgment biases specifically (iterative detect-and-rewrite vs generic reminder vs concrete rule hint), compared at equal total tokens?
6. How large is sequential or context-order anchoring in long agent contexts (prior tool results and earlier guesses), and does evaluating items in fresh contexts remove it?
7. Are LLM 90 or 98 percent confidence intervals overconfident, and does the 1974 calibration result replicate in models?
8. Is the anchor effect in shallow layers (c12, a33) reachable by any late prompt instruction, or only by removing the number from the input?
9. What did Many Labs and Hertwig and Gigerenzer actually report in full (exact N, items) so the founding numbers can be re-verified at source?
10. Does the human finding that direction knowledge gates the benefit of accuracy motivation (Simmons et al.) have an LLM analogue: does telling a model which way its guess is likely off reduce anchoring more than an accuracy instruction?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d21). Claims K09, K03, K04, K16, K18, K22, K24, K26, K27, K29, K30 were updated and K32 to K37 were added. The two claims whose status changed on weight of evidence are K16 (now contested) and K18 (now contested); K29 moved from single-source to established.

Closed or mostly closed:
- Gap 9, closed. Many Labs 1 (Table 2, opened at source, d01): 36 samples, 6,344 participants, anchoring replication d medians 2.43, 2.00, 1.88, 1.18 against an original aggregate d of 0.93, with 36 of 36 samples in the expected direction. The original and replication effect sizes are not like for like (point-biserial test-retest vs between-subjects). Hertwig and Gigerenzer (d02): 15 of 18 (83 percent) in Study 1, 0 and 13 percent in the frequency Studies 3 and 4, median 87 vs 17 percent over the literature; Jones et al. (1995) is the exception with 85 vs 81 percent.
- Gap 7, closed for LLMs in general, still open for the exact 1974 design. Three studies show LLM intervals are too narrow: GPT-4o-mini covered 63, 59 and 64 percent at 90, 95 and 99 percent asked (d03); eleven LLMs covered 9 to 44 percent at 95 percent asked, with no gain from reasoning effort (d04); hit rate was flat across 60 to 95 percent asked (d05). None used the 98 percent almanac design. The overprecision result replicates in direction and is larger than the human 30 percent miss rate.
- Gap 6, partly closed. AnchorBench (d06) measures anchors from the model's own earlier answer (influence 0.34 for plausible values), the prompt (0.22), a tool result (0.18), retrieval (0.13) and demonstrations (0.03). A judge paper (d08) finds prior scores in context shift scores in 7 of 8 models. Still open: no study ran the same items in fresh context against a running context, and the History and Tool numbers carry format confounds.
- Gap 3, partly closed. On 1,024 new Linda/Bill vignettes GPT-4 scored 0.98 on Linda items (d11), so strong-model success on conjunction items is not only memory of the famous text. Open: nothing tested 2025 to 2026 models on perturbed Linda, cab or hospital items. PsyAgentBench (d12) shows textbook-vs-counterfactual gaps for Asch conformity (Llama 70B 46.2 to 3.8 percent) and an anchoring pattern unlike humans (0 on facts, about 1 on invented quantities).

Partly informed:
- Gap 5. No equal-token comparison exists. SACD (d13) wins on its own benchmark where the bias is an injected cue, but round 1 can be worse than no debiasing on a strong model (0.2070 vs 0.1648) and the loop costs up to 9 extra calls. A short 'use only task evidence, ignore extraneous numbers' line cut anchor discrimination in 4 of 4 cells (d07). A self-check turn and a CoT instruction can raise anchoring (d07, d08). A generic reminder remains the worst-supported option (CogBias -4.4 percent, from the earlier pass). Best current guess: an input-side strip or labelling step plus a short evidence-only instruction, not a reflection turn.
- Gap 8. No paper tests a late instruction against the shallow-layer pathway. Indirect: 'think carefully' and reflection did not help on SynAnchors (d09), anchoring falls with model confidence (d18, abstract only), and an 'ignore' line helped small models (d07). Removing the number from the input is still the only fix with a clear mechanism.
- Gap 10. No controlled test. The informed-buyer arm (d10) is the nearest analogue: telling the buyer that the seller anchors recovered part of the loss, more for o1 (0.40 to 0.20) and QwQ (0.26 to 0.00) than for GPT-4o (0.38 to 0.32). It names the tactic and the direction was obvious, so it does not test direction knowledge.

Still open:
- Gap 1. Nothing new on stripping vs thinking budget at equal tokens. The reasoning-effort results (d04) and the earlier 0 to 8192 token result both point away from budget helping, but no study pits a strip or restate step against budget on anchored numeric items.
- Gap 2. No test of a 'name the base rate and sample size first' step on current models.
- Gap 4. No LLM study of counts-format vs probability-format on conjunction and Bayes items by arithmetic difficulty. The only 2025 data are a one-problem case study (d14), and the large gains seen on probability tasks come from code or simulation (d21).

Notes on weight: d12, d16, d19 and d20 are low-confidence (one model, no mitigation, or theory-led, or a 1B model in a simulation); d08, d09, d12, d16 and d21 were read through a fetch summary of the page text, not as a raw PDF; d18 is an abstract only. The arXiv ids dated 2605 to 2610 were taken from search results and fetched; their dates and content were not checked beyond the pages opened.
