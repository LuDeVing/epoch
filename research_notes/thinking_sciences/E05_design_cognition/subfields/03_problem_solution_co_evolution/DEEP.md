# Problem-solution co-evolution: deep document

*Subfield E05.03. Built from evidence_a-d.jsonl (a01-a28, b01-b28, c01-c28, d01-d20), claims.jsonl (K01-K35) and critique.md in this folder. Evidence ids are in brackets. Status tags: [E] established (two or more independent sources), [S] single-source, [C] contested. Where the cross-check found an error in an evidence line, the corrected number is used here.*

## 1. What it is

Co-evolution is the idea that, in design, the problem and the solution are not built one after the other. They grow together. A partial solution changes what the designer thinks the problem is. A changed problem frame changes what solutions look sensible. Creative moments are said to come when the two fit each other: a "bridge" [a01, a07, K01].

In plain terms for our agent: a solution attempt is also a probe of the problem. A failed attempt can show a missing constraint, a wrong goal, or a wrong representation. The idea says the agent should be allowed to go back from solving (S3) to framing (S2) and change the frame. It does not say the agent should always do so.

Key claims in the literature:

- Problem and solution spaces are explored in parallel, with bridges between them (Maher; Dorst and Cross 2001).
- Reframing is mostly triggered by solution-side events (a failed attempt, a tool limit, a chart that does not show the pattern), not by a planned problem step [b02, b05, K04].
- It is common but not universal [K03].
- Critique: designers "muddle through". Mapping the problem space first may serve creativity better than interleaving [a08, a27, K07, K08].

What is solid: many small qualitative studies see the pattern. What is thin: the founding result is nine designers, one task, no inferential test. There is almost no controlled test of the loop for language models. The best evidence for our agent is indirect: frame-first prompts on checkable tasks, failed-check triggers, and loop bounds.

Links to other subfields of this run (not covered here): Problem finding; Plans and schemas; Functional decomposition; Epistemic action; Anomaly response; Question wording and presupposition; Reflective reasoning and second look; Generation versus evaluation.

## 2. History and theories in depth

**Schon and the reflective conversation (1983).** Designers talk with the situation. They act, see what "talks back", and reframe. This is the root of the idea that framing continues during action. Kokotovich (2015) builds on "reflection-in-action" to argue for a different account of co-evolution [a08, d11].

**Maher and Poon (1996), Maher, Poon and Boulanger (2000), Maher and Tang (2003).** The first computational model. A space of requirements and a space of solutions both change. A genetic algorithm evolves both, and the fitness of one depends on the other. Later work compared the model with human protocols. The abstracts give no human-fit numbers [a03, a04, a05, a06, b24, K26].

**Dorst and Cross (2001).** Protocol study of nine experienced industrial designers on one modest realistic task. Concepts were rated by a panel of experienced educators. The authors link creativity to how the problem is formulated, say creative concepts show a bridge where problem and solution frames match, and say the data confirm the general validity of the model. They add "default" and "surprise" spaces as refinements. Cited about 1,570 times. No inferential statistics are known. The full text was not reachable: only the abstract was read [a01, d14, K01, K33].

**Cross (1997, reprinted 2024).** The "creative leap": a bridging idea that links problem space and solution space [a07, a02].

**Suwa, Gero and Purcell (2000).** "Unexpected discoveries" and S-invention of requirements: designers invent new requirements while sketching. Snippet only [a20, b28].

**Kruger and Cross (2006).** The same nine designers, classified after the fact into four strategies. The abstract says solution-driven designers scored higher on creativity and lower on quality, and problem-driven designers gave the best balance. With nine people over four strategies, cells hold one to four people. Not opened beyond the abstract [a19, d13, K32].

**Wiltschnig, Christensen and Ball (2013).** Collaborative co-evolution in design teams. A secondary quote says 84% of the team's solution attempts fell inside co-evolution episodes. Read only through Storm et al. [a11, b25].

**Kokotovich (2008, 2015).** Non-hierarchical mind mapping to analyse a problem. Within groups, more problem-structuring went with better creative outcomes, but the result is correlational and the paper is closed. The 2015 paper uses it to argue that holding back solutions helps, and that co-evolution is a looser claim than often stated [a09, a08, d11, d12, b26].

**Kopecka, Santema and Buijs (2012).** "Designerly ways of muddling through": designers do not follow a clean sequence [a27].

