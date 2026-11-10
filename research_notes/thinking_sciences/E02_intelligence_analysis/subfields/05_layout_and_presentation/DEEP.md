# Layout and presentation: deep document

*Subfield E02.05 of intelligence analysis. Written 2026-11-10 from evidence_a-d.jsonl (100 evidence lines), claims.jsonl (K01-K30) and critique.md in this folder. Evidence ids (a01, b11, d05 ...) point to those files. Status marks: [E] established, [S] single source, [C] contested.*

## 1. What it is

The question: does the shape in which we show the same evidence to a thinker change what the thinker concludes? In intelligence analysis the shape is usually a matrix. Heuer's Analysis of Competing Hypotheses (ACH) puts hypotheses across the top and evidence down the side (a12). Each cell says consistent, inconsistent or irrelevant. The analyst works along rows (one evidence item against all hypotheses) and then down columns (one hypothesis against all evidence).

Rows against columns is the sharp form of the question. Same hypotheses, same evidence, same cells. Only the grid is turned.

Why it matters for our agent: in the schema, S4 TEST shows evidence and candidate answers to the model, and code builds that presentation. Code can choose orientation, order, serialization (Markdown, JSON, HTML), position of items, and whether the model scores cell by cell or per hypothesis. If layout steers strategy, this is a free lever. If it does not, we should stop tuning it.

The honest summary up front:
- The human claim rests on ONE study (Dhami et al. 2024, N=161). No replication found.
- No study has tested rows against columns on a language model.
- LLM work on tables and prompt format shows that layout, order and serialization move accuracy by a few to tens of points. That part is solid. It is indirect for our question.
- One 2026 pipeline (PRISM) shows an ACH matrix adds only +0.8 points over filtering and profiling.

## 2. History and theories in depth

**Larkin and Simon (1987).** Two representations can hold the same information and still differ in how cheaply you can compute with them. Grouping related items by place makes search and recognition cheap. This is the root idea: layout is a computation aid, not decoration. We could not open the paper (fetch failed, a17); it is background only.

**Payne, Bettman and the information-display tradition (1970s-80s).** In decision research, how a matrix is organised (by alternative or by attribute) steers the order in which people process it. People tend to process along the organised dimension. Memory only; we did not open these (b23). No numbers cited.

**Kleinmuntz and Schkade (1993), Schkade and Kleinmuntz (1994).** The cost-benefit view: a display is an incentive system. It makes some strategies cheap and others costly, so it changes which strategy people pick. Three features: organization (matrix or list), form (numbers or words) and sequence (sorted or random). In the 1994 study, 60 MBA students chose the best of 8 loan applications on 4 attributes. Organization had the strongest effect on information acquisition and effort. Form had the strongest effect on combining and evaluating. Only abstracts were read (a15, a16, d14, d15). Del Missier (2004, a14) reviews the theory: in his Experiment 1 (60 undergraduates), numeric encoding appeared in 73% of statements with a compatible graph and 20% with an incompatible graph (p=.009). These are attribute-choice tasks, not hypothesis testing. They support "layout steers strategy". They do not predict that hypothesis-in-rows wins.

**Heuer (1999), Psychology of Intelligence Analysis.** The matrix is externalization: working memory cannot hold many options and many attributes, so put them on paper (a12, a13). Use it for important or controversial judgments or when an audit trail is needed. Heuer gave no experiment on the layout. It is argument by worked example (a car purchase).

**ACH evaluation studies (2008-2020).** Small tests before 2024 (Lehner 2008, Kretz 2012 and others) used small samples (b22). Two randomized trials followed:
- Dhami, Belton and Mandel (2019) and Mandel, Karvetski and Dhami (2018): 50 UK analysts, half trained in ACH, 4 hypotheses, 12 evidence items. ACH-trained analysts did not follow all steps, were less internally consistent, and were no more accurate. 80% of the untrained control group redrew the text as an ACH-style matrix on their own (a10, b07, b09). Only the abstract was opened; the numbers come from the 2024 paper.
- Maegherman et al. (2020): 191 law students. ACH training did not beat a bias-information control on evidence search or likelihood ratings. About a third used the matrix; helpfulness rated 57/100 (b08, second-hand).

