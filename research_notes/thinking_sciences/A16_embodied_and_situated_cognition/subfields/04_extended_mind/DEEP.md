# Extended mind: deep document

*Subfield A16.04. Scope: tools and notes as constituents of cognition. Schema focus: memory (notes and the library). Built from evidence_a-d.jsonl (a01-a30, b01-b26, c01-c28, d01-d18), claims.jsonl (K01-K35) and critique.md in this folder. Status marks: [E] established, [S] single-source, [C] contested. Date 2026-11-01.*

## 1. What it is

The extended mind thesis says that some mental processes, and some beliefs, are not only in the head. A notebook, a phone or a diagram can be part of the thinking system when it plays the same role an inner process would play (a01, a02). The claim is about constitution: the tool is a part of cognition, not only a helper.

Critics say this is ordinary tool use. They hold that a tool is causally coupled to thinking or embedded in a setting, and that this does not make it a part of the mind (a05, a06, a08, b01). The dispute is mostly philosophical. No experiment in our evidence separates "extended" from "embedded" (b26, K02).

Why we care. Our agent is an LLM with a scaffold. Its notes file and its skill library are outside the model. The thesis gives two practical things:
1. A design test (parity): if the store is used like memory, hold it to the rules we hold memory to.
2. A warning list (from the critics and from experiments): outside stores can be over-used, mis-trusted, left unused, or can leave the user weaker at the item stored.

For the agent, the label does not matter. What matters is measured: when to write a note, when to read it, how much to trust it, and what format works at equal tokens.

## 2. History and theories in depth

### 2.1 Founding paper (Clark and Chalmers 1998, a01-a04)

- Case: Inga remembers that MoMA is on 53rd Street. Otto has Alzheimer's and reads the address from his notebook. They say Otto believed it before he looked, because the notebook plays for Otto the same role that memory plays for Inga (a01).
- Twin Otto: his notebook wrongly says 51st Street, so he believes 51st (a01). This is the failure case for any note store: a wrong note is a wrong belief.
- Parity principle: if a part of the world works like a process we would call cognitive if done in the head, it is part of the cognitive process. It is a test of function, not location (a02).
- Four conditions for a store to count as belief-like (a03): (1) constant in the person's life, (2) directly and easily available, (3) automatically endorsed on retrieval, (4) consciously endorsed in the past. The fourth is arguable. Condition 3 is dangerous for an agent: it is the same property that lets a wrong note poison later steps.
- Other cases in the paper: Tetris piece rotation by button takes about 100 ms plus about 200 ms to select, versus about 1000 ms mentally (a04, quoted from Kirsh and Maglio); language and social extension.
- Limits: a thought experiment with no data. It rests on functionalism.

### 2.2 Wide computation and Supersizing (Wilson 2004, Clark 2008)

- Wilson argues from long multiplication: working on paper is easier than in the head, so the computation can be spread over head and paper (a07). This is the closest human analogue of a scratchpad for an LLM.
- Clark 2008 (Supersizing the Mind) replies to the critics (a08, b12; the latter seen only as a snippet).

### 2.3 The critics

- Adams and Aizawa: the coupling-constitution fallacy. A causal link between a process and a tool does not make the tool part of the process. They also give a "mark of the cognitive": intrinsic, non-derived content. Notes carry only derived content (a05, a08, b13). Adams and Aizawa (2010) add cognitive bloating (everything would count as cognition) (a08).
- Rupert: cognitive systems are embedded in tool-rich settings, not constituted by them. His axe analogy: a person using an axe does not make the axe part of the body (a06). Embedding explains the same data with less.
- Both critics accept that tools matter causally. They deny constitution.

### 2.4 Newer arguments

- Smart, Clowes and Clark (2025) test the thesis on an LLM plus retrieval (Digital Andy, c01-c04). They raise three problems. Redundancy: if a persona prompt alone does as well as retrieval, the store adds nothing constitutive (c02). Agency: the app, not the model, triggers retrieval and builds the prompt (c03). Use-versus-ignore: the store only matters if the model actually factors in the retrieved text; no one counted this (c04).
- Clark (2025, Nature Communications) argues generative AI extends thought only with calibrated trust, and that the key skill is choosing when to rely on inner memory or a tool by reliability, cost and fragility (a21, a22, c05).
- Direct-input-variable argument (a30): outside input can be modelled as a probability-weighted input, with no need to call it part of the mind. This drops the reliability and accessibility conditions.

### 2.5 Empirical neighbours

