# Mental spaces: deep document

*Subfield F01.05, cognitive linguistics. Written from evidence_a-d.jsonl, claims.jsonl (K01-K32) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Evidence ids (a01, c10, d05 ...) point to the jsonl files. Read this first: the founding theory has no experimental numbers. Almost all measured LLM evidence is theory of mind (ToM), not hypothesis separation in problem solving. The only direct mechanistic test is one preprint from one group.*

## 1. What it is

A mental space is a small, temporary, partial structure that a thinker builds on the fly while reading, talking or reasoning. It holds a few elements and the relations among them. It is not a model of the whole world. Examples of spaces: what Max believes, what would be true if it had rained, what the painting shows, what the dream contained, what was true in 1990, what a character knows.

Language and context open spaces with "space builders": "in 1990", "if", "Max believes", "in the picture", "suppose". Each space has its own contents. Elements in different spaces are linked by counterparts ("the real Max" and "Max in the painting"). Reasoning runs inside one space at a time. The base space is the here-and-now reality that other spaces hang from (a01, a02, a05).

Why it matters for our agent: schema state S2 (REPRESENT) writes 1 to 4 candidate rules. The mental-spaces idea says each candidate should live in its own named scope, so that a claim true "under hypothesis H2" is not read as true everywhere. The risk it addresses is leakage: one hypothesis, one distractor or one earlier assumption contaminating another.

Three things this subfield covers:
1. The linguistic theory (Fauconnier, Fauconnier and Turner, Dinsmore).
2. Human processing evidence (eye tracking, event-related potentials, ERP).
3. LLM evidence: do models keep scopes apart, how, and does a scaffold that enforces scopes help.

## 2. History and theories in depth

**Fauconnier 1985 / 1994, Mental Spaces (a01, b21, not opened).** Founding book. Built from linguistic data: referential opacity (the same noun phrase picks out different things in belief and reality), presupposition projection, counterfactual tense, pictures. One general principle, the Access Principle: an element in one space can be reached through its counterpart in another. No experiment. Meaning is built by the process, not stored in sentences.

**Dinsmore 1991, Partitioned Representations (a02, not opened).** An independent AI parallel. Knowledge is split into partitions (belief, fiction, time, hypothesis). The same inference rules run in every partition. What changes is which partition holds the premises. This is the cleanest design match for a scaffold: one rule set, many scoped fact stores.

**Fauconnier and Turner 1998, Conceptual Integration Networks (a03, not opened).** Extends spaces to four-space networks: two input spaces, a generic space, a blended space. Projection from the inputs is selective. Composition, completion and elaboration create emergent structure. About 20 vital relations (Cause-Effect, Analogy, Time, Space, Change, Identity, Part-Whole, Representation) and optimality principles govern it. Fauconnier 2005 (a04, opened) restates it. Worked example: complex numbers as a blend of the real line and 2D space, with a new operation (multiplication by angles) and a statement false in one input and true in the blend.

**Applications by the theory's own lab.** Coulson on sarcasm (a05): two counterfactual spaces (Expected Reaction, Counterfactual Trigger) plus a blend; the main load is tracking counterparts across spaces; making the spaces salient (an echo) makes irony easier. Coulson and Pascuale on persuasion (a06): corpus of real rhetoric; blends are constrained by frames and community, not only formal principles. Brone on humour (a08): layered viewpoint spaces explain hyper-understanding and misunderstanding. All qualitative, no counts (K26).

**Computational models.** Veale, O'Donoghue and Keane 2000 (a07): Sapper, spreading activation over a semantic network, builds bridges between spaces. Algorithmic, no benchmark numbers. Andreas 2022 (a26, snippet): LMs infer a model of the agent who wrote the text, so they act as if holding beliefs scoped to that agent.

**Competing views.** Formal semantics treats belief as a special, distinct kind of context. Fauconnier treats all spaces under one principle. Steele et al. 2026 find a coarse shared taxonomy and little special status for belief (c07, K25, contested). Blending theory is also criticised as hard to falsify; a 2026 paper (d19) is conceptual only and no measured LLM blending gain was found (K31).

