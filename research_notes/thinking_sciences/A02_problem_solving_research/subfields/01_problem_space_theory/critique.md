# Critique: Problem-space theory (cross-check)

Checked: evidence_a, evidence_b, evidence_c (about 90 lines). Claims in claims.jsonl (K01-K21). Sources re-opened this session as PDF text: Newell, Shaw, Simon 1958; Yao 2023 (ToT); Hao 2023 (RAP); Zhou 2023 (LATS); Sel 2023 (AoT); Katz 2024 (Thought of Search); Valmeekam 2024 (o1 / Strawberry Fields); Lawsen 2025; Fansher et al. 2022.

## 1. Numbers re-checked

Confirmed exactly:
- LT proved 38 of the first 52 theorems (73%); Theorem 2.48 about 45 min vs about 15 min with preparation of about 20 s (a02, a04).
- ToT Game of 24: IO 7.3, CoT 4.0, CoT-SC 9.0, ToT b=1 45, b=5 74; best of 100 CoT 49, IO 33; about 60% of CoT samples fail at step one (a21, b01, c01).
- ToT crosswords 78/60/20 (ToT), no prune 65.4/41.5/5, no backtrack 54.6/20/5 (c03).
- RAP Blocksworld table (CoT 0.17/0.02/0.00; RAP(20) 1.00/0.88/0.42; GPT-4 CoT 0.50/0.63/0.40); GSM8K 29.4/46.8/48.6/51.6; PrOntoQA 94.2/78.8 vs 87.8/64.8.
- LATS HumanEval 83.8 (GPT-3.5), 92.7 (GPT-4); HotPotQA ablations .37/.42/.58/.63.
- AoT table: ToT b=5 69% with 109.1 queries, AoT 71% with 1 query.
- Thought of Search: $40 / $200 / $14,000 / $16,000 estimates; 1361 of 1361 Game of 24 solved; Blocksworld 50,143 expansions, about 14 days and over $1000.
- o1-preview 97.8%, Mystery 52.8%, randomized 37.3%, 23.63% at 20-40 steps, 27% unsolvable flagged.
- Fansher Exp 1 n=129, 4-disk 100 vs 91 (chi2=4.45, p=.03), 5-disk 93 vs 63 (p=.001); Exp 2 n=371, 95.54 vs 87.57 (p=.009), 5-disk 87.37 vs 55.25.

## 2. Corrections made

1. c22 (Lawsen): the evidence said a 64k output limit puts the Hanoi ceiling near N=7-8. That was the paper's first version. The current version (v2) uses 10 tokens per move and the 2^N-1 move list; it gives a ceiling of N about 12-13 at 64k. Lawsen's point is then that observed collapse (before N=9) happens well below the token limit, so models stop early. Weaker than first recorded. Also the evidence is informal (a tweet replication, "preliminary", no count table).
2. c01 (ToT cost): the finding "less than brute-force sampling" is wrong in dollars. ToT is $0.74 per case vs $0.47 for best-of-100 CoT. ToT used fewer completion tokens (5.5k vs 6.7k) and won on accuracy. The paper's own Table 7 text is inconsistent (garbled in extraction; prompt tokens 1.4k vs 2.2k also favour ToT, yet dollars favour CoT). Treat dollars as stated, tokens as uncertain. The "5 to 100 times CoT" line was not found in the paper text I read; unverified.
3. a19 (Fansher transfer): 79.3% vs 65.4% is real but borderline (B=.98, p=.0488) and Exp 1 showed no such effect (B=-0.53, p=.57, wrong direction). Downgraded to contested (K13).
4. c05 / a24 (RAP "33% relative gain over GPT-4"): the headline is the paper's own average. Per length, RAP(20) beats GPT-4 CoT by a wide margin at 2 steps (1.00 vs 0.50) and 4 steps (0.88 vs 0.63) but at 6 steps only 0.42 vs 0.40. The gain is mostly on short plans. RAP also uses a 33B model and RAP search with 10-20 iterations; no token-matched GPT-4 baseline.
5. a27/c09 (LATS node counts 84.05 / 70.60 / 66.65): the PDF table layout is garbled; the assignment of numbers to ToT, RAP, LATS is inferred from row order. Likely right, not certain.
6. LATS HumanEval and HotPotQA numbers mix "LATS (n=10)", "LATS (CoT)", "LATS (ReAct)" variants. Compare like with like only.
7. ToT self-reported 74% vs 69% when AoT authors re-ran it (a21 vs c16). Katz also quotes ToT as 75% on 100 medium problems. Spread of 69-75% is rerun and subset noise, not a contradiction.

## 3. Contradictions between sources

