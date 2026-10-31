# Wisdom of crowds: conditions: deep document

*Subfield A17.01. Built from evidence_a-d.jsonl (a01-a28, b01-b26, c01-c26, d01-d16), claims.jsonl (K01-K26) and critique.md in this folder. Evidence ids in brackets. [V] = page or PDF text opened, [M] = snippet or secondary only. Several 2026 items are single-author preprints; treat their numbers as single-study.*

## 1. What it is

The wisdom of crowds is the claim that an aggregate of many answers (mean, median, majority vote) is more accurate than a typical single answer, and sometimes more accurate than the best one. It is a statistical fact first and a social fact second. It needs four conditions:

1. **Independence.** Voters' errors must not be shared. Shared error does not average out.
2. **Diversity.** Voters must differ, so their errors point in different directions.
3. **A correct answer that voters can reach.** Each voter must be right more often than wrong (binary case), or have errors centred on the truth (numeric case).
4. **Random, not shared, error.** Averaging removes random error. It never removes bias that every voter has [a04].

Two formal results hold the idea together.

- **Condorcet (1785).** Binary choice, each voter right with independent probability p. If p > 0.5 the majority gets better as voters are added and tends to 1. If p < 0.5 it gets worse. Example: n=3, p=0.8 gives 0.896 [a05]. Correlated votes cap the gain below 1 (Ladha 1992 [a26, M]).
- **Page's diversity prediction theorem (2007).** Collective squared error = average individual squared error minus diversity (variance of guesses around the group mean) [a06]. The crowd beats its average member by exactly its diversity. This is arithmetic, not a social effect. It says nothing about whether the crowd beats its best member.

Why it matters for our agent. Sampling one model k times and voting is the cheapest tool we have (schema S3, S7). Guardrail G4 says samples from one model are not independent, so agreement is a hint, not proof. This document says when a vote is valid, how much the shared-error ceiling costs, and what to do when the vote is not valid.

## 2. History and theories in depth

**Condorcet 1785.** Jury theorem above. Assumptions: two options, independence, equal competence p. Later work relaxes each. For equal-competence voters with equal pairwise correlation, there is a quota at which correlation does not matter. Under simple majority, more positive correlation lowers accuracy, and a correlated jury can be worse than one juror [d10, V abstract and intro].

**Galton 1907, "Vox Populi" (Nature 75).** Visitors to a Plymouth livestock fair paid 6d to guess the dressed weight of one ox. Galton chose the median ("one vote, one value"). Published: 787 usable cards of about 800, median 1207 lb, ox 1198 lb, error 9 lb (0.8%) [a01, M: the scan has no text layer; read only through Wallis]. Wallis (2014) went to the archive [a02, V]: correct median 1208 lb (394th of 787), true weight 1197 lb, error 11 lb (about 1%). Quartiles 1162 and 1236. Galton's published numbers had slips he never noticed. The arithmetic mean of the 787 guesses was exactly 1197, error 0 [a03, V]. Lessons: it is one ox, one fair, a paying crowd including butchers and farmers, so it is an anecdote about averaging, not a test of independence. The mean beat the median here; in Lorenz 2011 the mean was terrible. Even the founding numbers are cited wrongly, so check numbers at the source.

**Surowiecki 2004.** Popular statement of four conditions: diversity of opinion, independence, decentralisation, aggregation. Not a source of data. The condition list matches section 1.

**Hong and Page 2004.** Agents search a ring of random values with different heuristics. A random team beats a team of the individually best agents. Ring n=2000, k=3, l=12, 50 trials, ten best vs ten random: performance 92.56 vs 94.53; diversity (share of unique heuristics) 70.98% vs 90.99%. Twenty agents: 93.78 vs 94.72. l=20: 93.52 vs 96.08 [a10, V]. Mechanism: a team gets stuck only at a point that is a local optimum for every member, so different heuristics shrink the shared stuck set [a11]. Critique (Thompson 2014, not opened; Karge 2025 gives exact conditions in a Condorcet voting model with an opinion leader [b09, V]): the theorem needs a finite heuristic pool and agents with identical perspectives; it is about search, not voting on a fact [K09, contested].

**Lorenz et al. 2011.** First lab test of independence. 144 ETH students in 12 groups of 12, six factual estimation questions, five rounds, paid for accuracy. Conditions: no information, average of others, all estimates. Social information shrank diversity without making the mean better, pushed the truth to the edge of the estimate range ("range reduction"), and raised confidence with no accuracy gain. The wisdom indicator fell about one unit [a07, a09, b03; V]. Aggregate information hurt more than full information.

**Later work on influence.** Becker, Brackbill and Centola 2017: 1,360 people in 40-person networks. Decentralised networks improved (mean error 0.69 to 0.62, -10%; median -12%; individual error -23%; SD -43%; control unchanged). Centralised: if the central person started near the truth mean error fell 43%, if away it rose 19% [b04, V]. Almaatouq et al. 2021 reconcile the two: the sign depends on network centralisation and the shape of starting estimates (skewed starts favour centralised weighting). Theory, simulation and four datasets, 2,885 subjects [b05, V]. Kao, Berdahl and Couzin 2018: distribution-based corrected estimators stay robust under influence; 812 people over five jar datasets [b06, V]. Frey and van de Rijt 2021: sequential choice with visible tallies makes individual votes better but majorities worse; early errors cascade on hard questions [b07, M].

**Aggregation beyond the mean.** Prelec, Seung and McCoy 2017, Surprisingly Popular: pick the answer more popular than people predicted. Cut error 21.3% vs majority, 24.2% vs confidence-weighted, 22.2% vs advanced weighted (Wikipedia figures; paper paywalled) [a12 M, a04 M, b08 V partial]. It needs a minority that knows the truth and knows the majority is wrong.

