# Working-memory limits and chunking: deep document

*Subfield A08.08 of cognitive load theory. Written from evidence_a-d.jsonl, claims.jsonl (K01-K34) and critique.md in this folder. Evidence ids (a01, b07, d06 ...) point to lines in the evidence files. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Why it matters for our agent: the human limit is an analogy for the context budget. The LLM evidence is the part that can change the schema.*

## 1. What it is

Working memory (WM) is the small store that holds what a person is using right now. Two ideas define this subfield.

1. **A limit on how much can be held.** Miller (1956) said span is about seven items, plus or minus two. Cowan (2010) later argued the real limit is about three to five chunks once rehearsal and grouping are blocked.
2. **Chunking.** A chunk is a familiar unit built by grouping input and giving the group a name (a02). The count of chunks stays limited. The content per chunk can grow. So chunking is the only route to hold more content under a fixed count.

Baddeley and Hitch (1974) added structure: a phonological loop, a visuospatial sketchpad and a central executive, with an episodic buffer added in 2000 (a16). Their dual-task numbers were not obtained (a23, d16), so nothing here rests on them.

For a language model there is no direct match. A model has a context window, not seven slots. Still, five things carry over as measurable effects:
- accuracy falls as input grows, far below the window limit;
- position in the input matters;
- stale updates interfere with new ones;
- state not written out is lost;
- agents that replace raw history with short named summaries (chunks) can do better at lower cost.

No study tests Miller's 7 plus or minus 2 in an LLM or tests spontaneous chunk formation (c25, K23). The human numbers are analogy only.

## 2. History and theories in depth

**Miller (1956)** (a01-a03, b01-b03; opened, psychclassics HTML). Miller reviewed other people's data. He did not run new experiments.
- Absolute judgment of one-dimensional stimuli saturates at a mean of 2.6 bits (SD 0.6), about 6.5 categories. Range about 3 to 15 categories. Pitch 2.5 bits, loudness 2.3, salt 1.9, position in an interval 3.25.
- Six acoustic dimensions together give 7.2 bits (about 150 categories). Adding dimensions helps with sharply diminishing return. Eight binary dimensions give 6.9 bits.
- Span counts items, not bits. Decimal digits (3.3 bits each) give a span near 7; binary digits near 9; monosyllabic words (about 10 bits each) near 5.
- Recoding: Smith's experiment (20 subjects). Span was 9 binary or 7 octal digits. Binary triples recoded to octal. Smith recalled 12 octal digits, which is 24 binary digits at 2:1 recoding and about 40 at 4:1 or 5:1.
- Miller called the shared "seven" a possible "pernicious, Pythagorean coincidence". The 7 was never a constant.

**Chase and Simon (1973)** (a04-a06, opened, gwern PDF). Three chess players (master, class A, beginner), 5 s view.
- Middle-game first-trial recall: about 16 / 8 / 4 pieces. End games about 8 / 7 / 4.
- Random positions: "no relation at all" to skill.
- Pauses of about 2 s or more between placed pieces mark chunk boundaries. A label sits in short-term memory. Content comes from long-term memory.
- Chunks per first trial, middle games: master 7.7, class A 5.7, beginner 5.3. End games 7.6 / 6.4 / 4.2. Chunk count stays near 7 but is not flat across skill. First chunk size: master 3.8 pieces, beginner 2.4. Later chunks shrink to 1 to 2.
- Their model: a linear list of about seven chunk slots.

**Cowan (2010) and the "magic four"** (a07, a08, b04-b06). Capacity is about 3 to 5 chunks in young adults when rehearsal and grouping are blocked.
- Running span: last 3 to 5 digits. Rehearsal covers about 2 s of speech.
- Chen and Cowan: about 3 units with rehearsal blocked, for singletons or learned pairs. Saults and Cowan: about 4 after masking sensory memory.
- Development: about 1.5 items at age 7, about 3.0 in older children and adults.
- Long verbal chunks (idioms, sentences) give 3 or 4.
- Two readings of why: limit as weakness (neural firing cycles) or limit as strength (search is efficient near 3.5 items). Rivals: controlled-attention and spread-thin resource views (b06).

**Slots versus resources** (a09, a10; Luck and Vogel 2013 review, opened). Visual change detection shows Kmax of 3 to 4 objects, and multi-feature objects are held about as well as single-feature ones. Zhang and Luck's mixture model: going from 3 to 6 items mainly lowers the chance an item is stored. Precision barely changes. Observers could not raise Kmax by trading precision, even with money. Capacity explains about 43% of fluid intelligence variance (Fukuda 2010) and about 46% of a broad battery (Johnson 2013). Test-retest r = 0.77 over 1.5 years. Ma, Husain and Bays (2014) argue the opposite, for resources (b28, not opened). Both camps are paradigm owners. Status: contested.

