# Alternative-explanation controls: deep document

*Subfield A18.02 of comparative cognition. Written from evidence_a-d.jsonl (ids a01-a30, b01-b30, c01-c28, d01-d25), claims.jsonl (K01-K38) and critique.md in this folder. Numbers re-opened in the critique pass are marked as confirmed there. No new searching was done for this document.*

---

## 1. What it is

Alternative-explanation controls are the design tricks that comparative psychologists use to rule out cheap explanations of an animal's success. A crow pulls meat out of a tube and avoids a trap. Did it understand gravity? Or did it learn "avoid the hole" by trial and error? Or "avoid the blue rim"? Or did it guess? Each rival gets a name, a differential prediction, and a control that would break it.

The subfield focus is the list from Taylor et al. (2009): the authors ruled out **chance, associative learning on cues, visual and tactile generalisation, and prior dispositions**. The method is called triangulation (Heyes 1993): train on one task, then transfer with the arbitrary features changed and the causal structure held fixed.

Why it matters for our agent. Guardrail G3 says a pass must be on something the answer was not fitted to. This subfield is the best worked-out practice for building that "something". The animal literature shows:

- how to build a ladder of held-out variants, each killing one rival explanation;
- how a control can itself be invalid;
- how a failed control can mean "too much load" and not "no ability";
- how tiny samples make controls fragile;
- how a result can fail to replicate when the order or the cue was confounded.

The LLM literature (2022-2026) reuses the same design. It takes tasks models "pass", changes the surface or the world rules, and measures the drop. This is the same logic as the trap-table.

Scope note. This document covers controls and held-out checks. Other subfields in the same run cover bias and debiasing, diagnosticity of evidence, and generation versus evaluation. We only note links.

---

## 2. History and theories in depth

### 2.1 Morgan's canon and the two mistakes

Morgan's canon says: do not explain behaviour by a higher faculty if a lower one will do. In practice it became "associative learning wins by default". Heyes (2012, a24, opened) calls two opposite errors by name:

- **association-blindness**: never considering associative learning;
- **simple-mindedness**: assuming it wins without a test.

Her rule: "there are no short-cuts to finding out about animal minds". Spell out each explanation in enough detail to make differential predictions, then test them. Neither side gets a default.

Ullman (2023, a27/c04) took the opposite stance for LLMs. The zero hypothesis should be skeptical. One principled failure outweighs many successes, like a model that gets 100 small products right and fails 213 x 261. This conflicts with the animal lesson that a failed control may only show task load (K24). The conflict is real and unresolved (see section 5).

### 2.2 Trap-tube founding work

- Visalberghi and Limongelli (1994): capuchins. After 120 trials, 1 of 4 solved by pushing food away from the trap. It kept doing so when the trap was inverted and non-functional. Read as a distance rule without understanding. (a08, second-hand, not opened.)
- Povinelli (2000): one chimpanzee avoided the trap and also acted as if the inverted trap were functional. (a08, second-hand.)
- Silva et al. (2005): adult humans also avoid the inverted trap when avoidance is free. So the inverted-trap control was conceptually flawed. The "wrong" response had no cost. This is a key lesson: a control must be checked for validity (a08).
- Seed et al. (2006), Tebbich et al. (2007): rooks with a two-trap tube, which removes the need for the inverted control. 7 of 8 solved; 6 of 7 failed far transfers; one passed. Tebbich 2007 (one-trap tube): 3 of 7 solved, none transferred. (a09, second-hand.)
- Martin-Ordas, Call, Colmenares (2008, a07, opened): 20 great apes did a trap-platform and a trap-tube task. 12 of 20 solved the platform, 8 of 20 the tube; 5 solved both. Correlation across tasks r = 0.13, p = 0.57, n = 20. Prior trap experience had no effect.

### 2.3 Taylor et al. 2009: the ladder

Taylor, Hunt, Medina, Gray (2009, a01-a06, b01, c01, opened and numbers re-opened in the critique). Six wild New Caledonian crows. Two-trap tube: pull the meat away from the hole that has a base (a trap). Three crows (Obo, Tiga, Slevin) solved it in under 150 trials, mean 103.3 trials (standard error 20.3, not an SD). Then four transfers:

1. Transfer 1: remove the two yellow discs. Transfer 2: remove the blue rim and recolour the discs black. 3 of 3 passed both.
2. Transfer 3: one functional trap (hole with base) and one non-functional trap (bare hole). 3 of 3 failed. They used the hole, not the base, as the cue.
3. The trap-table: different shape, colour and material. 3 of 3 solvers passed, correct on trial 1. The 3 crows that failed the tube also failed the table. This argues against a prior disposition to avoid holes.
4. A separate paper (b02, Taylor, Roberts, Hunt, Gray 2009): 8 naive crows, 20 trials each, did not avoid the trap on the table (all p > 0.05). That rules out a sampling bias. An inverted tube with the hole on top gave no end preference in 3 solvers. That rules out a spatial analogy.

First trials correct: 10 of 12 (3 birds x 4 transfers, not independent). The paper gives no test on that number. The binomial p = 0.0156 in the paper's transfer-3 analysis means the chance that all 3 crows have their highest latency or side-switching in transfer 3 (3 x 0.25). It is not a test of failing the transfer (critique correction).

The authors conclude chance, associative learning, visual and tactile generalisation and prior dispositions are "unlikely", not "ruled out". They say the knowledge is intermediate between weak and strong causal understanding. They lean on Shepard's generalisation law (more perceptual distance, less generalisation). That is an argument, not a measure.

### 2.4 Rival-mechanism logic in other crow work

- Taylor et al. (2011, a13-a15): a clean associative control. Pair the same discrimination with a causal link (stone dropping) and an arbitrary link (search task). Associative learning should not care. Large stone: 88% in first 20 drops versus 46% in the matched search task (chi2(1) = 6.13, p = 0.013). Water vs sand: 58% vs 56% at group level (p = 0.99), one bird 90% vs 55%. Preferences did not transfer to stick tools (exp 9: 46% vs 46%, p = 0.78).
- Taylor, Elliffe, Hunt, Gray (2010, a11-a12): metatool problem. Each simple mechanism gets its own prediction. Resurgence predicts re-probing the hole. Conditional reinforcement predicts the short stick, which had become punishing, dies out. Chaining needs training on each component. Component group: 3 of 3 solved on trial 1. Innovation group (n = 4): 2 solved on trial 1. Only one of four was clearly spontaneous.
- Taylor et al. (2010, a10/b05): string pulling. Blocking vision cut the pull-step ratio from 96.5% to 55.7% and errors rose about 10 times (Wilcoxon p = 0.0625, the minimum at n = 4). Naive crows: 1 of 4 solved. Mirror to restore feedback: 2 of 4 solved. Reading: a perceptual-motor feedback loop.
- Taylor, Knaebe, Gray (2012, b04): horizontal two-string task removes the food-moves-closer feedback. Humans 49/50 and 42/50. Crows: first trial 8/11 connected (p = 0.11), none pulled enough to move food. Pooled p = 0.037, no individual significant.
- Neilands et al. (2016, b08): signature testing. If crows understand force they drop heavy blocks first. 12 crows; only 2 innovated dropping; pre-test no weight preference (128 of 240 light, p = 0.167). After training 125/140 first choices heavy.
- Jelbert et al. (2019, b09): crows watched objects blown by a fan. First touch correct 35/48 (72.9%, p = 0.01) fan on vs 23/48 (47.9%) fan off. The paired fan-off control rules out unintended visual cues.
- Gruber et al. (2019, a23/b10): metatool redesign, each stage hidden, distractors added. 11 crows got the stick problem; 4 reached 16/20 with few errors, 4 more by trial 43. Preplanning checks: Aretha 12/14 (p = 0.013), Freddie 14/18 (p = 0.031). Many crows failed and needed experience.
- Boeckle et al. (2020, b11): crows plan for future tool use. 4 of 6 reached training criterion; 3 of 4 above chance in tests with novel pairings (Neptune 9/10, Triton 7/10, Uranus 7/10; Saturn 3/10).

