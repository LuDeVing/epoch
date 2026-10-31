# Critique and cross-check: C06.06 Premise selection

## Re-opened sources (this session, PDF text via pdftotext)
Confirmed against the paper text:
1. DeepMath (arXiv 1606.04442): 57,917 theorems, 32,524 (56.2%) ATP-provable; 40% earlier portfolio, 27.3% best single method; Table top-16: 674/687/709/734/835 (24.6/25.1/25.9/26.8/30.5%); largest cutoff 65.1/66.4/67.9%; 823 new Mizar proofs; 61.3% to 66.4% with mining. All match.
2. Magnushammer (arXiv 2303.04488): 59.5 vs 38.3 PISA; 34.0 vs 20.9 miniF2F; Thor 57.0 to 71.0; BM25 30.6, TF-IDF 31.8, OpenAI 36.1; MAPL 56.3 vs HPL 54.0; 920K model 40.7. All match.
3. LeanDojo (arXiv 2306.15626): 51.2 / 47.6 / 29.0 / 23.8; novel 26.3 / 23.2 / 7.4 / 5.3; BM25 6.7/17.2/0.15, ReProver 13.5/38.4/0.31; novel 9.1/27.6; 120 GPU hours. All match.
4. Thor (arXiv 2205.10893): 39.0 LM, 25.7 Sledgehammer, 48.8 union, 57.0 Thor, 8.2% only-by-combination, 1.9% vs 28.2%, miniF2F 29.6 to 29.9, LISA 33.2. All match.
5. Flyspeck (arXiv 1211.7012): 39% in 30 s; 50% with dependencies; Z3 12.4% (256) vs 6.2% (740); Vampire 18.1 vs 12.9; E parallel over 20% at 512, 15.6% at 2048. All match. Note: evidence a10 says "one prover" for Z3; fixed by b04 (it is Z3).

