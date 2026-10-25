# Critique: Troubleshooting search strategies (cross-check)

## Sources re-opened this session (PDF text read)
Rasmussen and Jensen 1974 (a01-a07), Burroughs 1979 (a09-a11), Bertolazzi et al. 2023 (b15, b16), Hu et al. UoT (a24, b19, c03), Kim et al. 2026 RCA (b06-b08, c11), Cloud-OpsBench (b09, b10), AIOpsLab (b13, b14), BED-LLM (a25, a26, b20, b21, c08).

## Confirmed without change
- R&J 1974: 45 cases, 30 analysed, 6 men, 8 instruments, 22 analog + 8 digital; 31 functional, 82 topographic, 87 evaluations, 75 checks; 45/30/20 percent split of checks; 70 percent of 82 topographic searches inherit their field; about 40 percent succeed; failure follows 23/17/10 percent; "symptomatic" appears zero times in the paper.
- Burroughs: "about one-third as efficient as BETS"; 422 records, 71 percent first replacements wrong; half split 0 in the action matrix.
- Bertolazzi: optimal 3.50, baseline 4.00, ChatGPT 7.24 questions; constraint-seeking 57.14 vs 73.77 percent; 56.67 percent of games with questions after singleton, 29.29 percent unnecessary; 39.44 percent of second-turn questions EIG=0; stepwise prompt 6.4 questions, contradictory 13.50 to 8.42, spoiled 12.22 to 7.78.
- UoT: FloDial GPT-4 43.7 to 67.3 percent, 7.8 mean questions (text states it).
- Kim: 3.9 to 12.5 percent, 1,675 runs, 11.1 steps, 609.9 h, 1.38 B tokens, 71.2/63.9/39.9/27.2/18.6 percent, steps 11.9 to 9.2, tokens/step +24.8 percent.
- Cloud-OpsBench: GPT-5 JRA 0.68 on both, ECR 0.21 and 0.15, steps 5.56, Qwen3-8B 16.01 steps, RAR 0.46, EE 0.37.
- AIOpsLab: GPT-4 RCA 40.90 percent in 4.81 steps, ReAct 45.45, FLASH 36.36, GPT-3.5 9.09 in 14.00; localization top-1 61.54/53.85/46.15/30.77; FLASH 59.32 percent at 20 steps.
- BED-LLM: +37.4 percentage points; "more than double"; Split described as previous state of the art.

## Corrections
1. a09 (Burroughs): the table counts trials in which a heuristic was used, not exclusive choices. Anchoring and adjustment appears in 8 of 40 trials (20 percent), schematics 5, senses 4, in-to-out 1, half split 0. "Mostly anchoring" is therefore too strong. The 0 of 40 for half-split is solid. Still n=2 technicians, TV sets, coded by one researcher.
2. b06/c11 (Kim): the text says code-generation error ranges "1.8 percent for Gemini 2.5 Pro to 65.5 percent for Claude Sonnet 4", but Table 3 shows 1.8 percent in the Timestamp Error row for the last column and 40.0 percent for code generation there. The paper is internally inconsistent. Use only the overall 27.2 percent and the 65.5 percent maximum.
3. a26/b21 (BED-LLM): in 20 Questions the Entropy ablation is the strongest alternative, slightly better than Split, and BED-LLM beats both. The claim "entropy-only gives no gain over prompt-only" was NOT confirmed. The worked example (high marginal and conditional entropy, so no gain) is in the appendix for film preferences. Treat b21 as: entropy ≈ Split, both below full EIG; no-gain claim unverified.
4. a24/b19 (UoT): "+38.1 percent" is the paper's headline for success-rate improvement and is probably relative, while BED-LLM's 37.4 is in percentage points. Do not treat the two as the same unit. The GPT-4 troubleshooting gain is 23.6 points (about 54 percent relative). The baseline turns figure (13.4) comes from a garbled table row and is not cleanly confirmed.
5. b14: the "beyond 5 steps" quote applies to GPT-3.5 only, not all agents.
6. a02: the claim "functional search is the opening routine" is supported (21 of 30 protocols have exactly one functional search; 5 have none).

## Not re-verified
SDBench numbers (c20, c21) and Battleship numbers (c07): downloaded PDFs were damaged; kept as recorded, claims marked single-source. Also not reopened: Feldman 2010 (a20-a22), Simon and Kadane (OCR garbled), Venkatasubramanian, Siddiqi and Huang, Gonzalez-Sanchez, AR-Bench, HAProxy, FaulT-Bench, Time Travel.
Seen only in snippets or abstracts: a28, a29, b24, b25, b27, b28, b29, b30, b31, c22-c24 and Rouse 1987 (a27, progress report only).

## Contradictions between sources
- Instructors teach forward trace and split-half (b04), yet skilled technicians use almost none (a09, a04). Teaching is not practice.
- Greedy one-step is optimal or near optimal (a21, c01, b22) vs pathological cases and loss to random (b23, a23).
- Reasoning helps a lot in partly observable questioning (b17) vs no gain, 10x tokens in HAProxy isolation (c16) and little in AR-Bench (c10).
- EIG planners help (a24, a25, c07) vs AR-Bench finds UoT worse than zero-shot on open tasks (c10).
- "Topographic/functional/structural" mean different things in R&J 1974 (a02) and the 2003 review (a17).
- Knowledge instruction does not help new faults (b25) vs structured method training doubles solves (b27, unopened).

