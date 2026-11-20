# Deliberate practice: deep document

Scope: goals, feedback, repetition and rising difficulty as a route to expert performance. The row in SUBFIELDS.md says "meta-analytic r = 0.40 [V3]" and "background only (agent does not practice)". This document keeps that verdict and says what little carries over. Evidence ids (a01, b05, c13, d08 ...) point to evidence_a-d.jsonl in this folder. Claim ids (K01 ...) point to claims.jsonl (full id A10.04-K01). Checks done in critique.md are folded in.

Links to other subfields (not covered here): Limits of deliberate practice (05), Expert-novice differences, Chunking and templates (03), Testing effect, Working memory training transfer, RL on verifiable rewards, Automated discovery.

## 1. What it is

Deliberate practice (DP) is effortful activity designed to improve current performance. Ericsson, Krampe and Tesch-Romer (1993) named four conditions: a well-defined task of suitable difficulty, informative feedback, repetition, and error correction (a01). They set it against work (paid performance) and play (no goal).

The 1993 claim has three parts.
- Performance level is directly related to the amount of DP (a01).
- DP is effortful and not inherently enjoyable, and is capped at about 4 hours a day by fatigue (a04, a05).
- Innate talent matters little, except body size in some sports (a09).

Two things people attach to it are not in the paper. The "10,000 hours" figure is an extrapolation from one group of Berlin violinists, not a threshold (a10). Gladwell popularised it. Ericsson and Harwell (2019) say he never used the term DP properly.

The definition is loose on who designs the practice. Teacher-designed, self-designed and any structured solitary practice have all been counted as DP (a01, b03, b12). Much of the later dispute is about this definition (K04).

Why it is background for us: our agent does not learn between tasks, so it cannot practise. Only the four conditions map to anything we build. Training-time loops for LLMs (curricula, self-play, retry with feedback) copy the form. Inference-time scaffolds can borrow only the within-session part: attempt, external feedback, rewrite, retry.

## 2. History and theories in depth

**Before 1993.** Chase and Simon's chunking work and Chase and Ericsson's digit-span training (a08) showed that skill comes from a better method, not mere repetition. One subject who only rehearsed barely improved. Subjects who encoded with prior knowledge improved greatly. One using retrieval structures gained over 1000%. This is cited in the 1993 paper, not tested there. It is the closest human analogue to "design a better scaffold" over "do more reps".

**1993 paper (a01-a10).** Two studies in Berlin.
- Study 1, violinists: three groups of 10 (best, good, music-education students), plus 10 middle-aged professionals. The best group was 10 of 14 nominated as potential international soloists (a02). Accumulated solitary practice to age 18: best 7,410 h, good 5,301 h, music teachers 3,420 h. Middle-aged professionals: 7,336 h (a03). Diary week: the two top groups practised alone 24.3 h per week against 9.3 h for teachers. Sessions averaged about 80 min in all groups. The difference was sessions per week (19.5 vs 7.1) (a04). Top groups slept more (8.6 vs 7.8 h per day) and napped more (a05).
- Study 2, pianists: experts 7,606 h by age 18 against 1,606 h for amateurs. Diary week 56.75 h of music against 7.02 h (a06). Practice predicted tapping and bimanual coordination about as well as group membership did (a07).
- The theory claim: "complete correspondence" between skill and practice, no late catch-up possible (b04), and talent as a predisposition to start DP early (a09).

**2008-2014: popular spread and first attacks.** Meinz and Hambrick (2010) found working memory added prediction of piano sight-reading beyond DP (b17, abstract only). Mosing et al. (2014) found in about 10,500 Swedish twins that identical twins differing in practice did not differ in music ability, and that practice amount itself is 40-70% heritable (b16, b24). Hambrick et al. (2014) reanalysed chess and music: DP explained about one-third of reliable variance, 34% chess and 29.9% music (b08, a17).

**2014: meta-analysis.** Macnamara, Hambrick and Oswald (a11-a15): 88 studies, 111 samples, 157 effects, N=11,135. Overall r=.35, 12% of variance as first published. A 2018 corrigendum moved this to r=.38, 14%, with domains 24/23/20/5/1% (d01, d05). Platz et al. (2014) did music only with strict criteria: 13 studies, N=788, r=.54 observed, .61 corrected (a16).

