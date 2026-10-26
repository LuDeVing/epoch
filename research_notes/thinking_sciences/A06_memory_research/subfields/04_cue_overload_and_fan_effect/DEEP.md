# Cue overload and fan effect: deep document

*Subfield A06.04. Written from evidence_a-d.jsonl (ids a01 to d24), claims.jsonl (A06.04-K01 to K34) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Evidence ids are cited as a01, b12, K04 and so on. Every number below was checked in the critique unless marked "second-hand".*

---

## 1. What it is

**Cue overload** is the rule that a retrieval cue works worse the more items are filed under it. The cue does not get weaker with age. It gets weaker because it now points to many things, and they compete.

**The fan effect** is the same rule seen in a lab task. The "fan" of a concept is the number of facts attached to it. A person who is in one place has fan 1. A person who is in three places has fan 3. People answer slower and less accurately as fan goes up. The cost is large for the first extra item and smaller after that.

Why it matters for our agent. Our agent will keep a library of notes (lessons by problem class, helper rules, past results). The size of the set under one cue (one problem class, one entity, one tool name) is the thing the research says will hurt retrieval. Not the age of a note. Not the total library size by itself.

Three things must be kept apart:

| Term | What is counted | Who studies it |
|---|---|---|
| Fan (count of facts per cue) | how many different facts share one cue | Anderson 1974; ACT-R |
| Proactive interference by overwrite | how many earlier values the same key had | Watkins and Watkins 1975; PI-LLM |
| Distractor load in retrieval | how many near-miss passages sit beside the answer | RAG studies |

They look alike, and the LLM literature mixes them. The first is a set of different true facts. The second is a stack of replaced values. The third is a pool of wrong candidates. The cure differs for each: a set can be grouped or integrated, a stack can be superseded, a pool can be filtered.

Scope of the evidence. The human side is rich (50 years, many labs). The LLM side is young (2024 to 2026), mostly preprints, mostly synthetic key-value tasks, and mostly fan 1 to 2 for the true fan paradigm. The decision-relevant range for a library (5 to 50 notes per cue) has no direct data (critique, GAPS 1).

Links to parallel subfields, not covered here: Heuristics and biases; Generation versus evaluation; Plans and schemas; Gist extraction by overlapping replay; Value of information; Belief revision (AGM); Non-monotonic and default logic; Diagnosticity of evidence; Outside view and base rates; Novelty and atypicality. The sleep, interference-page and long-context material in earlier A06 documents also overlaps; see 00_FIELDS.md.

---

## 2. History and theories in depth

### 2.1 Cue overload (1975)

Watkins and Watkins (1975, JEP: Human Learning and Memory 1:442-452) explained "buildup of proactive inhibition" as a cue effect. In short-term recall, trial after trial uses the same cue. Later trials fail not because old items interfere in general, but because the cue now points to more items. [a01, d23; not opened. No numbers recorded. Do not quote cells.]

Tehan and Humphreys (1996) add a boundary: proactive interference shows only when the interfering and target items fall under the same cue. Category-dominance effects parallel PI effects. [a18, abstract page only.] A later Japanese test (second-hand, search summary) found 4-item conditions beat 8-item conditions on every trial. [d23, not opened.]

### 2.2 The fan effect (1974)

Anderson (1974, Cognitive Psychology 6:451-474) had people learn person-location sentences ("A hippie is in the park") and then judge probes. Three experiments, 26 study sentences, 16 persons and 16 places. Probe time rose with the number of facts attached to the person or the place. [a02, d22, a20; original not opened; cell values not recorded.]

Anderson (1983, Science 220:25-30), read in full:
- Subjects memorise 26 sentences and are drilled to perfect recall. Fan runs 1 to 3. RT rises with the fan of the person and of the place, for targets and for foils. [a03]
- Targets are about 100 ms faster than foils. Extracted column means 1.204 s (targets), 1.308 s (foils). Table text was garbled, so cell mapping is approximate. [a03]
- The effect holds for real-world knowledge (senators: 2.16 s for Kennedy vs 2.50 s for Bayh, uncontrolled), faces, and many materials. Learning new fantasy facts about a famous person slowed retrieval of old true facts about him (Lewis and Anderson). [a08]

### 2.3 Spreading activation with limited capacity (Anderson 1983)

Each concept has a fixed capacity to spread activation. More links out means less activation down each link. Activation spreads in parallel from every concept in the probe. A rival model, access from one concept only, predicts a fan effect of one concept; the data show about equal effects of both, so parallel access is favoured. [a04]

Foils are rejected by a waiting process. The system waits a set time for activation to intersect. If none does, it says no. The wait is longer for high-fan probes, so foils also show fan. King and Anderson: foils that share a subject with a studied sentence are much slower and more error-prone than unconnected foils, while targets do not differ. The shared cue creates a spurious intersection. [a05]

### 2.4 Strength, not count (Anderson 1983)

Relative strength drives the effect. With equal study frequency, a 2-fan and a 4-fan fact differ little. With equal fan, a fact studied 3 times beats one studied once by a lot. An unpublished result: a 2-fan fact studied 4 times is slower when its sibling was studied 8 times than 2 times. Under normal study the strength share is 1/N. [a06]

Practice removes the effect. Over 25 days, 24 test presentations a day (about 600 per sentence), recognition time fell as a power law to the same asymptote for fan and no-fan sentences. No-fan fit: T = 0.36 + 1.15 P^-0.51 (seconds, P in days). Same exponent, same asymptote 0.36 s. Only 8 sentences per condition, learned to perfect recall first; exact fan-condition coefficients were lost in extraction. [a07]

### 2.5 The paradox of the expert and the integration boundary

More knowledge should slow retrieval, but experts are often faster. Anderson credits practice and organisation. [a08, b20]

No fan effect when facts can be integrated into one theme and foils are unrelated. Smith et al.: Marty with 2 facts vs 2 plus an integrated third showed no difference; a third unrelated fact slowed responses. Reder and Anderson: the fan effect returns when foils are related, because a consistency judgment is no longer enough. Two themes about one person slow judgments versus one theme, but the number of facts in the irrelevant theme did not matter. [a09]

### 2.6 Mental-model rival (Radvansky and Zacks)

Facts that fit one situation (many objects in one location) show no fan on that dimension. One object in several locations needs several models and shows fan. Young adults: single-location RT 1395, 1448, 1415 ms for 1, 2, 3 associations; multiple-location 1441, 1615, 1853 ms. Old adults: multiple-location 1833, 1975, 3209 ms with errors 3.9, 9.3, 18.5 percent; single-location 1811, 1772, 1867 ms. 32 young, 32 old, 18 sentences. Condition x interference F(2,124) = 22.5. [a16, from Radvansky, Zacks and Hasher 1996] A 2002 Chinese replication with changed materials found no fan effect for "multiple persons have a single object" (search snippet only). [b26]

### 2.7 The test that split the theories (Sohn et al. 2004)

Mental-model theory says the focused (organising) dimension should show a smaller fan effect. ACT-R says larger, because focus raises that cue's attention weight. Result: person-focus group (N=19) slope 98 ms vs 63 ms on the other dimension, t(18)=2.59; location-focus group (N=17) 118 vs 73 ms, t(16)=2.80. Fan F(2,68)=56.80 for the focused and 30.91 for the non-focused dimension. 28 study sentences, 168 targets and 168 foils, fans 1 to 3. Accuracy fan effect for non-focused targets F(2,70)=36.08; for foils not significant (p>.70), which the authors cannot explain. [a15, b01, b02] One lab, small samples. The two theories do not agree on the materials, so material choice matters (b03).

### 2.8 ACT-R formalisation and the working-memory link

Chunk activation A = B + sum of W_j S_ji. Association S_ji = S - ln(fan_j). Retrieval time = F e^-A. Source activation W is split equally over sources. [a10] Anderson, Reder and Lebiere (1996) put the working-memory limit here: a fixed total of source activation, sum W_j = constant, is shared by all cues in focus. More concurrent load leaves less per cue. Odds = C e^(cA); time = B e^(-bA). Two experiments (digit span while solving equations; Exp 1 N=15). Harder either task hurt both. Most errors were misretrievals of similar active chunks. The scale of source activation is not identified by the data. [a14]

