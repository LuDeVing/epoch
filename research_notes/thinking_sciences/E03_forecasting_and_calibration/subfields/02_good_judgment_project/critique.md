# Cross-check critique: E03.02 Good Judgment Project (who forecasts well; persistence)

Cross-checker pass on evidence_a/b/c.jsonl (29 + 29 + 29 lines). Sources re-opened this session (text extracted): AI Impacts GJP blog page, Mellers et al. 2015 PDF, Himmelstein et al. 2021 PDF, Halawi et al. 2024 PDF, Schoenegger et al. 2024 (Wisdom of the Silicon Crowd) PDF, Karger et al. ForecastBench PDF, Lu 2025 PDF. Chang et al. 2016 and Mellers et al. 2014 were NOT re-opened by me (two agents each opened them and their numbers agree).

## Numbers re-checked (confirmed unless noted)

1. AI Impacts: 70% of superforecasters kept status; year-to-year correlation 0.65; structural model multiple correlation 0.64. Confirmed on the page. They are quotes from the book Superforecasting, not a paper table.
2. Mellers 2015 Table 1: standardized Brier -0.34 / -0.14 / +0.04; resolution .40/.35/.32; calibration .01/.03/.04; AUC 96 vs 75 (top-team individuals 84); learning -0.26 vs -0.18. Confirmed. Table 3 trait correlations with Brier: Raven -.18, Shipley abstraction -.22, extended CRT -.23, CRT -.16, numeracy -.16, active open-mindedness -.12 (all n=1,776).
3. Himmelstein 2021 Table 2 (Season 1, 94 vs 94 questions): same-metric cross-half r values .36 (simple), about .40-.41 (hierarchical), .36-.39 (IRT). Confirmed as a range; the PDF table layout is scrambled so I cannot assign each value to a metric with certainty.
4. Himmelstein: IRT-model R2 .57 at 80 resolved questions (S1), .35 (S2). Confirmed.
5. Halawi: test Brier .179 vs crowd .149, accuracy 71.5% vs 77.0%, best baseline GPT-4-1106 .208, random .250. Confirmed. Ablation .186 (no fine-tune) and .206 (neither). Confirmed in text.
6. Halawi: aggregate with crowd (4x weight) .149 to .146. Confirmed.
7. Schoenegger 2024: LLM crowd M=.20 (SD .12) vs human .19 (SD .19), t(60)=0.19, p=.850; vs .25 benchmark t(30)=-2.35, p=.026; GPT-4 .17 to .14, Claude 2 .22 to .15. Confirmed.
8. ForecastBench: supers .096, public .121, best LLM .122 (all p<.001); dataset-question subset .076/.096/.130; Arena r=-.68 p=.003; parity near Arena 1406. Confirmed.
9. Lu 2025: o3 .1352, o3-pro .1386, GPT-4.1 .1542 etc. Confirmed (Table 3, median ensemble).
10. Lu 2025 experts: mean .1573 / median .0225 (157 q, SE .0189); held-out mean .1222 / median .0196 (41 q, SE .0309). Confirmed, but see correction C2.

## Corrections made

- C1. Evidence line a06 says Mellers 2015 was "NOT READ", while b09-b12 opened it. I opened it: b09/b10/b12 are right. Use b-lines for Mellers 2015. Nothing in the Mellers 2015 text contains the .65 or the 70% figure, or the .64 model; they are book-level numbers (a07/b01/c29 are one source, not three).
- C2. The "experts beat o3" claim in Lu 2025 (a27, c11) uses the median of per-question expert Brier scores (.0225) against the models' mean (.1352). Expert mean Brier is .1573 (157 q) and .1222 (41 q), different subsets from the models' 464 questions. The headline is not apples to apples. Claim K20 is marked contested. Also a27 said o3-pro hold-out .1307 and c11 said .1386; main-set o3-pro is .1386 (median) / .1389 (mean); I did not verify .1307.
- C3. a22/b23/c05 triplicate the same Schoenegger study; independent_sources counted as 1, not 3. Same for a19-a21/b21-b22/c01-c04 (Halawi) and a26/b24/c13 (ForecastBench).
- C4. Halawi's ablation table rows have labels dropped in text extraction (a21/c03 reported .182 for fine-tuned GPT-3.5 only; the text shows .182 and .181 for two close variants). The qualitative statement (retrieval carries most) is safe.
- C5. Brier scale: Mellers 2014/2015 use the 0 to 2 scale; LLM papers use 0 to 1 (halve the former). Several lines mix them.

