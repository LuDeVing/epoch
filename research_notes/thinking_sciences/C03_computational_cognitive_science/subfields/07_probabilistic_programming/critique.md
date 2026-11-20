# Critique: C03.07 Probabilistic programming (cross-check)

Checked 7 arXiv papers by downloading the full text (Loula 2504.13139, Loose LIPS 2402.19471, NIPE 2306.14325, BToM 2402.10416, Ellis 2306.02797, RefineStat 2509.01082, BoxLM 2402.17879). PDFs deleted after extraction. Frank and Goodman 2012, Lake 2015, Gerstenberg 2021 are paywalled and were not re-opened.

## Corrections and confirmations
- Loula (Table 2): confirmed base vs Full SMC 0.063/0.419 (goal), 0.132/0.577 (molecules), 0.531/0.620 (SQL), 0.213 vs 0.346 or 0.407 (data science). The data-science Full SMC cell is ambiguous: the main table shows two values (0.346, 0.407) and the appendix 10-particle table shows 0.285. Treat data science as "gain exists, size unclear".
- Loula: Full IS vs Full SMC text-to-SQL is 0.618 vs 0.620, so resampling does nothing on SQL. Earlier lines (b18) only said the potential helps; now stated explicitly.
- Loose LIPS: k=1 EIG 0.65 (CodeLlama) and 0.66 (GPT-4 no board), grammar 0.36, human mean 1.27, best 3.61, 97% informative, 40% and 33% low fidelity: confirmed. One table row labels 0.36 as CodeLlama-7b and 0.65 as GPT-4 few-shot, which differs from the prose; the "0.65-0.66 for both LLMs" reading is from the prose. The k=5/k=10 claims were not re-checked.
- NIPE: r=0.927 (0.877-0.953), GPT-4 0.658, GPT-3.5 0.100, n=46: confirmed.
- BToM: belief r=0.92 [0.91,0.93], uniform-over-statements prior 0.86, heuristic mentalizer 0.04 (and 0.19), non-mentalizer 0.19, omniscient observer 0.64, goals r=0.93: confirmed. Earlier line b05 says omniscient observer 0.19 and ignorant observer 0.64; the table shows omniscient 0.64. CORRECTION: omniscient observer = 0.64 (b05 and b26 list 0.19 for it).
- Ellis: R2 = .81 for logical concepts and "within 3% of human" confirmed. The Number Game R2 = 0.95 appears in a figure; the exact "tuned prior" wording was not seen. Evidence line a21 says "about a couple dozen per person" and c14 says about 10^9 proposals for classic BPL; only the 5000-hypothesis figure was seen in the text. Treat 10^9 as unverified.
- RefineStat: run rate 0.10-0.11 to 0.45-0.50 confirmed. CORRECTION to c23: the line implied DQ-7B matches experts; Table 3 shows Dugongs 8.35 vs 22.43 and Surgical -114.29 vs -39.73, so matching holds only on Eight schools (-30.68 vs -30.70) and GP (-23.39 vs -26.53).
- CONTRADICTION across papers: Peregrine expert ELPD is -142.19 in BoxLM but -112.60 in RefineStat; Surgical expert -40.29 vs -39.73; Dugongs 22.52 vs 22.43. Different expert programs or reruns. BoxLM -173.11 is the same number in both.

## Weak spots
- Most gains are on tasks where an explicit checker exists. Nothing here tests an unconstrained reasoning task at equal tokens.
- Almost every LLM result uses small or old models (CodeLlama-7b, GPT-3, Llama-3.1-70B). Frontier-model baselines with long CoT are absent, so "beats plain LLM" is weak.
- Human-fit studies use small samples or aggregate correlations over few items (NIPE n=46, Number Game 8 people). High r with few items inflates.
- The 2023 Wong et al. paper has no measurements; the 2025 follow-up gives CI statements without R2 values we read.
- Criticism lines (b21-b23) were recalled, not opened; no replication numbers for Church-era claims were found.

## Only seen in snippets or secondary
b20-b23 (recalled), c26 (Large Language Bayes, secondary summary), c27 (AI4BayesCode listing), c28 (BLInD listing). Do not use for numbers.

