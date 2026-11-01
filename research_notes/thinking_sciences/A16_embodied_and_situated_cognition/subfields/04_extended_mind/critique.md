# A16.04 Extended mind: cross-check critique

## Re-opened sources (arXiv full text via pdftotext)
Confirmed exactly:
- Kosmyna 2025: 15/18 (83.3%) LLM vs 2/18 (11.1%) Search and Brain-only failed to quote; pairwise p<.001; LLM vs others only.
- Park 2023: TrueSkill 29.89 / 26.88 / 25.64 / 22.95 / 21.21; 100 raters.
- MemGPT: 38.7 to 66.9, 32.1 to 92.5, 35.3 to 93.4; ROUGE-L 0.296 for GPT-4 baseline, 0.814 with MemGPT.
- LongMemEval: GPT-4o 0.870 to 0.606 (30.3%); Llama 3.1 70B 0.710 to 0.454 (36.1%).
- Nye 2021: scratchpad 26.5%* (few-shot, asterisk = loosened criterion) and 41.5% (fine-tuned); 200 test programs.
- Reflexion: HumanEval 91.0 vs 80.1; 130 of 134 AlfWorld; +8% absolute from self-reflection.
- Voyager: 63 unique items text present; -73% without self-verification, -93% random curriculum. The 3.3x and 15.3x ratios were not located by my grep (probably in a table or figure); treat as unverified here.

## Corrections and caveats
1. Kosmyna session 4: lines a24/c27 label the group with 1/9 correct quotes as "LLM-to-Brain" and 7/9 as "Brain-to-LLM". The paper says "reassigned LLM group" 1/9 correct and "reassigned Brain-only group" 7/9, and the labels are ambiguous about direction. Do not use the direction until checked against the paper's group definitions. Also, a24 says brain-to-LLM had higher recall; this fits only if "reassigned LLM" means the former LLM users now unaided. Needs a re-read.
2. The 83.3% quoting figure appears in the paper's general quoting question; c27 attributes it to session 1 specifically. Unverified.
3. Kosmyna is a preprint ("under review"), N=18 per group, EEG. Four lines (a23, a24, b22, c27) are one source.
4. MemGPT appears in a26, b14, c06, c07, c08 and Reflexion, Park, Voyager, LongMemEval, Lost in the Middle each appear 3-4 times. Do not count repeats as independent.
5. Camerer 2018: a10 says Sparrow's Google Stroop failed to replicate there. b03 could not see Sparrow-specific numbers, and I could not confirm which Sparrow experiment Camerer replicated. The clean source for the Stroop failure is Hesselmann 2020 (a11 and b04 agree: N=117 tested, 89 final, BF01=5.07, 825 vs 821 ms). Attribute to Hesselmann only until Camerer is checked.
6. Hesselmann and Gong and Yang: PeerJ and Frontiers pages were not reachable by me this session; relied on two agreeing lines each (a11/b04, a19/b02). Not independently re-opened.
7. Dahmani GPS (r=-0.22, N=50, follow-up N=13): not re-opened; fragile statistics.

## Contradictions
- Google effect: meta-analysis says moderate positive pooled effect, d range -0.85 to 4.38, while the founding Stroop result failed. The headline effect is real in some designs, the priming mechanism is not.
- Offloading hurts memory (b06, Kosmyna) vs offloading frees resources for new learning (Storm and Stone). Reconciled by intent: harm to the offloaded item, benefit to the next item.
- Vendor memory benchmarks (Mem0, A-MEM, Zep) each report themselves best on LoCoMo; rankings are not independent.

## Weak spots
- Almost no study tests a philosophical claim. No experiment separates extended from embedded cognition (b26).
- LLM studies measure retrieval accuracy or believability, rarely whether the model actually used the note (c04). Twin Otto test not run anywhere.
- No study compares notes against equal-token reasoning without notes.
- Seen only in snippets or not opened: b03, b05, b12, b13, b23, b24, b25, c28.

