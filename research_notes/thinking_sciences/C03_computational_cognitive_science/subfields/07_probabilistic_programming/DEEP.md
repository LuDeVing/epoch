# Probabilistic programming: deep document

*Subfield C03.07 of computational cognitive science. Languages for models (Church, WebPPL). Sources: evidence_a-d.jsonl, claims.jsonl (K01-K26), critique.md in this folder. Evidence ids (a01, b05, d10 ...) point to lines in those files. Written 2026-11-20. Schema reference: research_notes/single_agent/SCHEMA.md v0.2.*

Short verdict first. The human-fit results are strong but come from one research group, small samples and hand-built or narrow tasks. The LLM results that matter for an agent are the ones with an explicit checker (SMC with a semantic check, Bayesian-network solvers, hypothesis propose-then-verify). No study compares an LLM-built probabilistic model against long chain of thought from a frontier model at equal tokens (K21). So almost nothing here is "add now" beyond guardrail-style rules that other fields already established.

## 1. What it is

A probabilistic programming language (PPL) lets you write a model of how data or an observation could be produced, as an ordinary program with random choices in it. You then ask a question by conditioning: "given that this happened, what is likely true?" The language runtime does the inference.

Core ideas:

- **A model is a program.** Any generative process can be written as code. Freer and Roy (2012), cited in the WebPPL text, show any computable distribution can be induced by a Church program (a16).
- **Evaluation is sampling.** Running the program once draws one possible world.
- **Query is conditional sampling.** Run many worlds and keep only those where the evidence holds (a01, c01). This is rejection sampling. Smarter samplers (Metropolis-Hastings, particle filters, variational inference) do the same job faster.
- **Memoised random functions (mem).** A random draw is fixed per argument, so a named latent cause stays the same everywhere in one world (a02).
- **Cognitive claim.** The "probabilistic language of thought" proposal says people reason about the world by building such mental models and conditioning them. The language is a tool for writing models of cognition, and also a hypothesis about it.

Main systems in the evidence: Church (2008, Scheme-based), Bher and Stochastic Matlab (2011), WebPPL (functional JavaScript subset, teaching text at dippl.org), Pyro (2018, Python on PyTorch), Stan and PyMC (statistical modelling, used as targets for LLM code), ProbLog (logic-based), LLaMPPL (2023, a PPL where an LLM is a random choice inside the program).

Why this is in our study: it is "background only" for the agent. Our agent is a scaffold of states and operators around a language model. A PPL would matter only as a tool the scaffold could call: the model writes a small generative model, code runs inference, and code returns a posterior. That is the "solver call" idea (K20) and the "write a model then condition" idea (K01).

Links to other subfields in this run (not covered here): Constraint satisfaction, Automated discovery, Language of thought, Imprecise credences, Hierarchical predictive coding, Simulation vs theory accounts, Causal attribution, Minimum message length, Autoformalisation, Efficient diagnosis algorithms, RL on verifiable rewards, Retrieval and ensembles for LLM forecasts, Evidence and probability reasoning.

## 2. History and theories in depth

### 2.1 Church and the founding idea (2008)

Goodman, Mansinghka, Roy, Bonawitz and Tenenbaum presented Church at UAI 2008 (a01, b01, c01). It is a stochastic lambda calculus on Scheme. Primitives: `flip` and other random procedures, `mem` (stochastic memoisation), and `query` / `lex-query`. The paper has no human data. It gives worked examples:

- Sprinkler, rain, wet grass (a02). With `mem`, `(= (rain 'day2) (rain 'day2))` is always true. Draw weights from a Beta(1,1) hyper-prior with `mem` and the program learns weights from other days.
- `DPmem`, a Dirichlet-process memoiser built by stick-breaking (a03). Concentration a=0 gives `mem`; a=infinity gives the identity. It yields infinite mixtures, infinite relational models, HDP-PCFG and HDP-HMM in a few lines.
- Planning as inference (a04). Condition on reward, read off the first action (after Toussaint et al.). Authors say choices are fairly random in the toy game and rejection is inefficient.
- Inference (a05, b02). A collapsed rejection sampler follows from the semantics. Metropolis-Hastings runs over evaluation traces and uses exchangeability. Chain initialisation under hard constraints is itself a rejection problem. Authors name inference cost as the main limit.

Boundary: the paper proves admissibility for `mem` only under conditions (a02), and MH for programs using `mem` is sketched, not fully proven (a05).

### 2.2 Making inference cheap enough (2011-2018)

- Wingate, Stuhlmuller, Goodman (2011): a source-to-source transform gives each random choice an address so MCMC runs at near native speed (a06). Tested on an HMM (sentence length 15, 10,000 samples) and LDA (10 topics, 10 words per document, 30 word types, 1,000 samples). Bher beat the MIT-Church interpreter on HMM and small LDA. MIT-Church scaled better on large LDA because it caches `mem` results and skips recomputation. A geology case study in Stochastic Matlab mixes a GPU renderer with stochastic layers (a07); single case, no error against ground truth.
- WebPPL (a16): purely functional JavaScript with random primitives. Inference uses continuations and coroutines. Exact enumeration costs time proportional to the number of executions, exponential in random choices. Particle filtering often scales better.
- Pyro (2018, a15): Python and PyTorch, stochastic variational inference, GPU maths and mini-batches. Authors state the four goals (universal, scalable, minimal, flexible) conflict and trade-offs were made.

Lesson for the history: the language idea was never the bottleneck. Inference cost was. Every later system exists mostly to fix it (b02). That matters for an agent, because the LLM-era version of the same problem is "how many samples can I afford".

### 2.3 Cognitive science results built on probabilistic programs

- **Rational Speech Act (RSA)**, Frank and Goodman 2012 (a08). A listener infers the referent by Bayes: salience prior times a likelihood that the speaker is informative (utility by surprisal). Reviewed by Goodman and Frank 2016 as nested probabilistic programs: pragmatic listener reasons about a speaker who reasons about a literal listener (a09). Used for scalar implicature, hyperbole, irony, metaphor, vague adjectives.
- **Bayesian Program Learning (BPL)**, Lake, Salakhutdinov, Tenenbaum 2015 (a11-a13, a25). A handwritten character is a generative program of strokes, parts and relations. One-shot classification matches people.
- **Counterfactual simulation model of causal judgment**, Gerstenberg, Goodman, Lagnado, Tenenbaum 2021 (a14). Causal judgment equals noisy simulation of "would the outcome have differed without the candidate cause".
- **Few-shot concept learning with LLM-proposed hypotheses**, Ellis 2023 (a21, a22, b11, c13, c14).
- **Theory of mind as inverse planning**, Ying et al. 2023, 2024 (b05, b09, b26, c15, c16).
- **Learning game rules**, Tsividis et al. 2021, EMPA (b13): programs for a game engine, Bayesian model learning and planning match human learning curves on 90 novel games. Double DQN and Rainbow make little or no progress at human timescales. EMPA gets symbolic object-level input and a hand-built hypothesis space.

