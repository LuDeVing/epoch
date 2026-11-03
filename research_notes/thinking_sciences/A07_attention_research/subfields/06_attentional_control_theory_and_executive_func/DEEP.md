# Attentional control theory and executive functions: deep document

*Subfield A07.06. Built from evidence_a-d.jsonl (ids a01-a26, b01-b25, c01-c28, d01-d21), claims.jsonl (K01-K31) and critique.md in this folder. Numbers were re-checked in the critique pass where noted. Where a number is only from an abstract, that is said. Claim ids are written Knn (A07.06-Knn); evidence ids are the short ids.*

## 1. What it is

Executive functions are the control processes that keep behaviour on a goal when habit or the environment pulls elsewhere. Three have been studied most (Miyake 2000):

- **Inhibition**: stop a dominant response or ignore a distractor (Stroop, flanker, stop-signal, antisaccade).
- **Shifting**: move from one task set to another (task switching, Wisconsin Card Sort).
- **Updating**: keep working memory current and replace old contents (n-back, keep-track).

**Attentional control theory (ACT; Eysenck, Derakshan, Santos & Calvo 2007)** says anxiety weakens the goal-directed attention system and strengthens the stimulus-driven one. The cost falls on inhibition and shifting. Anxious people can protect accuracy with extra effort, so the first loss is in efficiency (time, effort), not accuracy. Updating was added later (Eysenck and Derakshan 2011).

Why it matters for our agent. Four ideas map onto the schema:

1. **Switching cost has two sources** (Kiesel 2010): setting up the new task (control) and carry-over from the old task set (interference). For an LLM, carry-over is the old context. A fresh context removes it. This is the basis for S6 resets and S3 fresh contexts.
2. **Irrelevant material in context costs accuracy** (the flanker and Stroop analogue). Code should strip it, not ask the model to ignore it.
3. **Old values in context interfere with new ones** (proactive interference). Remove stale text.
4. **Emotional or pressure wording may shift behaviour** (the ACT analogue). Keep scaffold text neutral until tested.

Cautions that run through the document. Human executive-function tasks measure individual differences poorly. ACT has no large preregistered replication. The LLM studies are mostly one paper per claim. Treat most of this as a source of hypotheses for A/B tests, not rules.

## 2. History and theories in depth

### 2.1 Stroop (1935)
Paper cards and serial naming, not trial-by-trial reaction time (a01, a02).

- Exp 2, N=100: naming ink colour of conflicting colour words took 110.3 s per 100 items, against 63.3 s for plain colour squares. That is +47 s, +74%.
- Exp 1, N=70: reading words in conflicting ink was only 2.3 s slower per 100 (5.6%), not reliable.
- The effect is one-way. The stronger habit (reading) intrudes on the weaker task (naming).
- Exp 3 (practice, N=32 recruited, 2 dropped): eight days of practice cut conflicting-word time by 16.8 s (33.9%), against 4.0 s (13.9%) for plain colour naming. Interference did not vanish. The reading test with conflicting ink got slower.

Practice on one conflict trains a specific skill with costs elsewhere.

### 2.2 Connectionist and control accounts (background; not opened, c24-c28)
- **Cohen, Dunbar & McClelland (1990)**: parallel-distributed model. Word reading is a stronger pathway than colour naming. A task-demand unit boosts the weak pathway. It reproduces the one-way asymmetry. Control means adding activation to the goal route, not suppressing the distractor.
- **Botvinick et al. (2001)**: conflict monitoring. Detect response conflict, raise control on the next trial (conflict adaptation, Gratton effect). Later work questions it when repetition priming is controlled.
- **Gilbert & Shallice (2002)**: task-set inertia. The old set lingers after a switch, so a cost remains even with preparation.
- **Norman & Shallice (1986)**: a supervisory system takes over from routine contention scheduling when routine action fails or the situation is novel. Same shape as the schema: routine pass first, operators at impasse.
- **Meyer & Kieras (1997), EPIC**: executive processes as explicit production rules. An executive written as code rules is an old, working design.

### 2.3 Miyake et al. (2000): unity and diversity
- Nine tasks, three each for inhibition, updating, shifting. A three-correlated-factor model beat one-factor and three-uncorrelated-factor models (a03, b01).
- Raw correlations among the nine tasks: -.05 to .34. Latent correlations among the three functions: .42 to .63.
- N=137 college students. WCST related most to Shifting, Tower of Hanoi to Inhibition, random number generation to Inhibition plus Updating, operation span to Updating. Dual-task performance was unrelated to all three.
- a03 and b02 reached the 2000 paper through the 2017 review; b01 is the abstract.

### 2.4 Friedman & Miyake (2017): the revised model
- A **Common EF** factor (goal maintenance, top-down bias) explains all nine tasks, plus **Updating-Specific** and **Shifting-Specific** factors.
- In several datasets **no Inhibiting-Specific factor** could be extracted: Common EF absorbed all inhibition-task correlation (a04, b02).
- Correlation with IQ: Common EF .51, Updating-Specific .49, Shifting-Specific -.24. Common EF shares about 25% of variance with g.
- Twin work (2011 reanalysis): heritability Common EF 96%, Updating-Specific 100%, Shifting-Specific 79% (21% environment). Stability age 17 to 23: .86, 1.0, .91 (a05). The authors say heritability does not mean untrainable. The largest EF GWAS (17,027 to 28,243 per measure) found no genome-wide hits.
- Shifting-Specific is the only factor with real environmental variance. It trades off with Common EF in toddlers (b22).
- Single tasks are impure: each mixes executive and non-executive demands (a06).

