# E03.01 Scoring rules and calibration: cross-check critique

Checker re-opened (PDF text, this session) ForecastBench, Halawi et al., Tian et al., Schoenegger and Park, Silicon crowd, Xiong et al., Paleka et al., Turtel et al., Damani et al., GPT-4 Technical Report. Jewson's example re-computed by hand. 25 claims written to claims.jsonl (K01-K25).

## Corrections made (numbers re-checked against source text)

1. **a23 (ForecastBench) mixed two sets.** Source: on the 200-question human subset, superforecasters .096, public .121, Claude 3.5 Sonnet .122 (best LLM without crowd values .136). With combination questions: .076, .096, GPT-4o .130 (gap .054 vs GPT-4o-to-GPT-4 gap .026). Line a23 gave .076/.096 as the 200-subset. b19, b20, c07, c08 are right; a23 is wrong. Claim K17 uses the corrected pairing.
2. **b11 labelled GPT-4 numbers as gpt-3.5.** GPT-4 TriviaQA ECE is .078 (label) vs .024 (verbalized top-1), .041 (top-4). gpt-3.5 is .140 vs .068/.050/.054. a14, a15, c27 are right.
3. **a15 "discrimination is not better" is only partly true.** GPT-4 AUC: TriviaQA .950 label vs .937 verbalized (no gain), SciQ .820 vs .843, TruthfulQA .462 vs .622 (large gain). So verbalizing helped discrimination on the hardest set.
4. **Paleka correlations (a25, b22, c31).** Table 2 gives per-check correlations with Brier. Conditional check: .92/.87 scraped, .71/.69 NewsAPI. Negation: .60/.67 scraped but -.36/-.13 NewsAPI. Aggregate: .62/.85 scraped, .49/.66 NewsAPI (arbitrage/frequentist). a25 recommended "ask the negation"; that check is not robust. Only conditional checks held up on both datasets. Which panel carries the Figure 3 value 0.49 is not clear from the text.
5. **Halawi crowd Brier is .149 in the main result and .146 in the ablation table** (different aggregate/test slice). Both are in the paper. Our notes should state which one is used. Confirmed: .179 vs .149, 71.5% vs 77.0%, .199 vs .246, ablations .186/.182/.206, RMS error .42 vs .38, 13,253 fine-tune samples, SE .002-.003.
6. **Turtel (c21) needs the market baseline.** ReMax ensemble Brier .190, ECE .062, but the Polymarket price still beats it by .039 (o1 .202, ECE .093; plain DeepSeek-R1 14B .215). Modified-GRPO .192/.054 is as good as ReMax.
7. Confirmed unchanged: Tian label/verbalized ECE tables; Schoenegger and Park (.20 SD .18 vs .07 SD .08, t(22) -1.23 and -10.69, N=23, CV 42.14% vs 57.59%); Silicon crowd (.20 vs .19, p=.850, 57.35% mean, GPT-4 .17 to .14, Claude 2 .22 to .15, equivalence .081, Holm-type p .026 to .039); Xiong (ECE above .377, AUROC 62.7%, 54.8% to 92.7%, ECE .064 at 100%, .028 best); GPT-4 report ECE .007 vs .074; Damani 0.37 to 0.03 and 61.7% vs 63.0%; Guo numbers; Jewson 1/80.

## Contradictions between sources

- **Verbalized vs token confidence.** Tian: verbalized ECE far lower. Xiong: verbalized overconfident, average ECE above .377 on older models, GPT-4 AUROC only 62.7%. Different models, prompts and tasks; ECE rewards constant predictors, so neither settles which is better in Brier. (K08, contested.)
- **Direction of LLM forecast bias.** Silicon crowd: yes-bias (mean 57.35%, outcomes 14/31 yes). Pratt: low-probability bias, so negative-outcome-heavy sets favour the model. Halawi: hedging, rarely outputs low probabilities. Schoenegger and Park: hugging 50% not supported. Bias depends on model, prompt and base rate. (K14.)
- **Do plain LLMs beat .25?** Halawi and Phan: mostly near or worse. Bench to the Future: all no-evidence models below .25. Question mix and retrieval timing explain this.
- **Ensembling.** Silicon crowd: 12-model median matched the crowd. Phan: base-LM ensemble no gain. Halawi: ensemble of all forecasters beat top-k subsets. (K16.)
- **Brier vs log score.** Jewson argues Brier can prefer a catastrophic forecast; Damani chose Brier because the log score is unbounded. A design choice, not a factual conflict.

