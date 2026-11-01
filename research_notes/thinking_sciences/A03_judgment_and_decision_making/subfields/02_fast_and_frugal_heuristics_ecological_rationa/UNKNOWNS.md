# Fast and frugal heuristics, ecological rationality: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A03.02-U1 | Does a prompt showing only the top k validity-ordered cues match all cues? | Cue-limited input in simple modes | S0, O | K21, K16; d10 indirect; no direct study | Arms: all cues, top-k (1-3), k random. Items: city-size pairs + one new cue task, 100 pairs. Metric: accuracy, tokens | Top-2/3 within 1.5 points of all cues at <= 70% tokens, and beats random-k by >= 3 points | High |
| A03.02-U2 | Is sample agreement a valid one-reason cue for the S0 gate? | Agreement-based skip/escalate rule per task class | S0, G | K19; d01, d03, d04; never tested as a cue; validity domain-specific | Arms: gate by agreement over 5 samples, always-direct, always-full. Items: bench by class, 40+ per class. Metric: AUROC per class; accuracy at equal tokens | AUROC >= .75 in a class and gate beats always-full by >= 2 points at equal tokens in that class | High |
| A03.02-U3 | Does cheap-first cascade (direct, then escalate on failed check) beat always-full? | Cascade as the S0 default | S0, O | K13, K20; c14-c16, d06, d07; trained gates only | Arms: cascade vs always-full vs always-direct. Items: full bench. Metric: accuracy, total tokens, false-skip rate | Accuracy within 1 point of always-full at <= 70% tokens, or better at equal tokens | High |
| A03.02-U4 | Does longer thinking hurt on indeterminate items on our model? | Short-check route for indeterminate items | S0, G11 | K10; single-source (Bogdan), directional in frontier; d08, d09 same sign | Arms: direct, short CoT, long CoT. Items: 30+ cannot-be-determined + matched controls. Metric: correct-abstention rate, key-scored | Direct beats long CoT by >= 8 points on indeterminate items with controls flat (within 3) | High |
| A03.02-U5 | Does a data-derived 3-question FFT route modes better than the LLM choosing? | FFT gate in S0 | S0 | K09, K14; a24, c25; trees from LLM rules lose; no head-to-head | Arms: FFT from calibration data, LLM-chosen mode, always-full, always-direct. Items: bench with class tags, split calibration/test. Metric: accuracy at equal tokens; false-skip rate | FFT >= LLM-chosen mode on accuracy and tokens, by >= 1 point or >= 15% fewer tokens | High |
| A03.02-U6 | Does the model learn noncompensatory cue order from a few in-context pairs? | In-context cue-order learning for gate features | O, memory | K22; d11 numeric only; no Rieskamp-Otto test | 8/16/32 labelled binary-cue pairs from a noncompensatory vs a compensatory generator. Metric: share matching first-discriminating-cue vs weighted sum | >= 70% order-consistent choices at 16 pairs on the noncompensatory generator, and different from the compensatory one | Med |
| A03.02-U7 | Does outcome feedback let the agent pick modes better over a run? | Per-class running success rate to choose mode | S0, memory | K08; human only (28% to 71%) | Arms: fixed mode vs mode by running success per class. Items: 100+ sequential with feedback. Metric: cumulative accuracy at equal tokens | Cumulative accuracy >= fixed best mode + 2 points after 100 items | Med |
| A03.02-U8 | Where do simple modes stop winning as examples increase? | Rule: use simple mode when examples/cases below N | S0 | K02; human and ML only (a11, a25); untested on LLMs | Arms: simple vs full mode with 0, 2, 8, 32 worked examples. Items: 2 task classes. Metric: accuracy gap by example count | Gap changes sign or shrinks by >= 50% across the range; then we add a threshold rule | Med |
| A03.02-U9 | Does stepwise reasoning hurt on perceptual, exception-rule and spurious-feature items on our model? | Class flag routing these to direct | S0, G11 | K12; c06, c07; model-specific (Claude 3.5 Sonnet unchanged) | Arms: direct vs stepwise on 3 item classes. Metric: accuracy by class | Direct >= stepwise + 5 points in a class; then flag that class | Med |
| A03.02-U10 | Is mode use one pure rule or a per-item mixture? | Per-item reporting as standard in bench output | measurement | K06; contested in humans (b06) | Per-item mode-use logs from U3/U5. Metric: pure vs mixed share | Report only. Adopt if mixed share >= 20% (averages would then mislead) | Low |
| A03.02-U11 | What is the real token and latency cost of few-cue vs many-cue modes? | Cost table for the gate | G7 | K07; d06 tokens only; latency unmeasured | Arms: 1, 3, 9 cues; measure tokens and wall-clock. Items: 50. Metric: tokens, seconds, accuracy | Few-cue mode is >= 30% cheaper in seconds, not only tokens; otherwise drop cue count as a budget proxy | Med |
| A03.02-U12 | Do tuning-installed heuristics bias our model on gate-relevant items? | Bias probe set in the bench | G | K15; c04, c11, c27 | 10 classic items (CRT-like, framing, decoy) x 3 phrasings. Metric: share of intuitive-wrong | Adopt probe set if any family is above 30% intuitive-wrong; then add input hygiene for that family | Low |

## Open questions we cannot test on our bench yet

- Czerlinski et al. (1999) exact percentages and modern large data sets. Unblock: obtain the chapter or rerun the 20 data sets ourselves with proper tuning.
- Peer-reviewed LLM work on ecological rationality (JDM, Cognition, Psychological Review, CogSci). Unblock: a literature search once search quota returns.
- False-skip cost in general. Unblock: needs the full-schema results on the same items (comes out of U3 and U5).
- Whether the recognition-heuristic dispute (pure vs mixed use) matters for an agent. Unblock: only relevant if U10 shows mixed use.
- Black-box access to internal familiarity signals (known-entity direction, semantic-entropy probe). Unblock: open-weight models or an API exposing hidden states; sample agreement (U2) is the black-box proxy.
- Whether reasoning-trained frontier models overthink on our items. Unblock: run U4 on reasoning-trained models with budget controls.
- Rieskamp-Otto adaptive strategy selection with an LLM across 100+ trials with feedback. Partly covered by U7; a full replication needs a controlled environment generator.

## Order to run

1. A03.02-U3 (cascade vs always-full): cheapest, uses the existing bench, and gives the false-skip and token numbers every other gate test needs.
2. A03.02-U4 (indeterminate items, direct vs long CoT): small item set, key-scored, and it decides whether the "stop early" rule needs a class flag on our model.
3. A03.02-U1 (cue-limited prompt vs all cues): the open core question of this subfield, never run by anyone, and cheap on city-size pairs.
