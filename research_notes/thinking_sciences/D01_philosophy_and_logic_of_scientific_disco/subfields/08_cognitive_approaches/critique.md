# Critique: D01.08 Cognitive approaches (analogy, creativity, mental models)

Cross-checker pass. Sources re-opened this session (PDF text): Webb et al. 2212.09196, Lewis and Mitchell 2402.08955, Stevenson et al. 2411.02348, Sourati et al. 2310.00996, Shen et al. 2605.11258, Qin et al. 2404.12728, Yasunaga et al. 2310.01714, Webb reply 2404.13070 (search for its numbers only partly matched), Gick and Holyoak 1983.

## Corrections made
1. a12 says GPT-3 beat humans "on generative answers and on multiple choice (OR 6.27)". The paper gives OR 1.88 (p=0.005, CI 1.21-2.91) for generative answers and OR 6.27 (p=2.3e-8) for multiple choice. c01 (OR 1.88) is right for generative; claim K17 states both.
2. b11 gives the letter-string GPT-3 vs human result as p=6.3e-5. The paper says OR 1.76, p=0.0007, CI 1.27-2.46 (c02 is correct). Use p=0.0007.
3. Shen et al. (c23): the body text gives GPT 9.0%/28.2%/58.8% and Gemini 8.9%/37.8%/68.9%, while the table gives GPT 8.8/27.2/58.8 and Gemini 8.6/37.9/68.8. The paper disagrees with itself by a fraction of a point. Cite ranges; Claude 1.6/21.6/50.4 is consistent in both.
4. Lewis and Mitchell table (a10, b15, c04): the PDF text shifts row labels by one cell. Checked against the paper text: humans 0.753, GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452. The record order is right. Alternate-rule errors: GPT-3 5.81%, GPT-4 22.00%, GPT-3.5 38.59% (text confirms the 38.59% for GPT-3.5 and 5.81% for GPT-3).
5. Yasunaga GSM8K/MATH (a19): the extracted table has scrambled labels, but the values read in order are 0-shot 75.0, 0-shot CoT 75.8, 5-shot CoT 76.7, ours 77.8 (GPT-3.5, GSM8K); MATH 33.0/33.9/34.9/37.3. Confirms a19. For text-davinci-003 the column is 14.8/50.3/54.0/61.0.
6. Qin et al. (c10): the Table 5 accuracy columns are Relevant 62.0, N/A 72.0, Random-same 86.0; "no-example variant" in c10 means N/A (no example given). The 2.5% figure is random biology vs relevant math; the paper also says N/A had the best average.
7. Gick and Holyoak (a01, b01): the paper's own summary gives both "30 and 75%" and "30% unprompted and 70% in total" in different places, so cite "about 30% unprompted, 70-75% in total". The 45 vs 21% and 80 vs 53% and 91% figures (a05, b02) were confirmed.
8. Stevenson et al. (c06): all table values confirmed (adults 0.88/0.91/0.89, N=62; children 0.62/0.66/0.67, N=41; GPT-4o 0.85/0.63/0.48; Llama 0.79/0.74/0.27; Gemma 0.60/0.39/0.14; Claude 0.68/0.62/0.46). b18 says only "about 0.62 to 0.67" and 42 children; the paper says 41. Use c06.
9. ARN (a16, c13): confirmed 96.0 humans, 68.1 GPT-4, partition values 94.0/92.5/57.1/29.1, and the 39.6 vs 94.1 and 75.0 vs 97.9 figures. One oddity: the table's average row reads 76.9, 73.2, 45.3, 33.9 and 57.3 for models, so "57%" in a16 is the model average.
10. Webb reply (b17): confirmed N=99 and N=97 and P=0.496 for GPT-4 plus code vs humans. The P=8.9e-13 for plain GPT-4 was not re-matched in the text.

## Contradictions between sources
- Webb 2023 (GPT-3 matches humans) vs Hodel and West, Lewis and Mitchell (collapse on altered alphabets). Webb's reply says counting, not analogy, explains it and shows GPT-4 with code recovers. Both sides agree plain GPT is brittle. They disagree on why. (K05 established, K06 contested.)
- Yasunaga (self-generated relevant analogs help) vs Qin et al. (irrelevant but correct examples do as well or better). The cognitive reading of "analogy" is weakened. Both used GPT-3.5 on maths; unresolved for stronger models.
- Gick and Holyoak: stating the principle did not add to the analog (a03, 32/29/28%), yet b03 reports principle plus diagrams raised schema quality (44% vs 10%). Different conditions and measures, not a clean contradiction, but a principle alone is not reliably better.
- ARN: chain-of-thought lifts far analogies by up to 30 points but lowers near ones. Gains depend on the case type.

## Weak spots
- The classic human results rest on one lab's 1980-87 student studies (Gick and Holyoak; Holyoak and Koh; Needham and Begg). Independent large replications are not in the file. The only effect-size note (b10, d=0.20) is an unopened student blog snippet.
- Hesse, Nersessian, Boden and Holyoak and Thagard (ACME) were not opened (a23, a24, a26, a27). Their content is from memory, so no claim depends on them.
- Gentner 1983 scan was unreadable (a08).
- Spencer and Weisberg 1986 (b09) is known from a search snippet only.
- Most LLM analogy studies use 2022-2024 models; no 2025-26 reasoning-model counterfactual letter-string or ARN results. The Shen 2026 result is a preprint with LLM-judged novelty.
- Thought Propagation (b24) was only skimmed; its gains are author-reported on author-built baselines.
- No study found that tests analogy scaffolds at equal token cost against a plain best-of-N baseline. Almost all gains are unmatched for compute.
- Si et al. (b25-26), SciMON (c25), Mind's Eye (c26), Eisape (c27), Bhavya (c19) and Wijesiriwardene (c18) were not re-opened here; numbers are as recorded by the first agents.

