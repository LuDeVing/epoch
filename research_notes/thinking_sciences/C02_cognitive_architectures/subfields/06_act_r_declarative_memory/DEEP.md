# ACT-R: declarative memory: deep document

Subfield C02.06. Focus: retrieval depends on context and on the history of use. Why it matters for our agent: memory ranking.
Evidence ids (a01..a27, b01..b25, c01..c18, d01..d15) refer to the evidence_*.jsonl files in this folder. Claim ids (C02.06-K01..K30) refer to claims.jsonl. Marks: [V] page opened, [M] snippet or abstract only.

Headline: the human side is solid on shape (use history and recency both matter, and spaced use helps). The LLM side is thin. No study yet shows that an ACT-R-style score beats plain cosine (or the Generative Agents score) in an LLM agent at equal tokens. Most "established" items below are "the gap exists", not "the term helps".

## 1. What it is

ACT-R is a cognitive architecture. Its declarative memory holds "chunks" (facts, events). Each chunk has an activation. Activation decides two things: whether the chunk is retrieved, and how fast.

Activation has parts (a15, b05, c16):

- Base level B: the use history of the chunk. B = ln( sum over past uses j of (t_j)^-d ), where t_j is time since use j and d is the decay (about 0.5 by default; fitted .52 in a11). Every use adds a trace. Each trace fades as a power law. Many uses and recent uses both give high B.
- Spreading activation S: sum over cues in the current context of (source weight W_j x association strength S_ji). Strength falls with fan (the number of chunks linked to the cue). This is the "context" part.
- Partial matching: a chunk that matches only in part can still win, minus a mismatch penalty. This is the source of commission errors (a17).
- Noise: Gaussian noise on activation, so retrieval is stochastic.
- Threshold tau: below it, retrieval fails (an omission error).
- Retrieval odds = C e^(cA); retrieval time = B e^(-bA) (a15). Time falls as activation rises.
- Blending: the answer can be a weighted mix of chunks (b05).

Total: A = B + S (+ match penalty + noise).

Plain reading for an engineer: score = log(sum of power-decayed use events) + similarity to the current cues. Retrieve the top item if it clears a threshold. This is the cognitive-architecture version of "memory ranking".

How it relates to LLM agent memory:

- Generative Agents (a19, c01) ranks by recency + importance + relevance. Relevance is like spreading activation. Recency is like base level, but it is exponential, keyed to the last retrieval only, and has no use count. Importance has no ACT-R counterpart (a20).
- So ACT-R's distinctive offer is the use-history sum and its power-law shape. That is what this document tests.

Links to other subfields in this run (not covered here): ACT-R: production compilation (turning lessons into routines), Working memory, Semantic memory network structure, Retrieval-induced forgetting and memory errors, Cognitive load, Global workspace theory.

## 2. History and theories in depth

### 2.1 Rational analysis of memory (1989-1991)
- Anderson & Milson (1989) [M, a07] first argued memory is tuned to the statistics of need. Sources were library borrowings and file access. Anderson & Schooler said the sources were not true memory demands.
- Anderson & Schooler (1991) [V, a01-a06] is the founding paper. Two steps. First, human data: Ebbinghaus retention fits a power function (log P = 3.862 - 0.126 log delay, R2 .978, delays 20 min to 31 days). Practice (log trials = 4.08 - 1.44 log days, R2 .996) beats the exponential form on the same data (R2 .949). Second, the world: they counted real demands in 730 days of New York Times headlines, child-directed speech (CHILDES) and one person's e-mail senders. The chance an item is needed falls as a power of time since its last use, with exponents .73, .77, .83. An exponential did not fit in any corpus.
- Same paper: the spacing effect appears in the world. When the two earlier uses were close together, the slope was steeper (NYT .49 vs .20; parent speech .76 vs .45; e-mail 1.03 vs .48 for short vs long lag).
- Practice and retention combine about additively on a log-odds scale.
- The model had four assumptions: strength encodes need odds; strengths of separate presentations add; each decays as a power; the exponent shrinks with the lag since the previous presentation. Assumption 4 produced spacing. This is the root of B = ln(sum t^-d).

### 2.2 Practice and retention as one function (1999)
- Anderson, Fincham & Douglass (1999) [V, a11-a14]: one strength function explains the power law of practice and the power law of retention. Fit to 5 experiments, up to 240 practice trials, gaps up to 400 days. Exp 1: d = .52, R2 = .974, strength rose about 10x (2.26 to 19.33).
- "Slowed clock": time outside the session counts for much less. Items aged 32 blocks within a session but only 9.59 blocks between sessions; H was about 12 blocks per day. The authors say event count may be the true time variable (a12). For an agent this means "turns", not "wall seconds".

### 2.3 Spacing, adaptive decay (2004-2005)
- Pavlik & Anderson (2004) [V, a08-a09]: the fixed-d model could not handle massed practice. New rule: each trace gets its own decay, set by the activation at the time it was laid down (higher activation at the time, faster decay). This yields spacing and its interaction with repetition. Fit to 162 points r2 .971, but chi-square 260 on 157 df (a statistical misfit). Failed on the 8-repetition, lag-14 condition.
- Current statement (Stocco et al. 2023, b05): the Pavlik-Anderson variant is in the standard theory, with a rate parameter alpha. Their own stance: speculative, no new data. ACT-R still has no encoding interference, no episodic/semantic split and no active forgetting.

