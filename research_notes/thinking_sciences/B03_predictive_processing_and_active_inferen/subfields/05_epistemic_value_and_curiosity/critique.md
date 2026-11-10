# Critique and cross-check: B03.05 Epistemic value and curiosity

## Corrections made (sources re-opened this session)
Opened again: Krishnamurthy 2024 (arXiv 2403.15371), EVOLvE (2410.06238), Binz & Schulz (2206.14576), UoT (2402.03271), Voyager (2305.16291), Sajid 2021 (1909.10863), Mazzaccara 2024 (2406.17453).
Confirmed unchanged: Sajid FrozenLake numbers (99.88, 99.76, 97.79 deterministic; 98.90 vs 64.39 and 66.08 stochastic; null model 50.03/50.22; no-reward 0.00 / 39.94 / 44.00); Mazzaccara INLG 56.7 to 68.9, Things 51.1 to 61.1, FT 46.6 and 42.2, questions 7.1 to 5.2; Binz regret 2.72 vs 3.24, t(38878)=-5.03, horizon beta=-0.15, p=.58; UoT table cells (20Q-Things 15.0 to 25.0, DX 83.7 to 90.4, MedDG 60.2 to 64.3, FloDial 28.8 to 47.1, troubleshooting 43.7 to 67.3); Voyager 3.3x, 2.3x, 15.3x/8.5x/6.4x, -93% with random curriculum; EVOLvE Table 1 and OptFrac (UCB 32.7 to 65.0, Flash 9.3 to 10.7).
Corrections and clarifications:
1. Krishnamurthy: b08 says the >60% suffix failure is at T=500, c01 says T=100. Both partly right. The >60% figure is from Figure 1 (T=500, N=20); the main experiments use T=100, K=5, gap 0.2. Only 3 of the 72 GPT-4 configs avoid suffix failure; 2 of those (BNRND, BSSCD) fail the other way (uniform-like). So "one success out of 72" is right for GPT-4, but c02's "1 out of all tested configurations" is also right across models. Also the paper says T=500 gave "consistent/stronger conclusions".
2. EVOLvE Table 2 is garbled in extracted text. The prose says few-shot demos with summarised history reach 50.2 (Flash) vs 27.5 raw, and fine-tuning prefers raw (65.6) over summarised (28.3). c04 labels the 50.2 as "algorithm-guided"; b11 labels the same 50.2 as algorithm-guided too. The prose says summarised history. Treat 50.2 as summarised-history demos. Also the table shows few-shot Pro contextual bandit guided at 25.0, lower than Flash 60.7 (not recorded in c-notes).
3. EVOLvE arXiv id 2410.06238 (an agent first tried 2412.06438, which is a different paper). Use the right id in the source list.
4. UoT 38.1%: the abstract says "average performance improvement of 38.1% in the rate of successful task completion" across 5 datasets and 5 LLMs vs direct prompting. It is not stated whether this is relative or absolute points; the table cells suggest it is relative. Use "38.1% average improvement" and do not call it percentage points.
5. Binz & Schulz: in long-horizon tasks GPT-3's regret was significantly lower than humans (t(5550)=-4.07), but humans improved more within a task. "Matched humans at short horizon" is correct.
6. Sajid stochastic Q-learning is 66.08 [63.28, 68.88] (b04 said about 65-66, fine).

## Not re-opened (carry risk)
Wilson 2014 (N=30, t(29)=5.05), Mirza 2018 (log evidence 888), Itti & Baldi, Hafner, Tschantz 2020, Grand 2024 (1.27 bits), Hong 2024 (196 prompts), ELLM 64.9%, PUMA numbers, Champion 2023. Rely on earlier agents' notes.

## Seen only in snippets or abstracts (not opened)
Friston 2015 (a06, b27, c19), Friston 2017 curiosity and insight (a07, b28), Itti & Baldi, Sun 2011, Kakade & Dayan, Zajkowski 2017, Gershman 2018, Sadeghiyeh 2020, Somerville 2017, Wilson 2021 review, F-Explorer (c20), safer-AGI framework (c21). Claims resting on these are marked single-source or are borne by opened papers.

