# Comparison and relational language: deep document

*Subfield A11.09. Key work: Gentner and Markman 1997. Why it matters: schema state S2 says "study every example: what changes, what stays". This document asks what the research says about doing that well, and whether any of it has been tested on language models. Evidence ids (a01 ... d17) refer to evidence_a-d.jsonl in this folder; claim ids (K01 ... K22) refer to claims.jsonl.*

*Honesty note up front. Almost all of the founding human data come from one lab (Gentner, Markman and students). No independent replication and no failed replication of the core alignable-difference results was found (the search was limited; see section 10). No study found tests alignable versus nonalignable differences on a language model (K15). Everything about the agent is therefore by analogy, and most of it goes to "Test first", not "Add now".*

## 1. What it is

**The core idea.** When people compare two things, they do not just count shared and unshared features. They line up the parts of one thing with the parts of the other (structural alignment). Once the two are lined up, two kinds of difference appear.

- **Alignable difference.** A difference tied to a shared structure. Example: a car has tires and a motorcycle has tires, but the car has four and the motorcycle two. Same slot, different filler.
- **Nonalignable difference.** A feature of one thing that has no counterpart in the other. Example: a car has a trunk, a motorcycle has nothing that plays that role.

**The claims of the theory** (Gentner and Markman 1997, a01-a05):

1. Similarity is like analogy. Both rest on aligning relational representations.
2. Good alignments obey parallel connectivity, one-to-one correspondence, and systematicity (prefer connected systems of relations over isolated matches) (a02).
3. Alignable differences are tied to commonalities. So similar pairs have more alignable differences than dissimilar pairs. This is the "no difference without similarity" claim (a06, a07).
4. Alignable differences weigh more in similarity and choice judgments than nonalignable ones (a04, a09, a10). This fourth claim is the weakest part (see section 5).
5. Comparison produces candidate inferences: facts connected to the matched structure carry over, unconnected facts do not (b06).
6. Comparing two cases lets the learner abstract the shared schema (analogical encoding; b11-b13).
7. Relational language (a label for the relation) helps hold on to and carry the relation (b08-b10).

**Why this matters for an agent.** S2 in our schema says to compare examples and find what changes and what stays. The human literature says four things about how to do that well: (a) compare near examples so the changes are alignable and visible, (b) make the correspondences explicit, (c) state the shared schema in words, (d) give the relation a name. The LLM literature says models are weak on far analogy and that most of the weakness is in finding the analogue, not in mapping it once it is in context (K18).

## 2. History and theories in depth

**Structure-mapping theory (Gentner 1983) and SME (Falkenhainer, Forbus, Gentner 1989).** The engine works in three stages (a02): (1) local matches between identical predicates; (2) coalesce consistent local matches into structurally consistent kernels; (3) merge kernels into one or a few maximal mappings, scored by systematicity (deep connected relational systems beat shallow isolated matches). It then projects candidate inferences from the base to the target. It usually returns two or three best interpretations. A cross-mapped pair such as earth and moon gets the relational reading over the object reading because that mapping scores higher. SME needs hand-built predicate representations. Neither the 1989 paper nor MAC/FAC was opened this session (a25, c21, c22).

**MAC/FAC (Forbus, Gentner, Law 1995).** A two-stage retrieval model: a cheap content-vector filter, then structural alignment on the survivors. It explains why people retrieve surface-similar cases more than truly analogous ones (c22, not opened). This is the human version of the retrieval bottleneck that AnaloBench finds in LLMs (d09).

**The alignable difference program (1993-1996).** Markman and Gentner ran listing and rating studies to show that difference detection depends on alignment. The 1994 paper's title is the claim: "no difference without similarity" (a06, b01). The 1996 paper tried to show the fourth claim directly with picture triads (a10). Earlier word-pair regressions had failed to support the fourth claim; the authors blamed the regression method (a11).

**Analogical encoding (Gentner, Loewenstein, Thompson 2003).** The practical branch: comparing two cases while learning beats studying them separately, with a dose-response from none through separate, compare, to guided comparison (b12).

**Relational language (Loewenstein and Gentner 2005).** Labels for relations help children map, and the label must fit the relation (b08-b10).

**Rival and critical views.**
- ACME (Holyoak and Thagard) and Copycat (Hofstadter and Mitchell) are rival or complementary mapping mechanisms (b07, c23). Copycat's letter-string domain is now the main LLM analogy test (Webb, Lewis and Mitchell, Stevenson).
- Costello and Keane (2001) disputed whether alignment is necessary. Estes and Hasson (2004) built a "critical test" using nonalignable differences and, as reported second-hand, found nonalignable differences had the larger effect on geometric stimuli (b20, d03). Not opened; do not infer more.
- Ichien, Lin, Holyoak and Lu (2024, d01, d02) say the human similarity/difference asymmetry for relational information is better explained by cognitive complexity than by alignability.

**Teaching branch.** Alfieri, Nokes-Malach and Schunn (2013) wrote a meta-analysis of case comparison. It was NOT opened in either run (b19, d16). No figure from it is used here. Richland and Zhao (2026, b17, b18) summarise the classroom evidence, with the caveat that side-by-side comparison depends on prior knowledge.