The thesis itself is not tested, but a family of experiments is close to it:
- Google effects on memory (Sparrow 2011, a09, b05).
- Cognitive offloading (Risko and Gilbert 2016 framework, a15, b25; Gilbert and colleagues, a13, a14, b07, b08).
- Saving-enhanced memory (a12, b23).
- Photo-taking impairment (b10, d17).
- Skill atrophy: GPS (a18).
- LLM-assisted writing and memory (a23, a24).
- For agents: memory systems (MemGPT, Generative Agents, Reflexion, Voyager and others, section 6).

## 3. Core findings with exact numbers

Status uses the claims.jsonl label: established, single-source or contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Otto's notebook counts as belief store if constant, available, endorsed (parity) | Thought experiment; four conditions | a01-a03 | single-source (K01) |
| Critics: coupling is not constitution; no data separates the views | No numbers | a05, a06, a08, b01, b26 | contested (K02) |
| Google effect: expecting access lowers recall of content; may raise recall of location | Meta-analysis: 22 articles, 35 comparisons, 30,889 people, ages 12-89; d from -0.85 to 4.38 (range as reported in earlier lines; not found in the full text); cognitive-load subgroup d=0.73 [0.22, 1.24]; another subgroup 1.01 [-0.12, 2.13] | a19, b02, d04 | contested (K03) |
| Google Stroop priming failed to replicate | Original N=46, hard-question accuracy 47% vs 98% easy. Hesselmann: N=117 tested, 89 final; hard-block RT 825 vs 821 ms; BF01=5.07 for the null; hard accuracy 60%. Camerer: stage 1 N=104, pooled N=234, null | a09-a11, b04, d03 | established (K04) |
| Replication project overall | 13 of 21 (62%) replicated; mean effect about 50% of original | a10 | established (context) |
| Saving a file frees resources for new learning | Three experiments; sizes not read | a12, b23 | single-source (K05) |
| People offload more than optimal; driven by low confidence and effort avoidance; pay reduces but does not remove it | Registered report 2020 (rewarded vs flat pay); confidence study N=435 recruited, 363 analysed; metamemory: criterion more liberal for easy trials, diff 0.186 [0.070, 0.295] | a13, a14, a16, b07, b08 | established (K06) |
| Offloading speeds the task, no accuracy cost, worse later memory for offloaded items | Three experiments, N=172 each; identity memory t(170)=-2.76, p=.006, eta2=.04; identity-location t(170)=-2.63, p=.009; trial speed t(170)=-3.31 | b06 | established (K07) |
| Individual differences in offloading | N=114 final, set sizes 2-10 letters, registered report | b09 | single-source |
| Habitual GPS use goes with worse self-guided navigation | N=50, r=-0.22 [-0.41, -0.01]; follow-up N=13 | a18 | single-source (K08) |
| Searching the web inflates self-rated knowledge | Nine experiments | a17, b24 | single-source (K09) |
| Photographing impairs memory | Exp 1 N=60, 5-photo vs observe d=0.35 [0.09, 0.61]; 1-photo d=0.16 ns; Exps 2-3 replicate; earlier cited d=1.25; screenshots worst (d17) | b10, d17 | established (K10) |
| LLM-assisted essay writing: weaker brain connectivity, poor quoting | Failed to quote own essay: 15/18 (83.3%) LLM vs 2/18 (11.1%) Search, 2/18 Brain-only; pairwise p<.001; N=54 in sessions 1-3; session 4 N=18 (9 per group): reassigned LLM group 1/9 quoted correctly vs reassigned Brain-only 7/9. Preprint | a23, a24, b22, c27, d01, d02 | single-source (K11) |
| AI confidence goes with less critical thinking | 319 workers, 936 examples; no effect size seen | c28 | single-source (K12) |
| Medical students: AI-assisted study retained more | N=95 analysed; 1 week 75.5% vs 57.9%; 1 month 61.4% vs 35.9% | d18 | single-source (different design) |
| MemGPT tiered memory lifts deep memory retrieval | GPT-3.5 38.7 to 66.9; GPT-4 32.1 to 92.5; GPT-4 Turbo 35.3 to 93.4; ROUGE-L 0.296 to 0.814; nested KV: 0% at one level for GPT-3.5 baseline | a26, b14, c06, c07 | single-source (K13) |
| Long context fails to find memory in long history | LongMemEval (500 questions): GPT-4o 0.870 to 0.606 (-30.3%); Llama 3.1 70B 0.710 to 0.454 (-36.1%). LoCoMo: best model 32.4 vs human 87.9; RAG +22-66% but 56% below humans; temporal -73% | a29, b19, b20, c18, c20 | established (K14) |
| Lost in the middle | GPT-3.5 multi-doc QA can drop over 20% by position; below closed-book 56.1% in the middle; NoLiMa: GPT-4o 99.3 to 69.7 at 32K; 11 of 13 models below half of base | b21, c16, d16 | single-source (K15, K34) |
| Reflection notes across trials | HumanEval 91.0 vs 80.1; ALFWorld 130/134; +8% absolute from reflection over raw last trajectory (100 HotPotQA) | a27, b16, c11, c12 | contested (K16) |
| Reflection needs an outside correctness signal | GPT-3.5 HotpotQA 26 to 49 with oracle labels, 26 to 25 without; CommonSenseQA 75.8 to 38.1 without | d15 | established (K33) |
| Insight notes vs raw trajectories split by domain | ExpeL insights-only vs retrieval-only: HotpotQA 36 vs 31; ALFWorld 50 vs 55; WebShop 37 vs 38 | d14 | single-source (read with K33) |
| Memory stream with reflection | TrueSkill 29.89 full, 26.88 no reflection, 25.64 no reflection or planning, 22.95 crowdworkers, 21.21 none; 100 raters | a25, b17, c09, c10 | single-source (K17) |
| Verified skill library | 63 unique items in 160 iterations (3.3x); ablations: no self-verification -73%, random curriculum -93%; 3.3x/15.3x/2.3x ratios as reported, partly unverified | a28, b18, c13, c14 | single-source (K18) |
| Scratchpad for intermediate steps | 200 programs: 11% direct few-shot vs 26.5% scratchpad (loosened criterion); 20% vs 41.5% fine-tuned | c15, a07 | established (K19) |
| Reason-and-act with external sources | ALFWorld +34%, WebShop +10% absolute over imitation and RL | c24, c25 | single-source (K20) |
| Memory product rankings | A-MEM 85-93% fewer tokens per operation (about 1,200 vs 16,900); Mem0 91% lower latency, vendor-reported. Independent: BM25 41.5, HippoRAG-v2 41.6, bare model 42.3, MemGPT 28.3, Zep 24.0, Mem0 21.1 (GPT-4o-mini) | c22, c23, d12 | contested (K21, K31) |
| Wrong retrieved note is followed | ClashEval, 6 models, 1,200+ questions: context bias 15.7%-31.3% (Claude Opus 0.157, Sonnet 0.201, Gemini 1.5 0.245); prior bias (right note ignored) 2-4% | d05 | single-source (K22, K25) |
| Low model confidence predicts note reliance | Slope -0.1 to -0.45; calibration raised accuracy about 14%, cut context bias 20% | d05 | single-source (K26) |
| Models follow coherent counter-evidence, cling to prior under mixed evidence | GPT-4 memorization ratio 80% on popular facts (mixed condition) | d06 | single-source (K28) |
| Adaptive retrieval gate | PopQA 46.5%, +5.3 points over best fixed policy, about half the API cost; retrieval hurts on about 10% of questions; classifier misroutes 22-47% of some classes | d07, d08 | established (K27) |
| Curated notes beat full history and majority vote | Claude 3.5 Sonnet AIME 2024: baseline 23.3, 3-vote 23.3, full history 26.7, curated 50.0; AIME 2025 6.7 to 36.7; GPT-4o full history 6.7 vs baseline 20.0 | d09 | contested (K29) |
| Memory and test-time compute are complements | WebArena, Gemini-2.5-flash: no memory 40.5, ReasoningBank 48.8, +MaTTS 51.8; k 1 to 5 with memory 49.7 to 55.1; no memory stayed 39-42 | d10 | single-source (K30) |
| Gain from memory tracks task similarity | Pearson 0.717 (Gemini 2.5 Flash), 0.563 (Claude 3.7 Sonnet) | d11 | single-source |
| Note format at similar tokens | Raw rounds + facts as index keys +9.4% recall, +5.4% accuracy; time-aware expansion +6.8 to 11.3% recall on temporal questions; summaries lose information | d13, c20, c21 | single-source (K32) |
| Extended Mind Transformers | Retrieval accuracy at 16k: 33.54% vs base Chat Llama2 17.68%; at 2k the base is higher (42.74 vs 38.59) | b15 | single-source |

