# Analogical problem solving: deep document

*Subfield A02.08. Source files in this folder: evidence_a-d.jsonl, claims.jsonl (K01-K27), critique.md. Evidence ids (a01, b15, d04 ...) point to lines in the evidence files. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Cross-check done 2026-11-03: ten key numbers were re-opened as full text and confirmed, one needed correction (Yasunaga table, see section 3). The 1980s human numbers were read by earlier agents and agree across files a and b, but were not re-opened in the check.*

## 1. What it is

Analogical problem solving means using a solved problem (the source or base) to solve a new problem (the target). The solver must do four things:

1. **Represent** source and target.
2. **Retrieve** a source from memory or from the context. This is the "noticing" step.
3. **Map** parts of the source onto parts of the target (who plays which role, which relation matches which).
4. **Extend** the mapping into a solution for the target, and often **induce a schema** (a general rule shared by both cases).

Holyoak and Koh (1987) name the same four steps: represent, select source, map components, extend the mapping (a12).

The central idea of structure-mapping (Gentner): a good analogy matches **relations**, not objects. A mapping is better when it is **systematic**, meaning it links whole systems of connected relations, especially higher-order ones such as causes. Surface features (what the objects look like or are called) should count for little.

The founding paradigm is Gick and Holyoak (1980, 1983). People read a military story (a general splits his army and converges on a fortress), then solve Duncker's radiation problem (destroy a tumour with rays without harming healthy tissue). The convergence solution is the analogue of the army story.

The key empirical lesson: **people can apply an analogue easily once they see it, but rarely notice it by themselves.** Retrieval, not mapping, is the bottleneck. A second lesson: retrieval runs on surface similarity, while good use needs structural similarity. These two pull apart, so people retrieve look-alikes and miss true analogies.

For our agent this is operator **O7 "map an analogue"**: find a distant problem with the same structure, build a typed mapping, check it with code. The schema marks O7 as [E] for "unaided analogy rarely transfers", [S] for the mapping step, and says far analogues belong at impasses and in open mode only.

Scope: the founding human studies with numbers, the computational models (SME, MAC/FAC, ACME, ARCS), replications and failed replications, boundary conditions, and every LLM or AI study we found that tests or uses the idea (2020-2026). Parallel subfields (links only, not covered here): Incremental mapping; Connectionist and hybrid mapping models; Logic and philosophy of analogical arguments; Relational reasoning gap; Conceptual blending; Dynamic memory and early CBR; Failure-driven CBR; Worked examples; Self-explanation; Chain-of-thought prompting; Fluid reasoning (Gf); Language as a tool for relations.

## 2. History and theories in depth

### 2.1 Before 1980
Duncker (1945) posed the radiation problem and the idea that solutions come from restructuring. Gestalt work on fixation (a parallel subfield) shows people are stuck on the first representation. Analogy was treated as a curiosity of insight until the 1980s.

### 2.2 Gick and Holyoak 1980 and 1983: the founding experiments
- **1980 (not opened, [M]).** Subjects read the military story, then solved the radiation problem. Standard figures quoted in later papers: about 10% solve it with no analogue, about 30% with an analogue and no hint, about 75% with a hint to use the story (b01, b23). Secondary sources report 76% to 92% for the hinted figure. Use 75% as the central value, with that range.
- **1983 (opened).** Six experiments on schema induction (a01-a08). Numbers in section 3. Main claim: transfer comes from a **schema** formed when the solver compares two analogues and writes what they share. One analogue gives a poor schema and weak spontaneous transfer.
- The "noticing gap": about 30% unhinted against about 75% hinted. With a 10% base rate, only about 31% of potential appliers noticed the analogue on their own (a02). This estimate depends on the assumed base rate.

### 2.3 Holyoak and Koh 1987: what drives retrieval
They varied surface similarity (laser vs ultrasound source) and structural similarity (fragile glass vs insufficient intensity constraint) in a 2x2 design (a10). Both factors help unprompted retrieval about equally and additively. After a hint, only structure still matters (a11). They proposed a retrieval mechanism of summed activation from shared features, causal and surface (a12). They also showed a source read days earlier and discussed in class transfers at 81% to 86% (a09), so the noticing failure is not a pure lab artifact. Context and similarity decide.

### 2.4 Catrambone and Holyoak 1989: what rescues transfer
Comparing two analogues rescued pre-hint transfer under minimal delay (a13). After a context shift or a one-week delay with dissimilar analogues, transfer collapsed back to baseline, but hints still worked (a14). Three changes together recovered it: directive comparison, rewording the target to stress the shared structure, and three analogues (a15). This is the main source for "memory holds, cueing fails".

### 2.5 Gentner's line: structure-mapping, SME, systematicity
- **Structure-mapping theory (Gentner 1983).** Analogy is an alignment of relational structure. Attributes are dropped, relations kept, and systems of relations (joined by higher-order relations) are preferred. Only Gentner and Toupin (1986) and MAC/FAC were opened in this series. Gentner 1983, Clement and Gentner 1991 and Markman and Gentner 1993 were not (gap 10 in critique.md).
- **Gentner and Toupin (1986) (a31, a32).** Children aged 4-6 and 8-10 (N=72) acted out a target story from a source story. A systematic source (a causal chain) helped only from about age 8, mostly on the hardest cross-mapped condition (same objects, different roles). Systematicity acts at mapping, not at memory.
- **MAC/FAC (Gentner and Forbus 1991) (a22, a23).** A two-stage retrieval model. MAC is a cheap content-vector dot product over the whole memory. FAC runs a structural match on the survivors. It reproduces the Karla-the-hawk finding that people retrieve surface matches much more than true analogies.

### 2.6 Holyoak and Thagard: constraint satisfaction (ACME, ARCS)
- **ACME (1989) (a16-a18).** A localist network, one unit per possible pairing. Three soft constraints: structural consistency (isomorphism), semantic similarity, pragmatic centrality (goals). Activation settles into a mapping. Unlike SME, isomorphism is soft and it can map across different predicates when meaning supports it.
- **ARCS (Thagard et al. 1990) (a19-a21).** Retrieval as the same kind of network, with semantic similarity (WordNet-style), structure and goals. Tested on 5 radiation problems, 5 Karla stories, 100 fables and 25 play synopses. Networks typically settled in under 150 cycles; the largest Karla simulation had 570 units and 26,330 links.
- **Where the camps differ.** SME wants strict structural consistency and systematicity. ACME mixes structure, meaning and purpose. Both agree retrieval is cheap and surface-driven, and mapping is more structural.

