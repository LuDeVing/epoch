# Cross-check: Chain-of-thought prompting (C01.01)

Checked by re-opening the full PDF text (pdftotext) of 11 papers and comparing with evidence_a/b/c. PDFs were deleted after checking.

## Numbers re-checked (all against full text)
1. Wei 2022, PaLM 540B GSM8K 17.9 -> 56.9 (+39.0); SVAMP 69.4 -> 79.0; ASDiv 72.1 -> 73.9; AQuA 25.2 -> 35.8; MAWPS 79.2 -> 93.3. Confirmed. LaMDA 420M GSM8K 2.6/0.4 and 137B 6.5/14.3, AQuA 25.5 -> 20.6: confirmed.
2. Kojima 2022, MultiArith 17.7 -> 78.7, GSM8K 10.4 -> 40.7: confirmed (abstract and Table 1).
3. Wang 2022 self-consistency, PaLM GSM8K 74.4 (+17.9): confirmed. Correction: the paper's greedy CoT baseline is 56.5, not Wei's 56.9 (a re-run; 0.4 point gap). Do not mix them in one table.
4. Sprague 2025, means 14.2 / 12.3 / 6.9 and "as much as 95%" of MMLU gain on "=" questions: confirmed.
5. Turpin 2023, -36.3 (suggested answer, GPT-3.5 zero-shot), few-shot -24.1, -18.7 always-A, 39.5 -> 23.3: confirmed.
6. Liu 2024, GPT-4o artificial grammar 87.5 -> 64.4, face 64.0 -> 51.2 type values, 331% (2.9 -> 12.5 rounds): confirmed. Note the paper also re-ran a variant at 68.43% vs 87.5 zero-shot, so the drop is robust.
7. Chen 2025, faithfulness 25% (Claude 3.7) and 39% (R1); misalignment hints 20%/29%; RL plateaus 28% MMLU and 20% GPQA: confirmed.
8. Wang and Zhou 2024, first-100 GSM8K greedy 44.0 vs 72.0; full GSM8K PaLM-2 L 34.8 -> 63.2; Mistral-7B 9.9 -> 25.1: confirmed.
9. Meincke 2025, Gemini Flash 2.0 +0.135, Sonnet 3.5 +0.117, 100% metric -0.131 and -0.172, reasoning models +0.029/+0.031/-0.033, time cost 35-600% and 20-80%: confirmed. Extra: GPT-4o-mini also fell on the 100% metric (-0.091, p=.001), which a/b did not mention.
10. Suzgun 2022: PaLM answer-only 52.3 -> CoT 65.2; Codex 56.6 -> 73.9; abstract says CoT beats average human on 10/23 (PaLM) and 17/23 (Codex). Confirmed.

## Corrections made
- Stechly 2024 (b21/c23): the 59.3% is GPT-4 with the stacking-specific prompt; zero-shot GPT-4 is 3.83%. The statement "general prompts only 13.7-18%" is incomplete: general n-shot is 13.7/16.4/6.13 (GPT-4-Turbo/Claude-3-Opus/GPT-4), but the "Blocksworld Universal Algorithm" CoT reached 37.1/37.1/51.3. So the paper shows a broad algorithm prompt can help; what fails is generalising to larger stacks. Also: self-consistency dropped performance there. Claims K20 and K07 use the corrected form.
- Suzgun table text extraction is garbled (a "6/23" appears next to PaLM). Counts of tasks above human used only the abstract/headline (PaLM 10, Codex 17; answer-only 0 and 5). Intermediate counts (6, 4, 15) are ambiguous in extraction.
- c04 (Wei symbolic table values 49.3 -> 98.6 etc.) were flagged by the earlier agent as garbled column labels; not re-verified here. Treat as unconfirmed.

## Contradictions between sources
- Wei: CoT pre-answer helps; Meincke and Sprague: for modern models average gain is small outside math/symbolic, and Meincke finds more variance and fewer perfect runs. These are different model eras, not true contradiction, but the old headline overstates today's benefit.
- Turpin: zero-shot CoT worsened answers under a bias; Turpin also shows few-shot CoT improved them (35.0 -> 51.7 GPT-3.5). Prompt format changes the sign.
- Lanham 2023 (larger models less faithful) vs Chen 2025 (outcome RL improves faithfulness then plateaus): different measures; not directly comparable.
- Shojaee 2025 (collapse) vs Opus and Lawsen (artifact): unresolved; we mark contested.
- Wang 2022 (invalid exemplars keep 80-90%) vs Madaan and Wei (natural-language and relevance matter): compatible, but exact mechanism (format/relevance vs reasoning content) is open.

## Weak spots
- Sprague appears in a28-a30, b18-b20, c14-c15 as one source; counted once. This lowered several claims from "established" to "single-source" (K16, K17, K20 and others).
- Most mechanism evidence (ablations, exemplar validity) is from 2022 models (PaLM, GPT-3, LaMDA). Little tests the same thing on 2025-2026 frontier or reasoning models.
- Faithfulness evidence is about hints and bias; it does not show that unfaithful chains reduce accuracy, only that they cannot be trusted as explanations.
- Meincke is GPQA only, 198 questions; Liu has small tasks (six, three show drops).
- Equal-token comparisons are rare. Self-consistency and long-chain gains are mostly reported without matching token cost.
- Agent relevance entries use "G11 think briefly": no source directly measures a brief-vs-long budget on a modern model, only overthinking (Chen 2024) and inverted-U (Wu 2025).

