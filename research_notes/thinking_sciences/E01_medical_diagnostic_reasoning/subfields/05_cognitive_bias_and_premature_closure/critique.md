# Critique: E01.05 Cognitive bias and premature closure (cross-check)

Re-opened this session (abstract via Europe PMC, or full text via arXiv PDF): Graber 2005, Schiff 2009, Norman 2014, Mamede 2010, Sherbino 2014, Monteiro 2015, the 2026 premature-closure RCT (b17), Laban 2025, Nori 2025, Schmidgall 2024, Lou and Sun 2024.

## Confirmed
- Graber: 100 cases, 90 injury, 33 deaths, 548 factors in 93 cases (5.9 per case), system 65%, cognitive 74%, premature closure "single most common cause", knowledge "uncommon".
- Schiff: 669 reported, 583 kept, 162/241/180 severity, PE 26 (4.5%), testing 44%, assessment 32%.
- Norman 2014: 96 + 108 residents, 44.5% vs 45.0%, 69 s vs 89 s, wrong cases 17 s longer.
- Mamede 2010: 1.55 vs 2.19 (p=.03), 2.03 vs 1.42 (p=.046), 1.44 vs 0.72 (p=.04). Reflection numbers (2.03, 2.31) are in the cut-off text and were taken from earlier lines, not re-verified.
- Sherbino: 191 students (145/46), 52% vs 48% p=.91, 54% vs 48% p=.13, 64% vs 77% p=.12, 45% each p=.98.
- Monteiro 2015: 47 residents, 8% revised, 1.20 to 1.22, t=2.15 p=.03; 12/19, 9/11, 8/17.
- b17: 58 students, 0.27 vs 0.11 (61%), 0.17 (36%), F(2,693)=11.995, F(2,636)=4.799.
- Laban: 39% drop, CONCAT 95.1%, 30.9 vs 64.4.
- Nori: 78.6% at $7,850; 79.9% at $2,397; 85.5% at $7,184; 81.9% at $4,735; physicians 19.9% (20% in abstract).

## Corrections
1. a01 "about 4.3 cognitive instances per cognitive case" is my division; the paper's own figure is 5.9 factors per case (548 over 93 cases, system plus cognitive). Use 5.9.
2. Schmidgall drops (a18, b19, c01) are relative percentages of baseline, not points. GPT-4: 0.727 to 0.625 is 10.2 points = 14.0% relative. Wording "false consensus -14.0 points" should read "-14.0% relative (-10.2 points)". The same applies to the 24.9, 18.2, 12.9, 8.1 and 37.4 averages.
3. a18 "GPT-3.5 0.429 to 0.213" is a row mislabel from the garbled PDF table. The 0.429 baseline row belongs to another model (likely Llama 2 70B-chat). GPT-3.5 is 0.497 baseline (text: 49.7%) down to 0.239 under false consensus. PaLM-2 0.357 to 0.139 is consistent with the table.
4. c06 says Lou and Sun used a "small question set (15)". The paper uses 62 questions (plus 8 with irrelevant hints); the 15 is the number of expert-hint questions in the Both-Anchor figure. Both-Anchor worked on 8 of those 15 (nos. 5, 7, 8, 10, 12, 13, 14, 15), as c06 says. a17 and c06 now agree once read this way.
5. Nori: a19 says physicians 20%, c13 says 19.9%; both fine. a19 pairs "85.5%" with "max-accuracy mode" and c14 calls it Ensemble; the paper calls it ensembling. The unconstrained MAI-DxO is 81.9%, not in a19. The Instant Answer arm figure is still not captured (c15).
6. a08 names Norman as first author of the 2014 Acad Med trial; b09 and b08 list Monteiro as the author in the attribution. Author order was not verified on the page; cite as "Norman et al. 2014" only after a check.
7. Echterhoff: a16 says "400 prompts per experiment"; c04 says 13,465 prompts in total. These may both be right (per experiment vs dataset); not reconciled.

## Contradictions between sources
- Reflection: Mamede 2010 (structured reanalysis helps, experimenter-controlled) vs Monteiro 2015 (self-directed second look gains 0.02 of 2) vs Norman 2014 (exhortation null). Reconciled by structure and control of the reflection, but no study tests structure head-to-head.
- Lambe 2016 review says forcing improved accuracy; Sherbino 2014 and the ECG trial say null. The review is narrative and trainee-heavy.
- Strength vs bias: Schmidgall (GPT-4 loses less) vs Lou and Sun (GPT-4 and 4o more consistently anchored on numeric hints). Different bias types; not a real contradiction yet.
- Premature closure vs competition: b17 favours early stopping; no study found for experts.

## Weak spots
- Graber's central statistics rest on 100 selected cases, hindsight coding, no interrater figure. Many reviews cite "premature closure 12% of cognitive errors" as if general.
- Almost all human debiasing trials are trainees on written vignettes, small N, accuracy often near floor (45%, 27%).
- The LLM bias literature measures suggestibility to an inserted sentence (BiasMedQA, BiasBuster), not the model's own early commitment. Only SDBench, Laban and Hager touch real stopping behaviour, and Laban is non-medical.
- MAI-DxO anchoring evidence is by inspection of disagreements; Microsoft authors; no independent replication; no ablation.
- Ke 2024 uses cases selected for initial error, so improvement is partly regression to the mean.
- b21 and b22 are preprints (same group); the NEJM AI publication was not opened.

