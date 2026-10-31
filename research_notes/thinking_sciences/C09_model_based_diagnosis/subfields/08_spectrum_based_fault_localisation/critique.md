# Critique: Spectrum-based fault localisation (C09.08)

Cross-check of evidence_a, evidence_b, evidence_c (90 lines). Claims are in claims.jsonl (K01-K23).

## Re-opened sources and corrections

Re-opened this session: Abreu 2006 PDF, AutoFL (arXiv 2308.05487), AgentFL (arXiv 2403.16362), FlexFL (arXiv 2411.10714).

Confirmed:
- Abreu 2006: 132 versions provided, 14 discarded, 118 used; Ochiai about 5% better on average, up to 30% in specific cases; developer still inspects up to 40% in the worst case.
- AutoFL: acc@1 gain over Ochiai 19.7% (Defects4J), 166.7% (BugsInPy, GPT-3.5), 233.3% (GPT-4); 87.24 s per bug with five runs.
- AgentFL: 157 of 395 Top-1 on D4J 1.2, 28 more than LLMAO+Ochiai (129) and 36 more than ChatGPT+Ochiai (121), 77 more than Ochiai (so Ochiai = 80); D4J 2.0 (226 bugs) AgentFL 78 vs Ochiai 32 (46 more); ablation 148 / 125 / 133.
- FlexFL: Ochiai 167/316/389, Ochiai + LLM re-ranker 303/421/475, FlexFL 350/478/529 on 835 bugs.

Corrections and flags:
1. Abreu 2006 Table 2 (a02): the evidence row said "one program 10.5 / 7.3 / 1.0 / 2.0". The text layout shows these values belong to print_tokens (first row), then print_tokens2 20.0/17.5/13.9/16.4, replace, schedule, schedule2. The last two value rows (8.8/8.8/7.9/9.8 and 11.0/9.6/7.1/13.2) map to tcas and tot_info in an order the PDF text does not settle. Treat per-program labels for those two as unverified. The Ochiai-best pattern holds in every row regardless.
2. Ochiai baseline conflict (a22 vs a23/b21/c06): LLMAO's paper lists Ochiai Top-1 = 19 of 395 on D4J 1.2; AgentFL lists 80. Not both comparable (line vs method level, tie handling). Claim K19 is marked contested.
3. LLM4FL Top-1 is 326 in a25/b24 and 327 in c15/c16. Unresolved (versions of the paper); use "about 326".
4. a21 "XAI4FL" and "+68.4% over Ochiai": 197 vs 117 is +68.4%, consistent.
5. AgentFL D4J 2.0 number appears as "46 more than Ochiai" and "78 vs 32"; consistent.
6. Two cross-checker slips to note: the helper-script folder is shared, and running another agent's C09.08_mk.py regenerated evidence_c.jsonl identically (same 30 rows, only the timestamp changed). No content lost.

Not re-opened (time): Pearson 2017 numbers (opened by agents a and b who agree with each other, but both read the same paper, so not independent), Zou 2019, Rezaalipour and Furia 2024, FuseFL, LLM4FL, SemLoc, Callaghan and Fischer, Uddin, Gruber and Fraser.

## Contradictions between sources
- Ochiai baseline strength differs by paper (K19).
- Human studies: Parnin and Orso (no benefit) vs 36-professional follow-up (benefit) vs students (benefit only when fault ranked high). Never opened in full (K09 contested).
- LLM vs SBFL: AutoFL GPT-3.5 beats Ochiai at acc@1 but loses at acc@3/5; AgentFL beats Ochiai but loses to learned localisers; ordering rank across papers is not stable.
- Order effect: LLM4FL says DepGraph order best, Order Matters says Ochiai order no better than call-graph order (both agree Ochiai order is not special).

## Weak spots
- Independence: many "multiple" lines are the same paper described by two agents (Pearson, AutoFL, AgentFL, LLM4FL, FuseFL, SemLoc are each in 2-3 files). Counted as one source in claims.
- Almost all LLM results are Defects4J (Java, possible training-data contamination) or small student sets. Only SemLoc and BugT try to limit leakage.
- Most LLM papers are 2024-2026 preprints, many not peer reviewed; baselines are re-implemented by the authors.
- No study measures token cost matched against SBFL hint value. The only cost data: AutoFL seconds, AgentFL dollars per bug, Shi 2026 repair tokens.
- No study tests whether an LLM follows a wrong spectrum ranking (anchoring) directly.
- Industrial evidence (Philips) is four cases, authors call it debatable.

## Seen only in snippets or secondhand
- a11 (Jones 2002), a18 (Wong survey), b14-b17 (human studies, summaries only), c28-c30 (Abreu 2007, Parnin 2011, Jones 2005).
- b09 top-10 percentages from a garbled table.

