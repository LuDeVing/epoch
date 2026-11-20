# E11.09 Evidence and probability reasoning: critique

## Corrections and confirmations (sources re-opened this session)
- Hoffrage et al. 2000 (a07, a08): confirmed from the PDF text. Probability format 13% of professionals and under 1% of law students correct; natural frequencies 68% and 44%; guilty verdicts with probabilities 55% of students; with frequencies 32% and 33%. The 45% professionals figure was not re-seen in the extracted text (garbled OCR), keep as reported.
- Weber, Binder, Krauss 2018 (b01, b02): confirmed. The 4% vs 24% figures are McDowell and Jacobs (2017) meta-analysis means, cited by Weber, not Weber's own result. Their own N=180 results: 49% of participants given natural frequencies still calculated with probabilities; 18% of those given probabilities translated to frequencies; natural frequencies preferred in 34% of 360 tasks. CORRECTION: label b01 as "cited meta-analysis (McDowell and Jacobs 2017), read second-hand".
- Qiu et al. (b23, c07, c09, a23): confirmed "around 80% of the time" agreement. Added caveat: accuracy of about 80% was for simulated users; humans were much lower because their choices were inconsistent with stated preferences. Gemma original is 37% in the main figure but about 60% when filtered to human-like preferences, so the baseline gap depends on the preference distribution.
- Nafar et al. (b24, c10): GPT-4 chain-of-thought zero-shot 79, 63, 27 confirmed (V2, V3, V4). The PDF text table is garbled and a few-shot row reads 63, 46, 21 (model label not clear), while c10 says GPT-4 few-shot 78, 64, 36. This is NOT confirmed; treat c10 few-shot numbers as unverified until the table is read in layout mode.
- He et al. (c18, c19): "51 of 54" CoT setups positive and the Martingale 0.0 vs 0.04 Brier statement confirmed verbatim.
- Keppens (c01 to c03, c06): 37.06, 18.07, 0.6620 correct values, the 390 (about 21 times too high) error and 4 of 100 runs at 1.21 vs 0.66 confirmed. Note the "390" is described by the paper as the model reporting a different quantity than the asked LR, then rationalising it.
- Arithmetic checks: mammography posterior 0.8*.01/(0.8*.01+.096*.99)=0.078 correct; 1/8543 squared = 1 in 72.98 million, correct; LR 1000 at prior 1:9999 gives odds about 1:10 (9%), correct.
- Not re-opened (time): Gigerenzer and Hoffrage 16/28/46/50 (matches my memory of the paper and the first-agent PDF read), Li and Rui, Schoenegger et al., o1 vignette study, Wang and Redelmeier, Shengelia and Lagnado, Martire 2025.

## Contradictions between sources
- Natural-frequency success rate: 46-50% (Gigerenzer 1995 students), 24% (meta-analysis mean), 36% pooled and 51%/22% by item (Weber), 68% (Feufel medical students), up to 89% with training. The spread is large and depends on problem, sample and what counts as correct. Do not quote one figure.
- LLM base-rate results disagree: o1 100% correct on base-rate vignettes (b26) vs Li and Rui showing strong representativeness effects in older models, vs Schoenegger where a Bayesian prompt hurts. Differences are model era and task type (explicit numbers vs descriptions).
- Forewarning (b25): only 5% name the correct bias, yet framing moved 66 to 45%. Style vs substance is mixed.
- Sally Clark: standard critique (independence error) vs Fenton's point that the critique itself depended on hypothesis choice.

## Weak spots
- Foundational legal-psychology numbers (Thompson and Schumann 1987, cab problem, Koehler 1996) were never opened (a16, a17, a18). Do not use them as numbers.
- The LLM literature is mostly small, vignette-based, single-run or single-prompt studies; several are 2026 preprints or conference workshop papers (Keppens, canary paper b28, b17, b18, b21) with no replication.
- Keppens: four networks only, one model family, temperature 0.2, no human comparison.
- Mock-juror work uses MTurk samples and null results (b15); absence of format effect is not proof of equivalence.
- Several evidence lines are reviews with no numbers (a10, a15, a27, b07, b30, b31, c27, c28).
- No evidence of an LLM scaffold tested on real prosecutor's-fallacy transcripts or real case files; all legal-domain LLM evidence is either BN arithmetic or LegalBench slices.

## Seen only in snippets or second-hand
a16, a17, a18, a29 (second-hand), b14, b19, b20, b22, b28, b29, and the 4%/24% meta-analysis. 

