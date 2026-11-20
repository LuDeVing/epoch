# Critique: C06.09 Autoformalisation (cross-check)

## Corrections made (sources re-opened as PDF text this session)
Re-checked: ProofNet (2302.12433), Herald (2410.10878), Goedel-Prover (2502.07640), Poiroux (2406.07222), Wu 2022 (2205.12615), FormalMATH (2505.02735), CriticLean (2507.06181), DTV (2403.18120), MMA (2311.03755).
1. **a09 and c07 are wrong.** They say few-shot Codex gets 13.4% accuracy and 23.7% typecheck on ProofNet. Table 3 shows plain few-shot Codex typecheck 4.3%, BLEU 4.7, accuracy 0. The 23.7 / 25.1 / 13.4 row is prompt retrieval. b05, b07 are right. Use b05. a10 and c08 (retrieval 45.2% typecheck, 16.1% accuracy, via distilled back-translation) match the table. Note the table rows are garbled in text; the 45.2/14.8/16.1 row is "Dist. backtrans." on Codex. a10 labels it "prompt retrieval with Codex"; it is distilled back-translation.
2. **Herald numbers (a25, b16, c19) differ by version.** Abstract: 93.2% Pass@128, baselines 74.0 / 50.1. Body: 96.7% miniF2F-test, baselines 73.0 / 55.0 (table shows 73.0 and 50.1 for the same rows in different places). The 93.2% row in the ablation is the 580k data point; 96.7% is the 1160k point. Treat 93.2 to 96.7 as the range and cite the version.
3. **Goedel-Prover author is Lin et al., not Li** (a18 wrong, c20 right). Formalizer numbers in c20 confirmed (CC 76.74 to 88.48; FC 48.06 to 80.42; CC+FC 45.72 to 76.41); a18 ablation row confirmed.
4. **FormalAlign authorship** is given as Lu (a13, c23) and Ye (b23). Not resolved; check the paper header. FormL4 (a12) is Lu et al.
5. Confirmed with no change: Wu 25.3% (38/150) and 76% (29 of 36 coherent, quoted against 38); under 0.18% Isabelle data; Poiroux 31.8% (118 of 371), BEq+ P/R/F1 98.0/48.3/64.7, correlations 0.655 vs 0.974, 62.5 vs 29.6 recall short vs long, 4.11 to 40.54 pass@n, RLM25 context 20.64/24.56; FormalMATH 72.09%, 16.46%, 92.4 to 32.7; CriticLean 38/54/84 and 12.6 to 52.8; DTV 61.5 / 65.0 / 68.2; MMA 16-18%, 36/30 compile.

## Contradictions
- LINC vs Logic-LM: symbolic translation beats CoT on ProofWriter but loses on FOLIO (GPT-4) and PrOntoQA (Logic-LM 83.2 vs CoT 98.79). Claim K10 stated as mixed.
- Symbolic-equivalence selection: Li 2024 reports gains; Poiroux finds it no better than Self-BLEU or majority vote (K04 contested).
- Compiler feedback: helps GPT-4o, hurts DeepSeekMath-7B (a24); accuracy stalls in Logic-LM while executability climbs.
- Pretraining on formal data: Lean Workbook / MMA fine-tunes did not beat the base model on RLM25 (b12), yet Herald and Goedel gain from them on in-distribution sets.

## Weak spots
- Almost all human-graded accuracies use small samples (N=38, 50, 80, 100, 150). No confidence intervals reported in most.
- Metrics are not comparable across papers (typecheck, BLEU, human-perfect, BEq+, pass@k).
- Benchmarks are contaminated or saturated (miniF2F); ProofNet itself had 31.8% errors, so older ProofNet numbers (a09, b05) are measured against faulty references.
- Many 2025 results (ATLAS, Herald, Goedel) are self-reported by the model authors.
- No study here tests a general reasoning scaffold doing formalisation at equal tokens; our agent_tests are untested proposals.

## Only seen in snippets or not read
- a27 (Wang 2018), a28 (Szegedy 2020): not read. a29 and b31/c34 survey: abstract/intro only. b28 SatLM first pass: numbers not extracted (c27 has them). c12 table was garbled; row mapping uncertain. a21/c24 table rows read from garbled text.
- ATLAS, nl2spec, Clover, Lyra, Symbolic-CoT (c22, c30-c33) were not re-opened by me.

