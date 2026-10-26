# D05.07 Bias and debiasing: cross-check critique

Cross-checker pass. Sources re-opened this session as full text (PDF via pdftotext, or abstract via OpenAlex): Sellier et al. 2019 (author manuscript), Many Labs 2 (abstract), BiasBuster 2403.00811, SACD 2504.04141, CogBias 2604.01366, Hagendorff 2212.05206, Lou and Sun 2412.06593, Turpin 2305.04388, Huang 2310.01798, Wang 2305.17926, Itzhak 2308.00225, Knipper 2509.22856. Malberg (abstract only) and SynAnchors (not retrievable) were not re-verified.

## Corrections made

1. Sellier 2019 headline. Evidence a12/a15 (via Korteling) say "19% less likely"; b01 and the manuscript say "29% less likely". The raw numbers (58.8% vs 72.2%) give a relative risk of 0.81 (19% lower) and an odds ratio of 0.549 (45% lower odds). Neither equals 29%. Use the raw percentages (a 13.4 point drop). Source of 29% unresolved. Also: 26 participants were excluded for prior familiarity, and 22 untrained participants (20.4%) did not complete a gaming session (the manuscript says excluding them does not change results). Confirmed: N=290 (182 trained, 108 untrained), p=.022, OR .549, CI [.33,.92], short lag 56.8% vs long lag 63.2% (p=.419).
2. Hagendorff 2023 human sample. c20 says "human sample difficulty check: 38% correct versus 41% in the original study (n=3,428)". The n=3,428 belongs to the original published study. The new human sample was 500 Prolific participants (a07 is right). Numbers 5/59/96% correct, 80/15/0% intuitive, 38% and 55% for humans: confirmed. "Let's use algebra" 5 to 28% correct, 80 to 29% intuitive: confirmed. Semantic illusions (a07): 18 to 54% with "Think carefully and check the question for invalid assumptions", 72 to 28% intuitive: confirmed. c21 and a07 describe two different suffixes (CRT vs semantic illusions); not a conflict.
3. BiasBuster table: GPT-4 framing gaps -0.405 base, -0.470, -0.410, -0.570, -0.010 and GPT-3.5 0.165, 0.035, -0.080: confirmed. Note the GPT-3.5 and GPT-4 baselines have opposite signs, so "awareness helped GPT-3.5" means the gap shrank toward zero. The 0%/2.7% for GPT-4 (c03) is the share of biased prompt elements remaining after self-help, not an outcome gap. The "40-52%" Llama figure was not re-found in the extracted text; keep as unverified.
4. Knipper 2025 (c11/c12). The abstract says ">32B can reduce bias in 39.5% of cases"; the body says "reduce bias susceptibility by up to 39.5%". These are different quantities (share of cases vs size of reduction). Treat as ambiguous. Abstract also says Overattribution got worse by up to 8.8% with detail; c12 quotes 8.2% for a Level 1 to 2 move. Both exist; do not merge. Gains of 6.5 to 14.9% confirmed.
5. Turpin 2023 (b20): the "-30.6 to -21.5" for Claude 1.0 is zero-shot vs few-shot on Suggested Answer (zero-shot -30.6, few-shot -21.5), not a range of conditions. Zero-shot CoT lowering biased-context accuracy 39.5 to 23.3 (GPT-3.5) and 37.3 to 34.7 (Claude) compares No-CoT to CoT: confirmed. "Of 426 explanations supporting biased predictions only 1 explicitly mentions the bias": confirmed in the paper text (for a subset of the biasing setup; it is not a rate across all tasks).
6. Huang 2024 (c24): GPT-3.5 CommonSenseQA 75.8 to 38.1 occurs at the 3-call setting (after round 1). The GPT-4 GSM8K 95.5 to 89.0 is after round 2 (5 calls), not round 1. Oracle numbers confirmed (84.3, 89.7, 29.0).
7. CogBias (c08/c09): the "debiasing effect" is metric(neutral) minus metric(biased), where the neutral condition adds a debiasing instruction. Family numbers (+40.5, +5.9, -1.1, -4.4) confirmed. The per-bias table is garbled in text extraction; the labels beside -21.0, -19.6, -16.6 and -13.4 may be misaligned. Quote only the family-level numbers as reliable. Also, "Social +5.9%" is the share of "cannot be determined" answers, which is partly refusal behaviour.
8. Lou and Sun (b18, c13): 62 questions is the full dataset, 15 questions were plotted for Both-Anchor. Anchoring index about 0.45 (GPT-4) vs 0.61 (humans): confirmed.
9. SACD (a06/c04/c05): iteration scores 0.2070, 0.1460, 0.1175 (finance) and vanilla 0.6655 medical, 0.3840 and 0.4590 legal: confirmed. Debate 0.5155 and Reflexion 0.5585: confirmed.
10. Many Labs 2: abstract numbers confirmed (15 of 28, 54%; median d 0.60 vs 0.15; 16 small; 9 opposite; 11 (39%) significant Q heterogeneity). In b09, "19 of 28 near zero heterogeneity" and "13 of 14 reliable effects in both WEIRD and less-WEIRD" were not in the abstract and are unverified. The two abstract versions differ slightly (eight vs nine other effects with tau near .10).
11. Itzhak 2024 (a02/c17): certainty 0.24 to 0.67, belief-invalid 0.00/0.55/0.65: confirmed. Table cells with asterisks mean significance, not footnotes.

