# A14.04 Expected information gain models: cross-check critique

Date: 2026-11-01. Checker re-opened full PDF text of BED-LLM (arXiv 2508.21184v3), Kobalczyk et al. (2502.04485), Uncertainty of Thoughts (2402.03271), Mazzaccara et al. (2406.17453), Zhang et al. (2310.01468) and Grand et al. (2402.19471). Cook et al. 2011 is paywalled; only the PubMed abstract was re-read.

## Numbers re-checked

Confirmed:
1. BED-LLM +37.4 points average, never decreasing (abstract). Table 1 Animals GPT-4o: Prompt-Only 45, Split 83, CoT 62, BED-LLM 93, Entropy 88; Mistral-Large Celebrities 19 vs 91; Things GPT-4o 34 vs 64. Implicit maximisation Animals GPT-4o 70, Mistral 53, Qwen 61. ICL Beliefs GPT-4o 25. Wall-clock Qwen2.5-72B Animals: BED-LLM 2h30m, Data-Estimation 1d17h.
2. Kobalczyk code tables: HumanEval GPT-3.5 binary 70.8 -> 85.6, open 75.9 -> 85.0; GPT-4o-mini binary 79.6 -> 81.5; APPS GPT-4o-mini binary 62.9 -> 75.3, open 75.1 -> 87.2.
3. Mazzaccara DPO: INLG 56.7 -> 68.9 (FT 46.6), EIG 0.34 -> 0.45; Things 51.1 -> 61.1; 55,000 pairs; BigBench 17.2 -> 31.0 with EIG 0.31 -> 0.28.
4. Zhang et al. 20Q: GPT-4 0.31 Things, 0.50 Celebrities, 17.8 and 17.3 turns; RL 7B 0.26 on Things.
5. Grand et al.: human mean 1.27 bits, best 3.61, 97% above zero; LLM single sample 0.65-0.66; k=5 near human, k=10 beats it.
6. UoT: 97.0% on DX, 67.3% on FloDial, 43.7% for the matched earlier row, gains over CoT-SC 33.8, Reflexion 29.9, ToT 28.3 and 12.4.

## Corrections

- c15 (Kobalczyk 20 Questions rank table) was read backwards. The score counts position from the bottom, so a HIGHER number is better. At t=10, GPT-3.5: EIG-uniform 6.2, implicit 4.9, implicit-ToT 5.1, EIG-logprobs 4.1. GPT-4o-mini: EIG-uniform 6.8, implicit 5.5, implicit-ToT 6.6, EIG-logprobs 6.0. So EIG-uniform is best for both models, the gap is smaller for the stronger model (as the text says), and the line "implicit best" in c15 is wrong. b09/a20 were right. EIG-logprobs is below uniform from t=3 on for both models (only t=1 is slightly higher).
- The UoT "38.1%" (a17, b06, c10) is a relative improvement averaged over datasets and models, not percentage points. Per-cell gains for GPT-4 are +7.6 on DX (89.4 -> 97.0), +6.0 on Thing (30.8 -> 36.8), +21.9 on Common (49.0 -> 70.9), +25.3 on FloDial. Do not set it beside BED-LLM's 37.4 points. Llama3-70B 20Q Common closed set 51.4 -> 55.9 is only +4.5 points.
- BED-LLM and UoT use different success definitions and different answerers (open-set vs closed candidate lists), so their effects cannot be compared.
- c01 words "success more than doubled in over half of setups". Table 1 supports this for most open models but not for GPT-4o on Things (34 -> 64 yes) or Llama-3.3-70B Things (34 -> 55, no). Take the abstract wording as the authors' claim only.
- a18 and a19 both give GPT-4o-mini Animals Prompt-Only 44, BED-LLM 88 (matches table). OK.

## Contradictions between sources

