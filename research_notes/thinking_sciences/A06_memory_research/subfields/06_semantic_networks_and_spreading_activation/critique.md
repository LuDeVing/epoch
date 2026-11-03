# Critique: A06.06 Semantic networks and spreading activation (cross-check)

## Sources re-opened this pass (full text, pdftotext)
Lucas (2000, Springer PDF), Hutchison et al. (2013, SPP PDF), HippoRAG (arXiv 2405.14831), SYNAPSE (2601.02744), Query-aware SA (2606.30133), SA-RAG (2512.15922), SpreadPy (2507.09628).

## Confirmed numbers
- Lucas 2000: d = .26 semantic, .51 associative; by study .30 / .49; 3,882 subjects counting repeats, 2,243 after correction; N = 188 vs 72 for 80% power.
- SPP: 1,661 targets, 768 subjects, 4 universities; first-associate LDT priming 26 ms (200 SOA) and 20 ms (1,200 SOA) vs 42 and 60 ms in Hutchison 2008; 283 shared pairs; largest item effect 262.29 ms.
- HippoRAG: avg R@2/R@5 57.4/72.9 vs 53.9/65.6 (ColBERTv2); 2Wiki R@5 89.1 vs 68.2; HotpotQA 77.7 vs 79.3; all-recall AR@5 avg 52.0 vs 37.4; 2Wiki 75.7 vs 37.1.
- SYNAPSE: avg F1 40.5; no fan effect 36.1 (open-domain 25.9 -> 16.8); no node decay 30.7 (temporal 50.1 -> 14.2); no activation dynamics 30.5; graph structure removed 32.9; 814 vs 16,910 tokens; low-similarity drop 5.3% vs 43.1%.
- Query-aware SA: MuSiQue F1 41.68 vs 34.27 without gate; 2Wiki 55.00 vs 51.44; 1->2 hops +18.8 / +12.7 F1.
- SA-RAG: table values (MuSiQue 46 -> 75, 2Wiki 48 -> 87 correctness, phi4) confirmed.
- SpreadPy: d = 0.37 -> 0.61 timing, 0.78 magnitude confirmed; aphasia contrasts up to 1.47 appear in the table.

## Corrections made
1. a12 mislabels Lucas by task. Correct: paired lexical decision d = .33; continuous LD d = .27 (16 obs); mixed-list LD d = .26 (23 obs); naming d = .16. Use b02, not a12.
2. b16 says "query nodes only" scored 57.4/72.9. That is the full HippoRAG row (table layout merged them). Seed-only (query nodes only) is 50.7/56.2 avg; query nodes plus neighbours without PPR is 46.2/58.4; full is 57.4/72.9. Conclusion in b16 and c02 (spread beats seeds, neighbour stuffing is worse than spreading) stands, but the neighbour-stuffing variant is not worse than seeds only on R@5 (58.4 vs 56.2); it is worse on R@2 (46.2 vs 50.7). So a21 and c02 "neighbours worse than seed alone" holds for R@2 only.
3. HippoRAG cost claim: abstract says 10-20x cheaper, body and appendix say 10-30x. Use "10-30x (abstract says 10-20x)".
4. SA-RAG "39% absolute": the abstract says absolute, the intro and results text say "relative". The tables support absolute points (2Wiki 87 vs 48 = +39 points, phi4, 100 questions). Use 39 points, best case, 100 questions.
5. a25 phrase "improved answers" hides that on 2Wiki the method is about 15 F1 below HippoRAG (55.00 vs 70.33) and on MuSiQue F1 below QAFD-RAG (41.68 vs 47.99). Use b19.
6. a23 "up to 23% multi-hop" was not found in the table; multi-hop F1 is 35.7 (vs A-Mem 27.0). Use the table.

## Contradictions between sources
- Mediated priming: de Groot (1983, 7 experiments, via Hutchison) found none; strategy-controlled studies found 8-32 ms. Chwilla and Kolk: 25 ms n.s. vs 32 ms sig. Unresolved.
- Lucas (pure semantic priming exists) vs Hutchison (2003) (only some relation types prime automatically; category coordinates do not).
- Priming magnitude: 42/60 ms (2008) vs 26/20 ms (SPP) on the same kind of pairs.
- SYNAPSE adversarial F1 96.6 reflects refusal gating; gate on/off moves it 96.6 vs 67.2, so adversarial gains are a design effect.
- Decay: Query-aware paper finds decay hardly matters; SYNAPSE finds node decay is critical for temporal questions. Both can hold (different tasks).

## Weak spots
- Almost all 2024-2026 LLM results are single-lab, preprints, authors' own baselines. HippoRAG, SYNAPSE, SA-RAG, Query-aware, HeLa-Mem: no independent replication of the spreading step itself (Han et al. 2025 tests graph RAG broadly, not SYNAPSE).
- SA-RAG uses 100 questions per set; decay chosen on about 10 questions.
- HippoRAG's PPR is not decaying spread with threshold; the match to Collins and Loftus is by analogy.
- No test compares spreading activation against plain query rewriting or reranking at equal tokens inside an agent loop.
- Table layouts from pdftotext were scrambled in places (HippoRAG ablations); corrected here by reading adjacent rows.