**Crowd within.** Vul and Pashler 2008: averaging one person's two guesses beats one guess, more if the second comes 3 weeks later [b26, M]. Replication in section 5.

**LLM turn (2022-2026).** Self-consistency (Wang 2023) made the single-model crowd standard. Then a split opened: more agents (Li 2024) and mixture-of-agents (Wang 2024) on one side; correlated-error measurement (Kim 2025), "consensus is not verification" (Denisov-Blanch 2026) and "nine judges, two effective votes" (Kohli 2026) on the other. Section 6 covers them.

## 3. Core findings with exact numbers

Status: E established (2+ independent sources), S single-source, C contested. K ids are claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Galton ox crowd close to truth | 787 cards; median 1208 (not 1207); truth 1197 (not 1198); error 11 lb (~1%); mean 1197 exactly | Galton 1907 via Wallis 2014 [a01-a03] | S (K01); founding anecdote |
| Condorcet majority | n=3, p=0.8 gives 0.896; p<0.5 gets worse; correlation caps below 1 | Condorcet; Ladha 1992 [a05, b25, a25, c16] | E (K02) |
| Correlated majority ceiling | p=0.69: rho 0 gives 1.0; rho 0.1 ceiling 0.887; rho 0.2 0.805; rho 0.3 0.761. p=0.6, rho 0.1: 0.736. p=0.8, rho 0.1: 0.975; rho 0.2: 0.92. At rho 0.05: 0.800/0.860/0.898/0.943 at n=5/11/21/101 | Own beta-binomial calc [d11]; Kaniovski 2009 [d10] | E as math (K21); exchangeable model, our calculation |
| Ceiling is the all-wrong rate | 67 models, 21 providers. MATH-500 best single 0.836, oracle 0.948, all-wrong 0.052. GPQA-D (52 models) best 0.846 vs oracle 1.000. code_contests (18) 0.825 vs 0.921. Mean pairwise rho 0.464; pairwise rho does not identify the all-wrong rate | Chen 2026 [d04] | E with d11 (K21); single-author preprint |
| LLM errors strongly correlated | 349 LLMs, 12,032 MC items; 71 LLMs, 14,042 (HELM); agree ~60% when both wrong (chance 33%); mean pair 0.423 on HF; some pairs 0.97; features explain 34-62% | Kim et al. 2025 [a16, b19, c14] | E (K03) |
| Judge favours similar models | Pearson r=0.84 judge score vs similarity; Qwen2.5-72B scores Qwen2.5-7B 71% vs Llama-3.1-70B 67% (true MCQ accuracy 41% vs 51%) | Goel et al. 2025 [b21] | E with Kim (K03) |
| Effective voters far below nominal | 9 judges from 7 families: Kish n_eff 2.18 (CI 2.07-2.31), independence ratio 0.391; 17 VLMs: participation ratio 2.86, within-family r 0.67 vs cross-family 0.53 | Kohli 2026 [c16]; Hidden clones 2026 [a24] | E (K04) |
| Panel does not beat best member | MNLI 72.0 vs best 71.8; SNLI 77.7 vs 84.2; AlphaNLI 88.7 vs 91.2; smarter aggregation closed at most 11% of the gap | Kohli 2026 [c17] | S |
| Self-consistency gain | PaLM-540B GSM8K 56.5 to 74.4 (+17.9); SVAMP +11.0; AQuA +12.2; StrategyQA +6.4; ARC-c +3.9 | Wang 2023 [a14, c19] | E (K05) |
| More agents (vote) | 40 agents: GSM8K +12 to +24; MATH +6 to +10; MMLU +5 to +11; HumanEval +4 to +9; Chess +1 to +4; Llama2-13B at 15 agents = Llama2-70B single | Li 2024 [a15, b14] | E (K05); body numbers not re-seen by critique |
| Vote fails without verification | 5 benchmarks, 25x cost, no consistent gain; MATH plurality-wrong 3.9-25.8%; top wrong answer is 65-87% of wrong responses; temp 0.7 to 1.0 flips the plurality in only 2.9% of pairs | Denisov-Blanch 2026 [a18, a19] | E (K06), with d03, d08, d16 |
| Sentiment ensembles | bagging/vote within 0.00-0.01 of best single | Lefort 2024 [c18] | S |
| Heterogeneity vs clones (deliberation) | consensus error 0.164 vs mean 0.195 (d=0.40); clones: Anthropic z=1.22, d=0.087; OpenAI d=0.144; Google d=0.062; heterogeneous d=0.26 | Barrera-Lemarchand 2026 [a23, c11-c13] | E with c09, a24 (K07); preprints |
| Humans keep gaining, LLM groups flatten | LLM group accuracy flat with size; human groups keep gaining; hybrid up to size 4; ExpertiseTree hybrid 0.73-0.83 vs simple average 0.50-0.80 | Abels and Lenaerts 2025 [c09, c10] | S |
| Mixing models can lose to repeating the best | Self-MoA +6.6 AlpacaEval LC (65.7 vs 59.1), +3.8% average; only 2 of 13 mixes beat Self-MoA (+0.17, +0.35) | Li et al. 2025 [b18, c23, d12] | C (K08) |
| Quality beats diversity in a regression | t=a*q+b*d: MMLU a=2.558 b=1.841; CRUX 4.548/1.421; MATH 4.719/2.839 | Li et al. 2025 [d12] | C (K08) |
| Heterogeneous debate helps | Heter-SoM +6.4%, Heter-EoT +8.2% over single-model averages (vs average of the two, not the better one) | Zhang 2025 [b17] | S |
| Prompt diversity does not help a vote | gpt-oss-120b, N=8, 50 problems, p ~0.69, baseline 39.7/50 (sd 1.7); prompt mixes 36-40; error correlation mean -0.258 (all negative) | Nitarach 2026 [d01] | C (K20) |
| Prompt diversity helps pass@k not vote | GPT-4o-mini: +10.8% EM@100 MMLU-Pro, +9.6% MATH, +9.5% Pass@100 MBPP, +4.7% HumanEval; irrelevant-text control no gain; no consistent majority-vote gain | Wang 2025 [d03] | C (K20) |
| Persona error correlation | r=0.388 practitioner vs 0.461 lay (~19% lower); ensemble gain +5.0 vs +3.6; no same-prompt baseline | Upravitelev 2026 [d02] | C (K20) |
| Debate no better than vote | Qwen2.5-7B, 7 benchmarks: single 0.7205; vote 0.7691; debate T=2 0.7377, T=3 0.7112, T=5 0.7050; centralised T=2 0.6551. GSM8K 6 responses: debate 83.2 vs SC 85.3 | Debate or Vote 2025 [c21]; Huang 2023 [c20]; Smit 2024 [b15]; Wang 2024 [b16] | E (K11) |
| Blind revision beats peer-visible | Ministral GSM-Hard round 3: 48.3 vs 20.7 (p<0.001); Qwen MMLU-Hard 66.7 vs 60.7; Qwen GSM 61.0 vs 58.8; agents adopt majority 85.5% (Qwen MMLU-Hard); random rationales as good as peers | Bertalanic 2026 [d05] | S (K24) |
| Vote vs consensus by task | voting +13.2% on reasoning; consensus +2.8% on knowledge; more rounds before voting hurt | Kaesberg 2025 [b23] | S (K19) |
| Crowd within | Immediate N=471: MSE average 541 vs guess 1 589 (dz=0.40, CI 0.31-0.49); guess 2 615. Delayed 3 weeks N=140: 467 vs 517 (dz=0.34); guess 2 589. Second guess worse than first (dz -0.10) | Steegen 2014 [b01] | E (K12) |
| Crowd-within prior replications | of 4 earlier tries: 2 clear, 1 borderline, 1 unpublished failure | Steegen 2014 [b02] | E, mixed |
| Skewed errors need robust aggregator | Swiss murders (true 198): mean 838 (+323%), geometric 174 (-12%), median 170 (-14%). Pop. density (true 184): mean 2,644 (+1,337%), median 130. Mean beat a random first guess only 21.3% of time; log-scale mean 77.1% | Lorenz 2011 [a08] | E (K13) |
| LLM numeric guesses | median of 30 beats greedy, mode and mean; median of 5 beat SC at 30 on two sets; 15 post-cutoff questions included. Mixtral-8x22B normalised error median/SC/mean/greedy 1.33/33.66/55.73/4.79 | Chuang 2025 [d06] | S (K26) |
| Deterministic multi-model median | Amazon price relative error 88% to 45% (p=0.025); temperature sampling of one model no better | Talebirad 2026 [c24] | S |
| LLM forecast crowd ~ human crowd | 12 LLMs, 31 questions: Brier 0.20 vs human 0.19 (925 forecasters), t(60)=0.19, p=0.85; no-info 0.25; best single GPT-4 0.15; acquiescence above 50% | Schoenegger 2024 [a13, b12, c01, c02] | S (K15) |
| Anchoring on shown crowd median | GPT-4 Brier 0.17 to 0.14 (p=0.003); Claude 2 0.22 to 0.15 (p<0.001); update vs distance r=0.88/0.87; gain 17-28% | Schoenegger 2024 Study 2 [b13, c03] | S (K17) |
| Learned aggregator | 15 LLMs, 254 questions, clean subset 94: logistic Brier 0.241, MLP 0.264, mean 0.313; best single ~0.284 (Opus 4.6; Sonnet 4.6 0.273 on the 208 set); mean accuracy 0.511 vs MLP 0.606 | Douven 2026 [a20, c04, c06] | S, needs labels |
| Contamination | cloud-vs-local gap 35.8% (208 items) to 8.9% (94 clean); crowd below market at cutoff | Douven 2026 [c05, c26] | S (K16) |
| Label-free weights | OW/ISP correct 5.22% UltraFeedback, 9.83% MMLU, 3.66% ARMMAN questions missed by majority; t=12.53/23.39/3.22 | Ai et al. 2026 [a22] | S |
| Behaviour clusters | 3 medoid models beat 25-model vote: FutureX-Past 0.302 vs 0.296, BTF-v3 0.810 vs 0.800; 88% fewer calls; medoid line-up at 88th/83rd percentile of random line-ups; most-dissimilar picks at 5th percentile (worse than random) | Chetlapalli 2026 [a21, c07, c08] | S (K18) |
| Verifier beats extra vote | k=7, 570 items: strong verifier +24.2 pp on pivotal items (CI 14.1-33.7); same-source extra draw 0.0 pp; weak verifier -11.2 pp (CI -20.9 to -1.2); LiveCodeBench weak -24.5 pp | Shu 2026 [d08] | E with d07, d03, d16 (K22) |
| Judge selection beats vote and synthesis | diverse+judge 0.810 win rate vs single Opus; diverse+vote 0.496; diverse+synthesis 0.179; homogeneous+judge 0.512 | Maryanskyy 2026 [d07] | C on synthesis (K23); judges partly circular |
| Synthesis beats vote (one model, rephrased) | 11 calls vs 10: BBH-3 86.5 vs 80.4; MMLU-ML 92.0 vs 90.2; GPQA-D 73.2 vs 70.7; AIME 91.1 vs 85.6; LCB-Hard 62.6 vs 57.3; flips 81 beneficial vs 4 harmful | Fadnavis 2026 [d09] | C (K23) |
| Confidence is a weak signal | pair discrimination 52.2-62.3% (chance 50); P(True) cost cut 41%/46% at budget 5/10 with +1.6/+1.1 pts; adaptive stopping up to 7.9x budget cut at <0.1% loss | Taubenfeld 2025 [d13]; Aggarwal 2023 [d14] | E (K25) |
| Coverage is not accuracy | SWE-bench Lite 15.9% at 1 sample to 56% at 250 (coverage, needs a checker); vote and reward models plateau | Brown 2024 [d16]; Snell 2024 [d15] | E with d08 |
| LLM creativity homogeneity | 22 LLMs far more similar than humans (AUT t(1046)=11.0) | Wenger and Kenett 2025 [b22] | S |

