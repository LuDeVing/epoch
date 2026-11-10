# Cognitive approaches: deep document

*Subfield D01.08 (philosophy and logic of scientific discovery). Focus: analogy, creativity, mental models. Key works: Hesse; Holyoak and Thagard; Nersessian; Boden. Schema targets: O7 (map an analogue) and O6 (change representation). Evidence ids (a01 to d16) and claim ids (K01 to K24) refer to evidence_a-d.jsonl and claims.jsonl in this folder. Corrections from critique.md are applied.*

Related subfields researched in parallel (links only, not covered here): Analogical prompting for LLMs; Analogy and distant sources; Comparison and relational language; Vector-space relational similarity; Mental spaces; Blend network types; Conceptual change and revolutions; Creative problem solving; Notional machine, mental models; Scientific discovery systems; Novelty measurement; Search over thoughts; Tree of Thoughts. Earlier deep documents (see 00_FIELDS.md) already cover creativity training effects, fixation and distant-analogy grounding in F05/F06; this document does not repeat them.

## 1. What it is

This subfield asks how people (and now models) use one situation to understand another, and how they build and run mental models to get new ideas. Three research traditions meet here.

1. **Analogy as structure mapping.** An analogy pairs a known source with a new target. The useful part is the shared pattern of relations, not the shared surface objects. Gentner's structure-mapping theory and its code form (SME) say this. Holyoak and Thagard's multiconstraint theory (ACME) adds meaning similarity and purpose.
2. **Transfer studies.** Gick and Holyoak (1980-83), Holyoak and Koh (1987), Needham and Begg (1991) measured when people notice and use a source. The result that shaped the field: people can apply an analogy but rarely notice it unaided.
3. **Creativity and mental models.** Boden splits creativity into combinational, exploratory and transformational. Hesse separates positive, negative and neutral analogy (neutral analogy is where new predictions come from). Nersessian argues that scientists build and run mental models using analogy, imagery and thought experiments. (Hesse, Nersessian, Boden and ACME were not opened this session: a23, a24, a26, a27. Their content is from memory and no claim depends on it.)

For our agent the subfield maps onto two operators:

- **O7 Map an analogue**: find a distant problem, write a typed mapping, check it by code.
- **O6 Change representation**: re-express the problem in other terms (objects, counts, symmetry) so the structure shows.

The practical questions are: when does an analogy step help a language model at equal tokens, how should the source be found, how should the mapping be checked, and where does it fail.

## 2. History and theories in depth

### 2.1 Hesse (1966): positive, negative and neutral analogy
Hesse split what two things share. The positive analogy is the known matches. The negative analogy is the known mismatches. The neutral analogy is what is not yet known to match or not. New hypotheses live in the neutral part. The idea survives in SME as "candidate inferences": base facts with no target counterpart get projected onto the target (a06). [M] from memory.

### 2.2 Gentner (1983): structure-mapping
Analogy maps relations, not attributes. Systems of interconnected relations are preferred over isolated matches (the systematicity principle). The 1983 scan was unreadable (a08). The theory is confirmed through the SME paper (a06, a07) and the Wikipedia summary (a25).

### 2.3 Falkenhainer, Forbus and Gentner (1989): the Structure-Mapping Engine
SME is the first implementable version. A mapping pairs base items with target items. It must be one-to-one and structurally consistent: if two relations are paired, their arguments are paired too. Attributes of objects are dropped unless they sit inside a relational structure. SME builds local matches, merges them into global mappings without backtracking, scores them, then emits candidate inferences. Most steps are linear or low polynomial. The final merge step is factorial in the worst case, but typical cases are far better (a07). Worked example: water flow to heat flow. The pressure relation under CAUSE maps to the temperature relation. The isolated relation GREATER-THAN(DIAMETER(beaker), DIAMETER(vial)) is discarded (a06). Limit: the engine receives hand-built symbolic descriptions. It does not find the representation. That is exactly the O6 problem.

### 2.4 Holyoak and Thagard (1989): ACME and multiconstraint theory
Mapping as constraint satisfaction in a connectionist network. Structural, semantic and pragmatic (goal) constraints all push on the mapping. Keane and Brayshaw's incremental model adds working-memory limits. Hummel and Holyoak's later model recasts mapping with distributed codes (a25). [M] ACME itself was not opened (a24).

### 2.5 Gick and Holyoak (1980, 1983): the transfer paradigm
Participants read a story (a general takes a fortress by splitting his army into small groups that converge) and then solve Duncker's radiation problem. Key findings, all opened (a01 to a05, b01 to b04):

