# Critique: Falsificationism (D01.04), cross-check

## Numbers re-opened this session (full text or abstract)
Confirmed against the source text:
1. Jhaveri et al. 2026 (arXiv 2604.02485): task success 6% to 78%, 45-turn limit, discovery 42% to 56% with interventions; Wason 1960 restatement 29 people, 6 first announcement, 21 eventually, I:C 1.79 vs 0.24 and 0.50 vs 0.19. Distillation 0.59 and "almost tripling" appear in the text. (a08, a16, b11, b25, c02, c05, c06)
2. FalsifyBench (2606.04751): GPT-5.2-Chat 75%, GPT-OSS-120B 68%, best instruction-tuned 41%; Spearman -0.779 (p=0.003); -0.937 (p<0.001); coefficient -4.148, OR 0.016. (a19, a20, b13, b14, c09, c10)
3. POPPER (2502.09858): 66.5% more power than ReAct, 3.17x Self-Refine, 9.7x faster, 35.9% and 28.1% failure shares, nine experts. (a22, a23, b20, b21, c13)
4. REFUTE (2502.19414): 324 problems, under 9% counterexamples, 48.7 rating-implied solve rate, 3% with correct solution, 35% invalid RandSearch samples. (b19, c15, c16)
5. WILT (2410.10998): abstract says best model 28% (14/50). (a15, b16, c18)
6. Batista and Griffiths (2602.14270): N=557, "five times higher" discovery with unbiased sampling; abstract matches. Cell values 5.9% vs 29.5% were not re-opened (a25, b18).
7. Branchini 2023 (PMC10219317): 78.33% vs 36.66% confirmed. Branchini 2025 (PMC12402026): 78.33%, 38.33%, 36.66% confirmed. (b05, b06)
8. Berthet 2024 (PMC11561113): F(1,198)=158.12, 69.1% vs 48.2%, d=0.89 confirmed. (b07)
9. Scheel et al. 2021: abstract via Crossref confirms 71 RRs vs 152 standard, 96% vs 44%. (b10, which was marked opened:false but is now verified)

## Corrections and flags
- Branchini 2023 and 2025 give identical rates for the opposites arm (78.33%) and the control arm (36.66%). With 60 per arm that is 47/60 and 22/60 in both papers. This could be reused data or a coincidence. The 2025 paper is therefore not an independent replication of the effect size; treat the 78% as one study (K04, single-source).
- Jhaveri et al. describe WILT's best result as "26%" while the WILT abstract says 28% (14/50). Use 28%; the 26% is the secondary citation's error or an earlier version (a15, c18, b16 all say 28%).
- a08 and b25 cite arXiv 2604.02485 for Wason 1960 with opened:false for a08. Wason's own paper was never opened; the numbers come from Jhaveri's restatement. Marked second-hand in K01.
- b09 (Ragni et al. meta-analysis, 228 experiments) and b24 (Tweney 1980 about 60%) were not opened. b22 (P-Bench) was a Hugging Face page, not a paper. c25-c28 read only in part or not at all. c26-c28 are second-hand.
- Two evidence blocks duplicate the same papers (a16-a18 vs b11-b12 vs c01-c07; a22-a23 vs b20-b21 vs c12-c14). They are one source each, not independent. Counted as one in claims.

## Contradictions between sources
- Do reasoning models test more incompatibly? FalsifyBench: yes, much more (positive-test share 24-39% for reasoning vs 66-82% for instruction-tuned). Failing-to-Falsify: switching to thinking raises success but not consistently I:C (Qwen3-32B thinking I:C 0.14 at 0.41 success). Tasks differ (numbers vs WordNet categories; 45 vs 20 turns), and FalsifyBench measures confirmation share by an LLM annotator. Left as contested (K09).
- Think-in-Opposites helps thinking models and hurts or does nothing for several non-thinking ones, and Dual-Goal lowered success for some. Human literature says Dual-Goal doubles success. So human debiasing tricks do not transfer cleanly to LLMs (K10).
- Gale and Ball say the number of goals matters, Tweney says the DAX/MED labels matter; abstract-level only.

## Weak spots
- Almost all LLM evidence is the 2-4-6 family (rule discovery with yes/no feedback). Nothing shows the effect in open-ended reasoning, math, or code answer checking, except REFUTE and POPPER.
- Correlations (rho -0.779, -0.937) are across 12 model-level points; they do not show that forcing negative tests causes success. Only Jhaveri varies the prompt.
- LLM oracle in FalsifyBench (kappa 0.34 to 0.98) and GPT-5-Mini labelling of set relations are not human-checked at scale.
- Human studies of training effects are from one lab (Branchini); Gorman and Gorman was abstract only.
- Nothing here tests a falsification step inside a full multi-stage scaffold at equal tokens against best-of-N. The link to our schema G3 and S4 is by analogy.
- Philosophy evidence is mostly the Stanford Encyclopedia, a secondary source; Popper's Logik der Forschung and Mayo's book were not opened.