### 2.5 The Aesop's fable line, and its control failures

- Jelbert et al. (2014, a16): six experiments. Passed: water vs sand 76.3% (p = 0.001), sinking 88.0%, solid 89.0%, wide/high 86.8%. Failed: narrow tube 39.3%, U-tube 48.9% (p = 0.79). Fixed task order, so earlier tasks may have helped later ones.
- Logan et al. (2014, a17-a19, b06): added three controls.
  - Coloured U-tube: 1 of 5 passed; uncovered U-tube (connector visible): 0 of 5. Kitty's pass was a colour-cue association.
  - Platform task with no water: crows still chose solid over hollow 95% of the time (5 of 5 birds). So "solidity understanding" is an object preference.
  - Rescue version: with four objects, not twelve, 4 of 6 crows chose the narrow tube, and 3 of those switched to the wide tube when its water was higher.
- Miller et al. (2016, b07): a pre-existing bias that points at the answer. 29 of 30 insertions sinking and 29 of 30 solid before training. Set against the correct answer, crows passed 0 of 5 and 0 of 5 criteria; children 13/29 (45%) and 5/33 (15%). Trial 1 sinking: crows 24%, children 67%.
- Jacobs et al. (2015, b03): reply to Taylor et al. 2014 (crows 0/100 experimental trials, 2-year-olds learned in about 3). The reply lists unfair confounds (experience, familiarity, apparatus complexity, a visible ledge). No new data.

### 2.6 Hidden causal agents: a failed replication

Taylor, Miller, Gray (2012, a20): 8 crows; hide inspection higher when no human entered (UCA) than when one did (HCA). Wilcoxon Z = 3.171, p = 0.002. Rival: habituation. Commentaries (Boogert, Dymond 2013; a22, second-hand) pointed to fixed order HCA before UCA, sensitisation, and the human as a conditioned cue.

O'Neill et al. (2021, a21/b15, numbers re-opened): 14 crows in four groups (n = 4, 4, 3, 3). Direct replication: HCA 8.69 (SD 1.1) vs UCA 10.95 (SD 2.31) inspections per minute, t(3) = -2.16, p = .12. Reverse order: 7.52 vs 9.26, p = .42. Pooled Wilcoxon V = 7, p = .15. Because the base effect failed, the extra control groups could not be interpreted. Verdict: neither supports nor refutes hidden-agent reasoning. No third lab.

### 2.7 Primate and bird string/other controls

- Krupenye, Kano et al. (2017, b16/d01): apes in a false-belief video. Heyes proposed low-level cueing and asked for an inanimate control (a green semi-circle for the actor). 43 apes; 22 of 43 (51.2%) looked at a box vs 22 of 30 (73.3%) in the original; first looks to target 14 of 22 (p = 0.28). More than half made no look: low power. Heyes's reply was not read (d02).
- Bastos et al. (2021, b12): kea fail the loose-string task. 7 kea, 20 trials each: first touch correct 10, 11, 12, 9, 7, 7, 11 of 20. Switches in 41 of 140 trials. Fail even after feedback experience (d23).
- Smirnova et al. (2025, d24): 6 hooded crows, loose string, independent lab. None solved the first two tasks spontaneously. 105-243 trials to learn to pull both ends.
- Baciadonna et al. (2022, d25): 4 jays, mirror string. All learned direct view; none used the reflection. The authors cannot tell if the concept or the setup was the limit.
- Miller et al. (2020, b17): tool over-use in children, orangutans; crows and children could not refrain from non-functional tools. Abstract only.
- Bastos and Taylor (2020, b13): review of Macphail's null hypothesis. Birds show species differences and behaviour not explained by associative learning alone. No numbers.

### 2.8 The LLM transfer: from crows to counterfactual tasks

From 2022 the same logic was used on LLMs.

- Razeghi et al. (2022): GPT-J accuracy on arithmetic depends on how often the numbers occur in pretraining. Gap above 70 points between top 10% and bottom 10% frequent terms (c22/d21).
- Lampinen et al. (2022): content effects on logic tasks (c18).
- Shi et al. (2023): GSM-IC, one irrelevant sentence (d07).
- Wu et al. (2023/2024): counterfactual tasks (a25, b19).
- Ullman (2023), Shapira et al. (2023): ToM perturbations.
- McCoy et al. (2023): probability of task, output, input.
- Lewis and Mitchell (2024): permuted-alphabet analogies; answered by Webb et al. (2024).
- Mirzadeh et al. (2024/2025): GSM-Symbolic and GSM-NoOp.
- Zhang et al. (2024): GSM1k, a fresh matched set.
- Ivanova (2023/2024): "Toward best research practices in AI psychology" (c16, c28). 14 rules. Key: consider alternative strategies, add controls that omit the question, do not rely on famous items, test many varied items. Passing 20 varied logic tasks is stronger than one.
- Crosby et al. (2019, c27): Animal-AI Environment. Controlled tasks and hidden test sets copied from animal testing.