**LLM branch (2021-2026).** Word analogies (Ushio 2021, c17), SCAN (Czinczoll 2022, c18), Webb et al. 2023 (a16), counterfactual letter strings (Lewis and Mitchell, Hodel and West, Webb reply, Stevenson), story analogy (ARN, StoryAnalogy, AnaloBench), and analogical prompting (Yasunaga, Thought Propagation, contrastive CoT).

## 3. Core findings with exact numbers

Status key: **E** established (two or more sources; note most human ones are same-lab), **S** single source, **C** contested.

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Similar word pairs yield more listed differences than dissimilar pairs; the excess is alignable | Exp 1 (N=32, 40 pairs, 5 min): pairs with a difference 11.44 vs 5.88, F(1,30)=31.88; alignable 8.97 vs 3.88; nonalignable 2.47 vs 2.00 ns | Gentner and Markman 1994 (a06, b01) | E (same lab) |
| Same, between subjects, no choice of pairs | Exp 2 (N=48): 18.42 vs 13.79, t(46)=2.69; alignable 15.63 vs 11.54; nonalignable 2.79 vs 2.25 ns. Effect smaller (about 4.6 pairs vs 5.6) | 1994 (a07, b02) | E |
| Not a "narrow strategy" artefact | Top difference types: 76% of low-similarity differences vs 62% of high-similarity | 1994 (b03) | S (post hoc) |
| Picture pairs: alignable differences rise with similarity | high 3.20, medium 2.97, low 1.91; commonalities vs alignable r=.69 and .58; vs nonalignable r=-.06 | Markman and Gentner 1996 Exp 1 (a09) | S |
| Alignable differences lower rated similarity more | N=24, 8 sets: nonalignable-difference pairs rated 6.64 vs alignable 5.61, F(1,7)=10.63; interaction F(1,7)=8.19 | 1996 Exp 2 (a10) | C (8 items; word-pair regressions failed, a11; Estes and Hasson opposite, d03) |
| Complexity, not alignability, explains the similarity/difference asymmetry | N=184: relational similarity .81 vs difference .69, z=4.81; featural .84 vs .84. Stories N=129, interaction chi2(1)=4.82, p=.03 | Ichien et al. 2024 (d01, d02) | S (independent lab) |
| Side-by-side comparison improves anomaly detection | Exp 1 (N=68 analysed): single .61, low-alignable .81, high-alignable .87; high vs single d=1.86; high vs low d=0.43. Exp 2 (13 s deadline, N=48): .52/.57/.66 | Kurtz and Gentner 2013 (a12, a13) | S |
| Comparison transfers to new single items | Exp 3 (N=84): transfer .27 vs .14, d=0.86; retest .36 vs .25; old items .52 vs .37. Absolute accuracy low | Kurtz and Gentner 2013 (a14) | S |
| Normal/pathology radiograph pairs beat pathology/pathology (focal disease only) | .63 vs .54; no effect on diffuse diseases | Kok et al. 2013, second-hand (a15, a26) | S (not opened) |
| Analogical encoding in negotiation | Exp 2 (N=64): trade-off 59% vs 22%, chi2=8.26; contingent contracts 38% vs 16%. Exp 3 (N=158): contingent contract 37% none, 55% separate, 70% compare, 90% guided | Gentner, Loewenstein, Thompson 2003 (b11, b12) | S (single lab, one task) |
| Schema abstraction is the mechanism | Fully stated schema: 35% of comparers vs 8% of separate learners | 2003 (b13) | S |
| Explicit correspondence listing carries the effect | N=80 (20 per cell). Causal relevance F(3,76)=2.75; only joint+correspondence differs from control. Alignable proportion ns; schema statements p about .10 | Kurtz, Miao, Gentner 2001 (b14, b15) | S, weak |
| Relational labels help young children map | 3;8y: 72% vs 45%, F(1,84)=9.53; 4;7y cross-mapped: 65% vs 45%; 4;1y easy task 71% vs 64% ns (ceiling) | Loewenstein and Gentner 2005 (b08, b09) | S |
| The label must fit the relation | top-middle-bottom 62% vs on-in-under 40%, F(1,44)=13.31; kept after 2 days | 2005 (b10) | S |
| Alignment plus contrastive label, children 5-7 | Exp 2 (N=116): near transfer high 95% vs low 56%; label 88% vs 63%; far construction label 40% vs 21%, alignability no effect (36% vs 24%) | Zheng, Goldwater, Gentner 2025 (b16) | S (same lab) |
| Contrastive CoT lifts GPT-3.5 | GSM8K 69.2 to 79.0 (+9.8); Bamboogle 40.8 to 56.8 (+16.0); SVAMP +14.4; ASDIV +13.6; with self-consistency GSM8K 71.0 to 86.2 | Chia et al. 2023 (a23, c10; re-opened in critique) | S (one model family, no token match) |
| Every invalid-contrast type helps | GSM8K 76.0 to 80.2 across 5 types; Bamboogle 45.6 to 53.6 | Chia ablation (d13) | S |
| Analogical prompting: small gain for a strong model | GPT-3.5 GSM8K 0-shot 75.0, 0-shot CoT 75.8, 5-shot CoT 76.7, self-generated 77.8 (+1.1 over 5-shot); MATH 33.0/33.9/34.9/37.3 (+2.4) | Yasunaga et al. 2024 (a22, d10; critique corrected the row label in b27) | E for the modest size |
| Analogical prompting: big gain only for the oldest strong model | text-davinci-003 GSM8K 14.8/50.3/54.0/61.0; PaLM2 60.8/78.2/80.7/81.7. Retrieved beat or tied self-generated for davinci-002 (47 vs 48) and weaker models | Yasunaga (c09, d10) | E |
| Thought Propagation (solve analogous problems first) | Shortest path GPT-3.5 0.65 vs CoT 0.26; GPT-4 already 0.76 to 0.78 | Yu et al. 2024 (d12) | S |
| Letter-string drop under counterfactual alphabets | Humans .753; GPT-3 .488; GPT-3.5 .350; GPT-4 .452 (N=134 humans, 6,840 samples per model) | Lewis and Mitchell 2024 (a17, c04) | C |
| Drop across alphabets, with children | Latin/Greek/Symbol: GPT-4o .85/.63/.48; Llama-3.1 405B .79/.74/.27; Claude-3.5 .68/.62/.46; Gemma-2 27B .60/.39/.14; adults (n=62) .88/.91/.89; children 7-9 (n=41) .62/.66/.67 | Stevenson et al. (a19, b26, c07) | E |
| Counter-reply: counting and tools | GPT-4 alone vs humans P=8.9e-13; GPT-4 with code vs humans P=0.496; alternate-rule errors 46% GPT-4 vs 39% humans | Webb, Holyoak, Lu 2024 (c06, d04) | C |
| GPT-3 collapses on synthetic alphabet | accuracy under 0.1 on four of six modified transformations | Hodel and West (b25, d05) | E (GPT-3 only) |
| Story analogy: near good, far weak | ARN humans 97.9 near / 94.1 far; models 75.0 / 39.6; far vs near distractor 33.9. WHL GPT-3 near p=.0039, far p=.065; human vs GPT-3 OR=0.37 | Sourati et al.; Webb et al. 2023 (a16, a20, c11) | E |
| StoryAnalogy | ChatGPT about 30% on 4-way (random 25, humans 85.7); under 20% vs hard negatives | Jiayang et al. 2023 (a21) | S |
| Retrieval is the bottleneck | AnaloBench 4-way choice GPT-4 89.1/66.5/60.7 (1/10/30 sentences) vs humans 96.0/72.5/73.3; bank retrieval near random for 10 and 30 sentences | Choi et al. 2024 (d08, d09) | S |
| Answer-position bias | GPT-4 89% (16/18) correct story first vs 61% (11/18) second; humans about .78 either way | Lewis and Mitchell 2024b (b24) | S |
| Naming attributes helps matrices | GPT-3 RAVEN Center 77.2% with naming, 80.0% with decomposition; about +20 points from component split | Hu et al. 2023 (c15) | S |
| Rule induction from examples is hard | ConceptARC GPT-4 0.19 (T=0) to 0.33 with a detailed one-shot prompt (0.5 at T=0.5) | Mitchell et al. 2023 (c16) | S |
| Structure forcing helps | Self-Discover GPT-4 BBH 75 to 81, T4D 52 to 85; 10-40x fewer calls than ensembling | Zhou et al. 2024 (d15) | S (no matched control) |

