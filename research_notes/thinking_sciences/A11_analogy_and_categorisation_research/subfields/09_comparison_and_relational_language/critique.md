# Critique: A11.09 Comparison and relational language

## Numbers re-opened (arXiv full text, this session)
1. Chia et al 2023 (2311.09277), Table 2: GSM8K CoT 69.2 to contrastive 79.0 (+9.8); Bamboogle 40.8 to 56.8 (+16.0); with self-consistency GSM8K 71.0 to 86.2 (+15.2). Confirmed.
2. Yasunaga et al 2024 (2310.01714), Table 1: four rows (0-shot, 0-shot CoT, 5-shot CoT, self-generated). GPT-3.5 GSM8K 75.0 / 75.8 / 76.7 / 77.8. CORRECTION: evidence b27 labelled 75.0 as 5-shot CoT; it is 0-shot. a22/c08 are right. The real gain over 5-shot CoT is only +1.1 on GSM8K and +2.4 on MATH for GPT-3.5.
3. Lewis and Mitchell 2024 (2402.08955): humans 0.753 [0.734,0.773]; GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452. Confirmed (the pdf table text is scrambled but the values match).
4. Stevenson et al (2411.02348), Table 2: GPT-4o .85/.63/.48; Llama .79/.74/.27; Claude-3.5 .68/.62/.46; Gemma .60/.39/.14; adults n=62; children n=41. CORRECTION: runs per model are 54 (c07 says 55; a19 cites adults 68 / children 44, which is an earlier version).
5. Webb, Holyoak, Lu 2023 (2212.09196): digit-matrix OR=1.88, p=.005; story near p=0.0039, far p=0.065; human vs GPT-3 OR=0.37, p=0.0003; semantic distance OR=3.24, p=0.0165. Confirmed. Human near t(53)=21.5; far t(53)=16.7.
Not re-opened (no time/source reached): Gentner and Markman 1994/Markman and Gentner 1993 counts (a06, b01, b04 agree with each other, and a03 matches), Loewenstein and Gentner 2005, Gentner et al 2003, Kurtz and Gentner 2013, Sourati ARN (arXiv id not found by search; I used the evidence files). Five of ten target numbers confirmed, one label error found, two small count errors.

## Contradictions
- 1993 vs 1994 versions of Exp 1: 11.38 vs 11.44 pairs, 9.09 vs 8.97 alignable. Small, probably re-analysis; same lab.
- Letter-string: Lewis and Mitchell say models fail on counterfactuals; Webb et al 2024 say GPT-4 shows human-like error rates (46% vs 39% alternate-rule) and no old/new alphabet effect. Unresolved; depends on error-type scoring and on code use.
- Yasunaga gains are large for weak models (text-davinci-003 14.8 to 61.0 vs the 0-shot row) but small for GPT-3.5; the headline "+4% average" hides this.

## Weak spots
- Founding human data are almost all from one lab (Gentner/Markman) and its students. Independent replications are not in the files; the failed-replication slot is empty. K05 to K07 are single-source.
- Many "independent sources" counts for LLM claims treat different benchmarks as independent; they share authors or prompts in places.
- No LLM study here tests alignable vs nonalignable differences. The mapping from the human effect to agent S2 is by analogy only.
- Contrastive CoT and analogical prompting are prompt-format effects on 2023 models. They may shrink on current reasoning models.

## Only seen in snippets or not opened
a25, a26 (cited via Kurtz and Gentner), b19 Alfieri meta-analysis, b20 critics of alignment, c21-c25 (SME, MAC/FAC, Copycat, LRA), a24/c14 ANALOGICAL (scores not extracted), c12 few-shot ARN bars.

## GAPS
1. Does an LLM agent rate or choose by alignable vs nonalignable differences the way humans do (triad tasks, equal tokens)?
2. Does forcing explicit correspondence listing (S2) beat free-form comparison for an LLM at equal tokens, on current models?
3. Do contrastive (valid plus invalid) demonstrations still help reasoning models, and is the gain the same as in human comparison?
4. Do self-generated analogues beat retrieved examples for strong models, and on which tasks (Yasunaga gain is only +1.1 on GSM8K)?
5. Is there an independent (non-Gentner-lab) replication of analogical encoding (comparison beats separate study) with effect size, and what does the Alfieri et al meta-analysis actually report?
6. Does supplying a relational label for the discovered structure raise later transfer for an LLM, and does the label need to fit the relation?
7. What are the boundary conditions where comparison hurts (low alignability, novices, high memory load; Hansen and Richland, Kok diffuse diseases)?
8. Can the Lewis/Mitchell vs Webb dispute be settled with a fixed protocol on a current model (code on/off, error-type scoring)?
9. Do far-analogy failures (ARN far 39.6%) come from retrieval from memory or from mapping once both cases are in context?

## Gap search results (2026-11-10)
Limits of this run: the shared WebSearch budget was spent after one call, and the arXiv search, Semantic Scholar and OpenAlex APIs returned 429 for most calls. Sources were opened by direct arXiv and PDF fetch. Evidence is in evidence_d.jsonl (d01-d17); claims K02, K08-K11, K13, K15, K16 updated and K17-K22 added.

1. Alignable vs nonalignable for LLMs: STAYED OPEN. No LLM study found (K15 stands). New human evidence cuts against K02: Estes and Hasson 2004 (second-hand) and Ichien et al 2024 (N=184, opened) point to cognitive complexity, so K02 is now "contested".
2. Explicit correspondence listing at equal tokens: STAYED OPEN. Closest is Self-Discover (structure forcing, GPT-4 BBH 75 to 81), no matched control (d15, K22).
3. Contrastive demonstrations on reasoning models: PARTLY ADDRESSED. Chia ablation shows all invalid-contrast types help GPT-3.5 (d13); DeepSeek-R1 reports few-shot degrades it, no numbers (d14). No direct test on a reasoning model.
4. Self-generated vs retrieved: CLOSED for 2023 models. Self-generation wins only for the strongest davinci-003; retrieval wins for weaker; GPT-3.5 gain +1.1 GSM8K (d10, d11, K19). Not tested on 2025 models.
5. Independent replication and Alfieri meta-analysis: STAYED OPEN. PDF could not be opened; no independent replication or failed replication found (d16, d17).
6. Relational label for LLM transfer: STAYED OPEN. No source found or opened.
7. Boundary conditions: PARTLY ADDRESSED. Ichien Exp 2 (N=129): shallow side-by-side comparison of stories; asymmetry shrinks with separate encoding (d02). Hansen and Richland and Kok were not opened.
8. Lewis/Mitchell vs Webb: PARTLY CLOSED by reading. Webb's reply and Hodel and West were read: the failure is tied to counting; code-execution GPT-4 matched humans (P=0.496). A fixed protocol was not run (no model access) (d04-d06, K20).
9. Far analogy retrieval vs mapping: CLOSED in direction. AnaloBench shows retrieval near random while candidate selection is 89.1/66.5/60.7 (d08, d09, K18). Not the ARN tasks specifically.
