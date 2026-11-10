# C07.09 Language-guided exploration: cross-check critique

## Corrections made (sources re-opened this session, full PDF text)
Re-checked against the paper text: ELLM (2302.06692), OMNI (2306.01711), Voyager (2305.16291), Krishnamurthy (2403.15371), Schmied (2504.16078), EVOLvE (2410.06238), Motif (2310.00166), Bougie and Watanabe (PMLR v260).

1. ELLM Table 2 (b02 is wrong). Rewarded goals are 66.5% good, 1.1% context-insensitive, 32.4% common-sense violations, 0% impossible. Line b02 labelled 32.4% as "impossible". a02 and c01 are right. Suggested: 64.9 / 13.6 / 16.4 / 5.0 confirmed. The paper says "bad actions (32.4%)" and "impossible actions can never be achieved".
2. ELLM about 6 vs about 9 achievements, and RND/APT/Novelty under 3: confirmed.
3. OMNI Crafter: 55 tasks LP, 82 OMNI, 0.78 vs 0.52 on interesting tasks, 0.56 vs 0.42 on all tasks, 14 interesting tasks: confirmed. The 0.56 is overall success, not interesting-only. Uniform 0.103 interesting-only confirmed. Note the appendix has other settings (larger boring set: 307 tasks, 0.56 interesting-only for OMNI; LP 302 tasks 0.43), so numbers must be quoted with the setting.
4. Voyager: 63 items in 160 iterations, 3.3x, 93% drop (random curriculum), 73% drop (no self-verification), 5.7x (GPT-4 vs GPT-3.5 code): confirmed. Abstract also gives up to 15.3x faster wooden-tool milestone and 2.3x distance. Only 3 runs.
5. Krishnamurthy: "suffix failure in > 60% of replicates" and "only one configuration" confirmed. Three GPT-4 configs avoided suffix failures, two of them uniform-like: confirmed.
6. Schmied: 87% correct rationales and 58% greedy actions confirmed, but for Gemma2 27B on one task, not for LLMs in general. 40% / 65% / 55% / 25% coverage confirmed.
7. EVOLvE: 50.2 (summary) vs 27.5 (raw) few-shot; fine-tuning 65.6 (raw) vs 28.3 (summary); easy 50.2 vs hard 43.0 few-shot; hard 65.6 vs easy 54.5 fine-tune: confirmed from text. Table cells are garbled, so use the prose values. Flash only for these.
8. Motif: "about 30%" on the oracle task with intrinsic plus extrinsic reward, and the hallucination reward hack: confirmed.
9. iLLM: Crafter "about 7 vs 6" confirmed; PickUpLoc "0.85 after 68M" and "RND/NGU under 0.25 after 100M" confirmed. MiniHack River-Monster 0.38 vs 0.22: the table cells are ambiguous in text (several rows hold 0.38), treat as unconfirmed.
10. Dates: Bougie and Watanabe appears as 2024 in c16/c17 and 2025 in a19; the PMLR volume is 2025. Use 2025.

## Contradictions and duplication
- a, b and c cover the same papers. Evidence lines are not independent; claims count papers, not lines. Many "established" claims rest on two papers from related groups (Clune lab: OMNI, OMNI-EPIC, IGE; Meta/Mila: Motif, ONI).
- a28 and c23 are our own syntheses, not evidence; not used in claims.
- Krishnamurthy a24 says the best config is "GPT-4 with hint, summary, CoT"; c09 says zero-shot CoT; b16 says reinforced CoT. Minor wording difference, same config.
- a09/b07 and a07 report OMNI BabyAI success as tiny (0.0075 vs 0.006). Gains there are relative only.

## Weak spots
- Almost every positive result is in game worlds the LLM knows well (Crafter, Minecraft, BabyAI, NetHack). None tests a reasoning task with an open answer.
- Most results need RL training or an environment reward (ELLM, Motif, OMNI, iLLM, Eureka). Few test pure prompting at equal tokens. Only Voyager and Intelligent Go-Explore are prompt scaffolds, with 3 runs for Voyager.
- No paper reports cost per success. Equal-token comparison, which we need, is absent.
- Voyager baselines were re-implemented by the authors; ReAct/Reflexion at 0/3 may reflect weak implementations.
- Failed replications are almost absent: the only real contrary studies are the bandit papers (LLMs explore badly unscaffolded) and the tiny Quadros study.
- Bougie baseline numbers, Atari tables and the noisy-TV tables were not recovered (garbled text). Pitfall 125 and others come from a21-style lines read from tables; not re-verified.

## Seen only in snippets or not re-opened this session
GLAM (Carta), SayCan, Eureka, Text2Reward, SPRING, OMNI-EPIC, Intelligent Go-Explore, BALROG, ONI (Zheng), Quadros, Binz and Schulz were not re-opened by the cross-checker; their lines come from agents a to c. The figures were not re-verified here.