**Count corrections from the critique.** Stevenson runs per model were 54 (not 55); adults 62 and children 41 (the 68/44 in a19 is an earlier version). Evidence b27 labelled 75.0 as 5-shot CoT; it is the 0-shot row. 1993 and 1994 means differ slightly (11.38 vs 11.44 pairs), probably a re-analysis. Claim K06 calls the Zheng et al. result an "adult replication"; the evidence line says children aged 5-7, so treat it as a child result.

## 4. Mechanisms and models

Written so an engineer can build each one.

### 4.1 Structural alignment (SME-style), as an algorithm

Input: two cases, each a set of typed facts: entities, attributes (one-place), relations (n-place, possibly higher-order, e.g. CAUSE(R1, R2)).

1. **Local match generation.** For every pair of facts with the same predicate, make a match hypothesis (base item, target item). Relations match only if predicates are identical. Attributes match only if identical.
2. **Structural consistency (kernels).** A match hypothesis is supported if the matches for its arguments are also hypotheses. Enforce one-to-one (no base item maps to two target items and vice versa) and parallel connectivity (if two relations match, their arguments must match).
3. **Systematicity score.** Give each match a base score; propagate score from a higher-order relation down to its arguments. A match inside a deep connected system gets more than an isolated one.
4. **Merge.** Greedily merge compatible kernels into 1 to 3 maximal global mappings.
5. **Candidate inferences.** For base facts connected to the mapping but absent in the target, propose them as inferences for the target.
6. **Read off differences.** Alignable difference = matched slot with a different filler. Nonalignable = facts in either case that are in no kernel.

For an LLM agent, the useful part is not running SME but the output format: a table of correspondences (slot, base filler, target filler), a list of unaligned items, and a list of proposed inferences. Code can check the table for one-to-one consistency (each item used once).

### 4.2 The comparison-support ladder (what actually moved humans)

Gentner, Loewenstein, Thompson (b12) give an ordered ladder, with the share reaching the contingent contract: none 37% < separate study 55% < told to compare 70% < guided analogy with definition and diagram 90%. As a prompt ladder:

- L0: give two worked cases in separate turns.
- L1: give both together, "compare these".
- L2: give both together, require a correspondence table (K07, b14-b15).
- L3: require the table, then one sentence stating the shared principle, then apply to the new item.

