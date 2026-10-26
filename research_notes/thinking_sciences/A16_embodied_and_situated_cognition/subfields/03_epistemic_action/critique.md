# Cross-check: A16.03 Epistemic action

Checked 2026-10-26. Sources re-opened this session (full text, pdftotext or Europe PMC XML): Maglio and Kirsh 1996, Cook et al. 2012, Croom et al. 2023, Nye 2021, PAL, Mind's Eye, ReAct, Huang et al. 2023, Lanham et al. 2023, Tree of Thoughts, Zeng et al. 2026, SLEUTH (Liu 2026).

## Confirmed without change
- Maglio and Kirsh 1996 (b01, b03): extra rotations 7% / 5% / 4% of episodes (expert / intermediate / beginner); target orientation reached at 676 ms (SD 149) and 754 ms (SD 296) with extra rotations vs 1127 and 1122 ms without.
- Cook et al. (b05): N=115, beta -.17 (z 3.23) and -.13 (z 2.61); first-condition-only p=.057 and .02. The 16 excluded gesturers are correct, plus one non-native speaker excluded (not noted before).
- Croom et al. (a14): 76.2% d=2.12; 65.9% d=1.53, 4/18 players correct; 63.69% d=0.86; 63.72%.
- Nye (a16, b14, c01): 8.8 / 20.1 / 31.8 / 50.7.
- Tree of Thoughts (a19): 7.3 / 4.0 / 45 / 74.
- Huang (c08): all GPT-3.5 and GPT-4 figures in the table match.
- Zeng (b24): 0.93, 3.29-14.48, 82.8%, 59.4% (6.83 to 2.77), 2.2 calls for Qwen3-8B.
- SLEUTH (c17, c18): 66.1 / 61.4 / 60.2, 4-hop 53.1 vs 42.0, Notes 41.7, adherence 15% to 99%, 29.9 to 48.9.
- ReAct (c06): ALFWorld 71 / 45 / 37, worst ReAct 48, relative gain 33-90% (mean 62%); failure table 56% vs 0% hallucination and 23% search error.

## Corrections made
1. Lanham AQuA (c24, c14): c24 says AQuA had an accuracy drop of -4.69% with low reliance on the chain. Wrong on both counts. The -4.69 is HellaSwag. AQuA has the highest area over the curve, meaning the LEAST post-hoc reasoning: the answer changes more than 60% of the time when the chain is cut, and CoT adds +15.32 accuracy. Claims K07 and K09 use the corrected reading.
2. PAL GSM-Hard (a17, c03): the paper contradicts itself. Text: CoT drops 65.6% to 20.1%, PAL 61.5%. Table 1: CoT 23.1%, PAL 61.2%. Table 7 averages: CoT 23.3, PAL 61.2. Both pairs are in the paper. Use "about 20-23% vs about 61%". c03's "CoT 23.1" is the table value, a17 is the text value, neither is wrong.
3. PAL ablation (new, important): the model writing code but then predicting the result itself ("LLM Simulating Runtime") solves 23.2% vs 72.0% for PAL and 19.7% for direct. Succinct single-line code gives 47.8%. Not in the evidence files; added to K06. It says the active ingredient is real execution, not code-shaped prose.
4. Mind's Eye (c10): the two gain figures are both in the paper. 27.9 / 46.0 is the last "Grounding Gain" column of the results table (zero-shot / few-shot); 18.4 / 34.2 is stated in the body as the average over model sizes. Not a typo, a different average. The paper also reports 10.3% few-shot gain for GPT-3 1.3B vs 46.0% for 175B, so the claim that small models "match big ones" holds in zero-shot only.
5. ReAct (c06): the table also has CoT-SC alone at 33.4 (HotpotQA) and 60.4 (Fever). That beats plain ReAct (27.4 / 60.9 on Fever only slightly lower). c06 left it out, which flatters ReAct. Best HotpotQA 35.1 is ReAct then CoT-SC; best Fever 64.6 is CoT-SC then ReAct.
6. SLEUTH gain per hop (c17): says +11.1 to +11.9. The table says +11.9 (2-hop), +10.4 (3-hop), +10.9 (4-hop) vs the best external baseline. Minor.
7. Cook (b05): "N=115" is correct but means after 16 exclusions for gesturing on no-gesture trials; exclusion rate is 12% and is a researcher choice.

