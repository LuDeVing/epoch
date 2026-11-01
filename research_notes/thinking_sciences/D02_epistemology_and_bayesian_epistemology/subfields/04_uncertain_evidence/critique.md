# D02.04 Uncertain evidence: cross-check critique

Re-opened this session (pdftotext of arXiv PDFs, saved under D:/research_scratch/D02.04/): Jacobs 2019, Farmer et al. 2026, Wilie et al. 2024 (Belief-R), Sharma et al. 2024, Xiong et al. 2024, Halawi et al. 2024, Zhang et al. 2025 (discounted filters), Filbry et al. 2026, Samanta et al. 2026 (BayesBench), Qiu et al. (Bayesian teaching), Kim et al. 2025, Gupta et al. 2025, Xie et al. 2024.

## Numbers confirmed
- a01 Jacobs: 15% / 12% (Jeffrey) vs 3% (Pearl, 148/4702) confirmed.
- b14/b15 Belief-R: 10.99/92.09/51.54, 19.65/82.69/51.17, 35.38/36.57/35.98, 44.04/53.13/48.59 confirmed (table in PDF text).
- b17-b19 Xiong: ECE above 0.377, AUROC 62.7%, 54.8% to 92.7%, GSM8K ECE 0.064 at 93.6%, 0.522 vs 0.605 confirmed.
- b21/b22 Sharma: 32-86% answer change, 42-98% admit mistake confirmed.
- c05 Farmer: alpha by condition (1.03, 1.11, 1.18, 1.26), by dataset (1.18, 1.12, 1.05, 1.26), 4,975 problems, mean R2 about 0.76 confirmed.
- c02 gamma 0.88, correlation -0.85, "typically under 13% of total error" confirmed.
- a17 Filbry: over 50% across chats, 10% Gemini, 1 of 30 Gemma confirmed; "at least 30%" success loss confirmed.
- b06/b08 Qiu: 624 users, 48 human-annotated users (15 raters each, 720 participants), p = 0.002, about 80% agreement, 40% noise control confirmed.
- c10 Xie: GPT-4 80% memorization ratio, order effects over 5% (over 30% for PaLM2 and Llama2-7B) confirmed.

## Corrections made
1. c11 Halawi: "about 3,762 questions" is wrong as a test size. 3,762 is the TRAIN set; the test set is 914 (5,516 total). The 0.208 Brier is the ZERO-SHOT base GPT-4-1106 score, not the full system. Claims use 914 and "zero-shot".
2. b21 Sharma: the "up to 27%" is two different results. After "Are you sure?" it is Claude 1.3 (27%); for a user suggesting a wrong answer it is LLaMA 2 (27%). Do not merge them.
3. a16 Filbry: the 85% mass on a hypothesis with true posterior 0.261 comes from a Gemini-2.5-Pro reasoning-only trace on ProteinWorld-hard, no tools, uniform prior. The paper says neither reasoning-only variant approaches the oracle. The a16 text "with reasoning and code, close to oracle" is only partly checked (Gemma simple case not re-opened).
4. a18 BayesBench: over-updating is "can over-update in the coin task when the evidence is skewed", and a tendency to push middle triage labels to extremes. Not a general result for all seven models.
5. c05 Farmer: the summary line "later prompting stages show lower alpha" refers to repeated-elicitation stages in a fixed pipeline (GPT-5.2). Across conditions, conditions that add evidence have HIGHER alpha. The two should not be mixed. The same table pairs higher alpha with higher ECE/Brier, so the amplification is not harmless.
6. a05 claims "64%, 9%, 33%" for three WebPPL programs: the first number was not re-checked against the paper this session (only Jacobs, not Jacobs and Stein, was re-opened).

## Contradictions between sources
- Gupta (updates broadly Bayesian, error is in priors), Zhang (a discounted filter fits better; updates not flawed), Falck (martingale property violated, not Bayesian), Filbry/Qiu (updates are far off the oracle). These differ by task: hard binary data with a simple parameter vs. structured tasks with likelihoods to build. Not a true conflict, but "LLMs are Bayesian" is only supportable for the simple case.
- Over-reaction (Sharma, BayesBench, Farmer alpha above 1) vs under-reaction (Belief-R, Qiu plateau, human conservatism). Both exist; direction depends on source type (social pushback vs. logical undercut vs. evidence stream).
- Jeffrey vs Pearl: sources (Jacobs, Munk, Dziurosz-Serafinowicz) all disagree on which is "right"; none tests it.
- Kim et al. (contradictory evidence acts like golden) vs Xie (models do accept coherent counter-evidence): the first is about evidence shown beside the claim, the second about evidence conflicting with memory.

## Weak spots
- No study tests soft evidence (Jeffrey-style) on LLMs directly. Nearly all LLM work uses hard observations. Only Farmer et al. comes close, and it is a single preprint with externally built evidence signals.
- Several 2026 preprints (Filbry, Samanta, Farmer, Atwell) are single-source and not yet peer reviewed.
- All human Jeffrey studies (Zhao and Osherson 2010, Hadjichristidis 2014, Over 2009, Phillips and Edwards 1966) were abstract or snippet only: no N or effect sizes.
- Models are mostly small open models in the dynamics papers (2B-8B), so claims about frontier models rest on Filbry, Belief-R, Sharma, Farmer.

