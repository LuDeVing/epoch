# Critique and cross-check: F03.06 Epistemic diversity

Sources re-opened this session (arXiv PDF text via pdftotext, Thompson PDF): Li et al. 2502.00674, Kim et al. 2506.07962, Maryanskyy et al. 2603.20324, Hegazy 2410.12853, Wang et al. 2406.04692, Schoenegger et al. 2402.19379, Brown et al. 2407.21787, Kim et al. 2601.10825, Park et al. 2302.07267, Thompson 2014.

## Corrections made
1. a18/c04 (Maryanskyy): the headline win rate 0.810 (diverse + judge) and 0.929 (diverse mixed + judge) come from judges that also did the selection. With a decoupled panel of two independent judges the values fall to 0.611 and 0.726 (attenuation 53-67%); rank order kept (Spearman .90). The homogeneous cell is 0.500 under independent judging (all 756 verdicts ties). Treat 0.810 as an upper bound. The weak-model effect is exploratory, not pre-registered.
2. a14 (Li): the diversity coefficients carry the same se as quality in the table (MMLU 2.558 +- 0.176 vs 1.841 +- 0.176). Values confirmed. Note the R2 values (0.771, 0.685, 0.760) are from about 70 mixtures per dataset and are not independent of the quality measure used (Table 5 shows R2 changes with the quality definition).
3. a15/b17/c01 (Wang): confirmed 61.3 vs 56.7 at n=6. But the single-proposer row uses Qwen1.5-110B (56.7); in the same paper's Table 4 WizardLM-8x22B as a proposer scores 63.8, above 61.3. So the paper's own table already shows the best single proposer beating the mix. This reconciles MoA and Self-MoA (new claim K08).
4. b05/a10: Grim et al. were abstract-only, so their landscape-randomness result is second-hand.
5. c05/b24 (Choi et al.): I fetched arXiv 2502.08177 and it did not match; the numbers 0.7205/0.7691 were not re-verified. Marked single-source.
6. Duplicates: a13=b14=c02, a15=b17=c01, a16=b27, a20=b18, a21=b20=c06, a22=c09, a19=c14, c18 repeats a05/a06. Independent source counts in claims.jsonl count papers, not lines.
7. c24 is a synthesis by an agent, not a source; it was not used as evidence.
Confirmed unchanged: Hong-Page numbers (via Thompson, 131 vs 120, median of 200 random groups), Kim correlated errors (349 LLMs, 12,032 questions, 60%, 0.423), Hegazy (91% vs 82%, singles 78/64/70), Schoenegger (0.20 vs 0.19, p=.850; 0.17 to 0.14, p=.003), Brown (15.9% to 56%; 82.9% to 98.44%; 40.50% to 41.41%), Park (14 studies, 8 analysable, 37.5%, 99.6%), Kim 2026 (27.1% to 54.8%, 23.8%).

## Contradictions between sources
- MoA (diverse beats single) vs Self-MoA (single best beats mix): resolved partly by correction 3 and by Maryanskyy (selector quality) and Abdulaal (consistency gate, abstract only). Hegazy and ReConcile show cross-family gains when members are of similar quality; Li shows loss when one member is clearly best.
- Hong-Page (diversity trumps ability) vs Reijula-Kuorikoski, Thompson, Luan et al.: the effect appears only on unstructured landscapes with small ability differences (best vs worst agent 87.3 vs 84.3).
- Debate: Du et al. report large gains (arithmetic 67.0 to 81.8) while Choi, Smit, Zhang find voting or CoT matches it.
- Personas: Zheng et al. no gain, yet DIV-SE (approach diversity plus personas) gains large; the gain likely comes from approach choice, not persona.

## Weak spots
- Almost every LLM number comes from one benchmark family per paper and is single-run; no equal-token comparison in most papers (MoA uses more calls than one model).
- DIV-SE Graph Coloring 97 vs SC-10 23 is a huge gap on a task where the base prompt fails; likely a different-algorithm effect, not diversity per se.
- No LLM study isolates Hong-Page style diversity (different heuristics) from simple selection among samples.
- Human-team meta-analyses (Horwitz, Bell) have no effect sizes read.

## Only seen in snippets or abstracts
Weisberg-Muldoon 2009, Alexander et al. 2015, Lazer-Friedman 2007, Reijula-Kuorikoski 2019 listing, Page 2007, Grim et al. 2019 (abstract), Singer 2019, Kuehn 2017, Abdulaal et al. 2025, Wang et al. 2023 (self-consistency), Du et al. 2023 (partially), Horwitz, Bell. The 2025 approval-voting paper (b11) has unconfirmed authors.

