# Critique: D02.01 Bayesian conditionalization (cross-check)

## Corrections made (sources re-opened this session, PDFs from D:/research_scratch/D02.01)
Confirmed against the text:
1. Zhao et al. 2021: SST-2 4-shot permutation moved GPT-3 2.7B from 54.3% to 93.4%; contextual calibration up to 30.0 points. (b16 says "54% to 93%" and is consistent.)
2. Wang et al. 2023: GSM8K +17.9, SVAMP +11.0, AQuA +12.2 (table also shows +17.9 on a GSM8K-like row for code-davinci-002).
3. Zheng et al. 2024: gpt-3.5-turbo 67.2 to 60.9 (gold at D); llama-30B 53.1 to 68.2 (gold at A); 34.6/27.3/22.3/15.8.
4. Halawi et al. 2024: best no-retrieval Brier .208, crowd .149, random .250; full system .179, accuracy 71.5% vs 77.0%.
5. Qiu et al.: p = 0.002 for human improvement, Bayesian-tuned agreement about 80%, Bayesian Assistant final-round figure 81 appears in the figures.
6. Benjamin 2019: slope c-hat = 0.20 in the pooled data; correct posterior 94% for the 8a/4b card-deck problem.
7. Schulz et al. 2025: 36.2% vs 21.6% (OR 2.41), 4.9% vs 10.6% (OR 2.73), n = 329.
8. McCoy et al.: 51% vs 13% cipher decoding.
9. Cab problem Bayes answer 41%: recomputed, .12/.29 = 41.4%. Engineer-lawyer odds ratio (7/3)/(3/7) = 5.44: correct. Bookbag 0.967: recomputed, (7/3)^4 = 29.6, posterior .967: correct.

Corrections needed:
- c21 (Binz and Schulz): the line "answered 12 of 12 standard vignettes" is too strong. The paper says in 12 of 12 vignettes GPT-3 answered correctly OR made human-like errors; it answered only 6 correctly. On the cab problem it was approximately correct, but the authors also show it fails when the vignette is changed slightly (black cab gave "20%"). Treat the cab result as fragile, not as "GPT-3 has no base-rate fallacy".
- a15 vs b21: Gigerenzer and Hoffrage 1995 is reported as 16% vs 46% (a15, memory) and 48% vs 22% (b21, via the Cui review). Both cannot be the same statistic. Neither primary table was opened. Do not quote either number as the founding result until the 1995 paper is read.
- b01/b25: the headline slope 0.20 is a pooled number. For samples of size 2-6 the mean slope is 0.52-1.06, so "people move 20% as far as Bayes" overstates conservatism for small samples. Conservatism grows with sample size.
- a09: "43 percent as far as Bayes" is a distance in probability (.70-.50 over .97-.50), not in log-odds. In log-odds .70 is about 25% of the Bayes shift (0.85 vs 3.39). Use the log-odds figure when comparing to Benjamin.

## Not re-opened (still unverified)
- a28/b18 Mandel 2018 (35% and 61%): the journal page and PDF did not download in two attempts. The number rests on the repo's earlier claim file. The line "plain normalisation did as well as coherentisation" is the key one for G5 and is the most important gap.
- a12, a13, a14 (Kahneman and Tversky 1973, Bar-Hillel 1980, Casscells 1978: 11 of 60): from memory, opened:false.
- a29, a30 (Binz and Schulz title page, Griffiths 2023): title only.
- Qiu final-round range "36 to 58 percent" for off-the-shelf models is read from figures, not text.
- Ramsey, de Finetti, Lewis, Teller originals not read; credit taken from SEP.

## Contradictions and tensions between sources
- Natural frequencies: large benefit in 1995 and Binder 2015, mild in Yamagishi 2003, null in psychology students (OR 1.45, p = .22) and reversed for two sequential tests (Schulz 2025). The benefit is not general.
- Falck 2024 says LLMs violate the martingale property; Gupta 2025 and Arora 2025 say that with enough in-context evidence LLMs approach Bayesian posteriors or fit Bayesian scaling laws. These differ in model size, task and metric. Not a clean contradiction, but there is no study that tests both on the same model.
- b10/b11 say reasoning and step-by-step updates are near Bayes; Qiu says CoT did not help in the multi-round preference task. Task difference (verifiable likelihoods vs hidden user preferences) probably explains it, untested.
- Binz and Schulz (GPT-3 passes cab) vs Zheng/Zhao (huge prompt-order sensitivity): same direction of caution, passing a vignette is not evidence of coherent updating.

## Weak spots
- Almost every LLM-updating study is a preprint, uses 2B-70B open models, and one or two toy tasks (coin, die, flights). Only b10, b11 and Halawi use frontier models, and b11 has 40 runs per environment.
- b10 and b11 measure consistency against the model's OWN likelihoods, not truth. A model can be perfectly conditionalizing and still wrong.
- Nothing found tests the specific S7 operation: code normalising a model-given distribution over exclusive answers, versus the model's own stated distribution, at equal tokens. Only Mandel (human analysts, unverified) is close.
- No source tests elimination ("set to zero what the evidence rules out") separately from reweighting. Ratio preservation among survivors is assumed, never measured in LLMs.
- Claim K08 (Bayesian teaching) is training, outside a scaffold.
- Zero-probability handling (an eliminated answer later turns out right) is covered only in SEP; no LLM study.
- Only 2 of 19 claims have 3+ independent sources.

