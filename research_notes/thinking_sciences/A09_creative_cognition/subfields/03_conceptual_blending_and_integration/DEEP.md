# Conceptual blending and integration: deep document

*Subfield A09.03. Built from evidence_a-d.jsonl (a01-a30, b01-b31, c01-c26, d01-d19), claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids are cited as a07, K05 and so on. Numbers were re-opened by a checker pass on 2026-10-31 unless marked otherwise. Other subfields in this run (structure mapping, Boden's creativity types, framing and reframing, bio-inspired and analogical design, Einstellung) are only linked, not covered.*

## 1. What it is

Conceptual blending (also called conceptual integration) is a theory of how people combine two or more mental inputs into a new one. It was proposed by Fauconnier and Turner. The standard picture is a network of four mental spaces.

- **Input spaces.** Two (or more) sources, each with its own roles and relations.
- **Generic space.** What the inputs share at an abstract level. It licenses the cross-space match.
- **Blended space.** A new space that takes selected parts of each input.
- **Emergent structure.** Content that is in neither input. It comes from three steps: composition (put projected parts together), completion (fill the gap using background knowledge), elaboration (run the blend mentally and see what follows).

Classic examples are the Buddhist monk riddle (one monk walks up and down a mountain on two different days; blend the two days into one day with two monks and they must meet), the "debate with Kant", the boat race, and the computer virus (a01, a02).

Forerunner: Koestler's bisociation (two unrelated frames meet and give a creative act). Critics: the theory has no single testable hypothesis, and simpler processes may explain blends (a07, a08, a09, b10, b11).

**Why it matters for our agent.** It supplies the "open-mode operator: combine two sources". In the schema this sits between O7 (map an analogue) and open-mode generation in S3. The useful question is not "is blending theory true". It is: does a structured combine step (state the shared frame, then blend, then check) beat a plain "combine A and B" prompt at equal tokens? Section 6 and K25 show that nobody has run that arm.

**Scope warning.** The human evidence is mostly about concept conjunction (two-word concepts), not full four-space networks. No experiment manipulates the generic space (critique, weak spots). The LLM evidence is mostly rated by LLM judges.

## 2. History and theories in depth

### 2.1 Roots
- **Koestler (1964), bisociation.** Creativity as the meeting of two self-consistent but unrelated frames. Not tested in the sources we opened; it is the named forerunner.
- **Fauconnier, mental spaces (1985)** and **Fauconnier and Turner (1993, 1998, 2002).** The 1998 Cognitive Science paper is the fullest statement (a01-a04, opened). It has no experiment and no sample. The data are worked examples.
- **Grady, Oakley and Coulson (1999)** (a05) apply blending to metaphor. The surgeon-butcher example: butcher maps to surgeon, cow to patient, cleaver to scalpel, abattoir to operating room. The blend gives the idea "incompetent surgeon", which neither input holds.

### 2.2 The theory's parts (a02, a03, a04)
- **Cross-space mapping** between inputs, with a generic space capturing what is common.
- **Selective projection**: not all input content enters the blend.
- **Three levels of shared topology** across frame networks (a04). No counts.
- **Five optimality principles** (a03). Two matter for engineering. *Topology*: relations of a projected element should match its counterpart in the input. *Unpacking*: the blend alone should let you rebuild the inputs and the mapping.
- **Blend types.** Fusion, juxtaposition and replacement are used in the visual-metaphor literature (b28, c12). Replacement is the hardest (K18).

### 2.3 The critics
- **Gibbs (2000/2001), Harder (2003), Brandt (2005), Oakley and Hougaard (2008), Ferguson and Sanford (2008)** (named in b10, a08). Gibbs's paper itself was not opened (a28, b12 snippet only).
- **Ritchie (2004)** (a07, opened, no data): the theory is a descriptive framework, not an algorithm; falsifiability is unclear. Fauconnier and Turner (2002) answered by comparing blending to evolutionary biology.
- **Glebkin (2013)** (b10): lists the objectors, calls the complex-numbers example a misunderstanding. No new data.
- **Turner (2013)** (a09, b11) concedes the evidence is mainly in-sample generalisation and the process "does not appear to be algorithmic". He cites McCubbins and Turner (2013) for experiments on which blending patterns are easier for subjects. Not opened (K29).
- **Simpler explanations.** Deep networks and embedding averaging produce blends without any four-space structure (a26 McCaig et al. 2016; c23; K20).

### 2.4 The psychology of combining concepts (human data, 1987-2002)
Blending is close to the older topic of **conceptual combination**. The key finding there is that emergence is rare (K07) and depends on the demand to explain (K08). See section 3 for numbers. The 1990s work (Hampton, Hastie, Kunda, Wilkenfeld and Ward, Estes and Ward) is the empirical base. Almost all of it is 1987-2002 (critique, weak spots).

### 2.5 Computational blending
- **Sapper / Veale, O'Donoghue, Keane (c25).** Spreading activation over a network. Unchecked spreading may visit most nodes of a connected network.
- **Eppe et al. (2015, 2018)** (a10 opened, a11 snippet). Answer-set programming and amalgamation. A proof of concept on small logic concept bases. Not a performance test.
- **Topological group generation (a27, 2021).** Three specifications give the same concept. No statistics.
- **Lynn (2026)** (a21, d15, b29). A conceptual paper with a toy vector-symbolic model of the Osprey tiltrotor blend. No experiments. Claims human blends are goal-selected (K23).
- **Xi, Cheng, Soni, Turner (2026)** (a22, b31, d18). A poster proposing six scoring dimensions from blending theory for generative AI. No results.

### 2.6 The LLM turn (2021-2026)
Section 6 covers it. In short: Ge and Parikh (2021) and PopBlends (2023) used language models as blend engines. KOMBINE (2025/26) is the first benchmark that compares blending to association and analogy across 35 models. CCPT (2025) tests emergent property generation directly.

## 3. Core findings with exact numbers

Status: established = two or more independent sources or a replicated effect; single = one source; contested = sources disagree. "Human" and "LLM" are marked.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Truly emergent attributes are rare in plain conjunction (human) | Hampton 1987: strict scoring 3 of 174 attributes emergent, lenient 11. About 8% of 37 attributes unimportant for both parts were important for both orders of the conjunction | b01 (Hampton 1996 review) | established (K07) |
| Negated constituent (human) | 6 pairs, 51 attributes rated 0% for the head noun: 24 stayed 0%, 11 rose only 0-5%, only 6 reached 10% or more | b02 (Hampton 1989 in review) | established |
| Trait pairs give no emergence (human) | Congruent: 31 of 32 attributes inherited. Incongruent: 16 of 25 likely behaviours inherited, 9 not. Zero emergent attributes | b03 (Hampson 1990) | established |
| Stereotype conjunctions give more emergence; incongruity raises it (human) | Emergent ratings (outside both parts by one scale step) on 23% of ratings congruent, 33% incongruent; 15 bipolar dimensions | b04 (Hastie et al. 1990, Kunda et al. 1990) | single (K08) |
| Point of view changes what is inherited (human) | 210 attributes, 4 pairs. Own view: 11 of 65 (17%) inherited. Other category: 55 of 80 (69%) inherited. False of both parts: 22 of 63 (35%) emergent | b05 (Hampton 1996) | single |
| Metaphor costs more to process, graded N400 (human) | 18 adults, 165 triplets, cloze 3% matched. Metaphoricity 1.4 literal, 1.9 literal-mapping, 4.4 metaphor. Linear trend F(1,17)=6.86, p<.02 | a06 (Coulson and Van Petten 2002) | established (K11) |
| Same cost pattern in a replication (human) | 29 adults. RT literal 1377 ms, conventional 1487, novel 1620, anomalous 1615 | b06 (Lai, Curran, Menn 2009) | established |
| ERP data cannot tell blending from other accounts | Replication authors read the pattern as fitting indirect-access and career-of-metaphor | a06, b06, b08 | contested (K12) |
| Lexical blends (portmanteaus): shorter source contributes more (human) | 156 students, 4,708 blends, 24 source words. E1 chi2=266.51, V=0.25, R2=0.05. E2 chi2=194.7, V=0.1987, R2=0.022. Stress follows second word 61.5% vs 40.75% | b09 (Wulff and Gries 2019) | single; lexical, not conceptual |
| Far sources do not help human design ideas | 707 citing concepts, 110 (about 16%) shortlisted. Max source distance -0.33 log-odds per unit (95% CI -0.06 to -0.60). No-citation predicted rate 0.09 (CI .07 to .11); any-citation coefficient 0.31 (CI .01 to .62). Distance by LDA, r=0.51 with human ratings | d03 (Chan, Dow, Schunn) | contested (K09) |
| Atypical seeds give no creativity gain (human) | N=195. Total F(1,193)=1.680, p>.05. Sky story F(1,193)=4.446, p<.05 only | d02 (Kennedy 2015) | contested |
| Far analogies raise idea count but later concepts resemble the previous one | Abstract only | d04 (Chan and Schunn 2015) | contested; snippet |
| Iteration beats a single far combination | Indirect effects of far combinations were more consistently positive than direct effects | b14, d04 | single (K10) |
| Blending is the hardest of three tasks for LLMs | 35 LLMs, temp 0.9. Valid rate: association 59.0%, analogy 53.4%, blend 43.4%. Best blend 64.8% (gpt-5.6-sol; 55.4% on analogy) | a16, b18, c01 (KOMBINE) | single (K01) |
| Humans are lower still | 75 Prolific (120 recruited), 5 items each. Valid: association 22.1%, analogy 32.9%, blend 12.8% (skips scored zero) | c04 | single |
| The bottleneck is the shared abstraction (LLM) | Valid generic space 43.4%. Given a valid one, coherent blend 97.1% | c02, b19 | established (K02) |
| PopBlends has the same shape (LLM) | Connecting concept right 56.0 / 55.3 / 58.7% (No-, Half-, Full-GPT), pooled 56.7%. At least one good in five: 90.0 / 96.6 / 93.3% (pooled 93.3%). Scene on-topic 98.3% | a12, a13, c07, c08 | established |
| Blends from different models repeat each other | 2,070 concepts. 19.9% (412) share 2+ near-identical properties with another model's concept. Blends vs analogies: 37.3% vs 2.6% at 2+ (14.3x); 94.7% vs 36.3% at 1+. Same provider 9.3% vs 4.1% (2.3x) | a17, b19, c03 | single (K03) |
| LLM ideation collapses in diversity | Si et al.: about 5% non-duplicate of 4,000 seeds per topic (cosine 0.8). Novelty 4.84 human, 5.64 AI (p<0.01), 5.81 AI reranked (p<0.001). Feasibility 6.61 / 6.34 / 6.44 n.s. 49 per condition, 79 reviewers, 298 reviews | b26 | established (K04) |
| Best of N catches the good bridge | CCPT GPT-4o emergent-property score: base 40.8, best-of-5 (Multi-Oracle) 57.8 (gold 58.4, human 49.2) | d01 | established (K16) |
| Scaffolds give small gains on emergent properties | CCPT GPT-4o induction: base 40.8, CoT 42.4, spreading activation (LLM) 43.8, (ConceptNet) 45.8, (both) 45.2. Gain about +5; CoT about +1.6 | d01 (corrects b23, c19) | single (K05) |
| LLMs recognise better than they produce | GPT-4o "has property" 95.6%, "lacks property" 69.6%. Property-type labelling 56.4% vs human 81% (emergent 90.0%, component 37.2%, canceled 45.2%). Noun-phrase completion base 20.4 (human 38.0, gold 59.9) | b23, b24, c18 | single (K17) |
| Explicit shared-attribute step helps image mashups | IEI beat the shorter two-step prompt for all 5 image models (Friedman p<0.0001). Midjourney mean rank 1.98 vs 2.40. Prompt length 514.53 vs 487.95 words, p=.404. Win rate vs experts .26 to .35 | b22, c13 | single (K05) |
| VLMs identify blends better than people but trail experts on implication | GPT-4o identification P/R 75.67/85.00 vs people 53.42/70.33; explanation 74.19 vs 69.89; implication win rate 73.5 vs people 51.0, experts 78.3. Claude-3.5-Sonnet 60.08/74.83, 74.19, 62.9. Claude-3-Opus implication 39.2. 11 VLMs | b21, c12 | single |
| Staged schema agent beats a strong single prompt (human ratings, images) | 100 participants, 45 images per method. Ingenuity: Direct 2.75, Strong prompt 3.69, w/o transfer agent 3.71, w/o diagnostic 4.05, Full 4.56. Recognizability 4.47 vs 3.62. Preferred over GPT-Image 64.44%, Banana-pro 67.11%, Midjourney 72.89%, BAGEL 76.22% | c16, c17 | single (K05, K06) |
| Replacement blends are hard | VMetaphor-Bench, 1,500 images, 11 models: replacement 18.9% vs fusion 67.9%, juxtaposition 69.2%. Naming the structure adds 3.1 to 16.6 points. Top model 85.4 MCQ | b28 | established (K18) |
| Input weighting and order matter | Stable Diffusion 1.4, 1,000 image sets: blended depiction 0.621 at midpoint, 0.389 over all ratios, extremes about 0.14-0.26. Separate test, 100 adults, 22 pairs: embedding interpolation worst; first concept dominates | a15, c23, b27 | established (K19) |
| Judges of blend quality are weak | KOMBINE judge panel vs one human: 66% overall, 75% when unanimous (n=96; 60 items, 150 judgments). ICC 0.48-0.67; blend emergent utility 0.48. PopBlends annotators kappa .43. LLM judges of research ideas 43.3-53.3% vs human reviewers 56.1% | b20, a12, b26 | established (K14) |
| Putting two concepts in one prompt is not integration | Fused vs non-fused prompt: no significant difference in elicited tone (GPT-4o n=15, Gemini 2.5 Pro n=5); both beat control p<.05/.01 | c21 (Sato 2504.21012) | single (K15) |
| Temperature is a weak creativity lever | Llama-2-chat 70B: novelty beta .308 (SE .138), incoherence beta .240; no effect on typicality or cohesion. 36 raters, 31 stories | d07 | single (K24) |
| Structured protocol vs brainstorming, one case | 74/80 vs 49/80 (AI judge; author scores 75/80 vs 64/80). Batch of 8 random pairings: 7 of 8 judged successes, no baseline | d08 | single, weak (K25) |
| Code gate on cross-domain bridges | Preservation F below 0.30 rejected. Funnel 13,951 gate-passed, 163 cross-domain judged, 9 survivors (about 17:1). No human agreement measured | d09 | single (K26) |
| Multi-level analogue retrieval before recombining | Similarity to the real follow-up paper: 0.85 vs 0.78, 0.83 vs 0.75, 0.87 vs 0.77. 87 papers, Claude-3.5-Sonnet. Embedding similarity only | b25, c15 | single (K21) |
| Interactive blending tool, developers | 14 developers, 103 operations: global blend 36 (34.95%), drag-and-drop 35 (33.98%), regenerate 19 (18.5%). Satisfaction 3.2/5 (SD 1.3); 28 of 103 neutral | a24, c22 (Misty) | single |
| Analogy and recombination on task outcomes (not blending) | Thought Propagation: +12% optimal shortest paths, +15% agent planning (abstract). Discovery by Dreaming (training): GSM8K +14.5 pp, CI +9.8 to +18.7 at rank 256; putting the material in context to a 671B model did not reproduce it | d10, d11 | single (K27) |

## 4. Mechanisms and models

Each is explained so that an engineer can build it. Status is in sections 5 and 7.

### 4.1 The four-space network as a data structure
```
Input1 = {entities, roles, relations}      Input2 = {...}
Generic = abstract frame G such that Input1 and Input2 both instantiate G
Mapping = pairs (x in Input1, y in Input2) licensed by G
Blend   = selected subset of Input1 + Input2, mapped pairs fused or kept distinct
Emergent = relations in Blend that are in neither Input
```
The data structure is easy. The hard step is finding G (K02). Everything after G is cheap and works (97.1% coherent).

### 4.2 Three-step emergence
1. **Composition.** Put projected parts into one scene. Fuse mapped pairs (one day, one path) or keep both (two monks).
2. **Completion.** Match the scene against stored frames and add missing parts (the monks meet).
3. **Elaboration.** Run the scene and read off what follows (they debate identity).

For an LLM these are three separate calls, each given the state from the one before.

### 4.3 The two-stage split that the data support
Evidence for the split: valid generic space 43.4% vs coherent blend 97.1% (c02); PopBlends bridge right 56.7% vs scene on-topic 98.3% (c07, c08); Ge and Parikh 2021 found the find-the-shared-property step is the limiting step and improves with model scale (c10, a14).

Recipe:
1. Stage A: generate K candidate generic frames (K about 5; PopBlends shows 90-97% have at least one good one in five).
2. Check each frame by code or a blind second call (4.5).
3. Stage B: expand the best frame into a blend (composition, completion, elaboration).
4. Check the emergent claim (4.6). Keep the blend only if it passes.

### 4.4 Blend type is a parameter
Tell the operator whether to fuse, juxtapose or replace. Replacement is much harder (18.9% vs 67.9-69.2%), and naming the structure helps (+3.1 to +16.6 points) (b28). Image evidence only.

### 4.5 A three-part code check of a generic frame (not yet validated, K26)
- Non-empty: the frame states at least one relation, not just a category word.
- Covers both: each input's property list contains at least one instance of the frame.
- Not vacuous: the frame is not true of almost any pair (test it on 5 random unrelated inputs; reject if it fits most).

The nearest published check is a typed-structure functor-preservation gate with a 0.30 reject line (d09). Its human agreement is unmeasured.

### 4.6 Emergent-claim check
Generate the two input property lists first, before blending. The claimed emergent property must be absent from both lists and not a restatement of a listed property. Run the check as a separate call that sees only the claim and the two lists. Reason: LLMs judge "has property" well (95.6%) but type properties poorly (56.4%) and generate emergent ones weakly (b24, c18). Humans also over-claim emergence: most apparent emergence is recall of instances or category stretching (K07).

### 4.7 Order and weight test
Run the blend in both input orders. Reject blends where one input supplies all properties. Image models show strong first-input dominance and order sensitivity (b27, a15). Not shown for text; the test is cheap.

### 4.8 Why "explain it" may matter
People produce more emergence when they must explain an incongruent pair: they recall a case, apply a rule or simulate (b04, K08). The text analogue is asking "how could these two coexist" instead of "merge these". Untested in LLMs.

### 4.9 Goal-selected blending
Human blends are goal-selected (Lynn 2026; a21). Operationally: state the goal and the needed affordances, blend, test against the goal, revise from the failure. Conceptual proposal only (K23).

### 4.10 Dedupe before selection
Model samples repeat (K03, K04). Dedupe candidate blends by embedding similarity in code before ranking, then spend the budget on distinct ones.

## 5. What holds up

### 5.1 Holds (established)
- **Emergence is rare in plain conjunction.** Hampton 1987, 1989 and Hampson 1990: three lines (K07). It rises when the pair is incongruent and the reader must explain.
- **The abstraction step is the bottleneck, not the building.** Three sources: KOMBINE, PopBlends, Ge and Parikh (K02).
- **Sample several bridges and filter.** Best-of-5 lifted 56.7% to 93.3% (PopBlends) and 40.8 to 57.8 (CCPT) (K16).
- **Model samples collapse in diversity** (Si et al., KOMBINE) (K04).
- **Model judges are weak on blends and ideas** (4 sources) (K14).
- **Replacement is hardest** (2 sources) (K18).
- **Input weight and order change the blend** (image models, 2 sources) (K19).
- **Metaphor costs processing time, graded by conventionality** (Coulson and Van Petten; Lai et al.), but this does not prove the four-space mechanism (K11, K12).
- **Blending theory is not a falsifiable algorithm** (4 critics, and Turner concedes) (K13).

### 5.2 Single-source (do not rely on yet)
KOMBINE's headline numbers are one paper, with a judge panel validated by one human rater (66% agreement). The 14.3x homogeneity figure is at two shared properties; at one or more it is 94.7% vs 36.3%, about 2.6x. Also single: PopBlends user study (N=10), IEI (images, GPT-4o judge), Beyond Pixels (authors' own ablation, 45 tasks), CCPT scaffold gain (+5), the Fujiyoshi protocol case.

