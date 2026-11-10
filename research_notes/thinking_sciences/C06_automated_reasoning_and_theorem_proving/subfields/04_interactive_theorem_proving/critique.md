# C06.04 Interactive theorem proving: cross-check

## Corrections (sources re-opened this session: miniF2F, DSP, Kimina, DeepSeek-Prover-V2, Seed-Prover, Baldur, PACT, Thor, Hilbert, PutnamBench)

Confirmed: PACT 32 to 48.4% (also 37.1%, 1043 proofs, 94% of refl lemmas; 45.6 and 43.3 temporal); Thor 39.0 to 57.0, Sledgehammer 25.7, 8.2% only-Thor, miniF2F 29.6 to 29.9; Baldur 65.7 vs Thor 58.0, 47.5 and 47.9 with context; Hilbert 99.2% miniF2F and 462/660 (70.0%) vs Seed-Prover 331/657 (50.4%); Seed-Prover 99.6%, 78.1%, 47/55, 47/56, 331 vs prior 86; PutnamBench counts (ReProver 0, COPRA 1, DSP 4, Sledgehammer 3, Tactician 0); miniF2F GPT-f Lean 24.6 pass@1 / 29.2 pass@8 test, Metamath 1.3 / 1.6.

Corrections:
1. a08 gives Lean GPT-f as "29/244 test, 43-44/244" and tidy 13/244. The paper text says 24.6% / 29.2% (valid 23.9/29.3) and tidy 1.3%. a08's counts are not in the paper. Use b06, drop a08.
2. c05 reports Sledgehammer test 20.9 and heuristics 35.2. The DSP table fits b08: Sledgehammer 9.9/10.4, heuristics 18.0/20.9, Thor 28.3/29.9, Thor+expert iteration 37.3/35.2. Table extraction is garbled (rows interleave), so a residual doubt remains.
3. b19 attributes 52.94 / 68.85 / 77.87 / 80.74 to Kimina-Prover. In the DeepSeek-Prover-V2 comparison table these are DeepSeek's own rows (non-CoT 671B pass@1 52.94; CoT 7B 68.85 at 32, 77.87 at 1024; 671B 80.74 at 8192), while Kimina rows read 52.5 (distilled 72B pass@1), 63.1 (7B at 32), 70.8 (7B at 1024). The Kimina paper text itself quotes 52.94, 68.85 and 80.74 as its own and its table puts 77.87 at pass@32 while its text says 68.85 at pass@32. Unresolved. Safe fact: about 80.7% at pass@8192 for both.
4. c19 "ProverBench AIME 217/244" is wrong: 217/244 = 88.9% is the miniF2F-test overall pass rate. Fix c19.
5. c20 "4 of 6 within the contest": not found in opened text. Keep only 5 of 6 (abstract).
6. Baldur repair gain: a12 says about 1.5, b14 says +1.3. Use 1.3. Table rows are misaligned in extraction; the text confirms 34.8 (16 samples) and 40.7 (64).
7. a11 and b26 (Sledgehammer judgement day) disagree on goals (1240 vs 1200) and rate (about half vs 48%). Neither opened. Not used in claims.

## Contradictions between sources
- DSP Minerva column: a14 gives test 36.5/34.0/30.3; b09 gives 36.5/37.7/38.9 test and 40.6/43.9/42.6 valid. The table has both sets of figures; which is the ablation is unclear. K08 marked contested.
- HTPS miniF2F-valid 58.6% includes statements seen in training; not comparable to test numbers.
- Goedel-Prover 57.6% (V1, c17) vs 88.1% (V2, a21) are different model versions, not a conflict.
- Hilbert's gain (422%) is against the best public baseline and uses 16,384-attempt, proprietary-model runs.

## Weak spots
- Nearly every LLM-proof number is a lab self-report. PutnamBench is the one neutral check and it was measured in 2024, when scores were near zero.
- No user studies of humans using proof assistants with LLM help (Lean Copilot, LLMSTEP report none).
- Compute is rarely matched (pass@8192, search budgets, training data), so equal-token tests are our own design.
- Formal proofs are a closed, checkable domain. Transfer to open reasoning with no kernel is unmeasured here.
- Contamination: miniF2F and PutnamBench statements are public; only PACT and LeanDojo audit it.

## Seen only in snippets or not opened
a11, b26 (Sledgehammer judgement day); a24-a26 (our own syntheses); c23, c24 (cited secondhand); b23, b24 (abstract pages only, no coefficient).

