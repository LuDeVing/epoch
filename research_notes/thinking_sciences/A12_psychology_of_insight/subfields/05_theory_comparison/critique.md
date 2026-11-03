# Critique: Theory comparison (A12.05), cross-check

## Numbers re-opened and confirmed
1. d'Aliberti and Horta Ribeiro 2026 (arXiv 2601.00514, full PDF text): 6.31% shifted traces, 2.57% vs 16.44% accuracy, Math -19.78pp, Xwords -6.24pp, high-entropy Math -7.40pp, low -22.88pp, Pass1 to Pass2 +8.41pp (32.21% to 40.62%), N=320,000 Math. All confirmed.
2. Ollinger et al. 2017 ten-penny (PMC5533865): chi2(1,59)=23.80, chi2(1,58)=26.01, chi2(1,57)=14.85, phi .64/.67/.51, all p<.0001. Confirmed. Intersection use before hint 47% solvers vs 26% non-solvers confirmed. Maximisation group 28% failed (confirmed, 21/29 solved).
3. Mizumoto et al. 2025 (arXiv 2509.14704v2): humans 52.9% (n=126); 7.60% (n=16) vs 17.59% (n=19) on the 120-item subset; Welch t(24.093)=2.976, p=.00655, d=0.946, Mdiff 9.804pp CI [3.007,16.600]; OR 2.29 [1.99,2.64]; accuracy 9.42% vs 19.25% on all 201 items; size r=-0.017; Grok-4 Japanese 29.5% vs English 48.8%; Claude Opus 4 36.7% vs 28.7%; Gemini 0/12 Japanese vs 22/188. Confirmed.
4. Nasvytis and Fan 2026 (arXiv 2605.12970): 202 recruited, 189 analysed; value-loose-chunk 80.7%, tautology 19.2%; later accuracy 44.0% in Different; time 89.9 s vs 179.0 s. Confirmed (83.7% is the Same-condition figure, line cut off in text but consistent).

## Corrections
- a13 says 119 analysed. The paper recruited 120 and dropped 4 who solved within 5 minutes; group denominators are 30+29+28+29 = 116. Use 116 (b06 was right).
- a17 and b18 mix subsets: 7.6% vs 17.6% is the 120-item human-comparison subset, but the Welch t, d=0.946 and OR 2.29 are over all 201 items (9.42% vs 19.25%). Do not quote d with the 7.6/17.6 pair.
- a01 says Jones 2003 numbers were not seen. Sibling folder 04 (a21-a24) holds them: car park, N=39, normal 7/13 vs rotated 12/13 vs easy 12/13 unaided, Fisher p=.01. Those counts are derived, not read from a clean table. Treat as provisional until the published table is read.
- a20/b15/c09 triple-count one paper (Nasvytis and Fan); likewise Ormerod 2020 appears as a06/a07/b01-b03 and Mizumoto as a17/a18/b18-b20/c01-c05. Independent source counts in claims.jsonl reflect papers, not lines.
- Ormerod 2020 internal inconsistency: low-value tight is 13/30 in the outcome table but 11/29 in the first-move table. Not resolved (PDF not retrievable this session; escholarship returned HTML).