## 4. Mechanisms and models

### 4.1 Parity check as code (K01)
Define a store as "memory-like" when four checks hold. Implement them as flags on the notes module:
1. Constant: the store is loaded on every run with no setup step.
2. Available: a read costs one call and a fixed small token budget.
3. Endorsed on retrieval: a read result is inserted into the prompt as a trusted block. This is the risky flag; see 4.3.
4. Past endorsement: only entries the agent wrote and that passed a check are stored (Voyager stores a skill only after self-verification, up to 4 code rounds, retrieved top 5 by embedding of the description; c13, c14).

### 4.2 Offloading as a cost-benefit decision (Risko and Gilbert)
People pick the tool when the expected cost of using it is lower than the expected cost of remembering. Confidence in own memory is the main input (b07, b08). The bias: people offload even when the unaided option pays more (a13). To implement for an agent:
- Estimate p(correct unaided) from a confidence signal (see 4.4).
- Estimate cost of a read (tokens, latency) and p(note is right).
- Consult when p(unaided correct) is below p(note right) minus a cost margin.
- Keep a fixed margin so the agent does not consult always (human bias) or never.

### 4.3 Trust and the poison problem
ClashEval shows the data: a wrong retrieved note is followed 15.7-31.3% of the time when the model knew the answer, and a right note is ignored 2-4% (d05). Context bias is the bigger risk. Xie et al. show the model follows coherent counter-evidence but under mixed evidence clings to prior belief (d06). Design consequences:
- Do not auto-endorse. Mark each note with source, time, and whether a check passed.
- Notes from checked outputs get higher weight than unchecked notes (d15).
- When two notes conflict, resolve by code (newest verified wins), not by letting the model pick (K28, G5).

