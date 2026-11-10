# Epistemic diversity: deep document

*Subfield F03.06, sociology of knowledge. Built from evidence_a-d.jsonl (a01-a27, b01-b30, c01-c28, d01-d19), claims.jsonl (K01-K31) and critique.md in this folder. Schema references are to SCHEMA.md v0.2 (G1-G12, S0-S9, O1-O8, section 4b). Where this document and a source disagree, the source wins; where our own bench disagrees with this document, our bench wins (SCHEMA rule 8.3).*

## 1. What it is

Epistemic diversity asks one question: when a group searches for a solution, does it help to have members who think differently, and when does it beat having the most able members?

Three families of work answer it.

1. **Formal models of search.** Hong and Page (2004) put agents on a landscape. Each agent has a perspective (how the problem is encoded) and a heuristic (how it moves). A group relays the problem from one agent to the next. A group gets stuck only where every member is stuck. Weisberg and Muldoon (2009) put scientists on a landscape of "approaches" with hills of significance. Lazer and Friedman (2007) used NK landscapes with social learning. These are simulations.
2. **Critique of those models.** Thompson (2014), Reijula and Kuorikoski (2021), Grim et al. (2019), Alexander et al. (2015), Romaniega (2025). They test when the result holds.
3. **Empirical work.** Human team meta-analyses (small effects). Since 2023, LLM studies: ensembles of different models, mixtures of agents, debate, prompt diversity, persona diversity, error correlation, and homogeneity of model outputs.

Why it matters for our agent. We build one scaffolded agent on one model. The famous claim, "diversity trumps ability", suggests running varied attempts. Guardrail G4 says samples from one model are not independent. This document tests that tension. The short answer from the evidence:

- The theoretical claim is a possibility result, fragile, and partly an artefact of randomness and group size (K02, K03, K04).
- In LLM systems, **quality of the proposers and quality of the selector** matter more than diversity (K07, K16).
- Varying prompts inside one model does **not** lower error correlation (K25). Mixing different models does, a little (K09, d03), but we have one model.
- Coverage (some attempt is right) rises with the number of attempts. Selecting the right attempt is the bottleneck (K15, K16, K26).

## 2. History and theories in depth

### 2.1 Hong and Page 2001 and 2004 (a01-a04, b01)

Agents have a perspective and a heuristic. In the 2004 PNAS paper the perspective is shared and the heuristic differs. The group search is a relay: agent 1 searches until stuck, agent 2 starts from that point, and so on, until no agent can improve. The group's final point is a local optimum for every member (a01).

The computational experiment (a02): a circular landscape of n=2,000 points, values uniform on [0,100]. Each heuristic is an ordered set of k=3 step sizes drawn from {1..l}. With l=12 there are 1,320 heuristics; with l=20 there are 6,840 (20x19x18). Table 1, mean of 50 trials:

- 10 agents, l=12: best-10 group 92.56 (sd 0.020), random-10 group 94.53 (sd 0.007). Diversity 70.98% vs 90.99%.
- 20 agents, l=12: 93.78 vs 94.72. The gap shrinks as the group grows.
- One representative run (a03): best single agent 87.3, worst 84.3, mean of best-10 87.1, mean of random-10 85.6, group values 93.2 vs 94.7, pairwise diversity 0.72 vs 0.92.

Theorem 1 (a04): with probability one there exist N1 < N such that N1 random agents beat the N1 best of N drawn agents. It rests on four assumptions, including that agents never move to a worse point and that no agent solves the problem alone. It is a limit statement with no numbers for N or N1.

Page (2007), *The Difference*, states the claim in general form (a27). Thompson quotes p. 165. We did not open it.

The 2001 bit-string version of the model had no systematic diversity advantage (b02).

### 2.2 Critique (a05-a09, a12, b02-b07)

**Thompson 2014 (a05-a07, c18).** Opened. She says Theorem 1 has little content and does not apply to the experiment. Lemma 1 is wrong unless V is one-to-one. In the limit of a huge pool the best N1 agents are clones of one agent (die example: 6 agents, N1=50, N=10,000). She reproduced the simulation and confirmed 10 random beat 10 best (n=2,000, l=20, k=3). Her diversity sums over 45 pairs: 131 for random-10, 120 for best-10. Groups built for **maximal** diversity scored below the median of 200 random groups. So diversity as defined is not the cause. Her hostility point: the diversity score is only how many of three entries differ; relabel it hostility and the same data say hostility trumps ability.

**Romaniega 2025 (a08, a09, c19).** Opened (arXiv 2307.04709 v3). Counterexamples when V is not injective, when the best agent is not unique, and for clone performance. Proves a theorem with the opposite conclusion. Says the replies of Page and of Kuehn and Singer did not answer the injectivity point. One author, preprint.

**Reijula and Kuorikoski 2021 (b02-b04).** Opened. Replicated the ringworld result. The gap correlated .65 with the difference in effective group size. In nearly half of random groups the group heuristic was the full set [1..12]; only 13% of random groups had effective size below 11. The best and worst individual agents differ by 3.0 points (87.3 vs 84.3), so there is little ability to trade. On their own stairway landscape (l=3, k=12, n=2,000, 100 repetitions over 100 landscapes), high-ability groups win for small groups and simple problems; above group size 10 the random group catches up and no significant gap remains; diversity wins only when the problem needs more heuristics than any one agent holds.

