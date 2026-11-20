# A16.06 Gesture and thinking: critique (cross-check)

## Re-checked numbers (this session, from primary abstracts and APIs)
1. Kisa, Goldin-Meadow, Casasanto 2021 (b08): CONFIRMED. 7,969 phrases, 2,075 disfluencies, no difference for any content category. Abstract concludes no reliable evidence that preventing gesture impairs speaking.
2. Dargue, Sweller, Jones 2019 (b01-b07): CONFIRMED 83 independent samples, moderate benefit, production larger than observation. The abstract gives no numeric d; d .61, .91, .54 rest on the earlier full-text read. Correction: the journal DOI is 10.1037/bul0000202 (PubMed 31219263). Scope correction: outcome is comprehension of verbal information, not problem solving.
3. Wu et al. 2024 VoT (c20): CONFIRMED in abstract (NeurIPS 2024, VoT beats MLLMs on three 2D grid tasks). Table numbers not re-read.
4. Li et al. 2025 MVoT (c22): CONFIRMED qualitatively (robust gains where CoT fails). The "over 90%" and "+7%" figures were not re-read.
5. Hu et al. 2024 Sketchpad (c23): CONFIRMED exactly: +12.7% math, +8.6% vision, V*Bench 80.3%, BLINK spatial 83.9%, correspondence 80.8%.
6. EcoG-Bench (b23, b24): CONFIRMED 811 clips, human 96.9%, Gemini-3-Pro 17.0%, 17.0 to 42.9% with timestamped frames and verified ASR.
7. Pouw et al. 2020 Hanoi (a16): paper exists (Psychological Research, Crossref confirmed). Internal check found a flaw: 4-disc groups sum 19+18+35 = 72, but "73 analysed" is stated, so one participant is unaccounted for. Probably a 3-disc-only or exclusion difference; unresolved. The headline paper title says the benefit is for lower visual working memory, so the pooled times understate the conditional claim.
8. a17 manipulation check: partial eta2 arithmetic is plausible; not re-derived.
9. a15 Aldugom 2020 and b10 Cook 2012: not re-opened this pass. Treat as read-once.
10. b14/b15 Kersey 2024: not re-opened this pass.

No number was found wrong. One correction (DOI), one scope correction, one unresolved count mismatch.

## Contradictions between sources
- Lexical retrieval hypothesis: older studies say preventing gesture raises disfluency; Kisa 2021 (large, preregistered style conceptual replication) finds nothing. Status contested; it concerns speech, not problem solving.
- Gesture benefit on thinking vs on speech: strong for spatial and math tasks, absent for word finding. The "gesture helps thinking" claim should be limited to spatial, load-heavy, learning tasks.
- Creativity: encouraged iconic gestures gave no clear gain on the Alternative Uses Task (b21).
- Pouw 2014 and Wheeler 2013 disagree on how strongly gestures count as part of cognition; evidence cannot separate covert neural from gesture-realised cognition.

## Weak spots
- Most founding experiments (Goldin-Meadow 2001, Chu and Kita 2011, Alibali 2011) were read only through reviews; group means are missing (a02, a06, a07, a08, b18).
- Dargue is heterogeneous (I2 69%), some subgroups have 2 samples (metaphoric, beat, adolescent).
- Prevention designs confound gesture with extra effort of inhibiting; Hostetter and Alibali note both imposed and self inhibition gave the effect, which helps but does not remove it.
- Several LLM gesture papers are interface or generation work and say nothing about thinking.
- The closest AI analogues (VoT, MVoT, Sketchpad) externalise visual state; they are analogy, not tests of the gesture claim. Token budgets are not matched in those papers.

## Only seen in snippets
b18 (Chu and Kita 2011 abstract only), b27 and b28 (search sweeps; Semantic Scholar and OpenAlex rate limited), a21 JEGAL tables (garbled extraction).

## GAPS
1. Does externalising state (writing a grid, table or sketch) beat silent chain of thought at EQUAL token budget on spatial tasks? VoT, MVoT and Sketchpad do not match tokens.
2. Is the externalisation benefit larger for weaker or lower-capacity models, mirroring the lower visual working memory result in Pouw 2020?
3. Why does the Pouw 2020 4-disc count sum to 72 not 73, and what are the per-group results for low versus high visual working memory?
4. Raw numbers for Goldin-Meadow 2001 and Chu and Kita 2011: effect sizes and group means for the founding load and spatial studies.
5. Are there preregistered replications of gesture-prevention effects on spatial problem solving (gear, mental rotation), as Kisa did for speech?
6. When does externalised visual state hurt (VoT on ring navigation, state accuracy 24-26%)? Which task features predict failure?
7. Does an agent benefit from choosing when to externalise (cost-shifting, gestures fade with expertise) versus always or never externalising?
8. Do any 2025-2026 papers test LLMs on embodied-gesture-analogue reasoning, such as finger counting or action-simulated tasks, rather than gesture recognition?
9. Gesture and creativity: is the null AUT result robust (b21), and does any generation task benefit from externalisation?

