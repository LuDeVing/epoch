# F01.01 Conceptual metaphor theory: cross-check critique

Cross-checker pass over evidence_a.jsonl (32 lines), evidence_b.jsonl (26), evidence_c.jsonl (27). 23 claims written to claims.jsonl (K01-K23).

## Corrections made (sources re-opened this session)

1. Thibodeau and Boroditsky 2011, Exp 3 (PLOS ONE page re-read). Line a15 says congruent answers were 61% with the metaphor vs 50% with the lexical prime (chi2=4.23). The paper says 64% (beast prime) vs 65% (virus prime) enforcement, chi2=.001, p=.99, N=235. Line b02 is right; a15 is wrong. Claim K04 uses b02. Exp 1 (74% vs 56%, chi2=13.94) and the 65% overall enforcement figure confirmed.
2. MUNCH (arXiv 2403.11810, Table 3 re-read). Line c08 gives LLaMA-30B MRR .33 and GPT-3.5 .47. The table rows are LLaMA-13B .33 / .22 / .33, LLaMA-30B .47 / .28 / .40, GPT-3.5 .54 / .32. Line a27 is right; c08 shifted the labels by one row. Judgement accuracies in Table 2 (e.g. .28/.21/.23) confirmed in c07.
3. Thibodeau and Boroditsky 2013 (PLOS page): pooled N=939, chi2=12.55, p<.001 confirmed; per-experiment enforcement rate varied 19%, 76%, 39% (chi2=157.57), confirmed b05. Excluding the neighbourhood-watch option left the effect (chi2=13.34, N=856).
4. Steen et al. 2014 (PLOS page): Exp 4 final N=1,026 from 1,205 completions, confirmed; Exp 4 designed to detect a small effect, confirmed.
5. Ichien et al. 2023 (arXiv full text): GPT-4 91.27%, humans 94.42% (95.39% after exclusions), GPT-3 Davinci 68.41%, RoBERTa 90.32%, 3.35% non-answers, reversed metaphors 56%, r=0.79 over 55 items: all confirmed.
6. Prystawski et al. (arXiv full text): table values confirmed (Curie 2.52/2.49/2.55/2.63/2.76/2.72; DaVinci 2.73/3.71/3.58/3.84/3.74/3.68), familiarity beta=.36 [.01,.73] confirmed.
7. Liu et al. Fig-QA (arXiv 2204.12632): 68.41, 94.42, 90.32, 50.8%, 78.1%, 19.3% confirmed.
8. Stowe et al. 2021 (arXiv): exact-match row confirmed (MetMask .087, MERMAID .133, CM-Lex .107, CM-BART .293); annotator agreement .50 and .37 confirmed. The human-rating table (Gold, Rare, Unseen columns) is scrambled in the PDF text; the a29 reading (CM-BART 2.72/2.87 gold) is plausible but the rare and unseen cells could not be assigned with certainty. Note c15 reports MetMask exact-match 8.7%, which matches the table.

## Not re-verified this session (blocked or rate-limited)

Brugman et al. 2019 meta-analysis (d=0.11, k=91), Lynott et al. 2014 and Chabris et al. 2019 replications, Lakens 2012, Wachowiak and Gromann 2023 (arXiv id 2305.04886 in my guess was wrong; Semantic Scholar returned 429), Webb et al. 2023, Lewis and Mitchell 2024, Step-Back, Durgin 2026, Hu et al. 2026 (arXiv id 2607.28683 as given in a32). These stay as the earlier agents recorded them. Where two agents opened the same source independently (Wachowiak: b20 and c13 agree; Lynott/Chabris: b only) agreement is the only check.

## Contradictions between sources

- Human framing effect: Thibodeau and Boroditsky 2011/2013 (beast vs virus, 10-18 points) vs Steen et al. 2014 (no effect in four experiments, N up to 1,026). Differences: Steen used rank ordering of five policies, a neutral control, a pre-exposure baseline, and Dutch samples in Exp 1. Neither side shows a clear reason; both are the live disagreement for O6 and mark K01 and K02 as contested.
- b05 says the 2013 paper is a "replication" while it is by the same lab and same scenario; treat as a same-lab extension.
- Wachowiak error typology: b20 says 62.12% of errors were hallucinated source domains; c14 says 62.12% of Spanish errors were non-metaphoric calls for items that should be metaphoric. The same number is given two meanings. Unresolved without the paper.
- c19 versus c17/c18: GPT-3 beats students on familiar analogy sets but collapses on counterfactual alphabets. Not a contradiction but a boundary: familiarity.
- Brugman meta-analysis (d=0.11) vs Thibodeau pooled 10-18 point shifts: the meta-analysis includes small-study bias and many null studies, so the original lab effect is probably an upper bound.

## Weak spots

- Founding Lakoff 1993 is theory; Lakoff and Johnson 1980 and Lakoff 1999 were not opened. The robust evidence he cites is the analyst's own linguistic generalisation, not behaviour.
- Boroditsky 2000 numbers come from a review chapter (a07-a12), not the original; only the 71.3% figure is given, other experiments are directional.
- Almost all behavioural evidence is crime framing or space-time priming. No study tests a source domain for problem solving in the O6 sense (restate a problem in a source domain, then solve it).
- LLM evidence is mostly metaphor interpretation (can the model read it), not metaphor as a reasoning aid. The only direct prompting study (Kramer 2025, a30) is self-built, four tiny models, bar charts, no numbers.
- LLM metaphor results mostly use 2021-2023 models (GPT-3, GPT-3.5, LLaMA-1). Only Ichien, Ye et al. (2026), Hu et al. (2026) use GPT-4 class models. Ye et al. reports attribute-matched validation near chance (46-52%) for seven models including GPT-4, in tension with Ichien's 91%.
- Hu et al. 2026 (metaphor-induced steering) is the one study showing harm to model behaviour from metaphorical instructions; single study, effect varies by model (3.9% to 43.8% per task).
- Embodied-metaphor replications b15, b16, b26, b25 were never opened (paywalled). Do not quote.