**Grim et al. 2019 (a10, b05).** Abstract only. Extends the model to landscapes of varying randomness. The result is sensitive to landscape structure. Singer 2019 (b07) and Kuehn 2017 defend the diversity reading; neither was opened.

**Wallrich replication (a11).** Open mesa agent-based replication of Hong-Page and Grim et al. We read the README only; whether it reproduces the numbers is not stated.

### 2.3 Landscapes: Weisberg-Muldoon, Alexander et al., Lazer-Friedman

**Weisberg and Muldoon 2009 (a24, b10, c21, d13).** Not opened. Second-hand: followers copy successful neighbours, mavericks avoid explored ground, and a mixed population in which mavericks stimulate followers does better. **Alexander, Himmelreich and Thompson 2015 (b09, d12)** say this came from modelling errors, that seeking novelty need not be optimal, and that social learning is doubtful in complex landscapes. A re-implementation (c22, snippet only) reproduced the results but found high sensitivity to rule details. Status: **contested (K19)**. We read none of the three full texts.

**Lazer and Friedman 2007 (a25, d11).** Not opened. Second-hand via O'Brien et al. and Shore et al.: efficient networks win in the short run and lose in the long run on complex landscapes. Mason and Watts (2012), per Shore et al., found the opposite structural cause (clustering reduces exploration). Status: **contested (K29)**.

**O'Brien et al. 2025 (a23, c20).** Opened. NK landscape (N=20, K=5), 1,000 simulations per setting, social learning rate 25%, AI query probability 0.25 vs 0.75. A shared non-personalised AI (random pick among the ten best) makes agents converge; Hamming distance falls fastest and the community does worse as the query rate rises. Personalised AI preserves exploration at low query rates. The AI is a modelled oracle, not an LLM.

**Shore, Bernstein, Lazer 2015 (d10).** Human lab data. 417 individuals, 816 person-rounds analysed from 352 people, 51 runs, four 16-person networks. Clustering reduced redundant fact searching but made solution finding converge faster, including on wrong answers. Clustered networks did best overall; the ring did worst.

### 2.4 Other modelling results

- **Luan, Katsikopoulos, Reimer 2012 (b08).** Take-the-best (accurate, homogeneous) vs minimalist (less accurate, diverse) groups. Every manipulation that cut individual accuracy also raised diversity. A minimalist group of 100 still lagged a take-the-best group when cue validities differed strongly. Group accuracy peaked at an intermediate error level.
- **Approval-voting jury model (b11).** A diversity-beats-ability theorem inside a Condorcet model. Example bound: m=20, dp=0.4, p_hat=0.8, n=100, pi=0.1 gives P_min=0.85. Voting model, not search. Authors not confirmed.
- **Human meta-analyses (b12, b13, d14, d15).** See section 3.

### 2.5 The turn to LLMs (2023-2026)

Diversity moved from people to model ensembles: debate (Du 2023), mixture-of-agents (Wang 2024), heterogeneous debate (Hegazy, Zhang, ReConcile), prompt-level diversity (DIV-SE, DIPPER), then critiques (Self-MoA, Debate or Vote, correlated errors, co-failure ceiling, selection bottleneck). See section 6.

## 3. Core findings with exact numbers

