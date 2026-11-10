# Critique: E12.07 Automated wargaming (cross-check)

## Re-opened sources (full PDF text, this session)
Confirmed against arXiv PDFs: Lamparth 2024 (214 experts, 48 teams, matches on 16/10/9 of 21 actions); Rivera 2024 (GPT-3.5 10.15 to 26.02, 256%; Table 2 escalation scores GPT-4 9.78-11.83, GPT-3.5 17.79-21.88, Claude-2.0 3.36-6.67, Llama-2 4.44-5.79, GPT-4-Base 17.61-20.00; GPT-4-Base nuclear 6.71-7.09%); Elbaum and Panter 2025 (6.37 to 3.96 / 3.33 / 4.61 / 2.76; -38/-48/-28/-57%); Payne 2026 (21 games, 329 turns, 780,000 words, 45 times 6.9%, eight de-escalatory options unused, Claude 8-4, 100% to 33%, GPT-5.2 0% to 75%); COA-GPT (3.4% lower than human); Ma 2024 table (prompt 1 vs 2 rows exact); Matlin 2026 (20 of 223, 9%); CADET (4.2 vs 4.4, nine judges, 16 vs 0.4 person-hours); Riedl and Matlin five failure modes.

## Corrections and clarifications
- Lamparth: wording is "statistically matches" the frequency; match counts fall with newer models (16, 10, 9).
- Rivera Table 2: values are mean +/- interval, printed in blocks by scenario; quote as ranges, not one number per model. GPT-3.5 nuclear 0.13-0.21% confirmed.
- Payne: the tactical-nuclear table is column-garbled in text; only Claude 86% is confirmed by prose. The 79% (Gemini) and 64% (GPT-5.2) in c16 are likely but not verified. The 21 games include a seventh match of a model against a copy of itself.
- c07/a07 "about 33% as often" is a derived ratio (2.48/7.38), not a reported figure.
- Richelieu (c26/c27) and Ma fine-tuning numbers (c25) were not re-opened.

## Contradictions
- Personas: Lamparth null (menu game, background text) vs Snow Globe effect (goal-stating personas, 7B model). Probably different manipulation types. Contested.
- Temperature and prompt: Elbaum large effects (Mistral-7B) vs Rivera's own prompt variants mostly null (GPT-class). Shrivastava: wording matters as much as temperature.
- Different designs (menu vs free text) make most pairs not directly comparable.

## Weak spots
- Nearly all evidence is 2023-2026 LLM work with small N per cell (10-20 runs) and author-built scenarios. Only Lamparth has a human expert baseline.
- Cranfield/AIAA (Yuksek 2023) and Schwartz 2020 were not opened (403). CICERO and Diplodocus not opened. Emery read via a page summary.
- Only COA-GPT tests whether simulated evaluation improves plan quality against a real score, in one game.
- Payne is a single-author preprint; the escalation ladder is author design.
- Independence: agents inside one run share a model and world state, so bootstrap intervals are optimistic.

## Only seen in snippets
Cranfield/AIAA, Schwartz SPIE, CICERO, Diplodocus, Black thesis (cover only), Richelieu details.

## GAPS
1. Does simulate-then-revise (test by running) raise the accuracy of an LLM-made plan against ground truth, at equal tokens, outside StarCraft? Only COA-GPT tests this.
2. How many samples of a simulated evaluator are needed for a stable verdict, and does median of k beat one run at equal tokens?
3. Does an LLM adjudicator with code checks for plan drift match a human adjudicator on outcomes? No validation found.
4. Does a different-model or code-built adversary find more plan flaws than a same-model adversary (Welfare Diplomacy suggests yes, one test)?
5. Do escalation and agreement results hold on 2026 frontier models under the Rivera and Lamparth protocols (replications)?
6. What do the Cranfield/AIAA studies (Yuksek 2023; Schwartz 2020) measure, with numbers?
7. Do goal-stating personas change outcomes across models, versus background personas (resolve Lamparth vs Snow Globe)?
8. Does anonymising actors and changing one fact make a simulated outcome move (counterfactual sensitivity) across simulators?
9. What is the real base of the RAND 1950s and RSAS evidence on machine versus human players (Emery, Pauly)?
10. Does a reflection slot reduce bias but also reduce the validity of the test (instruction following versus real de-escalation)?

## Gap search results
Tool limits: arXiv API, Semantic Scholar and OpenAlex returned rate-limit errors; the shared WebSearch budget ran out after one query. Sources were opened as arXiv PDFs by known id. New evidence is in evidence_d.jsonl (d01 to d15).

- Gap 1 (simulate-then-revise raises accuracy vs ground truth): PARTLY CLOSED by general LLM evidence, still open for wargame plans. Huang 2024 (d01): self-revision without external signal lowers accuracy (Llama-2 GSM8K 62.0 to 36.5-43.5). CRITIC (d05): tool-checked revision helps. Claim K21 added. No new plan-specific test beyond COA-GPT.
- Gap 2 (samples needed, median of k): PARTLY CLOSED. Large Language Monkeys (d03) and Snell (d04): exact verifier gives log-linear gains; without one, vote plateaus (MATH 40.50% to 41.41%). Not tested on plan verdicts. Claim K22.
- Gap 3 (LLM adjudicator vs human): OPEN. Only chat-judge agreement over 80% with biases (d06). No wargame adjudication validation found. Claim K23.
- Gap 4 (different-model or code adversary): PARTLY CLOSED. Welfare Diplomacy RL exploiter (d09) and mixed-family debate 91% vs 82% (d10), but no equal-call baseline; Huang (d02) shows debate gains can be voting. Claim K25, single-source.
- Gap 5 (2026 replications): OPEN, search blocked.
- Gap 6 (Cranfield/AIAA): OPEN. Repository entry located, content blocked by 403 and a Cloudflare challenge (not bypassed); no numbers (d11).
- Gap 7 (personas): PARTLY CLOSED. Zheng 2024 (d07, no accuracy gain over 162 personas) and Hu and Collier (d08, under 10% variance) explain the null for background personas; goal-stating personas not tested in a wargame. Claim K24.
- Gap 8 (counterfactual sensitivity): OPEN.
- Gap 9 (RAND/RSAS base): OPEN.
- Gap 10 (reflection slot: bias vs validity): OPEN for wargames; method advice only (d15: compare to same-budget self-consistency, score on ground truth).

Caveat: Snow Globe was not re-opened in this step, so its persona claim stays as in earlier files.
