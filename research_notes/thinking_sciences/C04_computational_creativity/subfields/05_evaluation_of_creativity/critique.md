# Critique: Evaluation of creativity (cross-check)

## Numbers re-opened this session (against full text in D:/research_scratch/C04.05)
1. Si 2024: novelty 4.84 / 5.64 / 5.81 (review level, 109 reviews per condition) and 4.86 / 5.62 / 5.78 (idea level, 49 per condition, p=0.03 and 0.00). Correlations 0.725, 0.854, <0.1. Agreement 56.1; judges 43.3-53.3. CONFIRMED. Lines a01 and b01 differ only because one is idea level and one is review level; both are right. State the level whenever quoting.
2. Ideation-Execution Gap: ideation scores 4.912/4.404 human, 5.778/5.653 AI; drops -1.049, -1.760, -1.879 for AI. CONFIRMED from the HTML. Correlations (b07) not re-opened.
3. Kaufman 2008 CAT poems: alpha .832 vs .935 raw, .804 vs .575 standardised, r .216 (4.41% shared). CONFIRMED. Correction: a18 says "106 nonexperts" while the table shows 204 novice raters (after removing 4 raters, 2 writers); treat the rater count as unresolved.
4. TTCW: Fleiss .41, Pearson .69, 84.7% pass, 2,016 judgments, LLM kappa 0.016/0.035/-0.006, best single test .31. CONFIRMED. a22 "2000+" equals 2,016.
5. Falk 2025: kappa novelty 0.18 (2 buckets), 0.08 (3), 0.04 (5); usefulness 0.53 to 0.12; Prometheus-Llama 0.59; sample sizes. CONFIRMED (the 0.12 usefulness five-level figure not separately seen).
6. LitBench 73% / 78% / 65.25% / 2,480 / 43,827. CONFIRMED.
7. Sawicki: 0.87, 0.38, -0.33. CONFIRMED.
8. Beaty and Johnson: latent r .91 and .75. CONFIRMED.
9. Abstract-level only (full text not re-opened): RQ-Bench direction (experts prefer author RQs, LLM judges rate model RQs as novel), Tutone (misalignment, near-zero metric correlation), RINoBench (1,381 ideas, reasoning mirrors human rationale), Bhushan (strong judge-human correlation). The exact figures (78/56, 82/52, 27.2 to 49.1, tau values, F1 17.2, rho .732) stay at the earlier agents' reading and are UNVERIFIED by me.
10. Not re-opened: NoveltyBench, Shen, literature-grounded novelty, Domanti, S-DAT, n-gram frontier, Unlikely Duel.

## Correction notes
- A stray file chak.txt in the scratch folder is a different paper (education ethics); the TTCW text is artifice.txt. No effect on the evidence.
- Si 2024 appears in a, b and c: it is ONE source. Independent counts in claims.jsonl count it once.
- c31 is a synthesis, not a source; not used as evidence.

## Contradictions
- Pairwise vs direct judging: worse in RQ-Bench and for GPT-4o on ideas; better with batch ranking on poems (Sawicki). Task, model and batch size differ.
- Bias claims: Tutone, RQ-Bench and Domanti find judges favour machine text; Bhushan finds no self-preference or verbosity bias with a rubric and run history; Si found humans themselves rated AI ideas as more novel. So "AI-favouring" is not only a judge bias; it is a pre-execution rating effect.
- LLMs vs non-experts: Sawicki says LLMs (rho .87) beat crowd raters; Chakrabarty and Si say LLMs are near chance versus experts. Different ground truth (publication venue vs expert rating), small samples.
- Semantic distance: r .91 latent (Beaty) vs r .13-.24 item level (S-DAT). Latent correlations inflate; item-level is the relevant one for an agent.

## Weak spots
- Execution flip is one trial (43 ideas, NLP prompting); the rank flip on several metrics was not significant (b06).
- Most LLM-judge numbers come from small test sets (32, 49, 50, 98 items) and from 2026 preprints not peer reviewed.
- Ritchie/SPECS: no evidence tying them to downstream success; evidence is builder opinion.
- Novelty rated is not novelty measured; no study here links any automatic novelty score to later usefulness except the Ideation-Execution Gap.
- Only snippets: Organisciak 2023, Kaufman 2009, Amabile 1982, Koivisto and Grassini (a17, a28, a29, c28, c29).

