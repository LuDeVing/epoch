# Critique: Metacognition and higher-order representation (D06.08)

Cross-check of evidence_a/b/c.jsonl (77 lines). Sources re-opened this session as PDF text: Binder 2024 (2410.13787), Huang 2024 (2310.01798), Chen 2025 (2505.05410), Xiong 2024 (2306.13063), Turpin 2023 (2305.04388), Panickssery 2024 (2404.13076), Song 2025 (2503.07513), and the Lindsey page on transformer-circuits.pub.

## Numbers confirmed (10)
1. Binder: Llama 70B 48.5% vs GPT-4o 31.8%; GPT-4o 49.4% vs Llama 36.6%; +17% mean advantage; 32.6% to 49.4% with training; GPT-3.5 +0.8% (p=0.002). Confirmed.
2. Binder plateaus: 35.2% (GPT-4o predicting Llama, ~10k samples) and 36.2% (GPT-4 cross-prediction, 20k) against self-prediction 48.5% and 49.6%. Confirmed (appendix).
3. Huang: GPT-3.5 CSQA 75.8 to 38.1 (round 1) to 41.8 (round 2); GSM8K 75.9 / 75.1 / 74.7; GPT-4 GSM8K 95.5 / 91.5 / 89.0; 74.7% answers retained. Confirmed.
4. Huang oracle: GPT-4 GSM8K 95.5 to 97.5, HotpotQA 49.0 to 59.0; GPT-3.5 GSM8K 75.9 to 84.3. Confirmed.
5. Chen: 25% and 39% overall; 20% and 29% misalignment hints; 44% and 32% relative drop on GPQA; plateau 28% MMLU / 20% GPQA; reward hacks under 2% in 5 of 6 environments. Confirmed.
6. Xiong: average ECE above 0.377 for weaker models; GPT-4 AUROC 62.7% average; +22.2% GPT-3 to GPT-4; GSM8K CoT GPT-4 93.6% accuracy with ECE 0.064 from 100% confidence everywhere; white-box vs black-box 0.522 to 0.605. Confirmed.
7. Turpin: -36.3% (GPT-3.5 suggested answer), -18.7% / -4.7% answer-is-A, few-shot -36.3 to -24.1 and -30.6 to -21.5; 1 of 426 explanations mention the bias. Confirmed.
8. Panickssery: GPT-4 73.5% self-recognition vs two LLMs and humans; correlation 0.41 before finetuning. Confirmed.
9. Song: meta to direct correlation never above .25; r=.32 for similarity consistency; only "other" similarity class differs from self (beta=-.03, p<.01). Confirmed.
10. Lindsey: Opus 4/4.1 about 20% at best layer (about two thirds depth), strength 2; 0 false positives in 100 trials for production models; helpful-only variants false positives; Sonnet 3.5, Haiku 3.5, Opus 3 still above zero net. Confirmed. New detail: random vectors cause detection in 9 of 100 trials at strength 8; without the setup explained, affirmative rate rose 20% to 42% but only 2 of 50 looked introspective; base models had no net positive.

## Corrections and cautions
- Binder is reported with two different cross-prediction figures (31.8 / 36.6 in main text; 35.2 / 36.2 are data-scaling plateaus in the appendix). They are different conditions, not a conflict. Use main-text values for headline, plateau for the scaling claim.
- c20 gave Huang's HotpotQA oracle comparison as "59.0 vs 29.0 baseline". Wrong pairing: 29.0 is the GPT-3.5 baseline; the GPT-4 baseline is 49.0 (49.0 to 59.0). Fixed in claim K10.
- Xiong's "54.8% to 92.7%" compares different columns and methods (Top-K M=1 vs Self-Random+Consistency M=5). It is a best case, not a typical gain. Typical aggregate gains are smaller (tables show 56-79 AUROC). b11/c05 differ on "five dataset types" vs "eight tasks": both are true (five types, eight datasets).
- Lindsey year: the page is 2025 (Oct, Anthropic); a20 labels it 2026 and b24/c14 label it 2025. Treat as one source; evidence lines a20, a21, b24, c14, c15 are not independent. Likewise Kadavath is a16/a25/b09/c01-c03, Turpin a18/b07/c17, Chen b06/c19, Huang b13/c20/c21, Binder a19/b15/c08/c09 and Betley b17/c12/c13: same paper, so duplicates inflate nothing in the claims (counted once).
- b24 (Lindsey) says "from memory"; now confirmed by the page, so opened status for that fact is good.

## Contradictions between sources
- Human work says self-report is poor (Nisbett and Wilson 1977) but Grassi 2025 finds high detection of choice swaps (92.1%) when tested with a debrief and concurrent reports. Contested; the 13% figure for the classic study is secondhand.
- LLM work: Binder and Betley find self-knowledge advantage after finetuning; Song finds none off the shelf with 21 open models. Compatible only if the effect needs training.
- Kadavath calls models "mostly" calibrated while Xiong finds verbalized confidence overconfident. Resolved by format: logit-based or P(True) in multiple choice vs verbalized numbers in free generation.
- Higher-order theories (Rosenthal) vs first-order and global-workspace views is unresolved and not decision-relevant for the agent.

