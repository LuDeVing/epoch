# Critique: B01.03 Insight as a process (cross-check)

Checked 2026-11-03. Sources re-opened this session: arXiv 2601.00514 (HTML), arXiv 2509.14704 (PDF), Danek and Wiley 2017 (PMC5247466), Sio and Ormerod 2009 (PDF), Tree of Thoughts (arXiv 2305.10601), Huang et al. 2024 (arXiv 2310.01798), Jung-Beeman 2004 (PMC387268), Speed 2023 (arXiv 2309.07683), Orru 2023 (PMC10244637), BRAINTEASER (arXiv 2310.05057), Knoblich 1999 PDF.

## Corrections and confirmations

Confirmed exactly:
- Illusion of Insight (2601.00514): shifts 6.31% of traces; formal Aha detector 1.79%; Qwen-1.5B 2.57% vs 16.44% (N=723,200); Table 2 shift rates Xwords 1.22, Math 2.65, RHour 14.32, Qwen-7B Math 1.50, Llama-8B Math 5.04; pooled accuracy 6.6% with shift vs 29.0% without; forced reconsideration Math 32.21% to 40.62% (+8.41 pp), wins 50,574 vs 23,500; -22.88 pp low entropy, -7.40 pp high entropy; kappa 0.726 / 0.79.
- Nazonazo (2509.14704): human 52.9% (n=126), 7.6% vs 17.6%, OR 2.29 (1.99-2.64) with 9.42% vs 19.25% on 201 items; verification failure 5.23% to 39.34% (Table 2); Grok-4 Japanese 29.5% vs English 48.8%, p=0.0071.
- Danek and Wiley 2017: 1778 solutions, 36.8% (654) correct; Aha 66.50 vs 52.34, t(69)=10.21; 417 of 1124 wrong above correct mean; times 35.81 vs 42.46 s.
- Sio and Ormerod: 117 studies, 3,606 participants, median n=25; unweighted 0.41 (CI 0.28-0.54); weighted 0.29 (CI 0.21-0.39); median effect 0.26.
- ToT 4% vs 74% (also IO 7.3%); Huang rounds (75.9/75.1/74.7; 75.8/38.1/41.8; 95.5/91.5/89.0); Jung-Beeman 59% solved, 56% insight, 0.25% peak difference; Orru 7/15 and 5/15, p<0.72, human 0.55 and 0.35; Speed 1.5-3.5 and 4.5/5.

Corrections:
1. b01 says "over 11M traces". The arXiv abstract says "1M+"; per-model counts (723,200 for Qwen-1.5B) fit about 1-2M. Use 1M+ (a21 is right, b01 is wrong). The HTML shows "1 1 M+", which is probably a rendering artefact.
2. a04 SD for the weighted mean is cut off; the PDF gives SD 0.04 and CI 0.21-0.39.
3. Danek and Wiley 2017: a11 says 35 videos, b13 says 37 tricks. Both are right: 37 shown, 2 never solved, 35 analysed. Participants 70 (35 per counterbalance condition).
4. BRAINTEASER human 92% is from 3 expert annotators on 102 sampled items, not a crowd sample. Treat as an upper bound, not a typical human.
5. Gilhooly 2016's eight-test average r=0.11 and Strick g=0.224 are second-hand (b17); not re-opened.
6. Knoblich 1999 statistics (F values in a02, a03) could not be re-verified: text extraction of the PDF did not return the stats lines. They stay as recorded, unverified this session.

## Contradictions between sources

- Aha vs correctness: Webb 2016 (r about .40-.50 for classic insight, near zero for non-insight) and Wiley and Miller 2026 (F=112) support a link; Danek and Wiley show many false insights. Both hold: the feeling predicts correctness on average, but not per item.
- Incubation: Sio and Ormerod weighted d 0.29 versus Gilhooly's eight-test r=0.11 on intermittent work. Effect size depends on pooling and the break task.
- LLM insight performance: Speed (GPT-4 4.5/5) and Orru (modal human) versus Nazonazo, BRAINTEASER, Only Connect (large gaps). Differences: older public items (contamination), tiny N, partial credit, zero-shot retrieval-free protocols.
- "Aha moment" as a good sign in DeepSeek-R1 vs Illusion of Insight, Liu 2025, Wu 2025: shifts are rare and not linked to accuracy. The R1 paper itself cites a blog saying there may be no Aha moment.
- Reconsideration helps on MATH (+8.41 pp) but not on crosswords or Rush Hour, while intrinsic self-correction hurts (Huang). The difference is an externally triggered, entropy-gated pass vs unprompted re-reading.

## Weak spots

- Almost every LLM result compares an unscaffolded model with humans. Very few test an insight-style operator at equal tokens.
- Forced reconsideration is two passes: no best-of-2 control with the same tokens.
- Small samples: Jung-Beeman N=13, Knoblich Exp 1A N=20, Orru N=20 humans, Alderete 30 vs 33 trials, Speed single observation for GPT-4.
- Many reasoning-model analyses are on Qwen and Llama small models under GRPO; transfer to frontier models unknown.
- Nazonazo is Japanese; language of thought changed accuracy for Grok-4 only.

