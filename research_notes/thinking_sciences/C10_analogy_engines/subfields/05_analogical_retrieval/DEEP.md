# Analogical retrieval (MAC/FAC): deep document

*Subfield C10.05. Written 2026-11-01 from evidence_a-d.jsonl, claims.jsonl (K01-K35) and critique.md in this folder. Marks: [V] = source opened and read this session; [M] = snippet or second-hand only. Status marks: [E] established, [S] single-source, [C] contested. Evidence ids (a01 ...) point to the jsonl files; claim ids (K01 ...) to claims.jsonl. Number conventions follow critique.md: FOR = .09 (not .03); the paper is 1995, not 1994; Cohen's d values from Raynal are quoted as reported and are not comparable with t values.*

---

## 1. What it is

**The problem.** An agent has a store of past cases (solved items, notes, traces). A new problem arrives. Which stored case should come to mind? This is retrieval. It comes before any mapping or transfer.

**The tension.** People retrieve by surface likeness: same objects, same words, same setting. But the cases that help are the ones with the same relational structure, often with a different surface. Retrieval that is blind to structure misses them. Retrieval that checks structure on every stored case is too slow.

**MAC/FAC (Forbus, Gentner and Law 1995).** A two-stage answer.
- **MAC** ("many are called"): a cheap, structure-blind score over all of memory. Each case is a vector that counts predicate types. The score is a dot product. Keep the best and anything within 10% of it.
- **FAC** ("few are chosen"): the full structure matcher (SME) runs only on the MAC survivors. Keep the best structural matches.

**Why it matters for our agent.**
1. It names the memory-retrieval slot our schema has not filled (SCHEMA section 5 "subgoal library", section 7 "analogy O7").
2. It says what the human default does: retrieval is surface-driven, and analogies surface rarely. An LLM trained on human text may inherit this.
3. It gives a design pattern that maps onto an LLM agent directly: a cheap filter (embedding or keyword), then an expensive structural judgment (an LLM call) on a short list.
4. It warns about the cost of the wrong match: surface matches feel good and are often unsound.

**What this document covers.** The founding human data, the model, the human replications and boundary conditions, the LLM work 2023-2026 (benchmarks, retrieval for agents, memory design, trigger rules), and what to test on our bench. The mapping step itself (SME, candidate inferences) belongs to sibling subfields (Candidate inferences, Analogical inference, Retrieval and similarity) and is only linked here.

**Honest scope note.** No published study tests the exact MAC/FAC idea (cheap filter, LLM structural rerank) against one-stage retrieval and context stuffing on an agent-built store at equal tokens. Everything on the LLM side is a proxy. Section 7 and UNKNOWNS.md keep that gap visible.

---

## 2. History and theories in depth

### 2.1 Before MAC/FAC: the inert-knowledge problem
- **Gick and Holyoak 1980, 1983** (second-hand [M], via a23, a19, b16): people read the fortress story (many small forces converge) and later get the radiation tumor problem. About 30% solve it unhinted; 80-90% when told to use the story. The knowledge is in memory but not accessed. This is the classic "inert analogy" result.
- **Ross 1984, 1987, 1989; Brooks 1987; Holyoak and Koh 1987; Keane 1988; Seifert et al. 1986** (cited in a19, a22, b04, [M]): remindings in problem solving follow surface content.
- **Rattermann and Gentner 1987** (second-hand through a04, a20, b02; original [M]): the key human retrieval study. See 2.3.
- **Gentner, Rattermann and Forbus 1993** (second-hand [M]; the PDF is a scan): the retrieval versus soundness dissociation. See 2.4.

### 2.2 Competing views at the time
- **Indexed case-based reasoning (Schank, Kolodner)** (a24 [V], as argued by FGL): store cases under hand-chosen structural indexes. FGL argue this wrongly predicts that the best structural match is usually retrieved, and it needs someone to design the indexes.
- **Spreading-activation and constraint-network models (ARCS, Thagard, Holyoak, Nelson and Gochfeld 1990)**: retrieval as settling of a constraint network. FGL show it is slow, sensitive to memory size, and gets the human order wrong (4.3).
- **Feature-vector retrieval (MAC alone)**: cheap, but blind to structure.

### 2.3 The founding human data (as cited by FGL 1995)
Rattermann and Gentner 1987, Experiment 2, as summarised in a04, a20, b02:
- 32 stories memorised (20 base stories, 12 distractors). After a delay (the 1995 paper says about a week; the 1991 paper says two weeks, so the delay is uncertain) people read 20 probes, 5 of each of four types, and wrote down any earlier story they were reminded of.
- Probe types: **LS** literal similarity (same objects and same relations), **SF** surface or mere appearance (same objects, different relations), **AN** true analogy (different objects, same relations), **FOR** first-order only (different objects, same first-order relations, no higher-order structure).
- Proportion reminded: **LS .56, SF .53, AN .12, FOR .09.** LS and SF did not differ significantly. The order held across three versions of the study (b02).
- Five criteria FGL derive from this (a03): surface superiority in retrieval, primacy of literal (mundane) matches, rare insights (analogies must sometimes surface), scalability, structural soundness of what comes back.

### 2.4 Retrieval is not soundness
Gentner, Rattermann and Forbus 1993 (second-hand, a22, b03, b04):
- Surface similarity best predicts what comes to mind. Shared higher-order structure best predicts what people rate as sound.
- People rated analogy and literal matches as more sound than surface and first-order matches. Yet surface matches were retrieved about as often as literal ones, and analogies about a quarter as often.
- The dissociation held between and within subjects. Adding higher-order relations to a probe gave a non-significant retrieval gain in two studies and a small gain in a third.

### 2.5 The model (1991 and 1995)
- **Gentner and Forbus 1991** (a20 [V]) is the first form. **Law, Forbus and Gentner 1994** (a21 [V]) is the head-to-head against ARCS.
- **FGL 1995** (a01-a12, b01-b09 [V]) is the full paper, Cognitive Science 19. The QRG file name says 1994; the volume is 1995.
- Design stance: a psychological model that must reproduce the human order, not a retriever that maximises accuracy. It "fails" on purpose by returning mostly literal and surface matches.

### 2.6 Later human work: the story gets more conditional
- **Gentner, Loewenstein, Thompson and Forbus 2009** (a13-a19, b10-b15 [V]): comparing two cases raises later retrieval of a structural match. See 3.2.
- **Raynal, Clement and Sander 2025; Raynal, Clement, Gros and Sander 2026** (a25-a29 [V]): with everyday memories and familiar structures, people retrieve distant analogues far more than surface-only matches. A video-clip paradigm agrees. This turns "surface always wins" into a conditional claim (K02).
- **Expertise and intensive encoding** (Novick 1988; Faries and Reiser 1988; Blanchette and Dunbar 2001, all [M] via FGL and Gentner 2009): relational retrieval is better for experts and for deeply encoded originals. Not opened.

### 2.7 AI descendants (2017-2026)
- **Purpose/mechanism indexes** (Hope et al. 2017, 2022): learned structural keys for products (a30, a31, b30).
- **LLM benchmarks of analogy recognition and retrieval** (ARN, StoryAnalogy, AnaloBench, BRIGHT, CPR-eval): all show embeddings are surface-bound (K10-K12).
- **Analogical prompting** (Yasunaga et al. 2024): skip the store, have the model write its own analogues (K17).
- **Experience memory for agents** (ExpeL, Buffer of Thoughts, AWM, Dynamic Cheatsheet, ReasoningBank, HippoSpark, RA-RFT): memory design and retrieval-trigger studies (K15, K16, K18, K26, K30).

---

## 3. Core findings with exact numbers

Status column: E established, S single-source, C contested. [V] opened, [M] second-hand.

