# Critique: F03.07 Judgment and credence aggregation (cross-check)

## Re-opened this session (numbers confirmed from PDF text)
- Kim et al. 2025: 349 LLMs, 12,032 questions, wrong-wrong agreement 0.423, chance 0.127, 0.9987 pair, 100% and 97.5% of pairs above chance. Confirmed.
- Choi et al. 2025 Table 1: Qwen2.5-7B decentralised T=2 0.7377, centralised 0.6551, majority 0.7691; Llama3.1-8B majority 0.7242. Confirmed.
- Schoenegger 2024: LLM 0.20 (SD 0.12) vs human 0.19, t(60)=0.19, p=0.850; GPT-4 0.15; Coral 0.38; Study 2 0.22 to 0.15; t(92)=2.583 and 3.530. Confirmed.
- Wang 2023: GSM8K +17.9, self-consistency 74.4. Confirmed.
- Brown 2024: 82.9 to 98.44, vote 40.50 to 41.41, SWE-bench 15.9 to 56. Confirmed.
- Halawi 2024: trimmed mean 0.1649, mean 0.1656, no ensemble 0.1676, test 0.179 vs 0.149, 71.5 vs 77.0. Confirmed.
- List 2005 table: 0.0938, 0.2157, 0.2500, 0.3211, 0.7113, 0.9999. Confirmed.
- Not re-opened (Cloudflare block or API rate limit): Kurvers 2016, Lorenz 2011, Becker 2017, Satopaa 2015, Karger 2025, Douven 2026, He 2026, Prelec 2017.

## Corrections and flags
- No numeric correction was needed on the verified items.
- b27 (Prelec) says error cut 21.3%, and b02 (Lorenz) says the mean was closer than individuals in 21.3% of cases. The same figure in two unrelated studies is suspicious; one may be a misread. Treat both as unverified until reopened.
- a23: MoA abstract says 65.1%, body 65.8%. The paper disagrees with itself; cite 65.1 with a note.
- a15 line was truncated in places but b17/c15 carry the full table and match the PDF.
- a16/b19 (Smit): dataset mapping for the self-consistency row is not verified; do not cite those numbers.
- Evidence a10, a11, a12, b26 to b29 are from memory (opened:false). No claim rests on them alone. Claims K13/K19 (human studies) rest on b01 to b03 which were not re-opened.

## Contradictions between sources
- Debate: Du 2023 shows large debate gains; Choi 2025, Smit 2024, Zhang 2025 and Wang 2024 find them shrink or vanish against voting or a strong single prompt. Likely drivers: baseline strength, model size, tuning.
- Mixing models: MoA (Wang 2024) says mixing helps; Self-MoA (Li 2025) says repeat the best model; Zhang 2025 says mixing two models helps debate.
- Humans: Lorenz 2011 says social influence hurts; Becker 2017 says it helped in decentralised networks.
- Mean vs median: Douven (clean set) mean beat median; Halawi found negligible differences.
- Self-consistency (plain vote beats probability weighting) vs Han 2026 and Kurvers (confidence weighting helps): depends on whether confidence is informative.

## Weak spots
- Most LLM results use one model family, one benchmark set, and few runs; several debate papers lack an equal-token control.
- Almost nothing measures premise-based vs conclusion-based aggregation on LLM outputs. The core S7 question (doctrinal paradox in agent outputs) has no LLM measurement in this set.
- Forecasting crowd results are small (31 questions) and subject to training leakage (Douven 2026).
- Per-item competence (the real Condorcet condition) is estimated only in Chen 2024.
- 12 of 25 claims are single-source.

## Seen only in snippets or abstracts
Universal self-consistency (c10), Karge 2026 (c23), Reasoning and Tools (c25), Yuan 2026 (c26), Smit 2024 numbers, Wang 2024 numbers, authors of the Deliberative Crowds preprint (c20).

## GAPS
1. Does premise-based (sub-claim) aggregation beat answer-based majority vote for LLM samples on multi-step tasks at equal tokens? Is there any measured doctrinal-paradox rate in LLM output?
2. How much effective sample size does one model's temperature sampling give (ICC across tasks, temperatures, prompts), and does persona or prompt diversity reduce it?
3. When does per-item competence fall below 1/2, and can agreement share predict it well enough to gate voting (abstain or escalate)?
4. Confidence-weighted vs plain vote: does verbalised or token-level confidence help at equal samples (Wang 2023 says weighting hurt)?
5. Best code rule for probability outputs from samples (mean, median, trimmed, log-odds, extremized), and what extremizing factor suits correlated LLM samples?
6. Does a verifier or checker beat vote outside code and math (Brown 2024 shows the gap only there)?
7. Debate vs vote at strictly equal tokens with strong single-prompt baselines and one model only.
8. Reopen Kurvers 2016, Lorenz 2011, Prelec 2017, Genest-Zidek 1986 and Dietrich-List 2016 for exact numbers (and settle the 21.3% duplicate).
9. Does surprisingly-popular aggregation (asking the model to predict the crowd) work on LLM samples?
10. In a single model's own 2:1 splits, how often is the minority right (He 2026 found 25.5% for three vendors) and can anything flip safely?