## 4. Mechanisms and models

### 4.1 Error decomposition (Page's identity)
For numeric answers x_i with truth T and crowd mean m:
`(m - T)^2 = mean_i (x_i - T)^2 - mean_i (x_i - m)^2`.
Implement: collect k answers; the second term (variance) needs no truth. The first needs truth, so use it offline only. In deployment you see only the variance. High variance with a robust aggregator is fine. Zero variance proves nothing, because identical wrong answers also have zero variance.

### 4.2 Condorcet and the correlated ceiling
Binary item, k votes, per-vote accuracy p, pairwise error correlation rho. Beta-binomial model (exchangeable votes): draw an item-level success rate q ~ Beta(a, b) with mean p and a+b = (1-rho)/rho; votes are Binomial(k, q). Majority accuracy = P(Binomial(k, q) > k/2) averaged over q. As k grows this tends to P(q > 0.5), the ceiling [d11]. Example: p=0.69, rho=0.1 gives 0.887. Past about k=20 at rho 0.1, extra votes add almost nothing.

Two caveats that matter for engineering.
(a) Real items are not exchangeable. Some items have q near 0 for every model. The true cap for any method that outputs one sample's answer is 1 minus the all-wrong rate (0.052 on MATH-500), and pairwise rho does not identify it [d04]. Measure the all-wrong rate on pooled samples; do not infer it from rho.
(b) Multi-class: the plurality answer only has to beat each wrong answer, not reach 50%. Wrong answers that scatter lose to a right answer with a 30% share. That is why math voting works and truthfulness voting does not [d03 Prop 5.1; a18]: the vote works when the correct answer is the single mode.

