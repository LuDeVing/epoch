# Axiomatic design: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E07.06-U1 | Does a matrix-first scaffold (FRs, DPs, matrix, program flags knots) beat free design on multi-requirement tasks? | An S2 sub-step: build a requirement-by-choice matrix, program reports coupled knots | S2, S3, G5 | K15, K18: no LLM study; human cost data only (b02, d04) | Plain vs matrix-first; 40 tasks with 4-8 requirements and known conflicts; violated requirements, program-scored | Fewer violations by 10 percent or more on coupled items, and no loss on uncoupled items, at equal tokens | High |
| E07.06-U2 | Do LLM agents show the geometric (3.4^n) blowup on coupled numeric tuning, and does probe-then-solve remove it? | A rule: for coupled numeric tuning, probe n+1 times, estimate the map, solve by program | G5, G12, S3 | K02: human, 2 sources, same university; not tested on LLMs | Plain trial loop vs probe-then-solve; slider tasks n=2 to 5, 20 per size; evaluator calls to hit 5% range | Plain arm grows at least 2x per added variable and the solve arm uses at least 50% fewer calls at n>=4 | High |
| E07.06-U3 | Can the model classify coupling from text, or must a program do it from model-filled cells? | Fill cells by model, classify by program; never ask for a label | S2, G5 | K05: humans fail (80%+ on faucet, anecdotal); K18: no LLM study | Direct label vs cell-fill plus program; 50 designs with program-known class; accuracy by class | Cell-fill arm beats direct by 10 points or more on coupled-looking-uncoupled items | High |
| E07.06-U4 | Does a solution-neutral restatement of requirements raise answer quality? | An S1 line: restate each need as what, not how | S1, G2 | K06: argued (Homay), detection only (d11); human-only | Direct vs restate-first; 40 framing-trap items; correctness, lock-in rate | At least 5 points gain on trap items and no loss on plain items | Med |
| E07.06-U5 | Does injected guidance hurt on larger structure tasks, and for which model? | Rule: guidance blocks off by default above a size threshold; tune per model | G8, memory | K12, K19: single-source, Claude only; GPT and Qwen reverse (d07) | Hints shown vs hidden; 10, 15, 20, 30 node ordering/clustering tasks; final gap and early gap | Final gap worse with hints by 3 percent or more at a size, in two or more tasks | Med |
| E07.06-U6 | Does a proposer-plus-program-scorer loop with best-plus-random pool beat plain sampling outside DSMs? | Use the pool design for any structure search in S3/S4 | S3, S4, O3 | K11: established for DSMs, same-lab authors (c15, c17) | Plain best-of-N vs pooled loop; 30 non-DSM ordering/assignment tasks with program cost | Pooled loop reaches reference cost in 20 percent fewer evaluations or lower final cost | Med |
| E07.06-U7 | Does explicit edge direction in a graph prompt matter outside the one UCAV test? | Rule: always pass directed edges | S3 | K13: single-source (c19) | Directed vs undirected list; 20 tasks of 12-20 nodes; gap to reference | Directed beats undirected by 3 percent or more | Low |
| E07.06-U8 | Does an off-diagonal coupling count rank designs better than the three-way label? | A numeric coupling score at S7 as a tie-break | G5, S7 | K17: single-source, abstracts only (d13, d14) | Label vs count; 40 pairs of designs in the same class; agreement with ground-truth quality | Count agrees with truth 10 points more often than chance | Low |
| E07.06-U9 | Does the information axiom (pick the design with the larger chance of meeting each requirement) beat a plain preference as a tie-break? | A tie-break at S7 using estimated success probabilities from running checks | S7, G8 | K16: no outcome test; fuzzy multi-criteria use only | Plain pick vs log2(1/p) pick; 40 pairs of passing designs with stress inputs; robustness on held-out stress set | Wins by 5 points on held-out stress | Low |
| E07.06-U10 | Does the coupled-top-level warning (Suh S3: wrong top-level FRs cannot be fixed below) hold for LLM decomposition? | A check at S1: re-validate the top-level requirement list before decomposing | S1, O3 | K06, a03: theory only | Decompose with and without top-level re-check; 30 tasks with a planted wrong top requirement; rate of recovery | Recovery rate up 15 points | Med |
| E07.06-U11 | Is any AD scaffold gain real in the claimed agentic design setting (Joshi: coupling -34.2%, iterations -41%)? | Nothing yet; only after the full text defines coupling | G5 | K14: single-source, unverified | Read full text; then replicate with our own coupling count | Coupling measure defined and gain at least 20 percent at equal tokens | Low |

## Open questions we cannot test on our bench yet

- **Human-versus-LLM effort curve.** We need a slider-style interface with a hidden coupled map and call counting. Unblock: build the evaluator (also needed for U2).
- **Full texts of Goehler 2016 and Hirschi and Frey 2002.** Effect sizes and robustness conditions are unseen. Unblock: library access or a retried fetch.
- **Independent replications of Frey and Hirschi.** The 77 citing works were not read. Unblock: retry OpenAlex when rate limits clear.
- **Joshi 2026 full text.** Blocked. Unblock: author copy or SSRN download.
- **Dubois, Tate et al. 2012 (AD against other methods).** Title only. Unblock: full text.
- **Why knowledge hurts Claude on large DSMs.** Authors' semantic-misalignment account is a hypothesis. Unblock: U5 with a variant using shuffled node names.
- **Real design tasks with ground-truth coupling.** Our bench has puzzles and forecasts, which have no FR-DP matrix. Unblock: build a synthetic multi-requirement item set (U1, U3).
- **Information axiom outcome data.** None found. Unblock: U9 on a synthetic set.

## Order to run

1. **U2 (probe-then-solve vs trial and error, n=2 to 5).** Cheapest, fully program-scored, and the only claim with two human sources behind it.
2. **U3 (classification of coupling from text).** Cheap, uses the same synthetic item generator as U1, and tells us whether the model can be trusted to label at all.
3. **U1 (matrix-first vs free design).** The central question for this subfield. Run it after U3 so the matrix-building step is already validated.
