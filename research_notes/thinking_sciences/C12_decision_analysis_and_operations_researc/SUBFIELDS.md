# Decision analysis and operations research: subfields

This field studies how to choose well under uncertainty and cost. It divides into utility and decision trees, value of information, optimal stopping, sequential decision problems (MDPs and POMDPs), bandit allocation, search theory, multi-criteria analysis, and metareasoning, which applies value of information to the agent's own computation. It supplies our missing S0 gate and stop rules: when more thinking pays, when to stop, how to spend a budget. Marks: [V] = page opened this session; [M] = from memory or seen only in a search result.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Value of information | Expected value of perfect information (EVPI) = EV with perfect information minus best expected payoff; never negative; bounds all other information | Wikipedia article [V]; Howard 1966 [M] | High | S4, S7: pick tests by value per cost |
| Expected value of sample information | Value of imperfect information | Raiffa and Schlaifer [M]; not defined on the page opened | High | quality of a noisy test |
| Optimal stopping | Choose the time to act to maximise expected reward; secretary problem; Bellman equations, dynamic programming | Wikipedia article [V] | High | G11, S6 stop rule |
| Sequential analysis | Stop a test when evidence suffices | Wald [M]; only linked on the page | High | stop after enough agreement |
| Metareasoning, value of computation | Treat a thought as an action with cost and value | Russell and Wefald 1991 [M]; arXiv 2410.05563 [V] | High | S0 gate, S6 trigger |
| Bounded rationality, anytime | Quality as a function of time | Simon; Zilberstein [M] | High | G6, G12 |
| MDPs and POMDPs | Sequential decisions, belief states | Puterman; Kaelbling et al. [M] | Med | control formalism |
| Bandit allocation | Spending samples across options | Gittins [M] | High | G12 (see C07) |
| Learned termination | Teaching a model when it knows enough | CaRT, arXiv 2510.08517 [V] | Med | S0, S8 |
| Search theory | Where to look when finding costs | Koopman; job and price search (named in Wikipedia) [V] | Low | background only |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Value of information | [`subfields/01_value_of_information/DEEP.md`](subfields/01_value_of_information/DEEP.md) | done, batch 5 (2026-10-27) |
| Expected value of sample information | | not started |
| Optimal stopping | | not started |
| Sequential analysis | | not started |
| Metareasoning, value of computation | | not started |
| Bounded rationality, anytime | | not started |
| MDPs and POMDPs | | not started |
| Bandit allocation | | not started |
| Learned termination | | not started |
| Search theory | | not started |

## Dig into next

1. **Metareasoning and value of computation.** Can S0 pick the mode by comparing expected gain (class pass-rate lift of checked over direct) with token cost? How much class history makes the estimate stable? Evidence: per-class pass-rate-against-tokens tables from our logs; the Russell and Wefald model form (not yet opened).
2. **Optimal stopping for attempts.** After k independent attempts with m agreeing, what is one more attempt worth? Is a fixed rule (stop when two agree and one check passed) near the optimum? Evidence: simulation on logged attempts; fixed, sequential-test and bandit rules at equal tokens.
3. **Value of information for tests.** The EVPI bound says a test is worth at most EVPI, and refusing a test that costs more is right. Evidence: log test results with cost and the rate of wrong-to-right flips per test type.

## Combined with LLMs

- Rational Metareasoning for LLMs (arXiv 2410.05563): a reward based on value of computation, trained with Expert Iteration, teaches the model to use intermediate steps only when needed. Baselines few-shot chain of thought and STaR. Result: 20 to 37 percent fewer tokens across three models (not named on the abstract page) on "diverse datasets", with task performance maintained and no accuracy numbers given [V].
- CaRT (arXiv 2510.08517): fine-tunes on pairs where stopping is right and a minimally changed trajectory where it is not, and has the model explain each decision. Tasks: interactive medical diagnosis and math. The abstract says it improves information-gathering efficiency and task success over other fine-tuning methods; no numbers, no model names [V].
- Both are training-time methods. I did not find a prompt-free, code-run stopping rule tested at equal tokens. The 47 percent token cut and the "more thinking hurts" result came from search summaries only [M].

## Sources

1. https://arxiv.org/abs/2410.05563 [V] Rational Metareasoning for LLMs
2. https://arxiv.org/abs/2510.08517 [V] CaRT
3. https://en.wikipedia.org/wiki/Expected_value_of_perfect_information [V] EVPI
4. https://en.wikipedia.org/wiki/Optimal_stopping [V] optimal stopping
5. https://mlanthology.org/neuripsw/2024/sabbata2024neuripsw-rational [M] workshop version of the metareasoning paper
6. https://www.alphaxiv.org/abs/2604.10739.md [M] When More Thinking Hurts
7. Howard 1966; Russell and Wefald 1991, Do the right thing [M] (no URL)