## Seen only in snippets or abstracts
Gale and Ball 2002, Gorman and Gorman 1984, Ragni et al. 2018, Tweney 1980, P-Bench, Mayo 2019 (abstracts only), Baby-AIGS numbers, co-scientist (partly), He et al. 2026 (abstract and introduction), King (Robot Scientist), Langley (BACON).

## GAPS
1. Does a forced "opposite test" or "two complementary hypotheses" step at S4 raise accuracy of a tool-using agent on answer-checking tasks (not 2-4-6) at equal tokens versus best-of-N? No paper measures this.
2. Does making a thinking model test more incompatibly cause the gain, or only correlate? Needs an experiment that varies I:C while holding reasoning mode fixed (Jhaveri varied the prompt but gains also changed the reasoning length).
3. Can the Branchini effect (36.66% to 78.33%) be replicated by an independent lab, and is the 2025 data a fresh sample? Ask the authors or find a third study.
4. How well does an LLM refuter work when given the code to run and a held-out checker (REFUTE with execution feedback, more than 9%)? Does a random-input baseline match it, as in Zendo?
5. Are there tests that measure severity itself (Mayo's "would the test probably have detected the flaw") for LLM checks, for example by planting known flaws and measuring detection rate?
6. After a failed test, how often does an LLM correctly assign blame between candidate, test and auxiliary assumption (Duhem-Quine problem)? No LLM study found.
7. Does self-generated hypothesis sampling (Batista and Griffiths) occur in agents that write their own tests, and does code-generated mutation remove it?
8. What are Wason's 1960 exact original figures and Ragni et al.'s redundancy meta-analysis numbers (both only second-hand)?
9. Do results from FalsifyBench and Failing-to-Falsify hold on the newest models (2026 frontier), or does the gap close with scale beyond 75%?
10. Does negative testing hurt when the hypothesis is broader than the target (Klayman and Ha), and should the agent first estimate H vs target relation before choosing test type?

## Gap search results
Evidence in evidence_d.jsonl (d01-d16). Claims K01, K05, K08, K09, K13, K16 updated; K21-K26 added.

1. Opposite-test step vs best-of-N at equal tokens: STAYED OPEN. No paper found. Nearest: REFUTE and POPPER (K26).
2. Causal role of incompatible testing: PARTLY CLOSED, against a simple story. With mode held fixed, Think-in-Opposites raised success in 11 of 11 cells, but I:C fell in 4 of 22 interventions (GPT-4o 0.25 to 0.17, success 0.11 to 0.16). So I:C is not the whole mechanism. No mediation or token-matched test exists (d08).
3. Independent replication of Branchini: STAYED OPEN. Nothing new found; search budget ran out before a targeted search.
4. REFUTE with execution feedback and random baseline: CLOSED. o3-mini ReAct 6.8-8.6% vs 8.9-9.3% prompting, so execution feedback does not help much; it removes invalid tests. Random generator without sight of the bad code broke 14% of 403 candidates, removed by design. Randomized search plus brute force found 6% extra submissions; 35% of its samples ended with a wrong counterexample, 86% of those from wrong brute-force code (d03). Correction: the 3% in K13 is extra submissions broken when the correct solution was given, not overall success.
5. Severity measured by planted flaws: PARTLY CLOSED. SWE-Mutation (2,636 mutants, 7 LLMs, detection 25-72%, agentic mutants 71.04% to 39.81%) and Hamidi et al. 2026 (detection near zero) measure it for test suites; no study does it for a single falsification step (d10, d11).
6. Blame assignment after a failed test: PARTLY CLOSED. No Duhem-Quine study. TRACE (7 LLMs, 3,192 instances) shows weak blame ranking for code faults (tau_b <= 0.10); Huang et al. show tests inherit code errors (d04, d05).
7. Self-generated sampling in agents: PARTLY CLOSED. Konstantinou et al. 2026: tests written after own faulty code detect about 14% vs about 25% from a fresh session. Code-generated mutation as a remedy was not tested for hypotheses; random draws worked in Batista and Griffiths (29.5% vs 5.9%) (d06, d07).
8. Wason 1960 and Ragni: CLOSED for Wason (full PDF read, exact numbers in d01; 6/29, 13, 9, 1; 1.79 vs 0.24). Ragni: abstract only, 228 experiments, 99 with redundant selections (d02); full paper not opened.
9. Newest frontier models: PARTLY CLOSED. FalsifyBench lists GPT-5.2-Chat 75% as top among 12 models; no Claude or Gemini frontier run (d09).
10. Klayman and Ha broader-hypothesis case for LLMs: STAYED OPEN. No new LLM study found.

Corrections from this pass: a snippet claiming HumanEval test accuracy 80% to 57% conflicts with the Huang abstract (+57%); not used (d14). Batista and Griffiths hypotheses were coded by Gemini 2.5 Flash-Lite, not the preregistered model. Web search budget ran out after 5 searches; Semantic Scholar and OpenAlex APIs were rate-limited and the arXiv API did not respond, so pages were fetched directly.