## GAPS
1. Does verify-and-repair against a real checker beat independent sampling at equal total tokens, and by how much outside proofs (code with tests, algebra with a symbolic check)? Which papers report equal-compute comparisons?
2. How much do false verifications (checker loopholes, flawed autoformalized statements, sorry-like exits) inflate headline numbers of 2025 provers? Is there an output audit of Seed-Prover, Hilbert, DeepSeek-Prover-V2?
3. Resolve the Kimina vs DeepSeek-Prover-V2 pass@k clash by reading both tables and released results.
4. Is the DSP draft-then-formalize gain replicated independently, and does it hold with 2025 reasoning models as drafters?
5. What do user studies say about human efficiency with proof assistants plus LLM copilots (time, error rate, trust)?
6. How strong is contamination for miniF2F and PutnamBench-era provers? Are there results on post-cutoff problems (for example IMO 2025 formalised after release)?
7. Does lemma decomposition (Hilbert, Seed-Prover, DeepSeek-V2) keep its advantage when token budgets are matched to flat prompting?
8. What is the failure taxonomy of LLM proof attempts (Lu et al.: 49.6% wrong theorem application) and which categories can a scaffold fix without training?
9. Do retrieval and premise-selection gains (LeanDojo, Rango) transfer to retrieving prior solved problems as memory for a non-formal agent?

## Gap search results (evidence_d.jsonl, d01-d20; claims K18-K25 added, K04/K07/K10/K13/K17 changed)

Search note: the WebSearch budget ran out after 1 useful call, and the arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429. Papers were found by known arXiv ids and read as full PDFs. Gaps 5 and 6 are limited by this.

1. Repair vs resampling at equal tokens: PARTLY CLOSED. Outside proofs, Olausson et al. (code with unit tests) find about no gain: 1.05x and 0.97x of pass@20 / pass@22 for GPT-4 on APPS; budget is best spent on diverse first attempts (d04). Feedback quality is the limit (33.3 to 52.6 with expert human feedback, d05). Inside proofs, COPRA beats 60 independent samples (26.63 vs 15.98, d14) and Goedel-V2 pass@32 with 5 revisions (92.7) beats pass@8192 without (92.2), about 2% of the tokens by our arithmetic (d06). No equal-compute study for algebra with a symbolic check was found. K04 now "contested".
2. False verifications: PARTLY CLOSED. Faults in Our Formal Benchmarking (d08, d09) audited 13 benchmark variants: 398 certified faulty items, and an apply? bug passed 3 DeepSeek-Prover-V2 7B proofs with a hidden sorry. No output audit of Seed-Prover or Hilbert exists; no headline score was recomputed. Defects deflate and inflate (d09, d10: 31.8% of ProofNet Lean 4 ports flawed). A Lean kernel bug in July 2026 is only a search snippet (d20, unopened).
3. Kimina vs DeepSeek clash: CLOSED (d01, d02). The four numbers are Kimina-Prover Preview 72B; DeepSeek V2-671B is 61.9 / 82.4 / 86.6 / 88.9.
4. DSP replication: PARTLY CLOSED. Lyra (d13), another group, got 38.9 (GPT-4 drafts) and 39.7 (human) at 100 attempts, matching DSP's 38.9 / 39.3. COPRA shows informal proofs add only +0.83 over retrieval (d14). Not tested: 2025 reasoning models as drafters; Hilbert (d11) hints the reasoner matters a lot (13.3 vs 70.0 on PutnamBench).
5. User studies of LLM copilots: OPEN. Only an expert-telemetry study without LLM help (N=8, d19) was found.
6. Contamination: PARTLY OPEN. Informal Putnam variations drop o1-preview 19.6 points (d18); Rango's edge over Tactician falls to 30.1 vs 28.3 post-cutoff (d16); Seed-Prover reports 81.8 on MiniCTX-v2 written after Nov 2024 (d07) and formalised IMO 2025 at the contest with human experts (4/6 in time, 5/6 later). No Lean-prover variant test; no independent re-run on IMO 2025.
7. Decomposition at matched tokens: PARTLY OPEN. DeepSeek V2 CoT pass@32 (about 216k tokens, 82.4) beats non-CoT pass@1024 (about 780k tokens, 76.7), our arithmetic (d03), but modes are not a clean ablation. Hilbert D=0 pass@4 75 vs D=3 98.7 is not token matched (d11).
8. Failure taxonomy: CLOSED for Coq/GPT-3.5 (d15): 49.6% wrong theorem application; backtracking lifts 6.5 to 40.4; retrieval and rule repair add 3-7 percent each. Single paper, old model; not retested on 2025 models.
9. Retrieval transfer: PARTLY CLOSED in formal domains (d12, d16, d17: +47% proof retrieval, +3.3 skill library, tokens 4.0M to 2.3M). Transfer to non-formal memory is untested; only the verified-item rule carries over.

Still open: gap 5 (user studies), equal-token decomposition, 2025-model drafters, output audits of Seed-Prover and Hilbert, algebra-with-symbolic-check repair at equal compute.
Corrections to earlier notes: K10/b19 should not attribute 52.94-80.74 to DeepSeek; d11 corrects Hilbert's reasoner dependence (gpt-oss-120b 88/660).