## GAPS
1. At equal tokens, does N varied-approach attempts from one model beat N same-prompt samples AND beat the best single approach (DIV-SE style) on our benchmarks? No paper isolates this.
2. How much do varied attempts from one model overlap in errors (Kim style measure within one model), and do diversity operators lower it?
3. What selector quality is needed for diversity to pay, with only one model? Is self-verification good enough, or are tests and external checks required (Maryanskyy crossover)?
4. Which task structure predicts when diversity beats ability (stairway vs random landscapes) for LLM tasks, and can the agent detect it online?
5. Does early information sharing between attempts reduce diversity (Lazer-Friedman, O'Brien) in LLM agents, and does delaying sharing help at equal tokens?
6. Is Weisberg-Muldoon maverick (avoid explored ground) a useful operator for LLM search, given the contested modelling in Alexander et al.? Open the three papers.
7. Is the Choi et al. voting-beats-debate result reproduced with exact tables? Re-verify with the correct arXiv id.
8. Are there independent replications of Self-MoA beyond Li et al., especially with reasoning models where internal perspective diversity exists (Kim 2026)?
9. Do human team meta-analysis effect sizes (task-related diversity) give a prior for the size of the gain worth expecting?

## Gap search results

Evidence in evidence_d.jsonl (d01-d19). Opened this session: arXiv PDFs 2508.17536, 2606.27288, 2605.29116, 2602.03794, 2604.18005, 2505.11556, 2411.17501, 2506.18203, 2402.08115; Shore et al. 2015 (Harvard DASH PDF); Wallrich et al. 2024 (PDF). Blocked (403 or rejected): Alexander et al. full text, Lazer-Friedman 2007 full text, Weisberg-Muldoon 2009.

1. Equal tokens, varied approaches vs same-prompt samples vs best single approach: PARTLY CLOSED. One equal-call study (Fadnavis 2026, gpt-oss-120b, 7-11 calls) shows varied prompts plus a trace-reading aggregator beat self-consistency (GPQA +2.5, BBH-3 +6.1, LCB-Hard +5.3), but persona, paraphrase and strategy variants were the same (72.7, 72.7, 70.2), so designed approach variation is not shown to matter. No test against the best single approach on our benchmarks; still open for truly different algorithms (DIV-SE gap is untested for equal tokens).
2. Error overlap within one model: CLOSED in direction. Prompt variation leaves pairwise error correlation at about 0.6 (0.633 vs 0.603 GPQA; 0.571 vs 0.607 LCB-Hard); Self-MoA samples sit at 0.80 vs 0.42 across models at matched quality. Operators do not lower it. Whether stronger operators (meaning-changing, different algorithms) do was not tested.
3. Selector quality: MOSTLY CLOSED. Verifier false positives cap resampling and optimal K is often under 10 (Stroebl); self-critique can fall below plain prompting while a sound external check gives large gains (Stechly); weighted ensembles of weak verifiers reach 87.7 vs 72.2 for vote (Weaver). Answer: external tests or an ensemble of independent checkers are needed; one-model self-verification is not enough. The exact crossover point (Maryanskyy) was not re-measured.
4. Task structure that predicts diversity vs ability, and online detection: OPEN. Only indirect evidence: answer format changes the all-wrong share (MC vs free-response delta 0.127), and team meta-analysis effects are larger on complex and creative tasks. No detector found.
5. Early sharing between attempts: PARTLY CLOSED. LLM studies show dense interaction shrinks diversity (Vendi/N 1.03 to 0.47) and buries unique facts (30.1% vs 80.7%); human lab data show clustering raises convergence on wrong answers. No equal-token accuracy test of delayed sharing exists; Lazer-Friedman not opened.
6. Weisberg-Muldoon maverick operator: STAYS OPEN. Full texts of all three papers were blocked; only the Alexander et al. abstract was read. Keep K19 contested.
7. Choi et al.: CLOSED. Correct id is 2508.17536. Table verified: Qwen2.5-7B single 0.7205, best MAD 0.7377, vote 0.7691; Llama3.1-8B single 0.6203, best MAD 0.6990, vote 0.7242. K14 upgraded to established.
8. Self-MoA replications: PARTLY CLOSED. Two 2026 studies give mixed results: a mix of models beats Self-MoA by about +0.027 at matched quality (Chen), while Self-MoA fell below zero-shot on GPQA but was strong on AIME (Fadnavis). No independent reasoning-model replication with the original protocol. K06 changed to contested.
9. Human meta-analysis prior: CLOSED. Task-related diversity r about .04 to .10; all averages |r|<.1 in the 2024 registered report (615 reports); larger for R&D (.058 vs .020) and creativity outcomes (.056 vs .020). Expect small gains. Original effect-size tables for Horwitz, Bell, van Dijk were read only through the Wallrich summary table.

New caveats: many 2026 preprints are single-run with the authors' own method and small n (GPQA n=198, Formal Logic 126 questions). Yang et al.'s heterogeneity mixes models, prompts and tools, and its near-zero gpt-5-mini baseline looks like a format artifact.
