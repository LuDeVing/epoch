# Einstellung effect: deep document

*Subfield E16.08. Built from evidence_a-d.jsonl (a01-a29, b01-b25, c01-c28, d01-d19), claims.jsonl (K01-K39) and critique.md. Evidence ids are quoted as a08, K05 and so on. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Einstellung is German for "set" or "attitude". In problem solving it means this: a method that worked before comes to mind first, is used again, and blocks a better method that is equally available.

Two features make it different from plain ignorance.
- The person could find the better route. People without the earlier experience find it easily. In Luchins' data the trained group used the long method 0.83 of the time and the untrained control 0.00 (a02).
- The person does not feel blocked. They search as long as anyone else and report that they are still looking for something better (a13, a16).

Three related terms are often mixed up.
- **Einstellung (set).** A learned routine is reused. The better route is also reachable. This document.
- **Functional fixedness (Duncker).** An object is seen only in its usual use. Same family, but the block is on an object, not a method. Not covered here.
- **Anchoring on a wrong first answer.** The first guess steers the rest. LLM papers on first-step lock-in (d03) and multi-turn drift (c19) are cousins, not the same thing. They have no taught routine.

"Pernicious" Einstellung (Bilalic) is the strong form: the familiar solution is good enough to stop the search, so the better one is never found. The "benign" form is when the familiar method is also the best one.

Why it matters for our agent. A language model has a large store of familiar methods built in. We also feed it routines through examples, retrieved notes and lessons (SCHEMA section 5). Each is a possible Einstellung source. Guardrail G1 (doubt only on a signal) and the S3 rule (fresh context per attempt) are the places where this matters. The research asks four things: how big is the effect, what causes it, what undoes it, and does a scaffold undo it at equal tokens.

Links to other subfields (not covered here): representational change theory, fixation and ideation, chunking and templates, expert-novice differences, retrieval and similarity, cognitive offloading, overthinking, self-correction, case-based reasoning.

## 2. History and theories in depth

### 2.1 The founding studies

**Luchins (1942) water-jar task** (a01, read only as reported by others). People get jar problems: given jars of sizes A, B, C, measure a target volume. Five training problems all fit one long formula. Then "critical" problems appear that also fit a short formula, and an extinction problem that only the short formula solves.
- Over 80% kept the long formula on critical problems (Bilalic 2008, as reported).
- 64% of trained people failed the extinction problem, against 5% of a control group with no training (Luchins and Luchins 1959, as reported).
- Luchins ran more than 1000 people (Binz and Schulz). The original thesis was not opened in this study.

**Binz and Schulz (2021 preprint, a02-a07)** rebuilt Luchins' thesis tables into data (N=310 in the main comparison) and added a model. Details are in sections 3 and 4.

**Saariluoma (1990, a15, via Bilalic)** moved the effect to chess with a smothered-mate position. With the familiar line available, 11% of chosen answers were optimal and 67% were the familiar one. With the familiar line disabled, 69% found the optimal one (two matched groups of 6). 10 of 12 players at first failed to notice a shorter solution. There was no extinction control in the original design.

**Bilalic, McLeod and Gobet (2008)** are the modern anchor.
- Cognitive Psychology 56 paper (a08-a14): three experiments that measured the cost in rating points.
- Cognition 108 paper (a16-a18): eye tracking showed the mechanism.
- The printed Cognition text could not be opened (publisher 403, d19). All numbers rest on the in-press draft, which the critique re-opened and confirmed.

**Wiley (1998, b01-b05)** moved it out of chess: baseball knowledge hurt word puzzles whose baseball answer was wrong.

**Sheridan and Reingold (2013, a19-a20, b22)** replicated with eye tracking and found a boundary (section 5).

### 2.2 Theories

| Theory | What it says | Source | What it explains | What it does not |
|---|---|---|---|---|
| Schema / template theory (Gobet, Simon) | The first schema that matches directs attention to schema-consistent features, which confirms the schema | a18 | Why gaze stays on the familiar squares; why strong players still do better (richer schemas) | Not tested head to head against the others |
| ACT-R production strength / history of success (Anderson, Lebiere; Lovett and Anderson 1996) | A method is chosen by its record of past success | a18, c27 (not opened) | Why a successful old method wins; why success strengthens the set (b20) | Lovett and Anderson details not verified |
| Instance theory (Logan 1988) | Retrieval is a race among stored instances; more instances, faster retrieval | a18 | Why more training means a stronger set (a04) | No direct data |
| Confirmation bias / part-set cuing | The first idea is tested only for confirmation | a18 | Same attention pattern | Loose |
| Resource-rational model (Binz and Schulz) | People trade expected utility against the cost of thinking, with a prior that adapts to the environment | a07 | Training dose, time pressure, DBB instruction, interleaving | Fit to 1940s aggregate data only; predicts reaction times that nobody measured |
| Retrieval-cue account (Beda and Smith 2018) | Fixation comes from the memory strength of the wrong answer and its context cue | b17, b18 | Reinstated context raises the harm | Small effects |
| Accessibility of the right answer (Fang et al. 2026) | A rich semantic network around the right answer protects against induced set | b11, b12 | Why some items show no cost | Borderline p, N=30; matched-pair test not significant |
| Outcome-feedback learning | Old patterns are easier to relearn; success keeps them, punishment frees new learning | b20, b21 | Why a method that keeps paying is kept | Number game, not problem solving |

### 2.3 Where the concept moved

- Education: order of practice problems sets the set and lowers conceptual understanding (DeCaro 2016, b08-b10).
- Programming: 57 of 129 developers showed at least one mental set (c04).
- Clinical reasoning: medical benchmarks built on the idea (c08, a25, a27).
- Creative problem solving: defixation methods (c22).
- Neural nets: a rigidity index for shortcut features in continual learning (c17, a29). The analogy is loose.
- LLM agents: wrong memory followed (d11); stored abstractions keep errors alive (d10).

## 3. Core findings with exact numbers

