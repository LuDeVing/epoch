# A18.01 Causal reasoning and transfer tasks: cross-check critique

Checked 2026-10-31 by the cross-checker. Claims are in claims.jsonl (K01-K21).

## Numbers re-opened this pass (confirmed or corrected)

Opened: Taylor et al. 2009 (PMC full text), Farrar et al. 2020 (PMC full text), CLadder (arXiv 2312.04350), Lewis and Mitchell (arXiv 2402.08955), Corr2Cause (arXiv 2306.05836), Kiciman et al. (arXiv 2305.00050).

1. Taylor 2009, solve criterion: 17 correct trials over two consecutive 10-trial blocks, alpha .01, stop at 150 trials. CONFIRMED. Transfer criterion 15/20. CONFIRMED.
2. Taylor 2009, 3 of 6 solved, mean 103.3 +/- 20.3 trials (s.e.). CONFIRMED. Side switching 22.1 +/- 9.0% vs 0%, U=9, p=.0318 one-tailed. CONFIRMED. The "+/- 20.3" is an s.e., not an s.d.
3. Taylor 2009, transfer 3 p=.0156 (binomial, H1 p=.25, n=3). CONFIRMED. Note: this tests a latency/switching pattern across 3 birds, not accuracy.
4. Girndt 2008, 20 of 24 apes avoided the trap on trial 1. CONFIRMED (as cited in Taylor 2009).
5. Farrar 2020, 116 experiments, 63 papers, median N = 7, 44-59% positive claims, 87 with pass counts and 72 with at least one passer (so 15 with none), max passers 17, median 3. CONFIRMED.
   CORRECTION: a15 says "14 of them trap-tube variants". The paper says 14 PAPERS used trap-tube variants. CORRECTION: species count is 43 in the abstract and 45 in the body text. The paper is inconsistent. Quote "43 to 45".
6. CLadder: overall random 49.27, LLaMa 44.03, Alpaca 44.66, davinci 49.92, GPT-3.5 52.18, GPT-4 62.03, CausalCoT 70.40, +8.37; CausalCoT by rung 83.35 / 67.47 / 62.05. CONFIRMED. The PDF table is garbled, so the order of the GPT-3 instruct rows was read by position: text-davinci-001 51.40, -002 53.15, -003 56.26.
7. Lewis and Mitchell: humans 0.753 [0.734, 0.773], GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452. CONFIRMED by label order. Error rows: GPT-3 5.81 / 30.97, GPT-4 22.00 / 32.67, humans 38.59 / 14.67. CONFIRMED.
   Note: GPT-4 (0.452) is above GPT-3.5 (0.350) but below GPT-3 (0.488). This is odd and worth knowing before anyone says "newer models do worse". Counts are pooled over all alphabet types.
8. Corr2Cause: best F1 33.38 (BART MNLI), text-davinci-003 29.08 (precision 20.92, recall 47.66). CONFIRMED. The appendix table labels a row "GPT-4" with 29.08 and 64.6, apparently a mislabel. Fine-tuned drop to 39.29 on paraphrase and up to 62.30 after refactoring. CONFIRMED. Do not quote 29.08 as GPT-4.
9. Kiciman et al.: 97% Tubingen, 92% counterfactual, 86% necessary/sufficient, 80.3% / 98.5% on the new pair set. CONFIRMED.
10. Voudouris 2022 child baseline: a16/c01 say 52 children; a17/c04 say a 59-child baseline. NOT RESOLVED (not reopened). Different samples are plausible, since Mecattaf 2024 may have re-tested. Do not mix.

## Contradictions and weak spots