**2016-2019: sports, replication, rebuttal.**
- Macnamara, Moreau and Hambrick (2016): sports, 52 samples, r=.43, 18%. Elite samples r=.11, about 1% (a18, a19).
- Ericsson and Harwell (2019) re-coded the 2014 corpus with three criteria and kept 14 of 88 studies (b09). They got r=.54 (a20; Hambrick's table gives .56 with k=8) and, corrected, .61 (b10).
- Macnamara and Maitra (2019) ran a preregistered, double-blind replication of the violin study (a22, a23, b01-b04).
- Miller et al. (2019) re-analysed and got r=.40 (b06). That is the figure in our SUBFIELDS row.

**2020-2026: consolidation.** Macnamara and Hambrick (2020) review (b06-b09, d01-d04). A 2024 twin study found genetic variance did not fall with more practice (a24). Macnamara et al. (2022) found world-class athletes had more multisport childhood practice and slower early progress than national-class athletes (b20). LLM-era work appears from 2022 (section 6).

**Competing explanations of the practice-skill link.**
1. Practice causes skill (Ericsson). Prediction: r near the corrected .6-.8 in properly coded data.
2. Practice is a marker of aptitude and motivation (twin data, b16, b24). Prediction: effect shrinks within twin pairs. It did in Mosing 2014.
3. Recall bias: people infer past practice from present skill (a14: interview r=.45, questionnaire .34, logs .22).
4. Capacity limits: working memory and fluid ability add independent prediction (b17, b18).
5. Range restriction at the top (b11). Untested (d04).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Violinist practice alone to age 18 orders with skill | best 7,410 h, good 5,301, teachers 3,420; best vs good F(1,27)=4.59, p<.05; N=30 | a03 | Partly replicated (K07, K08) |
| Diary week: top groups practise more sessions, not longer ones | 24.3 vs 9.3 h per week; sessions 19.5 vs 7.1; mean 80 min; F(1,27)=44.05 | a04 | Single-source, K07 |
| Sleep and naps higher in top groups | sleep 60.0 vs 54.6 h/week; naps F=5.92, p<.05 | a05 | Single-source, correlational |
| Pianists: experts vs amateurs | 7,606 vs 1,606 h by 18; diary 56.75 vs 7.02 h; F(1,22)=26.29 | a06 | Single-source; easy contrast |
| Blind replication of violin study: best does not beat good | best n=13 8,224 h [6400,10048]; good n=13 9,844 [6937,12751]; less accomplished n=13 4,558; chi2(2)=13.90, eta2=.26 (original .48); 82% power for eta2=.23 | a22, b01, b02 | Established (K08) |
| Teacher-designed practice explains no more than practice alone | best 6,251 h vs good 6,821; t(24)=-0.37, p=.717 | a23, b03 | Single-source (K09) |
| 2014 meta-analysis, overall (post-corrigendum) | r=.38, 14%; originally r=.35, 12% [.30,.39]; 88 studies, 157 effects, N=11,135 | a11, d01 | Established (K01, K23) |
| By domain (post-corrigendum variance) | games 24, music 23, sports 20, education 5, professions 1%. Original r: .51, .46, .42, .21, .05 | a12, d01 | Established (K02) |
| Predictability moderates | high r=.49, moderate .35, low .21; Q(1)=20.49 | a13 | Single-source (K03) |
| Cleaner measurement, smaller effect | interview r=.45, questionnaire .34, logs .22 | a14 | Single-source |
| No publication bias in 2014 corpus; mild in sports | sports published r=.48 vs unpublished .33, Q(1)=4.23, p=.04 | a15, a19 | Mixed |
| Music-only strict meta-analysis | 13 studies, N=788, r=.54, corrected .61 [.54,.67] | a16 | Contested (K04, K05) |
| Sports meta-analysis; elite athletes | 52 samples, r=.43, 18%; elite r=.11, p=.50; sub-elite .44; Q(2)=7.04 | a18 | Contested (K06) |
| Ericsson and Harwell strict re-coding | r=.54 [.44,.63]; corrected .61 (36%); games .50 k=5, music .71 k=3, sports .58 k=5, education .31 k=1 | a20, b10 | Contested; authors are the theory holders |
| Corrected value depends on assumed reliability | at .70: 2014 meta .54, Platz .87, sports .64; at .90: 2014 .42 | b07 | Contested (K05) |
| Recall reliability is only measured over short spans | chess diary vs weekly r(34)=.60; musicians .60-.75; athlete vs parent .59; Ward 2007 older years not significant | a21, d03 | Established (K24) |
| Practice is heritable | practice amount 40-70% (Mosing 2014, about 10,500 twins); music auditory discrimination about 50% genetic, constant with practice (6,471 twins, 1,302 pairs) | b16, b24, a24 | Contested (K11) |
| Working memory and ability add beyond practice | DP nearly half of sight-reading variance, WM adds; fluid intelligence-chess r=.32 low skill vs .14 high | b17, b18 | Single-source, abstract-level for b17 |
| Chess hours to master vary 8-fold | 3,016 to 23,608 h, N=90, practice-rating r=.42 | d02 | Single-source |
| Early multi-sport practice predicts world class | 51 reports, 477 effects, 6,096 athletes incl. 772 world-class | b20 | Single-source, abstract-level |
| Simulation training with DP in medicine | effect size 0.71 [.65,.76], 14 studies | b21 | Abstract-level |
| AI tutor with metric feedback, randomised | N=70; practice score gain 0.66 vs instructor; blinded OSATS not significant (4.63, 4.40, 3.86) | a27 | Single-source; tutor is not an LLM |
| LLM patient simulator pilot | 1,024 encounters, 410 learners; volunteers vs others no gain (p>.30); LLM score exact match 32.5%, within one point 64.1% | a26 | Pilot, contested (K21) |
| LLM live hints to human tutors | 900 tutors, 1,800 students; mastery +4 pp (p<.01), +9 pp for low-rated tutors | c16 | Single-source (K20) |

## 4. Mechanisms and models

Written so an engineer can implement them. The human findings give a loop; the LLM literature shows which parts of the loop carry the gain.

**4.1 The DP loop as an algorithm.**
```
state: skill estimate s, task pool P with difficulty d(t), memory M
repeat:
  t = pick task from P with success probability near 0.5 for current s   # rising difficulty
  y = attempt(t, M)
  f = external_check(t, y)         # informative feedback: located, not an opinion
  if f fails: lesson = diagnose(t, y, f); M = distil(M, lesson)   # error correction
  update s from outcome
```
Each line has an LLM counterpart in section 6. Remove the external check and the loop stops helping (K18).

**4.2 Why mid-difficulty.** For binary reward and pass rate p, the group-normalised policy-gradient signal on a prompt is zero when p=0 or p=1 and largest at p=0.5 (c02, c03, c04, d06). SPEED-RL gives the gradient signal-to-noise theory. Before filtering, 34% (1.5B) and 25.8% (7B) of 1000 DAPO-17k prompts had pass rate exactly 0 (d06). This is the engineering form of "suitable difficulty". Implementation: estimate p with a few cheap rollouts, keep items with 0.2<p<0.8, count the screening cost.

**4.3 Learnability reward for self-set tasks.** R-Zero rewards the challenger with 1-|2p-1|, maximal at p=0.5 (c06). Absolute Zero scores proposed tasks by learnability and uses a code executor as verifier (c01). Self-Challenging agents attach a verification function and test cases to each task they write, and filter bad tasks (c07).

**4.4 Within-session retry with rewrite.** Reflexion: attempt, external feedback, written reflection, retry (c14, d10). EvoTest: after each episode an evolver model rewrites prompt, memory, hyperparameters and tool use, with a UCB rule to choose among variants (d13, d14). Greedy selection without UCB gave catastrophic drops after lucky mutations (d14). The rewrite quality depends on the evolver model: o3 0.94, DeepSeek R1 0.90, Qwen3-32B 0.82, Qwen3-8B 0.68, static 0.21 (Detective AUC, d14).

**4.5 Memory distillation.** Keep lessons, not raw trajectories, and cap size. A 2026 study found lesson distillation beats raw trajectories, and an intermediate memory size beats full memory (d17, abstract-level numbers). ExpeL found both abstraction and retrieval matter: random example selection 40.0 vs ExpeL 59.0 on ALFWorld (d12). This matches SCHEMA section 5 (one-line lessons, trusted after two successes).

**4.6 Capacity limit.** Practice does not remove working-memory limits (b17). For an LLM the analogue is context and base model strength: small models gain little from test-time learning loops (d09, d14).

**4.7 Hard-to-easy versus easy-to-hard.** The human DP idea says progress from easier to harder. In streaming agent memory, Evo-Memory found the reverse beat it (d16). Gain tracked task similarity (Pearson .717 on Gemini 2.5 Flash, .563 on Claude 3.7 Sonnet). So similarity, not order, is the supported driver.

## 5. What holds up

**Holds (established).**
- The raw practice-performance correlation is moderate. Across rival meta-analyses it spans .35-.43 with broad coding and .54-.61 with strict, corrected coding (K01, K04). It is never near 1 (b06).
- It varies by domain: games and music highest, professions near zero (K02). Post-corrigendum overall figure r=.38, 14% (K23).
- Recall reliability is measured only over short spans, and the full-career figure is a guess (K24).
- The 1993 gap between experts and clearly less accomplished players replicates (good vs less accomplished d=1.33, p=.005, a22).

**Failed or weakened.**
- Best vs good violinists: no difference in a double-blind replication, and the good group had slightly more hours (a22). Effect size was about half the original (eta2 .26 vs .48, b02).
- "Impossible to catch up" is contradicted: most best violinists had less solo practice than the good-group mean (b04).
- Teacher-designed practice added nothing over practice alone (a23).
- The twin finding that practice should reduce genetic influence failed on music discrimination: genetic variance stayed constant (a24).
- Elite athletes: practice explained about 1% (a18). Both camps agree range restriction lowers r. Nobody has corrected it (d04).

**Moderators.** Domain predictability (a13), skill level in sports (a18), performance measure (group membership r=.51 vs standardised score .28, a14), practice measure (a14), published vs unpublished in sports (a19). Not moderators in sports: team vs individual, open vs closed skill, age (a19).

**Why the camps disagree.** Three independent reasons. (1) Definition: Ericsson and Harwell kept 14 of 88 studies and exclude team practice and lectures (b09, b12). (2) Squaring: r vs r-squared (a16, a17). (3) Reliability: the corrected value runs from .42 to 1.00 with the assumption (b07). The coders on both sides have a stake (critique weak spots).

**Interventions that worked.**
- Simulation training with DP in medicine: effect size 0.71 across 14 studies (b21).
- AI tutor with immediate metric feedback in a randomised trial: large gain on the trained metric (a27).
- LLM hints to human tutors: +4 pp mastery (c16).

**Interventions that did not, or only partly.**
- Same AI tutor: blinded global rating not significant (a27).
- LLM patient simulator: dose too low (mean 2.5 cases per student), no gain for volunteers (a26).
- Early specialisation: the world-class path is broader (b20).

## 6. Language models

No LLM study tests the DP theory itself. The studies below test pieces of the loop. Everything is analogy. a25 (DPPO) has "Deliberate Practice" in its title only.

**6.1 Training-time loops.**

| Piece | Result | Id |
|---|---|---|
| Difficulty filtering (balanced pass-rate window) | Qwen2.5-7B on five math benchmarks; up to +10 on AIME in under half the steps; abstract says up to +12%. Skewed filtering (only easy or only hard) did worse than none | c02, c23 |
| SPEED-RL | 2x to 6x faster to target; per-benchmark about 3.0-3.5x; screening cost counted; total rollouts per prompt held fixed; same rule-based reward | c03, d06, d07 |
| DAPO dynamic sampling | 50 AIME 2024 vs 47 for R1-Zero-Qwen-32B at 50% of steps; naive GRPO 30. Share of dynamic sampling alone is only in a figure | c04 |
| Kimi k1.5 curriculum and prioritised sampling | Curriculum beat uniform in curves; no single number | c05 |
| Absolute Zero | Beats prior 7B zero-setting models by 1.8 points overall; math +10.9 (Base-7B), +15.2 (Coder-7B) after code-only training; pass@k kept at up to 512 in 4 of 5 cases | c01, c24 |
| R-Zero | Qwen3-4B-Base math 42.58 to 49.18 over 3 rounds (+6.49); gains shrink; some sub-scores fall at round 3 (MATH 79.8 to 78.0) | c06 |
| Self-Challenging agents | Over 2x for Llama-3.1-8B-Instruct on M3ToolEval and Tau-Bench; test-case filter matters | c07 |
| STaR | CommonsenseQA +35.9% over few-shot, +12.5% over direct fine-tune | c21 |
| DPPO (Pelican-VL) | +20.3% over Qwen2.5-VL-72B; MMStar forgetting 1.9 vs 5.0 SFT vs 24.8 RL; no non-deliberate hard-example baseline | a25 |
| Process supervision | Best-of-1860: PRM 78.2% vs ORM 72.4% vs majority 69.6%; 800,000 human step labels | c12 |
| Classic RL curricula | Teacher-Student CL, PAIRED, AlphaZero self-play. Pre-LLM. Per-task numbers not extracted | c09, c10, c11 |

Reading: the strongest and most repeated result is that learning signal peaks near pass rate 0.5. Five sources agree (K15). There is no matched mid-pass vs random-subset ablation in text, and the figures were not inspected. Gains diminish with self-generated labels (K16).

**6.2 Inference-time loops, no weight updates.**

| Method | Result | Id |
|---|---|---|
| Intrinsic self-correction | GPT-3.5 CommonsenseQA 75.8 to 38.1 after round 1 (41.8 after round 2); GPT-4 GSM8K 95.5 to 91.5 to 89.0; with oracle labels GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7, GPT-4 HotpotQA 49.0 to 59.0 | c13, c25 |
| Reflexion | AlfWorld +22% absolute in 12 steps; HumanEval Python 80 to 91; fell on MBPP Python 0.80 to 0.77 where test false-positive rate was 16.3% (1.4% on HumanEval) | c14, d10, d11 |
| Self-Refine | About 20% absolute average over 7 tasks; largest on subjective tasks; reasoning tasks without external feedback do not improve | c15 |
| EvoTest (J-TTL, 50 episodes, 6 games) | AUC: static 0.11/0.12, Reflexion 0.32/0.34, TextGrad 0.31/0.33, EvoTest 0.47/0.50. Plain repetition stays flat | d13, d14 |
| ExpeL | Insights vs retrieval alone: HotpotQA 36 vs 31, ALFWorld 50 vs 55. Both help. Order not ablated | d12 |
| Dynamic Cheatsheet | Claude 3.5 Sonnet AIME 2024: 23.3 baseline, 36.7 instructions only, 50.0 with memory (Cu). GPT-4o Game of 24: 10 to 99 (reused a Python brute force). GPT-4o MMLU-Pro Engineering 53.2 to 51.2. Small models: little or negative | d08, d09 |
| MaTTS / ReasoningBank (WebArena) | At equal k: with memory 49.7 to 55.1 (k=1 to 5); without memory 39.0-42.2 and unstable | d15 |
| Evo-Memory ordering | Hard-to-easy avg 0.81 vs easy-to-hard 0.77 for ReMem; ExpRAG 0.69 vs 0.57; base 0.41 | d16 |
| Decocted experience | Distilled lessons beat raw trajectories; intermediate memory size wins | d17 |
| Voyager (Minecraft) | Random curriculum: 93% fewer items; no self-verification: 73% fewer; GPT-3.5 for GPT-4: 5.7x fewer items | c08, c22 |

Reading.
- A real external signal is the gate. Without it, repeat attempts hurt (c13, c25, d11). With it, they help, to the extent the signal is accurate.
- Plain repetition does nothing. Update-between-attempts does (d13).
- Gain needs a capable model (d09, d14). Small models gain little or lose.
- Some of the headline gain is better instructions, not memory (d08: 13.3 of the 26.7 points on AIME 2024 for Claude came from memory over instructions-only).
- No paper matches tokens between a retry-and-rewrite loop and best-of-N (d10, d13). MaTTS matches rollouts k between memory and no-memory arms, which is the nearest thing (d15). This stays the key open gap.

**6.3 LLMs as practice partners and tutors for humans.**
- Tutor CoPilot, 900 tutors, mastery +4 pp (c16).
- Tutor trained by DPO against a simulated student: student-correctness prediction +33% over GPT-4o, but the outcome is simulated, not real learning (c17).
- MedSimAI pilot: 1,024 encounters, no gain for volunteers (a26).
- ChatGPT vs live coaching pilot: 25 trainees, both improved, no between-group effect in the abstract (b22).
- Conservatory study: AI practice app use at T1 to self-regulation at T2 beta=.47 to performance at T3 beta=.39, N=512, observational (b23).
- Fazlollahi: rule-based AI tutor beat instructor and control on its own metric (0.66) but not on blinded OSATS (a27).

## 7. What our agent should take

Honest summary: little. The agent does not practise across tasks, and DP itself carries no new inference-time element. What transfers is the evidence about the feedback gate and in-session retry loops. Most of that is already in the schema as G2, G3, G5, S4, S5.

Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| A revision or retry is triggered only by an external check, never the model's own judgement. Already stated; this adds numbers: intrinsic self-correction dropped GPT-3.5 CommonsenseQA 75.8 to 38.1 | G2 (already there) | [E] | c13, c25, c14, c15, d11; K18 |
| Rate the checker before trusting a retry loop: record the false-positive rate of any generated test. Reflexion went below base at 16.3% false positives | G3 / S4 note | [E] | d11; K27 |
| Do not quote 10,000 hours or "practice explains expertise" as support for any schema element | citation hygiene | [E] | a10, K01, K08 |

No new operator or state is established from this subfield.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Retry-and-rewrite against an external checker beats best-of-N at equal tokens | S5 / memory | [E] in token-unmatched form; equal-token form untested | d13, d14, d10; K26 |
| Memory (distilled lessons) beats no memory at the same number of samples, with an instructions-only control (part of "memory" gain is better instructions) | memory | [S] | d15, d17, d08; K28, K29 |
| Cap memory size and keep distilled lessons, not raw trajectories | memory | [S] | d12, d17 |
| Order of sub-goals: easy-first vs hard-first vs random | S6 / memory (subgoal library) | [C] | c08, c22, d16; K17 |
| Choose helper sub-problems by estimated mid-range solve rate | S6 / memory | [E] for RL training, no inference-time test | c02, c03, d06; K15 |
| Step-level self-check vs final-answer check as the selection signal | S4 / S7 | [S] | c12; K19 |
| Route by task predictability: spend loop budget only on stable, checkable tasks | S0 / G12 | [S] | a13, d08, d16; K03 |
| Noisy checker plus small model break-even | G3 / G7 | [E] qualitative, break-even unknown | d11, d09; K27 |

## 8. Concrete tests on our bench

All arms at equal total tokens, with setup and screening cost counted (G7). Report mean and an interval over at least 3 seeds. Items come from our existing bench, split into those with a code checker and those without.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Retry-and-rewrite vs best-of-N | ARC-style items with held-out check; BRAINTEASER items with a checker where available | (a) 4 independent attempts, code select; (b) attempt, located failure, one-line lesson, retry, same token budget; (c) plain single attempt with the same cap | Pass rate on the unfitted check; tokens per correct item | Small gain for (b) over (a) on items with a trusted check. No gain without one |
| T2 Checker quality sweep | Same items, checker made noisy by flipping 0, 5, 15, 30% of verdicts | Retry loop at each noise level vs best-of-N | Pass rate vs noise | Loop falls below best-of-N at roughly 15-20% noise (Reflexion MBPP) |
| T3 Memory vs instructions-only vs none | Streams of 30-60 items from the same class | (a) none; (b) instructions-only (rewritten prompt, no lessons); (c) one-line lessons shown after first attempt; (d) raw trajectories | Accuracy on stream items 20+; tokens | (c) above (b) by a few points on same-structure streams. (d) not better than (c). No gain on mixed-class streams |
| T4 Order of sub-goals | Decomposable items (O3) with 3-4 sub-goals | easy-first, hard-first, random, model-chosen | Pass rate | Ambiguous. Evo-Memory predicts hard-first not worse. Expect no large order effect |
| T5 Mid-rate helper selection | Impasse items where a helper problem is chosen | (a) helper with 0.3-0.7 estimated solve rate; (b) random helper; (c) easiest helper | Solve rate of the parent item, probe tokens counted | Mild gain for (a), eaten partly by probe cost |
| T6 Step vs final-answer check | Multi-step items | step-level check, final check, both | Pass rate at equal tokens; false-accept rate | Gain only if the step check is code-verifiable. A model-run step check expected to match the final check |
| T7 Predictability routing | Mixed bench: stable rule-bound vs open items | loop always on vs loop only on stable | Pass rate and tokens | Loop helps stable items, wastes tokens on open items |

## 9. What does not transfer, and why

- **Years of accumulated practice.** The agent has no between-task learning. The hours-to-expert curve has no counterpart.
- **The 4 h/day ceiling, sleep, rest** (a04, a05). Human fatigue limits only.
- **Heritability and talent** (a24, b16). Genes have no analogue for a fixed model. The nearest analogue is base-model strength, which gates all loops (d09, d14).
- **Effortful and unenjoyable.** Motivation is irrelevant to a model.
- **Recall reliability.** For an agent the log is exact, so the measurement problem that drives the human dispute disappears. Our agent logs everything (SCHEMA section 6).
- **Teacher-designed practice** (a23). In our setting the designer is code or a rule, and code is always the checker (G5).
- **Early-specialisation findings** (b20). No developmental trajectory.
- **Training-time curricula** (K15, K16). They change weights. Our agent is a scaffold, so only the form transfers.
- **Human tutoring results** (c16, a26, a27, b22, b23). They are about humans learning, not an agent thinking.

## 10. Open questions

1. Does retry-and-rewrite beat best-of-N at equal tokens? No paper matches tokens (d10, d13).
2. How much of the difficulty-filter gain comes from mid-pass selection versus extra rollouts or a verifier? Text says rollouts are fixed per prompt in SPEED-RL (d07), but there is no matched random-subset ablation in text, and DAPO's share is in a figure.
3. Does an inference-time self-built curriculum help? Only Voyager tests ordering with ablation (random curriculum, -93%), and Evo-Memory contradicts easy-first (d16).
4. What is the full-career reliability of recalled practice? Nobody has full-career diaries (d03).
5. Does range restriction explain the elite r=.11? No correction exists (d04).
6. Are there more independent replications of the 1993 violin study than Macnamara and Maitra (2019)? None found; the search was small.
7. Do LLM tutor gains survive blinded, non-optimised outcomes? Fazlollahi's blinded OSATS was not significant (a27).
8. Does step-level feedback beat outcome feedback outside math? Single source (c12).
9. Does task predictability moderate loop gains in agents, as in humans (a13)? Only indirect support: Dynamic Cheatsheet Game of 24, Evo-Memory similarity r=.717, and no gain on MMLU-Pro Engineering (d08, d16).
10. What is the exact 2014 corrigendum text? Paywalled. Overall r=.38 is taken from the authors' later citation (d01). The 2016 sports figure (.43 vs .45) is unreconciled (critique).

## 11. Sources

[V] = opened and read this session. [M] = snippet, abstract or metadata only.

- [V] Ericsson, Krampe, Tesch-Romer (1993), Psychological Review. https://graphics8.nytimes.com/images/blogs/freakonomics/pdf/DeliberatePractice(PsychologicalReview).pdf (a01-a10)
- [V] Macnamara, Hambrick, Oswald (2014) meta-analysis. https://www.psychologie.uzh.ch/dam/jcr:658d39fe-2f4b-467f-9ae2-ffeb25caf2b6/McNamara.PsychSci.25.2014.pdf (a11-a15)
- [M] Same, abstract. https://pubmed.ncbi.nlm.nih.gov/24986855/ (b05)
- [M] Macnamara, Hambrick, Oswald (2018) corrigendum, metadata only. https://doi.org/10.1177/0956797618769891 (d05)
- [V] Platz et al. (2014) music meta-analysis. https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00646/pdf (a16)
- [V] Hambrick et al. (2014) reply to Platz. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00751/pdf (a17)
- [M] Hambrick et al. (2014) Intelligence 45, paywalled. https://doi.org/10.1016/j.intell.2013.04.001 (a28)
- [V] Macnamara, Moreau, Hambrick (2016) sports meta-analysis. https://hhs.purdue.edu/skill-learning-and-performance-lab/wp-content/uploads/sites/43/2024/08/macnamara-et-al-2016-the-relationship-between-deliberate-practice-and-performance-in-sports-a-meta-analysis.pdf (a18, a19)
- [M] Same, abstract. https://pubmed.ncbi.nlm.nih.gov/27217246/ (b14)
- [M] Macnamara and Hambrick (2016) reply. https://pubmed.ncbi.nlm.nih.gov/27217248/ (b15)
- [V] Ericsson and Harwell (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6824411/ (a20, a21, b10-b13, d03)
- [V] Macnamara and Maitra (2019) replication. https://pmc.ncbi.nlm.nih.gov/articles/PMC6731745/ and https://europepmc.org/article/PMC/PMC6731745 (a22, a23, b01-b04)
- [V] Hambrick, Macnamara, Oswald (2020) / Macnamara and Hambrick (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7461852/ (b06-b09, b18, b19, b24, b25, d01, d02, d04)
- [V] Twin study (2024) heritability of musical expertise. https://pmc.ncbi.nlm.nih.gov/articles/PMC11433073/ (a24)
- [M] Mosing et al. (2014) twins. https://pubmed.ncbi.nlm.nih.gov/25079217/ (b16)
- [M] Meinz and Hambrick (2010). https://pubmed.ncbi.nlm.nih.gov/20534780/ (b17)
- [M] Macnamara, Moreau, Hambrick (2022) multidisciplinary practice. https://pubmed.ncbi.nlm.nih.gov/34260336/ (b20)
- [M] McGaghie et al. (2011). https://pubmed.ncbi.nlm.nih.gov/21512370/ (b21)
- [V] Zhang et al. (2025) DPPO, Pelican-VL. https://arxiv.org/abs/2511.16602 (a25)
- [V] Hicke et al. (2026) MedSimAI. https://arxiv.org/abs/2503.05793 (a26)
- [V] Fazlollahi et al. (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8864513/ (a27)
- [M] Philips et al. (2026) ChatGPT coaching pilot. https://pubmed.ncbi.nlm.nih.gov/42852079/ (b22)
- [V] Song (2026) conservatory AI practice. https://europepmc.org/article/PMC/PMC13619875 (b23)
- [V] Zhao et al. (2025) Absolute Zero. https://arxiv.org/abs/2505.03335 (c01, c24)
- [V] Bae et al. (2025) online difficulty filtering. https://arxiv.org/abs/2504.03380 (c02, c23)
- [V] Zhang et al. (2025) SPEED-RL. https://arxiv.org/abs/2506.09016 (c03, d06, d07)
- [V] Yu et al. (2025) DAPO. https://arxiv.org/abs/2503.14476 (c04)
- [V] Kimi Team (2025) k1.5. https://arxiv.org/abs/2501.12599 (c05)
- [V] Huang et al. (2025) R-Zero. https://arxiv.org/abs/2508.05004 (c06)
- [V] Zhou et al. (2025) Self-Challenging agents. https://arxiv.org/abs/2506.01716 (c07)
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 (c08, c22)
- [V] Matiisen et al. (2017). https://arxiv.org/abs/1707.00183 (c09)
- [V] Dennis et al. (2020) PAIRED. https://arxiv.org/abs/2012.02096 (c10)
- [V] Silver et al. (2017) AlphaZero. https://arxiv.org/abs/1712.01815 (c11)
- [V] Lightman et al. (2023). https://arxiv.org/abs/2305.20050 (c12)
- [V] Huang et al. (2024) cannot self-correct. https://arxiv.org/abs/2310.01798 (c13, c25)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c14, d10, d11)
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651 (c15)
- [V] Wang et al. (2024) Tutor CoPilot. https://arxiv.org/abs/2410.03017 (c16)
- [V] Scarlatos et al. (2025). https://arxiv.org/abs/2503.06424 (c17)
- [M] Bengio et al. (2009) curriculum learning, not opened. https://doi.org/10.1145/1553374.1553380 (c20)
- [M] Macnamara 2014 and Ericsson 1993 as listed from memory in c18, c19 (superseded by the opened versions above)
- [V] Zelikman et al. (2022) STaR. https://arxiv.org/abs/2203.14465 (c21)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (d08, d09)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (d12)
- [V] He et al. (2026) EvoTest. https://arxiv.org/abs/2510.13220 (d13, d14)
- [V] ReasoningBank and MaTTS (2025). https://arxiv.org/abs/2509.25140 (d15)
- [V] Evo-Memory (2025). https://arxiv.org/abs/2511.20857 (d16)
- [V] Decocted Experience (2026). https://arxiv.org/abs/2604.04373 (d17)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 9 established claims: 5 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A10.04-K02** (number corrected). The r values (games .51, music .46, sports .42, education .21, professions .05) are the original 2014 figures that the 2018 corrigendum superseded; post-corrigendum variance shares are games 24%, music 23%, sports 20%, education 5%, professions 1%, inconsistent with K01 which uses post-corrigendum values. Corrected claim: The size of the effect depends strongly on domain: after the 2018 corrigendum deliberate practice explains about 24% of variance in games, 23% in music, 20% in sports, 5% in education and 1% in professions (original 2014 values: r=.51, .46, .42, .21, .05).
- **A10.04-K04** (number corrected). Platz music r=.54 is observed (corrected .61) and Ericsson and Harwell's r=.54 is uncorrected (29% of variance; their corrected figure is 61% of variance, r about .78 under assumed reliabilities), so 'r=.54-.61 (corrected)' mislabels the figures; Macnamara and Hambrick also show the correction depends on assumed reliability, so not all disagreement is definitional. Corrected claim: The size of the effect depends on how deliberate practice is defined and corrected. Strict definitions (solitary or coached, no team practice or lectures) give r=.54 uncorrected (Ericsson and Harwell, 29% of variance; Platz music observed .54, corrected .61), and Ericsson and Harwell's attenuation correction raises this to 61% of variance (r about .78) only under assumed reliabilities (.6 practice, .8 performance) that Macnamara and Hambrick dispute; broad definitions give r about .35-.43. Part of the disagreement is definitional and part is the reliability correction.
- **A10.04-K24** (number corrected). Ericsson and Harwell 2019 report r=.54 (29% of variance), which after correcting for attenuation (practice reliability .6, performance .8) is 61% of variance (r about .78, Macnamara and Hambrick 2020 Table 3), not 'corrected r=.61'; also 'none cover full careers' is too strong because an unreferenced Ericsson (2013) lifetime reliability of .7-.8 is cited. Corrected claim: The corrected estimate of about 61% of variance (r about .78, from raw r=.54) depends on an assumed practice-recall reliability (0.6 in Ericsson and Harwell, 0.8 in Macnamara and Hambrick's re-correction); the direct data cited cover recent weeks or years (r .60-.75, de Bruin r(34)=.60; Ward 2007 found recall reliable only for about 5 years), and the lifetime-practice reliability of .7-.8 rests on an unreferenced statement rather than reported data.
- **A10.04-K27** (reworded: the sources support less). Reflexion MBPP Python 0.80 to 0.77 with 16.3% false-positive rate and Dynamic Cheatsheet small-model weakness confirmed, but EvoTest says a small Qwen3-8B evolver stays 'substantially above' the static baseline (Detective AUC 0.68 vs 0.21), so 'little gain with small models' is wrong for EvoTest. Corrected claim: In-session self-improvement is bounded by the signal and the model: Reflexion fell on MBPP Python (0.80 to 0.77) with a 16.3% false-positive test rate; Dynamic Cheatsheet gives little or inconsistent gain with small models (GPT-4o-mini, Claude 3.5 Haiku); EvoTest's gain shrinks with a weaker evolver (Detective AUC 0.94 with o3, 0.68 with Qwen3-8B) but stays well above the static 0.21.
- **A10.04-K08** (now single-source: only one opened source, code check).
- **A10.04-K23** (now single-source: only one opened source, code check).
