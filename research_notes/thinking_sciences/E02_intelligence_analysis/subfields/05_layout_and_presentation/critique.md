# E02.05 Layout and presentation: cross-check critique

## Corrections made (sources re-opened this session)
1. Liu, Wang, Chen (2023) table perturbations. Re-read arXiv 2312.16702 Table 1. Row order is Original, +Shuffle, +Transpose, +Transpose&Shuffle. So 52.21 (-12.25%) is SHUFFLE and 51.14 (-14.05%) is TRANSPOSE for direct prompting. Python agent: shuffle 47.91, transpose 12.45 (-77.73%), both 8.96. Evidence b11 swapped the labels ("transposed 52.21, shuffled 51.14"); a20 and c07 are right. Fix b11. Note that b11 said it "reconstructed the mapping"; that was the error source. Also, the big effect of transposing is for the code agent, not direct prompting (shuffle and transpose are about equal for direct prompting).
2. Dhami et al. (2024) re-opened: chi2(2)=9.43, p=.009, phi=.24; CRT 0.51 vs 2.32, t(221)=13.68, d=2.05; credibility chi2=0.15, p=.927. All confirmed. The per-layout percentages (HypCol 61.8%, HypRow 39.2%, HypText 67.3% confirm-only; 38.2/60.8/32.7 for B) do NOT appear in the page text (cell counts are in an image table). They are consistent with each other and with the n's (34/55, 20/51, 37/55) but I could not verify the counts. Treat as probable, not confirmed. The text itself says only that most HypRow chose B and most HypCol/HypText chose A.
3. PRISM (Lee, Kang, Shin 2026): 58.1, 57.2, 58.2, 58.0, 63.2, 71.3, 63.8, 70.5 all confirmed in the paper text.
4. Sui et al. 2024: HTML 67.00% size detection and 65.43% best average confirmed. He et al. 2024 (42%, 200%, 300%) confirmed. Chen et al. 2024 R-GSM 94.1 to 85.0 confirmed. Lost in the Middle 56.1% closed-book confirmed. Tam et al. 100% answer-first and 38.15% gap confirmed.
5. Sclar et al.: the abstract says up to 76 points (LLaMA-2-13B) and GPT-3.5 up to 56 with median spread 6.4; median task spread 7.5 points. Evidence b15 says "about 10 points on average across 50+ tasks"; I could not find "10" in the text, so use the 7.5 median. a23 "about 20% of tasks show a large spread" not re-checked.

## Contradictions and tensions
- Human layout study says ACH-style matrix (hypotheses in columns) is no better than prose; LLM pipeline PRISM says the ACH matrix adds only +0.8. Both point the same way: the matrix orientation Heuer taught has little support. But PRISM's matrix is evidence-by-suspect and was not compared with the other orientation.
- Dhami Study 1 (students: 56.5% confirm-only) vs Study 2 (analysts: 19.4%): the bias depends on the sample, so the "layout fixes bias" story may be a student effect.
- Best serialization conflicts across studies: HTML (Sui, GPT-3.5), JSON (He, GPT-3.5), Markdown (He, GPT-4), text over image (Deng). No single rule.
- Format-sensitivity size shrinks with model strength in Chen and He (GPT-4 loses less) but Sclar finds no shrink with size. Mixed.
- Tam: structured output hurts reasoning; Sui/Deng: structure helps table parsing. Input structure and output structure act differently.

## Weak spots
- The whole human layout claim rests on ONE study (Dhami 2024), not preregistered, two hypotheses, one decisive task, mechanism untested.
- PRISM is one 2026 preprint on one task (MuSR murder mysteries), ablation without repeat seeds reported in the evidence.
- LLM table studies mostly use GPT-3.5/GPT-4 era models; no 2025-2026 frontier model reasoning-trace results on layout.
- No LLM study maps to the human hypothesis-evaluation task.

## Only seen in snippets or summaries (opened:false)
a15 Kleinmuntz and Schkade 1993, a16 Schkade and Kleinmuntz 1994 (60 MBA, from snippet), a17 Larkin and Simon 1987 (fetch failed), b08 Maegherman 2020 (N=191, via 2024 summary), b09 Mandel 2018, b23 classics, b24 gap, c22, c23 (derived by a prior agent). Claims K07 rests on b08/b09 and b07 abstract only.

