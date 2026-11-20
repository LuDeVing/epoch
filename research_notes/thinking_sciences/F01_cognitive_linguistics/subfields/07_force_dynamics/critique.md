# Critique: Force dynamics (F01.07), cross-check

## Corrections and confirmations (sources re-opened this session)
1. Butnaru et al. 2026 (arXiv 2609.37497): confirmed 0/188 DeBERTa, 5/188 RoBERTa, 0/188 BART; Gemini Flash-Lite 0 / 41 (21.8%) / 188 (100%); probe control 87.5% at layer 4; 29/30 wrong grouping; human 58%/38% and 85%/5% (second-hand from Wolff). Note: this is a single paper about the neo-Gricean M-heuristic with causatives, not Talmy force dynamics proper. The 100% metalinguistic result used item-specific traces, so it may reflect prompt leakage of the gold rule.
2. Siskind 2001 (arXiv 1106.0256): confirmed 6 false negatives, 0 false positives; 4 on assemble, 1 move, 1 unstack. One subject, 35 movies.
3. Wolff and Barbey 2015 (PMC4301188): confirmed Exp 3 N=40, 30/32 vs 26/32; Exp 4 N=24, 23/25 vs 14/25 (p=.69); Exp 1a N=24, 1b N=25, Exp 2 N=20. Correction: evidence a12 omitted the Exp 3 N (40) and a11/b03 agree on N=20.
4. Khemlani et al. 2020 (PMC7888478): confirmed 50 MTurk per experiment, 66% spontaneous omissive conclusion, 1/2/3 possibilities listed 26/35/31%, 10.24 s vs 15.68 s. Correction: the 10.24 vs 15.68 figures are for "causes" only (enables: 10.91 vs 16.28). Author list in a16 omitted Nazari and Johnson-Laird; b07 is right. The 64% vs 8% figure was not re-found in the page text (probably in a table or figure caption); treat as unverified.
5. Weissweiler et al. 2024 (arXiv 2403.06965): confirmed 69.75, 68.12, 57.07, 43.20 on 765 sentences. This is the caused-motion construction, not force dynamics; a weak link.
6. Nie et al. 2023 MoCa: confirmed 43.1, 41.3, 36.1, 35.4.
7. Kiciman et al. 2023: confirmed 86.6% vs 46.6% on 15 vignettes, 97%, 92%. 
8. Not re-opened (taken from earlier agents): Ju and Kim 2024 numbers, Cheung 2026 numbers, CLadder, Carro, Zadrozny, Gillman, Luo, Wu and Lu, CLEVRER, Physion.

## Duplicates
a05/a06/c01/c02 are one source (Siskind). a07-a12 and b01-b06 are one source (Wolff and Barbey 2015). a16/b07-b09 are one source. a24/b21 are one source. Independent-source counts in claims.jsonl count these once.

## Contradictions and tensions
- Force theory vs causal model theory: tie on 23/25 in Exp 4; no separating evidence. Mental model theory is weaker only on composition, not on listing tasks.
- Double prevention: force theory predicts ALLOW 62% / CAUSE 38%; data show about 50/50 whole-chain, 39% ALLOW (Exp 3), PREVENT 65% in abstract text. The theory's own authors call it ambiguous.
- Omissive causes: 35% vs 37% acceptance (no difference) but slower listing; humans are fine with absences, but representation cost is higher.
- Butnaru finds LLMs blind to pragmatic causative forms under default NLI while Kiciman finds GPT-4 strong on vignettes; different tasks, not a real conflict.

## Weak spots
- Talmy (1988) itself was never opened (403); it was read through Wikipedia. Goddard and Deane debate only via Wikipedia.
- Most Wolff studies are abstract-only (2003, 2007, 2010) and use animations with 20 to 40 undergraduates each from one lab. No independent replication of Wolff and Barbey found.
- No direct LLM test of force dynamics exists in what we found; all LLM items are adjacent (causal reasoning, NLI pragmatics, intuitive physics). Search of arXiv was partly rate-limited, so absence is not proof.
- Physics benchmarks (GRASP, Flip Test, Physion) measure vision, not force-dynamic language.
- Claims K02, K03, K10 rest on one lab or one paper each.

