# Exploration and spontaneous experiments: deep document

*Subfield A14.03 (developmental cognitive science). Built from evidence_a-d.jsonl, claims.jsonl (K01-K31) and critique.md in this folder. Evidence ids (a01, b12, c24, d06 ...) point to lines in the evidence files. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Human data and LLM data are kept apart. Nothing here is added to SCHEMA.md until its test passes (see UNKNOWNS.md).*

---

## 1. What it is

**The question.** When a young child plays with a new toy, is the play random, or does it work like a small experiment? The founding answer (Cook, Goodman, Schulz 2011) is: it depends on the evidence. If the child has already seen clear evidence about which part causes an effect, play is broad and unfocused. If the evidence leaves two causes tied, a good share of children do the one thing that splits them apart. [a01, b02]

**The founding task.** A machine lights up and plays music when beads are placed on it. Children first learn a base rate. In the **All Beads** condition every bead works. In the **Some Beads** condition only some beads work. Then they see a stuck pair of beads activate the machine. In All Beads this tells them nothing new. In Some Beads one bead of the pair may be a dud, so the evidence is ambiguous. Then the child plays alone. The informative act is to pull the pair apart and try each bead alone. [b01, b26]

**Why it matters for our agent.** Our schema has two places that depend on this:
- **S7 discriminating test.** When two candidate rules still fit, run the one input where they differ. Cook gives the human case for firing that test only when the rules are tied.
- **Open-mode S3.** Open-ended exploration. The human data say useful exploration is selective (one critical action rises, breadth does not), and that the right selector may differ between a small closed rule set and an open world. [K03, K18]

**What this document is not.** It does not repeat heuristics, worked examples, epistemic action, value of information, diagnosticity, or the other parallel subfields. It links to them only where they touch (section 7).

**Honest headline.** The founding result is two experiments from one lab (N=60 and N=40). No direct replication and no failed replication was found among 112 citing records in Europe PMC (OSF and Many Labs registries not checked). The result is strongly supported by a *family* of conceptual relatives (confounded evidence raises focused play; effort tracks how hard rivals are to tell apart), but the specific ambiguity gate has not been tested on LLMs by anyone we could find. [K01, K25, d01, d12]

---

## 2. History and theories in depth

### 2.1 The line of work (all from one lab family unless noted)

1. **Schulz and Bonawitz 2007, "Serious fun."** Children (N=64, mean 57 months) played longer with a familiar toy whose causal evidence was confounded than with a new toy. Evidence that was clear sent them to the new toy. Three controls (matched effects, matched trials, no independent play) ruled out boredom, missing independent play, and simultaneous effects. 75% of the confounded group (12/16) moved each lever separately in free play. [a08, a09] I read the author manuscript, not the journal copy.
2. **Gweon and Schulz 2008, "Stretching to learn."** N=32. After confounded evidence, children paid a movement cost to play on the far side of a mat (variable play). After clear evidence they stayed on the near side: 10/16 near in Unconfounded vs 2/16 in Confounded, chi2(1,N=32)=8.53. Total play time did not differ (52.19 vs 52.75 s). The authors leave open "less variable when unambiguous" vs "more variable when confounded". [b06]
3. **Cook, Goodman, Schulz 2011** (the founding paper, Cognition 120:341-349). Ambiguous evidence does not just raise play. It raises one targeted act. Section 3 has the numbers. [a01-a07]
4. **Bonawitz et al. 2011, "Double-edged sword of pedagogy."** Teaching one function narrows exploration. Boundary on Cook: the *source* of the information changes what children test. [a12, a13]
5. **Bonawitz, van Schijndel, Friel, Schulz 2012.** Ambiguity is relative to a held theory. Children with a theory explore more when evidence contradicts it. Children with no theory prefer novelty. [a15]
6. **Schulz 2012 review (TICS).** Frames exploration after surprise and after confounding as one Bayesian principle: the learner is uncertain when two or more hypotheses have about equal posterior. Lists early-appearing practices: explore when evidence is confounded or surprising, isolate candidate causes, use sampling information, weigh teaching against self-exploration. The author says no single formal model yet gives all and only these practices. [a10]
7. **Siegel, Magid, Pelz, Tenenbaum, Schulz 2021.** Play time tracks how hard two hypotheses are to tell apart by the child's own senses. A graded, dose-response version of Cook's switch. [a14, b09, d04]
8. **Kosoy et al. 2022 (CLeaR).** First direct test of information-gain policies against children on a blicket game. Children do not look like ideal information gatherers. [a17]
9. **LLM era, 2022-2026.** Binz and Schulz 2022 (GPT-3 psychology), Kosoy 2023 (LaMDA), GX-Chen 2025 (language agents are poor causal explorers), Pan 2025 (Little Alchemy 2), Jhaveri 2026 (confirmation bias), Samiei 2026 (adults and LLMs as scientists), Piriyakulkij 2024 (Zendo), Alderete 2026 (typed scaffold). Section 6.

### 2.2 Competing accounts of why children do it