---

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested. "Ids" refer to evidence ids; claim ids K.. refer to claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A chain of transfers, each removing one rival, beats a single pass | 3 of 6 crows solved the tube, mean 103.3 trials (SE 20.3); 3 of 3 passed transfers 1 and 2 | Taylor 2009 (a01, a02, b01); K01 | E |
| Decisive control is a different-surface task with the same logic | 3 of 3 solvers right on table trial 1; 3 of 3 tube-failures failed; 8 naive crows none above chance; 10 of 12 first trials correct (not independent) | Taylor 2009 (a04, b02); K02 | S (one lab, N = 3) |
| Failing a transfer narrows the account | Transfer 3: 3 of 3 failed the bare-hole task; they used the hole, not the base | a03; K04 | E |
| One trap-task pass does not predict another | Apes r = 0.13, p = 0.57, n = 20; rooks 6 of 7 failed far transfers; crows 3 of 3 failed transfer 3 | a07, a09, a03; K03 | E |
| Pre-existing bias aligned with the answer inflates the pass | Crows 29/30 sinking, 29/30 solid before training; 0 of 5 passed when bias set against function; children 13/29 | Miller 2016 (b07); Logan 2014 (a18); K05 | E |
| LLM output-probability bias | GPT-4 cipher decoding 51% (likely output) vs 13% (unlikely); rot-13 GPT-3.5 0.21 vs 0.00 other shifts | McCoy 2023 (a29, c12); K05, K16 | E |
| Frequency of numbers in pretraining | Gap above 70 points absolute, GPT-J-6B, top vs bottom 10% | Razeghi 2022 (c22, d21); K16 | E (old models) |
| Causal vs arbitrary-link twin | Stone 88% vs 46% in matched search (p = 0.013); water vs sand 58% vs 56% group, 76.3% in another study | Taylor 2011 (a13); Jelbert 2014 (a16); K06 | C |
| Hidden-agent effect | Original n = 8, p = 0.002; replication n = 14 across four groups, direct n = 4 p = .12; pooled p = .15 | a20, a21; K07 | C |
| String pulling needs the feedback loop (partly) | Pull-step 96.5% to 55.7%; kea first touch 7-12 of 20 (chance); 4 of 11 crows pass hidden-stage redesign | a10, b04, b12, a23; K08 | C |
| Small n limits controls | Wilcoxon n = 4 floor p = 0.0625 | a10, a21; K09 | E |
| Counterfactual tasks lower LLM accuracy | 11 tasks, 4 models; parseable programs 99% default vs 62%, 71%, 75% (parse rate, not accuracy) | Wu 2024 (a25, b19, c08); K10 | S |
| Permuted alphabets break letter-string analogies | Synthetic alphabet GPT-3 below 0.1 on four of six problem types; humans 0.753 (1,876 samples) vs GPT 0.35-0.49 | Lewis and Mitchell; Hodel and West (a30, b21, c11, d13); K11 | E |
| Tool step can remove the gap | GPT-4 + code vs humans P = 0.496 (N = 99, 97); plain GPT-4 P = 8.9e-13 | Webb 2024 (d12); K28 | C |
| Logic-preserving ToM edits break answers | Original 99%; transparent bag 95% still "chocolate"; corrected second prompt popcorn 58% vs chocolate 36%; GPT-4 97% original, 0% on transparent access and "inon" | Ullman 2023; Shapira 2023 (a27, c02, c06); K12 | E |
| ToM for newer models | Kosinski: GPT-4 75% (40 tasks, 8 scenarios each); 2026 open models none fully robust; Llama-3-70B and DBRX limited | c05, d10, d11; K13 | C |
| Irrelevant clause (NoOp) drops | -17.5 (o1-preview), -29.1 (o1-mini), -32.0 (GPT-4o), -40.0 (GPT-4o-mini), about -60 for small models; "up to 65%" is the weak end | Mirzadeh 2025 (a26, c24); K14 | C |
| Distractor audit | 117 of 945 (12.4%) clauses truly irrelevant, kappa 0.32; audited drops 0-2 points for GPT-4o, Opus 4.6, Haiku 4.5 | LessWrong 2026 (d19); K32 | C (blog, unreviewed) |
| Distractor dose-response | Grok-3-Beta 43% to 19% (1 to 15 distractors); GPT-4.1 26% to 2% | Yang 2025 (d16); K31 | E |
| Cheap input hygiene | "Ignore irrelevant information": micro 72.4 to 77.8, macro 6.0 to 15.0; 20-sample self-consistency 88.1 and 30.0 (20x tokens) | Shi 2023 (d07); K30 | S |
| Single variant vs all variants | GSM-IC micro 72.4% vs macro 6.0%; ToM per-turn 58-74% vs all-scenes 0-4.4% | d08, d09; K29 | E |
| Name/number swaps no longer separate on a current model | Haiku 4.5: CoT 97.9 vs 96.6; PAL 97.2 vs 95.5; SBSC 96.4 vs 95.0 (drops 1.3, 1.7, 1.4) | Kutakh 2026 (d18); K37 | S |
| Matching: perturbed set must match difficulty | Larger numbers in variants (K-S 0.12); 8 of 20 open models significant | Dlugosz 2026 (d17); K36 | S |
| Contamination check by fresh set | GSM1k 1,205 items; drops up to 8%; r2 = 0.36; humans picked the new item 21.83% vs 20% chance | Zhang 2024 (b25, c25, d20); K15, K35 | E |
| Order effect | GPT-4 story analogies 89% (16/18) correct-first vs 61% (11/18) correct-second | Lewis and Mitchell 2024b (d14); K38 | S |
| Rule audit on ARC-style tasks | o3 text 77.1%; about 27% of correct outputs rest on unintended or wrong rules; Claude about 19%; humans about 7% | Beger 2026 (d22); K34 | S |
| ConceptARC minimal tasks as comprehension check | Humans 0.95; GPT-4 text 0.69; 12 of 482 humans excluded | Mitchell 2023 (c14, c15); K21 | E |
| Stated reasoning omits the cause | Up to 36% accuracy drop under biasing features across 13 BBH tasks; hint named 25% (Claude 3.7) and 39% (R1) | Turpin 2023; Chen 2025 (b27, d03); K17 | C |
| Paired-input check is cleaner | R1 0.37%, Sonnet 3.7 thinking 0.04% of 4,834 pairs; production non-thinking up to 13.49% | Arcuschin 2026 (d04); K33 | C |
| Self-correction gains came from oracle labels | GPT-3.5 GSM8K 75.9 to 95.5 with oracle; CommonSenseQA 75.8 to 38.1 without | Huang 2024 (c26); K18 | S |
| Content effects on logic | Better when meaning supports logic, in LMs and humans | Lampinen 2022 (c18); K19 | S |
| Consistency across question types | FANToM six question types; 25 controls and 5,000 items (Gandhi) | b28, c21, b29, c20; K20 | E |
| Hidden shortcuts in data | Horse tag in about 1/5 horse images; WSC lost validity | b18, c17, c28; K22 | E |
| Task load can mimic missing ability | 4 objects not 12: 4 of 6 crows pass; GSM-DC dose-response | a19, d16, d12; K24, K31 | C / E |
| First-trial success is not diagnostic alone | Tiga wrong on T2 trial 1 then right 19 times; right on T3 trial 1, then chance | a05; K27 | S |

---

## 4. Mechanisms and models

This section turns the animal controls into procedures an engineer can implement. Each is a code-level recipe, not a prompt.

### 4.1 Rival-explanation table (per problem class)

For each problem class, code stores a list of rival explanations. Each row has:

- **name**: "fitted to examples", "surface cue X", "answer prior", "memorised default", "irrelevant-clause sensitivity", "order effect".
- **prediction**: what the agent's answers would do if the rival were true (Taylor 2010 template: resurgence predicts re-probing; conditioning predicts the behaviour dies out).
- **control**: the variant that breaks the rival while keeping the rule (a11, a12, a24).
- **validity check**: the "wrong" answer in the control must have a real cost, otherwise passing proves nothing (Silva 2005 lesson, a08).

### 4.2 The ladder (triangulation)

Ordered variants V0 (given examples), V1 ... Vk:

1. V1: strip one cue (colour, label, name). Keep rule.
2. V2: strip a second cue.
3. V3: change surface form entirely (different notation, domain words, grid vs text). The trap-table analogue.
4. V4: a structured near-miss that the cue-follower and the rule-user answer differently (the two-hole transfer 3: it failed, and showed which feature was the cue).
5. A naive baseline: run the same variant without the training signal (8 naive crows, 0 of 8). For an agent: a plain model, or a model given only the surface.

Pass = all rungs pass, scored per problem (macro), not per variant (micro) (K29: 72.4% vs 6.0%). Record the first-attempt result and the block result separately (Tiga case, K27).

### 4.3 Cue ablation after a failure

When a rung fails, code ablates one feature at a time to find which one the answer depended on (Taylor 2009 transfer 3: hole, not base). The result becomes the S9 lesson line: "relied on feature F". K04.

### 4.4 Counter-prior items

Make items where the correct answer is the unlikely one (Miller 2016: bias set against function; McCoy 2023: unlikely output). Report prior-aligned and prior-opposed accuracy separately. The gap is the reliance on the prior (K05, K16). Include familiarity strata: round vs odd numbers, common vs rare strings (Razeghi; K16).

### 4.5 Counterfactual twin plus comprehension check (CCC)

From Wu et al. and Lewis and Mitchell:

1. Make a twin item that changes a constant or rule (base 9 instead of base 10, a permuted alphabet) with the same procedure.
2. Ask a comprehension question about the new rule alone (successor of this letter in the new alphabet).
3. If the comprehension check passes and the task fails, the gap is not misunderstanding of the setup (GPT-3.5, GPT-4 mostly 0.9-1.0 on successor and predecessor).
4. Report the gap: default minus counterfactual. A scaffold helps only if the gap shrinks, not if both rise (K10, K28).

### 4.6 Rescue version (load control)

If a perturbed item fails, rerun it with distractors cut or length halved (Logan 2014: 4 objects, not 12; Yang 2025 dose-response). If it passes, log "load-related failure". If it fails, treat as real. This replaces Ullman's one-failure rule with a two-step rule (K24, K31). Neither the rescue test nor a threshold for LLMs has been measured in the papers.

### 4.7 Distractor injection with audit

Code inserts a related but unused quantity or sentence (GSM-NoOp, "cats sleep most of their lives" trigger: R1 error 1.5% to 4.5%). Before the item enters the held-out set, a second model or a person confirms the clause cannot change the answer. In the audit study only 12.4% of model-written clauses passed, kappa 0.32 (K32). Log the share rejected.

### 4.8 Matching the perturbed set

Compare number magnitude, token length and step count of original and perturbed items; bootstrap over problem templates (Dlugosz 2026: larger numbers account for half the significant drops). K36.

### 4.9 Order-swap and paired-input checks

- Forced-choice items: run both answer orders; count only order-stable answers (GPT-4 89% vs 61%; K38).
- Decision steps: swapped-question check ("is X bigger than Y" and "is Y bigger than X") (Arcuschin; K33). Hint insertion alone is a weak G10 test.

### 4.10 Contamination probes

- Fresh matched set, with a distinguishability audit (humans 21.83% vs chance 20%).
- Likelihood of generating old items (r2 = 0.36 with the gap).
- Per-model perturbation gap.
- Verbatim completion of benchmark items.

Razeghi-style term counts need pretraining data; not usable on frontier models. K35.

### 4.11 Hidden test set discipline

