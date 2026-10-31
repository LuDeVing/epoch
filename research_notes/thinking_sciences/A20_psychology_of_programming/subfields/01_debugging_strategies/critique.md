# Critique: A20.01 Debugging strategies (cross-check)

## Corrections made (sources re-opened from arXiv PDFs this session)
1. Huang et al. 2024 (b23): oracle numbers were wrong (rows mixed). Paper Table 2: GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 GSM8K 95.5 to 97.5, CSQA 82.0 to 85.5, HotpotQA 49 to 59. Use a20/c05, not b23. Intrinsic numbers (75.9/75.1/74.7; CSQA 38.1/41.8; GPT-4 95.5/91.5/89.0) confirmed.
2. Self-Debug (c01, b24): on MBPP GPT-4 the rows are UT 80.6, UT+Expl 80.4, UT+Trace 80.2 (c01 swapped the first two). On TransCoder GPT-4 UT alone is 88.8; 90.4 is UT+Expl. Gain stays about +11 to +13. Spider Codex 81.3 to 84.1, no-execution results (Codex simple 57.6, trace 66.2; GPT-4 76.0/76.4; TransCoder 78.4) and the "within 0.1% after one turn" claim confirmed.
3. Agentless (a27, c11): 32.00% / 96 / $0.70 and 4.3/10.0/5.0% audit confirmed. StarShip is 23.67% resolved; the text says 90.0% file-level but the table row shows 79.0% file. The paper contradicts itself; quote with care.
4. Olausson (c04, a21, b20): 33.30 vs 52.60 and per-level figures confirmed. Ratios 1.05 (10 samples + 1 repair) and 0.97 (2 + 10) confirmed in the GPT-4 heatmap; GPT-3.5 cells are mostly below 1 (0.83 to 1.04). I did not confirm which dataset the heatmap shows.
5. Tyen (b21, b22, c06): 52.87, +23.53/+11.76, +43.92/+20.39, +36.86/+21.57 confirmed; 85/15 split of 300 traces per task confirmed; 2186 is the whole dataset.
6. DDI (a29, c18): 72.56 to 82.82, 84.1 to 92.1, phi4-reasoning E0 59.146 confirmed.
7. LDB (a23, b26, c12): all HumanEval numbers confirmed (73.8/81.1/82.9; 87.2/88.4/89.6; 91.5/92.1/95.1).
8. debug-gym (c13): Claude 3.7 37.2 / 48.4 / 52.1 confirmed. See contradiction 3.

## Contradictions between sources
1. Parnin and Orso 2011 vs Xia et al. 2016: null effect vs 11.38 vs 26.45 min. Plausible causes: tool accuracy, professionals vs students, real vs seeded bugs. Not settled. Also a14 and b10 list the NanoXML times in opposite group order (22:30 vs 20:16); neither is significant, but the direction is unknown. Neither source was re-opened.
2. Vessey internal: a08 gives faulty-module re-examination P=0.023, b03 gives p=0.007. a05 says 8 mistakes, b02 says 5 programmers made wrong fixes (compatible: 8 mistakes by 5 people). Original not re-opened (paywalled).
3. debug-gym: text says weak models lose with pdb from the start; the extracted appendix table seems to show GPT-4o 17.2 to 23.6 and Llama 2.4 to 4.0 (column order garbled). Unresolved.
4. Agentless file-level 90.0 vs 79.0 (above).

## Weak spots
- The founding human claims (Vessey) have no replication found. N=16, one program, expert label made after the fact. Gould 1975, Gugerty and Olson, Katz and Anderson were never opened (a11, a12, b07, b08, b09, c21, c22, c23 are opened:false).
- No LLM study directly tests Vessey's goal order (determine, understand, locate, repair, confirm). The evidence is indirect: locate and fix as separate skills (Tyen), location rate tracking solve rate (Agentless).
- Most LLM results use older models (GPT-3.5, GPT-4, Codex) and benchmarks near saturation (HumanEval, MBPP). Few use reasoning models; the one that does (debug-gym) is single-source.
- Alaboudi and LaToza 2020, Xia 2016, Parnin and Orso 2011, Kang 2025, RepairAgent, TraceCoder numbers were not re-opened.
- Evidence a, b, c overlap heavily (same Chen, Olausson, Huang, Tyen, LDB papers read by two or three agents). These are one source each, not independent confirmations; claims count independent sources, not evidence lines.
- c24 is a synthesis line, not evidence.
- Only seen as snippets: a11, a12, a13, b07, b08, b09, c21.