| Reading | Claim | Support | Against or untested |
|---|---|---|---|
| **A. Expected information gain (authors' account)** | Children pick the action with the highest expected entropy drop over live hypotheses. | Cook's model fits the pattern of who isolates. Children choose the isolating act from a menu (Lapidow and Walker 2020, abstract only). [a02, d02] | Kosoy 2022: children's play matches neither info gain nor reward; they repeat tests and stop early. [b10, b11] |
| **B. Cheap trial and error** | Ambiguous-condition children happen to touch beads one at a time as part of ordinary play. | Strict criterion, half the ambiguous group did not do it. | No paper tested it. [b22] |
| **C. Learning within the session** | Children infer in the session that isolating pays, by comparing the base-rate phase with the bead-pair phase. | Cook authors name it. Ruggeri 2019 and Legare 2012 fit session learning. [a07, d15, d19] | Not separated from A in any design found. |
| **D. Play serves other goals** | Skill, sensation, temperament. | Authors raise it. [a07] | Not testable in the Cook data. |

**Verdict.** No single reading wins. A and C are the live ones. The design confounds ambiguity, base rate and expected gain, so no design keeps ambiguity while removing the gain. [b26, K01]

### 2.3 Related theory

- **Theory-theory / "child as scientist"** (Schulz 2012, Gopnik line). Exploration serves belief revision. Surprise relative to a held theory drives it. [a10, a11]
- **Psychophysics view** (Siegel 2021). Exploration time is a function of perceptual discriminability, so effort is metacognitive: how hard is my own judgment? [a14]
- **Intrinsic motivation in RL** (Lidayan 2025, Kosoy 2020). Information gain, entropy and empowerment are three objectives. Which fits humans depends on the size of the world. [b15, b16]
- **Control-of-variables literature** (Chen and Klahr 1999). School-age children are often poor at designing controlled tests when asked. Cited as the contrast that makes Cook notable. Not opened. [b21]
- **Adaptive view of failure to control** (Bramley et al. 2022, n=104, ages 7-13). Not controlling variables can be adaptive when causes are sparse. Abstract only. [d17]

---

## 3. Core findings with exact numbers

Status key: [E] established, [S] single source, [C] contested. "Human" or "LLM" in the source cell.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Informative isolating test, ambiguous vs unambiguous evidence (Exp 1) | N=60, mean age ~54 months (range 46-64), 20 per cell. All Beads 1/20 (5%); Some Beads B 9/20 (45%); Some Beads AB 10/20 (50%). vs All Beads: chi2(1,N=40)=8.53 and 10.16, both p<.005. B vs AB chi2=0.10. 65% of All Beads never pulled the pair apart. Coder agreement 95%, kappa .90. Group means 53/55/54 months. | Cook 2011 (human) [a04, b02, c01] | [S] |
| Children invent the splitting act (Exp 2) | N=40, 20 per cell. Some Beads 9/20 (45%) vs All Beads 1/20 (5%), chi2(1,N=40)=8.53, p<.005. Act: stand the pair on end. Coder agreement 96%. Exp 2 followed a pilot observation. | Cook 2011 [a06, b04, c02] | [S] (same lab, same effect size, not independent) |
| Breadth of play does not rise | Action categories ~3.83 / 4.06 / 3.95, F(2,60)=1.08 ns. Exp 2: 3.00 vs 2.78 ns. Only snapped-apart-pair action differed: 63% vs 18%, chi2(1,N=40)=9.37, p<.005. | Cook 2011 [a05, b03] | [S] |
| Exclusions and partial samples in Cook | 7 children excluded and replaced (6 experimenter error, 1 language). Warm-up video data exist for only 17, 16, 12 children. No multiple-test correction on planned comparisons. | critique.md | note |
| Confounded evidence raises play with the familiar toy | N=64, mean 57 months, 16 per cell, 60 s. Confounded vs Matched-for-Effects chi2(1,N=32)=8.13 p<.01; vs Matched-for-Trials 6.15 p<.025; vs No-Independent-Play 4.5 p<.05. Familiar > novel within Confounded t(15)=2.79 p<.01. 12/16 (75%) moved each lever separately. | Schulz and Bonawitz 2007 [a08, a09] | [S] |
| Confounded evidence raises variable play | N=32. 10/16 near side (Unconfounded) vs 2/16 (Confounded), chi2=8.53, p<.003. Play time equal. 7/16 (44%) tried each block on each side. | Gweon and Schulz 2008 [b06] | [S] |
| Play effort tracks discriminability | 16 contrasts, 7 experiments. Model vs play r=0.95 (video), 0.89 (motion sensor), across condition means. Pooled beta=0.24, CI [0.18, 0.30]. Marble count did not predict play, beta=0.0065. 75-85% of children explore longer on harder contrasts (Exp 4-7: 19/24, 21/24, 18/24, 19/24). N is 168 (184 recruited minus 16 excluded); abstract says 160. Exp 7 preregistered. | Siegel 2021 [a14, b09, d04] | [S] (one lab; museum; aggregated r) |
| Prior theory x evidence | 95 children aged 6-7 and 31 aged 4-5. No-theory: novel toy preferred, F(1,29)=9.43, p<.01, no condition effect. Theorists: interaction F(1,59)=6.02, p<.05. 11/30 (37%) changed predictions after contradicting evidence. Center Theorists showed no selective magnet appeal (50% vs 56%). | Bonawitz 2012 [a15] | [S] (second lab, van Schijndel 2015, supports, abstract only: 100% vs ~50% unconfounded informative test first) |
| Teaching narrows exploration | N=85 (20 per group). Play time 119.2 s (taught) vs 179.6, 132.7, 205.7. Action kinds 4.00 vs 5.30, 5.90, 6.15 (F(1,81)=9.39, p<.01). Exp 2, N=64: overheard teaching for a similar child cut action kinds 3.94 vs adult-learner condition. | Bonawitz 2011 [a12, a13] | [S] |
| Not knowing the hypothesis space hurts | N=85, ages 4-5, 20-23 per cell. Data settle the rule: 71% (space given) vs 32% (not given), p=0.002. Actions 14.07 vs 10.58. Time 178.65 vs 195.38 s. Tested the empty machine 17.7%/17.5%; reordered same set 66.7%/65%. | Kosoy 2022 [a17, b10, c03] | [S] |
| Ideal info-gain agents differ from children | Agents always collect enough data in fewer steps. Children take more steps and often stop short. | Kosoy 2022 [b11, c04] | [S] |
| Recognising confounding is not choosing a control | N=57. Controlled choice on both two-variable trials 46%, one 40%, none 14%; chance chi2(2)=13.49, p=.001. Unrelated to detection. | Moeller 2022 [d03] | [S] |
| Informative action chosen from a menu | Ages 4-6, gears. Clear preference for removing one gear; kept when less pleasing. Abstract only. | Lapidow and Walker 2020 [d02] | [S] (unopened numbers) |
| Passive plan without own outcome is worst (adults) | N=306 (102 per cell). Conjunctive object ID: Active 0.69, Observer 0.45, Proposer 0.12. Rule choice 0.82, 0.69, 0.57. | Samiei 2026 [b12, c19, d08] | [S] (Proposer saw another person's outcomes) |
| Free exploration helps later goal search | Maze coverage 22/44/71%; steps to goal 95/89/66. Preliminary workshop. | Kosoy 2020 [b16] | [S] |
| Information gain fits small closed sets; entropy and empowerment fit open worlds | Crafter, 26 children 8+: breadth-depth rho=0.51 (p=0.01) children, -0.27 adults. Goal talk vs exploration rho=0.8 unadjusted, children only. | Lidayan 2025 [b15] | [E] with Pan 2025 |
| LLMs choose tests poorly | See section 6 table. | many | [E] |

---

## 4. Mechanisms and models

### 4.1 Expected information gain (Cook's model) as code

Setup: a set of hypotheses H1..Hn with prior P(H). An action A and possible data D. A likelihood table P(D | A, H).

```
entropy(P) = -sum p log2 p
IG(D, A)  = entropy(P(H)) - entropy(P(H | D, A))      # drop in uncertainty
EIG(A)    = sum_D  P(D | A) * IG(D, A)
P(D | A)  = sum_H P(D | A, H) * P(H)
choose A* = argmax_A EIG(A)
```

[a02] In the bead task: 4 objects of unknown status, 3 actions (2 single-object, 1 confounded pair). The second term P(D | A, H) matters only when actions cannot isolate variables one to one. With an All Beads prior there is one live hypothesis, so EIG of every action is about zero and play stays broad. With a Some Beads prior and a stuck pair, two hypotheses tie and the single-bead action has high EIG.

**Engineer's recipe for S7:**
1. Keep the live rule list from S2 (1 to 4 rules).
2. Run each rule on the attempts' outputs, or on candidate probe inputs. Group rules that agree.
3. If the number of distinct output groups on the probe set is 1, stop. No test is needed (the "All Beads" case).
4. If 2 or more groups, score each candidate probe by EIG (or, simpler, by how evenly it splits the live rules). Run the best probe in code, drop the rules it contradicts.
5. Repeat until one group is left or the probe budget is spent.

The evidence for step 4 being done in code and not by the model: Zendo experiment choice by code-computed InfoGain scored 6.55/8 vs 4.72/8 when the LLM picked and 5.84/8 for random. [d06, K30]

### 4.2 The ambiguity gate

Cook's switch is a gate: test when the live set is tied, do not test when one rule dominates. Operational form:

```
tie = (number of rules with posterior > 0.2 * max posterior) >= 2
if tie: run splitting probe (S7)
else:   skip
```

A toy break-even model (not an LLM measurement): a code gate beats always-split iff gate cost < (1 - tie rate) x split cost. With split 300 tokens and gate 20: accuracy per 1k tokens at tie rate 0.1 is 19.8 (gate), 12.7 (never split), 3.3 (always split). With gate 150 the gate falls to 5.5 and never-split wins at low tie rates. A model-judge gate with recall 0.5 reached 0.975 accuracy at tie 0.1 and 0.768 at 0.9, against 1.000 for the code gate. [d11, K29] The point: the gate must be cheap and computed by code, or it does not pay.

### 4.3 Graded effort from discriminability (Siegel)

Play time grows with how hard it is to tell two hypotheses apart. A noisy-perception model: the learner samples noisy evidence until the posterior gap clears a threshold, so closer rivals need more samples. [a14] Engineer's form: probes allowed = f(distance between rival rules' outputs). Rules that differ on many inputs need one probe. Rules that differ on one rare input need a probe aimed at that input. Test against a fixed budget at equal tokens. [K05]

### 4.4 Prior-relative surprise (Bonawitz 2012)

Surprise is measured against a held working rule, not against the world. No working rule, no surprise-driven test. Implementation: S2 writes a working rule; S4 or S7 compares each result against it; a mismatch triggers the targeted test. Without the rule the agent would drift to novelty. [a15, K06]

### 4.5 Narrowing by implication (Bonawitz 2011)

A helpful teacher who shows one function implies there are no others, so a Bayesian learner explores less. Inference: a stated hypothesis or a single worked example in context signals a closed space. For an agent this means a worked example may cut the number of distinct candidate classes in open-mode S3. No LLM test exists. [a12, K07, K31]

### 4.6 Two selectors for two regimes

- **Closed set, countable rules:** information gain.
- **Open world:** entropy (state diversity), empowerment (control over outcomes), novelty distance.

In Crafter, entropy and empowerment tracked human exploration; info gain did not consistently. In Little Alchemy 2, a regression shows models lean on uncertainty and ignore empowerment. In a grid world, mixing curiosity and competence beat either alone (abstract only). Working guess, untested: diversity first, control later. No switching rule exists in the literature. [b15, c24, d20, K18]

### 4.7 Enumerate and eliminate (GX-Chen)

Sample many distinct hypotheses as Python functions, reject duplicates to get a flat prior, tell the model to choose actions that eliminate as many as possible. Initial unique hypotheses 16, 32, 64, 96. More samples gave better exploration and removed the AND/OR gap (figure values only). Needs a hypothesis space expressible as code. [c17]

### 4.8 Code-side contradiction monitor (Alderete)

A monitor fires when an observation contradicts the confirmed model, forcing a re-test. Sensitivity 100% on post-switch correct episodes, PPV 90.5-100%. A typed 4-state machine ("context graph") raised reasoning-eligible accuracy 73.3% to 93.9%. [c29, c30, d10]

---

## 5. What holds up

### 5.1 Replications and failures

- **Direct replication of Cook:** none found. 112 Europe PMC citing records (2014-2026) scanned by title; none is a direct replication or a failed one. About 10 are conceptual extensions in other tasks: van Schijndel 2015, McCormack 2016, Lapidow and Walker 2020, Koksal 2021, Moeller 2022, Bramley 2022, Chu and Schulz 2023, Lapidow and Bonawitz 2023, Siegel 2021, Ruggeri 2019. Semantic Scholar and OpenAlex were rate limited; OSF and Many Labs not checked. [d01, K25]
- **Exp 2 inside Cook is not independent:** same lab, same toy, same effect size, followed a pilot observation. [b04]
- **Conceptual support (different tasks):**
  - Gweon and Schulz 2008 (N=32): variable play after confounding. [b06]
  - Schulz and Bonawitz 2007 (N=64). [a08]
  - van Schijndel 2015, second lab, shadow size: 100% vs ~50% (abstract only). [d16]
  - Siegel 2021: graded effort, preregistered Exp 7. [d04]
  - Lapidow and Walker 2020: informative action chosen when offered. [d02]
  - Koksal 2021, N=60, ages 5-6: ask for more information when evidence is confounded (abstract only). [d18]
- **Conceptual qualifications (tasks differ):**
  - Sobel et al. 2022 (ages 4-7, snippet only): children generating disambiguating data learn the structure more often, but children do not generally isolate variables. [d14]
  - Moeller 2022: detecting confounding and choosing a controlled test are unrelated. [d03]
  - Kosoy 2022: children given no hypothesis space settle the rule in only 32% of runs. [b10]

### 5.2 Weak spots in the founding result

1. Two experiments, one lab, N=60 and 40.
2. About half of the ambiguous group did not run the test; the criterion was strict (both beads tested separately).
3. Ambiguity, base rate and expected gain move together (confound). [b26]
4. Planned comparisons not corrected for multiple tests. The "one-tailed" claim for the null comparisons was not confirmed in the text read. [critique 3]
5. Warm-up data partial (17, 16, 12 children). [critique 2]
6. Children's mechanism belief was wrong (anything pressing the platform worked), so the design fit a folk theory, not the truth. [a06]
7. Competence (knew isolation from the start) vs on-the-spot inference not separated. [a07, b05]

### 5.3 Moderators with numbers

| Moderator | Effect | Source |
|---|---|---|
| Who supplies the information (teacher) | action kinds 4.00 vs 5.30-6.15; play 119 s vs 206 s | Bonawitz 2011 [a12] |
| Hypothesis space told or not | 71% vs 32% enough data | Kosoy 2022 [b10] |
| Owning the outcome (adults) | 0.69 vs 0.12 | Samiei 2026 [b12] |
| Held theory | theory-contradicting evidence raises play; no theory = novelty | Bonawitz 2012 [a15] |
| Discriminability | play follows it, r=0.95 on means; age effect on hard-vs-easy beta=-0.041 (CI -.45 to .40) | Siegel 2021 [a14, b09] |
| Rule type (AND vs OR) | children equal; LMs explore less on OR | GX-Chen 2025 [c16] |
| Age | 3-year-olds weak at choosing controls; 5-year-olds did not adapt without a cue (Ruggeri) | Moeller 2022, Ruggeri 2019 [d03, d15] |
| Culture, expertise, time pressure | none found | b23 |

### 5.4 Interventions that worked and did not (humans)

- **Worked:** giving the hypothesis space (71% vs 32%); letting people see the result of their own test (0.69 vs 0.12/0.45); free play before a goal (22/44/71% coverage, steps 95/89/66, preliminary). [b10, b12, b16]
- **Narrowed (cost):** teaching one function. [a12]
- **Did not help or hurt:** none of the human studies tested training isolation first with a Cook re-test. No study gave the informative action for free in the Cook design. [K31]

---

## 6. Language models

### 6.1 Did anyone run the Cook contrast on an LLM?

No. Searches of web, arXiv API and Europe PMC citations found no paper that gives an LLM ambiguous vs unambiguous evidence and counts how often it runs the single splitting test. Nearest items test falsifying tests (Jhaveri), ambiguous inference preference (GX-Chen), or active vs passive (Samiei). Coverage of 2025-2026 preprints is incomplete. [c31, d12, K25]

### 6.2 What LLMs do on nearby tasks

| Study (model era) | Task | Result |
|---|---|---|
| Binz and Schulz 2022 (GPT-3) [a18, a19, c07, c08] | 12 vignettes; horizon task | 12/12 vignettes correct or human-like (6 exact); blicket vignette right. Live: mean regret 2.72 vs humans 3.24; no directed exploration (horizon x reward-difference beta=-0.02, z=-1.47, p=.14; unequal-information beta=-0.15, p=.58); biased to options seen more. Causal chain answered like common cause. |
| Kosoy 2023 (LaMDA) [a21, c09] | developmental tasks, LRS 0-5 | Social/Moral 4.33; Perception 2.91; ToM 2.86; Causal 1.34 (worst). Blicket not-given conjunctive 1.12, disjunctive 0.44. Cited the authors' own blicket papers, so renamed "Zerpda". |
| Kosoy 2022 RL [c05, c06] | Blicket benchmark | Decision Transformer reward 0.16 (random data) vs 2.06 / 2.16 / 2.37 with 5 / 10 / 15 forced exploration steps; accuracy 0.67 to 0.77. GPT-3 and PaLM chose structure when given hypotheses but named too many blickets (tiny item counts). |
| Yiu, Kosoy, Gopnik 2023 [a22, c10] | Tool innovation | Children (n=42) 85.2%, adults (n=30) 95.7% for unrelated functional object; association 88.4% / 84.9%. LLMs matched association, missed innovation (LLM numbers in figures). |
| Krishnamurthy 2024 [c26] | Bandits | GPT-3.5, GPT-4, Llama2 did not explore robustly. GPT-4 basic prompt suffix failures in >60% of replicates. 1 of 72 GPT-4 configurations worked (CoT, suggestive framing, external history summary). |
| GX-Chen 2025 [c11-c17, d07] | Interactive blicket, 4 or 8 objects, 2 blickets, 32 actions | OR far easier than AND across GPT-4o, 4o-mini, DeepSeek-V3, R1, QwQ, Gemma3 and across default, ReAct, Reflexion, CoT. Info gain rho ~0.76 with success; response length ~-0.30; early exit ~-0.35 (figure-read, points are model-prompt combos). Oracle trace helped AND but GPT-4o stayed below OR. Random end-of-episode progress: 0.968 OR / 0.964 AND (4 objects); 0.944 / 0.877 (8). LM rows 0.812-0.999 OR, 0.798-0.935 AND; some below random. Enumerate-and-eliminate removed the AND/OR gap (figure only). LMs explored less in the OR condition; children explored equally. |
| Pan, Xie, Wilson 2025 [c24, c25, d05] | Little Alchemy 2, 500 trials per LLM, 29,493 human players | Elements: LLaMA3.1-8B 9; 70B 25; GPT-4o 35; DeepSeek-R1 85; o1 177; humans 42 (51 over all trials). t vs humans: o1 9.71, R1 3.40 (reported p<.027, odd), GPT-4o -5.48, 70B -6.39, 8B -28.12. Temperature x uncertainty beta=2.911; temperature x empowerment 0.196 (p=0.286). SAE: uncertainty peaks layer 2, empowerment layer 72. Paper contradicts itself on R1 (abstract only o1). |
| Piriyakulkij 2024 [b14, d06] | Zendo (8 scenes) | Humans 5.26; ReAct 4.60; strongest 6.55. LLM-chosen experiments 4.52 / 4.72; random 5.03 / 5.84; code-InfoGain 5.35 / 6.55 (fuzzy / hard). Random proposer with 1 / 5 / 10 candidates reranked: 5.84 / 6.23 / 6.55. Batch plateaus at 15 hypotheses; online at 75. Compute in calls, not tokens. GPT-4 Turbo class. |
| Gandhi 2025 BoxingGym [c27] | 10 environments scored by EIG regret | All tested LLMs (GPT-4o, Claude-3.7-Sonnet, Qwen-2.5, OpenThinker) struggled at design and discovery. Explicit statistical models did not consistently beat plain GPT-4o. |
| Jansen 2024 DiscoveryWorld [c28] | 120 tasks | Humans 66% completion, 55% explanatory knowledge. Best agent (ReAct) 38% easy, 18% challenge. Hypothesizer: 34% of gold knowledge easy, 8% challenge. |
| Jhaveri 2026 [c21-c23, d09] | 2-4-6 rule discovery; blicket (192 episodes per cell) | Think-in-Opposites: 42% to 56% average over 11 LLMs on Wason. Blicket, thinking: Qwen3-8B 0.32 to 0.40; 14B 0.50 to 0.61; 32B 0.57 to 0.86; R1-Llama-70B 0.41 to 0.43; QwQ 0.80 to 0.82. Non-thinking: 8B 0.11 to 0.19; 14B 0.25 to 0.20; 32B 0.64 to 0.56; Llama-70B 0.78 to 0.82. Distilled 32B reached 0.77 (about 70% of the prompt gain); 8B 0.34. Wason tokens per turn, thinking: 8B +58%, 14B +13%, 32B +41%, R1-70B +12%, QwQ -17%. Incompatible-test share vs success rho 0.65 (thinking), 0.74 (non-thinking), figure-read. |
| Samiei 2026 [b13, c18, c20] | Active exploration, 6 LLMs, 24 trials per rule type | Mean tests AND / OR: humans 9.6 / 6.4; top human 8.5 / 3.8; gpt-5 10.2 / 7.7; gpt-5-mini 10.8 / 7.1; gemini-2.5-flash 13.5 / 9.7; deepseek-reasoner 8.2 / 6.8; o4-mini 6.7 / 4.2; deepseek-chat 12.3 / 11.9. gpt-5 and deepseek-reasoner near-perfect on OR; deepseek-chat and o4-mini modest on AND. Stronger reasoning models moved from 1-object to targeted 2-object tests. Latency, not tokens. |
| Alderete 2026 [c29, c30, d10] | Blicket with rule change, Sonnet 4.5 acts, Haiku 4.5 monitors; 1,085 trials | Reasoning-eligible: Base 73.3% (22/30), CG 93.9% (31/33; p=0.038, h=0.59), CG+DB 95.3% (41/43). Raw (110 per arm): Base 87.3%, CG 77.3%, CG+DB 89.1%. CG = 94% of reasoning-eligible gain. Exactly-N trap CG 28.0% vs CG+DB 6.0% (p=0.003). Stochastic condition: 76.7 / 76.7 / 73.3, no effect. One-tailed tests, preprint, vendor authors. |

### 6.3 What changed LLM behaviour, by how much

| Change | Effect | Status |
|---|---|---|
| Code picks the experiment by InfoGain | 6.55 vs 4.72 of 8 (+1.8 scenes) on Zendo | [S] |
| Enumerate hypotheses in code then eliminate | removes AND/OR gap (figure) | [S] but see K12 as [E] with related sources |
| Think-in-Opposites prompt | Wason 42% to 56%; blicket: one thinking model +0.29, others +0.02 to +0.11; non-thinking mixed (+0.08, -0.05, -0.08, +0.04) | [S] |
| Reasoning training / thinking mode | o1 177 vs GPT-4o 35 elements; gpt-5, deepseek-reasoner near top on OR; o4-mini few tests, modest AND | [C] |
| Oracle exploration data supplied | AND accuracy up for all models; GPT-4o still below OR | [S] |
| Typed state machine | +20.6 points reasoning-eligible (73.3 to 93.9), but raw accuracy fell when used alone (87.3 to 77.3) | [S] |
| Contradiction monitor | trap rate 28% to 6% | [S] |
| Higher temperature | no gain in useful exploration | [S] |
| External summarised history + CoT + suggestive framing | 1 of 72 GPT-4 bandit configurations robust | [S] |
| Giving the hypothesis space (children) | 32% to 71% settle rule | human only |

### 6.4 Reading the LLM picture

1. Plain LLMs under-explore or explore badly on interactive causal tasks. [E] K10 (five sources).
2. They show a disjunctive bias that adults share under passive evidence, but 4-year-olds do not. [E] K11.
3. Correlational finding: tests that could contradict the leading rule go with success. [E] K13.
4. Vignette passing is weak evidence of exploration skill. GPT-3 passed 12/12 vignettes and showed no directed exploration live. [E] K20.
5. Prediction is not experiment choice (BoxingGym, DiscoveryWorld). [E] K24.
6. Contamination: LaMDA cited the blicket authors. Any blicket test of ours needs renamed or new machines. [critique]

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established [E])

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| N1 | Choose tests in code from an enumerated rule list (EIG or split-evenness), not by asking the model which test is best. Model-chosen tests are worse than random on some tasks. | S7 | [E] | K10, K12; a17, b14, c13, c27, d06 |
| N2 | Force low-prior rules (the AND rules) into the S2 candidate set. LLMs favour OR; the gap closes when hypotheses are enumerated. | S2 | [E] | K11, K12; c11, c15, c17, c18 |
| N3 | Do not judge exploration skill from a text vignette; judge it from live loops with renamed machines. Track the vignette-vs-live gap. | G10 | [E] | K20; a18, c07, c09 |
| N4 | Log per-test info gain and the share of tests that could contradict the leading rule; both correlate with success. Longer replies and early exit correlate with failure. | log (section 6 of SCHEMA), G5, G11 | [E] | K13; c12, c21, c22 |
| N5 | Use a selector per regime: info gain at S7 (closed set), diversity or novelty distance at S3 (open set). Do not use temperature for diversity. | S3 / S7 | [E] for the regime split (K18); [S] for temperature (K17) | b15, c24, c25 |
| N6 | Model-vs-code check: test quality benefits from a code check that the proposed test actually splits the rules. | S7 | [E] by N1 | d06 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Ambiguity gate.** Fire the splitting test only when the code finds a tie in the live rule list; skip otherwise. Compare gate vs always-split vs never-split at equal tokens. | S7 trigger | [S] | K01, K02, K29; a01, b02, d11 |
| T2 | **Break-the-leading-rule step** in S7 (Think-in-Opposites style) with a code check that the test splits the rules. | S7 | [S] | K14; c21-c23, d09 |
| T3 | **Interleaved test-then-choose** loop vs batch plan of tests. | G2 | [S] | K15; b12, c19, d08 |
| T4 | **Resolve a live tie before moving to a new item** vs novelty-first. | G1 / S7 | [S] | K04; a08, b06 |
| T5 | **Probe budget scaled to rival distance.** | S7 budget | [S] | K05; a14, b09 |
| T6 | **Working rule written at S2 as the surprise reference;** compare S7 with and without it. | S2 / S7 | [S] | K06; a15 |
| T7 | **Code contradiction monitor** to trigger re-test, vs scheduled recheck. | G1 / S7 | [S] | K19; c29, c30, d10 |
| T8 | **Menu of candidate tests** including the splitter vs no menu. | S7 | [S] | K26; d02 |
| T9 | **Open-mode: worked example in context** narrows or widens candidate classes. | S3 | [S] | K07, K31; a12 |
| T10 | **Short open-mode S3 before the task** (free exploration) vs none, at equal total tokens. | S3 | [S] | K22; b16 |
| T11 | **Forced untried actions before selection.** | S3 | [S] | K23; c05 |
| T12 | **Reasoning mode for S7** vs chat mode at equal tokens. | S7 mode | [C] | K16; c24, c25, b13 |
| T13 | **Own-statement unsure vs code tie** as trigger. | S7 trigger | [S] | K27; d03, d18 |
| T14 | **Force a different reading of an object** in open mode. | S3 | [S] | K21; a22, c10 |

