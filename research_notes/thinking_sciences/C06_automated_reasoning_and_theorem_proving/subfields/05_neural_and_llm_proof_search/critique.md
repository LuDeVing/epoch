# Cross-check: C06.05 Neural and LLM proof search

Re-opened this session (full PDF text or PMC page): COPRA (2310.04353), DSP (2210.12283), DeepSeek-Prover-V1.5 (2408.08152), GPT-f (2009.03393), Thor (2205.10893), LeanDojo (2306.15626), Huang and Yang IMO 2025 (2507.15855), AlphaProof Nature (PMC12999475), Goedel-Prover-V2 (2508.03613), Baldur (2303.04910). Not re-opened: Seed-Prover, BFS-Prover, Kimina, STP, HTPS, PACT, curriculum paper, LEGO-Prover, Lean-STaR, Lean Copilot, PutnamBench.

## Confirmed
- GPT-f: 56.22% vs 21.16%; model sizes 34.79/39.94/42.56/42.39; attempts curve +4.39/+3.97/+2.99/+2.45; 23 shortened proofs.
- Thor: 39.0 to 57.0; 8.2%; 1.9% vs 28.2%; Sledgehammer alone 25.7; miniF2F 29.6 to 29.9.
- LeanDojo: 51.2/47.6/29.0/23.8 random; 26.3/23.2/7.4/5.3 novel_premises; 26.5 miniF2F; 13.8 ProofNet; 21.1% to 1.4% proof-check errors.
- COPRA Table 1: 13.52, 15.98, 24.59, 26.63, 29.09, 29.92, 30.74; GPT-3.5 9.02; CodeLlama 5.73; ReProver 25.00.
- DSP: human informal 42.6 valid / 39.3 test; Codex and Minerva-8B 40.6/35.3; 62B 43.9/37.7; 540B 42.6/38.9; ablations valid -4.9/-3.7/-9.8, test 36.5/34.0/30.3 (-2.8/-5.3/-9.0).
- Huang and Yang: 5/6 = 85.7% for three models; baselines 31.6/21.4/38.1; IMC 94.5% rank 3 vs 57.7% rank 92.
- AlphaProof table: 96.3/33.2/27.9 ... 99.6/58.3/56.1; main RL about 80,000 TPU-days; about 80M formal problems from about 1M informal.
- Goedel-Prover-V2: 88.1 to 90.4; Putnam 44 and 86 at pass@184. Baldur: 47.9% whole-proof vs 39.0% search baseline; 65.7% with Thor.

## Corrections made
1. DSP test-set ablations were misread in c05 (and its framing in c05 "bigger drafter was worse"). The 36.5/34.0/30.3 test numbers belong to the three ablations (no comments, no informal proofs, no automated provers), not to Minerva 8B/62B/540B. The Minerva test scores are 35.3 (8B, same as Codex), 37.7 (62B), 38.9 (540B). Bigger drafters were not worse. a09 had this right; c05 is wrong. Claim K08 uses the correct values.
2. GPT-f value function: a02 and c01 say policy+value 47.21% vs policy-only 42.56%. The 42.56% is iteration 0. The fair comparison at iteration 2 is 47.21% vs 43.15% (+4.06), not +4.6.
3. GPT-f table puzzle: Table 12 (attempts curve) shows a=2 at 42.90%, below the Table 9 value 47.21% for the same model, so the two tables use different search settings; c01 labelled 47.21 as "a=1". Not resolved.
4. DeepSeek-Prover-V1.5: a13 gave 63.5% as "RMaxTS" and 60.2% as "single pass" without budget. In the paper 60.2% single-pass is at 32x6400 samples (about 200k), RMaxTS 62.7% (63.5% best mix); 51.6% is at 128 samples. Search gain is 2.5 to 3.3 points at matched budget. a13 text "128 samples 51.6% (rows 46.1, 50.0...)" is jumbled; use the Table 1 values.
5. COPRA: b14/c14 list 29.92% as COPRA headline and a11 lists 29.09% as pass@1 headline. Table 1: 29.09 is with retrieval, 29.92 adds informal proof, 26.63 is the base system. c14 said ablation rows were not pinned; now pinned (24.59 without backtracking).
6. Thor: a08 gives 29.9 vs 29.6 "GPT-f expert iteration"; that 29.6 is the expert-iteration baseline test score (33.6 valid). Fine, but 33.6 was the GPT-f valid score, easy to confuse with a PACT 33.6 in a04.
7. DSP baselines in a09: Sledgehammer test 10.4, with heuristics 20.9 (valid 9.9 and 18.0); b06 uses "baseline 20.9%" which is the stronger baseline, so "doubling" is relative to Sledgehammer plus heuristics.

