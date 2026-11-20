# Retrieval and ensembles for LLM forecasts: deep document

*Subfield E03.09. Sources: evidence_a-d.jsonl (a01-a26, b01-b28, c01-c25, d01-d21), claims.jsonl (K01-K21), critique.md. Brier scores: lower is better. Brier Index (BI) in BLF: higher is better. Question sets differ between papers, so absolute Brier is never comparable across papers (a26).*

## 1. What it is

An LLM forecasting agent has three levers that sit outside the model weights:

1. **Retrieval.** Search news or the web, filter, summarise, and put the result in the prompt. Fixed pipeline or agentic (ReAct) search.
2. **Ensembling.** Run the same pipeline N times, or run different models or prompts, and combine the numbers (mean, median, trimmed mean, log-odds mean, or an LLM that reads the runs).
3. **Crowd adjustment.** Show the model, or blend in code, the market price or community forecast.

These map to schema state S3 (generate independent attempts, combine in code). The question here: how much does each lever add, when, and what goes wrong.

The headline answer from 2024-2026 evidence:

- Averaging runs of one pipeline gains little: about 0.003 to 0.005 Brier. Mean, median and trimmed mean are equal.
- Mixing different models or prompts gains more, but only when their errors are decorrelated.
- Retrieval helps a plain model by about 0.02 Brier, helps a strong agent by about 0.009, and can hurt (inflated means, fake articles, leakage).
- Crowd price is worth 0.010 to 0.013 for a strong agent. The price alone is very hard to beat.
- Nobody has compared averaging against one longer run at equal tokens.

## 2. History and theories in depth

**Founding (2022).** Zou et al. (b26) built Autocast: pre-LLM retrieval models (T5, FiD with temporal news) got 65.4% true/false accuracy vs 92.4% for the human crowd. Retrieval helped; models were far below the crowd.

**Wisdom of the silicon crowd (2024).** Schoenegger et al. (a06, a07, a08) took the wisdom-of-crowds idea to LLMs: the median of 12 different LLMs, no retrieval, on 31 Metaculus questions had Brier .20 vs .19 for 925 humans (p=.85, equivalence within 0.081). The best single model (GPT-4, .15) beat the ensemble. LLMs said Yes too often (mean 57% while 14 of 31 resolved Yes). This is the human-forecasting theory (independent errors cancel) applied to models.

**Retrieval plus ensemble (2024).** Halawi et al. (a01-a05) built the template: query generation, news retrieval, relevance rating, summaries, fine-tuned reasoner, 6-forecast ensemble. Test Brier .179 vs crowd .149 on 914 questions (5 platforms). Retrieval worth about .02, fine-tuning .003-.007, ensemble about .003. The system beat the crowd only when the crowd was unsure, retrieval was early, and at least 5 relevant articles were found.

**Benchmarks and contrary results (2024-2025).** ForecastBench (a09, a10, b10): news retrieval did not help in the tested setup; the best LLMs used the market price ("freeze value"). Pratt et al. (a16): on a small company dataset a plain prompt beat every strategy including news retrieval. Hsieh et al. (c13): ensembling helps a ReAct agent but hurt base GPT-4o (.218 vs .210).

**Pastcasting and leakage (2025-2026).** Bench to the Future (a13, a14, c12) built a frozen corpus to fix backtest leakage. Paleka et al. (a17, c10) and El Lahib et al. (c11, d20) showed date-filtered search leaks: leak pages for 71% (Google) and 81% (DuckDuckGo) of questions; Brier .108 with leaks vs .242 without.

**Live tournaments (2024-2026).** Metaculus AI benchmarks (a22, b15-b18): pros beat bot teams by 8.9, 11.3, 17.7 and 20.0 points (Q4 2024 to Q2 2025); by spring 2026 the gap was 1.25 and not significant. Winners ensemble (86%), use more calls (28 vs 7), and search.

**Aggregation theory (2025-2026).** AIA Forecaster (d07-d10): mean of 10 runs beats a single run (.1140 vs .1182); an LLM supervisor that only rewrites is worse; an agentic supervisor that searches is best (.1125); Platt scaling and extremizing fix hedging. BLF (d01-d06): same pattern; plain mean beat the LLM aggregator; belief state cuts cross-trial SD from .094 to .030. Diversity papers (d11-d13, c14, c15): gains depend on decorrelation.