**Chunking mechanisms.**
- Redintegration versus compression (Norris, Kalm and Hall 2020, a11). Two-word chunks act like redintegration: long-term memory rebuilds a decayed trace, no space is saved. Three-word chunks act like compression, with a cost. In Exp 5, if one word of a learned triple was recalled, the chance all three were recalled was .94.
- Does chunking free capacity or only aid retrieval? Thalmann, Souza and Oberauer (2019, d13, abstract only): chunking helped both chunked and unchunked items, so it reduces load. It works best when chunks come from long-term memory, share no elements and come early in the list.
- Template theory (Gobet and Simon 1998, a25 not opened; Gobet and Clarkson 2004, d14 abstract): experts hold large templates with fillable slots. Most often no more than three chunks were replaced. Masters replaced chunks of up to 15 pieces.
- Retrieval structures (Ericsson, Chase and Faloon 1980, a15 via Wikipedia): student SF raised digit span from 7 to almost 80 over about 20 months, at least 230 hours. He still chunked only 3 to 4 digits at a time. Mnemonic associations in long-term memory did the work.
- CHREST (c23) and Soar chunking (c24): symbolic architectures. CHREST sets visual STM at 3 chunks. Soar compiles impasse reasoning into new rules. No fit statistics were read.
- Chunking as a development account (Jones 2012, a14): a chunking model reproduces growth in apparent span and speed with no change in capacity or speed parameters. Each chunk costs about 400 ms to encode.

