# Blend network types: deep document

*Subfield F01.03 (cognitive linguistics). Sources: evidence_a-d.jsonl (ids a01-a26, b01-b29, c01-c27, d01-d16), claims.jsonl (K01-K23), critique.md. Schema parts: G guardrails, S states, O operators, memory (SCHEMA.md v0.2). Status marks: [E] established, [S] single source, [C] contested.*

**Headline.** The four network types are a descriptive typology built from hand-picked examples. No study found varies the type and measures an outcome, in humans or in language models. "Use double-scope for novel ideas" is an untested design hypothesis. What does have evidence is nearby: a staged "how do the inputs combine" step (image tasks), finding a valid shared structure (the bottleneck for LLMs), code doing the combining, and checking every borrowed role afterwards.

## 1. What it is

Conceptual integration (blending) theory says that when we understand a combined idea, we run a network of mental spaces. Two input spaces hold the two things being combined. A generic space holds what they share. A blend space takes selected parts of both and adds new structure of its own.

A network "type" says how the organizing frames of the inputs relate to the blend. From Fauconnier and Turner (2003, opened, d04):

- **Simplex.** One input is a frame with roles. The other holds specific elements (values). The blend fills the roles with the values. Example: a "buying gasoline" frame; "He threw the ball over the fence" as role-value mapping.
- **Mirror.** One organizing frame is shared by all spaces (both inputs, generic space, blend). Example: the Buddhist monk riddle (one path, two journeys).
- **Single-scope.** The two inputs have different organizing frames. The blend inherits only one of them. Example: boxing blended with business competition (Murdoch knocked Iacocca out); the boxing frame organizes the blend.
- **Double-scope.** The inputs have different, often clashing frames. The blend takes essential frame structure and identity properties from both and builds new emergent structure. Examples: complex numbers, the computer desktop, "dolphin-safe" and "shark-safe".

The authors call these prototypes on a continuum, not strict boxes (d04). They tie double-scope blending to human creativity and call it "universal for our species" (d05). The 1998 paper does not use the four names (zero hits in the full text). It used older labels: frame networks, one-sided networks, two-sided networks (d02). The four names come from the 2002 book. That book chapter was not opened here; every statement about types comes from the 1998 and 2003 papers and Wikipedia.

Why it matters for our agent: the schema has operators for combining ideas (O3 decompose, O7 map an analogue, O8 reframe) and an open mode that needs novel ideas. The question is whether "choose a network type before combining two frames" is a useful operator. Honest answer today: the label is unproven. The pieces around it (check shared structure, make the combine step explicit, test borrowed roles) have some support.

## 2. History and theories in depth

**Roots.** Fauconnier's mental spaces and conceptual metaphor theory led to Fauconnier and Turner, "Conceptual Integration Networks" (Cognitive Science 1998, 22(2):133-187). It gives a four-space model with selective projection and a list of optimality principles: integration, topology, web, unpacking, good reason (relevance), metonymic tightening (a02, a03, d02). It reports no experiment. Examples are chosen by the authors: Regatta, Debate with Kant, Buddhist monk (frame networks); boxing business competitors (one-sided); computer desktop (two-sided) (d02).

**Typology and the novelty claim.** In the 1998 paper, two-sided networks give more chance of non-optimal blends and of clashing optimality principles, and also the opportunity for creativity. Complex numbers is the main worked case; Fourier, Maxwell and Faraday are named as further cases (d03, K20). So the founders themselves call double-scope double-edged. The 2002 book (The Way We Think) and the 2003 paper push the stronger line: double-scope is the cognitively modern, creative form (a23, d05). Turner's 2014 book repeats it. Neither book was opened for numbers; both argue from examples.

**Defence and expansion.** Coulson and Oakley (2000, a03) is the primer by the main experimental advocate. It says the optimality constraints are selective and often conflict. It reports Veale and O'Donoghue's Sapper (a05, a25) and Grady's proposal that spreading activation implements "completion" (a06).

