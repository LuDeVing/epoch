# Working memory and Gf: deep document

*Subfield A13.03. Built from evidence_a-d.jsonl (a01-a28, b01-b27, c01-c28, d01-d17), claims.jsonl (K01-K28) and critique.md. Evidence ids in brackets. Where a source was only seen as a snippet, recall, or abstract, the text says so. The two named key works are weak: Kyllonen and Christal 1990 was never opened (numbers are second-hand), and Dokic, Koso-Drljevic, Bilalic 2025 was not read at all (no figures; do not cite numbers from it).*

## 1. What it is

Working memory (WM) is the small set of information a person keeps active while doing something with it. Fluid reasoning (Gf) is solving new problems with rules that must be induced on the spot, for example Raven matrices. The question: does the size of the active store set how well a person reasons?

The founding answer (Kyllonen and Christal 1990, "Reasoning ability is (little more than) working-memory capacity?!") was close to yes. Latent WM and latent reasoning factors correlated .80 to .90 in four US Air Force samples [a01, a02, a08]. Thirty-five years of work say: the link is strong, but not identity. The best current figure is a latent r of about .70 to .80 at most, which is 50 to 60 percent shared variance [a26, a09]. The link depends on which tasks are used, whether tests overlap in content, whether testing is speeded, and whether interference is present [a27, a14, a04]. A rival account says the real driver is attention control, not storage [a17, d13]. Causal tests (WM training) mostly fail to move Gf [b01, b02].

Why this matters for our agent. A language model has no fixed WM store. It has a context window, attention, and its own written output. Humans are limited in how many rules and intermediate results they can hold live. The agent analogue is: how many rules, constraints and sub-results it can track at once without an external written state, and where compliance breaks. The human literature gives hypotheses (rule count drives difficulty; interference is the real cost; control matters as much as capacity). The LLM literature (section 6) shows real decline curves, but almost never links them to reasoning scores inside the same model.

Scope notes. Fluid reasoning as a construct is covered by A13.02. The capacity-hypothesis test is A13.04. Item difficulty modelling is A13.07. Chunking, cognitive load and attention-control theory sit in A07/A08 and in the parallel subfields "Attentional control theory and executive functions" and "Working-memory limits and chunking". This document links to them and does not repeat them.

## 2. History and theories in depth

### 2.1 The founding claim (1990)
Kyllonen and Christal tested four large Air Force samples. Second-hand figures: N = 723, 412, 415, 594; 15 reasoning tests; 6 WM tasks; latent r .80 to .90 [a01, a08]. The title ends with "?!" and the authors allowed a reverse causal reading (better reasoners show bigger apparent WM) [a27]. The recall-only version (about .88 often quoted) is not independent of this and was not verified [b11, critique item 3].

Limits flagged by two independent reviews [a27, a08, a02]:
- The WM battery was chosen from a vague definition. Conway et al. say the authors picked varied-content, varied-process tasks because no task theory existed.
- Content overlap. An arithmetic reasoning test appeared in all four samples; mental arithmetic in three; numerical assignment in three. Part of the r may be arithmetic skill shared by both sides.
- Correlational design.

### 2.2 The executive-attention turn (1999 to 2003)
Engle, Tuholski, Laughlin and Conway (1999): a latent WM-span factor predicted Gf (latent r .59, per Hagemann 2023). A short-term memory factor added nothing once WM was held. They concluded that controlled attention (the central executive) drives the link [a10, snippet level]. Conway et al. 2002 gave WM to Gf about .60 and showed STM and speed add little (N about 120, recall only) [b14].

Conway, Kane, Engle (2003) review [a02, a03, a04]:
- Complex span (storage plus processing, e.g. operation span) loads a factor that predicts g. Simple span (digit span, word span) does not. Complex-span alphas .70 to .80, intercorrelations only .40 to .60.
- High-span people beat low-span people only where interference or response competition exists. In a Sternberg-style scan with overlapping letter sets, the RT slope on set size was steeper for low WMC only when each letter belonged to two sets. With no overlap the slopes did not differ.
- Conclusion: WMC accounts for at least one-third and perhaps one-half of the variance in g.

### 2.3 The meta-analytic pushback and the reply (2005)
Ackerman, Beier, Boyle (2005): 86 samples, true-score WM-g r = .479 (CI .44 to .52 not re-verified); WM and intelligence are "related but distinct" [a11, a09]. Colom 2006 quotes .36; that is the WM-Gf figure, a different quantity (critique item 1) [a06, b12]. Kane, Hambrick, Conway (2005) replied: reanalysis of 14 data sets from 10 published studies, more than 3,100 people, median latent r = .72, about 50% shared variance (abstract-level, critique item 2) [a09, b13]. Oberauer et al. (2005) reanalysis gave r = .85 [a09]. The gap is mostly measurement: single tasks versus latent factors, weak versus pure batteries. Colom's own range-restricted sample (N = 229 air-traffic applicants) gave WM-intelligence r = .20 (.27 corrected) [a05].

Raw one-task correlations are small. Raven versus computation span r = .24; Raven versus mental counters r = .32 [a06]. Engle 1999: WM versus Raven/CFT raw r .24 to .34 [a10]. Executive measures correlate weakly with WM span (dual-task cost .15; random number generation .14 to .18) [a07].

### 2.4 Item-level theory: Carpenter, Just, Shell (1990)
Production-system models FAIRAVEN and BETTERAVEN solve Raven by finding correspondences, holding rules in a WM buffer, and generating the missing cell. Difficulty rises with the number of rule tokens and with goal management. Rule tokens explained 57% of item variance (as cited by Little 2014; original not opened) [a12]. This is the closest human result to "limits on holding many rules".

Little, Lewandowsky, Craig (2014) [a13]: older studies found the WM-Raven link flat across item difficulty, which seemed to refute Carpenter. Simulation (population r .10, .30, .50, .70, .80, .90; 10,000 replications) shows flat slopes appear when overall r is low, so invariance tests have low power. With a better composite WM measure the link rose with item difficulty. Status: contested (K05).

