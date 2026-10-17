# Selection and verification among candidate programs

Date: 2026-10-16. Plain notes. Short sentences.

Tags: [V] = checked on the arXiv abstract page this session. [M] = from memory, not checked. [S] = from a web search snippet only.
Caveat: WebFetch gave me abstracts only. Per-dataset tables were not read. Numbers marked [M] may be off.

## Our two failure modes
A. Several candidates pass all visible checks but disagree. Which one is right?
B. A popular wrong answer outvotes a correct minority. Also, we waste samples when early attempts already agree.

## 1. Adaptive sampling / early stopping

| Idea | Evidence | Effect | Source | Status |
|---|---|---|---|---|
| Adaptive-Consistency (Aggarwal et al. 2023) | 17 reasoning and code datasets, 3 LLMs. Stop sampling when a lightweight agreement criterion says the leader is safe. | Up to 7.9x fewer samples. Average accuracy drop under 0.1%. | https://arxiv.org/abs/2305.11860 | V |
| Early-Stopping Self-Consistency (ESC) | Sample in small windows. Stop when a window is unanimous. | Fewer CoT samples: GSM8K -80.1%, CommonsenseQA -78.5%, StrategyQA -76.8%, Coin Flip -84.2%, Last Letters -67.4%, MATH -33.8%. Accuracy "comparable". | https://arxiv.org/abs/2401.10480 | V |
| CISC (confidence-weighted vote) | 9 models, 4 datasets. Weighted vote using the model's own confidence per path. | Over 40% fewer paths on average. Beats plain SC in nearly all settings. The best-calibrated confidence method was the least useful. | https://arxiv.org/abs/2502.06233 | V |

Notes:
- Savings are largest on easy items, smallest on hard items (MATH only -33.8%). That is the right behaviour: stop early where agreement is real.
- Early stopping does nothing for failure B (correlated wrong consensus). It only saves tokens. A wrong unanimous window stops cheaply and wrongly.
- Code angle: agreement should be counted over behaviour on inputs, not over source text.

## 2. Choosing among candidates that pass visible tests

| Idea | Evidence | Effect | Source | Status |
|---|---|---|---|---|
| CodeT | Same LLM writes tests. Dual execution agreement: programs that agree with each other and pass many generated tests score high. 5 models, 4 benchmarks. | HumanEval pass@1 65.8%, +18.8 absolute over code-davinci-002. | https://arxiv.org/abs/2207.10397 | V |
| MBR-exec (Shi et al.) | Run candidates on inputs. Group by identical outputs. Pick by minimum Bayes risk (most agreed-with behaviour). | Beats all execution-unaware selection. No numbers on abstract page. | https://arxiv.org/abs/2204.11454 | V (no numbers) |
| AlphaCode filtering and clustering | Huge sampling, filter on example tests, then cluster by behaviour on generated inputs, submit from the largest clusters. | Top 54.3% on Codeforces. Clustering detail is from the paper body. | https://arxiv.org/abs/2203.07814 | V for ranking; clustering M |
| Coder-Reviewer reranking | Score = p(code given spec) x p(spec given code). Fixes bias toward degenerate programs. | Up to +17% absolute over coder-only reranking. 6 datasets, 8 models. With executability filter it often beats MBR. | https://arxiv.org/abs/2211.16490 | V |
| LEVER | Train a verifier on (spec, program, execution result). Combine with LM probability. Marginalise programs with same outputs. | +4.6% to +10.9% over code-davinci-002 on 4 datasets. | https://arxiv.org/abs/2302.08468 | V |
| TiCoder (interactive test-driven) | Generate discriminating tests. A user accepts or rejects outputs. Prune and rank code. | MBPP pass@1 +22.5 to +37.7 absolute. HumanEval +24.8 to +54.0 absolute. 1 to 5 user queries. | https://arxiv.org/abs/2208.05950 | V |

Which works best and why (my reading):
- Behaviour clustering (MBR-exec, CodeT, AlphaCode) beats text-level or likelihood selection. Programs that differ in text but agree on outputs are the same hypothesis. Count hypotheses, not strings.
- Visible tests are weak when several programs pass them. Extra discriminating inputs split the tie. CodeT and AlphaCode generate extra inputs for this reason.
- CodeT weakness: tests come from the same model. If the model has a systematic misconception, its tests encode it. Agreement then rewards the shared error. This is failure B again. [M]
- TiCoder's large gains need an oracle (user answers). Without one it reduces to CodeT-like self-agreement. Do not expect those numbers.
- LEVER needs a trained verifier and training data. Costly for us. Low priority.

## 3. Correlated errors and beating majority vote