## Seen only in snippets or secondhand (opened: false)
Collins and Loftus 1975, Collins and Quillian 1969, Meyer and Schvaneveldt 1971, Neely 1977, Anderson 1983, Posner and Snyder 1975, de Groot 1983, Crestani 1997, Jumelet et al. 2024. Their theory details and all RT values come from Hutchison 2003, Lucas 2000, Heyman 2016 or paper citations. Misra 2020 is partly confirmed (c12/c13 opened; b24 was only a search summary).

## GAPS
1. Does spreading-activation retrieval (code-run, 2-3 hops, gated by query similarity) beat dense retrieval plus a single model rewrite at equal tokens on our own tasks, split single-hop vs multi-hop?
2. What is the break-even question type: when does graph spread lose (HotpotQA, NQ single-hop) and can a cheap router predict it?
3. How much of the SYNAPSE gain survives independent re-implementation and equal-length baselines (authors' own runs, code unreleased at writing)?
4. Which edge types matter in an agent memory graph: co-occurrence/association versus embedding similarity versus LLM-extracted relations (Hutchison association vs feature overlap dispute)?
5. What fan-out normalisation (fan effect) and hub cap is best, and does it matter once a query gate is used?
6. Does spread reach hold at 2 hops for a growing memory (hundreds of thousands of nodes), and does noisy OpenIE extraction erase the gain?
7. How should the agent seed the graph (NER-to-node 87.1 vs query-to-node 74.6 recall in HippoRAG 2) when its own queries are free-form thoughts?
8. Is there evidence that human-like rank effects (primary associate matters more than strength) carry to embedding neighbours in LLM memory?
9. Do LLM-generated association networks (Abramski 2024) bias retrieval toward stereotypes (Abramski 2026), and how do we audit that?
10. Can a learned stop rule replace fixed T = 3 depth, given that gains vanish past 3 hops and four steps double latency?

## Gap search results (evidence_d.jsonl d01-d19; claims K23-K31 added, K07/K08/K13/K17 updated)

Method: full-text pdftotext of HippoRAG 2, Han et al. (RAG vs GraphRAG), GraphRAG-Bench, EA-GraphRAG, GraphRAG-Router (abstract and intro only), HeLa-Mem, SuperLocalMemory V3.3, Stop-RAG, TreeHop, HALT, and two Abramski papers. WebSearch budget was exhausted by other agents, and the arXiv, Semantic Scholar and OpenAlex APIs were rate-limited, so discovery used arXiv search pages.

Correction to the gap list: gap 7 numbers are mislabelled. In HippoRAG 2 Table 4 (recall@5 avg) the full query-to-triple design is 87.1, NER-to-node is 74.6, query-to-node is 59.6, no passage nodes 81.0, no triple filter 86.4 (d01).

- Gap 1 (spread vs dense plus rewrite at equal tokens): STAYS OPEN. Spread over passages costs about the same tokens as dense (1,008 vs 879, d09), but no source runs spread against dense plus a rewrite. Closest baseline: TreeHop (d16). Needs our own test (K31).
- Gap 2 (break-even and router): CLOSED in direction. Three independent lines show dense wins single-hop lookup (NQ F1 64.78 vs 61.03; LongMemEval single type 85.90 vs 78.85; GraphRAG-Bench Level 1) and graph wins multi-hop by about 3 points on independent runs (d05, d08, d13). A cheap router works: 65.1 to 71.6 accuracy (d10), and simple selection or concatenation also helps (d06). Open detail: routers were trained on benchmark questions, not free-form agent thoughts.
- Gap 3 (SYNAPSE independent re-implementation): STAYS OPEN. SuperLocalMemory V3.3 re-implements the SYNAPSE formula but only inside a 7-channel system, on 304 questions, and credits its gains to other parts (d14). K17 downgraded to contested.
- Gap 4 (edge types): PARTLY CLOSED. Triples-only graphs are weak (NQ F1 34.28 vs 64.78 dense; d07); edges must lead back to text. Co-activation edges work modestly (-2.6 F1 without spread, d12). No equal-footing comparison of the three edge types (K26).
- Gap 5 (fan-out and hub cap with a query gate): STAYS OPEN. No new source tests this. Only SYNAPSE (no fan effect -4.4 F1) and the query-aware paper (decay hardly matters) exist.
- Gap 6 (scale and OpenIE noise): PARTLY CLOSED. HippoRAG 2's lead held through 4x growth but accuracy still fell (d03); about 34% of answer entities are missing from extracted graphs (d06); seeding failures dominate misses (d04). Nothing tested at millions of nodes.
- Gap 7 (seeding): CLOSED in direction. Query-to-triple plus passage seeds beat entity and bare-node seeding by 12.5 and 27.5 recall points (d01). Not tested on free-form thoughts.
- Gap 8 (rank effects in embedding neighbours): STAYS OPEN. No source found that tests primary-associate rank effects on embedding neighbours.
- Gap 9 (stereotype bias and audit): PARTLY CLOSED. An audit recipe exists (d18) and LLM association graphs are narrower than human ones (d19). The Abramski 2026 retrieval-bias paper named in the gap was not found; no study shows a retrieval output shift.
- Gap 10 (learned stop): PARTLY CLOSED. Learned stop gains 1-3 F1 and needs training (d15); a training-free evidence-coverage stop saves 17-45% of loops without losing EM (d17). Fixed T=3 stays a sound default. None of these was tested on spreading depth.

Still weak after this pass: almost every new graph-memory number is again from the method's own authors; the independent Han et al. test shows smaller gains than the original papers. HeLa-Mem's table and text disagree on multi-hop F1 (36.04 vs 40.14).