**Critique.**
- Gibbs (2000, secondary only, a09): blending is a framework, not a testable theory; it infers process from products; it explains everything so predicts nothing.
- Ritchie (2004, secondary only, a10): many blends can be explained by simpler integration; the Buddhist monk example has alternative accounts.
- Coulson and Oakley accept that analysis must move past post hoc work but defend the approach (a04). Fauconnier is reported to have answered the critics (b02).
- Wikipedia lists no direct empirical test of the four types (b03). An arXiv search for "double-scope" returned zero papers (b28, c21).

**Human experimental line.** Coulson and colleagues turned the "same process for literal and figurative" claim into ERP and norming tests (section 3). These test integration effort, not network types. Rival theories (structure mapping, career of metaphor, relevance theory) predict the same graded N400, so the data do not favour blending over them (b07).

**Computational line.**
- Sapper, COINVENT (Eppe et al. 2018) and Lieto and Pozzato's description-logic combination implement blending as search over generalisations, consistency checks and a score (a24, a25, d14, d15). Eppe et al. state the system has no empirical evaluation. Lieto and Pozzato give worked examples only.
- Formal blending in category theory built the concept of a topological group from topology and group theory: one worked example (b29, c18).
- Gomez-Ramirez and Turner (2026 working draft, a12) propose formal blending with losses and benchmark design; no measured results.

