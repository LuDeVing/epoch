# Analogical access (retrieval): deep document

*Subfield A11.03. Written from `evidence_a.jsonl` to `evidence_d.jsonl` (ids a01 to d21), `claims.jsonl` (A11.03-K01 to K27) and `critique.md` in this folder. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. "Opened" means the page or PDF text was read in this run. Several human-side numbers come from restatements, and the document says so where it matters.*

---

## 1. What it is

Analogical access is the step before analogy is used. A person (or a model) holds a problem. Somewhere in memory sits a solved problem with the same deep structure. Access is whether that stored case comes to mind at all.

Analogy has three steps. They fail in different ways.

| Step | Question | Where it fails |
|---|---|---|
| Access (retrieval) | Does the useful stored case come to mind? | Most often. Surface content decides what is recalled. |
| Mapping | Which part of the old case matches which part of the new one? | Second most often, even after a hint. |
| Transfer or adaptation | Can the old solution be changed to fit and then checked? | Less studied; the model copies details that do not fit. |

The core fact of the field is a dissociation. People judge structural matches as the best sources of inference. The same people fail to retrieve those matches, because retrieval follows shared objects and surface words. The stored case is in memory. The cue does not reach it.

For our agent this matters in three places:

1. **Memory** (SCHEMA section 5). The planned subgoal library will hold solved subgoals. A lookup that finds only wording-near cases will not return the cases that help at an impasse.
2. **O7 Map an analogue.** O7 needs a source. Someone has to find it. This subfield says how it is found, and how often the find is wrong.
3. **G1 and S6.** In people the fix for failed access is a cue. A cue at an impasse is cheap and fires only on a failure signal. That fits G1.

Scope. This document covers human access (Gick and Holyoak, Gentner and colleagues), the MAC/FAC model and its rivals, what improves access in people, and what is known about language models: analogical prompting, retrieval by structure versus embeddings, and agent memory systems. Schema induction is a parallel subfield; library learning, chunking and quality-diversity are others. This document only notes the links.

---

## 2. History and theories in depth

### 2.1 The radiation problem (Duncker, then Gick and Holyoak)

Duncker's tumour (radiation) problem: a ray strong enough to kill a tumour also kills the healthy tissue it passes through. The answer is to fire weak rays from many directions that converge on the tumour. Few people find this unaided.

Gick and Holyoak (1980, 1983) gave people a story first. In the fortress story a general splits his army to converge on a fortress by several roads. Then they gave the tumour problem. Standard figures across their experiments (a01, a04, b13; restated, not from the 1980 primary):

- About 10 percent solve with no story.
- About 20 to 30 percent solve after reading the story, with no hint.
- About 75 to 80 percent solve once told "the story may help".

The jump from 20-30 to 75 percent after a bare hint is the key result. The story was stored and usable. It was not noticed. So the failure is access, not storage and not mapping. The critique warns that the no-hint rate varies by experiment (10 to 43 percent in restatements, d21). Use ranges, not one number. Gick and Holyoak's own account of the few who noticed: prior knowledge, demand effects, and chance abstract encoding of the story (a04).

### 2.2 Surface versus structure at access

- **Holyoak and Koh (1987).** A lightbulb-filament story and the radiation problem, with surface and structural similarity varied. Both kinds aid spontaneous transfer. The slide-deck restatement (b14, not the paper) gives before-hint rates of 69, 38, 33 and 13 percent as both similarities are removed, and after-hint rates of 75, 81, 60, 47. The summary reading: surface and structure matter about equally at access, structure matters most at mapping (b15).
- **Ross (1984, 1989), Novick (1988), Reed.** Story-line similarity changes the chance of accessing an earlier problem but not the chance of using its principle correctly once accessed (a09, restated). Experts retrieve structural matches more and reject surface lures faster (a14, restated).
- **Gentner, Rattermann and Forbus (1993).** The decisive study (a05 to a08, opened). Same story sets in two tasks. When rating inference soundness, people use relational structure. When cued from memory a week later, they recall by surface. Details in section 3.

### 2.3 Models of retrieval

**MAC/FAC** (Forbus, Gentner and Law 1995; a10 to a16). "Many are called, few are chosen." Stage one (MAC) is a cheap dot product between content vectors, which are counts of each predicate in a case. Stage two (FAC) runs full structure mapping on the few survivors. The model reproduces the human order: literal similarity > surface similarity > analogy > relations only.

**ARCS** (Thagard et al. 1990). A connectionist network using WordNet-style semantic similarity and a special input for goals. Law, Forbus and Gentner (1994; a17, b04) ran both on the same data. MAC/FAC was about two orders of magnitude faster (0.2 to 0.4 s versus 81 to 373 s). ARCS was distracted when 25 plays were added to 100 fables. ARCS produced two order violations against human data (a16). The authors are the MAC/FAC team, and ARCS would not settle on their own encodings, so the comparison is not neutral.

**LISA** (Hummel and Holyoak). Retrieval is "guided pattern recognition". Role-filler bindings fire in synchrony (at most about three propositions at once), activate stored propositions that share semantic units, and the same process does mapping (a18). It also fits human reminding data and predicts the same surface bias. Only a five-page overview was opened. So MAC/FAC is not uniquely supported (K06, contested).

### 2.4 What helps: comparison and schema induction

- **Gick and Holyoak (1983)** found that two analogous stories, with the reader asked to write what they share, produced an abstract schema and better transfer (a02, a03).
- **Catrambone and Holyoak (1989)** (b16, restated): comparing two analogs raised relational retrieval. Reading both did not.
- **Thompson, Gentner and Loewenstein (2000), Loewenstein, Thompson and Gentner (2003).** Comparing two cases beat reading them separately in negotiation training (a19, a20).
- **Kurtz, Miao and Gentner (2001).** Comparison helps only when it is intensive: joint description plus an explicit list of correspondences (a24).
- **Kurtz and Loewenstein (2007)** (b17, snippet). Comparing two unsolved target problems raised use of a studied source.
- **Gentner, Loewenstein, Thompson and Forbus (2009).** Comparing two cases builds a schema, and the schema is a better memory probe than either case. Shown in people and in MAC/FAC simulation (a21 to a23).
- **Alfieri, Nokes-Malach and Schunn (2013).** Meta-analysis of case comparison: d = 0.50 over 57 experiments (b10, abstract only).

### 2.5 Is the surface bias real in the wild?

Blanchette and Dunbar and field studies of scientists found many far analogies. Trench (2014) argues the generation task, not expertise, lets distant sources appear: novices in the same task also give far analogies, and experts did not differ from novices on a management task (b19). Trench and Minervino (2015) found a strong surface effect even when people generate their own analogs (b18, abstract only). Result: contested (K16). The safe reading is that far analogies come out when people generate them, and are rare when people must look them up.

### 2.6 The language-model turn

- Webb, Holyoak and Lu (2023): GPT-3 shows analogical behaviour, including a qualitative Gick-Holyoak pattern (c06).
- Counterfactual tasks (c07) and permutation controls (c08) show brittleness.
- Yasunaga et al. (2024): analogical prompting, the model recalls its own similar problems (a25 to a28).
- Qin et al. (2025): relevance of those recalled problems is not what drives the gain (b22).
- 2024 to 2026: structure-based exemplar retrieval, geometry with a verifier, agent memory, and mid-trace retrieval (section 6).

---

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested. "Opened" is reported in section 11. Claim ids are in brackets.

