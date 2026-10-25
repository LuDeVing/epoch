# Critique: Means-ends analysis (cross-check)

Scope: evidence_a, evidence_b, evidence_c (88 lines, a01-a36, b01-b28, c01-c25 minus gaps). 28 claims written to claims.jsonl (A02.02-K01 to K28).

## Sources re-opened (full PDF text, this session)
- Li and Kingsford 2026 (MEDAKA), arXiv 2610.24928: Tables 2, 3, 5, 7 and text.
- Kazemi et al. 2023 (LAMBADA), arXiv 2212.13894: gains, 28%, 48%, 29%, call ratios.
- Prasad et al. 2024 (ADaPT), arXiv 2311.05772: ALFWorld, WebShop, TextCraft, depth test.
- Lawsen 2025, arXiv 2506.09250: token arithmetic, N>5 statement, under 5,000 tokens.
- Valmeekam et al. 2024 (o1), arXiv 2409.13373: 587/600, 317/600, 224/600, 23.63%.

Not re-opened: PDFs for Stechly et al. (2405.04776), Thinking Forward and Backward (2411.01696) and MAKER (2511.09030) downloaded damaged (xref errors, 3 retries). Their numbers are unchecked by me.

## Corrections made
1. b04 swapped the Gemini ablation columns. It said minus recursive 76.0 and minus state tracking 75.1. Table 5 of the paper gives Gemini minus State 76.0 (-6.0) and minus Recursive 75.1 (-6.9). c02 had it right. Claim K13 uses the correct order. Claude values (90.5 minus state, 91.0 minus recursive) were right in both.
2. b02 and c01 per-tag numbers confirmed against Table 2 (Claude nonlinear 33.3 / 55.3 / 87.4; GPT-5.4 nonlinear 28.9 / 49.1 / 46.5; Gemma4 4B 14.5 to 12.6). One trap: the pass@3 table (Table 4) also has a 33.3 in a different cell, so the two tables are easy to mix up.
3. b01 says Medaka beats CoT pass@3 "on 4 of 7 models". Confirmed (not GPT-5.4, not the two Gemma4).
4. Token ratio 1.8 to 3.8 times is the paper's statement. From Table 7 medians the ratio per model is roughly 2.0 (Gemini), 2.4 (GPT-4o), 3.1 (Claude), 3.8 (GPT-5.4). Fine, but the gain per extra token is not equal-token evidence.
5. All other checked numbers (LAMBADA +44/56/37/113/43%, 28%, 48%, 3.8x/11.8x calls; ADaPT 71.6/43.3/57.5/44.0/52.0/26.9 to 78.2; Lawsen 10 tokens per move, N about 12-13, under 5,000 tokens; o1 97.8/52.8/23.63) match the sources. No change.
6. c01 describes the authors as "Li and Kingsford 2026" while b01 says "Medaka / Liquidworld authors". Same paper; the preprint is dated 18 Oct 2026, so it is very new and has had no replication.

## Contradictions and tensions between sources
- Cognitive data versus GPS: Greeno (1974) and Thomas (1974) say people organise moves forward in subsequences and some moves go backward from the goal; Jeffries et al. (1977) assumed a fixed noticing order that Schmalhofer and Polson (1986) then rejected for (5,3). The three primary papers were never opened (a24, a25, b27 are snippets), so the status of K07 is contested by default.
- Hanoi collapse: Shojaee (collapse before N=9, algorithm in prompt does not help) versus Lawsen (output limit, code answer works at 15 disks) versus Dellibarda Varela (still trouble near 8 disks) versus c16 (a move-by-move interface made it worse). The sources do not agree on how much is real reasoning failure. Lawsen is a short, unpowered comment partly written by an LLM.
- Backward chaining: LAMBADA says backward goal-directed search wins; c03 says GPT-4o plans worse backward than forward in all four domains. These are different tasks (deduction over rules versus state-changing planning), and LAMBADA's own control shows backward CoT alone is not clearly better. So the gain comes from the modular, code-held loop, not from the direction.
- AoT+ (b16) claims to match LLM-Modulo with an external verifier at fewer tokens; MEDAKA shows AoT+ is worse than CoT on GPT-4o and Llama. Search-style prompting is model-dependent.
- b09 and c12 (Shojaee) were read via fetch summaries or not at all (c12 PDF not opened), yet the collapse numbers in b09 are used in K21 and K22.

