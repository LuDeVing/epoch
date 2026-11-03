# Expert flexibility and adaptive expertise: deep document

*Subfield A10.02. Built from evidence_a-d.jsonl (ids a01-d22), claims.jsonl (K01-K34) and critique.md in this folder. Evidence ids are cited as a01, b13, d04 and so on. Items marked "second-hand" were read only through another paper. Where the critique found a number unverified, it is flagged.*

## 1. What it is

This subfield asks one question. When a person knows a good method, when does that knowledge help, and when does it block a better method? And what separates people who switch from people who do not?

Three strands sit under it.

1. **Einstellung (set) effect.** A familiar solution, once found, blocks a shorter or better one. Luchins (1942) showed it with water jars. Bilalic, McLeod and Gobet (2008) showed it in chess masters with eye tracking. Later work covers anagrams, card tricks, programming and baboons.
2. **Adaptive versus routine expertise.** Hatano and Inagaki (1984, 1986) split experts into routine experts (fast, accurate, brittle) and adaptive experts (they also know why the procedure works, so they can change it). Schwartz, Bransford and Sears (2005) recast this as two separate axes: efficiency and innovation.
3. **Heuristic toolboxes.** Gigerenzer and colleagues treat the mind as a set of simple, frugal rules (Take The Best and others). Each rule suits some environments. Choosing the rule is the skill. This links to our S6 step: pick an operator when stuck.

The subfield note also names "reflection in athletes". We found almost nothing direct. One paper builds fast-and-frugal trees for elite athletes (b27). It is about decision rules, not reflection. We say so in sections 5 and 10 and do not pad it.

Why it matters for our agent. S6 fires when the agent is stuck, then picks one operator (O1-O8). The human data say: (a) a good first answer is what blocks the better one; (b) people look at the alternative and still do not use it; (c) a warning helps only part way; (d) varied practice helps most; (e) switching has a cost when the old routine was right. Each maps to a testable S6 design choice.

## 2. History and theories in depth

**Luchins (1942).** Water-jar problems. Five set problems are solved by one long method (B - A - 2C). Critical problems then allow a much shorter method. Numbers below come from Binz and Schulz's reconstruction of the thesis data (d11, d12) and from Bilalic's summary (a01, second-hand).
- Plain group: 128 of 155 (83%) used the long method on critical problems C1/C2. Controls with no set problems: 0 of 155. On C3/C4: 100 of 155 (65%) versus 0 of 155. Chi-square 218.02 and 147.62 (d11).
- Extinction problem (only the short method works): 64% of the set group failed; controls 5% (a01, second-hand).
- "Don't be blind" warning: 87 of 153 (57%) still used the long method, versus 83% plain, chi2 = 24.16 (d12).
- Training that alternated long and short problems: 20 of 124 (16%) versus 97 of 121 (80%) plain (d12).
- Time pressure: 95 of 98 (97%) versus 126 of 153 (82%) (d12).

**Saariluoma (1990).** First chess work, second-hand through Bilalic (a08). Exp 2: 10 of 12 players missed the shorter solution. Exp 3, two groups of 6: with the familiar solution present, 11% of choices were optimal and 67% were the familiar non-optimal one. With it disabled, 69% found the optimal one. Bilalic notes flaws: no extinction task, a "mate as fast as possible" instruction, weak players (only 3 above USCF 2100).

**Wiley (1998).** Baseball knowledge hurt on misleading Remote Associates items (a09, second-hand, no figures). Knowledge from one domain misfired in a task where it was not real expertise.

**Bilalic, McLeod and Gobet (2008), three papers.**
- Cognitive Psychology (a02-a07). Quantified the effect in chess masters. Section 3 has the numbers.
- Cognition (a10, a11, b07-b09). Eye tracking. Candidate Masters said they searched for a shorter mate while their gaze stayed on the squares of the familiar mate.
- Specialization paper, 2009 (d19). Knowledge of a familiar opening area acts like about 1 SD of general skill. In their own area players search deeper and narrower; outside it, broader and shallower. Same lab, so not independent. Abstract only.

**Theoretical account (a07).** Chunks and templates (Gobet and Simon): the familiar solution is retrieved first because it is better indexed in long-term memory. ACT-R (strongest production fires) and instance theory (one stored instance wins the race) predict the same fast, hard-to-stop retrieval. The three theories agree that set occurs and differ on how skill reduces it. They were not compared head to head. The authors admit existing theories explain the effect after the fact.

**Sheridan and Reingold (2013) (a12-a14, b01-b06).** A new design: choose-a-move, 3 minute cap, one problem with a good-but-suboptimal familiar move and three where the familiar move is a blunder. This gave the first boundary conditions (section 5).

**Ellis and Reingold (2014) (a15, b11, b12).** Anagrams, 60 students. Familiar words slow solving and add re-checking, but speed the first look. So familiarity helps encoding and hurts integration.

**Not trying versus not seeing (a16, a17).** Pope-Caldwell and Washburn (2022): people look at the shortcut and do not use it. This challenges the attention-capture reading. The authors note the shortcut was very salient in their task, while in chess it is not, so the readings may not be separable there.

**Who escapes (a18).** Ninomiya, Terai and Miwa (2022): finders of the better water-jar procedure already spent more attention on information unrelated to the trained procedure, and the gap grew with repetition. No difference on the first set trial.

**Resource-rational view (b30, d11-d13).** Binz and Schulz (2022). A policy that prefers simple solutions, avoids costly computation and adapts to problem statistics reproduces the Luchins conditions. Plain beta = 25, speedy beta = 15. Simulated: 90 of 100 used the long method after long-only training, 23 of 100 after alternating training (data 0.80 and 0.16). So set can be a rational trade-off, not only an error. The parameters were set by hand to fit one 1942 dataset.

