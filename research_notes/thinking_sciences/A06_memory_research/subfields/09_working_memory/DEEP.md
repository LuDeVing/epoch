# Working memory: deep document

*Subfield A06.09. Short-term store and control. Evidence ids (a01 to d17) point to evidence_a-d.jsonl; claim ids (A06.09-K01 to K32, written K01 to K32) point to claims.jsonl. Cross-check notes are in critique.md. Related subfields researched in parallel and not covered here: Cognitive conflict and impasse, Global workspace theory, ACT-R declarative memory, Retrieval-induced forgetting, Calibration and overconfidence, Search over thoughts. Earlier series work on capacity and chunking: A08/08_working_memory_limits_and_chunking.*

## 1. What it is

Working memory is the small set of information a mind keeps active while it works on something. It is not long-term memory, and it is not short-term storage alone. The core question since 1974: does the same limited resource that holds a few items also run thinking?

Three ideas matter for our agent.

1. **A small active set.** Humans hold about 3 to 5 chunks when they cannot rehearse or regroup (a06, b18). The older figure of 7 came from rehearsal and recoding (a01, a02).
2. **Control, not just storage.** Individual differences and dual-task costs point at attention control: keep the goal, block look-alike items, select the one item needed (a04, a13, a26).
3. **Forgetting by interference.** Humans forget in working memory mostly because items compete and unwanted items must be removed (b22, b23). Time-based decay is contested (a05).

An LLM has a different setup. Its context holds all text with no decay. Yet it fails like a human when many similar or stale items compete (a18, a20, c07). So the useful carry-over is the interference and control side, not the slot count. The model's only working state is written tokens (d05).

## 2. History and theories in depth

**Miller 1956 (a01, a02).** Miller split two limits. Absolute judgment on one dimension is limited by information: mean 2.6 bits (SD 0.6), about 3 to 15 categories (pitch 2.5 bits, loudness 2.3, salt 1.9, position 3.2 to 3.9). Immediate memory is limited by item count, about 7 digits (about 3.3 bits each). Span differs by item type: binary digits about 9, monosyllabic words about 5. Recoding raised span: Smith recalled 12 octal digits after drilling, up to about 40 binary digits. Miller doubted the number 7 himself. Smith's subjects were drilled and included the author.

**Modal model and its critics (b24).** Atkinson and Shiffrin (1968, over 10,000 citations by 2018) set a separate short-term store feeding long-term memory. Baddeley, Hitch and Allen (2019) defend a separate store with patients who have grossly impaired long-term memory but intact short-term memory, and the reverse. Cowan's alternative treats short-term memory as activated long-term memory. The rivals do not predict clearly different agent designs.

**Baddeley and Hitch 1974 (a03, a04).** They asked whether the resources behind span also serve general thinking. They loaded healthy adults with irrelevant items to mimic a span-deficit patient, then tested reasoning, prose comprehension and free recall. Result: moderate but far from catastrophic interference when the load was at span; little or none when well below. They proposed a limited-capacity central executive plus an articulatory loop, later a visuospatial sketchpad and (2000) an episodic buffer that binds information across domains (a24, secondary source). Critics called the executive a homunculus. Early dual-task work gave little support for a processing-versus-storage trade-off inside it. Norman and Shallice's supervisory attentional system fits better: control engages only when automatic selection fails (a04). This matches schema G1. The loop's time decay is contested: word-length effects are disputed, and Oberauer and Lewandowsky (2008) cast doubt on trace decay (a05). Caveat: this comes from the founders' own 50-year review, not the 1974 chapter (its scan had no text layer).

**Daneman and Carpenter 1980 (a25, not opened).** Reading span (hold final words while reading sentences) predicted comprehension better than digit span. Correlations not read. Engle's executive-attention view (a26, not opened): capacity differences reflect control of attention, not store size.

**Cowan 1988 and 2001 (a06 to a11).** With chunking and rehearsal blocked, capacity is about 4 chunks (range 3 to 5), held in the focus of attention inside activated long-term memory. Evidence from the 2001 review text:
- Ignored speech with surprise recall (Cowan et al. 1999): adults 3.51 (SD 0.94, N=35), grade 4 2.99 (N=26), grade 1 2.34 (N=24); attended 5.43, 4.31, 3.48. Individual adult capacity about 2 to almost 6. Flat across list length.
- Luck and Vogel 1997 change detection: 1 to 12 coloured squares, 100 ms display, 900 ms blank. Near perfect at 1 to 3, slightly worse at 4, much worse above. Objects with 4 features were kept as well as objects with 1 feature.
- Subitizing (Mandler and Shebo 1982): near-zero errors for 1 to 4 items, then about +15% errors per added item to near 100% at 11.
- Free-recall recency: Watkins 1974 estimates 2.21 to 3.43. Delayed recency of 3 to 5 items after up to 42 s of arithmetic (Bjork and Whitten 1974) is a known problem for a pure store.
- A commentary using speed-accuracy data (Wickelgren 1980; McElree and Dosher): only the last item retrieves 50% faster, so focal attention may hold one item (a11).