Status: **est** = established (2+ independent sources agree), **single** = single source, **contested**, **human** = human only, **old** = older models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Hong-Page: random group of 10 beats best 10 on a random ringworld | l=12, n=2,000, k=3, 50 trials: 94.53 vs 92.56; 20 agents 94.72 vs 93.78 | a02, a06, b02 | est (reproduced by Thompson, Reijula-Kuorikoski, Grim) |
| Theorem is a possibility statement with a flawed lemma | needs V one-to-one; no N given; best-N are clones only with a huge pool | a04, a05, a08 | est |
| Result is partly randomness and group size, not diversity | max-diversity groups below median of 200 random groups; gap vs effective size r=.65; diversity score 131 vs 120 | a06, b02 | est |
| Individual ability barely differs in HP | best 87.3, worst 84.3 | a03, b04 | est |
| Effect is fragile to landscape | stairway: ability wins for small groups; random group catches up above size 10; 2001 bit-string model no advantage | b02, b03, a10 | est |
| Take-the-best groups beat diverse minimalist groups when validities differ | still true at group size 100 | b08 | single |
| Human team diversity: tiny effects | task-related r=.10 (35 studies); task-oriented .04 (39); job-related .05 (92); registered report 615 reports, 2,638 effects, all average abs(r)<.1 | b12, b13, d14, d15 | human, est |
| Team diversity larger on creative and R&D work | R&D .058 vs .020; creativity/innovation .056 vs .020 | d14 | human |
| MoA: mixing different models beats same-model sampling | n=6: 61.3 vs 56.7; n=3: 58.0 vs 56.1; n=2: 58.8 vs 54.5; AlpacaEval 2.0 LC 65.1 vs GPT-4o 57.5 | a15, c01 | single paper; confounded (next row) |
| The single proposer in MoA was not the best model | WizardLM-8x22B alone as proposer 63.8 > 61.3 | critique corr. 3 | est (K08) |
| Self-MoA: resampling the best model beats mixing | AlpacaEval LC 65.7 vs 59.1 (+6.6); avg +3.8 over MMLU-redux, CRUX, MATH | a13, b14, c02 | contested (K06) |
| Quality beats diversity in the MoA regression | MMLU 2.558 vs 1.841; CRUX 4.548 vs 1.421; MATH 4.719 vs 2.839; R2 .771/.685/.760; ~70 mixtures per dataset | a14, b15 | single |
| Mixing helps with complementary specialists | mixed 60.04 vs Self-MoA 59.69 (mixed task set) | c02, b16 | single |
| At matched quality a low-correlation mix beats Self-MoA slightly | +0.027 mean at k=3 (range +0.010 to +0.050; 60 of 60 positive); MATH-500 +0.020 | d03 | single |
| Compute-equalised Self-MoA depends on task | GPQA 64.1 (below zero-shot 66.7); AIME 90.0 | d06 | single |
| Cross-family debate beats same-model debate | GSM8K 91% vs 82% (3 copies), singles 78/70/64; ASDiv 94 vs singles 89/86/81 | a17, c03 | est (K09), small papers |
| ReConcile | StrategyQA 79.0 vs 72.2 (3x ChatGPT), +6.8; ANLI 57.7 vs 48.3 | b26, c10 | single paper |
| Heter-MAD | +2.7 to +8.2 over single-model MAD; avg 76.7 vs 69.9-74.3; MBPP -2.0% to -10.8% vs CoT | b25 | single |
| Debate adds little beyond voting | Qwen2.5-7B avg: single .7205, best MAD .7377, vote .7691, centralized .6551; Llama3.1-8B: .6203, .6990, .7242 | d01, b24, b22 | est |
| Original debate gain (older model) | arithmetic 67.0 to 81.8; GSM8K 77.0 to 85.0 | b23 | old; reduced by d01 |
| Persona prompts do not help | 162 personas, 2,410 MMLU questions, 4 families, no gain; auto-selection = random | b21, b22, c12 | est |
| DIV-SE: varied approaches from one model | GPT-4 Graph Coloring CoT 15, SC-10 23, DIV-SE 97; Blocksworld 3: 70/73/94; Blocksworld 4/5: 40/41.2/69.6 | a16, b27 | est but confounded (algorithm choice) |
| DIPPER | 7 prompts 57.31% vs same prompt 55.76% (mean single 56.55%); Qwen2-Math-1.5B | a19, c14 | single |
| Prompt variety within one model does not lower error correlation | .633 vs .603 (GPQA, n=198); .571 vs .607 (LCB-Hard, n=171) | d04 | single |
| Content of the variation does not matter | personas 72.7, paraphrases 72.7, strategies 70.2 (p>0.25) | d05 | single |
| At equal calls a trace-reading aggregator beats self-consistency | GPQA +2.5; BBH-3 86.5 vs 80.4 (+6.1); LCB-Hard 62.6 vs 57.3 (greedy; SC at T=0.7 67.3) | d06 | single |
| The aggregator reading minority traces is the active ingredient | minority-only 73.2% vs full 72.2% | d06 | single |
| Errors correlate across models | both wrong: same wrong answer ~60% (chance 1/3); mean agreement .423 vs .127 chance; 349 LLMs, 12,032 questions | a20, b18 | est |
| More accurate models correlate more | features explain 34-62% of variance in agreement | b18 | single |
| Same-family ties are higher | Arena 34.9% vs 28.8% (57,477 battles); MT-Bench 31.9% vs 20.9% | c26 | single |
| Intra-model error correlation of the best model | .80 vs .42 across models, matched band .74-.865 | d03 | single |
| Output homogeneity | within-model similarity >0.8 (26K queries, top-p .9, T 1.0); cross-model .71-.82; still >0.8 at T 2.0, min-p .1 | a21, b20, c06 | est |
| GPT-3.5 cannot stand in for a population | 6 of 14 studies zero variance; 8 analysed; 37.5% replicated; 99.6% conservative | a22, c09 | est, old model |
| Coverage scales, selection plateaus | SWE-bench Lite 15.9% to 56% at 250; MATH Llama-3-8B 82.9% (100) to 98.44% (10,000); vote/reward 40.50% to 41.41% | b28 | single (large study) |
| The selector decides whether diversity pays | diverse+judge .810; vote .496; synthesis .179; homogeneous .512; independent judges .611 / .726 | a18, c04, c27 | est, upper bound |
| Verifier false positives cap resampling | optimal K often <10; about 5 at cost-benefit ratio 4 | d16 | single |
| Weak-verifier ensemble | Llama 3.3 70B K=100: first 68.4, vote 72.2, Weaver 87.7 (oracle within 4.2) | d17 | single |
| Self-critique fails, a sound check works | Game of 24: 5% plain, 3% LLM critic, 36-38% with sound verifier | d18 | old (GPT-4) |
| Hard ceiling for any pool | vote/router accuracy <= 1 - delta; delta=0.052 MATH-500, 0.079 code, 0.127 GPQA free-response | d02, d19 | single |
| Consensus selection falls into a popularity trap | oracle ceiling up to +83%; diversity-based selection realises up to 95% | c07 | single |
| Same-model ensembles scale | Llama2-13B at 15 = Llama2-70B on GSM8K; gains grow with difficulty | b29, c13 | est |
| Dense sharing collapses diversity | Vendi/N 1.03 to 0.47 for 3 to 7 agents; hidden profile 30.1% vs 80.7% | d08, d09 | single per task |
| Internal perspectives in reasoning models | Countdown 27.1% to 54.8% with +10 steering, 23.8% with -10 | c15, c28 | single |
| Degeneration of thought | counter-intuitive arithmetic GPT-3.5 26.0 (base), 29.5 (SC), 27.5 (self-reflect), 37.0 (MAD) | c11 | single, old |
| Heterogeneity at small N | MIX beats best single by up to +14.28 at N=8 on 126 questions; gpt-4.1-mini debate 50.79 to 42.86 | d07 | single, confounded |
| Silicon crowd | median of 12 LLMs Brier .20 vs 925 humans .19, p=.850; GPT-4 .17 to .14 after human median, p=.003 | c08 | single |

