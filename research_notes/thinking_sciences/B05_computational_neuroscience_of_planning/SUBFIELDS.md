# Computational neuroscience of planning: subfields

This field builds mathematical models of how brains plan and tests them on recordings and behaviour. It centres on the hippocampus and prefrontal cortex: maps of space and of abstract structure, replay of paths, and the choice between cached habit and search through a model. Its models are explicit algorithms (successor representation, Dyna-style replay, prioritised replay, options), so it is one of the most transferable brain fields. Cell types and rodent mazes do not transfer.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Cognitive maps | Maps of relational structure, not only space; place and grid fields also code non-spatial states and skew toward goals | Tolman 1948; Momennejad 2020 [V] | Med | S2 represent: a map of states and moves for the task |
| Model-free, model-based and successor representation | MF stores action values; MB simulates; SR stores discounted expected future visits, a cheaper middle way | Dayan 1993; Stachenfeld et al. 2017; Momennejad 2020 [V] | High | Memory: store "where does this lead" structure by class |
| Replay as offline simulation (Dyna family) | Dyna-Q, Dyna-Q+ (exploration bonus), prioritised sweeping, SR-Dyna; SR-Dyna fit human revaluation best | Sutton 1991; Russek et al. 2017; Momennejad 2020 [V] | High | Memory: offline replay to update the subgoal library |
| Prioritised memory access | Replay ordered by utility = gain times need; reverse replay by gain, forward replay by need | Mattar and Daw 2018 [V] | High | Memory: order which stored subgoals to revisit |
| Map versus value replay | Replay builds a goal-general map (geodesic representation), priority weighted by beliefs about future goals | Sagiv, Akam, Witten and Daw 2025 [V] | Med | Memory: keep routes for likely future goals, not only the current one |
| Preplay and replay recordings | Sequences before and after movement | Foster and Wilson 2006; Dragoi and Tonegawa 2011; Pfeiffer and Foster 2013 | Low | Background |
| Planning by tree search with pruning | Depth-limited planning, pruning of branches | Huys et al. 2012 (cited in Doll [V]); Keramati et al. | High | S6 tree rules: depth and pruning set by budget |
| Hierarchical planning, options, subgoal discovery | Temporal abstraction; SR eigenvectors help find subgoals; eigen-options | Botvinick; Momennejad 2020 [V] | High | Subgoal library: discover subgoals as bottlenecks |
| Hippocampal sweeps and vicarious trial and error | Lookahead at choice points | van der Meer 2010 (cited in Doll [V]); Redish | Low | Background; lookahead at hard points only (G1) |
| Pathology of replay | Rumination and craving as dysfunction of prioritised access | Mattar and Daw 2018 [V] | Low | Not relevant |

## Dig into next

**1. Prioritised access for the subgoal library.**
- Can "gain" (how much using this stored rule would change the action) and "need" (how likely this situation is soon) be estimated for stored subgoals?
- The authors admit computing gain requires knowing the update's effect beforehand. What proxy is cheap?
- Evidence needed: Mattar and Daw model [V], retrieval logs.

**2. SR and bottleneck-based subgoal discovery.**
- Can bottleneck states (the shared steps of many solutions) be found from logged solution graphs and stored as subgoals?
- Evidence needed: Momennejad 2020 [V] on eigen-options, Sagiv 2025 on shared-route replay [V], our logs.

**3. Dyna-style offline updating.**
- Does replaying stored problems with the current rules (a model) improve the class record without new calls?
- Evidence needed: Dyna and SR-Dyna papers, our offline replay test.

## Does not transfer

Place cells, grid cells, theta, ripples and physical-space replay are biology. The Sagiv paper notes the map-versus-value debate is unresolved and that replay patterns lag behind goals because of slow learning. Mattar and Daw used simple, deterministic simulations. Rodent navigation is far from language reasoning. Keep the algorithms, drop the cell types.

## Sources

[V] means the page was actually opened (fetched and read) this session. [M] means seen only in search results or from memory.

1. [V] Momennejad 2020, Learning structures: predictive representations, replay and generalization https://pmc.ncbi.nlm.nih.gov/articles/PMC9004662
2. [V] Sagiv, Akam, Witten and Daw 2025, Neuron https://pmc.ncbi.nlm.nih.gov/articles/PMC12633763/
3. [V] Mattar and Daw 2018, prioritized memory access https://pmc.ncbi.nlm.nih.gov/articles/PMC6203620
4. [V] Doll, Simon and Daw 2012 (for Huys, van der Meer citations) https://pmc.ncbi.nlm.nih.gov/articles/PMC3513648
5. [M] Stachenfeld, Botvinick and Gershman 2017; Foster and Wilson 2006; Redish (no URL)
