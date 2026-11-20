# Process stage models and incubation: deep document

*Subfield A09.07. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K26), critique.md in this folder. Evidence ids (a01..d19) point to those files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Human numbers are from small lab studies unless noted. No LLM study tests a deliberate human-style incubation step (K21); LLM evidence is by analogy.*

## 1. What it is

Process stage models say that creative problem solving moves through named phases in a fixed order. The best known is Wallas (1926): Preparation, Incubation, Illumination, Verification. Incubation is the stage after a failed hard effort, when the person stops working on the problem. Illumination is the sudden idea that may follow.

The claim that matters for us is narrow. Does stopping, doing something else, and coming back improve the chance of solving a problem that was not solved before? And if so, why? Ward and Smith and Blankenship say a main reason is forgetting a misleading clue or frame. Others say unconscious work, hidden conscious work, or rest from fatigue.

Short answer from the evidence (K01, K02, K06):
- The stage order is a description built from anecdotes, not a tested causal sequence.
- Lab incubation gives a small, noisy gain on average (d about 0.29 to 0.41).
- The "unconscious thought" version for choices is close to zero after bias correction.
- Sleep helps on some insight tasks and not on others.
- For LLMs, nothing tests a Wallas break directly. The nearest tests (sleep-time compute, "Wait", resampling, reflection) give a different lesson: extra sequential thinking is non-monotonic, parallel fresh attempts are strong, and retrying needs an outside signal.

For our schema this means: keep stage names as labels at most. Do not add an incubation stage. The useful part is a conditional "restart from the bare problem with a short lesson" operator at an impasse, which is already close to what S5/S6 do. It needs a test.

## 2. History and theories in depth

### 2.1 Helmholtz and Poincare, then Wallas (a01-a03, a32)
- Helmholtz (1891 banquet speech) gave three stages. He said ideas "come unexpectedly without effort" and never when his mind was fatigued.
- Poincare gave two worked mathematical cases: hard fruitless work, then a break (military service, a journey), then a sudden idea, then checking.
- Wallas (1926, The Art of Thought) took Helmholtz as the template and added Verification as the fourth stage. [a01, opened]
- Wallas split Incubation in two: spending the break on other problems, or relaxing from all conscious work. He thought the first saves time but hard creative work needs real relaxation. [a02]
- Example from the book: a preacher who posed his sermon problem on Monday got a better sermon than one posed late in the week, for the same hours of work. N=1, no control. Barristers delay each brief on purpose.
- Wallas added a sub-stage of Illumination, Intimation: a fringe feeling that the flash is coming. It is rarely tested. [a03, a32]
- Wallas says the stages overlap in the stream of thought. They are not a clean sequence.

### 2.2 Later stage models (a30)
- Csikszentmihalyi (1996) has five stages: preparation, incubation, insight, evaluation, elaboration.
- Geneplore (Finke et al. 1992) has two repeating phases: generate, then explore. It is the stage model closest to a loop.
- All of them rest on retrospective reports. None gives an effect size for the order.

