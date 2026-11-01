# C12.08 Bandit allocation: cross-check critique

## Numbers re-opened from source text (this session)
Confirmed against the paper text: Large Language Monkeys (15.9% to 56% at 250; Gemma-2B 0.02% to 7.1%; MATH 82.9% to 98.44%, vote 40.50% to 41.41%); EVOLvE Table (RH 7.6/10.5/27.7/45.5, CB 0.0/7.1; AG 4.9/4.1/32.2/59.6, CB 46.4/64.3; UCB 90.6; LinUCB 96.4; 65.6 and 50.2); Krishnamurthy (72 GPT-4 and 48 GPT-3.5 configs, 32 Llama2 configs, BSSC0 only success, SuffFailFreq(T/2) TS 0.01, UCB 0.02, Greedy 0.48, basic 0.50); Binz and Schulz (2.72 vs 3.24, t(38878) = -5.03); Garivier-Kaufmann table (3968, 4052, 4516, 8437, 9590; 1370, 1406, 3078, 2716, 3334); Pan et al. (o1 177, humans 42, 29,493 players, 4,691,033 trials); Zuo and Zhu (11.10, 10.82, 11.23 points, all "up to"); Snell (about 4x, 14x, level 5 no progress); LATS (92.7, 83.8).

## Corrections
1. b19 says Llama-3-8B MATH coverage is 82.9% "at 1 sample". The paper says 82.9% at 100 samples (to 98.44% at 10,000). a22 and c17 are right; b19 is wrong.
2. a14 says "32 prompt designs for GPT-4"; the paper has 32 designs but 72 GPT-4 configurations in total (b02, c01 right). Treat 32 as the design grid, 72 as the count.
3. Zuo and Zhu gains are best-case ("up to") on a chosen budget, not averages. b22 numbers must be read that way.
4. a16/b03 report Pro raw-history contextual win rate as 7.1 (c06 agrees); a16 lists only Flash 0.0. No conflict, only a gap.
5. a19/b11 horizon-task t-test has df 38878; c10 has a different df (29134) for a different study (gambles). Not a conflict.
6. a14 "basic prompt suffix failure over 60%" (T=500) and the table value 0.50 (T/2, T=100) are different measures. Do not mix them.

## Contradictions and tensions
- Summarised history: Krishnamurthy and EVOLvE agree it helps in stochastic bandits. Park et al. find it matters in online learning but warn the settings differ. Status: contested for adversarial settings.
- Few-shot vs fine-tuning: they react in opposite ways to history format (50.2 vs 27.5 few-shot, 65.6 vs 28.3 fine-tuning). Small sample of tasks.
- Cumulative regret (UCB, Thompson) vs simple regret (Bubeck): which one an LLM agent should optimise depends on whether intermediate samples earn anything. In a reasoning scaffold they do not (only the final answer counts), which favours halving or best-arm methods over UCB.

## Weak spots
- Nearly all LLM bandit results use 2023-2024 models (GPT-3, GPT-3.5, GPT-4, Gemini 1.5, Gemma 2). Almost none test current reasoning models; Pan et al. is the one exception and shows a large gap. Conclusions "LLMs do not explore" may be stale.
- Many claims rest on one paper (Krishnamurthy, EVOLvE). Independence is low. EVOLvE win rates are pairwise and depend on the comparison set.
- Replicate counts are small (N=10 to 40). No confidence intervals reported in several tables.
- The test-time-compute papers are about allocating over queries, not within one chain of thought. Mapping to one agent's internal options (hypotheses, plans) is an inference, not measured.
- No source tested a Gittins-index scaffold on an LLM. Gittins itself is carried by secondary sources.

## Only seen in snippets or not read
- Gittins 1979, Lai-Robbins 1985, Robbins 1952, Thompson 1933, Weber 1992 not read; facts from Auer 2002, Russo 2018, Wikipedia (a26, c25).
- Wilson et al. 2014 horizon task original (c26) described via Binz and Schulz and Gershman only.
- Phelps 2025 sample sizes missing (b27). Lee 2023 and Laskin 2022 (c22, c23) have no figures. Schubert 2024 (c12) no effect sizes.
- Other evidence lines were marked opened by the finders; I re-checked only the numbers listed above.