- Is search the source of ToT/RAP/LATS gains or is it the verifier? Kambhampati (c11) argues the checker; ablations inside ToT (b03) and LATS (b08) show pruning, backtracking and value function each matter. Both can hold: search needs a reliable evaluator. Open: how much is search vs checker at equal tokens.
- Illusion of Thinking (c19, c20) says collapse is real at about 8 disks even with the algorithm given. Lawsen (c22) says it is an artifact. Varela (c23) and Su (c24): stepwise prompting delays but does not remove failures, and the tool-per-move agentic setup collapsed earlier. Net: neither side clean. Contested.
- o1 results (c12) show big Blocksworld gains with no explicit search, which weakens the claim that explicit search is the only route; but renaming and length drop it again.
- AoT (one query, 71%) vs ToT (about 100 queries, 69-74%) vs Thought of Search (code, 100%): the same task solved at three very different costs. Game of 24 is a task where the best scaffold is code, which limits what it says about open tasks.

## 4. Weak spots

- Almost all LLM search evidence is on Game of 24, Blocksworld, crosswords, Sudoku, Hanoi: well-defined, checkable puzzles (b27). Nothing on ill-defined problems.
- No paper compares search and best-of-N at fully equal dollars and tokens on varied tasks. The only equal-ish comparison is ToT Table 7, and it is mixed.
- Most numbers are single runs of closed models (2023 GPT-4 versions), small test sets (ToT crosswords 20 games, Game of 24 100 items, Long Sudoku 10 per size). No confidence intervals.
- Independent replication is thin: the only one is a student project (b10), which found the tree-vs-chain gap shrinks with a good value function.
- Evidence "independent_sources" counts in claims treat different papers by the same group (Kambhampati) as separate; this is generous (K09, K14).

## 5. Only seen in snippets or not opened

- Newell and Simon 1972 book (a30), Kotovsky/Hayes/Simon 1985 (a32, b20), Kotovsky and Simon 1990 (b21), Kaplan and Simon 1990 (a33), Jeffries 1977 (a31), Ohlsson 2012 (a34), Oellinger 2013 (b23). The human-side core of problem-space theory (isomorph effects, protocol studies) is therefore not quantified in this folder.
- b12 PlanBench table 1, b07 WebShop numbers: garbled, not recorded.
- b26 (majority voting does not help over trees): search summary only.
- Not re-opened by me: b10, b17, b19, c25-c30, a29. Taken as written.

## 6. Second pass (after evidence_a grew to a72, b to b35): re-checks and corrections

Evidence added since the first pass: Logic Theorist and GPS reports (a35-a43), Simon 1972/1975 (a44-a49, a56-a58), Laird and Rosenbloom 1992 (a50-a54), Anderson and Douglass 2001 (a59-a61), Kotovsky and Simon 1990 and Kotovsky and Fallside 1988 (a62-a72), Brown 2024, Sprague 2024, Koh 2024, Valmeekam 2024b, Knoblich 1999 and others (b29-b35). Claims K22-K34 were added.

Re-opened this session (PDF or abstract text): Brown 2024 (b29), Sprague 2024 (b30), Koh 2024 (b31), Valmeekam 2024 (b32, c12, c13), Kotovsky and Simon 1990 (a62-a67), Anderson and Douglass 2001 (a60, a61), Knoblich 1999 (b33), Fox et al. 2011 (b35, abstract via OpenAlex).

Confirmed exactly: SWE-bench Lite 15.9% to 56% at 250 samples; Gemma-2B 0.02% to 7.1% at 10,000; Llama-3-8B MATH 82.9% to 98.44%; CoT gains 14.2/12.3/6.9, others 56.8 vs 56.1; up to 95% of MMLU gain on equals-sign questions; Koh 18.9 to 26.4, 15.0 to 19.2, 7.6 to 16.7, 24.5 to 37.0 (c=20, d=5, b=5); o1-preview 97.8%, 52.8%, 37.3%, 23.63%, 27%; calendar $2.70/94% vs $2.48/97%; Sokoban 12.7% to 43.6%; Blocksworld hard 98.2% in 7 iterations; Chinese Ring F(2,21)=33.72, digital 25.48 and 14.55 min, Exp 2 79.7/19.9/13.0 min with F(2,63)=44.96, 24 of 41 failed in two hours, transfer 47.6%/60.5%, All-Info 206 illegal moves, expected-time 77 s = 13%, random-walk 242; Anderson and Douglass F values and 5%/1% stack-inspection rates; Knoblich medians 40/155/300/140 s (N=20); Fox r=-.03, 94 studies.