Individual differences. Cantor and Engle (1993): low-span people show a larger fan; with thematically related sentences high-span showed a negative fan (snippet only). Bunting, Conway and Heitz (2004) favour attentional control over capacity (abstract-level, not opened). [b24, b25]

### 2.9 Response-signal and dual-process work

Schneider and Anderson (2012): N=10 CMU subjects, 5 daily sessions, 32 person-location facts (half fan 1, half fan 2) from 24 persons and 24 locations; trials with lag RT under 100 or over 350 ms dropped (5.7 percent). Fan lowered the asymptote or the rate of rise, or both. Fan 1 beat fan 2 mostly at intermediate lags and the gap closed at the longest lag. ACT-R fit as well as the best descriptive model (mean adjusted R2 .921 individual, .981 group on Wickelgren and Corbett d-prime data). [a11, a12]

Field consensus as stated by them: fan effects hold for fictional facts, real knowledge, faces, alphabet arithmetic, in RT, accuracy and imaging. The accuracy cost is mainly more false alarms; hit rates are mixed (Dyne et al. 1990; Verde 2004). [a13]

Verde (2004): overlapping pairs (A-B, A-D) hurt recall but have inconsistent effects on recognition. Interference lowers recollection and raises familiarity, so false alarms always rise while hits can rise or fall. Three experiments; numbers not extracted. [a19, abstract only]

Anderson and Reder (1999) revised the account: fan depends on association strength and attention weights; absent fan with integrated material is explained in the same retrieval mechanism. [a17, b23: image scan, not read.] Reder's lab argues the size of the fan is set by process, not by representation. [b27, 403, not opened]

### 2.10 Recent human work

Link, van Maanen and Dotlacil (2025): fan persists with semantically similar concepts in natural Dutch. Exp 1 N=134 (46 lab, 88 online), fan 2 vs 4: longer RT and lower accuracy at fan 4. Exp 2 N=97 online, similar concepts: longer RT, accuracy high everywhere (possible ceiling). Poster abstract only. [b19]

Guo, Wu and Yiu (2026, preprint; arXiv id 2606 vs stated date 9 May 2026 do not match): N=112 online humans (Prolific, 120 recruited), 60 sentences at 5 s each, fan 1, 2, 4 only. Accuracy 91.2, 82.4, 71.8 percent. d' 2.84, 2.21, 1.67. Cohen d = 1.12 [0.89, 1.35]. Log slope 0.41 [0.35, 0.47]. [a27, b04, b05] This is the only direct comparison of log vs power forms (see 4.2).

### 2.11 Timeline

| Year | Event |
|---|---|
| 1974 | Anderson fan paradigm |
| 1975 | Watkins and Watkins cue overload |
| 1977, 1981 | Wickelgren and Corbett; Dosher response-signal studies (second-hand) |
| 1983 | Anderson spreading activation, strength, practice |
| 1991 to 1996 | Radvansky and Zacks mental models |
| 1996 | Anderson, Reder, Lebiere: fan as working-memory limit |
| 1999 | Anderson and Reder revision |
| 2004 | Sohn et al. differential fan; Verde dual-process |
| 2012 | Schneider and Anderson response-signal ACT-R |
| 2024 | Roberts et al. first LLM fan test; Cuconasu et al. distractors in RAG |
| 2025 | PI-LLM (Wang and Sun); Cao et al. LLM memory effects; Link et al. Dutch |
| 2026 | Chattaraj and Raj (39 models); Guo et al. log-fan; CMI; Supersede; xMemory; Context Rot era benchmarks |

---

## 3. Core findings with exact numbers

Status uses the claims file: E established, S single-source, C contested. "Human" means people.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Fan slows people and lowers accuracy | Fan 1 to 3 on 26 sentences; foils about 100 ms slower than targets (means 1.204 s vs 1.308 s as extracted) | Anderson 1983 (a03) | E (K01) |
| Fan effect in a modern large online sample | Accuracy 91.2, 82.4, 71.8 percent at fan 1, 2, 4; d' 2.84, 2.21, 1.67; N=112 | Guo et al. 2026 (b05) | E for direction, S for the shape (K02) |
| Fan holds with similar concepts | Exp 1 N=134, Exp 2 N=97; RT rose in both; accuracy loss in Exp 1 only | Link et al. 2025 (b19) | E (K01), abstract only |
| Accuracy cost is mostly false alarms | False alarms 23.1 percent humans vs 41.3 percent DPR at high competitor similarity (cos>0.7); 8.2 vs 12.4 percent at low similarity | Guo et al. (b06); Verde 2004 (a19) | E (K10) |
| Shared-cue foil is accepted/slowed | Connected foils much slower, more errors; targets unaffected | King and Anderson via Anderson 1983 (a05) | E (K11) |
| Log shape of the cost | Log beat power by BIC 18.4 (human), 23.1 (DPR), 15.7 (HippoRAG); model recovery right in 94 percent | Guo et al. (b06) | S (K02) |
| Indirect support for convex cost | First 10 percent of hard distractors caused 58 percent of the loss for Qwen2.5-7B (NQ, 128K); linear would be 10 percent | Gao et al. 2026 (d14) | S (K02) |
| Strength sets retrieval, practice erases fan | About 600 presentations per sentence; T = 0.36 + 1.15 P^-0.51 s; same asymptote 0.36 s | Anderson 1983 (a07) | S (K12) |
| Focused cue has the larger fan | 98 vs 63 ms (N=19), 118 vs 73 ms (N=17) | Sohn et al. 2004 (a15) | C (K14) |
| Integration removes fan | Young single-location 1395, 1448, 1415 ms vs multi-location 1441, 1615, 1853 ms | Radvansky and Zacks (a16) | C (K13) |
| Age magnifies fan | Old multi-location 1833, 1975, 3209 ms; errors 3.9, 9.3, 18.5 percent | a16 | S |
| LLM recognition fan at fan 2 | Accuracy 0.991 to 0.915 at list size 32; d' about 4.1 to 3.1 (GPT-4); human d' 3.7 to 2.5 is second-hand | Cao, Schooler, Zafarani 2025 (a21, b10) | E (K03) |
| LLM fan in probabilities only for some models | Only Mistral and SOLAR significant (p<=0.01 for absent items); none for GPT-2, Llama-2, RoBERTa; Llama-3 weak | Roberts et al. 2024 (b08, c01) | E (K03) |
| PI log-linear in LLMs | 46 keys, 3 to 400 updates, 30+ models, all fall log-linearly | Wang and Sun 2025 (a23, b12) | E (K04) |
| Not just length | Tracking more keys at fixed length: Llama-4-maverick near 100 percent with 2 keys, below 5 percent with 46. Context-length coefficient t = -0.144, p=.886 | Wang and Sun (b14, c04) | S (K05) |
| Value length hurts most | 10 words: under 40 percent for every model; 40 words: under 5 percent | Wang and Sun (a24) | S |
| Latest value is far worse than first | Cohen d=1.73; 39 of 39 models RIES>PIES; mean gap 69.5 points; PI falls 94 to 3 percent while RI stays 96 percent at N=50 | Chattaraj and Raj 2026 (c08) | E (K16) |
| Earliest value near ceiling | Earliest-state accuracy about 98 to 100 percent; latest collapses; gap large from T=32 to 128, plateau by 256; 13 models | Qiao et al. 2026 (c09) | E (K16) |
| Forget prompts barely help | Under 10 points at 100 updates; directed forgetting +1 point (Qwen2.5-32B 57.33 to 58.33) | Wang and Sun (b13); Qiao (c10) | E (K06) |
| Turn boundary helps a lot | Mock Q and A turn: Gemini Flash 2.0 at 150 updates matched baseline at 30 to 45 updates | Wang and Sun (b13) | S (K07) |
| Near-miss distractors hurt | Llama2 gold only 0.5642; 1 hard distractor far 0.4733; 8 far 0.3106; ADORE 0.4068, 0.3815, 0.3626 at 1, 2, 4; drops up to 0.38 (-67 percent) | Cuconasu et al. 2024 (b15) | E (K08) |
| Literal-overlap distractor | GPT-4o effective length falls to 1K | NoLiMa (c17) | E (K08) |
| Same-slot conflict | At count 8, lexical plasticity vs unrelated: repeated history -0.32 [-0.46, -0.20]; same-slot -0.48 [-0.62, -0.34]; unrelated -0.02 | Ding et al. 2026 CMI (c14) | E (K08, K18) |
| Unrelated load is cheap, with exceptions | Llama2 near position 0.5642 to 0.5681 (6 random, not significant) and 0.5859 (14 random, significant); dense retriever unrelated -0.18; MPT and Falcon differ | Cuconasu (b16); CMI (c14) | C (K09) |
| Middle position loses about 20 points | GPT-3.5, 20 docs: index 0 75.8, index 9 53.8, index 19 63.2 percent; closed-book 56.1 | Liu et al. (b17) | E (K15) |
| Gold nearest the query is best | 18 distractors: near 0.3781, far 0.2348, mid 0.1795 | Cuconasu (b16, c20, critique) | E (K15) |
| Long-context cue weakness | NoLiMa: 11 of 13 models under 50 percent of base at 32K; GPT-4o 99.3 to 69.7 | Modarressi et al. 2025 (b18) | E (K08) |
| Tool library bloat | 43.13 percent (top-1 vector) vs 18.20 (keyword prefilter) vs 13.62 (all tools) | RAG-MCP (a26) | S (K19) |
| Best k depends on reader | FLAN-T5 and GPT-3.5 plateau near k=10; Llama and Claude-3-haiku peak below 5 and then decline | RAGGED (d11); Jin et al. (d12); Leng et al. (d13) | E (K27) |
| Dedupe pays only with redundancy | Clean pools lose 0.7 to 33.0 S-Recall points; heavy redundancy gains +13.6 to +24.1 | Brouillette et al. 2026 (d03, d04) | S (K28) |
| Grouping by cue helps agent memory | xMemory F1 43.98 vs naive RAG 36.48 at 4,711 vs 8,633 tokens (Qwen3-8B, LoCoMo); cap 12 beats 8, 10, 14 | Hu et al. 2026 (d05, d06) | S (K29) |
| Fan-divided activation in retrieval | SYNAPSE weighted F1 40.5 vs 33.3; removing fan: open-domain F1 25.9 to 16.8; 814 vs 16,910 tokens | Jiang et al. 2026 (c16) | S (K21) |
| Models rarely say they are unsure | 8.6 percent of PI failures contain a refusal (0 under RI); 69 refusals in 194,480 calls (0.035 percent) | Chattaraj (c24); Chroma (d15) | E (K22) |
| Four-bit quantization worsens semantic PI | Qwen 81.0 to 68.3 percent (McNemar p<=2.6e-6); Mistral 44.0 to 37.4; Phi 61.8 to 54.0 | Shahrabi-Farahani and Rahmati (c11) | S (K23) |
| Agent memories add, rarely update | Insert in 76.8 percent of operations; best system average 33.4 percent | MINTEval (c15) | S (K24) |

