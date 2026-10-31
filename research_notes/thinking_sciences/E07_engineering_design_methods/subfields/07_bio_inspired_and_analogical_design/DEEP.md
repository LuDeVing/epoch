# Bio-inspired and analogical design: deep document

*Subfield E07.07. Focus: retrieval of analogues (Helms, Goel; Chakrabarti). Schema link: O7. Evidence ids (a01 to d17) are in evidence_a-d.jsonl; claim ids (K01 to K32) are in claims.jsonl (full id E07.07-Kxx); cross-check notes are in critique.md. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Design by analogy means solving a design problem by finding a solved problem in another place and carrying its idea across. Bio-inspired design (BID) is the special case where the other place is biology. The hard step is not mapping an analogue once you hold it. The hard step is finding it. This document is about that step: retrieval.

Retrieval has four parts.
- **Cue.** The text or idea you search with. It can be raw problem text, a reframed problem, or a function description.
- **Index.** How stored analogues are described: surface text, function, mechanism, or a structured model (Structure-Behavior-Function, SAPPhIRE).
- **Match.** How cue and index are compared: keyword, embedding, structure mapping, LLM judgement.
- **Check.** Whether the retrieved item truly fits: relevance, mapping, feasibility.

Why it matters for our agent (schema part O7, pull in an analogue): a language model holds a huge store of solved problems in its weights. It still fails to use them unless cued (K15, K16). The schema question is how to build a cue, an index and a rerank step that find structural analogues, at what token cost, and whether the result beats simply drawing more samples.

Two things set BID apart from ordinary analogy work (Goel 2015, a10): the source is cross-domain by definition, and problem and analogue change each other during search ("co-evolution"). Retrieval is also interactive: people search online, read, reframe, and search again (a08).

## 2. History and theories in depth

**Cognitive base (1980s to 1990s).** Gick and Holyoak (1983) showed that people rarely notice a useful analogue unless told to look. In their experiment 2, 29% (8 of 28) solved the target problem without a hint and 50% (14 of 28) with one (quoted in c13). Retrieval is driven by surface similarity; mapping by structure. Two models formalise this. Both were read only second-hand here (a24, a25, status [M]).
- **ARCS** (Thagard, Holyoak, Nelson, Gochfeld 1990): retrieval as constraint satisfaction. Semantic, structural and pragmatic similarity act together.
- **MAC/FAC** (Forbus, Gentner, Law 1995): a cheap content-vector scan (MAC) picks candidates, then a structure-mapping engine (FAC) scores them. This is the same shape as a modern "pull wide, rerank" pipeline (K13, K29).
- **Case-based reasoning** (Kolodner) is named as the third base theory (a09). It is covered in a parallel subfield; link only.

**Georgia Tech BID studies (2006 to 2013).** Goel, Helms, Vattam and colleagues watched about 350 students in a cross-disciplinary course (83 projects; a10, a05).
- Helms et al. 2008 (a01 to a04); journal version 2009 (a26, not opened): two processes. *Problem-driven*: define the problem, reframe it in biological terms, search, pick a source, extract the principle, apply. *Solution-based*: start from a biological solution, extract the principle, look for a problem. In 2006, 4 of 9 course projects were solution-driven; in 2007, 5 of 10.
- The reframing step ("biologizing") builds the cue. Example: "stopping a bullet" became "what characteristics do organisms have that enable them to prevent, withstand and heal damage?" (a02). Instructors gave four search heuristics: change constraints, champion adapters, variation within a solution family, multi-functionality. None was tested against a baseline.
- Compound analogy: a design often combines several sources, one per sub-problem. Applying an analogy creates new sub-problems that need new retrievals (a04). Example: the i-Fabric team joined beehive phase-change wax with wood-stork and arctic-wolf heat bypass.
- Vattam and Goel 2013 (a08, a09): finding a source is mostly online search. Three difficulties: findability, recognisability, understandability. In one embedded team, 39 relevant articles took about 3 person-hours each; 53 false positives were logged. They model retrieval as ARCS plus Information Foraging Theory (Pirolli), because memory here is an external information environment.
- Representation work: SR.BID (Helms and Goel 2013, a13) adds problem-side categories (environment, performance criteria, constraints, deficiencies) to Structure-Behavior-Function so problems can be matched to biology. Coding 5 random statements matched 129 of 147 concepts (87.8%). Design patterns (e.g. Hydrophobia and Hydrophilia from a fog-harvesting net, 42-design corpus) are proposed as the unit of transfer (a15, a11).
- Tool support: AskNature (functionally indexed), IDEA-INSPIRE, DANE, Biologue (a12). Building one organism's structured description takes 40 to 100 hours (c10), so hand-built libraries stay small.

**Chakrabarti line.** SAPPhIRE is a causal model that encodes a system at several abstraction levels so analogues can be matched on mechanism. Majumder, Bhattacharya, Chakrabarti (2024) automate the encoding with retrieval-augmented GPT (c11). The original Chakrabarti papers were not opened in this run.

**Distance debate (2007 to 2024).** Is a far analogue better than a near one?
- Christensen and Schunn 2007 (a23, title only) and Linsey et al. 2012 WordTree (a22, abstract only) are the usual human references. Numbers not obtained.
- Chan et al. 2011 (b01 to b06, d02): the large controlled test. See section 3.
- Fu et al. 2013 (a21, b10, d16, abstract and snippets only): near and far are relative to the problem, and a "sweet spot" lies between. Not verified; no peak distance can be cited (K32).
- Goucher-Lambert et al. 2020 (b07 to b09): adaptive near or far stimuli did not change novelty; the stimulus's own innovation score mattered.

