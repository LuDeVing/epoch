# Heuristic programming and machine discovery: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D01.06-U1 | Does a short signal-to-operator table beat free reasoning for a modern LLM? | Table of data signals to operators, fired in S2/S6 | O library, S2 | K01 [E] for 1980s programs only; K34 nearest (Self-Discover, no signal trigger); no direct test | Free vs table vs random-module table; fresh disguised law tasks (NewtonBench-style), noise 0 and 0.0001; exact-form accuracy | Table beats free by 3 points or more and beats random-module control by 2 points or more | High |
| D01.06-U2 | Does an explain-the-anomaly subgoal beat re-sampling after a failed prediction? | Surprise trigger in S6 | S6 | K05 single-source, abstract only (d17) | Re-sample vs forced explain subgoal; tasks with planted rule change; fraction revised correctly | 8 points or more gain, no more than 20% extra tokens | High |
| D01.06-U3 | Does forced revision on exact failing cases fix on-line revision? | Revise-on-counterexample step after contradiction | S5/S6, memory | K31 single-source (WorldCoder, belief task); K25 open problem | Free vs counterexample-forced vs self-critique; mid-run contradicting point; revision rate | Forced beats self-critique by 10 points or more | High |
| D01.06-U4 | Is the hypothesis layer worth its tokens only on retry? | Hypothesis-first gated on failed first attempt | S3 | K22, K27 single-source; GPT-4, older model; SyGuS shows no gain | Direct vs programs vs always-hypothesis vs gated; fresh ARC-like items; accuracy and tokens | Gated matches always-on within 2 points at 30% fewer tokens | Med |
| D01.06-U5 | Do cheap-first ladders beat random operator order in an LLM agent? | Operators ordered by token cost at S6 | S6 order | K06 symbolic regression only | Cheap-first vs random vs costly-first at S6; solved per token | 10% or more fewer tokens to solve, same accuracy | Med |
| D01.06-U6 | Does depth (revise best) beat breadth (fresh draws) with a hard code checker at our scale? | Revise-best loop as default when a checker exists | S5 | K28 [E] but Eureka/ShinkaEvolve, frontier models, reward design | 32 fresh vs 2x16 revise-best; code-checkable items; accuracy | Revise-best wins by 3 points or more | High |
| D01.06-U7 | How much generate-and-test gain survives a noisy or soft checker? | Checker-strength rule in S0 (when to use search) | S0, G5, G12 | K26 [E] direction; LLM-SR/LaSR never measured without checker | Same loop with strong, noisy and self-judge checkers; gain over plain per arm | Gain under noisy checker is under half of strong-checker gain, so we add the cut-off rule | High |
| D01.06-U8 | Does a minimum number of distinct probes before the first fit help strong models? | Probe-count guard in S4 | S4 | K32 single-source (NewtonBench: strong models settle early) | Free tool use vs at least 5 probes; interactive law tasks; accuracy by model strength | 5 points or more for strong model, no loss for weak | Med |
| D01.06-U9 | Does cost-aware choice of the next check beat cheapest-first and random? | Expected-value-per-cost check order | S4/S7 | K30 single-source (King 2004 abstract; Eve replay) | Cost-aware vs cheapest vs random on items with unequal check cost; tokens to first failing case | Cost-aware uses half the tokens of random | Low |
| D01.06-U10 | Does an early one-variable probe cut tokens? | Irrelevance probe stage | S2 | K03 single-source (BACON.3, two orderings) | With vs without probe; tasks with distractor variables; tokens to solution | 15% fewer tokens, equal accuracy | Low |
| D01.06-U11 | Does reusing a solved sibling's relation help (symmetry, analogy)? | Reuse operator and subgoal library lookup | O7, memory | K04 single-source (BACON.5) | Sibling-task batches with and without reuse; accuracy on later siblings | 5 points or more on later siblings, no harm on unrelated | Med |
| D01.06-U12 | Does a derivability check against background facts prune bad candidates? | Reject-if-contradicts check | S4 | K24 single-source (AI-Descarte) | With vs without contradiction filter; items with stated background facts; accuracy | 4 points or more, no true candidates rejected | Low |
| D01.06-U13 | Is a sparse model call at stuck points as good as calling every step? | Call-at-decision-points rule | S6, G11 | K11 single-source (LaSR, symbolic regression) | Every-step vs stuck-points-only; long symbolic tasks; accuracy at equal tokens | Equal accuracy at 30% fewer tokens | Med |
| D01.06-U14 | Do small models keep population-search gains? | Budget rule for model size vs sample count | G12, budget | K33 contested; no single number | Small open model vs frontier, same loop, equal tokens, one checkable task | Small model recovers 70% or more of the frontier gain | Low |

## Open questions we cannot test on our bench yet
- KEKADA's heuristic list and goal rules: need the full 1988 paper (publisher blocked). Until then U2 is built from the abstract only.
- Adam 2009 and King 2004 full text: the pairing of the 3-fold and 100-fold cost cuts to baselines, and the gene count (6 or 12). Unblock: open the PDFs.
- FunSearch supplement (StarCoder comparison): needed for U14.
- Whether model-judge Elo or reviewer score predicts external truth on our own tasks: needs items with known outcomes beyond code checks.
- Best hypothesis count per budget across styles (64 candidates, sparse calls, 16 x 5): needs one harness running all three.
- Physical or wet-lab experiments: not reachable by our agent.
- Open-reasoning tasks with no checker: no way to score without human grading.

## Order to run
1. D01.06-U7 (checker strength): cheapest, and it sets which modes every other search idea applies to.
2. D01.06-U1 (signal-to-operator table with random-module control): the founding claim, never tested against a modern LLM at equal tokens.
3. D01.06-U3 (forced revision on exact counterexamples): fills the field's named open problem and shares items with U2.