---

## 4. Mechanisms and models

### 4.1 ACT-R fan model (implementable)

Inputs: a probe made of sources j (for example person, place). Each source j has a fan, the number of stored chunks it links to.

1. Association strength: S_ji = S - ln(fan_j). With S about the log of the largest fan.
2. Chunk activation: A_i = B_i + sum over sources of W_j * S_ji. Total source activation W = sum of W_j is fixed, so W_j = W / (number of sources).
3. Retrieval time: T = F * exp(-A). Probability of retrieving before the deadline falls as A falls (failure time F*exp(-threshold)). [a10]
4. Foils: recall-to-reject. Retrieve the best chunk, compare to the probe, say no on mismatch. Or wait a set time for intersection; the wait is longer for higher fan. [a05, a10]
5. Differential fan: raising W_j for the attended cue raises its fan cost. [a15]

What an engineer takes from this: cost per extra item is ln(fan), so doubling items under a cue costs a fixed amount (ln 2) in association strength. The first extra item costs the most per item.

### 4.2 Signal detection with log fan (Guo et al.)

d'(fan) = d0 - k * ln(fan). Fit k from accuracy at fan 1, 2, 4, 8. Competitor density and mean cue similarity enter as extra terms. Humans k/sigma = 0.41 [0.35, 0.47]; DPR 0.67 [0.58, 0.76]; ColBERTv2 0.53; HippoRAG 0.44 [0.37, 0.51]. System x fan interaction beta = -0.12, SE .03, p<.001. Competitor sensitivity 0.021 human, 0.058 DPR, 0.043 ColBERTv2, 0.024 HippoRAG. Parameter recovery r=.93 to .97 on 1,000 synthetic sets; cross-validated R2 .91 (human), .88 (DPR), .90 (HippoRAG). [a27, a28, b04, b06, c28] Provenance doubts; human fan 8 missing; only human vs DPR is clearly separated. Mechanisms (encoding specificity, temporal binding, retrieval gating) are untested hypotheses.

Per doubling the human loss is 8.8 then 10.6 points; DPR drops 17.8, 18.1, 13.5 (critique). So "9 to 18 points per doubling" holds only at low fan.

### 4.3 Attention weights and working memory limit

Fixed total source activation shared by every cue in focus (a14). An LLM analogue: the context is one shared budget; each competing item takes share. This is an analogy, not a measured mechanism. Wang and Sun infer "one anti-interference resource, separate from context window length" from three load axes (updates per key, number of keys, value length) that all give log-linear decline (a24).

### 4.4 Dual-process view

Interference lowers recollection and raises familiarity (Verde). So the test must count false accepts, not only misses. A "recall-to-reject" check, retrieve the full stored fact and compare, is how ACT-R rejects foils (a10).

### 4.5 Fan division in a retrieval graph (SYNAPSE)

Activation sent from a node is divided by its out-degree. Spreading factor S=0.8, temporal decay 0.01, lateral inhibition on competitors, top-k stable for k 20 to 40. Removing the fan term cut open-domain F1 25.9 to 16.8. Hub nodes are tamed by the division; lateral inhibition can cause tunnelling on simple queries. One benchmark (LoCoMo), one backbone (GPT-4o-mini). [c16]

### 4.6 Decoupling and grouping (xMemory)

Split history into units, group units, retrieve groups first, add raw text only if the reader's answer entropy stays high. Group cap sweep (Qwen3-8B, LoCoMo, BLEU/F1): cap 14 33.19/42.10 (383 groups, 7.47 per group); cap 12 34.48/43.98 (642, 4.48); cap 10 33.23/42.80 (805, 3.64); cap 8 32.13/41.21 (1,111, 2.58). The authors derived 12 from a Fano bound with an assumed 2 bits of routing signal, so the match is partly post hoc. Differences are 1 to 2.4 points, no CIs. Ablation: decoupled units with plain similarity 31.81/40.77 at 7,236 tokens; with group selection 32.55/40.64 at 6,321 (flat on F1); add uncertainty expansion 33.23/42.55 at 6,557. [d05, d06, d07]

### 4.7 Entropy gate for a second lookup

Compute next-token entropy of the answer. If high, retrieve more. Result: +1.42 BLEU, +1.78 F1, 679 fewer tokens (Qwen3-8B). Simple uncertainty estimators match complex adaptive-retrieval pipelines with under one retrieval call per question (LLaMA 3.1-8B; 35 methods, 6 datasets). Both fall short of an oracle. Closed models need a proxy model. Not tested on crowded cues. [d07, d08]

### 4.8 Write-time handling

Code-only supersede, release and purge primitives (FORGETEVAL, 385 adversarial cases): deterministic stores 70.1 to 70.7 percent on 345 cases; Mem0 76.2. Per category for LETHE: temporal_qualifier 37/37, recursive_supersession 36/39, substring_trap 33/36, identifier_obfuscation 2/38 (5 percent), cross_lingual_id 0/38. An LLM mutation hook (DeepSeek-V3) 93.3 percent on 345 (91.7 on 385), about 17 cents per 385 cases, 2.3 s per case against 64 to 191 ms. So a code rule is exact only when cues are canonical. [d09]

### 4.9 Why length alone also hurts

Du et al.: accuracy dropped 13.9 to 85 percent as input length grew within claimed windows, even with perfect retrieval, blank tokens or masked tokens; recite-then-solve improved GPT-4o by up to 4 percent on RULER (abstract page only). [d16] Chroma: 18 models, needles less similar to the question degrade faster, one distractor lowers accuracy. [d15] So there are two effects: competitor count under one cue (fan) and raw length. Control both in tests.

