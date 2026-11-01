# Computational blending: deep document

*Subfield F01.04. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K23), critique.md in this folder. Evidence ids a01-a32, b01-b27, c01-c31, d01-d18. Web search quota was gone, so forward-citation search was partial. Status marks: [E] established (3+ sources or an absence finding with 3 sources), [S] single-source, [C] contested.*

**Bottom line.** Computational blending is a small, mostly worked-example field. There is no independent replication of any result (K12 [E]). The founding programs (Shrager 1987, Divago, TCL, COINVENT) have no benchmark and no baseline. The one large LLM study (KOMBINE, 35 models) says blending is the hardest of three combining tasks, and that the failure is finding the shared abstraction, not describing the blend. Scaffolds that helped all add a named middle step plus a check, but the gains are small next to a strong one-shot prompt, and nobody has tested a blend operator on a reasoning score. For our agent: do not add a blend operator now. Run the cheap ablations in section 8 first.

## 1. What it is

Conceptual blending (Fauconnier and Turner, 1998) says new meaning comes from merging two input mental spaces into a third, the blend. A network has four kinds of space (a01):
- two **input spaces** with specific content;
- a **generic space** holding structure both inputs share;
- a **cross-space mapping** linking counterparts;
- a **blended space** that takes selected parts of both inputs (selective projection).

Emergent structure arises by three operations: composition, completion, elaboration (a01). Four network types are described: simplex, mirror, single-scope, double-scope (a03). The Buddhist monk riddle (Koestler 1964) is the stock example: blend the climbing day and descending day into one day with two monks on one path; running the blend shows they must meet (a02, a03). The theory does not say where the inputs come from (a01).

**Computational blending** means programs that do this on purpose. Four families exist:
1. **Rule and frame programs**: Shrager's view application (1987), Divago.
2. **Logic and category-theory programs**: Guhe et al. 2011, COINVENT (Eppe et al. 2018, answer set programming), Goguen-style colimits and amalgams.
3. **Typicality logic**: Lieto and Pozzato's TCL for concept combination.
4. **LLM pipelines**: PopBlends, the KOMBINE benchmark, visual-metaphor agents, and image-model work.

Why we care: our agent has a "map an analogue" operator (O7) and wants to know if a coded blend operator is worth adding. Section 7 answers that.

## 2. History and theories in depth

**Koestler (1964), bisociation.** Named forerunner of the theory (a01). Gives the monk riddle (a02). No experiment.

**Shrager (1987), view application (a05-a12).** The earliest blend program. It predates the theory. It models how a person with no instructions changes theory about a device.
- Human data: 7 CMU undergraduates figured out a programmable toy tank (BigTrak) with no instructions. All built a mostly correct theory in 30 to 45 minutes. 33 to 68 interactions each (mean 52, SD 12.9). Mean gap between interactions 27.7 s (SD 5.7). Data come from Shrager and Klahr (1986), only summarised (a05).
- Six generalisations from the protocols (a06): theory changes come when the device does something unexpected or a new part is considered; learners use the positive behaviour seen, not blame analysis; changes are sometimes non-monotonic; sizes are uneven; learners draw on outside knowledge (a clock face for turn units); changes are coherent (one change touches many aspects).
- The program (IE) has eight hand-made views: CODE.AND.STARTUP, CLEAR, SIMPLE.CODED.DEVICE, SIMPLE.PROGRAMMING, COMMAND.ARGUMENT, MODE.SHIFT, BASIC, VECTOR.COMPRESSION. Each was added when the authors saw a subject use it, so the fit is circular (a08).
- Search claim (a09): 960 successors per theory at the second view, 5,760 theories after two view applications, against about 124 million at the eighth step of single-frame edits. These are back-of-envelope counts from assumed sizes (6 views, 2+2 frames, branching 10), not measured.
- Fit (a10): IE tracked a subject for up to 6 view applications (12 interactions of about 52) with no help, and about 30 interactions when the causal analysis was supplied by hand. Views and matches were chosen by hand; it does not predict new subjects.
- Generality (a11): also used for a CD player, microwave and digital watch (simplified simulations). Assumes deterministic devices, one function per operation, cheap interaction and rich behaviour. Would fail on a costly, low-feedback system like air traffic control.
- Known failure (a12): coherent is not correct. The BASIC view on a digital watch makes IE expect a program memory the watch lacks. One anecdote; no rate.

**Divago (Pereira and Cardoso, late 1990s to 2005).** One of the first blending systems (a17, b04). Rules plus concept maps, a Logo-like instance domain, a genetic search over blends. Tested on the house-boat blend. Evaluation was by example. We only have second-hand descriptions (b04) and an abstract (a17). Not opened: Pereira 2007, the 2006 Knowledge-Based Systems paper.

**Guhe et al. 2011.** Blending in basic mathematics, built on HDTP analogy (a21). Only metadata read (47 citations). Content here is unverified.

**Category-theory line (a19, a20, a22, b09, c26).** Goguen modelled concepts as logical theories and a blend as a colimit. Diaconescu (2017) proposes 3/2-categories with partial morphisms; whether the blend should be a minimal colimit is open (a22). The COINVENT project built systems for mathematics and music. Gomez-Ramirez et al. (2021) re-derived "topological group" from continuous functions plus groups in HETS, three specifications, called "heuristic evidence"; the known answer was the target (hindsight) (b09). Amalgams from case-based reasoning plus HDTP rebuild Pegasus as one worked example (a20).

