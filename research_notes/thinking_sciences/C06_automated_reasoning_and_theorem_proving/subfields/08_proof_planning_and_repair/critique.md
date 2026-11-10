# Critique and cross-check: C06.08 Proof planning and repair

Sources re-opened this session (pdftotext of arXiv PDFs, deleted after): Baldur 2303.04910, PALM 2409.14274, Lyra 2309.15806, Goedel-Prover-V2 2508.03613, Cobblestone 2410.19940, APOLLO 2505.05758, ProofAug 2501.18310, DSP 2210.12283, Huang et al. 2310.01798.

## Corrections made (to the evidence files; the files themselves were not edited, apply these when reading)
1. b05: "Thor alone 58.0%" is wrong. Baldur abstract/intro: Thor alone 57.0%; 58.0% is the ensemble of 10 Baldur models. (c01 had it right.) Baldur+Thor 65.7% confirmed.
2. a12: "Variant without CoqHammer: 702 (6.5%)" is wrong. The 702 (6.5%) variant is PALM without backtracking (paper: "outperforms by 523.5%", Finding 4). b08/c05 are right.
3. b20: "With oracle: GPT-3.5 GSM8K 75.9 to 95.5" is wrong. Oracle GPT-3.5 GSM8K is 84.3; 95.5 is GPT-4 standard (GPT-4 oracle 97.5). c16 is right.
4. c16 says "3 calls / 5 calls" for the intrinsic rows. In Huang's table these are call counts of the pipeline (rounds 1 and 2): GPT-3.5 GSM8K 75.1 and 74.7, CommonSenseQA 38.1 and 41.8, HotpotQA 25.0 and 25.0. The GSM8K drop for GPT-3.5 is only about 1 point; the big collapse (75.8 to 38.1) is on CommonSenseQA and is partly a prompt effect (the review prompt pushes switching). Do not quote the 38.1 as a general rate.
5. c11: "Beats PALM 15x by 8%, 9% and 2% on three datasets" - the three datasets are Wigderson100, PnVRocqLib100 and BB5100, not CoqGym100. On CoqGym100 Cobblestone does not clearly beat token-matched PALM. Also c11 and a18 mix cost figures: abstract $1.25 and 14.7 min is the average; $1.46 and 15.32 min is CoqGym100.
6. b03/c03 vs c01: the Baldur "+1.5%" in the abstract is the cost-matched repair gain; "+266 theorems, 4.2%" is the unmatched generate-then-repair (two samples vs one). a09 reports the 4.2% without saying it is not cost-matched. Use +1.5 (matched) not 4.2.
7. Lyra: the "DSP" baseline matters. Original DSP is 39.3% test (Codex, 100 attempts). Lyra's own GPT-4 re-run without corrections is 39.7% (100) and 42.6% (200). So the clean gain from corrections at 200 attempts is 42.6 to 51.2 = +8.6 on test (valid 50.4 to 55.3 = +4.9), not the +11.9/+12.7 headline vs Codex DSP, which also swaps the formaliser. a16 and b11 are right on the raw numbers but the headline mixes two changes.
8. PALM dataset size is given as 10,842 (a-file), 10,826 (c04), "more than 10K" (paper text); 4,377/40.4% implies about 10,834. Unresolved; the paper text confirmed only "more than 10K" and 27 projects.
9. Confirmed unchanged: Baldur 34.8/40.7 (16/64 samples), context 47.5, 62B 47.9, 24.9/26.2/25.4 cost-matched rows; PALM 40.4 vs 14.4/17.1/22.9, 49.6% taxonomy (520 errors, 579 theorems); Goedel-V2 88.1 to 90.4, 43 to 57, 92.7 vs 92.2 (the 92.7 is with extended context and more rounds, 5 per b15); Cobblestone 48/38, 59.3K vs 99.3K, 43% fail-safe; APOLLO 64.7 to 65.6 at 362 samples, 57.6/60.7/63.5/65.6, o3-mini 3.3 to 40.2; ProofAug "<0.2% advantage" over naive retry and 52.5%; DSP 20.9 to 39.3 and ablation drops 4.9/2.8, 3.7/5.3, 9.8/9.0, and larger Minerva = lower test (36.5, 34.0, 30.3).

## Contradictions and tensions
- Intrinsic self-correction fails (Huang) vs revise-with-checker-error works (Baldur, Goedel, Seed-Prover). Consistent once "external verifier signal" is the dividing line; Baldur's no-error-message arm is the within-paper test.
- RMaxTS tree search (+2.5 on miniF2F) vs ProofAug claim of under 0.2% over naive retry: the latter is a rival's claim, not independently run.
- Bigger informal planner not better in DSP (540B worse than 8B on test) vs Hilbert (stronger planner helps 3-4 points). Different benchmarks, different pipelines.
- Cobblestone vs PALM: efficiency claim depends on the 15x PALM repeat used to match tokens; a different matching would change the verdict.

## Weak spots
- Almost all LLM evidence is miniF2F, PISA, CoqGym, PutnamBench: possible contamination, saturated (miniF2F 99%). Only Cobblestone controls for leakage.
- Few results are token-matched. Seed-Prover, Hilbert, Aristotle, DeepSeek-Prover-V2 compare heavy pipelines to light baselines.
- The Edinburgh founding works (Bundy 1988, Ireland and Bundy 1996, Melis and Siekmann 1999) were not read in full (a03, a04, a24, c19, c20 unopened). a01/a02 read only the 1992 report. The claim that critics beat nqthm is a stated claim without counts.
- No source tests LLMs on repair after a library or specification change (the classic proof-repair task). c28 is empty.
- Pumpkin Pi evidence is case-study level (8 cases), not counted trials.
- Transfer to our agent: proof checkers give exact error text; open-domain reasoning rarely has such a verifier. Evidence supports "revise only with a checker", weak for plain reasoning.