"H" is human data; "L" is language-model data. Status uses the claim ids.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| H. Trained method kept after a better one exists | Plain 0.83 vs control 0.00 on critical C1/C2 (chi2=218.02, p<.001, N=310); 0.65 vs 0.00 on C3/C4. Early trials 0.83, later 0.65 (chi2=13.00). Over 80% missed the shortcut; 64% vs 5% failed extinction (as reported) | a01, a02 | [E] K01 |
| H. Dose: more training, stronger set | 10 training problems: 112/112 and 111/112 used the long method. 2 training problems: 79/108 (0.73) and 59/108 (0.55) | a04 | [S] K02 |
| H. Variety in training removes most of the effect | Alternating methods: 20/124 used the long method vs 97/121 plain (0.16 vs 0.80; chi2=100.65) | a05 | [S] K02 |
| H. "Don't be blind" instruction reduces but does not remove it | DBB 87/153 (0.57) vs plain 0.83 on C1/C2; 57/153 (0.37) vs 0.65 on C3/C4. The paper prints chi2=24.16 for both comparisons; the second is probably a copy error, do not quote it | a03, critique | [S] K03 |
| H. Time pressure raises it | Speedy group 95/98 (0.97) vs 126/153 (0.82) on C1/C2 (chi2=12.08); 94/98 (0.99) vs 100/153 (0.55) on C3/C4 | a06 | [S] K03 |
| H. Smothered-mate block, Exp 1 | Found the 3-move mate when the 5-move line was also present: GM 100% (n=6), IM 50% (n=6), Master 18% (n=11), Candidate Master 0% (n=11). All who failed found it in the 1-solution version | a08 | [S] K04 |
| H. Cost in rating points | Familiar line cut expert performance to that of players about 3 SD (about 600 Elo) weaker. Odds of success fall by a factor of 3.67 per 100 rating points (B=.013, SE .005) | a09 | [S] K05 |
| H. Exp 2, five tactics, "find the best move" | Optimal move found: IM/GM 92%, Master 69%, Candidate Master 35% (n=12 each). Controls (1-solution): 91%, 66%, 47% (n=8 each). Odds factor 1.82 per 100 points (B=.006, Z=3.72, p=.0002). Predicted .87 at Elo 2500, .67 at 2300, .37 at 2100 | a10 | [S] K05 |
| H. Difficulty bound | Easy problem 5: all experts solved it, only weak players blocked. Hardest problem 3: low even among super experts | a11 | [S] K05 |
| H. Experts underestimate it | Predicted vs actual success. Exp 1: IM 86 vs 50, Master 74 vs 18, Candidate Master 59 vs 0. Exp 2: 97/89/73 vs 92/69/35 (12 judges, mean Elo 2231) | a12 | [S] K06 |
| H. Not a motivation or time effect | Median search time before finding: GM 7 s, IM 9 s, Master 10 s; those who failed 9, 8, 8 s. Exp 2 found vs not found: 9.5 vs 9 s (IM/GM), 12 vs 13 (Master), 20 vs 22 (CM) | a13 | [E] K07 |
| H. A rejected plan stays rejected (Exp 3) | 12 specialists (5 GM, 4 Master, 3 CM): only 1 of 5 GMs found the move. Winners median Elo 2547 vs 2258 (U=2, p=.017) | a14 | [S] |
| H. Eye tracking: attention stays on the familiar line | Blocked group: gaze on smothered-mate squares did not change over six intervals (F(5,20)=0.6). Control group: gaze moved to the optimal squares (F(5,20)=11.9, p<.001, partial eta2=.75). Control found the mate in 79 s (SD 25); blocked group 148 s (SD 90) | a16 | [E] K07 |
| H. Effect lingers after the familiar line is removed | Exp 2: 1-solution problem solved in about half the time by never-blocked players vs earlier-blocked players, t(44)=2.16, p=.036, d=.65. Exp 1 alone 79 vs 148 s, t(8)=1.67, p=.13 | a17 | [S] |
| H. Equal choice by experts and novices on a good-but-suboptimal move | Ba7 chosen by 8 of 17 experts and 8 of 17 novices. First fixation on target region 407 ms experts vs 719 ms novices (t(32)=2.99). Blunder problems 2-4: the effect largely vanished | a19 | [C] K07 |
| H. Finders look away from the familiar region | Experts who found the optimal move (n=9): declining looking time at the target region, F(1,34)=43.45, p<.001. Those who chose Ba7 showed no trend | a20 | [E] K07 |
| H. Anagrams: time cost, not accuracy cost | N=60. Accuracy 51.7% (word) vs 53.8% (nonword), n.s. Time 15.3 vs 13.4 s (p<.01). Central-string dwells 8.11 vs 6.76 (p<.001) | a21 | [E] K09 |
| H. Insight puzzles: knowledge as a set | Exp 1, N=24: high knowledge solved misleading baseball items .15 vs neutral .50; low knowledge .40 vs .50 (F(2,44)=4.06, p<.02). Pooled N=54 interaction F(1,52)=17.66, p<.0001 | b01, b03 | [E] K09 |
| H. A one-sentence warning did not help | Exp 2, N=20 (5 per cell): high knowledge, misleading .20 no warning vs .30 warning, F(1,16)=1.89, n.s. | b02 | [S] K10 |
| H. Water-jar discovery signal | 46 analysed of 60; 31 (67%) found the shortcut before the last critical trial. Two trials before discovery: gaze difference F(1,34)=6.22, p=.018; at discovery F(1,34)=87.16, eta2G=.72. No group difference on the first set trial | a22, b06, b07 | [S] K08 |
| H. Mindfulness lowers water-jar rigidity | Meditators 1.17 (SD 1.75) vs pre-meditators 2.93 (SD 2.02), t(25)=2.40. After a programme 2.19 (n=27) vs 3.42 (n=26), t(51)=2.11. Alphabet-maze and water-jar rigidity r=.10 | a23 | [S] K11 |
| H. Shortcut-first order protects flexible use | Adults N=41: shortcut use 56% vs 19% (chi2(1,N=34)=4.86, p=.028). Children N=87: 30% vs 10% (chi2(1,N=66)=5.21). Conceptual knowledge F(1,39)=4.67 and F(1,82)=5.13. Accuracy equal (97.7 vs 98.8; 96.5 vs 97.0) | b08-b10 | [S] K12 |
| H. Semantic accessibility reduces cost | N=30. Low accessibility: weak induction 1.27 vs strong 0.70 (p=.009, d=0.52). High accessibility 1.90 vs 2.07 (p=.538). Interaction F(1,29)=4.88, p=.035. Matched-pair check (15 pairs) only directional | b11, b12 | [E] K14 (thin) |
| H. Relational encoding | Insight solved 22% (15/68) vs 43% (29/68). Two-string chi2(1,67)=4.23, p=.039; peanut problem p=.109 | b19 | [E] K14 (thin) |
| H. Directed forgetting protects | N=72. Remember-cued primes: target items 27.3% vs control 43.5% (d=-0.92). Forget-cued: 36.7% vs 37.6% (d=-0.06). Forget vs remember on targets t(69)=-2.17, p=.033 | b15, b16 | [S] K13 |
| H. Memory strength of the red herring | Exp 1 N=133: two retrieval practices cut solving, F(1,132)=5.17, partial eta2=.038. Exp 2 N=89: unprimed .539 vs primed with reinstated context .456 (d=.425); new context .506 (n.s.) | b17, b18 | [S] K11 |
| H. Chunk decomposition: set may cost only time | Exp 1 N=32: accuracy interaction F(1,31)=11.00, p=.002. Exp 2 N=28: accuracy n.s. (F=0.06), time interaction F(1,27)=29.50, p<.001 | b13, b14 | [C] K15 |
| H. Success keeps the old pattern | Old vs new pattern win rate .694 vs .592 (75% feedback); .725 vs .622 (88%); gone under 25% punishment. Exp 1: 66.16% vs 61.39% | b20 | [S] K16 |
| H. Programmers show sets | 129 surveyed, 57 with at least one set, 39 finished. Less Python experience, more sets (p=.006). Interventions rated unhelpful (M=0.97 of 5) | c04 | [S] K27 |
| L. Red herrings, Only Connect | 494 test walls. GPT-4 0-shot 6 solved (original) / 59 (randomised) / 471 (WordNet, no decoys); 10-shot 3 / 55 / 378. GPT-3.5 0-shot 0 / 5 / 337; 10-shot 2 / 17 / 428 (corrected table). Naming the connection: GPT-4 F1 41-45 vs humans about 80% correct | c01-c03, critique | [S] K17 |
| L. Clinical traps, mARC, 2025 | 100 items, 5 physicians 66% (SE 5.3). DeepSeek-R1 52%, DeepSeek-V3 50%, Gemini 1.5 pro 50%, o1 48%. Human-miss set (20 items): physicians 36% vs 73% elsewhere | a25, c08 | [E] K21 |
| L. Clinical traps, 2026 | Claude 4.1 Opus 75.1% (CI 73.8-76.3) vs physicians 66%. Gemini 2.5-Pro, GPT-5.1, Grok-4-Fast-Reasoning not different from physicians. Human-miss set: Opus 55.0% decisively right, 25.0% decisively wrong, 20.0% indeterminate | a26, c10, c11 | [E] K21 |
| L. MedEinst trap rate | 5,383 pairs, 17 LLMs. Trap rates 33.75 (ECR-Agent) to 66.10 (Baichuan-M2-32B). Gemini-2.5-pro 60.90, GPT-5 51.87, DeepSeek-R1 46.12, QwQ-32B 44.88, Claude-Sonnet-4.5 42.98, Qwen3-32B 43.46 | a27, c13, c14, d18 | [S] K18, K39 |
| L. Failure modes in MedEinst | GPT-5: key evidence ignored (blindness) in over 35% of errors; when noticed, 43% underthinking and 22% overthinking | c15 | [S] K20 |
| L. Edited-problem items (ReasoningTrap) | p-pass@1: Qwen3-32B think 33.25 (AIME) / 34.60 (MATH500) vs no-think 45.14 / 50.51; QwQ-32B 49.21 vs Qwen2.5-32B 59.12 | d06 | [C] K32 |
| L. Generic hint | Qwen3-32B: 33.25 to 45.30 (AIME), 34.60 to 46.88 (MATH500) with "unusual condition, do not overinterpret". Other wordings: 38.24, 41.23 (AIME); 42.11, 37.75 (MATH500). Originals 75.42 to 81.36 | d07 | [S] K33 |
| L. Mental-set order test | 6 items per cell. GPT-4o 0.33 / 0.66 / 0.66 / 0.83 (SP / SP+CPF / CP / CP+SPF). Llama-70B 0 / 0.16 / 0 / 0.66. Llama-8B 0.16 / 0 / 0 / 0 | c05 | [S] K23 |
| L. Shortcut underuse | SenseMath, 4,800 items, 5 LLMs: strong-shortcut use under plain CoT 20-39% at 4 digits, 37-59% at 16 digits; with a number-sense prompt 68-86% (+47 to +50 pp) | d01 | [S] K30 |
| L. Wrong memory is followed | WebArena, 5 models: wrong plausible memory adopted at the first exposed step 63-72%; success after adoption 17-31% vs 23-49% without memory; damage 2.1 to 25.5 pp | d11 | [S] K35 |

