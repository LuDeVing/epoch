# Industrial fault detection: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E08.10-U1 | Does a computed statistical evidence layer (signed z-scores against matched normal) lift diagnosis for our agent? | Evidence-layer step before the model reads sensor data | S2/O3 | K20; d04, d14; single-source, one 30B model, one real rig | Arms: raw windows vs z-score layer; 100 windows, 5+ classes plus TEP set; top-1 and top-2 | Top-1 gain of 15 points or more on both a real and a TEP set | High |
| E08.10-U2 | Does a code rule or trained selector beat prompt arbitration between tool label and model answer? | Code-side arbiter for tool outputs | O5/G5 | K19, K09; d01, d17; single-source, TEP closed set (oracle 92.76%, prompt 76.1%) | Arms: prompt arbitration vs probability-threshold rule vs small trained selector; 150+ conflict items, 2 datasets; missed corrections, harmful acceptances, accuracy | Accuracy up 3 points or more over prompt arbitration on both datasets, no rise in harmful acceptances | High |
| E08.10-U3 | Does LLM plus detector beat the detector alone at equal tokens on incipient faults (3, 9, 15)? | Detector-plus-LLM as default for diagnosis items | O1/S2 | K01, K07, K21; no equal-token study exists; human-only protocol spread 3-8% vs 97% | Arms: LLM on raw numbers; LLM calling detector; detector alone; faults 3, 9, 15 plus normal; hit rate at 1% FAR | LLM+detector at or above detector alone, and raw-LLM arm below both | High |
| E08.10-U4 | Can an LLM layer cut a noisy detector's false alarms at a fixed hit rate? | LLM false-alarm guard after detector | G | K22; d03; single-source, 25 runs, not at fixed hit rate | Arms: detector alone vs detector plus LLM guard; streaming normal runs plus faults; FAR at fixed hit rate | FAR drops by 30% relative or more with hit rate within 2 points | High |
| E08.10-U5 | How slow is an LLM agent to flag a fault (time-to-flag)? | Time-to-first-correct-flag in harness; routing rule (detector first) | S0/harness | K04, K24; d08, d06, b10; no LLM study; classical delays vary 0 to 819 min | Arms: detector, LLM, combined; streamed TEP with known onset; delay in samples | Add the metric always; add routing rule if combined is no slower than detector | Med |
| E08.10-U6 | Does a candidate-cause list help, and does it hide unknown faults? | Cause list in S2 with an explicit "none of these" slot | S2 | K08; a15, a16; single-source, 11 faults, one run | Arms: list vs open vs list with "other"; 21 faults; top-3 correct and wrong-confident rate | List gains 1+ faults of 11 and "other" slot keeps unknown-fault errors from rising | Med |
| E08.10-U7 | Why do faults 5, 10, 13 fail for every LLM, and does control-loop knowledge fix it? | Control-loop note in the hypothesis table | S2/memory | a15, a16, d11; failure observed in one study, cause untested | Arms: plain vs added control-loop description; faults 5, 10, 13; top-3 | Top-3 correct rises on 2 of 3 faults | Med |
| E08.10-U8 | Does graph retrieval of failure-mode to sensor links help diagnosis from signals (not just QA)? | Retrieval of failure-mode links in S2/S4 | S2/S4/O4 | K11; c11-c13; single-source, text QA only | Arms: direct vs graph retrieval + one call vs full staging; signal items and QA items; accuracy | Gain of 5 points or more on signal items, not only QA | Med |
| E08.10-U9 | Do summary statistics and short windows beat raw series as model input? | Input hygiene rule: summarise, then show | S1 | c16, d09; single-source each, simulated HVAC and synthetic series | Arms: raw vs summary stats vs image of series; 3 window sizes; F1 and FAR | Summary arm beats raw by 5 points or more with equal or lower FAR | Med |
| E08.10-U10 | More reasoning effort versus one extra verifying tool call at equal cost | Rule on where to spend budget for integration items | G11/O4 | K26; d02, d08; contested (+5.2 unaided, +2.2 integrated with interval including 0) | Arms: high effort vs low effort plus one tool call; hard conflict items; accuracy at equal tokens | Extra tool call wins by 2 points or more, or the two tie at lower cost | Med |
| E08.10-U11 | Does accuracy drift over repeated fault cycles, and does a memory reset help? | Reset operator between cycles | memory | K13; c16, d16 (second-hand); single-source, two models | Arms: carry history vs reset every cycle; 10 cycles; accuracy per cycle | Reset arm holds accuracy while carry arm drops 5 points or more | Low |
| E08.10-U12 | Does the agent flip its answer under small sensor perturbation? | Robustness check (perturb and compare) as a verify step | G/S8 | K15; a13, b16; neural classifiers only, not LLMs | Arms: plain vs summary-stats input; add noise at 3 levels; answer flip rate | Flip rate under 10% at the noise level of normal sensor drift | Low |
| E08.10-U13 | Do soundness-deliberation and a state tracker raise interactive diagnosis? | State tracker line in S6 and a soundness check | O2/S3 | K12; c14, c15; single-source, one simulator | Arms: plain loop vs state tracker vs soundness loop; interactive fault items; turns to correct diagnosis | Turns fall by 15% or more with no accuracy loss | Low |

## Open questions we cannot test on our bench yet

- **Real plant data.** Nearly every result is on simulated TEP. Unblock: obtain one real series (PRONTO, pilot-plant distillation data or a bearing set) with labelled onset.
- **A fixed TEP protocol.** No shared window, split or threshold across LLM studies. Unblock: freeze one protocol in our harness and publish it with the results.
- **Trained selector data.** U2 needs labelled conflict cases. Unblock: log tool-versus-model conflicts from U1 and U3 runs.
- **Chain of Physics knowledge graph.** Needs asset documents and a built graph. Unblock: build a small failure-mode to sensor graph from public ISO-style material.
- **Controlled latency and token accounting.** Needs an equal-token meter that counts detector compute as well as LLM tokens. Unblock: add a cost field to the harness.
- **Unknown-fault handling.** All LLM studies use closed fault lists. Unblock: add held-out fault classes in the bench.
- **Cause of the Gao 2024 FENet 79.05 vs 85.73% mismatch.** Matters only if we reuse their protocol; resolve by rerunning their code.

## Order to run

1. **E08.10-U3** (detector plus LLM versus detector alone at equal tokens): it answers the biggest gap, sets our protocol and gives the baselines everything else needs.
2. **E08.10-U2** (code arbiter versus prompt arbiter): cheap, uses logged U3 conflicts, and tests the most robust finding (LLM under-corrects tools).
3. **E08.10-U1** (statistical evidence layer): largest effect seen in any study (about +45 points on one dataset) and easy to build once the detector exists.