## Contradictions between sources
- Search vs sampling: DeepSeek-Prover-V1.5 says search adds about 2.5 to 3.3 points; BFS-Prover and Goedel get strong results with simple search or none; HTPS and AlphaProof claim large search gains. No paired equal-compute experiment exists across these.
- Refinement vs resampling: Seed-Prover says refinement saves a large budget (pass@8192 equivalent on one IMO problem); Goedel-V2 gain is confounded by 40k vs 30k tokens.
- Verifier: Huang and Yang rely on an LLM verifier; every formal paper relies on an exact checker. Only the second gives a guarantee.

## Weak spots
- Almost every result is on miniF2F (244 test items, so one point is about 2.4 items). Many ablation gaps under 1 point are noise.
- Compute differs by orders of magnitude (1 GPU 5 days to 500 TPU-days). Cross-paper comparisons mix pass@1, cumulative, and different time caps.
- Contamination of GPT-4 and DeepSeek on miniF2F is plausible but unmeasured.
- Only COPRA tests a training-free LLM scaffold in a formal setting; Huang and Yang test it informally. Nothing found that compares scaffolds at equal tokens against best-of-N in a formal prover.
- HTPS "cumulative" Metamath valid 82.6% includes training on valid statements.

## Seen only in snippets or not opened
- Seed-Prover numbers (99.6, 331/657, 78.1%), BFS-Prover, STP, Kimina, PutnamBench counts, Lean Copilot, LEGO-Prover, Lean-STaR were taken from earlier agents, not re-checked by me. c20 explicitly not opened.
- Gold-IMO 2025 claims from other labs were not covered.

## GAPS
1. At equal total tokens, does a frozen general LLM with a code-owned propose-check-backtrack loop beat plain best-of-N on formal or checkable proofs? (Only COPRA, one benchmark, GPT-4; no best-of-N at matched tokens.)
2. How much of the COPRA and Seed-Prover refinement gain survives when the budget is matched against resampling (feedback-conditioned retry vs fresh sample)?
3. How often does an LLM verifier (Huang and Yang style) pass a wrong proof or reject a right one? Needed to decide if an LLM verifier is acceptable at all under G2.
4. Does a code-computed state score (open goals, proof length) rank partial proofs as well as the learned value function of GPT-f and HTPS, with no training?
5. What is the minimum raw base-model pass rate for a scaffold to help (COPRA: GPT-3.5 and CodeLlama gain little)? Does this hold for current frontier models?
6. Does subgoal decomposition into verified lemmas help a frozen model at equal tokens, independent of training (DeepSeek-Prover-V2 and Seed-Prover both train)?
7. How strong is contamination on miniF2F and PutnamBench for current frontier LLMs, and what held-out split should our tests use (LeanDojo novel_premises analogue for non-formal tasks)?
8. Do these results transfer outside formal math (informal reasoning, planning) where the checker is weak or absent? Only Huang and Yang address this.
9. Is the Thor-style learned "when to call the solver" decision necessary, or does a fixed code rule (always try the solver first) get the same gain?
10. Does the DSP result (model-written informal draft equals human draft) replicate with current LLMs and on Lean?


