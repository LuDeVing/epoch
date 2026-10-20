# Heuristic search and planning: subfields

This field studies how to find a path or plan in a large space with limited effort. It divides into uninformed and informed search (A*), local search, sampling search (MCTS), automated planning (STRIPS, PDDL, hierarchical task networks), constraint satisfaction and bounded or anytime search. It supplies the vocabulary for the idea tree at S6: how to expand, rank, prune and spend a known budget. Marks: [V] = page opened this session; [M] = from memory or seen only in a search result.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Heuristic search (A*, best-first) | A heuristic ranks branches; admissible heuristics never overestimate | Newell and Simon; Pearl, Heuristics 1984 [V via Wikipedia] | High | control: rank children at S6 |
| Heuristic design by relaxation | Solve an easier problem to get an estimate | Pearl; Helmert, Hoffmann [M] | High | O4 drop a constraint |
| Monte Carlo tree search | Select, expand, simulate, back up; UCT balances explore and exploit | Kocsis and Szepesvari; Coulom [V] | Med | control; value of exploration |
| MCTS limits | Can miss trap states; many parameters | Wikipedia [V] | Med | caution |
| Tree of Thoughts | LLM proposes thoughts, scores, search with lookahead and backtracking | Yao et al. 2023, arXiv 2305.10601 [V] | Med | idea tree at S6 |
| Language Agent Tree Search | MCTS with LM value function, reflection, environment feedback | LATS, arXiv 2310.04406 [V] | Med | S6 with real feedback |
| Automated planning (STRIPS, PDDL) | Actions with preconditions and effects | Fikes and Nilsson; Ghallab et al. [M] | Med | O5 work backwards |
| Hierarchical task networks | Decomposing tasks by known methods | Erol, Hendler, Nau [M] | High | O3 decompose, method library |
| Means-ends analysis | Reduce the difference between state and goal | Newell and Simon [M] | High | O5, subgoal choice |
| Constraint satisfaction | Variables, domains, propagation | Dechter; Mackworth [M] | Med | O4, S4 |
| Anytime search, restarts | Best answer at any stop; escape bad early choices | Zilberstein; Gomes and Selman [M] | High | G6, S6 trigger |

## Dig into next

1. **Search with restarts under known cost.** When do independent restarts beat going deeper on one branch? What schedule suits an LLM call budget? Evidence: our attempt logs; Gomes and Selman heavy-tail results (not yet opened).
2. **Heuristic design by relaxation.** Which operators give a relaxed subgoal whose result ranks the real children? Evidence: whether the relaxed result predicts the child's test result in our runs.
3. **HTN-style method libraries.** Can solved decompositions be stored as methods with preconditions and tried first? Evidence: reuse rate and gain on the second problem of a class.

## Combined with LLMs

- Tree of Thoughts (arXiv 2305.10601): tasks Game of 24, Creative Writing, Mini Crosswords. On Game of 24, GPT-4 with chain of thought solved 4 percent; ToT solved 74 percent [V, abstract page].
- LATS (arXiv 2310.04406): MCTS with LM agents, LM value functions and self-reflection; tasks programming, interactive QA, web navigation, math. HumanEval with GPT-4: 92.7 percent pass@1. WebShop with GPT-3.5: average score 75.9. No numbers for QA or math on the page [V].
- A Stanford course project (seen only in search results [M]) reportedly found the value function mattered more than the search method and that chain of thought matched MCTS at one seventh of the time; small project, not opened, so not relied on.
- These are search-heavy results on tasks with checkable outcomes. They do not test equal-token comparison against voting, which G12 and G7 require.

## Sources

1. https://arxiv.org/abs/2305.10601 [V] Tree of Thoughts
2. https://arxiv.org/abs/2310.04406 [V] LATS
3. https://en.wikipedia.org/wiki/Monte_Carlo_tree_search [V] MCTS
4. https://en.wikipedia.org/wiki/Heuristic_(computer_science) [V] heuristics
5. https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/KamyarJohnSalahiPranavGurusankarSathyaEdamadaka.pdf [M] course project
6. https://docs.ag2.ai/latest/docs/blog/2024/12/20/Reasoning-Update/ [M] AG2 documentation
7. Russell and Norvig; Gomes, Selman and Crato on heavy tails [M] (no URL)