## GAPS
1. At equal tokens, does an agent with a persistent notes store beat the same agent with the same tokens spent on longer reasoning, on multi-session tasks?
2. Does the agent actually follow a retrieved note when it is wrong (Twin Otto test), and how often does it ignore a correct one?
3. What does a calibrated consult-or-recall gate (confidence-based, as in Gilbert/Hu/Risko work) gain over always-consult or never-consult for LLMs?
4. Which note format wins at equal tokens: flat chronological, fact-extracted, linked and rewritten (A-MEM), or verified skills (Voyager)?
5. Does reading notes reduce the agent's own later retention or reasoning on unannounced follow-ups (the offloading cost found by Grinschgl 2021)?
6. Where in the prompt should notes go given the lost-in-the-middle U shape with current frontier models (2025-2026 replication)?
7. Does writing a reflection note beat storing the raw trajectory in non-coding domains (Reflexion's +8% is one paper, 100 questions)?
8. Does the Google-effect pattern (remember where, not what) appear in LLMs told that storage is available?
9. Verify the Kosmyna session-4 group labels and whether any peer-reviewed or larger replication of LLM-assisted writing and memory exists.
10. Does Camerer 2018 replicate Sparrow's other experiments, and which?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d18, all opened). Claims K25-K35 added; K03, K04, K10, K11, K15, K16, K21, K22 updated. Web search quota ran out early, and the arXiv, Semantic Scholar and OpenAlex search APIs returned HTTP 429, so I worked from known arXiv IDs and Europe PMC. Some 2025-2026 papers on these gaps may exist that I could not find.

Closed:
- Gap 9 (Kosmyna labels): closed. "Reassigned LLM group" = former Brain-only now using the LLM, 1/9 correct quotes. "Reassigned Brain-only" = former LLM users now unaided, 7/9. Lines a24 and c27 had the direction reversed. The 15/18 figure is session 1; 6/18 still failed in session 3. No peer-reviewed or larger replication found. A medical-student study (Cureus 2026, N=95 analysed) found higher retention with AI tutoring, but with a different design (d18).
- Gap 10 (Camerer): closed. Camerer 2018 replicated Sparrow Experiment 1 (Google Stroop) only: original N=46, replication stage 1 N=104 and pooled N=234, null. The other Sparrow experiments were not part of it, and I found no direct replication of them. Hesselmann (N=117 tested, 89 final) fixed Sparrow's design objections and still found a null (d03).

Mostly closed (for facts, not agent notes):
- Gap 2 (Twin Otto): ClashEval measured it. A wrong passage beats a correct own answer 15.7% to 31.3% of the time; a right passage is ignored 2-4%. With mixed evidence models cling to prior belief (Xie, GPT-4 80%). Not measured for agent-written notes (d05, d06).
- Gap 3 (consult gate): the model's own confidence predicts note-taking and calibrating it raised accuracy about 14%; a popularity gate beat fixed policies by 5.3 points at half the cost; a trained classifier misroutes often. No test with an agent's verbal confidence on persistent notes (d05, d07, d08).

Partly closed:
- Gap 1 (notes vs equal tokens): Dynamic Cheatsheet beats a 3-sample majority vote (50.0 vs 23.3 on AIME 2024) at about 1.1x to 1.7x tokens, and full-history append is worse than curated notes. ReasoningBank shows memory and compute are complements. Not matched exactly, and not across separate sessions. Still open as a clean test (d09, d10, d11).
- Gap 4 (format): independent MemoryAgentBench puts Mem0 21.1, Zep 24.0 and MemGPT 28.3 below BM25 41.5 and the bare model 42.3; the vendor LoCoMo rankings do not hold. LongMemEval says keep raw text and add facts as keys; summaries lose information. Nobody compared Voyager-style skills against these at equal tokens (d12, d13).
- Gap 7 (reflection vs trajectory): domain split in ExpeL (insights win on HotpotQA 36 vs 31, trajectories win on ALFWorld 55 vs 50). Reflection without an external check hurts (Huang). Reflexion's +8% still rests on one paper (d14, d15).
- Gap 6 (placement): NoLiMa 2025 sees the dip in simple tests at 32K and a collapse everywhere in harder tests. No 2026 frontier model tested (d16).

Still open (no LLM study found):
- Gap 5: reading notes reducing later retention or reasoning in LLMs.
- Gap 8: Google-effect pattern in LLMs told storage is available.
- The gap-1 cross-session version.

Corrections to earlier files:
- K03: the Gong and Yang meta-analysis (opened now) mixes self-esteem, survey and lab measures and gives no pooled d in the text. The d range of -0.85 to 4.38 and the mobile and prior-knowledge moderators are not in the text. Status moved to contested.
- ClashEval abstract says "over 60%" but the tables show 15.7-31.3% context bias overall; the 60% condition was not located.
- Voyager 3.3x and 15.3x ratios still unverified.
