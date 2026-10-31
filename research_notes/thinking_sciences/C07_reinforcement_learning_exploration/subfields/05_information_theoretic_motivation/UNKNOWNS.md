# Information-theoretic motivation: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C07.05-U1 | Does EIG probe choice beat extra attempts plus voting on the final answer in open reasoning? | EIG-scored discriminating test as the default in S7 | S7 | K11, K10; single-source, closed-set 20Q only; the one matched-token test voted on questions, not answers | Arms: model-picked probe; EIG (N=12 hypotheses, M=6 probes); same tokens as extra attempts and vote. 60+ ambiguous items (ARC-style, code spec). Metric: final correct rate | EIG beats vote by 4+ points with CI above zero, setup tokens counted | High |
| C07.05-U2 | How many hypotheses and probes are enough, and what does each cost in tokens? | Fixed N and M defaults with a token budget rule | S7 | K26; single-source, one illustrative game, no token curve | N in {5,10,20,40} x M in {3,6,10} on the U1 items. Metric: argmax agreement with N=40 and accuracy per token | Smallest setting with 90%+ argmax agreement and accuracy within 2 points of the best | High |
| C07.05-U3 | Does the consistency filter matter inside our scaffold? | Mandatory filter step before scoring | S7, G2 | K27; established in 20Q (26.8 vs 70.7), not on open items | Same EIG pipeline with filter on vs off, plus prompt-only. U1 items. Metric: final accuracy; share of sampled hypotheses contradicting history | Filter-on beats filter-off by 5+ points | High |
| C07.05-U4 | Does execution-based EIG help code and ARC-style items at equal tokens? | Run sampled candidate programs on a sampled input; pick the input that splits their outputs best | S4, S7 | K28; single-source, oracle answers, no token-matched baseline, gain shrinks for strong models | EIG split vs sampling the same number of extra programs and voting. 48+ code items. Metric: held-out pass rate | EIG beats vote by 3+ points on at least the weaker model | High |
| C07.05-U5 | Does the entropy proxy fail with unequal noise (crashes, flaky tools)? | A per-probe noise estimate and full EIG when tools vary in reliability | S7 | K13; established for constant noise; mixed noise only derived | Items with injected per-tool noise rates. Arms: entropy; full EIG with noise estimate. Metric: final accuracy | Full EIG beats entropy by 3+ points | Med |
| C07.05-U6 | Can a stopping rule on EIG per token save tokens without hurting accuracy? | Stop probing when best EIG per token is below a set value or leader passes a probability | S7, G7, G12 | K29; contested, one threshold in CuriosiTree, theory noiseless only | Fixed 4 probes vs threshold rule (threshold set on a held-out split). Metric: accuracy per token | Same accuracy (within 1 point) with 20%+ fewer probe tokens | Med |
| C07.05-U7 | Does the EIG advantage vanish on soft-target tasks, and can we detect them at runtime? | A softness check that routes soft tasks away from EIG | S0, S7 | K14; BED-LLM film task, size unknown; detector is our proposal | Open-design and preference-like items. Arms: EIG vs prompt-only. Metric: run-checked score (not model opinion, G8). Detector: share of hypotheses with identical predicted answers | Gain near zero on soft items and detector separates the two item types at 80%+ | Med |
| C07.05-U8 | Does a computed option-count hint help open-mode probe choice? | Per-candidate count of distinct possible outcomes shown at S6/S7 open mode | S6, S7 | K18; single-source (Pan et al.), verbal hint only tested, GPT-4o, p=0.304 | Open-mode items. Arms: uncertainty-only; uncertainty plus computed option count. Metric: distinct valid outcomes found per token | 10%+ more valid outcomes at equal tokens | Low |
| C07.05-U9 | Is cheap trace statistics or an empowerment estimate a better per-run failure monitor? | A cheap monitor feeding the S6 impasse detector | G1, S6 | K19, K30; single-source, aggregate correlations only (N=16, N=6), inverts at floor performance | Our own traces. Arms: repeat rate and distinct valid outcomes vs empowerment estimate. Metric: AUC for per-run failure | AUC 0.70+ and beats the plain statistic by 0.05 | Low |
| C07.05-U10 | Does a small model with an EIG selector beat a larger plain model at equal cost? | Route cheap models through the selector | S0, S7 | K16; single-source (Battleship); most of the gain came from move and decision modules | Small plus selector vs large plain at equal dollar cost. U1 items. Metric: final accuracy | Small plus selector at least equal at the same cost | Med |
| C07.05-U11 | Does a goal-stating step before exploratory probes help? | One goal line before open-mode probes | S6 | K21; contested, human-only, N=10, unadjusted p, LLM-labelled; ELLM goal-conditioning null | Open-mode items. Arms: with vs without a one-line stated goal. Metric: valid distinct outcomes, final accuracy | 5+ points gain with CI above zero | Low |
| C07.05-U12 | Do strong models lose the EIG advantage on our items? | A model-strength gate: use EIG only below a pass-rate threshold | S0, G12 | K10, K16, d08; older and weaker models mostly | Run U1 on our strongest and weakest model. Metric: gain by model | Gain at least 3 points larger on the weaker model, so a gate has value | Med |

## Open questions we cannot test on our bench yet

- Human data: Brandle et al. (2023) and Klyubin et al. (2005) were not opened. Opening them would check the human basis for empowerment weights.
- A larger free-play dataset to replicate the goal-statement correlation (needs participants, not a bench).
- Long-context probe selection beyond about 20 turns. We need long transcripts with logged hypothesis sets to see which part fails first (sampling, answer model, history).
- Real tool noise: needs a bench with logged per-tool reliability.
- Per-run failure prediction by empowerment needs a trained estimator and many trajectories per setting.
- Whether questioner and answerer agreement inflates the 20Q gain. Needs a bench with a separate answerer model.
- Whether UoT gaps 33.8, 29.9, 28.3 are relative. Needs the full tables.

## Order to run

1. C07.05-U1 (EIG vs extra attempts plus vote on the final answer): it decides whether the whole line is worth any tokens, and it is the missing comparison in the literature.
2. C07.05-U3 (filter on vs off): cheapest, uses the same pipeline as U1, and the filter is the largest single component (26.8 to 70.7).
3. C07.05-U2 (N and M curve): sets the cost, and the result applies to U4 and U6.
