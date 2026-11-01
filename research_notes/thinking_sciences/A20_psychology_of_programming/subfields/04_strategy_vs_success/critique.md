# A20.04 Strategy vs success: cross-check critique

## Corrections made
Sources re-opened this session: Ko and Uttl 2003 PDF, Olausson 2024, Huang 2024, Agentless, SWE-agent.

Confirmed against the text: cluster sizes 20/40/15; bugs fixed 1.00/1.65/2.00 with SDs; Table 5 totals 28/29/25/16 of 75 and valueofoutlier 13/20, 12/40, 3/15; Table 6 experience 2.52/1.20/3.59, attitudes to experiment 4.89/4.68/5.53, to computers 5.65/4.76/5.98; inverted axes statistics test .40 vs .31; Olausson Table 1 (33.30/52.60 and per-level values) and 32/80 vs 7/80 inaccurate feedback; Olausson "up to 8%" and "34% relative"; Huang round values and oracle 84.3/89.7/29.0; Agentless 32.00%, $0.70, 18.33% at $1.62, 4.3% exact patch and 5.0% misleading (text); SWE-agent ablations 18.0/10.3/12.0/15.7, viewer 18.0/14.3/12.7, 90.5% to 57.2%, 52.0%.

Corrections:
1. c10: "shell-only GPT-4 Turbo 7.33%" is wrong. SWE-bench Lite shell-only is 11.00% with demonstration; 7.33% is shell-only without demonstration. SWE-agent is 18.00% (Lite) and 12.47% (full).
2. b05 numbers were checked and are right (computers attitude 5.49 vs 4.82; inverted axes 5.83 vs 5.08). b01's worry that Table 2 and Table 5 disagree is not needed: Table 5 totals 28/29/25/16 (valueofoutlier, pvalue, for-loop, inverted axes) fit b04 and the text. Inverted axes (16 of 75, 21.3%) is the least fixed.
3. Cluster 1 needs nuance: it was MOST successful on valueofoutlier (65%, p<.01) yet worst overall. "Depth-first did worst" holds only for the total.
4. Cluster 2 had the LEAST programming experience (1.20) and still beat cluster 1 (2.52). Experience does not map to success.
5. c13: use 4.3% (text) for exact-patch leakage; the 3.0% chart value is not confirmed.

## Contradictions between sources
- Ko and Uttl paper (per-bug knowledge predicts success) vs Ko thesis (experience, intelligence, statistics competence "played no role" in debugging success). Same data, different framing. So the headline is contested (K03).
- The common summary "no strategy was best" vs the paper: c2 and c3 beat c1 (p<.05); only c2 vs c3 is a tie.
- AutoSD is below the LLM baseline on Defects4J v1.2 (76 vs 87) and about equal on v2.0 (113 vs 110). "Competitive" is generous for v1.2.
- Olausson (self-repair gains modest or absent at equal cost) vs Self-Debug (large gains): differ by availability of execution feedback and by cost accounting.
- Agentless is best only among open-source systems; closed systems score higher (e.g. MentatBot 38%).

## Weak spots
- Founding human result: one study, N=75, one task, one language, students, 20 minutes, seeded bugs, exploratory, per-bug univariate tests without correction, partly circular cluster measures (authors warn). No direct replication found.
- No LLM study tests the actual claim (cluster strategies, relate to outcome with knowledge held fixed). All LLM links are analogies (information vs procedure).
- Most LLM evidence is 2023-2024 models. No 2025-2026 study was found (search quotas ran out for the earlier agents), so current-model behaviour is unknown.
- Agentless vs SWE-agent differ in model and cost accounting; leakage inflates both.
- Human feedback study: 16 people, about an hour each.

## Only seen in snippets or unread
- a01 (Ko and Uttl DOI page) and a02 (2020 ICPC paper) were never opened. b21 and c28 are absence-of-evidence notes.
- DebugBench (b17, c16-c18): Figure 4 values not read; the 75.0% / 62.1% figures were not re-opened by me. LDB (b18, c24) rests on abstract figures.
- b20 (Alaboudi and LaToza) was read through a summarising tool.
- c14, c15, c22, c25, c26 were not re-opened by me.