## Seen only in snippets or not opened

b20 (Weisberg 2015 claim), b21-b27 (Wallas, Metcalfe and Wiebe, Schooler et al., MacGregor, Becker 2021, Kizilirmak 2019: numbers not verified), a25 (Ohlsson 1992), b11 (McCoy 2025: abstract only), b12 (BRAINTEASER abstract), c12, c24. a13 (Kim 2026) is theory with no numbers. No LLM compound-RAT or incubation study was found (c26).

## GAPS

1. Does an entropy- or stall-triggered restructuring step (O6) beat plain continued reasoning and best-of-2 at equal tokens, across math, riddles and planning? (Only Illusion of Insight tests this, with unequal tokens.)
2. What does an incubation analogue do for an LLM: context reset, parked subproblem, or an unrelated interpolated task? Any measured result on RAT or compound-RAT items?
3. Does misleading-cue removal (drop the fixating context) at impasse recover accuracy, and how large is the fixation penalty on frontier reasoning models (post-2025)?
4. Which stall detector works: token entropy, repeated-answer rate, self-rated confidence, or step count? Reported accuracy of each as an impasse signal.
5. Can the verification stage (S8) be made reliable when the same model recorded the right answer and rejected it (5-39% of wrong answers)? Does an independent verifier fix it at equal tokens?
6. Are LLM-Aha confidence jumps predictive of correctness (like Aha-accuracy r about .4-.5 in humans) or are they false insights (like 37% of wrong human answers)?
7. Do the human boundary conditions (verbal vs visual, break task demand, break length, individual differences) carry over to LLM tasks?
8. Are there replication failures for the matchstick constraint-relaxation and transfer result (Knoblich 1999) and for the right aSTG finding? The cross-check found none but did not search for them.
9. Does storing the restructuring step with an insight solution improve later reuse (memory advantage in humans, 57.7% vs 35.4%) in an agent?
10. Does the Alderete context-graph result (+20.6 points) replicate beyond one model family and 63 trials?


## Gap search results

Searched 2026-11-03. Evidence in evidence_d.jsonl (d01-d18). Tool limits: arXiv search API returned empty, OpenAlex free budget exhausted, Semantic Scholar 429, so coverage is by WebSearch plus direct PDF opens. Search counts are small, so "none found" is weak evidence.

- Gap 1 (O6 trigger vs continued reasoning and best-of-2 at equal tokens): OPEN. No paper found with that control. Closest: Singhi 2025 (d12) says more independent attempts beat verification at low budgets, and EAT (d06) shows models often reach the right answer early and keep revising, so extra tokens often add nothing.
- Gap 2 (incubation analogue, RAT): OPEN. No LLM incubation or compound-RAT study found (d03). Indirect: a long sequential chain beats many short ones where state matters (d04). Human incubation on RAT has a null study (d02, snippet only).
- Gap 3 (misleading-cue removal, fixation penalty on frontier models): OPEN. Only older or tiny studies (d09 N=6 per cell, d10 old models). Liu 2025 (d18) is about human users, not model fixation.
- Gap 4 (stall detector): PARTLY CLOSED. Entropy after the stop token (d06), high-entropy transition tokens (d07), loop and hesitation triggers (d05), non-falling entropy plus repetition (d08, snippet). All validated for stopping or delegation, none for impasse precision and recall. Answer repetition is unreliable when errors are self-consistent (d13).
- Gap 5 (reliable S8): MOSTLY CLOSED on direction. Cross-family verifier beats self-verification (d11); self-consistent errors need an external check (d13). At equal tokens, more attempts beat verification until about 8x compute (d12). Not tested on insight riddles.
- Gap 6 (LLM Aha jumps predictive?): MOSTLY CLOSED for trace shifts (negative association, d14 re-using a21); open for verbal confidence jumps.
- Gap 7 (human boundary conditions carry over): OPEN. No LLM study of verbal vs visual, break length or individual differences.
- Gap 8 (Knoblich/aSTG replication failures): PARTLY CLOSED. No failed replication of the core constraint-hierarchy result found; the interactivity add-on failed to replicate in three experiments (d01). aSTG: nothing new found.
- Gap 9 (store restructuring step): PARTLY CLOSED. Strategy memory helps (d15) but agents often ignore condensed experience (d16). The insight-flag memory advantage is untested in agents.
- Gap 10 (Alderete replication): OPEN. No replication found (d17).

New claims K18-K25 added; K03, K06, K07, K08, K11, K12, K15 gained evidence ids. Not re-opened or only partly read: d04, d07, d16 (abstracts and intros), d08 and d02 (snippets), d10 (not extracted).
