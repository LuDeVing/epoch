# Knowledge networks: deep document

*Subfield E15.03 of science of science. Scope: links among concepts and gaps. Evidence files: evidence_a-d.jsonl (ids a01-d16), claims.jsonl (K01-K21), critique.md. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Earlier deep documents in this series (memory, analogy, creativity, novelty) are not repeated; this file links to them where they overlap.*

## 1. What it is

A knowledge network is a graph built from the scientific literature. Nodes are concepts (or chemicals, genes, materials, papers, authors). An edge means two nodes appear together: in one abstract, one paper, one citation, or one claimed relation. Edges carry a date. So the graph has a history, and the history can be cut at any year to test prediction.

The subfield asks three questions.
1. How does the graph grow? Which pairs link next? Where are the gaps?
2. How do scientists choose what to study inside it? Do they follow hubs, or jump?
3. Can a program use the graph to find new ideas, and are those ideas any good?

For our agent the graph is a model of memory and analogue retrieval. The agent keeps notes, past attempts and retrieved sources. These can be stored as a flat list (vector search) or as a linked graph. The science-of-science results tell us (a) which links in a graph carry future value, (b) how humans search such graphs badly, and (c) what the LLM versions of graph memory actually gain, at what token cost.

Important limit: almost all human-side results are population statistics on papers. They do not describe one reasoner. The LLM-side results (HippoRAG, GraphRAG, Mem0, Zep, A-Mem, idea-generation studies) are closer to our agent, but most use the authors' own benchmarks and LLM judges.

Links to parallel subfields (not covered here): Search over thoughts; Epistemic diversity; Novelty measurement; Peer review and replication; Scientific discovery systems; Semantic memory network structure; Analogy and distant sources; Vector-space relational similarity.

## 2. History and theories in depth

**Literature-based discovery (1986).** Swanson linked two literatures with no shared citations, fish oil and Raynaud's syndrome, through intermediate terms (blood viscosity, platelet aggregation). The idea: public knowledge holds undiscovered links between disjoint literatures. [M] Not opened this session (a31). It is the root of every method below: find A-B and B-C, propose A-C.

**Network models of problem choice (2015).** Rzhetsky, Foster, Foster and Evans modelled biomedicine as a network of chemicals and published relations. A scientist chooses the next study by node importance (degree) and difficulty (distance). They fitted these parameters every 5 years, 1975-2010, on 2,363,858 MEDLINE articles and 295,812 patents (30,060 chemicals, 1,338,753 relations). Result: science grows more conservative over time. Foster, Rzhetsky and Evans (2015) typed the moves: jump, new consolidation, new bridge, repeat consolidation, repeat bridge. Repeats are 85.8% of statements; new moves 14.2%. (a12-a17, b18, b19)

**Embedding the literature (2019).** Tshitoyan et al. trained word2vec on 3.3M materials abstracts (1922-2018) and ranked materials by cosine to "thermoelectric". Using only past abstracts, top predictions were studied later more often than random. No labels were needed. (a18-a21, b22)

**Concept networks and link prediction (2020-2025).** Krenn and Zeilinger built SEMNET from 750,000 quantum-physics papers and framed idea generation as link prediction. Science4Cast (2022) made it a benchmark on AI literature (64,719 nodes, about 18M edges). Gu and Krenn (2025) scaled to 21M papers and added citations (impact layer). (a01-a07, b01-b05)

**Human-aware graphs and surprise (2023).** Sourati and Evans added authors to the graph; Shi and Evans scored surprising content-context combinations. These show the graph needs people-behaviour to predict, and that avoiding the crowd finds slower, "alien" ideas. (a25-a27, b15-b17, b20, b21)

