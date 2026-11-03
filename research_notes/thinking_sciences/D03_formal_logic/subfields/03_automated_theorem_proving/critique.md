# Critique and cross-check, D03.03 Automated theorem proving

Checked against full-text PDFs (opened this session): DeepSeek-Prover-V2 (2504.21801), Kimina-Prover (2504.11354), DSP (2210.12283), GPT-f (2009.03393), LeanDojo (2306.15626), Seed-Prover (2507.23726), Hilbert (2509.22819), Goedel-Prover-V2 (2508.03613), LINC (2310.15164), PutnamBench (2407.11214).

## Corrections made
1. Kimina vs DeepSeek numbers mixed up. The row 52.94% (pass@1), 65.16% (pass@8), 68.85% (pass@32), 77.87% (pass@1024), 80.74% (pass@8192) is Kimina-Prover-Preview 72B's own row (Kimina paper, section 3.2.1 and table). The DeepSeek-V2 table prints it as a comparison, and PDF text layout merges the rows. So b12 ("7B CoT 77.87% at pass@1024 vs 7B non-CoT 52.94% at pass@1", "non-CoT 671B 80.74%") and c12 ("7B CoT 68.85% at pass@32") wrongly credit Kimina numbers to DeepSeek. a18/b13 (Kimina 52.94 / 68.85 / 80.74) are right. DeepSeek-V2's own numbers (82.4% pass@32, 88.9% pass@8192, 217/244, 47/658, 761.8 vs 6751.9 tokens) are confirmed. Layout was jumbled, so DeepSeek 7B figures should be re-read from a clean table.
2. DSP: b03 says "DSP with human informal proof 38.9%". Wrong. Paper: human proof gives 42.6% valid, 39.3% test; Minerva 62B 43.9% / 37.7%; Minerva 540B 42.6% / 38.9%. 200 of 488 proved with human proofs. a14 and c04 are right.
3. Hilbert is dated 2025 in some lines and 2026 in c19; arXiv id 2509 is Sept 2025. Use 2025.
4. Confirmed unchanged: GPT-f 56.22 vs 21.16, 700m 31.58 / 42.56, policy+value 44.59 / 47.21; LeanDojo 51.2 / 47.6 / 29.0, novel 26.3 / 23.2 / 7.4, 21.1% to 1.4% misjudged; Seed-Prover 78.1% (121/155), 99.6%, 331/657, CombiBench 30.0 vs 10.0, MiniCTX-v2 81.8 vs 44.3, IMO 2025 4/6 then 5/6, Seed-Geometry 43; Hilbert 99.2%, 462/660 (70.0%), 49.1%, 88/660, 96.7% (+35.4), Seed-Prover 50.4%; Goedel-V2 84.6 / 88.1 / 90.4 / 86 at pass@184; LINC 72.5 vs 75.3 p=0.58, 96.4/98.3, 38% syntax errors; PutnamBench 1/640, 0/640, 4/640, 3/640, 1/412.

## Contradictions between sources
- Whole-proof vs tree search: Baldur says whole-proof wins; DeepSeek-V1.5 shows only +3.3 points for MCTS; sample-matched comparisons are rare.
- Neurosymbolic help is not uniform (LINC with GPT-4 on FOLIO is below CoT, not significant).
- Formal vs informal: DeepSeek-V2 own table shows informal majority vote (8/15) beating formal (6/15) on AIME, while formal wins on olympiad-level items elsewhere.
- Hilbert: 2.3M tokens at 99.2% vs 4.0M tokens at 97.9% are different configurations, so "43% fewer tokens" is a configuration claim, not a clean ablation.

## Weak spots
- Pass@k numbers are not token-matched across papers; sample count hides reasoning length (DeepSeek CoT 6751.9 vs 761.8 tokens).
- Possible contamination: miniF2F and PutnamBench are public; near-100% miniF2F results are saturated and say little about generalisation.
- Seed-Prover and Hilbert use huge, partly proprietary compute; not reproducible at our budget.
- Statement formalisation for IMO 2025 was done by humans in Seed-Prover.
- No study here tests a light scaffold (no training) on proof tasks at fixed tokens; nearly all gains come from training.

## Seen only in snippets or secondary pages (opened:false)
a01 (Logic Theorist, via Wikipedia), a02 (Davis 1954), a03 (Robinson 1965), a04 (Gilmore, Davis-Putnam), b19 (Robinson), b20 (CASC J12 results, no counts). Classic-era claims (K15) are weak. Many other lines (Thor, Magnushammer, Baldur, COPRA, SATLM, Lean-STaR, LeanAgent, AlphaGeometry 2) were not re-opened in this cross-check; only the 10 papers above were.