## 4. Mechanisms and models

Each is written so it can be coded.

### 4.1 Relay search (Hong-Page)

```
pool = all heuristics (ordered k-tuples from 1..l)
group = chosen subset
x = start
repeat:
  moved = false
  for h in group:
    x2 = hill_climb(x, h)   # try each step in h, accept only if better; loop till none helps
    if x2 != x: x = x2; moved = true
until not moved
```
The group stops where all members are at local optima. The group beats a member because it escapes that member's local optima. It needs (i) members that differ on where they get stuck and (ii) a landscape where escaping one agent's trap leads upward. Two controls to always include (K03): a random group and a "maximum diversity" group. If the max-diversity group does not beat random, "diversity" is not the cause.

Mapped to our agent: an "attempt" is a heuristic; "stuck" means the answer fails the check; the relay is S5/S6 (hand the failing output to a different operator). Prompt sets are the pool.

### 4.2 Group effective size

Reijula-Kuorikoski: the random group beats the best group largely because the union of its heuristics is larger (effective size), and the best group is made of reorderings of the same numbers. Implement: compute the union of step sets (for prompts, the union of approach labels). Report the gap against effective overlap. Choose a prompt set by maximising coverage, not by taking the top N on dev.

### 4.3 Quality-diversity regression (Self-MoA)

Fit `accuracy ~ a*quality + b*diversity` over many subsets. Quality = mean single-member accuracy. Diversity = Vendi score of output embeddings (exp of the entropy of the eigenvalues of the normalised similarity matrix); Vendi/N is the utilisation ratio in d08. Found a > b on all three datasets (a14). Implement on our own prompt sets: about 70 subsets, regress.

### 4.4 Co-failure ceiling and error correlation

Per item, record which attempts are correct. Pairwise error correlation = correlation of the failure indicators. delta = share of items where every attempt fails. Any selector that outputs one member's answer is bounded by 1 - delta (d02). Pairwise correlation does not identify delta. Implement both: correlation to describe overlap, delta to decide whether more attempts can ever help. If delta is large, add information (tools, retrieval, a different method), not attempts.

### 4.5 Selection bottleneck

Teams of N attempts, a selector with quality q (probability to pick the best candidate when one exists). Maryanskyy et al. derive a closed-form crossover: diverse beats homogeneous only above a selector-quality threshold; at q=0 the optimal team size is 1 (c27). Practical rule: gain is about coverage gain times selector quality. Measure selector quality directly as P(selected is correct | some candidate correct). Sound external checks, tests, or an ensemble of weak independent verifiers (Weaver) raise it; self-critique does not (d18). A check that passes wrong answers caps K (d16).

### 4.6 Trace-reading aggregator

Instead of voting on final answers, give a separate call the traces of all attempts and ask which reasoned correctly (d06). Active ingredient: minority traces (73.2% minority-only vs 72.2% full). Answer-only input falls to the vote baseline. Caution: this is a model judge. G5 says a judge sees no authorship, no majority and no proposed answer. Run it blinded, with checks as veto, and test it before use (U4).

### 4.7 Sharing and convergence

Lazer-Friedman and O'Brien: the faster information flows, the faster the group converges and the less it explores. LLM version (d08): Vendi/N falls from 1.03 at 3 agents to 0.47 at 7 with dense interaction; blind independent writing first (nominal group technique) gives the highest initial diversity. Implement: attempts run in fresh contexts (already S3); share raw evidence (the failing output, a test result) only after all independent attempts are done; withhold other attempts' conclusions.

### 4.8 Heterogeneity without a second model

Candidates for in-model diversity: different prompts (no decorrelation, d04), different approach algorithms (DIV-SE: large gains where plain prompting fails, confounded with approach selection), different temperature, different tool use, internal perspective steering (c15, only in one 8B open model). Only designed-approach variation has any evidence of changing what is solved, and that evidence is confounded.

## 5. What holds up

**Replications that held**
- Hong-Page simulation numbers are reproducible (Thompson, Reijula-Kuorikoski, Grim; K01).
- Correlated errors across LLMs (349 models, two datasets, Arena and MT-Bench tie-rate evidence; K10).
- Output homogeneity across models (Jiang, Park; K11).
- Debate does not beat voting over same-model samples (Choi, Smit, Zhang; K14).
- Persona prompts do not help factual accuracy (Zheng, Smit, Choi; K13).
- Coverage rises and selection plateaus (Brown; K15). Selection quality is the limiting factor in four lines (Maryanskyy, Stroebl, Weaver, Stechly; K16).