**Machine retrieval from text (2017 to 2026).**
- Analogy mining (Hope et al. 2017, b11 to b13): purpose and mechanism vectors retrieve product analogies better than surface text. Follow-ups: Hope 2022 (b14), Kang 2022 (b15), Sultan and Shahaf 2022 (b16).
- BARCODE (Emuna 2023, c07 to c09): mine Wikipedia for challenge and strategy sentences.
- LLM era: Zhu 2022 fine-tuned GPT-3 on AskNature (c01 to c06); Ding 2023 and Ma 2023 tested GPT-3 as an inspiration source (b26, b27); AnaloBench and StoryAnalogy measured LLM retrieval (b17, c30, c31); 2026 work on cross-field retrieval (c28, c29, d08, d09, c20) and on explicit analogy prompting (d10, d11, d12).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Two ways in: problem-driven and solution-based. Solution-based is common. | 4 of 9 (2006) and 5 of 10 (2007) course projects; 27/74 cases (36.5%) in the meta-analysis | a01, a05, a08 | [E] K01 |
| Reframing the problem in function terms opens retrieval. | Example "stopping a bullet" to "prevent, withstand, heal damage". No measured gain from the step itself. | a02 | [E] K02 (direction backed by b11, c28) |
| Solution-based designs are more often multifunctional. | 22/27 (81.5%) vs 14/47 (29.8%), Fisher p<0.001; 36/74 (48.6%) multifunctional overall; kappa 0.88 | a05 (re-checked) | [E] K03 |
| Fixation on the first source is common but not tied to solution-based design. | Fixation 50/74 overall; 19/27 (70.4%) solution-based vs 31/47 (66%) problem-driven, n.s. The 2008 claim rested on 2 of 9 projects (nacre armour). | a03, a06 | [C] K04 |
| Compound analogy is frequent in human teams and goes with problem-driven design. | 6/9 (2006), 4/10 (2007); problem-driven plus compound p=0.008 and p=0.001 (two coders) | a04, a07, a08 | [E] K05 |
| Unaided people retrieve surface matches, not structural ones. | Story cues: surface 13/21 (61.9%) vs 5/43 (11.6%); higher-order 5/42 (11.9%), chi2(1,N=64)=7.107, p=.008. Exp 2 (N=239): 22/59 (37.3%) vs 13/120 (10.8%). Exp 3 (N=121): 7/35 (20.0%) vs 4/86 (4.7%) | a18, a19 | [E] K06 |
| A hint to use an analogy helps only a little. | HR problem 20.3% to 37% (17/46); factory 6.3% to 8.7% (4/46); Gick-Holyoak 29% to 50% | c13 | [E] K07 |
| Far-field examples raise novelty only when also uncommon. | Far + less-common vs control: mean novelty d=1.14, max novelty d=1.29. Far alone, less-common alone: no difference. N about 151-153, 9 cells + control | b01, b03, d02 | [S] K08 |
| Far analogies cost quantity and raise variance; common examples narrow breadth. | Quantity far vs near d=-0.30; variability of quality far vs near d=0.64, vs control d=0.78; breadth more-common vs control d=-1.03. Mean and max quality unchanged | b02, b05, d02 | [S] K09 |
| Mid-session near or far stimuli did not change novelty. | n=20 per group. Near: feasibility d=0.5 (p=0.05). Far: usefulness d=1.1 (p<0.01). Stimulus innovation vs outcome r=0.67. Convergence near 0.33 vs far 0.13 | b07 to b09 | [S] K10 |
| Function-only (purpose) representation retrieves better analogues. | Top-1% precision 0.739 vs TF-IDF 0.63; top-25% only 0.478 vs 0.399; recall at top 1% about 0.02. Good ideas 0.71 vs 0.28 (TF-IDF) vs 0.27 (random); 38 workers, 749 ideas, 249 good; k=3: 0.56 vs 0.16 | b11, b12 | [S] K11 |
| Domain-stripped skeletons and strategy mining beat raw text. | Skeleton AP 0.222 to 0.513 (18 families, 109 papers), whole fingerprint 0.557; BARCODE 72% vs 36% (top 7), 69% vs 29% (top 15) | c28, c07, c08 | [E] K12 |
| Generic embeddings are weak; an LLM rerank is strong. | Best of 11 retrievers Recall@10 0.26 (chance 0.07); LLM tournament rerank 0.81 (151-candidate pool); fine-tuned 4B 0.70; HyDE 0.16 to 0.44 | c29, d08 | [E] K13 |
| Rerank is capped by first-stage recall. | 404k-sentence pool: gold in tuned top 100 for 57 to 81% of queries; rerank then keeps it in the top 10 for 72 to 87%; rerank adds 8.4 to 15.5 MRR@10 points | d09 | [E] K29 |
| LLMs fall behind humans on long-story analogy choice. | GPT-4 89.1/66.5/60.7 vs human 96.0/72.5/73.3 at 1/10/30 sentences; gaps 6.9/6.0/12.6 (paper text says 28.8: error). Claude-v2 68.2/30.2/25.9; chance 25 | c30, d03 | [C] K14 |
| LLMs are near chance at finding analogues in a bank. | T2 GPT-4-Turbo P@3 42.9/6.5/3.9 at 1/10/30 sentences; random 3.9. StoryAnalogy: humans 85.7%, ChatGPT about 30%, davinci-003 37.1%, chance 25% | d04, b17 | [E] K15 |
| GPT-4 does not retrieve spontaneously but maps well when cued. | Radiation analogy 1/15 unprompted; precision and recall 0.00 unprompted; hinted recall 1.00, precision about 0.52 | c14 | [S] K16 |
| LLM analogy ability on standard tasks is real but brittle. | GPT-4 vs humans on altered alphabets P=8.9e-13; with code execution P=0.496 | b19 to b22 | [C] K17 |
| Self-generated exemplars give small gains for strong models. | GSM8K GPT-3.5: 75.0, 75.8, 76.7, 77.8 (+1.1 over best baseline); davinci-003 14.8 (0-shot), 54.0 (5-shot), 61.0; PaLM2 80.7 to 81.7. Irrelevant examples match or beat relevant: 71.5 vs 75.5 | c16, d06, d01 | [C] K18 |
| The exemplar gain is a within-prompt process effect. | No-CoT GSM8K GPT-4.1 48.8 / 57.9 (integrated) / 49.1 (decoupled); about +1 with CoT | d07 | [S] part of K18 |
| Model-made analogies match humans only at the largest scale. | Meaningful, target only: 1.90, 15.61, 48.29, 70.05% (0.3B to 175B) vs human 66.67% | b25 | [E] K19 |
| LLM inspiration helps but some is harmful and diversity is low. | Helpfulness median 4/5, reformulation 80%, up to 25% potentially harmful (480 analogies) | b26, b27, c19 | [E] K20 |
| Raising novelty costs feasibility. | BioSpark N=12: novelty 3.9 to 7.1, value 3.8 to 7.0, feasibility 6.8 to 5.7; ideas 5.5 to 10.3; species 4.6 to 8.2 | d14 | [E] K31 |
| Fine-tuned bio-design generators over-use near sources. | Birds in over 50% of retrieved analogues; classifier pass 58 to 84%; relevancy accuracy 75.3, 79.8, 94.4% | c01 to c04 | [E] K21 |
| Biology lookup is costly for people. | 3.36% of 3,416 articles gave design insight; 40 to 100 h per organism description; about 3 person-hours per relevant article | c10, a08 | [E] K22 |
| Explicit analogy beats plain and cross-domain prompts on diversity and novelty. | Binary novelty 50.4/58.8/68.9% vs 21.6/28.2/37.8% vs 1.6/9.0/8.9% for three frontier models; 2 calls vs 1 or 2 | d12 | [S] K26 |
| LLMs show source-domain homogeneity. | Baselines about 5% unique domains (7-8 of 150); best diversity-prompted model only 0.49; free-form source choice picked Computer Science 947 times (domain entropy 0.326) | d11, d12, c21 | [E] K27 |
| For strong models a summary step gets most of a structure step. | Sonnet-4.6 direct 2.24, summary 3.91, self-reflection 4.11, structural decomposition 4.17 (15 events, LLM judge) | d10 | [S] K28 |
| ChatGPT repeats itself in design. | Unique terms 67.4% vs 78.2% human award entries; 7/10 noticed (N=10) | d15 | [S] K30 |
| TRIZ pipelines are moderately accurate. | AutoTRIZ 7/10 textbook cases; TRIZ-GPT few-shot recall 0.675 to 0.245 (34 cases) | c25, c26 | [E] K24 |
| Mapping a given analogy is easier than finding one. | ARCANA hard tasks: best model about 48 to 51% vs humans 58 to 69% | c23, c24 | [E] K25 |