## GAPS (most decision-relevant first)
1. Does code-side normalisation of an LLM's raw option scores (G5/S7) improve Brier score or accuracy over the model's own stated probabilities, at equal tokens? Open Mandel 2018 and find any LLM replication.
2. Does hard elimination (set to zero) help or hurt compared with soft down-weighting when the model's evidence judgments are noisy? What is the error rate of an LLM's "this option is ruled out" call, and how costly is a wrong zero (SEP: no recovery from zero)?
3. Does presenting evidence one piece at a time (sequential, with code posterior) beat a batch update on frontier models, and does it hold outside the b10/b11 tasks? Replicate b10/b11 numbers.
4. How large is option-position and label bias on frontier 2025-2026 models, and does averaging over permutations before normalising remove it (Zheng 2024 used 2023 models)?
5. What does the primary Gigerenzer and Hoffrage (1995) paper actually report (16/46 or 22/48), and do natural-frequency restatements help current LLMs on Bayesian word problems?
6. How well calibrated are the verbalised likelihoods the agent would feed into the update (Tian 2023 is for answer confidence, not likelihoods P(E|H))? Find studies on elicited likelihood quality.
7. What is the best-supported handling of uncertain evidence (Jeffrey) in a scaffold, and is there any LLM study using it?
8. Are there 2024-2026 LLM studies on base-rate neglect with frontier models and adversarial variants (post Binz and Schulz), with numbers?
9. Does stating a prior in the prompt actually move frontier-model answers as Bayes predicts (Gupta 2025 found it did not for base models)?
10. Do multi-sample vote (self-consistency) and explicit normalised-probability aggregation differ at equal tokens on current models (Wang 2023 saw small gaps between them)?

## Gap search results (evidence_d.jsonl, d01-d18)

Search note: WebSearch quota ran out for most of the session and arXiv, Semantic Scholar and OpenAlex APIs returned HTTP 429, so discovery was limited. Papers were opened as full PDFs by id.

Closed
- Gap 1 (Mandel 2018): CLOSED for humans. Opened the full PDF. N=50 analysts; MAE 0.23 raw, 0.15 coherentized (35%, d=0.96), 0.09 after coherentizing and averaging all 50 (61%). Plain normalisation MAE 0.13, slightly better than the quadratic method (0.15). No LLM replication found, so "does normalising an LLM's raw scores help at equal tokens" is still untested (d01, d02, d09).
- Gap 5 (Gigerenzer and Hoffrage): CLOSED. Primary paper: Study 1 N=60, probability 16% (standard menu) and 28% (short menu), frequency 46% and 50%. 22 vs 48 is the menu average, so the a15/b21 clash was two views of the same data (d03, d04). LLM side: only one study found (Macmillan-Scott 2024), where the natural-count HIV version helped all models except Llama 2 (d05). No 2025-26 frontier test.
- Gap 3, partly: b10 was opened and CORRECTED claim K10. One-at-a-time updating is more consistent with the model's own likelihoods but does not give better task performance than batch (batch better or equal on 3 of 4 datasets; forced Bayes hurt on MediQ). b11 does compare against an external oracle posterior (not only self-consistency), but it tests reasoning and code, not one-at-a-time vs batch, with 40 runs per environment and mostly 26-35B models (d06, d07, d08). The "replicate b10 and b11" request was not met: no independent replication was found or run.

Partly answered
- Gap 2 (hard elimination): the only data are Balepur 2024: naming the wrong option is less accurate than naming the right one in all models; wrong zeros compound over rounds (70B loses a few points per round, 7B 20-30). 2023 models, 2-choice setup, table read from layout. No head-to-head of hard zero vs soft down-weighting (d11, d12, d07).
- Gap 6 (likelihood quality): b10 shows the model's own likelihoods are the weak part (about half of wrong-direction updates follow a better likelihood). QUITE shows word-valued premises are hard (8.7%). No direct calibration study of P(E|H) found (d07, d16).
- Gap 10 (vote vs normalised probability): Wang Table 1 shows vote and normalised weighted sum tie within 0.3 on PaLM-540B, but the weights are path probabilities and the model is 2022 (d10).
- Gap 9 (stated prior): Gupta reopened; only models up to about 8B; stated bias is outweighed by in-context data, instruction tuning helps (d18).

Still open
- Gap 4 (position bias on 2025-26 frontier models): Zheng 2024 permutation numbers confirmed (cyclic x4: llama-2-70B 50.8 to 54.7), but 2025-26 papers I opened (Guda 2025, PA-GRPO 2026) use 3B-32B models. No frontier-model measurement (d13, d14).
- Gap 7 (Jeffrey conditionalization in a scaffold): nothing found.
- Gap 8 (adversarial base-rate rewordings on frontier models): nothing new beyond Macmillan-Scott 2024 (GPT-4 and Claude 2 era) and Binz and Schulz 2022.

New cautions
- A scaffold that keeps a verbalised running differential (MAI-DxO, o3) beat plain o3 by 3.3 points (81.9 vs 78.6), but the Bayesian role was not ablated (d17).
- Code-side arithmetic is the best-supported piece: GPT-4 extract-then-ProbLog about 98% vs about 29% for CoT on BLInD (table layout garbled, figure approximate); reasoning plus Python closed an intractable-posterior case (d15, d08).
- Two numbers need a check against the PDF before quoting: Balepur Table 17 accuracies (d12) and the BLInD CoT average (d15).
