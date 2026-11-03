# Semantic networks and spreading activation: deep document

*Subfield A06.06. Evidence ids (a01-a27, b01-b25, c01-c25, d01-d19) and claim ids (A06.06-K01 to K31) refer to the jsonl files in this folder. Numbers follow the corrections in critique.md. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Memory is drawn as a network. Concepts are nodes. Links join related concepts. When a concept is used, it gets activation. The activation flows along the links to neighbours, gets weaker with each step, and a node must pass a threshold before it is "used". This is spreading activation (a01, a04).

Two research lines use the idea.

1. Cognitive psychology. It explains semantic priming: a word is recognised faster after a related word (nurse then doctor) than after an unrelated one (carrot then doctor) (a02, a03). Key works: Collins and Quillian (1969), Collins and Loftus (1975), Neely (1977), Anderson (1983).
2. Information retrieval and AI. Constrained spreading activation over term and document networks (Crestani 1997, c21). Since 2024 it is also used over knowledge graphs and agent memory built by language models (HippoRAG, SA-RAG, SYNAPSE, HeLa-Mem; a20-a25, c01-c11).

Minimal algorithm (a01): give source nodes weights. Pass weight to linked nodes. Decay it at each step. Drop nodes under a threshold. Read out the top nodes. Discrete weights are called marker passing.

Why it matters for our agent. It is the oldest, best-studied model of "a cue should lift its neighbours, not only exact matches". It maps to S3 (grounded retrieval from memory) and to the memory store. It is run by code, so it fits guardrail G5 (code selects) and G1 (cheap automatic pass first, costly search only on a signal).

Scope warning. Word-level semantic priming has large datasets and is real. Social or behavioural priming is a different literature that hit the replication crisis from 2012 (a03). Do not mix them (K22 [E]).

## 2. History and theories in depth

Note on sources. The original 1969-1983 papers were not opened (a04, a05, a06, a07, a26, a27: opened false). Their content below comes from Hutchison (2003), Lucas (2000), Heyman et al. (2016) and later papers that describe them. No original reaction-time values from those papers are quoted.

**Collins and Quillian (1969).** Hierarchical network. Facts are stored at the highest node where they apply (a05). Retrieval time depends on how many links are crossed. A strict hierarchy is too rigid. A free weighted graph is more flexible for agent facts.

**Meyer and Schvaneveldt (1971).** First lexical-decision priming result. Related pairs such as bread-butter were judged faster than unrelated pairs (a03, a06). The pairs came from association norms. So association and meaning overlap were confounded from the start.

**Collins and Loftus (1975).** The spreading-activation theory. As relayed in secondary sources (a04, c20): concepts are nodes. Link length shows relatedness. Activation spreads in parallel, fades with distance and time, and must pass a threshold. Relatedness between two concepts is found where spread from both meets. A lexical network is kept apart from a semantic network.

**Posner and Snyder (1975) and Neely (1977).** Two processes. First, fast automatic spread with no inhibition. Second, a slower, limited-capacity attention process that follows expectancy (a07, a27, b09). Stimulus onset asynchrony (SOA, the time between prime and target) is used to separate them. A short SOA (under about 200-250 ms) is taken to isolate the automatic part. Hutchison (2003) warns that no universal SOA cleanly separates the two (a08).

**Anderson (1983).** ACT-style activation with link strengths and the fan effect: the more links leave a concept, the less activation each link gets (a26). This is the formal reason for hub damping.

**De Groot (1983).** Seven experiments found priming only for direct associates and none for two-link (mediated) pairs in standard lexical decision (a09, b04). Later work found small mediated effects only when strategy was blocked (b05).

**Lucas (2000) versus Hutchison (2003).** Lucas, a meta-analysis, argued that priming without association exists (a11, b01). Hutchison re-checked each study. She concluded that automatic priming comes from both association strength and feature overlap, and that category coordinates and perceptually similar items do not prime automatically (a10, b03). The dispute is not settled (K05 [C]).

**Rival accounts.** Mediated priming may come from co-occurrence or shared meaning, not from a two-step link. McNamara found no link between plausibility of shared meaning and effect size (r = -.017) (b06). Livesay and Burgess found no link between priming strength and lexical co-occurrence (b06). Hutchison and Balota (2005) tried to pull meaning and association apart in false memory, in 6 experiments. Veridical memory differed by list type, but false memory of the critical item did not (b10).

**Big data era.** The Semantic Priming Project (SPP, Hutchison et al. 2013) gave 1,661 targets and 768 subjects (a13, b07). Heyman, Hutchison and Storms (2016) used it to show that item-level priming correlates across tasks only at the short SOA (b08).

**Machine lineage.** Crestani (1997) surveyed constrained spreading activation in IR (c21). Later analysis showed pure unconstrained spread converges to a near query-independent state. So hop limits, fan-out limits, decay below one and thresholds are required (c08, K11 [E]). Personalized PageRank in HippoRAG (2024) is a close kin, not the same algorithm (a20). SA-RAG, SYNAPSE, the query-aware gate paper and HeLa-Mem (all 2025-2026) implement decayed, thresholded spread directly (c07, c09, b18, c11).

## 3. Core findings with exact numbers

