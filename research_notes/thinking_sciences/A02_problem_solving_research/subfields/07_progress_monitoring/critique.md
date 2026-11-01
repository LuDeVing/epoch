# A02.07 Progress monitoring: cross-check critique

## Corrections made (sources re-opened this session)
Re-checked against the arXiv PDF text: ToT (Game of 24: 7.3 / 4.0 / 9.0 / 45 / 74), Reflexion (130 of 134, +22% AlfWorld), Huang 2023 (GPT-3.5 and GPT-4 rows), DEER (R1-Distill-Qwen-7B 64.2 to 69.2, length 61.5%; Qwen3-14B 82.8 to 83.7, length 57.1%), Zhang 2025 probe (threshold 0.85, 88.2%, 24% fewer tokens), Kadavath 2022 (0.928, 0.864, 0.687), Cao 2026 (48.3 to 56.9, 2.4 attempts, $0.78, SD .048).
- All confirmed. Small notes, no number changed:
  1. c05: Huang's table column is "# calls" (1, 3, 5), not "rounds"; the CommonSenseQA 75.8 to 38.1 drop is at 3 calls. GPT-4 CommonSenseQA stays 82.0, 79.5, 80.0 (no collapse, unlike GPT-3.5). Do not generalise the collapse to GPT-4.
  2. c14: the LiveCodeBench v6 gain +10.0 is the OVERALL figure; Hard +19.6 and Easy -0.7 are the splits (the Hard/Easy pairing in the line should be re-read against Table 5; the PDF layout was garbled).
  3. b04: solution times (38 s) cannot be from 15 s videos; unit unresolved (b04 already flags it).
  4. b01 duplicates a01-a04 (Metcalfe & Wiebe) and was only seen in a summary; a01-a04 are the authoritative lines. Hedne b02/b03 duplicate a06-a08.
  5. a22: Davidson (1995) 12-13% is second-hand.

## Contradictions
- Warmth shape: Metcalfe & Wiebe 1987 (flat/abrupt before insight) vs Hedne 2016 (no difference, d=.12) vs Kizilirmak 2018 (supports when insight = Aha report). Insight definition (problem type vs report) and rating density explain much of it.
- Metacognitive discrimination for insight answers: Hedne Az .56 (chance) vs Ishikawa AUC .90 (N=10, object recognition). Different task and N.
- Webb 2016 and Wiley & Miller 2026 say Aha belongs to the solver and the outcome, not the problem; this undercuts the 1987 problem-type framing.
- Kizilirmak b05 reports 2.59 vs 1.43; a12 reports the same test. No conflict.

## Weak spots
- The human core is thin: only one 1987 founding study, small N, one-tailed tests, many subjects dropped.
- The named key works for this subfield (MacGregor/Ormerod/Chronicle 2001-2002, Novick & Sherman 2003, Durso anagram, Smith & Kounios 1996) were NOT opened. The anagram solvability judgment claim in the focus line has no evidence here.
- LLM early-stop papers measure token savings on math benchmarks; they do not test a "no progress" trigger in open-ended agent work.
- Several 2026 LLM entries (b24, b25) are abstract-only; c11-c13, c21 lack author names.
- No head-to-head of hard count rules vs graded confidence rules.

## Only seen in snippets
b01 (summary), a27, a28, b24, b25, c24 (negative search result), c25 (synthesis, not a source).

## GAPS (most decision-relevant first)
1. Does a code-set count rule (N repeats / M steps without new information) beat a graded confidence trigger at equal tokens on our agent's tasks?
2. What do MacGregor, Ormerod and Chronicle (2001, 2002) actually report: criterion-of-progress numbers, and does the nine-dot/eight-coin data support a fixed progress criterion?
3. Do anagram solvability judgments really improve with time (Novick & Sherman 2003; Smith & Kounios 1996 all-or-none finding)? Exact numbers.
4. Can graded self-rated progress inside one LLM solve be made informative (Cao shows within-problem SD .048)? Does external signal (answer stability, test pass) do better?
5. What false-trigger rate do repetition and answer-convergence rules have on long open-ended agent traces (not math)?
6. After a no-progress trigger fires, which response works best (switch strategy, restart, ask, stop)? Any controlled comparison?
7. Is there a human analogue to the LLM "underthinking" failure (leaving a promising line too early), e.g. in Ormerod/Chronicle or foraging/patch-leaving work?
8. Do the Hedne (2016) design differences (confidence criterion, rating density) explain the failed replication? Any direct re-test?
9. Are there LLM studies after 2024 that elicit warmth-like ratings from a model mid-solve and test whether they rise before success?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d31). Claims K19, K16, K13 and K17 were updated; K20-K29 are new. The shared web search quota ran out early, so arXiv, Semantic Scholar and OpenAlex APIs (rate limited) and Europe PMC and a paper-search API were used instead. Publisher paywalls blocked the 2001, 2002 and 2003 papers.