**LLMs enter (2023-2026).** SciMON used a literature knowledge graph as retrieval memory for LLM ideas (2023). Si et al. ran the large blind expert study (2024), then the execution study (2025). Gu and Krenn's SciMuse put graph-chosen concept pairs into LLM prompts and had group leaders rate 4,451 ideas. In parallel the memory community built graph memory: HippoRAG (2024), GraphRAG (2024), A-Mem, Zep, Mem0 (2025), then neutral comparisons (Han et al., Xiang et al.). (a08-a11, a22-a24, c11-c13, d01-d16)

**Entrenchment.** Chu and Evans (2021): in large fields (1.8 billion citations, 90 million papers, 241 subjects) more papers do not turn over the canon; it ossifies. [M] abstract only (a30).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Link prediction on a quantum-physics concept graph | AUC 0.85 for 2017 state, 5-year horizon; 6,368 concepts, over 1.7M edges, 750k papers; only about 5% of pairs linked; test restricted to pairs sharing under 20% neighbours | Krenn & Zeilinger 2020 (a01-a03, b01, c01) | [S] one group |
| Same at larger scale | AUC 0.93-0.98; 141 features (41 network); four model types within about 0.01 (fcNN 0.963, XGBoost 0.960, Transformer 0.957, forest 0.953) | Gu & Krenn 2025 (a06, b05) | [S] |
| Strong vs new links | Links formed 3+ times: AUC about 99%; single new link: up to 0.93 | Krenn et al. 2022 (b02, c02) | [S] |
| Impact prediction is harder | Low vs at least 100 citations: AUC above 0.7 (test), above 0.67 (evaluation); average 0.029 citations over 10^7 pairs | Gu & Krenn 2025 (a07) | [S] |
| Hand-crafted features beat learned | Ten methods; learned-only often below AUC 0.6; augmentation +0.02 AUC | Krenn et al. 2022 (b03, c18) | [S] |
| Networks centralise | Clustering 0.919 (1999) to 0.650 (2013); edges concentrate in hubs; doubling time of AI papers about 23 months | Krenn et al. 2022 (b04, b24, c02) | [S] |
| Novel links sit at distance 2 | Most published links join already-linked chemicals (distance 1); most novel links join chemicals two steps apart (triadic closure); other distances very rare | Rzhetsky 2015 (a13, b19); Krenn 2020 (c17) | [E] |
| Science is conservative | Repeats 85.8% vs new 14.2%; new bridges and consolidations 12.4% vs jumps 1.8% | Foster 2015 (a16) | [E] |
| Rare strategies pay more, not enough | Jumps and new consolidations get more citations; prize-winner articles (137 prizes) enriched for new chemicals and relations | Foster 2015 (a17); Rzhetsky (a15) | [E] |
| Current strategy is inefficient for mature networks | Most efficient at about 13% discovered; at 50% discovered relative loss: optimal 33.6, coordinated 13.4, MEDLINE 95.7, random 271.4; over 3x costlier than best alternative | Rzhetsky 2015 (a14, b18) | [E] (model-based) |
| Embeddings rank untested materials | Top-10 power factor 40.8 vs 11.5 (3.6x candidate mean) and 17.0 (2.4x known thermoelectrics); 32% of first 150 predictions already studied elsewhere. The "8 times more likely than random" figure was NOT found on recheck | Tshitoyan 2019 (a18-a21, b22; critique) | [S] |
| Adding authors helps discovery prediction | Up to 400% better precision; drug repurposing 42% vs 10-12% content-only (350-400%); materials about 100% gain; removing authors: 48/50/58% vs 62/58/74% | Sourati & Evans 2023 (a25, a26, b15, b16, c07) | [S] |
| Avoid the crowd | Wait time to human discovery rises with avoidance parameter; COVID-19 predictions above 0.4: none discovered in window | Sourati & Evans 2023 (b17, c08) | [E] with Shi & Evans |
| Surprise predicts hits | Surprising context combos about 4x as likely top-10% cited; content 2x; both about 5x; distinguishes real from random combos over 95% of the time | Shi & Evans 2023 (b20) | [E] |
| LLM ideas rated more novel than human ideas | Novelty 5.64 vs 4.84 (p<0.05); rerank 5.81; feasibility 6.34 vs 6.61 n.s.; 49 ideas per arm, 79 reviewers | Si et al. 2024 (a22, b09, b10) | [S] |
| ...but not after execution | 43 experts, 100+ hours each, 24 AI and 19 human ideas, 7 NLP topics, 181 reviews; AI scores fell 1.0-1.9 points, human flat; effectiveness 4.13 vs 4.78 n.s. | Si et al. 2025 (d13, d14) | [S] same group |
| LLM idea diversity collapses | 4,000 seeds yield about 200 non-duplicates (cosine over 0.8) | Si et al. 2024 (a23, b11, c23) | [S] |
| LLM self-ranking of ideas is near chance | 53.3% on idea data vs 56.1% human reviewer agreement; 71.4% on ICLR accept/reject | Si et al. 2024 (b12, c19) | [C] |
| Retrieval lifts outcome prediction; fine-tuning more | 38.8% to 53.0% with paper retrieval; fine-tuned GPT-4.1 77% (51.9% before); 64.4% vs 48.9% for 25 experts (NLP); frontier models near random | Wen et al. 2025 (d15, d16) | [S] |
| Graph pairs not rated more interesting | Mean 2.40/5 (2.403 +/- 0.020); 24.9% rated 4-5 (1,107 ideas); high-citation pairs 2.350 vs random 2.446 vs titles-only GPT 2.414; 110 of 267 leaders (41.2%) | Gu & Krenn 2026 (b06, b08, c03) | [S] |
| Interest falls with connectedness and distance | Degree rho -0.166; PageRank -0.176; semantic distance -0.223 (N = 2,996) | Gu & Krenn 2026 (c04) | [S] |
| Interest is weakly predictable | AUC 63.2 (net), 67.44 (GPT-4o zero-shot) | Gu & Krenn 2026 (c05) | [S] |
| LLM ideas vs PhD ideas, same raters | Rated 4-5: human 29.1% (n=148), GPT-4 25.0% (n=100), GPT-5.2 32.5% (n=160) | Gu & Krenn 2026 (c06) | [S] |
| KG neighbours in prompts: modest | GPT4FS+KG preferred 52%/55% on two criteria, mostly ties; real paper idea beat best model idea in 85% | SciMON (a09, c22) | [S] |
| Iterative novelty boosting works | Round 1: 54.4-55.6% more novel (GPT4FS, semantic); KG 46.7%; round 2: 57.8%; 88.9% substantially different; novelty never dropped; 70 instances | SciMON (a10, b13) | [S] |
| HippoRAG beats flat on some multi-hop | R@5 2Wiki 89.5 vs 68.2; MuSiQue 52.1 vs 49.2; HotpotQA 76.2-77.7 vs 79.3 (loses); average 72.9 vs 65.6; 10-30x cheaper than iterative retrieval (abstract: 10-20x) | Gutierrez 2024 (c11, c20) | [E] with d-series |
| HippoRAG 2 closes the gap but only by a few points | Avg F1 over 7 sets: 59.8 vs 57.0 flat; recall@5 2Wiki 90.4 vs 76.5, MuSiQue 74.7 vs 69.7, HotpotQA 96.3 vs 94.5; NQ 78.0 vs 75.4 | Gutierrez 2025 (d01, d02) | [S] |
| Unified test: flat wins single-hop | NQ F1: RAG 64.78, HippoRAG2 61.03; temporal: RAG 30.70 vs Local-GraphRAG 50.60 | Han et al. 2025 (d04) | [E] with d08 |
| Token-matched flat erases the graph edge | MultiHop-RAG: RAG 67.02; token-matched RAG 69.33; Local-GraphRAG 69.01; temporal 36.71 vs 50.60 (about 14 points) | Han et al. 2025 (d05) | [S] |
| LLM-built graphs lose content | About 65.8% (HotpotQA) and 65.5% (NQ) of answer entities in graph; triplets-only HotpotQA F1 25.02 vs 60.04 | Han et al. 2025 (d06) | [S] |
| Community-summary GraphRAG on global questions | Comprehensiveness win 72-83% (podcast), 72-80% (news); diversity 75-82% and 62-71%; about 1M-token corpora; LLM judge; text-summarisation close behind | Edge et al. 2024 (c12, c21) | [S] |
| Graph memory build cost | Index input tokens: HippoRAG 2 9.2M, LightRAG 68.5M, GraphRAG 115.5M, RAPTOR 1.7M, flat none (11,656 passages); query prompts: flat 879-954, HippoRAG 2 about 1.0k, HippoRAG 1 about 7.2k, MS-GraphRAG local about 39k, global about 331k, LightRAG about 100k; QA time 12.1 s flat vs 99.5 s HippoRAG 2 | Gutierrez 2025 (d03); Xiang 2026 (d09) | [E] |
| Linked-note agent memory | A-Mem 643 vs MemGPT 16,910 tokens per answer on LoCoMo; A-Mem re-run in Mem0 paper: J 48.38 | Xu 2025 (c13); Chhikara 2025 (d10) | [C] |
| Flat extracted memory vs full context | LoCoMo J: full 72.90 (26,031 tokens); Mem0g 68.44 (3,616); Mem0 66.88 (1,764); Zep 65.99 (3,911); LangMem 58.10 (127) | Chhikara 2025 (d10, d11) | [S] vendor |
| Temporal graph memory | LongMemEval-s: gpt-4o-mini full 55.4% (115k tokens) vs Zep 63.8% (1.6k); gpt-4o 60.2% vs 71.2%; temporal 45.1 to 62.4; single-session-assistant 94.6 to 80.4; no flat-vector baseline | Rasmussen 2025 (d12) | [S] vendor |
| LLMs predict neuroscience results | 81.4% vs experts 63.4% (top-20% subset 66.2%); 1.3B-token fine-tune +3% | Luo et al. 2024 (c14) | [S] |