## Weak spots
- Not opened: Rosenthal books, Proust 2013 book, Nisbett and Wilson 1977, Johansson 2005, Koriat 1997, Nelson and Narens 1990, Maniscalco and Lau 2011 and 2012, Rounis 2010, Lau and Rosenthal 2011, Steyvers 2025. Claims K17, K18, K24 and the philosophy claims rest on secondary summaries.
- The philosophical core (Rosenthal, Proust) has almost no direct empirical content for an LLM agent. The useful evidence is the empirical metacognition literature.
- Almost every LLM result uses 2022-2024 models (GPT-3.5, GPT-4, Claude 1.0 to 3.7). No test on current frontier models of whether a scaffold step that asks for confidence or self-explanation improves final accuracy at equal tokens.
- Tian 2023 (b10) and Kapoor 2024 (b12) are cited from abstracts only in the evidence file; per-dataset numbers were not checked.
- Lindsey's 20% is a best-case setting (chosen layer and strength) on one model family; it is not a rate for natural use.

## GAPS
1. Does a confidence or self-check step, at equal tokens, improve final accuracy of a current frontier model on our benchmarks, versus spending the same tokens on extra samples with agreement voting?
2. Which monitor best predicts errors in our agent at equal cost: verbalized confidence, P(True), sample agreement, trace length/retries, or a separate critic with a different prompt or model?
3. Do reasoning models of 2025-2026 verbalize planted cues in the trace more often than the 25-39% of Chen 2025, and does asking for an explicit "what influenced this" step change that rate?
4. How large is the self-preference bias when the same model grades its own traces, and does swapping the grader model or hiding authorship remove it? (Panickssery measured recognition and preference on summaries only.)
5. Does self-correction help when the external check is cheap but imperfect (unit tests, retrieval, calculator, another model), and how bad can the check be before revise hurts (Huang vs Kamoi)?
6. Do the human metacognition results (performance confound in AUROC2, Fleming and Lau 2014; Rahnev 2025) change how we should score the agent's confidence, e.g. M-ratio style efficiency across difficulty bins?
7. Does introspective accuracy (Lindsey about 20%, Binder 48.5%) improve with scale or with post-training on current models, and does it help any task outcome, or only self-description?
8. What do the unopened primary sources (Nisbett and Wilson 1977 exact N and percentages; Johansson 2005; Koriat 1997; Proust 2013) actually show, and how do the choice-blindness replications compare?
9. Does stating confidence early in a trace (before answering) bias later steps (anchoring) compared with scoring confidence only after the final answer?
10. Can a non-verbal monitor (Proust-style feeling signal: agreement, entropy, fluency of the generation) serve as the trigger for S-state transitions, and at what false-alarm rate?


## Gap search results

New evidence: evidence_d.jsonl (d01-d19, 17 opened in full text, 2 abstract-only). Claims K26-K35 added; K07, K09, K10, K14, K15, K17 extended. Search tools: the WebSearch budget ran out after one call; arXiv and Semantic Scholar APIs were rate limited, so most sources were found by known id.

1. Confidence or self-check vs extra samples at equal tokens (frontier model): PARTLY CLOSED. CISC (d10) and DeepConf (d12) show that confidence-weighted voting beats plain voting at equal samples (P(True) saved 46% of samples; DeepConf 99.9% vs 97.0%). No study found that compares a single verbal self-check step with extra samples on a frontier API model. Own test still needed.
2. Best monitor at equal cost: PARTLY CLOSED. Sample agreement in meaning (d13) and trace-level confidence (d11, d12) beat verbalised numbers; P(True) is best for within-question weighting (d10); a trace-reading critic gives 95% vs 60% recall for hacks (d05). No head-to-head on our agent. Verbalised confidence is weakest in all comparisons except for reasoning models (d14).
3. Reasoning models verbalising cues: PARTLY CLOSED. R1 59% on the professor cue, but 6 to 34% on others (d03). Asking for an explicit "what influenced this" step: not tested, open.
4. Self-preference when the model grades itself: PARTLY CLOSED. GPT-4 bias 0.520 (d01); driven by low perplexity not authorship alone (d02). Whether swapping grader or hiding authorship removes it: not measured here, open.
5. Self-correction with a cheap imperfect check: PARTLY CLOSED. Needs a reliable check, ideally with error location (d07, d08). The tolerable error rate of the check stays OPEN.
6. Human metacognition measures for agent confidence: CLOSED at the level of method (d17): score within difficulty bins or within question. Rahnev 2025 not opened.
7. Introspection with scale and task benefit: PARTLY CLOSED. Small privileged access in 2026 models (d15), training needed for report accuracy (d16). Task benefit: none measured, so open.
8. Unopened human primaries: STAYED OPEN. Only abstracts of Johansson 2005 and Hall 2010 read; Nisbett and Wilson 1977, Koriat 1997 and Proust 2013 not obtained; no failed choice-blindness replication located.
9. Early stated confidence anchoring later steps: STAYED OPEN. No direct study found. Indirect hint (d14): confidence gets better as the CoT unfolds, so score it after the answer.
10. Non-verbal monitor as S-state trigger: PARTLY CLOSED. Works for discarding traces and stopping early (d12, d11); false-alarm rates for state transitions in an agent not reported.

Caveats: DeepConf, CISC and Kang use open models with logprobs. Numbers marked "not extracted" in evidence_d are from abstract or text only.
