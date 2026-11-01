# Critique: F01.02 Conceptual blending (cross-check of evidence a, b, c)

Scope: evidence_a.jsonl (33 lines), evidence_b.jsonl (25), evidence_c.jsonl (25). Claims: 24 (F01.02-K01 to K24). The earlier gap file evidence_d.jsonl was not used here; the gap searcher continues numbering from K25.

## Numbers re-opened this session (arXiv PDFs, pdftotext)
Confirmed against the paper text:
1. Scideator (2409.14634): CSI median 70.50 (Q1 57.50, Q3 79.00) vs baseline 61.00 (Q1 42.25, Q3 71.50), Wilcoxon V=208.50, p<.01 (c08).
2. Beyond Pixels (2602.01335): Fig. 7 table: full 4.47/4.56/4.51/4.74/4.76; w/o Diag. 4.26/4.05/3.98/4.61/4.48; w/o Trans. 4.01/3.71/3.83/4.33/4.25 (c16).
3. YARN (2603.29997): Qwen MCQ 0.17 against a 0.25 random baseline and ARN far analogy 0.24 against 0.50 (text, p. 9-10) (c22).
4. Olearo 2024 (2407.14280): global mean ranks alternate 2.61, switch 2.26, unet 2.68, textual 2.54; animal category textual 1.98 (c12).
5. Misty (2409.13900): 36.3 min (sd 7.0), 103 operations, 34.95/33.98/18.5/8.74/3.88%, satisfaction 3.2 (sd 1.3) (c18).
6. Matsuhira (2411.03595): BCD 0.621 and MCD 0.862 at the midpoint; averages 0.389 and 0.471; Concept A 0.152 to 1.000, Concept B 1.000 to 0.265 (c10).
7. KOMBINE (2509.21043): 59.0/53.4/43.4% valid; 43.4% valid generic space then 97.1%; 19.9% (412/2,070); humans 22.1/32.9/12.8% (a24-a28, b13).
8. PopBlends (2111.04920): 56.7% overall; kappa .43; 98.3% related scene; 2.03 vs 0.87 ideas; mental demand 2.85 vs 5.80 p=0.004 (a19-a21, c01-c04).
9. CreativeMashup (2504.13120): 666 mashups; winning rate 78.3 experts, 73.5 GPT-4o, 51.0 average humans; IEI rank 1.98 vs 2.40 (b12, b24).
10. Creative Blends (2502.16062): SUS t(23)=-2.547, p=0.018, d=0.800 (b11).

## Corrections and cautions
- Creative Blends (b11): the NASA-TLX table prints t=-4.861 on the Temporal Demand row, while the body text says mental demand t(23)=4.861. Only the SUS result is safe. The per-factor figures in b11 are unverified.
- YARN (c22): the "below chance" numbers are for the cosine-based structural mapper without abstraction, not for an LLM. LLM zero-shot scored 0.37 and chain of thought 0.41 on MCQ; the best abstraction run is 0.46, a small step above chain of thought. Claim K09 states this.
- Matsuhira (c10): the "0.152 to 1.000" belongs to the Concept A row; the MCD row also starts at 0.152 by construction. No error, but easy to misread.
- a25 vs a26/b13: "43.4% valid blend" and "43.4% valid generic space" are one number (a blend counts only if its generic space is valid).
- b24: the 2.40 is the II condition, not a no-blend baseline. It compares two blend prompts.
- Olearo 2024 (c12) vs Olearo 2025 (a23): textual blending wins on animals in 2024 but loses to alternate and switch in 2025 preference (0.60). Not a contradiction in data (different panels, categories, methods), but the ranking is unstable. K14 is marked contested.
- Coulson and Van Petten (a16-a18, b01-b02): the PDF URL no longer resolves; the four lines read the same paper, so they count as one source.

## Contradictions between sources
- Ranking of diffusion blending methods differs across the two Olearo studies (above).
- Scideator (c08) and PopBlends (a21) report large self-reported support gains, but Scideator's rated newness gain is 0.5 on 7 points. Support for "more ideas" is stronger than support for "more novel ideas".
- Privative-adjective results (b08) read as a blending cost, but negation accounts predict the same.