### 3.1 Human retrieval and the MAC/FAC simulations

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Human retrieval order is LS > SF >> AN > FOR | .56, .53, .12, .09; 32 stories, 20 probes (5 per type), delay about a week | Rattermann and Gentner 1987 via FGL 1995 (a04, b02) [V citing paper, original M] | E (K01) |
| Retrieval and soundness dissociate | Surface matches retrieved about as often as literal ones; analogies about a quarter as often; soundness ratings run the other way | Gentner, Rattermann, Forbus 1993 via FGL and Gentner and Markman 1997 (a22, b03, b04) [original M] | E |
| Gick-Holyoak inert analogy | about 30% unhinted vs 80-90% hinted | Gick and Holyoak 1980/1983 via a23 [M] | E (K08) |
| 2025 business replication: hint effect is weaker | Factory 6.3% unhinted vs 8.7% hinted (4/46); HR 20.3% vs 37% (17/46); n=199; original 29% (8/28) vs 50% (14/28) | Puranam, Sen, Workiewicz 2025 (b16) [V] | E |
| Sim 1: MAC/FAC reproduces the order (18 stories: 9 base + 9 FOR distractors) | correct retrieval LS 1.0, SF 0.89, AN 0.67; MAC and FAC identical | FGL 1995 (a05, b05) [V] | S (K03) |
| Sim 2: FAC acts as a structural filter (36 stories) | MAC passes 3.4 items, FAC keeps 1.6; wrong-set items 1.33 at MAC, 0.22 at FAC; LS 0.78 | FGL 1995 (a06, b06) [V] | S |
| Sim 3: literal matches removed (27 stories) | SF 0.88 MAC / 0.78 FAC; FOR 0.56 / 0.56; other-set 1.11 / 0.11 | FGL 1995 (a07) [V] | S |
| Selector width matters | viable only with MAC 10-20% and FAC at least 10%; MAC 1% or FAC 1%: analogies never retrieved; MAC 30%+ with wide FAC: junk; unnormalised vectors shift the zone to MAC 30-50% | FGL 1995 (a08, b09) [V] | S (K04) |
| Content vector must mix attributes and relations | attribute-only fails; relation-only works in a narrow band (MAC 40-50%, FAC 20-70%) but MAC then passes many items; 11 x 11 grid, 121 runs, about 98,010 MAC executions | FGL 1995 (a09, b09) [V] | S |
| MAC/FAC vs ARCS: order and speed | ARCS activations LS .67, FOR -.11, SF -.17, AN -.27 (wrong order); Sour Grapes among 100 fables: MAC/FAC 0.2-0.3 s vs ARCS 81-123 s; with 25 plays added (125 items): 0.3-0.4 s vs 251-373 s; ARCS up to 614 s; some encodings did not settle in 1000 iterations (12 h) | FGL 1995; Law et al. 1994 (a10, a21, b07, b08) [V] | S (rival modellers) |
| Cost per operation (1990s Lisp) | MAC about 0.002 s per vector pair; SME 1-11 s per pair, about 4 s average | FGL 1995 (a02, b01) [V] | S |
| Hamlet and West Side Story probes | West Side Story: FAC gives Romeo and Juliet 16.51 and only it survives (MAC scored Othello .86, Macbeth .85, R&J .83). Hamlet: FAC 6.79, 5.49, 3.72, 2.67; drop-off 20% is under the 100% cutoff, so several plays return | FGL 1995 (a11) [V] | S |

### 3.2 Comparing before retrieving (Gentner et al. 2009)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Exp 1 (consultants): comparing two cases raises retrieval from own memory | retrieval rating 1.25 vs 0.82, t(122)=2.65, p<.01; N=124 (64 vs 60); full structural analogy retrieved 63% (40/64) vs 42% (25/60); linked the two cases 88% vs 17%; contingent agreements in the test negotiation 59% vs 33%, chi2(1,N=62)=4.22 | a13, b10 [V] | S (K05) |
| Exp 2 replication (accounting students) | retrieval 1.47 vs 0.59, t(34)=2.88; principle quality 1.42 vs 0.53; linked cases 95% vs 18%; N=36 | a14, b11 [V] | S |
| Exp 3 (second principle, single-case control) | comparison beats both controls (Dunnett p<.05); linked cases 100% vs 36%; trade-off articulation 1.17 vs 0.78 n.s. | a15, b11 [V] | S |
| Exp 4 (controlled memory: 7 cases, 30 min filler) | analogue recalled 27% vs 6%, chi2=6.12, N=73; surface-similar case recalled 30% vs 78% | a16, b12 [V] | S |
| Exp 5 (problem solving) | tumor 31% vs 5%, chi2=24.71, N=227; Red Adair 41% vs 30%, p=.08 n.s.; reminded 18% vs 14%; solved if reminded 81% (n=21) vs 33% (n=95) | a17, b13 [V] | S (K06) |
| Schemas in memory: MAC/FAC retrieves them far more than raw cases | Sim 1 FAC: story probe retrieved shallow matches 86% / 100%, analogies 14% / 0%; schema probe retrieved analogies 86%, shallow 29%, FOR 14%. Sim 2 (literals present): schema probe literal 71%, analogy 86%. Sim 3: FAC returned 57% schemas, 57% shallow, 14% analogies. Sim 4 (literals added): analogies 0% | a18, b14 [V] | S (K07), simulation only |

### 3.3 Conditional surface dominance (Raynal et al.)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Exp 1: cue shares surface and structure; close analogues win | close M=0.47 (SD .57) vs distant 0.09 (SD .31), t(132)=14.45, d=0.84; N=133; 502 memories (85.7% surface overlap, 63.6% surface + structure, 11.8% structure only) | a25 [V] (Raynal 2026) | E (K02) |
| Exp 2: familiar structure, unusual surface; distant analogues win | distant 0.46 (SD .68) vs surface-only 0.04 (SD .20), t(80)=12.06, d=0.82; N=81; 311 memories, 66.8% structure only; usual combos retrieved more (0.25 vs 0.06) | a26 [V] | E |
| Exp 3: surface stripped; usual combos still win | usual 0.26 vs unusual 0.01, t(94)=11.82, d=0.54; N=95; 411 memories, 82.24% full structure; usual combos fall from 0.47 (Exp 1) to 0.26 when cues lose surface, d=-0.40 | a27 [V] | E |
| Video clips: structure beats surface | Exp 1A: 71.68% structure-only, 18.58% surface-only, 9.74% neutral (113 single-source participants); Exp 2: 82.41% vs 10.19% vs 7.41% (N=99, chi2=60.83, phi=.78) | a28 [V] (Raynal 2025) | E |
| Control: surface cue is strong when nothing competes | 88.10% retrieved the surface lookalike (42 participants, chi2=28.9, phi=.86) | a29 [V] | E |
| Cohen's d caution | Reported d (0.84, 0.82, 0.54) do not match t/sqrt(n) (about 1.25, 0.9, 1.2); use the t values | critique.md | note |