**Binding in transformers** (b24, Feng and Steinhardt 2024): models bind entities to attributes with "binding ID" vectors in a continuous subspace. This suggests a soft capacity for how many entities can be kept apart. No number given.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Absolute judgment channel capacity | 2.6 bits mean (SD 0.6), about 6.5 categories | Miller 1956 (a01, b01) | [E] human, review of others' data |
| Span is in items, not bits | decimal 7, binary 9, monosyllabic words 5 | Miller (b02) | [E] human |
| Recoding raises content under a fixed count | Smith: 12 octal = 24 to about 40 binary | Miller (a02, b03) | [S] one trained subject |
| Chess recall depends on real structure | master/A/beginner about 16/8/4 pieces, N=3; random: no relation | Chase and Simon 1973 (a04) | [S] N=3, later qualified |
| Chunks per trial | 7.7 / 5.7 / 5.3 (middle games) | Chase and Simon (a06) | [S] |
| Experts keep an edge on random material | r = .41 [.29,.51], 24 studies, 903 people, I2 = 63; trim-and-fill r = .29 [.17,.41]; experts better in 49 of 55 samples | Sala and Gobet 2017 (b07, d12) | [E] contradicts Chase and Simon's null |
| Domain moderator is marginal | music .69, games .42, programming .36, sports .30, other .24; Q(4)=8.69, p=.069 | b08 | [E] |
| Core capacity without rehearsal | 3 to 5 chunks | Cowan 2010 (a07) | [E] (3 sources) |
| Visual WM | Kmax 3 to 4; 43-46% of Gf variance | Luck and Vogel 2013 (a09) | [C] slots vs resources |
| Strict scoring removes pair benefit | 4 pairs = 2x singletons only under lenient scoring | Chen and Cowan via Norris (a12) | [C] |
| Complex span not lower because of blocked chunking | N=94, predicted interaction absent | Mathy et al. 2018 (a13) | [C] |
| Chunk size 2 vs 3 | 2 words: redintegration; 3 words: compression | Norris et al. 2020 (a11) | [C] |
| Far transfer is near zero with active controls | WM training 0.05 SD [-0.05,0.15], k=40; music 0.03 SD, k=54; chess 0.10 SD (one study). Passive controls: music 0.25, WM 0.18 | Sala and Gobet 2017b (b10) | [S] |
| Huge digit span from long-term structure | 7 to almost 80 in about 20 months | Ericsson et al. via Wikipedia (a15) | [S] secondary |
| LLM n-back drops like humans (GPT-3.5) | d' about 1 at n=3 in base, feedback and reasoning variants; noise lowers it; 50 blocks per n, temp 1 | Gong et al. 2024 (a17, c01) | [S] |
| N-back limit is not fixed | Llama 3.1 70B task accuracy 90.08/90.08/84.75% at n=8/9/10; 1/2/3-back 1.00/0.99/0.93; Llama 8B 1.00/0.14/0.17; GPT-3.5 1.00/0.51/0.43 | Hu and Lewis 2025 (c06, c07) | [S] |
| LLM span strong forward, weak backward | forward 50 digits; backward breaks near 15; Flanker 40-60% vs human 93-96% | de Langis et al. 2025 (c09-c11) | [S] |
| Padding hurts reasoning | mean accuracy 0.92 to 0.68 by 3000 tokens | Levy et al. 2024 (a20) | [E] |
| Length alone hurts | 13.9% to 85% drop with perfect retrieval, whitespace or masked distractors | Du et al. 2025 (d03) | [S] |
| Lost in the middle | GPT-3.5 drops over 20 points in the middle; below 56.1% closed-book at 20-30 docs; oracle 88.3% | Liu et al. 2024 (a19, c16) | [E] |
| Position bias depends on window fill | strongest up to about 50% fill, peaks near 25% (reasoning) and 38% (retrieval); then end bias | Veseli et al. 2025 (d01) | [S] but fits [E] pattern |
| Effective context shorter than claimed | GPT-4: 96.6, 96.3, 95.2, 93.2, 87.0, 81.2 from 4K to 128K, effective 64K; Mistral-v0.2 7B 75.4 at 32K, 13.8 at 128K | RULER (a21, c18) | [E] |
| No lexical overlap breaks long context | 11 of 13 models under 50% of baseline at 32K; GPT-4o 99.3 to 69.7 | NoLiMa (d04) | [E] |
| Irrelevant context dose-response | Gemini-2.0-Flash 0.85, 0.82, 0.78, 0.72 at 0/20/50/80% load; slope -0.003 per %, p<0.001; GPT-4o 0.65 to 0.55, p=0.07; small open models 0% everywhere | Adapala 2025 (b19) | [S] |
| Proactive interference | log-linear fall over 3 to 400 updates; threshold step under sequential order; parameter count t=3.03, p=0.005, N=30, 26.1% variance; "ignore" helps little | Wang and Sun 2025 (c13-c15) | [S] |
| Multi-turn loss | -39% average; aptitude -15%, unreliability +112%; 15 LLMs, 600 instructions | Laban et al. 2025 (a22) | [S] |
| Restating every turn only partly helps | recovers 15-20% of loss; CONCAT reaches 95.1% of FULL | Laban 7.1 (d10) | [S] |
| Hidden state not written is lost | CoT success GPT-4o-mini 5/150, GPT-4o 26/150 and 31/150 | Huang et al. 2026 (c12) | [E] with Kim and Schuster (b25) |
| Chunking-style prompt on tracking | +35.4 points to 96.4% (text-davinci-002); simple prompt +15.8 on ada-001 | Zhang et al. 2024 (b16, b17) | [S] |
| Subgoal summaries in an agent | success 21 to 42; context -35%; steps -3.8 | HiAgent (c21, d15) | [C] unreplicated |
| Masking old observations matches summaries | Qwen3-Coder 53.4 raw / 54.8 masked / 53.8 summary; Gemini Flash 32.8/35.6/36.0; cost cut 41-57%; summaries add about 15% turns | Lindenbauer et al. 2025 (d06) | [S] |
| Untuned summaries lose detail | AppWorld gpt-4.1 56.0 to 43.5; tuned rules 56.5 with 26-54% fewer peak tokens | ACON (d07) | [S] |
| Bounded state beats growing history | MEM1-7B 3.5x the 14B full-context model with 27.1% of peak tokens at 16 objectives (RL trained) | MEM1 (d08) | [S] |
| Training-free periodic summary | +4.5% average over ReAct | ReSum (d09) | [S] |
| Gist plus lookup | context extended 3.5x to 20x; QuALITY gist 85.53% | ReadAgent (c22) | [S] |
| Paging memory | deep memory retrieval GPT-4 32.1% to 92.5% | MemGPT (c19) | [S] |
| Stored workflows | WebArena 23.5 to 35.5 (+12.0), about 2 fewer steps | Agent Workflow Memory (d11) | [S] no equal-token control |
| Overload as attack | attack success Claude-3-Opus 99.99%, Llama-3-70B 92.67%, GPT-4 90.95% | Upadhayay et al. 2024 (c20) | [S] |

## 4. Mechanisms and models

**4.1 Chunk-and-label store (Chase and Simon, EPAM, CHREST).** Engineer's view.
- Long-term store: a discrimination network of patterns. A pattern is a small set of items linked by relation (attack, defence, colour, proximity).
- Working store: a short list of chunk labels. Cowan: 3 to 5 labels. Chase and Simon: about 7. CHREST sets 3.
- Cost model: about 2 s to recognise a chunk and store a label; about 300 ms per added element (a05); about 400 ms per chunk in Jones' model (a14).
- Recall: read the labels out and fetch each chunk's content from the long-term store.
- Boundary detection: a pause of about 2 s or more.
- Growth: templates. A stable core plus fillable slots. Masters hold chunks up to 15 pieces (d14).
- Implication: capacity in labels is fixed. Skill raises content per label. Recall of random material also benefits (r = .41), so many small chunks matter too.

