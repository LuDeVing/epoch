# E18.09 Resource-rational analysis: cross-check critique

## Re-opened (arXiv PDFs, text extracted this session)
Confirmed: De Sabbata RaM (2410.05563: 63.5 vs 61.9 vs 34.8 CoT-few; 146.2 tokens; cost 0.1; 50.3% easy-hard gap; MMLU-CF); Chen overthinking (2412.21187: 1,953%, 48.6%); Snell (2408.03314: about 4x less compute, 14x model); AdaptThink (2505.13417: -53%, +2.4%, -50.9/-63.5/-44.7); s1 (2501.19393: 50% to 57% AIME24, 53.3 vs 56.7 by Wait count); Sleep-time (2504.13171: +13%/+18%); Hassid (2505.17813: 34.5%, 40%); Liu et al. (2406.17055: 0.94 vs 0.48).

## Corrections and reconciliations
- Liu et al.: b25 says 13,006 problems, c22 says 9,831. Both right: 13,006 in choices13k; 9,831 non-ambiguous used in analysis. Use 9,831 for the analysis N.
- s1 AIME24: b20 "50 to 57" (up to 4x Wait, 56.7) and c08 "53.3 with 2x Wait" are the same curve at different Wait counts, not a conflict.
- BMPS 99.1%: a22 calls it the tree domain, b11 a Bernoulli metalevel task, c05 a Bernoulli tree. Treat as the Bernoulli metalevel task; label is inconsistent across lines.
- a25 "23-45% fewer tokens across three models" vs b12/c02 "23-32% vs STaR, 35-42% vs few-shot": the 45 comes from a third model; use per-model figures.
- RaM instruct-CoT baseline: c02 shows Instruct CoT 53.2 on 3B, above RaM 50.1. Accuracy was not better than that baseline for 3B; the claim holds only against STaR and few-shot CoT. Do not overstate.
- TALE (c12): accuracy fell 83.75 to 81.03 overall; "small accuracy cost" is fair, "no cost" is not.

## Contradictions and weak spots
- Several tokens-saved claims come from one author group (Griffiths lab) or one paper; K02, K06, K07, K08 are single-source.
- a05 and b02 (86% and 55%) are the same review passage, not independent; the primary Callaway planning paper was not opened.
- Anchoring (K04): fitted adjustment counts 8 vs 29 across datasets show the cost parameters are free; this supports the critics (b07), who say the approach is hard to falsify.
- Test-time scaling papers (DEER, Snell, s1) are engineering results; they do not test resource-rationality and are used here as a proxy for value-of-computation.
- Benchmarks differ (math-heavy); no evidence yet on open-ended or agentic tasks except R3-Bench.
- Training-based methods (RaM, L1, AdaptThink, O1-Pruner) need weights; our scaffold cannot use them directly. Only prompt-level and stopping-rule results (TALE, DEER, Adaptive-Consistency, probes) transfer.

## Only seen in snippets or not opened
a16 (Lieder & Griffiths 2017 full paper), a30 (Sprague meta-analysis, secondhand), a31 (Russell & Wefald 1991), c26 (the BBS paper itself not read in c; read in a/b). Lieder 2014 sorting numbers (N=100, 83%) and Vul 2014 re-analysis were not re-opened by me (NIPS/PNAS PDFs not fetched).
Not found: any independent failed replication of the strategy-selection experiments.

## GAPS
1. Does a cheap difficulty predictor (first-pass confidence, length, or probe) gate S0 well enough at equal tokens on mixed non-math tasks, or does gate overhead eat the savings?
2. Have the Lieder/Griffiths strategy-selection and anchoring results been independently replicated, or failed to replicate, outside their lab? (Search for replications 2019-2026.)
3. How much of the early-exit and shortest-chain gain survives on agentic and open-ended tasks, not only math and GPQA?
4. What stopping rule is best for the scaffold: Adaptive-Consistency (Bayesian), DEER (confidence probe), or VOC-threshold, at the same token budget?
5. Can a prompt-only budget (TALE-style) without training avoid the token-elasticity backfire, and where is the elasticity point for our model?
6. How do LLM-failure results (R3-Bench oracle gap, overthinking) change for models with budget awareness, and does a shared-budget allocator close the 71/72 oracle gap?
7. What is the human evidence for the planning figures (86%, 55%) in the primary Callaway paper, and what are the sample sizes?
8. Are resource-rational cost parameters measurable independently (time, error, effort) so a gate can be pre-registered without post hoc fitting?
9. Does sleep-time or offline precomputation (K18) pay back when queries vary widely, compared with online gating?
10. Does metareasoning overhead (VOC estimation) ever exceed its savings for LLM agents, given the BMPS finding that it pays only when object-level cost greatly exceeds it?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d16, all opened this session; d13-d16 are abstract-level reads). Claims K05, K14, K15 changed; K19-K25 added. Web search quota was exhausted, so searching used arXiv, Europe PMC and OSF APIs.