- Zendo (Piriyakulkij 2024): a26 lists "online fuzzy rules 5.35" and strongest "6.55" hard; b16 lists batch fuzzy 5.35 and online fuzzy 6.01. Row-to-number mapping from the garbled table is unresolved. Only the R2 values (.57, .25, .05) agree across a26 and b17.
- Zhang et al.: the paper states strong LLMs beat human players by a large margin, but its own human row (0.24 / 0.31 in an appendix table) is close to GPT-4 (0.31 / 0.50 on Things / Celebrities). Not resolved; human sample not checked.
- Nelson 2010 says probability gain best explains experience-based choice; Coenen 2019 review and the LLM papers treat EIG as the normative choice. These are not in conflict about LLMs (no LLM paper compares gain measures), but it means the human case for EIG over probability gain is weak.
- Mazzaccara: DPO raises success on INLG and Things but Celebrities gain is +1.1, and on BigBench success rose while EIG fell. Higher EIG does not always mean higher success.

## Weak spots

- Founding study: N=20 per cell, one session, 2-4 variables, no fit of computed EIG, one lab. No replication or failed replication was found by the three searchers; absence of replication is not shown by search, only unreported.
- BED-LLM, UoT, Kobalczyk, Grand are four closed-world games or tasks with a simulated answerer (GPT-4 or another LLM). No human answerers except Li 2023 and Handa 2024.
- Almost all LLM gains are over a weak prompt-only baseline. Strong baselines (best-of-N, plain split heuristic) win back a large share: Split reached 83 vs 93 on Animals GPT-4o; Entropy 88.
- Token cost: only UoT and BED-LLM report tokens or time; no EIG paper reports accuracy at equal tokens against best-of-N sampling. This is the main gap for our agent.
- All 2025 LLM results use 2024-vintage models (GPT-4o, Llama-3, Qwen2.5). Reasoning models were tested only on QuestBench.

## Only seen in snippets or secondary text

Oaksford and Chater 1994, Steyvers 2003, Coenen 2015, Rothe 2016/2018, Ruggeri 2015/2016, Nelson 2014, Bertolazzi 2023, Zhang and Choi 2023 (partially), Yiu 2023 (position paper summary). The Cook et al. cell counts and chi-square values come from two agreeing reads (a and b) which I could not re-open.

## GAPS

1. Does an EIG-in-code step still beat best-of-N sampling and a plain "split the hypotheses" rule at EQUAL total tokens, using a current reasoning model? No paper reports this.
2. Do reasoning models (o-series, extended-thinking Claude) already ask near-optimal questions, making the scaffold redundant? Only QuestBench tested them (about 50% on logic and planning).
3. How should hypotheses be generated for open tasks (code, proofs, research questions) where there is no entity list? BED-LLM filtering works for 20 Questions; what is the equivalent for open-ended problems and how many samples are needed?
4. Where is the ask-or-answer boundary? Which gate (entropy over intents, expected gain minus cost) best stops over-asking, and what is the measured cost of a wasted question?
5. Is there any replication of Cook et al. 2011 (Schulz lab or others) with larger N, or a failure to replicate the ambiguity effect? Also later EIG-fit studies in children (Nelson 2014, Ruggeri 2016) need their primary numbers.
6. How well do LLM-estimated likelihoods p(answer given hypothesis) hold up for tests that are not yes/no (running code, tool calls), and does miscalibration erase the gain? Conformal and uniform weighting helped; no direct test with tool outputs.
7. Does probability gain or expected error reduction predict agent success better than Shannon EIG in these tasks? No LLM paper compares gain measures (Nelson 2010 suggests humans differ).
8. Does EIG-chosen experimentation transfer to scientific-style tasks (Zendo, ActiveACRE) with strong baselines? The one study has noisy tables and toy domains.
9. How much of the gain survives a noisy or wrong answerer (human, tool errors)? BED-LLM tested Q/A model mismatch only between LLMs.
10. What is the exact compute overhead of Rao-Blackwellised EIG with about 10-85 hypotheses per turn in tokens, since a hypothesis count of 10 already preserved ranking in one example?

## Gap search results (evidence_d.jsonl d01-d20; claims K25-K32 added)