### 4.3 Alignability as a design variable

Kurtz and Gentner (a12) make a high-alignable standard by keeping orientation and layout identical; the low-alignable standard is the mirror image. Same information, but accuracy .87 vs .81 (d=0.43). The prompt analogue is to present the two examples in the same template: same field order, same units, so slot-to-slot correspondence is by position. Code can enforce this by rendering both cases from one schema.

### 4.3b Alignable versus nonalignable differences, as a data structure

After the table in 4.1, code splits the differences into two lists. List A (alignable): slots present in both cases with different fillers. List N (nonalignable): items in only one case. The human claim is that List A is where the decisive differences usually sit and that people list more of it for near pairs. For the agent the design question is whether to rank List A first when asking "what changes the answer". The evidence for that ranking is contested (K02), so it is a test, not a rule.

### 4.4 Relational labels

A label names the relation, not the objects. The label must fit the relation (b10). The lab's proposed mechanism: the label invites a relational encoding and keeps it available. Implementation: after comparison, code asks for a short name for the shared structure, stores it with the cases, and shows it back at test time. Not tested on LLMs (gap 6 open).

### 4.5 Retrieval as two-stage MAC/FAC

Stage 1: cheap vector similarity over case summaries (surface). Stage 2: structural match on the survivors. The LLM result (d08, d09) says retrieval from a bank is near random for long stories, so stage 1 must be fed relational summaries, not raw text. Implementation: store each case with a model-written structure summary (what relation links the parts, entity names removed) and embed that. Not tested.

### 4.6 Contrastive demonstrations

Chia et al. (a23, d13): for each demo question, show a valid chain and an invalid chain labelled as wrong. The invalid chain is made from the valid one by shuffling spans, for example incoherent objects or irrelevant language. All five corruption types helped GSM8K by 6.8 to 11.2 points over plain CoT (CoT 69.2; contrasts 76.0 to 80.2 in d13; the critique-confirmed headline is 79.0). The pair is nearly minimal, which is the human recipe for making a difference alignable. The paper does not frame it that way and does not manipulate it.

### 4.7 Self-generated analogues

Yasunaga (a22): prompt "recall 3 to 5 distinct relevant problems with solutions, then solve", in a single pass. The gain depends on the model writing correct, relevant exemplars. In their manual check of 50 correct items, 35 had relevant correct exemplars, 6 irrelevant, 9 relevant but wrong (b27). K=1 underperformed larger K. This is retrieval of analogues, not comparison of two cases: there is no alignment step.

## 5. What holds up

**Held up (within the evidence available).**
- More alignable differences for similar pairs: two experiments, two designs (within and between), two papers (1993 and 1994). Same lab. The effect shrank between subjects (a07).
- Comparison beating separate study: several measures and populations (adults in negotiation, skeleton drawings, children). Same lab, plus second-hand classroom work (b17, b18).
- Alignability helps (high vs low alignable standard): Kurtz and Gentner (d=0.43 Exp 1, d=0.53 Exp 2) and Zheng et al. 2025 (near transfer 95% vs 56%).
- LLM weakness on far analogy: ARN, StoryAnalogy, AnaloBench and the far condition of Webb et al. all agree in direction.
- LLM alphabet drop on letter strings: Lewis and Mitchell and Stevenson et al. (different groups) agree; Hodel and West agree for GPT-3.

**Failed, shrank, or contested.**
- The fourth claim (alignable differences weigh more in similarity judgments) failed in the authors' own earlier word-pair regressions (a11). The later picture design that supports it uses 8 item sets (a10). Estes and Hasson (2004) report the opposite direction for geometric stimuli (d03, second-hand). Ichien et al. (2024) say cognitive complexity explains the asymmetry (d01). Verdict: contested (K02).
- Kurtz, Miao, Gentner 2001: the predicted rise in alignable differences did not reach significance (F=1.33); weak manipulations gave no gain (b14).
- Kurtz and Gentner Exp 2: under a deadline the low-alignable standard gave no reliable gain over the target alone (a13).
- Zheng et al. Exp 1: the alignability advantage did not differ by label (p=.70); far construction showed no alignability effect (b16).
- Letter-string dispute: Lewis and Mitchell say GPT models fail counterfactuals; Webb et al. 2024 say the failure is counting and that GPT-4 with code matches humans (P=0.496). Not settled (K10, K11, K20). No fixed protocol was run; Lewis and Mitchell's protocol has no code arm and no error-type scoring (d06).
- Order bias: GPT-4 89% vs 61% by answer position; humans none (b24). Only 18 stories.
- Analogical prompting gains shrink with model strength: +1.1 on GSM8K for GPT-3.5 against 5-shot CoT, but 14.8 to 61.0 on text-davinci-003 against 0-shot.

**Moderators.**
- Prior knowledge: side-by-side helps those with some prior skill; novices did better studying separately (Rittle-Johnson 2009 as cited, b17). Hansen and Richland 2020 found side by side beat one at a time despite memory load; not opened.
- Disease type: normal/pathology pairs helped for focal, not diffuse, diseases (a15).
- Age: labels helped 3;8 and 4;7 year olds but not 4;1 on the easy task (ceiling) (b08, b09).
- Encoding: the similarity/difference asymmetry shrinks when stories are encoded one at a time (d02).
- Model strength: self-generation won only for the strongest model in the 2023 set (d10).
- Task semantics: naming attributes helped LLMs on matrices (c15).