## Weak spots
- The only strong measurement for the agent is KOMBINE: a single preprint, LLM-judged, unaided blending, no scaffold arm.
- Almost all positive tool studies are the authors' own system, small N (10 to 24), self-report. Beyond Pixels has N=100 but subjective ratings and an ablation by the authors.
- No equal-token comparison of a blend step with chain of thought exists in a, b or c.
- Human lab evidence is thin and old (one ERP study N=18).
- Wikipedia lines (a14, a15, b07) are pointers only.

## Seen only in snippets or not opened
Gibbs 2000 (b06), Fauconnier and Turner 2002 (b19), Hilpert 2010 (b21), Schmid noun-noun (b22), Pereira and Cardoso 2003 (b23), Eppe 2018 (c23), Pereira 2006 (c24), VisiBlends (c25), Glebkin's second-hand account of de Vega 2007 and Ferguson and Sanford 2008 (b04). Sato's quantitative claims live in an earlier arXiv paper (2505.00557) not opened. Keon et al. effect sizes (c21) and Scideator ablation scores (c09) were not extracted.

## GAPS
1. Does an explicit generic-space step (propose, then check shared structure, then blend) beat plain chain of thought on reasoning or design tasks at equal tokens? No study tests this.
2. Does a scaffold lift the KOMBINE rate of valid generic spaces above the 43.4% mean, and does another benchmark reproduce the bottleneck (43.4% vs 97.1%)?
3. Do blend prompts add real novelty, or only the cross-model repeats shown by KOMBINE (14.3 times more repeats than analogies)? How many samples or what input variation is needed to escape them?
4. What are solve rates for people and models on the monk riddle and its same-path isomorphs, with and without a "put both on one path" hint?
5. Does selective projection ("what not to carry over") reduce incoherent blends in LLMs, measured without an LLM judge?
6. Do the counterfactual comprehension studies (de Vega 2007; Ferguson and Sanford 2008) contradict the order composition, completion, elaboration? Open the primary papers.
7. How reliable are LLM judges of blend validity beyond 75% agreement on unanimous items, and is there a human-graded harder slice?
8. Is there any failed replication or direct blending-vs-relevance-theory test (Hilpert 2010; Schmid on noun-noun compounds)?
9. Does the fusion-over-replacement advantage in CreativeMashup carry over to text-only blends, and what are the per-type rates?
10. What do computational blending systems (Divago, Eppe 2018 framework, VisiBlends) report as measured results, and do any compare against non-blending baselines?

## Gap search results (evidence_d.jsonl d01-d25; claims K24 changed, K25-K28 added)
Closed:
- Gap 6 CLOSED. Both primary papers opened. de Vega et al. 2007 (d09) and Ferguson and Sanford 2008 (d10; three eye-tracking experiments, 36 students each, first-pass F1(2,35)=5.2, p<.01) support a dual, two-stage reading of counterfactuals. Neither tests the order composition, completion, elaboration, so K24 is no longer a contradiction; it is now established as "does not contradict". Real-world knowledge leaks into the counterfactual space at once.
- Gap 7 PARTLY CLOSED. Vibe Spaces (d18): LLM judge matches the human top-1 blend 35.7% and 31.3% (25% chance); human-human kappa 0.15 to 0.33. Short stories (d19): LLM vs human ICC .43. Still no human-graded hard slice for KOMBINE.
- Gap 10 PARTLY CLOSED. Eppe 2018 (d21) is a proof-of-concept with no baseline. VisiBlends 96% vs 21% (d22) is from a press release only; the paper was not opened.
Stayed open:
- Gaps 1, 2, 3, 5, 9: no study found (d24). The nearest support is indirect (Step-Back, self-generated analogies, Vibe Spaces attribute-first).
- Gap 4: no solve rate for the monk riddle (d14). NazoNazo (2509.14704) is a nearby insight benchmark, not opened.
- Gap 8: no failed replication or blending versus relevance test (d15); Hilpert 2010 could not be matched.
Limits of this pass: arXiv, OpenAlex and Semantic Scholar APIs were rate-limited; 8 web searches used at most; d22, d23, d25 are summary-level and marked opened:false.
