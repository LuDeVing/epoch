# Critique: D02.03 The problem of the priors (cross-check)

Sources re-opened this session (full text via arXiv/ACL/gwern PDFs): Drory 2015 (1503.09072), Arai et al. 2025 (2509.04250), Schoenegger et al. 2025 (2506.01578), Li and Rui 2024 (2412.11009), Qiu et al. 2025 (2503.17523), Gupta et al. 2025 (ACL), Efron and Morris 1977.

## Numbers confirmed
- Drory: 700 attempts, 363 successes (0.518), 123 chords longer than the triangle side, proportion 0.339. Confirmed. Standard error about 0.025, so 0.339 fits 1/3 and is far from Jaynes's 1/2. Note it uses a different generating process (stick released at a point on the circle edge), so it does not contradict Jaynes's straw set-up; it shows the answer follows the process.
- Efron and Morris: .077 vs .022, ratio 3.5, shrink about 80 percent, Clemente .294. Confirmed.
- Schoenegger et al.: Frequency-Based Reasoning -0.019 (adj p 0.022), Base Rate First -0.016 (0.036), Step-Back -0.015 (0.036), Bayesian Reasoning +0.025 (0.036), 38 prompts. Confirmed (pooled analysis). In a single-model table the raw gains were not significant after correction (adj p 0.128 to 0.256), so the effect is small and model-dependent.
- Li and Rui: odds ratios 9 / 9 / 8.86 / 6.36 / 3 / 9, humans 2.25; prior-posterior Spearman -0.84 to -0.90, posterior-similarity 0.90 to 0.95 in the main table (b07 says 0.87-0.94, c15 says 0.90-0.98 incl. modifications; ranges differ by what is counted). Confirmed.
- Gupta et al.: Mistral-7B-Instruct decay 0.9107; Pythia suite used; 60-80 percent heads bias. Confirmed.
- Arai et al.: Table 2 values confirmed (80%: -4.093 +/- 0.107; 100%: -4.094; baseline 100%: -4.103 +/- 0.136; 328 to 262 patients). Table 1: Llama blind T1.0 -3.842 +/- 0.294, baseline -3.963 +/- 0.464, MedGemma blind T0.5 -4.133, MedGemma blind T1.0 -3.844.

## Corrections
1. b21 and c10 are the same paper (Arai, Selby, Vargo, Vollmer; arXiv 2509.04250), not two sources. c10 labels the author "Anon"; wrong. The "overstated" judgement in c10 is the checker's reading, not a separate finding: all gaps are inside one SD. Counted as one source.
2. Qiu et al. human data: the 48 are simulated users, annotated by 15 human participants each (720 participants). c20 says "48 human participants" (wrong); b09 "Humans (48 users)" is ambiguous. b09's "random baseline 37%" is doubtful: the paper reports the original LLM's baseline accuracy as 37.0% (95% CI 30.6-43.5) in flights and 36.7% in hotels. Treat 37% as the unprimed model's first-round accuracy, not a random baseline, until checked.
3. Jaynes's "embarrassingly low chi-squared" (a03/b01): no table, no p-value; kept as informal.
4. a26/a27 were snippet-only in file a; b17/c18/c17 opened the same papers. a27 numbers (base-rate neglect "comparable to humans") are the CogBias background citing others, not CogBias's own result (its own judgment bias rate is 19.8 percent).

## Contradictions between sources
- Jaynes (invariance gives 1/2) vs Drory (same symmetry tools support 1/3 and 1/4). Both sides are internally consistent; status contested.
- Natural frequencies: meta-analysis headline 24% vs 4% (via Weber et al., secondary) but Weber et al. find 49% still convert to probabilities and only about 36% vs 20% correct in their own table. Size of the human benefit is unsettled.
- LLM priors help (AutoElicit, Arai headline) vs fail (Selby: ESS near 0, no beating of baselines). Differences in task: linear weights vs weather facts vs clinical rates.
- Prompting: step-by-step Bayes fixed the semi-structured test (Li and Rui) but "Bayesian Reasoning" made forecasts worse (Schoenegger) and CogBias debiasing prompts hurt judgment accuracy.

## Weak spots
- Almost all LLM studies use 2023-2024 models (GPT-3.5/4, Llama 2/3, Mistral-7B). No test of 2025-2026 frontier reasoning models on prior recall or class-record use.
- No study tests the exact thing our agent does: a measured class record as a prior in a gate. All is by analogy (Efron-Morris, AutoElicit).
- Several results are single-source (Gelman et al. example, Efron-Morris, iterated-learning readout, label-prior effect).
- Data leakage is acknowledged in AutoElicit and Selby; effect on headline numbers not quantified.

## Only seen in snippets or second-hand
- b03 (Shackel 2007), b13 (McDowell and Jacobs 2017 meta-analysis, via Weber et al.), b27 (Tversky and Kahneman 1974, Bar-Hillel 1980, Barbey and Sloman 2007), c24 (Dasgupta; abstract only), c25 (Jaynes 2003 book), c26 (Lampinen 2022, second-hand), Drory's other claims about Jaynes in a02/a25 Wikipedia summaries. Wikipedia lines (a24, a25) are secondary.
- Semantic Scholar and arXiv search APIs returned 429 during this check; no new sources were searched.