## Only seen in snippets / not opened
a03, a04, a19 (abstract only), a23, a24, b25, b26, b27, c19, c20, c28. Seed-Prover, Hilbert, Aristotle, DeepSeek-Prover-V2, DeepSeek-Prover-V1.5, LEGO-Prover, COPRA, Rango numbers were not re-opened this pass (taken from the finders' reading).

## GAPS
1. Does error-message-guided revision beat resampling at equal tokens outside formal proofs (code with tests, math with a calculator, constraint puzzles)? Which checker signals carry over to our agent?
2. What is the marginal gain per repair round at equal tokens for modern reasoning models (not 2023 fine-tuned models), and where is the best stopping round?
3. Local repair (keep verified steps, redo only the failing subgoal) vs full regeneration at equal tokens, with a contamination-free benchmark: is Cobblestone's saving real beyond Coq?
4. How much of the large APOLLO/Goedel/o3-mini repair gains is only syntax/format fixing vs true reasoning repair?
5. Plan-level revision (rewrite the sketch) vs step-level revision: Lyra shows it needs a strong filler; is there independent replication?
6. Do LLMs repair proofs after specification or library change (Pumpkin Pi's task)? No study found; search PUMPKIN PATCH / Coq repair with LLM follow-ups 2024-2026.
7. Do Bundy-style critics (failure pattern to lemma/generalisation patch) help an LLM: any study that feeds rippling-style failure diagnoses into prompts, vs raw error text?
8. Read the Ireland and Bundy 1996 journal paper and Melis and Siekmann 1999 for the actual success counts of critics versus nqthm.
9. Does a stronger planner or a stronger executor matter more at equal tokens (Hilbert says planner; DSP size result says not always)?
10. How big is the contamination effect on miniF2F/PutnamBench repair gains (rerun on post-cutoff problems)?


## Gap search results

Evidence in evidence_d.jsonl (d01-d18). Search tools ran out during this pass (WebSearch budget spent, Semantic Scholar and OpenAlex rate-limited, arXiv search page 429 after two calls), so papers were reached through direct PDFs. Opened: Olausson 2023 (2306.09896), Self-Debug (2304.05128), CRITIC (2305.11738), Tyen 2023 (2311.08516), Kamoi survey (2406.01297), Fix Not Just Resample (2610.26942), CAPRI (2608.13459), Double-Tank (2608.18822), LAMP (2606.28841), P3 (2608.09277). The 2026 papers are very recent single-group preprints.

1. Error-guided revision vs resampling outside formal proofs: PARTLY CLOSED. Olausson (code, tests): repair beats resampling only sometimes (GPT-4 APPS 1.05x vs 0.97x depending on how budget is split). Self-Debug: the gain needs execution and drops without it (MBPP Codex 61.4 to 57.6). CRITIC: tools matter. Kamoi survey: no success with prompted self-feedback outside suited tasks. Signals that carry over: executable checks (tests, calculators, search, constraint checks) and a located failing step. Not tested: constraint puzzles, or maths with a calculator at equal tokens.
2. Marginal gain per round for modern reasoning models: STILL OPEN for reasoning models. Closed for small models: first repair gives 84-96% of the gain (Lean), one turn is typical (Self-Debug). No source tests o3-class or R1-class models round by round.
3. Local repair vs full regeneration, contamination-free: PARTLY CLOSED. Lean step-level repair beats sampling at matched wall-clock; P3 cuts full restarts from 17-28% to 5-12%. No contamination-controlled replication of Cobblestone.
4. Syntax/format vs real reasoning repair: PARTLY CLOSED. One repair recovers 6.2% of rejected tactics, mostly shallow classes; type mismatches 2%. The APOLLO/Goedel/o3-mini split is not measured; stays open.
5. Plan-level vs step-level revision, independent replication of Lyra: PARTLY CLOSED. Not a Lyra replication, but LAMP (no Planner: -11.1 points, hard 88.2 to 58.8) and P3 (joint plan +4.6 to +11.2) are independent plan-first evidence. Only 4 of 48 P3 failures were plan errors.
6. Repair after spec or library change: STILL OPEN. Nearest: CAPRI and Double-Tank (Isabelle drift, spec weakening), not library migration. No LLM follow-up to Pumpkin Pi found (search limited).
7. Bundy-style critics fed to an LLM: STILL OPEN (no search possible). Tyen shows a step location beats a rewrite, which supports the idea indirectly.
8. Ireland and Bundy 1996 and Melis and Siekmann 1999 counts: STILL OPEN. Publisher pages blocked; DOIs recorded.
9. Stronger planner vs stronger executor at equal tokens: PARTLY CLOSED. Olausson: a stronger critic helps weaker coders at all budgets; LAMP: backbone changes the result 88.9% vs 68.9%. No equal-token planner-vs-executor swap found.
10. Contamination effect on repair gains: STILL OPEN. No post-cutoff rerun found; the Lean and Isabelle results above are not contamination-controlled.

New claims K21-K25 added; K02, K04, K09, K10, K15, K19 extended with the new evidence ids.
