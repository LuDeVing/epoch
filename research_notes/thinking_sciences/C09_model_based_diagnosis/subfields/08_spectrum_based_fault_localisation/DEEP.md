# Spectrum-based fault localisation: deep document

*Subfield C09.08. Evidence ids (a01 to d18) are in evidence_a-d.jsonl. Claim ids (K01 to K35) are in claims.jsonl. Source audit in critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Spectrum-based fault localisation (SBFL) ranks parts of a program by how suspicious they are. It uses only two things: which code each test run touched, and whether that run passed or failed.

The record of "which code each run touched" is the program spectrum. Take a matrix. Rows are test runs. Columns are code units (statements, blocks, methods). A cell is 1 if the run executed the unit. A final column holds the verdict, pass or fail. Each code unit then gets four counts:

- a11: runs that hit the unit and failed.
- a10: runs that hit the unit and passed.
- a01: runs that missed the unit and failed.
- a00: runs that missed the unit and passed.

A formula turns the four counts into a suspicion score. Sort by score. The developer (or tool) inspects from the top. The idea is simple: code that failing runs touch and passing runs avoid is probably the fault.

Founding formulas:

- Tarantula (Jones, Harrold, Stasko 2002; snippet only).
- Jaccard (from the Pinpoint tool).
- AMPLE.
- Ochiai (Abreu, Zoeteweij, van Gemund 2006), taken from molecular biology: a11 / sqrt((a11+a01)(a11+a10)).

Why it matters for our agent. Schema state S5 (REVISE) shows the model a failing output located by code. Our agent often has several attempts at one problem, and a check that marks each attempt pass or fail. That is a spectrum in the broad sense: attempts are runs, steps or claims are code units, the check is the verdict. SBFL is the oldest worked-out method for turning many pass/fail runs into a ranked "look here first" list. This document asks three things. Does the ranking idea hold up on real bugs? Does it help a language model? Does anything carry over to non-code reasoning attempts?

Short answer. Classic SBFL works as a shortlist, not a verdict. The formula barely matters. Test output matters more than scores. For strong LLM agents the measured gain from a spectrum hint is small or null. No study has tried the idea on non-code reasoning attempts (K31, K34).

## 2. History and theories in depth

### 2.1 Before 2006

- Jones, Harrold and Stasko (2002) introduced Tarantula. Statements were coloured red to green by the share of failing tests that run them against the share of passing tests that run them. Their paper and Jones and Harrold (2005) used the Siemens programs. We did not open either (a11, c30 are [M]).
- Naish, Lee and Ramamohanarao (2011) and Xie et al. (2013) worked on theory. Under a single-fault model some formulas (for example Op2) are provably optimal, and many proposed formulas are rank-equivalent. Xie et al. compared 30 metrics: six groups of equivalent metrics, seven with none (b13). We saw these only through a survey (a18, b13).

### 2.2 The founding study: Abreu, Zoeteweij, van Gemund (2006)

Opened in full (a01 to a04; re-checked in critique.md).

- Setup. Siemens suite, 7 programs. 132 faulty versions provided, 14 discarded, 118 used. Block-level spectra. Quality measure qd: the rank of the faulty block, with ties counted at the worst position, as a share of blocks.
- Failure detection was by comparing output to a correct version. This is a crude error detector. Error accuracy ran from 1.2% (schedule2) to 21.1% (tot_info).
- Result. Ochiai beat Jaccard, Tarantula and AMPLE in every program. Average gain about 5% of blocks to inspect; 2.4% to 10% per program versus Jaccard, the second best; up to 30% on single versions. In the worst case the developer still inspects 40% of the code; in the best case 1%.
- Failure causes (a03). The fault block is run by every pass and every fail (for example main); the fault is deleted code; other blocks always run together with the fault and tie.
- Industrial check (a04). Philips TV software, 65K blocks. Some faults ranked first, partly because error detection was ideal there. Not a controlled experiment.
- Caution on the table. A per-program label mix-up exists in the extracted Table 2 (critique item 1). The row "10.5 / 7.3 / 1.0 / 2.0" belongs to print_tokens. Labels for the last two rows (tcas, tot_info) are unverified. The Ochiai-best pattern holds in every row.

### 2.3 The practical extension: Abreu et al. (2009, JSS)

Opened (a05 to a09).

- 162 faulty versions (Siemens plus space). Nine coefficients. Ochiai at least as good as the others. Average gain about 4% over the second best; up to 30% on single versions.
- Observation quality qe (share of fault-touching runs that fail): 1.4% (schedule2) to 20.3% (tot_info) on Siemens; 50.9% on average for space.
- Label noise (a06). With qe near 1%, qd is still about 80% (about 20% of the code left to inspect). Better labels help, but less than expected.
- Number of runs (a07). More failed runs help up to about 10 and then flatten. Failed runs NF 1 to 30 on 110 of 162 versions, up to 100 on 60 versions, each point averaged over 50 random picks of passed runs. Passed-run count has little average effect; for single versions it can help or hurt.
- Formal result (a08). For blocks hit by at least one failed run, Tarantula, Jaccard and Ochiai each give the same rank order as a simpler expression in a11 and a10. Ranking is a trade-off between failures that touch the block and passes that touch it.
- Philips (a09). 150,000 blocks in 1800 files. Four real cases. Estimated qd 99.96% (NVM corrupt: 96 blocks, 10 files to inspect) and above 99.99% for two others. The authors call the estimates debatable.

### 2.4 Replication and the real-fault turn