## 4. Mechanisms and models

**4.1 Concept co-occurrence graph (SEMNET).** Extract concepts from abstracts (RAKE plus filtering). Node = concept. Edge = two concepts in one abstract; keep a year per edge. For each unlinked pair compute features: degrees, paper counts, cosine similarity of neighbour vectors, path counts of length 2-4, distances, Jaccard, PageRank. Feed to a small net (4 dense layers, 17 features) or gradient boosting. Label = linked within 3-5 years. Train on an early year, test on a later year never seen. Evaluate AUC. Restrict to pairs with under 20% shared neighbours to avoid trivial cases. (a02, c01, c18)

**4.2 Problem-choice model.** Each study picks a node with probability rising in degree and falling in distance from current knowledge. Fit by simulated annealing and MCMC per 5-year window. Simulate alternative strategies on a sample network and measure cost per newly found link. Mixed central-and-peripheral strategies win; the conservative one is best only up to about 13% coverage. (a12-a14)

**4.3 Move typology.** Classify each new statement as: jump (new entities), new consolidation, new bridge, repeat consolidation, repeat bridge. Count shares. This is a cheap audit of any exploration log. (a16)

**4.4 Embedding dot product.** Train skip-gram (200 dims) on domain text. Rank candidates by cosine to a property word. Only the target word changes per property; no retraining. (a18-a21)

