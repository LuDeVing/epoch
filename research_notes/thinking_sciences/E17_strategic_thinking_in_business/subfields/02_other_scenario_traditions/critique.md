# Critique: Other scenario traditions (E17.02)

## Verification (sources re-opened this session)
Re-opened: Csaszar et al. (arXiv 2602.01684), Lorenz and Fritz (2602.08889), Sela (2604.26561), Soleimani (2512.07867), Fruhling et al. (2602.08565), Fed SCAP results (May 2009), Ritchey GMA PDF.
Confirmed: 870 comparisons, 346 managers, 3 MBA investors, rho 0.74/0.45/0.19/0.04, 0.67 and 0.77 ensembles; Lorenz r 0.97/0.97/0.91 and 0.95/0.98/0.93, anonymised 0.30/-0.22/-0.40, plausibility coverage 39-80%, 16.6 vs 5.0 pp, citing panel mean 0.6% vs +45.4/+49.4; Sela 70.9 to 46.1 and 46.0 to 22.9, zero vote changes in 10 runs; Soleimani eta-sq 0.87, 1.6 pp, 4-7x; Fruhling 86-110 and 27-47 and 290 experts; SCAP $600B, $185B, 10 of 19; GMA 2,304 and over 500,000.

## Corrections
1. a19 (Csaszar replication): the preregistered replication had 26 projects (after 3 were removed), covered LLMs only (no humans), had lower absolute correlations, and model-rank consistency across the 19 shared models was about 0.54. "Similar results" is only qualitative. Do not cite it as a human-vs-LLM replication.
2. a18: the 0.19 "Prolific crowd" is the aggregate ranking of the 346 managers, not a separate group. The 0.04-0.45 human range is the three MBA investors only. The paper says confidence intervals are wide, and 0.04 and 0.19 are statistically indistinguishable from zero.
3. a16/c20: $185B is the buffer before Q1 2009 capital actions; c20 also gives $74.6B after actions. Both are right; label which one is used.
4. a03/a01: Kahn's Thinking About the Unthinkable date differs (1962 vs 1965) between two Wikipedia pages. Unresolved.
5. b24 (UI persona panel): arXiv id 2607.28439 returned a page (HTTP 200) but the arXiv API gave no record. Numbers kept as seen by the earlier agent, not re-verified here.

## Contradictions and overlaps
- Many evidence lines are duplicates across agents (Lorenz a21-a24 = b09-b13 = c03-c05; Bertolotti a25 = b06 = c01; Csaszar a18-a20 = c08-c10; Soleimani b17-b19 = c11-c12; Sela a26 = b23 = c16). Each paper is one source. independent_sources counts papers, not lines.
- Lorenz says LLM panels match human panel A closely (5.0 pp for GPT-5.1), yet Barrett says quantities are up to 70% lower and Lorenz own sea-level case is about half. Reconciliation: agreement holds on bounded percentages with evidence; divergence on unbounded quantities and long horizons.
- Delphi helps in Lorenz (r high), but the Barrett spread-vs-correctness test is only p = 0.053 and Sela shows feedback rounds hurt small models. No source ablates rounds directly, so rounds are not shown to add value over one evidence-rich pass.
- Csaszar: ensembles do not help. Lorenz and Sela: model diversity helps against consensus. Different targets (ranking accuracy vs spread), not necessarily in conflict.

## Weak spots
- Almost all human-tradition evidence (Kahn, Berger, Wack, Delphi, morphological analysis) comes from Wikipedia or one Ritchey PDF. No primary Kahn, Berger, or Dalkey and Helmer figures were read (a12, b26 unopened).
- Rowe and Wright 12 to 2 vote count: abstract snippet only (b01, opened false).
- Basu and Schroeder 3-4% error is a single business case via Wikipedia.
- All LLM studies are 2024-2026 preprints, mostly single-team, small samples (30 ventures; 120 deliberations; 9 human experts). Mostly not peer reviewed.
- No study tests morphological analysis, La Prospective, or Kahn stories with LLMs (searches negative, small search budget).
- Financial stress test evidence is about the 2009 SCAP only; no later accuracy evaluation of stress scenarios was read.