**Halstrom and Galle (2015).** Add a third element, audience, and say co-evolution is not always present, even in non-trivial cases [a15, b06, K03].

**Atman et al. (2007), Christiaans (1992), Akin and Akin (1996).** Time spent scoping the problem is linked to better design in several human studies. Second-hand only here [a12, b27].

**Storm, van Maanen and Goncalves (2019).** Interviews with 2 experts (about 200 codes, about 15 categories, 7 themes) and 9 interviewed students out of 21 at a workshop. Five of nine said they felt more confident. All said they spent more time reframing. Self-report, no control group [a10].

**Martinec, Skec, Horvat and Storga (2020).** The most numeric human test. See section 3 [a14, b03-b05].

**Cash, Goncalves and Dorst (2023).** A cognitive model of method use; a reanalysis of 31 novices' think-aloud data links uncertainty to transition type [a13, d03, d20].

**Chen et al. (2023).** 54 students split into problem-driven and solution-driven by the FBS (function-behaviour-structure) P-S index. The groups show different cognitive processes [a18, d15].

**Feast (2024); Hu et al. (2026); Parsons and Shukla (2025).** Qualitative expert work: a third element (situation), C-K theory mapping of frames, and 11 data-visualisation experts who kept reframing. The last says framing is "a continuous activity" [a16, a25, b01, c01, K27].

**Biskjaer, Halskov and de Rooij (2026).** Review of 16 DRS conference papers over 25 years. It calls co-evolution a "flexible boundary concept", which means it is loosely defined [a17].

**Goel (2014, 2018).** Neuroscience view of design creativity. Background only [b21, b22].

