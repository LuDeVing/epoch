# Conceptual blending: deep document

*Subfield C04.08. Merging two input spaces. Key works: Fauconnier and Turner. Evidence ids (a01 to d20) and claim ids (C04.08-K01 to K26) refer to the files in this folder. Numbers were re-checked against full text where critique.md says so. The founding Fauconnier and Turner papers were not opened; theory is described from opened secondary sources and Turner's own later essay.*

## 1. What it is

Conceptual blending is a theory of how people combine two mental scenes into a third one. Fauconnier and Turner describe a network of four mental spaces.

- Input space 1 and input space 2: the two things being combined.
- Generic space: the low-level structure both inputs share. It lets the inputs be lined up.
- Blend space: a new space that takes selected parts of both inputs. It can grow structure that neither input has. This is called emergent structure.

Standard example: "This surgeon is a butcher." The inputs are surgery and butchery. The blend carries the surgeon's goal and the butcher's crude means, and gives the new idea of incompetence. Another standard example is the monk riddle: put both journeys on one day and the two monks must meet.

Emergent structure comes by three routes: composition (put parts side by side), completion (fill a known pattern), and elaboration (run the blend and see what follows) (a06).

Why this subfield matters for our agent. Our schema has operator O7 "Map an analogue". Blending adds a different move: take two ideas, name what they share, keep selected parts of each, and run the result. In a stuck state this would be a way to merge two failed approaches. The honest finding of this document is that nobody has measured blending as a reasoning operator. What exists is human lab work on conceptual combination, a few computational systems tested on hand-built examples, and since 2021 LLM studies of creative output. The best new study (Schapiro et al. 2026) shows where LLMs break: finding a valid generic space.

## 2. History and theories in depth

**Roots.** Blending grew from mental space theory (Fauconnier, 1985) and from metaphor research that used two spaces, source and target. Blending added two things to that two-space picture: a generic space and a blend that can hold its own emergent structure (a01). The main paper is Fauconnier and Turner (1998), Cognitive Science 22(2):133-187. Development began about 1993 (a06). The book "The Way We Think" (2002) is the full statement. Neither was opened here.

**Governing principles.** In one account there are five optimality constraints for a good blend: integration, web, unpacking, topology, good reason (a02). Topology example: Church relates to Altar as Laboratory relates to Lab-Bench. Veale and colleagues note the constraints are not orthogonal, so no blend meets all of them, and other writings by the theory's authors give other lists. They were never turned into one measurable test (a02). Four network types are named: simplex, mirror, single-scope, double-scope (a06).

**Criticism.** Gibbs (2000) argued that blending is hard to falsify, works as a framework, and infers process from products (a07, b22; seen second-hand only). Veale (2002) said blending must be shown tractable and constrained, or it stays a set of "just-so" stories (a04).

**Turner's own concession.** In "Challenges to Blending Theory" (2013/2014) Turner says the evidence is mostly indirect. The method is to fit generalisations to in-sample data (for example grammar patterns), then check them on out-of-sample data. Blending is not an algorithm. Experiments exist (McCubbins and Turner 2013) but the design is hard (a05, b21). No effect sizes are on the page. Claim K01.

**Human experiments tied to blending.**
- Coulson and Van Petten (2002): brain-wave (N400) study of literal, metaphorical and "literal mapping" sentence endings, N=18. Seen as snippet only (a08).
- Bambini et al. (2016): N=13 in two experiments. N400 relates to contextual expectation, so integration cost is partly explained by context (b23).
- Forgacs et al. (2015): N=35 analysed. Metaphor N400 effect appeared for low-concreteness metaphors only (metaphor nouns -1.17 microvolts vs abstract literal -0.29, p<0.05) (d14).
- No direct replication of Coulson and Van Petten was found (d15, d16). Status: contested (K17).

**Conceptual combination research (older and separate).** Hampton's work on how people combine concepts such as "pets that are also birds" is the closest human behavioural base. It is not about Fauconnier and Turner's theory, and it dates from 1987 to 1996 (b01 to b05). It measures "emergent attributes": attributes true of the combination but not inherited from either part. Findings are in section 3.

**Education.** Dreyfus, Gupta and Redish (2015) apply blending to physics teaching. A professor and a student blend "energy as substance" with "energy as location" in one mental model. Two episodes, coded by predicates and gestures, no counts (b25). Illustrative only.