Cross-links to parallel subfields: S7 test choice and value of information (Value of information; Diagnosticity of evidence; Epistemic action); trigger and doubt (Expected value of control; Anomaly response); open-mode selection (Novelty and atypicality; Recombinant search); question wording (Question wording and presupposition). These documents are written in parallel; only links are noted here.

---

## 8. Concrete tests on our bench

All arms get the same token budget per item. Run on renamed machines or new tasks to avoid contamination (LaMDA cited the authors). Log tokens per state, tests run, EIG per test, and whether each test splits the live rules.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| **B1 Ambiguity gate (Cook analogue)** | Toy rule task with a stuck pair. Half the items have one dominant rule (All Beads), half have two tied rules (Some Beads). Build a closed rule list. | (a) plain model; (b) plain model plus stated rule list; (c) code gate: exact tie check then forced split. | Rate of the splitting test on tied vs dominant items; final rule accuracy per 1k tokens. | Plain model: little difference between tied and dominant (no LLM version exists). Gate: split rate near 100% on ties, near 0% on dominant; per-1k-token accuracy above never-split when the gate costs under (1 - tie rate) x split cost. |
| **B2 Gate vs always vs never** | Same items with tie rate 0.1, 0.5, 0.9. | gate, always-split, never-split. | accuracy per 1k tokens | Model predicts gate wins at 0.1 and 0.5; never-split beats an expensive gate at 0.1. Measure the real gate cost. |
| **B3 Code-chosen vs model-chosen test** | Blicket-style or Zendo-style closed rule sets, 4 and 8 objects, AND and OR. | LLM-chosen test; random; random proposer reranked by code EIG; LLM proposer reranked by EIG. | Steps to one live rule; final accuracy. | Code EIG beats model-chosen (Zendo gap was 1.8 of 8 scenes). Random reranked about equals LLM reranked. |
| **B4 Enumerate-and-eliminate** | Blicket with AND rules, 8 objects. | ReAct baseline; enumerate 16, 32, 64 hypotheses as code then eliminate. | AND accuracy minus OR accuracy; steps. | AND/OR gap shrinks with enumeration. Check at modern scale. |
| **B5 Break-the-leading-rule** | 2-4-6 and blicket. | plain; TiO prompt; TiO prompt plus code check that the proposed test splits. | rule discovery rate; incompatible-test share; tokens per turn. | Gain concentrated in thinking mode; tokens up 12-58% so equal-token check matters. |
| **B6 Interleaved vs batch** | Blicket tasks where the outcome depends on earlier tests. | interleaved test-then-choose; batch plan then see outcomes; yoked batch that sees mismatched outcomes. | final rule accuracy; tests used. | Interleaved above batch; yoked mismatched arm separates mismatch from lack of control. |
| **B7 Prior-relative surprise** | Items where a result contradicts the working rule, or confirms it. | with written working rule at S2; without. | rate of targeted test after contradiction vs after confirmation. | With rule: more targeted tests after contradiction. Without: no difference (children with no theory preferred novelty). |
| **B8 Worked example narrows S3** | Open-mode generation tasks. | no example; one example; one example plus "other solutions exist". | Distinct candidate classes (code-clustered). | Example in context narrows classes (Bonawitz analogue). No LLM test exists; it could go either way. |
| **B9 Probe budget by rival distance** | Pairs of rules differing on 1, 3, 10 inputs. | fixed probes; probes scaled to distance. | accuracy per 1k tokens | Scaled budget wins when distance varies widely. |
| **B10 Selector switch** | A task with a closed phase then an open phase. | EIG only; diversity only; EIG while more than one live rule then diversity. | success and novelty | Switch rule wins; none is tested in the literature. |
| **B11 Menu** | Closed-set items. | splitting test on a menu vs not. | rate picking split | Menu raises rate (children). |

