# Debiasing (E18.08) cross-check critique

## Sources re-opened this session (full text) and result
1. Morewedge et al. 2015 (PIBBS PDF): game -46.25% / -31.94% immediate, -34.76% / -23.57% follow-up; video -18.60% / -25.70%, -20.10% / -19.20% (Exp 1 / Exp 2). CONFIRMED in the conclusion text. d=.78/.24 trained facets, d=.79/.65 untrained facets, trained vs untrained d=.20: confirmed.
2. Sellier et al. 2019: 58.8% vs 72.2%, b=-.60, chi2=5.23, p=.022, OR .549, CI [.33,.92]: confirmed.
3. Mellers et al. 2015: 743 forecasters, 150,000+ forecasts, 199 questions, training r=.17 (t(741)=4.56), teaming r=.30: confirmed. Multiple R .43 (dispositions + training + teams, F(5,587)=26.13) vs .64 (adds behaviour, F(8,581)=52.24): both correct, different nested models. Dispositions-only .31, situation-only .34, plus behaviour .54.
4. O'Sullivan and Schofield 2019: 2.8 vs 3.1, CI -0.94 to 0.45, p=.49: confirmed. New caveat: 76 analysed out of 320 (244 excluded as incomplete), so underpowered and attrition-prone.
5. Echterhoff 2024: GPT-4 framing 0.375 vs 0.780 (gap -0.405), "40.5% more", Llama-2 7B 32.1% fewer females: confirmed.
6. Lyu 2025 (SACD): FOMC llama3.1-8b vanilla 0.3805, CoT 0.3425, self-help 0.2100, SACD 0.1570, debate 0.5020, few-shot debias 0.2900: confirmed.
7. Lou and Sun 2024: 62 questions in total; the numeric/forecast subset is 42 (7 of 42 time-period questions give 6 of 11 exceptions); GPT-4 anchoring index about 0.45 vs 0.61 in the human source: confirmed. Evidence a25 and c07 differ on 62 vs 42, both right for different subsets.
8. Huang et al. anchoring: Qwen2.5-0.5B 60.5, GPT-4o 27.3, R1 25.0, Qwen3 22.0, Llama-3.1-8B 34.7 to 24.7 with Anti-DP, knowledge enhancement 50.5 (worse): confirmed.
9. Chhikara 2025: GPT-4o SimpleQA 35.14% to 65.40%, ECE 0.612 to 0.037, helped in 91.97%; GPT-4-turbo ECE 0.750 to 0.165 (95.86%): confirmed. "Up to 460%" is a relative accuracy gain for one model, not GPT-4o.
10. Knipper 2025 headline figures (45 LLMs, 2.8M responses, 17.8-57.3%, 39.5%, 14.9%): confirmed in abstract.

## Corrections
- Morewedge abstract (PIBBS) quotes "games -31.94%, videos -18.60%, later -23.57%, -19.20%", mixing Exp 1 and Exp 2 figures. Use the body numbers per experiment. Evidence a12/a13 are right.
- Mellers .43 vs .64 is not a conflict (see above).
- c09 gives DeepSeek-R1 anchoring index "0.34 or 0.28": table shows 0.340; the 0.28 is unsupported, ignore it.
- Chhikara "accuracy up to 460%" is not GPT-4o.

## Contradictions between sources
- Checklists: Soll et al. say checklists help complex repeated tasks (no number); O'Sullivan RCT shows no gain for a cognitive forcing checklist. Likely split: forgetting errors vs judgement errors. Contested.
- Consider-the-opposite: helps in Lord et al. 1984 lineage, but backfires when many alternatives are hard to list (Sanna 2002). Contested.
- Lou and Sun: both-anchor helps GPT-4 on 8 of the expert-hint questions only; other questions stay far off.
- Reasoning helps anchoring (Huang) but CoT does not (Lou and Sun): CoT prompting on non-reasoning models is not the same as reasoning-trained models.
- Instruction tuning increases bias (Itzhak) yet self-help works best on the strongest instruction-tuned model (Echterhoff).

## Weak spots
- Almost all human training evidence comes from one lab (Morewedge); the 2025 replication is the same group. One independent replication is the key missing item.
- Human debiasing outcomes are bias-test scores, rarely real decisions. Sellier 2019 is the one field-like test.
- LLM studies mostly use bias-score gaps, not task accuracy, and rarely match tokens across arms. SACD uses several calls per item; no equal-token comparison against best-of-N.
- Model versions (GPT-3.5, Llama-2, 8B models) are old or small; frontier reasoning models are tested only in Huang 2026.
- Bias scores differ by paper, so numbers cannot be pooled.

