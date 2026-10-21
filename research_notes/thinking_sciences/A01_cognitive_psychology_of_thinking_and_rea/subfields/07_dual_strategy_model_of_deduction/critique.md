# Cross-check: dual-strategy model of deduction

## Numbers re-opened and checked (full text, this session)
Confirmed exactly: Verschueren 2005 (52.6% counterexample answers, F(2,50)=167.33, span groups .472/.543/.563, likelihood .143/.084/.067, pool 292, 1,728 answers); de Chantal 2020 (N=139, 62 statistical = 45%, 66 after WM exclusions, F(1,64)=19.90, .76 vs .32); Markovits 2021 (N=206, group sizes 44/32/25 and 41/30/34, F=21.67, eta2 .132, chance .503 at 3.5 s); Markovits 2015 (53/30/24, 1.51 to 0.13 vs 1.50 to 0.97, F=15.29, order effect 0.96 vs 0.53, F=4.45); Markovits 2017 belief effects (2.47, d=1.66; 1.47, d=1.04; F(1,168)=19.92); Gratton 2021 (768/794/560 of 2,122); Brisson 2020 (0.99 vs 1.55; premise type F(1,77)=16.42); Markovits 2010 (87.1%, 38.6%, F(1,66)=23.63); Bertolazzi 2024 (92%, 82.97, 62.79); Holliday 2024 (89.50, 87.17, 85.33); Markovits 2024 review text (time-constraint and instruction summaries, Intermediate rule).

## Corrections and flags
1. a07 says N=170 analysed (87 CE, 83 stat). The paper text says 170 took part, but its Table 1 lists 61 "other" (30+31). So 170 are classified and the total is about 231. b09 is right; a07 is misleading.
2. a19 spells the author "Begin"; b20 has "Beghin". Use Beghin and Markovits (2022).
3. Gratton 2021: tests use df 1290, so about 1,293 entered the design analysis, not all 1,562 classified. The interaction (b18, eta2p .004) is tiny; F=5.57 could not be extracted from the PDF text, so it stays unconfirmed.
4. b12 lists "WM b=.02 (p<.001)" next to the claim that WM stops predicting under limits. Both hold only through the WM x condition term; easy to misread.
5. a04/a25/b05 (time-pressure switching) and a05/a28 (instruction) rest on the 2024 review only. Direction confirmed in review text, numbers not.
6. c28 and c29 were snippets only.

## Contradictions and tensions
- Strategy shares vary: 45% statistical (students, n=139), 28% (students, 2015), 37% (Prolific, 2,122). The split is sample dependent.
- WM story (Verschueren: more WM, more counterexample) versus 2020-21 work (strategy beats WM; WM beta -.21, p=.07). WM effects are modest (counterexample share rose about 9 points low to high span).
- Knauff 2025 free text finds counterexample-based uncertainty most common, against a two-type split built on rating-like items.
- Kosourikhina 2025: under speed invalid forms feel valid to most people, which does not fit "counterexample users reject quickly".
- LLM papers: models show the statistical/form signature, yet their chains list alternatives (c13). Both can be true; no diagnostic was run directly.

## Weak spots
- Almost all human evidence is from one lab (Markovits) and one instrument (abstract AC items with stated odds). The "independent_sources" counts are papers, not labs.
- Beeson 2019 is a theory review without data; its proposals (figure effects, meta-reasoning selection) are untested.
- Classification is a single-session response pattern; test-retest reliability was not found.
- No direct LLM test of the strategy construct (c30).

## Seen only in snippets or second hand
a24, a25, a26, a27, a28, b05, b24, b28 to b31, c28, c29.

