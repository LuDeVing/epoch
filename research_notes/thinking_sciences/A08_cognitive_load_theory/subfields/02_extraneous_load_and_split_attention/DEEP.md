# Extraneous load and split attention: deep document

*Subfield A08.02. Built from evidence_a-d.jsonl (a01-a27, b01-b26, c01-c28, d01-d37), claims.jsonl (K01-K28) and critique.md (cross-check and gap pass of 2026-10-31). Evidence ids are in square brackets, claim ids as K##. "Opened" means the text was read in this research run; second-hand figures are marked. One number was corrected by the critique: Shi 2023 overall macro accuracy is 6.0 to 15.0, not 8.3 to 20.0.*

## 1. What it is

Extraneous cognitive load is mental effort that comes only from how material is presented, not from what must be learned. Intrinsic load is the effort the content itself needs. Germane load is effort that builds understanding.

The split-attention effect is the best-known case of extraneous load. A learner gets two or more sources, such as a diagram and its text. Neither is understandable alone. The learner must hold one in working memory, search the other for the matching part, and combine them. Search and matching use memory that is then not available for learning [a02]. The standard fix is to integrate: put the label or text on the part of the diagram it describes.

Three conditions define the effect.
1. The sources are mutually dependent (each is needed, neither is clear alone).
2. They are far apart in space or time.
3. The material is complex enough that the combining effort matters (high element interactivity) [a09, b08].

If a source is understandable alone, integrating it does not help, and repeating it hurts (the redundancy effect) [a05, a08, b11].

Why it matters for our agent. A prompt is a set of sources: rules, cases, tool lists, history, instructions. Two questions follow.
- Split-attention question: must the model search across the prompt to link a case to its rule?
- Extraneous-text question: does the prompt carry text that serves no purpose for this task?

The LLM literature on the second question is large. The literature on the first is almost empty. No study was found that tests the classic integrated-versus-separated contrast in text-only LLMs (K19; two search passes; the second had its search quota spent, so the negative is weak). Everything below on LLMs is therefore adjacent evidence: distractors, length, position, order, compression, layout.

## 2. History and theories in depth

**Origins (1980s to 1992).** Cognitive load theory (CLT) comes from Sweller's work on problem solving and worked examples. Geometry students given a diagram plus separate solution steps learned less than students given steps integrated into the diagram (Tarmizi and Sweller 1988; Sweller et al. 1990; Chandler and Sweller 1991, 1992; Purnell, Solman and Sweller 1991; Ward and Sweller 1990, as listed in Sweller 1994 [a07]). Chandler and Sweller (1992) named the effect "split attention". The founding paper was never opened in this research (K23). Its figures are not available. Only the second-hand claim stands: integrated formats gave faster learning and higher test scores when the sources were unintelligible alone.

**Sweller 1994 [a07-a10].** A narrative review with no pooled numbers. Its account: a conventional worked example has a diagram that says nothing alone and steps that make no sense alone. The learner must integrate them. That effort is extraneous because it comes only from the format. Two boundary points come from this review.
- Redundancy: Chandler and Sweller (1991) used a self-explanatory heart diagram with restating text. Integrating the text forced students to process unneeded words [a08].
- Element interactivity: Sweller and Chandler (1994) found split-attention and redundancy effects for numerical-control programming but not for word-processor commands [a09].

**Kalyuga, Chandler and Sweller 1999 [a02-a06, b09-b11].** Two computer-based studies with trade apprentices. These are the best-documented human experiments we opened.
- Exp 1 (N = 34, soldering diagram): visual text n = 11, visual plus audio text n = 12, audio text n = 11. Audio beat both. Fault-finding F(2,31) = 7.74. Multiple choice F(2,31) = 10.66. Dual presentation of the same words was worst (redundancy).
- Exp 2 (N = 16, 8 per group): colour-coding diagram parts and matching text. Multiple-choice gain F(1,13) = 7.17 (covarying study time). Load rating difference marginal, F(1,13) = 3.09. Fault-finding not significant, F(1,13) = 0.78.
- Load was one 7-point rating. Efficiency E = (P - R) / sqrt(2) [a06]. This single-item rating is the weak link of the whole line.

**Two rival accounts [a16].**
- CLT: separated sources add extraneous load through search and holding in working memory.
- Cognitive theory of multimedia learning (Mayer): the learner must map between a verbal model and a pictorial model. Unrelated items placed between the two cause micro-switching (a "contiguity failure").

There is no formal model with parameters. Both are verbal.

**Later accounts that weaken the load story.**
- Cierniak 2012 [a17]: format did not change a secondary-task load measure (Study 1, N = 103). Subjective extraneous load mediated only 8 and 16 percent of the effect.
- Pouw et al. 2019 [a18, b05], abstract only: distance changes process (slower integration, or a worse visual working-memory secondary task), but not learning.
- Schroeder 2020 [d22]: reviewed 41 comparisons. Load measures largely do not support the extraneous-load explanation. The author proposes germane or integrative processing instead.

**Meta-analytic phase.** Ginns 2006, Wang et al. 2016, Schroeder and Cenkci 2018 (details in section 3). The pooled size is positive and shrinking.

**Replication phase (2010 to 2024).** Several nulls and partial failures (section 5). The honest reading: the effect is real on average for complex, mutually dependent material, but is smaller than the early studies suggested, is often absent in single replications, and its stated mechanism (lower extraneous load) is poorly supported by load measures.

**Fixes proposed in the human literature [b25, a04, b09, b12].** Physical integration; colour-coding or signalling; replacing on-screen text with audio; instructing learners to integrate mentally; partially completed problems and worked examples [a10].

