# Collective intelligence factor c: deep document

*Subfield A17.07. Source files in this folder: evidence_a-d.jsonl (ids a01-a25, b01-b28, c01-c29, d01-d18), claims.jsonl (K01-K28), critique.md. Relevance to our agent: background only. No schema change follows from c itself. The usable lessons are about multi-agent design, and they mostly confirm guardrails G4, G7 and G9 that are already in SCHEMA.md.*

## 1. What it is

Collective intelligence c is the idea that a group has a general ability, like g for a person. A group that does well on one task tends to do well on other, different tasks. That shared ability is called c. It is inferred statistically: you give many groups a battery of varied tasks, check that the scores correlate (a "positive manifold"), and extract one factor. (a01, a24)

Three criteria are used to call something a c factor (a24, from Woolley 2010 and Chabris 2007):
1. One factor explains 30 to 50% of variance.
2. The first factor is at least twice the second.
3. It is not explained by average member intelligence.

What c is claimed to do: predict group performance on a new, held-out task better than average or maximum member IQ does. What c is claimed to depend on: social sensitivity, even speaking turns, and (in some samples) the share of women in the group. (a07)

The field is split. The Woolley network (MIT, Carnegie Mellon) reports c in every replication they run. Independent labs mostly report that c is weak, absent in computer-mediated or mixed-task data, or explained by member IQ. (a13)

The LLM version: researchers now build groups of LLM agents, run a task battery, and ask whether one "artificial CI" (ACI) factor appears. One paper says yes, with a much stronger factor than in humans (Zhou 2026, c01). Most other LLM papers do not measure c. They test the practical claims around it: do more agents help, does perspective-taking help, do groups pool information. Mostly they find that they do not, unless the task is decomposable or the base model is weak. (K11 to K19)

## 2. History and theories in depth

**Roots in g.** Spearman (1904) showed that scores on very different mental tests correlate. A single general factor g explains 40 to 50% of variance in individual batteries (a16 gives this range for humans). Chabris (2007) argued that a similar factor might exist for groups, and set the three criteria above (a24).

**Founding study: Woolley, Chabris, Pentland, Hashmi, Malone (2010), Science 330.** (a01 to a07; opened full PDF)
- Two studies, 699 people, 192 groups of 2 to 5 members. Study 1: 40 groups of 3. Study 2: 152 groups of 2 to 5. (Note: an earlier draft in c27 wrongly said 2-3 and 3-5; corrected in critique.)
- Tasks were taken from McGrath's task circumplex: brainstorming, matrix reasoning, moral reasoning, shopping trip planning, typing, and others. Study 1 used a video game as the criterion task. Study 2 used an architectural design task modelled on an R&D problem.
- Study 1: mean inter-task r = 0.28; first eigenvalue above 43% of variance; second 18%; CFA chi2 = 1.66, df = 5, p = .89, CFI = .99, RMSEA = .01.
- Study 2: first factor 44%, second 20%; CFA chi2 = 5.85, df = 5, p = .32, CFI = .98. Structures invariant across studies (chi2 = 11.34, df = 14, p = .66).
- Prediction: c with the video-game criterion r = 0.52 (p = .01, N = 40); average member IQ r = 0.18 (ns), maximum r = 0.13 (ns). Regression: c b = 0.51 (p = .001), IQ terms ns. Study 2 criterion: c b = 0.36 (p = .0001), IQ ns. The same design task done alone by 63 people gave IQ r = 0.33 (p = .009). So IQ predicts individual performance but, the authors argued, not group performance beyond c.
- Weak link to member IQ: pooled average member IQ with c r = 0.15 (p = .04); maximum r = 0.19 (p = .008).
- Predictors: average social sensitivity (Reading the Mind in the Eyes, RME) r = 0.26 (p = .002). Variance in speaking turns (sociometric badges, subset only) r = -0.41 (p = .01). Proportion female r = 0.23 (p = .007), mediated by social sensitivity (Sobel z = 1.93, p = .03). Cohesion, motivation and satisfaction did not predict c. In a joint regression only social sensitivity was significant (b = 0.33, p = .05).
- Detail that matters: the "43-44%" headline is the first eigenvalue share. Principal-axis extraction on the ten-task sets gave 31% (Study 1) and 35% (Study 2) (a04). Rowe later computed average variance extracted (AVE) of only 22% for Study 2 (b09).

**Replication by the same team: Engel, Woolley, Jing, Chabris, Malone (2014), PLOS ONE.** (a10, a11, b01 to b03)
- 68 groups randomly assigned: 32 face-to-face, 36 online text chat. New task battery. Planned minimum 60 groups for 80% power.
- First factor 49% (face-to-face) and 41% (online); second factor under half of that.
- RME with c: r = .53 (p = .002) face-to-face, r = .55 (p < .001) online. (a10 first printed .52; the original text and b02 give .53; critique corrected this.) Without the two lowest-RME groups: r = .47 and .48.
- Percent female with c online: r = .41 (p = .01). Mediation by RME: Sobel z = 1.95, p = .05 (marginal).
- More total communication went with higher c; a larger SD of communication across members (domination) went with lower c, in both modes. Exact table cells could not be reliably extracted from the PDF text.
- Personality general factor was unrelated to c.
- The point of the paper: RME predicts c even with no faces visible. So the trait is wider than eye reading. It is "reading between the lines".

**Cross-cultural: Engel et al. (2015).** US 68 groups, Germany 25 student groups, Japan 116 groups in organisations; c present in each (b20; second-hand via Janssens, not opened).

**Applied extensions by the same network (titles only, a25):** business performance (Mayo and Woolley 2017), 248 League of Legends teams where c predicted later play (Kim 2017; b18), high-stakes decisions (Radcliffe 2019; Rogers 2019).

