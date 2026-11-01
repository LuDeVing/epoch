# Critique: E09.03 Mental model of the system (cross-check)

## Numbers re-opened (full text, this session)
Confirmed against the source text:
1. Li and Coblenz 2026: 12/57/13/18 percent time split, 1.65 fix-validate cycles, 9 of 17 tasks returned to model update, four unfinished sessions ended in model update, streamers vs participants median 9 vs 4 transitions (Mann-Whitney, p=0.014).
2. Ko et al. 2006: 19 minutes = 35 percent of non-interrupted time navigating; 88 percent of searches useless; about 36 percent on irrelevant code.
3. Ko and Myers 2004 Whyline: 7.8x faster (F(1,5)=12.64, p<.02); 40 percent more tasks (t(7)=3.0, p<.02).
4. Alaboudi and LaToza 2020: 3/27 (11), 9/35 (25), 15/38 (39) percent correct hypotheses; 5x odds at stage 2.
5. Olausson 2024 table: GPT-4 feedback 42.64/19.33/3.67 = 33.30 overall; human 62.21/45.67/14.67 = 52.60.
6. debug-gym table: Claude 3.7 SWE-bench Lite 37.2 / 48.4 / 52.1 (column identity read from a garbled table, order consistent with text).
7. Mehtiyev and Assuncao 2026: 44.0 vs 39.6 steps, 263 of 416 tasks; 51.5 and 31.5 pp LLM effect; framework gap 19.4 to 3.8 to 0.9 pp.
8. SWE-Bench+: 32.67 and 31.08 percent; 12.47 to 3.97 percent; 94 percent pre-cutoff.
9. Samir and Rahman 2026: MAP gains 23.33-38.57 percent, best document MAP 0.407.
10. Kim et al. 2026: 16,758 trajectories, 5 destroyed gold patches, all 5 recovered by checkpoint.

## Corrections
- a05 and b02 say backward tracing was "primary only for P1" and that P2/P5 used it less. The paper text says backward tracing "emerged as a dominant strategy" at coarse levels (version history, files, calls) and that P2, P3, P5, P6 often began root-cause analysis backward. c04 ("backward dominant P3, P4") is closer. Claim K15 was written from the paper wording, not from a05/b02.
- b03 gives "9 vs 4 transitions" without saying the contrast is streamers vs participants. It is a group difference, not a technique effect.
- b01/c01 "participants" includes both professionals and streamers; the 57 percent is a mean over 17 tasks, not an inferential result.
- Kim et al. 60-69 percent: the abstract says "SWE-Agent and OpenHands ... edit the correct functions yet" fail; the exact 60-69 range was not re-found in the abstract snippet read (taken from d05). Treat the range as probable.
- b25 is not an evidence line (a pointer); ignored.
- b22, b23, b24 are unopened stubs (Gugerty and Olson, Parnin and Orso, Beller) and were not used for any claim.

## Contradictions between sources
- Run length: Majgaonkar (failed runs longer) vs Mehtiyev (resolved runs longer within contested tasks). Mehtiyev shows a confounding reversal after controlling task difficulty (effect grows when controlled), so raw length comparisons mislead. Status: contested (K08).
- Hypotheses: Alaboudi shows explicit hypotheses help when prompted; Li and Coblenz show professionals do not form formal hypotheses and still succeed. Compatible only if prompting adds value to those who would not do it; no direct test.
- Debugger tools: debug-gym says tools help strong models; Debug2Fix says optional tools can lower scores unless forced. Aider results are mixed (o3-mini 95.2 to 94.2). The tool effect depends on whether the agent actually calls the tool.