**Eppe et al. 2018 (a16, d13).** Generalisation as a search problem solved with answer set programming; blends pruned with metrics for the optimality principles. Demonstrated in mathematics and music. 87 citers on Semantic Scholar, none a re-implementation by title. Full text not reachable (403).

**Veale 2019 (a18).** "Conceptual mash-ups": a shallow, robust blend that reuses commonsense knowledge harvested by mining casual web questions. Abstract only.

**Lieto and Pozzato, TCL (a13-a15, b06-b08, c28).** A nonmonotonic description logic (ALC+TR) with probabilistic typicality inclusions. It solves the "pet fish" problem. Lieto's proxytype theory sits underneath (b08). The authors say no general method exists to assign HEAD and MODIFIER, and the final choice of creative combination is left to a human (b07).

**McCaig, DiPaola, Gabora (2016) (b23, c25).** Deep Dream and Deep Style read as visual blending; no novelty measure during generation; typicality versus novelty trade-off. Descriptive only.

**LLM era.**
- Ge and Parikh (2021): language models retrieve associations far better than ConceptNet; CLIP-guided generators draw blends better than a GAN (a23, a24, b13, b14, c08, c09).
- PopBlends (Wang et al. 2023, CHI): GPT-3 bridge finding plus scenes for pop-culture and product pairs (a25-a28, b10-b12, c01-c05).
- Peng et al. 2025 (c17-c20): blending-theory prompt for vision-language models.
- Hernandez et al. 2024 (b22, c21): "alien" combinations beyond human cognitive availability.
- Misty (Lu et al. 2025): interactive UI blending (b24, c06, c07).
- Xu et al. 2026: schema-driven visual-metaphor agents (b15, b16, c10-c12).
- KOMBINE (Schapiro et al. 2026): the large text benchmark (b17-b21, c13-c16, d10).
- Song et al. 2025 (CCPT): noun-phrase conceptual combination (d01-d03).
- Universe of Thoughts (Suzuki and Banaei-Kashani 2026): a blend-like operator on reasoning tasks (d05, d06).
- Lynn 2026 (a29) and Sato 2025 (a30, b27, c24): essays with no measured results.