Limits: 4 is a mean, not a constant. Estimates are "compound" (larger) when item associations help. Many commentators challenged the number.

**Slots versus resource (a12, b19 to b21).** Discrete-slot models: an object gets a slot with good precision or nothing. Flexible-resource models: a continuous resource divides across objects, so more objects mean lower precision each. Rouder et al. 2008 (N=23, set sizes 2, 5, 8): ROC lines had slope 1.0, as all-or-none slots predict, and the fixed-capacity model beat variable-capacity rivals. They also note that a capacity asymptote at 3 to 4 items can be mimicked by models without fixed capacity. Ma, Husain and Bays (2014) argue for variable precision and warn that slot summary numbers (K, guess rate) mislead when the model fits poorly. Souza et al. 2014 (a13): both families fit only when extended with graded transposition errors. Status: contested (K03).

**Interference and removal (b22, b23, d16, d17).** Lewandowsky, Geiger and Oberauer (2008), four experiments: forgetting depends on how many different distractors are spoken, not on time. Repeating one distractor caused no forgetting. Three-way interaction F(1,22)=5.3, p=.03, partial eta-squared .19. Oberauer et al. 2012 SOB-CS: a two-layer network with overlapping position markers reproduces complex-span benchmarks through interference. Free time between distractors is used to remove their traces, 1 to 2 s each (rate 1.5); refreshing is not needed. The rival TBRS (Barrouillet, Bernardin and Camos 2004; 7 experiments; a27, d14): span depends on cognitive load, retrieval time over total time, with traces decaying when attention is elsewhere. Newer: the refresh boost depends on the number of refreshing steps, not duration (Vergauwe et al. 2025, d15). Removal (Dames et al. 2025, n=219 and 241): delayed removal lowers memory for the removed item but does not help the others; immediate removal helps later encoding (d16). Removed words are later remembered worse, and people cannot remove from working memory while keeping in long-term memory (d17).

**Dual-task resource sharing (d13).** Pougeon, Camos, Belletier and Barrouillet (2024), Exp 1, N=24: single span 6.42 letters [5.90, 6.93]; processing span 5.88 digits. In the dual task, memory accuracy fell .88 to .66 and processing .83 to .58. Combined retained performance 124% [114, 134]. With articulatory suppression: memory span 3.77, storage 45%, processing 61%, combined 107% [101, 112]. A second duty costs part of each task, not all. The sum above 100% fits neither pure sharing nor pure time sharing.

**Training (b13 to b17, b26).** See section 5.

## 3. Core findings with exact numbers