## GAPS
1. At equal tokens, does a spectrum hint (Ochiai top-10) added to an LLM debugging agent beat the same agent given only the failing test output? (Only FuseFL and AutoCodeRover come close, both weak, GPT-3.5 era.)
2. Do strong 2025-2026 reasoning models (o3, Claude, Gemini 2.5+) gain anything from SBFL scores on real bugs, or do they ignore or over-trust them?
3. Does an LLM anchor on a wrong ranking? Test with a spectrum whose top item is not the fault (coverage collapse, SemLoc style) and measure recovery.
4. What is the best form of the hint: ranked list, scores, or covered-line diff between failing and passing runs? (Ordering and position bias evidence says the form matters a lot.)
5. For multi-fault programs, does iterative recompute (FLITSR) work in an LLM loop, and how many fix rounds before the spectrum is useless?
6. How do spectrum hints work on non-code reasoning (math or puzzle attempts as "programs" with pass/fail checks)? No study found; this is what our S5 needs.
7. How much do early termination, flaky tests and small failing-test counts degrade LLM-based localisation (only studied for classic SBFL)?
8. Contamination: how much of the LLM advantage on Defects4J survives on fresh bugs (BugT, SWE-bench Live style) when the SBFL baseline uses the same granularity and tie-breaking?
9. Resolve the human-study conflict by opening Parnin and Orso 2011, Xia 2016 and Xie 2016 in full, with N and conditions.
10. Do value-based spectra (data-flow, runtime values, SemLoc-style checks) justify their overhead for an agent that can simply print variables?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d18). Claims K24 to K35 were added; K04, K07, K09, K14, K16, K17, K20 and K22 were updated. Limits of this pass: the web-search quota ran out early and the arXiv, Semantic Scholar and OpenAlex search APIs returned 429, so papers were found through reference lists of papers already open, and gaps 5, 6, 7 could not be searched further.

Closed or mostly closed
- Gap 9 (human studies): Parnin and Orso 2011 and Xia et al. 2016 opened in full (d01 to d04). They do not directly contradict each other. Parnin: 24 + 10 students, 2 bugs, no mean gain. Xia: 36 professionals, 16 real bugs, large gains, but the list was simulated with the fault always in the top 10. Xie 2016 is closed access and stays unopened (d05); its N=207 is unconfirmed. K09 stays contested but now has the reason.
- K20 (Ochiai 19 vs 80): resolved by granularity. 19 is statement level (LLMAO Table 2), 80 is method level (AgentFL, SieveFL tables), 101/501 in Order Matters (d10, d12, d13). Status now established.
- Gap 3 (anchoring): answered for the repair setting with strong models (d08). Agents anchor on wrong hints (34.5 to 100%) but usually recover (34.8 to 95.9%); small models recover less. Not tested with a collapsed coverage spectrum itself.
- Gap 10 (value spectra): no justification found. SemLoc cost 2.2 to 3.0 times the tokens and did not beat one LLM call with the same inputs (81.4% vs 82.0%) (d14, d15). Open point: no study compares against an agent that prints variables.

Partly answered
- Gap 1 (spectrum hint vs failing output at equal tokens): still no direct study (K34). Nearest: AutoCodeRover +3 points for +8% tokens, one run, weak model (d06); Order Matters, same candidates, Ochiai order about equal to LOC order (d10); SieveFL, coverage as filter cut input tokens 49% at equal Top-1 (d13); SemLoc, failing-test output alone moves the LLM from 50% to 82% (d14).
- Gap 2 (strong reasoning models): indirect only. In 2026 repair agents (GPT-5.6 Luna, DeepSeek-v4 Flash, Gemini 3.1 Flash Lite) localisation hints changed pass@1 by -4.45 to +0.40 points and even gold hints gave +0.8 to +4.6 (d07). Plain Ochiai hints were not tested with o3 or Claude.
- Gap 4 (form of hint): no direct comparison of list vs scores vs covered-line diff. Evidence points to coarse grain and order-insensitive content (d10, d17, c21) and top-5 attention in humans (d04).
- Gap 8 (contamination): renaming cut Top-1 by 4 to 9% (d11) and the 19-vs-80 baseline problem is explained (d12). No LLM vs SBFL comparison on fresh bugs with matched granularity was found.

Still open
- Gap 5 (FLITSR with an LLM, rounds before the spectrum is useless): no study (K35, d18).
- Gap 6 (non-code attempts as programs): no study. Only the baseline that blame from one trace is weak, 14.2% step level on Who&When (d16, K31). A small own experiment is proposed in K31.
- Gap 7 (early termination, flaky tests, few failing tests for LLM localisation): no study (K35). SieveFL and AutoFL use only the failing test, which hints that passing runs matter less for LLMs, but that was not tested.

Other notes
- LLM4FL Top-1 326 vs 327 was not re-checked.
- The Abreu 2006 Table 2 row-label mix-up was not touched.
- d17 re-confirmed only from the abstract and intro this session.
- Suggested own test for S5 (K34): four arms at a fixed token cap: failing output only; plus unranked covered set; plus Ochiai top-5; plus a planted wrong top-1.