### 2.4 Working-memory and error accounts (1994-2000)
- Lebiere, Anderson & Reder (1994) [V, a17]: omission errors (below threshold) and commission errors (a more active, partly matching chunk wins). Most human errors were wrong-but-related items, not blanks.
- Anderson, Reder & Lebiere (1996) [V, a15-a16]: working memory is a fixed pool of source activation shared by cues. More cues, less activation each. A single pool beat a separate-capacity model (Exp 1 chi-square 36.14, about 10 worse for the rival with two fewer parameters). Base level was set to zero, so this is spreading only.
- Lovett, Daily & Reder (2000) [V, a18]: one parameter W (source activation) per person. Cross-task link to n-back was not significant (r = .04, and .56 with p = .12).

### 2.5 Neighbours
- Fan effect in anaphor resolution (Autry & Levine 2014 [V, b06]): more same-category nouns in a list slow and degrade retrieval of the referent. Pooled F(1,265) = 15.56, d = 0.24 [.12, .36]. Small, mostly significant by items only.
- Spaced repetition at scale: Settles & Meeder 2016 [V, b23], half-life regression on 12.9M Duolingo traces.
- ACT-R in applications: mHealth adherence (b07, b08), music relistening (c12, c13), embeddings inside ACT-R (b20, c15).

### 2.6 Into LLM agents (2023-2026)
- Generative Agents (2023), MemoryBank (2023), Hou et al. (2024), SynapticRAG (2025), Honda et al. (2025), SYNAPSE (2026), OBLIVION (2026), FadeMem (2026), CAMeR (2026), Kerestecioglu (2026). Details in section 6. Only Honda and the Sievers pyactr robot (a24) claim an ACT-R lineage in the strict sense; neither has measured results.

## 3. Core findings with exact numbers

Status key: established = several independent sources; single = one source; contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Lab retention follows a power function (Ebbinghaus data) | log P = 3.862 - 0.126 log delay, R2 .978; practice R2 .996 vs exponential .949 | Anderson & Schooler 1991 (a01, V) | established as a fit; form contested (see 5.2) |
| Need in the world follows a power law of time since last use | exponents .73 (NYT), .77 (child speech), .83 (e-mail); k = 1.0 / .76 / .9 | a02, a03 (V) | single (one paper, 3 corpora) |
| Spacing appears in the environment | exponent short vs long lag: NYT .49/.20; speech .76/.45; e-mail 1.03/.48 | a04 (V) | single, correlational |
| Strength = sum of power-decayed uses, one function for practice and retention | d = .52, R2 .974 (Exp 1); gap data r = .941; warm-up r = .95 | Anderson, Fincham & Douglass 1999 (a11, V) | single lab paradigm |
| Slowed clock: between-session time counts less | 32 vs 9.59 blocks; H about 12 blocks per day | a12 (V) | single |
| Spacing effect in paired associates | N = 40, 104 pairs; session-2 correct .64 (1 day) vs .52 (7 days); spacing F(2,76) = 58.2; rep x spacing F(4,152) = 4.38 | Pavlik & Anderson 2004 (a08, V) | established (spacing); model fit imperfect |
| Adaptive-decay model fit | 162 points, r2 .971, RMSD .046, chi-square 260 / 157 df; Glenberg data r2 .980 | a09 (V) | single, misfit |
| Spaced reminders beat massed at high frequency, field study | N = 64, 28 days; .55 vs .38 vs low-freq .34/.32 vs none .18; reminders vs none OR 7.52; interaction OR 2.22 | Pirolli et al. 2017 (b08, V) | single, cells 11-14, low power |
| Rate of forgetting independent of strength (against practice-slows-decay) | 4 sentence-recall experiments, N = 60/60/60/40; no reps x delay interaction in Exp 2-4 | Rivera-Lares 2022 (b03, V) | contested |
| Same in visual short-term memory | N = 22/21/21; Bayes factors for no interaction 5.47/7.31/6.29; pooled 11.86 | Cohen-Dallal 2018 (b04, V) | contested (different system) |
| Ebbinghaus replication: same shape, lower savings | 31-day savings .041 vs Ebbinghaus .211 (corrected measure .137); power R2 .974 AIC -16.6; summed exponential R2 .995 AIC -24.5 | Murre & Dros 2015 (b01, b02, V) | single subject |
| Parameter identifiability is weak | noise .001-.08 and BLC 6.9-16.9 across four fitting methods, same threshold and LF | Kangasraasio 2019 (b09, V); van der Velde 2022 (b10, V) | established |
| Cue overload lowers retrieval | digit span x algebra, F(2,28) = 4.96; Exp 2 F(3,57) = 35.87 | Anderson, Reder & Lebiere 1996 (a15, V) | single lab task |
| Embedding cosine can supply association strength | Spearman rho .50-.51 on 6,631 priming pairs, 512 people; equal to linear regression (.51), not better | Meghdadi 2026 (b20, c15, V) | established as parity |
| Repeat-aware ranking with base level helps when repeats dominate | Last.fm NDCG 12.16%; repeat share 72.4% (Last.fm), 89.1% (Deezer); frequency-only exploration NDCG .07 | PISA (c13, V) | single |
| Half-life regression: calibration up, ranking not | MAE HLR .128 vs Leitner .235, LR .211, constant .175; AUC .538 (Leitner .542) | Settles & Meeder 2016 (b23, V) | single |
| Park ranker has no use-count and was never ablated term by term | full 29.89 vs fully ablated 21.21 TrueSkill, d 8.16; whole-module ablation only | Park 2023 (a19, b14, c02, V) | established as a gap |
| Recall-count scoring beat Park scoring on 10 author tasks | t = -5.687, p = .0003, CI [-0.27, -0.12] | Hou 2024 (b15, c04, V) | single, small |
| Habit-vs-exception: both scorers fail | recall-count picked University .850 (habit); Park picked Restaurant 1.620 (recent one-off) | Hou Task 0 (d06, V) | single item |
| Delete-on-decay hurts on LongMemEval | S tier: raw RAG 78.4 [74.8, 82.0] vs aggressive consolidation 48.4 [44.0, 52.8] | Kerestecioglu 2026 (a25, V) | established (with c10) |
| VSCode gain came from deduplication, not decay | 97.2% retention precision, 58% store cut, +21.8 pp | a25 (V) + critique | single, correction |
| Retrieval method matters more than write method on LoCoMo | cosine 73.4%, BM25 57.1%, hybrid + LLM rerank 77.2%; raw chunks 77.9% / 81.1% | Yuan 2026 (c06, V) | single |
| SYNAPSE leads LoCoMo | F1 40.5 vs Zep 39.7, MemoryOS 38.0, A-Mem 33.3; no node decay 30.7 (temporal 50.1 to 14.2) | b19, c07, c08, d01 (V) | single group; decay is a leak, not base level |
| Decay settings are only mildly sensitive | SYNAPSE delta .3/.5/.7: 40.0/40.5/38.1; OBLIVION T table non-monotone | d03, d07 (V) | single |
| OBLIVION: small accuracy gain, large token cut | 90.60 vs 89.00; up to 73% cost cut | c11, d07 (V) | single |
| LoCoMo cannot test decay | on 19 session summaries all weights saturated at 0.99+ | CAMeR (c10, d09, V) | established as a limit |
| Counting retrieval as use credits passengers | 10 of 169 credited successes were marginal helps (5.9%) | Rocchi 2026 (d13, M abstract) | single |
| Small benchmark noise | BM25 vs full context n = 160, gap 8.8 points, p = .09 | d12 (M abstract) | single |

