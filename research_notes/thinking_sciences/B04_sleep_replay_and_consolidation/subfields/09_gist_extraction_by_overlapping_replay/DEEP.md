# Gist extraction by overlapping replay: deep document

*Subfield B04.09. Sources: evidence_a-d.jsonl (ids a01-a26, b01-b25, c01-c29, d01-d21), claims.jsonl (K01-K35, written as B04.09-Kxx), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The idea. During sleep the brain replays recent memories. If several memories share a part, that part gets replayed again and again, so it grows stronger. The parts that are unique to one memory get replayed once and fade. What is left is the shared structure: the gist, or schema. Lewis and Durrant (2011) call this "information overlap to abstract" (iOtA).

Why we care. Our agent solves many cases that share rule fragments. A subgoal library that merges overlapping rules is the machine version of this idea. The question is whether "merge by overlap" is a sound design, and how to do it safely.

The honest summary, in five lines:
- The theory is a proposal. No one has directly tested overlap-weighted replay in humans (K01, contested).
- Human sleep evidence is mixed. Many null results. The founding SWS result was not reproduced in a larger sample (K02, K05, K34).
- The LLM and program-synthesis side works well for library learning in general: DreamCoder, LILO, ReGAL, AWM (K11, established).
- No LLM study has tested the core human claim: merging overlapping items versus merging random items (K20).
- The design lessons from LLM work (gate merges, name rules, keep raw cases, merge offline) are better supported than the biology.

Rule for reading this document: treat the sleep literature as design inspiration, not as proof that merging works. Cite the LLM tests for that.

## 2. History and theories in depth

