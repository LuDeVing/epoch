# A05.01 Worked-example research: cross-check critique

Cross-checker pass over evidence_a, evidence_b, evidence_c (77 lines). Source texts re-opened from D:/research_scratch/A05.01 (pdftotext). 23 claims in claims.jsonl (K01-K23).

## Numbers re-opened and confirmed (10 plus)
1. Barbieri et al. 2023 (journal page text): 43 articles, 55 studies, 181 effect sizes, RVE g=0.48, p=0.01; self-explanation prompts significantly moderated the effect; "may not be a fruitful design modification". Confirmed. The sign (negative) is stated in the abstract text, so b01 (opened:false) is now backed by a12.
2. Reed and Bolstad 1991 Exp 1: 65 students, F(2,62)=6.01 p<.01, m=.96, r=.65, g=.45; Exp 2: 7/32/38 percent and F(5,168)=10.96. Confirmed. The 38 (simple) versus 65 or 70 (simple plus complex) comparison in K08 rests on a06; the 65 and 70 values were not re-read, only the 7, 32, 38 line.
3. Nathan, Mertz and Ryan 1994: F(1,25)=5.9, 6.76, 7.1. Confirmed.
4. Wang et al. 2023 CoT: standard 15.4, CoT 48.5, invalid reasoning 39.5, no coherence 23.1, no relevance 11.0, no relevance of bridging objects 27.5. Confirmed from the table. Note b16 and b17 and c07 and c24 are one paper, so they count as one source.
5. Cheng et al.: GSM8K 8-shot 95.75, zero-shot 91.58, zero-shot-fix 95.83; MATH 81.30 vs 81.64; base 90.52/84.69/90.27; LSAT-LR few-shot 41.55 vs zero-shot 84.65. Confirmed. b20, c06, c20 are one paper (versions 2025 and 2026); year labels differ between lines but it is the same arXiv 2506.14641.
6. Wang 2025 Harm to Help: single-demo AIME25 drops 6-16, three-shot up to 35, GPQA 1-5. Confirmed. The abstract says GPT-4.1 AIME25 "from 34.0 to 48.0 (+14.0)": an absolute-points gain, not a percent; evidence c04/c05 abstract wording "+14.0%" should be read as points.
7. Agent Workflow Memory: 51.1 percent relative, 12.0 points, 35.5 success, 24.6 percent Mind2Web, 8.9 to 14.0 points. Confirmed. CORRECTION: the paper itself is inconsistent on the margin over human-written workflows, 7.9 percent in the intro and 7.6 percent in the results text. b24 says 7.6, c14 says 7.9; both appear in the paper.
8. Chen et al. 2023: 0-7 percent drop from 7-8 demos to one random demo; 83 versus 60 percent; 12.5 percent. Confirmed.
9. Alazraki et al. 2025: 85 and 88 percent, +4.4/+2.2, +1.6/+1.9, +5.6/+6.2. Confirmed.
10. Voyager: Table 1 diamond tool 102 iterations (1/3); baselines 0/3; w/o library iron 29 +- 11, diamond N/A (0/3); 3.3x items, 2.3x distance, 15.3x faster. CORRECTION: the 15.3x speedup is for the WOODEN tool, not the deepest tier. CORRECTION: c26 says the library shows no benefit early and is silent on generalisation; Table 2 (zero-shot unseen tasks, 50-iteration cap) shows the library helps clearly: diamond pickaxe 19 +- 3 (3/3) versus 36 (2/3) without library; golden sword 18 vs 30; lava bucket 21 vs 27; compass 18 vs 26. c12 and c26 should cite this. Also AutoGPT given Voyager's library gets 1/3, 1/3, 0/3, 2/3, so the library does not rescue a weak loop alone.
11. Miller-Cotto and Medrano 2026: N=114, g fading 1.08, fading+SE .93, WE+SE .32, BAU .24, beta .60 p=.03. Confirmed. Caveat already in b10: g is within-condition pre/post.

No correction needed to the Wang, Cheng or Barbieri numbers. Corrections above are to Voyager (15.3x scope, Table 2 omitted), AWM (7.6 vs 7.9), and the unit on I2S (+14.0 points).