Status key: Est = established (two or more independent sources), Single = one source, Contested = sources disagree. "Human" = human data only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Absolute judgment limit by information | mean 2.6 bits (SD 0.6); 3 to 15 categories | Miller 1956 (a01) | Est, human |
| Span depends on item type; recoding raises span | binary 9, words 5; octal 7 to 12 after drilling, up to about 40 binary digits | Miller 1956 (a02) | Est, human |
| Pure capacity about 4 chunks (3 to 5) | ignored-speech adults 3.51 (SD 0.94, N=35); individuals 2 to almost 6; attended 5.43 | Cowan 2001 (a06, a07, b18) | Est, human |
| Change-detection limit is by objects, not features | near perfect 1 to 3, worse at 4; 4-feature objects = 1-feature objects | Luck and Vogel via Cowan (a08) | Est, human |
| Subitizing break near 4 | about +15% errors per item from 4 to 11 | Mandler and Shebo via Cowan (a09) | Est, human |
| Slots versus resource | ROC slope 1.0 (N=23); variable precision fits localisation data | Rouder 2008; Ma 2014 (b19, b21) | Contested |
| Focusing attention on one item helps | fewer guesses and transpositions; Exp 1 N=16, Exp 2 N=21 analysed | Souza et al. 2014 (a13) | Est, human |
| Forgetting is by interference | F(1,22)=5.3, p=.03; removal 1 to 2 s | Lewandowsky 2008; Oberauer 2012 (b22, b23) | Est, human |
| Delayed removal costs the removed item, no benefit to others | n=219, n=241 | Dames et al. 2025 (d16) | Single, human |
| Dual-task retained performance | 124% combined (66% storage, 58% processing); 107% under suppression | Pougeon et al. 2024 (d13) | Single, human |
| Full short-term load slows reasoning only moderately | "moderate but far from catastrophic" at span; little below span | Baddeley and Hitch 1974 via 2024 review (a03) | Est, human, secondary |
| ChatGPT n-back d' falls to about 1 at n=3 | 50 blocks per n, 24 trials (8 match), temperature 1; noise symbols lower capacity | Gong, Wan, Wang 2024 (a14, c01) | Est (with 2026 work) |
| Median d' across 15 open LLMs by N | 2.57 at N=1, 0.91 at N=4, 0.52 at N=6; Qwen2.5-14B 4.28 to 1.15 | Gong 2026 (c07) | Est |
| Scale does not remove the n-back limit | Llama-3.1-70B-Instruct 0.99 at 2-back, 0.62 (SD .31) at 3-back; Gemma-2-27B 0.61, 0.31 | Hu and Lewis 2025 (b04) | Est |
| Errors are lure errors | 79% match responses to N-1 lures vs 4% to other non-matches (N=2); heads off target on only 16%, 7%, 8% of misses at N=2, 3, 4 | Gong 2026 (c07) | Est (3 sources) |
| Readout bottleneck | probes decode target vs lure near perfectly; sharpening attention negligible | Gong 2026; Xiong 2026 (b06, c08) | Single |
| Distractor suppression gain shrinks on held-out data | +0.44 d' at N=4 (43 cells) vs +0.11 for earlier single-direction removal; random subspace -0.03; removing the target -1.54 | Gong 2026; Xiong 2026 (c08, c25) | Contested |
| n-back tracks benchmarks across 10 models | MMLU-Pro .78/.70, GPQA .88/.72, IFEval .69/.82; log parameters not predictive | Xiong 2026 (a19) | Contested (d08) |
| n-back is not a separate factor across 54 models | PC2 gain 3.17% [-1.53, 15.73]; construct groups vs random -2.02% [-5.10, .48] | Hou et al. 2026 (d08) | Single |
| Lure false alarms across families | ordinary non-target false alarms +.257 [.159, .341] over humans; only 3 of 32 gate-passers reach balanced accuracy .80, all thinking models | Hou et al. 2026 (d07) | Single |
| Task misunderstanding contributes | tiers T1 above 80%, T2 about 50%/40%, T3 below 20% on 2/3-back; Qwen-1.5-14B failed to get 2 correct in a row after 10 demos | Hu and Lewis 2025 (b04, c04) | Single |
| Demo ladder lifts large n | n=8, 9, 10: task accuracy 90.08, 90.08, 84.75%; retrieval 79.83, 80.17, 71.67% (no ladder: 75.25, 66.08, 57.1%) | Hu and Lewis 2025 (b05, c05) | Single |
| Proactive interference: latest-value retrieval falls log-linearly with updates | 46 keys, 3 to 400 updates, 30 models; size t=3.03, p=.005, R2=.261, rho=.673 (p=.0016, N=19); context length t=-0.144, p=.886 | Wang and Sun 2025 (a20, b08) | Single |
| "Forget the old values" prompts barely help | under 10 pp at 100 updates; relevance meta-prompt negative for gpt-4.1-mini | Wang and Sun 2025 (d01) | Single |
| Hidden state fails without written tokens | yes-no game, 60 objects: GPT-4o-mini 0% pass, GPT-4o 13.5%; CoT lifts base models to 10 to 30%; reasoning models 36 to 100% | Huang et al. 2026 (a22, d05) | Single |
| Cumulative state tracking without written steps | core 31.7% vs single-step 84.9%; K=3 44.4% to K=100 0.8%; with written steps 88.0%; assignment 90.0% vs sets and counts 54.1% | WMIP 2026 (c17, c18) | Single |
| External symbolic memory beats scratchpad | CLUTRR 92.34 vs 83.83 (GPT-4); AR-LSAT 70.00 vs 41.25; ProofWriter 77.33 vs 61.33 | Wang et al. 2024 (c19) | Est with c20 |
| Explicit memory units help factuality | VeriScore +2 to +6 points on four datasets (Llama-3.1 70B) | Zhang et al. 2024 (c20) | Single |
| Distractor share hurts retrieval | up to 24% accuracy lift from medoid voting; share 0 to 100% | Dsouza et al. 2024 (c16, c26) | Est |
| Entity removal inside the model is fragile | degeneration, no-op remove 0.84 (13B) / 0.49 (70B); shared labels 0.56/0.27; re-introduction 0.62/0.01 | Tang et al. 2026 (d12) | Single |
| Executive control is weak | Wisconsin card sort 0.29 (Llama3.1-8B), 0.49 (70B), 0.53 (Qwen2-7B), 0.50 (Qwen2-72B) vs human 0.70 to 0.80 | Strong Memory, Weak Control 2025 (b10) | Single |
| Multi-agent load splitting at matched tokens | 260 configs; +80.8% to -70.0%; mean -0.3% (CI -58.7 to +77.2); SWE-bench -2.1% to -14.9% | Kim et al. 2026 (d10, d11) | Est |
| Dual-task cost small for reasoning models | plausibility gap 0.064 dual vs 0.025 single; o3-mini, o4-mini near 100% | Emura and Sugawara 2026 (d09) | Single |
| Text beats images for spatial n-back | LLM text > VLM text > VLM vision; 3x3 grids collapse (over half of blocks 0% match responses) | Liang et al. 2026 (b11, c10) | Est |
| WM training, near transfer | untrained n-back g=0.62 [0.44, 0.81]; other WM tasks g=0.24 [0.16, 0.32]; children g=0.46 [0.35, 0.57] | Soveri 2017; Sala and Gobet 2017 (b13, b16) | Contested |
| WM training, far transfer | cognitive control g=0.16 [0.05, 0.27]; fluid intelligence g=0.16 [0.08, 0.24]; children g=0.12 [0.06, 0.18]; randomised with active control g=0.03 [-0.07, 0.14] (k=34) | Soveri; Sala and Gobet (b13, b17) | Contested |