## Contradictions between sources
- Millidge 2021 (epistemic term is added, not derived) vs Sajid 2021 / Da Costa 2023 (directed exploration emerges from EFE). Both are right at different levels: it emerges once you accept EFE, but EFE is a choice.
- Tschantz 2020 (epistemic agent solves sparse Mountain Car in one trial) vs Champion 2023 (epistemic variant fails dSprites) vs Tschantz Cup Catch (no benefit). The benefit depends on whether random actions find reward.
- Wilson 2014 (two separate mechanisms) vs Gershman 2018 (hybrid fits best) vs Schwartenbeck 2019 (random exploration only when directed fails).
- Meta-ICL (Coda-Forno): more tasks gave more greed, not more curiosity; Krishnamurthy says prompt alone leaves greedy-like behaviour. Consistent: LLM exploration is weak, and "learning" in context mostly sharpens exploitation.

## Weak spots
- Almost all active-inference evidence is simulation in toy tasks by the originating lab (T-maze, FrozenLake, dSprites). Human data: one eye-movement test (Mirza) with unrecorded N, hand-added heuristics.
- All LLM bandit studies are stateless bandits on GPT-3/3.5/4 or Gemini 1.5 era models. No test on current reasoning models, none with scaffolds like tree search.
- Information-gain question selection (UoT, DPO, LIPS) needs closed hypothesis sets and countable answers; the EIG is computed by code, not by the model. This is not the same as the model "being curious".
- No study isolates the active-inference switch (epistemic to pragmatic) in an LLM at equal tokens (c26). PUMA and Prakki change many parts at once.
- Voyager is 3 runs per method; OMNI/ELLM use an LLM as the interest judge (circular).
- Search tools were rate limited, so forward citation tracking was thin.