---

## 5. What holds up

### 5.1 Replications (human)

- Fan with fictional facts, real knowledge, faces, alphabet arithmetic, in RT, accuracy and imaging (a13). [E]
- Fan with semantically similar natural Dutch concepts, N=134 and N=97 (b19). [E, abstract only]
- Fan in a modern online sample, N=112, fan 1/2/4 (b05). Direction [E].
- Fan in response-signal accuracy, N=10 (a11). [E for direction, small]
- Fan for foils as well as targets (a03, b02). Exception: accuracy fan for foils in Sohn et al. was not significant (p>.70) and unexplained.
- Shared-cue foils are slower and error-prone (a05). [E]

### 5.2 Failures, contested points, moderators

| Point | What happened |
|---|---|
| Integration of facts | Fan vanishes with integrated material (a09, a16) but a Chinese replication with changed materials differed (b26, snippet) and ACT-R says the same retrieval mechanism explains it (a17). Contested (K13). |
| Which dimension has the larger fan | Mental models say focused is smaller; Sohn et al. found it larger (a15). One lab. Contested (K14). |
| Hit rates | Mixed in humans; false alarms are the reliable cost (a13, a19). |
| Individual differences | Low-span larger fan; related sentences can reverse it (negative fan); Bunting et al. challenge the capacity reading (b24, b25; not opened). |
| Age | Old adults much larger fan on multi-location facts (a16), none on single-location. |
| Practice | Removes the fan over about 600 presentations (a07). Small design. |
| Expertise | Paradox of the expert (a08, b20). |
| Hit-rate false alarms in LLMs | Not measured for fan beyond 2. |

### 5.3 LLM replications and failures

- The fan effect in LLM recognition replicates in direction at fan 2 with GPT-4 and 7 to 8B models (a21), but is small and has ceiling effects (0.99). Fan appears in token probability for 2 of 6 model families (b08). So the human fan does not transfer to every model.
- PI replicates across labs: Wang and Sun (30+ models), Chattaraj and Raj (39 models), Qiao et al. (13 models). Same shape, log-linear, in different tasks. [E]
- Size vs PI is disputed: Wang and Sun size class t=3.03, p=.005, N=30, Spearman .673 (p=.0016) in the 128-131k group, combined R2 .261; Chattaraj and Raj PI R2=.06 (p=.14), RI R2=.49. Chattaraj blames mixture-of-experts parameter counts. [C, K17]
- Hallucination: Wang and Sun describe a third stage of never-seen values; Chattaraj measures 0.2 percent (PI) and 0.9 percent (RI). Different definitions. [c23, c08]
- Unrelated load: cheap in two lexical tests, not cheap with dense retrieval (-0.18) or in NoLiMa (length alone cuts accuracy). [C, K09]
- Dedupe: hurts on clean pools, helps on redundant ones. [S]
- Write rule: mixed (see 6.6). [C, K31]

### 5.4 Interventions that worked

| Intervention | Effect | Status |
|---|---|---|
| Prefilter the library by code (top-1 vector) | Tool choice 13.62 to 43.13 percent; tokens 2133.84 to 1084 | S (one model, 20 trials, a26) |
| Put the gold item nearest the query | 0.3781 vs 0.2348 (far) vs 0.1795 (mid), 18 distractors | E (K15) |
| Mock Q and A turn before query | Gemini Flash 2.0: 150 updates matched baseline at 30 to 45 | S |
| Memory integration prompt, 2-shot | Qwen2.5-7B 18.67 to 25.83; Qwen3-235B 80.67 to 86.17; 2-shot LLaMA3.1-70B 72.17 to 76.50 | S, single-digit to low-teens gains |
| Group by cue, retrieve groups first | F1 43.98 vs 36.48, fewer tokens | S |
| Fan-divided activation | F1 40.5 vs 33.3 | S |
| Entropy gate for second lookup | +1.78 F1, -679 tokens | S |
| Dedupe when top-k is redundant | +13.6 to +24.1 S-Recall | S |
| Repeat the prompt (non-reasoning models) | 47 of 70 combinations better, 0 worse; NameIndex 21.33 to 97.33 percent (Flash-Lite) | S |
| Sculptor active context management (RL-trained 13B) | PI-LLM 22.5 to 71.8 (zero-shot Sculptor-M3) and 99.4 (RL) | S, needs training |
| Update/invalidation systems on LongMemEval knowledge update | Zep 44.4, Cognee 37.8, MemoryOS 35.6 vs long context 20.0 and embedding RAG 20.0 | C, not controlled |

### 5.5 Interventions that did not work

| Intervention | Result |
|---|---|
| "Forget the old values" prompts | Under 10 points at 100 updates; per-key forget worsened gpt-4.1-mini; relevance meta-prompt harmful for gpt-4.1-mini (a25, b13). [E, K06] |
| Chain of thought for retrieval | Equal or worse in 3 of 4 pairs (b13). |
| Restating the task goal | No change in the log-linear trend (c05). |
| Index numbering | Hurt: LLaMA3.1-70B to 38.33 percent, Qwen2.5-72B to 27.00 (c10, not re-verified). |
| Directed forgetting prompt | Qwen2.5-32B +1 point (c10). |
| Zero-shot tool use for context management | Claude-4-Sonnet PI-LLM +5.90, GPT-4.1 +6.58, DeepSeek-V3 -0.12; 4/1K length 99.13 to 90.43 (c13). |
| Model-written bounded memory | gpt-4.1-mini 82 vs 63, gpt-4.1 91 vs 64, gpt-5.4 (low reasoning) 92 vs 77 percent versus full context (d01). Giving 24x more room: 28 percent still (d02). |
| Recency alone | Poison acceptance .02 lexical, .00 dense; persistent-update or authoritative wording raised to .23/.12 and .26/.14 (c26). |
| Always-dedupe | -0.7 to -33.0 S-Recall points on clean pools (d03). |
| Context window size as a cure | No effect on PI endurance (b12). |
| List-strength test in LLMs | Repeating strong items did not hurt weaker ones; list 32 to 40 facts only (b11). |

---

## 6. Language models

### 6.1 Recognition fan (the human paradigm)

GPT-4 (gpt-4-0125-preview), Mistral-7B-Instruct-v0.3, LLaMA-3-8B. Study list of 32 person-location facts. Fan 1 = 32 unique pairs; fan 2 = 16 persons and 16 locations each twice; 64 test items (32 foils); foils rearranged inside the same fan. Accuracy 0.991 (fan 1) to 0.915 (fan 2). d' about 4.1 and 3.1 for GPT-4. Human d' 3.7 and 2.5 are second-hand from Schneider and Anderson. Online GPT-4 beat offline models and beat humans on d'. Recall stayed near perfect; recognition showed the errors. LLMs lacked a serial position curve and were robust to nonsense words. List size 32 to 40 gave a fluctuating drop. No list-strength effect. No significance tests or variance in most results. [a21, a22, b10, b11, c02, c22] This is one independent study; the several entries (a21, a22, b10, b11, c22) are the same paper.

Gap: fan above 2 is not measured for LLM readers.

### 6.2 Fan in token probability (Roberts et al. 2024)

Six families: RoBERTa, GPT-2, Llama-2, Llama-3, Mistral, SOLAR; each expanded to a PopulationLM of 50. Pretraining fan used 10 Rosch categories, and typicality of items. Mistral and SOLAR showed significant negative correlations between typicality and the probability of "absent" for absent items. In-context: Anderson 1974 recreation, 20 persons x 20 places, 16 fan combinations. For Mistral and SOLAR, absent-item correlations with fan were significant (p<=0.01); present-item correlations were not. Person fan gave effects; place fan disrupted or reversed them (SOLAR positive). Noise floors 0.2 to 0.45. Population variance showed no effect. The effect is in probability, not in measured errors; with certainty removed it vanishes. 7B to 10.7B models only. [b08, b09, c01, c21] Implication: the model's uncertainty signal is in logits, not in text.

### 6.3 Overwrite (proactive interference), the strongest LLM evidence

