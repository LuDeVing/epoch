# Critique and cross-check: D03.09 Inductive logic and ILP

Cross-checker pass. Re-opened (full text, pdftotext): FOIL (Quinlan 1990), Popper (2005.02259), Hypothesis Search (2309.05660), Qiu et al. (2310.08559), HtT (2310.07064), Gandarela et al. (2408.16779), SLR-Bench (2506.15787), ALBI (2611.05039), Reason Popper-ly (2607.23019). Scratch PDFs deleted.

## Confirmed (no change)
- FOIL: 78/80 family test cases; chess endgame CIGOL 77.2%, DUCE 33.7%/37.7%, FOIL 92.5% sd 3.6 and 99.4% sd 0.1; 128-constant limit; append 188 s, reverse 247 s.
- Popper: Enumerate 159 s vs Popper 4 s on evens; Metagol falls to default 50% near 10,000 examples, Popper fine at 20,000.
- Hypothesis Search: 17 / 23 / 30 / 33%, Icecuber 43%, 33 of 49 (67%).
- Qiu (GPT-4 main table): ACRE task 28.0 (IO) vs 59.0 (T=3,N=5); MiniSCAN 0.0 vs 46.0 (T=3,N=1); List Functions 39.6 vs 52.0 (T=1,N=1); MiniARC raw 33.1 vs 18.7.
- HtT: 50.6 -> 64.3, 9.9 with random rules, GPT-3.5 + GPT-4 rules 48.4; error shares 65% / 81%.
- ALBI table (Popper 6.8 iterations, 81.8 s; Gemini 333.6 s; Claude 397.7 s; GPT 1631.9 s), Popper-ly numbers (19.09 -> 61.93 etc.), SLR o3/gpt-5 rows, +1777% tokens, +1034% cost, Gandarela 21x and "3 orders of magnitude".

## Corrections
1. a18 mixes two rows: ACRE "IO 64.0 / SR 70.0 / best 82.5" are RAW accuracy; the matching TASK accuracy is 28.0 / 32.0 / 59.0. b14 and c04 are consistent with the table. Quote task accuracy for decisions.
2. b14 says MiniARC refinement raw "5.9-12.8"; the table has 5.9, 12.8, 10.1 and 18.7 (T=3,N=5). Range should be 5.9-18.7 versus 33.1 direct.
3. a19 "IID 39.6 -> OOD 32.0": the 32.0 matches the ACRE self-refine task accuracy in Table 1, so this IID/OOD pairing is probably a mis-read of a figure. Treat as unverified; do not use.
4. a16/c07 note "human-written ~ about the same": paper says human-selected 33% is "on par" with golden human-written; b18/c07 give 45% for human-written, and the paper says Icecuber (43%) "slightly underperforms the human-written results", so 45% is consistent. Keep 45%.
5. c22 "gpt-4o hard-level 20%": the table row is "100 93 29 ... 20" with a blank cell, and b22 reads it as medium 20 and hard about 0. Column alignment is ambiguous in the text; do not quote a GPT-4o hard score.
6. b22 calls $207 "cost of the run", c22 "per 1,000 prompts". The paper's column is "Costs ($)" for the full evaluation; the per-1,000 wording is unverified.
7. b09 and a09-a11, a23-a26 were never opened (paywalled or snippets). Muggleton's founding papers (1991 ILP, 1995 Progol, 2014 MIL) are therefore not backed by numbers in this folder.
8. c25 LLM2LAS and c26 Rocha were not re-opened in this pass.

## Contradictions and tensions
- CoT: MIRAGE (a22) says CoT lowers induction accuracy up to 18-22%; SLR-Bench (b22) says CoT adds about 5% on logic tasks; HtT uses CoT as its baseline and wins by adding rules. Task type (induction of an unseen rule vs deduction with given rules) probably explains it; no paper tests both in one setup.
- Verifier value: Qiu shows refinement is large with a symbolic interpreter and near zero or negative when the LM interprets or the task is perceptual (MiniARC). ALBI and ADVENT report gains from exact tests. Consistent, but all three use different benchmarks.
- Noise: Gandarela finds LLMs beat Popper under noise, MaxSynth shows noise-aware ILP beats plain Popper. Nobody compares LLM to MaxSynth.
- Cost: ALBI uses fewer iterations than Popper but is 4-20x slower in wall time; Gandarela says LLMs are 1000x faster. Different tasks, different baselines (Popper settings with timeouts).

## Weak spots
- Most LLM evidence is one-paper-per-claim; only a few claims reach independence 2-3. Wang et al. supplies four evidence lines that are one source.
- 2026 papers (ALBI, Popper-ly, ADVENT, AutoSpec, SLR) are single-lab and recent; no replication. Model names (GPT 5.4 Pro, Claude Opus 4.6) are not controlled for tokens.
- None of the studies report results at equal tokens. Our agent's question is token-matched, so every effect size here is an upper bound on what a fixed budget buys.
- Qiu and Wang use GPT-4 (2023); behaviour of 2026 reasoning models on the same tasks is unknown.
- Only snippets: b09 (ultra-strong ML 2018). Cropper 2020 "Turning 30" has no usable numbers (digits lost).
- Human studies (b10, c27) are small and the first has a 4 vs 9 student sample.