Search conditions: the shared WebSearch budget ran out early, and the arXiv API, Semantic Scholar and OpenAlex returned rate-limit errors. Work was done by opening papers directly. Gaps 1, 6, 7 and 9 had the thinnest search and should be retried when search works.

1. Equal-token comparison against best-of-N and a split rule: PARTLY CLOSED, still open at equal tokens. BED-LLM Table 1 and Table 3 show EIG beating the plain split rule and "LLM picks the best candidate" at about the same wall-clock (Celebrities GPT-4o 86 vs 63 vs 50; runtime 2h30m vs 2h46m vs 2h29m). No thinking model and no token count. (d15, K29)
2. Do reasoning models already ask near-optimal questions: PARTLY CLOSED. Pedrozo 2026 (Qwen3-8B and 30B): thinking lifts partially observable win rate from 0.08-0.10 to 0.93-0.94, but the model picks the max-IG candidate on only 19-36% of turns. No o-series, Claude or Gemini 2.5 number. QuestBench: code search 80.6% (depth 5) vs about 50% for the best LLM. (d07, d08, d19, K25)
3. Hypotheses for open tasks: STILL OPEN. The only recipe is BED-LLM's (one-list diverse sampling, filter at 0.2, at least 5 survivors, uniform prior); sample count for open spaces is unknown. Ranking was stable at 10 hypotheses in one entity example. (d18, K31)
4. Ask-or-answer gate and cost of a wasted question: PARTLY CLOSED. Gates are weak (best AUROC 0.63, entropy over intents). Over-asking has measured cost: success plateaus or falls past a middle budget, steps rise, an untrained clarifier cut success by up to 6.3 points. Humans over-ask too (52-83% asked a zero-gain question). No head-to-head of entropy gate vs EIG minus cost. (d05, d09, d10, d11, d12, K26-K28)
5. Cook 2011 replication and later child EIG numbers: PARTLY CLOSED. Full text of Cook re-read, cell counts confirmed (Exp 1 N=60, Exp 2 N=40). No direct replication or failed replication found. Moeller, Sodian and Sobel 2022 (N=57) is a conceptual follow-up: above-chance controlled-test choice (66% and 43%) but recognition of confounding was unrelated to choice. Ruggeri 2016 numbers now read (4.92 / 4.38 / 3.36 questions vs 2.85 optimal). Nelson 2014 still abstract-only. (d01-d06, K01, K02, K23)
6. LLM likelihoods for non-yes/no tests: STILL OPEN, with one useful partial answer. When the answer comes from running code on sampled solutions the likelihood is deterministic and the cost is O(N+M) calls, not O(N+M+NM). No tool-output test of miscalibration. (d17, K30)
7. Probability gain or error reduction vs Shannon EIG: STILL OPEN. No LLM paper found.
8. Scientific-style tasks (Zendo, ActiveACRE): PARTLY CLOSED. Piriyakulkij: InfoGain 6.55 vs random 5.84 vs LLM-picked 4.72 (out of 8); ActiveACRE task solving 0.35 online hard vs 0.15 batch vs 0.00 ReAct. Toy domains, 5 seeds. Zendo row dispute resolved: online fuzzy 5.35, online hard 6.55, Direct LLM 4.60 (a26 was right, b16 wrong). (d13, d14, K18)
9. Noisy or wrong answerer: STILL OPEN. Nothing new beyond BED-LLM's LLM-to-LLM mismatch.
10. Token overhead of Rao-Blackwellised EIG: PARTLY CLOSED. Runtime is no higher than marginal entropy or split; call counts given; ranking stable at 10 hypotheses in one example; token counts not reported. (d16, d17, K30)

Changes to claims: K01, K02 given full-text evidence; K18 status changed from contested to single-source after the row mapping was resolved; K10 and K20 extended; K23 numbers added (status kept single-source because Nelson 2014 is unread). New K25-K32.

Retry list for a working search: gaps 1, 6, 7, 9, then newer reasoning-model tests (o3, Claude extended thinking, Gemini 2.5) of question asking.