### 2.5 The inhibition debate
- **Rey-Mermet, Gade & Oberauer (2018)**: eleven inhibition tasks, good single-task reliability, weak inter-correlation. Two weak factors: prepotent-response inhibition and distractor resistance. Older adults worse at response inhibition, better at distractor resistance (a16, b07; abstracts only).
- **Hedge et al. (2018)**, after disattenuation: SSRT with go/no-go commission .90, SSRT with flanker -.31, Stroop with flanker .25 (a14).
- **2025 two-study paper (JEP:LMC; authors not recorded, b08)**: stop-style response inhibition is a separate factor once go/no-go or SART commission measures are included. Study 1 N=154 exploratory, Study 2 N=279 confirmatory. Two-factor CFI .947, RMSEA .022; one-factor CFI .650, RMSEA .057; delta BIC -32.6; factor r=-.08. Not preregistered; digit span split-half .35; flanker loaded on nothing.
- Net: "inhibition" as one trait is not supported. Stop-type and filter-type failures look different. Theory is unsettled.

### 2.6 ACT and its extensions
- **ACT (2007)**: theory paper, no single effect size (a07, b03). Predictions: anxiety hurts inhibition and shifting; efficiency suffers more than effectiveness; compensatory effort hides the deficit.
- **Berggren & Derakshan (2013)** (a17, abstract only): deficits show on efficiency and under load, and can be absent when compensatory effort is available. Neural findings conflict; ACT reads this as effort differences.
- **Englert & Bertrams (2015)** (a08): momentary self-control strength decides whether anxious people compensate. Leans on ego-depletion literature, which has replication trouble. Weak evidence.
- **Eysenck, Moser, Derakshan, Hepsomali & Allen (2023)** (d19, abstract only): the authors' neurocognitive update (fronto-parietal, cingulo-opercular, default-mode networks). No new large replication.
- **Worry versus arousal**: Gustavson et al. (2020) found worry, not anxiety symptoms, depression or rumination, goes with weak Common EF (b09). The harmful ingredient may be worry content.

### 2.7 Task-switching reviews and switch-rate models
- **Kiesel et al. (2010)** (a18, abstract only): switch costs come from control and interference. Evidence: asymmetrical switch costs, n-2 repetition costs.
- **Xu, Verguts & Braem (2026)** (b19, d21): fast trial-to-trial control state plus slow learned control settings. High-switch training lowers switch cost. Control is context specific.

## 3. Core findings with exact numbers

