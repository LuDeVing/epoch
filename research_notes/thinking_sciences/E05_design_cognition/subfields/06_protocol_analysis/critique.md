# Critique: E05.06 Protocol analysis (cross-check)

## Numbers re-opened and checked (local PDF/HTML text, this session)
1. Turpin 2023: accuracy drop "as much as 36%" and Suggested Answer -36.3% (few-shot -24.1%); 1 of 426 explanations mentions the bias; 0 of 234 generations. Confirmed (b21, a19).
2. Chen 2025: faithfulness 25% (Claude 3.7 Sonnet) and 39% (R1); RL plateau 28% MMLU and 20% GPQA; reward hack used >99%, verbalised <2%. Confirmed (a21, b23, c24).
3. Lanham 2023: under 10% answer change on lowest-AOC tasks; over 60% on AQuA; AOC LogiQA 0.44, HellaSwag 0.26; AQuA +15.32, HellaSwag -4.69. Confirmed (a20, b22).
4. Wurgaft 2025: 53% vs 49% (p=0.067), 125.1 vs 117.7 s (p=0.008), r=0.83. Confirmed (c03).
5. Gandhi 2025: ICC3 verification 0.66/0.65, backtracking 0.67, subgoal 0.70/0.77, backward chaining 0.55/0.40; LLM-LLM higher. Confirmed (c22).
6. Li 2025: 28 elements, 192K traces, 1,346 human traces; 240 recruited, 236 kept, 507 correct and 836 incorrect (3 ambiguous); 26% fewer elements for models; +9.7 and +18.8. Confirmed (b18, b19).
7. Borchers 2026: 630 utterances, cosine 0.16/0.19, beta -0.22/-0.44, float AUC 0.528. Confirmed (b17).
8. Zhang 2025: inter-coder 79.5%, expert r 77.02%, R 9.7 vs 4.3, F 18.9 vs 9.2, S 10.6 vs 29.3, Formulation 31.7 vs 16.3, PP 30.7 vs 15.3, PS 6.7 vs 10.5 (p=0.001). Confirmed (a08-a10, b11-b13). Correction: in the unconstrained table Be is 10.5 vs 13.6 (p=0.042), so "static shares match" is not true for every issue; Bs 6 vs 10.6 is p=0.370 unconstrained.
9. Sakib 2026: body gives 80.2% (LLM) vs 85.7% (human) at category level and 52.5% vs 74.7% subcategory. Confirmed. CORRECTION: the abstract says "up to 85.7% for GPT-4.1", but the body gives 85.7% as the HUMAN inter-rater figure and Experiment 2 tops at 85.1%. Treat 85.7% as the human figure; the LLM best is 80.2% (Exp 1) to 85.1% (Exp 2). Records a11 and c06 should be read this way.
10. Fox 2011 (r=-.03, 94 studies, ~3,500 participants): not re-opened beyond abstract; accepted because b01 and c04 are two independent reads of the same abstract text, so this is one source, not two.

## Contradictions and weak spots
- Sakib abstract vs body (above). Also c12: share figures for Tajik cells are inconsistent (23% / 28% / 3%); use counts only.
- Dunivin abstract says kappa >= 0.6 on 8 of 9 codes; table recount gives 7 (c13).
- Zhang: the LLM matched humans on static shares but reversed on problem-solution crossings; authors say LLMs stay in one space. The prompt names the issue types, so the match is partly circular (a27).
- Human-side foundations are thin: Ericsson and Simon (a16, b24), Nisbett and Wilson (a17, b25), Kuusela and Paul (b26), Dorst and Cross (a15), Kan and Gero (a14), Waterman and Newell (c29) were NOT opened. No numbers from them are claimed.
- The three Gero 2011 evidence lines (a01-a03, b05, b06) are one paper. Independent human design-protocol evidence is essentially only Hay 2017 (one review of 47 studies, no reliability data).
- Reliability is almost all percent agreement, not chance-corrected (Zhang 79.5%, Sakib). Only Dunivin, Kirsten, J Learn Analytics (kappa 0.65 human) give kappa.
- Faithfulness studies use multiple-choice hints where CoT is not needed; they test report completeness, not design-style protocol coding.
- No study found that uses FBS or linkography coding on LLM traces with a human-validated reliability number and a test of whether the coded process predicts outcome quality. Crossref titles (a24) were never opened.
- Evidence of effect on outcomes (b13, b27) cannot separate process style from longer reasoning.