Human work first, then machine work. Numbers are as corrected in critique.md.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pure semantic priming exists but is small; associative priming is about double | 26 studies. Semantic: 116 observations, mean d = .26 (by study .30). Associative: 73 observations, d = .51 (by study .49, 20 studies). 3,882 subjects counting repeats, 2,243 after correction. Power .80 needs N = 188 (semantic) vs 72 (associative) | Lucas 2000 (a11, b01) | E for the effect; C for "pure" meaning (Hutchison 2003) |
| Priming by task (corrected) | Paired lexical decision d = .33 (45 obs); continuous LD .27 (16 obs); mixed-list LD .26 (23 obs); naming .16 (29 obs). By study: paired LD .39 (16), mixed LD .28 (5), continuous .18 (6) | Lucas 2000 (b02; a12 is mislabelled) | E |
| Meaning-only priming is not just strategy | It did not shrink in tasks that limit strategy | Lucas 2000 (b02) | C |
| Mediated (two-link) priming is weak or absent in standard lexical decision | De Groot Exp 1, unrelated baseline: direct 43 ms, mediated 19 ms. Neutral baseline: direct 26 ms, mediated 2 ms (n.s.). Seven experiments | De Groot 1983 via Hutchison 2003 (a09, b04) | C |
| Mediated priming appears when strategy is blocked | Chwilla and Kolk 2002: 25 ms (n.s.) Exp 1, 32 ms (sig.) Exp 2 after an all-unrelated list. Plausible shared meaning 8 ms; none 10 ms; r = -.017 | Hutchison 2003 (b05, b06) | C |
| Priming shrinks in large varied samples | First-associate LDT priming 26 ms (200 SOA), 20 ms (1,200 SOA) in SPP vs 42 and 60 ms in Hutchison 2008 (300 first associates). On 283 shared pairs: 43 and 61 ms before vs 25 and 23 ms in SPP. z-score priming .37 and .44 vs .18 and .16. Largest item effect 262 ms | Hutchison et al. 2013 (a14, b07) | S |
| Rank matters more than strength | Anaki and Henik 2003: no difference between forward strength .10 and .42 if the item is the primary associate. Item "abandon" at 200 ms: first-associate 46.25 ms, other-associate -60.78 ms | SPP (a15) | S |
| Item-level priming is shared across tasks only at the short SOA | Cross-task r at 200 ms: .09 raw, .21 zRT, .17 residuals (1,661 items). At 1,200 ms: -.03, .10, .06 | Heyman et al. 2016 (b08) | S |
| No universal SOA splits automatic from strategic | Review-level | Hutchison 2003 (a08) | E |
| Spread model of aphasia naming errors | Multiplex of 4,118 words; about 1,200 trials; timing effect between error types up to d = 1.47 (some contrasts about 1.94) at retention R = 0.8 | SpreadPy 2025 (a18) | S (simulation) |
| Retention changes timing, not height | R 0.2 to 0.8 raised the easy-vs-hard timing effect d = 0.37 to 0.61; magnitude difference stayed about d = 0.78 | SpreadPy (a16) | S |
| Embedding-driven ACT-R spreading is only slightly better than frequency plus length | Spearman rho with SPP RT: EMMA-only .30; frequency-only .42; ACT-R plus word length .48; Word2Vec spread .50; BERT spread .49; with approximate fan effect .51/.50; plain linear regression .51 | Meghdadi et al. 2026 (c17) | S |
| Graph spread beats dense on entity-heavy multi-hop (author runs) | HippoRAG avg R@2/R@5 57.4/72.9 vs ColBERTv2 53.9/65.6. 2Wiki R@5 89.1 vs 68.2. MuSiQue 51.9 vs 49.2. HotpotQA 77.7 vs 79.3 (lower). 1,000 questions per set | HippoRAG 2024 (a20, c01) | S for size; E for direction |
| The margin is smaller in an independent test | HotpotQA F1 63.01 vs 60.04; MultiHop-RAG 70.27 vs 67.02 (about 3 points); temporal queries 49.91 vs 30.70. Reader Llama-3.1-8B | Han et al. 2026 (d05) | S |
| Dense wins single-hop lookup | NQ F1 RAG 64.78 vs HippoRAG 2 61.03 vs Community-local 63.01. LongMemEval single-session type: NaiveRAG 85.90 vs HeLa-Mem 78.85 | Han (d05); HeLa-Mem (d13); GraphRAG-Bench (d08) | E (4 sources) |
| Graph spread finds complete evidence sets | All-recall AR@5: 2Wiki 75.7 vs 37.1; average 52.0 vs 37.4; MuSiQue 22.4 vs 16.1; HotpotQA 57.9 vs 59.0 | HippoRAG (b17, c03) | S |
| The spreading step carries the gain (corrected) | Avg R@2/R@5: full 57.4/72.9; seeds only 50.7/56.2; seeds plus neighbours, no PPR 46.2/58.4; no node specificity 54.4/67.8; no synonymy edges 57.1/72.5 (2Wiki R@5 89.1 to 85.3). Neighbour stuffing is worse than seeds alone on R@2 only | HippoRAG ablation (b16, c02; critique correction 2) | S |
| Seeding method matters most | HippoRAG 2 passage recall@5 avg: query-to-triple (full) 87.1; NER-to-node 74.6; query-to-node 59.6; no passage nodes 81.0; no triple filter 86.4. Full per set: MuSiQue 74.7, 2Wiki 90.4, HotpotQA 96.3. Query-to-triple gains 12.5 points over NER-to-node | HippoRAG 2 (d01; c06 is mislabelled) | S |
| HippoRAG 2 fixes the simple-QA loss | QA F1 avg (Llama-3.3-70B): NV-Embed-v2 57.0; HippoRAG v1 53.1; HippoRAG 2 59.8; GraphRAG 49.6; RAPTOR 48.8; LightRAG 6.6. +9.5 on 2Wiki and +3.1 on LV-Eval over NV-Embed-v2 | HippoRAG 2 (c05, d02) | S |
| Query-aware gate on each hop | MuSiQue F1 41.68 vs 34.27 without gate (+7.4), EM 32.8 vs 26.1. 2Wiki 55.00 vs 51.44 (+3.6). Latency 4.9x faster on 2Wiki (0.09 s vs 0.44 s), 1.5x on MuSiQue. n = 1,000 | Query-aware SA 2026 (b18) | E for gating (with c08) |
| The gated method still loses to rivals | MuSiQue F1: QAFD-RAG 47.99, this method 41.68, GraphRAG 39.40, HippoRAG 38.33. 2Wiki F1: HippoRAG 70.33, QAFD-RAG 69.41, this method 55.00 | (b19; critique correction 5) | S |
| Depth matters more than decay | 1 to 2 hops: +18.8 F1 (2Wiki), +12.7 (MuSiQue). 2Wiki T = 2, 3, 4 indistinguishable; MuSiQue T = 3 best. Decay 0.3 to 1.0 moves F1 by 2.8 and 4.0, inside the CI. Four steps doubles latency | (b20); matches b14, b23 | E |
| Spread plus iterative retrieval is complementary | phi4, 100 questions per set. MuSiQue correctness: naive 46, CoT-RAG 56, HippoRAG 2 70, SA-RAG 67, SA-RAG+CoT 75. 2Wiki: 48, 68, 76, 76, 87 (+39 points absolute, best case). Decay chosen on about 10 questions | SA-RAG (b13, b14, c07; correction 4) | E for direction; sizes small-sample |
| Agent memory with spreading beats other memory systems on LoCoMo | Weighted F1 (GPT-4o-mini, adversarial excluded): SYNAPSE 40.5; Zep 39.7; MemoryOS 38.0; AriGraph 33.7; A-Mem 33.3; MemGPT 28.0; full-context 25.6. Multi-hop 35.7 (A-Mem 27.0); temporal 50.1 vs 45.9. Tokens 814 vs 16,910; $0.24 vs $2.67 per 1k queries; 1.9 s | SYNAPSE (a23, b21, c09, c25; correction 6) | C |
| SYNAPSE ablation | No fan effect 36.1 (open-domain 25.9 to 16.8). No node decay 30.7 (temporal 50.1 to 14.2). No activation dynamics 30.5. Graph removed 32.9. Vectors only 25.2. No lateral inhibition 39.4. Gate off: 40.3 avg but adversarial 96.6 to 67.2 | SYNAPSE (b22, c10) | S |
| Graph memory holds up with low query-evidence overlap | Relative F1 drop on low-similarity subsets: SYNAPSE 5.3% / 7.4%; A-Mem 43.1% / 56.3% | SYNAPSE (b23, c24) | S |
| Learned co-activation edges help modestly | HeLa-Mem avg F1 34.74 vs 32.19 without spreading (-2.6); multi-hop 36.04 to 33.88. Table multi-hop 36.04 vs text 40.14 disagree. LongMemEval-S overall 65.40 vs A-MEM 62.60 vs NaiveRAG 61.00 | HeLa-Mem (c11, d12, d13) | S |
| An independent SYNAPSE-style re-implementation is mixed | 304 questions: multi-hop 25.4 to 49.2 (+23.8) vs its own baseline; single-hop 60.5 to 65.1 but 14.9 below its previous version; total 70.4% vs 74.8% before. Spread channel not isolated | SuperLocalMemory V3.3 (d14) | C |
| Triples-only graph is a poor memory | NQ F1 34.28 (triples only) vs 50.27 (plus text) vs 64.78 dense. HotpotQA 25.02 / 42.60 / 60.04. MultiHop-RAG 41.24 / 48.51 / 67.02. Only about 65.8% (HotpotQA) and 65.5% (NQ) of answer entities appear in the graph | Han et al. (d06, d07) | S |
| Token cost differs by 3 orders of magnitude | Prompt tokens (novel corpus): dense 879; HippoRAG 2 1,008; RAPTOR 3,441; HippoRAG v1 7,208; MS-GraphRAG local 38,707; global 331,375; LightRAG about 100,832 | GraphRAG-Bench (d09) | S |
| Memory growth | HippoRAG 2 stayed ahead of NV-Embed-v2 through 4x corpus growth, but associative F1 fell at a similar rate for both. Largest graphs about 314k nodes and 2.67M edges | HippoRAG 2 (d03) | S |
| HippoRAG failure modes | Of 100 failures: 26% 2-hop, 41% 3-hop, 33% 4-hop. 7% no gold phrase matched before filtering; 26% none after filtering; 8% filtering lowered the share | HippoRAG 2 (d04) | S |
| Cost vs iterative LLM retrieval | 10-30x cheaper and 6-13x faster than IRCoT online (abstract says 10-20x). Indexing about 10x more expensive. HippoRAG + IRCoT avg R@5 78.2 | HippoRAG (c04; correction 3) | S |
| A cheap router works | Mixed benchmark accuracy: no retrieval 39.5; dense 65.1; EA-GraphRAG router 71.6. Latency: dense 0.08 s; graph 3.23 s; router with fusion 2.19 s. MultiHop-RAG: both right 55.4%, RAG-only 11.6%, GraphRAG-only 13.6%, both wrong 19.4% | Dong 2026 (d10); Han (d06) | E, but routers were trained on benchmark questions |
| LLM association networks reproduce spread priming | Wilcoxon effect size related vs unrelated, 50 SPP pairs: humans 0.870; Mistral 0.859; Llama3 0.869; Haiku 0.866. Spearman activation vs RT: -0.626 / -0.615 / -0.614 / -0.662 | Abramski 2024 (c14) | E |
| LLM shortest paths predict human RT | 4,988 Gemini triple lists, 32 mixed-effects models; best path-length beta = .044; worst .031 (all p < .001) | Kinney 2025 (c16) | S |
| LLM association networks are narrower | Unique responses: humans 116,640; Llama3 105,367; Mistral 41,369; Haiku 15,275 | Abramski 2024 (d19) | S |
| Stereotypes show up in spread audits | Significant stereotype effects in all four networks (paired Wilcoxon); humans strongest, Mistral weakest; Llama3 flips female/male direction | Abramski 2025 (d18) | S |