### 2.5 Speeding, attention control and competing orders (2013 to 2026)
- Chuderski (2013): time pressure raises the WM-Gf link. Study 1 N = 1,377 aged 15 to 46; speeded group 20 min, unspeeded 60 min; WM explained 38% of variance unspeeded; near-isomorphic under heavy speeding. Only a blog summary was opened [a14].
- Draheim et al. 2021/2022: N = 396; each construct from three tasks; the WM-Gf path was no longer significant once attention control was added, but full mediation appeared only with reliable accuracy-based control tasks [a17]. Burgoyne and Engle (2020) call attention control (maintenance plus disengagement) the common thread of Gf, WMC and sensory discrimination [d13, abstract only].
- Kane et al. (2016): N = 541 analysed; 6 WMC tasks, 5 restraint, 5 constraint tasks. WMC, restraint, constraint, mind wandering and RT variability are correlated but separable. WMC links most to restraint (stopping prepotent responses). Restraint-constraint 95% CI [.46, .74] [b10; the Crossref copy d15 was not opened].
- Unsworth et al. (2014): N = 164. Neural delay activity (CDA) correlates with Raven r = -.28 / -.29. CDA to gF indirect via capacity -.23; via capacity plus attention control -.41; direct path then not significant [b07].
- Cochrane, Simmering, Green (2019): the reverse order. 42 children plus 80 adults. Raven r with spatial span .412 (adults), .414 (children); n-back .383 / .298. Attention-Raven links were fully mediated by WM; attention did not mediate WM-intelligence. Weak exploratory structure (only 2 of 5 eigenvalues passed parallel analysis) [b05, b06, a18].
- Lee and Engle (2026 preprint, abstract only): avoiding re-testing rejected hypotheses is predicted by Gf, which absorbs the WMC effect; only selective attention predicts resampling [d14].
- Robison et al. (2023): over 1,000 people, 4 studies. Task-evoked (phasic) pupil response tracks WMC, attention control and Gf (latent r complex span-visual arrays .56; attention control-phasic .68). Resting arousal accounts got no support [b08]. Ruuskanen et al. (2024) failed to replicate baseline-pupil claims: N = 224 for Gf, r = -.01, BF01 = 11.6; WM r = .05, BF01 = 7.26 (N = 102); attention control r = .11, BF01 = 4.58 [b09].

### 2.6 Process overlap theory
Kovacs and Conway (2016): the WM-Gf correlation arises because tests of both draw on many overlapping processes, not one capacity. The paper was not opened (recall only) [b27]. Indirect support: a connectome study (N = 297) found global connectivity predicts g better than localised accounts, which fits overlap-type theories; no effect sizes extracted [d16].

### 2.7 Experimental load on Raven (Hagemann et al. 2023)
Load the central executive, phonological loop or sketchpad while people solve APM items. Study 1 N = 60 (mean age 22.45). Executive load cut APM scores, but modestly compared with the effect on span tasks. Title claim: Gf is "much more than" WM capacity. Read: capacity is one strand, not the whole [a15, a08].

### 2.8 Causal route: training
Jaeggi et al. 2008 (N = 70, mean age 25.6, 8 to 19 days of dual n-back, about 25 min a day) reported matrix-test gains [b25, b26; Wikipedia-level only]. Replications failed: Chooi and Thompson 2012, Redick et al. 2013, Thompson 2013 [a16, b25]. Meta-analyses are in section 5.

### 2.9 Where the field stands
The 2018 benchmark view (Oberauer) and Colom 2015 "quasi-isomorphism": 50 to 60 percent shared variance, r up to .70 to .80 at the latent level [a26]. About half of WM capacity variance is heritable and largely shared with Gf (Wikipedia-level) [b24]. Relational complexity (Halford): performance falls to chance near five interacting variables, read as a limit of about four [b24, Wikipedia-level].

## 3. Core findings with exact numbers

Status: Established = at least two independent sources or a meta-analysis. Single = one source. Contested = sources disagree. Weak = snippet or recall only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Founding latent WM-reasoning correlation | .80 to .90; 4 USAF samples N = 723/412/415/594; 15 reasoning tests, 6 WM tasks | K&C 1990 via Conway 2003, Hagemann 2023 [a01, a08] | Weak (never opened; inflated by overlap) |
| Content overlap inflates the headline | arithmetic reasoning in 4 of 4 samples; later designs give .58 to .72 | [a27, a08, a02] | Established (K02) |
| Meta-analytic WM-g | 86 samples, true-score r = .479 | Ackerman et al. 2005 [a11] | Established (abstract level) |
| Latent WM-Gf reanalysis | median r = .72, 14 data sets, >3,100 people | Kane et al. 2005 [a09, b13] | Established |
| Other latent values | .59 (Engle 1999); .60 (Conway 2002); .85 (Oberauer 2005) | [a10, b14, a09] | Established range |
| Field benchmark | 50 to 60% shared variance; r up to .70 to .80 | Oberauer 2018 via Hagemann [a26] | Established |
| WMC accounts for 1/3 to 1/2 of g variance | review conclusion | Conway et al. 2003 [a02] | Established |
| Complex span predicts Gf, simple span does not | complex alpha .70-.80, intercorrelations .40-.60 | [a03] | Single (K03) |
| Interference moderates the capacity effect | low-WMC slope steeper only with overlap | [a04, a13, a12] | Established (K04) |
| Range restriction shrinks the link | r = .20 (.27 corrected), N = 229 | Colom et al. 2006 [a05] | Single |
| Rule count explains Raven difficulty | 57% of item variance in rule tokens | Carpenter 1990 via Little 2014 [a12] | Contested (K05) |
| Humans: more unique rules is harder | OR = 0.61, p = .0047; progression rules OR = 0.41, p = .0001 | Webb et al. 2023, N = 40 [c22] | Single |
| Speeding raises the link | 38% variance unspeeded, N = 1,377 | Chuderski 2013 [a14] | Single, blog level |
| Attention control absorbs WM-Gf | N = 396; WM-Gf path non-significant with AC | Draheim et al. [a17] | Established with caveats |
| Restraint and constraint separable | CI [.46, .74], N = 541 | Kane et al. 2016 [b10] | Established |
| CDA predicts gF by two routes | via capacity -.23; plus control -.41; N = 164 | Unsworth et al. 2014 [b07] | Single |
| Baseline pupil unrelated to Gf and WM | r = -.01, BF01 = 11.6, N = 224 | Ruuskanen et al. 2024 [b09] | Contested (K08) |
| WM training, far transfer to Gf, active controls | g = 0.05 [-0.02, 0.13], k = 67; passive g = 0.20 [0.11, 0.28], k = 53 | Melby-Lervag 2016 [b01] | Established |
| WM gain does not predict Gf gain | beta = -.01, p = .86, k = 26 | [b02] | Single causal test |
| Dual n-back null vs active control | BF for null 39.97:1; 57 analysed | Lawlor-Savage 2016 [b03] | Single |
| Training meta-analytic dispute | Au g = 0.24 (not re-read) vs 0.05; control type Q(1) = 6.09, p = .01 | [b04, d10, d12] | Contested (K28) |
| ChatGPT n-back limit | d' about 1 at n = 3 | Gong et al. AAAI 2024 [a19] | Established (one group) |
| Weak open models fail 2-back | Qwen1.5-14B 1.00/.09/.08; Llama3.1-8B 1.00/.14/.17 at 1/2/3-back | Hu and Lewis [c06] | Single |
| Scale and curriculum extend n-back | Llama-3.1-70B retrieval 75.25/66.08/57.1% at n = 8/9/10; with curriculum 79.83/80.17/71.67 | [c07] | Single |
| Readout bottleneck across LLMs | median d' 2.57 (N=1), 0.91 (N=4), 0.52 (N=6); 15 models, 70M-14B | Gong 2026 [a23] | Established (K13) |
| N-back tracks benchmarks, 10 models | MMLU-Pro .78, GPQA .88, IFEval .69; size not a predictor | Xiong et al. 2026 [d09] | Contested (K14) |
| Forward span perfect, backward fails | forward 50 digits .99-1.00; backward at 15 digits .00 to .83 | de Langis et al. 2025 [c15] | Single |
| Incongruent control weak | 40-60% vs human 93-96%; with reasoning .91-.99 | [c18] | Single |
| Instruction density decay | at 500 rules best about 68%; o3 62.8, grok-3 61.9, claude-3.7-sonnet 52.7, opus-4 44.6, sonnet-4 42.9 | IFScale [d01, b21] | Single (K16) |
| Parallel-branch cliff | 100% through 12 branches, collapse at 20-30 | Patil et al. 2026 [b23] | Established (K17) |
| Rule knowledge does not fix execution | Hanoi collapse at 7-8 disks even with algorithm given | Shojaee et al. 2025 [d06] | Single (K22) |
| External state removes length collapse | 1,048,575 Hanoi steps, zero errors | MAKER [d07] | Single (K23) |
| Chunked status list on state tracking | 96.4%, +35.4 points | Zhang et al. 2024 [d08] | Single |
| Matrix collapse is perceptual, not range | o3-mini 86.6 to 81.0 (range 1000, clean); 17.0 with max noise | Camposampiero et al. 2025 [d05] | Single (K19, K24) |
| Per-attribute query lifts arithmetic | GPT-4 27.1% to 73.6% | Hersche et al. 2024 [d04] | Single (K25) |
| Effective context shorter than claimed | effective 64K for GPT-4 and Llama3.1-70B; 32K Qwen2-72B | RULER [c26] | Single |
| General factor in LLMs | 591 LLMs, 12 tests, positive manifold | Ilic and Gignac 2024 [c27] | Single |