## 4. Mechanisms and models

Written so an engineer can build each part.

**4.1 Two entry points (K01).**
- *Problem to source.* Input: task text. Steps: (1) write a function-level restatement; (2) retrieve sources for it; (3) map the best source back.
- *Source to problem.* Input: a source item the agent already holds (a solved case, a stored pattern). Steps: (1) write its mechanism as a skeleton; (2) ask which open sub-problems it could solve; (3) test the match. Use this when something useful turns up by chance; Goel calls this serendipity (a11).

**4.2 Reframe into a function cue (K02, K12).** One LLM call turns the problem into a domain-free statement: "How to [verb] [object] under [constraints]." Strip nouns that name the domain. Keep the verb, the quantity that must change, and the constraints. Cross-Pollination uses a query of this shape (d08). Cache the result; reuse it in every retrieval.

**4.3 Index by skeleton, not by surface (K12).** For each stored item, one LLM call at write time produces a "mechanism skeleton": what is done, to what, by what means, with no domain words. Kulikowski (c28) went from AP 0.222 on abstracts to 0.513 on skeletons. Store three fields: surface text, purpose (what it is for), mechanism (how it works). Hope et al. (b11) found purpose-only best at the top of the ranked list, and "near purpose, far mechanism" best for good ideas (b12).

**4.4 Two-stage retrieval (K13, K29).**
1. Stage 1: cheap and wide. Embed the skeleton and take the top 100 or more. Recall of the gold item in the top 100 is the ceiling (57 to 81%, d09). A fine-tuned embedder or a HyDE-style rewrite raises it (c29: BM25 with HyDE 0.16 to 0.44).
2. Stage 2: LLM rerank on structure. A tournament works: split 151 candidates into groups, keep winners, then score the final 10 one by one (d08). Recall@10 0.81 against 0.26 for the best embedder. The judge sees only skeletons, never authorship or earlier scores (G5).
3. Cost. Reranker token cost was not reported in the source. Count it in our own runs.

**4.5 Trigger (K15, K16).** The model does not volunteer the analogy (1/15). Two options. (a) A forced step "list 3 problems with the same structure, from different domains" before solving. (b) External retrieval, which does not depend on the model noticing. Puranam found that a hint produced false claims: with a hint GPT-4 claimed wrong sources about half the time (precision about 0.52). Every claimed analogue needs a mapping check.

**4.6 Mapping and check (K25, K31).** After retrieval, write the correspondence table: source element to target element, and what must hold for the idea to work. Then run a feasibility critic with fixed questions (does the mechanism need a property the target lacks? what scale or material limit breaks it?). The classic failure is the nacre armour case: the analysis showed the design 100 times too weak and 10 times heavier than Kevlar (a03). A critic that sees the numbers catches that. BioSpark (d14) shows that without a critic, feasibility falls 1.1 points on a 10-point scale as novelty rises.

**4.7 Source ledger (K27, K30).** Code keeps a list of source domains already used in this run. A second pass must pull from a domain not in the list. The model's own picks are poorly spread (about 5% unique domains), so the program must enforce it. Measure same-source repeats.

**4.8 Distance and timing (K08 to K10, K32).** Do not set a numeric distance target. Measure distance on function, not appearance. Human evidence suggests: show examples after a first unaided phase (b01, b13); use far and uncommon examples for divergence, near for repair; filter afterwards because far raises variance.

**4.9 Self-generated exemplars (K18).** Prompt: "recall 3 related solved problems, then solve." Gains come from extra reasoning inside one prompt (d07). Treat as a cheap variant to test, not as the retrieval mechanism.

## 5. What holds up

**Replications and meta-analyses**
- *Multifunctionality of solution-based BID*: confirmed in the 2021 meta-analysis over 74 cases (a05). Two coders, kappa 0.88. Still one institution, students, no control group.
- *Fixation caused by solution-based design*: did NOT replicate (a06): 70.4% vs 66%. The authors suggest teaching may have changed behaviour. The 2008 claim rested on 2 fixating projects out of 9. Treat as unsupported. [C]
- *Surface-dominated human retrieval*: replicated and extended (Dekel 2021, a18, a19). The higher-order effect is real but small (11.9% in the story contrast; 4.7 to 37% across experiments). Letter-string cues failed to reach significance (20% vs 10%, p=.283). Preprint.
- *Hint effect in strategy problems*: Puranam 2025 replicated Gick-Holyoak with two problems; effects were small (6.3 to 8.7%, 20.3 to 37%) against 29 to 50% in the original (c13).
- *Far-field benefit*: only one lab has the large test (Chan 2011). Goucher-Lambert 2020 found no novelty effect from adaptive stimuli. Fu 2013 said the picture is "relative", not "far is better". The slogan "far analogies give more novel ideas" is conditional on uncommon examples. [S]
- *Webb 2023 emergent analogy*: partly challenged by Lewis and Mitchell 2024 on counterfactual letter strings; partly restored by Webb 2024 with code execution (P=0.496 vs humans). Depends on task and tools. [C]
- *Yasunaga analogical prompting*: tested with controls by Qin 2024. Irrelevant self-made examples matched or beat relevant ones on math (GSM8K 71.5 relevant vs 75.5 not-applicable). Gwak 2026: the gain is a within-prompt effect and shrinks to about +1 with CoT. Source numbers: +1.1 over the best baseline for GPT-3.5 on GSM8K. Large gains are for weak models only. [C]

**Moderators found**
- Commonness of the example (Chan): more common narrows breadth (d=-1.03 vs control).
- Stimulus quality over distance (Goucher-Lambert): r=0.67 between stimulus innovation and outcome innovation.
- Story length (AnaloBench): gap to humans grows with length; retrieval from a bank collapses past one sentence.
- Model scale (Bhavya): meaningful analogies 1.90% at 0.3B, 70.05% at 175B.
- First-stage recall (RATIO): caps the rerank.
- Domain collaboration (Farzaneh 2020, a16, a17): supported engineer-biologist pairs transferred more correct analogies (5 pairs per cell, 196 ideas; alpha 10% used for some claims). Unsupported pairs were not significantly better. Weak evidence.

**Interventions that worked**
- Function or skeleton re-description before retrieval (c28, c07, b11).
- LLM rerank over a wide pool (c29, d08).
- Fine-tuning retrievers on analogy or citation pairs (c29: 4B model 0.70; 0.6B 0.12 to 0.50).
- Explicit analogy generation for diversity and novelty on frontier models (d12).
- A hint, for LLMs, to switch on mapping (c14), at a precision cost.
- Code execution for symbolic analogy tasks (b22).
- BioId support templates for human pairs (a17).