## Seen only as snippets or abstracts
a14, a15, a16, a17, a18, a24, b10, b24, b25, b26, c08, c29; b01-b04 and c04 are abstract-level.

## GAPS
1. Does coding agent traces with a fixed human-derived scheme (FBS issues, or Li's 28 elements) predict answer correctness at equal tokens, i.e. is any code share (for example problem-space steps, evaluation steps) a usable signal for our agent?
2. What is the chance-corrected (kappa) agreement of an LLM coder on FBS codes for design talk, per code, against two trained humans? Zhang gives only 79.5% raw.
3. Is the Zhang reversal (fewer problem-solution crossings in problem-driven LLM runs) real in other models and with unrevealing prompts, and do forced crossings improve design quality?
4. Does Ericsson-Simon style non-reactivity hold for LLMs: does requiring a think-aloud trace change accuracy vs silent answer at equal tokens, and does requiring explanation help as in Fox et al.?
5. How faithful are traces of current reasoning models on open-ended design or ill-structured tasks (not multiple-choice hints), and does a scaffold raise mention rates of hidden influences?
6. What are the original human numbers (Chen 2023, Jiang Gero Yen 2014, Kan and Gero entropy 2007, Dorst and Cross 2001) that the LLM studies compare to? Open them.
7. Are there replications or failures of linkography/entropy measures as predictors of design outcome, and have the 2023-2026 LLM-linkography papers (a24) reported validity numbers?
8. Is Fox et al.'s full-text moderator result (task type, instruction wording, ill-structured tasks) available, and does it include any design tasks?
9. Does LLM-LLM coder agreement exceeding LLM-human (Gandhi) indicate shared bias, and does mixing coder model families reduce it?
10. Does Li's trace-structure guidance (+9.7 on ill-structured) replicate outside the authors' trace pool and at equal tokens?

## Gap search results (evidence_d.jsonl, d01-d18)
Search tools: the OpenAlex and Semantic Scholar APIs were rate-limited and arXiv export returned 429, so work used 8 WebSearch calls plus direct page fetches. Records d14, d15, d17, d18 are snippet-level (opened:false).

1. Gap 1 (code share predicts correctness at equal tokens): STAYED OPEN for coding schemes. Related: Ballon 2026 (d09, d10) shows trace content, not length, carries signal (length-matched random tokens -3.9 to +4.2% vs original +18.1 to +33.1%), and longer traces correlate negatively with accuracy. Valmeekam (d11) says trace validity and accuracy can diverge.
2. Gap 2 (kappa of LLM coder on FBS): STAYED OPEN. Sakib 2026 (d04, d05) re-opened: Table 8 kappa unreadable; only percent (80.2% category, 52.5% subcategory vs human 85.7%/74.7%), per-code 20.8% to 93%. Not FBS.
3. Gap 3 (Zhang reversal replication): STAYED OPEN. Only Guo 2024 (d13), humans with AI, 20 novices; not the same question.
4. Gap 4 (non-reactivity for LLMs): STAYED OPEN. Luo 2026 (d12) abstract only, no equal-token silent comparison.
5. Gap 5 (open-ended faithfulness): PARTLY CLOSED. Walden (d06), Young (d07) show wide spread (39.7% to 89.9%) and judge dependence (about 13 points), but still multiple-choice; Lewis-Lim (d08) is soft reasoning, abstract only. No scaffold test.
6. Gap 6 (original human numbers): PARTLY CLOSED. Kan and Gero 2007 ICED opened (d01, d02). Dorst and Cross 2001, Chen 2023 and Jiang Gero Yen 2014 not opened (fetch failures) (d15).
7. Gap 7 (entropy validity): CLOSED toward negative. Original: low-scoring sessions had higher entropy; only entropy change is claimed. Fuzzy Linkography (d03) reports no validity numbers. No replication found.
8. Gap 8 (Fox moderators): STAYED OPEN; snippet only (d14), no design tasks known.
9. Gap 9 (LLM-LLM agreement shared bias): PARTLY CLOSED indirectly. Pombal 2026 (d16) self-preference over 50% on objective rubrics, ensembling helps but does not remove. No direct coder-agreement study.
10. Gap 10 (Li replication): STAYED OPEN (d18 snippet).

Corrections: Walden's reliance judge kappa is only 0.26 (hint presence 0.80). The Luo MATH numbers quoted in a search summary were not verified and are not used in claims.
