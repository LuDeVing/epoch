# Category learning: rule, prototype, exemplar: deep document

*Subfield A11.07. Written from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Status marks: [E] established, [S] single-source, [C] contested. [V] means the page or PDF text was opened; [M] means snippet, abstract or second-hand only. Founding-study numbers (Shepard 1961, Medin and Schaffer 1978, Rouder and Ratcliff, Goodman 2008, Smith and Minda 2000, Nosofsky 2000) were NOT read in full. Treat them as qualitative.*

## 1. What it is

Category learning asks how a learner builds a class from examples and then sorts new items into it. Three families of answer compete.

- **Rule.** The class is a logical statement over features ("size is large AND colour is red"). Items are in or out. Learning is search for the right statement, plus memorised exceptions.
- **Prototype.** The class is a central tendency: an average or best-example item. A new item goes to the class whose centre is nearest. Gives graded typicality.
- **Exemplar.** The class is the set of stored instances. A new item goes to the class with the larger summed similarity to all stored items.

A fourth family, decision bounds, cuts the feature space with a boundary (a07). Hybrids exist: RULEX (rules plus stored exceptions), ATRIUM (a rule module plus an exemplar module), COVIS (explicit rule system plus procedural learner) (a24).

Why it matters for our agent. The agent meets problem classes, not stimuli. At S0 it must label a problem by structure (one-feature rule, XOR, rule plus exception, family resemblance, arbitrary). It must also store what it learns about a class in memory. The open design question is the same as in the human literature: store a distilled summary (prototype or rule) or stored cases (exemplars), and when to prefer which. The human literature says neither wins everywhere. The newer agent-memory literature says distilled beats raw at small case counts.

Evidence quality warning. The human half of this document leans on one 30-year debate whose key numbers we could not open. The LLM half leans on small open models, one old model (Claude-v2), and a few agent-memory papers. No study tests a current frontier model on the six Shepard types. That is the largest gap.

## 2. History and theories in depth

**Rules first (to 1970s).** Early work assumed concepts are sets of logical rules (Bruner et al. 1956; if-then production systems) (a07, a17). Shepard, Hovland and Jenkins (1961) built the standard test bed: eight stimuli on three binary dimensions (size, colour, form), four per category, giving six structures (a01 [M]). Type I: one diagnostic dimension. Type II: XOR on two dimensions. Types III and V: a rule plus exceptions. Type IV: family resemblance. Type VI: arbitrary, memorise each item. The classic adult order is I < II < III,IV,V < VI. The authors concluded people abstract dimensions and test rules.

**Prototype and exemplar (1960s to 1980s).** Posner and Keele (1968) showed an unseen prototype can be classified well after training on distortions. Medin and Schaffer (1978) introduced the context (exemplar) model and the "5-4" structure: nine training items (five A, four B) on four binary dimensions, then 16 transfer items without feedback, with an interpolated task between (a03, a27 [M, via Lian 2024]). Their key contrast: a training item far from the prototype (stimulus 7) can be classified better than a transfer item closer to it (stimulus 4). Prototype models fail this. Nosofsky (1986) generalised this into the GCM, where choice probability rises with summed similarity to all stored exemplars. Kruschke (1992) added learned dimension attention (ALCOVE) (b26 [M]).

**Rules return, with hybrids (1990s).** Nosofsky, Palmeri and McKinley (1994) proposed RULEX: people form simple logical rules and memorise exceptions. Learning is stochastic, so averaged data blend idiosyncratic rules (b19 [abstract]). Rule models were also formalised for response times (Fific, Little and Nosofsky 2010; a06).

**The 5-4 meta-analysis fight (1998-2006).** Smith and Minda (1998) found early blocks fit a prototype model and later blocks an exemplar model (14 six-dimension stimuli, blocks of 56 trials) (b06). Smith and Minda (2000) reanalysed 30 uses of the 5-4 structure across 8 articles over 20 years. They argued 5-4 encourages memorising because it is small and poorly structured, and that exemplar models win only by reproducing training-item effects (b04). Nosofsky (2000) rebutted: many of the 30 sets did not test the real 5-4 structure, and the all-or-none exemplar processes in Smith and Minda's elaborated prototype models are implausible (b05). Nosofsky and Zaki (2002) said Smith and Minda confused the type of representation with the type of response rule (probabilistic vs deterministic); an exemplar model with response scaling fits (b03). Vanpaemel and Pattyn (2006) reanalysed (d07 [M]). Only abstracts and summaries were opened. Status: contested.

**Model-comparison turn (2004-2008).** Rouder and Ratcliff (2004): four experiments with one-dimensional stimuli and probabilistic category assignment, pitting a rule model (general recognition theory) against the GCM. Rules fit better with confusable stimuli, exemplars with few, distinct stimuli (b01, d05; abstract only). Their 2006 review says the data support neither alone and proposes a dynamic account: start with rules, learn discriminating features, then shift to exemplars with experience (b02, a18). Lee and Vanpaemel (2008) fit a hierarchical Bayesian Varying Abstraction Model to 30 published Nosofsky-lab data sets. Representations ran from pure exemplar to pure prototype, some data sets had split posteriors, and abstraction fell across blocks toward exemplar (b17, b18). Goodman, Tenenbaum, Feldman and Griffiths (2008): Rational Rules, Bayesian inference over a grammar of logical rules with a prior for short rules. It matched human generalisation for averages and individuals with few free parameters (b20, a20; no fit numbers read).