### 5.3 Failures, nulls and negative results
- **Sato fused vs non-fused prompt:** no significant difference (c21). Merging two ideas in one prompt is not integration.
- **Far inputs:** no direct benefit in Chan, Dow and Schunn (-0.33 log-odds), none in Kennedy (N=195), and KOMBINE's random unrelated pairs gave mostly invalid blends. Estes and Ward and Wilkenfeld and Ward report more emergence for far pairs, but only abstract-level or second-hand sources were reached (contested, K09).
- **Embedding interpolation** is the worst blending method in one test (b27). Another finds the midpoint is where blends peak (a15). Both agree one input dominates.
- **In-context use of recombination** did not reproduce the training gain and reversed it for a 671B model (d11).
- **Temperature** moves novelty only a little (beta .308) and also adds incoherence (d07).
- **ERP support** for blending is matched by other accounts (K12).
- **Chain-of-thought** added only about +1.6 on emergent induction (d01).

### 5.4 Moderators
- Congruence and demand to explain raise emergence (b04).
- Point of view shifts inheritance: 17% vs 69% (b05).
- Blend type: replacement vs fusion (b28).
- Property type: LLMs do emergent 90.0%, component 37.2%, canceled 45.2% (b24).
- Domain: PopBlends traits adjectives 79%, activities 58%, catchphrases 35% (c08); scenes product 89.1% vs pop culture 75.9%.
- Model: the best blender differs from the best on association and analogy (K22). Same-provider models repeat each other 2.3x more.
- Input order and weight (image models).

