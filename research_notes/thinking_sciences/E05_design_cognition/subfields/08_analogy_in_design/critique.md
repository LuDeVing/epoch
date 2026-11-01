# Critique: Analogy in design (E05.08), cross-check

## Numbers re-opened (from arXiv or author PDFs, this session)
Confirmed with no change: Hope et al 2017 (46/37/30% on 9 shared seeds at k=2, N=105/49/54; 38/22/21% at k=3, N=118/68/63; 749 ideas; kappa 0.51; pr(good) 0.71 and 0.56). Fu et al 2013 (max novelty F(2,59)=4.139, d=-0.82 vs near, -0.91 vs control; mean quality F(2,65)=4.07, d=0.76 near vs far, 0.54 near vs control; max quality F(2,65)=4.13, d=-0.76 and -0.72). Webb et al 2023 (GPT-3 near p=0.0039, far p=0.065; OR=0.37 p=0.0003; 3.24 CI [1.24, 8.5]). Sourati et al ARN (GPT-4 94.0/92.5/57.1/29.1; 17.7 without the instruction; model averages 75.0 near, 39.6 far; human 97.9/94.1). Ding et al 2023 (185/220 adding, r=-0.0266 p=0.6939). SCAR (GPT-4 73.28 English, 77.17 with 1-shot plus background; averages 65.01 and 69.10; human 85.94/86.03). Lewis and Mitchell 2024b story table (0.89/0.61/0.75; 1.0/0.72/0.86; humans 0.78).

## Corrections and clarifications
1. Ding et al 2023: the text says one-shot is more useful than zero-shot "80% compared to 40%", but Table 1 gives potential usefulness 0.82 vs 0.68 and unique-and-useful 0.70 vs 0.43. The 40% in the text matches neither column. Entries a14 (table) and c03 (text) differ because the paper contradicts itself. Use the table.
2. SCAR (a25 vs c06): c06's note that the first column could not be identified is resolved. The first column is the English subset score; the last column is the average over subsets. 69.10 is the average (1-shot plus background), 77.17 is English.
3. Lewis and Mitchell 2024b Table 4: the row labels in the PDF text are garbled. Reading by totals (16+11=27, 18+13=31) the 0.89/0.61 row is Webb's GPT-4 run and 1.0/0.72 is the authors' own GPT-4 run. Humans are 0.78 for both orders. Entry b19 is right; c16's labelling is right.
4. Hope et al: 46% (N=105) is the k=2 rule on the 9 seeds common to all conditions; 38% (N=118) is the k=3 rule. These are different cuts, not a contradiction. Do not quote 46% and 38% as one result.
5. Fu 2013 vs Chan 2011: a31 and a32 are consistent. Chan found no distance effect on mean or max quality; Fu found near > far on quality.

## Contradictions between sources
- Far vs near: Chan 2011 (far helps novelty, d=0.56 to 0.64) against Fu 2013 (far hurts max novelty d=-0.82). Same group, same style of protocol, different problem and stimulus set. Chan, Dow and Schunn 2014 note the literature splits evenly.
- Chan 2014 field data say source distance adds little (AIC drop about 6) while any analogy use is linked to shortlisting. This does not match the lab claim that distance is the lever.
- Webb et al (human-like LLM analogy) vs Lewis and Mitchell (brittle, order-biased, counterfactual accuracy 0.35 to 0.49 vs 0.753). Unresolved; the replication used the same models.
- Evidence of LLM analogy quality (Bhavya: 175B equals humans at 70% meaningful) sits beside StoryAnalogy and ARN where models are at or below chance for far analogies. The tasks differ: generating a analogy vs recognising a structural one.

## Weak spots
- Almost all human design studies use novices (students, crowd workers), one problem each, short sessions. No expert replication and no finished-design outcome.
- LLM studies are mostly GPT-3 to GPT-4 era (2022 to 2023). No frontier-model (2025 to 2026) measurement of near vs far was found in these files.
- Self-reported gains (Yasunaga, Yu and He) have no independent replication and no equal-token comparison with simple resampling.
- Usefulness and novelty are judged by few raters (one researcher in Ding; five graduate students in Hope; two graduate students as the SCAR human baseline).
- The novelty benefit of far analogues is untested where the criterion is correctness checked by code, which is what our agent needs.

## Only seen in snippets or second-hand
Gentner, Rattermann and Forbus 1993 (55% vs 12%), Gick and Holyoak 1980/83 (about 10% vs 41%), Forbus MAC/FAC, Linsey WordTree, Marshall et al, Yu Kraut Kittur 2014, Chan and Schunn 2015 (abstract only), Lewis and Mitchell 2024b beyond the story table. Claim K07 rests on these and is marked single-source.