**Interventions that worked.** Compare two cases with a correspondence listing (b14, b15); guided analogy with definition and diagram (b12); aligned presentation (a12, b16); a fitting relational label (b10, b16); contrastive valid/invalid chain demos on GPT-3.5 (a23); code execution for counting-heavy analogies (d04).

**Interventions that did not work or are unknown.** Bare "see both" or separate interpretation (b14). One-shot examples on SCAN (c18). Fine-tuning on BATS hurt SCAN (c18). Few-shot prompting degrades DeepSeek-R1 per its authors, no numbers (d14). Self-generated exemplars for models weaker than text-davinci-002 (c09).

**Gaps in the record.** No independent replication; no failed replication; Alfieri et al. 2013 unopened (b19, d16); the 1993/1994 counts, Loewenstein and Gentner 2005 and Gentner et al. 2003 were not re-opened in the critique; ARN figures not re-opened; Hansen and Richland and Kok et al. unopened.

## 6. Language models

**There is no LLM test of the central claim.** No study found asks a model to list or rate alignable versus nonalignable differences (K15, c26). The nearest are story and letter-string analogy tests and prompt methods that use comparison.

**What models do on analogy tasks.**
- Text analogies, 2023: GPT-3 matched or beat UCLA undergraduates on digit matrices (OR=1.88, p=.005), letter strings (zero-generalisation OR=1.76, p=.0007) and four-term verbal analogies. Like humans it did worse for semantically distant pairs (OR=3.24, p=.0165) (a16, b21, c02).
- Story analogies: GPT-3 reliable only on near (p=.0039), not far (p=.065); humans clearly better (OR=0.37, p=.0003). GPT-4 better (c01).
- Counterfactual letter strings: humans .753 vs GPT-3, 3.5, 4 at .488, .350, .452 (a17). Humans flat across 0 to 20 permuted letters, models decline. Different error profile: alternate-rule errors are 39% of human errors, 6% for GPT-3, 22% for GPT-4 (c04).
- Across alphabets (2024-25 models): GPT-4o .85 Latin to .48 symbol; adults flat .88 to .91 (a19, c07). Claude-3.5 and Gemma-2 were below children even on Latin.
- Musker et al. 2025: the strongest post-trained models reach human level in main conditions but differ on controls. Humans drop from about .7 to .4 on dual-attribute rules; models do not drop the same way (a18, d07).
- Narrative analogy: ARN near 75.0, far 39.6 (below the chance of 50), humans 97.9/94.1; GPT-4 mean 68.1; SBERT 42.3 (a20, c11). Adding 2, 4 or 6 demonstrations, with or without CoT, helped Llama-2, GPT-3.5 and GPT-4; exact deltas were not extracted (c12). Instructions to attend to system mappings helped somewhat (a20).
- StoryAnalogy: ChatGPT about 30% on a 4-way choice (a21).
- AnaloBench: choosing among four candidates is good for short stories and falls with length (GPT-4 89.1/66.5/60.7). Finding the analogue in a bank is near chance (d08, d09). This is the strongest evidence that retrieval, not mapping, is the weak link (K18). Long stories were written by GPT-4, and the bank experiment tested two proprietary models only.
- Position bias: GPT-4 89% vs 61% depending on answer order (b24).
- Rule induction: ConceptARC GPT-4 0.19 to 0.33 with a detailed one-shot prompt; GPT-4V worse than text (c16).

**What changed model performance, by how much.**

| Change | Effect | Source |
|---|---|---|
| Contrastive CoT (valid plus invalid chain) vs CoT, GPT-3.5 | GSM8K +9.8; Bamboogle +16.0; SVAMP +14.4; with self-consistency GSM8K +15.2 | a23, d13 |
| Analogical prompting vs 5-shot CoT, GPT-3.5 | GSM8K +1.1; MATH +2.4 | a22, d10 |
| Same, text-davinci-003 vs 5-shot CoT (54.0) | +7.0 (self-generated 61.0) | d10 |
| Code execution on shuffled-alphabet letter strings | from far below humans (P=8.9e-13) to par (P=0.496) | d04 |
| Naming attributes and splitting into components, RAVEN | Center 77.2% to 80.0%; about +20 points on multi-component tasks | c15 |
| Thought Propagation, GPT-3.5 shortest path | 0.65 vs CoT 0.26 | d12 |
| Self-Discover, GPT-4 | BBH 75 to 81; T4D 52 to 85 | d15 |
| Detailed one-shot prompt, ConceptARC GPT-4 | 0.19 to 0.33 | c16 |

**Cautions.**
- Most numbers are 2023 models. Contrastive CoT and analogical prompting are prompt-format effects that may shrink on current reasoning models (critique). The DeepSeek-R1 report says few-shot degrades it (d14), with no numbers.
- None of the prompt methods control tokens against a matched baseline. Analogical prompting uses more output tokens; Thought Propagation uses several calls; Self-Discover reports 10-40x fewer calls than ensembling but has no matched free-form control (d15). Our G7 requires equal tokens.
- The "independent source" counts for LLM claims sometimes treat benchmarks from the same group as independent.
- Chia's invalid chains are made by editing valid ones, so the pair is nearly minimal. That is the property the human literature says matters. It was not varied.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single source, [C] contested. Ids point to evidence files; claim ids in brackets.

