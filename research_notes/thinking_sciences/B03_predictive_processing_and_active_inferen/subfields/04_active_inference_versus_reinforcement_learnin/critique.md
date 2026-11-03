# Critique: B03.04 Active inference versus reinforcement learning

Cross-check done 2026-11-03. Sources re-opened this session (PDF text): Sajid 2021 (1909.10863), Tschantz 2020 (2002.12636), Voyager (2305.16291), Binz and Schulz (2206.14576), Krishnamurthy (2403.15371), CDE (2509.09675), PUMA (2605.24647), Millidge 2019 (1907.03876), Champion 2024 (partial).

## Corrections made

1. Sajid Table 1 row labels. Evidence b02 and c01 attach 97.79 to "Q-learning eps decaying" and 80.44 to "belief-based Q-learning" or "variant". The PDF (raw text) says: Q-learning (eps 0.1) 97.79 [97.41, 98.16] deterministic and 66.08 [63.28, 68.88] stochastic; Q-learning (eps 1 decaying to 0) 80.44 [78.96, 81.93] and 65.13 [62.57, 67.68]. Both Q-learning rows are "Belief-Based: N". Evidence a03 and a04 are right; b02 and c01 are wrong on labels (numbers right). The claim text uses the correct labels.
2. Sajid Table 2 (reward shaping) row mapping. The true rows (G, H, F rewards; Q-learning, Bayesian RL, active inference):
   - 0, 0, 0: 0.00 (15.00), 39.94 (9.17), 44.00 (8.67)
   - 0, -100, 0: 0.00, 0.00, 0.00 (all 15.00 moves)
   - 100, -100, 0: 95.56 (3.53), 99.77 (3.02), 99.52 (3.03)
   - 100, 0, -10: 96.00 (3.48), 99.89 (3.00), 99.47 (3.00)
   - 100, -100, -10: 96.47 (3.42), 99.79 (3.01), 99.58 (3.00)
   - 100, 0, 0: 95.32 (3.58), 99.74 (3.00), 99.50 (3.07)
   Errors: b04 says "reward only on goal: Q 96.00, BRL 99.89, AI 99.47" (that is the goal 100, living cost -10 row; goal-only is 95.32, 99.74, 99.50) and "goal 100, hole -100, step -10: Q 95.56" (that is 96.47). c07 says "goal 100, hole 0, living cost -10: Q 95.56 (3.53)" (true: 96.00 (3.48)); its goal-only line is correct. a06 only gives ranges, which hold.
3. a06 says Q-learning is "more sensitive to living costs". The table shows Q-learning varies by only about 1.2 points across rows (95.32 to 96.47), and living cost -10 gives slightly higher scores than none. Treat as weak: Q-learning scores about 4 points below the belief-based agents in every row, and the spread across rows is small. Also the Q-learning column is run on-policy (eps 0.0), unlike Table 1.
4. Sajid Table 1: the null model's stochastic CI upper bound prints as 50.22, equal to the mean (likely a typo in the paper). Not corrected, flagged.
5. Confirmed without change: Table 1 active inference and Bayesian RL numbers; non-stationary swaps at 21, 121, 141, 251, 451; "about 40 episodes" versus one episode; Tschantz (Mountain Car optimal in one trial; Ant Maze 35 episodes, 4 seeds; Half Cheetah 5 seeds, 100 episodes); Voyager table (wooden 6+-2 vs 92+-72; iron 21+-7 vs 135+-103; diamond 1/3); Binz and Schulz (beta -0.15+-0.27, p=.58; regret 2.72 vs 3.24); Krishnamurthy (>60% suffix failures); CDE (20.8 to 23.3, 21.0 to 23.5, 48.2 to 50.6, PPO 46.5); PUMA (1.62 vs 1.07, 75.9% vs 52.0%, 62.4% vs 34.0%, turns 12.2 vs 13.1, CAMI 0.717 vs 0.231); Millidge 2019 (20 trials of 15000 episodes).

## Contradictions between sources

- Sajid 2021 says active inference matches or beats RL. Champion 2024 says deep active inference on dSprites only works when it behaves like a reward maximiser, and 1% information gain drastically cuts reward. Millidge 2019 says the epistemic term did nothing on easy tasks. Fountas 2020 says exploration came with no reward cost. These are different scales (tabular vs deep) and different objectives, so they do not strictly conflict, but the epistemic benefit is only clean in tiny or sparse tasks.
- Tschantz 2020 (FEEF, with an information-gain term) wins on sparse Mountain Car; Millidge 2019 and Champion 2024 find the epistemic term useless or harmful. The difference: Tschantz uses a learned ensemble model and a sparse task where reward-only agents never see reward.
- Millidge 2020 (Whence the EFE) shows EFE is not the free energy of the future; Sajid 2021 treats it as the one objective. Theory and demonstration disagree on whether the exploration term is principled.
- Hafner 2022 argues active inference gives smaller niches in noisy worlds; Sajid 2021b (inverted U) shows noisy-TV-like collapse at 100% volatility. These are consistent.

## Weak spots