**Systems debate (2000s-2017).** COVIS and related work claim separate explicit-rule and procedural systems, based on at least 25 reported dissociations (feedback delay, working-memory load) between rule-based (RB) and information-integration (II) tasks (a09, b22). Ashby and Rosedahl (2017) showed a striatal neural model is mathematically equivalent to the GCM under five assumptions (R^2 .981 to .999 across four structures), so fit alone cannot separate the accounts (b22). Status: contested.

**Complexity line.** Feldman (2000): human ease of learning Boolean concepts falls with the length of the shortest logical formula (c24 [M]). Pape, Kurtz and Sayama (2015): that measure predicts only the classic Shepard order. A Shannon-entropy measure fits both orders (d01-d03).

**Individual-difference line.** Working-memory capacity predicts learning of all six Shepard types (Lewandowsky 2011, N=113; b14). Working memory predicts rule-task success and episodic memory predicts exemplar-task success (Hoffmann et al. 2014, N=279; b15). Older adults show deficits in category learning (Badham et al. 2017; b16).

**Machine-learning turn (2021-2026).** The same tests were applied to networks and LLMs: Dasgupta et al. 2022 (c08), Chan et al. 2022 (c06, c07), Jagadish et al. 2024 (a10-a14), Russin et al. 2025 (a15, a16, c19), Xiong et al. 2026 (b10, b11), Fu et al. 2026 (c12-c14), plus agent-memory work that is category learning only by analogy (c22, c23, d13-d15). See section 6.

## 3. Core findings with exact numbers