## Contradictions between sources

- Persistence size: .65 year-to-year (book) vs .36 to .41 split-half (Himmelstein). Different metric, sample (volunteers vs HFC), and question count (94 vs a year of questions); not a contradiction but they should not be quoted together as one number.
- Traits: Mellers 2015 reports fluid intelligence and open-mindedness among top correlates; HFC Season 2 found open-minded thinking about zero (scale alpha .24) and education reversed sign. Predictors of accuracy are unstable across samples.
- Merkle 2025 (r about -.7) vs HFC trait correlations (.1-.3): matched test/task content probably explains it.
- LLM vs experts: ForecastBench says best LLM trails supers by .026; Lu says experts far ahead by median, not by mean; Halawi says system near the crowd. Different questions, so none are directly comparable.

## Weak spots

- Everything on GJP persistence and training comes from one research group and one tournament family (Mellers, Tetlock, Chang). The only independent persistence check is Himmelstein (HFC), and it shows weaker numbers.
- Superforecaster persistence is confounded with team support, extra workload and label effects (Mellers 2015 acknowledges).
- Chang 2016 training effect: no outside replication found; effect shrank from 10-12% to 6-7%.
- Prompt-based analogues of the human findings (superforecaster persona, base-rate first) mostly failed in LLMs (Schoenegger 2025). The human lessons may not transfer to prompts; the transferable pieces seem to be aggregation, retrieval and recalibration.
- Scaffold-vs-plain comparisons from Metaculus bot makers are survey and rank data, not controlled at equal tokens (c18 is one bot).
- LLM benchmarks have leakage (Paleka: at least 3.8% and 10%) and small samples (31 questions; 39 supers; 10 experts).

## Seen only in snippets or second-hand

- Tetlock 2005 and Tetlock and Gardner 2015 (books): never opened.
- c16 (Brier Index / Good Judgment commentary): search summaries only.
- b28 (XPT): project page only, no accuracy numbers.
- c19-c21 (LessWrong synthesis of Metaculus posts): secondary.
- Chang 2016 and Mellers 2014 table values: from agents a and b, not re-opened by me.
- a25/c08 (AI-augmented): abstract plus partial read.
- Found by OpenAlex but not covered by any evidence line: "Superforecasting reality check: Evidence from a small pool of experts and expedited regression" (2020, PMC 7333631); Mellers et al. 2017 "How generalizable is good judgment? A multi-task, multi-benchmark study"; 2024 Psychological Science "Rethinking the Role of Teams and Training in Geopolitical Forecasting".

## GAPS (most decision-relevant first)

1. What is the real test-retest of a scaffolded LLM forecaster's Brier across two disjoint question sets, and how many questions are needed before a 6% Brier difference between two scaffolds is reliable (Lu: a noisier forecaster still wins 24% of 50-question tournaments)?
2. Does aggregation of several differently-prompted samples of the same model at equal total tokens beat one long chain of thought on resolved questions? (Teaming result K08 and LLM-crowd result K13 suggest yes, but no equal-token test exists.)
3. Does a running track record (per-domain Brier history) given to the agent help, as Himmelstein's "past performance beats traits after 20 questions" implies for humans, or does it only add noise?
4. Where does the .65 year-to-year correlation come from (Superforecasting p.104 footnote, which data, which years)? Is there a published primary source, e.g. Mellers 2017 "How generalizable is good judgment?" or the 2020 "reality check" paper?
5. What do the 2020 "reality check" and 2024 Psychological Science (teams and training) papers show about boundary conditions or non-replication of the training and teaming effects?
6. Was the Lu 2025 expert comparison redone with mean Brier on identical questions (later versions or FRI/Metaculus follow-ups)?
7. Which of the CHAMPS KNOW principles beyond comparison classes (e.g. granularity, updating frequency) transfer to an LLM as an operator without the persona/Bayes harm found in Schoenegger 2025? Does the harm come from pushing forecasts away from 0.5?
8. Do post-hoc extremizing and Platt scaling hold up on new LLM ensembles on held-out questions, and does the optimal extremizing factor drift (Baron 2014 fit was in-sample on one year)?
9. What are the primary-source numbers in Tetlock 2005 (experts vs baselines, fox vs hedgehog), to anchor the pre-GJP baseline?