- Pearson et al. (2017, ICSE) replicated 10 claims from earlier SBFL and mutation-based (MBFL) papers (a12 to a15, b01 to b05, c26, c27). On 2995 artificial faults (mutants in 6 Java programs), 7 claims held with significance, but only 3 had a non-negligible effect size. On 310 real Defects4J faults, every earlier result was refuted or was statistically and practically insignificant. About 70% of pairwise claims replicated overall; about 40% of results reversed on real faults. Metallaxis was best on artificial faults (EXAM 0.0432) and near the bottom on real ones. Ochiai beat Metallaxis on real faults.
- Formula choice (b03). On real faults the formula explains at most 2% of non-defect variance in EXAM. A Tukey test found all SBFL formula differences insignificant. Defect and debugging scenario dominate the variance (R2 = 0.65).
- Zou et al. (2019, a16): the largest real-fault study of families (SBFL, mutation, slicing, stack trace, predicate switching, IR, history). SBFL is the best single family. Ochiai and DStar are nearly identical (r2 = 0.753). A learned combination beats every single family.
- Rezaalipour and Furia (2024, a17, b06 to b09): conceptual replication on Python, 135 real faults, 13 BugsInPy projects, 7 techniques. SBFL again best, MBFL second, effect size -0.18 weakly favouring SBFL. Tarantula, Ochiai and DStar rankings correlate 0.94 to 0.99.

### 2.5 Fixes for known weaknesses

- Multiple faults (b11, b12). FLITSR (Callaghan and Fischer 2023) takes the top element, removes the tests it explains, and re-ranks. On 75000 synthetic variants and 326 real multi-fault Defects4J versions, wasted effort fell 30% to 90%. A learning-based follow-up, SA-BCL, is reported to beat FLITSR by up to 37.5% in wasted effort (second-hand, d18).
- Early termination (b28). A failing test stops at the first failed assertion, so later code is not recorded. 19.1% of failing tests terminate early. Coverage improves in 55% of versions. Ochiai and Tarantula improve by 15.1% and 10.7% in mean first rank.
- Flaky tests (b29). 80.3% of 101 flaky tests (48 Python projects) show varying coverage. Using only lines covered in every run narrows to about 3.5% of the code base, 18.7% better than DStar.
- No failing test (b10). Only 3.33% of crash-report bugs had a failing test when filed. Stack-trace ranking gave 56.67% in the top 5 on 60 crash bugs. SBEST raised MAP by 32.22% and MRR by 17.43%.
- Richer spectra (b30). Data-flow spectra put up to 50% more faults in the top 15 than line coverage, at 353% overhead versus 102%.

### 2.6 The human-use debate

Opened in full: Parnin and Orso (2011; d01, d02) and Xia et al. (2016; d03, d04). Not opened: Xie et al. (2016; d05, closed access), and the GZoltar and Kochhar studies (b14 to b17, summary only).

- Parnin and Orso: 34 students in a design check, then 24 in the main run and 10 in a rank-change follow-up. Two bugs (Tetris, NanoXML). Tarantula list. No mean gain. Tetris 12:42 with tool vs 14:14 without; NanoXML 20:16 vs 22:30; neither significant. Only high performers on the easy task gained (8:51 vs 14:28, p<0.05). Moving the fault from rank 7 to 35 did not change time (10:12 vs 12:36). Moving it from 83 to 16 made the group slower (15:12 vs 18:30). N=5 per group. People did not read the list in order.
- Xia et al.: 36 professionals, 12 per group, 16 real Defects4J bugs, 4 bugs each. The list was simulated: the fault sat randomly in ranks 1 to 5 (accurate) or 6 to 10 (mediocre). Success 98% (47/48) vs 94% (45/48) vs 77% without the tool. Mean time 11.38 vs 16.35 vs 26.5 min. Cliff delta 0.80 and 0.55.
- Behaviour (d04): 20 of 24 tool users (83.3%) read the top 5 in order. 18 of 24 (75%) read through rank 5, 8 (33.3%) through rank 6, 3 (12.5%) through rank 8. "I only trust the top-5 statements."
- Xie et al., second-hand: students, synthetic bugs in toy programs, helped only when the fault ranked near the top and often raised time. The N=207 figure is not confirmed.
- GZoltar user study (b17, snippet): 40 master's students, one fault. All with the tool found it in about 7 minutes; controls 35% in 30 minutes.

The studies differ in people, bug count, and tool realism. Neither tested a list that misses the fault. Status [C], with a reason (K09).

### 2.7 The LLM turn (2023 to 2026)