**Adaptive expertise (a19-a22, b32).**
- Hatano and Inagaki (1984): routine experts are fast, accurate, automatic and fail on new problems. Adaptive experts also hold conceptual knowledge of why the procedure works. Three conditions favour the adaptive course: built-in variability so the routine sometimes fails, a context that rewards understanding, and intrinsic motivation. Standardised settings remove the variation needed to learn why. No experiment numbers; the authors call the evidence scanty. The 1986 chapter was not opened.
- Schwartz, Bransford and Sears (2005): efficiency and innovation are two dimensions. Adaptive experts are high on both. After a few hours of invention-based instruction, 34% of high-school students invented a covariance measure; only 12% of top-20 university students did after a full course (different populations). Pie versus tile fractions (Martin and Schwartz 2004): over 50% of pie children who reached the adaptive quadrant regressed the next day; under 15% of tile children did.

**Adaptive toolbox (a23-a25, b24-b26).**
- Gigerenzer and Goldstein (1996): Take The Best checks cues in order of validity and stops at the first that discriminates. On 83 German cities, average proportion correct: Take The Best .658, weighted tallying .658, regression .657, tallying .656, Take The Last .645. With all cue values known: Take The Best .691, regression .694. It searched 2 to 20 cue values.
- Take The Last retries the cue that worked last time. The authors say this is the search principle studied as the Einstellung effect in water-jar tasks (a24). In an early run it exploited a systematic order of test pairs and beat the others by about 10 points, which is why they randomised the pairs. In the toolbox view, set is useful when consecutive problems share structure.
- Fenwick, Campitelli and Thompson (2026): tools are learned, automatised and selected by experience. Natural-frequency formats help novices. Tool selection is a research agenda, not a tested model.

**How expertise forms (b15-b17).** Deliberate practice explains: games 26%, music 21%, sports 18%, education 4%, professions under 1% of variance (157 effect sizes, N = 11,135). A chess SEM reanalysis gave 63% for serious practice, instruction and starting age (34% in an earlier analysis). Estimates depend on the model.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Luchins set: long method kept when a short one exists | 128/155 (83%) vs 0/155 controls on C1/C2; 100/155 (65%) vs 0/155 on C3/C4 | d11 (reconstructed thesis data), a01 | established (K28 single analysis); reconstruction by the authors |
| Extinction problem fails after set | 64% failed vs 5% controls | a01 | second-hand, original not opened |
| Chess: share finding 3-move mate with a 5-move mate present | GM 100%, IM 50%, Master 18%, Candidate Master 0% | a02 (Exp 1) | established as an effect (K01); gradient has no independent replication (K33) |
| Same players, familiar mate disabled | all IM, M, CM solved it (100%); weaker controls Class A 63%, B 13%, C 0% | a02 | single lab |
| Size of the effect | about 3 SD of skill; each 100 Elo fewer cut odds by 3.67 (B = .013, SE = .005, Z = 8.4, p = .004); predicted p: GM .64, IM .32, M .12, CM .01 | a03 | 3 SD figure second-hand to the critique |
| Exp 2 optimal-move rate, 4 problems | IM/GM 92%, Master 69%, Candidate Master 35%; controls A 91%, B 66%, C 47%; GEE B = .006, Z = 3.72, odds factor 1.82 per 100 Elo; experts predicted 97/89/73% | a04 | single lab (K02) |
| Fixation weaker on an easy item | problem 5: all Candidate Masters found the optimal move | a04 | boundary condition |
| Late escape | where not seen at once, IM/GM found it later in every instance; Masters 13/24 (54%); Candidate Masters 11/32 (34%) | a05 | single lab |
| Plan problems (Exp 3) | 1 of 5 GMs and none of the other 7 found the best plan; finder median Elo 2547 vs 2258, U = 2, p = .017 | a06 | N = 12 |
| Gaze stays on familiar squares | 2-solution group: square x time F(5,20) = 0.6 ns. Control group: F(5,20) = 11.9, p < .001, partial eta2 = .75 | a10, b07 | single-source (K03); about 5 per group; 50 Hz tracker |
| Time to settle | blocked group stopped at 37 s (SD 20); controls found the 3-move mate in 79 s (SD 25) | a10 | small N |
| Carry-over cost | 148 s (SD 90) vs 79 s (SD 25), t(8) = 1.67, p = .13, d = 1.2 (ns); Exp 2 vs fresh sub-group t(44) = 2.16, p = .036, d = .65; skill x group F(2,40) = 0.9 | a11, b08, b09 | single-source (K04); between-experiment comparison |
| Boundary: familiar move is a blunder | all 17 experts and most novices avoided it; looking-time trend F(1,66) = 79.88 (experts), 10.84 (novices) | b04, a13 | single-source (K05) |
| Boundary: familiar move good but suboptimal | 8/17 experts and 8/17 novices chose it | a12, b02 | single-source (K05) |
| Experts still better overall | move quality t(32) = 6.04 (rating), 4.93 (engine score), both p < .001 | a12 | one lab |
| Speed to see the trap | first fixation experts 407 ms, novices 719 ms, t(32) = 2.99, p < .01 | b05 | |
| Gaze separates escapers | optimal-move experts (n = 9) trend F(1,34) = 43.45; familiar-move experts (n = 8) F < 1; novices who chose familiar F(1,30) = 1.76, p = .194; dwells higher for escapers F(1,15) = 12.34 | b03, a13 | groups of 8-9, formed after the fact |
| Retrospective reports | 2 of 8 experts and 4 of 8 novices who chose the familiar move never ruled out mate | a14, b06 | self-report |
| Anagrams | RT 15.3 s (word centre) vs 13.4 s (nonword), t(59) = 3.25; accuracy 51.7% vs 53.8% ns; dwells 8.11 vs 6.76 and 10.45 vs 8.53 | a15, b11, b12 | established (K06); cost in speed, not accuracy |
| Not trying versus not seeing | 89.6% did not adopt the shortcut; mean use 9.56% (SD 25.39); 7/67 (10.45%) used it on over half of probes; fixation on shortcut location mu = .53 | a16 | established (K07) |
| Telling people | informed 65.25% shortcut use vs controls 9.12%; 24/34 (70.59%) vs 3/33 (9.09%) over half; 10/34 (29.41%) still did not adopt | a17 | established (K07) |
| Valuing the shortcut | r(67) = .45 after the video, .19 before | a17 | |
| Finders in water-jar task | 31/46 (67%) found the alternative; attention to unrelated information grew with repetition | a18 | proxy |
| Warning (Luchins) | 57% fixated vs 83% plain | d12 | established with forget-instruction data (K29) |
| Alternating practice | 16% vs 80% plain | d12 | single analysis (K28) |
| Time pressure | 97% vs 82% plain (C3/C4: 0.99 vs 0.55) | d12 | |
| Acting on the problem | real jars cut perseveration vs paper (two experiments) | d14 | single-source (K30); abstract only |
| Forget instruction | cut use of practised formula; slowed anagrams that needed it | d15 | abstract only |
| Baboons vs humans | 104 humans (7-68 y) hindered; 15 baboons almost unaffected; ages 7-10 broke set better than adolescents and adults | d16 | abstract only |
| Card tricks | one false solution blocks the obvious one even when told to look again | d17 | abstract only |
| Programming | 57/129 (44%) showed the set; less experience (25 vs 37 months, T = 2.806, p = .006); only 2 of 39 control switched; H(2) = 1.403, p = .496 | d18 | single-source (K32); skill direction opposite to chess |
| Semantic accessibility (2026) | N = 30; interaction F(1,29) = 4.88, p = .035; low access strong 0.70 vs weak 1.27 correct (d = .52); high access 2.07 vs 1.90 ns | b13, b14 | contested (K08); single lab |
| Take The Best vs regression | .658 vs .657 average; .691 vs .694 with full knowledge | a23 | established (K12); one environment |
| Representation vs rule training | after training about 60% (rules) vs 75-90% (frequencies); after 5 weeks about 20% vs still high | b25 | single-source (K13); second-hand |
| Practice variance explained | games 26%, music 21%, sports 18%, education 4%, professions under 1% | b16 | established (K14) |
| Athlete decision trees | trampoline tree 90% correct, volleyball tree 75% (466 athletes, 40% hold-out) | b27 | single study; not reflection |
| Chess players' cognition | 25 vs 25: better Tower of London and Cognitive Reflection; risky-choice evidence weak | b28 | single-source (K27) |

