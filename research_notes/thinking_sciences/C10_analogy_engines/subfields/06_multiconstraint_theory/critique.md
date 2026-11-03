# Critique: Multiconstraint theory (cross-check)

Scope: evidence_a (30 lines), evidence_b (30), evidence_c (27). Claims in claims.jsonl (25, K01-K25).

## 1. Numbers re-opened and checked (10 sources, text re-extracted this session)

| # | Number | Source | Result |
|---|---|---|---|
| 1 | Anthar 54% vs 19% (trade), 21% vs 58% (membership), chi2(1,N=53)=11.78 | Spellman & Holyoak 1996 | Confirmed (a09, b05) |
| 2 | Exp2 chi2(N=108)=8.85; Exp3 97% (chi2 N=107 = 95.33); 65% vs 35% (chi2 N=88 = 7.68); 16.41 | same | Confirmed (a10, a11, b07) |
| 3 | Mappings O .33, R .30, SO .32, U .06; F(3,141)=21.64; 2.36 mappings per character; SME 1.01 vs 6.21; LISA 24/18/48% | Krawczyk, Holyoak & Hummel 2004 | Confirmed (a15, b10, b11) |
| 4 | Humans .753 overall; error types Table 4 | Lewis & Mitchell 2024 (2402.08955) | Table 2 and 4 found. CORRECTION below |
| 5 | Story analogy order bias and paraphrase | Lewis & Mitchell (2411.14215) | Confirmed. Original Webb (WHL) data 0.89/0.61/0.75; their own GPT-4 run 1.0/0.72/0.86 (31/36); humans 0.78/0.78/0.78 (564/720). Paraphrase GPT-4 0.86 to 0.72, humans 0.78 to 0.70 |
| 6 | ARN: near 75.0 vs 97.9, far 39.6 vs 94.1, partitions 76.9/73.2/45.3/33.9, avg 57.3 | Sourati et al. 2310.00996 | Confirmed (a22, c08) |
| 7 | Letter-string by alphabet, all four LLMs and humans | Stevenson et al. 2411.02348 | Confirmed (b24); sample 54 runs per model, adults 62, children 41 |
| 8 | PAM: N=1,329; .74 vs .83 and .79 vs .89; 85% vs 88% vs 92%; .96 | Lu, Ichien & Holyoak 2103.16704 | Confirmed (b14, c19). Note .74/.79 are the human values, PAM is higher |
| 9 | Khojasteh: MCQ raw 0.17 (Qwen, chance .25), best 0.46 vs 0.41; Llama 0.45 vs 0.28 | 2603.29997 | Confirmed (c20) |
| 10 | Analogical prompting GSM8K 75.0/75.8/76.7/77.8 | Yasunaga 2310.01714 | Confirmed ordering 0-shot, 0-shot CoT, 5-shot CoT, self-generated. CORRECTION below |

## 2. Corrections made

- c05 is wrong. It says "Share of errors using an alternate rule: GPT-3.5 38.59%, GPT-4 22%, GPT-3 5.81%." In the paper (Table 4, text) 38.59% is HUMANS; the three rows are GPT-3, GPT-4, Human (GPT-3.5 is not in Table 4). Also c05's human N=46 conflicts with 1,876 human samples in Table 2; do not use N=46. b23 has this right for the alt-rule column (humans 38.59%).
- b23 is wrong on the "incorrect-rule" column. It lists 55.48 / 42.67 / 34.24, which is the "Wrong" category. True "Incorrect rule": GPT-3 30.97%, GPT-4 32.67%, humans 14.67%. "Wrong": 55.48, 42.67, 34.24. "Completely wrong": 7.74, 2.67, 12.50. Fixed in K15.
- b26 says "GSM8K 5-shot CoT 75.0%". 75.0 is 0-shot; 5-shot CoT is 76.7 (c15 is right). The gain of self-generated exemplars over 5-shot CoT is only 1.1 points for GPT-3.5 on GSM8K.
- a21/b22 row labels in the Lewis & Mitchell table are garbled in the text extraction. Resolved by matching 31/36 to the paraphrase table: 0.89/0.61/0.75 is Webb's GPT-4; 1.0/0.72/0.86 is Lewis & Mitchell's own GPT-4.
- b20 "Overall human accuracy 0.753 in Table 2" is the human row, fine, but the GPT rows in the extraction are scrambled; do not quote model overall numbers from that table without reading the PDF figure.

## 3. Contradictions between sources

- Structure vs object similarity: ACME/Spellman-Holyoak/Krawczyk (soft, equal weight under high load) vs SME-line work (structure first). Not resolved; load level is the likely moderator (b12).
- Letter-string analogies: Webb 2023 (GPT-3 human-level) vs Lewis & Mitchell 2024 (drops on counterfactual alphabets) vs Webb 2024 reply (GPT-4 with code is human-level) vs Hodel & West (training-data contamination). Genuinely contested; K12.
- Creativity transfer: Shen et al. 2026 (+90-173% diversity from structured analogy) vs Liu et al. 2026 (random cross-domain sources give LLMs no overall benefit). Different methods (structured vs random source), so not a direct contradiction, but both rest on novelty ratings.
- a13 vs a04: ARCS activation (.22/.15/.11/.05) vs human 69/38/33/13 agree in rank only. Row-to-version pairing in the ACME table 5 is uncertain (a04 flagged).

## 4. Weak spots

