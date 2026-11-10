# Critique and cross-check: E06.08 Problem posing, conjecture

Cross-checked 2026-11-10 by re-opening the arXiv and ERIC PDFs (pdftotext) behind the main numbers.

## Corrections made (numbers re-opened)

Confirmed exactly: STP 28.5% vs 13.2%, 65.0%, 23.9%, 8/644, 131 of 2.5M, 47%, 3.6M, 51.3B (2502.00212); CPL 5/20 vs 0/20, p=0.024, 106 vs 328, 2106 vs 1935 of 2123, 7 vs 0 of 80 (2509.14274); LeanConjecturer funnel 12,289 / 10,950 / 4,130 / 3,776, 103.25, 2285 / 3657 / 5307 of 24576, 412/392/108 (2506.22005); Rosli g values, Q values, N=1,316 (1,038 + 278), 3,730 pool; Kul and Celik effect sizes; MathDuels 62.9%, 27.6%, 39%, error table 5.1/9.5/25.0 and 3.0/6.9/21.1; BrokenMath 29.0%, 15.6, 22.5, 5.4, 8.6, 6.4, 55.6 to 51.0, 33.4 to 37.9; OEIS Open 147/492, 30/26/22%, 476,000, 216, $6/$9/$10.

Corrections and clarifications:
1. Chuharski et al. (a20, c03): the models are GPT-4o (gpt-4o-2024-05-13), Claude 3.5 Sonnet and Gemini 1.5 Flash, not "GPT-4, Claude Sonnet, Gemini 1.5". Unique counts per model are 94, 89, 237 (total 420). The percentages (109 = 25.95%, 40 = 9.52%, 271 = 64.52%) are shares of the 420 UNIQUE conjectures, not of the 757 outputs (a20 says "of outputs"). The three groups sum to exactly 420. So of the 149 testable conjectures, 40 survived (27%), a more useful figure than 9.5%. The 26.60/4.64/4.49% are shares within each model's unique conjectures. o1 (51 conjectures: 22 survived, 28 failed, 1 not run) is in the appendix and the authors say they did not finish it.
2. ConjectureBench (b10): the pair "78.77 (answer given) vs 26.70 (hidden), -52.07" compares LEAN-FIRE "Seen" with LEAN-FIRE "w/o FS Unseen" in Table 3. It mixes two changes (answer hidden and few-shot removed). The pure answer-hidden effect is the 23.7% average drop (Table 5) and the baseline 36.32 to 20.35 Grader@10. b10 wording "23.7% drop" is right; the -52.07 framing is wrong. a22 flagged "w/o few-shot" correctly.
3. OEIS Open (b13, c22): the paper itself re-scores Claude Opus 4.8 at 144/492 (29%) under the Comparator checker, versus 147/492 (30%). The best LITE score (44%) is from "Claude Fable 5", run only on LITE. AlphaProof Nexus: paper says 44/492, repo releases 38.
4. BrokenMath (b23): "34.1%" for DeepSeek-V3.1 under validate-first is written as "34.1% improvement"; b23 turned it into "34.1 points". Relative vs absolute is not stated in the text read. Treat as ambiguous.
5. STP (a12): the 131 of 2.5M figure comes from an Isabelle-experiment checkpoint (Section 4.4); the intro describes the 11.4% pass-rate checkpoint on LeanWorkbook in general terms. Fine, but do not mix with the Lean headline run.
6. Rosli (a06 vs b02): consistent. Note the paper calls the effect range "0.76 to 1.31" robust, which our reading disputes (fixed-effects, small k).

## Contradictions between sources
- Human meta-analyses (g about 0.8-1.3) vs the null achievement result in arXiv:2002.04447 (N=44, only the abstract page opened) vs Kul and Celik's own moderator (Qb=50.0 for published vs unpublished) that contradicts their "no publication bias" statement.
- STP says self-posed conjectures add 2-3% on external benchmarks; LeanConjecturer finds essentially no transfer (9/14 to 8/14). Different scale and method; unresolved (K22 contested).
- OEIS Open says elaborate agent loops and literature give nothing; CPL says a pose-then-prove loop with context beats joint generation. Not a direct conflict (different tasks, one target theorem in CPL), but it limits how far "loop structure helps" can be pushed.
- Silver and Cai (human): good solvers pose more and richer problems. MathDuels (LLM): the best solver is not the best author. Not exclusive; the first is correlational.

## Weak spots
- Almost all LLM evidence is formal (Lean, Isabelle, GAP) with a checker. Almost none is natural-language competition solving, which is what our agent does.
- No study tests What-If-Not (Brown and Walter) or Lakatos moves on an LLM. The primary books were not opened (a26, b25, b26). The Lakatos evidence is a rational reconstruction, only Part I read.
- Many headline LLM results rest on one target (CPL: one theorem; 5 vs 0 successes, Fisher p=0.024 is fragile), one seed (LeanConjecturer GRPO), or tiny held-out sets (14 problems).
- Dependencies: evidence files a, b and c overlap on the same eight papers. The independent source count in claims.jsonl counts distinct papers, not evidence lines.
- LLM judges and LLM verifiers decide validity in MathDuels, BrokenMath and ConjectureBench.
- Contamination signs in ConjectureBench; benchmark-overlap risk in STP.

## Only seen in snippets or abstracts
- a09 (arXiv:2002.04447): abstract page only.
- b03 (Silver and Cai 1996): Crossref abstract only; the "509 students" and result are from the abstract record.
- a27: ERIC titles only. a15 (Minimo transfer rates): numbers not extracted. c23 (AlphaProof Nexus): abstract and introduction. b04 (Ran et al.) and c02 (Martin and Pease) were not re-opened in this cross-check; Rosli and Kul were.
- Not re-opened this pass: MathDuels author Elo values, RIDE 21.73%, ALPS 2.2%/14%, Ran 74/18/8.

