# C10.01 Structure mapping (SME): cross-check critique

Scope: 86 evidence lines (a01-a30, b01-b27, c01-c29). Claims written: 28 (C10.01-K01 to K28). Sources re-opened this pass (PDF text): Webb et al. 2023, Lewis and Mitchell 2024, Sourati et al. 2023 (ARN), YARN 2026, Qin et al. 2025, Yasunaga et al. 2024, FAME 2023, SME 1989, Gentner-Rattermann-Forbus 1993, Lovett and Forbus 2017, Gentner-Loewenstein-Thompson 2003.

## Corrections and confirmations (ten key numbers)
1. Webb 2023 story analogies: confirmed (N=54; GPT-3 near p=.0039, far p=.065; OR=.37 p=.0003; 15/54 always right). The GPT-4 far p=.0039 is the same value as GPT-3 near. Both are real. p=.0039 equals 8 of 8 correct two-sided, so each condition has only about 8 items. Added as a caveat in K17.
2. Lewis and Mitchell: humans .753, GPT-3 .488, GPT-3.5 .350, GPT-4 .452 confirmed. The PDF table text is garbled and shifts labels by one row, which is a risk for anyone re-reading it. N=136 recruited, 2 rejected on attention checks. 1,876 human and 6,840 per-model samples confirmed.
3. Gentner-Rattermann-Forbus 1993: soundness 4.40/2.80/2.74 and retrieval .78/.44/.25 confirmed; r(52)=.15 between the two measures. Added the three-study numbers (surface .78/.53/.52; analogy .44/.12/.07).
4. SME 1989: heat/water top gmap 5.99, atom 6.03 vs 1.87, PHINEAS 53 min to 34 s all found in the text. The 3.94/2.44/4.04 values were not re-checked.
5. Lovett and Forbus 2017: 56/60 = 75th percentile (1993 norms); humans 54/60 = 61st percentile; mean 30.0/36 for 40 retained participants. CORRECTION to avoid confusion: the paper's "41st percentile" refers to a different model that got 50/60, not this one. Note a22 says "42 students (2 excluded)", the paper's 40 retained agrees.
6. ARN: near 97.9 vs 75.0, far 94.1 vs 39.6, far-vs-near-distractor 33.9, humans 96.0 overall, all confirmed. These are 2023 zero-shot models. No 2025-2026 reasoning model was tested.
7. YARN: 0.17 / 0.24 / 0.46 / 0.45 / 0.41 / 0.28 confirmed. Nuance not in a27: for Qwen, hybrid loses to zero-shot on ARN far (0.47 vs 0.52); only Llama gains there (0.46 vs 0.42). Also the "structural mapper" is a greedy cosine-over-embeddings mapper, not real SME. Claim K13/K14 reflect this.
8. Yasunaga: GSM8K GPT-3.5 75.0 / 75.8 / 76.7 / 77.8 and MATH 33.0 / 33.9 / 34.9 / 37.3 confirmed (rows 0-shot, 0-shot CoT, 5-shot CoT, self-generated). Gain over 5-shot CoT is only about 1.1 points on GSM8K and 2.4 on MATH. No variance reported in the main table.
9. Qin: GSM8K 71.5/75.5/75.1/76.3/75.3 confirmed; BBH exception (relevant best average) confirmed. Correction: their "Relevant" arm (71.5) is far below Yasunaga's 77.8 on the same model, so the two papers' baselines are not on the same footing.
10. FAME: 81.2 / 77.8 / 13.1 / 90 vs 70.2 confirmed; table 85.0 / 77.5 / 77.8 vs GPT-3.5 92 / 80 / 44. The 90 vs 70.2 human comparison is on one small task.
Also confirmed: Gentner-Loewenstein-Thompson 15/32 (47%) and chi2(1,N=48)=7.92, 48% vs 19% chi2=11.85 (N=128), 90% guided vs 70% comparison in face-to-face.

## Contradictions and tensions between sources
- Webb (GPT-3 matches students on letter strings) vs Lewis and Mitchell and Hodel and West (collapse on counterfactual alphabets) vs Webb 2024 reply (collapse is counting; code fixes it). Not settled; the code-execution result is one group's own test of its own claim.
- Yasunaga (analogical prompting helps) vs Qin (relevance does not matter on math, correctness does). The effect size in the original is small, so the mechanism is probably worth little.
- YARN (structure helps on far) vs its own table (helps for Llama, not Qwen). One paper, no variance, 8B models.
- Raven's: a22 reports the human equivalent as 61st percentile via a conversion to 60 items; c23 (a survey) converts 44/48 to 55/60. Different conversions, same story.
- ARN says SBERT alone gets 77.9% on near analogies, higher than the LLM average of 75.0%. Cheap similarity already solves near cases.