### 3.1 Human access

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Radiation problem: spontaneous use of a studied story is low; a hint lifts it | about 10% no story; 20-30% story, no hint; 75-80% story plus hint (range 10-43% no hint in restatements) | Gick and Holyoak 1980, 1983 (a01, b13, d21) [K01] | [E], primary 1980 not opened |
| Business-problem replications show a weaker hint effect | Factory problem 6.3% to 8.7%; HR problem 20.3% to 37% (17/46); G&H 1983 29% (8/28) to 50% (14/28); N=199 humans | Strategic-decisions study 2025 (c12) | [E] with K01, preprint |
| Two analogs beat one | no-hint 45% vs 21%; total 80% vs 53%; Exp 4, N=98 | Gick and Holyoak 1983 (a02) [K04] | [E] |
| Stating the principle helps only with two analogs | one analog: about 30% either way (p=.36); two analogs: 62% vs 40% no-hint (p<.01), 82% vs 67% total | Gick and Holyoak 1983 Exp 2, 5 (a03) [K17] | [E] |
| Retrieval follows surface; soundness follows structure | Exp 2 recall: literal .56, surface .53, analogy .12, relations-only .09; soundness: literal 4.41, analogy 4.16, surface 2.70, relations-only 2.58; correlation of soundness and recall r(78)=.008 | Gentner, Rattermann, Forbus 1993 (a06, b01) [K02] | [E] |
| Exp 1: higher analogy recall with a different set | recall: surface .78, analogy .44, first-order only .25; soundness: analogy 4.40, surface 2.80; N=30 | same (a05) [K03] | [S] for the dissociation as a pattern in access vs judgement (one lab) |
| Object-only overlap is not enough | Exp 3: literal .62, surface + relations 52%, objects only 17%, analogy 7% | same (a07) | [S] |
| Structure was encoded; access failed | one week later, forced choice: literal over surface 82% (16.46/20); analogy over relations-only 55% (chance); N=27 | same Exp 4 (a08, b02) [K03] | [S] |
| Surface and structure both gate spontaneous transfer | before hint 69/38/33/13% as both are removed; after hint 75/81/60/47% | Holyoak and Koh 1987 (b14, slides only) | [S], not opened |
| Comparing two cases boosts later use (negotiation) | contingent contract 14/22 (64%) vs 5/22 (23%), N=44 dyads, p<.01 | Thompson et al. 2000 (a19) [K04] | [E] |
| Team replication is weaker | 24/60 (40%) vs 8/37 (22%), p=.06; separate-case study no better than no training; joint gains $4.76M vs $4.28M vs $4.19M | Loewenstein et al. 2003 (a20, b09) | [E] with the row above; marginal |
| Comparison improves recall from own memory | consultants N=124: retrieval 1.25 vs 0.82 (p<.01); analogy 63% vs 42% of recalls; shallow 20% vs 40%; Exp 2 N=36: 1.47 vs 0.59; 88% vs 17% linked the two cases | Gentner et al. 2009 Exp 1-2 (a21, b05) | [E] |
| Comparison at probe time changes what is retrieved | N=73: structural match recalled 27% vs 6%; surface lure 30% vs 78% | Gentner et al. 2009 Exp 4 (a22) [K05] | [S] (same lab) |
| Comparison with delay on the tumour problem | N=227: 31% vs 5% (p<.001); fire problem 41% vs 30% (p=.08, n.s.) | same Exp 5 (a22, b06) | [S]; effect depends on problem pair |
| Case comparison meta-analysis | d = 0.50, 95% CI [0.44, 0.56], 57 experiments, 336 tests; stronger when asked for similarities, principle given after the comparison | Alfieri et al. 2013 (b10) | [E], abstract only; lag subgroup numbers conflict (b11, snippet) |
| Diagrams: static not accessed, animated is | static at baseline (about 5-13%); animated convergence 55% (p<.01); Exp 3 static + principle 45%, dynamic + principle 50% | Pedone, Hummel, Holyoak 2001 (b12) [K17] | [E] with K17 |
| Mapping stays hard after access | 50-68% succeed even when numbers are told; 75% total with a hint | Novick and Holyoak 1991 (b28, snippet) [K13] | [S], not opened |
| Intensive comparison needs correspondences | joint + correspondence list beat control (Dunnett p<.05); 48% vs 23% used all key terms | Kurtz, Miao, Gentner 2001 (a24) | [S] |

### 3.2 Model of retrieval (MAC/FAC and rivals)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| MAC/FAC reproduces the human order | MAC passes about 3.3-3.4 items, FAC accepts 1.5-1.6; MAC pass rates LS .78, SF .67-.78, AN .33, FOR .22 | Forbus et al. 1995 (a12, b03, c14) [K06] | [C]: critique found a12 and c14 disagree on cells; order is the same |
| Selector width matters | viable region about 10-20% (30-50% for binary vectors); 1% finds no analogies | same (a13) | [S] |
| MAC/FAC vs ARCS | about 100x faster; ARCS ordering literal, first-order, appearance, analogy vs human literal, appearance, analogy, first-order | Law, Forbus, Gentner 1994 (a17) | [C] by the MAC/FAC authors |
| Schema probe retrieves analogies | schema probe: analogical matches 86%; single-story probe: shallow 86% and 100%, analogy 14% and 0%; schemas about 80% relational predicates vs about 40% | Gentner et al. 2009 simulation (a23, b07) [K05] | [S] |
| Literal near-copies crowd out everything else | with literal items in memory they win 100% | same (a23) | [S] |

### 3.3 Language models and retrieval systems

