# Logic and philosophy of analogical arguments: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A11.06-U1 | Does a Hesse/Bartha record (link, source proof steps, target analogue per step, differences) improve judging analogical arguments? | Required record in O7 with code-counted unknowns capping confidence | O7 | K02, K19, K24; no LLM study (single-source, gap) | Plain judge vs record vs unstructured "list differences"; 30 classic + 30 held-out analogies with philosopher verdicts; agreement and false-accept rate | Record beats plain by >=8 points, CI excludes 0, and unstructured does not | High |
| A11.06-U2 | Does a causal-direction field (generative/preventive/common cause/common effect) stop wrong mappings? | Direction field and code refusal on mismatch | O7 | K05, K22, d07 (single-source) | Typed mapping with vs without field; >=40 McKay-type items where a preventive cause flips the verdict; accuracy on flipped items | >=10 points gain on flipped items, no loss on others | High |
| A11.06-U3 | Does order-swap accept-if-agree remove position bias in analogy choice? | Both-order run in code for any analogy choice | G5/S7 | K10, K25, b14, d14 (18 stories; general bias in 20 LLMs) | Single order vs both orders; 60+ stories; accuracy of accepted answers, flip rate | Accepted accuracy up >=5 points and accepted share >=70% | High |
| A11.06-U4 | Is the gain of self-generated analogues due to relevance or to example accuracy? | Keep O7 self-generation only if relevance matters; else use verified fixed examples | O7/G7 | K12, c10, d03, d04 (contested; GPT-3.5 math) | No example / relevant / random / verified fixed / accurate-irrelevant; math, BBH and puzzle items | Relevant beats accurate-irrelevant by >=3 points | High |
| A11.06-U5 | Does a required listed-differences field cut false acceptance of decoy sources? | Differences list required before an analogue is used | O7/G2 | K21, d06 (GPT-4, 2 pairs, precision about 0.5; single-source) | Free choice vs record; 30 source/decoy pairs; decoy false-accept rate | False-accept falls by >=20 points | High |
| A11.06-U6 | Does code execution on a mutated surface close the counterfactual gap for newer reasoning models? | Mutated-surface rule check as standard in O7 | G3/S4 | K09, c05 (original authors only); no reasoning-model run (older models only) | Text-only vs code-applied rule; counterfactual letter strings and renamed stories; accuracy by generalisation count | Code arm >=10 points above text-only on variants | Med |
| A11.06-U7 | How often do real tasks have a known determination set, and does code comparison prevent wrong transfers? | Determination check path in O7 | O7/G3 | K06, K23, d17 (single-source, no frequency data) | Audit 100 bench items for determinant sets; on those, model judgement vs code compare; wrong-transfer rate | >=15% of items have a set and wrong transfers drop >=50% | Med |
| A11.06-U8 | Does a human-written Walton critical-question list raise analogy-argument judging? | Fixed question list at the O7 accept step | G10 | K17, a24, d05 (single-source; model-generated questions cap at 57% Useful) | No list vs fixed list vs model-generated list; 60 analogy arguments; agreement with verdict | Fixed list beats no list by >=5 points and beats generated | Med |
| A11.06-U9 | Does a known essential difference in a retrieved exemplar lower accuracy (Hesse's negative analogy)? | Block exemplars with a flagged critical difference | O7 | K15, K21 (indirect only; contested) | Exemplars with injected critical difference vs matched neutral; accuracy | Drop >=5 points with difference and the flag removes it | Med |
| A11.06-U10 | Is a model-size gate needed for self-generated analogues? | Retrieve instead of self-generate under a size threshold | O7/G7 | K13, a20 (single-source, older models only) | Self-generated vs retrieved across our available models | Crossover found inside our model range | Low |
| A11.06-U11 | Does Thought Propagation beat plain revision? | Reuse of analogue solutions in S5 | O7/S5 | K16, c16 (single-source) | Plain revise vs analogue-solution reuse; shortest-path and planning items | >=5 points gain at equal tokens on two item types | Low |
| A11.06-U12 | Do similarity-count scorers fail against a causal-link checklist? (confirms a section 4b entry) | "Not to add: similarity-count strength" in section 4b | G5 | K03, a04 (philosophy only; no LLM data) | Count scorer vs checklist on held-out analogy items | Count scorer not above chance and checklist above it | Low |

## Open questions we cannot test on our bench yet
- Hesse 1966 and Bartha 2010 were never opened. Unblock: read the books or Norton's full chapter and build a labelled case set of successes and failures (Galileo, canals, caloric, Franklin).
- Philosopher verdicts for the U1 set need a second human rater; one rater's labels are weak ground truth.
- 2025-2026 reasoning models on Lewis-Mitchell counterfactual variants: no published run. Unblock: run ours, or find a new paper.
- Per-model ARN far-analogy values are unchecked; only the means (humans 94.1, models 39.6) are confirmed.
- Whether order and paraphrase effects hold beyond 18 stories. Unblock: a 60+ story set.
- Whether "essential difference" can be judged without a stated use; SEP says no. Unblock: tasks that state the use explicitly.
- Internal-state results (concept vectors, patching) need open weights; a black-box scaffold cannot test them.

## Order to run
1. U1 (checklist vs plain): the central guardrail question has zero studies, and 60 items make it cheap.
2. U5 (decoy-source false accepts): targets the one failure measured directly (precision about 0.5) on a small item set.
3. U4 (relevance vs accuracy): decides whether O7 self-generation stays, and reuses existing math and puzzle items.
