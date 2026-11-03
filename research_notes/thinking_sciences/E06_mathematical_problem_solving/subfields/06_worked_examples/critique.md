# Critique: E06.06 Worked examples (cross-check)

## Corrections and confirmations (sources re-opened this session, PDF text)
1. Wei 2022: PaLM 540B GSM8K 17.9 vs 56.9 (+39.0) confirmed.
2. Fu 2022: text-davinci-002 55.4 (+7.3) vs handcrafted 48.1; Codex 66.6 (+5.6) vs 61.0 confirmed.
3. Wang 2023: GSM8K STD 15.4, CoT 48.5, invalid 39.5, no coherence 23.1, no relevance 11.0 confirmed. Invalid keeps 81% of answer accuracy; the "over 90%" figure is intrinsic recall (39.8 vs 43.9 = 90.7%). Do not mix the two.
4. Simonds 2024 (REL): 6.66, 18.89, 5.56 confirmed. Caveat: 30 AIME problems, one run, fine-tuning not prompting.
5. Didolkar 2024: MATH CoT 42.2, Complex CoT 50.30, Topic 50.31, Skill 53.88 confirmed.
6. Zhou 2022 algorithmic prompt: 90.5 / 65.6 / 79.7 / 95.0 confirmed in the table (baseline values not re-read).
7. Yasunaga 2024: GSM8K 77.8, MATH 37.3 and PaLM2 81.7 confirmed in the same table.
8. Chen 2024 (Relevant or Random): relevant 71.5/33.3, N/A 75.5/36.1, GPT-4o-mini 90.7 vs 94.5, Llama 74.8 vs 81.0 confirmed.
9. SKiC: CoT 72.0 on the DP task, ComplexCoT 56.4 MATH row, GSM8K 86.9-87.8 vs 73.0-74.4 across orders consistent with the file.
10. Pardos and Bhandari: abstract confirms 70% pass, significant gains only for human hints, human gains significantly higher than ChatGPT, ChatGPT group near ceiling in Intermediate. Table cells not rechecked.

Corrections to the evidence files: b04 gives the GSM8K CoT baseline as 60.87 while noting 60.97 elsewhere in that paper; unresolved, use "about 61". a22 should also state that human-hint gains were significantly HIGHER than ChatGPT-hint gains (abstract). b23 duplicates a08. c17 (32% failure) is a search summary only.

## Contradictions
- Yasunaga (self-generated relevant exemplars help, GSM8K 77.8) vs Chen (relevant self-generated exemplars did not beat none or unrelated: 71.5 vs 75.5). Models, prompts and baselines differ. Unresolved (K16).
- Barbieri: self-explanation prompts lower the effect; Renkl and Nathan lines say they help under load limits. Different tasks (conceptual translation vs procedures).
- Wang 2023 (validity barely matters) vs Zhou 2022 (systematic errors drive accuracy near 0) vs Barbieri (correct examples larger). Resolution: random errors tolerated, systematic ones not (K06).
- Fu (complex examples help) vs least-to-most (2-step items: plain CoT better): gain depends on item difficulty.
- Expertise reversal (persona simulation, a15) vs Lechner 2024 (no fading gain, ceiling pretest, biology).

## Weak spots
- Founding papers (Sweller and Cooper 1985, Cooper and Sweller 1987, Ward and Sweller 1990, Chi 1989, Kalyuga 2001, Renkl/Atkinson fading) were NOT opened: a25-a30 are second-hand. No first-hand founding numbers in this folder.
- Barbieri 2023 seen as abstract only: no per-moderator g.
- Gwak 2026 (c05, c23) and Notes-to-Self 2026 (c14) could not be re-found through the rate-limited APIs this session; their numbers are carried from the evidence files, unverified here.
- Snippet-only: b17, b18, b22, b24, c17 to c20.
- Almost all LLM studies are 2022-2024 prompting on older models; none tests a subgoal library with a frontier reasoning model at equal tokens.
- Duplicated sources: a19=c01, a20=c02, a21=c03, b01/b02=c04, b10=c10; claims count each once.
- Many claims rest on one paper (single-source): K08, K09, K11, K12, K15, K17, K18, K21.