**Pro-c synthesis: Riedl, Kim, Gupta, Malone, Woolley (2021), PNAS.** (a08, a09, c25, d09)
- 22 studies, 1,356 groups, 5,279 people, groups of 2 to 7, 4 to 8 tasks per study, all on the POGS online platform. Three tasks (brainstorm object, typing, unscramble words) appear in every study.
- Mean inter-task r = 0.27 (range 0.12 to 0.50). Standardised loadings 0.27 to 0.52. AVE reported as 44%. Leave-one-task-out: mean r = 0.40 (95% CI 0.26 to 0.53), all p < .001.
- Method: random-effects meta-analytic one-factor model on pooled correlations, not Woolley's eigenvalue share (d09).
- Drivers by random forest: collaboration process (skill congruence, strategy, effort) most, then individual skill (mean and max), then group size, social perceptiveness, composition. Skill congruence and strategy positive; effort did not predict. Age diversity negative. Task matters: Sudoku over 51% from individual skill; unscrambling words 55% from process.
- Corrected in PNAS 2022 (correction not read).
- Arithmetic problem (inference by our own checker, d10): if loadings run .27 to .52, the mean squared loading is at most .27, so an AVE of 44% cannot come from them. A one-factor model with mean r .27 implies about 27%. Rowe's 30.23% agrees with this lower figure. We have not read the SI, so the 44% may use a different definition. Safe practice: always say which statistic you quote.

**Independent meta-analysis: Rowe, Hattie, Hester (2021), Cognitive Research.** (a12, a13, b08 to b11)
- 14 studies, 19 samples, 1,359 groups of 2 to 6. Mean first-factor variance 43% (SD 3.6%).
- c with criterion tasks: random-effects r = .26 (95% CI .10 to .40), 9 effects, 8 samples, N = 857 groups; Q(8) = 59.36, p < .001; I2 = 86.5%; tau2 = .05.
- Average member IQ with criterion (6 samples, N = 366): r = .06 or .067 (95% CI -.08 to .20; I2 = 35%). Average IQ with c: r = .185 to .19.
- AVE over 49 loadings: 30.23% (range 22% in Woolley Study 2 to 37% in Bates and Gupta Studies 2+3). Below the 50% Fornell-Larcker minimum.
- Power: only 6 of 19 samples (31.6%) had enough groups for r = .10 to .30 at 80% power. None had the 784 groups needed for r = .10. About 80% of studies underpowered.
- Only 7 of 19 samples independent of Woolley and co-authors. All Woolley-affiliated attempts reproduced c; independent attempts partly or wholly failed. Authors advise not adopting c until more evidence accumulates.
- Method critique (a14): tasks chosen by face validity, average battery 6.3 subtests, few and short tasks, low reliability, order rarely randomised, weak criterion tasks, 14 of 19 samples in a lab.

**The IQ rebuttal: Bates and Gupta (2017), Intelligence.** (b04 to b07, d11 to d13) See section 5.

**Computer-mediated and pooled nulls: Barlow and Dennis (2016); Graf, Gimpel, Barlow (2019); Credé and Howardson (2017).** See section 5.

**Dyad tests:** Tomprou et al. (2021) on video vs audio dyads (d14); a 2025 dyadic CHC-aligned study with 105 dyads (a15).

**LLM turn (2023 to 2026).** Li et al. (2023) on theory of mind in agent teams (d16); Choi et al. (2025) debate vs vote (b24); Kim et al. (2026) scaling agent systems (c20, c21, d02); Riedl (2026) emergent coordination (a20, c08 to c10, d15); Li, Naito, Shirado (2026) hidden profiles (c11 to c14, d05, d06); Wu et al. (2026) teammate benchmark (c15 to c18); Zhou et al. (2026) ACI factor (a17 to a19, c01 to c07, d03, d04); Tran and Kiela (2026) equal-token single vs multi-agent (d01); Li et al. (2026) Superminds Test (b25, d18). Ilic and Gignac (2024) give the single-model baseline (a16, d17).

**Competing theories of why groups differ.**
1. c theory: a group-level ability that comes from interaction quality (social sensitivity, turn-taking).
2. g theory (Bates and Gupta): group score is mostly average member IQ; any group factor is an echo of member g.
3. Process-fit theory (Riedl 2021; Janssens 2022; a23): CI is not a trait but a fit between interaction process and task demands over time. Outcome scores alone mislead.
4. Artifact theory (Credé and Howardson): small positive correlations arise from low-effort responding, nesting and averaging of members' separate answers.
5. Task-structure theory (McGrath types; Graf; Kim 2026 for LLMs): group ability is not one thing; it splits by task type (idea generation, conflict resolution, execution).

## 3. Core findings with exact numbers