**4.5 Human-aware hypergraph.** Hyperedge links materials, properties and the people who study them. Random walks and embeddings over it. Avoidance parameter: subtract a term for how likely a human community is to reach the candidate. Higher avoidance gives slower, rarer discoveries. (a25, a27, b17)

**4.6 Surprise score.** Hypergraph over content (keywords) and context (cited journals). Surprise = how unlikely the observed combination is under a null model. (b20)

**4.7 Personalised PageRank retrieval (HippoRAG).** Offline: LLM extracts entity-relation triples from each passage; build a graph linking entities to passages. Online: extract entities from the query, seed a personalised PageRank at those entities, rank passages by the resulting score. One step does multi-hop. HippoRAG 2 links by whole-query-to-triple matching, adds passage nodes and a recognition step. Keep raw passages attached. (c11, d01-d03, d06)

**4.8 Community-summary GraphRAG.** Build entity graph, detect communities (Leiden), write a summary per community level, answer global questions by summarising partial answers per community. Cost is high: the global query used about 331k prompt tokens. (c12, d09)

**4.9 Zettelkasten memory (A-Mem).** Each memory is a note with keywords and tags. A new note triggers: retrieve neighbours, let the model write links, update old notes. (c13)

**4.10 Temporal graph memory (Zep).** Facts are edges with valid-from and valid-to times; new facts invalidate old ones. Gain shows on temporal and multi-session questions. (d12)