### 3.4 Language models on analogy recognition and retrieval

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLMs recognise near analogies, fail far ones | ARN, 1,096 triples from 548 pairs, chance 50%: near analogy vs far distractor 76.9, near vs near 73.2, far vs far 45.3, far analogy vs near distractor 33.9; overall 57.3 (humans 98.6, 97.2, 96.8, 91.4; overall 96.0). Near 75.0 vs far 39.6 (humans 97.9 vs 94.1). SBERT alone: 77.9 easy setting, 42.3 average, about 1% on far | Sourati et al. 2024 (a32, b18, c10) [V] | E (K10) |
| CoT demonstrations that state each story's message help far analogies | up to +30 absolute points for GPT models; near analogies stay below zero-shot | ARN (b19, c11) [V] | S |
| StoryAnalogy: embeddings and LLMs pick the surface decoy | 4-way multiple choice, chance 25%: humans 85.7%, text-davinci-003 37.1%, Sultan and Shahaf model 44.9% | Jiayang et al. 2023 (c12) [V] | E |
| Analogies are rare in text | about 3% of a scientific corpus; SBERT top-100 precision 100% only because it finds self-analogies; structural mining FMQ 79%, FMV 72% | Sultan and Shahaf 2023 (b29, c13) [V; c29 M] | E (K23) |
| AnaloBench T1 (pick the analogy) | 340 human analogies, chance 25%; humans 96.0 (1 sentence), 72.5 (10), 73.3 (30); GPT-4 gap to humans 6.9 points at 1 sentence and 28.8 at 30 | Ye et al. 2024 (b20, c14) [V] | E |
| AnaloBench T2 (retrieve from a bank of 200) | GPT-4-turbo P@3 42.9% (1 sentence), 6.5% (10), 3.9% (30; random 3.9%); MAP 55.4 / 14.2 / 10.8; Claude-v2 1-sentence P@3 10.2% | b21, c15 [V] | E (K11) |
| Reasoning-intensive retrieval | BRIGHT, 1,384 queries, 12 datasets: best embedder nDCG@10 18.3 (24.3 best average) vs MTEB 59.0; BM25 average 14.5 | Su et al. 2025 (c16) [V] | E (K12) |
| LLM-written reasoning as the query | up to +12.2 nDCG@10; BM25 on GPT-4 reasoning tops the board | c17, d07 [V] | E (K13) |
| LLM reranking of top-k | BM25 base 14.3: GPT-4 top-10 17.4, top-100 17.0; Google base 19.5: 21.5 (k=10), 22.6 (k=100); MS MARCO cross-encoder worse (13.1 / 8.3 on BM25; 16.0 / 9.4 on Google) | d07 [V] | E |
| Cross-field idea retrieval | CPR-eval: 1,300 queries, 26 fields, 151 candidates (1 positive, 150 hard negatives); best retriever Recall@10 0.26 (chance 0.07); SPECTER2 0.09; LLM tournament reranker 0.81; 20.2 calls and $0.071 per query | Jung et al. 2026 (b22, d06) [V] | E (K12, K13) |
| Fine-tuned retriever | Recall@10 0.12 to 0.50, 0.17 to 0.69, 0.25 to 0.70 on cross-topic pairs (10,573); other training sets at most 0.13; HyDE with BM25 0.16 to 0.44 | b23 [V] | S (K14) |
| GPT-4 on Gick-Holyoak | no hint: 0 correct in 60 runs; hint: recall 1.00, precision .50-.52 (flags correct and wrong story); humans with hint precision .67-.75, recall .26-.39 | Puranam et al. 2025 (b17) [V] | S (K09) |
| Deep-research agents use no structural analogies | 0/22 past, 0/20 forward hidden factors for three commercial agents; CANA 13/22 (Sonnet-4.5), 7/22 (GPT-5.4), 1/22 (Qwen3-8B) | Chen et al. 2026 (b24, d05) [V] | S (K22) |

### 3.5 Retrieval for agents and in-context examples

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Learned usefulness beats similarity for examples | exact match: BREAK BM25 26.0, CBR 25.7, EPR 31.9 (oracle 43.1); MTOP 52.9 / 57.0 / 64.2; SMCalFlow 46.1 / 51.4 / 54.3; random 1.7 / 7.3 / 8.9 | Rubin et al. 2022 (c20) [V] | E (K15) |
| Structure coverage beats similarity | up to +23 points (SMCalFlow-CS 50.3 to 73.5); oracle coverage beat oracle similarity in 7 of 8 compositional splits; 24 demos | Levy et al. 2023 (c21) [V] | E |
| Self-generated analogues vs baselines | GSM8K 0-shot / 0-shot CoT / 5-shot CoT / ours: GPT-3.5 75.0 / 75.8 / 76.7 / 77.8; davinci-003 14.8 / 50.3 / 54.0 / 61.0; PaLM2 60.8 / 78.2 / 80.7 / 81.7. MATH GPT-3.5 33.0 / 33.9 / 34.9 / 37.3; PaLM2 27.1 / 29.8 / 34.3 / 34.8. Average gain about +4 | Yasunaga et al. 2024 (a33, d01) [V] | S (K17) |
| Generate vs retrieve by model size | GSM8K, curie / dav-001 / dav-002 / dav-003: 5-shot retrieved 3 / 11 / 47 / 57; self-generated 2 / 9 / 48 / 61; fixed 5-shot 2 / 10 / 43 / 54. Self minus retrieved: -1, -2, +1, +4 | d02 [V] | S (K35) |
| Codeforces | Acc@1 GPT-3.5: 3-shot CoT 11, exemplars 13, knowledge + exemplars 15; GPT-4: 17, 17, 19 | d03 [V] | S |
| ExpeL: task-similarity retrieval | ALFWorld ReAct 40.0, random successes 42.5, reasoning-similarity retrieval 48.5, task-similarity (ExpeL) 59.0. Insights-only vs retrieve-only: HotpotQA 36 vs 31, ALFWorld 50 vs 55, WebShop 37 vs 38 | Zhao et al. 2024 (c22, d12) [V] | S (K18) |
| Start-of-task experience retrieval can hurt | HippoSpark GPT-5.4-mini: vanilla .326, Trajectory Experience .255, ReasoningBank .306, HippoSpark without experience .409, with experience .483. Qwen3-14B: .283, .261, .330, .368 | Liu et al. 2026 (b27, d13) [V] | C (K16) |
| Embedding retrieval no better than a random trace | RA-RFT Qwen3-1.7B: GRPO 43.3; RA-RFT 47.4; Qwen3-Embedding-4B 38.5, fine-tuned 40.5; Reason-ModernColBERT 40.7, fine-tuned 47.4; random trace 37.6 | Xiao et al. 2026 (b28, d15) [V] | C (K16) |
| Distilled memory beats raw cases | AWM Mind2Web step SR 34.6 vs Synapse 30.6 (gpt-3.5), 45.1 vs MindAct 36.2 (gpt-4); ReasoningBank WebArena 48.8 vs Synapse 42.1, AWM 44.1, no memory 40.5; Dynamic Cheatsheet Claude 3.5 Sonnet AIME 2024 baseline 23.3, raw retrieval 43.3, curated 50.0, retrieve + synthesize 46.7; full-history appending 26.7 | d09, d10, d11 [V] | E (K26) |
| More injected items hurt | ReasoningBank retrieved-count curve 49.7 (1), 46.5 (2), 45.5 (3), 44.4 (4) (probably one domain); full-history GPT-4o AIME 2024 6.7 vs baseline 20.0; stuffing 20-30 documents falls below closed-book 56.1 | d11, d09, d19, d20 [V] | E (K27) |
| Gate retrieval | FLARE good at 40-80% of sentences, worse above 50-60%; PopQA adaptive retrieval for about 40% of questions with davinci-003; Self-RAG always-top-1 41.8 on PopQA in the ablation; HippoSpark 10.67% of AIME instances needed no retrieval and reached 71.88% | d13, d16, d17, d18 [V] | E (K30) |
| Retrieve first, escalate on "cannot tell" | Self-Route: GPT-4O 48.89 vs long-context 48.67 at 61.40% of tokens; Gemini 46.41 vs 49.70 at 38.39%; GPT-3.5 35.32 vs 32.07 at 38.85%; RAG and long-context agree on over 60% of queries | Li et al. 2024 (d08) [V] | S (K29) |
| Purpose/mechanism keys | precision at top 1%: purpose-only 0.739, mechanism-only 0.696, TF-IDF 0.630, LSA 0.413, LDA 0.435; ideation: good ideas 46% (N=105) vs 37% random (49) vs 30% TF-IDF (54), p<=.01 | Hope et al. 2017 (a30, a31) [V] | E (K19) |