The held-out set is never visible to prompt tuning. Log every time it is consulted (Animal-AI; K26). Fresh problems for any element-keeping decision, order counterbalanced (O'Neill 2021; K07).

### 4.12 Rule audit

Have the agent state its rule; compare the rule with the true rule. Beger 2026: accuracy alone overstates rule use (27% unintended or wrong rules for o3 vs 7% for humans). K34.

---

## 5. What holds up

### 5.1 Replications and failures

| Result | Outcome |
|---|---|
| Taylor 2009 trap-table | Same-lab extensions (b02) support. Independent confirmation exists for trap tasks mainly through contrast: apes (Martin-Ordas 2008) and rooks (Seed, Tebbich) show no far transfer. No independent lab repeated the crow design with the same transfers. |
| Hidden causal agents (Taylor 2012) | **Failed to replicate** (O'Neill 2021). Commentaries had flagged order and cue confounds in advance. Low power in both. |
| String pulling as insight | Contested. Feedback-loop account supported by Taylor 2010/2012 and kea (Bastos 2021). Hidden-stage redesign let 4 of 11 pass (Gruber 2019). Independent crow (Moscow 2025) and jay (Cambridge 2022) data show slow learning and cannot separate accounts. |
| Aesop water displacement | Logan 2014 re-tested and found colour cue (U-tube) and object bias (solid vs hollow). Several results shrank. Miller 2016: 0 of 5 pass when bias set against function. |
| Submentalizing (apes) | Inanimate control run (43 apes, p = 0.28), low power; Heyes's reply not read. |
| Letter-string analogies | Replicated as fragile by two groups (Lewis and Mitchell; Hodel and West). Webb et al. 2024 argue the gap is counting load; GPT-4 + code matched humans. Contested interpretation, agreed data. |
| ToM perturbations | Ullman's first flip was a whitespace artefact, corrected. Failure on transparent-access holds in Shapira's GPT-4 (0%). No run on 2025 reasoning models. |
| GSM-Symbolic | Direction holds. Magnitude contested: 8 of 20 open models show significant drops; number size confound; audited distractors 0-2 point drops on 2026 models; Haiku 4.5 name/number swaps 1.3-1.7 points. |
| GSM1k contamination | Replicated by design as a fresh matched set; frontier families show little overfit. |

### 5.2 What the controls taught

Things that worked as controls:

- Remove one cue, keep the logic (trap-table, uncovered U-tube).
- Set the prior against the answer (Miller 2016, McCoy 2023).
- Matched arbitrary-link twin (stone dropping vs search; K06 mixed).
- Signature error the rival predicts (heavy-block dropping).
- Paired condition with the mechanism switched off (fan off: 47.9% vs 72.9% on).
- Naive baseline (0 of 8 naive crows).
- Remove the feedback input (vision restricted).
- Comprehension check (CCC).
- Order-swapped pairs.

Things that did not work or were invalid:

- Inverted-trap control: humans also avoid it for free (Silva 2005).
- Fixed-order designs (Jelbert 2014; Taylor 2012).
- n = 3 or 4 birds: minimum p = 0.0625 at n = 4.
- A distractor set not audited (12.4% pass).
- A perturbation set not matched on difficulty.
- Whitespace-sensitive prompts (Ullman's artefact).

### 5.3 Moderators

- Task load: fewer objects rescued the narrow tube choice in crows; more distractors lower LLM accuracy steadily.
- Tool access: code removed a counting load in letter-string analogies.
- Model generation: name/number swaps no longer hurt Haiku 4.5; distractor drops fall to near zero when only truly irrelevant clauses are kept.
- Verbalisation budget: hint-verbalisation rises with token budgets in small open models.
- Priors: pre-existing biases can be aligned with or against the answer.

### 5.4 Interventions on LLMs

| Intervention | Effect | Status |
|---|---|---|
| "Feel free to ignore irrelevant information" | micro +5.4, macro +9.0 (old model); about zero tokens | S |
| Self-consistency, 20 samples | micro 88.1, macro 30.0 (20x tokens) | S |
| Code execution (letter-string) | Gap removed (P = 0.496) | C |
| Iterative or single-shot code (Haiku 4.5) | No shrink of an already tiny gap | S |
| CoT on ToM perturbations | Helps on average (67.2% to 89.6% unperturbed), hurts in some classes | S |
| More in-context examples | Did not close the default-counterfactual gap (Wu, section 5.5); 8 shots of similar NoOp did not fix it | S |
| Zero-shot CoT | Mostly helps, sometimes hurts | S |
| Outcome RL | Raised hint verbalisation 63% relative on MMLU then plateaued near 28% | S |
| Reasoning fine-tuning | Amplified a wording shortcut ("X thinks") in 2026 open models | S |
| Training with strong distractors and PRM beam search | Up to +6.29% OOD robustness | S |

---

## 6. Language models

### 6.1 What the papers show

Models score well on defaults and lose accuracy when the surface or the world rules change. Three types of change are measured.

**World rules changed (counterfactual).** Wu et al. 11 tasks, GPT-4, GPT-3.5, Claude, PaLM-2: counterfactual below default, above chance, correlated with default; base-10 arithmetic degrades more slowly with digits than other bases (memorisation signal); gaps sometimes "from near-perfect to near-zero". 0-shot CoT does not close the gap and sometimes hurts (PaLM-2 base-10 and base-16 addition; GPT-4 and GPT-3.5 chord playing). The 99% to 62/71/75% figure is a parse rate in a drawing task, not accuracy.

**Surface changed, logic kept.** Ullman: GPT-3.5 P(chocolate) 99% original, 95% transparent bag, 98% cannot read, 97% trusted testimony, 87% late label. Shapira: GPT-4 97% on original false belief, "other person" 93.8% (davinci-002) to 68.8%, "inon" 71.4% to 0%, transparent access 66.7% to 0%. Later GPT models can do worse on perturbed categories than older ones.

**Irrelevant content added.**
- GSM-IC (code-davinci-002): micro 72.4%, macro 6.0%.
- GSM-NoOp: drops from -17.5 points (o1-preview, 92.7 to 77.4) to -40 (GPT-4o-mini, 91.7 to 54.1), Llama3-8b 74.6 to 18.6.
- Triggers: R1 error 1.5% to 4.5%; across 1,000 GSM8K problems error up to 5.14x (reasoning models) and 7.21x (Mistral-Small-24B); o1 gave answers more than 1.5x budget in 26.4% of cases.
- Dose response (Yang 2025): Grok-3-Beta 43% to 19%, GPT-4.1 26% to 2%.

### 6.2 What changed it

- **Model generation.** Name/number swaps: GPT-4o 94.9 vs 95.0 (no change); Haiku 4.5 1.3-1.7 points. Audited distractors: 0-2 points for GPT-4o, Opus 4.6, Haiku 4.5 (blog, unreviewed). So the simple perturbations of 2024 are less diagnostic now (K37). Changed-rule counterfactuals and unaudited distractors still bite.
- **Tools.** Code removed a counting load (GPT-4 + code P = 0.496 vs humans).
- **Chain of thought.** Mixed: helps ToM overall; hurts some perturbation classes; did not fix Wu's gaps.
- **Prompt wording.** One ignore-sentence gave +5.4 micro on an old model. A whitespace change flipped one Ullman result.
- **Reasoning training.** Reasoning fine-tuning amplified a wording shortcut in 2026 open models (d11).
- **Distractor quality.** Only 12.4% of model-written NoOp clauses were truly irrelevant, so part of the reported drop was bad distractors.

### 6.3 ARC-style rule use

Beger 2026 on ConceptARC: o3 text pass@1 77.1% (medium), 68.3% (low); with Python 75.6% and 67.9%. About 27% of o3's correct outputs (and Gemini's) used a correct-unintended or incorrect rule; Claude about 19%; humans about 7% (19% of human rules unclear). Images: o3 29.2% output accuracy but 40.0% correct-intended rules. ConceptARC: humans 91%, Kaggle top program 52%, GPT-4 25%; minimal tasks humans 0.95 vs GPT-4 text 0.69.

### 6.4 Reasoning faithfulness

Turpin 2023 (GPT-3.5, Claude 1.0): up to 36% drop across 13 BBH tasks under biasing features; chain of thought never mentioned it. "Always A" cost GPT-3.5 18.7 points, Claude 1.0 4.7. CoT only weakly reduced sensitivity for GPT-3.5 (55.2 to 58.7%) but a lot for Claude 1.0 (63.2 to 80.1%). Chen 2025: hint named 25% (Claude 3.7 Sonnet), 39% (R1); misaligned hints 20% and 29%; harder GPQA lowers it. Arcuschin 2026: paired questions R1 0.37%, Sonnet 3.7 thinking 0.04%. Zaman 2026: omission is not necessarily unfaithfulness.

### 6.5 Self-correction

Huang 2024: with oracle labels GPT-3.5 GSM8K 75.9 to 95.5; without, CommonSenseQA 75.8 to 38.1 after round 1; GPT-4 GSM8K 95.5 to 91.5 to 89.0 over rounds; GPT-3.5 keeps its first answer 74.7% of the time, and more changes go from correct to wrong than the reverse.

### 6.6 What is missing

- No study measured a scaffold (reflection, multi-sample, code-selected verification) against the default-minus-counterfactual gap at equal tokens.
- No 2025-2026 run of the Ullman or Shapira sets on reasoning models. 2026 ToM papers used open models up to Llama-3-70B and DBRX (none fully robust).
- No false-accept curve for single-variant versus multi-variant held-out checks.
- No head-to-head of colour permutation, input mutation and symmetry checks on ARC false passes.
- No test of restate-and-strip against the NoOp drop.
- Most LLM data are 2023-era (GPT-3, 3.5, 4, PaLM-2, Claude 1).

---

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. **Held-out checks come as a ladder, not one variant.** Each rung removes one cue; the last rung changes the surface form completely. Accept only if all rungs pass; score per problem (macro). Schema part: G3, S4, S8. Status [E]. Evidence: a01, a02, a04, a06, b01, c01, c16 (K01); d08, d09 (K29, gap between one-variant and all-variant pass: 72.4% vs 6.0%; 58-74% vs 0-4.4%).
2. **Never accept a pass on one phrasing.** Require two or more structurally matched variants that look different. Schema part: G3, S8. Status [E]. Evidence: a07, a09, a03 (K03); b28, c21, b29, c20 (K20).
3. **Record which cue a failed check relied on.** Ablate one feature at a time; write the feature as the S9 lesson. Schema part: G3, S9, memory lessons. Status [E]. Evidence: a03, a18, b07, b08 (K04).
4. **Counter-prior and familiarity strata in the held-out set.** Report prior-aligned and prior-opposed accuracy separately. Schema part: G3, S1. Status [E]. Evidence: b07, a18, a29, c12, c22, d21 (K05, K16).
5. **Size the control set so p can reach the threshold.** At least 30 held-out items per class; report intervals. A Wilcoxon at n = 4 cannot go below 0.0625. Schema part: G7. Status [E]. Evidence: a10, b05, a21 (K09). (The 30-item number is our proposal; no source gives it.)
6. **Write the shortcut list per problem class and attach one control per shortcut.** Include a baseline that omits the question or masks the key field. Schema part: S0 gate table, G3. Status [E]. Evidence: c16, c28, b18, c17 (K22, K23).
7. **Include trivial comprehension items in each held-out set.** If the agent fails them, its failure on harder items is a comprehension problem. Schema part: S1, G3. Status [E]. Evidence: c15, a30, b20, c11 (K21).
8. **Keep a fresh, never-published problem set for G7 comparisons** and check model familiarity. Schema part: G3, G7. Status [E]. Evidence: b25, c25, d20 (K15, K35).
9. **Do not use name or number swaps as the main held-out variant on current models.** Use changed-rule twins and audited distractors. Schema part: G3. Status [S] on current models but the 2024 drops are [E]; filed as single source for the current-model claim (K37). Evidence: d18, d19.

### Test first

Each of these is a candidate; see UNKNOWNS.md for the test design.

10. **Counterfactual twin with comprehension check; track the gap, not the level.** Schema part: G3, S8. Status [S]. Evidence: a25, b19, c08, c09, d12 (K10, K28). Unknown whether scaffolds shrink the gap.
11. **Restate-and-strip in S1 against distractor clauses.** Schema part: S1. Status [S]. Evidence: d07 (K30), a26 (K14), d19 (K32). No test of restate-and-strip exists.
12. **Rescue version for failed variants** (cut distractors or length by half) to label failures load-related or real. Schema part: G3, S9. Status [C]. Evidence: a19, d16, d12 (K24, K31).
13. **Order-swapped pairs for every forced-choice item.** Schema part: G3, S1. Status [S]. Evidence: d14, d13 (K38).
14. **Rule-statement audit and a discriminating test for ARC-style items.** Which control removes the most false passes per token. Schema part: S7, S8. Status [S]. Evidence: d22 (K34).
15. **Paired swapped-question consistency check for G10 decision steps**, not hint insertion alone. Schema part: G10. Status [C]. Evidence: d03, d04, d05, b27 (K17, K33).
16. **Hide intermediate feedback in the held-out check** for code tasks (the feedback-loop control). Schema part: G3, G10. Status [C]. Evidence: a10, b05, b04, b12, d24, d25 (K08).
17. **Pair each rule task with an arbitrary-mapping twin of equal surface complexity.** Schema part: G3. Status [C]. Evidence: a13, a14, a16 (K06).
18. **Order-counterbalanced replication of any scaffold gain on a fresh sample before keeping the element.** Schema part: G7, section 8. Status [C]. Evidence: a20, a21 (K07).
19. **Audit distractors and match the perturbed set on difficulty.** Schema part: G3. Status [S]. Evidence: d19, d17 (K32, K36).
20. **Hold-out hygiene: hidden test set, log consultations.** Schema part: G3, G7. Status [S]. Evidence: c27 (K26).
21. **Block of items, not first attempt only.** Record first attempt and block. Schema part: G3. Status [S]. Evidence: a05 (K27).
22. **Self-correction without code-located failing output as a control arm for S5.** Schema part: G2, S5. Status [S]. Evidence: c26 (K18).

---

## 8. Concrete tests on our bench

All arms at equal tokens (total tokens per item, setup cost included, G7). Items: our bench item types (ARC-style grids, BRAINTEASER word puzzles, small math or logic items with code check). Report bootstrap intervals over problem templates.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style grid items with a given-examples check | (a) fit-to-examples check only; (b) +colour permutation; (c) +input mutation; (d) +symmetry flip; (e) +rule audit | False-pass rate (pass on check, wrong on hidden answer) and tokens per false pass removed | Each control removes some false passes; expect the cheapest code-run control to win. Prior from o3: about 27% of correct outputs rest on bad rules, so false passes are not rare. No source gives control sizes. |
| T2 | Same items, ladder depth | 1 variant, 2, 3, 4 variants at equal total tokens | False-accept rate vs number of variants | Rate falls with variants then flattens. The knee tells us how many variants (no source has a curve). |
| T3 | Math items with a changed constant or rule (counterfactual twin) + comprehension probe | plain; CoT; multi-sample vote; code-selected verification | Default minus counterfactual accuracy gap | A scaffold that is "doing more than recall" shrinks the gap. Wu: gaps persist with CoT and examples; code helped on counting load (Webb). |
| T4 | Word problems with a distractor clause (audited) | baseline; ignore-sentence; restate-and-strip | Accuracy drop vs clean item; tokens | Prior: a few points, not a fix (ignore-sentence gave +5.4 micro, +9 macro on an old model). On 2026 models drops may be near zero on audited clauses. |
| T5 | Failed variants (from T3/T4) | rerun as-is vs rescue version (distractors or length cut by half) | Share of failures that pass on rescue | If high, failures were load not missing rule. Informs whether Ullman's one-failure rule or the load reading fits our agent. |
| T6 | Forced-choice items | single order vs both orders (count only order-stable) | Accuracy; share of answers that flip | Old GPT-4 story analogies differed by 28 points by answer order (89% vs 61%); size on our model unknown. |
| T7 | Items with counter-prior vs prior-aligned answers | plain vs scaffold | Accuracy gap aligned minus opposed | A scaffold that reasons shrinks the gap; one that only recalls keeps it. |
| T8 | S5 revision items | revise with code-located failing output vs revise with no signal | Right-to-wrong and wrong-to-right flips | Gains only with the real signal (Huang: 75.9 to 95.5 with oracle; falls without). Confirms G2. |
| T9 | Decision steps that cite reasons | swapped-question pairs; hint insertion at k samples | Inconsistent-pair rate | Rates should be low on reasoning models (0.04% to 0.37% in sources); a higher rate on our scaffold flags a G10 problem. |
| T10 | Fresh vs published benchmark class | 30 fresh matched items vs old | Pass-rate gap, distinguishability audit | Gap near zero for frontier families (GSM1k). A gap means contamination. |
| T11 | Code tasks | intermediate output shown vs hidden in the held-out check | Pass rate on hidden-feedback variant | If scaffold gain survives hiding, it is not feedback-loop dependent. Sources are animal; transfer unknown. |
| T12 | Rule tasks vs arbitrary-mapping twins | scaffold on both | Gain on rule task minus gain on twin | A gain on both is not rule use. |

---

## 9. What does not transfer, and why

- **Sample sizes and statistics.** Animal studies used 3-14 birds because birds are costly. We can run thousands of items. Our problem is the reverse: choose the number of variants, not subjects. The animal "minimum p = 0.0625" lesson transfers only as a warning.
- **Naivety.** A naive crow has no training on the task. A language model has seen much of the internet. A fresh problem for a crow is not fresh for a model, and the contamination controls (GSM1k, likelihood) have no animal analogue.
- **Individual-bird logic.** Per-bird passes (Obo, Tiga, Slevin) are a replication unit. An LLM's samples are not independent (G4). The "individual" analogue is a fresh problem or template.
- **Perceptual distance and Shepard's law.** The argument that more perceptual distance means less generalisation does not hold for a text model: a surface that looks different to us can look the same in embedding space, and the reverse.
- **Motivation and food reward.** Birds stop when they lose interest. Models do not tire. Failure to pull the string in 20 trials is not the same as a failure to compute.
- **Feedback loop as a rival.** The perceptual-motor loop (food moves closer) is specific to embodied tools. For an agent the analogue (tool output visible after each step) is a design choice, not a hidden mechanism. We can switch it off in code.
- **Ullman's skeptical default.** Fine for a claim about general ability. For our agent we do not make a general claim; we want a pass rate per class. One failure is a data point, to be sized.
- **Interpreting the hidden-agent result.** Animal behaviour needs interpretation by inspection counts. LLM outputs are text we can compare directly.
- **Animal-only effects.** Species differences (rooks, kea, apes), tool-use habits and developmental comparisons with children have no use for the agent.
- **Old-model LLM findings.** Most numbers are from GPT-3 to GPT-4 and Claude 1. Some are already weaker on 2026 models (name and number swaps; audited distractors). Do not quote them as current.

---

## 10. Open questions

1. Does a scaffold shrink the default-minus-counterfactual gap at equal tokens, or only raise both? No source measures this (K10, K28, K37).
2. Do 2025-2026 reasoning models still fail the Ullman and Shapira perturbations and the permuted-alphabet analogies, and by how much?
3. How many held-out variants separate rule use from fitting? No false-accept curve exists; any number must come from our tasks.
4. Does restate-and-strip reduce the NoOp drop, and at what token cost?
5. Which control gives the biggest cut in ARC false passes: colour permutation, input mutation, or symmetry?
6. Does a failed LLM control pass when load is cut (rescue test)? The analogue is shown by dose-response; the same-item rescue was not run.
7. Is the Razeghi frequency effect present in frontier models? Needs pretraining counts.
8. Do Turpin-style results hold for long-reasoning models with large budgets? Partly: omission persists (25%, 39%), but swapped-question inconsistency is tiny.
9. Who settles the string-pulling debate? Independent labs (Moscow, Cambridge) say they cannot separate the accounts. Not needed for our agent, but it shows how long a contested control can stay open.
10. What did Heyes say in reply to the inanimate control (d02 not read), and did the exchange end with a design that resolved it?
11. Is the water-vs-sand difference (58% vs 56% group; 76.3% in another design) real? Different designs, not a direct contradiction.
12. Is a held-out check itself fitted to over time? If we reuse the same held-out set, the agent's prompts may be tuned to it. How fast does it decay?

---

## 11. Sources

[V] = opened and read this session (by the finder agents, numbers partly re-opened in the critique). [M] = snippet or second-hand only.

### Animal studies

- [V] Taylor, Hunt, Medina, Gray (2009) Do New Caledonian crows solve physical problems through causal reasoning? Proc R Soc B. https://pmc.ncbi.nlm.nih.gov/articles/PMC2674354/ (a01-a06, b01, c01)
- [V] Taylor, Roberts, Hunt, Gray (2009) Causal reasoning in New Caledonian crows: ruling out spatial analogies and sampling error. https://pmc.ncbi.nlm.nih.gov/articles/PMC2734031/ (b02)
- [V] Jacobs, von Bayern, Martin-Ordas, Rat-Fischer, Osvath (2015) Corvids create novel causal interventions after all. https://pmc.ncbi.nlm.nih.gov/articles/PMC4426607/ (b03)
- [V] Taylor, Knaebe, Gray (2012) An end to insight? https://pmc.ncbi.nlm.nih.gov/articles/PMC3497243/ (b04)
- [V] Taylor, Medina, Holzhaider, Hearne, Hunt, Gray (2010) An investigation into the cognition behind spontaneous string pulling. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0009345 and https://pmc.ncbi.nlm.nih.gov/articles/PMC2825261/ (a10, b05)
- [V] Taylor, Elliffe, Hunt, Gray (2010) Complex cognition and behavioural innovation in New Caledonian crows. https://pmc.ncbi.nlm.nih.gov/articles/PMC2982037/ (a11, a12)
- [V] Taylor, Elliffe, Hunt, Emery, Clayton, Gray (2011) New Caledonian crows learn the functional properties of novel tool types. https://pmc.ncbi.nlm.nih.gov/articles/PMC3237408/ (a13-a15)
- [V] Taylor, Miller, Gray (2012) New Caledonian crows reason about hidden causal agents (with reply). https://pmc.ncbi.nlm.nih.gov/articles/PMC3479607/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC3562812 (a20, b14)
- [V] O'Neill et al. (2021) New Caledonian crows and hidden causal agents revisited. Animal Behavior and Cognition 8(2). https://www.animalbehaviorandcognition.org/uploads/journals/33/AB_C_2021_Vol8(2)_ONeill_et_al.pdf (a21, b15)
- [M] Boogert et al. (2013); Dymond et al. (2013) commentaries on Taylor 2012, as described in O'Neill 2021 (a22). Same URL as O'Neill.
- [V] Jelbert, Taylor, Cheke, Clayton, Gray (2014) Using the Aesop's fable paradigm. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0092895 (a16)
- [V] Logan, Jelbert, Breen, Gray, Taylor (2014) Modifications to the Aesop's fable paradigm. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0103049 and https://pmc.ncbi.nlm.nih.gov/articles/PMC4108369 (a17-a19, b06)
- [V] Miller, Jelbert, Taylor, Cheke, Gray, Loissel, Clayton (2016) Performance in object-choice Aesop's Fable tasks. https://pmc.ncbi.nlm.nih.gov/articles/PMC5148090 (b07)
- [V] Neilands, Jelbert, Breen, Schiestl, Taylor (2016) How insightful is "insight"? https://pmc.ncbi.nlm.nih.gov/articles/PMC5156351 (b08)
- [V] Jelbert et al. (2019) New Caledonian crows infer the weight of objects. https://pmc.ncbi.nlm.nih.gov/articles/PMC6367178 (b09)
- [V] Gruber et al. (2019) New Caledonian crows use mental representations to solve metatool problems. https://pmc.ncbi.nlm.nih.gov/articles/PMC6384166/ (a23, b10)
- [V] Boeckle et al. (2020) New Caledonian crows plan for specific future tool use. https://pmc.ncbi.nlm.nih.gov/articles/PMC7735258 (b11)
- [V, abstract only] Miller et al. (2020) Decision-making flexibility in New Caledonian crows, young children and adult humans. https://pmc.ncbi.nlm.nih.gov/articles/PMC7065838 (b17)
- [V] Bastos et al. (2021) Kea fail a loose-string connectivity task. https://pmc.ncbi.nlm.nih.gov/articles/PMC8322428 and https://research-portal.st-andrews.ac.uk/en/publications/kea-nestor-notabilis-fail-a-loose-string-connectivity-task/ (b12, d23; the second page is abstract only)
- [V] Bastos and Taylor (2020) Macphail's null hypothesis. https://pmc.ncbi.nlm.nih.gov/articles/PMC7360938 (b13)
- [V] Martin-Ordas, Call, Colmenares (2008) Tubes, tables and traps. https://pmc.ncbi.nlm.nih.gov/articles/PMC2757606/ (a07)
- [M] Visalberghi and Limongelli (1994); Povinelli (2000); Silva et al. (2005), via Martin-Ordas 2008 (a08). https://pmc.ncbi.nlm.nih.gov/articles/PMC2757606/
- [M] Seed, Tebbich, Emery, Clayton (2006); Tebbich et al. (2007), via Martin-Ordas 2008 (a09). Same URL.
- [V] Kano et al. (2017) A test of the submentalizing hypothesis (inanimate control). https://pmc.ncbi.nlm.nih.gov/articles/PMC5595417 (b16); Krupenye, Kano, Hirata, Call, Tomasello (2017). https://research-repository.st-andrews.ac.uk/handle/10023/11631 (d01)
- [M] Kano et al. (2017) Submentalizing cannot explain belief-based action anticipation, TiCS. https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/277925/1/j.tics.2017.06.011.pdf (d02; snippets only)
- [V] Smirnova, Cheplakova, Kubenko (2025) Some hooded crows understand how a loose string works. https://pmc.ncbi.nlm.nih.gov/articles/PMC12050315 (d24)
- [V] Baciadonna, Cornero, Clayton, Emery (2022) Mirror-mediated string-pulling in Eurasian jays. https://pmc.ncbi.nlm.nih.gov/articles/PMC9107426 (d25)
- [V] Heyes (2012) Simple minds: a qualified defence of associative learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC3427553/ (a24)

### AI and LLM studies

- [V] Wu et al. (2024) Reasoning or reciting? https://arxiv.org/abs/2307.02477 (a25, b19, c08, c09)
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning. https://arxiv.org/abs/2402.08955 (a30, b20, c10, d13)
- [V] Lewis and Mitchell (2024) Evaluating the robustness of analogical reasoning. https://arxiv.org/abs/2411.14215 (d14)
- [V] Hodel and West (2024) Response: Emergent analogical reasoning in large language models. https://arxiv.org/abs/2308.16118 (b21, c11)
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks supports emergent analogical reasoning. https://arxiv.org/abs/2404.13070 (d12)
- [V] Ullman (2023) Large language models fail on trivial alterations to theory-of-mind tasks. https://arxiv.org/abs/2302.08399 (a27, b22, c02-c04)
- [V] Shapira et al. (2023) Clever Hans or neural theory of mind? https://arxiv.org/abs/2305.14763 (a28, b23, c06, c07)
- [V] Kosinski (2023/2024) Evaluating large language models in theory of mind tasks. https://arxiv.org/abs/2302.02083 (c05)
- [V] Kim et al. (2023) FANToM. https://arxiv.org/abs/2310.15421 (b28, c21; per-model numbers abstract-level)
- [V] Gandhi, Franken, Gerstenberg, Goodman (2023) Understanding social reasoning with language models. https://arxiv.org/abs/2306.15448 (b29, c20)
- [V] Nickel, Schrewe, Flek (2024) Probing the robustness of theory of mind. https://arxiv.org/abs/2410.06271 (d09)
- [V] Nickel, Schrewe, Mai, Flek (2026) Understanding artificial theory of mind: perturbed tasks and reasoning. https://arxiv.org/abs/2602.22072 (d10)
- [V] Kouwenhoven, van der Meer, van Duijn (2026) Traces of social competence in LLMs. https://arxiv.org/abs/2603.04161 (d11)
- [V] Mirzadeh et al. (2025) GSM-Symbolic. https://arxiv.org/abs/2410.05229 (a26, b24, c23, c24)
- [V] Shi et al. (2023) Large language models can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 (d07, d08)
- [V] Zhang et al. (2024) A careful examination of LLM performance on grade school arithmetic (GSM1k). https://arxiv.org/abs/2405.00332 (b25, c25, d20)
- [V] Dlugosz, Oliveira, Diaz-Rodriguez (2026) The importance of being statistically earnest. https://arxiv.org/abs/2605.28700 (d17, preprint)
- [V] Kutakh (2026) Reasoning, code, or both? https://arxiv.org/abs/2605.26414 (d18, preprint)
- [V, page-summary tool] LessWrong post (2026) Revisiting GSM-Symbolic. https://www.lesswrong.com/posts/Ze4C99Dasj74YKCFh/revisiting-gsm-symbolic-do-2026-frontier-models-still-fail (d19, unreviewed blog)
- [V] Rajeev et al. (2025) Cats confuse reasoning LLM. https://arxiv.org/abs/2503.01781 (d15)
- [V] Yang et al. (2025) How is LLM reasoning distracted by irrelevant context? https://arxiv.org/abs/2505.18761 (d16)
- [V] McCoy et al. (2024) Embers of autoregression. https://arxiv.org/abs/2309.13638 (a29, b26, c12, c13)
- [V] Razeghi et al. (2022) Impact of pretraining term frequencies on few-shot reasoning. https://arxiv.org/abs/2202.07206 (c22, d21)
- [V] Lampinen et al. (2024) Language models show human-like content effects on reasoning tasks. https://arxiv.org/abs/2207.07051 (c18)
- [V] Turpin et al. (2023) Language models don't always say what they think. https://arxiv.org/abs/2305.04388 (b27, c19, d06)
- [V, page-summary tool] Chen et al. (2025) Reasoning models don't always say what they think. https://arxiv.org/abs/2505.05410 (d03)
- [V] Arcuschin et al. (2026) Chain-of-thought reasoning in the wild is not always faithful. https://arxiv.org/abs/2503.08679 (d04)
- [V] Zaman and Srivastava (2026) Is chain-of-thought really not explainability? https://arxiv.org/abs/2512.23032 (d05)
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c26)
- [V] Mitchell, Palmarini, Moskvichev (2023) Comparing humans, GPT-4, and GPT-4V on abstraction and reasoning tasks. https://arxiv.org/abs/2311.09247 (c14, c15)
- [V] Beger et al. (2026) Distinguishing performance from competence in reasoning models (ConceptARC). https://arxiv.org/abs/2510.02125 (d22)
- [V] Ivanova (2024) Toward best research practices in AI psychology. https://arxiv.org/abs/2312.01276 (c16, c17, c28)
- [V] Lapuschkin et al. (2019) Unmasking Clever Hans predictors. https://pmc.ncbi.nlm.nih.gov/articles/PMC6411769 (b18)
- [V] Crosby et al. (2019) The Animal-AI Environment. https://arxiv.org/abs/1909.07483 (c27)

Not a source: b30 is an agent-written synthesis (opened: false) with no new data. The duplicates (a21/b15; a10/b05; a11 and b01/c01; a25/b19/c08/c09; a26/b24/c23/c24; a27/b22/c02/c03; a29/b26/c12/c13) count as one source each.
