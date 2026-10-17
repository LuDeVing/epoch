# 03 Generality: what makes automated research systems transfer

Date: 2026-10-17. Question: does HTSA's profile-driven mapper and verifier only look general?

How to read "Verified". "page" means I fetched the URL and the number was on it. "abstract" means only the arXiv abstract was read. "memory" means I did not check it this session and it may be wrong. "search" means a third-party search summary.

## Short answer

Every system that transfers well does the same thing. It asks the user for a runnable scorer and a small editable artifact. It does not ask the model to understand the domain from scratch. Where no scorer exists, results fall sharply.

Nobody I found has a clean test of "model plans from only a problem statement and a scorer, versus a hand-written plan". That gap is real, and HTSA's first real run can fill part of it.

## Table

| System | Problem interface | Problem types shown | Numbers | Source | Verified |
|---|---|---|---|---|---|
| FunSearch (2023) | Code: an evaluate function plus a seed program or skeleton. The LLM fills in one function. | Cap set, online bin packing (Shannon capacity from memory). | Largest cap set gain in 20 years (page). Cap set n=8 size 512 (memory). | https://deepmind.google/discover/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/ | page (blog); 512 memory |
| AlphaEvolve (2025) | User writes evaluate() returning a dict of scalar scores. Code to change sits between EVOLVE-BLOCK markers. A cascade of tests, cheap first, filters bad candidates. | Over 50 open math problems, Gemini matmul kernel tiling, data-centre scheduling, TPU circuit, 4x4 complex matmul in 48 multiplications. | Matched best known on about 75%, beat it on about 20%. Kissing number in 11 dims 592 to 593. Kernel 23% faster, about 1% of Gemini training time. | https://arxiv.org/abs/2506.13131 , https://arxiv.org/html/2506.13131 | page |
| AlphaEvolve limit | Needs an automated evaluator. Natural-science problems that can only be partly simulated are a harder fit. | Stated by the authors. | none | same | page |
| OpenEvolve | Open-source copy. Evaluator file plus config (timeout, retries, feature dimensions). | Circle packing n=26 as the main replication. | 2.6343 at 460 rounds vs AlphaEvolve 2.6359. A rival tool got 2.636 in 63 evaluations; OpenEvolve got 2.6307 at 200. Evaluator tolerance 1e-6 vs zero changes scores. | https://pypi.org/p/openevolve , https://arxiv.org/pdf/2605.19633 , https://arxiv.org/pdf/2511.23473 | search (third-party) |
| ShinkaEvolve (2025) | Same evaluator-plus-code pattern. | Circle packing, AIME agent harnesses, ALE-Bench programming, MoE load-balancing loss. | New best circle packing with 150 samples. | https://arxiv.org/abs/2509.19349 | abstract |
| LLM-SR (2024) | Equation as a program skeleton. The LLM writes the form, a fitter sets constants on data. | 4 benchmark problems in physics and biology. | Beats symbolic-regression baselines, mostly out of domain. | https://arxiv.org/abs/2404.18400 | abstract |
| Eureka (2023) | No template. The LLM writes a reward function from the environment source. An RL run scores it. | 29 RL environments, 10 robot types. | Beats human rewards on 83%; mean 52% normalised gain. | https://arxiv.org/abs/2310.12931 | abstract |
| ELM (2022) | LLM as mutation operator over programs; MAP-Elites keeps diverse ones. | One domain: Sodarace walkers. | Hundreds of thousands of working programs. | https://arxiv.org/abs/2206.08896 | abstract |
| MLE-bench (2024) | 75 Kaggle competitions. Agent gets description and data, graded on the real metric against the leaderboard. | ML engineering across many Kaggle task types. | Best: o1-preview with AIDE, bronze or better in 16.9%. | https://arxiv.org/abs/2410.07095 | abstract |
| AIDE (2025) | Tree search over whole solutions. Draft, debug, improve. Scorer is the validation metric. | Kaggle, MLE-bench, RE-Bench. | "State of the art" claimed; no figures on page. | https://arxiv.org/abs/2502.13138 | abstract |
| MLAgentBench (2023) | 13 tasks, each a starter folder plus a goal. | CIFAR-10 up to BabyLM and recent Kaggle. | Best (Claude 3 Opus) 37.5% average. 100% on old datasets, 0% on recent Kaggle. | https://arxiv.org/abs/2310.03302 | abstract |
| DSBench (2024) | Data analysis and data modeling tasks. | 466 analysis tasks, 74 modeling tasks. | Best agent solves 34.12% of analysis tasks. | https://arxiv.org/abs/2409.07703 | abstract |
| ScienceAgentBench (2024) | Task plus data; agent writes a program. | 102 tasks from 44 papers, 4 disciplines. | 32.4% alone, 34.3% with expert knowledge, 42.2% for o1-preview with self-debug at over 10x cost. | https://arxiv.org/abs/2410.05080 | abstract |
| DiscoveryBench (2024) | Dataset plus a natural-language question. | 264 tasks, 6 domains. | Best about 25%. | https://arxiv.org/abs/2407.01725 | abstract |
| Self-Discover (2024) | Model picks and composes reasoning modules per task, writes a structure, then follows it. | BigBench-Hard, agent reasoning, MATH. | Up to 32% over chain of thought. 10 to 40x fewer calls than self-consistency. Structures moved across model families. | https://arxiv.org/abs/2402.03620 | abstract |
| Least-to-most (2022) | Few-shot examples of splitting into sub-questions. | SCAN and maths. | 99%+ on SCAN with 14 exemplars; chain of thought 16%. | https://arxiv.org/abs/2205.10625 | abstract |
| Decomposed prompting (2022) | Library of sub-task handlers: prompts, trained models or code. | Symbolic reasoning, multi-hop QA. | none on page | https://arxiv.org/abs/2210.02406 | abstract |
| Plan-and-Solve (2023) | Zero-shot "make a plan, then do it". | 10 datasets, 3 reasoning types. | Beats zero-shot chain of thought on all 10. Fixes missing-step errors. | https://arxiv.org/abs/2305.04091 | abstract |
| ADaPT (2023) | Try the step; split only if the executor fails. | ALFWorld, WebShop, TextCraft. | Up to +28.3%, +27%, +33% over baselines. | https://arxiv.org/abs/2311.05772 | abstract |
| Tree of Thoughts (2023) | Per-task prompts to propose and rate thoughts. | Game of 24, creative writing, crosswords. | Game of 24 4% to 74%. | https://arxiv.org/abs/2305.10601 | memory (abstract has no numbers) |
| Optuna | Python objective taking a trial. Search space declared inside it (define-by-run). Direction, trial count, timeout set at study level. | Any black-box objective. | Docs advise few parameters since trials grow exponentially. | https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/002_configurations.html | page (objective, space); rest memory |
| Ax / BoTorch | Search space, objectives, parameter constraints, outcome constraints, noise. | Any, incl. A/B tests, mixed spaces. | Starts with quasi-random (Sobol) points, then a GP. | https://ax.dev/docs/why-ax/ | page (inputs); Sobol memory |
| AI Scientist v1 (2024) | One hand-written code template per domain. | 3 templates: NanoGPT, 2D diffusion, grokking. | About $10-15 per paper. Reviewer balanced accuracy 0.65 vs human 0.66. Best mean score 3.82. | https://arxiv.org/abs/2408.06292 | page |
| AI Scientist v1 failures | Aider failed to implement many ideas. Results overstated or invented. Too few experiments. Once evaded its time limit by relaunching itself. | | | same | page |
| AI Scientist v2 (2025) | Drops human code templates. Tree search over experiments. | ML workshop papers. | One of three submissions above the average human acceptance threshold at an ICLR workshop. | https://arxiv.org/abs/2504.08066 | abstract |
| Agent Laboratory (2025) | Three stages (literature, experiments, report); human feedback allowed at each. | ML research tasks. | 84% lower cost than earlier autonomous methods. Feedback raises quality. | https://arxiv.org/abs/2501.04227 | abstract |
| AI co-scientist (2025) | Natural-language research goal. Generate, reflect, rank in a tournament, evolve. | Drug repurposing, new targets, antimicrobial resistance mechanism. | Leukaemia repurposing candidates confirmed in vitro. Elo not on abstract. | https://arxiv.org/abs/2502.18864 | abstract; Elo memory |
| Virtual Lab (Nature 2025) | LLM PI agent plus specialist agents; human sets the agenda. | SARS-CoV-2 nanobody design. | Not read (paywall redirect). | https://www.nature.com/articles/s41586-025-09442-9 | not verified |
| AblationBench | Plan ablations from a method section. | AI papers. | Best system finds 45% of original ablations; chain of thought beat the agent. | https://icml.cc/virtual/2026/73481 | search |
| LLM warm-start for BO (LLAMBO and reproduction) | LLM proposes initial points from a text description. | Tabular hyperparameter tuning. | Beats random, Sobol, Latin hypercube starts; independent Llama 3.1 70B reproduction agrees. | https://arxiv.org/pdf/2402.03921 , https://arxiv.org/pdf/2511.18891 | search |

