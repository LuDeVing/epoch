# Boden's creativity types: deep document

*Subfield C04.01. Written from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Ids like a12 or K02 point to those files. Boden's and Wiggins's own texts were NOT opened (paywalled, 403/404), so the theory sections rest on later papers that quote and formalise them. Almost every LLM result below comes from one paper per result and none has been replicated by another group.*

## 1. What it is

Margaret Boden defines creativity as producing ideas or artefacts that are new, surprising and valuable. She splits it three ways by where the surprise comes from.

- **Combinational**: unfamiliar combinations of familiar ideas. Analogy, metaphor, collage, concept blending.
- **Exploratory**: finding new options inside an existing style or "conceptual space" by following its rules further than anyone has.
- **Transformational**: changing the rules of the space itself, so that ideas become possible that could not have been generated before.

She also separates **P-creativity** (new to the producer) from **H-creativity** (new in all history). Franceschelli and Musolesi (2024) add "B-novelty" (new to the beholder) and argue that LLM output often looks creative only in the B sense (a01, a02).

Wiggins (2006) made the exploratory/transformational split formal. A conceptual space is defined by rules R. A traversal strategy T says how to move through it. An evaluation E says what is good. Exploration is search in the space defined by (R, T, E). Transformation is search over spaces: change R or T (a04, a05).

Why it matters for our agent: it is a design vocabulary for S3 open mode. It asks which generator to use for a given open task: a combiner (analogy and blending), an explorer (search with a tree and a history), or a rule-changer (name the constraints, drop one, regenerate). It also tells us what scaffolds cannot do (section 9).

Scope note. The three types are labels, not validated mechanisms. No human-subject study tests them as separable categories (critique, weak spots). In the LLM papers below, "combinational", "exploratory" and "transformational" are names given to operators or benchmark subsets by the authors.

## 2. History and theories in depth

**Boden 1990, 1998, 2004 (The Creative Mind; Creativity and AI).** Founding statement. Not opened (b20, d19). Second-hand reading: the types are levels of surprise at rising levels of abstraction (a01). Her claim that transformational creativity is the deepest and rarest is conceptual. There is no experiment in the founding text.

**Wiggins 2006 (A preliminary framework for description, analysis and comparison of creative systems).** Not opened (b21, d19). Read through Espirito Santo, Wiggins and Cardoso (2024), who rebuild the framework as a formal learning theory (a04, a05, d15). Their Definition 17: an artefact a is transformative in situation s if the learned model M(sigma) differs from M(sigma + a). Theorem on novelty: novelty is neither necessary nor sufficient over sequences (d15). So an artefact can be new and not change the space, and the reverse.

**Ritchie 2007 (empirical criteria for attributing creativity to a computer program).** Not opened (b22). Known by title only. Treat as unverified.

**Lehman and Stanley 2011 (novelty search).** Not opened (b23). Its idea, reward novelty instead of the objective, is the root of the quality-diversity methods used below (Sodarace, c21).

**Schapiro, Black and Varshney (2025), a graph theory of transformational creativity in science.** Opened (a06, d16). Conceptual space is a directed acyclic graph of axioms and derived claims. Theorem 4: the node with the greatest transformative potential must be an axiom. Cases: Ptolemaic to heliocentric, Newtonian to relativistic physics, Euclidean to non-Euclidean geometry (altered parallel postulate). No empirical test. Consequence for us: banning one technique edits a leaf, not an axiom (K23, contested, our inference).

**Franceschelli and Musolesi (2024), On the Creativity of LLMs.** Opened (a01-a03, b18). Argument paper. Claim: current LLMs can reach combinational or exploratory creativity at most. Transformational is "not achievable through training" because of autoregressive fit to the data distribution and RLHF/DPO alignment that lowers diversity (cites Kirk et al. 2024). No experiment tests this. Scaffolds such as Universe of Thoughts partly contest it by simulating rule change in a prompt.

**Surveys and newer work.** Shahhosseini et al. (2026, TMLR) survey LLM scientific idea generation through the creativity lens (a08-a10). Colton, Cook, Hepworth and Pease (2014) is a position paper on observer issues: how the observer's view of process changes whether a system is judged creative (a23). Fanelli, Gangloff, Yu et al. and Boriceanu and Dinu (2026) were read for position only; no numbers (a24-a27).

**Timeline of LLM-era empirical work.** 2022 Lehman et al. use an LLM as mutation operator (c21). 2024 Chakrabarty et al. show LLM creative writing fails expert tests (b12); Si et al. run the large human study on research ideas (b17). 2025 OMEGA (reasoning generalisation by Boden type), Denial Prompting (rule change), AlphaEvolve, Artificial Hivemind. 2026 Universe of Thoughts (UoT), CreativeBench, KOMBINE, ML-engineering creativity study, AGC-Bench, long-tail evaluation, diversity training.