### Add now (established)

Nothing here is a large change. S2 already says to compare examples. These items tighten it. Each has two or more sources, but the human sources are mostly one lab. Under SCHEMA section 8 rule 1, "established" needs two independent sources, so record the same-lab caveat when making the change.

1. **S2: compare examples together, in one fixed template, before extracting rules.** Render all examples from one schema (same field order, same units) and show them side by side, not as separate narrated items. [E] with same-lab caveat. a12, a13, b16, b17, b18 [K03]. Cost: no extra tokens; done in code.
2. **S2: after comparing, write one sentence of what the examples share and one of what differs in the slots.** [E] with same-lab caveat. b11, b12, b13 [K04]. Hand-coded schema statements: 35% of comparers vs 8% of separate learners (b13).
3. **O7 and S3 (far analogues): keep analogue use at impasses and in open mode, not on routine problems.** The LLM evidence agrees with the schema text: models fail far analogy (ARN far 39.6%; AnaloBench bank retrieval near random). [E] a20, a21, d08, d09, c11 [K13, K18]. No change needed; the evidence reinforces the current placement.
4. **Guard: do not trust an analogy mapping that depends on counting, indexing or alphabet order unless code did the counting.** [E] for the drop itself (a17, a19, b26, c07) [K14]. The fix (code execution) rests on one source [S] (d04); keep the guard [E] and the fix [S].

### Test first (single-source or contested)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Require an explicit correspondence table (slot, base, target) before judging or generalising; code checks one-to-one | S2 | [S] | b14, b15, d15 [K07, K22] |
| 2 | Contrastive demonstrations: show a valid and a minimally corrupted solution together | S2, S5 | [S]; may not carry to reasoning models | a23, d13, d14 [K08, K21] |
| 3 | Ask for both "what is shared" and "what differs"; check that relational differences are not lost | S2 | [S] | d01, d02 [K17] |
| 4 | Name the found structure (short relational label) and store it with the case | S2, M | [S]; humans only, mostly children | b08, b09, b10, b16 [K05, K06] |
| 5 | Self-generated analogues at S3 for algorithmic problems vs retrieved or fixed exemplars | S3, O7 | [S]; model-strength dependent | a22, d10, d12 [K09, K19] |
| 6 | Order-robust analogy answers (accept only if stable across two option orders) | G | [S] | b24 [K12] |
| 7 | Store cases with a model-written structure summary; retrieve by structure, then map in context | M, O7 | [S], by inference from AnaloBench | d08, d09 [K18] |
| 8 | Rank alignable differences first when deciding what changes the answer | S2 | [C] | a10, a11, d03, d01 [K02] |
| 9 | Compare a near example before a far one | S2, S3 | [S], by analogy from high-alignable beats low-alignable | a12, b16 |
| 10 | Code on or off for permuted-order analogies | G, tools | [C] | c06, d04, a17 [K10, K11, K20] |
| 11 | Apply S2 comparison only when the agent has some skill on the class; novices get separate study first | S0, S2 | [S], human only | b17 |

**Do not add** (consistent with SCHEMA 4b): "tell the model to think analogically" without a structure, and unstructured self-reflection. Nothing here supports them, and analogical prompting at GPT-3.5 level gives +1.1.

## 8. Concrete tests on our bench

All arms at equal total tokens (input plus output; pad the control with neutral worked-example text if the treatment uses more). At least 3 seeds, 95% intervals. A test passes only if the lower bound of the gain is above zero.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Correspondence table | ARC and ConceptARC style example sets; ARN near and far | (a) free-form "compare the examples", (b) required table of correspondences plus unaligned list, code-checked for one-to-one | pass rate on held-out item; on ARN, accuracy | +3 to +8 points; larger on far items. Zero if the model already does this implicitly |
| T2 Contrastive demos | GSM8K, Bamboogle-like, our own class set | (a) CoT demos, (b) valid plus invalid demos, (c) valid plus a "what changes" instruction without demos; on a current reasoning model and a non-reasoning model | accuracy | Non-reasoning model +5 to +10; reasoning model about 0 or negative (K21) |
| T3 Shared-schema sentence | Pairs of worked solutions then a transfer item | (a) two solutions then solve, (b) two solutions plus "state the principle", (c) one solution shown twice | transfer accuracy | b over a by 5+ points |
| T4 Alignable-difference triads | Triads (target, alignable-different option, nonalignable-different option) built from Markman and Gentner 1996 style materials in text | per prompt style: similarity rating and forced choice; extra arm that lists alignments first | direction and size of the alignable vs nonalignable effect; compare with human 6.64 vs 5.61 | Fills K15. No expected direction; the point is to learn |
| T5 Similar vs dissimilar pair listing | 40 word pairs in the style of Gentner and Markman 1994 | agent lists differences for high vs low similarity pairs | count of listed and alignable differences | Reproduces the 11.44 vs 5.88 pattern if the model aligns like humans |
| T6 Order robustness | AnaloBench T1 and ARN | single order vs two-order agreement (third order if they disagree) | accuracy at equal tokens | +2 to +6 where the model has position bias |
| T7 Relational label | Transfer items after learning a structure from examples | (a) no label, (b) fitting label, (c) non-fitting label | transfer accuracy | b minus a about +5; c at or below a if the human fit effect carries |
| T8 Retrieval by structure | AnaloBench T2 style bank plus our own case store | (a) embed raw text, (b) embed structure summaries, then in-context mapping | recall at k; final answer accuracy | b above a on 10 and 30-sentence banks; a near chance (d09) |
| T9 Self-generated vs retrieved vs fixed | algorithmic problem set, GSM8K | three exemplar sources | accuracy | self-generated gain small on strong models (about +1) |
| T10 Letter-string protocol | Lewis and Mitchell style items, permuted and symbol alphabets | code on vs off; score alternate-valid rules separately | accuracy and error type | Closes the dispute for our model; code on near human |
| T11 Near-first order | multi-example classes | near-to-far vs far-to-near vs random order at S2 | accuracy | small, maybe 0 |
| T12 Skill gate | classes with low vs mid plain pass rate | S2 compare vs separate study | accuracy by class difficulty | Compare helps mid-skill classes, may hurt very hard ones |