## GAPS
1. Does an explicit stop rule (stop open-mode probing when the best probe's estimated information gain is below a threshold) beat a fixed exploration budget at equal tokens, on tasks with open hypothesis spaces?
2. Do current reasoning models (2025-2026) still show suffix failure and horizon-blindness on bandit-style probe tasks, with and without a coded tally?
3. How should expected information gain be estimated when the hypothesis set is open or soft (overlapping answers)? Which approximation (sampled hypotheses, LLM-estimated partition) keeps the UoT gain?
4. Does an LLM interest/relevance filter on probes beat raw novelty at equal tokens, and does it avoid the noisy-TV trap on unlearnable distractors?
5. Does telling the agent its remaining budget (horizon) change its exploration the way it changes humans, and does the effect survive in newer models?
6. What is the effect of the epistemic term alone (lambda_e = 0 vs positive) inside an LLM expected-free-energy loop, with equal compute and a score on a reasoning benchmark?
7. How does the exploration benefit scale with model size (Gemma 2B/9B gained nothing from guidance)? Is there a size below which the S3 scaffold should be skipped?
8. Do lookahead (sophisticated) probe scores beat one-step probe scores enough to pay for their extra tokens?
9. What did Friston 2015 and 2017 (curiosity and insight) actually claim and test? Open full texts to replace snippet-based claims.
10. Which human studies beyond Wilson 2014 (N=30) replicate directed exploration, with what effect sizes, and are there failed replications?

## Gap search results (evidence_d.jsonl, d01-d17; claims K21-K27 added, K02/K07/K08/K09/K12/K19 updated)

Search note: the WebSearch budget ran out after two calls and the Semantic Scholar and OpenAlex APIs rate-limited, so forward citation tracking stayed thin. All 17 evidence lines were read as full text (PDF or HTML).

1. Stop rule versus fixed budget. PARTLY CLOSED. Two answer-sampling studies show a stop rule wins: Adaptive-Consistency (d09, up to 7.9x fewer samples, under 0.1% accuracy drop, and better accuracy than uniform sampling at equal average cost) and answer-convergence stopping (d10, over 40% fewer tokens on NQ, unstable on MATH-500 and GPQA). Piriyakulkij (d15) shows the gain per question falling to near zero as a closed set empties. Still open: nobody tested stopping on information gain of open-ended probes. Kobalczyk (d11) lists "when to stop asking" as an unsolved limit.
2. Current reasoning models on bandit tasks. PARTLY CLOSED. o3-mini, Gemini-2.5-flash, R1, o1-mini and Gemini 3.1 Flash Lite explore more than older models, but directed exploration stays weak in non-stationary 4-armed tasks (d02), reasoning models do not remove the gap to explicit exploration (d03), and labels still bias them (d14). Still open: no suffix-failure rate with and without a coded tally on a 2025-26 reasoning model.
3. Expected information gain with open or overlapping answers. MOSTLY CLOSED. Sample about 20 hypotheses from the LLM, filter them against the evidence, weight equally, compute the gain in code (d11). LLM log-probability weights were clearly worse (d11). Posterior sampling by the LLM works in small spaces and costs more tokens (d03). Not tested: LLM-estimated partitions against sampled hypotheses head to head, and overlapping answers.
4. Interest filter versus raw novelty. STILL OPEN. OMNI (d12) beats learning progress alone and uniform sampling, but no unlearnable-distractor test and no equal-token comparison against raw novelty was found. Prediction-error curiosity (d17) is weak evidence.
5. Telling the agent its remaining budget. STILL OPEN for LLMs. People: the information bonus rises with the horizon (d07, N=31, TMS cuts it). Nothing new tests it on 2025-26 LLMs; Binz and Schulz stays the only LLM horizon test (GPT-3, no horizon effect).
6. Epistemic term alone in an LLM expected-free-energy loop. STILL OPEN. No study found that sets the weight to 0 versus positive at equal compute on a reasoning benchmark. arXiv search for "active inference" plus LLM was rate limited on the second try.
7. Scale. PARTLY CLOSED. Size swaps frequency bias for greed (d01: 2B repeats 96%, 27B 14% but greedy); in a pilot, 8B models explored too little while Qwen3-14B matched 32B (d14). Guidance is not useless for small models: a forced try-all sweep helped across Gemma2 sizes (d01). K09 is now "contested". A clean size floor for skipping S3 is not measured.
8. Lookahead versus one-step scores. STILL OPEN. LLM-IDS was myopic and still beat sampling-based exploration where one probe reveals the answer (d03). No head-to-head of lookahead against one-step scores at equal tokens.
9. What Friston 2015 and 2017 claimed. CLOSED. Both opened. 2015: expected free energy splits into extrinsic and epistemic value; 128-trial T-maze simulations in four schemes; expected utility falls below chance when utility is zero; an ambiguity term guards against noisy outcomes (d05). 2017: rule learning with 32 trials and 64 simulated agents, chance about 30%, nearly all reach 100% around trial 10 once Bayesian model reduction is added; no human test (d06). Both are simulation only (K26).
10. Human studies beyond Wilson 2014. PARTLY CLOSED. Zajkowski 2017 (d07): N=31, same lab, horizon information bonus cut by TMS; Gershman 2018 (N=45) and Chakroun 2020 (N=31) re-fitted in d02. No failed replication of the Horizon task found. Independent-lab effect sizes were not read (K27 stays single-source). The 2025 tDCS null (d08, N=43) used a different task.

Corrections carried into claims: K07 (suffix-failure figure is T=500; main runs T=100), K08 (50.2 is summarised-history), K12 (38.1% relative or points not stated), K09 (now contested).

Design consequences for S3: (a) code does the tally, the forced first sweep, the gain estimate and the stop test; the LLM proposes probes and hypotheses; (b) hypotheses are sampled and filtered, equal weights; (c) the stop test is a threshold on the leading hypothesis or best-probe gain plus a minimum probe count, tested against a fixed budget at equal tokens; (d) neutral probe labels.