What the history shows: the model came from small protocol studies, then spread by citation. Later work widens it (audience, situation), and some authors narrow it (not always present, order may differ).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Creative design coincides with problem-solution bridges | N=9 experienced designers, one task, panel ratings, no inferential test | Dorst and Cross 2001 [a01, d14] | [S] |
| Co-evolution seen in teams, experts, students, ethnography, but small and descriptive | 4 teams; 11 experts; 12 experts; one eight-year ethnography; 16-paper review | [a16, b01, a25, b07, a17] | [E] |
| Co-evolution is not universal | case examples; Halstrom and Galle | [a15, b06] | [E] |
| Textbook mapping (analysis = problem, synthesis = solution) fails | 12 students, 4 teams, 24 fragments; analysis vs problem transitions rS=-0.649; evaluation vs solution rS=0.672 | Martinec 2020 [b04] | [S] |
| Team time split | Ideation transitions 49% synthesis, 32% analysis, 19% evaluation; 37% problem space, 63% solution space. Review: 44% analysis, 31% synthesis, 25% evaluation; 12% problem, 88% solution. Kappa 0.71 on 20% of data | Martinec 2020 [b03] | [S] |
| New problem entities follow solution-space work | Wilcoxon p<0.05 overall only; pattern reverses within ideation alone; new solution entities after solution work p<0.001 | Martinec 2020 [b05] | [S] |
| Reframing is triggered by solution-side events | Qualitative (N=11); symptom-triggered repair beats generic reflection in agents, 20.15% vs 4.29% | [b02, d02] | [E] |
| Hedging language tracks transition type, but weakly | 31 novices, 1617 segments, chi2(6)=180.1; pseudo R2 about 1%; change in hedging p=.117 | Cash 2023 [d03, d20] | [S] |
| Solution-driven = more creative, less correct; problem-driven = balanced | N=9, abstract only | Kruger and Cross 2006 [d13] | [C] |
| Problem-structuring time linked to creative outcome | Correlational, no numbers read | Kokotovich 2008 [d11, d12] | [C] |
| LLM problem reframing gave no gain on open design frames | 280 frames (not people) rated by 15 experts, 4 arms, GPT-4o; times 23.25 / 21.82 / 28.35 / 20.78 min; structured Dorst chain +22% time; CSI 61.01-64.85 | Shin 2025 [c02-c04] | [S] |
| Skilled users gain more from LLM reframing | 12.54% more novel frames, z=2.70, p=0.01; free-form gap 20.84% not significant | Shin 2025 [d06] | [S] |
| 4-call Dorst-style chain rated more interesting | 29/189 vs 17/189 interesting; N=7 | Sood 2026 [c07, c10] | [S] |
| Rephrase-and-Respond raises accuracy on ambiguous tasks | GPT-4 average over 10 tasks 64.95 to 89.77; last-letter 21.36 to 86.82 | Deng 2024 [b18] | [S] |
| Self-rephrase depends on model strength | Vicuna-13b own rephrase lower than GPT-4's rephrase on 6 of 6 tasks (Sports 65.00 vs 73.64) | [b19, d05] | [S] |
| Step-back (abstraction first) | PaLM-2L MMLU physics 66.4 to 73.2, chemistry 70.9 to 81.8, TimeQA 41.5 to 66; fixes up to 40% of errors, adds up to 12% new | Zheng 2024 [b20] | [E] |
| Self-Discover (compose a structure first) | PaLM-2 BBH 56 to 67 (CoT 60), T4D 30 to 69; GPT-4 BBH 58 to 81 (CoT 75), T4D 51 to 85; beats CoT on 21 of 25 tasks | Zhou 2024 [c22] | [E] |
| Models fail to ask for the one missing fact | QuestBench: above 80% on GSM-Q and GSME-Q; 40-50% on Logic-Q and Planning-Q | Li 2025 [c18] | [S] |
| Clarifying questions before coding | GPT-4 Pass@1 70.96 to 80.80 (human answers, 10 participants, 140 problems; 2.85 questions per problem); about +10-13 points with simulated users on four benchmarks | ClarifyGPT [c20, c21] | [E] |
| Clarification is fragile | Lean specs, 189 tasks: -2.6 pp (same model, k=3), -4.2 pp (k=10), +6.3 pp (cross-model); k=10 no better than k=3 | Allaham 2026 [d08] | [S] |
| Monitor agent beats retry loop (one design task) | Battery capacity means 72.07 plain / 106.08 self-monitor / 141.17 co-regulation Ah, SD 20.52 / 45.60 / 48.45; 30 runs each; F(2,86)=21.606, partial eta2 0.334; d=0.956 and 1.846; steps equal 9.07 / 9.10 / 9.37 (p=.97); monitor tokens unmeasured | Xu 2026 [b15, d04] | [S] |
| LLMs jump to solutions | Accept a user tool choice; hackathon team fixated; Five Whys flow caught 6 of 6 seeded mismatches at about 0.01 USD per session | [a24, b17, c23] | [E] |
| Human-AI design: framing and breadth up, innovation down | N=32; framing 2.94 vs 4.64 (t(31)=14.03, dz=2.48); innovation 4.66 vs 3.40 (dz=2.69); output formats differed so raters could tell conditions | Chen 2026 [b10] | [C] |
| GAI helped idea generation and problem definition | N=20 (15 in AI groups); helped idea generation 86.7%, problem definition 73.3%; novelty p<0.01; overall p=0.005; feasibility p=0.084 | Guo 2025 [b08] | [S] |
| LLM output stays in one semantic region | 14,350 prompts, 5 models; pairwise novelty distances 0.206-0.341; brief type moves novelty | IDEAFix [b12, b14] | [S] |
| LLM personas copy static shares but not switches | GPT-4o, 10 runs per cell; problem-driven persona: PS switches 6.7 vs 10.5, SP 6.4 vs 9.8 (p<=.003 unconstrained); both beat a bare prompt on novelty and integrity (p<.05) | Zhang 2025 [d01] | [S] |
| Self-judged correction degrades | GPT-3.5 CommonSenseQA 75.8 to 38.1 after one round; GPT-4 GSM8K 95.5 to 89.0 after two; oracle trigger GPT-4 GSM8K 97.5 | Huang 2024 [d09] | [E] |
| Debate loses to voting at equal responses | 3 responses: debate below self-consistency 82.5; 6 responses 83.2 vs 85.3 | [d16] | [E] |
| Failed-check triggers beat blind reruns | 536 failed web-agent runs: symptom-triggered 20.15% (108/536); rerun 6.90%; self-reflection 4.29%; critic 3.73%; random node 3.73% | Luan 2026 [d02] | [S] |
| Reruns break passing runs | 54 passes rerun 3 times: 162 reruns, 85 failed; 39 of 54 cases failed at least once | [d17] | [S] |
| Self-Refine gains come early | Code optimisation 22.0 to 28.8 after 3 rounds; max 4 rounds; non-monotonic | Madaan 2023 [d10] | [S] |
| Self-evolving loops drift | R-Zero math 49.18 to 54.69 (+5.51) but pseudo-label accuracy 79.0% to 63.0% in 3 iterations (47.0% later); 0.6B model declined at 70.6% | Huang 2026 [c15-c17] | [E] |
| Research-software loop needs audit and contraction | Tool a3 F1 0.768 vs 0.364 for next baseline; 46 repos; about 400 commits; descriptive, own benchmark | Microsoft 2026 [c12-c14] | [S] |