## Snippet-only items
a13, a14, a15, a18, a23, b12-b18, b22, c25 (search log), c26 (titles only).

## GAPS
1. Does tagging causal claims with force slots (tendency, opposing entity, balance, outcome) beat plain chain-of-thought at equal tokens on MoCa, CLadder rungs 2-3 or Wolff-Barbey vignettes?
2. Does the Butnaru M-heuristic result replicate with other LLMs (Claude, GPT-4-class) and with a short principle prompt versus a long item-specific one at equal tokens?
3. Has any independent lab replicated Wolff and Barbey's chain-composition table (cause/allow/prevent), and how do LLMs fare on the composed relation?
4. How do LLMs handle double prevention and omissive causes (the ambiguous cells) compared with the human 50/50 split?
5. What does Talmy (1988) actually say about psychological and social forces (persuade, urge), and has this been operationalised for agents or dialogue systems?
6. Is there any 2023-2026 paper on LLMs and force-dynamic verbs (prevent, let, help, despite) such as event-structure or causal-verb probing outside Europe PMC and arXiv (ACL Anthology, Google Scholar)?
7. Do force-dynamic scaffolds help tool-use or planning agents where a blocker (antagonist) must be identified, versus plain obstacle listing?
8. Does Cheung et al. 2026 responsibility pattern (B over A, intent over proximity) hold for LLM blame ratings at equal tokens?

## Gap search results (2026-11-20)
Evidence is in evidence_d.jsonl (d01-d18). OpenAlex hit its daily budget and the arXiv API returned 429 mid-session, so "no study found" is weak evidence. Used 6 WebSearch calls.

1. Force-slot tagging vs plain chain-of-thought at equal tokens: OPEN. No study. Adjacent warning (d09, Caliper 2026): a 5-step structured scaffold cut mean normal-condition accuracy of five small models on CLadder from 62.6% to 57.2%, and CausalCoT left 48.1% of answers unparseable. Added claim K18.
2. Butnaru M-heuristic replication with other LLMs or a short principle prompt: OPEN. Only the original paper exists (d14).
3. Independent replication of Wolff and Barbey composition; LLMs on composed relations: OPEN. Only the theory's own lab (Wolff et al. 2010: N=30, 75, 36, 48; d03). No LLM test (d15).
4. Double prevention and omissive causes: PARTLY CLOSED for humans, OPEN for LLMs. Humans: Wolff 2010 gives 97/73/80% double-prevention descriptions vs 3/17% controls, but Henne and O'Neill 2022 and Lombrozo 2010 find people deny the double preventer is a cause, and order effects (Thanawala and Erb 2024) are reproduced by a counterfactual model (d05, d18). K04 stays contested. LLMs: CaLM omits enablement and disablement (d07); CRAFT is pre-LLM (d06). Added K17.
5. Talmy 1988 on psychological and social forces: CLOSED on the primary text (d01, d02, ch. 7 opened from the author's site). Sections 6 and 8 cover urge/persuade/relent and argumentation logic gaters. Operationalisation for agents or dialogue systems: none found. Added K15 (single-source).
6. LLMs and force-dynamic verbs outside arXiv and Europe PMC: MOSTLY OPEN. Nothing peer-reviewed; adjacent only (d11 Kankowski 2025, d12 CxMP 2026, d06 CRAFT). An unreviewed web note claim about GPT-4 is untraceable (d17). ACL Anthology search page not queried directly.
7. Blocker (antagonist) identification scaffolds for tool-use or planning agents: OPEN. No paper found (d16). d13 (CoT lets GPT-4o match humans, 85%, on affordance reasoning) is only an analogy.
8. Cheung 2026 responsibility pattern for LLM blame: PARTLY CLOSED. LLMs blame by actual force, humans by effort plus counterfactual effort (d04: LLM Force model r=.35-.82; humans ensemble r=.90-.92); GPT-4 matches human causal ratings on Icard et al. structure at r=.68 over 16 cells, other models not (d08). The B-over-A chain pattern itself is untested on LLMs; Carro and Lagnado 2026 is human-only (d10). K06 changed to contested; K16 added.

Corrections to earlier work: none found; Talmy's argumentation section is now a primary-source item rather than Wikipedia-derived.