- Wang and Sun: 46 keys, 400 words per category, 3 to 400 updates per key. Accuracy falls log-linearly in every model, 0.6B to 637B parameters. Errors move from adjacent earlier updates (stage 1), to far-upstream (stage 2), to values never shown (stage 3), with a pull to the earliest bin. Sequential (non-shuffled) updates show a step-like cliff at a model-specific threshold; shuffled interleaving gives the smooth line. Reasoning models excluded for latency (over 200 s). Humans plateau at high interference; LLMs keep declining (cited, not run). [a23, a24, b12, c03, c23, c25]
- Three load axes (updates per key, tracked keys, value length) give the same log-linear drop. Experiment A: 125 or 350 updates per key with 1 to 46 keys. Experiment B: input length fixed, tracked keys 1 to 46, near-identical curve. [b14, c04]
- Chattaraj and Raj: 39 LLMs from 1B to 2.5T parameters; PI vs RI Cohen d=1.73; 39 of 39 models RIES>PIES. Mean accuracy at N=3 is 93.9 percent. RI near ceiling to N=50 (96.0 percent) then 25 percent at N=300; PI falls from 94 to 3 percent. RI vs PI correlation r=0.21 (CI -0.11 to 0.49). RI errors are mostly "nothing returned" (50.8 percent retrieval failure); PI errors are same-key intrusions (56.1 percent). o1: RIES 186.4 (rank 1) but PIES 22.0 (rank 35). Reasoning models RIES 178.0 vs 150.3 for others. Under high PI accuracy flips bimodally between near-ceiling and near-floor across runs. [c08, c24]
- Qiao et al. (DKI, AB-AC paradigm, cites Watkins and Watkins): 13 LLMs, synthetic T=32 to 512 (200 instances) and 164 real-world DKIs (mean length 8.77). Earliest accuracy 98 to 100 percent. Gap above 0.6 for small and mid models; LLaMA3.1-405B, GPT5-N, Gemini2.5-F smaller. Internal attention and logit signals become flat on errors. Gap still about 91 percent for LLaMA3.1-8B after interventions. [c09, c10]
- Quantization: INT4 raises same-key intrusion errors from 21.5 to 24.6 percent of trials (p=4.8e-7); normalised IES loss 1.8 (Qwen), 5.1 (Mistral), 5.2 (Phi). The effect vanishes or reverses for numeric attributes. [c11]
- A toy 793K-parameter transformer with learned forgetting and merging (SleepGate) got 99.5 percent at PI depth 5 and 97.0 at 10 against under 18 percent for five cache baselines; it failed when many near-identical entries shared an entity (stale retrieval 23.5 to 62.0 percent at n=15 to 30). Proof of concept only. [c12]

### 6.4 Retrieval distractors