## GAPS (most decision-relevant first)
1. Does asking the model "what is worth trying here" at S3 beat plain sampling or a novelty tiebreak on a text reasoning task at equal tokens? Nothing here tests that outside games.
2. How often are LLM-proposed probes infeasible or context-blind on non-game tasks (puzzles, maths, code), and does a cheap feasibility check recover the loss? ELLM gives 35% bad in Crafter only.
3. Does an explicit tried/untried tally (summary state) fix the greedy-collapse and knowing-doing gap in a prompt-only agent on frontier models? Krishnamurthy and Schmied used GPT-4, Gemma and Llama; current models are untested.
4. How large is prompt-paraphrase sensitivity of LLM-suggested goals (Motif reward hack from rewording) when the agent asks for probes rather than rewards?
5. Does an archive/frontier list (Intelligent Go-Explore) help an agent without environment resets, and what does it cost in tokens?
6. Does a model-based interestingness filter (OMNI) transfer to tasks where "interesting" is not repetitive vs non-repetitive? OMNI oracle was written by the authors.
7. What are the real baseline numbers and effect sizes in iLLM Atari/MiniHack tables (not recoverable from text)? Needs the arXiv/PMLR tables or code.
8. Does the benefit of LLM priors shrink or invert when the domain is unfamiliar (iLLM authors claim smaller gains; no controlled test)?
9. Are there independent replications of ELLM or OMNI by groups outside the original labs, with different LLMs (open models, 2025-2026 frontier models)?
10. Does LLM-suggested exploration add anything beyond what a reasoning-trained model already does with internal search, i.e. is the S3 prior step redundant for current frontier models?

## Gap search results (evidence_d.jsonl d01-d18, claims K24-K34)
Limits of this pass: the WebSearch budget was already used up after one search, and the arXiv, Semantic Scholar and OpenAlex APIs returned rate-limit errors. Papers were found by one search plus known arXiv ids and read as full PDF text. No citation-graph search (who cites ELLM or OMNI) could be done.

1. Gap 1 (S3 prior vs plain sampling or novelty tie-break at equal tokens on a text task): STILL OPEN. Nearest evidence: Harris and Slivkins (d01) show LLM-proposed candidates beat random and retrieval baselines on text bandit tasks, but not plain repeated sampling. NoveltyBench and Verbalized Sampling (d12, d13) show plain sampling is itself a weak baseline (under 3 distinct answers in 10 samples); a "show earlier answers" loop reaches human-level diversity. So the baseline for a future test should be a regeneration loop, not independent samples (K25).
2. Gap 2 (infeasible probes outside games; does a cheap check recover them): PARTLY CLOSED. Si et al. (d14) show LLM research ideas are only slightly less feasible than expert ones (6.34 vs 6.61, n.s.) but 95% duplicates in 4,000 samples. Self-checking by the same model does not recover errors (Huang et al., d16: GPT-4 GSM8K 95.5 to 89.0), while oracle or external checks do (97.5). So the check must be external (K26). No measured infeasible-probe rate on puzzles, maths or code was found.
3. Gap 3 (tried/untried tally on current frontier models): STILL OPEN for frontier models. IGE ablation (d06) shows removing the per-state action history costs 67 points on Game of 24 with GPT-4 Turbo. GPT-4o with strategy hints and no tally did not improve in Little Alchemy (d04). Harris and Slivkins (d02) used GPT-5.2 but only for exploit tasks.
4. Gap 4 (paraphrase sensitivity when asking for probes): STILL OPEN. Only general evidence (Sclar, d11: up to 76 points on LLaMA-2-13B, median 6.4 for GPT-3.5; IGE generic prompts cost 12-20 points on two text games, d07). No test on exploration prompts.
5. Gap 5 (archive without resets, token cost): STILL OPEN. IGE (d05) assumes simulator restore and reports cost per task (1.04 USD Game of 24 with GPT-4), not tokens per success; the no-reset variant is only mentioned.
6. Gap 6 (OMNI filter beyond repetitive vs non-repetitive): STILL OPEN. IGE archive filtering helps modestly on Game of 24 (100 vs 93) and strongly on long text games (BabyAI 84 vs 48; archive 8x larger without it), but the same lab and an LLM-chosen notion of interesting. No author-independent oracle.
7. Gap 7 (iLLM tables): CLOSED. Tables recovered from the PMLR PDF (d08-d10). Pitfall 125 (iLLM(hop)) vs -6 best baseline confirmed; Montezuma 2,632 vs ChibiT 1,231; Seaquest iLLM 18,851 is below APT 19,989. Noisy-TV and dense-reward tables recorded. One residual doubt: the River-Monster baseline value 0.22 could not be tied to a named method because row labels were lost in extraction. Note the LLM is a 280M Transfo-XL.
8. Gap 8 (priors shrink in unfamiliar domains): STILL OPEN, with indirect support. PlanBench (d15) shows 62.6% to under 5% when names are obfuscated; iLLM Atari gain is large in well-known Montezuma and absent in Seaquest (d08). No controlled test inside an exploration method.
9. Gap 9 (replication outside original labs, open or 2025-2026 models): MOSTLY OPEN. iLLM re-ran ELLM as a baseline (a different lab) and found it weaker than its own method (ELLM 0.66 vs iLLM 0.94 on GoToObj) but this is not a replication of ELLM's claims. Intelligent Go-Explore is from the OMNI lab. No ELLM or OMNI replication with current models was found (search limited).
10. Gap 10 (S3 redundant for reasoning models): PARTLY ANSWERED, against redundancy but weakly. Pan et al. (d03) find o1 (177 elements) and R1 (85) explore far better than GPT-4o (35) and humans (42), so reasoning-trained models need the prior least. Wang et al. (d17) show they still switch thoughts too early (418% more switches on wrong answers). No study tests S3 on/off on a reasoning model. One game, one model family.

Corrections found while reading: none to the numbers already in claims. The ELLM b02 label (32.4% = common-sense violations, impossible 0%) is untouched by this pass.

Decision-relevant summary: three questions (1, 3, 5) are still testable only by running our own small experiments. Cheapest first test: S3 prompt as a regeneration loop with an external check vs a novelty tie-break, on a chat model and a reasoning model, over 10 paraphrases of the prompt, at equal tokens.
