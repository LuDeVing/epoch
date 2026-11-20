# Critique: TRIZ with systematic design (E07.05)

Cross-check done 2026-11-19. Sources re-opened this session as full PDF text: TRIZ-GPT (arXiv 2408.05897), Trapp and Warschat (arXiv 2403.14258), AutoTRIZ (arXiv 2403.13002), TRIZBench (ACL Findings 2026), Ogot and Okudan 2006, Hernandez et al. 2012. Mohammadi and Zeng (2025) was spot-checked from earlier extracted text.

## Corrections made (10 numbers checked)

1. TRIZ-GPT recall 0.691 (CoT), 0.675 (basic), 0.245/0.247 (few-shot variants); 85.3% and 88.2% consistency; cosine 0.829 and 0.82x; post-cutoff recall 0.544 vs 0.400. All CONFIRMED.
2. AutoTRIZ: entropy scale 0 to 6.64, 7 of 10 cases match or half-match, battery +24%, +64%, +26%. CONFIRMED. Note: the improvement figures are the authors' own calculation (K19).
3. Trapp and Warschat: sentence recall 0.71, precision 0.46, F1 0.56, 3.19 false positives, 86 of 100 contradiction-free patents flagged. CONFIRMED. The paper's own Table 1 prints labels shifted (precision shown as 0.93), so the 0.93 headline in the abstract is the BERTScore. Evidence line c20 was right.
4. TRIZBench pair F1: evidence b15 said "0.29 to 0.42". The paper text says Gemini-2.5-Pro reaches 0.42 to 0.45 on cases. CORRECTION: range is 0.29 to 0.45. Best LoRA detection F1 is 0.90, above the 0.75 to 0.87 zero/few-shot range.
5. TRIZBench principle Hit@3: evidence b16 called 0.67/0.48 "retrieval". In Table 3 that row is the plain Matrix lookup (non-LLM). TF-IDF reaches 0.69/0.56. Zero-shot Qwen3-8B 0.39/0.27, Gemini ZS 0.45/0.31. M-Rerank 0.71/0.59 confirmed. CORRECTION: the finding is that non-LLM baselines match the LLM reranker within 0.02 to 0.03. This changes the lesson for the agent (K12).
6. TRIZBench also has a 5-case human/frontier calibration (Table 9): Sonnet-4.6 HasF1 1.00, pair 0.60; GPT-5.2 0.80/0.60; Gemini-3-Pro 0.50/0.40; TRIZ-familiar humans 1.00/0.60. Authors say not statistically robust. Not in earlier evidence; N is far too small to use.
7. Hernandez et al. 2012: p-values confirmed (novelty 0.0004, 0.0145, 0.5786; quantity 0.2879, 0.5409, 0.6291). CORRECTION: b01 said TRIZ "raised novelty"; novelty was significant at two of three sites only, and the authors call it a trend. Table order is garbled in the PDF, so per-site assignment stays uncertain.
8. Ogot and Okudan 2006: 8.94 vs 4.42 feasible concepts per team, 35 vs 16.3 solutions per section, 21 unique concepts, section means 8.38/9.50 vs 4.88/3.75/4.63. CONFIRMED. No significance test; quantity only.
9. Hernandez counts of sample sizes (UTEP 21 vs 9, Maryland 20 vs 21) were not re-found in the extracted text; treat as unverified.
10. Mohammadi and Zeng functional-analysis accuracy 0.56 to 0.59 and idea counts 20 vs 4, 7 vs 2, 18 vs 1-2 seen in the extracted tables. Consistent.

## Contradictions between sources

- Quantity: Ogot 2006 doubles feasible concepts; Hernandez 2012, Dumas 2016 (-19.3% fluency) and the 2022 TRIZ10 study (+178% ideas, N=13) disagree in direction. Units differ (feasible concepts per team vs ideas per person), so this is partly a measurement artefact.
- Novelty: gains reported (Hernandez, Dumas and Schmidt +30.8%), tiny gain (Chang +1.5%, N=121), so effect size ranges over an order of magnitude.
- Belski simple-ideation gains vs the Valentine 2017 null replication.
- LLM side: Mohammadi gives LLM-TRIZ more novelty than experts in 5 of 6 comparisons; Cok et al. 2026 found LLM did not help students on complex tasks; Ma 2023 found plain GPT-3 less novel than people.

## Weak spots

- The central claim (FDM has a creativity gap that TRIZ fills) has no direct experiment. The 2018 paper has no N and no control; the 2016 and 2019 group papers are cases and course suggestions.
- Human TRIZ studies are student, one-task, short-training, and quasi-experimental (whole sections).
- LLM studies compare to textbook solutions, which probably sit in training data; TRIZ-GPT's post-cutoff drop (0.691 to 0.544) is across different collections, not a clean test.
- Idea-count wins for LLM (Mohammadi) favour a generator against fixed textbook answers.
- Labels in TRIZBench are partly made by Gemini with human check (74% agreement pre-adjudication).
- Single-author-group dominance: AutoTRIZ numbers are all self-reported.