| Finding | Numbers | Source | Status |
|---|---|---|---|
| GPT-4 almost never uses the radiation story unprompted | 1 of 15 runs used it; the surface dolphin story 14 of 15; with hint recall 1.00, precision 0.50-0.52 | Strategic-decisions study 2025 (c12, c13) [K14] | [C], preprint, story likely in training data |
| Far analogy vs near decoy, side by side | GPT-4 29.1% (chance 50); GPT-3.5 21.7%; SBERT 1.0%; humans 91.4%; near analogy with far distractor GPT-4 94.0% | ARN, Sourati et al. 2024 (c09, d04) [K19] | [E] with next row, 2023 models |
| Cause-effect-reversed decoys | GPT-4 95.5% to 83.2%; humans 100% to 96%; 92.3% of GPT-4 errors were the decoy | ParallelPARC 2024 (d05) [K19] | [E] |
| Embedding retrieval anchors on wording | hard tier Hit@1 0.0% (both embedders), Hit@10 55.4% (Gemini) and 21.0% (Qwen); easy tier 12.2/89.8/97.6 (Hit@1/5/10); 95.2-99.8% of misses won by a more lexically similar item; 500 queries, 117,088 items | Rashid and Kellis 2026 (b26) [K07] | [E] with BRIGHT, preprint |
| Reasoning-heavy retrieval is hard for embedders | best MTEB model 59.0 vs 18.3 on BRIGHT; BM25 14.5 average | BRIGHT (c26, d02) [K07] | [E] |
| LLM rerank of the top 10 closes part of the gap | 5.4% to 63.3% of recoverable gap in math, depends on judge; trajectories 42-76%; a lexical reranker hurts math | Rashid and Kellis (b27) [K08] | [E] |
| Reranking depth does not pay | GPT-4 listwise: top-10 17.4, top-100 17.0 (BM25); 21.5 vs 22.6 (second retriever); web cross-encoder hurts (13.1, then 8.3) | BRIGHT Table 3 (d03) [K25] | [S] |
| Perfect retrieval adds nothing where the solver already succeeds | 210 queries: accuracy flat 67-70% across no retrieval, adversarial top-1, gold-with-solution; McNemar none vs gold p=.678 (13 hurt, 10 helped) | Rashid and Kellis (b27) | [S] |
| Structure-keyed exemplars beat embedding-keyed (maths) | avg exact match, random / BGE / structure: 0.5B 18.6/27.6/34.3; 1.5B 27.6/40.7/47.1; 3B 52.7/57.6/60.8; 7-8B 59.7/66.2/68.8; 70-72B 66.3/72.8/74.4; math_qa -0.7 | Graph-retrieval maths paper 2024 (b25, c17) [K09] | [E], retriever was trained |
| Geometry: analogue retrieval plus verifier | same 3x5 budget: o1 52 to 80, Gemini-Flash 72 to 86, Sonnet 78 to 86, GPT-5 88 to 96; first run: o1 10 to 48, Gemini 22 to 48, Sonnet 28 to 60, GPT-5 44 to 64; N=50 | Sultan, Stern, Shahaf 2025 (b24, c27) [K09] | [E] with row above; baseline had no analogy, not embeddings; baseline prompt about 3x more costly |
| Retrieved analogues vs random examples (geometry) | Gemini / Sonnet: full 48/60, analogues with full theorem dictionary 30/42, random 24/28, baseline 22/28 | same (c27) | [S] |
| Analogical prompting: small gain on easy maths | GSM8K GPT-3.5 0-shot 75.0, CoT 75.8, 5-shot 76.7, ours 77.8; MATH 33.0/33.9/34.9/37.3; PaLM2 GSM8K 60.8/78.2/80.7/81.7; text-davinci-003 14.8/50.3/54.0/61.0 | Yasunaga et al. 2024 (a26, b20, c01) [K10] | [C] |
| Larger gains on harder tasks | Codeforces GPT-3.5 Acc@1 9 to 13, with knowledge first 15; GPT-4 16 to 17 to 19 | same (c02) [K12] | [S] |
| Self-generated beats retrieved only for strong models | GSM8K retrieved 5-shot vs ours: curie 3 vs 2, davinci-001 11 vs 9, davinci-002 47 vs 48, davinci-003 57 vs 61; K=1 76.1, K=3 77.5, K=5 77.8 | same (a27, b21) | [S] |
| Relevance of self-generated exemplars is not the driver | GSM8K relevant 71.5, none 75.5, random same 75.1, random different 76.3, random biology 75.3; MATH 33.3 vs 36.1; wrong demos cost about 5 points | Qin et al. 2025 (b22, c04, c05) [K11] | [S] |
| A fixed vetted bank beats per-query recall | GSM8K fixed math 75.7, fixed biology 77.9 vs relevant 71.5; Llama-3.1-8B 81.0 vs 74.8; Qwen2.5-14B 91.1 vs 86.5 | same | [S] |
| Beyond maths the gain is small | BBH five tasks GPT-3.5: relevant avg 63.2, +1.3 over none; lost on formal fallacies and word sorting | same (d16) [K26] | [S] |
| Where analogical prompting fails | 100-problem audit: 35/50 correct had relevant correct exemplars, 9 had wrong exemplars, 6 irrelevant; 50 failures: 28 relevant and correct but failed (12 generalisation gap, 8 over-reliance, 8 other), 12 relevant but wrong, 10 irrelevant | Yasunaga et al. (a28) [K13] | [S] |
| Agent memory keyed by task similarity | ExpeL HotpotQA 28.0 to 39.0, ALFWorld 40 to 59, key: task 59.0 vs reasoning-step 48.5 vs random 42.5; Memento +6.7 F1 (59.9 to 66.6), K=4 best (64.5), K=32 63.9 | ExpeL, Memento (c21, c22, d13) [K15] | [E] |
| Progress-blind text key is worse than no memory | WebShop no insight 31.03, base embedder 18.42, trained key 31.74; ALFWorld 52.86 / 54.29 / 60.71 | InsightEmb 2026 (d06) [K15, K20] | [E] with EconSkills, preprint, trained key |
| False transfer when no true match exists | no-match tasks: no skill 16.7%; one hint 11.4% (p=.043); all 50 skills 11.4% overall vs 28.1%; five retrieved 28.3 (tied) | EconSkills 2026 (d08) [K20] | [E], one run per task |
| Write-time abstraction | EconSkills matched skill 49.3% vs 41.0% (p=.0031) vs raw trajectory 7.0% (confounded); AWM +5.0 element accuracy, +4.0 step success over a retrieve-relevant method | EconSkills, AWM (d07, d14) [K24] | [E] |
| Mid-trace retrieval helps small models | AIME 2025: Qwen3-1.7B 24.4 to 35.6; 4B 63.3 to 66.7; 8B 67.8 to 71.1; GSM8K Qwen3-8B 96.1 to 97.2; start-only 88.80 vs 89.07; random per-step exemplars take part of the gain | ThinkRetrieve 2026 (d09, d10) [K21] | [S] |
| Gating beats always-on in factual QA | useful at 40-80% of steps; falls beyond 50% on StrategyQA; stagnation controller: 14 fewer search calls, +3 accuracy | FLARE 2023, RAAC 2026 (d11, d12) [K22] | [S], not analogue retrieval |
| Probe rewriting works without training | BRIGHT up to +12.2; BoT distiller; ThinkRetrieve intermediate-answer query 91.0 vs 90.2; MetaLadder restate +2.5 (fine-tuned only) | BRIGHT, BoT, ThinkRetrieve, MetaLadder (d01, d02, d10, d15) [K23] | [E], not specific to relational wording |
| Cross-domain demonstrations | +12.3% (ProofWriter to LogicalDeduction), +10.3% (ProntoQA to LogicalDeduction); small models (3-7B) negative | Cross-domain study 2026 (c24) [K18] | [S] |
| Strong models may not need exemplars | R1 report: few-shot hurts (no numbers); ThinkRetrieve gains shrink with model size | DeepSeek-R1 (d17), ThinkRetrieve [K26] | [S] |

---

## 4. Mechanisms and models

Written so an engineer can build each part. All of them are code with a model filling a small slot (SCHEMA section 1).

### 4.1 Case representation

A stored case needs two forms, side by side.

1. **Concrete form.** The original problem text, the solution, the check that passed.
2. **Abstract form.** The same case with names, numbers and domain words replaced by placeholders, plus a list of relation tags.

Relation tags (a short controlled vocabulary, for example `goal:count`, `constraint:parity`, `relation:converge`, `operation:partition`, `symmetry:rotation`). MAC/FAC needs a shared vocabulary: its content vectors count predicate names, and two cases only match if they use identical predicate names (a11). Re-representation is a separate step. This is why an agent's tag vocabulary must be fixed and small (a few hundred terms were tested in MAC/FAC; Buffer of Thoughts used six template classes, d15).

Evidence for storing both forms: abstract workflows beat retrieved concrete examples (AWM, d14); a matched parameterised skill beat no skill, and the raw trajectory fell to 7.0% (confounded by length and format, d07); human access depends on whether the story was encoded abstractly (a04).

### 4.2 MAC/FAC as an implementation recipe

**Stage 1 (MAC), cheap, surface-sensitive.**
- Build a content vector per case: a count of each tag or predicate.
- Score = dot product of probe vector and case vector.
- Keep the best case and every case within 10% of its score (a11, c15). Typical output: 3.3 items from a memory of 36.
- Embedding similarity of the abstract form can stand in for the dot product. It plays the MAC role in the LLM version (c14).

**Stage 2 (FAC), structural.**
- For each survivor, align probe and case: match relations first, objects second, and prefer matches that connect into larger systems (the structure-mapping idea: systematicity). SME does this in the original.
- Keep the best structural score and any within 10%. Typical output: 1.5 items.
- The FAC may return nothing. "Nothing reminded" is a valid outcome (c15, b08). Original MAC/FAC always returns something unless FAC rejects all, and its authors list the missing failure case as a limit (a15).