### 4.3 Effective number of voters
Equal weights: n_eff = n / (1 + (n-1) * rho_bar). Kish form for weights: n_eff = (sum w_i)^2 / sum w_i^2. Participation ratio = (sum of eigenvalues)^2 / sum of squared eigenvalues of the error-correlation matrix. Kohli: 9 judges give 2.18 [c16]; 17 VLMs give 2.86 [a24]. Implement: build a binary item-by-sample error matrix on a calibration set, compute the correlation matrix, report n_eff, and cap the gain you claim from a vote at n_eff voters.

### 4.4 Why self-consistency works despite correlation
Wrong reasoning paths scatter over many wrong answers; right paths converge on one. Plurality picks the right one if it is the mode [a14, c19]. It needs an answer string that can be compared. Failure mode: when a misconception is shared, the wrong answer is the mode. The top wrong answer was 65-87% of wrong MATH responses [a18].

### 4.5 Pivotal items and where a verifier acts
With k=7, only items where 3 or 4 votes are correct can be changed by one more voter. Replacing one vote with a strong independent verifier changed outcomes only there: +24.2 pp on pivotal items. A same-source extra draw gave 0.0 [d08]. Implement: after k votes compute the split. Lopsided (7-0, 6-1): accept. Near split (3-4): spend the next tokens on a separate verifier or an executable check, not on more draws [K22].

### 4.6 Aggregators and when each fits
- Mean: fine when errors are symmetric and bounded. Fails with order-of-magnitude outliers (+323% on murders) [a08].
- Median: robust to outliers; used by Galton, Schoenegger, Chuang [a01, c01, d06]. Median of 5 beat SC at 30 [d06].
- Geometric or log-scale mean: right-skewed positive quantities (77.1% beat the first guess) [a08].
- Plurality: categorical answers. Valid only if the correct answer is the mode and a checker exists [a18].
- Confidence-weighted: saves samples [d13]; fails as a truth signal [a18].
- Surprisingly Popular: voters also predict others' answers; needs a knowing minority [a12, b08]; no LLM test found; inverse-SP reached 80% on HLE yet was at chance elsewhere [a18].
- Learned logistic aggregator: needs labelled history; the useful signal was model disagreement [a20, c06].
- Label-free OW / ISP weights: use each model's expected accuracy and correlation [a22].
- Kao-style distribution correction: needs 20 to 175 training samples by estimator [b06].

### 4.7 Social influence model
Each round, voter i moves toward a weighted mean of others' answers. Decentralised, symmetric weights shrink variance; if the start mean is near truth this helps (-10% mean error [b04]). Centralised weights make the result follow the central voter (-43% or +19% by where they start). Skewed starts favour centralised weighting [b05]. For LLM agents shown peers' answers the evidence leans to harm: agents copy the majority 85.5% of the time and random unrelated rationales work as well as peer ones [d05]. Implement: in S5, show the failing output, not other samples' answers.

### 4.8 Crowd within
Two guesses from one person have partly independent error. Averaging cuts error: immediate dz 0.40, delayed 0.34 [b01]. Delay helps because the second guess is less tied to the first. For an LLM the analogue of delay is a changed frame or context. This is untested [K12, K26].

