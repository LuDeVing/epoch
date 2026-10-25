# Critique and cross-check: E06.01 Polya heuristics

## Corrections made (10 numbers re-opened in the paper text, this session)
1. Plan-and-Solve (arXiv 2305.04091v3, Table 2, text-davinci-003). Confirmed a15/c03: CoT 70.4, PS 72.9, PS+ 76.7, Manual-CoT 77.6; GSM8K 56.4/58.2/59.3; MultiArith PS 87.2. CORRECTION to b09/b20/b28-style rows: b09's "PS 73.5, GSM8K 57.0, MultiArith 92.2, SVAMP 70.8" is the Zero-shot PoT row, not PS. b09 is wrong on the PS row. The earlier "PS 87.2 vs 92.2" gap is a row mix-up. PS+ does NOT beat manual 8-shot CoT on average (76.7 vs 77.6), but beats it on GSM8K (59.3 vs 58.4) and AddSub/AQuA/SingleEq.
2. Plan-and-Solve symbolic: PS+ 75.2 vs manual CoT 70.6 on Last Letter (Table 4). Not in the evidence files.
3. Step-Back (2310.06117) MMLU table confirmed exactly (PaLM-2L 66.4/70.9 to 73.2/81.8; GPT-4 CoT 82.9/85.3 vs Step-Back 84.5/85.6). Note GPT-4 1-shot physics is 78.4, so the baseline is strong.
4. Step-Back 20.5% fixed / 11.9% introduced confirmed (line in paper).
5. Least-to-most (2205.10625): SCAN length 16.7 standard, 16.2 CoT, 99.7 L2M confirmed. GSM8K 60.87 vs 62.39 and by-steps table (2 steps 76.68 vs 74.53; 5+ steps 39.07 vs 45.23) confirmed. Caveat: a later appendix table labels the 60.87 row "Least-to-Most (1-shot)", so row labels are inconsistent inside the paper; main text agrees with a20/b11.
6. Self-Discover (2402.03620) table confirmed for PaLM 2-L and GPT-4. 74.7% computation errors of 99 wrong MATH answers confirmed. "23/25 vs direct, 21/25 vs CoT" confirmed (a21 is right; c07/b14 consistent).
7. Analogical prompting (2310.01714) Table 1: CORRECTION to b13. The 75.0% GSM8K figure is the 0-shot row, not 5-shot CoT. Correct GPT-3.5 GSM8K: 0-shot CoT 75.8, 5-shot CoT 76.7, self-generated 77.8 (c05 right). MATH GPT-3.5 33.9/34.9/37.3; PaLM2 29.8/34.3/34.8. Text extraction of the table is garbled, so row mapping is by position, with c05 as agreement.
8. Backward reasoning (2310.01991): GSM8K GPT-4 92.8/38.6, PaLM-2 58.4/10.8, LLaMa-2-70B 60.5/15.2; MultiArith GPT-4 97.8/54.8, LLaMa-2-70B 95.7/6.3 confirmed.
9. a24 said analogical gain on davinci is "6.9 to 10.7"; table gives 61.0-54.0 = 7.0 and 61.0-50.3 = 10.7. Minor.
10. Not re-opened (paywalled or unavailable): Schoenfeld 1992 (a/b opened it but it is one source), Hembree 1992, Trinchero and Sala 2016, Rott and Gawlick 2014, Lester et al. 1989. The disk filled up mid-session (0 MB free), which truncated several downloads; no data was lost in the deliverables.

## Contradictions between sources
- b09 vs a15/c03 on PS numbers: resolved as above (b09 wrong).
- b13 vs c05 on analogical 5-shot GSM8K: resolved (c05 right).
- a13 note: Lucas (1974) study length differs between sources (8 vs 13 weeks); unresolved, low importance.
- Evidence for "heuristic menus help" (Self-Discover, Step-Back, PS) conflicts with c01 (blog: menus hurt small models) and c18 (little gain on strong models). Boundary: model strength and error type.
- Teaching literature: a03 (little support in the 1970s) vs Schoenfeld's own later claim that fine-grained strategies work (b21) and Hembree. These are consistent only if "grain of specification" is the variable.

## Weak spots
- The central Schoenfeld control result (60% vs under 20%) comes from one chapter, with no N, no test, no control group. a05 and b05 are the same source, so it is counted once.
- Most LLM evidence is from 2023-era models (text-davinci-003, PaLM-2, GPT-3.5). Gains shrink on strong models (GPT-4 step-back, analogical on chat models). Almost nothing is measured on current reasoning models except the 2026 preprints.
- Triple counting: PS, Step-Back, L2M, Self-Discover each appear in three files. They are single papers, so independent_sources=1 in claims. Only claims with two truly different sources are marked established (K02, K04, K21).
- Equal-token control is missing in most LLM studies. PS+ and self-generated exemplars use longer outputs; Self-Discover uses 3 extra calls per task. Gains may partly be extra compute.
- Heuristic names as tested are mostly single Polya items (plan, abstract, related problem, decompose). Work backwards, draw a figure, and look back have almost no LLM-measured results.

## Seen only in snippets or second hand
- a14 (Schoenfeld 1985 book), a27 (Koichu 2007), c06 (L2M from memory, now verified), c10, c16, c17, c20 not opened. Hembree numbers only via Bruun. c01 is an informal blog. a23-a26 and a29 are anonymous preprints.