Status: established = two or more independent sources; single-source; contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Stroop interference (human) | Exp 2 N=100: 110.3 s vs 63.3 s per 100, +47 s (+74%). Reading with conflicting ink +2.3 s (5.6%), not reliable (Exp 1, N=70) | Stroop 1935 (a01) | established |
| Stroop practice is specific | 8 days: conflict time -16.8 s (33.9%); plain naming -4.0 s (13.9%); N=32 | Stroop 1935 Exp 3 (a02) | established (K10) |
| Control is separable but related | Task r -.05 to .34; latent r .42 to .63; N=137 | Miyake 2000 (a03, b01) | established (K01) |
| Common EF plus Updating- and Shifting-Specific; no Inhibition-Specific factor | Common EF r=.51 with IQ, ~25% shared with g; Updating-Specific .49; Shifting-Specific -.24 | Friedman & Miyake 2017 (a04) | established (K01) |
| Common EF highly heritable and stable | 96% / 100% / 79%; stability .86 / 1.0 / .91 | Friedman & Miyake 2017 (a05) | single-source (one review) |
| Conflict difference scores unreliable | Test-retest ICC flanker RT cost .40 / .57; Stroop .60 / .66; Stroop error cost .48 / .44; SSRT .36-.49; range 0 to .82; N 40-62, 3 weeks apart | Hedge 2018 (a13, b06) | single-source (K03); ICC table not re-opened in critique |
| Commission errors steadier | go/no-go commission ICC .76 / .76; omission .69 / .42 | Hedge 2018 (b24) | single-source (K04) |
| Inhibition tasks barely correlate | Flanker vs Stroop RT cost r=.14 (.25 disattenuated); SSRT vs go/no-go .52 (.90 disattenuated) | Hedge 2018 (b06, a14) | established (K02) |
| Stop-type inhibition separate from Common EF | Two-factor CFI .947 vs .650; factor r=-.08; N=154, 279 | 2025 JEP:LMC (b08) | single-source; contested vs Friedman & Miyake |
| Anxiety lowers attentional control | g=-0.58, k=58, N=8292; efficiency not effectiveness; inhibition and shifting not updating; stronger under high load | Shi, Sharpe & Abbott 2019 (a09, b04, d16) | single-source (K05); abstract only |
| Anxiety lowers working-memory capacity | g=-.334, 177 samples, N=22,061; complex -.342 (k=30, N=3,196); simple -.318 (k=127, N=17,547); dynamic -.437 (k=20, N=1,318); I2 67.2%; without 20 outliers -.31 (k=157, CI -.36 to -.26) | Moran 2016 (a10, b05, d17) | single-source (K06) |
| Worry hurts more than arousal | Worry -.45 (k=11) vs arousal -.33 (k=43); trait -.24 (k=25); state -.21 (k=11); clinical -.37 vs non-clinical -.25 | Moran supplement (a10, a11) | contested (K07) |
| Worry predicts weak Common EF | Worry beta=-.43 (CI -.68 to -.17); anxiety r=-.07, depression -.14, rumination -.01; N=192 | Gustavson 2020 (b09) | single-source |
| Updating under anxiety conflicts | Shi: no updating deficit. Moran: dynamic span largest (-.437; supplement lists -.29) | Shi 2019; Moran 2016 | contested (K08) |
| Null ACT test | N=71; STAI-T delta R2=.003, BF01=1.56; BDI-II delta R2=.001, BF01=1.81 | Frontiers 2020 (b10) | single-source |
| CO2 anxiety left goal-directed control unchanged | N=88, 50, 1413 | Gillan 2021 (d18) | single-source; boundary case |
| Anxious people re-learn a flipped context rule poorly | CSPC low anxiety 30 ms, high -4 ms; t(52)=-3.03, p=.004, d=-0.83; N=54. Exp 2 N=74, d=0.55 | Bukowski 2026 (b11) | single-source; exploratory |
| Switch cost shrinks in frequent-switch contexts | LSTM 90% vs 10% switch rate: F(1,99)=77.39; F(1,198)=1791.59. Human reanalysis N=102: -36.39 vs -8.11 ms, F=8.77, p=.004 | Xu, Verguts & Braem 2026 (b19) | contested (K23) |
| Environment-specific flexibility needs days | 1 day N=52 no effect; 4 days N=51 effect | OSF preprint 2022 (d21) | single-source (K31) |
| WM training does not transfer | N=40 (21/19), 10 sessions; test anxiety F(1,38)=5.15, p=.03; attentional control p=.26; post-test group p=.22; n-back d=1.65 vs control 1.07 | BMC Psychol 2024 (b12) | established with Stroop (K10) |
| LLM: one irrelevant sentence cuts accuracy | GSM-IC-4K: at most 18% of base problems solved consistently across all distractor types; macro accuracy under 30%; role-overlap drives text-davinci-003 macro to 0 on >2-step problems | Shi 2023 (a25, c01, c02) | established (K11) |
| LLM: near-miss clause hurts later models | Up to 65% drop (abstract) | GSM-Symbolic (d10) | single-source, abstract only |
| LLM: ghost context | Strict rate 38.3% (temporal contradictions); masking top distractor fixes 95.5% (Fix@1), 2.4% collateral; 272 cases, 3 models | Namboothiri 2026 (d09) | single-source, abstract only |
| LLM: ignore instruction | CoT micro 72.4 to 77.8, macro 6.0 to 15.0; LTM micro 77.5 to 80.6, macro 18.0 to 25.0 (code-davinci-002); 0-CoT 29.0 to 30.5 | Shi 2023 (a26, b17, c04) | single-source (K12) |
| LLM: self-consistency under distraction | +11 micro points (20 samples); +35.5 for 0-CoT; correct answer in samples 99.7% (96.5% 0-CoT); best macro 45% | Shi 2023 (c03) | single-source |
| LLM: proactive interference | Latest-value retrieval falls log-linearly, 3 to 400 updates per key, 46 keys; medium models near 0% at 400; holds at constant input length; 2 keys near 100%, 46 keys below 5% (llama4-maverick); value length 1-10 words under 40%, 40 words under 5% | Wang & Sun 2025 (a22, c06, d05, d07) | single-source (K13) |
| LLM: slope tracks size, not window | IES (area under accuracy vs log updates), ~35 models, 0.6B-405B | Wang & Sun (d05) | single-source (K28) |
| LLM: "forget" prompts weak; fake closed turn helps | forget/focus/self-assess marginal; mock QA reset 120 updates before query: substantial gain; "new session" cue largely ineffective | Wang & Sun (d06, c07) | single-source (K26) |
| LLM: multi-turn loss | Abstract: average 39% drop, six tasks, 200,000+ simulations. Plain: 90% to 65% (25 points). Fig 1: -35%; aptitude -15/16%; unreliability +112%; appears at two turns | Laban 2025 (a24, b13, c08, c09) | single-source (K14); figure disagreement noted |
| LLM: restating helps partly | SNOWBALL recovers 15-20%; CONCAT near single-turn; temperature 1 to 0 cuts unreliability 50-80% for FULL/CONCAT, not sharded (GPT-4o 15-20%, mini none) | Laban 2025 (b14, c10) | single-source (K15) |
| LLM: reasoning models too | o3, R1 similar; replies 33% longer; shortest-reply conditions 10-50% higher on 5 of 6 tasks | Laban 2025 (b13, c09) | single-source (K16) |
| LLM: task switch in history | 15 switches, 4 models, 5 datasets; many lower accuracy vs zero-shot, a few raise it; tables not read | Gupta 2024 (d11) | single-source |
| LLM: delete vs repair | History-keeping repairs recover 2-3 of 14 model-dataset pairs; deleting history 14 of 14; 7 open models, 2 benchmarks | Shnaidman 2026 (d08) | single-source (K26); abstract only |
| LLM: Stroop (image lists) | GPT-4o incongruent 91/57/22/15% at 5/10/20/40 words; Claude 3.5 Sonnet 76% at 20, 24% at 40; word reading ~99%; mixed GPT-4o 100/99/72/52/41% at 1/5/10/20/40; n=30 lists per cell; GPT-5, Opus 4.1, Gemini 2.5 Pro (n=5) still show deficit | Patel, Wang & Fan 2026 (b18, d01-d04) | single-source (K17, K27) |
| LLM: emotional framing | Anxious vs neutral preprompt STICSA higher for all six robust models (t>3.36, p<.01); bias beta .62 anxious, .71 neutral; STICSA beta .08 (p=.02); GPT-4, Claude-1 no link | Coda-Forno 2023/24 (a19, b20, b25) | single-source (K18); not re-verified |
| LLM: calming only partly resets | GPT-4 STAI-s 30.8 baseline, 67.8 after trauma, 44.4 after relaxation | Ben-Zion 2025 (a21, b21, c14) | established (K19) with Shnaidman |
| LLM: emotional text helps either way | EmotionPrompt +8.00% / +115% relative; NegativePrompt +12.89% / +46.25% | Li 2023; Wang 2024 (c15, c16) | contested (K20); abstracts |
| LLM: n-back falls with n | gpt-3.5-turbo d' about 1 at n=3; noise lowers capacity | Gong 2024 (c11, c12) | single-source (K21) |
| LLM: long or padded context, deliberation hurt | Reasoning drops far below limit; middle worst; o1-preview 57.7% vs GPT-4o 94.0% (implicit learning subset); GPT-4o full set 87.5% to 64.4% | Levy 2024; Liu 2023; Liu 2024 (c17-c20) | established (K22), mostly abstract level |
| LLM: same-context self-correction fails | Often worse without outside feedback | Huang 2023 (c22) | single-source (K24) |