**Dhami et al. (2024), Cognitive Research: Principles and Implications.** The first direct test of the layout itself. The authors state that no research had examined an ACH-style matrix with hypotheses in columns (b22). They gave three possible reasons why hypotheses-in-rows might help, none tested (a09, b04, b26):
1. Sequential processing of one hypothesis at a time uses less working memory.
2. Horizontal eye movement dominates human vision.
3. Reading runs left to right.

They also argue that cell-by-cell scoring in the ACH layout hides dependencies between evidence items (b20, argued, not tested).

**LLM line (2023-2026).** Three separate strands, none about hypotheses:
1. Table understanding: serialization, transposition, shuffling (Sui 2024, Liu 2023, Deng 2024, Li 2023, Ashury-Tahan 2026).
2. Prompt format sensitivity: separators, Markdown or JSON, answer-first schemas (Sclar 2024, He 2024, Tam 2024, Brittlebench 2026).
3. Order and position: premise order, lost in the middle, option-ID bias (Chen 2024, Liu 2024, Veseli 2025, Zheng 2024).

Plus two reasoning-adjacent items: PRISM (ACH matrix inside an LLM pipeline, 2026) and Failing to Falsify (LLMs choose confirming tests, 2026).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Layout changed confirm-only strategy in humans; only hypotheses-in-rows reduced it | N=161 (HypCol 55, HypRow 51, HypText 55); chi2(2)=9.43, p=.009, phi=.24; post hoc HypRow p=.003, HypCol p=.327, HypText p=.048. Derived rates confirm-only: 61.8% / 39.2% / 67.3% (counts 34/55, 20/51, 37/55) | Dhami 2024 (a01, a03, b01, c01) | [S] single study. Per-layout percentages unverified: not in the page text and not on OSF (d01, d03) |
| Overall confirm-only choice in students | 56.5% chose A (confirm-only), 43.5% chose B. Label validity: chi2(2)=28.85, phi=.49; 74.6% of A-choosers said they used consistent evidence only | Dhami 2024 (a02, b03) | [S] |
| Layout did not change credibility sensitivity | Switched on 3B: 77% HypCol, 78% HypRow, 75% HypText; chi2(2)=0.15, p=.927. Excluded for picking B in 3A: 18%, 15%, 35% | Dhami 2024 (a04, b02) | [S] |
| Layout did not change judgment coherence | Deviation from additivity M=17.59; layout F(2,160)=1.22, p=.299 | Dhami 2024 (c24, a08) | [S] |
| Analysts in the ACH layout mostly balanced evidence | N=62 Dutch analysts and cadets: CONS 19.4%, INCONS 14.5%, BAL 66.1%. Credibility sensitive: BAL 98%, CONS 72.7%, INCONS 33.3% | Dhami 2024 Study 2 (a06, a07, b05) | [S] no layout contrast |
| Cognitive reflection (CRT) predicted strategy in students, not analysts | Students CRT 0.27 vs 0.81, t(116)=3.88, d=0.54. Analysts 2.25 vs 2.34, t(60)=0.30, d=0.10. Group means 0.51 vs 2.32, d=2.05 | Dhami 2024 (a05, b06) | [C] fails within-paper replication across samples |
| 2016 pilot, single matrix with hypotheses as columns | N=64; Task 1: 48.4% chose A; strategy 47.6% CONS, 47.6% BAL; 67.2% credibility-sensitive | Belton and Dhami 2016 (d02-d04) | [S] human reference rate: 45-60% confirm-only on Task 1 |
| ACH training: no clear benefit | 50 analysts: ACH-trained less consistent, no more accurate; 191 law students: no gain, one third used the matrix | Dhami 2019; Maegherman 2020 (a10, b07, b08) | [C] two RCTs, mixed, second-hand |
| Serialization changes table accuracy (GPT-3.5) | Size detection: HTML 67.00% vs NL+sep 42.00%, Markdown 40.67%, JSON 42.67%, XML 43.67%. Column retrieval HTML 63.33% vs Markdown 35.33%. Best average 65.43% (HTML). TabFact HTML 71.33 vs Markdown 68.40 | Sui 2024 (a18, b10, c05) | [S] 300 samples per task; 2023 models |
| Transposing and shuffling a table hurts | WikiTQ, 837 questions. Direct prompting: original 59.50; shuffle 52.21 (-12.25%); transpose 51.14 (-14.05%); both 37.51 (-36.96%). Python agent: 55.91; shuffle 47.91 (-14.31%); transpose 12.45 (-77.73%); both 8.96 (-83.97%) | Liu 2023 (a20, c07; b11 had the labels swapped, corrected in critique) | [S] GPT-3.5 only |
| LLM cannot see a bad orientation; a normalizer fixes it | GPT-3.5 right on 32.54% of transposed tables; said "no transposition needed" for 93.35% of originals. With NORM: 58.66 direct (original 59.50); agent 52.45 | Liu 2023 (a21, b12) | [S] |
| Prompt format moves accuracy | Up to 76 points (LLaMA-2-13B); GPT-3.5 up to 56 points, median spread 6.4; median task spread 7.5 points. Size, shots, tuning do not remove it | Sclar 2024 (a23, b15, c10) | [E] Sclar, He and Brittlebench agree in direction |
| Best format differs by model | GPT-3.5 prefers JSON, GPT-4 Markdown. Top-template overlap (IoU) across series often below 0.2. Only 16% identical GPT-3.5 answers Markdown vs JSON | He 2024 (a22, c04) | [E] with ToRR (d10): no format wins |
| Premise order matters | R-GSM: GPT-4-turbo 94.1 to 85.0; PaLM 2-L 86.4 to 79.5; Gemini Pro 80.5 to 69.1; GPT-3.5 67.3 to 51.8. Logic: up to 20-30% loss | Chen 2024 (b16, c11) | [S] synthetic tasks |
| Lost in the middle | GPT-3.5 closed-book 56.1%, oracle 88.3%; middle position drops over 20%, below closed-book at 20-30 documents | Liu 2024 (a24, b17, c12) | [C] newer work shows model-specific effect |
| Position effect is model-specific in 2025-2026 | Veseli: U-shape strongest up to half the window. 2605.23170: GSM8K middle minus end -94 points (Qwen2.5-7B, 64K), no drop for DeepSeek-V3.2. N=50, one seed | Veseli 2025; 2605.23170 (d11, d12) | [C] |
| Option-ID bias | llama-30B picked A/B/C/D 34.6/27.3/22.3/15.8% (250 answers per slot); moving gold to A lifted vicuna-33B 57.0 to 68.2, to D gave 41.2 | Zheng 2024 (b18, c13) | [S] multiple choice |
| Structured output hurts reasoning | 100% of GPT-3.5 JSON-mode answers on Last Letter put the answer key before the reason, so no chain of thought; one setting showed a 38.15% gap | Tam 2024 (c09) | [S] |
| Text vs image tables: no winner | GPT-4 63.8% avg, GPT-3.5 55.2%, Llama-2-70B 50.0%. Text wins on WikiTQ and TabFact; image helps GPT-4 on FinQA. Gains under about 4 points | Deng 2024 (b13, c08) | [S] row-colour numbers inconsistent between lines, do not cite |
| Vanilla GPT-3.5 fails table-structure tests | Failed up to 74% of missing-cell tests on 1,000 tables | Li 2023 (c14) | [S] |
| PRISM (ACH inside a pipeline) | MuSR, 10 LLMs: Direct 58.1, CoT 57.2, Persona 58.2, P-CoT 58.0, SC(5) 63.2, PRISM 71.3 (+13.2; range +6.0 to +22.0). Filtering only 63.8; +MOMA 70.5 (+6.7, 89% of gain); +ACH 71.3 (+0.8, 11%) | Lee, Kang, Shin 2026 (a26, a27, c15, c16, c25) | [S] one preprint, one benchmark |
| LLMs favour confirming tests | 11 LLMs, Wason 2-4-6 game; success 6% to 78%; I:C ratio correlates with success (rho 0.341, p=0.021 in a controlled setting); Dual-Goal helps in 8 of 11 setups; rule discovery 42% to 56% | Jhaveri 2026 (a25, d05, d06) | [S] test selection, not layout |
| CoT barely removes format brittleness | Brittlebench: Claude Opus 4.5 perturbation drop 2.79% to 2.38%; perturbations explain up to half of variance; ranking flips in 63% of cases; McNemar chi2=787.71 over 83,870 questions | Romanou 2026 (d08, d09) | [S] typos and spacing, not layout |
| Format spread on reasoning models for layout | No study found | d20 | Gap |
| Evidence-graph pipeline for analysts | F1 0.65 to 0.81, 0.72 to 0.78, 0.56 to 0.65 on three datasets | Yousuf 2024 (c19) | [S] |
| Holistic vs analytic LLM scoring (essays) | QWK holistic 0.533-0.601 (Llama 70B); analytic 0.321/0.235 (ELLIPSE), 0.414/0.394 (DREsS) | arXiv 2604.00259 (d16) | [S] other domain |