## Seen only in snippets or abstracts

a22 (head-heart replication, abstract via Europe PMC), b15, b16, b25, b26, c26, c27 (not opened). a06 is Wikipedia only.

## GAPS

1. Does restating a reasoning problem in a concrete source domain (O6) improve a frontier model's accuracy over plain chain of thought, step-back, and self-generated analogs at equal tokens? No published study tests this directly with a 2025-2026 model.
2. Does the first-position effect (framing placed before the facts) hold for LLMs? Thibodeau Exp 4 vs 5 is the only evidence and it is human.
3. Does explicit correspondence-table mapping (source item to target item) beat a free-text restatement or a single cue word in an LLM, mirroring Thibodeau Exp 2 vs 3? Untested.
4. How often does a strong current model invent a source domain or import source inferences that contradict the target (Invariance Principle failure)? Wachowiak (GPT-3) and Hu 2026 (code models) suggest it is common; no GPT-4-class or reasoning-model measurement.
5. Why did Steen et al. 2014 fail to replicate Thibodeau and Boroditsky? Any later preregistered replication of the beast/virus framing (2015-2026), and the Brugman moderator results for reasoning-type outcomes, were not found.
6. Does a value-loaded source domain (good/evil, war) bias model judgement, as the black-white IAT work (Durgin 2026) and COVID war framing results (Panzeri 2021, null overall) suggest for humans? Measure on LLMs with neutral vs loaded sources.
7. Do reasoning models (o-series, R1, extended thinking) behave differently from the GPT-3/3.5 era models on MUNCH-style apt vs inapt judgement? Ye et al. 2026 and Tong 2024 conflict with Ichien 2023 on whether the metaphor knowledge is real or surface.
8. Which source domains give measurable benefit? Space for time has the best support in humans (concrete to abstract, one-way); are there LLM tasks (scheduling, ordering) where a spatial restatement helps?
9. Cross-linguistic variation (Aymara, Mandarin, Spain vs Morocco): does an LLM's mapping choice vary with prompt language the same way, and does it matter for a monolingual agent?
10. What are the full-text numbers for Boroditsky 2000 (Exp 1-4), Brugman 2019 and Lynott 2014, which we could not open? Needed before any figure is quoted in a decision.

## Gap search results

Search budget was nearly gone (WebSearch exhausted; arXiv, OpenAlex and Semantic Scholar APIs rate-limited), so sources were found through arXiv listing pages, Europe PMC and direct page fetches. 17 evidence lines in evidence_d.jsonl (d01-d17); claims K24-K32 added, K01, K02, K13, K17, K18 updated.

1. O6 versus CoT, step-back, analogs at equal tokens: STAYED OPEN. Nearest tests: Rephrase and Respond (GPT-4 average 64.95 to 89.77, d12) and Visualization-of-Thought (GPT-4 route success 9.48 to 14.72, d13), both same-domain or spatial. Kramer 2025 reread: no numbers (d14). Use RaR as the baseline.
2. First-position effect in LLMs: STAYED OPEN. Premise order drops accuracy by 20-40% (d11) and equivalent framings flip choices by 64.5 points (d09), but nobody has placed a metaphor first versus last. Partial.
3. Correspondence table versus free text versus cue word: STAYED OPEN. No LLM study found.
4. Invented source domains and invariance failures: PARTLY CLOSED. 15-25% of outputs from GPT-4, GPT-4o, o3-mini, R1 carry concept-irrelevant content (d06); models over-label metaphor (d07); metaphor in instructions can mislead (d08). No direct count of invariance violations.
5. Why Steen failed; later replications: PARTLY CLOSED. Same-lab reanalysis blames a shifted 'neighborhood watch' option; recoded, Steen Exp 4 p=.072, pooled N=876 p=.003, w=.14 (d01). Not independent. Related studies give d=.15-.20 (d02) and a null (d03). No preregistered independent replication of beast/virus found. Brugman moderators not opened.
6. Value-loaded source domains in LLMs: PARTLY CLOSED. Danger metaphors doubled critical misaligned answers in Qwen3-32B (d08). No war-versus-neutral test on judgement.
7. Reasoning models versus older models: MOSTLY CLOSED. o3-mini and R1 show no advantage and still give 15-25% irrelevant readings (d06); open-model scores are inflated by lexical overlap (d05). Ye 2026 near-chance multiple choice (46-52%) is explained by the multiple-choice format, not by a conflict with Ichien.
8. Which source domains help: STAYED OPEN, weak partial. Spatial restatement helps on spatial tasks only (d13).
9. Cross-linguistic variation: STAYED OPEN. Chang et al. 2026 (abstract only) report a Western default in metaphor generation (d15).
10. Boroditsky 2000, Brugman 2019, Lynott 2014 full text: STAYED OPEN. Wiley and repository gave 403; Stanford PDF 404 (d17). Do not quote.

Correction to carry forward: the Steen null is not a clean refutation; the 'neighborhood watch' coding changes it. Still contested, with small effects.