---

## 4. Mechanisms and models

### 4.1 MAC/FAC as an algorithm
```
# memory: list of cases; each case has (a) a structured description, (b) a content vector
def content_vector(description):
    v = {}
    for pred in all_predicates(description):      # attributes, relations, connectives
        v[pred.functor] += 1                      # count of each predicate type
    return v

def MAC(probe, memory, width=0.10):
    pv = content_vector(probe)
    scores = {c: dot(pv, c.vector) for c in memory}   # about 0.002 s per pair in 1990s Lisp
    best = max(scores.values())
    return [c for c in memory if scores[c] >= best*(1-width)]

def FAC(probe, candidates, width=0.10):
    scores = {c: SME(probe, c).structural_score for c in candidates}  # 1-11 s per pair
    best = max(scores.values())
    return [c for c in candidates if scores[c] >= best*(1-width)]

retrieved = FAC(probe, MAC(probe, memory))
```
Facts from the paper (a01, a02, a08, a09):
- The dot product estimates how many match hypotheses SME would build. It usually overestimates (it ignores argument alignment) and can underestimate (it ignores non-identical functions).
- Variants: raw counts, normalised, binary presence. Normalisation did not matter; selector width did.
- The vector needs attributes, relations and logical connectives together. Attribute-only vectors fail. Relation-only vectors work only in a narrow band.
- Selector width has no theory-given value. The human fit needs MAC 10-20% and FAC at least 10%.
- Failure mode: retrieval fails only if FAC rejects every MAC survivor. The authors say false negatives are cheaper than false positives because retrieval is iterative: re-represent the probe and try again (a12).
- Known scaling issue: the vector grows with the predicate vocabulary.

### 4.2 Why the two stages produce the human pattern
MAC picks whatever shares predicate types with the probe. Cases with shared objects and relations (LS, SF) pass in large numbers. Analogies share relations but not object types, so their MAC score is lower. They pass mainly when no literal match is in memory. FAC then keeps the best structural matches among the survivors. This gives "surface wins, analogy sometimes" without a rule that says so. When literal matches are removed from memory, surface and analogy matches rise (Sim 3).

### 4.3 The ARCS rival
ARCS is a constraint network over word-level similarity (WordNet-based). In FGL's runs it ranked the base story low, got the order LS, FOR, SF, AN, took 17-614 s per probe, changed answers when memory grew by 25%, and hinted at a size bias. The comparison was run by MAC/FAC's authors on ARCS's own encodings (a10, a21, b07, b08). Treat the speed claim as credible in shape and not as an independent benchmark.

### 4.4 Comparison before retrieval (the 2009 mechanism)
Gentner et al. propose that comparing two analogous cases yields a schema: a relational abstraction with about 80% relational predicates against about 40% in a base story (a18). The schema, used as a probe, matches stored analogues in MAC. Comparison also suppresses surface features, so the surface-similar case is recalled less (30% vs 78%, Exp 4). Two accounts remain open (b15): a schema account (the abstraction is stored) and an encoding account (richer encoding of the original). The experiments did not separate them.

### 4.5 The LLM translation of MAC/FAC (a design, not an established result)

| MAC/FAC part | LLM-agent version |
|---|---|
| Structured description | The agent's short abstract of the case: purpose, mechanism, key relations, outcome (cf. Hope purpose/mechanism, CANA decomposition, ReasoningBank items) |
| Content vector + dot product | Embedding or keyword score over those abstracts (cheap, whole store) |
| MAC width | Shortlist of 10-40 (K28; the first cut of 151 to 40 lost 8.3% of positives in CPR) |
| SME structural score | One LLM call per survivor, or a tournament: extract a role-by-role mapping, then check against a reject list (same problem, background only, unsupported mapping; kappa 0.84, n=50) |
| FAC width | Keep the top 1-3 (1 item was best in ReasoningBank; 3-5 for in-context examples in Yasunaga) |
| Re-represent and retry | Rewrite the query into abstract form (HyDE; BRIGHT reasoning-as-query up to +12.2 nDCG@10) and retrieve again |

Cost anchor: CPR's reranker used 20.2 LLM calls and $0.071 per query on 151 candidates. A 10-40 shortlist with one call each is the same order or cheaper.

### 4.6 Cue design: what raises structural retrieval for people and what might for a model
- Familiar named structures (making up an excuse, pretending to like a gift) with unusual surfaces: distant analogues win (a26).
- Stripped cues still favour usual surface/structure combinations (a27): association frequency matters.
- Stored schemas beat stored raw cases in simulation (b14).
- Comparison at probe time lifts structural retrieval (b12).

All four point to one engineering lever: store and query at the level of abstract, named structure rather than raw text. For a model, only the schema-versus-raw-trace piece has indirect support (K26).

### 4.7 Trigger design (when to retrieve)
From four independent papers (d13, d16, d17, d18; K30):
- Retrieve on demand, when the solver reports no clear next move or low confidence.
- Query with the current situation plus the local goal, not the original task text.
- Cap the calls: HippoSpark gains turned unstable after about 5 calls.
- Inject little: 1 item was best in ReasoningBank.
- The gate threshold shifts with model strength.

---

## 5. What holds up

### 5.1 Replications and independent confirmations

| Claim | Evidence | Verdict |
|---|---|---|
| Surface similarity drives spontaneous retrieval | FGL 1995 via Rattermann and Gentner 1987; Gick-Holyoak; Raynal Exp 1 (close beats distant, d=0.84); Raynal control 1B (88.10% surface lookalike when nothing competes); Puranam 2025 low unhinted rates | Holds under the classic cue design [E] |
| Hints turn analogy use on | Gick-Holyoak 30% vs 80-90%; Puranam 2025: 6.3% vs 8.7%, 20.3% vs 37% | Direction holds; the size is smaller in the 2025 business replication [E] |
| Comparison improves retrieval | Four experiments in one lab (Gentner 2009), different samples | Replicated within the lab only; no outside replication found [S] |
| Embeddings and LLMs are surface-bound for analogy | ARN, StoryAnalogy, AnaloBench, BRIGHT, CPR-eval | Holds across four to five independent benchmarks [E] |
| Structure-labelled keys beat text keys | Hope 2017 (0.739 vs 0.630), Hope 2022 (MAP 85-87% vs 40-60%, crowd evaluations), CANA | Holds in two domains; crowd judges, noisy extraction [E] |
| Distilled memory beats raw cases | AWM, ReasoningBank, Dynamic Cheatsheet | Three independent agent papers; task success, not a retrieval metric [E] |
| Gate retrieval | FLARE, PopQA, Self-RAG, HippoSpark | Four sources, QA and reasoning tasks; no analogue-retrieval test [E] |