### 2.4 The LLM turn (2022-2026)

Four moves, in order:

1. **Language to program (translate then infer).** Wong et al. 2023 "From word models to world models" (a17, a18, b03, b04, c02-c04): an LLM (Codex, few-shot) translates sentences into Church code and inference does the reasoning. Illustrative only (K05). Ying et al. 2023 NIPE and 2024 BToM measured it against humans (K04). Wong et al. 2025 "Model Synthesis Architecture" (MSA) writes a fresh WebPPL model per question with Llama-3.1-70B (b14, c19, d01-d03).
2. **LLM proposes, Bayes weighs.** Ellis 2023; Piriyakulkij et al. 2024 (b12, d14); Wang et al. 2024 Hypothesis Search on ARC (d13).
3. **PPL around the LLM.** LLaMPPL, SMC steering (Lew et al. 2023: a19, a20, b16, c05, c06); Loula et al. 2025 SMC control (b17-b19, c07-c09, d05, d06).
4. **LLM writes statistical models.** BoxLM (Li, Fox, Goodman 2024: a23, a24, c21, c22, d07), RefineStat (c23, c24, d08), Large Language Bayes (d09), LLM-BI (c25), BLInD (d10, d11).

### 2.5 The critique line

- Jones and Love 2011 "Bayesian fundamentalism or enlightenment": flexible priors and likelihoods fit data and ignore mechanism. Recalled, not opened (b21).
- Bowers and Davis 2012 "Bayesian just-so stories": Bayesian accounts can explain almost any behaviour as optimal and are seldom compared with non-Bayesian rivals. Opened (d17). Conceptual review, no pooled statistic.
- Marcus and Davis 2013 (d15, d16): the Frank and Goodman fit depends on a post hoc decision rule. With winner-take-all or a mixed rule, fits look dramatically poorer in their Figure 4 (figures only, no R2). The poetry and movie-gross priors were chosen post hoc; under a different asking assumption, subjects would look biased, not optimal.
- Griffiths, Chater, Norris, Pouget 2012 (d18): a Bayesian model is an empirical hypothesis with testable predictions, flexibility is in all model families, priors can be measured. They concede optimality claims need strong constraints.
- Goodman and Hamrick 2015 reply could not be opened (403).

No systematic re-fit across the literature was found (K17).

## 3. Core findings with exact numbers

