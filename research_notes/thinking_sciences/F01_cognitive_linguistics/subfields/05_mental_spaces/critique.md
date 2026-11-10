# Critique: Mental spaces (F01.05), cross-check

Sources re-opened this session (full PDF text from arXiv): Steele, Wen & Han 2026 (2607.10248), SimToM (2311.10227), SymbolicToM (2306.00924), FANToM (2310.15421), Hi-ToM (2310.16755), Li/Yu/Ettinger (2305.16572), Wu et al. (2307.02477), Feng & Steinhardt (2310.17191), Hypothesis Search (2309.05660), Kim & Schuster (2305.02363). PDFs deleted after extraction.

## Corrections and confirmations (10 checked)
1. Steele et al.: Qwen transfer index 0.73 has CI [0.67, 0.78]; the lower bound is under the pre-set 0.7 bar. Pythia 0.885 [0.882,0.889], Falcon3 0.711 [0.662,0.741]. Evidence a11 and c01 state the means as passing without flagging this. Confirmed the numbers, added the caveat (claim K02).
2. Steele et al.: DAS rank-1 0.883 (a12) is one seed; the 3-seed mean is 0.96 [0.88,1.00]; diff-of-means 0.59. Both are right, different aggregation. Equal 0.583 values for random and diff-of-means are stated by the authors as not a typo. Confirmed.
3. Steele et al.: cosine 0.11 / 0.17, bleed +0.07 / +0.09, belief margin +0.08 / +0.03 / +0.09, 14B belief 0.74/0.79, counterfactual 0.33/0.86, future flip 0.81/0.90/0.83, past-present 0.90 vs floor 0.03, Llama-8B 0.31: all confirmed in text.
4. SimToM tables: GPT-4 ToMI FB 25.5 / 74.25 / 87.75, GPT-3.5 67.25 / 34.0 / 81.0, ablations 58.75 and 31.75, oracle 96: confirmed. Note GPT-3.5 zero-shot (67.25) beats its CoT (34.0), which evidence a17 shows only indirectly.
5. SymbolicToM: LLaMA-7B 99/92/88 and GPT-3 davinci 92 confirmed. GPT-3.5 third-order: the paper shows +91 (about 9% to 100%), evidence says "8% to 100%". Minor; treat as about 9%.
6. FANToM: human 87.5 and GPT-4 26.6 / 40.2 / 57.7 are Table 1 (short conversation context, "All" metric). All* for GPT-4 0613 June is 18.4. Evidence a21 did not say "short context". Corrected in claim K12. Oct GPT-4 All 14.8 confirmed (All* 6.8).
7. Hi-ToM: GPT-4-32k 60.42 / 64.04 (CoT prompt), Claude-instant 49.33, GPT-3.5 28.67: confirmed. Order-4 claims not re-checked.
8. Li et al.: Exp1 "right in both conditions" GPT-2 18.8, GPT-3 50.0, BERT 9.4, RoBERTa 31.3, MPNet 28.1 confirmed; counterfactual-only preference rows BERT 53.1, RoBERTa 68.8, MPNet 46.9 confirmed. Two different metrics; a22 and b03 are consistent but must not be mixed.
9. Wu et al.: GPT-4 base-8/9/10/11/16 = 82.3 / 23.4 / 100.0 / 38.4 / 63.0, and CoT 98.2 / 38.6 / 56.5 for bases 10 / 9 / 11: confirmed.
10. Kim & Schuster: 62.7%, 87.6%, 12.4%, 86.8%, 3.1%, "over 25% after 7 operations": confirmed. Hypothesis Search 17/30/33 confirmed, plus an intermediate 23% (abstract hypothesis generation without summaries) that the evidence omitted. Feng & Steinhardt 99% / 3% / 97% confirmed.

No number was wrong enough to change a conclusion.

## Contradictions and tensions
- Steele says nested spaces read at ceiling with no bleed (strong models, shallow nesting); Hi-ToM shows near-zero accuracy at order 4. Different tasks (colour lookup versus recursive ToM reasoning), so not a refutation; marked contested (K13).
- Steele: "no bleed" in behaviour (a14) versus "context bleeds" in 3B decoding (c03). Behaviour at frontier scale and decoding at 3B are different levels.
- Belief special or not (K25): formal semantics treats belief as distinct; Steele finds a coarse shared taxonomy. One paper.
- ToM brittleness (K11): Kosinski 75% for GPT-4 versus Ullman and Shapira adversarial failures. Both hold; they test different variants.
- Li et al. says models are weak counterfactual switchers; but the models are GPT-2/3-era. Steele and Wu show current models do better on stated spaces. Do not generalise Li to 2025 models.

## Weak spots
- The only direct mechanistic test (Steele et al.) is one group, one preprint (2026-07-11), mostly models of 3B and under, synthetic colour stimuli, and Pythia fails the rule task. Never replicated by others. The belief companion paper (c09) was not opened.
- Nearly all LLM evidence is theory-of-mind. ToM is one use of spaces; hypothesis separation in problem solving (our S2) has almost no direct test. Hypothesis Search is not a spaces study.
- SimToM and SymbolicToM tests use 2022-2023 models; no result with current reasoning models.
- No token-matched comparison: SimToM uses two calls, SymbolicToM uses code. None reports equal-token baselines.
- Human evidence (Ferguson et al., Coulson ERP) was read only as abstracts or without N and effect sizes (b01, b02, a09, a10). Nieuwland & Martin (b22) was recalled, not opened.
- Founding works (a01, a02, a03, b21) not opened; theory, no data.
- Evidence a20/c20 (Ullman) opened only as abstract in one entry; b16 has partial numbers.