"Status" follows claims.jsonl. Rows from one paper are marked.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| No single model family wins; strategy depends on stimuli, stage, instruction | 30 data sets fit with a model spanning exemplar to prototype; some posteriors split between extremes (mass 0.36/0.20/0.12/0.10 and 0.39/0.36/0.13 for sets 11 and 15) | Lee and Vanpaemel 2008 (b17); Rouder and Ratcliff 2004/2006 (b01, b02) | [E] (K01) |
| Shepard difficulty order, adults, separable stimuli | I < II < III,IV,V < VI | Shepard et al. 1961 (a01, M); Nosofsky et al. 1994 per Jagadish (b24, M) | [E] (K18) |
| A second order holds for integral stimuli, children, monkeys | I < IV < III < V < II < VI | Pape et al. 2015 (d01) | [E] |
| Entropy complexity fits both orders; Boolean complexity fits only classic | R^2 .829 (classic data), .970 (general data) | Pape et al. 2015 (d02) | [S] |
| Boolean complexity rank fit drops on larger structures | about .79 on 4[4]; .986 on 4[3] (column heads lost) | Pape et al. 2015 (d03) | [S] |
| Rule model wins with confusable stimuli, exemplar with few distinct ones | 4 experiments; no fit numbers read | Rouder and Ratcliff 2004 (b01, d05) | [E] qualitative |
| Early prototype-like, later exemplar-like in humans | 14 six-dim stimuli, blocks of 56; prototype fits first five blocks | Smith and Minda 1998 via Jagadish (b06, a12) | [C] (K02) |
| 5-4 meta-analysis disputed | 29-30 data sets; counts per model not obtained | Smith and Minda 2000 (b04, d06); Nosofsky 2000 (b05, d07) | [C] |
| Meta-learned ERMI beats raw Claude-v2 as a participant | BIC 38722.13 vs 39816.90 (Badham data); 41207.20 vs 42401.42 (Devraj); MSE to human curves 0.05 vs 0.18 | Jagadish et al. 2024 (a10, a11, c01, c02) | [S] one paper (K03) |
| Classic models lose to ERMI | Posterior model freq: ERMI 0.43+-0.05, RMC 0.41+-0.05, MI 0.10, PFN 0.05; GCM, prototype, Rule, Rulex each at most 0.01 | Jagadish et al. 2024 (a10) | [S] |
| ERMI shows prototype-to-exemplar drift, plain MI does not | slope -0.01+-0.004, z=-2.54, p<0.01 vs -0.002+-0.005, z=-0.47, p=0.63 | Jagadish et al. 2024 (b09) | [S] |
| Claude-v2 prompted: exemplar-based from block 2; Type 2 harder than 3-5 | zero error on most levels in about 3 blocks | Jagadish et al. 2024 (a11, b08) | [S] (K04) |
| Cobweb fits Shepard curves | r basic: I .981, II .929, IV .910 (leaf), V .984, III .751, VI -.375 (leaf .884); RMSD .075-.231 | Lian et al. 2024 (a05) | [S] (K05) |
| Cobweb fits Medin-Schaffer | r .768 leaf, .713 basic; RMSD .166 and .130 | Lian et al. 2024 (a04) | [S] |
| Working memory predicts all Shepard types | N=113; one latent variable | Lewandowsky 2011 (b14) | [S] effect sizes unread |
| Working memory predicts rule tasks, episodic memory exemplar tasks | N=279 | Hoffmann et al. 2014 (b15) | [S] effect sizes unread |
| Neural model equals GCM | R^2 .999, .999, .981, .990 | Ashby and Rosedahl 2017 (b22) | [C] |
| Rule-based RTs favour serial self-terminating logical-rule models | 5 subjects; best BIC for 4 subjects (serial), 1 (parallel); EBRW poor | Fific et al. 2010 (a06) | [S] design favoured rules (a26) |
| Pretrained LM size changes style | 1B near exact exemplar; 7B, 70B more rule-based | Chan et al. 2022 (c07) | [E] (K06) |
| Transformers from scratch: rule in weights, exemplar in context | BX label chosen as AX or BW about equally | Chan et al. 2022 (c06) | [E] |
| Blocked helps rule-like ICL; rotated categories fail | Llama 2 blocked 601/640 = 93.9%, interleaved 478/576 = 83.0%; rotated 23.6% and 24.5%; GPT-3.5 order effect p=0.63; human interaction p=0.04, d=0.47 (blocking), d=0.33 (interleaving) | Russin et al. 2025 (c19, b13) | [S] (K07) |
| Rules beat examples in instruct models | instruct minus base: +0.178 rules, -0.024 examples; largest gain +0.3 to +0.4 on Operator Function and Set Game; examples added to rules: no significant gain | Fu et al. 2026 (c12, c13) | [E] (K08); size gaps approximate |
| Stated rule helps only if correct | GPT-4-turbo linear functions 30% to 96% with the true rule; self-stated rule accuracy vs ICL success r=0.0013 (GPT-3.5); Kalamang features 27.78% (GPT-3.5), 22.22% (GPT-4-turbo), 0% (Llama-2-7B) | Liu et al. 2024 (d09, d10) | [E] (K20) |
| Rule induction loop with a code interpreter beats plain IO | ACRE raw 64.0 to 79.8; MiniSCAN 61.7 to 77.0; MiniSCAN task accuracy 0.0 to 46.0; MiniARC raw fell 33.1 to 12.8 | Qiu et al. 2024 (c16) | [S] |
| LLM cannot reliably apply its own rule | MiniSCAN over 80% (symbolic interpreter) to about 0% (LM interpreter) | Qiu et al. 2024 (c17) | [S] |
| LLM brittle to noisy examples | 12.5%, 25%, 50% perturbed; human baselines ACRE about 80%, List Functions 45.9% | Qiu et al. 2024 (c18) | [S] |
| ICL accuracy falls with Boolean complexity | Gemma-2-9B 83% to 66%, Qwen2-72B 90% to 74% over classes 1-5; r -0.961 (p=.009), -0.898, -0.884, -0.854 (p=.065) | Wang et al. 2024 (c15) | [E] soft (K09) |
| LLM hypotheses plus Bayes match humans | Number Game R^2 .95 (100 samples); logical concepts R^2 .81, within 3% of human accuracy | Ellis 2023 (a21) | [E] (K10) |
| LLM final-layer in-context learning looks prototype-like | 8 LLMs (Llama3 3B/8B, Gemma3 1B-27B, Qwen3 4B, Qwen3.5 27B); prototype learner best match; flexible linear learners score higher task accuracy | Xiong et al. 2026 (b10, c11) | [S] (K11) |
| LLM representations support prototype and exemplar categorisation | prototype 90.64% (24 demos; FastText 77.86, sense vectors 85.13), 90.87% (48 demos, THINGSplus), 92.37% (THINGS); nearest-neighbour 87.46% and 88.63%; odd-one-out 52.41% vs human 67.67%; similarity rho .776 | Xu et al. 2025 (b12, c20) | [E] (K12) |
| Standard nets are exemplar-biased | LSTM EvR=0.54; partial-exposure accuracy 30.1% vs 84% zero-shot | Dasgupta et al. 2022 (c08) | [S] |
| LLM concept organisation weak at subordinate level | valid exemplars LLaMA-3.1-70B about 82%, Mistral-7B 52%, LLaVA-7B 44%; overlap with human exemplars about 24-29% | Pedrotti et al. 2025 (c21) | [S] |
| Distilled memory beats raw trajectories | ReasoningBank WebArena: none 40.5, raw (Synapse) 42.1, workflows (AWM) 44.1, distilled 48.8, with test-time scaling 51.8 | Ouyang et al. 2026 (d13) | [E] (K22) |
| More retrieved cases hurt | 1 experience 49.7, 4 experiences 44.4 (subset, figure text garbled) | d13 | [E] with caveat |
| Abstract workflows beat concrete examples | Mind2Web step success: AWM gpt-4 45.1 vs MindAct 36.2; gpt-3.5 AWM 34.6 vs Synapse 30.6 | Wang et al. 2024 (d14) | [E] |
| Curated summary beats full history | AIME 2024, Claude 3.5 Sonnet: full history 26.7 vs curated 50.0; GPT-4o 20.0 baseline, 6.7 full history, 40.0 DC-RS; Game of 24 GPT-4o 10% to 99% | Suzgun et al. 2025 (d15) | [E] |
| ExpeL insights vs retrieval | HotpotQA 36 vs 31; ALFWorld 50 vs 55; WebShop 37 vs 38 | Zhao et al. 2024 (c22) | [E] mixed |
| ERL heuristics beat few-shot trajectories | 56.1% (+7.8 over ReAct about 48.3); few-shot trajectories about 46.4, below baseline | Allard et al. 2026 (c23) | [S] |
| Many-shot ICL tracks k-NN | linear classification up to 2048 shots per class tracks k=5 NN; slight drop beyond 512 in higher dimensions | Agarwal et al. 2024 (d16) | [S] (K23) |
| CNNs show a weak prototype effect | errors to criterion: human 37.5, AlexNet 34.72, DenseNet-121 9.59, ResNet-18 6.52 | Van Maldegem et al. 2025 (c09) | [S] abstract |
| Function vectors for rule and example prompts differ | instruction FVs lift zero-shot from under 20% to over 50% in best models; fail to match demo FVs in 10-shot | Davidson et al. 2025 (d11) | [S] mechanism only |

## 4. Mechanisms and models

Each model below is written so it can be coded.

