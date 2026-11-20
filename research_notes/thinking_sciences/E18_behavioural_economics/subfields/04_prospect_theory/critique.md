# E18.04 Prospect theory: cross-check critique

## Re-opened this session (full text or abstract)
Confirmed against the source text:
- Walasek & Stewart 2015 (PMC4312134, Table 1): Exp 1a lambda 1.79 (gain 40 / loss 20), 1.00, 1.02, 0.88; Exp 1b 1.59, 1.01, 1.02, 0.81; Exp 2 2.28; Exp 3 1.81 and 1.23 (symmetric 40/40) and 0.93. Final samples 323, 382, 401 confirmed. Exp 3 N=82 not re-checked.
- Tarabeih 2026 (arXiv 2610.33103 PDF): pooled lambda 1.26 [1.06,1.46], t(27)=2.66 p=.013, range 0.49 to 2.72, prediction interval 0.20 to 2.31, symmetric 1.15 vs 1.07, weighting 0.81 [0.37,1.25 across four studies], three reasoning models share 0.81, study-level 1.31 [1.06,1.56].
- Jia et al. 2024 (arXiv 2406.05972 PDF): GPT-4-Turbo lambda 1.4786, Claude-3-Opus 6.316, Gemini 2.3333, human 3.47 (SD 3.92); persona-adjusted Claude 2.6017 then 2.1665; Gemini 2.7232 then 2.9430; 300 draws per model.
- Yechiam & Tarabeih 2026 (arXiv 2608.12339 PDF): ChatGPT 1.257/1.218 in loss-aversion condition; 1.09 (no paper), 1.79 (abstract), 1.52 (full report); Qwen 1.742 vs 0.940/0.929.
- Ruggeri 2020 (Nature Hum Behav page): n=4,098, 19 countries, 13 languages, 94% of items, 12 of 13 contrasts.
- Marks & Vollberg 2026 (arXiv 2610.40985 PDF): gain minus loss rating scale +1.2 to +24.3, p<.001; largest gemini-3-flash 24.3.
- Yechiam & Zeif 2025: title confirmed via Crossref only; the 1.07 figure rests on Tarabeih and the Crossref record gave no abstract.

## Corrections
1. a20 in evidence_a gave Claude "weighting 0.7613"; Jia's table puts 0.7613 under alpha (probability weighting) and 6.316 under lambda. Consistent with c02. No change in meaning, but a20 labels were garbled; trust c01/c02.
2. a15/b11 give the Gemini coefficient as 0.86 (Model 5) in one line and +0.69 in another (family model). Both are real: different models in the same paper (Model 5 includes year and stake). Keep both with the model named.
3. Release-year coefficient: -0.25 (Model 5, a17) vs -0.16 (b12). Same cause. Cite the model.
4. a24 and b23 cite Wang et al. 2026 (developmental trajectories); Tarabeih cites "Wang, Z. et al. (2025)" with GPT-3.5 2.72 and GPT-4.1 0.57. Probably the same paper with a changed year. Treat as one source.
5. b03 lists Exp 2 as "1.01 (20/60)"; the table puts 1.01 on the loss-range-60 row. Read it as: gains range 20, losses range 60 gave 1.01 (no reversal, just neutrality).

## Contradictions between sources
- Human reference lambda: 2.25 (1992), 1.96 (Brown), 3.47 (Jia sample), 2.63 (Tanaka), 1.31 (Walasek 2024), 1.07 (Yechiam & Zeif). "LLMs are below humans" depends entirely on which one is used.
- Anti-gambling paper (c18): abstract 24.3% vs results 52.4% loss-chasing reduction; overconfidence -18.7% vs -33.3%. Marked contested.
- Heuristics-and-biases drug paper (c21): abstract says 1,500 experiments, method implies 13,500.
- Marks & Vollberg: ratings asymmetric but choice lambda near 1; this contradicts the idea that stated feelings drive LLM choice.
- Jia: Claude lambda 6.32 (very high) versus Tarabeih pooled 1.26 and other studies at about 1.0; the Claude figure is an outlier from a multiple-price list design and one prompt.

## Weak spots
- All LLM-meta-analytic claims (K07, K08, K10, K11) depend on one author's preprint (Tarabeih 2026) and on Yechiam & Tarabeih (same group). Independence is counted as 1.
- Only 11 studies, 28 lambda estimates; cluster tests have few degrees of freedom; publication bias tests have k=10.
- Many LLM studies use different elicitation methods, temperatures, prompts; "model" is not a stable object (versions change).
- Human side: Brown 2024 and Yechiam & Zeif 2025 disagree because of inclusion rules; neither is settled. Imai 2025 weighting/curvature known only second-hand.
- No study here measures whether any bias knowledge helps or hurts thinking quality on hard tasks; the link to our scaffold is background only.

## Seen only in snippets or second-hand (opened:false)
a32/b10 Yechiam & Zeif 2025 (numbers via Tarabeih), a33/b26 Imai 2025, b08/b09/a22 Brown and Walasek 2024 (via Tarabeih and OSF page), c22, c23, c24 Gal & Rucker 2018 (no numbers), b05, b06, b07 Mrkva 2020 (no coefficients), a30/a31 Wikipedia. b28 no numbers.

