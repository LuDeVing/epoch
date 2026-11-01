# Expected information gain models: deep document

*Subfield A14.04. Evidence: evidence_a-d.jsonl (ids a01-d20), claims.jsonl (K01-K32), critique.md. Date 2026-11-01. Search was rate-limited late in the run, so "no paper found" means "not found", not "does not exist". In claims.jsonl the tag "O1" means "the information-query step"; SCHEMA.md has no operator for it yet (its O1 is Specialise). See section 7.*

## 1. What it is

An expected information gain (EIG) model says: when you can pick one action, question or test, pick the one that is expected to cut your uncertainty about the hypotheses the most.

The formula (b04, b11, a05):

- H is the set of hypotheses with prior P(h). a is a possible answer or outcome of test q.
- Uncertainty is Shannon entropy: H[P(h)] = -sum P(h) log P(h).
- EIG(q) = H[P(h)] - sum_a P(a|q) * H[P(h | q, a)]. This is the mutual information between answer and hypothesis.
- Upper bound: log of the number of hypotheses. A yes/no question scores at most 1 bit, reached by an equal split of the hypotheses (b11).
- With a cost c(q): U(q) = EIG(q) - c(q) (b11).

Cook, Goodman and Schulz (2011) wrote it for children as EIG(A) = sum_i P(D_i|A) Ig(D_i, A). The score depends on the prior over hypotheses P(H) and on what each action can show, P(D|A,H) (a01, b04).

Why it matters for our agent. A model told "ask a good question" does this poorly (section 6). If code holds a set of candidate hypotheses and scores each candidate test by EIG, test choice becomes arithmetic. The language model only (1) proposes hypotheses, (2) proposes candidate tests, (3) says what each hypothesis predicts. Code does the rest. This fits guardrail G5 (code selects) and G2/G3 (act on real output).

Competing measures (a05, a11): information gain (Shannon), KL distance, probability gain (expected rise in the chance of guessing right), expected error reduction, "impact". They usually pick the same test and differ only in built cases.

Three kinds of "EIG model" appear, and the evidence differs:

1. A descriptive model of what children and adults do (Cook 2011, Nelson, Ruggeri, Coenen).
2. A yardstick to score questions (Battleship, 20 Questions; Rothe, Grand).
3. A selection rule inside an LLM scaffold (BED-LLM, UoT, Kobalczyk, Piriyakulkij). This is what our agent would use.

## 2. History and theories in depth

**Foundations (adult cognition).**
- Oaksford and Chater (1994) recast the Wason four-card task as choosing the query with the highest EIG, assuming the named properties (vowel, even number) are rare. Under rarity, testing "2" beats testing "7", matching the usual human choice (a06). Seen only through the Coenen review. Critics (Klayman and Ha) prefer a positive-test strategy; the rarity prior is an assumption.
- Steyvers, Tenenbaum, Wagenmakers and Blum (2003): which alien people chose to intervene on tracked EIG over causal structures (a07, review account only).
- Najemnik and Geisler (2005): eye movements follow expected information (cited in a05).
- Coenen, Rehder and Gureckis (2015): adults chose interventions on 3-variable causal systems. A hierarchical model fit a weight between EIG and a positive-testing heuristic. Time pressure shifted people toward the heuristic. Positive testing is not a mere approximation of EIG (a08).
- Rothe, Lake and Gureckis (2016/2018): in Battleship, people writing questions rarely reached high EIG; picking from a list matched EIG predictions. People judge well and generate poorly (a09). The 2017 model writes questions as programs scored by EIG plus complexity, answer type and relevance. Mean Spearman correlation with human question frequency: 0.64 full, 0.65 information-agnostic, 0.55 type-agnostic, -0.36 complexity-agnostic. About 15% of human questions per context were novel. EIG alone did not predict how often a question was generated; complexity mattered more (a14).
- Coenen, Nelson and Gureckis (2019) review: optimal experiment design (OED) is useful but has blind spots. It assumes the hypothesis and answer sets are known, ignores cost and motivation, and assumes ideal updating (a05).

**Probability gain versus information gain.** Nelson, McKenzie, Cottrell and Sejnowski (2010) built environments where the measures disagree. In experience-based learning, 82-97% of subjects per condition preferred the higher probability-gain feature (4 conditions; median subject 99% of trials; N=129, 113 reached criterion). With described statistics the preference fell to 27% and 30% in two conditions (65% and 58% in the other two) (a11, a12). The human case for Shannon EIG over probability gain is weak.

**The developmental line.**
- Cook, Goodman and Schulz (2011), "Where science starts" (numbers in section 3). Preschoolers (mean 54 months) isolated variables mainly when evidence was ambiguous. The fit to EIG is qualitative.
- Ruggeri and Lombrozo (2015) and Ruggeri, Lombrozo, Griffiths and Xu (2016): children 7-8 ask hypothesis-scanning questions ("Is it Bill?"); 9-11 and adults ask constraint-seeking ones. Match to EIG grows with age (a10, d04, d05).
- Nelson, Divjak, Gudmundsdottir, Martignon and Meder (2014): 4th graders judged question usefulness well and adapted to environment statistics. Abstract only was read (d06). Do not cite counts.
- Moeller, Sodian and Sobel (2022): closest follow-up to Cook; a different paradigm, not a replication (d03).

**The AI line (2023-2026).**
- 2023: Piriyakulkij, Kuleshov and Ellis chose among 8 LLM-written yes/no questions by expected entropy reduction over 10 products (a16). GATE and OPEN for preference elicitation (a24, a25).
- 2024: Uncertainty of Thoughts (UoT, a17). Piriyakulkij et al. on Zendo (a26). Grand et al. on Battleship (a15). Zhang, Lu and Jaitly benchmark 20 Questions (a21). Mazzaccara et al. train on EIG pairs with DPO (a22).
- 2025-2026: BED-LLM (Choudhury et al., ICLR 2026; a18, c01-c07, d15-d18). Kobalczyk et al. (ICLR 2025; a20, b09-b12, c13-c15). Wang et al. 2025, meta-trained simulator with lookahead (c20). Chan et al. 2025, conformal information pursuit (c21). QuestBench (b25, c22, d19). Laban et al., multi-turn drop (c23). Pedrozo 2026 on reasoning models (d07, d08). Deng 2026 on clarification in tool agents (d09, d10).

