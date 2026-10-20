# Critique: medical diagnostic reasoning (round 2)

## What is solid
- Forced slowness and "be careful" instructions do not raise accuracy (Norman 2014, Ilgen 2013). Unstructured reflection corrects about as often as it breaks (Monteiro 2015, Lambe 2018). Debiasing instruction and bias checklists do not reliably work (Sibbald 2019, Smith 2015, two reviews). This matches our own losses on ARC and word puzzles.
- The earlier brief had three errors, now fixed: PMC4539330 is Monteiro 2015, not Norman 2014; Sibbald found no benefit from either checklist (the brief recalled retrieval beating debiasing); Norman's "n of 96 and 108" is only partly confirmed.

## What rests on one source
- Kammer 2021 (a list helps only if it holds the right answer) is the key design result and it is one RCT with 90 students. Do not build the whole candidate-source step on it without our own test.
- Graber 2005 (premature closure) is one case series. It was counted three times across rounds, but it is one study.
- MAI-DxO, Medprompt and Kanjee are each one source. MAI-DxO is a vendor preprint with no equal-compute ablation, so "the schema causes the gain" is unproven. The cross-model claim was fetched once and is not independently checked.

## Memory or snippet only
- Elstein 1978 (3 to 5 early hypotheses) is memory. Illness-script claims (Schmidt and Boshuizen) were not retrieved; Lee 2010 and Mamede 2008, 2010, 2012 are snippets.
- Sherbino r = -0.54 is unverified.
- Several 2026 items (Healy, Ong, Cusacovich, Oh, Li, Fan) are abstract-level with credibility 40 to 65 and small n. Do not quote their numbers in the design.
- Search budget ran out in round b, so the LLM side was checked least.

## What could be wrong
- Human trials use students and residents on case vignettes. A model has the facts in weights, so "reflection does nothing" may transfer, but "checklists need the right answer" may not. The mechanism may differ.
- Most LLM results use GPT-4 or o3 on curated NEJM or exam cases. Hager's real-data result goes the other way. Our small model on messy tasks is closer to Hager.
- The reflection evidence is contested (Mamede, Lambe 2016 positive; others null). The honest reading is "structured and conditional", which may just be a story that fits both sides.
- The human-plus-LLM trials say little about a program that uses the LLM's output directly.

## Missing, and it would change the agent
1. Any test of an LLM generating a differential, then picking a discriminating check, against equal-compute voting. This is the core of M1 and M2 and no evidence was found.
2. Evidence on when a second opinion helps people (independent versus anchored). Needed for the blind-second-call step.
3. Calibration: does an LLM's agreement or stated confidence predict being right on diagnosis? Meyer 2013 is about humans only.
4. Dynamic information gathering by LLMs (ask for the next test). Only MAI-DxO, a preprint.
5. Non-medical expert fields' base rates for "first answer right" (the router question). Medicine offers no clean number.
6. Harm from a wrong hint to a small model: BiasMedQA and Oh cover it, but not for open models near our size under a scaffold.

## Net use for the design
Keep: conditional, outside-sourced candidates at impasse; checks that read real input; no scheduled doubt. Drop or test first: illness cards, always-on reflection, confidence gates from the model's own words.