### 5.5 Interventions that worked (with the caveat)
- Best-of-N with a filter (strong, multiple sources).
- Naming the blend type (+3.1 to +16.6 points, images).
- Explicit shared-attribute step for image mashups (rank gain at matched prompt length).
- Staged schema agent over a strong single prompt (images, human ratings, not equal tokens).
- Multi-level analogue retrieval (thin).
- Human-LLM co-creation tool: PopBlends users produced 2.03 vs 0.87 ideas per pair (N=10).

### 5.6 Interventions that did not work, or are untested
- Merged-prompt "fusion" without structure: null.
- Higher temperature as a source of valid blends: weak.
- Far sources by default: null or negative.
- Untested: retry or a second model on the generic-space step; optimality principles as a score; expert cases with an explicit generic step (K29).

## 6. Language models

### 6.1 How LLMs behave
- **Blending is the weakest of three combinatorial skills.** 35 LLMs: 59.0 / 53.4 / 43.4% (association / analogy / blend); gap 10-16 points. The skills correlate (r=0.71 association-analogy, 0.70 analogy-blend, 0.54 blend-association), so a good analogy model is usually a good blender (c05). The leader changes: gpt-5.6-sol on blends (64.8), claude-opus-4.6 on association and analogy.
- **LLMs beat the Prolific humans** on all three tasks (59.0 vs 22.1; 53.4 vs 32.9; 43.4 vs 12.8), partly because humans skipped items. Humans and models sit in different semantic regions.
- **The failure is before the blend.** Valid generic space 43.4%. Given one, 97.1% coherent. Example: Photosynthesis + Bread, where only one frontier model found a valid generic space; others gave a bread-only schema. Every item was blended validly by at least one model, so none was impossible.
- **Homogeneity.** One in five invented concepts repeats another model's. Blends repeat far more than analogies: 37.3% vs 2.6% at two shared properties.
- **Recognition beats generation.** On CCPT, GPT-4o judged "has property" 95.6% but generated emergent noun-phrase completions at 20.4 (human 38.0, gold 59.9) and property induction at 40.8 (human 49.2, gold 58.4).
- **Novel combinations are where models follow humans least.** GPT-3 matches human compound interpretation, but fails when nonce words carry the category (d13). Embeddings track human plausibility less for novel compounds (d14, abstract only) (K28).
- **Visual blends.** VLMs beat average people at spotting the inputs (75.67/85.00 vs 53.42/70.33) and trail experts on implication (GPT-4o 73.5 vs experts 78.3). Image generators know the domains but fail at structure and mapping, especially replacement (18.9%).