## 4. Mechanisms and models

Each model below is written so an engineer can turn it into a test or a scaffold part.

### 4.1 Carpenter-style rule buffer (FAIRAVEN / BETTERAVEN) [a12]
- Input: a matrix of cells with attributes. Step 1: find correspondences between cells in a row (same attribute, same value or change). Step 2: induce one rule per attribute, one at a time, and push each rule token into a buffer. Step 3: apply all buffered rules to the last row to generate the missing cell.
- Load = number of rule tokens held at once, plus goal management (which attribute is being processed, what is next). BETTERAVEN adds goal management and does better than FAIRAVEN at matching human item difficulty.
- Agent mapping: an item with k interacting rules needs k tokens live. Prediction: if the agent loses rules silently, accuracy falls with k; writing each rule to a state table should remove the k effect. This is a hypothesis, not tested in LLMs (K23 gap).

### 4.2 Interference model of capacity [a04, a13]
- Capacity matters when representations overlap. Model: retrieval picks the strongest cue match; overlapping items compete. Low capacity = weak ability to hold the target while blocking the competitor.
- Engineer view: failure rate = f(overlap), not f(count) alone. Two arms to test: same rule count with distinct attributes versus same count with shared attributes. LLM n-back data match: larger spatial grids (less item overlap) raised measured capacity [c02, b16]; noise symbols lowered it [a19].

### 4.3 Executive attention (Engle, Kane, Draheim) [a10, a17, b10]
- Two sub-abilities: maintenance (keep goal active) and disengagement/restraint (stop prepotent or rejected content). Capacity tasks load both. Attention-control tasks measure restraint directly (antisaccade, flanker-type, visual arrays).
- Engineer view: separate "hold rules" from "suppress the wrong response". In LLMs the second shows as the Stroop/flanker incongruent drop (40-60% vs human 93-96%) which a reasoning step repaired (.91-.99) [c18].

### 4.4 Process overlap theory [b27, d16]
- A test taps several processes. Different tests sample overlapping subsets. g emerges from overlap; a limit applies to whichever process is the bottleneck for the given test (low-ability range: more overlap, stronger link; high-ability range: weaker link). Recall-level only.
- Engineer view and prediction (inference, not a measured LLM result [d16]): if a shared bottleneck exists, one load manipulation should give a common slope across rule tasks. If processes are task-specific, slopes differ by task.

### 4.5 N-back in a transformer [a21, a23, a24, a22]
- Task: stream of letters; output whether the current letter equals the one N back. A decoder transformer needs a head at the current position to attend to position i-N.
- Gong and Zhang 2024: 1-layer 1-head models decline roughly logarithmically to N = 6 (Kruskal-Wallis H = 38.517, p < .001, eta squared = .248). Attention to position i-N grows with accuracy; total attention entropy rises with N. Larger L or H often stay above 95% at all N [a21, c05].
- Gong 2026 (15 pretrained LLMs, 70M-14B): the information is present (linear probes decode target versus lure near perfectly, even on false-alarm trials) but the read-out confuses a lure with the target; lure errors 79% at N = 2. Sharpening attention at readout helps [a23].
- Xiong et al. 2026: "in-context superposition". Memories sit in entangled form. Removing letter-identity directions at the answer position raised accuracy, mostly in weaker models. A trained 2-layer transformer solves it perfectly. Lure effect versus accuracy r = -.51 (autoregressive) [a24, b20, d09].
- Liang et al. 2026: spatial n-back in Qwen2.5 versus Qwen2.5-VL. Text-rendered grids beat image-rendered in all conditions; nominal 2- and 3-back often follows a recency-locked comparison, not the instructed lag [a22].
- Engineer view: the limit in plain models is architectural and interference-driven. Writing the history in the visible output turns a retrieval-from-attention problem into a copy problem.

### 4.6 Task-set drift [c08, a20]
- Hu and Lewis: weak models answer as if m-back with m not equal to n. Gemma-2-27B drifts toward 1-back over a long dialogue and earlier 1-back errors speed the drift. Mean retrieval attention (max): Qwen2-72b 71.98%, Qwen1.5-14b 38.95%, Llama3.1-70b 8.52%, Llama3.1-8b 4.86%.
- Engineer view: the rule is a stateful instruction that decays. A re-stated rule at fixed intervals is the counter-measure (untested at equal tokens).

### 4.7 Working memory in the tokens, not a latent state [c12, c13, c14]
- Huang et al. 2025: models cannot privately commit to a hidden value. Number Guessing (pick 1-10, probe each i, 200 times): the "yes" probabilities should sum to 1; most models sum to 0 (GPT-4o-mini, GPT-4o 2024-05-13 and 2024-11-20, GPT-4.1, Qwen2.5-7B and 72B, DeepSeek-V3). Near 1: GPT-4o 2024-08-06 1.085, Llama-3.1-8B 0.980, Llama-3.1-405B 1.195.
- Yes-No Deduction (twenty questions style): GPT-4o-mini failed 200 of 200; GPT-4o 2024-08-06 failed 173 of 200. Hint plus object cut failures only to 145.
- Math Magic: without CoT GPT-4o-mini 0%, GPT-4o 2.0%, Llama-3.1-405B 26.0%. With CoT or reasoning models: R1 100%, o3-mini 96.7%, QwQ-32B 90.0%, o1-mini 50.0%, o4-mini 36.0% (as listed).
- Engineer view: any state the agent must keep across turns has to be in text. The written trace is the WM.

