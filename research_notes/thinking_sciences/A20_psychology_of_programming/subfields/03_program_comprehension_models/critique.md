# Critique: A20.03 Program comprehension models (cross-check)

## Numbers re-opened this session (full PDF text read with pdftotext)
Confirmed with no change:
1. Agentless (2407.01489): 32.00% (96 fixes), $0.70; file localisation 78.67 / 70.33 / 81.67%; skeleton 58.33% vs complete file 53.67%; edit locations 49.67%. (c20)
2. SWE-agent (2405.15793): 100-line viewer 18.0, 30-line 14.3, full file 12.7; summarized search 18.0, iterative 12.0, none 15.7; last-5 obs 18.0 vs full history 15.0; 90.5% -> 57.2% after one failed edit. (c22)
3. REval (2403.16437): average accuracy 44.4%, IC 10.3 (abstract); GPT-4-Turbo path 57.7, avg 75.0, IC 42.5; GPT-3.5 avg 55.7; CoT on CodeLlama-7B: path 10.8 -> 21.4, output down 6.8. (c14)
4. Wyrich, Bogner, Wagner 40-years mapping (2206.11102): 95 papers, median 34, range 5-277, 53.7% students only, 9.5% professionals only, 47% Java, 6 of 25 between-subject balanced (24%), one qualifying replication (Fucci et al.). (b20)
5. When Names Disappear (2510.03178): class summary GPT-4o 87.3 -> 58.7, Qwen3-Coder 87.2 -> 72.1, DeepSeek V3 87.7 -> 76.7, Llama 4 86.2 -> 66.4; ClassEval pass@1 85.7 -> 76.1; LiveCodeBench 85.4 -> 71.2. (c12)
6. Liu et al. coherency (2510.15079): 81.42% coherent, 46.92% of those correct; consistency strong 5.76 / weak 45.37 / random 48.87; 361 suspicious. (c15)
7. Kaufman et al. 2026 (2607.08885): 86 programmers; 73.9% vs 49.0%; top-down 31/50; intuition 12/50; 18/29 negative examples, 14/18 to confirm a hunch. (c01-c03)

Clarifications (not errors):
- REval: "44.4 / 10.3" are averages over models in the abstract. In the PDF table the same pair also sits beside a CoT row because of a layout overlap. Read it as the all-model average. The "execution path 19.4%" in c14 is the average of that column and was not independently isolated. Mild risk.
- a17 (1,138 tasks) and b15 (974 MBPP tasks): consistent, because 164 HumanEval plus 974 MBPP is 1,138. Not a conflict.
- a21 and b17 (Richards and Wessel): overall ToMMY effect is null (0.05, p=0.61); the split effects (+0.34 / -0.28) are subgroup results on 28 observations and should not be treated as findings.
- b18 and c01-c03 (Kaufman): same paper counted twice; they are ONE source. Claim K14 is therefore single-source.

Not re-opened this pass (rate limits: arXiv search and OpenAlex returned 429, Semantic Scholar not tried to avoid more load): Ko and Uttl 2003 numbers (1.00 / 1.65 / 2.00 bugs, N=75), Koenemann and Robertson 1991 (N=12, 24% of procedures), von Mayrhauser and Vans 1997 counts (N=4), Burkhardt 2002, Peitek 2020, Wagner and Wyrich 2021, Langhout 2021, Lehmen 2026. These stay as the earlier agents recorded them (opened:true there).

## Contradictions and tensions between sources
- Strategy is not tied to expertise the simple way Qiao et al. (a23, c10, c25) say. Ko and Uttl: the most experienced cluster was breadth-first. Busjahn/Peitek: experts read less linearly. Kaufman: with a docstring present, most people went top-down regardless. The "novice bottom-up, expert top-down" frame is a textbook slogan, not a measured result.
- Pennington (program model first) vs Burkhardt (situation questions answered better in OO code): paradigm or study design may explain it; unresolved.
- Brooks/Letovsky top-down vs Koenemann as-needed vs Singer just-in-time: these are one family seen at different scales, but nobody tested them head to head. Singer is N=1.
- Agentless (fixed top-down pipeline matches agents) vs LocAgent/SWE-Explore (open exploration with graph tools wins on localisation): different benchmarks, no equal-token comparison.
- Attention: Paltenghi finds partial match with human gaze; Li et al. and Kou et al. find weak match. Different tasks (sensemaking vs summarising vs task text).

## Weak spots
- Founding human studies are tiny: Koenemann N=12, von Mayrhauser/Vans N=4, Singer N=1, Siegmund N=17. Only Ko and Uttl (75) and Burkhardt (51) are mid-sized.
- Only one qualifying replication across 95 experiments (Wyrich 2023). Peitek's partial replication is the main replication here, and it partly failed.
- Comprehension measures hardly correlate with each other (Wyrich 2023), so cross-study numbers are not additive.
- All LLM "comprehension" studies measure output prediction, summary or localisation, not the construction of a model. No LLM study uses von Mayrhauser-Vans or Letovsky as a prompt (c27, search-based negative).
- c27 is a negative from limited search with APIs rate limited; absence is not proven.
- Most LLM numbers are single benchmarks, mostly HumanEval-like; contamination not discussed in most.