## GAPS
1. Does a round-trip check (formalise, informalise, compare) detect wrong formalisations better than type-check? No source measured it against human labels.
2. How well does a semantic LLM critic agree with expert humans on faithfulness (FormalAlign 65% vs human 79.6%, kappa 0.49)? What does a stronger 2026 judge reach?
3. At equal tokens, is sampling plus selection better than iterative critic-based repair? Sources test each separately.
4. How much does surrounding context (definitions, blueprint) help, beyond RLM25's single study, and does retrieval from a memory of past formalisations transfer?
5. Which failure type dominates for current frontier models (2025-2026): definition misalignment, missing assumptions, or silent weakening? Wu's counts are from 2022 Codex.
6. Where does formalise-then-solve beat CoT outside logic puzzles (planning, constraints, code specs), and what routing rule detects it?
7. Are there failed replications of Wu's 25.3% with modern models on the same 150 MATH problems?
8. How much of benchmark gain is contamination (miniF2F near 97%)? Need results on fresh post-cutoff problems.
9. What is the cost per verified statement (FormalMATH 6.89 USD human) versus an automated pipeline at the same faithfulness?
10. Do autoformalised statements used as verifiers (DTV) still help on open-ended, non-math reasoning?

## Gap search results (evidence_d.jsonl, d01-d21; claims K21-K29 added)
Search note: WebSearch budget was exhausted by other agents; arXiv, OpenAlex and Semantic Scholar APIs were rate limited. Papers were found through the Semantic Scholar citation list of Wu 2022 and direct arXiv PDF fetches. Several 2026 papers use model names (GPT-5.2, Claude Opus 5.5) as printed in the papers. d16, d17 and d18 were abstract-only (opened false).

1. **Round trip vs type-check: PARTLY CLOSED.** Mathesis (d01) measured re-informalisation against human labels: precision 93, recall 50, F1 0.65, worse than an LLM judge (F1 0.85) and a staged scorer (0.92). Clover (d02) had 0 false accepts on 240 adversarial code variants. The statutory round-trip paper (d03) validates only against NLI. No direct round-trip vs type-check comparison on maths statements exists. Subset size in d01 unknown.
2. **LLM critic vs expert humans: CLOSED for 2026 judges, with caveats.** Cross-family two-judge plus compile reaches 91.5% (54/59) human-majority agreement (d04); SA-PASS 98.8% (d06); LeanScorer F1 0.92 (d01). Human reviewers themselves have low kappa (0.18-0.28) and pairwise agreement about 69-70% (d04, d07). K18 changed to contested. Samples are small.
3. **Equal-tokens sampling vs repair: OPEN (partly informed).** At equal LLM calls the methods tie on statements (d05); feedback beats resampling at matched queries for proofs (d14). No study matches tokens.
4. **Context and memory: PARTLY CLOSED.** Three more studies support context (miniCTX d10, DDR d11, LLM+P d12); boundary from Verina (d14). Retrieval from a memory of past formalisations transferring: no study found.
5. **Dominant frontier failure type: PARTLY CLOSED.** 2026 data show type and library errors dominate for a frontier model; semantic-only errors are a minority but real (d05, d09, d08). K05 changed to contested. A clean taxonomy of silent weakening by frontier model was not found.
6. **Where formalise-then-solve beats CoT: PARTLY CLOSED.** Wins on planning with a solver and example (d12), code specs (d15, d02). Loses on constraint tasks for reasoning models (d13: 12 of 16). No routing rule found; hint: weak solver, rigid small problem, solver available.
7. **Failed replication of Wu 25.3%: OPEN.** No modern rerun on the same 150 MATH problems found.
8. **Contamination: OPEN.** Only indirect evidence (d19, d20). No fresh-problem autoformalization result found.
9. **Cost per verified statement: OPEN.** Only the human figure 6.89 USD (d21); Verina run costs (d14) are not matched to faithfulness.
10. **DTV-style verifiers on open-ended non-math: OPEN.** Nothing found; Semantic Scholar citation query for DTV was rate limited.

Corrections to earlier evidence: miniCTX table rows were garbled, so tuned-model figures follow paper text. CSP paper abstract says 15 of 24, body gives 12 of 16 plus 4 of 8.
