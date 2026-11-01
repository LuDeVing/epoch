# Critique: F02.07 Epistemic actions (cross-check, 2026-11-01)

## Corrections and confirmations (sources re-opened this session)
Re-opened and confirmed against the text:
- Kirsh and Maglio 1994 Table 1 (13.18/13.69/15.65 vs 19.04/19.33/20.05), and "each zoid rotated more than half its possible rotations" (1.5 expected for 4 orientations). Confirmed. Exact bar values for Fig 6 and 7 are still not readable.
- ReAct (arXiv 2210.03629): ALFWorld best ReAct 71%, best Act 45%, BUTLER 37%, worst ReAct trial 48%. Confirmed.
- Huang et al.: GPT-3.5 GSM8K 75.9/75.1/74.7 and CommonSenseQA 75.8/38.1/41.8. Confirmed.
- Olausson et al.: feedback repair rates 33.30% (own) vs 52.60% (human), 42.64/19.33/3.67 and 62.21/45.67/14.67 by difficulty. Confirmed. The 1.05x and 0.97x ratios appear in the grids, but each depends on the exact (initial samples, repairs) cell; treat as example cells, not a headline for all budgets.
- Krishnamurthy et al.: suffix failure in more than 60% of GPT-4 basic-prompt replicates. Confirmed.
- Agentless: 25.67 to 32.0% and $0.70 per issue, upper bound 126 (42.0%), gains plateau near 40 samples. Confirmed.
- Chen et al. Self-Debugging: MBPP baseline 61.4/67.6/72.8 vs trace 66.2/69.2/76.4. Confirmed.
- QuestBench: 99.39% GSME-Q and 84.05% GSM-Q on a subset; Logic-Q and Planning-Q 40-50%. Confirmed.
Not re-checkable (no open copy, Semantic Scholar rate-limited): Maglio and Wenger 2000, Maglio, Wenger and Copeland 2003, Maglio and Kirsh 1996, Kirsh 1995 coin counting.

## Flags (not corrected, because the source was not re-read)
- Maglio and Wenger 2000 (b07, d01): accuracy .86 vs .53 reported with t(59)=33.85, RT 869 vs 1791 ms with t=2.01. A 922 ms effect with t of only 2.01 and an accuracy effect with t of 33.85 look swapped or mistyped. Also df 59 does not match N=30. Treat the t values as unreliable; the direction (preview helps) is not in doubt.
- Kirsh 1995 coin counting (a19): aggregate p values read "p<.4" in the text; N=5.
- Kirsh 1995 gives internal rotation as 1000-1800 ms; the 1994 paper gives 800-1200 ms. Two numbers for the same quantity.
- Duplicate entries of the same papers (b07/d01, b08/d02, a28/b19/c05/c24, a26/b24, a27/b20/c06) are not independent sources; claim source counts treat them as one.

## Contradictions
- Skill and epistemic action: Maglio and Kirsh 1996 (N=2) say extra rotations rise with skill; Destefano and Gray 2007 (poster, N unstated) say complementary actions fall with expertise at matched speed. Unresolved, and both are weak (K02 marked contested).
- Self-repair: Chen et al. (+8 to 12%, matches 16-sample baselines) vs Olausson et al. (about 1.0x at equal budget) vs Huang (intrinsic correction hurts). The difference is feedback source and budget accounting.
- QuestBench: strong models over 80% on algebra, under 50% on logic and planning, so "LLMs can ask the right question" depends on domain.

## Weak spots
- The human core of the field is one lab (Kirsh, Maglio, Wenger) with tiny samples (N=2 to 5 in the key skill and coin studies; 3 players in the mental-rotation pilot). No independent replication of the preview experiments (d03). Kaye 2013 thesis (N=13/13/14) is about mental rotation transfer, not epistemic action.
- The mapping from Tetris rotation to LLM code probes is an analogy. No named-term LLM test exists (K16). Most "LLM evidence" is about tool feedback in general; it does not isolate the probe-before-attempt decision.
- Many LLM numbers concern selection or verification (Agentless, SWT-Bench) rather than steering, so benefit may come from reranking.
- Evidence with opened:false, seen only in snippets or abstracts: a23, a24, a25 (Friston), b09, b15 (Neth and Payne 2002), b16 (Gray and Fu 2000), b25, c25, c26, c27, d03, d17 (notes). Do not cite their content.
- Model versions in 2026 entries (GPT-5.4, Claude Sonnet 4.6, etc.) come from preprints I did not independently re-read here.