---

## 9. What does not transfer, and why

1. **The 5% vs 45-50% numbers.** They are rates of a spontaneous act in 4-5-year-olds. An LLM may do the splitting act 0% or 100% of the time depending on the prompt. Do not target the rates. Target the sign of the gate.
2. **Free play as intrinsic motivation.** Children play for skill, sensation and fun. [a07] Our agent has no such drive. Use the logic (test when tied), not the motive.
3. **Play time as the measure.** Siegel and Gweon use time and movement cost. Our cost is tokens; the unit differs.
4. **Teaching narrows exploration by pragmatic inference.** The child infers the teacher is helpful and informative. LLMs may anchor on any text. The mechanism differs; test the outcome (B8). [a12]
5. **Preschool cognitive limits.** Children stop early and repeat tests (Kosoy). The agent's problem is different: under-exploration and OR bias. [b10]
6. **Child-like inefficiency as a goal.** Kosoy 2022 shows children differ from ideal info-gain agents and may optimise for a wider set of alternatives. Our agent has a known budget and should not copy that. [c04]
7. **Ambiguity from base rates.** In Cook, ambiguity came from a visual stuck pair plus a base rate. In text tasks the tie must be computed from the rule list. If the rule list is wrong, the gate is wrong.
8. **Vignette success.** GPT-3 passed text blicket vignettes and failed live. [a18, c07]
9. **The 2011 sample as proof of LLM behaviour.** Zero LLM studies replicate the contrast.
10. **Info gain for open worlds.** It fits small closed sets; entropy and empowerment fit big worlds. [b15]

