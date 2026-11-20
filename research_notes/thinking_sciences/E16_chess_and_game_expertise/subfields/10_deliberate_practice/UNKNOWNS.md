# Deliberate practice: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E16.10-U1 | Does a one-line-lesson memory give a practice effect on our benches, and where does it plateau? | Cross-item lesson memory with a round cap | memory / S9 | K27; d04, d12, d13, d14 (other benches, older models) | Scaffold without memory vs with similarity-retrieved lessons; 20-40 same-class items with a code check; pass rate by round and on held-out items | Gain of at least +3 points on held-out items at equal tokens, interval excludes 0 | High |
| E16.10-U2 | Does weakness-targeted practice beat uniform practice and extra test-time samples? | Class-record-driven practice phase for batch runs | memory / S0 / S9 | K11 (single-source, human, observational); K30 (trains weights) | Practice on lowest-pass-rate classes vs random classes vs no practice with tokens spent on samples; mixed pool, then unseen test items; test pass rate and tokens per point | Targeted beats both by at least 2 points at equal tokens | High |
| E16.10-U3 | Is a code verifier step worth its tokens, by base solve rate? | Verifier step in S4/S8 for classes with a sound check | G2 / S4 / S8 | K28 (established direction); K29; K17 (verifier lowered ChessGPT puzzle accuracy) | No verifier vs self-verifier vs code verifier; items stratified low/mid/high base rate; accuracy and verifier false positives | Code verifier beats none by at least 3 points in the mid stratum and loses no more than 1 point elsewhere | High |
| E16.10-U4 | Which part of "deliberate" carries the gain: goal, feedback or coach selection? | Drop the coach component if it adds nothing | S0 / S9 | K32 (human re-analysis, p=.64, single-source) | Goal only vs goal plus code check vs goal plus check plus coach model choosing classes; test pass rate | Coach arm beats goal-plus-check arm by at least 2 points; otherwise keep the coach out | Med |
| E16.10-U5 | Do similar-task examples beat random and concept-labelled examples? | Similarity retrieval plus concept labels for lessons | memory / O7 | K33, d13 (single-source); K18 (human, no control) | No examples vs random vs similar vs concept-labelled; unseen items; pass rate and right-to-wrong flips | Similar or concept arm beats random by at least 3 points and right-to-wrong flips do not rise | Med |
| E16.10-U6 | Does scaffold gain shrink as base-model strength rises (ceiling effect)? | An S0 gate: skip practice and extras when class base rate is above a threshold | S0 / G7 / G12 | K31 (contested); d10, d11, d15; human elite K06 (contested) | Same scaffold on three base models; gain vs base pass rate | Gain under 1 point once base pass rate is above 90% on at least two task types | Med |
| E16.10-U7 | Does adaptive per-item budget beat fixed budget in our scaffold? | Difficulty-scaled budget in S0 | G12 | K22 (single-source, c21; consistent with schema) | Fixed samples per item vs budget scaled by class pass rate; accuracy at equal total tokens | Adaptive wins by at least 2 points, or saves 25% tokens at equal accuracy | Med |
| E16.10-U8 | Is weakness-ordered task sequencing better than random for a prompt-only agent? | Sequencing rule for batch runs | memory / S0 | K21, K30 (weight-trained or state-adaptive agents only) | Items ordered by estimated weakness vs random vs easy-to-hard; pass rate on the final third | Weakness order beats random by at least 2 points; easy-to-hard expected to be no better than random | Low |
| E16.10-U9 | Does whole-task self-play beat focused sub-skill drills in the agent loop? | Prefer rollouts or drills in the practice phase | memory | K10 (contested: Charness 2005 vs Southwick 2026, human-only) | Whole-task rollouts vs focused drills at equal tokens; test pass rate | One arm beats the other by at least 2 points on two task types; otherwise no rule | Low |
| E16.10-U10 | Does a stopping rule on practice rounds save tokens without losing accuracy? | Round cap tied to per-round gain | G7 / memory | K27 (plateau in 3 to 6 rounds, other benches) | Fixed 10 rounds vs stop when gain is under noise for 2 rounds; held-out accuracy and tokens | Same accuracy within 1 point with at least 30% fewer tokens | Low |
| E16.10-U11 | Does a scaffold with a sound check lift chess-puzzle accuracy over a plain model? | A chess-puzzle item type as a calibration bench | S0 / bench | K15 (66.5% for a general LLM, older model); K14; K17 | Plain vs scaffold with legal-move check vs scaffold with engine key; puzzle accuracy | Scaffold lifts accuracy by at least 5 points over plain with no loss in legal-move rate | Low |

## Open questions we cannot test on our bench yet

- Southwick 2026 confounds (motivation, prior rating, selection into drills). Needs the full paper and supplement. Until then 3.61x is unadjusted and observational.
- Burgoyne 2016 skill-band effect and the 2018 corrigenda of Macnamara 2014 and Burgoyne 2016 were not retrieved. Unblock: read the corrigenda and the chess-only forest plot. Background only for the agent.
- Concept mining from an engine (Schut-style) for non-chess tasks needs a concept extractor for our item types. Unblock: build a small concept tagger for ARC-like classes.
- Weight-level practice (STaR, SPIN, self-play, DPPO): the agent cannot train, so a test needs a separate fine-tuning track.
- A human-style teacher: a coach model's errors correlate with the agent's (G4). An independent coach (human or tool) is needed for a fair test of U4.
- Tasks with no reliable check cannot show practice effects. Unblock: add verifiable item types.
- ChessQA and ChessGPT scores, and the n=300 vs 600 conflict in the brittleness paper, were not extracted.

## Order to run

1. E16.10-U1 (lesson memory over rounds): cheapest, reuses S9 logs, and shows whether any practice effect exists on our benches and where it plateaus.
2. E16.10-U3 (code verifier by base-rate stratum): the sound-verifier direction is established, so this is a quick check of cost and of the ChessGPT-style harm.
3. E16.10-U2 (targeted vs random vs extra samples): the real DP question at equal tokens; run after U1 so the memory setup is reused.