**Knobs.** MAC width and FAC width. Too narrow (1%): no analogies retrieved. Too wide: junk. Viable 10 to 20% (a13). Our agent should tune both at equal tokens, not by taste (G7).

**What FAC can be in an LLM agent.** Option A: code compares relation tags and the typed signature (set overlap of relations, goal type and constraint type). Option B: a model call that must output an explicit alignment (a list of "probe element -> case element" pairs) and a code check that the pairs are one-to-one and complete. Kurtz et al. found that an explicit correspondence list is what makes comparison work (a24). Models prompted to "look for system mappings" still fell to decoys in ARN (d04), so Option B needs the code check.

**Behaviour to expect.** If a literal match exists, it wins and the structural match is crowded out (a12, a23). That is fine for reuse and bad for novelty. In open mode the surface term must be switched off on purpose (see 4.5).

### 4.3 Why comparison fixes access: schema as probe

The mechanism in Gentner et al. (2009; a21 to a23):

1. Take two analogous cases (two stored cases, or the current problem plus one solved sibling).
2. Align them. Keep what is shared (relations), drop what differs (objects).
3. The result (a schema) has about 80% relational predicates, against about 40% in a single story.
4. Use the schema as the memory probe. In simulation it retrieved analogical matches 86% of the time; a single story probe retrieved shallow matches 86 to 100% of the time.

Two placements.
- **Write time.** When a second similar case is solved, compare it with the first, store the schema. Human support: Thompson 2000, Loewenstein 2003, Gentner 2009 Exp 1-2, Alfieri meta-analysis.
- **Read time.** Compare the current problem with a second current problem (or a stored sibling) before searching. Human support: Gentner 2009 Exp 4-5, Kurtz and Loewenstein 2007.

Rules the human data impose:
- Reading two cases without comparing does nothing (a20: separate-case study no better than no training; only 18% of separate-case participants described links).
- Compare first, state the principle after (Alfieri moderator, b10). A stated principle alone does nothing from one case (a03).
- A joint description plus an explicit list of correspondences is the strong version (a24).

### 4.4 Probe reformulation before lookup

Rewrite the query so it carries the deep features. Training-free forms that worked:
- Reasoning-step query with a draft answer: up to +12.2 nDCG on BRIGHT (d02).
- A problem distiller that extracts key elements and constraints before template lookup (BoT, d15).
- The current intermediate answer appended to the query (91.0 vs 90.2, d10).
- Gold sub-concepts added to the query: retrieval 0.557 to 0.673 average (c25); generated sub-concepts added only 0.4 to 1.6 points.

Warnings. Extra reasoning can lower retrieval specificity (d19, abstract only). Keep it to one short pass. The active ingredient may be an answer-like expansion, not relational wording (d02). MetaLadder's "restate" step is the largest ablation but only after fine-tuning (d01).

### 4.5 Open mode: distant retrieval on purpose

In people, far analogies come from generation, not lookup (b19). Lookup is surface-first. The model version of this split: analogical prompting is generation (a25), a library is lookup. In free generation a model beat embedding retrieval from a fixed event pool by 0.25 Pass@1 on historical analogies, but the pool was small and coverage limited (b23).

A way to retrieve distant cases: use the abstract form only, mask domain words in the probe, and exclude entries with the same domain tag. This is a design idea built from a12 and a23. Not tested.

### 4.6 Trigger design

Human fix: a hint ("one story may help") raises use from about 30 to about 75% (a01). GPT-3 on the radiation problem was rescued by the same hint (c06). In code, a hint is a trigger for a lookup.

Candidates:
- Always-on at each step. ThinkRetrieve did this at stop-thinking boundaries (d09).
- Gated by confidence (FLARE, d11) or by stagnation (RAAC, d12).
- Only at an impasse (S6). Not tested anywhere.

The only controlled gating comparison found is FLARE: gating matched always-on at 40-80% of steps and always-on hurt on StrategyQA beyond 50%. Evidence is for factual QA with 2023 models.

### 4.7 Retrieval pipeline for our agent (design, not yet tested)

```
probe = restate(problem) -> elements, constraints, relation tags      # one short pass
C1 = MAC(probe.tags, memory.abstract_forms, width=10%)                # code, cheap
C2 = top-10 by embedding of the abstract form, union with C1          # wide recall
for c in C2: align(probe, c) -> mapping or REJECT                     # model slot + code check
pick = best mapping within 10% of the top score, else NONE            # code
if pick: show ONE case with its mapping, marked as a hypothesis       # never several at once
test on the unfitted part (G3)                                        # code
```

Reasons for each line: Rashid and Kellis (top-10 contains the answer, top-1 does not, b26); EconSkills (no-match must be allowed, k small, d08); ARN and the strategic-decisions study (models force all offered cases, c13, d04); Yasunaga (over-reliance on one exemplar, a28).

---

## 5. What holds up

### 5.1 Replications and independent confirmations

| Result | Independent confirmation | Verdict |
|---|---|---|
| Spontaneous analogue use is low and a hint fixes it | Gick and Holyoak 1980/1983, Pedone et al. 2001 (diagram groups equal to controls before the hint, over 60% after), Gentner 2009 Exp 5, business-problem study 2025 (weaker) | [E]. Size varies from 6% to 43% by materials. |
| Surface similarity dominates retrieval | Gentner et al. 1993, Holyoak and Koh 1987, Ross, Trench and Minervino 2015 (production), Rashid and Kellis 2026 (embeddings), ARN, StoryAnalogy | [E] in people and in models |
| Comparison of two cases improves later use | Gick and Holyoak 1983, Catrambone and Holyoak 1989 (restated), Thompson 2000, Loewenstein 2003, Gentner 2009, Alfieri 2013 | [E] direction; effect from d=0.50 (meta) to 40 vs 22% (teams, p=.06) |
| Two-stage retrieval with a structural filter works | MAC/FAC simulations, schema probes, LLM rerank on top-10 (Rashid), geometry retrieval with predictors (Sultan) | [E] as a design; nobody compared it with a trained alternative at equal cost |
| Structure-keyed exemplar retrieval beats embedding retrieval | graph-retrieval maths (trained retriever), InsightEmb (trained key) | [E] but the key was trained both times |

### 5.2 Failures, nulls and boundary conditions

- **Relevance is not the driver of analogical prompting.** With GPT-3.5, relevant self-generated exemplars scored 71.5 on GSM8K, below none (75.5) and below random (75.1 to 76.3) (b22). Yasunaga reports relevant at 77.8 with its own 75.8 baseline. The two use different prompts and seeds. Unresolved (K10, K11).
- **The gain does not survive on strong models** where 0-shot CoT is already high. GSM8K PaLM2 80.7 to 81.7, GPT-3.5 76.7 to 77.8 (a26). DeepSeek-R1 report: few-shot hurts (d17).
- **Perfect retrieval did not move accuracy** when the solver already succeeded (b27). Retrieval only helps where the model fails. Measure headroom first.
- **Comparison effect is not uniform.** The fire-hose problem: 41% vs 30%, p=.08 (a22). Teams: p=.06 (a20). Alfieri's lag subgroup numbers conflict with the abstract (b11 vs b10).
- **Mapping still fails after access.** 28 of 50 LLM failures had relevant, correct exemplars (a28). Humans: 50 to 68% even with the numbers told (b28, snippet).
- **Static diagrams and stated principles do not help from one source** (a03, b12). Animated or paired with a second case, they do.
- **Fewer than expected benefits for self-generated analogies in real tasks.** BBH: +1.3 average, a loss on two of five tasks (d16).
- **False transfer.** EconSkills forced top-1 cut success from 16.7 to 11.4% on no-match tasks even with "ignore if unsuitable" (d08). InsightEmb's progress-blind key took WebShop from 31.0 to 18.4 (d06).
- **Context dumps hurt.** All 50 skills in context: 11.4% vs 28.1% for none (d08). Memento: K=4 best, K=32 lower (c22).
- **Wrong exemplars cost about 5 points** (b22/c05). Self-graded stored memories inflate (abstract only, d18).