## 4. Mechanisms and models

### 4.1 Maher's co-evolutionary model (implementable)

State: two populations. R is a set of requirement or criteria sets. S is a set of candidate solutions. A solution's fitness is how well it meets the current requirement set. A requirement set's fitness is how consistent it is with the solutions found and with the higher-level aim. Each generation: evaluate S against R; mutate and recombine R and S; keep the best of both. The key point is that R is not fixed.

Agent version (cheap): keep the criteria list as an explicit object. After each failed solution check, allow one edit to the criteria list (add, drop or rewrite a criterion), with the failing output quoted. Re-run the check against the old and new criteria. Keep the version that the external check supports. This is the S3-to-S2 return, constrained by G2 (revise only from real output).

### 4.2 Bridge detection

Dorst and Cross define a bridge as a moment when a problem frame and a partial solution are recognised as matching. For code: a bridge is a step where one candidate both satisfies the rewritten criteria and passes the check that earlier candidates failed. A bridge log is "criteria version, candidate, check result". No study tested this as a trigger or selector.

### 4.3 Martinec transition coding

Code each step by content, not by operator name: does it add or discuss a problem entity (need, constraint, goal) or a solution entity (part, action, structure)? Count transitions P to S and S to P. Human teams in ideation: 37% problem space, 63% solution space. This is a trace diagnostic, not a driver. Analysis steps are not reliably problem steps (rS=-0.649), so tag by content [b03, b04].

### 4.4 Triggers for the return S3 to S2

Evidence ranks triggers:

1. An external failed check with a concrete symptom (20.15% repair vs 4.29% for generic self-reflection [d02]).
2. Oracle-quality signals in self-correction studies (GPT-4 GSM8K 97.5 with oracle vs 89.0 without [d09]).
3. A stall seen by a second monitor (Xu [b15]).
4. Hedging language, which is weak (pseudo R2 about 1% [d03]).

Do not use self-judged doubt.

### 4.5 Frame-first LLM steps

Three variants have numbers. Rephrase-and-Respond: the model rewrites the question, then answers (one or two calls). Step-back: ask for the governing principle first. Clarify-then-solve: ask up to about 3 questions, get answers, then solve. All three fix a frame before solving and never revise it. They are cheap and help on checkable tasks, but their extra calls need an equal-token control against best-of-N, which the papers did not run.

### 4.6 Bounded loop

Cap reframes at 2 to 3 rounds, keep best-so-far, and require a verified failure for each. Reasons: self-judged loops lose with each round [d09]; Self-Refine gains arrive in rounds 1 to 3 [d10]; R-Zero labels decay [c16]; reruns can break passing runs [d17].

## 5. What holds up

**Replications.** No numeric replication of Dorst and Cross 2001 on its original data was found. Support is conceptual and from other designs: Parsons and Shukla (N=11 experts), Martinec (12 students), Cash 2023 (31 novices), Storm 2019 (self-report) [K33].

**Failed or narrowed results.**
- Martinec: analysis does not map to problem space (rS=-0.649) [b04].
- Halstrom and Galle: co-evolution is not always present [b06].
- Shin et al.: no gain from LLM reframing on open design frames, even with the Dorst chain [c02-c04].
- Xu et al.: the paper's discussion swaps labels against its own Table 1; the table is right (critique). "Equal steps" holds (9.07 / 9.10 / 9.37), but monitor tokens were not counted.
- Frontiers 2026 [b11]: reported F=43.28 is inconsistent with the table; recomputed F is about 4.27 (means 20.90, 18.65, 16.13; n=40 each). Only the ordering of means is usable. Low reliability.

**Moderators.**
- Checkability: frame-first helps on checkable tasks (RaR, step-back, Self-Discover, ClarifyGPT) and was null on open frames (Shin, IDEAFix) [K16, contested]. The cause is not separated from judge strictness and model tier.
- Model strength: weak models lose from self-rephrase; a stronger model's rephrase helps a weak one on 6 of 6 tasks [d05].
- User skill: skilled users got 12.54% more novel frames [d06].
- Task: Zhang found a process-style prompt raised novelty over a bare prompt on one open task, so open framing is not always null [d01].

