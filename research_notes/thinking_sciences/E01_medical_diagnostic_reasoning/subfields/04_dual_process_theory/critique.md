# Critique: E01.04 Dual-process theory (cross-check)

## Numbers re-opened this session (arXiv full text via pdftotext)
Confirmed: Hagendorff et al. (CRT 38% human, 59% / 96% ChatGPT-3.5 / 4; davinci 5% to 28%, intuitive 80% to 29%; blocked CoT 97% to 0%, 84% to 0%, p=.49, 95% to 88%); Savage et al. (GPT-4 76 / 77 / 78 / 78 / 72 with p-values); SwiftSage (84.7, 45.3, 36.4, 33.8; tokens 757.07 vs 1855.84 / 1971.03 / 2983.46; ReAct 36.43 to 19.76); Sprague et al. (110 papers, 1,218 comparisons; 14.2 / 12.3 / 6.9; 56.9 vs 45.5; up to 95% of MMLU gain); S2A (62.8, 82.0, 80.3, 51.7, 61.3); Distilling (30.0, 44.5, 98.0, 75.69, 76.0, 81.3, 9.40); Liu et al. (87.5 to 64.4, 64.0 to 51.2, 44.0 to 29.6, 331%); Wu et al. (95 LLMs, 87 tasks, 82 of 95 = 86.3%, Gemini-2.5-flash -1.6, R1 -2.1, GPT-4o -3.5).

## Corrections
1. Liu et al. (a14, b20, c14): "o1-preview 57.7% vs GPT-4o 94.0%" is NOT a CoT-prompting effect. It compares o1-preview (built-in reasoning) with GPT-4o zero-shot on a 440-item subset. The clean prompt-CoT effect on GPT-4o is 87.5 to 64.4 (-23.1). Line b20 "GPT-4o subset 94.00%, 36.30 points lower with CoT" should read "o1-preview 36.3 points lower than GPT-4o zero-shot".
2. ChatGPT-4 correct is 96% in the main CRT result and 95% as the Study 2 baseline for the blocked-CoT comparison (95 to 88). Different conditions, not a conflict.
3. Schmidgall et al. (a15, b23, c20): the evidence says GPT-3.5 average drop -17.8%, but the paper text also says GPT-3.5 "average drop 37.4% across all biases" (absolute and relative drops seem mixed). Per-model drops are unreliable until the tables are read. The ranking (GPT-4 least affected, false consensus worst at 24.9% averaged) is confirmed.
4. Semantic illusions: human intuitive share is 64% in the authors' sample vs 52% in the original (n=61); do not cite 52% as an LLM-comparable number.
5. Pelaccia 95% first-five-minutes figure remains secondhand (Neufeld). Not primary.

## Contradictions between sources
- Reflection: Mamede 2010 shows induced availability bias fixed by reflection (N=36); van den Berg 2021 (N=117) could not induce availability bias at all. The 2010 effect may be small-sample or primer-specific.
- Bias teaching: Sherbino 2011 and 2014 find nothing; Lambe 2018 review says guided reflection worked in 5 of 28 studies. Not necessarily in conflict (reflection vs forcing), but no pooled effect exists.
- LLM mode: older models fall for traps and CoT rescues them; strong models fall less and CoT can lower clinical accuracy (Wu 2025). The direction of "slow is better" flips with model strength and task type.
- Default-interventionist vs conflict-detection (Bago/De Neys vs classic Kahneman/Evans) is open; Evans and Stanovich 2013 concede parts.

## Weak spots
- Many human clinical studies were abstract-only (a16 to a21, b01 to b03, b06 to b09, b11 to b15 not opened). Their numbers rest on abstracts.
- Frederick 2005, Evans and Stanovich 2013, Evans 1983 not opened. a24 figures are from memory; do not use.
- b26 (JMIR 2026 dual-system pipeline, +10 to 39 points) is a search summary only. Unverified.
- Bago and De Neys exact percentages not read. Bouwmeester RRR numbers not re-checked by me.
- No source tests an LLM scaffold that routes fast vs slow at equal tokens in medicine. All LLM work compares CoT on/off.
- Hagendorff CRT items are bespoke but may sit in newer models' training data.

## Only seen in snippets
b26; a24; the b16 meta-analysis counts (51 studies, N=15,850).