- Almost all human evidence for the three-constraint claim comes from one lab (Holyoak and colleagues). No independent replication of the Anthar goal reversal was found; K02 is marked established only because ARCS/PAM simulations and the same-lab Exp2/Exp3 agree, so independent_sources is really about 1.5. Treat as one lab.
- Spellman & Holyoak samples are small (N=53 in Exp1) and use text-only cover stories with undergraduates.
- ACME/ARCS fits are ordinal (a12, b08). No fit statistic.
- No LLM study tests the goal-driven mapping reversal directly. This is the main hole for our purpose.
- Many LLM results are for GPT-3/GPT-4/early models; 2025-2026 reasoning models untested on ARN, StoryAnalogy or letter-strings in this evidence.
- Yasunaga and Shen/Liu are tangential; they do not test "choosing among mappings".
- Gulf War numbers (a08, a28) not available; seen only via the 1997 book chapter.

## 5. Seen only in snippets or second hand (opened:false)

a27 (Holyoak & Koh 1987), a28 (Spellman & Holyoak 1992), a29 (SME paper), a30 (Doumas 2008), c16 (Bhavya 2022, downloaded not read), c23-c25 (founding papers listed as not opened in c, though a/b opened them). Hodel & West (c07): numbers in figures only. Musker 2025 (b28, c11): exact accuracies not extracted. ARN demonstrations/CoT (c09): values in figures only. Wijesiriwardene (b30, c17, c18): no quantitative results.

## GAPS

1. Does an LLM reverse its mapping with the goal, as people do in Spellman & Holyoak Exp1 (trade vs membership)? No measured LLM replication found. Run it first, with order randomised, on our base model.
2. At equal tokens, does scoring candidate mappings on three separate lines (relation, feature, goal) beat a single holistic choice on ARN far-analogy and StoryAnalogy items?
3. Does a forced abstraction step (Khojasteh-style: describe roles, then map) fix the far-analogy-vs-near-distractor failure (33.9% on ARN) for current reasoning models, or only for small models?
4. What is the load threshold above which surface and relational similarity get equal weight (Krawczyk 2004), and does the same shift appear in LLMs as relation count rises?
5. Is the counterfactual letter-string gap a position-counting failure (fixed by code, Webb 2024) or a real analogy failure? Needs a code-free, counting-free counterfactual task.
6. How much of LLM story-analogy accuracy survives answer-order shuffling and paraphrase on 2025-2026 models? Lewis & Mitchell used only 18 stories; a larger set is needed.
7. Is keeping two consistent mappings alive (bistability, K05/K08) worth the tokens compared with greedy commitment? No LLM test exists.
8. Does the goal leak into mapping (attenuation, K03) in LLMs, and does telling the agent to ignore irrelevant structure change it?
9. Do Gulf War type social-role mappings (a08/a28) have usable numbers? Original 1992 paper not opened; needed for an agent test set.
10. Can independent labs replicate the Spellman & Holyoak 1996 effects with larger samples (online, N over 200)? None found.

## Gap search results

Evidence in evidence_d.jsonl (d01-d18; d17, d18 opened:false). Claims updated: K05 (now established), K07, K12, K13, K14, K18, K22; new K26-K30. Search APIs (arXiv, OpenAlex, Semantic Scholar) were rate limited, so most sources came from direct PDF downloads plus 5 WebSearch calls.

1. LLM goal-reversal (Anthar): STAYS OPEN. A 2025 survey (d06) still names goal-driven mapping as unsolved; no measured test found. Must be run by us.
2. Three-line scoring vs holistic choice at equal tokens: STAYS OPEN. Nearest: a hint-then-choose prompt raised accuracy for all 4 models on 18 stories (d04), but that is not a three-constraint score.
3. Forced abstraction on reasoning models: PARTLY OPEN. Hints helped 2024 chat models (d04); mechanism work (d15) says relation application is a bottleneck. No reasoning-model result on ARN far-vs-near found (d18 is adjacent only, unopened).
4. Load threshold: PARTLY OPEN. LLM accuracy falls with unique relations, steeper than humans (d10: OR 0.25 vs 0.61). No LLM test of equal weighting of surface and relation under load.
5. Counterfactual letter strings: MOSTLY CLOSED. Counting is the main cause: GPT-4+code equals humans (P=0.496), plain GPT-4 worse (P=8.9e-13), contamination controls pass (d01, d02). Numeric-counting failure also appears in Musker (d14). Contamination counter-argument (d03) not fully dead for older tasks.
6. Story analogy shuffling/paraphrase on 2025-2026 models: PARTLY OPEN. Order balanced, 2024 models reach .82-.85 (d04) but only 18 stories and no order-bias estimate; no larger set found.
7. Bistability worth tokens: STAYS OPEN. Human bistability now documented in detail (d07, d08) but no LLM or cost test.
8. Goal leakage in LLMs: PARTLY OPEN. Irrelevant structure leaks more in LLMs than humans (d12-d14) but the goal-relevance variant is untested.
9. Gulf War numbers: CLOSED (d07, d08, d09). Exp1 N=42 table 21/2/6/13; Exp2 N=50 88% consistent; Exp3 one-to-many 41% vs 0%.
10. Independent replication of 1996: STAYS OPEN. Only an adjacent independent test (d16).

Caveats: Inani enhanced-prompt column pairing inferred from a scrambled table; Colhoun sample size from a search summary.