### 4.9 Diversity of search (Hong-Page)
Each agent hill-climbs with its own ordered heuristic list. The team passes the current point from agent to agent until nobody improves it. Performance rises when the agents' sets of local optima differ. Implement as a fixed set of distinct strategies applied in rotation, stopping when none improves the candidate. Not tested on LLM agent search (critique gap 9).

## 5. What holds up

**Holds (E).**
- Averaging helps when errors are random: Galton, the Lorenz baseline, the Steegen replication [a03, a08, b01].
- Correlation caps vote gain (math and measurement) [d10, d11, c16; K21].
- LLM errors are correlated, more so for similar models [K03]. Independent support: Kim, Goel, Denisov-Blanch, Kohli.
- Self-consistency works on checkable answers [K05].
- Voting without a verifier fails on truthfulness [K06].
- Debate does not beat voting at equal compute [K11].
- Skewed data need median or geometric mean [K13].
- Crowd within replicates in the best test [K12].
- A separate verifier beats more same-model votes on pivotal items [K22].

**Failures and boundary conditions.**
- Crowd within: of four earlier immediate replications, 2 clear, 1 borderline, 1 failed [b02]. Steegen's preregistered N=471 settles the immediate effect at dz=0.40, but it is one lab family, students, 8 trivia items.
- Social influence: Lorenz (harm) vs Becker 2017 and Almaatouq 2021 (help under decentralisation or the right weights). The sign is set by network structure and weighting [K10].
- Hong-Page needs a finite heuristic pool and identical perspectives [a10, b09].
- Heterogeneity: Self-MoA beats Mixed-MoA by 6.6 points when members differ in quality [b18]. Mixed models win at matched quality (+0.027 at k=3 [d04]) and with a good selector [d07]. No numeric quality-gap threshold found [K08].
- Prompt diversity: no vote gain where error correlation is already near zero (AIMO mean -0.258; diverse prompts cost 0.3 to 3.7 points [d01]); helps pass@k and best-of-N but not majority vote [d03]; persona frames lower correlation by about 19% but have no equal-token baseline [d02] [K20].
- Sentiment ensembles gained 0.00 to 0.01 [c18].
- Learned aggregators and Surprisingly Popular need labelled data or an expert minority.
- Contamination inflates LLM crowd skill [c05].

**Interventions that worked.**
- Median aggregation for numerics [d06].
- Separate strong verifier on pivotal items [d08].
- Judge selection over a diverse pool [d07, 0.810].
- Isolated (blind) revision [d05].
- Adaptive stopping on the answer distribution (up to 7.9x fewer samples) [d14].
- Mixed human-LLM crowds [c09].
- Weights from model disagreement [c06].
- Behaviour-clustered line-ups [c08], modest.

**Interventions that did not work.**
- Debate (G9 stands).
- Confidence weighting as a truth signal [a18, d13].
- Same-source extra votes on shared-error items (0.0 pp) [d08].
- Picking the most dissimilar models: worse than random [c08].
- Smarter aggregation of a correlated panel: at most 11% of the gap closed [c17].
- Weak verifiers: -11.2 pp and -24.5 pp [d08].
- Peer rationales in revision [d05].

## 6. Language models

**One model, many samples.** Self-consistency: +17.9 on GSM8K for PaLM-540B [a14]. Agent Forest: gains by task listed in section 3; small models at 15-20 samples match a 70B single [b14]. Gains are larger on harder tasks and weaker models, and taper at extreme difficulty. Both need exact answers.

**Correlation numbers.** About 60% agreement when both are wrong; pairs up to 0.97 [a16]. Pairwise rho 0.382 to 0.464, within-family 0.528 [d04]. VLM cross-family r=0.53 vs 0.67 within [a24]. Nine judges act as 2.18 voters [c16]. Even random strings gave correlated outputs across models [a19]. One counter-case: AIMO samples from one model at high temperature on hard problems had slightly negative mean error correlation (-0.258) [d01]. So correlation depends on task and temperature. Do not assume one number.

**What breaks a vote.**
1. No verifier plus a shared misconception: no consistent gain at 25x cost [a18].
2. A panel that is not better than its best member [c17].
3. Hidden "misleading" items: 2.5% of VQAv2, best model 78.9%, calibrated vote 0.0%, family-hierarchical voting 26.0% [a24].

**What changes it, and by how much.**
- Different model families: correlation drops (0.53 vs 0.67) [a24]; deliberation d=0.26 for heterogeneous vs 0.06-0.14 for clones [c12]. Mixing weak with strong loses (-3.8% average [b18]).
- Prompt or persona diversity: contested (section 5).
- Median instead of mean on numerics: normalised error 0.49 vs 3.12 for LLaMA-3.1-70B on MARBLES [d06].
- Verifier on split items: +24.2 pp [d08].
- Judge selection: 0.810 vs vote 0.496 [d07].
- Trace-level synthesis over rephrasings: AIME 91.1 vs 85.6, GPQA 73.2 vs 70.7 [d09]. Contradicted by synthesis losing in [d07]; model, task and aggregator differ.
- Isolated revision over peer-visible: up to 27.6 pp [d05].
- Stopping rules: up to 7.9x budget cut at under 0.1% loss [d14].
- Confidence weighting: about 40% fewer samples [d13].

**Debate.** Voting beats debate (0.769 vs 0.738 at T=2, Qwen2.5-7B) [c21]. Debate among models of unequal strength can flip right to wrong [c22]. Voting +13.2% on reasoning, consensus +2.8% on knowledge [b23]. Du 2023 (the original debate paper) was not read [b24].