---

## 10. Open questions

1. Has anyone replicated or failed to replicate the Cook bead contrast? OSF, Many Labs and CogSci proceedings not checked. [K25]
2. Does an LLM run the isolating test more often when evidence is ambiguous? No test found. [K31]
3. Is the trigger needed, or is always-splitting cheaper than the trigger? Only a toy model exists. [K29]
4. Which reading of Cook is right (A prior knowledge, B trial and error, C session learning)? No design separates them. [b22]
5. Does an LLM's hypothesis enumeration help at modern scale and equal tokens? Figure values only. [c17, d07]
6. Does the Samiei "own outcome" effect hold for LLM agents? Proposer confound unsolved. [d08]
7. Does Think-in-Opposites help only in thinking mode, and at what token cost? [d09]
8. Does a worked example narrow open-mode exploration (Bonawitz analogue)? [K31]
9. When should the selector switch from information gain to entropy or empowerment? [d20]
10. Unresolved numbers: Pan 2025 R1 vs humans (abstract vs text vs appendix); GX-Chen figure values (Q&A gain); Alderete model names and p-values (not re-checked); Siegel's exclusion counts. [critique, d04, d05]
11. Unopened sources must not be cited for numbers: Lapidow and Walker 2020, van Schijndel 2015, Koksal 2021, Legare 2012, Ruggeri 2019, Bramley 2022, Sobel 2022, Lucas 2014, Gopnik 2017, Schulz-Gopnik-Glymour 2007, Chen and Klahr 1999. [d02, d14-d19, a24, a25, b20, b21]
12. Culture, expertise and time pressure moderators: none found. [b23]