## 4. Mechanisms and models

### 4.1 Base-level activation (the one to copy)
For memory i with past use times t_1..t_n (age at now: a_j = now - t_j):

    B_i = ln( sum_j a_j^(-d) ),  d about 0.5

- n uses at the same age a give B = ln(n) - d ln(a). Doubling the uses adds 0.69. Doubling the age costs about 0.35 at d = .5.
- Cheap approximation for many uses (optimised learning): B = ln(n / (1 - d)) - d ln(L), L = age of the first use. Use it when the log is long.
- Implementation: store a list of use timestamps (or event numbers) per memory. Compute at query time. Add a floor (age at least 1 unit) to avoid infinity.
- Minimal ranker: score = w1 * B_norm + w2 * cosine. Park uses min-max scaling on each term, all weights 1 (a19). Do the same to keep comparisons fair.

### 4.2 Decay form
- Power: a^-d. Exponential: exp(-a/S). Stretched exponential: exp(-lambda a^beta) (FadeMem, d08). Wickelgren: (1 + beta a)^-psi (d14).
- Human data does not decide among them (section 5.2). So run both and pick on held-out ranking.

### 4.3 The clock
- Wall time (Park hours, Hou seconds), turns (OBLIVION), query rounds (CAMeR), timestamp gaps (SYNAPSE edges). None compared (d15, K23).
- ACT-R's own data suggest the true variable is closer to intervening events (a12). For an agent run that is idle between sessions, wall time would erase memories during idle time. Test events.

### 4.4 Spacing and adaptive decay
- Plain sum of powers does not give spacing. Two options: (a) Anderson-Schooler: exponent depends on lag from the previous use; (b) Pavlik-Anderson: decay of a new trace d_j = c e^(m_{j-1}) + alpha, where m is the activation at the time. Both add parameters. Needed only if the agent's reuse pattern is bursty and old items matter.
- Cheapest proxy: count a use only if it comes after a gap (for instance a new session or episode). Bursts then count once. This is also a guard against "passengers" (section 5.5). The formula in (b) is from memory of the Pavlik-Anderson model, not re-read here.

### 4.5 Spreading activation and fan
- S_i = sum over cues j of W_j * S_ji, with S_ji = S - ln(fan_j). For an agent: use cosine to the query as S, and divide by a fan count (how many memories share the cue). SYNAPSE does this on a graph (d01, d04): removing its fan penalty cost open-domain F1 25.9 to 16.8.
- Cue overload: total W is fixed (a15). Many query cues dilute each. For an agent, keep the query short and specific.

