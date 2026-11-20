# Cross-check: Search theory (C12.10)

## Corrections made (sources re-opened this session, arXiv full text)
Confirmed: Large Language Monkeys (15.9% to 56% at 250 samples, SOTA 43%); Krishnamurthy et al. (suffix failure in more than 60% of GPT-4 basic-prompt replicates); ESC (-33.8, -80.1, -76.8%; ESC beat CoT by 9.84%); Binz and Schulz (M=2.72 vs 3.24, t(38878)=-5.03; short horizon t(5566)=-0.043; long horizon t(5550)=-4.07); Kalayci et al. (15-35% fewer generations, 1,600 profiles, win rate above 54%); Goldstein et al. (6,537 players, 48,336 games, optimal 0.622 / 0.599, about 25% / 75% errors); Pilditch (57.2 to 97.3%, mean 81.1%, mean deviation 0.006).

1. a23 (Snell et al.): the paper says "about 4x less test-time compute" than best-of-N in some settings, not "more than 4x better efficiency" in general. The 14x claim holds on easy and intermediate questions, and on hard ones only "depending on the specific conditions". It is not "wherever the small model has nontrivial success". Claim K09 uses the corrected wording.
2. Binz and Schulz: a19 and c11 are one paper (arXiv 2022, PNAS 2023). Count once.
3. Goldstein et al.: arXiv 2017, Management Science 2019/2020. b11 and c17 are one paper, so K03 has one source.
4. Pilditch (2026) has an internal inconsistency: 198 items is called the full GPQA Diamond set in one place and "2 items failed to load" in the appendix. Efficiency numbers are unaffected. 57.2% is both the lowest pathway gain and a trial-level example.
5. Duplicate lines: b15-b17 = c01-c03 (Zhang and Zhao); b18 = c04 (Kalayci); b19 = c15 (Pilditch); a18 = c09 (Krishnamurthy). Independent sources count papers, not lines.

## Contradictions and tensions
- Humans under-search in one-shot lab tasks (b01-b07) yet learn near-optimal stopping in repeated games (b11). First-game errors go both ways, so "early stopping" is not universal.
- LLMs stop too early in the finite-horizon switch game (b16), yet ESC and the Pandora stopper show early stopping is safe when sampling the same question. The two measure different decisions (phase switch vs. stop between samples).
- Binz and Schulz: GPT-3 beats humans on bandit regret but shows no directed exploration. Krishnamurthy: later models fail to explore. Low short-run regret can hide exploration failure.

## Weak spots
- Classical numbers (Koopman, Gittins, Weitzman, secretary rule, MVT field data) come mostly from Wikipedia and citing papers, not primary text.
- Not opened (known only via citing papers): Brown/Flinn/Schotter 2011, Schotter and Braunstein 1981, Cox and Oaxaca 1989, Rapoport and Tversky 1970, Kahan 1967, Weitzman 1979, Wilson 2014, Wang 2023.
- Zhang and Zhao (2024): could not locate the paper this session; numbers rest on the earlier agents' reading and are NOT re-verified. Kittaka et al. and Marcu and Noussair numbers also not re-verified.
- No LLM study tests the classic reservation-value or Koopman allocation directly. Kalayci et al. is closest, and reward-model scores are a weak proxy for value.
- Stopping savings are reported on tasks with a checker or reward model; no evidence for open-ended tasks.
- Semantic Scholar returned 429 and the arXiv query API returned empty; arXiv PDFs and OpenAlex were used instead.

## GAPS
1. Does a Weitzman or Gittins style index applied to an agent's own tool calls and hypothesis checks beat fixed orders at equal tokens? No direct LLM test found.
2. Does the Kalayci stopping rule hold when there is no reward model and acceptance must come from model confidence?
3. Do Zhang and Zhao's stopping errors replicate on current frontier and reasoning models (2025-2026)?
4. Is the in-context exploration failure (Krishnamurthy) fixed by reasoning models, or only by external summaries?
5. What cheap signal gives per-prompt difficulty so adaptive budgets (Snell) work without oracle labels?
6. Does a marginal-value rule for abandoning a reasoning branch beat fixed depth on search-heavy benchmarks?
7. With correlated hypotheses, how much does the independence assumption of the index rule cost in practice?
8. Does memory of past stopping thresholds across tasks (Goldstein-style learning) transfer to an LLM agent?
9. Has any study replicated Stigler or McCall style search with LLM-simulated subjects and measured regret against the optimum?

## Gap search results (evidence_d.jsonl, d01-d16)
Web search budget ran out after 2 calls; the rest came from arXiv PDFs (full text via pdftotext). OpenAlex and the arXiv query API were rate limited or unhelpful.

1. Index on agent tool calls or hypothesis checks: STAYED OPEN for the exact case. Closest: Belloni et al. 2026 (d01) learned Weitzman indices beat a fixed FrugalGPT cascade, but in simulation with API choice only. Cinquin et al. 2025 (d02): a Gittins rule inside PRM tree search gave no gain (70.5-71.4% vs 71.6-71.9%) because the value estimate was poor. New claims K17.
2. Stopping without a reward model: PARTLY CLOSED. Agreement (Adaptive-Consistency, up to 7.9x fewer samples, under 0.1% accuracy loss), confidence weighting (CISC, over 40% fewer paths) and token confidence (DeepConf, 43-79% fewer tokens) all work on single-answer math. Overconfidence breaks DeepConf on some models. Kalayci's own rule still needs a reward model (d14). Open for open-ended tasks. K16.
3. Zhang and Zhao replication on 2025-2026 frontier models: STAYED OPEN. The paper was not located again and no replication was found. Their numbers remain unverified.
4. Reasoning models and exploration failure: PARTLY CLOSED. Harris and Slivkins (v3, 2026) find reasoning models help most but all LLMs lose to linear regression; Arumugam and Griffiths: o1-mini vs GPT-4o changed linear regret to PSRL-level regret in one stochastic task, using an external algorithm. Length-incentivized RL (d05) raises breadth but needs training. Not fixed by reasoning alone. K05 updated.
5. Cheap difficulty signal: PARTLY CLOSED. Hidden-state probes predict difficulty (d10, up to 50% compute saving). Snell's predicted bins lose some gains at high budgets (d11). For API-only agents no verified cheap signal beyond pilot agreement. K09 now established, K20 added.
6. Marginal-value abandon rule vs fixed depth: PARTLY CLOSED. DEER (19.1-80.1% shorter chains, accuracy +0.3 to +5.0%) and DeepConf online support early exit, but baselines are unrestricted reasoning, not fixed-depth truncation at equal tokens. PRM-based abandon rules failed (d02).
7. Cost of the independence assumption: STAYED OPEN empirically. Theory only: no efficient approximation for fully adaptive strategies under correlation, fixed-order adaptive-stop is the constant-factor fallback (d12). K18.
8. Cross-task memory of thresholds: STAYED OPEN. Kalayci learns thresholds within a run only (d14).
9. LLM-simulated Stigler or McCall search: STAYED OPEN. Horton's Homo Silicus (d15) has no search task. K19.

Corrections to earlier notes: the Kalayci rule's acceptance depends on a reward model, so "no reward-model" evidence for stopping comes from other papers (d06-d08). d16 (EVOLvE) was only skimmed; numbers not used.