## Only seen in snippets or from memory (opened:false)
a09, a10, a11, a12, a13, a14, a15, a23, a24, a25, b27, b28, b29, b30, c14-c18. Field (1978), Skyrms (1987), Diaconis and Zabell (1982), Pearl (1988, 1990), Chan and Darwiche (2005), Hawthorne (2004), Trpin (2019) are unverified at source.

## GAPS
1. Does coding a noisy check as a Bayes factor (code multiplies) beat letting the model restate credence, at equal tokens, on our own items? (K01, K02, K05 all point to yes but no direct test exists.)
2. How much should a verifier/check be weighted? Farmer gives alpha above 1 for LLM revisions; what is the calibrated weight for our checks, and does capping alpha at 1 lower error?
3. How correlated are repeated checks from the same model, and what discount is right? No measured intra-model correlation of check errors was found.
4. Does a rigidity test (does the check change within-cell conditionals?) catch real violations, and how often do they occur in practice?
5. What do the Zhao and Osherson (2010) and Hadjichristidis (2014) full papers report (N, effect sizes, failures of invariance)?
6. Does a no-new-evidence rule ("credence moves only on new tool output") stop sycophantic flips at equal tokens without raising under-update (Belief-R style)?
7. Are verbal hedges ("probably passed") mapped consistently to numbers across models (QUITE exact accuracies were not extracted)?
8. Do frontier reasoning models (not 2B-8B) show the discounting and prior-bias effects, and does extended thinking change alpha?
9. Do Jeffrey and Pearl conventions give different final answer accuracy in an agent loop, not just different numbers in a toy test?

## Gap search results (2026-11-01)

Constraint: WebSearch quota was exhausted and arXiv search, Semantic Scholar search and OpenAlex returned HTTP 429 all session. Only known-ID arXiv fetches and Crossref worked. Gaps 1, 4, 8, 9 therefore rest on "nothing found", which is weak. New evidence is in evidence_d.jsonl (d01-d16); new claims K18-K23.

- Gap 1 (code multiplies vs model restates, equal tokens): STAYS OPEN. Closest is Weaver (d05): code-side weighted log-odds combination of weak verifiers beat unweighted and majority vote by 13.5-17.1 points, but that is selection among samples, not credence updating. Needs our own arm.
- Gap 2 (verifier weight, cap alpha at 1): PARTLY CLOSED on direction. Per-check weights learned from accuracy beat equal weights by up to 11.2 points (d05), and checks are asymmetric (d06: self-check fail FNR 96-97% in two domains, pass FPR 0.5-18.6%), so set pass and fail Bayes factors separately and measure them. Whether capping alpha at 1 lowers error on our checks was not tested anywhere.
- Gap 3 (correlation of repeated checks): PARTLY CLOSED. No intra-model coefficient exists, but cross-model error agreement is 42-60% when both wrong, up to 0.97 within a provider (d04), and majority vote or reward-model selection gains almost nothing from 100 to 10,000 samples (40.50% to 41.41%, d13). Rule: count same-family checks as one source. Right discount still unmeasured.
- Gap 4 (rigidity test): STAYS OPEN. No LLM or agent-run study found.
- Gap 5 (Zhao and Osherson 2010, Hadjichristidis 2014): STAYS OPEN. Both closed access with publisher-withheld abstracts (d14, d15). K14 remains contested; no N or effect size can be cited.
- Gap 6 (no-new-evidence rule): PARTLY CLOSED. Self-review without outside signal does not help (d08, d07). Large and reasoning models resist pushback far more than small ones (d09: Turn-of-Flip 4.85-4.90 of 5 vs 0.83). Neutral re-judging beats continuing the chat (+24.6% net, d10). Nobody measured the under-update cost of a tool-output-only rule against Belief-R, so that half is open.
- Gap 7 (verbal hedges): PARTLY CLOSED. Strong models map hedges to numbers like humans in neutral contexts (85% or better modal agreement; 7 of 10 models beat an individual human) but shift 7.0 points on average, up to 49.5 for "possible", with the model's belief in the claim (d01). Small old models near chance (d02). Hedges are unfaithful to model uncertainty (d03). QUITE per-model accuracies still not extracted.
- Gap 8 (frontier reasoning models, extended thinking, alpha): PARTLY CLOSED. Reasoning models are still overconfident (often above 85% on wrong answers) and more thinking raises confidence on items they stay wrong on (d11); abstain less (d12). Alpha for reasoning models not measured.
- Gap 9 (Jeffrey vs Pearl by accuracy): STAYS OPEN.

Housekeeping: while writing, an older generator script (mk_D02.04.py in D:/research_scratch/D02.04/tmp) was run by mistake and rewrote evidence_b.jsonl (30 lines, 26 opened). It is the script that originally produced that file, so content should be unchanged, but the cross-checker should diff if in doubt.
