# Critique: C03.09 Metacognition models (confidence and monitoring)

## Corrections made (numbers re-opened from source text this session)
Confirmed unchanged:
1. Xiong et al. (arXiv 2306.13063): average ECE above 0.377, GPT-4 AUROC 62.7%, +22.2% AUROC GPT-3 to GPT-4, GSM8K 93.6% accuracy with ECE 0.064, white-box vs black-box gap 0.522 to 0.605.
2. Kumaran et al. (2507.03120): change of mind 32.5% hidden vs 13.1% shown; 39.2% vs 85.0% with opposite advice.
3. Steyvers et al. (2401.13835): 301 participants, 284 retained; model AUC .751/.746/.781; human AUC .589/.602/.592.
4. Yoon et al. (2505.14489) ablation table, TriviaQA: original 0.042/0.782, minus epistemic markers 0.109/0.837, minus non-linear reasoning 0.161/0.734, no CoT 0.150/0.689. Minus confidence reasoning 0.063/0.763.
5. Prasad and Nguyen (2505.19184): 72.9% initial, 83.3% final, 61.7% both over 75%, 64.1% to 75.2%.
6. BrowseConf (2510.23458): 41.3/5.67 and 36.7/10 on BrowseComp; 53.33% in best bin; 30.0 reported vs 30.49 reproduced.
7. Dai and Wang (2603.09309): M-ratio 0.62 to 0.92 confirmed; 78.2 and 92.1 appear in the table.
8. Kapoor et al. (2406.08391): N=181, 20 per variant, confirmed. Mazancieux et al. (PMC7397761): N=181 also confirmed. This is a coincidence of two different studies, not a copy error.
9. Huang et al. (2310.01798): the figures are right, but the columns in the table are number of LLM calls (1, 3, 5), not "round 0/1/2" as b24 says. Fixed in claim K12.
Corrections to the evidence files (not edited in place, noted here):
- a03/b-series: a21 and b16 give "AUC .778 and .83" for different models; they are examples in one figure, not a benchmark.
- a14: per-task P(IK) numbers were garbled; do not cite them.
- c14: the "-0.80 rank correlation with accuracy" rests on 4 models. Treat as anecdote.

## Contradictions between sources
- Tian (2023) says verbalized beats token probabilities; Kapoor (2024) says prompted verbal methods lag fine-tuned probes and do not improve with model quality; Xiong says white-box and black-box are close. These agree only if the claim is limited to chat/RLHF models and prompted-vs-prompted comparisons. Model set and datasets differ.
- Xiong reports consistency lifting AUROC strongly (54.8 to 92.7, GSM8K); Kapoor says sampling gives good ECE but weak AUROC on open-ended MMLU. Boundary: answer type (numeric vs free text).
- Yoon: reasoning improves calibration; Huang: self-correction harms. They differ in what is asked (confidence vs answer revision), so not strictly in conflict.
- BrowseConf helps on BrowseComp but not on BrowseComp-zh.
- Tool effect: web search overconfidence is one study (c20).

## Weak spots
- Human foundation papers were not opened: Nelson and Narens, Koriat, Maniscalco and Lau, Fleming 2010, Pouget 2016, Dunning-Kruger (a07-a11, a24, b05). Their descriptions come from memory or secondary sources; Fleming 2010's "about 32 participants" is unverified.
- Mostly preprints: Luo and Jho 2026, Cacioli 2026, Dai and Wang 2026, Xuan 2026, Prasad 2025, Ou 2025 are single-source.
- Several LLM studies are on older models (GPT-3.5, GPT-4, Llama-2) and may not hold for current reasoning models.
- Almost no study measures confidence quality at equal token cost against a baseline of simply sampling more.
- No failed replication found for the human metacognition efficiency measures, but none was searched in depth; a Confidence Database check (b25) failed.

## Only seen in snippets or abstracts
b22 (Chhikara, 460% and 90% from the abstract), a25 (Griot), a11, a24, b05, b25. Steyvers and Peters AUC example numbers (a21) come from one figure.

