# Critique: fixation, functional fixedness and structured imagination (A09.06)

Cross-check done on 95 evidence lines (a01-a33, b01-b31, c01-c31). 30 claims written to claims.jsonl (A09.06-K01 to K30).

## 1. Sources re-opened and numbers checked

| Line | Source | Result |
|---|---|---|
| b22/b23/b24/c15 | Deng, Brucks, Toubia 2026 (arXiv 2602.20408) | Confirmed: slopes 1.013 (SE .017) and 1.363 (SE .020), p<.001; categories 18.45 vs 24.84; ordinary persona .635 (SE .045), 2.6 times default; maximum 28 categories. |
| c04 | Tian et al. 2024 MacGyver (arXiv 2311.09682) | Human 65.1% confirmed. Self-reflect -9.7% infeasible vs div-conv -4.3%, +6.5% vs +2.2% efficient: confirmed. CORRECTION: the error table is laid out in columns that do not parse cleanly. Wrong tool usage 42.4% is clear; "goal not achieved 17.7%" and "unfaithful 9.5%" are not reliable. In the table 9.5% sits beside "Using unavailable tools", and 16.9% and 10.8% sit beside "not achieving the goal". Treat only 42.4% as sound. |
| c14 | Anderson, Shah, Kreminski 2024 (arXiv 2402.01536) | Confirmed: group level .24 vs .28, t(32)=2.154, p=.038, d=.47; individual level .65 vs .66, t(32)=.944, p=.352. |
| b26/c13 | Wadinambiarachchi 2024 (arXiv 2403.11164) | Confirmed: GenAI +.32, 89% CI [.11, .55], Bayes factor 124. NOTE: b26 and c13 are the same paper; count as one source. |
| b25/c18 | Verbalized Sampling (arXiv 2510.01171) | Confirmed: 1.6-2.1 times, +25.7% human score, 66.8% recovered. Also same paper twice. |
| a06/b17 | German and Defeyter 2000 | Table confirmed (5y 60/80, 6y 60/90, 7y 40/89%; times 44.5/55.8, 113.8/50.7, 115.3/28.9 s). CORRECTION: b17 gives "older children 18% vs 89%" and "5-year-olds 64% vs 65%". These ARE in the paper text but do not match its own table (table 5y: 60% vs 80%). The paper is internally inconsistent; the text numbers probably come from a pooled or companion measure. Use table values. b17 also says N=60 with 30 per condition; confirmed. |
| a03/b19 | Fleck and Weisberg 2004 | Confirmed: 23.5% (verbalising) vs 27.7% (silent), p=.736, 25% overall, 5.72 min (SD 3.13). The chi-square uses N=52 although 58 took part (excluded cases). |
| b20 | Howard et al. 2013 | Confirmed: ratio .88 to .53, p=.025, 12 teams, two-tailed paired t. No control group. |
| a14-a16 | Ward et al. 2002 | Confirmed: 99%, 97%, 91%; means 3.18 vs 4.34; handles 23% vs 73%, chi-square 33.20, N=135. |
| a08-a10 | Marsh, Landau, Hicks 1996 | Omnibus F(4,75)=5.91, delay F(1,73)=4.74 and 5.74 confirmed. CORRECTION: the linear trend is reported as F=4.75 (p<.01) in one place and 3.25 in another, and F=4.75 is not p<.01. Treat the trend as weaker than stated. |
| a25/b07 | George and Wiley 2020 | Means 2.65/1.90 and 2.68/1.88, d=0.58 confirmed. CORRECTION to the reading: the interaction was NOT significant (F=2.16, p=.14), but the planned comparison shows the whole gain sits in the single Examples+Avoid cell, and the other three cells did not differ. The main effects in a25/b07 are driven by that cell. Examples alone and warnings alone do nothing. |

Not re-opened this session: the Smith 1993 numbers (b01-b03, read earlier by the finding agent), Sio 2015 (never opened), Jansson and Smith 1991, Duncker/Adamson original data.

## 2. Contradictions between sources