## Weak spots
- Human evidence is small: Li and Coblenz N=12 (5 are streamers, not controlled), Ko N=10 analysed, Whyline N=9, Alaboudi N=20 in control arm. Several percentages are descriptive means.
- No study tests "mental model quality" as a manipulated variable in an LLM agent. LLM evidence is indirect: localization accuracy, trajectory analysis, debugger access.
- Models are mostly 2024-25. No 2026 frontier model in LocAgent, debug-gym, CodeSense. Effects may shrink at the frontier (Mehtiyev: framework gap 0.9 pp).
- Trajectory studies (Kim, Liu, Majgaonkar, Bouzenia) are correlational and use heuristic phase labels; Liu's gains were selected on stubborn instances.
- Time-share studies differ in method (think-aloud, logs, rules), so 35-70 percent comprehension figures are not comparable.
- Seen only in snippets or not extracted: debug-gym token counts (Figure 5), SWE-bench context-length numbers, Huang et al. per-benchmark values, Gugerty and Olson, Parnin and Orso, Beller. Scratch PDFs left under D:/research_scratch/E09.03 only as text; PDFs may be deleted.

## GAPS (most decision-relevant first)
1. Does a written, running system model (S2 note) raise fix rate at equal tokens over unstructured reading, on a clean, post-cutoff benchmark? No direct LLM test exists.
2. What does the model-update phase look like in agent traces by share of tokens (not action counts), and is 57 percent a good or bad target for an agent?
3. Does forcing probe-before-edit (Debug2Fix) replicate on other models and benchmarks, and is the gain due to the probe or to the delay?
4. Which parts of a model matter: static structure, dynamic behaviour, or causal explanation of the failure? Burkhardt suggests dynamic is hardest; no agent study separates them.
5. Do hypothesis lists help LLM agents as they do humans (Alaboudi 5-6x odds), and do they cause anchoring on the first hypothesis (Majgaonkar case)?
6. How do agents decide when to leave the model-update step (stop rule)? Step counts mislead (K08); what signal predicts that the model is good enough?
7. Is the 2026 frontier different? Do localization graphs (LocAgent) and debugger tools still add value for the strongest models?
8. How should a model be revised after a failed fix? Humans returned to model update in 9 of 17 tasks; do agents do this or only patch again (oscillation)?
9. Does compact S2 text beat full context at 100K+ tokens on real repositories, controlling for retrieval?
10. How much of the reported agent success on SWE-bench is leakage, and which of the above effects survive on contamination-filtered tasks?

## Gap search results
Web search quota ran out and the arXiv, Semantic Scholar and OpenAlex APIs returned 429, so the search was narrow. New evidence is in evidence_d.jsonl (d16-d23); claims K18-K21 added; K04, K05, K16 extended.

- Gap 1 (S2 note vs unstructured reading): STAYED OPEN. No direct test found (d22).
- Gap 2 (token share of model update): STAYED OPEN. Agentless (d21) shows a fixed localize-then-repair schedule works, but gives no token share of a model-update phase.
- Gap 3 (Debug2Fix replication; probe vs delay): PARTLY INFORMED. AutoSD (d16): real execution output matters, imagined output lowers plausible-patch rate 73% to 63%. This favours the probe reading, but is not a replication on other benchmarks.
- Gap 4 (static vs dynamic vs causal): STAYED OPEN (d23).
- Gap 5 (hypothesis lists for LLMs; anchoring): PARTLY CLOSED. AutoSD hypothesis loop equals a plain LLM on repair rate and adds a confidence signal (89% vs 82% correct with DONE). No human-style 5-6x odds effect in LLMs; anchoring on first hypothesis not tested.
- Gap 6 (stop rule): STAYED OPEN; only the schedule answer from Agentless. Generated reproduction tests were right 94 of 213 times, so they are weak stop signals.
- Gap 7 (2026 frontier): PARTLY CLOSED. SWE-Bench Pro (d17): best public 43.6%, commercial 17.8%; context overflow and endless file reading are main failure modes. No LocAgent or debugger-tool test at the frontier.
- Gap 8 (revision after failed fix): STAYED OPEN (d23).
- Gap 9 (compact S2 vs full context): STAYED OPEN; d17 (context overflow 35.6% for Sonnet 4) is indirect support.
- Gap 10 (leakage): CLOSED enough to act on. Same pair 19.25% on SWE-bench-Live vs 43.20% on Verified (d18); PatchDiff 7.8% false passes, 6.4 pp inflation (d19); issue-text-only file naming 76% vs 53% (d20). Any S2 test must use post-cutoff tasks and differential tests.
