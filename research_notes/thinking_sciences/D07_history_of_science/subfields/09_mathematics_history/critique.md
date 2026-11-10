# Critique: D07.09 Conjecture and proof development (cross-check)

## Corrections made (sources re-opened this session, full PDF text)
1. Davies 2021 (Nature): 78% test accuracy, 25% chance baseline, and the slope-only linear model also at 78% are all confirmed.
2. Chuharski 2024: 757 outputs, 420 unique (55.48%), 109 counterexamples (25.95%), 40 survivors (9.52%), 271 non-executable (64.52%) are confirmed. Per-model survival (25/94 = 26.60%, 4/89 = 4.49%, 11/237 = 4.64%) is confirmed. CORRECTION: ChatGPT non-executable is 33/94 = 35.1% by the paper's own table, not the 37.76% printed in its text. The paper is internally inconsistent; use 35.1%. Unique counts differ a lot by model (ChatGPT 94, Claude 89, Gemini 237 of about 250 outputs each), so the duplicates came mostly from ChatGPT and Claude (b04 was too general).
3. LeanConjecturer: 12,289 / 10,950 / 4,130 / 3,776 / 103.25 confirmed; 412/392/108 ablation confirmed; GRPO table (2285, 3657, 5307 of 24,576; 47, 49, 50 of 192) confirmed. CORRECTION: a26 and c09 say "31% non-trivial" (3,776/12,289). The paper uses 3,776 of 10,950 valid (34.5%). Both are right; state the denominator. The 3,776 is a subset of the 4,130 novel.
4. Petrov USAMO: 10.1/42 for Gemini-2.5-Pro and the other means are confirmed. The paper prints an average of 24.4%, while 10.1/42 = 24.05%; a small rounding mismatch in the paper. LLM graders gave about 15-20 of 42 for top models; "inflated by a factor of up to 20" is confirmed.
5. IMO-Bench: 80.0% AnswerBench, 65.7% advanced ProofBench, 23.3% and 7.1% for the next models, Pearson 0.96 and 0.93, and Grok 4 heavy 76.2% on USAMO vs 11.1% on novel problems are confirmed. Table: GPT-5 65.6% and Grok 4 73.1% on AnswerBench confirmed.
6. BrokenMath: GPT-5 29.0% sycophantic is confirmed in the table (c11 was abstract-only).
7. Plan-and-Solve: 70.4 vs 76.7 average; GSM8K 56.4 to 59.3; AQuA 38.9 to 46.0; SVAMP 69.9 to 75.7; error shares 27% and 12% are confirmed.
8. CounterMATH: 1,216 pairs, 1,025 SFT samples, Qwen2.5-Math-72B at 41.8 F1 are confirmed. CORRECTION: b09 pairs "65.1 strict / 75.7 loose" with the best commercial model, but that row has F1 77.0; the 80.7 F1 row has strict 54.2. They are different models. Model names are lost in the PDF layout, so do not name models.

## Contradictions between sources
- c05 says LLM judges gave 9-24 /42 where humans gave 1-10. The paper table shows about 15-20 for the models checked, so the 9-24 range was not reproduced. Use "up to 20x inflation".
- b04 (prompt wording did not fix duplicates) vs a11/b07 (prompt and context change yield sharply): different domains and metrics, so K13 is marked contested.
- Polya-heuristic prompting: c13 shows gains for some models and losses for others; Plan-and-Solve shows small gains. The effect depends on the model (K07 contested).
- The Plan-and-Solve paper does not cite Polya as its source (a16), so it is only an analogue.

## Weak spots
- No controlled LLM study tests Lakatos moves (monster-barring, exception-barring, lemma incorporation) as a factor. The nearest are Davies (human in the loop), c01 (small toy agent system) and c02 (self-report sprint).
- Lakatos 1976 and Polya 1945/1954 were never opened (a02, a21, c19, c20). Schoenfeld 1985 only via Wikipedia (a04, a23), so no effect sizes.
- LeanConjecturer is a non-archival workshop paper; "non-trivial" means only that aesop failed.
- Most LLM results use 2024 to early 2025 models; USAMO 2025 numbers are already superseded.
- Georgiev et al.: counts of matched vs improved problems among the 67 were never extracted.

