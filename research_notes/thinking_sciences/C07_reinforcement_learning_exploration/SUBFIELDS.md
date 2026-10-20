# Reinforcement learning, exploration: subfields

Exploration is the part of reinforcement learning that asks how an agent should gather information when it does not know what pays off. It divides into bandits and regret bounds, count and optimism methods, intrinsic motivation (curiosity, prediction error, empowerment), goal-conditioned and open-ended exploration, and Bayesian or information-gain exploration. For us it informs how the agent picks among untried directions at an impasse and in open mode, and when exploring is worth its cost. Marks: [V] = page opened this session; [M] = from memory or seen only in a search result.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Multi-armed bandits | Explore versus exploit; UCB1 | Auer, Cesa-Bianchi, Fischer (named in MCTS page) [V as name]; Lai and Robbins [M] | High | selection: which operator next |
| Thompson sampling | Sample a belief, act on it | Thompson 1933; Russo et al. [M] | High | operator choice with class record |
| Count-based exploration, unified with intrinsic motivation | Bonus for rarely visited states | Bellemare et al. 2016 [V via Wikipedia] | Med | S3 history of directions tried |
| Knowledge-based intrinsic motivation | Reward prediction error, learning progress | Oudeyer and Kaplan 2009; Kaplan and Oudeyer 2004; Schmidhuber 2010 [V via Wikipedia] | Low | background (needs a world model) |
| Information-theoretic motivation | Empowerment, predictive information, active inference | Wikipedia article [V] | High | S7 probe choice |
| Competence-based motivation | Flow, autotelic principle | Steels [V via Wikipedia] | Low | background only |
| Novelty search, open-endedness | Reward difference | Lehman and Stanley; Tao et al. 2020 [V as name] | Med | open mode (see C04) |
| Go-Explore, archives | Return to promising states, then explore | Ecoffet et al. [M] | High | S6 subgoals; keep best partial |
| Language-guided exploration | LLM suggests plausible useful behaviours | iLLM, Bougie and Watanabe [V] | Med | S3 priors |
| Curiosity in RL training of LLMs | Exploration bonus in RLVR | CDE, arXiv 2509.09675 [V] | Low | background only (training) |

## Dig into next

1. **Bandit selection of operators.** With 8 operators and few trials per class, does UCB or Thompson sampling over operator success beat a fixed order? How should a prior come from other classes? Evidence: operator success logs; a simulation of regret at our sample sizes.
2. **Go-Explore archive.** Can we store promising partial states and return to them rather than restart? Evidence: Go-Explore paper (not opened); our test of "return to best partial" against "restart".
3. **Information-gain tests.** Which input best splits two surviving rules (S7)? Evidence: how often the chosen input separates the rules compared with a random input.

## Combined with LLMs

- CDE (arXiv 2509.09675): an exploration bonus for RL with verifiable rewards, with an actor term (perplexity over its own response) and a critic term (variance of value estimates from a multi-head critic). Benchmarks: AIME. Result: "approximate +3 point improvement" over standard RLVR with GRPO or PPO. The page names no base models and gives no absolute scores. It also reports a "calibration collapse" in RLVR [V].
- iLLM (Bougie and Watanabe): an LLM suggests plausible behaviours and compresses history; environments BabyAI-Text, MiniHack, Atari, Crafter. Claims higher sample efficiency than prior curiosity methods; no numbers, no LLM named on the page [V].
- Both are training-time methods and do not transfer to a fixed-weight agent. The claim that "LLM agents sample rather than explore" came from a search-result summary only [M].

## Sources

1. https://arxiv.org/abs/2509.09675 [V] CDE
2. https://proceedings.mlr.press/v260/bougie25a.html [V] Language-driven exploration (iLLM)
3. https://en.wikipedia.org/wiki/Intrinsic_motivation_(artificial_intelligence) [V] intrinsic motivation
4. https://en.wikipedia.org/wiki/Monte_Carlo_tree_search [V] used for UCB and UCT
5. https://neurips.cc/virtual/2026/poster/140072 [M] Sampling Is Not Curiosity
6. Sutton and Barto, Reinforcement Learning; Ecoffet et al. 2021 Go-Explore [M] (no URL)