Status key: replicated (by more than one team), contested, single-source, human-only, LLM-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Positive manifold and first factor in human groups | 192 groups, 699 people; first factor 43% (Study 1, 40 groups) and 44% (Study 2, 152 groups); second 18% and 20%; mean r .28 | Woolley 2010 (a01 to a04) | Replicated by same team (Engel 49% and 41%, N = 68), by Bates and Gupta (39.8%, 26 groups), by Riedl pooled |
| Principal-axis share is lower than the headline | 31% (Study 1) and 35% (Study 2), ten-task sets | Woolley 2010 (a04) | Established |
| Pooled over 22 studies | 1,356 groups, 5,279 people; mean r .27 (.12 to .50); loadings .27 to .52; AVE 44% as reported (arithmetic suggests about 27%) | Riedl 2021 (a08, d09, d10) | Established for the factor; the 44% is questioned |
| Independent meta-analysis | 19 samples, 1,359 groups; first factor mean 43%; AVE 30.23% over 49 loadings | Rowe 2021 (a12, b09) | Established |
| c predicts held-out tasks | Woolley: r .52 (N = 40), b .36 (N = 152). Riedl leave-one-out r .40 (.26 to .53). Rowe r .26 (CI .10 to .40; I2 86.5%; 857 groups) | a05, a08, a12 | Established, weak to moderate, very heterogeneous |
| Member IQ link to c, Woolley | Average IQ with c r .15 (p .04); max r .19 (p .008) pooled | a06 | Contested |
| Member IQ explains group IQ, Bates and Gupta | Studies 2+3 (80 groups): average IQ explains 81% of group-IQ variance, beta .86; best SEM fixes IQ path at 1.0 with residual 0; Study 1: 57% of variance, IQ beta .76 | b04, b05, d12 | Contested; not preregistered; task overlap with IQ items |
| Meta-analytic IQ triple | c-criterion .253; IQ-c .185; IQ-criterion .067 | Rowe (b10) | Established as a pattern; unweighted means |
| Social sensitivity (RME) and c | r .26 (Woolley S2); .53 face-to-face, .55 online (Engel, 68 groups); min-RME r .52, max .41, mean .48 (Meslec, 30 groups); dyads beta .22 (105 dyads) | a07, b02, b17, a15 | Contested: Bates and Gupta found RME beta .19 only after IQ and a bad-fitting RME-only model (CFI .60) |
| Weak-link rule | Minimum RME beta .49 (p < .05) vs max .19 ns; min and mean correlate r .82 | Meslec 2016 (b17) | Single-source |
| Proportion female | r .23 (Woolley); r .41 online (Engel); positive in Riedl, mediated by social perceptiveness; ns in all three Bates and Gupta studies; dyads all-female beta -.54 | a07, b03, b06, a15 | Contested |
| Turn-taking equality | r -.41 (Woolley badge subset); communication SD negative (Engel); ns in Bates and Gupta; dyads beta .08, ns (p .24) | a07, a11, b06, a15 | Contested |
| Turn-taking intervention (human) | Equal-talk/empathy vs authority vs control (14/12/14): F(2,34) = 1.14, p = .33. Video vs audio: turn inequality 26.31 vs 9.14 (p < .001) but CI -.07 vs .08, t(97) = -1.23, p = .22 | d11, d14 | Null or inconclusive |
| No c in some independent data | Graf: 745 teams, mean inter-task r .001, one-factor chi2 = 40.79, CFI .73, TLI .45, parallel analysis 3 factors. Barlow and Dennis: 86 virtual groups, no c | b12, d07, b19 | Contested; Graf is a 4-page abstract |
| Underpowered literature | 6 of 19 samples powered for r .10 to .30 | b11 | Established |
| Human-AI groups | 106 experiments, 370 effect sizes, g -0.23 overall; decisions g -0.27 (p .002); creation g 0.19 (CI -0.09 to 0.48, ns) | Vaccaro 2024 (b21) | Established as meta-analysis; mostly pre-LLM |
| LLM populations have a general factor | 591 LLMs, 12 benchmarks, mean r .73 (humans .45 to .50), general factor 65.6%, omega h .94; parameters with factor r .54 | Ilic and Gignac 2024 (a16) | Single-source; rows non-independent |
| LLM groups have an ACI factor | 108 groups, 8 LLMs, 5 tasks; mean r .55 (human 0.28 quoted from different tasks); first factor 66.3%, second 18.7%; CFI .967 | Zhou 2026 (a17, c01, c02) | Single-source, LLM-only |
| ACI predicts held-out task | Leave-one-out r above .8 on 3 tasks and about .5 on the other 2 | c03 | Single-source |
| ACI drivers | Skill congruence over 50% of random-forest importance; mean member g 37%; max g, size, effort each under 5% | a18, d04 | Single-source; congruence uses same task scores (circular risk) |
| Stronger model is not enough | Qwen2.5-72B group (g 119.9), 75% more cost, ACI 9.7% lower than an internlm2.5-20b group (g 92.1) | c05 | Case study only |
| Centralised hub | Strongest LLM as hub beat fully connected network in most cases at lower token cost | a19, c05 | Single-source |
| ACI as regulariser | GPTSwarm math .81 to .91 (+12.3%); others +1.1 to +3%; G-Designer +2.3 to 7.8%; reported average +4.6% | c07 | Single-source |
| More agents hurt | GPT-4.1 guessing game: odds of success x0.92 per extra member (p < 1e-16), x1.50 per temperature unit (preliminary grid, 7,150 runs) | Riedl 2026 (a20, b22) | Single-source |
| Capability ceiling | Single-agent accuracy above ~45% means negative returns from more agents: beta -0.236 (CI -0.396 to -0.076), p .004, 4,800-token matched budget. Relative change +80.8% (Finance, decomposable) to -70.0% (PlanCraft, sequential). Error amplification 1.0 / 4.4 / 5.1 / 7.8 / 17.2 for single / centralised / hybrid / decentralised / independent | Kim 2026 (c20, c21, d02) | Established for these benchmarks; 45% is a fit over 6 benchmarks |
| Equal thinking tokens, single vs multi-agent | Mean accuracy single / sequential / debate / ensemble at 100 tokens .290/.364/.370/.280; 1k .418/.379/.388/.333; 5k .427/.386/.420/.411; 10k .411/.424/.423/.420 | Tran and Kiela 2026 (d01) | Single-source, text multi-hop QA |
| Vote beats debate | Qwen2.5-7B: single .7205, debate .7377, vote .7691. Llama3.1-8B: .6203, .6990, .7242. Arithmetic Qwen: single .8140, vote .9900, centralised debate .43 to .55 | Choi 2025 (b24) | Single-source (2 small models, 7 benchmarks) |
| ToM prompt, powered test | N = 10, T = 1, 200 groups per arm (Plain, Persona, Persona+ToM): overall success not different. Emergence share Plain 37%, Persona 44%, ToM 18%. Mediation via synergy ACME .034, 95% CI -0.000 to 0.07, p .053 | Riedl 2026 (a20, c08, d15) | Null for success |
| Synergy x redundancy | Interaction .24, p .014; each amplifies the other by 27% on log-odds | b23, c09 | Single-source, observational |
| ToM belief text, small test | ToM accuracy GPT-4 with belief state 97.2 / 80.1 / 69.4% (introspection / 1st / 2nd order) vs GPT-4 80.0 / 60.0 / 64.3%; ChatGPT 79.0 / 41.9 / 11.6; team test 3 trials | Li 2023 (d16) | Underpowered |
| Hidden-profile failure | 65 tasks, 15 LLMs: 30.1% multi-agent distributed vs 80.7% full information. GPT-4.1 verification tasks .008 before, .233 after, .733 full profile. Humans .125 before, .385 after, .604 full | Li, Naito, Shirado 2026 (c11, c12) | Single-source |
| Structured exchange fixes it | Exchange (2 rounds: 1 to 2 facts plus one doubt) then Decide (1 pass): GPT-4.1 .037 to .800; Gemini-2.5-Flash .173 to .727; Flash-Lite .043 to .743; 18 tasks, 5 runs, 4 agents | d05 | Single-source; token cost not reported |
| Prompt and size effects, hidden profile | Rounds 5/10/15/20: .108/.200/.233/.133. Cooperative .200 to .242; conflictual .017; zero-shot CoT .222; "Informing Asymmetry" .367 best; forced disclosure 96.7%. N=3 .167 to .514, N=4 .072 to .321, N=7 .017 to .023 | c13, d06 | Single-source |
| Scale does not predict pooling | Gemini-2.5-Pro .671, Flash .550, Flash-Lite .394; GPT-5 variants no better than GPT-4.1-Mini | c14 | Single-source |
| Teamwork ability tracks capability | 18 models, 240 tasks; one component 71% of variance in 8 scores; r .92 with intelligence index (CI .87 to .97; 85% variance); same-capability models differ by up to 11 points; conflict handling r -.34 with capability; best deal only 14% of conflicts | Wu 2026 (c15 to c17) | Single-source |
| Multi-agent systems fail often | 1,642 traces, 7 frameworks, failure 41% to 86.7%, 14 modes in 3 categories, kappa .88 | Cemri 2025 (c22) | Single-source |
| No society-scale CI | Over 2 million agents: 98.4% of posts no comments; 35 commented posts scored 11.4% individual, 8.6% joint vs frontier 14.3 to 20.0%; of 111 comments 76.5% superficial, 3.6% correct reasoning | Li 2026 Superminds (b25, d18) | Single-source, uncontrolled platform |
| Human-AI IRT | 667 people; GPT-4o +29 points, Llama-3.1-8B +23; solo ability and AI-collaboration ability distinct; ToM predicts success with AI | Riedl and Weidmann 2025 (c24) | Project page only |