**Evaluation history (b05).** Confalonieri et al. (2015) proposed Lakatosian argumentation to judge blends; the paper says there is no evidence of an implementation. Other systems (Steinbruck 2013, Vismantic 2015) are example-driven. Evaluation has always been weak.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Blending is harder than association or analogy for LLMs and humans | Valid outputs: LLM (35 models) association 59.0%, analogy 53.4%, blend 43.4%; humans (N=75) 22.1%, 32.9%, 12.8%. One model: 64.8% blend, 55.4% analogy | Schapiro 2026 (b17, c13, c14) | [S] |
| LLM failure is the generic space, not the description | Valid generic space 43.4% of attempts; given one, coherent blend 97.1% | Schapiro 2026 (b18, c13) | [S] |
| Inventive homogeneity across models | 412 of 2,070 (19.9%) invented concepts repeat 2+ properties of another model's; blend reuse of 1+ property 94.7% vs analogy 36.3%; 2+ properties 37.3% vs 2.6% (14.3x); same provider 9.3% vs different 4.1% | Schapiro 2026 (b19, c15) | [S] |
| Task abilities correlate across models | assoc vs analogy r=0.71; analogy vs blend r=0.70; blend vs assoc r=0.54 | Schapiro 2026 (b20) | [S] |
| LLM judge panel is only moderately tied to humans | ICC(2,3) 0.48 to 0.67 (n=1,023); panel majority agrees with one author 66% (60 items); 75% when unanimous (n=96) | Schapiro 2026 (c16, d10) | [S] |
| Within-model sameness | Pairwise similarity of samples 0.810 to 0.880 for five small models on open prompts; persona plus extreme temperature needed to get below 0.7 | Fu 2026 (d07) | [S] |
| Bridge finding is partly reliable (GPT-3) | Valid per bridge 56.0 / 55.3 / 58.7% (3 strategies); at least 1 good of 5: 90.0 / 96.6 / 93.3% (93.3% overall); rater agreement 0.41 Pearson | PopBlends (a25, b10, c01) | [S] |
| GPT-3 as knowledge base is uneven | Attribute accuracy 57% (2.86 of 5); adjectives 79%, activities 58%, catchphrases 35% | PopBlends (a26, c03) | [S] |
| Scenes after a bridge | At least one related scene 98.3%; product 89.1% vs pop culture 75.9% | PopBlends (a27) | [S] |
| Tool beats web search for ideation | Ideas per pair 2.03 (SD 0.84) vs 0.87 (SD 0.56), Wilcoxon p<0.001, N=10; mental demand 2.85 vs 5.80 (p=0.004) | PopBlends (a28, b12, c05) | [S] |
| Staged blend pipeline beats one strong prompt (images) | Metaphor ingenuity 2.75 plain, 3.69 strong one-shot, 4.56 full loop (N=100 raters); preferred over GPT-Image 64.44%, Banana-pro 67.11%, Midjourney 72.89%, BAGEL 76.22%; cost about 8.3k tokens, 4 min 11 s per sample | Xu 2026 (b15, b16, c11, c12) | [S] |
| Removing the diagnostic step costs most | MI 4.05 without diagnostic vs 4.56 full; 3.71 without transfer | Xu 2026 (c11) | [S] |
| Explanation step helps image combination | Midjourney mean rank 2.40 to 1.98; win rate vs experts 0.26 to 0.35; Friedman p<=0.0001; SD3 minimal gain; prompt length not the cause (514.5 vs 488.0, p=0.404) | Peng 2025 (c17, c18) | [S] |
| VLM understanding of blends | Gemini-1.5-Pro identification 73.67% precision, 81.33% recall vs average humans 53.42% / 70.33%; expert win rate on implication 78.3% vs average people 51% | Peng 2025 (c19) | [S] |
| Concept step outruns rendering | 36 of 40 combinations good; 10 of 36 still failed to render | Peng 2025 (c20) | [S] |
| Coded visual blender covers human blends | 23 of 39 (59%) reproduced; 13 of 16 misses explained (2 impossible, 6 no mapping, 5 parts unused) | Cunha 2017 (b01) | [S] |
| Good blends let raters name both inputs | pig-angel 70% vs 10%; cactus-pig 30% vs 0%; angel-cactus 40% vs 10% (5 raters per blend) | Cunha 2017 (b03) | [S] |
| TCL trivial scenarios dominate | Top trivial scenario 20.4% discarded; pet-fish right scenario at 0.138% and 0.013%; first 43 blocks inconsistent in one run | Lieto and Pozzato (a14, b06) | [S] |
| LM beats knowledge base at simile property recall | P@1000: ConceptNet 5.90 vs best LM row 66.38 (66,442 pairs); row labels uncertain | Ge and Parikh (a23, b13) | [S] |
| Higher temperature is not enough for "alien" blends | Above T=1, 85% of combinations contain a new concept; at T=3 over half have no cognitively unavailable concept; explicit search needed. Judged by GPT-4 and embeddings only | Hernandez 2024 (b22, c21) | [S] |
| Interactive blending tool, mixed satisfaction | 14 developers, 103 operations; mean 3.2/5 (SD 1.3); 44 above 3, 28 at 3, 31 below; 5 of 14 agree it expresses intent | Misty (b24, c06) | [S] |
| Diffusion blend peaks at midpoint | Ratio 0.5: BCD 0.621, MCD 0.862; averaged BCD 0.389 vs MCD 0.471 (1,000 pairs) | Matsuhira 2024 (a32, c22) | [S] |
| Noun-phrase scaffolds (GPT-4o, emergent property) | Base 40.8, CoT 42.4, spreading activation 43.8 to 45.8, oracle best-of-5 57.8, gold 58.4; completion 20.4 / 23.1 / 25.5-26.9 / oracle 38.9 (human 38.0) | Song 2025 (d02) | [S] |
| Property type is often wrong | GPT-4o 82.6% has-property, 56.4% four-way type, humans 81%; judge vs human r=0.85 (300 pairs) | Song 2025 (d03) | [S] |
| Analogue-mechanism-solution chain on reasoning | HypoArena win rate: C-UoT 19.5, CoT 18.8, OnePrompt 14.3, ToT 25.5, E-UoT 32.7; full beats no-transfer in 58.3% of comparisons | UoT 2026 (d05) | [S] |
| Judges weak at item level | Creativity r=0.708 over 27 method cells but 0.342 over 267 items; novelty 0.224 (p=0.26) | UoT (d06) | [S] |
| Decomposed judges are better | Specificity r=0.67 (75 paths); factuality balanced accuracy 85.9%, precision 0.52 on wrong relations; creative utility r about 0.55 | CREATE 2026 (d09) | [S] |
| Creative knowledge puzzles are hard | 2,061 items; GPT-5.4 9.4% to 17.8% (medium thinking) English; factual vs creative drop 6.08 to 17.21 points | CresOWLve 2026 (d04) | [S] |
| No independent replication of any blending result | 0 re-runs among 11 opened sources; KOMBINE 8 citers, CCPT 2, Xu 6, none re-run | b25, d12, d13, d17 | [E] |
| Image-blending and speculative work gives no text-reasoning evidence | Sato: no numbers; Matsuhira, Cho, Ge: image only | a30, a31, a32, c22, c24 | [E] |
| LLM judges weakly validated for blend validity | See judge rows above (K14, K19) | c16, d03, d06, d09, d10 | [E] |

## 4. Mechanisms and models

Each model below is described so an engineer can code it. "Program" means plain code; "model" means an LLM slot (SCHEMA section 1).

### 4.1 Core blend network (Fauconnier and Turner, via a01)
Data: input A, input B, generic G, mapping M, blend B*.
1. Take two inputs as lists of entities, relations, roles.
2. Find G: a structure both fit (for example "container that transforms inputs").
3. Build M: pairs of counterparts, one-to-one.
4. Project: choose which parts of A and B go to B*, and which merge.
5. Run the blend: composition (combine), completion (fill from a background frame), elaboration (simulate it forward). Emergent facts are the ones in neither input.

In KOMBINE the model fails at step 2 (43.4% valid), not at steps 3 to 5 (97.1% coherent once G is valid) (b18).