### 4.4 Consult gate
Three published gates:
- Token-probability confidence of the model: low confidence means more reliance; calibration lifts accuracy about 14% (d05).
- Popularity of the entity: retrieve only for rare facts; 46.5% on PopQA, 5.3 points above the best fixed policy at about half the cost (d07).
- Trained complexity classifier: none / one-step / multi-step; misroutes 22-47% in some classes (d08).
For our agent the practical gate is the third kind with simple inputs: has a check failed, does a similar item exist in the library, is the model's own answer consistent across short samples.

### 4.5 Memory architectures (what to copy)
- Tiered memory with paging (MemGPT): main context, working context, external store; warn at about 70% of context, flush at 100%, evict about 50% with a recursive summary (c06, c08).
- Memory stream with scoring (Generative Agents): natural-language entries, retrieval by recency, importance and relevance, plus periodic reflection (c09). Typical failure: not retrieving a relevant memory, and inventing details around a real one (c10).
- Episodic reflections (Reflexion): trigger on same action and response more than 3 cycles, or over 30 actions (c12).
- Skill library (Voyager): executable code, verified, indexed by description (c13, c14).
- Linked notes (A-MEM): notes link to each other and rewrite older notes (c22).
- Fact consolidation (Mem0): extract salient facts (c23).
- Curated cheatsheet (Dynamic Cheatsheet): a compact memory the model rewrites after each task (d09).
- Distilled strategies from success and failure (ReasoningBank) (d10).

### 4.6 Note format (K32)
Store raw rounds (not session summaries), add extracted facts as extra index keys, and read back in structured form. JSON plus chain-of-note reading added up to 10 points under perfect retrieval (d13). Replacing text with summaries or facts loses information, except for multi-session reasoning.

### 4.7 Placement
The U shape: information at the start and end of the context is used best, the middle worst (b21, c16). In simple tests this persists to 32K in 2025 models; in harder tests it is swamped by general long-context failure (d16). Keep the notes block short and at the edge.

### 4.8 Scratchpad (K19)
Write intermediate steps to a visible workspace (Nye 2021). This is the clearest case of Wilson's wide computation: the written steps do real work (c15, a07).

## 5. What holds up

### 5.1 Holds
- Offloading is guided by confidence, over-used, and costs later memory for the offloaded items (K06, K07). Several independent labs and registered reports agree (a13, a14, b06-b09).
- Photo-taking impairment replicates in three more experiments (b10, d17).
- Google Stroop priming does not hold (K04). Two separate replications are null (Camerer stage 1 N=104, pooled N=234; Hesselmann BF01=5.07).
- Scratchpad helps (K19). Reflection helps only with an outside signal (K33).
- Long-context reading of a long history is worse than oracle evidence by 30-60% (K14).
- A retrieval gate beats fixed policies (K27).

### 5.2 Failed or weak
- Google Stroop (above). The headline "hard questions prime Internet words" is not to be built on.
- Camerer replicated only Experiment 1 of Sparrow; the other three experiments were not in the project, and no direct replication found (d03).
- The Google effect meta-analysis mixes self-esteem, survey and lab measures; no pooled d in the text; the range and moderators (mobile phone, low prior knowledge) quoted in earlier lines could not be found (d04, K03).
- Vendor memory rankings (Mem0, A-MEM, Zep on LoCoMo) do not hold in the independent benchmark: Mem0 21.1, Zep 24.0, MemGPT 28.3 vs bare model 42.3 and BM25 41.5 (d12). All methods fail multi-hop selective forgetting (at most 28%).
- Reflexion's +8% rests on 100 HotPotQA questions in one paper. Huang 2024 shows no-oracle reflection can fall (26 to 25; 75.8 to 38.1) (d15).
- Kosmyna 2025: preprint, 18 per group, EEG, one source (all lines a23, a24, b22, c27, d01, d02 are the same paper). The group labels were corrected in this pass (d01).
- GPS study: N=50 and a follow-up N=13; fragile.