**Interventions that worked.** Step-back (physics +6.8, chemistry +10.9); RaR on ambiguous tasks; ClarifyGPT (+9.84 points with human answers); symptom-triggered repair (20.15%); Five Whys requirement check (6 of 6 seeded mismatches); monitor agent on one design task (141.17 vs 72.07 Ah).

**Interventions that did not work, or hurt.** Self-judged correction without an external signal; debate versus voting; long structured reframing chains for open frames (22% more time, no quality gain); unbounded self-evolution loops; clarification at k=10 (no better than k=3); generic reflection and critic agents in repair [d02].

**Problem-first vs muddling through.** Open. Kokotovich is correlational; Kruger and Cross is N=9; Cross 2024 says the solution space may be structured first from precedents. No study runs problem-first, solution-first and interleaved under equal conditions [K08, K32].

## 6. Language models

**Baseline behaviour.** Models solve fully specified tasks but do not check requirements. They accept a user's stated tool choice and fixate after small snags [a24, b17]. On QuestBench the best models are above 80% on arithmetic-style missing-information items and only 40 to 50% on logic and planning items [c18]. Detecting under-specification is easier than using the answer [d08, d19].

**Does the loop exist in LLM traces?** Zhang et al. (GPT-4o, 10 runs per cell, one task): static issue shares match humans; cross-space switches are fewer than in humans, and a problem-driven persona switches less than a solution-driven one (PS 6.7 vs 10.5, SP 6.4 vs 9.8). Both personas beat a bare prompt on novelty and integrity (p<.05). Whether switch count predicts quality was not tested [d01, K23, K25].

**What changed behaviour, with numbers.**
- Rephrase-and-Respond: GPT-4 10-task average 64.95 to 89.77. Weak models gain less and sometimes lose [b18, b19].
- Step-back: PaLM-2L physics +6.8, chemistry +10.9; up to 40% of errors fixed, up to 12% new errors added [b20].
- Self-Discover: beats CoT on 21 of 25 tasks. 74.7% of MATH failures were computation errors that no frame fixes [c22].
- ClarifyGPT: 70.96 to 80.80 with human answers, 2.85 questions per problem [c20].
- Clarification in Lean spec writing: -4.2 to +6.3 pp [d08].
- Shin 2025 (open design frames, GPT-4o): no gain in novelty or usefulness in any arm; the Dorst chain cost 22% more time [c02-c04].
- Monitor agent (Gemini 3.1 Pro, battery pack design, 30 runs per arm): 141.17 Ah vs 72.07 plain. One task, one model, tokens not equal [b15, d04].
- Failed-trace repair: symptom-triggered 20.15% vs 6.90% rerun [d02].
- Self-correction without signal: GPT-3.5 CSQA 75.8 to 38.1 after one round [d09].

**Human-AI findings (indirect).** Chen 2026: AI groups scored higher on framing and breadth but lower on innovation (4.66 vs 3.40). Guo 2025 (N=20): novelty p<0.01, feasibility not different. IDEAFix: models stay in a narrow semantic region under defixation prompts (distances 0.206-0.341) [b08, b10, b12].

**Gaps.** No LLM study tests "revise the frame after a failed solution" against "frame once then solve" at equal tokens. No LLM study compares problem-first, solution-first and interleaved with numbers [K25]. Almost no study measures tokens.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Revise the frame (criteria, goal wording) only from a failing output located by code, never from model opinion | G2, G1; S5 | [E] | K04, K29; d02, d09, b02 |
| Cap any frame-revision loop at 2 to 3 rounds; keep best-so-far; stop when a check passes | G6, S5, S6 | [E] | K24, K29; d09, d10, c16 |
| Check stated premises (tool choice, guess, constraint) against the task; move unsupported ones to the marked block | S1 input hygiene, G10 | [E] | K17; a24, b17, c23 |
| Tag trace steps by content (problem entity vs solution entity), not by operator name | Run log (section 6 of SCHEMA) | [S] data, cheap and safe | K05; b04 |
| No self-judged "should I reframe?" step | G1, G10, 4b | [E] | K29; d09 |
| No multi-agent reframing debate; voting beats debate | G9 | [E] | d16 |
| Zero reframes is a legal path (co-evolution is optional) | G1, G12 | [E] | K03; a15, b06 |