**Interventions that did not work or backfired**
- Few-shot examples in TRIZ contradiction analysis: recall 0.675 to 0.245 (c26).
- Training retrievers on three standard retrieval sets lowered AnaloBench nDCG (c29).
- Diversity tricks (top-k, top-p, entropy steering): more diversity, less quality (Mistral-7B quality 4.32 to 4.21 for diversity 0.33 to 0.53; d11). Effects vary by model.
- Reflection loops for historical analogy ran in only about 10% of cases; more than five candidates added tokens but little gain (c32).
- Relevant self-generated exemplars on math (d01).
- Far stimuli added mid-session: lower usefulness (d=1.1), no novelty gain (b08).

**Known data problems.** AnaloBench text says a 28.8-point gap at 30 sentences; its tables give 12.6 (d03). Its Table 4 subset gives GPT-4 22.7, below chance, so do not cite (d05). Chan 2011 cell counts sum to 151, not 153 (d02). Zhu 2022 classifier numbers changed between preprint versions (c06). The Lewis and Mitchell model-to-accuracy assignment is inferred (b21); do not cite by model. Fu 2013, Linsey 2012 and Christensen and Schunn 2007 were not read in full, so no sweet-spot distance exists in this record.

## 6. Language models

**Standard analogy tasks: strong.** GPT-3 was above the estimated high-school average on 374 SAT analogies and matched or exceeded humans on digit matrices and verbal analogies (b19). GPT-4 was near perfect on near story analogies (b20). GPT-3 did not reach significance on far story analogies (p=0.065) while humans did (OR 0.37, p=0.0003).

**Altered tasks: brittle.** On permuted or symbol alphabets, GPT models fall sharply (b21). GPT-4 with code execution matches humans (P=0.496, b22). Reading: part of the failure is counting, not analogy.

**Choosing a given analogue: depends on length.** AnaloBench T1 accuracy at 1/10/30 sentences: GPT-4 89.1/66.5/60.7; GPT-3.5 65.3/46.4/30.8; Claude-v2 68.2/30.2/25.9; human 96.0/72.5/73.3 (c30, d03). Gaps 6.9, 6.0, 12.6. The human 30-sentence value is only 30 items. GPT-4 does as well on Claude-written stories (57.6 vs 60.7), so this is not self-preference. Claude-v2 is near chance at 10 and 30 sentences. All models are from 2023.

**Finding an analogue in a bank: near chance.** AnaloBench T2 (200+ stories): GPT-4-Turbo P@3 42.9 at one sentence but 6.5 and 3.9 at 10 and 30 (random 3.9). StoryAnalogy: ChatGPT about 30% vs 25% chance, humans 85.7% (b17). Models pick surface-similar hard negatives as often as the true analogue (b18). No 2025 or 2026 frontier model was found on these benchmarks (d04). This is the biggest hole in the record.

**Spontaneous use: almost none.** GPT-4 used the radiation analogy in 1 of 15 unprompted runs but chose the near-surface dolphin story 14 of 15; with a hint recall was 1.00 and precision about 0.52 (c14). The authors argue the weak step is causal matching rather than retrieval (c15). Models fail from surface similarity; humans fail from subtler causal misreadings.

**Prompting for self-recall.** Yasunaga (c16, d06): GPT-3.5-turbo GSM8K 75.0 / 75.8 / 76.7 / 77.8 (0-shot, 0-shot CoT, 5-shot CoT, self-generated). text-davinci-003 14.8 / 50.3 / 54.0 / 61.0. PaLM2 60.8 / 78.2 / 80.7 / 81.7. MATH GPT-3.5 33.0 / 33.9 / 34.9 / 37.3. Codeforces Acc@1 GPT-3.5-16k 8, 9, 11, 15; GPT-4 16 to 19. One exemplar hurts; 3 to 5 is best (c17). Qin 2024 (d01; GPT-3.5-turbo, 500 items, 3 seeds): GSM8K relevant 71.5 vs unrelated 75.5; example accuracy mattered (MATH: relevant examples 62% correct vs random-same 86%). Gwak 2026 (d07; no CoT): GPT-4.1 48.8 to 57.9, GPT-4o 49.9 to 54.6, Llama-3.1-8B 12.1 to 16.5. Decoupled reuse of the examples gave almost nothing. With CoT about +1. The no-CoT baselines sit far below known scores, so part of the gain is extra reasoning text. Not tested: reasoning models, non-math tasks.

**Embedding, rewrite and rerank (2026).**
- Cross-Pollination (c29, d08): 1,300 queries, 26 fields, 151 candidates. Best embedder Recall@10 0.26; LLM tournament rerank 0.81; fine-tuned 4B embedder 0.70; HyDE with BM25 0.16 to 0.44.
- RATIO (d09): 404k pool; GPT-5-mini listwise rerank adds 8.4 to 15.5 MRR@10 points; first stage caps it.
- Kulikowski (c28): skeleton AP 0.513 vs 0.222; the trained scientific embedder SPECTER was lowest (0.095, lifted to 0.334 by the fingerprint).
- Idea-Catalyst (c20 to c22): Qwen3-14B with metacognitive steps, novelty +21.38% and insightfulness +16.22% over guided dual retrieval; N=6 human check; judge gpt-oss-120b.
- Analogical Deep Research (d10): deep-research agents with frontier backbones mostly match surface features. For Sonnet-4.6: direct 2.24, summary 3.91, reflection 4.11, structural decomposition 4.17. Only 15 events, LLM judge, no equal-token control.

**Generation of analogies and designs.**
- Bhavya 2022 (b25): meaningful analogies 70.05% for 175B, target only, vs human 66.67%.
- Ding 2023 (b26): 480 GPT-3 analogies; median helpfulness 4/5; reformulation 80%; up to 25% potentially harmful.
- Ma 2023 (b27, c19): GPT-3 solutions more feasible and useful but less novel than crowd; few-shot pulls toward crowd; a unique adjective gave the lowest mean cosine similarity 0.746.
- Zhu 2022 (c01 to c05, d13): fine-tuned GPT-3 retrieves near animals (birds over 50%); open input gave more novel and less feasible concepts. Human feasibility check: about 6 concepts, 9 usable raters.
- BioSpark (d14): GPT-4-turbo sparks plus mechanism clusters raised ideas and species; novelty 3.9 to 7.1; feasibility 6.8 to 5.7 (N=12).
- Shen 2026 (d12): explicit analogy generation on Claude Sonnet 4.5, GPT-5.2, Gemini 3 Flash. Binary novelty 50.4/58.8/68.9% vs cross-domain 21.6/28.2/37.8% vs plain 1.6/9.0/8.9%. Diversity metrics up 90 to 173%. Humans judged analogical outputs more novel 78% of the time. No best-of-N arm, no feasibility score.
- Shen 2026 diversity (d11): ten recent LLMs show domain homogeneity; best diversity-prompted model 0.49.
- Chen 2025 (d15): ChatGPT chair concepts 67.4% unique terms vs 78.2% human.
- Majumder 2024 (c11): RAG-based SAPPhIRE models; groundedness 0.81, answer relevance 0.86, context relevance 0.79; LLM judge, three artificial systems.
- TRIZ: AutoTRIZ matched 7 of 10 textbook cases (c25); TRIZ-GPT recall by prompt style 0.675 / 0.691 / 0.245 / 0.247 for basic / CoT / few-shot / both (c26); solution-generation similarity 0.829 vs 0.823 to 0.824, no prompt effect (c27).
- Other: historical analogy (c32): free generation beat dataset retrieval by 0.25 on the authors' metric. ARCANA (c23, c24): best model 48 to 51% vs humans 58 to 69%; a concept-slippage-execute loop solved 9 of 17 hard tasks (selected for low direct accuracy).