**Failures and refutations**
- The theorem: flawed lemma, does not match the experiment (Thompson, Romaniega).
- "Diversity" as measured is not the cause: max-diversity groups lose to random groups (Thompson).
- The 2001 bit-string model: no diversity advantage (Reijula-Kuorikoski).
- Weisberg-Muldoon maverick result: contested (Alexander et al.; sensitivity to rules). Not read in full.
- MoA diversity headline: the single-proposer comparator was weaker than the best proposer (critique correction 3).
- Original debate gains (Du et al.): largely recovered by voting.
- Synthesis aggregation: 0.179 win rate, preferred in 0 of 42 tasks (a18).
- Self-critique as selector: below plain prompting (d18).

**Moderators**
- Landscape structure: a random landscape favours diversity; stairway and structured landscapes favour ability (b03).
- Group size: the gap shrinks as the group grows (a02) and vanishes above size 10 in the stairway model (b03).
- Quality gap among proposers: if one model is clearly best, resample it (K06, K07); if models are of similar quality, cross-family helps (K09; d03 +0.027).
- Selector quality: below the crossover, diverse teams lose (a18, c27).
- Task format: free response exposes shared failures (delta .127) that multiple choice hides (d19).
- Task type for humans: creative, R&D and complex tasks show larger diversity effects (d14).
- Stronger models: negative scaling in some settings (gpt-4.1-mini debate 50.79 to 42.86; d07).

**Interventions that worked**
- Resample the best model and select with a sound check (Brown, Weaver, Stechly).
- Cross-family mixes at similar quality (Hegazy, ReConcile, Heter-MAD, Chen).
- Varied approach prompts where plain prompting fails (DIV-SE; confounded).
- Trace-reading aggregation at equal calls (Fadnavis; single, own method).
- Diversity-based selection over consensus in code ensembles (c07).
- Blind independent first drafts, then structured sharing (d08, d09).

**Interventions that did not work**
- Personas, paraphrases and strategy rewrites as decorrelators within one model (d04, d05, b21).
- Debate with homogeneous agents (martingale; d01).
- Synthesis (MoA-style blending) when selection is available (a18).
- Model self-verification as selector (d18).
- Dense early communication (d08, d09, d10).

**Caveats on the evidence base.** Many 2026 numbers are single-run preprints from authors promoting a method, with small n (GPQA n=198; Formal Logic 126). Few compare at equal tokens. No LLM study isolates Hong-Page style diversity (different heuristics) from selection among samples. Human meta-analysis effect sizes were read only through the Wallrich summary table.

## 6. Language models

**How they behave.**
- *Within one model:* outputs are alike. Pairwise similarity above 0.8 on 26K open queries, even at temperature 2.0 (c06). Intra-model error correlation .80 for the best model vs .42 across models at matched quality (d03). GPT-3.5 gave zero variance in 6 of 14 Many Labs 2 studies (c09).
- *Across models:* errors still overlap. When two models are both wrong they pick the same wrong option about 60% of the time (chance 1/3). Mean agreement .423 vs .127 random. More accurate models agree more (b18). LLM judges inflate scores for weaker models that share their errors (b19). In coding, ten models from five families had complementary solves (oracle up to +83%), but consensus selection fell into a popularity trap (c07).
- *Reasoning models:* simulate several internal voices. In DeepSeek-R1-Llama-8B, steering one conversational feature raised Countdown accuracy from 27.1% to 54.8%; negative steering gave 23.8% (c15). One model, one task; the voice counter is itself an LLM judge (Spearman .86 on N=1,196 debate turns).

**What changed it, by how much.**

| Change | Effect | Source |
|---|---|---|
| Different model families, similar quality, debate | +9 points GSM8K (91 vs 82); +6.8 StrategyQA | c03, c10 |
| Heterogeneous debate | +2.7 to +8.2 | b25 |
| Different models at matched quality, k=3 | +0.027 mean (+0.010 to +0.050) | d03 |
| Resample best model instead of mixing (quality gap) | +6.6 AlpacaEval LC; +3.8 average | a13 |
| Diverse team with strong selector | win .810 (upper bound; .611 with independent judges) | a18, c04 |
| Same team, majority vote | .496 | a18 |
| Same team, synthesis | .179 | a18 |
| Varied approach prompts (DIV-SE) | Graph Coloring 97 vs SC-10 23 | a16 |
| Prompt diversity (DIPPER) | +1.5 over same prompt | a19 |
| Prompt perturbation, error correlation | .633 vs .603 (no change) | d04 |
| Persona vs paraphrase vs strategy | 72.7 / 72.7 / 70.2 (same) | d05 |
| Trace-reading aggregator at equal calls | +2.5 GPQA, +6.1 BBH-3, +5.3 LCB-Hard greedy | d06 |
| Debate vs vote | vote .7691 vs best MAD .7377 (Qwen2.5-7B) | d01 |
| More samples: coverage | 15.9% to 56% at 250 (SWE-bench Lite) | b28 |
| More samples: selected accuracy | 40.50% to 41.41% | b28 |
| Weak-verifier ensemble over 100 samples | 72.2 (vote) to 87.7 | d17 |
| Dense interaction, 3 to 7 agents | Vendi/N 1.03 to 0.47 | d08 |
| Distributed information, multi-agent | 30.1% vs 80.7% single with all facts | d09 |

