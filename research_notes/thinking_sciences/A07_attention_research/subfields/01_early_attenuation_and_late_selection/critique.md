# Critique: A07.01 Early, attenuation and late selection (cross-check)

## Corrections made (sources re-opened this pass)
1. Shi et al. 2023 (arXiv 2302.00093): confirmed 18%, "fewer than 30%", +11 points, +35.5 for 0-COT, 99.7% and 96.5%, best macro 45%. The 18% is among problems solved by the baseline.
2. Weston and Sukhbaatar 2023 (2311.11829): confirmed 62.8 to 80.3 (oracle 82.0), 74.5 keep-original, 71.7 instructed, 51.7 to 61.3 on GSM-IC, Suggest Correct 92 vs Suggest Incorrect 38.
3. Liu et al. 2023 (2307.03172): confirmed more than 20-point drop, 56.1 closed-book, 1.5% and 1% gains beyond 20 documents, closed-book and oracle rows.
4. Leviathan et al. 2025 (2410.02703): CORRECTION to a25. The 16x, 25x, 47x memory savings need the extra memory loss (Lmem, alpha 0.1). With the standard loss the savings are 5x, 7x, 8x. The "2x heads" equivalence is confirmed.
5. Li et al. 2024 (PMC11089017): confirmed N=37 after exclusion, 22,033 trials, over 100 ms slowing, and own-name reports 24/24, 20/24, 4/23.
6. Roer and Cowan 2021 (PMC8908911): confirmed N=80, 23 (29%) reporting own name, BF10 = 1.023, 0.582, 1.018. CORRECTION to b05: two participants reported the yoked-control name, one the semantically unexpected word and two the expected word. "Only 1 noticed an unexpected word" was incomplete.
7. Yang et al. 2025 (2505.18761): confirmed Grok-3-Beta 43% to 19%; GPT-4.1 26% confirmed, the "to 2%" tail was not re-read.
8. Differential Transformer (2410.05258): the 30-point gap at N=6, R=2 is present in the text.
9. MUSI (2605.17225): Gemini-2.0-Flash 0.955 single-stream vs 0.242 cocktail party confirmed. AMBIGUITY: c17 says "0.955 vs 0.320 with Spanish at +5 dB". That 0.955 equals the single-stream figure and may be a paraphrase slip. Treat the language comparison as unverified.
10. Not re-opened this pass: Macdonald and Lavie 2008, Conway 2001 (20% vs 65%), Snowden and Gray 2025 RT numbers. They stay as the earlier agents recorded them.

## Contradictions between sources
- Conway 2001 (span moderates name noticing) vs Roer and Cowan 2021 (inconclusive Bayes factors; their lowest-quartile span was far higher than Conway's).
- Perceptual load theory (Lavie) vs Snowden and Gray 2025 and Marciano and Yeshurun 2017 (no reliable load effect, large individual variation).
- Shi: instructions help partly; Weston: instructions help little vs filtering. Different models, so not a clean conflict.

## Weak spots
- All classic founding papers (Cherry 1953, Broadbent 1958, Moray 1959, Treisman 1960, Treisman and Geffen 1967, Deutsch and Deutsch 1963, Norman 1968, Corteen and Wood 1972, Holender 1986) were NOT opened. Numbers are second-hand from Conway 2001 and Macdonald and Lavie 2008. Moray's 33% (4 of 12) is second-hand.
- Many LLM claims rest on one paper each (Shi, Weston, Liu). Evidence-line counts overstate independence. Models are 2023 vintage (davinci, LLaMA-2, GPT-3.5); modern reasoning models may differ.
- Neural studies have small N (29, 23).
- No LLM paper tests the classic theories directly (a26). The mapping is analogy.
- Only seen in snippets or not extracted: Mesgarani and Chang 2012, Cohen-Dunbar-McClelland 1990, Conv-TasNet, Kamradt needle test.

## GAPS
1. Do 2025-26 reasoning models (with thinking) still show the GSM-IC distractor drop, and does a filter-rewrite step still help at equal tokens?
2. Does an S2A-style rewrite pass beat best-of-N voting at equal total tokens on distractor QA?
3. Does a salient self-relevant but irrelevant token (the agent's own task name) capture a model's reasoning, as the own-name effect would?
4. What are the exact Treisman 1960 ear-switch and Treisman and Geffen 1967 detection percentages, from the originals?
5. Is Moray's 33% (4 of 12) correct in the 1959 paper, and under which condition?
6. Does the first/last placement effect (Liu et al.) hold in 2025-26 long-context models, and does truncation beat full context at equal tokens?
7. Does Snowden and Gray's load-independence hold under independent replication, and what is the 2026 status of load theory?
8. Does the span-by-name-noticing link (Conway) replicate with a larger sample and proper quartile contrast?
9. Is the MUSI 0.955 vs 0.320 language comparison real, and does same-language interference matter for text agents with mixed-language context?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d18). WebSearch budget ran out after two calls and the arXiv, Semantic Scholar and OpenAlex APIs returned 429, so most results come from direct page fetches.

1. Reasoning models and distractors: PARTLY CLOSED. Yes, reasoning models are still distracted by irrelevant trigger text (CatAttack: R1 1.50% to 4.50% attack success, up to 3x longer answers). GSM-DC (2025) tested no reasoning models. Filter-rewrite at equal tokens not tested. (d01 to d04; new claim K17)
2. S2A vs best-of-N at equal tokens: OPEN. No paper found (d17, K23). Recite-then-solve (d08) and ignore-instruction (d03) are partial proxies.
3. Self-relevant irrelevant token capturing reasoning: PARTLY CLOSED. Salient irrelevant sentences (cats trivia, numeric hint) do capture reasoning models, but no test used the agent's own name or task name. (d01, d02)
4. Treisman 1960 and Treisman and Geffen 1967 percentages: OPEN. Originals paywalled (d13, K21).
5. Moray 33% (4 of 12): OPEN. Conway 2001 confirms 33% but gives no N or count (d13). The "4 of 12" stays unverified.
6. Position effect in 2025-26 models, truncation vs full context: PARTLY CLOSED. Effect shrinks beyond about half the window (Veseli), no position effect in Chroma's 18 models, length alone hurts (Du), focused beats full on LongMemEval (Chroma). Equal-token truncation test on frontier thinking models is not done. (d05 to d11)
7. Snowden and Gray replication, 2026 load status: OPEN. No direct replication; two 2026 load papers found, abstract only (d14, d15, d18).
8. Conway span link with larger sample: OPEN. Re-read Conway: N = 40, 20% vs 65%, Fisher p = .005, upper and lower quartiles (d12). Roer and Cowan (N = 80) stays inconclusive; no larger replication found.
9. MUSI 0.955 vs 0.320: PARTLY CLOSED. The numbers are in Table 11 and the paper's text, but the same-language cell equals the single-stream score, which is suspicious. Mixed-language text agents untested. (d16)

Caveats: abstract-only reads for d09, d14, d15. Page fetches are summaries by a small model, so exact table values in d07, d08, d10 should be spot-checked before they go into the final report.