**LLM line (2020-2026).** Work splits into (a) benchmarks of LLM blending (Kombine, Peng et al.), (b) scaffolds and tools (PopBlends, Xu et al., Misty, Dish COVER), (c) diffusion-model blending (Matsuhira, Olearo, Cho), (d) position papers (Sato 2025, Lynn 2026, Lippolis et al. 2025, Xi et al. 2026 poster). None manipulates the Fauconnier and Turner type as a variable.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Four types defined as prototypes on a continuum; 1998 paper used frame/one-sided/two-sided | no numbers; worked examples | F&T 2003, 1998 (d02, d04); K01 | [E] (definition) |
| No study varies network type and measures an outcome | arXiv "double-scope": 0 hits; Xi et al. 2026 poster: rubric only, no scores; Birdsell 2019: 34 asked, 25 usable drawings, 5 analysed qualitatively | b28, c21, d01, d16; K02, K23 | [E] (gap exists, within search limits) |
| Integration effort rises with mapping demand (human, ERP) | N=18; N400 sentence-type effect F(2,34)=3.90, p<.05; metaphor vs literal F(1,17)=6.86; linear trend F(1,17)=6.86, over 98% of variance; 74% of literal-mapping sentences involved pretense, lying or mistaken identity | Coulson and Van Petten 2002 (a07, a26, b04); K03 | [E] |
| Graded N400 replicated; knowledge lowers cost | anomalous > novel metaphor > literal; engineers had smaller N400 for engineering metaphors; three-way interaction not significant; L2 users showed anomaly effect only | Jonczyk 2020, Miller 2025 (b05-b07); K03, K04 | [E] graded N400; [S] knowledge moderator |
| Rival theories explain the same N400 gradient | studies cited: Arzouan 2007, Lai 2009, De Grauwe 2010 and others | b07 | [E] (non-discriminating) |
| Context shifts feature sets toward the target (norming) | cosine to null-context set: literal 0.84, literal mapping 0.81, metaphoric 0.78; F(2,68)=5.48, p<.01; t=3.26 | Coulson and Matlock 2001 (a08) | [S] |
| LLMs worse at blending than analogy or association | valid outputs, 35 LLMs, temp 0.9: association 59.0%, analogy 53.4%, blend 43.4% | Kombine (a13); K05 | [S] |
| Bottleneck is the valid generic space, not building the blend | 97.1% coherent blend given a valid generic space | Kombine (a13, d09); K05 | [S] |
| Humans below LLMs on the same tasks | association 22.1% vs 59.0%; analogy 32.9% vs 53.4%; blending 12.8% vs 43.4%; 120 recruited, 75 kept; 5 items per task | Kombine (a15) | [S] |
| Model integration scores vary widely | "emergent integration" as % of max: top model 76.7, phi-4 3.3, humans 1.3 (model names as printed in the paper) | Kombine Table 10 (d08) | [S] |
| LLM blends are homogeneous | 2,070 invented concepts, 7,868 properties, threshold 0.674; about 1 in 5 (412/2,070 = 19.9%) repeats another model's property; blends reused 14 times more than analogies; same-provider 2.3 times more than cross-provider | Kombine (a16); K11 | [E] (with d11) |
| Default GPT-4o juxtaposes instead of integrating | self-BLEU-2 0.929 (Exp 1), 0.912 (Exp 2); same-pair cosine 0.90; 24.98 ingredients vs 12.3 for Dish COVER | Dish COVER (d11); K17 | [E] (with Kombine "concatenation") |
| Code doing the combine raised judged novelty | Exp 1 (10 pairs, 50 recipes per model): novelty 3.53 vs 3.146 (p=0.0009); value 4.320 vs 4.326. Exp 2 (100 recipes each): 3.612 vs 3.141 (p=9.2e-8); valuable 85% vs 98%; 48 raters; alpha about 0.2 | Mizrahi et al. 2025 (d10); K16 | [S] |
| Bridge concepts: precision low, best-of-5 high | related to both domains 56.7% overall (56.0, 55.3, 58.7%); at least one good of five 90.0, 96.6, 93.3%; product scenes related 89.1% vs pop culture 75.9% (raw 80.0 vs 63.4); attribute IRR 0.32-0.47 | PopBlends (a17, b26, c01-c03); K06 | [S] |
| Bridge-concept tool doubled idea output | ideas per pair 2.03 (SD 0.84) vs 0.87 (SD 0.56), Wilcoxon p<0.001, N=10; mental demand 2.85 vs 5.80 (p=0.004); effort p=0.006 | PopBlends (b25, c03) | [S] |
| Models decode mashups above average people, below experts | implication win rate: experts 78.3, GPT-4o 73.5, GPT-4V 71.9, Gemini-1.5-Pro 71.7, Claude-3.5-Sonnet 62.9, average people 51.0, Claude-3-Opus 39.2; judge GPT-4o, 81.6 and 85.1% agreement with experts; 11 models, 666 mashups | Peng et al. 2025 (b14, c05); K08 | [S] |
| Fusion decoded better than replacement | fusion higher for 9 of 11 models and average people (bars read by eye; replacement higher for Claude-3.5-Sonnet 0.62 vs 0.59 and LLaVA-1.6-13B); the caption saying the reverse is an error; no significance test | Peng et al. (b15, c07, d06); K10 | [S] |
| IEI scaffold raised image quality at similar prompt length | Midjourney win rate vs experts 0.26 to 0.35; prompt length 487.95 vs 514.53, t=-0.84, p=0.404; IEI mean rank 1.98 vs II 2.40; rankings differ p<0.0001 | Peng et al. (b16, c06); K07 | [S] image, author metrics |
| Schema extract, transfer, diagnose, backtrack loop beat a one-shot blending-theory prompt | N=100; full system 4.47/4.56/4.51/4.74/4.76 vs strong one-shot 3.97/3.69/3.77/3.89/4.09 vs direct 3.62/2.75/2.96/3.75/3.65; pairwise wins 64.44, 67.11, 72.89, 76.22% vs four image systems | Xu et al. 2026 (b23, c08, c09); K07 | [E] by claim file (two image studies), but both author-built |
| Equal weighting of two inputs maximises blended depiction (diffusion) | ratio 0.5: BCD 0.621, MCD 0.862; all ratios 0.389 and 0.471; 3 of 4 methods order-sensitive; 100 raters, 22 pairs; Alternate vs Switch 51% (p=0.31) | Matsuhira, Olearo (a19, b17, b22, c13, c14); K09 | [E] |
| Interactive LLM blending output is imperfect | Misty N=14; 103 operations; mean satisfaction 3.2/5 (median 3, SD 1.3); 44 above 3, 28 at 3, 31 below 3; global blending 36 of 103; 5 of 14 (35%) agreed it expressed intent | Misty (a21, b20, c17); K14 | [S] |
| Ranking by unlikeliness beats raising temperature | 50 inputs x 150 outputs per temperature, temps 0.1-3.1; above temp 1, 85% had a new concept; at temp 3 over half still not unavailable to artists | Hernandez 2024 (c16, d07); K22 | [S] |
| Frame distance trades creativity against coherence | 1,000 GPT-4 vs 1,000 human metaphors; Fantasy creativity 4.8, coherence 3.8; Direct coherence 4.5, novelty 3.9; judged by GPT-4 and TF-IDF | Palamas 2025 (d13); K19 | [S] |
| Analogy recall before solving helps text reasoning | +4% average accuracy vs 0-shot and few-shot CoT (GSM8K, MATH, Codeforces, BIG-Bench; GPT-3.5, GPT-4, PaLM2); not equal tokens | Yasunaga et al. (d12); K18 | [S] |
| A code-side blend score exists, unvalidated | value = info + compression - imbalance if consistent, else 0; no empirical evaluation | Eppe et al. 2018 (d14); K21 | [S] |
| Text-to-image blending: LMs beat ConceptNet at properties | precision table garbled; do not use numbers; human study 6 questions x 3 pairs x 20 descriptions x 9 subjects | Ge and Parikh 2021 (a18, b11, b12, c04) | [S], numbers unusable |