- The headline result (99 vs 64 in the stochastic world) is a single simulation on a 3x3 grid with a naive Bayesian RL baseline; the authors say so. No independent replication of the FrozenLake table was found.
- The one-episode recovery after a goal swap is a built-in feature (an explicit context state), not a property of "treating reward as an observation".
- Tschantz figures give no text numbers for Ant Maze coverage or Half Cheetah SAC comparison; SAC is a single fixed reference at 100 episodes, not step-matched.
- Voyager has only 3 runs per method; its curriculum is exploration-driven but is not active inference.
- LLM + active inference papers: Prakki (no baseline), Wen (two position papers, no experiments), PUMA (simulator only, small model, one benchmark family). No study tests reward-as-observation inside an LLM scaffold against a reward-driven baseline at equal tokens.

## Only seen in snippets (not opened)

b20 (Hafner 2022: abstract only), b23 (2608.19202), b25 (APEX forum post), a28 (Cullen 2018 second-hand). Treat as unconfirmed.

## GAPS

1. Does an LLM scaffold that picks its next probe by expected information gain (plus a pragmatic term) beat a plain "try something different" prompt at equal tokens in open mode? No measured study found.
2. Is the Sajid FrozenLake result reproducible against a stronger RL baseline (explicit context or change-point belief)? The authors say a richer RL agent might match it.
3. How much of the epistemic benefit survives in deep or LLM settings, given Champion 2024 and Millidge 2019 found none or harm? What weight on information gain stops hurting accuracy?
4. In reward-free settings, what stops LLM exploration collapsing to a noisy-TV (Sajid inverted U at 100% volatility)? Is there a code-side stop rule?
5. Does an explicit "context switched" hypothesis in a written scaffold give one-step recovery after a mid-task rule change, as the active inference agent showed?
6. Can learned or self-written preferences (success criteria) drift to bad attractors in LLM agents, as the agent learned to prefer the hole? Measure drift with and without a fixed criterion.
7. Which LLM exploration failures (Krishnamurthy suffix failures, Binz no directed exploration) are repaired by code-kept history rather than prompt framing?
8. Does Voyager-style curriculum exploration come from the exploration pressure or from the skill library? Needs an ablation at equal tokens.
9. Do any 2026 LLM papers (2608.19202 and others seen only as snippets) report measured gains for expected-free-energy question-asking, and against which baseline?
10. Does the Wei 2024 regret bound (linear in horizon, quadratic in information gain) give a usable rule for how much exploration to allow by problem difficulty (G12)?


## Gap search results

Gap search done 2026-11-03. Evidence in evidence_d.jsonl (d01-d17). The arXiv, Semantic Scholar and OpenAlex APIs were rate limited all day, so PDFs were fetched directly and 6 web searches were used. Sources opened (PDF text): BED-LLM 2508.21184, Mazzaccara 2406.17453, Dutta 2608.19202, Hou 2509.25438, EVOLvE 2410.06238, Wang 2604.04182, Pan 2402.06627 and 2407.04549, Hashash 2606.22813, Voyager 2305.16291 (ablations).

1. Gap 1 (EIG probe vs plain prompt): CLOSED for a crisp hidden-target game. BED-LLM beats Prompt-Only by about 2x (Animals Mistral-Large 33 to 95). Not token-matched, and not an open-mode scaffold test. New claim K24.
2. Gap 2 (stronger RL baseline for Sajid): STAYS OPEN. No replication found. Hashash 2026 (d12) uses another weak Bayesian RL baseline. K02 and K03 stay single-source.
3. Gap 3 (survival of the epistemic benefit, weight): PARTLY CLOSED. In LLM question asking the benefit is large on crisp tasks and small on vague ones (K25). No tested weight for information gain in an accuracy-versus-exploration trade; Dutta's tuned threshold (K27) is the only number.
4. Gap 4 (noisy-TV stop rule): PARTLY CLOSED. Learning-progress rewards are robust in deep RL (K26); no LLM test. Candidate code rule: stop when answers do not change the hypothesis set.
5. Gap 5 (explicit context-switch hypothesis): STAYS OPEN, with new negative evidence that plain LLMs perseverate 7-27 trials after a reversal versus 2.9 for humans (K28). No scaffold test.
6. Gap 6 (preference drift): PARTLY CLOSED. Two papers show self-judged and proxy objectives drift (K29). No fixed-versus-self-written comparison.
7. Gap 7 (code-kept history vs prompt framing): CLOSED for bandits. EVOLvE: code-computed statistics lift Pro from 45.5 to 59.6 (MAB) and 7.1 to 64.3 (contextual); small models gain nothing. K18 raised to established (2 sources).
8. Gap 8 (Voyager curriculum vs skill library): PARTLY CLOSED. Ablations show both matter (random curriculum -93%, no skill library plateaus), but not at equal tokens.
9. Gap 9 (2608.19202): CLOSED as to content. It is a framework paper with an oracle gap and small simulated gains (0.375 vs 0.0417 compliance); no plain-prompt baseline. The better measured answer is BED-LLM. K22 updated. No other 2026 papers on expected-free-energy question asking were found.
10. Gap 10 (Wei bound as a rule): STAYS OPEN. Not re-opened; no empirical rule exists (K30).

Limits: BED-LLM baselines are not token-matched; all LLM numbers come from single papers; d09 and d17 were not opened.