### 5.3 Moderators
- Offloading: confidence, effort cost, reward (a13, a14, b07, b08).
- Saving benefit: reliable saving and large enough saved content (K05).
- Photos: number of photos (1 photo ns, 5 photos d=0.35) (b10).
- Memory systems: gains scale with task similarity (Pearson 0.717 and 0.563, d11); model size and recurring tasks (d09: GPT-4o full history 6.7 vs baseline 20.0).
- Memory with compute: only strong distilled memories scale with more attempts (d10).
- Reflection: domain (insights for QA, trajectories for embodied action; d14).

### 5.4 Interventions
Worked:
- Paying for performance (reduces offloading bias, does not remove it) (a14).
- Calibrating the model's confidence (d05).
- Adaptive retrieval (d07).
- Curated compact notes (d09, d10).
- Storing facts as extra keys over raw rounds (d13).
- Verified-only skills (c13, c14).
Did not work:
- Unverified self-reflection (d15).
- Full-history append (d09).
- Session-level summaries (d13), event-graph summarization (14% below base on LoCoMo; c19).
- Memory products as a bare layer on a good backbone (d12).

### 5.5 Contradictions reconciled
- Offloading hurts memory for the offloaded item (b06) but frees resources for the next item (Storm and Stone, a12). The reconciliation: harm to the stored item, benefit to the next item.
- Kosmyna (LLM use hurts retention) vs medical-student study (AI-assisted retains more, d18). Different design (tutoring vs essay writing); do not combine.

## 6. Language models

### 6.1 What was done
No study in our evidence tests the extended mind thesis on an LLM as a constitution question. Smart, Clowes and Clark build Digital Andy (gpt-3.5-turbo-1106, 20 queries, 20 paragraph or 5 section chunks, ada-002) and judge it qualitatively, no scores (c01). A persona-only version approached the retrieval versions on some queries (c02): a redundancy warning.

### 6.2 External memory raises task accuracy
- MemGPT: deep memory retrieval GPT-4 32.1 to 92.5 (+60.4 points); GPT-3.5 +28.2; GPT-4 Turbo +58.1 (a26). Fixed-context models hit 0% on nested key-value lookups by one (GPT-3.5) to three (GPT-4) levels, while MemGPT with GPT-4 was unaffected (c07).
- Extended Mind Transformers: at 16k the extended model scores 33.54 vs 17.68 for base; at 2k the base is better (b15).
- Generative Agents: full architecture 29.89 vs 21.21 with none; the human crowd scored 22.95 (a25).
- Reflexion: HumanEval 91.0 vs 80.1; ALFWorld 130/134 in 12 trials (a27).
- Voyager: 3.3x unique items, no-library plateau; self-verification matters most (-73%) (a28, c13).
- Scratchpad: 11 to 26.5 few-shot, 20 to 41.5 fine-tuned (c15).
- ReAct: +34% ALFWorld, +10% WebShop (c24).

### 6.3 Long context is not a substitute
- LongMemEval: reading the whole 115k-token history costs 30-60% against oracle evidence (a29, b20).
- LoCoMo: best model 32.4 vs human 87.9 (b19).
- NoLiMa 2025: GPT-4o 99.3 to 69.7 at 32K; 11 of 13 models below half of base (d16).
- No 2026 frontier model tested for placement (K34).

### 6.4 Do models use or ignore notes
- ClashEval: wrong note followed 15.7%-31.3%; right note ignored 2-4% (d05). Claude Opus had the lowest context bias in that table (0.157), Gemini 1.5 higher (0.245).
- Xie 2024: models follow coherent counter-evidence; under mixed evidence GPT-4 sticks to its prior 80% of the time on popular facts (d06).
- Retrieval hurts on about 10% of PopQA questions, mostly popular entities (d07).
- This is measured for facts, not for agent-written notes.

### 6.5 Memory systems vs plain retrieval
Independent MemoryAgentBench (GPT-4o-mini): BM25 41.5, HippoRAG-v2 41.6, bare model 42.3; MemGPT 28.3, MIRIX 26.2, Zep 24.0, Mem0 21.1, Cognee 20.6, Self-RAG 18.7 (d12). Plain beats fancy here. Vendor claims on LoCoMo are not independent (K21).