## 4. Mechanisms and models

**4.1 The four-space network.** Data structure: inputs I1 and I2, each a set of frame roles and filled values; generic space G, the roles both share; blend B, a new structure with selected elements of I1 and I2 plus emergent elements. Selective projection: not everything is copied. Cross-space mapping: counterpart links between I1 and I2 elements, justified through G.

**4.2 Typology as a code-checkable decision (our reading, not validated).** Ask which input frame supplies the roles of the blend.
1. Extract the role set R1 of frame 1 and R2 of frame 2 (the model fills a slot; code stores them).
2. Count which roles in the blend description come from R1 only, R2 only, both, or neither (emergent).
3. Classify. One input has no frame, only values, and all roles come from the other: simplex. R1 and R2 are the same frame: mirror. Roles from one frame only, values from both: single-scope. Essential roles from both plus emergent roles: double-scope.
Expect boundary cases, since the authors call the types a continuum. Use agreement between two runs as a quality check (K01 agent test).

**4.3 Kombine's operational version (not the F&T typology).** Q in {1,2,3}: 1 if both inputs project structure (Kombine calls this single-scope), 2 if both also fill a shared slot (called double-scope), 3 if emergent structure appears. The judge prompt tags each triple as u (input 1), v (input 2), uv (shared slot) or emergent (a14, d09). Concatenation means u and v lines that never share a slot. Do not cite this as a test of the 2003 types (critique flag 5).

**4.4 Generic-space gate (proposed, untested).** Models do well given a valid generic space (97.1%) and poorly when they must find it (43.4% overall). Gate: the model proposes the shared slot; code checks that the slot has a value in each input (lookup, a second short call with a fixed question, or a test) before any blend is built. No paper tested this (d09).

**4.5 Code-side combination.** Dish COVER: the LLM parses each input into a tree; code computes a tree edit-distance blend, filters for value, ranks for novelty; the LLM writes it up (d10). Pattern: model fills slots, code recombines. This fits SCHEMA section 1 (the program decides, the model fills slots).

**4.6 Blend ranking score.** Eppe et al.: value(c) = infoValue(c) + compression(c) - imbalance(c) if consistent, else 0. Imbalance is half the absolute difference of information taken from the two inputs. Implement: count facts kept, compression, unequal contributions. Unvalidated (d14).

**4.7 Stage scaffolds.** IEI (Peng): identify inputs, explain how they combine, state the implication. Schema loop (Xu): extract schema (subject, carrier, relational invariant, violation, emergent meaning), transfer, diagnose, backtrack on failure (c08). Both put a "how they combine" step before generation; Xu also adds a critic.

**4.8 Ranking pairs by unlikeliness.** Hernandez: sample many candidate pairs, score each by how unlikely under a model of existing use and of human availability, keep the lowest co-occurrence that is still coherent (d07).

**4.9 Frame distance.** Palamas: Synectics types (Direct, Personal, Symbolic, Fantasy) set the distance; more distance gives more creativity and less coherence (d13). A different typology from F&T.

**4.10 Weighting.** In diffusion models, interpolation at ratio 0.5 gives the best joint depiction; heavy weight on one input collapses to it (c13, b22). Text analogue: when one input dominates, flag the blend as replacement-like (harder to decode in Peng).