1. Cheap difficulty predictor at equal tokens on mixed tasks: PARTLY OPEN. Gates work inside a domain (probe 24% fewer tokens, d05; one-token self-check on AlpacaEval and GSM8K, d09) but need training, and the probe fails across domains. Gate overhead is real (DEER latency saving 27.9-40.1% vs token saving; DeepConf 16-trace warm-up, d04, d11). No zero-shot gate was tested on mixed non-math tasks at equal total tokens. Needs our own test (K19).
2. Replication of Lieder/Griffiths: STILL OPEN. No independent replication or failed replication of the cost-sensitivity results was found for 2019-2026. Nearest: Xie and Moss 2025 (N=144) replicates a different strategy-selection theory (d14); Warwick group builds on sampling and argues constraints are unsettled (d15). Treat K02 and K04 as single-lab.
3. Agentic and open-ended tasks: PARTLY CLOSED. Early exit does not carry over as plain "think less": low effort raised overthinking 35% in SWE agents, but picking the lower-overthinking of 2 cheap runs matched high effort at 57% of the cost (d03). Open-ended chat gating works after training (d09); TALE saves about 60% tokens on code summary and empathetic reply at comparable BLEU (d06). Shortest-chain gain on agentic tasks was not measured.
4. Best stopping rule at equal tokens: OPEN. Beta rule beats entropy and majority rules at equal cost (d10), DeepConf and DEER beat fixed-N votes (d04, d11), but no paper compares all three against a value-of-computation threshold (K22). Experiment to run.
5. Prompt-only budget and elasticity: PARTLY CLOSED. Budget in the prompt helps in a band, fails on hard items (DEER on AIME24, d11), and TALE's estimator is in range 60.61% of the time (d06). A budget display for agents works without training (d12). Elasticity point for our model must be measured by a sweep (d16 supports per-model optimum).
6. Oracle gap and budget-aware models: PARTLY CLOSED. Second independent source confirms the failure (d01, 7 models). A trained 1.5B solve-or-skip model closes most of the gap on 3-problem papers (Hard-512 0.15 to 0.93, d02), but prompting alone does not (planning prompt left priorities unchanged, d01). Whether a scaffold-side allocator closes the 71/72 gap is untested.
7. Callaway primary sample sizes: CLOSED, with a correction. Primary paper read (d07): 95, 298, 291 and 93 analysed in Exp 1-4. The 86% and 55% figures are NOT in it; K05 downgraded to contested and rewritten with the real numbers (0.92 points below Pareto front, 81.5% best-first, 45 vs 41 best fit).
8. Independent measurement of cost parameters: PARTLY CLOSED. Lieder et al. 2018 manipulated time and error costs experimentally rather than fitting them (d13), so pre-registered cost settings are possible. Sample sizes not read; no independent replication.
9. Sleep-time pay-back: CLOSED for the tested case. Pays when many related, predictable queries share a context (2.5x cheaper per query at 10 queries, gap grows with predictability); weak with few or unpredictable queries (d08). Untested on widely varying real queries.
10. VOC-estimation overhead for LLM agents: PARTLY CLOSED. Stopping-rule compute is negligible (0.03 ms, d10); learned estimators and trial answers carry real cost (d11, d04, d06 extra query). No direct measure of net savings after estimator cost on agent tasks. BMPS caveat stands.

Still-open list for the next round: (a) equal-token comparison of three stopping rules, (b) zero-shot gate on mixed non-math tasks including its own tokens, (c) scaffold-side shared-budget allocator versus prompt-only planner, (d) independent replication of strategy-selection and anchoring cost effects, (e) full texts of Lieder 2018 and Vul 2014 for N.
Caveats: d16 and d13-d15 were read at abstract level. d07 mapping of the 319-person sample to Exp 3 is inferred from the methods order. Cuadron trajectory counts differ between abstract (4018) and body (3,908).
