# Critique: E18.05 Choice architecture and nudging (cross-check)

Cross-checker pass. Sources re-opened this session: Madrian & Shea NBER w7682 PDF, DellaVigna & Linos NBER w27594 PDF, Mertens et al. and Maier et al. (PMC full text), and arXiv PDFs of Liu (lost in the middle), Zheng (PriDe), Wang (fair evaluators), Cherep (hypersensitive), Echterhoff (BiasBuster), Allouah (ACES), Sclar (FormatSpread). 27 claims written to claims.jsonl.

## Numbers re-checked (10 or more)

Confirmed exactly:
- Mertens: d = 0.45 (CI 0.39-0.52), N = 2,149,683, I2 = 99.67%, tau2 = 0.23, prediction interval [-0.48, 1.39], about 15% backfire, default d = 0.62 (k = 132, N = 139,948), food 0.72 (N = 12,515), finance 0.25.
- Maier: combined 0.43 / RoBMA-PSMA 0.04 [0.00, 0.14] / precise 0.11 [0.00, 0.24]; combined BF01 = 0.95 and 0.31; information BF01 = 33.84.
- DellaVigna & Linos: 126 RCTs, over 23 million people; 8.7 pp (s.e. 2.5), 33.5% over control 26.0; nudge units 1.4 pp (s.e. 0.3), 8.1% over 17.2; median arms 10,006 vs 484; bias-corrected academic 3.16-3.2 pp.
- Madrian & Shea: 86% participation in the automatic-enrolment cohort; 48.5 pp gap in non-participation; 76% of NEW participants at 3%; 61% at 3% plus money market; 80% of money to the money market fund.
- Liu: 20 docs GPT-3.5 75.8 / 53.8 / 63.2 (index 0 / 9 / 19); 30 docs GPT-3.5-16K 73.4 / 50.5 / 63.7 (index 0 / 9 / 29); closed-book 56.1.
- Zheng: 67.2 to 60.9 (D), 53.1 to 68.2 (A) vs gpt-3.5 65.3; llama-30B letters 34.6/27.3/22.3/15.8.
- Wang: conflict 46.3% / 5.0% (GPT-4), 82.5% / 52.5% (ChatGPT); win rate 2.5% vs 82.5%; scoring 44.4 to 53.2 to 58.7%, conflict 82.5 to 35.0%.
- Cherep: human accept 0.51 to 0.88; GPT-3.5 0.33 to 0.99; Gemini 1.5 Flash 0.94; 340 trials per condition.
- Echterhoff: 13,465 prompts, 40.5% and 32.1% quoted in text; GPT-4 framing gap -0.405 baseline, -0.010 self-help, awareness -0.470, contrastive -0.410.
- Allouah: position coefficients 1.224 / 1.045 / 0.344; Overall Pick 1.060 / 0.802 / 1.897; seller gains +3.66 / +8.37 / +14.79 pp; "ignore position" text confirmed.
- Sclar: 76 points (LLaMA-2-13B), 56 points with median 6.4 (GPT-3.5, 320 formats, 53 tasks).

## Corrections made

1. a03 said the earlier WINDOW cohort participated "about half". The paper gives 37% at 3-15 months tenure vs 86% (NEW), so the ratio is under one half. The 48.5 pp figure is the gap in the 0% contribution category, not a gap in participation rates read from a table; it is consistent with 86% vs 37% only roughly (49 pp).
2. a12 agent_relevance said the real effect is "about one fifth" of the published one. The paper says about one sixth (1.4 vs 8.7). Use one sixth.
3. a04: 76% at 3% is a share of participants. Among all NEW employees 61% sat at 3% plus money market. The paper also gives 65.1% of NEW at 3% (all employees), so the three figures answer different denominators. Do not mix.
4. b12 / a24 / c15: "66 of 80" is the abstract claim (Vicuna beats ChatGPT in 66 of 80 with ChatGPT judge). It equals the 82.5% win rate in the favoured slot. It is not a second statistic. Treat it as one number.
5. a11 gives no combined-effect Bayes factor; b03 has it (0.95 and 0.31, undecided). Use b03. a11's text "using most precise estimates BF" not needed.
6. b04 says severe-bias sensitivity d = 0.08 while the original paper text says 0.03; kept as unresolved (reply letter vs article). Not re-opened here.
7. a16 "remaining biased prompt elements 0% / 1.4% / 2.7%" was not found in the table values I read; the verified self-help result is the GPT-4 framing gap change (-0.405 to -0.010). Treat a16's percentages as unverified.
8. b11 states PriDe estimates stable "from 2% to 20%" and "beats full or cyclic permutation" from the paper's text; I did not re-verify these two. Gain tables in c13 were never copied.
9. c10 vs a20: both fine, but a20 ("falls by more than 20%") is the paper's abstract wording about the worst case; keep as stated.