## 4. Mechanisms and models

Written so an engineer could implement or test each one.

**4.1 Chunk-limited active set (Cowan).** State: one focus item, plus at most about 4 chunks immediately available, plus long-term store. Agent version: the working block in the prompt holds 3 to 5 named units. Group related fields into one record (a08: 4-feature objects cost no more than 1-feature objects). Everything else lives in code-held storage and is pulled in on demand. This is a human number. Hu and Lewis reach 10-back with a demo ladder (b05), so the LLM limit is not fixed at 4.

**4.2 Interference model (SOB-CS style, Oberauer).** Items are bound to overlapping position markers. Each new item adds interference to older bindings. Free time removes distractor bindings at 1 to 2 s each. Agent analogue: the number of look-alike items visible in the prompt is the driver. Cut it by deleting superseded values, not by adding text that says "ignore". Evidence: PI-LLM (a20), n-back lure rate (c07), noise symbols (c02).

**4.3 Executive control as selection.** The 2026 LLM papers frame capacity as "the ability to select task-relevant information under interference" (a18). A step that restates the one item needed before answering is a refocus (a13, d15). Refresh count is the lever, not time. Implementation: before each answer, the program asks the model to quote the one record it will use, then checks the quote against the code-held state by exact match.

**4.4 Readout bottleneck in LLMs (c07, c08, b06).** The needed item is decodable by linear probe and attention usually lands on it, yet the answer is wrong. Suppressing the letter identity of non-targets in the residual stream raises d' by +0.44 at N=4 when tuned on calibration data. This is a mechanism claim on 70M to 14B open models and cannot be run from a prompt. Use it as an explanation for why clean prompts help.

**4.5 Written trace as the only working state (d05, a22, c17).** Models do not keep hidden variables latently. Entity tracking gathers information at the last token rather than updating step by step (d12). So every live variable must be rewritten into visible text each step. Implementation: the program holds a state object (JSON). Each model call receives the full current state and returns the full new state. Code diffs, validates and stores it. In WMIP the write-steps instruction gave most of the lift (the larger budget added 195 correct, the instructions 400 more).

**4.6 Overwrite versus tag-remove.** Inside the model, deletion is a global remove tag that weakens as operations accumulate (d12). Humans pay a removal cost that gets worse when delayed (d16). Design: replace the old value in the state and drop it from the prompt entirely. Keep it in a separate log, outside the working block, if it may be needed later (d17). A restated current-state block with a closed batch boundary (the Mock-QA reset, d02) helps partly and is a cheaper fallback.

**4.7 External symbolic memory (c19).** Facts and rules are stored in natural language and symbols. Code finds applicable rules each step and the model applies them. This beat scratchpad CoT on CLUTRR, ProofWriter and AR-LSAT. It is the nearest published match to our program-holds-state design.

**4.8 Time-based resource sharing (TBRS).** Cognitive load = retrieval time over total time. An LLM has no decay and no clock, so TBRS maps only to per-step token load. Do not implement timing.

## 5. What holds up

**Replicated and stable**
- A capacity near 3 to 5 chunks under blocked rehearsal (Cowan, several paradigms), with the exact number depending on the data model (b20, b21).
- Chunking and recoding raise effective span (Miller, Smith; Cowan 2010: 3 to 4 chunks of idioms or short sentences, b18).
- Interference over decay as the main source of verbal forgetting (b22, b23). TBRS proponents disagree (a05, d14).
- LLM n-back decline with N in several independent groups: Gong 2024, Hu and Lewis 2025, Gong 2026, Xiong 2026 (K07). Lure dominance in three (K09).
- LLMs track written state far better than hidden state (a22, c17, d05, c19).
- Multi-agent splitting at equal tokens is no general win (d10, d11).

**Failed, shrunk or contested**
- The n=3 "human-like capacity" in LLMs: a demo ladder takes Llama-3.1-70B to 10-back (b05). Hu and Lewis say part of the weak-model failure is task comprehension. Yet the applied rule differs from the instructed N in only 14 of 90 cases for small models at N of 4 or more (c22).
- Suppression gain: +0.44 d' tuned on calibration data; the first single-direction result shrank to about a fifth (+0.11) on held-out data (K11).
- n-back as a predictor of reasoning: 10 models give r .70 to .88 on benchmarks (a19), but 54 models show one shared scale dimension and no working-memory-specific factor (d08). Compute was not controlled. The human range r=.31 to .78 quoted in a19 is a human figure, not an LLM result (critique note 1).
- Cowan's 4 is contested by the one-item focus view (a11) and by resource models (b21).
- The spatial grid-size effect in Gong 2024 is the authors' guess with no human control (a15).