**Forecasting.** The 12-LLM median Brier 0.20 matched 925 humans at 0.19, with acquiescence bias [c01, c02]. Models follow shown medians in proportion to distance (r=0.87-0.88) [c03]. Douven: learned aggregation 0.241 vs mean 0.313; contamination makes cloud models look better; the crowd stayed below the market at cutoff [a20, c05].

**Mixed human and LLM.** Hybrid ensembles beat pure groups up to size 4 [c09].

**Open end.** Nearly all tests use multiple choice, exact-answer math or short numerics. Open-ended reasoning traces are untested for independence (critique).

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. **Measure before trusting a vote.** Estimate pairwise error agreement, n_eff and the all-wrong rate on a calibration set. Cap claimed vote gain at n_eff. | G4; S0 class record (memory) | [E] | K02, K03, K04, K21; c16, d04, d11, a16.
2. **Vote only where a checker or a single-mode answer exists.** Without one, a vote is a hint (G4 stands). Route to a separate verification or executable check, not more draws. | G4, S4, S7 | [E] | K05, K06; a14, a18, d03, d16.
3. **On split items (about 3-4 of 7), spend tokens on a verifier or judge from a different build than the generator, not on more same-model votes.** A weak verifier is worse than none, so validate the verifier on a small set first. | S7, S8, G5 | [E] | K22; d08, d07, d03, d16.
4. **Aggregate numeric answers by median** (or geometric mean for positive right-skewed quantities). Never a plain mean when order-of-magnitude outliers are possible. | S7 | [E] | K13; a08, d06.
5. **No debate; vote wins at equal cost.** (G9 stands.) | G9 | [E] | K11; c21, c20, b15, b16.
6. **Never use stated or sampled confidence to resolve a shared-error split.** Agreement fraction may be used to stop early on easy items only. | G4, G12 | [E] | K25; d13, d14, a18.
7. **Never treat a panel of model judges as independent voters.** Judges favour models like themselves. | G4, G5 | [E] | K03; b21, a17, c16.
8. **Benchmark crowd gains on post-cutoff or generated items.** Contamination hides the real effect. | G7 | [S] but cheap and safe | K16; c05.

### Test first

| # | Candidate | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Prompt or frame diversity vs plain temperature sampling at equal tokens, measured in error correlation and vote accuracy | S3 | [C] | K20; d01, d02, d03, d09 |
| T2 | Adaptive stopping on answer distribution (stop at a lopsided split) | G12, S3 | [S] for our setup | K25; d14, d13 |
| T3 | Verifier on pivotal splits vs 2k extra votes at equal tokens | S7, S8 | [E] direction; our magnitude untested | K22; d08 |
| T4 | Blind vs peer-visible revision | S5, G4 | [S] | K24; d05 |
| T5 | Median of 5 vs mean vs mode on numeric items | S7 | [S] | K26; d06 |
| T6 | Trace-level synthesis vs vote vs judge selection | S7 | [C] | K23; d09, d07 |
| T7 | Different strategies or roles vs best-only repeated | S3, O1-O8 | [C] | K07, K08; c12, b18, d04, d12 |
| T8 | Crowd within: reframed second sample averaged with first, vs same-prompt second | S3, memory | [S] | K12, K26; b01 |
| T9 | Hong-Page strategy rotation on search tasks | S3, S6 | [C] | K09; a10, b09 |
| T10 | Surprisingly-Popular analogue: samples predict others' answers; gap flags shared bias | S7 | [S], human only | K14; a12, a18 |
| T11 | Learned or label-free weights using the class record | S0, memory | [S] | K14; a20, a22 |
| T12 | Vote vs consensus by task type | S0 mode | [S] | K19; b23 |

## 8. Concrete tests on our bench

All arms at equal total tokens (prompts plus completions plus setup, G7). Log per SCHEMA section 6.

1. **Correlation audit.** Items: 100 or more with exact answers (ARC-style, BrainTeaser), plus a set with no checker. Arms: k=8 temperature samples; k=8 frame-diverse samples. Metric: pairwise error correlation, n_eff, all-wrong rate, realised vote gain vs the beta-binomial curve. Expected: rho 0.1 to 0.5; realised gain below the independent prediction; ceiling set by the all-wrong rate.
2. **Frame vs temperature diversity.** Items: those with measured rho above 0.1 (else skip). Arms: k same-prompt samples; k samples over 4-5 frames (restate, example-first, work backwards). Metric: majority accuracy and rho. Expected: gain only where rho was high; no gain or a loss if rho is near zero [d01]; per-frame accuracy within 3 points of the plain prompt.
3. **Verifier on splits.** Items: tasks where the vote splits 3-4 of 7. Arms: (a) 7 votes plus one verifier call; (b) 7 votes plus extra draws at the same tokens; (c) 7 votes alone. Verifier from a different build, validated on 30 items first. Metric: accuracy on pivotal items. Expected: +10 to +24 pp for a strong verifier, about 0 for extra draws, negative for a weak verifier [d08].
4. **Blind vs peer revision.** Items: 100 with a check. Arms: revise with failing output only; output plus other samples' answers; output plus random unrelated rationales (noise control). Metric: accuracy after round 2 and right-to-wrong flips. Expected: blind >= peer; peer = noise [d05].
5. **Numeric aggregation.** Items: 50 numeric estimates (Fermi-style, post-cutoff). Arms: greedy; mean of 5; median of 5; mode of 5; median of 15. Metric: median normalised error. Expected: median of 5 beats mean by a large factor on skewed items [d06].
6. **Stopping rule.** Items: easy and medium exact-answer items. Arms: fixed k=8; stop when the leader is 3 votes ahead of the runner-up. Metric: accuracy and tokens. Expected: 2x or more fewer samples at under 0.5 pp loss [d14]; log how many shared-error items stop early wrongly.
7. **Synthesis vs vote vs judge.** Items: 60 mixed. Arms: 10-call vote; 5 rephrasings x 2 plus synthesis; 10 samples plus one judge. Metric: accuracy. Expected: contested; a win must beat the vote at equal tokens on two item types.
8. **Heterogeneity.** Items: 80 exact-answer. Arms: best model x k; two near-equal models x k/2; best plus weak. Metric: accuracy. Expected: mixing wins only when models are within a few points [d04, d12].
9. **Crowd within.** Items: 80 numeric. Arms: average of 2 same-prompt samples; average of 2 differently framed samples; single sample. Metric: squared error. Expected: reframed >= same-prompt >= single (human dz 0.34-0.40 [b01]).
10. **Surprisingly-popular flag.** Items: 80 with known answers and a likely shared misconception. Arms: plain vote; vote plus a "predict the most common answer others would give" flag. Metric: AUC for detecting wrong-mode items; accuracy after rerouting. Expected: small; inverse-SP was at chance outside one benchmark [a18].

