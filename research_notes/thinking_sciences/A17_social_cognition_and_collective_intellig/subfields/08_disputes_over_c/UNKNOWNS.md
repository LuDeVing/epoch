# Disputes over c: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A17.08-U1 | Does a forced private-fact disclosure step fix information pooling across sub-agents? | Disclosure step before any merge of sub-agent outputs | S3, S4 | K19, K22; single-source (one team, GPT-4.1, oracle arm) | Free merge vs structured fact list (code merges) vs passive summary; 30+ hidden-profile items; accuracy | Gain of 0.15+ absolute over free merge, CI excludes 0, tokens within +10% | High |
| A17.08-U2 | Is the LLM group factor just shared single-model ability? | A bench rule: never credit a group factor without the single-agent control | memory (bench rule) | K21, K13; single-source | Same 6+ task battery for single agents and k-agent groups; compare first-eigenvalue share and AVE | Single-agent share within 10 points of group share (then c-like claims are dropped for good) | High |
| A17.08-U3 | Does debate ever beat self-consistency at equal tokens for us? | Narrow debate-like operator on named task classes (relaxes G9) | O, G9 | K18; contested (Wunderlich +1.3 vs several null or negative studies) | SC vs 3-agent debate vs heterogeneous debate; MMLU-Pro, BBH and bench items; accuracy over 3 seeds | Debate beats SC by 2+ points, CI excludes 0, on at least 2 task classes | Med |
| A17.08-U4 | Does model or temperature heterogeneity beat identical samples? | Mixed-temperature or mixed-model sampling in S3 | S3 | K17, K18; Riedl OR 1.50 per temperature unit; Zhang heterogeneous 76.7 vs 72.5; older models | Same-model samples vs mixed temperature vs mixed model; k fixed; accuracy and answer diversity | Gain of 2+ points over same-temperature samples, CI excludes 0 | High |
| A17.08-U5 | Can debate be gated cheaply (self-agreement gating fails: 66% unanimous but wrong)? | A gate for when to spend on multi-agent steps | S0, S6 | K24; single-source | Always SC vs vote-entropy gate vs learned gate; mixed items; accuracy per token | Gate recovers 50%+ of oracle gain at no extra cost | Low |
| A17.08-U6 | Do process or coordination steps help only on split-information tasks? | Task-class routing for process steps | S0, O | K12; single-source, human data | Step on vs off; split-fact tasks vs single-solver tasks; accuracy difference | Gain on split tasks 0.10+ and under 0.02 on single-solver tasks | Med |
| A17.08-U7 | Does skill-matched role assignment (strong agent at hub) beat flat groups at equal tokens? | Hub-and-spoke for any sub-agent step | O, S3 | K14; single-source (Zhou, older models) | Flat vs hub with strongest model; 3 task types; accuracy | Hub wins by 2+ points on 2 of 3 task types | Med |
| A17.08-U8 | Does a one-factor structure hold for agent batteries, or are two factors better? | A report rule: fit 1- and 2-factor models before claiming a general score | memory | K11; human only (Graf, Rowe 2024, Kommol) | Fit 1, 2, 3 factors to bench scores of 20+ configs over 8+ tasks; CFI, RMSEA, parallel analysis | Two-factor model CFI higher by .05 or more | Low |
| A17.08-U9 | Is a c-like factor stable across protocols (not only debate)? | Nothing; it would end the question | none | K13; one framework | Factor from debate vs vote vs hub groups; correlation of loadings between protocols | Loadings correlate above .8 across protocols (otherwise drop the c idea) | Low |
| A17.08-U10 | Do persona or ToM prompts change success anywhere? | Social-framing prompt for named tasks | S3 | K17; null in one game, GPT-4.1 | Plain vs persona vs persona+ToM; 200 runs per arm; success rate | Gain of 3+ points, CI excludes 0 | Low |
| A17.08-U11 | Is the ACI-style plug-in gain larger than seed noise? | Predicted-factor objective for design search | G7 test harness | K15; single-source, one run per cell | Designs chosen by ACI vs by held-out accuracy, 5 seeds | Mean gain above 2 SD of seed noise | Low |

## Open questions we cannot test on our bench yet
- Per-sample first-factor values from Credé and Howardson 2017 and the 2018 reply. Needs the original papers; we read press accounts only.
- Kommol, Riedl, Woolley 2025 fit indices and AVE. Needs the full preprint text.
- Why independent labs find c-to-IQ r = .32 and Woolley-affiliated labs .10. Needs raw data from both; human studies cannot be run on our bench.
- Any randomised intervention that raised c and transferred to a held-out task. None exists in the literature found; it would need human experiments.
- Independent replication of Zhou 2026. Needs their code and group configurations, or a second team.
- Gupta 2024 nudge study and McDonald 2026 effect sizes. Only press summaries were read.

## Order to run
1. A17.08-U2 (single-agent factor control): cheapest, and it decides whether any c-like language belongs in our docs at all.
2. A17.08-U1 (disclosure step): largest reported effect (.233 to .967) and cheap to build in S3 and S4; must be confirmed at equal tokens and without the oracle.
3. A17.08-U4 (heterogeneous sampling): the one multi-agent setting with positive evidence in several papers; low implementation cost.