## Corrections and wording fixes
- b02 says "negative mining doubled theorems proved at top-16". The DeepMath text only says 61.3% to 66.4% (union over cutoffs). The "doubled" statement is NOT checked; do not use. Claim K10 uses only 61.3 to 66.4.
- b02/b11 label Magnushammer BM25..Magnushammer as "single-step"; the table text confirms single-step. a18 and c10 are consistent. Some pdf text had the label "Multi-step" next to BM25 in the extracted rows; this is a layout artifact.
- ReProver baseline recall differs across sources: LeanDojo own paper R@1 13.5, R@10 38.4, MRR 0.31; Petrovcic (c16) re-run 13.42/39.60/0.3283; Tao et al. (c17) 11.79/36.69; LeanPremise says definitions of upper bound differ (c26). Do not compare recall across papers.
- a25 reports GNN gains relative to 13.42/39.60 (Petrovcic's own baseline), not 13.5/38.4. Fine, but flagged.
- b09 says Cover 0.56 (RF) and a15/c14 say 0.57 (names+bigrams): both consistent (different feature sets).
- b18 vs a23/c15: accumulating across sizes is 34.5 (b18), 37.3 (a23, c15). Union with MePo is 35.9/37.6 (b17), 34.5 (c15). These conflict. Not re-opened (see below). Treat 33.3 (single 82M, cumulative) and 43.0 (oracle) as the safe numbers; b17 says ground truth 41.0 full / 43.0 cumul.
- a07/b05: SNoW run is +31.8% vs "+32%" (60 vs 70 variant naming differs); harmless.
- Mizar relative-gain stat: c06 states ATPboost 15.7% relative over k-NN and "deep learning gain over k-NN was 4.3%". Not matched with DeepMath: DeepMath k-NN 65.1 vs def+char 67.9 at largest cutoff is 4.3% relative: consistent.

## Not re-opened this pass
LeanPremise (2026), LeanSearch v2 (2026), Lean Finder, RocqStar, DRIFT, Tao et al., CSLibPremiseBench, Petrovcic. arXiv search returned nothing for the 2026 titles and Semantic Scholar rate-limited (429). Their numbers rest on the earlier agents' reading (opened:true) and are single-pass. The a-vs-b-vs-c agreement on LeanSearch v2 (20% vs 16% vs 4%, n=100) and LeanPremise 30.1/33.3/43.0 is at least consistent across three agents, which is weaker than independent checking. DRIFT, HybridProver (b25, b26) and Natural Language Premise Selection (c28) were seen only in snippets; no numbers.

## Contradictions
- Retrieval value: ReProver gains +3.6/+3.1 points over no retrieval, Lean Finder gains 0.4 to 2.2 points; versus Magnushammer/Thor +14 and LeanSearch v2 +16 (n=100). The gain depends on whether retrieval is paired with a hammer or a reasoning step. Small n in LeanSearch tests (100, 50): one problem = 1 point; the 16 vs 20 gap is 4 problems.
- Embedders: ada-002 is worse than trained on PISA, yet beats ReProver on novel premises (c17). So "general embedders are weak" is contested.
- Structure: HolStep paper says Siamese conditioned models do not beat unconditioned (a14, b07); graph model says conditional 90.3 vs unconditional 90.0. Small difference everywhere; premise-conditioned scoring adds little.
- ProverQA (b24): GPT-4o accuracy drops with distractors and shuffling (hard: 62.4 to 50.0), a natural-language logic setting, hinting that irrelevant facts hurt LLMs; this fits K02 but is a different task and only one model.

## Weak spots
- Almost all evidence is ATP-hammer or fine-tuned retriever on formal libraries. Hardly any test is of a frozen general LLM agent choosing from a subgoal library. The jump to our agent is by analogy.
- Benchmarks are small, label-noisy (CSLib 48.2% linked premises elaborated), and leak: Mathlib premises seen in pretraining.
- Few failed replications in the strict sense; the closest are CSLibPremiseBench (structure gain weak) and the Z3 premise-count collapse.
- Token cost of retrieval is almost never reported; equal-token comparisons are not available in any paper.

## GAPS
1. Does retrieving from a library help a frozen LLM agent (no fine-tuning) at equal total tokens, versus just putting the whole library in a long context? Is there a measured crossover library size?
2. What is the best number of retrieved items k for an LLM reader (not a first-order prover)? Z3/Vampire curves peak near 256 premises, but LLM distraction curves (ProverQA, FormalML M=10 vs 20) suggest a much smaller peak.
3. How much of the gain from reasoning retrievers (LeanSearch v2 reasoning mode, query rewriting) survives once the extra reasoning tokens are charged to the budget?
4. How do retrievers do on unseen or newly added library items (novel_premises) when the library grows during the run, as ours will? Which method degrades least?
5. Does retrieval by goal state (stepwise, ReProver, Magnushammer) beat retrieval by whole problem statement (LeanSearch, Lean Finder) for a planning agent that stores subgoals?
6. Can the LeanSearch v2, LeanPremise and Lean Finder headline numbers be reproduced independently? They are 2026 single-paper results with small n.
7. What is the oracle gap for LLM agents (ground-truth lemmas given) in non-formal settings, and how much of it can retrieval close?
8. Are there studies of distractor harm for LLMs specific to retrieved-but-irrelevant lemmas (not general RAG), with effect sizes?
9. Is symbol-overlap or BM25+symbol enough once library items are written in natural language? (CSLib suggests the structure-aware reranker adds little.)
10. How should negatives or near misses be chosen when calibrating a selector on our own subgoal library, and how many examples are needed (Magnushammer: ~4K gives a win over Sledgehammer)?

## Gap search results

Sources opened this pass (PDF text via pdftotext): Self-Route, OP-RAG, Long Context vs RAG revisits, Power of Noise, GSM-IC, Lost in the Middle, Long-Context LLMs Meet RAG, Yoran et al., BRIGHT, ReasonIR, Rank1, NV-Retriever, LEGO-Prover, Rango, Lean Finder, RAG-MCP, Voyager. Evidence is in evidence_d.jsonl (d01 to d17); new claims K20 to K27 and status changes are in claims.jsonl. Web search quota and arXiv/OpenAlex search were exhausted, so papers were opened by arXiv id only; no new 2026 papers could be discovered.

1. Gap 1 (retrieval vs whole library in context, frozen LLM): PARTLY CLOSED. Full context wins on accuracy when the facts sit together and fit (Self-Route: LC 49.70 vs RAG 37.33, Gemini); retrieval wins on tokens, and retrieve-then-fall-back keeps most accuracy at 38-61% of tokens. OP-RAG shows 16K retrieved tokens beating 117K full context (44.43 vs 34.26 F1). Only RAG-MCP gives a crossover in item count (about 30 to 100 tool descriptions), and it is a short preprint. No paper compares retrieval against a library of short subgoals at equal total tokens. Still open: the crossover size for our library.
2. Gap 2 (best k for LLM readers): PARTLY CLOSED. Inverted U confirmed: peak 16K tokens for Llama3.1-8B, 32-48K for 70B (OP-RAG); Lost in the Middle sees marginal gains past 20 documents; Jin et al. see rise then fall with a strong retriever. All are for text chunks of passages, not subgoals; exact optimal k in items is not given. Self-Route finds k=5 cheapest on average, k=1 on extractive sets. Our own sweep is still needed; start with 3 to 10 items.
3. Gap 3 (reasoning-retriever gain after charging tokens): STILL OPEN. BRIGHT, ReasonIR and Rank1 show the gain (BM25 14.5 to 27.0; ReasonIR 24.4 to 29.9; Rank1-7B 27.5 vs 17.5 without chains), and ReasonIR estimates rewriting plus bi-encoder at over 200x less compute than Rank1-32B. No paper holds total tokens fixed against a non-reasoning arm. Rank1 budget forcing did not help.
4. Gap 4 (unseen or newly added items, growing library): PARTLY CLOSED. LEGO-Prover (frozen LLM, library grows in run) 50.4 vs 47.1 without library and a gap that widens with library size; Voyager without library plateaus; Rango proof retrieval cuts the loss from not training on a project. Which retriever degrades least on novel items is not compared beyond the ReProver and LeanDojo numbers already in K08.
5. Gap 5 (goal-state vs problem-statement retrieval): PARTLY CLOSED. Rango: retrieving earlier proofs keyed by proof state +47%, lemmas +3%. Lean Finder: raw proof state R@1 8.3 vs natural-language statement 64.2; adding a description to the state raises R@1 to 24.6. So state-keyed text is hard unless a plain-language gloss is stored. No head-to-head on the same agent.
6. Gap 6 (independent reproduction of LeanSearch v2, LeanPremise, Lean Finder): STILL OPEN. Lean Finder (opened) is again self-reported on its own synthetic test sets, with user study of 5 people; it gives numbers for Lean Search and Qwen3-Embedding-8B that are consistent with a weak general embedder. No independent reproduction found, and LeanSearch v2 and LeanPremise were not found by id.
7. Gap 7 (oracle gap outside formal settings): PARTLY CLOSED. BRIGHT StackExchange with Claude-3.5-Sonnet: none 77.7, best retriever 79.6, oracle 81.8 (46% of gap closed). Lost in the Middle GPT-3.5: closed-book 56.1, oracle 88.3, and 20 retrieved documents can be below closed-book. These are open-domain QA, not subgoal libraries; our U4 test remains the way to measure it.
8. Gap 8 (distractor harm specific to retrieved items): CLOSED enough for design. Power of Noise: one hard distractor up to -25%, many up to -67% (Llama2), random documents far milder; Jin et al.: stronger retriever, harder negatives, bigger harm; GSM-IC: at most 18% of solved problems stay solved across distractor types. Models used are old or small; effect for current frontier models is likely smaller but present (Jin et al. used Gemini-1.5-Pro).
9. Gap 9 (symbol overlap or BM25 enough for natural language items): PARTLY CLOSED. Rango: BM25 beat dense embeddings by 46%; BRIGHT: BM25 with reasoning-step queries scores 27.0, above dense models on the raw query; but Lean Finder shows a trained dense model beating Lean Search clearly (64.2 vs 49.2 R@1). So BM25 is enough only when queries are rewritten or items carry a gloss.
10. Gap 10 (choosing negatives): PARTLY CLOSED. NV-Retriever: positive-aware mining (below 95% of positive score) 0.5856 vs naive top-k 0.5407; ReasonIR: easy synthetic queries added nothing, hard ones did. How many examples are needed for a small library remains unmeasured beyond the Magnushammer figure.

Corrections found while writing: author names in a first draft of the evidence were checked against the PDF title pages and fixed (OP-RAG is Yu, Xu, Akkiraju of NVIDIA; Long-Context LLMs Meet RAG is Jin, Yoon, Han, Arik; NV-Retriever is Moreira et al.). Some figure-only results (Jin et al. peak positions, RAG-MCP stress test method) were not read as numbers.