## GAPS (most decision-relevant first)
1. At equal tokens, does a Polya-style operator menu (O1-O5) beat plain CoT or self-consistency on a current reasoning model? Nearly all measured gains are on older models and ignore compute.
2. Which problem features predict when each heuristic helps or hurts (specialise, work backwards, auxiliary element, decompose)? Only a blog (c01) gives per-type data. A selection rule with preconditions is untested.
3. Does a control step (periodic what/why/does-it-help check) improve LLM reasoning models, and how often does the model fail to notice dead ends? Schoenfeld's 60% to under 20% has no LLM replication here.
4. Is the bottleneck selection or execution? L2M and Self-Discover say structure is rarely the failure (25.3% structure vs 74.7% computation), but L2M says choosing the decomposition is. Needs a direct split on one model.
5. What are the Hembree effect sizes by grade and by method (Polya heuristic vs other)? Needed to calibrate how large an effect to expect.
6. Is there any LLM evidence for "draw a figure", "look back" (verify/generalise afterwards) and "work backwards" as prompted operators at equal tokens? Backward reasoning is hard for models (c08), so the operator may need reformulation.
7. Do wrong or unrelated heuristics cost accuracy (c09 says yes for wrong hints)? How much damage does a mis-selected heuristic do, and can a self-check catch it?
8. Does heuristic diversity (c11) give gains through union of attempts with a verifier, versus single best-strategy selection (c12, c13)?
9. Replication of Schoenfeld 1979 and Rott and Gawlick 2014 with larger samples: is the human effect real and how large?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d16, all opened this session; d15 is abstract only). Claims K25 to K30 were added and K02, K03, K04, K15, K17, K23 gained evidence ids. The web search quota ran out early, so the arXiv API, Crossref and ERIC record were used. No gap is fully closed, because no source tests a Polya operator menu on a current reasoning model at equal tokens.

1. Menu vs plain CoT or self-consistency at equal tokens on a current reasoning model: OPEN. New context only. Generic CoT on reasoning models is marginal or mixed (d02: o3-mini +2.9, o4-mini +3.1, Flash 2.5 -3.3 points; "decompose" and "weigh paths" prompts no better on GPT-4o), and a distilled-R1 study (d14) disagrees but uses a baseline that suppresses thinking. Result: K27 contested. Diversity of named approaches beats same-call-count sampling on non-reasoning models (d03, d04, K28), which is the closest equal-budget evidence for a menu.
2. Problem features that predict which heuristic helps: OPEN. PRISM (d12) shows no strategy wins across slices and a trained router adds 0.9 to 7.6 points, shrinking with model strength. iSelf-Discover (d13) shows planning granularity depends on task uniformity. No hand-written precondition rule is tested.
3. Control step: PARTLY. Zero-information self-checks hurt older models (d07, d16: GPT-4 GSM8K 95.5 to 89.0), finding the error is the bottleneck (d09: 52.87% best), but reasoning models detect errors far better (d08: o1-mini 87.9 vs GPT-4o 61.9 average F1). So the case for a concrete control step on a reasoning model is plausible, not shown. Schoenfeld's 60% to under 20% still has no LLM replication. K25 established (for 2023-24 non-reasoning models), K26 single-source.
4. Selection vs execution: OPEN. No direct split on one model found. d13 shows plan format matters (prose beat JSON by 9 to 12 points on MATH) but does not separate choosing from executing.
5. Hembree effect sizes: OPEN for numbers. Only the abstract was reachable (d15): no method better in K-5, heuristics mildly better in 6-8, distinctly better in high school, diagram training the largest gain. Needs the full paper.
6. Draw a figure, look back, work backwards at equal tokens: PARTLY. Work backwards helps as a check or reformulation, not as a solver (d11 +1 to 2 points over self-consistency with extra chains; d10 training only). Look-back with no new information hurts (d07). Nothing on "draw a figure" for LLMs; Hembree's abstract points to representation as the strongest human lever. K29 single-source.
7. Cost of a mis-selected heuristic and whether a self-check catches it: PARTLY. A mis-aimed fix is costly (d16: random backtracking broke 7 to 16 points of correct traces; d12: one strategy ranged from 13.5 to 95.3 across datasets). Self-check catching it is not shown (d07, d09). Intervene only on evidence of failure.
8. Diversity with verifier vs single-strategy routing: PARTLY. Diversity beats repeated sampling under majority vote (d03, d04). Routing beats best single strategy (d12) but its ensemble baseline looks mis-tuned. No head-to-head with a verifier. K21 (union with a verifier) stays the only verifier-based support.
9. Replication of Schoenfeld 1979 and Rott and Gawlick: PARTLY. Rott and Gawlick re-opened (d01): n=9/10/9, d about 0.8 (explicit vs practice 0.79, vs no training 1.44), posttest harder than pretest; the authors ask for a much larger study. No larger replication found, but the search was cut short, so absence is weak.

Corrections to earlier files: none needed. Cautions added: d14 and d02 contradict, so K27 is contested; the PRISM ensemble baseline (GSM8K 24.0) is not a reliable comparator.

Next best experiment: O1-O5 menu vs bare problem vs k-way approach split (d03 style) on one reasoning model, 25 samples per problem, paired test, thinking tokens logged, plus a control-step arm that is concrete (substitution, special case) rather than generic.
