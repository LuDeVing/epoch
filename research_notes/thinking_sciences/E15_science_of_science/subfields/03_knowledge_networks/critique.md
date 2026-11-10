# Critique: E15.03 Knowledge networks (cross-check)

## Re-opened numbers (arXiv/PMC text, this session)
Confirmed: Krenn & Zeilinger AUC2017 = 0.85 and 1.7M edges (arXiv 1906.06843); Rzhetsky MEDLINE most efficient at 13% discovered; Sourati & Evans "up to 400%" and 42% vs 350-400%; Si et al. novelty 4.84 / 5.64 / 5.81, 4,000 seeds -> 200 non-duplicates, ranker 53.3% vs reviewer agreement 56.1%, Claude-3.5-Sonnet 71.4% on ICLR; HippoRAG 2Wiki R@5 89.5 vs 68.2, avg 72.9 vs 65.6; GraphRAG comprehensiveness 72-83% (podcast), 72-80% (news); SciMuse 2.40 mean, 24.9% = 1,107 ideas rated 4-5, 41.2% participation (110/267); BrainBench 81.4% vs 63.4%.

## Corrections
1. HippoRAG cost: abstract says 10-20x cheaper; body says 10-30x cheaper, 6-13x faster. Use "10-30x (abstract: 10-20x)".
2. a19 (Tshitoyan "8 times more likely than random, 3 times vs bandgap"): NOT found in the text re-read. Verified instead: top-10 mean power factor 40.8 vs 11.5 (3.6x) candidates and 17.0 (2.4x) known thermoelectrics; 32% of first 150 predictions already studied elsewhere. Treat "8 times" as unverified.
3. SciMuse mean is 2.403 +/- 0.020 in the paper body (rounded to 2.40 elsewhere).
4. Si et al.: novelty table is review-level (n=109 reviews per AI condition), p-values printed 0.00**; evidence lines quoting "p<0.05" are the idea-level test. Not a contradiction.
5. c03/b06 and c05 list AUCs for interest prediction (63.2, 67.44 GPT-4o); third method value (60.39) label unclear. Not re-opened.
6. Hazard: the shared scratch folder contained files with the same arXiv-like names from other agents; arXiv 2006.01905 is NOT Krenn (it is an unrelated algebra paper). Krenn is 1906.06843.

## Contradictions and tensions
- Link-prediction AUC 0.85-0.98 vs SciMuse: top-ranked graph pairs were NOT rated more interesting (2.350 vs random 2.446). Predicting that a link will be cited is not predicting that it is valuable. b07 has one comparison at 1.94 (weak, flagged).
- HippoRAG helps on 2Wiki and MuSiQue but loses on HotpotQA (76.2-77.7 vs 79.3): benefit depends on the task.
- Rzhetsky shows science is inefficient yet Foster et al. show conservative strategy is the common one and jumps are cited more: both can hold.

## Weak spots
- Most link-prediction evidence is one group (Krenn, Gu, Zeilinger); status downgraded to single-source.
- Si et al. is one study (49 ideas per arm, NLP only); LLM ideas judged by humans on paper, not executed.
- GraphRAG and A-Mem use LLM judges and the authors' own benchmarks.
- No study tests a knowledge-graph memory inside a thinking scaffold at equal tokens.
- Snippet-only or not opened: a30 (Chu & Evans, abstract), a31 (Swanson, memory), a32 (Fortunato review), b25, b26; b14 and c24 lack exact numbers; a29 lacks scores.
- Not re-opened: Shi & Evans 4x/2x/5x, Science4Cast clustering, Sourati 40%/20% author results, A-Mem F1 table (header alignment unclear), Qi et al.

## GAPS
1. Does a graph-structured memory beat flat vector memory for analogue retrieval inside a scaffold at equal tokens, and on which task types (2Wiki vs HotpotQA suggests it varies)?
2. Does retrieving distance-2 (triadic closure) analogues beat nearest-embedding analogues for reasoning, not just link prediction?
3. Can a cheap novelty-vs-correctness check separate useful from merely novel LLM ideas, given that experts rated graph-predicted pairs no better than random?
4. How much does self-ranking of ideas improve with external grounding, given ranker accuracy of 53.3% on idea data?
5. Does an explore/exploit mix (about 85/15 as in science) improve retrieval over greedy, and what ratio is best?
6. Does hub bias (rising centralisation) hurt agent memory, and does degree-penalised retrieval fix it?
7. Is the 8x claim in Tshitoyan et al. real (Nature text vs preprint), and do embeddings still rank well for non-materials domains?
8. Does adding "who/what source" edges (human-aware graph) transfer to a single-agent memory (source-and-tool links)?
9. Independent replication of Si et al. novelty gain outside NLP and with executed ideas.
10. Cost: what is the token overhead of building and querying the graph versus the gain (HippoRAG 10-30x cheaper than iterative retrieval)?

## Gap search results

Evidence is in evidence_d.jsonl (d01-d16, all opened this session). Search APIs (WebSearch budget, OpenAlex, Semantic Scholar, arXiv search) were rate-limited or used up, so I worked from known arXiv ids only. This left gaps 2, 5, 6, 7 and 8 without new primary sources.

**Closed or mostly closed**
- Gap 1 (graph vs flat at equal tokens): answered as task-dependent (d01, d04, d05, d08, d11). HippoRAG 2 fixes the HotpotQA loss (recall@5 96.3 vs 94.5). In a unified test flat RAG wins NQ (F1 64.78 vs 61.03). With token-matched RAG the overall graph edge vanishes (69.33 vs 69.01); the edge stays on temporal questions (36.71 vs 50.60). New claim K18; K14 updated.
- Gap 10 (cost): HippoRAG 2 indexing took 9.2M input and 3.0M output tokens on 11,656 passages; GraphRAG 115.5M; plain embedding none (d03). Query prompts: HippoRAG 2 about 1.0k vs flat 0.9k; MS-GraphRAG global 331k (d09). The old 10-30x claim is vs iterative retrieval only. New claim K19.
- Gap 9 (Si et al. outside NLP, executed ideas): the same group's execution study shows the novelty gain does not survive (AI -1.0 to -1.9 points; human flat; d13). Replication outside NLP by an independent group was not found. Partly closed.
- Gap 4 (self-ranking with grounding): off-the-shelf models near chance; retrieval 38.8 to 53.0; fine-tuning 77 (d15, d16). Training is outside our scaffold, so the legal gain is the retrieval part (about +14 points from a below-chance start). Partly closed.
- Gap 3 (cheap useful-vs-novel check): none found. Review scores correlate weakly with executed outcomes (d14). Stays open; K21 records the negative result.

**Stayed open**
- Gap 2 (distance-2 analogues for reasoning): no study found. Only the link-prediction evidence (K03) stands.
- Gap 5 (explore/exploit ratio): no direct test found. Only iterative retrieval vs single-pass (d07).
- Gap 6 (hub bias): the only new data is that LLM-built graphs are sparse (average degree about 1.5 to 13; d09), so hub centralisation may not apply to them. Untested.
- Gap 7 (Tshitoyan "8 times"): could not reach the Nature text or a preprint (Nature redirected to login, OSTI refused). Still unverified; non-materials ranking also untested.
- Gap 8 (source and tool edges): no direct test. Zep and Mem0 add temporal and entity edges, not source or tool edges; the temporal gain (d11, d12) is the nearest evidence.

**Caveats on this round**: Mem0 and Zep are vendor papers with their own evaluations; Zep has no flat-vector baseline, so graph and compression are confounded (d12). Several PDF tables were garbled; unaligned numbers were left out.