## GAPS
1. Does an LLM-built probabilistic model plus sampling beat long CoT from the same frontier model at equal tokens on any reasoning benchmark (not human-fit)?
2. What is the token cost of the translate-then-infer pipeline (Wong 2023/2025) versus CoT, and does the gain survive matching it?
3. Does best-of-k by expected information gain (Loose LIPS) hold with frontier models and at k above 10, and what is the cost curve?
4. Exact R2 values and the LM-only baselines in Wong et al. 2025 Exp 1-3, plus the original 2014 tug-of-war numbers for a true replication check.
5. Were Frank and Goodman 2012 and Lake 2015 replicated, and what are the numbers in many-labs or cross-language replications of RSA?
6. Data-science Full SMC gain in Loula (0.346, 0.407 or 0.285): which setting is right, and does it hold at 5 particles?
7. Why do Peregrine expert baselines differ (-142.19 vs -112.60), and how do LLM-written Stan programs fare on a fixed expert set?
8. Quantitative published rebuttals to Bayesian just-so critiques (Jones and Love, Bowers and Davis, Marcus and Davis): did flexible priors change fits in re-analyses?
9. Do LLM-proposed hypothesis methods (Ellis, Piriyakulkij) generalize beyond Number Game and small rule worlds, e.g. to ARC?

## Gap search results (evidence_d.jsonl, d01-d21)
Full texts opened: Wong 2023 and 2025, Loula 2025, BoxLM, RefineStat, Large Language Bayes, BLInD, Loose LIPS, Hypothesis Search, Piriyakulkij 2024, Marcus and Davis 2013, Bowers and Davis 2012, Griffiths et al. 2012, Waldon and Degen 2021, Pournemat 2025. PDFs deleted afterwards.

1. OPEN, partly informed. No study matches an LLM-built probabilistic model against long CoT from a frontier reasoning model at equal tokens. Nearest: BLInD (d10), where GPT-4 few-shot CoT drops 78 to 7 percent from 2 to 10 variables while ProbLog stays 96 to 100, but on CLADDER the CoT is already 96 vs PAL 98 (d11). Models are 2023-24 era.
2. OPEN. Wong 2023 reports nothing on cost (d04); Wong 2025 reports no tokens or time and compares only to Llama-3.1-70B (d01). Cost anchors exist (d09, d06, d11) but none is matched to CoT.
3. PARTLY CLOSED. Loose LIPS tested k up to 50 with CodeLlama-7b and gpt-4-0613: passes the human mean at k=10, never the best humans (d12). Frontier models and a cost curve remain untested.
4. PARTLY OPEN. Wong 2025 gives LM-only R2 only in heatmaps; MSA Exp1-Exp2 self-consistency is about 0.95-0.98 (d02). The 2014 tug-of-war original numbers were not retrieved.
5. OPEN. No replication text opened. A Qing and Franke 2015 replication appears only in a snippet (d20); Waldon and Degen is an extension (d19). Marcus and Davis show the fit is decision-rule sensitive (d15).
6. MOSTLY CLOSED. Table 6 (8B): 5 particles 0.224 vs IS 0.204, 10 particles 0.285, 50 particles 0.292. The 70B 0.346 vs 0.407 cell is still unassigned, and Table 4 gives 0.225 for the same 8B, N=10 setting as Table 6's 0.285, an unexplained inconsistency in the paper (d05, d06).
7. CLOSED. Peregrine is a different dataset in BoxLM (real, 40 counts, -142.19) and RefineStat (simulated, 9 years, -112.60) (d07, d08). o3 on the fixed RefineStat set matches the expert on 3 of 5 (d08). Small Surgical and Dugongs differences are unexplained.
8. PARTLY CLOSED. Rebuttals were opened (d15-d18). They are arguments and worked examples; no systematic re-fit showing flexible priors preserved or broke fits across studies was found. Goodman and Hamrick 2015 reply could not be opened (403).
9. PARTLY CLOSED. Hypothesis Search (d13) shows propose-then-verify on ARC: GPT-4 17 to 30 percent on 100 tasks. Piriyakulkij (d14) stays on Zendo and ActiveACRE. Bayesian reweighting on ARC is untested.
Claims updated: K03, K05, K06, K07, K08, K11, K13, K14, K17; new K20 to K26.