## Contradictions between sources
- Rotation account vs preview account of Tetris expertise (K01 vs K03). Maglio and Kirsh 1996 say experts rotate more; Berry 2023 says elite play depends on the Next Box. Different players (2 learners vs elite tournament players) and different time pressures.
- Gesture helps (Cook, Dargue d=.61) vs gesture hurts (Overoye and Wilson, d=.34, N=40). Different tasks (factoring explanation, comprehension, verbal analogies).
- Written output helps on symbolic tasks (Nye, Wei, Sprague) vs hurts on implicit or perceptual tasks (Liu 2025, Lanham HellaSwag). Reconciled by task type, not contradictory.
- Interactivity effect: Kirsh-type theory predicts benefit, but Ross and Vallee-Tourangeau and Spiridonov find null aggregate effects (K20).
- Dot-by-dot: filler helps in trained small transformers (Pfau) but not in Claude 2 / GPT-3.5 (Lanham, Pfau's own commercial test).

## Weak spots
- The founding paper (Kirsh and Maglio 1994) was never opened by anyone. All Tetris numbers come from the 1996 paper (2 players) and Kirsh's summaries. The 150/200/300 ms external rotation times and the 1000-1800 ms mental rotation times differ across summaries; treat as unverified.
- The theory-to-LLM bridge is an analogy. No paper maps epistemic vs pragmatic action onto LLM tool use (c21). The two 2026 papers that use the word (Iris, SLEUTH) are single-run or single-author preprints.
- Iris ablation: 15 tasks, one run, a 6.7 point change equals one task.
- Several human-side results (b09-b12) are second-hand via Pouw et al. 2014.
- Most LLM gains are on Codex / PaLM / GPT-3.5 / GPT-4 era models. Modern reasoning-trained models were not the subject of Sprague, PAL, PoT, ReAct or Nye. Gains may be smaller now because the model already writes long traces by default.
- "Established" claims K05-K09, K13, K14, K20 rest on prompt-era benchmarks; none controls tokens, so the equal-token form of each claim is untested.
- Rios-Garcia 2026 (b25) and Sprague (b20, a28) could not be re-opened this session (PDF text extraction failed); numbers are from the A/B agents' reading and not re-checked.

## Seen only in snippets or abstracts
a01 (Kirsh and Maglio 1994, Crossref abstract), b09-b13 (second-hand), c15 (Wang et al. abstract page), a21, a22, a23, a29, a30 (abstract only), c22 (partial), c09 (Toolformer table assigned by row order), c12 and a24 (VoT tables interleaved; VoT 37.02 vs 37.17 CoT vs no-viz differ between files, same paper).

## GAPS (most decision-relevant first)
1. At equal tokens, how much of the gain from written intermediate steps on a current reasoning-trained model remains once the model already thinks at length by default, and does an extra scratchpad or run-code step add anything beyond the model's own hidden reasoning?
2. Does a gate ("what unknown does this action resolve, and why can I not resolve it in context?") reduce unneeded tool or code calls and keep accuracy, in a prompt-only form rather than the trained fixes tested by Zeng et al.?
3. Does trace ablation (delete or corrupt step k) predict which written steps are truly epistemic, and what fraction of steps in our own agent's S2/S4 traces pass that test?
4. Is the active ingredient of run-code-to-think the execution result or the planning discipline, and how does this change when the task cannot be turned into code (PAL simulating-runtime ablation says execution; Chain of Code suggests simulated execution still helps)?
5. Which task features decide when a forced write-out hurts (implicit statistical learning, perceptual, verbal analogies)? Is there a cheap pre-check that routes those items away from S2 notes?
6. Do LLM agents show the Kirsh-Maglio signature: early, reversible, information-seeking probes that become more frequent with stronger models? No published test was found; a search with working quota should repeat the check, including 2025-2026 agent-trace analyses.
7. Does a typed state (facts, hypotheses, open questions) beat free notes at equal tokens when the format is code-enforced, with independent replication beyond one author and Claude Sonnet 4.6 / GLM-5?
8. Does the physical-interactivity null result in people (Ross, Spiridonov) have an agent analogue: are there task types where letting the agent act on a structure gives no gain over thinking about it?
9. Original Kirsh and Maglio 1994 numbers (Tetris, 1994 Experiments) and the Reisberg drawing-vs-imagery claim (a05) should be checked from primary text; is the 100% reinterpretation of drawings vs 0% from imagery still supported after later work?
10. Can a small-model-plus-exact-simulator or code tool match a larger model alone at equal cost (Mind's Eye is zero-shot only, 2022 models), and is that still true with current small models?

## Gap search results

Searched 2026-10-27. WebSearch quota was exhausted, so papers were found through the arXiv API (rate limited, used sparingly), Crossref, Europe PMC and direct arXiv PDFs. 22 new evidence lines are in evidence_d.jsonl (d01-d22, 20 opened, 2 abstract-only). Claims K01, K02, K07, K09, K12, K16, K17 and K23 were edited; K24-K36 were added.

### Closed or mostly closed
- Gap 9 (original 1994 numbers): CLOSED, with a correction. Full text of Kirsh and Maglio 1994 (author PDF) was read (d02). It has no per-skill percentages and no stated player count in the text; the 4/5/7% rates come only from the 1996 paper. The timing numbers were three separate things: physical rotation as fast as 100 ms, mental rotation ESTIMATED at 800-1200 ms from a 3-player pilot (plus 200 ms key allowance), and 150-300 ms earlier exposure of the shape. K02 rewritten. The paper itself says epistemic and pragmatic purpose are hard to separate by behaviour.
- Gap 9 (Reisberg drawing vs imagery): PARTLY CLOSED. The 0% vs 100% contrast is too strong (d03: 24 of 44 reinterpreted a held image after a rotation step; d04: reconstruals are common, reference-frame reversals need a hint). Only abstracts were read for these two; Chambers and Reisberg 1985 itself could not be opened. K35 added as contested.
- Gap 1 (equal tokens on a reasoning-trained model): PARTLY CLOSED. Extra prompted steps add about 0-3 points on o3-mini, o4-mini and Flash 2.5 for 20-80% more time (d01). Native thinking still doubles hard-math scores (Qwen3-235B AIME'24 85.7 vs 40.1, d21; Qwen3-8B Olympiad 71.5 vs 49.8, d20), but on code always-think was lower than no-think on HumanEval for three Qwen3 sizes (d20). Execution adds solved problems on top of thinking in the trained regime (d13, d14). STILL OPEN: nobody ran a token-matched test of "model's own thinking" vs "thinking plus a visible S2/S4 scratchpad" on a closed prompt-only setup; that is the experiment to run ourselves.
- Gap 4 (execution vs planning discipline): PARTLY CLOSED. Combined with the PAL ablation already in K06 (simulated runtime 23.2% vs real execution 72.0%), a 14-task, 6-model study shows that code-only already beats text-only on average (77.2 vs 73.9) and that code plus text plus a reconcile step is best (79.5, d05). Forcing text on o1-preview cost 6.3 points relative to just answering. For tasks that cannot become code the evidence is still Chain of Code (K15); no new test found.
- Gap 3 (trace ablation): PARTLY CLOSED on method, OPEN on our own traces. Sentence-level resampling is a working black-box test and picks out plans and revisions, not computations (d06); chains are an incomplete record of what drove the answer (d07); a detector for confirmatory tool calls gives 81% in one setting (d18). The share of OUR S2/S4 steps that pass is unmeasured.

### Stayed open
- Gap 2 (prompt-only gate): OPEN, with new bounds. A verbal yes/no gate beats always-calling on decision accuracy (61.9% vs 50%, 8B model, d10). The one prompt-only ask-vs-act decomposition tested raised clarification F1 about 0.28 but cut mean task success from 28.6% to 27.0% and REAL from 32.1% to 19.2% (d11, "capability dilution"). Naming the missing unknown is weak on logic and planning (40-50%, d19). The trained fixes (d09) are not prompt-only. No test of "what unknown does this resolve" as a gate on tool calls was found. K12 changed to contested.
- Gap 5 (when does forced write-out hurt; cheap router): PARTLY. Harm is concentrated where the answer rests on fast statistical or perceptual impressions learned from many examples (d08: GPT-4o 87.5 to 64.4). A cheap router exists in the abstract form of a two-draft agreement check (d20), but it was tested on math and code, not on the implicit or perceptual items where notes hurt. Nobody has tested a router on those.
- Gap 6 (Kirsh-Maglio signature in agents): STILL OPEN. A position paper now maps the theory onto LLM agents (d12; K23 wording updated, so the earlier "no paper maps it" is wrong) but has no data. Measured near-misses: stronger reasoning means more information per question and earlier (d16); spontaneous exploration is poor without a code-built summary (d15). No trace analysis of early, undone, reversible probes found. Searches for 2025-2026 agent-trace analyses returned nothing that matched.
- Gap 7 (typed state replication): STILL OPEN. Re-checked the SLEUTH paper (d22); no independent replication was found.
- Gap 8 (physical-interactivity null has an agent analogue?): OPEN, weak lead only. Code-only gave no gain over question-only for GPT-4o (80.3 vs 80.6, d05) and tool offers hurt MATH accuracy for Mistral-7B (-4.0, d09), which are the nearest "acting on the structure gave no gain" cases; no study set out to test it.
- Gap 10 (small model plus tool vs big model at equal cost): PARTLY. ReTool 32B with code beat o1-preview on AIME 2024 (67.0 vs 44.6, d13) and SMART 7B-scale models matched larger ones on tool-use questions (abstract claim in d09), both with training. The prompt-only, current-small-model, equal-cost form was not found. Mind's Eye remains a 2022 zero-shot result.

### Source notes and cautions
- d03 and d04 are abstract-only; Chambers and Reisberg 1985 not opened.
- Some table rows (Chen et al. cost table, DART Table 1, QuestBench, Pedrozo Qwen3-8B rows) came out garbled in text extraction; only readable cells were used.
- The Qwen3 thinking vs non-thinking figures are builder-reported.
- All new LLM results are on models from 2024-2026; most are single preprints and several are one-author or work in progress.