**Failure theory (2026).** Retrieval is an attack surface and a bias source (a19-a21, c17, c18, d16, d17): more documents push the mean up; fake articles flip 56-82% of forecasts; defenses have bypasses.

**Crowd adjustment (2024-2026).** Halawi (a05) found 4x weight on the crowd best (.149 to .146). Schoenegger (b09) found simple 50/50 averaging beats letting the model update toward the crowd. FRI's post (b13, b14) credits Cassi's "crowd adjustment" with nearly 0.01, but BLF (d02) puts Cassi's market gain over the plain price at +0.6 index points, not significant.

**Competing explanations.**
- Variance story: ensembles help by cutting run noise (a13). Predicts gains when run SD is large.
- Bias story: retrieval or training bias is shared by all runs, so averaging cannot fix it (c07, d16). Predicts small gains for same-model copies.
- Correlation story: gain is set by how decorrelated members are (d11-d13). Predicts mixed models win.
- Anchor story: the price carries most of the information; agents mostly add small adjustments (d02, d09).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Averaging 6 runs of one pipeline gains little | Validation Brier: mean .1656, median .1651, geometric .1655, trimmed .1649, single run (avg) .1676, crowd .1600; gain about .0027 | Halawi a03, b04, c04 | Established (K01) |
| 10-run mean vs single, 1,610 questions | single .1182; mean .1140; trimmed .1142; median .1138; most gain by 5 runs, small gain to 15 | AIA d07 | Established |
| 5-sample average, weak base model | Brier 23.47 to 23.07 (0.004) at about 5x tokens | CHAIN d14 | Single-source |
| 4 mixed frontier runs vs 1 | .130 to .125 (about .005) on 1,367 questions; mixes models | FutureSearch d15 | Single-source (blog) |
| LLM re-reading of runs is worse than mean | USC .1691 vs mean .1656 (Halawi); non-agentic supervisor .1168 vs mean .1140 (AIA); agentic supervisor .1125 | a03, d08, d03 | Established (K20) |
| Run noise is large | single runs swing under 20% to over 80%; mean of 5 cuts SD by about two thirds; about 60% of variance in final judgment | FutureSearch a13, b19 | Single-source (18 questions, one model) |
| Reasoning model still noisy | market-question cross-trial SD .094 (Pro), .105 (Flash); .030 and .032 with belief state | BLF d04 | Single-source |
| Averaging can hurt a weak base model | GPT-4o base: ensemble .218 vs single .210; ReAct ensemble .169-.170 vs .180 | Hsieh c13 | Contested (K04) |
| Mixed ensemble can be worse than best member | 9-forecast ensemble .194 vs best single .178 (Claude 3.5 Sonnet); LLM crowd of 12 .20 vs GPT-4 alone .15 | b11, a06 | Established |
| Diversity beats copies at fixed samples | best 5-call team: FT 2, Gemini 1, GPT-5 1, Grok 1; never all one model; Grok 4 replaceability 1.7 bp vs under 0.1 for GPT-5 and Gemini | Aitchison d11, a25 | Established with 3 others (K03) |
| Highly correlated models add nothing | 7 models, mean pairwise correlation .943; ensemble gain .0047, none significant after Holm | SoccerArena d13 | Single-source, sports |
| Pairs of weak models match the best | linear pool of 2 matches or beats best single in 11 of 16 groups; within 5% in all 16; flat past 3 | Peng d12 | Single-source |
| Cluster-selected 3-model crowd beats 25-vote | .302 vs .296 (FutureX-Past); 88% fewer calls; random 3 matches in 1 draw in 8 | Chetlapalli c15 | Single-source |
| Deliberation helps only with mixed models | log loss diverse+shared .501 to .481 (p=.017); homogeneous +.008 to +.020 (worse) | Schneider c14 | Single-source |
| Retrieval helps a base model | base GPT-4: no retrieval .206 vs retrieval .186 (about .02); fine-tuned setup .183 to .181 | Halawi a02, c03 | Contested (K05) |
| Retrieval helps strong agent a little | none .1230; weak non-agentic .12168; weak agentic .11824; good non-agentic .11738; good agentic .1140 | AIA d09 | Established |
| Retrieval helps small models leak-free | Qwen3-8B .234 to .179; Gemma-3-27B .214 to .184; 8 of 9 improve, up to 23%; Entertainment -31, Sports +16 | Hindcast d18 | Single-source |
| Retrieval did not help in ForecastBench | news rows .004-.005 worse than no-news rows; best LLM .128 (table) | a09, b10 | Contested |
| Retrieval can inflate mean and hurt | Qwen2.5-7B .159 to .250; mean forecast .20 (0 docs) to .46 (3-5 docs); Hermes .192 to .226 | Lu and Zhang a20, d16 | Established (K06) |
| Fixes for inflation | base-rate prompt .250 to .184; per-document median .250 to .222; base-rate only .127; market .074 | d16 | Single-source |
| One fake article flips forecasts | 1 article 56%; 3 70%; 5 69-74%; 10 89%; Brier .18 to .37; spoofed publisher 77% flips; perplexity filter at T=1.2 67% flips | a21, c17, d17 | Established (K07) |
| Frontier models also flip | 74-82% of opposing forecasts reversed; deployed agents retrieve the fake in about 90% of runs; passage filter discards 39% of genuine news | Zhang and Stadie a19, c18 | Single-source |
| Date-filtered search leaks | leak pages 71% (Google), 81% (DuckDuckGo); Brier .108 leaky vs .242 leak-free; at least 3.8% of Halawi test resolved early | c10, c11, d20 | Established (K08) |
| Leak filter cost | recall 93.8%; 29.9% of clean results dropped; 1.5% residual leaks | BLF d05 | Single-source |
| Simulated ignorance fails | 52% of pre-cutoff Brier gap remains; closes 28-91% by model | c22 | Single-source |
| Crowd blend | .149 to .146 with 4x crowd weight (test) | Halawi a05 | Established (K10) |
| Price access for an agent | no search .116 to .103 with price; agentic search .085 to .075; price alone .096 | AIA d09 | Established |
| Show the human median to the LLM | GPT-4 .17 to .14; Claude 2 .22 to .15; simple average better (.13, .14) | Schoenegger b09, c08 | Established (K12) |
| Cassi crowd adjustment | "nearly 0.01" over own ensemble (blog); vs plain price market +0.6 BI ns; overall +1.0 over crowd+prior ns | FRI b13, b14; BLF d01, d02 | Contested (K11) |
| Top agents near the price | crowd+prior baseline BI 69.9 overall; BLF +3.4 (sig), Cassi +1.0 (ns), Grok +0.1 to +1.0 (ns) | BLF d02 | Single-source |
| LLM vs human gap | Halawi .179 vs .149; ForecastBench best LLM .128 vs supers .096 (200 items); gap .017 by Jan 2026; Metaculus pro-bot gap 20.03 (Q2 2025) to 1.25 ns (spring 2026) | a01, a09, b13, b15, b18 | Established (K09) |
| Winners ensemble and call more | 86% ensemble; 28 vs 7 calls (p=.022); aggregating +1,799 points (CI +1,017 to +2,582) in survey; teams of bots saturate near 2-10 | a24, b15, b18 | Single-source, observational (K13) |
| Higher reasoning wins | higher-reasoning twin beats standard in 8 of 8 pairs (p=.004); FutureSearch thinking vs not .1597 vs .1560, p=.53 | b18, b20 | Contested |
| Hedging fix after averaging | Platt on mean .1076; extremize d=3 .1085; none .1140; Platt added .016 (binary) in bot survey | d10, a24 | Single-source |
| Bias to Yes is not fixed by averaging | mean 57% vs 14/31 Yes; models over-predict Yes in BttF too | a07, c07, b20 | Established (K15) |
| Structure beats repeats | 5 direct samples 0.004; structured 5-call 0.036 at 4.9x tokens | CHAIN d14 | Single-source (K17) |
| Consistency checks | Cond r .92/.87 and .71/.69; Negation .60 vs -.36; patched forecaster no better | Paleka a18, b27, d19 | Contested (K14) |
| Prompt tweaks | most near zero; base rate first about -.011 to -.016; Bayesian prompts worse | Schoenegger b23 | Single-source |
| Humans with LLM assistant | +24-28% accuracy (N=991, 6 questions) | a11, b24 | Established but human-only |