## Contradictions between sources
- WM and insight: Ash and Wiley 2006 and Lv 2015 say WM relates to search not restructuring; Chein and Weisberg 2014 read WM as evidence against a special insight process. These are compatible only if the staged view holds.
- Ormerod 2020 says constraint relaxation is not needed; Ollinger 2017 says relaxation is necessary but not sufficient. Same data pattern, opposite emphasis.
- LLM verbal insight: Orru 2023 and Speed 2023 report near-human scores; BRAINTEASER and NazoNazo report large gaps. Likely contamination of classic items and difficulty of novel ones.
- Spontaneous shifts hurt (d'Aliberti) while the R1 report presents the Aha moment as a gain.

## Weak spots
- Jones 2003 itself: tiny N, one task, impasse threshold set by the author, predictions for both theories set by the same author, circular lookahead inference. The headline "RCT predicted better" rests on one 39-person experiment.
- Ormerod 2024 (PRODIGI) questions whether Jones discriminated between models; seen only as a search summary, not opened.
- No LLM paper runs a head-to-head. All LLM evidence is indirect.
- Matchstick work in humans uses between-subjects single problems; effect on repeated measures unknown.

## Only seen in snippets or abstracts
a01-a05, a11 (second-hand numbers), a24, b10, b13, b14, b27, c16 (second-hand citation), c22, c23, c24, a16 tables.

## GAPS (most decision-relevant first)
1. Does any LLM show the Ormerod 2020 interaction (large value gap lifts hard tautology problems) in matchstick items? No direct test exists.
2. What exactly are Jones 2003 per-cell numbers and statistics in the published table, and does the RCT advantage hold in a Rush Hour variant for LLMs?
3. Ormerod 2024 PRODIGI: what does it replace in CSP, and does it change the detector design (relative stall rule)?
4. Is the reframe-plus-criterion result (ten-penny, 72% vs 7-21%) reproduced on other multi-step insight tasks or with LLMs?
5. When does gated reconsideration (d'Aliberti +8.41pp on math) help on puzzle domains where the gain was near zero (crosswords, Rush Hour)? What gate works there?
6. Do LLM stalls have a measurable analogue of eye-fixation impasse (mean + 2 SD of own step time) that predicts success?
7. Is verification failure (correct candidate written then rejected) reducible by an explicit endorse step, and at what token cost?
8. Do the contested WM-search findings (Ash and Wiley, Lv, Chein and Weisberg) predict anything about context length or branching factor for the agent?
9. Which public insight items are contaminated for current models (Speed, Orru results vs BRAINTEASER)?
10. Does frame transfer by problem type (Nasvytis and Fan) work for an agent memory keyed by type tag at equal tokens?

## Gap search results

Search tools were mostly unavailable (WebSearch budget spent; arXiv, Semantic Scholar, OpenAlex all returned 429 or rate-limit errors). Work used Europe PMC and the full texts already on disk. Evidence is in evidence_d.jsonl (d01-d17).

1. Ormerod 2020 interaction in LLMs: STAYED OPEN. No LLM study found with a factorial chunk x value design. New human context: d01 replicated the matchstick difficulty order (A easiest, C hardest) in three experiments.
2. Jones 2003 per-cell table: STAYED OPEN. DOI and PsycNet pages returned no content (d16, opened:false). K02 stays provisional. Rush Hour variant for LLMs: no study.
3. PRODIGI (Ormerod 2024): PARTLY CLOSED on design, OPEN on the paper. An earlier executable CSP model (d04) shows the detector: criterion = remaining dots / remaining lines, failure triggers widening. Supports a relative stall rule. The PRODIGI paper itself was not found.
4. Ten-penny reframe-plus-criterion replication: STAYED OPEN. Nothing found beyond Ollinger 2017. Chao 2025 (d13) shows far-candidate sampling helps on RAT, a different task.
5. Gate for crosswords and Rush Hour: ANSWERED AS UNTESTABLE. d05: Rush Hour base accuracy 0.0233% (+0.01pp), crosswords 9.70% (+0.45pp); models were 1.5B to 8B, so no headroom. Entropy sign also flips by domain (d06). A gate for puzzles needs a stronger model.
6. Entropy/step-time stall analogue: PARTLY CLOSED. No eye-fixation-style rule tested in LLMs. d06 says entropy is domain-dependent; d03 says the human shift is abrupt and late.
7. Endorse step: STAYED OPEN. d07: verification failure is 5-39% of wrong answers, but no study adds an endorse step or measures cost. d10 suggests convergence is the weak phase.
8. WM and search: PARTLY CLOSED. d12 (Korovkin 2018, 32+32) supports a staged view; prediction for context length and branching is stated but untested in LLMs.
9. Contamination: PARTLY CLOSED. d08, d09: classic English sets treated as contaminated or saturated; release date predicts accuracy (Spearman .402, n=38), size does not. No per-item measure.
10. Frame transfer by type tag at equal tokens: STAYED OPEN (d15, human data only).

New caveats: the movement result in d01/d02 is post hoc; baseline accuracy was about 86% (ceiling). Claims K19-K24 added; K08 raised to 3 sources; K13 now carries the floor-effect caveat.
