# Critique: C09.05 Efficient diagnosis algorithms (cross-check)

## Re-opened sources (this session) and outcome
Re-read in full text: Rodler AIJ 2022 (arXiv 2010.04282), DynamicHS (2012.11078), He et al. 2026 QXR (2601.13600), plus the cached texts of FastDiag, Ignatiev et al., Shchekotykhin 2012, Zhu and Chang, the habilitation thesis and the IJCAI abstract.
Confirmed unchanged: RBF-HS memory factor 14.1 (ENT) / 13.8 (SPL), max 50/57, factor over 10 in 45% of cases; 400-node switch, 416-node cap; maxProb median 3.75 vs 3.56, 73% vs 72%, positive in 53%; DynamicHS 99.4% / 96%, median 52%, max 75%, hardest 64%/89%; QXR VitaminC recall 0.617->0.957 (Sonnet 4.5) and 0.574->0.968 (Opus 4.6); FastDiag RMSD 0.95/0.97/1.64; IHS 1140 instances, 177/185; OAEI 286/140/122/26; Zhu and Chang 12/12, 9/12, 9/9, 8/9; thesis 37%/117% and 99.999%/4%; IJCAI abstract 93%/98%, 85%/98%; DynamicHS benchmark 20 problems.

## Corrections
1. Dataset size: a03/b01 say 14 ontologies (AIJ, Table 1 lists 14, 42 to 33,203 axioms). b08/c08 say 12; that is the short DX version. Both right, different papers. c09 "4 of 10 cases faster" is the earliest short version only. Do not mix them.
2. b20 says QXR needs "435 oracle calls at N=30 and 4,950 at N=100". Paper text: these are the pairwise-checking counts N(N-1)/2, used to show how calls scale, not QXR's own counts. QXR is O(I*m*(1+k log N)). c06 is correct; b20 is wrong. Claim K17 uses the corrected reading.
3. b03 "avg space factor 18, max 158" comes from the appendix single-run experiment (minCard), not the main 5-session tests (main: 14.1/13.8, max 57). Two different runs; the 158 should not be quoted as the headline.
4. b07 (IJCAI 2023): the task text calls it Jannach et al.; it is Rodler's extended abstract of RBF-HS. c11 (seen only as snippet) is superseded by b07 which was opened.
5. a28 and the 2026 arXiv ids 2606.23720 and 2610.00126 were read from abstract/intro or cached text; a28 has no numbers.

## Contradictions and tensions
- Memory saving vs time: minCard gives positive tradeoff in 94-96% of cases; maxProb only 53%. Same algorithm, opposite verdict. Any headline "RBF-HS saves 14x memory" holds only for minCard.
- DynamicHS wins on time but costs memory; RBF-HS wins on memory but can cost time. They are not directly compared with each other.
- Direct (conflict-free) vs HS-Tree: wins on 13 hard alignments but timings elsewhere are mixed (b27: LogMap ENT 6.60 vs 13.41, Lily SPL 82.9 vs 115.2, but GOMMA-bk 18.34 vs 14.47).
- QXR: Sonnet 4.5 F1 falls slightly on RAMDocs (.882 -> .870) while it rises on VitaminC. Gains are model- and dataset-dependent.

## Weak spots
- Almost all numbers come from one author (Rodler) on one benchmark family (OntoDebug knowledge bases, Pellet). No independent replication of RBF-HS or DynamicHS was found. Therefore the status "established" is used only where different groups agree (FastDiag/direct vs HS-Tree, MergeXplain/parallel family is one group so kept single-source). Five claims were downgraded to single-source for this reason (K02, K05, K07, K10, K19).
- Runtime is wall-clock with a reasoner; no token or LLM cost. Transfer to an LLM agent is analogy only.
- The LLM evidence is one preprint (QXR, temperature 0, Bedrock, about 30-claim sets, single oracle call) and one small agent-debugging study (12 dev cases). No peer review checked.
- Fault-probability priors drive heuristic choice (a19); an LLM agent has no calibrated priors.
- Only seen as snippet or abstract: c11 (IJCAI abstract page, later opened as b07), a28 body, a29 is a negative search (no Semantic Scholar/OpenAlex hits for LLM + RBF-HS).
- Background-only relevance: the subfield is about scaling exact enumeration, which an LLM agent seldom needs.