**What moved the numbers.** (1) A function or skeleton rewrite: AP x2.3. (2) An LLM rerank over a wide pool: Recall@10 x3.1 over the best embedder. (3) A hint or explicit analogy instruction: flips use from 1/15 to near-certain, with false claims. (4) Code or tools for symbolic tasks. What did not generalise: the self-recall prompt on strong models with CoT.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Relevant guardrails: G4 samples from one model are not independent; G5 code selects; G7 every element must pay at equal tokens; G8 novelty is judged by running, not by opinion.

### Add now (established)

1. **Function-level restatement before any analogue search.** Part: S1/S2 and O7. [E] K02, K12; a02, b11, c28, c07. Rewrite the problem as a domain-free "how to" statement and search with that. Keep the original wording beside it.
2. **Index memory by skeleton and purpose, not surface.** Part: memory. [E] K12; c28, c07, c08. Write a domain-stripped skeleton once, at write time.
3. **Two-stage retrieval: wide pull then LLM rerank on structure.** Part: O7 and memory. [E] K13, K29; c29, d08, d09, c28. Pull the top 100 or more; spend tokens on the rerank, not on query rewriting. The rerank sees no authorship or earlier scores (G5).
4. **Do not rely on the model to find analogues unaided.** Part: O7. [E] K15; d04, b17, c14, b18. Use external retrieval or a forced listing step.
5. **Check every claimed analogue by mapping.** Part: O7 and S4. [E] K25, K19; c23, b25, c14. Write the correspondence and test it with a judge that sees no source label. A hint raises false claims to about half.
6. **Keep a source ledger of domains used.** Part: G (diversity) and S3. [E] for the problem (K27; d11, d12, c21, c04). The forced-second-source remedy is untested (see Test first, item 4).
7. **Add a feasibility critic after any novelty step.** Part: S4 and O7. [E] K31, K20; d14, c05, a03, b26. Novelty gains came with feasibility losses; up to 25% of outputs were potentially harmful.
8. **Report cost per relevant analogue.** Part: G7. [E] K22; c10, a08. Humans pay about 3 person-hours per relevant article.
9. **Allow both entry points and a small cap of compound analogies.** Part: O7. [E] K01, K05; a01, a05, a08. Both paths are common in human practice.

### Test first (single-source, contested, or no equal-token evidence)

1. **Explicit analogy step vs best-of-N at equal tokens.** O7/S3. [S] K26; d12. The only frontier-model result has no best-of-N arm and no feasibility score.
2. **Forced "list analogous problems" trigger.** O7. [S] K16; c14. GPT-4 only, 15 runs.
3. **Self-recall prompt ("recall related problems").** O1/O7. [C] K18; c16, d01, d06, d07. Likely near zero with CoT on strong models.
4. **Forced second, different source reduces same-source repeats.** G diversity, S3. [S] K30, K27; d15, d11. Effect unmeasured.
5. **Skeleton vs purpose-only vs full text on one bank.** memory. [S] K11, K12; b11, c28. Different banks in each paper.
6. **Structure decomposition vs plain summary before retrieval.** O1/O7. [S] K28; d10.
7. **Far vs near, common vs rare, and timing.** O7. [S] K08 to K10; b01, b07. Human evidence only, one problem each.
8. **Compound analogy vs single best source.** O5/O7. [E] for humans (K05), no LLM test.
9. **Domain-expert sub-role.** roles. [S] a16, a17; 5 pairs per cell.
10. **Long source descriptions: compress then match.** O7. [C] K14; c30, d03.

## 8. Concrete tests on our bench

All arms get the same token budget, counted including setup, retrieval and rerank calls (G7). Judges see no arm label and no authorship (G5). Where an item has a check, score by the check.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Open-ended design or idea items (NoveltyBench-style) plus a feasibility rubric | A plain best-of-N; B explicit analogy (find a cross-domain problem with the same relational structure, borrow its solution); C analogy plus feasibility critic | Distinct-idea count, blind-judged novelty, feasibility pass rate | B beats A on novelty (d12); feasibility drops (d14); C recovers most of it |
| T2 | Bank of 200+ solved cases with known analogue pairs (AnaloBench T2 or StoryAnalogy plus our own cases) | A model picks from raw bank text; B embedding top 10; C skeleton embedding top 100 then LLM rerank to 10; D C without the rewrite | Recall@10, MAP, tokens per hit | C beats B widely (0.26 to 0.81 in c29); A near chance |
| T3 | Problems with a known structural analogue (Gick-Holyoak style, 15+ runs per variant) | A plain solve; B "use an analogy" hint; C forced listing of 3 analogous problems; D external retrieval of the analogue | Solve rate, share of correct source used, share of false analogues claimed | B and C raise use but add false claims (c14); D raises solve rate with fewer false claims |
| T4 | Reasoning items with checks (maths, code) | A zero-shot CoT; B self-recall prompt; C fixed few-shot | Accuracy at equal tokens | B within +/-1 point of A for a strong model (d07) |
| T5 | Same as T1, 20 runs per problem | A plain; B source ledger forcing a different second source | Same-source repeats, unique domains per 150 samples, quality | B cuts repeats; quality no worse (generic diversity tricks cost quality, d11) |
| T6 | Mixed bank with surface-matched decoys | A raw problem text cue; B function-abstracted cue; C both | Share of top-10 that are structural vs surface matches | B raises the structural share (K02, K12) |
| T7 | Design items with near/far x common/rare example cells | Four example conditions plus none | Mean and max novelty, variance, feasibility, quantity | Only far + rare lifts novelty (b03); variance rises (b05); a filter is needed |
| T8 | Long case descriptions (10 and 30 sentences) | A raw choice; B compress to 3 lines then choose | Accuracy | B closes part of the 12.6-point gap (c30) |
| T9 | Multi-constraint design items | A single best source; B two to three sources merged | Constraint coverage, feasibility | B higher coverage and cost; compound analogy was common in human teams (6/9, 4/10) |
| T10 | Forecast or foresight style items | A direct; B summary then retrieve; C structure decomposition then retrieve | Judge score and tokens | B gets most of C for a strong model (d10) |