## Only seen in snippets or not re-opened this session
- Not re-opened by me: Nye 2021, Madaan 2022, Lanham 2023, Shi 2023, GSM-Symbolic, Fu 2022, Zhou 2022, Arcuschin 2025, Wu 2025, Chen 2024 (overthinking), Shojaee, Opus and Lawsen, Pfau, Merrill, Feng, DeepSeek-R1, Shaikh. They rely on the first-pass agents (marked opened:true there).
- The "up to 65%" GSM-NoOp figure and Shaikh's 78% -> 25% are single examples as reported.

## GAPS
1. Equal-token test on a modern frontier model: does a short (G11-sized) chain, a long chain, and k short chains with a vote differ in accuracy per token on multi-step reasoning items?
2. Where is the knee of the thinking budget by difficulty tier for current reasoning models, and does a cheap difficulty gate beat always-think?
3. Does an explicit "think step by step" instruction harm or help models that already reason internally, beyond GPQA (Meincke) and across other task types?
4. How often does a modern model's stated chain cite a misleading hint it used, and does a verification step (G10) catch the cases the chain hides?
5. Which part of the gain is executing symbolic steps vs planning, on current models, and does tool execution at equal tokens beat written-out execution?
6. Which task types show CoT harm in current models (statistical learning, perception, intuition), and is the harm reproducible across vendors (Claude 3.5 Sonnet showed none on grammar)?
7. Do the Wang 2022 invalid-exemplar results hold for current models, i.e. is the lever format and relevance rather than correctness?
8. Does vote share among sampled chains calibrate confidence well enough to trigger extra checking, and what is its cost versus its benefit?
9. How does the Shojaee collapse result change when output limits and impossible instances are controlled (Opus and Lawsen), on models with larger output budgets?
10. Do CoT gains survive distractor and perturbation items (GSM-NoOp type) on 2026 models, and does an "ignore irrelevant information" line help at equal tokens?

## Gap search results (evidence_d.jsonl, d01-d15)

Method: full text (pdftotext) of 12 papers opened; web search budget was exhausted, so no new search for follow-ups to Shojaee. PDFs deleted afterward.

1. Equal-token test: PARTLY CLOSED. Hassid 2025 (d01): for reasoning models, the shortest sampled chain beats random (+2.2 to +15.7 points on math) and longest (up to +34.5); short-3@k beats majority vote at all budgets. Wu 2025 (d03) and Balachandran 2025 (d04) show saturating returns and a weak link between tokens and accuracy. Still open: a brief-chain vs long-chain vs k-short-vote test on a non-reasoning frontier model at matched tokens.
2. Knee of the budget by difficulty: PARTLY CLOSED. Snell 2024 (d02): allocation by difficulty bin gives about 4x compute saving; search hurts on easy bins and fails on the hardest. Evidence is for verifier search on PaLM 2 / MATH. Whether a cheap gate beats always-think on current reasoning models is not measured.
3. Explicit CoT instruction on reasoning models beyond GPQA: PARTLY CLOSED. Li 2025 (d06): CoT lowers instruction-following in 13 of 14 models, Claude 3.5 Sonnet 86.5 -> 79.5; reasoning variants no better than base (Claude 3.7 90.2 vs 90.6). Gema 2025 (d05) adds longer-reasoning harm on distractor tasks. Not tested: adding "think step by step" to o-series style models across many task types.
4. Chain cites the hint; does verification catch hidden cases: HALF CLOSED. Chua and Evans (d13): R1 names the cue 59% (non-reasoning best 13%), other cue types near 0% for all. No study found that tests an independent verification step on the unstated cases. Open.
5. Symbolic execution vs planning, tool vs written at equal tokens: STAYS OPEN. PAL (d11) shows tool execution is robust (GSM-Hard 61.5 vs CoT 20.1) but is 2022-era and not token-matched.
6. Task types where CoT harms, across vendors: PARTLY CLOSED. Claude models now show harm on instruction following (d06) and distractor counting (d05), though not on grammar (Liu). Statistical learning and perception on other vendors still rest on Liu 2024 only.
7. Invalid exemplars on current models: PARTLY CLOSED, indirectly. Li 2025 (d12): content errors cost little and step order costs a lot in long-CoT fine-tuning. This is training, not prompting; a prompted invalid-exemplar test on current models was not found.
8. Vote share calibration and cost: LARGELY CLOSED. CISC (d09): within-question confidence beats plain voting, over 40% fewer samples on average, and the best-calibrated score was the least useful. Adaptive-Consistency (d10): up to 7.9x fewer samples, under 0.1% accuracy loss. Caveat: no test of vote share as the trigger for a separate verifier.
9. Shojaee vs Opus and Lawsen: PARTLY CLOSED, stays contested. d14: River Crossing N>=6 (capacity 3) is unsolvable; Hanoi N=15 solved as code in under 5,000 tokens (preliminary, no trial counts). Opus and Lawsen's own text says the collapse before N=9 comes earlier than the token limit, so the output-cap story is not complete. No larger-budget rerun found.
10. Perturbation items on 2026 models: PARTLY CLOSED. CatAttack (d07): error rates up 300-500% for reasoning models; an ignore-distractors line cut attack success 37.5% -> 9.9% on one 8B model (not equal-token). GSM-Plus (d08): GPT-3.5 CoT 74.17 -> 62.92. Gema (d05): inverse scaling in Claude and DeepSeek. No 2026 frontier-model GSM-NoOp rerun found.

Net: only gap 8 is largely closed. New claims K28-K33 added; K30 is the only one rated established (three sources). K23 stays contested. Li 2025 (d12) baselines were read from garbled tables and are approximate.