## Contradictions between sources
- Self-explanation: human training studies (Chi 1989, Bielaczyc 1995, Renkl 1998, about 2 SD) versus maths meta-analysis and 2026 trial (no benefit or negative). LLM side: I2S and LEAP help only for models strong enough. Status contested (K10, K11).
- Partial versus full examples: Paas 1992 and Stark 1999 (partial equal or better) versus Manson and Ayres 2019 (full better for novices who failed items). Contested (K13).
- Few versus many: Chen 2023, Wang 2025, De Wynter say few or one; Bertsch 2025 and Agarwal 2024 say many help for classification and MATH until about 125. The split follows task type and model type (K08, K09).
- Moderators unstable across analysis versions: poster found none significant, journal version found self-explanation and example type significant (b02 vs b01). A moderator reported once should not be trusted.
- Fading: Miller-Cotto 2026 supports; Gonzaga 2026 (N=27 TAs) finds no load advantage; Atkinson 2003 far transfer needs prompts. Contested (K12).
- Is a worked example plain learning or efficiency? McLaren: 21 percent less time, no learning gain; Schwonke: both. K21 treats it as established that format/efficiency explains part of the effect.

## Weak spots
- The founding studies were never read. Sweller and Cooper 1985 (a20), Paas 1992 (a21), Quilici and Mayer 1996 (a26), Nievelstein 2013 (a27), Zhu and Simon 1987 (a28), Atkinson 2003 (a23), Chandler 2001 (a24), Renkl and Atkinson 2003 (a22) are all opened:false. The task asked for founding numbers with N; we have none for them. The "three examples no better than one" and "partly completed as good as full" parts of the subfield focus rest on Wikipedia (a25, b07) and the Atkinson review.
- Many a-line numbers are second-hand through Atkinson et al. 2000 (a03, a04, a07, a09, a10, a11, a18, a19): no N, no effect sizes.
- Duplicate counting risk: a12/b01 and a13/b02 are one meta-analysis in two versions; b20/c06/c20 one paper; b16/b17/c07/c24 one paper; b24/c14 one paper; c10/c22 one paper. independent_sources in claims counts papers, not lines.
- b25 is the agent's own synthesis, not a source; it is not cited as evidence in claims.
- Several LLM results use old models (text-davinci-002, code-davinci-002, GPT-3.5) and may not hold for strong current models; the two results on strong models (Cheng, Wang 2025) pull the other way.
- None of the LLM studies is a human-style worked-example experiment (study versus solve, matched tokens). No study measures a stored-solution library against a stored-skeleton library at equal tokens.
- Small samples in the 2026 human studies (b12, b13, b14, b10 cells of 21-33); Barbieri heterogeneity I2 about 94 percent means the 0.48 mean says little about any one class.
- Seen only in snippets or abstracts: Bastani 2025 (c18, abstract page), Barbieri tables, Manson and Ayres means (garbled), Madaan and Mishra per-condition numbers.

## GAPS
1. What are the real numbers in Sweller and Cooper 1985 (N, time ratio, error rates, near versus far transfer), and did Cooper and Sweller 1987 or later direct replications hold at that size? This anchors the whole "studying beats solving" claim.
2. Does a retrieved solved case help a strong current LLM on hard, non-saturated items (not GSM8K) at equal tokens, once the parser is fixed and a format-only exemplar arm is included? Cheng 2026 and Wang 2025 say no or harmful; Voyager and AWM say yes. What separates them: model type, task depth, or example abstraction?
3. Is the best library entry a full solution, a subgoal skeleton, an abstract insight (I2S, Buffer of Thoughts), or a wrong/right pair (Alazraki)? No head-to-head at equal tokens exists.
4. What is the cross-over point for a given class (expertise reversal) in an agent: how many unaided successes before the example should stop being shown, and does gating on zero-shot success recover the benefit?
5. How many examples and which kind of difference between them (Reed and Bolstad contrast, Quilici and Mayer no gain at three, Chen one correct beats eight)? Is contrast between examples or retrieval match the driver?
6. Does fading (backward step removal) help an LLM, or is it only a human load-management device? Is there any LLM test of faded or completion examples?
7. Does a self-explanation step (goal and reason per step) help at the agent's strength, and at which strength does it reverse (LEAP Llama-2 versus GPT-4)? Is the human negative moderator in Barbieri an artifact of prompt quality?
8. How fast does library quality degrade when wrong solutions enter (AWM warns, no slope is measured)? What is the verification threshold before storing?
9. Does the effect carry to ill-structured domains in humans with primary numbers (Nievelstein 2013, law; efficiency versus learning)? This decides whether the library should cover non-algorithmic tasks.
10. How large is the reverse effect for low element interactivity (Chen, Kalyuga, Sweller 2015-2017 numbers) and can the agent classify an item as low interactivity cheaply enough to skip the example?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d20). Claims K02, K03, K08, K10, K13, K16, K17, K18, K22, K23 were updated; K24 to K29 are new. Sources read as PDF text: Sweller and Cooper 1985, SkillEvolBench, ThinkRetrieve, Compliance Trap, Xu and Wu 2026. Others were read through a fetch summarizer and are flagged in the limits field. Paywalled and not opened: Cooper and Sweller 1987, Paas 1992, Chen Kalyuga Sweller 2015, Tetzlaff 2025 (snippets only), Quilici and Mayer 1996.

