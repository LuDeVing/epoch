# Forecasting and calibration: subfields

Forecasting research studies how well people and now models predict uncertain events, and how to improve it. It divides into scoring (Brier and its parts), the study of top forecasters, training, aggregation, procedures (outside view, decomposition), and LLM benchmarks. Questions resolve later, so there is a real check, but the outputs are probabilities rather than single exact answers, so transfer is partial. Opened facts: the Brier score is the mean squared error of probabilities, splits as BS = reliability - resolution + uncertainty, and a 70 percent rain forecast scores 0.09 if it rains and 0.49 if not.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Scoring rules and calibration | Brier score and decomposition | Brier 1950; Murphy | High | Logging; S9 class record |
| Good Judgment Project | Who forecasts well; persistence | Tetlock; Mellers | Med | Year-to-year correlation .65; about 70% of superforecasters kept status (AI Impacts) |
| Training | One-hour module on probability, outside view, bias | Chang et al. 2016; Moore et al. 2017 | Med | Reported effect lasted at least a year (secondary source) |
| Outside view and base rates | Comparison classes as starting point | Kahneman and Lovallo | High | S0 gate. Forecasts tagged with comparison classes averaged Brier 0.17 against 0.26 for the next-best tag (AI Impacts, observational) |
| Decomposition (Fermi-ize) | Split question into sub-questions | Tetlock | High | Operator O3. No effect size reported in source |
| Aggregation and extremizing | Pool, weight, push away from 0.5 | Baron et al.; Satopaa | Med | G4: no extremizing for correlated samples. Source calls extremizing controversial |
| Belief updating | Small steps on new evidence | Tetlock | Med | S5 revise |
| LLM forecasting benchmarks | Models against superforecasters | ForecastBench (Karger et al.); FRI | High | Direct. 1,000 auto-generated questions; experts beat the top LLM (p < 0.001); gap to superforecasters now 0.017 Brier, about one year of LLM progress; parity projected around November 2026 (wide interval) |
| Retrieval and ensembles for LLM forecasts | Search tools, averaging 8 runs, crowd adjustment | xAI, Cassi entries (FRI post) | Med | S3: averaging independent runs; crowd adjustment gained nearly 0.01 |
| Verbal confidence | Stated against actual confidence | Kadavath et al. 2022 | Med | Guardrail on confidence |

## Dig into next

**1. Base rates and comparison classes as the S0 gate.**
- Is the 0.17 against 0.26 gap causal, or because careful forecasters use comparison classes?
- Does giving the model its class's measured pass rate improve effort allocation (G12)?
- Evidence: the Chang et al. training study (not opened), our logged class records.

**2. Decomposition and combine step.**
- LLMs lagged most on combination questions in the original ForecastBench paper; does a coded combine step close it?
- Evidence: ForecastBench question types, equal-token test.

**3. Calibration of agreement.**
- Is the fraction of samples agreeing calibrated for our task classes, and does code normalisation help (schema G5)?
- Evidence: Brier decomposition on our own logs.

## Does not transfer

Superforecaster teams talk, share news and compete. Tournament question selection and long resolution waits are institutional. Personal traits are about people. Many questions need current news that our tasks lack. The ForecastBench result is on probability scores, not on exact answers.

## Sources

[V] = opened and read this session. [M] = search result only, or from memory. Two further searches were refused (budget exhausted). Opened: 4.

1. ForecastBench abstract, arXiv 2409.19839. https://arxiv.org/abs/2409.19839 [V] (abstract only)
2. AI Impacts, Evidence on good forecasting practices from the Good Judgment Project. https://aiimpacts.org/?p=1283 [V]
3. FRI, LLMs are closing the gap on human superforecasters. https://forecastingresearch.substack.com/p/llms-are-closing-the-gap-on-human [V]
4. Brier score (encyclopedia entry). https://en.wikipedia.org/wiki/Brier_score [V]
5. FRI, Brier Index. https://forecastingresearch.substack.com/p/introducing-the-brier-index [M]
6. SJDM 2021 poster on training. https://dlab.sauder.ubc.ca/sjdm/presentations/2021-Poster-Karimi_Motahhar-Vahid-Forecasting-Probability-Training.pdf [M]
7. Chang, Chen, Mellers, Tetlock 2016, JDM. [M]
8. Tetlock and Gardner 2015, Superforecasting. [M]
