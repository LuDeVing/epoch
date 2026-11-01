# A05.05 Transfer of learning: cross-check and critique

Checked against full texts in D:/research_scratch/A05.05 (earlier extractions) and PMC pages re-fetched this session. 24 claims written to claims.jsonl (K01 to K24).

## Corrections made (10 number sets re-opened)

1. Gick and Holyoak 1983 Exp 2 (c13): c13 says 50% (14 of 28) solved "with a hint". The 1983 table shows analog-only 29% (8) before the hint, 50% (14) added by the hint, 79% (22) in total. The 2025 paper restated the added share as if it were the total. Use 29% unaided and 79% total (matches a08). Do not use c13 as a baseline.
2. Yasunaga et al. GSM8K (c17): c17 shifts the row labels by one (calls 75.0 "5-shot CoT"). The table has four rows per column: 0-shot 75.0, 0-shot CoT 75.8, 5-shot CoT 76.7, self-generated 77.8 for GPT-3.5-turbo (davinci-003 14.8 / 50.3 / 54.0 / 61.0). a23 and b22 are right; c17 and c18's labels are wrong. The PDF text extraction drops row labels, so the mapping is by row order; the paper's own sentence says self-generation beats both baselines.
3. Lewis and Mitchell Table 2 (a20, b20, c04): the extraction offsets the labels by one row. Values in order are humans 0.753, GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452. This matches a20. The model confidence intervals (about +/-0.02) look too wide for 6,840 samples each, so the model interval may be across prompt variants; flagged, not resolved.
4. Sala and Gobet (a17, b09): music 0.25 [0.17,0.34] k=64 passive, 0.03 [-0.07,0.12] k=54 active confirmed. WM passive is printed as 0.18, 95% CI [-0.09, 0.26], k=34, an interval that looks like a typo in the paper; WM active 0.05 [-0.05,0.15] k=40 confirmed.
5. Melby-Lervag, Redick and Hulme (b07, b08): confirmed. Near transfer g=0.80 [0.62,0.97] vs treated controls, 1.88 vs untreated; 87 publications, 145 comparisons; large studies (k=34) g=0.01 vs small (k=25) g=0.26.
6. ARN (b17, c07): human 94.1 vs model 39.6 far; 97.9 vs 75.0 near; partition average 76.9 / 73.2 / 45.3 / 33.9, overall 57.3. Confirmed.
7. Agent Workflow Memory (c19, c20): Mind2Web table confirmed: MindAct 36.2 / 30.1 / 18.6; AWM offline 45.1 / 33.7 / 32.6; online 43.6 / 33.9 / 35.5. +24.6% and +51.1% relative confirmed. Note the 12.0 absolute-point claim is the paper's.
8. Loewenstein, Thompson and Gentner (b16): 24/60, 8/37, 50/213, chi-square 7.08 and schema 21/38 vs 12/38 confirmed.
9. Trninic, Kapur and Sinha (b14): 38 per condition, initial-learning d=1.276 confirmed; the paper cites 76% (Kaminski 2008), 75% (De Bock 2011), 79% (this study) for abstract-training transfer, which means the "76% vs 44%" original and the later replication results are not all comparable cells. Treat K08 as contested.
10. Stevenson et al. (b21, c10): GPT-4o 0.85 / 0.63 / 0.48 and adults 0.88 / 0.91 / 0.89 confirmed. Children N is 42 in the text and 41 in the table (one drop). Claude-3.5 row reads 0.68 / 0.62 / 0.46 in the table (b21 gives the first two only).

Minor: Ren et al. (c27) GPQA-D base appears as 44.1 in one table and 41.8 in another; no effect on the claim. Huan et al. column identity for 30.2 / 45.3 / 60.0 was not verified. BoT (Buffer of Thoughts) Game of 24 columns could not be mapped from extraction (74.0 vs 73.2 for two baselines).

## Contradictions between sources

- Webb et al. 2023 (GPT-3 matches students) vs Lewis and Mitchell, Hodel and West, Wu et al. (breaks on altered forms). Differences in prompting, model version, and whether the test is on original or altered items explain much; not settled.
- Math SFT transfer: Huan et al. (fails) vs Ren et al. 2026 (works with verified long CoT). Different data quality and base model.
- Abstract vs concrete training: original and 2011 replication vs 2020 non-replication.
- Near-transfer size for WM training: 0.80 (Melby-Lervag, vs treated controls) vs 0.44-0.46 (Sala and Gobet). Different study pools and moderators.
- Hint lift: Gick and Holyoak 30% to 80% total, but the 2025 business problems reach only 8.7% and 37% hinted.

## Weak spots

- K02 and K04 rest almost entirely on one 1983 paper family (same lab, high school and undergraduate students). Independence is partial (Gentner supports the retrieval half).
- Agent-memory results (AWM, ExpeL, Voyager, ReasoningBank, BoT) are authors' own benchmarks, not equal-token, not seeds-controlled. None isolates transfer across classes from simple retrieval of near-duplicate tasks.
- No source in this set tests a lesson-reuse scheme across problem classes with a measured cost; this is where our own test must come from.
- The Webb et al. GPT-3 analogue results on Gick and Holyoak are single qualitative runs, not rates.
- LLM studies use 2020-2024 models (GPT-3 to GPT-4o, Claude-3.5). Little is known for 2025-2026 reasoning models on far-analogy tasks.

## Only seen in snippets or abstract

