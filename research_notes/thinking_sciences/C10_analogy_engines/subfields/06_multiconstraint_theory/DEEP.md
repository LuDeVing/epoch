# Multiconstraint theory: deep document

*Subfield C10.06. Built from evidence_a-d.jsonl (a01-a30, b01-b30, c01-c27, d01-d18), claims.jsonl (K01-K30) and critique.md in this folder. Evidence ids are cited in brackets. Where critique.md corrected a number, the corrected number is used here.*

## 1. What it is

Multiconstraint theory says that people choose an analogical mapping under three soft pressures at once.

- **Structure.** The mapping should be consistent: one source element to one target element, and linked elements should map to linked elements. The ideal is an isomorphism.
- **Similarity.** Elements that look alike, or relations that mean alike, attract each other.
- **Purpose.** The reasoner's goal makes some elements and pairings more important than others.

The word "soft" is the core of the theory. None of the three is a rigid rule. They act like forces in a design. A mapping that breaks one-to-one can still win if similarity and purpose push hard enough. The mapping that wins is the one that satisfies the three pressures best overall, found by a parallel constraint-satisfaction process [a01, a02, a18].

What the theory covers:

- Analogical **mapping** (which source element goes with which target element). Original model: ACME (1989).
- Analogical **retrieval** (which stored case comes to mind). Model: ARCS (1990).
- Later models that add working-memory limits (LISA, 1997) and word-vector semantics (PAM, 2022) [a16, b14].

What it is not: it is not a theory of how to find a good source or how to generate ideas. It is about choosing among candidate mappings once candidates exist.

Why it matters for our agent. In schema operator O7 ("Map an analogue") the agent must pick a mapping, and the schema asks for it to be "checked by code". The theory tells us what a good mapping score has to contain: three separate lines (relation fit, feature fit, goal fit), not one similarity number. It also tells us where models fail: they follow surface similarity when the correct analogy is far, and they use the goal poorly [a22, d06].

The honest state of evidence: the human data for the three-constraint claim come mostly from one lab (Holyoak and colleagues) with small undergraduate samples. The LLM literature tests mapping, structure and surface lure, but no study tests the goal-driven mapping reversal directly [critique, K22, K30].

## 2. History and theories in depth

### 2.1 Before 1989: structure first

Gentner's structure-mapping theory (1983) and its program SME (Falkenhainer, Forbus, Gentner 1989) say that analogy is the alignment of relational structure. SME builds match hypotheses from identical relations, assembles structurally consistent global mappings, and ranks them by systematicity (a deep, interconnected relational system). Semantics and pragmatics are kept outside the mapping stage [a29, second-hand]. Object attributes count little.

### 2.2 ACME, 1989: three constraints in one network

Holyoak and Thagard (1989) built ACME as a localist network [a02, b01].

- Each possible pairing of a source element and a target element is one unit. A source with 46 propositions and a target with 49 gave 1,207 units and 22,271 links in one run [a12].
- Excitatory links join pairings that support each other (same proposition, consistent arguments). This is the structure constraint.
- Inhibitory links join pairings that compete (the same element mapped twice). This is the soft one-to-one pressure.
- A **semantic unit** boosts pairings of similar predicates. This is the similarity constraint.
- A **pragmatic unit** boosts elements marked IMPORTANT and pairings marked PRESUMED. This is the purpose constraint.
- Activation is updated with the Grossberg (1978) rule until the network settles.

Defaults in all reported runs: decay d=.1, excitation e=.1, inhibition i=-.2, min=-1, max=1, IMPORTANT weight p1=.1, PRESUMED weight p2=.3, start activation .01, similarity weight .1 for identical predicates. The network usually settled well under 100 cycles and never over 220 in the reported runs [a02]. (One large network took 402 cycles [b04].)

ACME results [a03-a07, b02-b04]:

- It found the correct mapping in all four lightbulb/radiation versions of Holyoak and Koh (1987). Surface similarity (laser vs ultrasound) had no measurable effect on mapping difficulty. In the poor-constraint versions the key proposition ("do not destroy healthy tissue") had no mapping at all, offered as the reason people failed to transfer [a04].
- On the Gentner and Toupin "jealous animal" stories, systematicity mattered only when similarity misled (cross-mapped versions). In the unsystematic cross-mapped version ACME failed unless inhibition was lowered from -.2 to -.1 or the floor was raised from -1 to -.3 [a05, b02]. That fix was found after the fact.
- It handled formal isomorphs with no shared predicates (the boys-and-dogs problem: unique isomorphism found with no semantic help) and non-isomorphic cases such as Socrates as midwife [a06, a07].
- Sensitivity: a wide parameter range works. Excitation above .12 is unstable. High inhibition can block recovery from an early wrong mapping. Inhibition should exceed excitation [a03].

### 2.3 ARCS, 1990: retrieval under the same constraints

ARCS (Thagard, Holyoak, Nelson, Gochfeld 1990) applies the same three constraints to memory search [a13, a14]. A probe links only to stored structures that share semantically similar predicates. Then structure and pragmatic support settle in a network. Semantic overlap is a gate: structure alone cannot retrieve a far analog. It reproduced the order of retrievability in Holyoak and Koh (1987). Scale: 100 Aesop fables (about 22 propositions each) and 24 Shakespeare synopses (about 55 each). Links grow about as the square of database size. Fragility: deleting 25% of units broke the human fit 75% of the time.

### 2.4 Spellman and Holyoak, 1992 and 1996: goals change mappings

Two human programs tested the purpose constraint (numbers in section 3).