**4.2 Compression versus redintegration (Norris and Kalm).** Two ways a stored pattern helps.
- Redintegration: a decayed trace is cleaned up using long-term knowledge. No working space saved. Seen with 2-item chunks.
- Compression: a group is recoded into one shorter code. Space saved, with a cost to decode. Seen with 3-item chunks.
- Implement as: summarise only when the summary is shorter than the source and the loss of detail is acceptable. A summary equal in size to the source is just rewording.

**4.3 Load relief for neighbours (Thalmann).** A chunk is useful when it comes from long-term memory, has no overlapping elements and comes early in the list. Then other items in the list are recalled better too. For a prompt: put stable named chunks first and keep them non-overlapping (single source, abstract level).

**4.4 Slots plus averaging (Zhang and Luck).** Each item is either stored with fixed precision or not stored. Raising the number of items lowers the chance each is stored. Implement as: probability an item is available falls as K/N once N exceeds K. Contested by resource models.

**4.5 Transformer-side mechanisms (as far as measured).**
- Attention dispersion (c04, c05): in small decoder-only transformers trained from scratch on N-back, attention entropy rises with N and correlates negatively with accuracy. Test accuracy declines logarithmically out to N=6. 1-layer 1-head: Kruskal-Wallis H=38.517, p<.001, eta-squared 0.248. Models with more layers or heads stay above 95%. Correlational, small models only.
- Retrieval heads (c08): Qwen 1.5 14B has a head whose attention matches the needed retrieval (max 71.98%). Llama 3.1 8B and 70B are far more diffuse (4.86%, 8.52%), yet 70B does 10-back. So diffuse attention does not by itself mean low capacity.
- Positional bias (d02): a U-shaped attention bias on first and last tokens regardless of relevance. Calibrating it out improves RAG by up to 15 points.
- Binding IDs (b24): entity-attribute binding by vectors in a continuous subspace. Soft capacity.
- Proactive interference (c13-c15): older values compete with the latest. Under shuffled order, decay is log-linear. Under sequential updates, a step at a model-specific threshold.

**4.6 Agent-side chunking (what an engineer can build now).**
- HiAgent: the model sets a subgoal, acts, and on completion replaces that subgoal's action-observation pairs with a summary. Only the current subgoal keeps full detail.
- Observation masking: replace observations older than a window of M=10 with a placeholder (d06).
- ACON: compression guidelines refined from failure cases; thresholds of 4096 (history) and 1024 (observation) worked best (d07).
- MEM1: one consolidated state rewritten each turn (RL trained, d08).
- MemGPT: small main context with a recursive summary queue and archival storage paged by function calls (c19).
- ReadAgent: paginate, gist, look up (c22).
- Agent Workflow Memory: induce reusable workflows from past successes (d11).

## 5. What holds up

**Replicated or well supported**
- Item count, not bits, limits span (Miller). Reviewed data, long accepted. [E]
- Real human capacity is below 7 once strategies are blocked: about 3 to 5 (Cowan, Saults and Cowan, Chen and Cowan, Luck and Vogel). [E]
- Experts' memory advantage is largely domain-specific: 49 of 55 samples favour experts on domain material; far transfer from WM or chess or music training is near zero with active controls (0.03-0.05 SD). [E] for domain specificity.
- Accuracy falls with input length and irrelevant material in LLMs: Levy, RULER, NoLiMa, Context Rot (18 frontier models), Du et al. [E].
- Position effects in LLMs: Liu et al. and Veseli et al. [E] for the pattern, with fill-level moderation.
- Unwritten state is lost: Huang et al. and Kim and Schuster [E].

**Failed, qualified or contested**
- Chase and Simon's null on random positions (N=3) did not hold up. Sala and Gobet found r = .41, shrinking to .29 after publication-bias adjustment. Chase and Simon is not in the meta-analysis; it appears only in the table with N=3.
- A fixed chunk count fails under strict scoring (Chen and Cowan): four pairs beat four singletons only under lenient scoring. Without articulatory suppression there was no chunk-based limit.
- Mathy et al. (N=94): the prediction that complex span (4 plus or minus 1) is lower than simple span (7 plus or minus 2) because processing blocks chunking was not confirmed.
- Chunk size matters: 2-word chunks do not free space (Norris et al.).
- Seven slots (Chase and Simon) versus about 2 to 3 large templates (Gobet and Clarkson) versus 3 to 5 (Cowan). All can be right if they describe different things (strategy-assisted recall, core store, expert templates).
- Hebb effect (repetition learning, a lab model of chunk formation): Musfeld et al. 2026 (b12) argue it is neither gradual nor implicit once analyses are corrected.
- Slots versus resources is still open.
- Bridge experts (b13): advantage requires the hand sorted by suit (group F(1,98)=38.33; group x suit F(1,98)=30.21, partial eta2 .236). Supports both template and SEEK accounts.
- Multi-set capacity (Superbia-Guimaraes and Cowan 2026, b11): recall of one set of 3 items depends on the number of sets, not just total items. N=181 over four experiments. Trade-off 2.77 items per item lost (with pauses), 1.44 without pauses.

