# Critique: C01.05 Self-correction (cross-check)

Checked against full PDF text (pdftotext) of: Huang 2310.01798, Tyen 2311.08516, Stechly 2310.12397, Valmeekam 2310.08118, Kumar 2409.12917, Madaan 2303.17651, Olausson 2306.09896, Gou 2305.11738, Liu 2406.15673, Tsui 2507.02778. PDFs deleted afterwards. Claims are in claims.jsonl (K01 to K26).

## Corrections made

1. b01 wrote Huang's oracle HotpotQA as "GPT-3.5 26.0 to 49.0 (GPT-4 29.0 to 59.0 as extracted)". WRONG. Table 2 is: GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 GSM8K 95.5 to 97.5, CSQA 82.0 to 85.5, HotpotQA 49.0 to 59.0. a01 and c02 are right.
2. Huang Table 3 (intrinsic) confirmed exactly as in a02/c01 (GPT-3.5 CSQA 75.8 / 38.1 / 41.8; GPT-4 GSM8K 95.5 / 91.5 / 89.0; HotpotQA 49.0 / 49.0 / 43.0).
3. Huang Table 7 (debate): the clean text gives Standard 1 response 76.7; SC 3 = 82.5; Debate round 1 = 83.2 at "6" responses; SC 6 = 85.3; Debate round 2 = 83.0 at "9" responses; SC 9 = 88.2. So a06 ("debate near 83 at 9") is right; b03 ("83.2 at 3 responses") has the wrong response count. The paper's own text says debate is "only slightly better" than SC at 3 responses, which does not match its own table counts; the table's response-count column is unclear.
4. Huang Table 8 (CommonGen-Hard) has three row pairs: Madaan 44.0 to 67.0; a second Madaan pair 53.0 to 61.1 (model not identified in the text); Huang's stronger prompt 81.8 to 75.1. Evidence lines (b04, c03) cite only the first and third. Fine, but the middle pair is unexplained.
5. Tyen backtracking table: the text confirms word sorting only (11.11% right traces broken, 23.53% wrong fixed). The table rows are misaligned in extraction, so c09's pairing "multistep arithmetic -6.67/+43.92" and b06's row-to-task pairing are NOT confirmed. Use only the word sorting figure; the range across tasks is -0.00 to -11.43 broken and +18.04 to +43.92 fixed with true location, vs +10.59 to +21.57 with random location.
6. Tyen mistake-finding GPT-4 39.80 / 52.87 / 43.40 confirmed.
7. Stechly confirmed: baseline 16%; self-critique 1/100; 2 of 100 optimal colourings accepted; 30 of 500 called correct (118 truly correct), right 5 times; in 40 instances where an optimal colouring appeared, verifier never recognised it (39 hallucinated edges, 1 was a timeout end). Added point missed by a15 summary: the "about 40%" sound-verifier result equals top-n sampling at 40% (K06).
8. Valmeekam confirmed: 40/100; 55/100 (3.48 iterations); 88/100 (4.18); verifier 61/100, 54 TP, 38 FP, 38/45 = 84.45%. c11 says "1 of 55 valid plans rejected", matching the table (1/55).
9. Kumar (SCoRe) Gemini 1.5 Flash MATH: base 52.6 to 41.4 (-11.2); SCoRe 60.0 to 64.4 (+4.4); right-to-wrong 15.8% to 1.4%. Confirmed. NEW inconsistency: the table lists base wrong-to-right 4.6%, but the text says 9.5% for base vs 14.5% SCoRe. a23 repeats the 9.5% without noting this. Treat fix-rate numbers as unreliable.
10. Madaan confirmed: GPT-3.5 math 64.1 to 64.1; ChatGPT 74.8 to 75.0; GPT-4 92.9 to 93.1; 94% "looks good"; oracle math GPT-3 +4.8 (64.06 to 68.9). The appendix also has second rows (ChatGPT 74.8 to 76.2, GPT-4 92.9 to 93.8), likely oracle or another setting; not in the evidence file.
11. Gou (CRITIC): text-davinci-003 GSM8K 70.1 / 72.2 (+2.1) / w/o tool 68.3 (-1.8) confirmed. But for ChatGPT on GSM8K: PoT 72.5, w/o tool 78.2 (+5.7), full CRITIC 77.0 (+4.5). So the no-tool critique BEAT the tool version there. b19 recorded this but the summary line "removing the tool gives gains near zero or negative" and a17/c08 ("tool feedback gives reliable gains") overstate. Made K08 "contested".
12. Olausson human vs GPT-4 feedback 52.60% vs 33.30% confirmed (Table 1). The "1.05x pass@20 / 0.97x pass@22" figures in a21 could not be located in the extracted text (the grid tables are unreadable); unverified.
13. Wrong URL/paper risk: the file arXiv 2406.02378 is a different paper ("Uncertainty and Latent Concept", Liu et al.). The evidence c14 correctly cites 2406.15673. Checked that one. Its Table 2: CSQA GPT-3.5 75.92 to 76.00; GPT-4 84.11 to 84.60; HotpotQA GPT-3.5 31.00 to 47.00, GPT-4 88.00 to 89.00; MMLU GPT-4 83.66 to 84.76. Evaluations used the first 200 questions and give no error bars. c14 said "all evaluated models improved", true but mostly by under 1 point.
14. Tsui headline numbers (64.5%, 76.0% with 5,306 traces, 89.3% with Wait) confirmed in the abstract and text.