- With a hint to use the story, about 75% give the convergence solution. Controls with no story: under 10%.
- With no hint, about 30% (the paper's own summary also says "30% unprompted, 70-75% in total"). The authors infer that only a third or less of those able to use the analogy noticed it unaided.
- Exp 1, cord problem: analog groups 71% vs control 20% before the hint (G2(1)=15.8); 98% vs 30% in total (a02).
- Exp 2: stating the principle on top of the story did not help (32%, 29%, 28% for story plus principle, story only, principle only before the hint; totals 80/79/66; n.s.) (a03).
- Exp 3: a diagram added nothing for spontaneous transfer; diagram alone 1 of 15 (7%) solved unprompted (a04).
- Exp 4: two analogs beat one: 45% vs 21% unprompted (G2(1)=6.35), 80% vs 53% in total. Similar pair 39%, dissimilar pair 52% (n.s.). Schema quality (scored from written descriptions) predicted transfer: 91% of good-schema writers solved without a hint (a05).
- Principle plus diagrams raised good-schema rates (44% vs 10%); two analogs plus diagrams 57% vs 37% unprompted (b03). Poor schema writers solved unprompted 44% with similar analogs vs 12% with dissimilar ones (b04).

### 2.6 Holyoak and Koh (1987): surface and structure
Both surface and structural similarity drive spontaneous retrieval. A laser story with fragile glass (high on both) gave 69% spontaneous convergence solutions; with neither shared, 13%. Noticing ranged from 88% to 13% across the four cells. The two factors were about equal and did not interact. Experiment 1 found substantial transfer even after a delay of days (b05, b06).

### 2.7 Needham and Begg (1991): try first, then see the analog
Five experiments (Exp 5: 142 subjects). Subjects who first tried to solve the training problem and then saw the solution later showed spontaneous transfer above 80%; memory-oriented study above 60%; baseline about 5%. The advantage held at a 15-minute delay. Training attempts nearly always failed, so the benefit comes from the attempt, not success. Story or problem format made no difference (b07, b08).

### 2.8 Spencer and Weisberg (1986): context dependence
Reported no transfer when delay or context change separated source and target. Known only from a search snippet (b09, [M]).

### 2.9 Boden: three kinds of creativity
Creative ideas are new, surprising and valuable relative to a conceptual space. Combinational: unfamiliar combinations of familiar ideas. Exploratory: searching the space under its rules. Transformational: changing the rules of the space. Franceschelli and Musolesi (2025) argue current LLMs reach combinational and exploratory creativity at most, and that transformational creativity is not reachable by current training. This is a conceptual argument with no experiment (a22, b27, c21).

### 2.10 Nersessian (2008): model-based reasoning
Scientists build mental models, run them (simulative reasoning), and extend them through analogy, visual imagery and thought experiments. [M] not opened (a26). Its machine analogue is a code-run simulation (section 4.5).

### 2.11 The LLM era
- 2022: LLMs can generate analogies for explanation (Bhavya et al., c19).
- Dec 2022 to 2023: Webb, Holyoak and Lu claim GPT-3 matches humans on analogy tasks (a12 to a15, c01 to c03).
- 2023 to 2025: counterfactual replications show brittleness (a09, a10, c06); the authors reply that counting, not analogy, explains it (b17, d01, d02).
- 2023 to 2025: analogical prompting (Yasunaga), its critique (Qin) and an equal-budget test (Liu 2025).
- 2025 to 2026: analogy-first idea generation (Shen et al.), execution checks of LLM novelty (Si et al.), relation-aware retrieval of analogs (Barakat and Kochmar).

## 3. Core findings with exact numbers

Status key: established (two or more independent sources), single-source, contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Unaided noticing of a source is rare | about 30% solve unprompted vs about 75% with hint; controls under 10% | a01, b01 | established (K01; one lab 1980-87 plus Holyoak and Koh) |
| Near target: noticing is higher | cord problem 71% vs 20% before hint; 98% vs 30% total | a02 | boundary: closeness of source and target drives noticing |
| Surface plus structure both drive retrieval | both shared 69%; neither 13%; noticing 88% to 13% | b05 | established (K03; matches AnaloBench d06 for LLMs) |
| Two analogs beat one | 45% vs 21% unprompted; 80% vs 53% total; G2(1)=6.35 and 8.36 | a05, b02 | single-source (K02); a student note gives d=0.20, 68% power, N=143, unverified (b10) |
| Schema quality predicts transfer | 91% of good-schema writers solved unprompted; schema grades 21% good, 20% intermediate, 59% poor | a05 | single-source; correlational |
| Stating the principle alone adds nothing | 32/29/28% before hint; totals 80/79/66; p=.36 | a03 | single-source; null, small cells |
| Diagram adds nothing for spontaneous transfer | diagram only 1/15 (7%) | a04 | single-source |
| Try the target first, then see the analog | over 80% vs over 60% memory-oriented vs about 5% baseline; Exp 5 N=142 | b07 | single-source (K04) |
| GPT-3 matches humans on digit matrices | humans N=40; OR 1.88 generative (p=.005); OR 6.27 multiple choice (p=2.3e-8) | a12, c01 | contested (K17; contamination not excluded) |
| GPT-3 on letter strings, zero generalisation | humans N=57; OR 1.76, p=.0007, CI 1.27-2.46 | c02 | contested |
| GPT-3 on far story analogies is weaker than students | humans N=54; OR 0.37, p=.0003; 15 of 54 humans correct on every trial | a15, c03 | single-source |
| LLM letter-string success breaks on altered alphabets | mean accuracy: humans 0.753 (1,876 samples, 136 people); GPT-3 0.488; GPT-3.5 0.350; GPT-4 0.452 | a10, c04 | established (K05) |
| GPT-3 on synthetic alphabet (Hodel and West) | under 0.1 on extend, successor, predecessor, fix; N=50 per condition | a09, c05 | established |
| Alternate-rule errors | GPT-3 5.81%, GPT-4 22.00%, GPT-3.5 38.59% of errors; humans about 15% | a11, b16 | single-source |
| Domain shift hurts every LLM, not children or adults | adults 0.88/0.91/0.89 (N=62); children 0.62/0.66/0.67 (N=41); GPT-4o 0.85/0.63/0.48; Llama-405B 0.79/0.74/0.27; Claude 3.5 0.68/0.62/0.46; Gemma-2 27B 0.60/0.39/0.14 (Latin/Greek/Symbol) | c06 | established (K05) |
| Code access closes the counterfactual gap | humans N=99 and 97; humans vs GPT-4+code P=0.92 (PNAS Nexus; arXiv v2 0.496); humans vs plain GPT-4 P<2e-16; humans vs GPT-4+CoT P=3e-8; code-forbidden model 22.5% vs GPT-4 21.7% | b17, d01, d02 | contested (K06, K23; one group, GPT-4 only) |
| Far narrative analogies are below chance | far: humans 94.1%, models 39.6% (chance 50%); near: 97.9% vs 75.0%; GPT-4 68.1% average; 1,096 triples | a16, c13 | established (K07) |
| Surface distractors drive failure | far analogy vs near distractor: models 33.9% | a16, b21 | established |
| StoryAnalogy hard negatives | chosen 55.8-59.7% (LLaMA-65B 59.7, ChatGPT 59.5, GPT-3.5 55.8; FlanT5 37.2) vs correct 28.6-45.4%; human 85.7%; chance 25% | d07 | established |
| AnaloBench: length kills identification | GPT-4 89.1/66.5/60.7 at 1/10/30 sentences; humans 96.0/72.5/73.3; random 25; retrieval of top-10 of 200 near random | d06 | established |
| Principle first lifts far analogies | up to +30 points on far; near still below zero-shot | c14 | established (K08; ARN plus Codeforces) |
| Restating in structured form lifts models | RAVEN: OPT-1.3B from 20-30% to over 70%; GPT-3 92.6% on one sub-task; 2x2Grid 87.8%, 3x3Grid 93.2% | a18, c16 | established (K09; hand-built encodings) |
| Self-generated analogical prompting: small gains | GPT-3.5 GSM8K 75.0 to 77.8 (5-shot CoT 76.7); MATH 33.0 to 37.3; PaLM2 MATH 27.1 to 34.8; Codeforces Acc@1 GPT-3.5 8 to 13 (knowledge plus exemplars 15; GPT-4 16 to 19) | a19, a20, c08 | contested (K10) |
| Needs a strong model | small models: labelled few-shot CoT won; from davinci-002 up analogical won; K=1 underperforms, K>=3 helps | c09, a21 | single-source |
| Correctness may matter, not relevance | random biology examples about 2.5% better than relevant math (up to 4% on GSM8K); example accuracy 62.0 relevant, 72.0 none, 86.0 random same-type | c10, c11 | contested (K11) |
| At equal budget plain CoT beats analogous prompting | limit accuracy CoT vs AnP: Qwen2.5-7B 88.2 vs 81.3; GLM-4-9B 83.1 vs 77.0; LLaMA-3-8B 71.3 vs 68.2; Phi-3.5-mini 81.4 vs 77.6 | d03, d04 | established (K22) |
| Varied contexts per sample | varied-context beats self-consistency in 5 of 6 pairs (Gemini 1.0); analogical beat ZCoT on 2 of 3 tasks (TSO Ultra 49 vs CoT 78) | d05 | single-source (K24) |
| Analogy-first ideation raises diversity | domain Vendi +100-115%, solution Vendi +90-173%; baselines domain 2.64/2.84, solution 5.81/8.34 | c22 | single-source (K12; preprint) |
| Analogy-first raises judged novelty | Claude 1.6/21.6/50.4%; GPT about 9/27/59%; Gemini about 9/38/69% (no-domain, cross-domain, AR); humans chose AR in 78% of pairs, kappa .445 | c23 | single-source; LLM-judged; text and table differ by under 1 point |
| LLM ideas more novel, less feasible | novelty human 4.84, AI 5.64, AI plus rerank 5.81; 49 writers, 79 reviewers, 298 reviews; about 5% non-duplicate seeds; best self-judge 71.4% | b25, b26 | established (K13) |
| Ideation-execution gap | 19 human and 24 AI ideas, 43 experts, over 100 hours each; overall ideation 4.596 vs 5.382, execution 3.968 vs 3.406; AI lost 1.0 to 2.0 points, human about 0 to 0.6; AI idea r with execution: novelty -0.019, excitement -0.321 | d09, d10 | single-source for size; supports K13 |
| Originality and usefulness trade off | r = -.56 humans, -.61 GPT-3; humans more original (beta .17), GPT-3 more useful (beta .10); 42 humans vs 144 GPT-3 runs | c20 | single-source (K15) |
| Writing with an RLHF-tuned model cuts diversity | 38 writers; InstructGPT lowered lexical and content diversity, base GPT-3 did not | b28 | single-source |
| Simulation as mental model | Mind's Eye: +27.9 points zero-shot, +46.0 few-shot; 39 tasks; GPT-3 1.3B plus simulator 29.8% vs vanilla 175B 29% | c26 | single-source (K19) |
| Relation-aware source retrieval helps a little | sub-concepts: average 0.557 to 0.673; Hit@1 24.5% gold sub-concepts vs 19.5% embedding-only; model-written sub-concepts 18.2% | d11 | single-source (K21) |
| Humans beat the best LLMs on ConceptARC | humans 91%; GPT-4 25%; first-place Kaggle program 52%; GPT-4V 0.23 | c17 | single-source (2023 models) |
| Syllogisms: larger models beat humans yet share biases | best model about 75% on some sets | c27 | single-source |
| Thought Propagation | +12 points optimal shortest-path, +13% human preference in writing, +15% planning completion; authors only | b24, c12 | single-source (K20) |

## 4. Mechanisms and models

### 4.1 Structure-mapping as a code check (G2, O7)
Represent source and target as typed relation graphs: predicates with ordered arguments, with higher-order relations such as CAUSE over relations. A mapping is a partial one-to-one function from source entities to target entities.

1. Build local match hypotheses: pair every source relation with every target relation of the same predicate.
2. Reject a pair if its arguments cannot be paired consistently (one-to-one, parallel connectivity).
3. Merge compatible hypotheses into global mappings (gmaps).
4. Score a gmap by the size of the shared relational structure; deep, connected structure scores higher than loose matches. Object attributes count only inside a relation.
5. Candidate inferences: source relations whose arguments are all mapped but have no target counterpart. These are Hesse's neutral analogy, the new hypotheses (a06, a07).

For our agent the model proposes the typed graphs and the mapping; code checks one-to-one, argument consistency and what the mapping implies for the target (K18). Whether model-written graphs are good enough is untested. The check validates the form of the mapping, not the truth of the inferences. Inferences must still be tested (G3).

### 4.2 Retrieval: why noticing fails and what to do about it
Human retrieval is driven by surface cues plus structure (b05). LLMs are more surface-driven than people: models pick hard negatives with high noun overlap more than the true analogy (d07), and fall to 33.9% when a far true analogy competes with a near distractor (a16). Reading a long bank is near chance (d06). Implementation consequences:

- Do not hope the model recalls a source unaided inside a long context. Either supply the source or run an explicit retrieval step.
- Index candidate sources by relational descriptions (sub-concepts: the relational parts of the system), not by name or topic. Barakat and Kochmar: average retrieval 0.557 to 0.673 with sub-concepts. Top-1 stays low (19.5% embedding-only, 24.5% with gold sub-concepts), and model-written sub-concepts did worse (18.2%) than gold (d11). Expect a weak retrieval step: keep several candidates (top-k) and let code filter each by the mapping check.
- Strip surface content (names, domain words) from the target before querying, to reduce surface pull. This is the O6 step before O7. Not tested (critique gap 9).

### 4.3 The comparison and schema step
Gick and Holyoak: two sources compared and a common principle written gave 45% vs 21% unprompted transfer. Procedure: pick two sources that share the structure, write what they have in common in a short rule, then apply the rule to the target. Stating a rule without comparing did not help (a03), so the comparison is the active part. Written schema quality predicts success (a05), so the agent can score the written rule in code: does it name relations and carry no source-domain nouns?

### 4.4 Principle-first matching (K08)
In ARN, having the model state each story's message (its proverb) before comparing lifted far-analogy accuracy by up to 30 points, but made near analogies worse than zero-shot (c14). In Codeforces, knowledge first then examples gave the best result (15% vs 13%, a20). Implementation: use it only when the first match was surface-near and the target is structurally far, or at impasse. Route by case type, never by default.

### 4.5 Run the mental model (O6, G3)
Mind's Eye: a physics engine simulates the described scene and its result is put into the prompt (c26). Webb's reply: code execution fixed position counting (d01). Both give the model the job of writing a runnable model and give code the job of running it. Implementation: for an analogy whose source has a codable causal model (flow, queue, spring, graph), have the model write a small program of the source structure, rebind it to the target, run it, and compare to known target cases. Untested outside physics and counting (critique gap 10).

### 4.6 Re-representation (O6)
RAVEN: naming entities, then decomposing into components and attributes, lifted GPT-3 175B to 77.6-92.6% on sub-tasks and OPT-1.3B from 20-30% to over 70% (a18, c16). Ordinal naming beat random naming by over 20 points in large models. Implementation: a restatement slot that outputs objects, attributes and relations in a fixed typed form. Caveat: the encodings were hand-built. Whether a model-written restatement gives the same lift is open.

### 4.7 Analogy-first ideation pipeline (open mode)
Shen et al. (c22, c23): per problem, first produce many candidate source domains, then build a solution from each analogy, then dedupe. This raised diversity by 90-173% (Vendi) and judged novelty. The mechanism is a diversity-forcing step that pushes samples to different domains, much like the program-tracked direction history in S3. Si et al. (d09) warn that novelty edges vanish after execution. So the pipeline must be followed by code-run validation (G8).

### 4.8 Boden operators for the schema (O8 link)
- Combinational: pair two sources and combine (O7).
- Exploratory: search within the rules of the space (S3 history tracking).
- Transformational: change one rule of the space (O4 drop a constraint, O8 reframe). There is no empirical LLM test (K14).

## 5. What holds up

### 5.1 Replications and independent confirmation
- **Surface plus structure both matter for retrieval.** Human data (Holyoak and Koh) and three LLM benchmarks (ARN, StoryAnalogy, AnaloBench) agree that surface similarity pulls retrieval (K03, K07).
- **Letter-string brittleness.** Hodel and West, Lewis and Mitchell and Stevenson et al. are three independent groups. All find that GPT-3, 3.5, 4, GPT-4o, Claude 3.5, Llama-405B and Gemma fall under alphabet or domain changes while humans do not (K05).
- **Equal-compute weakness of fancy prompting.** Liu et al. (6 models) and Wang et al. (budget-aware) agree: plain CoT with voting matches or beats complicated strategies (K22).
- **LLM novelty is not diverse and not reliably judged.** Si 2024, Si 2025, the Shen 2026 baselines and Padmakumar and He agree on low diversity (K13).

### 5.2 Failed or weak replications and contradictions
- **Webb 2023 vs counterfactual results.** Webb's GPT-3 results may be contaminated by training exposure (the authors flag it). Counterfactual tests broke them. The reply shows GPT-4 with code recovers (P=0.92 in the published version, 0.496 on arXiv v2). Both sides agree plain GPT is brittle. They disagree on why (K05 established, K06 contested).
- **Yasunaga vs Qin.** Self-generated relevant analogs help (GSM8K +2.8, MATH +4.3 for GPT-3.5), yet irrelevant but correct examples do as well or better (Qin). This weakens the claim that analogy is the active ingredient (K11).
- **Gick and Holyoak: principle.** The principle alone did not add to the story (a03), yet principle plus diagrams raised schema quality (b03). Different conditions and measures. A principle alone is not reliably better.
- **ARN chain of thought.** Gains up to 30 points on far analogies but lowers near ones (c14). The gain depends on case type.
- **Human classics.** All are 1980-91 student studies from few labs. No large independent replication is in the file. A student power note puts the two-analog effect at d=0.20 (unverified, b10). The Alfieri, Nokes-Malach and Schunn (2013) meta-analysis of case comparison is the right source but its numbers were not read (d14). Do not quote an effect size from it.
- **Spencer and Weisberg.** Reported no transfer under delay or context change (snippet only, b09), against Holyoak and Koh who found transfer after days (b06). Unresolved here.

### 5.3 Moderators and boundary conditions
- Source-target closeness (cord problem 71% unprompted vs radiation about 30%).
- Order: attempt then analog (b07).
- Number of sources: two beat one (a05).
- Model size: self-generated analogs need a strong model; small models do better with retrieved labelled examples (a21, c09). One example underperforms; three or more help.
- Case type: near vs far (c14).
- Task type: analogical prompting beat zero-shot CoT on FOLIO and RACO but lost on TSO (Ultra 49 vs 78) (d05).
- Compute: equal-sample comparisons reverse the gains (d03).
- Length: AnaloBench accuracy falls as stories lengthen (GPT-4 89.1 to 60.7).
- Distractors: semantic distractors cost GPT-4 about 0.6-0.8, Claude 3 and Llama-405B about 0.4-0.5 in match to reference, against a modest drop for humans (d08).

### 5.4 Interventions that worked
- Provide the source rather than leave it to recall (K01).
- Compare two sources and write the shared rule (K02, single-source).
- Principle-first matching on far cases (K08).
- Structured re-representation (K09).
- Code-run models (Mind's Eye; code on letter strings) (K19, K23).
- Varied example context per sample (K24, weak).
- Analogy-first domains for diversity (K12, single-source).

### 5.5 Interventions that did not work
- Stating the principle alone (a03). A diagram alone (a04).
- Zero-shot analogical prompting at equal tokens against CoT voting (d03).
- Model-written sub-concepts for retrieval (18.2% vs 19.5% embedding-only) (d11).
- Instructions to prefer system mappings did not fix near-distractor failure (a16).
- Human reranking of AI ideas did not remove the execution gap (d09).
- Self-judgement of ideas: best model 71.4% on predicting accepted papers (b26).

## 6. Language models

### 6.1 Analogy benchmarks, by era
- **GPT-3 (2022-23), Webb et al.** Matched or beat UCLA undergraduates on digit matrices (N=40; OR 1.88 generative, 6.27 multiple choice), letter strings (N=57; OR 1.76) and SAT-style verbal analogies (374 items), with human-like difficulty patterns (item correlation r(30)=0.39). Weaker than students on far story analogies (N=54; OR 0.37). Prompt format mattered (a12 to a15, b13, c01 to c03). Training exposure not excluded.
- **Counterfactual tests (2023-25).** Hodel and West: GPT-3 under 0.1 on synthetic-alphabet extend, successor, predecessor and fix tasks. Lewis and Mitchell: all three GPT models below humans overall (0.35-0.49 vs 0.753) and falling with each added permutation while humans stay flat. Comprehension checks were mostly 0.9 to 1.0, so the models knew the new alphabet. Stevenson et al. extend this to 2024 frontier models: GPT-4o 0.85 to 0.48, Llama-405B 0.79 to 0.27 across Latin, Greek and symbol alphabets; children and adults flat (a09, a10, c04 to c06).
- **Why it fails.** Webb's reply: counting and position tracking, not analogy. With self-chosen code execution GPT-4 matched humans (P=0.92 published), CoT alone did not (P=3e-8 vs humans), and a code-capable model told not to run code scored 22.5% vs 21.7% for plain GPT-4. GPT-4 found the letter interval only 10.8% of the time. One research group, GPT-4 only (d01, d02, d15).
- **Narrative analogies.** Near analogies are handled (75.0%) and far ones fall below chance (39.6% vs humans 94.1%). A far analogy against a near distractor: 33.9%. Few-shot CoT that states each story's message lifts far items by up to 30 points (a16, c13, c14). StoryAnalogy and AnaloBench confirm the surface pull (d06, d07).
- **Mapping with distractors (Musker et al. 2025).** GPT-4, Claude 3 and Llama-405B match humans in default conditions, differ when random or semantic words distract (drops 0.4-0.8 vs a modest human drop). Authors conclude LLMs offer a how-possibly account only (a17, d08).
- **Abstraction (ConceptARC).** Humans 91%, GPT-4 25%, GPT-4V 0.23, top Kaggle program 52% (c17). 2023 models.
- **No 2025-26 reasoning-model result** was found for letter-string counterfactuals or ARN far items (d12). Treat the picture as brittle-for-plain-models, unknown-for-reasoning-models.

### 6.2 What changed performance, by how much
| Change | Effect | Evidence |
|---|---|---|
| Code execution (self-chosen) on counterfactual letter strings | plain GPT-4 below humans (P<2e-16) to parity (P=0.92) | d01 |
| Chain of thought on the same task | still below humans (P=3e-8); GPT-4 vs GPT-4+CoT P=0.004 | d01 |
| Structured decomposed encoding of RAVEN | OPT-1.3B 20-30% to over 70%; GPT-3 up to 92.6% | a18, c16 |
| Simulator output in the prompt | +27.9 zero-shot, +46.0 few-shot absolute; 1.3B plus simulator equals 175B | c26 |
| Stating message first (far narrative analogy) | up to +30 points far; worse on near | c14 |
| Self-generated analogs (GSM8K, GPT-3.5) | 75.0 to 77.8 (vs 5-shot CoT 76.7) | a19 |
| Self-generated analogs (MATH, GPT-3.5) | 33.0 to 37.3 | a19 |
| Knowledge plus exemplars (Codeforces Acc@1, GPT-3.5) | 8 to 15 | a20 |
| Random correct biology examples vs relevant self-generated | +2.5 average, up to +4 on GSM8K | c10 |
| Analogous prompting vs plain CoT at equal budget | -3 to -7 points (e.g. 81.3 vs 88.2) | d03 |
| Oracle per-question strategy and sample allocation | LLaMA-3-8B MATH-500 15.2 to 61.0 (needs oracle labels; models cannot do it alone) | d16 |
| Relational sub-concepts for source retrieval | average 0.557 to 0.673; Hit@1 19.5% to 24.5% | d11 |
| Analogy-first ideation | solution Vendi +90-173%; novelty judged 1.6% to 50.4% (Claude) | c22, c23 |
| Writing with InstructGPT (not base GPT-3) | lower lexical and content diversity across authors | b28 |

### 6.3 Creativity and ideation
- LLM ideas are rated more novel (5.64 vs 4.84) and slightly less feasible by blind experts; seed ideas are about 95% duplicates; self-judgement is weak (best 71.4%) (b25, b26).
- After 100-hour execution, AI idea scores fell 1.0 to 2.0 points and human ideas about 0 to 0.6, erasing the AI lead; review scores before execution barely predict scores after (d09, d10). Small N (19 and 24 ideas).
- Humans score higher on originality and surprise on the Alternative Uses Task, GPT-3 on utility; originality and utility trade off (r=-.56 and -.61) (c20).
- Analogy-first generation is the one scaffold in this file that raises diversity at large scale, with LLM-judged novelty and four biomedical tasks (c22, c23). It is a 2026 preprint.
- Domain case studies (LacMaterial, SciMON) show analogy prompts producing candidate lists, with no wet-lab or large-sample validation (c24, c25).
- Transformational creativity: argued, not measured (a22).

### 6.4 Analogical prompting at equal cost
Yasunaga reported gains against unmatched baselines. Liu et al. (6 models, 8 strategies, 6 benchmarks) compared strategies at equal sample count or token price. Plain CoT led analogous prompting on 4 of 6 models by 3 to 7 points; the other two were within 1 point (d03). Wang et al. found CoT self-consistency matches or beats debate and Reflexion at 20 queries or 10k tokens (d04). The tested form is the generic one-pass "recall related problems" prompt on maths and science QA. A two-source O7 with a written common rule on structure-bound tasks has not been tested at equal tokens.

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested. Schema parts: G, S, O, memory.

### Add now (established)

1. **Do not rely on unaided recall of a source (O7, S6).** Code or the retrieval step supplies candidate sources; the model does not "remember" one inside a long context. [E] K01, K03. Evidence a01, b01, b05, d06.
2. **Check surface-change twins after any mapping (G3).** After an analogical mapping or a rule inferred from examples, rerun on a surface-changed twin (altered symbols, renamed entities) and require the same answer. [E] K05. Evidence a09, a10, c04, c06.
3. **Treat surface similarity as a known failure of source choice (O7).** When picking among candidate sources, run the mapping check on each and prefer the one with the larger shared relational structure, not the one with matching words. [E] K03, K07, K16. Evidence a16, b21, d06, d07, d08.
4. **Use analogies only at impasse and in open mode, never on routine problems (G1, G11, O7).** Equal-compute tests show plain CoT with voting beats analogical prompting on maths and science QA. This agrees with the existing schema text. [E] K22. Evidence d03, d04, d16.
5. **Hand counting, indexing and exact position work to code (G5, G2).** Letter-string failures are largely counting; code removes the gap in the one test run. Use code for counting steps; this is cheap and safe even though the analogy reading is contested. [E for "plain models are brittle" K05; the code fix itself [C] K06]. Evidence d01, d02, d15.
6. **Re-represent into a typed, decomposed form before mapping (O6, S2).** Structured restatement lifts the same model by large margins (RAVEN, Mind's Eye). Keep the original wording beside it (existing S1 rule). [E] K09, with the caveat that gains used hand-built encodings. Evidence a18, c16, c26.
7. **For far-case matching, state the abstract message first (O7).** Only when the case is structurally far; skip when near. [E] K08. Evidence c14, a20.
8. **Do not let the generator be the final selector of ideas (G8).** LLM ideas are rated more novel yet lose their lead after execution; the generator's self-judgement is weak. [E] K13. Evidence b25, b26, d09, d10.
9. **Do not add analogy training instructions or a generic "think of an analogy" line (section 4b).** Gains are small and fall behind plain CoT at equal cost. [E] K22.

### Test first

1. **Two sources plus a written common rule (O7).** [S] K02. Evidence a05, b02, b03; human-only, one lab, student note d=0.20.
2. **Attempt the target first, then show the analog (O7, S5/S6).** [S] K04. Evidence b07, b08; human-only. Risk: a failed attempt in context may anchor the model.
3. **Relational-description retrieval of sources from the subgoal library (memory, O7).** [S] K21. Evidence d11, d06. Top-1 hit rates are low, so test whether top-k plus code filter beats keyword or embedding retrieval.
4. **Surface-stripped re-description before retrieval (O6 then O7).** [S] K16 (indirect). Evidence d07, d08.
5. **Typed mapping check by code (G2).** [S] K18. Evidence a06, a07. Does a code check of one-to-one and argument consistency beat model self-assessment of mapping quality?
6. **Analogy-first generation in open mode (S3 open, O7).** [S] K12. Evidence c22, c23; novelty LLM-judged, so require our own retrieval-based novelty check and a code-run validity check.
7. **Code-run mental model of the source (G3, O6).** [S] K19, K23. Evidence c26, d01. Test beyond physics and counting.
8. **Varied analog per sample (S3).** [S] K24. Evidence d05; old models.
9. **Principle-first only on far cases (O7).** Known from ARN; test the routing rule (near vs far detection by code) rather than the effect itself.
10. **Self-generated vs retrieved vs code-verified analogs (O7).** [C] K10, K11. Evidence a19, a21, c10, c11, d03. Decide whether correctness or relevance carries the gain.
11. **Originality plus code-testable usefulness selection (G8).** [S] K15. Evidence c20.
12. **Rule-change operator for transformational search (O4, O8).** [S] K14. Evidence a22. No empirical support; needs a task that requires changing the space.
13. **One-layer analog-and-revise (Thought Propagation) (O7, S5).** [S] K20. Evidence b24, c12; author-only baselines.

## 8. Concrete tests on our bench

All tests: both arms get the same total token budget (including setup and any retrieval). Arms are compared against best-of-N plain sampling at the same tokens (G7). Report solve rate with a binomial confidence interval and the per-state token log.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-like and matrix items with a known structural twin in the library (u1) | A: plain best-of-N. B: O7 with source supplied by scaffold. C: O7 with source left for the model to recall | solve rate on held-out items | B over C by 10+ points if K01 transfers; B vs A unknown, likely small |
| T2 | Counterfactual letter strings (permuted alphabets, symbol alphabets, 3 interval sizes) | A: plain model. B: plain plus code tool. C: reasoning model, code available but optional; log whether code is chosen | accuracy per alphabet type; gap to flat-human level | B near parity per Webb; C unknown (critique gap 2) |
| T3 | Far-analogy retrieval with planted surface distractors (ARN-style, 200-source store) | A: embedding retrieval. B: keyword. C: typed relational description index plus code mapping check, top-5 | Hit@1, Hit@5 of the structural match; distractor-pick rate | C Hit@5 above A Hit@5 by 10+ points; distractor rate below 40% |
| T4 | Structure-bound tasks (altered-rule matrix items, rule-shift puzzles) | A: best-of-N CoT. B: O7 with two sources and a written common rule, then solve. C: O7 one source | solve rate | B over C by 5+ points (K02 transfer); B vs A decisive for adoption |
| T5 | Same items as T4 | A: read analog first. B: attempt first (capped tokens), then read analog | solve rate; rate of anchoring on the failed attempt | B over A by 10+ points (K04); watch anchoring |
| T6 | Same items, surface-changed twin of every item | A: re-description before mapping. B: no re-description | pair-consistency (same answer on twin); accuracy | A higher consistency by 10+ points |
| T7 | Items with known causal structure (queue, flow, spring, graph) | A: model-only mapping. B: model writes and runs a small simulation of the source, then maps | accuracy on target prediction items | B over A by 10+ points |
| T8 | Open-mode problems (NoveltyBench-style plus 20 science-style problems with a code check) | A: plain isolated attempts. B: S3 open mode with program-tracked history. C: B plus analogy-first domain list | Vendi diversity, retrieval-based novelty, code-validated validity rate | C over B on diversity by 20+ percent; validity must not drop |
| T9 | Subset of T4 split into near and far cases | A: direct matching. B: principle-first matching | accuracy per case type | far gain 10+ points, near not worse than 3 points lower |
| T10 | Recalled analog types on maths and code items | A: none. B: self-generated relevant. C: irrelevant but correct. D: code-verified recalled case | accuracy; example accuracy | D over A, and C not below B (tests K11) |
| T11 | Ideation items with a runnable usefulness check | A: select on originality only. B: select on originality plus check pass | pass rate of selected ideas; originality rating | B higher pass rate at small originality loss |
| T12 | Rule-change tasks (the solution needs a space-rule change) | A: plain sampling. B: O4/O8 rule-change operator | solve rate | B over A on this class only; if not, drop O8 as a creativity claim |

## 9. What does not transfer, and why

- **Human spontaneous retrieval from memory.** People forget the source; the model has no episodic memory across calls (a15 notes GPT-3 cannot retrieve past episodes). The relevant analogue for us is a retrieval index, not forgetting. The human finding transfers only as "do not rely on unaided noticing".
- **Gick and Holyoak effect sizes.** One lab, student samples, small cells (n 20 to 47), one ill-defined puzzle, and a reported small effect (d=0.20, unverified). Treat the direction as a hypothesis and the numbers as not usable for planning.
- **Mapping engine inputs.** SME needs hand-built symbolic relations. Models do not reliably produce them, and we have no data on error rates.
- **Hand-built encodings in RAVEN and UTOPIA.** The big gains came from human-written representation or a physics engine. We cannot assume a model-written restatement gives the same lift.
- **Analogical prompting gains on GSM8K and MATH.** These are contaminated, solved-by-CoT tasks. Gains are 1 to 4 points and vanish at equal budget. They do not tell us about structure-bound tasks.
- **Webb's "emergent analogy" headline.** GPT-3 era, possible contamination, breaks on altered alphabets.
- **LLM-judged novelty.** Shen et al. use LLM judges plus a pairwise human check (kappa .445). Our G8 forbids this as a selector.
- **Boden's transformational creativity as a design target.** No operational test exists. Do not add an "invent a new conceptual space" step.
- **Principle statements and diagrams as human-style aids.** Stating the principle alone had no effect on humans (a03) and diagrams added nothing (a04).
- **Educational analogy generation (Bhavya; Barakat and Kochmar).** Aims at explaining to students, not solving; use only the retrieval numbers.
- **Syllogistic bias results (Eisape).** Mental-model theory for syllogisms is not an operator in our schema.

## 10. Open questions

1. At equal tokens, does O7 with two sources and a written common rule beat best-of-N plain sampling on non-contaminated structure-bound tasks? No paper controls for compute here.
2. Do 2025-26 reasoning models, with and without code, still fail counterfactual letter strings and far ARN cases? No published test found.
3. Is the benefit of recalled analogs correctness or relevance? Does code-verified recall resolve it?
4. Can relational descriptions find far analogs in a store at a useful hit rate, given 17.5-24.5% Hit@1 at best in the one test found?
5. Does the Needham and Begg order (attempt first) transfer to agents, or does a failed attempt anchor the model?
6. Do Shen et al.'s analogy-first diversity gains survive an independent novelty check and validity by code?
7. Is there any measurement of transformational creativity in agents?
8. How large are the original Gick and Holyoak effects at proper power? (Alfieri, Nokes-Malach and Schunn 2013 not read.)
9. Does surface stripping before mapping reduce distractor pull, and by how much?
10. Does the code-run mental model extend beyond physics and counting to causal and social domains?
11. Why does the Spencer and Weisberg null (delay, context change) disagree with Holyoak and Koh (transfer after days)?
12. Does error in the model-written typed relation graph dominate the benefit of a code mapping check?

## 11. Sources

[V] opened (page or PDF text read in this run series; critique re-opened the ones noted there), [M] snippet or memory only.

| Mark | Source | URL | Ids |
|---|---|---|---|
| V | Gick and Holyoak (1983) Schema induction and analogical transfer | https://www.gwern.net/doc/psychology/1983-gick.pdf | a01-a05, b01-b04 |
| V | Holyoak and Koh (1987) Surface and structural similarity in analogical transfer | https://link.springer.com/content/pdf/10.3758/BF03197019.pdf | b05, b06 |
| V | Needham and Begg (1991) Problem-oriented training promotes spontaneous analogical transfer | https://link.springer.com/content/pdf/10.3758/BF03197150.pdf | b07, b08 |
| M | Spencer and Weisberg (1986) Context-dependent effects on analogical transfer | https://doi.org/10.3758/BF03197019 | b09 |
| M | Student replication note of Gick and Holyoak (d=0.20, unverified) | https://rstudio-pubs-static.s3.amazonaws.com/449388_16364e2a6bc94601a5a223469a1a5d60.html | b10 |
| M | Alfieri, Nokes-Malach and Schunn (2013) Learning through case comparisons (metadata only) | https://doi.org/10.1080/00461520.2013.775712 | d14 |
| V | Falkenhainer, Forbus and Gentner (1989) The Structure-Mapping Engine | https://groups.psych.northwestern.edu/gentner/papers/FalkenhainerForbusGentner89.pdf | a06, a07 |
| V (unreadable scan) | Gentner (1983) Structure-mapping | https://groups.psych.northwestern.edu/gentner/papers/Gentner83.pdf | a08 |
| V | Wikipedia, Analogy (cognitive science section) | https://en.wikipedia.org/wiki/Analogy | a25 |
| M | Boden (2004) The Creative Mind (memory) | none | a23 |
| M | Holyoak and Thagard (1989) Analogical mapping by constraint satisfaction (memory) | none | a24 |
| M | Nersessian (2008) Creating Scientific Concepts (memory) | none | a26 |
| M | Hesse (1966) Models and Analogies in Science (memory) | none | a27 |
| V | Webb, Holyoak and Lu (2023) Emergent analogical reasoning in LLMs | https://arxiv.org/abs/2212.09196 | a12-a15, b11-b13, c01-c03 |
| V | Hodel and West (2023) Response | https://arxiv.org/abs/2308.16118 | a09, b14, c05 |
| V | Lewis and Mitchell (2024) Counterfactual tasks | https://arxiv.org/abs/2402.08955 | a10, a11, b15, b16, c04, d12 |
| V | Webb, Holyoak and Lu (2024) reply, arXiv | https://arxiv.org/abs/2404.13070 | b17 |
| V | Webb, Holyoak and Lu (2025) PNAS Nexus version | https://sites.lifesci.ucla.edu/psych-cvl/wp-content/uploads/sites/162/2025/08/A149.Webb-et-al.PNAS-nesus.pdf | d01, d15 |
| V | Webb et al. arXiv 2404.13070 v2 | https://arxiv.org/html/2404.13070v2 | d02 |
| V | Stevenson, Pafford, van der Maas and Mitchell (2025) Can LLMs generalize analogy solving like children can? | https://arxiv.org/abs/2411.02348 | b18, c06, c07 |
| V | Sourati et al. (2024) ARN: Analogical Reasoning on Narratives | https://arxiv.org/abs/2310.00996 | a16, b20, b21, c13, c14 |
| V | Musker, Duchnowski, Millière and Pavlick (2025) LLMs as models for analogical reasoning | https://arxiv.org/abs/2406.13803 | a17, b19, c15, d08 |
| V | Hu, Storks, Lewis and Chai (2023) In-context analogical reasoning | https://arxiv.org/abs/2305.17626 | a18, c16 |
| V | Yasunaga et al. (2024) LLMs as analogical reasoners | https://arxiv.org/abs/2310.01714 | a19-a21, b22, b23, c08, c09 |
| V | Qin et al. (2025) Relevant or Random | https://arxiv.org/abs/2404.12728 | c10, c11 |
| M (abstract and cost section skimmed) | Yu et al. (2024) Thought Propagation | https://arxiv.org/abs/2310.03965 | b24, c12 |
| V | Liu et al. (2025) Rethinking the role of prompting strategies in test-time scaling | https://arxiv.org/pdf/2505.10981 | d03, d16 |
| V | Wang et al. (2024) Reasoning in token economies | https://arxiv.org/html/2406.06461v1 | d04 |
| V | Google DeepMind authors (2025) Enhancing reasoning with collaboration and memory | https://arxiv.org/html/2503.05944v1 | d05 |
| V | Ye et al. (2024) AnaloBench | https://arxiv.org/html/2402.12370v2 | d06 |
| V | Jiayang et al. (2023) StoryAnalogy | https://arxiv.org/html/2310.12874 | d07 |
| V | Barakat and Kochmar (2026) Teaching through analogies | https://arxiv.org/pdf/2605.24211 | d11 |
| M | Das and Balke (2025) From prototypical to relational (snippet) | https://preview.aclanthology.org/dashboard/2025.inlg-main.28 | d13 |
| V | Mitchell, Palmarini and Moskvichev (2023) Humans, GPT-4 and GPT-4V on abstraction tasks | https://arxiv.org/abs/2311.09247 | c17 |
| V | Wijesiriwardene et al. (2023) ANALOGICAL benchmark | https://arxiv.org/abs/2305.05050 | c18 |
| V | Bhavya, Xiong and Zhai (2022) Analogy generation by prompting LLMs | https://arxiv.org/abs/2210.04186 | c19 |
| V | Stevenson et al. (2022) GPT-3 creativity, Alternative Uses Test | https://arxiv.org/abs/2206.08932 | c20 |
| V | Franceschelli and Musolesi (2025) On the creativity of LLMs | https://arxiv.org/abs/2304.00008 | a22, b27, c21 |
| V | Shen, Druckmann and Zou (2026) Unlocking LLM creativity in science through analogical reasoning | https://arxiv.org/abs/2605.11258 | c22, c23 |
| V | Guo (2025) LacMaterial | https://arxiv.org/abs/2510.22312 | c24 |
| V | Wang et al. (2024) SciMON | https://arxiv.org/abs/2305.14259 | c25 |
| V | Li et al. (2022) Mind's Eye | https://arxiv.org/abs/2210.05359 | c26 |
| V | Eisape et al. (2024) Syllogistic reasoning in humans and language models | https://arxiv.org/abs/2311.00445 | c27 |
| V | Si, Yang and Hashimoto (2024) Can LLMs generate novel research ideas? | https://arxiv.org/abs/2409.04109 | b25, b26 |
| V | Si, Hashimoto and Yang (2025) The ideation-execution gap | https://arxiv.org/pdf/2506.20803 | d09, d10 |
| V | Padmakumar and He (2024) Does writing with language models reduce content diversity? | https://arxiv.org/abs/2309.05196 | b28 |