## 3. Core findings with exact numbers

Status: established = two or more independent sources agree; single = one paper; contested = sources disagree. Evidence ids repeat across files, so "independent" counts papers, not ids.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Boden-mode operators beat their own ablations only modestly | Full operator preferred over ablated version: C-UoT 58.3%, T-UoT 54.2%, E about 52% (chance 50%). 100 HypoArena tasks, position-debiased LLM pairwise judge | UoT (a14, b10, c07) | single (K01) |
| Best mode depends on task and backbone | Low-constraint, GPT-4o, human creativity: Bridge T-UoT 0.680 vs OnePrompt 0.480, CoT 0.590, ToT 0.580; Electricity T-UoT 0.620 vs OnePrompt 0.540. Hypothesis tasks, Qwen3-14B, Bradley-Terry rating / win rate: E-UoT 1535.4 / 32.7%, ToT 1515.8 / 25.5%, EGoT 1505.1 / 25.3%, C-UoT 1489.6 / 19.5%, T-UoT 1484.6 / 17.3%, OnePrompt 1475.7 / 14.3%. GLM-4-9B: OnePrompt first, 1560.4 / 46.3%; E-UoT 1542.1 / 40.7% | UoT (a12, a13, c05-c07) | single (K02) |
| Mode search costs far more tokens | Relative to one prompt (3.7k tokens): ToT 7.4x (27.1k), E-UoT 10.0x (36.7k), EGoT 27.6x (101.6k), C-UoT 36.5x (134.3k), T-UoT 52.5x (193.3k). The cheapest structured method won | UoT (c08) | single (K03) |
| Analogy fails at transfer, not retrieval | C-UoT picked a valid analogue 100%, mapped-mechanism specificity 0.97, strong transfer 52% on tasks it won vs 32% on tasks it lost. T-UoT gate passed 100%, transform applied 75% (wins) vs 83% (losses) | UoT (c09) | single (K04) |
| Scale helps combination, not exploration | Qwen2.5-7B: Combo pass@1 9.21%, creativity 0.168; Explore 4.11%, 0.0146. Gemini-2.5-Flash-Lite: Combo 36.41%, 0.509; Explore 23.51%, 0.1681. Evolutionary search / steering add little: Combo 0.168 to 0.193, GEPA 0.188; Explore 0.0146 to 0.0169-0.0182 | CreativeBench (a17-a19, b08, b09) | single (K05) |
| RL transfers within a skill, not to composed or transformed skills | Qwen2.5-7B GRPO on 1k problems. Zebra Logic base 30%, +61 ID, +53 OOD. Geometry base under 15%, +31 ID, +8 OOD. Matrix rank: ID +56%, transformative OOD fell 30 points from 70%. GCD level 3 from 6% to 10%, level 5 flat | OMEGA (a15, a16, b06, c02, c03) | single (K06) |
| More samples do not cure high complexity | pass@k (k to 32; 64 attempts) approaches 100% at low complexity, 0 at level 6; a DP solver needs 36 states. Computation share of tokens fell from about 65% (level 1) to under 40% (level 7); conjecture filled the gap. Models: DeepSeek-R1, Claude-3.7-Sonnet, o3-mini, o4-mini | OMEGA (b07, c01, c04) | single (K07) |
| AI research ideas rated more novel, less diverse | Novelty human 4.84 (SD 1.79, n=119 reviews) vs AI 5.64 (SD 1.76, n=109), p<0.01; AI + human rerank 5.81. Excitement 4.55 vs 5.19 (p=0.04). 49 ideas per condition, 79 reviewers. Of 4000 seeds per topic only 200 non-duplicate (cosine > 0.8). Reviewer agreement 56.1% vs 66.0% at NeurIPS 2021 | Si et al. (b17, c17, c18) | single (K08) |
| Aligned LLMs are homogeneous | Hivemind: average same-model response similarity above 0.8 in 79% of cases. Poems: top 1% of rhyme pairs cover 30.7% (Qwen3 30B-A3B) to 49.8% (Gemma 3 4B) of rhymes; top 1% of content words 46.3-61.5%. Model size vs distinct rhyme words r = 0.719-0.765 | Jiang; Matthews and Hamilton; Mohammadi (b15, c15, c16) | contested (K09) |
| The homogeneity effect is overstated by its null | Pairs expressing different ideas already exceed cosine 0.8 in 20% (LLM labels) to 32% (clusters). Original same-prompt pairs exceed it only 1.9-3.1x as often | Schaeffer et al. (b16) | single (K10) |
| Cheap diversity fixes work | Verbalized sampling: 1.6-2.1x creative-writing diversity; larger models gain 1.5-2x more. Random-prefix: LLM-rated diversity 0.68 vs 0.33, relevance 0.98 vs 0.99; 244 clusters from 250 ideas vs 35 on one topic. Weight steering: originality d = +0.36 (AUT, six models), up to +14 human percentile points on DAT, utility fell | Zhang; Luo; Schapiro (c19, b13, b14) | single per method (K11) |
| Diversity gain is capped by the answer space | Independent batches without memory plateau near batch 60. Collapse (near-duplicates of first 50 batches, cosine 0.85): naive 5.6 +/- 2.0%, any method with dedup 0.0% (200 batches, 2-3 seeds, two model families). Random-prefix saturates on finite answer sets | Lingo and Chhajer; Luo; Si (d11, b27, c18) | established (K12) |
| Agents explore new regions but it does not help | H-creativity (0-4): AIDE GPT-5 1.423 vs human gold 0.744, silver 0.524, bronze 0.293 (p<1e-15 vs gold); AIDE Qwen3-32B 0.838 (p=0.33). GPT-5 medal rate 21.25%. Change in impact vs change in P-creativity: human -0.111 (p<0.05), agents about 0. Greedy, MCTS, evolutionary all fell below P-creativity 1 within a few episodes | Bhushan et al. (b01, b03-b05) | single (K13) |
| Judging creativity is the weak link | 10 writers, 48 stories: New Yorker stories pass 84.7% (11.9 of 14 tests), LLM stories pass 3-10x fewer, no LLM-administered test correlated positively with experts. Newer judge: GPT-5 Spearman 0.732 with human P-creativity labels (alpha 0.724, N=300 episodes), GLM-5 0.703, DeepSeek V3.2 0.700, Qwen3-235B 0.685, GPT-OSS-120B 0.544. KOMBINE panel vs human: 75% unanimous (n=96), 66% majority. AGC-Judge: Spearman 0.80 vs LLM gold, 0.65 vs human gold (n=718, Williams t=-7.98) | Chakrabarty; Bhushan; KOMBINE; AGC-Bench (b12, b01, a20, d07) | contested (K14) |
| Stylistic bias of the judge is small in one probe | Register-only paraphrase: polish +0.40 (d=0.29), humanize +0.52 (d=0.15) on a 10-50 scale, 50 cells. Judge error not tied to plan length (partial r -0.032, p=0.585) or code length (-0.074, p=0.201). Conceptual paraphrase untested | AGC-Bench; Bhushan (d06, b02) | single (K15) |
| Combination: LLMs beat humans but converge | LLMs 10-16 points better than 75 humans at association and analogy. 19.9% (412 of 2,070) of invented concepts reuse a property another model invented; provider effect 2.3x. Blending-explanation step in text-to-image: Midjourney mean rank 1.98 vs 2.40 (50 raters, Friedman p<0.0001). VLM implication win rate: experts 78.3%, GPT-4o 73.5%, GPT-4V 71.9%, Gemini-1.5-Pro 71.7%, Claude-3.5-Sonnet 62.9%, average people 51.0%, LLaVA-1.5-7B 20.1% | KOMBINE; Peng et al. (a20, a21, c11, c12) | established (K18) |
| LLM as mutation operator plus evaluator finds new valid artefacts | Sodarace: map of 1,728 niches, nearly all seeds fill it; fine-tuning on accepted diffs raised niches reached. AlphaEvolve tensor decomposition: 54 targets, matched state of the art in 38, surpassed 14, behind in 2. Kissing number in dimension 11 raised to 593 | Lehman et al.; Novikov et al. (c21, c22) | established (K19) |
| Rule drop: correctness falls, divergence rises | Denial Prompting, 199 Codeforces problems, GPT-4 pass@1 after 0-5 forbidden techniques: 16.1, 11.6, 7.1, 5.2, 2.3, 2.1%. Constraint following 100% falling to 14.4%. Divergent creativity 4.5% to 15.3%. Claude-3 and Llama3-70B reach zero joint score within two states. Only MCTS of four reasoning strategies raised divergent creativity; gain 0 after step 2 | Lu et al. (c20, d08, d09) | single (K17, K21) |
| Cheapest validity check for a changed rule | Original tests still pass, plus a technique detector confirms the forbidden element is absent (GPT-4 detector 94% recall, pilot). For prose, humans license 18.7-22.8% of unsupported content (Whiteboard), so a goal check is needed | Lu et al.; Tang et al. (d09, d10) | single (K22) |
| Creativity wrappers can hurt quality in the novel region | q@Tail vs vanilla 0.474, average over 4 models: min-p +17.7% (0.558); convergent-divergent thinking -6.9% (0.442); persona -11.2%; branch-solve-merge -13.9%; self-consistency -19.0%; meta-prompting -32.5% | Wang et al. (d01) | single (K25) |
| One factor dominates | General creativity factor explains 81.5% of variance across 83 LLMs on 78 datasets (omega 0.96); holds after partialling out fluid reasoning (0.91); correlated with reasoning rho 0.55 | AGC-Bench (d05) | single (K26) |
| Set prompting trades quality for distance | Distance 0.24 to 0.80 (Claude Opus 4.8), win rate 0.33 to 0.21, CU 0.34 to 0.38. Training with a set-level reward: CU 0.64 vs 0.38 Opus, 0.52 DARLING (needs training). Human panel: promising ideas per portfolio 2.17 vs Opus 2.20 | Wadhwa et al. (d02-d04) | single (K27) |
| Judge-free diversity signal | Semantic entropy over clustered meanings: rho 0.56 with human preference, above cosine, Self-BLEU, Distinct-n; LLM novelty judge rho 0.80 on 30 pairs. Divergent score did not rise with model size while convergent did | Min Sen et al. (d13) | single (K29) |
| Explore-then-refine schedule | 40% exploration, 60% gap filling used; never compared with a constant mix. Self-rated obviousness filter: Spearman -0.065 with distance from centroid; of 852 ideas it would reject, 826 (96.9%) pass dedup, dedup caught 30 (3.0%) | Lingo and Chhajer (d11, d12) | single (K28) |
| No independent replication of UoT | arXiv and Semantic Scholar searches: zero citing items | d17 | single, negative search (K24) |