## 4. Mechanisms and models

This section says how each model works, in enough detail to implement it on our bench.

### 4.1 How c is measured (psychometric pipeline)
1. Choose a battery of 5 to 12 tasks spanning McGrath quadrants (generate, choose, negotiate, execute). Tasks must have comparable, reliable scores.
2. Run each group on every task. Standardise each task score across groups (z-scores).
3. Compute the inter-task correlation matrix. Report the mean r and the share of positive pairs (Rowe: about 90% positive).
4. Extract a first factor. Three methods are in use and give different shares: (a) first eigenvalue share of the correlation matrix (Woolley headline 43-44%); (b) principal axis factoring (31-35% on the same data); (c) meta-analytic one-factor CFA with average variance extracted (Riedl 44% reported, Rowe 30%). Always state which.
5. Retention rule (Woolley): keep factors with eigenvalue above a parallel-analysis threshold (1.38 in the original); check first is at least twice second.
6. Fit a one-factor CFA. Report chi2, df, CFI, RMSEA. Woolley got CFI .98 to .99. Graf got CFI .73 (bad). Zhou got CFI .967.
7. The c score: average of weighted z-scores (Riedl), scaled to mean 100, SD 15. Zhou does the same and calls it ACI.
8. Validate: leave-one-task-out. Build c from all tasks but one, correlate with the held-out task (Riedl mean r .40; Zhou r above .8 on three tasks, about .5 on two).
9. Control: regress the held-out task on c and on average and maximum member score together. The g-vs-c question is whether c keeps a coefficient. (Woolley: yes; Bates and Gupta: no.)

Known artifacts to guard against (b13, b14, b19, d08): part-whole inflation (c is built from the tasks it is tested against), tasks whose group score is an average of separate individual answers, low-effort participants, nesting of groups within studies, one task family from one platform.

### 4.2 Process model of what raises c (human)
- Social sensitivity: average RME of members, or the minimum RME (weak link, Meslec beta .49 for min vs .19 for max). Implementation for humans: administer RME (36 items). For LLMs there is no direct equivalent; the closest operational form is Wu 2026's task where a teammate holding a key fact withdraws (c18).
- Turn-taking: SD of speaking time across members. Low SD goes with high c in correlational data. Implementation: log tokens or turns per agent; compute SD (Zhou uses variance of node degree as a proxy).
- Skill congruence (Riedl, Zhou): the correlation between each member's ability and how much weight or connectivity they get. In LLM groups: rank agents by solo score, then compute the correlation with node degree or message share. Zhou found this over 50% of random-forest importance.
- Communication amount: more total communication goes with higher c in humans (b03). Not tested at equal tokens in LLMs.

### 4.3 LLM group generator used by Zhou 2026 (d03)
- Framework: multi-agent debate (Du et al. 2024 style).
- Factors varied: group size 3/5/8; rounds 2/3; topology decentralised, centralised, random; homogeneous or mixed models.
- Models: gpt-3.5-turbo-0125, gpt-4o-mini, Qwen2.5-7B/32B/72B, glm-4-9b-chat, internlm2.5-20b-chat, gemma-2-27b-it.
- Tasks: commonsense, math, games, coding, writing.
- Per-agent ability g: mean score on tasks, scaled to IQ-like scale (Qwen2.5-72B 119.9; internlm2.5-20b 92.1).
- ACI predictor: random forest on group indicators (skill congruence, mean g, max g, size, effort). 2-fold CV R2 above .8 for ACI, above .6 on most tasks (c06).
- Use as design tool: predicted ACI added as a regulariser to GPTSwarm and G-Designer topology optimisation (c07).

### 4.4 Information-theoretic emergence (Riedl 2026)
- Game: N agents each guess a number without direct communication; success depends on the group sum (Goldstone-style guessing game).
- Measures: synergy (information in the whole not in any part, order-2 only) and redundancy (aligned information). Computed from agent output time series with partial information decomposition.
- Arms: Plain, Persona (each agent gets an identity), Persona+ToM (adds "think about what other agents might do").
- Result: synergy x redundancy interaction .24 (p .014). ToM did not raise overall success in the powered test (200 groups per arm).
- Implementation cost: needs a time series per agent and a PID library; this is a diagnostic, not a scaffold step.

### 4.5 Two-stage exchange (Li, Naito, Shirado 2026, d05)
Exchange phase (2 rounds): each agent shares 1 to 2 decision-relevant facts it holds, plus one reason the current front-runner may be wrong. Decide phase (1 pass): each agent summarises evidence and uncertainty and votes. In code: the program collects shared facts into a common pool, redistributes it, then runs the vote. Lifted GPT-4.1 from .037 to .800 on 18 tasks.

### 4.6 Scaling-law style predictor (Kim 2026, c20, c21)
- Inputs per configuration: single-agent baseline accuracy (PSA), number of agents, architecture type, tool count, capability metric.
- Interaction: PSA x log(1 + agents) beta -0.236. Cross-validated R2 .373 (.413 with capability metric).
- Use: before spending on multiple agents, measure single-agent accuracy on a sample. If above about 45%, stay single. If below and the task is decomposable (finance-style), multi-agent can pay (+80.8% best case).
- Error amplification by architecture: single 1.0, centralised 4.4, hybrid 5.1, decentralised 7.8, independent 17.2.