**LLM phase (2022 to 2026).** The CLT vocabulary was borrowed by a few LLM benchmarks (Adapala 2025, CogniLoad, ToolLoad). Most LLM evidence predates or ignores CLT: GSM-IC distractors (Shi 2023), Lost in the Middle (Liu 2023), length alone (Levy 2024, Du 2025), premise order (Chen 2024). These test extraneous text, not split attention.

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources agree), S = single source, C = contested. Ids refer to the evidence files.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Integrated text-and-picture beats separated (human, meta-analysis, spatial plus temporal) | Ginns 2006: d 0.85, 95% CI 0.68 to 1.02, 50 independent studies, 2,375 novices (CI second-hand via Beege 2019). A spatial-only figure of g 0.72 on 37 effects is an inference, not confirmed | Ginns 2006 [d20, b01, a13] | E (scope fix, K02) |
| Same, updated | Schroeder and Cenkci 2018: g 0.63 on 58 comparisons, n = 2,426. Worksheets g 0.80 (28 effects); computer-based 0.50 (20); 2-D pictures 0.71; complementary text and picture 0.72; mobile device 0.04 (1 effect). Test type, duration, retention vs transfer not significant moderators | [d21, a11, a12, b02] | E, size falling |
| Same, third meta-analysis | Wang et al. 2016, 53 studies: retention d 0.48, transfer d 0.39, rated load d -0.24 | [b03] snippet | E (abstract level) |
| Moderator: element interactivity | d 0.78 high complexity vs d 0.28 (p > .05) low complexity. Second-hand via Beege 2019 | [b08, a16, d20] | E (human, second-hand) |
| Audio instead of on-screen text for novices | N = 34; F(2,31) = 7.74 (fault finding), 10.66 (multiple choice); audio beat both | Kalyuga 1999 [a03, b09] | S |
| Colour-coding parts with matching text | N = 16; MC F(1,13) = 7.17; effort F(1,13) = 3.09 marginal; fault-finding F(1,13) = 0.78 n.s. Authors warn about more than about five colours | Kalyuga 1999 Exp 2 [a04, b10] | S |
| Redundant duplicate (text plus same audio) hurts | Visual-plus-audio lowest of three groups, N = 34 | Kalyuga 1999 [a03, b11]; Sweller 1994 [a08] | E |
| Telling learners to mentally integrate | N = 87; recall d 0.77, comprehension d 0.94 vs split no-strategy; integrated vs split: recall d 1.11, comprehension d 0.81; causal inference n.s. | de Koning, Rop and Paas 2020 [b12, b13] | S |
| Failed replication: distance and signalling | Exp 1 (about 107): no effect on effort or transfer, BF null 4.72 (distance), 22.94 (interaction). Exp 2 (about 140; replication of Johnson and Mayer 2012): F(2,137) = 1.91, p = .153, BF null 5.11 | Cammeraat 2020 [b04, d01, d02] | E (null) |
| Failed replication: Beege Exp 1 | N = 98: separated vs integrated retention t = 0.66, p = .51; transfer t = 1.47, p = .15. Medium distance best on transfer, t = 2.19, p = .03. Exp 2 N = 85: retention r = .22, transfer r = .27 | Beege 2019 [a14, b06, d23] | E (null in Exp 1) |
| Other nulls and partials | Florax and Ploetzner 2010 (N = 165): retention only, credited to text segmentation. Zhang 2022 (N = 122) and 2024 (N = 146) null, 2023 (N = 129) positive. Jarodzka 2015: split format more efficient when extra text irrelevant | [d24, d25, d26, a15] | C |
| Load is a weak mediator | Cierniak 2012 N = 103: no secondary-task difference; extraneous mediation 8 to 16 percent, germane 9 to 18 percent. Schroeder 2020: 41 comparisons do not back the load story | [a17, d22, b03] | C (K07) |
| One irrelevant sentence breaks LLM math | GSM-IC (code-davinci-002, text-davinci-003): of base problems solved, at most 18 percent solved for all distractor types; fewer than 30 percent solved consistently. About 4,000 problems from 100 base problems | Shi 2023 [a20, c01, b16] | E |
| Ignore-instruction helps a little | code-davinci-002 chain-of-thought micro accuracy 72.4 to 77.8; least-to-most 77.5 to 80.6; overall macro 6.0 to 15.0 (corrected). Self-consistency (20 samples) +35.5 points on 0-CoT; correct answer present in 99.7 percent | [c02, a21, b16] | E |
| Hardest distractors | Same-topic sentences, shared role names, in-range numbers; number size mattered little | Shi 2023 [d30, b16] | E |
| Inert clause (GSM-NoOp) | Drops up to 65 percent (Phi-3-mini over 65). o1-preview -17.5, o1-mini -29.1, GPT-4o -32.0 points. 8 shots of the same question did not close the gap | Mirzadeh 2025 [a24, b17, c08, d14] | E |
| Newer models still lose | GSM-DC 2025: Grok-3-Beta step accuracy 43% to 19%, GPT-4.1 26% to 2% from 1 to 15 irrelevant items at depth 5. Opus 4 near 100% to 85-90% on counting with distractors; R1 70% to 30% at five distractors; Cats trigger: R1 error 4.50% vs 1.50%. GSM-Plus: humans -2.05% vs GPT-4 -8.23% | [d28, d29, d13, d33] | E (size task-dependent, K24) |
| Length alone hurts (weaker models) | Levy 2024: mean accuracy 0.92 to 0.68 at 3,000 tokens. Du 2025: drops 13.9 to 85 percent with whitespace or masked filler, 5 models; at least 7.9 percent with masking; Mistral GSM8K 35.5 to 66.7 with recitation (up to +31.2) | [a23, c09, b19, c10, c11] | C (K10) |
| Length at agent scale, strong models | RULER: GPT-4 96.6 to 93.2 (4K to 32K), 81.2 at 128K; Llama 3.1 70B 96.5 to 94.8 at 32K, 66.6 at 128K. Du: Claude 3.7 Sonnet GSM8K -7.0, -8.5, -7.0; Gemini -3.8, -5.2, -6.0 | [d35, b19] | E (small cost) |
| Depth interacts with length | Multi-hop QA (gpt-4.1) 0.575 to 0.305 from 256 to 2,048 padded tokens; single-span 0.635 to 0.570. Drop 0.270 and 0.245 vs 0.065 and 0.025 (n = 200 each) | Dhara and Sheth 2026 [d12] | E (K27) |
| Near-miss worse than random | Related-wrong passage -25 percent per distractor; random unrelated documents up to +35 percent (RAG, one setup) | Cuconasu 2024 [c13, d31] | E (K14) |
| Position (U-shape) | GPT-3.5-Turbo drop over 20 points; worst case at 20 and 30 documents below closed-book 56.1 (oracle 88.3). Key-value: perfect at 300 pairs with query before and after, worst case 45.6 without | Liu 2024 [a22, b20, c04] | E, older models |
| Premise order | Shuffled premises: over 30 percent drop; GPT-4-turbo and PaLM 2-L -20 to -30 points; Gemini 1.0 Pro and GPT-3.5 from over 65% to below 25%. R-GSM: 220 pairs | Chen 2024 [c07, d32] | E (K25) |
| Context before question | CQO 69.26 vs QOC 54.54 (14.7 points), 21 open models. Gemini-3-Flash no thinking 87.4 vs 75.5 (11.84). CoT closes 83.4% of the gap on Gemini, 49.2% on open models | Ok and Lee 2026 [d07, c06] | E |
| Prompt repetition | 7 models, 7 benchmarks, reasoning off: 47 of 70 wins, 0 losses (p < 0.1). With reasoning: 5 wins, 1 loss, 22 ties of 28. Flash-Lite NameIndex 21.33 to 97.33 | Leviathan 2025 [d06] | S (early-2025 models) |
| Literal cue restores long-context loss | Llama 3.3 70B, one-hop at 32K: 56.2 plain, 93.1 with multiple-choice cue; two-hop 25.9 vs 87.2 | NoLiMa [d08] | S |
| Filter-then-answer (S2A) | LLaMA-2-70B-chat: factual QA with opinions 62.8 to 80.3 (oracle 82.0); GSM-IC in-topic 51.7 to 61.3; prompt-only variant 74.5; instruction-only 71.7 | Weston 2023 [b18, c03, d18] | E |
| Compression | LongLLMLingua up to +21.4 percent with about 4x fewer tokens | Jiang 2024 [c12] | E (with S2A, recite) |
| History trimming in agents | Observation masking (last 10 turns) cut cost 41 to 57% in 4 of 5 setups. Solve rate raw / mask / summary: Qwen3-Coder 53.4 / 54.8 / 53.8; Gemini 2.5 Flash 32.8 / 35.6 / 36.0; Flash thinking 40.4 / 36.4 / 31.4; Qwen3-32B thinking 23.0 / 24.6 / 24.8. Summaries +15% turns vs masking | Lindenbauer 2025 [c24, d27, c23] | E with boundary (K15) |
| Multi-turn sharding | 15 LLMs, 200,000+ simulations: mean drop 39 percent, visible in two turns; reliability loss dominates | Laban 2025 [c25] | S |
| Format noise | Up to 76 points (LLaMA-2-13B); GPT-3.5 median 6.4 over 320 formats; spread up to 56. Voronov 2024: SD up to 35% of mean, chance-level worst cases | Sclar 2024, Voronov 2024 [b21, c26, d36] | E |
| Separating question from image helped | VMMU: open VLMs 41.32 to 50.97; thinking models +2.10 | [c22] | S (opposite to human rule) |
| Load-framed LLM benchmarks | Adapala: Gemini 0.85 / 0.82 / 0.78 / 0.72; slope -0.003 per percent load (p < 0.001); GPT-4o 0.65 to 0.55, p = .07, 32% outputs lacked a final answer; Llama and Mistral 0.00 everywhere; long control p = .45. CogniLoad: 22 models, steepest decline N = 20 to 50. ToolLoad: exponential decay, k 0.034 to 0.088 | [b22, c16, c18, c19] | E but weak (K20) |
| Instruction density | 10 to 500 instructions: best 2025 model about 68% at 500 (o3 62.8, claude-opus-4 44.6, claude-sonnet-4 42.9); reasoning models near perfect to a threshold of 100 to 250 | Jaroslawicz 2025 [d34] | S |
| Gold passage size | Small gold passages lose more and are more position-sensitive: Gemini 2.0 Flash 48% (small) to 73% (large); small gold at start 94%, near end 33% | Bianchi 2025 [d10] | S |
| First distractors do most damage | First 10% of hard distractors causes most loss (drop ratio 0.58 vs 0.1 if linear); 10% hard cut gold attention by 76% | Gao 2026 [d11] | S, open models |