**4.1 Exemplar model (GCM).** Store every training item x_j with its label. For a probe x, similarity s(x, x_j) = exp(-c * d(x, x_j)), with distance d = (sum over dimensions w_k * |x_k - x_jk|^r)^(1/r). Weights w_k sum to 1 (attention). Sensitivity c sets how sharply similarity falls. P(A | x) = (sum of s over stored A items) / (sum of s over all stored items), optionally raised to a response-scaling power gamma (Nosofsky and Zaki 2002 argue gamma matters, b03). ALCOVE learns the w_k by gradient descent on error (b26). Memory cost grows with items. Behaviour: strong on exceptions and small, irregular structures (the 5-4 pattern, Type VI).

**4.2 Prototype model.** Keep one centre per class: the mean feature vector (or modal value per dimension). P(A | x) from the ratio of exp(-c * d(x, centre_A)) over both centres. Memory cost is constant. Behaviour: strong on family-resemblance structure (Type IV), fails on XOR (Type II) because the centres coincide, and on exception items. Multiple-prototype or clustering models (Anderson 1991; Love, Medin and Gureckis 2004) sit between (a17).

**4.3 Rule model, RULEX style.** Search over one-feature rules, then two-feature conjunctions, then add exceptions for items the rule misses. Learning is stochastic, so run N searches and expect different rules per run. Evidence for rule use: response times fit serial self-terminating per-dimension decisions (a06); the fit for four of five subjects beat EBRW and parallel or coactive variants. Warning: that design gave explicit rules and separable dimensions on purpose (a26).

**4.4 Rational Rules (Goodman 2008).** Define a grammar of logical formulas over features. Prior probability falls with formula length (a simplicity prior). Likelihood: a formula labels each training item correctly, with a noise parameter. Posterior over formulas; generalisation to a probe is the posterior-weighted vote. Implementation recipe: sample formulas by MCMC. Fewer free parameters than RULEX (b20, a20). Numbers not read.

**4.5 Varying Abstraction Model (VAM).** Items are merged into clusters. All items in one cluster per class = prototype; each item alone = exemplar. Lee and Vanpaemel (2008) put a hierarchical Bayes prior over partitions and infer the partition from data (b17). Implementation: enumerate or sample partitions, score each by GCM-like likelihood, report posterior mass. Gives "how abstract" as a number.

**4.6 Cobweb (Lian et al.).** Incremental tree of concept nodes with category utility as the split criterion. Predict from the leaf level (exemplar-like) or a basic level (prototype-like). Leaf-level correlation to Medin-Schaffer humans .768; basic-level .713 (a04). Shepard fits are good except Type VI at basic level, where it fails (r -0.375), because grouping cannot help arbitrary labels (a05). Engineering reading: a tree with summaries at upper nodes and cases at leaves, queried top-down until confident.

**4.7 Hybrid systems.** RULEX (rules plus exceptions), ATRIUM (rule module plus exemplar module with a gate), COVIS (explicit verbal system plus procedural system) (a24). Engineering reading: a gate chooses between a fast pattern learner and a slow rule learner.

**4.8 Meta-learned learner (ERMI).** Generate about 10,000 category-learning tasks with an LLM (Claude-v2); the tasks match real datasets in noise, feature correlation and linearity (a25). Meta-train a transformer to predict labels trial by trial on those tasks. It fits human choices better than seven cognitive models and reaches state of the art on OpenML-CC18 (a10, c04). The extension to 15 experiments keeps the result (c05, a14). Caveat: the fitted learner is a small network, not the LLM.

**4.9 Complexity measures for S0.**
- Boolean complexity: length of the shortest formula that defines the concept (Feldman 2000). Wang et al. 2024 show LLM accuracy falls with it (c15).
- Entropy-based information complexity (Pape et al. 2015): fits both Shepard orders (d02).
Implementation: for a problem class with discrete features, enumerate Boolean formulas and take the shortest. For anything larger, treat the score as a soft prior only.

**4.10 Individual-level mixture.** Type II aggregates mix fast learners (two-dimension rule) and slow learners (one dimension fixed) (d04). Aggregated curves hide strategy mixtures. Engineering reading: log per-run strategy, not only the mean.

**4.11 In-context learning as a learner.** Fitting six online learners to LLM final-layer states, the prototype (class centroid) learner best predicted trial-by-trial behaviour across eight open models, though flexible linear learners reached higher accuracy from the same states (c11, b11). Learnability depended on whether the task axis lay along leading principal components (b11). Amplifying the task axis did not help. Transformers trained from scratch generalise by exemplar in context and by rule in weights (c06). Many-shot ICL tracks k-NN (d16).

## 5. What holds up

**Holds up (multiple sources or strong design).**
1. No single strategy wins. Stimulus confusability, stimulus count, stage of learning, instructions and individual differences all move the answer (b01, b02, b17, b19; K01).
2. The Shepard types give reliable, structure-dependent difficulty, but the order depends on the stimulus type (classic vs general) (d01).
3. Complexity of the minimal description predicts difficulty, in humans and in small LLMs (c15, d02). Soft prior only.
4. A stated rule helps an LLM only when it is correct and simple (d09). A wrong or unreliable self-stated rule does not (r=0.0013; Kalamang 22-28%) (d09, d10).
5. Rule gain is largest on algebraic or symbolic tasks and small on linguistic or knowledge-heavy tasks (c13).
6. Distilled memory beats raw stored cases at small case counts, in four independent agent-memory studies (d13, d14, d15, c23). Mixed in ExpeL (c22: ALFWorld retrieval 55 beats insights 50).
7. Model size changes the strategy: small pretrained LMs are exemplar-like, larger ones more rule-like (c07).
8. ICL fails on non-rule structures: rotated categories 23.6% and 24.5% for Llama 2 (c19). Examples do not rescue structures with no short description.