**Reconciling MoA and Self-MoA.** (1) MoA's single-proposer row used a weaker model; its own Table 4 shows WizardLM-8x22B alone as a proposer scores 63.8, above 61.3. (2) Li et al. show proposer quality matters more than diversity. (3) Mixed pools help when members are of similar quality (Chen: +0.027) or have complementary skills (c02: 60.04 vs 59.69; Hegazy). (4) Selection quality gates all of it (Maryanskyy). (5) Compute-equalised, Self-MoA can be weak on GPQA and strong on AIME (d06). So direction depends on quality gap, selector and task, and the effect sizes are small.

**What this means for one model.** The cross-model advantage (+0.027, +2.7 to +8.2) is about the most a second model gives. Within one model, prompt variety does not decorrelate errors (d04). What remains is: more attempts (coverage), a sound selector, approach-level variation where the task admits different algorithms, and a reader of minority traces. All of these still need an equal-token test on our bench.

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep G4 as written: samples from one model are not independent; agreement is a hint. Add the numbers: two wrong models share the wrong answer about 60% of the time; one model resampled correlates more (.80). | G4 | [E] | K10, K11; a20, b18, a21, d03 |
| A2 | Selection decides the gain. State in G5/S7: a resampling or diversity step pays only if the selector is a test or independent check. Never blend attempts into one answer (synthesis) when selection is possible. | G5, S7 | [E] | K16, K17; a18, c04, c07, b28, d16, d17, d18 |
| A3 | Do not add persona or strategy-persona voters (already in G4). The evidence now covers 162 personas and a null content ablation. | G4, section 4b | [E] | K13; b21, c12, d05 |
| A4 | Debate stays out (G9). Add the figure: vote .7691 vs best debate .7377 (Qwen2.5-7B). | G9 | [E] | K14; d01, b24, b22 |
| A5 | Log coverage (any attempt correct) and selected accuracy separately, plus delta (share of items where every attempt fails). If delta is large, spend on new information, not new attempts. | logging (section 6), G12 | [E] coverage vs selection; delta [S] | b28; d02 |
| A6 | Never treat "diversity trumps ability" as a law. Compare any diverse set to the best single member resampled and to a random set, not to an arbitrary member. | method rule | [E] | K02, K03, K04, K08 |
| A7 | Expect small gains from diversity alone: human prior r about .04 to .10; cross-model LLM gain about +0.03 at matched quality. | priors | [E] human, [S] LLM | K21; d14, d03 |

### Test first

| # | Item | Schema part | Status | Evidence | Test |
|---|---|---|---|---|---|
| T1 | Approach-level variation in S3: ask for N genuinely different methods (different algorithm, not persona), run each as an attempt, select by check. | S3, O3 | [S], confounded | K12; a16, d05 | U1 |
| T2 | Compare varied attempts with N same-prompt samples AND the best single approach at equal tokens. | S3, G7 | [S] | critique gap 1 | U1 |
| T3 | Trace-reading selector over varied attempts (blinded, checks as veto). | S7 | [S] | K27; d06 | U4 |
| T4 | Delay sharing: attempts run isolated; raw failing outputs shared only after. | S3, S5, memory | [S] | K28, K18; d08, d09, a23 | U5 |
| T5 | Forbid-visited-approaches operator ("maverick") with a code-kept history of approaches tried. | S3 open mode, O3 | [C] | K19; a24, b09 | U6 |
| T6 | Landscape detector: route structured items to best-approach resampling and random-like items to varied approaches. | S0 | [S] | K04, K30; b03, d19 | U7 |
| T7 | Measure within-model error correlation with and without operators on a dev set; an operator counts as diversity only if it lowers it. | logging | [S] | K25; d04 | U2 |
| T8 | Internal-perspective prompt analogue for reasoning models. | S3, O8 | [S] | K22; c15 | U9 |
| T9 | Track selector quality: P(pick correct given some attempt correct). | S7 | [E] direction, threshold [S] | K16 | U3 |
| T10 | Quality-versus-diversity regression on our own prompt sets. | S0 gate | [S] | K07; a14 | U10 |

## 8. Concrete tests on our bench