### 6.2 What changed the result, and by how much
| Lever | Change | Source | Caveat |
|---|---|---|---|
| Best of 5 with an oracle filter | 56.7 to 93.3% (PopBlends); 40.8 to 57.8 (CCPT) | c07, d01 | oracle row is an upper bound |
| Spreading-activation scaffold | +5.0 (40.8 to 45.8) | d01 | one model family |
| Chain-of-thought | +1.6 | d01 | |
| Explicit shared-attribute step (IEI) | mean rank 2.40 to 1.98 | c13 | images, GPT-4o judge |
| Staged schema agent vs strong single prompt | ingenuity 3.69 to 4.56 | c17 | not equal tokens |
| Naming blend structure | +3.1 to +16.6 | b28 | images |
| Retrieval at several abstraction levels | similarity +0.07 to +0.10 | c15 | embedding only |
| Higher temperature | novelty beta .308 | d07 | Llama-2 stories |
| Model choice | 43.4 mean vs 64.8 best | c01 | |
| Interactive tool (PopBlends) | 2.03 vs 0.87 ideas per pair | c09 | N=10 |

### 6.3 What is missing
- No arm of "plain combine A and B" vs "structured blend" at equal tokens exists (K25). Closest: 74/80 vs 49/80 in one case, AI judge.
- No task-outcome test of a blend operator (K27). Analogy gives +12% / +15% on gold tasks, but that is analogy.
- No code check of a generic frame with human agreement (K26).
- No retry or second-model test on the generic-space step (K24). KOMBINE tested only temperature 0.9.
- Judges are LLMs in KOMBINE, CCPT, CreativeMashup and VMetaphor. The one human check of KOMBINE is a single rater.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | In open mode, split the combine operator in two calls: state a generic frame first, then blend. The weak step is the frame (43.4% vs 97.1%). No new operator; it makes O7 and open-mode S3 two calls. | O7, O2, S3 (open) | [E] | K02: a16, a13, b19, c02, c07, c10 |
| 2 | Draw several candidate frames or bridges (about 5), filter in code, expand only the best. | S3, G12 | [E] | K16: a12, c07, c09, d01 |
| 3 | Dedupe candidate blends by embedding similarity in code before selection; budget for distinct ones. | G4, G8, S7 | [E] | K04: b26, a17, b19 |
| 4 | Do not select blends by a model's opinion. Select by code checks and running; log how often a blind judge agrees. | G5, G8 | [E] | K14: b20, b26, a12, a20, a16 |
| 5 | Require every claimed emergent property to be absent from both input property lists, checked in a separate call. Never accept the model's own rating of a novel blend. | G2, G5 | [E] (principle) | K07, K28: b01-b03, d13, d14 |
| 6 | Tell the operator the blend type (fuse, juxtapose, replace). Expect replacement to fail more. | O7 | [E] (images) | K18: b28, c12 |
| 7 | Run the blend in both input orders; reject one-input-dominates blends. | O7 | [E] (images; text unknown) | K19: a15, c23, b27 |
| 8 | Keep blend as an impasse and open-mode operator only. Do not apply it to routine problems. Do not claim the four-space structure is the mechanism. | G1, G8, G10 | [E] | K13, K09: a07-a09, b10, b11 |
| 9 | Do not cite ERP data as proof of the four-space mechanism. Treat input distance as a controlled variable. | none | [E] | K11, K12 |