### 5.2 Failed or contested results
- **"Surface always dominates" is not universal.** Raynal et al. 2025-2026: with familiar structures and unusual surfaces, distant analogues get 0.46 vs surface 0.04 (N=81); video clips 71.7-82.4% structure vs 10-19% surface. This does not refute the classic result (different cues, everyday memories, not a story set) but narrows it. Lab stimuli may be encoded shallowly (a27).
- **Compare-then-solve does not carry everywhere.** Red Adair 41% vs 30% (p=.08), and explicit reminding was equally rare (18% vs 14%) (a17).
- **Gentner 2009 retrieval is still low in absolute terms.** 27% analogue recall even in the best condition, one analogue among seven cases.
- **Free recall of autobiographical cases is hard to verify.** 66% of examples were own or colleagues' experience; confabulation risk. Exp 4 was added to rule it out.
- **Task-level experience retrieval is contested for LLM agents.** Positive: ExpeL 59.0 vs 40.0. Negative: HippoSpark trajectory retrieval .255 vs vanilla .326; RA-RFT embedding retrieval 38.5 vs random 37.6 and GRPO 43.3. The critique notes that the HippoSpark gain (.326 to .483) mostly comes from state assessment plus verification (.409 before any experience); experience adds .074. The likely cause of the disagreement is the retrieval key and the benchmark.
- **LLM analogy ability is fragile.** Lewis and Mitchell 2024: humans .753, GPT-3 .488, GPT-3.5 .350, GPT-4 .452 on letter strings (a partial failed replication of Webb et al. 2023). Stevenson et al. 2025: each LLM falls from Latin to Greek to symbol alphabets (p<.001 for all but Llama-3.1 405B); children and adults do not. These are recognition tasks, not memory retrieval.
- **Webb et al. 2023** (c09): GPT-3 picked the causally matching story (combined p=.0005; near p=.0039) but not reliably in the far condition; humans beat GPT-3 (OR 0.37, p=.0003).
- **The MAC/FAC evidence base is one lab.** Simulations on 18-125 hand-encoded stories; the ARCS comparison was run by the MAC/FAC authors; no realistic memory size; no LLM as encoder.
- **Few-shot can hurt reasoning models.** The DeepSeek-R1 report advises zero-shot (d04, qualitative).

### 5.3 Moderators

| Moderator | Effect | Evidence |
|---|---|---|
| Distance (near vs far) | Near 75% vs far 39.6% for LLMs; humans flat | a32, c10 |
| Story length | AnaloBench GPT-4 gap 6.9 (1 sentence) to 28.8 (30 sentences); T2 P@3 42.9% to 3.9% | b20, c15 |
| Familiarity of the structure | Distant analogues win when the structure is familiar | a26 |
| Unfamiliar symbols | LLM accuracy falls; humans flat | c25, c26, d23 |
| Expertise and depth of encoding | More relational retrieval for experts and intensive encoding (second-hand) | a24, b15 |
| Memory size and coverage | 20 items gave weaker top-1 (0.676) than 112 items (0.751); analogies about 3% of text | d14, b29 |
| Presence of literal matches | Literals crowd out analogies and schemas (Sim 4: analogies 0%) | b14 |
| Model strength | Retrieved exemplars win to davinci-001; tie at davinci-002; self-generated wins at davinci-003; self-generated exemplar gain on Codeforces +2 (GPT-3.5) to 0 (GPT-4) | d02, d03 |
| Number of injected items | 1 best; more lowers success | d11, d19, d20 |

### 5.4 Interventions that worked
- LLM reranking of a shortlist (CPR 0.26 to 0.81; BRIGHT +3.1 at k=10).
- LLM-written reasoning or an abstract rewrite as the query (up to +12.2 nDCG@10).
- Fine-tuning on cross-topic pairs with same-topic hard negatives (0.12 to 0.50 etc.). Not available to a scaffold-only agent.
- Chain-of-thought demonstrations that first state each story's message (up to +30 points on far ARN).
- Structural decomposition before retrieval (CANA 13/22 vs 0/22), though the margin over plain self-reflection is small for strong models (sonnet-4-6 4.17 vs 4.11).
- Distilled, abstracted memory entries (ReasoningBank, AWM, Dynamic Cheatsheet).
- On-demand retrieval gated on a stuck signal.
- Human hints (Larraz and Corma 2026: Stokes law used 0/20 baseline vs 18/20 guided; success 10% vs 100%). This tests a hint, not retrieval; one 7B model and one case limit it (a35).

### 5.5 Interventions that did not work
- Raw embedding similarity for far analogies (SBERT about 1% on far; best retriever 0.26 on CPR-eval).
- Training a retriever on web search, citation or reasoning-retrieval data (at most 0.13).
- An MS MARCO cross-encoder for reranking reasoning-intensive queries (lowered scores).
- Widening the LLM rerank pool from 10 to 100 (-0.4 to +1.1 nDCG).
- Stuffing the bank into context (AnaloBench T2 near random; 20-30 documents below closed-book).
- Appending full history (GPT-4o 6.7 vs 20.0 baseline on AIME 2024).
- Plain solved demonstrations for near analogies (they hurt).
- Case-based retrieval with fine-tuned embeddings: +1.94% semantic similarity only (c28; 32 cases, 7B generator).
- Retrieving whole-task traces at the start with an untrained model (RA-RFT, HippoSpark; contested).

---

## 6. Language models

### 6.1 Recognition versus retrieval
Most LLM analogy tests are forced choice (ARN, StoryAnalogy, AnaloBench T1). They show that a model can recognise a relational match when the surface helps. Retrieval from a store is harder. Only AnaloBench T2, CPR-eval, BRIGHT and CANA test something like it.

### 6.2 Behaviour by setting

| Setting | Result | Change that moved it | Size of change |
|---|---|---|---|
| Pick the analogy, near | about 75% (random 50%) | none needed | n/a |
| Pick the analogy, far | 39.6%, below chance | CoT demonstrations stating each story's message | up to +30 points |
| Pick among 4 with a surface decoy (StoryAnalogy) | 37.1% (humans 85.7%) | none tested here | n/a |
| AnaloBench T1 (30-sentence stories) | GPT-4 28.8 points under humans | larger models | little at 10-30 sentences |
| AnaloBench T2 retrieval from 200 | P@3 3.9% at 30 sentences (random 3.9%) | fine-tuned retriever | nDCG@10 +0.04 to +0.12 |
| BRIGHT (reasoning-intensive) | best embedder 18.3-24.3 nDCG@10 | LLM reasoning as query; GPT-4 rerank | +12.2; +3.1 |
| CPR-eval | 0.26 Recall@10 | LLM tournament rerank; fine-tuning | 0.81; 0.50-0.70 |
| Gick-Holyoak with GPT-4 | 0/60 correct without hint | hint | recall 1.00, precision about 0.5 |
| Deep-research agents, hidden factors | 0/22 | decompose then retrieve (CANA) | 13/22 with Sonnet-4.5 |
| Letter-string analogy | GPT-4 .452 vs humans .753 | familiar alphabet | accuracy falls with each alphabet change |

### 6.3 Profile in one paragraph
Models and sentence embeddings are surface-bound, like people, but without the human gain from familiar structure. Given a hint, GPT-4 flags the right story every time and the wrong one as often (precision about 0.5). So the weak step is verifying the match, not recalling candidates. An LLM used as a reranker over a short list recovers most of the structure that embeddings lose (0.26 to 0.81). Rewriting the query into abstract form helps further.

### 6.4 Generate or retrieve
Yasunaga et al. 2024 show that a model can write its own analogues instead of retrieving them. The trade depends on model strength. In 2022-era models retrieval won to davinci-001 and tied at davinci-002; self-generation won by 4 points at davinci-003. Newer signals point the same way but are indirect: the self-generated exemplar gain on Codeforces falls from +2 (GPT-3.5) to 0 (GPT-4); CANA's lead over self-reflection falls from +0.67 (gpt-5.4-mini) to +0.06 (sonnet-4-6); DeepSeek-R1 says few-shot hurts. No direct test on frontier models. Expect self-generation to be enough unless the store holds knowledge the model lacks.

### 6.5 Memory design for agents
Distilled entries beat raw traces on task success in three independent papers. The retrieved count should be small. Triggering on a stuck signal beats always-on retrieval. Whole-task retrieval at the start is contested. Nobody measured structural retrieval rate directly.