### 4.6 Threshold, noise, partial match
- Retrieve only if A > tau. This gives "I do not remember" instead of a wrong item. Our schema G6 (never abstain on first pass) applies to final answers, not to memory: a failed memory lookup should return nothing and let the model proceed.
- Noise s = .25 in a09. Noise gives variation across runs. For a ranker, noise should be zero in evaluation.
- Partial match is where wrong-but-related chunks come from (a17). Expect the top-ranked memory to be a near neighbour, not always the target.

### 4.7 What to log per use
Memory id, time and event number of each use, whether the memory was cited in the final answer (see 5.5), and the outcome of the run. Without this log none of the tests below can run.

## 5. What holds up

### 5.1 Holds (human)
- Recency and frequency both predict future need (a02, a03). Spaced use beats massed use (a08, b08). Practice raises starting strength (b03, b04 agree on that).
- Spreading from cues with a fan penalty fits priming and anaphor data (b06, b20), though effects are small (d = 0.24) and embeddings match, not beat, a regression (rho .51 both).
- Parameters are weakly identified (b09, b10): noise and BLC change by method. Do not read much into any single fitted value.

### 5.2 Contested: the form of forgetting
- Power vs exponential: Murre & Dros power R2 .974 vs summed exponential .995, AIC gap 2 (b02). Anderson-Schooler favour power. Averell & Heathcote 2011 (d10, M abstract) fit individuals with an exponential yet select a power by Bayesian comparison. Averaging exponentials mimics a power law (Murre & Chessa 2011 [M, b13]; a14). Verdict: contested. Do not hard-code.
- Murre & Dros caveat: the 31-day "no retention" was partly a measure artefact (corrected .137, not .041).

### 5.3 Contested: does practice slow decay?
- ACT-R (Pavlik-Anderson) says strong traces decay differently. Four sentence-recall replications of Slamecka-McElree (b03) and three visual-memory experiments (b04, BF about 5-12 for no interaction) say the rate is the same. Rivera-Lares Exp 1 had floor effects at 1 week and about 20 per cell. Verdict: unresolved. The extra parameter is probably not needed for an agent (inference, not tested).

### 5.4 What did not work (LLM side)
- Deleting by decay: aggressive consolidation 48.4% vs raw RAG 78.4% (a25). Kerestecioglu's VSCode win was dedup.
- Time-driven decay alone collapses weights to near zero over 100 rounds (CAMeR, d09).
- Learned per-memory decay (81-parameter MLP) did not beat the keyword gate (c10).
- Composite scores can crown a bad policy: Alqithami 2025 abstract says Hybrid .911, its Table 2 says Random Drop .635 (a22). Excluded from claims.
- Frequency-only ranking fails on exploration: NDCG .07 (c13).

### 5.5 Credit assignment for use counts
- If every retrieval counts as a use, passengers get reinforced. In ALFWorld only 5.9% (10 of 169) of retrieval-credited successes were marginal helps (d13, abstract only). So increment the count when the memory is cited or changes the answer, not when it is merely retrieved. This is an inference from one abstract.

### 5.6 Moderators and boundary conditions
- Repeat share of the stream: base-level terms pay when repeats are 72-89% of targets (c13). Where targets are mostly new, they do not.
- Whether the stream has a newest-is-right bias: LoCoMo temporal questions favour recent facts by design, so decay gains there may be benchmark-specific (c08).
- Benchmarks where every query touches every memory (LoCoMo) cannot show frequency or retention effects (c10).
- Task type: A3-Bench shows that supplying the correct activated memory lifts ten LLMs by 13.48 points on average (34.71 to 48.19%), but that is an oracle, not a ranker (b25).
- Narrative text: recall depends on gist fit with the whole story and shows no primacy effect (c17). Activation history is not the whole story for text.

### 5.7 Interventions that worked
- Spaced re-presentation at high frequency (b08, field, N = 64).
- Dedup before indexing (a25).
- Retrieval quality over write quality: hybrid + rerank 77.2% vs BM25 57.1% (c06).
- Graph spreading with fan on LoCoMo (d01), with the caveats above.

## 6. Language models

What we know, by what was measured.

### 6.1 Ranker used in practice
- Generative Agents (Park et al. 2023, a19, b14, c01, c02 [V]): recency (0.995 per game hour since last retrieval) + importance (LLM 1-10) + relevance (cosine), each min-max scaled, all weights 1. 25 agents, 2 game days, 100 raters. TrueSkill: full 29.89 (sigma .72), no reflection 26.88, no reflection or planning 25.64, human crowd-worker 22.95, none 21.21. H(4) = 150.29, d = 8.16. Ablations are whole modules. No retrieval-term ablation exists. No frequency term.
- MemoryBank (Zhong et al. 2023, a21, b17, c03 [V]): R = e^(-t/S), S + 1 per recall, reset t. 194 probing questions (97 English, 97 Chinese). Table 2 (confirmed in critique): English retrieval/correctness: ChatGLM .809/.438, BELLE .814/.479, ChatGPT .763/.716. Chinese: .84/.418, .856/.603, .711/.655. Authors call the forgetting model "exploratory and highly simplified". No forgetting ablation.
- Aschenbrenner 2026 (a23 [V]): S = 3.0 max(0, 1 - 0.1 t_creation) + 2.0 ln(1 + N_access) + 1.5 max(0, 1 - .05 t_last), times an emotion multiplier. Video study N = 43: sociability d = .60. Memory vs no memory, not term vs term.