### 4.2 Shrager's view application (a07-a09)
Use when you have a current theory T and a library of stored views V.
1. Copy a view V as the base.
2. Merge T into V by matching frames of the same type. Ambiguous matches: Shrager picks at random (stated weakness). Better: rank by overlap and keep the top 2.
3. Coerce child frames to their new parent type.
4. Fill uninstantiated view slots from T.
5. Enforce one function per object per operation (constraint check).

Keep only coherent results. Search is hill climbing. Few big steps: 5,760 candidates after two steps against about 124 million for single edits (a09, assumed sizes). Add a **grounding check**, because coherent can be wrong (a12): test each slot filled from V against the real device output before keeping it.

### 4.3 Coded visual blender (Cunha et al., b01-b03)
1. Mapper: analogy mapping between part structures of A and B (6 of 16 misses came from "no such mapping").
2. Search: genetic search over which parts to swap. Fitness f(b) = mean degree to which base relations are respected, in [0,1]. Mutation 0.05 per gene, recombination 0.2 per individual, tournament size 2.
3. Output ranked blends. Reject inconsistent ones (2 of 16 misses were impossible).

Known bias: this fitness favours blends that swap few parts. Add a second criterion (both inputs recognisable, see b03) to avoid near-copies.

### 4.4 TCL typicality blend (a13, a14, b06)
1. Each concept is a set of typicality inclusions p::T(C) subset D (default properties with weights).
2. Mark one concept HEAD and one MODIFIER (by hand).
3. Build scenarios: choose subsets of properties to keep, drop inconsistent ones, prefer HEAD over MODIFIER on conflict.
4. Rank by probability. Pick not the top but a non-trivial one: the top scenario is often trivial or inconsistent (20.4% trivial, discarded).
5. Feed the result back to combine already-combined concepts.

Code form: a property table with weights, a conflict list, a head-wins rule, a trivial filter. The hard parts are weights and head assignment, both hand-set. It fails if the knowledge base gives its highest weight to the property that should be dropped (b06).

### 4.5 ASP generalisation search (Eppe et al., a16, d13)
Find the generalised input concepts by answer-set search (the generic space as a search result, not a guess), then prune blends by optimality metrics. Not read in full. Treat the design as a pointer: the generic space is something to search and score, which matches KOMBINE's finding that it is the bottleneck.

### 4.6 LLM staged pipelines
**PopBlends (a25-a28).** (1) Propose connecting concepts for a domain pair; (2) generate k=5, keep those a check or person marks valid; (3) expand scenes for the connecting concept. Result: 56.7% per draw, 93.3% best-of-5. Check for made-up facts (catchphrases 35% right).

**Xu et al. schema agents (c10).** Schema is a 7-tuple whose parts map to blending components (subject, carrier, relational invariant = generic space, violation point, emergent meaning, intent). Steps: a Schema agent extracts it from a reference; a Transfer agent keeps the invariant fixed and picks a new carrier; a Generation agent renders; a Diagnostic agent checks and backtracks across levels; retry cap 5; Generation and Diagnostic agents average 2.19 calls each (ideal 1).

**Peng et al. IEI prompt (c17).** Identify the input spaces, Explain the shared attributes, then state the Implication. Dropping the explanation step cost rank 1.98 to 2.40.

**Song et al. spreading activation (d02).** Retrieve related concepts from the LLM and/or ConceptNet, filter them against the seed concepts, repeat up to T=5 rounds (convergence 0.1), then answer from the expanded set. The filter mattered for canceled properties (55.6 to 63.3).

**Universe of Thoughts C-UoT (d05).** Pick an external analogue, extract an abstract mechanism, transfer to the target. An analogue-mechanism-solution chain.

### 4.7 A design that merges these (our synthesis, untested)
1. Program picks two inputs (or takes them from a failed attempt and a stored analogue).
2. Model proposes k generic spaces (k=3 to 5).
3. Program checks each G against each input separately (the KOMBINE failure was a G that fits one input only).
4. Model describes a blend for each surviving G and lists kept properties.
5. Program asks, per kept property, "does it still hold in the merged concept?" (the peeled-apple error).
6. A different-family judge ranks. Final selection is by running a downstream check, not by model opinion (G8).
7. Memory stores used property sets, to exclude repeats.

None of this combined design has been tested (K17, K21).

## 5. What holds up

**Held up (as much as anything does).**
- Blending is the hardest of the three combining tasks. The direction is the same for 35 LLMs and 75 humans. One source (b17), so [S].
- Added named middle steps plus a check raised outputs in three settings from three groups (K04 [E]): IEI (c17), the schema pipeline (c11), bridge-then-expand (a28). The gains are on creative or idea-count measures, not on correctness.
- Narrow, decomposed checks work as judges (r=0.85 Song; 0.67 CREATE), while whole-item creativity judges do not (0.342 per item) (K19 [E]).
- Best-of-k with a check carries much of the success: PopBlends 93.3% at k=5 vs 56.7% single; Song oracle best-of-5 +17 vs +2 to +5 for spreading activation.