A newer thread asks if a language model can replace or use the spectrum. See section 6. In short: LLM methods use the failing test output and repository tools; SBFL serves as a shortlist, a baseline, or an input.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Ochiai beats Jaccard, Tarantula, AMPLE on single-fault Siemens | about 5% fewer blocks to inspect on average; up to 30% on single versions; 118 versions used | a01, a02 (Abreu 2006) | [S] (K01) |
| Same on 162 versions; Ochiai at least as good as 8 others | about 4% over second best; up to 30% | a05 (Abreu 2009) | [S] |
| Formula choice matters little on real faults | formula explains at most 2% of non-defect variance; Ochiai/Tarantula/DStar rank correlation 0.94 to 0.99 | a08, a13, b03, b07, b13 | [E] (K02) |
| Ochiai, Jaccard, Tarantula reduce to a simple a11/a10 ordering | exact for blocks hit by a failing run | a08 | [E] (math) |
| SBFL tolerates very noisy labels | qd about 80% at qe about 1%; gains flatten after about 10 failing runs | a06, a07 | [S] (K03) |
| SBFL structurally fails on shared or deleted code | fault run by every test; coverage collapse in 22.9% of 809 programs; Ochiai first in 2.2% there | a03, a28, b26, c13, c14, d14 | [E] (K04) |
| Artificial-fault results do not transfer to real faults | 2995 artificial, 310 real; about 40% of results reversed on real | a12, a13, b01, b02, c26 | [S] (K05) |
| On real Defects4J, SBFL is the best single family but a weak ranker | Top-1 only 16 to 17 (4% to 5%); 155 to 156 faults (about 44%) in top 10 | a16, a17, b06, b09 | [E] (K06) |
| Hit rate in practice | best case DStar top-5/10/200 = 30% / 39% / 82%; average case 18% / 26% / 69%; 98% of practitioners want top 10 | a14, c27 | [S] |
| Many real faults are outside what coverage can see | 76% of fixes span several statements; about 30% only add missing code; 4% non-executable lines | a15 | [S] (counts quoted from other studies) |
| Multi-fault masking; iterative recompute helps | wasted effort cut 30% to 90% (75000 synthetic, 326 real) | b11, b12 | [S] (K07) |
| Early termination and flakiness hide coverage | 19.1% of failing tests end early; 55% of versions improve; 80.3% of flaky tests vary | b28, b29 | [E] (K08) |
| Humans: professionals gain when fault is in top 10 | success 98% / 94% vs 77%; time 11.4 / 16.4 vs 26.5 min | d03 | [C] (K09) |
| Humans: students, 2 bugs, no mean gain | 12:42 vs 14:14; 20:16 vs 22:30, n.s. | d01 | [C] |
| Humans read the top 5 only | 83.3% read top 5 in order; 33.3% read through rank 6 | d04 | [S] (K24) |
| LLM with repo tools and failing test beats Ochiai at acc@1 | +19.7% D4J; +166.7% (GPT-3.5), +233.3% (GPT-4) BugsInPy; GPT-3.5 lags SBFL at acc@3/5 | a19, b19, c04 | [S] (K10) |
| Repeated LLM runs merge well | one GPT-4 run beat five merged GPT-3.5 runs; single explanation accurate 20.0% of 300; at least one right for 56.7% of 60 bugs | a20, b20, c05 | [S] (K11) |
| Test results help LLMs more than suspicion scores | FuseFL Top-1: baseline 150, SusScore 169, TestRes 187, CodeDesc 180, all three 197 (324 programs, GPT-3.5) | a21, b25, c20, c21 | [S] (K12) |
| Hybrid: shortlist then LLM re-rank | D4J 2.0, 835 bugs: Ochiai 167, Ochiai+LLM re-rank 303, FlexFL 350 | a24, c18 | [E] (K13) |
| LLM4FL | about 326 of 675 Top-1 vs Ochiai 121; DepGraph (learned) 359 | a25, b24, c15 | [E] with K13 |
| Agent pipeline beats Ochiai, not best learned | AgentFL 157/395 vs Ochiai 80; D4J 2.0 78/226 vs 32; no test-failure analysis 125 | a23, b21, b22, c06, c07 | [S] (K21) |
| Ochiai baselines differ by granularity | 19 (statement, DeepFL ties) vs 80 (method) of 395; 101 of 501 in another study | a22, d12, d10, d13 | [E] (K20) |
| LLM input order moves results a lot | up to 22% Top-1 spread; reverse order Java 57% to 20%, Python 38% to about 3% | a25, c08, c17, d10 | [E] (K14) |
| Ochiai order is not special | Ochiai order 164 (32.7%), LOC order about 163, call-graph BFS 175 (34.9%) of 501; Ochiai alone 101 | d10, c09 | [S] (K27) |
| Memory plays a part | renaming cut Top-1 by 4% (217 to 208) to 9% (278 to 253) | d11 | [S] (K32) |
| Semantics-preserving edits break localisers | 78% fail on a fault found before (750,013 tasks) | c12 | [S] (K15) |
| SBFL hint to a repair agent: small, noisy gain | AutoCodeRover Lite 57 (19%) to 66 (22%) at 37k to 40k tokens; best of 3 runs 78 | a26, c24, d06 | [C] (K16) |
| Localiser hints do not lift strong repair agents | pass@1 change -4.45 to +0.40; down in 17 of 18 settings; gold hints +0.8 to +4.6 | c10, d07 | [S] (K26) |
| Anchoring on wrong hints is common, recovery usual | anchor 34.5% to 100%; recover 34.8% to 95.9% | d08 | [S] (K25) |
| Localisation tokens often exceed repair savings | repair tokens down up to 39.2% with gold; end-to-end tokens up in 13 of 18 settings (-16.4% to +129.8%) | c10, d09 | [E] (K17) |
| Failing-test output carries most of the signal | SemBugs Acc@1 50.0% (function only) vs 82.0% (tests plus errors); ChatGPT-4 without error log -25.6% Top-1 | d14, b18, c21 | [E] (K28) |
| Coverage as a filter, not a ranker | candidates -79%; input tokens about -49%; Top-1 165/395 unchanged | d13 | [S] (K29) |
| Value-check spectra did not beat a plain LLM call | SemLoc 81.4% vs 82.0%; 2.2 to 3.0 times tokens; 51.9% of violated constraints wrong | d14, d15 | [S] (K30) |
| Patch-and-rerun separates right from wrong top lines | verified in 76.9% of 7,845 right vs 19.9% of 1,836 wrong | d15 | [S] |
| File-level hints dominate; line-level hurts | file-level 15 to 17 times over no file; best at 6 to 10 files; 500 tasks, 61 configurations | c11, d17 | [S] (K33) |
| Reasoning LLMs beat SBFL on small student programs | 13 LLMs vs SBFL/MBFL, 3 datasets of 503; SBFL alone found 8 unique faults on Codeflaws | a29, b27, c19 | [S] (K23) |
| Non-code analogue: blaming a failing step from one trace is weak | best 14.2% step-level, 53.5% agent-level on Who&When | d16 | [S] (K31) |
| Untested: spectrum hint vs test-only at equal tokens, strong model | none | K34 | untested |
| Untested: FLITSR in an LLM loop; flaky, early-stop, few-failure effects on LLM FL | none | K35 | untested |

## 4. Mechanisms and models

### 4.1 The core algorithm (an engineer can build this in an hour)

Inputs: a list of runs R. For each run r: a set cov(r) of code units it executed, and a verdict v(r) in {pass, fail}.

1. For each unit u compute a11(u) = number of failing runs with u in cov; a10(u) = passing runs with u; a01(u) = failing runs without u; a00(u) = passing runs without u.
2. Score. Ochiai(u) = a11 / sqrt((a11 + a01) * (a11 + a10)). Set score 0 if the denominator is 0.
3. Sort by score, high first.
4. Ties. Give every tied unit the average rank (Pearson 2017) or the worst rank (Abreu 2006). Say which. This one choice moves Top-1 counts a lot (K20).
5. Report the top k. Evidence says k = 5 for people (d04) and 5 to 10 for a shortlist (a14).