### 6.6 Memory against more compute
- Dynamic Cheatsheet vs 3-sample majority vote on Claude 3.5 Sonnet: AIME 2024 50.0 vs 23.3; full-history append 26.7 (d09). Tokens about 1.1x-1.7x, so not an exact match.
- ReasoningBank: memory and compute are complements; 1 to 5 trajectories lifted strong-memory agents 49.7 to 55.1 and left no-memory at about 39-42 (d10).
- Evo-Memory: a plain experience-retrieval baseline is strong across 10 streams; gain tracks task similarity (d11).

### 6.7 Human-side findings about LLM use
Kosmyna (a23): 15/18 LLM users could not quote their own essay vs 2/18 in the other groups. A 2026 medical-student study went the other way (d18). Lee et al. (c28): confidence in AI goes with less critical thinking (snippet only).

### 6.8 Not found
No LLM Google effect study (remember where, not what), no LLM study of reading notes lowering later retention, and no matched cross-session notes-vs-reasoning test (K35).

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. Do not auto-endorse notes. Mark source, time and whether a check passed. Resolve conflicts in code. | memory, G5 | [E] | K22, K06; d05, d06, a03
   - The single-source ClashEval number (15.7-31.3%) sets the size of the risk; the principle that outside text can mislead is established across d05, d06, d07.
2. Consult the note store by a gate, not always and not never. Start with: consult when a check failed or the model is unsure; skip when confident. | G12 spirit, O, memory | [E] for the gate idea | K27, K06; d07, d08, a13, b07, b08
3. Write reflection notes only after an outside check (test, tool output), never from opinion. | G2, memory | [E] | K33; d15, a27
4. Keep notes compact and curated; do not append full history. | memory | [E] on the direction (full-history append is worse than curated or none in d09; long contexts lose 30-60% in a29, b20) | K14, K29
5. Use a scratchpad for multi-step computation. | S3/S4, O | [E] | K19; c15, a07
6. Do not build on Google Stroop priming; do not rely on the Google effect for design. | none | [E] | K04; a10, a11, d03

### Test first

- T1 (K29, K30): notes vs the same tokens on longer reasoning or a vote, on a stream of similar tasks. | memory, G7 | [C] | d09, d10, d11
- T2 (K25, K28): Twin Otto test on our own notes: wrong vs right note, log follow and ignore rates; seed two conflicting notes. | G, memory | [S] | d05, d06, c04
- T3 (K26, K27): confidence-based gate vs always vs never consult. | G, O | [S] | d05, d07
- T4 (K32, K21, K31): note format: raw plus fact keys vs summaries vs linked notes vs verified skills at equal tokens; plain retrieval as the default before any memory product. | memory | [S]/[C] | d13, c22, d12
- T5 (K16, K33): reflection note vs raw trajectory retry, in coding and in QA. | O, memory | [C] | a27, d14, d15
- T6 (K15, K34): note placement start vs middle vs end. | memory | [S] | b21, d16
- T7 (K18): only verified procedures in the library. Consistent with G2/G3 but single-source. | memory, G3 | [S] | c13, c14
- T8 (K07, K35): does reading notes lower the agent's own later retention on unannounced questions? | memory | [S] human-only | b06
- T9 (K03, K35): does telling the agent the store is available lower recall of content and raise recall of keys? | memory | [C] human-only | a19, d04
- T10 (K09, K12): confidence before and after retrieval; does the agent still verify a trusted note? | G | [S] human-only | a17, c28
- T11 (K05): saving block 1 to notes before reading block 2. | memory | [S] human-only | a12

See UNKNOWNS.md for thresholds.

## 8. Concrete tests on our bench