## GAPS
1. At equal tokens, does probe-first (run code or a toy case before a full attempt) beat attempt-first for a current model, and on which task types does it lose?
2. Does probe benefit come from steering the next attempt or only from selection and reranking (Agentless and SWT-Bench confound these)?
3. How should the agent decide to probe at all: is a value-of-information check (EIG vs cost) better than a fixed rule, given tool overuse over 30% of the time (d13)?
4. Do probes help more as task difficulty or hidden state grows, and do they stop helping for strong models (gap shrinks with model strength in b21, GSM-Q saturation)?
5. Was the Maglio and Wenger 2000 statistic correctly reported, and has anyone outside their lab replicated the preview effect with N above 30?
6. Does epistemic-action use rise or fall with skill (Maglio and Kirsh 1996 vs Destefano and Gray 2007), and what does that predict for agent probe rate as it gets familiar with a task?
7. Which probe kinds pay off most: running code, printing intermediate state, a tiny test, or asking the user (clarification vs world probe)?
8. Is there any LLM study using the term epistemic or complementary action with measured results beyond the 2026 position paper (c01)?
9. What does a probe cost in context (history resending, 11-12x uncached in c21), and does carrying probe output forward hurt later reasoning?
10. Can an agent tell when a probe result is misleading (partial or wrong tool output), given self-correction fails without a reliable external signal?

## Gap search results (2026-11-01, evidence_d.jsonl d18-d34, claims K21-K29)
Evidence ids d01-d17 from the earlier pass were kept because claims cite them; d18-d34 are new. Claim ids K17-K20 are cited in UNKNOWNS.md but do not exist in claims.jsonl; new claims start at K21.

| Gap | Status | What was found |
|---|---|---|
| 1 Probe-first vs attempt-first at equal tokens | OPEN | No matched-budget study found (d34). Adjacent: PaT try-first-then-plan beats plan-first, 83.13 vs 81.18 Pass@1 at 4.85 vs 8.31 cost (d28); interaction beats per-step thinking by 1-3 points for a 12B web agent (d23). Where probing loses is not measured. |
| 2 Steering vs selection | PARTLY CLOSED | Google BRT: reproduction test as input gave plausible fixes on 17 of 23 bugs vs 13 of 23, 33% vs 2% per run (d22). Upper bound, because the test was oracle-filtered; 23 bugs. New K21 (single-source). |
| 3 Deciding to probe | PARTLY CLOSED | Agents both under-use (simulator under 1%) and over-use (over 30%; ASK about 2x planner) tools (d20, d13, d26). A gate on a failed outside check was cheaper and better (d28). No tested value-of-information gate for code probes. K24 established, K25 single-source. |
| 4 Difficulty and model strength | OPEN, CONTESTED | CodeAct gains widen with model ability (d27); belief queries help a saturating model little (d19); success falls from 66-73% easy to 4.8-19% hard (d21). K27 contested. |
| 5 Maglio and Wenger statistic; replication | PARTLY CLOSED | The odd t and df values are printed in the original (d01), so they are not our transcription error. No independent replication with N above 30 found (d33); search was limited. |
| 6 Skill direction | CLOSED toward "falls or humps" | Destefano, Lindstedt and Gray 2011, N=59 players, 173 games: complementary actions fall with skill, lenient rules show a hump (d18). The old 'rises with skill' rests on two players. K02 stays contested but the weight has moved; new K23. Classification by log rules is a caveat. Prediction for the agent: probe more when the task type is new, less once familiar. |
| 7 Which probe kind pays most | OPEN | Only the action format was compared (code beats JSON/text, d27). No study ranks run code, print state, tiny test and ask-user against each other. K29. |
| 8 Named-term LLM studies | PARTLY CLOSED | Found one with experiments citing Kirsh and Maglio (belief queries, figures only, d19) and one with ASK actions (d26). Neither tests probe-before-attempt. K16 updated. |
| 9 Context cost of probes | CLOSED for software agents | Masking old tool output cut cost by over half with no loss (52% cheaper, +2.6 points on Qwen3-Coder 480B); summaries lengthened runs (d24). K26. |
| 10 Misleading probes | PARTLY CLOSED | Own-reproducer pass but real-test fail in 17-30% of open-process agent patches (d21); models copy silently wrong tool output, up to 47% below no-tool best, warning gives up to +30% (d25). Both are 2024-era models. K22 established. A free doubt cue recovers about 15% of failed runs but net effect unknown (d31). |

Still unread or unreachable: Kirsh 1995, Maglio and Kirsh 1996 full texts; the IBM 'self priming' paper; OpenAlex and Semantic Scholar were rate-limited, so absence claims (gaps 1, 5, 7) are weaker than they look. Exact per-condition values for d19 are only in figures.