## 4. Mechanisms and models

Each is written so an engineer can build it.

**M1. Retrieval race with a strength advantage (a07).**
- Keep each known method with a strength. Strength grows with use and success.
- On a new problem, score each method by strength x cue match. The top score fires first.
- Skill adds more methods and raises the strength of good ones, so the first-fired method is better more often. It does not remove the race.
- For the agent: the first-proposed approach is the strongest production. Fixation means the first approach wins every time. The first approach can also be right (Take The Last works when problems cluster).

**M2. Satisficing stop with a weak check (b04, a14).**
- After the first method gives a result that passes the check, search stops.
- A blunder gets clear negative feedback, so everyone moves on. A good-but-suboptimal move gets none.
- Rule: fixation risk is high when the familiar method passes a check that can say "good" but not "best". For the agent: when a check returns only pass/fail, a passing first answer ends the search. Add a check that ranks (length, cost, score) or a second route to compare.

**M3. Attention versus effort (a10, a16, a17).**
- Two readings: the first solution holds attention (Bilalic), or the alternative is seen and not adopted (Pope-Caldwell).
- Both predict that a prompt that says a better method may exist raises switching. In humans it did (9% to 65%) but 29% never switched.
- The value placed on the alternative predicts use (r = .45). Implementation: make the agent state the expected saving of the alternative before choosing.

**M4. Carry-over / priming (a11).**
- After a blocked attempt, the old frame persists and roughly doubles time on the next problem (d = .65). The authors read it as decaying priming.
- Implementation: retry in a clean context and compare with a continued context.

**M5. Resource-rational policy (d13).**
- Choose a method with probability proportional to exp(beta x (prior preference - cost)). Lower beta (time pressure) pushes toward the habit (0.97 vs 0.83).
- Alternating training lowers the prior of the habit (0.16).
- Implementation: a per-class prior over methods, updated by outcome. Varied exemplars keep it flat. A token cap acts like low beta, so expect more fixation under tight caps.

**M6. Adaptive expertise: store why (a19-a22).**
- Store each procedure with its rationale: the condition that makes it work. On a changed constraint, check whether the rationale still holds before reuse.
- Variation in practice builds the rationale (Hatano and Inagaki condition 1). Efficiency-only learning regresses (K11).

**M7. Toolbox: search, stop and decision rules (a23, b24, b26).**
- A heuristic has a search rule (which cue next), a stopping rule (stop at the first discriminating cue) and a decision rule.
- Ecological rationality: choose the heuristic by environment structure, not general merit. Take The Best ties full regression on average.
- Implementation for S6: a table from task-structure features to operator, each operator with a stop rule (for example, stop when a child test beats its parent).