## Only seen in snippets or abstracts
c02 (First Proof Sprint), c03 (QED), c06 (Godel Test), c08 (ConjectureBench), c12 (Draft Sketch Prove), c14 (Llama-Polya), c15 (FrontierMath), c16 (DeepTheorem), c13 (blog, no n). Unverified from memory: c10 (FunSearch), c17, c19-c22. Used in claims only as single-source.

## GAPS
1. Does an explicit Lakatos-style typed counterexample reaction (change the claim, the step, or both) beat untyped retry at equal tokens? No study found.
2. What fraction of surviving model conjectures are true and non-trivial under an independent check (not just aesop failing or no counterexample found)? This sizes the funnel.
3. Does a forced look-back step (re-derive another way, generalise) improve final accuracy? Only dialogue-share data (Llama-Polya) exists.
4. Do Polya heuristics help when chosen by a program rule per state rather than listed in the prompt? Current evidence (a blog) is mixed and unreviewed.
5. How do 2026 frontier models score on novel proof tasks with and without a scaffold, at equal tokens?
6. What are the primary effect sizes in Schoenfeld 1985 for heuristic training vs control?
7. How often do checker-gaming events occur in code-checked conjecture loops, and does a hold-out check cut them? Only anecdotes (AlphaEvolve).
8. Do conjectures the agent made and stored as lemmas help on later same-topic items (the inference-time analogue of the GRPO result, which showed no transfer)?
9. What measured results exist for Pease/Colton computational Lakatos models, Lenat's AM and Graffiti critiques?
10. Does the skeptic-agent gain (c01) replicate outside the homology toy domain?

## Gap search results
Search conditions: the shared web search budget ran out after one query; OpenAlex and Semantic Scholar returned HTTP 429 and the arXiv API returned empty results. Most gaps therefore stay open. New evidence is in evidence_d.jsonl (d01 to d18; d18 is a negative-search note, opened:false).

- GAP 1 (typed Lakatos reaction vs untyped retry): STAYED OPEN. No direct study found. Nearest: CRAFT (ICML 2026, abstract page only) with 78% to 94% for a 7B model on 50 claims, with a baseline of round-1 judgment, not untyped retry. Learning to Disprove trains on a two-part check (valid example plus which hypothesis breaks). New claim K21 marks it untested.
- GAP 2 (fraction of surviving conjectures that are true and non-trivial under an independent check): STAYED OPEN. Nothing new; the funnel numbers of K01 stand.
- GAP 3 (forced look-back step): STAYED OPEN. Not searched beyond one failed query.
- GAP 4 (program-chosen Polya heuristic per state): STAYED OPEN.
- GAP 5 (2026 frontier models on novel proofs, scaffold vs none): PARTLY ADDRESSED. QED: 5 of 18 open research projects solved with expert confirmation; verifier 0/17 false positives out of 214 candidates; First Proof Sprint: 4 of 10 closed and validated. Both self-reported and without an equal-token no-scaffold arm, so the scaffold effect is not measured (K22).
- GAP 6 (Schoenfeld 1985 effect sizes): STAYED OPEN. Not accessible.
- GAP 7 (checker gaming rates): PARTLY ADDRESSED. The Georgiev et al. paper was opened and the quote verified, plus one worked case (irregular function exploiting the numerical integration; fixed by restricting to bounded step functions). Still no rates and no hold-out test (K19).
- GAP 8 (stored lemmas helping later same-topic items): STAYED OPEN.
- GAP 9 (Pease/Colton HRL, Lenat AM, Graffiti measured results): STAYED OPEN. Martin and Pease 2013 was opened; it describes HRL and HR but gives no benchmark numbers. It gives a human base rate: counterexamples or examples in 34% of sampled MathOverflow responses, errors corrected in 37%.
- GAP 10 (skeptic gain replication): STAYED OPEN. The paper was opened; it is a single task (homology from polyhedra) and a symbolic RL system. I did not extract the result tables. No replication found.

Other corrections from this pass: c08 (ConjectureBench) is now opened with exact numbers (d15). The a-claim "Georgiev matched/improved counts" is still not extracted; the 67-problem count is verified, the per-outcome counts are not (d09). The Chen 2026 lecture notes were only searched, not read in full (d06).