## 4. Mechanisms and models

Written so an engineer could implement or test them.

**4.1 Human account: working-memory search cost.**
- Model: the learner holds item A (text) in a limited buffer, scans source B (diagram) for the referent, matches, then drops A. Cost per link = hold time + scan time. Total cost grows with (number of links) x (distance between source and referent) x (interactivity of the elements).
- Prediction: the effect is large when links are many and elements depend on each other (d 0.78), and near zero for simple material (d 0.28, n.s.) [b08].
- Implementation analogue: count the links (case-to-rule, fact-to-referent) in an item. High link count = candidate for restructuring. Low link count = leave alone.
- Weakness: measured load does not follow the story [a17, d22, b03].

**4.2 Human account: mapping and micro-switching.**
- Model: between two matched sources, unrelated items in the gap force switches that break the match. Medium distance did best in one study (inverted U, Beege Exp 1 transfer t = 2.19, p = .03) [a14].
- Analogue: too many inline snippets might clash. Test a cap (UNKNOWNS U9).

**4.3 Human account: redundancy.**
- Model: a self-contained source plus its restatement forces the learner to reconcile the two. Rule: restate only if the first is not intelligible alone [a05].
- Analogue: do not add a paraphrase of a clear instruction, and do not paste the same fact twice.

**4.4 Machine account: attention is a budget (softmax).**
- Each token attends over all prior tokens with weights that sum to 1. Gold-token attention share falls as other tokens are added. Gao 2026: the share is a convex function of the hard-distractor share, so the first hard distractors do most damage; 10% hard distractors cut gold attention by 76% [d11].
- Zhang 2025: splitting context into separately encoded pieces raises attention entropy and degrades output [c15]. Niu 2025: tokens seen earlier get higher output probability (entrainment heads) [c14].
- Implementation: nothing to build at scaffold level. Use as a prior: fewer, cleaner tokens; remove the first near-miss distractors first.

