# Critique: E11.08 Judicial bias and noise (cross-check)

## Corrections made (sources re-opened this session)
1. Zheng et al. 2023 (arXiv 2306.05685): b17 confirmed. GPT-4 65.0% (30.0% first, 5.0% second), GPT-3.5 46.2% (50.0% first), Claude-v1 23.8% (75.0% first), few-shot 65.0% to 77.5%.
2. Wang et al. 2023 (arXiv 2305.17926): b16 confirmed. GPT-4 conflict rate 37/80 = 46.3% for Vicuna-13B vs ChatGPT; Vicuna wins 66 of 80 queries under ChatGPT as judge.
3. Chen, Moskowitz, Shue 2016 (full text): b10/a12 confirmed. 0.5 pp unconditional, 1.1 pp non-extreme judges, 3.3 pp moderate judges same-day same-type; "two percent" of asylum decisions reversed; "up to nine percent" for loan officers.
4. Kleinberg et al. 2018: b11 figure 82.9% for most lenient quintile confirmed in the text (other figures not re-checked).
5. CORRECTION to b04: it says completed cases per session range "2 to 283". The Glockner text reads "2 and 283", which is the number 28 with footnote marker 3. a09 ("2 to 28") is right. Use 2 to 28.
6. Hagger et al. 2016 N: a08 says 2,142 (via Glockner), b14 says 2,141 (abstract). Use 2,141 (abstract); the difference is a one-person discrepancy in the secondary source.
7. Glockner effect size (OR 35, d = 1.96; depletion meta-analysis d about 0.10 to 0.25) confirmed from the extracted Glockner text (a08/b03 agree).
8. b07: the review says the prosecutor-demand gap is "8 months longer" but the means (24.41 vs 17.64) differ by 6.77. Left as a flagged source-internal inconsistency; do not quote "8".
9. a20/a21 (Englich 2006, Tversky and Kahneman 1974) were never opened. Their numbers stay unverified and are not used in claims as numbers.

## Contradictions between sources
- Danziger authors (a06) say the effect survives representation controls; Weinshall-Margel and Shapard (a05) and Glockner (a07) say order is not random and the effect is mostly a scheduling artifact. Neither side's full tables were available (supplement tables S1 to S15 not opened). Status: contested.
- LLM anchoring: c09 and b21/b23 say LLMs anchor as much as or more than humans; b20 finds a lower index (0.45) than the human dataset (0.61). Differences in task, model and index definition explain much of this.
- Mitigation: b19/c12 report that self-help works; c10 reports that some self-improving prompts make anchoring worse. Model size and bias type decide.
- Temperature: c05 says higher temperature lowers measured bias because noise masks it; c13 says temperature lowers consistency by 12.1 points. These are consistent (bias and noise trade off) but should be separated.

## Weak spots
- Almost all human field findings are observational (Danziger, Eren and Mocan, Chen et al. asylum). Only the loan-officer part of Chen et al. is randomised.
- The Noise book items (a16 to a19) were read through summaries, not the book. Clancy 1981 numbers come from a Wikipedia summary (b12).
- Many LLM judicial-bias papers use vignettes or synthetic facts; real-court validity is untested (c04 reports 219% MAPE against real sentences).
- Single-source claims: K04, K06, K07, K08, K11, K15, K16, K19.

## Only seen in snippets or not opened
a20, a21, a22, a23, a24, b01, b06, b08, b09, b14, b15, b23, b24, b25, b26, c19 to c25. Numbers from these (Bystranowski d = 0.58 / 0.91, Vohs d = 0.06, the 2026 diagnostic anchoring paper, radiology and clinic time-of-day) rest on abstracts only.

## GAPS
1. Does an LLM agent in a long context show late-position drift in decision rate (a hungry-judge analogue)? c21 found zero studies.
2. Does a swap-order plus verdict-first format cut flips at equal token cost, across judge models other than Gemini-2.5-Pro (K11, K12)?
3. Do Danziger supplementary tables (S1 to S15) and the DLA reply give effect sizes once representation and deferrals are controlled? What is the residual effect?
4. Is there any pre-registered or randomised replication of order effects in real judicial decisions (not asylum or loans)?
5. Which debiasing steps (counter-anchor, blind label, relative scales) reduce LLM anchoring at equal tokens, and when do they backfire (K14, K15)?
6. How large is occasion noise vs level vs pattern noise for LLM judges on legal tasks (a variance decomposition on the Noise model)?
7. Does averaging k independent samples remove noise without removing real judgment, in legal vignettes? (Link to Debiasing and Retrieval/ensemble subfields.)
8. Do real-court outcomes (sentences, damages) show the anchoring size predicted by the meta-analysis (d about 0.58), outside vignette studies?
9. Does the numeric translation step (K20) generate most of LLM sentence variance, as in humans?

## Gap search results (gap searcher, 2026-11-19)
Search tools were limited: WebSearch budget exhausted, arXiv/OpenAlex/Semantic Scholar APIs rate-limited (429), publisher and PMC full text blocked. Work was done from direct arXiv fetches and PDFs. New evidence is in evidence_d.jsonl (d01 to d16, all opened).

1. Late-position drift in LLM agents: STAYS OPEN. No study of decision-rate drift over a sequence of cases. Nearest result is Lost in the Middle (d05): U-shaped retrieval accuracy, GPT-3.5 drops over 20% mid-context. New claim K27 (contested) with a cheap test.
2. Swap-order plus verdict-first across other judges: CLOSED, answer is no. Verdict-first cut flips only for Gemini-2.5-Pro (56.0% to 6.9%); it raised flips for GPT-4o (24.0% to 33.0%) and Gemini-2.0-Flash (46.0% to 90.0%). K12 changed to contested and rewritten. Caveat: judge-to-row mapping in the Direct rows was inferred (d09). Position bias also changes direction by task (d07, K23).
3. Danziger supplementary tables and residual effect: STAYS OPEN. Full text, tables S1 to S15 and the reply body were not retrievable; only the abstract was read again (d13). K01 and K05 stay contested.
4. Pre-registered or randomised real-judicial order replication: STAYS OPEN. None found. Only archival evidence (d14, d15).
5. LLM anchoring debiasing: PARTLY CLOSED. Ignore-instruction, chain-of-thought, principles and reflection fail (d02); knowledge enhancement backfires (34.7% to 50.5%, d03); Anti-DP (own criteria first) and a bracketing counter-anchor help (d03, d04, d02). Not tested at equal tokens. K15 rewritten.
6. Variance decomposition for LLM judges on legal tasks: STAYS OPEN. Method template exists for human annotators (pattern noise largest, d11); occasion noise and order flips are measured for LLMs (d06, d08) but not on legal vignettes. New claims K21, K22, K25.
7. Averaging k samples in legal vignettes: STAYS OPEN. Self-consistency helps on reasoning benchmarks (d12, abstract only) and the judge audit recommends order averaging then repeats (d10), but there is no legal test. K24 single-source.
8. Real-court anchoring size versus d = 0.58: STAYS OPEN, with a hint. Archival coding gives Cramer's V = 0.186 (d15) and an old bail study (d14, secondary). K26 contested.
9. Numeric translation step as the source of LLM sentence variance: STAYS OPEN. No new evidence found; K20 unchanged.

Corrections: K12 was too strong (generalised from one judge). Evidence d08/d09/d10 URL points to the proceedings root because the paper was read from a saved PDF; the exact page link should be added when the arXiv id is known.