Other formulas. Tarantula = (a11/F) / ((a11/F) + (a10/P)) with F = total failing, P = total passing. Jaccard = a11 / (a11 + a01 + a10). DStar = a11^* / (a10 + a01). Op2 = a11 - a10/(P+1). The 2009 result (a08) says Tarantula, Jaccard and Ochiai produce the same order as a simple function of a11 and a10 on units that a failing run touches. So do not spend effort here (K02).

### 4.2 Why it works and when it breaks

- It works because a fault is on the path of every failing run and is, by chance, off the path of many passing runs.
- It breaks when that is false. Three cases from a03, a15, a28:
  1. The fault is executed by all runs (main, setup code). a10 is as big as a11.
  2. The fault is missing code (about 30% of real fixes, a15). No unit is wrong.
  3. Coverage collapse: failing and passing tests run the same lines and differ only in values. 22.9% of 809 real Python bugs. Ochiai first in 2.2% there (b26, d14).
- Overall on real Defects4J faults Top-1 is 4% to 5% for statement-level SBFL (a16). It is a shortlist tool: about 44% in the top 10.

### 4.3 Hardening the spectrum before use

- Run each test to the end, not to the first failed assertion (b28).
- Rerun tests to catch flakiness; keep only lines covered in every run (b29).
- Several failing runs, up to about 10 (a07). Passing runs matter less.
- If no failing test exists, make one first (b10). Stack-trace ranking is a fallback (56.67% in top 5).
- Multiple faults: fix the top candidate, drop the failing runs it explains, recompute (FLITSR, b11).

### 4.4 Four ways an LLM uses a spectrum

1. As a ranked list in the prompt (AutoCodeRover top-5 methods, FuseFL scores). Gains are small (K16) or smaller than test results (K12).
2. As a filter: drop units no failing run touched (SieveFL). Candidates -79%, tokens about -49%, Top-1 unchanged (K29). The most cost-effective use found.
3. As a shortlist then LLM re-rank (FlexFL, LLM4FL). Ochiai 167, plus re-ranker 303, FlexFL 350 of 835 (K13).
4. As an inspiration for a new spectrum the LLM builds itself (SemLoc): the LLM writes value checks, the program counts violations per test, then Ochiai ranks over violations. It helps in coverage collapse (40.9% vs 2.2%) but does not beat a plain LLM given tests and errors (81.4% vs 82.0%) and costs 2.2 to 3.0 times the tokens (K30).

### 4.5 A model of the LLM's use of the hint

From the evidence, the LLM behaves as a reader of a candidate list, not as a ranker:

- Input order carries bias: reversing it takes Java Top-1 from 57% to 20% (c08). Splitting into smaller contexts narrows the gap to 1%.
- The order does not need to be Ochiai: LOC order and call-graph order do as well or better (d10).
- What it gets from coverage is mostly which units were run by the failing test (the filter), not the score (K27, K29).
- It anchors on a wrong hint 34.5% to 100% of the time but usually recovers (d08).
- It profits most from the failing-test output itself (K28).

### 4.6 Mapping to our agent (a model, not a result)

Treat each attempt at a problem as a run, each checkable step or claim as a unit, and the check outcome as the verdict. Then:

- a11(step) = failed attempts that contain the step; a10(step) = passed attempts that contain it.
- Steps that only failing attempts contain would rank first.

No study has done this (K31, K34). The only data point is that blaming a step from a single trace is weak (best 14.2% step-level, d16). Two hurdles: steps must be matched across attempts (code needs a canonical form), and the number of attempts is small (3 to 5), far below the 10 failing runs the classic result needs (a07). The mapping is a hypothesis to test, not an established tool.

## 5. What holds up

### 5.1 Replicated or confirmed

- Formula choice is minor on real faults: 4 independent sources (K02) [E].
- SBFL breaks on shared, deleted or collapsed coverage: 2 sources (K04) [E].
- SBFL is the best single non-LLM family on real Java faults, replicated on Python (135 faults), with Top-1 only 4% to 5% (K06) [E].
- Hidden measurement problems (early termination, flakiness) reduce SBFL: 2 studies (K08) [E].
- Hybrid classical-then-LLM beats either alone on Defects4J: 2 sources (K13) [E].
- LLM FL is order-sensitive: 2 sources, one with a reversal experiment (K14) [E].
- Localisation cost often exceeds the repair saving; file-level hints give most of the gain: 2 sources (K17) [E].
- Failing-test output carries most of the LLM's signal: 2 sources (K28) [E].
- Baseline disagreement (19 vs 80) is a granularity difference, not an error (K20) [E].

### 5.2 Failures and reversals

- Mutant-based results did not transfer: about 40% of results reversed on 310 real faults (K05). Any S5 aid must be tested on real failures, not injected ones.
- Human benefit did not replicate across studies (K09). Students on two bugs: no mean gain. Professionals on 16 bugs with a simulated top-10 list: large gain. Reasons differ: population, list realism, whether the fault was ever missing from the list.
- Strong-agent hints: six LLM localisers on three 2026 repair models lowered pass@1 in 17 of 18 settings (-4.45 to +0.40) (K26). Gold hints add only +0.8 to +4.6 points. The ceiling is low.
- AutoCodeRover's +9 tasks is one run per arm, within run noise (three runs of the base agent reached 78) (K16) [C].
- Fine-tuned LLM localisers (LLMAO) are compared to learned baselines, not to a fresh Ochiai in the abstract (b23).

### 5.3 Moderators

- Granularity: file or function hints beat line hints (K33). Statement-level Ochiai top-1 is 19 of 395; method-level 80 of 395 (K20).
- Fault type: omission faults (about 30%) and non-executable lines (4%) are invisible to coverage (a15). Data-science bugs are harder (b08).
- Number of faults: effort rises with fault count; iterative recompute helps (K07).
- Model size: small models recover less from wrong hints (K25). GPT-3.5 lags SBFL at acc@3 and acc@5 (K10).
- Task size: reasoning models do better on small student programs but accuracy falls with difficulty (K23).
- Ties and tie rules, and observation quality qe (a06).
- Memory: renaming methods cut Top-1 by 4% to 9% (K32). Semantics-preserving edits break 78% of earlier finds (K15).