For every test, log per SCHEMA section 6: tokens per state, whether the comparison changed the answer, and whether it fixed or broke it.

## 9. What does not transfer, and why

- **Founding human effects are about listing and rating, not solving.** The 1994 listing task, the 1996 rating task and the triad choices have no right answer. Whether an LLM agent solves more problems by ranking alignable differences first is unknown.
- **Memory load.** Side-by-side comparison costs working memory in humans, and helps only with prior knowledge (b17). An LLM has no equivalent load, but has long-context load: AnaloBench accuracy falls with story length (89.1 to 60.7) (d08).
- **Perceptual alignment.** The alignable standard in Kurtz and Gentner is same orientation versus mirror image (a12). The text analogue (same template) may not matter to a model that reads tokens, or may matter more. Untested.
- **Children's labels.** The relational-language studies are on 3 to 7 year olds (b08-b10, b16). The mechanism there is acquiring a relation concept. An LLM already has the words, so the effect may be nil.
- **Negotiation outcome measures.** Comparing two negotiation cases (b11) measures strategy use in a new negotiation. Mapping this to code or maths items is by analogy.
- **Training-data contamination.** Letter strings and Gentner stories may be in training data (a16, b25). Success on classic items is weak evidence.
- **Few-shot demonstrations on reasoning models.** The contrastive-demo gain was measured on GPT-3.5. The R1 report says few-shot degrades reasoning models (d14).
- **Hand-built representations.** SME needs symbolic predicates. We ask the model for a correspondence table, which is a looser object.
- **Same-lab evidence.** If the lab's effects are partly specific to its materials, transfer to our items is even less certain.

## 10. Open questions

1. Does an LLM treat alignable and nonalignable differences differently in rating, choice and listing? (No study found.)
2. Does a required correspondence table beat free-form comparison at equal tokens on current models? (Closest: Self-Discover, no matched control.)
3. Do contrastive demonstrations help reasoning models, or hurt as the R1 report implies for few-shot?
4. What does the Alfieri, Nokes-Malach and Schunn (2013) meta-analysis report, and how large is the effect without same-lab studies?
5. Is there an independent replication, or a failed replication, of analogical encoding, or of "no difference without similarity"? (Search was limited by rate limits and a spent search budget.)
6. Does a relational label raise transfer for an LLM, and must it fit the relation?
7. Where does comparison hurt (low alignability, novices, high load)? Hansen and Richland and Kok et al. were not opened.
8. Can the Lewis/Mitchell versus Webb dispute be settled with one fixed protocol (code on and off, error-type scoring) on a current model?
9. Are far-analogy failures from retrieval or mapping on ARN itself? AnaloBench says retrieval; ARN was not decomposed.
10. Is the Ichien complexity account or the alignability account right for relational difference, and does it show in LLMs?
11. Do 2025-26 reasoning models still show alphabet drop and order bias?
12. Do self-generated analogues help strong 2025 models at all? (The gain was +1.1 for GPT-3.5.)

## 11. Sources

[V] opened and read this session (full text or a substantial portion); [M] snippet or citation only.

