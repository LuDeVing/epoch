# A12.10 Methods and measurement: cross-check critique

## Numbers re-opened this session (full text, Europe PMC XML or arXiv PDF)
Confirmed exactly:
1. Danek and Wiley 2017 (PMC5247466): 2450 trials, 603 timeouts, 69 missing, 1778 solutions, 36.8% (654) correct, 63.2% (1124) wrong; Aha 66.50 (SD 18.42) vs 52.34 (SD 18.78), t(69)=10.21; 417/1124 (37%) wrong answers above correct mean; solve time 35.81 vs 42.46 s (t(1776)=6.26). Matches a08, b06.
2. Webb, Little and Cropper 2016 (PMC5035735): Exp 1 N=193 (118 female); Aha-accuracy r=0.50 insight, 0.41 CRA, 0.02 non-insight; Exp 1a F(2,158)=33.98, eta2=.30; BIC 5839.0 to 5627.8; 51.9% of correct trials reported insight (a quote of Salvi).
3. Hedne, Norman and Metcalfe 2016 (PMC5005374): 971 trials, 29% insight; accuracy .57 vs .37 d=.51; confidence 78.32 vs 68.95 d=.50; differential warmth 12.93 vs 11.65, t(239.38)=0.72, p=.47, d=.07.
4. Laukkonen and Tangen 2018 (PMC5854655): 631 correct, 180 with 2+ warmth ratings; per-person r=.61 (n=51), per-problem r=.08 (n=182, p=.235); 75.6% / 24.4% / 50.8% / 49.2% contingency.
5. d'Aliberti and Ribeiro 2026 (arXiv 2601.00514): 6.31% shifts; 2.57% vs 16.44% accuracy; 1.79% formal detector; +8.41 pp (0.322 to 0.406) on MATH-500; raw effects -22.48 (high entropy) and -22.90 (low entropy) printed.
6. Alavi Naeini et al. 2023 (arXiv 2306.11167): humans 285/494 walls, 1405/1976 groups; GPT-4 0-shot 6 walls / 239 groups, 1-shot 4/262, 3-shot 5/272, 5-shot 7/269; OCW-Randomized 59/595; OCW-WordNet 471/1926; GPT-3.5 0-shot 0/114, 5/274, 337/1522.

## Corrections and clarifications
- b21 says "best few-shot 7 walls (5-shot), 272 groups (3-shot)" and c16 says "5 walls (3-shot)". Both are right: the best solved-wall count (7) and best group count (272) come from different shot settings. Quote them separately.
- a04 gives Aha-accuracy r=.40 for insight problems; b01 gives .50. Not a conflict: .50 and .41 are Exp 1, .40 is Exp 1a (ESL-filtered subset). Always name the experiment.
- Table 5 of the red-herring paper is garbled in text extraction; the pairing of the 59/595 and 471/1926 figures with GPT-4 0-shot follows row order, not an explicit label. Treat as likely, not certain.
- a21 prints raw shift effects of about -22.5 pp, but the simple gap 16.44 minus 2.57 is -13.9 pp, and a math raw gap is about -11.8 pp (c07). The -22.5 figures are domain-specific, entropy-bucketed and fixed-effect; do not mix them with the pooled gap.
- a03 and b14 (Ash and Wiley 2006) give different F degrees of freedom (111 vs 112) and N (203 with WM data vs a regression df of 111). Regressions use a subsample; the exact N per analysis is unverified.
- a22 (Latif 2024) is not an insight study; its use as proof that models beat humans on insight (b26) is a citation stretch. Do not use it as insight evidence.
- Danek and Wiley 2017 solve-time: a08 gives correct 35.81 s; confirmed. The mixed-model interaction (t=1.58, p<.12) is not significant; claim only the main effects.

## Contradictions between sources
- Warmth: Metcalfe and Wiebe 1987 (sudden jump for insight problems), Kizilirmak 2018 (steeper rise with Aha, CRA) against Hedne 2016 (no difference, d=.07) and Laukkonen and Tangen 2018 (per-problem r=.08). Task (CRA vs magic tricks vs verbal problems), rating interval and number of usable ratings differ.
- Is Aha diagnostic of correctness? Salvi 2016 and Hedne say yes; Metcalfe 1986 and Danek and Wiley say a large share of wrong answers carry Aha; Wiley and Danek 2026 say it depends on the task and on the first move (matchsticks differ across labs).
- Is insight special? Macchi 2025 (verbalisation dissociates) against Salmon-Mordekovich and Leikin 2023 (mostly analytic routes) and Weisberg 2015 (business as usual).
- LLM strength on insight tasks: Speed 2023 (RAT bad, insight problems good), Orru 2023 (human-median), Zhang 2025 (models beat humans on RAT, mixed on insight) against NazoNazo 2025 (far below humans) and OCW 2023. Item sets, scoring (answer only vs justified) and model generation differ; no single "LLMs are bad or good at insight" statement holds.

## Weak spots
- Many LLM claims are single-paper: NazoNazo (one group, one language), d'Aliberti (one group, small open models plus a few closed-model traces), OCW. Counting several evidence lines of one paper as independent would overstate support; claims were marked single-source for that reason.
- The riddle benchmark measures the final answer; it does not show that a riddle needs insight rather than lexical search.
- Wikipedia/field-note claim that lab tasks misrepresent real insight (b28) and the gradual-insight naturalistic side were never opened. This is the second half of this subfield's brief and is thin.
- Human data for LLM comparisons are small (NazoNazo pilot n=126 on a 120-item subset; Orru n=20; Zhang 60-61).
- Speed 2023 and Orru 2023 used early ChatGPT versions; results are dated.