### 4.8 Human WM strategies moved into prompts (CoT+) [c11, d08]
Zhang et al. 2024 took strategies from interviews with human n-back players: rehearsal (restate the facts so far, trigger "so before that"), chunking (group items per person), a focus cue. On Tracking Shuffled Objects (text-davinci-002) a chunked name(color)-swap status list reached 96.4%, +35.4 points over original CoT. Web of Lies with a code-style prompt 96.4% (+4.8). Temporal Sequence on GPT-3.5: a re-check cue lifted accuracy to 96% (+32.8). text-ada-001 with a short cue reached 25.4% (+15.8). Fancier prompts hurt small models: answer-only beat AutoCoT, plan-and-solve and tree-of-thought for small LMs on BBH [c10]. Old models; not re-run on current frontier models.

### 4.9 Load by instruction density [b21, b22, d01, d02]
- IFScale: 10 to 500 keyword-inclusion rules in a business-report task, 20 models, 7 providers, 5 seeds. Three decay shapes: threshold (reasoning models, e.g. o3, gemini-2.5-pro), linear (gpt-4.1, claude-sonnet-4), exponential (gpt-4o, llama-4-scout).
- Primacy ratio (error in last third / first third) peaks near 150-200 rules, falls to 1.0-1.5 beyond 300. Error type shifts to omission (omission:modification up to 34.88 for llama-4-scout; claude-3.5-haiku row 0.00 at 10 to 31.69 at 500). At 500 rules o3 emits about 1,500 tokens and falls below the coherence score of 6. Latency grows (o3 26 s to 220 s; another model 12.4 s to 436 s at 250).
- Engineer view: if tracking a list, expect omission, and early items favoured. A code-side check of each rule is the natural remedy (G5, STICK).

## 5. What holds up

### 5.1 Replicated and robust
- Latent WM-Gf link is large and well above zero in every latent design (.59, .60, .72, .85, up to .90) [a09, a10, b14]. Raw single-task link is small (.24 to .32) [a06]. Both are true: the number depends on measurement.
- Complex span beats simple span as a Gf predictor [a03; single source in this record, but replicated in Engle 1999 and Conway 2002 as cited].
- Interference as the place where capacity matters [a04, a13].
- Attention control accounts for much of the WM-Gf link (Draheim, Unsworth, Burgoyne and Engle) [a17, b07, d13], although Cochrane 2019 finds the reverse order in a small sample [b05].
- WM training far transfer to Gf against active controls is essentially zero (g = 0.05, k = 67) and the WM-gain to Gf-gain mediation is null (beta = -.01, k = 26) [b01, b02]. Lawlor-Savage 2016 BF 39.97:1 for the null [b03].
- LLM n-back decline with N across many models and papers [a19, a20, a21, a23, a24, c09, a28].

### 5.2 Failed replications and null results
- Jaeggi 2008 dual n-back gain: not replicated by Chooi and Thompson 2012, Redick 2013, Thompson 2013 [a16, b25].
- Baseline pupil size as marker of WM and Gf: Ruuskanen 2024, BF01 11.6 for Gf [b09]. Task-evoked pupil still tracks WM and Gf (Robison 2023) [b08].
- "ChatGPT has a human-like limit near n = 3": partly a comprehension failure. Hu and Lewis show weak models answer a different lag, and 70B models hold to 10-back [a20, c06, c07]. The explanation changed over the series: comprehension, then attention dilution in small models, then readout interference [a28].
- Invariance of the WM-Raven link across item difficulty: seemed to refute rule-count theory, but low power explains the flatness [a13].

### 5.3 Moderators and boundary conditions
- Task purity and content overlap (K&C arithmetic): .80-.90 down to .58-.72 [a27].
- Speeding: more speed, more overlap with WM (38% unspeeded) [a14].
- Sample range: restricted samples give r = .20 [a05].
- Interference/overlap: capacity matters mostly with overlap [a04].
- Task type: complex versus simple span [a03].
- Control type in training meta-analysis: Q(1) = 6.09, p = .01; baseline adjustment; n-back-only scope; adult age 18-50 in Au [d10, d11].
- In LLMs: model scale, curriculum demonstrations, chain-of-thought, spatial versus verbal, grid size, noise, thinking mode, vision versus text [a19, c07, a22, c14].

### 5.4 Interventions that worked
- On LLMs only, with older models: chunked status list +35.4 [d08]; per-attribute queries 27.1 to 73.6 on arithmetic rules [d04]; in-context curriculum for large n-back (79.83 versus 75.25 at 8-back) [c07]; chain-of-thought for spatial n-back [a19]; explicit reasoning for incongruent control (.47 to .91 for Llama-3.1-8B) [c18]; rewriting state each step plus voting (MAKER, zero errors across 1,048,575 steps) [d07]; generated YES/NO checklist +3.8 (Command-R+) and +0.8 (GPT-4o) on LiveBench [d03].
- On humans: none for far transfer to Gf.

### 5.5 Interventions that did not work
- WM training for Gf (humans) [b01, b02, b03].
- Giving the model the algorithm: Hanoi collapse unchanged [d06].
- More thinking effort on noisy matrix items: o3-mini high effort 31.0% at 53,596 tokens, versus 17.0% at medium [d05].
- Free-form Self-Refine: degraded GPT-4o Instructions 50.4 to 36.4 (STICK 51.6) [d03].
- Fancier prompting for small models (AutoCoT, plan-and-solve, ToT) [c10]. CoT did not raise results overall on RAVENT [c23].
- Interactive demonstrations for task-set drift: Llama-3.1-70B 3-back fell 0.31 [c08].
- Hint plus object to fix self-contradiction: only 200 to 145 failures [c13].

### 5.6 Causal status
The claim "WM capacity causes Gf" is not established. Training gives no far transfer, mediation is null, and process overlap fits the data. The claim "attention control mediates" has support but alternative orders exist. [b02, b27, a17, b05]. Mark the whole causal story contested (K10).

## 6. Language models

