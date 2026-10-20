# Critique: intelligence analysis field (round 2)

## What the evidence supports
- Repeated: the full ACH procedure gave humans no accuracy gain and may have cost a little coherence. Repair in code (normalize to sum to 1, average several judges) helped a lot. Doubt with no external signal helps little (self-correction and debate results).
- Net: do not run ACH by default. Do run probability repair and small-panel aggregation.

## What could be wrong
1. Not independent. Nearly every ACH null comes from one group (Mandel, Karvetski, Dhami). Samples are small, tasks are simple, and Dhami 2019 probably reuses the 2018 analysts. "Established" means several papers, not several labs. No outside replication was found.
2. No human gain is not no agent gain. Humans skipped steps; a program does not. No one has tested a code-counted matrix on LLMs. The field gives a hypothesis, not a result.
3. Duplicated lines. Three agents recorded the same Mandel 2018 numbers. The counts in claims.jsonl collapse them. The "about three judges" figure is only in the earlier brief.
4. The layout effect (hypotheses in rows) rests on one abstract that two of three agents could not open. It also says trained military analysts mostly showed no bias.
5. Pro-ACH LLM designs (AgentCDM, SIA, simulated misdiagnosis) have no usable numbers. They count as zero.
6. The earlier brief had an error: arXiv 2609.00738 is BASIN, not a MuSR hypothesis paper. The "89% hypothesis structuring" claim is still unfound. Drop both.
7. Most LLM claims are preprints checked at abstract level only.

## Contested
- Devil's advocate: small gains in an agent setting (WebArena +3.5) and group satisfaction, against weak self-correction and sycophancy. Our BrainTeaser drop agrees with the second side. Keep it behind a check or an external test.
- Majority vote: one preprint says the minority is right about one time in four; others say debate cannot beat voting. Both can hold. Voting stays the baseline to beat.

## Missing, and would change agent design
- Any test of ACH-like structure on LLMs at equal tokens against vote. This is the central gap.
- Pre-mortem, key assumptions check, red team: no controlled study found. They stay practice, not evidence.
- Base rates of first-answer-right by task type. Our router depends on it.
- Source credibility rating (Admiralty-style). Tradecraft has it; no tested LLM version found.
- Estimative language (words to numbers) was not searched. It bears on how the agent reports confidence.
- Deception and adversarial inputs were not covered.
- Schwenk 1990 and Chang 2018 were never read in full.

## Memory or snippet only
Schwenk 1990 (record only), RAND 2016 (snippet), Whitesmith 2020 (snippet), Dhami 2024 (abstract, one agent), Mandel 2015, Mellers 2014, Mandel and Barnes 2014 (abstracts), Heuer 1999 (fetched, but a book, not data).

## Advice
Keep: coherence repair, small varied-panel average, counterexample test only when feedback exists, a code filter that drops evidence fitting all hypotheses. Test, do not assume: ACH-lite at a probe split. Avoid: default devil's advocate.
