# Stage model and incubation: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A12.08-U1 | Does a context reset at impasse (task only, failed text dropped) beat one continuous pass on insight items? | Reset step in S6 | S6, O6 | K22, K12; d01 (MATH, 2 small models: continue won 9 of 9); older models only | A: one long pass. B: short pass, S6 fires, fresh context, remaining tokens. 60+ code-checked riddle and insight items, plain pass rate 10-60%. Metric: paired pass rate | B beats A by 5 points or more, with paired CI above 0, on 2 models | High |
| A12.08-U2 | Does showing a one-line failure log after the reset beat a blank restart? | Failure log shown on return | memory, S5 | K05 contested; b15 (human, UUT), d07 and d08 partial | A: reset blank. B: reset plus failure log. Same items as U1, same tokens. Metric: pass rate, fixation rate (same wrong answer repeated) | B beats A by 3 points and repeat-wrong rate falls by 20% relative | Med |
| A12.08-U3 | Does a reconsideration cue gated by entropy or a failed check beat one longer pass? | Gated cue as an S6 trigger | G1, G11 | K15 contested; b26 (+8.41pp, no token match, 1.5B to 8B); Llama -4.19pp on a subset | A: one pass at 2x length. B: pass, gated cue, same total. Math and puzzle items, models with logit access. Metric: pass rate, tokens per solved item | B beats A by 3 points at matched tokens on 2 or more models, and does not lose on any | High |
| A12.08-U4 | Does a literal-reading check by code cut false reframes? | Literal-answer check in O8 and O6 | G3, O8 | K24 single-source; d14 (84.9% vs 50.7%) non-thinking mode | A: reframe step. B: reframe plus candidate answer must also be tested under the literal reading. Items: riddle-like with literal answers plus true riddles. Metric: accuracy on both types | Literal-item accuracy up 10 points with no more than 2 points lost on true riddles | Med |
| A12.08-U5 | Does our stuck detector predict failure within a problem, not just across problems? | Detector kept as S6 trigger | S6 | K23 single-source; d02 (within-problem AUROC 0.496) | Score detector within problem vs a question-only difficulty baseline on 200+ items with 8 samples each | Within-problem AUROC at least 0.60 and above baseline by 0.05 | High |
| A12.08-U6 | Is code or independent-sample verification better than model self-verification on riddle items? | Verify state that never uses self-endorsement for riddles | G3, G4, S8 | K17 established that self-verification fails; no equal-token comparison (gap 10); c09 5-39% failures | A: model picks among its own candidates. B: code check or independent sample picks. NazoNazo-style items. Metric: verification-failure rate (right candidate written, wrong one chosen) | B cuts failures by 25% relative at equal tokens | High |
| A12.08-U7 | Does resurfacing the cue of unsolved items from a log later in a session raise solving? | Resurface step | memory | K09, K26 contested; one lab dz = 0.47; Beijamini null; human only | A: leave unsolved items. B: re-present short item tag at a later turn. Multi-item sessions, within-model. Metric: solve rate cued vs uncued | Cued beats uncued by 5 points on 2 models | Low |
| A12.08-U8 | Is sleep-time pre-computation worth it when queries about one stored context repeat? | Offline pre-read step for stored contexts | memory | K16 contested; c15 up to +13% and +18%; d06 baseline gave none on tool agents | A: answer cold. B: pre-compute on the context, then answer. Repeated queries on one document. Metric: accuracy and total tokens per query including pre-computation | Total cost per query falls 20% at equal or better accuracy, over 5+ queries per context | Low |
| A12.08-U9 | Do aha-style markers in a trace carry any signal once defined by output change? | None (it would justify a trace-based trigger, which G10 forbids) | G10 | K14 contested; d'Aliberti 6.31% shifts, 2.57% vs 16.44%; Yang 2025 marker-based, no effect size | Label shifts by a change in the extracted answer between early and final. Compare accuracy of shifted vs unshifted traces within problem, 3 models. Metric: within-problem accuracy difference | Shifted traces beat unshifted by 5 points within problem. Otherwise keep G10 as written | Low |
| A12.08-U10 | Does a longer first attempt before the reset make the later reset pay more (preparation length effect)? | Minimum first-attempt budget before S6 reset | S6 | K03 single-source; b04 correlated moderators | Vary first-attempt token share (20%, 50%, 80%) before the reset in U1's design. Metric: pass rate by share | Pass rate differs by 5 points across shares with a monotone trend on 2 models | Low |
| A12.08-U11 | Does a lower pass rate on repeated exposure (Baird) show up in agents: does a prior failed attempt help a later one? | Stored failed-attempt summaries per item | memory | K05 contested; d07 partial; humans, divergent tasks | A: fresh attempt, no history. B: attempt with stored failure summary from a previous session. Items seen before vs new. Metric: pass rate | Seen-item gain exceeds new-item gain by 5 points | Med |

## Open questions we cannot test on our bench yet

- Sleep and its stages. No agent analogue; Lacaux (N1) and Lowe (N2) conflict and the stage groups are not randomised. Unblocked only by a larger randomised human study, which does not change the schema.
- The unconscious thought effect on insight tasks (not decisions). No replication on insight items was found. Would need human data.
- Segal 2004 sample sizes and effect sizes, and the Weisberg 2015 and Bowden 2005 null results. Would need the original papers.
- The 2021 follow-up on cueing with fixating information (HTTP 403). Needs the full text.
- Does d'Aliberti's second-pass gain hold for frontier reasoning models? The paper only ran 1.5B to 8B models and had no equal-token baseline. Unblocked by our own run of U3 on frontier models.
- Sleep-time compute predictability threshold. No threshold in Lin and Snell; needs a predictability score of our own question sets.
- Contamination of insight benchmarks. Needs post-cutoff or self-written items before any result is trusted.
- Cognitive-model fits (CLARION). Not read; the press numbers 35.3% and 45.3% are unverified.

## Order to run

1. **A12.08-U1 (reset vs one pass).** It is the only break-like operator that maps to an agent, it is cheap to run, and the prior (d01) says it will fail, so a quick result protects the 4b rule.
2. **A12.08-U6 (code or independent verification vs self-verification).** The strongest established weakness of models on insight items is verification, and a fix would fit existing guardrails G3 and G4.
3. **A12.08-U5 (within-problem stuck detector check).** Every reset or reconsideration step depends on the S6 trigger, and d02 shows such detectors often read only difficulty.