**Moderators**
- Model size: size class predicts PI resistance (t=3.03, p=.005, N=30); context window does not (p=.886) (a20). Larger small-trained models stay above 95% on n-back (a17).
- Stimulus set size and lure probability (lures r=-.51/-.32, set size r=-.30/-.26; a18). Grid size changes lure density (c11).
- Modality: text beats image rendering (b11).
- Prompting: demo ladder helps (c05). Chain of thought partly lifts n-back but leaves the limit (a15, c24). Small models do better with short answer-only prompts than with heavy scaffolds (c15, c23). Natural-language forget instructions give under 10 pp (d01).
- Reasoning models: success on hidden-variable tasks comes only through the trace (d05). Only 3 of 32 gate-passers reach .80 on n-back, all thinking models (d07).

**Training interventions (humans)**
- n-back training (Soveri, 33 randomised trials, 2,105 people, b13): g=0.62 on untrained n-back, 0.24 other WM, 0.16 control, 0.16 fluid intelligence. No effect of dose g=0.01, single vs dual g=0.06, active vs passive control g=0.09 (b14).
- Au et al. g=0.24 versus Melby-Lervag and Hulme 0.13 on the same trials: coding choices decide the answer (b15).
- Children: near transfer 0.46, far 0.12. Randomised with active control: far 0.03 (b17).
- Redick et al. 2013, placebo-controlled: gains on trained tasks, no intelligence gain. Not opened (b26).
- Verdict: contested; training does not generalise. In-context practice should not be expected to either.

## 6. Language models

**n-back (letters).**
- ChatGPT (gpt-3.5): d' about 1 at n=3 in three of four verbal variants; noise lowers capacity; feedback and CoT do not remove the drop (a14, c24). GPT-4 above GPT-3.5 (Kruskal-Wallis H=58.5, p=3.95e-12, effect 0.65; tested to n=3 only). Open 6 to 13B models sit at a floor (a16, c03).
- Fifteen open LLMs, 70M to 14B (Gong 2026): median d' 2.57, 0.91, 0.52 at N=1, 4, 6. Qwen2.5-14B 4.28 to 1.15. Errors concentrate on N-1 lures (79% vs 4%). Attention is off target on 16%, 7%, 8% of misses at N=2, 3, 4.
- Llama-3.1-70B-Instruct: 0.99 at 2-back, 0.62 at 3-back. With a demo ladder, 84.75 to 90.08% task accuracy at n=8 to 10 (b05).
- Fifty-four open models (CogBattery): lure false alarms +.257 over humans; three thinking models reach .80 (d07).
- Small trained transformers: 1 layer 1 head declines log-like with N (H=38.517, eta2 .248); larger ones stay above 95% (a17).
- VLMs: text beats image; nominal 2- and 3-back often become recency-locked 1-back; AUC at the instructed lag near 50% (c10).

**Proactive interference (PI-LLM).** 30 models. Accuracy falls log-linearly with the number of earlier values per key. llama4-maverick is near 100% at few keys but about 5% at 46 keys (c12). The dataset authors state without numbers that GPT-5, Grok-4 and Gemini 2.5 Pro decline too (d04). Reasoning models were left out of the regression for latency (d03). This is the biggest gap for 2026 frontier models.

**Hidden state.** GPT-4o-mini passes 0% of 60-object game trials, GPT-4o 13.5% (a22). Hidden-variable persistence under CoT: 3.3% (GPT-4o-mini) to 32.7% (Qwen2.5-7B); reasoning models 36.0 to 100%, with the mapping to model names not fully verified (d05). Many correct answers are the number 7 (66.7% for o1-mini).

**Cumulative state tracking (WMIP).** 18 LLMs. Core 31.7% vs 84.9% single step. K=3 44.4% falling to K=100 0.8%. Written steps 88.0%. Assignment state 90.0% but sets and counts 54.1%; meeting counts 34.1%, inventory 64.6% (c17, c18).

**What changed the outcome, and by how much**

| Change | Effect | Source |
|---|---|---|
| Write steps at each update | 31.7% to 88.0% | c17 |
| External symbolic store vs scratchpad | +8.5 (CLUTRR, GPT-4) and +28.8 (AR-LSAT, GPT-4) points | c19 |
| Demo ladder | retrieval 57.1% to 71.67% at n=10; task accuracy 84.75% | b05, c05 |
| Explicit memory units | +2 to +6 VeriScore | c20 |
| Natural-language "forget" | under 10 pp | d01 |
| Chain of thought on n-back | partial; limit remains | a15 |
| Residual-stream suppression | +0.44 d' (calibration), +0.11 (earlier method, held-out) | c08 |
| Bigger model | helps PI and n-back, but 14B still drops 4.28 to 1.15 | a20, c07 |
| Multi-agent split at equal tokens | mean -0.3%, range +80.8% to -70.0% | d10 |
| Cleaner input (less distractor share) | up to 24% accuracy lift via medoid voting | c16 |