### 2.3 Four rival explanations of incubation (a09, a32, b07, b11)
Gilhooly (2016) lists them:
1. **Intermittent conscious work.** The person keeps thinking about the problem in gaps. Seldom checked in the literature.
2. **Beneficial forgetting.** Misleading cues fade (Smith and Blankenship; Segal's "Fresh Look"; Ward). Predicts that incubation helps mostly after fixation. Vul and Pashler (2007) title states this boundary: incubation helps only after misdirection (a19, b17; not opened).
3. **Unconscious work.** Spreading activation or other processing continues off-line. Gilhooly's own divergent-thinking data favour it. Proponent view; weigh accordingly.
4. **Recovery from fatigue.** Selective fatigue relief. Ellwood et al. (2009) say it fits their data as well as unconscious work (a12).

A dual-process commentary adds: for insight (convergent) problems, escaping an impasse needs controlled processes (working memory, inhibition, switching), so incubation cannot be only unconscious. Unconscious work may fit divergent tasks better (b11).

### 2.4 Computational models (a28, a29, c25)
- Helie and Sun (2010): CLARION. Explicit rules and implicit associations run in parallel, are stored redundantly, and their outputs are integrated and iterated. Simulates incubation and insight data. Abstract only read.
- Gupta, Jang, Mednick and Huber (2012): semantic-space model of RAT items. The correct answer is found by the semantic model, while a frequency-biased model explains right and wrong responses. People do worse when pulled to high-frequency candidates. 48 RAT items under speed pressure. Abstract only.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Wallas stages derive from anecdotes | 4 stages; Helmholtz gave 3; no effect size in the book | Wallas 1926 (a01-a03) | [E] as a description of origin |
| Early vote-count review | 29 of 39 experiments found a significant incubation effect; Olton and Johnson (1976) null | Dodds, Ward and Smith 2003 via Ritter and Dijksterhuis 2014 (a08, b04) | [E] but vote counting |
| Incubation meta-analysis, size | 117 studies, 3,606 participants, median N 25; 85 of 117 effects positive; unweighted mean unbiased d = 0.41 (SD 0.71, CI 0.28 to 0.54), median 0.26; Gilhooly quotes about 0.29 | Sio and Ormerod 2009 (a04, a09, b07) | [E]; exact weighted d unverified (K26) |
| Publication bias test in that meta | standardized beta = .08, p = .41; weak test | Sio and Ormerod (a05) | [C] |
| Moderator: task type | Creative (divergent) effects larger than visual and linguistic insight; visual vs linguistic z = 1.25, n.s. | Sio and Ormerod (a06) | [S] |
| Moderator: preparation length | r = .40 visual (df 35, p=.02), r = .60 creative (df 14, p=.03), r = .04 linguistic (p=.75) | Sio and Ormerod (a06) | [S], correlational |
| Moderator: filler load | Low-demand filler beat rest on linguistic problems, beta = .54, p<.05; high-demand filler gave smaller effect | Sio and Ormerod (a07) | [S] |
| Break length is inverted U | 3 min beat 1 min and 5 min | Yang et al. 2012 via review (b06) | [S], not opened |
| Immediate vs delayed incubation | Immediate > delayed > control on alternate uses (direction only) | Gilhooly et al. 2012 (a13, b10) | [S] |
| Cross-domain filler | Spatial filler helped verbal divergent thinking more than verbal filler, and the reverse | Gilhooly et al. 2013 (a11) | [S]; fatigue account fits too (a12) |
| Unconscious thought advantage, meta | 61 effects (54 articles, 129 comparisons); random-effects g = 0.15 [0.03, 0.26]; 45 n.s., 12 favour distraction, 4 deliberation; funnel Z = 2.11, p = .04; trim-and-fill g = 0.018 [-0.10, 0.14] | Nieuwenstein et al. 2015 (a15, b02) | [E] near-zero after correction |
| UTA large replication | N = 399; 58.2% (deliberation) vs 61.9% (distraction), within-subject, n.s.; between-subject first-done 55.61% (n=196) vs 55.17% (n=203); BF 7.83 for null | Nieuwenstein et al. 2015 (a16, b01) | [E] null |
| Earlier UTA meta (proponents) | 92 decision studies, g = 0.224 (one source says d .218) | Strick et al. 2011 via Gilhooly (a14, b09) | superseded |
| UTA in medical decisions | 17 contrasts, z = 0.35, p = .73, I2 = 69.9%; experts d = -0.14, novices d = 0.24; expertise Q(1)=5.71, p=.017 | Medical-decision meta 2015 (b20) | [E] null |
| UTA selection effect | Idea generation equal after conscious and unconscious thought; choice of best idea better after unconscious thought | Ritter et al. 2012b (a18) | [S], proponent lab |
| Fixation then delay helps | Exp 1 N=146: incubation F(1,142)=22.86, p<.001, partial eta2 .139; context F(1,142)=6.18, p=.014; interaction F=1.31, p=.255; delayed-retest context d=.19 | Smith and Beda 2019 (a20) | [C] (interaction n.s.) |
| Smith and Beda replication | about 120 participants; interaction F(1,116)=2.89, p=.092; delayed context d=.222, immediate d=.033 | Smith and Beda 2019 Exp 2 (a21) | [C] |
| Mind wandering filler (original) | Undemanding 0-back raised creative uses on repeated problems only | Baird et al. 2012 (a22, b13) | [C], not opened |
| Mind wandering failed replications | Smeekens and Kane (3 expts), Steindorf et al., Murray et al.: no effect; 0-back accuracy .91 to .93 vs .87 in Baird; Du et al. 2025 N=85, 0-back .96, no divergent effect | a23, b12 | [C]; original is the outlier |
| Mindfulness and MW correlations | N=90 (30/29/31); r(27)=.40 p=.038 in one subgroup; N=28 tau=.28 p=.03; preregistered N=200 writing task: no difference across break types | a24, b14, b15 | [C] |
| Sleep, hidden rule | More than twice as many found the rule after 8 h sleep; about 60% vs 23% awake | Wagner et al. 2004 (a25, b06) | [E] with 3 sources |
| Sleep onset (N1) | N=103; N1 83.33% (20/24), wake 30.61% (15/49), N2 14.29% (2/14); Fisher p<.001 N1 vs wake and vs N2 | Lacaux et al. 2021 (a26) | [S] for N1 effect; sleep stage not randomized |
| Sleep helps only hard RAT items | Sleep group better on difficult items, no difference on easy | Sio, Monaghan, Ormerod 2013 (a27) | [S] |
| REM and TMR null results | REM study: 90-min break, N=111 first attempt, 25 solved; after break 10 of 84 non-solvers (11.9%); wake 20% (4/20), NREM 5% (1/20), REM 11.4% (5/44), p=.36. TMR: 56% and 58% vs 57%, no cue gain; Exp 1 sleep 62% vs wake 24% | b18, b19 | [C] |
| REM awakening | REM awakening gave 32% anagram advantage; REM naps about 40% better on RAT | Walker 2002, Cai 2009 via review (b06) | [S], not opened |
| Interactivity during break | Time 1: 43% with chains (12) vs 6% (2); Time 2 among failures: 44% (7/16) vs 15% (5/33), chi2(1, N=49)=4 | Interactivity study 2020 (b21) | [S] |
| LLM insight set | ChatGPT matched the most probable human score on 30 verbal insight problems (humans N=20); within top 5% of probable outcomes | Orru et al. 2023 (a31, b22) | [C]: small, contamination risk |
| LLM lateral thinking | BRAINTEASER 1,100 puzzles; ChatGPT sentence puzzles 60.8%, human about 91%; 53% and 63% on the two subtasks vs random 25% | Jiang et al. 2023 (c23, d09) | [E] models far below humans (2023 model) |
| LLM divergent thinking | GPT-4 above human mean; Hedges g about 0.5 to 2.6 vs average humans | Bellemare-Pepin 2024; Huang 2026 review (c22, b23) | [C] diversity, not incubation |
| Sleep-time compute | About 5x less test-time compute at equal accuracy; up to +13% and +18%; 2.5x lower cost per query when multi-query | Lin et al. 2025 (b24, c01-c03, d04) | [E] with conditions |
| Sleep-time compute limits | Gain widens with query predictability; at high test-time budget test-time-only slightly wins; o1 limited; SWE-Features about 1.5x fewer tokens at low budget only | Lin et al. 2025 (c02, c04, d01, d02, d05, d06) | [S] on the limits |
| "Wait" budget forcing | s1-32B AIME24 50.0% to 56.7%; ablation: no extrapolation 50.0 / 93.0 MATH500 / 57.6 GPQA; ignoring stop with no string 50.0 / 90.2 / 55.1; Wait best | Muennighoff et al. 2025 (c08, d18) | [E] |
| Longer thinking is non-monotonic | 82.2% to 87.3% (385 to 1,100 tokens), then 70.3% at 15,980; 1.5B model GSM8K at 16K: Wait and Think More -11.8%, parallel +10.1% | Ghosal et al. 2025 (c10, d08) | [E] |
| Parallel beats sequential at equal tokens | Up to 20% (abstract); up to 22% over Wait and Think More and about 47% over exact-budget control at 16K | Ghosal et al. 2025 (c11, d07) | [E] |
| Underthinking | Wrong AIME24 answers: 225% more tokens, 418% more thought switches; decoding penalty: QwQ 38.3 to 44.1, R1-Distill-32B 61.4 to 64.1, R1 73.8 to 74.8; prompt-only R1 72.4 (below baseline) | Wang et al. 2025 (c12, c13) | [S] |
| Inverse scaling | Longer reasoning lowers accuracy on distractor, spurious-feature, deduction tasks | Gema et al. 2025 (c14, d16) | [E] with Ghosal, Thoughtology |
| Distraction by misleading context | At most 18% of baseline-solved items stay solved under all irrelevant-context types; macro accuracy under 30%; instruction to ignore plus exemplars with distractors +35.5 points on 0-CoT | Shi et al. 2023 (c15, c16) | [E] |
| Rumination on early formulation | R1 ruminates on earlier formulations; sweet spot of thought length | Marjanovic et al. 2025 (d17) | [S] |
| Intrinsic self-correction fails | GPT-3.5 GSM8K 75.9 to 75.1 to 74.7; CommonSenseQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; keeps first answer 74.7%; with oracle labels GPT-4 GSM8K 95.5 to 97.5 | Huang et al. 2024 (c17, c18, d11, d12) | [E] |
| Reflexion | HumanEval pass@1 91% vs GPT-4 80%; AlfWorld +22% in 12 steps; HotPotQA +20%; reflection adds +8% over episodic memory; baselines at temp 0.7 solved none of their first-trial failures later; Rust without tests 52% vs 60% | Shinn et al. 2023 (c20, d13-d15) | [E] needs external signal |
| Tree of Thoughts | Game of 24: CoT 4%, ToT 74% (breadth 5), breadth 1 45% | Yao et al. 2023 (c21) | [E] |
| Reflection layer in agents | Believability TrueSkill: full 29.89, no reflection 26.88, none of memory, planning, reflection 21.21 | Park et al. 2023 (c19) | [S] |
| R1 "aha" | R1-Zero AIME24 pass@1 15.6% to 77.9% during RL; reflective words up 5 to 7 fold | DeepSeek-AI 2025 (c05) | [S] correlational report |
| Aha models | Aha models near zero language mixing and path repetition at difficulty 3-6; difficulty probe shifts across layers | Yang et al. 2025 (c06, c07) | [S] |
| Waiting task for AI image generation | N=60, F(3,56)=9.201, p<.001, eta2p=.330; task relevance F(1,56)=10.864; workload F(1,56)=9.612; interaction F(1,56)=7.126 | Front Psychol 2026 (b25) | [S] human-AI interaction, not an LLM test |

## 4. Mechanisms and models

Each mechanism is written so an engineer could build or test it.

### 4.1 Fixation and forgetting (Smith and Blankenship; Smith and Beda)
- Human model: a misleading cue is attached to a context. The problem is retrieved with that cue. Over time or in a new context, the cue weakens. The right answer becomes reachable.
- Machine analogue: the failed reasoning trace sits in the prompt and pulls the next tokens (Shi 2023: irrelevant or wrong context cuts accuracy to under 30% macro; Marjanovic: R1 ruminates on earlier formulations).
- Implementation of a "forgetting" step: on impasse, drop the failed trace. Restart with only (a) the problem statement and (b) a 1 to 2 line lesson written by the model and checked by code against the failing output. This matches Reflexion's finding that a short lesson beat the full last trajectory by 8% (d14).
- What it does not give: proof that forgetting is the cause. Smith and Beda's interaction test was not significant (a20, a21). In humans the effect is about d 0.2. K07 [C].

### 4.2 Pause then return (set aside, filler, return)
- Human protocol: work N minutes, impasse, filler task for T minutes, return. Gains need an unsolved selection; studies that drop people who did not meet an impasse are sounder (a24).
- Parameters that mattered: preparation length (r .40 to .60 for visual and creative), filler load (low beats high), break length (inverted U, 3 min best in one study), difficulty (sleep helped hard RAT only, a27).
- Machine version: abandon attempt, run an unrelated low-load generation, return with a fresh context. Nobody has measured it (K21). The honest analogue to test is "fresh-context restart" (4.1) with and without a filler, at equal tokens. The filler's role in an LLM is unclear, because a stateless model has no fatigue and no decaying memory. The only plausible effect is context change.

### 4.3 Sleep-time compute (offline consolidation)
- Pipeline: given context c, run a reasoning pass offline to produce a rewritten context c'. At question time, answer from c' with a small budget. [b24]
- Gain condition: the question must be predictable from c (accuracy gap widens over five predictability bins, d05). Amortise across several questions per context (2.5x cheaper per query, c03).
- Costs: offline tokens are extra spend. At high test-time budgets test-time-only slightly wins (d01); on agentic SWE-Features it only helped at low budget and lowered precision because the agent edited more files (d06).
- Engineering use: after a long session, write a notebook (facts, derived results, likely follow-ups). Do not run it for unpredictable one-off questions.

### 4.4 Budget forcing and "Wait"
- When the model emits end-of-thinking, append "Wait" and let it continue. [c08] s1-32B AIME24 50.0 to 56.7.
- Non-monotonic: the gain comes with rising output variance, not better reasoning (c10). At the same token budget, independent traces plus a majority vote beat Wait by up to 22% (d07). So continuation is a worse way to spend tokens than restarts, except at small budgets.
- Boundary: s1 authors think short correct traces were on track from the start and long ones backtrack (c09).

### 4.5 Underthinking and thought switching
- Wrong AIME traces switch ideas 418% more often (c12). A decoding penalty on switch tokens helped (QwQ 38.3 to 44.1). A prompt-only version did not.
- This is the opposite of fixation. The failure is leaving a promising line too early. Any "restart" operator must be gated so it does not feed this.

### 4.6 Self-correction needs an outside signal
- With oracle labels, correction gains are large (GPT-4 GSM8K to 97.5). Without them, accuracy falls (c17, d11).
- So a "return" step must be triggered by a test failure, not by the model's doubt (K24). Rust Reflexion without tests: 52% vs 60% (d15).

### 4.7 Structured search as mechanised restructuring
- Tree of Thoughts: Game of 24 74% vs 4% for CoT. Breadth 1 already gives 45% (c21), so most of the gain is search with evaluation, which matches S6/O1-O8.

### 4.8 Dual-system model (CLARION)
- Two modules: explicit rule-based, implicit associative. Both produce answers. An integration step combines them and iterates. Redundant storage across both. A pause lets the implicit side finish without explicit interference. (a28) This is a design reference only; our agent has no implicit module.

## 5. What holds up

### 5.1 Replicates
- A small positive average incubation effect in lab tasks. 85 of 117 studies positive, d about 0.29 to 0.41, with large heterogeneity. [E] (K02)
- Sleep helps hidden-rule discovery. Wagner (about 60% vs 23%), and a later sleep-vs-wake study (62% vs 24%, b19). [E] (K10)
- LLM facts that repeat across several labs: longer sequential thinking is non-monotonic (4 sources), intrinsic self-correction fails (2+ sources), parallel samples with voting are strong at equal tokens (Ghosal, s1 caveat, Lin Fig 5).

### 5.2 Failed or weak
- Unconscious thought advantage: after trim-and-fill g = 0.018. Large replication N=399 null, BF 7.83. Medical meta z=0.35. [E null] (K06)
- Mind wandering during the break helps: original is the outlier. Three or four later labs null (K08).
- REM sleep and TMR: no gain in a small REM study (p=.36) and a TMR study (56 to 58% vs 57%). [C] (K11)
- Smith and Beda: context effect small (d about .2); the interaction was not significant in both experiments. [C] (K07)
- Sio and Ormerod moderators are across-study correlations with small cells (14 creative, 16 rest studies).
- Median N 25 means most human incubation numbers are weak.

### 5.3 Moderators that show up repeatedly
- Impasse selection. Effects are larger or only appear in people who got stuck (a24; Vul and Pashler title; Smith). Studies without it dilute the effect.
- Problem difficulty. Sleep helped hard items, not easy ones (a27).
- Misleading cue present. A clue during incubation helps if useful and hurts if misleading (a08).
- Task type. Divergent > visual and linguistic insight (a06). Expertise reversed the predicted direction in medical decisions: experts d -0.14, novices 0.24 (b20).
- Interactivity. External chains beat pen and paper (b21). Externalising state aids insight.
- Predictability of the later question (LLM sleep-time, d05).
- Test-time budget (LLM). Offline compute helps at low budgets, test-time wins at high (d01, d06).

### 5.4 Interventions that worked
- In LLMs: Wait at moderate budgets (c08); parallel independent samples with a vote (d07); search with an evaluator (c21); verbal reflection with an external pass/fail signal (c20, d13-d14); decoding penalty on thought switches (c13); instruction to ignore irrelevant context plus distractor exemplars (c16); sleep-time precomputation for predictable queries (b24).
- In humans: low-demand filler over rest on linguistic problems (a07); N1 sleep onset (a26); interactive format (b21).

### 5.5 Interventions that did not
- In LLMs: intrinsic self-correction (c17); self-reflection with no tests (d15); prompt-only switch penalty (c13); extended sequential thinking to large budgets (c10); resampling from scratch on failures in Reflexion baselines at temperature 0.7 (d13).
- In humans: unconscious-thought distraction for choice (b01, b02); targeted memory reactivation (b19); mind-wandering induction (a23, b12).

## 6. Language models

What we know, grouped by what they test.

**No direct test.** No paper found tests a Wallas-style step, incubation break, or aha prompt on creativity or insight benchmarks (K21, c26). Search tools were rate-limited in the gap pass, so this is "not found", not "does not exist". Orru et al. 2023 cite Wallas but test no stage (a31).

**Insight and lateral-thinking performance.**
- ChatGPT matched the most probable human score on 30 verbal insight problems (humans N=20), but the human sample is small and puzzles may be in training data (a31).
- BRAINTEASER (1,100 puzzles): ChatGPT 60.8% on sentence puzzles vs human about 91%. It scored 53% and 63% on the two subtasks; random 25%. The gap widens when consistency across rewrites is required (c23, d09). SemEval-2024 had 483 team submissions (d10, no scores). These are 2023 numbers; no newer model result was opened.
- Divergent tasks: GPT-4 above the human mean (DAT), temperature 1.5 mean 85.6, higher than 72% of humans (c22). Reviews put g at 0.5 to 2.6 (b23). That measures diversity against average humans, not incubation.

**Offline compute (the closest to incubation).** Sleep-time compute: about 5x less test-time compute at equal accuracy, +13% and +18% more with scaling, 2.5x cheaper per query across multiple queries. Frontier shift is significant for o3-mini, R1 and Claude 3.7 Sonnet, limited for o1 (d02). It beats pass@k at equal test-time tokens on Stateful GSM-Symbolic (d03). Limits: only for predictable queries; test-time-only wins at high budget; on SWE tasks about 1.5x fewer tokens at low budget only.

**Continuation vs restart.** Wait: +6.7 points on AIME24 for s1-32B. At 16K tokens, independent restarts with voting beat Wait by up to 22%. Longer sequential traces fall to 70.3% from an 87.3% peak (c10). Inverse scaling in distractor tasks (c14).

**Fixation analogues.** Irrelevant context drops accuracy sharply (c15). R1 ruminates on earlier formulations (d17). Nobody tested whether a context reset reverses it (K25).

**Self-review and reflection.** Intrinsic self-correction lowers accuracy (GPT-4 GSM8K 95.5 to 89.0). With oracle labels it rises to 97.5. Reflexion's lesson beats episodic replay by +8%. Without tests it falls (52% vs 60%).

**R1 "aha".** Reflective words rise 5 to 7 fold during RL while pass@1 goes 15.6% to 77.9% (c05). This is a correlation, not an incubation test. Yang et al. found aha models adjust stated uncertainty to difficulty (c06).

**Human-AI interaction.** A 2026 study of design students waiting for AI images found waiting-task relevance and workload both mattered (b25). It is about humans.

## 7. What our agent should take

### Add now (established)
1. **Do not add an incubation or "sleep on it" stage.** The UTA result is null after correction; mind-wandering is null; stage order is anecdote. Schema part: confirms section 4b. [E] K01, K06, K08. Evidence a01, a15, a16, b01, b02, b20, a23, b12.
2. **Keep stage names as labels only.** Wallas's four stages map loosely to S1-S3 (preparation), S6 (impasse), S3 re-entry (illumination), S7-S8 (verification). No causal weight. Schema part: S labels. [E] K01. a01-a03.
3. **Any retry needs an external failure signal.** Intrinsic doubt does not work; test failure or a code-located error does. Schema part: G1, G2, G3. [E] K18, K24. c17, c18, d11, d12, d15.
4. **Prefer parallel fresh attempts over extending one trace.** Schema part: G11, S3. [E] K16. c10, c11, d07, d08. Keep per-mode token caps.
5. **If "Wait" or a re-examine nudge is used, use it only inside a small budget and only after a failing check.** Schema part: O, G1. [E] K15, K16. c08, c10.
6. **Search with an evaluator beats a single chain.** Schema part: O (idea tree at S6). [E] K19. c21, c20.
7. **Guard against irrelevant or misleading context.** Move suggestive material out; tell the model to ignore irrelevant information; use exemplars with distractors. Schema part: S1 input hygiene. [E]. c15, c16.
8. **Offline precompute only when the next question is predictable and the test-time budget is small.** Schema part: memory. [E] with conditions: K13, K22. b24, d01, d05, d06. Offline tokens are extra, so superiority at equal total tokens is not shown.

### Test first
| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Restart on a failed item from the bare problem plus a 1 to 2 line lesson, instead of continuing in context | O: restart with distilled lesson; G: fixation reset | [C] K07, K23, K25 | a20, a21, d13, d14, d16, d17 |
| Unrelated filler between attempts (incubation in the narrow sense) | O: pause step | [S] K04, K21 | a07, c26 |
| Immediate pause: plan or a different task before the first attempt | S0 or early O | [S] K05 | a13, b10 |
| Preparation budget before the pause (1k vs 4k tokens) | O: budget | [S] K03 | a06 |
| Offline notebook rewrite between sessions | memory | [E] K13 but unequal tokens | b24, d01-d06 |
| Switch penalty or "stay on line" rule | G: stay on a line of attack | [S] K17 | c12, c13 |
| Editable scratchpad on insight puzzles | memory | [S] K12 | b21 |
| Wait vs restart on lateral-thinking items (BRAINTEASER) | O: re-examine | [C] K23 | d07, d08, d09 |
| Retry trigger: test failure vs self-doubt (check on our own code) | G: external verification | [E] K24 | d11, d15 |

## 8. Concrete tests on our bench

All arms use equal total tokens (include any offline and filler tokens). Run on items the plain model failed once (stuck set) and on a random set to catch harm.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | BRAINTEASER sentence and word puzzles; ARC items failed on first pass | (a) continue in place; (b) fresh resample; (c) fresh start with problem only plus 2-line lesson; (d) Wait continuation | Solve rate on first-failed items; net fixes minus new breaks | (c) >= (b) > (a); (d) below (b) at same tokens (K23) |
| T2 | Same stuck set | Fresh restart with unrelated filler (a 300-token unrelated generation) vs fresh restart with no filler | Solve rate | No gain from filler (expected null; a stateless model has no mechanism for it) |
| T3 | Items with a planted misleading hint (GSM-IC style) | Continue in context vs drop failed trace and restart | Accuracy on stuck items | Restart recovers part of the loss (human analogue d about .2; may be larger for LLMs) |
| T4 | Multi-turn contexts with 3 to 5 follow-up questions each | No offline pass vs sleep-time notebook vs same tokens at test time; split by predictability bin | Accuracy per bin | Offline wins on predictable bins at small test budget; ties or loses on unpredictable bins |
| T5 | AIME-style math or hard coding | Sequential Wait to N tokens vs best-of-k with vote, same tokens | Accuracy | Parallel better, up to 10 to 20 points |
| T6 | Failed items with tests | Retry triggered by test failure vs by self-reported doubt | Net fixes minus new breaks | Test-triggered wins; self-doubt triggers break right answers |
| T7 | Insight puzzles | Pre-attempt pause (plan on a different problem first) vs none | Solve rate | Small or null; the human immediate-incubation effect is single-source |
| T8 | Long chain-of-thought failures | Switch penalty at decode vs prompt-only vs none | Pass@1; count of line changes | Decode-level helps by 1 to 6 points; prompt-only does not |
| T9 | Insight puzzles | Editable scratchpad vs none | Solve rate | Gain if the human interactivity effect is real |

## 9. What does not transfer, and why

- **Fatigue recovery.** A model has no fatigue. A rest or filler cannot repair it. Any gain from a pause must come from context change, not rest.
- **Forgetting by time.** Humans forget a misleading cue over minutes. A model's context is exact. We must delete the trace; time does nothing.
- **Unconscious processing.** A transformer pass has no background process between tokens. The only "offline work" is extra generated tokens (sleep-time compute), which cost money.
- **Mind wandering.** It has no machine counterpart and the human effect failed to replicate.
- **Impasse as a felt state.** In humans it is a self-reported selection step. In LLMs "impasse" is undefined; only an external test gives it meaning (K24).
- **Sleep stages.** REM, N1, N2 and TMR have no analogue, and the human sleep effects are task-specific and partly null.
- **Illumination (the sudden flash).** Illumination is a human report. LLM "aha" words correlate with RL training but are not proof of insight (c05).
- **Stage order as a sequence.** Our states branch and loop under code control. Fixing a stage order has no evidence-based gain (K01).
- **Human effect sizes.** d about 0.2 to 0.4 on tiny samples is a prior only. Do not size an LLM gain from it.

## 10. Open questions

1. Does "restart with problem plus lesson" beat fresh resampling on failed items at equal tokens, and does an unrelated filler add anything? (K21, K23)
2. How much of the human effect is forgetting a misleading context, and does a context reset reproduce it in LLMs? (K07, K25)
3. Where is the crossover between sleep-time and test-time compute on agentic tasks, with equal total tokens including offline? (K13, K14, K22)
4. Does Wait beat restarts on insight and lateral-thinking items, not just math? (K23)
5. What is the exact weighted vs unweighted mean d of Sio and Ormerod, and which moderators hold? (K26)
6. Are there 2024 to 2026 LLM papers that test incubation, aha, or Wallas prompts on creativity benchmarks? Not found under a blocked search budget (K21).
7. Is there any LLM analogue of immediate incubation (planning before reading) with a measured effect?
8. Does the N1 sleep-onset effect replicate independently, and is there a cheap partial-consolidation analogue?
9. How can an agent detect impasse cheaply without an oracle? (K24)
10. Is Smith and Beda's effect replicable outside Smith's lab, preregistered?
11. Do newer reasoning models still fail BRAINTEASER at the same gap?

## 11. Sources

[V] opened, [M] snippet or secondary only.

- [V] Wallas (1926) The Art of Thought. https://archive.org/details/artofthought0000grah (a01-a03)
- [V] Sio and Ormerod (2009) Does incubation enhance problem solving? Psychol Bull 135, 94-120. https://www.gwern.net/doc/psychology/writing/2009-sio.pdf (a04-a07). Weighted d unverified; [M] http://psycnet.apa.org/journals/bul/135/1/94.pdf and https://api.crossref.org/works/10.1037/a0014212 (b08, d19)
- [V] Gilhooly (2016) Incubation and intuition in creative problem solving. Front Psychol. https://pmc.ncbi.nlm.nih.gov/articles/PMC4956660/ (a09, a32, b07)
- [V] Ritter and Dijksterhuis (2014) Creativity, the unconscious foundations of the incubation period. https://pmc.ncbi.nlm.nih.gov/articles/PMC3990058/ and https://www.frontiersin.org/articles/10.3389/fnhum.2014.00215/full (a08, a18, b04)
- [V] Commentary on Gilhooly (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC5110525/ (b11)
- [V] Nieuwenstein et al. (2015) unconscious thought meta-analysis and replication. https://doi.org/10.1017/s1930297500003144 and https://jbaron.org/journal/14/14321/jdm14321.pdf (a15, a16, b01-b03). Critique could not reopen the numbers; three lines agree.
- [V] Medical-decision unconscious thought meta-analysis (2015). https://pmc.ncbi.nlm.nih.gov/articles/PMC4436803/ (b20)
- [V] Smith and Beda (2019) JEP General. https://people.tamu.edu/~stevesmith/SmithBeda2019.pdf (a20, a21)
- [V] Mind wandering, mindfulness and incubation (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9053813/ (a23, a24)
- [V] Du, Gordon, Tolmie (2025) mind wandering during incubation. https://pmc.ncbi.nlm.nih.gov/articles/PMC12190454/ (b12)
- [V] Mind wandering and creative incubation (2017) Sci Rep. https://pmc.ncbi.nlm.nih.gov/articles/PMC5578971/ (b14)
- [V] Mind wandering in a writing task (2025) Sci Rep. https://pmc.ncbi.nlm.nih.gov/articles/PMC12241419/ (b15)
- [V] Lacaux et al. (2021) Sleep onset is a creative sweet spot. https://pmc.ncbi.nlm.nih.gov/articles/PMC8654287/ (a26)
- [V] REM sleep and restructuring (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13542217/ (b18)
- [V] Sleep and targeted memory reactivation (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC7965947/ (b19)
- [V] Incubation and interactivity (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC6994426/ (b21)
- [V] EEG alpha in creative ideation (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4026701/ (a30)
- [V] Orru et al. (2023) ChatGPT insight problems. https://pmc.ncbi.nlm.nih.gov/articles/PMC10244637/ (a31, b22)
- [V] Huang, Liu, Yang (2026) LLMs in creative thinking review. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608707/ (b23)
- [V] AIGC waiting period (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13696403/ (b25)
- [V] Lin et al. (2025) Sleep-time compute. https://arxiv.org/abs/2504.13171 and https://arxiv.org/pdf/2504.13171 (b24, c01-c04, d01-d06)
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948 (c05)
- [V] Yang et al. (2025) Understanding aha moments. https://arxiv.org/abs/2504.02956 (c06, c07)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393 (c08, c09, d18)
- [V] Ghosal et al. (2025) Does thinking more always help? https://arxiv.org/abs/2506.04210 and https://arxiv.org/pdf/2506.04210 (c10, c11, d07, d08)
- [V] Wang et al. (2025) Underthinking of o1-like LLMs. https://arxiv.org/abs/2501.18585 (c12, c13)
- [V] Gema et al. (2025) Inverse scaling in test-time compute. https://arxiv.org/abs/2507.14417 (c14, d16)
- [V] Shi et al. (2023) LLMs easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 (c15, c16)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 and https://arxiv.org/pdf/2310.01798 (c17, c18, d11, d12)
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (c19)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 and https://arxiv.org/pdf/2303.11366 (c20, d13-d15)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c21)
- [V] Bellemare-Pepin et al. (2024) Divergent creativity. https://arxiv.org/abs/2405.13012 (c22)
- [V] Jiang et al. (2023) BRAINTEASER. https://arxiv.org/abs/2310.05057 and https://arxiv.org/pdf/2310.05057 (c23, d09)
- [V] Jiang et al. (2024) SemEval-2024 Task 9 (abstract). https://arxiv.org/abs/2404.16068 (d10)
- [V] Marjanovic et al. (2025) Thoughtology. https://arxiv.org/abs/2504.07128 (d17, abstract)
- [V] Ellis et al. (2020) DreamCoder. https://arxiv.org/abs/2006.08381 (c24)
- [M] Segal (2004) Fresh Look, via Gilhooly. https://pmc.ncbi.nlm.nih.gov/articles/PMC4956660/ (a10)
- [M] Gilhooly et al. (2012, 2013, 2015); Ellwood et al. (2009); Dijksterhuis and Meurs (2006), all via Gilhooly 2016 (a11-a13, a17, b10)
- [M] Strick et al. (2011) UTA meta, via Gilhooly. https://pmc.ncbi.nlm.nih.gov/articles/PMC4956660/ (a14, b09)
- [M] Smith and Blankenship (1989, 1991). https://link.springer.com/article/10.3758/BF03334612 (a19)
- [M] Baird et al. (2012) Inspired by distraction, via reviews (a22, b13)
- [M] Wagner et al. (2004) Sleep inspires insight. https://pubmed.ncbi.nlm.nih.gov/14737168/ (a25; abstract re-confirmed in critique)
- [M] Sio, Monaghan, Ormerod (2013). https://pubmed.ncbi.nlm.nih.gov/23055117/ (a27)
- [M] Helie and Sun (2010) CLARION. https://pubmed.ncbi.nlm.nih.gov/20658861/ and https://doi.org/10.1037/a0019532 (a28, c25)
- [M] Gupta, Jang, Mednick, Huber (2012). https://pubmed.ncbi.nlm.nih.gov/22344387/ (a29)
- [M] Olton and Johnson 1976; Zhong 2008; Ashby 2011; Pachur and Forrer 2013; Yang 2012; Barrett 1993; Walker 2002; Cai 2009; Sio 2012, via Ritter and Dijksterhuis (b05, b06)
- [M] Chandolia et al. (2026) aha moments. https://pmc.ncbi.nlm.nih.gov/articles/PMC13514830/ (b16)
- [M] Vul and Pashler (2007), title only. https://europepmc.org/ (b17)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 9 established claims: 8 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A09.07-K01** (reworded: the sources support less). Wallas text (Art of Thought 1926, Helmholtz and Poincare as worked cases, Intimation, four stages) confirmed, but 'no effect size supports the stage order as a causal sequence' is an absence claim no opened source tests (the EEG paper only lists stage models). Corrected claim: Wallas's four stages (preparation, incubation, illumination, verification) were derived from introspective anecdotes (Helmholtz, Poincare), not experiments; the sources checked report no experimental test of the stage order as a causal sequence.
- **A09.07-K13** (now single-source: only one opened source, code check).