## Seen only in snippets or not opened
a01, a02, a03, a09, a10, a26, b21, b22, c09. Entries for Ferguson (b01, b02) are repository abstracts.

## GAPS
1. Does a scaffold that keeps hypotheses in separate named scoped spaces beat a flat shared notes state on multi-hypothesis reasoning (not ToM) at equal tokens with a current model? No study found.
2. SimToM and SymbolicToM gains: do they survive with current frontier and reasoning models, and when the extra call or code is charged to the token budget?
3. Which leaks matter most: does leakage between spaces grow with context length or number of spaces in frontier models doing derived inference (Steele found stated binding at ceiling, derivation hard)?
4. Why does reporting a value differ from using it (K04), and does an explicit "apply the rule inside space X" step close the gap in prompting? Does it replicate outside Steele's synthetic task and outside 3B models?
5. Do counterfactual-space penalties (Wu et al., GPT-4 base 9 at 23.4) shrink for current reasoning models, and does restating the space's rules each step help?
6. Is the belief-not-special finding (K25) replicated by an independent group, and does it change whether we need separate tags for belief, supposition and fiction?
7. What are the effect sizes and sample sizes in the human eye-tracking and ERP work (Ferguson & Sanford 2008, Ferguson et al. 2010, Coulson & Van Petten 2002, Nieuwland & Martin 2012)? Needed to say how much leakage humans show.
8. How does accuracy fall with nesting depth for current models, and does an explicit written stack of spaces fix the order 3-4 collapse seen in Hi-ToM?
9. Did anyone test cost of blending (Fauconnier & Turner) as a prompt method for creative or analogical tasks with measured gains?
10. Backward inference into a space (K14, backward belief .40): does a hypothesis-first step help, and is there data for 2025-2026 models?

## Gap search results

Evidence: evidence_d.jsonl (d01-d19). The search tools were throttled (WebSearch budget used up after one call; arXiv, OpenAlex and Semantic Scholar APIs returned 429), so discovery was limited. Sources opened: 2602.10625, 2601.16853 (PDF), 2504.01698, 2502.11881 (PDF), 2510.04980, 2402.18496 (PDF), 2406.17513 and 2505.06120 (abstract pages), Steele et al. (PDF, re-read), Kulakova & Nieuwland 2016 and the 2022 Ferguson-lab ERP study (full text via Europe PMC), PubMed abstracts for Nieuwland & Martin 2012 and Coulson & Van Petten 2002, Lynn 2026.

1. Scoped hypotheses versus flat notes (not ToM): STAYED OPEN. Nearest is thought-tracing (d10-d12): weighted per-agent hypotheses beat flat CoT on four ToM benchmarks (GPT-4o ToMi 59.5 / 67.0 / 76.0), but it is ToM and has no flat-list control at equal tokens. New claim K27.
2. SimToM and SymbolicToM with current models: PARTLY CLOSED. No re-test of SimToM or SymbolicToM was found. Current evidence: reasoning models do not reliably beat non-reasoning ones (d04), classic false belief is near ceiling (d07), and a scoped scaffold with a non-reasoning model matches reasoning models at lower token cost (d11, authors' statement, token counts in a figure). Equal-token comparison against SimToM itself still missing. K28, K29.
3. Leakage versus context length or number of spaces: STAYED OPEN. Only indirect evidence (d14, multi-turn lock-in, 39% drop). K32.
4. Report versus use gap closed by a prompt step: STAYED OPEN. Steele et al. run no prompting test (d01). Untested design guess.
5. Counterfactual penalty for reasoning models (Wu et al.): STAYED OPEN. No 2025-2026 re-run of the counterfactual-base tasks was found; searches for it failed on rate limits. Do not generalise Wu's GPT-4 numbers.
6. Belief-not-special replication: STAYED OPEN. The companion belief paper is by the same group (d01). Independent groups (Zhu d02, Bortoletto d03) show belief representations are linear and structured but do not test the space-type taxonomy. K25 stays contested, one source.
7. Human effect sizes: PARTLY CLOSED. Got N and statistics for Kulakova & Nieuwland 2016 (N=30; counterfactual mood 0.72 microvolt, F(1,22)=8.44, eta-sq .28) and N=48 for the 2022 switching study; Coulson & Van Petten N=18. Not obtained: Ferguson & Sanford 2008 and Ferguson et al. 2010 eye-tracking numbers (PubMed search found nothing), Nieuwland & Martin N and amplitudes (abstract only). K30.
8. Nesting depth for current models: CLOSED for the depth curve, OPEN for the fix. HiToM orders 0-4 for nine 2025-2026 models (d05): best o3 0.996 to 0.467; DeepSeek-V3 0.979 to 0.608; R1 0.988 to 0.196; Hanabi second order costs 10-20 points (d13). RL fixes order 4 (d09) but no explicit written stack was tested. K13 updated.
9. Blending as a prompt method: STAYED OPEN. No measured gain found (d19, conceptual paper). K31.
10. Backward inference and hypothesis-first: PARTLY CLOSED. Zhu et al. backward belief 0.40 even after steering (d02); thought-tracing ablation shows the perception-inference step matters most (-7 to -20 points, d12). No hypothesis-first prompt test on backward items. K14 updated.

New caveats: the HiToM comparison paper (2602.10625) gives no N or token costs; de Haan et al. use two items per cell; thought-tracing tables were partly garbled in text extraction, so only unambiguous rows were recorded; Zhu et al. baseline row not read reliably.