## Only seen in snippets
b01 (Rowe and Wright), a12 and b26 (Dalkey and Helmer), b25 (Ritchey 1998), c22 and c23 (synthesis and search notes).

## GAPS
1. Does a Delphi-style feedback round add accuracy beyond one evidence-rich independent pass plus averaging at equal tokens? No ablation of rounds exists.
2. Do LLM forecasts built from stories or scenario branches (Kahn style) beat plain probability answers on scored questions? No study found.
3. What are the primary Delphi numbers (Dalkey and Helmer 1963 rounds, error by round) and later meta-analyses of Delphi accuracy (Rowe and Wright details, Sackman critique)?
4. Can an LLM do cross-consistency assessment for morphological boxes reliably (agreement with human workshop judgments, share of valid configurations kept)?
5. How well did the scenario traditions actually forecast (Kahn Year 2000 hits and misses; Shell scenarios; La Prospective)? Need primary texts and hit-rate counts.
6. Does the Csaszar ranking result hold in other domains and for agent scaffolds (not single calls), and does a scaffold beat the best single model at equal tokens?
7. How to anchor LLM scenario severity so it follows numbers and not prompt wording (Soleimani)? Does a text-to-number consistency check fix it?
8. Do stress-test style adverse scenarios with stated probability anchors improve agent decisions versus baseline-only reasoning at equal tokens?
9. Does model heterogeneity beat persona heterogeneity on forecasting accuracy (not only on spread) at equal tokens?

## Gap search results
Search tools were limited: the shared WebSearch budget ran out after three calls, the arXiv, OpenAlex and Semantic Scholar APIs returned empty bodies or 429, and RAND and ScienceDirect returned 403/404. Evidence is in evidence_d.jsonl (d01 to d16). Claims K20 to K24 added; K01, K03, K07, K10, K12, K15, K17, K19 got extra evidence ids.

1. Delphi round vs one evidence-rich pass at equal tokens: PARTLY CLOSED, still open for the equal-token test. Schneider and Schramm (d01, d02): one round helps only across different models (log loss 0.501 to 0.481, p 0.017, one cell of four), not for same-model groups. InfoDelphi (d03, d04): 2 rounds best (Brier 0.178), 3 rounds worse (0.196), 1 round 0.206, rationale sharing is the main driver. Neither matches tokens against independent samples averaged. Lorenz (d13) has no round data. Sela (d14) shows rounds hurt 7-9B models.
2. Story or scenario forecasts vs plain probability: PARTLY CLOSED. One scripted-narrative prompt was worse for 11 of 12 models (d05). Kahn-style branch-then-probability is untested.
3. Primary Delphi numbers: OPEN. RAND blocked; only secondary sources (d06, d07). Rowe and Wright 12-2 and 5-1 vote counts now confirmed from the abstract listing, still not full text.
4. LLM cross-consistency for morphological boxes: OPEN. Negative search again (d10, d11); search recall was low.
5. How the traditions actually forecast: OPEN. Only anecdote for Shell (d08); no hit-rate count for Kahn Year 2000 (d09). Date discrepancy in correction 4 mostly settled: Thinking About the Unthinkable is 1962, On Escalation is 1965.
6. Csaszar result in other domains and scaffolds: OPEN. Paper tests one domain, single calls, no token matching (d15).
7. Anchoring scenario severity: PARTLY CLOSED. Reconciling stated changes against levels and a fixed baseline catches contradictions; severity itself still follows prompt wording; authors recommend prescribing the severity path (d12). No test of the check as a fix.
8. Probability-anchored adverse scenarios improving agent decisions: OPEN. Only human stress-test history found (d16): EBA adverse case was -0.6% in 2009 and 2010, -4.0% in 2011.
9. Model vs persona heterogeneity on accuracy: PARTLY CLOSED. Mixed-model groups gained from feedback while same-model groups did not (d01); InfoDelphi used one model throughout (d04). No direct persona-vs-model accuracy test at equal tokens.