1. Founding numbers (gap 1): PARTLY CLOSED. Sweller and Cooper 1985 was read in full. Exps 2-5, N=20, 22, 40, 24. Learning time ratio 5.8 in Exp 3 (185.5 s vs 32.0 s). Test errors 1.64 vs 0.18 (Exp 3). Exp 2 did not show a significant test gain. No far-transfer gain in Exps 4 and 5. The earlier K23 text about geometry and kinematics is not from this paper. Still open: Cooper and Sweller 1987 numbers, Paas 1992, Quilici and Mayer (three examples no better than one), and any independent direct replication.
2. Retrieved case on hard items with a strong model (gap 2): PARTLY CLOSED. The split is model strength and placement. Generic or static examples do nothing for strong models (ThinkRetrieve static ICL 62.2 vs 63.3 at 4B; WebArena retrieval -1.9 and +1.7 pp; Dynamic Cheatsheet R1 and o1 minimal). Relevance-matched in-trace retrieval helps small reasoning models (+13.4 at 1.7B, about +2 at 4B and 8B). Curated or verified skills help agents (+16.3 pp). Self-written skills do not. Still open: a test on a current frontier model with a format-only arm at equal tokens.
3. Entry form (gap 3): NARROWED, NOT CLOSED. Xu and Wu: abstraction level and one worked example are second-order (+0.7 to +1.3 pp, intervals cross zero). Raw versus distilled conflicts: Dynamic Cheatsheet favours distilled (50.0 vs 26.7), SkillEvolBench favours retrieved raw trajectories. No full-solution vs skeleton vs insight vs pair test at equal tokens exists.
4. Expertise reversal cross-over for an agent (gap 4): OPEN. Human anchor now exists (Tetzlaff meta-analysis d=0.505 and -0.428, snippets only). Agent data point both ways: SkillsBench gains did not shrink for stronger models; memory damage grew with baseline. No test of gating on zero-shot success.
5. How many and what difference (gap 5): OPEN. Diversity paper shows diversity helps on harder non-reasoning tasks and is flat on GSM8K. No matched-contrast test.
6. Fading and completion for an LLM (gap 6): OPEN for fading. A partial-solution prefix helps a weaker model monotonically (77.5 to 94.1 on GSM8K). Paas 1992 abstract puts the full worked arm ahead of completion.
7. Self-explanation at strength (gap 7): OPEN. Only an LLM-judge pilot (N=8) was found. No new test of whether the explainer gains.
8. Degradation with wrong entries (gap 8): PARTLY CLOSED. Add-all loses 3.7 to 12.1 points against a fixed memory, strict verification gains 4 to 22 (GPT-4o-mini, four tasks). Wrong hints cost 2.5 times what right ones gain. Conflicting memory costs up to 26 points and the damage rises with baseline skill. Still missing: accuracy as a function of percent wrong, and a verification threshold.
9. Ill-structured domains (gap 9): STILL THIN. Nievelstein 2013 abstract confirms worked example effect for novice and advanced law students with no reversal; no N or effect sizes obtained.
10. Low element interactivity (gap 10): OPEN on size. Direction confirmed in the 2018 review; no statistics retrieved from the 2015-2017 papers; no agent-side classifier.

Corrections to earlier lines: the claim that Sweller and Cooper 1985 showed a transfer benefit should be read as near transfer only. Cooper and Sweller 1987 abstract does claim transfer gains, but its numbers are unread.