### 6.6 What is missing
No study uses an LLM as the encoder inside MAC/FAC, tests cheap filter plus LLM rerank against one-stage and stuffing at equal tokens on an agent-built store, or replicates the compare-then-retrieve effect in a model. All 2026 arXiv numbers (HippoSpark, RA-RFT, ADR, CPR) are single preprints without peer review.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5. Status: [E] established, [S] single-source, [C] contested.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Do not treat surface similarity as a sign of relevance.** Embedding retrieval returns surface matches, and surface matches feel sound and often are not. Any retrieved case must pass a structure check before use (see A6). | G (guardrail candidate) and O7 | [E] | K01, K10, K12; a04, a22, a32, c16, d06 |
| A2 | **Two-stage retrieval shape: cheap shortlist, then an LLM structural judgment on 10-40 survivors.** An LLM rerank beats the best single-vector retriever on cross-topic retrieval (0.81 vs 0.26). Do not widen to 100. | memory | [E] for the rerank (K13); shortlist size [S] (K28) | b22, d06, d07, c17 |
| A3 | **Inject at most 1-2 retrieved cases, best first.** More items lower success; stuffing the store is worse than none. | memory | [E] | K27; d11, d09, d19, d20 |
| A4 | **Store distilled entries (situation, mechanism, outcome), not raw traces.** Three agent papers favour distilled memory on task success. Matches our "lessons, one line each" rule in SCHEMA section 5. | memory | [E] on task success; the structural-retrieval claim is [S] (K07) | K26; d09, d10, d11 |
| A5 | **Retrieve on a signal, not at the start of every item:** use the stuck signal or impasse detector. Fits G1 (doubt only on a signal) and keeps analogy at S6. | S6 / G1 | [E] for gating (K30); start-of-task retrieval [C] (K16) | d13, d16, d17, d18, b27, b28 |
| A6 | **Verify the mapping after retrieval.** A hint raises analogy use, but GPT-4 flags the right and the wrong story alike (precision about 0.5). Retrieval must be followed by a mapping check in code or an independent call. | O7 + G | hint effect [E] (K08); LLM precision [S] (K09) | a23, b16, b17 |
| A7 | **Expect most items to have no true analogue.** Analogies are about 3% of a text corpus; small stores give weak best matches. Log top-1 similarity and the verifier verdict. Allow "no analogue found" without penalty and fall back to the plain path (G6, G7). | memory + S0 | [E] for rarity (K23); store-size effect [S] (K31) | b29, d14, d22 |
| A8 | **Index on structure-labelled keys (purpose and mechanism), not raw text.** The agent writes a purpose/mechanism summary at store time and the index uses that. | memory | [E] (K19) | a30, a31, b30 |
| A9 | **Keep analogy at impasses and in open mode only.** Far analogues are the hard case for models and the base rate is low. This agrees with SCHEMA O7. | O7 | [E] | K10, K23 |

### 7.2 Test first (not yet in the schema)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Cheap filter + LLM structural rerank vs one-stage top-k vs stuffing, at equal tokens, on a store the agent builds.** The central MAC/FAC claim. No head-to-head exists. | memory | [S] (K03) | b22, d06, d08 |
| T2 | **Rewrite the query into an abstract form (problem class, mechanism, constraint) before retrieval.** Up to +12.2 nDCG@10 on BRIGHT; HyDE 0.16 to 0.44 on CPR. | memory / S1 | [E] on retrieval benchmarks (K13); [S] for agents | c17, b23 |
| T3 | **Compare two solved items and write one shared principle, then retrieve on it.** The Gentner 2009 effect; no LLM test. | O1 / S-retrieve | [S] (K05, K33) | a13, a16, d12 |
| T4 | **Schema notes vs raw traces for cross-domain retrieval.** Simulation says schemas win; agent papers say distilled wins on success. | memory | [S] (K07) | b14, K26 |
| T5 | **Retrieve at start vs at stuck point with the same key.** Contested; the key is the likely cause. | memory / S6 | [C] (K16) | b27, b28, c22 |
| T6 | **Mapping-plus-reject-list verifier for false analogies.** Role-by-role mapping, then a check against a reject taxonomy; independent narrow checks. | G / O7 | [S] (K32) | d21, d22 |
| T7 | **Self-generated analogues vs retrieved cases on current models.** Expect self-generation to be enough. | O1 / memory | [S] (K17, K35) | d02, d03, d05 |
| T8 | **Named-pattern labels in the index** (bottleneck, hidden invariant, conservation). | memory | untested (K34) | a26, d23 |
| T9 | **Decompose-then-retrieve vs reflect-then-retrieve.** The CANA margin shrinks with strength (4.17 vs 4.11). | O3 / S2 | [S] (K22) | b24, b25 |
| T10 | **Shortlist size sweep (10, 20, 40, 100) on the agent's own store.** | memory | [S] (K28) | d06, d07 |
| T11 | **Escalate from 1-2 retrieved cases to more context only on a "these do not help" flag.** Knowledge QA evidence only. | memory | [S] (K29) | d08 |
| T12 | **Coverage-based example selection (needed sub-structures) vs top-k similarity.** | memory | [E] on semantic parsing (K15); untested for agents | c20, c21 |

---

## 8. Concrete tests on our bench

All arms get the same token budget, including setup, store building and verifier calls (G7). Items come from our suites (ARC-style puzzles, BrainTeaser-style riddles, and a planted-twin set built from them). Report mean, spread and per-item flips (right to wrong, wrong to right).

**Shared fixture: the planted-twin set.** Build a store of solved items with abstract notes. For each probe, mark whether (a) a structural twin exists with a different surface, (b) a surface decoy exists with a different structure, (c) neither exists. Use roughly 40% (a), 30% (b), 30% (c), so the base rate is not the 3% of natural text. Report the natural-rate result separately by re-running with the real mix.

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| B1 | Two-stage vs one-stage vs stuffing (T1) | planted-twin probes | (1) embedding top-1; (2) embedding top-20 then LLM rerank to 1-2; (3) whole store in context; (4) no memory | Twin-hit rate in the injected set; decoy-hit rate; task accuracy; tokens | Arm 2 beats arm 1 on twin-hit by 20+ points on far twins (CPR shape 0.26 to 0.81); arm 3 no better than arm 4 |
| B2 | Query rewrite (T2) | same | raw query vs abstract rewrite vs rewrite + raw | Twin-hit rate | +5 to +15 points on far twins |
| B3 | Compare-before-retrieve (T3) | pairs of solved items with known twins | retrieve on item A; retrieve on item B; compare A and B, write one principle, retrieve on the principle | Twin-hit rate; decoy-hit rate | Principle arm has higher twin-hit and lower decoy-hit (human: 27% vs 6%; 30% vs 78%) |
| B4 | Schema notes vs raw traces (T4) | store built from 100+ solved items | index on raw trace; on a (situation, mechanism, outcome) note; on a purpose/mechanism pair | Structural-match rate at top-1; task accuracy | Notes beat raw traces on cross-surface twins; purpose/mechanism pair beats free-form note |
| B5 | Trigger rule (T5) | full bench items, mix of easy and stuck | no retrieval; retrieve at S1; retrieve at S6 only; both; same key (situation + local goal) | Accuracy at equal tokens; flips; retrieval calls | S6-only at least ties start-of-task and costs less; start-of-task lowers easy-item accuracy |
| B6 | Verifier (T6) | probes with planted surface decoys | use top-1 unchecked; role-by-role mapping check; mapping + reject taxonomy; independent narrow checks | False-positive rate (decoy used); twin kept rate; tokens | FP rate halves with a small loss of true hits; target precision above 0.8 (GPT-4 baseline about 0.5) |
| B7 | Shortlist size (T10) | store of 500-2000 items | k = 10, 20, 40, 100 into the rerank | Recall of the twin in the final set; calls and tokens | Plateau between 20 and 40 |
| B8 | Generate vs retrieve (T7) | same item set | no help; 3 self-generated analogues; 1-2 retrieved cases from own store | Accuracy | Self-generation about equal or better unless the store holds facts the model lacks |
| B9 | Named labels (T8) | twins with unusual surfaces | index with vs without a pattern name | Twin-hit rate | Gain larger for familiar named structures than for new ones |
| B10 | Decompose vs reflect (T9) | open-mode items | decompose then retrieve; reflect then retrieve; direct | Quality score; twin use | Margin small for strong models (CANA 4.17 vs 4.11) |
| B11 | Base-rate log | all natural runs | log top-1 similarity, verifier verdict, whether an analogue existed | How often a true analogue exists | Under 10% of items; sets the ceiling on any retrieval gain |
| B12 | Injected-count curve | any retrieval arm | 0, 1, 2, 4 items, best first | Accuracy and flips | Peak at 1-2; fall after (ReasoningBank 49.7 to 44.4) |

