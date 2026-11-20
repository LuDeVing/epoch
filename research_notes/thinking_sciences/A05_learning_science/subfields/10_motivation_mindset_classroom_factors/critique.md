# Critique: Motivation, mindset, classroom factors (A05.10)

## Checks done this session
Re-opened (PubMed XML or arXiv abstract page) and confirmed: Macnamara and Burgoyne 2023 (63 studies, N=97,672, d=0.05 [0.02,0.09]; 13 studies d=0.04; 6 studies d=0.02; financial-incentive authors larger effects); Sisk 2018 (k=273 N=365,915; k=43 N=57,155; abstract only); Burnette 2013 (k=113, N=28,217, all six r values match); EmotionPrompt (8.00%, 115%, 45 tasks, 106 human raters); Yin politeness abstract; Meincke tipping/threat (no significant aggregate effect); Handa 2023 (174 teachers, 1,006 students); Wuji 2026 (+59%, d=2.28, p=.002; Study 2 +74% steps p=.008, +25% hidden issues p=.016; fear framing no gain, p>.3); Dobariya and Kumar (80.8% to 84.8%, 50 questions x 5 tones); Huang 2024 abstract. Not re-opened: Yeager 2019 figures (three evidence files agree with each other but all read the same PMC page), Kestin, Bastani, Voyager, Reflexion, OPRO.

## Corrections
1. c17 is labelled "Burnette et al. (2023)" but its numbers (63 studies, N=97,672, d=0.05) are Macnamara and Burgoyne 2023. Burnette 2023 is the re-analysis with 0.09 overall (b25). Treat c17 as the same source as a14 and b09, not an independent one. Triangulation counts it once.
2. a14, b09, c17 are one source. a15, b10, b25 are one commentary. Independent-source counts in claims.jsonl use this.
3. c18 DOI (10.1177/0956797617707270) is wrong; the Sisk paper is 10.1177/0956797617739704 (confirmed in PubMed). Its recalled "d about 0.08" is confirmed by b07 (0.08, CI -0.01 to 0.17, not significant).
4. a12 says exact r and d were not read; b06/b07 give r=.10 and d=0.08. Use those.
5. a05, a06, b15, b16, c23 (Blackwell 2007, Mueller and Dweck 1998) carry no real numbers; b15's "38% vs 13%" is from memory and must not be cited until checked. The search URLs in a05/a06 are PubMed search pages, not the papers.
6. a01, b01, c16 are the same table read three times; they are one source for triangulation.

## Contradictions between sources
- Overall effect: 0.05 d, non-significant after bias correction (Macnamara and Burgoyne) versus 0.09 SD, 0.05 after corrections still p=.004 (Tipton, Yeager et al.). Authors on both sides are invested; the Macnamara paper also reports that financially incentivised authors found larger effects.
- Quality subset: "highest-quality d=0.02" versus Tipton footnote that this subgroup came from miscoded studies.
- Tipton report that the Egger test fired in data with no real publication bias; this undercuts the "not significant after bias correction" line.
- EmotionPrompt gains versus Meincke (no aggregate effect of tips and threats) versus GPT-4 average dropping under EmotionPrompt. Different models, tasks, and prompt types, so not a direct clash, but the gain is not general.
- Politeness: rude hurts older models (Yin) but helps GPT-4o (Dobariya and Kumar, 50 questions, tiny).

## Weak spots
- Almost the whole human evidence base on interventions is from one team (Yeager, Dweck) or the one opposing team (Macnamara, Sisk, Burgoyne).
- LLM evidence is prompt-wording tests; none tests mindset as the theory defines it (belief about malleability plus failure experience). The mapping from classroom to agent is an analogy.
- Wuji 2026 is single author, one model, nine scenarios in Study 1, and tied to a named prompt methodology. Not strong enough to base a design change on.
- EmotionPrompt and NegativePrompt come from overlapping authors; gains are relative percentages on tasks with low baselines (BIG-Bench), which inflates headline numbers.
- Self-determination theory (a25), Bandura (a26) and Dweck and Leggett (a24) were not opened.

## Only seen in snippets
Bastani 2025 (c20), Kim 2024 (c21), Li and Bates (b12), EEF Changing Mindsets (b13), Bahnik and Vranka (b14), Mueller and Dweck, Blackwell 2007, Macnamara abstract only (b09), Sisk abstract only.