**4.5 Machine account: causal mask and order.**
- A decoder-only model cannot attend from earlier tokens to later ones. Option tokens placed before the context cannot see it. Fix by putting context first and the question last (CQO), or by repeating the prompt so every token sees every other [d06, d07, d16].
- Implementation rules: long material first, question and answer options last; if reasoning is off, repeat the question (or the whole prompt) once; if reasoning is on, expect the gain to vanish (5 wins, 1 loss, 22 ties) [d06].
- Using-order rule: list facts in the order the solution uses them. Shuffling cost 20 to 40 points [d32].

**4.6 Machine account: similarity-driven distraction.**
- Near-miss text (same topic, same role names, in-range numbers) is the most harmful class in reasoning (Shi) and in retrieval (Cuconasu: -25 percent). Random text can even help in RAG (+35 percent, one setup) [d30, d31].
- Hop recall drop correlated with task similarity (r 0.35 to 0.42) [c17].
- Implementation: a filter that ranks removal candidates by overlap with the task (shared entities, same units, same topic words) and removes the highest-overlap non-task items first.

**4.7 Machine account: depth amplifies the cost.**
- Extra text costs little for lookup and a lot for multi-step dependence: multi-hop lost 0.245 to 0.270, single-span 0.025 to 0.065 [d12]. GSM-IC step count matters [d30]. This mirrors element interactivity.
- Implementation (S0 gate): bucket items by number of dependent steps or interacting elements. Switch on hygiene and restructuring only above a threshold.

**4.8 Filter pipelines.**
1. Code filter: delete spans by rule (known-irrelevant fields, stale tool output, duplicate lines). Cheap, deterministic, cannot invent text, but cannot judge relevance.
2. Model rewrite (S2A): a first call rewrites the input to keep only relevant, non-opinionated parts; a second call answers from the rewrite. Gain 62.8 to 80.3 in one setup. Extra call, and the rewrite can drop needed facts; the drop rate was never measured [d18].
3. Recite-then-answer: the model copies the relevant parts, then answers from them (Du 2025) [c11].
4. Question-aware compression (LongLLMLingua) [c12].
5. Observation masking in agents: replace old tool outputs with a placeholder, keep the last N turns [d27].

**4.9 Layout noise.**
- Equivalent prompts differ by large margins [b21, d36, d15]. Any layout test needs many formats, many items, and a reported spread. Treat differences below the spread as noise (K17).

## 5. What holds up

**Human effect: replications and meta-analyses.**
- Three meta-analyses agree in sign: Ginns d 0.85 (spatial plus temporal, 50 studies); Wang retention d 0.48 and transfer d 0.39 (53 studies); Schroeder and Cenkci g 0.63 (58 comparisons). The pooled size is falling as studies diversify.
- No bias-corrected size was found. None of the abstracts or summaries read discusses publication bias (K28). The size to trust is probably below g 0.63.
- The Ginns size clash (0.72 vs 0.85 vs 0.89) is a scope difference, not an error: 0.85 pools spatial and temporal contiguity (K02).

**Failures and partial failures.**
- Cammeraat 2020: two nulls, with Bayes factors in favour of no effect (BF 4.72 to 22.94 in Exp 1, 5.11 in Exp 2) [b04].
- Beege 2019 Exp 1: null on retention and transfer (N = 98) [a14].
- Pouw 2019 Exp 3: no effect on learning (abstract only) [b05, b07].
- Schmidt-Weigand 2010: could not replicate (second-hand) [a19].
- Florax and Ploetzner 2010: retention only, attributed to text segmentation [d24].
- Zhang 2022 and 2024 null; 2023 positive [d25].
- Language learning: integrated glosses helped low-proficiency readers' comprehension but hurt vocabulary, with the pattern reversing for more proficient readers [b15]. Adjacent layout gave 1.23x odds of a correct answer (He and Loewen), while vertical did not beat horizontal [b14].
- Jarodzka 2015: split format more efficient when the added text was irrelevant [d26].

**Moderators that survive.**
- Element interactivity (d 0.78 vs 0.28) [b08].
- Medium: worksheets g 0.80 vs computer-based 0.50 [a12].
- Subject: biology and geography medium; maths and physics small [b02].
- Intelligibility: integration helps only if the sources are unintelligible alone (redundancy) [a05].
- Learner expertise (see the parallel subfield on expertise reversal).

