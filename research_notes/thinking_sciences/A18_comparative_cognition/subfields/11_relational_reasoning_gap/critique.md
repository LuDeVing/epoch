# Critique: A18.11 Relational reasoning gap (cross-check)

## Corrections and confirmations (sources re-opened this session)
Re-opened full text for: Fagot and Maugard 2013 (Springer PDF), Webb et al. 2023 (arXiv 2212.09196), Lewis and Mitchell 2024 (arXiv 2402.08955), Webb, Sinha, Cohen 2021 ESBN (arXiv 2012.14601), ConceptARC (arXiv 2305.07141), Musker et al. 2025 (arXiv 2406.13803).
1. Fagot and Maugard: 96.3 vs 62.2 (shape), 94.3 vs 55.4 (colour), 78.5 vs 76.9 (Phase 2), 76.6 vs 63.4 (Exp 2). CONFIRMED (a04, a05).
2. Webb 2023: generative OR 1.88 (p=0.005, CI 1.21-2.91), semantic distance OR 3.24 (p=0.0165), story analogy OR 0.37 (p=0.0003), 15/54 always analogous. CONFIRMED (b01, c01, c03, c04). The OR 6.27 was not re-seen in text search; trusted from two lines.
3. Lewis and Mitchell Table 2: the PDF text is garbled. The correct mapping is humans 0.753, GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (c07 right). CORRECTION: b03's "GPT-3.5 is worse" wording is right, but b03's range "0.35 to 0.49" should not be read as GPT-3 lowest. Error shares 5.81% vs 38.59% alternate-rule CONFIRMED (b04).
4. ESBN: Transformer 73.7 at m=95 and 56.1 at m=98; LSTM 61.8 and 56.5; RN 50.5 at m=95 and 52.3 at m=98. CONFIRMED (a17, c20). Note: a17 lists LSTM 61.8 at m=95 only; fine.
5. ConceptARC: over 90% on 11 of 16, over 80% on rest, GPT-4 under 30% on 15 of 16 (33% on one), 40-point gap. CONFIRMED (b08).
6. Musker: 194 participants, default no-gap p=0.097 (GPT-4 and Llama) and 0.194 (Claude 3); order permutation Claude 3 coef -1.78, z=-4.217. CONFIRMED (b07, c11). Small note: c11 gives z=-4.22 (rounding).
Not re-opened (carry over from first-pass): Webb 2024 counterfactual P values, Hodel and West, Cook and Wasserman, Smith 2019 numbers, Stevenson, KiVA, Gendron, Yasunaga.

## Contradictions between sources
- Webb 2023 says GPT-3 matches or beats humans; Lewis and Mitchell, Hodel and West show collapse on counterfactual alphabets. Webb 2024 reply says code execution closes the gap (P=0.496) and that errors are valid alternative rules. Both are partly right: the result depends on whether the item is familiar and on tool use.
- Fagot and Maugard say their design rules out the Penn et al. variability explanation; Penn et al. camp disputes this (a25). Unresolved.
- Musker: no significant human-LLM gap in the default condition, but a significant gap when pair order is permuted. Same models, opposite conclusion by condition.
- Different human baselines: 0.753 (Lewis and Mitchell, Prolific) versus Hodel and West's undergraduates; human sample type shifts the gap.

## Weak spots
- Penn, Holyoak, Povinelli 2008 itself (a01, a02) was read only as an abstract. The whole animal-gap argument therefore rests on later papers.
- Several animal papers (Premack 1983, Thompson-Oden 1997, Fagot 2001, Thompson-Oden 2000) are second-hand (opened:false). Crow (b14) and Monk et al. 2024 (c22, HTTP 403) are not verified.
- a01 and a02 duplicate; a15, a25, a26, b16, b19, b25 are repeats of other lines, so evidence count overstates independent sources.
- Claim independence is often generous: Webb papers share authors and data.
- Most LLM studies are on GPT-3 to GPT-4 and Claude 3 era; no 2025-2026 frontier reasoning-model result on counterfactual alphabets or ConceptARC was found.
- No study tests a scaffold (not just prompting) on relational tasks at equal token budgets.
- Only snippets: Smith/Church secondary figures (6 of 29 baboons) come from reviews.

## GAPS (most decision-relevant first)
1. Do 2025-2026 reasoning models (long chain-of-thought) close the counterfactual-alphabet and ConceptARC gaps, and at what token cost versus a scaffold?
2. Does a scaffold step that re-encodes a problem into explicit roles and fillers (a relational bottleneck in text) improve accuracy at equal tokens versus plain chain-of-thought?
3. How much of the LLM counterfactual drop is misreading (comprehension) versus failing to abstract, measured with matched comprehension checks on current models?
4. Is the order-permutation sensitivity (Musker) fixed by averaging over shuffled example orders, and is the cost worth it?
5. Does self-generated analogical exemplar prompting (Yasunaga) still help on strong 2025+ models, or only on weak ones?
6. What does Penn et al. 2008 argue in full (its seven claims about relational vs perceptual similarity), and which have survived 2013-2025 animal replications?
7. Do the monkey and ape negative results (rhesus none over 260,000 trials) hold up with the newer training methods, and how large is the species gap in effect size?
8. Monk, Meyer, Ngo 2024 (LLMs and relational match-to-sample): what accuracy do LLMs get on the exact RMTS task used with animals?
9. Does human stalling at high similarity under load (Smith 2019) have an LLM analogue, such as accuracy falling with distractor similarity or context length?
10. Are there failed replications of the Cook and Wasserman pigeon relational-matching transfer and of the crow result?

## Gap search results (evidence_d.jsonl, d01-d17)
Closed or mostly closed:
- Gap 1 (partly closed). ConceptARC text: o3 77.1 vs humans 73.0, so accuracy gap is closed, but ~27% of o3's correct answers use unintended rules (humans ~7%) (d01). I-RAVEN-X shows o3-mini 86.6 to 17.0 with 3.4x tokens (d06). No counterfactual-alphabet test on reasoning models found. Token cost versus a scaffold: not found.
- Gap 3 (partly closed). Letter-string transfer fails on ordering rules, not repeat rules, so failure is not only misreading (d07). Relation is encoded but applying it is a bottleneck (d08). No matched comprehension check on 2025 reasoning models.
- Gap 6 closed. Penn et al. 2008 full text read; it is organised by domain, not seven claims (d12).
- Gap 8 (partly). Monk et al. 2024 abstract only, no numbers (403). Superseded by the 2026 RMTS VLM study showing frontier models pass (d04).
- Gap 10 (partly). Crow result challenged on method by Dymond and Stewart 2016 and Vonk 2015 (d13). No formal failed replication of crow or pigeon found.
Still open:
- Gap 2: only a small-model narrative result (d09), no equal-token test.
- Gap 4: no study of averaging over shuffled orders (d14); reasoning models still lose 5-8 points under premise shuffling in some blocks (d10).
- Gap 5: no 2025+ test of self-generated analogical exemplars (d15).
- Gap 7: no new rhesus or ape training data found; effect size across species not computed.
- Gap 9: no LLM study of distractor similarity or context length mirroring Smith 2019; only loose analogues (irrelevant premises, d10; object count and noise, d04).
Corrections: the Musker "permuted pairs" condition shuffles the order of example lines inside a question (d14).