## Weak spots

- Founding papers were not opened by any agent: Brier 1950 (HTTP 403), Murphy 1973 (403), Ferro and Fricker 2012 (download failed). The decomposition facts come from Gneiting and Raftery, Siegert, Dimitriadis, Wikipedia. Treated as second-hand but consistent across four sources.
- Almost all forecasting-LLM studies are small or pre-2025 models: N=23, N=31, a few hundred questions, GPT-4/Claude 2/3.5-era. No 2026 frontier model has a measured Brier in this folder except Bench to the Future (Sonnet 4 .1560) and Turtel (14B).
- Several claims are single-paper (ForecastBench, Paleka, Halawi ablations). Halawi tuned hyperparameters on validation, and kept training samples that beat the crowd, which may leak crowd information.
- ForecastBench parity extrapolation: about 10 models, R2 .47/.41, p=.046.
- Plenty of ECE numbers use different bin counts (10 equal-count in Kadavath, 15 in Guo, adaptive in Autocast), so they cannot be compared across papers.
- No source here tests what we most need: whether a thinking scaffold changes the decomposition (REL, RES, UNC) at equal tokens, rather than only the total Brier.

## Seen only in snippets or second-hand (not opened)

Brier 1950, Murphy 1973, Ferro and Fricker 2012, Mason 2004 (via Gneiting and Raftery), Pratt et al. table columns (flagged by the agent as uncertain column order), Phan et al., Leng et al., Yoon et al., Hambly et al. numbers, Kapoor results tables, Hoessly, Steyvers, Paleka Pitfalls counts, Autocast calibration number, the Silicon-crowd "17 to 28%" accuracy gain. Treat these as unverified in their details.

## GAPS (open questions, most decision-relevant first)

1. Does a thinking scaffold change reliability or resolution (Murphy split), or only total Brier, at equal tokens on resolved questions? No source separates the two for a scaffold.
2. How many resolved items per question class are needed before a class-level calibration map (temperature or Platt) beats raw stated probabilities on held-out Brier? Kapoor suggests about 1,000 for learned calibrators; Halawi's system gained nothing from recalibration. Where is the break-even?
3. What are the 2025-2026 measured Briers of current frontier chat and reasoning models (Claude, GPT-5-class, Gemini 2.5/3) on live ForecastBench or other unresolved sets, and does the superforecaster gap still stand near .05?
4. Is the safety-training hedging effect (never outputs under 5% or over 95%) real, and does a push-to-extremes recalibration or an explicit instruction to use the full 0-100 range gain Brier on held-out items?
5. Which consistency checks (conditional, negation, and/or) predict later Brier robustly across question sources, and can they serve as the pre-resolution signal in S9? Negation flipped sign across datasets.
6. For non-forecasting tasks with exact answers (our actual use), how should the S9 record map pass/fail checks to probabilities, and does Brier on a pass-probability log track real accuracy gain better than raw pass rate?
7. Do multi-sample agreement scores from the same model give real resolution beyond the model's own stated probability after calibration (Xiong shows AUROC gain; G4 warns about correlation)? Needs a head-to-head with a calibrated verbalized baseline.
8. Which proper score should the log use for rare events, Brier or log score, given Jewson's catastrophic-forecast case and Damani's boundedness argument? Needs a comparison of class rankings under both on one real record.
9. Does stating the confidence before vs after reasoning change calibration for current models (Tian: CoT did not help; Yoon: introspection mixed)?
10. Have the founding texts (Brier 1950, Murphy 1973) any claims, such as the exact partition conditions, that later reviews misstate? A full-text read is still missing.

## Gap search results

Gap searcher read 26 new evidence lines (evidence_d.jsonl, d01-d26; 25 opened as text, d26 not opened) and added claims K26-K33 and edits to K08, K14, K17, K18, K19, K21, K22, K25. Web search quota ran out early, so most sources came through arXiv PDF text and arXiv search pages; the FRI, Good Judgment and Lightning Rod pages (d07-d09) were read through a page-summarising fetch tool, not raw text.

**Gap 1 (scaffold and the Murphy split): partly closed.** One source gives the split for a scaffold change: sub-question decomposition took calibration .026 to .008 and refinement .091 to .083 (Brier .141 to .132, n=500; d01). So the gain came through reliability, and resolution did not rise. At matched tokens, LEAP cut top-option ECE .147 to .088 and Brier .250 to .206 against a two-sample monolithic arm (d03). Neither is a clean equal-token REL/RES test, and each is one paper. K26, single-source.