### 4.7 Debate as martingale (Choi 2025, b24)
Belief updates among homogeneous agents form a martingale, so debate adds no expected accuracy. Voting captures the sampling gain. Implementation: majority vote over N samples is the baseline any debate design must beat at equal tokens.

## 5. What holds up

### 5.1 Holds up
- A positive manifold of group scores exists in most samples that use similar tasks. About 90% of pairwise correlations are positive (Rowe, b09). Mean r about .27 (Riedl) to .28 (Woolley).
- A first factor of 30 to 50% (depending on method) appears in many samples, including the independent Bates and Gupta Study 1 (39.8%, 26 groups).
- c predicts a held-out task with r about .26 (Rowe) to .40 (Riedl leave-one-out). It is moderate, not strong.
- Group process variables (skill congruence, strategy) matter more than individual skill on coordination tasks. Individual skill matters more on puzzle tasks (Sudoku: 51%).
- Group size does not drive c (Riedl 2021; Zhou 2026, under 5% importance).
- More agents in LLM groups often hurts, and the 45% single-agent boundary appears in Kim 2026 under matched tokens (d02). Tran and Kiela at equal thinking tokens find single agents best or tied for 500 to 5,000 tokens (d01).
- Voting beats debate on most benchmarks tested (b24).
- Hidden-information pooling fails in LLM groups and in humans (30.1% vs 80.7% LLM; .385 vs .604 humans).

### 5.2 Replications and failed replications
| Attempt | Sample | Result | Source |
|---|---|---|---|
| Woolley 2010 Study 2 | 152 groups | c found (same team) | a04 |
| Engel 2014 | 68 groups, face-to-face and online | c found, RME .53 and .55 | b01, b02 |
| Engel 2015 | 68 + 25 + 116 groups, US, Germany, Japan | c found (second-hand) | b20 |
| Meslec 2016 | 30 Dutch groups, chat | c found, weak-link rule | b17 |
| Kim 2017 | 248 League of Legends teams | c predicted later play (second-hand) | b18 |
| Bates and Gupta 2017 | 26 + 40 + 40 groups | One factor 39.8% in Study 1, but IQ explains about 80%; RME, gender, turn-taking not supported | b04 to b07 |
| Barlow and Dennis 2016 | 86 virtual groups | c rejected (second-hand; paper paywalled) | b19 |
| Credé and Howardson 2017 | 6 published samples reanalysed | Support weak (press summary only; per-sample numbers unread) | b13, b14 |
| Woolley, Kim, Malone 2018 reply | n/a | Authors dispute artifact reading, agree on better measures (not opened) | b15 |
| Graf et al. 2019 | 745 teams, 13 studies | Mean r .001; one factor poor; three factors | b12, d07 |
| Dyads 2025 | 105 dyads | c driven by individual intelligence (beta .33) and confidence (.32); social sensitivity .22 held; turn-taking and gender did not | a15 |
| Riedl 2021 | 22 studies, 1,356 groups | c found; same research network, single platform | a08 |
| Rowe 2021 | 19 samples | Pooled c weak to moderate; independent attempts mostly fail | a12, a13 |

Pattern: studies from the Woolley network always find c; independent studies find a factor of 30 to 40% in some and none in others. Rowe notes only 7 of 19 samples were independent (a12). Source independence of the "established" claims is therefore lower than the study count suggests.

### 5.3 Moderators and boundary conditions
- Medium: Graf's authors say correlations are consistently larger face-to-face than computer-mediated (d08). But Engel found equal c online and face-to-face.
- Task type: pooled across five McGrath task types, c disappears (Graf). Task-structured effects in LLM systems (Kim: +80.8% decomposable, -70.0% sequential).
- Task structure for dyads: c appears for well-structured single-answer tasks (a15).
- Power: groups under 30 give wide intervals; Bates and Gupta Study 1 had 58% power for the reported social-sensitivity effect (d13).
- Ceiling: Raven items hit ceiling in Bates and Gupta Study 3, which weakens the intervention test (d11).
- Coordination structure can create c: in a thesis experiment (65 groups) c appeared only in the coordination-structured arm (r with criterion .339, p .026; b19, second-hand).
- Model capability: Riedl 2026 says capable models show coordination; Llama-3.1-8B largely fails (c10). Choi 2025 uses small models only.
- Group size in LLM hidden profiles: gains shrink as N grows (N = 3: .167 to .514; N = 7: .017 to .023; d06). Rows for N = 5 to 7 rest on 5 tasks each.
- Range restriction: Woolley's college sample could shrink IQ correlations. Bates and Gupta rebut this (Wonderlic mean 17.0 range is wide; limits text in b05).

### 5.4 Interventions that worked or did not
Worked:
- Structured fact sharing plus doubt, then decide (hidden profile): .037 to .800 (GPT-4.1), +.55 to +.70 in the three models tested (d05). Forced disclosure of all facts gave 96.7% (c13).
- "Informing Asymmetry" prompt: .367 (best prompt, far below full profile) (c13).
- One adversarial agent among helpers helped; more adversaries hurt (c13).
- Hub-and-spoke with the strongest model at the hub, often better and cheaper than all-to-all (c05).
- Majority vote over N samples (b24).
- Predicted-ACI regulariser: +1.1% to +12.3% in topology search (c07).

Did not work or not shown:
- Equal-talk or empathy instruction in human groups: F(2,34) = 1.14, p = .33 (d11). Authority instruction beta -.42 (p .14).
- Video vs audio manipulation changed turn inequality but not CI (p = .22) (d14).
- Theory-of-mind prompt on LLM groups: no change in overall success (200 groups per arm); emergence share fell from 37% to 18% (d15).
- Conflictual prompt: .017 (c13). More rounds: peak at 15 rounds (.233), lower at 20 (.133).
- More agents: hurts above the 45% boundary; GPT-4.1 odds x0.92 per member.
- Debate over vote (b24).
- Scale and stronger model alone: a 72B group cost 75% more and had 9.7% lower ACI (c05); GPT-5 variants no better than GPT-4.1-Mini on pooling (c14).
- Mega-scale society: no CI at 2 million agents (d18).