**Did not hold, or unreplicated.**
- **No replication** of any blend program or LLM result (K12 [E]). Forward lists: Xu 6 citers, KOMBINE 8, CCPT 2, Eppe 87 titles. None is a re-run.
- **Founding programs have no baseline.** IE was matched to protocols by hand, with views added from the same protocols (a08, a10). TCL has no human data (a13, b07). Topological group was a hindsight target (b09).
- **A strong one-shot prompt closes much of the gap.** Xu: 2.75 to 3.69 from the prompt alone, then 4.56 from the loop. VLM judge scores are near ceiling (8.79 to 9.02 of 10) with no significance tests (b16). The authors own the benchmark, and Gemini-3-pro is generator and one judge. Not reproduced. PRISM (a different group, images) found refinement beats zero-shot by human choice 57.65%, smaller with a stronger model, and its structure score as chooser did worse than zero-shot (82.5% vs 88.5%) (d11). That is not a replication.
- **Universe of Thoughts does not support a blend operator on reasoning.** C-UoT is about equal to CoT (19.5 vs 18.8), best on one of three creative tasks (d05). Exploratory search beat it (32.7).
- **Spreading activation gain is small** (+2.4 to +5.0 points for GPT-4o) against standard errors of 0.2 to 2.0 (d02). Token cost of five rounds not reported.
- **Sampling alone does not fix sameness.** Temperature gave new combinations but not alien ones (c21); persona plus extreme temperature was needed for within-model diversity (d07). Showing earlier answers gave the most distinct paths but used extra calls (d08).

**Moderators.**
- Model strength: gains from added steps shrink with stronger models (Peng: SD3 minimal gain; PRISM: smaller with a stronger refiner).
- Pair type: KOMBINE pairs are random unrelated Wikidata entities; bridges are easier when domains are curated (PopBlends).
- Domain: product scenes 89.1% vs pop culture 75.9% (a27); catchphrases 35% vs adjectives 79% (a26).
- Task framing: blend vs analogy differ most in reuse (94.7% vs 36.3%): blending invites the same invented properties.
- Humans in KOMBINE could skip, and skips scored zero, so part of the 43.4 vs 12.8 gap is effort.

**Interventions that did not work or are unproven.** Be-creative and verbalized sampling helped little or hurt (CREATE, d08). Persona alone, temperature alone (d07). A structure score alone as chooser (d11). Interactive single-call blending: 3.2/5 satisfaction (b24).

**Ambiguous items.** Peng's text and a figure caption disagree on whether fusion or replacement mashups are easier (c19). Ge and Parikh table row labels were lost (b13). PopBlends rater agreement is 0.41 Pearson, not kappa (critique.md); the either-rater rule in the connecting-concept count inflates scores (c01).

## 6. Language models

**Text-only evidence is thin.** Almost all LLM evidence is images (K13, c31). The text studies are KOMBINE, PopBlends (GPT-3), CCPT, CREATE and UoT.

**What they do.**
- KOMBINE, 35 LLMs at T=0.9, default reasoning, one sample per item: blend 43.4% valid, analogy 53.4%, association 59.0% (b17, d10). Ranking across tasks is correlated (r=0.54 to 0.71). The best model reaches 64.8% on blends.
- The bottleneck is abstraction: valid generic space 43.4%, coherent blend given one 97.1% (b18). Invalid blends are often subtly wrong generic spaces that sound fine (yeast and bread vs photosynthesis: a gas-exchange space that fits only one input) (d10).
- Models keep parent properties that the combination cancels (peeled apple): property type right 56.4% (GPT-4o) vs 81% for humans (d03).
- Models converge: 19.9% of invented concepts repeat another model's properties; blends 94.7% vs analogy 36.3% (b19). One model repeats itself too: similarity above 0.8 across samples (d07, small models, open prompts).
- Creative knowledge puzzles: models retrieve the facts but fail to join them (missing creative connection and clue misreading dominate; hallucination is rare) (d04). Thinking helps (GPT-5.4 9.4 to 17.8% English at medium thinking). Factual vs creative drop 6.08 to 17.21 points.

**What changed the results, by how much.**

| Change | Effect | Source |
|---|---|---|
| Best-of-5 with a good/bad check | 56.7% to 93.3% (GPT-3) | a25 |
| Oracle best-of-5 (upper bound only) | +17 points over base, GPT-4o emergent property | d02 |
| Spreading activation vs CoT | +2.4 to +5.0 points | d02 |
| Explanation step in prompt | rank 2.40 to 1.98 (Midjourney) | c17 |
| Strong one-shot blend prompt | MI 2.75 to 3.69 | c11 |
| Full staged loop over strong prompt | MI 3.69 to 4.56 | c11 |
| Remove diagnostic agent | MI 4.56 to 4.05 | c11 |
| Verifier-in-loop refinement (images) | 57.65% human preference, less with stronger model | d11 |
| Analogue-mechanism-solution chain vs CoT | 19.5 vs 18.8 win rate (about equal) | d05 |
| Higher temperature | New but not alien combinations | c21 |
| Persona plus extreme temperature | similarity 0.85 down to 0.65 | d07 |
| Prior answers shown | most distinct paths, extra calls | d08 |
| Tool vs web search (humans) | ideas 0.87 to 2.03 | a28 |

**Caveats on all of it.** LLM judges are used in most 2024 to 2026 work (K14). The same model family is generator and judge in Xu (b15, c10) and part of Song (d01). Cost is rarely reported (Xu: about 8.3k tokens, 4 min 11 s per sample). Equal-token comparison is almost never done. Parallel files record that an analogy-then-solve step raised novelty at call-matched settings (A09.04-K25, A11.02-K29: 50.4 to 68.8% vs 21.6 to 37.9% across three frontier models; numbers copied, not re-derived; d15). Those measure breadth, not validity.

