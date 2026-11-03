# Critique: C10.04 Incremental mapping (cross-check)

## Corrections made (numbers re-opened in source text)
1. Laban et al. 2025 (arXiv 2505.06120): 39% average drop, aptitude -16% (not significant), unreliability +112%, CONCAT 95.1% of FULL. Confirmed. Evidence a21 omits that the 16% aptitude drop is non-significant; c10 has it.
2. Webb et al. (arXiv 2212.09196): letter strings OR=1.76 has two p-values in the paper. Overall GPT-3 vs human p = 6.3e-5 (a15, a24); zero-generalization subset p = 0.0007 (b10). Both right; b10 paired the overall OR with the subset p. Digit matrices OR 1.88 p=0.005 and MC OR 6.27 p=2.3e-8 confirmed. Story analogies OR 0.37 p=0.0003 confirmed.
3. Huang et al. (2310.01798): c17 "CommonSenseQA 75.8 to 41.8" is GPT-3.5 after 5 calls (round 2); it is 38.1 after 3 calls, so the fall is not monotone. GPT-4 CSQA barely moves (82.0 to 80.0). GSM8K GPT-3.5 75.9 to 74.7, GPT-4 95.5 to 89.0, oracle 84.3 / 97.5, HotpotQA GPT-4 49 to 43: confirmed.
4. Chen et al. premise order (2402.08939): confirmed.
5. Lovett and Forbus 2017: 56/60 (75th percentile), earlier model 50/60 (41st), 54/60 = 61st percentile. Confirmed.
6. Forbus et al. 1994: 178.0 s vs 363.1 s, remaps 1.5 vs 3.0, confirmed in text. Human times are quoted from Keane "in press"; original never opened.
7. Lewis and Mitchell: human 0.753, GPT-3 0.350, GPT-3.5 0.452 confirmed in table text (layout partly garbled; GPT-4 0.488 sits in a garbled row).
No number was found wrong; the real fixes are items 2 and 3.

## Contradictions between sources
- Counterfactual analogy: Lewis and Mitchell say LLMs fail to generalise; Webb et al. 2024 reply that 46% of GPT-4 errors follow a valid alternative rule and humans do too (39%). Unresolved; marked contested (K10).
- Self-correction: Huang says intrinsic revision hurts; Self-Refine and Reflexion report gains. Reconciled by grounding: gains come with external feedback or a verifier.
- Analogy ability: Webb says GPT-3 beats humans on digits; Stevenson and Lewis show collapse on unfamiliar symbols. Same models, different task familiarity.

## Weak spots
- The core of the subfield (I-SME) rests on one 1994 paper (a01-a08, b01-b04, c01-c05 are the same source), so independent_sources is 1. No replication of the order effect is in the evidence.
- Human order-effect data (Keane), Kotovsky and Gentner 1996, Goldstone and Medin 1994, and Sloutsky and Yarlas were second-hand.
- Zero LLM studies test incremental mapping itself. Multi-turn, premise-order and belief-revision papers are proxies.
- Several LLM tables were garbled (Hu 2023, Yasunaga 2024, Lewis and Mitchell Table 1); cell numbers are approximate.
- YARN (2026) and Bayesian teaching are recent preprints with no independent check.
- I-SME model fit rests on two example sets, no fit statistics.

## Seen only in snippets or not opened
a06, a12, a21, a23, b05, b06, b24, b25, c06-c09 (Keane et al. 1994, IAM, PHINEAS, Bridge, Hodel and West).

## GAPS
1. Does extending a stored mapping with new facts beat re-mapping from scratch in an LLM at equal tokens, and on which tasks does it lose accuracy?
2. When should the agent remap instead of extend? Does a coverage/score signal like I-SME's "fraction of possible structure" predict the need, and can an LLM estimate it?
3. Does fact order (easy-first vs hard-first) cause an order effect in LLM mapping like Keane's twofold human slowdown? Has anyone replicated Keane's original study (N, statistics)?
4. How should the agent revise a mapping on a conflicting new fact without sycophantic flipping (K20) or stubbornness? What is the update-vs-maintain trade-off with a structured belief store?
5. Does an explicit structured mapping table (slots, scores, rivals) in context beat free-text history in multi-round settings at equal tokens?
6. Do successors of I-SME (SME in large-scale models 2016, Companion systems, Bridge Incremental Analogizer) report accuracy or speed numbers on incremental sessions?
7. Is joint consistency checking of candidate inferences (Falkenhainer 1990) better than per-inference checking for LLM agents, and how many can be checked jointly before it fails?
8. Does a hybrid structure-mapper plus LLM abstraction (YARN-style) hold up on independent benchmarks and larger models?
9. Do progressive-alignment curricula (close-to-far case order) improve LLM relational mapping, as in children and Kandaswamy et al.?

## Gap search results
Tool limits: Semantic Scholar, OpenAlex and the arXiv API all returned HTTP 429 for the whole session and the WebSearch budget ran out after one query. Gaps that needed new searching could not be closed. Evidence is in evidence_d.jsonl (d01-d16).

- Gap 1 (extend vs re-map at equal tokens in an LLM): OPEN. No direct test found (d15). Proxy: sequential presentation costs accuracy in 14-16 of 17 models (d06, claim K28) and multi-turn challenges flip more than first-query claims (d03, K27).
- Gap 2 (remap trigger from coverage signal): OPEN. No source on LLMs estimating match coverage. Only I-SME's own fraction-of-structure signal (K02, single source).
- Gap 3 (order effect and Keane replication): OPEN. No replication found (d13); the original was not opened. Human order effect remains one result (K03).
- Gap 4 (revise without sycophancy or stubbornness): PARTLY CLOSED. Evidence now shows both failures: inertia and collateral damage (AGM-Bench d04), a drift versus update-tracking trade-off (BeliefShift d01), flip compounding (d05), 43.5% of flips went toward correct (d08), over-updating by larger models (BayesBench d02). K20 raised to established; K29 added. No tested recipe for a structured belief store beyond RAG, which helped update tracking only (+0.09 BRA, +0.02 DCS).
- Gap 5 (structured mapping table vs free-text history): OPEN. Only the earlier K24 proxies. BeliefShift RAG result (d01) is weak support for stored history.
- Gap 6 (I-SME successors with numbers): OPEN. Nothing found (d14).
- Gap 7 (joint vs per-inference checking): OPEN. Nothing found (d15).
- Gap 8 (hybrid on independent benchmarks): OPEN. YARN still single-source; FAME named as another hybrid (d11).
- Gap 9 (close-to-far curricula in LLMs): OPEN for LLMs. Computational precedent confirmed for the child result (Kandaswamy et al. d09, model only, qualitative). No LLM curriculum study found.

Corrections: BeliefShift and Kim and Khashabi tables are garbled in text extraction; per-cell values are approximate (flagged in limits).
