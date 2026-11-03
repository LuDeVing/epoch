# Critique: Coherence norms and Dutch book arguments (D02.02)

## Numbers re-opened and checked (this session, full text)
1. Fluri, Paleka, Tramer (arXiv 2306.09983), table of strong violations: GPT-3.5 negation 52.6% (mean 0.34), paraphrase 30.8% (0.21), monotonicity 42.0%, Bayes 68.6% (0.28); GPT-4 10.9% (0.10), 12.5% (0.13), 16.0%, 58.8% (0.25). CONFIRMED.
2. Same paper, prompting table: GPT-4 negation prompting 2.9% negation, 17.3% paraphrase, 68.6% Bayes. CONFIRMED. GPT-3.5 negation prompting 37.1%, paraphrase 41.3%, Bayes 51.0% (a13 omitted the Bayes figure). GPT-3.5 paraphrase prompting: paraphrase 37.5%, Bayes 45.1%. CONFIRMED (c10). Note: a13/b13 and c10 are about two different prompts; both are right. Not a conflict, but one must not say "GPT-3.5 paraphrase 30.8 to 37.5" under negation prompting.
3. Paleka et al. (arXiv 2412.18544) correlation table: Cond 0.92 (arbitrage) / 0.87 (frequentist); Aggregated 0.62 / 0.85 on scraped set; NewsAPI Cond 0.71, Aggregated 0.49 / 0.66; Negation 0.60 scraped but -0.36 NewsAPI; Or -0.24 NewsAPI. CONFIRMED.
4. Andrews and Sarkar (arXiv 2609.02797): baseline profit 0.002067 per unit stake, CI [0.001471, 0.002737]; 365,100 elicitations; 0.002067 to 0.1994 (about 100x); Brier 0.1966 to 0.2157; Spearman 0.9143; 101 of 105 pairs vs 32 for Brier; joint cells +0.00244 [0.001971, 0.002961]; 95 percent of answers identical over five passes. All CONFIRMED.
5. Mandel, Karvetski, Dhami (2018, JDM, open access PDF): control sum M=1.54 [1.33,1.76], ACH 1.77 [1.56,1.97]; MAE 0.23 to 0.15, d=0.96, t(49)=6.77; averaged 0.09; random coherentized 0.21; ACH share of error from sum violation .73 vs .50; d=0.69 control, 1.37 ACH; normalisation 0.13 vs coherentization 0.15. CONFIRMED.
6. Zhu and Griffiths (arXiv 2401.16646): 24 event pairs (12 weather, 12 politics), 4 LLMs, both temperatures. CONFIRMED (structure; per-identity numbers not re-extracted).
7. Zhu, Sanborn, Chater (2020) percentages: 40/59 = 67.8%, 18/59 = 30.5%, 1/59 = 1.7%, 52/84 = 61.9%. Arithmetic CONFIRMED; sample sizes not re-opened.
8. Redelmeier et al. (1995): 14+26+55+69 = 164 CONFIRMED arithmetically; not re-opened (no free full text found quickly).

## Corrections and cautions
- a25 and b18 say d=0.96 for the coherentization effect; the same d=0.96 appears in the paper for the control-group sum exceeding 1 (t[24]=13.63). Two different effects with the same d. Cite carefully.
- Mandel et al. found plain normalisation (MAE 0.13) beat their coherentization (0.15). a25 headlines the 35% cut; the cheaper method is as good or better. Claim K06 records this.
- a25 "chance after coherentizing MAE 0.21": it is a random-response baseline, so coherentizing alone does not create accuracy.
- ACH raw MAE was worse (0.26 vs 0.21, p=.14, not significant), so "ACH hurt" is a trend, not established; the sum-violation share difference (.73 vs .50, p=.04) is the firmer result.
- c16: "kill threshold 0.05 fired" means incoherence was too small to matter at median; it does not mean the models were coherent per proposition (25% of propositions at 1.5B had profit above 0.25).
- b21 (coherence weighting +30%) is second-hand; keep status single-source.

## Contradictions between sources
- Zhu and Griffiths (LLMs incoherent in a sampling-bias pattern) vs Dragonevskiy (small models nearly coherent on median): different tasks, formats, model sizes.
- Fluri et al.: consistency prompting helps one axis, hurts others; Paleka et al.: training on arbitrage gives no accuracy gain; Kotawala: coupling-visible elicitation helps. Elicitation format may work where instructions do not. Not tested head to head.
- Bayesian Sampler wins overall but several Exp 2 identity tests were null.

