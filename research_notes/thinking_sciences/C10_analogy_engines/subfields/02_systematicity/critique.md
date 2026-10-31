# Critique: Systematicity (C10.02)

Cross-check of evidence_a, evidence_b, evidence_c. Sources re-opened this session as extracted text: Clement and Gentner 1991, Gentner Rattermann Forbus 1993, Gentner and Toupin 1986, Falkenhainer Forbus Gentner 1989, Colhoun and Gentner 2009, Myers and Gentner 2017 (CogSci proceedings), Lee and Holyoak 2007, Lewis and Mitchell 2024 (two papers), Sourati et al. 2024, Webb et al. 2023.

## Numbers re-checked and confirmed
- Clement and Gentner Exp 1: N=48, F(1,44)=13.15 for choices; Exp 2 choice 2.9 vs 1.8, F(1,28)=16.43.
- Gentner Rattermann Forbus 1993: soundness F(2,58)=70.51, analogy 4.40 vs surface 2.80 vs first-order 2.74; recall .78/.44/.25; relational F(1,19)=85.78.
- Gentner and Toupin: Age F(1,68)=14.93, Systematicity F(1,68)=6.28.
- SME: 80% trickle-down, SES 4.04 for the temperature rival, Karla 22.4 vs 16.8.
- Colhoun and Gentner: 7.53 / 6.35 / 5.01, F(2,286)=44.4. Myers and Gentner: 62.28 vs 47.28, t(31)=3.44. Lee and Holyoak: 7.58 / 4.77 / 5.09; strength 33.60 / 58.57 / 35.32.
- Sourati: GPT-4 94.0 / 92.5 / 57.1 / 29.1, avg 68.1; humans 96.0; far 94.1 vs 39.6; near 97.9 vs 75.0.
- Lewis and Mitchell story test: GPT-4 0.86 (31/36), 0.75 for Webb's GPT-4. Webb: near p=.0039, humans t(53)=21.5.

## Corrections
1. b03 labels the .92 vs .13 and 1.875 vs 1.0 results (F(1,44)=5.15 and 13.15) as a free-prediction task in general. They belong to Experiment 3 (base hidden, from memory), as a07 says. Experiment 2 (base visible) gave the larger gap: 1.63 vs 0, F(1,28)=20.05. Claims K01 and K02 use the corrected attribution.
2. b02 says N about 32; the text gives F(1,28), consistent with 32 subjects, but the N itself is inferred, not stated in the passage read. Keep "about".
3. Human letter-string accuracy: b20 gives 0.754; Table 2 gives 0.753 [0.734, 0.773] across all alphabets (the 0.754 is the zero-permutation cell). Minor. Model-to-number mapping (GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452) is read from a scrambled table layout; it matches the label order but the PDF layout is the only basis.
4. Sourati: a26/b24 quote "models 57%" overall humans 96%; the per-model table gives GPT-4 avg 68.1, GPT-3.5 60.3, so 57% is the average over the full model set, not GPT-4. Do not cite 57% as GPT-4.
5. b01 gives the Exp 1 rating scale as 7-point; a04 says 1-9. Not resolved from the text; the means are the same.

## Contradictions between sources
- GPT-4 on far story analogies: 0.86 overall in the Lewis and Mitchell items (a27, b19), above chance and near human, versus 29.1% to 57.1% in ARN far cases (c15). The tasks differ (ARN uses distractors that share surface with the query), so this is a task difference, not an error, but it means "LLMs fail far analogies" holds when surface lures are present.
- Webb et al. (GPT-3 emergent analogy) versus Lewis and Mitchell, Hodel and West (brittle). Webb reply (counting) was tested by one lab with code execution only.
- Lee and Holyoak versus Gentner lab on mechanism (K08): same data, two accounts.

## Weak spots
- Almost every human systematicity result comes from one lab and its students (Illinois, Northwestern, MIT). Independent replications of Clement and Gentner 1991 itself were not found; independence in K01 to K05 is one source.
- Sample sizes are small (N=24 to 72 per study); effect sizes beyond F and p are not reported in the originals.
- The failed passage in Exp 3 and the children null (Gentner and Toupin) are boundary conditions that are rarely cited.
- No LLM study uses a systematicity score as an agent step. LLM evidence is about whether models solve analogies, not whether a systematicity scaffold helps.
- Analogical prompting (Yasunaga, Thought Propagation) is not structure mapping; it should not be counted as support.

## Only snippets or not opened
- a18 (Lassaline 1996) and a30 (Gentner Rattermann Forbus as secondary report; primary was opened in b05 to b07), a24 (ACME), c28, c29, b28 (ConceptARC abstract only; c26 opened) were not read in full.
- b14 relies on a review for the 700-1000 ms deadline result (Goldstone and Medin); original not opened.
- b21 appendix tests not read.