## Contradictions between sources

- Defaults in LLMs: Echterhoff finds the stated status-quo option chosen less by most models (reverse), while Cherep finds a default in the prompt is accepted at 0.99 vs 0.88 for humans. Different tasks (status quo bias vs. prompt-visible suggestion), so not a true contradiction, but nobody ran both on one model. Claim K16 is marked contested.
- Mean effect: Mertens (d 0.45, later 0.31 / 0.08 sensitivity) vs Maier (0.04-0.11). Structure nudges are undecided (BF01 1.1). Both sides accept heterogeneity.
- Capability: Itzhak says instruction tuning raises some biases; Hagendorff (unread) says CRT biases vanish in ChatGPT; Allouah says plain errors fall but position bias stays.
- Sign of position bias flips between models and versions (Allouah), so Zheng's letter-A preference is not a general law.

## Weak spots

- Almost all LLM layout evidence is 2022-2023 models (GPT-3, GPT-3.5, early GPT-4, Vicuna, Llama-2). Only Allouah (2025) and Cherep (2025) use recent models, and Allouah is a mock store, not reasoning tasks.
- Lost-in-the-middle, FormatSpread, and Wang are each single-source for their exact numbers. Many later replications exist but were not in the evidence files.
- Human framing and default founding numbers come via Wikipedia or memory (Johnson & Goldstein, Tversky & Kahneman original percentages, Save More Tomorrow, Jachimowicz d = 0.68). Not opened: a02, a05, a06, a07, a08, a14, b07, b20-b23, c24, c25.
- Jachimowicz d = 0.68 appears in two files but both are second-hand.
- No replication of Asian disease framing (Many Labs or later) was checked, and no failed replication of Madrian & Shea style defaults other than the nudge-unit result.
- Allouah coefficients are logit coefficients in one simulated store; the "ignore position" attenuation size was not recorded.
- Suri (GPT-3.5) has 11 or 5 trials per cell and near-deterministic output, so t-tests overstate certainty.
- No study tests layout effects on a scaffolded agent (program plus model), which is the real target.

## Only seen in snippets or secondary summaries

Nudge definition and critiques (Wikipedia); Asian disease numbers (Wikipedia); Johnson & Goldstein; Save More Tomorrow; prospect theory parameters; Jachimowicz; Szaszi letter (via Mertens reply); Hagendorff; Horton; Pezeshkpour (abstract and figure only); Macmillan-Scott (abstract and part of a table); PMC12478545 (download failed).

## GAPS

1. Do layout effects (option order, default marker, framing, anchor) survive on current reasoning models at equal tokens, and by how much, in one matched battery on the same model? (Decides whether layout guards are worth their token cost.)
2. Does a code-side permutation-and-vote guard beat an instruction-only "ignore order" guard, and a single canonical layout, on our own benchmark items at equal tokens?
3. Does S1 neutral restatement remove framing and anchor effects without changing meaning? Needs a meaning-preservation check; Echterhoff measured removal of biased parts, not correctness.
4. Is the LLM default effect driven by endorsement (a marked or recommended option) or by copy bias (any sample value in context)? Test marked vs unmarked sample answers.
5. What do recent long-context and reasoning models show on lost-in-the-middle and format spread (2024-2026 replications)? Which prompt zones are safe for rules?
6. What do Many Labs and other large replications say about gain/loss framing (Asian disease) and anchoring in humans, and how big is the surviving effect?
7. Does a reasoning budget (extended thinking) reduce nudge sensitivity? Cherep's PNAS 2026 follow-up reportedly says only inconsistently; read it.
8. How large is the real default effect in humans after correction (Jachimowicz, original read; organ donation actual donation vs registration; default-change field trials)?
9. Do judges and selectors show the same position bias when the agent's own candidates are compared (self-preference plus order), and how many order-swaps are needed before returns vanish?
10. Do retrieved or candidate texts edited to win selection (Allouah seller result) matter for our memory and candidate-ranking steps, and can code-side stripping of persuasion cues block them?

