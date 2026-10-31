# Theory theory / child as scientist: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A14.01-U1 | Does a REVISE loop beat N independent attempts plus a consistency check on hidden-rule induction? | Keep S5 for this class, or cut it | S5 | K17 open; math-only evidence says self-inspection loses (d10, d11); no blicket test | 60+ blicket items (4 and 8 objects; OR, AND, XOR): N independent runs + data check vs REVISE loop; pooled accuracy | REVISE wins by 5+ points with CI excluding 0; otherwise replace S5 with resample + check for this class | High |
| A14.01-U2 | Does a counterexample step (code labels tests compatible/incompatible; inject "test what your guess says will fail") raise success? | Counterexample step in S5 and S7 | S5/S7/G | K10 single-source (Qwen3, one lab, not token-matched); K18 correlation in two labs | Hidden-rule items, thinking and non-thinking model: REVISE vs REVISE + counterexample step; success and I:C | +5 points pooled on the thinking model, no loss on non-thinking | High |
| A14.01-U3 | Does an enumerated pool of 16-96 distinct hypotheses with code elimination close the AND-OR gap? | Pool builder and elimination in S3/S4 for rule-induction class | S3/S4/O1 | K09 single-source; size and prior flatness confounded (d03) | AND 8-object items: default vs pool 32 vs pool 64 (pool cost counted); AND accuracy, gap to OR | AND accuracy +10 points and gap under 5 points at equal tokens | High |
| A14.01-U4 | Does a forced check of the final hypothesis against all collected data help? | Data-consistency check before commit | S8/S5 | K14 single-source (48% to 60%); symbolic check helped in ACRE (c20) | Items with collected data: commit vs forced check then commit; accuracy | +5 points at under 10% extra tokens | High |
| A14.01-U5 | Does replaying the full evidence log in code fix retroactive discounting (backward-blocking form)? | Log replay for credit assignment | S5/memory | K03 contested in humans; no LLM study (d17) | AB+ then A+ items: sequential vs replay; share correct on B | Replay beats sequential by 15+ points on this form | Med |
| A14.01-U6 | Does a typed context graph as S5 state help pooled accuracy, not only the subset? | Graph state for switch problems | S2/S5/memory | K13 single-source; graph alone lowered pooled accuracy (77.3 vs 87.3); no outside replication | Mid-run rule switch items: plain vs graph vs graph + monitor; pooled and post-switch accuracy | Pooled accuracy +3 points over plain, no rise in trap exposure | Med |
| A14.01-U7 | Does a contradiction monitor that widens the pool help beyond the graph? | Widening trigger at S5 to S6 | S5/S6/G1 | K13 (monitor added +1.4 to +2.3 points over graph; a24); fired in 77% under noise with no gain (K19) | Switch items: graph vs graph + monitor, equal tokens including monitor calls | +5 points over graph alone with no token overrun | Low |
| A14.01-U8 | Under noisy tests, does repeating the same test and tallying beat the scaffold? | Repeat-and-tally for noisy classes (flagged by code) | S4/S5 | K19 single-source; scaffold gave nothing at p=0.70 | Machines with activation 0.7 and 0.9: plain vs repeat-and-tally vs full scaffold | Tally beats plain by 10+ points at p=0.7 | Med |
| A14.01-U9 | Does planning all tests up front hurt, versus choosing each after seeing the result? | Rule: one test at a time, result visible | S4/S5 | K20 human-only (0.69, 0.45, 0.12); LLM correlation of info gain with success (c02) | AND items: write-all-tests vs sequential vs fixed transcript | Sequential beats batch by 10+ points on AND | Med |
| A14.01-U10 | Does a directive prompt narrow search as teaching narrows child exploration? | Prompt rule: no directive plan before first exploration | S0/G | K15 single-source child data; no LLM test (d17) | Multi-function hidden-rule tasks: open vs directive prompt; distinct hypotheses and functions found | Open arm finds 20% more hidden rules with no loss on the shown one | Low |
| A14.01-U11 | Does handing the agent an explicit list of rule forms (OR, AND, XOR, exactly-N) help? | Rule-form list in S2 | S2/S3 | K07 child data single-source; K08 LLM bias to OR | Hidden-rule items: no list vs list of 4 forms | +5 points on AND/XOR with no loss on OR | Med |
| A14.01-U12 | Is there an accuracy cliff as candidate causes go 2, 4, 8, and does S5 shift it? | Hypothesis-count rule in S0 gate (route to resample past the cliff) | S0 | K04 single-source (children); no LLM test | 2, 4, 8 causes; REVISE on vs off | Cliff found and an S0 rule beats a fixed route by 5 points | Low |
| A14.01-U13 | Does the incompatible-to-compatible ratio over the first tests predict failure early enough to trigger S6? | I:C flag as an S6 trigger | S5/S6/G1 | K18 correlation in two labs (d07, d08); no early-warning test | Log I:C over first 5 tests across 200 runs; predict final failure | AUC at least 0.70 on held-out runs, and trigger arm beats no trigger by 3+ points | Med |

## Open questions we cannot test on our bench yet

- **Child arm under active exploration.** Samiei 2026 is adults only. Needs a human lab study.
- **Original numbers for Gopnik 2001, Sobel 2004, Denison 2010.** Paywalled. Unblocked by library access to the PDFs.
- **Outside replication of Alderete and Jhaveri.** Needs another lab, or our own runs on a second model family (U2 and U6 give part of this).
- **Non-text and many-variable tasks.** Nothing beyond 8 objects. Needs a generator of larger hidden-rule or causal-graph tasks.
- **Noisy causal discovery with more than 4 causes.** Needs a noisy-machine generator with reliable ground truth.
- **LLM backward blocking in free-text tasks.** No study exists. U5 covers a code-level version only.
- **Hypothesis-space size versus prior bias.** Needs a design that varies pool size while holding prior flatness fixed (for example, many near-duplicate hypotheses).
- **Pedagogical narrowing in agents.** Needs a multi-function hidden task with an open-ended success count.

## Order to run

1. **A14.01-U1 (REVISE vs N independent attempts + check).** It decides whether S5 earns its place for rule induction. The only nearby evidence says self-inspection loses, and the other tests build on its answer.
2. **A14.01-U3 (enumerated pool with code elimination).** Largest published effect (AND-OR gap closes), implementable in code, and cheap to run on the same items as U1.
3. **A14.01-U2 (counterexample step) with U4 (final data check) as extra arms in the same batch.** Each is one added line to REVISE and has the best single-source gains (blicket 0.57 to 0.86 at 32B; 48% to 60% at 4 nodes).