## GAPS
1. Does a "convert to counts of N cases" operator (natural-frequency rewrite) improve a frontier LLM on perturbed base-rate and DNA-match problems at equal tokens, compared with plain chain-of-thought and with a tool-computed posterior?
2. How often do current LLMs commit the prosecutor's fallacy (transposed conditional) when summarising forensic evidence in realistic case prose rather than textbook vignettes?
3. Does the Hoffrage DNA case (13% vs 68% correct) replicate with LLMs, and with human legal professionals in 2020-2026?
4. Which Nafar et al. table row holds GPT-4 few-shot values, and does the BLInD collapse with network size persist for 2025-2026 reasoning models?
5. Can offloading to a Bayesian-network or ProbLog solver be made automatic (hypothesis set, priors elicited from text), and how often is the elicited structure wrong (Fenton's exclusivity and independence issues)?
6. Do reasoning models (o1/o3 class, Claude thinking) still show the weak-evidence effect, conservatism or belief entrenchment (Martingale) on legal-evidence sequences?
7. What were the original Thompson and Schumann (1987) and Koehler (1996) results, and do they replicate (defence attorney's fallacy, base-rate use)?
8. Does a bias-forewarning or explicit-hypothesis-listing step (G5) improve LLM accuracy on Sally Clark-style dependent-evidence tasks more than a generic warning?
9. How well do LLM-stated likelihood ratios and verbal evidential strengths calibrate against ground-truth BN values across many networks and models (extension of Keppens beyond four networks)?
10. Does the human null on forensic conclusion format (Martire 2025) hold for LLM readers/judges, who may be more format-sensitive?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d19). Scratch work was kept in the session scratchpad because drive D: does not exist on this machine. Web search was exhausted by parallel agents, so most finding was done through Europe PMC, arXiv pages, OSF and direct fetches.

- Gap 1 (convert-to-counts operator at equal tokens): STAYS OPEN. Only Araya 2025 (d03) tested natural-frequency prompting on LLMs, qualitatively, one problem, 3 models: partial and inconsistent use. No controlled test exists in what was found.
- Gap 2 (prosecutor's fallacy in realistic forensic prose): STAYS OPEN. Nothing measured; HelixCross (d14) is an untested training tool, Pompedda 2025 (d13) was read only via press releases.
- Gap 3 (Hoffrage DNA case replicated with LLMs or professionals 2020-2026): STAYS OPEN. Only indirect signal: the canary paper (d12) implies LLMs far exceed human ceilings on textbook Bayes items.
- Gap 4 (Nafar row): CLOSED for the table. GPT-4 few-shot CoT is 78, 64, 36, 25, 22, 16, 7, 7, 7 (d01), so c10 was correct. The question about 2025-2026 reasoning models on BLInD stays OPEN.
- Gap 5 (automatic solver offloading, elicited structure): PARTLY ADDRESSED. Translation from explicit text to ProbLog is 96 to 100 percent for GPT-4 and number extraction is 100 percent (d02), but the text states all numbers and links. Eliciting hypotheses, priors and independence from messy case prose is unmeasured, so Fenton's exclusivity and independence risk stays OPEN.
- Gap 6 (reasoning models, weak evidence, conservatism, entrenchment on legal sequences): PARTLY CLOSED. GPT-4o has strong order effects and conservative updating on a Sally-Clark-style vignette (d07, d08); GPT-5.2 is weaker but still order-sensitive (d09); GPT-5 is much more coherent than humans on explicit probabilities but still shows 18.8 percent conjunction fallacies (d11). Claude thinking and o3-class models are untested; the weak-evidence effect specifically was not tested on LLMs.
- Gap 7 (Thompson and Schumann, Koehler): PARTLY CLOSED. Koehler 1996 abstract read (d05). Thompson and Schumann 1987 stays unverified behind a paywall (d06); do not quote its numbers.
- Gap 8 (forewarning vs hypothesis listing on dependent evidence): STAYS OPEN. Generic prompts have limited, inconsistent effect (d10); hypothesis listing not tested.
- Gap 9 (LR and verbal-strength calibration beyond four networks): STAYS OPEN for legal evidence. Related finding: verbal probability words are unstable and lay-like across four chatbots (d15, medical).
- Gap 10 (LLM readers and conclusion format): STAYS OPEN. Pompedda (d13) is the only near-match and was not read in full.

Caveats: several 2026 items are preprints or abstract-only reads (d12, d13, d14, d16, d17, d18 flagged in their limits). Two lines (d06, d13, d16) are marked opened:false.