### 6.1 N-back and span tasks (memory measures, not reasoning)
- Gong, Wan, Wang (AAAI 2024; preprint 2023): gpt-3.5-turbo verbal and spatial n-back, n = 1-3, 50 blocks per cell. d' falls to about 1 at n = 3 in three of four verbal variants. Noise symbols and abstract-reasoning variants lower capacity; larger grids (3x3 to 7x7) raise it; feedback and CoT help, but do not remove the decline. GPT-4 far exceeds GPT-3.5 (tested only to n = 3). Seven small open models (Bloomz-7B, ChatGLM-6B, Vicuna-7B/13B) are nearly indistinguishable and very low [a19, c01-c04, b15, b16]. This is one paper, counted many times in the evidence file.
- Zhang et al. (EMNLP 2024): n-back d' across the InstructGPT line up to GPT-4: U-shaped with scale; larger models have more WM but do not match humans consistently [c09].
- Hu and Lewis (2024/2025): see 4.6 and 5.2. Retrieval accuracy 1/2/3-back: Qwen1.5-14B 1.00/.09/.08; Llama3.1-8B 1.00/.14/.17; Gemma2-27B 1.00/.57/.36; GPT-3.5 about 1.00/.51/.43; Qwen2-72B 1.00/.81/.84; Llama3.1-70B 1.00/.99/.93. Llama-3.1-70B at n = 8/9/10: 75.25/66.08/57.1% retrieval, task accuracy 83.33/78.25/71.92; with an in-context curriculum 79.83/80.17/71.67 and 90.08/90.08/84.75 [c06, c07].
- Gong and Zhang (2024): from-scratch transformers; entropy of attention rises with N [a21].
- Gong (2026): 15 LLMs, 70M-14B; median d' 2.57 / 0.91 / 0.52 at N = 1/4/6; Qwen2.5-14B 4.28 at N = 1, 1.15 at N = 6; the best-fit k-back rule differed from N in only 14 of 90 cases [a23, a28].
- Xiong et al. (COLM 2026): 10 open models (Gemma3 1B-27B, Qwen3.5 2B-27B, Ministral3 14B, Llama3 8B), non-thinking mode, N = 1-4. N-back accuracy versus benchmarks (autoregressive): MMLU-Pro .78, GPQA Diamond .88, IFEval .69; teacher forced .70, .72, .82. Log parameter count did not predict the three benchmarks. The authors cite human r = .31-.78 [a24, b19, d09]. Exact r values were not re-verified (critique item 7).
- de Langis et al. (EACL 2026): six open models. Forward span at 50 digits .99-1.00. Backward at 15: Gemma-2-9B .21, Gemma-2-27B .59, Llama-3.1-8B .18, Llama-3.1-70B .83, Qwen2-7B .00, Qwen2-72B .51. Operation span .93-.99; reading span .66-.98. N-back 1/2/3 for Llama-3.1-70B .93/.82/.82 vs human about .98/.91 (human 3-back not captured). Parameters vs mean span r = 0.82, p < .05; attention heads r = 0.76, p = .08. Wisconsin Card Sorting: 3060 trials per model (102 x 30 prompts); model accuracy .29 (Llama-3.1-8B) to about .53 vs human 70-80%; accuracy drops after a brief rise, read as forgetting the rule. Flanker incongruent 40-60% vs human 93-96%; Llama-3.1-8B 0.944 / 0.471 without reasoning and 0.977 / 0.910 with it; Qwen2-32B 0.917 / 0.638 base, 0.994 / 0.985 with reasoning. Larger span scores did not carry to problem-solving [b17, b18, c15-c18]. Reasoning models gain on backward and reading span but not on every control task.
- Liang et al. 2026: text-rendered grids beat image-rendered grids in Qwen2.5 versus Qwen2.5-VL [a22].
- Huang et al. 2025: no private commitment; written reasoning carries the work (see 4.7) [c12-c14].
- Parameter-count result disagreement: parameters predict span in de Langis (r = .82, six models) but not benchmarks in Xiong (ten models). Different dependent variables; do not merge [critique, K14].

### 6.2 Rule-holding and state tracking
- IFScale (Jaroslawicz et al. 2025): see 4.9. Reasoning models are near perfect through 100-250 rules. At 500: best about 68% (probably gemini-2.5-pro, inferred from a garbled table; the abstract says "best frontier model"; do not call o3 the best), o3 62.8%, grok-3 61.9%, claude-3.7-sonnet 52.7%, claude-opus-4 44.6%, claude-sonnet-4 42.9%, deepseek-r1 30.9%, qwen3 26.9%. Claude thinking mode gives moderate gains (figure only). Floors 7-15% for the weakest [b21, d01].
- Patil et al. (2026): 7 instruction-tuned models 8B-235B; 100% through 12 parallel branches, collapse at 20-30; GPT-4o Mini collapses at step 5 in sequential chains; Llama 3 8B fails at 3 ops per branch. Working memory (parallel independent sub-results) is the dominant scale-invariant bottleneck [b23].
- Kim and Schuster (2023): entity tracking; only code-pretrained GPT-3.5 models tracked state. In Alchemy, the initial state alone gives 62.7% on unchanged boxes; a probe gets only 3.1% on the changed ones [c25].
- Shojaee et al. (2025), The Illusion of Thinking: thinking models beat non-thinking at medium size, then all collapse at a model-specific size. Hanoi collapses around 7-8 disks (100-200 moves); first error near move 40 at N = 8 (255 moves), within the first 100 moves at N = 10; about 100 correct moves in Hanoi but only 4 in River Crossing. Giving the algorithm did not help. Temperature 0 versus sampling: no change [d06]. This paper is contested in the wider literature on whether the collapse is a token-limit artifact; that critique is not in our evidence.
- Meyerson et al. (2025), MAKER: 20 disks, 1,048,575 steps, zero errors. Microagents get the current state, make one move, return the next state; first-ahead-by-k voting and red-flagging. Per-step error: gpt-4.1-nano about 0.357 (not viable), gpt-4.1-mini about 0.0045, o3-mini about 0.0017. Estimated cost for gpt-4.1-mini about 3.5K dollars [d07].
- Huang et al. 2025: see 4.7.
- Adapala 2025 (ICE): 200 questions, 10 replications, five instruction-tuned models; Llama-3-8B and Mistral-7B 0% in all conditions including control; Gemini-2.0-Flash 85% in control with a slope of -0.003 per percent load (p < .001) [d17]. Floor effects limit use.
- RULER (Hsieh et al. 2024): average score 4K to 128K: GPT-4 96.6 to 81.2 (effective 64K); Llama3.1-70B 96.5 to 66.6 (64K); Qwen2-72B effective 32K; Mixtral-8x22B 31.7 at 128K; DBRX 2.4 at 64K [c26].
- Cook et al. (2024) STICK: generated checklist as the critique in one pass; LiveBench reasoning +7.8 absolute on the best case (abstract); overall +3.8 (Command-R+) and +0.8 (GPT-4o); InFoBench +6.5, WildBench +7.1 (Command-R+); best-of-N by STICK +5.1 InFoBench, +5.3 WildBench; Self-Refine degraded both models [d03].

### 6.3 Matrix and analogy reasoning
- Webb, Holyoak, Lu (2023): text-davinci-003 beat the mean of 40 UCLA undergraduates on text digit matrices. Generative: OR = 1.88 (CI 1.21-2.91), p = .005. Multiple choice: OR = 6.27 (CI 3.28-11.99). Item-pattern correlation r(30) = .39, p = .027. Number of unique rules: humans OR = 0.61 (p = .0047); progression rules harder, OR = 0.41 (p = .0001) [c22].
- Gendron et al. (2023): RAVENT open QA text/symbolic: text-davinci-003 .343/.234; GPT-3.5-turbo .226/.161; GPT-4 .410/.330; LLaMA-7B 0. Multiple choice: text-davinci-003 .452 (text); GPT-4 .697/.535. CoT not higher than base [c23].
- Hersche et al. (2024), I-RAVEN-X, oracle perception: I-RAVEN 3x3 GPT-4 93.2%, Llama-3 70B 85.0%. 3x10 grid at ranges 50/100/1000: GPT-4 82.2/79.6/76.6; Llama 76.8/73.0/74.2. Arithmetic-rule accuracy: GPT-4 73.6 (3x3) then 30.4/25.1/8.4; Llama 45.0 then 1.5/2.6/0.4. Table IV: arithmetic 27.1% for GPT-4 without per-attribute queries, 73.6% with. I-RAVEN-X varies grid width and range, not rule count [d04].
- Camposampiero et al. (2025): o3-mini 86.6% on I-RAVEN to 17.0% on I-RAVEN-X with max uncertainty (3.4x more reasoning tokens); DeepSeek R1 80.6% to 22.8% (23.2% in the abstract; chance 12.5%). With clean inputs, range 10 to 1000 (3x10): o3-mini 86.6 to 81.0 (5.6 pt loss); R1 80.6 to 82.8 (+2.2); tokens 5,445 to 7,209. High-effort o3-mini: 92.6 on I-RAVEN, 80.6 at range 1000 (2.7x tokens, no gain); 31.0% at 53,596 tokens under noise. Neuro-symbolic ARLC: 98.6 to 88.0 [c24, d05]. So the collapse is perceptual uncertainty, not rule count or range. The "I-RAVEN-X tests Carpenter's rule-count prediction" idea is closed with answer no (K19).