## GAPS
1. Does an explicit locate-then-patch step (S5) beat direct patching at equal tokens for current reasoning models, and does the gain survive when the model's own location is wrong 40% of the time?
2. What does a wrong self-made location cost versus no location? Tyen shows random location still helps on wrong traces but hurts correct ones. Is there a break-even location accuracy for code?
3. Do the self-repair-vs-resample results (Olausson) hold for 2025-2026 reasoning models at equal tokens? Any matched-token replication?
4. Does real tracing (printing values, LDB, pdb) beat prose reasoning on logic bugs for strong models, and when should the tool be unlocked (debug-gym says after failures)? Resolve the debug-gym table-versus-text conflict.
5. Is the "restart with summary after 2 failed rounds" rule (DDI) confirmed on frontier models and real repos, with token cost counted?
6. Why do Parnin and Orso and Xia et al. disagree, and does any 2020+ study of ranked suspect lists (including LLM-ranked) settle it?
7. Has Vessey's finding (experts keep hypotheses open, breadth-first, system view) been replicated or tested with modern eye-tracking or think-aloud studies, or contradicted?
8. Do candidate-cause lists (hypotheses) beat location lists for LLM agents, as Alaboudi found for humans (OR 6.24 vs 1.4)? Any LLM test?
9. What share of agent failures on SWE-bench Verified come from wrong diagnosis versus right location with wrong patch, with recent agents (2025-2026)?
10. Does confirmation (rerun reproduction script, regression tests) as the last goal reduce false-positive fixes, given Reflexion's 16.3% false-positive rate on MBPP?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d17); claims K20-K26 added; K07, K09, K10, K12, K13, K15 updated. Web search quota ran out early; arXiv search, Crossref and direct paper pages were used. The C drive was full, so scratch files went to D.

**Closed or mostly closed**
- Gap 4 (debugger tool timing): debug-gym tables re-read. pdb from the start hurts GPT-4o (19.1 to 17.2) and GPT-4o-mini (4.0 to 3.5) on SWE-bench Lite, helps o1-preview (10.7 to 30.2) and Claude 3.7 (37.2 to 48.4). pdb after 5 failed rewrites beats rewrite for all 6 models. The text/table conflict is only about Llama-3.3-70B (table 2.4 to 4.0, tiny base). InspectCoder: real debugger beats simulated by 8.0 and 4.6 points (Qwen2.5-Max only). K12 moves from contested to single-source.
- Gap 9 (diagnosis vs wrong patch): 60.8% to 69.1% of failures for capable models happen after the right functions are reached (Coherence Collapse, 16,758 trajectories). RGFL: of 209 failures, only 28 were file misses. Caveat: "right location" is a loose test (recall at least 0.5).
- Gap 5 (restart rule): full text read. HumanEval only, 18 mostly small models, gains up to about 10 points for weak models, none for strong, no frontier or repo test, token claim unsupported. Closed as "not shown for frontier agents".

**Partly answered**
- Gaps 1 and 2: Shi et al. 2026 (strong bash agents, 16,248 trajectories) found predicted locations did not help (-4.45 to +0.40 points, none significant) while gold causes did (+4.4 to +7.0). Loc2Repair and RGFL show gains for pipelines. Campos 2025 shows collapse when the location is mostly wrong. No break-even accuracy has been measured anywhere; no equal-token comparison of self-located vs direct patching. Open on those two points.
- Gap 8: still no LLM study testing candidate-cause lists against location lists. Indirect support: SGAgent suggestion step (+13.3 points), Shi et al. bug-cause hints. Human numbers re-confirmed from the primary text (OR 6.24 p=0.03 vs 1.4 p=0.64; N=20 analysed, 60 sessions).
- Gap 7: no replication of Vessey found. Naturalistic data (Alaboudi 2021, 11 pros, 89 episodes) and a 3-student think-aloud do not test it. Open.

**Still open**
- Gap 3: no matched-token self-repair vs resampling study for 2025-2026 reasoning models was found (search blocked by rate limits; not proven absent).
- Gap 6: Parnin and Orso and Xia 2016 full text not fetched (404, 403). No 2020+ ranked-list user study found. Open; K14 stays contested.
- Gap 10: no paper found measuring false-positive fixes before and after a reproduction rerun. SGAgent shows reproduction tests as a reranker (+6.6 points over regression tests) only.

**New cautions**
- Shi et al. use unusual model names and are a single preprint; treat K20 as single-source.
- SGAgent has internal number errors (154 vs 152 resolved).
- Campos text and table drops disagree.