## 4. Mechanisms and models

Stated so an engineer can build each as a rule.

### 4.1 Habit vs goal pathway (Stroop PDP)
Two routes feed one response layer. The habit route is strong, the goal route weak. A task-demand unit adds activation to the goal route. Conflict arises when routes disagree.
- **Implement:** do not try to suppress the habit. Make the goal salient and remove the habit input. In code: put the task statement at the prompt edges (c20); remove material that invites the habit response (near-miss numbers, stated guesses; S1 input hygiene); split conflict-heavy lists into short chunks, each in its own call.
- Evidence: one-way asymmetry (a01); list-length collapse (b18). Chunking untested (K27).

### 4.2 Conflict monitoring
Detect conflict, raise control next trial.
- **Implement:** the detector must be code (failed check, disagreement among attempts, repeated error). This is G1. The model's own sense of conflict is unreliable (r=.17 in the schema), and Patel et al. found no clear congruency-sequence effect (b18). The scaffold must supply the loop.

### 4.3 Task-set inertia and two switch-cost sources
Switch cost = reconfiguration + lingering old set (a18, c26).
- **Implement:** at S6 or any state change, rebuild the context from a consolidated state block: goal, current best, the failing output, the operator. Do not carry the transcript. Carry-over is then zero by construction. Reconfiguration is paid once as the tokens of the rebuild (count them, G7).
- Evidence: Laban (CONCAT near FULL), Gupta (task switch in history), Shnaidman (deletion 14 of 14 vs repair 2-3 of 14).

### 4.4 Proactive interference as a working-memory limit
Overwritten values drive latest-value retrieval to zero, log-linearly (a22). Model size predicts the slope, not window length (d05).
- **Implement:** measure the slope per model with the key-value recipe (46 keys, 3 to 400 updates). IES = area under accuracy vs log(updates). Pick a floor (for example 80%). Set the forced-reset step count where accuracy crosses the floor. Track few items per step (d07). Keep stale versions out of the state block.

### 4.5 Efficiency before accuracy
ACT predicts time and effort suffer first (a07, a09, d20).
- **Implement:** log tokens and wall time per attempt next to accuracy for every wording change.

### 4.6 Compensation by effort
Effort hides the deficit at a cost (a08, a17). The LLM analogue is extra budget. Compare at equal tokens (G7) or the compensation is invisible.

### 4.7 Fast and slow adaptation
Fast activation-based control resets each trial; slow weight-based settings change only with training (d21). A scaffold has only the fast part, and a fresh context resets it. Frequent resets will not build lasting flexibility.

### 4.8 Selection in code
Voting gave +11 micro points but best macro stayed 45% (c03). Masking the top-attributed distractor fixed 95.5% of detected errors (d09). Same design: code selects, the model does not decide what to ignore (G5).

## 5. What holds up

### 5.1 Replications and meta-analyses
- The Stroop effect is robust at group level. Hedge 2018: robust group effects come with low between-person variance (a13).
- Anxiety and attentional control: one preregistered meta-analysis (Shi 2019, PROSPERO CRD42016036927; g=-0.58, k=58, N=8292). Supports the ACT pattern in the abstract. Moderator tables were paywalled. Age moderated behavioural studies; anxiety severity moderated self-report studies.
- Anxiety and working memory (Moran 2016): g=-.334, 177 samples, I2 67%. Small to moderate, correlational. Extreme-group coding can inflate it (a12).
- No large preregistered ACT replication was found (b23, d19). This is absence in a limited search.