## 4. Mechanisms and models

Six mechanisms are on the table. Each is described so an engineer can build or ablate it.

**4.1 Strategy steering by grid axis (display-organization theory).** The grid makes one traversal cheap. In hypotheses-in-rows, the cheap traversal is "read one hypothesis end to end". In hypotheses-in-columns (ACH), the cheap traversal is "read one evidence item across all hypotheses". The first favours per-hypothesis tallies, including counting the inconsistent items. The second favours item-by-item scoring and, per the authors, tallying consistent cells. Implementation for an agent: pick the traversal, then render so that traversal is a contiguous block of text. For a language model the "cheap traversal" is contiguity in the token stream, not eye movement. Serialize row by row. If hypotheses are rows, the text for hypothesis 1 is one line. This is testable and cheap.

**4.2 Working-memory externalization (Heuer).** The matrix replaces a mental running tally. For an LLM the context already is the external store, so the benefit is different: code can compute the tally. Mechanism to implement: the model fills cells with local one-pair judgments; code counts inconsistent cells per hypothesis and ranks (ACH-Grounding design, c18, no results; practitioner ACH in separate calls, c17, no numbers). This matches schema rule G5 (code selects).

**4.3 Processing order versus layout.** Rows-in-layout may simply force one-hypothesis-at-a-time reading. If so, the effect is about order, not geometry, and can be got with sequential per-hypothesis calls on any layout. Test: sequential per-hypothesis calls vs one-shot matrix at equal tokens. Nobody has run this (d18).