Note: items 5, 6 and 7 are established as facts about the failure (human emergence is rare; replacement is hard; order matters). The checks themselves are untested. They are cheap guards, so add them and measure them.

### Test first (not yet added)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Structured blend (frame, blend, check) vs plain "combine A and B" at equal tokens. The central missing arm. | O7, G7 | [S] | K05, K20, K25: d08, c13, c17 |
| T2 | Three-part code check of the generic frame vs two human raters. | G5 | [S] | K26: d09 |
| T3 | Distance sweep of input pairs: near, moderate, far. Far inputs only at impasses. | O7 | [C] | K09: d02, d03, b14-b17 |
| T4 | Build on a blend with one refinement round vs a one-shot far blend. | S3, S5 | [S] | K10: b14, d04 |
| T5 | "How could these coexist" vs "merge these". | O7, O8 | [S] | K08: b04, b05 |
| T6 | Goal and affordances stated first, then blend, test, revise. | S1, S4 | [S] | K23: a21, b29 |
| T7 | Temperature sweep, retry, or second-family model on the frame step. | G5 sampling | [S] | K24: d07, d16 |
| T8 | Blend operator on a gold-answer task (ARC-like or design puzzle). | S-open | [S] | K27: d10, d11 |
| T9 | Template vs template plus diagnose-and-retry. | G7 | [S] | K06: c17 |
| T10 | Multi-level retrieval of the generic frame. | O2, O7 | [S] | K21: b25, c15 |
| T11 | A separate model for the blend operator. | G7 | [S] | K22: c05, a18 |
| T12 | Lessons in memory: record which pair types and blend types worked, by class. | M | [S] (inference) | K22; schema memory rules |