### 5.4 Interventions that worked

- Run tests to completion (+15.1% and +10.7% mean first rank for Ochiai and Tarantula, b28).
- Keep only lines covered in every rerun for flaky tests (18.7% better than DStar, b29).
- FLITSR iterative recompute for multi-fault (30% to 90% less wasted effort, b11).
- Coverage as a filter before the LLM (-79% candidates, -49% tokens, same Top-1, d13).
- Merging repeated LLM runs (b20) and test-failure analysis (AgentFL ablation 157 to 125 without it, b22).
- Patch-and-rerun check of the top line (76.9% pass for right vs 19.9% for wrong, d15).
- Splitting LLM context into smaller segments (order gap 22% and 6% to 1%, c08).

### 5.5 Interventions that did not work

- Tuning the formula (K02).
- Ordering LLM input by Ochiai versus plain size or call graph (K27).
- Line-level context added to file-level (K33).
- Value-check spectra over a plain LLM call with the same inputs (K30).
- Chain-of-thought and few-shot prompting for localisation: mixed or case-specific (c02).
- Plugging in off-the-shelf LLM localisers for strong repair agents (K26).

## 6. Language models

### 6.1 Without any spectrum

- Wu et al. (2023, b18, c23): ChatGPT-4 at function level with the error log had Top-1 46.9% above SmartFL; at class level 49.9% lower. Removing the error log cut Top-1 by 25.6%.
- AutoFL (Kang et al. 2024; a19, a20, b19, b20): 798 bugs. Acc@1 over Ochiai: +19.7% Defects4J, +166.7% BugsInPy (GPT-3.5), +233.3% BugsInPy (GPT-4). GPT-3.5 lags SBFL at acc@3 and acc@5; GPT-4 beats all baselines up to acc@5. 87.24 s per bug (5 runs) vs 112 s for SBFL cited from Zou. A single explanation was accurate 20.0% of the time (300 explanations, 60 bugs); at least one of five was accurate for 56.7%. Confidence under 0.25: 23.8% accurate; 0.50 to 0.75: 34.3%. Merging 5 runs raised acc@k strongly.
- LLMAO (Yang et al. 2024; a22, d12): fine-tuned CodeGen 350M, 6B, 16B with adapters; no coverage. Defects4J 1.2 statement level Top-1/3/5: Ochiai 19 / 65 / 99; LLMAO-16B 88 / 149 / 183; 6B 85 / 115 / 160; 350M 82 / 106 / 126. Unseen projects: 31.9% Top-1.
- SemLoc baseline (d14): an LLM seeing only the function gets 50.0% Acc@1; with tests and errors, 82.0%.
- Novice programs (a29, b27, c19): 13 LLMs vs SBFL and MBFL on 503 programs per dataset (Codeflaws C, ConDefects Java, BugT C++ built to limit leakage). All six closed models beat SBFL and MBFL. o3 and DeepSeek-R1 best. SBFL alone found 8 unique faults on Codeflaws; MBFL 1. The extracted Ochiai/DStar/Op2 rows had identical cells, pointing to ties on tiny programs.
- Xiao et al. (2026, c02): four LLMs (Qwen2.5-Coder-32B, DeepSeek-V3, GPT-4.1 mini, Gemini-2.5-Flash); bug report context helped on Defects4J; few-shot and chain-of-thought mixed.

### 6.2 With a spectrum or a classic localiser

- FuseFL (GPT-3.5, 324 Refactory programs, 600 faulty lines; a21, c20 to c22). Top-1: Tarantula 89, Ochiai 117, Op2 115, Barinel 89, DStar 115, XAI4FL 149, FuseFL 197 (+68.4% over Ochiai, +32.3% over XAI4FL). Prompt table: Baseline 150, CoT 163, SusScore 169, CodeDesc 180, TestRes 187, SusScore+TestRes 192, TestRes+CodeDesc 190, SusScore+CodeDesc 177, all three 197. Of 117 faults Ochiai got at Top-1, FuseFL got 116 (99%). 81 found only by FuseFL. In 77 cases SBFL missed in the top 3, the score prompt got only 8 at Top-1. Failed localisations: 78.5% wrong-output errors, 21.5% runtime errors. Cohen d 0.30 to 0.71 vs SBFL at Top-1. 22 of 30 sampled explanations correct.
- AgentFL (ChatGPT, three agents: comprehension, navigation, confirmation; a23, b21, b22, c06, c07). D4J 1.2 (395): 157 Top-1, 183 Top-3, 187 Top-5; Ochiai 80. D4J 2.0 (226): 78 / 119 / 140 vs Ochiai 32 / 74 / 93, GRACE 85 Top-1. $0.074 and 97 s per bug. 34 bugs found only by AgentFL. Ablation Top-1: full 157; no test behaviour 148; no method documentation 133; no test failure analysis 125. Loses to learned localisers: 3 fewer than FLUCCS, 19 fewer than DeepFLcov, 35 fewer than GRACE.
- FlexFL (open models; a24, c18). D4J 2.0 (835): Ochiai Top-1/3/5 167 / 316 / 389; Ochiai plus LLM re-ranker 303 / 421 / 475; FlexFL 350 / 478 / 529 (363 / 511 / 558 with repetition). Without the program text, Top-5 falls to 75. Llama3-8B version finds 42 and 63 more bugs than AutoFL and AgentFL (GPT-3.5). 93 Top-1 bugs that non-LLM FL cannot find.
- LLM4FL (GPT-4o-mini, 675 D4J 2.0 faults; a25, b24, c15 to c17). Top-1 about 326 (one version says 327; unresolved); Ochiai 121; DeepFL 257; GRACE 298; DepGraph 359; AutoFL 275; AgentFL 311. Top-10: 494 to 496 vs Ochiai 413. Ablation: no code navigation 273 (-16.5%); no coverage division 251 (-23.2%); no reflexion 290 (-11.3%). Order effect up to 22% Top-1.
- Order Matters (Rafi and Chen 2026; c08, c09, d10, d11). 501 D4J faults, gpt-4o-mini. Ochiai alone 101; Ochiai order 164 (32.7%); LOC order about 163; call-graph BFS 175 (34.9%); DFS 173 (34.5%); learned DepGraph order 242 (48.3%). Java Top-1 57% to 20% on reverse order; Python 38% to about 3%. Renaming did not remove the bias. Renamed worst order 152 (30.3%) vs perfect 253 (50.5%).
- SieveFL (Nemotron-3-Nano-30B; d13). 395 D4J 1.2 bugs. Top-1 165 (41.8%), MRR 0.469, +2.1 points over AgentFL. On 383 paired bugs: candidates 398.8 to 187.2; wall-clock 5.07 to 4.05 min; Top-3 to Top-10 up 2.3 to 2.4 points. Coverage-only scoring lost 0.5 points.
- SemLoc (d14, d15; a28, b26, c13, c14). 809 real Python bugs from 750 projects, plus QuixBugs, four LLMs. SBFL misses the first rank in at least 83.8% with each of six formulas. In coverage collapse (185 programs): violations rank the fault first in 40.9%, Ochiai 2.2%, Daikon 7.0%. Ochiai misses the top five in 55.1% there. 99.4% of constraints compile. 68.4% of top answers carry a test-confirmed patch, 93.6% of those correct. LLM confidence >= 0.9 on 76.2% of answers, only 84.1% of those right; only 33.1% of wrong answers fall below the threshold. Cost 2.2 to 3.0 times tokens.
- AutoCodeRover (a26, c24, d06). SWE-bench Lite 300 tasks, GPT-4-era model. No SBFL 57 (19.00%), 37k tokens, $0.43. With top-5 SBFL methods 66 (22.00%), 40k tokens, $0.47, 250 s. Three runs without SBFL: 78 (26.00%), 112k tokens. 7 tasks solved only with SBFL. The agent did not blindly follow rank 1 (case django-13964). Of 78 plausible patches in the base run, 51 correct (65.4%).
- Agentless (a27): describes SBFL but localises with the LLM and picks patches by model-written reproduction tests.

