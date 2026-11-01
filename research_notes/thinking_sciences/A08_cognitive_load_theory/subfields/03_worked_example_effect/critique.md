# Critique and cross-check: Worked-example effect (A08.03)

## Numbers re-opened this session (arXiv full text via pdftotext)
Confirmed: Wang et al. (2023) GSM8K 15.4 / 48.5 / 39.5 / 23.1 / 11.0 (b16, c05); Wei et al. (2022) PaLM 540B GSM8K 17.9 to 56.9 (+39.0) (c06); Kojima et al. (2022) 17.7 to 78.7 and 10.4 to 40.7 (c07); Min et al. (2022) 1.7 and 2.6 average cost of random labels (c04); Agarwal et al. (2024) Minerva 4-shot 55.7 / 90.6, human-solution ICL peaks near 125, Reinforced ICL plateaus near 25 (b18, c10); AdaptMI Table 1 (57.2 vs 53.0 on MATH avg for Qwen2.5-1.5B, gains up to 3.6 and 6) and easy-question GSM8K 96.3 fixed vs 83.2 skill-based (-13.1) (c01, c02); Voyager ablations -93% random curriculum, -73% no self-verification (c14).
Corrections and clarifications:
- c04 says "0 to 5 points"; the paper text re-read shows the averages 1.7 and 2.6 only. The 0-5 range was not re-found; treat as unverified.
- b01 vs b02 vs b21: Barbieri et al. g = 0.43 (40 articles, 49 studies, 185 effects, preprint/poster) vs g = 0.48 (43 studies, published, via snippets). These are two versions of one analysis, not two sources. Use 0.43 to 0.48 and count it as one source.
- b16 and c05 are the same paper (Wang et al.); b17 and c04 the same paper (Min et al.); b18, b19, c10, c11 one paper (Agarwal et al.). Independent-source counts in claims.jsonl reflect this.
- a25 (Sweller and Cooper 1985 "half the time, one fifth of the errors") is from Wikipedia, unverified; not used in any claim.
- Not re-opened (no access this session: OpenAlex quota exhausted): Barbieri paper itself, Schwonke 2009 numbers, Salden 2009 Ns, Pardos and Bhandari. These numbers stay as recorded.

## Contradictions between sources
- Self-explanation: Renkl et al. 1998 trained SE helps (a18); Barbieri finds prompts moderate the effect negatively (b02).
- Few-shot: Agarwal says reinforced many-shot helps (b18); DeepSeek-R1 says few-shot degrades (c22, one sentence, no data); the Substack test (c23) is a toy and secondary.
- Variability: Paas and van Merrienboer found no main effect of variability (a19) vs. Quilici and Mayer null for 3 vs 1 example (b09).
- Adaptive fading: lab win, classroom partial (b11).
- Sweller (2023) says the effect failed for years in geometry and was rescued by split-attention fixes (b04); that is the author's own account of his own program.

## Weak spots
- Most CLT evidence is a review by the theory's own authors (Sweller 2011, 2023; Sweller, van Merrienboer, Paas 1998). Few independent replications with Ns.
- Meta-analysis: I2 = 94%, no moderator significant, so "medium effect" hides a wide spread (-1.80 to 4.66). Publication bias is not reported in what was read.
- No LLM study tests the CLT effect itself. All LLM items (CoT, ICL, AWM, Voyager) are analogies; they vary exemplar content, not load.
- LLM results are mostly 2022 models; the one reasoning-model data point (DeepSeek) has no numbers.
- Evidence lines a25, a26, a27, b03, b23-b25, c23, c24, c26, c29 were not opened or are snippets.

## What was only seen in snippets
a25, a26, a27, b03, b23, b24, b25, c23, c24 (abstract), c26. Pillay 1994, Quilici and Mayer 1996 and Paas 1992 come from Wikipedia (b09).