**Gap 2 (break-even size for a calibration map): partly closed.** Kapoor's 1,000 is for a learned classifier (d18). A 2-parameter Platt fit on 30% of a few hundred items removed 99% of a large reliability term when raw calibration was poor (d16). It did nothing for Halawi's already-calibrated system (d15). Per-model Platt matched the strongest single model in only 7 of 16 ForecastBench groups at N>1,000 (d17). Analytic power: about 350 items to see a .02 edge, 1,400 for .01 (d19). No paper measures the break-even directly; the practical rule is condition-dependent (K32 contested, K31).

**Gap 3 (2025-26 frontier Brier, superforecaster gap): closed for ForecastBench, open elsewhere.** Gap is about .02 (Oct 2025) and .017 (Mar 2026), not .05, but models see market prices and GPT-4.5 correlates .994 with them (d07, d08). Good Judgment and Lightning Rod read the same board differently (d09). Without prices, Opus 4.5 is near coin-flip on hard markets (soft-Brier .256 vs .25; d12) and only one of five models beat the base rate on KalshiBench (d11). K27 contested, K28 established.

**Gap 4 (hedging, push-to-extremes): stays open.** Halawi's hedging claim is a stated hypothesis (d15). Prophet Arena and the World Cup run show conservatism or under-confidence when a market price is shown (d10, d13); KalshiBench and the one-shot arm of LEAP show over-confidence without it (d11, d03). No source tests an extremise step or a full-range instruction on held-out items. K14 stays contested.

**Gap 5 (consistency checks as pre-resolution signal): partly closed.** An independent analysis of the Paleka cliques confirms that negation and paraphrase checks carry little and and/or checks carry most (d16). The size of incoherence predicted which bets lost most (CV AUC .775) but this is regret against the repaired quote, not later Brier of the original. Whether conditional checks predict Brier across question sources beyond Paleka's two sets is still untested.

**Gap 6 (pass/fail checks to probabilities for exact-answer tasks): stays open.** Closest is self-rated effort beating stated confidence for failure prediction across 12 LLMs and 38 tasks (d23), with scaled ratings, not true probabilities. No source scores a check-to-probability map by Brier or compares it with raw pass rate. A 21-case pilot shows how wide the intervals are at small N (d24).

**Gap 7 (multi-sample agreement vs calibrated stated probability): stays open.** The one new data point shows agreement moves with sampling temperature (66% to 30%) while stated confidence does not move (d21). Nobody compares agreement against a calibrated verbalized baseline on AUROC or Brier. ForecastBench pooling of different models beat Platt-calibrated single models (d17), which is a different question.

**Gap 8 (Brier or log score for the log): partly closed.** On 965 held-out items Brier and log score rewards gave test Brier .1653 vs .1648, inside a three-seed spread of .0032 (d14). ECE and Brier ranked the World Cup agents in opposite order (d13). No rare-event comparison on a real record was found; Jewson's case stays an analytic point. Recommendation: log both, treat Brier gaps under about .005 as ties (K29).

**Gap 9 (confidence before vs after reasoning): closed for one model, open for frontier chat models.** An 8B forecaster's stated confidence was nearly unchanged between forced and free answering (Spearman .90; same answer 67%; d20). With Tian's earlier result, K25 is now established for the models tested; no frontier chat model with reasoning has been tested on the ordering.

**Gap 10 (founding texts): stays open.** Brier 1950, Murphy 1973 and Ferro and Fricker 2012 returned 403 or bot pages again (d26). Four later sources state the decomposition the same way; Foresight Arena says it is exact only at the bin mean, and Yang et al. use Stephenson's exact binned version, which has extra terms. No misstatement found, but not verified against the originals.

### New caveats found

- Several 2026 tables in the PDFs are garbled in text; rows were rebuilt from the abstract and checked by arithmetic (d01, d02, d14). Their model labels may be off in the rows marked "inferred".
- Foresight Arena's LLM leaderboard is a simulation (d19). Do not cite its pattern of low REL and high RES as a measurement.
- Multi-outcome Brier values (Forecast-Dojo, World Cup 1X2, FutureX) are on a different scale from binary Brier and must not be compared with .25.
- Preprints dated Jul-Oct 2026 have had little or no peer review; treat single-paper claims as single-source.