## What the evidence says

1. The scorer is the transfer mechanism. FunSearch, AlphaEvolve, OpenEvolve, ShinkaEvolve, LLM-SR and Eureka run on very different problems. They share one interface: a function that returns a number, plus an artifact the model may edit. The model never needs the whole domain.
2. Breadth is narrower than it looks. ELM is one domain. AI Scientist v1 is three hand-built templates in one field. LLM-SR is four problems. Only AlphaEvolve (50+ problems) and Eureka (29 environments) show real spread, and both had a fast, trusted scorer.
3. Cheap staged evaluation matters. AlphaEvolve's cascade drops bad candidates early. The OpenEvolve comparison shows scorer details alone (1e-6 tolerance vs zero) change headline numbers. A loose scorer lets search exploit the scorer.
4. Without a scorer, results drop. DiscoveryBench (about 25%), DSBench (about 34%), ScienceAgentBench (32-42%) and MLE-bench (16.9% medal) are all low. MLAgentBench ranges from 100% on old datasets to 0% on new Kaggle ones, a hint that part of "generality" is memory of known tasks.
5. Model-made task structure helps on reasoning, with weak evidence for research. Self-Discover, Plan-and-Solve and ADaPT report gains from model-made plans, all on short reasoning or game tasks. The only research-planning test I found (AblationBench) shows 45% recall of human ablations, and plain chain of thought beat an agent. That argues against a heavy mapper.
6. Removing templates is possible but unproven. AI Scientist v2 dropped templates and got one workshop-level pass of three. v1 never ran template-free. Templates were always supplied by humans.
7. Human input pays. Agent Laboratory reports feedback at each stage helps. ScienceAgentBench shows expert knowledge adds about 2 points. Small but consistent.
8. Cold start in optimisers uses cheap generic points. LLM priors add a modest gain: LLAMBO and an independent reproduction beat random and Sobol starts. A separate ablation says that without a prior the optimiser still finds the region, just slower. I found no clean test isolating only the initial-point effect.
9. Gap: no paper I found compares a model's first decomposition against a hand-written one, given only a problem statement and scorer. Treat "the mapper generalises" as untested.