**Honest status.** The theory gives design vocabulary: scope, space builder, counterpart, base space, open and close. It does not give effect sizes. Every effect number in this document comes from experiments in neighbouring areas (ToM, counterfactuals, entity tracking, distractors).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| 3B open LLMs keep actual and alternative value for a non-actual space; both decodable after intervening text | base 0.96 [0.95,0.97], alternative 0.94 [0.94,0.95], n=240 per seed, chance 0.25 | Steele et al. 2026 (a11, c02) | [S] K01 |
| A space-index subspace trained on one space type controls others | transfer index Qwen 0.73 CI [0.67,0.78] (lower bound under the 0.7 bar), Pythia 0.885 [0.882,0.889], Falcon3 0.711 [0.662,0.741]; within-class 0.89-0.92 vs between-class 0.53-0.76 | Steele (a11, c01) | [S] K02 |
| Binding IDs control which value attaches to which entity | >99% control, <3% after one swap, >97% after double swap | Feng and Steinhardt 2024 (b12, c22) | [E] with Steele, K02 |
| Report and use are causally separate | colour subspace flip: report 1.00, rule result 0.00; consequent subspace flip: rule 1.00, report 0.32; principal cosine 0.11 / 0.17 | Steele (a13, c05) | [S] K04 |
| Binding is retrieval-shaped: distractor colours decode at target token | advantage +0.07 Qwen, +0.09 Pythia; about 0 after about 16 filler sentences | Steele (c03) | [S] K03 |
| Frontier models hold up to 8 stated bindings with no swaps; derived inference under load is hard | Llama-8B 0.31 on the harder derived task | Steele (a14, c08) | [S] K05 |
| Hand-built steering equals random; learned subspace works | diff-of-means 0.583 vs random 0.583; DAS rank-1 0.883 (one seed), 0.96 [0.88,1.00] over 3 seeds, rank-4 1.000 | Steele (a12, c04) | [S] K06 |
| Nested spaces compose; time spaces transfer | future flip 0.81 / 0.90 / 0.83; past-present 0.90 vs floor 0.03 | Steele (c06) | [S] |
| Belief not special | belief transfer above between-class baseline by +0.08 / +0.03 / +0.09; 14B belief 0.74/0.79, counterfactual 0.33/0.86 | Steele (c07) | [C] K25 |
| Perspective filter before answering (SimToM), ToMi false belief | GPT-4 25.5 zero-shot / 74.25 CoT / 87.75 SimToM; GPT-3.5 67.25 / 34.0 / 81.0; oracle perspective 96 | Wilf et al. 2023 (a17, c10) | [S] K07 |
| SimToM, BigToM false belief | GPT-3.5 41.0 / 56.25 / 70.5 | (c12) | [S] |
| SimToM needs two steps | one-call merge: GPT-3.5 81.0 to 58.75; generic reasoning instead of filter: 31.75 | (c11) | [S] K08 |
| Per-agent belief graphs (SymbolicToM) | LLaMA-7B depth 1/2/3: 99/92/88; GPT-3 davinci +38 to 92% avg; Flan-T5-XL +62 first-order FB; GPT-3.5 +78 second-order FB; third-order about 9% to 100%; paraphrase: supervised TTT -54, finetuned GPT-3 about -40 | Sclar et al. 2023 (a18, b14, b15, c13) | [S] K09 |
| Scoped weighted per-agent hypotheses (thought-tracing) | GPT-4o ParaphrasedToMi 59.5 plain / 67.0 CoT / 76.0 TT; MMToM-QA GPT-4o+TT+CoT 69.0 = o3-mini-medium 69.0 at under half the tokens (authors' statement) | Kim et al. 2025 (d10, d11) | [S] K27 |
| Thought-tracing ablation: drop perception-inference step | -7 to -20 points | (d12) | [S] |
| Scoped beats shared across three methods, same direction | see rows above | a17, a18, d10 | [E] K10 (principle only) |
| False-belief success is brittle | GPT-3.5 flipped by transparent or relabelled container; some models 66.7 to 0 on transparent access; Kosinski: GPT-4 solves 75% of 40 tasks | Ullman, Shapira, Kosinski (a20, b16-b18) | [C] K11 |
| 2025-26 reasoning models pass most altered tasks but still score 0 on transparent-container and relationship-change variants | Claude thinking, Grok-3-mini, R1 score 0; GPT-5-high 0.5 on one; two items per cell | de Haan et al. 2026 (d07, d08) | [S] K29 |
| Cross-question consistency collapses (FANToM, short context, All metric) | GPT-4 0613 + CoT All 26.6, All* 18.4; Oct GPT-4 All 14.8 (All* 6.8); human 87.5 | Kim et al. 2023 (a21, c14, c15) | [S] K12 |
| Nesting depth hurts | Hi-ToM GPT-4-32k 60.42 standard, 64.04 CoT; HiToM order 0 to 4: o3 0.996 to 0.467, DeepSeek-V3 0.979 to 0.608, R1 0.988 to 0.196; Hanabi second order costs 10-20 points (R1 87.05 to 68.31, Llama-8B 61.98 to 20.71) | c16, c17, d05, d13 | [C] K13 |
| Reasoning models do not reliably beat non-reasoning on scoped belief | HiToM overall o3 0.747, DeepSeek-V3 0.694, R1 0.549, Qwen3-8B-Reasoning 0.481 vs Qwen3-8B 0.558; no options: R1 0.549 to 0.691; 1,500-token cap: Qwen3-8B-Reasoning 0.706; o1 true-belief 36-49% | d04, d06 | [E] K28 |
| RL on belief tracking | Hi-ToM N=600: Qwen2.5-7B 52.17 to 83.33; 3B 39.17 to 81.17; held-out order 4: 7B-1M 17.83 to 94.50 vs DeepSeek-V3 58.67, GPT-4o 46.17 | d09 | [S] |
| Backward belief much worse than forward | GPT-4 0-shot forward belief .97, forward action .79, backward belief .40; humans about 82% / 72% (20 participants); Mistral-7B backward .40 even with steering | Gandhi 2023 (c18); Zhu 2024 (d02) | [S] K14 |
| Weak counterfactual switching in old models | right in both conditions: GPT-2 18.8, GPT-3 50.0, BERT 9.4, RoBERTa 31.3, MPNet 28.1 (chance 25); counterfactual-only preference BERT 53.1, RoBERTa 68.8, MPNet 46.9 | Li, Yu, Ettinger 2023 (a22, b03) | [S] K15 |
| Counterfactual rule changes cost accuracy | GPT-4 two-digit addition: base 10 100.0, base 8 82.3, base 16 63.0, base 11 38.4, base 9 23.4; CoT 38.6 / 56.5 for bases 9 / 11 | Wu et al. 2024 (a23, b06, c21) | [S] K16 |
| Entity-state tracking depends on code pretraining; inflated by trivial cases | 62.7% of Alchemy states equal initial; probe 86.8% trivial vs 3.1% non-trivial; failure above 25% after 7 operations | Kim and Schuster 2023 (a16, b09, c23); Li et al. 2021 (a15: T5 probe 14.3% Alchemy, 53.8% TextWorld) | [E] K19 |
| Belief tracking circuit exists | probe >80% (Mistral-7B); circuit restores >=88% of fine-tuned performance | Zhu (a19), Prakash (b11, c25) | [E] K20 |
| Irrelevant context leaks | under 30% of base problems solved consistently with one irrelevant sentence (GSM-IC); S2A: LLaMA-2-70B factual QA 62.8 to 80.3, GSM-IC in-topic 51.7 to 61.3 | Shi 2023 (a24, b19); Weston and Sukhbaatar (a25) | [E] K21 |
| Evidence order swings results | over 5 points generally, over 30 for PaLM2 and Llama2-7B | Xie et al. 2024 (b20) | [S] K22 |
| Multiple hypotheses tested separately (ARC 100 subset) | direct 17%, abstract hypotheses 23%, LLM-summarised 30%, human-selected 33% | Wang et al. 2024 (c26) | [S] K23 |
| Multi-turn lock-in | -39% average single-turn to multi-turn, six tasks, 200,000+ conversations | Laban et al. 2025 (d14) | [S] K32 |
| Humans: counterfactual mood costs a little | N400 +0.72 microvolt, N=30, F(1,22)=8.44, eta-sq .28; switching back N=48 early interference then recovery; Coulson and Van Petten N=18 | d15-d18 | [E] K17, K30 |

## 4. Mechanisms and models

### 4.1 Inside the model (what the mechanistic papers say)

1. **Binding IDs (Feng and Steinhardt, b12).** The model gives each entity-attribute pair a low-dimensional "binding ID" vector. The entity and its attribute carry the same ID. At query time, the entity's ID is used to look up the attribute. Swap the IDs and the answer swaps: >99% control, <3% after one swap, >97% after a double swap. Engineer's view: the model does an associative lookup, key = ID, value = attribute.
2. **Space index (Steele et al., a11, c01).** A low-rank subspace tags which space a value belongs to (actual vs painting vs belief vs dream vs past vs hypothetical). One value in the actual slot, one in the alternative slot, both decodable. A subspace trained on one type steers others (transfer 0.71-0.89). Builders compose (a painting inside a belief gets a new router over the shared slot).
3. **Retrieval, not storage (c03).** The binding is rebuilt at the query token. Distractor entity colours still decode there (+0.07 / +0.09). The effect fades by about 16 filler sentences. So distance and interleaving matter, and re-stating state near the query should help.
4. **Report is not use (a13, c05).** The subspace that makes the model say a value is not the subspace that makes a rule consume it (cosines 0.11 / 0.17). Changing one leaves the other. A model can state a space's contents and still apply the wrong one in a derived step.
5. **Belief lookbacks (Prakash, c25).** Three steps: bind character and object ordering IDs to state; retrieve the answer; a visibility lookback that updates an observer's beliefs. Layer ranges roughly 10-31 (visibility), 20-38 (binding), 34-56 (answer) in Llama-3-70B/405B and Qwen2.5-14B. Zhu et al. find belief status linearly decodable in mid-layer heads (a19).
6. **Entity tracking (Kim and Schuster, a16; Li et al., a15).** State is linearly readable and editable, but incomplete (T5 14.3% of Alchemy states). Code in pretraining is the main enabler.

Caveat: most of this is 3B-and-under models on synthetic colour stimuli, from one group. It tells us scopes exist as vectors. It does not tell us that a prompt scaffold helps.

### 4.2 Scaffold-level methods (implementable now)

**A. Perspective filter, two calls (SimToM, a17).**
```
call 1: given STORY and AGENT X, rewrite the story keeping only events X witnessed or was told.
call 2: answer QUESTION using ONLY the filtered story.
```
Ablations: merged into one call 81.0 -> 58.75 (GPT-3.5 ToMi FB); generic reasoning replacing the filter 31.75. The separation of scope building from answering is the active ingredient. Oracle filter: 96.

**B. Per-agent belief store, built by code (SymbolicToM, a18).**
```
state = { agent: set of facts, nested_agent[a][b]: set of facts }  # depth <= 2-3
for each story event e:
    witnesses = who saw e
    for a in witnesses: state[a].add(e)
    for a,b in witnesses: state[a][b].add(e)   # a knows b saw it
query(agent A, B): pass only state[A][B] sub-graph to the model
```
Gains are large and survive paraphrase (LLaMA-7B 99/92/88 at depths 1/2/3). The program does the scoping; the model answers from the narrowed context.

**C. Weighted hypotheses per agent (thought-tracing, d10).**
```
for each new observation o:
    for each agent a: infer what a perceived from o; update a list of (hypothesis, weight) for a's state
answer using the top-weighted hypothesis for the asked agent
```
GPT-4o ToMi 59.5 / 67.0 / 76.0. The perception-inference step carries the effect (-7 to -20 points when removed). It hurt on some true-belief items, so control items are needed.

**D. Context filtering (S2A, a25).** Regenerate the context keeping only relevant parts, then answer. LLaMA-2-70B factual QA 62.8 -> 80.3.

**E. Explicit space stack (untested).** Written stack of open spaces, each with a name, its rules, and its base-state pointer; open and close are explicit steps; on close restate the base state. Design guess from human data (cost at entering and leaving a space, K30) and the Hi-ToM skipped-step errors (K13). Not measured for LLMs.

**F. Cap deliberation.** Reasoning models over-assume false belief and lose from long chains on scoped belief (K28): a 1,500-token cap lifted Qwen3-8B-Reasoning to 0.706.

### 4.3 Human processing model

Humans open a counterfactual or false-belief space quickly and use it predictively (b01, b02). Real-world knowledge still leaks a little: N400 cost 0.72 microvolt for world-true words in a counterfactual antecedent (d16). On switching back to the factual world there is early interference then recovery (d17). Design translation: leakage sits at the boundaries, so make boundaries explicit.

## 5. What holds up

**Replications and independent agreement.**
- Scoped context beats shared context on belief tasks: three methods (SimToM, SymbolicToM, thought-tracing) all in the same direction. Strong on the principle, but no two share a protocol, and all use ToM tasks [E for principle].
- Binding by ID vectors: Feng and Steinhardt and Steele et al. agree on mechanism type; Zhu, Prakash and Bortoletto show belief representations are linear and structured. [E that scoped belief representations exist].
- Distractor leakage: GSM-IC and S2A agree [E].
- Reasoning models do not reliably improve scoped belief tracking: two independent comparison sets (d04, d11) [E].
- Entity tracking: Kim and Schuster and Li et al. agree on code pretraining and on inflated trivial-case headlines [E].
- Human data: three ERP/eye-tracking sources agree leakage is small and boundary-located [E].

**Failures and contradictions.**
- ToM brittleness [C]. Ullman and Shapira show failures on trivial alterations; Kosinski shows 75% success. Both hold; different variants. 2026 reasoning models pass most altered items yet still score 0 on transparent-container and relationship-change variants (d07, d08, two items per cell).
- Nesting depth [C]. Steele reports no bleed in shallow nests at ceiling. Hi-ToM and HiToM show collapse at order 4 for most models (R1 0.196, o3 0.467). Different tasks.
- Belief special or not [C]. One group says not special; formal semantics says special. No independent replication.
- Behaviour versus decoding: no bleed in frontier behaviour (a14) versus bleed in 3B decoding (c03). Different levels.
- Ferguson and Sanford: real-world violations still cause early difficulty regardless of context (b01), against the claim of fully separate worlds.
- Thought-tracing was uneven: Qwen2.5-72B no FANToM gain from TT alone; TT+CoT hurt GPT-4o and Gemini on true-belief ToMi items.
- SimToM: GPT-3.5 zero-shot (67.25) beats its own CoT (34.0) on ToMi FB. CoT is not a safe control.

**Moderators.** Model size and code pretraining (K19). Depth of nesting. Distance and filler (about 16 sentences). Evidence order (over 30 points for PaLM2, Llama2-7B). Prompt wording (d03). Answer options (R1 0.549 to 0.691 without options). Reasoning length. One-shot prompting helps; zero-shot CoT does not (c19). Commonness of the counterfactual (Wu: smaller gap for common ones).

**Interventions that worked.** Perspective filter (two calls); per-agent belief graph with sub-graph passing; weighted per-agent hypotheses; S2A context regeneration; RL on belief tracking (order 4 17.83 to 94.50 for 7B-1M); capping tokens; removing answer options; learned low-rank steering (3B, research only).

**Interventions that did not work.** Hand-built diff-of-means steering (equals random 0.583). Zero-shot CoT on backward belief. Generic reasoning in place of perspective filtering (31.75). Merging filter and answer into one call. Extra reasoning for scoped belief (reasoning models not better). Steering for backward belief (Mistral-7B 0.40).

**Evidence quality problems.** No equal-token comparison anywhere (SimToM uses two calls, SymbolicToM uses code). 2022-2023 models for SimToM and SymbolicToM; no re-test with current reasoning models. The HiToM comparison paper gives no N or token costs. de Haan et al. use two items per cell. Steele is a single preprint (2026-07-11). Human effect sizes missing for Ferguson (b01, b02) and Nieuwland and Martin (d15).

## 6. Language models

**What models do on tasks that need scopes.**
- Older models (GPT-2/3, BERT family) barely switch into counterfactual spaces: 9.4-50% right in both conditions (chance 25), most follow lexical triggers (a22). GPT-4 under altered rules loses much: base 9 at 23.4 versus base 10 at 100.0 (a23). Do not generalise these numbers to 2025-26 models; no re-run was found.
- Classic false belief is near ceiling for reasoning models (d07). Higher-order and altered scenes are not. HiToM: o3 0.996 at order 0 down to 0.467 at order 4; R1 0.988 to 0.196; DeepSeek-V3 0.979 to 0.608 (d05).
- Consistency across question types remains low: FANToM short context GPT-4 All 26.6, All* 18.4, versus 87.5 for humans (a21). CoT trades inclusion errors for exclusion errors.
- Backward inference is the weak direction: .40 for GPT-4 0-shot; Mistral-7B .40 even after steering (c18, d02).
- Stated bindings are easy, derivations are hard (a14, c08).
- Multi-turn use loses 39% on average from lock-in of early assumptions (d14).

**What changed performance, by how much.**

| Change | Effect | Source |
|---|---|---|
| Perspective filter, two calls | GPT-4 ToMi FB 74.25 (CoT) to 87.75 | c10 |
| Per-agent belief sub-graph | LLaMA-7B depth 1/2/3 99/92/88 | c13 |
| Weighted per-agent hypotheses | GPT-4o ToMi 67.0 to 76.0 | d10 |
| Context regeneration (S2A) | LLaMA-2-70B 62.8 to 80.3 | a25 |
| RL on belief tracking | Hi-ToM overall Qwen2.5-7B 52.17 to 83.33 | d09 |
| Token cap 1,500 | Qwen3-8B-Reasoning 0.481 to 0.706 | d06 |
| Remove answer options | R1 0.549 to 0.691 | d06 |
| One-shot example | helps consistently; zero-shot CoT does not | c19 |
| Reasoning model instead of plain | no reliable gain (o3 0.747 vs DeepSeek-V3 0.694) | d04 |

**The scaffold versus reasoning-model question.** Thought-tracing with a non-reasoning model matched o3-mini-medium on MMToM-QA at 69.0 with under half the tokens (authors' statement; token counts are in a figure, not tabulated) [S, d11]. This is the closest thing to an equal-cost comparison. It is not a flat-list control.

**Gaps.** No study tested a Fauconnier-style space scaffold for hypothesis separation in problem solving (K24, b23). No current-model re-run of SimToM or SymbolicToM. No test of blending as a prompt method with a measured gain (K31).

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence | What to add |
|---|---|---|---|---|
| Written state tags every claim with the space it belongs to (hypothesis name, source, scope); a fact is used only in its space | S2 | [E] for the principle | a17, a18, d10 (K10); b12, c01 (K02); a19, c25 (K20) | Each hypothesis from S2 gets a named block with its own facts and consequences. Code, not the model, decides which block is shown to a given step. |
| Filter irrelevant or out-of-scope context before answering, counted in the token budget | S1/S2, G7 | [E] | a24, a25, b19 (K21) | S1 input hygiene already moves suggestive material to a marked block; keep it and charge any filter call to the budget. |
| Track entity state in a written table updated per operation; do not recompute from the story each time | S2/memory | [E] | a15, a16, b09, c23 (K19) | State table updated by code where possible; vary operations in tests because accuracy falls with their number. |
| Cap deliberation on scoped-belief steps; add true-belief and shared-knowledge control items | G11, O | [E] | d04, d06, d11 (K28) | Short chains in scoped states; always include controls so over-separation shows. |
| Judge scope changes on perturbed variants, not canonical items only | G3 | [C] but cheap | a20, b16, d07, d08 (K11) | Evaluation rule for the bench, not a runtime state. |

Note: "tag each claim with its space" is established as a principle (three methods agree, mechanism exists), but no study measured a hypothesis-space tag in a problem-solving scaffold at equal tokens. Treat the exact format as Test first (T1). Space open/close as explicit steps rests on human data (K30, [E] for humans) and is a design guess for LLMs, so it is in Test first.

### Test first

| Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|
| Scoped hypothesis blocks versus flat hypothesis list at equal tokens, multi-hypothesis non-ToM tasks | S2 | [S] | K23, K24, K27 (c26, d10) | No direct study. Gain from scoped spaces in strong models may be small for plain stated bindings (K05). |
| Two-call perspective filter versus single-call CoT at matched total tokens, current models | S2 | [S] | a17, c10, c11 (K07, K08) | 2023 models; no token match. |
| Per-agent or per-hypothesis belief list with answer only from the matching list | S2 | [S] | a18, c13 (K09) | 2023 models, code scaffold; cost not matched. |
| Explicit written stack for nested spaces (order 3-4) | S2 | [S]/[C] | c16, d05, d09 (K13) | Depth collapse is real, a written stack was never tested. |
| Explicit open and close of each space with base restatement on close | S2 | [E] humans, design guess for LLMs | d15-d17 (K30) | No LLM test. |
| Separate "stated contents" and "derived consequence" questions with a consistency check | S2/O | [S] | a13, c05, a21 (K04, K12) | Mechanism is from 3B synthetic tasks. |
| Restate base state per space before each query versus once at the top | S2/G | [S] | c03 (K03) | One group; 3B models. |
| Restate the hypothetical space's rules before each step | G | [S] | a23, b06 (K16) | GPT-4 era. |
| Visibility check inside each scope for altered scenes | S2 | [S] | d07, d08 (K29) | Two items per cell. |
| Perception-inference ("what did they perceive") step first on backward items | S2 | [S] | c18, d02, d12 (K14) | No prompt-level test on 2025-26 models. |
| One uniform space tag versus type-specific tags | S2 | [C] | c07, d01 (K25) | One group. |
| Shuffle order of hypothesis spaces to measure variance | G | [S] | b20 (K22) | Order effects reported for older models. |
| Reset or restate scoped state each turn in multi-turn use | S2/memory | [S] | d14 (K32) | Indirect evidence only. |

Not to add: a blend operator (K31, SCHEMA 4b); activation steering (K06, not a prompt-level method).

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (count all calls, filter calls and state rewrites in the budget). Report accuracy with a 95% interval and the per-item token count. Include control items where over-separation would show.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Multi-hypothesis tasks from our bench (ARC portfolio is the honest control; BRAINTEASER where several candidate readings coexist) | A: flat hypothesis list in the state. B: one named block per hypothesis with its facts and predicted outputs; code shows only the active block | Accuracy; rate of cross-hypothesis errors (a claim from H2 cited under H1) | Small to moderate gain (a few points); more on derived-inference items than on stated ones (K05) |
| T2 | False-belief and multi-agent knowledge items (ToMi, BigToM style, plus a few altered scenes) | A: single-call CoT. B: filter-then-answer. Total tokens matched by capping A's CoT at B's two-call total | Accuracy; true-belief control accuracy | B up if the gain survives current models; a flat result would say current models absorbed it (d07) |
| T3 | Same items, orders 1-4 | A: free CoT. B: explicit written stack of nested spaces | Accuracy per order | Larger gain at order 3-4 than 1-2; no loss at order 0 |
| T4 | Items with one irrelevant or out-of-scope sentence (GSM-IC style) | A: single pass. B: filter call then answer, filter charged | Consistency over base problems | Gain like S2A (+10 to +17 points for older models); smaller for strong current models |
| T5 | Derived-inference items under hypothetical rules (changed-base arithmetic, "if rule X then") | A: plain. B: restate space rules before each step. C: separate stated-contents and derived-consequence questions with a consistency check | Accuracy; disagreement rate between stated and derived | B and C help on derivation-heavy items; no effect on stated lookups |
| T6 | Interleaved two-space items with filler of 0, 8, 16, 32 sentences | A: state at top only. B: restate relevant space before the query | Cross-space error rate vs filler length | Error grows with filler in A; flat in B (c03) |
| T7 | Backward items (infer the earlier percept from action) | A: plain CoT. B: first open a "what did they perceive" space | Accuracy | Gain if the perception step matters as in d12 |
| T8 | Space open/close items (counterfactual then back to fact) | A: free. B: explicit open and close steps with base restatement | Accuracy on the post-close fact question | Fewer carry-over errors in B |
| T9 | Order and tag format | A: fixed order. B: shuffled order. C: uniform tag vs type-specific tag | Variance across shuffles; accuracy | Variance estimate; tag format likely no difference (K25) |
| T10 | Multi-turn items (3-6 turns) | A: carry conversation. B: restate scoped state each turn | Accuracy by turn | B recovers some of the lock-in loss (d14) |

Rule for any of these: also run the plain model with a larger token allowance, since G11 says extra thinking can hurt and G7 says the scaffold must pay for itself.

## 9. What does not transfer, and why

- **Activation-level results (K06, a12).** Steering vectors and subspace edits need weights access. Our agent is a prompt scaffold. The finding that hand-built directions equal random says nothing about prompts.
- **3B-model mechanisms.** Binding retrieval and the report-versus-use gap were found in models of 3B and under on synthetic colour stimuli. Frontier models do stated bindings at ceiling (a14). The mechanisms suggest design, not magnitude.
- **ToM numbers as proof for hypothesis separation.** SimToM, SymbolicToM, thought-tracing and the rest test who-knows-what. S2 wants hypothesis-by-hypothesis separation. The principle is shared (scoped context), the effect sizes are not.
- **2022-2023 model numbers.** SimToM (GPT-4 25.5 to 87.75), SymbolicToM (GPT-3.5 +78) and Li et al.'s counterfactual weakness use models far weaker than the ones we run. Expect smaller gains.
- **Blending (K31, K18).** Four-space integration networks are descriptive. No measured prompt gain. SCHEMA 4b already says not to add.
- **Human ERP and eye-tracking.** The data show where leakage sits (boundaries), not how to prompt. The blend work is from the theory's own lab, with N=18 and no amplitudes.
- **Code-built belief graphs (SymbolicToM).** Need a parser that turns the task into events and witnesses. On open problems there are no clean events. Usable only where our program already structures the input.
- **RL fixes (d09).** Training is outside this project's premise.
- **Theory claims about linguistic phenomena** (presupposition, opacity, tense). No LLM-agent counterpart tested.

## 10. Open questions

1. Does separate scoped hypothesis state beat a flat shared notes state on non-ToM multi-hypothesis reasoning at equal tokens with a current model? No study found (K24).
2. Do SimToM and SymbolicToM gains survive current reasoning models when extra calls are charged to the budget?
3. Does leakage between spaces grow with context length or number of spaces in frontier models doing derived inference? Only indirect evidence (K32).
4. Does a prompt step "apply the rule inside space X" close the report-versus-use gap outside 3B synthetic tasks (K04)?
5. Do counterfactual-rule penalties (GPT-4 base 9 at 23.4) shrink for 2025-26 reasoning models, and does restating the rules help (K16)?
6. Is belief-not-special replicated by an independent group (K25)? Does it change whether we need separate tags for belief, supposition and fiction?
7. Human effect sizes for Ferguson and Sanford 2008, Ferguson et al. 2010 and Nieuwland and Martin 2012 are not extracted.
8. Does an explicit written stack fix the order 3-4 collapse (K13)?
9. Any measured gain from blending as a prompting method (K31)?
10. Does a hypothesis-first step help backward inference for 2025-26 models (K14)?
11. Do scoped spaces over-separate: do they hurt true-belief and shared-knowledge items (K27, K28)?
12. What does the Steele companion belief paper (c09, not opened) show?

## 11. Sources

[V] = opened and read (full text, or the abstract page where noted). [M] = snippet or abstract only, or recalled.

- [M] Fauconnier (1985/1994) Mental Spaces. https://www.cambridge.org/core/books/mental-spaces/990994C4CD82B3F34DAB8504 (a01, b21)
- [M] Dinsmore (1991) Partitioned Representations. https://www.philpapers.org/rec/FAUMSA (a02)
- [M] Fauconnier and Turner (1998) Conceptual Integration Networks. https://dblp.org/rec/journals/cogsci/FauconnierT98.html (a03)
- [V] Fauconnier (2005) Compression and Emergent Structure. https://pages.ucsd.edu/~scoulson/spaces/fauconnier05.pdf (a04)
- [V] Coulson (2005) Sarcasm and the Space Structuring Model. https://pages.ucsd.edu/~scoulson/spaces/coulson-sarc.pdf (a05)
- [V] Coulson and Pascuale (c. 2008) For the sake of argument. https://pages.ucsd.edu/~scoulson/spaces/coulson-pascuale.pdf (a06)
- [V] Veale, O'Donoghue and Keane (2000) Computation and Blending. https://mural.maynoothuniversity.ie/id/eprint/8182/1/DOD-Computation-2000.pdf (a07)
- [V] Brone (c. 2008) Hyper- and misunderstanding in interactional humor. https://pages.ucsd.edu/~scoulson/spaces/Brone.PDF (a08)
- [M] Coulson and Van Petten (2002) ERP study of conceptual integration and metaphor. https://link.springer.com/article/10.3758/BF03195784 (a09); abstract page [V] https://pubmed.ncbi.nlm.nih.gov/12450098/ (d18)
- [M] Coulson (2001) Semantic Leaps. https://doi.org/10.1017/CBO9780511551352 (a10)
- [V] Steele, Wen and Han (2026) One mechanism for many mental spaces. https://arxiv.org/abs/2607.10248 ; data https://huggingface.co/datasets/osteele/mental-spaces (a11-a14, c01-c08, d01)
- [M] Steele et al. companion paper on belief in mental spaces (c09), cited by the main paper only.
- [V] Li, Nye and Andreas (2021) Implicit representations of meaning. https://arxiv.org/abs/2106.00737 (a15, c24)
- [V] Kim and Schuster (2023) Entity Tracking in Language Models. https://arxiv.org/abs/2305.02363 (a16, b09, b10, c23)
- [V] Wilf et al. (2023) Think Twice (SimToM). https://arxiv.org/abs/2311.10227 (a17, c10-c12)
- [V] Sclar et al. (2023) SymbolicToM. https://arxiv.org/abs/2306.00924 (a18, b14, b15, c13)
- [V] Zhu, Zhang and Wang (2024) Language Models Represent Beliefs of Self and Others. https://arxiv.org/abs/2402.18496 (a19, b13, d02)
- [V] Ullman (2023) LLMs fail on trivial alterations to ToM tasks. https://arxiv.org/abs/2302.08399 (a20, b16, c20)
- [V] Kim et al. (2023) FANToM. https://arxiv.org/abs/2310.15421 (a21, c14, c15)
- [V] Li, Yu and Ettinger (2023) Counterfactual reasoning. https://arxiv.org/abs/2305.16572 (a22, b03-b05)
- [V] Wu et al. (2024) Reasoning or Reciting. https://arxiv.org/abs/2307.02477 (a23, b06-b08, c21)
- [V] Shi et al. (2023) LLMs can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 (a24, b19)
- [V] Weston and Sukhbaatar (2023) System 2 Attention. https://arxiv.org/abs/2311.11829 (a25)
- [M] Andreas (2022) Language Models as Agent Models. https://arxiv.org/abs/2212.01681 (a26)
- [V] Ferguson and Sanford (2008) Anomalies in real and counterfactual worlds. https://kar.kent.ac.uk/23060/ (b01; abstract only, no N)
- [V] Ferguson, Scheepers and Sanford (2010) Expectations in counterfactual and theory of mind contexts. https://kar.kent.ac.uk/23062/ (b02; abstract only, no N)
- [V] Prakash et al. (2024) Fine-tuning enhances existing mechanisms. https://arxiv.org/abs/2402.14811 (b11)
- [V] Feng and Steinhardt (2024) How do language models bind entities in context? https://arxiv.org/abs/2310.17191 (b12, c22)
- [V] Shapira et al. (2023) Clever Hans or neural theory of mind? https://arxiv.org/abs/2305.14763 (b17)
- [V] Kosinski (2024) Evaluating LLMs in theory of mind tasks. https://arxiv.org/abs/2302.02083 (b18)
- [V] Xie et al. (2024) Adaptive chameleon or stubborn sloth. https://arxiv.org/abs/2305.13300 (b20)
- [M] Nieuwland and Martin (2012) If the real world were irrelevant, so to speak. https://pubmed.ncbi.nlm.nih.gov/21962826/ (b22; d15 is the abstract page)
- [V] Wu et al. (2023) Hi-ToM. https://arxiv.org/abs/2310.16755 (c16, c17)
- [V] Gandhi et al. (2023) Understanding social reasoning in language models with language models. https://arxiv.org/abs/2306.15448 (c18, c19)
- [V] Prakash et al. (2025) Language Models Use Lookbacks to Track Beliefs. https://arxiv.org/abs/2505.14685 (c25)
- [V] Wang et al. (2024) Hypothesis Search. https://arxiv.org/abs/2309.05660 (c26)
- [M] Bortoletto et al. (2024) Brittle Minds, Fixable Activations. https://arxiv.org/abs/2406.17513 (d03; abstract page)
- [V] To Think or Not to Think (2026), ToM with reasoning models. https://arxiv.org/html/2602.10625v1 (d04-d06)
- [V] de Haan, van der Putten and van Duijn (2026) Reasoning Promotes Robustness in Theory of Mind. https://arxiv.org/abs/2601.16853 (d07, d08)
- [V] Rule-based RL for ToM (2025). https://arxiv.org/html/2504.01698v2 (d09)
- [V] Kim et al. (2025) Hypothesis-Driven Theory-of-Mind Reasoning (thought-tracing). https://arxiv.org/abs/2502.11881 (d10-d12)
- [V] Liang et al. (2025) LLM-Hanabi. https://arxiv.org/html/2510.04980v1 (d13)
- [M] Laban et al. (2025) LLMs Get Lost In Multi-Turn Conversation. https://arxiv.org/abs/2505.06120 (d14; abstract page)
- [V] Kulakova and Nieuwland (2016) Pragmatic skills predict online counterfactual comprehension. https://doi.org/10.3758/s13415-016-0433-4 (d16)
- [V] Autistic adults and counterfactual maintenance and switching (2022). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8732958/ (d17)
- [V] Lynn (2026) Conceptual blending in humans and language models. https://doi.org/10.3389/fpsyg.2026.1849083 (d19)