## 4. Mechanisms and models

### 4.1 The Binz and Schulz resource-rational model (a07)

Implementable in about 30 lines.

- State: a prior preference over solution methods, p0(m). Each method has a utility u(m) and a cost.
- Policy: p(m) proportional to p0(m) * exp(beta * u(m)), where beta is the inverse temperature. A low beta means little deliberation, so the prior dominates. A high beta means the policy follows utility.
- Learning: after each trial the prior moves toward the method just used (learning rate 0.5 in their simulation). Training problems that favour method E push p0(E) up.
- Resource limit: beta is capped by a cost on computation. Time pressure lowers it (beta 15 in their simulation vs 25 base).
- Result: with learning rate 0.5 and beta 25, 90 of 100 simulated agents used the long method on critical problems after training, 0 of 100 without. "Don't be blind" is simulated as higher beta. Removing any one of the three ingredients (effort preference, computation cost, prior adaptation) fails at least one of Luchins' results.
- Limits: fit only to 1940s aggregate data. The model predicts reaction times that were never measured.

Engineer reading. The set is a prior over strategies that moves with use, and the deliberation budget decides how far the prior is overridden. For an agent: the number of in-context examples that show a method raises its prior; the reasoning budget plays the role of beta.

### 4.2 The attention account (a13, a16, a20, a22)

