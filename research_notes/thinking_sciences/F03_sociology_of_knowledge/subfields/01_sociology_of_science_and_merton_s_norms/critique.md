# F03.01 Sociology of science and Merton's norms: cross-check critique

## Numbers re-opened this session (abstract or record fetched via arXiv, Crossref, OpenAlex)
Confirmed exactly: Liang 2023 overlap (30.85/39.23 vs 28.58/35.25, 3,096 and 1,709 papers, 308 researchers, 110 institutions); Liang 2024 6.5-16.9% range; Latona 2024 (15.8%, 53.4%, p=0.002, +14.4%, +4.9 pp, p=0.024); Ye 2024 (5% -> 12%, 4.5x); Jin 2024 (37.1%); Si 2024 (p<0.05, over 100 researchers); Wang 2023 (66 of 80); Beel 2025 (42%, 8%, median 5, 5 of 34); Huber 2022 (3,300 invitees; 23/48/65% reject); Tomkins 2017 (1.63, 1.58, 2.10, 0.78, 22%); Bol 2018 (more than twice, 8 years); Errington 2021 (50 experiments, 23 papers, 158 effects, 85%, 92%, 39/97); Panickssery (non-trivial self-recognition; the 73.5% figure is not in the abstract).

## Corrections and notes
1. Tomkins: a11 says female effect "not significant", true for the single experiment. The abstract says a meta-analysis makes it significant in aggregate. Do not cite it as "no gender effect".
2. Huber: a10 says "over 20% accept with laureate, under 2% with junior" while b04 says "accept or minor revision 58.8/23.6/9.9%". These are different categories and cannot be reconciled from abstracts. Use only the reject rates (23/48/65, confirmed).
3. Errington: the results paper is eLife 71601 (confirmed). The "challenges" paper (eLife 67995) is a different document; check evidence lines cite the right one.
4. Panickssery: c16 says "over 50%", a25 says 73.5% for GPT-4. The 73.5% is not verified here; keep only "non-trivial out of the box, over 90% after fine-tuning" as confirmed from text read by the earlier agent.
5. Camerer 2018: abstract unavailable from Crossref. 13/21 (62%) and "about half" effect size are from memory and the earlier agents; the effect-size ratio I recall is about 46%, not verified. Treated as unconfirmed in K06.
6. Mitroff 1974: no abstract in any API. The 42-scientist, 3.5-year figure rests on a search snippet. Treat as unverified.

## Contradictions
- LLM prestige bias is large in a19/a20 (+4 points in positive share; +0.39 rating) but small in a21 (reject 6.7% to 5.0%, 10 papers, one model) and absent for Claude on author prominence (a20). Different models, designs, scales. Marked contested (K08).
- LLM review value: a16 (overlap parity, helpful) versus c18 (expert annotation: more deficient segments, low diversity). Overlap of points is not quality. Marked contested (K15).
- Mitroff counter-norms: Anderson 2010 finds them weakly endorsed (18-23%), but Mitroff described ambivalence; the two measure different things (ought versus held in practice) and a08/b01 add that practice is seen as counter-normative. Not a true conflict.
- a22 and c02 both give the 27.7% result, but a22 phrases it as "reviewers know identity for only 10% of papers" and b19/c02 as all reviewers. Treat the wording as unresolved.

## Weak spots
- Almost every LLM peer-review number is from preprints on ICLR/NLP data, one or two models, often an LLM judge of an LLM reviewer.
- The Merton theory lines (a01-a03) are essays; there is no measured test of whether the four norms improve a single agent.
- Many "established" claims have two sources that share a root (b-lines and c-lines repeat the same papers a-lines cover), so independence counts are conservative: I counted by distinct papers, not lines.
- Nothing tests an LLM agent adopting Merton-style norms as a scaffold; all LLM evidence is about judges, not about generators following norms.