### 2.7 Later human work
- **Bearman, Ormerod and Ball (2002) (b05, b06, b26).** Told to evaluate the source stories, people transferred less than when told to summarise. Pre-hint rates with an analogue and two distractors were tiny (8%, then 1.3%), far below the original 30%.
- **Beveridge and Parkins (1987) (b07).** The Gick-Holyoak null result for diagrams was a boundary condition. Diagrams help if they depict the right problem-solving structure.
- **Alfieri, Nokes-Malach and Schunn (2013) (b08, b09).** Meta-analysis of case comparison in learning.
- **Developmental work (a31, b16).** Systematic structure helps from about age 8; transfer of letter-string rules is already adult-like at 7-9.

### 2.8 Computational and AI line
Copycat (Hofstadter and Mitchell) is the older non-LLM letter-string analogy system (slipnet and coderack; only a snippet was seen, c26). SME, MAC/FAC, ACME and ARCS are the cognitive models. From 2020 language models were tested as analogy-makers (section 6), and analogy-like prompting and memory (analogical prompting, Thought Propagation, ExpeL, Buffer of Thoughts, step-back) entered agent design.

## 3. Core findings with exact numbers

Status uses the claim labels. N and condition are in the numbers column.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Baseline: radiation problem with no analogue, with analogue unhinted, with hint | about 10% / about 30% / about 75% (range 76-92% hinted in secondary sources) | Gick and Holyoak 1980/1983 via a01, b01, b23 (1980 not opened) | established |
| Only about a third of potential appliers notice the analogue | (30-10)/(75-10), about 31%; depends on assumed 10% base | a02 | established (estimate) |
| Cord problem: analogue story vs control | pre-hint 71% vs 20%; total 98% vs 30%; N=69 (25/24/20); recall vs summary instructions no difference | Gick and Holyoak 1983 Exp 1 (a03) | single experiment |
| Stating the principle alone does not help one-analogue transfer | pre-hint: analogue+principle 32% (10/31), analogue only 29% (8/28), principle only 28% (8/29); total 80/79/66%; N=88; G2(2)=2.05, p=.36 | Exp 2 (a04) | established (K05) |
| One diagram with one story does not help noticing | combined analogue conditions 31% pre-hint; diagram-only 1/15 (7%) pre-hint, 67% total; N=66 | Exp 3 (a05) | established |
| Two analogues + write the similarities beat one analogue | pre-hint 45% vs 21%; total 80% vs 53%, G2(1)=8.36, p<.003; N=98 | Exp 4 (a06) | established (K04) |
| Schema quality predicts transfer | good schema 91% (10/11) solved pre-hint, 100% total; poor schema 30% pre-hint, 70% total | Exp 4 (a06) | correlational |
| Principle + two analogues helps | with principle 62% pre-hint, 82% total; without 40% / 67%; G2(1)=6.75, p<.01; N=143 | Exp 5 (a07) | established |
| Diagrams after two analogues help | diagram 57% vs 37% pre-hint, 92% vs 79% total; N=189; best condition 68% pre-hint, 95% total (N=37) | Exp 6 (a08) | established |
| Visual analogue that depicts the right structure helps | Exp 1: control 0%, Red Adair story 14%, strips analogue 32%; Exp 2: strips 95% vs Red Adair 75% | Beveridge and Parkins 1987 (b07) | single-source |
| Recently activated textbook source transfers spontaneously | analogy group N=21: 81% (lightbulb), 86% (radiation); controls N=10: 10%; G2(1)=15.2 | Holyoak and Koh Exp 1 (a09, b02) | established |
| Surface and structure both drive unprompted retrieval | pre-hint: laser+fragile 69%, ultrasound+fragile 38%, laser+insufficient 33%, ultrasound+insufficient 13%; fragile 54 vs insufficient 23 | Holyoak and Koh Exp 2 (a10, b03) | established (K02) |
| After a hint, only structure matters | total: fragile 78% vs insufficient 54% (G2(1)=4.31, p<.05); laser 68% vs ultrasound 64% (ns) | a11 | established |
| Long-term retrieval prefers look-alikes (Karla) | after 2 weeks, 32-story memory: literal .56, surface .53, analogy .12, first-order-only .09; people still rate analogies more sound | Gentner and Forbus 1991 (a22) | established (K03) |
| Same order in ARCS-modelled data | literal 58%, mere appearance 45%, true analogy 18%, false analogy 8% (read from a graph) | Thagard et al. 1990 (a21) | model fit; graph-read |
| Pre-hint transfer rescued by comparing two analogues | two analogues 47% pre-hint, 68% total (n=19) vs one analogue 16% / 53% (n=19); combined total 71% vs 41%, G2(1)=7.16 | Catrambone and Holyoak Exp 1 (a13) | established |
| Delay and context shift kill spontaneous transfer | Exp 2: no condition above the 10% baseline; total 65% (30 min) vs 42% (1 week); pre-hint at 1 week 7% (Exp 2), 23% (Exp 3) | a14 | single-source (K06) |
| Rewording the target + three analogues restores it | Exp 4: directive 36% vs 10% pre-hint; intensity wording 32% vs dosage 14%; Exp 5 (1 week): 74% overall | a15 | single-source, confounded |
| Telling people to evaluate sources lowers transfer | post-hint success evaluative 28% / 22% vs summary 61% / 50%; n=18 per cell; Wald=6.7, p=.009; 27 of 72 forgot a source: non-analogous once, surface-similar 16, conceptually similar 14 | Bearman et al. 2002 (b05, b06) | single-source (K07) |
| Pre-hint rate in a conceptual replication is far below 30% | 6/72 (8%) Exp 1; 1 person (1.3%) Exp 2 | b26 | contradicts original |
| Case comparison beats other instruction | d=.60 (95% CI .47-.72), 57 experiments, 336 tests, Q(56)=136.74, I2=59% (conference version); published article about d=.50; vs sequential d=.37; adults d=.53, adolescents d=.34 (CI -.01 to .68, k=4); similarities-only prompts best | Alfieri et al. 2013 (b08, b09) | single meta-analysis (K08) |
| Systematic causal structure helps mapping from about age 8 | N=72; age F(1,68)=14.93; systematicity F(1,68)=6.28; interaction F(2,136)=3.89, p<.05 | Gentner and Toupin 1986 (a31) | single-source (K10) |
| Letter-string analogy: LLMs fail on counterfactual alphabets | humans .753 (CI .734-.773) vs GPT-3 .488, GPT-3.5 .350, GPT-4 .452 | Lewis and Mitchell 2024 (b13) | established (K14) |
| Same, with children | Latin/Greek/symbol: adults .88/.91/.89 (n=62); children .62/.66/.67 (n=41); GPT-4o .85/.63/.48; Claude-3.5 .68/.62/.46; Gemma-2 27B .60/.39/.14; Llama-3.1 405B .79/.74/.27 | Stevenson et al. (arXiv 2411.02348; J. Memory and Language 145, 2025) (b16) | established |
| Shuffled alphabet: code execution closes the gap | GPT-4 vs humans P=8.9e-13; GPT-4 + code vs humans P=0.496; human N=99 (interval 1), 97 (interval 2) | Webb et al. 2024 reply (d04) | contested (K15) |
| GPT-4 story analogy is order-biased | original data: 89% (16/18) correct-first, 61% (11/18) correct-second, total 75% (27/36); their rerun 1.0 / 0.72, 0.86 (31/36); humans 0.78 (564/720) | Lewis and Mitchell 2025 (b15) | established (K16) |
| Paraphrasing the correct target hurts GPT-4 more | GPT-4 0.86 to 0.72; humans 0.78 to 0.70; 18 items, too few for significance | b15 | established |
| Digit matrices: moved blank breaks models | digits .715 humans / .813 GPT-3.5 / .810 GPT-4; alternate blank .771 / .480 / .477; symbols .704 / .790 / .792 | b14 | established |
| Models do not retrieve the right source unaided | GPT-4 0/15 correct source unhinted; hinted recall 1.00, precision about .50; humans (n=199) radiation recall 6.25% (3/48), precision .42; dolphin precision 1.0, recall about 22%; factory problem: GPT-4 used an analogy 1/15 unhinted vs 15/15 hinted | Puranam et al. 2025 (a28, c11) | established (K12) |
| Far analogies lose to near distractors | ARN, 1,096 triples, GPT-4: near vs far distractor 94.0, near/near 92.5, far/far 57.1, far analogy vs near distractor 29.1, mean 68.1; GPT-3.5 mean 60.3 (21.7 on far-vs-near); humans mean 96.0 (91.4 on far-vs-near) | Sourati et al. 2024 (c07) | established (K13) |
| Story-level analogy | text-davinci-003 37.1% (random 25%); humans 85.7% | StoryAnalogy (c08) | established |
| Long stories hurt | AnaloBench 1/10/30 sentences: GPT-4 89.1/66.5/60.7; GPT-3.5 65.3/46.4/30.8; Claude 68.2/30.2/25.9; humans 96.0/72.5/73.3; retrieval from a 200-story bank near chance | Ye et al. 2024 (c09) | established |
| Self-generated analogues (analogical prompting), GSM8K | text-davinci-003 0-shot 14.8, 0-shot CoT 50.3, 5-shot CoT 54.0, self-generated 61.0; GPT-3.5-turbo 75.0/75.8/76.7/77.8; PaLM2 60.8/78.2/80.7/81.7; MATH GPT-3.5 33.0/33.9/34.9/37.3. Average gain about +4 | Yasunaga et al. 2024 (b19, c12) | established (K17); gains small (K18) |
| Scale boundary | GSM8K 0-shot CoT / 5-shot retrieved / self-generated: curie-001 2/3/2; davinci-001 6/11/9; davinci-002 22/47/48; davinci-003 50/57/61. CORRECTION: the paper's Table 4 gives fixed 5-shot as 43 and 50 for d-002/d-003, which conflicts with Table 3's 54.0; the paper is internally inconsistent. Safe claim: self-generated 61.0 vs best fixed or retrieved 54-57 | b20, critique item 3 | established |
| Analogous-problem propagation | shortest path optimal: GPT-3.5 IO .33, CoT .26, TP .65; PaLM-2 .14/.24/.36; GPT-4 .78/.76/.88; 100 items; one layer gives most of the gain | Yu et al. 2024 (c14, d11, d12) | single-source (K27) |
| Experience-retrieval agents | ExpeL ALFWorld retrieve-only 40.3 to 54.4 over rounds R0-R3; insights-only vs retrieve-only HotpotQA 36 vs 31, ALFWorld 50 vs 55, WebShop 37 vs 38; Buffer of Thoughts Game of 24 82.4 vs ToT 74.0, Checkmate-in-One 86.4 vs 57.2 | c15, c16 | single-source each (K19) |
| Abstraction first (step-back) | PaLM-2L MMLU Physics +7, Chemistry +11, TimeQA +27, MuSiQue +7 | Zheng et al. 2024 (c17) | single-source (K20) |
| Reasoning models collapse under noise | o3-mini 86.6% to 17.0%; R1 80.6% to 23.2% (chance 12.5%); 3.4x more reasoning tokens; o3-mini tokens 7,209 to 18,589; high effort (2.7x) +6% on I-RAVEN, 0 on I-RAVEN-X; neuro-symbolic ARLC 98.6% to 88.0% | Camposampiero et al. 2025 (d01-d03) | single-source (K25) |
| Task demands matter | model-size by evaluation-method interaction z=2.631, p=.009 | Hu and Frank 2024 (d14) | supported (K26) |
| Abstract rule transfer far below humans | ConceptARC 480 tasks: humans 91%, GPT-4 25% (0.33 with a detailed one-shot prompt), best Kaggle program 52% | Mitchell et al. 2023 (c20) | single-source (K23) |