- Step 1: a familiar pattern is recognised very early. Its squares (or jars) draw attention.
- Step 2: the person keeps returning to those squares. Gaze on the familiar region does not decline over time (blocked), or does decline (finders).
- Step 3: search time is the same, so the block is about where search goes, not how long it lasts.
- Step 4: the person reports "still looking" and gives a plausible account. Experts predict much less block than there is (a12).
- Early signal. In the water-jar eye data, future finders already looked less at the trained procedure two trials before they reported the shortcut (K08). Nobody has found an equivalent signal outside lab tasks.

Engineer reading. The observable that matters is which candidates are actually expanded or re-checked, not what the text says. Count repeated returns to the same candidate and the share of reasoning tied to the familiar solution.

### 4.3 Retrieval-cue and accessibility accounts (b11, b15-b18)

- Memory of the wrong answer, and of the context it was learned in, sets how much it intrudes (b18: harm only with reinstated context).
- The right answer's accessibility reduces the cost (b11: cost 1.27 vs 0.70 at low accessibility, none at high).
- Removing the wrong answer from memory with a forget cue removes the harm (b15: 36.7% vs 37.6%). The forget cue works only partly: forgotten words were still recalled 19.8% of the time (b16).

Engineer reading. Context and cue overlap decide the harm. An agent that rereads a note whose context matches the new task is in the reinstated-context condition.

### 4.4 LLM-side models

- **Contamination ratio (d09).** Split a reasoning trace into paragraphs. Embed each. Count the share closer to the familiar original solution than to the edited problem. Accuracy holds up to about 40% and falls sharply above. Wrong runs gain contamination as they grow. It needs the familiar solution as a reference.
- **First-step lock-in (d03).** A wrong first step cuts final accuracy by 40% on average (43% hardest third, 33% easiest third). First-prediction correctness correlates r=0.60 with final correctness. Models spend as many tokens after a wrong start as after a right one.
- **Hidden-state settling (d17).** Step-4 hidden-state similarity across repeated runs correlates with later variability, r=-0.35. A monitor built from three partial runs gets AUROC 0.81 for variability. It tracks stability, not correctness.
- **Compliance with conflicting memory (d11).** A task-wrong memory is followed at the first exposed step about two times in three. After divergence, re-alignment is 7-15% vs 27-42% with helpful memory (K35).
- **Self-correction blind spot (d13).** Models fix an error labelled as the user's but not as their own: 64.5% blind spot across 14 open models. Appending "Wait" cuts the blind spot by 89.3%.
- **Learned prior override (d12).** In Leela Chess Zero the correct tactic is present in middle layers and replaced by a quiet move at the end in 68.3% of 8,648 forgotten positions. Steering recovered 71.7% of held-out forgotten puzzles. A prior beating a computation is the same shape as Einstellung but not the same test.

## 5. What holds up

### 5.1 Replications

| Claim | Replicated by | Result |
|---|---|---|
| Familiar chess line blocks a better one | Saariluoma 1990 (via a15), Bilalic 2008 Exp 1-3, Sheridan and Reingold 2013 | Yes for a strong block. Sheridan and Reingold: yes for a good-but-suboptimal familiar move, mostly no when the familiar move is a blunder |
| Trained method kept after a shortcut exists | Luchins; Binz and Schulz (reconstruction of his data) | Yes; the reconstruction is of the same 1940s data, not a new sample |
| Gaze marks the block | Bilalic 2008b; Sheridan and Reingold 2013; Ninomiya 2022 | Yes in three labs (all small) |
| Domain knowledge acts as a set outside chess | Wiley 1998 (3 experiments); Ellis and Reingold 2014 (anagrams); DeCaro 2016 | Yes, but the anagram effect is in time, not accuracy |
| Order of practice sets the set | DeCaro 2016 adults and children | Yes; smaller in children (d=.35 vs .56) |

### 5.2 Failures and limits

- **Experts equal to novices.** Sheridan and Reingold: 8 of 17 experts and 8 of 17 novices chose Ba7. Their experts were mostly Experts and Candidate Masters (mean CFC 2223), below Bilalic's masters. Boundary: the effect needs a believable familiar move.
- **Difficulty dependence.** Bilalic Exp 2: the easy problem 5 showed no effect in Candidate Masters. The expert effect is partly confounded with problem difficulty.
- **Accuracy vs time.** Anagrams: no accuracy cost, a time cost. Chunk decomposition Exp 2: no accuracy cost, a time cost (F(1,27)=29.50). Exp 1 of the same paper shows an accuracy cost. A set can show as delay.
- **Small samples.** Bilalic cells of 6 to 12. Eye-tracking groups about 5 per group (df=8). Wiley Exp 2 had 5 per cell. Fang 2026 N=30 with p=.035 on the key interaction. Beda and Smith partial eta2=.038.
- **Wiley's knowledge groups were intermediate.** The ten top scorers averaged 32.3 on the questionnaire vs 41.3 and 40.0 in earlier baseball-expert samples (b05). The effect may be an intermediate-knowledge effect.
- **Confounded comparisons.** Bilalic's control is a different, weaker sample. The lingering-effect result compares across experiments.
- **Reconstructed data.** Binz and Schulz is a preprint with population-level counts only.
- **Independence.** The "four independent sources" for some claims often means one research group (Bilalic, Reingold, Wiley).
- **Unopened founders.** Luchins 1942, the original Saariluoma paper and Lovett and Anderson 1996 were not opened.

### 5.3 Interventions

| Intervention | Worked | Did not work | Evidence |
|---|---|---|---|
| Interleave methods in training | alternating: 0.16 vs 0.80 use | | a05 |
| "Don't be blind" instruction | partial: 0.57 vs 0.83, 0.37 vs 0.65 | not complete | a03 |
| Time pressure | (it hurts) speedy 0.97 and 0.99 vs plain 0.82 and 0.55 | | a06 |
| Shortcut-first order | 56% vs 19% shortcut use later | | b08 |
| Directed forgetting of the fixating item | 36.7% vs 37.6% (no harm) | forgetting incomplete (19.8% recalled) | b15, b16 |
| Mindfulness training | water-jar rigidity down (2.19 vs 3.42) | did not predict alphabet-maze (r=.10) | a23 |
| Relational encoding | insight 22% to 43% | one of two problems significant | b19 |
| Accessible right answer | no induction cost at high accessibility | direct test n.s. in matched pairs | b11, b12 |
| One-sentence warning (human) | | .30 vs .20, n.s., N=20 | b02 |
| "Forget earlier solutions" cue, colour change (programmers) | | not reliable | c04, c26 |
| Context change (lab) | reported to weaken it (second-hand) | not in programming | c26 |
| Defixation prompts in LLM ideation | about +10% to +41% per metric, partly garbled | measures novelty, not correctness | c22, K26 |

