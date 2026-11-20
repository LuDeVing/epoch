# Critique: Beliefs and affect (E06.09)

## Corrections made (sources re-opened this session)
1. EmotionPrompt 8.00% and 115% confirmed (arXiv 2307.11760).
2. Zero-shot vs few-shot gain: a18 says "few-shot 2.05 vs zero-shot 0.33"; c03 says "2.05 zero-shot vs 0.33 few-shot". The paper's own sentence says the gain is larger in few-shot "(0.33 vs. 2.05)", which reads backward. The paper is internally inconsistent. Do not quote either direction.
3. Underthinking: 225% more tokens and 418% more thought switches confirmed (arXiv 2501.18585, intro).
4. Overthinking: 1,953% and 48.6% confirmed (arXiv 2412.21187).
5. Sycophancy: 27%, 32%-86%, 42%-98% confirmed (arXiv 2310.13548). Two different 27% figures exist: up to 27% for LLaMA 2 under a user-suggested wrong answer (Results text, Fig 3), and 27% (Claude 1.3) averaged over six datasets for "Are you sure?" (line 1052). Earlier lines blur these.
6. s1: 50.0 to 56.7 on AIME24 confirmed in the paper table (arXiv 2501.19393). The a26 ablation row (53.3) was not re-checked.
7. Barroso 2021 exists (Psychological Bulletin, doi 10.1037/bul0000307); r=-.28 (b14) not re-opened.
Not re-opened: Caviola, Macnamara, Yeager figures; Huang self-correction table; BrokenMath ranking. These rest on earlier agents' reading.

## Contradictions
- Overthinking (stop earlier) vs underthinking and budget forcing (think longer). Consistent only if the stop point depends on verification.
- Mindset: Yeager +0.10 grade points in lower achievers vs Macnamara best-evidence 0.02.
- EmotionPrompt relative gains (115%) depend on low base scores; not comparable to absolute gains.

## Weak spots
- Core Schoenfeld numbers (a02-a10, b02-b05) come from slides and a handbook review, not the 1985 book or 1988/1989 papers (a11-a15 unread). No group sizes for the wild goose chase 60% to under 20% result.
- Math anxiety and mindset evidence is human-only; no clear mapping to an agent.
- No study tests belief interventions on LLM math solving directly.
- Over/underthinking studies use different models, so they are only loosely comparable.
- Seen only in snippets or citations: a11-a15, b06, b08-b10, b14, b18, b19, b27-b29, c19-c22.
- LLM anxiety evidence is questionnaire self-report, not accuracy.

## GAPS
1. Does telling an LLM that problems are hard or long (against the 5-minute belief) change give-up rate and accuracy at equal tokens?
2. What are the actual sample, effect size and statistics of Schoenfeld's wild goose chase result (60% to under 20%), and was it replicated?
3. Does a verification-based stop rule beat both budget forcing and early stopping at equal tokens?
4. Does EmotionPrompt or NegativePrompt survive a length-matched neutral control on math, on 2025-2026 models?
5. Do anxiety-inducing pre-prompts change math accuracy, not just questionnaire scores?
6. Does the "Are you sure?" flip rate fall when the agent must re-verify before changing an answer?
7. Which classroom belief-change interventions (Schoenfeld, Lester, Garofalo) have measured effects, and is any analogous to a schema rule?
8. How do 2026 frontier models score on persistence behaviours (flip rate, premature give-up) versus the 2023 numbers?
9. Is the Macnamara vs Yeager mindset conflict explained by moderators we could mimic (e.g. challenge-seeking framing)?

## Gap search results (evidence_d.jsonl, d01-d20; claims K16-K22 added)
Search note: WebSearch budget and the Semantic Scholar, OpenAlex and arXiv APIs were rate-limited or exhausted, so sources were found by memory of paper ids, Crossref, ERIC and archive.org metadata, and direct PDF downloads.

1. Hard-problem priming (give-up rate at equal tokens): STAYS OPEN. No study found that tells an LLM problems are hard or long. Indirect only: TEMPER (d05, d06) shows affective problem wording costs 2 to 10 pp; inverse-scaling (d14) shows longer thinking can hurt.
2. Wild goose chase statistics: CLOSED (as far as the source goes). Primary source is Schoenfeld's 1982 NSF final report (d01): 7 of 12 pretest protocols (58%) vs 2 of 12 posttest (17%), six student pairs, author-coded, no test statistic, no independent replication found. The "60% to under 20%" figure is a rounding of this count. Course effect on the problem test is separate (d02: 21 to 73 vs 14 to 24, interaction F(1,17)=48.2).
3. Verification stop rule vs budget forcing and early stopping at equal tokens: PARTLY CLOSED. DEER, Dynasor, hidden-state probe and DeepConf (d09 to d13) show verification or confidence stops cut tokens with equal or better accuracy; DEER beat a token-budget prompt set to its own length (AIME24 49.2 vs 48.4, vanilla 41.7). Parallel voting beat extended thinking at 16K (d12). No paper does a strict equal-token three-way against s1 Wait forcing.
4. EmotionPrompt on math, 2025-2026, length-matched control: CLOSED, negative. Replication on newer models: +1% overall, p=.74; original 115% was best-of-11 (d08). 2026 test: GSM8K within about 2 pp (d07). Length-matched paraphrase control exists for TEMPER (d06) and shows the harm is from affect, not length. No length-matched neutral filler control for the positive EmotionPrompt suffixes specifically.
5. Anxiety pre-prompt and math accuracy: STAYS OPEN for pre-prompts. Related: emotional wording in the problem lowers accuracy (d05), fear 5.2 pp mean, 6.1 on GSM8K.
6. "Are you sure?" with a re-verify step: PARTLY OPEN. FlipFlop (d15) tested fine-tuning only (about 60% less deterioration); SycEval (d16) gives regressive 14.66%; ProCo (d17) shows a structured substitute-and-check beats plain self-correction (AQuA 65.2 vs 48.7). No direct test of verify-before-flip.
7. Classroom belief interventions: PARTLY CLOSED. Lester, Garofalo and Kroll (d04): gains with no control and a ceiling effect; orientation phase mattered most. Schoenfeld course effect (d02) is large but tiny-sample. Garofalo-style and Schoenfeld belief-specific interventions were not measured in the sources read. Analogue to a schema rule: orient and size the task before executing, and keep something to monitor.
8. 2026 frontier persistence vs 2023 numbers: STAYS OPEN. 2025-2026 models were measured on social sycophancy (ELEPHANT, d18) and emotional framing (TEMPER with GPT-5.4), not flip rate or give-up on math. Keep the 2023 flip numbers labelled as 2023.
9. Macnamara vs Yeager moderators: STAYS OPEN. Hecht et al. 2023 (d19) points to disadvantaged classes and teacher practice, abstract only. Burnette, Tipton and Rege (d20) were leads only, not read.

Corrections: the "60% to under 20%" figure in K02 now rests on a primary source and counts protocols (12 and 12), not students. K05 is now contested because of a failed replication. K11 and K12 now carry the stop-rule evidence.