## GAPS
1. Does any independent group replicate RBF-HS or DynamicHS on non-ontology domains (circuits, software, configuration)?
2. Does localise-then-delete (QXR) keep its recall gain at equal total tokens against self-consistency or best-of-N, since it uses many more calls?
3. How does QXR degrade when the oracle is non-monotonic or noisy, and does the weighted hitting-set variant fix it (not tested in the paper)?
4. Do QXR gains hold on diagnosis tasks (faulty code, reasoning chains) rather than claim sets of about 30?
5. Can an LLM agent give usable fault probabilities, so best-first and entropy/MPS heuristics can run, and how wrong may they be (a19: wrong heuristic costs up to 250%)?
6. Is reusing the candidate set across observations (DynamicHS idea) beneficial for an agent with a limited context window, versus re-deriving it?
7. At what candidate count does a bounded frontier (RBF-HS style) start to matter for an LLM, given that an agent rarely lists over 100 suspects?
8. Which results of the 2023-2026 diagnosis literature (Rodler, Hipler/Leucker) use LLMs at all? A targeted search with Semantic Scholar/OpenAlex was not completed.
9. Are random or worst-first samples (a15) better than best-first when the LLM proposes the candidate sample?

## Gap search results (evidence_d.jsonl, d01-d17)
Limits: WebSearch budget was used up, and arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429 for most queries. MDPI and ScienceDirect blocked fetches. QXR full text, ProcessBench, BIG-Bench Mistake, Xiong, Tian, Kadavath, Bailis, Brown and Liu were opened as PDFs.

1. Independent replication on non-ontology domains: STAYS OPEN. Semantic Scholar lists 4 citers of RBF-HS (d14): one same-group software paper (spreadsheets), three others from other groups, none opened. EC-MHS (Symmetry 2026) may compare against RBF-HS; unconfirmed (d15). No DynamicHS citer list obtained.
2. Equal-token comparison for QXR: STAYS OPEN. No call or token counts in the paper (d04). Appendix Table 5 shows a self-consistency prompt lowers recall (e.g. GPT-OSS-120B .876 to .475) while QXR reaches .995 (d03), but budgets are not matched. Best-of-N and voting scaling papers (d11, d12) show why a tuned equal-call baseline is needed.
3. Noisy or non-monotone oracle: STAYS OPEN. One call per query, no repeats (d01). Weighted and graded variants are only proposed (d02). New claim K21.
4. Diagnosis tasks beyond claim sets: PARTLY CLOSED as indirect evidence. QXR itself only has claim sets (d05). Error localisation in chains is weak but still useful (d06, d07): GPT-4 52.87 on BIG-Bench Mistake, backtracking gains plateau near 65 percent accuracy. Claim K22.
5. LLM fault probabilities: CLOSED for the practical question. Verbalised confidence is overconfident, GPT-4 AUROC 62.7 percent (d08); calibration improves with verbalised probabilities (d09, d10). Combined with a19 (bad priors: random probing best), do not feed LLM priors into entropy or best-first heuristics without calibration. Claim K23 (established, 3 independent sources, but all about answer confidence, not fault priors).
6. Candidate reuse under a context window: STAYS OPEN. No test found. Claim K24 records this.
7. Frontier size threshold: STAYS OPEN. Only indirect long-context evidence (d13). No measured threshold.
8. LLM use in 2023-2026 diagnosis literature: STAYS OPEN. Searches could not run (d17). Earlier finding stands (c22 to c26, a28).
9. Random vs best-first samples with an LLM-proposed sample: STAYS OPEN. No source found; a15 evidence is from non-LLM settings.

Claim changes: K14, K15, K17, K19 got notes and evidence ids; K20 to K24 added. No status downgraded.