## 8. Concrete tests on our bench

All arms get the same total token budget per item, including setup and checks (G7). Judges are code checks or blind second calls. A blind human sample of 50 to 100 is scored in every test.

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | 100 random concept pairs (KOMBINE-style) | plain "combine A and B"; chain-of-thought; frame-then-blend-then-check; best-of-5 with code filter | Valid-blend rate by code check plus blind human sample; emergent property absent from both input lists | Structured +5 to +15 points over plain; best-of-5 largest (CCPT: +5 scaffold, +17 best-of-5) |
| B2 | Same 100 pairs, frame step only | temperature 0.3 / 0.7 / 1.0; one model vs second family; retry up to 3 | Valid-frame rate; cost per valid frame | Retry and second family beat temperature; temperature gives small shifts |
| B3 | 100 pairs, 10 samples each | same-model repeats vs different input pairs sharing a frame | Distinct emergent properties per 1,000 tokens (embedding threshold) | Dedupe raises unique yield about 2x |
| B4 | Pairs binned by embedding distance (near, mid, far) | blend arm at each bin | Validity and downstream usefulness | Far has more invalid blends; mid best on usefulness; no gain from far on routine items |
| B5 | 50 incongruent pairs | "merge" prompt vs "how could these coexist" | Emergent-claim validity | Small gain (single human source) |
| B6 | 100 blends | code frame check vs two human raters | Agreement (kappa), false-negative rate | Need kappa 0.6 or more to trust the check |
| B7 | ARC-like or design puzzles with a gold answer, items where plain pass rate is low but above zero (G12) | no blend; blend operator at impasse; best-of-N | Pass rate at equal tokens | Gain only on items with a foothold; none on easy items |
| B8 | Blends | one-shot; one refinement round against a check | Validity of final blend | Refinement helps (human data on iteration) |
| B9 | Blends in both orders | with and without order-dominance rejection | Share where one input supplies all properties; validity after rejection | Rejection removes a visible fraction (text size unknown) |
| B10 | Blends with type tags | untagged vs fuse / juxtapose / replace | Validity per type | Tag helps replacement most |