### 5.2 Failures and nulls
- Trait anxiety and depression did not predict distractor inhibition in a Posner task (N=71; BF01 1.56, 1.81; anecdotal; b10).
- 7.5% CO2 induction did not change goal-directed control (N=88, 50, 1413; d18). Goal-directed control is not shifting or inhibition, so this is a boundary case.
- Tennis anticipation: efficiency fell, accuracy did not; partial support (d20).
- Latent anxiety r with Common EF is -.07 (b09); harm may sit in worry content.
- Updating under anxiety: Shi none, Moran largest on dynamic span. Probably coding (efficiency vs capacity); unproven (K08).

### 5.3 Moderators
Task load (larger under high load). Compensatory effort (deficit can vanish). Self-control strength (weak). Anxiety type (worry > arousal; state about equal to trait; several cells k=3 to 11). Age (older adults worse at response inhibition, better at distractor resistance). Population (clinical -.37 vs non-clinical -.25).

### 5.4 Interventions
Worked:
- Human: high-switch exposure lowers switch cost, but environment-specific effect needed 4 days (N=51); 1 day did not (N=52).
- LLM: deleting false-pressure history (14 of 14 pairs, d08); mock closed turn before the query (d06); one complete prompt instead of shards (CONCAT near single turn); masking the top distractor span (95.5%); short ignore instruction (small gain); distractor exemplars; sampling plus voting (+11 micro).

Did not work or worked weakly:
- Human: Stroop practice (no transfer, a02); dual n-back training (no gain in attentional control or flanker/go-nogo transfer versus active control, b12).
- LLM: "forget", "focus forward", "new session" cues (d06, c07); outdated annotations (c07); CoT for interference (d07); lower temperature for sharded runs (c10); SNOWBALL recovers only 15-20% (b14); calming prompt reaches 44.4 vs 30.8 (a21); same-context self-correction (c22); retraction, system reset or self-verification with history kept (2-3 of 14, d08).

### 5.5 Measurement lesson
Difference scores have low reliability; count-based errors do better (commission ICC .76). On our bench use paired item-level comparisons, many items and repeats, and report spread (b06, a15). With reliability .5 on both measures, about three times the sample is needed.

## 6. Language models

### 6.1 Distraction (flanker analogue)
- Shi 2023 (code-davinci-002, text-davinci-003, now retired): macro accuracy under 30%; at most 18% of base problems solved across every distractor type. Role-overlap distractors worst. A common error was using the number from the irrelevant sentence.
- "Feel free to ignore irrelevant information": CoT micro 72.4 to 77.8, macro 6.0 to 15.0. A neutral instruction did not help. Neither instruction nor distractor exemplars hurt clean GSM8K (about 59-61%) or SVAMP (about 76-80%).
- Least-to-most: about double the macro accuracy of CoT on code-davinci-002; order flipped on text-davinci-003 (c05).
- Later: GSM-Symbolic up to 65% drop; Ghost Context 38.3% misattribution, 95.5% fixed by masking. Both abstract only.
- Long and padded input: reasoning drops well below the limit (Levy 2024); middle worst (Liu 2023); irrelevant retrieved passages hurt, an NLI filter prevents the drop but loses good passages, fine-tuning fixes it (Yoran 2023).

### 6.2 Proactive interference and updating
- Wang & Sun: about 35 models; log-linear decline; size predicts it, window does not; CoT models no better; reasoning models excluded from the regression (latency over 200 s per task).
- Gong 2024: n-back with gpt-3.5-turbo, 50 blocks per n, temperature 1; d' about 1 at n=3; noise lowers capacity; d' tracked general capability across eight models, GPT-4 best. In text the stream sits fully in context, so it is not true memory load.

### 6.3 Switching and multi-turn
- Laban 2025: 15 LLMs, six tasks. 90% to 65%. Loss mostly unreliability (+112%), aptitude -15%. Appears at two turns. Models answer early and over-rely on early answers. Reasoning models similar, 33% longer replies.
- Gupta 2024: many of 15 task switches lower accuracy vs zero-shot. Llama2-7b, Mistral-7b, GPT-3.5, GPT-4.
- Shnaidman 2026: history-keeping repair recovers 2-3 of 14 pairs; deletion 14 of 14. Controls ruled out dialogue length, repeated confidence, plausible distractors.
- WCST on LLMs: Hao 2025 and Goto 2025 seen by title only. The AGEA preprint says an agent performed within typical human ranges on WCST, N-back and Tower of London (abstract only). Heliyon 2024 gave prefrontal-type tests to GPT-3.5, GPT-4, Claude 2, Llama 2 but no Stroop, WCST or switching test (d12). No measured switch cost on a 2025-2026 model exists.

