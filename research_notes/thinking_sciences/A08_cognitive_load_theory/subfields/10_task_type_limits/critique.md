# Critique: A08.10 Task-type limits (cross-check)

## Numbers re-opened this session (PDF text, pdftotext)
Confirmed:
- Sprague et al. 2025 (arXiv 2409.12183): symbolic +14.2, math +12.3, logic +6.9; top three 56.9 with CoT vs 45.5 without; others 56.8 vs 56.1; up to 95% of MMLU gain on "=" questions.
- Liu et al. 2025 (2410.21333): GPT-4o 87.50 vs 64.40 with CoT (-23.10, p<0.0001); on a 440 subset GPT-4o 94.00 vs o1-preview 57.70 = 36.3 points.
- Lin et al. 2026 HCoT (2604.12390): 24 Game ToT-BFS 758/1362=55.65% at 7.28M tokens; HCoT 497/1362=36.49% at 2.88M; IO 5.65%, CoT 9.54%; 1D-ARC GPT-4o ToT-prompt 47.61%.
- Zhang et al. (2510.01171): VS diversity 1.6-2.1x, +25.7% human score, 66.8% of base diversity.
- Li et al. 2026 (2511.16660): accuracy 62.4 / 51.7 / 57.5; humans 41% and models 26% fewer elements on ill-structured; +9.7 and +18.8 (dilemmas) for strong models; PPMI .217.
- Stechly et al. (2405.04776): GPT-4 3.83% zero-shot, 6.13% n-shot, 51.3% universal, 59.3% stacking.
- Wadinambiarachchi et al. (2403.11164): BF 124 for GenAI fixation.
- Li et al. 2024 (2407.02028): 160 question-response pairs; negative similarity correlation on open-form.

Corrections:
- Wadinambiarachchi fixation CI: a and b files say [.11, .54]; the paper says [.11, .55] (c file correct). Use .55.
- Liu o1-preview "36.3 points" is relative to GPT-4o on a 440-item subset (94.0 vs 57.7), not full set. a20 reads as if general; the full-set GPT-4o drop is 23.1.
- Not re-checked: "+4.4 (SE 1.2)" for all models in c16 (text did not match the grep; likely table formatting).

## Not re-openable
- Nievelstein et al. 2013 (the anchor): all numbers (a01-a05, b01-b03, c01-c02) are consistent across three agents, but the journal page and PDF were not re-opened by me (Crossref confirmed title and DOI 10.1016/j.cedpsych.2012.12.004 only; no abstract). Treat as single-source. n=9 per cell for third-years is small, so the "no reversal" finding is weakly powered.
- Rourke and Sweller 2009, Kyun et al. 2013, Schworm and Renkl 2007, Hilbert 2008, Reiss 2008, Hefter 2019, Marsh 1996 were seen only as abstracts, secondary text (Renkl 2023, Chen thesis) or not at all. Kyun sample sizes (63, 62) came from search summaries.

## Contradictions and tensions
- Human worked examples help on open tasks (Nievelstein), but LLM evidence says close examples can hurt open-form questions (Li 2024) and homogenize output (Padmakumar, Anderson, Wadinambiarachchi). Different mechanisms (learning vs generation), so no direct conflict, but the human result cannot be transferred to inference-time prompting.
- CoT on "soft reasoning" gives about +2 points (Sprague), yet Li 2026 scaffolding gives +9.7 on ill-structured problems for strong models. Different interventions (trace-order guidance vs plain CoT) and a GPT-4.1 judge; not comparable.
- Marsh 1996 says conformity to examples is real but modest; the AI studies find stronger effects. Population and task differ.
- Bichler 2022 re-analysis found no significant worked-example effect on self-explanation (p=.234, N=74), against the broader claim.

## Weak spots
- Human evidence for the core claim is basically one paper plus one lab family. No replication found; absence from OpenAlex/Semantic Scholar was partly due to rate limits (b25).
- Zero LLM studies test worked examples on ill-structured tasks directly. All LLM evidence is analogy via CoT, ICL or diversity.
- Many LLM results use 2022-2024 models (Min, Stechly, Li 2024); reasoning models may behave differently.
- Evidence files b contains invalid UTF-8 bytes (e.g. in author names); fix before parsing with strict readers.
- Claim K04 counts 3 sources but they are mostly one research network.

