# B03.03 Active inference decision theory: cross-check critique

## Corrections made (sources re-opened this session, arXiv full text)
1. Sajid et al. 1909.10863: Table values confirmed (deterministic AIF 99.88, Bayesian RL 99.76, Q-learning 97.79; stochastic AIF 98.90 vs Q 66.08, BRL 64.39; null 50.03 / 50.22; goal 44.0%). No change.
2. Champion et al. 2303.01618: confirmed "even 1% of information gain dramatically decreases reward" and the single-action ("down") collapse. No change.
3. Hu et al. UoT 2402.03271: headline 38.1%, 46.6%, 33.8%, 29.9%, 28.3%, 12.4%, 97.0%, 43.7 to 67.3 all confirmed. CORRECTION/CAVEAT: the paper does not say whether 38.1% is relative or in points. Per-cell gains differ widely: Llama3-70B 20Q Common open-set 34.2 to 36.9 (+2.7), Thing 15.5 to 21.0, but DX 26.0 to 35.6 and MedDG 25.7 to 50.6. Headline scores use closed candidate sets (CS); open-set (OS) is much lower. Do not quote 38.1% as points.
4. Grand et al. 2510.20886: 0.227 bits, 94.2%, 0.367 to 0.764, 0.450 to 0.782, rho 0.684, 18.5% / 14.6%, human 92.5% confirmed. Win rate 0.82-0.83 vs humans confirmed; also 0.67 vs GPT-5.
5. Mazzaccara 2406.17453: INLG, Things, Celebrities rows confirmed (56.7/68.9/46.6; 51.1/61.1; 71.1/72.2).
6. BED-LLM 2508.21184: "+37.4 percentage points" confirmed; Table 4 static vs updating confirmed (Qwen Animals 95 vs 89, GPT-4o 93 vs 86; Llama-3.1-8B Animals reversed 63 vs 67).
7. Markovic 2101.08699: "A-AI outperforms bandit algorithms only up to T=10^4" for K=10 confirmed (the garbled "104" in evidence = 10^4).
8. Kobalczyk 2502.04485: values 6.2 / 4.1 / 5.1 / 4.9 (HumanEval, GPT-3.5, t=10) confirmed, but they are ACCURACY PERCENT of generated code on a filtered hard set (48 tasks), so absolute levels are low (4 to 7%). Also EIG-logprobs was the WORST variant in that cell; only EIG-uniform won. Evidence b19 should be read as "EIG helps, but estimator matters".
9. Bogdan 2606.15877: 17.3 points, CI [7.7, 25.5], 7,875 responses confirmed; the registered test used a 45-item subset of FEH-79, seven models.
10. Tschantz 2002.12636: "single trial", 25 episodes of at most 200 steps confirmed (author-run).

## Contradictions between sources
- Deep active inference: Tschantz 2019/2020 and Fountas 2020 report good results with information gain; Champion 2023 (independent reimplementation) finds every info-gain agent fails dSprites and notes discrepancies between Fountas paper and code. Unresolved; replication favours skepticism.
- Millidge says EFE is not a principled free-energy bound while Da Costa/Friston treat it as the definition. Practitioners choose the epistemic term; it is not forced by theory.
- Tabular active inference beats RL (Sajid) but approximate active inference is worse than UCB/Thompson in long stationary bandits (Markovic). Same family, opposite sign, depends on regime.
- LLM work: EIG question choice helps (UoT, BED-LLM) but Grand finds high EIG alone barely helps play; Kobalczyk finds logprob-EIG worse than implicit reasoning.

## Weak spots
- Almost all LLM gains use a hand-built hypothesis set with an LLM-simulated likelihood. Our agent's hypotheses will be open-ended; Mazzaccara and UoT-OS show gains shrink there.
- Gains are against weak baselines (direct prompting). Few compare to "same tokens, best-of-N" controls. Token cost of EIG estimation is rarely reported.
- None of the LLM papers call their method active inference; they use Bayesian experimental design. Support for "EFE" itself, including the pragmatic term, in LLMs is nil (Prakki, Duraisamy, Wen are qualitative or position papers).
- Many results are from preprints (2025-2026), not peer reviewed; several are single-group.

## Only seen in snippets or not opened
- Friston et al. 2015 (a04): not opened, no numbers. Friston 2017 graphical brain (a28): not opened.
- Wen 2025 (c27): search summary only.
- Handa OPEN exact figures not captured (b15, c18); BED-LLM Table 1 ranking read from prose only (c15).
- b27: no human experimental test found; search budget limits, not proof of absence.