## GAPS
1. Does any experiment in people or models show that scoring a mapping by connected higher-order structure beats a plain LLM judge, at equal tokens, on far analogies with surface lures? (No study found; the main decision question.)
2. Has Clement and Gentner 1991 been replicated by an independent lab, with effect sizes, and with expert or non-student samples?
3. How should an LLM agent get the relation predicates that systematicity needs (re-representation)? Which extraction prompt gives the best mapping precision, and how much does error in extraction cost the final score?
4. Does the trickle-down scorer still prefer the right mapping when case descriptions are bottom-heavy, and does a re-representation or compression step fix swamping?
5. Is the human similarity vs inference dissociation (Lee and Holyoak) reproduced in LLMs, and is it a useful signal that the agent should separate "looks similar" from "supports this inference"?
6. When is systematicity harmful? Boundary cases: children, easy mappings, short time, memory-only mapping, misleading causal chains. What predicts when a connected system is wrong?
7. Do the post-2024 models (reasoning models) still fail ARN far-near cases, and is the failure removed by extra thinking tokens or by tool use?
8. Which direction of base-target choice (Bowdle and Gentner) should the agent use, and does it change inference accuracy?
9. Does retrieving stored cases by relational summary instead of surface text fix the retrieval-soundness gap in an agent memory?
10. What is the cost in tokens of an explicit mapping-score step compared with best-of-N, and where is the break-even?

## Gap search results (2026-10-31, evidence_d.jsonl d01 to d15, claims K21 to K27)
Search limits: the shared WebSearch quota was used up. OpenAlex and Semantic Scholar returned 429. I used the arXiv search page, Crossref, Europe PMC and direct PDFs. Absence of a paper below means "not found with these tools", not "does not exist".

1. Mapping score vs plain LLM judge at equal tokens: STILL OPEN, partly informed. YARN (d01, d02) is the closest. With abstraction, an embedding-based one-to-one mapper was competitive on far items (Llama 0.46 vs 0.42) and worse on near items. Far-near stayed below 0.5. 8B models, no token counts, and not a higher-order score.
2. Independent replication of Clement and Gentner 1991: OPEN. None found (d13). Bowdle and Gentner 1997 (d08) extends it inside the same lab.
3. Getting relation predicates: PARTLY CLOSED on recipe, OPEN on cost. YARN gives a working events-then-frames recipe (d15). Raw phrases scored below chance (MCQ 0.17); abstraction raised it to 0.46. Extraction error itself was not measured.
4. Bottom-heavy cases: PARTLY. AnaloBench (d03) shows LLMs lose far more than people as surface detail grows (GPT-4 89.1 to 60.7; humans 96.0 to 73.3). YARN (d02) shows abstraction level must match the surface overlap. Nobody tested the trickle-down scorer itself on this.
5. Lee and Holyoak dissociation in LLMs: OPEN. No paper found (d14).
6. When systematicity hurts: PARTLY. New cases: near pairs (mapping worse than plain LLM, d01), easy mappings, shuffled/non-alignable pairs (asymmetry shrinks, d08). No predictor of a wrong connected system found. Misleading causal chains remain untested.
7. Reasoning models on far analogies: PARTLY. No ARN retest found. ARCANA (d07) shows GPT 5.2, Gemini 3 Pro, Claude Opus 4.5 below undergraduates on far analogy (best 48-51% over 12 attempts vs 59-69% single attempt), with huge between-model differences. Thinking budget not varied. A ranking study (d09) shows frontier models do well on a different format.
8. Direction: CLOSED for people (same lab). Use the richer, more causally connected case as base (d08: .76 forward comparisons, .80 forward inferences, N=48 each). Effect on LLM inference accuracy untested.
9. Retrieval by relational summary: PARTLY CLOSED. Purpose/mechanism indexing beats surface (d04: 0.739 vs 0.63 precision at 1%; good-idea rate 0.71 vs 0.28). Surface embeddings were near random for reasoning transfer (d05: 38.5 vs random 37.6). Both use learned or trained components, and neither is a prompt-only agent memory.
10. Token cost vs best-of-N: OPEN. No study found.

New caution: d06 shows an LLM judge that accepts wrong analogies on surface grounds (GPT-4 precision about 0.50). That supports a verify step, but the verify step has not been shown to work.
Unverified: first authors of d05, d06, d09, d10 were not recorded from the pages I opened. Corrections from the earlier cross-check (b03, b24/a26, b20, b01/a04) are unchanged.