## 4. Mechanisms and models

This section is written so an engineer can build each part.

### 4.1 The four-step pipeline (Holyoak and Koh)
```
represent(source), represent(target)       # propositions: relation(arg1, arg2), plus goals
candidates = retrieve(target, memory)      # step 2: the weak step
for s in candidates:
    mapping = map(s, target)               # step 3: one-to-one role assignment
    ok = check(mapping)                    # structural consistency + goal coverage
solution = extend(mapping)                 # step 4: carry source solution over, then test it
schema = induce(s1, s2)                    # optional: write what two cases share
```

### 4.2 Retrieval: MAC/FAC (two-stage filter)
- **Representation.** Each memory item gets a **content vector**: a count of how often each predicate or entity type occurs in its relational description.
- **MAC stage.** Dot product of the target vector with every memory vector. Keep the best and anything within a margin. In Gentner and Forbus's simulation MAC returned about 3.3 items on average from 36 stories (a23). Cost is linear in memory size and cheap.
- **FAC stage.** Run a structure-mapping match on each MAC survivor. Accept the best, plus others within a margin. FAC accepted about 1.5 items on average (a23).
- **Why it matters.** MAC is surface-driven, so it surfaces look-alikes. FAC rescues true analogues only if MAC passes them. In Simulation 1, correct retrieval was literal 1.0, surface .89, analogy .67 (MAC) and .56 (FAC). Analogies are the hardest. Design note: the first stage must be generous (keep several) and the second stage must be structural.