## GAPS
1. Do current reasoning models (o-series, R1, Claude, Gemini 2.5+) still show suffix failure on the Krishnamurthy hard bandit with raw history, and at what thinking budget does it disappear?
2. At equal total tokens, does successive halving over candidate solutions or plans beat uniform best-of-N and difficulty-routed allocation when a verifier is weak or absent?
3. Does early partial reasoning predict final correctness well enough for pruning (rank correlation after k tokens)? Where is the Hyperband-style failure (SVHN case)?
4. Is there any measured LLM use of a Gittins or Whittle index (not UCB), for example for tasks with switching costs or discounted token budgets?
5. How well can an LLM estimate its own per-option success probability (calibration), since all adaptive allocation methods (Damani, Zuo and Zhu) depend on it? What happens when estimates are overconfident?
6. Does a prompt-only forced-exploration rule (try every option once, untried-option bonus) raise coverage without hurting accuracy, as the fine-tuned +1 bonus did (50% to 70%)?
7. How do bandit allocators behave when arms are non-stationary or adversarial (a plan that works then breaks)? Park et al. show GPT-4 failing; is there a scaffold fix?
8. What is the cost of the bookkeeping (tool-computed per-arm stats) in tokens versus its gain, and does a self-written tally work as well as an external one?
9. For agents with a stopping decision, what do optimal-stopping and bandit stop rules (Adaptive-Consistency, early-stopping SC) lose on hard problems with low base accuracy (MATH level 5)?
10. Do few-shot demonstrations of allocation hurt strong models (EVOLvE Pro) in other tasks, and is the cause demo difficulty or format?

## Gap search results (evidence_d.jsonl, d01 to d20; claims K24 to K35 added)
Method note: the general web search quota was used up, and the arXiv API, Semantic Scholar and OpenAlex returned rate-limit errors. Work used arXiv's own search pages and direct PDF reads. Every d-line was read from the paper text (opened:true). PDFs were deleted after extraction.

1. Suffix failure in reasoning models: STAYED OPEN. No paper re-runs the Krishnamurthy hard bandit with o-series, R1, Claude or Gemini 2.5. Nearby data: more thinking raises directed exploration (o3-mini high, Gemini-2.5-flash budget; d01), GPT-5-mini solves the exploit step from raw history (d02), and scaffolded Thompson sampling beats R1 (d03). The budget at which SuffFailFreq reaches zero is unmeasured. Claim K24.
2. Successive halving vs best-of-N with weak verifier: STAYED OPEN. Closest are ST-BoN (no verifier, hidden states, 70-80% cost saving; d09) and REx (verifier needed; d19). Claim K33.
3. Early prediction and pruning: PARTLY CLOSED. White-box probes give about 65% accuracy at 10% of a chunk and 79% peak (d08); Certaindex and ST-BoN show usable signals (d09, d11); Hyperband SVHN and DeepConf's overconfidence loss show where cutting fails (d18, d10). No black-box rank correlation after k tokens found. Claims K29, K30.
4. Gittins or Whittle index in an LLM: CLOSED AS NEGATIVE (arXiv only). Zero hits (d20). Claim K31.
5. Self-estimated success probability: MOSTLY CLOSED. Overconfidence documented (d13), better in reasoning models (d14), learned P(IK) works (d15), overestimates of hopeless options attract budget (d16). Not tested: per-plan success priors before any attempt. Claim K28 (established).
6. Prompt-only forced exploration: PARTLY CLOSED. Try-all and random context both help (d04, d05) but neither is a clean prompt-only test on a frontier model. Claim K27.
7. Non-stationary or adversarial arms: PARTLY CLOSED. Failure shapes are narrower than "GPT-4 fails" (d06); thinking helps but not to human level (d01); forgetting is the bandit-side fix (d07). No scaffold-only LLM fix measured. Claim K32.
8. Bookkeeping cost: PARTLY CLOSED. Token numbers for full-history prompts and written Beta tallies exist (d02, d03); no head-to-head of self-written vs tool tally. Claim K35.
9. Stop rules on hard problems: CLOSED for the main point. Savings shrink on hard sets (MATH 33.8% vs GSM8K 80.1%; d17), and confidence cutting can lose when wrong traces are confident (d10). Claim K34.
10. Few-shot allocation demos hurting strong models: STAYED OPEN. Only the EVOLvE result (b04, c07, a17) and the DeepSeek-R1 report's remark that few-shot prompting degrades R1 are known; the cause (demo difficulty vs format) is not separated. No new d-line.

Status changes: K10 gained two sources (still single-source); K19 now four sources; K28 and K29 are new "established" claims; no claim was refuted. Existing evidence line corrections from the cross-check (b19, a14) were not touched here.