## Weak spots
- Almost all positive LLM evidence for explicit means-ends is ONE preprint (MEDAKA), on one synthetic domain, thinking mode off. The gain may shrink with reasoning mode on. No second domain.
- The classical evidence is old and on tiny domains (logic, 3-5 disks). Newell and Simon (1972) was never opened (a36 is a quote via Norvig), so GPS-to-protocol fit statistics are missing.
- Independent source counts are inflated if one group appears twice: a29, a30 and b22 are the same Fansher et al. data; b14, c07 and c08 are one Stechly paper; b01, b02, b03, b04, c01, c02 are one paper. I counted these as one source in claims.
- Hobbits and orcs (Thomas, Greeno, Simon and Reed, Jeffries) is the focus of the subfield and has only second-hand coverage. Same for Anzai and Simon, Korf, Chapman.
- STRIPS and Prodigy evidence is from the authors of the systems (a16, a17, a18). Only Graphplan (c23) is an outside comparison, and on 1990s machines.
- c10 numbers are re-quoted from other papers of the same group.

## Only seen in snippets or abstracts
a19 (summary only), a23, a24, a25, a26, a31, a32, a33, a34, b26, b27, b28, c12, c15, c24, c25. Treat as pointers, not evidence.

## GAPS
1. Does an explicit means-ends scaffold (goal-difference, subgoal stack, state ledger) still help when the model reasons natively (thinking on), and at equal tokens against CoT pass@k plus a verifier? MEDAKA only tested thinking off and gave the scaffold 1.8-3.8 times the tokens.
2. Which part carries the gain: the subgoal stack, the state ledger, or the difference naming? MEDAKA ablated two parts but not a stack-only arm; no study isolates the "difference" step.
3. Does the gain transfer outside continuous-state mixing, for example to ARC-style grid tasks, puzzles, code, and open reasoning questions where no clear goal state exists?
4. What does the original human data (Thomas 1974, Greeno 1974, Jeffries 1977, Simon and Reed 1976) show about when people break away from means-ends (detours, moves away from the goal), and can that be turned into a rule for when the agent should allow a non-greedy move?
5. How wrong can the difference-operator table or the model's difference naming be before means-ends does worse than free CoT? No study measured table-error tolerance, and for an LLM the table is generated by the model itself.
6. How often does goal clobbering (Sussman-type interaction) occur in LLM outputs on multi-goal items, and does a final all-goals check or goal protection fix it at small token cost?
7. When to decompose: always, or only on failure (ADaPT)? ADaPT used GPT-3.5; does as-needed decomposition still beat always-decompose with current models, and at what depth cap?
8. Is the Hanoi collapse real once code holds the move list? A clean test of "model chooses next step, code holds state and output" on N at 8 to 15 would settle the Shojaee-Lawsen dispute for our design.
9. Does a learned control-rule memory (Prodigy/HAMLET style, 218 to 135 unsolved) carry over to an LLM agent, and does it survive a change of problem class (the EBL transfer failure in a18)?
10. How reliable is the model as its own progress or subgoal checker (F1 0.68 in c19, verifier near chance in c20)? What checker accuracy is needed for subgoal checks to help rather than add false progress?


## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d22; d03, d04, d05 are abstract-level and not opened). Claims K02, K07, K12, K13, K17, K18, K19, K21, K22, K23, K28 were updated and K29 to K34 added. The web search quota ran out partway, so some searches were done through arXiv HTML pages only. No gap is fully closed.

Overall: 2 gaps narrowed to a specific design test (2, 8), 3 gaps got useful indirect evidence (5, 7, 10), 2 gaps gained a candidate rule or negative result (4, 9), 3 stay open (1, 3, 6).