## 9. What does not transfer, and why

- **Page's identity as proof of benefit.** It guarantees the crowd beats the average member, not the best one. A strong single member can beat the panel (72.0 vs 71.8 on MNLI, worse on SNLI) [c17].
- **Hong-Page "diversity trumps ability".** Holds for search with finite heuristic pools, not for voting on a fact [b09]. For one model in several roles the "diversity" lives in prompts, not in independent knowledge.
- **Human social-influence results.** Humans in networks hold independent private beliefs. LLM copies share weights and copy the majority 85.5% of the time [d05].
- **Surprisingly Popular.** Needs a minority that knows the truth and predicts the majority. LLM samples have no such minority; no LLM test found.
- **Crowd within by delay.** Human delay causes forgetting and a fresh view. An LLM call is already context-free, but samples share weights, so the independence it buys is limited. Untested for LLMs.
- **Large human crowds.** Humans keep gaining with size; LLM groups flatten [c09]. Do not assume the same returns.
- **Learned aggregators.** Need labelled history for the same task type; a new problem has none [c04].
- **Forecasting parity.** 31 questions, different families, contamination possible [c01, c05]. It supports diverse-model crowds, not resampling one model.
- **Multi-agent mixing results.** Often measured with an LLM judge or synthesis rather than a code vote, and against the average of members, not the best [b17].

## 10. Open questions