## 7. What our agent should take

Context: SCHEMA.md has G1-G12, states S0-S9, operators O1-O8. O7 "Map an analogue" already holds a typed mapping checked by code. The question is whether a blend step earns a place beside it (G7: every element must win at equal tokens).

### Add now (established)

| Item | Schema part | Status | Evidence | Why |
|---|---|---|---|---|
| Judge blend or combination outputs with a different model family than the generator, using narrow decomposed questions (does this property hold for this input?), plus a small human spot check. Never one holistic "is it creative?" score | G (self-check; supports G4, G8) | [E] | K14, K19; c16, d03, d06, d09, d10 | Narrow checks agree with humans at r=0.67 to 0.85; whole-item creativity only r=0.342 per item; 75% agreement even when unanimous |
| Treat every blend result as a hypothesis; do not add a blend operator on the strength of published results | G7 | [E] | K12; b25, d12, d13, d17 | No replication; evaluation by example or small panel |
| Do not cite image-blending or speculative LLM-blending papers (Matsuhira, Cho, Ge, Sato, Lynn) as support for a text operator | G7 | [E] | K13; a29, a30, a31, a32, c22, c24 | No text reasoning test |
| If a blend or analogy step is built, give it a named middle step (shared structure) and a check, and cap retries | O7 (extended), S (check) | [E] that this form beats plain prompts on creative outputs; not shown on reasoning accuracy | K04; c11, c17, a28 | Three groups. Keep as an option in O7, off by default until section 8 passes |

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence | What to test |
|---|---|---|---|---|
| Generic-space step: model proposes k generic spaces, code checks each against both inputs separately, then describe | O7 / new blend operator, step 1 | [S] | K01, K02; b17, b18 | Valid rate vs strong one-shot at equal tokens |
| Per-property consistency check ("does it still hold in the merged concept?") | O7, verifier | [S] | K16, K18; d03, d10 | Catches coherent-but-wrong blends |
| Propose k, filter with a check | G (verify) | [S] | K08; a25 | k=5 plus checker vs 1 draw, current model |
| Stored library of views or analogues seeding hypotheses (Shrager view application) | memory, O7 retrieval | [S] | K06; a05-a12 | View-seeded vs blank-slate, with a grounding check |
| Exclusion list of used property sets across blend attempts | G (diversity), memory | [S] | K03, K23; b19, d07, d08 | Distinct property sets at equal tokens |
| Explicit avoid-the-most-common-pairing rule instead of temperature | G (anti-fixation) | [S] | K10; c21 | Equal tokens, blind panel |
| Fitness of relations preserved from each input, to rank LLM blends | O7 selection | [S] | K07; b01-b03 | Rank agreement with a blind panel |
| Code-side typicality blend (head wins, trivial filter) | O7 / combination | [S] | K05; a13, a14, b06 | Against free-text combination on pet-fish items |
| Head-to-head: blend operator vs analogy-then-solve with grounding check | O7 | [S] | K20; d15 | Must beat the better-tested neighbour first |
| Blend operator on a downstream reasoning score (CresOWLve creative subset with factual control) | S (operator choice) | no study | K17; d04, d05 | Accuracy, not blend ratings |

### Design choices that follow from the evidence (for any blend step we build)
- Code selects (G5): a program holds the network structure, runs the checks and ranks; the model only fills slots.
- Search the generic space; do not trust one guess (b18, d13).
- Check each candidate generic space against each input alone (d10).
- Select by running, not by model opinion (G8).
- Keep memory out of the first attempt (existing memory rule); the used-property list appears only on the second and later blends.

## 8. Concrete tests on our bench

All arms at equal total tokens (include setup cost, G7). At least 100 items per arm where possible; fixed seeds; judge from a different family than the generator, plus a 10% blind human spot check.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Text blend items: random entity pairs (KOMBINE-style) | (a) plain blend prompt; (b) strong one-shot with the full blend recipe; (c) k generic spaces + per-input check + describe | Valid-blend rate by narrow judge | (c) beats (b) by 5+ points; (b) beats (a) by more. If (b) equals (c), stop |
| T2 | Same items | (a) 5 independent draws, pick by model; (b) 5 draws + per-property consistency check; (c) 1 long draw | Valid rate; share of pre-seeded coherent-but-wrong blends caught | (b) beats (a); catch rate above 60% |
| T3 | CresOWLve creative subset, factual subset as control | (a) plain; (b) generic-space + verifier operator at an impasse (G1: only after a failed attempt); (c) analogy-then-solve with grounding | Accuracy | (b) > (a) on creative only; no effect on factual. The main test |
| T4 | Insight-style items already on the bench (ARC and brainteaser) | (a) schema without blend; (b) schema + blend as O7 option | Pass rate at equal tokens; operator-pick rate | Small gain (about 2 points) or none; accept only if above noise |
| T5 | Blend tasks, N=10 blends per item | (a) no memory; (b) exclusion list of used properties after each blend; (c) high temperature | Distinct property sets (embedding threshold 0.674 as in b19) | (b) +20% distinct sets over (a), no loss in validity |
| T6 | Hidden-device tasks (BigTrak style, 8 to 20 views) | (a) blank slate; (b) view-seeded hypotheses with grounding check | Steps to correct theory; rate of coherent-wrong theories | (b) fewer steps; wrong-theory rate must not rise |
| T7 | Pet-fish style combination items | (a) LLM free text; (b) code typicality blend; (c) LLM + code consistency check | Consistency and non-triviality by narrow judge | (c) better than (a); (b) probably worse on coverage |
| T8 | 200 blend outputs | (a) same-family judge; (b) separate-family judge; (c) human spot check | Agreement with humans at property level | Separate family at least 0.7 Pearson |
| T9 | Same blend items with retry cap 1, 2, 3 | Retry-loop versions | Gain per extra call | Diminishing after 2 (Xu average 2.19 calls) |