**Interventions that worked (human).** Integration; audio for text (small N); colour-coding (N = 16); mental-integration instruction (N = 87, d 0.77 to 0.94).

**Interventions that did not work, or are unproven.** Signalling in Cammeraat's replications; physical closeness alone in Beege Exp 1. Load meters: they do not track the effect.

**LLM side: what holds up.**
- Irrelevant text hurts reasoning accuracy: Shi, Mirzadeh, Yang, Gema, Cats, GSM-Plus (K09, K24).
- Near-miss text hurts more than unrelated text (K14).
- Order and position matter (K11, K25).
- Layout noise is large (K17).
- Removing or rewriting irrelevant text recovers part of the loss (K13).
- Trimming history in tool-using agents is safe for non-thinking models and saves 41 to 57 percent of cost (K15).

**LLM side: what failed or is contested.**
- "Ignore irrelevant information" gives small gains: +5.4 micro on code-davinci-002 CoT, and "no consistent gain" in the S2A paper on LLaMA-2-70B. More shots did not close the NoOp gap (K12).
- Length alone: Du and Levy say it hurts; Adapala's long control did not differ (p = .45), though 3 of 5 models were at floor (K10).
- Random text helped in one RAG test (Cuconasu), which contradicts "all extra text hurts".
- Chroma found no position effect in its setup [d09]. Smaller gold passages are more position-sensitive [d10].
- Separating text from image helped in VMMU, opposite to the human rule (K18).
- Gemini 2.5 Flash with thinking got worse with masking and summary (40.4 to 36.4 and 31.4) [d27].
- Prompt-repetition gains mostly vanish with reasoning on [d06].
- Mitigation papers are single-lab and do not count the extra call against the token budget (G7). The dropped-fact rate of a rewrite is unmeasured [d18].

**Quality caveats from the critique.**
- Founding paper never opened (K23). Ginns full text never opened.
- Adapala: 200 questions, only two usable models, a truncation confound, and a slope (-0.003) that does not match the cell means (it predicts about -0.24 at 80 percent load; the observed drop is 0.13). Quote cell means.
- Distractor evidence is dominated by older models (code-davinci-002, text-davinci-003, LLaMA-2). No clean 2026 measure on the newest models.
- Pairs of evidence lines describing the same study (a14/b06, a11/b02, a20/b16/c01, a22/b20/c04, a24/b17/c08, a23/c09) count as one source each.

## 6. Language models

**No direct test.** No study was found that varies only whether facts sit next to their referents (integrated) or apart (separated), at equal tokens, in a text-only LLM task (K19). Nearest analogues: premise order (20 to 40 points), question-last placement (up to 14.7 points), the NoLiMa literal cue (56.2 to 93.1), and Thread of Thought (a segment-by-segment pass over cluttered context; PopQA exact match about 0.65 to 0.67 on GPT-4, GPT-3.5, Llama-2-70B) [d32, d07, d08, d17].

**How models behave on adjacent tasks.**
- Inert or related-but-wrong clauses: 2022 to 2023 models lose most of their accuracy (GSM-IC). 2024 to 2025 models still lose: o1-preview -17.5, GPT-4o -32.0 on NoOp; GPT-4.1 26% to 2% on GSM-DC [d14, d28]. Strong reasoning models fail differently: o3 stable on counting with distractors, Claude Opus 4 degrades as reasoning lengthens, R1 collapses [d29]. More thinking does not cure distraction and can worsen it (G11).
- Size depends on task. Du 2025 saw only -3.8 to -8.5 on GSM8K for Claude 3.7 Sonnet and Gemini [b19]. Cats triggers raise R1 error from 1.50% to 4.50% [d13].
- Length: for strong models at 5K to 30K tokens the loss from filler is small (GPT-4 about 3 points to 32K) [d35]; it grows with reasoning depth [d12]. Chroma's 18-model report (Claude Opus 4, Sonnet 4, o3, GPT-4.1, Gemini 2.5) found every model better on a focused 300-token input than on the full 113k-token one [d09]. Exact values were in charts only.
- Position: U-shaped for 2023 models; newer models improved retrieval but still depend on gold-passage size [d10].
- Order: context first, question last. CQO beats QOC by 14.7 points on open models, 11.84 on Gemini-3-Flash without thinking; chain-of-thought closes about half to 83 percent of it [d07]. The vendor page for current Claude models says put long documents on top and the query last (up to 30 percent claimed, no published method) and ask the model to quote relevant parts first [d05].
- Instruction density: 500 instructions in one prompt gave about 68% for the best model; reasoning models hold to a threshold of about 100 to 250 [d34].
- Tool-using agents: masking old observations halves cost with no loss for non-thinking models; a thinking model lost 4 to 9 points [d27].
- Multi-turn: spreading one task across turns lost 39 percent on average over 15 models [c25].

**What changed the result, and by how much.**
- Removal or rewrite of irrelevant text: +10 to +12 points on GSM-IC (S2A); +17.5 on opinion QA; recite-then-answer up to +31.2 on a weak open model.
- Ignore instruction: +5.4 micro on code-davinci-002 CoT; none consistent on LLaMA-2-70B.
- Self-consistency: +35.5 points on 0-CoT (a sampling fix, not an input fix).
- Question last or repeated: +11.8 to +14.7 points (non-reasoning, multiple choice).
- Premise order matched to the solution: avoids a 20 to 40 point loss.
- Literal cue: +37 points on one-hop at 32K.

