# Geneplore model: deep document

*Subfield A09.01. Written 2026-10-26 from evidence_a-d.jsonl (a01-a26, b01-b29, c01-c27, d01-d18), claims.jsonl (K01-K31) and critique.md in this folder. Evidence ids are cited in brackets. Claim ids are written K01 etc. (full form A09.01-K01). Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Numbers were re-opened by the cross-checker unless the text says otherwise.*

Reading rule for this document. "Opened" means full text or PDF text was read. "Abstract only" or "snippet" means the number is not verified. Where a claim sits on one lab, we say so.

---

## 1. What it is

Geneplore is a two-phase model of creative thought by Finke, Ward and Smith (book: *Creative Cognition*, 1992). The name joins "generate" and "explore."

- **Generate.** The mind builds mental structures that are not yet meaningful. These are called **preinventive structures**. Examples are a half-formed shape, an odd combination of parts, or a mental model with no stated purpose. [a08]
- **Explore.** The mind then interprets those structures. It looks for attributes, assigns a meaning or a function, tests what the structure could be used for, and finds its limits. [a08]
- **Product constraints** act on the cycle. They can focus the concept (narrow it) or expand it. The loop then repeats. [a08]

The key claim is a claim about order. A structure can be built first, with no goal, and its use can be found afterwards. Finke's data suggested that people cannot predict in advance what a set of parts will turn into. They find it by building and looking. [a01, a02]

The model is **descriptive and prescriptive**. It says how creative thought works and how to arrange the work. It does not limit itself to one kind of creativity. [a08] It has no formal or computational version in any source we opened. [a08]

Why it matters for our agent. Our schema already has a generate state (S3) and a test state (S4). Geneplore is the cognitive-science name for that shape, with one extra idea: the generate step may deliberately be done **without a target**, and the "what is it?" question is asked second. Whether that extra idea helps a language model is not known. No one has tested it (K25).

**Scope of this document.** The human core is small and old (1988 to 2006) and comes mostly from one lab. The language-model side is large but indirect: it covers generate-then-filter pipelines, example anchoring, and explore-by-feedback. We keep the two apart.

---

## 2. History and theories in depth

### 2.1 Origins: creative imagery (1988 to 1990)

- **Finke and Slayton 1988** is the founding experiment. Students got three random parts (shapes, lines, letters), shut their eyes and had 2 minutes to imagine them combined into a nameable figure. There was no target and no advice on how to combine. [a01]
  - The authors separate two skills: creative *combination* of parts, and creative *interpretation* of the combination. In some figures the arrangement was clever. In others the reading was clever. [a03]
  - They conclude that theories of imagery must explain how features are combined, not only how they are retrieved. [a03]
- **Finke 1990** (book *Creative Imagery*) added the **creative invention task**. We know it only second hand [a04, a22]:
  - A person picks or is given 3 of 15 object parts and mentally builds a form. They draw it.
  - They are then given one of 8 semantic categories (furniture, tools, weapons, toys and so on) and must say what the form is and how it works in that category.
  - Reported result: the most highly creative inventions came when subjects chose their own parts and the experimenter chose the category. [a04]
  - A teaching slide set says that combining parts intuitively with no use in mind worked best, and that people found more creative uses for forms they built than for forms others built. [a22] (Unsourced, no figures. Low weight.)
- The paradigm trick: fixing the *parts* and the *category* by chance means the product cannot be the result of a plan. Any inventiveness has to come from the interpretation step.

### 2.2 The model (1992)

The compact statement we have [a08]:

- Generation processes: retrieval, association, synthesis, transformation, analogical transfer.
- Exploration processes: attribute discovery and assignment, conceptual interpretation, functional inference.
- Focus or expand the concept, under product constraints.

Background from memory of the book, **not checked this session** (treat as unverified): the book also lists mental transformation and categorical reduction among generative processes, and contextual shifting, hypothesis testing and searching for limitations among exploratory ones. It names properties of good preinventive structures: novelty, ambiguity, meaningfulness, emergence, incongruity, divergence. We have no source for these lists in our folder.

### 2.3 Structured imagination (Ward, 1994 and after)

Ward's line of work shows that generation is not free. When people imagine new things, they start from a known exemplar and keep its features. He called it the **path of least resistance**. [a14, d04, d01]

- Ward 1994 itself was **not opened**. What we know comes from Marsh et al. 1996 [a14, b07] and Ward et al. 2002 [d04]. Students inventing creatures for another planet still gave them sense organs, limbs and bilateral symmetry. On a lava planet they added wings, not jet engines. Telling them to go "beyond your wildest imagination" did not remove the pattern. [a14]
- Ward et al. 2002 is the opened source with numbers (section 3). It adds a retrievability account: the easier an exemplar is to call to mind, the more often it is the base. [d01]

### 2.4 Example constraints and fixation (1993 to 1996)

A second branch asks what happens when a person sees examples before generating.

- **Smith, Ward and Schumacher 1993.** After seeing three example toys or creatures with shared features, people drew new ones that copied those features. The count of designs did not change. [a09, b01]
- **Marsh, Landau and Hicks 1996.** The copying grew with the number of examples shown (0, 1, 3, 6, 9). Total output and elaboration did not shrink. The authors compare four accounts: activation of example features, retrieval blocking, structured imagination, and category abstraction. No experiment separates all four. [a11, a13, b07]
- **Design fixation.** Jansson and Smith 1991 found copying of flawed example features in engineers. Purcell and Gero 1992 failed to replicate. Dahl and Moreau 2002 found transfer of example properties. [a16] Warnings not to copy gave mixed results. [b22, b23] (Details in section 5.)

### 2.5 The exploration side in real design (2007)

Christensen and Schunn 2007 tested preinventive structure in the field. In seven transcripts of engineering design meetings they coded 102 analogies. Bare ideas drew more distant (between-domain) analogies than physical prototypes. Their reading: once the idea has a concrete form, fixation on that form rules out far analogies. [a15, b08]

### 2.6 The first replication of the invention task (2006) and its critique

McKnight, Ormerod, Sas and Dix 2006 ran Finke's Experiments 2 and 6 in one design. [a06, a07]

- They list weaknesses of the original: effects came from cross-experiment comparisons; two judges with no published reliability; results only in book chapters; one generate-explore pass, so the *cycle* is never tested. [a07]
- They contrast two accounts. **Exploration:** a preinventive phase should raise originality and practicality. **Constraint:** originality up, practicality down. Their data fit constraint. [a07]
- Earlier physical-synthesis work: Pike 2002 found a preinventive phase gave more creative products, but participants were told about creativity and were not blind. Ishii and Miwa 2002 used LEGO Mindstorms, which limit materials. [a07]

### 2.7 Later human work and links to other theories