## 4. Mechanisms and models

**4.1 Why averaging helps (and how much).** For squared error, the Brier of the mean forecast equals the mean Brier of members minus the variance of members around the mean (Jensen). Gain = within-question variance of runs. If runs are similar (SD small, errors shared), gain is near zero. Halawi (.0027), AIA (.0042), CHAIN (.004) are all this small. The mean never loses to the average member, but it can lose to the best member (b11, a06). Implementation: collect K probabilities p_i, clip to [0.02, 0.98], take arithmetic mean or median. Trimmed mean (drop or half-weight the point farthest from the median) is equal within noise (differences .0007).

**4.2 Logit vs arithmetic mean.** BLF (d03): logit averaging gives only a small extra gain; it degrades more gracefully when one run fails (p=0.95 with one dead trial in five: arithmetic loses about 9 points, logit about 4). AIA: Platt scaling on the arithmetic mean was best (.1076).

**4.3 Why mixed models help.** Gain over copies grows as pairwise correlation falls. Frontier models correlate .94 (soccer, d13). A second draw from the same model is nearly redundant; one draw from a different model is not. Implementation: for a budget B, allocate across 3 or more distinct members, drop members that correlate above about .9 with another, and stop adding after about 3 distinct (d12, d11). Members must each be decent: a much worse member can pull the mean below the best single (b11).

