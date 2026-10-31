# Critique: Case-based reasoning in law (E11.05)

## Re-opened sources and corrections
Opened full text of arXiv 2510.08710 (Thinking Longer), 2610.28799 (Where Do Legal Factors Live), 2508.16153 (Memento), 2404.04302 (CBR-RAG), 2401.01301 (Large Legal Fictions), 2306.13906 (GPT-4 and case-law sentences).
- CONFIRMED: Task 1 100%; Task 2 64.82% to 92.09%; Task 3 11.46% to 33.99%; qwen3 78.66% vs 30.04% (Task 3 33.99% vs 0.00%); 253 instances; gpt-5 4,456 vs 3,081 tokens (45% more); 3,189 vs 9,596 tokens (3.0-fold).
- CORRECTION: file c (c01 to c04, c22) names the authors "Li et al."; the authors are Li Zhang, Grabmair, Gray, Ashley (Li is a given name). Cite as Zhang et al.
- CORRECTION: the paper's token table has misaligned model labels in text extraction (rows show gpt-5 with 78.66 and "non-thinking" with 92.09). Trust the prose: gpt-5 = 92.09% at 3,189 tokens; qwen3-thinking = 78.66% at 9,596. c03's "gemini-pro 5,144 for 64.82%" conflicts with prose giving 64.82% to gemini-flash; treat that pairing as unverified.
- CONFIRMED: Where Do Legal Factors Live: AUC 0.86 to 1.00, medians 0.961/0.972/0.961, train 3,932, test 3,961, audit of 220 passages (paper dated Oct 2026).
- CONFIRMED: Memento 87.88% Pass@3 val, 79.40% test, +4.7 to 9.6 points; CBR-RAG 0.8967 to 0.9141, +1.94%, 2,124 pairs, 57% with no act reference; Dahl 58% to 88%, at least 49%; Savelka F1 .53, .52, .51, .57.
- Not re-opened: ExpeL tables (garbled), COLIEE tables, Suttle and Lillis, Magesh, Wu et al.

## Contradictions and weak spots
- Almost all strong numbers on HYPO/CATO-style reasoning come from one group (Zhang, Ashley et al.) on synthetic CATO factor sets in one domain (trade secret). Independence is low.
- Factors are given to models in most tests; extraction from text is a separate weak step (F1 .5 to .6, MCC .3 to .5).
- The classic symbolic results (HYPO, CATO, IBP, Aleven teaching test) were never opened: a22, a23, b22, b23 are recalled. Do not cite 91% / 186 cases until checked.
- Thinking vs non-thinking is confounded with RL post-training, one model family.
- CBR-RAG gain is small, measured by embedding cosine on LLM-made questions; no correctness metric.
- Memento and ExpeL are general agent memory, not legal precedent; transfer to law is by analogy.
- Web search quota ran out in file c; 2020-2026 LLM studies on HYPO/CATO may be missing.
- No human-psychology studies of how lawyers or judges reason from precedent are in the evidence.

## GAPS
1. Does the Task 3 collapse (identifying significant distinctions) also appear with real opinions and with factors that must be extracted, and does a scaffold (extract factors, compare, verify) lift it at equal tokens?
2. What do the original IBP, CATO and Aleven evaluations report (accuracy, sample, baseline)? Open them.
3. Does retrieving case text before citation cut hallucinated or wrong-holding citations, and by how much, with correctness grading?
4. What number of retrieved cases (K) is best for reasoning tasks, and is distilled rule memory better than raw case memory? Memento and ExpeL disagree by task.
5. Is LLM persuadability and sycophancy toward cited authority reduced by a forced steelman of the opposing side? Read Molfetta et al. in full.
6. Are there independent replications of the Zhang et al. factor benchmarks outside Pittsburgh?
7. Do human studies exist on how lawyers and judges use analogy to precedent (anchoring on the first case, framing)?
8. Is decodable factor structure in hidden layers causally used (ablation or steering), or only correlated?
9. Does thinking-token length predict error well enough to act as a stop or re-check trigger across models?
10. Which 2020-2026 prompting-level studies test explicit analogise/distinguish moves against plain similarity on chat LLMs?

## Gap search results (evidence_d.jsonl, claims K21-K29)
Conditions: the WebSearch budget was used up, and the arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429, so discovery of new papers was not possible. Only papers with known IDs were opened (pdftotext on fetched PDFs). D: drive does not exist on this machine, so nothing was saved to D:. Springer, Elsevier, ACM, ResearchGate and Cornell PDFs gave 403 or login redirects.

- Gap 1 (Task 3 collapse on real opinions; scaffold at equal tokens): OPEN. Zhang and Ashley's own limitations section says real judicial opinions are the next step (d07). LePREC (d08, abstract only) shows LLM factor extraction plus a linear scorer on 769 real cases, but a different task.
- Gap 2 (original IBP, CATO, Aleven evaluations): OPEN. All routes were paywalled or blocked. K20 stays unverified; do not cite 91% / 186 cases.
- Gap 3 (read text before citing): PARTLY CLOSED. Magesh et al. (d01, d02): legal RAG tools hallucinate 17% to 33% against about 43% closed-book GPT-4 on 202 queries. No controlled read-then-cite ablation found. Misgrounding is the residue.
- Gap 4 (best K; rules vs cases): PARTLY CLOSED. Few cases is enough (Yasunaga K=3 to 5, d12; Memento K=4 vs 32 from file c). ExpeL (d13, d14): insights beat cases on HotpotQA (36 vs 31) and lose on ALFWorld (50 vs 55); relevance of retrieved cases is the main lever (59.0 vs 42.5 random). No legal-domain test.
- Gap 5 (steelman vs sycophancy): OPEN. Molfetta et al. read in full (d03, d04): statutes not precedent, multiple choice, zero-shot, no mitigation tested. Larger reasoning models defer more to false context.
- Gap 6 (independent replication of Zhang et al.): OPEN. No replication found. LePREC and ACAL (d08, d09) are different tasks from different groups, abstract pages only.
- Gap 7 (human studies on lawyers and judges): OPEN. Guthrie, Rachlinski and Wistrich (2001) and Englich et al. (2006) were targeted; PDFs returned 403. Nothing opened.
- Gap 8 (causal use of factor structure): OPEN, confirmed absent. Authors list intervention as future work (d07).
- Gap 9 (token length as trigger): PARTLY CLOSED. Hassid et al. (d05, d06): shortest of several samples beats longest by up to 34.5 points; works within a question, not across questions. Supports a relative-length trigger. Not tested on legal tasks.
- Gap 10 (analogise/distinguish prompting vs plain similarity): OPEN. Closest found: Yu et al. legal prompting on statute entailment (d10) and Yasunaga analogical prompting on math (d11). No case-pair test.

New caveats: d01 hallucination values per tool were read from a figure with garbled labels. d08 and d09 are abstract-page reads only. d12 K table was only partly read. d16 has no numbers.