## Only seen in snippets or abstracts
Abstract only: a04, a05, a06, a08, a09, a10, a11, a22, b03, b04, b05, b07, b08, b09, b10 to b16. Not opened: a13 (Tversky and Kahneman, numbers from memory), a14, a15, a21 (Hager seen in c23 instead), b24, b25, c18, c21, c25, c26. Quotes from those lines were not re-checked.

## GAPS
1. Does an LLM stop investigating too early on common-disease cases? No published rate; build or find a staged benchmark with benign-looking leads (PE, ACS, stroke) and an Instant Answer vs full-investigation comparison. Also the Instant Answer accuracy from SDBench (figure only).
2. Which part of MAI-DxO carries the gain: the challenger, the hypothesis tracker, the cost stewardship or the checklist? Look for ablations or run one.
3. Does a challenger/recheck step harm cases where the first answer is right (flip rate on correct answers)? Ke 2024 only used wrong-first cases.
4. Does structured reanalysis (Mamede-style) beat generic reconsideration in an LLM at equal tokens, and does fresh-context re-derivation beat same-context reconsideration?
5. What does "Large language models exhibit greater diagnostic anchoring than physicians" (SSRN 2026) report? Open it; it is the most on-target LLM anchoring study and was unread.
6. Does the Goh UK replication (2026) and the Ke 2025 letter change the picture on human-LLM deference and multi-agent bias mitigation?
7. Replications of Graber's cognitive-share figures: newer audits (e.g. Singh/Schiff-style chart reviews 2015-2025) of how often premature closure is coded, with interrater agreement.
8. Has anyone replicated the b17 early-distractor result in experienced physicians, or tested the same order manipulation on LLMs (distractor first vs last)?
9. Do stopping rules based on stated confidence fail in LLMs (calibration subfield link)? Which signal (sample disagreement, open-test list, rival-set size) predicts wrong early stops best?
10. Missing 2025-2026 LLM work not reached (search budget): CRAFT-MD, MedR-Bench, Wang 2024 MCQ bias mitigation, Nguyen 2024 finance anchoring mitigation; verify their numbers.

## Gap search results
Evidence in evidence_d.jsonl (d01-d17). Sources opened: Nori 2025 full text (arXiv), Huang 2024, CRAFT-MD (medRxiv), MedR-Bench, Lopez 2026 (arXiv 2603.14158), SSRN anchoring abstract via Crossref. Others are search summaries (opened false).

- Gap 1 (LLM early stopping on common diseases): stays open. No published early-stop rate. MedR-Bench: free-turn questioning did not raise recall of needed examinations (R1 43.61 to 40.67), rare and common diagnosis comparable (d08). Instant Answer accuracy for SDBench is figure-only; not recovered.
- Gap 2 (which MAI-DxO part carries the gain): stays open. The paper has no role ablation; its only ablation is single vs batched mode (83.9% both, $3,991 vs $5,084) (d02, d03).
- Gap 3 (flip rate on correct answers): closed in part. Huang 2024 shows unguided self-review lowers accuracy (d05); Lopez 2026 measures susceptibility, 5.6-7.3% for GPT-5 variants up to near 100% compliance for conformist models (d10). No study on a diagnosis-specific self-challenger.
- Gap 4 (structured vs generic reanalysis, fresh vs same context): stays open. Indirect: ensembling 85.5% vs one panel 81.9% (d04); debate no better than self-consistency at equal samples (d06). No equal-token test of structured reanalysis.
- Gap 5 (SSRN anchoring): closed. LLMs 55.6% vs residents 21.2% vs attendings 10.0% ranking the planted anchor first, OR about 4 (d01). Abstract only; the model list and full methods were not read.
- Gap 6 (Goh UK, Ke 2025 letter): partly closed. Ke letter found (asks for single-LLM control; d13). Goh UK replication not found. Related: Lopez 2026 and Everett 2026 show AI anchoring on clinician input (d09, d12; the latter unverified).
- Gap 7 (newer audits of premature closure): stays open. Only reliability figures from snippets (ICC 0.52-0.72; 0.37) (d15).
- Gap 8 (b17 replication or LLM order test): stays open (d17).
- Gap 9 (which stop signal predicts early stops): stays open; indirect pointers only (d17, d11).
- Gap 10 (CRAFT-MD, MedR-Bench, Wang, Nguyen): CRAFT-MD and MedR-Bench opened and recorded (d07, d08). BiasMedQA 2025 follow-up, Nguyen and Wang not opened (d16).

Corrections listed earlier still stand (5.9 factors per case; Schmidgall drops are relative percentages). Claims K16, K17, K22, K13 were extended; K24-K29 added.
Data-source limits this run: OpenAlex free quota exhausted, arXiv API returned empty, Semantic Scholar rate-limited, SSRN page blocked.
