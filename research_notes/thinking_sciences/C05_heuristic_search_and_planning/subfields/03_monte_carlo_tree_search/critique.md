# Critique: Monte Carlo tree search (C05.03)

Cross-check of evidence_a/b/c.jsonl (93 lines). Sources re-opened this session as PDF text: rStar (2408.06195), LATS (2310.04406), RAP (2305.14992), Wu et al. inference scaling (2408.00724), Koh et al. tree search for agents (2407.01476), Coulom 2006, Chaslot 2008.

## Corrections made

1. rStar baselines (a25 vs c13). a25 and the rStar abstract say Mistral-7B goes "36.46% to 81.88%". The paper's own table shows 36.46 is SC@maj8; few-shot CoT is 17.89 (c13 is right). LLaMA2-7B 12.51 to 63.91 and LLaMA3-8B-Instruct 74.53 to 91.13 confirmed. Use 17.89 as the CoT baseline; the abstract mixes baselines. SC@maj128 in the same table (23.05 / 52.84 / 67.55 / 84.69 / 88.68) is the fair rival.
2. LATS ToT value (a21 vs c11). Both are in the paper but in different tables: ToT 0.55 (reasoning-only, Table 2), ToT(ReAct) 0.39 (Table 2) and 0.49 (k=50 cost table). c11 mixed these. Confirmed LATS k=50 appears as 0.63 (Table 9) and 0.61 (Table 10): a genuine internal inconsistency (claim K13).
3. RAP full Blocksworld (a20 vs c08). Confirmed from Table 4: Easy CoT 0.49/0.18/0.06/0.01/0.01/0.00, all 0.08; RAP(10) 1.00/0.99/0.75/0.61/0.32/(12-step garbled), all 0.65. Hard CoT all 0.05, RAP(10) all 0.51; Hard RAP(10) by steps 0.67/0.76/0.74/0.48/0.17. a20 "Easy CoT 0.08" is the all-steps value; c08's per-step CoT values are right.
4. Evidence a07 (Coulom) says "not opened"; b05/b06 opened it. Coulom Table 1 re-confirmed (128 sims: mean 6.44, max 41.70, robust max 39.60, mix 5.29; 131,072 sims: 2.84, 1.83, 1.88, 2.05). a07 should be read as superseded by b05/b06.
5. Chaslot 2008 (a08/a09) re-confirmed: 9x9 none 33.2% (1000 games), PU 58.3% (1000), PB+PU 61.7% (2000); 19x19 level 0 PB+PU 48.2% (500). Column alignment for PB only (37.2) and 13x13 was not re-checked.
6. Wu et al. (b24/c18): "dozens of times more generated tokens" for MCTS confirmed. The exact quote that MCTS "underperforms ... at each compute budget" and the 7x REBASE saving come from the paper's text and Table 1 (found, table text binary-mangled; 7x not recomputed).
7. Koh et al.: VWA 18.9 to 26.4 (+39.7%), WA 15.0 to 19.2 (+28.0%), depth/breadth rows 1/1 24.5%, and 37.0% at the top budget confirmed.

## Contradictions between sources

- Is MCTS good for LLM reasoning? RAP, LATS, rStar, rStar-Math report large gains; Wu et al., Snell et al. and Feng et al. find MCTS or lookahead no better than or worse than sampling and beam search at matched compute. Gains are mostly measured against single-chain CoT, not against equal-token best-of-N with a checker.
- RAP GSM8K: a19 says RAP single trace 48.8, b15 says RAP(1) 48.6 and RAP(10) 51.6. Possibly different columns; not resolved.
- AlphaMath: a27 reports SBS B1=3 at 66.3 on MATH, c22 gives 66.30 (matches); a27 GSM8K 84.1 not verified.
- Feng et al. say CoT-SC beats tree search on GSM8K at equal tokens, yet RAP reports a 2-point edge over SC(10) with unequal compute.
- rStar says RAP saturates after 4 rollouts; RAP's own paper shows RAP(20) > RAP(10) on Blocksworld. Different models and tasks.

## Weak spots

- Most LLM-MCTS results compare tree search at 10-50 iterations to 1 chain. Few are token-matched (Wu, Snell, Feng, partly LATS and ReST-MCTS*).
- Small test sets: 200 questions in rStar ablations (plus or minus 3 points), 15 AIME problems (53.3% is 8 of 15), 100 games in AlphaZero matches.
- Many headline gains need training (rStar-Math, AlphaMath, ReST-MCTS*, MCTS-DPO) and do not transfer to a scaffold-only agent.
- Value from the model's own opinion (RAP, MCTSr, Marco-o1 confidence) is the weak link; evidence that it fails is indirect (LATS ablation, Feng prompted vs learned value).
- Theory (UCT consistency, regret) says nothing at budgets of 10-50 rollouts.

## Seen only in snippets or not opened

- a10 Gelly and Silver (RAVE), a11 Browne survey, a12 Coquelin and Munos (hyper-exponential worst case), a13 AlphaGo: not opened.
- Marco-o1 (c30), Tian et al. imagination search (c23), MCTSr (c16), Zhao et al. LLM-MCTS (c28), SWE-Search (c26), PG-TD (c27): numbers recorded by other agents, not re-opened by me.
- DeepSeek-R1 failed-MCTS statement (b31) and AlphaZero numbers (a14, b07, c03): consistent between two agents, not re-opened by me.
- Failed replications of MCTS for LLMs as such are rare; the negative evidence is compute-matched comparisons, not replication attempts.