1. Does resampling one model with prompt or frame diversity cut error correlation enough to restore vote gain at equal tokens? (Contested, K20.)
2. With no verifier, what is the best use of extra tokens: retrieval, a different-frame critique, a separate verifier? No head-to-head found.
3. Does realised vote gain track n_eff or participation ratio across tasks? Only indirect evidence (d04, d11).
4. What quality gap makes mixing models lose? No numeric threshold. Transfer to one model in several roles is untested.
5. Is there any truth signal for shared error (Surprisingly Popular, predicting others' answers)? No LLM study found. The search budget ran out, so this is not proof of absence.
6. Reframed or spaced second sample vs same-prompt second sample (crowd within) for LLMs.
7. Does the Hong-Page effect appear in LLM agent search with distinct strategies?
8. Best aggregator for probabilities (extremising, geometric mean) under LLM acquiescence, on post-cutoff items.
9. Open-ended reasoning traces: independence unmeasured.
10. Do the 2026 preprints hold? Most are single studies with small effects.

## 11. Sources

- [V] Wallis (2014) Revisiting Francis Galton's Forecasting Competition. https://arxiv.org/abs/1410.3989 (a02, a03)
- [M] Galton (1907) Vox Populi, Nature 75:450-451. https://galton.org/essays/1900-1911/galton-1907-vox-populi.pdf (a01, b11; scan with no text layer)
- [M] Wikipedia, Wisdom of the crowd. https://en.wikipedia.org/wiki/Wisdom_of_the_crowd (a04)
- [V] Wikipedia, Condorcet's jury theorem. https://en.wikipedia.org/wiki/Condorcet%27s_jury_theorem (a05, b25)
- [V] Lorenz, Rauhut, Schweitzer, Helbing (2011) How social influence can undermine the wisdom of crowd effect. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3107299/ (a06-a09, b03)
- [V] Hong and Page (2004) Groups of diverse problem solvers can outperform groups of high-ability problem solvers. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC528939/ (a10, a11); [M] https://www.pnas.org/doi/10.1073/pnas.0403723101 (b10)
- [M] Prelec, Seung, McCoy (2017) Surprisingly popular, Nature 541. https://doi.org/10.1038/nature21054 (a12); [V partial] https://www.nature.com/articles/nature21054 (b08)
- [V] Schoenegger, Tuminauskaite, Park, Tetlock (2024) Wisdom of the Silicon Crowd. https://arxiv.org/abs/2402.19379 (a13, b12, b13, c01-c03)
- [V] Wang et al. (2023) Self-consistency. https://arxiv.org/abs/2203.11171 (a14, c19)
- [V] Li et al. (2024) More Agents Is All You Need. https://arxiv.org/abs/2402.05120 (a15, b14)
- [V] Kim, Garg, Peng, Garg (2025) Correlated errors in LLMs. https://arxiv.org/abs/2506.07962 (a16, a17, b19, b20, c14, c15)
- [V] Denisov-Blanch et al. (2026) Consensus is not verification. https://arxiv.org/abs/2603.06612 (a18, a19)
- [V] Douven (2026) Wisdom of LLM crowds. https://arxiv.org/abs/2607.18269 (a20, c04-c06, c26)
- [V] Chetlapalli et al. (2026) Diverse by reasoning. https://arxiv.org/abs/2608.24001 (a21, c07, c08)
- [V] Ai et al. (2026) Beyond majority voting. https://arxiv.org/abs/2510.01499 (a22)
- [V] Barrera-Lemarchand, Sigman, Navajas (2026) Wisdom of artificial deliberative crowds. https://arxiv.org/abs/2609.22497 (a23, c11-c13)
- [V] Hidden clones (2026). https://arxiv.org/abs/2603.17111 (a24)
- [V] Latent dimension of Condorcet's theorem for AI advisers. https://arxiv.org/abs/2609.14438 (a25)
- [M] Ladha (1992) Condorcet jury theorem with correlated votes. https://doi.org/10.2307/2111584 (a26)
- [M] Frey and van de Rijt (2021) Social influence undermines the wisdom of the crowd in sequential decision making. https://doi.org/10.1287/mnsc.2020.3713 (a27, b07)
- [M] Examining independence in ensemble sentiment analysis (SSRN). https://doi.org/10.2139/ssrn.5199096 (a28)
- [V] Steegen et al. (2014) Measuring the crowd within again. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00786/pdf (b01, b02)
- [V] Becker, Brackbill, Centola (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5495222/ (b04)
- [V] Almaatouq et al. (2021). https://arxiv.org/abs/2006.12471 (b05)
- [V] Kao, Berdahl, Couzin (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC5938592/ (b06)
- [V] Karge (2025) When diversity in voting trumps ability. https://doi.org/10.1017/epi.2025.10042 (b09)
- [V] Smit et al. (2024) Should we be going MAD? https://arxiv.org/abs/2311.17371 (b15)
- [V] Wang et al. (2024) Rethinking the bounds of LLM reasoning. https://arxiv.org/abs/2402.18272 (b16)
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788 (b17)
- [V] Li et al. (2025) Rethinking Mixture-of-Agents. https://arxiv.org/abs/2502.00674 and https://arxiv.org/html/2502.00674v1 (b18, d12)
- [V] Goel et al. (2025) Great models think alike. https://arxiv.org/abs/2502.04313 (b21)
- [V] Wenger and Kenett (2025) We're different, we're the same. https://arxiv.org/abs/2501.19361 (b22)
- [V] Kaesberg et al. (2025) Voting or consensus? https://arxiv.org/abs/2502.19130 (b23)
- [M] Du et al. (2023) Multiagent debate. https://arxiv.org/abs/2305.14325 (b24)
- [M] Vul and Pashler (2008) Measuring the crowd within. https://doi.org/10.1111/j.1467-9280.2008.02136.x (b26)
- [V] Abels and Lenaerts (2025) Wisdom from diversity. https://arxiv.org/abs/2505.12349 (c09, c10)
- [V] Kohli (2026) Nine judges, two effective votes. https://arxiv.org/abs/2605.29800 (c16, c17)
- [V] Lefort et al. (2024) Independence in ensemble sentiment analysis. https://arxiv.org/abs/2409.00094 (c18)
- [V] Huang et al. (2023) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c20)
- [V] Debate or Vote (2025). https://arxiv.org/abs/2508.17536 (c21)
- [V] Wynn, Satija, Hadfield (2025) Talk isn't always cheap. https://arxiv.org/abs/2509.05396 (c22)
- [V] Wang et al. (2024) Mixture-of-Agents. https://arxiv.org/abs/2406.04692 (c23)
- [V] Talebirad et al. (2026) Wisdom of the machines. https://ifaamas.org/Proceedings/aamas2026/pdfs/MTWR9974.pdf (c24)
- [M] Verga et al. (2024) Replacing judges with juries. https://arxiv.org/abs/2404.18796 (c25)
- [V] Nitarach (2026) Model capability dominates. https://arxiv.org/html/2603.27844v1 (d01)
- [V] Upravitelev et al. (2026) Multiperspectivity. https://arxiv.org/html/2603.22103v1 (d02)
- [V] Wang et al. (2025) Effect of sampling diversity in scaling LLM inference. https://arxiv.org/html/2502.11027v4 (d03)
- [V] Chen (2026) When does combining language models help? https://arxiv.org/html/2606.27288v1 (d04)
- [V] Bertalanic and Fortuna (2026) The cost of consensus. https://arxiv.org/html/2605.00914v1 (d05)
- [V] Chuang et al. (2025) Probing LLM world models. https://arxiv.org/html/2501.17310v4 (d06)
- [V] Maryanskyy et al. (2026) When agents disagree. https://arxiv.org/html/2603.20324v2 (d07)
- [V] Shu (2026) When verifiers vote backwards. https://arxiv.org/html/2609.26144v1 (d08)
- [V] Fadnavis et al. (2026) Beyond consensus. https://arxiv.org/html/2605.29116v1 (d09)
- [V abstract and intro] Kaniovski and Zaigraev (2009) Optimal jury design. https://Serguei.Kaniovski.wifo.ac.at/fileadmin/pdf/condorcet_robust.pdf (d10)
- [V] Own calculation, D:/research_scratch/A17.01/tmp/ladha_A17.01.py (d11)
- [V] Taubenfeld et al. (2025) Confidence improves self-consistency. https://arxiv.org/html/2502.06233v2 (d13)
- [V abstract only] Aggarwal et al. (2023) Let's sample step by step. https://arxiv.org/abs/2305.11860 (d14)
- [V abstract only] Snell et al. (2024) Scaling test-time compute. https://arxiv.org/abs/2408.03314 (d15)
- [V abstract only] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 (d16)