**Dual-task and control.** Reasoning models lose little under a parallel arithmetic duty (d09). Executive tasks lag humans: Wisconsin card sorting 0.29 to 0.53 vs 0.70 to 0.80 (b10). Span (store) beats humans but does not predict executive scores.

**Position papers.** Mapping Baddeley's model onto agents (c21) has no experiments. CoThinker (b12) reports gains from load splitting on high-load tasks; exact gains not extracted.

## 7. What our agent should take

Status codes: [E] established, [S] single-source, [C] contested. Part codes: G guardrail, S state, O operator, memory = schema section 5.

### Add now (established)

1. **Keep the live reasoning state small and in code, about 3 to 5 named units per step.** Part: G/memory. [E] (K01; a06, a07, a08, b18). A design budget from human data, not a proven LLM limit; Hu and Lewis reach 10-back with a ladder (b05).
2. **Group related fields into one record.** Part: S2/memory. [E] human (K02; a02, a06, a08). The agent-level gain from chunk rewriting is untested (U1).
3. **Hold state as written text in a program-owned object; the model rewrites it each step.** Part: G/S. [E] direction (K15, K16, K17, K27; a22, c17, c19, d05). The exact lift is single-source.
4. **Do not rely on the model to ignore stale content. Remove superseded values from the visible state in code.** Part: G/O/memory. [E] direction (K04, K09, K13, K14, K25; a20, b09, c07, d01). Overwrite versus append is untested at equal tokens (U2).
5. **Keep distractors and near-duplicates out of the working prompt.** Part: G/memory. [E] (K09, K18; a18, c02, c07, c16, c26).
6. **Give each tracked variable a distinct label format; do counts and set membership in code.** Part: G/S. [E] direction (a15, c18). Counting in code already fits schema section 1.
7. **Retire a value when it is replaced, not in a later clean-up pass; archive it if it may be needed.** Part: O/memory. [E] human only (K29; d16, d17).
8. **Do not add any WM drill or n-back practice.** Part: none (add to 4b). [C] (K06; b13 to b17). No transfer expected.
9. **Use a second agent only for decomposable parts.** Part: none. [E] (K23; d10, d11). Fits G9.
10. **Keep state in text, not images.** Part: S. [E] (K19; b11, c10, c11).

### Test first

11. **Focus step: before answering, quote the one record needed.** Part: O. [E] human, [S] LLM (K05; a13, d15). U3.
12. **Write full state each update at equal tokens on our own tasks.** Part: G/S. [S] (K16; c17, c18). U4.
13. **Overwrite-in-place versus append-only versus restated current-state block.** Part: memory/O. [S] (K13, K25, K28; a20, d02, d12). U2, U12, U13.
14. **Demo ladder before any lag or rule-tracking item.** Part: S1. [S] (K08; b05, c05). U5.
15. **A lure n-back probe as a gate for model choice.** Part: S0. [C] (K12, K32; a19, d07, d08). U6.
16. **Check the model applies the instructed rule before reading a failure as a memory limit.** Part: G/S0. [S] (c04, c22). U7.
17. **Measure agent-level span (live variables before accuracy falls).** Part: G. [S] (K13; c12). U8.
18. **Match scaffold weight to model size.** Part: G7. [S] (c15, c23). U9.
19. **Dual-duty cost of carrying a state block.** Part: G7. [S] (K30, K31; d09, d13). U10.
20. **Place the item needed next at the prompt edges.** Part: memory. [S] (c16). U11.
21. **Chunk renaming (group items under one label) to raise span.** Part: S2. [E] human, no LLM test (K02). U1.

## 8. Concrete tests on our bench