## GAPS (most decision-relevant first)
1. Does a worked example or analogous solved case improve a strong LLM on ill-structured tasks (case analysis, dilemmas, design) at equal tokens, versus solving cold? No study exists.
2. Is there an expertise-reversal analogue: at what model strength does an example or scaffold stop helping or start hurting on open tasks (Li 2026 shows weak models lose)?
3. Does the Nievelstein result replicate with larger third-year samples, or in other less-structured domains (medicine, ethics)? Any failed replication?
4. Which scaffold part carries the open-task gain: named heuristic steps (skill level) vs example content (topic level), tested on LLMs?
5. Do reasoning models (o1/R1 class) still show CoT-neutral or CoT-harmful behaviour on soft and implicit tasks, 2025-2026 replications of Sprague and Liu?
6. How should the agent classify a task as well-structured vs ill-structured at S0 reliably, and what is the cost of misrouting?
7. Can example-free diversification (stratified directions, verbalized sampling) beat example-fed ideation on open tasks at equal tokens in a multi-sample agent?
8. How many examples and which similarity level is best for open-form tasks (Li 2024 suggests distant beats near; no dose-response)?
9. Do process-step checklists without examples (Toulmin-style) help LLMs, given they did not help novices?
10. Individual-difference moderators (shifting, Gf in Bichler) have an LLM analogue? Does benefit depend on the model's baseline on the task?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d17; 13 opened as full text or HTML, 3 read as abstracts only, 1 citation scan). New claims K19-K25 in `claims.jsonl`; K05, K09, K11-K15 and K18 got extra evidence ids. Web search budget ran out, and arXiv and Semantic Scholar rate limits cut the search short, so some gaps may hold papers that were not found.

Closed or mostly closed:
- Gap 7 (example-free diversification): partly closed. NoveltyBench (d09) and Artificial Hivemind (d10): sequential regeneration with earlier outputs shown matched humans; system-prompt creativity requests did not; multi-model sampling gives little real variety (cross-model similarity 71-82%). Direct head-to-head of stratification vs verbalized sampling vs regeneration at equal tokens is still missing.
- Gap 5 (reasoning models on soft tasks): partly closed. Harm from more thinking in reasoning models is now shown on distractor tasks (d01), instruction following (d02) and diversity (d09, o3 effort). No 2025-2026 replication of Liu's implicit-learning result was found, and math still shows gains (d07). Status: contested.
- Gap 4 (skill vs content): partly closed. Narration-of-Thought (d05) shows named steps with no example carry their own effects (ablation); patent drafting (d03) shows the steps help only when not written out. Example content was not varied in either study, so skill vs topic is still not tested head to head.
- Gap 9 (checklists without examples): partly closed. For LLMs, step lists help (d03, d05) even without examples, unlike the novice-law-student null. Outcomes are weak (trace features; 80 human-rated items).

Still open:
- Gap 1 (worked example vs cold on ill-structured tasks at equal tokens): no study found. The nearest is d06, where open-ended sets gain 0-2 points on small models and up to 11 on one 14B model, judged by GPT-4.1.
- Gap 2 and 10 (expertise-reversal analogue, baseline moderators): directional evidence only (d07, d02, Li 2026), pointing both ways. No clean design on an open task.
- Gap 3 (Nievelstein replication): a scan of 93 citing records (d16) found none. Near-domain studies (d13, d14, d15) give a null (n=78), a partial effect (n=118, unaided skill not improved) and no reversal on transfer. K01 and K02 stay single-source. I still could not open the original paper.
- Gap 6 (S0 task classification): gates exist (d02, d11) but none splits well- from ill-structured, and misrouting cost for that split is unmeasured. Known costs: -16.2 points when CoT is wrongly applied (d02).
- Gap 8 (dose and similarity): structured-task curve peaks at 5-20 examples (d08); reasoning models prefer one-shot (d07) and copy near examples (d06). Nothing on open-form tasks or distant examples.

Caveats on new evidence: d13-d15 are abstract-level only. d12 was read through a fetch summary. d05's gains are measured on judge-coded trace features, not on decision quality. The 2026 arXiv papers (d03, d04, d05, d08) are preprints.

Next step for the build: the open-mode scaffold in the schema should use named steps, at most one abstracted example, hidden planning with a length cap, and a logged S0 route so misrouting can be measured.
