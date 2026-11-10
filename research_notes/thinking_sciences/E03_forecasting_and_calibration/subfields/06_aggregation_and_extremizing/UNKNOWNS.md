# Aggregation and extremizing: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E03.06-U1 | Does a fitted, capped push on the pooled logit of K same-model samples beat the plain mean? | Push step with a fitted slope and CI gate | G4, O (aggregate) | K09, K17, K27; contested; AIA -5.6% (d11) vs BLF no resolved gain (d15) | Arms: N=5 mean vs N=5 mean + push fitted on a held-out half. 300+ resolved binary questions; Brier, bootstrap CI | Brier gain of at least 0.003, CI excludes 0, on 2 backbones | High |
| E03.06-U2 | Push vs more samples vs one careful pass at the same tokens | Choose the cheapest of the three as default | G7, G11 | K17 single-source; d18 (trained single beat median-5); no token-matched test exists | Arms: push on N=5; N=10 no push; one long pass. Same items; Brier at matched tokens | Push arm beats both others by at least 0.002 | High |
| E03.06-U3 | What is the error correlation between samples of one model, and what changes it (temperature, prompt variant, retrieval)? | A measured overlap number to set push size; a rule for which diversity knob to turn | G4, S3 | K21; between-model r = 0.943 (d17); within-model unmeasured; human-only theory | Same questions; K=5 samples under temperature 0.3/1.0, 3 prompt variants, 3 retrieval variants; mean pairwise residual correlation | A knob lowers correlation by at least 0.2 and that lowers Brier | High |
| E03.06-U4 | Does evidence-diverse sampling (different retrieved sources per sample) make a push useful? | Sample by evidence, then push by overlap | S3, G4 | b07 coin example; a05; d16 (decorrelated members help); no LLM test; human-theory | Arms: K shared-retrieval vs K diverse-retrieval, each with fitted push vs none; Brier, fitted slope | Slope CI above 1 only in diverse arm and Brier gain at least 0.003 | High |
| E03.06-U5 | Is there an online detector (overlap of retrieved documents, sample dispersion) that sets push size or flips it below 1? | Detector-gated push | G4, S0 | K24; none found; BLF dispersion shrinkage never chosen (d14); anti-extremizing 18%-73% (d09, abstract only) | Compute overlap per question; bin by overlap; fit slope per bin on held-out half | Slope differs between low and high overlap bins by at least 0.3 and gate beats fixed push | Med |
| E03.06-U6 | Does yes bias or hedging change the sign of the right push, and does intercept + slope fix it? | Joint intercept and slope fit | G4 | K25; human data only (d04); LLM claims conflict (d13 vs c03, b16, b15) | Arms: mean; slope only; slope + intercept. Include sets with low and high base rate | Joint fit beats slope-only by at least 0.002 on the biased subset | High |
| E03.06-U7 | Does a push help or hurt in the tails (pooled p under 0.1 or over 0.9)? | Tail rule: clip or skip push | G4 | K13; Halawi tails accuracy up, Brier worse (b08); AIA gain tiny near 0/1 (d11) | Items binned by pooled p; push vs none per bin; Brier and log loss | Push loses in tail bins: add skip rule. Push wins there: relax clip | Med |
| E03.06-U8 | Does the agentic supervisor (search to resolve disagreement) beat the mean at equal tokens? | Supervisor at S7 for forecasts | S7, O | K07 contested; AIA 0.1125 vs 0.1199 none (d12); BLF merge worse (d14) | Arms: mean of 5; supervisor with search over the same 5 | Brier gain of at least 0.004 vs mean and not larger than extra tokens would buy | Med |
| E03.06-U9 | Is a mixed-backbone pool better than a same-model pool? | Mix backbones when budget allows | S3, memory | K21; d16 single-source; ForecastBench ensemble lost to best single (a26); Schoenegger median lost to GPT-4 (c02) | Arms: 5 samples one backbone; 5 across 2-3 backbones; best single | Mixed pool beats best single by at least 0.003 | Med |
| E03.06-U10 | Does blending with an external anchor (crowd, market, retrieved base rate) beat the agent alone, and at what weight? | Anchor blend with fitted weight | S7, memory | K12 established in LLM papers (a25, c04); weight 4x is single-source; our items may lack a crowd | Arms: agent; anchor; blend weights 1:1, 1:4; prose self-update | Blend beats both singles, numeric blend beats prose update | Med |
| E03.06-U11 | Can a class record (fitted slope and bias per problem class and backbone) be learned from few resolved items? | Class record read at S0 | memory | a20 (online weights low regret); d15 (record-level LOO may be optimistic); [D] design | Rolling fit on first 50, 100, 200 resolved items; score on the next 100 | 100-item fit holds out-of-sample gain at least 0.002 and CI excludes slope 1 | Low |
| E03.06-U12 | Does a consistency check across related questions flag bad pools before pooling? | Consistency gate | S4 | a29 (violations track Brier); no extremizing link | Compute violation score per forecast set; correlate with Brier; gate: drop or widen | Score rank-correlates with Brier at 0.3 or more and gating lowers Brier | Low |
| E03.06-U13 | Does log-odds pooling beat probability pooling for LLM samples when samples are extreme? | Default log-odds pool | O (pool) | d05, b10, d14 point yes, but gains tiny and logit numbers only in a figure | Arms: mean prob vs mean logit; items with pooled p in tails | Logit better by at least 0.001 overall and robust to one failed sample | Low |

## Open questions we cannot test on our bench yet

- **No resolved-question set with enough items.** E1-E4 need about 300 resolved binary questions after the model cutoff. Unblock: a post-cutoff set, or ForecastBench-style questions resolved over time.
- **No crowd or market values for our items.** U10 needs an external anchor. Unblock: items drawn from markets that publish prices.
- **Within-model error correlation by sampling setting.** No source measured it; needs the data from U3.
- **Mellers et al. 2014 team-size breakdown and the Satopaa 2014 IJF numbers.** Not opened; need a library PDF.
- **Palley-Soll behaviour near 0/1 and Sevilla's formula.** Snippet only or not found.
- **Replication of AIA on ForecastBench or Prophet Arena.** Needs the AIA pipeline or the BLF code; only partial check exists.
- **Horizon dependence.** BIN says bias correction matters at long horizons and information fusion at short ones; our items may lack horizon labels.
- **Search quality as a driver.** Whether better retrieval changes the optimal push has no data.

## Order to run

1. **U3 (error correlation by setting).** Cheapest: no outcomes needed for the correlation, and the answer sizes every other test (low correlation justifies a push; high says hold).
2. **U1 plus U2 (fitted push vs more samples at equal tokens).** The core G4 question; nobody has run it, and AIA and BLF disagree.
3. **U6 (intercept and slope together).** Quick add-on to the same data; guards against pushing the wrong way under yes bias or hedging, which would otherwise ruin U1.
