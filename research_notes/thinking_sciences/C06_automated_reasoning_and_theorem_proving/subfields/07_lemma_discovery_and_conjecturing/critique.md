# Critique: Lemma discovery and conjecturing (C06.07)

Cross-check done 2026-10-26. I re-opened the arXiv PDF text (pdftotext) for ten sources and checked about 45 numbers. Most numbers are right. Corrections are below.

## Numbers re-checked and confirmed
- LEGO-Prover (2310.00656): 57.0/50.0 at 100 attempts; 50.4 vs 47.1 library ablation at 50 attempts; skill origin 10.8/38.2/51.1%; 257 of 488.
- STP (2502.00212): 28.5% vs 13.2%; 65.0%/23.9%/8-of-644; 131 of 2.5M; at least 47%; 11.4% checkpoint; 98.5% compute wasted (cited from earlier work).
- Rabe (2006.04757): 32.19/26.20, 19.61/12.28, 82.32/12.70, 97.75/0.59; 3445/3857, 979/3440, 49/130.
- MathlibLemma (2602.02561): funnel 3427/2591/3130, 71.4/66.6/63.2% judge, compilable counts 1887+1219+1211 = 4317, 4,028 final, 1,506 proofs, 107 of 138, 54/46% audit, 37.39% union, 19.39% best single, $200 + $500.
- Kasaura CPL (2509.14274 v4): 106 vs 328 theorems, 5/20 vs 0/20, Fisher p=0.024, 309 vs 941, 2106/2123 vs 1935/2123, McNemar 4e-35, 14M tokens.
- Lemmanaid (2504.04942): 7,628 census with 1,721/1,356/1,802/2,749; 50.2% / 28.6%; 58.6% / 42.7% ensemble; 84.9%; QuickSpec 22.8% and precision under 1%; AFP-2026 numbers for Opus 4.5 and GPT-5.2.
- Kaliszyk and Urban (1402.3578): 61.7 to 64.8; 54.5 to 61.4 to 63.8; 76.5 cheating; 33% subsumed.
- Johansson and Smallbone survey (2109.03721): Vampire 7 plus 18 = 25; HipSpec 44, CLAM 41, Zeno 21.
- Hilbert (2509.22819): 99.2%; 462/660; D=0 75%, D=2 98.36%, D=3 98.7%; 548 vs 862 reasoner calls.
- Seed-Prover (2507.23726): 121/155 = 78.1% heavy; 47/55, 47/56 (and 27/44 hard); 5000 conjectures by default.

## Corrections
1. TheSy vs Hipster timing (b15). The total times 51.6K s (TheSy) vs 47.1K s (Hipster) are WITH TheSy case splitting. The paper says case splitting causes the slowdown; without it TheSy is much faster. b15 wrote "without case split", which is wrong.
2. Seed-Prover (b12). The 99.6% miniF2F and 331/657 PutnamBench results are from the MEDIUM setting, not heavy. Only the IMO 121/155 and the 5000-conjecture default belong to heavy. Do not credit large conjecture pools for the miniF2F or Putnam numbers.
3. Lemmanaid Octonions (a05/b05/c07/c09). Two different figures appear for the best system: 78.9% (Lemmanaid types+defs, HOL+AFP training, in Table 1, quoted in the text as "best reaching 78.9%") and 76.6% (DeepSeek-6.7B template combined, in the commercial-LLM table). They are different table rows, not an error, but they should not be mixed. The neural baseline is 62.3% in the text (and 61.7% in the commercial table). The extracted Table 1 text is scrambled, so which row holds 62.3% was not independently confirmed.
4. MathlibLemma cost (a22/c13). $0.46 per proof is the all-in cost ($700 / 1,506). Proving alone is about $0.33 per proof. Both are in the paper. Also the denominator for "useful" is released proofs after a bypass screen, not statements proved.
5. Kasaura numbers across versions (a14/a15 vs c04/c05). a14/a15 report "30 loops, 269 theorems vs 400 loops, 359 theorems" and "267 of 269". These do not appear in the current arXiv v4 (29 Jun 2026) text I opened. c04/c05 (106 vs 328, 2106/2123) do. The a14/a15 numbers probably come from an earlier version. Treat them as version-specific and do not cite them. Likewise the "128 tries" for the alpha-open re-proof was not found in v4 (v4 says 16 tries for 5 contexts).
6. LEGO-Prover (a12). a12 says ICLR 57.0/50.0 and "later arXiv v3 headline 50.4 valid / 47.1 test". The version I opened lists 57.0/50.0 at 100 attempts. The 50.4 and 47.1 figures are the ablation (library vs no library) on the VALID set at 50 attempts, not valid vs test. The table in the PDF text is garbled, with 47.1 labelled "human informal proof", so the table labels alone are unreliable; the body text is clear. Use the body text.
7. GPT-4o "10 times" (c06). The denominator was not found; I used "10 times" without a ratio in claim K17.

## Contradictions and tensions between sources
- LEGO-Prover shows a 3.3-point library gain (small), while Seed-Prover and Hilbert credit lemma pools and decomposition for large gains. These are not comparable: different provers, compute and benchmarks.
- STP: conjectures help training, but the final re-training gain is only 2-3 points. The headline 28.5% vs 13.2% is on the training set (LeanWorkbook), where the model sees the statements; it is not a generalisation measure.
- Rabe: weighted sampling raises "provable" to 97.75% but "provable and new" falls to 0.59%. Provable alone is a trap metric. Lemmanaid shows the same shape: 22.6% gold but 36% unresolved.
- Lemmanaid commercial LLMs do worse with templates than with direct writing (19.4 vs 34.5 for Opus), while the small trained model does better with templates. Templates are not free help for strong general models.
- CPL longer proofs (KS p=1e-13) may mean harder lemmas or just more verbose proofs; not separated.