All tests use both arms at equal tokens (count setup, note writing and reading). Use at least 100 items per arm and a fixed seed set, as in our harness; report the paired difference with an interval.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 Notes vs compute | Streams of 30-50 related tasks (math word problems, ARC-like puzzles) in separate sessions | (a) persistent curated notes, (b) same tokens on longer reasoning or extra samples with vote | Accuracy per stream, tokens per correct | Notes win by several points when tasks are similar; no gain on unrelated streams (d11) |
| E2 Twin Otto | Questions with known answer; note injected | (a) right note, (b) wrong note, (c) no note | Follow rate of wrong note, ignore rate of right note | Wrong note followed 15-30% (d05); we want lower with provenance flags |
| E3 Conflict | Two conflicting notes for the same fact | (a) model picks, (b) code picks newest verified | Accuracy | Code pick better; model clings to prior (d06) |
| E4 Gate | Mixed hard and easy items with a notes store | always consult, never consult, confidence gate, check-failed gate | Accuracy and tokens | Gate matches best accuracy at lower tokens (d07: +5.3 points, half cost) |
| E5 Format | Multi-session question set | raw rounds, raw plus fact keys, session summaries, linked notes | Recall@k, answer accuracy | Raw plus keys best (+9.4 recall, +5.4 accuracy; d13) |
| E6 Reflection | Coding and QA tasks with and without test feedback | reflection note, raw trajectory, nothing | Pass rate on retry | Reflection helps only with the outside signal (d15); trajectory better on embodied-style tasks (d14) |
| E7 Placement | Same note at start, middle, end of prompt | three placements | Accuracy | End or start better than middle; effect small at short length (d16) |
| E8 Retention | Agent reads notes, then an unannounced follow-up that needs the same content | reads notes, solves from memory | Follow-up accuracy | Possible drop for note readers (b06 in humans); untested in LLMs |
| E9 Where not what | Tell agent a store will exist vs not | with notice, without | Recall of content, recall of keys | Unknown; human effect contested (d04) |
| E10 Verified-only library | Repeated procedure tasks | store verified only, store all | Success on reuse | Verified-only better (c13: -73% without verification) |

## 9. What does not transfer, and why

- The metaphysical debate (constitution vs embedding): no testable difference for the agent; skip (K02).
- Google Stroop priming: a priming effect of a human lexical network; failed to replicate even in humans (K04).
- Photo-taking impairment, GPS atrophy: depend on human attention and encoding; the model has no encoding that changes when it writes a note. The skill-atrophy risk applies only if we fine-tune, which we do not (K08, K10).
- Self-rated knowledge inflation (Fisher): the human feeling of knowing; the agent analogue is overconfidence after retrieval, which must be measured, not assumed (K09).
- EEG connectivity (Kosmyna): no analogue in a prompt-only agent. Only the lesson on outsourced encoding survives, as a caution (K11).
- Ageing and Alzheimer's framing (Otto): our agent's "memory" is a fresh context each call. Condition 1 (constant) is by construction.
- Vendor memory numbers: not independent (K21).
- The human offloading bias comes from effort avoidance and confidence; the model has no effort, so the bias may point either way. It needs a direct measure.

## 10. Open questions

1. Does notes-vs-equal-reasoning hold across separate sessions? (Gap 1, partly closed with d09, d10.)
2. Does the agent follow a wrong note of its own writing? ClashEval covers facts only.
3. Does a verbal-confidence gate work as well as token probabilities, which many APIs hide?
4. Which note format wins at equal tokens when Voyager-style skills are included?
5. Does reading notes cost later reasoning in LLMs?
6. Where to place notes with 2026 frontier models?
7. Does reflection beat raw trajectory outside coding and HotPotQA?
8. Does the Google pattern (where, not what) appear in LLMs?
9. Does anyone replicate Sparrow's Experiments 2-4?
10. The Google meta-analysis d range and moderators: where did they come from?
11. Voyager's 3.3x and 15.3x ratios are not located in the text.
12. Is the ClashEval ">60%" abstract figure for some condition we have not seen? Tables show 15.7-31.3%.
13. Is there a peer-reviewed or larger replication of Kosmyna?

## 11. Sources

[V] opened, [M] snippet only.