## GAPS
1. Does any growth-mindset-style prompt (ability is malleable, mistakes are informative) beat a length-matched neutral prompt on a reasoning benchmark at equal tokens, across 3+ models and 5+ seeds? No study found; this is the decision-relevant test.
2. Does the effect of an encouragement or "you can improve" retry prompt depend on having a verifier signal? Huang 2024 suggests yes; a direct 2x2 (verifier or not, encouragement or not) is missing.
3. What are the exact numbers in Mueller and Dweck 1998 (inflation of reported scores, post-failure persistence) and Blackwell 2007 Study 2 (cell sizes, grade slopes), and have they been replicated beyond Li and Bates?
4. What did the EEF Changing Mindsets trial (Foliano 2019) and the Li and Bates trials actually report (N, intervals)? Needed to settle the independent-replication count.
5. Do the persona result (Zheng 2024) and the tip/threat null (Meincke 2025) hold on reasoning models (o-series, Claude thinking models), where prompt sensitivity may be lower?
6. Is the EmotionPrompt gain just any extra salient sentence? Needs the positive, negative and neutral-length comparison on one model set.
7. Can the Wuji trust versus fear framing be replicated by an independent group with more than 9 scenarios?
8. Does a Bastani-style harm (worse after help removal) have an agent analog, such as a scaffold that raises in-loop score but lowers performance when removed?
9. Which curiosity or learning-progress signals (OMNI, Motif) have been tested as branch selectors in reasoning agents rather than embodied games?
10. Is there independent (non-Yeager) evidence on teacher-mindset moderation, to test whether context matters or only one dataset says so?

## Gap search results (2026-11-20)
Sources are in evidence_d.jsonl (d01-d18). Claims updated: K04, K08, K10, K11, K12, K14, K17, K20; new K22-K25. Search tools were rate-limited (Semantic Scholar, arXiv API, OpenAlex returned 429 or budget errors), so work relied on 8 web searches and direct PDF reads.

1. Growth-mindset prompt vs length-matched neutral on reasoning benchmark: STAYS OPEN. Closest is Battle and Gollapudi 2024 (60 positive-thinking snippets, 3 old models, GSM8K subsets of 10-100 items, no length control, d07). No study with the required design found.
2. Encouragement by verifier 2x2: STAYS OPEN. Kamoi 2024 survey (d08) says prompted self-feedback fails under fair settings and works with reliable external feedback; no direct 2x2.
3. Mueller and Dweck 1998 and Blackwell 2007: PARTLY CLOSED. Mueller and Dweck read in full: 67% vs 8% performance goals (Study 1), 38% vs 13% vs 14% misreporting (Study 3, N=88), score change -0.92 vs +1.21 (d09). The "38% vs 13%" is now verified. Blackwell: only the abstract (373; 48 vs 43); slopes unread (d11). Replication beyond Li and Bates: a China praise study, N=103, partial support (d10); Li and Bates 2020 grades near-replications, n=832 (d12).
4. EEF and Li and Bates numbers: CLOSED for EEF (101 schools, 5,018 pupils, maths -0.01 [-0.04,0.01], reading -0.00, grammar -0.00, 0 months, d13) and for Li and Bates 2020 (d12). The 2019 JEP:General Li and Bates paper was not opened. Independent-null count is now: EEF, Li and Bates, China praise study (partial).
5. Reasoning models: LARGELY CLOSED for tips, threats and personas. Report 3 (5 models incl. o4-mini, d01) and Report 4 (6 models incl. o3-mini, o4-mini, d03) show no consistent gain. No Claude thinking model was tested in these; that part stays open.
6. EmotionPrompt vs any salient sentence: CLOSED for current models. Positive equals negative (+0.04 pp, CI -0.34 to +0.42) and both sit 1.3-1.4 pp under neutral (d05); six-benchmark study shows small changes (d04). A length-matched neutral arm with the original prompts was not found; the ICML paper's distractor control is exploratory.
7. Wuji trust vs fear replication: STAYS OPEN. No independent replication found.
8. Bastani-style harm analog: PARTLY ADDRESSED. A scaffold can raise the mean while lowering reliability (CoT: mean up, all-25-correct down, d02), but no agent study of performance after scaffold removal was found.
9. Curiosity or progress signals as branch selectors: STAYS OPEN. Only training-time uses (CDE, +2.4 average, d15) and RLVR task-selection hits (d16, unopened).
10. Non-Yeager teacher-mindset moderation: MOSTLY CLOSED. Chile census, 292,960 students, +0.02 SD, bigger in low-income schools (d14); a Psychological Science trial may show the opposite direction for teacher type (d17, snippet only).

New weak spots: d16, d17, d18 are search summaries (opened:false). Blackwell Study 2 slopes, Li and Bates 2019, Yeager 2019 figures remain unread. Decision-relevant tests (gaps 1, 2, 7, 9) must be run in our own harness.