## GAPS
1. At equal tokens, does generate-hypotheses + counted test on the examples beat plain chain-of-thought and best-of-N for rule induction with a current reasoning model (not GPT-4)?
2. How many candidate rules are enough? Wang shows recall of a correct hypothesis (49 of 100) is limiting; what is the recall-vs-N curve and where does selection become the bottleneck?
3. Does an MDL-style score (fit minus rule length, as in MaxSynth) pick better rules than "consistent with all examples" when 10-30% of examples are wrong, in an LLM loop?
4. Does the induce/apply gap (MiniSCAN, 80% to near zero) persist for current models, and is code execution the only fix or can a fresh-context application call close it?
5. Is a store of verified rules (HtT-style) worth its tokens for tasks beyond kinship and arithmetic, and how do wrong rules in the store propagate (random rules cost 40 points)?
6. When should the agent refuse to refine (MiniARC, perceptual tasks)? What cheap signal predicts that refinement will hurt?
7. Do LLMs beat or lose to classical ILP on deep chains of independent predicates (Gandarela CHAIN) with 2026 models, and is there a hop-count cutoff for handing off to a solver?
8. Do the primary Muggleton papers (inverse entailment, MIL, ultra-strong ML) contain numbers on example efficiency (often one example) that we can test against the LLM claim?
9. Does LLM predicate invention verified by code (ADVENT 80%) transfer to open domains, and what does it cost in tokens?
10. Can ILP-style generate-test-constrain be used on the agent's own failed attempts (forbid the failure class) and reduce rounds, as Popper's 159 s vs 4 s suggests?

## Gap search results (gap searcher pass, 2026-11-10)
Evidence in evidence_d.jsonl (d01-d20; d19 and d20 are search logs, not opened). Papers read in full text: SOAR 2507.14172, PBEBench 2505.23126, InductionBench 2502.15823, Parab 2509.01016, Li et al. 2502.16169, Sharma MML 2508.06230, SIRBench 2509.16226, MATHEMAGIC 2510.05962, LLM-PV 2510.14331, Sketch-and-Verify 2605.08658, Muggleton 2018 USML (Machine Learning 107), Lin 2014 MetagolDF. Scratch PDFs deleted. The arXiv, Semantic Scholar and OpenAlex APIs were rate-limited (429), so 7 WebSearch calls plus direct PDF fetches were used.

- Gap 1 (equal tokens, reasoning model): PARTLY CLOSED. At equal LLM calls, test-and-repair beats pure sampling (SOAR: 72B 12.88 to 25.25). PBEBench shows longer thinking beats more samples for one reasoning model. Nobody reports an equal-token comparison of hypothesis-plus-test vs CoT vs best-of-N with a current reasoning model on rule induction. Stays open at token level.
- Gap 2 (how many candidates): PARTLY CLOSED. Parab: correct hypothesis in 46.4% of 64-sample trials (GPT-4o); LLM-PV bound k about 1/p; diversity beats count (Sketch-and-Verify, code task). No recall-vs-N curve for rule induction was found. Selection bottleneck: the summariser loses 26% of correct hypotheses.
- Gap 3 (MDL in an LLM loop): OPEN. MML vs C-MDL (no LLM) shows no gain under 10-50% noise, gains on few or one-sided examples. Li et al. show a plain execution-score loop loses 5.6 to 7.6 points at 10% noise (DeepSeek-R1). No LLM + MDL study found.
- Gap 4 (induce/apply gap): PARTLY CLOSED. Not uniform: GPT-5 shows no gap on altered arithmetic (87.2 vs 83.7), GPT-4o-mini does (47.8 vs 71.4). The test is implicit induction, not rule-writing, so the MiniSCAN case is not re-tested with 2026 models. K09 now marked contested.
- Gap 5 (rule store beyond kinship and arithmetic; wrong-rule propagation): OPEN. No new study found.
- Gap 6 (when to refuse refinement): PARTLY CLOSED. Refinement gave no gain on fuzzy scientific tasks (SIRBench); example gains vanish when the hypothesis space is large (InductionBench). Candidate cheap signals: weak check proxy, large window or vocabulary. No study validates a predictor.
- Gap 7 (chain depth cutoff with 2026 models): PARTLY CLOSED. PBEBench and InductionBench show a wall with chain length even for GPT-5 and o3-mini. No direct LLM vs Popper test on CHAIN with 2026 models. No hop-count threshold has been measured.
- Gap 8 (Muggleton primary numbers): PARTLY CLOSED. Opened 2018 USML (human trials) and Lin 2014 one-shot (accuracy about 61%, humans 87%/74%, FlashFill 76%). Progol 1995 and the MIL 2015 paper were not obtained, so example-efficiency numbers for them remain missing.
- Gap 9 (predicate invention in open domains, token cost): OPEN.
- Gap 10 (generate-test-constrain on the agent's own failures): OPEN. No LLM plus Popper constraint paper found beyond ALBI and Reason Popper-ly.

Changes to claims.jsonl: K06 now 2 sources (established); K08 and K10 raised to 2 sources; K09 set to contested; new claims K21-K26. Caveat carried over: no study here is matched on tokens; SOAR is matched on calls.