All arms at equal total tokens (setup cost counted, G7). At least 3 seeds; paired comparison per item.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Varied approaches vs same prompt vs best approach (T1, T2) | ARC and BRAINTEASER items with a check; plus a graph or planning set where approach choice matters | (a) N samples of one prompt; (b) N varied-approach attempts; (c) best single approach on dev, N samples; all select by the check | solve rate at equal tokens; delta | b beats a by 0 to +3 points on typical items, more on planning-like items; b vs c unknown, near 0 |
| B2 Error correlation (T7) | 100 dev items | identical prompt; paraphrase; persona; different approach; different operator | pairwise error correlation; delta | paraphrase and persona stay near .6; an algorithm change lowers it only if it changes what is solved |
| B3 Selector quality crossover (T9) | items with and without a check | selector = check; blinded self-judge; vote; trace-reading; crossed with N=1, 3, 5, 8 | solve rate; P(pick correct given some correct) | check wins; self-judge at or below vote; diversity gain vanishes when selector quality is low |
| B4 Trace-reading vs vote (T3) | open-answer items | vote on answers; aggregator on answers only; aggregator on all traces; aggregator on minority traces only | solve rate | trace-reading +2 to +6 over vote if Fadnavis holds; answer-only equals vote |
| B5 Sharing delay (T4) | multi-step items, hidden-profile style items | all independent; early conclusion sharing; raw failing outputs shared after the independent round | solve rate; Vendi/N; distinct final answers | independent-first wins or ties; early conclusion sharing lowers diversity and accuracy |
| B6 Maverick operator (T5) | open mode (NoveltyBench style) and impasse items | no history; history with forbid-visited | distinct approaches; solve rate | more distinct approaches; accuracy effect unknown, contested |
| B7 Landscape split (T6) | all items, labelled structured or random-like after the fact | best-approach resampling vs varied approaches | solve rate per class | best approach wins on structured items; varied wins on random-like; check whether a cheap probe predicts class |
| B8 Format split | same items as multiple choice and as free response | resampling arms | delta; gain | free response shows larger delta and more headroom |
| B9 Hong-Page toy | toy search with a prompt pool | random 10 vs max-different 10 vs best-10-on-dev | score | replicate K01 and K03 on our pool; report gap vs overlap |
| B10 Quality-diversity regression | about 70 prompt sets | regress accuracy on mean quality and Vendi | coefficients | quality coefficient larger, as in a14 |

## 9. What does not transfer, and why

- **The Hong-Page theorem and ringworld.** Agents are deterministic hill-climbers on a random landscape with no structure. An LLM attempt is neither deterministic nor on a random landscape. The theorem is a limit result with no sizes. Do not use it to justify any count.
- **Human team diversity.** Humans differ in knowledge and experience. One model has one training set. The human effects are also tiny (r about .04 to .10) and mostly correlational.
- **Cross-family gains (+9 GSM8K, +6.8 StrategyQA).** They need a second model of similar quality. We have one. They also use more calls.
- **Persona diversity.** A persona changes style, not knowledge (b21, d05).
- **Debate.** Same-model debate is a martingale (d01). Voting recovers the gain. G9 stays.
- **Weisberg-Muldoon mavericks.** Modelled scientists avoid explored ground for the benefit of followers. Our attempts do not follow each other. The result is contested.
- **Wisdom of the silicon crowd.** Needs 12 different LLMs; 31 questions; acquiescence bias (c08).
- **Steering voices (c15).** Needs internals of an open reasoning model; a scaffold cannot steer features.
- **Large-N coverage (Brown: 250 to 10,000 samples).** Our budget is a few attempts per item (G11), and we usually lack a verifier.
- **Diversity-collapse and hidden-profile results (d08, d09).** About pooling facts and idea generation across many agents. They support isolation but do not size a gain for one thread.
- **MoA synthesis.** Rewrites attempts into one answer. It lost to selection (a18).

## 10. Open questions

1. At equal tokens, do N varied-approach attempts from one model beat N same-prompt samples and the best single approach? No paper isolates this. DIV-SE is confounded with approach selection and Fadnavis found no effect of variation content.
2. Do meaning-changing, algorithm-changing operators lower within-model error correlation? Only surface perturbations were tested (d04).
3. What selector quality is needed for diversity to pay with one model? The Maryanskyy crossover was not remeasured, and its headline was inflated by judge circularity (53 to 67% attenuation).
4. Can the agent detect structured versus random-like tasks online? No detector exists (K30).
5. Does delaying sharing improve accuracy at equal tokens? Only diversity metrics and hidden-profile pooling were measured.
6. Is the maverick operator useful? The three key papers were not opened; Weisberg-Muldoon and Alexander et al. disagree.
7. Does Self-MoA replicate with reasoning models under the original protocol? Two 2026 studies disagree (d03, d06).
8. Do results hold on frontier models? Many numbers come from 7-8B models, GPT-3.5 or GPT-4; the gpt-4.1-mini debate result goes the other way (d07).
9. What do the Lazer-Friedman and Mason-Watts originals say? The sign of the clustering effect is contested (K29).
10. Do human meta-analysis effect sizes (r .04 to .10) set a fair prior for LLM scaffolds? Unknown.

## 11. Sources

**[V] = opened (this batch). [M] = snippet, abstract or second-hand only.**