## GAPS
1. Does any 2023-2026 study give an LLM agent either worked solutions or bare problems at matched tokens, and measure the difference, with reasoning models (o1-class, R1-class)? Is the few-shot degradation real and how large?
2. Is there an expertise-reversal analogue for LLMs: at what model strength or task difficulty do stored solutions stop helping or start hurting (beyond AdaptMI's easy-vs-hard split)?
3. What are the exact Ns and effect sizes in Schwonke et al. 2009 (cognitive tutor, fading) and Salden et al. 2009, and the original Sweller and Cooper 1985 numbers?
4. Does the Barbieri meta-analysis report publication bias tests, and is g = 0.43 or 0.48 the right published figure? Are there other meta-analyses (Crissman 2006; Wittwer and Renkl 2010 on instructional explanations)?
5. Do self-explanation prompts help LLM agents reading a stored solution (explain-then-use) at equal tokens?
6. Does solution correctness matter for an agent library (verified vs unverified self-generated solutions), beyond Wang's invalid-reasoning result?
7. How does the number of retrieved examples (k = 1, 2, 4) interact with relevance ranking for subgoal libraries, given Agarwal's decline past 125 and Yasunaga K=1 vs 3-5?
8. Does fading (removing steps from the stored solution over repeated use) beat full solutions for agents, as in human adaptive fading?
9. Which LLM tutoring studies (2024-2026) measure learning from LLM-generated worked examples with test scores (not ratings)?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d18). WebSearch quota was used up and OpenAlex/arXiv search were rate-limited, so work went through Crossref, direct arXiv/Springer/Nature pages and a CMU-hosted PDF. Claims K02, K05, K06, K11, K17 updated; K18 to K22 added.

1. **Reasoning models and stored solutions: mostly closed.** "From Harm to Help" (2509.23196) measures it: one CoT demo cost about 6 to 16 AIME-2025 points, three cost up to 35, GPQA 1 to 8 points. Distilling demos to short insights reversed it. Cheng et al. and Zheng et al. add that strong instruct models gain nothing beyond format, and that direct beats CoT by 5.10 points on pattern-ICL. The R1 paper sentence was re-opened: still no data. Still open: no matched-token example-vs-bare-problem test, and only k = 1 and 3.
2. **Expertise-reversal analogue: partly closed.** Exemplars help weak or base models and do nothing for Qwen2.5-72B (GSM8K 95.75 vs 95.83). The threshold is ragged. No clean strength-by-difficulty curve.
3. **Exact Ns (Schwonke, Salden, Sweller and Cooper): open.** All three are paywalled or blocked. Learned: the Schwonke 2009 paper is in Computers in Human Behavior, not Learning and Instruction; the Salden adaptive-fading paper is Instructional Science; a review of eight tutored studies gives counts (5 of 8 saved time; conceptual transfer benefit 1 of 4; long-term retention 3 of 3).
4. **Barbieri: closed on the figure, open on bias.** Published abstract: g = 0.48, 43 articles, 55 studies, 181 effects. The 0.43 / 49-study figure is not in the journal text. Publication-bias tests are not visible (paywall). Wittwer and Renkl 2010 found (21 studies). Crissman 2006 not found.
5. **Self-explanation prompts for LLMs: open.** Only indirect: own-voice explanations beat human ones (d10, abstract only); Barbieri's prompt moderator is negative.
6. **Solution correctness: closed in direction.** Add-all memory fell below a small fixed memory; strict-checked adds raised EHRAgent from 16.75 to 38.50. Caveat: records are task outputs, not subgoal solutions.
7. **k and relevance: partly closed.** Over-prompting peaks near 5 to 20 in classification; agents used k = 6 to 10. No k = 1, 2, 4 sweep for subgoal libraries.
8. **Fading for agents: open.** Only the human adaptive-fading result (adaptive > fixed > problem solving; retention gain), taken from an abstract and a review.
9. **Test-score tutoring studies: mostly open.** The Kestin et al. RCT (194 analysed, 0.63 SD) used step-by-step solutions inside the tutor prompt, but is not a worked-example manipulation. No 2024-2026 study found that tests learning from LLM-generated worked examples against problems.