- [V] Gentner and Markman (1997) Structure mapping in analogy and similarity. http://groups.psych.northwestern.edu/gentner/papers/GentnerMarkman97.pdf (a01-a05, b05-b07)
- [V] Gentner and Markman (1994) Structural alignment in comparison: no difference without similarity. http://groups.psych.northwestern.edu/gentner/papers/GentnerMarkman94.pdf (a06-a08, b01-b03)
- [V] Markman and Gentner (1993) All differences are not created equal (CogSci). https://groups.psych.northwestern.edu/gentner/papers/MarkmanGentner93a.pdf (b04)
- [V] Markman and Gentner (1996) Commonalities and differences in similarity comparisons. http://groups.psych.northwestern.edu/gentner/papers/MarkmanGentner96.pdf (a09-a11)
- [V] Kurtz and Gentner (2013) Detecting anomalous features in complex stimuli. http://groups.psych.northwestern.edu/gentner/papers/kurtz%26Gentner_2013.pdf (a12-a15)
- [V] Gentner, Loewenstein, Thompson (2003) Learning and transfer: a general role for analogical encoding. https://groups.psych.northwestern.edu/gentner/papers/GentnerLoewensteinThompson03.pdf (b11-b13)
- [V] Kurtz, Miao, Gentner (2001) Learning by analogical bootstrapping. https://groups.psych.northwestern.edu/gentner/papers/KurtzMiaoGentner01.pdf (b14, b15)
- [V] Loewenstein and Gentner (2005) Relational language and the development of relational mapping. https://groups.psych.northwestern.edu/gentner/papers/LoewensteinGentner05.pdf (b08-b10)
- [V] Zheng, Goldwater, Gentner (2025) Structural alignment and linguistic contrast help children learn a key principle of spatial construction. https://pmc.ncbi.nlm.nih.gov/articles/PMC12741211/ (b16)
- [V] Richland and Zhao (2026) Relational reasoning and educational applications. https://pmc.ncbi.nlm.nih.gov/articles/PMC12938770/ (b17, b18)
- [V] Ichien, Lin, Holyoak, Lu (2024) Cognitive complexity explains processing asymmetry in judgments of similarity versus difference. https://cvl.psych.ucla.edu/wp-content/uploads/sites/162/2024/09/A141.Ichien-etal.CogPsych.2024.pdf (d01, d02)
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (a16, b21, b22, c01-c03)
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning in LLMs. https://arxiv.org/abs/2402.08955 (a17, c04, d06)
- [V] Lewis and Mitchell (2024) Evaluating the robustness of analogical reasoning in large language models. https://arxiv.org/abs/2411.14215 (b23, b24; table text garbled)
- [V] Hodel and West (2023) Response: Emergent analogical reasoning in large language models. https://arxiv.org/abs/2308.16118 (b25, c05, d05)
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks supports emergent analogical reasoning in LLMs. https://arxiv.org/abs/2404.13070 (c06, d04)
- [V] Stevenson, Pafford, van der Maas, Mitchell (2024/25) Can large language models generalize analogy solving like children can? https://arxiv.org/abs/2411.02348 (a19, b26, c07)
- [V] Musker, Duchnowski, Milliere, Pavlick (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803 (a18, d07; partly scrambled)
- [V] Sourati et al. (2023/24) ARN: Analogical reasoning on narratives. https://arxiv.org/abs/2310.00996 (a20, c11, c12; figures not re-opened in critique)
- [V] Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/abs/2310.12874 (a21, c13)
- [V] Choi et al. (2024) AnaloBench. https://arxiv.org/abs/2402.12370 (d08, d09)
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714 (a22, b27, b28, c08, c09, d10; table rows scrambled, corrected in critique)
- [V] Chia et al. (2023) Contrastive chain-of-thought prompting. https://arxiv.org/abs/2311.09277 (a23, c10, d13; Table 2 re-checked)
- [V] Yu et al. (2024) Thought Propagation. https://arxiv.org/abs/2310.03965 (d12)
- [V] Kim et al. (2022) Self-generated in-context learning. https://arxiv.org/abs/2206.08082 (d11)
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948 (d14; qualitative statement only)
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620 (d15)
- [V] Hu, Storks, Lewis, Chai (2023) In-context analogical reasoning with pre-trained language models. https://arxiv.org/abs/2305.17626 (c15)
- [V] Mitchell, Palmarini, Moskvichev (2023) Comparing humans, GPT-4, and GPT-4V on ConceptARC. https://arxiv.org/abs/2311.09247 (c16)
- [V] Ushio et al. (2021) BERT is to NLP what AlexNet is to CV. https://arxiv.org/abs/2105.04949 (c17; averages indicative)
- [V] Czinczoll et al. (2022) Scientific and creative analogies in pretrained language models. https://arxiv.org/abs/2211.15268 (c18)
- [V] Yuan et al. (2023) AnalogyKB. https://arxiv.org/abs/2305.05994 (c19)
- [V] Bhavya, Xiong, Zhai (2022) Analogy generation by prompting LLMs. https://arxiv.org/abs/2210.04186 (c20)
- [V] Wijesiriwardene et al. (2023) ANALOGICAL benchmark. https://arxiv.org/abs/2305.05050 (a24, c14; abstract and taxonomy only, scores not extracted)
- [M] Alfieri, Nokes-Malach, Schunn (2013) Learning through case comparisons: a meta-analytic review. https://doi.org/10.1080/00461520.2013.775712 (b19, d16; could not be opened; no numbers used)
- [M] Kok et al. (2013) radiograph comparison, cited through Kurtz and Gentner and Richland and Zhao (a26)
- [M] Estes and Hasson (2004) The importance of being nonalignable. https://doi.org/10.1037/0278-7393.30.5.1082 (b20, d03; direction only)
- [M] Costello and Keane (2001) and the reply on the necessity of alignment (b20; titles only)
- [M] Falkenhainer, Forbus, Gentner (1989) The structure-mapping engine. https://doi.org/10.1016/0004-3702(89)90077-5 (a25, c21)
- [M] Forbus, Gentner, Law (1995) MAC/FAC. https://doi.org/10.1207/s15516709cog1902_1 (c22)
- [M] Hofstadter and Mitchell (1994) The Copycat project. https://doi.org/10.1016/B978-0-387-34868-6.50027-2 (c23)
- [M] Turney (2006) Similarity of semantic relations. https://arxiv.org/abs/cs/0608100 (c24; figure recalled)
- [M] Hansen and Richland (2020), Rittle-Johnson et al. (2009), Richland and McDonough (2010), Bustamante et al. (2022): cited through Richland and Zhao (b17, b18)
- [M] Self-Discover is [V] only for its abstract-level table numbers in d15; DeepSeek-R1 only for one sentence.