## Weak spots
- No study tests the central design question: does an SME-like score computed from LLM-written relation lists predict whether a transferred step helps an agent (K27).
- Almost all LLM tests are 2023-2024 models (GPT-3 to GPT-4o, Qwen3-8B, Llama-3.1-8B). No frontier reasoning-model results on ARN, StoryAnalogy, or Gentner story sets were found.
- Human SME evidence is old (1986-1999) and mostly small-N college samples. Few direct replications of the cognitive-science results exist; I found none that failed, but absence of replication papers is not evidence of success.
- Small item counts in key LLM comparisons (Webb stories, about 8 per condition).
- Reported conversions (Raven's percentile, FAME human comparison) depend on one-off norms.
- Several evidence lines are not first-hand (a19 Forbus and Oblinger 1990, a20 Wolff and Gentner 2011, a30, c05, c22, c24-c27, c29), seen only through later papers or surveys.

## Seen only in snippets or second-hand (opened:false)
a14 (partly; numbers verified here from the 1993 paper), a19, a20, a30, c05, c22, c24, c25, c26, c27, c29. Treat as unverified. The survey figures in a28/c23 (Donvito and Lieto) are a formal scoring by the authors, not measurements, and were not re-opened.

## GAPS
1. Does an SME-style structural score, computed in code from LLM-written relation lists, predict which transferred steps help the agent (score vs benefit, at equal tokens)? No study found.
2. How well does a current frontier reasoning model do on far analogies against surface distractors (ARN far-vs-near-distractor, StoryAnalogy) with and without a code-side structure step? Existing numbers are 2023-2024 models.
3. How reliable are LLM-written relation lists as input: how much do they vary across runs, paraphrase, and abstraction level, and how does the mapping score vary with them? (SME is sensitive to representation; YARN shows raw input is below chance.)
4. Does a structural step help only on far analogies (low surface overlap) and hurt on near ones, so that routing by surface overlap is worth it? YARN is mixed and one paper.
5. What is the net token cost of a structured mapping step (relation extraction, greedy merge, inference check) against its accuracy gain, versus just writing two cases side by side (analogical encoding)?
6. Is the benefit of analogical encoding (compare two cases) reproducible in LLMs, and does a random-correct-case control remove it (as Qin found for self-generated examples)?
7. Does support-based gating of candidate inferences reduce wrong transfers in a model, and what threshold works? Evidence is only a small coaching prototype and a simulation.
8. Are there independent replications or failures of the classic human results (Clement and Gentner 1991, Gentner and Toupin 1986, Markman and Gentner 1993) with modern N and preregistration?
9. Does a code tool for exact counting and matching fix the counterfactual-alphabet failure outside the original authors' lab?
10. Does answer-order and paraphrase sensitivity (GPT-4 89% vs 61%) persist in current models on story analogies, and does shuffling plus voting remove it?

## Gap search results (evidence_d.jsonl d01-d18, claims K29-K37)
Search limits: the web search tool hit its session cap, OpenAlex and Semantic Scholar rate-limited, and arXiv search gave 429 after three queries. Gaps marked "open" may be open only because the search was blocked.

1. Structural score from LLM-written lists predicting benefit at equal tokens: OPEN. Nothing found (d18, K37).
2. Frontier reasoning models on far analogies: PARTLY. No ARN or StoryAnalogy run with a 2025-26 model found. Nearest: o3, Claude Sonnet 4 and Gemini 2.5 Pro reach or pass human accuracy on ConceptARC text (o3 77.1 vs humans 73) but about 27% of correct answers rest on a wrong or unintended rule vs 7% for humans (d06, d07). On Raven-style rules with noise, o3-mini and R1 fall to 17.0% and 23.2% while a symbolic solver stays at 88.0% (d04). On OpenLock, GPT-5.2 and others gained little from a text copy of the earlier solution (d11).
3. Reliability of LLM-written relation lists: PARTLY. Only a proxy: gpt-4.1 extraction overlap between runs is about 0.55 for atomic facts and 0.21 for paragraphs (d17). SMTB paper says flat lists remove SME's higher-order signal (d08). No paper maps list variation to mapping score.
4. Structural step only for far analogies: OPEN, still one paper (YARN, c09/c10).
5. Token cost vs analogical encoding: OPEN. Only a Raven-task cost line (d05) where code replaces 4.5k to 19k reasoning tokens.
6. LLM analogical encoding with random-correct-case control: OPEN.
7. Support-based gating in a model: OPEN. Nearest is a simulation where structure mapping put the intended procedure first 86.7% vs 26.7% (d13); it orders search, not wrong transfers.
8. Independent preregistered replications of the classic human results: OPEN. The Alfieri 2013 meta-analysis and Mason 2016 were identified but could not be opened.
9. Code tool outside the original lab: OPEN. The PNAS Nexus version is still the same authors (d03). In an outside lab, generic Python did not help text ConceptARC (d06). The two tasks differ.
10. Answer-order and paraphrase persistence: PARTLY. The 89% vs 61% numbers come from Lewis and Mitchell 2024 on GPT-4-0613 (1.00 vs 0.72 in their rerun; paraphrase 0.86 to 0.72; humans no order bias) (d01). Current models and shuffle-and-vote not tested.

Corrections to earlier lines: c15 source is now first-hand (d01, Lewis and Mitchell 2024, arXiv 2411.14215, not the 2402.08955 short paper). c05 was mislabelled; Hodel and West is a synthetic-alphabet counterexample study (d14). c25 (SCAR) is now read first-hand (d09, d10). Still unverified: a19, a20, a30, c22, c24, c26, c27, c29.