Corrections:
7. a62: "25 of 26 solved a digital isomorph" is not in the paper text. What the text says: 26 students; 12 attempted the Chinese ring, 1 solved it in 90 minutes, one other made progress; digital mean times 25.48 and 14.55 min. The 25-of-26 figure should not be used.
8. a63: the 79.7 min mean for the Chinese ring includes non-solvers scored at the time cap (the paper says so in a footnote), so it is a floor, not a true mean. 24 of 41 did not solve in two hours.
9. b31: the +51.0% (24.5 to 37.0) is with self-consistency (n=20) in the value function; without it the same search gets 28.5%. The "20 times more calls" is the paper's upper bound for c=20, per search iteration, not a measured average.
10. b32: the cost table text is staggered, so row labels do not line up with numbers. The text confirms Sokoban 12.7 to 43.6 and graph coloring "up to 94%"; the 64 to 94 row in the table may be trip planning or graph coloring. Use the prose figures only.
11. a68 / a70: the 2:1 and 16:1 isomorph ratios are quoted by the same school in later papers (Kotovsky and Simon 1990 confirmed the 16 times wording, Kotovsky and Fallside 1988 the 16:1 ratio). The 1974, 1977 and 1985 originals were not opened. K25 stays "established" because the Chinese Ring data are first hand, but the exact ratios are secondhand.
12. K25 counts Kotovsky and Simon 1990 and Kotovsky and Fallside 1988 as separate sources; they are the same lab and school. Treat independence as about 2, not 3.

## 7. New contradictions and weak spots

- Brown 2024 (repeated sampling, coverage) vs ToT/LATS gains: coverage with an oracle checker is an upper bound; picked-answer accuracy without a checker plateaus. So search wins mostly where the evaluator, not the proposer, is the bottleneck, and ToT never ran against a checker-matched sampling baseline at equal tokens. Valmeekam 2024b shows a cheap model in a verifier loop beats an expensive reasoning model, which points the same way.
- Human protocol work (a50-a52, a56-a61) shows people mix strategies and lack a perfect goal stack; Soar and the LLM-search papers assume clean stacks. The LLM papers do not test whether goal-stack loss matters in a context window.
- Think-aloud is nonreactive on accuracy (Fox) but explaining helps, and insight tasks may be harmed by verbalising (Schooler, contested). The one scaffold-relevant claim, "write the reasoning out", is therefore task dependent.
- Isomorph results (a62-a72) show representation dominates difficulty, but all human data are small-cell (cells of 7 to 14, a few Hanoi n=129 and 371 from Fansher) and use time with caps.
- LLM isomorph sensitivity is shown only for planning (Mystery Blocksworld, c10, c12) and ARC encoding (b17); no study applies the Kotovsky operator-compatibility transfer asymmetry to LLMs.
- a29 (AlphaLLM) mixes training and search; it cannot be credited to a scaffold.

## 8. Still only snippets or not opened

Newell and Simon 1972 (a30), Jeffries 1977 (a31), Kotovsky/Hayes/Simon 1985 (a32, b20), Kaplan and Simon 1990 (a33), Ohlsson 2012 (a34), Oellinger 2013 (b23), b26, b28 (a question list), b35 full text (abstract only), Schooler 1993 (b34) via secondary summary, c25 per-cell numbers, a55 summary only. The first-hand human protocol numbers from the 1972 book are absent.

## GAPS

1. At equal total tokens and dollars, does tree search with a coded goal test beat best-of-N with the same coded verifier on our own task mix? (Brown 2024 and Valmeekam 2024b suggest sampling plus a checker is hard to beat; no paper runs the matched comparison.)
2. How much of ToT/LATS/RAP gain is search and how much is the evaluator? Replace search by plain resampling with the same evaluator (K09 vs K03, K07).
3. Does writing operators and goal test as code (Thought of Search, K11) transfer from puzzles to messy tasks, and what is the first-try failure rate of generated code?
4. Is the Hanoi / River Crossing collapse real once state is held by a program and instances are valid? A clean rerun with counts at sizes around the threshold is missing (K15, K16, K32).
5. Does the search gain survive on the smaller model we would deploy? (GPT-3.5 ToT 19% vs GPT-4 74%, but Llama-3-70B gained most in relative terms in Koh; contradictory direction.)
6. Where is the gating threshold (G1): what fraction of items a cheap first pass solves before search pays for itself, per task type; CoT gain is concentrated on symbolic steps (K23).
7. Do LLMs show the Kotovsky operator-compatibility effect and move-demonstration effect (K25)? That is, does a worked move demonstration or an explicit legality check close a representation-driven gap at small token cost?
8. Does a forced restructure operator (S7) help on insight problems where search stalls, and can an impasse be detected from state alone (K21, K31)?
9. Do impasse triggers (Soar) beat confidence triggers for escalating from fast to deliberate mode in an LLM scaffold (K19)?
10. Does keeping subgoals in a written, re-read goal stack beat the implicit stack in context at depth 5 or more, given that people lose goals (K27)?