**Open theory debates.**
- Does EIG describe what people do, or only correlate with simpler heuristics (positive testing, probability gain, split balance)?
- Does EIG-like behaviour need understanding? Cook's authors say no. Moeller found that recognising confounds and choosing controlled tests were unrelated (K02).
- Greedy one-step EIG versus lookahead. Wang et al. found MCTS beat greedy EIG in all cases, and greedy EIG loses at most a constant fraction of the best achievable gain (c20).

## 3. Core findings with exact numbers

Status: E = established (2 or more independent sources, or very consistent), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Preschoolers isolate variables when evidence is ambiguous (Exp 1) | Informative action: All Beads 1/20 (5%); Some Beads B 9/20 (45%); Some Beads AB 10/20 (50%). chi2(1,N=40)=8.53 and 10.16, p<.005. B vs AB chi2=0.10 ns. 65% of All Beads children never pulled the pair apart. N=60, age ~54 months. Coder agreement 95% (kappa .90) | Cook et al. 2011 (a02, b01, d01) | S |
| Same, when the test must be invented (Exp 2) | All Beads 1/20 (5%) vs Some Beads 9/20 (45%), chi2(1,N=40)=8.53, p<.005. Coder agreement 86% (kappa .71) in one read, 96% in another. 55% of ambiguous-condition children still did not do it | Cook et al. 2011 (a03, b02, d02) | S |
| Ambiguity is not just more play | Play categories ~3.8 (Exp 1, F(2,60)=1.08 ns); 3.00 vs 2.78 (Exp 2, t(40)=0.89 ns) | Cook et al. 2011 (b03) | S |
| Cook fit is qualitative only | No computed EIG per child; authors disclaim understanding of experimental design; 2-4 variables, one session, one lab | Cook et al. 2011 (b04, b05) | S |
| Conceptual follow-up, different task | N=57, ages 3-6. Controlled-test choice on 66% of two-variable and 43% of three-variable trials; 70% chose one at least once; about a quarter could say confounded evidence supports no conclusion; recognition unrelated to choice | Moeller et al. 2022 (d03) | S |
| Children need more questions than adults | Questions to solve: 7-yr 4.92 (SE .34), 10-yr 4.38 (SE .35), adults 3.36 (SE .35); optimal 2.85; F(2,67)=5.29, p=.007. Mean question IG 0.83 (participants) vs 0.50 random vs 1.06 optimal | Ruggeri et al. 2016 (d04) | S |
| People ask zero-gain questions | At least once: 83% of 7-yr (n=20), 70% of 10-yr (n=16), 52% of adults (n=12). Object-selection study: adults 4.11 vs optimal 4.17 | Ruggeri et al. 2016 (d05) | S |
| Humans favour probability gain in experience tasks | 82-97% of subjects per condition preferred higher probability-gain feature (p<.001); median 99% of trials; N=129. Described-statistics task: 27% and 30% (two conditions), 65% and 58% (other two) | Nelson et al. 2010 (a11, a12) | S |
| Humans choose better than they generate | Modal Battleship question was mundane; list choices matched OED | Rothe et al. via Coenen 2019 (a09, a14, a15) | E |
| Time pressure shifts adults to positive testing | Three time-pressure experiments moved toward heuristic; one moved toward EIG. No point values | Coenen et al. 2015 via review (a08) | S (review only) |
| Human Battleship questions | Mean 1.27 bits, best 3.61 bits, 97% above zero; N=40, 605 board-question pairs, 18 boards | Grand et al. 2024 (a15, b19) | S |
| Sample-and-score beats a single sample | One GPT-4 or CodeLlama-7b question: 0.65-0.66 bits. k=5 near human mean; k=10 beats it (p<.001 CodeLlama, p=.01 GPT-4). Valid program rate 75% (CodeLlama), 88% (GPT-4). None reached the best human question. GPT-4V image input gave no gain | Grand et al. 2024 (a15, b19) | S (E that generation lags selection) |
| Unaided LLMs are weak at 20 Questions | Success Things / Celebrities: GPT-4 0.31 / 0.50, GPT-3.5 0.28 / 0.27, Claude-2 0.21 / 0.31, Vicuna-7B 0.09 / 0.06, Mistral-7B 0.13 / 0.22. GPT-4 used 17.8 and 17.3 of 20 turns. Zero-shot question quality 0.29-0.35 of a perfect half split | Zhang et al. 2024 (a21, c16); Mazzaccara 2024 (b14) | E |
| EIG in code lifts 20 Questions | Average +37.4 points, never lower (6 LLMs x 3 sets, 100 targets each). GPT-4o Animals 45 -> 93; Mistral-Large Celebrities 19 -> 91; GPT-4o Things 34 -> 64; Llama-3.1-8B Animals 8 -> 63; Llama-3.1-8B Things 10 -> 26. Standard errors ~2-5 points | Choudhury et al. 2026 (a18, c01, c02) | S |
| Model picking the best question is worse than code | Same candidates. Animals: GPT-4o 70 vs 93; Mistral-Large 53 vs 95; Qwen2.5-72B 61 vs 95. Prompt-only 45/33/45 | BED-LLM Table 1 (c02); Kobalczyk (a20, b09) | E for direction; S for numbers |
| Belief must be filtered hypotheses | In-context beliefs only: Animals GPT-4o 25 vs 93; Qwen2.5-72B 46 vs 95; Mistral-Large 53 vs 95 | BED-LLM ablation (c03) | S |
| Full EIG beats entropy and split by a smaller margin | Animals GPT-4o 93 / 88 / 83 (EIG / Entropy / Split). Celebrities Mistral-Large 91 / 68 / 63. Things GPT-4o 64 / 49 / 40. Celebrities GPT-4o: EIG 86, Split 63, Implicit-Max 50 | BED-LLM (c04, a19, d15) | S |
| Answer space beats hypothesis space | Data-Estimation Animals GPT-4o 70 vs 93; runtime 1d17h vs 2h30m (Qwen2.5-72B) | BED-LLM (c05, c07) | S |
| Runtime similar to cheap rules | Qwen2.5-72B, Animals set: BED-LLM 2h30m35s, Implicit-Max 2h28m43s, Split 2h46m19s, Entropy 3h10m39s; prompt-only and CoT 26-45 min | BED-LLM Table 3 (c07, d15, d16) | S |
| Gain survives a Q/A model mismatch | Questioner and answerer were different LLMs (e.g. Qwen2.5-72B asks, GPT-4o-mini answers); BED-LLM still led. Movie task: 200 users, 5 turns | BED-LLM (c06) | S |
| UoT gain over direct prompting | +38.1% relative (not points) averaged over 5 datasets and 5 LLMs; Llama3-70B +46.6%. GPT-4 per cell: DX 89.4 -> 97.0, Thing 30.8 -> 36.8, Common 49.0 -> 70.9, FloDial 42.5 -> 67.8 (a17 gives 43.7 -> 67.3). Llama3-70B 20Q Common closed set 51.4 -> 55.9 (+4.5) | Hu et al. 2024 (a17, b06, c10) | S |
| UoT versus other scaffolds | Over CoT-SC +33.8%, Reflexion +29.9%, ToT +28.3%, adapted ToT +12.4% (relative). At ~9k GPT-4 tokens: UoT 20Q 54.4, MD 92.5, TB 66.0 vs adapted ToT 40.9, 86.7, 63.7. At ~4.6k tokens CoT-SC (k=33) 32.6/37.6/42.5; pruned UoT 48.1/88.4/63.2 at 4.7k | Hu et al. 2024 (c11, b07) | S |
| UoT diagnosis length | DX GPT-4 97.0% success; 2.0 questions per success vs 3.0-3.5 for direct methods; MedDG 88.0% (GPT-4), 81.4% (Gemini-1.5-Pro) | Hu et al. 2024 (c12) | S |
| EIG for clarifying code tasks | HumanEval GPT-3.5 binary 70.8 -> 85.6, open 75.9 -> 85.0; Llama3-8B binary 53.0 -> 65.8, open 64.8 -> 75.5; GPT-4o-mini binary 79.6 -> 81.5. APPS GPT-4o-mini binary 62.9 -> 75.3, open 75.1 -> 87.2; GPT-3.5 binary 62.4 -> 71.3, open 69.7 -> 77.3. 4 questions; 48 and 47 tasks | Kobalczyk et al. 2025 (c13, c14, b10) | S |
| EIG over sampled solutions on 20 Questions | Rank score at t=10 (higher is better): GPT-3.5 EIG-uniform 6.2, implicit 4.9, implicit-ToT 5.1, EIG-logprobs 4.1. GPT-4o-mini 6.8, 5.5, 6.6, 6.0. N=20 sampled solutions approximated a 500-animal list | Kobalczyk et al. 2025 (c15 as corrected by critique, b09) | S |
| LLM log-probabilities as weights hurt | EIG-logprobs below EIG-uniform from t=3 on for both models. LLM distributions are biased and overconfident; conformal set size is more robust | Kobalczyk (b12); Chan et al. 2025 (c21); BED-LLM (a18) | E |
| DPO on EIG pairs helps a 7B model | INLG 56.7 -> 68.9 (EIG 0.34 -> 0.45); Things 51.1 -> 61.1 (0.29 -> 0.40); Celebrities 71.1 -> 72.2 (+1.1). Plain fine-tuning lowered success (INLG 46.6). 55,000 pairs. BigBench 17.2 -> 31.0 while EIG fell 0.31 -> 0.28 | Mazzaccara et al. 2024 (a22, b13, c18) | E |
| RL on game play | Vicuna 7B Things 0.09 -> 0.26; 13B 0.18 -> 0.27. Cloning all games 0.13; successes only 0.23 | Zhang et al. 2024 (c17) | S |
| Zendo: EIG experiments plus rule revision | Accuracy out of 8: human 5.26; direct LLM 4.60 (SE .19); online fuzzy 5.35 (SE .09); online hard 6.55 (SE .13). R2 with human per-rule accuracy: online fuzzy .57, ReAct .25, hard .10, batch .05. Log-likelihood of human data: online fuzzy -1478.82 | Piriyakulkij et al. 2024 (a26, d13) | S |
| Zendo: who picks the experiment | Hard rules: LLM-chosen 4.72, random 5.84, InfoGain 6.55. Fuzzy: 4.52, 5.03, 5.35. Candidate experiments 1/5/10: ~5.84/6.23/6.55 (random proposer), 5.73/6.19/6.55 (LLM proposer). ActiveACRE solving: online hard 0.35, batch hard 0.15, ReAct 0.00 | Piriyakulkij et al. 2024 (d14) | S |
| Preference elicitation | GATE: 388 participants, 3 domains, beat no elicitation in all (p<.05 except email). OPEN beat LM-only; arms ~44 users; exact TIDA values not recorded | Li et al. 2023; Handa et al. 2024 (a24, a25, b24) | E for direction |
| GPT-3 lacks directed exploration | Horizon task beta=-0.15 +/- 0.27, z=-0.56, p=.58 (no horizon effect); fails intervention-based causal tasks; fine on vignettes | Binz and Schulz 2023 (c25, c26, b22) | E, old model |
| QuestBench | Logic-Q and Planning-Q best ~40-50% (o1-preview ZS+CoT 49.9% and 42.3%); GSM-Q 77-94%, GSME-Q over 90%. CoT and few-shot no consistent gain. BFS in code: depth 3 39.0%, depth 5 80.6%, depth 10 99.8% | Li et al. 2025 (b25, b26, c22, d19) | S |
| Multi-turn drop | 39% average drop single- to multi-turn, 200,000+ simulated conversations, six tasks; mostly reliability, little aptitude | Laban et al. 2025 (c23) | S |
| Reasoning mode, small open models | Qwen3-30B partially observable: no-think win 0.10 (IG/turn 0.14, 29.1 turns) vs think 0.93 (0.42, 14.9 turns). Qwen3-8B 0.08 vs 0.94 (0.17 vs 0.41). Llama-3.1-8B 0.81 (0.35). 120 games per model | Pedrozo et al. 2026 (d07) | S |
| Reasoning models seldom pick the best listed question | Optimal rate: 30B FO 0.26, PO 0.25; 8B FO 0.36, PO 0.19. Chosen vs best listed IG (bits): 30B FO 0.77 vs 1.40; PO 0.43 vs 0.88; 8B FO 0.66 vs 1.11; PO 0.41 vs 0.94. 5.05-9.74 candidates per turn | Pedrozo et al. 2026 (d08) | S |
| Over-asking costs | Budget 0 -> moderate: success ~15% -> >21%; steps 24.2 -> 22.1 -> 26.5 -> 23.6 -> 25.1 beyond 16. Untrained Qwen3-8B clarifier: -0.6 averaged, -3.5 for Qwen3-8B agent, -6.3 airline. Learned 1.7B clarifier: +3.7 averaged (airline +5.4, retail +1.4), 1.3 turns vs 3.9-5.1. DeepSeek-R1 agent 35.7 -> 40.0 | Deng et al. 2026 (d09, d10) | S |
| Ask-or-answer gates are weak | AUROC QA GPT-3: likelihood .590, Self-Ask .538, semantic entropy .625, intent entropy .628. MT: .547, .371, .531, .512. LLaMA-2 7B QA .501-.532. At 30% budget a gate captured ~49% of the full gain (random 30%). Trained gate F1 24.3 vs random 23.4 vs ProCoT 15.6 | Zhang and Choi 2023; Zhang, Knox and Choi 2025 (d11, d12) | S each; E that gates are weak |
| Lookahead beats greedy | MCTS > greedy EIG in all cases on 3 datasets (10,000 simulated runs each); greedy beats base Llama-3.1-8B | Wang et al. 2025 (c20) | S |
| Cost and stability | Calls O(N+M+NM) for LLM-answered tasks; O(N+M) when answers come from running sampled programs. Ranking at 10 hypotheses equalled ranking at 85 in one turn (M=8 candidates, N>=5) | BED-LLM App. F.2; Kobalczyk App. F (d16, d17) | S |
| Hypothesis-set recipe | Independent sampling of 200 collapses onto a few modes. Recipe: one list, T=1.3 (20Q) or 1.0 (preferences), history-compat filter 0.2, >=5 survivors, uniform prior, re-ask 2-3 times | BED-LLM (d18) | S |