## GAPS (most decision-relevant first)
1. Does a What-If-Not operator (list givens, negate each, solve the variants) raise final accuracy over a plain "restate and check" step at equal tokens, on natural-language competition problems? No LLM test exists.
2. Does a code-run counterexample search (small cases, brute force) before proving raise accuracy on conjecture-type and "find the answer" problems, compared with a model judgement of truth? How much of the gain survives when no code sandbox is available?
3. Does a log of verified findings (CPL-style, S9) help a non-formal solver on related problems, and does it help beyond the same model re-proving its own easy results (the CPL caveat)? Is there a replication of the CPL 5/20 vs 0/20 result on a second target?
4. Which counterexample-handling move (lemma-incorporation vs monster-barring or exception-barring) do LLMs actually make when a check fails, and does forcing explicit new definitions with a full re-test cut false rescues? No measured rate exists.
5. How well does an LLM guess the answer first (ConjectureBench-like) on natural-language problems, and how often is a wrong early conjecture kept despite later evidence? Is the 3-6% strict-match rate mainly a metric artifact?
6. Does the "pass rate in (0, 1/4]" lemma-selection rule from STP work at inference time as a subgoal filter without training, and what K makes the pass-rate estimate cheap enough?
7. How much of the human posing meta-analysis effect (g 0.64-1.31) survives with unbiased designs? Are Larsen and Zandieh (2008) guided-reinvention results and the WIN geometry studies (EJ1186756, EJ1301417) stronger than the two meta-analyses?
8. Does the author-solver gap (MathDuels) mean a solver's self-posed variants are unreliable, i.e. what fraction of an agent's own what-if-not variants are ill-posed or have a wrong key, and does an independent check lower it?
9. Do few-shot examples of posed-and-refuted conjectures beat a structured conjecture procedure (ConjectureBench pointed to examples), and for which model strength?
10. Does hiding or leaking the target claim in our own benchmarks shift scores by an amount comparable to the 23.7% in ConjectureBench?

## Gap search results (2026-11-10, evidence_d.jsonl d01-d19)

Budget note: 6 WebSearch calls returned; the last 2 were refused (shared budget). arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429, so the search was mostly web search plus direct PDF fetches.

Closed or mostly closed:
- Gap 2 (code counterexample search): partly closed. REFUTE (d01-d03): o3-mini high with code execution breaks under 9% of wrong solutions; randomized brute-force prompting gives 4.0 to 8.3% and 86% of failed search runs come from wrong brute-force code. MathConstruct (d04-d05): interpreter roughly doubles accuracy at 5x cost; small-cases-then-generalize beats pure brute force (19.2 vs 9.9, 12.9 vs 7.6). Without a sandbox the gain is not available; that exact ablation was not found. New claims K23, K24; K08 changed to contested.
- Gap 5 (answer-first) and Gap 10 (answer leakage): mostly closed. DAP (d15-d16): answers above 80% on PutnamBench vs formal proof under 10%; 293/340 vs 265/340 with and without self-verification; spurious rfl proofs when the answer is visible. So the "3-6% strict-match" of ConjectureBench is mainly about formal statement matching, not natural-language answer finding (K11 now contested). New claim K25.
- Gap 8 (ill-posed own variants): closed with a number. Code2Math (d06, d08): external judge certified 74/90 to 98/98 of internally accepted variants, so up to 18% were ill-posed after a self-check; human audit 126/127. New claim K26.
- Gap 7 (human meta-analysis): partly closed. Zhang et al. 2024 (d13-d14): g=0.72 [0.53, 0.90], I2=69.2%, controlled designs give smaller effects, Egger test significant. Outcome is posing skill, no WIN-only effect. Larsen and Zandieh guided reinvention and the WIN geometry studies were NOT re-read, so that half stays open. New claim K28.

Partly addressed:
- Gap 3 (verified-findings log, CPL replication): 2606.28747 (d18) shows verified theorems as prompt lemmas help GPT models in a toy Hilbert system (no exact values in the text); Prover Agent (d17) feeds verified lemmas back at inference. No replication of CPL 5/20 vs 0/20 on a second target, and no natural-language test. Stays open for replication.
- Gap 6 (pass-rate filter at inference): Prover Agent (d17) is training-free and uses lemmas (25% special cases, 25% technique, 41.7% subgoals) but no pass-rate filter. Open. New claim K27 on special-case lemmas.

Still open (no source found, d19):
- Gap 1: What-If-Not operator vs restate-and-check at equal tokens. No LLM test exists in anything found.
- Gap 4: lemma-incorporation vs monster-barring rates in LLM revision. No measured rate.
- Gap 9: few-shot examples of refuted conjectures vs a structured procedure. Not searched beyond ConjectureBench.

Other findings worth keeping: CounterMATH (d09-d10) shows most models give almost no real counterexamples (strict example rate as low as 0.4%) and a counterexample hint prompt alone added about 1.4 F1; its SFT result (AIME24 20.0 to 30.0) is 3 problems out of 30 and one run. Learning to Disprove (d11) was rejected from ICLR 2026; its hypothesis-deletion mutation matches the what-if-not step of dropping a given, but evidence is training-only.

Caveats of this pass: REFUTE and CounterMATH tables had scrambled layouts in pdftotext; only headline cells and row-order readings are used. Prover Agent lemma percentages come from about 12 lemmas.
