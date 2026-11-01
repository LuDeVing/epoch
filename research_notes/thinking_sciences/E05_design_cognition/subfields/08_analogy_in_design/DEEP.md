# Analogy in design: deep document

*Subfield E05.08, near and far analogues. Built from evidence_a-d.jsonl (a01-a36, b01-b27, c01-c26, d01-d20), claims.jsonl (K01-K24) and critique.md in this folder. Ids like a31 are evidence lines; K07 is a claim. "Opened" means the page or PDF text was read; "second-hand" means a secondary source reported it.*

## 1. What it is

Design by analogy (DbA) means solving a design problem by borrowing structure from a different problem or product. The source is called the base or analogue. The problem at hand is the target.

Two questions run through the field.

1. How far should the source be from the target? "Near" means same domain or same function. "Far" means a different domain, such as a bird wing for a drone or a general splitting an army for a tumour.
2. How is the source found and mapped? Humans retrieve by surface match. They only profit from relational match.

For our agent the home is operator O7 (map an analogue), plus lesson memory (S9) and the rule that novelty is judged by running code (G8). The current O7 line in SCHEMA.md says: unaided analogy rarely transfers [E], the mapping step is [S], and far sources lower the average and raise the spread, so they belong at impasses and in open mode.

This document tests that line against the full record. Short verdict:

- The "far raises spread, lowers mean" claim is NOT as solid as the schema says. Two same-group experiments point opposite ways (K02, contested). Only the spread part has a second source.
- The human result "any analogy use goes with better outcomes; distance adds little" is the best-supported finding (K06).
- LLM evidence is old (GPT-3 to GPT-4, 2022-2023) for near/far, and thin for design. No frontier-model, equal-token, code-checked test exists (critique GAP 1).
- Small gains from self-generated exemplars shrink or vanish on strong models (K13, K19).

## 2. History and theories in depth

### 2.1 Structure-mapping theory (Gentner, 1983 on; review a01, a02, a03, a06, a07, c26)

Gentner and Markman (1997, opened) state the theory. An analogy is an alignment of relational structure between base and target. Object attributes are mostly dropped. Three constraints:

- One-to-one matching: each base element maps to at most one target element.
- Parallel connectivity: if two relations match, their arguments must match.
- Systematicity: a connected system of relations, tied by higher-order relations such as "causes", beats the same number of isolated matches.

Cross-mapping shows structure beats objects. When identical objects take swapped roles, people align by role (1:3 :: 3:9 pairs the 3s by role). Time course (cited from Goldstone and Medin 1994, Ratcliff and McKoon 1989): under about 700-1000 ms, similarity rests on local matches; with more time, relational matches take over. Alignable differences count more than non-alignable ones.

Candidate inferences: unmatched base facts are projected to the target. In a story-prediction study people predicted the key fact tied to the matching causal antecedent more than twice as often as the other fact (a07, second-hand). Willingness to project rose with shared causal relations (Lassaline 1996).

### 2.2 The retrieval-versus-use gap (a04, a08, b14, b15)

This is the founding fact for design.

- Gentner, Rattermann and Forbus (1993): people recalled surface-matched stories 55% of the time versus 12% for purely analogical matches. Yet only relational matches were rated useful for inference. (Quoted second-hand in b14, b15. Primary not opened. K07 is therefore single-source.)
- Gick and Holyoak (1980, 1983): on Duncker's radiation problem about 10% solve unaided; about 41% apply the fortress analogy spontaneously after the story; about 85% when told to use the earlier story (b14, second-hand).
- Same split reported for Ross (1987, 1989) and Keane (1988); Hammond, Seifert and Gray (1991) is a counter-case.

Meaning: what comes to mind is near on surface. What helps is near on structure. These are different sets.

### 2.3 Computational models (a02, a05)

- SME (Falkenhainer, Forbus, Gentner): stage 1 matches identical predicates blindly; stage 2 merges local matches into structurally consistent clusters (kernels); stage 3 merges kernels into one to three global mappings; then projects candidate inferences. It needs hand-built predicate representations. Getting those from messy design text is the weak point.
- MAC/FAC (Forbus, Gentner, Law 1995): MAC is a cheap scan over cheap content vectors. FAC runs SME on the few survivors. It reproduces surface-heavy remindings with structure-heavy quality judgments. (Not opened; the parallel subfield "Analogical retrieval (MAC/FAC)" covers it in depth.)

### 2.4 Design-specific experiments (the human core)

- Linsey and colleagues: WordTree (re-represent the problem as function words, then search linked words for analogies, 2012) and fixation work (2010). Named only in opened sources (a29); no numbers read.
- Chan et al. (2011), the "far helps" study (a31, b01-b04, opened).
- Fu et al. (2013), the "far hurts" study (a32, b05, b06, opened).
- Chan, Dow and Schunn (2014/2015), field data from OpenIDEO (a33, b07, b08, opened).
- Chan and Schunn (2014/2015), in vivo professional team (a34 abstract; b11, b12 opened).
- Goel's line (structure-behaviour-function models, biologically inspired design) is named in the focus statement but no Goel primary source reached these files. This is a gap, not a finding.

### 2.5 The AI-for-DbA line (a11, a12, a26, a28)

Patent-network knowledge distance (Luo, Sarica and Wood 2021), purpose-mechanism analogy mining (Hope et al. 2017), GPT-based bio-inspired design (Zhu and McComb 2022/2023), then LLM prompting (Ding et al. 2023) and a 2026 survey of 85 studies (Li et al., CHI 26) that finds a significant lack of rigorous empirical evaluation (a28, c25, d19).