| Idea | Evidence | Effect | Source | Status |
|---|---|---|---|---|
| Plain majority vote plateaus | Large Language Monkeys: coverage (any sample correct) rises log-linearly with samples, e.g. SWE-bench Lite 15.9% at 1 sample to 56% at 250. Majority vote and reward models "plateau beyond several hundred samples". | Selection, not sampling, is the bottleneck. | https://arxiv.org/abs/2407.21787 | V |
| Universal Self-Consistency (USC) | Model reads all candidates, picks the most consistent. | Matches SC on math. Matches execution-based voting on code without execution. Abstract has no numbers. It still picks the "most consistent", so it tends to follow the majority. | https://arxiv.org/abs/2311.17311 | V (no numbers) |
| Weighted vote by confidence (CISC) | See section 1. | Over 40% fewer paths. | https://arxiv.org/abs/2502.06233 | V |
| Learned aggregator (AggLM) | RL-trained model reads candidates and synthesises. Training mix balances easy and hard items so it learns to rescue minority-correct answers. | Beats rule-based and reward-model baselines. Fewer tokens than voting with more samples. No numbers on abstract page. | https://arxiv.org/abs/2509.06870 | V (no numbers) |
| Surprisingly popular (SP) | Origin: Prelec et al., Nature 2017. Ask for the answer AND the predicted crowd distribution. Pick the answer more common than predicted. LLM versions: Inverse Surprising Popularity (arXiv 2510.01499, ICML 2026 poster); Machine Truth Serum (arXiv 1909.13004, classification). | Targets exactly the case where the majority is wrong. Numbers not checked. | https://arxiv.org/pdf/1909.13004 ; https://icml.cc/virtual/2026/poster/63160 | S for LLM versions; Prelec M |
| Echo-chamber warning | Shared errors mean N agents give far fewer than N independent signals. | Explains why more samples do not fix correlated errors. | https://arxiv.org/pdf/2602.09341 | S |
| Knockout / league pairwise selection | Proves failure probability falls exponentially with compute if the model can sometimes produce a correct solution and beats chance at picking correct over wrong in pairs. Needs no answer grouping. | Theory. Experiments not read. | https://arxiv.org/abs/2411.19477 | V (abstract) |
| Pairwise RM knockout | Pairwise comparison and elimination. | Gains concentrated on hard problems: 40 to 60% relative on the hardest 50%. | https://arxiv.org/pdf/2501.13007 | S |

Practical reading for us:
- Cheap SP-style trick: after clustering by behaviour, ask the model "what fraction of attempts would give this answer?" for each cluster. Clusters rarer than predicted that still pass all checks are rescue candidates. Not validated for code. [my idea]
- Any minority rescue needs a signal independent of the vote. Execution on new inputs is independent. Model opinion is only partly independent.

## 4. LLM-as-judge for rival solutions

| Idea | Evidence | Effect | Source | Status |
|---|---|---|---|---|
| Intrinsic self-correction fails | Huang et al. 2023. Without external feedback, models fail to correct reasoning and sometimes get worse. | Negative. Earlier positive results leaned on oracle labels (this point M). | https://arxiv.org/abs/2310.01798 | V (abstract) |
| Self-preference | GPT-4 and Llama 2 recognise their own outputs. Recognition correlates linearly with preference, apparently causal. | A judge from the same model favours the model's own style. | https://arxiv.org/abs/2404.13076 | V |
| Multiagent debate | Several instances debate over rounds. Reported gains on math and strategic reasoning. | Abstract gives no numbers. Later work (not checked) found debate often no better than self-consistency at equal compute. | https://arxiv.org/abs/2305.14325 | V; critique M |
| Pairwise comparison with guarantee | See knockout and league above. | Works if pairwise accuracy beats chance and a correct candidate exists. | https://arxiv.org/abs/2411.19477 | V |
| Claim: a critic seeing all candidates can pick the minority answer | Argument in a 2026 preprint, not a controlled test. | Unproven. | https://arxiv.org/pdf/2605.13695 | S |

Does "derive each candidate and compare" beat voting? I found no clean primary result saying yes in general. What the evidence supports:
- Judging without new information is weak and biased (Huang, self-preference).
- Judging works better when anchored to something checkable: a concrete discriminating input where rivals give different outputs, plus the task spec. Then the model only decides which output is right for one input. That is much easier than "which program is better".
- Pairwise beats scoring one candidate alone, and has theory behind it (2411.19477). But its premise (judge beats chance) is exactly what correlated error threatens.
- Have the judge compute the expected output from the spec BEFORE seeing the candidates' outputs. This reduces anchoring. [my suggestion]

## 5. Discriminating inputs for rival programs

| Idea | Evidence | Effect | Source | Status |
|---|---|---|---|---|
| TiCoder | See section 2. Tests that split candidates; an oracle labels them. | Large gains with 1 to 5 queries. | https://arxiv.org/abs/2208.05950 | V |
| CodeT, AlphaCode | Generate extra inputs, compare candidate outputs. | See section 2. | links above | V |
| Distinguishing inputs / oracle-guided synthesis (Jha et al., ICSE 2010; Ellis and Gulwani 2017 on string-transform disambiguation) | Pick an input where two consistent programs differ, ask the oracle, prune. About log(candidates) queries if each query halves the set. | Classical result. Not re-checked. | no URL fetched | M |
| Hypothesis Search (Wang et al.) on ARC | LLM proposes natural-language hypotheses, implements as Python, checks on examples. | ARC 100-problem subset: direct 17%, automated pipeline 30%, human-picked hypotheses 33%. Human selection added only 3 points. | https://arxiv.org/abs/2309.05660 | V |