Status key: established (two or more independent sources), single-source, contested, unreplicated. Claim ids in brackets.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Church: evaluation is sampling, query is conditional sampling; no human data | UAI 2008 pp. 220-229; Metropolis-Hastings over traces; rejection initialisation problem | Goodman et al. 2008 (a01, a05, b01, c01) [K01] | established as design, no empirical test |
| RSA predicts speaker bets | r=0.98 (P<0.0001), speaker N=206 | Frank & Goodman 2012 (a08) [K03] | established as one-lab result; no replication opened |
| RSA predicts listener bets | r=0.99; r=0.87 after removing 0 and 100 bets; salience alone r=0.19, P=0.40; listener N=263 | Frank & Goodman 2012 (a08) [K03] | same |
| Deeper recursion is rare | about 15% of participants in a complex paradigm; chance in several experiments | Goodman & Frank 2016 (a10) [K03] | boundary condition |
| RSA fit depends on decision rule | winner-take-all or mixed rule give visibly poorer fits (figure only) | Marcus & Davis 2013 (d15) [K17] | contested |
| BPL one-shot classification (20-way) | people 4.5% error (N=40), BPL 3.3%, deep convnet 13.5%, another one-shot deep model 8.0%, Hausdorff 34.8%; BPL without compositionality 11.0% and 14.0% | Lake et al. 2015 (a11) [K02] | single-source |
| BPL visual Turing tests | new exemplars: judges at 52%, 3 of 48 reliably above chance; parsing N=143 judges 59%; lesions: no compositionality 68% (15 of 22 above chance), no learning-to-learn 64% (22 of 45) | Lake et al. 2015 (a12, a25) [K02] | single-source |
| BPL learning to learn from few alphabets | BPL 4.3% and 4.0% with two 5-alphabet sets vs 3.3% with 30; deep nets 24.0% and 22.3% | Lake et al. 2015 (a13) | single-source |
| Noisy counterfactual simulation explains causal judgment | noise 0.9: r=.96, RMSE 13.46; noise 0: r=.86, RMSE 28.15; about N=41 per judgment type | Gerstenberg et al. 2021 (a14) [K18] | single-source |
| Translate-then-infer on goal inference (NIPE) | r=0.927 (CI 0.877-0.953) vs GPT-4 0.658 (0.403-0.79) vs GPT-3.5 0.100 (-0.145 to 0.361); n=46 (6 excluded) | Ying et al. 2023 (b09, c15) [K04] | single paper, re-verified in full text |
| Same for belief statements (BToM) | full model r=0.92 [0.91,0.93]; uniform-over-states prior 0.86 [0.85,0.87]; heuristic mentalizer 0.86 or 0.04 depending on prior; non-mentalizer 0.19; omniscient observer 0.64 (critique correction; b05 listed 0.19); goals r=0.93 [0.91,0.94]; N=100, 9 of 18 scenarios each | Ying et al. 2024 (b05, b06, b26, c16) [K04] | single paper |
| Model synthesis on sports vignettes | fits inside human split-half 95% CI in 3 experiments; N=78, 80, 20; 1000 samples (Exp1-2), 500 (Exp3); LM-only worse, most in open-world Exp3; MSA self-consistency Exp1 vs Exp2 R2 about 0.95-0.98 (read from garbled figure text) | Wong et al. 2025 (b14, c19, d01, d02) [K06, K25] | single-source; exact LM-only R2 not quotable |
| 2023 word-models proposal | no benchmark, no head-to-head; tug-of-war example about 23.9% chance for one player beating another | Wong et al. 2023 (a17, b03, d04) [K05] | established as "illustrative only" |
| Best-of-k by expected information gain (Battleship) | k=1 EIG CodeLlama 0.65, GPT-4 0.66, grammar 0.36; human mean 1.27, best human 3.61, 97% of human questions informative; k=5 near human mean; k=10 beats human mean (p<0.001 CodeLlama, p=0.01 GPT-4); never reaches best humans up to k=50; 18 boards, N=40 humans, 605 question-board pairs | Grand et al. 2024 (b07, c10, d12) [K07] | single-source |
| Translation to program validity | few-shot 75% CodeLlama, 88% GPT-4; GPT-4 zero-shot 40%; 40% and 33% of sampled programs had EIG=0 | Grand et al. 2024 (b07, c11) | single-source |
| Board format | textual board beat no-board (p<0.05, k=1-20); GPT-4V no better than no-board | Grand et al. 2024 (b08, c12) | single-source |
| SMC control raises constraint satisfaction | 10 particles; goal inference 0.063 to 0.419; molecules 0.132 to 0.577; text-to-SQL 0.531 to 0.620; data science 0.213 to 0.346 or 0.407 (70B, cell ambiguous) | Loula et al. 2025 (b17, c07, d05) [K08] | established (two readings plus checks) |
| SMC vs importance sampling | goal: grammar-only SMC 0.401, Sample-Rerank 0.289, Full IS 0.257, Full SMC 0.419; molecules: Full IS 0.404, Full SMC 0.577, grammar-only SMC 0.205; SQL Full IS 0.618 vs Full SMC 0.620 | Loula et al. 2025 (c08, critique) [K08, K10] | established; resampling task-dependent |
| Data science by particles (Llama 3.1 8B) | 5 particles 0.224 vs IS 0.204; 10 particles 0.285 vs 0.223; 50 particles 0.292 vs 0.218; Table 4 says 0.225 for the same N=10 setting | Loula et al. 2025 (d05, d06) [K08] | internal inconsistency in the paper |
| SMC Control vs SMC Steering (SQL) | 0.620 (0.60,0.64) at 10 particles vs 0.607 (0.58,0.63) at 5; intervals overlap | Loula et al. 2025 (b19) [K09] | single-source |
| Small model plus SMC beats larger | Llama 3.1 70B Full SMC beats Codex-002 (175B) on DS-1000; small models beat models over 8x larger in 3 of 4 domains; SQL 1B instruct Full SMC 0.348 vs 0.224 | Loula et al. 2025 (c09, d06) | single paper |
| LLM-written Stan, BoxLM (GPT-4), ELPD-LOO vs expert | Eight schools -30.42 vs -30.70; Dugongs 23.40 vs 22.52; Surgical -38.03 vs -40.29; Peregrine -173.11 vs -142.19 (worse); 4 rounds x 12 proposals | Li et al. 2024 (a23, c21, d07) [K11] | contested (baselines differ across papers) |
| RefineStat run rate | Standard 0.10-0.11, SynCode 0.21, RefineStat 0.45-0.50; about twice the tokens; DQ-7B Dugongs 8.35 vs 22.43, Surgical -114.29 vs -39.73, Eight schools -30.68 vs -30.70, GP -23.39 vs -26.53 | Kanda/Ghosh et al. (c23, c24, d08) [K12] | single-source |
| o3 writing Stan (fixed PosteriorDB set) | expert vs o3: Eight schools -30.70 vs -30.74; Dugongs 22.43 vs 22.83; Surgical -39.73 vs -38.73; Peregrine -112.60 vs -133.29; GP -26.53 vs -34.95 | RefineStat paper (d08) [K22] | single-source; textbook models may be in training data |
| LLM-proposed hypotheses plus Bayes, logical concepts | R2=0.81 at 100 proposals per batch; within 3% of human accuracy; 112 concepts; 1,596 participants; beats GPT-4 alone | Ellis 2023 (a21, c14) [K13] | single-source |
| Number Game | R2 about 0.95 (figure; tuned prior) vs 8 humans; 50-100 proposals vs over 5000 hypotheses classically; English hypotheses beat Python | Ellis 2023 (a21, a22, c13) [K13] | single-source; 10^9 proposals claim unverified |
| Online rule revision (Zendo) | human 5.26/8; ReAct 4.60; best model 6.55; fit to humans: online fuzzy R2=0.57, hard rules 0.10, batch 0.05, ReAct 0.25 | Piriyakulkij et al. 2024 (b12, d14) [K14] | single-source |
| ActiveACRE solving | 0.00 for ReAct and fuzzy rules; 0.10-0.15 batch and refinement; 0.35 online hard rules | Piriyakulkij et al. 2024 (d14) | single-source |
| Hypothesis search on ARC (GPT-4, 100 of 400 training tasks) | direct 17%; program only 23%; LLM-summarised hypotheses 30%; human-selected 33%; human-written 45%. 1D-ARC (108): 39.6 / 61.1 / 73.1 | Wang et al. 2024 (d13) [K23] | single-source for the numbers; two related studies |
| CoT collapses on Bayesian networks | GPT-4 few-shot CoT by variables V2..V10: 78, 64, 36, 25, 22, 16, 7, 7, 7 percent; ProbLog 99, 98, 100, 100, 96, 97, 97, 98, 96; Monte Carlo 100 down to 88; plain Python PAL 7 at V10; 900 test instances | Nafar et al. 2024 (d10) [K20] | single-source |
| Small causal items: CoT is fine | CLADDER adaptation (100 items) GPT-4: CoT zero-shot 64, CoT few-shot 96, PAL 98, Monte Carlo 97; GPT-3.5 CoT few-shot 26, PAL 75 | Nafar et al. 2024 (d11) [K20] | single-source |
| Distribution reasoning over long context | over 60% degradation as context grows | Pournemat et al. 2025 (d21) | single-source |
| GPT-3 vs humans on structured thought | humans beat GPT-3 in every condition (p<0.001); blind raters N=393; 240 human generators; LLM-as-planner solved none of the most constrained problems | Collins et al. 2022 (b10, c17) [K15] | established (old model) |
| CLIPS pragmatic instruction following | 1.26-1.68x faster, 1.18-1.58x cheaper than baselines; human-rating r=0.15 to 0.96 | Zhi-Xuan et al. 2024 (c18) [K16] | single-source |
| LLM-elicited priors | near-identical posteriors to manual weak priors; one regression only | Huang 2025 (c25) [K19] | single-source |
| Cost anchors | 1024 Stan models in 10-15 min on one A100; DS-1000 SMC runs on 4 H100 and 64 vCPUs; BLInD solver in milliseconds vs seconds for LLM generation | Domke 2025 (d09), Loula (d06), Nafar (d11) [K26] | anchors only, none matched to CoT |

## 4. Mechanisms and models

Each model is explained at the level an engineer could implement it. None is run by our harness today.

### 4.1 Rejection sampling and conditioning (the base operation)