## 6. Language models

### 6.1 Single-model baseline
LLMs as a population show a stronger general factor than humans do. 591 models, 12 benchmarks: mean inter-test r .73 (humans .45 to .50), 65.6% first factor, omega hierarchical .94 (a16). Parameter count correlates with the factor r = .54 (CI .48 to .59), with diminishing returns. Rows are non-independent (fine-tunes and merges share bases) and contamination is possible (a16, d17). The factor is across models on public tests, not across prompts or scaffolds of one model (d17). Nobody has tested a "scaffold factor" for one model (K27).

### 6.2 Do LLM groups have a c factor?
Only one study (Zhou 2026, ACL Findings) tests it directly (c01 to c07, d03, d04).
- 108 groups, 8 LLMs from 5 providers (3 Qwen), 5 tasks, debate framework.
- Mean inter-task r .55; first factor 66.3%; second 18.7%; CFA CFI .967.
- Compared with human 0.28, but that figure comes from other tasks and designs, so the gap is suggestive only.
- Predictors: skill congruence over 50%, mean g 37%, the rest under 5% each.
- Weaknesses: groups are reshuffled copies of 8 models; "process" is graph structure; skill congruence is computed from the same task scores (circular); 2024-era small models; no seeds reported; 2-fold CV on one generator.
- No replication by another lab and no LLM study with Woolley's original battery was found (c29).

### 6.3 What the other LLM studies say, task by task
- **More agents.** GPT-4.1 guessing game: odds x0.92 per extra member (a20). Hidden profile gain falls with N (d06). Kim: above 45% single-agent accuracy, negative returns, beta -0.236; at matched 4,800 tokens. PlanCraft sequential planning -39.1% to -70.0%; SWE-bench Verified -2.1% to -14.9%; Workbench +5.6% to -1.2%; Finance Agent (single .349) up to +80.8% (the 73% to 81% range). Tran and Kiela: single agent .418 vs ensemble .333 at 1k thinking tokens; at 100 tokens single .290 vs debate .370.
- **Debate vs vote.** Vote beats debate (b24). Our SCHEMA G9 already says this.
- **Theory of mind.** Prompt-level ToM did not raise success in a 600-run test (d15). Explicit belief text raised ToM inference accuracy in a 3-agent game but with three trials per condition (d16). K17 stays contested.
- **Information pooling.** Fails by default (30.1% vs 80.7%); structured exchange fixes it (.037 to .800) on 18 tasks, cost not reported. Humans fail too.
- **Teamwork skill.** One component, 71% of variance, r .92 with capability, but same-capability models differ by up to 11 points (c15 to c17).
- **Failure modes.** 41% to 86.7% of traces fail; causes are design, misalignment, weak verification (c22).
- **Scale.** 2 million agents show no CI (d18).
- **Human-AI.** Combinations worse than the best alone on decisions (g -0.27) (b21). Not LLM-group data, and mostly pre-LLM.

### 6.4 What changed performance, by how much (LLM)
| Change | Effect | Source |
|---|---|---|
| Add structured exchange + decide | +.55 to +.76 absolute on hidden profile | d05 |
| Forced fact disclosure | 96.7% | c13 |
| Informing Asymmetry prompt | .367 vs about .22 baseline | c13 |
| Majority vote vs single | +.05 to +.12 absolute | b24 |
| Vote vs debate | +.03 to +.05 absolute | b24 |
| Strong hub topology | better than all-to-all in most cases, lower cost | c05 |
| ACI regulariser | +1.1% to +12.3% | c07 |
| ToM prompt | 0 on success (200/arm) | d15 |
| Add one agent | odds x0.92 | a20 |
| Raise temperature one unit | odds x1.50 (preliminary grid) | a20 |
| Single agent above 45% baseline | MAS -2% to -70% | d02 |
| Equal thinking tokens 1k | single .418 vs best multi .388 | d01 |

## 7. What our agent should take

Overall: c is background. The founding result is contested in humans and the LLM version is single-source. Nothing about c itself belongs in SCHEMA.md. What the LLM-group work adds is mostly support for guardrails already in the schema.

### Add now (established)
| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| 1 | Keep G9 (no debate). Majority vote of independent samples captures the gain credited to debate. | G9, G4, O (sample-and-vote) | [E] already in schema; new evidence: b24, d01 at equal tokens | b24, d01, d02, a20 |
| 2 | Keep G7: every multi-agent element must beat the single scaffolded agent at equal tokens. Matched-token tests show single is best or tied from about 500 to 5,000 thinking tokens. | G7 | [E] | d01, d02, c21 |
| 3 | Gate by single-agent accuracy. If the plain model already passes about 45% on a problem class, do not add agents. Treat 45% as a fitted boundary, not a law. | G12 (spend by difficulty) | [E] for the direction; the 45% number is [S] | c21, d02 |
| 4 | Report the factor-share method with any cross-task statistic we compute (first eigenvalue, principal axis, or AVE) and use identical tasks across runs. | Run log (section 6 of schema) | [E] | a04, d10, b09, d08 |
| 5 | Verification and information checks beat extra agents: multi-agent failures come from design, misalignment and weak verification. Already covered by G2 and G3. | G2, G3 | [E] | c22 |