**Reading for our agent.** The classic human prescription (integrate) is untested for LLMs. "Drop irrelevant text" is established. "Order facts as they are used, put the question last" is established for the model types tested. Strong reasoning models are less affected by length and still affected by near-miss clauses. Everything else needs our own bench.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Input hygiene in S1 by code, near-miss first.** Code moves or drops text that is not part of the task (stale tool output, duplicate lines, stated guesses, unrelated clauses). Remove the highest-overlap non-task items first. S1 [E]. Evidence K09, K13, K14, K24 (a20, a24, d28, d29, d30, c03, c13). The S1 text already names input hygiene; this adds the removal order and the sizes.
2. **Order of material.** Long material first, question and answer options last; facts listed in the order the solution uses them. S1/S2 [E]. K11, K25 (c04, d32, d07, d05).
3. **Do not pad.** Keep every call's context to what the step needs. G11 [E for weak models, C for strong models at agent length]. K10, K27 (b19, d35, d12). The cap is cheap and safe; the size of the gain on our model is unknown.
4. **Do not rely on an "ignore irrelevant" line.** Use removal; the instruction is a fallback only. S1 [E]. K12 (c02, c08).
5. **Layout is noise, so test with spread.** Any layout rule needs many formats, many items and a reported spread before it enters the schema. G7 [E]. K17 (b21, d36, d15).
6. **Trim agent history by masking old tool outputs for non-thinking runs.** Keep the last about 10 turns. memory [E] with a boundary: thinking models may need history. K15 (c24, d27, c23).
7. **No redundancy.** Do not restate a clear instruction or paste the same fact twice. S1 [E in humans; unverified for LLMs, so treat as hygiene, not as a claim]. K05 (a05, a03).
8. **Spend more checking budget on items with many distractor facts or dependent steps.** G12 [E]. K20, K27 (c16, c18, d12).

### Test first (not yet established)

| Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|
| Put each rule next to the case it governs (integrate) vs rules in a header | O2, S2 | [C] human; no LLM test | K01, K03, K19 | Human effect shrinking and failed in several replications; no LLM data |
| ID tags on cases (text colour-coding analogue) | S2 | [S] | K06, d08 | Human N = 16; NoLiMa cue effect is indirect |
| "Name the rule for each case before answering" step | S1/S2 | [S] | K08 | Human N = 87 only |
| Gate restructuring by difficulty | S0 | [E] human, [S] LLM | K04, K27 | Could save tokens |
| Code filter vs model rewrite, with a needed-fact survival audit | S1 | [E] direction, cost unmeasured | K13, d18 | Rewrite cost and drop rate unknown |
| Repeat the question once when reasoning is off; question-last template | S0 template | [S] early-2025 models | K25, d06, d07 | Not tested on our model |
| Fresh full context per S3 attempt vs sharded facts | S3 | [S] | K16 | One simulated-user study |
| Per-state guardrail list instead of all G1-G12 in every prompt | G | [S] | K26 | One synthetic task |
| Separate vs merged sources of different modality | S1 | [S] | K18 | Opposite to the human rule |
| History: masked vs summary vs full under S3 fresh attempts | memory | [E] without S3, open with it | K15 | Interaction unknown |

## 8. Concrete tests on our bench

All arms get equal total tokens, including cleaning calls. Pad shorter arms with neutral task-relevant detail, or count extra calls against the arm that uses them (G7). Use at least 10 meaning-preserving formats and several seeds; report min, median and max accuracy per arm (K17).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Format spread | One fixed task, 10 equivalent formats | none (noise floor) | min, median, max accuracy | Sets the threshold for T2 to T8 |
| T2 Integrated vs separated | 60+ rule-application items; easy and hard strata | (a) each rule inline with its case, (b) rules in a header, (c) current prompt; use-order fixed in all arms; extra shuffled-order arm to size the order effect | Accuracy by stratum; wrong-rule rate | Null on easy items; a gain of a few points on hard items if the human moderator transfers |
| T3 Tags | Same items as T2 | header with case IDs vs inline vs header only | Accuracy; wrong-rule match rate | Tags near inline, above header only |
| T4 Link-first instruction | Same items | instruction + header vs inline vs header only | Accuracy; output tokens | Gain over header only with under 15% more output tokens |
| T5 Distractors | Our tasks with 1, 3, 5 inert clauses and 1, 3, 5 near-miss clauses | raw, code-filtered, "ignore this" line, S2A-style rewrite | Accuracy drop vs clean; needed-fact survival; total tokens | Near-miss drop larger than inert drop; code filter recovers most |
| T6 Length vs content | Solved items only | clean; + near-miss; + unrelated; + filler of equal tokens | Accuracy drop | Settles Du vs Adapala for our model (K10) |
| T7 Order / question last | 100+ items, 5k to 20k tokens | question first, question last, first and last; reasoning on and off | Accuracy; tokens | Question-last gain with reasoning off, smaller with reasoning on |
| T8 Difficulty gate | Our tasks bucketed by dependent steps | cleaner on vs off by bucket | Gain per bucket | Gain concentrated in the multi-step bucket (K27) |
| T9 History | Multi-step agent tasks | full, masked, summary; with and without fresh-context S3 attempts | Success; tokens | Masking about equal to full at half the cost for non-thinking mode |
| T10 Sharding | Same tasks | all facts at once, sharded, sharded then consolidated | Accuracy | Sharded loses; consolidation recovers part |
| T11 Guardrail density | G1-G12 adherence | all in prompt vs only the active ones | Adherence rate | Fewer rules, better adherence |

## 9. What does not transfer, and why