```
def query(model, condition, n):
    out = []
    while len(out) < n:
        world = model()          # run program once, all random choices drawn
        if condition(world):     # evidence holds in this world?
            out.append(world)
    return out                   # samples from the posterior
```

Cost: 1 / P(evidence) draws per kept sample. If evidence is rare, this fails. This is the "initialisation problem" in Church (b02) and the "significant time cost" in MSA (d01). MSA used 1000 samples (Exp1-2) or 500 (Exp3) of rejection sampling in WebPPL, with 10 simulated participants per vignette (d01).

Fixes in order of cost: enumeration for small discrete models (time proportional to executions, exponential in random choices, a16); MCMC over program traces (a05, a06); particle filtering / SMC (a16, a19); variational inference (a15).

### 4.2 Stochastic memoisation (`mem`)

```
cache = {}
def mem(f):
    def g(*args):
        if args not in cache: cache[args] = f(*args)
        return cache[args]
    return g
```

Reset the cache at the start of every world. Effect: a latent such as "person X's strength" is drawn once per world and reused in every sub-question. DPmem generalises this with a Chinese-restaurant style reuse probability (a03).

### 4.3 Rational Speech Act (RSA)

For a reference game with objects o and utterances u:

```
L0(o | u)  proportional to  [u is true of o] * prior(o)     # literal listener
S1(u | o)  proportional to  exp(alpha * (log L0(o|u) - cost(u)))   # speaker
L1(o | u)  proportional to  S1(u | o) * prior(o)            # pragmatic listener
```

Frank and Goodman used a measured salience prior, `alpha=1`-style informativeness and a proportional (probability matching) decision rule in the betting task (a08, a09). Marcus and Davis showed that the fit changes when the decision rule is winner-take-all (d15). Extensions needed: non-deterministic adjective semantics and incremental utterance choice for redundant colour adjectives (Waldon and Degen 2021, d19). Implementation note: all quantities are small tables, so exact enumeration is enough.

### 4.4 Bayesian program learning (BPL)

Generative program: draw number of strokes, draw each stroke from primitives and relations, render with motor noise. Classification: score the test image under each class's inferred program(s). Learning to learn: the priors on strokes and parts come from a background set of alphabets (30 alphabets gives 3.3% error, 5 alphabets 4.0-4.3%, a13). Needs hand-built primitives (a11).

### 4.5 Counterfactual simulation model

```
for each clip: S = observed trajectory with the candidate cause
    for i in range(n): S_cf = re-run physics without the candidate, with noise sigma on object motion
    p_cause = fraction of runs where the outcome differs
```

Noise sigma is a fitted parameter (0.9 gave the best fit; 0 gave the deterministic model, worse, a14). Needs a physics engine.

### 4.6 Translate-then-infer (NIPE, BToM, MSA)

Pipeline:

1. LLM maps text to a formal problem. NIPE: goal-inference problem in a gridworld. BToM: an epistemic-logic formula over agent beliefs and goals. MSA: a fresh WebPPL model per question.
2. A probabilistic program (inverse planning, Bayesian theory of mind) is run on that formal object.
3. Code returns a graded posterior.

BToM model: joint posterior over goal, belief and plan given observed actions; the plan layer is needed (b26: removing the goal-to-instrumental-plan link hurts). Translation quality is a separate failure point (see 5.3).

### 4.7 Propose-then-reweight (Ellis 2023) and online revision

```
H = llm.propose(examples, n=100)            # hypotheses as English sentences
H = [translate_to_code(h) for h in H]       # optional, English did better than Python
for h in H: score(h) = prior(h) * prod(likelihood(x | h) for x in examples)
posterior over h; answer = weighted vote of h(test)
```

Prior is fine-tuned on human ratings (critical for logical concepts, a21). Ablating the data-conditioned proposal gives a poor fit (a22). Online version (Piriyakulkij): keep a particle set of rules, after each experiment reweight, resample, and ask the LLM to revise rules that conflict with new data (b12). Fuzzy rules fit people better, hard rules score higher accuracy (b12).

### 4.8 SMC steering and SMC control for LLM decoding

Treat generation as a Feynman-Kac model over token sequences (a19):

```
particles = [empty] * N
for step in range(T):
    for p in particles: extend p by one token (or a token block) from LM; weight *= potential(p)
    if effective sample size is low: resample particles proportionally to weight
return weighted particles
```

- Cheap potentials: grammar mask, syntax check. Expensive potentials: execute the code, check a semantic constraint (Loula, b17, b18).
- Expansion factor K=3 in the 2023 paper (a19). A trie cache avoids repeated LLM calls across particles (a19).
- E[log Z-hat] lower-bounds log Z and the gap bounds KL between sampler and true posterior (a20). Chain-of-thought proposals break exact proposal density (a20).
- Needs token probabilities, so closed chat APIs without logits cannot be used (c06). Token masking can distort the distribution; SMC with potentials tends to the constrained posterior as particles grow (c06).
- Ablation (b18, c08): the expensive potential does most of the work; weight correction helps little or not at all on goal inference and molecules once the expensive check is in; resampling matters on goal inference (grammar-only SMC 0.401 vs IS 0.083) but not on SQL.

### 4.9 Best-of-k by expected information gain (Loose LIPS)

```
qs = [llm.sample_question(board_text) for _ in range(k)]
progs = [llm.translate_to_dsl(q) for q in qs]     # 75-88% valid with few-shot
for each prog: EIG(prog) = H(answer) over worlds consistent with the board so far
pick argmax EIG
```

Needs a world model (Battleship board posterior) to compute EIG. Textual board description is better than image (b08).

### 4.10 Box's loop with an LM (BoxLM, RefineStat)

BoxLM: proposer LM writes a PyMC program (temperature 0.7), fit by MCMC, posterior predictive checks and ELPD-LOO, critic LM (temperature 0) reads the statistics and suggests changes; 4 rounds, 12 proposals per round (c21). Only 70-78% of programs executed in the variants tested (c21). RefineStat adds semantic checks during decoding and resamples priors or likelihood when diagnostics fail (Rhat, ESS, divergences, Pareto-k); executable rate 0.10 to 0.45-0.50 on four 7-8B models (c23).

### 4.11 Solver call for many interacting quantities (BLInD)

Gate: extract variables and conditional probability tables from the text, emit ProbLog or Monte Carlo code, run it, read the number. Accuracy stayed 96-100% (ProbLog) while GPT-4 CoT fell from 78% to 7% as variables grew from 2 to 10 (d10). On small problems CoT is equal (96 vs 98, d11). The solver is exact and takes milliseconds; the cost is the LLM writing the code (d11).

## 5. What holds up

### 5.1 Replications