**4.4 Aggregation by LLM.** Rewriting the ensemble with an LLM (USC, non-agentic supervisor) is worse than the mean because LLMs overweight outliers (d07, d08). The one version that worked: an agentic supervisor that finds disagreement, searches to resolve it, and overrides the mean only when highly confident (.1125 vs .1140, a 0.0015 gain). So: code aggregates; an LLM may only add new evidence.

**4.5 Retrieval pipeline.** Halawi: (1) model writes search queries; (2) news API returns articles; (3) a cheap model rates relevance and summarises; (4) forecaster reasons; (5) ensemble. Agentic ReAct search beat the fixed pipeline for every model in Bench to the Future (a14); it also has more run variance (about 1.7x SD of fixed-evidence runs, a13), so more need to average. Model-guided retrieval (retrieve only what a quantitative base model needs) halved search count (11.7 vs 23.9) and improved base-probability Brier (.0802 vs .0882) (c19).

**4.6 Retrieval inflation.** Each added document tilts toward the event. Mean forecast rises from .20 to .46 (a20). Fix stack (single-source each): base-rate-first prompt; one forecast per document then median (the poison paper shows k=5 still 40-52% flips); cap per-document shift; compare against a constant base rate. Note the opposite error: after averaging, forecasts are hedged toward 0.5 and extremizing helps (d10). Both can be true. A reference-class prior first, then shift by evidence type, then extremize, is the untested combination (K19).

**4.7 Crowd anchoring.** Three versions measured: (a) show the price to the model (AIA price access .116 to .103); (b) blend in code (Halawi 4x weight on the crowd); (c) review step when forecast and price diverge (Cassi, rule unpublished). Schoenegger (b09): the model's own update is worse than a plain 50/50 average. The model moves in proportion to the gap (r = .88, .87), so it already imitates the anchor. Prefer code blend over model update. Near price 0 or 1 the system hedges and loses .04 Brier (a04).

**4.8 Poison and leakage.** A retrieved document is treated as true regardless of publisher label (a21). The attack succeeds because ensembles retrieve the same fake in about 90% of runs (c18), so averaging does not dilute it. No defense tested both keeps real news and rejects fakes (a19: filter discards 39%; BLF leak filter 29.9% false positive). For evaluation, use post-cutoff questions or a frozen leak-free corpus.

## 5. What holds up

**Replicated across independent sources (K01, K03, K06, K07, K08, K09, K10, K12, K15, K20).**
- Averaging runs gives a small, real gain (.003 to .005); 4 sources.
- Mixed models beat copies when decorrelated; 4 sources.
- LLM re-reading of runs is worse than the mean; Halawi, AIA, BLF.
- Retrieved text is an attack surface; 3 sources.
- Leakage inflates backtests; 3 sources.
- LLM forecasts lean Yes and the lean survives ensembling; 3 sources.
- Mixing in the crowd gives small gains; the price alone is a strong baseline; 3 sources.

**Failed or contradictory.**
- Retrieval did not help in ForecastBench (a09) or Pratt (a16), helped in Halawi (.02) and AIA (.009), hurt small models in Lu and Zhang (.159 to .250). Likely reasons: retrieval quality, base-rate handling, headline-only sources, model strength.
- Ensembling hurt GPT-4o base (c13) and a 9-forecast mixed ensemble lost to its best member (b11).
- Thinking models: FutureSearch no significant gain (b20); Metaculus 8 of 8 pairs better (b18). Different metrics and question sets.
- Consistency checks: correlate with Brier across models but a consistency-patched forecaster did not improve (d19).
- Deliberation: helped only for mixed models (c14), consistent with schema G9.