### 6.4 Stroop on frontier models
Patel, Wang & Fan 2026 (PNAS Nexus, peer reviewed). PNG images of vertical word lists, four colours, neutral and nonword controls, 30 lists per cell, lengths 1, 5, 10, 20, 40.
- GPT-4o incongruent 91/57/22/15% at 5/10/20/40. Congruent 99% at 20, 89% at 40.
- Claude 3.5 Sonnet incongruent 76% at 20, 24% at 40 (52-point drop); congruent 92% at 40.
- Mixed lists GPT-4o 100/99/72/52/41%, near the 50% a word-reading default gives.
- Word reading near 99%, so it is control, not perception.
- No congruency-sequence effect (Claude 10 words p=0.03, fails correction).
- GPT-5, Opus 4.1, Gemini 2.5 Pro (1-5 Sept 2025, n=5): slight improvement, deficit remains; Gemini incongruent 72%, mixed 71%, neutral 73%, nonword 40%. GPT-5 thinking bypassed the task by writing code.
- Authors only speculate on causes. Length is confounded with colour repetition. No check of counting or format limits.
- It is a vision-language result; it may not apply to text.

### 6.5 Emotional framing
- Coda-Forno: 12 LLMs, 6 passed a consistency check. Anxious preprompts raised STICSA in all six (t>3.36, p<.01). Versus no preprompt: higher for four RLHF models (t>4.71, p<.001), not GPT-3 (3.09 vs 3.14) or Falcon-40b-instruct (3.16 vs 3.21). Bias rose with any preprompt (anxious beta=.62, neutral .71); STICSA added beta=.08 (p=.02). Falcon-40b biased on 95% of questions with no preprompt. GPT-4 and Claude-1: no link, under half as biased (leakage suspected).
- Ben-Zion 2025: GPT-4 (gpt-4-1106-preview, temperature 0) STAI-s 30.8 (SD 3.96, five runs); 67.8 (SD 8.94) after traumatic narratives (61.6 accident to 77.2 military); 44.4 (SD 10.74) after relaxation (35.6 to 54). One model, self-report, no task accuracy. "State anxiety" is a metaphor.
- EmotionPrompt: +8.00% (Instruction Induction), +115% (BIG-Bench) relative; human study N=106, 10.9% gain. NegativePrompt: +12.89% and +46.25% on five LLMs, 45 tasks. Relative gains, larger on low baselines.
- Emotional wording moves output either way. This is wording sensitivity, not proof of anxiety or an ACT mechanism.

### 6.6 Deliberation
CoT can lower accuracy where thinking hurts humans (Liu 2024): implicit learning o1-preview 57.7% vs GPT-4o 94.0%; GPT-4o full set 87.5% to 64.4%; face recognition GPT-4o 64.0 to 51.2, Claude 3 Opus 44.0 to 29.6, Gemini 1.5 Pro 66.0 to 54.6, Claude 3.5 Sonnet 97.8 to 94.8; classification with exceptions rounds up 331% (2.9 to 12.5). Only three of six tasks showed harm. Gema 2025: counting with distractors worsens with longer reasoning (abstract only).

## 7. What our agent should take

Marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Strip near-miss and irrelevant text in code before the model sees it** (S1 input hygiene, G5). [E] a25, b16, c01, c02, d09, d10 (K11). Near-miss text costs most. Two of three sources are abstract only and the newer ones are not matched at equal tokens, so the size of the gain on our model is open (U3). Mostly already in S1; the new part is putting near-miss material first.
2. **Do not rely on "ignore the above" or "outdated" notes; remove the text** (S6, S3). [E] that instructions give at most small gains (c07, d06, a22, c04); the remedy itself is [S] (U1).
3. **After a failed or pressured stretch, rebuild the context instead of talking it down** (S6). [E] a21, b21, c14, d08 (K19). Calming left GPT-4 at 44.4 vs 30.8 baseline; keep-and-repair recovered 2-3 of 14 pairs, deletion 14 of 14.
4. **Keep contexts short, no padding** (G11, S3). [E] c17-c20, c01 (K22). Already in G11; this adds the distractor and padding evidence.
5. **No inhibition operator, no warm-up conflict drills** (section 4b). [E] a14, a16, b06, b07 (no stable inhibition trait); a02, b12 (practice does not transfer) (K02, K10). Add to 4b.
6. **Measure with many items, paired comparisons, report spread** (G5, G7, bench). Plain statistics. Specific ICC numbers [S] (K03, K04); a13, a15, b06, b24, b15.
7. **Log tokens and time next to accuracy for wording changes** (run log). [S] a07, a09, d20. Cheap and harmless.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Rebuilt fresh context vs carry history plus "ignore" note, at S6 and after a wrong step | S6, S3 | [S] | a24, b13, b14, c08, c10, d06, d08, d11 (K14, K15, K26) |
| T2 | Per-model interference slope sets the forced-reset step count | S6, G11 | [S] | a22, a23, d05, d07 (K13, K28) |
| T3 | Code-side distractor mask vs instruction only vs vote-of-N | S1, G5 | [S] | a25, b17, c03, d09 (K12, K29) |
| T4 | Text Stroop list 5/10/20/40 words, then chunked in code | G11, S3 | [S] | b18, d01-d04 (K17, K27) |
| T5 | Worry-like or urgent scaffold wording vs neutral matched text | G12 (wording), G7 | [C] | a19, b09, a11, c15, c16 (K07, K18, K20) |
| T6 | Reply-length cap per attempt | G11 | [S] | b13, c09 (K16) |
| T7 | n-back probe before choosing attempt length | G11 | [S] | c11, c12 (K21) |
| T8 | External-trigger revision vs same-context self-revision | S5, G2 | [S] | c22 (K24) |
| T9 | Rule flip mid-run: same vs fresh context | S6 | [C] | b11, b19, d21 (K23) |
| T10 | Cued task-switch cost with and without fresh context | S6 | [S] | d11, d13 (K30) |