## GAPS
1. Does a near vs far analogue step beat a same-token resampling baseline on a code-checked task for a current (2025 to 2026) model? No file has this measurement.
2. Is the far-analogue failure (ARN 39.6%, GPT-3 far p=.065) still present for current frontier models, and does an explicit "name the shared structure first" step close it?
3. Which retrieval key works best for an agent's lesson memory: surface text, abstracted purpose/mechanism vector, or typed structure (MAC/FAC style)? Hope et al is the only controlled test, with wide intervals.
4. Does the quantity cost of far analogues (mapping tokens) wipe out the novelty gain at equal tokens?
5. Does analogical encoding (comparing two solved cases and writing the shared schema) improve transfer of an LLM's stored lessons, as it did for humans (about 3x)?
6. Can the model's own usefulness rating of an analogue predict downstream success? Ding found r=-0.027 for humans' a-priori ratings; no LLM-as-judge test was found.
7. Where is the sweet spot of distance, and is it task-dependent enough that it must be estimated per problem class online?
8. Do Yasunaga-style self-generated exemplars survive an equal-token comparison with 5-shot CoT and with extra samples on newer models?
9. How often do analogues cause harm (Ding upper bound 25%), and can code-run checks screen them cheaply?
10. Are there published 2024 to 2026 LLM design-by-analogy studies with expert designers or finished-design outcomes? The 85-study survey says rigorous evaluation is lacking.


## Gap search results

Tools: WebSearch quota was used up and the arXiv, Semantic Scholar and OpenAlex search APIs returned 429, so I found papers through Crossref search, Europe PMC, arXiv abs/PDF pages and the citations of the 2026 survey. This means coverage of 2025 to 2026 LLM analogy papers is thin. 20 evidence lines are in evidence_d.jsonl (d01 to d20); claims K03, K09, K12, K13, K16, K17, K18 got new evidence ids, K13 moved from established to contested, and K19 to K24 were added.

1. Near vs far against same-token resampling on a code-checked task, current model: STAYS OPEN. No such measurement exists in what I could reach. The closest are Yasunaga (self-consistency adds +7.5 GSM8K, +8.7 MATH, while the analogue method adds only +1.1 and +2.4 over 5-shot, d01) and Cheng 2026 (strong models ignore exemplars, d03).
2. Far-analogue failure on frontier models, and a name-the-structure step: PARTLY ADDRESSED, not closed. No 2025 to 2026 far-vs-near benchmark run found. Webb 2025 shows the counterfactual failure was counting: GPT-4 with code execution matches humans (P=0.92, d15). Step-back (d05, d06) is the nearest abstraction-first test: it helps PaLM-2L by about 7 to 8 points but GPT-4 by only 0.3 to 1.6 over CoT, with up to 12% new errors. No test on analogy items.
3. Best retrieval key: STAYS OPEN. ExpeL: task similarity beat step similarity and random (d07). AWM: abstracted workflows beat concrete examples (+4.0 step SR, d09). Dynamic Cheatsheet: curated beats full history (d12). Nobody varied surface vs abstract-mechanism vs typed-structure key.
4. Mapping-token cost vs novelty gain at equal tokens: STAYS OPEN. No equal-token study found. Yasunaga did not control tokens.
5. Analogical encoding for stored LLM lessons: STAYS OPEN, with a lead. ExpeL builds rules from a failure and success pair (+5 on FEVER transfer, d08) and Dynamic Cheatsheet shows curation beats verbatim storage (d12), but neither has a pair-vs-single-case arm.
6. Self-rating predicts success: STAYS OPEN, evidence points against trusting it. No direct test. Indirect: LLM ideas lose 1.0 to 1.9 rating points once executed (d14), intrinsic self-correction lowers GPT-4 GSM8K 95.5 to 89.0 (d16), and an agent-memory audit credits 169 retrievals but only 10 are real marginal helps (d17, abstract only).
7. Distance sweet spot and online estimation: PARTLY ADDRESSED. Biomimetics 2024: biological and cross-domain analogies did not differ, both beat near (d18, abstract only). AWM: online lessons gain more as the train-test gap widens (d10). The survey says optimal distance depends on stage, goal and expertise (d19, secondary). Supports estimating per task, but no LLM sweep exists.
8. Self-generated exemplars at equal tokens on newer models: LARGELY ANSWERED in direction. Margin over 5-shot is small (d01), model must be strong (d02), and recent strong models ignore exemplars while R1 degrades with few-shot (d03, d04). Not run: an exact equal-token comparison with extra samples; and the Cheng tests use maths, not analogies.
9. Harm rate and code-run screens: PARTLY ADDRESSED. Harm is measurable: step-back introduces up to about 12% new errors (d06); retrieval cut GPT-4o scores in several Dynamic Cheatsheet cells, e.g. MMLU-Pro Eng 53.2 to 44.0 (d11, d13). No study tested a code check as the screen; that remains a design claim.
10. 2024 to 2026 expert or finished-design LLM DbA studies: STAYS OPEN, confirmed absent in reachable sources. The survey says the same (d19). Nearest: 32-student counterbalanced AI ideation test, human-only higher on innovation (d20), and the ideation-execution gap with 43 experts (d14, NLP not design).

Net effect on the schema: the direction of evidence is that analogue and exemplar injection has small or no gain on strong models, abstraction/curation helps, retrieval can harm, and any analogue or lesson must be judged by matched with/without runs checked by code. All of this is indirect; a direct equal-token near/far test on a current model is still the missing measurement.

Corrections to earlier text: K13 was marked established; it is now contested because the authors' own gain over 5-shot is small and newer work shows exemplars are ignored. Items marked opened:false in evidence_d (d17, d18) were read as abstracts only.
