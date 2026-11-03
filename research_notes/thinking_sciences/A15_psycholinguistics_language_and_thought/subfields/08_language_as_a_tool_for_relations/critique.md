# Critique: A15.08 Language as a tool for relations (cross-check)

## Re-opened numbers (full text read this session)
Confirmed:
1. Jamrozik & Gentner 2020 Exp 1 (a02, a03): baseline 4.58 domain vs 1.56 relational of 10; condition estimates 3.19, 3.40, 2.51, 1.97 (p=.188), 5.67, 6.78. The PDF table is scrambled by extraction; matched by recomputing exp(B). Domain-label Bayes factor 0.389 confirmed.
2. Anderson et al. 2022 (a13): Ferry infants 18.31 vs 13.21 s; label infants 16.60 vs 16.05 s; F(1,121)=5.05, p=.026; 34 of 64 looked longer at novel; p=.354. Note: in the relational-label test trials alone the means were 20.32 vs 17.02 s (n.s.); 16.60/16.05 is the pair-habituation phase. Do not merge them.
3. Zheng et al. 2025 (a16, b01): Exp 1 transfer language b=2.278, p=.001, OR 3.15; alignment b=1.938, OR 2.66; repair alignment OR 2.31, language p=.58.
4. Hu et al. 2023 (c01, c02): 77.2%, 28.2%, 51.8%, 22.2 -> 45.6%, 72.0%, 93.2% all found in text.
5. Sourati ARN (c18): GPT-4 94.0/92.5/57.1/29.1, human 98.6/97.2/96.8/91.4 confirmed.
6. ConceptARC (b21): Above/Below .90/.23, Same/Diff .93/.20, Inside/Outside .83/.27, Count .86/.03, Order .95/.23 (human vs GPT-4) confirmed.
7. Lewis & Mitchell digit matrices (c08): extraction misplaced row labels, but row order is humans 0.715/0.771/0.704, GPT-3.5 0.813/0.480/0.790, GPT-4 0.810/0.477/0.792 (Digits/Alt-Blank/Symbols). c08 reading was right, but the GPT rows are specifically GPT-3.5 and GPT-4.
8. Webb et al. 2023 (a22, b17): digit matrices N=40; letter strings OR 1.76, p=6.3e-5 overall, and also OR 1.76 (p=.0007) for zero-generalization items alone (a coincidence of values); story OR 0.37, p=.0003.

Corrected:
- a25 (Yasunaga) called GSM8K GPT-3.5 75.0% "0-shot CoT" and 75.8% "3-shot CoT". Table 1 of the paper shows 75.0% is 5-shot CoT and self-generated exemplars give 75.8-77.8%. c10 had it right; use c10. a25's BIG-Bench 0-shot values (word sorting 66.8 -> 75.2; logical deduction 30.0 -> 41.6) match the paper.
- Anderson time pairs: see item 2.

Not re-checked: Zettersten 2024 (a20; PMC fetch returned an error stub), Mind Melds (b11, b12), Lee et al. patching numbers.

## Contradictions between sources
- Labels help infants compare action goals (Gerson & Woodward 2014, a21, not opened) vs no help for same/different at 12 months (Anderson 2022). Likely differing tasks; unresolved.
- Redundant-label advantage (Lupyan 2007, a09) vs failed online replication (b10); Lupyan & Ward 2013 vs the 2026 EEG null (b15, N=20, low power).
- Label effect on immediate repair null but on transfer large (a16): labels help later generalisation, not necessarily immediate performance.
- Webb 2023 (human-level analogy) vs Lewis & Mitchell 2024 (collapse on counterfactual variants); both hold on their own item sets.
- Strong adult but weak child nameability effect (a20).

## Weak spots
- No LLM study tests the Gentner or Lupyan label effect directly (c24). All agent_relevance lines are inference.
- Hu 2023 manipulates input naming, not a controlled relational-label condition; its random-word arm is the nearest control.
- Many older figures (Rattermann & Gentner 1998, Loewenstein & Gentner, Dessalegn & Landau) are second-hand via 2022/2025 papers.
- Label vs comparison vs salience is confounded in most developmental studies.
- Yasunaga analogical prompting is self-retrieval of cases, not relation naming.

