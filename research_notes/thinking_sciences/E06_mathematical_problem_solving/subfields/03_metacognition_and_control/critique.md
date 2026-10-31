# Critique: E06.03 Metacognition and control (cross-check)

## Corrections made (sources re-opened from arXiv PDFs this session)

Confirmed: Huang 2024 table (GPT-3.5 GSM8K 75.9 / 75.1 / 74.7; CSQA 75.8 / 38.1 / 41.8; GPT-4 GSM8K 95.5 / 91.5 / 89.0; oracle 84.3 / 89.7 / 29.0). Chen 2025 (1,953% more tokens; "in more than 92% of cases" first round correct). Wang 2025 (225% / 418%; UT 58.2 and 65.4 on MATH500-Hard; AIME24 QwQ 38.3 to 44.1 with TIP). Tyen 2024 (GPT-4 52.87; GPT-3.5 10.10; 2186 traces, 300 sampled for annotation). Zhang 2025 (24% token cut; 88.2% at threshold 0.85). Yao 2023 (4% / 45% / 74%). Tsui 2026 (64.5%, 5,306 traces, 76.0%, 89.3% for "Wait"). Gandhi 2025 (Countdown, Qwen vs Llama).

Corrections:
1. **b16 (s1) mislabels the benchmark.** The row "26.7, 30.0, 33.3, 36.7" is AIME **2025**, not AIME24 (s1 paper, Table 5). Correct AIME24 for s1-32B: 50.0 (no forcing), 53.3 (Wait x1), 53.3 (x2), 56.7 (x4). For s1.1, AIME24 is 56.7 flat across forcing, and AIME25 is 50.0 flat. Claim K13 uses the corrected numbers. c18 (50 to 57) is right.
2. **b25 / a18 "11.6% over CoT" is 11.6 absolute points, not relative.** Didolkar: plain CoT 42.2, complex CoT 50.30, skill-based 53.88. Gain vs complex CoT is 3.6 points (c01 right; b25 says "3.5 percent", abstract rounding). Do not quote 11.6 as a gain over a fair baseline; the fair comparison is +3.6 over complex CoT.
3. a18 says about 500 skill names for GSM8K and 5,000 for MATH; c01 says 117 clusters on MATH. Both fit (fine names then clusters) but quote them separately.
4. Duplicates: a16 = b07 = c03/c04 (Huang), a20 = b11 = c14 (Chen), a21 = b12 = c11-13 (Wang), a19 = a25 = b21 (Gandhi), a15 = b09 = c08 (Kamoi), a14 = b01 (Lester). Counted once each for independence.

## Contradictions and tensions between sources

- Self-correction: Huang and Kamoi say intrinsic correction hurts, yet s1 "Wait" and Tsui's "Wait" (89.3% blind-spot cut) say a trigger word helps. Resolution: Tsui tests non-reasoning models with injected errors; s1 gains are small, flatten, and on s1.1 are zero; Ghosal attributes the gain to variance. Status: contested.
- Overthinking (Chen) vs underthinking (Wang) point in opposite directions. Both can hold: too much on easy items, too many switches on hard ones. The same stop rule cannot fix both; the trigger has to depend on difficulty.
- Shojaee "collapse" is partly an artifact (Lawsen), so high-complexity give-up evidence is unreliable.
- Gandhi (behaviours cause RL gains) vs Liu / Essential AI (reflection phrases do not track accuracy). Behaviours that are present are not the same as phrases that are present.

## Weak spots

- The human core (Schoenfeld 1981-85, Garofalo and Lester) is mostly qualitative and small-N. The only hard numbers are Lester 1989 (modest, ceiling effect) and Schoenfeld and Herrmann (N=19). The "7 of 12 sessions" wild-goose-chase figure comes from a 1983 paper, and the 1985 book was never opened (a10, b05). No replication of the wild-goose-chase rate found.
- Almost no LLM study tests Schoenfeld's specific control rules (three loci, progress check, "too complicated" cutoff). The links are analogies by us.
- Most LLM evidence is on non-current models (GPT-3.5, GPT-4, QwQ-Preview, R1-distill); one 2026 study.
- Underthinking has a single source (Wang), including its own mitigation. Same for ToT, Tsui and Didolkar.
- Probes (Zhang) need hidden states; not usable on a closed-API agent.

## Seen only in snippets or not opened

a10, a13, a23, a24 (Schoenfeld book, Garofalo and Lester 1985, Flavell, Lester 1994), b05, b06 (meta-analyses, no numbers), b26, b27. Treat as unverified. c22 (AutoMeco), c24 (CRITIC), c25 abstract-level, no numbers. b04 abstract only.

## GAPS

