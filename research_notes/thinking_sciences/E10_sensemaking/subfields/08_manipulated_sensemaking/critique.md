# E10.08 Manipulated sensemaking: cross-check critique

## Re-opened sources (numbers checked against paper text or abstract this session)
1. Chan et al. 2017 (PMC5673564): k=52, N=6,878; ds 2.41-3.08 / 1.14-1.33 / 0.75-1.06. CONFIRMED.
2. Sharma et al. 2024 (arXiv 2310.13548): 98% wrongly admit (Claude 1.3), up to 27% drop from a wrong user suggestion (LLaMA 2), 27% drop from "Are you sure?" (Claude 1.3), 32-86% answer changes, 42-98% admit mistakes. CONFIRMED. CORRECTION: a19 and c17 both say "up to 27%" but for different tests and different models. They are not a conflict. Claims keep them apart.
3. Xu et al. 2024 (arXiv 2312.09085): turn-1 4.1-63.4%, MR@4 20.7-78.2%, robustness 79.3/52.1/49.9/36.3/21.8. CONFIRMED. (a18 calls 78.2% "Llama-2-7B averaged"; the paper says 78.2% is the worst model's average MR@4. Fine.)
4. Salvi et al. (arXiv 2403.14380): 81.7%, p<0.01, N=820; no personalization p=0.31. CONFIRMED (abstract). Note a22 says "vs human opponents": the abstract says compared to participants who debated humans. Fine.
5. Hackenburg et al. 2025 (arXiv 2507.13919): 51%/27%, N=76,977, 466,769 claims, +1.59pp, +2.29pp vs +1.37pp, 10.60 vs 8.34, r=0.76, 44% variance, 62% vs 78%, 56% vs 70%, 72% vs 82%, r=0.87. CONFIRMED. CORRECTION: the 27% prompting boost in the abstract and the "information prompt is 27% more persuasive" are the same figure family; do not count as two sources. The 44% explained variance applies to all conditions, 75% to developer post-trained models only (not in the evidence lines).
6. Hackenburg et al. 2024 (arXiv 2406.14508): 5.77 and 1.26 and the ~12pp ceiling present. CONFIRMED. Also: the paper calls the ceiling a likely lower bound.
7. PoisonedRAG (arXiv 2402.07867): abstract says "90% attack success rate with five texts"; table shows 0.97 for PaLM 2 on NQ. CONFIRMED in direction; the 97/99/91 triple was partly seen (0.97, 0.99, 0.91 appear in the table text). Year on a16 is given as 2025 in the source field and 2024 in the year field; the arXiv paper is 2024 (USENIX Security 2025).
8. Chen and Shu 2024: 9.6% human, ChatGPT-3.5 0.0%, GPT-4 10.0%. CONFIRMED. Caveat: this is for the hallucinated-news category only, and the base is ChatGPT-made fakes, not all LLM fakes.
9. Spitale et al. 2023: 869 recruited, 697 analysed, 0.92 vs 0.89 for false tweets, 0.72 vs 0.64 for GPT-3 as judge. CONFIRMED. a21 wrote "people believed GPT-3 disinformation slightly more"; the data are recognition rates, so synthetic fakes were recognised as false slightly less often. Same thing, but the effect is 3 points.
10. Hines et al. 2024: datamarking about 50% to below 3% (GPT-3.5 summarisation), 8.0% Q&A; encoding 0.0% / 1.8%; GPT-4 1.0%. CONFIRMED. ClashEval (>60%) CONFIRMED from abstract.

No number needed to be changed. Two wording fixes are noted above (27% pair; 27% reused).

## Contradictions and tensions between sources
- Xie (coherent LLM-written counter-evidence accepted) vs Xie (confirmation bias toward memory-consistent evidence): same paper, both true; acceptance depends on coherence and on how much of the mix agrees with memory. Pan 2023 and PoisonedRAG both support the coherence side.
- Wan 2024 says models ignore human credibility cues and weigh relevance. Hackenburg 2025 says dense fact-like content wins. These agree on "surface features that look like evidence"; they disagree with the idea that story or style cues carry weight. Storytelling is untested here.
- Chen and Shu say LLM fakes are harder to detect; Spitale shows only a 3-point gap. The size of the "AI fakes are better" effect differs a lot by method.
- Inoculation: big gain on technique recognition (d up to 0.68), small gain on truth discernment (d 0.10-0.32) and a field effect below the preregistered threshold. Chan 2017 shows debunking is partial. Together: telling people or models a technique exists does not reliably change the final judgment.

## Weak spots
- The founding claim (deep stories set later frames) rests on one qualitative paper (Prochaska 2024, about 1000 tweets, no inter-coder statistics, no outcome measure). No replication. Not tested on people experimentally or on LLMs. The agent link is by analogy only.
- Almost all LLM studies measure uptake of false content (answers, beliefs), not framing of later, unrelated events. The schema-relevant mechanism (a frame carried from earlier context to a later event) has zero direct measurements.
- LLM results mix model eras (GPT-3, 2023 models, Llama-2) with 2025 models. Modern frontier models are underrepresented, and the ranges (4%-63%, 20%-78%) are model-specific.
- Persuasion studies (Salvi, Hackenburg) are on political attitude shift in people, not on LLM agents being manipulated. They bear on the threat, not the defence.
- Defence evidence: spotlighting is for instruction injection; Pan 2023 voting costs linear tokens. No defence has been tested at equal tokens on framing.

## Seen only in snippets or not opened
- Costello, Pennycook, Rand 2024 (403; "about 20%, two months" is from memory/abstract-level, in three lines a25, b14, c24).
- Prochaska 2023 (a06; PDF refused), Goldstein 2023 and 2024 (a26, b30, b31), Green and Brock (a27), Lewandowsky 2012 (a28), Walter and Murphy 2018 (b32), Johnson and Seifert (a11), Greshake 2023 (c23), Weick/Klein/Hochschild/Kapferer (described via Prochaska only), Bad News preprint (abstract only), Pennycook 2021 numbers, Turpin and Shi details.
- Xie 2024 exact shares (a13 values were from the paper but c19 says only in Figure 2); not re-verified here.

## GAPS (most decision-relevant first)
1. Does a frame planted earlier in an LLM's context shift how it reads a later, unrelated ambiguous event (deep-story priming), and how large is the effect for current frontier models? Nothing measures this.
2. Does an S1 step that strips or marks source and framing (provenance tags, neutral restatement of events before reasoning) reduce framing and injection effects at equal tokens, versus plain prompting and best-of-N voting?
3. Which cheap defence has the best effect per token on coherent-false context: voting over evidence subsets (Pan), prior-first comparison (ClashEval-style), context-faithful narrator reframing, or an accuracy prompt? No head-to-head exists.
4. How do 2025-2026 frontier models score on Farm (multi-turn belief erosion), ClashEval and PoisonedRAG-style tests? The numbers we hold are mostly from 2023 models.
5. Is there a human experiment that tests deep-story or schema priming on interpretation of later ambiguous events (narrative transportation, frame priming, continued-influence with story context)? Search the framing and schema priming literature (Green and Brock 2000, Johnson and Seifert 1994) and read the actual figures.
6. Does explicit plausibility-versus-accuracy separation (ask "is this plausible" and "is this verified" as two checks) reduce uptake of coherent fakes in LLMs?
7. Do models' own reasoning traces ever expose the planted frame (Turpin: no)? Can a separate auditor pass detect frame carry-over at low token cost?
8. What does Costello 2024 report exactly (N, effect, durability, which beliefs), and does the mechanism (tailored counter-evidence) work on an LLM that holds a planted frame?
9. Does repair work: after a planted frame is detected, does a retraction plus replacement explanation remove its influence in LLMs the way it does in people (Chan; Johnson and Seifert)?
10. What does Prochaska 2024 lack in measurement (inter-coder agreement, sampling bias) and have later papers (Starbird group, 2025-2026) quantified deep-story effects or replicated them on other events?


## Gap search results
Sources are listed by evidence id in evidence_d.jsonl. Search tools were rate-limited (arXiv search, Semantic Scholar 429, OpenAlex partial).

1. Planted frame shifts later reading in frontier LLMs: STILL OPEN. Nearest: Lam 2023 (d10, pronoun priming, 2023 models, syntactic only) and Kelly 2025 (d06, humans, d=0.26-0.49).
2. Frame-stripping S1 at equal tokens: OPEN. Related: Germani and Spitale (d09) show a blind condition is a measurable control; Prochaska 2026 (d19) gives frame slots (Actor, Object, Action) to strip.
3. Best cheap defence: PART-CLOSED. Astute RAG (d12) is best on cost; forewarning (d18) beats generated prebunks; narrator reframing (d14). Still no head-to-head on coherent frames (K20, contested).
4. 2025-2026 frontier numbers: PART-CLOSED. SYCON 17 LLMs (d14), SycEval (d15), Costello 2026 with Claude Opus 4.6, GPT-5.2, Gemini 3 Pro (d04), Beyond Belief with Gemini-3.6-Flash (d18). Farm, ClashEval and PoisonedRAG on frontier models not found.
5. Human deep-story or schema priming: PART-CLOSED. Kelly 2025 (d06) is the nearest human experiment; COVID continued-influence (d07). Green and Brock, Johnson and Seifert not opened.
6. Plausible-versus-verified split: OPEN, with indirect support. Rating-first changes behaviour (d18); credibility and sharing scores overlap (d23); evaluators collapse criteria into fluency (d22). No direct test.
7. Traces expose the frame: CLOSED as negative. Reasoning models verbalise used hints 25% (Claude 3.7) and 39% (R1) (d17). Separate auditor pass at low token cost: still untested.
8. Costello 2024: CLOSED (d01, d02, but d01 and d02 were read in the earlier run, not re-opened). Study 1 N=1,055, d=1.15, 21.4% fall, no decay at 2 months; Study 2 N=2,286, d=0.79. Reverse (bunking) in d03.
9. Repair after a planted frame: PART-CLOSED for people (d05 debrief; d07 negative frames resist). Not tested on LLMs.
10. Prochaska 2024 measurement and follow-ups: PART-CLOSED. 2026 tropes paper (d19) adds 2 coders per rumour and calibration but no kappa seen; LLM summaries used. Deep Storytelling (d20) and evidence-frame (d21) are same-group. No independent replication.

Status changes: K15 raised to established (2 sources, d17). K17 rewritten with verified numbers, stays single-source. New claims K18-K22.
