# Critique: Soar operator selection, impasses and impasse types (C02.01)

Cross-check of evidence_a, evidence_b, evidence_c (93 lines, 21 claims written to claims.jsonl, ids C02.01-K01 to K21).
Sources re-opened this session by the cross-checker: NL2GenSym (arXiv 2510.09355, PDF text), STARS (2306.06770, HTML), CogRec (2512.24113, HTML), Tree of Thoughts (2305.10601, PDF), Huang et al. (2310.01798, PDF), Zhu and Simmons (2403.00810, PDF), PALADIN (2509.25238, PDF), Laird 2022 (2205.03854, PDF), Soar Manual chapters 2 and 4 (HTML).
Not re-opened: Reflexion (c20), AgentDebugX (c27), Shepherd (c28), Chain-in-Tree (b19), Kirk 2023 (a26), Mohan 2012 (a28), and everything marked opened:false.

## 1. Ten numbers re-checked

| # | Number | Result |
|---|---|---|
| 1 | NL2GenSym success: Flash+framework 86%, qwen 91%, manual 84%, one-shot 55% (Gemini Pro) and 66% (qwen), zero-shot 0 | Confirmed (Table II). Hard cases: manual 46.67, one-shot 20 and 46.67, framework 76.67 and 86.67. Average minimum cycles 7.97; 1.76x and 1.98x confirmed. |
| 2 | NL2GenSym ablation: -23 overall, -37 hard and variant, -17 basic KB, -14 case KB | Confirmed in text. Correction of wording: the paper writes "23% reduction" and never says points or relative percent. Our a22 and b11 say "points"; treat as unstated. |
| 3 | NL2GenSym "Pro about 2,500x optimal cycles" | Confirmed (2552.63x in the table; text says 2500x). |
| 4 | STARS completion 52.5/66.7/35.7 to 77.5/94.4/92.9 | Confirmed (Table 2). |
| 5 | STARS tokens 41,407 to 139,871; 17,078 to 61,808; 12,992 to 76,056 | Confirmed. Ratios 3.38x, 3.62x, 5.85x. |
| 6 | STARS ablation ST 50.0/66.7/21.4, STS 40.0/66.7/21.4, STAR 77.5/77.8/64.3 | Confirmed. New detail: in kitchen the selection step (STAR to STARS) adds 0 points for +13,785 tokens; it matters in groceries (+16.6) and office (+28.6). |
| 7 | CogRec HR@10 ML-1M 0.3124, LLM-Direct 0.2901, GPT4Rec 0.2956, Soar 0.0511; gains 4.1 to 9.1% | Confirmed from the table. a25 was wrong (see section 2). |
| 8 | Tree of Thoughts Game of 24: IO 7.3, CoT 4.0, CoT best of 100 49, ToT b=1 45, b=5 74; tokens 5.5k vs 6.7k, $0.74 vs $0.47 | Confirmed. Crosswords 60% word-level, 4 of 20 games confirmed. |
| 9 | Huang: GPT-3.5 GSM8K 75.9 to 74.7, CommonSenseQA 75.8 to 41.8, HotpotQA 26.0 to 25.0 | Confirmed (Table 3, 5 calls row). GPT-4 also drops (GSM8K 95.5 to 89.0). |
| 10 | Manual: Soar 9.4 arithmetic agent learns 1263 rules, 9.6 learns 8; four impasse types; Laird 2022 text 3 types, glossary 4 | Confirmed all three. |
| 11 | PALADIN recovery 89.68 vs CRITIC 76.34, ToolBench 32.76, vanilla 23.75 | Confirmed in Table (Gemma-3 12B). Paper's own abstract also prints "89.86%" once, an internal typo. |
| 12 | Zhu and Simmons find 14/15 vs 15/15, 12/15 without LLM, tokens 54,754 vs 917 | Partly confirmed. The numbers exist but the extracted table is scrambled, so which cell belongs to which row/agent is inferred, not read. Success counts (14/15, 15/15, 12/15) and p-values 0.446, 0.347 for steps are clear. |

## 2. Corrections made

- a25: said LLM-Direct = 0.2815 on ML-1M HR@10. Wrong. 0.2815 is SASRec; LLM-Direct is 0.2901 and second-best is GPT4Rec 0.2956 (so +5.7% is over GPT4Rec, +7.7% over LLM-Direct). c07 had it right.
- c07: said gain "+4.4% to +9.1%". The table's Improve row runs from 4.1% to 9.1% (b15 and a25 had 4.1). Use 4.1 to 9.1.
- a27: object counts "58 unique objects (35 kitchen, 12 office, groceries by subtraction 11)". Wrong. The appendix lists 35 kitchen objects, 15 grocery objects and 12 office objects (11 appliances and 7 furniture items are locations, not objects).
- b12: "10 runs per task". Only the STARS condition was repeated 10 times (means 77.5, 93.89, 92.14; SD 2.04, 1.76, 2.26). Table 2 (all conditions) is one run each. c21 stated this correctly.
- a22/b11: "points" vs paper's unmarked "%" (see row 2).
- b13: "STARS selection failure blamed on missing task context" is right, but the full gain is zero in kitchen, not "small".