## Contradictions between sources

- Huang (no gain, big losses) vs Liu 2024 (small gains at temperature 0 and neutral prompt). Difference may be prompt wording, temperature, model version (gpt-3.5-0613 vs 0301), metric. Not resolved. Liu's own HotpotQA GPT-4 baseline is 88 vs Huang's 49, so the grading differs; the two are not directly comparable.
- Gou: tool vs no tool (above).
- Madaan Self-Refine "20% average gain" vs Huang CommonGen replication (loss with a stronger first prompt).
- Tyen: finding errors is "poor" for GPT-4, but ProcessBench (b25) shows o1-mini at F1 87.9 on a different task, so "cannot find errors" is model- and period-dependent.
- RISE/SCoRe vs the "cannot self-correct" view: training changes the answer, prompting does not. No contradiction, a boundary.
- Tsui blind spot says models do fix errors if attributed to the user. Huang-type prompts frame the answer as the model's own, which fits Tsui's explanation, but nobody has run both on one setup.

## Weak spots

- Almost all hard numbers are 2023 models (GPT-3.5, GPT-4, Llama-2). Few tests on 2025-2026 reasoning models; Tsui is the main one and is a single benchmark of injected errors.
- Many studies use 100 to 200 items with no error bars (Stechly, Valmeekam n=100; Liu first 200).
- Evidence count of independent sources is lower than the evidence line count: Huang's paper supplies a01-a06, b01-b04, c01-c03 (one source, 14 lines). Claims count papers, not lines.
- K06 and K13 rest on one paper each.
- Planning and colouring tasks (Stechly, Valmeekam) are synthetic; transfer to open-ended agent work is unproven.
- No study measures self-correction at equal tokens against best-of-n for reasoning models; only Olausson (code) and Huang (debate) do.

## Seen only in snippets / not opened

- a14 (Tyen classifier tables), a29, b24, c22 (Pan surveys) not read; c23 (Kim RCI) known only through Huang and Kamoi; c24 (Du debate) known only through Huang.
- c15 (IoE prompt), c17 (SCORE small models), c21 (backward verification), a26/a27 per-model tables: numbers not extracted.
- c19 and c20 were reported from abstracts and texts; I did not re-open them.

## GAPS