## GAPS
1. Does any 2024-2026 study cross strategy x information (fixed vs free procedure, with vs without execution or retrieved knowledge) on one model at equal tokens? If not, we must run the 2x2 ourselves.
2. For current models, does a scripted locate-then-fix route still beat free agent strategy once the base model is strong (SWE-bench Verified or newer, leak-filtered)?
3. Is there any LLM trajectory study that clusters agent behaviours into strategies and relates them to success (an analogue of Ko and Uttl), e.g. SWE-agent or OpenHands trajectory taxonomies?
4. Does the strategy effect grow with familiarity (the Ko and Uttl hypothesis)? Compare common vs rare-language or unseen-API tasks for models.
5. How much does a retrieved bug-class lesson help, and how much does a wrong or misleading retrieved fact hurt?
6. Do misleading comments or spec-code contradictions attract LLM attention as they did humans, and does a guardrail remove the effect?
7. Which papers cite or replicate Ko and Uttl 2003 (forward citations; end-user debugging work such as Ko and Myers)? The forward-citation check was never done.
8. Does forcing output inspection before the first edit raise fix rate for bugs that raise no error (inverted-axes analogue)?
9. When is a stop-and-rediagnose trigger after failed edits better than continued editing at equal tokens?

## Gap search results (2026-11-01, evidence_d.jsonl d01-d17)
Method note: the web search quota ran out. I used Semantic Scholar (citation graph, rate-limited), arXiv abstract pages and full-paper PDFs (read with pdftotext). Several queries returned nothing because of rate limits, so "not found" means not found, not proven absent.

1. Strategy x information 2x2 at equal tokens: OPEN. No such study found (d17). Nearest: SWE-Effi scaffold x model (d09), BC-Bench model vs harness (d10), SWE-Exp experience on/off (d02), SWE-Bench Pro requirements on/off (d05). We must run the 2x2 ourselves.
2. Scripted locate-then-fix vs free agent with strong models: MOSTLY CLOSED, answer is no longer a clear win (d12, d05, d11). Verified leaderboard: best fixed multi-agent workflow 75.2%, best autonomous single agent 73.2%; fixed no-agent pipelines significantly worse. Agentless failed on multi-file tasks in SWE-Bench Pro and was Python-only in SWE-PolyBench. Caveat: leaderboard data is observational and not leak-filtered; K10 downgraded to contested. A controlled test with a strong model is still missing.
3. LLM trajectory clustering like Ko and Uttl: PARTLY CLOSED. Bouzenia and Pradel (d01) compare action n-grams and anti-patterns of 120 trajectories by success; SWE-Bench Pro (d05) clusters failure modes with an LLM judge. Neither clusters strategies with knowledge held fixed, and both are confounded by difficulty and agent identity.
4. Strategy effect vs familiarity: OPEN. Only indirect: language gap (d11), repository familiarity (d04), rare-library retrieval (d14), rare DSL where model beats harness (d10). Nobody varied strategy across familiarity.
5. Retrieved bug-class lesson, and cost of wrong facts: PARTLY CLOSED. One good lesson gave +4.2 points (37.8 to 42.0, DeepSeek-V3, Verified); more lessons or forced citation reduced it (39.8 with two, 39.0 with four) (d02, d03). Deliberately false facts remain untested.
6. Misleading comments and guardrails: MOSTLY CLOSED for output prediction (d06, d07): about 24% average relative drop; an ignore-comments instruction did nothing under direct inference. Open: effect on first-edit location in repair tasks.
7. Forward citations of Ko and Uttl: CLOSED (d16). 56 citing papers in Semantic Scholar, none a replication, none an LLM test. Coverage is incomplete (Google Scholar not checked).
8. Output inspection before first edit: OPEN. No study. SWT-Bench (d15) shows self-made reproducing tests filter finished fixes (precision more than doubled for SWE-agent), which is a verifier role, not a pre-edit inspection step.
9. Stop-and-rediagnose trigger: OPEN. Backtracking search helps (+23% relative on Lite) but at higher cost (d13); stuck runs are expensive (d09); no equal-token trigger test.

Claims changed: K05 and K10 status changed; K04, K11, K14, K17, K18, K19 got new evidence ids and text; K20-K25 added. Net effect on the headline: still single-source for humans, and the LLM literature now supports "information beats procedure" (SWE-Bench Pro, SWE-Exp, Illusion) more firmly than "no strategy is best".
