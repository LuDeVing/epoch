# C04.07 Story, music, art, humour systems: cross-check critique

Sources re-opened this session (full text via arXiv PDF, ACL Anthology PDF or Nature HTML): Hessel 2023, Zhang 2024, Jentzsch and Kersting 2023, Chakrabarty 2024, Tian 2024, Yang (Re3) 2022, Gomez-Rodriguez and Williams 2023, Porter and Machery 2024. PDFs deleted after extraction.

## Corrections made
1. Hessel 2023 (c04): the "human explanation beat the best machine explanation in 87.8% of pairs" is from a footnote about an earlier fine-tuned GPT-3 vs human experiment. The main result against 5-shot GPT-4 is "more than 2/3" (a18 is right). Treat 87.8% as FT-GPT-3 only. Confirmed: 62% vs 94%; GPT-4 5-shot 84.5 (table).
2. Zhang 2024: Table 4 gives 1.6% (expert) and 35.4% (crowd); the text says 34%. The 54.40 for Claude-3-Opus (c05) is a GPT-judged win rate, a different measure from the human preference. a20/b07 and c05 are consistent once the evaluator is named. Confirmed 250 million ratings, 2.2 million captions.
3. Jentzsch 2023: 909 of 1008 identical to a top-25 joke; the top-25 list covers 917 of 1008 (includes small variants). Both numbers are in the paper; they are not an error. Top four over 50% confirmed.
4. Chakrabarty 2024: 84.7% pass for New Yorker stories, kappa 0.41, aggregate Pearson 0.69 confirmed. LLM pass rates in the table are 8.7, 27.9 and 30.0 percent, so "3 to 10 times less likely" and "9 to 30%" agree.
5. Tian 2024: 14.6 / 9.3 vs 1.3 / 1.7 percent, 440 narratives, 16 annotators confirmed. "Over 40%" in the abstract is 45% diversity and 40% engagement in the text.
6. Re3: all c08 numbers confirmed (coherent 60.0 vs 45.7, relevant 64.0 vs 44.0, interesting 54.3 vs 45.0, judged human 83.3 vs 74.0).
7. Gomez-Rodriguez 2023: 80.2 vs 60.0, kappa 0.48, humour mean 3.4 and best 6.5 confirmed. Important detail: on individual metrics GPT-4 is significantly BETTER than the human writers (p=0.00031); Claude and Bing not different; the rest worse. a22 states this partly; the writers were creative-writing students and there was one prompt.
8. Porter and Machery 2024 (c23, was unopened): confirmed 46.6% accuracy, 1,634 participants in study 1 (N=16,340 judgments). Poems were generated with ChatGPT-3.5, no curation. Now opened.

## Contradictions
- Judge reliability: Chakrabarty (judge correlation near 0) vs Zhang (GPT-4 judge 67% vs crowd 61%) vs HumorRank (tau 0.889 among judges). Agreement between LLM judges is not agreement with humans. Zhang shows the GPT judge gives Claude 54.4% while humans give 35.4% and 1.6%.
- Quality vs humans: Chakrabarty (experts, professional baseline) says LLMs far behind; Gomez-Rodriguez (students baseline, single prompt) says GPT-4 ahead. Baseline and rater drive the answer.
- Lay vs expert: lay readers can't tell AI poetry apart (46.6%), yet GPT-3.5 and GPT-4 stories are attributed to AI over 80% in the TTCW study.
- Individual vs population: LLM individual originality is near human (0.711 vs 0.696) while population variability is far lower.

## Weak spots
- The historical systems (TALE-SPIN, MINSTREL, EMI, AARON, JAPE) have almost no controlled human evaluation. Our EMI and AARON lines come from Wikipedia only; Hofstadter's test has no counts (a31 not opened).
- Several modern figures are single-lab or from small samples (Mirowski n=13 of 15; TTCW 12 human and 36 LLM stories; Gomez-Rodriguez 65 stories).
- Models tested are 2022-2024 (GPT-3.5, GPT-4, Claude 3). Nothing in the set tests current frontier models on stories with matched tokens.
- No study here tests a scaffold at equal tokens against plain sampling for creative output, except in part Re3, COMIC and Tian, and those use their own baselines.

## Seen only in snippets or not re-opened
a21 (accuracy tables not extracted), c13, c14, c15, c16, c17, c18, c19 (not re-opened by me; taken from the earlier agent), a31 to a34 and c24, c25 (never opened), b22 to b25 (numbers partial), c10.

