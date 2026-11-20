# TRIZ with systematic design: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E07.05-U1 | Does naming a contradiction (and one code-picked principle) before ideation raise blind-rated novelty of a current model? | Contradiction-then-lookup reframe as a typed O8 | O8/O4 | K21, d05: single-source, N=1 chair; human studies contested (K03) | A plain "improve X" vs B named contradiction plus principle vs C contradiction only; 20 post-cutoff design problems, 5 samples each; blind novelty by 2 raters, kappa, tokens per novel idea | B beats A on novelty by 0.5 points on a 7-point scale or more, on at least 2 of 3 problem families, kappa 0.6 or more, no loss in feasible count over 15% | High |
| E07.05-U2 | Does a task re-questioning step before decomposition find the hidden need? | A short task-questioning pass at S1 before O3 | S1/O8 | K01, b07: single-source industrial case, no control | A decomposition alone vs B plus re-questioning; 30 briefs with a hidden need; blind fit-to-need score; share of runs that change the task | B wins on 2 of 3 families by 10 points of fit rate; no loss on routine briefs | High |
| E07.05-U3 | Does a none-found exit plus an independent checker cut false contradiction claims? | Exit and checker inside the contradiction slot only (final answer still never abstains, G6) | G1/G6 scope note, O8 | K13, K24, d09, d08: single-source, labels doubtful (86 of 100 is an upper bound) | A one-pass naming vs B with none-found exit vs C B plus checker without authorship; 50 conflict items and 50 none; false-positive rate, detection F1, pair accuracy | False positives fall 20 points or more and detection F1 drops under 0.05 | High |
| E07.05-U4 | Is a code-fixed lookup as good as, or better than, free LLM choice or rerank, for principle choice and the final idea? | Code lookup only; drop LLM free choice | O8, memory | K12, b16, d11: single benchmark, non-LLM within 0.02-0.03 of best LLM | A matrix lookup vs B TF-IDF vs C LLM free vs D lookup plus rerank; TRIZBench cases plus 20 own problems; Hit@3 and blind novelty of the resulting ideas | D beats A by 0.05 Hit@3 or 0.3 novelty points, otherwise keep A | Med |
| E07.05-U5 | Does frequency over 5-10 namings gate when to fire the reframe? | Entropy gate: fire O8 only if naming entropy is low, else broaden | G1/G4, S6 | b12, c02: single-source, 10 cases, G4 says samples correlated | 100 repeated namings on 10 cases; compare gate on vs off; match to labelled pair, final blind rating | Entropy predicts match with AUC 0.7 or more and gate improves final rating | Med |
| E07.05-U6 | Does a Problem-Solution Network (how-to tree with code validator) beat plain decomposition? | PSN as the decomposition form with a validator | S2/O3 | K20, a04: no test of any kind | A O3 plain vs B PSN with six-rule validator; 20 decomposition-hard problems; solved rate, blind novelty, tokens | B beats A on solved rate by 8 points or more at equal tokens on 2 of 3 families | Med |
| E07.05-U7 | Does problem typing (SM/PP/HE) route to better reframes than an untyped reframe? | Typed routing table into O8 | S0/O8 | a02, a05, d06, K22: no ablation anywhere | A untyped reframe vs B typed routing; 30 mixed problems; blind novelty and tool-fit | B beats A by 0.3 novelty points or 8 points of solved rate | Med |
| E07.05-U8 | Does the order matter: working principle before contradiction, or after? | Enforce the winning order | S1 | K02, a03: authors' argument for humans only | Same items as U1; A principle first vs B contradiction first; validity of ideas, wasted calls | Order A cuts invalid ideas by 15% or more | Low |
| E07.05-U9 | Does TRIZ cut idea count and what is the token cost per novel idea? | Run TRIZ ops only where cost per novel idea is lower than plain sampling | G7, G12 | K25, K26, d04, b01: contested in humans, 150k-250k tokens per multi-agent run | A plain best-of-N vs B TRIZ chain at same tokens; fluency, variety, novelty scored separately | B has a lower token cost per blind-rated novel idea by 20% or more | High |
| E07.05-U10 | Is any LLM TRIZ gain still there on post-cutoff problems? | Permission to trust U1 results | bench rule | K27, a15, d17: 0.691 to 0.544 drop is across different collections; no study with kappa | Same arms on textbook set vs post-cutoff set; gain per set | Gain on post-cutoff is at least half of gain on textbook set | High |
| E07.05-U11 | Does manager-plus-specialist TRIZ beat a single chain at matched budget? | Nothing expected; confirms G9 | G9/S5 | K16, c15-c17: no control exists | A single chain vs B multi-role, matched tokens, 10 cases; novelty, role coverage | B beats A on novelty by 0.5 points; otherwise keep G9 | Low |
| E07.05-U12 | Do concrete principle wordings beat abstract ones? | Concrete principle text in the lookup table | O8, memory | b24: snippet only, unverified | A abstract vs B concrete sub-principle wording; 20 problems; idea count and novelty | B gains 20% ideas or 0.3 novelty at equal tokens | Low |
| E07.05-U13 | Does remembering which principle worked on which problem class help later runs? | Principle-by-class store | memory | None; no source | Run 50 problems twice, arm with store vs without, same budget; solved rate on held-out problems of the same class | Store arm gains 5 points or more on the second pass | Low |

## Open questions we cannot test on our bench yet

- **Human FDM creativity gap.** Nobody measured it. We can test an agent analogue (U2) but not claim anything about human designers. Needs a study with human designers and a control.
- **Cok 2026 cell means and per-cell n.** Not read. Unblock by getting the full paper or tables; would show if the wind turbine gain is skill or problem.
- **Fiorineschi 2018 reviews (Computers in Industry, J Eng Des).** Paywalled; counts of 10 proposals and 5 issues are second-hand. Unblock by institutional access.
- **Why human quantity effects disagree.** Needs the originals of Dumas 2016, Chang 2016, Valentine 2017, Belski 2014/2015. Not reachable this run.
- **Independent raters with kappa on a labelled idea set.** We have no rated post-cutoff design set. Building it (U1, U10) unblocks most of the table.
- **Best principle labels.** TRIZBench labels are inventors' choices. Needs expert re-labelling to say whether lookup truly equals free choice.
- **Hernandez per-site sample sizes.** PDF table order garbled; needs the journal version.
- **Transfer from textbook to real tasks.** No source tests LLM TRIZ on live engineering problems with outcomes.

## Order to run

1. **U1 (contradiction-named reframe vs plain, blind novelty, equal tokens).** It is the central unproven claim and decides whether any TRIZ step enters the schema.
2. **U3 (none-found exit plus checker).** Cheap, uses existing items, and the known failure (over-detection) would otherwise make O8 fire on every problem.
3. **U9 with U10 (tokens per novel idea, post-cutoff).** G7 requires proof of payoff, and without a cost figure and a leakage check, U1 cannot be trusted.
