# A16.01 Conceptualization (grounded cognition): critique

## Corrections made (sources re-opened this session)
1. Zwaan and Pecher 2012 (PLoS ONE full text): Exp 1a 33 ms (N=164), 1b 38 ms (N=172), 2a 57 ms and 2b 70 ms (N=176 each), 3a/3b N=152 each, 3a 157 ms match advantage. Confirmed. Correction: a12 gives N about 186 and 189 for Exp 3; analysed N is 152 each (recruited more). Exp 1b sits in the table as 44 ms in one parse, the text says 38 ms; text used. Added nuance: Exp 3a/3b pooled BF01 was 5.26 on trimmed RTs (supports no effect) but under 0.01 on medians, so the colour result depends on the RT treatment.
2. Morey et al. 2022 (Springer PDF): 1,492 recruited, 214 excluded, N=1,278; ACE CI95 [-0.006, 0.004] on log lift-off; originals 155 ms (1,766 ms mean) and 170 ms (1,871 ms), about 9 percent. Confirmed. a09 and c18 are the same paper, so K01 counts as one source.
3. Marjieh et al. 2023 (arXiv 2302.01308): pitch IRR .90 [.87,.92], consonants .46 [.36,.56]; gain over other models r=.15 colours, .16 pitch, .16 taste, .14 consonants. Confirmed. CORRECTION to a21: colour naming ARI English is GPT-4 0.59 [0.56,0.63], GPT-3.5 0.50, GPT-3 0.39 (a21 said 0.54 and 0.35). Also the paper itself argues the gain reflects richer text, not images.
4. Abdou et al. 2021 (arXiv 2109.06129): BERT mini to base RSA max .077 to .162, linear-map max .729 to .740; shuffled controls non-significant (p>.05); warm colours align better. Confirmed.
5. Xu et al. 2025 (Nature Human Behaviour PDF): N=829 and 3,500, about 4,442 words; published-version tests: sensorimotor (n=7) vs non-sensorimotor (n=11) GPT-4 U=65, P=0.018, rrb=0.69; GPT-3.5 U=67, P=0.010, rrb=0.74; imageability Rs=.69, concreteness Rs=.62. Confirmed for c01/c02. WARNING: b11 reports U=10 p=.004 and median rho 0.64/0.77; these did not match the published text (the 0.64 I found there belongs to an arousal row). They likely come from the earlier preprint. Treat b11 medians as unverified; prefer c01.
6. Not re-opened (budget, rate limits): Kim 2019 (b06), Wagenmakers 2016 RRR (a26, b18), Many Smiles 2022 (b19), Coles 2019 (b20), Chlapanis 2026, Roy 2026, Rosenberg 2026, Liu 2025, Zhuang 2024, Li 2021. Their numbers rest on the earlier agents' reading.

## Contradictions between sources
- Vision causes gain? Xu 2025 ties gain to visual association; Marjieh 2023 says gain is not vision-driven. Neither isolates vision.
- Zwaan and Pecher say the replications support simulation; Morey 2022 says one flagship motor effect is null. The field result depends on paradigm.
- Colour: Marjieh finds text alone gives human-like colour structure; Liu 2025 shows blind effect (.21) far below sighted (.60); Kim 2019 shows blind gaps on size. Both can be true: text gives a lot, not all.
- Chlapanis 2026 (r<=.37 on free property generation) vs rating alignment r about .6-.8: the task format decides how grounded a model looks.

## Weak spots
- Almost all LLM evidence uses prompted ratings or similarity tasks, not use in action or reasoning.
- Several effect sizes (b18, b19, b20) came from memory or snippets.
- c13 (conceptual metaphor prompting) has an LLM judge and no statistics.
- No source tests a scaffold step derived from grounded cognition at equal tokens. Relevance to our agent stays background.

## Only seen in snippets or abstracts
a03, a13 to a16, a18, a19, a24, a26, a27, b18 to b23, c20, c21.

## GAPS
1. Does any study show that prompting an LLM to simulate or imagine the situation (state sensory and motor details) improves reasoning accuracy at equal tokens?
2. Did the Wagenmakers 2016 RRR and Many Smiles 2022 effect sizes check out against the full papers (pooled estimates, moderators)?
3. Do the 2025 Frontiers third-person ACE results hold against the Morey null, and what N and effects were reported?
4. How big is the Coles 2019 facial-feedback meta-analytic effect after bias correction?
5. Which LLM benchmarks test affordance or physical commonsense, and does grounding (multimodal training) help them at fixed scale?
6. Do metaphor-framed prompts (Lakoff and Johnson style) beat plain prompts in a human-judged, significance-tested study?
7. Is there evidence that LLM concept representations (probing) causally mediate behaviour on perceptual concepts (interventions beyond Li 2021)?
8. How large are the Petilli 2024 blind vs sighted differences, and do they hold for abstract concepts?
9. Does the Solomon and Barsalou associative-vs-simulation boundary carry over to LLM property verification?

## Gap search results
Search tools were mostly down: WebSearch budget ran out after 2 calls, arXiv search, Semantic Scholar and OpenAlex were rate-limited. Evidence came from direct arXiv PDFs, Europe PMC and a few publisher pages (evidence_d.jsonl d01 to d16).

1. Imagery prompting at equal tokens: STAYED OPEN. Visualization-of-Thought (d01) gives GPT-4 gains on spatial tasks (tiling 63.94 vs 54.15 CoT) but tokens were not matched and it is a state trace, not sensory imagery. Mind's Eye (d03) uses an external simulator; SimToM (d04) is perspective-taking and fails for GPT-4. New claims K19, K20.
2. Wagenmakers 2016 RRR and Many Smiles: HALF CLOSED. RRR verified from the PDF (N=1,894, 0.03 [-0.11, 0.16] vs 0.82). Many Smiles is paywalled; only the abstract was read (n=3,878; mimicry and voluntary action work, pen-in-mouth inconclusive). Pooled effects and moderators unverified.
3. Frontiers 2025 third-person ACE: CLOSED (weakly). About 117 and 115 analysed per experiment; effects only in one direction or axis and dependent on animacy and priming; the paper cites the Morey null. A JEP:LMC 2025 series also reports no robust ACE. K01 upgraded to established.
4. Coles 2019 bias-corrected effect: STAYED OPEN for the number. Abstract confirms 286 effects, 138 studies, small and heterogeneous, bias for affective judgments only. The R dataset psymetadata could recompute it.
5. Affordance and physical benchmarks: CLOSED. PIQA (human 94.9 vs RoBERTa 77.1 in 2019), ViComTe (multimodal beats BERT, scale does not help), VEC (CLIP/BLIP beat OPT-175B on embodied concepts such as mass). Frontier-LLM numbers on these are not measured here. K21.
6. Metaphor-framed prompts, human-judged: STAYED OPEN. No source found; K17 stays single-source and weak.
7. Causal mediation of LLM concepts: PARTLY CLOSED. Othello-GPT intervention (errors 2.68 to 0.12) and Gurnee and Tegmark (probes, authors say use unproven). Nothing for perceptual concepts. K14 extended.
8. Petilli 2024 blind vs sighted: STAYED OPEN (paper not located). Related: Liu 2025 and Anceresi 2025 (N=42) support language compensation; abstract concepts untested. K22.
9. Solomon and Barsalou boundary for LLM property verification: STAYED OPEN, no LLM study found.

Caveats: d13 N values inferred from degrees of freedom; d14 author name inferred from a citation; d15 r values not re-found.