### 5.3 Moderators

| Moderator | Effect |
|---|---|
| Model strength | Retrieved exemplars beat self-generated for weak models; the order flips at text-davinci-002/003 (a27). Gains from structure keys fall from +6.7 (0.5B) to +1.6 (70B) (c17). Mid-trace retrieval gains fall from about +10 (1.7B) to +1 to +3 (8B) (d09). Cross-domain demonstrations hurt below about 7B (c24). |
| Difficulty | Gains are largest on the hardest sets (d09, d15), near zero on saturated ones. |
| Problem pair | Comparison effect varies by pair (a22, b06). |
| Retrieval distance | Near analogy with a far distractor: GPT-4 94%. Far analogy with a near distractor: 29.1% (d04). |
| Presence of a literal match | A literal match crowds out all structural ones (a23). |
| Principle given after comparison | Stronger in Alfieri than principle given before (b10). |
| Competition in memory | Several surface-similar entries can sharpen a structural cue (Wharton et al. 1994, a30; restated only). |
| Expertise | Experts and intensively trained people retrieve more structure (a14, restated), but the generation-task account explains field data too (b19). |

### 5.4 Interventions that worked and did not

| Worked | Did not work |
|---|---|
| A bare hint that a stored case may help (human 30 to 75%; GPT-3) | Reading two cases without comparing |
| Comparing two cases and stating what they share | A stated principle with only one case |
| Schema or abstract form as the probe | Static diagrams alone |
| Wide recall then rerank by structure (top-10) | Deeper reranking (top-100) |
| Write-time abstraction with placeholders | Raw trajectories as the stored form (7.0% in EconSkills, confounded) |
| Fixed vetted exemplar set | Per-query self-generated "relevant" exemplars (GPT-3.5 maths) |
| Probe rewrite (reasoning-step or distiller) | Web-trained cross-encoder reranker (BRIGHT) |
| Small k (4 to 5) | Putting the whole library in context |

---

## 6. Language models

### 6.1 How they behave on access tasks

**Models show the human surface bias.** ARN: GPT-4 chooses the right analogy well when it is near (94.0%) and drops to 57.1% when it is far with a far distractor, to 29.1% against a near surface distractor (chance 50, humans 91.4%). SBERT cosine scored 1.0% in that cell (d04, c09). ParallelPARC: reversing cause and effect in a decoy cut GPT-4 from 95.5 to 83.2%, humans stayed at 96 to 100%, and 92.3% of GPT-4 errors were the decoy (d05). StoryAnalogy: text-davinci-003 averaged 37.1% against 85.7% for humans; a structure baseline scored 44.9% (c10). SCAN: cross-domain analogies are harder than same-domain ones for older models (c11).

**Models are not good at judging when shown the pair.** The human split (sound when shown, poor at retrieval) is not the LLM pattern. The LLM failure is already present at recognition (d04, K19). This applies to 2023-era models. Newer ones are untested.

**Embeddings anchor on wording.** Rashid and Kellis: on paraphrased math problems the planted lexical near-miss won; strict Hit@1 on the hard tier was 0.0% for both embedders, yet Hit@10 was 55.4% (Gemini) and 21.0% (Qwen). On agent trajectories Hit@1 was 17.8%, 15.3% and 9.3% against chance 15.3% (b26). BRIGHT confirms the weakness on reasoning-heavy queries (59.0 vs 18.3, c26).

**The radiation problem with GPT-4.** Without a hint it used the radiation story in 1 of 15 runs and a surface dolphin story in 14 of 15. With a hint, recall was 1.00 but precision about 0.50. Humans had high precision and low recall. The model is an eager but unselective retriever. It used both stories when both were offered (c12, c13). Caveats: preprint, story probably in training data.

**Fragility.** Counterfactual letter-string tasks: humans 0.753, GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (c07). Small prompt changes moved GPT-4 from about 20 to about 100% on one variant (c08). Webb et al. argue part of this is task demands (c30, not opened). Any access step needs several prompt variants.

### 6.2 What changed performance, and by how much

| Intervention | Change | Where | Note |
|---|---|---|---|
| Analogical prompting (self-recall K=3 to 5) | GSM8K +2.0 (75.8 to 77.8), MATH +3.4 (33.9 to 37.3), five BBH tasks +3 to +13 over 0-shot CoT (word sorting 67.6 to 75.2, temporal 44.8 to 57.6 where 3-shot gets 58.0), Codeforces Acc@1 +4 (9 to 13), +6 with knowledge | GPT-3.5, PaLM2 (a26, b20) | Single runs, no confidence intervals. Gain is 1.1 over fixed 5-shot on GSM8K. |
| Same, independent test | relevant 71.5 vs none 75.5 on GSM8K | GPT-3.5 (b22) | Contradiction unresolved |
| Fixed vetted exemplars | +6.4 over relevant (77.9 vs 71.5); Llama-3.1-8B 81.0 vs 74.8 | Qin et al. (c05) | Single paper |
| Self-consistency on top of analogical prompting | GSM8K 77.8 to 85.3, MATH 37.3 to 46.0 | Yasunaga (b21) | Extra samples; a token cost not equalised |
| Structure-keyed few-shot retrieval vs BGE | +6.7 (0.5B), +6.4 (1.5B), +3.2 (3B), +2.6 (7-8B), +1.6 (70B) | 6 maths sets (c17) | Retriever trained on labelled graphs |
| Analogue retrieval plus symbolic verifier | first run 10 to 48 (o1), 44 to 64 (GPT-5); with retries 52 to 80, 88 to 96 | FormalGeo, N=50 (b24, c27) | Baseline carried an 18K-token theorem list; random examples reached 24/28 |
| Mid-trace retrieval | +11.2 (Qwen3-1.7B AIME), +3.3 (4B), +3.3 (8B); GSM8K +1.1 | ThinkRetrieve (d09) | 309,609-item corpus, no structural key; random per-step exemplars take part of the gain |
| Query rewrite with reasoning | up to +12.2 nDCG | BRIGHT (d02) | BM25 gains most |
| Rerank top-10 by a model | closes 5.4 to 63.3% of the gap | math (b27) | Depends on judge |
| Agent memory by task similarity | ExpeL +11 HotpotQA, +19 ALFWorld; Memento +6.7 F1 | (c21, c22) | Embedding key, not structure |
| Trained progress-aware key | WebShop 18.4 to 31.7 vs progress-blind | InsightEmb (d06) | Trained retriever |
| Abstract workflows vs retrieved concrete examples | +5.0 element accuracy, +4.0 step success | AWM (d14) | Not a matched ablation |
| Matched parameterised skill | 41.0 to 49.3% | EconSkills (d07) | No-match tasks lose |
| Thought propagation (generate neighbours, solve, aggregate) | +12% optimal paths, +13% preference, +15% ALFWorld completion | (c20) | Same-model analogues, blind spots shared, higher token cost |
| Cross-domain demonstrations | up to +12.3% | (c24) | Only above a size threshold |

### 6.3 What this adds up to

