# Critique and cross-check: A09.09 ordinary cognition and implicit-explicit theories

Method: re-opened 9 sources and checked 10 key numbers against the PDF text (Helie & Sun 2010; Sio & Ormerod 2009; Fleck & Weisberg 2004; Liu et al. 2025; d'Aliberti & Ribeiro 2026; Mizumoto 2025; Jiang 2025; Si 2024; Zhang 2025). Claims are in claims.jsonl (22 claims, A09.09-K01 to K22).

## Confirmed exactly
- Sio & Ormerod: 117 studies, 3,606 participants, unweighted mean d 0.41 (SD 0.71), weighted random-effects 0.29 (CI 0.21-0.39), between-study variance .0834.
- Fleck & Weisberg: 23.5% vs 27.7% box solutions, p=.736; impasse chi2(1,N=34)=4.242, p=.039.
- Helie & Sun coin problem: 45.8% vs 35.6% human, 45.3% vs 35.3% model, t(74)=2.13, 82 participants.
- Mizumoto: 7.6% vs 17.6% vs 52.9%.
- Jiang (Hivemind): 26,070 open queries, mean within-prompt similarity 0.821, 81% above 0.7 and 61.2% above 0.8 under min-p.
- Si et al.: novelty 4.84 / 5.64 / 5.81 (49 ideas per condition; 109 review rows per condition); 5% non-duplicate after 0.8 dedup; Claude-3.5-Sonnet 71.4%.
- Zhang 2025 Exp1 t values (5.32, 5.10, 8.89; -3.37, -4.60) and association t=15.15.

## Corrections
1. c04 (Liu et al.): the "drop of 36.3 points (94.0% to 57.7%)" compares o1-preview with GPT-4o zero-shot on a subset. It is NOT a CoT-on vs CoT-off contrast for one model (o1 cannot run without reasoning). The clean same-model CoT effects are GPT-4o 87.5 to 64.4 (-23.1), Claude 3 Opus -8.0, Gemini 1.5 Pro -6.05. Claude 3.5 Sonnet went 65.9 to 67.7 (+1.8, p=.969): no harm. Also its zero-shot is 65.9, so the "97.8 to 94.8" figure belongs to face recognition only. Claim K08 uses the clean numbers.
2. b14/b25 (d'Aliberti): "+8.41 points on MATH-500, smaller gains on crosswords and Rush Hour" overstates. Table 5: MATH 0.322 to 0.406 (+8.41 pp), crosswords +0.45 pp, Rush Hour +0.01 pp (near zero base rate). These are pooled over small tuned model checkpoints and temperatures (320,000 paired samples), not frontier models. The entropy-to-shift link is weak and domain dependent (pooled OR 0.77, p=.070; positive in crosswords, negative in math). Status set to single-source.
3. a05 / b01 attribution: the 45.8% vs 35.6% data are from Schooler et al. (1993), re-used by Helie & Sun to fit the model. They are not new evidence, and Fleck & Weisberg (b01) found no verbalization cost. The model "reproducing" it is a fit, not a test. K04 is marked contested.
4. b06 (Nieuwenstein), b07 (Stuyck 2022 effect sizes), c05-c07 and several others were not re-checked; they stand as recorded. b07 and a20 give slightly different reporting (d=-1.57 for accuracy; counts 16.4 vs 10.5 vs 18.0 vs 11.4 per different analyses). Treat insight counts as approximate.
5. c10: the 71.4% is Claude-3.5-Sonnet predicting accepted vs rejected ICLR papers, a calibration of the LLM ranker on a side task, not accuracy on the ideas in the human study.

## Contradictions between sources
- Ordinary-process (Weisberg, Fleck) vs special-process: Chein & Weisberg (a19) find insight tied to verbal working memory; Stuyck 2022 (b07/a20) finds insight solutions immune to load. Beucler & De Neys (a24) find most correct answers are fast first answers. Mixed.
- Verbal overshadowing on insight: Schooler (via a05) says yes; Fleck & Weisberg say no; registered replication confirms it for faces only (b20).
- Incubation: meta-analysis positive (d 0.29); unconscious-thought version null after correction (g 0.018). Different tasks, but the "hidden work" account loses support.
- Output vs process in LLMs: models equal or beat humans on AUT/DAT/RAT yet lose on representational change and association distance (c05-c07, c13).
- Reasoning helps riddles (b13) but hurts implicit-pattern tasks (c04) and reasoning distillation moves models away from creative brain-like patterns (c14).

## Weak spots
- Honing theory (Gabora): all evidence from one lab, small judged samples, counts missing; no LLM test.
- EII (Helie & Sun): fits old data; the only new prediction (distractor study, N=114) is a conference paper. No LLM test of EII or incubation found.
- Many LLM results come from one model or a few models, one prompt format, and are not replicated (c11, c13, c14, c15).
- c15 (TACIT maze diffusion) is a single-author analogy, not evidence.
- Items seen only through snippets or abstracts: a08, a18, a23, a26, b09, b18, b19, b20, c02, c12, c17, c21-c26. c24 (Doshi & Hauser) and c25 (Hubert) were not opened.
- Number of independent sources is often 1 because evidence lines from the same paper (c05-c07, b07/a20) share one source.

## GAPS
1. Does a scaffold that separates wide cheap sampling from a rule-based check beat a plain loop at equal tokens on insight-type items (direct EII test on an LLM)? No published test found.
2. Does a pause or fresh-context restart help an LLM, and does it matter what happens in the gap? No LLM incubation test exists.
3. Which variation operators actually raise real distinctness for LLMs (distant cues gave no mean gain in c11; temperature is weak)? Need an operator-by-operator comparison with a diversity metric at equal tokens.
4. When should the rationale be dropped? Need a task-class rule for rationale vs direct answer, tested on current models (Liu 2025 used older models; Claude 3.5 Sonnet showed no harm).
5. Can program-triggered reframing (entropy or disagreement) help frontier models, not just small tuned ones? d'Aliberti shows gains only on MATH for small models.
6. What is the original size and replication status of Schooler 1993 verbal overshadowing on insight and of Gabora and Saab 2011 (N, stats)? Neither was opened in full.
7. Do the numbers in Weisberg 2015 and Fleck & Weisberg 2013 (five problems) support one toolbox of methods over two systems? Full texts not read.
8. Why do models fail to endorse correct insight candidates (b13), and does an external verifier close the human gap on riddles?
9. Do Beucler & De Neys (a24) fast-first-answer findings carry over to LLMs, i.e. how often is the first sample already the final correct answer?
10. Does engineered diversity survive dedup at scale: where does diversity plateau across models and tasks beyond the 5% non-duplicate figure of Si et al.?

## Gap search results
Search limits: the WebSearch budget ran out after 3 calls; arXiv, Semantic Scholar and OpenAlex APIs were rate-limited. Evidence is in evidence_d.jsonl (d01-d16); claims K23-K27 added, K04/K07/K10/K11/K19 updated.

1. Equal-token explicit-implicit scaffold on insight items: OPEN. No direct test. Proxies: Snell (d08) and Large Language Monkeys (d09) show wide sampling pays when a check is reliable and plateaus without one; CreativeDC (d04) shows explore-then-satisfy beats plain CoT on distinct tasks.
2. Pause or fresh-context restart: OPEN. No LLM incubation test found (d12, d13 only human or position papers). Lost in Conversation (d07) hints wrong early turns persist, recap recovers 15-20%.
3. Operators for real distinctness: PARTLY CLOSED. Personas plus CoT, in-context regeneration, verbalized sampling help; temperature, paraphrase, creative system prompts do not (d02, d03, d05). Still no single equal-token comparison.
4. Rationale rule: PARTLY CLOSED. Sprague (d10) and inverse-scaling (d11) support math/symbolic only; insight items on current models untested.
5. Program-triggered reframing on frontier models: OPEN. Nothing beyond d'Aliberti found.
6. Schooler 1993 and Gabora and Saab 2011: PARTLY. Schooler's numbers seen secondhand only (d01); replication status mixed (Gilhooly 2010 BF 0.92 insensitive). Original N unknown. Gabora and Saab 2011: not found, OPEN.
7. Weisberg 2015 and Fleck and Weisberg 2013: OPEN (full texts not retrieved).
8. Endorsement gap: OPEN. d14: no verifier test on insight riddles found.
9. Fast first answer in LLMs: PARTLY CLOSED for math: first round correct in more than 92% of cases (d06). Not tested on insight items.
10. Plateau after dedup: PARTLY. NoveltyBench (d05): fewer than 3 distinct of 10 for many models; Deng (d02): 23 to 27 categories vs 28 for humans, with combinations rising 85 to 240 under persona plus CoT. No cross-model plateau curve.