## GAPS
1. Does verbalized confidence after reasoning beat confidence before reasoning at equal tokens for current reasoning models (not older GPT-3.5/4)?
2. At equal tokens, does k-sample agreement as confidence beat one answer plus self-reported confidence, and where does the crossover sit?
3. Does confidence-gated stopping or retry (BrowseConf-style) beat fixed-n resampling on tasks like the project's ARC and BrainTeaser benchmarks?
4. Does showing the agent its own earlier answer during review (choice-supportive bias) reduce accuracy of revise steps, and does masking it help?
5. What stated-confidence wording in the final answer improves a reader's AUC, and does it transfer to a model reader?
6. Is metacognitive efficiency (M-ratio) stable across tasks for the same LLM, i.e. is there an LLM domain-general metacognition factor?
7. Do evidence-gathering tools and verification tools change calibration in opposite directions in other studies (replication of Xuan 2026)?
8. What do the primary human sources (Maniscalco and Lau, Fleming 2010, Koriat 1997) report exactly, and have the meta-d' results replicated with large samples?
9. Does scale granularity (0-10, five-level verbal, probabilities) change AUROC on current models, as Dai and Wang suggest?
10. Do calibration gains from temperature scaling on a small dev set (n=250 in Luo and Jho) persist out of domain?

## Gap search results
Evidence in evidence_d.jsonl (d01-d19). Claims K08, K10, K11, K13, K14, K15 revised; K19-K25 added.

1. Verbalized confidence after reasoning vs before, current reasoning models: PARTLY CLOSED. No study isolates before vs after at equal tokens. Del 2026 (gpt-oss-20b, Qwen3-30B, DeepSeek-R1-8B) shows confidence stated with the answer matches a later judge pass (d03). Other work says longer thinking worsens calibration (d05, small d04) and that confidence ignores the trace (d18). K10 is now "contested". Still open: the direct before/after test.
2. k-sample agreement vs one answer plus confidence: CLOSED for k up to 8 on reasoning models (d01, d02). One confidence beats SC at equal small k (SC@2 63-70 AUROC vs VC@1 69-79). No crossover up to K=8. The best use of a second sample is hybrid: +12.9 AUROC in math at K=2, then about +2.7 and +1.5. Caveat: 3 mid-size open models, MMLU-Pro style tasks.
3. Confidence-gated stopping vs fixed n: PARTLY CLOSED. CAS, CGES and BrowseConf show 58% to 12x savings at equal accuracy (d07, d08, K13 now established). All on QA, math, search tasks; none on ARC or BrainTeaser; gates use RL-trained or token-level confidence. Needs a project test.
4. Choice-supportive bias in revise steps: PARTLY CLOSED. Bias confirmed and shown to vanish when the earlier answer is attributed to another LLM (31.3% vs 33.2%, d10). Accuracy effect of masking is not measured anywhere I found. AAAI-25 agent-memory paper seen only as a snippet (d11, opened false).
5. Wording that improves reader AUC: STAYED OPEN. Only a human study of hedges (Kim 2024, N=404, d12), no AUC, no model reader.
6. Domain-general LLM metacognition: CLOSED with a negative answer for now. Efficiency is domain-specific (Science and Tech weakest for all four models, d13); M-ratio is steadier across tasks within a model for 2 of 3 (d14), but three tasks and three models do not show a general factor. Correction to c14: in v3 the accuracy-efficiency rank link is -0.80 / 0.00 and the cross-model ordering changed.
7. Tools opposing effects (replication of Xuan): STAYED OPEN, now contested. No independent replication. A second paper (d05) finds retrieval helps confidence assessment, though its task differs. K14 -> contested.
8. Primary human sources: PARTLY CLOSED. Fleming 2010 opened: N=32 confirmed, Aroc 0.55-0.75, r=-0.11 with accuracy, split-half r=0.69 (d15). Rahnev 2024 gives the large-sample picture: M-ratio test-retest r .17-.42, split-half high (d16). Maniscalco and Lau 2012 and Koriat 1997 could not be opened (403); still secondary (d19). No direct large-sample replication of the 2010 brain-structure result was checked.
9. Scale granularity on current models: STAYED OPEN. Del 2026 used 1-100 only (d03). Nothing new on 0-10 vs verbal vs probability scales.
10. Temperature scaling on small dev set, out of domain: PARTLY CLOSED. Review shows recalibration is model-dependent (no gain for Llama 3.1 8B, d17), and calibration training shows ECE gain with AUROC loss OOD (d06). No test of Luo and Jho's n=250 map. K22 single-source.

New caution: the Cacioli preprint changed its headline between v1 and v3 because of a scorer bug (53% of one model's correct answers missed). Automatic scorers can flip conclusions in LLM metacognition work.