### Test first (not established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| S3-to-S2 return: after a failed check, rewrite the criteria list once, then retry; vs frame once | S3, S2, O8 | [S] | K01, K26, K28; d02 |
| Restate-then-solve (RaR) on ambiguous items | S1 | [S] | K14; b18, d05 |
| Step-back principle call before S3 on science items | S2, O2 | [E] on PaLM-2L; untested on our models | K15; b20 |
| Clarify-then-solve with at most 3 questions on under-specified items | S1 | [E] for code, [S] elsewhere | K19, K34; c20, d08 |
| Missing-information check on logic and planning items | S6 | [S] | K18; c18 |
| Problem-first vs solution-first vs interleaved order | S2 vs S3 | [C] | K07, K08, K32 |
| Gate self-framing by model tier; stronger framer for weak models | S0, S2 | [S] | K35; d05 |
| Stall-triggered monitor that proposes a reframe | S6 | [S] | K20; b15, d04 |
| Hedging language as a soft extra trigger beside a check | S6 | [S] | K31; d03 |
| Force one solution-to-problem return in open mode and code the trace | open-mode S3 | [S] | K23; d01 |
| Long structured reframing chains (Dorst nine steps) | O8 | [S] against; likely not worth it | K10, K11; c03 |

Note on O8: SCHEMA.md already says "LLM reframing null in one large test". That is Shin and is single-source. Keep O8 at impasse only, as written.

## 8. Concrete tests on our bench

All arms equal in total tokens, including monitor and clarify calls. Use plain model and best-of-N as baselines (G7). Report new errors introduced, not only net gain.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-like and puzzle items with a checker | (a) frame once, solve, revise solution only; (b) frame once, on failed check rewrite criteria then retry; (c) resample only | pass rate at equal tokens; share of passes where the frame changed | (b) beats (a) by a few points on items with hidden constraints; ties on easy items |
| T2 | Open-ended design briefs scored by running/checks and blind expert | same three arms | novelty and correctness together (G8) | small or null; tests the checkability boundary |
| T3 | Brainteasers with ambiguous wording | solve; RaR; step-back; best-of-2 matched | accuracy; new-error count | RaR and step-back help if ambiguity is real; tie otherwise |
| T4 | Under-specified items (one missing fact) | solve; ask up to 3 questions with simulated answerer; best-of-N | accuracy; extra calls | gain on logic and planning items, none on closed arithmetic |
| T5 | Mixed items | reframe rounds 0, 1, 2, 3 | accuracy vs rounds; broken-pass rate | gain mostly by round 2; decline after 3 |
| T6 | Items with a seeded wrong premise | no check; premise check in S1 | premise detected rate; accuracy | large detection gain, small accuracy gain |
| T7 | Order | problem-first (long S2), solution-first, interleaved | novelty and correctness | unknown; this is the open dispute |
| T8 | Weak and strong model | self-frame; stronger-model frame; no frame | accuracy | weak model loses from self-frame |
| T9 | Triggers | failed check; stall; hedging; fixed interval | repair rate at equal budget | failed check best |
| T10 | Traces from T1 and T7 | code transitions by content | switches vs score correlation | answers Zhang's open question |

## 9. What does not transfer, and why

- **Human creative leaps.** The "bridge" is a human recognition event seen in nine designers' talk. We have no equivalent signal except a check passing under a new frame.
- **Designer experience.** Expert-versus-novice differences (Shin: 12.54% more novel frames for skilled users) depend on the steering person, not on an autonomous agent.
- **Long structured chains.** The Dorst nine-step chain cost about 22% more time and gave no quality gain. Felt help (CSI 61-65) is not evidence.
- **Human-AI group studies.** Guo and Chen use novices working with a model. Breadth gains and innovation losses may be about how humans use output.
- **Training-based co-evolution.** R-Zero and COvolve change weights or environments. We do not train. Only the drift warning transfers.
- **Persona prompts.** Making the model "act like a problem-driven designer" changed switches but is a persona voter in disguise; G4 forbids personas on single-answer problems.
- **Genetic search.** Maher's population search needs many cheap evaluations. The idea of an editable criteria set transfers; the population does not.
- **Process claims from the model.** A report of "I reframed" is not evidence (G10).

## 10. Open questions