## 9. What does not transfer, and why

- **The four-space network as a claim of mechanism.** No experiment manipulates the generic space; the theory has no single testable hypothesis (K13). We borrow the checkable outputs only.
- **ERP and reaction-time data** (Coulson and Van Petten, Lai): brain cost of metaphor, not agent output quality. They also fit other accounts (K12).
- **Hampton's conjunction results**: two-word concepts and human recall. They are a guard (check emergence claims), not a recipe.
- **Image-model results** (IEI, Beyond Pixels, Stable Diffusion interpolation, VMetaphor): the generator is a diffusion model or VLM. Embedding interpolation does not apply to text prompts. The staged agent also was not tested at equal tokens.
- **Lexical blends** (Wulff and Gries): portmanteau word formation, weak effects (R2 0.05).
- **Tone effects** (Sato): no integration effect shown.
- **Far analogies as a default.** Human field data say far sources do not beat citing nothing, and KOMBINE's random pairs gave mostly invalid blends. Far inputs belong at impasses and open mode only.
- **"LLMs beat humans" on KOMBINE.** The humans were Prolific lay people with skips scored zero. It says nothing about expert designers.
- **Interactive tools** (Misty, PopBlends UI): rely on a person to pick. Our agent has no human in the loop (G5).
- **"Creative" judge scores** (Si et al.: AI ideas more novel, not more feasible): G8 forbids a model judge as the final selector.
- **Training-based recombination gains** (Discovery by Dreaming): the in-context version failed to reproduce them.

## 10. Open questions

1. Does frame-then-blend beat plain "combine A and B" at equal tokens on any measured outcome? (K25.)
2. Does a blend operator raise accuracy on a gold-answer task? (K27.)
3. Can code check a generic frame with human-level agreement? (K26.)
4. What input distance gives the best usefulness for text blends in LLMs? (K09, contested.)
5. Do retry, a second model family or lower temperature fix the 43.4% generic-space step? (K24.)
6. Do blends from different input pairs that share a frame give more distinct emergent properties than repeated samples for the same pair? (K03.)
7. Do the optimality principles (topology, unpacking) work as automatic scores that track human value judgments? Only a proposal poster exists (K29).
8. Do expert blends later judged valuable show an explicit generic-space step? (Left to the discovery case studies subfield.)
9. Has Hampton's emergence result been replicated since 2010, including with LLMs? We found no direct replication (K28).
10. Do Gibbs (2000), Coulson and Matlock (2001), McCubbins and Turner (2013), Eppe (2018), Estes and Ward (2002) and Wilkenfeld and Ward (2001) hold numbers that change any of the above? Not opened (K29).
11. Is the abstraction bottleneck caused by missing experiential knowledge, as KOMBINE suggests? That explanation was not tested.
12. Does first-input dominance, seen in images, also appear in text blends?

## 11. Sources

[V] = opened (page or PDF text read in this series); [M] = snippet or abstract only. Evidence ids in brackets.

**Theory and criticism**
- [V] Fauconnier and Turner (1998), Conceptual integration networks. https://www.neurohumanitiestudies.eu/archivio/SSRN-id1292966.pdf (a01-a04)
- [V] Grady, Oakley, Coulson (1999), Blending and metaphor. https://markturner.org/blendaphor.html (a05)
- [V] Ritchie (2004), Lost in conceptual space. https://web.pdx.edu/~cgrd/Metaphors%20of%20Conceptual%20Integration.html (a07, a08)
- [V] Turner (2013), Challenges to blending theory. https://markturner.org/ChallengesToBlendingTheory.html (a09, b11)
- [V] Glebkin (2013), A critical view on conceptual blending theory. https://escholarship.org/uc/item/95p302sj (b10)
- [M] Gibbs (2000/2001), Making good psychology out of blending theory. https://doi.org/10.1515/cogl.2001.020 (a28, b12, d17)
- [M] Coulson and Matlock (2001). https://benjamins.com/online/emetbib/publications/3697 (a29, d17)
- [M] Fauconnier and Turner (2002), The Way We Think (book). https://markturner.org/blendaphor.html (a30)
- [M] Ferguson and Sanford (2008). https://kar.kent.ac.uk/23060/ (b13)
- [V] Lynn (2026), Conceptual blending in humans and language models. https://pmc.ncbi.nlm.nih.gov/articles/PMC13461484/ (a21, b29, d15)
- [V] Xi, Cheng, Soni, Turner (2026), poster. https://markturner.org/ACL2026_Conceptual_Blending_Poster_compressed.pdf (a22, b31, d18; c26 snippet)