## Gap search results

Evidence in evidence_d.jsonl (d01-d20). WebSearch was exhausted (shared budget), OpenAlex and Semantic Scholar rate-limited, so sources came from Europe PMC, Crossref, arXiv pages and PDFs, and the JDM journal PDF. Opened in full: PMC7333631 (reality check), Mellers 2017 JDM, Schoenegger 2025 prompt paper, Lu 2025, AIA Forecaster report, Diversity paper, Murphy 2026. Abstract only: Hauenstein et al. 2024, EvoForesight.

1. Test-retest and question count: PARTLY CLOSED. No one published a test-retest of a scaffolded LLM's Brier on disjoint sets. Murphy 2026: question difficulty is 62.2% of score variance, method 2.7%. My own power calculation (d19): a 0.01 Brier gap needs about 650-1,500 questions at paired SD 0.10-0.15 (fewer with 5-10 samples per question); 0.02 needs about 200-450. The Lu "24% win in 50 questions" figure is second-hand and untraced.
2. Aggregation vs one long chain at equal tokens: STAYS OPEN. Evidence for sampling 10x (AIA: .1182 single vs .1140 mean of 10) and for model diversity (Diversity paper, N=113), none at equal tokens against a long chain.
3. Running track record for the agent: STAYS OPEN. Only within-question memory (Murphy: compact state not worse, CI includes zero) and an abstract-level skill-distillation claim (EvoForesight).
4. Origin of .65 and 70%: STAYS OPEN. Mellers 2017 (opened) and the 2020 reality check have neither. Still only the 2015 book via AI Impacts. The 2020 paper is a small partial replication (2 of 195 at top 2%, no luck null).
5. Reality check 2020 and 2024 Psychological Science: CLOSED to the extent of abstracts. 2020: weak persistence replication, extra training no significant effect. Hauenstein et al.: IRT re-analysis says teaming and training effects shrink, vanish or reverse with method variables controlled. Effect sizes not read. K06 and K08 moved to contested.
6. Lu expert comparison redone: STAYS OPEN. No later version or follow-up found. Footnote: experts relabelled for trademark reasons; o3-pro hold-out .1307 verified (resolves the a27/c11 conflict). AIA gives a mean-Brier same-question comparison instead (AIA .1076 vs supers median .1110 on FB-7-21).
7. CHAMPS KNOW elements beyond comparison classes: PARTLY CLOSED. Only reference-class prompts (Base Rate First -0.016, Frequency-Based, Step-Back) survive correction in paired tests; K16 corrected (the earlier "none beat noise" was too strong). The Bayesian prompt harm is not explained by distance from 0.5 alone (Chain of Thought equally decisive, not significantly harmful). Granularity and updating frequency untested.
8. Extremizing and Platt on new ensembles: PARTLY CLOSED. AIA: fixed 1.73 gives .1119 to .1076; fitted on other data only .1104; best factor 1.72 (supers) vs 2.27 (LLM). Murphy: no resolved gain with a crowd price in context; shrinkage chose none. The factor is not stable and depends on anchors.
9. Tetlock 2005 primary numbers: PARTLY CLOSED. Only headline counts (284 experts, about 28,000 forecasts, 1984-2003) via Wikipedia; calibration and discrimination indices not obtained, book not opened.

New claims K23-K30 added; K06 and K08 contested; K16 corrected; K13, K10, K20 annotated. Open for a later pass: full text of Hauenstein et al. (which variables), equal-token test, track-record ablation, Neyman and Roughgarden 2022 (source of the 1.73 value), Tetlock 2005 tables.