**M8. Strategy meta-selector (d08, d09, d10).**
- A contextual bandit (LinUCB) reads a short progress report and chooses continue, backtrack, switch strategy or restart. Game of 24, GPT-4o-mini: CoT 4%, SC-CoT 9%, Reflexion 53%, ToT 65%, MACM 80%, Meta-Reasoner 89% (GPT-4o 92%). Without the bandit (LLM picks the arm) 82. Without the progress report 85. Fixed sets K = 3: 65; K = 5: 72; dynamic 89. Time 29-33% below ToT, Reflexion, MACM and best-of-N. TheoremQA GPT-4o-mini: CoT 39.46, Meta-Reasoner 84.13.
- Oracle headroom: TruthQuest Phi-4 47.2 to oracle 82.9; R1-Distill 63.4 to 90.1; ZebraLogic Qwen3 32.0 to 36.4. HybridMind oracle at least 10.3 points above the best single method; its selector picks the default 94.10% of the time on MATH.
- Implementation: S6 operator choice as a bandit over O1-O8 keyed by problem class, reward = child test result.

**M9. Process metric for fixation (d06, d07).**
- Underthinking score UT = 1 - (tokens until first correct thought / total tokens), over wrong answers, with thoughts split at switch words. QwQ-32B-Preview 58.2, R1 65.4 on MATH500 L5.
- This measures the opposite failure. A mirror metric for fixation is the share of tokens on the first route and the count of distinct routes. Nobody has validated it (K31).

## 5. What holds up

**Replicates.**
- The set effect itself: water jars (Luchins, d11; Vallee-Tourangeau d14; Tempel and Frings d15), anagrams (a15), card tricks (d17), a visuomotor task in humans and baboons (d16), chess (a02, a12), programming (d18). Established (K06).
- Gaze stays on the familiar region in both chess studies (a10, a13), and gaze goes with later choice (b03).
- Telling people helps (9% to 65%, a17) and Luchins' warning helps (83% to 57%). Both agree a warning is partial (K29).

**Failed, null or divergent.**
- No independent replication of the chess GM-to-CM gradient (GM 100% down to CM 0%) among 59 citing records (d20). This is absence of evidence only (K33).
- Sheridan and Reingold did not find a skill advantage on their trap item: 8/17 experts and 8/17 novices chose the familiar move (b02). Designs differ (move choice versus shortest mate; good versus optimal), so this is a boundary result, not a refutation.
- Programming ran the other way: set group had less experience (d18). Interface change and forget-instruction did not help (2 of 39 switched; response-time H = 1.403, p = .496).
- Eye-tracking Exp 1 was underpowered (t(8) = 1.67, p = .13). The carry-over finding rests on a between-experiment comparison (p = .036).
- Luchins' total block was not reproduced in chess: all experts solved the mate once the trap was gone (b08).
- Knowledge helps or hurts: the 2026 study found the induced strategy hurt only at low semantic accessibility (N = 30, p = .035, single lab; b13). Matched-item costs at high access were similar in size but not significant at n = 15 (0.072 and 0.067; b14). Contested (K08).

**Moderators.**
- Cost of the familiar option: a blunder is rejected, a good option is kept (b04, b02).
- Item difficulty: fixation vanished on the easiest item (a04).
- Skill: optimal-move rate 92% (IM/GM), 69% (Master), 35% (Candidate Master) in Exp 2. Part is faster recognition, part is later escape (a05).
- Time pressure raises fixation (97%, d12). Real objects lower it (d14). Children 7-10 broke set better than adults (d16). Valuing the shortcut predicts use (a17).

**Interventions that worked.** Alternating long and short training (83% to 16%, d12). Telling people (9% to 65%, a17). Warning (83% to 57%). Forget instruction (cut perseveration but slowed items needing the old routine, d15). Real objects (d14). Representation training over rule training (b25, second-hand).

**Interventions that did not work.** Forget instruction and interface change in programming (d18). A "complete every idea" prompt in LLMs (R1 AIME24 73.8 to 72.4, d07). Telling LLMs which strategy to use (45.1-49.0 vs 47.2, d10). Generic debate and dynamic agents on MedEinst (robust accuracy 3.20 and 1.19 vs 11.28, d04).

**Practice backdrop.** Practice explains 26% of variance in games and under 1% in professions (b16). Nothing here says practice volume alone yields flexibility.

**Athlete reflection.** No direct study found. The only athlete paper is a decision-tree study (b27). It is not evidence for reflection.

## 6. Language models

No LLM study replicates the Luchins jar task with reasoning models (c28). All evidence is by analogy, benchmark by benchmark.

