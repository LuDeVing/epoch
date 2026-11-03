# Critique: Failure-driven CBR (C08.10)

Cross-check run on 2026-11-03. Sources re-opened from arXiv PDF text (pdftotext) for the 10 checks below.

## Corrections made (10 numbers re-checked)

1. Huang et al. 2024 (arXiv 2310.01798) Tables 2 and 3. CONFIRMED: GPT-3.5 CommonSenseQA 75.8 to 38.1 (3 calls) and 41.8 (5 calls); GSM8K 75.9 to 75.1 to 74.7; GPT-4 GSM8K 95.5 to 91.5 to 89.0. CORRECTED c12: its oracle numbers "GPT-3.5 GSM8K 75.9 to 95.5, HotpotQA 26 to 49" are wrong. Real oracle values: GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 GSM8K 95.5 to 97.5, CSQA 82.0 to 85.5, HotpotQA 49.0 to 59.0. (c12 mixed GPT-4 baselines into GPT-3.5.) a25 and b16 are right.
2. ExpeL (arXiv 2308.10144) Table 2, ALFWorld. CORRECTED: a19 and c04 say "ExpeL 54% vs Reflexion 59% at R3". The caption says the highlighted 59.0 is ExpeL with ONE attempt; ReAct+Reflexion goes 40.3, 47.8, 52.2, 54.4 over R0-R3; ExpeL retrieve-only plus Reflexion 54.5 to 60.4; full ExpeL plus Reflexion 59.0 to 64.2. b06 and b08 (59.0 vs 54) are right. Row labels are garbled in text extraction, so the mapping is inferred from the caption and Fig. 5 (59.0).
3. Reflexion (2303.11366) Rust ablation. CONFIRMED: 0.60 base; 0.52 (tests off, reflection on); 0.60 (tests on, reflection off); 0.68 both. The 16.3% vs 1.4% false-positive rates, 22% hallucination rate and +8 reflection boost are confirmed in the text.
4. ReasoningBank (2509.25140). CONFIRMED: Shopping, Gemini-2.5-flash: no memory 39.0, Synapse 40.6, AWM 44.4, ReasoningBank 49.7 (main table, with failures). Text: Synapse 40.6 to 41.7 and AWM 44.4 to 42.2 when failures are added; ReasoningBank 46.5 success-only to 49.7. Real-judge accuracy 72.7% confirmed. Warning: 46.5 also appears as the Gemini-2.5-pro Synapse number in another table; do not mix them.
5. Olausson (APPS) 33.30 vs 52.60 and the per-level numbers: CONFIRMED in table text.
6. Tsui (2507.02778): CONFIRMED 64.5% blind spot, 179.5% more correction markers on GSM8K-SC, 89.3% with "Wait", 5,306 traces gives 76.0% reduction. Frontier models in the paper: Claude 3.5 Haiku 52.5%, Sonnet 4 41.4% blind spot (not in the evidence files; worth adding).
7. Wang et al. negative-aware training (2402.11651): CONFIRMED +8.74 (7B, 2k), +0.52 (13B, 5k), -3.16 low-quality vs +8.74 high-quality, action error 4.01% vs 15.33%.
8. Tyen et al. (2311.08516): CONFIRMED 2186 traces, GPT-4 52.87, word sorting 23.53% fixed and 11.11% broken.
9. LEMA (2310.20689): CONFIRMED 83.5 vs 81.4, 25.0 vs 23.6, 29.3 with correction-centric evolution, CSQA 85.3 vs 84.2. Text confirms the equal-data-size exception is LLaMA-2-7B only. The "+0.3 to +4.6" cross-model range was not re-verified at its endpoints.
10. Dixit et al. (2026): CONFIRMED 0 of 121, 7.6 vs 1.5 trials, r=0.808, 134/156 (86%). AWM (2409.07429): CORRECTED b13: "SR 36.4 vs 40.9" are element-accuracy values in the cross-domain table; step SR is 32.6 offline vs 35.5 online (c10 is right on step SR); trajectory SR is 0.7 vs 1.7. The +12.0 points and 51.1% relative on WebArena and 24.6% relative on Mind2Web are confirmed. Memento (GAIA 87.88 validation, 79.40 test) and AgentDebug (24.3 vs 0.3; 45.0 vs 28.0) are confirmed.

## Contradictions between sources

- Reflexion (large gains from reflection) vs Xing et al. and Li et al. (no gain or a loss from reflection or hindsight on cross-app and HotpotQA tasks, GPT-3.5). Plausible resolution: reflection helps when the failure is an understandable execution error with a reliable signal, not when the cause is exploration or missing knowledge. Marked contested (K17).
- Reflexion and ExpeL (failures help) vs ReasoningBank (failures help only with a design that distils them; AWM and Synapse got worse). Same direction: memory design decides.
- Huang et al. (self-correction hurts) vs Reflexion (self-reflection helps). The difference is an external or oracle outcome signal. Reflexion's HumanEval gains rely on self-generated tests whose false-positive rate ranges from 1.4% to 16.3%.
- ExpeL: insights-only beats retrieve-only on HotpotQA but loses on ALFWorld. Task-dependent.

## Weak spots

