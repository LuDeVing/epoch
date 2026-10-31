# Theory theory / child as scientist: deep document

*Subfield A14.01. Built from evidence_a-d.jsonl (a01-a27, b01-b26, c01-c28, d01-d18), claims.jsonl (K01-K21) and critique.md in this folder. Evidence ids in brackets. [V] = opened and read, [M] = snippet or second-hand only. Search tools were out of quota for the gap pass, so coverage of 2026 work is thinner than intended.*

## 1. What it is

The theory theory says that children hold intuitive theories of the world and change them with evidence, much as scientists do. The picture has three parts.

- **Structure.** A theory is abstract, coherent and causal. It names hidden entities. It comes in layers: a broad framework theory above narrow specific theories. [a01]
- **Function.** A theory predicts, explains evidence, and supports interventions and counterfactuals. [a01]
- **Dynamics.** A theory changes when evidence goes against it, often through intermediate versions, and it changes in a rational way. [a01]

The modern form is "Theory Theory 2.0" (Gopnik and Wellman 2012). Theories are probabilistic causal graphs. Learning is Bayesian-like updating from observed evidence and from the child's own interventions. [a02, b01]

Why we care. Our agent's S5 REVISE state must change a working hypothesis when a test fails. This literature gives (a) a list of what a good revision loop does, (b) a clear set of ways it goes wrong, and (c) a family of small hidden-rule tasks (the blicket detector) on which LLM agents have now been measured. Honest summary: the human data show a limited, task-bound ability in small deterministic systems. The LLM data say current models are weak at exactly the steps REVISE needs: generating rival hypotheses, choosing tests that split them, reading results, dropping a favoured rule. No study shows that a theory-theory-shaped loop beats cheap resampling at equal tokens (K17).

## 2. History and theories in depth

**Roots.** Constructivism (Piaget): knowledge is built through action and changed when it fails. Theory theory (Carey 1985; Gopnik 1988; Wellman 1990; Keil 1989; Gopnik and Meltzoff 1997) made the claim specific: concepts sit inside theory-like systems and conceptual change resembles scientific change. [a01]

**The old theory theory** did not say what the representations were or what learning mechanism moved a child from one theory to the next. The authors admit this. [a01]

**Theory Theory 2.0 (2001-2012).** Causal Bayes nets (Pearl; Spirtes, Glymour, Scheines) supplied the representation. Hierarchical Bayes nets supplied framework theories above specific ones. Interventions are graph surgery; counterfactuals use the same machinery. [a02] Main empirical programme:

- Gopnik, Sobel, Schulz, Glymour 2001: 2-, 3- and 4-year-olds use covariation and screening-off to say which blocks are blickets, then act correctly. [a05, b03; second-hand]
- Sobel, Tenenbaum, Gopnik 2004: backward blocking in 4-year-olds, sensitive to the base rate of blickets. [a27; second-hand]
- Kushnir et al. 2005: a block that fired 2 of 3 times is rated stronger than one that fired 2 of 6. [a02]
- Schulz, Gopnik, Glymour 2007: conditional interventions on gear toys. [a07, a08, b06; opened]
- Denison et al. 2010: 4-year-olds guess in proportion to probability, read as sampling from the hypothesis distribution. [a04; second-hand]
- Lucas et al. 2014, Gopnik et al. 2017: young children adopt an unusual conjunctive rule more than adults. [a12, a13, b09, d04]
- Bonawitz et al. 2011: teaching narrows exploration. [a15, b11, d05]
- The search answer: a learner cannot test every hypothesis, so it samples one, tests it, updates and resamples, or mutates a likely hypothesis into neighbours. This is Monte Carlo style search. It converges to the Bayesian answer only in the long run, and no step estimate is given. [a03]

**Rivals.**

- *Associative / domain-general learning.* McClelland and Thompson 2007: a plain back-propagation network with interleaved training reproduces the screening-off, one-cause, two-cause and graded backward-blocking data with no causal machinery. It needs earlier events re-presented, which is an add-on. [a06, b04]
- *Nativism / core knowledge* (Spelke, Carey) disputes "theories all the way down". [a01]
- *Stage views* (Piaget) versus gradual change. Each child mixes right and wrong answers across 20 to 30 false-belief tasks (Liu et al. 2007), which fits a gradual shift of probabilities. [a19, b02]

**The 2020s turn.** The same group (Gopnik, Kosoy, Yiu, GX-Chen, Samiei) moved the blicket detector into AI: RL benchmarks (2022), position papers on LLM imitation versus innovation (2023-24), text blicket games for LLM agents (2025), and an adult active-exploration study with an LLM arm (2026). Other labs added Wason-style confirmation-bias tests (Jhaveri 2026, Bertolazzi 2026) and a scaffold study (Alderete 2026). [a20-a24, c01-c28, d01-d18] The blicket-LLM papers share authors, so they are one connected group, not independent labs. [d18]