## 9. What does not transfer, and why

- **Shrager's IE as a reasoning engine.** Fitted to 7 people and 8 hand-made views; random tie-breaks; only deterministic, cheap-to-probe devices (a05, a08, a11). The idea (copy a view, merge, keep coherent) transfers; the program does not.
- **Category-theory and ASP machinery (COINVENT, Eppe).** Needs formal theories as input. Our items are text. No evidence it beats LLM text blends; no reproduction (a16, a22, b09).
- **TCL probabilities.** Weights and head assignment are hand-set; reasoning is EXPTIME-complete (a13, b07). We have no typicality knowledge base to feed it.
- **Image blending results** (Peng, Xu, Matsuhira, Cho, Ge, Hernandez, PRISM, VMetaphor-Bench). Gains are in image quality and metaphor ratings, and the concept step is already strong while rendering is the bottleneck (c20). In text, the bottleneck is abstraction (b18). Images show the form of a scaffold, not its size on reasoning.
- **Human ideation gains (PopBlends).** Counts of ideas for N=10 students versus web search, not versus a plain LLM prompt, and not rated for quality (a28). A person was the filter; our agent has code.
- **GPT-3 numbers.** 2021 model. Use only for the shape (best-of-k plus check).
- **Blending theory as explanation.** It is descriptive, has no measure of which network type gives better solutions (a03), and does not say how to pick inputs (a01). It gives a vocabulary for a data structure, not a causal account.
- **Essays (Lynn, Sato).** No measured results (a29, a30).
- **Blend ratings as the target.** Our agent is scored on answers. Blend validity may not predict accuracy; nobody tested that (K17).

## 10. Open questions

1. Does an explicit generic-space step plus verifier beat a strong one-shot blend prompt at equal tokens on text, for a current model? (K01, K02, K17)
2. Does any blend operator raise accuracy on a downstream reasoning benchmark, rather than blend ratings? CresOWLve is a test bed (d04).
3. How often is a blend coherent but wrong in LLMs, and does a per-input check catch it? (K18)
4. Does the Xu staged gain (3.69 to 4.56) reproduce outside the authors, and at what token cost? (K22)
5. What do Divago, Eppe 2018 and Guhe 2011 actually show? Full texts unopened; any independent re-run unknown. (K12)
6. Does within-model sameness hold for blends, and does an exclusion list fix it at equal tokens? (K03, K23)
7. How well does a separate-family judge agree with humans on blend validity for current models? (K14, K19)
8. Is blend the right operator, or is analogy-then-solve with grounding checks enough? (K20)
9. Is the KOMBINE 43.4% sensitive to reasoning level, temperature or prompt wording? Defaults only were used (d10).
10. Does the human-model gap partly come from skipped items scoring zero? (b17)
11. Does blend validity depend on pair distance, and can the program choose better pairs (the missing input-selection step, a01)?
12. Do property-type errors (parent properties kept) occur in blends, not just noun phrases? (d03)

## 11. Sources

[V] = opened and read this session; [M] = metadata, abstract, snippet or citation only.