## 9. What does not transfer, and why

- **Human fixation findings.** The solution-based fixation story (a03) failed to replicate (a06). It rested on 2 projects, students told about fixation, and coder judgement. LLMs have their own fixation (same-domain homogeneity, d11), which must be measured directly.
- **Cost of lookup.** Human costs (40 to 100 hours per organism, about 3 hours per article) do not apply to an LLM that reads in seconds. What matters is token cost per relevant hit.
- **Hand-curated libraries.** AskNature and DANE are small and slow to build; our memory can be built by a program. A model fine-tuned on AskNature-style items only replays known success stories (c01 limit).
- **Far-is-better slogans.** Human evidence is one lab, one problem, patent examples and students (b01). For an LLM the cost of a bad far example is a wasted rerank slot, and the benefit is not shown.
- **Biology-specific content.** The bird bias (c04) shows biology retrieval clusters near. The general lesson (cross-domain skeleton retrieval) transfers; the biological content does not.
- **Math and symbolic tasks.** Analogue retrieval does not help where the model already has the procedure; the exemplar gain is explained by extra reasoning text (d07, d01).
- **Small panels and LLM judges.** Many LLM-design studies use 9 raters, 6 PhD users, or LLM judges (c05, c22, d10). Effects are suggestive only.
- **Fine-tuned retrievers.** We do not train. Fine-tuning gave large gains (c29: 0.6B from 0.12 to 0.50), but the transferable result is the zero-shot rerank (0.81).
- **Human memory models** (ARCS, MAC/FAC) describe a person's memory, not an external store. The two-stage shape transfers; the parameters do not.

## 10. Open questions

1. At equal tokens, does explicit analogy retrieval beat best-of-N for reasoning and design on a current strong model? No paper tests it (d12 lacks the arm).
2. Which index works best: skeleton, purpose-only or full text with rerank, on one shared bank? K11 and K12 used different data.
3. What do 2025 to 2026 models score on AnaloBench T2 and StoryAnalogy? No result found (d04).
4. Does the Yasunaga effect hold for reasoning models and on non-math tasks (d07)?
5. What distance is best? Fu 2013, Linsey 2012 and Christensen and Schunn 2007 were not obtained (d16, a22, a23).
6. Do forced second sources reduce LLM source-locking (K30)? Do compound analogies help LLMs?
7. What share of LLM bio-inspired concepts survive blind expert feasibility checks? Only about 6 concepts and 9 raters exist (d13).
8. What triggers spontaneous analogy use, and what does a cheap trigger cost in false positives (K16)?
9. Does a domain-expert sub-role help beyond Farzaneh's 5 pairs per cell?
10. Chakrabarti's SAPPhIRE papers and the original ARCS and MAC/FAC papers were not opened. Would a structured causal model (SAPPhIRE, SBF) beat skeleton text for retrieval?
11. Is the AnaloBench human-GPT-4 gap really 12.6 points at 30 sentences? The human value rests on 30 items.

## 11. Sources

Key: [V] opened and read this session; [M] snippet or abstract only.

**Georgia Tech and BID line**
- [V] Helms, Vattam, Goel, Yen, Weissburg (2008) Problem-driven and solution-based design (ACADIA). https://cbid.gatech.edu/wp-content/uploads/2018/04/Helms_et_al_2008_Acadia.pdf (a01 to a04)
- [M] Helms, Vattam, Goel (2009) Biologically inspired design: process and products. Design Studies 30(5). https://doi.org/10.1016/j.destud.2009.04.003 (a26)
- [V] Goel and Hancock (2021) Multifunctional and domain independent? Design Science. https://www.cambridge.org/core/journals/design-science/article/multifunctional-and-domain-independent-a-metaanalysis-of-case-studies-of-biologically-inspired-design/154F3753DF4E95D9DFE0E7344E3D4542 (a05 to a07)
- [V] Vattam and Goel (2013) Seeking bioinspiration online. https://www.designsociety.org/download-publication/34599/seeking_bioinspiration_online_a_descriptive_account (a08, a09)
- [V] Goel (2015) Is biologically inspired invention different? ICCC. https://computationalcreativity.net/iccc2015/proceedings/3_1Goel.pdf (a10, a11)
- [V] Goel (2015) BID, a new paradigm for AI research on computational sustainability. https://cdn.aaai.org/ocs/ws/ws0139/10205-45937-1-PB.pdf (a12)
- [V] Helms and Goel (2013) Grounded knowledge representations for BID (ICED13). https://www.designsociety.org/download-publication/35084/grounded_knowledge_representations_for_biologically_inspired_design (a13)
- [M] Vattam, Helms, Goel (2010) A content account of creative analogies in BID. AI EDAM. https://www.cambridge.org/core/journals/ai-edam/article/content-account-of-creative-analogies-in-biologically-inspired-design/C888A14108C7962EC2CCAA0D04974C03 (a14; abstract page only, although the log marks it opened)
- [V] Goel et al. (2011) Design patterns and cross-domain analogies. https://cdn.aaai.org/ocs/2480/2480-10848-1-PB.pdf (a15)
- [V] Hashemi Farzaneh (2020) Bioinspired design: engineers and biologists. https://link.springer.com/content/pdf/10.1007/s00163-020-00333-w.pdf (a16, a17)
- [V] Goel and Shu (2015) Analogical thinking editorial. https://web.archive.org/web/20180728110954id_/https://www.cambridge.org/core/services/aop-cambridge-core/content/view/04B58C66108E065AC575E174246C5BAC/S0890060415000013a.pdf (a27)

**Human retrieval and distance**
- [V] Dekel, Burns, Goldwater (2021 preprint) Leaping across the mental canyon. https://osf.io/download/xrdmj/ (a18, a19)
- [V] Chan et al. (2011) Benefits and pitfalls of analogies for innovative design. https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/2011-jmd-distancecommonness.pdf (b01 to b06, d02); [M] abstract at https://doi.org/10.1115/1.4004396 (a20)
- [M] Fu et al. (2013) The meaning of near and far. https://doi.org/10.1115/1.4023158 and https://www.lrdc.pitt.edu/Schunn/papers/fuchanetal-near-far-2013.pdf (a21, b10, d16; full text not obtained)
- [M] Linsey, Wood, Markman (2012) WordTree. https://doi.org/10.1115/1.4006145 (a22)
- [M] Christensen and Schunn (2007) Analogical distance and function. https://doi.org/10.3758/bf03195939 (a23)
- [V] Goucher-Lambert, Gyory, Kotovsky, Cagan (2020) Adaptive inspirational design stimuli. https://codesign.berkeley.edu/pdfs/papers/kgl-adaptive-stimuli-jmd.pdf (b07 to b09)
- [M] Examining the boundary between near and far design stimuli (Design Society proceedings, abstract page). https://www.cambridge.org/core/journals/proceedings-of-the-design-society/article/examining-the-boundary-between-near-and-far-design-stimuli/F3E58559BF57F93EAEF980B6993296F2 (d17; abstract only)
- [M] Forbus, Gentner, Law (1995) MAC/FAC. https://doi.org/10.21236/ada286291 (a24)
- [M] Thagard, Holyoak, Nelson, Gochfeld (1990) ARCS. https://doi.org/10.1016/0004-3702(90)90018-u (a25)