## Weak spots
- Almost every LLM test-selection result uses a simulated LLM answerer and a closed candidate list, not real instruments with noisy readings.
- Human data are tiny (R&J 6 men; Burroughs 2; Dounas-Frazer 8 pairs) and none measures half-split efficiency head to head. Goldbeck et al. 1957, the one direct test, was never found.
- RCA benchmarks measure telemetry reading, not test choice; step counts are confounded with model size.
- No source holds equal tokens across arms, so the efficiency claims do not transfer directly to our equal-token rule.

## GAPS
1. Does an LLM agent that chooses its own tests need more tests than a code half-split or greedy-gain selector on known-fault systems, counted at equal tokens? (No study found; core test.)
2. How much of the gain from code-side selection comes from the filter (drop zero-gain tests, stop at singleton) vs from the scoring rule?
3. How should the agent get test outcome likelihoods and reliabilities (needed for noise-aware gain), and how badly does a wrong table hurt vs random?
4. Where does the closed-candidate assumption break: how large and open can the fault list be before the scaffold stops helping (AR-Bench boundary)?
5. Do structured troubleshooting methods (Schaafstal 2000, Gugerty 2007, Goldbeck 1957) really beat untrained search; what are the effect sizes (all unopened)?
6. When to start with symptom matching (fast, known faults) and when with normal-reference search (novel or multiple faults); is there a measured switch rule? (Besnard 1999 expert error unopened.)
7. What is the right stop rule: sufficiency (singleton set), cost-benefit, or no-fault acceptance, and what does it do to the 11 to 24 percent false-fault rate?
8. Does cost-weighting (SDBench-style) transfer to tests priced in tokens and time rather than dollars, and does a cheap-observation-first rule hold?
9. Does a model-as-oracle verdict need verification at every split (bisect fragility), and what is the cheapest check?

## Gap search results (gap searcher, evidence_d.jsonl d01 to d17, claims K24 to K34)
Tool limits: WebSearch budget ran out, Semantic Scholar and OpenAlex were rate-limited, arXiv search returned 429, and the shared disk filled to 0 free. Direct PDF downloads still worked. Extracted text was deleted after reading.

Re-opened full text this session: ACTMED (2510.18988), ASIG (2607.03426), AR-Bench (2506.08295), FaulT-Bench (2608.27021), Time Travel (2511.18854), SDBench (2506.22405), Battleship (2510.20886), Besnard 1999. Schaafstal 2000: abstract page only.

- Gap 1 (LLM own test order vs half-split or greedy at equal tokens): OPEN. Closest are ACTMED (d01, accuracy at a fixed 3 tests) and Battleship (d13). Neither counts tests to solve at equal tokens. ASIG (d03) shows code-side BED costs 25 to 36 times the inference time, so equal tokens is a real constraint. K23 stays single-source.
- Gap 2 (filter vs scoring): PARTLY CLOSED. Battleship: question scoring alone gave +0.021 to +0.026 F1, while using answers by Bayesian move choice gave about +0.4 F1 for weak models (K25). The zero-gain filter cut redundant questions to near 0 (K26). No study separated filter from scoring, so we still need our own ablation.
- Gap 3 (where likelihoods come from, cost of a wrong table): OPEN. ACTMED draws outcome tables from LLM simulation (d01) and entropy vs KL gave small differences (d02), but nothing compares a wrong table with random order.
- Gap 4 (closed-candidate boundary): PARTLY CLOSED. AR-Bench full tables (d04, K28) show UoT below zero-shot, with failure tied by the authors to large, infinite or non-eliminable answer spaces. The explanation is untested and no size curve exists.
- Gap 5 (effect sizes for structured methods): OPEN. Schaafstal abstract gives only twice as many solved (d15). Gugerty 2007 and Goldbeck 1957 were not reachable (d16).
- Gap 6 (switch rule symptom vs normal reference): PARTLY CLOSED. Besnard 1999 opened (d05, d06): 39.33 vs 13 tests, 47.45% vs 15.38% on the look-alike part, N=3 vs 3, no statistics. It shows the failure but gives no measured switch rule (K29).
- Gap 7 (stop rule): PARTLY CLOSED. The ACTMED belief-change stop cut tests about 50% at equal or better accuracy (d02, K27). FaulT-Bench shows agents lack a no-fault exit (d07, K30). No study tests a no-fault rule.
- Gap 8 (cost weighting in tokens): OPEN, but SDBench is now re-verified (d11, d12, K31). All prices are dollars; transfer to token or time prices is untested.
- Gap 9 (verify each bisect split): OPEN. Time Travel is scored all-or-nothing (74.2% to 80.6%, d09). The per-step figure in d10 is own arithmetic with assumptions. No check was tested (K32).

Corrections to earlier work: none found. SDBench numbers c20 and c21 hold (d11). Battleship c07 holds in direction; the question-only gain is now cited as +0.021 to +0.026 F1 (d13).
