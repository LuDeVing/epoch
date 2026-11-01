# Critique: Einstellung effect (E16.08), cross-check

## Numbers re-opened (full text in D:/research_scratch/E16.08)
1. Bilalic et al. 2008 (draft text): odds factor 3.67 per 100 Elo (Exp 1), 1.82 (Exp 2); 92/69/35% actual vs 97/89/73% predicted; 86/74/59% predicted in Exp 1; Exp 2 comparison t(44)=2.16, p=.036, d=.65; 79 s (SD 25) vs 148 s (SD 90). CONFIRMED. Caveat: file is the in-press draft, not the printed Cognition text.
2. Sheridan and Reingold 2013 (PMC3790829): 8 of 17 experts and 8 of 17 novices chose Ba7; first fixation 407 vs 719 ms, p<.01. CONFIRMED.
3. Binz and Schulz: N=310, 0.83 vs 0.00, chi2=218.02; DBB 87/153, 0.57 vs 0.83, chi2=24.16. CONFIRMED. The text prints chi2=24.16 for both the C1/C2 and C3/C4 DBB comparisons; the second is probably a copy error in the paper. Do not quote the C3/C4 statistic.
4. Naeini et al. (Table 5): CORRECTION. Lines c01 and c02 gave GPT-4 10-shot as 6 walls (239 groups) and GPT-3.5 10-shot as 0/10/415. Those are the GPT-4 0-shot row and the GPT-3.5 3-shot row (PDF layout scrambled). Right values: GPT-4 0-shot 6/59/471 walls (orig/randomised/WordNet), 10-shot 3/55/378; GPT-3.5 0-shot 0/5/337, 10-shot 2/17/428. New finding: for GPT-4 more shots lowered the no-decoy score (471 to 378). Claim K17 uses the corrected values.
5. Haq et al.: EM table confirmed (GPT-4o 0.33/0.66/0.66/0.83; Llama-70B 0/0.16/0/0.66; Llama-8B 0.16/0/0/0; CoT rows confirmed). Values are k/6, so one item is 0.17.
6. Shidara 2026: 0.751 (CI .738-.763); human-miss 20/100, 36% vs 73%; Opus 55.0/25.0/20.0. CONFIRMED. Note a26 says "top 5 models 50-70%", c11 says 55-70%; the abstract figure was not rechecked.
7. Kim 2025: physicians ~66% confirmed in text; model list not rechecked in detail.
8. MedEinst: 5,383 pairs, 17 LLMs, Gemini 60.90, GPT-5 51.87, ablation 40.25/11.86/43.46 then 55.49/19.94/38.32 then 69.49/24.21/33.75 CONFIRMED. UNRESOLVED: the main table is scrambled; Qwen3-32B appears as 44.12/11.28/43.46 and as 40.25/11.86; MDAgent/DyLAN accuracy could be 29.70/32.11 or 14.93/6.51. a27 says 40.26 (typo for 40.25). Do not quote MDAgent accuracy drops until checked on a clean copy. Trap rates 40.34 and 41.69 (MDAgent, DyLAN) look right.
9. Huang et al. 2024: tables confirmed (GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GSM8K 74.7% answers retained). This paper is about self-correction, not Einstellung; used only as indirect evidence.
10. Laban 2025: 39% drop, +112% unreliability, -15% aptitude CONFIRMED. Also indirect.

## Contradictions between sources
- Experts: Bilalic finds a strong rating gradient; Sheridan and Reingold find equal choice of the Einstellung move by experts and novices (8/17 each) on problem 1, and no fixation at all on the blunder problems 2-4. Boundary: the effect needs a believable familiar move.
- Wiley: warning did not help; mindfulness training did help (Greenberg) but did not predict water-jar rigidity. The two kinds of de-fixation do not line up.
- Huang et al. 2018: Exp 1 shows an accuracy cost, Exp 2 only a time cost.
- Clinical LLM: Kim 2025 (models below physicians) vs Shidara 2026 (models above physicians). The benchmark is the same family; gap is mostly newer models.
- Multi-agent: MedEinst finds consensus raises the trap; no source here finds the opposite, but it is one paper.

## Weak spots
- Sample sizes are small in the founding chess data (n=6 to 12 per cell; specialist group n=12). Wiley Exp 2 had 5 per cell.
- The Bilalic "blocked" effect is partly confounded with problem difficulty (Exp 2 easy problem showed none).
- LLM studies: Haq has 6 items per cell, so every ratio is noise-prone. IDEAFix numbers are garbled. Naeini's decoy effect mixes a dataset change with a decoy change.
- Almost nothing tests a scaffold or de-fixation operation on an LLM at equal tokens. No LLM paper reproduces the core Luchins design (train on a method, test shortcut use) with measured rates and a control.
- Only snippets/abstracts seen: Luchins 1942 (a01, via secondary), Saariluoma 1990 (a15, via Bilalic), Lovett and Anderson 1996 (c27, unopened), Bilalic mechanism paper listed again as c28.
- The 4 independent-source count for "established" often reflects the same research group (Bilalic, Reingold, Wiley).

