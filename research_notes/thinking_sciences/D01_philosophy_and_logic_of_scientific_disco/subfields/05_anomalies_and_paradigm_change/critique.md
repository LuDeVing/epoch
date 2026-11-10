# Critique: D01.05 Anomalies and paradigm change (cross-check)

## Numbers re-opened this session (source text read)
Confirmed with no change:
- Fugelsang et al. 2004 (b01, b02): 12 meetings, 28 projects, 165 experiments, 417 results, 223 inconsistent, 196 method explanations, 27 theory changes (12%), 61% theory change after replication (84 replications; 51/84 = 61%).
- Dunbar 1997 chapter (a11): 6 experiments, 70 conditions, 22 expected / 18 unexpected / 30 exploratory; 23 vs 176 group interactions; 8 of 10 inconsistent surprises gave new hypotheses. The 33 vs 161 reasoning-block counts sit in Table 4, which the text extraction did not show, so they were not re-checked.
- Trickett et al. 2001 (b04): t(28)=2.33; 27 astronomy and 9 physics noticings; 7.6 vs 1.5 and 3.0 vs 1.25 later references. Only 3 scientists. The extracted table labels are misaligned, so row assignment rests on the text ("over 3 times" astronomy, "more than twice" physics).
- Huang et al. 2024 (b21, c07, c08): GPT-3.5 CSQA 75.8 to 38.1; GSM8K 75.9 to 75.1 to 74.7; GPT-4-Turbo 91.5, 88.0, 90.0; oracle GSM8K 95.5 / 97.5.
- EvoSCM (a19-a21, b17, c18-c19): 51.64 to 75.09; pass@1 7.27 to 56.36; ablations 48.18 / 47.45; K=1 63.27, K=4 74.86, K=6 75.09; transfer 57.64 / 62.55 / 74.00.
- DiscoverPhysics (a17): 22 worlds, MSE below 0.1 pass rule, best two models pass about half.
- FalsifyBench (c16, c17): 41%, 75%, 68%, 12%, 21% and the confirmation-bias figures 39.0 / 27.3 present.
- NewtonBench (a23): 324 tasks, 108 shifted laws, 75.9% and 65.4%.
- Rios-Garcia et al. 2026 (b13): 25,000+ runs, 68%, 71%, 26%, 53%, 63%, 7%.

## Corrections
1. c15 describes the Rios-Garcia result as "619 chemistry tasks, three LLMs", taken from a news article. The paper itself reports 25,000+ runs over many environment scopes (b13). The 68% and 26% figures are per trace over the whole benchmark. Treat c15 as a secondary, partial description; do not count it as an independent source.
2. b13 / b14 / b27 / c15 are one study, not four. Same for Huang (b21, c07, c08), DiscoveryWorld (a25, b22, c04-c06), EvoSCM (a19-a21, b17, c18, c19) and DiscoverPhysics (a17, a18, b15, b16). Claims count these once.
3. Huang: "74.7%" is two different things. Text: GPT-3.5 keeps its first GSM8K answer 74.7% of the time. Table 3: round-2 GSM8K accuracy is also 74.7. Both are real; do not merge them. Also oracle numbers are inflated by stopping when correct, which the paper notes.
4. a28 compares "4 of 32 vs 6 of 10" and "8 of 10". The 4/32 figure and the 6/10 figure come from Chinn and Brewer 1993 (a07), which could not be re-opened (escholarship returned an HTML page, not the PDF). Unverified.

## Contradictions and tensions
- Experts (Dunbar, Trickett: attend to anomalies) vs students (Chinn and Brewer, Brewer and Chinn: discount them). Fugelsang's own lab study shows both: 12% theory change at first clash, 61% after replication. These are not contradictory once timing is tracked, but samples are very different (3 labs, 3 scientists, vs 64-72 undergraduates).
- Dunbar counts "unexpected" findings that are consistent with the hypothesis (8 of 18), so "attention to unexpected" is not the same as "attention to contradiction". Only 10 of 18 were inconsistent.
- Fugelsang: 88% of inconsistent results got method explanations. Dunbar: little explaining away. Different labs and coding schemes.
- Gershman (b10): shielding with auxiliaries can be rational. Chinn and Brewer, EvoSCM: treat non-revision as a failure. Not reconciled; no measured agent test.
- NewtonBench says tools hurt strong models; EvoSCM says structure helps. Different mechanisms (premature exploitation vs hypothesis population), not directly contradictory.

## Weak spots
- Kuhn is a historical and interpretive account. There is no counted effect in this folder for the oxygen case itself; no primary source on Lavoisier, Priestley or Scheele was opened (b28). Critiques of Kuhn's oxygen story are missing.
- Almost all LLM evidence is 2026 and on three benchmarks (DiscoverPhysics, EvoSCM on it, NewtonBench). Several are single-lab preprints. EvoSCM compares at unequal token cost.
- Nothing tests a paradigm-level reframe in an LLM (c25). Belief-revision proxies stand in.
- Haq et al. (c20) has no accuracy figures extracted.

## Seen only in snippets or not opened
a04 (Bruner and Postman, via Kuhn), a09, a16 (Darden), a26 / b08 / b09 (Chinn and Brewer review and 1998 test), b06 (fMRI), b12, b24 (WILT; FalsifyBench summary), b25, b26, b29, c21-c24 (from memory), plus a07 / a28 numbers.

