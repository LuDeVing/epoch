# Blend network types: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| F01.03-U1 | Does forcing "double-scope" (both frames give roles, emergent structure) beat "single-scope" or plain on novelty without losing validity? | Open-mode operator: choose combine style by goal | O3 | K02 (no study varies type); K20; d13 trade-off (single-source) | Plain vs single-scope vs double-scope prompts; 40 cross-frame open items; blind novelty and validity, distinct count | Double-scope novelty beats plain by 0.3 on 5-point scale and validity drops under 10 points | High |
| F01.03-U2 | Does an "inputs / how combined / implications" field plus critic with backtrack help text tasks? | Staged combine template in open mode | O3, S3 | K07 (image only, author metrics, extra calls) | Template+critic vs one-shot at equal tokens; open items and cross-frame reasoning items; blind ratings plus held-out pass | Gain of 5 points win rate or 0.3 rating, holds at equal tokens | High |
| F01.03-U3 | Does a code check that the shared slot holds in both inputs raise valid-blend rate? | Generic-space gate before any blend | O3, S4 | K05 (single-source: 43.4% vs 97.1% given valid space); no one tested a gate (d09) | Gate vs no gate; 50 cross-frame pairs; valid-blend rate by blind judge, final pass rate | Valid rate up 10 points and final pass not down | High |
| F01.03-U4 | Does code-side recombination of listed parts beat one-shot at equal value? | Code combine step for open mode | O3, S3 | K16 (cooking only; value fell to 85% vs 98% in Exp 2) | Model lists parts, code recombines, validity check vs one-shot; 40 text items; blind novelty and value | Novelty up 0.3 and value within 3 points | High |
| F01.03-U5 | Is a rejection rule for splittable (juxtaposed) blends useful? | Reject-juxtaposition check in code | G5, S4 | K17 (established as a failure mode, rule itself untested) | With vs without filter; 40 blend items; Kombine-style integration score, distinct count | Integration score up and no loss in validity | High |
| F01.03-U6 | Can the network type be labelled reliably by the model and checked by code? | Type label in memory and S9 lessons | O3, memory | K01 (definition only, no coder validated) | Two runs label 100 agent cross-frame steps; code checks role sources; agreement | Agreement at or above 80% and label predicts error rate | Med |
| F01.03-U7 | Do cross-frame steps have higher error than same-frame steps in agent traces, justifying a check after them? | Mandatory check stage after cross-frame steps | G3, S4 | K03 (human ERP only; rival theories explain it) | Tag steps in existing traces; error rate by tag; no new arm needed | Cross-frame error rate at least 1.5 times same-frame | Med |
| F01.03-U8 | Does ranking far pairs by low co-occurrence beat raising temperature? | Far-pair ranking in open mode | O7, S3 | K22 (GPT-2, art domain, GPT-4 judge; single-source) | Ranked vs temperature vs default; 30 open prompts; blind novelty, coherent share | Novelty up 0.3 with coherence within 5 points | Med |
| F01.03-U9 | Does checking both input orderings help in text? | Order-swap step with check | O7, S4 | K09 (diffusion only) | One order+check vs both orders+check; 40 items; pass rate | Pass rate up 3 points | Low |
| F01.03-U10 | Does a post-blend check that each borrowed role holds in the target frame catch errors? | Role-validity check | G3, S8 | K20 (argued from examples, single-source) | With vs without check; items with ground truth; error rate | Errors caught at least 20% more | Med |
| F01.03-U11 | Do far frame pairs raise ungrounded claims? | Lower trust, more checking for far pairs | G3 | K12 (position papers only) | Near vs far pairs; held-out fact check; ungrounded-claim rate | Far rate at least 1.3 times near | Low |
| F01.03-U12 | Does the Eppe-style score (info + compression - imbalance, zero if inconsistent) predict blind-judge preference? | Code-side blend ranker | G5 | K21 (unvalidated, no empirical evaluation) | Score candidate blends; correlate with blind preference | Spearman at or above 0.4 | Low |
| F01.03-U13 | Does extra checking on the implication step of a blend beat equal checking everywhere? | Weighted check budget | G5 | K08 (image, GPT-4o judge, single-source) | Equal vs implication-weighted check at equal tokens | Pass up 3 points | Low |

## Open questions we cannot test on our bench yet
- Whether network type predicts novelty for real human products: needs a coded corpus of inventions or designs (Dreyfus 2014 and Turner 2014 not opened).
- The 2002 book chapter on types: needed to confirm definitions and any novelty claim beyond the 1998 and 2003 papers; needs a copy of the book.
- Temperature and model-size effects on blend quality: Kombine publishes one temperature and no Q split; needs the data release or a rerun.
- Whether Xu et al.'s 16.8% gain is on analogy appropriateness: needs the metric definition opened.
- Whether Kombine's model identities are right: names are as printed in the paper.
- Independent human-judge validation of blend novelty for our outputs: needs a rater pool; LLM judges carry self-preference risk.

## Order to run
1. **U3 (generic-space gate):** cheapest, a code check, and it targets the one measured bottleneck (43.4% valid vs 97.1% given a valid space).
2. **U5 (reject juxtaposition):** a pure code filter on an established failure mode, nearly free.
3. **U1 (single vs double-scope prompts):** the first direct test of the subfield's central claim; it decides whether any type label belongs in the schema.