## GAPS (most decision-relevant first)
1. Does a stored class record (k of n, shrunk toward the pooled pass rate) beat the model's own recalled prior in our S0 gate, measured by Brier score at equal tokens, for classes with n below 10?
2. Which default prior for a class with zero history (Beta(1,1), Beta(1/2,1/2), Haldane, or pooled-empirical) gives the best early gate calibration on our own run logs?
3. How much does an explicit effective-sample-size or (k,n) display change whether the model respects the prior, versus a bare percentage? (Natural-frequency effect for LLMs is only second-hand.)
4. Do 2025-2026 reasoning models still show similarity-over-base-rate behaviour (Li and Rui: prior-posterior correlation about -0.9), and does a code-computed posterior remove it?
5. Is "start from the base rate" (Schoenegger: -0.016 Brier) robust across models and tasks, or limited to forecasting, and does it stack with a stored class record?
6. How should the agent set prior strength (Carnap lambda / pseudo-count) from data, e.g. by empirical Bayes across classes, and how many classes are needed?
7. When the class record and the case evidence conflict (prior-data conflict), what detection rule (prior-predictive check, ESS near 0) should trigger a doubt step, and what is its false-alarm rate?
8. How large is memorisation/leakage in LLM-stated priors for tasks like ours, and do private tasks show smaller gains than AutoElicit's public datasets?
9. Does the 66-patient saving of Arai et al. replicate on other trials with proper variance, or is it noise?
10. Does the Jaynes invariance step (list what the task leaves unspecified) change agent answers on under-specified "random" problems, or just add tokens?

## Gap search results (evidence_d.jsonl d01-d16; claims K29-K35 added)

Search limits: all 8 WebSearch calls used; arXiv, Semantic Scholar and OpenAlex APIs were rate-limited (429 or zero credit) on 2026-11-03, so no forward-citation lookups worked. Three of the gaps were attacked by simulation on synthetic data (script D02.03_sim.py and D02.03_sim2.py in D:/research_scratch/D02.03/tmp). Simulation results are model evidence, not measurements on our run logs.

Partly closed (answer from theory plus simulation; still needs our logs):
- Gap 1 (class record vs recalled prior, n<10): in simulation, Beta(1,1) shrinkage of (k,n) gave Brier 0.2339 vs raw k/n 0.2678 and a recalled prior of 0.8 (assumed 0.2 too high) 0.2794 (pool mean 0.6, strength 6). Direction is clear. The size on real logs is open (K29).
- Gap 2 (zero-history default): Beta(1,1), Jeffreys and Haldane give the same 0.5 (or are unusable) at n=0; the pooled empirical rate beats them (0.240 vs 0.250). Winkler et al. 2002 show defaults disagree strongly at zero events (K30). Real-log check open.
- Gap 6 (prior strength from data): method of moments needs about 20 classes in simulation; below 10 fixed Beta(1,1) wins (K31). Chen and Lei 2025 back data-tuned shrinkage on real data with small per-unit n (about 1 to 5 percent MSE gain).
- Gap 7 (prior-data conflict rule): the beta-binomial prior-predictive check is exact for (k,n) records; false-alarm rate 0.014 to 0.051 at alpha 0.05; power 0.33 to 0.38 at n=5 to 10 for a drop from 0.6 to 0.2 (K32). Rate on our logs open.

Moved forward but not closed:
- Gap 3 (display of (k,n) vs bare percentage): indirect evidence only. Raw lists are hard to count and order-sensitive (Pournemat 2025; Chlon 2026) (K33). No direct LLM test of (k,n) vs percentage found.
- Gap 5 (base-rate-first robustness): no new stacking study found. CogBias shows prompt debiasing backfires on Judgment items (-4.4 percent), which argues against relying on prompt wording (d11).

Still open:
- Gap 4 (2025-2026 reasoning models and similarity-over-base-rate): no study found. Newest studies use non-reasoning or small distilled models (K34, d16).
- Gap 8 (leakage in LLM-stated priors for private tasks): nothing new found.
- Gap 9 (replication of the 66-patient saving of Arai et al.): forward-citation lookup failed; no replication found.
- Gap 10 (Jaynes invariance step for agents): no LLM study found. Search for LLM plus Bertrand paradox returned only philosophy sources.

New contrasts and corrections:
- Winkler et al. (d02): conservative shading of a prior can flip a downstream decision (0.018 vs 0.053). Opposes any plan to feed the gate a pessimistic class rate.
- BASIL re-read (d14) is the same paper as c12 and c13; not a new source.
- Chen and Lei Table 1 came out garbled in text extraction; the column mapping in d09 is a reading.
- Nott et al. author list in d04 was written from memory of the paper header and not re-checked in the PDF text.