## 3. Contradictions between sources

1. How many impasse types. Laird 2022 main text: 3. Laird 2022 glossary: 4. Manual contents: 4; manual overview paragraph: 3; manual detailed section: 4, with no-change split in two. NL2GenSym critic: 5. Constraint-failure has 0 mentions in Laird 2022 main text. No source is wrong; the count depends on the grouping. (K02)
2. Can preferences always remove an impasse? Laird 2022 footnote 4 says yes, even if it means copying operators. The Manual says a constraint-failure impasse "cannot be resolved by additional preferences". The Manual is the later and more specific text. (K03, contested)
3. Laird 2022 says time-bounded substates give a random or non-optimal choice; the Manual says nothing opened here about a time bound. Neither is measured.
4. Soar-style systems and equal-token comparisons. ToT reports an equal-completion-token comparison against best-of-100 CoT (74 vs 49, but $0.74 vs $0.47). STARS and NL2GenSym report no equal-token control at all. The only evidence that structure beats sampling at equal cost is therefore ToT, a system with no impasse typing.
5. Fan and Lan 2026 say the full Soar bundle is absent from modern LLM agents, while CogRec, STARS and Zhu and Simmons each implement part of it inside Soar-hosted agents. Not a conflict: those are Soar agents that call LLMs, not LLM agents with Soar's control structure.

## 4. Weak spots

- Same-lab dependence. Laird 2022, the Manual and Laird 2021 are one group; Kirk 2023, Kirk 2024 and Wray 2021 are one group. "Established" in K01, K05 for the Soar mechanics means two documents from related authors, which is adequate for a description of a design but not for a performance claim.
- No equal-token test of any impasse-driven scheme against sampling plus a code check. This is the main hole for our G7.
- No ablation by impasse type anywhere. CogRec's example is a tie; NL2GenSym's example is a state no-change loop; STARS has no impasse mechanism at all (a Soar agent calling an LLM when a goal is unknown). Nothing shows that the type of the impasse did any work.
- Small, toy or simulated settings: Water Jug (100 cases, one run), simulated kitchen and office (3 tasks), MovieLens/Amazon/Yelp (no variance, no seeds, no significance), Game of 24 (100 games), crosswords (20 games).
- CogRec ablations and long-tail results are in figures only; no numbers read. Baseline inconsistency: pure-Soar baseline has about 20 hand rules, the no-bootstrap ablation 5, the full system about 500.
- NL2GenSym's manual baseline was deliberately basic rules without search control; the 84% and 3390x are a floor, not an expert benchmark.
- PALADIN and AgentDebugX are about tool failures and run-level failure attribution, use LLM simulators and graders, and need training for PALADIN. Distance to our setting is large. A 2026 follow-up snippet (c26: logistic regression matched annotated recovery 63.6% vs 43%) was only a search snippet and is unverified.
- Chain-in-Tree (b19, 75 to 85% savings by gating branching) was read through a page fetch and has only 100 items per benchmark; it is the best support for "branch only on need" but is thin.

## 5. What was seen only in snippets (opened:false)

Laird, Newell, Rosenbloom 1987 (a32); Laird 2012 book (a33); Laird, Rosenbloom, Newell 1986 chunking (a34); Nason and Laird 2005 Soar-RL (a35); Brown and VanLehn 1980 repair theory (b25); Tambe, Newell, Rosenbloom 1990 expensive chunks (b26); Standard Model of the Mind (b27); "Recovery Is a Decision" (c26); Illusion of Thinking, abstract only (c30). The user's brief named Laird 2012 and the 1987 founding paper; neither was read. Everything we say about universal subgoaling comes from Laird 2022, a 1988 secondary report (a31) and the Manual.

## GAPS