**Complementary learning systems (McClelland, McNaughton, O'Reilly 1995; a15, c28, abstract only).** Cortical networks find structure only when learning is slow and interleaved over many items. Learning a new item alone overwrites old knowledge (catastrophic interference). The hippocampus learns fast and replays to the cortex, interleaving new with old. Prediction: gist needs interleaved replay, not massed new learning. Updated by Kumaran, Hassabis and McClelland 2016 (a16): replay can be goal-weighted, and cortex can learn fast when the new item fits known structure.

**Schapiro et al. 2017 (a17, model, opened).** Hippocampal subfields do two jobs. The monosynaptic route (EC to CA1) learns regularities. The trisynaptic route (EC-DG-CA3-CA1) learns single episodes. Rapid regularity learning here needs no sleep. This is a wake model, so it competes with the sleep story.

**Transformation hypothesis (Winocur and Moscovitch 2011; a25, abstract only).** Episodic memories turn into gist-like cortical memories. Detail still needs the hippocampus. Gist does not.

**Schema and consolidation (Tse et al. 2007, a14; abstract only).** In rats, once a schema had formed, a new association learned in one trial became hippocampus-independent very fast. A schema speeds consolidation of fitting items.

**iOtA (Lewis and Durrant 2011; a01, b11, c26).** Related memories are replayed in overlapping combinations in slow-wave sleep (SWS). Hebbian strengthening grows the overlap. General downscaling then removes the non-shared detail. Repeated replay in new combinations builds schemas. The same mechanism is said to explain insight and false memory. A theory paper with no new data. Cited 357 times; that shows influence, not support (critique).

**BiOtA (Lewis, Knoblich and Poe 2018; a02, a03, a26, opened).** Two stages.
- Non-REM: the hippocampus biases the cortex to replay linked memories together. Overlap is potentiated. Gist forms in a first cortical layer. Non-REM replay runs 6 to 20 times faster than real time.
- REM: hippocampus and cortex decouple. Random input activates unrelated cortical schemas together, so structure shared between whole schemas (atom and solar system) can be found. Output goes to a deeper, more compressed layer.
- Order: non-REM first, REM second, then reconcile in the next non-REM.
- Replay facts they use: a 20 s rat track run replays in about 200 ms; replay occurs tens to hundreds of times a night, more for salient or recent items.
- The network is hypothetical, not run. The REM role is the least supported part.

**Computational descendants.**
- Wake-sleep program learning: DreamCoder (Ellis et al. 2020; a21, b14, b15, c11). Abstraction phase = SWS analogue, dreaming phase = REM analogue. The authors call the biology link speculative.
- Sleep-like replay in neural nets: Tadros et al. 2022 (a20), Sorrenti et al. 2023 (c24), van de Ven et al. 2020 (a19, c25).
- LLM agent memory that names sleep as its model: LightMem (c08), Sleep-time compute (a23), Auto-Dreamer (d04).

**Competing accounts for "why gist appears".**
- Time, not sleep: Sweegers and Talamini 2014 (a12) found generalisation rose over 4 h with no sleep versus wake difference. Durrant 2011 also reported a time-based component (a05).
- Wake hippocampal learning (Schapiro, a17).
- Slow, multi-night abstraction (Lutz 2017; a11, b10, b23).
- Separation as well as merging: Matorina and Poppenk suggest REM discretises memories (b03).

## 3. Core findings with exact numbers

Status uses the claim status in claims.jsonl. "Human" rows are inspiration only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Sleep roughly doubles hidden-rule discovery in the number reduction task (young adults) | "more than twice as many" gained insight after 8 h sleep; N=106 in review table; exact percentages not read; absent without initial training; absent in older adults (Debarnot 2017, N=74) | Wagner 2004 (a04, abstract), Lerner and Gluck 2019 (a09, a24) | K03 established |
| SWS predicted statistical-learning gain | N=36, overnight; nap of 4 h beat 4 h wake; SWS correlate; also a time-based component | Durrant 2011 (a05, b12; abstract/secondary) | K02 contested |
| Larger sample did not reproduce SWS prediction; REM predicted worse statistical learning | N=69 (preprint). SWS predicted no gist type; SWS vs summary gist b=1.625, t(56)=1.980, p=.053; NREM vs stat. learning b=.445, p=.041 (fails FDR .013); REM vs stat. learning b=-0.626, t(58)=-2.662, p=.010 (survives FDR) | Matorina and Poppenk 2019 (b01-b04) | K02 contested |
| Only fully connected relational structure survived a week | Category gist -22%, instance memory -15%, detail -6%; F(2,182)=38.72, p<.001; inferential gist +0.6% while premise pairs -2%; authors: overlap "an insufficient condition" | Matorina and Poppenk (b01, b04) | K07 single-source |
| Far transitive inference gains after sleep | B>E: 93% sleep vs 69-70% wake, t(29)=2.21, p=.03; n=14 vs 17; one-degree B>D 73-75% in both, t(29)=0.18; sleep-by-degree F(1,27)=7.3, p=.01; averaged 79% vs 72%, p=.51 | Ellenbogen 2007 (b05, full text) | K07 single-source |
| Sleep effect on hidden-rule extraction depends on task | Explicit detection: 14 of 30 studies found an effect; all 9 stationary-rule explicit tests null; temporal 31/45 vs stationary 15/22 once implicit effects counted (advantage disappears); ASRT no effect in 4 studies; Weather Prediction 3 of 5 | Lerner and Gluck 2019 (a09, b06, b07) | K04 single-source (vote count, no pooled effect) |
| Stage carrying the effect flips | Lau 2010 N=31: SWS correlate. Alger and Payne 2016 N=58: REM correlate. Same paradigm | a08 | K09 established |
| No overall sleep effect on DRM false memory | Lures g=.129, SE .210, CI [-0.282, 0.539], p=.540; Q(12)=63.227; Egger p=.365; 13 effects. Recall g=.606, CI [0.020, 1.192], p=.043. Recognition g=-.150, p=.538 | Newbury and Monaghan 2019 (b08, b09) | K05 established |
| Large preregistered DRM replication null | N=398 (104 sleep, 101 wake, 99 AM control, 94 PM control); no effect on false or general memory; false memory rose after sleep only when intrusion-adjusted memory was high (post hoc) | Nagel et al. 2026 (d18, abstract) | K05 established |
| Gist may need a long delay | 10 h: sleep raised old-item memory (t(12)=2.27, p=.043, eta2=.30), not prototype memory (t(12)=-0.08). One year (N=17): only prototypes encoded before sleep above chance, t(16)=6.25, p<.001, eta2=.71; old items at chance. REM vs item memory r=.61, p=.027. Gaze r=.57, p=.025. Stage correlates with year-long gist all \|r\|<.34 | Lutz 2017 (a11, b10) | K06 contested |
| Generalisation rose with time, not sleep | 4 h post-learning; sleep = wake; extraction hurt memory for arbitrary features; regularity robust over weeks | Sweegers and Talamini 2014 (a12, abstract) | K06 contested |
| New items that fit a schema consolidate better | Spindle density + SWS explain 56.2% of variance in overnight schema effect, F(5,13)=5.63, p=.006 (N=19 in regression; groups 23 and 24); spindle t=4.11, p=.001; SWS t=-3.05, p=.009; unrelated facts F(17)=0.69. Rats: one-trial learning became hippocampus-independent once a schema existed | Hennies 2016 (a13); Tse 2007 (a14) | K08 established |
| Human replay is structure-guided | After learning a rule, new objects replayed in rule-implied order; peak 40 ms lag; beta=.017+-.005; Study 1 N=21 (16 forward), Study 2 N=22 (17 forward); awake rest, MEG | Liu et al. 2019 (a18) | K21 single-source |
| Overlap causes interference that sleep-like replay repairs (network) | Overlapping pixels 12-16; CUB-200 two tasks 5%/95% to 63.2%/45.4% with sleep replay; CIFAR-10 44% vs 19%; below rehearsal with 0.75% stored data in one column (48.47 vs 79.91) | Tadros 2022 (a20) | K10, K26 |
| Interleaved/generative replay beats regularisation | Split MNIST class-IL: fine-tune 19.90, EWC 19.90, SI 20.04, LwF 24.17, DGR 91.24, RtF 92.56, upper bound 97.93. Wake/NREM/REM net: wake only 4.70, +NREM 27.61, +REM 25.68, all 35.68 | van de Ven 2020 (c25); Sorrenti 2023 (c24) | K10 established |
| Replay + shared-fragment extraction raises later solve rate (programs) | DreamCoder SyGuS 3.7% to 79.6%, 235 s to 40 s; CVC4 82.4%, DreamCoder 84.3% with generous budget; LOGO/tower near 100% vs no baseline above 60%; physics 93% of laws after 8 cycles | Ellis 2020 (a21, b14, c11) | K11 established |
| LILO beats DreamCoder by mean solve rate | REGEX +33.14 (77.07 vs 43.93), LOGO +20.42, CLEVR +2.26; vs LLM-only +0.94, +8.09, +16.82. Use means, not the best-seed values 93.20/73.87 | Grand 2024 (a22, b16, c12) | K11 established |
| Unreadable merged abstractions hurt | Stitch without names vs plain solver: REGEX -30.60 as reported (mean difference -22.93), CLEVR -2.91, LOGO -11.11. AutoDoc adds +9.73, +2.27, +0.00 | LILO (b16, d05) | K12 single-source |
| LLM asked to compress code fails | 19.01% valid (998/5250); REGEX 24.93%, CLEVR 24.20%, LOGO 4.93%; compression ~1.0x vs Stitch 1.5x-3.5x | LILO appendix (a22, d06) | K13 established |
| Refactor bank raises accuracy; order matters | ReGAL: +11.5% LOGO, +26.1% Date, +8.1% TextCraft (best cases); CodeLlama-13B + bank beat GPT-3.5 without by 19.2% on LOGO; no curriculum: LOGO 55.0 to 36.3, Date 77.0 to 56.6, TextCraft 34.12 to 28.78 | Stengel-Eskin 2024 (b17, b25, d08) | K18 single-source (order) |
| Workflow induction lifts web agents | AWM WebArena 23.5 to 35.5 (+12.0, +51.1% rel.); Mind2Web cross-task step SR 36.2 to 45.1 offline, 43.6 online; cross-domain 18.6 to 32.6 / 35.5; gap 8.9 to 14.0 as distance grows; beat 14 human workflows (35.5 vs 33.0) | Wang 2024 (b18, c01, c02) | K11, K22 established |
| Abstraction vs whole examples | AWM vs Synapse +5.0 element accuracy, +4.0 step SR; ExpeL insights vs retrieval HotpotQA 36 vs 31, ALFWorld 50 vs 55, WebShop 37 vs 38; Mind2Web full-task success only 1-5% | c02, c15, d15 | K16 established |
| Success-only merge is model dependent | WebArena no memory / AWM: Claude-3.7 41.7 / 40.8; Gemini-2.5-pro 46.7 / 47.6; Gemini-2.5-flash 40.5 / 44.1. ReasoningBank (learns from failures too) 46.3 to 56.3 across backbones; retrieving 1 item 49.7 vs 4 items 44.4 | ReasoningBank (c03, d17) | K15 established |
| Incremental edits beat free rewrite | ACE: +10.6% agent, +8.6% finance; rewrite collapsed 18,282 tokens to 122 and accuracy 66.7 to 57.1 (base 63.7); dedup threshold 50/70/90% gives 77.0/73.9/78.6 | ACE (c04, c05) | K13, K14 established |
| Offline compute pays when later queries overlap | Sleep-time compute ~5x less test-time compute, +13% (GSM), +18% (AIME), 2.5x lower cost per query (~10 questions per context, t=10); LightMem up to 38x fewer tokens | a23, d02, c08 | K19 established |
| Count trigger and cadence have an optimum | RecMem count 5: 81.1 vs count 6: 78.9, 87.3% fewer construction tokens; Auto-Dreamer k=1 and k=20 worse than k=8-10 on ScienceWorld; bank shrunk 6x-11x | RecMem (d03); Auto-Dreamer (d04) | K31 single-source |
| Add-all memory hurts | RegAgent 55.48 vs fixed 67.53 vs strict 70.95; EHRAgent 13.05 / 16.75 / 38.50; AgentDriver 32.32 / 40.11 / 51.00; CIC-IoT 59.90 / 71.50 / 85.40 | Xiong 2025 (d14) | K27 established |
| Regression gate on stored cases | MedAgentBench gpt-oss-120b: no skills 40.6; GRASP 88.8; no gate K=1 40.1, K=4 63.5; no regression budget 81.8; probe run, verdict ignored 70.8 / 67.2; gate on five baselines +1.6 to +15.0 in-domain, ~0 out-of-domain | GRASP (d11) | K28 single-source |
| LLM reader is a weak guard | Unguided judge picks better skill 46.4%; 15.8% on largest gaps; rubric 73.8%; 25% of extractor-target pairs negative (47% ALFWorld) | Huang 2026 (d13) | K29 single-source |
| Math libraries often unused | TroVE 3 correct reuses in 3,201 MATH questions; no-reuse ablation equal or higher (number theory 0.290 vs 0.258); LEGO-Prover 0-1 lemma reused per split; DSP matches at matched budget (cost ratio 5.84-14.23) | Berlot-Attwell 2024, 2025 (d09, d10) | K30 single-source |
| Weak models gain little from memory | Haiku GPQA 43.4 / 41.9 / 43.7 / 49.0; GPT-4o-mini AIME 2024 16.7 / 20.0 / 13.3 / 13.3 (30-item sets, 1 item = 3.3 points); GRASP: all three transferred libraries lowered FHIR baseline 51.5 (47.2, 45.7, 48.3) | b19, d01, d12 | K17 established; K32 contested |

## 4. Mechanisms and models

Five mechanisms matter for implementation. Each is described so it can be coded.

### 4.1 iOtA: overlap strengthening plus decay of the rest

Human version: a store of traces, each a set of elements. Replay picks several related traces at once. Each element gets a Hebbian increment per replay. A global downscaling shrinks all weights. Elements shared by many traces survive; unique elements fall below threshold.

Engineer version (a toy, not tested in LLMs):
1. Represent each solved case as a set of fragments (steps, sub-rules, patterns).
2. Pick a cluster of related cases (see 4.3).
3. For each fragment, count the cases in the cluster that contain it. Call this its overlap count.
4. Fragments with overlap count at or above a threshold become the candidate rule. Fragments below stay only in the raw case.
5. Raw cases are kept (K23). Only the rule store is rewritten.

This gives a gate on structure. Matorina's data say that surface overlap alone is not enough: sets that were fully connected by relations survived, while overlapping categories and statistical sets decayed (b04, K07). So step 4 should also check that the fragment supports a derived conclusion on a held-out case (G3).

### 4.2 BiOtA: two-pass consolidation (single source, contested)

Pass 1 (non-REM analogue): merge cases inside one family into a rule. Pass 2 (REM analogue): compare whole rules across families to find structure they share. Pass 3: reconcile, by re-running pass 1 with the new cross-family rules visible. Order is a testable ablation (K09, K18). Only ReGAL's easy-to-hard ordering is tested (d08), and not a within-family-first order.

### 4.3 Finding the overlap set

The sleep theory says the hippocampus picks which memories to replay together. In an agent, code must pick. Options with their evidence:
- Symbolic fragment compression (Stitch). Needs rules as code or structured trees. 1.5x-3.5x compression on frozen LILO programs where GPT-4 got about 1.0x. 3-4 orders of magnitude faster than DreamCoder's compressor; test compression ratios 2.55x-11.57x across eight graphics domains (c10, d06).
- Shared entities (HippoRAG): up to +20 points R@5 on 2WikiMultiHopQA; weaker on HotpotQA. This is retrieval, not abstraction (c17).
- Embedding similarity: not reliable. In LILO, similarity vs random example choice: REGEX 77.07 random vs 71.33 similar; CLEVR 96.76 vs 97.41; LOGO 48.95 vs 53.15. Similarity was fooled by shared surface words (d07).
- Link before edit (A-MEM): LoCoMo multi-hop F1 9.65 with neither module, 21.35 without evolution, 27.02 full (messy table; c07).
- Cluster by query embedding then order short to long (ReGAL, Ward clustering; d08).
- Recurrence counts (RecMem): similarity 0.7 and count 5 (d03).
No head-to-head of entity overlap versus embedding versus symbolic exists (K24).

### 4.4 The wake-sleep loop (DreamCoder, LILO)

1. Wake: solve tasks, keep solutions that pass a check.
2. Sleep-abstraction: take solved programs, find fragments common to several, add each as a named primitive if it shortens total description length.
3. (LILO only) Document: an LLM writes a name and a docstring for each new primitive. Without this, the solver misuses it (K12).
4. Sleep-dreaming (DreamCoder only): train a recogniser on replayed and imagined tasks.
5. Repeat. The library grows in layers.

The compression criterion is measurable: a merge is accepted only if total description length of solved cases falls. Cost: DreamCoder took about a day on 20-100 CPUs.

### 4.5 Memory-update disciplines from LLM agents

- ACE grow-and-refine: append bullets, update in place, dedup by embedding similarity. Never rewrite the whole context (c04, c05).
- ExpeL: ADD, EDIT, UPVOTE, DOWNVOTE on an insight list; remove at zero count (c15).
- LightMem: append online (soft update), merge only offline, compare only similar entries, later entries may update earlier ones only. Worked example shows hard update deleting a compatible fact (c08, c09). The loss rate is not measured.
- GRASP gate: probe set of stored pass and fail episodes, hard regression budget, reject an edit if too many old cases break (d11).
- Xiong deletion: remove records whose later use correlates with failure (d14).
- Auto-Dreamer: rewrite only a region (new entries plus recently retrieved old ones) every k tasks (d04).
- RecMem: run the LLM merge only when a similar cluster has recurred count times (d03).

### 4.6 Complementary stores

Keep a verbatim case store and a separate rule store, with separate retrieval (K23). Route by task type: rules for reasoning-style questions, raw cases for exact action sequences (ExpeL; the router is hand-set by the authors, d15).

## 5. What holds up

### Replications and failures (human)

- Wagner 2004 number reduction: young adults yes; older adults no (Debarnot 2017, N=74); no gain without initial training. Task-bound.
- Durrant 2011 SWS: not reproduced in the one larger test (Matorina N=69, preprint). No peer-reviewed large replication of Durrant 2011 or of Matorina's REM result exists as far as found (K34). Same group's later nap and cueing studies are not independent labs (a05).
- Lau 2010 vs Alger and Payne 2016: same paradigm, different stage (K09).
- Ellenbogen 2007: replicated by Werchen and Gomez 2013 (N=64; implicit yes, explicit no; seen via review only, a07). The gain is on the far pair only. Use b05, not a07, for numbers (critique B).
- DRM false memory: meta-analysis null (g=.129); recall-only effect barely excludes zero (CI lower bound .020); Nagel 2026 N=398 null.
- Lutz 2017: short delay null for gist, one-year effect on N=17 (11 of 28 lost).
- Sweegers 2014: time helps, sleep does not add.
- Lerner and Gluck 2019: 14 of 30 explicit-detection studies positive; nine of nine stationary-rule explicit tests null.

Moderators that recur: task type (temporal vs stationary rule), age, whether initial training occurred, recall vs recognition, retention delay, and whether the prior schema existed.

### Interventions that worked (LLM and AI)

- Extract common fragments from several solved cases and add them as named primitives (DreamCoder, LILO, ReGAL, AWM).
- Name and document each merged rule (LILO).
- Admit only checked-successful runs (AWM judge; ReGAL; all six opened systems merge only solved items, b22).
- Include failures as a separate counterfactual signal (ReasoningBank).
- Merge offline and incrementally (LightMem, ACE).
- Gate edits with a regression probe (GRASP).
- Order easy to hard (ReGAL).
- Trigger by count (RecMem) or cadence (Auto-Dreamer).
- Offline compute shared over about 10 related queries (sleep-time compute).

### Interventions that did not work

- Unaided LLM compression of programs: 19.01% valid (LILO).
- Unlabelled abstractions: below the no-library solver on all three domains (LILO).
- Whole-context LLM rewrite: ACE collapse, 66.7 to 57.1.
- Add-all admission (Xiong), ungated skill edits (GRASP: 40.1 vs no-skills 40.6).
- Cosine-similarity grouping as a guarantee (LILO d07).
- Free-text math libraries: near-zero reuse, no gain at matched compute (d09, d10).
- Small models using their own memory (Dynamic Cheatsheet d01), and libraries moved to a different benchmark (GRASP d12).
- Adding reflections into insight extraction (ExpeL).
- More retrieved items: 1 item 49.7, 4 items 44.4 (ReasoningBank d17).
- Voyager: library slowed the stone tier (11 vs 9 iterations) while iron improved (21 vs 29) (c13).

### Contradictions not settled

- SWS vs REM vs neither as the carrier of abstraction (K09).
- Whether gist needs one night, many nights, or just time (K06).
- LLM-written insights succeed in ExpeL, AWM and ACE but fail in LILO. Reconciled by task: LILO needed executable, valid code; the others store prose (critique).
- Strong-writer to weak-solver libraries: help in GRASP (gated), fail in Dynamic Cheatsheet and one ASDA snippet, help in a SKILL-DISCO snippet. Snippets not opened (K32).

## 6. Language models

What LLMs do on these tasks, with measured size.

**Library learning on code DSLs (best evidence).**
- LILO: +33.14 REGEX, +20.42 LOGO over DreamCoder (means). Gain over LLM-only solver is small on REGEX (+0.94, 77.07 vs 76.13, std 1.50 vs 12.04) and larger on LOGO (+16.82). Part of the gain is the LLM prior itself: unaided LLM beat DreamCoder by +32.20 on REGEX.
- ReGAL: up to +11.5% LOGO, +26.1% Date, +8.1% TextCraft. A 13B code model with the bank beat GPT-3.5 without by 19.2% on LOGO. Gains were seen with 25 demos (+2.56%). Gains smaller for strong models.
- DreamCoder (not an LLM): 3.7% to 79.6% on SyGuS.

**Agent memory on web tasks.**
- AWM: +12.0 points WebArena (gpt-4); +8.9 to +14.0 points as distance grows. Gains within tens of examples (figure note: gap 22.5 after 40 examples; d16). Step success rises; full-task success on Mind2Web stays 1-5%.
- ReasoningBank: 46.3 to 56.3 depending on backbone; AWM was below no-memory for Claude-3.7 (40.8 vs 41.7) and degraded on cross-website tasks.
- SkillWeaver: WebArena 25% to 38% after 160 iterations; transfer to weaker agents up to +54.3% (c18; skills tested, not merged).
- Dynamic Cheatsheet: Claude 3.5 Sonnet +27 (AIME 2024), +30 (AIME 2025); GPT-4o Game of 24 from about 10% to 99% by reusing stored Python. The gain is largest when one reusable code recipe exists.

**Offline consolidation of conversation memory.**
- LightMem: accuracy up to +7.7% (LongMemEval) and +29.3% (LoCoMo), tokens down up to 38x and 20.9x. Offline step alone not isolated.
- Auto-Dreamer: bank tokens down 6x-11x; success ALFWorld 48.0 to 59.2 (untrained rewrite) to 60.2 (trained); ScienceWorld 29.6 to 31.4 to 41.1; WebArena 44.2 to 46.6 to 52.3. Lost location details on one task family. No seed variance reported.
- RecMem: score 81.1, 87.3% fewer construction tokens than Mem0.
- A-MEM: 85-93% fewer tokens per memory operation.
- Sleep-time compute: about 5x less test-time compute; +13% / +18%.

**Where it fails.**
- Math word problems with learned lemmas or functions: near-zero reuse; gains vanish once sampling and compute are matched (d09, d10).
- Weak solvers: gains small or negative (d01).
- Unreadable or ungated merges: -22.93 to -30.60 points (LILO), 40.1 vs 88.8 (GRASP).
- LLM judges of rules: 46.4% pairwise accuracy.
- LLM false memory (DRM analogue): critical lure marked old 0.114 vs 0.053 unrelated; small local models near none (d19). No study found of merged rules causing confident unsupported output.

**What the LLM side does not test.**
- Overlap-based grouping versus random grouping. Zero direct tests in 22 opened papers plus the gap search (K20).
- A token-matched gain from merged rules on free-text reasoning.
- A within-family-first merge order.
- A controlled merge-at-N sweep.

## 7. What our agent should take

Status codes: [E] established, [S] single-source, [C] contested. Evidence ids refer to evidence files; K ids to claims.jsonl.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Merge only from checked-successful runs; a merged rule enters the library only after a check on a case it was not fitted to. | G2, G3, memory | [E] | K15; c03, b18, c06, b22 |
| A2 | Do overlap finding and bookkeeping in code. The model may name a rule, fill one slot, or judge one pair. Never ask it to find shared structure unaided on structured rules. | G5 | [E] | K13, K24; a22, d06, c10 |
| A3 | Name every merged rule in plain words with a one-line use condition. | memory, O2/O3 | [E] as direction (3 domains), magnitude single-source (K12) | b16, d05, c12 |
| A4 | Merge incrementally with logged edits and de-duplication; never rewrite the whole library in one model call. | memory | [E] | K14; c04, c05, c15, c08 |
| A5 | Keep raw cases in a separate store. Rules are a second store with its own retrieval. | memory | [E] | K23; a12, a17, a25, c05, d15 |
| A6 | Do not merge online. Append during a task; merge in an offline pass between tasks. | G1, G7 | [E] (LightMem argument plus ACE collapse; error rate not measured) | c08, c09, c05 |
| A7 | Keep admission strict. Add-all is worse than a small fixed memory. | G6, memory | [E] | K27; d14 |
| A8 | Cap how many rules enter a prompt (start with 1 to 2). | G11, memory | [E] direction, one benchmark | d17 |
| A9 | Test the library on the target solver, not the writer. Report per base model. | G7 | [E] | K17; b19, d01, d13 |
| A10 | Gate library retrieval by difficulty; expect no gain on easy items and more on deep, far-from-training items. | G12 | [E] | K22; c13, b18 |
| A11 | Any claimed gain from a merged library must beat the same agent with majority vote at equal tokens, and must report rule reuse rate. | G7 | [E] methodology | K30; d09, d10 |
| A12 | Between-task consolidation is worth its tokens only when later related tasks are expected (about 10 per context in the test). Count its tokens against later savings. | G7, G12 | [E] | K19; a23, d02 |
| A13 | Interleave the new case with old cases whenever the library is updated. Flag any old case that now fails. | memory, G3 | [E] | K10; a15, c25, a19 |

### Test first (single-source, contested or untested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Overlap-based groups for merging beat random groups at equal tokens. The central claim of the subfield. | memory, O2 | [S] none direct | K20; c29, d07, d08 |
| T2 | Regression gate: after a merge, replay stored pass and fail cases and reject if more than a small budget break. | G6, S6 | [S] | K28; d11 |
| T3 | Merge trigger by count of related unmerged cases (4 to 6), not by schedule. | G1 | [S] | K25, K31; d03, d04, c16 |
| T4 | Merge in easy-to-hard, checked-first order. | memory | [S] | K18; b25, d08 |
| T5 | Gate merges on structure (relations that support held-out derived conclusions), not only on surface overlap. | G3, O3 | [S] | K07; b01, b04, b05 |
| T6 | Two-pass merge: within family, then across families. | O7, memory | [C] | K09; a02, a26 |
| T7 | Exceptions list beside each merged rule; a rule must cite source cases. | G10, memory | [S] | K26, K35; b03, a20, d04 |
| T8 | Vote-and-prune (ExpeL) versus append-only versus rewrite. | memory | [S] | K14; c15, d14 |
| T9 | Value-weighted re-examination of cases (replay salient or surprising cases more). | G12 | [S] | K21; a03, a18, a16 |
| T10 | Rules versus raw cases routed by task type. | memory | [S] | K16, K23; d15, c02 |
| T11 | Generation test for merged rules causing unsupported output (DRM analogue), not recognition only. | G2, G10 | [S] | K05, K35; b09, d19 |
| T12 | Strong writer to weak solver transfer with a gate. | G7 | [C] | K32; d11, d12, d01, d13 |
| T13 | Long-horizon library value measured after 100+ tasks, not at the next task. | G7 | [C] | K06, K33; a11, d16 |

What to do with the human evidence: nothing in the schema should depend on SWS, REM or any sleep stage (K09, K34). Do not cite Wagner or Durrant as proof.

## 8. Concrete tests on our bench

Bench item types: ARC items (grid rule induction, code-checkable), BRAINTEASER items (small exact answers), NoveltyBench items (open mode). All arms spend equal tokens, with consolidation tokens counted inside the arm that uses them (G7). Hold out tasks from the cases used for merging. At least 3 seeds; report mean and std (LILO showed std 12-14 on small sets).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 overlap vs random merge | ARC items grouped by shared sub-rule family (e.g. symmetry, fill, recolour) | (a) merge overlap sets, (b) merge random sets of the same size, (c) no merge, raw-case retrieval only, (d) plain model plus majority vote at the same total tokens | Held-out solve rate; rule reuse rate; old-case breakage | (a) over (b) by 3+ points if overlap matters. LILO and ReGAL suggest the effect may be small; the null is informative |
| T2 regression gate | ARC and BRAINTEASER | merge with gate (probe of stored pass and fail cases, budget of 1 break) vs same merge without gate vs probe-run-verdict-ignored | Held-out solve rate; count of old cases broken | Gate helps; GRASP effect was large (40.1 vs 88.8) but on a different task. Expect smaller here |
| T3 trigger | ARC stream of 60 to 100 tasks | merge when a cluster of 4, 5 or 6 related unmerged cases exists vs fixed interval of 8 vs never | Solve rate on later tasks; consolidation tokens | Count trigger matches or beats fixed with fewer tokens |
| T4 order | ARC | easy-to-hard checked-first vs random order feeding the merge | Held-out solve rate | ReGAL: -18.7 for random on LOGO. Expect a smaller drop |
| T5 structure gate | BRAINTEASER with chained relations (A then B then C) | accept merge if it derives a held-out two-step conclusion vs accept on surface overlap alone | Accuracy on two-step derived items; false-rule admission count | Structure gate admits fewer false rules, possibly at equal accuracy |
| T6 two-pass | ARC across 3 or more rule families | within-family then cross-family pass vs single pass vs reverse order | Held-out solve rate on items mixing families | Small positive at best; sleep theory is speculative here |
| T7 exceptions | ARC and BRAINTEASER | merged rules with exceptions list and source citations vs without | Rate of confident wrong answers from merged rules | Fewer unsupported answers with the list |
| T8 update style | ARC stream | append-only vs vote-and-prune vs full rewrite | Solve rate; library size; breakage | Rewrite worst (ACE collapse); prune vs append close |
| T9 naming | ARC | each merged rule with name and use condition vs bare rule | Held-out solve rate | LILO: naming recovers most of a 10-30 point loss on code DSLs. Expect a smaller effect on prose rules |
| T10 routing | ARC (rule-heavy) and tasks needing exact earlier detail | rules only, cases only, both with hand-set router | Solve rate by task type | Rules win on general guidance, cases win on exact-detail items |
| T11 generation check | BRAINTEASER | after merge, ask for generated cases implied by the rule; check each against stored facts | Rate of implied cases that contradict stored facts | Measures the DRM analogue; no prior value |
| T12 weak solver | ARC with a smaller solver | library from strong writer, gated vs ungated vs none | Solve rate of weak solver | Gated helps, ungated may hurt (GRASP, Huang) |
| T13 long horizon | ARC stream 100+ tasks | solve rate in blocks of 20 with and without library | Block curve | Early dip is possible (LILO), gain later |
| NoveltyBench control | NoveltyBench open items | rules library on vs off | Novelty score (baseline 3.18 to 9.63 in the schema) | A merge library may narrow output (gist over detail). Expect no gain or a loss; check before enabling in open mode |

Always report the "no-memory plain model with majority vote at equal tokens" arm. Without it the result is unproven (d09, d10).

## 9. What does not transfer, and why

- **Sleep stages.** The SWS-vs-REM story flips between replications. There is no analogue for stages in an agent. Do not copy a stage order (K09).
- **Hebbian strengthening and global downscaling.** The agent has no synaptic weights. Counts and a keep threshold are an implementation choice, not a transfer of evidence.
- **One-year timescale.** Lutz's year-long gist effect (N=17) has no agent analogue. Agent benefits appeared in tens of tasks (AWM) or not at all (math libraries).
- **DRM false memory.** The sleep effect is null across 13 effects and a 398-person replication. LLM lure effects are small (0.114 vs 0.053). Do not expect a human-like gist intrusion from rule merging. Test it directly instead.
- **Rat place-cell replay.** A 20 s run replayed in 200 ms is trajectory replay, not replay of overlapping sets (a03).
- **Awake structured replay (Liu 2019).** Shows learned structure re-orders new items, not that overlap drives strengthening.
- **Neural-network sleep replay (Tadros, Sorrenti, van de Ven).** These protect old tasks from forgetting in image models. They do not extract shared structure. In Tadros, overlap is the source of interference, the opposite of a feature.
- **DSL results.** DreamCoder, LILO and ReGAL work on REGEX, LOGO, CLEVR, text editing and dates where a compressor exists. Free-text rules have no compressor. Math libraries failed. ARC programs may be closer to the DSL case if rules are written as code.
- **Step success vs task success.** AWM's step gains sit beside full-task success of 1-5% on Mind2Web.
- **Conversation-memory benchmarks.** LightMem, RecMem, A-MEM merge facts and dialogue, not rules. They support the process shape, not the merge value.
- **Small human samples.** Most human studies have N below 60. Lutz one-year N=17.
- **Detail loss.** Gist-over-detail is a feature in the brain. For an agent that must recall an exact earlier case, it is a loss. Keep raw cases (K23).

## 10. Open questions

1. Does overlap-based grouping beat random grouping at equal tokens in an LLM agent? (No published test; K20.)
2. Which overlap finder works best on structured rules: shared entities, embeddings or symbolic fragments? (No head-to-head; K24.)
3. Does a merged-rule library pay for itself on free-text reasoning at matched tokens? (Negative for two math systems; no positive result found.)
4. How many related cases are needed before merging helps, and does an early merge hurt first? (Tens of tasks in AWM; no controlled sweep; K33.)
5. Is a within-family-then-across-families order better than a single pass? (Untested; only easy-to-hard is tested; K18.)
6. What fraction of merged rules are bad, and which guard has the lowest admission rate? (GRASP gives accuracy, not a count; K28.)
7. Does a strong model's library help a weak solver, and under what gate? (Contested; K32.)
8. Is there a peer-reviewed large replication of Durrant 2011 or Matorina's REM result? (None found; K34.)
9. Can merged rules cause confident unsupported generation, the LLM version of a false memory? (Not tested; K35.)
10. Can a learned router choose between rules and raw cases? (No; routing is hand-set; K23.)
11. What is the break-even count of related later tasks for an offline merge? (Sleep-time compute states none; K19.)
12. Do human gains need multiple cycles (Lutz), and is there an agent analogue of repeated consolidation?

## 11. Sources

[V] = opened and read this session (per evidence files and critique). [M] = abstract, snippet or secondary text only.

**Human sleep and memory**
- [M] Lewis and Durrant 2011, Overlapping memory replay during sleep builds cognitive schemata. https://pubmed.ncbi.nlm.nih.gov/21764357/ (abstract read per critique; also https://doi.org/10.1016/j.tics.2011.06.004)
- [V] Lewis, Knoblich and Poe 2018, How memory replay in sleep boosts creative problem-solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC7543772/
- [M] Wagner et al. 2004, Sleep inspires insight. https://pubmed.ncbi.nlm.nih.gov/14737168/
- [M] Durrant et al. 2011, Sleep-dependent consolidation of statistical learning. https://pubmed.ncbi.nlm.nih.gov/21335017/
- [M] Durrant et al. 2013, Overnight consolidation aids transfer of statistical knowledge. https://pubmed.ncbi.nlm.nih.gov/22879350/
- [V] Ellenbogen et al. 2007, Human relational memory requires time and sleep. https://pmc.ncbi.nlm.nih.gov/articles/PMC1863467/
- [V] Lerner and Gluck 2019, Sleep and the extraction of hidden regularities: a systematic review. https://pmc.ncbi.nlm.nih.gov/articles/PMC6779511/ (first 100,000 characters via summarising fetch)
- [M] Lau et al. 2010; Alger and Payne 2016; Werchen and Gomez 2013; Debarnot 2017; Song 2007; Hallgato 2013; Wilhelm 2013 (all via Lerner and Gluck table, same URL)
- [V] Lutz et al. 2017, Sleep supports the slow abstraction of gist. https://pmc.ncbi.nlm.nih.gov/articles/PMC5314355/
- [M] Sweegers and Talamini 2014, Generalization from episodic memories across time. https://pubmed.ncbi.nlm.nih.gov/25129237/
- [V] Hennies et al. 2016, Sleep spindle density predicts the effect of prior knowledge. https://pmc.ncbi.nlm.nih.gov/articles/PMC4812136/
- [M] Tse et al. 2007, Schemas and memory consolidation. https://pubmed.ncbi.nlm.nih.gov/17412951/
- [V] Matorina and Poppenk 2019 (preprint), REM negatively predicts statistical learning but not other forms of gist. https://www.biorxiv.org/content/10.1101/578492v3.full.pdf
- [V] Newbury and Monaghan 2019, When does sleep affect veridical and false memory consolidation? https://pmc.ncbi.nlm.nih.gov/articles/PMC6488554/
- [V] Nagel et al. 2026, Sleep links gist abstraction to veridical memory (abstract only, so [M] for full text). https://pubmed.ncbi.nlm.nih.gov/42024337/
- [V] Liu et al. 2019, Human replay spontaneously reorganizes experience. https://pmc.ncbi.nlm.nih.gov/articles/PMC6657653/

**Models and theory**
- [M] McClelland, McNaughton and O'Reilly 1995. https://pubmed.ncbi.nlm.nih.gov/7624455/
- [M] Kumaran, Hassabis and McClelland 2016. https://pubmed.ncbi.nlm.nih.gov/27315762/
- [V] Schapiro et al. 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5124075/
- [M] Winocur and Moscovitch 2011. https://pubmed.ncbi.nlm.nih.gov/21729403/

**Neural-network replay**
- [V] van de Ven, Siegelmann and Tolias 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7426273/ and https://arxiv.org/abs/1809.10635
- [V] Tadros et al. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9755223/
- [V] Sorrenti et al. 2023, Wake-Sleep Consolidated Learning. https://arxiv.org/abs/2401.08623

**Program and library learning**
- [V] Ellis et al. 2020, DreamCoder. https://arxiv.org/abs/2006.08381
- [V] Grand et al. 2024, LILO. https://arxiv.org/abs/2310.19791
- [V] Bowers et al. 2023, Stitch. https://arxiv.org/abs/2211.16605
- [V] Stengel-Eskin et al. 2024, ReGAL. https://arxiv.org/abs/2401.16467
- [V] Berlot-Attwell, Rudzicz and Si 2024, Library Learning Doesn't. https://arxiv.org/abs/2410.20274
- [V] Berlot-Attwell, Rudzicz and Si 2025, LLM Library Learning Fails. https://arxiv.org/abs/2504.03048
- [V] Wang et al. 2023, Voyager. https://arxiv.org/abs/2305.16291
- [V] Zheng et al. 2025, SkillWeaver. https://arxiv.org/abs/2504.07079
- [V] Cai et al. 2024, LATM (abstract and intro only). https://arxiv.org/abs/2305.17126

**LLM agent memory and consolidation**
- [V] Wang et al. 2024, Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Ouyang et al. 2025, ReasoningBank. https://arxiv.org/abs/2509.25140
- [V] Zhang et al. 2025, ACE. https://arxiv.org/abs/2510.04618
- [V] Suzgun et al. 2025, Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952
- [V] Xu et al. 2025, A-MEM (table cells messy). https://arxiv.org/abs/2502.12110
- [V] Fang et al. 2025, LightMem (tables messy). https://arxiv.org/abs/2510.18866
- [V] Zhao et al. 2024, ExpeL. https://arxiv.org/abs/2308.10144
- [V] Park et al. 2023, Generative Agents. https://arxiv.org/abs/2304.03442
- [V] Shinn et al. 2023, Reflexion. https://arxiv.org/abs/2303.11366
- [V] Gutierrez et al. 2024, HippoRAG. https://arxiv.org/abs/2405.14831
- [V] Lin et al. 2025, Sleep-time Compute. https://arxiv.org/abs/2504.13171
- [V] Dai et al. 2026, RecMem. https://arxiv.org/abs/2605.16045
- [V] Ye et al. 2026, Auto-Dreamer. https://arxiv.org/abs/2605.20616
- [V] Moll et al. 2026, GRASP. https://arxiv.org/abs/2605.29668
- [V] Huang et al. 2026, From Raw Experience to Skill Consumption. https://arxiv.org/abs/2605.23899
- [V] Xiong et al. 2025, How Memory Management Impacts LLM Agents. https://arxiv.org/abs/2505.16067
- [V] Cao et al. 2025, Memory Effects in LLMs through Cognitive Psychology. https://arxiv.org/abs/2509.17138
- [V, intro/abstract only] Fountas et al. 2025, EM-LLM. https://arxiv.org/abs/2407.09450
- [V, weak evaluation] Zhong et al. 2023, MemoryBank. https://arxiv.org/abs/2305.10250
- [V] Memory in the Age of AI Agents: A Survey (2026). https://arxiv.org/abs/2512.13564
- [M] MOOM (2025), snippet only. https://arxiv.org/abs/2509.11860 (do not cite without opening)
- [M] SKILL-DISCO, ASDA, Skill Transfer NeurIPS 2026, snippets only. https://arxiv.org/abs/2606.26669

**Corrections carried from the critique.** LILO "max" columns (93.20, 73.87, 45.60) are best-of-3 seeds, not means; use means. The LILO REGEX -30.60 is a difference of maxima; the mean difference is -22.93. Sleep-time compute appears three times in the evidence (a23, b20, c20) but is one paper; DreamCoder three times (a21, b14, c11); van de Ven twice (a19, c25). Evidence a07 overstates the Ellenbogen result; use b05.

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 13 established claims: 7 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B04.09-K10** (reworded: the sources support less). Tadros Table 1: SRC is below 0.75 percent rehearsal in three of five columns (e.g. 48.47 vs 79.91) but above it on Inc. CIFAR10 (44.55 vs 39.39) and on the CUB-200 average (63.2/45.4 vs 42.32/51.49), so 'scores below rehearsal' is not general. Corrected claim: In artificial networks, interleaved replay of old items with new ones prevents overwriting, and generative or representation replay beats regularisation: Split MNIST class-IL fine-tune 19.90, EWC 19.90, DGR 91.24, RtF 92.56, upper bound 97.93. Sleep-like replay without stored data (Tadros 2022) raises CUB-200 two-task accuracy from 5/95 to 63.2/45.4, but in its own Table 1 it scores below rehearsal with 0.75% stored data on Inc. MNIST, Fashion MNIST and multi-modal MNIST (e.g. 48.47 vs 79.91), and above it on Inc. CIFAR10 (44.55 vs 39.39).
- **B04.09-K14** (reworded: the sources support less). Only ACE contrasts incremental merging with free whole-context rewriting (a single AppWorld case study of context collapse, in a Dynamic Cheatsheet-style rewrite, plus gains over baselines); ExpeL and LightMem are described designs with no head-to-head against free rewrite, so 'works better than free rewrite' rests on one paper. Corrected claim: Incremental edit merging with de-duplication is used in ACE (grow-and-refine: +10.6% agent, +8.6% finance over strong baselines; its context-collapse case study shows free whole-context rewriting destroyed information; dedup threshold effect non-monotone 77.0/73.9/78.6 at 50/70/90%), ExpeL (ADD/EDIT/UPVOTE/DOWNVOTE with removal at zero) and LightMem (append online, merge offline), but only ACE compares against free rewrite.
- **B04.09-K16** (reworded: the sources support less). AWM's gain over whole-example retrieval (Synapse) is on Mind2Web, a web-action task, which contradicts 'but not on action tasks'; the ExpeL split (HotpotQA vs ALFWorld) is the only support for the reasoning versus action contrast. Corrected claim: Abstracting sometimes beats storing whole examples and sometimes does not, depending on the task: AWM beat Synapse's whole-example retrieval on Mind2Web (+5.0 element accuracy, +4.0 step success), and ExpeL insights-only beat retrieval-only on HotpotQA (36% vs 31%) but lost on ALFWorld (50% vs 55%). Mind2Web full-task success stays 1-5%.
- **B04.09-K17** (reworded: the sources support less). Dynamic Cheatsheet Table 3 shows Claude 3.5 Haiku gaining +26.7 points on AIME 2024 (10.0 to 36.7), as large as Sonnet's, so gains were not small for Haiku (only GPQA-Diamond and GPT-4o-mini were flat or negative); and ReGAL found the smallest model (CodeLlama-13B) benefited most, the opposite of a gains-shrink-with-weak-models pattern. Corrected claim: Memory gains depend on the base model but do not simply shrink with model size: Dynamic Cheatsheet gains are mixed for GPT-4o-mini (AIME 2024 16.7 to 13.3 under DC-Cu, AIME 2025 10.0 to 16.7 under DC-RS, GPQA-Diamond flat or down) and for Claude 3.5 Haiku are large on AIME (10.0 to 36.7 and 0.0 to 13.3) but flat on GPQA-Diamond except DC-RS (43.4 to 49.0), and minimal or inconsistent for o1 and R1; ReGAL gives its largest gains to the smallest model tested (CodeLlama-13B), though large models also gain; and a memory built by a stronger model does not reliably help a weaker one (Dynamic Cheatsheet). [Gap search: Dynamic Cheatsheet numbers confirmed (30-question AIME sets). Reversal exists: GRASP strong-writer libraries help weaker executors when gated; weak-writer libraries hurt strong ones; 25% of extractor-target pairs are negative in Huang 2026; skill value does not track model size.]
- **B04.09-K23** (reworded: the sources support less). Sweegers 2014, Winocur and Moscovitch 2011, ACE collapse (18,282 to 122 tokens, 66.7 to 57.1 vs 63.7 base) and ExpeL numbers (36/31, 50/55, 37/38) check out, but Schapiro 2017 does not simulate summarising or gist extraction or test its effect on episodic recall; it only shows separate pathways learn regularities and individual episodes. Corrected claim: Keep episodic cases and gist rules as separate stores with separate retrieval: regularity extraction trades detail for gist (Sweegers 2014), the Schapiro 2017 model has separate pathways for regularities and single episodes (it does not test whether summarising harms episode recall), gist is hippocampus-independent while detail is not (Winocur and Moscovitch 2011), and ACE shows full LLM rewriting of a context can destroy information (one case: 18,282 to 122 tokens). [ExpeL numbers rechecked: insights vs retrieve-only HotpotQA 36 vs 31, ALFWorld 50 vs 55, WebShop 37 vs 38. Routing is by the authors' task type; no learned router found.]
- **B04.09-K24** (reworded: the sources support less). All figures check out (HippoRAG +21.3 R@5 on 2Wiki single-step, A-MEM ablation, Stitch 3-4 orders faster, LILO LLM compressor 19.01% valid, similarity vs random mixed), but the headline 'best done with cheap structure, not the model' is wider than the sources: HippoRAG and A-MEM both use an LLM to build their structure, and the claim itself concedes no head-to-head exists. Corrected claim: Overlap finding works better with explicit structure than with an unaided LLM or plain embedding similarity: shared entities (HippoRAG, +21.3 R@5 on 2Wiki single-step, +3 on MuSiQue, below baseline on HotpotQA), linking before editing (A-MEM ablation, though its links use an LLM), and symbolic top-down compression (Stitch, 3-4 orders of magnitude faster than DreamCoder's compressor; an LLM compressor gave valid abstractions only 19.01% of the time in LILO). Caveat: cosine similarity was fooled by shared surface words in LILO and did not reliably beat random example choice. No head-to-head of entity overlap vs embedding vs symbolic compression exists.
- **B04.09-K03** (now single-source: only one opened source, code check).
- **B04.09-K08** (now single-source: only one opened source, code check).
- **B04.09-K22** (now single-source: only one opened source, code check).