## Seen only in snippets or abstracts (not opened)
Ash, Cushen and Wiley 2009 (abstract page only; PDF 403); Metcalfe and Wiebe 1987; Salvi et al. 2016 (via Webb and press); Weisberg 2015; Klein and Jarosz 2011; Yang et al. 2025 (abstract level); Wadhwa et al. 2026 CREATE; Latif 2024.
Could not re-open this session: Mizumoto et al. NazoNazo (arXiv search and API returned nothing; Semantic Scholar and OpenAlex were rate-limited). Its numbers (7.60%, 17.59%, 52.9%, OR 2.29) are consistent across a17, b18, c01 (three separate readings) but unverified by the cross-checker.

## GAPS
1. Does a forced-reconsideration operator, triggered by high agent uncertainty, beat always-on and never-on reconsideration at equal tokens on a held-out insight set (d'Aliberti shows +8.41 pp on MATH-500 only; no test on riddles or CRAs)?
2. What do the three restructuring criteria of Ash, Cushen and Wiley 2009 (wrong first representation, change, discontinuity) look like in an LLM trace, and can they be scored automatically? The full paper was not read.
3. What does the naturalistic and historical record (Klein and Jarosz 2011 firefighters, mathematics, science case studies, Weisberg's work) say about how often real insight is gradual, with numbers?
4. Do independent labs replicate NazoNazo-style results in other languages and with newer models, and is the reasoning-model gap (7.6% vs 17.6%) explained by length or by verification?
5. Is the verification failure rate (5% to 39% of wrong answers) reproducible on another puzzle set, and does an explicit "check each candidate written in the trace" step remove it?
6. What are the item-level human base rates of insight (not just accuracy) for CRA, magic tricks, matchsticks and riddles, so the S6 set can be matched by difficulty and insight rate?
7. Do LLM Aha-like markers ("Oh!", "wait") carry any signal about correctness when conditioned on entropy and position in the trace, across closed models, not just small GRPO models?
8. Does verbalisation (step-by-step thinking) hurt LLMs on insight items the way it hurts humans (Macchi 2025: 13% vs 57%) at equal tokens?
9. Which of Salvi 2016's (94% vs 78%) and Metcalfe's (warmth marks wrong answers) findings holds for model self-reports of insight, and does an agent's confidence track speed as human Aha does?
10. How large is the contamination risk for classic insight problems (Ansburg and Dominowski, nine-dot, Only Connect) in LLM training data, and which renewable item sets avoid it?

## Gap search results (evidence_d.jsonl, d01-d22; claims K22-K29 added, K04, K07, K08, K11-K16, K18, K19, K21 updated)

Source limits this pass: the WebSearch budget was spent, arXiv API and Semantic Scholar were rate-limited, OpenAlex was out of budget. I used arXiv PDFs by ID, Europe PMC full text, Crossref abstracts and one page summary tool. Ash, Cushen and Wiley (2009) PDF is still blocked (403). Klein and Jarosz (2011) was read as an abstract only.

Closed or mostly closed:
- Gap 4, first half (NazoNazo figures): re-read, 7.6%, 17.6%, 52.9% (CI 46.6-59.2%) and verification failure 5.23%-39.34% match (d21). The cross-checker flag is closed. Independent replication still not found.
- Gap 9, partly: Salvi 2016 numbers now read (93.7% vs 78.3% on CRA; 78.4% vs 41.5% on visual Aha) (d13); the Aha bundle result (only surprise tracks prediction error) is in (d19). Model self-reports of Aha were not found; Kadavath (d09) gives only a calibration baseline.
- Gap 10, partly: contamination risk is real (d03, d10, d11, d15, d22). A renewable design exists (NazoNazo open/blind/post-cutoff sets, d21) and a cheap completion test (d11). Contamination rate for the nine-dot or Ansburg items was not measured by anyone found.
- Gap 7, partly: Aha and wait words are in base models, not tied to accuracy (d04), and sit on high-entropy tokens (d05). No test in closed models of marker versus correctness given entropy.

Moved, still open:
- Gap 1: the +8.41 pp in d'Aliberti is pass 2 over pass 1 on MATH-500 with no cue-free control found and double the tokens. Llama 3.1-8B lost 4.19 pp in a small slice (d20). Self-correction without an oracle lowered accuracy in older models (d08). No equal-token three-arm test on insight items exists in the sources read.
- Gap 3: field data is thin. Klein and Jarosz coded 120 incidents with three pathways (d17); filmed mathematicians gave 27 sudden insights with measurable lead-up (d16). No number for "often gradual" was found; the claim K21 is now contested, not supported.
- Gap 5: the 5%-39% rate is on one puzzle set, measured by literal answer mention (d21). Traces are often unfaithful (d06) and hidden states encode correctness (d07). No test of a written check step.
- Gap 6: partial human base rates (magic 41% Aha, d12; Romanian CRA accuracy mean .54, SD .43, d14). No source with per-item insight rate across CRA, matchsticks and riddles.
- Gap 8: CoT hurts models on three human-verbal-overshadowing tasks, none an insight task (d01). Insight items at equal tokens untested.

Stayed open, no new source:
- Gap 2: the three restructuring criteria in an LLM trace. No automatic scoring method was found. The d'Aliberti shift detector (cue word plus change) is the nearest, and its false-positive handling is in its appendix, not read in full.

New caveats:
- Salvi 2016 numbers came through a page summary, not the PDF text.
- d09 (Kadavath) and d19 (Surprise! 2024) were read at abstract or section level; no effect sizes recorded.
- Latif 2024 is not insight evidence (already noted); the GenAI-vs-students RAT paper (d15) is a better source for RAT saturation.