### 6.3 Repair with localisation in 2026

- Shi, Yang, Chen (2026; c10, d07, d08, d09). Six LLM-based localisers plugged into one agent (mini-swe-agent). SWE-bench Verified (500) and Defects4J v3.0.1; repair models GPT-5.6 Luna, DeepSeek-v4 Flash, Gemini 3.1 Flash Lite; 16,248 trajectories. Pass@1 change -4.45 to +0.40 points; down in 17 of 18 settings. Example: GPT-5.6 Luna no-FL 73.4%; LocAgent 72.0%, CoSIL 72.0%, OrcaLoca 71.2%. Repair-stage tokens down in 16 of 18 settings (-31.3% to +9.8%); steps down in 17. End-to-end tokens (including FL) up in 13 settings, down in 5 (-16.4% to +129.8%); all six GPT-5.6 Luna settings up. Gold symbols cut repair tokens by up to 39.2%. Anchoring under completely wrong file hints (7 to 206 cases per setting): 34.5% to 100% looked at a suggested file first; 34.8% to 95.9% of those still reached a correct file; below 50% in all three Gemini 3.1 Flash Lite Defects4J settings.
- Sepidband, Pham, Hemmati (2026; c11, d17). GPT-5-mini, 500 SWE-bench Verified tasks, 61 context settings. File-level hints 15 to 17 times better than no file. Best around 6 to 10 relevant files. Line-level expansion often degrades repair.
- Haroon et al. (2026; c12). 10 LLMs, 750,013 localisation tasks, over 1300 Java and Python programs. After a semantics-preserving change the model fails on 78% of previously found faults. Code earlier in context is reasoned about better.
- LDB (Zhong, Wang, Shang 2024; c25): shows intermediate values per basic block; up to 9.8% on HumanEval, MBPP, TransCoder. AutoSD (Kang et al. 2023; a30): hypothesis, debugger probe, observation, conclusion; no SBFL-specific numbers recorded.

### 6.4 Summary of what changed results, and by how much

- Giving the LLM the failing test output: the biggest lever (50.0% to 82.0% in SemBugs; -25.6% Top-1 without the log for ChatGPT-4).
- Repository tools and repeated runs: large (AutoFL).
- Shortlisting with Ochiai then LLM re-rank: Top-1 167 to 303 of 835 (+81%), then 350 with the full pipeline.
- Adding spectrum scores to the prompt: small (+3.7% over CoT at Top-1; 169 vs 150 baseline in FuseFL).
- Input order: up to 22% Top-1.
- Spectrum hint for a strong repair agent: about zero.
- Caveats: nearly all results are Defects4J (Java, possible memory, 4% to 9% loss on renaming); many are 2024 to 2026 preprints with author-built baselines (critique "Weak spots").

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| S5 always shows the real failing output (test or check result) before anything else; a spectrum-style hint is never a replacement for it. | S5 (supports G2) | [E] | K28, d14, b18, c21 |
| Do not tune or compare ranking formulas. If a spectrum is built, use Ochiai and move on. | S5 | [E] | K02, a08, b03, b07 |
| Any ranked hint is a shortlist. Show at most 5 to 10 items, coarse grain (function or step, not long line lists). | S5 | [E] for shortlist use; grain [S] | K06, K17, K13; K24, K33 |
| Randomise or split candidate order across attempts; never assume the score order is the best order. | S3, S5 | [E] | K14, c08, d10 |
| Detect ties or collapse in a hint (everything covered by all runs). On collapse, drop the ranking and fall back to tracing real values or the failing output. | S5 | [E] | K04, a03, b26 |
| Run each check to completion, rerun for flakiness, before counting a pass or a fail. | S4, S5 | [E] | K08, b28, b29 |
| Charge hint-building tokens against the savings. Cheap, code-made hints only (filters, counts), no extra model call for localisation unless it pays. | G7, S5 | [E] | K17, d09 |
| Any evaluation of an S5 aid uses real failures, not injected ones, and reruns baselines with the same tie rule and granularity. | G7 (bench rule) | [E] | K05, K20 |
| If no failing check exists, build one first (or use the trace as the check) before any localisation step. | S4 | [S] (already near G2) | K18, b10 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Spectrum-from-attempts: rank steps by Ochiai over several attempts' pass/fail. | S5 | [S] (no non-code study) | K31, d16, K34 |
| Executed-set filter: show only the functions or steps the failing attempt actually ran. | S5 | [S] | K29, d13 |
| Ochiai top-5 hint on top of failing output for code attempts. | S5 | [C] | K16, K26, d06, d07 |
| Anchoring guard: ask whether the evidence agrees with a hint before using it. | S5, G10 | [S] | K25, d08 |
| Repeated short localisations merged by agreement, as a confidence signal. | G4 sampling, S5 | [S] | K11, b20 |
| FLITSR-style recompute after each fix. | S5, S8 | [S] (untested with LLMs) | K07, K35, b11 |
| Probes plus patch-and-rerun check of the top suspect in preference to value spectra. | S5, S8, G3 | [S] | K22, K30, d15 |
| Show scores, test results or both. | S5 | [S] | K12, c21 |
| Hint grain: file or function versus line. | S5 | [S] | K33, c11 |
| Rename or reformat before S5 to reduce memory and brittleness. | S1 | [S] | K15, K32 |
| Top-5 cap versus top-10. | S5 | [S] | K24, d04 |
| Keep a per-class lesson: which hint type helped. | memory | [D] | K34 |