## GAPS
1. Does any LLM study measure frame change (not parameter refit) when a held frame is wrong, with a clean contrast of structure-adding vs parameter-adding fixes? DiscoverPhysics hidden-source worlds look closest; are per-world pass rates and failure counts available?
2. What does EvoSCM's gain cost at equal tokens? Rerun or find equal-budget numbers for the population, pre-commit and discriminating-experiment parts separately.
3. What impasse trigger works for an LLM without an external oracle: residual threshold, repeated-failure count, or prediction-error log? No measured comparison found.
4. Is the Fugelsang pattern (hold on first clash, revise after replication) better for an agent than reframe-at-first-clash? Test on injected anomalies with noise, where some anomalies are artefacts.
5. What are the exact Chinn and Brewer numbers (1993 Cogsci and 1998 test): sample sizes, response frequencies, and which factors (alternative theory, data credibility) moved theory change?
6. Is there a replication or failed replication of Dunbar 1995/1997 and Trickett 2001 with other fields or computational scientists, and of Bruner and Postman 1949 (card anomalies)?
7. How do historians of chemistry (e.g. critiques of Kuhn's oxygen account, Priestley vs Lavoisier) change the claim that discovery needs an anomaly first? What is the best primary-source check?
8. Does a forced "propose one new entity" or "name an alternative frame first" step raise LLM reframe rate, and does it raise false reframes?
9. How often are LLM surprise signals (Bayesian surprise) already implied by logged results, and does a derivability check cut wasted reframes?
10. Do LLMs show Bruner-Postman style normalisation of contradictory items in familiar templates, and what prompt removes it?


## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d17). Claims K02, K03, K04, K05, K06, K07, K08, K09, K12, K15 and K18 got extra evidence ids; K19 to K24 are new. Limits of this pass: arXiv, OpenAlex and Semantic Scholar APIs returned 429, and the shared WebSearch budget ran out after 3 queries, so negatives below are thin.

1. Frame change vs parameter refit: PARTLY CLOSED. DiscoverPhysics Appendix F (d01, d02): of 50 failed runs by the two best models, 15 (Opus 6, GPT-5.5 9) were "never considered the right kind of law", the top cause; it was implicated in all four worlds where both models fail. Self-monitoring failures were 10 of 50. Per-world pass rates are in a heatmap only, and the failure labelling was done by Opus 4.7 itself. No controlled structure-fix vs parameter-fix contrast exists (K09, K20, K21).
2. EvoSCM cost at equal tokens: PARTLY CLOSED. Parts are ablated separately (d04, d05): free-text hypotheses 48.18%, random experiments 47.45%, no pre-committed prediction 63.47%, full 75.09%; K=1 63.27%, K=4 74.86%. Runs are matched on rounds and capped on episodes, not on tokens; token use is only in a bar chart. Equal-token rerun still missing (K22).
3. Impasse trigger without oracle: OPEN. No comparison found. Traces show ignored signals (plateaued refits, 6.7-fold residual excess) (d02, K20). Needs our own ablation.
4. Fugelsang hold-then-replicate vs reframe-at-first-clash: OPEN, but a test bed now exists. DISCERN (d06, d07) elicits the prior before evidence and has 8 real controls; models either commit (Kimi 92.3%) or abstain (Astra 100%), and only 29.7% of clean controls were accepted. No study of hold-versus-reframe policies (K19).
5. Chinn and Brewer exact numbers: OPEN. Only the ERIC record (seven responses tested, one added) and the 1994 PSA page confirmed (d13, d14). The 4/32 and 6/10 figures stay unverified; full text 403.
6. Replications of Dunbar, Trickett, Bruner and Postman: PARTLY CLOSED. Alberdi, Sleeman and Korpi 2000 (5 botanists) points the same way (d12); Trickett 2001 is N = 3 (d11). No computational-scientist replication. Bruner and Postman figures (114 ms vs 28 ms, 10% fail at 1 s) now known second-hand from Schindler 2024 (d10); no replication found.
7. Historians on the oxygen case: PARTLY CLOSED. Hudson 2001 via Schindler 2024 (d09): Priestley counts as discoverer without the right theory; X-rays came by accident. Anomaly-first is one route (K24). Primary-source check (Priestley 1775, Lavoisier memoirs, Scheele notebooks) not done.
8. Forced "propose one new entity" step: OPEN. Nothing found. Warning sign: HypoArena (d17) shows structured-skill prompts moving ratings from +88 to about -58 depending on model.
9. Bayesian surprise already implied by logs / derivability check: OPEN. Nothing new beyond K15.
10. Bruner-Postman normalisation in LLMs: PARTLY CLOSED. Wu et al. 2024 (d15): GPT-4 drops on altered default conditions even when the change is stated; few-shot CoT narrows but does not close it. No test of unannounced contradictions and no prompt that removes it.

Recommended next steps: (a) open the Chinn and Brewer 1998 PDF through a library; (b) run our own trigger ablation (gap 3) and hold-vs-reframe test on DISCERN-style dossiers (gap 4); (c) read the 1949 Bruner and Postman paper.