### 4.3 Retrieval: ARCS (constraint network)
- One unit per plausible pairing between target propositions and each memory item. Excitatory links between consistent units; inhibitory links between competing units (same element mapped twice).
- Constraint weights: semantic similarity (concept hierarchy), structure, pragmatic importance (goal elements get extra weight).
- Settles in under 150 cycles in most runs. Output: the memory item with the most active pairing units. It reproduced the human order literal > surface > analogy > false analogy (a21).
- Engineer's reading: a weighted sum of semantic, structural and goal cues predicts retrieval and mapping (K09). A target constraint with no counterpart in the source predicts failed transfer (ACME found the "do not destroy healthy tissue" proposition had no map in the poor versions, a17).

### 4.4 Mapping: SME style (strict) vs ACME style (soft)
- **SME-like.** Generate local matches between identical predicates, merge them into structurally consistent clusters (one-to-one, parallel connectivity), score clusters with a systematicity bonus (a relation scores higher if it sits inside a deeper connected system). Pick the best global cluster. Then make **candidate inferences** from unmapped source structure that connects to the mapped part.
- **ACME-like.** One unit per candidate pairing; links as in 4.3; run to convergence. Allows mapping different predicates when meaning supports it.
- **Checks to implement in code (our O7).** (1) One-to-one: no source role maps to two target roles and the reverse. (2) Goal coverage: every target constraint has a counterpart or is flagged as uncovered. (3) Higher-order consistency: if a cause maps, its argument relations must map consistently. (4) Cross-mapping test: swapping objects but keeping roles should not change the answer. The Gentner and Toupin result suggests this matters most when the same objects play different roles (a31). Items 2 to 4 are our design from the models, not tested on LLMs.

### 4.5 Schema induction
Two analogues + the task "write how they are similar" produces an abstract schema (a06, a13). Schema quality predicts transfer (91% vs 30% pre-hint). Implementation: give the model two solved cases, ask for a short rule in neutral vocabulary (no surface nouns), then retrieve by that rule. Rewriting the target in the schema's vocabulary was one of three levers that restored transfer after delay (a15).

### 4.6 Analogical prompting and memory loops for LLMs
- **Analogical prompting.** One call: "recall 3 to 5 relevant, distinct problems with solutions, then solve this one". K=3 to 5 is best; K=1 is worse (c12). Failure: recalled examples were easier than the target (b21).
- **Thought Propagation.** Build several analogous sub-problems (neighbours or rephrasings), solve each, aggregate or refine the first answer. One layer gives most of the gain (d12).
- **Buffer of Thoughts / ExpeL.** Store distilled templates or insights, retrieve the nearest by task description, instantiate. Retrieval is by description similarity, so it is **near** analogy only (c15 limits).
- **Step-back.** Ask for the principle first, then solve (c17). The relational core of structure-mapping without a second case.

### 4.7 Computational view of the human bottleneck
Retrieval is cheap and content-based (MAC). Mapping is costly and structural (FAC, SME). The human weakness is that the cheap stage decides what the costly stage sees. LLMs show the same pattern in stronger form (section 6): without a cue they do not retrieve the structural match at all.

## 5. What holds up

### 5.1 Replicated and robust
- **The noticing gap.** Replicated in conceptual form several times (Holyoak and Koh; Catrambone and Holyoak; Bearman et al.). A hint produces a large jump (about 30% to about 75%). The exact pre-hint level varies from 1.3% to 47% (see 5.2).
- **Surface and structure both drive retrieval; only structure survives a hint.** Holyoak and Koh Exp 2, ARCS fit, Karla data (K02, K03).
- **Two analogues + comparison beat one.** Within Gick and Holyoak (Exp 4: 45% vs 21%), Catrambone and Holyoak (47% vs 16%), and the Alfieri meta-analysis (d about .50-.60) (K04, K08).
- **Models of retrieval agree.** MAC/FAC, ARCS and Holyoak-Koh summation are all "cheap broad filter, then structure" (K09).
- **LLMs: no unaided retrieval, easy application once cued** (K11, K12).
- **LLMs: surface bias in far analogy.** ARN, StoryAnalogy, AnaloBench agree (K13).
- **LLMs: letter-string analogy does not survive counterfactual alphabets.** Four independent human-vs-LLM comparisons (K14).

### 5.2 Failed replications and weakened claims
- **Webb et al. 2023 "emergent analogical reasoning" is weakened.** GPT-4 story analogy is biased by answer order (0.89 vs 0.61) and drops on paraphrase (0.86 to 0.72) (b15). The letter-string headline reversed in a partial replication: GPT models did worse than humans, and the replication humans did better than Webb's undergraduates (b22). Webb's reply (d04) and Hu and Frank (d14) narrow the claim: part of the gap is counting and answer format.
- **The Gick-Holyoak pre-hint level (30%) did not replicate in Bearman et al.:** 8% and 1.3% with an analogue plus distractors (b26). Explanations offered, not tested: distractor load and instructions.
- **Human spontaneous transfer is both large and tiny.** 81-86% (Holyoak and Koh Exp 1, source read days earlier and discussed in class) vs 7-23% (Catrambone and Holyoak, one-week delay, dissimilar analogues). The reconciling variable is surface similarity and context, as Holyoak and Koh Exp 2 predicts.
- **Diagrams.** Null in Gick and Holyoak Exp 3 (diagram plus one story), positive in Exp 6 (diagrams after two analogues: 57% vs 37%) and in Beveridge and Parkins (right-structure visuals).
- **Evaluate vs summarise (Bearman).** Goes against the schema-induction view that active comparison helps. Likely reconciliation: criticising one source blocks encoding of its key idea. One study only.
- **Alfieri effect size.** d=.60 in the conference version, about .50 in the published article. Cite both.