- 1992: Gulf War vs World War II mappings are bistable (two internally consistent mappings), and knowledge can steer which one people pick [d07, d08, d09, a08].
- 1996: the processing goal reverses the mapping of a structurally ambiguous element. ACME reproduces this when the goal is implemented as selective attention, meaning inhibition of goal-irrelevant propositions [a09-a12, b05-b09].

### 2.5 LISA, 1997: the theory in a limited working memory

Hummel and Holyoak (1997) recast the theory in a symbolic-connectionist model with synchrony binding and limited working memory [a16, a17]. They list 14 phenomena an analogy model must cover, including that semantic similarity weighs more in access than in mapping and isomorphism weighs more in mapping. LISA simulates Ross (1989) access vs mapping patterns, the Barebrute goal weights and the soap-opera Experiment 3. It solved the boys-dogs problem only when all 10 propositions of both analogs were in the phase set together, more than human working memory allows (so LISA's authors argue ACME is too powerful on such unnatural problems). All fits are qualitative.

### 2.6 Krawczyk, Holyoak, Hummel 2004: the discriminating test against SME

Under high relational complexity, people weighted object similarity and relational structure about equally. SME (structure first) did not reproduce this. LISA (soft constraints in a limited memory) did [a15, b10-b12].

### 2.7 Successors: PAM and beyond

- Hummel and Holyoak (2005) put the theory into a neural network; Doumas, Hummel, Sandhofer (2008) learn relations from unstructured examples [a18, a30, both second-hand].
- **PAM** (Lu, Ichien, Holyoak 2022) is Bayesian graph matching with soft constraints on concept similarity, relation similarity, structure and attention-weighted pragmatic focus, using word vectors and learned relation vectors [b14, b15, c19].
- Related LLM-era work: Webb, Holyoak, Lu 2023 (GPT-3 analogy), Ichien et al. 2023 (metaphors) [a19, b27].

### 2.8 The rival and the long argument

The SME line holds that structure comes first and similarity is a tie-breaker. The multiconstraint line holds that all three are weighed at once. Evidence does not settle it. The likely moderator is relational load: Krawczyk found equal weights under high load; Gentner and Markman used lower-load items where structure dominated [b12]. Colhoun and Gentner (2009), an independent lab, argue that an effect inference can be judged after mapping, not only by a causal model. This is an adjacent claim and a competing explanation, not a failed replication of the 1996 result [d16].

## 3. Core findings with exact numbers

Status key: established = consistent across sources; single = one source; contested = sources disagree; model = simulation result.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Goal reverses mapping of an ambiguous element (Anthar) | Trade goal: Grandus 54% vs Minutus 19%. Membership goal: 21% vs 58%. chi2(1,N=53)=11.78, p<.001. 116 recruited, 12 dropped. Winter country to Grandus 31% vs 4%, chi2(2,N=55)=6.82 | Spellman and Holyoak 1996 Exp1 [a09, b05] | Established, but one lab (K02, K30) |
| Goal-irrelevant information still leaks (attenuation, not a filter) | Exp2 N=159: collapsed chi2(1,N=108)=8.85. Many-to-one mapping in control 8 of 16 (50%); 32% across goal conditions. Military condition 77% vs 13% | SH 1996 Exp2 [a10, b06] | Single-source (K03) |
| Goal acts only where structure is ambiguous | Unambiguous countries (Afflu, Compak) mapped as expected by about 90% in all five goal conditions | SH 1996 Exp2 [b09] | Single-source (K04) |
| All three constraints at once (soap opera) | N=128. Plot task: 88% wrote a continuation, 97% matched the goal focus (chi2=95.33, n=107). Mapping task n=88: goal-consistent 72% vs 28% (chi2=16.41); followed incidental inheritance relation 65% vs 35% (chi2=7.68, p<.01). Goal-consistent in plot task but not mapping: 23 vs 1 (chi2=20.17) | SH 1996 Exp3 [a11, b07] | Single-source |
| Bistable mapping (Gulf War vs WW2) | 196 surveyed, 122 attempted, 42 met criteria. Bush=FDR with US-WW2: 21; FDR with Britain: 2; Churchill with US-WW2: 6; Churchill with Britain: 13. 34/42 = 81% consistent, chi2(1,N=42)=16.16 | SH 1992 Exp1 [d07] | Established, same lab (K05) |
| Slanted histories steer only toward consistent pairs | N=50 usable of 76. 88% consistent overall (chi2=26.60). 89% under consistent histories vs 86% under crossed, chi2=0.15 ns. Consistent histories gave opposite patterns, chi2(1,N=25)=11.65 | SH 1992 Exp2 [d08] | Single-source |
| One-to-one is strong but soft | N=67, 59 retained, 46 mapped. One-to-many mappings 41% crossed vs 0% consistent, chi2(1,N=46)=9.75 | SH 1992 Exp3 [d09] | Single-source (K26) |
| Surface and structure both drive spontaneous transfer | Spontaneous convergence solutions 69 / 38 / 33 / 13% across four surface-by-structure versions. After hint 75 / 81 / 60 / 47% (pairing uncertain) | Holyoak and Koh 1987, via ACME/ARCS [a04, a13, a27] | Established (second-hand numbers) |
| Retrieval and mapping dissociate | Keane 1987: 88% retrieved same-domain story vs 12% remote. Once cued, solving about 86% either way | via PAM paper [b16] | Established, second-hand |
| Under high load, object similarity weighs as much as relations | N=48. Mappings O .33, R .30, SO .32, U .06 (F(3,141)=21.64). Inferences O .28, R .23, SO .50, U .02 (F=18.78). 2.36 mappings per character. SME: object inference 1.01 vs relational 6.21. LISA 50 runs: 24% / 18% / 48% | Krawczyk et al. 2004 [a15, b10, b11] | Contested (K07) |
| ACME ordinal fit to human transfer | Cycles to success 3, 38, 5, 5 (version pairing uncertain). Network settled by cycle 31, goodness 4.84 for laser/fragile | HT 1989 [a04] | Model |
| ACME failure modes | Excitation above .12 unstable. Unsystematic cross-mapped Jealous Animals: no success at i=-.2 | HT 1989 [a03, a05] | Model |
| Pragmatic support speeds non-isomorphic mapping | Socrates-midwife: 34 cycles (isomorphic), 105 (non-isomorphic), 83 (non-isomorphic, pragmatic) | HT 1989 [a07] | Model |
| ARCS reproduces retrieval order | Human 69/38/33/13% vs activation .22/.15/.11/.05. Tumor probe: 100 units, 1,104 links, 95 cycles | Thagard et al. 1990 [a13] | Model, rank only |
| Relation use is strategic | Priming only when told to note and use the relation: 761 vs 786 ms, 25 ms, F(1,23)=36.54 | Spellman, Holyoak, Morrison 2001 [b17] | Single-source |
| PAM matches human mapping and the goal effect | N=1,329. Category triplets humans .74 vs PAM .83. Part-Object-Location .79 vs .89. Keyword analogies 85% vs adults 88%. Goal-focus correlation .96 over 10 conditions. Without relation similarity 77% | Lu, Ichien, Holyoak 2022 [b14, b15, c19] | Model, single-source (K23) |
| GPT-3 vs students on text analogy | Digit matrices (N=40): OR 1.88 generative (p=.005), 6.27 multiple choice. Letter strings (N=57): OR 1.76. Story analogies (N=54): OR 0.37 (p=.0003). Near stories p=.0039, far p=.065 | Webb, Holyoak, Lu 2023 [a19, b18, c01-c03] | Single-source, same lab (K11) |
| Relational load hurts GPT-3 more than humans | Unique rules (3-rule): humans OR 0.61, GPT-3 OR 0.25. Progression: 0.41 vs 0.07. Spatial permutation: 0.52 vs 0.06 | Webb et al. 2023 [d10, c27] | Single-source |
| Counterfactual letter strings: models drop, humans do not | Humans 1,876 samples, overall .753 [.734, .773]. GPT-3, 3.5, 4 at temperature 0 drop sharply | Lewis and Mitchell 2024 [b20, c05] | Contested (K12) |
| Reply: the failure is counting | Humans N=99/97. GPT-4+code vs humans P=0.496. Plain GPT-4 vs humans P=8.9e-13. New alphabet P=0.52; older engine P=0.12. 46% (23/50) of GPT-4+code errors were valid alternative rules | Webb et al. 2024 [d01, d02] | Contested; same lab |
| LLM errors differ in kind (corrected, critique) | Alternate-rule errors: humans 38.59%, GPT-4 22.00%, GPT-3 5.81%. Incorrect-rule: GPT-3 30.97%, GPT-4 32.67%, humans 14.67%. Wrong: 55.48 / 42.67 / 34.24%. Completely wrong: 7.74 / 2.67 / 12.50% | Lewis and Mitchell 2024/25 [b23, c05, critique] | Single-source (K15) |
| Far story analogies with a near lure | ARN 1,096 triples, chance 50%. Near analogies: models 75.0% vs humans 97.9%. Far: 39.6% vs 94.1%. Near analogy vs far disanalogy 76.9%; (near,near) 73.2%; (far,far) 45.3%; far analogy vs near distractor 33.9%. GPT-4 best, 68.1% mean. Overall humans 96% vs models 57% | Sourati et al. 2024 [a22, c08] | Established (K13) |
| StoryAnalogy multiple choice | Chance 25%, humans 85.7%, ChatGPT about 30% | Jiayang et al. 2023 [c10] | Single-source |
| Answer-order bias, paraphrase | Webb data GPT-4: first .89 (16/18), second .61 (11/18), total .75. Lewis and Mitchell GPT-4: 1.0 / .72 / .86 (31/36). Humans .78 either order (564/720, N=245). Paraphrase: GPT-4 .86 to .72, humans .78 to .70 | Lewis and Mitchell 2024/25 [a21, b22, critique] | Single-source (K14) |
| 2024 models on 18 Gentner stories, order balanced | Humans .847; GPT-3 .75. Conventional: gpt-4o-mini .7011, gpt-4o .8233, Llama-3.1-8B .6528, Llama-3.1-70B .8538. Hint-then-choose best about .915 (70B) | Inani et al. 2025 [d04] | Single-source (K13, K28) |
| Familiarity effect on letter strings | Latin/Greek/Symbol: adults .88/.91/.89; children .62/.66/.67; GPT-4o .85/.63/.48; Claude-3.5 .68/.62/.46; Llama-3.1 405B .79/.74/.27; Gemma-2 27B .60/.39/.14. Humans p=1.0, LLMs p<.001 | Stevenson et al. 2025 [b24] | Single-source (K16) |
| Association inflates LLM analogy scores | 14,006 children, 622 Dutch analogies. Controlling for association: 1-2 age-year drop | Stevenson et al. 2023 [c12] | Single-source (K17) |
| Irrelevant structure leaks more in LLMs | Random left-hand items: humans lose about .15; Claude 3 about .5; GPT-4 .6 and .4. Widened task: humans and Claude 3 about .7, GPT-4 and Llama-405B about .35. Numeric conditions GPT-4 .2-.3 | Musker et al. 2025 [d12-d14] | Single-source (K18, K27) |
| Abstraction before mapping | MCQ (chance .25): raw embedding mapping Qwen .17; with LLM abstraction best .46 vs best LLM-only .41. Llama .16 to .45 vs .28 LLM-only | Khojasteh et al. 2026 [c20] | Single-source (K19) |
| Relation application is a bottleneck | Patching fixed +49.8% (Llama-2-13B), +61.9% (Gemma-7B), +55.3% (Qwen2.5-14B) of errors | Lee et al. 2025 [a23, d15] | Single-source (K29) |
| Analogical prompting | GSM8K GPT-3.5: 75.0 / 75.8 / 76.7 / 77.8 (0-shot / 0-shot CoT / 5-shot CoT / self-generated). text-davinci-003: 14.8 / 50.3 / 54.0 / 61.0. PaLM2: 60.8 / 78.2 / 80.7 / 81.7. MATH GPT-3.5: 33.0 / 33.9 / 34.9 / 37.3. Codeforces Acc@1 GPT-3.5: 8 / 9 / 11 / 13, with knowledge 15. Average +4% | Yasunaga et al. 2024 [a24, c15, critique] | Single-source, related work (K21) |
| Structured analogy for ideas | Vendi +90-173%; novel solutions over 50% vs as low as 1.6%; 50 problems, 3 LLMs. Random cross-domain sources gave LLMs no overall gain (humans N=140; originality vs feasibility r=-0.74) | Shen et al. 2026 [c21]; Liu et al. 2026 [a26] | Contested (K20) |

## 4. Mechanisms and models

This section is written so an engineer can build each piece.

### 4.1 ACME as an algorithm

Inputs: source propositions and target propositions, each as predicate(arg1, arg2, ...). Optional: a list of important target elements, and presumed pairings.

1. For every source proposition and target proposition with the same arity, create units for the predicate pair and for each argument pair.
2. Add links:
   - Excitatory (+e) between a predicate-pair unit and the argument-pair units under it, and the reverse.
   - Inhibitory (i, negative) between any two units that map the same source element to different targets, or the same target from different sources.
   - Semantic: a link from a constant "semantic" node to each unit, weight proportional to predicate similarity (.1 for identical predicates; .06 for similar and .01 for dissimilar objects in the animal stories).
   - Pragmatic: a link from a constant "pragmatic" node to units that involve IMPORTANT elements (p1=.1) and to PRESUMED pairings (p2=.3).
3. Initialise all units at .01. Update: `a(t+1) = a(t)(1-d) + net*(max-a(t))` if net>0, else `a(t)(1-d) + net*(a(t)-min)`, with net = weighted sum of neighbour activations. Run until the largest change is below a small threshold (cycles reported: 3 to 402, typically under 100).
4. Read out, for each source element, the target with the highest activation. Elements with no positive unit stay unmapped.

Parameters that matter: inhibition must exceed excitation; excitation above .12 oscillates; lowering inhibition or raising the floor rescues cross-mapped cases [a03, a05]. (The update rule and the link recipe above are the standard Grossberg form as described in the paper; exact thresholds are an implementation choice.)

### 4.2 Goal as selective attention (SH 1996)

To add a processing goal, inhibit the goal-irrelevant propositions (reduce their weight) before running the network. Goal-relevant relations (trade, or membership) then dominate the choice among units for an ambiguous element. This reproduced the Anthar reversal, the Exp2 pattern and the Exp3 pattern, with ordinal fit only [a12, b08]. PAM does the same by drawing an attention weight uniformly from [1, 1.1] on goal-relevant relations, averaged over 1,000 samples per condition [b15].

### 4.3 PAM as a scoring rule

PAM scores a candidate mapping as a probability from three kinds of evidence: node similarity (word vectors), edge or relation similarity (learned relation vectors, for example BART), and structure (consistent pairing of edges and their endpoints), with attention weights on goal-relevant edges. Dropping the relation term cut accuracy to 77% on 20 keyword analogies; using word2vec differences for relations also gave 77% [b14]. This is the closest published design to "three lines scored, then combined".

### 4.4 LISA constraint: working memory

LISA binds roles to fillers by synchrony and can hold only a few propositions at once. Mapping proceeds in phases. Consequence: the weight of surface similarity rises under load, because relations cannot all be held [a16, b12]. For an LLM agent the analogue is context and attention: long relational descriptions may act like high load.

### 4.5 A scaffold-ready scoring procedure (our proposal, not published)

```
candidates = list of mappings (role table: source role -> target role, with justification)
for m in candidates:
    rel  = fraction of source relations whose arguments map consistently under m   # structure
    feat = mean similarity of mapped element pairs (attributes, type)               # similarity
    goal = weight of mapped elements/relations that the goal marks as important     # purpose
    one2one_violations = count of elements mapped twice
score = w_rel*rel + w_feat*feat + w_goal*goal - w_pen*one2one_violations
```

Rules from the data:

- Keep the three terms separate in the log, so a wrong pick can be traced (G10).
- Give the goal weight only through elements that are structurally ambiguous (K04).
- Treat one-to-one as a soft penalty, and allow a flagged one-to-many when two source roles both fit (K26).
- If the top two scores are within a margin, keep both mappings and look for a discriminating check (K05, K08).
- Compute the score in code where possible (G5). The LLM supplies the role table and the per-relation judgments; code does the arithmetic and the one-to-one count.

This is a hypothesis. No published LLM study tests it (critique GAP 2).

### 4.6 Abstract-then-map pipelines (YARN)

Khojasteh et al. split stories into units, have an LLM abstract each unit into roles and relations, then run a greedy one-to-one structural mapping in code with soft constraints. Raw event text through embeddings was below chance; abstraction lifted it [c20]. Hint-then-choose prompts (Inani) and two-step relation prompts follow the same idea [d04, d15].

## 5. What holds up

### 5.1 Holds up

- **Goal changes mapping when structure is ambiguous.** Seen across Exp1, Exp2, Exp3 of 1996 and in PAM's simulation (r=.96) [a09-a11, c19]. Boundary: unambiguous elements are stable (about 90%) [b09].
- **Bistable mappings exist and social-role consistency is strong.** 81% and 88% consistent in two 1992 experiments [d07, d08].
- **Soft constraints beat structure-only rules in the lab's own tests.** Krawczyk 2004 vs SME [b11].
- **LLMs follow surface lures on far analogies.** ARN far vs near distractor 33.9%; StoryAnalogy about 30% vs 25% chance [a22, c10]. This is reported on benchmarks from different labs, so it is the best-established LLM finding here.
- **Position bias and surface overlap in LLM story analogy.** Order bias 0.89 vs 0.61 [b22].

### 5.2 Weak or contested

- **No independent replication of the Anthar reversal.** The nearest independent test is adjacent (Colhoun and Gentner 2009) [d16]. Critique: independent_sources is really about 1.5.
- **Samples and materials.** N=53 in Exp1 (after dropping 12 of 116), text cover stories, undergraduates, written mappings. Exclusion rates are large: 80 of 122 in 1992 Exp1; 26 of 76 in 1992 Exp2; 31% in the 1996 Exp3 mapping task [d07, d08, a11].
- **Many-to-one may be a response-format artefact.** The answer format allowed several entries [a10, b13].
- **Model fits are ordinal.** ACME and ARCS claim no fit statistic; ARCS broke 75% of the time when 25% of units were removed [a12, a14, b08].
- **Structure vs similarity is unresolved.** Equal weight under high load [b10]; structure first at low load [b12]. Load was not manipulated within one study.
- **Letter-string zero-shot analogy.** Webb 2023: human level. Lewis and Mitchell 2024: counterfactual alphabets break it. Hodel and West: contamination. Webb 2024: code fixes it, so counting is the cause (P=0.496 with code). Still same-lab on one side; contamination cannot be excluded for older tasks [b20, c07, d01-d03].
- **Reasoning models and 2025-2026 models are barely tested** on ARN, StoryAnalogy or letter-strings. The 18-story set shows 2024 models at .82-.85 against humans .847 [d04], so the far-analogy gap may have shrunk on easy sets, while ARN far-vs-near distractor items are untested.

### 5.3 Moderators

- Relational load (above).
- Familiarity of the domain: LLMs only [b24].
- Counting and numerosity: LLM-specific [d01, d14].
- Surface overlap of the correct story with the source sentence (paraphrase test) [b22].
- Model family: Claude 3 stayed human-level where GPT-4 and Llama-405B fell [d13].

### 5.4 Interventions that worked

- Hint-then-choose (model writes causal-structure hints first): all four models up on 18 stories, best .915 vs .8538 [d04]. Caveat: item difficulty became less human-like for 3 of 4 models, and a ceiling effect is possible [d05].
- LLM abstraction then code mapping: Llama .28 to .45 on MCQ, but a loss on near analogies for Qwen (CoT .79 vs YARN .69) [c20].
- Code execution for counting: closed the counterfactual letter-string gap [d01].
- Solved demonstrations helped far-analogy detection but hurt near ones [c09].
- Prompt to "consider earlier stories" restored the radiation solution after distractors in GPT-3 (single qualitative runs) [a20].

### 5.5 Interventions that did not work, or do not test the claim

- Told to look for system mappings, models still preferred surface-similar stories [a22].
- Few-shot demonstrations first reduced near-analogy skill [a22].
- Random cross-domain source prompts: no overall gain for LLMs [a26].
- Self-generated exemplars: only +1.1 over 5-shot CoT on GSM8K for GPT-3.5 [critique]; and it tests recall, not mapping choice [a24].
- Biased histories pushing crossed pairs did not break the consistent-pair preference in people [d08].

## 6. Language models

### 6.1 What was measured

| Study | Models | Task | Result |
|---|---|---|---|
| Webb et al. 2023 [a19, c01-c03] | GPT-3 (text-davinci-003), GPT-4 preliminary | Digit matrices, letter strings, verbal analogies, story analogies | At or above students on text matrices and letter strings; below on stories (OR 0.37); GPT-4 near perfect on near stories, above chance on far (p=.0039, 72 items) |
| Lewis and Mitchell 2024 [b20] | GPT-3, 3.5, 4 | Counterfactual letter strings | Large drop; humans .753 |
| Webb et al. 2024 [d01] | GPT-4, with code | same | Human level with code (P=.496) |
| Lewis and Mitchell 2025 [b22] | GPT-4 | 18 story analogies | Order bias 1.0 vs .72; paraphrase .86 to .72 |
| Sourati et al. 2024 [a22] | Llama 2, Flan-T5, UnifiedQA, GPT-3.5, GPT-4 | ARN | Far analogies 39.6% (below chance); far vs near distractor 33.9% |
| Jiayang et al. 2023 [c10] | ChatGPT | StoryAnalogy MCQ | About 30% vs 85.7% humans |
| Inani et al. 2025 [d04] | gpt-4o-mini, gpt-4o, Llama-3.1 8B/70B | 18 stories, order balanced | .65-.85 conventional; up to .915 with hints |
| Musker et al. 2025 [d12-d14] | GPT-4, Claude 3 Opus, Llama-405B | Semantic structure mapping | Leakage of irrelevant structure; model differences |
| Stevenson et al. 2025 [b24] | GPT-4o, Claude-3.5, Llama-3.1, Gemma-2 | Letter strings in 3 alphabets | Familiarity effect, humans none |
| Lee et al. 2025 [d15] | Llama-2-13B, Gemma-7B, Qwen2.5-14B | Proportional and story analogies | Relation application is a failure point |
| Khojasteh et al. 2026 [c20] | Qwen, Llama | ARN, MCQ | Abstract-then-map +.17 on MCQ for Llama |
| Webb et al. 2023 digit matrices [d10] | GPT-3 | Relational load | OR .25 vs .61 for 3-rule problems |

### 6.2 Pattern

1. **Models are good where similarity and structure agree** (near analogies 75.0%, matrices OR 1.88 to 6.27) and weak where the correct analogy is far and a lure is near.
2. **Surface association inflates scores** (1-2 age-year drop when controlled [c12]; domain familiarity effect [b24]).
3. **Irrelevant content leaks into the mapping** more than in people [d12].
4. **Order and wording matter** [b22, c11].
5. **Counting and numerosity are separate failure points** that code fixes [d01, d14].
6. **The purpose constraint is untested.** The 2025 survey names goal-driven mapping as an open problem and cites no measurement [d06, b29]. The position paper [b30, c18] has no data.
7. **Mechanism:** relation information is present in mid-upper layers when the answer is correct; failures often come from not applying the relation to a new entity [d15]. Concept vectors for abstract "previous/next" are not invariant: Llama 70B scores 98% on previous/next items but 62% on abstract versions [c13].

### 6.3 What changed results, and by how much

- Hint-then-choose: .8538 to about .915 (Llama-3.1-70B) [d04]. Weak evidence: 18 items.
- Abstraction plus code mapping: Llama .28 (LLM only) to .45 on MCQ [c20].
- Code for counting: from far below human to human level [d01].
- Self-generated exemplars: +1 to +6 points on strong models [c15].
- Structured analogy generation: Vendi +90-173% [c21]; judged by LLMs, so G8 applies.
- Model choice: Claude 3 human-level where GPT-4 and Llama-405B were not (.7 vs .35) [d13].

### 6.4 Caveat for our agent

Almost all numbers are from 2023-2024 chat models. We have no measurement of a current reasoning model on ARN far-vs-near items, on the Anthar goal task, or on load shifts. Our first job is to measure our own base model.

## 7. What our agent should take

Status tags: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Treat surface match as a lure, not as evidence, in O7.** Never accept a mapping or analogue because it looks similar in content. Require the role table to be justified by relations. Basis: the far-vs-near-distractor failure (33.9% on ARN, about 30% on StoryAnalogy) and the retrieval gate effect. Schema: G (anti-surface-match) + O7. [E] K13, K06, K09. Ids: a22, c08, c10, a13, a04.
2. **State the goal before mapping and pass it to O7.** Goals change which mapping people choose, and a mapping made without a goal is under-determined when structure is ambiguous. Schema: S1/S2 feed a goal line into O7. [E] K02. Ids: a09, b05, c19. Caution: the human evidence is one lab and the claim is about humans, so this is a design choice that still gets measured (UNKNOWNS U1), not a promised gain.
3. **Output a typed role table (one source role to one target role) and let code check the one-to-one count.** Violations are allowed but flagged, because one-to-one is soft. Schema: O7, G5. [E] for the soft one-to-one structure (K01); the one-to-many rate (K26) is [S]. Ids: a02, d09.
4. **Randomise option order and run both orders when choosing among candidate analogues.** Count disagreement as unreliability. Schema: G (position bias) in S7. [S] K14, but cost is trivial and the effect (0.89 vs 0.61) is large; adopt as a check, not as a claim of gain. Ids: a21, b22.
5. **When a mapping task needs counting or index arithmetic, delegate it to code.** Schema: G5, tool use. [C] K12, but the counting reading is the best supported (P=.496 with code). Ids: d01, d14.
6. **Flag bistability.** If two mappings are both internally consistent (the Gulf War case), report both and mark the choice as goal-dependent rather than present one as the truth. Schema: S7 SELECT + S9. [E] K05 (same lab). Ids: d07, d08.

### Test first

- **Three-line scoring (relation, feature, goal) vs one holistic choice** at equal tokens (K01 agent_test). [S] as an LLM claim. UNKNOWNS U1/U2.
- **Goal reversal on the Anthar task.** First LLM replication (K22, K30). [S]
- **Goal as tie-breaker only** vs always-apply-goal (K04). [S]
- **Keep top-two mappings alive** vs greedy commitment (K08, K05). [S]
- **Abstract roles first, then map** (K19, K28, K29). [S]
- **Hint-then-choose vs direct** on fresh far items (K28). [S]
- **Explicit "drop what is irrelevant to the goal" step** (K27, K03). [S]
- **Load threshold:** does surface weight rise with relation count in LLMs? (K07). [C]
- **Attention-weighted relation similarity as the scoring rule** (K23). [S]
- **Alternate-rule exploration:** does the agent find valid alternative rules as people do? (K15). [S]
- **Structured analogy for idea generation** (K20). [C]; G8 applies.
- **Self-recalled problem plus explicit mapping step** vs recall only (K21). [S]

## 8. Concrete tests on our bench

All tests: both arms use the same total tokens (count setup and extra calls, G7). At least three seeds. Randomise option order. Report 95% intervals.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Goal reversal | Anthar-style ambiguous-element stories (build 20 new variants, invented countries) with two goals (trade vs membership) | A: goal stated first, then map. B: map, goal not stated. Swap the goal in a second run | Share choosing the goal-congruent mapping; flip rate between goals | A flip of 30 points or more (human: 54 vs 19 and 21 vs 58) if the model uses the goal. A flip near 0 means the model ignores the goal |
| T2 Three-line scoring | ARN far-analogy items and StoryAnalogy MCQ (at least 200 each) | A: single holistic choice. B: score each candidate on relation, feature and goal lines, code sums | Accuracy; accuracy on the far-vs-near-distractor partition | +5 points on the far-vs-near partition (baseline 33.9% for 2024 models; ours unknown) |
| T3 Abstract then map | Same items | A: direct. B: describe roles, then map (YARN-like), code does one-to-one | Accuracy; near-item loss | +10 points far, no more than 3 points lost on near |
| T4 Order and paraphrase robustness | 18 Gentner stories plus a larger new set (100 or more) | Both orders; paraphrased correct story | Disagreement rate between orders; accuracy drop | Order disagreement under 10% for a robust agent |
| T5 Hint-then-choose | Fresh far-analogy set | A: direct. B: hints on causal structure then choose | Accuracy; hint quality | +3 to +7 points (Inani: +6 for 70B) |
| T6 Top-two retention | Ambiguous mapping items (Gulf War style, cross-mapped stories) | A: greedy first mapping. B: carry two mappings, test with a discriminating check | Accuracy on ambiguous items; token use | +5 points or break-even in tokens |
| T7 Goal leakage | Soap-opera Exp3-style items with a goal-relevant and an incidental relation | A: no instruction. B: "ignore what is irrelevant to the goal" | Share mapping by incidental relation (human 65%) | Drop from about 65% toward 35% |
| T8 Load shift | Same story pairs at 2, 4, 6, 8 relations with a surface lure | Plain model only (measurement) | Rate of choosing the object-similar mapping vs relation count | A rise with load would match Krawczyk |
| T9 Counterfactual letter strings | Permuted alphabets, interval 1 and 2 | A: plain. B: code for index conversion | Accuracy | Gap closes, as in d01 |
| T10 Error kind | Letter-string and story errors | Classify as alternate-rule, incorrect-rule, wrong | Share per class | More valid alternatives with an explicit "list other rules" step |
| T11 Goal tie-breaker | Mixed items with structurally clear and ambiguous elements | A: apply goal everywhere. B: goal only when top mappings are within a margin | Accuracy on clear items (should stay about 90%) | B holds clear items, A damages them |

## 9. What does not transfer, and why

- **The constraint-satisfaction network as such.** ACME is a hand-built localist network on predicate-calculus inputs. Our agent maps text and has no such input. Only the idea of separate soft terms transfers. Weights set by hand would have to be tuned on our own data [a02, a12].
- **Human-specific numbers.** 54 vs 19%, 65% vs 35%, and similar describe UCLA undergraduates reading stories. They are not expected values for an LLM. LLMs may be more literal, or follow the goal more cleanly.
- **Working-memory-load explanations.** Krawczyk's load account (LISA) is about limited human working memory. An LLM's limits differ (context, attention). The same surface-weight shift under load may or may not appear [b12, d10].
- **Bistability as a cognitive curiosity.** For an agent the use is a branch-keeping decision, not Necker-cube phenomenology.
- **Pragmatic input as a modeller's hand-set weight.** In ACME the modeller marks the important elements. For us the model must derive the goal from the task, which is a source of error. PAM sidesteps this with fixed attention weights [b15].
- **Analogical prompting and idea-generation results.** These generate sources or ideas. They do not test choosing among mappings and rest on LLM-rated novelty (G8) [a24, c21, a26].
- **Mechanistic patching.** It edits hidden states of open models. A prompt scaffold cannot do it [a23, d15].
- **Letter-string tasks.** Narrow, under-determined, possibly contaminated, number-dependent. Poor proxies for real problem analogies [b20, d03].
- **Metaphor interpretation.** Related, but near-human zero-shot GPT-4 (91.27% vs 94.42%) tells us nothing about choosing among competing mappings [b27].
- **Any claim of independent replication.** We have none for the goal reversal; do not cite it as replicated beyond one lab.

## 10. Open questions

1. Does an LLM reverse its mapping with the goal as people do on Anthar? No test exists (critique GAP 1; d06).
2. Does three-line scoring beat one holistic choice at equal tokens?
3. Does forced abstraction help current reasoning models on ARN far-vs-near items, or only small chat models?
4. Is there a relation-count threshold above which surface similarity gets equal weight in LLMs?
5. Can the counterfactual-alphabet gap be separated from counting with a code-free, counting-free task?
6. How much of story-analogy accuracy survives order shuffling and paraphrase on 2025-2026 models, on a set larger than 18?
7. Is keeping two mappings alive worth the tokens?
8. Does the goal leak into mapping in LLMs, and does an instruction to ignore irrelevant structure change it?
9. Can an independent lab with N over 200 replicate the 1996 effects?
10. How should the weights of the three lines be set: fixed, learned per problem class from S9 records, or chosen by the goal?
11. Does the retrieval gate (semantic overlap needed to retrieve a far analog) hold for LLM memory, where retrieval is by embeddings?
12. Who judges the goal line? If the same model rates goal fit, G4 and G10 apply.

Links to subfields researched in parallel (not covered here): Analogical problem solving, Connectionist and hybrid mapping models, Incremental mapping, Conceptual metaphor theory, Logic and philosophy of analogical arguments, Relational reasoning gap, Language as a tool for relations, Surface-cue heuristics, Debiasing by structure.

## 11. Sources

[V] = opened and read; [M] = snippet or second-hand only. Evidence ids in brackets.

- [V] Holyoak and Thagard (1997) The analogical mind. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/HolyoakThagard.1997pdf.pdf (a01, a08)
- [V] Holyoak and Thagard (1989) Analogical mapping by constraint satisfaction. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Holyoak_Thagard.1989.pdf (a02-a07, b01-b04)
- [V] Spellman and Holyoak (1996) Pragmatics in analogical mapping. https://sites.lifesci.ucla.edu/psych-reasoninglab/wp-content/uploads/sites/273/2021/04/SpellmanHolyoak.CP_.1996.pdf (a09-a12, b05-b09)
- [V] Spellman and Holyoak (1992) If Saddam is Hitler then who is George Bush? https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/SpellmanHolyoak.1992.pdf (d07-d09; a28 was [M] before the gap search)
- [V] Thagard, Holyoak, Nelson, Gochfeld (1990) ARCS. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Thagard_etal1.AI_.1990.pdf (a13, a14)
- [V] Krawczyk, Holyoak, Hummel (2004). https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Krawcyk_Hummel_Holyoak.2004.pdf (a15, b10-b13)
- [V] Hummel and Holyoak (1997) LISA. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Hummel-Holyoak.1997.pdf (a16, a17)
- [V] Spellman, Holyoak, Morrison (2001) Analogical priming via semantic relations. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Spellman_etal.2001.pdf (b17)
- [V] Lu, Ichien, Holyoak (2022) PAM. https://arxiv.org/abs/2103.16704 (b14-b16, c19)
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (a19, a20, b18, b19, c01-c04, c26, c27, d10, d11)
- [V] Lewis and Mitchell (2024) Using counterfactual tasks. https://arxiv.org/abs/2402.08955 (b20, b21, c05)
- [V] Lewis and Mitchell (2025) Evaluating the robustness of analogical reasoning in LLMs. https://arxiv.org/abs/2411.14215 (a21, b22, b23)
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks. https://arxiv.org/abs/2404.13070 (c06, d01, d02)
- [V] Hodel and West (2024) Response. https://arxiv.org/abs/2308.16118 (c07, d03)
- [V] Sourati et al. (2024) ARN. https://arxiv.org/abs/2310.00996 (a22, c08, c09)
- [V] Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/abs/2310.12874 (c10)
- [V] Stevenson, Pafford, van der Maas, Mitchell (2025) Can LLMs generalize analogy solving like children can? https://arxiv.org/abs/2411.02348 (b24, b25)
- [V] Musker et al. (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803 (b28, c11, d12-d14)
- [V] Lee et al. (2025) The curious case of analogies. https://arxiv.org/abs/2511.20344 (a23, d15)
- [V] Inani et al. (2025) Modeling understanding of story-based analogies using LLMs. https://arxiv.org/abs/2507.10957 (d04, d05)
- [V] Khojasteh et al. (2026) YARN. https://arxiv.org/abs/2603.29997 (c20)
- [V] Petersen, Stevenson, van der Plas (2025) Modelling analogies and analogical reasoning. https://arxiv.org/abs/2509.09381 (b29, d06)
- [V] Wijesiriwardene et al. (2023) Neuro-symbolic AI for pragmatic analogies. https://arxiv.org/abs/2308.01936 (b30, c18; no data); ANALOGICAL benchmark https://arxiv.org/abs/2305.05050 (c17)
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 (a24, b26, c15)
- [V] Hu et al. (2023) In-context analogical reasoning. https://arxiv.org/abs/2305.17626 (a25)
- [V] Ichien, Stamenkovic, Holyoak (2023) Novel literary metaphors. https://arxiv.org/abs/2308.01497 (b27, c14)
- [V] Stevenson et al. (2023) Do LLMs solve verbal analogies like children do? https://arxiv.org/abs/2310.20384 (c12)
- [V] Opielka, Rosenbusch, Stevenson (2025) Concept vectors. https://arxiv.org/abs/2503.03666 (c13)
- [V] Liu et al. (2026) Cross-domain mapping and creativity. https://arxiv.org/abs/2603.19087 (a26)
- [V] Shen, Druckmann, Zou (2026) Analogical reasoning for scientific creativity. https://arxiv.org/abs/2605.11258 (c21)
- [V] Donvito and Lieto (2026) Structural ranking of models of analogy. https://arxiv.org/abs/2605.01359 (c22; conceptual scoring only)
- [V] Colhoun and Gentner (2009) Inference processes in causal analogies. https://groups.psych.northwestern.edu/gentner/papers/Colhoun_Gentner_SOFIA_042709.pdf (d16)
- [V] Wikipedia: Analogical reasoning. https://en.wikipedia.org/wiki/Analogical_reasoning (a18; secondary)
- [M] Holyoak and Koh (1987) Surface and structural similarity in analogical transfer. https://doi.org/10.3758/BF03197035 (a27)
- [M] Falkenhainer, Forbus, Gentner (1989) The structure-mapping engine. https://doi.org/10.1016/0004-3702(89)90077-5 (a29)
- [M] Doumas, Hummel, Sandhofer (2008), via Wikipedia (a30)
- [M] Bhavya, Xiong, Zhai (2022) Analogy generation by prompting. https://arxiv.org/abs/2210.04186 (c16; downloaded, not read)
- [M] Das and Balke (2025) From prototypical to relational. https://aclanthology.org/2025.inlg-main.28 (d17; snippet)
- [M] Deep relational reasoning, DeepSeek-R1. https://arxiv.org/abs/2506.23128 (d18; snippet, adjacent task)
- [M] DOI records of founding papers listed in c23-c25 (https://doi.org/10.1207/s15516709cog1303_1, https://doi.org/10.1006/cogp.1996.0019, https://doi.org/10.1207/s15516709cog1904_1); the papers themselves were opened under the ids above.
