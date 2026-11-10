# Belief updating: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E03.07-U1 | Does an explicit evidence ledger (new items, direction, diagnosticity, then move) beat plain CoT? | Ledger as the body of S5 on evidence-driven items | S5 | K01, K29; a17, c02, b08; no direct study (single-source, older models only) | Pastcasting set, 3-5 evidence batches per item; plain CoT vs ledger; Brier of final forecast, paired bootstrap, 150+ items | Brier lower by 0.005 or more, 95% interval excludes 0, and no loss on easy items | High |
| E03.07-U2 | Does a "new evidence?" gate stop empty-pushback flips without hurting real retraction? | Gate rule in S5: change only if code finds a new item | S5 / G | K12, K23, K25; c17, d01, d03, a19 (established for flips; retraction side single-source) | Mixed set: half "are you sure?" with no evidence, half real defeaters (Belief-R style); plain vs gate; report hold rate and update rate | Hold rate up 15 points or more and update accuracy down 5 points or less | High |
| E03.07-U3 | Does a code-kept posterior table fix the stall after round 1? | Posterior bookkeeping in code, shown to the model each round | S5 / memory | K07, K08, K10; a17, c02, b08 (single-source, non-reasoning models) | 5-round preference task (Qiu-style); plain vs CoT vs code table; accuracy by round 2-5 | Round-5 accuracy up 10 points or more over plain, and CoT does not match it | High |
| E03.07-U4 | Does a code or calculator step for posterior arithmetic help on realistic forecasts? | Python step in S5 for odds and LR arithmetic | S5 / tools | K10, K28; b08, d07 (single-source; Python never ablated alone) | Same items as U1; ledger without code vs ledger with code; Brier and arithmetic error vs Bayes | Brier lower by 0.003 or more, or arithmetic error cut by half, at no more tokens | Med |
| E03.07-U5 | Does Platt extremising stack with an in-scaffold rule or replace it? | Platt in code as a fixed final step | S5 / G5 | K14, K15; b19, c11, d12 (hedging is established; stacking untested) | Plain vs Platt vs ledger vs ledger plus Platt; Brier; fit Platt on held-out half | Platt lowers Brier by 0.005 or more on held-out items and does not hurt calibration error | High |
| E03.07-U6 | Is a step-size cap or damping good or bad for an LLM? | A rule on maximum move per evidence item | S5 | K01, K03; a05, a01, b12 (human-only; contested for LLMs) | Same items; no cap vs cap at 0.2 vs inverse cap (floor); Brier, mean abs update | Cap lowers Brier by 0.005 or more without raising error on items where the crowd is near 0 or 1 | Med |
| E03.07-U7 | What step size and confirmation rate does a frontier LLM show, and does skill track small steps? | A logged step-size band used as an audit flag, not a rule | S5 / logging | K29, K01, K02; a01, a03, d17 (no LLM data) | Log step size and confirmation on U1 streams; correlate with per-item Brier and with first-forecast Brier | Correlation of small steps with better first forecast, abs(r) 0.2 or more on 150+ items | Med |
| E03.07-U8 | Does a two-gate update (is it new?, then size) beat one-step update? | Two-gate S5 | S5 | K22; a25, a07 (human-only, contested vs Fildes) | One-step vs two-gate on U1 items; Brier, confirmation rate | Brier lower by 0.003 or more and confirmation rate under 25% | Med |
| E03.07-U9 | Does base-rate-first (not "think Bayesian") help? | Base-rate-first opening in S3 for forecasting items | S3 / S5 | K16; c06, c07 (single-source, small gain, not in primary analysis) | Plain vs base-rate-first vs "think Bayesian"; Brier on 100+ items | Base-rate-first beats plain by 0.003 or more and "think Bayesian" does not | Low |
| E03.07-U10 | Does shuffling evidence order change the answer, and does the ledger reduce that? | Order-invariance audit: run in two orders, flag disagreement | S5 | K24; d04, d05 (single-source, knowledge-conflict tasks) | 3 random orders per item; plain vs ledger; variance of final forecast across orders | Ledger cuts order variance 30% or more | Med |
| E03.07-U11 | Do blends with an outside estimate beat the model's own move? | Fixed-weight blend when a reference estimate exists | S5 / O | K13; a15, b15 (single-source, small set, N=31 questions) | Own update vs 50/50 average vs weight w tuned on a held-out half; Brier | Blend beats own update by 0.005 or more on held-out items | Low |
| E03.07-U12 | Does an outcome-free audit (martingale, expected-evidence, excess volatility) detect bad updating? | Audit flag in logging; later a trigger for S6 | S5 / logging | K17, K26; a20, d09, a24 (synthetic or weak) | Run audits on U1 streams; correlate flags with Brier | Audit score correlates with Brier at abs(r) 0.4 or more on 150+ items | Low |
| E03.07-U13 | Do reasoning models (extended thinking) still stall or fail to retract? | Nothing; sets whether U2, U3 are needed | S5 | K07, K11; d13, d14 (older models only) | Run T3 and T4 on a reasoning-mode model vs a non-reasoning one | Needed only if the reasoning model stalls (round-5 gain under 5 points) | High |
| E03.07-U14 | Does class-weighted scoring or an ask-both-ways complement check remove low-probability bias? | Complement check as a cheap probability audit | S5 / eval | K27; d11, d12 (single-source) | Basic vs complement check on skewed items; class-weighted Brier | Weighted Brier lower by 0.005 or more | Low |

## Open questions we cannot test on our bench yet

- **A reproduction of the Atanasov pattern.** We have no tournament data. Unblock: get public Good Judgment Open or IARPA forecast streams (K29, gap 8).
- **Human baseline for our own items.** Without a human or crowd forecast per question we cannot test blending (U11) or compare to superforecasters. Unblock: pastcasting questions that carry a market or crowd price.
- **Training-versus-marker question.** The IRT reanalysis says training effects may be smaller than reported. We cannot run human training. Unblock: only a literature check of the full reanalysis (publisher page was blocked).
- **Fine-tuning.** Bayesian teaching and Brier-reward RL work in papers but a scaffold cannot copy them. Unblock: none unless we allow training.
- **Motivated updating on our agent's own earlier answer.** No design yet for a robot-style placebo. Unblock: build the item pair (same evidence about own answer vs another agent's answer).
- **Primary sources behind the founding numbers.** Phillips and Edwards (1966) and Edwards (1968) were seen only via Benjamin; Tetlock (2005) figures are from memory. Unblock: open the originals.
- **Shapira 2026 model names.** Unverified. Unblock: open the paper and check the models used.

## Order to run

1. **U13 plus U3 (reasoning model on the Qiu-style task).** Cheap, and it decides whether U2 and U3 are worth building at all.
2. **U2 (new-evidence gate on mixed pushback and defeater items).** The only established failure (flips) meets the only single-source failure (no retraction); it tests both sides together, which no paper does.
3. **U1 with U5 (ledger vs plain, and Platt stacking).** Same item set and logs give U7 and U10 data for free; Platt is the cheapest known gain.