- Cuconasu et al. (SIGIR 2024): NQ-open, Llama2-7b, Phi-2, MPT, Falcon. Gold only 0.5642. Hard distractors cost up to -0.38 (-67 percent); a single distractor up to -0.24 (-25 percent). Attention goes to the distractor. Random passages beside the gold did not hurt; the best random setting was about +0.02 (0.5859 at 14, significant), 6 random +0.0039 not significant. MPT rose with 8 far distractors (0.2148 to 0.3039). Models are small and 2023-era. [b15, b16, c07; the "+0.08 (+36 percent) for one model" was not re-verified]
- Liu et al. (Lost in the Middle): closed-book GPT-3.5-Turbo 56.1, Claude-1.3 48.3, MPT-30B 31.5, LongChat-13B 35.0; oracle 88.3, 76.1, 81.9, 83.4. 20 docs GPT-3.5: 75.8 at index 0, 53.8 at index 9, 63.2 at index 19. [b17]
- Jin et al.: with a strong retriever, quality rises then falls; hard negatives hurt more than random; Gemini-1.5-Pro resists random but not hard negatives; reordering helps. [d12]
- Leng et al.: 20 models, 2k to 128k tokens. Steady gains to about 100k for o1-preview, o1-mini, GPT-4o, GPT-4o mini, Claude 3.5 Sonnet, Claude 3 Opus, Gemini 1.5 Pro. Llama 3.1 405B drops after 32k, GPT-4-0125 after 64k, Qwen 2 70B holds to 64k; most open models effective only to 16k to 32k. [d13]
- RAGGED: k swept to 50 on NQ, HotpotQA, BioASQ; reader-specific; rerankers and prompts do not change the pattern. [d11]
- NoLiMa: 13 models, 58 question-needle pairs, 5 haystacks, 26 placements, 7,540 tests per length. Effective length = longest length above 85 percent of base. GPT-4o 99.3 to 69.7 at 32K; 11 of 13 below 50 percent of base. With a literal-overlap distractor GPT-4o effective length falls to 1K (base 93.8 and 84.4 for GPT-4o and Llama 3.3 70B). The ">50% at 128K" for GPT-4o and Gemini 2.0 Flash 16.4 percent at 128K are from c17. [b18, c17]
- Chroma Context Rot: 18 models; needle-question similarity 0.445 to 0.775 (essays), 0.521 to 0.829 (arXiv); distractors at 0, 1, 4; LongMemEval full prompts about 113k tokens vs focused about 300 tokens (306 prompts); shuffled haystacks did better than coherent ones. Vendor report; per-model values in charts only. [d15]
- Gao et al. (First Drop of Ink): the first 10 percent of hard distractors caused 58 percent of total loss (Qwen2.5-7B, nq easy, 128K). Attention on the gold passage fell 76 percent (97 to 21 percent in the paper's example) when 10 percent of 100 distractors were hard. Filtering helps mostly by shortening the context. [d14]
- OpenAI MRCR: 2, 4 or 8 identical requests ("poem about tapirs") hidden in a long chat; the model returns the i-th one. 438 entities, 10 writing formats, 100 samples per token bin from 4,096 to 1,048,576 tokens. The dataset card gives no per-needle accuracy. Aggregator numbers (not lab reports): 8-needle Gemini 3.6 Flash 54, Gemini 3.5 Flash 26.6, Gemini 3.1 Pro 26.3 percent; 2-needle at 128K from 36.6 (GPT-4.1 nano) to 95.2 (GPT-5 high) (d19, not opened). [d17, d18, d19, d20]

### 6.5 Agent memory systems

- Ding et al. (CMI): TravelPlanner build, load levels L0 to L6 = 3, 6, 12, 24, 48, 90, 135 memories. Noise-only plasticity 0.510 to 0.455 (non-monotonic). Lexical: unrelated -0.02, repeated history -0.32, same-slot -0.48 at count 8. Dense (Qwen3-Embedding-8B): unrelated -0.18, repeated -0.46, same-slot -0.44. The critique warns: the "stability 0.92 to 0.54" figure is unverified; 0.54 is dense same-slot Target Recall@3. Lexical same-slot Target Recall@3 0.34; dense repeated history recall 0.48. [c14]
- MINTEval: 15.6K questions, contexts averaging 138.8K tokens (up to 1.8M), about 86 updates deep. Average accuracy 27.7 percent in text (27.9 in abstract) with Qwen3.6-35B-A3B; best system 33.4; most-recent questions 47.5; MemAgent 85.7 on bAbI Simple but 7.5 on HorizonBench; evidence present in 58.3 percent, answering adds a 25.2 percent drop; inserts 76.8 percent of operations. [c15]
- Supersede: LongMemEval knowledge-update oracle split, n=78, LLM judge. Full context vs 300-character bounded memory: gpt-4.1-mini 82 vs 63 (McNemar p=0.0035; 19 vs 4 discordant), gpt-4.1 91 vs 64, gpt-5.4 low reasoning 92 vs 77 (p=0.0033; 13 vs 1). Scale (gpt-4.1-mini, n=25): 2 sessions at 300 characters 68 percent; 48 sessions (122k tokens) 28 percent (p=0.002); 48 sessions at 7,150 characters still 28 percent. GRPO on Qwen2.5-3B 9.0 to 16.7 percent (single run). [d01, d02]
- Systems with update or invalidation: see 5.4 (d10). Systems differ in many ways, tokens are not matched.
- Mem0 vendor note: moved to add-only, +42.1 on temporal reasoning at under 7,000 tokens per retrieval; an independent study found its own update path scored 24.7 points lower; insertions 87.6 percent of operations in one system. Search snippet only. [d24]
- Causal selection (CAUSAL-LOCOMO): task score 0.846 vs 0.845 and 0.839 for the best baselines; bad-memory rejection 0.990; useful-memory F1 0.875. The task-score gap is tiny; the gain is in rejecting poisoned memories. [c18]

### 6.6 What changed the results, by how much

| Change | Effect size | Notes |
|---|---|---|
| More updates per key 3 to 400 | Accuracy toward zero, log-linear | all models |
| Ask for latest vs earliest | 69.5-point mean gap | d=1.73 |
| Model size | PI: disputed; RI: R2 .49 | K17 |
| Reasoning mode | RIES 178.0 vs 150.3; PI not clearly better | o1 rank 35 of 39 on PI |
| Prompt to forget | under 10 points | E |
| Mock Q and A turn | 150 updates matched 30 to 45 | S |
| 4-bit quantization | -6 to -13 points on semantic overwrites | S |
| Hard distractor count | -0.09 (1) to -0.25 (8) absolute, Llama2 | E |
| Gold position | 0.378 vs 0.180 | E |
| Prompt repetition | up to +76 points on one custom task | S, non-reasoning only |
| Group cap 12 vs 8 | +2.8 F1 | S, no CI |

---

## 7. What our agent should take

Schema parts: G (guardrails), S (states), O (operators), memory (section 5 of SCHEMA.md). Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Do not rely on prompts to forget or ignore old notes. Remove superseded or conflicting notes in code before the model sees them.** Part: G2/G5 and memory. [E] K06 (a25, b13, c05, c10). The "forget" instruction moved results under 10 points; directed forgetting +1 point. Candidate for SCHEMA section 4b: "Telling the model to forget, ignore or focus on later notes".
2. **Treat the count of competing notes under one cue, especially near-miss ones, as the main retrieval risk, not total library size.** Part: memory. [E] K04, K08, K16, K18 (a23, b12, c08, c09, b15, c14, c17). Log it per cue.
3. **Count false accepts, not just misses.** Part: G3 and S8. [E] K10, K11 (a19, a13, a05, b06). Check the chosen note against the whole claim, not one shared key.
4. **Order candidate notes so the best is nearest the query; never leave the best one in the middle.** Part: S3/G5. [E] K15 (b17, b16, c20, d12).
5. **Do not fix k. Tune the number of notes shown per reader on the deployed model.** Part: memory/G5. [E] K27 (d11, d12, d13). The result says "tune", not "use N". All data are 2023 to 2024 models.
6. **Do not use the model's "I am not sure" as a trigger.** Part: G10/G2. [E] K22 (b08, c01, c24, d15). 8.6 percent refusals in PI failures; 0.035 percent of 194,480 calls.
7. **Expect the latest value after many writes to be the weak one, and the first value to be strong.** Part: memory. [E] K16 (c08, c09). So an append-only lesson library will fail at "current value" questions even while "first value" questions pass.

### Test first (single-source or contested)

| Item | Part | Status | Evidence ids |
|---|---|---|---|
| Code-side replace (one live value per cue) vs append-only | memory/G7 | [C] K31 | d01, d02, d09, d10, d24 |
| Group notes under sub-cues; cap group size near 4 to 12 | memory | [S] K29 | d05, d06 |
| Integrated case note vs N loose notes | memory | [C] K13 | a09, a16, b20, b26 |
| Prefilter by code, sweep k | memory/G5 | [S] K19 | a26, d11 |
| Cue weighting (emphasise one cue) | memory | [C] K14 | a15, b01 |
| Fan-divided scoring in lookup | memory | [S] K21 | c16 |
| Turn boundary before the query | S5/memory | [S] K07 | b13 |
| Dedupe only when redundant | memory/G3/G5 | [S] K28 | d03, d04 |
| Entropy gate for second lookup | G10/S8 | [S] K32 | d07, d08 |
| Canonical cue key + one normalising call | memory/G7 | [S] K30 | d09 |
| Log shape (log vs power) of cost per cue | memory | [S] K02 | a27, b06, d14 |
| Re-exposing the key note next to the query | memory | [S] K34 | d21 |
| Use-count boost (strength by success) | memory | [S] K12 | a06, a07 |
| Fold/forget tool for long runs only | S5/G7 | [S] K20 | c13, d01 |
| Swap-in/out selection by effect on the answer | G3/G5 | [S] K25 | c18 |
| Measure PI slope on the deployed model, reasoning on and off, quantized or not | memory | [S] K33, K23, [C] K17 | c08, c03, c11 |

Cost check (G7): every row here must win at equal tokens with setup cost counted. Several (Sculptor, FORGETEVAL's LLM hook, SleepGate) have not been tested at equal tokens.

---

## 8. Concrete tests on our bench

All tests: both arms at equal total prompt tokens (pad the small-library arm with unrelated filler notes of the same length), model fixed, 3 seeds, items drawn from the lesson/class-record style library the agent will really keep. Report accuracy and false accepts separately (K10). Bench types: synthetic lesson-lookup items on our own problem classes, and ARC or BRAINTEASER lessons retrieved by class.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Fan curve | Query by cue for the lesson on that cue; N = 1, 2, 4, 8, 16, 32 near-related notes per cue | One arm per N, padded to equal tokens | Accuracy; false accepts; slope per doubling; fit log vs power | Accuracy falls with N; first doubling costs the most (log). If slope per doubling is under 3 points the deployed model is robust at this range. |
| T2 Overwrite | Same cue overwritten k = 1, 3, 10, 30, 100 times; ask for latest | Append-only; code-replace; "ignore old" prompt | Latest-value accuracy | Code-replace flat; append-only falls log-linearly; prompt arm close to append-only (K04, K06). |
| T3 Near-miss vs unrelated | Add 4 near-duplicates vs 4 unrelated notes to the candidate set | Near, unrelated, none | Accuracy; false accepts | Near hurts, unrelated costs little (K08); check dense vs lexical lookup (K09). |
| T4 Top-k sweep | k = 1, 3, 5, 10, 20 over the real library, near-duplicates left in | One arm per k | Accuracy at each k; spread near peak | Inverted U, peak reader-specific (K27). |
| T5 Position | Candidate list ordered best-last, best-first, random | 3 orderings | Accuracy | Best nearest the query wins by several points; middle worst (K15). |
| T6 Grouping | Same notes flat; grouped under sub-cues (cap 4, 8, 12); one integrated case note | 4 layouts | Accuracy; false accepts; tokens | Grouping helps at N >= 8 (K29); integrated note may remove fan on the shared cue (K13). |
| T7 Full-match verify | Foils that share a cue with a stored note | Cue-only accept vs full-claim compare | False-accept rate | Full compare lowers false accepts (K11). |
| T8 Dedupe | Library with 0, 10, 30 percent near-duplicate pairs; single-note and multi-note questions | Plain top-k; always-dedupe; dedupe-when-redundant | Accuracy | Rule wins at high redundancy; always-dedupe loses on clean pools (K28). |
| T9 Turn boundary | Stale-value query after 30 and 100 updates | With vs without a mock Q and A turn | Latest-value accuracy | Gain, but still falls with update count (K07). |
| T10 Entropy gate | Cues with N = 1 to 16 notes; needs logprobs | Single lookup; second lookup when entropy over threshold | ROC-AUC of entropy vs correctness; accuracy at equal tokens | AUC above 0.7 and a gain (K32). |
| T11 Canonical key | Notes written with variant cue spellings | Raw text cue; code canonical key; canonical key plus one normalising call | Latest-value accuracy; setup tokens | Canonical key wins when cues vary; count setup (G7) (K30). |
| T12 Re-exposure | N = 8 competitors | Chosen note once vs twice next to the query | Accuracy | Small gain on non-reasoning models (K34). |
| T13 Use-count | Library with notes used before (some 5 times, some 0) | Equal weight vs use-count boost | Accuracy on older, often-used notes | Boost helps if past use predicts relevance (K12). Could also add noise. |
| T14 Model sensitivity | T2 on reasoning off/on and full vs quantized | 4 arms | Slope per doubling | Reasoning helps little on PI; quantization adds a few points of loss (K33, K23). |

---

## 9. What does not transfer, and why

- **Reaction time.** The human fan effect is mostly latency. An LLM has no retrieval latency. Only accuracy and token probability can be measured. Cost in tokens is a different quantity.
- **Memory decay, practice over days, sleep.** The 600-presentation result needs repeated exposure over 25 days. An LLM agent re-reads the same note unchanged; there is no strengthening unless code adds it (K12, K34).
- **Humans plateau; LLMs keep falling.** Wang and Sun cite human data that plateau at high interference. LLMs fall toward zero. The human PI literature comes from other tasks, so this is not like-for-like (critique).
- **The human PI/RI pattern is reversed.** In LLMs the first value is easy and the latest is hard (d=1.73). Do not import human advice about proactive interference directly.
- **ACT-R's source-activation account.** LLMs have no fixed source activation. The analogy (the context as a shared budget) is untested. Also later ACT-R dropped multi-link spread (a04 note).
- **Foil waiting.** The "wait and give up" mechanism has no LLM counterpart; a model answers in one pass and rarely refuses.
- **Integration.** The human benefit depends on situation models. Whether an LLM benefits from an integrated case note is not tested; even in people it is contested.
- **Tiny fans.** The LLM fan test is fan 1 vs 2 on 32 facts. A library has dozens of notes per cue.
- **Synthetic tasks.** Random words and key-value updates (PI-LLM, Chattaraj) have no meaning and no prior knowledge. Real notes carry meaning that may help or hurt.
- **Retrievers are not readers.** Guo et al. test DPR, ColBERTv2, HippoRAG, not LLM readers. Their log fan applies to the retrieval stage.
- **Old models.** Cuconasu (Llama2-7b, Phi-2, MPT, Falcon), Liu (2023), RAGGED (2023-24), Jin (2024). Modern frontier models may differ.
- **Distractor share vs count.** Gao and Leng vary share or total length, not the number of items under one cue.
- **Vendor and aggregator numbers.** Chroma, benchmarklist.com, Mem0 blog: direction only.

---

## 10. Open questions

1. What is the fan slope of a current frontier model in natural text, for 1 to 50 notes per cue, with a compact in-context library? (GAP 1; data stop at fan 2.)
2. Does a code-side supersede rule beat append-only at equal tokens in a real agent loop, setup cost counted? (K31, GAP 2.)
3. Does grouping or integrated case notes reduce fan cost in LLMs? Does the single-location boundary appear? (K13, K29.)
4. How steep is the loss when top-k goes from 1 to 20 on modern models, near-duplicates in vs out? (GAP 4.)
5. Does emphasising one cue help or hurt (differential fan)? No LLM test. (K14.)
6. Does repeated successful use make a note safe from crowding, or only add noise? (K12, K34.)
7. Can answer entropy trigger a second lookup on crowded cues? (K32.)
8. Do size, reasoning mode and quantization change the PI slope on our model? (K17, K23, K33.)
9. What are the original cells for Watkins and Watkins 1975 and Anderson 1974? (GAP 9; blocked by paywall and a Cloudflare check.)
10. Is the Guo et al. log-fan result reproducible? An independent human or reader replication at fan 1 to 16 is needed. (K02, GAP 10.)
11. Does the log form hold for LLM readers, or is it a retriever property?
12. Is the 8-needle MRCR drop (26 to 54 percent) a cue-overload effect or an ordering effect? A same-model 2/4/8 sweep would settle it.
13. Why do random near-query passages help some models (Llama2) and not others (Falcon)?

---

## 11. Sources

[V] = opened and read this session (some only at abstract or report level, noted). [M] = snippet or aggregator only.

Human work
- [M] Watkins and Watkins (1975) Buildup of proactive inhibition as a cue-overload effect. https://doi.org/10.1037/0278-7393.1.4.442 (a01, c27, d23)
- [M] Anderson (1974) Retrieval of propositional information from long-term memory. https://doi.org/10.1016/0010-0285(74)90021-8 (a02, b22, d22)
- [V] Anderson (1983) Retrieval of information from long-term memory, Science 220:25-30. https://app.nova.edu/toolbox/instructionalproducts/edd8124/articles/1983-Anderson-Retrieval.pdf (a03 to a09)
- [V] Schneider and Anderson (2012) Modeling fan effects on the time course of associative recognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC3259266 (a10 to a13)
- [V] Anderson, Reder and Lebiere (1996) Working memory: activation limitations on retrieval. https://www.andrew.cmu.edu/user/reder/publications/96_jra_lmr_cl.pdf (a14)
- [V] Sohn, Anderson, Reder and Goode (2004) Differential fan effect and attentional focus. https://www.andrew.cmu.edu/user/reder/publications/SARG-PBR-04.pdf and https://www.cmu.edu/dietrich/psychology/memorylab/publications/SARG-PBR-04.pdf (a15, b01 to b03)
- [V] Radvansky and Zacks (2005) Age and inhibition (data from Radvansky, Zacks and Hasher 1996). https://pmc.ncbi.nlm.nih.gov/articles/PMC1751467 (a16)
- [M] Anderson and Reder (1999) The fan effect: new results and new theories. https://www.andrew.cmu.edu/user/reder/publications/99_jra_lmr_2.html and https://doi.org/10.1037/0096-3445.128.2.186 (a17, b23; image scan, not read)
- [V] Tehan and Humphreys (1996) Cuing effects in short-term recall. https://link.springer.com/article/10.3758/BF03201097 (a18; abstract page only)
- [V] Verde (2004) Associative interference in recognition memory. https://link.springer.com/article/10.3758/BF03206318 (a19; abstract page only)
- [V] Wikipedia, Fan effect. https://en.wikipedia.org/wiki/Fan_effect (a20, b21)
- [V] Link, van Maanen and Dotlacil (2025) Similarity comes at a cost. https://research-portal.uu.nl/en/publications/similarity-comes-at-a-cost-novel-evidence-for-associative-memory-/ (b19; poster abstract only)
- [V] Reder lab fan effect overview. https://www.cmu.edu/dietrich/psychology/memorylab/fan.html (b20)
- [M] Cantor and Engle (1993). https://doi.org/10.1037/0278-7393.19.5.1101 (b24)
- [M] Bunting, Conway and Heitz (2004). https://doi.org/10.1016/j.jml.2004.08.001 (b25)
- [M] Radvansky and Zacks (1991); Radvansky (1999), incl. Chinese replication. https://pubmed.ncbi.nlm.nih.gov/8423436 (b26)
- [M] Reder, The size of the fan effect: process not representation. https://kilthub.cmu.edu/articles/journal_contribution/The_Size_of_The_Fan_Effect_Process_not_Representation/6618788/1 (b27; 403)
- [M] Schneider and Anderson d' values as cited in arXiv 2509.17138 (b28)

LLM and agent work
- [V] Cao, Schooler and Zafarani (2025) Analyzing memory effects in LLMs through the lens of cognitive psychology (listed as "Huang et al." in c02, c22 in error). https://arxiv.org/abs/2509.17138 (a21, a22, b10, b11, c02, c22)
- [V] Roberts, Moore, Pham, Ewaleifoh and Fisher (2024) LLM recall uncertainty is modulated by the fan effect. https://arxiv.org/abs/2407.06349 (b08, b09, c01, c21)
- [V] Wang and Sun (2025) Unable to forget: proactive interference. https://arxiv.org/abs/2506.08184 (a23 to a25, b12 to b14, c03 to c05, c23, c25)
- [V] Chattaraj and Raj (2026) LLMs remember first, forget last. https://arxiv.org/abs/2603.00270 (c08, c24)
- [V] Qiao et al. (2026) Diagnosing retrieval bias under multiple in-context knowledge updates (DKI). https://arxiv.org/abs/2603.12271 (c09, c10)
- [V] Shahrabi-Farahani and Rahmati (2026) Compress and Forget. https://arxiv.org/abs/2608.18578 (c11)
- [V] Xie (2026) SleepGate. https://arxiv.org/abs/2603.14517 (c12)
- [V] Li et al. (2025) Sculptor. https://arxiv.org/abs/2508.04664 (c13)
- [V] Ding et al. (2026) Controlled memory interference (CMI). https://arxiv.org/abs/2608.07622 (c14, c26)
- [V] Lee et al. (2026) MINTEval. https://arxiv.org/abs/2605.18565 (c15)
- [V] Jiang et al. (2026) SYNAPSE. https://arxiv.org/abs/2601.02744 (c16)
- [V] Sahai Srivastava (2026) Causal intervention-based memory selection. https://arxiv.org/abs/2605.17641 (c18)
- [V] Guo, Wu and Yiu (2026) The interference gap (arXiv id/date mismatch). https://arxiv.org/abs/2606.28327 (a27, a28, b04 to b07, c06, c28)
- [V] Gan and Sun (2025) RAG-MCP. https://arxiv.org/html/2505.03275v1 (a26)
- [V] Cuconasu et al. (2024) The power of noise. https://arxiv.org/abs/2401.14887 (b15, b16, c07, c20)
- [V] Liu et al. (2024) Lost in the middle. https://arxiv.org/abs/2307.03172 (b17); [M] secondary report in c19
- [V] Modarressi et al. (2025) NoLiMa. https://arxiv.org/abs/2502.05167 (b18, c17)
- [V] Patel (2026) Supersede. https://arxiv.org/abs/2606.27472 (d01, d02)
- [V] Brouillette et al. (2026) Finding the right balance. https://arxiv.org/abs/2610.09412 (d03, d04)
- [V] Hu et al. (2026) xMemory. https://arxiv.org/abs/2602.02007 (d05 to d07)
- [V] Moskvoretskii et al. (2025) Adaptive retrieval without self-knowledge? https://arxiv.org/abs/2501.12835 (d08)
- [V] Yang (2026) FORGETEVAL control-plane placement. https://arxiv.org/abs/2606.15903 (d09)
- [V] Zhou et al. (2026) Are we ready for an agent-native memory system? https://arxiv.org/abs/2606.24775 (d10)
- [V] Hsia et al. (2025) RAGGED. https://arxiv.org/abs/2403.09040 (d11)
- [V] Jin et al. (2024) Long-context LLMs meet RAG. https://arxiv.org/abs/2410.05983 (d12)
- [V] Leng et al. (2024) Long context RAG performance. https://arxiv.org/abs/2411.03538 (d13)
- [V] Gao et al. (2026) The first drop of ink. https://arxiv.org/abs/2605.10828 (d14)
- [V] Chroma Research (2025) Context rot. https://www.trychroma.com/research/context-rot (d15; report level, no per-model tables)
- [V] Du et al. (2025) Context length alone hurts. https://arxiv.org/abs/2510.05381 (d16; abstract page only)
- [V] OpenAI MRCR dataset card. https://huggingface.co/datasets/openai/mrcr (d17)
- [V] benchmarklist.com MRCR v2 8-needle page (aggregator). https://benchmarklist.com/benchmarks/mrcr_v2_8_needle/ (d18)
- [M] benchmarklist.com OpenAI MRCR 2-needle pages. https://benchmarklist.com/benchmarks/openai_mrcr_2_needle_128k/ (d19)
- [V] Vodrahalli et al. (2024) Michelangelo. https://arxiv.org/abs/2409.12640 (d20)
- [V] Leviathan, Kalman and Matias (2025) Prompt repetition improves non-reasoning LLMs. https://arxiv.org/abs/2512.14982 (d21)
- [M] Mem0 team blog (2026). https://mem0.ai/blog/mem0-the-token-efficient-memory-algorithm (d24)

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 12 established claims: 6 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A06.04-K01** (reworded: the sources support less). Schneider and Anderson (2012) intro does state fan effects across fictional and real knowledge and that accuracy costs show as higher false-alarm rates with mixed hit-rate effects (secondhand, citing others), but the Dutch poster (Link et al., AMLaP 2025, not a full paper) found RT slowing in both experiments and lower accuracy only in Experiment 1 (repeated concepts); with semantically similar concepts accuracy was at ceiling, so 'lowers accuracy' is not shown there. Corrected claim: More facts attached to one cue slows recognition in people, and usually lowers accuracy mainly through extra false alarms (hit-rate effects are mixed). This holds for fictional facts and real-world knowledge; in a Dutch conference poster with semantically similar concepts RT rose with fan in both experiments but accuracy fell only in the repeated-concept experiment (similar-concept accuracy near ceiling).
- **A06.04-K03** (reworded: the sources support less). Cao et al. numbers verified (0.991 to 0.915 at list size 32; GPT-4 d' about 4.1 to 3.1) but the paper does not call the effect small (d' drop about 1.0, versus about 1.2 in humans); and Roberts et al. found no fan effect for GPT-2/Llama-2/RoBERTa only in the pretraining-fan experiment, while the in-context experiment tested only Mistral and SOLAR, so 'when all facts are in context ... not GPT-2, Llama-2' is not supported. Corrected claim: With all facts in context, GPT-4 shows a fan effect on person-location recognition (accuracy 0.991 to 0.915 at list size 32; d-prime about 4.1 to 3.1, versus about 3.7 to 2.5 in humans), with offline Mistral-7B and LLaMA-3-8B showing the same direction. In token probabilities, Roberts et al. found human-like fan effects for Mistral and SOLAR but not RoBERTa, GPT-2 or Llama-2 (pretraining fan; Llama-3 weak and non-significant); their in-context fan test covered only Mistral and SOLAR.
- **A06.04-K04** (reworded: the sources support less). Wang and Sun's abstract says accuracy declines log-linearly toward zero (3 to 400 updates, models from 0.6B to 637B across Google, OpenAI, Anthropic, xAI, DeepSeek, Qwen, Meta, Nvidia) but the figure caption says only 'most models' showed a quasi-log-linear drop, with exceptions and two-phase declines, and Chattaraj and Raj (39 models) describe proactive interference as collapsing bimodally at high interference and do not state a log-linear fit; the '35 to 39 models' merges two separate studies built on the same task design. Corrected claim: In Wang and Sun's PI-LLM task (46 keys, 3 to 400 updates per key, about 35 models from 0.6B to 637B parameters across many labs), accuracy at reading the latest value of a key falls approximately log-linearly toward zero for most models, with some exceptions and two-phase declines. A follow-up with 39 models (Chattaraj and Raj) confirms that proactive interference is severe in every model, but describes its collapse as bimodal at high interference rather than log-linear.
- **A06.04-K08** (number corrected). In Cuconasu Table 1 (hard ADORE-type/related distractors) Llama2 gold-only 0.5642 falls to 0.4586 (1 far) and 0.2643 (8 far); the quoted 0.4733 and 0.3106 are Table 2 (random unrelated documents, far), so they do not show near-miss damage. NoLiMa literal-overlap distractor GPT-4o effective length 1K confirmed; CMI not opened. Corrected claim: Near-miss competitors under the same cue hurt most. Hard distractors cut Llama2 accuracy from 0.5642 to 0.4586 (1 distractor, far) and 0.2643 (8 distractors, far) in Cuconasu et al., while random unrelated documents placed far from the query also cut it (0.4733 at 1, 0.3106 at 8) but placed near the query helped; same-slot conflicts cut agent memory uptake more than unrelated memories; a literal-overlap distractor cut GPT-4o effective length to 1K.
- **A06.04-K10** (reworded: the sources support less). Numbers check out (Guo et al.: false alarms 23.1% human vs 41.3% DPR at cos>0.7; Link et al. fan in Dutch with RT effect in both experiments; Verde: interference always raised false alarms), but no source compares similarity against count, so "matters as much as count" is not supported; the Guo figures come from one preprint and Link et al. is a conference poster. Corrected claim: Competitor similarity matters as well as count. In one preprint (Guo et al. 2026), false alarms at high competitor similarity were 23.1 percent for humans and 41.3 percent for dense passage retrieval, against 8.2 and 12.4 percent at low similarity; similar concepts still show a fan effect in Dutch (reaction time in both experiments, accuracy in one; Link et al. poster); interference raises familiarity so false alarms rise even when hits do not (Verde 2004).
- **A06.04-K22** (reworded: the sources support less). Roberts et al. found a fan effect in absent-item probabilities only for Mistral and SOLAR (RoBERTa, GPT-2, Llama-2 none, Llama-3 weak), so it is not a general LLM finding; 8.6% vs 0% refusals confirmed in Chattaraj and Raj. Corrected claim: Model uncertainty about cue overload rarely appears in output: in two of six model families tested (Mistral and SOLAR) fan shows in token probabilities when the queried item is absent, and only 8.6 percent of proactive-interference failures contain an explicit refusal (0 percent under retroactive interference). Errors are mostly same-key intrusions of stale values (56.1 percent).
