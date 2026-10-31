# Critique and cross-check: Expertise reversal and fading (A05.02)

Cross-checker pass over evidence_a.jsonl (30 lines), evidence_b.jsonl (27), evidence_c.jsonl (29). Claims are in claims.jsonl (K01 to K29).

## 1. Numbers re-opened this session

Opened the full text (arXiv PDF or journal repository) and compared with the evidence lines.

| # | Number | Source | Result |
|---|---|---|---|
| 1 | SkillsBench 33.9% to 50.5%, +16.6 pp, 87 tasks | Li et al. 2026 (arXiv 2602.12670) | Confirmed (Table 2, Finding text) |
| 2 | Self-generated skills -8.1, -11.3, -11.5 pp vs none | same, Table 6 | Confirmed. Curated gain on same 3 configs is +18.2, +19.7, +24.8 pp. |
| 3 | 13 of 87 tasks negative, worst -7.4; compact +19.0, standard +21.5, detailed +14.5, comprehensive +0.7 | same | Confirmed. Added: 1 skill +18.0, 2-3 skills +19.0, 4+ skills +10.1. |
| 4 | Worked example in skill: +0.7 and +1.3 pp, CIs cross zero, no skill 31.3 / 26.0, medium 61.3 / 44.0 | Xu and Wu 2026 (2605.31408) | Confirmed. CIs: GPT-5.5 [-5.3, +6.0], DeepSeek [-6.0, +9.3]; Holm p 1.0 and 0.87; 150 trials per cell; detectable difference 8.3 to 16.0 pp. |
| 5 | Nievelstein: 58.63 vs 8.59 (F(1,68)=105.2, f=1.24); 82.28 vs 37.06 (F(1,32)=37.03) | Nievelstein et al. 2013 repository PDF | Confirmed. The third-year versus first-year prior-knowledge test also seen (17.12). |
| 6 | Tetzlaff 2025: 1590 screened, 176 effects, 60 studies, 5924 participants, d = 0.505 and -0.428 | OpenAlex abstract text (full text not opened) | Confirmed from the abstract. Searches PsycINFO and ERIC only, Dec 2022 and Nov 2024. Moderators: knowledge-test type, educational status, domain. Cited 35 times. |
| 7 | Qiu 2026: 96.4 to 56.9 and 98.2 to 66.0 | arXiv 2605.26350 | Confirmed. CORRECTION below on the "larger models" claim. |
| 8 | Honda 2025 (Gemini 1.5 Pro): MATH500 86.3 / 82.3 / 88.0; GSM8K 94.5 / 95.1 / 94.5; GPQA 57.1 / 56.7 / 60.4 | arXiv 2509.20820 | Confirmed (8-shot / 400- or 250-shot / cheat sheet). |
| 9 | Sprague 2025: 110 papers, 1,218 comparisons, +14.2 / +12.3 / +6.9; 56.9 vs 45.5 | arXiv 2409.12183 | Confirmed. |
| 10 | AdaptThink 1.5B: GSM8K 83.1 vs 79.0, MATH500 82.0 vs 80.6, AIME 31.0 vs 29.4, +2.4, -53.0%; NoThinking 86.9 / 76.8 / 40.4% | arXiv 2505.13417 | Confirmed (lambda 0.05 row). |
| 11 | Meincke 2025: N=4950, +0.135, +0.117, -0.131 | arXiv 2506.07142 | Confirmed. The "35-600% longer" is for non-reasoning models; reasoning models took 20 to 80% longer. Line c14 should say so. |
| 12 | He-Yueya 2024: 42 Year 9 students in the original; 120 personas | arXiv 2403.02795 | Confirmed. |

## 2. Corrections