### 6.4 General structure
Ilic and Gignac (2024): 591 LLMs, 12 tests mapped to Gf, Gkn, Grw, Gq; positive manifold, a general factor, and a combined Gkn/Grw group factor; parameters correlate with it with diminishing returns [c27]. Single source.

### 6.5 Summary of what changed behaviour, and by how much
| Lever | Effect | Where |
|---|---|---|
| Scale and training | weak open models 0.09 at 2-back; 70B 0.99; 70B holds to 10-back (57% retrieval) | [c06, c07] |
| In-context curriculum | +4.6, +14.0, +14.6 retrieval points at 8/9/10-back | [c07] |
| Chain-of-thought | spatial n-back up; incongruent control .47 to .91; Math Magic 0 to 100% for R1 | [a19, c18, c14] |
| Chunked status list | +35.4 points (old model) | [d08] |
| Per-attribute query | 27.1 to 73.6 on arithmetic rules | [d04] |
| Extreme decomposition with state passing and voting | zero errors over 1,048,575 steps | [d07] |
| Checklist re-pass | +0.8 to +3.8 overall LiveBench; free-form re-pass negative | [d03] |
| Thinking mode on rule density | moderate gains for Claude (figure only); reasoning models near perfect to 100-250 rules, then collapse or shrink output | [d01, d02] |
| More reasoning effort on noisy matrices | 17.0 to 31.0 only, at 3.4x to 10x tokens | [d05] |
| Giving the algorithm | no change in the collapse point | [d06] |

### 6.6 What is missing
- No study links a model's n-back or span score to its matrix-reasoning score inside the same model with size and thinking mode held fixed (gap 3 partly answered by Xiong; benchmarks are knowledge, not Gf).
- No study varies rule count at equal tokens with and without an external state (gap 1).
- No study tests IFScale-type collapse beyond 500 rules or with Claude-class models in thinking mode as a function of a checklist re-pass (gap 5, 7).
- No LLM test of process overlap versus shared bottleneck (gap 8) or of restraint versus constraint (gap 9).
- Most n-back work shares authors and prompt format (critique).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts are from SCHEMA.md: guardrails G1-G12, states S0-S9, operators O1-O8, memory section 5.

### Add now (established)
1. **Keep the working state in text, rewritten at each step [E].** Part: S (a written state carried from S2 to S4, S5, S8) and memory. Reason: models have no private commitment; the tokens are the WM; implicit memory shows a readout bottleneck and drift. Evidence: a21, a23, a28, b19, b20, c12, c13, c14 (K13, K11, K17). Note: the strongest "state rewrite" results (MAKER, chunked status list) are single-source (K23), so the claim to add is only "do not rely on implicit state", not a specific format.
2. **Do not stack many simultaneous live rules [E in direction].** Part: G (a cap on rules held at once; split into groups; recheck list). Reason: compliance decays with density; omission dominates; collapse around 100-250 rules for reasoning models, with a parallel-branch cliff at 20-30 [b21, b22, d01, d02, b23, c26] (K16 single-source in magnitude, K17 established for the cliff). Add as a cap-and-chunk rule, not as a number: the number must be measured on our model.
3. **Decompose long procedures, with the state carried between pieces [E].** Part: O3 decompose, S5/S8 checkpoint. Reason: the single-run length collapse is real and rule knowledge does not fix it (d06), while one-step state passing removes it (d07), and chunking lifted arithmetic rules (d04). Evidence: d06, d07, d08, d04, c25, b23 (K17).
4. **Write only the relevant attributes: filter before reasoning [E in part].** Part: S1 input hygiene, O6 change representation. Reason: interference, not count alone, hurts humans [a04, a13]; in LLMs, noise and confounders cause the collapse on matrix items, not range [d05, K19]. The human interference result is established; the LLM filter step is a hypothesis (see Test first).
5. **Do not buy capacity by training or by more reasoning on noisy items [E].** Part: G7, G11. Reason: WM training has no far transfer [b01, b02, b03]; high reasoning effort did not rescue noisy matrix items (d05, but K24 is single-source). Consistent with the existing G11 text; no schema change.
6. **Separate "hold" from "suppress" when diagnosing failures [E in humans].** Part: S4/S6 diagnosis log only. Evidence: b10, a17, d13, c18. No operator change yet: no LLM study isolates it.

### Test first (not established for the agent; each is a UNKNOWNS candidate)
- Written rule table versus no table, scaling with the number of interacting rules at equal tokens (K23, gap 1). [S]
- Checklist re-pass for dense-rule prompts (STICK-style) on Claude-class models (K16, d03). [S]
- Re-stating the rule list every k steps against task-set drift (a20, c08, K11/K12). [S]
- Rejected-hypothesis list as separate from the active-rule list (K26, d14). [S]
- Distractor filter pre-pass on noisy rule items (K24, d05). [S]
- Per-attribute split queries versus joint queries at equal tokens (K25, d04). [S]
- Checkpointing every k steps in long procedures (K22, d06, d07). [S]
- Whether n-back or span predicts matrix-reasoning in the agent model (K14, gap 3). [C]
- Shared bottleneck versus task-specific slopes (K27). [open]
- Explicit reasoning step on manipulation (backward) tasks (K15, c15, c18). [S]

### Do not add
- Any claim that the agent has a capacity of "about 4" or "about 3". The human 4 comes from relational complexity (Halford) at Wikipedia level [b24]; the LLM 3 is a prompt and model artefact [a20, c07].
- A training or practice phase to raise capacity [b01, b02].
- Free-form self-refinement as the re-check (already in 4b; d03 adds one more case) [d03].
- Elaborate prompting schemes for small models (c10).

## 8. Concrete tests on our bench