### 5.3 Moderators
- **Delay and context.** Spontaneous transfer falls to baseline after one week with dissimilar analogues; hints still work (a14).
- **Surface match with the target.** Raises unprompted retrieval; irrelevant after a hint (a11).
- **Number of analogues.** Two beat one; three plus reworded target restored transfer (a15).
- **Principle statement.** Useless with one analogue (a04), helpful with two (a07).
- **Instruction.** "Find only similarities" is best in the meta-analysis (b09). "Evaluate" lowers transfer (b05).
- **Age.** Systematic structure helps mapping only from about age 8 (a31).
- **Source length (LLMs).** AnaloBench accuracy falls from 1 to 30 sentences (c09).
- **Model scale (LLMs).** Self-generated analogues help only at text-davinci-002/003 scale and above (b20). Small models write invalid exemplars. The production vs forced-choice gap shrinks with model size (d14).
- **Answer order (LLMs).** Large effects in GPT-4 (b15); Permuted Pairs coefficients -1.68 to -2.34 (d09). Humans unaffected.

### 5.4 Interventions that worked
- Hint that an analogue exists (humans and LLMs).
- Two analogues + write the similarities (humans, K04).
- Principle + two analogues; diagrams after two analogues (K05).
- Reword the target in schema vocabulary (single-source).
- Chain-of-thought with a "state the proverbial message first" step: GPT models gained up to 30 absolute points on far analogies in ARN (c07). Plain few-shot demos hurt near analogies.
- Self-generated analogues with strong models (+1 to +4 points).
- Code execution for letter-string counting (GPT-4 reaches human level on the shuffled alphabet, d04).
- One-shot radiation prompt for design analogies: useful 80% vs 40% zero-shot (c19; small, human-rated).

### 5.5 Interventions that did not work
- Principle alone, or one diagram alone, with one analogue (a04, a05).
- Evaluating rather than summarising sources (b05).
- Recall vs summary instructions (a03: no difference).
- More reasoning tokens on noisy analogy (d01-d03).
- Self-generation at small model scale (b20).
- Listing sub-concepts before searching an open set: +0.4 to +1.6 points only (a30).
- Plain few-shot demos on near analogies (c07).

## 6. Language models

### 6.1 Timeline
- **2022 to 2023: first positive claims.** Webb, Holyoak and Lu (2023) report GPT-3 (text-davinci-003) matching or beating UCLA undergraduates on digit matrices (humans N=40; generative OR=1.88, p=.005; multiple choice OR=6.27), letter strings (N=57; OR=1.76; error correlation with humans r(39)=.7) and verbal analogies (N=57) (c01). On story analogies (Gentner materials, humans N=54) GPT-3 preferred the causally matching story in near analogies (p=.0039) but not significantly in far ones (p=.065); humans beat GPT-3, OR=0.37, p=.0003 (a26). In the radiation paradigm GPT-3 gave a non-convergent answer alone, found convergence after the army story, lost it when two distractor stories were added, and recovered when told to consider the earlier stories (a24, a25). These are single transcripts without counts. On the children's gumball/genie task it named the correspondences but produced mechanically nonsensical solutions (a27).
- **2023 to 2025: robustness checks.** Hodel and West: shuffled alphabet, 121 students, GPT-3 under 0.1 (c03, d06). Lewis and Mitchell: counterfactual alphabets, digit matrices, stories (b13-b15). Stevenson et al.: children and adults vs four LLMs (b16). Musker et al.: re-representation tasks (b17, d08-d10). Hu and Frank: task demands (d14).
- **2025: reasoning models.** o3-mini and R1 collapse on noisy matrix analogy (d01-d03).

### 6.2 Retrieval (the Gick-Holyoak bottleneck) in LLMs
GPT-4 on a matching task with two sources and two targets (Puranam et al. 2025, n=60 runs vs humans n=199): without a hint it picks no analogy at all (precision 0, recall 0, accuracy .50). With a hint it uses every analogy (recall 1.00) but half are wrong (precision .50 to .52, F1 .67 to .68). Errors came from surface similarity. Humans have the opposite profile: high precision, low recall (radiation precision .42, recall .06; dolphin precision 1.0, recall .22). The authors note a demand effect: the hint makes the LLM over-claim. Human solve rates here were lower than in 1983 (6.3% and 20.3% unhinted vs 29% in Gick and Holyoak Exp 2), partly because of the matching load. So GPT-4 shows a stronger form of the human failure, and the hint creates a new failure (over-application).

AnaloBench retrieval from a 200-story bank is near chance (c09). StoryAnalogy: text-davinci-003 37.1% vs random 25% and humans 85.7% (c08).

### 6.3 Mapping and surface bias
ARN far-analogy vs near-distractor: GPT-4 29.1%, GPT-3.5 21.7%, humans 91.4% (c07). In a two-way choice these are below chance level, so the model prefers the surface-similar distractor. A "state the message first" CoT recovered up to 30 points on far analogies (c07).

### 6.4 Letter strings and counterfactuals
Numbers are in section 3. Reading across the dispute (K15):
- Lewis and Mitchell, Hodel and West: the drop shows weak abstraction and reliance on training data. Webb's team admitted in peer review that some items could be online (d07).
- Webb et al. 2024: GPT-4 with code execution matches humans on the shuffled alphabet (P=0.496); 46% of GPT-4 errors used a valid alternative rule vs 39% for humans (d05).
- Opiełka et al. (c21), inside Llama-3.1 70B: no stable concept vector for abstract "previous/next"; 98% on known lists vs 62% abstract. Letter-string accuracy 0.35 with no permutation, 0.10 (2 letters permuted), 0.05 (5), 0.00 (10 and 20), 0.15 with symbols (chance 0.04 letters, 0.1 symbols).
- Musker et al.: best LLMs (GPT-4, Claude 3, Llama-405B) do not differ significantly from humans in default re-representation tasks (p=.097, .194, .097); weak models fail (Pythia-12B 0.0, Falcon-40B 0.1, GPT-3 0.5, Claude 2 0.6). All LLMs are order-sensitive where humans are not. Models keep trusting an uninformative source (d10).
- Hu and Frank: format matters.
- Net: the failure is partly counting and indexing, partly format, and partly real abstraction weakness. Undecided; the rule-in-words test was never run.