**Medical Einstellung.**
- M-ARC / mARC-QA (a26, b18, b19, c11, d01): 100 hand-written clinical questions, a familiar cue next to a blocker. Physicians (5) 66% (SE 5.3). arXiv v1: Gemini-1.5-Pro 50%, o1 48%, most models under 50%, several under 20%, medical fine-tunes near 0%. The journal version adds DeepSeek-R1 52% and V3 50%; those are not in arXiv v1 (d01). Larger models in a family do better; Llama 405b scored below 70b (maybe quantisation). On the 20 human-miss items humans scored 36% versus 73% on the rest; DeepSeek-R1 was confidently correct 45% and confidently incorrect 40%. 15 stochastic runs per model.
- Follow-up (b20, b21, d05): Claude 4.1 Opus 0.751 (CI 0.738-0.763) versus physicians 0.66 (CI 0.55-0.75). Gemini 2.5 Pro, GPT-5.1 and Grok-4-Fast-Reasoning not significantly different from physicians. Reasoning variants beat non-reasoning ones at the highest effort setting. On the human-miss set, Claude 4.1 Opus was decisively correct on 55.0%, wrong on 25.0%, indeterminate 20.0%. No trap-warning prompt was tested. Items may have leaked into training.
- MedEinst (c13-c16, d02-d04): 5,383 paired cases, 49 diseases, 17 LLMs, 96.1% of pairs valid on physician review. Bias Trap Rate = misdiagnosing the trap while getting the control right. Table 1 rows (base / robust / trap): Qwen3-32B 44.12 / 11.28 / 43.46; Qwen3-14B 42.20 / 11.32 / 54.19; QwQ-32B 39.65 / 11.25 / 44.88; GLM-4.6 47.82 / 12.46 / 47.63; Qwen3-235B 41.05 / 11.14 / 43.32; GPT-5 40.51 / 11.40 / 51.87; MedGemma-27B 42.09 / 12.36 / 53.88; Lingshu-7B 54.30 / 15.78 / 36.74; Llama3-Med42-8B 53.58 / 10.97 / 44.00. Trap rate alone: Gemini-2.5-pro 60.90, Baichuan-M2-32B 66.10, Kimi-k2 47.12, DeepSeek-R1 46.12. Robust accuracy about 11-12% for most.
- The paper says "stronger priors, stronger blindness". Its own table does not support that: over 8 aligned rows r = -0.69 between base accuracy and trap rate, and the cited 54.30 and 53.58 sit on Lingshu-7B and Llama3-Med42-8B rows, not GPT-5 and Gemini (d03). The table text was garbled, so confirm against the PDF image. Contested (K18).
- GPT-5 error coding: 35% blindness to key evidence; of the rest, 43% underthinking and 22% overthinking (c14).
- Agents on Qwen3-32B (base 44.12 / 11.28 / 43.46): MDAgent debate 14.93 / 3.20 / 40.34; DyLAN 6.51 / 1.19 / 41.69; ECR-Agent 40.92 / 11.68 / 33.75. ECR-Agent ablation: 40.25 to 55.49 (+ causal inference) to 69.49 (+ memory) base accuracy. ECR-Agent adds structure and calls together, so the scaffold effect is not isolated; no equal-token run (K19).

**Red herrings.**
- Only Connect Wall (b23, c01-c03): humans 285 of 494 walls, 1405 of 1976 groups. GPT-4 solved 2-7 walls and up to 269 groups; GPT-3.5 0 walls. OCW-Randomized: GPT-4 5-shot up to 68 walls, 655 groups. OCW-WordNet (decoys removed): about 279-471 walls; 0-shot 415 walls and 1759 groups, 10-shot 471 walls and 1926 groups (pairing corrected by the critique). Best embedding E5-base: 1 wall, 89 groups. More shots did not help. The synthetic variants are also easier, so the gain is not purely decoy removal. 2023 models only.

**Set shifting (Wisconsin Card Sorting Test).**
- Hao et al. (c04, c05): Claude-3.5 Sonnet with chain of thought on text finished 5.00 categories (SD 0), about 67.5% correct-learning; straight answers gave 0.1-0.5 categories and near-chance errors. Visual input was much worse. Human row about 4.7 categories, 65% (table garbled). Role-play impairment prompts raised one model's non-perseverative errors from 3.50 to 20.10.
- Li et al. 2025 (c06-c08, d21): 360 human students versus five LLMs. Most LLMs beat humans on correct matches. Humans make more random than perseverative errors; LLMs except DeepSeek the reverse. 15 prompt variants x 10 repeats with GPT-4o left the pattern unchanged. Not found by title in the critique's re-check; numbers unverified there.
- Reflection-Bench (c09, c10): WCST 72 trials; o1-preview and Claude-3.5-Sonnet 81.25, Gemini-1.5-pro 64.58. By rule block: shape 80.0%, color 44.2%, number 26.0%, shape 76.4%, color 47.0%, number 45.4%. Rule order was fixed. Overall: Claude-3.5-Sonnet 68.78, o1-preview 66.57 (direct); extended reasoning not uniformly better.
- Contested (K20, K21). Format, trial count and prompt differ. No study links WCST to trap tasks (K34).

**Mental set on math (b22, c17).** Llama-3.1-8B/70B and GPT-4o, 6 items per cell. GPT-4o few-shot exact match: shortcut 0.33, shortcut after complex 0.66, complex 0.66, complex after shortcut 0.83. With chain of thought 0.66 / 0.66 / 0.83 / 0.83, solved in 3 steps. No statistics. Too thin to use (K22).

**Strategy choice.**
- Models lean on one favoured strategy (c19, d22, second-hand). Telling the model which strategy to use changed nothing (d10). Majority vote over strategies: Phi-4 54.9, R1-Distill 68.4. Verifier: R1-Distill 74.1, Phi-4 46.9. Oracle selection 82.9 and 90.1.
- Meta-Reasoner and HybridMind: see M8. HybridMind's fine-tuned Llama-3.1-8B selector beat GPT-4o natural-language reasoning by 4.4 points on FOLIO and 1.3 on MATH; a prompted GPT-3.5 selector gained 10 on hard FOLIO.
- Underthinking (d06, d07): wrong answers have 418% more thought switches and 225% more tokens. A decoding penalty on switch tokens lifts QwQ AIME24 38.3 to 44.1 and R1-Distill-Qwen-32B 61.4 to 64.1. The failure there is too many switches, the opposite of Einstellung. Any scaffold that forces switching must be watched for this.
- Longer chain of thought lowered accuracy under high meta-uncertainty by a median 17.3 points (CrI 7.7-25.5), 7 models, 79 frames, 7,875 responses (c22). Single-author preprint (K23).

**Non-LLM.** An Einstellung Rigidity Index exists for continual-learning networks (c24). Analogy only.