---

## 9. What does not transfer, and why

- **Human memory decay and delay.** The 1987 data use a week's delay and 32 stories. An LLM store has no forgetting; its failure is crowding, not decay.
- **"Surface dominates" as a law.** For people it depends on cue design (Raynal). For a model we do not know; the evidence is for surface-bound embeddings, not for a human-like dominance.
- **Hand-encoded predicate calculus.** FGL's content vectors count predicates in a clean propositional encoding. Text has no such encoding. Building one with an LLM adds cost and noise, and nobody has tested it.
- **Tiny memory sizes.** 18-125 stories. The timings (0.002 s, 1-11 s) are 1990s Lisp.
- **The ARCS speed claim.** Run by rivals on the other model's encodings; the shape is credible, the magnitudes are not portable.
- **Selector widths of 10-20%.** On a 1000-item store that is 100-200 items for the LLM stage. Evidence says 10-40 is enough (K28).
- **Free recall of autobiographical cases.** Gentner 2009 Exp 1-3 measure memory for real events. The agent retrieves from a log it can search.
- **Fine-tuning retrievers.** Large gains (0.12 to 0.50) need training. A scaffold-only agent cannot do this. It must supply the structure through rewrite, abstraction and rerank.
- **RA-RFT, trained retrievers, Self-RAG training.** They train the policy with the retriever. Our agent does not train.
- **Hint studies as retrieval.** Larraz and Corma (0/20 vs 18/20) and the Gick-Holyoak hint cells show the model can use a given analogy, not that it finds one.
- **Knowledge QA gating results** (Self-Route, FLARE, PopQA). Useful for trigger and cost shape, not for analogue retrieval.
- **The comparison effect with an LLM.** In people, comparing two cases builds a schema. An LLM writing a "shared principle" may only paraphrase, and the effect may not hold.
- **Debate-style variants.** Several agents arguing about which case matches stay excluded by G9.

---

## 10. Open questions

1. Does cheap filter + LLM rerank beat one-stage top-k and stuffing at equal tokens on a self-built store? (No test found.)
2. How often does a true structural analogue exist in an agent's own memory? Retrieval gains cap at that base rate.
3. Does writing memory as abstract schemas raise structural retrieval for LLMs, as simulations say for MAC/FAC? Nobody measured retrieval rate directly.
4. Does comparing two cases before retrieval help an LLM?
5. Do familiar named structures raise structural retrieval in LLMs, as Raynal suggests for people?
6. When does self-generation beat retrieval for current frontier and reasoning models? Only 2022-era models were tested directly.
7. What is the right trigger and key for retrieval on analogue tasks: start, stuck point, or both? Same-key comparisons are missing.
8. What is the cheapest false-analogy filter that works on analogies? CoVe and CPR's mapping check are candidates. None is tested on analogues, and no token costs are given.
9. What shortlist size works at thousands of items?
10. Is the human retrieval order a real feature of LLMs, or only of embedders? A direct replication of the 32-story design with an LLM agent and a store of similar size is missing.
11. Do the Rattermann and Gentner 1987 and Gentner 1993 numbers hold up? We rely on second-hand reports.
12. Is Gentner 2009's retrieval benefit independent of the lab? No outside replication was found.
13. Is the HippoSpark experience gain (.074 over .409) real at larger test sizes? AIME sets are 30 problems per year.

---

## 11. Sources

Marks: [V] opened and read this session; [M] snippet or second-hand only.

**Human retrieval and the model**
- [V] Forbus, Gentner and Law (1995), MAC/FAC: A model of similarity-based retrieval, Cognitive Science 19. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_1994/Forbus_1994_MAC_FAC_Model_Similarity-Based_Retrieval_CogSci.pdf (and the -v2.pdf copy in the same folder) (a01-a12, b01-b09, c01-c08)
- [V] Gentner and Forbus (1991), MAC/FAC: A model of similarity-based retrieval. https://www.qrg.northwestern.edu/papers/Files/macfac91(searchable).pdf (a20)
- [V] Law, Forbus and Gentner (1994), Simulating similarity-based retrieval. https://groups.psych.northwestern.edu/gentner/papers/LawForbusGentner94.pdf (a21)
- [V] Gentner and Markman (1997), Structure mapping in analogy and similarity, American Psychologist. https://www.qrg.northwestern.edu/papers/Files/Gentner_Markman_AmPsy_Jan97.pdf (b04)
- [V] Gentner, Loewenstein, Thompson and Forbus (2009), Reviving inert knowledge, Cognitive Science 33. http://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2009/Gentner,Loewenstein,Thompson&Forbus_2009-1.pdf (a13-a19, b10-b15)
- [V] Raynal, Clement, Gros and Sander (2026), Bridging the retrieval gap. https://pmc.ncbi.nlm.nih.gov/articles/PMC13719747/ (a25-a27)
- [V] Raynal, Clement and Sander (2025), The role of surface and structural similarity. https://pmc.ncbi.nlm.nih.gov/articles/PMC11724687/ (a28, a29)
- [V] Puranam, Sen and Workiewicz (2025), Can LLMs help improve analogical reasoning for strategic decisions? https://arxiv.org/abs/2505.00603 (b16, b17)
- [M] Rattermann and Gentner (1987); Gentner, Rattermann and Forbus (1993); Gick and Holyoak (1980, 1983); Ross (1984, 1987, 1989); Brooks (1987); Holyoak and Koh (1987); Keane (1988); Seifert et al. (1986); Novick (1988); Faries and Reiser (1988); Blanchette and Dunbar (2001); Thagard et al. (1990) ARCS; Kurtz and Loewenstein (2007). Numbers reached only through the opened papers above.

**LLM analogy benchmarks and retrieval**
- [V] Sourati, Ilievski, Sommerauer and Jiang (2024), ARN. https://arxiv.org/abs/2310.00996 (a32, b18, b19, c10, c11)
- [V] Jiayang et al. (2023), StoryAnalogy. https://arxiv.org/abs/2310.12874 (c12, c13)
- [V] Ye et al. (2024), AnaloBench. https://arxiv.org/abs/2402.12370 (b20, b21, c14, c15)
- [V] Su et al. (2025), BRIGHT. https://arxiv.org/abs/2407.12883 (c16, c17, d07)
- [V] Jung et al. (2026), Cross-Pollination Retrieval. https://arxiv.org/abs/2610.25678 (b22, b23, d06, d22)
- [V] Chen, Chen, Sun and Zhang (2026), Analogical Deep Research. https://arxiv.org/abs/2607.13602 (b24, b25, d05)
- [V] Sultan and Shahaf (2023), Life is a circus and we are the clowns. https://arxiv.org/abs/2210.12197 (b29); [M] c29 (via StoryAnalogy)
- [V] Webb, Holyoak and Lu (2023), Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (c09)
- [V] Lewis and Mitchell (2024), Using counterfactual tasks. https://arxiv.org/abs/2402.08955 (c25, d23)
- [V] Stevenson, Pafford, van der Maas and Mitchell (2025), Can large language models generalize analogy solving like people can? https://arxiv.org/abs/2411.02348 (c26)
- [V] Yuan et al. (2023), Beneath surface similarity (SCAR). https://arxiv.org/abs/2305.12660 (c27)
- [V] Larraz and Corma (2026), Human analogical guidance amplifies LLM performance. https://pmc.ncbi.nlm.nih.gov/articles/PMC13223311/ (a35)
- [V] Wiratunga et al. (2024), CBR-RAG. https://arxiv.org/abs/2404.04302 (c28)