1. Models do the analogue-finding step (recall by generation) cheaply, and it gives small gains on strong models and larger gains on weak ones. The gain is not clearly caused by analogy (b22, a28: 9 of 50 correct answers had wrong exemplars).
2. Lookup by external memory is dominated by the key. Wording keys fail in a predictable way (Rashid). Structure keys help, mostly when the solver is weak.
3. Accuracy gains from perfect retrieval are limited by headroom. Retrieval cannot fix a problem the model solves anyway, and may break easy ones (13 hurt, 10 helped, b27).
4. Tokens are rarely equalised. Analogical prompting adds generated tokens; thought propagation more; the geometry baseline carried 3x more tokens than the analogy arm. No result here can be taken as an equal-token gain.
5. Almost nothing is known about current frontier models.

---

## 7. What our agent should take

Marks: schema part G / S / O / memory. Evidence ids in brackets. Status as in claims.jsonl.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Never look up by raw text similarity alone.** Wording-keyed lookup returns the wrong item first; the right one is usually in the top 10. Retrieve wide (up to 10), then pick by structure, in code or with a model slot whose pick is checked. | memory (library lookup), O7 | [E] K07, K08 | b26, b27, c26, d02, d03, c25 |
| A2 | **Rerank window of about 10, not 50 or 100.** Deeper reranking did not reliably pay and a longer prompt costs tokens. | memory | [S] K25 (put here only as the cap on A1; do not extend further without a test) | d03, b27 |
| A3 | **A lookup may return nothing.** Include an explicit no-match outcome. A forced top-1 with no true match cost about 5 points even with "ignore if unsuitable". | memory, G7 | [E] K20 | d08, d06, d18 |
| A4 | **Keep k small (about 4 to 5 cases) and offer one at a time with its mapping.** Whole-library dumps were worse than no skill. Models use every case offered. | memory, O7 | [E] K20 (with K14 [C] for the "use all" behaviour) | d08, c22, c13 |
| A5 | **Store an abstract form beside the concrete form** when writing a solved subgoal (placeholders for names and numbers, plus relation tags). Do not store the raw trajectory alone. | memory, S9 | [E] K24 | d14, d07, d13, a04 |
| A6 | **Rewrite the probe once before lookup** (elements, constraints, relation tags; or a short reasoning-step draft). One short pass only. | memory, S1 to S2 | [E] K23, but the relational wording itself is not isolated | d02, d15, d10, c25 |
| A7 | **A retrieved case is a hypothesis.** It must pass the unfitted check (G3) before it counts. Models copy details that do not fit (8 of 50 failures were over-reliance; 12 generalisation gap). | G3, O7 | [E] G3 plus K13 [S] for the failure counts | a28, b28, a09 |
| A8 | **Memory writes need an independent check.** Store a solved subgoal only if it passed the check (G3), not on self-grade. | memory, S9 | [S] K20 | d18 (abstract only), d06 |
| A9 | **Do not rely on a model to choose between a decoy and a structural match shown side by side.** A relation-by-relation mapping with a code check is needed. | O7 | [E] K19 | d04, d05 |

Note on A2 and A8: they are flagged [S] because their evidence is a single paper each. They are listed here because they cap A1 and A3 and cost nothing. If the team wants a strict [E] list, A2 and A8 move to "Test first".

### Test first

| # | Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | **Cue lookup at an impasse (S6)**, not always-on and not never. Human data: a cue lifts use from about 30 to about 75%. | S6, O7, G1 | human [E] K01; trigger comparison [S] K22 | a01, c06, d11, d12 | No study compares failure-triggered with always-on analogue retrieval per token. |
| T2 | **Relation-tag key vs embedding key** for the subgoal library, same k, equal tokens. | memory | [E] that structure keys help in maths (K09), [S] for a zero-training key in a loop (K15) | c17, b25, d06, b26 | Every winning key was trained. |
| T3 | **Compare two solved subgoals and store the schema** (write time). | memory, S9 | human [E] K04; LLM none | a02, a19 to a21, b10, d13 | No LLM study has a two-case arm. |
| T4 | **Compare the current problem with a sibling** and use the result as the probe (read time). | memory, S6 | human [S] K05 | a22, a23, b17 | Same lab; no LLM data. |
| T5 | **Explicit mapping step** (list of correspondences, code-checked) between probe and retrieved case. | O7 | [S] K13; the check logic is [E] by A7 | a24, a28, d04 | Mapping benefit unmeasured for LLMs. |
| T6 | **Fixed vetted bank of worked examples** instead of per-query self-generated analogues. | O7, memory | [S] K11 | b22, c05 | One paper, GPT-3.5 era. |
| T7 | **Self-generated analogues at impasse** (analogical prompting inside O7), with general knowledge first. | O7 | [C] K10, [S] K12 | a25, b22, c02, d16 | Contested; gains small on strong models. |
| T8 | **Mid-trace injection** of one retrieved case at a revision point vs at the start. | S5, S6 | [S] K21 | d09, d10 | Math only, small models, no failure trigger. |
| T9 | **Gate by model strength and difficulty** (use retrieval on hard items; skip it on easy ones). | S0, G12 | [S] K21, K26 | d09, d17, b27, c17 | Frontier models untested. |
| T10 | **Distant retrieval in open mode** (mask domain words, exclude same-domain entries). | S3 open, O7 | design idea from a12, a23; no direct test | a12, a23, b23, b19 | Untested. |
| T11 | **Tag consistency**: do model-written tags agree across rewrites, and does tag-filtered MAC beat untagged lookup? | memory | [S] K27 | d08, d14, d15 | Nobody measured it. |
| T12 | **Knowledge-first prompting** (state the general principle, then the analogue) on hard tasks. | O7 | [S] K12 | c02 | One paper, Codeforces. |

---

## 8. Concrete tests on our bench

Common rules for all tests. Both arms run at equal total tokens, counting every extra pass (tagging, restating, lookup, mapping). Report solve rate, tokens per solved item, and the number of items that flipped right to wrong and wrong to right (SCHEMA section 6). Use the same base model for all arms. Report results by problem class, since the class record is read by S0. Item types below use the suites the project already has (ARC grid items with a check, BRAINTEASER word puzzles, NoveltyBench open items). Where a test needs a memory of solved subgoals, build it first from the agent's own passed runs (A8).

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| E1 | Does lookup find structure or wording? | A paraphrase set built from stored solved items: same structure, new surface words (and a lexical decoy per item) | (a) embedding of raw text, top-1; (b) embedding top-10 then structure pick; (c) relation-tag MAC then pick | Hit@1, Hit@5, Hit@10; tokens per lookup | (a) Hit@1 near 0 on the hard tier, as in Rashid; (b) and (c) +20 to +50 points Hit@1 over (a). Offline, no solving needed. |
| E2 | Probe rewrite | Same set as E1 | raw probe; one-paragraph restatement; relation-tag abstraction | Hit@1 | +5 to +15 points over raw; relation-tag at least as good as free restatement. |
| E3 | Tag consistency | 50 stored cases, each tagged 5 times | none (measurement) | Mean pairwise Jaccard of tag sets; Hit@1 of tag-filtered vs untagged lookup | Jaccard at least 0.7 needed for tag-keyed lookup to work. Unknown. |
| E4 | Trigger | ARC and BRAINTEASER items with a populated memory (analogue exists for half of them, none for the other half) | none; always-on at S3; lookup only at S6 impasse | Solve rate on the whole set; tokens per solved item; loss on no-analogue items | Impasse arm keeps most of the gain of always-on at lower tokens, and avoids the false-transfer loss. Unknown size. |
| E5 | No-match gate and mapping check | Items with no true analogue (e.g. 40 of 100) | forced top-1; top-1 with no-match option; top-1 with no-match option plus code-checked mapping | Solve rate on no-analogue items vs no-memory; solve rate on analogue items | Forced top-1 loses about 3 to 5 points on no-match items (EconSkills: 16.7 to 11.4). The gate removes most of it. |
| E6 | Key inside the loop | ARC items with memory of passed subgoals | embedding key; relation-tag key; none | Solve rate, tokens per solved | Relation key +2 to +6 points over embedding if the model is weak on the class; near zero on easy classes. |
| E7 | Write-time form | Same | raw case; single-case abstraction; two-case schema | Solve rate on a third, structurally similar item | Abstraction beats raw; schema beats single abstraction by a few points (human d=0.5 would be a medium effect; LLM effect unknown). |
| E8 | Read-time sibling comparison | Pairs of open items | probe alone; probe plus sibling compared, schema as probe | Hit@1 on E1-style set; solve rate | +10 to +20 points Hit@1 if the human 27% vs 6% pattern carries over. |
| E9 | Self-generated vs vetted bank | GSM8K-like and ARC-like items | 0-shot; self-recall K=3; fixed vetted bank of 5 | Solve rate, tokens | Fixed bank at least equal to self-recall and cheaper, on weak and mid models; no gain on a strong model. |
| E10 | Decoy judgement | 100 pairs: structural match vs lexical decoy | pick without mapping; pick with code-checked mapping | Decoy picks (%) | Without mapping many decoy picks on far analogies (GPT-4 era 29% correct); mapping lowers it. Current base model unknown. |
| E11 | Rerank depth and memory size | Memory grown from 50 to several thousand cases | top-5, 10, 25 rerank | Hit@1 and solve rate at fixed token cost | Flat after about 10; top-1 solve rate drops without rerank as memory grows. |
| E12 | Open mode | NoveltyBench-type items | attempts grounded in surface-near analogues; in domain-masked distant analogues; none | Distinct-answer count; quality by run or check | Distant grounding adds distinct answers; average quality drops and spread rises (SCHEMA O7 note). |