## GAPS
1. Do retrieved worked examples still help frontier reasoning models at equal total tokens, or has the model internalised the procedure (expertise reversal for LLMs)?
2. Does example-first beat attempt-first-then-example (productive failure) on novel items for an LLM?
3. Does fading driven by code-checked success beat always-full examples, including on far transfer?
4. Does labelling subgoals in stored examples beat unlabelled examples for LLMs (the Catrambone/Margulieux effect)?
5. What are the first-hand effect sizes of Sweller and Cooper 1985, Cooper and Sweller 1987 and Kalyuga 2001?
6. Do self-generated exemplars help (Yasunaga) or not (Chen) when correctness is fixed by a verifier?
7. What are the per-moderator g values in Barbieri 2023 (incorrect examples, self-explanation, grade level)?
8. Why does an experience library help one model family and hurt another (Llama up, Qwen and Gemma down), and what predicts the sign?
9. How much of the in-context example gain in maths comes from format and distribution versus solution content (Min 2022 covers classification only)?
10. What fraction of LLM-generated worked examples fail code verification, and does admitting only verified ones change downstream accuracy?

## Gap search results (evidence_d.jsonl, d01-d19)
Tool limits this session: OpenAlex out of budget, Semantic Scholar and arXiv API rate-limited, web search budget used up after one query. Papers were opened as arXiv PDFs and read with pdftotext.

1. Frontier models and expertise reversal: PARTLY CLOSED. Cheng 2026 (Qwen2.5-72B-Instruct): GSM8K 8-shot 95.75 vs fixed zero-shot 95.83, MATH 81.30 vs 81.64; exemplars teach format. DeepSeek-R1 paper: few-shot consistently degrades it (no numbers). Notes to Self 2026: hints help items solved under 50% of the time (+6.31) and hurt fully solved items (-2.32). No test with a frontier closed reasoning model at equal total tokens. (d01-d03, d13-d14; claims K24, K25)
2. Example-first vs attempt-first: OPEN. No LLM study found. LEMA (fine-tuning on attempt plus correction) is only a loose analogue (+2.1 GSM8K on LLaMA-2-70B). (d12, d19; K29)
3. Fading driven by code-checked success: OPEN. No study found. (d19)
4. Subgoal labels for LLMs: PARTLY CLOSED. Zhao 2023 on miniF2F with an Isabelle verifier: removing subgoal demos 45.5 to 40.6; 44.3 vs 38.5 without organiser. Formal proofs only, not Margulieux-style natural-language labels. (d04, d05; K26)
5. First-hand Sweller/Cooper 1985, Cooper/Sweller 1987, Kalyuga 2001: OPEN. Paywalled, no open copy found. Keep those entries marked unopened. (d18)
6. Self-generated exemplars with a verifier: PARTLY CLOSED. Auto-CoT shows unverified self-chains retrieved by similarity repeat errors (21.3% zero-shot error on MultiArith); STaR shows answer-verified self-chains work for fine-tuning. Still no direct Yasunaga-vs-Chen test with correctness fixed. K16 stays contested. (d10, d11, d16)
7. Barbieri per-moderator g: OPEN. Springer blocked. (d17)
8. Why libraries help one family and hurt another: LARGELY CLOSED for one study. Notes to Self: baseline strength on the item, format fragility (Qwen's loss was answer-format disruption and mismatched retrieval), and retrieval fit; Gemma lost even with a blank template (gemma-2-2B 21.77 to 13.08). Single paper, small models. Also confirms the numbers carried from c14. (d13-d15; K19, K25)
9. Format and distribution vs content in maths: PARTLY CLOSED. Madaan 2022: wrong equations keep 24.39 vs 27.37 on PaLM-62B GSM8K; no-pattern prompts fall to direct level; Cheng 2026 content masking returns to zero-shot. Old models, no per-component maths effect sizes for modern models. (d06, d07, d01; K27)
10. Failure rate of LLM-generated examples under code verification: PARTLY CLOSED. OpenMathInstruct-1 reports coverage (MATH 80.1 to 85.9 with masked solutions) and shortcut copying but not a raw failure rate or a downstream effect of admitting only verified items; Toshniwal call right-answer-wrong-reasoning rare but unmeasured. The earlier 32% (c17) remains a snippet. (d08, d09; K28)

Housekeeping: duplicate source LEMA authors are An et al. (2024). Auto-CoT Table 1 cell assignment came from a garbled extract; do not quote the three-column figures without re-checking. Still stays unopened: Gwak 2026 (c05, c23).