**Moderators**
- Domain: music .69 to sports .30 (marginal, p=.069). Presentation time had no effect (p=.346).
- Scoring: lenient versus strict.
- Rehearsal: blocked versus allowed.
- Chunk source: learned in long-term memory versus ad hoc; non-overlapping versus overlapping; early versus late in the list.
- Window fill (LLMs): positional bias changes shape with fill.
- Presentation order (LLMs): shuffled gives gradual decay, sequential gives a step.

**Interventions that worked**
- Human: long-term retrieval structures (SF, 7 to about 80 digits). Domain learning for domain recall.
- LLM: restate the evidence before solving (GPT-4o up to +4% on RULER; Llama-3.1-8B up to +31.2% on GSM8K, d03). Query-aware placement (query before and after the data) made GPT-3.5-Turbo 16K perfect at 300 key-value pairs, versus a worst case of 45.6% (c17). Calibrating positional bias: up to +15 points on RAG (d02). Binding entity and attribute in one unit: +35.4 points on an old model (b17).
- Agent: masking old observations (cost -41 to -57% at equal solve rate), failure-tuned summary rules (43.5 to 56.5), subgoal summaries (21 to 42, unreplicated), bounded rewritten state (RL), workflow memory (+12.0).

**Interventions that did not work**
- Telling the model to ignore stale input: little help (Wang and Sun). Explicit "ignore irrelevant text" and self-consistency only partly fixed GSM-IC (b23).
- Masking distractors does not remove the length cost (d03).
- Restating all prior information each turn: only 15-20% of loss recovered (d10).
- Untuned LLM summaries: they lost 12.5 points on AppWorld (d07), and made runs about 15% longer (d06).
- Training-free summarisation: only +4.5% (ReSum).
- Reasoning models do not reliably raise WM span (c10).
- Small models often do better with answer-only prompts than with AutoCoT, PS or ToT (b16).
- General WM or domain training for far transfer: near zero.

## 6. Language models

**6.1 N-back and span tests (capacity analogue).**
- GPT-3.5-turbo, verbal n-back: d' falls to about 1 at n=3 in base, feedback and reasoning variants. Noise lowers it. Larger spatial grids give higher capacity. Spatial is lower than verbal. CoT prompts improved spatial performance. GPT-4 is higher but only tested to n=3. Six open 6B-13B models are very low and nearly alike (a17, a18, c01-c03).
- Zhang et al. (EMNLP 2024, b16): d' rises with model size and instruction tuning. Human d' 3.39-4.05 in a 4x4 grid; text-ada-001 and babbage-001 d' 0.01-2.51. "After thinking carefully, the answer is" lifted ada-001 to 25.4% (+15.8) on Tracking Shuffled Objects. text-davinci-002 reached 96.4% (+35.4) with the chunked prompt, +4.8 on Web of Lies.
- Hu and Lewis (c06-c08): weak models' errors match a different m-back task, so they misunderstood the task. Llama 3.1 70B: 84.75% task accuracy at 10-back. So "capacity of 3" belongs to GPT-3.5 and that prompt.
- de Langis et al. (c09-c11): forward span 50 digits; backward breaks near 15. More WM capacity did not correlate with executive scores.
- Gong and Zhang (c04): from-scratch small transformers; not evidence for deployed models.
- Caveat: most of these are 2023-2024 models.

**6.2 Length, distraction and position.**
- Levy: 0.92 to 0.68 by 3000 tokens, key facts fixed; next-word-prediction quality does not predict reasoning accuracy; CoT adds a similar amount at every length (GPT-4 excepted).
- Adapala: dose-response in Gemini-2.0-Flash (0.85 to 0.72 at 80% load). Length alone did not explain it (long control 0.82, p=0.45). Weak open models floor at 0%.
- Shi et al.: one irrelevant sentence cuts grade-school math accuracy; exact drops not extracted.
- RULER: only about half of 17 models stay satisfactory at 32K. NoLiMa: 11 of 13 below half of baseline at 32K. Context Rot: all 18 frontier models degrade; one distractor hurts, four hurt more; shuffled haystacks beat coherent ones in all 18.
- Du et al.: the drop persists with perfect retrieval, whitespace and masked distractors. So length itself costs accuracy.
- Position: Liu et al. U-shape; Veseli et al.: the U-shape is strongest below about 50% fill, then recency (distance to end) dominates.
- Multi-turn (Laban): -39%; CONCAT reaches 95.1% of FULL, so rephrasing is not the cause.