---

## 9. What does not transfer, and why

- **Forgetting and delay.** The human effect depends on a week-long gap between study and test. The agent's memory is an exact store. The failure the agent faces is a bad key, not decayed memory. The weak-cue explanation from people (the case is stored but not reached) is the one that carries over, not forgetting.
- **Demand characteristics.** Part of the 20 to 30% no-hint rate in people may be subjects guessing the story is relevant (a01). An agent that is shown a list of cases has no such guess. It will use all of them (c13).
- **Small memories.** MAC/FAC was tested on 18 to 125 hand-encoded items. Our store may reach thousands of entries. The speed claim (100x faster than ARCS) comes from a small test by the MAC/FAC authors.
- **Hand-coded predicates.** MAC/FAC assumes identical predicate vocabularies (a11). Model-written tags may drift. Nobody has measured it (K27).
- **Training-based retrievers.** The graph-retrieval maths paper, InsightEmb and MetaLadder trained something. We do not train. Their gains are an upper bound for a training-free key.
- **Surface help on purpose.** Holyoak and Koh show shared surface features raise access (b14, a29). For reuse of the same class (the common case), literal matches are the right answer. The surface bias is a bug only when we need far analogues.
- **Single-pass analogical prompting as "retrieval".** The model is its own memory and retriever. G4 says its samples are not independent. The gain may be a format or priming effect (a28, c04), so it should not count as access.
- **Teams and negotiation tasks.** The comparison effect is measured on negotiation scenarios, with motivated adults. It tells us about direction and rough size, not about LLM gain.
- **Expert versus novice.** Not applicable to a fixed model. The nearest analogue is model strength, which does moderate results (section 5.3).
- **Diagrams and animation.** Perceptual, no text counterpart (b12). The nearest equivalent is a force or motion relation tag.
- **2026 preprints.** Rashid and Kellis, InsightEmb, EconSkills, ThinkRetrieve, RAAC and SEAM are not peer reviewed and some had integrity incidents listed by the authors (b27). They guide tests, not the schema.

---

## 10. Open questions

1. At equal tokens, does a zero-training relation-tag key beat embedding retrieval for the agent's own solved subproblems inside a multi-step loop? (Gap 1; K15, K20)
2. Does a failure-triggered analogue cue recover more per token than always-on retrieval? Is the LLM analogue of a human hint a trigger or a rerank step? (Gap 2; K22)
3. How much of the analogical-prompting gain survives with a fixed vetted bank, beyond maths, on a current frontier model? (Gap 3; K10, K11, K26)
4. How consistent are model-written relation tags across writes, and how large a vocabulary does MAC need? (Gap 4; K27)
5. Which is larger for an LLM agent: write-time schema from two cases or read-time sibling comparison? (Gap 5; K24)
6. What cheap check keeps false transfer low when retrieval is loosened? (Gap 6; K20, K13)
7. Is the model a better judge than retriever on current models, when a decoy and a structural match are shown together? 2023 models were not. (Gap 7; K19)
8. How does retrieval quality change with memory from 50 to several thousand cases, and where does rerank depth stop paying? (Gap 8; K25)
9. Is relational wording in the probe the active ingredient, or is any answer-like expansion enough? (Gap 9; K23)
10. What do the primary texts of Gick and Holyoak 1980, Holyoak and Koh 1987, Novick and Holyoak 1991, Catrambone and Holyoak 1989 and Alfieri 2013 give? The no-hint rate ranges from 10 to 43% by experiment in restatements. (Gap 10; K01, K13)
11. Do the human conclusions about experts (more structure at access) have an analogue in model scale, and where does it flip?
12. Does retrieving a case help at all when the base model's own thinking mode is strong? SCHEMA section 7 asks for an equal-token baseline of one extended-thinking attempt first.
13. How much of the lookup gain in agent memory comes from the injection act (a second look with new text) and not the content? Random per-step exemplars took part of the ThinkRetrieve gain (d10).

---

## 11. Sources

[V] = opened and read in this run (full text or the relevant sections, or a page that carried the numbers used). [M] = snippet, abstract or secondary restatement only. The critique re-opened arXiv PDFs for Yasunaga, Qin, Rashid and Kellis, Sultan et al., the graph-retrieval paper, and the strategic-decisions paper; Alfieri's d = 0.50 and 57 experiments were not re-confirmed there.

### Human access and models of retrieval

1. [V] Gick and Holyoak (1983) Schema induction and analogical transfer. https://Www.Gwern.net/doc/psychology/1983-gick.pdf (a01 to a04)
2. [M] Gick and Holyoak (1980) Analogical problem solving. Cognitive Psychology 12, 306-355. https://deepblue.lib.umich.edu/items/c0edbf58-93fd-41d4-91d6-22ae89d1adca/full (a31; download failed, numbers from 1983 and 1993 restatements)
3. [V] Gentner, Rattermann and Forbus (1993) The roles of similarity in transfer. https://groups.psych.northwestern.edu/gentner/papers/GentnerRattForbus93.pdf (a05 to a10, b01, b02, b03, b15)
4. [V] Forbus, Gentner and Law (1995) MAC/FAC: a model of similarity-based retrieval. https://qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_1994/Forbus_1994_MAC_FAC_Model_Similarity-Based_Retrieval_CogSci.pdf and https://www.qrg.northwestern.edu/papers/Files/macfac91(searchable).pdf (a11 to a16, c14, c15)
5. [V] Law, Forbus and Gentner (1994) Simulating similarity-based retrieval: ARCS and MAC/FAC. https://groups.psych.northwestern.edu/gentner/papers/LawForbusGentner94.pdf (a17, b04)
6. [V] Hummel and Holyoak, overview of the LISA project (Current Directions). https://pages.ucsd.edu/~scoulson/Courses/101c/Articles/hummell.pdf (a18); the 1997 Psychological Review paper was not opened.
7. [M] Holyoak and Koh (1987) Surface and structural similarity in analogical transfer. https://dspace.ewha.ac.kr/handle/2015.oak/208243 (a29) and slides https://pages.ucsd.edu/~scoulson/Courses/101c/analogy2.pdf (b14)
8. [M] Wharton et al. (1994) Below the surface. https://escholarship.org/uc/item/5h3765rq (a30)
9. [V] Pedone, Hummel and Holyoak (2001) The use of diagrams in analogical problem solving. https://sites.lifesci.ucla.edu/psych-reasoninglab/wp-content/uploads/sites/273/2021/04/Pedone_etal.MC_.2001.pdf (b12, b13)
10. [M] Catrambone and Holyoak (1989) Overcoming contextual limitations. https://sites.lifesci.ucla.edu/psych-reasoninglab/wp-content/uploads/sites/273/2021/04/Catrambone_Holyoak1989.pdf (b16; truncated downloads)
11. [M] Novick and Holyoak (1991), as cited in https://arxiv.org/pdf/2603.07979 (b28)
12. [M] Ross (1984, 1989), Novick (1988), Faries and Reiser (1988), Schumacher and Gentner (1987): restated inside items 3 and 4 only.
13. [M] Gick and Holyoak (1980) experiment figures as restated at https://nmoer.pressbooks.pub/cognitivepsychology/?p=925 (d21)