1. **a30 / b14: "larger models stayed within about 2%" is too broad.** The paper says "stronger recent larger models" stay within about 2%. Llama-2-70B-Chat falls from 97.3 to 87.6 (SD 11.8) at 100% shift; Qwen2.5-72B on the Hard split drops 4.9; Llama-3.1-70B on Medium drops 1.4. Use c06 for the detail. Also the perturbation is an input-style shift, not redundant knowledge.
2. **a11 / b04 (Lee, Plass and Homer 2006): internal arithmetic does not match.** Table 1 as recorded gives novice d = 0.30 and expert d = -1.39, but the listed difference is 2.99. 0.30 + 1.39 = 1.69. Either the novice effect is about 1.60 or the difference is 1.69. The original table could not be re-opened (Springer paywall; the UNSW handle returned nothing to curl). Treat the "largest difference in the table, 2.99" as unverified. I checked the other 9 rows of differences by subtraction (a03, a04, a05, a06, a07, a08, a10, a12 partially): all agree.
3. **Independence of Kalyuga 2007 numbers.** a03 to a13 (opened:false) and b02 to b08 (opened:true) are the same Table 1 transcribed by two agents. They agree, which checks transcription only. They are one source. Founding-study numbers (Kalyuga 1998, 2000, 2001) were never seen in the original papers.
4. **b11 says "from a search summary, not verified"; a25 says abstract only.** Now verified against the abstract (OpenAlex), so both are upgraded to abstract-level confirmed. Full text still not read: the moderator coefficients are unknown.
5. **c13 limits:** keep the 20-80% (reasoning) and 35-600% (non-reasoning) time costs apart. The "+0.101 for Sonnet 3.5 on the 100%-correct metric" in c13 was not found in the text; the table shows Sonnet 3.5 at the 51% threshold +0.131. Treat that single figure as unverified.
6. **Claim "within about 4.9x test-time cut" (a14):** the review gives up to 4.9x for first-step test; not re-opened.
7. **Opened flags:** the Kalyuga 2007 review rows (b01 to b08) are marked opened:true but the only copy reachable this session was the abstract page. The earlier agents may have had a different route; I cannot confirm. Treat them as secondary reads.

## 3. Contradictions between sources