## Only seen in snippets or unopened
Mitroff 1974, Anderson 2007 numbers, Merton 1968, Blank 1991, Peters and Ceci 1982, Strevens 2003, Kitcher 1990, Webb 2008 direction, Budden 2008, Camerer 2018 details, Ye 2024 CALM per-bias numbers, Liang 2024 pre-ChatGPT baselines.

## GAPS
1. Does the exact judge we use shift its score when author, institution or "famous" text is added, and by how much compared with the 4-point human-style effect? (decides G5 stripping)
2. Does an early defend-your-own-hypothesis phase before organised doubt beat doubt from the start (Mitroff counter-norm as a feature), at equal tokens?
3. What is Mitroff 1974 actually reporting (per-norm numbers, the 42 scientists)? Needs the full paper or a faithful secondary.
4. Is a model-based sceptic effective only when it has external search or code, as the co-scientist novelty drop 6.14 to 2.38 suggests? Replicate with a controlled ablation.
5. Do independent judges (different models) reduce conformity and self-preference versus N copies of one model in a real task, not a simulation like AgentReview?
6. What is the true Camerer 2018 effect-size ratio and Errington success rate, and do they carry over to LLM-generated claims (shrinkage prior for the agent)?
7. Does the Huber accept-category result (58.8 versus 9.9%) match, and does the effect hold outside finance?
8. How big is LLM judge prompt-injection harm for a non-peer-review judge, and does sanitising input in code remove it?
9. Do Strevens and Kitcher division-of-labour models have an LLM analogue: is diversity across prompts as good as diversity across models?
10. Are there post-2025 replications of the 15.8% AI-assisted review rate or of the 12% top-30% displacement result?

## Gap search results (evidence_d.jsonl, d01-d16)
Search tools were limited: WebSearch budget ran out after one call, arXiv and Semantic Scholar APIs returned 429, OpenAlex was out of daily budget. Work used page fetches, Europe PMC, Crossref and PDFs.

Closed or mostly closed:
- Gap 6 (closed for human literature): Camerer 2018 is 13/21 (62%), effect about 50% (not 46%), true-positive rate 67%. Errington 2021 is 46% (51/112), 40% for positive effects. Carry-over to LLM claims untested (d05, d06).
- Gap 7 (closed for the category question): Huber full text confirms accept/minor revision 58.8/23.6/9.9% alongside reject 23/48/65%. Both are real, different outcomes. Not tested outside finance (one paper) (d07).
- Gap 1 (partly): the a21 line is Howell 2025. Effect is 1.7 pp on a 6.7% reject base (about 25% relative) with quality scores moving about 1%, so "small" and "large" are the same data. Vasu 2025 shows hard ratings hide a large preference visible in token probabilities (66-94% RS win across seven models). Our exact judge is still untested (d01-d04).
- Gap 5 (partly): different models in debate beat the average of the single models (+6.4%), but no equal-token test against N copies of the best model. Persona diversity did not beat voting (d10-d12).
- Gap 8 (partly): injected text raises acceptance about 20% in a second peer-review study; optimised injections reach 90-98% success on pairwise judges; prompt-only defences cost score level. Code-level sanitising still untested (d13, d14).
- Gap 4 (partly): no co-scientist ablation, but CRITIC and Huang give a controlled answer: critique without tools is flat or harmful, with tools it gains (d15, d16).

Still open:
- Gap 2: no LLM test of defend-first-then-doubt. Mitroff's companion report (d08, d09) supports advocacy by committed roles, nothing more.
- Gap 3: Mitroff 1974 ASR paper not opened; only the 1973 NASA companion report. No per-norm numbers. The "42" and "3.5 years" figures remain unconfirmed (report says over 40, three years).
- Gap 9: Strevens and Kitcher not opened; only the LLM side (d11, d12) was checked.
- Gap 10: no post-2025 replication of the 15.8% rate or the 12% displacement found; the search tools failed. Not checked.

Corrections to the earlier notes: Camerer effect ratio is about 50%; the Mitroff "42 for 3.5 years" is not from the NASA report; a21 and the Howell paper are the same study.