## GAPS
1. Does any cheap judge (retrieval-grounded, rubric plus run history) rank ideas by their later execution success? Only the Ideation-Execution Gap measures outcomes, and it did not test judges.
2. Is distinct-answer count (NoveltyBench style) or semantic entropy correlated with later usefulness, or only with diversity?
3. At equal tokens, is k-sample pooled judging (CAT-style pass counts) better than one long judgment, and what k saturates?
4. Does length/elaboration residualisation remove the machine-text bias in judges for ideas, not just AUT answers?
5. How large is the self-preference bias when the judge is the same model that generated the ideas, with authorship hidden? Evidence conflicts (Bhushan vs Tutone).
6. How stable is retrieval-grounded novelty to the choice of prior corpus and its date (novelty is time-dependent)?
7. Is the "novelty mirage" in RQ-Bench reproduced for ideas with an explicit narrowness or source-boundedness test, and does that test transfer to our domains?
8. What is the minimum expert-labelled calibration set needed per task class to make a zero-shot judge usable (Kaufman: novices fail)?
9. Do Ritchie/SPECS-style multi-criterion scores add anything over pass/fail execution on checkable tasks?

## Gap search results

Gap searcher pass. Evidence is in evidence_d.jsonl (d01 to d19, all full texts opened; the web search quota ran out, so papers were found through arXiv listing pages and read as PDFs). Claims K05, K06, K08, K18 and K19 were updated and K20 to K27 added. Next free id is C04.05-K28.

Closed or mostly closed
- Gap 5 (self-preference): mostly closed. Tutone's judge (Llama-3.3-70B) wrote none of the AI stories, so that result is a machine-text preference, not own-output preference (d08). Bhushan used a neutral reference judge and found GPT-5 more conservative on its own runs (d09). A style-neutral blind test found raw self-preference vanishing after controls (S +0.003) while authorship labels alone moved scores (d06, d07). Objective rubric items still showed more than 50% excess own-output passing (d10). The conflict is explained by task, style visibility and the reference. Status of the claim: contested (K22).
- Gap 6 (corpus and date): partly closed. Retrieval changes verdicts, can make a judge say novel because nothing in five retrieved abstracts matches, and can also hide real novelty (d03, d04). A time-split with a fixed cutoff exists (d01). Frozen corpus with per-case cutoff is practical (d05). No paper varied the corpus date on identical ideas and measured drift; that exact measurement stays open.
- Gap 7 (novelty mirage for ideas): mostly closed. The same inflated-approval pattern shows for proposals (74% of unsound approved, d13) and ideas (d01 negative correlation with later match). Explicit claim-attribution repair works (72.2%, d05) and narrowness testing works on RQ-Bench; both fixes were built after seeing the failure. Not tested in our domains.

Partly answered
- Gap 1 (cheap judge vs later execution): one outcome-based test exists but uses publication match, not execution (d01): the judge's novelty ran negative. No test of a retrieval-grounded or rubric-plus-history judge against execution success. DeepInstructor and the ML-trajectory rubric judge were scored against human ratings only (d15, d09). Still open for execution.
- Gap 3 (pooling k vs one long judgment): k=3 voting adds a few points pointwise and up to 11 pairwise; longer reasoning and extra retrieval add little (d03, d17); pooling six models matched the best single model (d11). No k curve and no equal-token test. Still open on the saturation point.
- Gap 4 (length and elaboration for ideas): rewriting ideas into one plan format did not remove judge instability (d04); a decoupled evidence-then-score judge reduced the length-score correlation by 5.81% but did not remove it (d12). No residualization test on ideas. Still open.
- Gap 8 (calibration set size): a fine-tune on about 140 labelled samples reached QWK 0.47 against 0.64 for a decomposed rubric with no labels (d12); human-human floors are about 0.36 Spearman on idea distance (d14). No curve of agreement against label count. Still open.

Still open
- Gap 2 (distinct-answer count or semantic entropy vs usefulness): only set-level evidence that diversity training did not lower execution success on 15 instances (d14). No per-idea correlation. Open.
- Gap 9 (Ritchie or SPECS vs pass/fail): nothing found; ALPS shows the pass/fail side only (d18). Open; keep Ritchie and SPECS as vocabulary only.

Corrections and cautions from this pass
- Chae et al. (d07) Table 7 row-to-dimension mapping is garbled in text extraction; quote only the direction, not the dimension.
- d12 AUT and TTCW cell values were not verified.
- d16 and d17 were read only in abstract, introduction and appendix parts.
- Kaufman 2008 novice count (106 vs 204) remains unresolved by this pass.
- All new numbers come from 2026 preprints that are not peer reviewed; K22 and K23 are contested, and K20, K24 and K27 rest on one study each.
