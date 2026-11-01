# C06.10 Counterexample finding: cross-check critique

## Numbers re-opened and checked (PDF text this session)
1. REFUTE (arXiv 2502.19414): ratings and solve rates confirmed (R1 2029 / 44.0, o3-mini high 2130 / 48.7). RandSearch 4.0 / 3.7 / 4.0 / 8.3 confirmed. 35 percent invalid confirmed. Correction: abstract says "< 9 percent", but Table 1 has an o3-mini cell of 9.3. Quote as "about 9 percent at best".
2. CounterMath (2502.10454): 1,216 samples, 1,025 filtered training samples, F1 59.0 / 60.1 / 58.9 / 80.7 / 64.8 / 77.0 (GPT-4o, o1-preview, Qwen-max, R1, Claude 3.7, Gemini 2.5 Pro) confirmed by table row order. MATH 80.5 to 87.9 and AIME 20 to 30 confirmed; AIME 2024 has 30 problems, so +10 points is 3 problems.
3. TestCase-Eval (2506.12278): Qwen3-32B 43.8, GPT-4.1 36.5, GPT-4o 31.7, human 93.3, cov@20 95.7 confirmed.
4. WILT (2410.10998): Claude 3.5 Sonnet 14/50, o1-mini 13/50 and 19/50 with 4o tests confirmed.
5. Wagner (2021, arXiv 2104.14516; NOT 2111.00702): n=19, value 5.16 < 5.24, 190 vertices threshold, 203-vertex graph confirmed.
6. PatternBoost (2411.00566): 81 edges for d=6 vs 82 confirmed.
7. Reynolds et al. 2013: 793 problems, 723 / 664 / 617 / 309 confirmed.
8. Jhaveri et al. 2026 (2604.02485): "6% to 78%", "45 turns", "42% to 56%" confirmed in text; per-model tables not re-checked.
9. Tyen et al. 2024: CORRECTION. 52.87 is GPT-4 overall step-level accuracy; 40.67 for logical deduction is the DIRECT TRACE column (step-level is 67.67). Entry b18 mixed columns. Backtracking range +18.04 to +43.92 confirmed, but the same table shows losses on already-correct traces (about -0 to -11 points).
10. Huang et al. 2024: CORRECTION. In b19, "Oracle: GPT-3.5 GSM8K 75.9 to 95.5" is wrong. Oracle gives 75.9 to 84.3 for GPT-3.5; 95.5 is GPT-4 standard prompting (oracle 97.5). The "after two rounds" label also needs care: 74.7 is round 2 (5 calls). 75.8 to 41.8 on CommonSenseQA confirmed.
11. McCune Mace4 manual and the Nitpick guide: lines were read by agents a, b, c with agreement (start size 2, 1 to 10 scopes, 30 s); not re-opened by me.

## Other corrections
- b21 (CriticGPT) is credited to "Trebacz et al."; the arXiv record (2407.00215) lists McAleese et al. as first author, as in c27. Use McAleese.
- The same paper often appears under three ids (REFUTE: a20/a21/b01-b05/c01-c04; CounterMath: a22/a23/b12/b13/c07-c09; WILT: b10/b11/c13/c14; Jhaveri: b06-b09/c10-c12). These are NOT independent. Claims counted distinct papers only, so many claims came out "single-source" even where three agents agree.

## Contradictions and tensions
- Self-correction: Huang (no gain without feedback) vs Tyen and CriticGPT (models can fix once located, and critics help). These agree once the failure is located as the weak link: locating is hard, fixing is easy.
- Positive-test strategy: Wason and Nickerson call it a bias; Klayman and Ha say it is often rational; Evans says the cause is not thinking of falsifiers. Unresolved; the LLM result (more incompatible tests, more success) supports the first view only for the Wason rule family.
- Thinking mode raises success without raising incompatible-test share (Jhaveri), yet incompatible-test share predicts success. Both can hold; the mechanism is not isolated.
- CounterMath fine-tuning: the in-domain gain is tiny, the out-of-distribution gain large; the scrambled table labels make the OOD rows uncertain (c09 itself notes this).

## Weak spots
- Not opened by anyone: McCune 1994 MACE, Paradox (a05), Kodkod (a11), QuickCheck (a12), Lakatos (a13 from memory), Blanchette and Nipkow 2010 Nitpick (c18). The "founding studies with exact numbers" for Mace/Paradox/Nitpick are missing; only manuals exist. No timing or success-rate figures for Mace4 versus provers.
- a24-a28 (2026 Lean disprove, OpenConjecture, INSPIRE) were not re-opened by me.
- Little evidence on counterexample FALSE ALARMS (invalid counterexamples are counted in REFUTE only), and none on the cost of a wasted S7 test.
- No study compares tool-assisted (Mace4/Nitpick/SMT) LLM refutation with unaided LLM refutation.
- Everything LLM-side is on code or toy rules; math-statement and open-ended-claim counterexamples are covered only by CounterMath and OpenConjecture.