## GAPS
1. At equal tokens, does EIG-ranked test selection (S7) beat an LLM simply choosing the most discriminating test from the same candidates, on open-ended (not enumerated) hypothesis sets?
2. How much of the EIG gain is lost with noisy LLM likelihood estimates, and which estimator (sampling, logprobs, entropy proxy) is best and cheapest?
3. Does adding a pragmatic/goal term to EIG help or hurt in LLM tasks (the Champion collapse vs the null-preference wandering)? Where is the weight sweet spot?
4. Does conditioning the next move on the test result (Grand's marginalisation) matter more than test choice in non-game reasoning tasks?
5. Is one-step EIG enough, or does 2-3 step lookahead (sophisticated inference) pay off after pruning at equal cost? UoT suggests one step captures most of it; needs confirmation outside 20 Questions.
6. Do hypothesis-compatibility filtering and a static likelihood (BED-LLM) transfer to math/code reasoning where hypotheses are candidate solutions?
7. Is there any human or animal behavioral data distinguishing EFE-style information seeking from plain expected information gain or reward models? (Search found none.)
8. Does the Bogdan finding (more chain-of-thought hurts under high meta-uncertainty) replicate, and does it imply a stop rule for S7 testing?
9. Do 2020-2026 papers exist that apply EFE or active inference directly to LLM agents with measured baselines (Prakki found only qualitative)?

## Gap search results (evidence_d.jsonl, d01-d19)
Tool limits: arXiv, Semantic Scholar and OpenAlex APIs returned HTTP 429 all session; WebSearch had one productive call. Sources came from direct PDF fetches and Europe PMC full text. Gaps 1, 2, 4, 5 and 8 could not be searched properly, so "open" below means not found, not proven absent.

1. Equal-token EIG vs LLM choice on open-ended sets: STAYS OPEN. Partial: Piriyakulkij 2024 (d08) shows scaffold-only EIG over an LLM-generated candidate list beats vanilla and ReAct prompting, but with no equal-token control. Dutta 2026 (d01) shows plain LLM question choice stays above the DP optimum even on enumerated tables. QuestBench (d07) shows LLM question choice is weak on logic and planning while search is near perfect.
2. Noisy likelihood loss and best estimator: STAYS OPEN. STaR-GATE (d09) uses gold-response log-probability as an information signal and warns that unregularised optimisation degrades results. No new estimator comparison found.
3. Pragmatic term in LLM tasks: PARTLY ANSWERED, weight still open. Dutta prompt autocompletion (d02): goal-linked weights plus a stop threshold took compliance from 0.0417 to 0.375 (48 tasks, simulated answers). PUMA (d06) fixed weights at 0.4 / 0.6 and did no sweep. No sweet spot located.
4. Conditioning the next move on the test result in non-game tasks: STAYS OPEN. No new evidence.
5. Lookahead vs one-step: STAYS OPEN. Dutta Prop 3.3 and Appendix B (d04) state greedy EIG is not globally optimal; no LLM measurement of 2-3 step lookahead.
6. Transfer to math/code: PARTLY ANSWERED. QuestBench (d07): under 50% on Logic-Q and Planning-Q, over 80% on math word problems, CoT no consistent help, BFS 99.8% at depth 10. Friston-group 2026 simulation (d17): EIG over candidate rules cut discovery time 28.5 to 19.4 trials. No LLM EIG test with candidate solutions beyond Kobalczyk (earlier file).
7. Human or animal data separating EFE from plain EIG or reward models: ANSWERED NEGATIVELY. Gijsen 2022 (d11), Zhang 2025 (d12) and Cogliati Dezza 2022 (d14) are compatible with an information term, Mathar 2025 (d16) shows a heuristic-bonus RL model fits as well, and Nelson 2010 (d13) found probability gain beat Shannon information gain. No direct EFE vs EIG-plus-reward test exists in what we found.
8. Bogdan replication and stop rule for S7: STAYS OPEN for the replication. A stop rule exists in theory (Dutta Prop 3.3, d04) and trained form (CaRT, d10), but no prompt-only version was measured.
9. EFE applied directly to LLM agents with baselines: PARTLY CLOSED. PUMA (d05) is the first measured case (Qwen3-8B Lift 1.62 vs best baseline 1.07), but it bundles a world model and belief module, so it does not isolate EFE. Dutta 2026 (d01, d03) frames question asking as EFE but its prompt-optimization result is qualitative.

Net changes to claims: K19 and K21 rewritten (K21 now contested); K03, K11, K12 gained evidence; new K22 to K28.