### 6.5 Reasoning models
o3-mini 86.6% to 17.0% and DeepSeek-R1 80.6% to 23.2% when perceptual noise is added (chance 12.5%); reasoning cost 3.4x; more effort gave nothing on the hardest setting. The authors attribute only 5.6% of o3-mini's drop to length and range and most of the rest to uncertainty (d03). Reasoning models cope with longer rules far better than plain LLMs. No reasoning model has been tested on unaided retrieval of a deep analogue (open gap 4). This fits schema guardrail G11 (extra thinking does not buy accuracy).

### 6.6 Analogy-style prompting and agents
- Analogical prompting: +4 points on average. GSM8K: GPT-3.5-turbo 75.8 to 77.8, PaLM2 78.2 to 81.7, text-davinci-003 50.3 to 61.0 (against best fixed exemplars 54.0, see correction). Codeforces: 15% with self-generated knowledge and exemplars (GPT-3.5-turbo) vs 16% for the GPT-4 baseline.
- Thought Propagation: GPT-3.5 .33 to .65, PaLM-2 .14 to .36, GPT-4 .78 to .88. 100 shortest-path items. The "analogous problems" are neighbour sub-problems; ToT fails in some settings, which flatters TP. Creative writing coherence GPT-4 7.989 vs ToT 7.684 and CoT 6.927, human preference 45% vs 33% and 15%. ALFWorld 134 environments: 82-95% vs Reflexion 79.1 (some baselines quoted from other papers). Tokens not matched.
- ExpeL and Buffer of Thoughts: numbers in section 3. Retrieval by description similarity. Transfer HotpotQA to FEVER: ReAct 58%, ExpeL variants 63 to 70% (c15).
- Step-back: gains in section 3.
- Design analogies: GPT-3 one-shot with the Duncker example 80% useful vs 40% zero-shot, 480 analogies (c19). InstructGPT analogy generation, share rated meaningful: 1.90 / 15.61 / 48.29 / 70.05% for 0.3B / 1.3B / 6.7B / 175B (c18).
- ConceptARC: GPT-4 25% to 33% vs humans 91% (c20).
- Teaching pipeline (Barakat and Kochmar, 2026, arXiv 2605.24211): closed-set Hit@1 gold sub-concepts 24.5%, background 22.2%, gold+background 20.8%, embedding only 19.5%, generated sub-concepts 18.2%, names only 17.5%; open-set gains 0.4 to 1.6 points (a30).
- AnalogyKB: lifts RoBERTa-large from 59.92 to 77.44 on analogy recognition (58.08 with unchecked data); the checking step is the point (c22).

### 6.7 What changed LLM behaviour, by how much
| Change | Effect |
|---|---|
| Hint that an analogue exists | GPT-4 recall 0 to 1.00, precision about .50 |
| "State the message" CoT (ARN) | up to +30 points on far analogies |
| Code execution (letter strings) | GPT-4 vs humans from P=8.9e-13 to P=0.496 |
| Self-generated analogues, strong model | +1 to +4 points; +10.7 over 0-shot CoT on davinci-003 |
| Scale | self-generation helps only at davinci-002 and above; production gap shrinks with size |
| Answer order swap | GPT-4 drops 0.89 to 0.61 or 1.0 to 0.72 |
| Paraphrase target | GPT-4 -0.14, humans -0.08 |
| Story length 1 to 30 sentences | GPT-4 89.1 to 60.7 |
| More reasoning tokens (noisy analogy) | no gain |

Caveat: most LLM studies use GPT-3 to GPT-4-era models. Only Stevenson (Claude-3.5, GPT-4o), Musker (Claude 3) and Camposampiero (o3-mini, R1) touch newer ones. No study applies the Gick-Holyoak paradigm to a current frontier model with many trials.

## 7. What our agent should take

Operator O7 already exists in SCHEMA.md. These items refine it. Marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **O7: a forced retrieval step.** Before mapping, the program makes the model answer "which known problem or stored case has the same structure as this one? Name it or say none." Never rely on the analogue being "noticed" inside a long context. Part: O7 / S6. [E] K01, K12. Evidence a01, a02, a28, c11.
2. **O7: retrieval is two-stage.** Cheap broad filter (embeddings or keyword vectors, keep several) then a structural relational check. Part: O7 / memory. [E] K09, K02. Evidence a12, a19, a22, a23.
3. **O7: describe cases by structure before indexing.** Index and query by relational summary (roles, constraints, goal), not topic nouns, because surface-only retrieval returns look-alikes (Karla .56 and .53 vs analogy .12). Part: O7 / memory. [E] K02, K03. Evidence a10, a22. The exact index type is open (Test first).
4. **Reject surface false friends with a code check on the mapping.** The mapping must be one-to-one, and every target constraint must have a counterpart or be marked uncovered. Code checks typed mappings; the model does not grade itself. Part: O7 with G3 and G5. [E] for the need: K03, K12, K13. Evidence a21, a28, c07. The check's effect size is untested (U4).
5. **O7: use two analogues when the case matters.** Compare two solved cases and write the shared rule in neutral wording. One case plus a principle statement is not enough. Part: O7. [E] K04, K05 for humans. Evidence a06, a07, a13. The LLM version is in Test first.
6. **G (bench rule): randomise and swap answer order in every analogy or case-choice evaluation.** GPT-4 story analogy swings 0.89 vs 0.61 with order. Part: G / bench design. [E] K16. Evidence b15, d09. Running each test in two formats is [S] (K26, d14).
7. **O7: far analogues only at impasses and in open mode.** Already in the schema; this evidence agrees. Far-vs-near (GPT-4 29.1%) says far sources are risky; over-application after a hint (precision about .50) says every retrieved analogue must pass a check. Part: S6 / O7. [E] K12, K13.
8. **Code does counting, indexing and string handling inside a mapping.** GPT-4 with code matches humans on the shuffled alphabet. Part: G5 / S4. [C] cause is disputed (K15, d04), but using code costs little.
9. **Do not add thinking tokens to an analogy step.** More reasoning did not help on noisy analogy. Covered by G11. [S] K25, consistent with [E] G11.