**6.3 State tracking and interference.**
- Kim and Schuster: only code-pretrained GPT-3.5 tracks box contents well; performance falls with more operations.
- Huang et al.: unwritten hidden state is lost; CoT helps 10-30%, except some GPT-4o versions.
- Wang and Sun: stale updates interfere; parameter count predicts resistance, not window size.

**6.4 What changed it, by how much (summary).**
- Chunked/bound state format: +35.4 points (old model).
- Recite-then-solve: up to +4% (GPT-4o, RULER), up to +31.2% (Llama-8B, GSM8K).
- Query before and after the data: 45.6% worst case to 100% (GPT-3.5 16K).
- Calibrating position bias: up to +15 points (RAG).
- Failure-tuned summaries: 43.5 to 56.5 on AppWorld.
- Masking: cost -41 to -57%, solve rate about equal.
- Subgoal chunking (HiAgent): 21 to 42 success, context -35%. Caveat from critique: the headline progress +23.94% and context -35.02% match the Jericho row in Table 1, not a clean average. One reading reports +20% success against subgoals without trimming; the abstract shows no component ablation. Treat as contested.
- RL-trained bounded state: 3.5x at 27.1% peak tokens (MEM1).
- Workflow library: +12.0 points (GPT-4, WebArena), no equal-token control.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md.

### Add now (established)

1. **Keep the context per step minimal and relevant. (G, new guardrail "minimal context per step"; S3/S5 prompts)** [E] K14. Evidence a20, a21, b19, b21, b22, c18, d03, d04, d05. Useless padding costs accuracy far below the window limit. G7 already demands equal-token tests, so this fits.
2. **Put the current subgoal and key facts at the end of the prompt, not the middle. (S1, S3 prompt layout)** [E] K15. Evidence a19, b20, c16, d01, d02. Place last, because near-full windows favour the end. Start-plus-end duplication is untested, see Test first.
3. **Write state out; do not rely on implicit tracking. (S2 REPRESENT, S5, code ledger)** [E] K18. Evidence c12, b25. Consistent with G10 (decide from outputs).
4. **Keep the working set per step small and count structures, not atoms. (G, S3)** [E] for the human limit (K03; a07, b04, a09, b05). The item cap itself is untested in LLMs, so use 3 to 5 named things per step only as a design rule of thumb. Count large named structures as one (K31, d14).
5. **When history must be compressed, keep a path back to the source (gist plus lookup). (memory)** [E] K20. Evidence c22, c19.

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Named subgoal summaries replace raw history for finished subgoals | memory, O3 Decompose | [C] | K19; c21, d15, d06, d07 |
| Observation masking before any summarising | memory | [S] | K26; d06 |
| Summary rules built from failure analysis; compression threshold sweep | O, memory | [S] | K27; d07, d09 |
| Code-held state ledger, restated each step | G (program holds state) | [S] | K17, K29; a22, d10, d08 |
| Delete superseded facts, do not say "ignore" | memory | [S] | K16; c13-c15, d06, d03 |
| Recite needed facts before reasoning | S1/S3 slot | [S] | K28; d03 |
| One task per step (no bundling) | G, S3 | [S] | K24; c20, b23 |
| Bind entity with attribute in one unit | S2 representation | [S] | K21; b16-b18 |
| Stable named chunks first in the prompt | S layout | [S] | K30; d13 |
| Cap by structures (2, 4, 8) | G | [S] | K31; d14 |
| Pattern or workflow library vs raw history at equal tokens | memory (subgoal library) | [S] | K32; d11 |
| Measure our backbone's working-set size (n-back or state-update) | S0 class record | [S] | K11, K12; a17, c06, c07 |
| Bounded rewritten state, training-free | memory | [S] | K33; d08, d09 |
| Summarise only when it compresses | O | [C] | K09; a11, b11 |

## 8. Concrete tests on our bench

