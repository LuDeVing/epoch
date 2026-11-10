# Critique: Analogy and distant sources (A09.10)

## Corrections made (10 numbers re-opened, arXiv PDFs read via pdftotext)
1. Yasunaga et al. Table 1 (a13, b15): the text extraction shifted row labels by two. Correct: GSM8K GPT-3.5 0-shot 75.0, 0-shot CoT 75.8, 5-shot CoT 76.7, analogical 77.8; text-davinci-003 14.8 / 50.3 / 54.0 / 61.0; MATH GPT-3.5 33.0 / 33.9 / 34.9 / 37.3. b15 ("5-shot CoT 75.0%") is wrong; use a13/c06.
2. ARN (c21, b25): columns are (analogy, distractor) = (near,far) 94.0, (near,near) 92.5, (far,far) 57.1, (far,near) 29.1 for GPT-4. GPT-4 is below chance (29.1) only on far analogies with near distractors; with far distractors it is 57.1. The "below random" on far analogies (39.6%) is a mean over models and distractors. c21 overstates for GPT-4 alone.
3. Lewis & Mitchell Table 2 (a10, c10): labels shifted one line in extraction. Humans 0.753 [0.734, 0.773], GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 confirmed. Note GPT-3 beats GPT-4 overall.
4. Confirmed unchanged: Webb OR 1.88 (p=.005) and 1.76 overall (p=6.3e-5; zero-generalization also OR 1.76, p=.0007, a coincidence, not a copy error); story near p=.0039, far p not significant; OR 0.37 p=.0003. Stevenson adults .88/.91/.89, children .62/.66/.67. Qin relevant 71.5/33.3/52.4 vs N/A 75.5/36.1/55.8.
5. Not re-opened (no free full text): Chan 2011 effect sizes, Hope 2017 percentages, Christensen & Schunn counts. These were read in earlier sessions by the evidence agents; I did not re-verify them.

## Duplicates
Many lines repeat the same paper (Webb x4 sets, Yasunaga x4, ARN x3, Lewis and Mitchell x3, Bhavya x2, Hope x4). These are re-extractions, not independent replications; claims count independent papers only.

## Contradictions
- Chan 2011 (far examples raise novelty) vs Song 2017 (near-containing sets raise novelty, far raises quality).
- Christensen & Schunn (45% between-domain, in vivo design) vs Dunbar (distant rare, second-hand).
- Yasunaga (self-generated relevant exemplars help) vs Qin (irrelevant ones do as well or better).
- Webb (emergent analogy) vs Lewis & Mitchell (fails on counterfactuals), partly rebutted by code-execution result.

## Weak spots
- Founding studies (Gick & Holyoak 1980/1983, Gentner 1993, Dunbar 1997, Holyoak & Thagard, Ward, Dahl & Moreau) were NOT opened; a22-a28 are from memory. Gick & Holyoak figures are unverified.
- Only snippet: Chan, Dow & Schunn 2015 (b11).
- No meta-analysis of far-source effects; Chan 2011 cells are small and unequal.
- Almost all LLM tests are 2022-2024 models (GPT-3 to GPT-4o, Claude 3.5). Nothing from 2025-2026 reasoning models.
- Thought Propagation (c18) uses near analogues; headline gains are abstract-level averages.
- LLM idea novelty (Si 2024) is not an analogy test.

## GAPS
1. Do current reasoning models (2025-2026) close the far-analogy and counterfactual gap seen in ARN, Stevenson, Lewis & Mitchell? Needs a re-run with measured numbers.
2. What do the original Gick & Holyoak 1980/1983 and Gentner 1993 numbers actually say (spontaneous transfer rates, hint effects, schema induction gains)?
3. Is the Qin result (random exemplars match relevant ones) reproduced on reasoning models, and does an analogy step ever beat a plain extra-sampling control at equal tokens?
4. What distance is best for an LLM agent: is there an inverted-U (mid-distance) rather than far-is-better, given Chan 2011 vs Song 2017?
5. Does an explicit abstraction step (state the relation first) help far analogies without hurting near ones, outside ARN (c22 saw a near-accuracy cost)?
6. How often are generated analogies harmful or constraint-violating (about 25% in Ding 2023, 37.5% infeasible in MacGyver), and does a constraint audit lower that rate at equal tokens?
7. Does structured purpose/mechanism retrieval (Hope 2017/2021) carry over to retrieval from an agent's own memory of past tasks?
8. What do Dunbar's original in vivo counts say about distant-analogy frequency and which analogies led to discoveries?
9. Do LLM idea pools lose diversity because of analogy sources (duplicate collapse in Si 2024), and does varying source distance restore it?

## Gap search results
Sources: evidence_d.jsonl (d01-d17). Search budget used up (8 WebSearch); arXiv, Semantic Scholar and OpenAlex APIs returned 429.

1. Reasoning models on far analogy: PARTLY OPEN. Only symbolic Raven-style tests found (o3-mini 86.6 -> 17.0, R1 80.6 -> about 23 under noise, d01, d02, d14); extra reasoning tokens did not rescue accuracy. No 2025-2026 rerun of ARN, Stevenson or Lewis and Mitchell found.
2. Gick and Holyoak numbers: CLOSED for 1983 (opened full text: 10% base, about 30% unprompted, 75-80% hinted; two analogs 45% vs 21%; schema quality 91% vs 30%; d03-d07). The 1980 paper was not opened (403), only recapped. Gentner 1993 (retrieval by surface similarity) not retrieved: STILL OPEN.
3. Qin result on reasoning models and equal-token test: OPEN (d17). No study found.
4. Best distance: PARTLY CLOSED. Liu 2026 (d08, d09) finds originality rises with distance, no inverted U, strong LLMs gain only beyond a distance floor. Quality and feasibility by distance bin not reported; the Chan 2011 vs Song 2017 conflict is unresolved for design quality.
5. Abstraction step outside ARN: PARTLY CLOSED. Step-Back (d13) helps single-problem reasoning but is close to CoT on GPT-4 (84.5 vs 82.9) and adds 11.9% new errors; Gick and Holyoak Exp 2-3 show a given principle did not help (d07), a self-induced schema did (d03, d04). Near-accuracy cost for far-analogy abstraction still untested.
6. Harmful or infeasible analogies: PARTLY CLOSED. Shen 2026 (d12): reasonable 67% for analogy solutions vs 86% for plain cross-domain. No constraint audit tested at equal tokens.
7. Purpose/mechanism retrieval from an agent's own memory: OPEN (d16). Only snippet-level memory-structure papers.
8. Dunbar in vivo counts: OPEN. Only the secondary 98% local or regional (d15); chapter not opened.
9. Idea-pool diversity: CLOSED for biomedical solution generation (d11). Baseline domain Vendi 2.64-2.84, only about 5% unique domains; analogy pipeline raises solution Vendi 90-173% at the same 2 calls. Not tested for the Si 2024 research-idea setting.

Claims: K17 raised to established (read in 1983 text), K11 set to contested, K02 and K16 extended; new K18-K23 added.