**4.11 SciMON-style loop.** Retrieve inspirations by three routes (semantic, KG, citation neighbours); generate; compare to retrieved prior work; rewrite if too similar; repeat up to 2 rounds. (a08, a10)

## 5. What holds up

**Holds.**
- Distance-2 closure is where new links appear (two independent sources, different fields) [E].
- Conservative search with rare, better-paying jumps [E] (Rzhetsky, Foster, Shi & Evans agree).
- Graph retrieval is task dependent [E]: flat wins single-hop detail; graph helps multi-hop, temporal and comparison questions (Han, Xiang, HippoRAG, Mem0). The edge is about 2-3 points overall, about 14 points on temporal questions at matched tokens.
- Graph memory costs a lot to build [E] (HippoRAG 2: 9.2M input and 3.0M output tokens for 11,656 passages).
- LLM ideas judged on paper do not predict execution [S, plausible with d14, d15].

**Failed or weak.**
- Graph-predicted pairs were not more interesting than random (2.350 vs 2.446). High AUC measures whether a link will form, not whether it is valuable (b23).
- Novelty gain of LLM ideas did not survive execution (d13). Same group did both studies; no independent replication found.
- Token-matched flat RAG erases the overall graph edge (69.33 vs 69.01).
- Graph-only retrieval trails flat badly because the graph covers only about 65% of answer entities.
- Structure-only baselines (RAPTOR 56.8, Proposition 61.2) did not beat ColBERTv2 65.6 on average; a graph with PageRank did (c20).
- HippoRAG 1 lost on HotpotQA; HippoRAG 2 fixed it, with a different reader and retriever setup, so not a clean replication.
- Mem0's own paper shows its graph variant adds 1.56 points at twice the tokens and nothing on single- or multi-hop (d10, d11); A-Mem re-run scored 48.38 against its own claims (c13 vs d10). Contested.

**Moderators.** Question type (single-hop vs multi-hop vs temporal vs global); corpus size and age; whether raw text stays linked to graph nodes; reader model; hub centralisation; sparsity of the literature (people-aware gains are largest when the literature is sparse).

**Interventions that worked.** Hand-crafted network features (over learned ones); data augmentation (+0.02 AUC); author edges (up to 400%); paper retrieval for outcome prediction (+14 points from below chance); iterative novelty boosting (about 55% of ideas more novel per round); temporal edges (Zep).

**Interventions that did not.** Prompt variants in SciMuse pilots; KG neighbours for idea quality (mostly ties); fine-tuning on 1.3B tokens (+3% on BrainBench); learned-only features (often AUC under 0.6).

**Selection and judge caveats.** SciMuse: only 41.2% of leaders took part (110/267; 138 no reply). GraphRAG and A-Mem used LLM judges and the authors' own benchmarks. Mem0 and Zep are vendor papers; Zep has no flat-vector baseline, so graph and compression are confounded.

## 6. Language models