## GAPS
1. Does any LLM, run on the Markovits diagnostic (90% vs 50% alternative-antecedent items), show a counterexample or a statistical pattern, and does it flip with framing ("valid?" vs "how likely?") or token budget?
2. Does a code-executed counterexample search (not model-judged) beat plain chain of thought on invalid AC/DA and belief-conflict items at equal tokens, and on which item classes does it lose?
3. Test-retest reliability of the diagnostic: how stable is a person's type across sessions and content?
4. How much of the time-pressure switch (Markovits 2013) is real strategy change versus guessing? Original numbers were never opened.
5. Can strategy be chosen deliberately? Markovits and Thompson 2023 training: sample sizes, effect sizes and transfer size are unknown.
6. Which item classes does each strategy win on outside belief-bias syllogisms (causal, quantified, planning)? Causal-task effects are tiny (eta2p .004 to .038).
7. Does the PHM min/atmosphere heuristic explain LLM errors beyond form priors, and does a 'nothing follows' probe fix it without raising false rejections?
8. Do independent labs replicate the Markovits instrument's results (belief bias, deadlines)? None found.
9. Can a cheap router, triggered by G1-style signals, pick search versus estimate better than always searching (Beeson's meta-reasoning selection)?

## Gap search results (evidence_d.jsonl, d01 to d23; claims K18 to K26 added)

Tool notes: OpenAlex and Semantic Scholar rate-limited, web search quota ran out partway, APA full texts (2013, 2023) are paywalled. Europe PMC abstracts, the open 2024 review and arXiv PDFs were read.

1. LLM on the Markovits diagnostic and framing/budget flip. STAYS OPEN. No study found (K17 updated). Nearest: Hasan 2026 (d15, 29 models, fixed Yes/No priors, wording matters, only 9 beat the floor, direct answers only) and BIS 2026 (d17, effort 69 vs 99 for GPT-5-nano, weak effect for Qwen3-32B; all items valid, so it hides accept-everything bias).
2. Code-run counterexample search vs plain CoT at equal tokens. STAYS OPEN. Partial: Logic-LM (d18) shows code beats CoT on 4 of 5 sets with GPT-4 and loses on PrOntoQA (83.20 vs 98.79); Poddar 2025 (d14) shows CoT is no uniform fix. No equal-token test on invalid AC/DA or belief conflict.
3. Test-retest. STAYS OPEN, now with a negative search record (d22). Only within-session stability and the review's "short term" wording.
4. Time-pressure switch, real or guessing. PARTLY CLOSED. 2013 abstract opened (d01): direction and confidence result confirmed, numbers still unopened. New: fast answers follow semantic availability and carry validity information (d07, d09, d10): about 15% respond to form alone at 5 s. So fast answers are cue-driven, not random guesses, and not usually logic.
5. Deliberate strategy choice. PARTLY CLOSED. Abstract of Markovits and Thompson 2023 opened (d02): N=885 over two studies, following is limited by spontaneous strategy, effect carried over to the next task. Per-study sizes, effect sizes and durability still unknown.
6. Item classes. PARTLY CLOSED. Strategy matters for belief bias, base rates, denominator neglect, social bias; not for the conjunction fallacy (d04, d12). On MP the groups flip with premise type (d05). Quantified and planning classes: only LLM-side data (d16, d19), no human strategy split.
7. PHM min/atmosphere in LLMs and a 'nothing follows' probe. PARTLY CLOSED on the first half: NeuBAROCO atmosphere items give GPT-3.5 39.42%, BERT-type about 0% (d16), and fixed Yes/No priors across 29 models (d15). The probe itself is untested.
8. Independent replication. STAYS OPEN as a negative finding (d23, K26): about 20 papers, all from the Markovits network. Newman, Gibb and Thompson 2017 (d07) is a near-independent deadline study without the diagnostic.
9. Cheap router. STAYS OPEN. Analogue only: Guo 2026 (d21) router beat random, self-select and always-think on ranking at about half the tokens. Human signals that could drive a rule: confidence (d11, N=289) and alternative count (d09).

New caveats from this pass: most d-lines are abstract-level (marked in limits). The 2013 and 2023 papers still need a full-text copy to close gaps 4 and 5. Skipped as too weak: arXiv 2512.04228 (proposal paper, no usable numbers). One correction to K02: the "groups answer alike on MP" statement holds only for plain MP (d05).