- [V] Clark and Chalmers (1998) The Extended Mind. https://consc.net/papers/extended.html (a01-a04)
- [M] Clark (2008) Supersizing the Mind; Adams and Aizawa (2001, 2008); Rupert (2004) as cited on SEP/Wikipedia (b12, b13)
- [V] Wilson and Foglia, Embodied Cognition, SEP. https://plato.stanford.edu/entries/embodied-cognition/ (a05-a07, b01, b26)
- [V] Wikipedia, Extended mind thesis. https://en.wikipedia.org/wiki/Extended_mind_thesis (a08)
- [V] Sparrow, Liu and Wegner (2011) Google effects on memory. https://pubmed.ncbi.nlm.nih.gov/21764755/ (a09); [M] Science page https://www.science.org/doi/10.1126/science.1207745 (b05)
- [V] Camerer et al. (2018) Nature Human Behaviour. https://www.nature.com/articles/s41562-018-0399-z (a10); [M] second fetch (b03)
- [V] Hesselmann (2020) PeerJ. https://pmc.ncbi.nlm.nih.gov/articles/PMC7651475/ (a11, b04, d03)
- [V] Storm and Stone (2015). https://pubmed.ncbi.nlm.nih.gov/25491269/ (a12); [M] https://doi.org/10.1177/0956797614563341 (b23)
- [V] Gilbert et al. (2020). https://pubmed.ncbi.nlm.nih.gov/31448938/ (a13)
- [V] Sachdeva and Gilbert (2020). https://pubmed.ncbi.nlm.nih.gov/33032027/ (a14)
- [V] Risko and Gilbert (2016). https://pubmed.ncbi.nlm.nih.gov/27542527/ (a15); [M] https://doi.org/10.1016/j.tics.2016.07.002 (b25)
- [V] Metacognitive account of offloading (2015). https://pubmed.ncbi.nlm.nih.gov/26306555/ (a16)
- [V] Fisher, Goddu and Keil (2015). https://pubmed.ncbi.nlm.nih.gov/25822461/ (a17); [M] https://doi.org/10.1037/xge0000070 (b24)
- [V] Dahmani and Bohbot (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7156656/ (a18)
- [V] Gong and Yang (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC10830778/ (a19, b02, d04)
- [V] Grinschgl and Neubauer (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9329671/ (a20)
- [V] Clark (2025) Nature Communications. https://www.nature.com/articles/s41467-025-59906-9 (a21, a22, c05)
- [V] Kosmyna et al. (2025). https://arxiv.org/abs/2506.08872 (a23, a24, b22, c27, d01, d02)
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (a25, b17, c09, c10)
- [V] Packer et al. (2023) MemGPT. https://arxiv.org/abs/2310.08560 (a26, b14, c06-c08)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (a27, b16, c11, c12)
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 (a28, b18, c13, c14)
- [V] Wu et al. (2025) LongMemEval. https://arxiv.org/abs/2410.10813 (a29, b20, c20, c21, d13)
- [V] Direct input variables, predictive processing. https://pmc.ncbi.nlm.nih.gov/articles/PMC13680224/ (a30)
- [V] Grinschgl, Papenmeier and Meyerhoff (2021). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8358584/ (b06)
- [V] Hu, Luo and Fleming (2019). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6838677/ (b07)
- [V] Confidence guides offloading. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6889107/ (b08)
- [V] Individual differences in offloading. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6942100/ (b09)
- [V] Photo-taking impairment. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9296013/ (b10)
- [V] Nijssen et al. (2018). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6118357/ (b11)
- [V] Klett and Ahle (2024) Extended Mind Transformers. https://arxiv.org/abs/2406.02332 (b15)
- [V] Maharana et al. (2024) LoCoMo. https://arxiv.org/abs/2402.17753 (b19, c18, c19)
- [V] Liu et al. (2023) Lost in the Middle. https://arxiv.org/abs/2307.03172 (b21, c16, c17)
- [V] Smart, Clowes and Clark (2025). https://eprints.soton.ac.uk/502110/1/s11229-025-05046-y (c01-c04)
- [V] Nye et al. (2021) Scratchpads. https://arxiv.org/abs/2112.00114 (c15)
- [V] Xu et al. (2025) A-MEM. https://arxiv.org/abs/2502.12110 (c22)
- [V] Chhikara et al. (2025) Mem0. https://arxiv.org/abs/2504.19413 (c23)
- [V] Yao et al. (2023) ReAct. https://arxiv.org/abs/2210.03629 (c24)
- [V] Schick et al. (2023) Toolformer. https://arxiv.org/abs/2302.04761 (c25)
- [V] Sumers et al. (2024) CoALA. https://arxiv.org/abs/2309.02427 (c26)
- [M] Lee et al. (2025) Impact of Generative AI on Critical Thinking, Microsoft Research (c28)
- [V] Wu, Wu and Zou (2024) ClashEval. https://arxiv.org/abs/2404.10198 (d05)
- [V] Xie et al. (2024) Adaptive Chameleon or Stubborn Sloth. https://arxiv.org/abs/2305.13300 (d06)
- [V] Mallen et al. (2023) When Not to Trust Language Models. https://arxiv.org/abs/2212.10511 (d07)
- [V] Jeong et al. (2024) Adaptive-RAG. https://arxiv.org/abs/2403.14403 (d08)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (d09)
- [V] Ouyang et al. (2026) ReasoningBank. https://arxiv.org/abs/2509.25140 (d10)
- [V] Wei et al. (2026) Evo-Memory. https://arxiv.org/abs/2511.20857 (d11)
- [V] Hu, Wang and McAuley (2026) MemoryAgentBench. https://arxiv.org/abs/2507.05257 (d12)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (d14)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d15)
- [V] Modarressi et al. (2025) NoLiMa. https://arxiv.org/abs/2502.05167 (d16)
- [V] Lurie, Fabrizio and Westerman (2025) cost of saving photos. https://pmc.ncbi.nlm.nih.gov/articles/PMC13332969/ (d17)
- [V] Cureus (2026) AI-assisted vs traditional learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC13561434/ (d18)