### Test first (not established)
| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| 6 | A structured shared-facts step ("share 1 to 2 decision-relevant facts plus one doubt, then decide") when information is split across sub-contexts. | memory / sharing, O3 decompose merge step | [S] | d05, c11, c13 |
| 7 | Hub-and-spoke (one strong coordinator) over all-to-all when several sub-agents are used. | G9 context; O3 | [S] | c05, a19 |
| 8 | Task decomposability classification at S0 before deciding single vs multi-agent. | S0 gate | [S] | c20, c21 |
| 9 | Explicit perspective-taking step ("what do other agents hold or believe"). Powered test found no success gain. | O (new) | [C] leaning null | d15, b23, d16 |
| 10 | Turn or message balance forcing between sub-agents. No causal evidence even in humans. | O | [C] leaning null | d11, d14 |
| 11 | Cross-task general factor for a single agent with different scaffolds (a "scaffold factor"), used as a diagnostic rather than a step. | Whole schema (diagnostic) | [S] absent | d17, K27 |
| 12 | Mixed-model sub-agents (strong and weak) with strongest as hub. | G (member diversity) | [S] | a18, c05, c16 |

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens (reasoning plus all agent calls plus setup), at least 50 runs per arm, and 30 or more items per class. Seeds are fixed and shared across arms. Report mean difference with a bootstrap 95% CI.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Hidden-profile style items (split facts across 3 to 4 sub-contexts), 30 items | A: scaffolded agent with free-form multi-agent talk. B: same with two-stage exchange then decide. C: single scaffolded agent given the full profile at equal tokens | Accuracy | B above A by 0.3 or more absolute (d05 reports +0.55 to +0.76); C is the ceiling reference. Net of token cost, B should still beat A |
| T2 | Mixed ARC and BRAINTEASER items stratified by plain-model accuracy: below 30%, 30 to 60%, above 60% | A: single scaffolded agent. B: N = 3 independent samples plus code vote. C: N = 3 agents with hub coordinator | Accuracy per stratum at equal tokens | A at or above B and C above 45% plain accuracy (Kim beta -0.236). B above A below 30% (Finance-style). Crossover near 45% |
| T3 | Same items as T2 | Vote of N samples vs N-agent debate | Accuracy at equal tokens | Vote at or above debate by 0.03 to 0.05 (b24) |
| T4 | Multi-agent items with a ToM line | A: sub-agents with no perspective line. B: sub-agents prompted to state what the others know | Accuracy; 200 runs per arm to match Riedl | Zero difference expected (d15). Adopt only if B beats A by at least 3 points with CI above zero |
| T5 | Scaffold factor: 6 scaffold variants (plain, CoT, best-of-N, our scaffold, scaffold minus one operator, scaffold with different budget) on one model across 8 task types, 30 items each | Compute 6 x 8 score matrix | Mean inter-task r across tasks; first factor share by eigenvalue and by principal axis; leave-one-task-out r | If first factor share is over 50% and leave-one-out r over .5, scaffold quality is a general trait; if under 30%, the effect is task-specific and per-class routing (S0) matters more |
| T6 | Same items; sub-agent pool of mixed strong and weak models | A: homogeneous strong. B: mixed, strong as hub. C: mixed, fully connected | Accuracy and tokens | B within 2 points of A at 20% or more lower cost (c05) |
| T7 | Turn balance: sub-agents write one at a time | A: free order. B: forced equal message length and turn count | Accuracy at equal tokens | Zero expected; test only if budget allows |
| T8 | Decomposable vs sequential item sets (code tasks vs planning puzzles) | Classifier at S0 routes decomposable items to multi-agent | Accuracy gain over always-single | Positive on decomposable (Kim +80.8% best case), negative on sequential if forced multi |

## 9. What does not transfer, and why

- **Social sensitivity (RME).** It measures reading facial expression of humans. LLM agents have no eyes or empathy trait to vary. The closest analogue (belief-state text) has only underpowered evidence (d16).
- **Proportion of women.** A human demographic with no counterpart in an agent pool. Not even robust in humans (K06).
- **Turn-taking from sociometric badges.** Humans have limited speaking time; LLM agents can all write at once and turn count is a design parameter, not a social behaviour. Causal evidence is null even in humans.
- **Group IQ vs member IQ.** Our agent is one model with a scaffold. There are no "members" with different IQ to average.
- **Face-to-face vs online.** No analogue for agents.
- **Cohesion, motivation, satisfaction.** These did not predict c and have no agent counterpart.
- **POGS online platform tasks.** Typing and unscrambling words are not our bench tasks.
- **Zhou's ACI.** It is built over a pool of 8 different LLMs that we do not use. Its drivers (skill congruence and node degree) are properties of a network of different-strength models. A single-model scaffold has no such network.
- **Human-AI synergy.** Mostly pre-LLM and measures human decision makers (b21).
- **Society scale.** 2 million agents on an open platform (d18) has no bearing on a single-agent scaffold.
- **Group effects of social loafing, conformity, status.** Not tested in any source found and probably absent in LLM samples from one model, because they share weights (G4: samples from one model are not independent).

## 10. Open questions

1. Does an LLM-group general factor survive when members come from disjoint model sets, and after controlling for mean member capability? (Gap 1; Zhou used 8 models from 5 providers; partial control only.)
2. Where exactly is the crossover between single scaffolded agent and N agents at equal tokens? The 45% value is a fit over six benchmarks, not a sweep over one task at varied difficulty. (Gap 2)
3. Is there a "scaffold factor" for one agent? (Gap 9, K27)
4. What is the first-factor share on Riedl's pooled data by Woolley's method? Not answerable from the main text. The arithmetic suggests about 27%, not 44%. SI and 2022 correction unread. (Gap 4)
5. Which is right, g or c, after correcting for reliability and task ceilings? No preregistered large replication exists. (Gap 5)
6. Why does c vanish in Graf and Barlow and Dennis: task-type mix, computer mediation, or scoring rules? Barlow and Dennis was paywalled. (Gap 6)
7. Does the hidden-profile fix survive on more than 18 tasks, and what is its token cost? (Gap 7)
8. Is turn equality causal for LLM groups? No study. (Gap 8)
9. Does Zhou's ACI replicate with different frameworks (not debate), larger models and 2025 to 2026 reasoning models?
10. Does a verification or critic step help differently on decision vs creation tasks, as Vaccaro (g -0.27 vs +0.19) suggests for human-AI? Untested for LLM groups.
11. The Riedl 2026 temperature effect (x1.50 per unit) comes from a preliminary grid and not the main 600 runs. Is it exploration or something else?
12. Sources only seen as snippets (b13, b15, b16, b27, b28, c27, c28, c29, a23, Vaccaro g values, Engel 2015, Kim 2017) should be opened before anything here is quoted outside this folder.

## 11. Sources

[V] opened this session; [M] snippet or abstract only. Status is from the evidence files and critique re-opening.