1. **Thinking on, equal tokens, against CoT pass@k plus verifier: OPEN.** MEDAKA was re-read (d22): thinking was turned off on purpose and external verifiers were left out on purpose. Nothing tests a means-ends scaffold with thinking on. Indirect: a plain step-by-step prompt gives little to reasoning models and Gemini Flash 2.5 lost 13.1 points at the 100%-correct metric (d13, GPQA, not planning); under equal tokens thinking and non-thinking are comparable on math but differ on medium puzzles (d07). Expect small gains and some risk; test before shipping.
2. **Which part carries the gain: PARTLY ANSWERED.** Reading the MEDAKA ablation closely (d22) shows each single-module arm alone recovers most of the gain over CoT. Claude: decomposition only 90.5, tracking only 91.0, CoT 77.8, full 94.5 (76% and 79% of the gain). Gemini: 76.0 and 75.1 against 65.6 and 82.0 (63% and 58%). The "state tracking" arm also carries the numeric calculation instructions, so a pure ledger and a pure stack arm still do not exist. Nothing isolates difference naming. A separate fine-tuned-model result (d17) says a goal-distance count hurt out of distribution while exact state and effects helped inside the trained length range. Next test: four arms (ledger, calculation hints, stack, difference naming).
3. **Transfer beyond continuous mixing: OPEN.** Positive transfer evidence is on ALFWorld, WebShop, TextCraft (d12), and elsewhere LAMBADA; code-held search covers puzzles with an explicit goal test (d11: 100% on 1,362 24-game, 502 Blocksworld, 4,000 PrOntoQA items). No study found for ARC grids, code repair, or open questions without a goal state.
4. **Human data on breaking from means-ends: PARTLY ANSWERED, still second-hand.** Thomas 1974, Greeno 1974, Jeffries 1977 and Simon and Reed 1976 are paywalled; I only got abstracts (d03, d04, d05, not opened). The Schmalhofer and Polson 1986 full text (d01, d02) is the best open source: no fixed noticing order (120 students, all F<1); behaviour is a probabilistic mix of means-ends and a constraint-driven balance strategy; moves are filtered by a visited-state memory and an avoid-backward-move check; and the subgoal is only recognised after it is accomplished. Removing the balance strategy dropped fit for (4,3) to r=.76 and (5,3) to r=.78 (from .93 and .94). Levin et al. (d06): solvers who had to justify each move against the goal made 17 instead of 27 moves and repeated 22.4% instead of 40.2%, and pairs restarted when stuck. Candidate rule (K30, hypothesis): allow a non-greedy move only on loop, on a constraint conflict, or when no operator reduces the difference; allow a reset to start. Needs an LLM test.
5. **How wrong can the table be: OPEN, indirect evidence only.** Nearest is Wang et al. (d14, 2022 model): invalid but relevant, ordered reasoning kept about 80% of the CoT gain (GSM8K 39.5 vs 48.5, standard 15.4), irrelevant content was below no-CoT (11.0). Nothing on operator tables or difference naming. Suggested test: inject wrong, vague and irrelevant differences.
6. **Goal clobbering rate: OPEN, no direct study found (K34).** Only hints: strong multi-goal gains from decomposition in MEDAKA, loops of pick-up/put-down in stepwise agents (d19). A final all-goals check was not tested anywhere I could find.
7. **Always decompose or only after failure: PARTLY ANSWERED, old models.** ADaPT was also run with GPT-4, LLaMA-2 70B, Lemur, not only GPT-3.5 (correction to the gap text); gain rises with depth cap 1 to 2 to 3, and on WebShop always-decompose (17.0) was worse than the plain executor (29.0) and as-needed (44.0) beat both (d12). All models are from 2023; no current or thinking model. Cap near 3 is supported, not proven for current models.
8. **Hanoi with code-held state: NARROWED, partly contested (K21, K22, K23).** (a) The MAKER 20-disk run was a completed run, not a projection (corrects K23); it gave the algorithm and state in each one-step prompt, used k=3 voting and an output-length red flag, error rate about 0.0045, no error in 1,048,575 steps (d10). (b) When the model only chooses moves in a tool-call environment with state returned and no algorithm given, collapse still came earlier and showed loops, 40% deterministic reuse at n=8 (d08, single run, n up to 8). (c) Stepwise p-move prompting still failed from about N=8 (d09). (d) The Apple reply puts the first error at move 40 of 255 (d07). The tidy reading: long runs are lost to step errors and loops; short steps plus the known algorithm plus voting fix it; the model finding the strategy is a different question. The exact test (8 to 15 disks, algorithm given or not, voting or not, visited-state guard) is still to run.
9. **Learned control-rule memory carry-over: PARTLY ANSWERED for LLM agents, not for planning control rules.** ExpeL transfer HotpotQA to FEVER 63 to 65 or 70 (d21); AWM gains hold across websites and domains online but offline memory loses its edge as the gap widens (d20). This matches the Prodigy transfer failure: memory matched to the current class helps, mismatched memory fades. Tag by class and retire on change.
10. **Model as its own checker: STRONGER NEGATIVE, threshold still unmeasured.** GPT-4 as verifier had false-negative rates of 20.7%, 95.8%, 97.1% (d15); self-correction without outside signal lowered GPT-3.5 CommonSenseQA from 75.8 to 38.1 (d16); GPT-3.5 accepted every Blocksworld plan (d18); a fine-tuned 7B model detected wrong steps with precision 90.5% and recall 99.2% yet validity did not improve (d17). A rough rule I derived, not from a source: if the checker is run on every subgoal, expected false progress is roughly (rate of wrong subgoals) times (false-accept rate), and the checker's false-reject rate costs retries; a checker whose accept rate does not depend on truth adds only cost. Treat it as an untested design hint. Recompute subgoal state from the code-held ledger instead.

Corrections to earlier files: K23 said "projected run"; the paper says the full system solved the problem. K17 and the "not re-checked" note: the forward/backward paper text was opened (d18) and the 4 to 24 point gain and the GPT-3.5 accept-all verifier are confirmed. MAKER numbers (k=3, 20 disks, zero errors) were confirmed from a text copy of the paper.

Still unopened primary sources: Thomas 1974, Greeno 1974 (full text), Jeffries et al. 1977, Simon and Reed 1976, Newell and Simon 1972, Anzai and Simon 1979. The Shojaee page read is the authors' latest HTML version, which includes their replies to critics.