- **Church-era claims**: no replication numbers found (critique). The founding paper is a language paper with no data.
- **RSA (Frank and Goodman 2012)**: no many-labs or cross-language replication was opened (K24). A close replication by Qing and Franke 2015 is known only from a search snippet (d20), which also says one-shot web-based language games suggest listeners may be less pragmatic than assumed. Waldon and Degen 2021 is an extension, not a replication, and shows basic RSA does not predict redundant colour adjectives without extra machinery (d19). Treat the fit as one-lab.
- **BPL (Lake 2015)**: no replication opened. The numbers rest on one paywalled paper not re-opened by the critique; the later line "deep nets narrowed the gap" is noted in a11 as a limit.
- **Tug-of-war**: Wong et al. 2025 Exp 1 is described by the authors as essentially replicating the 2014 tug-of-war probabilistic-model result with synthesised models (b24). Same group, same stimulus family. 2014 original numbers were not retrieved.
- **BoxLM vs RefineStat on Peregrine**: not a failed replication. They are different datasets under one name (real 40 counts, 1964-2003, expert -142.19; simulated 9 years, expert -112.60, d07, d08). Small differences on Surgical (-40.29 vs -39.73) and Dugongs (22.52 vs 22.43) are unexplained.

### 5.2 Failures and internal inconsistencies

- Deeper social recursion works in only about 15% of participants (a10).
- RSA fit depends on the decision rule (d15).
- BPL needs hand-built primitives (a11).
- Loula Table 4 vs Table 6: data-science Full SMC 0.225 vs 0.285 for the same setting (d06). The 70B 0.346 vs 0.407 cell is unassigned (d05).
- Piriyakulkij: LLMs revise hypotheses well but do not consistently beat random guessing when proposing experiments (b12). ActiveACRE solved 0.00 by ReAct and fuzzy rules (d14).
- BoxLM fails on Peregrine (-173.11 vs -142.19) and no-metadata Surgical (sim -63.72 vs -39.80, c21). Metadata can hurt: with metadata it chose a logistic growth model that misses the early decline; without it a quartic polynomial closed the gap (a24).
- RefineStat DQ-7B misses experts on Dugongs and Surgical (c23, d08). The critique corrected an earlier line that implied it matched experts everywhere.
- Hypothesis Search on ARC: still far from solved at 45% with human-written hypotheses (d13).
- Wong 2025 MSA: sample variance often too low; struggled to invent models for a truly novel sport (d03, c19).
- Wong 2025: one domain was dropped because humans disagreed with each other (b25).

### 5.3 Moderators and boundary conditions

- **Prior and decision rule.** BToM drops from r=0.92 to 0.86 with a different belief prior, and a heuristic mentalizer collapses to r=0.04 with a wrong prior (b05, b06). RSA depends on decision rule (d15). Ellis: tuned prior matters, especially for logical concepts (a21).
- **Translation quality.** Few-shot 75-88%, zero-shot 40% (b07, c11). 33-40% of sampled programs had zero EIG (b07). 70-78% executability for BoxLM (c21), 10% to 45-50% with RefineStat (c23).
- **Verifier.** SMC gains need an expensive semantic check; grammar alone helped little (goal inference 0.063 to 0.086, c08). Tasks all had formal checkers (b17).
- **Model size.** Gains from SMC are larger for smaller LMs (d06). o3 matched the expert on 3 of 5 Stan problems (d08).
- **Task size.** CoT collapses with number of variables (d10) but not on 100 small CLADDER items (d11). Direct reasoning over explicit distributions degrades over 60% as context length grows (d21).
- **Board format.** Text beat image for Battleship (b08).
- **Hypothesis language.** English hypotheses beat Python hypotheses (a22).
- **Metadata.** Can hurt model discovery (a24).
- **Training-data leakage.** BoxLM used simulated analog datasets to handle leakage (a23). The o3 result uses textbook models that may be in training data (d08). Domke asks that problems not be reused for models with a cutoff after 21 April 2025 (d09).

### 5.4 Competing explanations

- **Why translate-then-infer beats plain LLMs on human fit.** Wong 2025 suggests LM baselines are incoherent across related variables, while synthesised models are coherent by design (b15). Untested; a competing explanation is that LM baselines were prompted one way only (b15). The only LM baselines used were Llama-3.1-70B direct and CoT, with temperature 1.0 and 5 scalar judgments x 8 questions (d01).
- **Why Bayesian models fit.** Because people are near-Bayesian (Griffiths et al.), or because priors and decision rules are tuned (Bowers and Davis, Marcus and Davis). Not resolved (K17).
- **Why SMC helps.** Mainly the expensive potential (b18), not the resampling.

### 5.5 What worked, what did not

| Worked | Did not |
|---|---|
| Expensive semantic checks inside decoding (b17, b18) | Grammar-only constraints (c08) |
| Best-of-k by information gain up to the human mean (b07) | Matching the best humans at any k up to 50 (d12) |
| Solver code for large Bayesian networks (d10) | Plain Python PAL at 10 variables (7%, d10) |
| LLM proposes hypotheses, evidence filters them (a21, d13) | LLM-only judgments (GPT-4 "decidedly different from humans", a21) |
| Textual board description (b08) | Image board (GPT-4V, b08) |
| Online revision of fuzzy rules for human fit (b12) | Batch inference (R2 0.05, b12) |
| Few-shot translation (b07) | Zero-shot translation (40%, c11) |
| Semantic checks during PyMC decoding (c23) | Standard decoding (run rate 0.10-0.11, c23) |

## 6. Language models

How LLMs behave on tasks in this subfield, what changed performance, by how much. All measured with 2021-2025 models; none with a long-reasoning frontier model except the o3 Stan result.

**LLM as direct judge of human-like graded beliefs**

- NIPE goal inference: GPT-4 r=0.658, GPT-3.5 r=0.100 against humans; translate-then-infer r=0.927 (b09). GPT-4 near zero on the Colored-Different variant (it ignored a stated key rule), weak on spatial path planning.
- BToM: models that do not infer mental states score r=0.19; omniscient observer 0.64; full model 0.92 (b05). These are model-vs-human baselines, not LLM direct baselines.
- Wong 2025: Llama-3.1-70B direct and CoT fit worse than MSA, with the gap largest in the open-world experiment and for a sport not in published literature (b14, c19, d02). No R2 values in text. LMs correlate with each other more than with humans (d02).
- GPT-3 (2022) lost to humans in every planning and explanation condition (N=393 raters, p<0.001); as a planner it solved none of the most constrained problems (b10, c17). A Parse-and-Solve hybrid (Codex to PDDL plus symbolic planner) did better on constrained planning (c17).
- Ellis: raw GPT-4 yes/no probabilities were decidedly different from humans; propose-then-reweight reached R2=0.81 (a21).