## GAPS

1. At equal total tokens, does MCTS with UCT beat best-of-N plus a code or checker verifier on a hard reasoning set when the agent is a frontier model (2025-2026), not 7B? Evidence so far is on small models and MATH.
2. What exploration constant and rollout budget work for LLM trees (UCT c value, progressive widening)? No source gives a sensitivity sweep for LLM MCTS.
3. Is there a difficulty gate (easy vs hard questions) that predicts when search helps, so the scaffold can skip it on easy items (Snell: it hurts there)?
4. Can a non-learned value (executable test, constraint check, independent second-model check) replace a trained process reward model, and how much of the rStar-Math / ReST-MCTS* gain survives?
5. Do 2025-2026 reasoning models (o1/R1 style, long chain of thought) still gain from external MCTS, or does internal search make it redundant? Only DeepSeek's negative note was found.
6. How does REBASE-style balanced expansion or step-level beam search compare with MCTS at equal tokens outside MATH (planning, coding, agents)?
7. What is the token overhead of MCTS bookkeeping (state descriptions, reflections) vs gain on agent tasks (LATS, SWE-Search, Koh)? Costs are reported inconsistently.
8. Does UCT's deceptive-tree worst case (Coquelin and Munos) show up in LLM reasoning trees, and do restarts or budget caps fix it?
9. Does storing MCTS-found verified traces in memory (without training) match the gains seen from MCTS-based fine-tuning?


## Gap search results

Evidence in evidence_d.jsonl (d01-d18). Search APIs (arXiv query, Semantic Scholar, OpenAlex) were rate limited and WebSearch budget was used up, so sources were papers fetched by arXiv id, read as PDF text. New claims K24-K31 added; K02, K09, K10 upgraded or extended; K16, K17, K19 annotated.

1. Frontier model, equal tokens, MCTS vs best-of-N plus checker: PARTLY CLOSED. Best evidence is AB-MCTS (d01, d02). With GPT-4o and DeepSeek-V3 at 27 calls, fixed-width MCTS is about equal to repeated sampling on code and worse on ARC-AGI (9.0 vs 15.0). With reasoning models on ARC-AGI-2 (o4-mini 23% to 27.5% coverage, 120 tasks), adaptive tree search wins by about 4.5 points. No test with UCT proper on a frontier reasoning model at equal tokens. Still open for a scaffold that uses UCT.
2. Exploration constant and budget: CLOSED AS "NO SWEEP EXISTS". LATS (w=0.5 worse, 1 and 2 equal), TS-LLM (two values tried), SWE-Search (c=1.41), AB-MCTS (UCT unusable, width sweep 3/5/10: 0.429/0.432/0.402). Width and rollouts matter more than c. Practical range 16-64 rollouts (rStar-Math saturates at 64). A sweep for our agent has to be run (agent_test in K26).
3. Difficulty gate: PARTLY CLOSED. Snell (d04), Liu (d05), Chen (d07) agree that search helps middle difficulty, hurts or wastes on easy, and gives little on hardest. Liu shows the gate depends on model size (72B: best-of-N at all levels). Cost of estimating difficulty was not charged anywhere. Open: a cheap gate tested end to end.
4. Non-learned value instead of trained PRM: PARTLY OPEN. rStar-Math round 1 (answer match plus code execution, no learned reward) gave MATH 58.8 to 75.2 versus 89.4 at round 4 (d12), but this includes fine-tuning. AB-MCTS uses demonstration-case execution as score (d02). rStar uses a second-model consistency check (d16). No paper swaps a checker for a PRM at inference with everything else fixed. Open.
5. Reasoning models and external MCTS: PARTLY OPEN. DeepSeek (d06) says MCTS can help inference only with a pre-trained value model and gave it up for training; no numbers. Chen (d07) shows internal search is wasteful on easy items. s1 (d17) shows REBASE on top of a reasoning model still helps on AIME24 but its reward-model cost is not counted. AB-MCTS d02 is the only external-search gain on reasoning models. Open: controlled, token-matched test.
6. REBASE or step beam vs MCTS outside MATH: STILL OPEN. d18 is a synthesis; nothing found that compares them on planning, code or agents at equal tokens. TS-LLM (d09) shows tree search winning on deep problems (Game24, chess) and losing to CoT-SC on GSM8K.
7. Token overhead: PARTLY CLOSED. SWE-Search about 5x cost (14x for GPT-4o) for 23% relative gain (d14, table alignment inferred from garbled text). LATS reports tokens only upon success (d10). No uniform accounting exists.
8. Coquelin-Munos deceptive tree: THEORY CLOSED, EMPIRICS OPEN. d08 opened: exp(exp(D)) rounds on the constructed tree, remedies (modified UCT, flat UCB, BAST). No LLM reasoning-tree study checks it; AB-MCTS drops UCT for related reasons.
9. Memory of MCTS traces without training: STILL OPEN. Only indirect evidence: ReST-MCTS* training gain is marginal (LLaMA-3-8B 29.02 vs few-shot 28.99, d13).

Corrections from this pass: the earlier note that Coquelin-Munos is "hyper-exponential" is exp(exp(D)) for square-root bonus and D-1 nested exponentials for the log bonus. arXiv id 0708.2380 is a different paper (Wishart distributions); the correct id is cs/0703062. LATS Table 11 row order is ambiguous in extracted text; only w=0.5 (0.55) and the text statement on w=2.0 are safe to cite.