## Only seen in snippets or abstracts
b06-b10, b14-b16, b23-b25, c12, c17, c20-c23, a21, a26-a29. Thought Propagation numbers (c12) and Loewenstein & Gentner 2005 are abstract-only.

## GAPS
1. Does adding a relation name (vs a domain tag vs nothing) to a retrieved or in-context case raise relational transfer for an LLM at equal tokens? No direct study.
2. Is the name most useful placed before the case (Jamrozik), and does the effect vanish when the model must generate the name itself?
3. Does compare-then-name beat compare-only or name-only for LLMs (the Zheng 2025 alignment x label design)?
4. Which LLM analogy failures are missing relation information (fixable by naming) vs failure to apply it (Lee 2025)? Is the 38.4% patching gain reachable by prompt?
5. Does naming quality (ordinal vs random vs ASCII, Hu 2023) generalise beyond RAVEN to text relations and ConceptARC groups?
6. Do relation names reduce the far-analogy and surface-distractor gap (ARN GPT-4 far/near 29.1%) for 2025-2026 models?
7. Do label gains survive the perturbations (permuted alphabets, moved blanks) that broke unaided models in Lewis & Mitchell?
8. Does a shared label vocabulary raise agreement across agent samples (Mind Melds alignment), and does it cost diversity?
9. What do the two unread 2026 reviews (Lupyan, Gentry, Zettersten; Liu & Lupyan) conclude about language as a relational tool in AI?
10. Are there further replications of Lupyan 2007 and Jamrozik 2020 beyond the one failed online replication?

## Gap search results
Access note: the arXiv search, Semantic Scholar and OpenAlex APIs returned 429 or budget-exhausted, and WebSearch allowed one query. Work was done by direct page fetches. New evidence is in evidence_d.jsonl (d01-d16); new claims K23-K29.

Closed or partly closed:
- Gap 4 (partly closed): Lee et al. 2025 (d01). The 38.4% patching gain is Gemma-7B (Qwen2.5-14B +35.6%). The paper does not split failures into missing vs not applied and tests no prompt fix, so "reachable by prompt" stays unknown.
- Gap 5 (partly closed): naming/structuring objects helped on ARC (GPT-4 13/50 -> 23/50; 81 -> 97 of 400; d04) but adding relation edges hurt (23 -> 16 with CoT). ConceptARC with naming was not tested.
- Gap 6 (partly closed): AnaloBench (d05) shows the long-story, far-analogy gap persists (GPT-4 60.7% vs human 73.3% at 30 sentences; retrieval near random). Beger et al. 2025 (d08): o3 reaches 77.1% on ConceptARC text (humans 73%) but about 27% of right answers rest on unintended or wrong rules. No relation-name arm.
- Gap 8 (partly closed): Mind Melds re-read (d09). Labels raise alignment (.20 vs .11/.12; .35 vs .21/.27). Diversity cost is mixed, not tested.
- Gap 9 (partly closed): Liu & Lupyan 2026 read in part (d10): no resolution on whether language drives mappings; no AI section found in the text read. Lupyan, Gentry & Zettersten 2026 (d11): abstract only; a position that language gives any learner compact cultural abstractions.

Partial hints for gaps 1-3 (no direct study found):
- Stating the relation in the prompt helped 6 of 9 models (GPT-3.5 45.7 -> 55.3, Zephyr -13.6; d02) and a relation-over-entity instruction helped two of four (d06). Neither isolates a name, a placement, or compare-then-name.

Still open:
- Gap 1, 2, 3: no direct LLM test of relation name vs domain tag vs none, name position, or compare-then-name. This is a constrained search, so absence is unproven.
- Gap 7: Lewis & Mitchell tested no hints or CoT (d07); models state permuted-alphabet rules at near 1.0 yet fail the analogy, so an explicit rule statement is a candidate test.
- Gap 10: no further replication of Lupyan 2007 or Jamrozik 2020 found beyond the failed online replication (b10, abstract only).