1. Does a revise or check step help a 2025-2026 reasoning model (long-CoT) at equal total tokens vs simply letting it think longer or sampling more? No clean test found.
2. Does the Tsui self-attribution effect carry over to a scaffold: is re-presenting the draft as "another solver's answer" better than "your previous answer", at equal tokens, on math and code?
3. What is the right-to-wrong / wrong-to-right ratio of a neutral temperature-0 check step on current models (replicating Liu vs Huang with several seeds and error bars)?
4. Which tasks have a cheap sound checker (code tests, arithmetic recomputation, constraint lists) so S5 can use it, and how large is the gain over best-of-n at equal calls on those?
5. How reliable are test-based signals when they can be wrong (Reflexion's 16.3% false-positive rate on MBPP)? How does a false pass hurt compared to no signal?
6. Does locate-then-fix (Tyen) beat one-shot critique with a 2025 model, and can a cheap "first wrong step" locator reach useful accuracy with a reasoning model (ProcessBench-style)?
7. How many revision rounds are useful before flip noise dominates (Song: 2-3 rounds saturate; Huang: round 2 worse on some sets)? Is a hard cap of 1 round optimal?
8. Does "keep unless you can name the specific error" (IoE-style confidence gating) cut right-to-wrong flips without cutting fixes? Need the numbers from Li et al. (2402.12563).
9. Does item-by-item verification in isolation (CoVe) transfer from factual lists to multi-step reasoning claims?
10. Is the SCoRe/RISE gain mirrored by any prompt-only method on open models, or does it need training (decides whether we can ever drop external signals)?

## Gap search results

Evidence: `evidence_d.jsonl` (d01 to d21, all opened as PDF text). New claims K27 to K36; K06, K09, K18, K20, K22, K23, K26 updated. Web search quota was exhausted, so papers were found through arXiv listing pages and opened as PDFs. Parallel arXiv searches hit rate limits late, so some further 2025-26 searches were not run.

Status: **closed 0 fully, partly closed 6, still open 4.**

1. **Revise vs think longer vs sample more, reasoning model (partly closed).** Best test is SEVRA (d06, Qwen3-4B): a bigger first-solve budget (8,192) equals the best verify policy (MATH500 76.0 vs 76.3, GSM8K 94.54 vs 94.47) with 28% fewer tokens. Always-verify hurt on CommonsenseQA (-4.17). Hassid (d17) says short chains plus voting beat long chains. Caveats: one 4B model, 45% of MATH500 first attempts were truncated, so "fix" is mostly finishing. Not tested on a frontier long-CoT model with seeds. Default for the agent: tune the first-solve budget, then gate the check (K27).
2. **Tsui attribution in a scaffold (still open).** No paper tests "another solver's answer" vs "your previous answer" at equal tokens. Tsui's own design (d20) varies only the chat role header and the author scopes the claim to role, not authorship. So a scaffold that pastes the draft into a user message may already get the favourable condition (inference, K34). Panickssery (d19) warns that models recognise their own style (GPT-4 73.5%), so a pure relabel may be seen through. The 2026 spectral paper (d21) is theory and adds no data.
3. **Right-to-wrong vs wrong-to-right at T=0 on current models, with seeds (partly closed).** Stav (d09) gives per-model W2C/C2W for five 2025-26 models, T=0, one run: SAT C2W at most 2.1%, BBEH/HLE up to 13.25%, and Gemini Pro on HLE 10.56 fixed vs 9.32 broken. Zhang (d05) shows a neutral "are you sure" round still overturns answers in o1-mini, 4o, V3 and R1. Still missing: several seeds and error bars. No Liu-vs-Huang replication with seeds exists in what I found.
4. **Tasks with a cheap sound checker (partly closed).** Candidates with evidence: SAT-style constraint tasks (d09), code with real tests (d13: MBPP GPT-4 72.8 to 80.6; one debug turn is enough), recomputable arithmetic (d12, DISC 98.3% on multistep arithmetic from a bad start). Self-Debug also matches or beats many-sample baselines on Spider (greedy + debug = 16 samples). Missing: a 2025 model, equal calls against best-of-n.
5. **Unreliable test signals (mostly closed).** Reflexion (d18): MBPP FP 0.16, FN 0.59, result 0.77 vs no-loop 0.80 (a 3-point loss); HumanEval FP 0.01 gave +11. Stroebl (d03): false positives cap resampling; optimal K about 5 at cost ratio 4, can be 0 at higher ratios; weaker models have more false positives. Rule for S5: a self-written test pass is weak evidence; cap retries near 5; weight by coverage.
6. **Locate-then-fix vs one-shot critique, 2025 model (partly closed).** Locator half answered: ProcessBench (d04) o1-mini F1 87.9 vs GPT-4o 61.9. The fix half at equal tokens against one-shot critique is untested with a 2025 model.
7. **Round cap (partly closed).** Self-Debug: gain after turn 1 within 0.1% (d13). DISC with a judge gate: net +22 (K=1), +34 (K=3), +35 (K=8), degradation does not compound (d11). Zhang: ungated 10 rounds flip answers constantly (d05). So: 1 round ungated; up to 3 only with a gate. Not tested on a reasoning model.
8. **Confidence gating (partly closed).** Li (d01): critique hurts confident answers (82.75 to 77.35) and helps unconfident ones (27.69 to 39.23) on GSM8K-100; IoE brings GPT-3.5 5-set average from 66.1 (critical) to 73.0 (standard 70.3), GPT-4 82.5 to 86.6 (standard 85.1). The right-to-wrong figure values in Figure 4 were unreadable. Gains over doing nothing are about 1 to 3 points, single run. K20 now holds these numbers.
9. **CoVe-style isolated checks on reasoning (partly closed, answer is "not reliably").** DISC's re-run on BIG-Bench Mistake (d12): CoVe broke 28.9% of correct multistep-arithmetic answers and 35.6% on word sorting for Sonnet 4.5, but was best on arithmetic for GPT-4o (95.0). Needs a keep/change judge.
10. **Prompt-only match for SCoRe/RISE (still open).** Found nothing. S2R (d16): 51.0 to 81.6 on MATH500 from training, with plain long-CoT SFT at 80.2, so training explains most of it. Kamoi (d15) restates that no fair prompted success exists in general tasks. Snell (d02) used a fine-tuned reviser because prompting was ineffective.

Contradictions or cautions found:
- Self-attribution advice (Tsui) and self-preference (Panickssery) point in different directions for relabelling.
- DISC's headline (149:1 improvement per degradation) starts from 15% correct traces, so there are few correct answers to break. Do not read it as a general flip rate.
- Refine-then-vote (d07) is not matched on compute; do not cite as an equal-compute win.
- Several tables (Zhang Table 1/2, Reflexion rows, S2R RL rows, ProcessBench Table 3) were scrambled in extraction. Only unambiguous numbers were used; each such caveat is in the evidence `limits`.

Open items for the next pass: seeds and error bars on a neutral check at T=0 for a 2025 reasoning model; a token-matched A/B of attribution framing; locate-then-fix vs one-shot critique at equal tokens; equal-calls check vs best-of-n on code with tests for a 2025 model; any prompt-only method vs SCoRe on open models.