**Computational line.**
- Sapper (Veale, O'Donoghue, Keane 2000): spreading-activation graph matcher. Bridges built by triangulation (two concepts share a neighbour) and squaring (a bridge links neighbours). Example threshold 0.01, 10% attenuation per arc. Argued to be closest to blending of SME, ACME, Tabletop, LISA (a03). A Tabletop-style slipnet softens strict isomorphism (a25).
- Divago (Pereira 2007): two input domains plus generic space, blend principles applied until a stable solution (c22; not opened).
- Goguen / Diaconescu: blends as colimits in category theory, later lax cocones (a10). Theory only.
- COINVENT (Eppe et al. 2018): generalise inputs by answer set programming; rank blends by optimality principles (a09, c21; not opened). Besold and Plaza (2015): anti-unification (HDTP) then asymmetric amalgams; two case studies, no numbers (c19). Their worked example shows the shared generic space explains why one phrase blends and another does not.
- Li et al. (2012) goal-driven blending; VisiBlends (Chilton et al. 2019) (c23, c25; not opened).
- All of these were checked on hand-built examples. No shared benchmark exists (K19). Slides from 2025 still name determining the generic space and rating blend quality as the main open challenges (d19, snippet only).

**LLM era.** From 2021: language models propose the connecting object (Ge and Parikh), GPT-3 proposes connectors (PopBlends), vision-language models read artist mashups (Peng), benchmarks of emergent properties (Song), and the open-ended benchmark across association, analogy and blending (Schapiro). See section 6.

## 3. Core findings with exact numbers

Status key: established (more than one independent source or consistent across sources), single-source, contested, refuted.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Blending theory has four spaces; no single measurable criterion for a good blend | Five optimality constraints, not orthogonal | a01, a02, a05, b21 | established (K01) |
| Strict emergent attributes in human conjunctions are rare | Hampton 1987: 3 of 174 strict, 11 lenient | b01 | single-source (K02) |
| Stricter emergence test leaves almost nothing | 51 attributes with 0% for A; 24 stayed 0% for "A which are not B"; 11 slight (0 to 5%); only 6 reached 10% or more | b02 (Hampton 1989 via 1996 chapter) | single-source (K02) |
| Social-stereotype conjunctions give more emergents | Conjunction rating fell outside constituent range on 23% (congruent) and 33% (incongruent) of trait judgments | b03 (Hastie et al. 1990) | single-source |
| Attributes false of both inputs are often true of the conjunction | 22 of 63 (35%) | b04 | single-source (K03) |
| Inheritance depends on point of view | 210 attributes, 4 pairs, only 2 true of both categories; own-view positives 65, only 11 (17%) inherited; 69% of "other" inherited; about 8% for 37 unimportant attributes | b04 | single-source |
| Incongruent combination makes people invent explanatory stories | Qualitative only | b05 | single-source |
| LLMs are worse at blends than at analogy or association | Valid rates 43.4 / 53.4 / 59.0% (blend / analogy / association), 35 LLMs | a15, b09 | single-source (K04) |
| Frontier LLMs beat lay humans on all three tasks | Humans 12.8 / 32.9 / 22.1% valid (N=75 Prolific, 5 items per task). Humans' skipped items scored zero, so the gap is inflated | a15, b10 | single-source (K05) |
| Bottleneck is the generic space | Valid generic space 43.4%; given one, coherent blend 97.1% | a15, b09 | single-source (K06) |
| Inventive homogeneity across LLMs | 2,070 concepts, 7,868 properties; 19.9% (412) reuse 2 or more properties. Blends vs analogies: 37.3% vs 2.6% (14.3x) at level 2; 94.7% vs 36.3% (2.6x) at level 1. Same provider 9.3% vs different provider 4.1% (2.3x) | a16, b11 | established as a pattern (K07) |
| Same homogeneity on other tasks | Pairwise distance LLM vs human: AUT 0.459 vs 0.738; FF 0.534 vs 0.835; DAT 0.665 vs 0.819. Recipe merges: 56% used smoked paprika (0.375% in repository) | d01, d08 | established (K07) |
| Skills correlate across models | Association vs analogy originality r=0.73; vs original blends r=0.42; vs surprising blends r=0.50; mean cross-task r 0.47; n=35 models | a17, b12 | single-source (K08) |
| LLM judges for blends are only moderately reliable | ICC 0.67 (integration quality), 0.67 (utility G(g)), 0.48 (utility V(c)); panel agrees with humans 75% on unanimous items; research-ideation LLM vs human Pearson 0.159 (best seen 0.234) | b13, b26 | established (K09) |
| LLMs poorly name why a property holds | GPT-4o has-property 82.6% (95.6% when yes, 69.6% when no); four-way type 56.4% vs human 81% (n=1000, 250 per type) | b07, c04 | single-source (K10) |
| LLMs write few emergent noun phrases | Emergent score E at most 27 for baseline LLMs; humans 38.0; gold 59.9; CCPT has 12,315 instances | b06, c03 | single-source (K10) |
| Iteration adds little for emergents | Spread-activation prompt, 1 to 5 iterations: property induction emergent 45.1 to 45.8; canceled 60.5 to 63.3; completion emergent 26.0 to 26.9 (model attribution of the last pair uncertain, see critique) | b08, c05 | single-source (K11) |
| LLM judge tracks human on emergence | Pearson 0.85, Spearman 0.83 (300 pairs, 3 raters each); human Fleiss kappa 0.59 | b08, c06 | single-source |
| Generator plus filter helps human creators | PopBlends 2.03 (SD 0.84) vs 0.87 (SD 0.56) ideas per pair, N=10, Wilcoxon p<0.001; NASA-TLX mental demand 2.85 vs 5.80 (p=0.004); effort 3.05 vs 5.00 (p=0.006); all 10 preferred it | a12, c16 | single-source (K12) |
| But GPT-3 content is partly wrong | Connector accuracy 56.0 / 55.3 / 58.7% (No-, Half-, Full-GPT); at least one good of five 90.0 / 96.6 / 93.3%; attribute accuracy 2.86 of 5 (57%); adjectives 79%, activities 58%, catchphrases 35% | b15, b16, c15 | single-source |
| Theory-guided prompting raises judged ingenuity | Image metaphors, N=100: direct prompt 2.75, strong prompt 3.69, no-theory-text 3.66, full 4.56 (text says 4.61) | a20 | single-source (K13) |
| VLMs understand mashups at near-expert level | Implication win rate: experts 78.3, GPT-4o 73.5, GPT-4V 71.9, Gemini-1.5-Pro 71.7, Claude-3.5-Sonnet 62.9, average people 51.0, Claude-3-Opus 39.2, LLaVA-1.5-7B 20.1; 666 mashups. Identification precision 75.67 vs 53.42 (humans) | a13, b18, c13 | single-source (K14) |
| Concept step works, rendering fails | 90% (36/40) integrated; 27.8% (10/36) failed to render | a14, b19 | single-source (K14) |
| Three-step IEI prompt beats two-step | Friedman p<0.0001 across 5 image models; Midjourney mean rank 1.98 (IEI) vs 2.40 (II) | c14 | single-source |
| Diffusion midpoint is not reliable blending | At ratio 0.5: blended-concept depiction 0.621, mixed 0.862; over all ratios 0.389 and 0.471; 1,000 nouns | a21, b17, c11 | single-source (K15) |
| No image blend method wins everywhere | 100 participants, 22 pairs, ALTERNATE over SWITCH 51% (p=0.31); ALTERNATE over TEXTUAL 60% | c09, c10 | single-source (K16) |
| Temperature is a weak lever | GPT-4o idea diversity 0.618 (T=0) to 0.679 (T=1); Llama-2 70B novelty slope 0.308 (SE 0.138), coherence loss 0.240 (SE 0.122); gibberish above T=1 | d04, d05, d06, d08 | established (K21) |
| Personas and constraints restore diversity | Diversity: humans 0.773; random personas 0.757; random constraints 0.735; zero-shot 0.679. "Be creative" system prompt: variability 0.503 / 0.576 vs 0.459 baseline (human 0.738). Iterative "bolder" lowers to 0.575 | d02, d03 | single-source (K22) |
| Structured recombination beats plain GPT-4o on novelty | Novelty 3.53 vs 3.146 (p=0.0009); 3.612 vs 3.141 (p=9.2e-8); valuable 80% vs 82% (Exp.1), 85% vs 98% (Exp.2) | d07, d08 | single-source (K23) |
| Abstraction-first prompting helps but can break answers | Step-Back PaLM-2L MMLU Physics 66.4 to 73.2%, Chemistry 70.9 to 81.8%; corrects 20.5% of baseline errors, adds 11.9% new | d09, d10 | single-source (K24) |
| Blending as a problem-solving operator: no measurement | Nearest: Mixture-of-Agents 65.1% vs 57.5% AlpacaEval 2.0 (candidate aggregation, not blending) | d11, d12, d20 | single-source (K25) |
| GPT-2 on emergents | 7 of 15 Murphy items; humans had an emergent property on 15 of 18 items | d13 | single-source (K26) |
| Blending prompts "awaken" LLMs | No controlled support; fused vs non-fused prompts not significantly different | a22, b20, c07, c08 | refuted/unsupported (K18) |

## 4. Mechanisms and models

Each is described so an engineer could build it. None has been shown to improve reasoning accuracy.

**4.1 The four-space procedure as a prompt pipeline.**
1. Input: two items A and B (ideas, approaches, concepts).
2. Generic space: write the shared abstraction as typed roles. Example: "both are a way to reduce a set by testing a property". Check it (section 4.5).
3. Align: list pairs of matching elements and relations (lab=church, bench=altar).
4. Selective projection: for each element choose from A, from B, from both, or neither. Write the choice and one reason.
5. Compose: build the blend as a short structured description.
6. Elaborate (run the blend): derive consequences. In a reasoning task, run it: execute the merged procedure on examples with code.
7. Unpack: say how the blend maps back to A and B. A blend that cannot be unpacked fails the "unpacking" constraint (a02).
8. Check the five constraints as a rubric (integration, web, unpacking, topology, good reason).

**4.2 Sapper-style graph blending (a03, a25).** Store concepts as graph nodes with typed edges. Spread activation from both inputs. Add a bridge when two nodes share a neighbour (triangulation). Add a bridge between neighbours of an existing bridge (squaring). Attenuate activation 10% per arc, threshold 0.01. A slippage rule lets related but non-identical relations match above a minimum probability. Bridges that cover a coherent set form the alignment; the generic space is what the aligned nodes have in common.

**4.3 Generalise-then-blend (COINVENT, HDTP) (c19, a09).** Generalise each input by anti-unification: replace differing constants by variables so both inputs fit one pattern. The pattern is the generic space. Then combine with asymmetric amalgams: take the generalised pattern and instantiate parts from A and parts from B. Rank by optimality metrics. Search for generalisations can be done with answer set programming.

**4.4 Generator plus filter (PopBlends) (b15, c15).** Stage 1: expand each domain into associations (LLM plus knowledge base), find a connecting concept, filter by whether it relates to both domains. Stage 2: find scenes or objects related to the connector. Filter again. Stage 1 connector accuracy was only about 56 to 59%, but at least one of five was good 90 to 97%. So generate five, filter, keep one.

**4.5 Verification of the generic space.** Schapiro scores a generic space on utility, coherence and emergent integration with a judge panel (a18). For an agent, a cheap check is: does each claimed shared role have a concrete instance in A and in B (checkable by a second pass or code)? Step-Back shows an unchecked abstraction adds errors (11.9% new errors) (d10).

**4.6 Spread-activation scaffold for combination (c05).** Iteratively retrieve related concepts from the LLM and ConceptNet, filter distractors, then answer. Gains were under 3 points per task.

**4.7 Structured recombination (DishCover) (d07).** Parse both items into trees, recombine with an edit-distance operator, rank by novelty, rewrite. This is the nearest tested thing to "selective projection".

**4.8 Diffusion blends (c09, a21).** Embedding average, switching or alternating prompts mid-denoising. Mixing is not selective projection. Not relevant to text reasoning.

## 5. What holds up

**Holds up (more than one source).**
- Blending theory has no single decisive test; even its founder says the evidence is indirect (K01).
- LLM outputs across models and vendors are more alike than human outputs (K07: Schapiro 19.9% reuse; Wenger and Kenett AUT 0.459 vs 0.738; DishCover 56% smoked paprika).
- Temperature does little for diversity and costs coherence (K21; four sources).
- LLM judges of creativity are only moderately reliable (K09; ICC 0.48 to 0.67, Pearson 0.159 for ideation).
- Evaluation is mostly LLM-judged and in shifted domains, so effect sizes for text blending in reasoning are unknown (K20).

**Single-source but carefully checked.** Schapiro's ranking of blend below analogy below association; the 97.1% coherent-given-valid-generic-space figure; Song's emergent-type 56.4% vs 81%; PopBlends 2.03 vs 0.87 ideas. All re-opened in full text (critique.md).

**Failures and non-replications.**
- No replication of Coulson and Van Petten 2002 was found; the later ERP study (N=35) found the effect only for low-concreteness metaphors (d14). Contested.
- McCubbins and Turner (2013) could not be located (d16).
- Claims that blending prompts awaken or induce hallucination in LLMs: fused and non-fused prompts did not differ significantly; no controlled design (c08, K18).
- Iterated self-refinement for emergents gave under 3 points (c05). Iterative "bolder" refinement lowered diversity (d03).
- Diffusion midpoint blending fails to depict both concepts in a large share of cases (0.389 over all ratios) (a21).

**Moderators and boundary conditions.**
- Congruence: stereotype conjunctions gave 23% (congruent) vs 33% (incongruent) rating shifts (b03). Object categories give far fewer emergents (b01).
- Point of view: inheritance depends on which input you take as the own view (17% vs 69%) (b04).
- Same-provider models are 2.3 times more alike than different-provider models (b11).
- Fusion mashups are easier to decompose than replacement ones in 9 of 11 models, but the paper's own text is not fully consistent on direction (a14).
- Concreteness moderates the metaphor N400 (d14).
- Seed and prompt order: swapping order changes which concept dominates in diffusion; 10 seeds per pair tested (c10).
- Category: no image method wins everywhere (c09).

**Interventions that worked (narrow).**
- Generator plus filter for human ideation (PopBlends, N=10) (c16).
- Theory text, diagnosis and transfer agents for image metaphors: 2.75 to 4.56 judged ingenuity (a20). Removing the theory text moved ingenuity only from 4.56 to 3.66, while a strong generic prompt already reached 3.69, so a good prompt carries part of the gain and the theory text's own share is unclear.
- Random personas and constraints for diversity (d03).
- Structured recombination for novelty (d07).
- Three-step identify, explain, implicate prompt for image generation (c14).
- Step-Back abstraction on STEM questions (d09), at a cost of 11.9% new errors.

**Interventions that did not work or are unproven.**
- Temperature (K21), "be creative" system prompts (d02), repeated "bolder" refinement (d03), spread-activation iteration (c05). Exclusion lists and a generic-space step for blends were never tested.

## 6. Language models

**How they behave on blending tasks.**
- Schapiro et al. 2026 (a15, b09, b10, b11, b12, b13; arXiv 2509.21043): open-ended tasks on random entity pairs. 35 LLMs, 75 Prolific adults. Sampling T=0.9, top-p and top-k off (d17). Valid rates: association 59.0%, analogy 53.4%, blend 43.4%. Humans 22.1 / 32.9 / 12.8%. Top blend score 64.8 for one OpenAI model, 45.7 for one Anthropic model (critique-confirmed). The valid generic space is the bottleneck: valid 43.4% of the time; 97.1% coherent blend afterwards. Reuse across models 19.9%; blends 14.3 times more reusable than analogies at level 2. Humans use different semantic regions: LLMs name more people (+5.2 points) and places (+3.6) (a19).
- Caveats: humans' skipped items were scored zero; humans were lay, not experts; judges were a three-LLM panel with ICC 0.48 to 0.67; the unit in the correlations is the model (K05, K08, K20).
- Song et al. 2025 (CCPT; arXiv 2502.06086): LLMs including o1 find emergent properties harder than canceled ones; four-way type 56.4% vs 81% human. Models tested: Llama-3.1-70B, Qwen2.5-72B, GPT-4o, Claude-3.5-Sonnet, o1-mini, o1 (b06).
- Lake and Murphy 2021: GPT-2 got 7 of 15 emergent items; context did not help (d13). No modern repeat exists.
- Peng et al. 2025: understanding of visual mashups close to human experts for top VLMs; some models far below (Claude-3-Opus 39.2, LLaVA 20.1). Rendering is the weak step (27.8% fail) (b19).
- Ge and Parikh 2021: bigger language models find the blend partner better (P@1000 best 66.38 vs BERT-base 5.90; row labels unclear) (b14, c01). Human raters (20 descriptions, 6 questions, 9 raters) preferred BigSleep over DeepDaze, both over DF-GAN (c02).
- Xu et al. 2026: multi-agent "Schema Grammar" system raised judged ingenuity (a20).

**What changed behaviour, and by how much.**
- Theory-aware structure in the prompt: +0.9 to +1.8 ingenuity points on a 5-point scale (2.75 to 3.69 to 4.56), but the strong generic prompt gave most of the first step (a20).
- IEI three-step prompt beat the two-step prompt (c14).
- Personas / constraints: diversity 0.679 to 0.757 / 0.735 (d03).
- Temperature: 0.618 to 0.679 (d04).
- Iteration: under 3 points (c05).
- Structured recombination: about +0.4 novelty points on a 5-point scale (d07).
- Step-Back (abstraction first): +6.8 points Physics, +10.9 Chemistry for PaLM-2L; costs 11.9% new errors in the Physics error analysis (d09, d10).

**What is missing.** No study tests whether the blending structure improves an LLM's reasoning or problem solving. All LLM blend studies are about creative output, mostly images, with LLM judges. Token cost is not reported in any of these studies.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = Section 5 memory of SCHEMA.md.

### Add now (established)

1. **Do not trust a single LLM judge for blends or novelty; use code checks or human spot checks.** Part G (G5, G8). [E] K09, K20; ev b13, b26, c18, a15. Consistent with G8; this adds the numbers: ICC 0.48 to 0.67, Pearson 0.159.
2. **Expect homogeneous output; do not use temperature to diversify attempts.** Part O7 and G4. [E] K07, K21; ev a16, b11, d01, d04, d05, d06, d08. Several blend attempts will overlap. Temperature costs coherence for a small diversity gain (0.618 to 0.679).
3. **Log the concept step and the execution step separately.** Part G (G2, G10). [S] K14; ev b19. Concept can be fine while execution fails (27.8%). A logging rule, not a schema change.
4. **Do not use "be creative" prompts or "bolder" iteration as a diversity move.** Part O7. [S] K22; ev d02, d03. The null for "be creative" is in d02. Treat as a "do not add" note, consistent with section 4b.
5. **Do not add the "blend prompts awaken the model" idea.** Part none. [refuted] K18; ev c08.

### Test first (not established)

1. **Generic-space-first blend operator (merge two failed approaches).** Part O7 / S6. [S] K06, K24, K25; ev a15, b09, d09, d10. Name the shared abstraction, verify it, then project and run. Nobody has tested this; Schapiro suggests the generic space is the bottleneck.
2. **Verifier on the abstraction before merging.** Part G (verification). [S] K24; ev d10 (11.9% new errors).
3. **Selective projection with explicit keep/drop choices vs simple "combine".** Part O7. [S] K23, K19; ev d07, d08.
4. **Persona or constraint injection across sampled blend attempts.** Part O7 / memory. [S] K22; ev d03.
5. **Exclusion list in memory of properties already used.** Part memory. [S] K07; ev a16. Never tested anywhere.
6. **Generator then cheap filter (five connectors, keep one).** Part O7. [S] K12; ev b15, c15, c16.
7. **Check for false emergents: a claimed new property must not be retrievable from one input alone.** Part G3 / O7. [S] K02, K03, K10; ev b01, b02, c04.
8. **Run the blend (elaboration) by code on examples.** Part G3 / G8. Supported by theory (a06), untested for LLMs. [C].

## 8. Concrete tests on our bench

All arms get equal total tokens, including setup (G7). Blind or code-based scoring where possible. The bench harness skill runs these.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Stuck-state items from our reasoning bench (plain model failed; two attempts failed differently) | (a) restart fresh, (b) best-of-N, (c) generic-space-first blend of the two failed attempts, (d) plain "combine the two attempts" | Solve rate at equal tokens, exact-answer check | (c) at least +3 points over (a) and (b); (d) near (a). Likely small; ensemble gain may be only extra sampling (G9) |
| T2 | Schapiro-style random entity pairs (blend task) | plain prompt vs generic-space propose-and-check then blend | Valid-blend rate by blind rubric plus code check on listed roles | Valid rate above the plain baseline by 5+ points if the bottleneck claim is right |
| T3 | Same items | with vs without verify-the-abstraction step | Fraction of generic spaces rejected; valid-blend rate | Rejection 10 to 30%; net gain only if new errors stay under 12% (Step-Back level) |
| T4 | k=5 blends per item | temperature 1 vs persona injection vs constraint injection vs exclusion list | Property reuse across runs (a16 definition) and valid rate | Persona and constraint reduce reuse more than temperature; exclusion list reduces most; validity drops by no more than 3 points |
| T5 | Hampton-style conjunction pairs (from b01, b04) | LLM attribute lists vs human lists | Share of LLM "emergents" retrievable from one input; agreement with human emergents | LLM false-emergent rate above the human strict rate (3 of 174) |
| T6 | Selective projection ablation | keep/drop table vs plain "combine" | Novelty and validity by blind judges (human spot checks on 20 items) | Projection adds novelty and costs some value (DishCover: 85% vs 98% valuable) |
| T7 | Judge reliability on 100 human-rated blends | LLM panel of 3 vs single judge vs rubric | ICC and agreement with humans | Panel ICC 0.5 to 0.7; need above 0.8 before trusting a leaderboard |
| T8 | Procedure-style tasks | merged procedure run on 3 held-out examples vs not run | Solve rate | Gain only on procedure-style tasks |

## 9. What does not transfer, and why

- **Image and diffusion results** (Matsuhira, Olearo, Peng's rendering step, Vibe Blending): they measure embedding mixing and rendering, not selective projection or reasoning. Midpoint blending is not O7.
- **Lay human comparisons** (12.8% vs 43.4%): humans' skipped items counted as zero, no experts, so "LLMs beat humans at blending" is not a usable claim (K05).
- **Hampton emergence rates**: attribute lists for noun-noun concepts, 1987 to 1996; definitions of emergence differ (attribute listing vs rating position). They show how rare real emergence is, not how to solve problems.
- **PopBlends**: N=10 students on pop-culture product ideation; ideas were counted, not rated for quality. Not comparable with Schapiro's judged quality.
- **Brain-wave work (N400)**: small samples, contested, nothing about agent design.
- **Formal systems (Divago, COINVENT, category theory)**: built for hand-made domains with symbolic knowledge bases; no benchmark against plain LLMs.
- **Physics-education case studies**: two episodes.
- **Creative-writing and recipe results**: these tasks reward novelty and diversity; our bench scores correctness. A blend that is novel and wrong loses.
- **Sato's essays**: hypothesis only (K18).

## 10. Open questions

1. Does an explicit generic-space step raise valid-blend rate or reasoning accuracy for an LLM at equal tokens? (Gap 1)
2. Does blending help as a stuck-state operator at all? (Gap 2)
3. What is the expert baseline for textual blends? Schapiro names it as future work (d17). (Gap 3)
4. Do exclusion lists reduce reuse, and at what token cost? (Gap 4, partly closed)
5. Which blend judge setup reaches ICC above 0.8? Human-calibrated rubrics vs LLM panels. (Gap 5)
6. Do the Coulson and Van Petten and McCubbins and Turner results replicate? (Gap 6)
7. Do modern LLMs produce more or fewer true emergents than humans on the same pairs? (Gap 7)
8. Do Divago or COINVENT beat a plain prompt on a shared benchmark? (Gap 8)
9. Does selective projection matter in text, or does simple mixing do as well, as it nearly does in diffusion? (Gap 9)
10. Is the 97.1% coherence-given-valid-space figure partly caused by lenient LLM judges?

## 11. Sources

[V] opened (full text or page) by the evidence agents; [M] snippet or second-hand only.

- [V] Veale, O'Donoghue, Keane (2000) Computation and Blending. https://mural.maynoothuniversity.ie/id/eprint/8182/1/DOD-Computation-2000.pdf
- [V] Veale (2002) How to Blend Concepts and Influence People. https://apcz.umk.pl/THS/article/download/ths.2002.016/13458
- [V] Turner (2013/2014) Challenges to Blending Theory. https://markturner.org/ChallengesToBlendingTheory.html
- [V] Wikipedia, Conceptual blending (accessed 2026). https://en.wikipedia.org/wiki/Conceptual_blending
- [M] Gibbs (2000) Making good psychology out of blending theory (via secondary pages). https://en.wikipedia.org/wiki/Conceptual_blending
- [M] Coulson and Van Petten (2002) Conceptual integration and metaphor: an ERP study. https://link.springer.com/article/10.3758/BF03195780
- [M] Fauconnier and Turner (1998) Cognitive Science 22(2):133-187; (2002) The Way We Think (named only, not opened)
- [M] McCubbins and Turner (2013); Turner (2001) Cognitive Dimensions of Social Science. https://markturner.org/cdss.html
- [M] Hampton (1987), Wilkenfeld and Ward (2001) originals. https://pubmed.ncbi.nlm.nih.gov/?term=Wilkenfeld+Ward+similarity+emergence+
- [V] Hampton (1996) Emergent attributes in combined concepts (author PDF). https://www.staff.city.ac.uk/hampton/PDF%20files/Creative%20concepts%201996
- [V] Lake and Murphy (2021) Word meaning in minds and machines. https://arxiv.org/abs/2008.01766
- [V] Bambini et al. (2016) Disentangling metaphor from context. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016
- [V] Forgacs et al. (2015) Metaphor N400. https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fn
- [V] Dreyfus, Gupta, Redish (2015) Applying conceptual blending to model coordinating multiple ideas in physics. https://arxiv.org/abs/1412.1693
- [V] Diaconescu (2017) 3/2-institutions. https://arxiv.org/abs/1708.09675
- [M] Eppe et al. (2018) A computational framework for conceptual blending. https://tore.tuhh.de/entities/publication/ebc32175-2b53-4ea3-9d9c-8f5a6988a
- [V] Besold and Plaza (2015) Generalize and Blend. https://www.iiia.csic.es/~enric/papers/generalize_and_blend.pdf
- [M] Pereira (2007) Creativity and AI: a conceptual blending approach. https://estudogeral.uc.pt/bitstream/10316/1747/2/PhDThesis.pdf
- [M] Li, Zook, Davis, Riedl (2012) Goal-driven conceptual blending (seen as a citation)
- [M] Chilton, Petridis, Agrawala (2019) VisiBlends. https://dl.acm.org/doi/10.1145/3290605.3300402
- [V] Ge and Parikh (2021) Visual Conceptual Blending with Large-scale Language and Vision Models. https://arxiv.org/abs/2106.14127
- [V] Wang, Petridis, Kwon, Ma, Chilton (2023) PopBlends. https://arxiv.org/abs/2111.04920
- [V] Peng et al. (2025) Probing and Inducing Combinational Creativity in VLMs. https://arxiv.org/abs/2504.13120
- [V] Schapiro et al. (2026) Measuring Combinatorial Creativity in LLMs. https://arxiv.org/abs/2509.21043
- [V] Song et al. (2025) Is a Peeled Apple Still Red? https://arxiv.org/abs/2502.06086
- [V] Xu et al. (2026) Beyond Pixels (schema grammar). https://arxiv.org/abs/2602.01335
- [V] Matsuhira et al. (2024) Investigating Conceptual Blending of a Diffusion Model. https://arxiv.org/abs/2411.03595
- [V] Olearo et al. (2025) Blending Concepts with Text-to-Image Diffusion Models. https://arxiv.org/abs/2506.23630
- [V] Yang et al. (2025) Vibe Spaces for Creatively Connecting. https://arxiv.org/abs/2512.14884
- [V] Sato (2025) The Way We Prompt. https://arxiv.org/abs/2505.10948 ; Waking Up an AI. https://arxiv.org/abs/2504.21012
- [V] McCaig, DiPaola, Gabora (2016) Deep convolutional networks as models of generalization and blending. https://arxiv.org/abs/1610.02478
- [V] Lu et al. (2026) Rethinking creativity evaluation. https://arxiv.org/abs/2508.05470
- [V] Xi, Cheng, Soni, Turner (2026) ACL poster. https://markturner.org/ACL2026_Conceptual_Blending_Poster_compressed.pdf
- [V] Wenger and Kenett (2025) We're Different, We're the Same. https://arxiv.org/abs/2501.19361
- [V] Terwiesch et al. (2026) idea diversity study. https://arxiv.org/abs/2607.27553
- [V] Peeperkorn et al. (2024) Is temperature the creativity parameter? https://arxiv.org/abs/2405.00492
- [V] Evstafev (2025) The Paradox of Stochasticity. https://arxiv.org/abs/2502.08515
- [V] Mizrahi et al. (2026) DishCover, structured recombination. https://arxiv.org/abs/2504.20643
- [V] Zheng et al. (2024) Take a Step Back. https://arxiv.org/abs/2310.06117
- [V] Yasunaga et al. (2024) LLMs as Analogical Reasoners. https://arxiv.org/abs/2310.01714 (abstract level only)
- [V] Wang et al. (2024) Mixture-of-Agents. https://arxiv.org/abs/2406.04692
- [M] Leemhuis and Kutz (2025) Abstractron slides. https://www.inf.unibz.it/~okutz/resources/Leemhuis-Abstractron25.pdf
- [M] Du et al. (2025) The Challenge of Teaching Reasoning to LLMs. https://arxiv.org/abs/2507.09850
- [M] BIG-bench conceptual combinations (2023), FakeReef. https://arxiv.org/abs/2206.04615