1. Does S3-to-S2 beat frame-once at equal tokens, and on which task types?
2. What are the real numbers behind Dorst and Cross 2001 and Kruger and Cross 2006 (full texts closed)?
3. Which order of work gives higher novelty and correctness?
4. Why do frame steps help on checkable tasks and not on open frames: checkability, model tier, or judge strictness?
5. What is the optimum number of reframe rounds for a scaffolded model?
6. Which solution-side signal best triggers a reframe?
7. Does transition complexity predict quality in LLM traces?
8. Does the Xu et al. gain survive at equal tokens, on other tasks and models?
9. Do clarifying-question steps transfer to open design where no single fact is missing?
10. How much does model tier gate the benefit?

## 11. Sources

[V] opened (page or PDF text read this session), [M] snippet or abstract only. Cross-check corrections applied.

**Founding and human design studies**
- [M] Dorst and Cross 2001 (abstract page only, numbers not read): https://research.tue.nl/en/publications/creativity-in-the-design-process-co-evolution-of-problem-solution/ ; https://doi.org/10.1016/S0142-694X(01)00009-6 [a01, b23, d14]
- [V] Cross 2024 chapters (reprints of 1997, 1999): https://doi.org/10.1007/978-1-4471-7541-4_5 ; https://doi.org/10.1007/978-1-4471-7541-4_4 [a02, a07]
- [M] Maher and Poon 1996; Maher, Poon and Boulanger 2000; Maher and Poon 2002; Maher and Tang 2003 (abstracts): https://doi.org/10.1007/978-0-387-34925-1_1 ; https://doi.org/10.1007/pl00013714 ; https://doi.org/10.1007/978-0-85729-345-9_22 ; https://doi.org/10.1007/s00163-002-0016-y [a03-a06]
- [M] Poon and Maher 1997: https://doi.org/10.1016/S0954-1810(96)00047-7 [b24]
- [V] Kokotovich 2015: https://opus.lib.uts.edu.au/bitstream/10453/41435/1/IASDR2015%20Kokotovich%20Final%20Paper%20378%20.pdf [a08, d11]
- [M] Kokotovich 2008: https://doi.org/10.1016/j.destud.2007.09.001 ; https://opus.lib.uts.edu.au/handle/10453/9818 [a09, b26, d12]
- [V] Storm, van Maanen and Goncalves 2019: https://doi.org/10.1017/dsi.2019.39 [a10]
- [M] Wiltschnig, Christensen and Ball 2013: https://doi.org/10.1016/j.destud.2013.01.002 [a11, b25]
- [M] Christiaans 1992; Akin and Akin 1996 (via Storm): https://doi.org/10.1017/dsi.2019.39 [a12]
- [V] Cash, Goncalves and Dorst 2023: https://doi.org/10.1016/j.destud.2023.101219 ; https://opus.lib.uts.edu.au/bitstream/10453/178995/2/1-s2.0-S0142694X23000601-main.pdf [a13, d03, d20]
- [V] Martinec et al. 2020: https://www.mdpi.com/2076-3417/10/18/6303 [a14, b03-b05]
- [V] Halstrom and Galle 2015: https://doi.org/10.14434/artifact.v3i4.12815 [a15, b06]
- [V] Feast 2024: https://doi.org/10.21606/drs.2024.279 [a16]
- [V] Biskjaer et al. 2026: https://doi.org/10.21606/drs.2026.1221 [a17]
- [M] Chen et al. 2023: https://doi.org/10.1007/s10798-022-09740-7 ; https://link.springer.com/article/10.1007/s10798-022-09740-7 [a18, d15]
- [M] Kruger and Cross 2006: https://doi.org/10.1016/j.destud.2006.01.001 ; https://oro.open.ac.uk/7423 [a19, d13]
- [M] Suwa, Gero and Purcell 2000: https://doi.org/10.1016/s0142-694x(99)00034-4 [a20, b28]
- [V] Hu et al. 2026: https://doi.org/10.21606/drs.2026.1126 [a25]
- [M] Kopecka et al. 2012 (via Kokotovich 2015; same URL as above) [a27]
- [V] Parsons and Shukla 2025: https://arxiv.org/abs/2508.07058 ; https://arxiv.org/pdf/2508.07058 [b01, b02, c01]
- [V] Design science ethnography 2023: https://pmc.ncbi.nlm.nih.gov/articles/PMC10062208/ [b07]
- [M] Atman et al. 2007: https://doi.org/10.1002/j.2168-9830.2007.tb00945.x [b27]
- [V] Goel 2018, 2014: https://pmc.ncbi.nlm.nih.gov/articles/PMC6236478/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4012206/ [b21, b22]