All arms get the same total tokens (setup cost counted, G7). Score strictly (exact match or exact slots), since lenient scoring inflated the chunk benefit in humans (K04).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Multi-step puzzle or agent trajectory of 15+ steps | A raw history; B named-subgoal summaries; C masking with window 10 | exact-answer accuracy; tokens; list of lost facts in failures | B and C beat A at long horizons; C about equal to B; B loses facts unless rules are tuned |
| T2 | Same tasks, compression sweep (1x, 2x, 4x, 8x) | raw vs summaries at each ratio | accuracy vs ratio | flat, then falls; find the knee |
| T3 | Subgoal placement at 25% and 90% window fill | start; middle; end; start plus end | accuracy | end or start-plus-end best at 90%; middle worst at 25% |
| T4 | State-update task (keys updated 3 to 400 times) | A all updates kept; B delete superseded; C keep plus "ignore"; D masked | accuracy of latest value | B > C; B about D |
| T5 | Multi-turn sharded problems (Laban style) | A accumulating chat; B model restates; C code-held ledger re-sent each step | accuracy; run-to-run spread | C > B > A; C recovers more than 15-20% |
| T6 | N-back or tracking at n=1 to 10 on our backbone | bare; scaffold; with written ledger | d' or accuracy by n | find n where accuracy falls under 80%; ledger lifts it |
| T7 | Tracking Shuffled Objects style | separated vs bound entity-attribute state | accuracy | bound better on weaker models; small on frontier |
| T8 | Padding (1x, 3x, 5x irrelevant tokens) | plain; recite-then-solve | accuracy | recite recovers part of the loss |
| T9 | Items per step (2, 4, 8 structures) | cap at each size | accuracy per token | drop above about 4; structures count |
| T10 | Repeated problem class | A 3 stored workflows or lessons; B same tokens of raw history; C none | accuracy; steps | A > B > C |
| T11 | Chunk placement | stable named chunks first vs last | accuracy on remaining items | first better |

## 9. What does not transfer, and why

- **The number seven (or four).** It is a limit of a biological store. An LLM has a context window and soft interference. No study finds an LLM item cap. Hu and Lewis show 10-back at 84.75%. Use 3 to 5 only as a design rule of thumb for how many things a prompt step asks about.
- **Chunk formation by pauses and attention.** Chase and Simon's 2 s pause rule has no LLM counterpart.
- **Rehearsal.** Humans rehearse silently. Models have no hidden loop. Writing text out is the nearest analogue and it costs tokens.
- **Long-term retrieval structures.** SF's span of about 80 depended on 230 hours of practice. A model can get a lookup in one call, but whether it beats a larger context at equal tokens is untested.
- **Visual WM slots.** Human only. Capacity as a predictor of Gf (43-46% of variance) says nothing about a model; de Langis found capacity did not predict executive scores in LLMs.
- **Training for far transfer.** Near zero in humans (0.03-0.05 SD); we do not train.
- **Attention-dispersion explanation.** Shown only in small from-scratch transformers, correlational. Not a design reason.
- **N-back as a capacity.** Weak-model failures are task misunderstanding (Hu and Lewis), and GPT-3.5's "3" is specific to that model and prompt.
- **2023-2024 numbers.** GPT-3.5, Claude-1.3 and text-davinci-002 results may not hold on current models.

## 10. Open questions

1. What are the exact Baddeley and Hitch (1974) dual-task numbers? Not obtained (d16).
2. Do the full Thalmann et al. (2019) numbers support "chunking frees capacity for other items"? Only the abstract was read.
3. Is the HiAgent gain real, and where does detail loss begin along a compression-ratio curve? No replication, no ablation.
4. What is the usable working-set size of our own backbone, with and without scaffold prompts?
5. Does a 3 to 5 item limit exist in frontier models, or does interference depend only on parameter count (Wang and Sun, t=3.03, N=30)?
6. Does the +35.4 point chunking prompt reproduce on current models?
7. Do stored chunks beat a larger context at equal tokens?
8. Does start-plus-end placement remove the middle loss in recent models?
9. Delete versus ignore: no direct test of superseded facts.
10. Does a code-held ledger beat model-held state across turns?
11. Gobet and Clarkson full paper: how were chunks counted, and does "two" hold? Abstract only.
12. Exact numbers for Shi et al. (GSM-IC) and per-task numbers in Zhang et al. were not extracted.
13. Slots versus resources remains unresolved in humans.

## 11. Sources

[V] opened this session; [M] snippet, abstract only or secondary.