- Avoid instructions: no effect (Smith 1993, Jansson and Smith 1991, Viswanathan) vs works (Chrysikou and Weisberg 2005, George and Wiley's combined cell). Wang 2023 offers two explanations (group vs individual testing, psychology vs engineering) but neither was tested directly.
- Examples as harm vs help: Sio 2015 meta-analysis (abstract only) says examples reduce variety but raise novelty and quality. Smith/Marsh show copying with no change in count. Fu 2019 shows transfer without a quality loss. "Fixation" is therefore a statement about overlap, not necessarily about worse final ideas.
- Delay: Marsh Exp 3 raises copying after a day; the incubation meta-analysis says breaks help (d=0.29). These are different manipulations (a gap after the examples vs a break after getting stuck), but nobody has put them in one design.
- SCHEMA 4b says incubation by distraction does not replicate; a28/b15 show d=0.29 over 117 studies. The two are compatible only if the 4b statement is about unconscious-thought-theory claims. Wording in 4b should be checked by the schema owner.
- Reflection: SCHEMA 4b rejects unstructured self-reflection; MacGyver found affordance-checking reflection the best defixation prompt. The difference is structure (check each step against what the object affords), so it is not a direct contradiction.
- Within-session LLM fixation (Deng) says LLMs match humans, yet group-level LLMs are less diverse. Both are true: the fixation is in sequential generation; the homogeneity is across runs.

## 3. Weak spots

- Duplicates inflate counts. b22/c15, b25/c18, b26/c13, a29/c30 and b19/a03 are the same papers; independent source counts in claims.jsonl already merge them.
- The defixation-method evidence for humans with effect sizes is thin: the generic parts technique (McCaffrey) exists only as a press release (67% "more often"; a secondary "50% vs 83%" is unverified). The task asked for effect sizes; none could be confirmed with a control rate and N.
- Almost every LLM defixation study (IDEAFix, Meincke, Ma) compares prompts with different token costs. Only Verbalized Sampling states compute held fixed. No source gives an equal-token comparison of defixation methods.
- Measures of diversity are embedding-based or category-coded by LLMs in several studies (G8 warns against model judges). Deng uses fixed categories; others less clear.
- Child studies are tiny (N=10 per cell). The 2025 "cooties" replication (b18) was seen in a snippet only.
- LLM mental-set study (Haq) has 6 problems per condition and results like 0.16/0/0/0; unreliable.
- Einstellung (MedEinst), CreativityBench and IDEAFix are 2026 preprints; not peer reviewed as far as seen.
- Only seen in snippets or abstracts: a12, a13, a31, a32, a33, b12, b13, b18, c30, c31 (opened:false).
- Numbers read from figures (IDEAFix gains, Anderson figure caption) are approximate.

## 4. GAPS (most decision-relevant first)

1. At equal total tokens, which defixation procedure gives the best final-pick quality on an LLM: title-revise-expand, critique-and-edit, verbalized sampling, banned-feature list, or plain best-of-n? No source ran this.
2. Does a code-checked banned-feature list (the only version with human support, George and Wiley) beat a free "avoid these" instruction for LLMs, and does it cost more than it gains?
3. Does showing prior outputs from the same run (the agent's own earlier drafts) cause measurable copying in later attempts, and does summarising failures as no-goods or dropping them from context remove it? (Link to the CDCL and Go-Explore subfields.)
4. What are the real effect size and control rate of the generic parts technique (McCaffrey 2012, and any replication)? Does an LLM version help on MacGyver or BrainTeaser at equal tokens?
5. Does function-level (abstract) presentation of prior solutions reduce LLM copying the way it does for people, and where do the primary studies (Atilola 2016, Ezzat 2020, Agogue 2011) put the size of the effect?
6. Is the Sio 2015 meta-analytic result (examples narrow variety but raise novelty and quality) correct and how large is it? Need the full text and per-moderator effects (number and commonality of examples).
7. Does affordance-grounded reflection (MacGyver) beat chain-of-thought alone on functional-fixedness items for current models, given that GPT-4o with CoT already matched humans in Gjerde 2025?
8. Is fixation from domain knowledge (Wiley, Ricks, MedEinst) in LLMs reduced by extra thinking, by sampling, or by neither? Humans do not benefit from more working memory in this case.
9. Do the human null results for avoid instructions (Jansson and Smith 1991, Viswanathan) replicate, and does the group-vs-individual or psychology-vs-engineering split explain the mixed findings?
10. Which cheap fixation test could serve as a standing probe for the agent (candle-style item, MedEinst-style counterfactual pair, Deng category slope), and which has the least judge noise?

## Gap search results

Evidence in evidence_d.jsonl (d01-d20, 19 opened, 1 not opened). Claims K13, K05, K09, K11, K18, K23 and K29 were extended; K31-K40 are new. Web search quota was used up, and OpenAlex, Semantic Scholar and arXiv API calls were rate-limited after a few queries, so I opened papers by direct link only. No PDFs remain in D:/research_scratch/A09.06 after cleanup.

| Gap | Status | What was found |
|---|---|---|
| 1. Best defixation procedure at equal tokens (final-pick quality) | Open | No source ran it. Closest: Verbalized Sampling compares Direct, CoT, Sequence, Multi-turn and VS at equal candidate counts, but scores pool diversity and mean quality, not the best pick (d03). Listing k answers in one call captures most of the gain on jokes (1.83 to 2.93, VS 3.01). One prompt with many personas was worst; parallel calls were better (d13). Temperature is weak (d16, d19). Same-model critique-and-edit without an outside check hurt reasoning accuracy (d18). |
| 2. Code-checked banned list vs free "avoid" | Partly closed | Free avoid instructions are unreliable for LLMs (d09, old models, table partly garbled). A human per-idea coded signal "search for another path" gave a borderline gain (d08, d=.49, N=60) and the opposite signal hurt (d=.79). No LLM test of a code-checked list vs free instruction; cost not measured. |
| 3. Does seeing own drafts cause copying; do no-goods help | Partly closed | Two directions. Implicit exposure and errors in context raise later errors and over-reliance on first attempts (d05, d17); thinking mode and a sliding window removed it (d06). Explicit "give a different answer" with all earlier answers in context gave the best diversity in NoveltyBench (d02). So the instruction decides whether context helps or harms. Summarising failures as no-goods was not tested by anyone I found. |
| 4. Generic parts technique rate and replication | Partly closed | Control 49% vs trained 83%, N=14 per group, 8 problems, t(26)=4.23 (d01). This is the authors' own report; no placebo control; no replication; no LLM test. A 2018 title "Effectiveness of generic-parts technique in idea generation" exists in OpenAlex but could not be opened. |
| 5. Function-level presentation, primary effect sizes | Open | Only the review account (d11): function tree cut copied features, effect lost with a sketch; picture-vs-text did not replicate once. Atilola 2016, Ezzat 2020, Agogue 2014 not opened. No LLM test. |
| 6. Sio 2015 meta-analysis | Open | Could not be opened (publisher block, no open copy). Only an unverified machine summary (d15). Do not cite its numbers. |
| 7. Affordance reflection vs plain CoT | Open, sharpened | MacGyver compared only vanilla, self-reflect and divergent-convergent prompts, no CoT arm (d20). Gjerde (c23) shows CoT alone reaches human level on a multiple-choice tool task. Needs a three-arm test at equal tokens. |
| 8. Domain-knowledge fixation vs extra thinking | Partly closed | mARC-QA: R1 52% vs V3 50%, o1 48%, humans 66% (d07); MedEinst trap rates 43-66% (c26). Thinking did not remove it. Sampling not tested. Self-conditioning on errors is removed by thinking (d06), a different effect. |
| 9. Do human avoid-instruction nulls replicate; what explains the split | Open | Review lists the two untested explanations (d10). George and Wiley Exp 2: avoid removed the visual-example drop but did not beat no-example (d12). Jansson and Smith 1991, Viswanathan, and Chrysikou and Weisberg 2005 were not opened. |
| 10. Cheapest standing probe, least judge noise | Closed for design choice | Keyed items have no judge noise: counterfactual pair or tool-substitution multiple choice. Human agreement on diversity ranged 0.54 (poem) to 0.87 (story); on quality 0.49 (story) to 0.79 (joke) (d04). Deng's slope uses one GPT-4o coder with no agreement figure (d16). Recommendation: counterfactual pair or tool choice as the standing probe; use category slope only with a fixed category list and a second coder. |

### New contradictions or warnings

- Context effects point both ways: Deng, Sinha and Laban show earlier output pulling later output; NoveltyBench shows earlier output helping when the prompt asks for something different. The agent should keep earlier answers only with an explicit exclusion request, and keep raw failed drafts out otherwise.
- The George and Wiley Exp 2 result adds to the correction already in this file: the avoid line restored the no-example level but did not exceed it.
- Ezzat 2017: the gain came from more expansion ideas, not fewer fixation ideas; and wrong-direction feedback hurt more (d=.79) than right-direction feedback helped (d=.49).
- McCaffrey: "67% more" is the relative gain between 83% and 49%, not 67 percentage points. d about 1.6 is my calculation from t, not reported.
- Several of the new LLM sources are about tasks with one right answer (Sinha, Laban, Huang). Treat them as mechanism evidence, not proof for creative ideation.

### Still needed

1. A three-arm equal-token test: plain best-of-n, k-in-one-call, and one structured operator (title-revise-expand), scored on the best pick by running or a keyed probe.
2. A test of free avoid text vs a code-checked banned list vs no-good summary on the same items.
3. Primary papers for gaps 5, 6 and 9 behind publisher walls; ask the user for PDFs or retry when search quota refills.