## Contradictions between sources

- Awareness prompts: harmful on GPT-4 framing (BiasBuster), mixed or helpful on GPT-3.5 (BiasBuster, Sumita), helpful at 6.5 to 14.9% (Knipper levels 3 to 4), backfire on judgment biases (CogBias), sign flips with persona (c27). Net: no reliable direction. All "helps" findings are small and per bias.
- Chain of thought: rescues davinci-003 on CRT (5 to 28%) but hurts GPT-3.5 in biased context (39.5 to 23.3), enlarges consistency bias (Opedal), fails for anchoring (Lou and Sun), raises stereotypes (Shaikh). Model and task decide.
- Self-correction: SACD's rewrite loop works while Huang says intrinsic self-correction fails. Likely reconciliation: SACD edits visible cues in the input, which the model can see; Huang asks the model to judge the truth of its own reasoning, which it cannot. SACD's first pass was also worse than vanilla in finance.
- Scale: Malberg says larger OpenAI models somewhat more biased; Knipper says over 32B reduces bias in some cases; SynAnchors says reasoning models least anchored. Different bias sets and metrics.
- Pretraining vs tuning: Itzhak 2024 (tuning raises bias) vs Itzhak 2025 (backbone dominates).
- Human training: Sellier and the games (positive) vs Korteling and Willingham (little transfer evidence). Most positives come from one programme.

## Weak spots

- Most LLM studies plant the cue in the prompt text, so "debiasing" there means detecting and deleting text. This does not test biases that arise inside the model.
- Models are from 2022 to 2024 in many studies (GPT-3.5, Claude 1.0, Llama-2). Frontier 2026 reasoning models are barely covered.
- Human evidence is largely secondary: Fischhoff 1982, Lord 1984, Sanna 2002, Fong 1986, Gigerenzer 1995, Sedlmeier 2001, K and T 1996 were never opened (a22 to a29 are from memory or citations).
- Sellier is quasi-experimental; the trained group had higher CRT.
- Bias scores differ across papers (rate gap, index, accuracy delta), so cross-paper size comparison is unsafe.
- No study tests a debiasing scaffold at equal tokens against a plain model on non-planted biases (our G7 test).

## Only seen in snippets or secondary text

a14, a15 (secondary via Korteling), a20 (secondary), a21 to a29, b26 (abstract only), c28, c29 (abstract and intro), Malberg (abstract only this pass), SynAnchors (not re-opened), Many Labs 2 per-effect rows (b07, b08).

## GAPS

1. Does any scaffold-level debiasing step (neutral restatement, opposing references, forced disconfirming test) beat a plain model at equal tokens on biases not planted in the prompt, for a 2026 reasoning model?
2. Do frontier reasoning models (Claude, GPT-5-class, o-series, DeepSeek-R1) show baseline bias on perturbed or unfamiliar bias items, and how large is it compared with Many Labs 2 replication sizes?
3. Does an explicit debiasing instruction backfire for current frontier models on judgment biases (CogBias used GPT-4o-mini, Llama-3.3-70B, Qwen2.5-72B), and is the sign stable across prompt wordings?
4. Why does Sellier's 29% (manuscript) differ from the 19% in the review, and has the study been replicated by an independent group?
5. Do the human consider-the-opposite and the number-of-alternatives boundary (Lord 1984, Sanna 2002) hold for LLMs: does asking for 1 vs 5 counter-reasons change drift?
6. How much of SACD's gain survives when the cue is not planted by the authors, and does it hold at equal tokens against best-of-N?
7. Does LLM-as-judge position and self-preference bias persist in 2025 to 2026 judges, and how much does swap-and-aggregate cost at equal tokens?
8. Is bias in an agent's long context (history turns, tool outputs) measurable and removable by context pruning in code (Weerasekara found neutral turns alone raise bias)?
9. Do independent replications exist for the serious-game debiasing results (Morewedge 2015, Clegg 2014/2015) and for the frequency-format training retention (Sedlmeier 2001)?
10. Does post-training (RLHF, reasoning RL) add or remove bias in 2025 to 2026 models, resolving Itzhak 2024 vs 2025?

## Gap search results

Gap searcher pass. Evidence lines d01 to d19 in evidence_d.jsonl, claims K34 to K41 added, K01, K03, K04, K10, K11, K13, K16, K21, K22, K25 updated. WebSearch quota ran out after two queries, so the rest used arXiv, Europe PMC, Crossref and direct PDF reads. Nothing here replaces the full-text human sources (Lord, Sanna, Fischhoff, Sedlmeier), which were still not opened.

Status by gap:

1. Scaffold step vs plain model at equal tokens, unplanted biases, 2026 reasoning model: STAYS OPEN, partly informed. Best new evidence: Sovrano 2026 (d06). Having the model write the neutral best practices first cut sensitivity from 12.9% to 6.3% (p<.001), while a bias warning gave -4.6 points (not significant per bias) and chain of thought raised it to 16.1%. But the models are cheap (GPT-4o-mini, GPT-4.1 family, Llama, R1-distill), the cue is still wording in the prompt, the method uses extra tokens, and there is no equal-token or best-of-N arm. Chain-of-Models (d11) shows a cross-family audit lifting planted-cue accuracy from 0.805 to 0.884, again planted cues and an extra call.
2. Baseline bias of frontier reasoning models: MOSTLY CLOSED for existence, OPEN for size against Many Labs 2. Claude Sonnet 4.5 and Gemini 2.5 Pro show opening-to-final price rho of 0.78 and 0.91 (d07). Reasoning models have the lowest anchored share, about 22-25% of questions, not zero (d08). o1 lost as much as GPT-4o to a seller anchor unless warned (d09). No paper gave a replication-size comparison with Many Labs 2 (d about 0.15 median). Model-level table totals in SynAnchors were misaligned in extraction and are not quoted.
3. Backfire of debiasing instructions on frontier models, sign stability: STAYS OPEN. No 2025-2026 paper tested GPT-5-class or Claude 4-class on CogBias-style judgment biases. Evidence is mixed in sign: warnings help a little, not significantly, on cheap models (d06), help reasoning models when the warning names the real cue (d09), and a generic reminder slightly raised anchoring on 7-8B models (d08). No backfire was found, but none of the tested models are frontier 2026. K02 stays single-source.
4. Sellier 29% vs 19%: PARTLY CLOSED. The manuscript abstract does say 29%; the results give 58.8% vs 72.2% (relative drop 19%, odds ratio .549). The text never derives 29%. One cell (4-day window) has exp(b)=.29, which may be the source, but this is a guess (d01). No independent replication found. The 2025 risk-analyst study (d02) is by Morewedge and Scopelliti, pre/post, no control group.
5. Consider-the-opposite and number of alternatives in LLMs: OPEN. Several searches found no LLM study that varies 1 vs 5 counter-reasons. Lord 1984 and Sanna 2002 are still unopened secondary text (K24 unchanged).
6. SACD gain when the cue is not planted, and vs best-of-N: STAYS OPEN. PROBE-SWE (d05, d06) uses minimal wording edits made by the authors; no SACD rerun on those. No best-of-N arm anywhere.
7. Judge position and self-preference bias in 2025-2026 judges, cost of swap-and-aggregate: CLOSED for persistence, OPEN for cost at equal tokens. Kumar 2026 (d14): GPT-5.2, Claude-Sonnet-4.6, Gemini-2.5-Pro, GPT-4o all show order flips on JudgeBench (11%, 15%, 56%, 24% under the direct prompt); reruns at temperature 0 change 7-17% of verdicts; one-call rubric scoring lifted Gemini-2.5-Pro from 28.9% to 77.9% trustworthy rate, while four-call decomposition lowered it for five of six judges. Self-preference: Chae 2026 (d15) finds none when blind but a +0.43 label effect on a 7-point scale; Guey 2026 (d16) finds none on a verifiable task (gap -5.1 points, CI [-12.9, +2.7], underpowered). K11 moved to contested.
8. Long-context or history bias and pruning: HALF CLOSED. Weerasekara 2026 (d17) shows any preceding user turn raises bias (+0.086 Llama-3.1-8B, positive in 7 of 8 models), but it tested user turns only, on 2024-vintage models, and did not test removal by pruning. Tool outputs untested.
9. Independent replication of serious-game and frequency-format training: STAYS OPEN. Only same-lab follow-ups (d02). For frequency formats the McDowell and Jacobs 2017 meta-analysis gives 24% vs 4% (via Weber 2018, d03), which supports the wording effect but not retention. Sedlmeier 2001 unopened.
10. Post-training effect on bias, Itzhak 2024 vs 2025: PARTLY CLOSED. The two papers answer different questions: 2024, instruction tuning shifts certain biases; 2025, the pattern across 32 biases is set by the backbone (d04). Both papers cover 7-11B models and supervised tuning only. RLHF and reasoning RL on 2025-2026 models: no evidence found, so open.

Corrections to earlier notes found during this pass:

- Ye et al. 2024 (CALM) bandwagon robustness: Claude-3.5 is 0.610 and GPT-4o 0.791 (distraction is the column where Claude is 0.878). Check any older note that mixed these.
- Shi et al. 2025 table text is garbled for the Claude rows, so only GPT, Llama and Gemini rows are quoted.
- SynAnchors Table 1 rows do not align with labels in extracted text. Do not quote per-model totals.

New items worth a separate look next: no LLM study tests counter-reasons count; no frontier 2026 test of generic debiasing instructions; no equal-token comparison of any debiasing step.