### 6.2 Use-history scoring vs Park
- Hou et al. 2024 (b15, b16, c04, d06 [V]): recall probability p(t) = (1 - exp(-r e^(-t/g))) / (1 - e^-1), threshold .86. 10 author-built tasks, 4 candidate events each. Paired t = -5.687, p = .000299, CI [-0.27, -0.12]. Task 0 (a concert breaks the Thursday habit): recall-count model picked the habit (University .850 vs Home .830, Library .836, Restaurant .836); Park picked the recent one-off (Restaurant 1.620 vs University 1.489). Both wrong. Elapsed times 55,800 to 434,700 s.
- Honda et al. 2025 (d05 [V abstract]): ACT-R-inspired agent (temporal decay + semantic similarity + noise), HAI '25, DOI 10.1145/3765766.3765803. Abstract only. No numbers, no baseline.
- Sievers & Russwinkel 2025 (a24 [V]): real pyactr memory with gpt-4o-mini chunks, pasted into prompts. "Unsatisfactory level of reliability"; no quantitative evaluation.
- No head-to-head of Park vs true base-level vs hybrid exists (K22).

### 6.3 Graph and spreading
- SYNAPSE (b19, c07, c08, d01-d04 [V]): LoCoMo, GPT-4o-mini, weighted F1 over four non-adversarial categories, N = 500, paired t p < .05. Synapse 40.5, Zep 39.7, MemoryOS 38.0, LangMem 34.3, AriGraph 33.7, A-Mem 33.3, MemGPT 28.0. Ablations: no node decay 30.7 (temporal 50.1 to 14.2); no fan 36.1 (open domain 25.9 to 16.8, multi-hop 35.7 to 30.2); no activation dynamics 30.5; vectors only 25.2; no lateral inhibition: adversarial 96.6 to 71.5. Other backbones, same authors: GPT-4o 43.4 vs A-Mem 36.1; Qwen-3b 36.6 vs 22.1. About 814 tokens per query vs 16,910. Low-similarity subset (cos < .3): Synapse falls 7.4%, A-Mem 56.3%. Sensitivity delta .3/.5/.7: 40.0/40.5/38.1. Important correction (d04): the "decay" is a per-step leak (1 - delta) a on graph activation, with delta .5 over T = 3 steps. Time enters only through edge weights exp(-rho |dt|), rho = .01. There is no use count. So it supports time-aware spreading on LoCoMo, not base-level learning.
- SynapticRAG (b18 [V]): up to +14.66 over RAG (avg 10.41); removing temporal integration -9.90, stimulus propagation -4.35, fixed time constant -10.54. Dialogue sets built for temporal questions. Not ACT-R.
- FadeMem (c09, d08 [V]): stretched exponential, beta .8 long-term, 1.2 short-term, importance = alpha relevance + beta f/(1+f) + gamma exp(-delta dt). 82.1% of critical facts at 55.0% storage vs Mem0 78.4% at 100%. Multi-hop F1 29.43 vs Mem0 28.37. Dropping the dual layer: 19.45; dropping fusion: 13.63. Modules ablated, not the frequency term.

### 6.4 Decay with reinforcement, accessibility not deletion
- OBLIVION (c11, d07 [V]): R = exp(-n/S), S = (utility + frequency + eps) T, n = turns since reinforcement. LongMemEval S, GPT-4.1-mini: 90.60 vs 89.00 baseline; up to 73% token-cost cut. Hierarchy: L2 only 86.40, L2 + L3 89.60, all 90.60. GoodAILTM 2K buffer 60: T = 1: 8.41, 3: 6.97, 5: 6.69, 10: 7.78, 20: 6.88, 50: 6.55. Text says T = 10 best; table says T = 1. No decay on/off ablation.
- CAMeR (c10, d09 [V]): decay .99 per round, +.2 reinforcement. 76 memories, 8 clusters, 100 rounds, query counts 0 to 37. Retention gap, keyword-gated .039 vs embedding-only .024 (1.6x). Top-5 retrieval saves 83.2% tokens (39k vs 231k). Scores weights, not answers.
- Kerestecioglu (a25 [V]): see 5.4. LongMemEval M tier: raw RAG 71.2 [67.2, 75.0]; pipeline 200K 70.1, 115K 65.6, 50K 49.2, 25K 38.8.

### 6.5 Benchmarks and measurement
- Yuan 2026 (c06 [V]): 1,540 non-adversarial LoCoMo questions, k = 5, 3 x 3 grid. Retrieval failure 11 to 46% of questions. Write strategies differ by 3 to 8 points; retrieval methods by up to about 20.
- MemoryAgentBench (d11 [V]): selective forgetting (overwrite), at most 28% on multi-hop. Tests recency of fact, not frequency.
- Preprint cost-retention study (d12 [M]): BM25 39.4% vs full context 30.6% (n = 160, p = .09). Power analysis: 360 to 430 questions to confirm a gap this size (K30).
- Hindsight (b22 [M]): four-network memory, 91.4% LongMemEval, 89.61% LoCoMo; no decay term.
- A3-Bench (b25 [V]): oracle activation lifts ten LLMs 34.71 to 48.19 average.
- Ji-An 2024 (c18 [V]): induction heads act like the CMR model; ablating them hurts in-context learning more than random heads. That is memory inside the model, not an external store, and not ACT-R.

