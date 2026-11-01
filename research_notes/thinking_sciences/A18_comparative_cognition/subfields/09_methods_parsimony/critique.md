# A18.09 Methods: parsimony - cross-check critique

## Numbers re-opened and checked (text re-read this session)
1. Kosinski (arXiv 2302.02083): 5% davinci-002, 20% davinci-003 and GPT-3.5-turbo, 75% GPT-4 (CI 66-84%), R=0.98. Confirmed (a18, b13, c05). Also found: davinci-003 fell from 90% to 20% once true-belief controls were added; used in K11.
2. Shapira (2305.14763): ToMi 81% overall, 46% on false-belief questions; FauxPas-EAI 27% for GPT-4. Confirmed (a21, b12, c03).
3. Zhang GSM1k (2405.00332): drops up to 8%, Spearman r2=0.36. Confirmed. Note the paper itself says Pearson r2=0.26 and that outliers lower the figure.
4. Mirzadeh GSM-Symbolic (2410.05229): up to 65% drop, o1-preview -17.5, o1-mini -29.1. Confirmed. The 65% is the worst case (Phi-3-mini), not typical.
5. McCoy Embers (2309.13638): cipher 51% vs 13%; reverse sequence 97% vs 53%. Confirmed.
6. Kano 2017 control (PMC5595417): 22/43 (51.16%) vs 22/30 (73.33%); first looks 14/22 target, p=.28. Confirmed.
7. Kampis 2021 (PMC8386515): 160 infants tested, 90 kept, 49/90 (54%) familiarisation, 22/49 at test p=.568. Confirmed. Detail: FB1 15/31 vs FB2 7/18.
8. Kulke and Rakoczy 2019 (PMC6433471): FB1 7/12 (58%), BF10 0.643. Confirmed.
9. Schmidjell 2012 (PMC3530188): 69 dogs, N=17/18/17/17 groups. Confirmed.
10. Pfungst via Wikipedia raw text: 50/56 (89%). Confirmed. The 2/35 (6%) was not re-seen in the text I pulled; keep it as secondary. Wikipedia is not Pfungst.
11. Strachan (PMC11272575): faux pas GPT-4 P=5.42e-5; N=1,907 total. Confirmed. FLAG: the text gives P=0.040 for BOTH irony and hinting, with identical Z=0.00 and r=0.32 but different CIs. Likely a reporting oddity or a copy artefact; a23 attributes 0.040 to irony only. Corrected in K13 to cover both.

Not re-verified: Farrar 2021 survey numbers (a14; no local text found), SimpleToM, FANToM, Ullman variants, Golchin, Oren. Those rest on the first agents' reading.

## Corrections made
- a23: irony P=0.040 is shared with hinting; not irony-specific.
- Triplicates: a19/b10/c01 are one paper (Ullman), a21/b12/c03/c04 one paper (Shapira), a18/b13/c05/c24 one paper (Kosinski), a14 vs c14 and b17 same (Sap). Independent source counts in claims count papers, not lines.
- b21/b22 labelled 2024 in id, source year 2026 in the title: it is an arXiv 2024 paper with a 2026 venue version. Not a data conflict.
- a25 (Niven and Kao), a26, a27 were opened:false in snippets only; a26 numbers were confirmed against b19 and the paper.

## Contradictions
- Kano 2017: control says apes' effect weaker (51% vs 73%) but the authors say no evidence of low-level cueing; Heyes's account is not refuted or confirmed.
- Strachan vs Shapira: GPT-4 at human level on faux pas after rewording (Strachan follow-up) vs 27% (Shapira FauxPas-EAI). Different items, formats and scoring; not a clean contradiction.
- Kosinski (75%, child level) vs Ullman (fails trivial changes): same model family, different test, no direct head-to-head on GPT-4. Ullman tested GPT-3.5.
- SimpleToM: large models over 95% on explicit awareness but 10-25% on behaviour judgement, yet one reminder lifted Claude-3.5-Sonnet to 84.1%. Large model dependence.

## Weak spots
- Almost all LLM perturbation studies use GPT-3.5/GPT-4-era models (2023-24). No evidence on current reasoning models for ToM perturbation; Mirzadeh includes o1 only.
- Nothing measured Morgan's canon as an operator in an agent loop (K17). All agent-relevant claims are inferred from perturbation-test results.
- Contamination detectors validated on few datasets and mostly GPT-3.5/4 or small open models.
- Animal-side numbers mostly come from review text or Wikipedia, not from the original papers (Pfungst 1911, Morgan 1903, Krupenye 2016, Hare 2001).
- Heyes 2012, Shettleworth 2010 (b25, b27, a15, a16, a17, b24) were seen only as listings or abstracts.