**Moderators.**
- Run variance (higher variance, bigger gain).
- Member decorrelation and quality.
- Crowd uncertainty (.3-.7) and number of relevant articles (5+) for retrieval value (a04).
- Topic: sports and awards gain, hype topics lose (d18).
- Search quality: weakest search equals no search (d09).
- Question base rate: 80-83% of questions resolve No in several sets, which flatters low guesses and price anchors (b15, d06, d18).

**Interventions that worked.** Retrieval for a plain model; mixed-model ensembles; mean of 5-10 runs; agentic supervisor with search; Platt or extremizing after averaging; crowd blend in code; base-rate-first prompt (about -.011 to -.016); belief state for two of three backbones.

**Interventions that did not.** LLM rewriting of runs; calibration by binning or isotonic regression (Halawi); simulated ignorance by instruction; allow-lists, perplexity filters and per-document median as poison defenses; more documents past about 5; letting the model update toward the crowd; consistency-patching.

**Evidence quality limits.** Halawi numbers are one paper counted by three agents (independent sources for ensembling: about 4). Question sets are small (31, 113, 202, 464). Winner statistics are observational. Many 2026 results are preprints or blogs.

## 6. Language models

**Baselines without retrieval.** Halawi (c02): 14 models, most near or worse than .25; only GPT-4 and Claude-2 families beat it by more than .02 (GPT-4-1106 .208). Arena score correlates with Brier at r = -.68 (b12). By 2025, no-evidence frontier models still beat .25 but are clearly worse than evidence forecasts (b20).

**With retrieval and ensembling.** Halawi .179 (2024). Lu (a15, b22): o3 .1352 (median of 5), o3-pro .1386, GPT-4.1 .1542, GPT-4o .1883, GPT-4o-mini .2743 on 464 questions; median and mean about the same. Bench to the Future (b20): Sonnet 3.5 .1925, 3.5 v2 .1690, 3.7 thinking .1645, Sonnet 4 .1560 (p=.0024 vs 3.5), Gemini 2.5 Pro .1611. Newer models also know more (confound).

**How much each factor changed things.**
- Model generation: about .03-.04 Brier across 2024-2025 (largest).
- Retrieval: .02 (plain base) down to .009 (strong agent).
- Fine-tuning: .003-.007 (Halawi); RL on outcomes plus 7-run ensemble .190 vs o1 .202, still .039 behind the market (a12, K16).
- Averaging: .003-.005.
- Crowd price: .010-.013 for a strong agent.
- Platt or extremizing: .0055-.0064 after averaging (d10).

**Behaviour patterns.** Yes lean and hedging toward the middle (a07, a04); optimism bias that rises with document count (a20); models treat retrieved text as truth (a21); small models move the right way on new evidence but by too little (c20, 1.5B-8B only); giving the whole news history made it worse (c20). Ensembles of retrieval agents retrieve the same fake in about 90% of runs, so ensembles add exposure (c18).

**Frontier status.** FRI (b13): Grok 4.20 Preview (8 forecasts averaged, X and web search, Python) 0.102; Claude 3.5 Sonnet (Oct 2024) 0.117; gap to superforecasters 0.017 (about one year); projected parity Nov 2026 (CI Jan 2026 to Nov 2027), an extrapolation. BLF (d01, paired): BLF 73.3 BI, Cassi 70.8, Grok 4.20 70.5, Foresight 69.3; question difficulty explains 62% of score variance, so unpaired leaderboard gaps are weak. The xAI result cannot be split into 8-run average vs search tools (no ablation). Cassi uses Tavily retrieval, an o3 plus GPT-5 ensemble, a review LLM and a crowd adjustment on market questions (b14).

