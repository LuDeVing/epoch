# Critique and cross-check: E14.05 Atypicality versus disruption

## Corrections made (sources re-opened this session as full PDF text)
Checked and CONFIRMED: Li/Lin/Wu 2025 (2506.15959): 41M articles, 40,453,825 (Fig 2) and 40,935,251 (Fig 3), cut-offs A>22.9, D>0.04. Lin/Evans/Wu 2022: r=-0.05, 61% vs 36%, 2.3%, 3.9% to 1.4%. Holst: 97% and 78%, R2 0.10 to 0.52 and 0.15 to 0.95. Petersen: 0.051, 13.6 years. Lin/Li/Wu 2504.04677: 65% d_p<0, 62% D<=0, 20 scholars/190 responses, AUC 0.83. Fang/Evans: r=0.37 and -0.37, df=23,448,429, 73.96%, 0.405 to 0.214 (-47.2%). Si et al.: 4.84/5.64/5.81, N=49, 79 reviewers. Ideation-execution: N=43, -1.049/-1.760/-1.879. Catalyst: AUC 0.83/0.60/0.49/0.42, 36,113 papers.
Corrections:
1. a07/b16: the "0.014 expected by chance" is a model-predicted probability (their Eq. 9), not a random-shuffle baseline. The ratio 37x is as stated.
2. a10/b05: r=-0.05 is for TYPICALITY vs D, so it means atypical goes with more disruptive. This is the OPPOSITE sign to Li/Lin/Wu 2025 (see contradiction 1). Evidence lines that call it "atypicality vs D r=-0.05" must be read with this sign.
3. a26/b18: the Nobel AUC for standard D (0.73) is confirmed in the figure text; the 1D Nobel value of 0.981 (a26) was not found in extracted text (only "0.94 to 0.98" is stated). Use the range.
4. a18: "0.033 + 0.018" confirmed only as growth components of gC; keep.

## Contradictions
1. Sign of the A-D link: 2022 paper (atypical, disruptive positively linked, 61% vs 36%) vs 2025 paper (atypical, less disruptive, Fig 3). Same group. Differences in measure (median z of journal pairs vs A-index top cut-offs), corpus (MAG vs OpenAlex), and D window may explain it; the 2025 text does not reconcile it. Open.
2. Decline of disruption: Park 2023 says real decline; Holst, Petersen, Bentley say artefact; Lin/Li/Wu 2025 say team-size result depends on window and reference count.
3. Large teams: Wu 2019 small teams disrupt; Huang/Xie 2026 and Lin/Yang/Wu 2026 find the opposite with pairwise measures.
4. Validity: Wu 2019 Nobel mean D 0.10 higher than controls; Wei 2020 finds no difference (0.236 vs 0.239).
5. LLM ideas: Si 2024 says AI more novel; Si 2025, Gupta/Pruthi 2025 and the diversity work say that novelty is shallow, borrowed or fails at execution.

## Weak spots
- The central 2025 claim has no printed effect size; the text of 2506.15959 is only about 15k characters. No correlation coefficient. The functional-equivalence argument is by hand-picked example.
- Uzzi 2013, Funk/Owen-Smith 2017, Wu 2019 and Park 2023 were not opened (paywalled); numbers come second-hand.
- The LLM tests in the 2025 paper (Llama-3.1-70B zero-shot) report direction only.
- Almost no study tests atypicality vs disruption on LLM agent attempts. All agent claims here are by analogy.
- Many "2026" arXiv records (IDs 2604-2610) were read only at abstract level in several lines (c13, c17, c19: no numbers).

## Seen only in snippets or abstracts
c05, c06 (withdrawn paper), c07, c08, c13, c17, c19, a13 to a16, b07.

## GAPS
1. Why do Lin/Evans/Wu 2022 and Li/Lin/Wu 2025 give opposite signs on atypicality vs D? Re-run both measures on one corpus.
2. What is the actual correlation coefficient and effect size between A and D in 2506.15959 (any supplementary data or code)?
3. Does any study test distant-analogy attempts versus in-topic displacement attempts in an LLM agent at equal tokens?
4. Does the pairwise 1D / displacement measure replicate on an independent group and on patents?
5. Can an LLM or embedding "displacement score" between a candidate answer and the incumbent answer predict which wins under execution check?
6. Does execution (running or verifying) restore or remove the AI novelty advantage in domains other than NLP research ideas (math, code)?
7. How does semantic atypicality (Fang/Evans) compare to reference atypicality as a predictor of award papers, replicated outside their data?
8. What are the exact Uzzi 2013 odds ratios (conventional-plus-novel pattern, top 10% tail) and have they been replicated with LLM-based novelty measures?
9. Is generalization (unifying prior ideas) detectable in a single agent's attempts, and does it correlate with correctness?
10. Do dedup and diversity controls (5% non-duplicate, 79.3% dominated by 1-2 papers) change with retrieval or planning methods at equal budget?

## Gap search results
Limits: shared WebSearch budget ran out after 3 calls; arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429. Direct PDF downloads worked. Evidence is in evidence_d.jsonl (d01-d16).

1. Sign conflict (2022 vs 2025): STAYS OPEN, narrowed (d02, d05). Candidate causes from the texts: MAG vs OpenAlex; median z vs top-tail A-index; longest D window to 2018 vs unstated window; pooled r=-0.05 vs binned means. No re-run on one corpus exists.
2. A-D effect size in 2506.15959: STAYS OPEN (d04). Full text has no coefficient, D window or code link.
3. Distant-analogy vs in-topic attempts in an LLM agent at equal tokens: STAYS OPEN. Nearest: Heuresis (d07, d08): novelty-seeking strategies gave rare, low-quality novel ideas; polishing won in 2 of 3 domains. Not the same test.
4. Pairwise/1D replication on another group and patents: PARTLY CLOSED. Huang/Xie (d12) validate 1D on six benchmarks (AUC 0.94-0.98) for papers. Patents untested; Rutzer et al. (d13) show standard patent CD is data-dependent.
5. LLM/embedding displacement score vs execution: STAYS OPEN (d14, d15). No study found; only an unvalidated Llama theory/method labeller.
6. Execution restoring AI novelty edge outside NLP: CLOSED in the negative for ML and weakly for algorithms (d07, d10, d16). No case where novelty survives execution found; math/code evidence is one paper.
7. Semantic vs reference atypicality for awards: PARTLY CLOSED (d06). Semantic wins in all tested domains; no independent replication.
8. Uzzi 2013 numbers: CLOSED (d01). Hit rates 9.11 / 5.82 / 5.33 / 2.05 per 100 vs 5; no printed odds ratio; no LLM-measure replication found.
9. Generalization detectable in a single agent's attempts: STAYS OPEN. No source; Fang/Evans index needs a citation network.
10. Dedup/diversity under retrieval or planning at equal budget: PARTLY CLOSED (d11). Retrieval cuts within-set diversity 5.6-17.9% and raises pooled diversity 10.2-18.1%; planning not compared at equal budget.

Corrections: Nobel 1D AUC 0.981 is in the Huang/Xie supplement table (D 0.731), so critique item 3 is resolved. Heuresis counts 13/300 (appendix) vs 20/200 (main text) are unreconciled.