1. Does the type of impasse matter for an LLM agent? Run one generic recovery operator against impasse-typed operator selection (tie: compare candidates; no-change: reframe or retrieve; conflict: find the discriminating test; constraint-failure: relax or abandon) at equal tokens. No source does this.
2. At equal tokens, does generate-run-critique (NL2GenSym) or analyse-repair-select (STARS) beat best-of-N plus a code check? Neither paper has a matched-cost control, and STARS costs 3.4x to 5.9x the tokens.
3. How good are code-fired impasse triggers (same error twice, no change over 2 rounds, budget fraction) compared with model-stated "stuck" signals, and how often is a fired trigger a false alarm (the operator no-change ambiguity: stuck vs slow)? No LLM-agent source measures trigger precision or recall.
4. What does isolating a subgoal's context actually buy? Is a fresh context returning only a typed result better than a shared context at equal tokens, and does it reduce anchoring on earlier failed attempts? Soar's isolation is architectural; no LLM study isolates this factor (Fan and Lan list "parent isolation" as a missing piece).
5. Does storing the fix from a solved subgoal (the chunk analogue) help on later items of the same class, and when does retrieval cost or over-general fixes erase the gain (expensive-chunk effect, over-general justifications)? Only CogRec (figures) and Zhu and Simmons (toy) show call reduction; no accuracy-at-equal-tokens result.
6. Are there replications or critiques of CogRec, NL2GenSym and STARS (2024 to 2026) with variance, seeds or other domains? None found; all three are single-lab with single runs for the main table.
7. What is the base rate of each impasse type in LLM reasoning traces? Laird 2022 and the Manual give mechanics, not frequencies. Counting how often our scaffold meets a tie (several passing candidates), no-change (no progress) or conflict (checks disagree) on our benchmarks decides whether typing is worth building (the Ohlsson note in the schema says impasse may be only about 8% of problems).
8. What do Laird 2012 (the book) and the 1987 founding paper say about universal subgoaling, the decision procedure's eight steps and the claimed link between impasse type and search method, beyond Laird 2022? Both were unreadable this run.
9. Does the "all impasses can be resolved by more preferences" claim (footnote 4) hold in practice for LLM agents, or do hard-constraint contradictions need a dedicated fallback beyond G6? Test with seeded contradictory constraints.
10. Is time- or token-bounded subgoal reasoning (Soar's stated fallback to a random or non-optimal choice) better than unbounded recursion at equal total tokens, and what depth cap is right? Stated by Laird, never measured.

## Gap search results

Evidence in evidence_d.jsonl (d01 to d17); claims K22 to K31 added, K13 and a few others got extra evidence ids. Search limits: the web search budget was used up, Semantic Scholar and OpenAlex returned 429, the disk filled up late in the run, so a few downloads were skipped. No gap was closed outright; none of the ten asks for something the literature has measured directly. Three are narrowed.

| Gap | Result | What is now known |
|---|---|---|
| 1 Typed vs generic recovery | Open, narrowed | No typed-vs-generic test exists. Feedback quality is the bottleneck of repair loops (K22, established): a typed operator helps only if it improves the diagnosis. Score by diagnosis accuracy. |
| 2 Equal-token repair vs best-of-N | Open, narrowed | Olausson 2024 is the one matched-budget test: repair is often equal or worse than resampling, more first samples beat more repairs. Snell 2024: revisions beat parallel only with a trained revision model and verifier, mixing saved up to 4x. K23 is contested. NL2GenSym and STARS themselves are still untested at equal cost. |
| 3 Trigger precision | Open | OpenHands uses 3 and 4 repeat thresholds, no precision or recall reported (K26). Model-side signals are poor (K27, established). Our "same error twice" is more aggressive than that threshold, so log false alarms. |
| 4 Context isolation | Open, evidence leans for isolation | Lost-in-conversation, Snell and the Context-Folding and THREAD results all point the same way, but none isolates the factor (K24, K25). Cheapest clean experiment on the list. |
| 5 Stored fixes | Open, partly informed | Agent Workflow Memory gives accuracy gains and shorter runs, with authors warning about wrong workflows (K28). No equal-token result and no retrieval-cost result. |
| 6 Replications | Open (negative search) | Nothing found, but only NL2GenSym could be checked in a citation index (empty); CogRec and STARS lookups failed (K31). |
| 7 Impasse frequencies | Open | MAST shows loop-like failures at about 12 to 16% of labels in multi-agent systems, with no tie or conflict category (K29). Count in our own logs. |
| 8 Laird 1987 and 2012 | Open | Both still unreachable (certificate error, 404s). Needs a person with library access. |
| 9 Contradictory constraints | Open, supportive | MiP-Overthinking: models given unsolvable questions spend 2x to 4x tokens and mostly fail to abstain. This is missing premises, not contradictions, but it argues for a code-fired exit beyond G6 (K27). Seeded test still needed. |
| 10 Depth and token cap | Open | Context-Folding uses depth 1 and 10 branches; THREAD ran to depth 10 uncapped; s1 reports a 30K cap with a forced answer slightly helps (N=30). No sweep exists (K30). |

Caveats on this pass. MAST percentages come from the paper text because the figure text was scrambled; the Context-Folding table was scrambled so only text numbers were used; Kamoi 2024 was read at abstract and introduction level only; the s1 uncapped baseline number was not read. The disk-full condition prevented reading the "How Memory Management Impacts LLM Agents" paper, which bears on gap 5.

Net for the build: the evidence supports code-fired triggers, a fresh typed-return subgoal, and an equal-token best-of-N control. It does not yet support impasse typing as a source of gain. Run the cheap tests first: the isolation ablation (gap 4), the trigger false-alarm log (gap 3) and the impasse frequency count (gap 7).