**Reasoning models.** Higher-reasoning twins win 8 of 8 (b18) but FutureSearch finds no significant gain (b20). Reasoning models still show cross-trial SD of .09-.10 on market questions (d04). The effect of averaging for reasoning models is not cleanly measured.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Average 5 independent runs in code, mean or median.** S3. [E] K01. Evidence a03, b04, c04, d07, d14, d15. Expect .003-.005, not more. Cap at 5 (AIA: most gain by 5). Consistent with G4 and G11.
2. **Code aggregates; no LLM re-reading of runs.** S3, G5. [E] K20. Evidence a03, d07, d08, d03. An LLM may be given only a search step and a confidence-gated override; that is a Test first item.
3. **When averaging, mix models or distinct prompts only if decorrelated; do not add copies past 5.** S3. [E] K03, K18. Evidence a06, c14, c15, d11, d12, d13.
4. **Retrieved text is untrusted: record source and age, and let no single document move the forecast past a cap.** G. [E] K07. Evidence a19, a21, c17, c18, d17. Provenance labels alone do not help (flips occur regardless), so the cap is the rule; its size is a Test first item.
5. **Check the shift caused by retrieval against the base rate.** G. [E] K06. Evidence a20, d16, d18. When added documents lift the mean sharply, compare to the reference-class prior and report both.
6. **Leak hygiene in our own benchmark.** Evaluation, not schema. [E] K08. Use post-cutoff questions or a frozen corpus.
7. **Where a market price or community forecast exists, give it to the pipeline and blend in code.** S3, memory. [E] K10, K12. Evidence a05, b09, d09. Use a simple average, not a model update.
8. **Check the aggregate's mean against the base rate; averaging does not remove Yes lean.** S3. [E] K15. Evidence a07, c07, b06.
9. **Do not add tricks tested and failed: binning or isotonic calibration, simulated ignorance, model updating toward the crowd.** Candidates for section 4b. [E] a25, c22, b09.

### Test first

| Item | Part | Status | Evidence | Why test |
|---|---|---|---|---|
| Platt or log-odds extremizing after the mean | S3 | [S] | d10 | Conflicts with G4 "no extremizing votes"; that rule covers voters on answer problems, probability tasks differ. Test before editing G4. |
| Reference-class prior first, move only by evidence type, cap per-document shift | S2/S3 | [S] | d16, K19 | Each piece tested alone on 7-8B models only. |
| Agentic supervisor that searches to resolve disagreement | S3/S7 | [S] | d08 | One source, .0015 gain. |
| Mixed prompt personas (different decomposition styles) instead of identical copies | S3 | [S] | d14, K17 | Single source, not equal tokens, not search forecasting. |
| One long run vs k short runs at equal tokens | G11 | [S] | none directly; d14 | Nobody measured this. |
| Price-divergence review step (Cassi style) | S3/O | [C] | b14, d02, d06 | Rule unpublished; gain not significant over price. |
| Consistency violation between paired questions as an ensemble filter | G | [C] | d19 | Not tested as a filter. |
| Belief state (probability plus evidence summary carried between steps) | S3 memory | [S] | d04 | Helped 2 of 3 backbones. |
| Search-quality gate: skip search if provider is weak | G12 | [S] | d09 | Weak search equals no search. |
| Retrieve only when the crowd is uncertain (.3-.7) or 5+ relevant articles | G12 | [S] | a04 | Conditions found after viewing validation. |
| Model-guided retrieval (quantitative base first, retrieve only needed inputs) | S2/S3 | [S] | c19 | One scaffold paper. |
| Poison defense that keeps genuine news | G | open | a19, d17 | No defense has been shown. |

## 8. Concrete tests on our bench

All tests: both arms use equal total tokens (count setup and aggregation). Items: binary forecasts resolved after the model cutoff, or pastcast items from a frozen corpus; at least 150 questions for a .005 effect (use paired bootstrap CIs). Metric: Brier, paired, plus mean forecast vs base rate.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Binary forecast, search enabled | A: 1 run with 5x reasoning budget; B: 5 runs averaged | Brier, paired | B better by .003-.005 or tie; if A wins, drop averaging for long-reasoning models |
| T2 | Same | B: 5 identical runs; C: 5 runs with 3 different decomposition prompts; D: 3 models | Brier; pairwise correlation of runs | D >= C > B; correlation falls from about .9 to under .8 |
| T3 | Same | mean vs median vs trimmed vs LLM re-reader vs agentic supervisor (with search) | Brier | mean = median = trimmed; LLM re-reader worse by about .003; agentic supervisor ties or beats by .001 |
| T4 | Same | no extremizing vs Platt vs log-odds d=2,3 on the mean | Brier, calibration | .005 gain if hedged; none if already extreme |
| T5 | Questions with documents | search vs no search; with base-rate-first step; with per-document median; with cap on shift | Brier; mean forecast shift | Search +.009 to .02 for a plain model; base-rate step recovers about half of inflation |
| T6 | Questions with market price | blind vs price in prompt vs code blend (50/50) vs model update | Brier on mid-range prices | Code blend >= price in prompt > model update; gain .010-.013 |
| T7 | Planted fake article set | no defense vs source weighting vs per-document median vs cap on shift | flip rate at k=1 and k=5; Brier | baseline flip rate 56%; a defense that gets under 30% passes |
| T8 | Questions split by run SD | 1 run vs 5 runs | Brier gain vs SD | Gain rises with SD; none when SD small |
| T9 | Retrieval toggle by crowd uncertainty | always search vs search only if price in .3-.7 or 5+ documents | Brier at equal tokens | Same Brier, fewer tokens |
| T10 | Paired related questions | drop members with consistency violations vs keep all | Brier | .002 gain if the filter works |