Practical reading:
- Cheapest step: run all passing candidates on the given inputs plus a few mutated or generated inputs. Keep only inputs where candidates disagree.
- Who labels a disagreeing input? We have no oracle. Options: the model derives the expected output from the rule in plain words (weak, see section 4), or check invariants (output size, colour set, symmetry) that any correct rule must satisfy. [my idea]

## 6. Consilience / explanatory coverage

I found no primary paper that tests "the rule explains every observed detail, no leftovers" as a selection criterion for LLM hypotheses against votes.
Nearest evidence:
- Hypothesis Search: checking hypotheses against all examples helps, but it only uses pass/fail.
- Coder-Reviewer (section 2) is the closest formal analogue. It asks "how well does this program explain the spec?" via p(spec given code). Up to +17% over coder-only. [V]
- Bayesian program induction (DreamCoder and similar) prefers short programs that fit all data. [M]
Verdict: plausible, cheap, no direct evidence. Use as a tie-breaker, not a main selector. Operational version: for each surviving candidate, check that all changed cells are accounted for by the rule and no cells are left unexplained. Penalise rules with special-case patches.

## 7. Execution-feedback revision

| Idea | Evidence | Effect | Source | Status |
|---|---|---|---|---|
| Self-Debug | Few-shot, uses execution results and self-explanation. Spider, TransCoder, MBPP. | Up to +12% with unit tests. +2-3% on Spider with explanation only. Can match baselines that sample more than 10x as many programs. Round count not on abstract page (I recall most gain in the first one or two rounds). | https://arxiv.org/abs/2304.05128 | V; rounds M |
| Is self-repair a silver bullet? (Olausson et al., ICLR 2024) | Code Llama, GPT-3.5, GPT-4 on HumanEval and APPS. Compares repair against i.i.d. resampling at equal budget. | Gains "often modest", sometimes absent. Limited by the model's own feedback quality. Stronger feedback model gives much larger gains. Per search snippet: i.i.d. sampling sometimes equal or better, especially at small budgets; GPT-4 on APPS up to about +8%; 10 initial + 1 repair each gave about 1.05x pass@20. Spending on diverse initial samples beats extended repair. | https://arxiv.org/abs/2306.09896 | V (abstract); detail S |
| Reflexion | Verbal self-reflection across trials using execution feedback. HumanEval pass@1 about 91% reported with GPT-4. | Not re-checked. | arXiv 2303.11366 | M |
| Intrinsic self-correction | See section 4. | Without an external signal, revision can hurt. | https://arxiv.org/abs/2310.01798 | V |

Practical reading:
- Revision pays when feedback is concrete (a failing input with expected and actual output). It does not pay when the model only re-reads its own code.
- At equal tokens, fresh samples are about as good as repair for weak models. Repair helps most on hard items and with a stronger critic.
- One or two rounds capture most of the benefit. [M]
- A repair that passes the visible examples is no more trustworthy than a fresh program that passes. Cluster it like the rest.

## Ranked: what most likely fixes our failure modes at low token cost

1. Cluster by behaviour, not text, and vote over clusters (MBR-exec, AlphaCode, CodeT). Near-zero extra model tokens. Fixes the agreement accounting for both modes. Strong evidence.
2. Adaptive stopping on cluster agreement (Adaptive-Consistency, ESC). Up to 7.9x fewer samples at under 0.1% loss on reported datasets. Targets token waste. Use a stricter threshold than usual, since correlated wrong consensus stops cheaply and wrongly. Escalate to 3-5 only when clusters split.
3. Discriminating-input step for ties: when two or more clusters pass all visible checks, find an input where they disagree and decide which output is right. One or two short calls per tie. Best evidence for mode A (TiCoder, CodeT, classical synthesis). Weak point: needs a labeller. Use independent derivation of the expected output plus invariant checks.
4. Pairwise (not whole-set) judging anchored to that input, judge derives expected output before seeing candidates. Theory supports pairwise (2411.19477). Mitigates self-preference. Limit to the top two or three clusters.
5. Coder-Reviewer style tie-break: p(task description given program), or its operational cousin, explanatory coverage. Up to +17% over coder-only in the paper. Cheap. Tie-breaker only.
6. Minority rescue: SP-style check on clusters, or an aggregator prompt told to look for minority-but-consistent clusters. Mostly unvalidated for code. Try only if 3-5 do not recover enough.
7. Targeted repair from a concrete failing input, 1-2 rounds, only for items with no passing candidate. Equal-budget evidence says do not prefer it over fresh samples elsewhere.
8. Skip for now: LEVER (needs trained verifier), debate (cost, weak evidence), unanchored LLM-judge or self-correction (documented to fail), confidence-weighted voting (about 40% saving; useful only if cheap within-question confidences exist).

Gaps: no per-table numbers read for MBR-exec, USC, AggLM, debate. No direct evidence for consilience. Surprisingly-popular for code is unproven.