**Idea generation.** Retrieval-augmented agent ideas were rated more novel than 49 expert ideas (5.64 vs 4.84), less feasible (6.34 vs 6.61, n.s.). After 43 experts executed the ideas the AI scores fell 1.0-1.9 points and the ranking flipped, not significantly. LLM-vs-PhD ideas in SciMuse were similar (GPT-5.2 32.5% rated 4-5 vs human 29.1%). Diversity: 200 of 4,000 seeds unique.

**Using a graph in the prompt.** SciMON: KG neighbours gave small human-preferred gains (52-55%, mostly ties). Iterative comparison with prior work raised novelty in about 55% of ideas per round. SciMuse: graph-chosen pairs did not beat titles-only GPT (2.350 vs 2.414). Graph control worked (you can steer which pair is used) but quality did not rise.

**Judging ideas.** Frontier models are near chance on which idea works (53.3% on Si's data); 71.4% on ICLR accept/reject. Paper retrieval gave 38.8% to 53.0%; fine-tuning 77%. Zero-shot GPT-4o predicted ratings of interest at AUC 67.44.

**Graph memory.** HippoRAG: 2Wiki R@5 89.5 vs 68.2 (Contriever vs best flat). HippoRAG 2: avg F1 59.8 vs 57.0. Neutral studies: flat wins NQ (64.78 vs 61.03); graph wins temporal; token-matched flat nearly ties overall. GraphRAG wins global summarisation (72-83%) at very high token cost. Mem0 flat memory keeps about 92% of full-context score (66.88 vs 72.90) at about 7% of tokens (1,764 vs 26,031). Zep beat full context on LongMemEval-s (63.8% vs 55.4% mini; 71.2% vs 60.2% gpt-4o) at 1.6k vs 115k tokens, but lost on single-session-assistant (94.6 to 80.4).

**LLMs as literature models.** BrainBench: 81.4% vs 63.4% for experts at choosing the real abstract. Models absorb link structure, so they could fill the role of the embedding model in 4.4.

**Missing.** No study tests a graph memory inside a thinking scaffold at equal tokens. None tests distance-2 analogue retrieval for reasoning.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Keep memory flat by default. Route to a graph path only for temporal, comparison or multi-hop lookups | memory | [E] | d04, d05, d08, d11, c11, K14, K18 |
| Count build plus query tokens for any graph memory; use a graph only when memory is large and long-lived | G7 | [E] | d03, d09, d10, K19 |
| Retrieve distance-2 neighbours (shared-neighbour concepts) as analogue candidates alongside nearest-embedding | memory; analogue retrieval | [E] for the pattern in science, untested for reasoning | a13, b19, c17, K03 |
| Never rank ideas by model novelty rating or review-style scores; require an executable check | G8 (supports) | [E] with F01, F05 | a24, b12, d13, d14, d15, K21 |
| Keep raw text linked to any graph node (do not answer from triples alone) | memory | [S] but cheap and safe | d06, K20 |
| Audit exploration with the 5-move typology (repeat vs new) to detect over-conservative search | S3 open mode (log only) | [E] descriptive | a16, K08 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Distance-2 vs nearest-embedding analogues for reasoning items | memory; S3 | [S] | K03; no reasoning test |
| Explore/exploit mix (about 85/15) in analogue retrieval vs greedy | S3 | [C] | a16, b18; no direct test |
| Degree-penalised retrieval to fight hub bias | memory | [S] | b04, b24, c04 |
| Distant-neighbour seeding to raise unique-idea share | S3 open mode | [S] | a23, K10 |
| Iterative novelty-vs-prior-attempts rewrite (max 2 rounds) with code similarity gate | S3 open mode | [S] | a10, b13 |
| Avoid-the-crowd penalty vs agent's own prior outputs | S3 | [E] in science, untested in LLM | b17, b20 |
| Temporal edges (valid-from, valid-to) in session memory | memory | [S] vendor | d11, d12 |
| Source and tool edges ("who/what produced this note") | memory | [S] analogy from author edges | a25, b16, K06 |
| Retrieval-grounded self-ranking vs raw self-ranking | G5/G8 | [S] | d15, d16 |
| Embedding dot product to rank unseen analogue candidates | memory | [S] | a18-a21, K05 |

## 8. Concrete tests on our bench

All tests: both arms use equal total tokens including graph build; same items; code scores.

1. **Router test.** Item type: multi-session memory QA with lookup, temporal and multi-hop questions (LoCoMo-style, our own notes). Arms: flat vector only; graph only; router (flat default, graph for temporal or multi-hop). Metric: exact-match or J score by question type, tokens per answer. Expected: router at least flat on lookup, +5 to +14 points on temporal.
2. **Distance-2 analogues.** Item type: ARC or analogy items where a solved earlier item shares structure. Arms: top-k nearest embedding; top-k from two hops via shared concept tags; half and half. Metric: solve rate with analogue shown. Expected: mixed arm beats nearest by 2-5 points; effect unknown.
3. **Explore/exploit retrieval.** Arms: greedy top-k; 85/15 exploit/explore with random distant analogues; 70/30. Metric: solve rate and unique-approach count (code-clustered). Expected: higher diversity at equal solve rate.
4. **Hub penalty.** Arms: PageRank-style retrieval vs degree-penalised. Metric: share of retrieved notes from top 10% degree nodes; solve rate. Expected: lower hub share, no loss.
5. **Idea diversity (open mode, NoveltyBench).** Arms: bare resampling; graph-neighbour seeded; both with a code duplicate filter (cosine 0.8). Metric: unique share of 100 samples; NoveltyBench score. Expected: unique share from about 5% to above 10%.
6. **Novelty rewrite loop.** Arms: one-shot; one round of compare-and-rewrite against prior attempts; two rounds. Metric: code-judged distinctness and executable check pass rate. Expected: distinctness up on about 50% of items, check pass rate flat or lower; do not keep if pass rate drops.
7. **Grounded self-rank.** Items with known executed outcomes. Arms: model ranks pairs alone; model with retrieved prior results; random. Metric: pairwise accuracy. Expected: from about 50% to about 53% (d16); keep only if above 58%.
8. **Temporal edges.** Item type: facts that change over a session. Arms: flat store; flat plus valid-from and valid-to; full context. Metric: accuracy on "current value" questions. Expected: large gain on temporal items, small loss on single-session detail.

## 9. What does not transfer, and why

- Link prediction AUC (0.85-0.98) is about whether humans will co-mention concepts. It says nothing about whether a pairing is useful; SciMuse shows graph pairs no better than random. Do not use AUC as a goal.
- Citation and prize signals (Shi & Evans, Foster) are population outcomes over years. Our agent has seconds and an executable check.
- Author and people edges (Sourati & Evans) need a community. A single agent has none. The only analogue is source and tool edges, which are untested.
- 85/15 explore/exploit is a description of scientists, not a tuned optimum; the best ratio for retrieval is unknown.
- Hub centralisation is measured on growing literature graphs. LLM-built graphs are sparse (average degree about 1.5-13), so the effect may not exist.
- Fine-tuning gains (Wen 77%, BrainBench +3%) are outside the scaffold (no training).
- Community-summary GraphRAG needs 1M-token corpora and costs 331k tokens per global query; our sessions are far smaller.
- Idea ratings by human reviewers (Si, SciMuse) do not apply to checkable tasks; G8 already says run, not rate.

## 10. Open questions

1. Does graph memory beat flat memory inside a scaffold at equal tokens, by task type?
2. Do distance-2 analogues help reasoning, not only link prediction?
3. Is there a cheap check that separates useful from merely novel ideas?
4. How much does grounding improve self-ranking beyond 53%?
5. What explore/exploit ratio is best for retrieval?
6. Does hub bias exist in agent memory graphs?
7. Is Tshitoyan's "8 times" figure real? (Not found in recheck; Nature text unreachable.) Do embeddings rank well outside materials?
8. Do source and tool edges help a single agent?
9. Does Si et al.'s ideation-execution gap replicate outside NLP, by an independent group?
10. Which of graph vs compression drives Zep's gain?

## 11. Sources

Opened [V]; snippet or memory only [M].

- [V] Krenn & Zeilinger (2020) Predicting research trends with semantic and neural networks. https://arxiv.org/abs/1906.06843
- [V] Krenn et al. (2022) Predicting the Future of AI with AI (Science4Cast). https://arxiv.org/abs/2210.00881
- [V] Gu & Krenn (2025) Forecasting high-impact research topics via ML on evolving knowledge graphs. https://arxiv.org/abs/2402.08640
- [V] Gu & Krenn (2026) SciMuse. https://arxiv.org/abs/2405.17044
- [V] Wang et al. (2024) SciMON. https://arxiv.org/abs/2305.14259
- [V] Rzhetsky, Foster, Foster & Evans (2015) Choosing experiments to accelerate collective discovery. https://pmc.ncbi.nlm.nih.gov/articles/PMC4664375/
- [V] Foster, Rzhetsky & Evans (2015) Tradition and innovation in scientists' research strategies. https://arxiv.org/abs/1302.6906
- [V partial] Tshitoyan et al. (2019) Unsupervised word embeddings capture latent knowledge from materials science literature. https://doi.org/10.1038/s41586-019-1335-8 ; press summary https://www.sciencedaily.com/releases/2019/07/190703134059.htm (full-text "8 times" unverified)
- [V] Si, Yang & Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto & Yang (2025) The Ideation-Execution Gap. https://arxiv.org/abs/2506.20803
- [V] Sourati & Evans (2023) Accelerating science with human-aware AI. https://arxiv.org/abs/2306.01495
- [V] Shi & Evans (2023) Surprising combinations of research contents and contexts. https://pmc.ncbi.nlm.nih.gov/articles/PMC10039062
- [V] Qi et al. (2023) LLMs are zero-shot hypothesis proposers. https://arxiv.org/abs/2311.05965
- [V] Yang et al. (2024) Automated open-domain scientific hypotheses discovery. https://arxiv.org/abs/2309.02726
- [V] Gutierrez et al. (2024) HippoRAG. https://arxiv.org/abs/2405.14831
- [V] Gutierrez et al. (2025) From RAG to Memory: HippoRAG 2. https://arxiv.org/abs/2502.14802
- [V] Edge et al. (2024) From Local to Global: GraphRAG. https://arxiv.org/abs/2404.16130
- [V] Han et al. (2025) RAG vs. GraphRAG: A Systematic Evaluation. https://arxiv.org/abs/2502.11371
- [V] Xiang et al. (2026) When to Use Graphs in RAG (GraphRAG-Bench). https://arxiv.org/abs/2506.05690
- [V] Xu et al. (2025) A-Mem. https://arxiv.org/abs/2502.12110
- [V] Chhikara et al. (2025) Mem0. https://arxiv.org/abs/2504.19413
- [V] Rasmussen et al. (2025) Zep. https://arxiv.org/abs/2501.13956
- [V] Luo et al. (2024) LLMs surpass human experts in predicting neuroscience results. https://arxiv.org/abs/2403.03230
- [V] Ghafarollahi & Buehler (2024) SciAgents. https://arxiv.org/abs/2409.05556
- [V] Wen et al. (2025) Predicting Empirical AI Research Outcomes with Language Models. https://arxiv.org/abs/2506.00794
- [M] Chu & Evans (2021) Slowed canonical progress in large fields of science. https://doi.org/10.1073/pnas.2021636118
- [M] Swanson (1986) Fish oil, Raynaud's syndrome, and undiscovered public knowledge. https://doi.org/10.1353/pbm.1986.0087
- [M] Fortunato et al. (2018) Science of science. https://doi.org/10.1126/science.aao0185