All tests: two arms at equal total output tokens (including hidden reasoning if counted), same model, same items, at least 5 seeds per cell, report paired differences with bootstrap CI. Items below are designed fresh; no source gives them.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Rule-table items: 2, 4, 8, 16 interacting rules (e.g. apply rules in order to an input, text matrices with k attribute rules) | A: free reasoning. B: write and update a rule table, then apply | accuracy by rule count; slope of accuracy on k | B gain grows with k; B slope flatter. Zero gain at k = 2 |
| T2 | Instruction-density report task (IFScale-style) at 50, 100, 200, 400 rules | A: one pass. B: one pass plus generated YES/NO checklist re-pass at the same total tokens | compliance %; omission rate | B +2 to +6 points at 200-400; no gain at 50 (K16, d03) |
| T3 | Distractor-rich rule items: same rules with 0, 3, 6, 12 irrelevant attributes | A: direct reasoning. B: relevance filter pre-pass writes only the relevant attributes | accuracy by distractor count | B protects against the drop; A falls with distractors (K24) |
| T4 | Long procedure (Hanoi-like, 6-12 disks; also a non-Hanoi stateful sort) | A: single run. B: checkpointed state every k steps, k in {5, 10, 20} | collapse size; first-error index | B moves collapse out by more than 1 disk (K22, d06, d07) |
| T5 | Task-set drift: n-back-like instruction (2- or 3-back, m-back variants) over 40 turns | A: rule stated once. B: rule restated every 5 turns | accuracy by turn; drift to m-back answers (Hu and Lewis measure) | B reduces drift |
| T6 | Split vs joint query on attribute-wise rules (arithmetic progression, distribute-three) | A: one joint query. B: one query per attribute, answers joined by code | rule-type accuracy, equal tokens | B large gain on arithmetic rules (K25) |
| T7 | Backward span, 5-15 items, plus incongruent control | A: direct. B: stepwise reasoning | accuracy by length | B gain on backward and incongruent (K15) |
| T8 | Predictive link: n-back d' (levels 1-6) and matrix-style item accuracy for 3+ model sizes and thinking on/off | n/a (correlational) | partial correlation of n-back and matrix accuracy controlling for size and mode | positive partial r would support transfer of the human claim (K14); null would support "separate" |
| T9 | Rejected-hypothesis search tasks (guess a hidden rule with feedback) | A: active rule list only. B: active list plus rejected list | repeat-test rate; solves per token | B lowers repeats (K26) |
| T10 | Shared vs specific bottleneck: apply one load manipulation (extra rules, noise) to 3 different rule tasks | n/a | slope by task, interaction test | common slope = shared bottleneck (K27) |

## 9. What does not transfer, and why

- **Capacity as a fixed number.** Humans have a stable span across contexts. LLM "capacity" depends on prompt format, model scale, curriculum, grid size, noise and thinking mode (all in section 6). A fixed "n = 3" is false for current models [c07].
- **The latent correlation .70-.80.** It compares individual differences across people on tasks that one brain performs. Between-model scores differ in training data, size and mode. The only cross-model correlation (Xiong) is with benchmarks, not Gf, on ten small models [d09].
- **Simple versus complex span.** LLMs are perfect on simple forward span at 50 digits [c15]; they fail on manipulation. The distinction is real but the cause is different (control and readout, not storage).
- **Training for capacity.** Not applicable; our agent is not trained. The human null does not tell us anything about the scaffold either.
- **Pupil, delay activity, heritability, neural findings.** Human only [b07, b08, b09, b24, d16].
- **Speeding and time pressure.** Token budget is not time pressure; the K06 test is an analogy only.
- **Reverse causation by Gf.** No LLM analogue.
- **Hanoi results.** A solved puzzle with a known algorithm; the collapse measures execution length and token behaviour, not reasoning ability. It is a good test for state carrying, not for Gf (d06).
- **Gong's "human-like" label.** Similar curves can have different causes: attention dilution, comprehension failure, readout interference [a28]. Do not infer that human theory (executive attention) explains LLM data.

## 10. Open questions

1. What are the actual figures in Dokic, Koso-Drljevic, Bilalic 2025, the named key paper? (gap 2; not read)
2. Kyllonen and Christal full text: exact task list and the content-overlap sensitivity analyses (gap 10).
3. Does a written working state raise accuracy at equal tokens, and does the gain scale with rule count? (gap 1).
4. Is there a WM-Gf link inside LLMs after controlling for size and thinking mode (gap 3)?
5. Where is the collapse point for frontier thinking models above 500 rules, and does a checklist re-pass move it (gap 5)? Which model reached about 68% at 500 in IFScale (likely gemini-2.5-pro)? (gap 7)
6. Au 2014: what are its active-control numbers? The 0.05 versus 0.24 dispute is explained in cause (control type, baseline adjustment, scope) but Au's own numbers were not re-read (gap 6).
7. Process overlap versus shared bottleneck in LLMs (gap 8); restraint versus constraint in LLMs (gap 9).
8. Is the Illusion of Thinking collapse a token-limit artefact, and how does it change with state passing? (not covered in our evidence)
9. Do Claude-class models show the human-like interference pattern in n-back (lure effects)? Most n-back work used GPT-3.5/4 or open models.
10. Do the open-model n-back findings (non-thinking, small) hold in current frontier thinking models?
11. Chuderski 2013 and Carpenter 1990 were not opened. K05 and K06 rest on secondary summaries.

## 11. Sources

[V] opened this session by the evidence agents, [M] snippet/recall/abstract only.