## 3. Core findings with exact numbers

Status key: E = established (two or more independent sources agree), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Far-field patent examples raised novelty and quality spread, cut quantity (novices, energy harvester) | N=153 seniors, 1,321 ideas. Far vs near: solution transfer d=0.60; mean and max novelty d=0.56; quality variability d=0.64 (vs control 0.78); quantity d=-0.30 (about one idea fewer); mean and max quality no distance effect. Far alone vs control on novelty not significant | Chan et al. 2011 (a31, b01) | S, K01 |
| Less-common examples help, more-common hurt | Less vs more common: novelty d=0.61, quality SD d=0.62, quantity d=0.67, breadth d=0.61. More-common vs control: breadth d=-1.03, quantity d=-0.76. Far plus less-common vs control: mean novelty d=1.14, max d=1.29 (post hoc) | Chan 2011 (b02) | S, K04 |
| Picture vs text made no difference to final novelty | Mean novelty p=.20, max p=.49, quality SD p=.44. Text raised copying (d=0.60) and cut quantity by about 2 ideas | Chan 2011 (b03) | S |
| Part of the far quantity cost is mapping time | After removing example-processing phase, distance effect on quantity p=.47; commonness effect stayed (p<.05, d=0.56). Correlational path model | Chan 2011 (b04) | S, K05 |
| Far patents hurt: lower max novelty and lower mean quality than near | N=72 (70 analysed), 24 per cell. Max novelty F(2,59)=4.14, far lower than near d=0.82, than control d=0.91 (p=.008). Mean quality F(2,65)=4.07, near>far d=0.76; near vs control d=0.54 n.s. Max quality F(2,65)=4.13, d=-0.76 (far vs control d=-0.72, p=.11 n.s.). Far patents rated less relevant, d=-0.64. Quantity p=.94 | Fu et al. 2013 (a32, b05) | S, K02 |
| Near and far are relative: sweet spot at intermediate distance | Near = 0-1 node, far = 3 nodes on a patent-structure map. Account is post hoc; position depends on problem and patent set | Fu 2013 (b06) | S, K03 |
| Literature on far sources splits | Only 4 earlier studies had 18+ per cell (Chan 2011, Fu 2013, Goncalves 2013, Tseng 2008): evenly for and against | Chan, Dow, Schunn 2014 (b08) | C, K02 |
| Field data: using any cited source goes with shortlisting; distance adds little | 2,341 concepts, 12 challenges, 1,190 contributors. 707 citing concepts; 110 shortlisted (16%) vs 241 of 2,341 (10%). AIC 511.39 baseline, 506.04 with max distance, 505.13 with mean distance. Closer sources were more beneficial in all 12 challenges | Chan, Dow, Schunn (a33, b07) | E (field plus lab, both correlational), K06 |
| Professional team: far analogies did not produce jumps; they raised idea rate | 144 analogies, two transcripts. After far analogy concepts were not further from predecessor. Study 2, N=938 slots: lag 0 OR=1.99 (b=.69, p<.01, R2=.013); lag 1 OR=1.88 | Chan and Schunn (b11, b12, a34) | S |
| Biological (far) vs within-domain (near) raised novelty; bio vs cross-domain (middle) no difference | 26 novice teams, one source from each of 3 domains. Abstract only | Biomimetics 2024 (d18) | S |
| Retrieval follows surface; use follows structure | 55% vs 12% recall; Gick and Holyoak about 10% / 41% / 85%. Second-hand | Gentner 1993; Gick and Holyoak (a04, b14, b15) | S, K07 |
| Purpose-mechanism analogy mining beat TF-IDF and random in a human ideation test | 38 MTurk workers, 12 seeds, 749 ideas. k=2 on 9 shared seeds: 46% (N=105) vs random 37% (49) vs TF-IDF 30% (54), p<=.01. k=3: 38% (118) vs 22% (68) vs 21% (63). Mixed-model pr(good) 0.71 [0.48, 0.87] vs 0.28 and 0.27 (k=2); 0.56 [0.36, 0.75] vs 0.16 and 0.14 (k=3). Fleiss kappa 0.51 | Hope et al. 2017 (a13, b16, c21) | S, K09 |
| Analogical encoding (compare two cases, state the shared principle) raised transfer | Exp 1: contingency use 0% to 69% (11/16); tradeoff 19% to 38%. Exp 2: MBA students nearly 3x as likely to use the strategy | Loewenstein, Thompson, Gentner 1999 (a35, b13) | S, K08 |
| Surface retrieval is the default failure of tools and LLMs | SBERT 77.9% on near analogies; TF-IDF returned same-domain items; over 50% of GPT-based bio-analogies were birds; GPT-4 story answers biased by sentence overlap | b17, c21, a26, b19 | E, K10 |
| 2022-23 LLMs do far worse on far than near analogies | GPT-3 stories: near p=.0039, far p=.065 (humans N=54, both p<1e-22; OR=0.37, p=.0003). ARN: near 75.0% vs far 39.6% model average; humans 97.9% / 94.1%. GPT-4 zero-shot with mapping instruction 94.0 / 92.5 (near) and 57.1 / 29.1 (far); 17.7 on the hardest cell without the instruction. StoryAnalogy: humans 85.7%, best model 37.7 points lower | a18, b17, c18, a24, c17 | E, K11 |
| LLM analogy robustness is disputed | Counterfactual letter-strings: humans 0.753 [0.734, 0.773] (N=136); GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452. Story order bias: GPT-4 0.89 correct-first vs 0.61 second (Webb run); 1.0 vs 0.72 (their run); humans 0.78 both. Paraphrase: GPT-4 0.86 to 0.72. With code execution GPT-4 matches humans: P=0.92 (humans N=99/97) | a17, a20, b19, c16, d15 | C, K12 |
| Self-generated exemplar prompting: small gains | GPT-3.5 GSM8K 77.8 vs 0-shot CoT 75.8 vs 5-shot 76.7 (+1.1); MATH 37.3 vs 33.9 vs 34.9 (+2.4). With self-consistency 85.3 (+7.5) and 46.0 (+8.7). GPT-4 Codeforces Acc@1 19 vs 16 (0-shot CoT) | Yasunaga et al. 2024 (a21, d01) | C, K13 |
| Strong models ignore exemplars | Qwen2.5 7B/14B/72B on GSM8K and MATH: exemplars do not beat zero-shot; noise in exemplars no loss in most settings. R1: few-shot "consistently degrades" (no numbers) | Cheng 2026 (d03); DeepSeek-R1 (d04) | C, K19 |
| Analogy generation scales with size | Meaningful, no-source: 1.90% (0.3B), 15.61%, 48.29%, 70.05% (175B) vs human 66.67%. With a source: 8.97, 29.05, 38.46, 53.79 vs human 71.88. 1,407 analogies, kappa 0.347 | Bhavya et al. 2022 (a23, c08) | S, K14 |
| One-shot examples make GPT-3 analogies farther and more often useful | Zero-shot: useful 0.68, duplicates 0.24, unique-and-useful 0.43, similarity to problem 0.72. One-shot (manager): 0.82, 0.12, 0.70, 0.48. One-shot (Duncker): 0.80, 0.03, 0.77, 0.43. Few-shot: 0.67, 0.02, 0.65, 0.31 (Table 1; the text's "80% vs 40%" matches neither column, use the table) | Ding et al. 2023 (a14, critique) | S, K16 |
| Analogue value cannot be predicted in advance | 110 analysed, 220 pairs. Added information 185/220 (84.09%), rejected 23 (10.45%). Median helpfulness 4/5. A-priori usefulness vs in-use helpfulness r_pb=-0.0266, p=0.6939. Harm upper bound about 25% | Ding 2023 (a15, a16) | S, K16 |
| Looser prompts: more novel, less feasible | Relevancy pass 62% to 80% across types; looser generators farther in word-mover distance; 9 usable engineer surveys | Zhu et al. (a26, c01, c02) | S, K15 |
| LLM ideas rated more novel but redundant, and lose value on execution | Novelty human 4.84, AI 5.64, AI reranked 5.81 (79 reviewers, 49 ideas per condition); about 5% of 4,000 seeds non-duplicate. After execution LLM ideas fell 1.0 to 1.9 points, human ideas flat (43 experts) | Si et al. 2024, 2025 (b24, d14) | S, K17; E for K22 |
| Abstraction before solving: helps weak models more | MMLU Physics: PaLM-2L CoT 65.0 to step-back 73.2; GPT-4 CoT 82.9 to 84.5. TimeQA: fixes up to 40% of errors, introduces up to 12% (11.9%) | Zheng et al. 2024 (d05, d06) | S, K23 |
| Abstracted memory beats concrete or full-history memory; retrieval can hurt | AWM Mind2Web cross-task: +4.0 step SR vs concrete-example retrieval. Dynamic Cheatsheet AIME 2024 Sonnet 23.3 baseline, 26.7 full history, 50.0 curated. GPT-4o MMLU-Pro Eng 53.2 to 44.0 | Wang 2024; Suzgun 2025 (d09, d11, d12, d13) | S, K20 |
| Task-level similarity key beat step-level and random in agent memory | ALFWorld best 59.0%; random "significant drop" | ExpeL (d07) | S, K21 |
| No rigorous 2024-2026 expert or finished-design test of LLM DbA | 85-study survey; 32-student counterbalanced study: human-only higher on innovation | d19, d20 | E, K24 |

## 4. Mechanisms and models

Each mechanism below is stated so it can be built. Evidence level is given.

### 4.1 Two-key retrieval (surface vs structure)
Cause: humans, TF-IDF, SBERT and LLMs all rank by surface overlap (K10). Structure-mapping says the useful base shares a relational skeleton.
Build:
1. Take the target problem text. Ask the model for an abstract schema in a fixed form: goal, constraint, mechanism ("what causes what"), with domain nouns replaced by slots. Hope et al. needed exactly this scaffold for workers (write a schema, then a more abstract one) to avoid surface matches (c21).
2. Embed the schema string, not the raw text. Search the analogue bank by that vector (the purpose/mechanism approach, K09).
3. Return k candidates (Hope showed 12 inspirations per seed; the 46% / 38% figures are judge-threshold rules k=2 and k=3, not retrieval k).
4. Log the fraction of retrieved items from the same domain as the target. This is a free diagnostic (K10).
Status: single-source for the gain (K09). The three-way key comparison (surface text vs abstract string vs typed slots) has never been run (K21).

### 4.2 MAC/FAC as an agent pipeline
MAC = cheap embedding scan over the bank, keep about 10. FAC = a structure check on each: write a one-to-one mapping (source element to target element), keep those whose mapping passes a test. For code tasks the test is running the mapped procedure on the examples AND on a held-out or mutated input (G3). Status: design proposal built from a05, a02. Not tested on LLMs.

### 4.3 Typed mapping with candidate inferences (SME-like)
Output form for O7:
- pairs: base element to target element, one-to-one
- relations that carried the match (cause, constraint, order)
- candidate inference: the base fact that has no target counterpart yet, now a hypothesis for the target

Reject the mapping if two target elements share a base element or if the matched relations are unconnected (systematicity). Then run the candidate inference as code. Status: theory [E] in humans (a01, a07); no LLM test of the typed form. The ARN result that an explicit system-mapping instruction lifts GPT-4 on the hardest cell from 17.7 to 29.1 (and gives 94.0 on near) (c18) is the only LLM hint that an explicit mapping instruction matters.

### 4.4 Distance as a tuned variable, not a constant
The inverted-U (b06) says success peaks at middle distance, at a place that depends on problem and source set. To implement: compute distance between target schema and each candidate (embedding or graph hops), bin it into 3-4 bins, and log pass rate per bin per task class. Choose the bin online per class. AWM (d10) found online-induced workflows gained more as train-test gap grew (cross-domain step SR 32.6 offline vs 35.5 online), which supports per-task estimation. Status: contested (K02, K03).

### 4.5 Mapping cost model
Chan 2011 found far examples cost about one idea (d=-0.30) and the cost vanished once example-processing time was removed (p=.47, b04). So an agent must charge mapping tokens to the same budget as attempts (G7, G12). An analogy step that costs 2 attempts must win by more than 2 extra samples. This is why Yasunaga's result matters: self-consistency added +7.5 on GSM8K while the analogy method added +1.1 over 5-shot (d01).

### 4.6 Analogical encoding for memory
Loewenstein et al.: do not store one lesson. Put two solved cases side by side, write the shared principle, store that principle with both cases as support. For S9: when a new solved problem shares a class with a stored one, run one compare-and-write call, and store the abstracted rule. ExpeL does the failure-versus-success pair version and gained on FEVER transfer (ReAct 58, ExpeL Transfer 63 without task demos, 65 with), but no ablation separates pair-comparison from single-case summaries (d08). Status: single-source in humans (K08), indirect in agents.

### 4.7 Screening an analogue by execution
Since a-priori usefulness rating had r=-0.027 with in-use helpfulness (a16) and LLM ideas lose 1.0-1.9 rating points on execution (d14), an analogue's value is measured by a matched with/without run checked by code. A memory audit found 169 credited retrievals but only 10 true marginal helps (5.9%, abstract only, d17). So the screen is a paired run, not a story about why it helped.

## 5. What holds up

### 5.1 Replications and failed replications
- Chan 2011 (far helps novelty) was NOT reproduced by Fu 2013 (far hurts max novelty, d=-0.82 vs near). The two are the same group, similar protocol, different problem and stimulus set (a32, b05). The authors reconciled them post hoc by an inverted-U on a shared patent map. This is an explanation after the fact, not a test (K03).
- Chan, Dow and Schunn found in field data that closer sources went with better outcomes in 12 of 12 challenges (b07). Lab and field disagree with "far is the lever".
- The Chan and Schunn in vivo study rejects the "jump" account: concepts after a far analogy were not further from the prior one (b11). Far analogies raised the idea rate (OR=1.99 at lag 0) with R2 of only .013.
- Webb et al. (2023) human-like LLM analogy: Lewis and Mitchell (2024, 2024b) reproduce the original numbers but show failure on counterfactual alphabets (humans 0.753 vs GPT-4 0.452), order bias and paraphrase sensitivity. Webb et al. (2025, PNAS Nexus) answer that most failure is counting: GPT-4 with code execution matches humans (P=0.92). Both sides use their own models and tasks. K12 stays contested.
- Yasunaga's gains: no independent replication. Recent evidence (Cheng 2026; R1 note) says strong models ignore exemplars. K13 moved from established to contested.

### 5.2 Power and design problems
- Most earlier far/near experiments had 12 or fewer per cell (b08). Only four had 18+.
- Nearly all human studies use novices (students, crowd workers), one problem, short sessions, early ideation only (critique). No expert replication; no finished-design outcome.
- Ratings were made by few raters (one researcher in Ding; five graduate students in Hope; two graduate students as SCAR humans).
- Hope et al.'s own intervals are wide; the authors say a replication may land between conditions (a13).

### 5.3 Moderators named in the record
- Stage of design: far for early vision, near for refinement (d19, secondary, citing human studies; Tseng 2008 reported far helps more after ideation began, second-hand b09).
- Goal: quantity favours near, quality-variance favours far (d19; Chan 2011).
- Expertise: novices near, experts far (d19). Chan, Dow, Schunn say no study directly tests the expertise-mediation account (b10).
- Commonness of the source: less-common better, independent of distance (b02).
- Modality: picture vs text no effect on final novelty (b03).
- Source relevance: far patents were rated significantly less relevant (d=-0.64), which may drive the Fu result (b05).
- Model strength: Yasunaga self-generation helps only with text-davinci-002 and later; weaker models do better with retrieved exemplars (d02). Step-back helps PaLM-2L 7 to 8 points, GPT-4 0.3 to 1.6 (d05).

### 5.4 Interventions that worked
- Comparing two cases and stating the shared principle (humans, negotiation; about 3x).
- Scaffolding workers to write a schema then a more abstract one before searching (Hope).
- Purpose-mechanism retrieval over TF-IDF (Hope, single study).
- A hint to use the earlier story (Gick and Holyoak, about 10% to 85%).
- Telling GPT-4 to map the systems explicitly (ARN: far cell 29.1 vs 17.7 without).
- Code execution for GPT-4 counterfactual letter strings (P=0.92 vs humans).
- Curated, abstracted memory over full history (AIME 2024 Sonnet 50.0 vs 26.7 vs 23.3).

### 5.5 Interventions that did not work or backfired
- Unaided analogy: rarely transfers (Gick and Holyoak).
- Far stimuli in Fu 2013: lower max novelty and quality.
- More-common examples: breadth d=-1.03 vs control (fixation).
- K=1 self-generated exemplar hurts because the model leans on it; K=3 to 5 best (a22).
- Demonstrations hurt near-analogy detection while helping far (ARN, GPT-3.5 and Llama-2).
- CoT with worked explanations raised GPT-4 but lowered ChatGPT and InstructGPT-003 on SCAR (c07).
- Intrinsic self-correction: GPT-4 GSM8K 95.5 to 89.0 over two rounds (d16).
- Full-history memory: GPT-4o AIME 2024 20.0 to 13.3 (d12). Curated retrieval lowered GPT-4o MMLU-Pro Engineering 53.2 to 44.0 (d11).
- Model self-rating of idea quality: failed as a ranker (b24).

## 6. Language models

### 6.1 Recognising analogies
| Task | Result | Era | Id |
|---|---|---|---|
| Story analogies, near | GPT-3 p=.0039; GPT-4 near perfect (preliminary) | 2022-23 | a18 |
| Story analogies, far | GPT-3 p=.065 n.s.; GPT-4 above chance p=.0039 (preliminary) | 2022-23 | a18 |
| ARN narratives, near | GPT-4 94.0 / 92.5; model average 75.0; human 97.9 | 2023 | c18, b17 |
| ARN narratives, far | GPT-4 57.1 / 29.1; GPT-3.5 50.4 / 21.7; model average 39.6; human 94.1 | 2023 | c18, b17 |
| StoryAnalogy multiple choice | ChatGPT about 30%, GPT-3.5 37.1%, LLaMa-65B 28.6%, FlanT5-xxl 45.4%, humans 85.7%, chance 25% | 2023 | c17 |
| SCAR system analogies | GPT-4 69.10 avg (1-shot plus background; English 77.17); ChatGPT 65.87; InstructGPT-003 49.66; humans 85.94/86.03 (two grad students) | 2023 | a25, critique |
| Long-text analogies (13 datasets, 8 LLMs) | Harder as the six-level taxonomy rises | 2023 | b25 |

Pattern: models are pulled by shared nouns. Easy random negatives are rejected (under 20% chosen), hard negatives that share entities are not (c17). A far analogue with a near distractor is the worst case: 33.9% in ARN (b17).

### 6.2 Generating analogies
- InstructGPT 175B reaches 70.05% meaningful vs human 66.67% with no source given; only 53.79% vs human 71.88% when it must explain a given source (c08). Imperative prompts at low temperature win. Spelling errors hurt (c09).
- GPT-3 zero-shot analogies stay close to the problem and repeat (24% duplicates). One example cut duplicates to 12% (3% with the Duncker example) and raised unique-and-useful from 0.43 to 0.70-0.77 (a14).
- Fine-tuned GPT-3 for bio-inspired design returns birds first in over 50% of cases (a26). Looser problem statements gave more distant, more novel, less feasible concepts (c01, c02). With few-shot GPT-3 the near/far pattern faded and unique ideas rose (GPT-2 fine-tuned 35.8-40.8% unique vs GPT-3 few-shot 71.8%, 67.4%; c22). Novelty proxy confounded with text length.
- Ideas look more novel than expert ideas (5.64 vs 4.84) but the pool collapses (about 5% non-duplicate) and the model cannot rank them (b24). After execution the lead disappeared and flipped (d14).

### 6.3 Using analogy to solve (prompting)
- Analogical prompting: tiny gains over 5-shot (+1.1, +2.4); larger on Codeforces (GPT-3.5 Acc@1 9 to 15, GPT-4 16 to 19) and BIG-Bench word sorting 66.8 to 75.2, logical deduction 30.0 to 41.6, colored objects 50.4 to 68.0; no gain on temporal sequences (58.0 vs 57.6). Manual audit of 50 correct outputs: 35 good, 9 relevant but wrong, 6 irrelevant exemplars (b22, c11).
- Thought Propagation reports +12 (shortest path), +13 (creative writing preference), +15 (ALFWorld) points. Abstract numbers only; analogues are near, same task type; more calls per item (c20, b27).
- Strong models: exemplars ignored (Cheng 2026), R1 degrades with few-shot (d03, d04).
- Abstraction first: helps PaLM-2L, barely GPT-4 (d05); introduces up to 12% new errors (d06).

### 6.4 What changed performance, by how much
| Change | Effect |
|---|---|
| Model scale (generation) | 1.90% to 70.05% meaningful |
| Explicit system-mapping instruction (ARN, GPT-4, hardest cell) | 17.7 to 29.1 |
| One-shot example (GPT-3 analogies) | unique-and-useful 0.43 to 0.70-0.77 |
| Code execution (letter-string counterfactual) | GPT-4 to human level, P=0.92 |
| Self-generated exemplars vs 5-shot (GSM8K, GPT-3.5) | +1.1 |
| Self-consistency added on top (GSM8K) | +7.5 |
| Abstraction first, over CoT, MMLU Physics (PaLM-2L vs GPT-4) | +8.2 vs +1.6 |
| Curated memory (AIME 2024, Sonnet) | 23.3 to 50.0 (N=30, one run) |
| Abstracted workflows vs concrete (Mind2Web) | +4.0 step SR |

### 6.5 What is not known for LLMs
No far-vs-near test on a 2025-2026 model; no equal-token control; no test of model self-rating as analogue filter; no expert or finished-design outcome (critique GAPS 1, 2, 4, 6, 10).

## 7. What our agent should take

Part codes: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **Judge any analogue by a matched with/without executed run, never by model rating or story.** G8, O7. [E] K22, K06; d14, d16, d17, a16. A-priori usefulness r=-0.027; LLM ideas lose 1.0-1.9 points on execution; self-correction lowers GPT-4 GSM8K 95.5 to 89.0.
2. **Do not hard-code distance as the lever. Use an analogue as a candidate step that must beat resampling.** G7, O7. [E] K06 (field AIC drop about 6; lab studies split). Evidence a33, b07, b08, a31, a32. This softens the current schema line: the sign of the far effect is contested (K02), so keeping far analogues for impasses and open mode is a cautious default, not an established rule.
3. **Treat surface retrieval as the default failure; log the same-domain fraction of retrieved analogues.** O7, memory. [E] K10; b17, c21, c02, b19.
4. **Treat an unperturbed analogy pass as no evidence; test mappings on a perturbed or held-out variant.** G3, O7. Direction [E], size contested (K12); a20, b19, c16, d15.
5. **Charge analogue-mapping tokens to the budget; compare at equal total tokens.** G7, G12. [S] K05, but it follows from G7 itself; it is accounting, not a finding to test.
6. **Count no published DbA-LLM gain as proven for our setting.** G7. [E] K24; d19, d20, a28.
7. **Do not add a "recall related problems" step by default for strong models.** O7, S3. [C] K13, K19. Keep it out until a Test-first item shows it beats zero-shot.

### Test first (not yet added)
1. **Near vs far analogue step vs same-token resampling, code-checked, current model.** O7, S3. [C] K01, K02, K03. Evidence a31, a32, b07, d01. The central missing measurement (GAP 1).
2. **Retrieval key: surface text vs abstracted mechanism string vs typed slots.** O7, memory. [S] K09, K21. Evidence a13, b16, c21, d07, d09.
3. **Name-the-shared-structure step before mapping.** O7. [S] K23. Evidence d05, d06, c18. May matter for weak models and do nothing for a strong one.
4. **Compare-two-cases lessons at S9.** S9, memory. [S] K08. Evidence a35, b13, d08, d12.
5. **Abstracted vs verbatim lessons.** S9, memory. [S] K20. Evidence d09, d11, d12, d13.
6. **Distance sweep in 3-4 bins with per-class estimate.** O7, S0. [C] K03. Evidence b06, d10, d19.
7. **Common vs uncommon analogues for breadth.** O7, G1. [S] K04. Evidence b02.
8. **Loose vs strict analogue constraint, with novelty and feasibility logged together.** O7, O8. [S] K15. Evidence a26, c02.
9. **Dedupe by code and count unique candidates per token for analogue-generated ideas.** G8, S3. [S] K17. Evidence b24, c22.

## 8. Concrete tests on our bench

All arms get the same total tokens (analogue-writing and mapping tokens included). The metric is held-out pass by code unless stated. Report fixed-by-step and newly-broken counts separately (as step-back did, d06).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style and code-checked puzzles with known structural cousins (bank of solved items in 3 distance bins) | (a) plain; (b) plain plus extra samples to match tokens; (c) near analogue then solve; (d) far analogue then solve; (e) mid analogue | Held-out pass rate; fixed vs broken vs plain | (c),(d) at or below (b) on routine items; (d) gains only where plain fails all samples. Report sign per task class, not pooled (K02) |
| T2 | Same bank | Retrieval keys: raw text embedding; abstract-schema string embedding; typed-slot match plus code check | Same-domain fraction; held-out pass; helpful-retrieval rate by matched with/without | Schema key lowers same-domain fraction and lifts pass by a few points; Hope's 46% vs 30% (k=2) is the human guide |
| T3 | ARN-style far-analogy items plus code-checked mapping items | Plain; "name the shared structure first"; explicit one-to-one mapping instruction; both | Accuracy on far/near split; fixed vs newly broken | Helps weak models, small or null on strong ones (d05: +1.6 on GPT-4). If far is at chance on the current model, restrict O7 to code-checked mappings (K11) |
| T4 | Perturbed variants of solved items (rename, reorder, paraphrase) | Accept unperturbed pass vs require perturbed pass | Share of analogues that survive; downstream held-out pass | Perturbed pass screens out brittle mappings (Lewis and Mitchell); fewer accepted analogues |
| T5 | Sequence of 40+ related items from 4 classes | S9 lesson formats: none; single-case lesson; compared-pair lesson with written shared principle; verbatim trace | Pass on fresh items of the same and a different class; harm cells | Pair beats single for transfer to a different class (human about 3x; agent effect unknown) |
| T6 | Open-mode idea tasks with an executable novelty check | Near vs far vs no analogue, loose vs strict constraint; dedupe by code | Distinct candidates per 1k tokens; share passing feasibility check; max novelty by code | Far: wider spread, lower mean, fewer ideas (Chan 2011 shape); ask whether spread helps best-of-set |
| T7 | Items where the model self-rates analogue usefulness | Rating by model vs matched-run outcome | Correlation of rating with executed gain | Near zero (a16 r=-0.027); closes GAP 6 |
| T8 | Same items, two source commonness levels | Common vs uncommon sources | Breadth (distinct solution families); pass | Uncommon wider (b02, d=0.61) |

Run T1, T2, T3 first (see UNKNOWNS.md).

## 9. What does not transfer, and why

- **Novice lab samples.** Students and crowd workers fixate on near sources and cannot map cheaply. Our agent has no domain-knowledge gap in the same sense and no social anchoring. Expertise-mediation is untested even for humans (b10).
- **Rated novelty and quality as outcomes.** The human studies score by judges. Our target is correctness checked by code (G8), where the novelty benefit of far analogues is untested (critique weak spots).
- **Quantity of ideas as a lost resource.** Human quantity falls with mapping time (p=.47 once removed). For the agent the cost is tokens, which G7 already charges.
- **Time-based mapping cost.** Humans pay minutes; the agent pays tokens and can run mapping calls in parallel fresh contexts.
- **Field data on shortlisting (OpenIDEO).** An expert shortlist mixes novelty with feasibility. Citation behaviour is self-selected. It says analogy use goes with success, not which step to run.
- **Gick-Holyoak hint effects.** Telling a person to use the story is a free prompt; the agent's version is what retrieval returns, which is already the weak link.
- **Word and letter-string analogy tests.** They overstate analogical skill (SCAR: low overlap with structure success; a25). Letter-string counterfactual failure was largely counting (d15), so it says little about design mapping.
- **Exemplar prompting gains from 2022-23.** Strong models ignore exemplars (d03). The +1.1 margin over 5-shot came from GPT-3.5.
- **The inverted-U.** Post hoc from two studies; the location is problem-specific. It cannot be a fixed distance constant (K03).
- **Persuasive LLM prose about why an analogy fits.** Reasoning text is not evidence (G10).
- **Patents and nature as source banks.** Our banks are previously solved problems and lessons; distance measures built for patents (co-classification, a11) do not carry over.

## 10. Open questions

1. Does a near/far analogue step beat equal-token resampling on a code-checked task for a 2025-2026 model? (GAP 1, nothing found.)
2. Is the far-analogy failure (ARN 39.6%, GPT-3 far p=.065) still present on frontier models? Does naming the shared structure close it? (GAP 2.)
3. Best retrieval key: surface, abstract mechanism, or typed structure? Hope is the only controlled test (GAP 3).
4. Does the mapping-token cost cancel any novelty gain at equal tokens? (GAP 4.)
5. Does comparing two solved cases improve transfer of an LLM's stored lessons as it did for humans (about 3x)? (GAP 5.)
6. Can a model's rating of an analogue predict downstream success? Humans: r=-0.027. (GAP 6.)
7. Where is the distance sweet spot, and must it be estimated online per class? (GAP 7.)
8. Do self-generated exemplars survive an equal-token comparison with extra samples on newer models? (GAP 8.)
9. How often do analogues harm (Ding upper bound 25%; step-back up to 12% new errors), and can a code run screen them cheaply? (GAP 9.)
10. Are there 2024-2026 studies with expert designers or finished-design outcomes? None reachable (GAP 10).
11. Primary sources never opened: Gentner, Rattermann and Forbus 1993; Gick and Holyoak 1980/83; Forbus MAC/FAC; Linsey WordTree; Marshall et al.; Yu, Kraut and Kittur 2014; Goel on structure-behaviour-function. K07 depends on them.
12. Coverage of 2025-2026 LLM analogy papers is thin because the search quota ran out (critique).

## 11. Sources

[V] opened and read this session. [M] snippet, abstract only, or second-hand.

- [V] Gentner and Markman (1997) Structure mapping in analogy and similarity. https://groups.psych.northwestern.edu/gentner/papers/GentnerMarkman97.pdf ; https://doi.org/10.1037/0003-066X.52.1.45
- [M] Gentner, Rattermann and Forbus (1993) The roles of similarity in transfer. Via Gentner and Markman 1997 and Loewenstein et al. 1999 (no direct URL).
- [M] Forbus, Gentner and Law (1995) MAC/FAC. Via Gentner and Markman 1997.
- [M] Gick and Holyoak (1980, 1983); Holyoak and Koh (1987); Ross (1987, 1989). Via https://arxiv.org/abs/2302.12832 and Loewenstein et al.
- [V] Chan, Fu, Schunn, Cagan, Wood and Kotovsky (2011) On the benefits and pitfalls of analogies for innovative design. https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/2011-jmd-distancecommonness.pdf ; https://doi.org/10.1115/1.4004396
- [V] Fu, Chan, Cagan, Kotovsky, Schunn and Wood (2013) The meaning of near and far. https://joelchan.github.io/files/2013-jmd-nearfar.pdf ; https://doi.org/10.1115/1.4023158
- [V] Chan, Dow and Schunn (2014/2015) Do the best design ideas (really) come from conceptually distant sources of inspiration? https://joelchan.github.io/files/2014-desstudies-nearfar-in-press.pdf ; https://doi.org/10.1016/j.destud.2014.08.001
- [M] Chan and Schunn (2015) far analogies and concept jumps, professional team. https://doi.org/10.1111/cogs.12188 (abstract; numbers via b11, b12 in the Design Studies paper)
- [V] Loewenstein, Thompson and Gentner (1999) Analogical encoding. https://groups.psych.northwestern.edu/gentner/papers/LoewensteinThompsonGentner99.pdf ; https://doi.org/10.3758/BF03212967
- [M] Linsey, Markman and Wood (2012) WordTree; Linsey et al. (2010) fixation; Marshall, Crawford and Jensen (2016); Yu, Kraut and Kittur (2014); Tseng et al. (2008); Wilson et al. (2010); Hender (2002); Goncalves (2013). Via https://arxiv.org/abs/2602.09423 and the Chan, Dow, Schunn review.
- [V] Luo, Sarica and Wood (2021) Guiding data-driven design ideation by knowledge distance. https://arxiv.org/abs/2210.10104
- [V] Hope, Chan, Kittur and Shahaf (2017) Accelerating innovation through analogy mining. https://arxiv.org/abs/1706.05585
- [V] Ding, Srinivasan, MacNeil and Chan (2023) Fluid transformers and creative analogies. https://arxiv.org/abs/2302.12832
- [V] Webb, Holyoak and Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning in LLMs. https://arxiv.org/abs/2402.08955
- [V] Lewis and Mitchell (2024b) Evaluating the robustness of analogical reasoning in LLMs. https://arxiv.org/abs/2411.14215
- [V] Webb, Holyoak and Lu (2025) Evidence from counterfactual tasks supports emergent analogical reasoning in LLMs. https://pmc.ncbi.nlm.nih.gov/articles/PMC12107539/
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Yu and He (2024) Thought Propagation. https://arxiv.org/abs/2310.03965 (abstract-level numbers)
- [V] Bhavya, Xiong and Zhai (2022) Analogy generation by prompting LLMs. https://arxiv.org/abs/2210.04186
- [V] Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/abs/2310.12874
- [V] Yuan et al. (2023) Beneath surface similarity (SCAR). https://arxiv.org/abs/2305.12660
- [V] Sourati, Ilievski, Sommerauer and Jiang (2024) ARN. https://arxiv.org/abs/2310.00996
- [V] Wijesiriwardene et al. (2023) ANALOGICAL benchmark. https://arxiv.org/abs/2305.05050 (abstract and setup only)
- [V] Zhu and McComb / Zhu and Luo (2022/2023) Biologically inspired design concept generation using GPT. https://arxiv.org/abs/2212.13196 ; preprint https://arxiv.org/abs/2204.09714
- [V] Zhu and Luo (2022) Generative transformers for design concept generation. https://arxiv.org/abs/2211.03468
- [V] Li, Zhang, Cao and Chen (2026) Beyond input-output: design-by-analogy in human-AI collaboration (CHI 26). https://arxiv.org/abs/2602.09423
- [V] Si, Yang and Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto and Yang (2025) The ideation-execution gap. https://arxiv.org/abs/2506.20803
- [V] Cheng et al. (2026) Revisiting chain-of-thought prompting: zero-shot can be stronger than few-shot. https://arxiv.org/abs/2506.14641 (per-cell accuracies not extracted)
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948 (one sentence)
- [V] Zheng et al. (2024) Take a step back. https://arxiv.org/abs/2310.06117
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Lin (2026) Generative AI as a cognitive support tool in early-stage design ideation, PLOS One. https://doi.org/10.1371/journal.pone.0358542
- [M] SSRN preprint (2026) Does memory credit travel? Paired factorial audits of LLM-agent memory. https://doi.org/10.2139/ssrn.7160321 (abstract only)
- [M] Biomimetics (2024) Comparing analogy-based methods: bio-inspiration and engineering-domain inspiration. https://doi.org/10.3390/biomimetics9060344 (abstract only)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 4 established claims: 2 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E05.08-K10** (reworded: the sources support less). SBERT 77.9% is a good score on near analogies (not a failure); TF-IDF same-domain is one figure caption on a single seed; the human claim rests on Hope et al. citing earlier work; Lewis and Mitchell show GPT-4 accuracy drops with paraphrase, suggesting rather than proving a sentence-overlap shortcut. Corrected claim: Surface similarity pulls both humans and tools: SBERT alone scores 77.9% on near analogies in ARN but far analogies defeat models; in Hope et al.'s example the TF-IDF baseline returned same-domain items; GPT generators retrieved birds as the analogy in over 50% of cases for a flying-car task; and GPT-4 accuracy on story analogies fell when the correct story was paraphrased to remove sentence-level overlap with the source, suggesting it partly relies on that overlap.
- **E05.08-K22** (reworded: the sources support less). The '169 credited vs 10 real marginal helps' agent-memory audit is not supported by either listed source, and Si et al. measure human-reviewer ratings, not the model's own rating. Corrected claim: LLM-generated ideas lose 1.0 to 1.9 points of reviewer rating after expert execution while human ideas stay flat (Si et al.), and intrinsic self-correction lowers GPT-4 GSM8K from 95.5 to 89.0 (Huang et al.); these are indirect evidence, and no direct test of LLM self-rating of analogue usefulness was found.
- **E05.08-K06** (now single-source: only one opened source, code check).