- [V] Hong and Page 2004, PNAS 101(46):16385. https://www.pnas.org/doi/10.1073/pnas.0403723101 (a01-a04, a12 opened; b01 and c23 record the page as blocked in other sessions, so cross-check Table 1 numbers with Thompson and Reijula-Kuorikoski)
- [V] Thompson 2014, Notices of the AMS 61(9). https://www.ams.org/notices/201409/rnoti-p1024.pdf
- [V] Romaniega 2025, arXiv:2307.04709. https://arxiv.org/abs/2307.04709
- [V] Reijula and Kuorikoski 2021, Philosophy of Science. https://doi.org/10.1086/714938
- [M] Grim et al. 2019, Philosophy of Science 86(1):98. https://doi.org/10.1086/701070
- [M] Singer 2019. https://doi.org/10.1086/701074
- [M] Kuehn 2017, Critical Review 29(1) (listing only)
- [V] Wallrich replication README. https://github.com/rougier/diversity_abm_replication
- [M] Page 2007, The Difference. https://press.princeton.edu/books/paperback/9780691138541/the-difference
- [M] Weisberg and Muldoon 2009. https://doi.org/10.1086/644786
- [M] Alexander, Himmelreich, Thompson 2015. https://researchonline.lse.ac.uk/id/eprint/60256
- [M] Lazer and Friedman 2007. https://doi.org/10.2189/asqu.52.4.667
- [M] Replication of the Weisberg-Muldoon model (2018). https://ssoar.info/ssoar/handle/document/56493
- [V] Luan, Katsikopoulos, Reimer 2012, PLoS ONE. https://doi.org/10.1371/journal.pone.0031043
- [V] Approval-voting diversity paper, Episteme 2025 (authors unconfirmed). https://doi.org/10.1017/epi.2025.10042
- [V] O'Brien, Fazelpour, Rubin, Wong 2025, CogSci. https://escholarship.org/uc/item/84g365px
- [V] Shore, Bernstein, Lazer 2015. https://dash.harvard.edu/server/api/core/bitstreams/7312037d-569e-6bd4-e053-0100007fdf3b/content
- [V] Wallrich et al. 2024, J Business and Psychology 39:1303. https://doi.org/10.1007/s10869-024-09977-0
- [M] Horwitz and Horwitz 2007; Bell et al. 2011; Joshi and Roh 2009; van Dijk et al. 2012; Stahl et al. 2010 (via Wallrich Table 1). https://doi.org/10.1177/0149206307308587 and https://doi.org/10.1177/0149206310365001
- [V] Wang et al. 2024, Mixture-of-Agents. https://arxiv.org/abs/2406.04692
- [V] Li et al. 2025, Self-MoA. https://arxiv.org/abs/2502.00674
- [V] Naik et al. 2024, DIV-SE. https://arxiv.org/abs/2310.07088
- [V] Hegazy 2024. https://arxiv.org/abs/2410.12853
- [V] Maryanskyy et al. 2026. https://arxiv.org/abs/2603.20324
- [V] Hu et al. 2025, DIPPER. https://arxiv.org/abs/2412.15238
- [V] Kim et al. 2025, Correlated errors. https://arxiv.org/abs/2506.07962
- [V] Jiang et al. 2025, Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Park, Schoenegger, Zhu 2023. https://arxiv.org/abs/2302.07267
- [V] Zheng et al. 2024, personas. https://arxiv.org/abs/2311.10054
- [V] Smit et al. 2024, MAD. https://arxiv.org/abs/2311.17371
- [V] Du et al. 2023 (tables in b23; c16 notes layout only). https://arxiv.org/abs/2305.14325
- [V] Choi, Zhu, Li 2025, Debate or Vote. https://arxiv.org/abs/2508.17536
- [V] Zhang et al. 2025, Heter-MAD. https://arxiv.org/abs/2502.08788
- [V] Chen, Saha, Bansal 2024, ReConcile. https://arxiv.org/abs/2309.13007
- [V] Brown et al. 2024, Large language monkeys. https://arxiv.org/abs/2407.21787
- [V] Li et al. 2024, Agent Forest (no headline number in b29; GSM8K figure from c13). https://arxiv.org/abs/2402.05120
- [V] Cemri et al. 2025, MAST. https://arxiv.org/abs/2503.13657
- [V] Vallecillos-Ruiz, Hort, Moonen 2025. https://arxiv.org/abs/2510.21513
- [V] Schoenegger et al. 2024, Silicon Crowd. https://arxiv.org/abs/2402.19379
- [V] Liang et al. 2024, divergent thinking MAD. https://arxiv.org/abs/2305.19118
- [V] Kim, Lai, et al. 2026, Societies of Thought. https://arxiv.org/abs/2601.10825
- [M] Abdulaal et al. 2025, Balancing Act. https://mlanthology.org/iclr/2025/abdulaal2025iclr-balancing
- [M] Wang et al. 2023, Self-consistency. https://arxiv.org/abs/2203.11171
- [V] Chen 2026, Co-failure ceiling (GPQA free-response part at abstract level). https://arxiv.org/abs/2606.27288
- [V] Fadnavis, Kanakaraj, Wyss 2026, Beyond Consensus. https://arxiv.org/abs/2605.29116
- [V] Yang et al. 2026, agent scaling via diversity. https://arxiv.org/abs/2602.03794
- [V] Chen et al. 2026, Diversity collapse. https://arxiv.org/abs/2604.18005
- [V] Li, Naito, Shirado 2026, HiddenBench. https://arxiv.org/abs/2505.11556
- [V] Stroebl, Kapoor, Narayanan 2026, Limits of resampling. https://arxiv.org/abs/2411.17501
- [V] Saad-Falcon et al. 2026, Weaver. https://arxiv.org/abs/2506.18203
- [V] Stechly, Valmeekam, Kambhampati 2024, self-verification. https://arxiv.org/abs/2402.08115