1. **Count rule vs graded trigger at equal tokens: still open (partial).** No head-to-head on agent tasks. Closest: EAT on math (graded signal beat a fixed token cap and an answer-count rule; d20), Cao N=100 (learned FOK/JOL 47.0 vs hand rule 42.0, intervals overlap; d21), OnTrack on SWE traces (simple loop/stall rules matched the full monitor; d14). New claim K23, status contested.
2. **MacGregor/Ormerod/Chronicle numbers: partly closed.** The criterion is now defined (nine-dot: dots remaining over lines available; failure widens search; d01, d03) and the matchstick test numbers are in (d02). The 2001 tables and 2002 eight-coin rates were NOT read (paywalled). Second-hand: 80-93% solved simpler variants, nobody solved the nine-dot in Exp 1 (d04). Ollinger 2013 gives a competing account for the eight-coin data (d06). K25 contested.
3. **Anagram solvability judgments: stays open.** Smith & Kounios 1996 (abstract) found little or no partial information, an all-or-none shift (d07, d08). That runs against a gradual nearness signal. Novick & Sherman 2003 was not opened (d09, opened false). The focus-line claim remains unsupported (K19, K26).
4. **Graded self-rating inside one LLM solve: mostly closed (no).** Cao's within-problem SD .048 vs .270 re-read (d22). External signals do better: hidden-state probes predict failure from round 1 (AUC .86 and .81, d23); behaviour-only features were weaker (9.9% vs 41.6% tokens saved). A harness-enforced count of "useless" judgments works where self-report does not (d18). K24 and K20.
5. **False-trigger rate on open-ended traces: partly closed.** OnTrack flags 13-21% of benign SWE traces at the shipped point and 29-32 of 40 for weak variants (d15). Loops are 2.18-3.59% of production trajectories (d12) but 26-57% of CodeGym episodes under context compression (d16). Detectors trained on injected faults fall to chance on organic failures (d29). Still no false-trigger rate for a pure repeat-count rule on long non-coding traces. K22.
6. **Best response after the trigger: partly closed, no single controlled comparison.** Enforced switch beats suggestion (d18, d19); Loop Breaker with escalating forced switches helps loop-prone models (d17); bare rewind can hurt while rewind plus carried lessons helps (d28); compact feedback beats the full failed trace (d21); a nudge recovers 79-91% but 37% of failures ignore it (d13). No study compares switch, restart, ask and stop head to head. K29.
7. **Human analogue of underthinking: not found.** Humans overharvest (d10) and persevere on dead ends (d11). LLM underthinking has a monitor-and-backtrack fix (d30, abstract only). K27.
8. **Hedne design differences and any re-test: stays open.** No direct re-test found in Europe PMC or the paper search; 2026 Aha-rating papers only cite Hedne (d31, negative result).
9. **LLM warmth-like ratings mid-solve: stays open (none found).** Nearest: spontaneous text 'aha' shifts do not predict success (d24), forced reconsideration under high entropy helps (d25), premature confidence is a risk flag (d27), internal belief rises earlier than text shows (d26). K28.

### New cautions for later stages
- Do not read d02 or d03 as clean support for a fixed threshold; the 2001 and 2002 papers were not opened.
- d09, d31 are opened:false. d05, d06, d07, d27, d29, d30 are abstract-page reads only.
- The strongest design finding is K20: enforce the response in code; do not rely on the model to act on its own no-progress judgment.