## Minimum problem definition

Five fields cover every system above:
1. Goal as one sentence, with direction (maximise or minimise).
2. Artifact: the exact thing the model may change, with boundaries (a file, a block, a function).
3. Scorer: a command that returns numbers, with a time limit, a cheap smoke stage before the full stage, and a stated tolerance.
4. Constraints: hard limits that make a candidate invalid (a validity check), kept apart from the score.
5. Budget: maximum evaluations or time, and a baseline score to beat.

Optional: seed solution, vocabulary, parts of the problem. These are priors, not requirements.

## Ranked: what HTSA's profile and mapper should copy

1. Make the scorer the only mandatory contract: seed program, stages, timeout, tolerance, validity check, baseline score. (AlphaEvolve, FunSearch.) Reject profiles with no runnable scorer, or label them "no-check" and report them separately.
2. Add a cheap-first evaluation cascade to the profile: smoke test, small instance, full run. Prune before builders run. (AlphaEvolve.)
3. Keep validity apart from score and fix the tolerance in the profile. (OpenEvolve tolerance finding.)
4. Require an edit boundary for the artifact. (EVOLVE-BLOCK, FunSearch skeleton.)
5. Let the mapper start from the profile's parts and grow the tree only when a part fails, as ADaPT does. Do not ask for a full tree upfront. AblationBench suggests a heavy planner may not beat a plain prompt.
6. Seed with generic cheap probes first (baseline, random variation, a few known heuristics), then let ideas follow. This is the cold-start lesson from Ax and LLAMBO.
7. Report scores by problem family, with a baseline, and report no-check problems separately. MLAgentBench's 0% on new tasks warns against averages.
8. Allow human feedback at stage gates. Cheap and consistently positive. (Agent Laboratory, ScienceAgentBench.)
9. Sandbox and time-limit builders. AI Scientist relaunched itself and evaded limits.

## What the first real non-LLM run should check

Pick one problem family unlike the training-script one, with a fast deterministic scorer. Bin packing fits (FunSearch precedent, so a known target exists). Run the same real model and budget in three arms:

- A. Profile only: goal, artifact, scorer; no parts, no vocabulary.
- B. Full profile with parts and vocabulary.
- C. Plain best-of-N with no mapper, same number of scorer calls.

Check:
1. Does the first tree from arm A differ from arm B? Count the parts it names and how many the scorer later shows matter. This tests cold-start planning directly.
2. Does arm B beat arm C at equal scorer calls? If not, the mapper adds no value on this problem.
3. How many candidates fail the smoke stage? Does the verifier accept anything a reference checker rejects? Test with planted wrong solutions.
4. Did any prompt, code or vocabulary still name the language-model problem? Grep the prompts actually sent.
5. Spend: scorer calls and tokens per accepted improvement, against the baseline score.
6. Repeat with three seeds; report spread, not one run.

Then repeat on the no-check design problem with a real model. Expect a worse result and report it plainly.

## Caveats

Most rows are abstract-only. Per-task detail inside MLE-bench, AIDE, ScienceAgentBench and AI co-scientist was not read. Virtual Lab and FunSearch's Nature paper were paywalled. Tree of Thoughts and cap set numbers are from memory. Search-summary rows are third-party and unchecked against the papers.