## 8. Concrete tests on our bench

All tests use equal token caps per arm, at least 3 seeds, and real failures (K05).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Small buggy programs with test suites, real or held-out (not mutants), strong model | (a) failing output only; (b) plus unranked set of executed functions; (c) plus Ochiai top-5; (d) plus Ochiai top-5 with a planted wrong top-1 | Solve rate; tokens to first correct fix; share that follow the wrong top-1 | (b) and (c) within 3 points of (a); (b) cheaper in tokens (d13 saw -49%); (d) lowers solve rate for small models more than large ones (d08) |
| T2 | ARC-style or word-puzzle items, 5 attempts each with a checkable output | (a) one-trace blame (model names the first wrong step); (b) Ochiai rank over steps matched across attempts; (c) random step | Step-level hit rate on seeded errors; rate of fixes that work | (b) above (c); (b) vs (a) unknown; baseline from Who&When is 14.2% step-level |
| T3 | Same as T2 | 5 short attempts merged by agreement vs 1 long attempt, localising the same fault | Hit rate at equal tokens | Merging gains (b20); size unknown |
| T4 | Buggy programs, strong model | Hint grain: file or function only vs functions plus line list | Solve rate; tokens | Function-only equal or better (c11) |
| T5 | Programs with two planted faults | Fix-one-then-recompute vs single ranking | Faults fixed per token | Recompute better (b11); untested with an LLM |
| T6 | Programs where all tests cover the same lines (collapse) | Ochiai hint vs failing output with values vs probe-then-patch check | Top-1 localisation; solve rate | Ochiai hint at about 2% (b26); probes close to plain LLM (d14) |
| T7 | Items with candidate lists | Same list in Ochiai order, random order, reverse order, split into segments of 10 | Top-1 | Position bias; split narrows it (c08) |
| T8 | Same items before and after renaming or reformatting | Raw vs normalised input to S5 | Top-1 change | Drop of 4% to 9% in raw (d11) |
| T9 | Items with a check that fails early | Run-to-completion vs stop at first failure | Hint quality; solve rate | Better coverage in 55% of cases (b28) |
| T10 | Items without a failing test | Agent writes a failing check first vs goes straight to localising | Solve rate | Likely gain; untested (K18) |

## 9. What does not transfer, and why

- Human results (K09). The agent is not a human reading a list. Top-5 reading habits and trust are human. The analogue is anchoring, which d08 supports only for repair agents.
- The formula race. The ranking formulas assume tens of runs and block-level coverage. Our agent has 3 to 5 attempts, so a11 and a10 are tiny and ties are common. The formula is irrelevant anyway (K02).
- Mutant-based evidence. It reversed on real faults (K05).
- Defects4J scores. Java, probable memory (K32), different granularity (K20). Do not read these as agent gains.
- Value spectra (K19, K30). Data-flow spectra cost 353% overhead; SemLoc cost 2.2 to 3.0 times tokens and did not beat a plain call. Our agent can simply print values.
- Fine-tuned localisers (LLMAO). We do not train (G7 and the project aim).
- Multi-agent pipelines (AgentFL, LLM4FL). Their gains come with several roles and reflexion loops. G9 says no debate; the evidence here shows tools, test analysis and navigation helped, not argument between agents. Only the test-failure analysis and code-navigation components transfer.
- Industrial Philips cases. Four cases, estimated by the authors and called debatable (a09).
- Omission faults and non-executable lines. Not visible to coverage (a15). A reasoning error that is a missing step also has no step to blame.
- Repair-agent results (K26). Strong repair agents already read the failing output and explore the repository. Our reasoning attempts are not software repair.

## 10. Open questions

1. At equal tokens, does a spectrum hint added to a strong agent with the failing output beat the failing output alone? No direct study (K34).
2. Do 2025 to 2026 reasoning models (o3, Claude, Gemini 2.5+) gain from plain Ochiai hints? Only indirect: localiser hints gave -4.45 to +0.40 points (K26).
3. Does an LLM follow a spectrum whose top item is wrong because of coverage collapse? Only tested with wrong file lists (K25).
4. Which hint form is best: ranked list, scores, or covered-line diff between failing and passing runs? No direct comparison.
5. Does FLITSR-style recompute work in an LLM loop, and how many rounds before the spectrum is useless? Not studied (K35).
6. Does the spectrum idea work on non-code reasoning attempts with step checks? Not studied (K31).
7. How do flaky tests, early termination and few failing tests affect LLM-based localisation? Not studied (K35).
8. How much of the LLM edge on Defects4J survives on fresh bugs under matched tie rules and granularity? Not studied.
9. Do value spectra beat an agent that prints variables? Not compared (K30).
10. Human conflict: Xie et al. (2016) stays unopened, N=207 unconfirmed.
11. LLM4FL Top-1 is 326 in one place and 327 in another.
12. Abreu 2006 Table 2 labels for tcas and tot_info are unverified.