## Weak spots
- Many "useful fraction" numbers use different meanings of useful: matches a human gold lemma (Lemmanaid), used at least once in a proof (Rabe), used for the final goal (TBC), merged into Mathlib (MathlibLemma). They cannot be put on one scale. Claim K01 reports them side by side, not as one rate.
- Most LLM results are single runs or few seeds, with no confidence intervals (LEGO, STP, Lemmanaid). Only CPL gives a test (Fisher).
- Training-based results (STP, Minimo, Gauthier and Urban) may not transfer to a no-training scaffold.
- Contamination: Mathlib and AFP lemmas may be in model training data. Lemmanaid's AFP-2026 split is the only leakage-controlled test, and it is single group.
- Graffiti, HR and AM claims lean on historical or secondary sources.

## Only seen in snippets, abstracts or secondary pages (not full text)
- a03 Ritchie and Hanna (1984): abstract only (opened:false).
- a19 Lemmanaid early citation, a18 Subgoal-Learning numbers via LEGO-Prover's table.
- b22 Lenat and Brown 1984 journal version: snippets only.
- b23 Ritchie 1991: abstract only, no online copy.
- b26 HR (Colton 2002) book: blurb only. b27 Graffiti "80 papers, 60 proved": secondary, unverified. b25 TxGraffiti: abstract only for proof rate.
- b21: Ritchie and Hanna content via Wikipedia.
- c28 AutoGraphForge: abstract only.
- c29/c30: synthesis notes, not sources.

## GAPS (most decision-relevant first)
1. At equal tokens, does asking an LLM for lemmas inside a single reasoning session (no training, no external prover) raise correctness on hard problems versus spending the same tokens on a longer direct attempt? No paper tests this directly.
2. What fraction of LLM-proposed lemmas in a plain-text (non-formal) setting are true and used, and how does a cheap self-check (small cases, counterexample search) change that fraction? All numbers found are for formal Lean or Isabelle settings with a checker.
3. How much of the lemma-library gain survives de-duplication, triviality filtering and a held-out split? LEGO-Prover's +3.3 points has one split and admitted trivial lemmas.
4. Does a lemma proposed for one problem transfer to different problems (cross-problem reuse count), as opposed to reuse inside one run? Rabe, LEGO and CPL measure only same-run reuse.
5. Are the gains of Seed-Prover and Hilbert due to lemma pools and decomposition or to stronger base models and compute? An ablation with the prover held fixed and equal tokens is missing (Hilbert D=0 vs D=2 is the closest).
6. What is the best number of conjectures to propose before proving (breadth vs depth)? Seed-Prover uses 5,000; CPL ran 106 per run; LEGO ran thousands. No curve of success against number of conjectures at fixed budget.
7. Do goal-directed conjectures (bridge to a named target) beat undirected ones (explore a theory)? CPL, TBC and Lemmanaid mix both purposes; no paired test.
8. Why do commercial LLMs do worse with templates than direct writing (Lemmanaid), while small tuned models gain? Is it prompt length (about 1700 vs 325 tokens), format or capability?
9. How good is a judge model at deciding whether a conjecture is interesting, new or trivial? MathlibLemma judge false-negative rate was 46% on a small audit (n=53); there are no calibrated numbers for other judges.
10. Does symbol renaming (recall test) change LLM lemma quality in other domains beyond Johansson and Smallbone's drawing language? A single case study so far.

## Gap search results
Method note: the web search quota was exhausted, so this pass opened nine arXiv full texts by direct ID (Hilbert, Seed-Prover, LEGO-Prover, Large Language Monkeys, DeepSeek-Prover-V2, Si et al., GSM-Symbolic, Putnam-AXIOM, CounterMath, Least-to-Most). Evidence is in evidence_d.jsonl (d01-d16). New claims K18-K21; K03, K06, K09, K15 got extra evidence.

Closed (as far as the literature reachable now goes):
- Gap 5 (partly): no ablation holds the prover and tokens fixed. Hilbert's D=0 is a pass@4 prover with no informal reasoner. Seed-Prover has no lemma-pool ablation. The gain is confounded with a strong reasoner (d01, d02, d05, d15). Answer: unconfirmed, and the confound is now documented.
- Gap 3 (partly): LEGO-Prover already de-duplicates (SequenceMatcher under 0.85). The no-library arm also drops the evolver. No held-out split. Stays unmeasured but the confounds are specific (d06, d07).
- Gap 4 (narrowed): LEGO's library is shared across problems in one run; about 24% of 135 proofs (about 32) used retrieved skills. No per-lemma cross-problem count (d07).
- Gap 9 (partly): judges are weak elsewhere too (53.3% vs 56.1% human-human on idea ranking). No math-conjecture judge calibration found (d10).
- Gap 10 (partly): renaming alone does nothing on word problems, but constant perturbation lowers Putnam accuracy by 19.6 points for o1-preview (d11, d12). Not the same test as Johansson and Smallbone.

Still open (no new direct evidence, partly because search was unavailable):
- Gap 1 (equal-token lemma-first vs direct): only baselines found (d08, d09, d14).
- Gap 2 (plain-text lemma truth rate): only that self-judged counterexamples are weak (d13) and verifiers drive conversion (d08).
- Gap 6 (best number of conjectures), gap 7 (goal-directed vs undirected), gap 8 (template vs direct for commercial models): nothing new.