## GAPS (most decision-relevant first)
1. Does a debiasing or re-frame step in a scaffold change an agent's loss-aversion or framing flips at equal tokens, and does it change accuracy on real tasks (not just on lottery items)?
2. What is the human lambda in a design-matched set (symmetric ranges, incentivised, same scale) that we should use as the target for our agent, given 1.07 vs 1.96 vs 2.25?
3. Does stating the bias name in a system prompt or scaffold text (prompt contamination, Yechiam & Tarabeih) raise bias in other models and in reasoning models?
4. Do reasoning or thinking-enabled models behave closer to expected-value maximisers (o3 chose the sure option 399/399; EV in 20-47% of rationales), and is that preferable for decisions with real human-value stakes?
5. How stable is lambda across reruns, wordings and temperatures for one fixed model (Qwen2.5-32B 0.95 to 2.01), and what number of runs is needed for a trustworthy estimate?
6. Do LLMs reproduce the original 1979 problems (P1-P14) and the 2020 replication battery with human-like choice shares, and which items fail?
7. Is the Ge et al. 2026 description-versus-experience gap in 20 LLMs vs 360 humans a stronger lever than loss aversion? Need the actual decisiveness numbers.
8. What does the territorial prospect theory replication (69%/81% of items) say about boundary conditions, and has it been peer reviewed?
9. Does persona or stake context (rich vs poor d=4.15) leak into agent decisions on neutral tasks, and can a guardrail block it?
10. Do KTO-style loss weights (lambda_D, lambda_U) matter outside alignment training, i.e. is there any scaffold-side use of loss-weighting?

## Gap search results (evidence_d.jsonl, d01-d18)
Search budget note: the shared WebSearch budget ran out partway and the arXiv, Semantic Scholar and OpenAlex APIs were rate limited, so gap 6 could not be searched further. All 18 evidence lines are opened:true (full PDF text, or the page abstract for d13 and d16).

1. Debias or re-frame step (PARTLY CLOSED). SACD cuts bias scores (FOMC llama3.1-8b 0.3805 to 0.1570; PubMedQA 70b 0.4730 to 0.0560) and DeFrame cuts fairness framing disparity 92% (4 calls). Neither reports task accuracy at equal tokens, SACD's "loss aversion" is a punishment-warning prompt, not lambda, and CoT, few-shot and debate sometimes raised bias (d06-d08). Kraishan: extra thinking tokens did not reduce bias (Delta +0.031, p=.157); a one-line restate-the-anchor step did lower anchoring (5 of 5 items, p=.057) (d04, d05). Still open: accuracy on real tasks at equal tokens.
2. Design-matched human lambda (STAYS OPEN, narrowed). Brown et al.: mean 1.955 [1.824, 2.104], median 1.69, field and general samples higher, surveys lower, money type no clear effect, only 14.4% of heterogeneity explained (d11, d12). Yechiam & Zeif: about 1.07 for symmetric unordered lotteries, 84 papers, 163 estimates (d13). No single incentivised, symmetric, same-scale estimate found. Working rule: 1.07 for symmetric designs, 1.8 to 2.0 for loss-skewed designs.
3. Prompt contamination (PARTLY CLOSED). In ChatGPT-4o and Qwen2.5-72B, prompting with human loss-aversion behaviour or papers moves lambda (ChatGPT 1.785 after Brown vs 1.043 after Yechiam & Zeif; control 1.09; Qwen 1.742 vs 0.940 in Study 3) (d09, d10). Still open: reasoning models, other vendors, a bias name in a system prompt.
4. Reasoning models and EV (CLOSED for lottery items). RM-vs-EV correlation 0.86 to 1, CM below 0.5, RMs invariant to order, frame and explanation, further from humans than CMs (d01, d03); Kraishan finds loss aversion leans against the human direction, like an EV maximiser (d05). Whether EV-like is preferable for human-value decisions is a design judgement, not settled by data here.
5. Lambda stability (PARTLY CLOSED). Wang et al.: 256 samples per lottery at T=0.7; fits below R2 0.10 or MAE above 0.20 are unreliable; Qwen2.5-32B baseline 1.213 vs 0.95 to 2.01 across rounds; verbal wording shifts lambda (d14, d15). No paper gives a required run count; Ge et al. found 10 vs 50 samples changed little for choice rates (d01).
6. 1979 problems and 2020 battery in LLMs (STAYS OPEN). No LLM study reproducing P1-P14 or the Ruggeri battery with choice shares was found; searches could not be run. Wang et al. fits PT but does not test those items (d14).
7. Description-versus-history gap (PARTLY CLOSED). Qualitative result confirmed: all LLMs move toward humans with histories, little for GPT-5.1 and DeepSeek-R1, a lot for chat models and open reasoning models; humans move toward EV (d02). Per-model decisiveness numbers are only in figures and were not extracted. It is the larger lever for chat models than loss aversion.
8. Territorial replication (CLOSED on status). It is a PsyArXiv preprint v2 (28 Jul 2025, modified 21 Aug 2025), no journal peer review found; item replication 69% and 81%, theoretical contrasts 77% and 92%, reflection effect not robust (d16).
9. Persona leakage (STAYS OPEN). The GPT-4.1 persona study shows d=4.15 inside a gambling task, but goal text differs per persona and no neutral-task transfer or guardrail was tested (d17).
10. KTO loss weights outside training (CLOSED, negative). lambda_D and lambda_U are training hyperparameters with default 1 and a 1 to 1.5 ratio rule; no scaffold-side use found (d18).

Claims changed: K01, K05, K10, K11, K13, K14, K15 gained evidence ids or caveats; K19 to K25 added.