### Test first (not established; each has a row in UNKNOWNS.md)

- Equal-token value of an O7 retrieval step on real problem sets (gap 1, never measured). U1.
- Self-recall of analogues vs fixed few-shot vs retrieved cases on our model. K17 is [E] for older models; K18 says gains are +1 to +4. U2.
- Two-analogue schema extraction for LLMs (K04 is human; Thought Propagation says one layer gives most of the gain). U3.
- Structure check lowers over-application after a hint (precision about .50 in Puranam). U4.
- Relational-summary vs embedding index for the analogue store (gap 6). U5.
- Restate the target in schema vocabulary before retrieval (K06 single-source). U6.
- Step-back principle before mapping (K20 single-source). U7.
- "State the message" before far analogy (ARN, up to +30). U8.
- Summarise vs critique retrieved cases (K07 single-source, human). U9.
- Sub-concept listing before retrieval (K21: closed-set gain, open-set about zero). U10.
- Cross-mapped causal-chain check (K10, human children). U11.
- Reasoning-model unaided retrieval (gap 4). U12.
- Counterfactual-alphabet rule-in-words test (gap 5). U13.

## 8. Concrete tests on our bench

All arms get equal tokens, including setup and retrieval calls (G7). Answer order and item order are randomised and swapped in every multiple-choice item (K16). Report each metric with counts and a paired comparison on the same items.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Puranam-style matching: 20 short business or science problems, each with 2 stored cases (one true analogue, one surface look-alike) plus a no-analogue control | (a) plain CoT, (b) analogue in context, no cue, (c) forced "which case has the same structure? or none" step, (d) c plus code structure check | precision, recall, F1 of source choice; final solve rate | (b) near-zero recall; (c) recall near 1.0, precision about .5; (d) precision above .8 at recall above .8 (to be shown) |
| T2 | ARN-style far-vs-near distractor, 100 items, order swapped | plain; relational-mapping step; "state the message" CoT | accuracy on far-analogy vs near-distractor | plain about 30%; CoT up to +30 points (ARN report) |
| T3 | Real problems (GSM8K-hard, MATH level 4-5, small code tasks) | plain CoT; fixed 3-shot; self-recall K=3; retrieved from store; best-of-N at equal tokens | accuracy | +1 to +4 points for self-recall on strong models; may lose to best-of-N (G7 decides) |
| T4 | Same problems as T3, store holds two true analogues | one analogue + mapping; two analogues + shared-rule writing | accuracy; schema quality scored by code (does the rule predict held-out cases) | small gain, if any; humans gained +24 to +31 points pre-hint (K04) |
| T5 | Store build test: 50 solved cases | index by text embedding; by LLM relational summary; by predicate list | top-1 and top-3 retrieval of the planted true analogue vs the look-alike | summary index beats text embedding on true-analogue rate; closed-set differences are only a few points (a30) |
| T6 | Target restatement | query with original text vs query reworded into schema vocabulary | retrieval hit rate | single-source; 74% vs 10-23% in humans, confounded |
| T7 | Counterfactual letter-string items (shuffled, symbols) | agent with code tool; without; rule stated in plain words with the alphabet | accuracy vs human .75 | with code near human; without .35 to .49; rule-in-words separates indexing from abstraction |
| T8 | Cross-mapped items (same objects, different roles) | map without role check; map with typed role check by code | accuracy | gain mostly on cross-mapped items |
| T9 | Summarise vs critique each retrieved case | two instructions | mapping success | human effect 61% vs 28%; unknown for LLMs |
| T10 | T1 on a reasoning-capable model | normal vs high effort | recall and precision | no gain from effort (K25 analogue) |
| T11 | Position and paraphrase audit | swap answer order; paraphrase the correct target | accuracy change | GPT-4 lost 0.14 to 0.28 under swap or paraphrase; the scaffold should shrink the drop |

## 9. What does not transfer, and why

- **Duncker's radiation problem is a poor general test.** Ill-defined, very famous, steered by the analogue (a01 limits). College students only. The human line has no ecologically valid problem-solving test.
- **The human noticing failure is partly a memory problem.** People forget the structurally relevant source more than the irrelevant one (Bearman: surface-similar forgotten 16 times, conceptually similar 14, non-analogous 1). An agent with a perfect text store does not forget; its problem is cue matching, which a code step can fix. The 30%-vs-75% numbers do not set a target for the agent.
- **Evaluate vs summarise.** A human interference effect on memory (b05). Probably does not apply to an agent. Test only because it is cheap (U9).
- **Delay and context shifts** (one week, different room) do not exist for an agent.
- **Child-development results** (systematicity from about age 8) say nothing about LLM capacity.
- **Letter-string and matrix tasks** mix analogy with alphabet knowledge, counting and tokenisation. Do not read them as analogy ability alone.
- **Analogical prompting gains were measured mainly on math and code with GPT-3.5 and PaLM-2 era models.** A current frontier model already solves most GSM8K; room for gain is small.
- **ExpeL, Buffer of Thoughts and Thought Propagation retrieve near analogues** (similar task descriptions or neighbour sub-problems). They test case reuse, not the far analogy of the Gick-Holyoak line.
- **Author-reported agent gains** use different baselines and unmatched tokens. They are hypotheses for us, not evidence.
- **Analogues as voters or debaters** are blocked by G4 and G9. Several analogies are not independent samples.
- **Section 4b of SCHEMA.md ("not to add") still applies.** Nothing here justifies a standing "think by analogy" phase on routine problems.

## 10. Open questions