## Gap search results

Gap searcher pass. 17 evidence lines in evidence_d.jsonl (d01-d17); claims.jsonl now has 34 claims (K12 and K18 upgraded to established; K28-K34 added; notes added to K01, K03, K13-K15, K23, K26). Budget: 8 WebSearch calls at most; the arXiv and OpenAlex APIs were rate limited (HTTP 429) for the second half, and the Many Labs 1 PDF was blocked (403), so human replication numbers there are second-hand.

1. Matched battery of layout effects on a reasoning model at equal tokens: STAYED OPEN. Closest is d01 (six 2026 models, 21,600 runs, defaults and social proof, reasoning on vs off) which shows pull persists (default OR 8.70, social OR 37.24). Nothing varies order, mark, framing and anchor together.
2. Permute-and-vote vs instruction-only guard vs canonical layout: STAYED OPEN for our items. d04 gives the nearest data (swap helps Flash +4.7 pp; merged CoT+rubric with swap +7.5 to +11.5 pp; plain swap costs 6.5-11.1 pp on clear-cut LLMBar pairs).
3. Neutral restatement meaning check: PARTLY. d14 (multi-framing consistency, 92% less framing disparity on BBQ) and d15 (framing words cause directional error up to 94%) show the lever, but no study audits that a rewrite keeps meaning. Still needs our own equivalence check.
4. Endorsement vs copy bias: PARTLY. d11 shows expert-labelled anchors bite and irrelevant hints do not; d07 shows endorsement a significant moderator for humans (b 0.32) and ease not; d02 shows no-deliberation models take defaults 97.5-99.9%. No marked vs unmarked sample-answer test found.
5. Lost-in-the-middle recent: PARTLY CLOSED. d05 (COLM 2025, six open models): U-shape strongest at or below half of the window, end bias beyond; d06: present at initialisation. No 2026 frontier reasoning model test found. Safe zones: start and end.
6. Many Labs and large replications: CLOSED at second-hand level (d09, d10, d16). Framing d = 0.60 in ML1, larger corrected estimates d about 0.3-0.5 across meta-analyses; anchoring replicated. Primary PDF not read.
7. Reasoning budget and nudges: CLOSED at abstract level. d03 (PNAS 2026 abstract opened; preprint shows o3-Mini takes defaults at 1.0 but resists late suggestions) and d01 (reasoning cuts defaults 92% to 86% but raises social proof 96% to 98%). Full PNAS text not opened.
8. Real human default effect: MOSTLY CLOSED. d07 original read: d = 0.68 (0.53-0.83), 58 studies, n 73,675, trim-and-fill goes up to 0.80, so the correction story differs from Mertens/Maier (unresolved, see K03). d08: Welsh opt-out did not raise deceased donor numbers (101 vs 104) and rest of UK rose as much. Johnson and Goldstein original not read.
9. Judges and self-candidate order swaps: PARTLY. d04: position bias 0.04 or less on current judges, style bias dominates; self-preference measured only partly. How many swaps before returns vanish: not found (two calls, one swap, was the design).
10. Persuasion-edited candidates: PARTLY. d12 (about 40% of 200 evaluations improved), d13 (exaggerated claims work, mere praise does not; Bing 2.5x; prompt-injection defences do not cover it). No tested code-side stripper found; untested idea only.

Corrections to earlier files: none needed beyond status changes. Unresolved: b04's 0.08 vs 0.03 sensitivity figure.