| Source | Mark | URL |
|---|---|---|
| Wikipedia, Conceptual blending (summarising Fauconnier and Turner 1998; Koestler 1964; computational list) | [V] | https://en.wikipedia.org/wiki/Conceptual_blending |
| Shrager (1987) Theory change via view application in instructionless learning, Machine Learning 2:247-276 | [V] | https://link.springer.com/content/pdf/10.1007/BF00058681.pdf |
| Lieto and Pozzato (2020) A description logic framework for commonsense conceptual combination (TCL), JETAI | [V] | https://arxiv.org/abs/1811.02366 |
| Lieto (2019) Heterogeneous proxytypes extended | [V] | https://arxiv.org/abs/1909.01645 |
| Eppe et al. (2018) A computational framework for conceptual blending, AI 256 | [M] | https://doi.org/10.1016/j.artint.2017.11.005 |
| Cardoso, Pereira et al. (2019) Nuts and bolts of conceptual blending: Divago | [M] | https://doi.org/10.1007/978-3-319-43610-4_5 |
| Pereira and Cardoso (2006) Experiments with free concept generation in Divago (not reachable) | [M] | https://doi.org/10.1016/j.knosys.2006.04.008 |
| Veale (2019) From conceptual mash-ups to badass blends | [M] | https://doi.org/10.1007/978-3-319-43610-4_4 |
| Amalgams, colimits and conceptual blending (2018) | [M] | https://doi.org/10.1007/978-3-319-65602-1_1 |
| Relationship between conceptual blending and analogical reasoning (2018) | [M] | https://doi.org/10.1007/978-3-319-65602-1_5 |
| Guhe et al. (2011) Computational account of conceptual blending in basic mathematics, Cogn Syst Res | [M] | https://doi.org/10.1016/j.cogsys.2011.01.004 |
| Diaconescu (2017) 3/2-institutions for conceptual blending | [V] | https://arxiv.org/abs/1708.09675 |
| Gomez-Ramirez et al. (2021) Notion of topological group | [V] | https://arxiv.org/abs/2112.02457 |
| Cunha, Martins, Machado et al. (2017) A pig, an angel and a cactus walk into a blender | [V] | https://arxiv.org/abs/1706.09076 |
| McCaig, DiPaola, Gabora (2016) Deep convolutional networks as models of blending | [V] | https://arxiv.org/abs/1610.02478 |
| Ge and Parikh (2021) Visual conceptual blending with large-scale language and vision models | [V] | https://arxiv.org/abs/2106.14127 |
| Wang et al. (2023) PopBlends, CHI | [V] | https://arxiv.org/abs/2111.04920 |
| Peng et al. (2025) Probing and inducing combinational creativity in VLMs | [V] | https://arxiv.org/abs/2504.13120 |
| Hernandez et al. (2024) Alien recombination | [V] | https://arxiv.org/abs/2411.11494 |
| Matsuhira et al. (2024) Conceptual blending of a diffusion model | [V] | https://arxiv.org/abs/2411.03595 |
| Cho et al. (2025) IT-Blender | [V] | https://arxiv.org/abs/2506.24085 |
| Lu et al. (2025) Misty | [V] | https://arxiv.org/abs/2409.13900 |
| Xu et al. (2026) Beyond pixels: visual metaphor transfer | [V] | https://arxiv.org/abs/2602.01335 |
| Schapiro et al. (2026) Measuring combinatorial creativity (KOMBINE) | [V] | https://arxiv.org/abs/2509.21043 |
| Song et al. (2025) Is a peeled apple still red? (CCPT) | [V] | https://arxiv.org/abs/2502.06086 |
| Ismayilzada et al. (2026) CresOWLve | [V] | https://arxiv.org/abs/2604.03374 |
| Suzuki and Banaei-Kashani (2026) Universe of Thoughts | [V] | https://arxiv.org/abs/2511.20471 |
| Fu et al. (2026) Beyond the Hivemind | [V] | https://arxiv.org/abs/2608.02618 |
| Wadhwa et al. (2026) CREATE | [V] | https://arxiv.org/abs/2603.09970 |
| Zeisler et al. (2026) PRISM | [V] | https://arxiv.org/abs/2610.01383 |
| Donvito and Lieto (2026) Minimal Cognitive Grid | [V] | https://arxiv.org/abs/2605.01359 |
| Schapiro et al. (2026) DRAT | [V] | https://arxiv.org/abs/2605.13450 |
| Chen et al. (2026) VMetaphor-Bench | [V] | https://arxiv.org/abs/2609.02502 |
| Lynn (2026) Conceptual blending in humans and language models, Frontiers in Psychology | [V] | https://doi.org/10.3389/fpsyg.2026.1849083 |
| Sato (2025) The way we prompt | [V] | https://arxiv.org/abs/2505.10948 |
| Semantic Scholar citation lists (Xu, KOMBINE, CCPT, Eppe) | [V] | https://api.semanticscholar.org/graph/v1/paper/arXiv:2602.01335/citations |
| Sibling files A09.04, A11.02, C10.03, C04.03 claims.jsonl (numbers copied, not re-derived) | [V] | C:/Users/User/Desktop/AGI/research_notes/thinking_sciences/A09_creative_cognition/subfields/04_conceptual_combination/claims.jsonl |

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 5 established claims: 4 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F01.04-K04** (number corrected). Song et al. (CCPT, GPT-4o, emergent property induction): Base 40.8, CoT 42.4, SA(LLM) 43.8, SA(ConceptNet) 45.8, SA(both) 45.2, oracle best-of-5 57.8, so spreading activation is +1.4 to +3.4 over CoT (+3.0 to +5.0 over base); the stated +2.4 to +5.0 over CoT matches neither. Other figures (IEI 2.40 to 1.98 and 0.26 to 0.35; MI 2.75/3.69/4.56 with N=100; PopBlends 0.87 to 2.03; PRISM 57.65%) check out. Corrected claim: Scaffolds that improved LLM blending outputs add a named middle step plus a check: explanation/shared-attribute step (IEI, Midjourney mean rank 2.40 to 1.98; win rate vs experts 0.26 to 0.35); generic-space-invariant transfer with diagnostic retry (mean MI 2.75 plain, 3.69 strong one-shot prompt, 4.56 full loop; N=100 raters); bridge-then-expand (ideas per pair 0.87 to 2.03). A strong one-shot prompt closes much of the gap. Gains of added steps are small or model-dependent: spreading activation on GPT-4o gave +1.4 to +3.4 points over CoT (+3.0 to +5.0 over base) on emergent property induction, while an oracle best-of-5 gave +17 over base; a structure-score refinement loop (PRISM) won human forced choice 57.65%, with smaller gains with a stronger model.