**Human-AI and LLM design studies**
- [V] Guo et al. 2024, 2025: https://doi.org/10.21606/drs.2024.983 ; https://dl.designresearchsociety.org/drs-conference-papers/drs2024/researchpapers/306 ; https://arxiv.org/pdf/2502.00283 [a21, b08, b09]
- [M] Lim and Lee 2025: https://doi.org/10.21606/iasdr.2025.897 [a22]
- [M] Chen et al. 2025 GPSdesign: https://doi.org/10.1080/10447318.2025.2453003 [a23]
- [V] O'Hara 2025: https://doi.org/10.36227/techrxiv.176583345.56962463/v1 [a24]
- [M] Gong et al. 2026: https://doi.org/10.18260/1-2--59833 [a26]
- [V] Chen et al. 2026: https://pmc.ncbi.nlm.nih.gov/articles/PMC13585246/ [b10]
- [V] Frontiers in Psychology 2026 (low reliability): https://pmc.ncbi.nlm.nih.gov/articles/PMC13318989/ [b11]
- [V] Carichon et al. 2026 IDEAFix: https://arxiv.org/pdf/2606.00875 [b12-b14]
- [V] Xu, Martelaro and McComb 2026: https://arxiv.org/pdf/2603.24768 ; https://arxiv.org/abs/2603.24768 [b15, d04]
- [V] Wang et al. 2026 NexusAI: https://arxiv.org/pdf/2604.10575 [b16]
- [V] Ege et al. 2024: https://arxiv.org/pdf/2404.18479 ; https://arxiv.org/abs/2404.18479 [b17, c23]
- [V] Shin et al. 2025: https://arxiv.org/abs/2503.01631 ; https://arxiv.org/pdf/2503.01631 [c02-c06, d06]
- [V] Sood et al. 2026: https://computationalcreativity.net/iccc26/papers/ICCC26_paper_78.pdf [c07-c10]
- [V] Zhang et al. 2025: https://openaccess-api.cms-conferences.org/articles/download/978-1-964867-39-7_12 ; https://openaccess.cms-conferences.org/publications/book/978-1-964867-39-7/article/978-1-964867-39-7_12 [c11, d01]

**LLM prompting and loop studies**
- [V] Deng et al. RaR: https://arxiv.org/pdf/2311.04205 [b18, b19, d05]
- [V] Zheng et al. Step-back: https://arxiv.org/pdf/2310.06117 [b20]
- [V] Zhou et al. Self-Discover: https://arxiv.org/abs/2402.03620 [c22]
- [V] Mu et al. ClarifyGPT: https://arxiv.org/abs/2310.10996 [c20, c21]
- [M] ClarifyCoder secondary report: https://codex.danielvaughan.com/2026/07/28/clarifycodesbench-ambiguous-requirements-clarification-gap-codex-cli-plan-mode-agents-md-elicitation-defence/ [c27]
- [V] Li, Kim and Wang QuestBench: https://arxiv.org/abs/2503.22674 [c18, c19]
- [V] Microsoft Research 2026 Theory Under Construction: https://arxiv.org/abs/2604.27209 [c12-c14]
- [V] Huang et al. R-Zero: https://arxiv.org/abs/2508.05004 [c15-c17]
- [V] COvolve (abstract page only): https://arxiv.org/abs/2603.28386 [c24]
- [V] Luan et al. 2026 Repair or Resample: https://arxiv.org/pdf/2608.25920 [d02, d17]
- [V] Brunzema et al. 2026 Sara: https://arxiv.org/pdf/2608.00316 [d07]
- [V] Allaham et al. 2026: https://arxiv.org/pdf/2610.22382 [d08]
- [V] Huang et al. 2024 self-correct: https://arxiv.org/pdf/2310.01798 [d09, d16]
- [V] Madaan et al. Self-Refine: https://arxiv.org/pdf/2303.17651 [d10]
- [M] Ask Less, Ask Better: https://arxiv.org/abs/2610.24411 [d18]
- [M] Knowing When Not to Answer: https://arxiv.org/abs/2610.08413 [d19]