- **Working-memory capacity.** Humans hold about four items; a model has no such buffer. Its limits are attention dilution and the causal mask, so "reduce load" is a loose analogy.
- **Load measurement.** Human load ratings and secondary tasks do not even track the human effect [a17, d22]. Do not build a load meter for the agent (K07). Measure accuracy.
- **Diagrams.** Most human studies pair pictures with text. Text-only prompts have no spatial layout in the human sense; "nearness" is token distance and order only.
- **Physical integration.** Putting a label on a diagram has no direct analogue. The nearest are inline placement and ID tags, both untested.
- **Learners are novices.** The human effect is for novices; experts show reversal (parallel subfield). The model is not a novice in any stable sense; its "expertise" depends on training coverage.
- **Colour and audio.** Single small human studies [a03, a04]. The only text analogue is consistent labels.
- **Redundancy effect.** Redundancy hurts humans by forcing reconciliation. A model may ignore a repeated line, or gain from it (prompt repetition [d06]). Both directions exist.
- **Separation helped machines in VMMU.** Different modalities may suit separate channels [c22].
- **Adversarial clutter.** The cognitive-overload attack (up to 99.99% claimed) is a safety result seen only in snippets [b24, c28]. Not an accuracy claim.
- **CLT-labelled LLM benchmarks** (Adapala, CogniLoad, ToolLoad) borrow the words. They test difficulty scaling, not the human effect.
- **Old-model results.** Shi, Weston and Sclar rest on GPT-3 era and LLaMA-2 models; effect sizes on current models are smaller or unknown.

## 10. Open questions

1. Does integrated vs separated, at equal tokens and fixed use-order, change accuracy at all in current LLMs? (K19, gap 1.)
2. Which fix wins at equal total tokens on the current model: code filter, ignore line, S2A rewrite, recite-then-answer? What fraction of needed facts does a rewrite drop? (gap 2)
3. How large are distractor losses on the newest reasoning models? Mirzadeh (o1-preview -17.5) and Du (-3.8 to -8.5) disagree on scale. (K24)
4. Is the length penalty real for clean, task-relevant context at 5k to 30k tokens? Adapala's long control said no; Du said yes. (K10)
5. What are the real numbers in Chandler and Sweller 1992 and in Ginns 2006 full text? (K23, K02)
6. How much of the human effect survives bias correction? (K28)
7. Does element interactivity predict where restructuring helps LLMs, so the S0 gate can switch it on? (K27)
8. Can code detect near-miss distractors cheaply? (K14)
9. Which history treatment is best at equal tokens, and does it interact with fresh-context S3 attempts? (K15)
10. How large is layout noise for our own prompt format? (K17)
11. Is there an over-integration cost (inverted U) from too many inline tags? (a14 in humans)
12. Is the mechanism attention dilution, the causal mask, or similarity-driven entrainment? Closed models cannot be probed.

## 11. Sources

[V] = opened and read in this research run (full text, or the abstract page for ERIC records). [M] = snippet, citation page, or second-hand only.

**Human studies, reviews and meta-analyses**
- [M] Chandler and Sweller (1992), The split-attention effect as a factor in the design of instruction. https://doi.org/10.1111/j.2044-8279.1992.tb01017.x ; https://www.e-teaching.org/materialien/literatur/chandler-sweller-1992 [a01, d04]
- [V] Kalyuga, Chandler, Sweller (1999), Managing split-attention and redundancy in multimedia instruction. https://tecfa.unige.ch/tecfa/teaching/methodo/Kalyuga99.pdf [a02-a06, b09-b11, d03]
- [V] Sweller (1994), Cognitive load theory, learning difficulty, and instructional design (copy hosted at mrbartonmaths.com, path in evidence_a.jsonl a07) [a07-a10]
- [V] Clearing House Unterricht (2019), Kurzreview 23 of Schroeder and Cenkci 2018 (German summary). https://www.clearinghouse.edu.tum.de/wp-content/uploads/2019/06/ [a11-a13]
- [V] Beege et al. (2019), Spatial continuity effect vs. spatial contiguity failure. https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2019.00086 [a14-a16, b06-b08, d23]
- [V] Cierniak (2012), dissertation, Tuebingen (abstract page). https://tobias-lib.uni-tuebingen.de/xmlui/handle/10900/49678 [a17]
- [M] Pouw et al. (2019), The cognitive basis for the split-attention effect. https://doi.org/10.1037/xge0000578 [a18, b05]
- [M] Schmidt-Weigand, Kohnert, Glowalla (2010). https://doi.org/10.1002/acp.1554 [a19]
- [V] Sweller, Clark, Kirschner (2010). https://files.eric.ed.gov/fulltext/EJ909939.pdf [a25] (low relevance)
- [M] Ayres and Sweller (2005), Cambridge Handbook of Multimedia Learning [a26]
- [M] Cierniak, Scheiter, Gerjets (2009). https://doi.org/10.1016/j.chb.2008.12.020 [a27]
- [M] Ginns (2006), Integrating information. https://doi.org/10.1016/j.learninstruc.2006.10.001 [b01]; [V] ERIC abstract https://api.ies.ed.gov/eric/?search=id:EJ747512 [d20]
- [V] Schroeder and Cenkci (2018). https://doi.org/10.1007/s10648-018-9435-9 [b02]; abstract https://link.springer.com/article/10.1007/s10648-018-9435-9 [d21]
- [M] Wang et al. (2016), meta-analysis. https://devpsy.bnu.edu.cn/EN/Y2016/V32/I5/565 [b03]
- [V] Cammeraat, Rop, de Koning (2020). https://repub.eur.nl/pub/121858/Repub_121858.pdf [b04, b25, d01, d02]
- [V] de Koning, Rop, Paas (2020). https://repub.eur.nl/pub/128039/Repub_128039_O-A.pdf [b12, b13]
- [V] He and Loewen (2024). https://doi.org/10.1017/S0272263123000281 [b14, b15]
- [V] Schroeder (2020), Do measures of cognitive load explain the spatial split-attention principle. https://api.ies.ed.gov/eric/?search=id:EJ1240932 [d22]
- [V] Florax and Ploetzner (2010). https://api.ies.ed.gov/eric/?search=id:EJ872944 [d24]
- [V] Zhang and colleagues (2022 to 2024). https://api.ies.ed.gov/eric/?search=id:EJ1436677 [d25]
- [V] Jarodzka et al. (2015) and test-item studies. https://api.ies.ed.gov/eric/?search=id:EJ1338781 [d26]