- **Fading works vs does not.** Renkl 2000 (near transfer F(1,51)=4.58 lab; far transfer null) and Atkinson 2003 (fading plus principle prompts helps) against Grosse 2015 (N=143, fading no better than example-problem pairs, p=.129). Not a clean contradiction: different domains and the control differs. Status contested.
- **Reversal predicted vs found.** Law, art history, literature (a17, a18, a19) show no reversal. Statistics (Leppink 2011) and geometry (Chen 2016) show it. Domain structure and how far the "advanced" group really is from schema mastery explain it (authors' own argument; no direct test).
- **"Examples hurt strong reasoning models".** DeepSeek-R1 report says few-shot degrades it (statement only). Hannan 2026 shows a strong model gets little from selection. Honda shows no gain for GPT-4.1. But Xu and Wu find a small positive (+0.7, +1.3) for an example inside a skill. All consistent with "near zero for strong models", none shows a clear harm with numbers.
- **Skill length.** Honda: short cheat sheet beats many shots. SkillsBench: compact beats comprehensive. Consistent. But SkillsBench confounds length with content quality (authors say so).
- **Size and harm.** Wei 2023 says large models override priors using examples; Qiu 2026 says large models are robust to shifted examples. Both are about "large models follow examples better but are less misled by noise". Not contradictory but easy to misread.

## 4. Weak spots

- All the founding human numbers pass through one review (Kalyuga 2007), by the main proponent of the effect, with conservative SDs, no publication-bias check, and mostly cross-sectional groups formed by a pretest median split (regression to the mean risk).
- Meta-analysis (Tetzlaff 2025) is one source and was read at abstract level only. Its asymmetry finding (0.505 vs 0.428) is the best number we have but we do not know the heterogeneity, the publication-bias test or the spread by domain.
- Small cells: many studies have N = 15 to 30 per cell. Leppink 2011 is just significant (F(3,97)=2.762, p<.05).
- Immediate tests can miss the effect (Chen 2016 Exp 4). A one-session agent test would also miss it.
- Only the SkillsBench and Xu and Wu papers test lessons on agents, and neither splits tasks by competence. SkillsBench domain-level comparison is confounded by task difficulty and domain. Xu and Wu is underpowered (8 to 16 pp).
- The LLM demonstration studies (Qiu, Agarwal, Tang, Zou) test the number or quality of examples in classification or math prompts, not whether the agent's competence on a class decides if a lesson helps. They give indirect support only.
- Several 2026 arXiv items (Xu and Wu, Qiu, Li, Hou, Song, Sankaranarayanan, Anand and Idan, the scaffolding-collapse paper) are preprints; I could re-open five and found them accurate. The remainder were not re-opened.

## 5. Only seen in snippets or abstracts

- Tetzlaff 2025 (abstract only), Atkinson 2003 (abstract only), Rey and Buchwald 2011 (abstract only), Chen, Kalyuga and Sweller 2017 (not opened), Salden 2009/2010 (snippets), Gonzaga 2026 (search summary), Kalyuga 1998/2000/2001 originals (review table only), Rourke and Sweller 2009 and Kyun 2013 (thesis review chapter only), DeepSeek-R1 few-shot statement (no table), Song 2026 (abstract direction only).

## GAPS (most decision-relevant first)

1. In an agent loop, does a lesson shown on a task class where the model already passes a high share of items lower accuracy or only waste tokens? Needed: a within-class, competence-split, randomised lesson on/off experiment at equal tokens, with enough tasks to detect 5 pp. No published study found.
2. Where is the cut between weak, middle and strong for a given model, and how many probe items give a stable class pass rate (3, 5, 10)? Kalyuga's probe tests (r .71 to .92) are for humans on well-defined tasks.
3. Does the lesson effect depend on the model size or on reasoning-mode (thinking on/off) after controlling for class pass rate? Qiu and DeepSeek-R1 suggest yes, with no direct measure.
4. Is fading (shorter lesson, last step removed, "name the rule" prompt) better than the full lesson or no lesson for an agent on mid-skill classes? Human evidence is split (K06, K07).
5. Does the lesson effect show up only after a delay (new session, fresh items) as in Chen 2016 and the Cognitive Tutor classroom? What delayed test fits an agent that has no memory between runs?
6. Does item-level complexity (number of interacting steps) predict lesson value better than class pass rate (element interactivity account)? Could be tested cheaply with annotated items.
7. How many and how long should lessons be for each band? SkillsBench says 1 to 3 compact skills; no per-competence breakdown.
8. Full-text check of Tetzlaff 2025: moderators (age, domain, knowledge-test type), heterogeneity, publication-bias tests, and the studies with high-level knowledge groups showing a reliably negative effect.
9. Do lessons derived from verified failing outputs (not model-written) avoid the -8 to -11 pp penalty of self-generated skills? And does the gate cut the 13-of-87 tasks that got worse?
10. Any LLM study with a "stronger model, less benefit from the same example library" curve at fixed tasks (e.g. same library, 3 model sizes, per-task pass rates)? Hannan 2026 (small versus strong) is the nearest, but only for vulnerability detection.

## Gap search results

Search status: the web search quota ran out early; OpenAlex, Semantic Scholar and the arXiv API mostly returned 429. Tetzlaff 2025 was read in full from the CC BY copy on pedocs. New agent papers were read as PDFs (arXiv). Evidence is in evidence_d.jsonl (d01 to d30); claims K30 to K37 are new.

### Closed
- **Gap 8 (Tetzlaff full text): closed.** 60 studies, 176 effects, N=5924. I2 = 90.87% (low side) and 87.55% (high side). Egger p=.57 and .77, no sign of publication bias. Difference of differences d=0.971 [0.631, 1.312], below the 1.72 of the 2007 review. Moderators: educational status (R2 25.92% / 8.47%), content area (low side only, R2 20.59%), and how prior knowledge was assessed (high side R2 50%). Measured median-split groups show only about -0.2 on the expert side (my offset calculation, d27). K02 now established.
- **Gap 9 (verified vs self-written lessons): mostly closed.** Self-written skills fail because the solver never opens them, authoring uses the trial, wrong content, leakage (d05); a second study finds unfiltered induced skills lower average success (d09); evidence-based updates work regardless of writer strength (d21); gated pools beat ungated (d12). No arm compares verified-failure lessons with ungrounded ones at equal tokens.

### Partly answered
- **Gap 1 (within-class reversal at equal tokens):** still no direct study. Closest: rho -0.55 / -0.45 over 33 cells (d09); +66.7 vs +5.6 for one harness on two models (d14). SkillsBench model-level lift is unrelated to baseline (r=-0.03, d17).
- **Gap 2 (probe size):** calculation only (d25): 3 to 5 items are too noisy; about 20 for plus or minus 0.2; SkillApt plateau at about six paired states (d10).
- **Gap 3 (model size / reasoning mode):** hump-shaped benefit in model strength (d18 to d20); weak models do not load or follow lessons; strong models read selectively (d24). Thinking on/off was not isolated.
- **Gap 7 (lesson size per band):** 1 to 3 skills equal, 4+ drops (d06); no per-band breakdown.
- **Gap 10 (same library, several model sizes):** Lin et al. is the best curve (d18); it uses an evolved harness, not a fixed example library.

### Still open
- **Gap 4 (fading for agents):** nothing found; pruning after a model upgrade (d14) is the nearest relative.
- **Gap 5 (delayed test):** no agent study compares immediate and delayed.
- **Gap 6 (item complexity vs class pass rate):** difficulty strata exist (d22) but no interacting-step annotation was tested.

### Corrections
- Tetzlaff 2025 is in Learning and Instruction, not Educational Psychology Review. The "snippets only" entry no longer applies.
- Planning rule: about +0.5 on the weak side, about -0.4 (or -0.2 for measured groups) on the strong side, with very wide spread.