**Human experiments**
- [V] Hampton (1996), Emergent attributes in combined concepts; reviews Hampton 1987 and 1989, Hampson 1990, Hastie et al. 1990, Kunda et al. 1990. https://www.staff.city.ac.uk/hampton/PDF%20files/Creative%20concepts%201996.pdf (b01-b05)
- [V] Coulson and Van Petten (2002). https://link.springer.com/content/pdf/10.3758/BF03195780.pdf (a06; b07 landing page [M])
- [V] Lai, Curran, Menn (2009). https://www.colorado.edu/lab/curran-lab/sites/default/files/attached-files/ (b06; URL truncated in evidence file)
- [M] Frontiers in Human Neuroscience (2015), ERP stimulus-control review. https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fn (b08; URL truncated)
- [V] Wulff and Gries (2019). https://journals.openedition.org/lexis/3625 (b09)
- [V] Chan, Dow, Schunn (2015/2018). https://doi.org/10.1007/978-3-319-91134-2_12 (d03)
- [M] Chan and Schunn (2015). https://www.lrdc.pitt.edu/Schunn/papers/Chan-Schunn2015-Cognition.pdf (b14); https://doi.org/10.1111/cogs.12127 (d04)
- [V] Kennedy (2015) thesis. https://ir.ua.edu/handle/123456789/2546 (b15, d02)
- [M] Estes and Ward (2002). https://doi.org/10.1207/S15326934CRJ1402_2 (b16, d05)
- [M] Wilkenfeld and Ward (2001). https://doi.org/10.1006/jmla.2000.2772 (b17, d06)
- [V] Peeperkorn et al. (2024), temperature and creativity. https://arxiv.org/abs/2405.00492 (d07)

**Computational blending**
- [V] Eppe et al. (2015). https://www.inf.unibz.it/~okutz/resources/LPNMR15-asp-amalgamation-concept.pdf (a10)
- [M] Eppe et al. (2018). https://doi.org/10.1016/j.artint.2017.11.005 (a11)
- [V] McCaig, DiPaola, Gabora (2016). https://arxiv.org/pdf/1610.02478 (a26)
- [V] Topological group generation (2021). https://arxiv.org/pdf/2112.02457 (a27)
- [V] Veale, O'Donoghue, Keane (2000), Sapper. https://www.cs.ucd.ie/ (c25; URL truncated)

**LLM and AI studies**
- [V] Schapiro, Jagadish et al., KOMBINE. https://arxiv.org/abs/2509.21043 (a16-a18, b18-b20, c01-c06, d16)
- [V] Wang, Petridis et al. (2023), PopBlends. https://arxiv.org/abs/2111.04920 (a12, a13, c07-c09)
- [V] Ge and Parikh (2021). https://arxiv.org/abs/2106.14127 (a14, c10, c11)
- [V] Song et al. (2025), CCPT, "Is a peeled apple still red". https://arxiv.org/abs/2502.06086 (b23, b24, c18, c19, d01)
- [V] Peng et al. (2025), CreativeMashup / IEI. https://arxiv.org/abs/2504.13120 (b21, b22, c12-c14)
- [V] Xu et al. (2026), Beyond Pixels. https://arxiv.org/abs/2602.01335 (a23 abstract only, c16, c17)
- [V] Matsuhira et al. (2024). https://arxiv.org/abs/2411.03595 (a15, c23)
- [V] Olearo et al. (2026). https://arxiv.org/html/2506.23630 (b27)
- [V] VMetaphor-Bench (2026). https://arxiv.org/html/2609.02502v1 (b28)
- [V] Sun et al. (2025), Creative Blends of Visual Concepts. https://arxiv.org/abs/2502.16062 (c24)
- [V] Lu et al. (2025), Misty. https://arxiv.org/abs/2409.13900 (a24, c22)
- [M] IT-Blender (2025). https://arxiv.org/pdf/2506.24085 (a25)
- [V] Sato (2025), Waking up an AI. https://arxiv.org/abs/2504.21012 (a20, c21)
- [V] Sato (2025), The way we prompt. https://arxiv.org/abs/2505.10948 (a19, b30, c20)
- [V] Gu et al. (2025), combinatorial creativity. https://arxiv.org/abs/2412.14141 (b25, c15)
- [V] Si, Yang, Hashimoto (2025). https://arxiv.org/html/2409.04109v1 (b26)
- [V] Fujiyoshi (2026). https://arxiv.org/abs/2604.09597 (d08)
- [V] Wang and Luan (2026). https://arxiv.org/abs/2608.20361 (d09)
- [M] Yu, He, Ying (2024), Thought Propagation. https://arxiv.org/abs/2310.03965 (d10)
- [V] Zahn, Evans, Eagleman (2026), Discovery by dreaming. https://arxiv.org/abs/2607.16256 (d11)
- [M] Radensky et al. (2024), Scideator. https://arxiv.org/abs/2409.14634 (d12)
- [V] Li, Carlson, Potts (2022), GPT-3 and novel compounds. https://arxiv.org/abs/2210.09492 (d13)
- [M] Ciapparelli, Zarbo, Marelli (2025). https://doi.org/10.1111/cogs.70048 (d14)
- [M] Search-limits note for Hampton replications and expert cases. https://arxiv.org/search/ (d19)

Source-quality notes: b23 misread CCPT (corrected in d01); a20 under-reports Sato's null; Hampton results come from his 1996 review, not the original papers; Si et al. is not a blending test. Evidence a, b and c overlap on KOMBINE, PopBlends, IEI and CCPT; claims count each paper once.