**Confirmed absent.** No LLM test of: an informed "better method may exist" prompt; an equal-token scaffold versus plain on trap items; storing rationale with procedures; WCST as a proxy for trap failure; a validated process measure of fixation (K34, critique GAPS).

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Fixation is a first-answer effect, so the second route must be generated independently of the first.** Part S3 (fresh context per attempt) and S6. [E] K01, K06. Evidence a02, a15, d11, d14-d17. This is already in the schema (S3 fresh context). Keep it. Note: it supports S3, it does not add a new element.
2. **A one-line warning is not enough and is not free.** Do not rely on "a better method may exist" alone. Warning cut human fixation only from 83% to 57%; telling about the shortcut left 29% fixated; forget-instructions slowed items that needed the old routine. Part G (extends 4b: slow-down and bias prompts). [E] K07, K29. Evidence d12, a17, d15. Implication: the switch must be triggered by a signal (G1) and forced by structure, not by an exhortation.
3. **Mixed exemplars beat warnings.** When showing the agent worked examples or lessons for S9/memory, vary the best method across exemplars; do not show five of the same. Alternating training cut human fixation to 16%. Part memory (lessons shown after the first attempt; vary them). Status: the human effect is one reanalysis [S] K28; the principle that varied practice builds rationale is [E] K10 (a19, a20, a21). Treat the memory rule as "add now, measured in the test below".
4. **Store why with each stored procedure.** Part memory (subgoal library, lessons). [E] K10 (Hatano and Inagaki; Schwartz et al.), but no LLM test exists (K34). Cheap to build; add now as a field, and keep it only if the test in section 8 (T6) passes.
5. **Frugal rules are not worse.** Operator stop rules may be simple (first discriminating cue). Take The Best .658 vs regression .657. Part O (stop rule per operator). [E] K12. Evidence a23, a24, b26. Fix a stop rule for each operator; cost is near zero.
6. **Ranking, not pass/fail, in S4/S7.** A check that only says "ok" ends the search on a good-but-suboptimal answer (M2). Where the item has a cost measure (length, steps, score), S7 compares candidates on it. Part S7. Supported by K05 [S] and consistent with the schema (S7 selects by behaviour and shortest). Mark [S]; do not claim more.
7. **Guard against over-switching.** A scaffold that forces alternatives on every item will cost accuracy on items where the familiar route is right (forget-instruction data d15; underthinking d06, d07; schema [O] forced doubt 92% to 75%). Part G1 (reconfirmed). [E] K29 plus own data.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| T-A. Informed prompt ("a shorter or different method may exist") on trap and non-trap items | G1 / S6 | [S] human only | a17, d12, K07, K29 |
| T-B. Second-route-then-compare scaffold versus plain and best-of-N at equal tokens | S6, S7 | [S] ECR-Agent not equal-token | c16, d04, K19 |
| T-C. Mixed-exemplar versus same-method exemplars in lessons | memory | [S] human only | d12, K28 |
| T-D. Rationale stored with procedure versus procedure only | memory | [S] no LLM test | a19-a22, K10, K11 |
| T-E. Bandit or rule-based operator selector versus fixed order O1-O8 | S6 | [S] not on trap items | d08, d09, K24 |
| T-F. First-route token share as a fixation detector (impasse signal) | G1 / S6 / logging | [S] unvalidated | d06, d07, K31 |
| T-G. Clean-context retry versus continued-context retry after a failed attempt | S5, S6 | [S] human only | a11, K04 |
| T-H. Code execution in the second-route step | S4, S6 | [S] abstract only | d14, K30 |
| T-I. Time or token cap as a fixation risk (tight cap vs loose) | G11, G12 | [S] human only | d12, d13, K09 |
| T-J. WCST as a cheap proxy for trap failure | logging | [C] | c04, c06, K20, K21 |
| T-K. Skill gradient on code and medical trap items (chess vs programming direction) | S0 gate | [S] | a04, d18, K02, K32 |

None of these enters the schema until its test passes (see UNKNOWNS.md).

## 8. Concrete tests on our bench

All arms get the same total tokens (setup cost counted, G7). Report accuracy on trap items, accuracy on control items (familiar route correct), and trap-minus-control gap.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T-A informed prompt | Paired items: trap version (hidden shorter or different route) and control version (familiar route is right). Use mARC-style, MedEinst subset, water-jar-style tasks, ARC items with a known simpler rule | plain; plain + one-line "a shorter or different method may exist"; plain + signal-triggered switch | trap accuracy; control accuracy; net change | Small gain on trap items (humans 9% to 65%; LLM effect unknown), loss on control items. Keep only if net gain > 0 |
| T-B second route | Same pairs | plain CoT; best-of-N (N matched to tokens); S3 isolated attempts + S7 compare; ECR-style structure | trap rate, robust accuracy, tokens | Beats best-of-N by a few points; debate-style does not (d04) |
| T-C mixed exemplars | Luchins-style series: 5 long-method exemplars then a short-route item | 5 same-method exemplars; 5 alternating; 5 same + warning; tight token cap | share using the long method | 80% to 16% in humans; LLM effect likely smaller. The tight cap should raise fixation |
| T-D store why | Transfer items with a changed constraint | procedure only; procedure + rationale; worked solutions only | accuracy on changed-constraint items; wrong reuse rate | Rationale arm gains on changed items, no loss on unchanged |
| T-E selector | Mixed class set, trap and routine | fixed order O1-O8; random order; bandit keyed by class; LLM self-pick | solved subgoals per token | Bandit beats fixed by 3-7 points (Meta-Reasoner 89 vs 82 self-pick); oracle gap 10+ |
| T-F fixation detector | 100+ trap items | log tokens on first route, route count | AUC of detector for trap failure | AUC > 0.65 to count as a usable signal |
| T-G clean retry | Items where attempt 1 failed | retry in fresh context; retry continuing the context | solve rate, tokens to solution | Fresh context faster (humans about 2x) |
| T-H execution | Items with computable shortcut | text-only second route; second route with code run | trap rate | Lower trap rate with execution |
| T-I cap | trap items | cap at 0.5x, 1x, 2x tokens | trap accuracy | Tighter cap raises fixation (humans 0.97 vs 0.83) |
| T-J WCST proxy | WCST plus trap set | correlation across model/prompt variants | rank correlation | rho > 0.5 for use as a proxy |
| T-K skill gradient | Code and medical traps; weak vs strong model | model size sweep | trap-rate slope | tells which direction S0 should assume |