## 4. Mechanisms and models

Each model is written so it can be coded.

### 4.1 Basic spreading activation (Collins and Loftus style)

State: a weight per node, `a[i]`. Edges `w[i][j]` in [0,1] (link strength; a short link means high w).

1. Seed. `a[s] = 1` for each source node (or the query score).
2. Repeat for T steps (T = 2 to 3): `a_new[j] = decay * sum_i( a[i] * w[i][j] / fan(i) )`, where `fan(i)` is the number of out-links of i (Anderson's fan effect).
3. Apply the threshold: set `a[j] = 0` if `a[j] < theta`.
4. Optionally keep seeds at their start value (restart).
5. Read out the top-k nodes by activation.

Required constraints (c08, K11 [E]): hop limit, fan-out cap, decay below 1, threshold. Without them the state converges to a query-independent pattern.

Settings reported (c22): SYNAPSE T = 3, retention 0.5, temporal decay 0.01, top-k about 30 (range 20-40). SA-RAG decay 0.45, threshold 0.5, c = 0.4. HippoRAG PPR damping 0.5, synonymy threshold 0.8. HeLa-Mem spreading strength 0.1, threshold 0.4 or 0.6, edge decay 0.995, learning rate 0.02. SpreadPy retention R in {0.2, 0.5, 0.8}.

### 4.2 Two dials, not one

Retention (decay) sets timing: when activation peaks. Diffusion strength and threshold set reach (a16). Tune them apart. In retrieval, depth matters more than decay (b20, K12).

### 4.3 Fan effect (hub damping)

Divide outgoing weight by node degree. Removing it dropped SYNAPSE avg F1 40.5 to 36.1 and open-domain 25.9 to 16.8 (b22). In embedding ACT-R an approximate fan effect added about +0.01 rho (c17). In HippoRAG, "node specificity" (an inverse-frequency weight on seeds) is the same idea. Removing it cost 3.0 R@2 and 5.1 R@5 (b16).

### 4.4 Query gate per hop

At each hop pass activation to a candidate only if `cos(query_emb, candidate_emb) > g`, or multiply by that cosine. This keeps spread on topic. +3.6 to +7.4 F1 and 1.5 to 4.9x lower latency (b18). SYNAPSE has a separate "uncertainty gate" that refuses when top activation is low. It moves adversarial F1 96.6 vs 67.2 but average only 40.5 vs 40.3 (b22). That is a design effect, not a retrieval gain.

### 4.5 Personalized PageRank (HippoRAG)

Build a graph offline. An LLM extracts triples (OpenIE) from each passage. Nodes are phrases (and, in v2, passages). Edges are relations, synonym links (embedding similarity over 0.8) and passage-contains-phrase links. Online: link the query to the graph, set reset probabilities on seeds, run PPR with damping 0.5, read passage scores. One step, no LLM walk (a20).

HippoRAG 2 changes (c05, d01): add passage nodes. Seed by matching the whole query to triples, then filter triples with an LLM. Seed passage nodes by dense score. Recall@5 is 87.1 against 74.6 for NER-to-node seeds.

### 4.6 SYNAPSE-style agent memory

A unified graph of episodic and semantic nodes. Parts: spreading activation (T = 3, retention 0.5), lateral inhibition (top-M nodes suppress rivals), temporal decay on edges (0.01), fan-effect dilution, and an uncertainty gate. Fuse with a vector score. About 814 tokens per query (c09, c25).

### 4.7 HeLa-Mem Hebbian edges

Edges between memories retrieved together get stronger (learning rate 0.02) and decay (0.995). Retrieval has two paths: semantic search, plus spread along learned edges (strength 0.1, threshold 0.6). About 1,010 tokens per query (d12).

### 4.8 Embedding-driven spreading in ACT-R

Replace hand-coded association strengths with cosine similarity from Word2Vec or BERT. Activation is base level plus the sum of source weight times association strength. It predicts item-level SPP RT at rho about .50, versus .48 for frequency plus length (c17). Embedding similarity is almost as good as hand links for this purpose.

### 4.9 Multiplex layers (SpreadPy)

Separate layers (meaning links, sound links) with spread across them (a18). Layers can be audited separately (c15).

### 4.10 Spread audit for bias

Prime demographic words, spread, compare final activation of stereotype-consistent against inconsistent targets with a paired Wilcoxon test (d18).

### 4.11 Stop rules for depth

Fixed T = 3 is the default. The alternatives were tested on iterative retrieval loops, not on spread depth. A learned Q-network stop gave +1 to 3 F1 on two of three sets (d15). A training-free evidence-coverage stop avoided searching on 17-45% of loops without losing EM (d17). An embedding-level rewriter (TreeHop) runs at 0.1-0.2 s per query (d16).

### 4.12 Router

A small MLP over query syntax features predicts whether graph beats dense (d10). A prompted fact-vs-reasoning classifier also works (d06). Concatenating both contexts works too.

## 5. What holds up

**Holds up well.**
- Word-level semantic priming exists. Large datasets (SPP: 1,661 targets, 768 subjects) back it (K22 [E]).
- Associated pairs prime about twice as much as meaning-only pairs (d = .51 vs .26) (K01 [E]; "pure" meaning is contested).
- Automatic and strategic parts both exist, with no universal SOA split (K04 [E]).
- Spread needs constraints: hop limit, decay, threshold, fan (K11 [E]).
- Gating by query similarity helps (K11).
- Depth 2 to 3 matters. The decay value hardly does (K12 [E]).
- Dense retrieval wins single-hop lookup. Graph spread wins multi-hop by a few points in independent tests (K08, K24 [E]).
- Spread plus iterative retrieval is complementary (K16 [E], small samples).
- LLM-built association networks reproduce human priming predictions (K19 [E]).

**Replication problems and shrinkage.**
- SPP shows priming about half the size of earlier studies (26/20 ms vs 42/60 ms) (a14). Expect gains from demos to shrink.
- Mediated priming: de Groot found none in 7 experiments. Strategy-blocked studies find 8-32 ms. Chwilla and Kolk had 25 ms n.s. and 32 ms sig. (K03 [C]).
- The independent test (Han et al.) shows a multi-hop margin over dense of about 3 points. HippoRAG's own report was +20.9 R@5 on 2Wiki (d05).
- On HotpotQA graph spread is not better than dense on recall (77.7 vs 79.3).
- SYNAPSE has no isolated independent re-test. SuperLocalMemory V3.3 re-implemented the formula only inside a 7-channel system, credited its gains to other parts, and was 14.9 points lower on single-hop than its earlier version (d14). K17 is [C].
- HeLa-Mem: the spread ablation is only -2.6 F1, and its table and text disagree on multi-hop F1 (36.04 vs 40.14).
- Decay: the query-aware paper finds it hardly matters. SYNAPSE finds node decay critical for temporal questions (50.1 to 14.2). Both can hold because the tasks differ.

**Moderators.**
- Task: lexical decision d = .27-.33, naming .16 (b02).
- SOA and list design: a long SOA and a high nonword ratio inflate priming through strategy (a08).
- Relation type: synonyms, antonyms and functional associates support feature overlap. Category coordinates do not prime automatically (a10).
- Rank over strength (a15).
- Question type: single-hop vs multi-hop. Entity-heavy (2Wiki) vs not (HotpotQA). Temporal questions favour graph memory (49.91 vs 30.70, d05).
- Graph design: triples-only is weak (NQ 34.28). Edges must lead back to text (d07).
- Seeding: query-to-triple plus passages beats entity or bare-node seeds (d01).
- Memory size: gains held through 4x growth up to about 314k nodes, but accuracy still fell (d03).
- Extraction noise: about 34% of answer entities are missing from extracted graphs (d06).

**Interventions that worked.** Hub damping (b22). Query gate (b18). PPR instead of neighbour stuffing (b16, R@2 only). Passage-linked graph (c05). Chain-of-thought plus spread (b13). Router between dense and graph (d10). Coverage-based stop (d17, on iterative loops). Temporal decay on edges for time questions (b22).

**Interventions that did not work, or did not isolate.** Adding direct neighbours without PPR: worse on R@2 (46.2 vs 50.7), better on R@5 (58.4 vs 56.2) (b16, corrected). Lateral inhibition: only -1.1 avg F1 when removed (39.4 vs 40.5) (b22). A prompted stop check gave no gain over no stopping (d15). Forgetting in HeLa-Mem: no loss, on 300-turn conversations only (d12). Raising the SYNAPSE gate to 0.15 raised adversarial F1 but doubled false refusals, 2.1% to 4.2% (b23).

**Overall caution.** Almost all 2024-2026 LLM results are single-lab preprints on the authors' own baselines. SA-RAG uses 100 questions per set. HippoRAG's PPR is not decaying spread with a threshold, so the match to Collins and Loftus is by analogy.

## 6. Language models

**Do LLMs show priming themselves?** Only weakly or conditionally (K18 [E]).
- GPT-4o mini on SPP pairs inside masked sentences: 500 trials, 127 usable contrast pairs. Complete-case Wilcoxon W = 1793.0, p < .05. With multiple imputation (201 of 500 missing, 40%) W = 441.0, p = .088, not significant (b11).
- GPT-3 in a text lexical decision, 300 targets: sentence format confidence .56 unrelated vs .76 related (4-letter), .62 vs .81 (5), .66 vs .81 (6), p < .001. Question format .78 vs .85, .81 vs .85 (p = .004-.0044). Simple format .79 vs .74 (b12). Priming depends on prompt format.
- BERT (Misra et al. 2020): 3,058 target-related-unrelated triples, 2,112 after filtering. Facilitation falls as context constraint rises (p < .001). In strict mode, from the 8th constraint bin BERT-base is primed in 49% or fewer cases. A related word can mislead in constrained contexts ("mispriming"). Facilitation is larger for synonym (418 pairs), category (164) and antonym (153) than for phrasal associate (263) (c12, c13). This is a loose analogue of human context effects.
- Structural priming (Jumelet 2024) is a different effect and was not opened (b25).

**Can LLM-built networks stand in for human ones?** Yes, for priming predictions. LLM World of Words (12,282 cues, over 3 million responses per model): spread effect size 0.859-0.869 vs 0.870 human. Spearman with RT -0.614 to -0.662 vs -0.626 (c14). Gemini triple graphs: path length predicts RT, beta .031-.044, all p < .001 (c16). But LLM networks are narrower (Haiku 15,275 unique responses vs humans 116,640; d19) and carry stereotypes in different directions (d18). The human layer pattern (bias falls from associative to categorical layers) was not reproduced by Mistral or Llama3 (c15, c23; K21 [S]).

**Do embedding models act like association links?** Embedding ACT-R spreading reaches rho .49-.50 vs .48 for frequency plus length and .51 for plain linear regression (c17). Embeddings are about as good as hand links, but not much better than simple baselines (K20 [S]).

**Retrieval and memory systems.**
- HippoRAG family (a20, c01-c06, d01-d04): a large gain in author runs on 2Wiki, smaller in independent runs (d05). HippoRAG 2 fixed the single-hop loss of v1 (c05).
- SA-RAG: training-free classical spread. With CoT retrieval it is best in all four setups. Up to +39 points absolute over naive RAG (best case, 100 questions, phi4) (b13, c07).
- Query-aware spread: gate +3.6 to +7.4 F1 (b18).
- SYNAPSE: LoCoMo F1 40.5 with 95% fewer tokens (c25).
- HeLa-Mem: LoCoMo ablation -2.6 F1. LongMemEval-S overall 65.40 vs 61.00 NaiveRAG, but it loses single-session (78.85 vs 85.90) (d12, d13).
- Independent evaluations: Han et al. (d05-d07), GraphRAG-Bench (d08, d09), router papers (d10, d11).
- Stop and iteration controls (d15-d17) were tested on iterative RAG, not on spread.

**What changed results, by how much.**
- Gate on each hop: +3.6 to +7.4 F1.
- Fan effect: +4.4 avg F1 (+9.1 open-domain).
- Decay: +35.9 temporal F1 in SYNAPSE (50.1 vs 14.2). Not important in the query-aware paper.
- Seeds by query-to-triple: +12.5 recall points vs NER-to-node, +27.5 vs bare-node.
- Iterative CoT on top of spread: MuSiQue correctness 67 to 75, 2Wiki 76 to 87 (b13).
- Router between dense and graph: 65.1 to 71.6 accuracy (d10).
- Graph on single-hop: negative (NQ -3.75 F1; LongMemEval single type -7.05).

**Equal-token status.** HippoRAG 2 keeps prompts near dense size (1,008 vs 879 tokens, d09). Other graph methods use 4x to 377x more. No source compares spread against dense plus an LLM query rewrite at equal tokens (K31, open).

## 7. What our agent should take

Each item: schema part, status, evidence ids.

### Add now (established)

1. **Spread is always constrained.** Hop limit 2 to 3, decay below 1, threshold, fan-out cap. Part: S3, memory. [E] K11. Evidence: c08, b18, a25, b20. Code runs it (G5). The model never walks the graph.
2. **Gate each hop by similarity to the query.** Part: S3. [E] K11. Evidence: b18 (+3.6 to +7.4 F1, 1.5-4.9x faster), a25.
3. **Fix depth at 2 to 3. Do not tune decay.** Part: S3. [E] K12. Evidence: b20, b14, b23. Gains vanish past 3 hops. Four steps doubles latency.
4. **Do not spread on single-hop lookups. Route.** Spread only when the thought names 2 or more entities, asks a relation, or is temporal. Part: S3 router, G12 (spend by difficulty). [E] K08, K24. Evidence: d05, d06, d08, d10, d13. Dense wins single-hop (NQ 64.78 vs 61.03).
5. **Keep a cheap automatic pass before any deliberate search.** Part: G1, S3. [E] K04. Evidence: a07, a08, b08.
6. **Pair spread with iterative retrieval, not instead of it.** Part: S3, S6. [E] K16. Evidence: b13, c07, a22, c19. Treat sizes as best case.
7. **Edges lead back to raw text.** No triples-only memory. Part: memory. Evidence: d07, d06, c05. K25 itself is [S], but the direction agrees across sources.
8. **Report held-out gains on a fresh item set and plan for shrinkage.** Part: G3, G7. Evidence: a14 (priming halved in the large sample), d05 (independent margin about 3 points vs 20.9 in author runs).
9. **Tag evidence by priming type.** Social priming failures do not apply to lexical priming. K22 [E]. Evidence: a03, a13.
10. **Log the share of gold entities present in the memory graph.** Part: memory. Evidence: d04, d06 (about 34% missing in LLM-extracted graphs).

### Test first

| # | Candidate | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Spread vs dense vs dense plus rewrite vs spread plus rewrite, equal tokens | S3 | open | K31, d16, d05 |
| T2 | Seed by whole-query-to-triple/passage vs entity vs node | S3 seeding | [S] | K23, d01, d04 |
| T3 | Hub damping (fan effect) with a query gate present | S3, memory | [S] | K13, a24, b22 |
| T4 | Recency decay on edges for time questions | memory | [S] | K14, b22, d05 |
| T5 | Rank-based (top-k per node) vs weight-based thresholding | S3 | [S] | K06, a15 |
| T6 | Edge types: co-occurrence vs embedding similarity vs LLM relation | memory | [S] | K05, K26, d01, d12 |
| T7 | Co-activation (Hebbian) edges learned from use | memory | [C] | K17, d12 |
| T8 | Coverage-based stop vs fixed T = 3 | S3, S6 | [S] | K29, d17 |
| T9 | Prime-and-spread bias audit on memory graph | G, memory | [S] | K30, d18 |
| T10 | Low-overlap slice: graph vs dense | S3 | [S] | K15, c24 |
| T11 | LLM-seeded association edges when no corpus graph exists | memory | [E] for priming prediction, untested for retrieval | K19, c14, c16 |
| T12 | Router trained on our own free-form thoughts | S3 router | [E] direction | K24, d10 |

All of these are repeated, with thresholds, in UNKNOWNS.md. Nothing in "Test first" goes into SCHEMA.md until its test passes.

## 8. Concrete tests on our bench

All arms get the same total tokens (prompt plus output, setup cost counted, G7). Use a held-out half of items for the final number (G3). Report accuracy per token and the single-hop / multi-hop split.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 (K31, T1) | Multi-hop and single-hop questions over an agent memory of past attempts and notes | (a) dense top-k; (b) dense plus one model query rewrite; (c) gated spread, T = 3, code-run; (d) spread plus rewrite | Answer accuracy; all-evidence-found rate (AR@k); tokens | Spread beats dense by about 3 points on multi-hop (independent figure) and loses by about 3-7 on single-hop. Unknown against (b) |
| B2 (K23, T2) | Same, with free-form thoughts as queries | Seed by query-to-passage, by entity extraction, by bare node | Recall@5 and AR@5 | Query-to-passage seeds best (12.5 and 27.5 points in HippoRAG 2) |
| B3 (K11, K12) | Multi-hop slice | Uniform spread vs query-gated spread; T = 1, 2, 3, 4 | F1 and latency | Gate +3 to +7 F1. T 1 to 2 is the biggest jump. Flat after 3 |
| B4 (K13) | Memory with hub entities (frequent names, tools) | Spread with and without degree normalisation, gate on | Open-domain F1 | About -4 F1 without the fan term (SYNAPSE). Unknown with a gate |
| B5 (K14) | Time-dependent questions on a growing log | Recency decay on or off | Temporal accuracy | Large gain with decay in SYNAPSE (50.1 vs 14.2). Independent check needed |
| B6 (K24) | Mixed single- and multi-hop set | Always-dense, always-spread, rule router, concatenate both | Accuracy, latency | Router or concatenation above either alone (65.1 to 71.6 in Dong) |
| B7 (K06) | Neighbour selection | Weight threshold vs top-k by rank | Precision of kept neighbours | Rank at least as good. Human data only |
| B8 (K26) | Memory graph variants | Co-occurrence edges; embedding-similarity edges; LLM-relation edges | Recall@5, AR@5 | Unknown. Triples-only is weak |
| B9 (K15) | Slice with low word overlap between query and evidence | Dense vs spread | Relative F1 drop vs full set | Spread drops under 8% vs 43% for dense memory (single source) |
| B10 (K29) | Multi-hop iterative loop | Fixed T = 3 vs coverage stop | EM and loop count | 17-45% fewer loops, EM held |
| B11 (K30) | Memory graph audit | Prime-and-spread before and after a policy change | Activation gap, stereotype-consistent vs inconsistent | Detects bias. Link to output shift unproven |

## 9. What does not transfer, and why

- **Millisecond effects.** Priming speeds recognition by 20-60 ms. Our agent does not recognise words under time pressure. Only the structure (a cue lifts its neighbours) transfers.
- **The automatic/strategic split by SOA.** There is no SOA in an LLM loop. The functional split (cheap code pass vs costly model pass) transfers. The timing does not (a08).
- **Mediated priming across several hops.** Humans show weak effects past one link (a09). Retrieval systems do gain from 2 to 3 hops, but because of multi-hop questions, not because of the human effect. Do not cite human data as support for deep chains.
- **Pure semantic priming.** The human meaning-only effect is small (d = .26) and disputed. Most embedding memories have only similarity links. The human result suggests weighting association edges above similarity, which we cannot test with human data.
- **Layered System 1 / System 2 networks.** Human bias falls from associative to categorical layers. Mistral and Llama3 do not show this (c15). Do not assume LLM structure mirrors human structure.
- **LLM internal priming.** GPT-4o mini priming vanishes under multiple imputation (p = .088). BERT priming fades under strong context (b11, c12). Do not assume the model's own associations spread like human ones. Expand memory outside the model.
- **PageRank as the same mechanism.** HippoRAG's PPR is a kin, not Collins and Loftus. Do not borrow human parameters (decay, threshold) for PPR.
- **Social priming results.** Do not use them at all (a03).
- **ACT-R fit on RT.** Embedding spread fits item-level RT at rho .50 vs .51 for linear regression (c17). It is a model of human RT, not proof that spread retrieves better.
- **Author-run LLM gains.** Treat them as upper bounds. Independent runs show a much smaller margin (d05).
- **Scale.** Nothing was tested at millions of nodes (d03).

## 10. Open questions

1. Does gated spread beat dense plus one model rewrite at equal tokens? (K31; no source.)
2. When does spread lose, and can a cheap router predict it from free-form agent thoughts? The direction is closed. Free-form queries are untested (d10).
3. How much of SYNAPSE survives independent re-implementation with equal-length baselines? (d14 does not isolate the spread.)
4. Which edge types matter, compared on equal footing (K26)?
5. What fan normalisation and hub cap is best once a query gate is on (K13)? Only one ablation each way exists.
6. Scale to millions of nodes, and the cost of OpenIE noise (d03, d06).
7. Seeding from free-form thoughts rather than benchmark questions (d01).
8. Do human rank effects (primary associate over raw strength) carry to embedding neighbours? (a15; no LLM source.)
9. Do biased LLM association graphs shift retrieval outputs? The 2026 retrieval-bias paper named in the gap list was not found (d18, d19).
10. Can a learned or coverage stop replace fixed T = 3 for spread depth? Tested only in iterative RAG (d15, d17).
11. Does the mediated priming dispute (de Groot vs strategy-blocked studies) matter for hop depth in agents? Probably not, but it is unresolved (K03).
12. Does Hebbian learning from use beat a static graph over a long run (K17, d12)?

## 11. Sources

[V] = opened and read this session (full text or page). [M] = snippet, secondhand, or paywalled.

**Human work**
- [M] Collins and Quillian (1969) Retrieval time from semantic memory. https://doi.org/10.1016/S0022-5371(69)80069-1
- [M] Meyer and Schvaneveldt (1971) Facilitation in recognizing pairs of words. https://doi.org/10.1037/h0031564
- [M] Collins and Loftus (1975) A spreading-activation theory of semantic processing. https://doi.org/10.1037/0033-295X.82.6.407
- [M] Posner and Snyder (1975) Attention and cognitive control. (no URL)
- [M] Neely (1977) Semantic priming and retrieval from lexical memory. https://doi.org/10.1037/0096-3445.106.3.226
- [M] Anderson (1983) A spreading activation theory of memory. https://doi.org/10.1016/S0022-5371(83)90201-3
- [M] de Groot (1983) mediated priming, via Hutchison 2003. https://www.montana.edu/attmemlab/documents/HutchisonPBRreview2003.pdf
- [M] Crestani (1997) Application of spreading activation techniques in information retrieval. https://doi.org/10.1023/A:1006569829653
- [V] Lucas (2000) Semantic priming without association: a meta-analytic review. https://link.springer.com/content/pdf/10.3758/BF03212999.pdf
- [V] Hutchison (2003) Is semantic priming due to association strength or feature overlap? https://www.montana.edu/attmemlab/documents/HutchisonPBRreview2003.pdf
- [V] Hutchison and Balota (2005) Decoupling semantic and associative information in false memories. https://www.montana.edu/attmemlab/documents/Hutch_Balota_JML_2005.pdf
- [V] Hutchison et al. (2013) The Semantic Priming Project. https://www.montana.edu/attmemlab/documents/spp.pdf
- [V] Heyman, Hutchison, Storms (2016) Uncovering underlying processes of semantic priming by correlating item-level effects. https://link.springer.com/content/pdf/10.3758%2Fs13423-015-0932-2.pdf
- [V] Wikipedia: Spreading activation; Priming (psychology). https://en.wikipedia.org/wiki/Spreading_activation ; https://en.wikipedia.org/wiki/Priming_(psychology)
- [V] Citraro et al. (2025) SpreadPy. https://arxiv.org/abs/2507.09628
- [V] Citraro (2026) Early language learning via spreading activation and category exploration. https://arxiv.org/abs/2607.06258 (exact scores not extracted)

**Language models and AI**
- [V] Misra, Ettinger, Rayz (2020) Exploring BERT's sensitivity to lexical cues using tests from semantic priming. https://arxiv.org/pdf/2010.03010
- [M] Lam et al. (2023), search summary relaying Misra 2020. https://ar5iv.labs.arxiv.org/html/2305.16917
- [V] Shaki, Kraus, Wooldridge (2023) Cognitive effects in large language models. https://arxiv.org/pdf/2308.14337
- [M] Jumelet, Zuidema, Sinclair (2024) Do language models exhibit human-like structural priming effects? https://arxiv.org/html/2406.04847v2
- [V] Gutierrez et al. (2024) HippoRAG. https://arxiv.org/pdf/2405.14831
- [V] Gutierrez et al. (2025) From RAG to Memory (HippoRAG 2). https://arxiv.org/pdf/2502.14802
- [V] Han et al. (2025/2026) RAG vs. GraphRAG: a systematic evaluation. https://arxiv.org/pdf/2502.11371
- [V] Xiang et al. (2026) When to use graphs in RAG (GraphRAG-Bench). https://arxiv.org/pdf/2506.05690
- [V] Dong et al. (2026) Use graph when it needs. https://arxiv.org/pdf/2602.03578
- [V] Fu et al. (2026) GraphRAG-Router (abstract and intro only). https://arxiv.org/pdf/2604.16401
- [V] Pavlovic, Krasz, Hajdu (2025/2026) SA-RAG. https://arxiv.org/pdf/2512.15922
- [V] Glybovets and Makarov (2026) Query-aware spreading activation. https://arxiv.org/pdf/2606.30133
- [V] Jiang et al. (2026) SYNAPSE. https://arxiv.org/pdf/2601.02744
- [V] Zhu et al. (2026) HeLa-Mem. https://arxiv.org/pdf/2604.16839
- [V] SuperLocalMemory V3.3 authors (2026). https://arxiv.org/pdf/2604.04514
- [V] Park, Cho, Lee (2025) Stop-RAG. https://arxiv.org/pdf/2510.14337
- [V] Li et al. (2025/2026) TreeHop. https://arxiv.org/pdf/2504.20114
- [V] Roh and Han (2026) HALT. https://arxiv.org/pdf/2608.02009
- [V] Abramski et al. (2024) LLM World of Words. https://arxiv.org/pdf/2412.01330
- [V] Abramski, Rossetti, Stella (2025) Word association network methodology for implicit bias. https://arxiv.org/pdf/2510.24488
- [V] Abramski, Rossetti, Stella (2026) System 1 and System 2 semantic memory structures. https://arxiv.org/pdf/2604.12816
- [V] Kinney (2025) LLM-generated semantic networks predict semantic priming effects. https://journalpub.escholarship.org/cognitivesciencesociety/article/49
- [V] Meghdadi, Duff, Demberg (2026) Integrating language model embeddings into ACT-R. https://www.frontiersin.org/journals/language-sciences/
- [V] Colombi and Strapparava (2025) Semantic priming in GPT. https://ceur-ws.org/Vol-4112/28_main_long.pdf