**4.4 Position and order priors in the model.** Models have token and position priors: favour first and last, favour option IDs A and B, prefer forward order of premises (b16, b18, b17). Mechanism to implement: randomize hypothesis order and labels per run and vote in code, or put decisive evidence at the edges. Option-ID bias is mostly a token prior on the ID (Zheng), so relabel (use neutral names, not A-D) and permute (PriDe-style).

**4.5 Format as a hidden variable.** Format sensitivity is a variance source, not a bias to be cured by one best format. Mechanism: report a range (FormatSpread-style) over a small set of equivalent formats (3 to 5 serializations), choose per model by a pilot, and never copy across models (IoU below 0.2). A layout-normalising step (detect orientation, transpose to canonical row form, sort rows) recovered the table loss in Liu 2023 (58.66 vs 59.50).

**4.6 Output schema ordering.** Force reasoning before the verdict. If the output schema lists "answer" before "reasoning", the model answers directly (100% of GPT-3.5 JSON-mode cases, Tam). Input structure helps parsing; output structure can hurt reasoning. Separate the two: free-text reasoning first, then code or a short second call fills the structured table.

## 5. What holds up

**Holds up (two or more sources, or clear mechanism):**
- LLM accuracy depends on meaning-preserving format changes. Sclar (up to 76 points, median spread 7.5), He (up to 40%, GPT-3.5), Brittlebench (up to 21% average drop, ranking flips in 63%), ToRR (no format wins; Kendall's W rises by more than 0.35 from 1 to 10 prompts) agree. [E]
- The best format is model-specific. He (IoU below 0.2), Sui (HTML for GPT-3.5), He (Markdown for GPT-4), Deng (no text/image winner). [E]
- Order matters for deduction (Chen) and for choosing among options (Zheng). Weaker models lose more in Chen and He, but Sclar found no shrink with size. [mixed]

**Did not hold or is contested:**
- Row advantage in humans: single study, not preregistered, students (90.1% female, mean age 20), 2 hypotheses, one decisive task (Task 1). HypText was borderline (p=.048), so the text-versus-matrix difference is not clean. 35% of the text group were excluded from the credibility analysis against 15-18% elsewhere.
- Confirmation bias depends on the sample: students 56.5% confirm-only, analysts 19.4% (Study 2 had no layout contrast). So "layout fixes bias" may be a student effect.
- CRT link: students yes (d=0.54), analysts no (d=0.10). Floor effect in students (mean 0.51 of 3).
- ACH training for humans: two RCTs, no clear gain; one suggests lower coherence. Matrix use was voluntary and partial.
- Lost in the middle: strong for 2023 models; 2025-2026 work shows it is model- and filler-specific, and DeepSeek-V3.2 shows no drop. N=50 per cell, one seed, five API stacks (d12).
- ACH matrix inside an LLM pipeline: +0.8 points. The gain came from filtering and profiling (attention quality), not the grid.
- Transposing: big effect for the code agent (-77.73%), modest for direct prompting (-14.05%). Shuffle and transpose are about equal for direct prompting.

**Interventions that worked:**
- Row-per-hypothesis layout (humans, one study).
- HTML table serialization for GPT-3.5 on structure tasks; self-augmented prompting (+0.84 to +5.68 points).
- NORM layout normalization (tables).
- Evidence filtering and profiling before judging (PRISM: 58.1 direct to 63.8 filter only to 70.5 with profiling).
- Dual-Goal prompting for test choice (8 of 11 setups).
- Permutation-based debiasing of option IDs (PriDe).
- Mixture-of-formats few-shot (Ngweta 2025): a different format per example cut spread, e.g. Llama-3-70B task1347 0.276 to 0.071; no gain on one task (0.035 vs 0.037). Older and small models, no CIs.

**Interventions that did not work or were weak:**
- ACH training for humans (no accuracy gain).
- Chain of thought against format brittleness (2.79% to 2.38%).
- Row colour in table images (inconsistent; model-specific).
- Self-consistency: 5 samples gave 63.2 vs structured 71.3 in PRISM. Voting does not fix a shared attention problem.
- Prose per hypothesis as a layout: no better than the ACH matrix.

## 6. Language models

What we know about LLM behaviour here, by question.

**Does serialization matter?** Yes, mostly for structure-reading tasks, much less for downstream QA. HTML gave 67.00% on size detection against 40.67-43.67% for Markdown, JSON and XML (GPT-3.5); on TabFact the spread is 68.04 to 71.33, a few points (b10). He reports up to 40% variation on code translation, but these are relative changes from low bases.

**Does orientation matter?** Yes. Transpose cost direct prompting 14.05% relative and a Python agent 77.73% (GPT-3.5, WikiTQ, 837 questions). The code agent assumes row-form tables. The model could not tell: it identified 32.54% of transposed tables correctly. Implication: any code that touches the S4 matrix must fix orientation itself, not trust the model.

**Does order matter?** Yes. Forward order is best (Chen). Shuffling costs GPT-4-turbo 9.1 points on R-GSM and GPT-3.5 15.5.

**Does position matter?** Mixed. Strong in 2023, model-specific in 2025-26, and tied to retrieval: if the model finds the item, reasoning follows (Veseli: Qwen-2.5-32B 0.38 to 0.82 when retrieval succeeds). Our S4 tables are short, so this matters less than for long documents. Not tested on short tables with frontier reasoning models.

**Do bigger or reasoning models escape?** Partly. Chen and He show stronger models lose less. Sclar finds no shrink with size. Brittlebench: CoT lifts accuracy but removes only a sliver (McNemar: 4.1% CoT-right/non-CoT-wrong vs 1.7% reverse; interaction beta=.007, p=.006). Single frontier model for the CoT test. No reasoning-mode study varies layout.

**Does output format matter?** Yes, in the other direction: forced JSON or XML lowers reasoning accuracy; answer-first schemas remove chain of thought (Tam).

**Do LLMs show confirmation bias like humans?** Jhaveri 2026: all 11 favour confirming tests in rule discovery; reasoning-trace models show less. Dual-Goal prompts raised discovery from 42% to 56%. This is test choice, not layout. Nobody has run Dhami Task 1 on an LLM.

**Does an ACH matrix help an LLM?** PRISM (2026, 10 models, MuSR): full pipeline 71.3 vs 58.1 direct. The matrix itself added +0.8. GPT-5.2 went 58.0 to 80.0. CoT lowered accuracy for some models (Mixtral-8x7B -4.8, Qwen3-14B -2.0). The matrix is built by the model, orientation not varied, one benchmark.

**Does decomposing hurt?** Nearest data (essay scoring, open models): holistic agreement with humans QWK 0.53-0.60; trait-by-trait 0.2-0.4. Suggestive only, different task.

**Tool and agent studies.** An evidence-graph agent for analysts (Yousuf 2024) raised F1 by 0.06 to 0.16 over clustering baselines. ACH-Grounding (code ranks, model fills cells) has no results. Practitioner ACH in separate calls (c17) has no accuracy numbers; the wiki calls single-prompt ACH a failure mode (their reading, not a measurement).

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Never trust one prompt format. Report a range over 3 to 5 equivalent formats for any benchmark claim about the scaffold (FormatSpread style) | G7 / O7 variance note | [E] | K11; a23, b15, c10, a22, b14, d07, d08, d10 |
| Choose the serialization per model with a small pilot; never copy a format across models | S4 | [E] | K12; a22, c04, a18, d10 |

Cheap, harmless safeguards that are not yet [E] but cost almost nothing. Adopt as defaults, not as claims:

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Fix orientation and row order in code before any code or model reads a table. Do not rely on the model to detect a transposed table | S4 | [S] | K09, K10; a20, a21, b12 |
| Randomise order of hypothesis labels across runs and vote in code; use neutral labels, not A-D | S4 / G5 | [S] (option-ID bias is [E]-like for multiple choice only) | K15; b18, c13, b16 |
| Keep reasoning before the verdict in the output; never use an answer-first structured schema for the reasoning step | S4 | [S] | K16; c09 |
| Do not make a cell-by-cell ACH matrix a mandatory step on the strength of the human literature | G7 | negative: no direct evidence of benefit | K07, K18; b07, b08, a27 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Hypotheses-in-rows vs columns vs prose for the S4 evidence table (Dhami Task 1 port) | S4 | [S] | K01, K20; a01, b01, b25 |
| Sequential per-hypothesis calls vs one-shot matrix (order vs layout) | S4 | [S] | K06, K29; b04, b26, d18 |
| Holistic per-hypothesis scoring vs cell-by-cell scoring | S4 / G5 | [S] | K21, K30; b20, c24, d16 |
| Evidence ordered in proof order vs random | S4 | [S] | K13; b16, c11 |
| Decisive evidence at start/end vs middle in short tables | S4 | [C] | K14; d11, d12 |
| Layout-normalizing step before S4 | S4 | [S] | K10, K30; a21, b12, d19 |
| Disconfirming-test instruction (Dual-Goal) at S4 | S4 / G3 | [S] | K25; a25, d05, d06 |
| ACH matrix step on ARC and BrainTeaser items | S4 | [S] | K18, K19; a27, c16, c25 |
| Free-text reasoning then code-built structured table vs structured-only output | S4 | [S] | K16; c09 |
| Evidence graph store vs flat table for evidence | S2 / memory | [S] | K23; c19 |

## 8. Concrete tests on our bench

Rule for all: both arms get the same total tokens (setup counted, G7). Use at least 3 seeds and 5 or more equivalent prompt wordings, because format spread alone can be several points. Report a range, not one number.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Port of Dhami Task 1 (2 hypotheses, 12 evidence items; consistent count favours A, inconsistent count favours B) plus Tasks 3A/3B, 30+ item variants | HypRow vs HypCol vs HypText, same cell content, same model | Share choosing B (balanced); credibility switch rate in 3B | Human: B 60.8% vs 38.2% vs 32.7% (unverified). Expect a smaller gap for a strong model, 0 to 15 points. Switch rate unchanged |
| T2 | Same items, varied to 3-6 hypotheses and 12-30 evidence items | Row vs column layout at each size | Correct best hypothesis, B-choice rate | Tests whether the effect scales; direction unknown |
| T3 | T1 items | (a) one-shot matrix; (b) one call per hypothesis then code tally; (c) one call per evidence item then code tally | Accuracy against known answer; tokens | If (b) matches HypRow, the effect is order, not layout |
| T4 | BrainTeaser and ARC items with a candidate list | Candidates shown as a table in rows, columns, and prose; 3 serializations (Markdown, JSON, HTML) | Final accuracy at S7; spread over formats | 1-5 point swing between formats; use as a per-model pilot |
| T5 | MuSR-style or own mystery items | Filter and profile only vs plus matrix vs plus matrix with orientation swapped | Accuracy | PRISM: +0.8 for the matrix; expect 0 to 2 points |
| T6 | Items with one decisive clue | Decisive item at first, middle, last row of a 6-20 row S4 table | Accuracy; share citing the decisive item | 0 to 5 points for current models; drop if under 2 |
| T7 | Items with clues in proof order | Proof order vs random vs reversed | Accuracy | Up to about 10 points for weaker models; less for strong |
| T8 | Items with hypothesis labels | Labels A-D vs neutral names, with and without permutation vote | Accuracy; slot-choice distribution | Slot skew (e.g. 34.6/27.3/22.3/15.8) falls toward uniform |
| T9 | Any evidence-weighing item | Cell-by-cell scoring vs holistic per-hypothesis scoring (code aggregates) | Accuracy | Holistic equal or better; essay prior QWK 0.6 vs 0.3 |
| T10 | Items needing a disconfirming test | Plain vs Dual-Goal at S4 | I:C ratio of tests; success | Jhaveri 42% to 56%; expect less on stronger models |
| T11 | T1 items | Thinking on vs off, across 4 formats | Format spread (max minus min accuracy) | Spread shrinks little (Brittlebench 2.79% to 2.38%) |
| T12 | Code-execution mode on tables | With and without orientation normalizer | Accuracy | GPT-3.5 transposed drop was -77.73%; expect smaller on newer models |

## 9. What does not transfer, and why

- **Eye movement and left-to-right reading.** A model has no eye. It reads a token stream. Geometry matters only through contiguity in the serialization. The horizontal-vision argument cannot carry over.
- **Student confirmation bias.** The human bias (56.5% in students, 19.4% in analysts) depends on sample. An LLM's bias comes from priors and instructions. We cannot assume the row effect exists.
- **CRT link.** CRT predicted strategy in students only. An analogue (reasoning effort) is a guess.
- **ACH training results.** Training effects are human learning effects. For the agent the matrix is just a prompt step.
- **Working-memory relief.** A model's context is already the store. The matrix helps humans hold items; for a model the gain, if any, comes from forced attention and code-made tallies, as PRISM suggests.
- **Attribute-choice display studies.** Choosing among alternatives described by attributes differs from weighing evidence for hypotheses.
- **2023-era table results.** GPT-3.5 and GPT-4 numbers on WikiTQ may not hold for current reasoning models. The -77.73% code-agent result is GPT-3.5 behaviour.
- **Images.** Image tables are model-specific and gains are under about 4 points; skip.
- **Fine-tuning fixes (Table-GPT, TAMO).** Outside a scaffold-only plan.
- **Lost in the middle at 20-30 documents.** Our S4 tables are short.

## 10. Open questions

1. Does hypotheses-in-rows vs columns change an LLM's confirm-only choice on Task 1, with and without reasoning mode? No study.
2. Is the row advantage processing order or layout? Untested in humans and LLMs.
3. Does the human effect hold with 3 to 6 hypotheses, more than 12 items, non-student samples, preregistration? No replication found by search on 2026-11-10.
4. What are the real per-layout counts? OSF holds only the 2016 report and a 64-row CSV with no layout column; request the raw data from the authors.
5. How large is format spread for current reasoning models on evidence prompts, and does thinking shrink it? Brittlebench covers typos only.
6. Does the ACH matrix add anything beyond filtering and profiling outside MuSR?
7. Does a layout-normalising step before S4 cut variance?
8. Does decisive-item position matter in short tables for frontier models?
9. Does cell-by-cell scoring harm dependency reasoning relative to holistic scoring?
10. Do the full texts of Schkade and Kleinmuntz (1993/94) predict the row advantage? Paywalled; only abstracts read.
11. Which of the three untested mechanisms (working memory, order, reading direction) is right? Only the order mechanism is testable on an LLM.

## 11. Sources

[V] = opened and read this session (per the evidence files). [M] = snippet or secondary only.

- [V] Dhami, Belton, de Werd, Hadzhieva, Wicke (2024) Effects of task structure and confirmation bias in alternative hypothesis evaluation. Cognitive Research: Principles and Implications. https://link.springer.com/article/10.1186/s41235-024-00560-y and https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00560-y (a01-a11, b01-b06, b20-b22, b25-b26, c01, c02, c24)
- [V] Belton and Dhami (2016) Technical Report, OSF. https://osf.io/download/efxqg/ ; CSV https://osf.io/download/ecyvm/ ; project https://osf.io/hcdp3/ (d01-d04)
- [V] Heuer (1999) Psychology of Intelligence Analysis. https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf (a12, a13)
- [V] Del Missier (2004) Properties of the decision environment and display organization in choice. https://iccm-conference.neocities.org/2004/proceedings/papers/DelMisser.pdf (a14)
- [M] Kleinmuntz and Schkade (1993) Information displays and decision processes. Psychological Science. https://www.psychologicalscience.org/journals/psychological-science/ (a15; d15 abstract page only)
- [M] Schkade and Kleinmuntz (1994) Information displays and choice processes. https://ideas.repec.org/a/eee/jobhdp/v57y1994i3p319-337.html (a16, d14)
- [M] Larkin and Simon (1987) Why a diagram is (sometimes) worth ten thousand words. https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1101_4 (a17; fetch failed)
- [V, abstract page only] Dhami, Belton, Mandel (2019) The analysis of competing hypotheses in intelligence analysis. https://strathprints.strath.ac.uk/69049/ (b07)
- [M] Maegherman, Ask, Horselenberg, van Koppen (2020), via the 2024 paper (b08); Mandel, Karvetski, Dhami (2018), via the 2024 paper (b09)
- [M] Information-display classics (Payne 1976; Bettman and Zins; Jarvenpaa 1989), from memory (b23)
- [V] Sui, Zhou, Zhou, Han, Zhang (2024) Table Meets LLM. https://arxiv.org/abs/2305.13062
- [V] Liu, Wang, Chen (2023) Rethinking tabular data understanding with LLMs. https://arxiv.org/abs/2312.16702
- [V] Deng et al. (2024) Tables as Texts or Images. https://arxiv.org/abs/2402.12424
- [V] He et al. (2024) Does prompt formatting have any impact on LLM performance? https://arxiv.org/abs/2411.10541
- [V] Sclar, Choi, Tsvetkov, Suhr (2024) Quantifying language models' sensitivity to spurious features in prompt design. https://arxiv.org/abs/2310.11324
- [V] Liu et al. (2024) Lost in the middle. https://arxiv.org/abs/2307.03172
- [V] Chen, Chi, Wang, Zhou (2024) Premise order matters in reasoning with LLMs. https://arxiv.org/abs/2402.08939
- [V] Zheng et al. (2024) LLMs are not robust multiple choice selectors. https://arxiv.org/abs/2309.03882
- [V] Tam et al. (2024) Let me speak freely? https://arxiv.org/abs/2408.02442
- [V] Li et al. (2023) Table-GPT. https://arxiv.org/abs/2310.09263
- [V] Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to falsify. https://arxiv.org/abs/2604.02485
- [V] Lee, Kang, Shin (2026) Make LLMs see like investigators (PRISM). https://aclanthology.org/2026.acl-long.1056
- [V] Roberts (2025) LLM SATs FTW, sats4llms wiki. https://mattdot.github.io/sats4llms/concepts/analysis-of-competing-hypotheses
- [V] suprathermal (2024) ACH-Grounding. https://mattdot.github.io/sats4llms/sources/suprathermal-ach-grounding-2024 (c18 opened; d17 snippet)
- [V] Yousuf et al. (2024) LLM augmentations to support analytical reasoning over multiple documents. https://arxiv.org/abs/2411.16116
- [V, abstract and introduction only] Zhong et al. (2026) Before the Action: prospective hypothesis discovery. https://arxiv.org/abs/2607.15766
- [V] Ngweta et al. (2025) Towards LLM robustness to prompt format styles. https://arxiv.org/abs/2504.06969
- [V] Romanou et al. (2026) Brittlebench. https://arxiv.org/abs/2603.13285
- [V] Ashury-Tahan et al. (2026) The Mighty ToRR. https://arxiv.org/abs/2502.19412
- [V] Veseli et al. (2025) Positional biases shift as inputs approach context window limits. https://arxiv.org/abs/2508.07479
- [V] Positional failures in long-context LLMs (2026). https://arxiv.org/abs/2605.23170
- [M] Tian et al. (2025) Distance between relevant information pieces causes bias in long-context LLMs. https://preview.aclanthology.org/setup/2025.findings-acl.28 (d13)
- [V] Essay scoring under holistic and analytic prompts (2026). https://arxiv.org/abs/2604.00259
- [M] Tabular robustness papers. https://arxiv.org/abs/2406.12719 (d19, summary only)

Links to parallel subfields (not covered here): Cognitive bias and premature closure; Debiasing and cognitive forcing; Aggregation and extremizing; Cognitive artifacts; Choice architecture and nudging; Compression at inference time; Comparison and relational language.