---

## 11. Sources

[V] = opened and read this session or the earlier session that produced the evidence files (as recorded in the evidence `opened` flag; the cross-check re-opened some). [M] = snippet, abstract or secondhand only.

**Human, founding and family**
- [V] Cook, Goodman, Schulz 2011, Where science starts. https://web.stanford.edu/~ngoodman/papers/CookGoodmanSchulz2011.pdf (a01-a07, b01-b05, b26, c01, c02)
- [V] Schulz and Bonawitz 2007, Serious fun (author manuscript). https://cocosci.dreamhosters.com/Liz/SchulzBonawitzInPress.pdf (a08, a09); journal: https://doi.org/10.1037/0012-1649.43.4.1045 [M] (b07)
- [V] Gweon and Schulz 2008, Stretching to learn. https://sll.stanford.edu/docs/2014_and_older_cogsci/2008_cogsci_Gweon_Schulz.pdf (b06)
- [V] Schulz 2012, Origins of inquiry (TICS). https://eccl.scripts.mit.edu/papers/TICS.pdf (a10, a11)
- [V] Bonawitz et al. 2011, Double-edged sword of pedagogy. https://cocosci.dreamhosters.com/Liz/Bonawitzetal11.pdf (a12, a13, b08)
- [V] Bonawitz, van Schijndel, Friel, Schulz 2012. https://cocosci.princeton.edu/Liz/BonawitzetalBalance12.pdf (a15); DOI https://doi.org/10.1016/j.cogpsych.2012.01.003 [M] (b19)
- [V] Bonawitz, Lim, Schulz 2007. https://cocosci.dreamhosters.com/Liz/BonawitzLimSchulz2007.pdf (a16)
- [V] Siegel et al. 2021, Nature Communications. https://pmc.ncbi.nlm.nih.gov/articles/PMC8203670 and https://www.nature.com/articles/s41467-021-23431-2 (a14, b09, b25, d04)
- [V] Kosoy et al. 2022, Learning causal overhypotheses (CLeaR). https://arxiv.org/abs/2202.10430 (a17, b10, b11, c03, c04)
- [V] Kosoy et al. 2020, Exploring exploration. https://baicsworkshop.github.io/pdf/BAICS_24.pdf (b16)
- [V] Moeller, Sodian, Sobel 2022. https://doi.org/10.3389/fpsyg.2022.800226 (d03)
- [V] Lidayan et al. 2025, Intrinsically motivated humans and agents. https://arxiv.org/pdf/2503.23631 (b15)
- [V, context only] Yiu, Allen, Ginosar, Gopnik 2025, Empowerment gain. https://arxiv.org/pdf/2512.08230 (b17)
- [M] Lapidow and Walker 2020. https://doi.org/10.1016/j.cognition.2020.104315 (d02)
- [M] van Schijndel et al. 2015. https://doi.org/10.1016/j.jecp.2014.11.008 (d16)
- [M] Koksal, Sodian, Legare 2021. https://doi.org/10.1016/j.jecp.2020.105080 (d18)
- [M] Legare 2012. https://doi.org/10.1111/j.1467-8624.2011.01691.x (d19, a24)
- [M] Ruggeri et al. 2019. https://doi.org/10.1016/j.cognition.2019.104013 (d15)
- [M] Bramley et al. 2022. https://doi.org/10.3758/s13423-022-02120-1 (d17)
- [M] Sobel et al. 2022. https://doi.org/10.1016/j.cogdev.2022.101194 (d14)
- [M] Gweon and Schulz 2008 per a23; Lucas 2014 and Gopnik 2017 via Kosoy (a25); Schulz, Gopnik, Glymour 2007 https://doi.org/10.1111/j.1467-7687.2007.00587.x (b20); Chen and Klahr 1999 https://doi.org/10.1111/1467-8624.00081 (b21)
- [V] Europe PMC citation list for Cook 2011, PMID 21561605, 112 records. https://www.ebi.ac.uk/europepmc/webservices/rest/MED/21561605/citations (d01)