## GAPS
1. Does a plain LLM show the Luchins pattern (long method learned from in-context examples, then shortcut missed) with enough items, and how large is it vs a no-example control?
2. Which de-fixation operation works on an LLM at equal tokens: generic warning, forced alternative generation, relational restatement, or an external check? (Human data conflict.)
3. Does reasoning length (more tokens) reduce Einstellung in LLMs, as Binz's deliberation account predicts, or does it increase overthinking (MedEinst: 22%)?
4. Does a critic or verifier agent cut the trap rate while multi-agent voting raises it? Replicate MedEinst's contrast on a clean base.
5. Does retrieved memory (a past solved example) act as an Einstellung source for agents, and how does the harm scale with example similarity and success count?
6. Is there an observable early signal (token overlap, attention, repeated candidate) that precedes fixation, analogous to the gaze drop two trials before discovery?
7. How well do LLMs predict their own fixation (experts under-estimated it in Bilalic)? Is stated confidence lower or higher on fixation items than on controls?
8. Does the Bilalic difficulty dependence hold for LLMs: is fixation weaker on easy shortcuts and stronger on hard ones?
9. Do chess engines or chess-trained LMs show Einstellung-like misses on mate-in-N with a familiar longer line (no clean test found)?
10. What do clean reads of the MedEinst main table and the printed Cognition 2008 paper change in the numbers above?

## Gap search results

Searches: WebSearch hit its session budget after one query; arXiv, Semantic Scholar and OpenAlex returned rate-limit errors from this network. Candidate papers were found through the Hugging Face paper search and read as full text from arXiv. New evidence is in `evidence_d.jsonl` (d01 to d19, all opened except d19). New claims are E16.08-K30 to K39; K11, K18, K19 and K24 were updated.

Closed or mostly closed
- Gap 10 (MedEinst half): closed. A clean table came from the arXiv HTML version (d18). Qwen3-32B base is 40.25 / 11.86 / 43.46; MDAgent 29.70 / 10.34 / 40.34; DyLAN 32.11 / 8.11 / 41.69; ECR-Agent 69.49 / 24.21 / 33.75. K19 was rewritten with these. The earlier MDAgent/DyLAN worry is resolved: both lose 8-10 accuracy points and gain only 2-3 on trap rate.
- Gap 2 (which de-fixation step): partly closed. A generic hint raised Qwen3-32B by about 12 points on edited items with no loss on originals, but wording mattered (d07). An external or role-switched check also works (d13, Wait closes 89.3% of the blind spot). Forced alternative generation and relational restatement are still untested at equal tokens.
- Gap 6 (early signal): partly closed. Contamination ratio, with a knee near 40% (d09); first-step lock-in, -40% accuracy when wrong (d03); step-4 hidden-state similarity, AUROC 0.81 but it tracks stability, not correctness (d17). Nobody has tested these on a Luchins-style design.

Narrowed but still open
- Gap 3 (length): evidence is mixed, so K32 is marked contested. Thinking models are worse than non-thinking twins on ReasoningTrap (d06), more effort helped inside o4-mini (d08), and extra reasoning can undo a correct early answer (d14, d02). Binz's deliberation account is not supported or refuted for LLMs.
- Gap 4 (critic vs voting): the critic half has support (d05, d13, d16: coupling matters). The claim that voting raises the trap rate is not shown; in the clean MedEinst table the consensus agents did not raise it (d18).
- Gap 5 (retrieved memory as source): agent evidence is real (d11: 63-72% adoption of wrong memory, damage grows with agent strength; d10: stored abstractions 49.0% vs raw trajectories 53.5%). The dose-response by similarity and success count is still unmeasured; MemTransfer (d15) is weak.
- Gap 9 (chess): d12 shows a learned prior overriding a computed solution in Leela, but no one has tested shorter mate vs familiar longer mate. Open.

Not closed
- Gap 1 (plain LLM Luchins pattern with a no-example control): still no paper. SenseMath (d01) and ReasoningTrap (d06) are the nearest and differ in kind. K30 says so. This remains the most decision-relevant open item and needs our own run.
- Gap 7 (predicting own fixation): nothing new on fixation items. d01 shows applicability judgments say yes to everything; d16 shows confidence predicts resistance to feedback. No trap-vs-control confidence comparison exists.
- Gap 8 (difficulty dependence): untested for LLMs. SenseMath points the other way (shortcut use rises with problem size).
- Gap 10 (printed Cognition 2008 half): publisher text returned 403; only the record was confirmed (d19). Bilalic numbers still rest on the in-press draft.