### 5.4 Moderators

- Amount of training: strongly positive (a04).
- Variety in training: strongly negative (a05).
- Time pressure: positive (a06).
- Problem difficulty: the effect is larger when the alternative is hard to see (a11). LLM data point the other way for shortcut use (SenseMath: use rises with problem size, d01).
- Skill: strong players fixate less, but not never (a09, a10).
- Plausibility of the familiar move: it must be good enough (a19).
- Outcome feedback: success keeps the old pattern, punishment frees it (b20).
- Memory context: reinstated context raises the harm (b18).
- Accessibility of the right answer (b11).

## 6. Language models

### 6.1 No direct test of the Luchins design

No paper trains a method in-context, then measures shortcut missing against a no-example control with enough items (K30, critique gap 1). The nearest studies:
- **Haq et al. 2025 (c05-c07).** Adapts DeCaro's equivalence problems, three models, 6 items per cell, no significance tests. GPT-4o 0.33 / 0.66 / 0.66 / 0.83 by condition; Llama-70B 0 / 0.16 / 0 / 0.66. Chain of thought raised Llama to 0.5-0.83 but steps stayed at 3 where humans need 1. Too small to conclude.
- **SenseMath 2026 (d01).** With no taught method, models default to long computation on shortcut-friendly items. Strong-shortcut use 20-39% at 4 digits under plain CoT; a number-sense prompt lifts it to 68-86%. This is baseline underuse, not an induced set. Asked whether a shortcut applies, GPT-4o-mini was right on 100% of strong items and 0% of controls because it said yes to everything; Qwen3-8B 98% and 0% (K37).
- **ReasoningTrap 2025 (d06-d09).** Items are edited so the familiar method gives the wrong answer. The familiar solution comes from pretraining, not from in-context practice.

### 6.2 Behaviour on red herrings and familiar framings

| Setting | Result | Source |
|---|---|---|
| Only Connect, GPT-4 | 6 of 494 walls solved at 0-shot, 3 at 10-shot; 59 with randomised decoys, 471 with none. Ten shots did not help and lowered the no-decoy score from 471 to 378 | c01-c02, critique |
| Only Connect, GPT-3.5 | 0 / 5 / 337 at 0-shot; 2 / 17 / 428 at 10-shot | critique |
| Famous-puzzle framing | Models say "this resembles a famous puzzle" and then apply a heavy method to a trivial question. Claude Opus 4 falls from near 100% to 85-90% as reasoning lengthens; DeepSeek R1 falls from 70% to 30% with 5 distractors; o3 recovers when distractors hide the famous framing | d02 |
| Edited math (Qwen3-32B think) | 75.42 on originals, 33.25 on edited (AIME) | d06, d07 |
| Medical traps | see section 3; the gap to humans closed with newer models | a25, a26 |
| Chess LMs | brittle out of distribution; a 25M model trained only on (position, best move) beats larger chess LMs on a 600-puzzle mate-in-N suite; an external verifier raised move validity from 19.3 to 95.3% and best-move accuracy from 1.2% to 21.2% | c20, c21 |

### 6.3 What changed it, and by how much

| Change | Effect | Source | Note |
|---|---|---|---|
| Newer reasoning models (clinical) | 2025 best 52%; 2026 75.1%, above physicians 66% | a25, a26 | Items now public; contamination possible |
| Generic hint "unusual condition, do not overinterpret" | +12.05 pp (AIME), +12.28 pp (MATH500); originals up | d07 | Wording matters: other hints +5 to +8 pp on AIME; one hint lower than none on MATH500 |
| Cutting thinking budget (low, 2000 tokens) | Edited 33.25 to 53.66, but originals 75.42 to 31.09 | d07 | Not a fix |
| More effort inside o4-mini | MATH500 edited 39.06 to 51.80 to 53.47; AIME 31.25, 41.98, 36.90 | d08 | AIME not monotone |
| Thinking vs no-think twin | thinking worse by 7 to 16 pp on edited items | d06 | |
| Longer reasoning (Misleading Math) | Opus 4 from near 100% to 85-90% | d02 | |
| Stop at the first correct prefix | beats standard reasoning by up to 21% (about 10% average) | d14 | Not knowable at run time; plain early stopping raised harmful overthinking from 10.1 to 14.1-18.4 |
| Show the old answer as someone else's draft; append "Wait" | blind spot cut 89.3%; fine-tuning on 5,306 traces cut it 76.0% | d13 | Injected math errors, open non-reasoning models |
| External feedback (near-perfect) | still plateaus below target on nine tasks; counterfactual arithmetic never above 20% after 10 rounds | d16 | |
| Critic coupled to solver | broadcast discussion: critique changed the answer 93.5% of the time vs 33.6% with a more precise reviewer (precision 0.644 vs 0.861) | d05 | |
| Self-correction without feedback | GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 89.0; with oracle labels GPT-3.5 GSM8K 84.3 | c18 | 2023 models |
| Multi-agent consensus (MedEinst) | MDAgent 29.70 / 10.34 / 40.34 and DyLAN 32.11 / 8.11 / 41.69 vs base 40.25 / 11.86 / 43.46: accuracy down 8-10, trap rate down only 2-3 | d18 | Voting raising the trap rate is not shown |
| Structured evidence audit + validated-path memory | 40.25 / 11.86 / 43.46 to 55.49 / 19.94 / 38.32 (+DCI) to 69.49 / 24.21 / 33.75 (+DCI+CGME) | c16, d18 | Same authors made benchmark and method; one base model |
| Debate vs vote (Qwen2.5-7B) | single 0.7205, majority 0.7691, centralised debate 0.6551 | d04 | General benchmarks |
| Raw trajectories vs abstractions in memory | 53.5% vs 49.0%; on-demand guidance that is discarded 59.9% | d10 | Mean of 9 settings |
| Wrong memory injected | followed 63-72%; damage grows with agent strength | d11 | Injected, not retrieved |

### 6.4 Where LLM fixation shows