- The founding classical work (Hammond CHEF 1986/1990, Riesbeck 1981, Schank 1982, Schank and Leake 1989) has NO quantitative evaluation. Claims K01 and K02 are design-level only; nothing measures the effect. Schank 1982, Hammond's thesis and 1990 paper, Kolodner 1993 (a08, a11, a12, a13, c20, c21) were not opened in full.
- Almost every LLM number is from one benchmark, one run, small N (HotPotQA 100, ALFWorld 134, WebShop 100), often with no confidence interval. Many gains are a few points.
- Most positive results use GPT-3.5 or GPT-4-class models from 2023. Current frontier models may self-correct differently (Tsui: Sonnet 4 blind spot 41.4%).
- Token cost is rarely matched. Only Mistake Notebook Learning (514 vs 9406 tokens) and LEMA's equal-size ablation report cost. Reflexion retries are extra samples, and best-of-N baselines are mostly missing.
- Fang et al. 2026 (a29) and Yin and Leake 2026 (c22) were not re-verified.
- No study isolates a "trap warning" lesson (avoid X because Y) from a positive recipe lesson. The direct LLM test of the CHEF idea is missing.
- ReasoningBank and Mind2Web tables were read from garbled extraction; column mapping was inferred.

## Seen only in snippets or not opened

a08, a11, a12, a13, c20, c21 (opened:false). Other lines are marked opened:true by their searchers; I trust them except where corrected above.

## GAPS

1. Does a stored failure lesson that names the trigger features, the causal chain and the repair beat a plain "what went wrong" reflection at equal tokens on held-out repeated trap families (the CHEF claim, never measured on LLMs)?
2. Does a trap warning (avoid X because Y) transfer better or worse than a positive recipe lesson, and how often does a warning fire wrongly on a non-matching task?
3. With a self-judged failure signal (no oracle), at what judge accuracy does a lesson store start to hurt? ReasoningBank says 70-90% is fine; Dixit shows confabulated lessons can loop. Needs a direct test on current frontier models.
4. How does the reflect-and-retry gain compare with best-of-N and plain resampling at equal total tokens on current models (Reflexion never matched sampling cost)?
5. Which failure types (execution, knowledge, exploration, bad plan) benefit from reflection vs exploration, and can a cheap classifier route them (the Xing vs Reflexion conflict)?
6. What lesson granularity and count K work best in the prompt: raw cases, strategy-level insights or clustered guidance? Memento K=4 and MNL 514 tokens suggest small, but nobody has swept both.
7. Do the 2023 negative results (Huang, Li, Tyen) still hold on 2025-2026 reasoning models, and does a "Wait"-style forced re-check (Tsui, 89.3% blind-spot cut) work as a cheap trigger inside the scaffold?
8. Does forcing a lesson to quote its supporting trace step (Dixit mitigation, 0% to 86% object mention) raise downstream success outside ALFWorld and HumanEval?
9. How should stale or wrong lessons be expired (Xiong: periodic plus history-based deletion helped)? Which deletion rule is best at equal memory size?
10. Is there any independent replication of CHEF-style indexed failure retrieval in modern CBR (ICCBR, 2020-2026) with a measured effect?

## Gap search results

Run 2026-11-03. New evidence in evidence_d.jsonl (d01-d18; d01-d16 opened from PDF text, d17 and d18 snippets only). Claims K21-K28 added; K03, K10, K11, K17, K18 extended.

- Gap 1 (CHEF-style lesson vs plain reflection, equal tokens): STAYS OPEN. Closest is Renze and Guven (d03): richer explanation and solution reflections beat bare retry (GPT-4 0.876 and 0.925 vs 0.827), but with an oracle wrong-flag and answer leakage, and tokens unmatched. No trigger-feature/cause/repair arm exists.
- Gap 2 (warning vs recipe): PARTLY CLOSED. MemGuard (d09): removing failure guards costs 1.1 to 1.9 points; removing governance costs 4 to 7. U-Mem (d05): failure-only 51.6 vs success-only 50.8 vs hybrid 52.4 (within noise). ConMem (d11) gives a firing rule for false suppression. No isolated test; false-fire rate on non-matching tasks still unmeasured.
- Gap 3 (judge accuracy break-even): PARTLY CLOSED. MemGuard verifier 86% agreement, 88.1% balanced accuracy; 30% simulated noise degrades but does not erase gains (d10). Break-even point not found; confabulation-style noise untested.
- Gap 4 (reflect-retry vs best-of-N at equal tokens): CLOSED for small models, OPEN for frontier. Mirzaei (d01) and Verma (d02): reflection never beats equal-cost resampling at 1.5B to 7B; code retry shows anchoring. Frontier models and external test signals untested. VRL-Bench (d04): retry-relative results mixed.
- Gap 5 (failure-type routing): PARTLY CLOSED. VRL-Bench (d04): an LLM scheduler choosing exploit vs explore was the only update positive over retry in all 6 settings; AgentDebug (d16) and Kamoi (d14) support typing the failure and the signal first. A cheap classifier alone was not tested.
- Gap 6 (granularity and K): PARTLY CLOSED. K=3 best in U-Mem (d06); raw episodes beat LLM-consolidated lessons over time (d07). Joint sweep not done.
- Gap 7 (2023 negatives on reasoning models): MOSTLY CLOSED. Reasoning models have a small or negative blind spot (d12); extra correction loops add marginal gains (d13). Wait trigger works on non-reasoning bases (0.567 to 0.902). Natural-error tests on frontier reasoning models missing.
- Gap 8 (quote-the-trace mitigation outside ALFWorld/HumanEval): STAYS OPEN. No study found.
- Gap 9 (expiry rule): PARTLY CLOSED. Periodic plus history-based deletion best with a reliable evaluator (d08); append-only loses 3.2 points (d05); governance is the largest component in MemGuard (d09). Equal-size head-to-head of rules for failure lessons not done.
- Gap 10 (CHEF replication in modern CBR): STAYS OPEN. ICCBR 2025 and CBR-LLM workshop searched (snippets only, d18); nothing measures failure-indexed retrieval.

Caveats: several 2026 sources are single-lab preprints; Xiong Table 2 and Zhang Fig. 1b were garbled in extraction so only prose claims were used; d17 and d18 not opened; claim statuses stay single-source except where noted.