**Machine retrieval and analogy mining**
- [V] Hope, Chan, Kittur, Shahaf (2017) Accelerating innovation through analogy mining. https://arxiv.org/abs/1706.05585 (b11 to b13)
- [V] Hope et al. (2022) Scaling creative inspiration with fine-grained functional aspects. https://arxiv.org/abs/2102.09761 (b14)
- [V] Kang et al. (2022) Augmenting scientific creativity with retrieval across knowledge domains. https://arxiv.org/abs/2206.01328 (b15)
- [V] Sultan and Shahaf (2022) Life is a circus. https://arxiv.org/abs/2210.12197 (b16)
- [V] Emuna et al. (2023) BARCODE. https://arxiv.org/abs/2312.12681 (c07 to c10)
- [V] Majumder, Bhattacharya, Chakrabarti (2024) RAG tool for SAPPhIRE models. https://arxiv.org/abs/2406.19493 (c11, c12)
- [V] Kulikowski (2026) Same problem, different field. https://arxiv.org/abs/2609.07595 (c28)
- [V] Jung et al. (2026) Cross-Pollination Retrieval. https://arxiv.org/abs/2610.25678 (c29, d08)
- [V] Sharon and Hope (2026) RATIO. https://arxiv.org/abs/2608.27394 (d09)
- [V] Kargupta et al. (2026) Idea-Catalyst. https://arxiv.org/abs/2603.12226 (c20 to c22)

**LLM studies**
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2212.09196 (b19, b20)
- [V] Lewis and Mitchell (2024) Counterfactual tasks. https://arxiv.org/abs/2402.08955 (b21)
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks. https://arxiv.org/abs/2404.13070 (b22)
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 (b23, b24, c16 to c18, d06)
- [V] Qin et al. (2024) Relevant or Random. https://arxiv.org/abs/2404.12728 (d01)
- [V] Gwak et al. (2026) Not the example, but the process. https://arxiv.org/abs/2602.15863 (d07)
- [V] Bhavya, Xiong, Zhai (2022) Analogy generation by prompting InstructGPT. https://arxiv.org/abs/2210.04186 (b25)
- [V] Ding, Chan, Kittur et al. (2023) Fluid transformers and creative analogies. https://arxiv.org/abs/2302.12832 (b26)
- [V] Ma, Grandi, McComb, Goucher-Lambert (2023) Conceptual design generation using LLMs. https://arxiv.org/abs/2306.01779 (b27, c19)
- [V] Wijesiriwardene et al. (2023) ANALOGICAL benchmark. https://arxiv.org/abs/2305.05050 (b28)
- [V] Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/abs/2310.12874 (b17, b18)
- [V] Ye et al. (2024) AnaloBench. https://arxiv.org/abs/2402.12370 and https://arxiv.org/html/2402.12370v2 (c30, c31, d03 to d05)
- [V] Puranam, Sen, Workiewicz (2025) Can LLMs help improve analogical reasoning for strategic decisions. https://arxiv.org/abs/2505.00603 (c13 to c15)
- [V] Zhu, Zhang, Luo (2022) Biologically inspired design concept generation using GPT. https://arxiv.org/abs/2212.13196 and preprint https://arxiv.org/abs/2204.09714 (c01 to c06, d13)
- [V] Luu and Buehler (2023) BioinspiredLLM. https://arxiv.org/abs/2309.08788 (c33)
- [M] Buehler (2023) Diatom-inspired architected materials. https://arxiv.org/abs/2301.05875 (c34)
- [V] Jiang et al. (2024) AutoTRIZ. https://arxiv.org/abs/2403.13002 (c25)
- [V] Chen et al. (2024) TRIZ-GPT. https://arxiv.org/abs/2408.05897 (c26, c27)
- [V] Li et al. (2025) Past meets present: historical analogy. https://arxiv.org/abs/2409.14820 (c32)
- [V] Chen, Wang, Wang (2026) ARCANA. https://arxiv.org/abs/2610.29271 (c23, c24)
- [V] Chen et al. (2026) Analogical Deep Research. https://arxiv.org/abs/2607.13602 (d10)
- [V] Shen et al. (2026) On the diversity of analogy making in LLMs. https://arxiv.org/abs/2608.03233 (d11)
- [V] Shen, Druckmann, Zou (2026) Unlocking LLM creativity in science through analogical reasoning. https://arxiv.org/abs/2605.11258 (d12)
- [V] Kang et al. (2025) BioSpark. https://arxiv.org/abs/2503.09838 (d14)
- [V] Chen et al. (2025) Understanding design fixation in generative AI. https://arxiv.org/abs/2502.05870 (d15)