## 3. Core findings with exact numbers

Status: E established, S single source, C contested, O open.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| 4-year-olds infer which gear is causal from conditional interventions | Test n=25: 84% trial 1, 76% trial 2, 64% both (p<.025). Controls n=18 each: 33%, 6%, 22% both trials. 80 children, mean age 4;6 | Schulz, Gopnik, Glymour 2007 Exp 1 [a07, b06, V] | E (K01) |
| Children choose among four gear structures | Exp 2 group A 60% on both (n=20, p<.001); no switch evidence 37% chain, 50% conjunction (n=16, chance). Exp 3: common effect 71%, conjunction 86% (n=14 each) | Schulz et al. 2007 [a08, V] | E |
| Predicting evidence from a known structure is much harder | Exp 4: 44-50% per trial (n=16); 12% right on all four | Schulz et al. 2007 [a07, b06, V] | S |
| Blicket detector: 2-4 year-olds use covariation | 4-year-olds called the 67%-effective object a blicket 16% (one-cause) vs 78% (two-cause); 3-year-olds 66% and 85% | Gopnik et al. 2001 via McClelland and Thompson [a05, M] | E for direction; numbers second-hand |
| Bayesian reading vs associative network | Network reproduces group data; children say yes to ~67% of stimuli the normative model rejects; 2-of-3 answers inside 95% interval of probability matching | McClelland and Thompson 2007 [a06, b04, V] | C (K02) |
| Probability matching at age 4 | 80/20 bag: ~80% red guesses, ~20% blue; two-bag condition follows machine contents, not raw counts | Denison et al. 2010 via review [a04, M] | S |
| Hidden insides tied to causal power at age 4 | N=64: 61% (one-tailed p=.05; two-tailed p<.10); 83% name right insert. 3-year-olds 31% (causal) / 19% (association); 4-year-olds 72% / 17%. Age F(1,60)=5.91, condition F(1,60)=17.48, interaction F(1,60)=6.89 | Sobel et al. 2007 [a09, b07, V] | S, weak |
| Backward blocking fails in 6-month-olds | n=19, F(3,54)=0.28, p=.84 (corrected; b05's F(3,51)=1.55 was the sex x test interaction) | Benton and Rakison [a11, V] | C (K03) |
| Backward blocking fails in adult ratings | n=60; A rose 50.83 to 96.25 (p<.006); B did not drop significantly (t(59)=1.84, p=.07) | Benton and Rakison [a11, b05, V] | C |
| Backward blocking fails in 3-year-olds | No numbers; abstract only | Beckers et al. 2009 [d12, M] | C |
| Backward blocking in adults only in an incidental RT task | blocked 496 vs 496 ms (dz=-0.01) vs control dz=0.39; interaction b=9.45, CI [1.34, 17.63]; 50 of 84 kept | PLoS One 2024 [d13, V] | S |
| Diagnostic inference over 4 uncertain causes is late | N=242, ages 4-10. Blicket 38.5%, 41.0%, 55.3% by age third; butterfly 26.2%, 38.1%, 59.5%; chance 33%; only oldest beat it (p=.007, p<.001). Exp 2 N=112 replicates. Category version N=110: 27%, p=.20 | Weisberg, Choi, Sobel 2020 [a10, b08, b22, V] | S (K04), replicated within paper |
| Young children adopt an unusual conjunctive rule more than adults | Key object called blicket under AND: 4 yr 0.92; 6-7 yr 0.56 (n=90); 9-11 yr 0.60 (n=90); 12-14 yr 0.28 (n=86); adults 0.25. Pooled AND 0.52, OR 0.13, baseline 0.15. 4 vs 6-7 P<.01; 12-14 vs adults P=1.0 | Gopnik et al. 2017 [a12, b09, d04, V] | E (K05) |
| Social attribution is an inverted U | 4 yr 0.93, 6 yr 0.43, 9-11 0.55, 12-14 0.24, adults 0.38 (baseline score); adolescents most flexible on one measure | Gopnik et al. 2017 [a12, d04, V] | S |
| Giving children the hypothesis space helps exploration | N=85, ages 4-5. Enough data to settle the rule: 71% given vs 32% not given (p=.002). Actions 14.07 vs 10.58. ~17.5% tested the empty machine | Kosoy et al. 2022 [a20, b12, b25, V] | S (K07) |
| Teaching narrows exploration | N=85. Play 119.2 s pedagogical vs 205.7 s baseline (F(1,81)=4.52, p<.05); action kinds 4.00 vs 6.15 (p<.01); hidden functions found 0.72 vs 1.15 (p<.05). Exp 2 N=64 | Bonawitz et al. 2011 [b11, d05, V] | S (K15) |
| Mixed strategies in children | ~50 preschoolers; 65% passed >75% of false-belief tasks, 30% passed <25% | Liu et al. 2007 via review [a19, M] | S (K16) |
| Adults: active beats passive on AND | N=306 (102 each). AND object identification: active 0.69, passive observer 0.45, passive proposer 0.12. Rule choice 0.82, 0.69, 0.57. Accepted CogSci 2026 | Samiei et al. 2026 [a23, b19, c08, d01, V] | S (K06, K20) |
| LLMs: OR yes, AND no | 4 vs 8 objects, up to 32 steps. Oracle = 1.0. Info gain vs success rho=0.76; unique states 0.33; steps before exit -0.35; response length -0.30 | GX-Chen et al. 2025 [c01, c02, V] | E (K08) |
| Higher reasoning effort can hurt exploration | o3-mini and o4-mini at higher effort worse on 8-object AND exploration | GX-Chen et al. 2025 [d03, V] | S |
| More hypotheses removes the AND-OR gap | 16, 32, 64, 96 seeds: accuracy rose, gap gone at larger counts. Size and prior flatness changed together | GX-Chen et al. 2025 [b16, c06, d03, V] | S (K09) |
| Oracle data does not fully fix AND | All LMs beat their own self-explored AND score with oracle trajectories; all but deepseek-reasoner stay well below perfect | GX-Chen et al. 2025 [c03, V] | S |
| Reasoning models close much of the gap | gpt-5, deepseek-reasoner near-perfect on OR; AND still below top humans. Tests per AND/OR trial: avg human 9.6/6.4, top human 8.5/3.8, gpt-5 10.2/7.7, deepseek-chat 12.3/11.9, o4-mini 6.7/4.2 | Samiei et al. 2026 [c09, d02, V] | S |
| Imitation vs innovation | Imitation: children 88.4%, adults 84.9%, GPT-4 83.3%. Innovation: children 85.2%, adults 95.7%, GPT-4 75.9%, gpt-3.5 58.9%, Claude 58.2%, Flan 45.7%, davinci 8.9% | Yiu, Kosoy, Gopnik 2023/24 [a22, b14, b15, V] | E for 2023 models (K11) |
| Counterexample prompt (Think-in-Opposites) | Wason: Qwen3-8B 0.21 to 0.36, 32B 0.41 to 0.61. Blicket (192 episodes): 8B 0.32 to 0.40, 32B 0.57 to 0.86; non-thinking 8B 0.11 to 0.19. Mean over 11 models 42% to 56%. Blicket I:C 8B 0.44 to 0.57, 32B 0.54 to 1.31 | Jhaveri et al. 2026 [b18, c12-c14, d07, V] | S (K10) |
| Confirmation bias predicts failure | 12 LLMs x 100 games. rho=-0.779 (p=.003); odds ratio 0.016; GPT-5.2-Chat bias 20% in won vs 50% in lost games | Bertolazzi et al. 2026 [d08, V] | E (K18) |
| Context graph + monitors | Post-switch reasoning: base 73.3% (22/30), graph 93.9% (31/33), +monitors 95.3% (41/43); Fisher p=.038. Pooled raw: base 87.3% (96/110), graph 77.3%, graph+monitor 89.1% | Alderete et al. 2026 [a24, b20, b21, d09, V] | S (K13) |
| Scaffold does nothing under noise | p=0.70 activation: 76.7%, 76.7%, 73.3% (n=30 each); noise monitor fired in 77% of episodes | Alderete et al. 2026 [d09, V] | S (K19) |
| Final-hypothesis check | 4-node accuracy 48% to 60%; about half the intervention budget unused | CausaLab 2026 [c25, V] | S (K14) |
| Self-refine vs resampling at equal tokens | Math, Qwen2.5 1.5B-7B, 36 comparisons: 0 better, 10 worse, 26 indistinguishable | Mirzaei 2026 [d10, V] | S, not blicket (K17) |
| Orchestration gains are small | At most +4.6 points over tuned CoT, at 2-4x tokens | Leins et al. 2026 [d11, V] | S |
| Hypothesis refinement with a symbolic checker | ACRE raw: IO 64.0, self-refine 70.0, refine T=3,N=5 82.5. ARC subset 17% to 30% (33% human-selected) | Qiu 2024; Wang 2024 [c20, c21, V] | C (K12) |
| Online rule revision with experiments | ActiveACRE: online hard-rule model 0.35 (SE 0.11), batch 0.10-0.15, direct LLM 0.00. Zendo: human 5.26/8, best model 6.55 | Piriyakulkij et al. 2024 [c22, V] | S |

## 4. Mechanisms and models

Each is written so it can be coded.

**4.1 Causal graph state (Theory Theory 2.0).** Keep the hypothesis as a small causal structure: variables, edges, rule type (OR, AND, other) and parameters. Update after each test. Code holds the structure; the model proposes edits. Children do this well for tiny deterministic systems [K01]. Alderete's context graph accounted for 94% of the post-switch gain [a24].

**4.2 Hypothesis enumeration and elimination.** The best-supported LLM fix [c06, b16].
1. Ask the model for N distinct hypotheses, each as a Python function from a test input to an outcome. Reject duplicates until the pool has 16 to 96 entries.
2. Treat the pool as a flat prior.
3. For each candidate test, run all surviving functions in code. Pick the test whose outcomes split the pool most evenly.
4. After the result, run every function on it and drop those that disagree.
5. Stop when one function (or one behavioural class) survives. Code counts survivors.
This approaches the information-gain oracle (accuracy 1.0). Limit: the space is small and enumerable (2^n+1 rules) [c06]. Open-ended problems need a different pool builder.

**4.3 Sampling-based search (the child as Monte Carlo).** Pick a hypothesis in proportion to its weight, test it, update weights, mutate survivors into neighbours [a03]. This is a particle filter over rule text. Behaviour data (probability matching) do not separate it from noisy associative responding [a04, b04].

**4.4 Online rule revision with experiments (Piriyakulkij).** Rules are natural-language statements compiled to programs. Monte Carlo keeps a weighted set. Experiments are chosen by expected information gain. Beliefs update after each result. ActiveACRE 0.35 vs 0.00 for the direct LLM [c22]. This uses a symbolic checker; it is not a prompt.

**4.5 Counterexample testing.** Label each test compatible (the current hypothesis predicts a positive result) or incompatible (it predicts a negative). I:C is incompatible over compatible tests. Success tracks I:C in two labs [d07, d08]. Cheap implementation: code labels each test against the leading hypothesis; if the last k tests were all compatible, inject "pick a test your current guess says will fail". The published prompt form is "think in opposites" [b18].

**4.6 Hypothesis-vs-data consistency check.** Before commit, code re-runs the final hypothesis on every collected observation and lists contradictions. One such check lifted 4-node accuracy 48% to 60% [c25]. A symbolic interpreter did the same job in ACRE refinement [c20, d15].

**4.7 Monitors that widen the space.** Detect a result no surviving hypothesis predicts, and widen the pool instead of patching. Alderete's monitors had 100% sensitivity across five datasets but added little alone; the graph carried the gain [a24, b20]. Under noise they could not tell a failed true cause from a non-cause [d09].

**4.8 Retroactive rescoring (backward blocking).** After AB+ then A+, B should lose credit. A Bayesian or replay-based learner does this; a sequential delta-rule learner does not [a06]. Implementation: do not update credit sequentially; re-score all hypotheses against the full evidence log at every step, so discounting is automatic. Whether children, adults or LLMs do it unaided is contested [K03].

**4.9 Active choice of tests.** Seeing the outcome of your own test before choosing the next matters: 0.69 active vs 0.45 observer vs 0.12 proposer on AND [d01]. Implementation: choose one test, run it, update, choose again. Never write a batch up front.

**4.10 Hypothesis-space priming.** Telling a child which kinds of rule exist raised settling from 32% to 71% [b12]. In code: every pool contains OR, AND and at least one other rule form.

## 5. What holds up

**Held (two or more sources, or checked in full text).**
- Preschoolers infer causal structure in small deterministic systems well above chance [K01]. This is a group-level pattern; the Bayesian interpretation is not required.
- Four-year-olds adopt an unusual conjunctive rule more readily than adults [K05]. Numbers verified in the PNAS text [d04]. Part of the adult gap is a passive-design effect (adults active 0.69 vs observer 0.45) [d01].
- LLM agents favour OR over AND, explore badly, and gain from information-gain data [K08].
- Confirmation-biased testing predicts failure in two independent labs [K18].
- Imitation is easy for LLMs and innovation harder (2023 models) [K11].

**Failed, partial or contested.**
- Backward blocking: null in 6-month-olds (F(3,54)=0.28), null in adult ratings (p=.07), null in 3-year-olds (abstract only), present in adults only in an incidental reaction-time task with effects under 20 ms [a11, d12, d13]. The infant positive (Sobel and Kirkham) was not read [a27].
- The Bayesian reading: an associative network fits the same data [a06]; 4-year-old answers sit inside a probability-matching interval; children say yes to ~67% of stimuli the normative model rejects [b04].
- Sobel 2007's headline is one-tailed (p=.05) with a strong side bias (chi2=28.90) [a09, b07].
- Several uncertain causes: 4-7 year-olds at chance with four candidates; only 8-10 year-olds beat it. A category-membership version stays at chance (27%) [K04]. "Child as scientist" holds for small systems, not for diagnosis over several causes.
- Predicting evidence from known structure is hard: 12% right on all four in Schulz Exp 4 [a07].
- Older work (Chen and Klahr 1999, Kuhn) found older children and adults design controlled experiments poorly when asked explicitly [a14, M].

**Moderators.**
- Number of candidate causes (2 vs 4): cliff near age 8 [a10].
- Rule type: AND harder than OR for passive adults and for LLMs [K06, K08].
- Content: blicket and butterfly show the age effect; the baby-dinosaur category task does not [b22].
- Who teaches: hidden functions found Direct 0.50, Indirect child 0.75, Indirect adult 1.31, Intentional 1.00 [d05].
- Noise: p=0.70 activation removes scaffold gains [K19].
- Thinking mode: counterexample prompts help thinking models; small or mixed for non-thinking [d07].

**Interventions that worked (with caveats).**
- Large seeded hypothesis pool, text blicket [K09], single source.
- Think-in-Opposites (Qwen3, Wason and blicket), one lab, not token-matched [K10].
- Context graph (Claude Sonnet 4.5), one company lab [K13].
- Final-hypothesis check (CausaLab) [K14].
- Symbolic interpreter filter in hypothesis refinement [c20, c21].

**Did not work.**
- Chain-of-thought for PaLM on blicket (2022) [c18]. Zero-shot CoT hurt on ACRE (73.2 vs 77.8) [d15].
- Self-consistency N=5 on ACRE: 77.0 vs 77.8 standard [d15].
- Higher reasoning effort on 8-object AND exploration [d03].
- Context graph alone on pooled raw accuracy (77.3 vs 87.3%). It met the exactly-N trap more often (21.8% vs 10.9% exposure); its reasoning accuracy was 98.7% vs 97.5% [b21].
- Scaffold under noise [K19].
- A stats-modeling tool (Box's Apprentice) gave no consistent gain [c24].
- Equal-token self-refine and Reflexion vs repeated sampling on math [d10].
- Distilling counterexample behaviour: less than prompting (0.77 vs 0.86 at 32B; 0.34-0.38 vs 0.40 at 8B) [c14], and outside our no-training rule.

**Replication status.** No large-sample or multi-lab replication of child causal inference was found. Alderete has no outside replication. Jhaveri's prompt has none; only the correlation has one [K21, d18].

## 6. Language models

**2021-2023 models.**
- Vision models on ACRE learn covariation (up to 87% on indirect queries) and fail screening-off and backward blocking [c19, d14]. The backward-blocking row spans 23.91% to 99.80% across ten models; which model is which was not read.
- RL and imitation agents on the blicket benchmark: Decision Transformer forced-choice 0.64-0.77 (chance 0.5); reward 0.16 to 2.37 with 15 forced exploration steps; behaviour cloning 0.55-0.68 [a21, b13, c17].
- GPT-3 and PaLM: given the hypotheses they pick structure right but name wrong blickets; CoT did not help PaLM; 1-8 trials per cell, no statistics [c18].
- GPT-3 failed a blicket intervention task and showed no directed exploration (Binz and Schulz) [c26].
- GPT-4 75.9% innovation vs adults 95.7% [K11].

**2025 models (text blicket).**
- AND worse than OR; 8 objects worse than 4; oracle 1.0; longer responses go with lower accuracy [c01-c03].
- LMs behave like adults, not 4-year-olds, on the ambiguous-evidence task: they prefer OR when evidence supports AND [c04].
- Children explore the same under AND and OR; LMs explore less under OR [c05].
- Info gain rho=0.76 with success [c02].
- What changed it: oracle data (partly), a larger seed pool of hypotheses (gap gone at 16-96 seeds), reasoning models (deepseek-reasoner). What did not: higher effort in o3-mini/o4-mini made 8-object AND worse [d03].

**2026 models.**
- gpt-5 and deepseek-reasoner are near-perfect on OR with active exploration; AND is still below top humans; deepseek-chat and o4-mini only modestly above random on AND. LLMs do not consistently gain from choosing their own interventions; object errors are mostly near-misses [c09, c10, d02]. Per-model AND numbers are in figures only.
- Confirmation bias across 11-12 LLMs: success 6% to 78% in 45 turns (Jhaveri); GPT-5.2-Chat 75% vs best instruction-tuned DeepSeek-V3.1 41% (FALSIFYBENCH) [b18, d08]. Reasoning models beat instruction-tuned; small reasoning models do not.
- Think-in-Opposites: mean success 42% to 56%; Qwen3-32B blicket 0.57 to 0.86; helped in all 11 model settings on Wason, Dual-Goal in 8 of 11 [d07]. Non-thinking: small or negative.
- CausaLab: GPT-5.2-high 92% task accuracy but 0.471 all-edge F1 at 6 nodes; 64% at 7 nodes; half the intervention budget unused; one check lifts 4-node accuracy 48% to 60% [c25]. RAUMA snippet: picking what to test is the easy part (93% surrogate-optimal), reading the outcome is where models fail [c27, M].
- Scaffolds: Alderete as above, with the noise boundary [d09]. Cost 30-50% above base; the 1,085-episode series cost about $807 [b20, d09].
- BoxingGym: all LLMs struggle; larger beats smaller; instruction-tuned beat reasoning-tuned small models [c24]. A learned intervention policy (ACE) beats Bayesian OED on synthetic SCMs (5-node median loss 0.61 vs 1.99) but is trained, not prompted [c28].
- Bayesian teaching (fine-tuning) fixes belief updating across rounds (Bayesian assistant ~81% final round vs LLMs ~37-58%) [c23]; outside our no-training limit.

**Token-matched evidence.** None on blicket. Nearest: Mirzaei (0 of 36 better, 10 worse for self-inspection vs repeated sampling, math, small models) and Leins (at most +4.6 points at 2-4x tokens) [d10, d11]. Gains in Jhaveri, Alderete, Qiu and Piriyakulkij are not token-matched.

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested. Parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Log the share of S4 tests that lie outside the current hypothesis (I:C); flag runs where it stays near zero.** Part S5/G, feeds S7. [E] K18. Evidence d07, d08, c12. A diagnostic, not a new step; costs nothing.
2. **S5 cites the failing output and is driven by code-located contradictions.** Already G2. This literature supports it: models choose tests well but fail to read results (c27, snippet) and rarely check the final hypothesis against data (c25). Part G2/S5. [E] as G2; the specific support is [S].
3. **Pools of candidate rules contain more than one rule form (at least OR and AND) in S2/S3.** Part S2/S3. [E] K08: the disjunctive bias persists across families and sizes (c01, c04, b16, c09). The large-pool effect itself is [S].
4. **Do not rely on the model to re-score earlier evidence after a later result explains it away; replay the full evidence log in code at S5.** Part S5/memory. Design choice [S]; the human finding is [C] (K03, a06, d14).
5. **Choose each test after seeing the previous result; do not plan a batch up front.** Part S4/S5. Human evidence [S] (d01), consistent with the [E] LLM correlation of info gain with success (c02). Default, not a proven gain.

### Test first (each has a row in UNKNOWNS.md)

- Counterexample step in S5. [S] K10. d07, c13, c14. Qwen3 only, not token-matched.
- Enumerated hypothesis pool (16-96) with code elimination at S3/S4. [S] K09. b16, c06, d03.
- Final data-consistency check before commit at S8. [S] K14. c25, c20, d15.
- REVISE against N independent attempts plus a consistency check, equal tokens. [O] K17. Nothing measured.
- Widening monitor on contradiction. [S] K13. a24, b20, d09. Fails under noise [K19].
- Typed context graph as S5 state. [S] K13. b21 shows its raw-accuracy cost.
- Explicit list of rule forms handed to the agent. [S] K07. b12.
- Directive vs open exploration prompt (pedagogical narrowing). [S] K15. No LLM test (d17).
- Repeat-and-tally under noise. [S] K19. Untested anywhere.
- Hypothesis-count cliff (2, 4, 8 causes). [S] K04.

## 8. Concrete tests on our bench

All arms get equal total tokens, including setup, critique, monitors and consistency checks. Report pooled accuracy, not subsets (K13). Use the schema's own model, in thinking and non-thinking settings (K10).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Hidden-rule blicket puzzles: 4 and 8 objects; OR, AND, XOR; 60+ items per cell | (a) plain; (b) N independent runs + data-consistency check, picked by code; (c) REVISE loop citing failing output; (d) REVISE + counterexample step | Final rule accuracy; tests-to-solve; I:C | (d) over (c) +5 to +15 points on thinking models; (c) over (b) uncertain, K17 predicts none |
| T2 | AND rules, 8 objects | (a) default; (b) enumerated pool of 32 hypotheses with code elimination | AND accuracy; AND-OR gap | Gap shrinks to under 5 points |
| T3 | Items with a mid-run rule switch | (a) plain; (b) typed graph state; (c) graph + contradiction monitor | Pooled and post-switch accuracy; trap exposure | (c) +3 to +10 pooled; raw accuracy must not fall (b21) |
| T4 | Noisy machines, activation 0.7 and 0.9 | (a) plain; (b) repeat-and-tally, no scaffold; (c) full scaffold | Accuracy; tests per hypothesis | (b) beats (a) and (c) at 0.7; scaffold alone ~no gain (K19) |
| T5 | Backward-blocking form (AB+ then A+) | (a) sequential updating; (b) code replay of full log | Share that correctly downgrade B | (b) near 100%; (a) lower |
| T6 | AND items, same tests | (a) agent picks one test at a time seeing results; (b) agent writes all tests first; (c) agent reads a fixed transcript | AND identification | active > observer > proposer (human: 0.69, 0.45, 0.12) |
| T7 | Multi-function hidden-rule tasks | (a) open exploration prompt; (b) directive plan prompt | Distinct hypotheses explored; functions found | (b) narrower search, lower recall, faster on the shown function |
| T8 | 2, 4, 8 candidate causes | S5 loop on vs off | Accuracy per size | A cliff, not a smooth decline (K04) |
| T9 | Items with all data available at commit | (a) commit; (b) forced consistency check, then commit | Accuracy | +5 to +12 (c25: +12 at 4 nodes) |

## 9. What does not transfer, and why

- **"Bayesian child" as a mechanism.** Group data fit an associative network and probability matching [a06, b04]. Treat Bayes as a design metaphor (K02).
- **Child-over-adult flexibility.** Part of it is a passive-observation artifact in adults [d01]. An LLM is not a child: its OR bias resembles the adult one, not the child's [c04]. "Be more childlike" is not an operational instruction. The useful pieces are a flat prior and elimination.
- **Child exploration under cost.** Children use more steps than information-gain agents and do not optimise cost [a20]. Our agent pays tokens.
- **Developmental stages and mixed strategies.** Not testable on one agent trace (K16).
- **Infant looking-time findings.** Hard to interpret and unreplicated (a11, b26).
- **Fine-tuning results** (distilling counterexample behaviour; Bayesian teaching). Outside the no-training rule [c14, c23].
- **Small deterministic worlds.** Child results are 2-4 variables, deterministic, cells of 12-25, US museum or preschool samples [b01]. Real problems have noise, many variables and open hypothesis spaces. A pool of 16-96 may not scale [c06].
- **Scaffold gains from one lab on one model** (Claude Sonnet 4.5 plus Haiku, hand-written monitors, no cross-model run) [d09].
- **Old LLM results.** 2022-23 numbers describe obsolete models (K11).
- **Pedagogy findings.** One preschool toy with hidden functions; no LLM analogue tested [d17].

## 10. Open questions

1. Does a REVISE loop beat N independent attempts at equal tokens on blicket-type induction with current models? (K17; nothing measured.)
2. Is the AND-OR gap caused by hypothesis-space size or by prior bias? Seeding changes both at once [d03].
3. Do the Alderete and Jhaveri interventions replicate outside their labs and on other model families? [K21]
4. Original numbers for Gopnik 2001, Sobel 2004 and Denison 2010 are still second-hand (paywalled) [d16].
5. Do adults and LLMs retroactively revise (backward blocking) when asked to re-score? Why did adult B ratings not drop in Benton and Rakison? [K03, d17]
6. Does the child-over-adult result hold under active exploration? Samiei has no child arm [d01].
7. What is the S5-specific error profile when an agent confirms instead of falsifies? Partly answered: the I:C-success correlation holds in thinking and non-thinking models, but prompt effects are mainly in thinking models [d07].
8. Do effects hold with more than 4 uncertain causes? Noise result: scaffold gain vanishes at p=0.70 [d09].
9. Does pedagogical framing have an analogue in directive system prompts? [d17; d06 abstract only]
10. Why did thinking mode raise success without raising I:C? [d07]
11. Why does higher reasoning effort hurt exploration in some models? [d03]
12. Is the blicket-LLM literature too narrow (one author group)? [d18]

## 11. Sources

[V] opened and read. [M] snippet, abstract or second-hand only.

- [V] Gopnik and Wellman (2012) Reconstructing constructivism. Psych Bull 138(6). https://pmc.ncbi.nlm.nih.gov/articles/PMC3422420 (read to character 100,000 of 222,442)
- [M] Gopnik, Sobel, Schulz, Glymour (2001) Causal learning mechanisms in very young children. https://doi.org/10.1037/0012-1649.37.5.620
- [M] Sobel, Tenenbaum, Gopnik (2004) Children's causal inferences from indirect evidence. https://doi.org/10.1207/s15516709cog2803_1
- [M] Denison, Bonawitz, Gopnik, Griffiths (2010) Preschoolers sample from probability distributions (via review). https://pmc.ncbi.nlm.nih.gov/articles/PMC3422420
- [M] Bonawitz et al. (2010) Just do it? (via review). https://pmc.ncbi.nlm.nih.gov/articles/PMC3422420
- [M] Gweon and Schulz (2011) 16-month-olds rationally infer causes of failed actions. Science 332 (via review). https://pmc.ncbi.nlm.nih.gov/articles/PMC3422420
- [M] Xu and Garcia (2008); Kushnir, Xu, Wellman (2010) (via review). https://pmc.ncbi.nlm.nih.gov/articles/PMC3422420
- [M] Schulz and Bonawitz (2007); Cook, Goodman, Schulz (2011) (via review). https://pmc.ncbi.nlm.nih.gov/articles/PMC3422420
- [M] Seiver, Gopnik, Goodman (2013) (via review). https://pmc.ncbi.nlm.nih.gov/articles/PMC3422420
- [M] Liu et al. (2007); Siegler (1995, 2007) (via review). https://pmc.ncbi.nlm.nih.gov/articles/PMC3422420
- [V] McClelland and Thompson (2007) Using domain-general principles to explain children's causal reasoning. https://doi.org/10.1111/j.1467-7687.2007.00586.x
- [V] Schulz, Gopnik, Glymour (2007) Preschool children learn causal structure from conditional interventions. https://doi.org/10.1111/j.1467-7687.2007.00587.x
- [V] Sobel, Yoachim, Gopnik, Meltzoff, Blumenthal (2007) The blicket within. https://doi.org/10.1080/15248370701202356
- [V] Weisberg, Choi, Sobel (2020) Of blickets, butterflies, and baby dinosaurs. https://doi.org/10.3389/fpsyg.2020.02210
- [V] Benton and Rakison (2013) Causal reasoning in infants and adults: revisiting backwards-blocking. https://escholarship.org/uc/item/7b8730jz
- [V] Gopnik et al. (2017) Changes in cognitive flexibility and hypothesis search across human life history. https://pmc.ncbi.nlm.nih.gov/articles/PMC5544286/
- [M] Lucas, Bridgers, Griffiths, Gopnik (2014) When children are better (or at least more open-minded) learners. https://www.research.ed.ac.uk/en/publications/when-children-are-better-or-at-least-more-open-minded-learners-th/
- [V] Bonawitz et al. (2011) The double-edged sword of pedagogy. https://pmc.ncbi.nlm.nih.gov/articles/PMC3369499/
- [M] Beckers et al. (2009) Three-year-olds' retrospective revaluation. https://doi.org/10.1027/1618-3169.56.1.27
- [V] Forward and backward blocking in statistical learning (PLoS One 2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11299817/
- [M] Perez and Derex (2026) Socially guided individual learning. https://doi.org/10.1098/rspb.2026.0619
- [V] Kosoy et al. (2022) Learning causal overhypotheses through exploration in children and computational models. https://arxiv.org/abs/2202.10430
- [V] Kosoy et al. (2022) Towards understanding how machines can learn causal overhypotheses. https://arxiv.org/abs/2206.08353
- [V] Yiu, Kosoy, Gopnik (2023) Imitation versus innovation. https://arxiv.org/abs/2305.07666 ; published 2024, https://doi.org/10.1177/17456916231201401
- [V] GX-Chen et al. (2025) Language agents mirror human causal reasoning biases. https://arxiv.org/abs/2505.09614
- [V] Samiei et al. (2026) Human adults and LLMs as active explorers. https://arxiv.org/abs/2606.06464
- [V] Alderete, Benthall, Xu, Xing (2026) Separable pathways for causal reasoning. https://arxiv.org/abs/2604.20039
- [V] Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to falsify. https://arxiv.org/abs/2604.02485
- [V] Bertolazzi, Tentori, Bernardi (2026) FALSIFYBENCH. https://arxiv.org/abs/2606.04751
- [V] Zhang et al. (2021) ACRE. https://arxiv.org/abs/2103.14232
- [V] Qiu et al. (2024) Phenomenal yet puzzling. https://arxiv.org/abs/2310.08559
- [V] Wang et al. (2024) Hypothesis search. https://arxiv.org/abs/2309.05660
- [V] Piriyakulkij et al. (2024) Doing experiments and revising rules with natural language and probabilistic reasoning. https://arxiv.org/abs/2402.06025
- [V] Qiu et al. (2025/26) Bayesian teaching. https://arxiv.org/abs/2503.17523
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540
- [V] Yang, Zhang et al. (2026) CausaLab. https://arxiv.org/abs/2605.26029
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576
- [M] Hieu (2026) RAUMA (snippet). https://neurips.cc/virtual/2026/156578
- [V] Cooper and Velasquez (2026) Active Causal Experimentalist via DPO (abstract and intro). https://arxiv.org/abs/2602.02451
- [V] Mirzaei (2026) Sample more, reflect less. https://arxiv.org/abs/2607.28576
- [V] Leins et al. (2026) When does LLM orchestration pay off? https://arxiv.org/abs/2608.00685
- [V] arXiv search listings, 31 Oct 2026 (negative results for gaps 5 and 9). https://arxiv.org/search/?query=blicket&searchtype=all