## Seen only in snippets or not opened
- a30-a33 (Fischhoff 1982, Arkes 1991, Larrick 2004, Lord et al. 1984): known only from citations.
- c22 is our own synthesis; c23 not read; c24 (Hills) and c25 (Ma et al.) are search snippets only.
- Evidence lines a01-a11, a29, b07-b12 are from review chapters or secondary reads; effect sizes in the originals (Fong and Nisbett, Soll and Klayman, Larrick-Mannes-Soll, Arkes-Dawes-Christensen) were not opened.

## GAPS
1. At equal tokens, does an iterative detect-analyse-rewrite loop (SACD) beat best-of-N or plain self-consistency on anchoring and framing tasks with frontier reasoning models?
2. Do reasoning-trained models (R1, Qwen3 thinking, GPT-5-class, Claude thinking) still show anchoring and framing, and does extra thinking budget reduce it at fixed cost?
3. Is there any independent (non-Morewedge) replication of one-shot game training, and what is its decay beyond 3 months?
4. Which LLM biases are missing-rule errors (fixable by supplying rules) vs intuition errors (need input restructuring)? No LLM study splits them, as Aczel did for humans.
5. Does pre-mortem / prospective hindsight prompting have any measured LLM effect (Hills 2025 is unmeasured)?
6. Can we retrieve past-error feedback from memory to mimic game-with-feedback training, and does it transfer to untrained bias facets?
7. Do SPIES-style bin elicitation and fractile splitting improve LLM calibration (overprecision) as in humans?
8. Does debate with deliberately diverse roles (DReaMAD, MoLaCE) beat single-agent debiasing at equal tokens, given that same-model debate raises bias?
9. When do checklists help an LLM (forgetting-type errors in long tasks) vs fail (judgement errors)? Needs a direct test matching Soll's boundary.
10. How stable are LLM bias scores across paraphrases and repeats (Suri, Macmillan-Scott), and what sample size makes a debiasing gain detectable?

## Gap search results
Evidence: evidence_d.jsonl (d01-d20). Search limits: WebSearch budget was used up by other agents, and arXiv, Semantic Scholar and OpenAlex APIs returned 429 for most of the run. Sources came from the arXiv search page (via fetch), Crossref, direct PDFs and publisher pages. Most papers read in full text (pdftotext); d18 and d19 are abstract-only.

1. SACD vs best-of-N at equal tokens: STAYS OPEN. No paper found that matches tokens. Only partial hint: PROBE-SWE shows CoT can be worse than no strategy (16.1% vs 12.9%) and its rule-elicitation fix uses extra calls without a best-of-N arm (d05, d06).
2. Reasoning models and thinking budget: PARTLY CLOSED, answer is negative. Kraishan 2026 (d01-d03): not less biased than siblings (Delta=+0.031, p=.157), no negative slope on realised tokens, only anchoring is human-like, framing reversed. This conflicts with Huang et al. (K15), so K15 is now contested. Open: budgets above about 3,500 tokens and frontier Claude/GPT-5-class thinking beyond Haiku 4.5 and GPT-5.1.
3. Independent replication of game training: CLOSED for the immediate and 8-week effect (Martey et al. 2014, d16-d17; Dunbar 2017 abstract, d18). Remaining limits: same funding programme, video comparator, heavy attrition (144 of 391 at 8 weeks), nothing beyond 8 weeks. K03 raised to established.
4. Missing-rule vs intuition errors in LLMs: PARTLY CLOSED. PROBE-SWE (d05-d07): generic prompts do not help, eliciting the rules first cut sensitivity about 51%. Kraishan's restate-the-anchor line (d04) is an input fix. Still no study that sorts LLM biases by error type as Aczel did; K25 is single-source.
5. Pre-mortem prompting: STAYS OPEN. Hills 2025 is a demonstration with no numbers (d08); InvThink is a safety analogue (d09). No measured effect on judgement bias.
6. Past-error memory as game-feedback analogue: STAYS OPEN, with a warning. RealICU (d12-d13) shows stored insights from earlier windows can cause anchoring (Hit@5 0.526 with memory vs 0.601 without). No transfer-to-untrained-facets test exists.
7. SPIES and fractiles for LLM calibration: STAYS OPEN. Only plain interval prompts tested (d10-d11): hit rates far below nominal and flat across stated confidence.
8. Role-diverse debate vs single-agent debiasing at equal tokens: STAYS OPEN. Ma et al. (d14-d15) confirm same-model debate raises bias; one debiased critic gives small gains. DReaMAD and MoLaCE were not compared head-to-head.
9. Checklists, forgetting vs judgement errors: STAYS OPEN. No direct LLM test found.
10. Stability and sample size: PARTLY CLOSED. d07 and d20 show 5 items per bias and 40-item arms are too small; K31 gives a plan (100+ items, paraphrases, 10+ repeats, item-level tests). Paraphrase variance was not re-measured.

Claims changed: K03 single-source to established; K15 single-source to contested; K02, K08, K09, K14, K19, K24 got new evidence ids; new K25-K31.