## Weak spots
- Almost all LLM evidence is on forecasting or event-probability questions, not on the multiple-choice or answer-choice use of our guardrail (sum to 1 over exclusive answers).
- Andrews and Sarkar, Kotawala, Dragonevskiy, Filbry et al., Williamson et al. are 2026 preprints, single-group, not independently replicated. Status stays single-source.
- Accuracy-dominance (K03) rests on one review (a09); the original proofs (Joyce 1998, Leitgeb and Pettigrew 2010) not opened.
- Dutch book critiques (Hajek, Christensen) are only via SEP text.

## Only seen in snippets or second-hand
a04 (de Finetti), a28 (Tversky and Koehler), a29 (Hajek), b21, b26, b27, c21 to c26 (no numbers). Redelmeier numbers were taken from the earlier evidence, not re-opened.

## GAPS
1. Does forcing sum-to-one (normalise or one-shot partition prompt) over exclusive answer options improve accuracy or calibration of an LLM at equal tokens on multiple-choice items, versus independent per-option probabilities? No LLM study found measures this directly.
2. Is plain renormalisation enough, or does a coherence projection (least-squares, as in Mandel et al.) add anything for LLM samples?
3. Does the sum of per-option probabilities (the raw violation) predict correctness per item, so it can act as a free uncertainty or stop signal? Paleka et al. show this is check-dependent.
4. Does listing an explicit residual option ("none of the above") remove the unpacking inflation seen in humans (Redelmeier, Tversky and Koehler) in LLMs?
5. Does reasoning (chain-of-thought, thinking tokens) reduce incoherence at equal tokens versus resampling? Evidence on vNM (Tak et al.) and Bayes updates (Filbry et al.) suggests yes; for probability identities it is untested.
6. Do the irrelevant-context effects (Andrews and Sarkar) apply to long agent contexts, i.e. does incoherence grow with scaffold length and memory load?
7. Which version of the Dutch book argument (pragmatic, depragmatized, accuracy) is the right justification when the agent is not a bettor, and does the choice change any guardrail design?
8. Can coherence-based weighting of multiple samples (Predd et al.) be reproduced with LLM samples? The +30% figure is second-hand.
9. Are fine-tuned or prompt-based anti-exploitability gains robust, given the collapse to uninformative equilibria in Dragonevskiy (half the runs)?
10. Do diachronic Dutch book results (conditionalization, Teller/Lewis) predict LLM update failures better than one-shot identities do (Filbry et al., Imran et al.)?

## Gap search results
Search tools were mostly blocked in this pass (web search budget used up; arXiv, Semantic Scholar and OpenAlex APIs rate-limited). Work was done by opening PDFs and SEP pages directly. Evidence is in evidence_d.jsonl (d01 to d15; d15 is a status line, not evidence).

- Gap 1: PARTLY CLOSED. No study compares forced sum-to-one against independent per-option probabilities at equal tokens. Indirect evidence agrees: joint options beat cloze scoring on 16 of 20 datasets, mean +9.7 points (d10); constraining mass to valid option tokens by prefilling gives +3.4 to +25.9 accuracy points and better calibration (d03); renormalised max probability predicts correctness but is not calibrated (d01). New claims K27, K28.
- Gap 2: PARTLY CLOSED. Plain renormalisation leaves option-ID bias; prior correction (PriDe) and contextual calibration add accuracy (d04, d05). A least-squares coherence projection on LLM samples is still untested. Claim K29.
- Gap 3: OPEN. The max renormalised probability predicts correctness (d01, d02), but the raw sum of independent per-option probabilities was not measured as a signal (d14). Stays check-dependent per Paleka et al.
- Gap 4: CLOSED in direction. Explicit residual option is under-used by a 52B model, not over-filled; named options absorb the residual (d07). Needs a modern-model rerun, and the human unpacking effect itself was not tested in LLMs. Claim K30.
- Gap 5: OPEN. CoT and top-k prompts lower ECE (d09, d08) but their effect on probability-identity violations is untested. Claim K31 records the calibration part only.
- Gap 6: OPEN. Nothing new found.
- Gap 7: PARTLY CLOSED. The accuracy-dominance theorem needs no bettor but needs a strictly proper score (d12); pragmatic and depragmatized versions still lean on bets or value judgements (d11, d13). Original proofs not opened. K03 upgraded to established (two reviews); K32 added, status contested.
- Gap 8: OPEN. Predd et al. not reproduced or opened; K24 stays single-source.
- Gap 9: OPEN. Nothing new found.
- Gap 10: OPEN. The Lewis/Teller four-bet structure was read (d11) but no LLM study links diachronic books to update failures.

Caution: d01 to d10 are mostly 2021 to 2024 papers on older or open-weight models and on accuracy and calibration, not on coherence identities. Treat them as indirect.