- **Who makes good preinventive forms.** Palmiero et al. 2015 (N=50): spatial ability predicted originality of inventions; imagery vividness predicted lower practicality. [a21]
- **Dual process.** Sowden, Pringle and Gabora 2015 map generation to fast associative (Type 1) thought and exploration to analytic (Type 2) thought. They note analytic thought can also create ideas, and that blind variation and selective retention assumes independent successive ideas, which Geneplore does not. [a17] That last point matters to us: a Geneplore cycle is path-dependent, and our S3 rule of fresh isolated attempts is closer to blind variation.
- **Tool taxonomy.** Bi, Ma and Hua 2026 sorted 57 creativity-support tools by Geneplore phase: 61.4% support generation, 38.6% exploration. Qualitative only. [a24]
- **Creative problem solving beyond output search.** A position paper argues that search in output space is not enough and one needs to change the conceptual space (Boden's exploratory versus transformational). [c26]

### 2.8 Language-model era (2023 to 2026)

No one ran the Finke task on a language model [c27, K25]. The nearest items:

- Kwon et al. (ICED 2025): GPT-4o was given the Geneplore definition and a drawing of an IKEA table and asked for preinventive structures. [a25, b29]
- Prompt2Craft (2025): an LLM builds functional objects from a parts list, with a physics simulation as the explore step. [c19]
- Large generate-then-filter idea pipelines (Si et al. 2024) and generate-and-evaluate loops (FunSearch, a 2026 neural-architecture designer). [a19, c18, c17]

---

## 3. Core findings with exact numbers

Status here follows claims.jsonl. "Single" means one lab or one paper. Numbers re-opened by the cross-checker are marked (RC).

### 3.1 Human work

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Random parts imagined into a figure give a recognizable pattern about 4 trials in 10 | Exp 1: 119/312 = 38.1%, 19 judged highly creative. N=39 students, 8 trials each. No recognizable pattern 22.4%; poor correspondence 32.7%; wrong parts 6.7%. 56 distinct pattern types. (RC) | Finke and Slayton 1988 [a01] | Single (K01) |
| Same, second experiment | Exp 2, N=70: repeated trials 124/280 = 44.3% (19 creative, 15.3% of recognizable); non-guessed 110/280 = 39.3% (15 creative). Across both: 353 recognizable, 53 highly creative. (RC) | [a02] | Single (K01) |
| Outcomes cannot be predicted from the parts | Experimenter predicted 14.3% of recognizable patterns and 1 of 19 creative ones. Subjects predicted 18.5% of their own. Prior guessing did not help: chi2(1)=1.44, ns. 10.0% when all three guesses were made. | [a01, a02] | Single (K02) |
| Trial-and-error assembly is the main strategy | 74.4% of subjects named it; they produced 18 of 19 creative patterns (self-report). | [a01] | Single |
| Preinventive phase: more original, less practical, no net gain | N=48, 288 trials. Originality 2.47 vs 2.23, F(1,46)=3.47, p<.07. Practicality 3.08 vs 3.32, F(1,46)=4.38, p=.04. Sum score: no effects. "Highly creative" (score above 7): 22 of 267 designs (8.24%), 13 preinventive and 9 control. No design reached Finke's cut-off of 8. Judge alpha .55 originality, .44 practicality, .57 creativity. | McKnight et al. 2006 [a06] (not re-opened by cross-checker) | Contested (K06) |
| Mental and physical (dough) synthesis did not differ in creativity | Same study, N=48. | [a06] | Single |
| Naming a preinventive form did not change time per use | 21.4 s (SD 18.5) for naming vs about the same; first six trials 23.8 s vs 29.6 s, ns. Time fell from first to last function (fatigue). | Preis thesis [a05] | Single, thin (K07) |
| Examples raise feature overlap, not output count (Smith) | N=94. Toys per person 2.82 vs 2.90; creatures 2.95 vs 3.08. Toy conformity .22 vs .35; creature conformity .11 vs .24. Tail .15 vs .37; antennae .05 vs .17. (RC) | Smith, Ward, Schumacher 1993 Exp 1 [a09, b01] | Established with Marsh (K03) |
| Conformity grows with number of examples (Marsh) | N about 80, 16 per group; 0, 1, 3, 6, 9 examples. Conformity .087, .137, .189, .233, .280. Critical features 4.4% to 12.1%. Creatures per person 4.4, 5.1, 4.9, 5.2, 5.4 (no loss). Tail F(4,75)=3.65; four legs F(4,75)=2.73; antennae F(4,75)=1.46, p=.224, ns. (RC) | Marsh, Landau, Hicks 1996 Exp 1 [a11, b04, b05] | Established (K03) |
| Natural bundles copied as bundles | Exp 2, N about 77: natural-bundle F(2,74)=5.18; artificial bundle F(2,74)=4.50. | [a12] | Single paper |
| A 23-minute delay did not remove conformity (Smith); a one-day delay raised it (Marsh) | Smith Exp 2 N=91; drop with delay was an order effect, F(1,87)=4.61. Marsh Exp 3 N about 75: .169 immediate vs .242 delayed, F(1,73)=4.74, p<.05. | [a10, b02, a12, b06] | Established that delay does not help (K04) |
| Telling people to be different does not remove copying | Smith Exp 3 N=80. Tail proportion: control .16, standard .34, diverge .53, conform .62. Control vs diverge t(76)=2.89. Standard vs conform t(76)=3.36. Overall F(3,76)=8.69. Control vs standard only t(76)=1.56. (RC) | [a10, b03] | Established (K04) |
| A generic "be creative" instruction barely moves reliance on Earth exemplars | N=203, Earth fruit reliance 66% control, 62% "creative" (ns), 48% "not bound" (p<.05). | Ward et al. 2002 Exp 4 [d03] | Single lab (K04 update) |
| People start from a known exemplar | Animals: 45/71 = 63% named a specific Earth animal; tools 68% (N=135); fruit 66% (N=203). Correlation of how often an item was a base with how dominant it is on a list: r about .49 (all), .68 (items listed by 5+). | Ward et al. 2002 [d01, d02, d03] | Single lab (K26) |
| Aliens keep standard features | 99% sense organ, 97% appendage, 91% bilateral symmetry. | [d01] | Single lab (K26) |
| Reliance on a known exemplar lowers originality | 3.18 vs 4.34 (animals, t(69)=2.81); 3.03 vs 4.18 (tools, t(133)=4.25); 2.50 vs 3.40 (fruit, F(1,197)=34.51). About one scale point of 7. | [d01, d02, d03] | Single lab (K26) |
| A hard constraint does not remove the default; people patch it | No-appendage constraint: handles on 23% of tools vs 73%; mouth pieces 39% vs 1%; harnesses 20% vs 3%; chi2(1,135)=33.20. Reliance 64% control vs 72% constrained. | [d02] | Single lab (K26) |
| Verbal examples + an avoid instruction raise originality; examples alone do not; visual examples fixate | N about 144, alternate-uses task. Original ideas: avoid 2.68 vs no-avoid 1.88. Examples+Avoid best, t(142)=3.51, p=.001, d=0.58. Examples without avoid: t(142)=0.97, ns. Visual examples lowered originality; avoid only restored the baseline. | George and Wiley 2020 [d05] | Single (K03, K30) |
| Analogical distance depends on form of the idea | 102 analogies in 7 transcripts: 55% within-domain, 45% between. Ideas vs prototypes: chi2(1)=7.88, p=.006. Distance by structure: chi2(2)=19.26, p<.001. Within-domain analogies shared 3.82 of 4 surface features vs 0.52, t(100)=17.21. | Christensen and Schunn 2007 [a15, b08, b09] | Single (K08) |
| Spatial ability predicts invention originality | N=50. Paper Folding vs originality of inventions r=.41; vs originality of preinventive forms r=.37. Vividness vs practicality r=-.33. R2=31.5% for invention originality. Judge ICC about .48 to .58. | Palmiero et al. 2015 [a21] | Single |
| Defixation helps closed problems more than open ones | Systematic review of 53 experiments; no pooled effect size. | Wang, Okada, Takagi 2023 [b21] | Single review (K23) |
| Exposure to many AI ideas raises human group diversity, not single-idea creativity | 800+ people; beta=0.31 (disclosed), 0.26 (undisclosed), both p=0.001. | Ashkinaze et al. 2025 [b20] | Single (K21) |

### 3.2 Language-model work

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Generate-dedupe-rank pipeline beats experts on rated novelty | Novelty human 4.84 (119 reviews), AI 5.64 (109), AI+human rerank 5.81 (109); p<.01. 49 ideas per condition. Feasibility 6.61 / 6.34 / 6.44 ns. Overall 4.68 / 4.85 ns / 5.34 (p=.04, Test 1 only). (RC) | Si, Yang, Hashimoto 2024 [a19, b10, c01] | Single (K10) |
| Over-generation saturates | 4,000 seeds per topic, about 200 (5%) non-duplicate at cosine 0.8. (RC) | [a20, b11, c02] | Established with Meincke (K09) |
| Best prompt only delays exhaustion | Cosine similarity: human group 0.243; GPT-4 base 0.377; Steve Jobs persona 0.368; HBR tools 0.387. Pool estimate 3,700 vs 4,700; repeats 13.8% vs 11.7%; gap gone by about 750-800 ideas. (RC) | Meincke, Mollick, Terwiesch 2024 [b17, b18, c13, c14] | Established (K09) |
| LLM judges rank ideas near chance | Balanced accuracy (top vs bottom 25%): expert inter-reviewer 56.1%; Claude-3.5 pairwise 53.3%; Claude direct 51.7%; GPT-4o direct 50.0%; GPT-4o pairwise 45.0%; AI Scientist reviewer 43.3%. (RC) | Si 2024 [a20, b12, c03]; also [c20, c12] | Established (K14) |
| The ideation edge does not survive execution | 43 experts, 100+ hours each. LLM ideas dropped significantly more than human ideas on novelty, excitement, effectiveness, overall (p<.05). Post-execution human vs AI gap itself was not significant ("insufficient statistical power"). (RC) | Si, Hashimoto, Yang 2025 [b13, c04] | Single (K11) |
| About a quarter of pipeline proposals were borrowed | 13 experts, 50 documents: 14.0% direct copy (7/50) plus 10.0% (5/50) = 24%; 36% counting unverified claims. Detectors missed them. The 50 include 14 exemplars. | Gupta and Pruthi 2025 [b14, b15] | Single (K12) |
| Mixed verdict on LLM novelty | See the three rows above. | [a19, b13, b14] | Contested (K13) |
| Output collapses inside and across models | 79% of queries: mean pairwise similarity over 0.8 across 50 samples (26,070 queries, 70+ models). Across models 71-82%. Min-p at temperature 2.0: 81% of pairs still above 0.7. Distinct answers in 10 samples: Claude-3.5 Sonnet 1.76; gpt-4o 2.88; gemini-2.0-pro 2.25; Llama-3.1-405B 3.20; Llama-3.2-1B 6.74; gemma-2-2b 5.66 vs gemma-2-27b 3.03. | Jiang et al. 2025/26 [c12, d17]; Zhang et al. NoveltyBench [c11] | Established (K15) |
| Temperature raises novelty and incoherence together | 36 raters, 100 stories (31 rated). Novelty beta=.308; incoherence beta=.240. Alpha .639 (novelty .547). | Peeperkorn et al. 2024 [a18] | Established with Padmakumar (K16) |
| Asking for novelty barely helps | Scale and post-training raise novelty through quality; gains plateau from OLMo-2 7B to 32B. | Padmakumar et al. 2025 [c10] | With K16 |
| Hard bans trade correctness for novelty | GPT-4 pass@1 16.1% to 11.6, 7.1, 5.2, 2.3, 2.1% over five bans. Divergent creativity 4.5% to 15.3%. Convergent creativity 16.2% to 0.0%. Constraint-following 100% to 14.4%. MCTS, self-correction, planning each traded divergent for convergent gains. | Lu et al. 2025 NeoCoder [c08, c09] | Established with CS4 (K19) |
| Story constraints reduce satisfaction | 7 to 39 constraints: about 35% drop for LLaMA-2 7B vs about 20% for Gemma-7B. | Atmakuru et al. 2024 CS4 [c21] | With K19 |
| Generate-wide-then-converge helps a little, model-dependent | GPT-4, 180 problems: self-reflection cut infeasible 9.7% (div-conv 4.3%); div-conv raised efficient by 6.5% (self-reflection 2.2%). Self-reflection did not help Claude2 or Llama2-13b; div-conv helped all. (RC) | MacGyver [c06] | Contested (K17) |
| MacGyver baseline | 1,683 problems. On 323: GPT-4 62.4%, humans 65.1%, Claude2 52.7%, GPT-3.5 40.6%, PaLM2 40.6%, Llama2-7b 35.5%. Failure modes of 200 infeasible GPT-4 solutions: wrong tool use 42.4%, goal not achieved 17.7%, unavailable tools 16.9%, spatial 10.8%, ignored constraints 9.5%. | [c05, c07] | Single benchmark |
| Fresh resample vs repair depends on class | Prompt2Craft (o4-mini, 800 images): first try 63.4%; re-prompt no feedback 85.0%; with collision feedback 75.7%; plus simulation 77.1%. Small code models (MBPP+): near-identical retries 33-68% when shown own attempt vs 2-14% blind; pass@1 penalty 6.1 points at 1.5B (p=0.006), tie at 7B. Math without tests: MATH500 55.6 to 58.0, AMC 25.0 to 32.5 with refine. EscapeBench: hints 10.30 to 5.03 with reflection. REx: 1.5x to 5x fewer calls. | [c19, d07, d11, c25, d10, d09] | Contested (K18) |
| A model anchors on its own earlier attempt; other-task examples do not hurt | Cross-task exemplars: all nine paired contrasts ns (e.g. 7B .709 / .728 / .696). | Verma 2026 preprint [d07, d08] | Single (K27) |
| Coverage by repeated sampling keeps growing | CodeContests Gemma-2B 0.02% (1 sample) to 7.1% (10,000). SWE-bench Lite 15.9% (1) to 56% (250). MATH Llama-3-8B 82.9% (100) to 98.44% (10,000), while vote/reward-model selection only 40.50% to 41.41%. | Brown et al. 2024 [d12] | Established with Si/Meincke contrast (K28) |
| External evaluator loops find new results | FunSearch cap set bound 2.2180 to 2.2184; prompts hold k=2 programs; about 1M samples. Architecture designer: full filter 455 novel models vs 220 with no novelty filter; valid rate 44.0% to peak 74.5%. | [c18, c17] | Established (K20) |
| Retrieve-compare-rewrite raises novelty by recombining popular concepts | Round 1: 88.9% substantially different, 55.6% more novel; round 2: 57.8%. Concept recombination: +7 to 10% similarity to later real papers. | SciMON [b16]; Gu et al. [a23, c15] | Single (K22) |
| Retrieval at generation widens the pool | 3.4x more unique novel ideas, at least 2.5x more top-rated (abstract-level read). | Nova [d16] | Single |
| Run-based novelty does not predict success | 3,222 scored runs, 0 rated Original; top-10 by quality intersect NS<=2: 1 idea; surprise vs quality r=-0.11. | Heuresis 2026 [d13, d14] | Single (K29) |
| Autonomous scoring loops fabricate scores | 40 confirmed across 1,628 scored runs; auditor caught 19 of 20 in one check. | [d15] | Single (K31) |
| LLMs show fixation | GPT-4 solved 5-7 of 494 red-herring walls vs 285 for humans; removing herrings lifted accuracy; 1 to 10 shots gave no consistent gain. | Naeini et al. 2023 [c24] | Single (K24) |
| LLMs beat average humans on word-distance divergent tasks | Alternate-uses originality F(1,600)=622.10, effect size 0.51 (eta squared, not d); fluency matched 6.94 vs 7.01; DAT 84.56 vs 76.95; elaboration 38.69 vs 5.45 words. | Hubert et al. 2024 [b19] | Single; measure rewards odd words (limits) |
| Experts see LLM stories as weaker | 48 stories, 10 experts; LLM stories passed 3-10 times fewer tests; professional about 84.7%. No LLM assessor correlated positively with experts. | Chakrabarty et al. 2024 [c20] | With K14 |
| No LLM run of the Finke task exists | Zero direct hits across several queries. | [c27] | Absence, not proof (K25) |

---

## 4. Mechanisms and models

This section says how each mechanism works in a form we can build. Where the source gives only a verbal account we write the simplest implementable reading and flag it as ours.

### 4.1 The Geneplore cycle as a program

```
state: structures = []   # preinventive pool
loop (budget B):
  GENERATE: make a structure from parts/context, WITHOUT stating a target use
  EXPLORE:  for each structure, assign an interpretation (what is it, what does it do)
  TEST:     check the interpretation against product constraints
  REFOCUS:  keep (focus) or widen (expand) the concept; repeat
```

Our reading. A **preinventive structure** is any intermediate object that has form but no committed purpose. In a language-model agent the candidates are:

- a partial program or data transform (a "helper" with no stated goal);
- a set of random components bound together (parts triple, grid operations, words);
- a rule-sketch with free slots.

An **interpretation** is a one-line statement of what the structure does or solves, which code can check. In Finke's task the check was a human judge. In our bench the check is code: run the structure and see which target items it solves or what category of output it produces.

### 4.2 Why undirected assembly might work (the Finke account)

Finke and Slayton found that outcomes could not be predicted from the parts, that guessing in advance did not help, and that creative products came from trial-and-error assembly. [a01, a02] The engineering reading: the space of combinations is large, a plan cannot see the value of a combination before it exists, and so building is cheaper than predicting. It is search with cheap generation and a post-hoc scorer.

Limit on this reading: it rests on 39 and 70 undergraduates, a 15-item part set weighted to simple forms, three judges, and self-reported strategy. There is no control without parts. [a01]

### 4.3 Constraint versus exploration accounts of the preinventive phase

McKnight et al. give two rival models. [a07]

- *Exploration account:* a preinventive phase gives the explorer more raw material, so both originality and practicality should rise.
- *Constraint account:* a built form narrows the set of uses, so originality rises (the form is odd) and practicality falls (the form fits few real uses).

Their data matched constraint: originality 2.47 vs 2.23, practicality 3.08 vs 3.32, no net gain. [a06] Implementation consequence: a form-first arm should be scored on two axes. A single "creative" score would hide the trade.

### 4.4 Structured imagination (path of least resistance)

Mechanism, as an algorithm [d01, d02, d03]:

1. Request: "invent a new X."
2. Retrieval picks a base exemplar by ease of recall. Easier recall gives higher selection odds (r .49 to .68).
3. The base's features are copied (99% sense organ, 97% appendage, 91% symmetry).
4. Constraints are met by *patching* the base, not by leaving it (handles 23% vs 73%).
5. Originality falls about one point on a 7-point scale for those who used a base.

Language-model analogue (ours, untested): the base is the highest-probability prototype. Sampling at temperature does not change the prototype (Hivemind: 81% of pairs above 0.7 even at min-p, temperature 2.0). [d17] The fix that worked for people was removal of the default (the "not bound by Earth fruit" instruction cut reliance from 66% to 48%). [d03] For a program that means: ban or remove the top prototype from context, not add a generic novelty request.

### 4.5 Example anchoring (conformity)

Mechanism candidates (Marsh et al.): activation of example features; retrieval blocking; structured imagination; category abstraction, where examples redefine the category of acceptable new items. [a13] The data favor an unintended-memory account over obedience:

- telling people to differ did not help (t(76)=2.89 vs control) [a10];
- telling them to conform made it worse (t(76)=3.36) [a10];
- a one-day delay increased conformity, which fits inadvertent plagiarism and not activation decay [a12];
- the recall experiment that would show what people keep from examples has not been done. [a13]

Language-model version. A model shown its own failed attempt makes near copies: 33-68% near-identical vs 2-14% blind (small code models, preprint). [d07] Cross-task examples did not matter (within 3.5 points). [d08] So the harm comes from *close* examples in context, not from context length.

**Instruction rule (K30, partly reconciling Smith/Marsh with NoveltyBench).** What happens after examples are shown depends on what the instruction says:

| Setup | Result | Source |
|---|---|---|
| Examples shown, no instruction | Feature overlap rises | [a09, a11] |
| Examples shown, "be different" | Overlap still above control | [a10] |
| Verbal examples + avoid list | Original ideas up, d=0.58 | [d05] |
| Visual examples + avoid | Back to no-example level only | [d05] |
| Earlier answers shown + "give a new one" (LLM) | Best of the diversity tricks in NoveltyBench | [c11] |
| Earlier outputs shown + "mix parts" (chatbots) | Raised scores; "try to beat" mostly failed | [d06] |

No one has run all four arms in one experiment, so this is a hypothesis.

### 4.6 The generate-filter pipeline

Si et al.'s pipeline is the best-measured Geneplore-like system. [a19, a20]

1. Generate 4,000 seed ideas per topic (one model).
2. Deduplicate with an embedding model; cosine threshold 0.8. About 5% survive.
3. Rank with a pairwise Swiss-system tournament (N=5 rounds), using a model as the judge.
4. Humans rate blind.

Observed: step 1 saturates (the generator is the bottleneck), step 3 is near chance, step 4 shows a novelty gain with no feasibility gain. Under execution the gain goes. [c02, c03, b13]

### 4.7 Explore as a loop with an external evaluator

FunSearch is the clean positive case. [c18] A frozen model proposes programs. A deterministic evaluator scores them. A database of good programs (islands) feeds back into prompts, with k=2 programs per prompt. The evaluator is code. The architecture-design loop shows the same: remove the novelty filter and distinct outputs halve (455 vs 220). [c17] Heuresis shows the risk when the scorer is reachable by the agent: 40 fabricated scores in 1,628 runs. [d15] Design rule: the evaluator lives outside the agent's write scope.

### 4.8 Stop rule for generation

Two different curves.

- *Open ideas:* distinct ideas saturate. The new-distinct rate falls with every batch. [c02, c14]
- *Checkable tasks:* coverage keeps growing roughly log-linearly with the number of samples (MATH 82.9% to 98.44% from 100 to 10,000). [d12] The gain per doubling is about constant, so the useful signal is **coverage gain per doubling versus cost of an operator call**, not the duplicate rate.

Implementable rule (ours): after the first 8 to 32 samples, fit coverage against log2(samples). Compute slope times remaining budget. If that is below the cost of firing an operator (O4, O6, O8), fire the operator.

### 4.9 Revise versus resample as a bandit

Choosing which program to refine, or whether to start fresh, is an exploration-exploitation problem. REx uses Thompson sampling over candidates and reports 1.5x to 5x fewer calls. [d10] The decision depends on the feedback signal: weak feedback and small models favour a fresh resample [d07, d09]; strong executable feedback or voting without tests favour refinement [d11, c25]. The bandit does not need to know in advance.

---

## 5. What holds up

### 5.1 Replications and their weight

| Claim | Replicated? | Verdict |
|---|---|---|
| Random parts yield recognizable patterns about 40% of the time | Two experiments in the same paper (38.1%, 44.3% and 39.3%). No independent lab found. | Single lab. |
| A preinventive phase raises creativity | McKnight 2006: originality up, practicality down, no net gain. Pike 2002: more creative products, but not blind and told about creativity. A student replication reportedly found no differences (snippet only). | Contested. The original theory's strong form is not supported; the constraint account fits better. |
| Examples cause conformity | Smith 1993 (3 experiments), Marsh 1996 (3 experiments), George and Wiley 2020 (visual examples fixate), design-fixation studies (Jansson and Smith 1991; Dahl and Moreau 2002). Purcell and Gero 1992 failed to replicate. | Established as a phenomenon. Not a pure Smith/Marsh replication by a different lab. |
| Conformity costs output count | No. Marsh 1996 found no loss of total output, elaboration or noncritical novel features. | The "examples reduce creativity" claim is not confirmed; only "examples shift content" is. |
| Delay reduces conformity | Smith: no (23 minutes). Marsh: a one-day delay raised it. | Delay does not help. |
| Path of least resistance | Ward 1994; Ward and Sifonis 1997; Ward et al. 2002 (three domains, four experiments); science fiction authors. All one lab. | Single lab despite many experiments. |
| Warnings against copying work | Failed: Jansson and Smith 1991; Viswanathan and Linsey 2013a,b; Viswanathan et al. 2014. Worked: Chrysikou and Weisberg 2005. Abstract warnings helped (Ezzat 2020). | Contested. Moderators unresolved (group vs individual; psychology vs engineering students). [b22, b23] |
| Defixation works | Review of 53 experiments: helps closed problems, no automatic gain on open ones. | Single review; no pooled effect. |

### 5.2 Boundary conditions found

- **Modality.** Verbal examples plus avoid raise originality; visual examples fixate even with avoid. [d05]
- **Instruction wording.** A generic "be creative" had no effect on reliance (62% vs 66%); a targeted release cut it to 48%. [d03]
- **Hard constraint form.** A constraint that does not remove the default gets patched, not escaped. [d02] In LLMs hard bans cut correctness hard (pass@1 16.1% to 2.1%). [c08]
- **Problem type.** Defixation helps closed, not open problems. [b21]
- **Idea maturity.** Far analogies drop once a physical prototype exists. [a15]
- **Judge reliability.** Every human creativity score here comes from judges with low agreement (alpha .44 to .57; ICC .48 to .58; novelty alpha .547). [a06, a21, a18]
- **Measure type.** The one number that looks like a replication across domains (conformity) counts planted features only; it is not an originality score. [a09]
- **The big human result is a task artifact risk.** Parts from a 15-item set weighted to simple forms, no no-parts control, one lab. [a01]

### 5.3 Interventions that worked (with size)

| Intervention | Size | Where | Source |
|---|---|---|---|
| Verbal examples + explicit avoid | d=0.58; 2.68 vs 1.88 original ideas | Humans, alternate uses | [d05] |
| "Not bound by Earth fruit" instruction | Reliance 66% to 48% | Humans | [d03] |
| Show earlier answers, ask for new ones | Best of tested diversity tricks (no number in the text) | LLMs | [c11] |
| Draft 100 ideas, then revise each bolder (CoT) | Pool 3,700 to 4,700; effect gone by about 750 | GPT-4 | [b17, b18] |
| Divergent-then-convergent prompting | +6.5% efficient (GPT-4, 180 problems) | LLM | [c06] |
| External executable evaluator + archive | New bounds (FunSearch) | LLM loop | [c18] |
| Novelty filter on outputs | 455 vs 220 distinct models | LLM loop | [c17] |
| Retrieval of prior work at generation | 3.4x more unique novel ideas (abstract-level) | LLM | [d16] |
| Reflection with a task list of failed attempts (EscapeAgent) | Hints 10.30 to 5.03 | GPT-4o | [c25] |
| Fresh resample without feedback (Prompt2Craft) | 63.4% to 85.0% | o4-mini | [c19] |
| Bandit mix of refine and resample (REx) | 1.5x to 5x fewer calls | LLM code repair | [d10] |

### 5.4 Interventions that did not work

| Intervention | Result | Source |
|---|---|---|
| Telling people to differ from examples | Overlap still above control, t(76)=2.89 | [a10] |
| 23-minute delay | No reduction | [a10, b02] |
| "Be creative" instruction | 62% vs 66% reliance, ns | [d03] |
| "Beyond your wildest imagination" | Pattern persisted | [a14] |
| Hard constraint on the base | Patched, not escaped | [d02] |
| Persona prompts (Steve Jobs) | 0.368 vs 0.377 (0.009) | [b17, c13] |
| Asking the model for novelty | Little effect; quality drops | [c10] |
| Raising temperature | Novelty up with incoherence up (beta .308 vs .240); min-p at temperature 2.0 still 81% of pairs above 0.7 | [a18, d17] |
| Paraphrasing and system prompts | Marginal for diversity | [c11] |
| LLM judge as selector | Near chance (45.0 to 53.3%) | [a20] |
| Standard reasoning scaffolds for creativity (MCTS, self-correction, planning) | Traded divergent for convergent; none raised both | [c09] |
| Self-reflection for Claude2, Llama2-13b | No benefit | [c06] |
| Few-shot examples on red-herring puzzles | No consistent gain | [c24] |
| Self-repair when feedback is weak and budget is equal | 0.83 to 1.01 of resampling | [d09] |
| Shown-own-attempt repair (small code model) | Penalty 6.1 points at 1.5B | [d07] |
| Naming a preinventive form before use generation | No time difference | [a05] |
| Few AI ideas shown to people | No effect | [b20] |

### 5.5 Where the field disagrees

- **Overlap versus distinct count.** Showing earlier outputs raises feature overlap in humans (Smith, Marsh) yet raises distinct answers in LLMs (NoveltyBench). A wording-based reconciliation exists (K30), not yet tested together. [critique]
- **Revise versus resample.** Prompt2Craft and Verma say resample; EscapeBench, Bilal and Olausson (with strong feedback) say refine. Task and feedback quality differ. [d07, d09, d11, c19, c25]
- **Novelty at ideation versus after execution.** Si 2024 shows an ideation edge; Si 2025 shows it falls more than the human baseline; Gupta and Pruthi show a quarter are copies. The post-execution human-vs-AI gap itself is not significant. [a19, b13, b14]
- **Self-reflection.** Helps GPT-4 on MacGyver (9.7%), not Claude2 or Llama2-13b. [c06]

---

## 6. Language models

### 6.1 No direct test of the Geneplore claim

No published study runs Finke's parts-to-object task or Ward's alien-creature task on a language model. No Geneplore-implementing system was found. [c27, K25] The nearest are the IKEA-hack study (7 structures generated; 49 hacks, 12 contained structures not in the AI list; label coverage only, single coder) [a25] and Prompt2Craft (parts list, physics check). [c19]

### 6.2 How models behave on open generation

- **They repeat themselves.** 79% of queries show mean pairwise similarity above 0.8 across 50 samples. Distinct answers in 10 samples: Claude-3.5 Sonnet 1.76; gpt-4o 2.88. [c12, c11] Larger models in a family are less diverse (gemma-2-2b 5.66 vs gemma-2-27b 3.03; Llama-3.2-1B 6.74 vs Llama-3.1-405B 3.20). [c11]
- **They agree with each other.** Across models, 71-82% similar. [d17]
- **Their idea pool is smaller than a group of people.** Mean cosine similarity 0.377 (GPT-4 base) vs 0.243 (human group). [b17]
- **They saturate.** About 5% of 4,000 are unique. The best prompt delays it to about 750 ideas. [a20, b18]
- **They copy their own earlier attempt.** 33-68% near-identical vs 2-14% (small code models). [d07]
- **They fixate.** GPT-4 solved 5-7 of 494 red-herring walls; humans 285. [c24]
- **They can seem novel at first read.** Rated novelty 5.64 vs 4.84 (expert human). [a19] With word-distance measures GPT-4 beats 151 humans on originality (84.56 vs 76.95 on DAT). [b19] Experts judge LLM stories to pass 3-10 times fewer craft tests. [c20] The DAT edge uses a measure that rewards odd words.
- **They fail at feasibility more than at ideas.** MacGyver: 42.4% of GPT-4's infeasible solutions came from wrong tool use. [c07] GPT-4 62.4% vs human 65.1% on solvable problems; the gap is small and no test was given. [c05, critique]

### 6.3 What changed behavior, by how much

| Lever | Effect | Verdict |
|---|---|---|
| Wide generation, dedupe, rank | Rated novelty +0.8 (4.84 to 5.64) | Ideation only; falls on execution |
| Prompt wording (CoT revise) | Pool 3,700 to 4,700 | Modest, delays exhaustion |
| Persona | 0.009 cosine | Nothing |
| Temperature up | Novelty up, incoherence up | No net gain beyond a point |
| Ask for novelty | Little | Nothing |
| Show earlier answers + ask for new | Best in NoveltyBench (no figure) | Works for distinct count |
| Show examples, no instruction | Not tested on LLM feature overlap | Unknown |
| Hard ban on technique | Divergent 4.5% to 15.3%, pass@1 16.1% to 2.1% | Big trade |
| Self-reflection | GPT-4 only, +9.7% feasible | Model dependent |
| Divergent-then-convergent | +6.5% efficient | Modest |
| Fresh resample vs repair | 85.0% vs 75.7% (Prompt2Craft); penalty 6.1 points (1.5B) | Class dependent |
| Retrieval of prior work | 3.4x unique novel ideas (abstract) | Widens the pool |
| External evaluator loop | New math bounds | Real, code-checked |
| Training scale and post-training | Raises novelty through quality; plateau 7B to 32B | Not a prompt lever |

### 6.4 Selection is the weak step

Judges do not beat chance by much. Best LLM 53.3% vs expert 56.1% and a chance level of 50%. [a20] Reward models and LLM judges align worse with humans on open prompts. [c12] Retrieval changes the verdict: a retrieval-grounded grader was stricter than an ungrounded one. [d13] No study compares a grounded novelty filter with random selection. [critique gap 10]

### 6.5 Transfer to checkable tasks is untested

Most LLM evidence is from stories, research proposals and consumer ideas that no code can check. [critique] Our scaffold targets checkable tasks. The better analogues are FunSearch, Prompt2Craft, MacGyver and the coverage curves of Brown et al. [c18, c19, c05, d12]. Those show real gains where a cheap exact scorer exists. [c18]

---

## 7. What our agent should take

Each item: schema part, status, evidence ids. Status [E] means two independent sources. Anything that rests on one lab or one paper is [S]. Anything where the sources disagree is [C].

### 7.1 Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Each S3 attempt gets a fresh context with no earlier attempt of the same problem. Prior output pulls later output toward its features, and a delay or "be different" does not undo it. (Already in v0.2; this adds support and the rule for open mode: no "be different" line as a fix.) | S3 / G4 | [E] | K03, K04; a09, a10, a11, a12, b02, b03 |
| A2 | Do not use a generic "be creative" or "be different" line as an operator. It did not change behavior in people, and asking an LLM for novelty does little. Use a targeted change instead (see Test first). | S3 / 4b | [E] | K04, K16; d03, a10, c10 |
| A3 | Do not use temperature as the novelty operator. Novelty and incoherence rise together; high-temperature decoding still leaves outputs similar. | S3 / 4b | [E] | K16, K15; a18, c10, d17 |
| A4 | The S3 stop rule for checkable classes is marginal coverage gain per doubling of samples against the cost of one operator call, not the duplicate rate. Open ideas saturate on duplicates; checkable solutions keep growing with samples. | S3 / G12 | [E] | K09, K28; d12, a20, b18, c14 |
| A5 | Code selects. Never rank candidates with a model judge or the generating model. Judges are near chance (45.0 to 53.3% vs expert 56.1%). | S7 / G5 / G8 | [E] | K14; a20, b12, c03, c20, c12 |
| A6 | The evaluator is code the agent cannot edit, and it is the sole source of a pass. Loops with an external executable evaluator find new results; removing a novelty filter halved distinct outputs. | S4 / G8 | [E] | K20; c18, c17 (with the fabricated-scores caution, d15 [S]) |
| A7 | Hard bans of an approach are for S6 impasses only, never default. They cut correctness steeply (pass@1 16.1% to 2.1%) for a gain in divergence. Fits G1 and O4's place at S6. | O4 / S6 | [E] | K19; c08, c09, c21, d02, d03 |
| A8 | Over-generation is not a free fix in open mode. Expect about 5% unique at 4,000 draws; a revise-bolder prompt delays but does not remove exhaustion. Use external structure (assigned untried directions, code-chosen seeds, other operators) rather than more draws of the same prompt. | S3 open mode | [E] | K09, K15; a20, b18, c11, c12, d17 |

### 7.2 Test first (single-source or contested)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Preinventive phase: build a form with no target, then name its use. Might raise originality; the one replication saw practicality fall and no net gain. | S3 / S4 | [C] | K06, K01, K02; a06, a01, a02 |
| T2 | Plan-first versus build-then-read. Humans could not predict what a build would yield. | S3 | [S] | K02; a01, a02 |
| T3 | Instruction wording after earlier attempts are shown: none / shown / shown + avoid / shown + recombine. | S3 / G4 | [C] | K30, K03; d05, d06, c11, a09, a11 |
| T4 | At S5, revise from failing output versus one more fresh S3 attempt versus a bandit mix, by problem class. Log similarity between consecutive attempts. | S5 | [C] | K18, K27; d07, d09, d10, d11, c19, c25 |
| T5 | Cross-task memory is safe; own-attempt text in context anchors. Keep lessons shown after the first attempt (already in schema), keep failed attempt text out of S3. | memory / S3 | [S] | K27; d07, d08 |
| T6 | Default-prototype ban: count default features in S3 candidates; ban the top prototype only when attempts collapse onto it. | S1 / S3 / O4 | [S] | K26; d01, d02, d03 |
| T7 | Prior-art lookup against the solved-problem library before counting a candidate as new. | S7 / G8 | [S] | K12, K29; b14, d13, d16 |
| T8 | Rank candidates by run results (S4) rather than model opinion; novelty at ideation does not carry to execution. | S4 / G8 | [S] | K11, K13; b13, c04, d13 |
| T9 | Archive of validated candidates (k=2) in the prompt. FunSearch used it, but our own T3/T5 finds may say it anchors. | S3 / memory | [S] | K20; c18, d07 |
| T10 | Allow far analogues at S2 and S3 while ideas are abstract; restrict to near analogues once an executable construct exists. | O7 / S2 | [S] | K08; a15, b08 |
| T11 | Feasibility self-check line versus code execution of the candidate. | S4 | [C] | K17; c06, c07 |
| T12 | Code-chosen random seeds for diversity instead of asking the model to be random. | S3 | [S] | d18, K15 |
| T13 | Surface-feature mutation in S1 to test whether a candidate set changes (fixation test). | S1 / S6 | [S] | K24; c24 |
| T14 | Checker outside the agent's write scope; log any score the checker did not produce. | G8 | [S] | K31; d15 |

### 7.3 Not to take

- Do not add a standalone "preinventive" state. No evidence supports it for an LLM. It enters only through T1.
- Do not expect operator switches to raise creativity on open tasks. [K23]
- Do not use model-judged novelty as a success measure. [K13, K14]
- Do not import the human multiplayer result (K21) into the single agent. It belongs to the planned multi-person layer.

---

## 8. Concrete tests on our bench

All arms run at equal total tokens (setup cost counted, G7). Same items, same seeds, same checker. Scoring is by code unless noted. Where a test needs a new item set, we say so.

### Test 1. Parts-to-object on code-checked functions (T1, T2)

- **Item type.** Triples of random parts (for example 3 code primitives or 3 grid operations from a fixed set). Hidden: a list of target functions the parts can compute (code verified). Build a set of 60 to 100 triples.
- **Arms.**
  - A: purpose-first. The target function is shown, then the build.
  - B: form-first. Build with no target, then name what it does, then the target is shown and the form is adapted.
  - C: build-then-read. Build with no target; code runs the structure; the model reads the output and names a use. No target shown.
  - D: plain model.
- **Metric.** Number of distinct nameable constructs per attempt whose named use is true under code. Separately: share of constructs that solve any hidden target (practicality) and share that do not match any known target (originality proxy). Report two axes, not a sum (McKnight).
- **Expected effect.** Per McKnight: more distinct constructs and lower practicality for B and C; no net gain in solved targets. We expect C to beat B. Accept a small effect; a null is informative.

### Test 2. Overlap versus distinct count in one experiment (T3)

- **Item type.** Open generation of 20 constructs (puzzle rules, tool uses) with a feature coder; plus 20 checkable puzzles.
- **Arms.** (i) no prior shown; (ii) prior shown, no instruction; (iii) prior shown + avoid; (iv) prior shown + recombine.
- **Metric.** Feature overlap with the shown set (code-computed from a feature list), distinct-candidate count (embedding cosine below 0.8), and pass rate on the checkable set.
- **Expected effect.** (ii) overlap up, distinct count flat; (iii) distinct up and overlap down; (iv) overlap up, pass rate up. Based on [a09, a11, d05, d06, c11].

### Test 3. Revise versus resample versus bandit (T4, T5)

- **Item type.** Three classes: executable test; no test with vote; open creative.
- **Arms at equal tokens.** S5 revise-from-failing-output; one more fresh S3 attempt; REx-style bandit; also an own-attempt-hidden revise (error line only).
- **Metric.** Pass rate on held-out checks; similarity between consecutive attempts (anchoring); tokens to first pass.
- **Expected effect.** Resample wins when feedback is weak (executable class on small models); revise wins with specific feedback; the bandit is at least as good as the best fixed arm. [d07, d09, d10, d11]

### Test 4. Stop rule (T-A4)

- **Item type.** Each puzzle class; 256-sample coverage curves.
- **Arms.** fixed N; stop on duplicate rate; stop on marginal coverage per doubling.
- **Metric.** Solved at equal tokens; tokens saved.
- **Expected effect.** The coverage rule solves more at equal tokens than the duplicate-rate rule on checkable classes. [d12]

### Test 5. Default-prototype ban (T6)

- **Item type.** 30 invented-category prompts (non-Earth creature, unusual tool) and 30 puzzle problems with a common default approach.
- **Arms.** plain; generic "be creative"; ban the most frequent prototype after impasse; ban at start.
- **Metric.** Share of default features per candidate (code), originality by embedding distance, and correctness for the puzzle problems.
- **Expected effect.** Ban-after-impasse lifts distinctness at a small correctness cost; ban-at-start costs correctness (as in [c08]); generic request does nothing [d03].

### Test 6. Prior-art lookup and run-based pick (T7, T8)

- **Item type.** Checkable tasks with a solved-problem library.
- **Arms.** random pick; model-ranked pick; prior-art-checked pick; run-based pick.
- **Metric.** Pass rate on held-out checks after one refinement step.
- **Expected effect.** Model-ranked is not better than random (A5). Run-based pick wins. A prior-art check helps only if the library overlaps.

### Test 7. Surface-mutation fixation test (T13)

- **Item type.** Puzzles with red-herring features; mutated copies.
- **Arms.** plain; S1 input hygiene; S1 plus mutated restatement.
- **Metric.** Share of candidate sets that change under mutation; pass rate.
- **Expected effect.** Fixation shows as an unchanged candidate set; hygiene reduces it. [c24]

### Test 8. Far versus near analogues by maturity (T10)

- **Item type.** Problems with and without a runnable partial solution.
- **Arms.** far analogue at S2/S3; near analogue only; switch by maturity (code detects a runnable construct).
- **Metric.** Pass rate; variance of outcomes.
- **Expected effect.** Far analogues raise spread and lower mean; the maturity switch captures upside early and restricts later. [a15, schema O7]

---

## 9. What does not transfer, and why

- **The human perceptual core.** Finke's task uses closed-eye mental imagery, 2 minutes, three parts. The core finding (cannot predict what will emerge) may be about working-memory limits on visual synthesis. A model can write out and run a combination at no imagery cost, so "cannot predict" may not hold, and "build then read" may not differ from "plan." Not shown either way. [a01, a03]
- **Judged creativity.** Highly creative status came from three human judges (rating 4+ of 5 plus 2 of 3 labelling it creative), with no published reliability. [a01, a07] We have code checks, not judges.
- **Conformity numbers.** They count planted features in drawings. They do not measure a loss of originality, and Marsh found no loss in output. [a09, a11] They tell us that examples shift content; they do not tell us by how much a model's solution quality changes.
- **Ward's alien creatures.** The base-exemplar effect is about retrieval by ease of recall. It may hold for LLMs, but no LLM study exists; sampling at temperature alone does not remove it. [d17]
- **The novelty-up result.** Si's ideas were judged on written proposals in NLP prompting; ideas were not executed. [a19] Our tasks are checkable, where novelty has no value unless the candidate passes.
- **Plausible but unverified: a "preinventive" structure in a model.** In humans it is a held mental image. In a model the closest thing is text the model has written. Whether a text structure behaves like an image is unknown. T1 is the first test.
- **Design fixation studies.** Engineers shown a flawed example are not models shown a failed attempt. The analogy is the Verma result, a small-model code preprint. [d07]
- **Ideation-stage idea pools.** A group of people produce a pool by independent thinkers. A single model draws from one distribution. G4 already says its samples are not independent. [b17]
- **Exposure effect on groups.** K21 concerns people exposed to AI ideas. Not for the single agent. [b20]
- **Creativity-support tool taxonomy.** Qualitative; no effect sizes. [a24]
- **fMRI result.** The serial-order study has no creativity outcome. [b27]

---

## 10. Open questions

1. Does a build-first, name-after step beat purpose-first on a language model at equal tokens, scored by code-checked use? (Nobody has run it.)
2. How are Smith/Marsh conformity and NoveltyBench's gain from showing earlier answers reconciled? Does instruction wording explain it?
3. At what marginal coverage rate should S3 stop and an operator fire, per puzzle class?
4. Revise versus resample: where is the crossover, and does a bandit mix reach it for free?
5. Does ideation-stage novelty matter at all for checkable tasks? Is there a run-based measure that predicts later success? (Surprise did not: r=-0.11.)
6. Does Ward's path of least resistance appear in LLM generation of new categories? Does banning the top prototype raise originality?
7. Which constraint form lifts originality without collapsing correctness? Only indirect evidence exists.
8. Is the McKnight result (more original, less practical) robust? One within-experiment replication plus an unverified student replication.
9. Does a retrieval-grounded novelty check beat random selection?
10. Ward 1994 has not been opened. What are its counts?
11. Is anything in the 2026 preprints (Verma, Bilal, Heuresis, Grammenos and Lubart, Illusion of Stochasticity) reproduced by an independent lab? None has been.
12. Does the Finke result about self-chosen parts plus experimenter-chosen category (a04) have an LLM analogue? We read it second hand.
13. Do larger or reasoning models behave the same? Hivemind shows larger models in a family are less diverse. [c11] Reasoning-distilled Llama shows negative alignment with high-creativity responses, not replicated in Qwen. [c22]

---

## 11. Sources

[V] = opened (full text or PDF text read this session, or the specific passage cited). [M] = abstract, snippet or second-hand report only.

### Human work

1. [V] Finke and Slayton (1988) Explorations of creative visual synthesis in mental imagery. https://link.springer.com/content/pdf/10.3758/BF03197758.pdf (also https://doi.org/10.3758/BF03197707 [M] first page only) [a01, a02, a03, b26]
2. [M] Finke (1990) Creative Imagery: Discoveries and Inventions in Visualization, via Preis thesis. https://cogsci.ucsd.edu/undergraduates/honors-program/Preis,-Anton_Final_Thesis.pdf [a04, a05] (the thesis itself is [V]; the book is second hand)
3. [M] Finke (1990) via teaching slides. https://www.slideshare.net/slideshow/creative-invention-task/2584556 [a22]
4. [V] McKnight, Ormerod, Sas and Dix (2006) As useful as a bicycle to a fish. https://escholarship.org/uc/item/697070x7 [a06, a07, a08] (opened once; a later download failed twice, so numbers are not re-checked)
5. [V] Smith, Ward and Schumacher (1993) Constraining effects of examples. https://link.springer.com/content/pdf/10.3758/BF03202751.pdf ; https://doi.org/10.3758/BF03202744 [a09, a10, b01, b02, b03]
6. [V] Marsh, Landau and Hicks (1996) How examples may (and may not) constrain creativity. https://link.springer.com/content/pdf/10.3758/BF03201091.pdf ; https://doi.org/10.3758/BF03201092 [a11, a12, a13, b04, b05, b07]. Experiments 2 and 3 for [b06] are [M] (abstract).
7. [M] Ward (1994) Structured imagination. Cognitive Psychology 27, 1-40. Second hand through Marsh et al. and Ward et al. 2002 [a14, d04].
8. [V] Ward, Patterson, Sifonis, Dodds, Saunders (2002) The role of graded category structure in imaginative thought. https://link.springer.com/content/pdf/10.3758/BF03195281.pdf [d01, d02, d03]
9. [V] Christensen and Schunn (2007) Analogical distance and preinventive structure. https://link.springer.com/content/pdf/10.3758/BF03195939.pdf [a15, a16, b08, b09]
10. [V] George and Wiley (2020) Need something different? Here's what's been done. https://link.springer.com/content/pdf/10.3758/s13421-019-01005-4.pdf [d05]
11. [V] Palmiero et al. (2015) Domain-specificity of creativity. https://pmc.ncbi.nlm.nih.gov/articles/PMC4664616 [a21] (fetch summary, not a clean PDF)
12. [V] Sowden, Pringle and Gabora (2015) The shifting sands of creative thinking. https://arxiv.org/pdf/1409.2207 [a17]
13. [V] Wang, Okada and Takagi (2023) How to effectively overcome fixation. https://www.frontiersin.org/articles/10.3389/feduc.2023.1183025/full [b21, b22, b23]
14. [V] Heinonen et al. (2016) Default mode and executive networks. https://doi.org/10.1371/journal.pone.0162234 [b27] (introduction, methods and limits only)
15. [V] Ashkinaze et al. (2025) How AI ideas affect the creativity, diversity, and evolution of human ideas. https://arxiv.org/abs/2401.13481 [b20]
16. [V] Bi, Ma and Hua (2026) A Geneplore model-based taxonomy of digital tools. https://openaccess-api.cms-conferences.org/articles/download/978-1-964867-82-3_8 [a24]
17. [M] Replication of Finke (1990) with a preinventive play condition (course project). https://creativeit.cs.colorado.edu/CreativeIT/188 [b28] (search snippet only; page returned errors)

### Language-model work

18. [V] Si, Yang and Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109 [a19, a20, b10, b11, b12, c01, c02, c03]
19. [V] Si, Hashimoto and Yang (2025) The ideation-execution gap. https://arxiv.org/abs/2506.20803 [b13, c04] (key claim confirmed in full HTML by the cross-checker)
20. [V] Gupta and Pruthi (2025) All that glitters is not novel. https://arxiv.org/abs/2502.16487 [b14, b15]
21. [V] Wang, Downey, Ji and Hope (2024) SciMON. https://arxiv.org/abs/2305.14259 [b16]
22. [V] Meincke, Mollick and Terwiesch (2024) Prompting diverse ideas. https://arxiv.org/abs/2402.01727 [b17, b18, c13, c14]
23. [V] Hubert, Awa and Zabelina (2024) AI more creative than humans on divergent thinking tasks. https://doi.org/10.1038/s41598-024-53303-w [b19]
24. [V] Mukherjee and Chang (2023) The creative frontier of generative AI. https://arxiv.org/abs/2306.03601 [b24] (position paper)
25. [M] Gu, Wang, Zhang, Li (2024/2025) LLMs can realize combinatorial creativity. https://arxiv.org/pdf/2412.14141 [a23, b25, c15, c16] (abstract and introduction only)
26. [V] Peeperkorn et al. (2024) Is temperature the creativity parameter of LLMs? https://arxiv.org/pdf/2405.00492 [a18]
27. [V] Tian et al. (2024) MacGyver. https://arxiv.org/html/2311.09682v4 [c05, c06, c07]
28. [V] Lu et al. (2025) NeoCoder, denial prompting. https://arxiv.org/abs/2407.09007 [c08, c09]
29. [V] Padmakumar et al. (2025) Measuring LLM novelty. https://arxiv.org/abs/2504.09389 [c10]
30. [V] Zhang et al. (2025) NoveltyBench. https://arxiv.org/html/2504.05228v4 [c11]
31. [V] Jiang et al. (2025/2026) Artificial Hivemind. https://arxiv.org/html/2510.22954 ; https://arxiv.org/pdf/2510.22954 [c12, d17]
32. [V] LLM as a Designer of Novel Neural Architectures (2026). https://arxiv.org/html/2601.02997v2 [c17]
33. [V] Romera-Paredes et al. (2024) FunSearch. https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/ [c18]
34. [V] Prompt2Craft (2025). https://arxiv.org/html/2512.04568v1 [c19]
35. [V] Chakrabarty et al. (2024) Art or Artifice? https://arxiv.org/abs/2309.14556 [c20]
36. [V] Atmakuru et al. (2024) CS4. https://arxiv.org/abs/2410.04197 [c21]
37. [V] Ismayilzada, Beaty et al. (2026) LLMs align with the human brain during creative thinking. https://arxiv.org/abs/2604.03480 [c22]
38. [M] Bellemare-Pepin et al. (2025) Divergent creativity in humans and LLMs. https://arxiv.org/abs/2405.13012 [c23] (abstract page only)
39. [V] Naeini et al. (2023) LLMs are fixated by red herrings. https://arxiv.org/abs/2306.11167 [c24]
40. [V] EscapeBench (2024). https://arxiv.org/abs/2412.13549 [c25]
41. [V] Creative problem solving in large language and vision models (2024). https://arxiv.org/abs/2405.01453 [c26]
42. [V] Generating preinventive structures: AI-driven creativity in product repurposing (ICED 2025). https://doi.org/10.1017/pds.2025.10207 [a25]; Kwon et al. abstract page https://codesign.berkeley.edu/papers/kwon-repurposing [M] [b29]
43. [V] Grammenos and Lubart (2026) Are eight chatbots better than one? https://www.researchsquare.com/article/rs-8718021/latest.pdf [d06] (preprint)
44. [V] Verma (2026) Try Again, Don't Look Back. https://arxiv.org/pdf/2607.26117 [d07, d08] (preprint)
45. [V] Olausson et al. (2024) Is self-repair a silver bullet for code generation? https://arxiv.org/pdf/2306.09896 [d09]
46. [V/M] Tang et al. (2024) Code repair with LLMs gives an exploration-exploitation tradeoff (REx). https://arxiv.org/pdf/2405.17503 [d10] (abstract, introduction and method outline only; per-domain tables not extracted)
47. [V] Bilal et al. (2026) Refining over resampling. https://arxiv.org/pdf/2608.05643 [d11] (preprint)
48. [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/pdf/2407.21787 [d12]
49. [V] Antoniades et al. (2026) Heuresis. https://arxiv.org/pdf/2606.25198 [d13, d14, d15] (preprint)
50. [M] Hu et al. (2024) Nova. https://arxiv.org/pdf/2410.14255 [d16] (abstract and introduction only)
51. [M] Gu et al. (2026) The illusion of stochasticity in LLMs. https://arxiv.org/pdf/2604.06543 [d18] (abstract and introduction only)
52. [M] Absence check: web searches 2026-10-26 for LLM tests of parts-to-object. [c27] Also mentioned, not opened: CREA (arXiv 2504.05306) and PMC12568592.