1. Does a hand-written S6 stall rule (Reflexion-style: repeated step or step cap, plus no new progress marker) beat no trigger at equal tokens on competition maths with a current model? No paper measures this directly.
2. Is a progress check at fixed intervals better than a trigger on stall, for a current reasoning model on MATH/AIME-level items (Schoenfeld locus 3 vs locus 1)?
3. Do overthinking (Chen) and underthinking (Wang) results hold for current frontier models (2026), and does an easy/hard difficulty gate on stop vs switch rules work?
4. Does "role reframe" (presenting own earlier step as another party's) close the self-correction blind spot for reasoning-capable current models on maths, not only injected errors?
5. What is the best error-location monitor available without ground truth (separate judge, independent sample disagreement, tool check)? Compare F1 and cost against ProcessBench numbers for current models.
6. What do Schoenfeld's original coded rates actually say (episode types, share of sessions with no control event)? Needs the 1985 book or the 1992 chapter opened; the 7 of 12 figure needs a primary check.
7. How large is the human training effect of metacognitive instruction in later meta-analyses (Dignath and Buettner 2008, Hattie-style) for maths specifically? Numbers not yet recorded.
8. Is extra "Wait"-style rechecking worth more than the same tokens in parallel samples with voting, at equal tokens, on current models (s1 vs Ghosal vs Hassid disagree in setting)?
9. Does prompted abandon-with-reason (state why the line failed, record in memory) reduce repeated dead ends, measured on a multi-attempt maths task?
10. Calibration as a control signal: does verbalised confidence from a current model predict when to stop or switch well enough (Kadavath was 2022, pre-reasoning models)?

## Gap search results

Search tools were limited: WebSearch quota was used up, and arXiv, Semantic Scholar and OpenAlex search APIs were rate-limited. Sources were reached by known arXiv ids and one publisher page. 22 evidence lines are in `evidence_d.jsonl` (d01 to d22); claims K22 to K28 are new and K03, K05, K06, K07, K08, K10, K13, K18, K19, K20 were extended.

1. **Stall rule vs no trigger at equal tokens: still open, partly narrowed.** No paper tests a repeated-step or step-cap rule on maths. Nearest evidence: DEER (trial-answer confidence at each Wait; AIME24 41.7 to 49.2 with 13,765 to 9,839 tokens on R1-Distill-7B) and DeepConf (43% to 79% token savings vs majority, a few small drops). Both use open 2025 models and confidence, not a stall rule. Reflexion's rule (K18) was tested only outside maths (d20). K23.
2. **Fixed-interval check vs stall trigger: open.** Certaindex (probe every 64 tokens) and answer convergence work as stop rules (d12, d14), but nobody compares them with a stall-triggered check. Both miss a stable wrong answer. K22.
3. **Overthinking and underthinking in 2026 frontier models: open.** No 2026 frontier test found. Illusion of Thinking (v3, Nov 2025) shows difficulty regimes on Claude 3.7 Thinking, R1, o3-mini in puzzles (d18); AdaptThink shows NoThinking matches thinking on easy MATH levels (d19). A hand-written easy/hard gate is untested. K27.
4. **Role reframe on current models: mostly closed.** Tsui v3 (d01, d02): reasoning models have a small or negative blind spot, so reframing adds little for them; closed non-reasoning Sonnet 4 still shows 41.4%; on natural errors only 4.3% to 10.8% are rescued. Panickssery (d03) says models recognise their own text (GPT-4 73.5%), which weakens a disguise. Verdict: weak lever. K07, K28.
5. **Best error-location monitor: partly closed.** Numbers now side by side (d05, d06, d07): ProcessBench F1 o1-mini 87.9, QwQ 71.5, GPT-4o 61.9; DeltaBench best critic 40.8; ThinkPRM 87.3/85.7 vs plain judge 72.8/67.8 with up to 55% invalid output for small judges. Not compared: disagreement between independent samples and tool checks, and no cost per call. K25.
6. **Schoenfeld coded rates: open.** Primary text (1985 book, 1992 chapter) could not be fetched (Berkeley PDF returned 404; no free copy found). The "7 of 12 sessions" figure remains unverified.
7. **Human training effect: partly closed.** Dignath and Buettner 2008 (abstract only): 84 studies, 357 effects, average d 0.69, higher in maths than reading (d21). The metacognition-only and maths-only effect sizes were not found. Later meta-analyses (Donker 2014, Hattie-style tables) not reached. K20.
8. **Wait vs parallel at equal tokens: contested, narrowed.** For small open reasoning models, parallel plus vote beats Wait (d15, d16) and removing Wait costs little (d22). Cause of the s1 gap stays setting differences (model size, benchmark, cap). No 2026 frontier test. K26.
9. **Abandon with reason in memory on a multi-attempt maths task: open.** Only non-maths evidence: Reflexion's written reflection adds 8 points over plain episodic memory on HotPotQA with ground-truth context (d20). K18.
10. **Verbalised confidence as a control signal: partly closed.** Yoon (d10) shows reasoning models are better calibrated, increasingly so along the chain; DeepConf (d11) shows token confidence works as an abandon signal but fails on confident wrong traces. No test of verbalised confidence as a stop/switch trigger. K24.

Not read in full: Kamoi survey (abstract and introduction only), answer convergence and NoWait (abstract and figures), SETS maths rows (table garbled), Dignath (abstract page only). Corrections from the cross-checker (b16, b25/a18) were already applied in K13 and K17 text; they were not re-checked.