- Not noticing the key fact (blindness), under-weighing it, or arguing toward the prior: GPT-5 over 35%, then 43% and 22% (c15).
- Overconfidence on the very items missed (Kim 2025). Larger models were better calibrated but still overconfident (c09). Newer reasoning models have better Brier scores (c12).
- Locking in at the first step (d03) and in conversation (c19: 39% drop, unreliability +112%, aptitude -15%).
- A learned prior overriding a computed solution (d12).

### 6.5 Honest summary

LLMs plainly show fixation on familiar framings and decoys. No clean measure exists of the in-context Luchins effect, of the size of a taught-method set against a control, or of which de-fixation operation works at equal tokens. The gap to humans changed a lot between 2025 and 2026 models, so any old number is perishable.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = SCHEMA section 5.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep "lessons shown only after a first attempt" (already in memory). The effect itself is established: a taught or retrieved routine becomes the default and is not noticed as one. The specific remedy is still single-source | memory | effect [E]; remedy [S] | K01, a02, a05, d11 |
| A2 | Judge the search by what is actually expanded, not by what the text says. Log which candidates are returned to. Consistent with G10 | G10, S4 | [E] | K07, a13, a16, a20 |
| A3 | Use an external check, not "think again", to decide whether a first working answer is final | G2, G3, S4 | [E] (K29); K24 single-source | K29, c20, c18 |
| A4 | Do not trust stated confidence or a self-rated "is the shortcut applicable" as a gate. Experts under-predicted the block by 36 to 59 points; models say yes to every applicability question | G1 | [E] (K22); K37 single-source | K06, K22, K37, a12, c09, d01 |
| A5 | Build the bench with fixation items from several domains, not chess only (anagrams, insight puzzles, arithmetic shortcuts, medical, programming) | bench | [E] | K09, a21, b01, c04 |
| A6 | Restate the problem in relational terms in S1/S2 before generating. Support is thin: 22% to 43%, one of two problems significant | S1/S2, O6 | [E] on claim file, thin | K14, b19, b11 |
| A7 | Chess-trained LMs are not an Einstellung test; they show pattern reliance, and an external verifier helps | bench | [E] | K29, c20, c21 |

Note on A1 and A6: the claim file marks the underlying claims established, but no LLM test exists for the specific remedy. Keep an [S] tag on the remedy in SCHEMA until the section 8 tests are run.

### 7.2 Test first (not yet added)

| # | Idea | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | After a first working answer, look for a shorter route only when a signal fires (G1). Candidate signals: share of the trace tied to a retrieved or earlier solution above about 40%; first step matches the earlier solution; repeated returns to one candidate | G1, S6 | [S] | K34, d09, d03, d17 |
| T2 | A short specific warning ("a familiar method may not be needed here") | G1 | [S] for LLMs; human null | K33, K10, K11, d07, b02 |
| T3 | Forced generation of one alternative route (O4/O6) after a working answer, vs warning, vs external check | S3, O | [C] | K11 |
| T4 | Present the earlier answer as a third party's draft to a checker role that must reject and redo | G-check, S5 | [S] | K36, d13, d05 |
| T5 | Mix methods among the in-context examples; keep the number of examples low | S2, memory | [S] human only | K02, a04, a05 |
| T6 | Shortcut-first ordering of examples | S2, memory | [S] human only | K12, b08-b10, c05 |
| T7 | Store raw cases, rebuild guidance per task, and treat any retrieved solution as a hypothesis | memory, S3 | [S] | K35, d10, d11 |
| T8 | Drop or tag a blocking candidate out of context (forget cue) vs keeping it visible | S3, memory | [S] human only | K13, b15, b16 |
| T9 | Rule: when the trace says "this is like known problem X", write one line on why X's method is or is not needed | G1, S3 | [S] | K31, d02 |
| T10 | Reasoning length: short vs long vs long with a constraint checkpoint | G11 | [C] | K32, d06, d07, d08, d14 |
| T11 | Critic vs consensus on counterfactual pairs | G9 | [S] | K19, K36 |
| T12 | A negative-check signal when the first method fails | S5, S6 | [S] human only | K16, b20 |
| T13 | Tag failure modes in traces: not seen, seen but not weighed, rationalised | S9 | [S] | K20, c15 |