### 6.6 Summary of what changed behaviour, and by how much
- Retrieval method: up to about 20 points (cosine vs BM25) on LoCoMo.
- Time-aware spreading: up to 15 points (SynapticRAG, best case), 9.8 average F1 for removing the leak (SYNAPSE), on temporal benchmarks.
- Use-count scoring over Park: significant on 10 small tasks, not replicated.
- Delete-on-decay: minus up to 30 points on LongMemEval.
- Token savings are the most reliable benefit: 73% (OBLIVION), 83% (CAMeR top-5), about 95% (SYNAPSE 814 vs 16,910).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **Memory: rank, do not delete.** Use scores to order and cap what is shown; never drop a lesson from the store by decay. [E] K12; a25, c10, d07, d09. Supports G7 (pay for itself) and keeps the lessons store intact.
2. **Memory: retrieval quality first.** Spend effort on the similarity and rerank step before any decay term. Raw entries retrieved well match extracted summaries. [S, one benchmark, with d12 pointing the same way] c06, d12. Schema part: memory.
3. **Memory: deduplicate before indexing.** [E] a25 (dominant mechanism on VSCode, critique correction). Cheap, no model call.
4. **G7: size tests properly.** Any retrieval-term test uses 400+ questions or paired replays; do not trust a few points on LoCoMo-sized sets. [S] K30, d12.
5. **Memory: embedding cosine is an adequate spreading term; do not expect it to beat a tuned linear model.** [E] K15; b20, c15.
6. **Memory: parameter humility.** Fix d near 0.5 and report at d in {0.3, 0.5, 0.7} with repeated seeds. [E] K16; b09, b10, d03.
7. **Memory logging (section 6 of schema): log per-memory use events with a flag for "cited in final answer".** Needed for every test below. [E] as a requirement; d13 explains why the flag matters.
8. **Do not claim ACT-R support for existing systems.** Park is not ACT-R; SYNAPSE decay is a leak. [E] a20, d04.

### Test first (not yet established; all candidates also appear in UNKNOWNS.md)
1. **Memory: add a use-count / base-level term to the Park-style score.** [S] K06, K07, K22; a19, a20, b15, c04. The core experiment.
2. **Memory: power vs exponential recency at ranking.** [C] K02, K24; b02, d10.
3. **Memory: decay clock (wall vs turns vs intervening events).** [S] K05, K23; a12, d15.
4. **Memory: rank-only vs delete.** [S] K26; a25, d07, d09.
5. **Memory: count a use only when cited.** [S] K27; d13.
6. **Memory: goal or explicit-statement term for exceptions.** [S] K25; d06.
7. **Memory: spacing-aware count (gap-gated).** [E for humans, untested for LLMs] K03; a04, a08, b08.
8. **Memory: fan penalty on shared cues.** [S] K10; d01, d04.
9. **Memory: partial-match / near-neighbour guard.** [S] a17 (human); no LLM test.
10. **S/O: none.** ACT-R declarative memory does not give a new state or operator. Production selection and compilation are other subfields.

## 8. Concrete tests on our bench

Common design: same memory store, same top-k and token budget in all arms (count prompt tokens including the memory block); same model, three seeds; paired comparison per item; 400+ items per test or paired replays (K30). Score by answer accuracy first, retrieval NDCG or hit rate at k second.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Multi-session store, about 80 memories, 20 sessions, 100-200 questions with graded reuse (K29 design) | A: cosine only; B: Park (recency + importance + cosine); C: B + ln(use-count) base-level; D: ACT-R B + cosine | Answer accuracy; NDCG@5; tokens to correct | C or D beat B by 2-5 points when repeats are over 70% of targets; no gain or a loss when targets are mostly new (c13). Guess, not measured |
| T2 | Same replay | Decay form: power a^-0.5, exponential, stretched | NDCG@5, held-out | Within 1 point; if so keep the simpler form |
| T3 | Same replay | Clock: wall time, turns, intervening memory events | NDCG@5 | Events or turns beat wall time when idle gaps are long (a12) |
| T4 | Same replay | Rank-only vs delete-below-threshold vs neither, same token cap | Accuracy; store size | Rank-only at least equals neither; delete worse (a25: -30 points aggressive) |
| T5 | Same replay with irrelevant retrieved passengers | Count-on-retrieval vs count-on-cited | Accuracy over late sessions | Count-on-cited keeps ranking cleaner (d13); expect a 1-3 point gain (guess) |
| T6 | 20 announced exceptions on habitual slots (Hou Task 0 style) | Park, base-level, base-level + explicit-statement boost | Accuracy on exception items | Both base terms fail; boost fixes. Habit items must not regress |
| T7 | Bursty vs spread reuse (equal counts) | Plain count vs gap-gated count | Recall at 1-week lag | Gap-gated better on spread items (a04, b08); needs a long replay |
| T8 | Low-similarity queries (cos < .3) | Cosine vs cosine + fan-penalised spreading | Accuracy | Spreading helps most there (d04: -7.4% vs -56.3%) |
| T9 | LoCoMo-type and one benchmark with older-fact-right items | SYNAPSE-like leak on and off | F1 | Gain on temporal items, loss where old is right (c08 bias) |
| T10 | d sweep | d in {0.3, 0.5, 0.7}, 3 seeds | Accuracy | Spread below seed noise (d03: up to 2.4 F1) |