### Comparison and schema induction

14. [V] Thompson, Gentner and Loewenstein (2000) Avoiding missed opportunities in managerial life. https://mail.loewenstein.web.illinois.edu/papers/Thompsonetal%20OBHDP00.pdf (a19)
15. [V] Loewenstein, Thompson and Gentner (2003) Analogical learning in negotiation teams. https://business.illinois.edu/loewenstein/papers/Loewensteinetal%20AMLE03.pdf (a20, b09)
16. [V] Gentner, Loewenstein, Thompson and Forbus (2009) Reviving inert knowledge. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2009/Gentner,Loewenstein,Thompson&Forbus_2009-1.pdf (a21 to a23, b05 to b08)
17. [V] Kurtz, Miao and Gentner (2001) Learning by analogical bootstrapping. https://groups.psych.northwestern.edu/gentner/papers/KurtzMiaoGentner01.pdf (a24)
18. [M] Kurtz and Loewenstein (2007) Converging on a new role for analogy. https://link.springer.com/article/10.3758/BF03193454 (b17)
19. [V abstract only] Alfieri, Nokes-Malach and Schunn (2013) Learning through case comparisons. https://eric.ed.gov/?id=EJ1000186 (b10); lag subgroup [M] https://www.scinapse.io/papers/2124645092 (b11)
20. [M] Trench and Minervino (2015) The role of surface similarity in analogical retrieval. https://ri.conicet.gov.ar/handle/11336/32461 (b18)
21. [V] Trench (2014) Explaining the abundance of distant analogies (commentary). https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.01487/pdf (b19)
22. [V] Accelerating Innovation Through Analogy Mining (2017). https://arxiv.org/abs/1706.05585 (c16)

### Language models: analogy and prompting

23. [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714 and https://arxiv.org/pdf/2310.01714 (a25 to a28, b20, b21, c01 to c03)
24. [V] Qin et al. (2025) Relevant or random: can LLMs truly perform analogical reasoning? https://arxiv.org/pdf/2404.12728 and https://arxiv.org/html/2404.12728v3 (b22, c04, c05, d16)
25. [V] Webb, Holyoak and Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (c06)
26. [M] Webb et al. response to counterfactual critique. https://arxiv.org/abs/2308.16118 (c30)
27. [V] Counterfactual analogical-reasoning tasks (2024). https://arxiv.org/html/2402.08955v1 (c07)
28. [V] Musker et al. (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803 (c08)
29. [V] Sourati et al. (2024) ARN: Analogical Reasoning on Narratives. https://arxiv.org/html/2310.00996v3 and https://arxiv.org/abs/2310.00996 (c09, d04)
30. [V] StoryAnalogy (2023). https://arxiv.org/pdf/2310.12874 (c10)
31. [V] Czinczoll et al. (2022) SCAN. https://aclanthology.org/2022.findings-emnlp.153.pdf (c11)
32. [V] Can LLMs help improve analogical reasoning for strategic decisions? (2025). https://arxiv.org/pdf/2505.00603 (c12, c13)
33. [V] Sultan et al. (2024) ParallelPARC. https://arxiv.org/abs/2403.01139 (d05)
34. [V] Li et al. (2025) Past meets present: historical analogy with LLMs. https://arxiv.org/pdf/2409.14820 (b23)
35. [V] Thought Propagation (2024). https://arxiv.org/abs/2310.03965 (c20)
36. [V] MetaLadder (2025). https://arxiv.org/html/2503.14891v1 and https://arxiv.org/abs/2503.14891 (c18, c19, d01)

### Retrieval by structure, reranking, reformulation

37. [V] Sultan, Stern and Shahaf (2025) Reliable proof generation via analogical retrieval and symbolic verification. https://arxiv.org/pdf/2505.14479 and https://arxiv.org/html/2505.14479 (b24, c27)
38. [V] Learning by analogy: computational graph-based retrieval (2024). https://arxiv.org/pdf/2411.16454 and https://arxiv.org/html/2411.16454v1 (b25, c17)
39. [V] Rashid and Kellis (2026) Retrieved but not ranked. https://arxiv.org/pdf/2609.01556 (b26, b27)
40. [V] BRIGHT (2025). https://arxiv.org/abs/2407.12883 (c26 [M] earlier, d02, d03 [V])
41. [V] Teaching Through Analogies: modular pipeline (2026). https://arxiv.org/pdf/2605.24211 (c25)
42. [V] Cross-domain prior knowledge for in-context learning (2026). https://arxiv.org/pdf/2604.05396 (c24)
43. [V] CHAIRO (2026). https://arxiv.org/html/2604.10502 (c28)
44. [M] AURA (2026) utility-guided adaptive reasoning. https://arxiv.org/abs/2610.21030 (d19)
45. [V] Buffer of Thoughts (2024). https://arxiv.org/abs/2406.04271 (d15)

### Agent memory and triggers

46. [V] ExpeL (2024). https://arxiv.org/html/2308.10144 and https://arxiv.org/abs/2308.10144 (c21, d13)
47. [V] Memento (2025). https://arxiv.org/html/2508.16153 (c22)
48. [V] SEAM (2026). https://arxiv.org/pdf/2602.02556 (c23, c29)
49. [V] InsightEmb (2026). https://arxiv.org/abs/2608.04761 (d06)
50. [V] EconSkills (2026). https://arxiv.org/abs/2609.19523 (d07, d08)
51. [V] ThinkRetrieve (2026). https://arxiv.org/abs/2608.10928 (d09, d10)
52. [V] FLARE, Jiang et al. (2023). https://arxiv.org/abs/2305.06983 (d11)
53. [V] RAAC, When deep research agents stagnate (2026). https://arxiv.org/abs/2608.15191 (d12)
54. [V] Agent Workflow Memory (2024). https://arxiv.org/abs/2409.07429 (d14)
55. [M] Memory Reward Inflation (2026). https://arxiv.org/abs/2608.00017 (d18)
56. [M] Causal Memory Policy; EARM (2026). https://arxiv.org/abs/2610.02070 (d20)
57. [V] DeepSeek-R1 report, prompting note (2025). https://arxiv.org/abs/2501.12948 (d17)

### Cross-checks

58. critique.md in this folder: re-opened items 23, 24, 32, 33, 37, 38, 39 against the arXiv PDFs (text extracted, PDFs deleted); noted inconsistencies in a12 vs c14, in the no-hint rate, and in the Alfieri numbers.