## GAPS
1. Does giving an LLM a finite-model finder (Mace4, Nitpick, SMT model output) raise refutation rate over unaided reasoning, at equal tokens? No study found.
2. How often are counterexamples an LLM claims invalid (wrong hypotheses, arithmetic slips), and does an exact external checker remove them? Only REFUTE (35 percent) and AlphaEvolve cheating give data.
3. Does a Think-in-Opposites style instruction (Jhaveri) transfer from Wason rules to real claim testing (code, math statements) and does it still help at equal tokens versus plain thinking?
4. Is test design the bottleneck or the update after the test? WILT cross-model test suggests design; is that replicated with other models and with a single model split into two calls?
5. What is the union gain of several falsification strategies (random search, boundary cases, small-model search, opposite test) versus the best single one at equal tokens?
6. Founding numbers: how well did MACE, Paradox and Mace4 do against provers on counterexample problems (TPTP satisfiable problems, CASC model-finding track results)? Needs the CASC reports.
7. When a counterexample is found, how well do models repair the claim (Lakatos-style) versus simply discard it, and does repair improve downstream answers?
8. Do trained critics or verifiers transfer to refuting plausible-but-wrong natural-language reasoning (not code)? Link to Tyen (location) and CriticGPT.
9. Are the CounterMath out-of-distribution gains real (AIME 30 problems) or noise? Need a replication with confidence intervals.
10. What fraction of OpenConjecture-style counterexamples survive expert review as non-trivial, and does a "check intended hypotheses" step raise that fraction?

## Gap search results (evidence_d.jsonl, d01 to d16)
Search note: WebSearch quota ran out after two calls; arXiv search pages were then rate limited (429) and OpenAlex and Semantic Scholar were exhausted. So gaps 3, 4, 7 and the CASC part of 6 got no new sources. Nothing was searched around that limit.

CLOSED
- Gap 6 (founding numbers), mostly. Nitpick (d01, d02): 3200 mutants, 10 s, genuine counterexamples on most theories; 293 of 2729 TPTP formulas vs Refute 214; found 3 prover bugs. Paradox vs Mace4 (d03, d04): TPTP 3.1.1, 300 s, 1251 satisfiable problems, Paradox 1083, Mace4 802, FM-Darwin 1074. TPTP 5.4.0: Paradox 1450, CVC4 1277, Z3 941. Still not opened: McCune 1994 MACE paper and the CASC model-finding track tables (the "CASC against provers" part).
- Gap 9 (CounterMath out-of-distribution gains), in the negative. INSPIRE (d12) finds AIME 2024 unchanged for 2 of 3 models, +6.67 (2 problems) for one, MATH500 +0.6 to +1.8, all single runs without confidence intervals. The earlier AIME +10 is probably noise. Claim K10 stays "contested" and K31 added. Formal route confirmed from the primary paper (d11: 127 to 222 of 1,058 pass@1, rejected from ICLR 2026).
- Gap 2 (invalid counterexamples), partly. SymCE (d05 to d07): an exact verifier checking all hypotheses plus negated conclusion works as reward, residual verifier error 2.3 percent (4 of 177). Counterexample-only SFT drives true-theorem recognition 0.27 to 0.00 (invalid witnesses, mostly an unnegated conclusion). ARBITER (d08, d09): legality plus checker failure is the success criterion. Still no measure of invalid-claim rate for an unaided frontier model at inference.

PARTLY ANSWERED
- Gap 8 (trained critics): code only. ARBITER 40.61 to 62.67 percent hack success, TCS 28.56 to 43.01 selection gain (d08, d09, d15). No study found on natural-language reasoning refutation. Stays open for that domain.
- Gap 5 (union of strategies): d13 shows complementary wins between LLM semantic search and numeric optimizers (14 of 21 specs vs complete failures on others); d14 shows a random property generator equals an adaptive LLM tester (-0.024, CI [-0.097,+0.043]). No equal-token union measurement. Stays open.
- Gap 1 (model finder plus LLM): no direct study. d16 (Logic-LM) is the nearest: solver offload helps when translation succeeds (GPT-4 ProofWriter +11.5 over CoT) and hurts otherwise (PrOntoQA 83.20 vs CoT 98.79). Stays open.
- Gap 10 (OpenConjecture survival): d10 gives about 60 percent off-the-shelf, trivial cases, same-model review only. No expert review, no test of a hypothesis-check step. Stays open.
- Gap 4 (design vs update): d14 shows tester source access added nothing (-0.005); not a WILT replication. Stays open.

STILL OPEN, NO NEW EVIDENCE
- Gap 3 (Think-in-Opposites transfer to code or math claims).
- Gap 7 (Lakatos-style repair after refutation; only the ARBITER diagnosis-to-repair signal in d09, code only).

New claims K29 to K36 added; K03, K10, K16, K17, K18, K22, K23, K26 extended with d-evidence. Corrected numbers from above (Huang, Tyen, REFUTE, CriticGPT) were not changed by this pass.