**LLM studies**
- [V] Shi et al. (2023), distracted by irrelevant context. https://arxiv.org/abs/2302.00093 [a20, a21, b16, c01, c02, d30]
- [V] Liu et al. (2024), Lost in the Middle. https://arxiv.org/abs/2307.03172 [a22, b20, c04, c05]
- [V] Levy, Jacoby, Goldberg (2024), Same task, more tokens. https://arxiv.org/abs/2402.14848 [a23, c09]
- [V] Mirzadeh et al. (2025), GSM-Symbolic. https://arxiv.org/abs/2410.05229 [a24, b17, c08, d14]
- [V] Weston and Sukhbaatar (2023), System 2 Attention. https://arxiv.org/abs/2311.11829 [b18, c03, d18]
- [V] Du et al. (2025), Context length alone hurts. https://arxiv.org/abs/2510.05381 [b19, c10, c11]
- [V] Sclar et al. (2024), spurious features in prompt design. https://arxiv.org/abs/2310.11324 [b21, c26]
- [V] Adapala (2025), Cognitive load limits in LLMs. https://arxiv.org/abs/2509.19517 [b22, c16, c17]
- [M] ToolLoad-Bench abstract. https://arxiv.org/abs/2601.20412 [b23]; [V] Wang et al. (2026), same id [c19]
- [M] Cognitive Overload Attack. https://arxiv.org/abs/2410.11272 [b24, c28]
- [M] Ok and Lee (2026) snippet, https://aclanthology.org/2026.findings-acl.1921/ [c06]; [V] full text https://aclanthology.org/2026.findings-acl.1921.pdf [d07]
- [V] Chen et al. (2024), Premise order matters. https://arxiv.org/abs/2402.08939 [c07, d32]
- [V] Jiang et al. (2024), LongLLMLingua. https://arxiv.org/abs/2310.06839 [c12]
- [V] Cuconasu et al. (2024), The Power of Noise. https://arxiv.org/abs/2401.14887 [c13, d31]
- [V] Niu et al. (2025), Llama See, Llama Do. https://arxiv.org/abs/2505.09338 [c14]
- [V] Zhang et al. (2025), Attention entropy. https://arxiv.org/abs/2412.16545 [c15]
- [V] Kaiser et al. (2025), CogniLoad. https://arxiv.org/abs/2509.18458 [c18]
- [V] Shang et al. (2026), United Minds or Isolated Agents. https://arxiv.org/abs/2506.06843 [c20]
- [M] Negative search records [c21, d19, d37]
- [V] VMMU. https://arxiv.org/abs/2508.13680 [c22]
- [V] Kang et al. (2026), ACON. https://arxiv.org/abs/2510.00615 [c23]
- [V] Lindenbauer et al. (2025), The Complexity Trap. https://arxiv.org/abs/2508.21433 [c24, d27]
- [V] Laban et al. (2025), LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120 [c25]
- [M] Fu et al. (2025), Exclusion of Thought. https://aclanthology.org/2025.acl-long.1051 [c27]
- [V] Anthropic (2026), long-context prompting guidance. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips [d05]
- [V] Leviathan et al. (2025), Prompt repetition. https://arxiv.org/abs/2512.14982 [d06]
- [V] Modarressi et al. (2025), NoLiMa. https://arxiv.org/abs/2502.05167 [d08]
- [V] Chroma (2025), Context Rot (company report, read through a summarising fetch). https://www.trychroma.com/research/context-rot [d09]
- [V] Bianchi et al. (2025), Hidden in the Haystack. https://arxiv.org/abs/2505.18148 [d10]
- [V] Gao, Chen, Huang (2026), The First Drop of Ink. https://arxiv.org/abs/2605.10828 [d11]
- [V] Dhara and Sheth (2026), context-length robustness in QA. https://arxiv.org/abs/2603.15723 [d12]
- [V] Rajeev et al. (2025), Cats Confuse Reasoning LLM. https://arxiv.org/abs/2503.01781 [d13]
- [V] He et al. (2024), prompt formatting. https://arxiv.org/abs/2411.10541 [d15]
- [V] Xu et al. (2024), Re-Reading (RE2). https://arxiv.org/abs/2309.06275 [d16]
- [V] Zhou et al. (2023), Thread of Thought. https://arxiv.org/abs/2311.08734 [d17]
- [V] Yang et al. (2025), How is LLM reasoning distracted (GSM-DC). https://arxiv.org/abs/2505.18761 [d28]
- [V] Gema et al. (2025), Inverse scaling in test-time compute. https://arxiv.org/abs/2507.14417 [d29]
- [V] Li et al. (2024), GSM-Plus. https://arxiv.org/abs/2402.19255 [d33]
- [V] Jaroslawicz et al. (2025), IFScale. https://arxiv.org/abs/2507.11538 [d34]
- [V] Hsieh et al. (2024), RULER. https://arxiv.org/abs/2404.06654 [d35]
- [V] Voronov, Wolf, Ryabinin (2024), Mind your format. https://arxiv.org/abs/2401.06766 [d36]