**LLM as probabilistic reasoner on explicit numbers**

- Bayesian networks: GPT-4 CoT 78% at 2 variables, 7% at 10 (d10). Code route 96-100%.
- Small causal items: CoT fine (96%, d11). GPT-3.5 CoT few-shot 26% vs PAL 75% (d11).
- Distributions in context: over 60% degradation as context length grows; DeepSeek-R1-Distill-Qwen-7B and GPT-4o-mini included (d21).
- What changed it: moving the arithmetic out of text and into code. Size of change on 10-variable networks: 7% to 96-100% (d10).

**LLM as model writer**

- Stan/PyMC: GPT-4 matched expert on 3 of 4 BoxLM datasets (c21). o3 matched on 3 of 5 (d08). 7-8B models write runnable programs 10-11% of the time by default, 45-50% with RefineStat, at about twice the tokens (c23).
- GPT-4 text-only vs plots-only did about as well; GPT-3.5 comparable on most datasets (c22).
- LLM-elicited priors gave posteriors near-identical to manual weak priors on one regression (c25).

**LLM as hypothesis proposer**

- ARC with GPT-4 on 100 tasks: direct 17%, program only 23%, LLM-summarised hypotheses 30%, human-written 45% (d13). Gains are real but the ceiling is the LLM's own hypothesis quality.
- Zendo: online SMC over LLM rules 6.55/8 best vs ReAct 4.60/8 (b12).

**LLM as generator steered by a PPL**

- SMC with an expensive check, 10 particles: goal inference 0.063 to 0.419, molecules 0.132 to 0.577, SQL 0.531 to 0.620 (b17). Small models beat models more than 8x larger in 3 of 4 domains (c09).
- Resampling beats importance sampling with one-tenth of particles in 3 of 4 domains and one-fifth in the fourth (b17).

**LLM as question generator**

- Battleship: single sample below human mean (0.65-0.66 vs 1.27); best of 10 above human mean; best humans never matched (b07, d12).

**Cost**

- Wong 2023 and 2025 report no tokens or latency; the only remark is that rejection sampling "incurs a significant time cost" (d01, d04). BLInD gives solver time in milliseconds vs seconds for LLM generation, but no token table (d11). RefineStat uses about twice baseline tokens (c23). 1024 Stan models took 10-15 minutes on one A100 (d09). None is matched to CoT.

**What is not measured**

- Any frontier reasoning model with long CoT against an LLM-built probabilistic model at equal tokens (K21). This is the single most important hole.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, memory. Remember the subfield is rated "background only", so most items are "test first".

### Add now (established)

| Item | Schema part | Status | Evidence | Note |
|---|---|---|---|---|
| Do not claim a probabilistic route helps unless it beats the plain route at equal tokens | G7 (already) | [E] as rule; the absence of a matched baseline is itself established | K21; d01, d04, d09 | Already in G7. Do not add a new rule; record that no PPL result here is a matched-token result. |
| Fix the model structure and priors before looking at the fit; never tune priors to the item being scored | G3 (already) | [E] | K17; d15, d16, d17, d18 | Same logic as G3 (a pass must be on something the answer was not fitted to). Adds nothing new to the schema; supports G3. |
| Put the expensive check inside the loop, not grammar or style checks | G2 / S4 (already) | [E] | K08, K10; b17, b18, c08 | Consistent with S4 and G2. Cheap syntax checks alone gained 0.063 to 0.086 on goal inference. |
| Report the executable rate and the final score separately when a step writes code | log section 6 | [E] by two papers | K11, K12; c21, c23 | Run rate 0.10 to 0.50 hides whether the final answer is better. Add to run logs if not present. |

No new operator or state is established enough to add now. The established items support rules already in the schema.

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence | What it would be |
|---|---|---|---|---|
| Solver gate: if more than about 5 interacting quantities, write code and run it instead of reasoning in text | S0 / S3 (mode "checked" with a solver) | [S] | K20; d10, d11, d21 | CoT 78% to 7% from 2 to 10 variables vs code 96-100%. But CLADDER small items are equal, and models are 2023-24. |
| Propose-then-verify hypotheses (propose several rules, run each on the examples, keep those that pass all) | S2, S4, O (hypothesis operator) | [S] | K13, K23; a21, d13 | GPT-4 ARC 17% direct to 30% with summarised hypotheses. Overlaps with G3: a rule passing every example is not proof. |
| Best-of-k by expected information gain for question-asking tasks | S3 (many draws, code selects) | [S] | K07; b07, d12 | Needs a world model to score EIG. Only one task. |
| Check placement ablation: checker only vs checker plus resampling | G5 / S4 | [S] | K10; b18, c08 | Resampling helped goal inference not SQL. |
| Counterfactual simulation with noise for causal items | O (simulate) | [S] | K18; a14 | Needs a simulator, human-fit only. |
| Translate-then-infer for social reasoning | O (symbolic world model) | [S] contested between human fit and matched-token gain | K04, K06; b05, b09, b14 | Human-fit evidence is good (r 0.92-0.93) but no matched-token baseline (K21). |
| Online revision of fuzzy rules in interactive discovery | S5 / O | [S] | K14; b12, d14 | Narrow task family; ActiveACRE 0.00 for fuzzy ReAct. |
| Persistent named latents (`mem` idea) as a memory structure inside one problem | memory | [S] only as an analogy to Church | K01; a02 | No test in the evidence. Cheap to try as "named assumptions list". |
| Audience-aware check (what would a speaker mean) for ambiguity items | O | [S] one-lab result | K03, K24; a08, d15 | RSA fit is decision-rule sensitive. |

## 8. Concrete tests on our bench

Both arms at equal tokens (including the cost of the model-writing step, G7). Item types follow our bench: word puzzles (BrainTeaser type), ARC-like rule tasks, and uncertain-evidence arithmetic items we can build.