## GAPS
1. Does an explicit plan (arc, turning points) plus critique beat plain sampling on story quality at equal tokens, rated by blind experts against a skilled-human baseline?
2. Does a code-side diversity selector over N independent attempts raise human-rated novelty without lowering quality (G4, G8)?
3. Is there any LLM-as-judge method for creativity that correlates with experts above 0.5 on held-out items, and at what cost?
4. Do frontier 2025-2026 models still show the joke collapse (25 jokes cover about 90%) and the missing turning points (1.3% vs 14.6%)?
5. What is the evidence on Hofstadter's EMI test (counts, N) and Cope's later blind listening studies, beyond Wikipedia?
6. How do humans rate AI humour when the baseline is average rather than top-10 human captions or professional writers?
7. Does retrieval from a library of solved cases with typed adaptation (MINSTREL, Skald) help LLM creative tasks, and what is the sensible fraction?
8. Music and visual art: which controlled LLM or generative studies (2020-2026) give numbers on human preference or detection?
9. Does co-writing lower content diversity for newer instruction-tuned models than InstructGPT, and does sampling temperature or best-of-N fix it?

## Gap search results

Evidence in evidence_d.jsonl (d01 to d21). Sources opened in full text: Verbalized Sampling, Artificial Hivemind, Doshi and Hauser, Anderson et al., Agents' Room, CritiCS, Gorenz and Schwarz (PLOS ONE page), Orwig and Beaty 2026, CreaEval 2026, Ha et al. 2024, Figueiredo 2025, Sarmento 2024 (abstract and method only). WebSearch budget ran out after one search; arXiv, Semantic Scholar and OpenAlex APIs were rate limited, so discovery used arXiv search pages.

1. Plan plus critique vs plain sampling at equal tokens, blind experts, skilled-human baseline: PARTLY CLOSED, NOT FULLY. Agents' Room (9,900 pairwise ratings by writer-annotators) and CritiCS (Interesting 85.0 vs 57.6) show gains over one-pass or outline baselines, and human stories still win. No study matches tokens. Open: equal-token test.
2. Code-side diversity selector raising human-rated novelty without quality loss: PARTLY CLOSED. Verbalized sampling raises human-rated diversity (90 lay annotators) with flat quality on jokes and a 5 to 7 point drop on stories; Doshi shows more model ideas do not remove homogenisation. No study of an independent-N similarity selector with human novelty ratings. Open.
3. LLM judge above 0.5 with experts on held-out items: CLOSED WITH CONDITIONS. Yes at system level (rho 0.62, creativity 0.85) and zero-shot for images (r .57 to .68); no per item for stories (0.41) and for direct judging of multi-step tasks (0.31). Judges lose agreement on near-equal items (Jiang). Cost is one model call per item (two stages for CreaEval).
4. Frontier models and the joke collapse: CLOSED FOR JOKES. 2025 models (Claude 4, Gemini 2.5, GPT-4.1) show direct joke diversity 17 to 30 vs 60 to 67 with verbalized sampling; hivemind similarity above 0.8. The exact 25-joke count and the 1.3% turning-point figure were not re-run. Open: turning points on 2025 to 2026 models.
5. EMI test counts and Cope blind listening: OPEN. Only an unquantified Wikipedia line; Ariza 2009 gave HTTP 403. Needs Hofstadter 2001 or Ariza text.
6. Humour against an average baseline: CLOSED. Gorenz and Schwarz: ChatGPT 3.5 2.63 vs lay humans 2.20 (69.5% preferred AI); vs The Onion 2.37 vs 2.49, p=.14.
7. Retrieval of solved cases with typed adaptation for LLMs: OPEN. No LLM study with numbers found (one arXiv search returned nothing; a second hit HTTP 429). K02 (MINSTREL numbers) is the only evidence.
8. Music and visual art: CLOSED FOR DETECTION, OPEN FOR PREFERENCE. Images: general users near chance, professional artists 75.3%, best detector 98.0%. Suno music: 0.53 random pairs, 0.66 similar pairs (308 participants). Human preference ratings for AI art and music at scale were not found.
9. Co-writing diversity with newer models and fixes: CLOSED IN PART. Doshi (GPT-4) and Anderson (ChatGPT, group d=0.47, individual not significant) confirm collective homogenisation; min-p leaves 61.2% of pairs above 0.8 and verbalized sampling helps. Best-of-N was not tested in these studies. Open: best-of-N and temperature effect on co-writing homogenisation.

New claims K15 to K20 added; K04 raised to established, K05, K06, K07, K10 and K11 extended with the new numbers.