## Gap search results

Evidence in `evidence_d.jsonl` (d01 to d18, all opened as full text). Claims K35 to K43 are new; K03, K04, K07, K08, K11, K15, K16, K19, K21, K25, K27, K32 gained evidence; K08 moved to contested.

| Gap | Status | What the new evidence says |
|---|---|---|
| 1 Search vs best-of-N, coded checker, equal cost | Open (partly informed) | No paper runs it. Naive MCTS lost to sampling at every FLOP budget, reward-guided REBASE won with about 7x less compute (d03). With a learned verifier, tree search beat weighted voting by 0 to 4 points on GSM8K at 1 to 3x tokens (d17). Wang 2024: ToT wins at GPT-4, loses to self-consistency at GPT-3.5 (d01). K35 (contested). |
| 2 Search vs evaluator | Partly closed | Random evaluator collapses ToT, cheap GPT-3.5 evaluator keeps 72% vs 76%, weak proposer gives 0.38 (d02). Still no arm that swaps the tree for resampling with the same evaluator. K36. |
| 3 Code operators on messy tasks | Half closed | First-try failure rate is now known for puzzles: 1.2 to 2.8 tries for GPT-4 successor code, 2.0 to 10 calls with automatic tests, most errors in successor soundness and completeness (d06, d08, d09). Transfer to fuzzy rules is untested; every domain had exact short rules. K38. |
| 4 Hanoi collapse rerun | Mostly closed for Hanoi, open for River Crossing | MAKER solved 20-disk Hanoi with zero errors using single-move calls, state in prompt, strategy given, per-step voting (d10, d11). One run, authors' system. A clean count table at sizes around the threshold with the same model on both designs is still missing, and nothing new on valid River Crossing instances. K39. |
| 5 Small model | Partly closed | Direction depends on who judges. Small model plus strong evaluator gains (Llemma-7B beat 34B, d04); small model as proposer and judge loses (d01, d02). Small per-step error rates are enough for voting if p above 0.5 (d11). Our actual deployment model is untested. K08 now contested. |
| 6 Gating threshold | Partly closed | Search hurts on easy items and helps mid items (d05, d04). Model-specific difficulty bins from a cheap pass beat labelled difficulty. Exact escalation share per task type for our mix is still unknown. K37 (established on math). |
| 7 Kotovsky effects in LLMs | Open | Only an indirect analogue: 8 worked examples lifted GPT-4 base-9 addition from 38.6% to 85.8% (d18). No operator-compatibility or isomorph-ratio test. K40. |
| 8 Forced restructure, impasse from state | Open | Riddle study shows many failures are non-endorsement of a correct candidate (5 to 39% of errors) (d13), pointing to a verify step. The mental-set paper is too small (d12). K41. |
| 9 Impasse vs confidence trigger | Open | Verbalised confidence has AUROC about 0.52 (d14). A trained step router beat a binary switch (d15). No head-to-head of impasse and confidence in a scaffold. K42. |
| 10 Written goal stack at depth 5+ | Open | Only HiAgent: subgoal text 10% to 40%, with summarised subgoal memory 60%, one task (d16). No depth sweep. K43. |

Decision effect on the schema:
- Keep G1 gating; Snell and Wu support it, and the cheap-pass first design is cheap to test.
- Do not assume search beats sampling. Make the matched-cost arm (checker plus resampling or repair loop) the default comparison in our bench.
- Plan a repair loop for generated operator code, and write the tests for it.
- Prefer one-step-at-a-time calls with state held outside the model for long procedures.

Corrections and cautions on these sources:
- d17: the table text in the PDF is garbled; row pairing is my reading, and the 0 to 4 point range is approximate.
- d03: the sample count per row is garbled in the PDF text; FLOPs and accuracy are as printed.
- d10 projections ($3.5K) are the paper's estimates; only one full run is reported.
- d16: number of episodes per task not confirmed.
- d12 is too small to use. d18 is a rule change, not an isomorph design.
- Gap searches by WebSearch worked; nothing was blocked.

Still not opened after this pass: Newell and Simon 1972, Jeffries 1977, Kotovsky, Hayes and Simon 1985, Kaplan and Simon 1990. Searches found no LLM replication of Kotovsky isomorph effects, no LLM test of a forced restructure operator on matchstick or eight-coin items, and no goal-stack depth experiment.