## Only seen in snippets
a24 (CoCoNUT, 47%), b04 (Peachock replication, seen only through Peitek), b08 (Gopstein 2017, seen via Langhout), b24 (Chain of Understanding), b25 (Brooks, Letovsky, von Mayrhauser 1995 primary texts, citations only). The Brooks, Letovsky and Littman 1986 primary papers were never opened; their content comes via Wyrich 2023 and Detienne's survey.

## GAPS (most decision-relevant first)
1. At equal tokens, does an explicit comprehension strategy prompt (bottom-up chunking, top-down hypotheses, as-needed) beat a plain "read then fix" prompt on repo bug-fix and code-QA tasks? No study tests this.
2. Does letting the agent run code (real execution) beat having it simulate execution, and by how much, when reading code to confirm a hypothesis? REval/Liu show simulation is weak; the head-to-head with a tool is missing.
3. Does hiding or scrambling identifiers during first reading (forcing structure-based bottom-up) reduce the name-trust errors seen in c12/b13, and what does it cost in accuracy?
4. Does a comment or docstring anchor LLM reviewers the way it anchors humans (Kaufman: correct accepted 73.9%, wrong caught 49.0%)? Test with equal code, wrong comments.
5. Are Ko and Uttl's breadth-first advantage and the three clusters replicable with a larger, professional sample or with LLM agents (survey all modules, then dive)?
6. Which reading unit helps an agent most: skeleton (58.33% vs 53.67% in Agentless), 100-line window, or call-graph? Needs one benchmark with equal tokens.
7. Is Pennington's order (control flow first, function second) real for LLM agents, and does it depend on language paradigm (Burkhardt reversal in OO)?
8. Does the agent's own step count or repeated action (failures run 2x longer in c18, 13.6% vs 6.1% repeats in c17) work as a stopping trigger for re-planning without losing wins on hard tasks?
9. What do the primary papers (Brooks 1983, Letovsky 1986, von Mayrhauser and Vans 1995) say about the beacon and hypothesis-failure rules that could be turned into operators? Not opened.
10. Does perplexity spike (b12, rho 0.37) work as a cheap trigger for "re-read this line", given that snippet-level perplexity fails (b11)?


## Gap search results (evidence_d.jsonl, d01-d20)
Search limits: arXiv API, OpenAlex and Semantic Scholar hit rate limits; 6 web searches used. All numbers below were read from full PDF text unless marked.

1. CLOSED PARTLY (still open for named strategies). No study tests bottom-up / top-down / as-needed prompts at equal tokens (d20). Nearest: DeskCheck stage-wise code reasoning, +6.29 to +10.53 points on SWE-bench Pro, +7.6% tokens (d02, d03); semi-formal certificates, 78.2% to 88.8% at 2.8x steps (d05). New claims K24, K25.
2. PARTLY ANSWERED. DeskCheck simulation reached method recall 0.66 vs 0.23 for an executor that ran 28 reproduction tests (d04). Not a clean ablation. Claim K26. Real execution vs simulation on the same scaffold is still missing.
3. PARTLY ANSWERED. CodeCrash neutral renaming costs about 1-9% (CRUX) and up to 27% (LCB) (d07). No two-pass test. Claim K28.
4. ANSWERED with a boundary. LLMs are anchored by wrong comments on output prediction (-23.2% relative, -13.8% with CoT; d06) but not in security review (p>0.21; d08). K14 moved to contested; K27 added. No human-vs-LLM paired test on identical code exists.
5. STILL OPEN. No replication of Ko and Uttl and no agent breadth-vs-depth test. SWE-Adept uses depth-first but bundles other changes (d12).
6. PARTLY ANSWERED. Skeleton and previews save tokens (d12), call hints add +2.2 Func@5 (d09), graph views +20 to +46 resolved (d11), graph-only tool loses to grep (d10). Still no single equal-token benchmark across skeleton, window and call graph. K29, K30.
7. STILL OPEN. No LLM test of Pennington's order or the OO reversal.
8. PARTLY ANSWERED. PAUSE: one re-plan at the first edit beats rule-based monitoring (+3.2 / +3.7) and matches periodic review at 11-15% planner cost (d13). Step-count and repeat triggers were not tested alone. Model-uncertainty triggers exist but only seen in snippets (d19). K31.
9. CLOSED for von Mayrhauser and Vans (primary text read, d14): three hypothesis-failure reasons, beacons, switching between models, keep open hypotheses few. Letovsky only through a 1989 report (d15). Brooks 1983 primary still not opened (d16, snippets). K32.
10. PARTLY ANSWERED. Region-level perplexity spikes track EEG confusion (rho 0.47 vs 0.05 on clean; 24 participants) (d17); snippet-level fails (b11). False positives exist. K33. No agent test of perplexity as a trigger.

Still open after this pass: 5, 7, and the equal-token tests in 1, 2, 3, 6, 8. Brooks 1983 and Letovsky 1986 primaries remain unopened.