Both arms use equal total tokens, hidden reasoning included. Same items and seeds, 3 or more repeats.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Key-value update stream, 46 keys, 3 to 400 updates per key, last value asked | A append-only note; B overwrite-in-place state; C append plus "ignore old" line; D restated current-state block | Last-value accuracy vs log updates; slope; accuracy at 100 updates | B flat; A and C decline log-linearly; D between. B over A by more than 20 pp at 100 updates |
| T2 | Cumulative state tracking, K=3 to 100 updates (WMIP style) plus our own bench items | A hidden budget; B write full state after each update | Final-state accuracy by K; tokens used | B at least 30 pp over A at K of 20 or more; check the gain holds on non-arithmetic items |
| T3 | Multi-step tasks needing one of several stored facts | A no restatement; B quote the needed record, code verifies exact match | Accuracy; wrong-record errors | Wrong-record errors down 20% relative |
| T4 | Tracking 4, 8, 16 live variables across 20 steps | A raw history; B per-step named-chunk state | Accuracy vs number of variables | A drops from about 4 variables; B drops later |
| T5 | n-back and 2-back with lure trials (rate .25), letters and our task words | A zero-shot; B demo ladder 1-back to N-back | d' and lure false-alarm rate by N from 2 to 8 | B higher d' at N of 4 or more |
| T6 | Same n-back items on 4 or more model/scaffold variants | probe score vs our bench score | Rank correlation | rho of 0.5 or more, else drop the gate |
| T7 | n-back and tracking with a rule-restatement item | A none; B state the rule before the stream | Fraction of runs where applied lag differs from instructed | B halves rule drift |
| T8 | Distractor share 0, 25, 50, 75% at constant length | A raw context; B code-filtered context | Accuracy vs share | B flat, A falls (SWiM) |
| T9 | Hardest bench items with a second duty (parallel counting) | A plain; B with state block carried | Accuracy ratio dual over single | Ratio above 0.9 for reasoning models (d09) |
| T10 | Small vs large model on heavy vs light scaffold | 2 sizes by 2 weights | Accuracy | Heavy scaffold hurts the small model |
| T11 | Needed fact at start, middle, end of constant-length prompt | 3 positions | Accuracy | Middle lowest |
| T12 | Retired value must stop appearing | A "REMOVE x" line; B rewrite without x; C rewrite plus separate log | Stale-value reappearance rate; later recall of x | B and C near 0 reappearance; only C answers recall |

## 9. What does not transfer, and why

- **Decay and time-based refreshing.** An LLM has no decay and no clock. TBRS timing maps only to tokens per step (d14). Refresh equals reselecting the item in the written state (d15).
- **The number 4 as a hard slot count.** Human data with a contested slot model (K03). LLM capacity moves from about 3 to 10 with prompting (b05).
- **Slot versus resource arguments.** Not decision-relevant (K03).
- **WM training.** The agent is not trained. Even in humans far transfer is near zero with active controls (b17).
- **Attention sharpening and neural interventions** (b06, c08, a17, a23). They need weights access or fine-tuning. Latent-thought training (a23: +2.5 to +7.5 on GSM8K over Coconut) is not available to us.
- **Brain stimulation and theta-gamma coding** (b25). No agent analogue.
- **Human dual-task ratios** (d13). A template for how to measure, not a target number.
- **Baddeley-style box diagrams for agents** (c21). Unmeasured boxes; our executive is code.
- **Visuospatial sketchpad.** VLMs do worse from images (b11).
- **Letter n-back as a model of agent work.** Almost all LLM n-back work uses letter streams. The only link to reasoning is a 10-model correlation that a 54-model study does not support (K12).

## 10. Open questions

1. Does overwrite or retire-stale beat append-only at equal tokens for 2026 reasoning models? (Gap 1; open.)
2. Does the WMIP write-state gain hold at equal total tokens on non-arithmetic tasks? (Gap 2.)
3. What are n-back and PI-LLM numbers for GPT-5, Grok-4, Gemini 2.5 Pro and current Claude models? The authors assert decline without numbers (d04).
4. Is the n-back to reasoning link real once training compute is controlled? (K12.)
5. Does a restate-only-the-relevant-item prompt reduce lure false alarms on held-out trials? Not tested anywhere found.
6. What is the agent-level span, and is it near 3 to 4?
7. Does renaming a group of items under one label raise agent span as Smith's recoding did for humans? No LLM study found.
8. Are the Daneman-Carpenter and Engle effects reproducible in LLMs? Only across-model structure and a dual-task paradigm found. A backward-digit-span versus fluid-intelligence paper and a December 2025 classic-WM-tasks study appeared in a snippet and were not opened, so are not counted.
9. Multi-agent load splitting versus a single agent with structured notes: not compared.
10. Original numbers from Baddeley and Hitch 1974, Daneman and Carpenter 1980, Redick 2013 and the full TBRS paper were not opened.
11. The c19 table order (GPT-4 versus GPT-3.5) was assumed (critique note 5). The unlabelled transition-statistics sign split (.36 / -.62) in a18 is unexplained.

## 11. Sources

[V] = opened and read (in part or in full) in this series. [M] = snippet or secondary only.