## Gap search results (evidence_d.jsonl, d01 to d23)

Status per gap: CLOSED, PARTLY CLOSED, or OPEN.

1. Equal-token comparison: OPEN. No token-matched study found. Rajpal 2026 (d14) shows the grid route used 10x to 63x the text tokens (for example GPT-5.1 StepGame 249 vs 15,727). MentisOculi (d18) shows 13x more reasoning tokens gave no gain and self-generated imagery gave no gain. Optical Reasoning (d22) reports a token-efficiency gain but for compressing rationales, not spatial state. The needed test is text best-of-N at the same cost.
2. Larger benefit for weaker models: PARTLY CLOSED, answer is mostly no. StepGame pruned-grid gains: LLaMA3.1-8B +13.5, Qwen3-8B +25.6, Qwen3-14B +16.4, Qwen3-32B +17.1, LLaMA3.1-70B +42.0, GPT-5.1 +13.8 (d13). Not monotone with capacity. VoT helped weak models unreliably (d17). The weakest model had a small gain because its grid construction is poor.
3. Pouw 2020 count: CLOSED. The paper is Eielts, Pouw et al. 2020. Totals are 73 (3-disc: 27/11/35) and 72 (4-disc: 19/18/35); the authors report N=72 on the 4-disc table. Groups were defined per task. Per-capacity results: benefit only for roughly the bottom 26.4% (instructed) or 33.3% (spontaneous) of visual working memory, and a slowdown for the top 1.9 to 2.8% (d01, d02). The source label in a16/a17 was wrong and is now flagged (K27).
4. Raw numbers for Goldin-Meadow 2001 and Chu and Kita 2011: MOSTLY CLOSED. Test statistics, N and effect sizes recorded (d03 to d07). Group means for recall and mental rotation errors exist only in figures and were not extracted.
5. Preregistered replications of gesture prevention on spatial problem solving: OPEN. None found in six searches and API checks. What exists: Alibali 2011 shows no accuracy difference (d08, d09), Chu and Kita 2011 shows allowed equals prohibited (d06), Wassenburg 2018 fails to reproduce the interference effect (d10). So the prevention claim K05 was downgraded to contested. This is a correction to the earlier file.
6. When externalised state hurts: PARTLY CLOSED. Features found: the task reduces to direct symbolic computation (ring navigation, CoT 52.5 vs VoT 49.5, N=200); low construction accuracy (self-drawn ASCII correct 12 to 50% of the time and below text-only, d15); long horizons with cascading errors (d23); models that cannot use even correct oracle images (d18); counting-heavy multi-object tasks (Gather, d16). CORRECTION: the 24 to 26% figure belongs to navigation and tiling state accuracy, not to ring navigation (d17).
7. Choosing when to externalise: PARTLY CLOSED. Adaptive switching gives +0.4 to +1.6 accuracy and mixed token savings (d14). SwimBird learns text vs visual mode and beats fixed baselines (d19). No LLM test of cost-shifting with practice.
8. LLM tests of embodied-gesture analogues (finger counting, action simulation): OPEN, negative result. Only CFG-Bench (video action description, d21) and sensory-norm studies turned up. They do not test the claim.
9. Creativity null: PARTLY CLOSED. Null is stable in adults (N=151, d12; b21). Children show a fluency gain when encouraged (d=.98, N=54) but no originality or flexibility gain, and restriction did not significantly lower fluency (d11). PainterBench (d20) has an agentic drawing task but no draw-versus-no-draw comparison. No generation task showing a benefit from externalisation was found.

New or changed claims: K05 downgraded to contested and reworded; K06 reattributed with counts; K11 and K12 extended; K13 extended; K17 made contested (not token matched, MentisOculi null); K18 rewritten; K21 to K27 added.

Limits of this pass: Chu and Kita was read from the accepted manuscript, not the journal copy. Wassenburg 2018 and the Optical Reasoning, STAR and Frith and Miller papers were read only in part (abstract and first sections). Semantic Scholar and OpenAlex were rate limited, so search was by arXiv API and 8 WebSearch calls or fewer.