**Contested.**
- The prototype-to-exemplar shift in humans (b04, b05, b03; Nosofsky and Vanpaemel disputes). Lee and Vanpaemel's data agree only suggestively (b18).
- Whether rule-based and II learning need separate systems (b22 shows near-equivalence of a neural exemplar model and the GCM).
- What an "LLM style" is. Xiong et al. 2026 say prototype-like; Chan et al. 2022 say small LMs are exemplar-like and larger are rule-like; Russin et al. 2025 say rule-like when a rule exists; Jagadish et al. 2024 say Claude-v2 is fully exemplar-based from block 2. These differ by model, task and measure.
- Fu 2026 (rules beat examples) versus ExpeL (retrieval beats insights on ALFWorld, 55 vs 50) (c13, c22).

**Failures and null results.**
- GPT-3.5 shows no blocked/interleaved effect (p=0.63) where Llama 2 does (c19).
- Amplifying the task-aligned axis did not improve LLM behaviour (b11).
- MiniARC raw accuracy fell from 33.1 to 12.8 under rule induction with refinement (c16).
- Instruction function vectors did not match demonstration function vectors in 10-shot (d11).
- Combining rules and examples gave no consistent gain over rules alone (c12, d12).
- Retrieving 4 experiences scored below 1 (49.7 vs 44.4) (d13).
- An earlier claim that Smith et al. 2004 replicated the classic Shepard order was wrong: that study is the monkey (general-order) study per Pape 2015 (K18 correction).

**Moderators.** Stimulus type (separable vs integral); stimulus confusability and count; task stage; explicit rule instruction; working memory (N=113 and N=279, effect sizes unread); age (older adults); model size; instruction tuning (+0.178 rules, -0.024 examples); example order (Llama 2 only); number of cases (1 vs 4 retrieved, 512+ shots).

**Interventions that worked.** True-rule instruction (30% to 96%); propose-select-refine with an external symbolic interpreter (ACRE 64.0 to 79.8, MiniSCAN task accuracy 0.0 to 46.0); LLM-proposed hypotheses scored by Bayes (R^2 .81 to .95); distilled strategy memory (+8.3 over no memory on WebArena for one backbone); curated summary (26.7 to 50.0 on AIME); blocked order for rule-like tasks on Llama 2.

**Did not work.** Self-stated rules from the model itself on real grammars; using the LM itself as rule interpreter (MiniSCAN from over 80% to about 0%); appending full history (6.7 for GPT-4o on AIME); few-shot trajectories (below baseline in ERL); stuffing more retrieved experiences.

## 6. Language models

**What was tested.** The direct tests are few: Jagadish 2024 (Claude-v2 as participant), Chan 2022, Dasgupta 2022, Russin 2025, Wang 2024, Xiong 2026, Xu 2025, Fu 2026, Liu 2024, Qiu 2024, Ellis 2023, Pedrotti 2025. An arXiv sweep for "Shepard + language model" returned almost nothing else (b28). The agent-memory papers (ExpeL, ERL, ReasoningBank, AWM, Dynamic Cheatsheet) are about problem-class memory; their rule/exemplar reading is ours, not theirs.

**Behaviour.**
- *Claude-v2 as a participant* (a11, b08): reached zero error in about 3 blocks on most Shepard levels, found Type 2 harder than Types 3-5, was fully exemplar-based from block 2 on the Smith and Minda task, and fit worse than ERMI (BIC 39816.90 vs 38722.13; 42401.42 vs 41207.20; MSE 0.18 vs 0.05). Not clearly an anomaly: Type II hard is the general-order pattern (d01).
- *Size* (c07): 1B near exact exemplar; 7B and 70B more rule-based on shape/colour words with nonsense labels.
- *From scratch* (c06): in-context exemplar, in-weights rule.
- *Rule vs non-rule* (c19): Llama 2 learned a rule-like colour-animal task far better than a rotated one (93.9% vs 23.6% blocked; chi2=428.6 for rotation). GPT-3.5 showed the same split without an order effect.
- *Complexity* (c15): accuracy falls with Boolean complexity (83% to 66%, 90% to 74%).
- *Rules vs examples* (c12, c13): open models 7B-32B (Gemma 3, Qwen 2.5, Qwen 3, OLMo) plus GPT-5.4 as a reference. Rules beat examples. Instruction tuning gained +0.178 for rules and -0.024 for examples. Larger models gained more (+0.213 base vs +0.063 instruct, read from a garbled figure: approximate). AND beat OR for examples in Lexical Category Inference as in humans (c14), but the split did not show under rule prompts.
- *Representation level* (b10, b12, c20): in-context states support prototype (90.64% at 24 demos to 92.37%) and exemplar (87.46%-88.63%) categorisation, with prototype slightly ahead. Odd-one-out plateaus at 52.41% vs human 67.67%.
- *Many shots* (d16): with up to 2048 shots per class, Gemini 1.5 Pro tracks k=5 NN on linear classification. This is exemplar-style.
- *Noise* (c18): brittle to 12.5%, 25% and 50% perturbed examples.
- *Subordinate categories* (c21): alignment with Italian speakers is low at the subordinate level.

**What changed behaviour, and by how much.**
- True rule: 30% to 96% (GPT-4-turbo linear functions).
- External symbolic interpreter: MiniSCAN task accuracy 0.0 to 46.0; LM as interpreter: collapse.
- Instruction tuning: +0.178 on rules, no gain on examples.
- Scale: more rule-like.
- Blocked order: 93.9% vs 83.0% on Llama 2, null on GPT-3.5.
- Memory form: distilled 48.8 vs raw 42.1 vs none 40.5; curated 50.0 vs full history 26.7.
- Number of retrieved cases: 1 beats 4 (49.7 vs 44.4, subset).