## GAPS
1. Does hypotheses-in-rows vs hypotheses-in-columns change an LLM's confirm-only choice on Dhami's Task 1 (and with reasoning models)? No direct study exists.
2. Is the row advantage a processing-order effect (one hypothesis at a time) or a layout effect? Test sequential per-hypothesis calls vs one-shot matrix at equal tokens.
3. Does the row effect hold with 3-6 hypotheses and more than 12 evidence items, and does it survive a preregistered replication with non-student samples?
4. For current reasoning models, how large is the format-spread (FormatSpread) on an evidence-evaluation prompt, and does an explicit chain of thought remove it?
5. Does an ACH matrix step add anything beyond evidence filtering and profiling on tasks other than MuSR (e.g. our ARC or BrainTeaser items)?
6. Do the counts behind Dhami's per-layout percentages (OSF osf.io/hcdp3) match the derived 61.8/39.2/67.3%? Pull the OSF data.
7. Does a layout-normalizing step (detect and fix orientation) before S4 reduce variance, as NORM did for tables (58.66 vs 59.50)?
8. Does position of decisive evidence (start, middle, end) in the S4 table change verdicts for modern long-context models?
9. Do Schkade and Kleinmuntz 1993/94 display-organization findings (matrix organized by attribute vs alternative) predict the hypothesis-row advantage? Read the originals.
10. Does cell-by-cell scoring harm dependency reasoning compared with holistic per-hypothesis scoring in an LLM?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d20); claims.jsonl now has K24 to K30. Web search, arXiv, Semantic Scholar and OpenAlex APIs were rate limited or exhausted, so some items are search-summary only (marked opened:false).

1. Rows vs columns on an LLM (Dhami Task 1): STAYS OPEN. No study found. Nearest is Failing to Falsify (d05, d06): 11 LLMs favour confirming tests, Dual-Goal prompting lifts rule discovery 42% to 56%. That is test selection, not layout.
2. Processing order vs layout (sequential vs one-shot): STAYS OPEN. No study found (d18).
3. 3-6 hypotheses, more items, preregistered non-student replication: STAYS OPEN. No replication found (d18). Study 2 had only the ACH layout. A 2016 pilot with hypotheses in columns (N=64) gave 47.6% confirm-only (d02, d03).
4. Format spread on reasoning models and CoT: PARTLY CLOSED, negative. Brittlebench (d08, d09): CoT cut the drop only 2.79% to 2.38% (Claude Opus 4.5); perturbations explain up to half of variance; ranking changes in 63% of cases. ToRR (d10): no format wins, 35 configs per example. Not measured on layout or on reasoning-mode toggles across many formats.
5. ACH matrix on ARC or BrainTeaser: STAYS OPEN. No data beyond PRISM (+0.8, MuSR). ACH-Grounding (d17) is a design with no results.
6. OSF counts behind 61.8/39.2/67.3%: STAYS OPEN, now diagnosed. osf.io/hcdp3 root has no files; the child holds only the 2016 technical report and a 64-row CSV with no layout column (d01, d03). Request the raw data from the authors. The percentages remain unverified.
7. Orientation-normalizing step before S4: STAYS OPEN. Only the NORM table result (d19, summary only). No evidence-matrix test.
8. Position of decisive evidence: PARTLY CLOSED. Veseli 2025 (d11): U-shape strongest up to half the window, retrieval drives most of the reasoning bias. 2605.23170 (d12): model-specific, from no drop (DeepSeek-V3.2) to -94 points (Qwen2.5-7B at 64K); N=50, one seed. Claim K14 moved to contested. No test on short tables with frontier reasoning models.
9. Schkade and Kleinmuntz originals: PARTLY CLOSED. Only abstracts could be read (d14, d15). They support "layout steers strategy" but do not predict hypothesis-in-rows. Full text is paywalled.
10. Cell-by-cell vs holistic scoring in an LLM: STAYS OPEN. Nearest is essay scoring (d16): holistic QWK about 0.6 vs analytic 0.2 to 0.4. No dependency-reasoning test.

Net: no gap fully closed. The human row-layout claim is still one study; the LLM side has no direct test. New items change K14 to contested and add K24 to K30.