| # | Item type | Arm A | Arm B | Metric | Expected effect |
|---|---|---|---|---|---|
| T1 | Probability items with 2, 4, 6, 8, 10 interacting variables (Bayesian networks written as text) | Plain short CoT, N attempts, majority vote | LLM writes ProbLog or Monte Carlo code, code runs it, 1-2 repair rounds | Accuracy by variable count, tokens | Gap opens above about 5 variables (d10: CoT 25% at 5 variables vs 96-100%); no gap at 2-3. Frontier models may keep CoT high longer; that is the question. |
| T2 | ARC-like few-shot rule tasks (training split, 100 tasks) | Direct program writing with N samples, pick by agreement | Propose M natural-language rules, implement each, keep those passing all training pairs and a held-out pair, tie-break by shortest | Pass rate on held-out test grid | +5 to +13 points as in GPT-4 (17 to 30, d13), likely smaller with a stronger model. Matches G3 so held-out pair must be used. |
| T3 | Question-asking items (20-questions or Battleship-like with a known world model) | One question from one sample | k=5 and k=10 sampled questions, code scores EIG against the world model, pick best | Mean EIG per question; final identification rate | EIG above single sample, near or above human mean at k=10 (b07). Report tokens per extra sample. |
| T4 | Items where the answer is checkable by code (SQL, code with unit tests, constraint tasks) | Best-of-N with the checker as final filter | Particle-style branch and prune: partial attempts scored by the checker mid-way, resample from survivors | Pass rate at equal total tokens | Gain over best-of-N only if the checker can score partial work. SQL showed no resampling gain (0.618 vs 0.620, c08), so test on goal-like tasks too. Requires logits for the exact method; use block-level resampling with an API model. |
| T5 | Check placement ablation on T4 items | checker at end only | checker mid-way only vs mid-way plus resampling | Pass rate | Expect the mid-way check to account for most of any gain (b18). |
| T6 | Everyday social-reasoning items with graded answers (Ying-style gridworld clips converted to text) | CoT answer as a number 1-7 | LLM translates to a small inverse-planning model, code returns the posterior | Correlation with human mean (we have none for our own items; use item-level gold from a small rater group) or accuracy on items with a determinate answer | Large gap against GPT-3.5-class models, smaller against GPT-4 (0.927 vs 0.658). Frontier gap unknown. |
| T7 | Causal counterfactual items with a simulator | CoT explanation | simulate-with-noise counterfactual in code | Accuracy against the simulator's true answer | Unknown; only human-fit evidence exists (a14). |
| T8 | Persistent named assumptions (`mem` analogue) on multi-question problem sets sharing latent facts | Fresh reasoning per question | One shared list of named latents carried across questions | Consistency rate across questions; accuracy | Better consistency; accuracy effect unknown. Cheap test. |
| T9 | Any of T1-T7, report separately | executable-rate and final-score | | both | Prevents run-rate gains hiding a flat final score (c23). |

Controls for all: same total token budget counted from the first token (model-writing step included); same model; held-out items; report per-class results (G7, G3). If a frontier reasoning model is the base, add a "long CoT at the same budget" arm, because that is the missing comparison (K21).

## 9. What does not transfer, and why

- **Human-fit evidence is not correctness evidence.** NIPE, BToM, RSA, counterfactual simulation and the MSA results score agreement with human graded judgments, not truth. High r with few items inflates (NIPE n=46, Number Game 8 humans, critique).
- **Hand-built domains.** BToM is one gridworld, BPL needs stroke primitives, EMPA needs object-level symbolic input and a hand-built hypothesis space, Battleship needs a DSL, Zendo has a very small hypothesis space (a11, b13, b07, d14).
- **Same-group results.** Almost all LLM-PPL human-fit papers come from one network of labs. Wong 2025 Exp 1 replicates their own 2014 stimulus (b24).
- **Model age.** Codex, GPT-3, CodeLlama-7b, gpt-4-0613, Llama-3.1-70B. The o3 Stan result is the only reasoning-model data (d08), and textbook models may be in training data.
- **Needs logits.** SMC steering needs token probabilities, so a closed API without logits cannot run it exactly (c06). Chain-of-thought proposals break exact weights (a20).
- **Needs a checker.** Gains come where a formal check exists (b17). Our open-mode and no-check tasks have none (SCHEMA modes).
- **Inference cost.** Rejection sampling is slow, and the original Church authors say so (a05). SMC data-science runs used 4 H100 GPUs (d06).
- **Not a reasoning style for people to copy.** The theory is about what the mind computes, not about a verbalised procedure. Our schema moves only through code-checked states; a PPL would be one solver the code can call, not a new state.
- **Critique line not settled.** Flexibility of priors and decision rules (K17). Do not read a good fit as proof the model is right.
- **Number Game and Zendo scale.** Hypothesis spaces are tiny compared with open reasoning.
- **No matched-token baseline.** See K21; this is why nothing here goes into the schema.

## 10. Open questions

1. Does an LLM-built probabilistic model plus sampling beat long CoT from a frontier reasoning model at equal tokens on any reasoning benchmark? (K21, gap 1)
2. What is the token cost of translate-then-infer (Wong 2023, 2025) against CoT, and does the gain survive matching it? (gap 2)
3. Does best-of-k by EIG hold with frontier models, and what is its cost curve? (gap 3; tested only to k=50 with CodeLlama-7b and gpt-4-0613)
4. Exact R2 values and LM-only baselines in Wong 2025 Exp 1-3; original 2014 tug-of-war numbers. (gap 4, K25)
5. Have Frank and Goodman 2012 and Lake 2015 been replicated at many-labs scale or cross-language? Open Qing and Franke 2015 to read the numbers. (gap 5, K24)
6. Which data-science Full SMC cell in Loula is right (0.346, 0.407, or 0.285 vs 0.225)? Does it hold at 5 particles? (gap 6; 8B 5 particles 0.224 vs IS 0.204 is small)
7. How do LLM-written Stan programs fare on a fixed expert set with several frontier models and fresh, non-textbook problems? (gap 7)
8. Do flexible priors preserve or break fits in systematic re-analyses? No cross-study re-fit exists. Goodman and Hamrick 2015 reply not read. (gap 8, K17)
9. Does Bayesian reweighting (Ellis) help on ARC beyond a pass-all-pairs filter? Hypothesis Search used no reweighting. (gap 9, K23)
10. Is the coherence explanation for LM baseline misfit right (b15), or does better prompting close the gap?
11. Can block-level (not token-level) SMC with a closed API recover most of the SMC gain? Not tested.
12. How much of the o3 Stan result is memorised textbook models? (d08)
13. What does an agent that writes a probabilistic model do when the translation is wrong (33-40% zero-EIG samples)? Is there a cheap validity check before running inference?

## 11. Sources

[V] opened this session (full text or page). [M] snippet or recalled only. Notes in brackets where the critique says otherwise.