## Only seen in snippets or abstracts

b19-b25 (Valentine, Belski 2014/2015, Spreafico and Russo, neuro-cognitive study, Livotov, 102-student comparison), a19/a20 (abstract-level on first pass; TRIZBench since read in full here), a23, a24, a25, a27, a28, a26, c27. Treat their numbers as unverified.

## GAPS

1. Does a TRIZ-style step (contradiction naming, principle lookup) raise blind-rated novelty of a modern LLM agent at equal tokens versus plain decomposition plus brainstorming? No source tests this on a current model.
2. Is a code-fixed or retrieval-based lookup for principles (matrix, TF-IDF) as good as LLM free choice, and does the LLM add anything beyond reranking?
3. How often does an LLM claim a contradiction where none exists (86 of 100 in Trapp), and does an abstain option or second pass fix it?
4. Is the FDM creativity gap measurable at all: compare function-structure plus morphology against the same plus a task-questioning step (Frillici 2016 style) with human or LLM designers and a control.
5. Does the 2018 Problem-Solution Network (how-to problems co-evolving with solutions) beat plain functional decomposition in any experiment?
6. Quantity versus novelty trade-off: for an agent, does TRIZ cut idea count and at what token cost per novel idea?
7. Why do human TRIZ studies disagree in direction on quantity (Ogot vs Hernandez vs Dumas)? Training length, unit of analysis, or task?
8. Are LLM-TRIZ gains robust on post-cutoff problems (not in textbooks), and with independent raters and kappa?
9. Does multi-agent TRIZ (manager plus specialists) beat a single agent with the same chain once token budget is matched?
10. Does LLM help with the contradiction matrix improve human students on hard tasks (Cok 2026: participant N and statistics not yet read)?


## Gap search results (2026-11-19)

Sources opened this session: Cok et al. 2026 (page fetch, text summary), TRIZ Agents, TRIZa, TRIZ-RAGNER, text-to-CAD, Owen and Roberts poster, plus re-reads of AutoTRIZ, Trapp and Warschat and TRIZBench. The WebSearch budget was already spent, Semantic Scholar, OpenAlex and the arXiv API were rate-limited, and several publisher or host pages refused access. Evidence is in evidence_d.jsonl (d01 to d19).

1. Gap 1 (does a TRIZ step raise blind-rated novelty of a modern LLM at equal tokens): OPEN. Closest is the text-to-CAD study (Claude Sonnet 4.5, N=1 chair): vanilla prompt scaled dimensions, contradiction-named prompts changed structure (d05). No novelty rating, no replicates, no token match.
2. Gap 2 (code-fixed lookup vs LLM choice): MOSTLY CLOSED. TRIZBench shows matrix lookup 0.67/0.48 and TF-IDF 0.69/0.56 against zero-shot LLM 0.39 to 0.45 / 0.27 to 0.31, with rerank 0.71/0.59 (d11). AutoTRIZ uses code lookup (d10). Remaining hole: benchmark labels are inventors' principles, not best principles, and TRIZa has no ablation (d06).
3. Gap 3 (false contradiction claims, abstain, second pass): PARTLY CLOSED. The 86 of 100 figure is an upper bound because the labels are doubtful (d09). An abstain instruction is in every TRIZBench arm and detection F1 is still 0.75 to 0.87 (d08). Nobody tested abstain vs no abstain or a second pass.
4. Gap 4 (FDM creativity gap measurable): OPEN. Publisher pages blocked (d16); no source found. The LLM morphology paper (d12) is abstract-only.
5. Gap 5 (Problem-Solution Network vs plain decomposition): OPEN, same reason.
6. Gap 6 (quantity vs novelty, token cost per novel idea): OPEN. Only cost figure is 150k to 250k tokens per TRIZ-agent run (d04). No tokens-per-novel-idea figure.
7. Gap 7 (why human studies disagree on quantity): PARTLY ADDRESSED. Pattern across the tables: full course or per-team count gives gains, one lecture gives nothing or a loss (d14). Not tested, and Dumas and Chang are second-hand. Valentine and Belski PDFs were unreachable (d15), so K06 numbers stay unverified.
8. Gap 8 (post-cutoff robustness, independent raters, kappa): OPEN. No study found with all three (d17 to d19).
9. Gap 9 (multi-agent TRIZ vs single chain at matched budget): OPEN. TRIZ Agents has no single-agent control (d04); IdeaForge used a tiny model with no baseline.
10. Gap 10 (Cok 2026 N and statistics): CLOSED. N=113 (62 with LLM, 51 without), method effect p=.076, gain only on one of three problems whose group was AI-specialised, contradiction naming felt easier (d=-0.78) (d01 to d03). Cell means not read.

Claims changed: K17 rewritten with the numbers; K12, K13, K16, K20, K06, K03, K01 got extra evidence ids and caveats. New claims K21 to K27.