Minimum size: 50 items per condition (Haq's 6 per cell was unusable, K22). Pre-register the thresholds.

## 9. What does not transfer, and why

- **Eye movements.** Gaze is the main human measure. An LLM has no gaze. The closest analogues are attention weights and token share, and neither is validated (K31). Reasoning text is not evidence of what drove the answer (G10), so do not read fixation from what the model says it considered. This is the same pattern as in humans: experts reported searching while gaze stayed put (K03).
- **Skill gradient from chess.** GM 100% to CM 0% is one lab, one position pair, and does not hold in programming (d18) or at equal rates in Sheridan and Reingold (b02). Do not assume a bigger model is less fixated. The MedEinst table suggests no simple link (d03, K18 contested).
- **Years of experience.** Human flexibility is built over years of varied practice. A model has fixed weights. The memory store is the only place where "experience" can change during a run, and it changes by retrieval, not by new skill.
- **"Not trying".** Human motivation (valuing the shortcut, r = .45) has no direct counterpart. In an LLM the match is how much budget the scaffold gives to alternatives.
- **Warnings and instructions.** People respond to "don't be blind". Models mostly do not change under strategy instructions (d10) or persistence prompts (d07). Prompts are weak levers; structure and code checks are strong ones.
- **Water-jar and Luchins numbers.** From 1940s paper tests with college students. They give direction, not effect sizes for models.
- **Athlete reflection.** No evidence to transfer.
- **Toolbox accuracy results.** Take The Best vs regression was on one environment of 83 German cities with binary cues. It supports simple stop rules, not that heuristics beat reasoning on language tasks.
- **Debate.** Multi-agent debate made MedEinst robust accuracy worse (d04). This matches G9; the toolbox idea does not justify adding agents.

## 10. Open questions

1. Does an equal-token second-route scaffold reduce LLM Einstellung on MedEinst, M-ARC and Only Connect Walls? (No study; ECR-Agent confounds tokens and structure.)
2. Does the informed prompt help LLMs, and what does it cost on non-trap items?
3. What process measure of fixation works for an LLM, and can it be used as the S6 trigger? Is a first-route token share predictive?
4. Is there an independent replication of the Bilalic skill gradient and the carry-over cost (d = .65)? Are there failed replications in medicine or music?
5. Do stronger LLMs get more or less trapped? The MedEinst text says more; its own table says less (r = -0.69 over 8 rows). Which feature of the benchmark, counterfactual flips or unusual items, drives the difference from M-ARC where reasoning models improved?
6. Does adaptive-expertise training (explain why a procedure works; invention before instruction) transfer to LLM agents?
7. Does a learned operator selector beat a fixed O1-O8 order on trap items, and what does the monitor cost in tokens?
8. What stop rule tells the agent when to stop searching for alternatives (Binz and Schulz gave a model, not a rule)?
9. Is WCST perseveration (more perseverative than random errors in LLMs) a valid proxy for trap failure?
10. Why does knowledge help or hurt depending on accessibility (b13)? The 2026 study is N = 30 and one lab.
11. Does athlete reflection research offer anything usable? No source found.
12. Verify unconfirmed items before quoting: Bilalic 2008 "3 SD" and the 3.67 odds factor (second-hand in the critique); Qwen3-32B and other MedEinst cells; Haq 2025 and Li 2025 WCST numbers; Hatano and Inagaki 1986; Binz and Schulz journal version.

## 11. Sources

[V] = opened and read in the research session. [M] = snippet, abstract or second-hand only.

- [V] Bilalic, McLeod, Gobet (2008) Inflexibility of experts. Cognitive Psychology 56:73-102. https://bura.brunel.ac.uk/bitstream/2438/641/1/Flexibility_Cog%20Psy_revisionFINAL.pdf (a02-a07)
- [V] Bilalic, McLeod, Gobet (2008) Why good thoughts block better ones. Cognition 108:652-661. https://bura.brunel.ac.uk/bitstream/2438/2276/1/Einstellung-Cognition.pdf ; https://pubmed.ncbi.nlm.nih.gov/18565505/ (a10, a11, b07-b10; b10's 3 SD figure is second-hand)
- [M] Bilalic, McLeod, Gobet (2009) Specialization effect in expert chess players. https://pubmed.ncbi.nlm.nih.gov/21585497/ (d19, abstract)
- [V] Sheridan and Reingold (2013) PLoS ONE 8:e75796. https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0075796&type=printable ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3790829/ (a12-a14, b01-b06)
- [V] Ellis and Reingold (2014) Front Psychol 5:679. https://pmc.ncbi.nlm.nih.gov/articles/PMC4079068/ (a15, b11, b12)
- [V] Pope-Caldwell and Washburn (2022) Sci Rep 12:2179. https://pmc.ncbi.nlm.nih.gov/articles/PMC8828898/ (a16, a17)
- [V] Ninomiya, Terai, Miwa (2022) Front Psychol 13:934029. https://pmc.ncbi.nlm.nih.gov/articles/PMC9447375/ (a18)
- [V] Binz and Schulz (2022/2023) Reconstructing the Einstellung effect (thesis data reanalysis). https://osf.io/download/yhcf4/ (d11-d13). Web summary [M]: https://www.ethicalpsychology.com/2021/09/reconstructing-einstellung-effect.html (b30)
- [M] Luchins (1942) Mechanization in problem solving. https://doi.org/10.1037/h0093502 (a01, b29; numbers via Bilalic and Binz)
- [M] Saariluoma (1990) Apperception and restructuring in chess players' problem solving. https://doi.org/10.1017/CBO9780511571350 (a08, via Bilalic)
- [M] Wiley (1998) Expertise as mental set. https://doi.org/10.3758/BF03201137 (a09, via Bilalic)
- [M] Blech, Gaschler, Bilalic (2020) think-aloud and Einstellung. https://researchportal.northumbria.ac.uk/en/publications/why-do-people-fail-to-see-simple-solutions-using-think-aloud-prot/ (b31, snippet)
- [M] Vallee-Tourangeau, Euden, Hearn (2011). https://pubmed.ncbi.nlm.nih.gov/21851153/ (d14, abstract)
- [M] Tempel and Frings (2019). https://pubmed.ncbi.nlm.nih.gov/31733435/ (d15, abstract)
- [M] Pope et al. (2015) baboons. https://pubmed.ncbi.nlm.nih.gov/26194414/ (d16, abstract)
- [M] Thomas and Didierjean (2016) magicians. https://pubmed.ncbi.nlm.nih.gov/27318598/ (d17, abstract)
- [V] Sergeyuk et al. (2023) mental set in programming. https://arxiv.org/pdf/2307.06673 (d18)
- [V] Europe PMC citation list for PMID 18565505. https://www.ebi.ac.uk/europepmc/webservices/rest/MED/18565505/citations (d20, titles only)
- [V] Semantic accessibility and heuristic fixation (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13117359/ (b13, b14)
- [V] Hatano and Inagaki (1984) Two courses of expertise. https://hdl.handle.net/2115/25206 (a19, a20). 1986 chapter [M] (b32)
- [V] Schwartz, Bransford, Sears (2005) Efficiency and innovation in transfer. https://aaalab.stanford.edu/assets/papers/2005/Efficiency_and_Innovation_in_Transfer.pdf (a21, a22)
- [V] Gigerenzer and Goldstein (1996) Reasoning the fast and frugal way. https://www.dangoldstein.com/papers/FastFrugalPsychReview.pdf (a23, a24)
- [V] Fenwick, Campitelli, Thompson (2026) adaptive toolbox and expertise. https://pmc.ncbi.nlm.nih.gov/articles/PMC13481750/ (a25, b24-b26; Sedlmeier and Gigerenzer 2001 second-hand)
- [V] Macnamara, Hambrick, Oswald (2014) meta-analysis. https://doi.org/10.1177/0956797614535810 (b16)
- [V] Burgoyne et al. (2019) chess reanalysis. https://englelab.gatech.edu/articles/2019/Burgoyne_et_al_2019_AJP.pdf (b17)
- [V] Campitelli et al. (2015) editorial. https://pmc.ncbi.nlm.nih.gov/articles/PMC4354238/ (b15)
- [V] Siebert et al. (2025) fast-and-frugal trees in athletes. https://pmc.ncbi.nlm.nih.gov/articles/PMC12360579/ (b27)
- [V] Chess players, planning and reflection (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC11942737/ (b28)
- [V] Kim et al. (2025) M-ARC / mARC-QA. https://arxiv.org/abs/2502.04381 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12606185/ (a26, b18, b19, c11, c12, d01)
- [V] Shidara et al. (2026) reasoning and clinical flexibility. https://arxiv.org/abs/2601.11866 (b20, b21, d05)
- [V] Chen et al. (2026) MedEinst. https://arxiv.org/abs/2601.06636 (c13-c16, d02-d04; table text garbled)
- [V] Alavi Naeini et al. (2023) Only Connect Wall. https://arxiv.org/abs/2306.11167 (b23, c01-c03)
- [V] Hao, Alexandre, Yu (2025) WCST in visual LLMs. https://arxiv.org/abs/2505.22112 (c04, c05)
- [V] Li et al. (2025) near-optimal decision-makers. https://arxiv.org/abs/2506.16163 (c06-c08, d21; not found again by the critique)
- [V] Li et al. (2024) Reflection-Bench. https://arxiv.org/abs/2410.16270 (c09, c10). Kennedy and Nowak (2024) [M] (c25)
- [V] Haq et al. (2025) Is your LLM trapped in a mental set? https://arxiv.org/abs/2501.11833 (b22, c17; not found again by the critique)
- [V] Zhang et al. (2025) Reasoning strategies in LLMs. https://arxiv.org/abs/2507.11423 (c18, d10, d22). Mondorf and Plank (2024) [M] (c19)
- [V] Sui et al. (2026 v6) Meta-Reasoner. https://arxiv.org/abs/2502.19918 (c20, c21, d08)
- [V] Han et al. (2025) HybridMind. https://arxiv.org/pdf/2409.19381 (d09; c27 was snippet-only before)
- [V] Wang et al. (2025) Underthinking of o1-like LLMs. https://arxiv.org/pdf/2501.18585 (d06, d07)
- [V] Bogdan (2026) Free energy heuristics. https://arxiv.org/abs/2606.15877 (c22, c23)
- [V] Gu and Shi (2025) Einstellung Rigidity Index. https://arxiv.org/abs/2510.00475 (c24)
- [M] Trapped by Expectations: functional fixedness in LLM-enabled chat search (2025). https://arxiv.org/abs/2504.02074 (c26, listing only)
- [V] arXiv title searches for Einstellung and functional fixedness (c28). https://arxiv.org/search/?query=Einstellung&searchtype=title
