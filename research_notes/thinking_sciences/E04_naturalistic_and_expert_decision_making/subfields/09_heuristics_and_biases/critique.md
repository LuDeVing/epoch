# Critique: Heuristics and biases (E04.09)

Cross-check date 2026-11-19. Sources re-opened from text copies already on D:/research_scratch/E04.09 plus fresh arXiv downloads (Hagendorff 2212.05206, Macmillan-Scott 2402.09193, Suri 2305.04400, Itzhak 2308.00225, Echterhoff 2403.00811).

## Numbers re-checked (10)

1. Tversky and Kahneman 1974: hospital answers 21 larger / 53 same (21 smaller), ascending vs descending product 512 vs 2,250, correct 40,320. CONFIRMED in text copy.
2. T and K 1981: Asian disease problem labels N=152 and N=155 confirmed (percentages 72/28 and 22/78 consistent with the paper, not re-parsed line by line).
3. Many Labs 2 abstract (15,305 participants, 15/28 = 54%, median d 0.60 vs 0.15, 9 reversed, 11 heterogeneous). CONFIRMED. Note: 14/28 at p<.0001 is stated as "fourteen (50%)".
4. Many Labs 2 calculator item: aggregate N=7,228, 49% (cheap item on sale) vs lower share for costly item. CONFIRMED (N and 49%); 32% and d=0.40 not re-parsed.
5. Kuhberger 2023: d=0.60 (r=0.28), bias-corrected 0.52, lambda 1.955 all present in the PMC text. CONFIRMED.
6. Hagendorff: humans 38% vs 41% original (n=3,428), ChatGPT-3.5 59%, GPT-4 96%, davinci-003 intuitive 80%, CoT 5% to 28% and 80% to 29%. CONFIRMED. GPT-4 95% to 88% with CoT blocked is stated in the paper text (a different base from the 96%, because the blocked-reasoning run is a separate sample).
7. Suri: anchoring means 20.83/22.50 low and 105.97/80.50 high; conjunction 18/20 ChatGPT vs 10/20 humans; endowment 37 of 40 vs 34 of 40. CONFIRMED.
8. Itzhak: certainty 0.24 (davinci-002), 0.67 (davinci-003), belief invalid 0.55/0.65, decoy-expensive GPT-4 0.38. CONFIRMED for the DaVinci family. The Mistral and T5 columns are garbled by PDF extraction, so evidence a23 values for Mistral (0.05 vs 0.26) and GPT-4 certainty 0.15 are not confirmed.
9. Echterhoff: 40.5% and 32.1% confirmed; "1.4%" and "2.7%" present but their exact row mapping was not rechecked.
10. Macmillan-Scott: **CORRECTION.** Table 2: GPT-4 correct (reasoned) 0.692, Claude 2 0.550, GPT-3.5 0.292 confirmed. But a26's "GPT-4 human-like 73.3%" is wrong or unexplained: the table gives GPT-4 incorrect-human-like 0.042 and correct-with-poor-reasoning 0.117. The claim "GPT-3.5 50.8% counting human-like correct" also does not match the table (0.292 + 0.042 + 0.217 = 0.551). Use evidence c13 (the table values) and treat a26 numbers for human-like rates as unreliable.

## Contradictions between sources

- Anchoring in LLMs: Suri (GPT-3.5, GPT-4) and Lou and Sun find it; Shaki et al. find none in GPT-3. The difference may be method (choice vs token probability), model, or sample size (Suri cells about 30; GPT-4 only 5 trials). Claim K14 is marked contested.
- Binz and Schulz say GPT-3 resists the cab base-rate error but fails on perturbed versions; Suri/Malberg show broader biases. This fits recall of known items, not rule use.
- Human anchoring itself: explicit anchors replicate (Many Labs 1); incidental anchors failed in Many Labs 2 (d 0.04 vs 0.30).
- Named-bias prompts: Sumita finds AwaRe helps, Echterhoff finds awareness gives small and uneven gains. Contested.
- Evidence a21 gives 60 humans, b21 says 61 mTurk participants. Minor; the paper table says 30 per cell.

## Weak spots

- Many agents (a, b, c) covered the same LLM papers, so claim "independent sources" counts distinct papers, not evidence lines.
- Most LLM studies are on 2022-2023 models (GPT-3, Llama-2). Current frontier models are almost untested; only the 2025-2026 anchoring and SACD studies are recent.
- CRT and Linda are public; contamination cannot be separated from competence.
- Bias scores in LLM papers are treatment-minus-control gaps; they measure sensitivity, not accuracy. Low bias can come from refusing or answering at random (Llama 1B in Malberg; base-model position bias in Itzhak).
- Human replication evidence is strong for framing and anchoring, thin for availability, representativeness (no large replication found), and conjunction fallacy rates.

## Seen only in snippets or not opened