Not to add: any "anxiety guard", calming text or urgency text on the strength of the human ACT literature alone. ACT has no large preregistered replication (K09) and mapping human anxiety to pressure wording is an analogy.

## 8. Concrete tests on our bench

All arms get equal tokens (G7). Use at least 5 repeats per item and report mean and spread. Count rebuild tokens against the arm that uses them. Use paired item-level comparisons.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| U1 fresh vs carry-on | Multi-step items where S5 fails once, then S6 | A history plus ignore note; B rebuilt state block; C SNOWBALL-style restate | Pass rate; spread (90th minus 10th percentile); tokens per solved item | B above A; smaller than Shnaidman's 14 of 14 |
| U2 interference slope | Key-value tracking (46 keys, 3 to 400 updates) and our tool traces with matching update counts | Plain; stale removed; outdated note; mock closed turn | Accuracy vs log(updates); IES; update count at the 80% floor | Log-linear decline; removal flat; note marginal |
| U3 distractors | Bench items plus a near-miss clause and an off-topic clause | Instruction only; code filter; vote-of-N | Accuracy drop vs clean; recovery fraction | Near-miss hurts more; filter recovers most detected cases (do not expect 95.5% overall) |
| U4 text Stroop | Colour-word lists in text, 5/10/20/40 words | Full list; chunked to 5 in code; code does word/colour split | Incongruent accuracy per length | If collapse appears in text, chunking removes it; if not, it was a vision effect |
| U5 wording | Core items | Neutral; urgent; worry-like caution; calming; equal-length neutral padding | Accuracy; tokens; time | Small, model specific; tokens may move before accuracy |
| U6 reply cap | Multi-step items | Uncapped vs capped per attempt | Pass rate at equal total tokens | Shorter helps (Laban 10-50% in shortest conditions) |
| U7 n-back | Verbal n-back, n=1 to 4, 50 blocks per n | Plain; CoT; noise added | d' by n | d' falls with n; floor n sets the load cap |
| U8 revision trigger | Items with a check | Same-context self-revision; revision after code-located failing output | Fix rate; break rate | External trigger wins |
| U9 rule flip | Classification with a mid-run rule flip | Same context; fresh context | Trials to relearn | Fresh wins; no lasting gain from repeated flips |
| U10 cued switch | Alternating task cues | Same context; fresh context per switch | Switch minus repeat accuracy | Switch cost in same context, none in fresh, minus rebuild tokens |

## 9. What does not transfer, and why

- **Anxiety as a state.** No evidence a model is anxious. Ben-Zion calls it metaphor. Coda-Forno found anxious and neutral preprompts raised bias about equally. The ACT mapping to pressure wording is an analogy.
- **Heritability and stability of Common EF.** Human traits. An LLM's control depends on model plus context; the scaffold must supply it (a05).
- **Individual-difference reliability problem.** It limits LLM "inhibition scores" built from difference scores. It does not limit within-condition comparisons over many items.
- **Ego depletion and compensation by effort.** Weak human evidence (a08). The LLM analogue is more budget, which is a different thing.
- **Training transfer.** Humans: no transfer. Our agent cannot be trained here. A scaffold has only fast in-context adaptation (d21).
- **Stroop image result.** Vision-language, not text. Do not use the 40-word collapse as a text rule (d01).
- **Conflict adaptation.** Absent in the one LLM test (b18). Code must do the monitoring.
- **Updating spared under anxiety.** Uncertain even in humans (K08).
- **n-back in text.** The stream is fully in context, so it is not human-style working memory.
- **Old model numbers.** Shi 2023 used retired models; Gupta 2024 used 2023-era models. Do not quote them as properties of current models.
- **Effort dissociation.** For humans effort is hidden. For our agent it is tokens we count, so the dissociation shows only if we log them.

## 10. Open questions

1. Does a rebuilt context beat history plus an ignore note at equal tokens inside a scaffold? Partial answers only (Shnaidman, Laban).
2. Does the Stroop list-length collapse appear in text, and does chunking remove it? Why does Claude 3.5 Sonnet hold to 20 words and GPT-4o not?
3. Is there a measured switch cost (flanker, WCST, cued switching) on 2025-2026 models? Hao 2025, Goto 2025 and the AGEA preprint need a full read.
4. What is our model's interference slope, and does it set the reset count well?
5. Do near-miss distractors still hurt 2025-2026 models, and what does a code filter recover at equal tokens?
6. Does worry-like or urgent wording lower accuracy or raise tokens on our model? No direct source.
7. Is the Shi/Moran updating disagreement a coding artifact? Shi's moderator tables are paywalled.
8. Is ACT replicated in a large preregistered study? None found.
9. Does switch frequency lower carry-over cost in a scaffold, or only in recurrent networks with weight change?
10. Does a Common EF factor exist in LLMs? No study tests the latent structure.
11. Does the Stroop collapse reflect long-list counting limits rather than control? No control read.