## GAPS
1. At equal tokens, does explicit analogy (O7: two sources, written common rule, then solve) beat best-of-N plain sampling on non-contaminated reasoning tasks? No paper controls for compute.
2. Do 2025-26 reasoning models (with thinking and code tools) still fail counterfactual analogy (altered alphabets, ARN far cases), or does code access remove the gap (Webb reply)?
3. Is the gain from analogical prompting due to example correctness rather than relevance (Qin vs Yasunaga)? What happens if recalled cases are code-verified before use?
4. Can source retrieval by relational description (not embeddings) find far analogs in a memory store, and what hit rate does it reach vs cosine retrieval, given models drop to 33.9% against surface distractors?
5. Does an "attempt the target first, then view the analog" order (Needham and Begg, 83%+ vs 5%) transfer to LLM agents, and does a failed attempt in context help or anchor?
6. Do the analogy-first diversity gains (Shen 2026) survive an independent novelty check (retrieval against prior literature, domain experts) and downstream validity tests by code?
7. Is there any empirical test of transformational creativity (rule change of the search space) in LLM agents, or only argument (Franceschelli and Musolesi)?
8. Are the original Gick and Holyoak effects (two-analog benefit, d about 0.2 per a student note) replicated at scale with proper power, and how large is the effect once base rates are fixed?
9. Does stripping surface content (O6 re-description to a structural form) before mapping reduce distractor pull in LLMs (Musker et al.), and by how much?
10. Does a code-run simulation as the "mental model" (Mind's Eye style) extend beyond physics to causal or social domains where the agent's O7 analogs are used?

## Gap search results

Evidence: evidence_d.jsonl (d01-d16). The arXiv, OpenAlex and Semantic Scholar search APIs were rate-limited, so the sweep used four web searches plus direct page and PDF reads. Absence of a paper below is therefore weak evidence.

1. Equal-token O7 vs best-of-N: PARTLY CLOSED. Liu et al. 2025 (d03) compare analogous prompting with CoT, step-back, least-to-most and others under equal samples or token price on 6 models. AnP falls behind CoT (81.3 vs 88.2 on Qwen2.5-7B). Budget-aware work (d04) shows CoT self-consistency matches or beats debate and Reflexion. But this tests the generic one-pass prompt on maths, not a two-source O7 with a written common rule on structure-bound tasks. Still open for that.
2. Reasoning models on counterfactual analogy: OPEN. No 2025-26 reasoning-model result found (d12). The published Webb reply (d01) is stronger than the arXiv one (P=0.92 vs 0.496; no-code control 22.5%; CoT still below humans, P=3e-8), so the code-fixes-counting reading is better supported, still by one group and GPT-4 only.
3. Correctness vs relevance: OPEN. No new evidence beyond Qin; d03 is consistent with a weak benefit of self-generated analogs. Code-verified recall was not tested in anything found.
4. Relational retrieval vs cosine: PARTLY CLOSED. Barakat and Kochmar 2026 (d11): sub-concept (relational) descriptions lift average closed-set retrieval from 0.557 to 0.673, and gold-sub-concept re-ranking gives 24.5% Hit@1 vs 19.5% embedding-only. Model-written sub-concepts gave only 18.2%. AnaloBench (d06) shows long-context model recall is near chance. Hit rates remain low.
5. Attempt-first order for LLM agents: OPEN. No LLM test of the Needham and Begg order found.
6. Independent check of analogy-first novelty: PARTLY CLOSED. Si et al. 2025 (d09, d10) is an execution check of LLM ideas in general (N=43, over 100 hours each). AI ideas lose 1.0-2.0 points after execution vs about 0-0.6 for human ideas, and idea-stage scores barely predict execution scores. No such check of the Shen 2026 analogy-first pipeline itself.
7. Transformational creativity test: OPEN. Nothing new found (search budget ran out before this query).
8. Gick and Holyoak at scale: OPEN. The Alfieri, Nokes-Malach and Schunn 2013 meta-analysis (d14) is the right source but its abstract and effect size could not be read this session. No number is claimed.
9. Surface-stripping before mapping: OPEN, with indirect support. Musker et al. 2025 (d08): semantic distractors cost GPT-4 about 0.6-0.8 and Claude 3 and Llama-405B about 0.4-0.5 in match to reference, vs small human drops. StoryAnalogy (d07): hard negatives chosen 56-60% of the time. No test of re-description as a fix.
10. Code-run simulation beyond physics: OPEN. Nothing new found.

Claims changed: K06 text updated with published numbers; K07 promoted to established (three independent benchmarks); K10 moved to contested (equal-compute result); K13 and K16 strengthened; K12 given a caution; K03 gets d06. New claims K21 (retrieval by model reading is near chance), K22 (equal compute favours plain CoT), K23 (counting vs analogy), K24 (varied contexts).

Corrections to earlier files: the Webb reply P for GPT-4+code vs humans is 0.92 in the published PNAS Nexus version (0.496 in arXiv v2). The P=8.9e-13 for plain GPT-4 in b17 is confirmed in the v2 text. AnaloBench text says the GPT-4 gap at 30 sentences is 28.8 points but its table gives 12.6.