**Human c factor**
1. [V] Woolley, Chabris, Pentland, Hashmi, Malone (2010) Evidence for a collective intelligence factor in the performance of human groups. Science 330. https://www.gwern.net/doc/iq/2010-woolley.pdf (a01 to a07). Official page https://www.science.org/doi/10.1126/science.1193147 [M] (b28, 403).
2. [V] Engel, Woolley, Jing, Chabris, Malone (2014) Reading the Mind in the Eyes or reading between the lines. PLOS ONE. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115212 (a10, a11, b01 to b03).
3. [V] Riedl, Kim, Gupta, Malone, Woolley (2021) Quantifying collective intelligence in human groups. PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC8166150/ (a08, a09, c25, d09, d10). Abstract only [M]: https://doi.org/10.1073/pnas.2005737118 (b16).
4. [V] Rowe, Hattie, Hester (2021) g versus c: comparing individual and collective intelligence across two meta-analyses. Cognitive Research. https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-021-00285-2 and https://pmc.ncbi.nlm.nih.gov/articles/PMC8019454/ (a12 to a14, a24, a25, b08 to b11, b19).
5. [V] Bates and Gupta (2017) Smart groups of smart people: evidence for IQ as the origin of collective intelligence in the performance of human groups. Intelligence. https://www.gwern.net/doc/iq/2016-bates.pdf (b04 to b07, d11 to d13).
6. [V] Graf, Gimpel, Barlow (2019) Clarifying the structure of collective intelligence in teams: a meta-analysis approach (work in progress). https://www.fim-rc.de/Paperbibliothek/Veroeffentlicht/1043/wi-1043.pdf (b12, d07, d08).
7. [V] Meslec, Aggarwal, Curseu (2016) The insensitive ruins it all. Frontiers in Psychology. https://www.frontiersin.org/articles/10.3389/fpsyg.2016.00676 (b17).
8. [V] Janssens, Meslec, Leenders (2022) Collective intelligence in teams: contextualizing collective intelligent behavior over time. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2022.989572 and https://pmc.ncbi.nlm.nih.gov/articles/PMC9659728/ (b18, b20, a23; only abstract and introduction read for a23).
9. [V] Tomprou, Kim, Chikersal, Woolley, Dabbish (2021) Speaking out of turn. PLOS ONE. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0247655 (d14).
10. [V] A recipe for dyadic collective intelligence for well-structured tasks (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12460217/ (a15).
11. [M] Credé and Howardson (2017) The structure of group task performance: a second look. Press summary: https://www.sciencedaily.com/releases/2017/10/171017124354.htm [V as press only] and https://academicnewsletter.sufe.edu.cn/info/370165 (b13, b14).
12. [M] Woolley, Kim, Malone (2018) Measuring collective intelligence in groups: a reply to Credé and Howardson. https://papers.ssrn.com/abstract=3187373 (b15, 403).
13. [M] Barlow and Dennis (2016) Not as smart as we think. J Manage Inf Syst 33(3). Known through Rowe only (b19).
14. [M] Engel et al. (2015) CI in computer-mediated collaboration emerges in different contexts and cultures. Known through Janssens (b20). Kim et al. (2017), Mayo and Woolley (2017), Radcliffe 2019, Rogers 2019: titles only via Rowe (a25).
15. [V] Jiang et al. (2025) AI-augmented co-design in healthcare. https://pmc.ncbi.nlm.nih.gov/articles/PMC12729299/ (c26).
16. [V] Vaccaro, Almaatouq, Malone (2024) When combinations of humans and AI are useful. Nature Human Behaviour. https://doi.org/10.1038/s41562-024-02024-1 (b21; PDF only partly readable, g values not re-verified).
17. [V] Riedl and Weidmann (2025) Quantifying human-AI synergy. https://riedlc.github.io/Quantifying-Human-AI-Synergy/ (c24; project page, not the preprint).
18. [M] Burton et al. (2024) How large language models can reshape collective intelligence. Nature Human Behaviour. https://doi.org/10.1038/s41562-024-01959-9 (c28; paywalled).

**LLM and AI**
19. [V] Ilic and Gignac (2024) Evidence of interrelated cognitive-like capabilities in large language models. https://arxiv.org/pdf/2310.11616 (a16, d17).
20. [V] Zhou, Liu, Liu, Wang, Shao, Xu, Jin, Li (2026) Identifying collective intelligence factor in LLM agent groups for generalizable multi-agent systems. ACL Findings. https://aclanthology.org/2026.findings-acl.624.pdf (a17 to a19, c01 to c07, d03, d04).
21. [V] Riedl (2026) Emergent coordination in multi-agent language models. ICLR 2026. https://arxiv.org/abs/2510.05174 and https://arxiv.org/pdf/2510.05174 and https://arxiv.org/html/2510.05174 (a20, b22, b23, c08 to c10, d15).
22. [V] Li, Naito, Shirado (2026) Systematic failures in collective reasoning under distributed information (HiddenBench). https://arxiv.org/abs/2505.11556 and https://arxiv.org/html/2505.11556v4 (c11 to c14, d05, d06).
23. [V] Wu et al. (2026) Measuring AI agents as teammates with collaborative intelligence. https://arxiv.org/abs/2611.02633 (c15 to c18).
24. [V] Kim et al. (2026) Towards a science of scaling agent systems. https://arxiv.org/abs/2512.08296 and https://arxiv.org/html/2512.08296 (c20, c21, d02).
25. [V] Tran and Kiela (2026) Single-agent LLMs outperform multi-agent systems on multi-hop reasoning under equal thinking token budgets. https://arxiv.org/html/2604.02460v1 (d01).
26. [V] Choi, Zhu, Li (2025) Debate or vote. https://arxiv.org/abs/2508.17536 (b24).
27. [V] Cemri et al. (2025) Why do multi-agent LLM systems fail? https://arxiv.org/abs/2503.13657 (c22).
28. [V] Li et al. (2026) Superminds test. https://arxiv.org/abs/2604.22452 (b25, d18; abstract page and part of text).
29. [V] Li, Chen, Hou et al. (2023) Theory of mind for multi-agent collaboration via large language models. https://arxiv.org/pdf/2310.10701 (d16).
30. [V] Ruan et al. (2025) SwarmBench. https://arxiv.org/abs/2505.04364 (c23).
31. [V] Fan et al. (2026) Towards a science of collective AI. https://arxiv.org/pdf/2602.05289 (a21; front matter and appendix headings only).
32. [V] Huang, Zhao, Yi, Xie (2025) On the dynamics of multi-agent LLM communities driven by value diversity. https://arxiv.org/abs/2512.10665 and https://arxiv.org/pdf/2512.10665 (a22, b26, c19).
33. [M] Scofield (2026) Multi-agent constraint factorization. https://arxiv.org/abs/2601.15077 (b27; abstract only; thematic link only).