- Sala et al. 2019 meta-meta-analysis (b25): search summaries only.
- Detterman 1993 (b26): not extracted.
- Forbus, Gentner and Law 1995 (c29): not opened; MAC/FAC numbers come from the 1993 paper.
- Barnett and Ceci 2002 (a16, b11): abstract only.
- Perkins and Salomon 1992 (a04): secondary summary; the encyclopedia entry was not read.
- Hodel and West (c12): not opened; described in two other papers; arXiv id unverified.
- Lampinen et al. 2024 (a26): no accuracies extracted.
- ExpeL table value 70 (+/-0.7) (c21) unlabelled; Figure 6 numbers (c22) missing.
- Chess "about 0.5 SD" expert gap (b10) not rechecked.

## GAPS (most decision-relevant first)

1. How much does a lesson written for one problem class lift accuracy on a different class at equal tokens, for a current (2025-2026) frontier model? No study isolates this from retrieval of near-duplicates.
2. Does a code-checked mapping step (O7 with a typed mapping) raise precision of analogue reuse above model-judged matching, and at what token cost? (Precision is about 0.5 for GPT-4 in the only test.)
3. Do current reasoning models (o-series, Claude 4+, Gemini 2.5+ thinking) still fall below chance on far analogies in ARN-style tests, or did test-time compute close the gap?
4. Is lesson abstraction (slots, principle line) better than concrete worked lessons for LLM agents at equal tokens? Human evidence is contested (2020 non-replication).
5. Does a compare-two-cases step (schema induction from paired solved instances) raise LLM transfer as it does for people (45% vs 21%, 40% vs 22%)? No LLM test found.
6. What is the false-match cost of surface-based lesson retrieval (negative transfer), and how large is it for agents? Humans: retrieval 52% surface vs 7% relational; harm from wrong reuse is barely measured.
7. Is the memory-agent gain (AWM, ExpeL, ReasoningBank) due to cross-class transfer or to same-template reuse? Re-analyse by distance bucket.
8. Where does Barnett and Ceci's taxonomy (content, context, time gap) put the cheapest reliable gains for an agent? Read the full paper's dimension tables.
9. Do the Sala et al. 2019 pooled numbers (near g about 0.27, far about 0.12) hold in the full text, and how do they compare with the schema's view that near transfer is the only safe bet?
10. Does negative transfer or Einstellung from a stored lesson hurt a model on a problem where a plain attempt would succeed? (Links to the Einstellung subfield; no LLM measurement found.)

## Gap search results

Searches: web search quota ran out partway; arXiv, Semantic Scholar and OpenAlex APIs were rate limited. The work rests on about 11 full PDFs read (evidence_d.jsonl, d01-d18; d12 and d18 are unopened placeholders). New claims K25-K30.

**Closed**
- Gap 9 (Sala 2019): full text read. Published near g = 0.32 naive (k=99), corrected summary 0.21, active-control-only 0.24. Far g = 0.12 (k=119, CI 0.08-0.16), about 0.01 once placebo and bias are controlled, true variance zero. The 0.27 / 0.121 pair came from a preprint; do not cite it. (d11)
- Gap 6 (cost of false match), mostly: measured in four agent studies. Concrete traces cost up to -26.1 points on items the plain agent failed (ALFWorld), -12.7 (BabyAI); some baselines fall below no-memory (LifeMem airline 0.26 vs 0.32). Harm to already solved items is small (at most -2 points). (d03-d07, d17; K27)
- Gap 4 (abstract vs concrete), direction only: insight beats trajectory in three independent agent studies (MTL +3.7 vs +1.1; Hu +6.5 vs -9.5; LifeMem). No study matches tokens. (K25)

**Partly closed**
- Gap 1: MTL builds the store from other benchmarks, so +3.7 points (GPT-5-mini; +2.6 DeepSeek, +1.8 Qwen3-Coder) is cross-class, not near-duplicate. Not token matched, mid-tier models, Pass@3. LifeMem shows the lift shrinks with a stronger backbone (+15.3 vs +6.9). (K26, K30)
- Gap 2: only the model-judged side was found. LLM reranking and rewriting lost to embedding retrieval (0.598 / 0.608 vs 0.630). A typed code-checked mapping is still untested. (d02, K28)
- Gap 3: ARN numbers re-confirmed (39.6% is the all-model far average; GPT-4 far,far 57.1, far,near 29.1). No reasoning-model ARN result found. On ConceptARC reasoning models match humans on text accuracy (o3 77.1 vs 73.0) but 27% of correct o3 answers use unintended rules. (d09, d10, d15, K29)
- Gap 7: AWM re-bucketed by distance: step success +8.9 cross-task, +3.6 cross-website, +14.0 cross-domain, yet full-task success is 0.7-4.8% in all three. Cross-template WebArena also gains. ExpeL, ReasoningBank, Voyager not re-bucketed. (d08)
- Gap 10: no direct Einstellung test. Nearest: MTL analysis of cases where zero-shot succeeded and memory failed (three causes named), Hu RR (-2.0 to +4.6), MemHarness unadapted memory 82.4 vs 83.0 without memory. Harm to solved items looks small. (d03, d04, d06)

**Still open**
- Gap 5 (compare-two-cases step for LLMs): nothing found; searches returned only human work.
- Gap 8 (Barnett and Ceci full tables): publisher PDF closed; needs a library copy. (d12)
- Lewis and Mitchell Table 1/2 label order: PDF extraction still ambiguous; keep as inferred. (d13)
- Token-matched lesson control (gap 1), typed mapping (gap 2), current reasoning models on ARN (gap 3): need our own runs.

Gick and Holyoak 1983 correction (29% before hint, 79% total) was not re-read here; relied on the earlier cross-check. (d18)