**Structure-labelled indexes**
- [V] Hope, Chan, Kittur and Shahaf (2017), Accelerating innovation through analogy mining. https://arxiv.org/abs/1706.05585 (a30, a31)
- [V] Hope et al. (2022), Scaling creative inspiration with fine-grained functional aspects of ideas. https://arxiv.org/abs/2102.09761 (b30)

**Prompting and in-context examples**
- [V] Yasunaga et al. (2024), Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714 and https://ar5iv.labs.arxiv.org/html/2310.01714 (a33, a34, b26, c18, c19, d01-d03)
- [V] Rubin, Herzig and Berant (2022), Learning to retrieve prompts. https://arxiv.org/abs/2112.08633 (c20)
- [V] Levy, Bogin and Berant (2023), Diverse demonstrations improve in-context compositional generalization. https://arxiv.org/abs/2212.06800 (c21)
- [V] Yu et al. (2024), Thought Propagation. https://arxiv.org/abs/2310.03965 (c23)
- [V] DeepSeek-AI (2025), DeepSeek-R1. https://arxiv.org/abs/2501.12948 (d04)

**Agent memory and retrieval triggers**
- [V] Zhao et al. (2024), ExpeL. https://arxiv.org/abs/2308.10144 (c22, d12)
- [V] Yang et al. (2024), Buffer of Thoughts. https://arxiv.org/abs/2406.04271 (c24, d24)
- [V] Wang, Mao, Fried and Neubig (2024), Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (d10)
- [V] Ouyang et al. (2025), ReasoningBank. https://arxiv.org/abs/2509.25140 (d11)
- [V] Suzgun et al. (2025), Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (d09)
- [V] Liu et al. (2026), HippoSpark. https://arxiv.org/abs/2606.29929 (b27, d13, d14)
- [V] Xiao et al. (2026), RA-RFT. https://arxiv.org/abs/2606.13680 (b28, d15)
- [V] Li et al. (2024), RAG or long-context LLMs (Self-Route). https://arxiv.org/abs/2407.16833 (d08)
- [V] Jiang et al. (2023), FLARE. https://arxiv.org/abs/2305.06983 (d16)
- [V] Mallen et al. (2023), When not to trust language models. https://arxiv.org/abs/2212.10511 (d17)
- [V] Asai et al. (2023), Self-RAG. https://arxiv.org/abs/2310.11511 (d18)
- [V] Liu et al. (2024), Lost in the middle. https://arxiv.org/abs/2307.03172 (d19)
- [V] Jin, Yoon, Han and Arik (2024), Long-context LLMs meet RAG. https://arxiv.org/abs/2410.05983 (d20)
- [V] Dhuliawala et al. (2023), Chain-of-Verification. https://arxiv.org/abs/2309.11495 (d21)

**Caveats on source quality.** The Yasunaga table rows were settled by d01 (0-shot, 0-shot CoT, 5-shot CoT, Ours); 5-shot CoT there is fixed exemplars, not retrieval. The Self-Route text quotes 46.83 vs 47.04 for GPT-4O but the table average reads 48.89 vs 48.67; sub-point gaps are approximate. The Self-RAG full-model row was not recovered. All 2026 arXiv items are single preprints.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 10 established claims: 4 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C10.05-K01** (now single-source: the sources are not independent). Numbers (.56/.53/.12/.09, 32 stories, 20 probes, one-week delay) match the MAC/FAC paper, but all four listed entries are versions of one paper by one lab reporting one study (Gentner/Rattermann/Forbus 1993 data); Gentner and Markman 1997 is same-lab review with no new data.
- **C10.05-K08** (reworded: the sources support less). The 30% vs 80-90% figures are the MAC/FAC authors' summary of Gick and Holyoak; the 2025 paper's own citation of Gick and Holyoak 1983 Exp 2 gives 29% (8/28) unhinted vs only 50% (14/28) hinted, so 80-90% is not the classic hinted rate across studies. Corrected claim: Hints turn analogy use on: Gick and Holyoak's classic radiation-problem studies are summarized as about 30% unhinted vs 80-90% hinted (Forbus, Gentner & Law 1995), though 1983 Exp 2 is cited as 29% vs 50%; a 2025 business replication (n=199) found lower rates (factory 6.3% unhinted vs 8.7% hinted; HR 20.3% vs 37%).
- **C10.05-K13** (reworded: the sources support less). Numbers are right (0.81 vs 0.26; 20.2 calls and $0.071; +12.2 'up to'; 17.4 vs 17.0), but 'recovers most of the lost structure' holds only for the 151-candidate CPR-eval shortlist; on BRIGHT the GPT-4 rerank adds just +3.1 over BM25 (14.3 to 17.4) and BRIGHT scores stay low. Corrected claim: An LLM reranker over a 151-candidate shortlist lifts CPR-eval Recall@10 from 0.26 (best retriever) to 0.81 (20.2 calls and $0.071 per query), and LLM-written reasoning queries add up to +12.2 nDCG@10 on BRIGHT, but on BRIGHT GPT-4 reranking of the top-10 adds only +3.1 over BM25 (14.3 to 17.4) with no gain from widening to the top-100 (17.0).
- **C10.05-K15** (reworded: the sources support less). EPR gains over the best baseline are +5.9 (BREAK), +7.2 (MTOP) and +2.9 EM (SMCalFlow), not a uniform +6 to +7; the RA-RFT 47.4 vs GRPO 43.3 comparison is against GRPO without retrieval (similarity-retrieval GRPO scored 37.7), so it does not show usefulness-aimed retrieval beating pure similarity. Corrected claim: Retrievers or selectors aimed at usefulness or structure coverage beat similarity or heuristic retrieval for in-context examples: EPR gains +2.9 to +7.2 EM over the best baseline (BM25 or CBR) on BREAK, MTOP and SMCalFlow, and structure-coverage selection gains up to +23 points (SMCalFlow-CS 50.3 to 73.5); RA-RFT (47.4) beats GRPO without retrieval (43.3) on Qwen3-1.7B, where naive similarity retrieval hurt GRPO (37.7).
- **C10.05-K23** (now single-source: the sources are not independent). Sultan and Shahaf 2023 (100 random ProPara paragraph pairs, 3% analogies; SBERT top-100 100% mostly self-analogies, FMQ 79%, FMV 72%) is the only data source; StoryAnalogy merely cites it, and the sample is one crowdsourced science-process dataset, not 'ordinary text'.
- **C10.05-K30** (reworded: the sources support less). Mallen et al. say adaptive-retrieval gains are much smaller for models under 10B (not that it rarely helps); FLARE says performance plateaus above 60% on 2WikiMultihopQA and only drops above 50% on StrategyQA. Corrected claim: Gate retrieval instead of always retrieving: FLARE finds triggering retrieval for 40-80 percent of sentences usually performs well, with a plateau above 60 percent on 2WikiMultihopQA and a drop above 50 percent on StrategyQA; PopQA adaptive retrieval retrieves for about 40 percent of questions with davinci-003, and its gain is much smaller for models under 10B (which almost always retrieve); Self-RAG reports a large drop on PopQA and ASQA when it always retrieves the top passage (41.8 PopQA in that ablation; full-model row not recovered); HippoSpark gains turn unstable after more than five retrievals and 10.67 percent of instances needed none. The threshold shifts with model strength.
- **C10.05-K02** (now single-source: only one opened source, code check).
- **C10.05-K11** (now single-source: only one opened source, code check).
- **C10.05-K19** (now single-source: only one opened source, code check).