## Gap search results (evidence_d.jsonl, d01 to d24; claims K26 to K36 added)

Tools: WebSearch quota was exhausted, the arXiv API and OpenAlex were rate limited for curl. Paper PDFs were fetched from arxiv.org/pdf, PMC pages from pmc.ncbi.nlm.nih.gov, and search was done through the arXiv API via WebFetch. Search relevance was poor, so coverage of 2025 to 2026 LLM work is partial.

### Closed or mostly closed
- Gap 7 (debate vs vote at equal budget): closed for one model. Wang 2024 (d13): debate 18 queries lost to CoT-SC 20 and declined with budget. Ferreira 2026 (d14): 23 small models, 5,500+ runs, solo 80.4, debate 84.4, SC-9 84.8, debate 3.4x tokens. Mansuri 2026 (d15) gives the mechanism (withheld dissent). Claim K30 established.
- Gap 8 (reopen sources): Kurvers 2016 (d06) and Lorenz 2011 (d07) reopened from PMC and confirmed. The duplicate 21.3% is Lorenz (arithmetic mean closer than first estimates in 21.3% of cases; 77.1% in log space). Prelec 2017 is paywalled; the 21.3% in b27 stays unverified and should be cited as unverified or dropped. Genest-Zidek 1986 and Dietrich-List 2016 could not be fetched (Project Euclid and LSE links failed), so these stay open and no numbers from them should be cited beyond the theory already in a-entries.
- Gap 4 (confidence-weighted vs plain vote): resolved as "depends on the signal". CISC (d01): P(True) weighting saves 41% (budget 5) to 46% (budget 10) of samples; verbal 0-100 saves 22% and 30%; accuracy gain only 1 to 2 points at equal budget; the best-calibrated signal was not the best weight. Sakai (d05): P(True) AUROC 0.47 on Qwen3-1.7B, below chance. Claim K21 moved to contested; K28 added.

### Partly closed
- Gap 2 (effective sample size): one direct measurement. Error correlation among 5 samples from gpt-oss-120b is 0.57 to 0.63 with or without persona prompts (d11), so n_eff is about 1.5 of 5 (my arithmetic). Method-prompt diversity helped a lot on planning tasks (d09), but it also changes prompt quality. No ICC across tasks and temperatures was found. K07 kept single-source; K26 and K31 added.
- Gap 3 (when competence falls below 1/2, gating): agreement share correlates with accuracy (d04) and is a safe stopping rule (d02, d03; K27 established). Nobody was found who measured accuracy by agreement bin or tested it as an abstain gate. Open for abstention.
- Gap 5 (code rule for probabilities, extremizing): theory only. Lichtendahl 2018 (d21): extremize when information is private, anti-extremize when it is shared; one model's samples share nearly everything, so default factor 1. No LLM test. Lorenz (d07) says use median or geometric mean for skewed numbers. K32, K34 added; both weak.
- Gap 6 (verifier outside code and math): Weaver (d19) shows a weighted ensemble of 33 verifiers beats vote on GPQA and MMLU (87.7 vs about 72 average), but with a labelled dev set; a plain average did not. Stroebl (d20) shows false positives cap gains. A same-model verifier outside code and math was not tested. K29 added.
- Gap 10 (minority in 2:1 splits): He 2026 re-read and matches (d17). Blind trust -19.16 points. For a single model, Sakai (d05) gets +1.5 points; DCR (d16) rescues minority answers on math with an LLM step. K33 added. Open: harm counts for DCR; no gate that works across models.

### Still open
- Gap 1: no one measured a doctrinal-paradox rate or premise-wise code voting on LLM samples. Nearest: SC-MoA (d10), an LLM reading all traces beat vote by 5 to 6 points at about equal calls on three benchmarks (single paper), and Graph SC (d22), which shows final-answer wins are often unfaithful (MedQA 40% faithful). K35 records this as single-source. We must run this in our own harness.
- Gap 9: no study applying the Surprisingly Popular rule to one model's samples was found in the searches that worked. Indirect: PopMCQ (d24) 66% popular-wrong choices; Shinitzky 2022 (d23) human-only. K36 single-source and untested.

### Flags
- Weaver Table 1 and Table 3 disagree on the GPQA majority entry (47.4 vs 44.9); the table text is garbled in extraction, cite averages only (72.2 vs 71.6).
- DCR Table 1 shows jumps of 30 to 40 points for weaker models (Llama-4 36.4 to 73.7 on MATH500). These look too large; treat as unconfirmed.
- K16 downgraded from established to contested because SC-MoA and USC show an LLM aggregator can match or beat a vote on reasoning tasks, while the forecasting result (numeric outputs) still favours code rules.
- Several 2026 sources are preprints from single teams with no replications.
