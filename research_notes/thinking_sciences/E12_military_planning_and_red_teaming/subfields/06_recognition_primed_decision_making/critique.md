# E12.06 Recognition-primed decision making: cross-check critique

Checked 2026-11-01. Claims are in claims.jsonl (24 claims, E12.06-K01 to K24).

## Sources re-opened (the 10 key numbers)
1. Klein, Calderwood, Clinton-Cirocco 1985 (DTIC ADA199492 full text). Confirmed: 156 decision points, 127 prototype, 28 with more than one option, 16 with relative evaluation, under 12% comparison, over 80% recognition.
2. Same report, Table 4. Confirmed with a correction (below).
3. Ruoss et al. 2024 (arXiv 2402.04494) Table 1. Confirmed: 270M model puzzles 95.4, 136M 94.5, 9M 88.9, Elo 2895 vs humans, 2299 vs bots; GPT-3.5-turbo-instruct 66.5; AlphaZero policy 56.1, value 82.0, 400 MCTS 95.6. Added: Leela policy-only 88.6, 400 MCTS 99.6.
4. Liu et al. 2025 (arXiv 2410.21333). Confirmed 87.5 to 64.4 (23.1 points) and the 331% slowdown. Correction on the 36.3 figure (below).
5. Ma et al. 2025 (arXiv 2504.09858): 51.3 vs 28.9 on AMC23 at 700 tokens confirmed in abstract and text.
6. Sprague et al. 2025 (arXiv 2409.12183): "over 100 papers", 20 datasets, 14 models confirmed.
7. Vidulich and Tsang 2026 (Cognitive Research): t(19)=6.54 d=1.39, t(19)=4.23 d=0.96 confirmed in the full text.
8. Kopka and Feufel 2026 (JMIR Biomed Eng): abstract and PMC text confirm 63.3 / 67.6 / 66.7, OR 2.26 and 2.05, OR 2.15, self-care 13.4 to 29.8 and 24.6, 82.2% correct at least once.
9. Dualformer (arXiv 2410.09918): 97.6 / 93.3 / 45.5% fewer / 80 vs 30 / 96.6 / 59.9% fewer confirmed in abstract and table.
10. Rivera et al. 2024 (arXiv 2401.03408): 10.15 to 26.02 (+256%) confirmed in the text; Thinkless 50-90% confirmed in the abstract.

## Corrections made
- a02 (founding study counts). The scan of Table 4 is garbled. Reading it with the text: deliberated 10 (8 at the pumping station) = 18, constructed 7 (4) = 11, analog 3, prototype 114 (10) = 124. The text's "127 prototype" therefore equals prototype 124 plus analog 3. The a02 line lists analog as a separate group, which double counts; the groups are not additive to 156 as written.
- a05 (pumping station). The report text says "roughly 59%" of pumping-station decisions were deliberated, but Table 4 gives 8 deliberated out of 22 (36%). The report is inconsistent with itself. Use "36% by the table, 59% by the text" and do not quote either as firm.
- c04/c05 (36.3 points). 36.3 is the gap between o1-preview (57.7) and GPT-4o direct (94.0) on a 440-item subset: two different models. The cleaner same-model CoT cost is GPT-4o 87.5 to 64.4 (23.1 points, p<0.0001). K16 uses 23.1.
- c01 (Elo). 2895 is Lichess blitz against humans; against bots it is 2299 and the paper says its estimated Elo against engines is far lower. Quote both.
- c14 (Rivera). The 256% is the text's "neutral scenario" claim; the appendix table row is labelled Invasion in text extraction, so the scenario label is uncertain. The paper also says most start-to-end increases are not significant.
- a23/b09 duplicates: both are one paper (Kopka and Feufel 2026, same as a23-a25, b09-b12). Counted as one source in K14/K15. Likewise a26 and c17 (Heander 2025) and a15/b01-b06 (Kahneman and Klein 2009) are single sources.
- Status labels. K01 and K02 are "single-source" despite many lines, since a01-a07, a33, b27 are all the same report and b02 is its co-author.

## Contradictions between sources
- Strong RPD reading ("experts are fine with the first option under time pressure", Calderwood 1988) vs Vidulich and Tsang 2026 (grandmasters blunder more in blitz, d=1.39). Not a true refutation of RPD: blitz is also about speed of search, not only recognition. Open.
- Klein 1985 says 81% recognition; Klein and Calderwood 1990 (12 vs 12) says only 18% of points fit classical concurrent comparison and 32% involved evaluating between options. The share depends on how "decision point" is coded.
- Kopka 2026: RPD prompt +4.3 points but data-frame prompt +3.4 with no significant difference between the two; the headline "RPD prompt works" is really "a structured NDM prompt helps a bit".
- Sport: Hepler and Feltz replicate the option order effect but not the consistency or confidence claims.
- Pumping station 59% vs 36% (above).

## Weak spots
- The whole human base is interview data from one group on hand-picked incidents. No controlled test shows that the first option was best.
- Army RPM evidence (30% faster, 20% faster) is participant estimates by the model's developers.
- LLM evidence for RPD itself is one paper (Kopka), one task (triage), one vendor family, no length-matched control, no effect for the newest models.
- Machine evidence for fast-first mode (Sprague, Liu, Ma, Ruoss, Dualformer, Thinkless) is about fast vs slow modes, not about Klein's serial generate-and-simulate loop. It supports a gate, not the full RPD procedure.
- Wargame LLM papers (Lamparth, Rivera) test escalation behaviour, not recognition.