## 5. What holds up

**Holds up (human).**
- Integration effort scales with mapping demand: replicated graded N400 (Coulson and Van Petten 2002 with N=18; Jonczyk 2020; Miller 2025; others in b07). Weakness: small N in the founding study; rival theories predict the same pattern.
- Prior knowledge lowers cost for novel metaphors: single-source; the three-way interaction was not significant, so the moderator is weak (b05).

**Not holding or untested.**
- No direct test of the four types exists. Wikipedia lists none (b03). Canovas and Manzanares (2014) mention blending 22 times and the four types 0 times (b08).
- "Double-scope produces novel ideas": support is the authors' own argument by examples, with no comparison group (d03, d05). The authors say two-sided networks are riskier (K20).
- Blending as a theory is criticised as post hoc and untestable (Gibbs 2000, Ritchie 2004). Treat the typology as a labeling heuristic.
- No code-side generic-space gate has been tested (d09). No human study codes real products by network type (K23).

**Moderators seen.**
- Thin frames: scene relatedness 89.1% for product vs 75.9% for pop culture (b26).
- Input weighting and order in diffusion models (K09).
- Temperature: more new combinations but unreliable (d07).
- Frame distance: creativity up, coherence down (d13).
- Cost of the code-combine approach: valuable share 85% vs 98% in Exp 2 (d10).

**Interventions that worked (single studies, author metrics).** IEI scaffold; schema loop with diagnose and backtrack; bridge-concept step; code-side combination; ranking by unlikeliness.

**Interventions with no benefit shown.** Raising temperature alone (d07). Free LLM blending in Misty (mean 3.2/5; 35% agreed it expressed intent). One-shot blending-theory prompts (3.97/3.69/3.77/3.89/4.09 vs the staged loop). Note SCHEMA 4b already rules out generic "be careful" prompts; a type label could become one if it adds length without a check.

**Judge risks.** Kombine used a 3-LLM panel (human-judge agreement 75%, n=96); Peng used GPT-4o to judge GPT-4o; Hernandez used GPT-4; Palamas used GPT-4 and TF-IDF. Self-preference could inflate results. This is why G8 says novelty is judged by running, not by model opinion.

## 6. Language models