- a13 (Tversky and Kahneman 1983 Linda), a14 (Kahneman and Frederick 2002), a15 (Gigerenzer / Kahneman and Tversky 1996), a16 and b05 (Many Labs 1, HTTP 403), b24 (Gigerenzer and Gaissmaier 2011), b25 (Kahneman and Klein 2009), b26 (Morewedge 2015), c29 (Machine psychology, abstract only). b22 gains not transcribed.
- Many Labs 1 numbers come second-hand through Kuhberger 2023.

## GAPS

1. Do current frontier and reasoning models (2025-2026) still show anchoring, framing and conjunction errors when items are novel and contamination-controlled, and at what rates?
2. At equal tokens, does a prompt-rewrite or counter-anchor step beat plain chain of thought and self-consistency on bias gap and on accuracy?
3. Which biases actually cost accuracy on our agent's tasks (planning, forecasting, code review) as opposed to merely shifting answers in synthetic vignettes?
4. Do debate and Reflexion really amplify bias, and under what conditions (SACD result is a single paper)?
5. Large-scale human replication data for availability, representativeness, base-rate neglect and the conjunction fallacy under natural frequencies (Gigerenzer rival account).
6. Does the Kahneman-Klein condition (regular environment plus feedback) have an LLM analogue: when is the model's first-answer intuition trustworthy, and can verbal confidence flag it?
7. Is instruction-tuning bias amplification (Itzhak) reproduced in current open models and does it depend on position bias rather than value choice?
8. Does few-shot or in-context debiasing transfer to held-out task types, or only to the example type (Hagendorff 2% to 92% is same-type)?
9. How reliable is any bias probe across prompt wording and sampling runs (test-retest) for LLMs, mirroring Aczel and Berthet on humans?


## Gap search results

Date 2026-11-19. Evidence file evidence_d.jsonl (d01-d20, 18 opened, 2 abstract-only). Search budget was exhausted after three searches, and the arXiv, OpenAlex and Semantic Scholar APIs returned rate-limit errors, so gaps 5 and 6 rest on thin evidence. New claims K23-K28 were added and K05, K11, K12, K14-K18, K20 were updated in claims.jsonl.

1. Frontier models on novel items (PARTLY CLOSED). AnchorBench (d03) tests GPT-5.4-mini, Claude Haiku 4.5, Gemini 2.5 Flash and Grok-3-mini: irrelevant anchors move answers about 0.00-0.02 (index scale), plausible anchors 0.07-0.16 on External, with control accuracy 96-100%. SynAnchors (d05) finds anchoring on 22-25% of novel items even for reasoning models. Knipper (d01) finds representativeness resistance 0.53-0.72 for o4-mini, gpt-4.1 and Claude 3.7. Still open: no source tests the largest 2026 models with contamination control on conjunction or framing items.
2. Equal-token comparison of prompt rewrites (STILL OPEN, better informed). No paper matches tokens. Direction: ignore-instruction and evidence-first estimation help (d04, d06), self-check can worsen anchoring (0.26 to 0.45), axiom elicitation halves sensitivity (d08, 12.9% to 6.3%), generic debiasing backfires on judgment biases (d12, -4.4%). K16 is now contested.
3. Which biases cost accuracy on agent tasks (PARTLY CLOSED). Software-engineering dilemmas (d07, d08) and search agents (d15) show decision flips; confirmation (+33.7 pp) and framing (+23.1 pp) grow with reasoning steps; dead-end history cut Qwen's switching from 87% to 23.5%. Still open: planning, forecasting and code review as measured against ground-truth outcomes, not flips.
4. Debate and Reflexion amplify bias (MOSTLY CLOSED for debate). Three papers now agree (d09, d10, d11), K17 is established. Reflexion-specific evidence is still only SACD.
5. Large human replications of availability, representativeness, base-rate neglect, conjunction (STAYS OPEN). Only abstracts of two meta-analyses were read (d17 natural frequencies, d18 incentives, d = 0.19). No large preregistered replication of Linda or base-rate rates was found.
6. Kahneman-Klein analogue and verbal confidence (STAYS OPEN, negative lead). Stated confidence is weakly tied to correctness (d16, r up to 0.175, one preprint). No study tests regularity-plus-feedback as a trust condition for LLM first answers.
7. Instruction-tuning amplification (PARTLY CLOSED). Position bias is large (first-option picks 77-79% vs 36.8% chance, d12) and dialogue format alone shifts bias (d14). No direct reproduction of Itzhak on current open models; K11 now contested.
8. Transfer of in-context debiasing to held-out tasks (STAYS OPEN). No new transfer test found. CogBias shows prompt debiasing differs by bias family (d12), which suggests poor transfer across families.
9. Test-retest reliability (PARTLY CLOSED). Wording instability 10.5% vs 6.3% for repeats (d19, stereotype tasks), and session-to-session flips (d20). No LLM study with a formal test-retest coefficient on classic heuristics tasks was found.

Caveat: several new sources are 2026 preprints not peer reviewed (d03, d12, d14, d15, d16), and most test mid-size or cost-tier models.