## Gap search results

Sources opened this session (full text unless noted): Hilbert 2509.22819, DeepSeek-Prover-V2 2504.21801, LEGO-Prover 2310.00656, PutnamBench 2407.11214, Seed-Prover 2507.23726, Mahdavi et al. 2511.13027, QEDBench 2602.20629, Naik et al. 2604.02450, Thor 2205.10893 (re-read), BFS-Prover 2502.03438, DSP+ 2506.11487, Yousefzadeh and Cao 2507.04719; NeurIPS 2026 abstract page for the repair-vs-retry paper. Search-snippet only (opened:false): Pythagoras-Prover decontamination, tree-search-vs-best-of-N snippets. Evidence is in evidence_d.jsonl (d01 to d19). The arXiv, Semantic Scholar and OpenAlex APIs were rate limited, so papers were fetched by direct PDF link.

Status per gap:
1. OPEN. No paper runs a propose-check-backtrack loop against best-of-N at equal tokens in Lean. Hilbert compares to pass@4 and to call counts, DSP+ to token counts read from other papers. Outside formal proof the matched-token result is mixed (snippets only, d19).
2. PARTLY CLOSED, against the optimistic view. Seed-Prover gives no matched ablation (d06). A 2026 controlled study finds no feedback condition beats instruction-only resampling and that showing the failed proof lowers success by anchoring (d07; abstract only, 11 problems, no rates). Claim K17 stays contested. Design hint: pass the diagnostic, not the failed text.
3. CLOSED enough for a decision. LLM judges are lenient: false-pass 38.0% to 74.8% (QEDBench), 7 of 48 flawed USAMO proofs passed by GPT-5 even with a reference solution and 5 votes, olympiad balanced accuracy 77 to 88%, prompt sensitivity up to 27 points. New claim K25: an LLM verifier cannot be the final gate under G2. Caveat: no paper reports a clean false-pass rate on olympiad proofs for the Huang and Yang verifier itself.
4. MOSTLY OPEN. BFS-Prover shows a no-value-head search is competitive (length-normalised model log-prob, 70.83%), but that score is model-derived. No head-to-head of a code-computed state score (open goals, size) against a learned value head was found.
5. PARTLY CLOSED. Hilbert PutnamBench one attempt: 55.9% (Gemini 2.5 Pro) vs 13.3% (gpt-oss-120b) with the same loop; the loop lifts weaker planners to 90%+ on miniF2F. The floor is not isolated and no frontier re-run of COPRA was found. K09 rewritten.
6. PARTLY CLOSED. Frozen-model decomposition works: LEGO-Prover on GPT-3.5 (library +3.3 points), Hilbert (D=0 about 75% to D=2 98.36%). Still not equal tokens. K16 extended, K28 and K29 added.
7. OPEN. No measurement of miniF2F or PutnamBench contamination for frontier LLMs was found; only warnings, construction arguments and benchmark errors (8 mis-formalised statements in DSP+, 97% vs 67% autoformalisation). K27 added.
8. OPEN. Only the informal-math verifier papers (Huang and Yang, Mahdavi, QEDBench) speak to weak-checker domains; planning and other tasks not covered here.
9. OPEN. Thor's baseline is a union of independent runs (48.8% vs 57.0%), not a fixed solver-first rule. The cheap rule is untested.
10. CLOSED. DSP+ replicates DSP in Lean 4 without training (miniF2F-test 79.5% at 1024 attempts); model drafts match or beat human drafts, and with a strong prover the draft adds only about 0 to 4 points. K08 upgraded to established, K26 added.

Corrections noted while reading: Hilbert's text says Pro beats Flash by 3-4 points while its table shows 1.7 to 4.5; Naik et al. use 'false negative' in a way that conflicts with their own definition; the LEGO-Prover ablation table label order (47.1 vs 50.4) is clear only from the text.