## GAPS
1. At equal tokens, does routing by a confidence or agreement signal beat always-CoT and never-CoT on medical diagnosis benchmarks (MedQA, NEJM cases)?
2. Do reasoning models on open-ended diagnosis (not multiple choice) show anchoring and premature closure, and does a forced differential step reduce them?
3. What is the per-model per-bias table in BiasMedQA (absolute vs relative drops), and does a challenge step close the gap?
4. Is the 2026 dual-system pipeline result (conversational model plus reasoning model, +10 to 39 points) real, and was it token-matched?
5. Does response length cause LLM diagnostic error (Moell: 8,118 vs 3,648 characters) or only mark hard items?
6. What did Bago and De Neys find exactly (percent correct first answers), and does an LLM first-sample/second-sample analogue exist?
7. Does retrieval of similar cases (the knowledge view) beat added deliberation for LLM diagnosis at equal tokens?
8. Has the Mamede 2010 reflection effect been replicated beyond N=36, in humans or LLMs?
9. Which 2025-2026 LLM studies test explicit System 1/System 2 switching beyond SwiftSage, and with what token accounting?

## Gap search results (evidence_d.jsonl, d01 to d18; claims K23 to K29 added)
Search note: WebSearch budget was spent, so I used Europe PMC full text, arXiv PDFs and PubMed. Two sources were blocked (Bago full text behind a bot check; arXiv and Semantic Scholar search APIs rate-limited).

1. Routing at equal tokens (OPEN). Still no study. Nori 2024 gives MedQA accuracy against cost (GPT-4o 84.4, GPT-4 Turbo Medprompt 90.2, o1-preview 96.0; roughly $5 / $50 / $500 per 88 / 92 / 96%) but no router. Griot 2025: most models say confidence 5 on everything, so verbal confidence is a weak signal (d14, d17). K24, K25.
2. Anchoring in open-ended diagnosis (PARTLY). Ke 2024: a challenge-and-differential agent team went from 0/80 first answers to 76% top-2 on bias-linked case reports. The 0% is by case selection and there is no equal-token control. Brodeur 2024: o1-preview has the right diagnosis in its list 78.3% but first only 52%. No test of reasoning models' anchoring on open cases was found. K26, K27 (d07, d08).
3. BiasMedQA table (CLOSED). The "-17.8" style numbers are absolute points; "37.4%" is relative (GPT-3.5: 0.497 to 0.311 mean = -18.6 points = -37.4%). GPT-4: -5.4 points. A short warning or demo lifts GPT-4 mean from 0.673 to 0.709 (education) or 0.749 (few-shot, own no-bias 0.757), little for weak models. No reasoning-on test. K15 rewritten (d01 to d03).
4. JMIR 2026 dual-system (CLOSED, claim weakened). Real (Zuo, Wan, Wang; 1,273 MedQA cases). Gains up to +38.7 points under biased dialogue, but o1-mini alone scored 85.1% biased, above every dual result (best 75.5%), and tokens were not matched. It is a model-swap result, not evidence for a router. K23, K16 (d04, d05).
5. Length as cause (PARTLY). Moell: t=-2.74, p=.032, based on 7 wrong answers; 1 of 7 coded as anchoring. Nori: prompting o1 for longer reasoning raised accuracy. So length marks hard items; no causal test. K04 (d06, d15).
6. Bago and De Neys (OPEN on numbers). Only the abstract was readable; exact percentages not obtained. LLM analogue found: Huang 2024, second pass without an outside signal does not help (GPT-3.5 CommonSenseQA 75.8 to 41.8; GSM8K 75.9 to 74.7), while oracle labels do (84.3 on GSM8K). K05 (d12, d13).
7. Similar-case retrieval vs deliberation (OPEN). Only document retrieval tested: no gain over CoT on MedQA-US (GPT-4 83.97 to 82.80; Mixtral 64.10 to 60.02), not token-matched. A 2026 Nature rare-disease agent (PMC12999473) uses case retrieval and was not read. K22 (d16).
8. Mamede replication (CLOSED: no independent success). Independent Japanese RCT (N=46) induced availability bias but reflection did not repair it; van den Berg (N=117) induced none; the supportive follow-ups are from the same group. No LLM test found. K03, K28 (d10, d11).
9. 2025-2026 explicit S1/S2 switching beyond SwiftSage (MOSTLY OPEN). Found: AdaptThink (learned Thinking/NoThinking switch; math; -53% length, +2.4% accuracy) and the JMIR pipeline. No scaffold-level medical switch with token accounting found. K16 (d04, d18).

Corrections to the earlier notes: the BiasMedQA mismatch is a units issue, not an error in either number; the JMIR "+10 to 39" excludes GPT-4o (-1.0) and ignores that o1-mini alone beats the pipeline; "anchoring" in Moell is 1 of 7 errors.