**Baseline behaviour.**
- Blending is the hardest of three combinatorial tasks: 43.4% valid vs 53.4% analogy vs 59.0% association (35 LLMs, Kombine). Humans are lower (12.8%). Top integration score 76.7% of max; phi-4 3.3% (names as printed).
- The bottleneck is the generic space: 97.1% coherent blends given a valid one.
- Default blends juxtapose (Dish COVER: separate preparations joined at the end; self-BLEU-2 0.929) and are homogeneous (1 in 5 of 2,070 invented concepts repeats another model's; blends reused 14 times more than analogies).
- On decoding, not generating: GPT-4o 73.5 vs experts 78.3 vs average people 51.0 on implication; implication is the weakest step; fusion is easier than replacement for 9 of 11 models.

**What changed results, and by how much.**
- Stating "how the inputs combine" before generating (IEI): Midjourney win rate 0.26 to 0.35 at nearly equal prompt length (p=0.404). Images only.
- Staged schema loop with diagnosis and backtracking: 4.47/4.56/4.51/4.74/4.76 vs strong one-shot 3.97/3.69/3.77/3.89/4.09 (N=100). Confound: the loop uses extra calls; no equal-token control.
- Code-side combination: novelty +0.38 (3.53 vs 3.146) and +0.47 (3.612 vs 3.141); value equal in Exp 1, lower in Exp 2 (85% vs 98%).
- Bridge-concept step: 2.03 vs 0.87 ideas per pair; N=10 humans.
- Distance push: ranking by unlikeliness beats temperature; at temperature 3 over half of outputs were still not unavailable to artists.
- Analogical recall prompt: +4% average on text reasoning sets (not blending; not equal tokens).

**Not known.** No text-only reasoning test of a blend scaffold. No test that varies the type. Temperature and size effects on blend quality cannot be read from Kombine (one temperature, no Q split).

**Related subfields (not covered here).** Analogical prompting for LLMs, Analogy and distant sources, Mental spaces, Creative problem solving, Compression at inference time, Novelty measurement.

## 7. What our agent should take

Honest summary: little here is an established gain. The established items are about what not to rely on, and about checks.

### Add now (established)

1. **Treat the typology as a labeling heuristic, not a lever.** Schema part: O3 note only. [E] that no test supports the types as a lever and that critics call them post hoc. Evidence: K02, K13; d03, d05, a04, a09, a10. Do not add a "choose double-scope" rule to SCHEMA.md.
2. **Reject juxtaposition.** In open mode and O3/O7, reject any blend that can be split back into input A and input B with nothing lost; require at least one element that uses both frames. Schema part: G5 / S4 (code check). [E] as a failure mode (Dish COVER plus Kombine concatenation); the rule itself is a test candidate (U5). Evidence: K17; d09, d11.
3. **A model never selects its own novel blends.** Supports G8; blending papers add judge-risk cases (Kombine panel, GPT-4o judging GPT-4o). [E]. Evidence: K11 and the critique judge-risk list.
4. **Blends from one model are not independent.** Supports G4 and the isolated attempts in S3: 1 in 5 of 2,070 concepts repeated across models; blends reused 14 times more than analogies; same-provider 2.3 times. [E]. Evidence: K11; a16, d11.

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Fields "inputs / how combined / implications" plus a critic with backtrack before the answer, open mode | O3 / S3 | [S] image-domain only | K07; b16, c06, b23, c08, c09 |
| Code check that the proposed shared slot holds for both inputs (generic-space gate) | O3 / S4 | [S] | K05; a13, d09 |
| Code-side recombination of two frames' parts, then validity check | O3 / S3 open | [S] | K16; d10 |
| Bridge-concept step: 5 bridges, filter by check, vs top-1 | O7 | [S] | K06; a17, c01, c03 |
| Network-type label per cross-frame step plus two-run agreement | O3 / memory | [S] (K01 is [E] only for the definition) | K01; d04 |
| Far-pair step ranked by low co-occurrence plus coherence gate, instead of higher temperature | O7 / S3 open | [S] | K22; d07 |
| Check that each borrowed role still holds in the target frame | G3 / S8 | [S] | K20; d03, d05 |
| Run a blend in both input orders and let a check choose (established for diffusion, unproven for text) | O7 / S4 | [E] images, untested text | K09; a19, b17, b22, c13, c14 |
| Show projected parts per blend, accept or reject by check | G2 | [S] | K14; a21, b20 |
| More checking on implication claims than on identifying inputs | G5 | [S] | K08; b14, c05 |
| Frame distance as a labeled choice, more checking after a far choice | G4 | [S] | K19; d13 |
| Eppe-style blend score validated against blind judges | G5 | [S] | K21; d14 |

## 8. Concrete tests on our bench

All arms get equal token budgets, setup cost included (G7). Blind judges plus code checks; the judge is never the generating model (G8). Where a check exists, the metric is a pass on held-out input.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Open-mode novelty items (NoveltyBench style, cross-frame prompts) | plain; single-scope-style prompt (one frame organizes); double-scope-style prompt (both frames give roles, emergent structure required) | blind novelty and validity; distinct-output count | No difference or small gain; double-scope higher novelty and lower validity (matches Palamas trade-off). First direct test of the type; exploratory |
| T2 | Same items | plain vs "inputs / how combined / implications" fields plus critic with one backtrack | blind novelty and validity; tokens | Image gain was 0.26 to 0.35 win rate; expect a smaller text gain that may vanish at equal tokens |
| T3 | Cross-frame reasoning items with a check | with vs without generic-space gate | valid-blend rate, held-out pass rate | Kombine: 43.4% valid vs 97.1% given a valid space; expect a gain in valid rate, uncertain gain in final answers |
| T4 | Text recombination tasks | one-shot vs code-side recombination of listed parts | blind novelty, valuable share, tokens | Novelty about +0.4 on a 5-point scale at similar value; value may fall (85% vs 98%) |
| T5 | Cross-frame steps in agent traces | label with type; same-frame vs cross-frame | error rate per step; label agreement across two runs | Cross-frame steps have higher error; label agreement shows whether the label is usable |
| T6 | Blend pairs | both orderings vs one ordering plus a check | pass rate, dominance log | Small gain; shows whether order matters in text |
| T7 | Far-pair choice | ranked by low co-occurrence plus coherence gate vs higher temperature vs default | blind novelty; coherent share | Ranking beats temperature (Hernandez) |
| T8 | Juxtaposition filter | with vs without rejection of splittable blends | blind integration rating (Kombine-style Q), diversity | Fewer concatenations; Q up |
| T9 | Blend claims | near vs far frame pairs, held-out fact check | ungrounded-claim rate | Far pairs have more ungrounded claims (K12 hypothesis) |

## 9. What does not transfer, and why

- **The typology as a recipe.** No evidence that picking a type changes outcomes. The types came from after-the-fact analysis of hand-picked examples and the authors call them prototypes on a continuum.
- **Human ERP results.** N400 gradients measure reader effort. Models have no N400. They support only the broad idea that cross-frame steps cost more, and rival theories predict the same.
- **Image-domain gains.** IEI, the schema loop and diffusion weighting are image generation with author-designed metrics; baselines got a plain prompt while the scaffold used extra calls. Text transfer is unproven.
- **Pop-culture and cooking domains.** PopBlends (10 students) and Dish COVER (cooking, 10 dish pairs in Exp 1) use thick familiar frames. Reasoning tasks differ.
- **Kombine scores as a typology test.** Its single-scope and double-scope are its own scale.
- **"Double-scope for novel ideas" inside our guardrails.** G8 and G12 say novelty is judged by running and search needs a foothold; the schema's O7 note says far analogues lower the average and raise the spread. A double-scope push is a far-pair move and belongs in open mode and at impasses only.
- **LLM-judged quality.** Self-preference risk; judges were GPT-4o, GPT-4 or LLM panels.
- **Position papers (Sato 2025, Lynn 2026, Lippolis 2025).** No measurements; vocabulary only.

## 10. Open questions

1. Does labeling a blend by network type predict novelty or validity? No data either way.
2. What does the 2002 book chapter claim about each type? Not opened.
3. Does a text-only "how the inputs combine" field help reasoning at equal tokens?
4. Does a code-side generic-space gate raise valid-blend rate? Untested (d09).
5. What share of LLM blends reach Kombine's Q=1, 2, 3, and how does that vary with temperature and size? Not published (d08).
6. Is the 16.8% gain in Xu et al. on analogy appropriateness or on the paper's own "AA" metric? Not verified (critique flag 2).
7. Does the Eppe imbalance term predict blind-judge preference?
8. Do human creators' products differ by network type in novelty? No coded study found (Dreyfus 2014, Turner 2014 not opened).
9. Does far-frame blending raise ungrounded output (Sato's claim) by a measurable amount?
10. Can Hernandez's "alien" ranking be done in text with open models?

## 11. Sources

[V] opened and read; [M] snippet, listing or secondary report only.

- [V] Wikipedia, Conceptual blending. https://en.wikipedia.org/wiki/Conceptual_blending (a01, b01-b03, c19, c20)
- [V] Fauconnier and Turner (1998; expanded 2001) Conceptual Integration Networks. https://www.neurohumanitiestudies.eu/archivio/SSRN-id1292966.pdf (d02, d03)
- [M] Fauconnier and Turner (1998) web page. https://markturner.org/cin.web/cin.html (a02, b09)
- [V] Fauconnier and Turner (2003) Conceptual blending, form and meaning. https://ojs.uclouvain.be/index.php/rec/article/download/48413/46613 (d04, d05)
- [M] Fauconnier and Turner (2002) The Way We Think. https://www.basicbooks.com/titles/mark-turner/the-way-we-think/9780465 (a23, b10)
- [M] Turner (2014) The Origin of Ideas. https://global.oup.com/academic/product/the-way-we-think-9780465087860 (b10)
- [V] Coulson and Oakley (2000) Blending basics. https://pages.ucsd.edu/~scoulson/Papers/basics.pdf (a03-a06, a25)
- [V] Coulson and Van Petten (2002). https://pages.ucsd.edu/~scoulson/Papers/coulson-vanpetten.pdf ; https://europepmc.org/article/MED/12450098 (a07, a26, b04)
- [V] Coulson and Matlock (2001). https://pages.ucsd.edu/~scoulson/Papers/CoulsonMatlock2001.pdf (a08)
- [M] Gibbs (2000) Making good psychology out of blending theory. https://doi.org/10.1515/cogl.2001.020 (a09)
- [M] Ritchie (2004), as reported on Wikipedia (a10)
- [V] Jonczyk et al. (2020) Engineering creativity. https://pmc.ncbi.nlm.nih.gov/articles/PMC7540055/ (b05; sample sizes not extracted)
- [V] Miller, Jonczyk, Zaharchuk and van Hell (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12063520/ (b06, b07)
- [V] Canovas and Manzanares (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4009410/ (b08)
- [V] Turner blending page; Gomez-Ramirez and Turner (2026). https://markturner.org/blending.html ; https://markturner.org/FormalConceptualBlending2026-07-24.pdf (a11, a12)
- [V] Xi, Cheng, Soni and Turner (2026) ACL poster. https://markturner.org/ACL2026_Conceptual_Blending_Poster_compressed.pdf (d01; URL as stored in the evidence list, which was truncated in my view)
- [V] Schapiro et al. (2026) Kombine. https://arxiv.org/abs/2509.21043 (a13-a16, d08, d09)
- [V] Wang et al. (2023) PopBlends. https://arxiv.org/abs/2111.04920 (a17, b25, b26, c01-c03)
- [V] Ge and Parikh (2021). https://arxiv.org/abs/2106.14127 (a18, b11-b13, c04)
- [V] Peng et al. (2025). https://arxiv.org/abs/2504.13120 (b14-b16, c05-c07, d06)
- [V] Olearo et al. (2025). https://arxiv.org/abs/2506.23630 (a19, b17, b18, c14); Olearo et al. (2024) https://arxiv.org/abs/2407.14280 (c15, thin detail)
- [V] Matsuhira et al. (2024). https://arxiv.org/abs/2411.03595 (b22, c13)
- [V] Cho et al. (2025) IT-Blender. https://arxiv.org/abs/2506.24085 (b21, c22; qualitative only)
- [V] Xu et al. (2026). https://arxiv.org/abs/2602.01335 (b23, c08, c09)
- [V] Lu et al. (2025) Misty. https://arxiv.org/abs/2409.13900 (a21, b20, c17)
- [V] Sato (2025). https://arxiv.org/abs/2505.10948 (a20, b19, c10)
- [V] Lynn (2026). https://doi.org/10.3389/fpsyg.2026.1849083 (c11)
- [V] Cappa, Lippolis and Zoia (2025). https://arxiv.org/abs/2507.10354 (a22, b24, c12; no results)
- [V] Hernandez et al. (2024) Alien Recombination. https://arxiv.org/abs/2411.11494 (c16, d07)
- [V] Mizrahi et al. (2025) Dish COVER. https://arxiv.org/abs/2504.20643 (d10, d11)
- [V] Yasunaga et al. (2024). https://arxiv.org/abs/2310.01714 (d12)
- [V] Palamas (2025). https://computationalcreativity.net/iccc25/ (d13)
- [V] Eppe et al. (2018). https://doi.org/10.1016/j.artint.2017.11.005 (d14)
- [V] Lieto and Pozzato (2020). https://arxiv.org/abs/1811.02366 (d15)
- [V] Gomez-Ramirez et al. (2021). https://arxiv.org/abs/2112.02457 (b29, c18)
- [V] Birdsell (2019). https://iafor.org (d16)
- [V] arXiv keyword search "double-scope". https://arxiv.org/search/?query=%22double-scope%22&searchtype=all (b28, c21)
- [M] Veale and O'Donoghue (2000); Grady (2000) (both via a03); Lieto et al. PET-FISH (b27); Cunha et al. (2020) (c24); Sun et al. (2025) (c25); Hicke and Kristensen-McLachlan (2024) (c26); Dreyfus, Gupta and Redish (2014) https://arxiv.org/abs/1412.1693 (c27).
