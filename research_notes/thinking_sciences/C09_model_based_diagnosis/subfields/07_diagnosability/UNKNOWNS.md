# Diagnosability: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C09.07-U1 | Does a script-computed separability table plus a "need probe X" verdict cut confident wrong answers on non-separable pairs? | S0 separability check; "ask a probe" verdict | S0, S7, G | K26, K29, d02, d15 (single-source; observability only) | 60 generated systems, 15% non-separable; scaffold with vs without check; wrong-confident rate and accuracy on separable pairs | Wrong-confident rate falls at least 30% relative and separable accuracy loses under 2 points | High |
| C09.07-U2 | Does code-scored probe choice (even split or EIG) beat free probing for a frontier reasoning model? | Operator: split probe selected by code | O, S7, G5 | K07 established on older models; K30 contested (d08, d10, d12) | Items as T1; reasoning model alone vs + code-split vs best-of-N at equal tokens; accuracy | At least +5 points over best-of-N at equal tokens | High |
| C09.07-U3 | Is the gain from the ledger or from the scored split step? | Keep only the part that pays | S ledger, memory | K11, d11 (split carries most; no ledger-only arm) | 4 arms: free text; ledger only; split only; ledger + split; accuracy | Ledger-only beats free text by at least 5 points, else drop the ledger | High |
| C09.07-U4 | Can an LLM tell which hypothesis pairs are inseparable from a small model? | Let the model do the check (else code does it) | S0 | K32 (no study); d04 (0.30-0.53), d15 | 100 small models with known isolability matrix; LLM vs script; precision/recall on inseparable pairs | LLM recall and precision both at least 0.9; else keep code | High |
| C09.07-U5 | Does the top-two separator (SIA) replicate at equal tokens? | Operator: question that splits the top two | O, S7 | K15 (single group, one benchmark, LLM judge) | T3 items; free probing vs SIA vs Ask-5 vs best-of-N; final accuracy and potential-final gap | At least +5 points over best-of-N and gap down at least 5 | Med |
| C09.07-U6 | Does a "name a probe that would break the leader" step lower confirmation bias at equal tokens? | Falsifying-probe operator | O, G | K21, c24 (42% to 56%, single-source) | Rule-discovery items; with vs without step; discovery rate | At least +8 points | Med |
| C09.07-U7 | Does code hitting-set enumeration before ranking catch multi-fault cases the LLM misses? | Tool: hitting-set enumerator at S3 | S3, G5, tools | K17 (1 of 13 models found the double fault), K18 | Multi-fault circuits (1-3 faults, up to about 150 diagnoses); LLM enumerates vs code then LLM ranks; recall of minimal diagnoses | Recall gain at least 20 points on 2-3 fault items | Med |
| C09.07-U8 | Does re-checking separability after each observation beat a fixed probe plan? | Re-check step after each observation | S, O | K06 (theory; no LLM test) | Items where an observation removes a separating probe; re-check vs fixed plan; probes used and accuracy | Fewer probes at equal accuracy, or at least +5 points | Med |
| C09.07-U9 | Does a code simulator for per-hypothesis predictions beat LLM derivation? | Tool: predictor in code where the model is computable | S2, tools | K28; d05 (0.88-1.00 given vs 0.51-0.74 derived) | Same items; LLM-derived vs code-given predictions; accuracy | At least +10 points when a simulator exists | Med |
| C09.07-U10 | Does an abstain-with-cost option improve calibrated accuracy on provably unseparable items? | Cost-weighted "need more evidence" action | G, S7 | K31, d13, d14 (benchmarks lack an abstain option) | Mixed items, 20% non-separable; with vs without abstain cost; accuracy on answered items, coverage, score under cost | Score under cost improves with coverage loss under 15% | Med |
| C09.07-U11 | Does probing the suspected cause in both directions raise accuracy (causal, not correlational)? | Contrastive-pair probe rule | O | K27, d06 (0.71 vs 0.04, correlation only) | Items with a perturbable cause; forced both-direction probe vs free; accuracy | At least +10 points | Med |
| C09.07-U12 | Does acting to trigger an indicator event expose faults that observation alone cannot? | "Act to expose" operator | O | K03 (single-source theory) | Items with command-triggered faults; observe-only vs act; detection rate | At least +15 points detection | Low |
| C09.07-U13 | Does a cost-weighted probe order beat cheapest-first at equal budget? | Cost-aware probe score | O, G12 | No source (K04: NP-hard in general) | Items with unequal probe costs; cheapest-first vs gain-per-cost; accuracy at fixed budget | At least +5 points | Low |
| C09.07-U14 | Does the ledger reduce adoption of a plausible wrong hint? | G: resist leading hints | G | K16 (10 pairs, 80.0 to 76.0) | At least 100 hint pairs; ledger vs no ledger; adoption rate | Adoption falls at least 30% relative | Low |

## Open questions we cannot test on our bench yet
- Whether frontier 2026 reasoning models behave like the older models in UoT and BED-LLM. Needs access to those models at equal-token settings; our bench may need a reasoning arm first.
- True isolability ground truth for real tasks. Needs generated systems with a computed isolability matrix; real benchmarks (Cloud-OpsBench) mix telemetry limits with missing source access.
- Open-set (no candidate list) gains at equal tokens. Needs a hypothesis-generation scorer that does not rely on an LLM judge.
- Independent replication of SIA by another group. Cannot be done by us as an independent group; only a re-implementation check.
- Whether abstention is rewarded by real graders. Existing benchmarks give no credit for it; needs our own scoring rule.
- Cost of information-gain scaffolds in wall-clock terms (25x to 61x slower in published work). Needs token and time accounting in the harness.

## Order to run
1. C09.07-U3 (ledger vs split ablation): cheapest, decides which part of the scaffold to keep before anything else is built.
2. C09.07-U2 (code-split probe on a reasoning model vs best-of-N): the main established-but-contested claim; a null result would remove the largest item.
3. C09.07-U1 (separability check plus "need probe X"): the one idea unique to this subfield, with no LLM evidence yet; the same generated items serve U1, U3 and U4.