Cost note: T1-T5 reuse one replay file. Build the replay once. This also satisfies G7: every element must beat the plain model at equal tokens, counting setup.

## 9. What does not transfer, and why

- Human timescales. ACT-R decay is fitted to seconds to months of human practice. An agent's "time" is turns; its store is lossless text. Forgetting is a human limit; for an agent it is a ranking device only (K12).
- Deletion. Forgetting has a function in people (clears interference, frees capacity). In an agent with a text store and a context cap it mostly loses information (a25).
- Latency prediction. ACT-R predicts retrieval time. For an LLM, retrieval time is not a decision variable.
- Noise as realism. Stochastic retrieval reproduces human variability but adds error for an agent. Keep noise off in evaluation.
- Practice-dependent decay (Pavlik-Anderson). Costs parameters, contested in humans (b03, b04), and probably unnecessary for an agent (inference).
- Working-memory pool. The source-activation limit explains human cue overload. LLM context overload is a different mechanism, covered in other subfields.
- Frequency as truth. In people, frequent facts are usually the ones needed (a02). For an agent, frequent retrieval can be self-reinforcing (passenger credit, d13) and cannot distinguish a habit from an exception (d06).
- Gist. Human narrative recall depends on fit with the whole story (c17); an activation score ignores that.
- Fits are small N and in-sample: 20 per group (a08), 5 per cell (a13), cells of 11-14 (b08), 1 subject (b01).

## 10. Open questions

1. Does adding a use-count / base-level term to Park scoring raise accuracy at equal tokens on a stream with real reuse? (K22; no study.)
2. Best clock for agents: wall time, turns, or events? (K23.)
3. Power vs exponential at ranking? (K24.)
4. Rank-only vs delete at equal tokens? (K26.)
5. Does SYNAPSE's fan and decay gain replicate on a benchmark where the older fact is sometimes right, and by other authors? (K10.)
6. Does practice-dependent decay survive the Slamecka-McElree replications, and does it matter for an agent? (K04.) Averell & Heathcote 2011 and Murre & Chessa 2011 not opened in full.
7. What did Honda et al. 2025 measure? (d05, abstract only.)
8. How big is the effect of noise and of d? No noise sweep exists. (K28.)
9. How to handle exceptions: explicit-statement term, goal term, or something else? (K25.)
10. Is the Rocchi passenger result general beyond ALFWorld? (K27, abstract only.)
11. Is there a published, answer-level use-history benchmark? CAMeR is weights only (K29).

## 11. Sources

[V] opened (full text or a page read this session); [M] snippet or abstract only.

