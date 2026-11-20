# Early, attenuation and late selection: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A07.01-U1 | Does a rewrite-and-discard filter beat plain thinking on distractor items with a current model? | Filter operator before solving | O / S0 gate | K09 single-source (LLaMA-2-70B only) | plain vs filter; GSM-IC-style, 3 distractor types; accuracy, rewrite tokens counted | filter beats plain by 3 points or more, CI excludes 0 | High |
| A07.01-U2 | Does the filter beat best-of-N voting at equal tokens? | Pick filter over vote for distractor items | O / G4 | K23: no study found | filter vs N-vote sized to the same tokens; same items; accuracy | filter beats vote by 2 points or more | High |
| A07.01-U3 | Does a one-line "ignore irrelevant text" help current models? | Cheap ignore line in prompt template | G | K18 contested (Weston none; Rajeev 37.5% to 9.9%) | plain vs ignore line vs filter; same items; accuracy | ignore line gains 3 points or more at under 1% extra tokens | High |
| A07.01-U4 | Does recite-then-solve help strong models on long inputs? | Recite step for long-context reads | memory | K19 single-source (7B +31.2, GPT-4o +4.0) | full vs recite vs top-k; items at 10k and 50k tokens; accuracy | gain 3 points or more net of recite tokens | Med |
| A07.01-U5 | Does a focused memory slice beat full history? | Retrieve-then-read memory rule | memory | K20 single-source, vendor report | full vs focused slice; long run logs; accuracy and tokens | focused wins on 70% of items at lower tokens | High |
| A07.01-U6 | Does key-evidence placement (first or last) matter for current models? | Placement and truncation rule | memory | K11 contested (2023 strong, 2025 mixed) | middle vs first vs last at 25% and 90% fill; accuracy by position | position gap 5 points or more at our fill levels | Med |
| A07.01-U7 | Does a salient self-relevant irrelevant token (task name) capture reasoning? | Guardrail to strip self-referential noise from inputs | G | K03 human only; d01, d02 adversarial triggers only | with vs without inserted token; accuracy, answer length | accuracy drop 3 points or more, or length up 20% | Low |
| A07.01-U8 | Does distractor-count slope flatten with a filter? | Log distractor count; filter-threshold rule | G7 logging / O | K13 established for plain models | counts 1, 5, 15; plain vs filter; slope | slope cut by half | Med |
| A07.01-U9 | Does vote-over-N still help against distractors on reasoning models? | Vote only on distractor-prone items | O / G4 | K08 single-source, older models | N-vote vs single; distractor items; accuracy | +3 points at N=5 over single, equal tokens | Low |
| A07.01-U10 | Does the filter cost accuracy on clean items? | Gate: filter only when distractor risk is flagged | S0 gate | none | filter vs plain on clean items; accuracy | filter costs 1 point or less, else gate it | High |
| A07.01-U11 | Do same-topic or role-overlap distractors hurt more than off-topic ones on current models? | Distractor-type risk score in S0 | S0 gate | K07 and b23 (2023 models only) | three distractor types; plain; accuracy gap | gap 5 points or more | Low |
| A07.01-U12 | Does a step-check (PRM-style) cut distractor errors on shifted items? | Step-check operator | G3 / O | c12 single-source, +2.57 to +6.29 | beam with check vs plain; shifted items; accuracy | +3 points at equal tokens | Low |

## Open questions we cannot test on our bench yet
- Original numbers for Treisman 1960, Treisman and Geffen 1967 and Moray 1959 (the "4 of 12"). Needs library access to the originals. No schema impact.
- Independent replication of Snowden and Gray (load independence). Needs human experiments. No schema impact.
- Span-by-name link with a larger sample and a like-for-like quartile contrast. Human experiment. No schema impact.
- Mixed-language interference for text agents. The MUSI 0.955 same-language cell may be a table slip; needs the authors or a rerun, and audio.
- Whether weight-level fixes (Selective Attention, Differential Transformer, head scaling) matter to a scaffold. Needs open weights and training; outside scope.
- Natural (unsearched) distractor rates for reasoning models. CatAttack triggers were searched adversarially. Needs a log of real distractors from our own runs.

## Order to run
1. **A07.01-U10 together with U1** (clean-item cost and filter gain on one item set): cheapest, and the filter either pays for itself under G7 or is dropped.
2. **A07.01-U2** (filter vs N-vote at equal tokens): no study exists, and the answer decides whether the filter earns a slot next to voting.
3. **A07.01-U5** (focused memory slice vs full history): cheap, high expected gain, and it shapes the memory design directly.