## GAPS
1. At equal total tokens, does a training-free scaffold (sample, check, repair with kernel error) match trained provers on a small fixed Lean/Isabelle benchmark when run with a frontier general model? (Hilbert is the only hint: 49.1% alone vs 99.2% with a specialised prover.)
2. How much of Hilbert's and DSP's gain comes from decomposition itself versus the specialised prover or extra tokens? Needs a matched-token ablation.
3. How often does autoformalisation (S2) silently change the statement, and does a round-trip check catch it? Only Wu et al. 25.3% perfect is known.
4. Does the exact-checker route help on non-formal tasks (SAT, code with tests, arithmetic) as much as on Lean, and where does translation fail (AR-LSAT 32.6% executable)?
5. Does lemma/subgoal-library retrieval transfer to novel premises? LeanDojo drops from 51.2 to 26.3; any 2024-2026 fix?
6. Token-matched comparison of whole-proof sampling vs tree search with a verifier (Baldur vs HTPS vs DeepSeek RMaxTS).
7. Classic ATP numbers: CASC results, E/Vampire solve counts, and whether LLM-guided premise selection helps saturation provers.
8. Null or failed results: papers where LLM plus prover did not help, or Lean results that did not replicate across versions.
9. Cost per verified proof (tokens or dollars) for general frontier models on PutnamBench-like tasks.

## Gap search results (gap searcher, 2026-11-03)
Evidence in evidence_d.jsonl (d01-d17, all opened this session as full PDF text). Claims K05, K08, K10, K14, K16 updated; K18-K22 added.

1. Training-free scaffold vs trained provers at equal tokens: PARTLY CLOSED, still open on matching. Theo (Claude Opus 4.7, agent scaffold, no training) solved 32/32 random PutnamBench items; Aleph (GPT-5.2 agentic) 637/672 at $54 and 668/672 at $68; trained DeepSeek-V2-671B only 47/672. No study matches tokens, so the head-to-head test is still ours to run (K18).
2. Decomposition vs prover vs extra tokens (Hilbert/DSP): PARTLY CLOSED. Hilbert prover alone (pass@4) 75% vs 98.4% at depth 2; the ETH router paper shows an 8B prover goes from 23/85 to 48/85 with decomposition plus lemma attempts. The "43% fewer tokens" was a clean retrieval ablation (99.2% at 2.3M vs 97.9% at 4.0M tokens), not a configuration mix-up. A matched-token decomposition ablation is still missing.
3. Silent statement change in autoformalisation: CLOSED enough. miniF2F-v2: whole pipeline about 36% vs 97% and 69-71% for parts; more than half of the problems had formal/informal discrepancies; LLM judge 97% vs human 66% faithful for Herald @128. A model round-trip check does not catch it (K21).
4. Exact-checker route on non-formal tasks: PARTLY CLOSED. SATLM: large gains on constraint tasks (GSM-SYS 69.4 vs 43.4), none on plain GSM (71.8 vs 72.7); solver turns errors into refusals. Code-with-tests and arithmetic not studied here. AR-LSAT 32.6% executable not re-checked.
5. Library retrieval on novel premises: PARTLY CLOSED. Rango (Coq) loses about 5 points on unseen projects (32.0% vs 36.8%) with in-project proof retrieval (proof retriever +47%, lemma retriever +3%); LeanAgent continual update proved 155 sorry theorems; Hilbert retrieval cuts reasoner tokens. No direct re-run of the LeanDojo 51.2 to 26.3 comparison.
6. Token-matched whole-proof vs tree search: STILL OPEN. Only sample-matched: RMaxTS under 0.2% over naive retry at 3200 samples (ProofAug). No token-matched Baldur vs HTPS vs DeepSeek study found.
7. Classic ATP numbers and LLM-guided premise selection: PARTLY CLOSED. Neural (not LLM) clause selection in Vampire: +101% Mizar40 test, +24.7% Isabelle, +93.5% CoqHammer, but below default off-distribution. CASC J12 summary counts not obtained (page too large; per-problem tables only). LLM-guided premise selection for E/Vampire not found.
8. Null/failed results: PARTLY CLOSED. Four negatives found (d17). No Lean-version non-replication found.
9. Cost per verified proof: CLOSED enough. About $5-70 for frontier general-model agents, $18-170 for trained provers (author estimates; subscription vs API list differ 6x) (K19). Leaderboard figures not independently verified.

Still open: items 1 and 2 token-matched ablations, item 6, CASC counts, LLM premise selection for saturation provers.