Tension with the schema. G11 says think briefly and S3 says fresh contexts. The Einstellung data do not argue against these: extra reasoning did not cure fixation (K32 [C]), and fresh contexts remove the in-context routine. But no study shows that fresh contexts reduce Einstellung specifically. That is test material, not an addition.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (prompt plus output), at least 30 items per cell, at least 3 seeds, per-cell rates with intervals. Items are matched trap and control twins: same surface and difficulty, one has a shorter or different route that only the trap item rewards. Score a trap loss as a difference from the control twin, not as a raw score (MedEinst's definition). Report the human-miss subset separately where one exists.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Luchins-style arithmetic or jar items: solved examples of one long method in context, then critical items with a short route, then extinction items only the short route solves | (a) 5 examples, (b) 0 examples, (c) 2 examples, (d) 10 examples, (e) 5 mixed-method examples | Shortcut rate on critical items; failure rate on extinction items; tokens per solution | (a) clearly above (b); (d) above (c); (e) near (b). Human anchor: 0.83 vs 0.00; interleaved 0.16 vs 0.80. The gap in a model may be smaller or larger; the point is to measure that it exists |
| B2 | Trap/control twins in medical or logic domains (MedEinst-style, mARC-style) | plain; scaffold with G1 signals; scaffold with external check | Trap rate (control right, trap wrong); accuracy on the human-miss set | Trap rate down at least 5 pp vs plain. The MedEinst audit agent moved 43.46 to 33.75 (about 10 pp) |
| B3 | ReasoningTrap-style edited items (condition changed so the familiar method fails) | plain; generic hint; forced alternative; external check; third-party-draft checker | p-pass@1 on edited and original items; contamination ratio | Generic hint about +12 pp as in d07. The question is whether forced alternative or the checker beats it |
| B4 | Decoy sets (Only Connect style, or our own decoy puzzles) | plain; scaffold with S3 history of directions; scaffold with harvest | Groups correct; walls solved; with/without-decoy gap | Decoy gap shrinks. Judge by the gap, not by the level |
| B5 | Memory as Einstellung source: a retrieved past solved example at three similarities (near, medium, far) and three success counts (1, 3, 10) on tasks where the old solution is wrong or longer | retrieval off; retrieval before attempt; retrieval after first attempt (our rule); raw trajectory vs abstraction | Adoption rate of the old method; final success; step at which divergence is corrected | Adoption rises with similarity and success count; "after first attempt" lowers adoption at equal or better success |
| B6 | Early signal on B1 and B3 traces | Log contamination ratio, first-step match, repeated candidate returns | AUROC of each signal for a missed shortcut | AUROC at least 0.7 for one signal; compare with the 40% knee in d09 |
| B7 | Reasoning length on B1 and B3 | short cap; long; long with a constraint checkpoint | Trap gap; tokens | No direction assumed (K32). A checkpoint arm beating both would be the new finding |
| B8 | Confidence on trap vs control twins | Ask for confidence before and after the answer | Confidence gap between trap and control; ECE per set | If confidence on wrong trap items equals that on right control items, confidence cannot trigger a re-check |
| B9 | Difficulty sweep | matched twins in three tiers (shortcut easy, medium, hard to see) | Trap gap per tier | Bilalic: gap near 0 when easy, large when hard. SenseMath points the other way. Either result is useful |
| B10 | Critic coupling | single; solver + critic whose output is forced into the next attempt; solver + critic whose output is optional; majority vote of 3 | Trap rate, uptake, repair rate | Forced uptake beats optional (d05: 93.5% vs 33.6% uptake). Vote not expected to help (G4, G9) |
| B11 | Chess slice (optional): mate-in-N positions with a familiar longer mate vs a shorter mate, against the same with the familiar line removed | plain LLM; LLM plus engine check; chess-trained LM | Shorter mate found; length of the answer line | A gap between the two versions would be the first Bilalic-type test in a model; an engine check should close it |

## 9. What does not transfer, and why

- **Eye gaze.** Humans show attention by gaze. A model has none. The nearest are token overlap with the familiar solution and hidden-state similarity. None is shown to be causal (d09, d17).
- **Rating-point cost.** The 100-Elo odds factors (3.67, 1.82) are measured on chess players and say nothing about model size or strength. MedEinst finds no size trend (a27, c14).
- **Skill as protection.** In humans skill reduces the block. In LLMs higher accuracy did not mean fewer traps (K18, K39), and stronger agents lose more from wrong memory (d11).
- **Warning instructions.** A human warning did not help (b02) but an LLM hint did (d07). Humans and models respond differently to cues; only direct tests count.
- **Time pressure.** Models do not feel time. The analogue is a token cap, and it both helped and hurt (d07).
- **Mindfulness.** No analogue for an agent. Skip.
- **Directed forgetting.** Models do not forget. The analogue is dropping an item from context, which is easier than human forgetting and untested (K13).
- **Learning within a session.** The human set forms over minutes of practice. A model's weights do not change; the set comes only from the context. The learning-rate part of the Binz model maps to the number of in-context examples, not to learning.
- **1940s water-jar tables.** Population counts, no individual data, no reaction times. Good for direction, not for effect sizes in 2026 models.
- **Multi-turn drift (c19) and first-step lock-in (d03).** These are the model's own early guess, not a taught routine. Related, not the same.
- **Creative defixation (IDEAFix).** Measures novelty, not correctness (c22).
- **Neural rigidity index (c17).** The authors' test shows distraction, not human-like rigidity.
- **Leela behaviour (d12).** A learned prior overriding a calculated move; not a familiar-longer vs shorter-mate test.

## 10. Open questions

1. Does a plain LLM show the Luchins pattern from in-context examples against a no-example control, and how big is it? (K30; the most decision-relevant open item.)
2. Which de-fixation step works at equal tokens: generic hint, forced alternative, relational restatement, or external check? (K11)
3. Does more reasoning reduce or raise fixation? Evidence conflicts (K32).
4. Does a critic coupled to the solver cut the trap rate while voting does not? Only the critic half has support (K19, K36).
5. Is a retrieved past solution an Einstellung source for agents, and how does harm scale with similarity and success count? (K35)
6. Is there an early signal that works outside benchmarks with a known familiar solution? (K34 needs the familiar solution as reference.)
7. Do models know when they are fixated? Confidence on trap vs control is unmeasured (K37).
8. Does the difficulty dependence hold for LLMs? (K39)
9. Do chess engines or chess LMs show a Bilalic-type miss on a shorter mate vs a familiar longer mate? (K38)
10. What does the printed Cognition 2008 text change in the numbers? (d19)
11. Is the human effect larger or smaller for true masters than in the 2008 samples? Sheridan and Reingold used lower-rated experts.
12. How much of the 2025-2026 clinical gain is real flexibility, and how much is contamination of the now public items? (a26)
13. Is the Wiley warning null real or a power problem (N=20, 5 per cell)? (b02)
14. Does fixation in models show as extra tokens rather than wrong answers, as in some human tasks? (K15) Needs both measured.

## 11. Sources

[V] opened and read this session. [M] snippet, abstract or secondary report only.

**Founding and human studies**
- [M] Luchins (1942) Mechanization in problem solving; Luchins and Luchins (1959), as reported in a01. https://osf.io/preprints/psyarxiv/yhcf4 (via Bilalic 2008 and Binz and Schulz)
- [V] Binz and Schulz (2021 preprint) Reconstructing the Einstellung effect. https://osf.io/preprints/psyarxiv/yhcf4 (a02-a07)
- [V] Bilalic, McLeod, Gobet (2008) Inflexibility of experts: reality or myth? Cognitive Psychology 56. https://doi.org/10.1016/j.cogpsych.2007.02.001 (a08-a14; in-press draft text)
- [V] Bilalic, McLeod, Gobet (2008) Why good thoughts block better ones. Cognition 108. https://doi.org/10.1016/j.cognition.2008.05.005 (a16-a18; draft text). [M] printed record only (c28, d19)
- [M] Saariluoma (1990) Apperception and restructuring in chess players' problem solving, as reported in Bilalic 2008. https://doi.org/10.1016/j.cogpsych.2007.02.001 (a15)
- [V] Sheridan and Reingold (2013) The mechanisms and boundary conditions of the Einstellung effect in chess. https://pmc.ncbi.nlm.nih.gov/articles/PMC3790829/ (a19, a20, b22, b23)
- [V] Ellis and Reingold (2014) The Einstellung effect in anagram problem solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC4079068/ (a21)
- [V] Ninomiya, Terai, Miwa (2022) Attention to the trained procedure in finders and non-finders. https://pmc.ncbi.nlm.nih.gov/articles/PMC9447375/ (a22, b06, b07)
- [V] Greenberg, Reiner, Meiran (2012) Mind the trap: mindfulness practice reduces cognitive rigidity. https://pmc.ncbi.nlm.nih.gov/articles/PMC3352909/ (a23)
- [V] Huang, Tang, Hu (2018) Unconditional perseveration of the short-term mental set in chunk decomposition. https://pmc.ncbi.nlm.nih.gov/articles/PMC6297678/ (a24, b13, b14)
- [V] Wiley (1998) Expertise as mental set. https://doi.org/10.3758/BF03211392 (b01-b05)
- [V] DeCaro (2016) Inducing mental set constrains procedural flexibility and conceptual understanding in mathematics. https://doi.org/10.3758/s13421-016-0614-y (b08-b10)
- [V] Fang et al. (2026) Semantic accessibility and experience-induced heuristic fixation. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13117359/ (b11, b12, b25)
- [V] Gauselmann and Tempel (2025) Preventing fixation: item-method directed forgetting. https://doi.org/10.3758/s13423-024-02564-7 (b15, b16)
- [V] Beda and Smith (2018) Chasing red herrings. https://doi.org/10.3758/s13421-018-0799-3 (b17, b18)
- [V] Kurtz et al. (2025) Relational encoding promotes creative insight. https://doi.org/10.3758/s13421-025-01685-1 (b19)
- [V] Recover or discover: outcome feedback and response patterns (2026, npj Science of Learning). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13315270/ (b20, b21)
- [V] Review on Bayesian reasoning with the adaptive toolbox (2026). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13481750/ (b24; secondary)
- [V] Sergeyuk et al. (2023) Overcoming the Mental Set Effect in Programming Problem Solving. https://arxiv.org/abs/2307.06673 (c04, c26)
- [V] Liu, Karimnazarov, White (2025) Trapped by Expectations: functional fixedness in LLM-enabled chat search. https://arxiv.org/abs/2504.02074 (c24; abstract page)
- [M] Lovett and Anderson (1996) History of success and current context in problem solving. https://doi.org/10.1006/cogp.1996.0010 (c27; not opened)

**Language-model studies**
- [V] Alavi Naeini et al. (2023) Large Language Models are Fixated by Red Herrings. https://arxiv.org/abs/2306.11167 (a28, c01-c03; Table 5 corrected in critique)
- [V] Haq et al. (2025) Is your LLM trapped in a Mental Set? https://arxiv.org/abs/2501.11833 (c05-c07)
- [V] Kim et al. (2025) Limitations of LLMs in clinical problem-solving from inflexible reasoning (M-ARC). https://arxiv.org/abs/2502.04381 and https://pmc.ncbi.nlm.nih.gov/articles/PMC12606185/ (a25, c08, c09)
- [V] Shidara et al. (2026) Advances in LLM reasoning enable flexibility in clinical problem-solving. https://arxiv.org/abs/2601.11866 and https://pmc.ncbi.nlm.nih.gov/articles/PMC13274283/ (a26, c10-c12)
- [V] Chen, Zhu, Huang, Wang (2026) MedEinst. https://arxiv.org/abs/2601.06636 and https://arxiv.org/html/2601.06636v1 (a27, c13-c16, d18)
- [V] Gu and Shi (2025) Einstellung Rigidity Index. https://arxiv.org/abs/2510.00475 (a29, c17)
- [V] Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (c18; indirect)
- [V] Laban et al. (2025) LLMs Get Lost in Multi-Turn Conversation. https://arxiv.org/abs/2505.06120 (c19; indirect)
- [V] Tang (2026) Brittleness testing for chess-trained language models. https://arxiv.org/abs/2605.17565 (c20)
- [V] Meszaros, Reizinger, Huszar (2025) Out-of-distribution tests reveal compositionality in chess transformers. https://arxiv.org/abs/2510.20783 (c21; abstract and introduction)
- [V] Carichon et al. (2026) IDEAFix. https://arxiv.org/abs/2606.00875 (c22, c23)
- [V] Leins et al. (2026) LLM orchestration methods across chess puzzles, competitive programming and math. https://arxiv.org/abs/2608.00685 (c25; abstract page)
- [V] Zhuang et al. (2026) SenseMath. https://arxiv.org/abs/2604.01988 (d01)
- [V] Gema et al. (2025) Inverse Scaling in Test-Time Compute. https://arxiv.org/abs/2507.14417 (d02)
- [V] Liao et al. (2025) Lost at the Beginning of Reasoning. https://arxiv.org/abs/2506.22058 (d03)
- [V] Choi, Zhu, Li (2025) Debate or Vote. https://arxiv.org/abs/2508.17536 (d04)
- [V] Yang et al. (2026) Precise but Uncoupled. https://arxiv.org/abs/2607.15388 (d05)
- [V] Jang et al. (2025) Reasoning Model is Stubborn (ReasoningTrap). https://arxiv.org/abs/2505.17225 (d06-d09)
- [V] Wang, Panaganti, Zhou (2026) More Memory, Worse Agents. https://arxiv.org/abs/2610.27406 (d10)
- [V] Chen, Bai, Yuille (2026) The Compliance Trap. https://arxiv.org/abs/2607.10608 (d11)
- [V] Sandmann, Lapuschkin, Samek (2026) The Algorithm Is Not the Behavior. https://arxiv.org/abs/2508.21380 (d12)
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778 (d13)
- [V] Caldarella et al. (2026) Thinking Past the Answer. https://arxiv.org/abs/2606.02835 (d14)
- [V] Tang et al. (2026) MemTransfer. https://arxiv.org/abs/2609.32313 (d15; weak)
- [V] Jiang et al. (2025) Feedback Friction. https://arxiv.org/abs/2506.11930 (d16)
- [V] Mehta and Datta (2026) When Agents Commit Too Soon. https://arxiv.org/abs/2606.22936 (d17)
- [M] Bilalic et al. printed Cognition record (Crossref, Europe PMC). https://doi.org/10.1016/j.cognition.2008.05.005 (d19)