**What is missing.** No test of a current frontier model on the six Shepard types; no blocked/interleaved test on one; no human-vs-LLM stage drift over a long session; no token-matched rule-vs-example comparison (Fu 2026 used minimum-coverage examples, not matched tokens); no problem-class retrieval test of prototype vs exemplar memory.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | The S0 gate labels a problem by structure (one-feature rule, conjunction, XOR-like, rule plus exception, family resemblance, arbitrary) and does not apply one strategy to all classes. | S0 | [E] | K01, b01, b02, b17, a07, a24 |
| A2 | Memory for a problem class is a distilled summary (rule, strategy, lesson) plus at most a few retrieved cases. More cases are not better. Consistent with SCHEMA lessons-by-class memory; keep retrieved cases to one or two. | M | [E] | K22, K13, d13, d14, d15, c23 |
| A3 | A rule the model states replaces examples only after a code-run held-out check passes. A wrong stated rule is worse than none. Aligns with G2 and G3. | G3/O | [E] | K20, d09, d10, c17 |
| A4 | Rule induction is done as propose, select, refine with a code interpreter that applies the rule. The model itself does not apply its own rule. | O/G5 | [E] as a method result on ACRE and MiniSCAN; gain on our bench untested (also T3) | c16, c17, a21 |
| A5 | A structural complexity score (length of minimal description, number of exceptions) is a soft input to the S0 difficulty estimate and budget split. Not a hard router. | S0/G12 | [E] soft | K09, c15, d02, d03 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Run the six Shepard types as permuted text tasks on our agent; compare with both human orders; use as an S0 calibration suite. | S0 | [S] | K04, K18, d01, a11 |
| T2 | State-the-rule-first step vs few-shot-only at equal tokens, by task type (rule-structured vs rotated or family-resemblance) and model size. | O/G | [E] for open 7B-32B models; untested on ours | K06, K08, c12, c13 |
| T3 | Propose-hypotheses-then-score vs direct answer on rule-induction items. | O | [E] on human match; [S] for accuracy | K10, a21, c16 |
| T4 | Hierarchical memory (class summary on top, cases below) vs flat; vary stored cases 5 to 500 to find a crossover. | M | [S] | K05, K22, K23, a05, d16 |
| T5 | Blocked vs interleaved order of few-shot examples by task type. | M | [S] | K07, c19 |
| T6 | Summarise early, store cases late (human drift), vs fixed strategy across a long session. | M | [C] | K02, b06, b09 |
| T7 | Prototype retrieval vs nearest-case retrieval for S0 problem classes. | M/S0 | [E] on representations, untested on problem classes | K12, b12, c20 |
| T8 | Does shrinking context push toward exemplar-like use (human working-memory effect) or does long context push toward k-NN (many-shot)? | G | [S] | K16, K23, b14, b15, d16 |
| T9 | Offer rule and example together at S0 vs rule alone. | O | [S], Fu says no gain | K21, c12, d12 |

## 8. Concrete tests on our bench