- Independence is poor for the headline claim. Every crow result (a01-a05, b01, b02, b12) comes from the Taylor lab. The only outside check on the 2009 design is a comparison with apes, which fail for different reasons (tool load). No outside lab replicated the three-transfer series on crows. The follow-up (b12: 3 of 14 crows passed the trap-table, only those who passed the tube) was read as abstract and search summary only.
- a11 (Seed 2006: 7 of 8 rooks) and b13 (Tebbich 2007: 3 of 7 non-tool-using rooks) are different studies, not a conflict. Neither was opened. One rook reportedly passed transfers.
- Several lines are duplicates of one paper counted twice: a16 = c01 (Voudouris 2022), a17 = b17 = c04 (Mecattaf 2024), a20 = c20 (CLadder), a05/b05 vs a07 (Martin-Ordas). Independent-source counts in claims.jsonl were set to the number of distinct papers.
- Effect of tool load vs causal knowledge is competing: Voelter and Call 2014 (a09) explain the ape failure by tool load, Povinelli (a14) by lack of unobservable-force reasoning, Martin-Ordas (a07) by analogy tied to action. The data do not separate them.
- Aesop's fable: Jelbert 2014 says crows pass some, fail others; Hennefield 2018 and Ghirlanda and Lind 2017 re-analyses (abstract and snippet only) say trial-and-error learning. Not settled.
- LLM side: no study runs the crow tasks. The nearest are Animal-AI items (Mecattaf 2024, 3 models, 12 trials per level, coarse controls), blicket tests, and counterfactual swaps. Counterfactual-swap results (K12) are the strongest bridge to the cue-removal logic, but they test pattern vs rule, not physical causes.
- Several LLM results are old models (GPT-3 era, LaMDA). Newer evidence is c15-c18 (2025-2026), partly from preprints, including one vendor preprint (c18).

## Seen only in snippets or abstracts

a11, a12, a13, a14 (restated via Taylor 2009 or others), a21, a22, a23, a25, b10, b11, b12, b13, b14, b15, b16, b26, c23, c24. Neilands 2016 (weight) is second-hand through Taylor 2020. Mecattaf 2024 and GX-Chen 2025 numbers were not re-opened (arXiv API was blocked; OpenAlex and Semantic Scholar rate-limited).

## GAPS

1. Has any outside lab replicated the Taylor 2009 three-transfer series (cue removal, inverted/two-hole, trap-table) on crows or another bird, with first-trial data? (Taylor, Roberts, Hunt, Gray 2009 and later: not opened.)
2. How do current frontier LLMs and scaffolded agents do on a text/grid trap-tube with cue removal, a decoy (hole with base) and a visually different trap-table, at equal tokens? No study found.
3. Does a plain-vs-scaffold comparison on Animal-AI trap-tube items (Mecattaf 2024 protocol) show any gain, and with newer models than Claude 3.5 Sonnet, GPT-4o and Gemini 1.5 Pro?
4. In Mecattaf 2024, what is the per-task result for trap-tube items, and does the child baseline use 52 or 59 children?
5. Do chain-of-thought and longer reasoning help or hurt on cue-removal transfer in LLMs (CheeseBench suggests harm, CLadder suggests help)? Which task features decide this?
6. Is the AND-rule (disjunctive bias) deficit in blicket tasks gone for current reasoning models (gpt-5 era), and does hypothesis sampling still add value at equal tokens?
7. What do Ghirlanda and Lind 2017 and Hennefield 2018 actually find in the numbers: how much of Aesop's-fable success is within-task learning vs first-trial preference?
8. Which controls count as sufficient triangulation: if adults fail the inverted-trap control (Silva 2005), what pass criterion is fair for an LLM agent?
9. How far does failure on a transfer task come from the action interface (tool load) rather than causal knowledge, for LLM agents? Does simplifying the action format change pass rates?
10. Do outcomes on the Pearl-ladder rungs (CLadder 83 / 67 / 62) hold for 2025-2026 models and with equal-token baselines such as self-consistency?

## Gap search results (2026-10-31, gap searcher)

Method note: the WebSearch quota ran out after two calls. arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429. I used Europe PMC, PMC full text, arXiv abs pages and the local text extractions in D:/research_scratch/A18.01/. Evidence is in evidence_d.jsonl (d01-d19). New claims are K22-K29.