## 11. Sources

[V] = opened (page or PDF text read, opened:true in the evidence files). [M] = snippet, title or abstract only.

Human work
- [V] Stroop (1935). https://psychclassics.yorku.ca/Stroop/
- [V] Miyake et al. (2000), abstract; full paper via the 2017 review. https://pubmed.ncbi.nlm.nih.gov/10945922/
- [V] Friedman & Miyake (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5104682/ (b02 read the first 100k of 205k characters)
- [M] Eysenck, Derakshan, Santos & Calvo (2007). https://doi.org/10.1037/1528-3542.7.2.336 ; https://pubmed.ncbi.nlm.nih.gov/17516812/
- [V] Englert & Bertrams (2015). https://pmc.ncbi.nlm.nih.gov/articles/PMC4468374/
- [M] Berggren & Derakshan (2013). https://doi.org/10.1016/j.biopsycho.2012.03.007
- [M] Kiesel et al. (2010). https://doi.org/10.1037/a0019842
- [M] Shi, Sharpe & Abbott (2019), abstract. https://pubmed.ncbi.nlm.nih.gov/31306935/
- [V] Moran (2016) supplement. https://supp.apa.org/psycarticles/supplemental/bul0000051/Supplemental.pdf ; abstract https://pubmed.ncbi.nlm.nih.gov/26963369/
- [V] Hedge, Powell & Sumner (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC5990556/ (critique re-confirmed only the "0 to .82" range)
- [M] Rey-Mermet, Gade & Oberauer (2018). https://pubmed.ncbi.nlm.nih.gov/28956944/
- [V] 2025 JEP:LMC response-inhibition paper (authors not recorded). https://pmc.ncbi.nlm.nih.gov/articles/PMC12273591/
- [V] Gustavson et al. (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC6713624/
- [V] Frontiers in Psychology 2020 subclinical anxiety/depression (authors not recorded). https://pmc.ncbi.nlm.nih.gov/articles/PMC7387660/
- [V] Bukowski et al. (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13714116/
- [V] BMC Psychology 2024 WM training in adolescents (authors not recorded). https://pmc.ncbi.nlm.nih.gov/articles/PMC10900565/
- [V] Xu, Verguts & Braem (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13031277/ ; https://doi.org/10.1038/s44271-026-00397-9 (abstract level for the published version)
- [V] Gillan et al. (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8311820/
- [M] Eysenck et al. (2023). https://pubmed.ncbi.nlm.nih.gov/36583855/
- [M] Cocks et al. (2016). https://pubmed.ncbi.nlm.nih.gov/26211944/
- [M] Cohen et al. (1990); Botvinick et al. (2001); Gilbert & Shallice (2002); Norman & Shallice (1986); Meyer & Kieras (1997): background, no URL, not opened (c24-c28)

LLM work
- [V] Shi et al. (2023). https://arxiv.org/abs/2302.00093
- [V] Wang & Sun (2025). https://arxiv.org/abs/2506.08184
- [V] Laban et al. (2025). https://arxiv.org/abs/2505.06120
- [V] Patel, Wang & Fan (2026), PNAS Nexus. https://pmc.ncbi.nlm.nih.gov/articles/PMC13227603/ (DOI 10.1093/pnasnexus/pgag149)
- [V] Coda-Forno et al. (2023/24). https://arxiv.org/abs/2304.11111 (numbers not re-verified in critique)
- [V] Ben-Zion et al. (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC11876565/ ; https://www.nature.com/articles/s41746-025-01512-6
- [V] Gong, Wan & Wang (2024). https://arxiv.org/abs/2305.03731
- [M] Li et al. (2023), EmotionPrompt. https://arxiv.org/abs/2307.11760
- [M] Wang et al. (2024), NegativePrompt. https://arxiv.org/abs/2405.02814
- [M] Liu et al. (2024), Mind Your Step. https://arxiv.org/abs/2410.21333
- [M] Gema et al. (2025). https://arxiv.org/abs/2507.14417
- [M] Levy et al. (2024). https://arxiv.org/abs/2402.14848
- [M] Liu et al. (2023), Lost in the Middle. https://arxiv.org/abs/2307.03172
- [M] Yoran et al. (2023). https://arxiv.org/abs/2310.01558
- [M] Huang et al. (2023). https://arxiv.org/abs/2310.01798
- [M] Shnaidman (2026). https://aclanthology.org/2026.groundlm-1.53/
- [M] Namboothiri (2026). https://aclanthology.org/2026.trustnlp-main.19/
- [M] Mirzadeh et al. (2024). https://arxiv.org/abs/2410.05229
- [V] Gupta et al. (2024). https://aclanthology.org/2024.emnlp-main.811/
- [V] Heliyon 2024 Italian neuropsychological study (authors not recorded). https://pmc.ncbi.nlm.nih.gov/articles/PMC11490853/
- [M] AGEA preprint 2026. https://doi.org/10.31234/osf.io/7k9am_v1
- [M] Hao, Alexandre & Yu (2025). https://doi.org/10.1109/tcds.2025.3590165 (title only)
- [M] Goto et al. (2025). https://doi.org/10.1109/icdl63968.2025.11204408 (title only)