## 11. Sources

[V] means opened and read this session (full paper or substantial text). [M] means snippet only or seen only through another paper.

| Source | Mark | URL |
|---|---|---|
| Abreu, Zoeteweij, van Gemund (2006) An evaluation of similarity coefficients for software fault localization | [V] | https://webarchive.di.uminho.pt/haslab.uminho.pt/ruimaranhao/files/azg_prdc06.pdf |
| Abreu, Zoeteweij, Golsteijn, van Gemund (2009) A practical evaluation of spectrum-based fault localization (JSS) | [V] | https://webarchive.di.uminho.pt/haslab.uminho.pt/ruimaranhao/files/jss |
| Abreu et al. (2006) Automatic fault diagnosis in embedded software | [V] | https://webarchive.di.uminho.pt/haslab.uminho.pt/ruimaranhao/files/psc |
| Abreu, Zoeteweij, van Gemund (2007) On the accuracy of spectrum-based fault localization | [M] | n/a |
| Jones, Harrold, Stasko (2002) Visualization of test information to assist fault localization | [M] | https://dl.acm.org/doi/10.1145/581339.581397 |
| Jones, Harrold (2005) Empirical evaluation of the Tarantula technique | [M] | n/a |
| Wong et al. (2016) A survey on software fault localization; Naish et al. (2011) | [M] | https://dl.acm.org/doi/10.1145/2000791.2000795 |
| de Souza et al. (2016) survey of spectrum-based fault localization (source of Naish, Debroy, Xie, Xie 2016, Xia, GZoltar, Kochhar summaries) | [V] survey; its summaries of others [M] | https://arxiv.org/abs/1607.04347 |
| Pearson et al. (2017) Evaluating and improving fault localization | [V] | https://www.cs.umass.edu/~brun/pubs/pubs/Pearson17icse.pdf |
| Zou, Liang, Xiong, Ernst, Zhang (2019) Empirical study of fault localization families | [V] | https://arxiv.org/pdf/1803.09939 |
| Rezaalipour and Furia (2024) Fault localization in Python programs | [V] | https://arxiv.org/abs/2305.19834 |
| Rafi et al. (2025) SBEST | [V] | https://arxiv.org/abs/2405.00565 |
| Callaghan and Fischer (2023) FLITSR | [V] | https://arxiv.org/abs/2306.09892 |
| Uddin et al. (2025) Early test termination | [V] | https://arxiv.org/abs/2504.04557 |
| Gruber and Fraser (2023) Debugging flaky tests using SBFL | [V] | https://arxiv.org/abs/2305.04735 |
| Ribeiro et al. (2019) Data-flow coverage in SBFL | [V] | https://arxiv.org/abs/1906.11715 |
| Parnin and Orso (2011) Are automated debugging techniques actually helping programmers? | [V] | https://web.eecs.umich.edu/~weimerw/2018-481/readings/debugging-helping.pdf |
| Xia, Bao, Lo, Li (2016) Automated debugging considered harmful considered harmful | [V] | https://xin-xia.github.io/publication/icsme161.pdf |
| Xie et al. (2016) Revisit of automatic debugging via human focus-tracking analysis | [M] closed access | https://doi.org/10.1145/2884781.2884834 |
| Wu et al. (2023) Large language models in fault localisation | [V] | https://arxiv.org/abs/2308.15276 |
| Kang, An, Yoo (2024) AutoFL | [V] | https://arxiv.org/abs/2308.05487 |
| Kang et al. (2023) AutoSD | [V] | https://arxiv.org/pdf/2304.02195 |
| Yang et al. (2024) LLMAO | [V] | https://arxiv.org/abs/2310.01726 |
| Ji et al. (2024) Impact of LLMs of code on fault localization | [V] abstract | https://arxiv.org/abs/2408.09657 |
| Widyasari et al. (2024) FuseFL | [V] | https://arxiv.org/abs/2403.10507 |
| Qin et al. (2025) AgentFL | [V] | https://arxiv.org/abs/2403.16362 |
| Xu et al. (2025) FlexFL | [V] | https://arxiv.org/abs/2411.10714 |
| Rafi et al. (2025) LLM4FL | [V] | https://arxiv.org/abs/2409.13642 |
| Rafi and Chen (2026) Order Matters | [V] | https://arxiv.org/abs/2412.18750 |
| Farzandway and Ghassemi (2026) SieveFL | [V] | https://arxiv.org/pdf/2605.13491 |
| Yang et al. (2026) SemLoc | [V] | https://arxiv.org/pdf/2603.29109 |
| Xu et al. (2025) LLMs for novice program fault localization | [V] | https://arxiv.org/abs/2512.03421 |
| Xiao et al. (2026) LLMs for fault localization: an empirical study | [V] abstract and intro | https://arxiv.org/abs/2510.20521 |
| Zhang et al. (2024) AutoCodeRover | [V] | https://arxiv.org/pdf/2404.05427 |
| Xia et al. (2024) Agentless | [V] | https://arxiv.org/pdf/2407.01489 |
| Shi, Yang, Chen (2026) From finding to fixing | [V] | https://arxiv.org/pdf/2610.25826 |
| Sepidband, Pham, Hemmati (2026) Role of fault localization context | [V] | https://arxiv.org/pdf/2604.05481 |
| Haroon et al. (2026) Impact of code changes on fault localizability of LLMs | [V] | https://arxiv.org/abs/2504.04372 |
| Zhong, Wang, Shang (2024) LDB | [V] | https://arxiv.org/abs/2402.16906 |
| Zhang et al. (2025) Which agent causes task failures and when? (Who&When) | [V] | https://arxiv.org/pdf/2505.00212 |
| Du et al. SA-BCL, as described in SieveFL | [M] | https://arxiv.org/pdf/2605.13491 |