## 9. What does not transfer, and why

- **Training-based gains (RL on outcomes, fine-tuning).** Our agent does not train. K16 ignored.
- **Human-only results.** The LLM assistant RCT (a11, N=991) shows what humans do with an assistant, not what an agent does.
- **Extremizing human crowds.** In human aggregation extremizing rests on independent partial information. Samples from one model share the same information (G4). The LLM result (d10) is a calibration fix for hedging, not an information argument.
- **Metaculus winner statistics.** 28 vs 7 calls and 86% ensembling are confounded by effort and skill (b15).
- **Leaderboard gaps for Cassi and xAI.** Blog results with no ablation. Do not copy the 8-run average or the crowd adjustment on the strength of rank.
- **Small-model retrieval results (Lu and Zhang, Hindcast).** 7-27B models only. Frontier models may be more skeptical or more robust; unknown.
- **Sports 3-way results.** Soccer predictions with .94 correlation across models do not set the diversity level for binary news questions.
- **Price anchoring on low base-rate sets.** Price and prior look strong partly because 80-83% of questions resolve No (d06).
- **Questions without a crowd price.** Crowd adjustment needs a live price; most of our items will not have one.
- **Search at scale.** Winners with 50-100 calls per question (a22) are not a model for a token-limited agent (G7, G11).

## 10. Open questions

1. Does averaging N runs beat one longer run at equal tokens for a scaffolded agent? (No study.)
2. How much retrieval benefit remains in Halawi's setup with leak-checked retrieval?
3. What exactly is Cassi's crowd-adjustment rule and score outside market questions?
4. How many distinct members before the gain flattens, for frontier models on binary news questions? Direction is clear (about 3), size is not.
5. How to detect poisoned articles without dropping genuine news? (No defense shown.)
6. Does a base-rate-first step plus per-document cap plus extremizing fix retrieval inflation on frontier agents?
7. Is xAI's #2 rank due to its 8-run average or its search tools?
8. Does consistency work as an ensemble-member filter?
9. Do reasoning models gain from small ensembles? (Cross-trial SD .09-.10 suggests possibly yes.)
10. Do the Yes lean and the retrieval optimism bias add or cancel across question sets?

## 11. Sources

[V] opened, [M] snippet only. Several [V] items were read through a page summariser (Metaculus notebook, LessWrong posts, alphaXiv): numbers from them are lower confidence.