- [V] Miller (1956) The magical number seven, plus or minus two. http://psychclassics.yorku.ca/Miller/ (via a summary of the full text)
- [V] Hitch, Allen, Baddeley (2024) The multicomponent model of working memory fifty years on. https://eprints.whiterose.ac.uk/id/eprint/224362/1/hitch-et-al-2024-the-multicomponent-model-of-working-memory-fifty-years-on.pdf
- [V] Cowan (2001) The magical number 4. https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf
- [V] Souza, Rerko, Lin, Oberauer (2014) Focused attention improves working memory. https://link.springer.com/content/pdf/10.3758/s13414-014-0687-2.pdf
- [V] Gong, Wan, Wang (2024) Working memory capacity of ChatGPT. https://arxiv.org/abs/2305.03731
- [V] Gong and Zhang (2024) Self-attention limits working memory capacity. https://arxiv.org/abs/2409.10715
- [V] Xiong et al. (2026) In-context superposition. https://arxiv.org/abs/2604.09670
- [V] Wang and Sun (2025) Unable to forget (PI-LLM). https://arxiv.org/abs/2506.08184
- [V] Huang, Sun, Wang, Dredze (2026) Failure of latent state persistence. https://arxiv.org/abs/2505.10571
- [V] Aichberger and Hochreiter (2026) Reasoning in Memory. https://arxiv.org/abs/2605.30343 (not re-opened in the cross-check)
- [M] Baddeley (2000) episodic buffer, via Wikipedia. https://en.wikipedia.org/wiki/Baddeley%27s_model_of_working_memory
- [M] Daneman and Carpenter (1980). https://doi.org/10.1016/S0022-5371(80)90312-6
- [M] Engle (2002). https://doi.org/10.1111/1467-8721.00160
- [M] Barrouillet et al. (2004) / Oberauer (2002). https://doi.org/10.1037/0096-3445.133.1.83
- [V] Hu and Lewis (2025) Do language models understand the cognitive tasks given to them? https://arxiv.org/abs/2412.18120
- [V] Gong (2026) Language models share a readout bottleneck. https://arxiv.org/abs/2610.21176
- [V] Strong memory, weak control (2025). https://arxiv.org/abs/2504.02789
- [V] Liang, Zhu, Wang, Zhou (2026) Spatial n-back in VLMs. https://arxiv.org/abs/2602.04355
- [V] CoThinker, United Minds (2026). https://arxiv.org/abs/2506.06843
- [V] Soveri et al. (2017) n-back training meta-analysis. https://link.springer.com/article/10.3758/s13423-016-1217-0
- [V] Au et al. (2016) reply. https://link.springer.com/article/10.3758/s13423-015-0967-4
- [V] Sala and Gobet (2017) children meta-analysis. https://eprints.lse.ac.uk/102203/
- [V] Cowan (2010) Magical mystery four. https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/
- [V] Rouder et al. (2008) fixed-capacity models. https://pmc.ncbi.nlm.nih.gov/articles/PMC2329704/
- [V] Ma, Husain, Bays (2014) Changing concepts. https://pmc.ncbi.nlm.nih.gov/articles/PMC4159388/
- [V] Lewandowsky, Geiger, Oberauer (2008) Interference-based forgetting. https://api.research-repository.uwa.edu.au/ws/files/1545881/11334_PID11334.pdf
- [V] Oberauer et al. (2012) SOB-CS. https://link.springer.com/article/10.3758/s13423-012-0272-4
- [V] Baddeley, Hitch, Allen (2019) Modal model. https://link.springer.com/article/10.3758/s13421-018-0878-5
- [V] Turi, Alekseichuk, Paulus (2018) primer. https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.2005867&type=printable
- [M] Redick et al. (2013). https://pubmed.ncbi.nlm.nih.gov/22708717/
- [V] Zhang et al. (2024) Working memory identifies reasoning limits. https://aclanthology.org/2024.emnlp-main.938.pdf
- [V] Dsouza et al. (2024) SWiM. https://arxiv.org/abs/2407.03651
- [V] Wang et al. (2026) WMIP. https://arxiv.org/abs/2603.27343
- [V] Wang et al. (2024) Symbolic working memory. https://arxiv.org/abs/2408.13654
- [V] Zhang et al. (2024) Ewe explicit working memory. https://arxiv.org/abs/2412.18069
- [V] Empowering working memory for LLM agents (2023). https://arxiv.org/abs/2312.17259
- [V] giantfish-fly (2025) PI-LLM dataset card. https://huggingface.co/datasets/giantfish-fly/LLMs-First-Task
- [V] Hou et al. (2026) CogBattery. https://arxiv.org/abs/2607.24999
- [V] Emura and Sugawara (2026) Dual-task sentence comprehension. https://arxiv.org/abs/2604.26351
- [V] Kim et al. (2026) Scaling agent systems. https://arxiv.org/abs/2512.08296
- [V] Tang et al. (2026) Entity tracking across state changes. https://arxiv.org/abs/2605.30233
- [V] Pougeon, Camos, Belletier, Barrouillet (2024) Quantifying resource sharing. https://doi.org/10.3758/s13423-024-02494-4
- [V] Barrouillet, Bernardin, Camos (2004) abstract. https://europepmc.org/article/MED/14979753
- [V] Vergauwe et al. (2025) Instructed refreshing. https://doi.org/10.3758/s13421-024-01666-w
- [V] Dames et al. (2025) Removing information from working memory. https://doi.org/10.3758/s13423-024-02550-z
- [V] Oberauer and colleagues (2026) Removal from working versus long-term memory. https://europepmc.org/article/PMC/PMC13068088