- [V] Miller (1956) The magical number seven, plus or minus two. https://psychclassics.yorku.ca/Miller/
- [V] Chase and Simon (1973) Perception in chess. https://www.gwern.net/doc/psychology/chess/1973-chase.pdf
- [V] Cowan (2010) The magical mystery four. https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/
- [V] Luck and Vogel (2013) Visual working memory capacity. https://pmc.ncbi.nlm.nih.gov/articles/PMC3729738/
- [V] Norris, Kalm and Hall (2020) Chunking and redintegration. https://pmc.ncbi.nlm.nih.gov/articles/PMC7144498/
- [V] Mathy, Chekaf and Cowan (2018) Simple and complex WM tasks. https://pmc.ncbi.nlm.nih.gov/articles/PMC6634419/
- [V] Jones (2012) Chunking and developmental change. https://pmc.ncbi.nlm.nih.gov/articles/PMC3375604/
- [V] Chai et al. (2018) Working memory review. https://pmc.ncbi.nlm.nih.gov/articles/PMC5881171/
- [V] Sala and Gobet (2017) Experts' memory superiority for random material. https://pmc.ncbi.nlm.nih.gov/articles/PMC5323477/
- [V] Sala and Gobet (2017) Does far transfer exist? https://pmc.ncbi.nlm.nih.gov/articles/PMC5724589/
- [V] Superbia-Guimaraes and Cowan (2026) Multiple dissimilar sets. https://pmc.ncbi.nlm.nih.gov/articles/PMC13253884/
- [V] Musfeld et al. (2026) Revisiting Hebb. https://pmc.ncbi.nlm.nih.gov/articles/PMC13095083/
- [V] Liu et al. (2025) Bridge experts. https://pmc.ncbi.nlm.nih.gov/articles/PMC11852315/
- [V] Gong, Wan and Wang (2024) Working memory capacity of ChatGPT. https://arxiv.org/abs/2305.03731
- [V] Zhang, Jian, Ouyang, Vosoughi (2024) Working memory identifies reasoning limits. https://aclanthology.org/2024.emnlp-main.938/
- [V] Gong and Zhang (2024) Self-attention limits WM capacity. https://arxiv.org/abs/2409.10715
- [V] Hu and Lewis (2025) Do LMs understand n-back? https://arxiv.org/abs/2412.18120
- [V] de Langis et al. (2025) Strong memory, weak control. https://arxiv.org/abs/2504.02789
- [V] Huang et al. (2026) Failure of latent state persistence. https://arxiv.org/abs/2505.10571
- [V] Wang and Sun (2025) Unable to forget. https://arxiv.org/abs/2506.08184
- [V] Liu et al. (2024) Lost in the middle. https://arxiv.org/abs/2307.03172
- [V] Levy, Jacoby, Goldberg (2024) Same task, more tokens. https://arxiv.org/abs/2402.14848
- [V] Hsieh et al. (2024) RULER. https://arxiv.org/abs/2404.06654
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120
- [V] Adapala (2025) Cognitive load limits in LLMs. https://arxiv.org/abs/2509.19517
- [V] Shi et al. (2023) LLMs easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093
- [V] Feng and Steinhardt (2024) Entity binding. https://arxiv.org/abs/2310.17191
- [V] Kim and Schuster (2023) Entity tracking. https://arxiv.org/abs/2305.02363
- [V] Packer et al. (2023) MemGPT. https://arxiv.org/abs/2310.08560
- [V] Upadhayay et al. (2024) Cognitive overload attack. https://arxiv.org/abs/2410.11272
- [V] Hu et al. (2024) HiAgent. https://arxiv.org/abs/2408.09559
- [V] Lee et al. (2024) ReadAgent. https://arxiv.org/abs/2402.09727
- [V] Veseli et al. (2025) Positional biases shift. https://arxiv.org/abs/2508.07479
- [V] Hsieh et al. (2024) Found in the middle. https://arxiv.org/abs/2406.16008
- [V] Du et al. (2025) Context length alone hurts. https://arxiv.org/abs/2510.05381
- [V] Modarressi et al. (2025) NoLiMa. https://arxiv.org/abs/2502.05167
- [V] Chroma (2025) Context Rot. https://www.trychroma.com/research/context-rot
- [V] Lindenbauer et al. (2025) The complexity trap. https://arxiv.org/abs/2508.21433
- [V] Kang et al. (2026) ACON. https://arxiv.org/abs/2510.00615
- [V] Zhou et al. (2025) MEM1. https://arxiv.org/abs/2506.15841
- [V] Wu et al. (2026) ReSum. https://arxiv.org/abs/2509.13313
- [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Wikipedia, Chunking (psychology), secondary for Ericsson et al., Dirlam, Kibbe and Feigenson. https://en.wikipedia.org/wiki/Chunking_(psychology)
- [V] Wikipedia, CHREST. https://en.wikipedia.org/wiki/CHREST
- [V] Wikipedia, Soar. https://en.wikipedia.org/wiki/Soar_(cognitive_architecture)
- [M] Thalmann, Souza, Oberauer (2019) How does chunking help WM? Abstract only. https://doi.org/10.1037/xlm0000578
- [M] Gobet and Clarkson (2004) Chunks in expert memory. Abstract only. https://doi.org/10.1080/09658210344000530
- [M] Baddeley and Hitch (1974) Working memory. DOI confirmed only. https://doi.org/10.1016/S0079-7421(08)60452-1
- [M] Norris and Kalm (2021) Chunking and data compression. https://doi.org/10.1016/j.cognition.2020.104534
- [M] Ma, Husain, Bays (2014) Changing concepts of working memory. https://doi.org/10.1038/nn.3655
- [M] Gobet et al. (2001) Chunking mechanisms in human learning; Gobet and Simon (1998) template theory (background recall, no URL).
- [M] Chen and Cowan (2005, 2009) and Cowan et al. (2012), via Norris et al. (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7144498/

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 6 established claims: 6 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A08.08-K01** (now single-source: only one opened source, code check).