- [V] Anderson & Schooler (1991) Reflections of the environment in memory. https://dyurovsky.github.io/learning-humans-machines/class/13-class/papers/anderson1991.pdf (a01-a06)
- [M] Anderson & Milson (1989) Human memory: an adaptive perspective (via the 1991 paper). Same URL (a07)
- [V] Pavlik & Anderson (2004) An ACT-R model of the spacing effect. https://www.gwern.net/docs/www/act-r.psy.cmu.edu/f4b85d71f1bd93309c094119607097a071bb09e3.pdf (a08-a10)
- [V] Anderson, Fincham & Douglass (1999) Practice and retention: a unifying analysis. https://cenl.ucsd.edu/Jclub/Anderson_1999.pdf (a11-a14)
- [V] Anderson, Reder & Lebiere (1996) Working memory: activation limitations on retrieval. https://www.cmu.edu/dietrich/psychology/memorylab/publications/96_jra_lmr_cl.pdf (a15, a16)
- [V] Lebiere, Anderson & Reder (1994) Error modeling in the ACT-R production system. https://www.cmu.edu/dietrich/psychology/memorylab/publications/94_cl_jra_lmr.pdf (a17)
- [V] Lovett, Daily & Reder (2000) A source activation theory of working memory. https://www.cmu.edu/dietrich/psychology/memorylab/publications/00_mcl_lzd_lmr.pdf (a18)
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (a19, a20, b14, c01, c02)
- [V] Zhong et al. (2023) MemoryBank. https://arxiv.org/abs/2305.10250 (a21, b17, c03)
- [V] Alqithami (2025) Forgetful but Faithful. https://arxiv.org/abs/2512.12856 (a22)
- [V] Aschenbrenner et al. (2026) Not Forgotten (robot head Kim). https://arxiv.org/abs/2607.24190 (a23)
- [V] Sievers & Russwinkel (2025) Personalized interactions with a social robot. https://ceur-ws.org/Vol-4058/paper6.pdf (a24)
- [V] Kerestecioglu et al. (2026) Human-inspired memory architecture for LLM agents. https://arxiv.org/abs/2605.08538 (a25)
- [M] Uddin et al. (2026) From recall to forgetting. https://arxiv.org/abs/2604.20006 (a26)
- [M] pensyve-core activation.rs. https://docs.rs/crate/pensyve-core/1.2.0/source/src/activation.rs (a27)
- [V] Murre & Dros (2015) Replication and analysis of Ebbinghaus' forgetting curve. https://pmc.ncbi.nlm.nih.gov/articles/PMC4492928/ (b01, b02)
- [V] Rivera-Lares et al. (2022) Rate of forgetting is independent of initial degree of learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC8735725/ (b03)
- [V] Cohen-Dallal, Fradkin & Pertzov (2018) Are stronger memories forgotten more slowly? https://pmc.ncbi.nlm.nih.gov/articles/PMC6044536/ (b04)
- [V] Stocco et al. (2023) ACT-R declarative memory and its neurobiology. https://pmc.ncbi.nlm.nih.gov/articles/PMC13292821/ (b05)
- [V] Autry & Levine (2014) A fan effect in anaphor processing. https://pmc.ncbi.nlm.nih.gov/articles/PMC4114326/ (b06)
- [V] Pirolli (2016) Self-efficacy and daily adherence in mHealth. https://pmc.ncbi.nlm.nih.gov/articles/PMC5110491/ (b07)
- [V] Pirolli et al. (2017) Implementation intention and reminder effects. https://pmc.ncbi.nlm.nih.gov/articles/PMC5730820/ (b08)
- [V] Kangasraasio et al. (2019) Parameter inference for cognitive models with ABC. https://pmc.ncbi.nlm.nih.gov/articles/PMC6593436/ (b09)
- [V] van der Velde et al. (2022) LBA for ACT-R memory parameters. https://pmc.ncbi.nlm.nih.gov/articles/PMC9790673/ (b10)
- [M] Averell & Heathcote (2011) The form of the forgetting curve (abstract read, d10). https://doi.org/10.1016/j.jmp.2010.08.009 (b12, d10)
- [M] Murre & Chessa (2011) Power laws from individual differences. https://doi.org/10.3758/s13423-011-0076-y (b13)
- [V] Hou, Tamoto & Miyashita (2024) My agent understands me better. https://arxiv.org/abs/2404.00573 (b15, b16, c04, d06)
- [V] Hou et al. (2025) SynapticRAG. https://arxiv.org/pdf/2410.13553v2 (b18)
- [V] Jiang et al. (2026) SYNAPSE. https://arxiv.org/html/2601.02744v1 (b19, c07, c08, d01-d04)
- [V] Meghdadi, Duff & Demberg (2026) Embedding cosine in ACT-R. https://www.frontiersin.org/journals/language-sciences/articles/10.3389/flang.2026.1721326/full (b20, c15)
- [V] Innerebner et al. (2025) Hybrid personalization with ACT-R modules (vision paper). https://arxiv.org/html/2505.05083v1 (b21)
- [M] Latimer et al. (2025) Hindsight is 20/20. https://arxiv.org/abs/2512.12818 (b22)
- [V] Settles & Meeder (2016) A trainable spaced repetition model. https://aclanthology.org/P16-1174.pdf (b23)
- [V] Sumers et al. (2023) CoALA. https://arxiv.org/abs/2309.02427 (b24, c05)
- [V] A3-Bench (2026). https://arxiv.org/pdf/2601.09274 (b25)
- [V] Yuan, Su, Yao (2026) Diagnosing retrieval vs utilization bottlenecks. https://arxiv.org/abs/2603.02473 (c06)
- [V] Wei et al. (2026) FadeMem. https://arxiv.org/abs/2601.18642 (c09, d08)
- [V] Lai (2026) CAMeR. https://arxiv.org/abs/2607.20458 (c10, d09)
- [V] Rana et al. (2026) OBLIVION. https://arxiv.org/abs/2604.00131 (c11, d07)
- [V] PISA (2024) Transformers meet ACT-R, with the Moscati and Reiter-Haas work as summarised in its related work (secondhand). https://arxiv.org/abs/2408.16578 (c12, c13)
- [V abstract] Honda et al. (2025) Human-like remembering and forgetting in LLM agents (HAI '25). https://doi.org/10.1145/3765766.3765803 (c14, d05)
- [V] Stocco et al. (2024) Fitting cognitive architecture models using likelihood. https://arxiv.org/abs/2410.18055 (c16)
- [V] Georgiou et al. (2023) Large-scale study of human memory for meaningful narratives. https://arxiv.org/abs/2311.04742 (c17)
- [V] Ji-An et al. (2024) Linking in-context learning to human episodic memory. https://arxiv.org/abs/2405.14992 (c18)
- [V] Hu et al. (2025) MemoryAgentBench. https://arxiv.org/html/2507.05257 (d11)
- [M] Anon. (2026) Retrieval beats cheap structured memory. https://doi.org/10.20944/preprints202608.1369.v1 (d12)
- [M] Rocchi (2026) Does memory credit travel? https://doi.org/10.2139/ssrn.7160321 (d13)
- [M] Maurya (2026) Beyond the single forgetting curve. https://doi.org/10.2139/ssrn.6933638 (d14)