Gap 1, outside replication of the Taylor 2009 series: STAYS OPEN for the full series, but narrowed. No outside lab ran cue removal plus the decoy hole plus the trap-table with first-trial data. What outside labs did show: rooks 3 of 7 passed the tube and 0 transferred (d02); Darwin's finches 0 transfers (d04); hooded crows 1 of 6 passed on trial 1 and 4 by trial and error (d03); macaws and caiques 1 of 8 showed clear transfer, with confounds named by the authors (d05); zebra finches N=34 transferred at chance (d06); border collies never reached 60% (d07). The 14-crow follow-up is now read in full (d01): 8 naive crows at chance, 3 of 14 passed, all trap-tube solvers. It is still the Taylor lab. K22, K23.

Gap 2, frontier LLM or scaffolded agent on a text or grid trap-tube at equal tokens: STAYS OPEN. Negative again, but with limited search (quota and API blocks). The closest items are Animal-AI (d11) and CheeseBench (d13, d18); neither has cue removal, a decoy and a trap-table.

Gap 3, plain-vs-scaffold on Animal-AI trap items with newer models: STAYS OPEN. Mecattaf 2024 has no scaffold arm; its one prompt variant (one in-context example) gave mixed results (d11). K26.

Gap 4, Mecattaf per-task trap-tube numbers and the 52 vs 59 children: PARTLY CLOSED. Per-task numbers are not in the paper (per-level figure only, n=12 trials per level, no trap-tube breakdown). Mecattaf says 59 children; Voudouris 2022 analyses 52 children (44 after outlier removal) and 30 AIs. The papers disagree; I could not find where 59 comes from. Use 52 with Voudouris as source. d11, d12, K26.

Gap 5, CoT help or harm: PARTLY CLOSED as a task-shape answer. CheeseBench's harm is from Qwen2.5-VL-7B, 15 trials per cell, about +-25pp noise (d13). CLadder's help is from a fixed procedure on GPT-4: +8.37 on v1.5, +2.36 on v1.0, +9.65 on anti-commonsense, +1.5 at rung 3 (d14). A 2026 preprint finds Socratic prompting beat CoT on counterfactuals by +0.09 (d19, abstract only). No equal-token cue-removal test. K27.

Gap 6, AND deficit in reasoning models: PARTLY CLOSED. gpt-5 and deepseek-reasoner are near-perfect on OR, AND remains harder, and gpt-5 takes about 40 s per test against about 20 s for humans (d15). Value of hypothesis sampling at equal tokens: OPEN. K28.

Gap 7, Aesop's fable re-analyses: CLOSED for Hennefield 2018 (full numbers, d09); Ghirlanda and Lind 2017 only to abstract level (23,928 choices, 36 birds, 11 of 33 experiments; d10). Result: learning in the task explains two of three tested tasks; the third shows a first-trial preference for solid objects (OR 57.02). K24.

Gap 8, fair pass criterion: CLOSED as a recommendation, with one source. Silva et al. 2005 (d16): adults pass functional traps 40/40 and 10/10 but fail ineffective-trap items (36 of 40 far-end insertions) and give causal reasons. Pass rule: correct on functional items, a causal reason in words, and the decoy reported as a separate bias check. K25.

Gap 9, interface vs causal knowledge: CLOSED in direction, OPEN for causal transfer tasks specifically. CheeseBench 20% to 57% by interface settings (d18); matched MCP/CLI interfaces diverge in 94.3% of 2,004 episodes, repair gains up to 9.0 points (d17). No study re-runs a causal transfer item with a simplified action format. K29.

Gap 10, CLadder rungs for 2025-2026 models and equal-token baselines: STAYS OPEN. Two 2026 abstracts on the ladder were found (d19) but neither uses CLadder or self-consistency. The 83.35 / 67.47 / 62.05 numbers are GPT-4 (May 2023) with a structured CoT; the vanilla GPT-4 rung values are 63.01 / 62.82 / 60.55 (d14), so the rung-3 gain is 1.5.

Open after this pass: 1 (full series), 2, 3, 6 (sampling at equal tokens), 10. No existing claim statuses were changed; K01 stays single-source because the new evidence (d01) is again from the Taylor lab.