1. At equal tokens, does a forced retrieval step (O7) improve a current frontier model on real problem sets, against plain CoT and best-of-N? No study.
2. Do two explicit analogues plus a shared-rule write-up give an LLM a gain like the +24 to +31 point human pre-hint gain?
3. After a hint, does a structure check on a typed mapping remove the over-application (precision about .50)? Does a code-run or consistency check do it?
4. Do reasoning models retrieve a deep analogue unaided? Does extra thinking help or hurt?
5. Is the counterfactual-alphabet failure a lack of abstraction or a task-demand/indexing artifact? The rule-in-words run was never done.
6. Which index works for an analogue store: text embeddings, predicate summaries, or LLM-written abstractions? Closed-set results show only a few points between options.
7. Does restating the target in schema vocabulary transfer to LLM retrieval? Is the gain from the wording or from the three analogues?
8. Do "evaluate vs summarise" instructions change LLM use of retrieved cases?
9. How much do answer-order and paraphrase bias distort ARN and StoryAnalogy? No order-swap rerun was found.
10. What are the adult human effect sizes of Gentner's systematicity preference (Clement and Gentner; Markman and Gentner), and how do LLMs match them on the same materials?
11. Why is the pre-hint rate 30% in 1983 but 1.3-8% in Bearman? Distractor load and instructions are untested guesses.
12. Do the gains of analogical prompting persist in current frontier models, where baselines are already high?

## 11. Sources

[V] = opened and read (full text or full page) by this series. [M] = snippet or abstract only, not opened.

**Human studies**
- [V] Gick and Holyoak (1983) Schema induction and analogical transfer. https://www.gwern.net/doc/psychology/1983-gick.pdf
- [M] Gick and Holyoak (1980) Analogical problem solving, Cognitive Psychology. https://deepblue.lib.umich.edu/items/c0edbf58-93fd-41d4-91d6-22ae89d1adca (numbers via later papers)
- [V] Holyoak and Koh (1987) Surface and structural similarity in analogical transfer. https://link.springer.com/content/pdf/10.3758/BF03197035.pdf
- [V] Catrambone and Holyoak (1989) Overcoming contextual limitations on problem-solving transfer. https://sites.lifesci.ucla.edu/psych-reasoninglab/wp-content/uploads/sites/273/2021/04/Catrambone_Holyoak1989.pdf
- [V] Holyoak and Thagard (1989) Analogical mapping by constraint satisfaction (ACME). https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Holyoak_Thagard.1989.pdf
- [V] Thagard, Holyoak, Nelson and Gochfeld (1990) Analog retrieval by constraint satisfaction (ARCS). https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Thagard_etal1.AI_.1990.pdf
- [V] Gentner and Forbus (1991) MAC/FAC. https://www.qrg.northwestern.edu/papers/Files/macfac91%28searchable%29.pdf
- [V] Gentner and Toupin (1986) Systematicity and surface similarity in the development of analogy. https://groups.psych.northwestern.edu/gentner/papers/GentnerToupin86.pdf
- [V] Bearman, Ormerod and Ball (2002) A negative effect of evaluation upon analogical transfer. https://eprints.lancs.ac.uk/id/eprint/10171/1/TomOrmerod20030627T104300.pdf
- [V] Beveridge and Parkins (1987) Visual representation in analogical problem solving. https://link.springer.com/content/pdf/10.3758/BF03197721.pdf
- [V] Alfieri, Nokes-Malach and Schunn (2013) Learning through case comparison (conference version). https://files.eric.ed.gov/fulltext/ED528947.pdf
- [M] Reeves and Weisberg (1994) The role of content and abstract information in analogical transfer (pointer only, no URL)

**LLM and AI studies**
- [V] Webb, Holyoak and Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196
- [V] Webb, Holyoak and Lu (2024) Evidence from counterfactual tasks supports emergent analogical reasoning. https://arxiv.org/abs/2404.13070
- [V] Hodel and West (2024) Response: Emergent analogical reasoning in large language models. https://arxiv.org/abs/2308.16118
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning in LLMs. https://arxiv.org/abs/2402.08955
- [V] Lewis and Mitchell (2025) Evaluating the robustness of analogical reasoning in LLMs. https://arxiv.org/abs/2411.14215
- [V] Stevenson, Pafford, van der Maas and Mitchell (2025) Can large language models generalize analogy solving like people can? https://arxiv.org/abs/2411.02348
- [V] Musker, Duchnowski, Millière and Pavlick (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803
- [V] Hu and Frank (2024) Auxiliary task demands mask the capabilities of smaller language models. https://arxiv.org/abs/2404.02418
- [V] Puranam, Sen and Workiewicz (2025) Can LLMs help improve analogical reasoning for strategic decisions? https://arxiv.org/abs/2505.00603
- [V] Sourati, Ilievski, Sommerauer and Jiang (2024) ARN: analogical reasoning on narratives. https://arxiv.org/abs/2310.00996
- [V] Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/abs/2310.12874
- [V] Ye, Wang et al. (2024) AnaloBench. https://arxiv.org/abs/2402.12370
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Yu, Ying and He (2024) Thought Propagation. https://arxiv.org/abs/2310.03965
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271
- [V] Zheng et al. (2024) Take a step back. https://arxiv.org/abs/2310.06117
- [V] Bhavya, Xiong and Zhai (2022) Analogy generation by prompting LLMs. https://arxiv.org/abs/2210.04186
- [V] Ding, Srinivasan, MacNeil and Chan (2023) Fluid transformers and creative analogies. https://arxiv.org/abs/2302.12832
- [V] Mitchell, Palmarini and Moskvichev (2023) Comparing humans, GPT-4 and GPT-4V on abstraction and reasoning tasks (ConceptARC). https://arxiv.org/abs/2311.09247
- [V] Opiełka et al. (2025) Analogical reasoning inside LLMs: concept vectors and the limits of abstraction. https://arxiv.org/abs/2503.03666
- [V] Yuan et al. (2024) AnalogyKB. https://arxiv.org/abs/2305.05994
- [V] Wijesiriwardene et al. (2023) ANALOGICAL (no scores extracted). https://arxiv.org/abs/2305.05050
- [V] Camposampiero et al. (2025) Can large reasoning models do analogical reasoning under perceptual uncertainty? https://arxiv.org/abs/2503.11207 (an earlier snippet copy, https://aitopics.org/doc/arxivorg:C527BA0F, was [M])
- [V] Barakat and Kochmar (2026) Teaching through analogies. https://arxiv.org/abs/2605.24211
- [M] Webb, Holyoak and Lu reply as described on the Nature Human Behaviour page. https://www.nature.com/articles/s41562-023-01659-w
- [M] Reimplementation and Reinterpretation of the Copycat Project. https://export.arxiv.org/api/query?search_query=Copycat