**LLM and AI**
- [V] Binz and Schulz 2022/2023, Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (a18-a20, c07, c08)
- [V] Kosoy et al. 2023, Comparing machines and children (LaMDA). https://arxiv.org/abs/2305.11243 (a21, c09)
- [V] Yiu, Kosoy, Gopnik 2023, Imitation versus innovation. https://arxiv.org/abs/2305.07666 (a22, c10)
- [V] Kosoy et al. 2022, Towards understanding how machines can learn causal overhypotheses. https://arxiv.org/pdf/2206.08353 (c05, c06)
- [V] GX-Chen et al. 2025, Language agents are poor causal explorers (COLM). https://arxiv.org/pdf/2505.09614 (c11-c17, d07)
- [V] Samiei et al. 2026, Human adults and LLMs as scientists. https://arxiv.org/pdf/2606.06464 (b12, b13, c18-c20, d08)
- [V] Jhaveri et al. 2026, Failing to falsify. https://arxiv.org/pdf/2604.02485 (c21-c23, d09)
- [V] Pan, Xie, Wilson 2025, LLMs think too fast to explore. https://arxiv.org/pdf/2501.18009 (c24, c25, d05)
- [V] Krishnamurthy et al. 2024, Can LLMs explore in-context? https://arxiv.org/pdf/2403.15371 (c26)
- [V] Gandhi et al. 2025, BoxingGym. https://arxiv.org/pdf/2501.01540 (c27)
- [V] Jansen et al. 2024, DiscoveryWorld. https://arxiv.org/pdf/2406.06769 (c28)
- [V] Alderete et al. 2026, Separable pathways for causal reasoning. https://arxiv.org/pdf/2604.20039 (c29, c30, d10)
- [V] Piriyakulkij et al. 2024, Doing experiments and revising rules. https://arxiv.org/pdf/2402.06025 (b14, d06)
- [M] Lee et al. 2025 (NAACL) hypothesis diversity. https://arxiv.org/abs/2412.13422 (d13)
- [M] From Curiosity to Competence, arXiv 2507.08210. https://arxiv.org/abs/2507.08210 (d20)
- Own toy simulation (no LLM calls): D:/research_scratch/A14.03/tmp/A14.03_gate_sim.py (d11)

Critique note: the re-open pass in critique.md confirmed Cook, Kosoy, Siegel, Samiei and Jhaveri numbers. Alderete, GX-Chen and Pan were re-read in the gap pass (d05, d07, d10) for the numbers shown above, and their figure-only values stay unverified.

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 7 established claims: 6 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A14.03-K18** (reworded: the sources support less). Lidayan et al. do show entropy and empowerment (not information gain) track human exploration in Crafter, but Pan et al.'s Little Alchemy 2 regression uses uncertainty and empowerment only and never tests information gain, and neither source tests the 'info gain is right in closed hypothesis sets' half. Corrected claim: In a large open world (Crafter), entropy and empowerment track human exploration progress while information gain does not consistently (Lidayan et al., children and adults); in Little Alchemy 2 humans balance uncertainty and empowerment while most LLMs rely on uncertainty alone (Pan et al.; information gain not tested). Information gain as the test selector is supported in small closed hypothesis sets by separate studies (e.g. Zendo, blicket), not by these sources.