## 4. Mechanisms and models

Written so an engineer can build them. The model fills slots. Code does the control (schema section 1).

**4.1 The Wiggins loop (design vocabulary).** Make three explicit lists before generating: R (the rules and constraints of the space, as short statements), T (the traversal: how the next candidate is chosen, for example "pick an unused direction"), E (the evaluation: how a candidate is scored). Exploration = repeat T under fixed R and E. Transformation = edit R (or T), then explore again. This is a prompt structure plus a loop in code. Evidence that explicit lists beat unlabelled generation: none yet (K20).

**4.2 Combinational operator (C-UoT shape, c09).**
1. Code picks a source domain by retrieval (embedding nearest to a far domain), or the model lists candidate analogues.
2. Model selects one analogue (C-UoT did this correctly 100% of the time).
3. Model writes a typed mapping: source element, target element, mechanism carried over.
4. **Transfer check** (the missing step): a second call asks whether the mapped mechanism is specific and works in the target. Strong transfer was only 52% on wins and 32% on losses, so quality is lost here.
5. Optional blending explanation: list shared attributes before blending. In image mashups this gave mean rank 1.98 vs 2.40 (c12).
6. Code dedups against earlier outputs and earlier runs (19.9% of invented concepts repeat another model's property, a21).

**4.3 Exploratory operator (E-UoT / tree shape, c06, c08).** Tree search over the space: expand a node into a few children, score, keep the best, expand again. Code stores the history of directions tried and assigns untried ones. This was the best structured method on hypothesis tasks with Qwen3-14B at 10x the tokens of one prompt. A generate-test loop with an automatic evaluator (AlphaEvolve, Sodarace) is the strongest form (c21, c22). Without an evaluator the score comes from a judge, which is the weak link.

**4.4 Transformational operator (T-UoT shape and Denial Prompting).**
1. Model lists the constraints implied by the task and by the usual solution (R).
2. Gate: decide whether the space is low-constraint (T-UoT gate passed 100%).
3. Choose a constraint to drop or a technique to forbid. A leaf rule (ban a technique) is cheap. An axiom-level drop (an assumption many other things depend on, then re-derive) is the formal version and is untested (K23).
4. Regenerate under the new rule set.
5. **Validity check**, two parts: the original goal test still passes; a detector confirms the old element is gone. On code tasks this is unit tests plus a technique detector (94% recall pilot, d09). On prose there is no cheap test.
6. **Budget**: correctness roughly halves every one to two added rules (GPT-4: 16.1, 11.6, 7.1, 5.2%). Stop after 2-3 drops.

**4.5 Duplicate memory and stop rule (d11, d13).** Keep an embedding or meaning-cluster store of every idea. Reject any new idea above a similarity threshold. Stop when new non-duplicate yield per batch falls below a threshold or the cluster count is flat (near batch 60 without memory). Use meaning clusters, not raw cosine alone (K10): pairs of different ideas already reach cosine 0.8 in 20-32% of cases.

**4.6 Diversity prompting.** Verbalized sampling: ask for several responses with stated probabilities and sample from the low-probability ones (1.6-2.1x diversity, c19). Set prompting: ask for 3 ideas in one response (distance up, win rate down, d03). Both are prompt-only. Random-prefix decoding and weight steering need decoding or weight access and are not available to a scaffold.

**4.7 Tail-quality scoring (d01).** Score open mode on quality inside the most novel quarter of outputs, not on novelty alone. Report q@Tail.

## 5. What holds up

**Holds up (two or more sources):**
- LLMs produce homogeneous output after alignment. Direction agreed (Mohammadi, Kirk cited, Hivemind, poems). Size disputed.
- Diversity is capped by the real answer space (Luo, Si, Lingo and Chhajer). A duplicate memory removes collapse.
- LLM-plus-evaluator search yields valid new artefacts (Sodarace, AlphaEvolve). Needs an automatic check.
- LLMs are strong at combinational tasks yet converge on the same properties (KOMBINE, Peng).

**Single-source, unreplicated:** every mode ranking from UoT; the scaling asymmetry from CreativeBench; the within-skill generalisation pattern from OMEGA; the explore-versus-performance finding from Bhushan et al. No independent replication of any of these was found (d17).

**Failures and contradictions:**
- UoT mode ranking flips with the backbone: E-UoT best on Qwen3-14B, plain OnePrompt best on GLM-4-9B (46.3% win rate). AGC-Bench says one factor explains 81.5% of variance, so backbone likely dominates mode (K26).
- Hivemind versus Schaeffer: the effect is real but 2-3x smaller than first claimed (K10).
- Transformational: Franceschelli and Musolesi argue it is out of reach; T-UoT scored best on two low-constraint tasks. These are compatible because those tasks are low-constraint, with 10 PhD raters, so "transformational" there means a prompt-level rule change (critique).
- Judge reliability: near-zero LLM-expert correlation in 2024 (Chakrabarty), 0.732 in 2026 (Bhushan). Task, model generation and rubric differ. AGC-Judge agrees more with LLM gold than human gold, so an LLM judge may partly reward LLM taste.

**Moderators:** backbone (strongest), constraint level of the task, model size (larger models gain 1.5-2x more from verbalized sampling; scale raises convergent but not divergent scores), whether an automatic evaluator exists, and number of rules dropped.

**Interventions that worked:** verbalized sampling; random-prefix decoding (not scaffold-usable); persistent duplicate memory; min-p sampling for tail quality (+17.7%, needs sampler access); explanation-of-attributes step before blending; unit tests plus a detector for rule changes; LLM-plus-evaluator search.

**Interventions that did not work or hurt:** persona (-11.2% tail quality), branch-solve-merge (-13.9%), self-consistency (-19.0%), meta-prompting (-32.5%), convergent-divergent prompting (-6.9%); self-rated obviousness filter (weak, Spearman -0.065); evolutionary search and steering for exploratory benchmark items (0.0146 to 0.0182, negligible); RL for transformed skills (regressed 30 points); more samples at high complexity (pass@64 still 0); reasoning strategies other than MCTS in Denial Prompting (and the MCTS gain was 0 after step 2); creativity-training prompts in general (schema 4b).

## 6. Language models

**Combinational tasks.** Good and improving with scale. CreativeBench Combo creativity 0.168 (7B) to 0.509 (Flash-Lite). KOMBINE: LLMs 10-16 points above 75 humans, but 19.9% of concepts repeat a property already used by another model. Analogy retrieval is solved (100%); transfer is not (32-52%).

**Exploratory tasks.** Weak and flat. CreativeBench Explore creativity 0.0146 (7B) and 0.1681 (Flash-Lite). Neither evolutionary search (0.0146 to 0.0182) nor activation steering (0.0169) moved it much, and absolute numbers are tiny. On UoT hypothesis tasks structured exploration did help at 10x tokens (win rate 32.7% vs 14.3% for one prompt) with Qwen3-14B and not with GLM-4-9B.

**Transformational tasks.** Prompt-level rule change helps on low-constraint, human-rated tasks (0.680 vs 0.480) and costs the most tokens (52.5x). On checkable code tasks every forbidden technique cuts correctness (16.1% to 2.1% over five) while divergence rises (4.5% to 15.3%). Weaker models collapse to zero within two states. In math reasoning, RL-trained models regress on transformed skills (-30 points).

**Research ideas.** AI ideas were rated more novel than expert human ideas (5.64 vs 4.84, p<0.01) but gave 200 non-duplicates out of 4000 seeds. Reviewer agreement was low (56.1%). Feasibility was slightly lower.

**Agents on ML engineering.** They explore regions humans did not (GPT-5 1.423 vs gold 0.744) but novelty does not raise performance. Creativity fell and performance rose over iterations for both humans and agents. Search policy (greedy, MCTS, evolutionary) did not matter.

**What changed it, by how much.** Backbone choice (flips the mode ranking). Duplicate memory (collapse 5.6% to 0.0%). Verbalized sampling (1.6-2.1x diversity). Random-prefix (diversity 0.33 to 0.68). Set prompting (distance 0.24 to 0.80, win rate down). Min-p (+17.7% tail quality). Training with a set-level reward (CU 0.64 vs 0.38). Most scaffold wrappers lowered tail quality.

**Evaluation caveat.** UoT tasks are small (3 tasks, 10 generations, 10 raters). The HypoArena judge is a 12B model (two other judges agree 0.59-0.79). 2026 arXiv papers were not checked for peer review.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Keep a persistent duplicate memory in open mode (embedding or meaning-cluster store; reject near-duplicates). Stop open generation when non-duplicate yield per batch falls below a threshold. Do not expect gains past the true answer space. | S3 open, G12 | [E] | K12; d11, b27, c18 |
| Where an automatic verifier exists, use the generate-test loop (LLM as mutation operator, code evaluator, keep valid improvements). Without a verifier this arm is unavailable. | S3, S4 | [E] | K19; c21, c22 |
| Before blending or analogy, add an explicit step listing shared attributes and the mapped mechanism; code dedups against earlier runs. | O7, S3 | [E] for the explanation step and cross-model overlap; the transfer check itself is [S] (K04) | K18; a20, a21, c12 |
| Measure diversity by distinct meaning, not raw cosine above a threshold; compare against a different-idea null. | S3, G8 | [E] direction (homogeneity real, size disputed) | K09, K10; b15, b16 |
| The generating model is never the final selector of novelty (already G8). This evidence adds: judges track LLM taste (0.80 vs 0.65) and LLM raters correlated near zero with experts on stories. | G8 | [E] | K14; b12, d07 |
| Rule changes are budgeted: at most 2-3 drops, each followed by the original check. | O4, G7 | [S] on the numbers; [E] on the direction that rules cost correctness | K21, K22; d08, d09 |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Boden-mode generator (combine / explore / rule-drop) versus a plain search wrapper at equal tokens, on a second backbone and on checkable tasks | S3 | [S] | K01-K03; a14, c07, c08 |
| Route the mode by constraint level (low: rule drop; well-specified: exploratory; control: plain) | S0, S3 | [S] | K02; a12, a13 |
| Analogy transfer check | O7 | [S] | K04; c09 |
| Verbalized sampling inside open mode | S3 | [S] | K11; c19 |
| Set prompting in the explore step, then a quality filter | S3 | [S] | K27; d03 |
| Wiggins R/T/E explicit lists | S3 | [S] | K20; a04 |
| Axiom-level operator versus leaf-rule ban | O4, O8 | [C] | K23; d16 |
| Explore-early, refine-late schedule versus constant mix | S3, S5 | [S] | K13, K28; b03, d11 |
| Score open mode by quality inside the novel tail (q@Tail) | S3, G | [S] | K25; d01 |
| Meaning-entropy as a judge-free stop signal | S3, G | [S] | K29; d13 |
| Judge calibration on 30 human-labelled items, unanimous panels | G8 | [C] | K14; a20, b01 |

Do not add persona voters, self-consistency wrappers or meta-prompting as creativity wrappers: all lowered tail quality in d01 (single source, consistent with G4 and G9).

## 8. Concrete tests on our bench

All arms get equal tokens. Report setup cost (G7). Two backbones where possible.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Mode generator vs plain wrapper | NoveltyBench-style open prompts; 20 low-constraint design tasks | (a) plain best-first search; (b) C/E/T operator prompts; (c) one-prompt control | Distinct-meaning count per 10k tokens; pairwise win rate by a debiased panel of two judge families | Small: UoT ablations 52-58%. Expect no win at equal tokens. |
| T2 Duplicate memory and stop rule | NoveltyBench prompts, 200 batches | memory on / off | cluster count, collapse rate (cosine 0.85 to earlier batches), tokens at stop | Collapse 5.6% to 0%; stop saves tokens near batch 60. |
| T3 Rule-drop budget | Code problems with unit tests, 100 items | drop 0, 1, 2, 3 rules vs plain resampling | pass@1 on original tests, technique-detector absence, divergent-solution rate | Pass rate falls about 30% per rule; divergence rises. Find the knee. |
| T4 Axiom-level vs leaf rule | Same checkable tasks plus ARC-style puzzles | list assumptions, drop most-depended-on, re-derive vs ban one technique | pass rate; solution-type distance | Unknown. |
| T5 Analogy transfer check | 30 tasks with a far-domain analogy | with / without the check | strong-transfer rate (judge), correctness where checkable | Strong transfer above the 32-52% base. |
| T6 Verbalized sampling | open prompts | direct vs verbalized vs set prompt | distinct-meaning count, quality-filter pass, q@Tail | Diversity 1.6-2.1x; quality may drop for set prompt. |
| T7 Explore-then-refine | one checkable task, 20 iterations | constant mix vs 40/60 | best score at fixed tokens; novelty per iteration | Unknown; never compared. |
| T8 Judge stability | 100 outputs, paraphrased in register and in concept order | judge before / after | rank correlation, flip rate | Register shift small (d 0.15-0.29); conceptual shift unknown. |
| T9 Second-backbone UoT replication | HypoArena-style tasks | E/C/T/plain on two backbones, judge from another family | rank of modes per backbone | Ranking flips with backbone. If so, build no mode routing on UoT. |

## 9. What does not transfer, and why

- **Training-time results.** OMEGA's RL generalisation, EvoRePE steering, CreativityNeuro weight steering, random-prefix decoding and min-p sampling need weights or the sampler. A scaffold cannot use them. The set-level reward paper (CU 0.64) also needs training.
- **True transformation.** A scaffold edits the rule list inside a prompt. It cannot change the model's learned conceptual space. Formal theory puts transformation at axioms with many dependents (Theorem 4, d16). A technique ban is a leaf edit. OMEGA shows trained models regress on transformed skills; a prompt cannot supply what the model never learned.
- **Open tasks without a verifier.** AlphaEvolve and Sodarace need automatic evaluators. Open-mode tasks usually lack one, so the generate-test loop applies only where a check exists (G8: novelty is judged by running).
- **Human-creativity ratings.** UoT's human scores come from 10 PhD students and small task sets. They may not match a bench judged by code.
- **Hypothesis-task rankings.** Judged by a 12B model and position-debiased pairwise comparison; rankings flip by backbone, so do not carry them to other models.
- **Token cost.** Mode-specific search costs 7x to 52x a single prompt. Under G7 and G11 it must pay for itself against many short plain attempts.
- **Human processes.** No human study of the explore-then-refine schedule exists. The novelty-falls-while-performance-rises pattern comes mostly from agent trajectories.
- **Boden's own claims.** Her claims about human creators are conceptual. No experiment in the founding text transfers to an agent.

## 10. Open questions

1. Does an explicit Boden-mode generator beat a plain search wrapper at equal tokens on a second backbone and on checkable tasks? Only Magellan (d14) adds a data point: a search wrapper beat ToT on a 1.7B model with an LLM judge and no equal-token check.
2. Does UoT replicate with a different judge family and a larger human panel? No citing paper found (d17).
3. Can the agent route to a mode by constraint level without ground truth? No paper found.
4. What is a cheap, stable judge of conceptual (not register) novelty? Partly closed by AGC-Bench. The Lu et al. 2026 execution audit and TwistBench were not located (d18).
5. What is the yield per token for verbalized sampling and duplicate filters? No paper reported it.
6. Do the primary texts (Boden 2004, Wiggins 2006) define transformation in a way a prompt-level rule change can meet? They could not be opened.
7. Do humans show the iteration pattern (novelty falls as performance rises), and is a scheduled explore-then-refine policy better than a constant mix?
8. Is the leaf-rule versus axiom-level distinction real in practice? Only our inference (K23).
9. Are the three modes separable mechanisms at all, or one creativity factor (81.5% of variance) plus noise?

## 11. Sources

[V] = opened and read this session. [M] = never opened; content is second-hand.

| Mark | Source | URL |
|---|---|---|
| V | Franceschelli and Musolesi (2024) On the Creativity of Large Language Models | https://arxiv.org/abs/2304.00008 |
| V | Espirito Santo, Wiggins, Cardoso (2024) Towards a Formal Creativity Theory | https://arxiv.org/abs/2405.02148 |
| V | Schapiro, Black, Varshney (2025) Transformational Creativity in Science: A Graphical Theory | https://arxiv.org/abs/2504.18687 |
| V | Shahhosseini et al. (2026) LLMs for Scientific Idea Generation: A Creativity-Centered Survey | https://arxiv.org/abs/2511.07448 |
| V | Suzuki and Banaei-Kashani (2026) Universe of Thoughts | https://arxiv.org/abs/2511.20471 |
| V | Sun et al. (2025) OMEGA: Can LLMs Reason Outside the Box in Math? | https://arxiv.org/abs/2506.18880 |
| V | Wang et al. (2026) CreativeBench | https://arxiv.org/abs/2603.11863 |
| V | Schapiro et al. (2026) Measuring Combinatorial Creativity in LLMs and Humans (KOMBINE) | https://arxiv.org/abs/2509.21043 |
| V | Colton, Cook, Hepworth, Pease (2014) On Acid Drops and Teardrops | https://doc.gold.ac.uk/aisb50/AISB50-S03/AISB50-S3-Colton-paper.pdf |
| V | Fanelli (2026) The next Fourier transform | https://arxiv.org/abs/2609.26974 |
| V | Gangloff (2026) Assessing LLMs' mathematical abilities | https://arxiv.org/abs/2608.16118 |
| V | Yu, Ahn, Romero (2026) Dataset repurposing and disruptive AI research | https://arxiv.org/abs/2609.16736 |
| V | Boriceanu and Dinu (2026) Creative Transformation in Literary Texts | https://arxiv.org/abs/2607.28513 |
| V | Wikipedia, Computational creativity (first 100,000 of 124,305 characters) | https://en.wikipedia.org/wiki/Computational_creativity |
| V | Bhushan, Zhang, Wang (2026) Can LLM Agents Discover? Creativity on ML Engineering | https://arxiv.org/abs/2608.30047 |
| V | Chakrabarty et al. (2024) Art or Artifice? | https://arxiv.org/abs/2309.14556 |
| V | Luo, King, Puett, Smith (2026) Inducing Sustained Creativity and Diversity in LLMs | https://arxiv.org/abs/2603.19519 |
| V | Schapiro, Sosa, Park, Varshney (2026) CreativityNeuro | https://arxiv.org/abs/2607.01433 |
| V | Jiang et al. (2025) Artificial Hivemind | https://arxiv.org/abs/2510.22954 |
| V | Schaeffer et al. (2026) How Strong Is the Evidence for the Artificial Hivemind | https://arxiv.org/abs/2609.33936 |
| V | Si, Yang, Hashimoto (2024) Can LLMs Generate Novel Research Ideas? | https://arxiv.org/abs/2409.04109 |
| V | Peng et al. (2025) Probing and Inducing Combinational Creativity in VLMs | https://arxiv.org/abs/2504.13120 |
| V | Gomez-Rodriguez and Williams (2023) A Confederacy of Models | https://arxiv.org/abs/2310.08433 |
| V | Mohammadi (2024) Creativity Has Left the Chat | https://arxiv.org/abs/2406.05587 |
| V | Matthews and Hamilton (2026) Language Models are Lazy Poets | https://arxiv.org/abs/2610.24223 |
| V | Zhang et al. (2026) Verbalized Sampling | https://arxiv.org/abs/2510.01171 |
| V | Lu et al. (2025) Benchmarking Language Model Creativity (Denial Prompting) | https://arxiv.org/abs/2407.09007 |
| V | Lehman et al. (2022) Evolution through Large Models | https://arxiv.org/abs/2206.08896 |
| V | Novikov et al. (2025) AlphaEvolve | https://arxiv.org/abs/2506.13131 |
| V | Wang, Huang, Padmakumar, Lee (2026) Evaluating LLM Creativity through Long-Tail Performance | https://arxiv.org/abs/2610.12998 |
| V | Wadhwa et al. (2026) Training Reasoning Models to Generate Diverse Scientific Ideas | https://arxiv.org/abs/2610.22324 |
| V | Beaty et al. (2026) AGC-Bench | https://arxiv.org/abs/2607.01152 |
| V | Tang et al. (2026) Is Imagination Derived from Hallucination? (Whiteboard) | https://arxiv.org/abs/2609.22152 |
| V | Lingo and Chhajer (2026) Dynamic Context Evolution | https://arxiv.org/abs/2604.07147 |
| V | Min Sen, Chun et al. (2026) Automated Creativity Evaluation of Language Models | https://arxiv.org/abs/2606.11762 |
| V | Chang (2025) Magellan: Guided MCTS for Latent Space Exploration | https://arxiv.org/abs/2510.21341 |
| V | arXiv searches for UoT replication and TwistBench (negative) | https://arxiv.org/search/?query=%22Universe+of+Thoughts%22&searchtype=all |
| M | Boden (1990/1998/2004) The Creative Mind; Creativity and artificial intelligence | https://doi.org/10.1016/S0004-3702(98)00055-1 |
| M | Wiggins (2006) A preliminary framework for description, analysis and comparison of creative systems | https://doi.org/10.1016/j.knosys.2006.04.009 |
| M | Ritchie (2007) Some empirical criteria for attributing creativity to a computer program | https://doi.org/10.1007/s11023-007-9066-2 |
| M | Lehman and Stanley (2011) Abandoning objectives: novelty search | https://doi.org/10.1162/EVCO_a_00025 |

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 3 established claims: 2 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C04.01-K18** (number corrected). The 10-16 points is LLMs' advantage on association and analogy over blending (59.0, 53.4 vs 43.4), not over humans; against 75 humans LLMs lead by about 37, 20 and 31 points (59.0 vs 22.1, 53.4 vs 32.9, 43.4 vs 12.8). Corrected claim: KOMBINE: LLMs are 10-16 points better at association and analogy than at blending, and score well above 75 humans on every task (valid association 59.0% vs 22.1%, analogy 53.4% vs 32.9%, blend 43.4% vs 12.8%), yet 19.9% (412/2,070) of invented concepts reuse a property another model invented; adding an explanation step improved text-to-image mashups (mean rank 1.98 vs 2.40, Peng et al.).