**Founding and systems**
- [V] Goodman, Mansinghka, Roy, Bonawitz, Tenenbaum (2008) Church: a language for generative models. https://arxiv.org/abs/1206.3255 (a01-a05, b01, b02, c01)
- [V] Wingate, Stuhlmuller, Goodman (2011) Lightweight implementations of probabilistic programming languages via transformational compilation. https://proceedings.mlr.press/v15/wingate11a.html (a06, a07)
- [V] Goodman & Stuhlmuller, The Design and Implementation of Probabilistic Programming Languages (WebPPL, dippl.org). https://dippl.org/chapters/01-introduction.html (a16)
- [V] Bingham et al. (2018) Pyro: deep universal probabilistic programming. https://arxiv.org/abs/1810.09538 (a15)

**Cognitive science**
- [V per evidence line; paywalled, critique did not re-open] Frank & Goodman (2012) Predicting pragmatic reasoning in language games. https://doi.org/10.1126/science.1218633 (a08)
- [V] Goodman & Frank (2016) Pragmatic language interpretation as probabilistic inference. https://doi.org/10.1016/j.tics.2016.08.005 (a09, a10)
- [V per evidence line; paywalled, critique did not re-open] Lake, Salakhutdinov, Tenenbaum (2015) Human-level concept learning through probabilistic program induction. https://doi.org/10.1126/science.aab3050 (a11-a13, a25; b20 is a recalled duplicate, [M])
- [V per evidence line; paywalled, critique did not re-open] Gerstenberg, Goodman, Lagnado, Tenenbaum (2021) A counterfactual simulation model of causal judgments for physical events. https://doi.org/10.1037/rev0000281 (a14)
- [V] Tsividis et al. (2021) Human-level reinforcement learning through theory-based modeling, exploration and planning. https://arxiv.org/abs/2107.12544 (b13)
- [V] Waldon & Degen (2021) Modeling cross-linguistic production of referring expressions. https://aclanthology.org/2021.scil-1.19v1.pdf (d19)
- [M] Qing & Franke (2015) close replication of Frank & Goodman. https://escholarship.org/uc/item/9gh7r8g7 (d20; snippet, not read)

**Critique line**
- [M] Jones & Love (2011) Bayesian fundamentalism or enlightenment? https://doi.org/10.1017/S0140525X10003134 (b21, recalled)
- [V] Bowers & Davis (2012) Bayesian just-so stories. https://pages.ucsd.edu/~mckenzie/Bowers&Davis2012PsychBull.pdf (d17; b22 is the recalled duplicate)
- [V] Marcus & Davis (2013) How robust are probabilistic models of higher-level cognition? https://sites.socsci.uci.edu/~lpearl/courses/readings/MarcusDavis2013_BayesianCognition.pdf (d15, d16; b23 is the recalled duplicate)
- [V] Griffiths, Chater, Norris, Pouget (2012) How the Bayesians got their beliefs (and what those beliefs actually are). https://sites.socsci.uci.edu/~lpearl/courses/readings/GriffithsEtAl2012_BayesianBeliefs.pdf (d18)

**LLM and PPL**
- [V] Wong et al. (2023) From word models to world models. https://arxiv.org/abs/2306.12672 (a17, a18, b03, b04, c02-c04, d04)
- [V] Wong, Collins, Ying, Zhang, Weller, Gerstenberg, O'Donnell, Lew, Andreas, Tenenbaum, Brooke-Wilson (2025) Modeling open-world cognition as on-demand synthesis of probabilistic models. https://arxiv.org/abs/2507.12547 (b14, b15, b24, b25, c19, c20, d01-d03)
- [V] Ying et al. (2023) The Neuro-Symbolic Inverse Planning Engine (NIPE). https://arxiv.org/abs/2306.14325 (b09, c15)
- [V] Ying, Zhi-Xuan, Wong, Mansinghka, Tenenbaum (2024) Grounding language about belief in a Bayesian theory-of-mind. https://arxiv.org/abs/2402.10416 (b05, b06, b26, c16)
- [V] Zhi-Xuan, Ying, Mansinghka, Tenenbaum (2024) Pragmatic instruction following and goal assistance via cooperative language-guided inverse planning (CLIPS). https://arxiv.org/abs/2402.17930 (c18)
- [V] Collins, Wong, Feng, Wei, Tenenbaum (2022) Structured, flexible, and robust: benchmarking and improving LLMs towards human-like behavior in out-of-distribution reasoning tasks. https://arxiv.org/abs/2205.05718 (b10, c17)
- [V] Grand, Pepe, Andreas, Tenenbaum (2024) Loose LIPS sink ships: asking questions in Battleship with language-informed program sampling. https://arxiv.org/abs/2402.19471 (b07, b08, c10-c12, d12)
- [V] Ellis (2023) Human-like few-shot learning via Bayesian reasoning over natural language. https://arxiv.org/abs/2306.02797 (a21, a22, b11, c13, c14)
- [V] Piriyakulkij, Langenfeld, Le, Ellis (2024) Doing experiments and revising rules with natural language and probabilistic reasoning. https://arxiv.org/abs/2402.06025 (b12, d14)
- [V] Wang et al. (2024) Hypothesis search: inductive reasoning with language models. https://arxiv.org/abs/2309.05660 (d13)
- [V] Lew, Zhi-Xuan, Grand, Mansinghka (2023) Sequential Monte Carlo steering of large language models using probabilistic programs. https://arxiv.org/abs/2306.03081 (a19, a20, b16, c05, c06)
- [V] Loula et al. (2025) Syntactic and semantic control of large language models via sequential Monte Carlo. https://arxiv.org/abs/2504.13139 (b17-b19, c07-c09, d05, d06)
- [V] Li, Fox, Goodman (2024) Automated statistical model discovery with language models (BoxLM). https://arxiv.org/abs/2402.17879 (a23, a24, c21, c22, d07)
- [V] RefineStat (Kanda, Ugare, Misailovic; listed as Ghosh et al. in d08, ICLR 2026) https://arxiv.org/abs/2509.01082 (c23, c24, d08). Author list differs between lines; check before citing.
- [V] Domke (2025) Large Language Bayes. https://arxiv.org/abs/2504.14025 (d09). c26 is a secondary summary ([M]) at https://arxivlens.com/PaperView/Details/large-language-bayes-8423-95f9efbb; do not use its 71.9% figure.
- [V] Huang (2025) LLM-BI. https://arxiv.org/pdf/2508.08300 (c25)
- [V] Nafar, Venable, Kordjamshidi (2024) Reasoning over uncertain text by generative large language models (BLInD). https://arxiv.org/abs/2402.09614 (d10, d11). c28 is a secondary listing ([M]).
- [V] Pournemat et al. (2025) Reasoning under uncertainty: probabilistic reasoning of LLMs. https://arxiv.org/abs/2509.10739 (d21)
- [M] AI4BayesCode (2026), search listing only. https://arxiv.org/html/2605.18476 (c27)