## Seen only in snippets or second-hand (not re-opened)
Kaempf 1996 (95% / 4%, via Reale 2023 and abstract), Klein et al. 1995, Johnson and Raab 2003, Calderwood 1988 (via Vidulich), Calderwood Crandall Klein 1987, Cohen Freeman Wolf 1996, Lipshitz 2001, b27-b29, a31, a32, c18, c22, c23. The Army RPM numbers (a19) come from a review article by the developers. Sport shares (60-81%) come from reviews citing Macquet 2020.

## GAPS (most decision-relevant first)
1. At equal tokens, does a keep-first-then-simulate agent beat generate-N-and-compare on tasks with expert-labelled workable options (incident or planning cases)? No study measures a model's first-option workable rate against experts.
2. Which cue tells the agent a case is "typical" enough to keep the first option (task features, retrieval similarity, answer consistency)? Is a prompt-only typicality gate as good as the trained gates (Thinkless, Dualformer)?
3. Is the simulate-the-first-option step what protects RPD? Is there any ablation, human or LLM, of simulation versus no simulation?
4. Does the Kopka RPD gain replicate on another task, another model family, and against a length-matched neutral prompt, and why did GPT-5.2 not respond?
5. Does option quality fall with generation order in LLMs (the take-the-first effect), and does the effect differ for reasoning and non-reasoning models?
6. What drop trigger works (expectancy violation, low self-consistency, verifier failure), and how fast should it fire? Mismatch events were only 3 of 156 in the original study.
7. How far does the grandmaster blitz result (Vidulich 2026) transfer: is the harm from less search or from less verification, and does a token cap on an agent show the same blunder pattern?
8. Does the Army single-course-of-action plus pre-mortem method beat three-course comparison on a blind-scored outcome in a controlled test (not self-estimated time saving)?
9. For red teaming specifically: does keep-first make an agent worse at finding an adversary's best reply, since the adversary's move is atypical by design?
10. How large must the case memory be for pattern recall to substitute for search (Ruoss needed 15.3B labels), and how does retrieval quality change the first-option hit rate?

## Gap search results (2026-11-01, evidence_d.jsonl d01 to d18; claims K25 to K34 added, K08, K15, K20, K24 updated)

Limit: the shared web-search quota ran out after 3 queries and arXiv, OpenAlex and Semantic Scholar then returned 429. Sources were reached by direct PDF and PMC download. Gaps that depend on finding new papers stayed open.

1. Keep-first-then-simulate vs generate-N at equal tokens on expert-labelled cases: STILL OPEN. Partial: first-attempt plan validity is 8.8% to 97.8% across models on Blocksworld (d09), and early-finishing chains beat compare-N on verifiable math (d13). No expert-labelled case study. Claims K25, K32.
2. Typicality cue and prompt-only vs trained gates: PARTLY CLOSED. Draft agreement (DART, d03) is a training-free gate that matches or beats always-think; self-asked gates are weak (d04, d06); prompt-based switching beat routers at 9B and 1.1T but not at 20B and 671B (d05). No direct comparison with Thinkless or Dualformer. Claims K27, K28, K29, K30.
3. Is simulation what protects RPD: PARTLY CLOSED for LLMs. Same-model review without outside feedback does not help and approves most bad plans (d07, d08); simulating candidates beat re-ranking in WebDreamer (d10). No ablation inside a keep-first agent, and no human ablation found. Claim K26, K08.
4. Kopka replication: PARTLY CLOSED. The GPT-5.2 miss is a floor effect (self-care 0 to 3.1% under all prompts) in a model with a strong refer-to-professional default (d01). Still no length-matched neutral prompt, no second task, no second model family (d02). The 66.7 vs 67.6 near tie is consistent with a generic think-first effect.
5. Option quality by generation order: STILL OPEN. Only presentation-order effects exist: first-listed option favoured when options are good, last when poor (d11), and reorder sensitivity of 13 to 75% (d12). No reasoning-model comparison. Claim K31.
6. Drop trigger: PARTLY CLOSED for samples. Agreement-based stopping saves up to 7.9x samples with under 0.1% loss (d16); entropy-triggered escalation raises accuracy on code at higher cost (d05). Nothing tests plan-level expectancy violation, and the rarity of mismatch events (3 of 156) is not addressed.
7. Grandmaster blitz transfer: STILL OPEN. The nearest LLM result is that early wrong fixation and overthinking depend on complexity (d14, d15). No token-cap blunder study found.
8. Army single COA vs three COAs, blind-scored: STILL OPEN (search blocked). Best evidence stays a19 (self-estimated at least 30% time saving; Thunholm about 20% faster).
9. Red teaming and the atypical best reply: STILL OPEN (search blocked). No test found.
10. Case memory size: STILL OPEN. Chess scaling shows data-size dependence and overfitting at 10K games (d17), but no text case-retrieval curve.

Corrections found while reading: (a) Kopka per-model tables show GPT-5.2 Thinking nonemergency accuracy of 71 / 73 / 70.7, so "no gain" holds for both GPT-5.2 versions; (b) Chen et al.'s 92% is conditional on responses that reach a correct answer, so it must not be quoted as the overall first-solution accuracy; (c) Valmeekam 2023's abstract wording "diminish" is relative to an external verifier, since 55/100 beats the 40/100 no-check baseline.