Links to parallel subfields (not covered here): structure mapping, case representation, case-based reasoning in law, conceptual blending, framing and reframing, sampling and voting, heuristic search.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 17 established claims: 4 confirmed as written, 13 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E07.07-K01** (now single-source: the sources are not independent). Numbers check out (Helms 2008: 4/9 and 5/10 solution-driven projects; Goel & Hancock 2021: 27/74 = 36.5%), but all three sources (Helms et al., Goel & Hancock, Vattam & Goel) come from Goel's Georgia Tech lab, so there is one research group behind the evidence.
- **E07.07-K02** (reworded: the sources support less). The bullet-to-'prevent, withstand and heal damage' example is in Helms et al. 2008, but it is a described process step in a class, not evidence that reframing is the step that opens retrieval; Hope et al. 2017 supports only that purpose/mechanism abstraction improves machine retrieval of product analogies. Corrected claim: Reframing the problem in abstract, biology-ready function terms is the second step of the problem-driven bio-inspired design process taught in the Georgia Tech course ('stopping a bullet' became 'prevent, withstand and heal damage'), and separate work on product descriptions finds that purpose/mechanism abstraction improves analogy retrieval; no study isolates reframing as the step that opens retrieval for human designers.
- **E07.07-K03** (now single-source: the sources are not independent). Counts verified in Goel & Hancock Table 8 (22/27 = 81.5% vs 14/47 = 29.8%, Fisher p<0.001, using the authors' reclassification; the earlier classification in Table 7 gave 9/10 vs 27/64), but the corroborating Helms 2008 source is the same lab and only a small class sample (100% vs 60%).
- **E07.07-K05** (now single-source: the sources are not independent). Vattam & Goel 2013 gives 6/9 (Fall 2006) and 4/10 (Fall 2007, not 2008) compound solutions, and Goel & Hancock say compound analogy is rare with solution-based design, but all sources are from the same lab, and the 'in 2008' label is the paper year, not the cohort year.
- **E07.07-K06** (number corrected). In Dekel et al. Exp 1, 61.9% (13/21) is the surface-schema (and first-order-schema) condition retrieving its matched story and 11.6% is the retrieval rate of that story in other conditions; the higher-order condition retrieved its story 40.9% (9/22) vs 11.9% elsewhere; Exp 2's 37.3% vs 10.8% is the modified higher-order cue condition after a comparison, not unaided retrieval. Puranam et al. is not about retrieval. Corrected claim: After comparing two stories, people retrieved a surface-matched story 61.9% of the time (vs 11.6% in other conditions) but a higher-order (structural) match only 40.9% (vs 11.9%) in Exp 1; in Exp 2 the higher-order condition reached 37.3% vs 10.8% elsewhere (Dekel, Burns and Goldwater, preprint). Without a schema-inducing comparison, retrieval of structural analogues is rare (about 11 to 12%).
- **E07.07-K12** (reworded: the sources support less). Kulikowski's numbers are right (skeleton AP 0.222 to 0.513 vs abstract with TF-IDF, 18 method families) and BARCODE's 72% vs 36% at top 7 is right (strategy sentences, entire data), but BARCODE compares its whole system against a different baseline system, so it does not isolate a domain-stripped or function-focused representation. Corrected claim: Domain-stripped representations improve cross-domain retrieval in one 18-family benchmark (skeleton fingerprint raised average precision from 0.222 to 0.513 over TF-IDF on abstracts); BARCODE, which retrieves challenge/strategy sentences, got 72% vs 36% strategy precision at top 7 against a different baseline system, which supports sentence-level strategy extraction but is not an ablation of representation.
- **E07.07-K15** (reworded: the sources support less). AnaloBench T2 (about random) and StoryAnalogy figures (ChatGPT ~30%, text-davinci-003 37.1%, human 85.7%, chance 25%) check out, but 37.1% is not 'near chance', and the clause that LLMs do better when mapping a given pair is not supported by AnaloBench/StoryAnalogy (Puranam et al. only shows GPT-4 solving strategy problems with a hint). Corrected claim: LLMs are close to random at retrieving analogues from a large story bank (AnaloBench T2, 200+ stories) and weak at StoryAnalogy multiple choice (ChatGPT about 30% and text-davinci-003 37.1% vs human 85.7%, where chance is 25%).
- **E07.07-K20** (reworded: the sources support less). Ding et al. figures verified (median helpfulness 4/5, observable reformulation changes in 80%, upper bound 25% potentially harmful), but Ma et al. found LLM concepts more feasible/useful and less novel than crowd concepts, with a 'diverse' prompt word helping in one prompt and hurting in another, so 'less diverse unless prompted' is not what the source shows. Corrected claim: LLM analogies as inspiration helped designers on a problem reformulation task (median helpfulness 4/5; observable changes to problem formulations in 80% of cases), with up to 25% of outputs rated potentially harmful (mostly upsetting rather than biased); in a separate study LLM-generated design concepts were rated more feasible and useful but less novel than crowdsourced ones, and prompt wording changed their similarity to the crowd set unpredictably.
- **E07.07-K21** (reworded: the sources support less). The filter-pass rates and bird share come only from Zhu et al.'s single flying-car case with fine-tuned GPT-3 (Table 5 lists 50% to 84%, not 58-84%; birds >50% of analogues is stated), while BioinspiredLLM (materials Q&A) and the SAPPhIRE RAG tool report nothing on filters, birds or weak structure-level evaluation. Corrected claim: In one flying-car case study with fine-tuned GPT-3 (Zhu et al.), generated bio-inspired concepts passed the automatic relevancy classifiers at roughly 50 to 84% depending on generator and check, and birds made up over 50% of the retrieved analogues; BioinspiredLLM (materials questions) and a RAG tool for SAPPhIRE models show that fine-tuned or retrieval-grounded LLMs can produce usable bio-inspired content, but they were not evaluated at the structure level.
- **E07.07-K22** (reworded: the sources support less). Numbers verified (BARCODE: 40-100 h to hand-describe one organism in the SBF framework, and 3.36% of 3,416 PubMed articles gave design insight, citing Kaiser et al. 2012; Vattam & Goel: about 3 person-hours per relevant article, a rough estimate from one 6-person team), but 40-100 h is the cost of curating a structured database entry, not of looking up biology, and Helms & Goel 2013 contains none of these figures. Corrected claim: Finding and encoding biology is expensive for humans: hand-describing one organism in a structured framework takes 40 to 100 hours (BARCODE paper), only 3.36% of 3,416 heuristically filtered PubMed articles gave design insight (Kaiser et al. 2012, as cited), and one design team spent roughly 3 person-hours of search per relevant article (rough estimate, Vattam and Goel 2013), so automated retrieval has headroom.
- **E07.07-K24** (reworded: the sources support less). TRIZ-GPT numbers verified (recall 0.675 to 0.245 with few-shot, precision 0.259 to 0.333), but AutoTRIZ's 7/10 means 'complete or half match to the textbook's contradiction analysis within the top 3 detections', not 7 of 10 cases fully matched. Corrected claim: TRIZ-style LLM pipelines are only moderately accurate: AutoTRIZ's contradiction detections matched or half-matched the textbook analysis within the top 3 detections in 7 of 10 textbook cases, and TRIZ-GPT few-shot prompting lowered recall (0.675 to 0.245) while raising precision (0.259 to 0.333).
- **E07.07-K25** (reworded: the sources support less). ARCANA figures verified (best model GPT 5.2 51.20% / 48.33% by typo scoring vs human average 68.96% / 58.35%, wide spread: Claude Opus 4.5 8.61%), but ARCANA is whole-benchmark, not 'hard tasks', and neither source compares mapping a given analogy with finding one (ANALOGICAL tests identifying analogous pairs via embeddings and finds harder analogy levels harder). Corrected claim: On the ARCANA far-analogy mapping benchmark the best model (GPT 5.2) scores about 48-51% against human averages of 58-69%, with a large spread between models (Claude Opus 4.5 about 7-9%); this shows far analogical mapping is still unsolved, not that mapping is easier than finding an analogy.
- **E07.07-K31** (reworded: the sources support less). BioSpark numbers all verified (novelty 3.9 to 7.1, feasibility 6.8 to 5.7, value 3.8 to 7.0, species 4.6 to 8.2, ideas 5.5 to 10.3, 12 participants), but a feasibility drop alongside much higher value in one small study is not a demonstrated novelty-feasibility cost, and Chan et al. 2011 reports far-field examples raised novelty and quality variability, not lower feasibility. Corrected claim: In one small within-subject study of an LLM-supported bio-inspired design tool (BioSpark, 12 participants, blind expert ratings), novelty rose 3.9 to 7.1 and value 3.8 to 7.0 while feasibility fell 6.8 to 5.7; unique species rose 4.6 to 8.2 and ideas 5.5 to 10.3. Feasibility dipped as novelty rose, but value also rose strongly.
- **E07.07-K27** (now single-source: only one opened source, code check).