Rules for all: both arms at equal total tokens (setup counted, per G7); at least 3 seeds with permuted surface labels (the Smith et al. 2004 permutation trick, a02); report the per-seed distribution, not only a mean.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Six Shepard types as text (8 items, 3 binary features, labels permuted over 6 permutations per type, 24 blocks) | Plain model vs plain model with a "state a rule then check" step | Trials to criterion per type; Type II as distribution over runs; match to classic vs general order | Types I and VI at the extremes; Type II either hard (general) or intermediate (classic). A frontier model may reach zero error faster than humans (Claude-v2 took about 3 blocks). |
| B2 | Rule-structured vs rotated (45 degree) two-feature categories, 64 items, 32 train | Few-shot only; rule-first; rule-first plus examples | Held-out accuracy | Rule-first wins on rule-structured (gap near Fu's +0.3 to +0.4 on algebraic tasks); small or no gain on rotated (Llama 2 fell to about 24%). If it harms a class, G7 drops the step there. |
| B3 | Rule-induction items (ACRE-like, List Functions-like) | Direct answer; propose k hypotheses, score each by code on given examples plus a held-out check | Task accuracy | Positive, near the 64.0 to 79.8 raw gain; watch for a MiniARC-style loss (33.1 to 12.8). |
| B4 | Repeated problem classes from our bench, 20 per class | A: distilled class summary. B: top-1 retrieved case. C: summary plus 1 case. D: summary plus 4 cases. E: 5, 50, 500 stored cases | Pass rate on later items of the class | Summary at least equal to cases at small N; D below C (ReasoningBank pattern). Look for a crossover at large N (K23). |
| B5 | Rule-like and non-rule tasks | Blocked vs interleaved examples | Held-out accuracy | Blocked helps rule-like only if the model behaves like Llama 2; null for a GPT-3.5-like model. Run on our model first. |
| B6 | Boolean concept classes with complexity 1 to 5 (18 concepts each) | Plain; plain with complexity-based budget (more attempts at high complexity) | Accuracy per class; correlation of accuracy with complexity | r near -0.85 or stronger; budget by complexity beats uniform at equal tokens. |
| B7 | 50 held-out S0 labelling items (problem written, true structure known) | Model labels structure vs code feature extractor | Label accuracy; downstream pass rate when routing by label | Label accuracy above 80% for routing to be worth adding (our threshold, untested). |
| B8 | Long session of 100 class items | Fixed summary; fixed case store; summary early then cases | Pass rate by block | Tests the drift; no evidence for the direction on LLMs. |
| B9 | Same item, wrong stated rule injected | With and without held-out check | Accuracy | The check prevents the drop; Liu 2024 show self-stated rules do not track accuracy (r=0.0013). |

## 9. What does not transfer, and why

- **Stimulus-level findings.** The 5-4 structure, dot patterns, Type VI memorisation and response-time models act on perceptual stimuli. Our agent reasons over text. Response-time model fits (a06, K15) have no analogue.
- **Human working-memory and age effects.** Lewandowsky 2011, Hoffmann 2014 and Badham 2017 concern human capacity limits. An LLM's limit is context and attention, which need not behave the same way. The many-shot result goes the other way (d16).
- **Neural-implementation debate.** The striatal model and COVIS systems claims (b22, a09) do not change agent design (K14).
- **Layer-level mechanism.** Xiong 2026's final-layer prototype learner and function-vector work (b10, d11) need open-model internals. Our agent is a closed-model scaffold. Background only.
- **CNN prototype effects** (c09). Image networks, abstract only.
- **Small-model results.** Gemma, Qwen, Llama 2 and OLMo at 1B-70B: size changes strategy (c07), so numbers may not hold for a frontier model.
- **ERMI.** A small meta-trained network, not an LLM scaffold. The lesson used here is that ecological priors beat hard-coded strategy.
- **Agent-memory studies.** WebArena, Mind2Web, AIME and ALFWorld are multi-step tasks; the class-level reading is ours.
- **Distilled-beats-raw as a law.** Not uniform: ALFWorld retrieval beat insights (55 vs 50).

## 10. Open questions

1. Does a current frontier model reproduce either human Shepard order when tasks are run as text with permuted labels?
2. Does "state the rule, then test it" beat few-shot at equal tokens, and does it hurt on non-rule classes? Fu 2026 shows no clear harm but did not token-match.
3. What do Rouder and Ratcliff 2004/2006 and Goodman 2008 report numerically? Which designs favour rules vs exemplars?
4. How many of the 30 data sets favour each model in Smith and Minda 2000, and which did Nosofsky 2000 call invalid?
5. Do the prototype-then-exemplar drift and its switch point hold for LLM agents over a long session?
6. Where is the crossover between a distilled summary and stored cases as the case count grows (5 to 500)?
7. Does blocked ordering matter for a frontier model on rule tasks (Llama 2 yes, GPT-3.5 no)?
8. Does Boolean or entropy complexity predict agent failure well enough for S0 routing, beyond the small-model result (r near -0.9 on four models, one with p=0.065)?
9. What are the effect sizes for working memory and exemplar use (Lewandowsky 2011, Hoffmann 2014)? Does small context push an agent toward exemplar behaviour?
10. Is "LLM style" a single thing? Prototype (Xiong), exemplar (Chan small, Jagadish) and rule (Chan large, Russin, Fu) results conflict by model and task.
11. Would a meta-learned task bank (ERMI-style) give better S0 priors than hand-made classes?

## 11. Sources

Legend: [V] opened this session (page or PDF text); [M] snippet, abstract only or second-hand.

**Founding and human work**
- [M] Shepard, Hovland and Jenkins (1961) Learning and memorization of classifications. Described in Lian et al. 2024 (a01, b24). No URL.
- [M] Medin and Schaffer (1978) Context theory of classification learning (a03, b25). No URL.
- [M] Kruschke (1992) ALCOVE (b26). No URL.
- [M] Johansen and Palmeri (2002) Are there representational shifts during category learning? (b27). No URL.
- [M] Smith, Minda and Washburn (2004) Shepard replication; monkeys per Pape 2015 (a02, d01). No URL.
- [V] Smith and Minda (1998) Prototypes in the mist, read via Jagadish 2024 (b06). https://arxiv.org/pdf/2402.01821v2.pdf
- [M] Smith and Minda (2000) Thirty categorization results in search of a model (b04, d06). https://researchconnect.buffalo.edu/en/publications/thirty-categorization-results-in-search-of-a-model/
- [M] Nosofsky (2000) Exemplar representation without generalization? (b05). https://europepmc.org/search?query=Exemplar%20representation%20without%20generalization
- [M] Vanpaemel and Pattyn (2006) reanalysis (d07). https://lirias.kuleuven.be/bitstream/123456789/152268/1/vanpaemelps2006.pdf
- [M] Nosofsky and Zaki (2002) Exemplar and prototype models revisited (b03). https://europepmc.org/search?query=Exemplar%20and%20prototype%20models%20revisited
- [M] Nosofsky, Palmeri and McKinley (1994) Rule-plus-exception model (b19). https://europepmc.org/search?query=Rule-plus-exception%20model%20of%20classification%20learning
- [M] Rouder and Ratcliff (2004) Comparing categorization models (b01, d05, a19; abstract only). https://pmc.ncbi.nlm.nih.gov/articles/PMC1403834/
- [M] Rouder and Ratcliff (2006) Comparing exemplar- and rule-based theories (b02, a18). https://www.psychologicalscience.org/journals/current-directions/j.0963-7214.2006.00397.x/
- [M] Goodman, Tenenbaum, Feldman and Griffiths (2008) A rational analysis of rule-based concept learning (b20, a20, d08). https://pubmed.ncbi.nlm.nih.gov/21635333/
- [V] Lee and Vanpaemel (2008) Exemplars, prototypes, similarities and rules (b17, b18). https://sites.socsci.uci.edu/~mdlee/Lee_Vanpaemel_2007.PDF
- [V] Fific, Little and Nosofsky (2010) Logical-rule models of classification response times (a06, a07, a26, b21, d17). https://pmc.ncbi.nlm.nih.gov/articles/PMC2869285/ and https://faculty.gvsu.edu/fificm/assets/publications/2010FificLittleNosofsky.pdf
- [V] Ashby and Rosedahl (2017) A neural interpretation of exemplar theory (a08, a09, a24, b22). https://pmc.ncbi.nlm.nih.gov/articles/PMC5481458/
- [M] Feldman (2000) Minimization of Boolean complexity (c24). https://doi.org/10.1038/35036586
- [V] Pape, Kurtz and Sayama (2015) Complexity measures and concept learning (d01-d04). https://arxiv.org/abs/1406.7424
- [M] Lewandowsky (2011) Working memory capacity and categorization (b14). https://europepmc.org/search?query=Working%20memory%20capacity%20and%20categorization%20Lewandowsky
- [M] Hoffmann, von Helversen and Rieskamp (2014) Pillars of judgment (b15). https://researchportal.bath.ac.uk/en/publications/pillars-of-judgment-how-memory-abilities-affect-performance-in-ru/
- [M] Badham, Sanborn and Maylor (2017) Deficits in category learning in older adults (b16). https://europepmc.org/search?query=Deficits%20in%20category%20learning%20in%20older%20adults
- [V] Wikipedia: Concept learning (a17). https://en.wikipedia.org/wiki/Concept_learning
- [V] Tano et al. (2019) Towards a more flexible Language of Thought (a22). https://arxiv.org/abs/1805.06924

**Models and LLM or AI work**
- [V] Jagadish, Coda-Forno, Thalmann, Schulz and Binz (2024) Human-like category learning by injecting ecological priors from LLMs (a10-a13, a25, b07-b09, c01-c04). https://arxiv.org/abs/2402.01821
- [V] Jagadish et al. (2026) Meta-learning ecological priors from LLMs (a14, c05). https://arxiv.org/abs/2509.00116
- [V] Lian, Varma and MacLellan (2024) Cobweb (a04, a05, a27, b23). https://arxiv.org/abs/2403.03835
- [V] Russin, Pavlick and Frank (2025) In-context and in-weight learning in humans and neural networks (a15, a16, b13, c19). https://arxiv.org/abs/2402.08674
- [V] Chan et al. (2022) Transformers generalize differently from information stored in context vs in weights (c06, c07). https://arxiv.org/abs/2210.05675
- [V] Dasgupta, Grant and Griffiths (2022) Distinguishing rule- and exemplar-based generalization (c08). https://arxiv.org/abs/2110.04328
- [V] Xiong et al. (2026) LLMs reorganize representational geometry in context (b10, b11, c10, c11). https://arxiv.org/pdf/2605.28854
- [V] Xu et al. (2025) Revealing emergent human-like conceptual representations from LLMs (b12, c20). https://arxiv.org/pdf/2501.12547
- [V] Wang, McCoy and Steinert-Threlkeld (2024) Minimization of Boolean complexity in in-context concept learning (c15). https://arxiv.org/abs/2412.02823
- [V] Fu, Cho, Lee and Kim (2026) LLMs learn better in-context from rules than from examples (c12-c14, d12). https://arxiv.org/abs/2609.03213
- [V] Liu, Neubig and Andreas (2024) An incomplete loop (d09, d10). https://arxiv.org/abs/2404.03028
- [V] Davidson, Gureckis, Lake and Williams (2025) Do different prompting methods yield a common task representation (d11). https://arxiv.org/abs/2505.12075
- [V] Qiu et al. (2024) Phenomenal yet puzzling: testing inductive reasoning (c16-c18). https://arxiv.org/abs/2310.08559
- [V] Ellis (2023) Human-like few-shot learning via Bayesian reasoning over natural language (a21). https://arxiv.org/abs/2306.02797
- [V] Chari and Pattanaik (2026) Wild guesses and mild guesses in active concept learning (a23). https://arxiv.org/abs/2602.06818
- [V] Pedrotti et al. (2025) How humans and LLMs organize conceptual knowledge (c21). https://arxiv.org/abs/2505.21301
- [V] Agarwal et al. (2024) Many-shot in-context learning (d16). https://arxiv.org/abs/2404.11018
- [V] Zhao et al. (2024) ExpeL (c22). https://arxiv.org/abs/2308.10144
- [V] Allard et al. (2026) Experiential reflective learning (c23). https://arxiv.org/abs/2603.24639
- [V] Ouyang et al. (2026) ReasoningBank (d13). https://arxiv.org/abs/2509.25140
- [V] Wang, Mao, Fried and Neubig (2024) Agent Workflow Memory (d14). https://arxiv.org/abs/2409.07429
- [V] Suzgun et al. (2025) Dynamic Cheatsheet (d15). https://arxiv.org/abs/2504.07952
- [V] Van Maldegem et al. (2025) Replicating Posner and Keele (c09; conference abstract). https://2025.ccneuro.org/abstract_pdf/Maldegem_2025_Replicating_Posner__Keele_1968_Standard.pdf
- [M] Singh et al. (2021) CNN prototype effect (c27). No URL.
- [M] Davidson et al. 2026 and Liu 2024 as cited in Fu 2026 (c25, c26).
- [V] Gap note: arXiv keyword sweep for LLM Shepard tests (b28). https://export.arxiv.org/api/query?search_query=all:Shepard+AND+all:language+models