- [V] Halawi, Zhang, Yueh-Han, Steinhardt (2024), Approaching Human-Level Forecasting with Language Models. https://arxiv.org/abs/2402.18563
- [V] Schoenegger, Tuminauskaite, Park, Bastos, Tetlock (2024), Wisdom of the Silicon Crowd. https://arxiv.org/abs/2402.19379
- [V] Karger et al. (2025), ForecastBench. https://arxiv.org/abs/2409.19839
- [V] Schoenegger, Park, Karger, Trott, Tetlock (2024), AI-Augmented Predictions. https://arxiv.org/abs/2402.07862
- [V] Turtel et al. (2025), Outcome-based RL to Predict the Future. https://arxiv.org/abs/2505.17989
- [V] Wildman / Hambly et al. (FutureSearch) (2025), Bench to the Future. https://arxiv.org/abs/2506.21558
- [V] Lu (2025), Evaluating LLMs on Real-World Forecasting Against Expert Forecasters. https://arxiv.org/abs/2507.04562
- [V] Pratt et al. (2024), Can Language Models Use Forecasting Strategies? https://arxiv.org/abs/2406.04446
- [V] Paleka et al. (2025), Pitfalls in Evaluating Language Model Forecasters. https://arxiv.org/abs/2506.00723
- [V] Paleka et al. (2025), Consistency Checks for Language Model Forecasters. https://arxiv.org/abs/2412.18544
- [V] Zhang, Stadie (2026), One Fabrication Is Enough. https://arxiv.org/abs/2611.15102
- [V] Lu, Zhang (2026), The Corroboration Illusion. https://arxiv.org/abs/2609.22246
- [V] Metaculus Q1 2025 notebook (page summary). https://www.metaculus.com/notebooks/38673/q2-ai-benchmark-results-pros-maintain-clear-lead/
- [V] Metaculus Q2 2025 results (LessWrong). https://www.lesswrong.com/posts/Surnjh8A4WjgtQTkZ/q2-ai-benchmark-results-pros-maintain-clear-lead
- [V] Metaculus Q4 2024 results (LessWrong). https://www.lesswrong.com/posts/P8YwCvHoF2FHQoHjF/metaculus-q4-ai-benchmarking-bots-are-closing-the-gap
- [V] Metaculus FutureEval spring 2026 (LessWrong). https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is
- [V] AI forecasting in 2026: what 11 analyses say (LessWrong, page summary). https://www.lesswrong.com/posts/a82q6yd8zKpYk56cF/ai-forecasting-in-2026-what-11-analyses-say
- [V] Aitchison, Jeen, Shevlane, Day (2026), Diversity is the Strength of the AI Crowd. https://arxiv.org/abs/2606.29661
- [V] Zou et al. (2022), Forecasting Future World Events with Neural Networks. https://arxiv.org/abs/2206.15474
- [V] Forecasting Research Institute (2026-01-29), LLMs Are Closing the Gap on Human Superforecasters. https://forecastingresearch.substack.com/p/llms-are-closing-the-gap-on-human
- [V] Hsieh, Fu, Chen (2024), Reasoning and Tools for Human-Level Forecasting. https://arxiv.org/abs/2408.12036
- [V] Schneider, Schramm (2025), The Wisdom of Deliberating AI Crowds. https://arxiv.org/abs/2512.22625
- [V] Chetlapalli et al. (2026), Diverse by Reasoning. https://arxiv.org/abs/2608.24001
- [V] Yang et al. (2025), LLM-as-a-Prophet. https://arxiv.org/abs/2510.17638
- [V] Schoenegger, Jones, Tetlock, Mellers (2025), Prompt Engineering LLMs' Forecasting Capabilities. https://arxiv.org/abs/2506.01578
- [V] El Lahib et al. (2026), Temporal Leakage in Search-Engine Date-Filtered Web Retrieval. https://arxiv.org/abs/2602.00758
- [V] Cao et al. (2026), From Narrative to Auditable Forecasts. https://arxiv.org/abs/2609.05905
- [V] Yuan, Ding, Vlachos (2026), Do Language Models Update their Forecasts with New Information? https://arxiv.org/abs/2509.23936
- [V] Chi et al. (2026), WorldReasoner. https://arxiv.org/abs/2606.11816
- [V] Li et al. (2026), Simulated Ignorance Fails (IJCAI). https://www.ijcai.org/proceedings/2026/0650.pdf
- [V] Murphy (2026), Agentic Forecasting with Structured Linguistic Beliefs (BLF). https://arxiv.org/abs/2604.18576
- [V] Alur et al. (2025), AIA Forecaster technical report. https://arxiv.org/abs/2511.07678
- [V] Peng et al. (2026), Two Heads Are Better Than One. https://arxiv.org/abs/2609.33257
- [V] LLM-SoccerArena (2026). https://arxiv.org/abs/2607.24573
- [V] Liu et al. (2026), CHAIN. https://arxiv.org/abs/2609.36689
- [V] FutureSearch (2026-05-01), Run agents twice for fun and profit (blog). https://futuresearch.ai/blog/run-agents-twice
- [V] Hindcast (2026), Replaying Prediction Markets. https://arxiv.org/abs/2607.14051
- [M] Karger et al. / FRI update posts (snippet only). https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark
- [M] News-augmented forecasting failure modes (snippet only). https://arxiv.org/abs/2511.18394

*Corrections applied from critique.md: Halawi Table 5 is read as .181 fine-tuned GPT-3.5 alone, .183 same without retrieval, .186 base GPT-4 with retrieval, .206 without (retrieval about .02 for a base model, about .002 for the fine-tuned setup). ForecastBench best LLM on the 200 set uses .128 (table) since the text's .122 is inconsistent. Halawi crowd Brier .149 (text) vs .146 (Table 5 caption). Evidence ids a22, a23, a24 come from page summaries; a18 values were not transcribed.*