## GAPS
1. Does a forced "cheap rival plus discriminating probe" operator improve accuracy or reduce contamination damage at equal tokens versus a plain CoT baseline? (No one has tested it; K16 and K17.)
2. How do 2025-26 reasoning models (o-series, extended-thinking) score on Ullman-style and FANToM-style perturbation twins? Is the gap still there?
3. What is the base-rate of "default minus counterfactual" gap on our own tasks, and does our scaffold shrink it?
4. Which cue-ablation (Pfungst-style) checks catch the most contamination per token on an LLM: paraphrase, name swap, number swap, or format swap?
5. How many repeat runs or rephrasings are needed before a single pass is trustworthy (the human replication literature suggests many pass-once effects vanish)?
6. Do the Kano and Kampis replication gaps have an LLM analogue: do published LLM ToM passes shrink on preregistered re-runs by other groups?
7. Can contamination detectors (Golchin guided completion, Oren order test) run on API-only models at useful power, and at what token cost?
8. Does lowering task demands (likelihood or forced choice) change conclusions across more than two studies, and does it interact with CoT?
9. Do original-source numbers for Pfungst (2/35), Krupenye 2016, Hare 2001 and Farrar 2021 survey match the secondary reports used here?
10. Is there any evidence that rubrics requiring the "simplest sufficient explanation" cause under-claiming (false negatives) in an agent?

## Gap search results

Search limits: WebSearch quota was used up and the arXiv, OpenAlex and Semantic Scholar APIs returned 429 (rate limited). Work was done by fetching known arXiv PDFs, Project Gutenberg and PMC pages directly. Evidence is in evidence_d.jsonl (d01-d17). New claims K19-K23; K02, K09, K12, K14, K15, K17 updated.

Closed or mostly closed:
- Gap 9 (source numbers). Pfungst's own text: 102 blinder tests, 35 not seen (2 correct, 6%), 56 seen (89%), 11 undecided (18%). Matches the secondary 2/35 and 50/56, which hid the undecided bin. Farrar 2021: 1001 invited, 210 completed (21.6%), 39.7% and 38.8% hoping for a result, all match. Not closed: Krupenye 2016 and Hare 2001 (only abstracts reachable, so 22/30 stays second-hand via Kano).
- Gap 7 (detectors on API models). Guided completion works on chat APIs (10 instances per split, temperature 0, 500 tokens, plus a judge call; 14/14 and 13/14 partitions agreed with experts). The order test needs prompt log probs, misses single exposures, and detects from about 4 or more duplicates. Power on unlabeled real models is still unmeasured.
- Gap 2 (reasoning models), partly. SimpleToM shows the explicit-versus-applied gap remains for o1, o3-mini, GPT-5 and DeepSeek-R1 (judgment 32.5 to 65.8 against 85-99 mental-state accuracy). It is not the Ullman or FANToM twin design, so the original question stays open in its exact form.
- Gap 8 (task demands), partly. Hu and Frank show the demand gap in four domains. Chain-of-thought interaction was not tested by them.
- Gap 5 and gap 4, partly. Format and paraphrase changes move scores by up to 56 to 76 points (median 6.4 for GPT-3.5), and rankings change across paraphrases. Paraphrase hides contamination best (85.9 on MMLU undetected by n-grams). No source ranks paraphrase, name, number and format swaps per token, and none gives a number of rephrasings needed.

Still open:
- Gap 1 (rival-plus-probe versus plain CoT). No test found. The nearest result is a warning: a forced generic self-review lowered GPT-3.5 CommonSenseQA from 75.8 to 38.1. Needs our own experiment with a keep-answer exit and equal tokens.
- Gap 3 (default-minus-counterfactual gap on our tasks). Needs our own run.
- Gap 6 (LLM analogue of Kano and Kampis shrinkage). No preregistered re-run by another group found; search failed so this is not evidence of absence. BigToM suggests only GPT-4 holds under paired false-belief controls.
- Gap 10 (under-claiming from a simplest-explanation rubric). No evidence found. Needs our own false-negative measurement.

Next: rerun the literature search when quota returns for Ullman or FANToM twin re-runs on o-series and extended-thinking models, and for ToM re-runs by other groups.