## 4. Mechanisms and models

### 4.1 The core loop (an engineer can build this)

State kept in code:
- H: a list of N sampled hypotheses (N about 10-20; at least 5 survivors).
- History: all (test, outcome) pairs.
- Weights: uniform over survivors (uniform beat the model's own log-probabilities, K14).

Per turn:
1. Filter. For each hypothesis, ask the model whether it is consistent with the full history. Drop inconsistent ones. If fewer than 5 survive, ask the model for more hypotheses in one list (diversity prompt, high temperature, latest Q/A moved to the top). Re-ask up to 2-3 times (d18).
2. Propose. Ask for M candidate tests (M about 8; BED-LLM and Piriyakulkij used 8).
3. Predict. For each (candidate q, hypothesis h) get the predicted outcome. If the world is a program, run it (cost O(N+M), d17). If an LLM predicts, it costs about N*M cheap calls. Deterministic predictions give a split score; noisy ones use p(a|q,h).
4. Score. Code computes EIG(q) = H(marginal outcome) - mean over h of H(outcome | h). The conditional term matters: a question whose answers are noisy even for the true item has high marginal entropy and near-zero EIG (a19). Subtract a cost term if tests differ in price.
5. Act. Run the top test in the real world.
6. Update. Append the outcome; go to 1.
7. Stop (see 4.4).

### 4.2 Three scoring levels, cheapest first

| Level | What code does | Source |
|---|---|---|
| Split balance | Count how evenly the test splits survivors. No noise model | Split baseline, c04 |
| Marginal entropy | Entropy of the predicted answer distribution | Entropy ablation, a19 |
| Full EIG | Marginal minus mean conditional entropy | BED-LLM, c04 |

Animals, GPT-4o: 83 / 88 / 93. Most of the gain over prompting (45) comes from holding a hypothesis set and scoring splits at all. Full EIG adds points mainly when answers are noisy.

### 4.3 Why each design choice (from ablations)

- Hypotheses, not in-context beliefs: in-context belief tracking collapsed to 25% (c03). Models hold beliefs that contradict the history.
- Code does the arithmetic: model picks from the same candidates gave 70 vs 93 (c02). Humans show the same generate-versus-select gap (a09).
- Uniform weights: the model's own probabilities are overconfident and biased (b12, c21).
- Uncertainty in answer space, not hypothesis space (c05).
- Sample many candidate tests, keep the best by score. Humans are matched at k=5 and beaten at k=10 (a15). A random proposer with 10 candidates equals an LLM proposer, so the selection rule matters more than who writes candidates (d14).
- Lookahead helps if a simulator of future answers exists; it needed meta-training (c20). UoT simulated 3 steps for cost reasons (c11).

### 4.4 Stop and ask-or-answer rules

- Stop 1: one hypothesis left. Further questions have zero gain; 52-83% of people still asked (d05).
- Stop 2: max EIG under a small threshold, or EIG minus cost below zero (b11).
- Budget cap: success rises to a moderate budget then plateaus or falls; extra turns add steps (d10).
- Ask-or-answer gate: evidence is weak (AUROC about 0.6, d11). Entropy over simulated user intents is the best simple one found. A principled gate is "ask only if best EIG minus cost exceeds the expected loss from answering now". Untested (K28).

### 4.5 Cook's model

EIG(A) = sum_i P(D_i | A) * Ig(D_i, A) (a01). Ambiguous evidence raises prior uncertainty, so isolating actions score higher. When all beads worked, little was left to learn, so any action scored near zero. Agent analogue: do not spend a test where all live hypotheses predict the same outcome. Check first that a test can separate hypotheses at all.

## 5. What holds up

**Replications.**
- Cook et al. 2011: no direct replication or failed replication found (K01). Three searchers found none; that shows none was reported, not that none exists. Moeller et al. 2022 (N=57) is a conceptual extension and found recognising confounds and choosing controlled tests were unrelated (d03).
- The direction "unaided LLMs ask weak questions; sample-and-score helps" repeats across independent labs and tasks: Grand (Battleship), Zhang (20 Questions), Mazzaccara (20 Questions), Piriyakulkij (shopping, Zendo), Kobalczyk (20 Questions, code), Hu (20 Questions, diagnosis), Choudhury (20 Questions, preferences). Direction established; each size is single-source.
- Log-probabilities as weights fail in three sources (b12, c21, a18).

**Failures, nulls and negatives.**
- Plain supervised fine-tuning on high-EIG questions lowered success (INLG 56.7 -> 46.6; Things 51.1 -> 42.2; Celebrities 71.1 -> 46.7; b13).
- Higher EIG did not always give higher success: BigBench success rose 17.2 -> 31.0 while mean EIG fell 0.31 -> 0.28; Celebrities DPO gain only +1.1 (c18).
- CoT and plan-and-solve did worse than plain GPT-4 on 20 Questions in UoT (b08).
- GPT-4V with the board image gained nothing over text (a15).
- LLM-chosen Zendo experiments (4.72) were worse than random (5.84) (d14).
- An untrained clarifier hurt a tool agent (-3.5 to -6.3 points; d09).
- WebShop (150 tasks): the EIG advantage appears only after more than one question (a16).
- The gap between EIG and implicit prompting shrinks for the stronger model: GPT-4o-mini rank 6.8 vs 5.5 (implicit) and 6.6 (implicit-ToT); HumanEval GPT-4o-mini binary 79.6 -> 81.5 (c15, c13).
- Entropy-over-intents gate near chance on translation (AUROC .512; d11).

**Moderators.**
- Model strength: weaker models gain more (GPT-3.5 vs GPT-4o-mini).
- Task difficulty: larger gain on harder tasks (APPS +12.4 binary and +12.1 open for GPT-4o-mini, vs +1.9 binary on HumanEval).
- Closed versus open hypothesis set: UoT's open set is weaker than closed (a17).
- Question type: open questions are more informative than binary but cost the answerer more effort (c14, b24).
- Experience versus description for humans (a11, a12). Time pressure (a08).
- Candidate-set size: DPO gains shrink with larger sets (b13) but remain (+6.7 and +13.8 at 16 and 29 candidates; a22).

**Worked.** Code-side EIG over filtered sampled hypotheses (+37.4 points, 20 Questions). EIG for clarifying code tasks (+12 to +15 points for weaker models on APPS and HumanEval). EIG experiment choice in Zendo (6.55 vs 5.84 random). DPO on EIG pairs. Uniform or conformal weights.

**Did not work.** Plain fine-tuning on high-EIG questions; LLM log-probability weights; CoT prompts for question choice; image input; untrained clarifiers; unbounded question budgets; asking the model to pick the best question.

**Caveats from the critique.**
- UoT's 38.1% is relative; BED-LLM's 37.4 is points. Not comparable. Success definitions and answerers differ (open versus closed lists).
- Almost all LLM gains are over a weak prompt-only baseline. A strong baseline (split rule) wins back a large share (83 vs 93).
- All 2025 LLM results use 2024-vintage models. Reasoning models were tested only on QuestBench (2024-25 models) and small Qwen3 models.
- Answerers are mostly simulated by LLMs. Human answerers: Li 2023 and Handa 2024 only.
- No paper reports accuracy at equal tokens against best-of-N. This is the central gap.

## 6. Language models

**Unaided behaviour.**
- 20 Questions (2023-24): GPT-4 wins 31% (Things) and 50% (Celebrities) and uses 17-18 turns of 20; open models under 25% (a21, c16). Failure modes: early enumeration, redundancy, inconsistent questions (c16).
- Zero-shot Llama-2-7B questions score 0.29-0.35 of a perfect half split (b14).
- Prompt-only: GPT-4o Animals 45; Mistral-Large Celebrities 19; Llama-3.1-8B Animals 8 (a18).
- Battleship: a raw GPT-4 or CodeLlama-7b question averages 0.65-0.66 bits, about half the human 1.27 (a15).
- QuestBench: strong models pick the right clarifying question only ~50% on logic and planning while able to solve full problems; BFS in code reaches 80.6% at depth 5 (b25, d19).
- GPT-3 showed no directed exploration (c25). It did well on information-search vignettes (6 of 12 correct, all 12 correct or human-like) but those were probably in training data (b21).
- Multi-turn: models guess early and do not recover; 39% average drop (c23).
- Yiu, Kosoy and Gopnik (2023): LLMs do well on superficial matching but poorly on functional innovation and on extracting causal over-hypotheses on the blicket detector. Position paper; contamination risk (c24).

**What changed it, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Code-side EIG over filtered sampled hypotheses | +37.4 points average, 20 Questions | c01 |
| Same, versus model picks best candidate | 93 vs 70 (GPT-4o Animals) | c02 |
| Remove hypothesis filtering | 93 -> 25 | c03 |
| Marginal entropy only | 93 -> 88 | a19 |
| Even-split rule only | 93 -> 83 | c04 |
| Uniform weights vs model log-probs | rank 6.2 vs 4.1 (GPT-3.5) | c15 |
| UoT simulation + info-gain reward | +38.1% relative | a17 |
| Sample k questions, keep best EIG | 0.65 bits at k=1; human level at k=5; above human at k=10 | a15 |
| EIG-chosen clarifying questions before coding | +11.3 to +12.4 points (APPS GPT-4o-mini), +14.8 (HumanEval GPT-3.5 binary), +1.9 (HumanEval GPT-4o-mini) | c13, c14 |
| DPO on EIG pairs (training) | +12.2 INLG, +10.0 Things | b13 |
| Reasoning mode (Qwen3 8B/30B, partial observability) | win 0.08-0.10 -> 0.93-0.94 | d07 |
| Share of turns where reasoning model picks best listed question | 19-36% | d08 |

**Reasoning models.** Thinking mode closes most of the gap on a city-guessing game, yet the model picks the best of its own listed candidates only 19-36% of turns (d07, d08). Thinking improves hypothesis building and sorting, not optimal selection. Whether o-series, Claude extended-thinking or Gemini 2.5 make code-side EIG redundant has not been measured. SCHEMA section 7 already lists the "Thinking-mode baseline" as a first test.

**Cost.** BED-LLM wall-clock is about the same as split or implicit max (2h30m vs 2h46m vs 2h29m) and far below Data-Estimation (1d17h). UoT at ~9k tokens beat adapted ToT (20Q 54.4 vs 40.9); CoT-SC k=33 at ~4.6k gave 32.6 (c11). No paper reports tokens for BED-LLM.

## 7. What our agent should take

Mapping. The test-choice step lives in S4 TEST (choose which check to run) and uses G5 (code selects). It needs a new operator slot, called "OT: choose the most separating test" here, until SCHEMA.md assigns a number. Claims tagged "O1" in claims.jsonl mean this step.

### Add now (established [E])

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | Rank candidate tests in code, not by asking the model which is best. Model picks recover only part of the gain (70 vs 93; 53 vs 95; 61 vs 95). | G5 / S4 | [E] | K08; c02, a18, a20, b09, c13 |
| 2 | Use uniform weights over filtered samples inside the score, never the model's stated probabilities. | G5 | [E] | K14; b12, c15, c21, a18 |
| 3 | Generate several candidate tests, then select. One sample is about half of human quality; k=5 matches humans, k=10 beats them. | S3 / S4 | [E] direction | K05, K06; a15, b19, a14, a09 |
| 4 | Treat the model's own question choice as a weak baseline. Unaided models ask poorly and CoT does not fix it. | S4 | [E] | K15, K20; a21, c16, b14, b26, c22 |
| 5 | Make ask-versus-answer an explicit decision; guessing early and not recovering is a documented failure. (The gate itself is untested; see Test first.) | S0 / S1 / G | [E] for the failure | K21; c23, a27 |
| 6 | Positive testing is not EIG. If candidate tests only confirm, force at least one that would separate two live hypotheses. | S4 | [E] | K05; a08, a09 |

These are defaults for tasks with a small, enumerable hypothesis set. G7 still applies: keep each only if it wins at equal tokens.

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Hypothesis set kept as a sampled, filtered list, not in-context belief | S2 / memory | [S] | K09, K31; c03, d18 |
| T2 | Full EIG vs even-split score (the split score may be enough) | S4 | [S] | K10; c04, a19, d15 |
| T3 | EIG-in-code vs best-of-N vs thinking mode at equal tokens | G7 / S4 | [S] | K29, K25; d15, d07, d08 |
| T4 | Ask-before-solving on underspecified items, questions chosen by EIG | S0 / S1 | [S] | K13; c13, c14 |
| T5 | Ask-or-answer gate (three gates) and a question cap | S0 / G | [S] | K26, K28; d09-d12 |
| T6 | Stop rule: one survivor, or max EIG below threshold | S4 / S7 | [S] | K27; d05 |
| T7 | Rule revision plus EIG experiments on rule induction | S3 / S4 | [S] | K18; a26, d13, d14 |
| T8 | Two-step lookahead in code vs greedy | S4 | [S] | K22; c20 |
| T9 | Shannon EIG vs probability gain | S4 | [C] (humans lean to probability gain; LLM untested) | K03, K04, K32; a11, a12 |
| T10 | Hypothesis sampling for open tasks (code, proofs) | S3 | [S] | K31; d18 |
| T11 | Noisy or wrong answerer (tool errors) | S4 | no data | K32 |
| T12 | Cook analogue: with clear vs ambiguous prior evidence, does the agent design a discriminating test? | S4 | [S], human-only | K01, K02 |

Not for the schema: DPO and RL on EIG pairs (K16, training); Cook's numbers as an effect-size prior (K02); the Wason-rarity argument until the primary is read (K24).

## 8. Concrete tests on our bench

Every test runs both arms at equal total tokens (count every extra candidate and likelihood call in the EIG arm). Report accuracy, mean turns, tokens, and log the tests chosen.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Selection by code | Small hidden-set items (20 Questions; rule induction) | A: model picks best of 8 candidates. B: code EIG over 10-20 sampled hypotheses, same 8 candidates | Success in 20 turns; turns to success | B above A by 15-25 points on mid-tier models (BED-LLM saw 23-42); smaller on stronger models |
| B2 EIG vs split | Same as B1 | A: even-split score. B: full EIG with noise term | Success; tokens | B above A by 5-10 points when answers are noisy; tie when deterministic |
| B3 Equal tokens vs best-of-N and thinking | Underspecified coding items (HumanEval/APPS style with hidden requirements); diagnosis puzzles | A: thinking mode, one long attempt. B: best-of-N vote. C: EIG scaffold with 4 questions | Accuracy at fixed total tokens | C beats B by 5+ points on hard items only (APPS +12); none on easy items |
| B4 Filtered vs in-context belief | 20 Questions | A: unfiltered hypotheses. B: filtered against all history | Success; survivors per turn | B above A by 20+ points (93 vs 25) |
| B5 Ask-or-answer gate | Items with and without a missing variable (QuestBench style, 50% underspecified) | A: always ask. B: intent-entropy threshold. C: best EIG minus cost > expected loss | Accuracy; questions asked; wasted questions | C asks about half as often as A with no accuracy loss; B near A (AUROC 0.63) |
| B6 Question cap | Same | Cap 0, 2, 6, 16 | Success vs steps | Peak at 2-6, no gain beyond (Deng 2026) |
| B7 Stop rule | Games where one hypothesis can remain | A: none. B: stop at one survivor or max EIG < 0.1 bit | Zero-gain questions per game; turns | B halves wasted turns with no loss of success |
| B8 Generate then select | Battleship-like or hidden-rule items | k = 1, 5, 10 sampled tests, code picks max EIG | Bits per test; success | EIG rises from ~0.65 bits at k=1 toward human level at k=5 |
| B9 Lookahead | 20 Questions, diagnosis | Greedy vs 2-step EIG | Success at equal tokens | 2-step helps only if simulation is cheap |
| B10 Gain measure | Cases where EIG and probability gain disagree | Shannon EIG vs probability gain | Final correctness | Unknown; run to settle K03/K04 |
| B11 Noisy answerer | 20 Questions with answer flips | 0, 10, 20, 30% flips; with and without noise term | Success | Full EIG degrades more gently than split; threshold unknown |
| B12 Open-task hypotheses | Code spec disambiguation | N = 5, 10, 20; one-list diverse vs independent sampling | Rank stability; survivors per turn; accuracy | Stable ranking at N=10; independent sampling mode-collapses |
| B13 Cook analogue | Items with clear (all candidates behave alike) vs ambiguous prior evidence | Same agent, two evidence conditions | Rate of discriminating tests | Higher in the ambiguous cell if the agent follows value of information |

## 9. What does not transfer, and why

- Cook's numbers: 20 children per cell, 2-4 variables, one lab, qualitative fit, authors disclaim understanding (K02). Use only as support for "ambiguity motivates tests".
- Human over-asking figures: they show humans over-ask; they give no threshold for an agent whose questions cost tokens.
- Human generation-versus-selection gap: for the agent, generating many candidates is cheap. The lesson transfers only as "select in code".
- Closed-world games: 20 Questions, Battleship, Zendo and DX have an enumerable hypothesis set and a truthful answerer. Coding, research and open problems do not (gap 3). UoT's open set is already weaker than its closed set.
- Simulated answerers: almost all results use an LLM as answerer. Real tools can be wrong or slow.
- Training results (DPO, RL, STaR-GATE; K16): our agent is a scaffold with no training.
- Absolute numbers across papers: success definitions, answerers and metrics differ; do not set 37.4 points beside 38.1%.
- Preference elicitation (GATE, OPEN): the user is the answerer; relevant only if our agent asks users.
- GPT-3-era negatives (no directed exploration): predate current models; need a rerun, not a rule.
- Vision (GPT-4V no gain): not our setting.

## 10. Open questions

1. Does code EIG still beat best-of-N and extended thinking at equal tokens on a current reasoning model? Nothing reports it.
2. Do o-series, extended-thinking Claude and Gemini 2.5 already ask near-optimal questions? Only small Qwen3 data exist (19-36% optimal choices).
3. How should hypotheses be generated for code, proofs and research questions, and how many samples are needed?
4. Where is the ask-or-answer boundary? Is EIG minus cost better than intent entropy (AUROC 0.63)?
5. Is there any replication or failed replication of Cook 2011? Do later EIG-fit child studies (Nelson 2014) show the same pattern?
6. How do LLM likelihoods hold up for tool outputs, not yes/no answers? Does miscalibration erase the gain?
7. Does probability gain or error reduction predict agent success better than Shannon EIG?
8. Does EIG experiment choice transfer to scientific-style tasks with strong baselines? Zendo and ActiveACRE are toy domains with 5 seeds.
9. How much of the gain survives a wrong or noisy answerer?
10. What is the true token overhead of EIG with 10-85 hypotheses?
11. Why did higher EIG not always give higher success (BigBench, Celebrities)? Does EIG break as a proxy when targets are abstract?
12. Does lookahead pay for its tokens in a scaffold without meta-training?
13. Retry list for a working search: gaps 1, 6, 7, 9, then newer reasoning-model tests of question asking.

Links to other subfields run in parallel (not covered here): Bayesian and causal learning; Exploration and exploitation, Bandit-style exploration (value of information); Optimal stopping, Metareasoning and value of computation (when to stop asking); Counterexample finding, Probabilistic and test-based reasoning (discriminating tests); Test-time compute scaling (the equal-token baseline); Debugging as scientific method, Fault localisation and repair, Model-based diagnosis (probe choice); Confidence and signal-detection measures (likelihood calibration); Metamemory judgments.

## 11. Sources

[V] = opened and read; [M] = snippet or secondary text only.

- [V] Cook, Goodman and Schulz (2011), Where science starts: spontaneous experiments in preschoolers' exploratory play. https://dspace.mit.edu/bitstream/1721.1/106813/1/Spontaneous%20experiments%20in%20preschoolers.pdf and https://web.stanford.edu/~ngoodman/papers/CookGoodmanSchulz2011.pdf (a01-a04, b01-b05, d01, d02). The critic could re-read only the PubMed abstract; two independent reads agree on cell counts.
- [V] Coenen, Nelson and Gureckis (2019), Asking the right questions about the psychology of human inquiry, Psychon Bull Rev. https://link.springer.com/content/pdf/10.3758/s13423-018-1470-5.pdf (a05; source for secondary entries a06-a10, a13)
- [M] Oaksford and Chater (1994), selection task as optimal data selection. Via a05 (a06).
- [M] Steyvers, Tenenbaum, Wagenmakers and Blum (2003), causal networks from observations and interventions. Via a05 (a07).
- [M] Coenen, Rehder and Gureckis (2015), strategies to intervene on causal systems. Via a05 (a08).
- [M] Rothe, Lake and Gureckis (2016/2018), Do people ask good questions? Via a05 and a15 (a09, b20).
- [M] Ruggeri and Lombrozo (2015); Ruggeri, Lombrozo, Griffiths and Xu (2015). Via a05 (a10, b27).
- [V] Nelson, McKenzie, Cottrell and Sejnowski (2010), Experience matters. https://pmc.ncbi.nlm.nih.gov/articles/PMC2926803/ (a11, a12)
- [M] Nelson, Divjak, Gudmundsdottir, Martignon and Meder (2014), Children's sequential information search. https://pubmed.ncbi.nlm.nih.gov/24184396/ (a13, d06; abstract only)
- [M] Rothe, Lake and Gureckis (2017), Question asking as program generation, NeurIPS. https://papers.nips.cc/paper_files/paper/2017/file/24681928425f5a91335 (a14; URL truncated in the evidence file)
- [V] Grand, Pepe, Andreas and Tenenbaum (2024), Loose LIPS sink ships. https://arxiv.org/abs/2402.19471 (a15, b19)
- [V] Piriyakulkij, Kuleshov and Ellis (2023), Active preference inference using language models. https://arxiv.org/abs/2312.12009 (a16, c08, c09)
- [V] Hu et al. (2024), Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271 (a17, b06-b08, c10-c12)
- [V] Choudhury et al. (2026, ICLR), BED-LLM. https://arxiv.org/abs/2508.21184 (a18, a19, c01-c07, d15, d16, d18)
- [V] Kobalczyk, Astorga, Liu and van der Schaar (2025, ICLR), Active task disambiguation with LLMs. https://arxiv.org/abs/2502.04485 (a20, b09-b12, c13-c15, d17)
- [V] Zhang, Lu and Jaitly (2024), Probing the multi-turn planning capabilities of LLMs via 20 Questions. https://arxiv.org/abs/2310.01468 (a21, c16, c17)
- [V] Mazzaccara, Testoni and Bernardi (2024), Learning to ask informative questions. https://arxiv.org/abs/2406.17453 (a22, b13, b14, c18)
- [V] Andukuri, Franken, Gerstenberg and Goodman (2024), STaR-GATE. https://arxiv.org/abs/2403.19154 (a23)
- [V] Li, Tamkin, Goodman and Andreas (2023), Eliciting human preferences with language models. https://arxiv.org/abs/2310.11589 (a24, b23)
- [V] Handa, Gal, Pavlick et al. (2024), Bayesian preference elicitation with language models. https://arxiv.org/abs/2403.05534 (a25, b24, c19)
- [V] Piriyakulkij, Langenfeld, Le and Ellis (2024), Doing experiments and revising rules. https://arxiv.org/abs/2402.06025 (a26, b16-b18, d13, d14)
- [V] Zhang and Choi (2023), Clarify when necessary. https://arxiv.org/abs/2311.09469 (a27, d11)
- [M] Bertolazzi et al. (2023), ChatGPT's information seeking strategy. Via b14/b15 (b15).
- [V] Binz and Schulz (2023), Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (b21, b22, c25, c26)
- [V] Li, Kim and Wang (2025), QuestBench. https://arxiv.org/abs/2503.22674 (b25, b26, c22, d19)
- [V] Wang, Zollo, Zemel and Namkoong (2025), Adaptive elicitation of latent information. https://arxiv.org/abs/2504.04204 (c20)
- [V] Chan et al. (2025), Conformal information pursuit. https://arxiv.org/abs/2507.03279 (c21)
- [V] Laban et al. (2025), LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120 (c23)
- [V] Yiu, Kosoy and Gopnik (2023), Imitation versus innovation. https://arxiv.org/abs/2305.07666 (c24; position paper)
- [V] Moeller, Sodian and Sobel (2022), Developmental trajectories in diagnostic reasoning, Frontiers in Psychology. https://www.frontiersin.org/journals/psychology (d03; the evidence file holds the full article URL)
- [V] Ruggeri, Lombrozo, Griffiths and Xu (2016), Sources of developmental change in the efficiency of information search. https://cocosci.princeton.edu/papers/Ruggeri_DevPsych.pdf (d04, d05)
- [V] Pedrozo, Soares and de Oliveira (2026), Do reasoning models ask better questions? https://arxiv.org/pdf/2601.17716 (d07, d08)
- [V] Deng et al. (2026), Uncertainty-aware clarification in LLM agents. https://arxiv.org/pdf/2606.03135 (d09, d10)
- [V] Zhang, Knox and Choi (2025), Modeling future conversation turns to teach LLMs to ask clarifying questions. https://arxiv.org/pdf/2410.13788 (d12)
- [V] Search-outcome note, negative result under rate limits (d20). https://arxiv.org/pdf/2508.21184

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 8 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A14.04-K05** (now single-source: only one opened source, code check).
- **A14.04-K06** (now single-source: only one opened source, code check).
