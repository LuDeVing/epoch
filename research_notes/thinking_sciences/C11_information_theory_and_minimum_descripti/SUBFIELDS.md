# Information theory and minimum description length: subfields

This field treats learning and understanding as compression: the best explanation gives the shortest total code for the model plus the data. It divides into Shannon information theory, Kolmogorov complexity and algorithmic probability, the minimum description length (MDL) principle, Bayesian model selection, and views of prediction as compression. For us it supplies a principled tie-break for S7 (prefer the shorter rule that fits) and a probe-choice rule (information gain). It also carries a warning: simplicity must be paired with held-out checks (G3). Marks: [V] = page opened this session; [M] = from memory or seen only in a search result. Only two sources here were opened.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Shannon information, entropy | Uncertainty and code length | Shannon 1948 [M] | Med | S7 probe choice |
| Kolmogorov complexity | Length of the shortest program; uncomputable, but two programs can be compared by length | Kolmogorov, Chaitin, Solomonoff [V via Wikipedia] | Med | background; shortest-rule selection |
| Statistical MDL | Total length = hypothesis + data given hypothesis | Rissanen 1978; Grunwald and Roos overviews [V] | High | S7 tie-break |
| Minimum message length | Related Bayesian-style code principle | Wallace and Boulton 1968 [V via Wikipedia] | Low | background only |
| MDL and Bayes | Code length matches probability; some MDL codes (normalised maximum likelihood) have no Bayes counterpart | Wikipedia article [V] | Med | selection with priors |
| Model selection links | BIC, Lasso and Ridge penalties | Wikipedia article [V] | Low | background only |
| Algorithmic MDL | Learning program-like models | Wikipedia article [V] | High | S2, S7 |
| MDL program synthesis on ARC | Shortest program on the ARC benchmark | MADIL, arXiv 2505.01081 [V] | High | S2, S7 on ARC tasks |
| Compression at inference time | Learn per puzzle by minimising code length | CompressARC [M] | Med | alternative solver |
| Prediction as compression, critique | LLM training seen as coding; contested | arXiv 2501.06802; Zenil et al. 2025 [M] | Low | background only |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Shannon information, entropy | | not started |
| Kolmogorov complexity | | not started |
| Statistical MDL | | not started |
| Minimum message length | | not started |
| MDL and Bayes | | not started |
| Model selection links | | not started |
| Algorithmic MDL | | not started |
| MDL program synthesis on ARC | [`subfields/08_mdl_program_synthesis_on_arc/DEEP.md`](subfields/08_mdl_program_synthesis_on_arc/DEEP.md) | done, batch 5 (2026-10-27) |
| Compression at inference time | | not started |
| Prediction as compression, critique | | not started |

## Dig into next

1. **MDL as the S7 tie-break.** How is "length" defined for a rule in words or code, and does the shortest candidate that passes held-out checks beat the vote? Our data: 34 of 36 for the selector against 33 of 36 for the vote, a small margin. Evidence: more items with several length measures (tokens, tree nodes, number of primitives).
2. **MDL program synthesis on ARC (MADIL).** What description language did it use, and could its primitives be the vocabulary for our subgoal library? Evidence: the paper's ablations and failures (full text not yet read), overlap with our wrong-but-fitting programs.
3. **Information gain as a probe rule.** Is the input that best splits the surviving rules' outputs the best test? Evidence: split rate, see C09.

## Combined with LLMs

- MADIL (arXiv 2505.01081): MDL applied to inductive learning with pattern-based decomposition, on ARC. The only number on the abstract page: about 7 percent at ArcPrize 2024, which the authors say is below LLM-based methods, with better efficiency and interpretability. No LLM is part of the method [V].
- The Wikipedia MDL article says algorithmic MDL is studied as part of work on general intelligence [V]. It reports no LLM results.
- CompressARC (20 percent on ARC-AGI-1 evaluation puzzles), Zenil et al. on compression and LLMs, and the agent-as-compressor paper were seen only in search results [M], so their numbers are not quoted here. No opened source shows MDL selection added to an LLM loop beating voting at equal cost.

## Sources

1. https://arxiv.org/abs/2505.01081 [V] MADIL
2. https://en.wikipedia.org/wiki/Minimum_description_length [V] MDL
3. https://export.arxiv.org/pdf/2501.06802 [M] LLMs and Kolmogorov complexity
4. https://arxiv.org/pdf/2606.25960 [M] agentic system as compressor
5. Rissanen 1978; Grunwald, The MDL Principle (2007); Li and Vitanyi [M] (no URL)