Human work
- [M] Kyllonen, Christal (1990), Intelligence 14. https://doi.org/10.1016/S0160-2896(05)80012-1 [a01, b11]
- [V] Conway, Kane, Engle (2003), TiCS. https://www.gwern.net/doc/dual-n-back/2003-conway.pdf [a02-a04, a27]
- [V] Colom, Rubio, Shih, Santacreu (2006), Psicothema. https://www.psicothema.com/pdf/3314.pdf [a05-a07]
- [V] Hagemann et al. (2023), Fluid intelligence is (much) more than WMC. https://publikationen.bibliothek.kit.edu/1000158608/150792286 [a08, a09, a15, a16, a26]
- [M] Engle, Tuholski, Laughlin, Conway (1999), JEP:General. https://doi.org/10.1037/0096-3445.128.3.309 [a10]
- [M] Ackerman, Beier, Boyle (2005), Psych Bull. https://doi.org/10.1037/0033-2909.131.1.30 [a11, b12]
- [M] Carpenter, Just, Shell (1990), Psych Review. https://doi.org/10.1037/0033-295X.97.3.404 [a12]
- [V] Little, Lewandowsky, Craig (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC3968765/ [a13]
- [M] Chuderski (2013), Intelligence. https://doi.org/10.1016/j.intell.2013.04.003 (blog summary read) [a14]
- [V] Draheim, Pak, Draheim, Engle (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8853083/ [a17]
- [V] Cochrane, Simmering, Green (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6705795/ [a18, b05, b06]
- [M] Dokic, Koso-Drljevic, Bilalic (2025), Intelligence. https://doi.org/10.1016/j.intell.2024.101874 [a25] (metadata only)
- [V] Melby-Lervag, Redick, Hulme (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4968033/ [b01, b02, d10]
- [V] Lawlor-Savage, Goghari (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4820261/ [b03, b04]
- [V] Unsworth, Fukuda, Awh, Vogel (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4465247/ [b07]
- [V] Robison et al. (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10118234/ [b08]
- [V] Ruuskanen, Hagen, Espeseth, Mathot (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11086595/ [b09]
- [V] Kane et al. (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4965188/ [b10]; [M] Crossref copy https://doi.org/10.1037/xge0000184 [d15]
- [M] Kane, Hambrick, Conway (2005). https://doi.org/10.1037/0033-2909.131.1.66 [b13]
- [M] Conway et al. (2002), Intelligence. https://doi.org/10.1016/S0160-2896(01)00096-4 [b14]
- [V] Wikipedia: Working memory. https://en.wikipedia.org/wiki/Working_memory [b24]
- [V] Wikipedia: Fluid and crystallized intelligence. https://en.wikipedia.org/wiki/Fluid_and_crystallized_intelligence [b25]
- [M] Jaeggi et al. (2008), PNAS. https://doi.org/10.1073/pnas.0801268105 [b26]
- [M] Kovacs, Conway (2016). https://doi.org/10.1080/1047840X.2016.1153946 [b27]
- [M] Melby-Lervag, Hulme (2016) reply. https://doi.org/10.3758/s13423-015-0862-z [d11]
- [M] Au et al. (2015). https://pubmed.ncbi.nlm.nih.gov/25102926/ [d12] (abstract)
- [V] Burgoyne, Engle (2020), abstract via Crossref. https://doi.org/10.1177/0963721420969371 [d13]
- [V] Lee, Engle (2026 preprint), abstract. https://doi.org/10.31234/osf.io/4nw5s_v1 [d14]
- [V] Connectome study N = 297. https://pmc.ncbi.nlm.nih.gov/articles/PMC9921238/ [d16]

Language-model work
- [V] Gong, Wan, Wang (2024), Working memory capacity of ChatGPT. https://arxiv.org/abs/2305.03731 [a19, b15, b16, c01-c04]
- [V] Hu, Lewis (2025), Do LMs understand the cognitive tasks given to them? https://arxiv.org/abs/2412.18120 [a20, c06-c08]
- [V] Gong, Zhang (2024), Self-attention limits WM capacity. https://arxiv.org/abs/2409.10715 [a21, c05]
- [V] Liang et al. (2026), Spatial n-back in VLMs. https://arxiv.org/abs/2602.04355 [a22]
- [V] Gong (2026), Readout bottleneck. https://arxiv.org/abs/2610.21176 [a23, a28]
- [V] Xiong et al. (2026), In-context superposition. https://arxiv.org/abs/2604.09670 [a24, b19, b20, d09]
- [V] de Langis et al. (2025), Strong memory, weak control. https://arxiv.org/abs/2504.02789 [b17, b18, c15-c18]
- [V] Jaroslawicz et al. (2025), IFScale. https://arxiv.org/abs/2507.11538 [b21, b22, c19-c21, d01, d02]
- [V] Patil et al. (2026), algebraic reasoning failures. https://arxiv.org/abs/2604.06799 [b23]
- [V] Zhang, Jian, Ouyang, Vosoughi (2024), WM identifies reasoning limits. https://aclanthology.org/2024.emnlp-main.938 [c09-c11, d08]
- [V] Huang, Sun, Wang, Dredze (2025). https://arxiv.org/abs/2505.10571 [c12-c14]
- [V] Webb, Holyoak, Lu (2023). https://arxiv.org/abs/2212.09196 [c22]
- [V] Gendron et al. (2023). https://arxiv.org/abs/2305.19555 [c23]
- [V] Camposampiero et al. (2025). https://arxiv.org/abs/2503.11207 [c24, d05]
- [V] Hersche et al. (2024), I-RAVEN-X. https://arxiv.org/abs/2412.05586 [d04]
- [V] Kim, Schuster (2023), Entity tracking. https://arxiv.org/abs/2305.02363 [c25]
- [V] Hsieh et al. (2024), RULER. https://arxiv.org/abs/2404.06654 [c26]
- [V] Ilic, Gignac (2024). https://doi.org/10.1016/j.intell.2024.101858 [c27]
- [V] Sumers et al. (2023), CoALA. https://arxiv.org/abs/2309.02427 [c28]
- [V] Cook et al. (2024), STICK. https://arxiv.org/abs/2410.03608 [d03]
- [V] Shojaee et al. (2025), Illusion of Thinking. https://arxiv.org/abs/2506.06941 [d06]
- [V] Meyerson et al. (2025), MAKER. https://arxiv.org/abs/2511.09030 [d07]
- [V] Adapala (2025), ICE. https://arxiv.org/abs/2509.19517 [d17]

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 9 established claims: 5 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A13.03-K02** (reworded: the sources support less). Sources say the .80-.90 may be partly due to arithmetic content overlap and an arbitrary battery (K and C conceded arbitrariness); they do not show it was inflated, nor that .58-.72 come from overlap-free designs. Corrected claim: The strongest headline (.80-.90) may be partly inflated by content overlap (an arithmetic reasoning test in all four samples) and an arbitrary, impure WM battery; later latent-variable studies with other designs report lower values (.58-.72), though the sources do not establish those designs were free of overlap.
- **A13.03-K04** (reworded: the sources support less). Only Conway et al. (one Sternberg-variant study) supports the overlap-specific slope result; the second source (Little et al. 2014) is about item difficulty, not interference, and the general rule is extrapolated from one example. Corrected claim: In one Sternberg-scan variant reviewed by Conway, Kane and Engle (2003), low-WMC people had steeper RT slopes than high-WMC people only when letters overlapped across sets; with no overlap slopes did not differ. This is one example, and it suggests (not shows) that capacity matters most under interference.
- **A13.03-K07** (number corrected). In Kane et al. 2016 [.46,.74] is the 95% confidence interval around one correlation (attention restraint with attention constraint), not a range of correlations, and it is not 'of mind wandering'; Draheim 2021 full mediation (N=396) held only with accuracy-based tasks and needs replication. Corrected claim: Attention control (antisaccade, visual arrays) may carry much of the WM-Gf link (Draheim 2021, N=396: full latent mediation only with reliable accuracy-based tasks, not yet replicated); attention restraint and attention constraint are correlated but separable (Kane 2016, 95% CI around the correlation .46 to .74, which excludes 1.0).
- **A13.03-K13** (reworded: the sources support less). Numbers match (most larger models above 95%, not all), but 'limit is architectural' overreaches: Gong 2026 locates it in readout under interference, and the 2-layer perfect solution shows capacity depends on model size/training, not a fixed architectural ceiling; all but Xiong are one author (Gong). Corrected claim: In small transformers trained from scratch, a 1-layer 1-head model shows a logarithmic accuracy decline up to N=6 while most models with more layers or heads stay above 95%; in 15 pretrained LLMs (70M to 14B) errors cluster on lures (models say match to 79% of N-1 lures at N=2), which Gong 2026 attributes to readout under interference rather than finding the item; Xiong et al. report a 2-layer transformer solves the task perfectly. This points to interference and attention dispersion, not a fixed architectural limit.
