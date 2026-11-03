# Self-explanation: deep document

*Subfield A05.07. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K27), critique.md in this folder. Evidence ids (a01, b09, c14, d05 ...) point to those files. Status tags: [E] established, [S] single-source, [C] contested. Numbers marked "second-hand" were not read in the primary text.*

## 1. What it is

Self-explanation means a learner explains to themselves why a step in a worked example or a text sentence follows. They do not just read it. They say what rule justifies it, what goal it serves, and how it links to what they already know.

Two things are called "self-explanation effect" and they must be kept apart.

1. **Spontaneous self-explanation.** Some learners explain without being asked. Chi et al. (1989) found they learn more than learners who do not. This is a correlation (a01, a02).
2. **Induced self-explanation.** An instructor or tutor prompts the explanation. Chi et al. (1994) and a meta-analysis of 64 reports (Bisra 2018) test this. This is the causal claim (a03, a10).

Why it matters for our agent. The schema state S5 (REVISE) says: show the failing output, the model writes one line naming what is wrong, then fixes it. That one line is a self-explanation. This document asks three questions.

- Does the line itself help, or does any extra processing do the same?
- What must the line contain?
- What must surround it (a check, feedback, a model strong enough to write it) for the line to help?

Short answer from the evidence: the human effect is real but medium (g about .55) and shrinks when time is matched. The LLM evidence is mixed and mostly from 2022-2023 models. No study tests the human mechanism (explain each step of a worked example) on an LLM at equal tokens (K21, c26). That is our experiment.

## 2. History and theories in depth

### 2.1 Founding study: Chi, Bassok, Lewis, Reimann, Glaser (1989)

- Eight college students read the prose of a physics (mechanics) chapter. They then talked aloud while studying three worked examples. Then they solved problems.
- After the fact, the 4 best solvers (Good) and the 4 weakest (Poor) were compared.
- Good solvers had produced far more self-explanations: about 15.3 vs 2.8 per example (as Chi 1994 reports) or 15.5 vs 2.7 (as VanLehn 1992 reports). Posttest: 82% vs 46% correct. All second-hand (a01). The two secondary sources disagree slightly and the scanned original was unreadable.
- Monitoring differed. Good solvers had 53% positive and 46% negative monitoring statements. Poor solvers said they understood 85% of the time, even when later work showed they did not (a02).
- Example look-ups differed. Good: 2.7 look-ups per problem, 1.6 lines each. Poor: 6.7 look-ups, 13.0 lines each (they reread from the top). Both groups used examples on most problems, about 75% vs 83% (a02).
- Limits. N=8. Groups were split by outcome after the fact. Prior knowledge and ability are confounded with explaining. Status [C] (K01).

### 2.2 Replications of the observational pattern (a08)

VanLehn, Jones and Chi (1992) summarise three protocol studies.

- Chi 1989, physics.
- Pirolli and Bielaczyc (1989), LISP: Good solvers spent 45% of episodes on deep processing vs 18% for Poor. Poor spent 19% on superficial study vs 10%.
- Fergusson-Hessler and de Jong (1990), mass spectrometer: "everything is clear" appeared three times more often in Poor protocols.
- Impasses (Chi, VanLehn and Reiner 1988): one Poor solver had 30 impasses in 77 episodes (39%). One Good solver had 7 in 31 (23%). In 6 of the Good solver's 7 impasses a correct piece of knowledge was learned.

So Good solvers differ in four ways: more explanations, more accurate monitoring, fewer look-ups, more targeted look-ups. The poor-monitoring result is the most robust piece [E] (K07).

### 2.3 First controlled test: Chi, de Leeuw, Chiu, LaVancher (1994)

- 24 eighth graders read a circulatory-system text. 14 were prompted to explain after every line. 10 read the text twice (a03).
- Pre-to-post gain 32% vs 22%, group x test interaction F(1,22)=5.1, p<.05. On hard inference questions +22.6% vs +12.5%, t(22)=2.64, p<.01. No main effect of group.
- Time on task was not equal: prompted mean 2h05 (range 1h27 to 2h53), control 1h06 (range 22 min to 2h47). Time confound.
- Inside the prompted group, top 4 vs bottom 4 explainers: 87 vs 29 explanation inferences (t(6)=5.64, p<.001); correct ones 61 vs 14. Gain 38% vs 27% (p<.07). Hard-question gain 33% vs 17% (p<.05). Open-book look-ups 2 vs 11 of 54 questions (a04). A dose-response, but correlational.
- Mental models (a05). Prompted: 8 of 14 (57%) reached the correct "double loop-2" model. Unprompted: 2 of 9 (22%). High explainers 4 of 4, low explainers 1 of 4.
- Content of explanations (a06). At least 30% integrated the text with prior knowledge. About 25% of explanations were wrong, in both the physics data and this study. Results held when wrong ones were partialed out. Ability did not matter: the 5 highest and 5 lowest CAT scorers both gained about 30%.
- Status of K02: [S]. The primary PDF is paywalled; numbers come from an earlier opened read and were not re-checked (critique item 9).

### 2.4 Theories

**Chi's three characteristics (a07).** Self-explaining works because it is (1) constructive (the learner produces something beyond the text), (2) integrative (it uses prior knowledge), and (3) piecemeal (small local explanations, so conflicts with the evolving mental model get noticed and repaired). Summarising, diagram drawing and writing a complete theory-based explanation each lack one. VanLehn 1992 found only 50-60% of the rules needed for the physics problems were in the text, so the rest had to be constructed.

**Gap-filling and repair.** Explanations expose gaps (the missing premise) and conflicts (the model of the system disagrees with the text). The learner then repairs. Wrong explanations are tolerated because correct later text contradicts them (a06). Caveat: the text in Chi 1994 was always correct, so contradiction was guaranteed. With no real source, wrong explanations may never be repaired.

**Coverage vs generation (b27).** Two rival accounts. Coverage: explaining only adds missing information, so a given instructional explanation should do as well. Generation: the learner's own links to prior knowledge are what matter. Bisra found self-explanation beat instructional explanation by g=.35 (k=6), so generation counts for something, but coverage may account for about half.

**Cascade (VanLehn, Jones, Chi 1992) (a09).** A rule-based simulation. Explaining gives two kinds of knowledge: domain rules (learned when an impasse is resolved with an overly general rule that is then specialised) and derivational knowledge (stored derivations that later guide search by analogy). Details are in section 4.

**Anticipative reasoning (Renkl 1997, a28).** Successful learners predicted the next step or explained goal structure and used principles. Fixed learning time; N=36; numbers not obtained. Bisra's one anticipatory study gave g=1.37 (k=1).

**Structure-mapping model (Lee, MacLellan, Weitekamp 2026, a25).** Self-explanation as abduction: which operation turned the earlier expression into the changed one? Naive search is combinatorially explosive. Mapping parts of the old expression onto the new result and searching near those anchors first returned the intended procedure before any other equal-valued computation in 104 of 120 subproblems (86.7%) vs a median of 32 (26.7%) for 100 random-order unguided runs. 93.8% fewer value-operation combinations tested. Symbolic model, no human or LLM data.

**Time-on-task / extra processing account.** The effect may be partly more time and more processing per item. Evidence in section 5.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Good solvers produce more self-explanations (spontaneous) | N=8 (4 vs 4); posttest 82% vs 46%; about 15 vs 3 explanations per example | Chi et al. 1989 (second-hand; a01, K01) | [C] correlational, tiny N |
| Poor solvers over-claim understanding | Poor said "understood" 85% of the time; Good 53% positive / 46% negative; "everything is clear" 3x more in Poor protocols | Chi 1989 via VanLehn 1992; Fergusson-Hessler and de Jong (a02, a08, K07) | [E] |
| Good solvers look up examples less and more precisely | Good 2.7 look-ups, 1.6 lines each; Poor 6.7, 13.0 lines | Chi 1989 via VanLehn 1992 (a02) | [S] |
| Prompted explaining beats re-reading (small experiment) | Gain 32% vs 22% (N=14 vs 10); hard items +22.6% vs +12.5%; study time 2h05 vs 1h06 | Chi et al. 1994 (a03, K02) | [S], time confound |
| Explanation count tracks learning inside the prompted group | Top 4 vs bottom 4: 87 vs 29 inferences; gain 38% vs 27% (p<.07); hard items 33% vs 17% | Chi 1994 (a04) | [S] correlational |
| Correct mental model reached more often | 8/14 (57%) prompted vs 2/9 (22%); high explainers 4/4 vs low 1/4 | Chi 1994 (a05) | [S] |
| About a quarter of explanations are wrong, no harm | 25% wrong; effect unchanged when partialed out | Chi 1994 (a06, K08) | [S] |
| Cascade simulation reproduces the effect | Explain+analogy: 23/23 problems solved, 23 rules; no explaining: 9 solved, 3 rules, 6 wrong, 8 timed out; explain without analogy: 19 solved, 18 rules, 4 incorrect | VanLehn, Jones, Chi 1992 (a09) | [S] model, sufficiency only |
| Overall induced effect | g=.552 (CI .454-.650), 69 effect sizes, 64 reports, N=5,917, Q=196.63, I2=65.4% | Bisra et al. 2018 (a10, b01, K03) | [S] one meta-analysis |
| Effect depends on comparison | No extra explanation g=.673 (k=41); mixed .462 (k=15); instructional explanation .354 (k=6); other strategy .304 (k=7); QB=11.65, p=.009 | Bisra 2018 (a11, b02, K04) | [S] |
| Task type | Study text .787 (k=14); solve problems .476 (k=20); study worked examples .362 (k=8, CI .109-.615); simulation .241 ns (k=2); QB=10.15, p=.119 ns | Bisra 2018 (a12) | [S] |
| Prompt content | Conceptual .873 (k=13) vs metacognitive .192 ns (k=3); multiple choice .242 ns (k=2); interrogative .559, imperative .395, fill-in .895 (k=2) | Bisra 2018 (a13, b03, b04, K06) | [S] |
| Prompt timing | Concurrent .521 (k=57); retrospective .571 (k=8); beginning 1.241 (k=4) | Bisra 2018 (b03) | [S] |
| Outcome type | Problem solving .445 (k=14); transfer .534 (k=17); inference 1.794 (k=2); essay .624 ns (k=3) | Bisra 2018 (b05) | [S] |
| Age | Elementary .483; high school .426; undergraduate .611 | Bisra 2018 (b06) | [S] |
| Region | East Asia 1.191 (k=6) vs North America .525 (k=42), Europe .481 (k=18); QB=13.14, p=.011 | Bisra 2018 (a14, K19) | [S] probably artefact |
| Time on task | More-time studies .72 vs similar-time .41, difference ns; fail-safe N 6,028; Orwin 274 | Bisra 2018 (b07) | [S] |
| Treatment fidelity | Checked .613 (k=31) vs unchecked .409 (k=21), QB=4.74, p=.19 ns | Bisra 2018 (b08) | [S] |
| Fiorella and Mayer review | 44 of 54 tests favoured explaining; median d=0.61 | Lawson and Mayer 2021 intro (b14) | [S] second-hand |
| Writing an explanation helps on delayed test, not immediate | Exp 2 delayed: write 8.06 (SD 4.02) vs no activity 5.41 (SD 3.78), p=.018; read-an-explanation 4.47 ns; write 3x longer | Lawson and Mayer 2021 (b13) | [S] time confound |
| Time-matched: modest benefit over extra practice | N=69, grades 2-4, modest benefit on some subscales only | McEldoon et al. 2013 (b09, d01) | [C] abstract only |
| After good conceptual instruction, prompts add nothing | Exp 2 n=48 no effect | Matthews and Rittle-Johnson 2009 (d02) | [C] abstract only |
| Prompts plus on-demand explanation worse than prompts alone | No figures | Schworm and Renkl 2006 via Bisra (b12, a14) | [S] second-hand |
| Self-explanation prompts add nothing over extra practice (grade 3) | N=238, interleaving helped; prompts no added benefit; quality still predicted outcomes | Scheitz et al. 2025 (a16) | [C] abstract only |
| Classroom trial null | 58 classrooms, no overall effect on foundational algebra knowledge or preparation for future learning | McGinn, Booth, Huyghe 2025 (a17) | [C] abstract only |
| Explanation quality mediates worked-example effect for low-aptitude learners | N=115, moderated mediation by prior knowledge and working memory, not fluid intelligence | Bichler et al. 2026 (a15, K09) | [S] abstract only |
| Novices can lose | 27 students: example-based 54.63 vs self-explanation 48.15 median at day 10 (p=.047); gone at day 40 | Yip et al. 2026 (a18) | [S] tiny |
| Hypothesis generation beat self-explanation | N=88: accuracy .22 vs .17, p=.03, partial eta2=.06 | Mahzari group 2018 (b25, K20) | [C] |
| Feedback after explaining helps near, not far transfer | N=94: 90.73 / 89.92 vs 82.03 control, p<.05; far transfer no difference | Canadian medical school study 2019 (b26) | [S] |
| LLM feedback on written explanations | N=92; transfer explanation +11.9 (SE 5.8, p=.030, d=.44, CI 1.2-22.6); menu +4.7 ns; plain post-test no difference (menu -2.4, open +0.8 ns); problems done 58.9 / 43.8 / 16.9 | Chen et al. 2026 (a19, b16, c01-c03, K10) | [S] |
| LLM grading of explanations | GPT-5.1 vs human consensus kappa .78, vs single graders .66-.68, humans .70 (160 explanations); tutor correctness kappa .32, F1 .91, 42 false negatives vs 16 false positives | Chen 2026 (c04); Lekshmi-Narayanan 2026 (a20, b18, K11) | [E] moderate reliability |
| Balanced-set LLM judge | F1 0.98 vs similarity baselines 0.69-0.72 on 1,435+1,435 examples | Lekshmi-Narayanan et al. 2026 (a21) | [S] ceiling |
| Self-explanation helps human oversight of LLMs | N=400; error detection +10.6 points, odds 3.9x; second study N=240, cue OR 1.17 | Fu, Ramasubbu, Galletta 2026 (a26) | [S] preprint |
| Fluent AI answers inflate confidence | Phase 2 N=85; standard assistant highest perceived, lowest actual learning | Eleftheriou et al. 2026 (a27) | [S] abstract only |
| LLM: explain each utterance | MultiWOZ JGA 35.93 vanilla, 27.64 CoT, 39.19 plan-and-solve, 44.44 self-explain (GPT-4 50.97); STARv2 51.88 / 51.85 / 63.66 | Gao et al. 2023 (a22, b20, c11, K12) | [E] for dialogue only |
| LLM: wording | MultiWOZ: understand 36.52, summarize 40.98, explain each utterance 44.44 | Gao 2023 (b21, K18) | [S] |
| LLM: own rationales as exemplars | MedMCQA / MedQA / StrategyQA: self-explain 56.6 / 59.6 / 59.7; human CoT 53.2 / 57.5 / 58.5; wrong-answer explanations 56.0 / 59.4 / 59.1 | Zhao et al. 2024 (a23, c06, c07, K14) | [S] |
| LLM: explanations in context | Large models gain; smaller do not; matched control explanations do not help | Lampinen et al. 2022 (b22, c09) | [E] |
| LLM: explanations unreliable | text-davinci-002 72.0 to 86.9 explain-first; other models small gains; factuality check SYNTH 52.4% to 74.8% | Ye and Durrett 2022 (b23, c10) | [S] |
| LLM self-debug with explanation | Spider: Codex 81.3 / 81.3 / 84.1; GPT-4 73.2 / 73.4 / 73.6; TransCoder unit tests 91.6, +explanation 92.5, +trace 87.9 | Chen et al. 2023 (c14, c15, K16) | [E] small |
| LLM reflection in memory | HotPotQA self-reflection about +8 over episodic memory; Rust: reflection w/o tests 0.52, tests only 0.60, both 0.68 | Shinn et al. 2023 (c12, c13) | [E] |
| Intrinsic self-correction hurts | GPT-3.5 CSQA 75.8 to 41.8; GSM8K 75.9 to 74.7; GPT-4 GSM8K 95.5 to 89.0; oracle GPT-3.5 GSM8K 84.3 | Huang et al. 2024 (c17, K15) | [E] |
| Invalid reasoning keeps most CoT gain | GSM8K standard 15.4, CoT 48.5, invalid 39.5 (81%), no relevance 11.0 | Wang et al. 2023 (d03, K23) | [S] |
| Models find mistakes poorly, fix well when told | GPT-4 52.87 mistake-finding; backtracking gains plateau at about 65% finder accuracy | Tyen et al. 2024 (d13, d14, K24) | [S] |
| Specific feedback beats generic | Code optimisation 27.5 / 26.0 / 24.8; math gain 0 because model said "looks good" 94% | Madaan et al. 2023 (d15, d16) | [S] |
| Step-level checking beats outcome checking | PRM 78.2 vs ORM 72.4 vs majority 69.6 (best-of-1860, MATH) | Lightman et al. 2023 (d10, K26) | [E] |
| CoT gains concentrate in symbolic tasks | Symbolic 14.2, math 12.3, logic 6.9, others about 0.7 | Sprague et al. 2025 (d08, d09) | [E] |
| Fixed compute: best method depends on difficulty | About 4x efficiency by allocation; sequential revision better on easy, search on hard | Snell et al. 2024 (d05, d06, K22) | [S] |
| Self-preference in judges | Bias rises linearly with self-recognition; GPT-4 judge over 80% agreement with humans but position, verbosity and self bias | Panickssery 2024; Zheng 2023 (d11, d12, K25) | [S] |
| Training use | ExP-GRPO level-5 MATH pass@4 23% vs 12% (GRPO + expert CoT); STaR CSQA 68.8 to 72.5 | Zhou 2025 (a24); Zelikman 2022 (b24, c16, K17) | [E] but training only |

## 4. Mechanisms and models

Each mechanism below is stated so that an engineer can build it as a scaffold step.

### 4.1 Cascade-style "derive each step" loop (VanLehn, Jones, Chi 1992)

Inputs: a worked example (list of lines), the model's current rule set, a rule library.

1. For each example line, try to derive it from the previous lines using the current rules (explain it).
2. If derivation succeeds, record the derivation (which rule, which earlier lines). Store it.
3. If derivation fails, this is an impasse. Try an overly general rule (for example "any quantity along the direction can be summed") to make the line derivable.
4. If the general rule works, specialise it (add the conditions the example satisfies). Store the new rule.
5. At problem time, use stored derivations to steer search by analogy (retrieve the example whose derivation matches the current subgoal).

Simulation results (a09): with steps 1-5, 23 of 23 problems solved. Without explaining (only read lines), 9 solved, 6 wrong, 8 timed out. With explaining but no analogical search control, 19 solved and 4 of 18 learned rules were incorrect. So the explanation produces knowledge, and the stored derivation makes it usable.

Agent analogue: a "worked example" is a past solved item in memory. The agent does not edit weights, so the "rule" is a stored lesson line and the "derivation" is a stored subgoal sequence. This is close to the subgoal library already in the schema.

### 4.2 Impasse-driven learning

Learning happens at impasses, and the quality of what is learned depends on how the impasse is resolved (a08: Good solver learned a correct piece in 6 of 7 impasses; Poor solver had more impasses and learned wrong things). Implementation: log an impasse whenever a step cannot be justified. Only at an impasse write the explanation line. Do not explain steps that pass a check. Bisra's note (b28) supports triggering explanation where confidence is low, not on every step.

### 4.3 Anticipate, then compare (Renkl 1997; a28)

1. Hide the next step of a worked example.
2. Model predicts it.
3. Code compares to the real step.
4. A mismatch is a gap flag; the model writes one line naming the gap.

This is explanation with an external check built in. Bisra's single anticipatory study had g=1.37 (k=1), so treat as [S].

### 4.4 Structure-mapping search (Lee et al. 2026; a25)

To explain a step "A became B":

1. Find parts of A that appear in B (anchors).
2. Search operations that produce the changed parts from the anchors first.
3. Verify with code that the operation reproduces B.

86.7% of subproblems returned the intended procedure first, 93.8% fewer candidate combinations. Fit for arithmetic or grid transformations where code can verify.

### 4.5 Explain, then check, then revise (Self-Debug / Reflexion / ESSE)

- Self-Debug "rubber duck" (c14): model explains its code line by line, then uses the explanation plus execution result.
- Reflexion (c12): a first-person reflection on why the trial failed is stored in memory for the next trial.
- ESSE tutor (a20, b19): an LLM judge returns correctness and completeness; the student revises. Revision rate 63% after an "incorrect" verdict vs 35% after "correct". Revisions added concepts (concept coefficient .50 vs volume .33).

Common structure: a signal outside the explanation (test, reward, judge) triggers the explanation; the explanation guides one revision; the revision is re-checked. Without the external signal the loop fails (Huang 2024, c17).

### 4.6 Judge for explanations

LLM judges: F1 .91 but kappa .32 on skewed real data (a20); F1 0.98 on balanced data (a21); false-flag rate 27% on correct explanations (c21). Panickssery 2024: a model favours its own text. Implementation: use a different model, randomise order, give no authorship, and measure false-flag rate on a skewed labelled set before trusting it (G5).

### 4.7 Why wrong explanations may not hurt

Two readings. Human reading (Chi): later text contradicts and repairs. LLM reading (Wang 2023, Zhao 2024): explanation correctness barely matters for in-context exemplars; relevance and order do (d03: no relevance 11.0 vs CoT 48.5; invalid 39.5). Zhao: explanations built from wrong answers 56.0 vs 56.6. These are exemplar results, not self-correction results; do not mix them.

## 5. What holds up

### 5.1 Held up

- **Poor self-monitoring is real and general** (Chi 1989, Fergusson-Hessler and de Jong, Eleftheriou 2026 for AI answers, Madaan 2023 "looks good" 94%) [E].
- **A medium effect for induced explanation against no-explanation controls** (Bisra g=.67, k=41). Fail-safe N 6,028 makes pure publication bias unlikely.
- **Content matters**: conceptual prompts work (.873), metacognitive prompts do not (.192 ns). Multiple-choice prompts do not (.242 ns, k=2). Chen 2026: free text +11.9 vs menu +4.7 ns.
- **Generation before seeing the answer**: Fu 2026 (own explanation first gave +10.6 points in catching LLM errors), Schworm and Renkl (on-demand help hurts), Lawson and Mayer (reading a given explanation did nothing: 4.47 vs 5.41 control).
- **External signal plus explanation** helps LLM agents (Self-Debug, Reflexion).

### 5.2 Failed or shrank

- **Time-matched comparisons.** Bisra: more-time .72 vs similar-time .41. McEldoon 2013: modest, only some subscales. Scheitz 2025 (N=238): no added benefit. Chen 2026: equal gain with 3.5x fewer problems, but no plain post-test lift. Chi 1994 itself had a 2x time confound.
- **After good conceptual instruction**: Matthews and Rittle-Johnson 2009, n=48, no prompt effect.
- **Large classroom trial**: McGinn 2025, 58 classrooms, no overall effect; only students who did many prompts and had adequate prior knowledge benefited; higher-prior students were hurt by more worksheets.
- **Novices**: Yip 2026, example-based teaching beat self-explanation at day 10 (54.63 vs 48.15), gone at day 40.
- **Competing methods**: hypothesis generation beat explanation (.22 vs .17, N=88).
- **Feedback with the answer**: near transfer only (90.7 vs 82.0), no far transfer.
- **Comparison to an explanation supplied by an instructor**: only g=.35.

### 5.3 Moderators

- Prior knowledge and aptitude: Bichler 2026 says quality matters more for low-aptitude learners; McGinn says enough prior knowledge is needed to produce anything; Yip says novices without any knowledge lose. This is an inverted U, similar to the LLM pattern below.
- Region (East Asia 1.19) is probably an artefact of 6 text-study trials with no-explanation controls.
- Fidelity of treatment: not significant (QB=4.74, p=.19).

### 5.4 Contradictions not resolved

Chi 1989 counts (15.3 vs 15.5; 2.8 vs 2.7). Bisra's large effect vs the time-matched nulls. Chen 2026: better explanation quality but equal post-test. Right and wrong explanations perform alike for LLM exemplars (Zhao) while human theory says repair needs contradiction.

### 5.5 Interventions that worked and did not

| Worked | Did not work |
|---|---|
| Conceptual "why does this follow" prompts | Metacognitive "how am I doing" prompts |
| Free-text explanation with feedback | Menu of explanation choices |
| Explain before getting the answer or help | On-demand instructional explanation on top of prompts |
| Writing an explanation, delayed test | Reading a given explanation |
| Reflection plus test result (Reflexion both: 0.68) | Reflection without tests (0.52 vs 0.60 base) |
| Explanation plus unit tests (92.5 vs 91.6) | Line-by-line execution trace (87.9) |

## 6. Language models

### 6.1 No direct test of the Chi mechanism

Across searches and opened papers, no study gives an LLM a worked example, makes it explain each step, and measures later problem solving at equal tokens (c26, K21). Absence is not proven; search coverage was partial and API rate limits stopped the last gap search.

### 6.2 Zero-shot "explain first" prompts

- Gao 2023, gpt-3.5-turbo: explaining every dialogue utterance before the task gave MultiWOZ JGA 44.44 vs 35.93 vanilla, 27.64 CoT, 39.19 plan-and-solve. STARv2 63.66 vs 51.88 (about +12). GPT-4 reference 50.97 and 70.27. MuTual 68.97 to 71.58, MELD 59.14 to 61.71. Wording: understand 36.52, summarize 40.98, explain each utterance 44.44. CoT hurt here. Single run, no variance, comprehension not multi-step reasoning.
- Sprague 2025: CoT gains are concentrated in symbolic (14.2), math (12.3), logic (6.9) and near zero elsewhere. Self-explanation likely follows the same task profile; this is inferred, not measured.

### 6.3 Self-generated explanations as exemplars

- Zhao 2024 (GPT-3.5): self-explained exemplars 56.6 / 59.6 / 59.7 vs human CoT 53.2 / 57.5 / 58.5. The student model is usually its own best teacher; a stronger teacher was not better (c08). 94-98% of explanations passed their faithfulness filter.
- Lampinen 2022: explanations after few-shot answers helped a 280B model on 40 BIG-bench tasks; benefit about one third of adding few-shot examples and about twice that of task instructions; matched control explanations did not help; small models did not benefit.
- Ye and Durrett 2022: gains were small for most GPT-3-era models; text-davinci-002 gained a lot (72.0 to 86.9 on one dataset). Explanations often did not follow from the input. A factuality check lifted SYNTH from 52.4% to 74.8%.
- Wang 2023: in demonstrations, relevance and order matter more than validity (GSM8K 48.5 / 39.5 / 11.0).

### 6.4 Explanation as part of a revise loop

- Self-Debug (Chen 2023): Spider Codex +2.8 (81.3 to 84.1), GPT-3.5 +1.1, GPT-4 +0.4, StarCoder +0.2. Explanation matters most without unit tests. With unit tests the explanation adds +0.9 on TransCoder; a trace hurts. Authors report up to +12% with unit tests on TransCoder and MBPP, +9% on hardest Spider queries.
- Reflexion (Shinn 2023): HumanEval pass@1 91% vs 80%; +22 AlfWorld, +20 HotPotQA, +11 HumanEval. Self-reflection gave about +8 on HotPotQA over episodic memory alone. On hard Rust problems, reflection without tests lowered pass rate to 0.52 (base 0.60); with tests 0.68.
- Self-Refine (Madaan 2023): average gain about 20 points over 7 tasks, but math 0 because the model said everything was fine 94% of the time. Specific feedback beat generic (code 27.5 vs 26.0 vs 24.8).
- Huang 2024: intrinsic self-correction hurt. GPT-3.5 GSM8K 75.9 / 75.1 / 74.7; CSQA 75.8 / 38.1 / 41.8; HotpotQA 26.0 / 25.0. GPT-4 GSM8K 95.5 / 91.5 / 89.0; HotpotQA 49 / 49 / 43. Oracle: GPT-3.5 GSM8K 84.3, CSQA 89.7. GPT-3.5 kept its answer 74.7% of the time and changed right to wrong more often than wrong to right.
- Tyen 2024: LLMs are poor at locating the mistaken step (GPT-4 52.87) but fix well when told. Backtracking helps only if the finder is about 65% accurate.
- Kamoi 2024 survey: reliable self-correction needs external feedback or a task with favourable structure.

What changed the effect, in size order: an external check (null to positive, up to +12 in code); the task type (symbolic or code vs knowledge); model strength; wording and unit of explanation (+8.5 points between "understand" and "explain each utterance" on MultiWOZ); relevance and order of exemplar content.

### 6.5 Model strength: inverted U (c27, K13)

Large models benefit and small ones do not (Lampinen). Weaker or older strong-ish models gain most; the strongest gain least (Spider +2.8 Codex vs +0.4 GPT-4). This is a cross-paper synthesis on different tasks, not a controlled test. No current-generation ladder exists.

### 6.6 Faithfulness

Turpin 2023: accuracy dropped by as much as 36% on 13 BIG-Bench Hard tasks with a biased prompt, and explanations did not name the bias. Lanham 2023: reliance on the stated reasoning varies; larger models were less faithful on several tasks. So the line a model writes is not evidence of why it answered (G10).

### 6.7 Explanation quality grading

GPT-5.1 vs human consensus kappa .78 (c04). In the tutor, kappa .32 with more false negatives (42) than false positives (16) (a20). LLMs falsely flagged 27% of correct explanations and invented issues in 34% of a qualitative sample of mostly-correct ones (c21). Fine-tuned models up to 15% better than prompting on gap detection; feedback quality up to 35% better after preference tuning (c20, simulated student explanations).

### 6.8 Training uses

ExP-GRPO (a24): explain a known-correct answer, use as a positive sample; Qwen2.5-3B MATH pass@4 96/91/86/76/23 across levels 1-5 vs GRPO + expert CoT 95/89/83/65/12; base pass@128 at level 5 is 4%. STaR rationalization (b24): CSQA 68.8 to 72.5. Outside the scaffold scope.

### 6.9 Human-AI use

Fu 2026: self-explanation before reading the LLM's explanation gave +10.6 points error detection (N=400). Eleftheriou 2026: the standard assistant gave the highest perceived and lowest actual learning.

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | The S5 line must be produced after code shows the real failing output, and must name a specific step and fault. Generic "check your work" is worse. | S5, G2 | [E] | K24; d13, d15, d16; K15, c17 |
| 2 | Never accept the model's own "looks fine" as a check. Self-monitoring fails in people (85% over-claim) and models (94% "looks good"). A check must be code or an independent verifier. | G2, G3 | [E] | K07, K15; a02, d15, c17 |
| 3 | Do not use intrinsic explain-and-revise with no external signal. It lowered accuracy in every opened test. | G2 | [E] | K15; c17, d07 |
| 4 | Do not let the generator grade its own explanation. Use a different model or code, randomised order, no authorship; measure false-flag rate (27%) on skewed labelled data. | G5 | [E] (supported) | K11, K25; a20, c21, d11, d12 |
| 5 | The S5 prompt asks content ("what is wrong in this step and why does the correct step follow"), not metacognition ("how confident are you"). | S5 | [S] from meta-analysis, aligns with [E] items 1-2 | K06; b04, a13 |
| 6 | Count tokens. Any S5 gain is credited only against an equal-token control, not a bare baseline. | G7 | [E] by design | K04, K05; b07, a16 |
| 7 | Keep stored lessons in the model's own words. | memory | [S] only; keep as a style rule, no cost | K14; a23, c08 |
| 8 | Explain before showing a reference answer or hint. | S5, S8 | [S] | b12, a14, a26 |
| 9 | Do not expect lift on knowledge or open tasks; self-explanation, like CoT, is for formal multi-step items. | G12 | [E] for CoT, [C] for self-explanation | K26; d08 |

Items 1-4 duplicate G2/G3/G5 and S5 in the current schema. The new information is the size of the harm without a signal (CSQA 75.8 to 41.8) and the 94% "looks good" rate. Nothing here needs a new schema element.

### Test first

| # | Candidate | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | One-line error naming at S5 beats an equal-token extra sample or a bare revise. | S5, G7 | [S]/[C] | K02, K05, K21, K22 |
| T2 | Gate S5 by difficulty: S5 on medium items, extra samples on hard ones. | S5, G12 | [S] | K22; d05, d06 |
| T3 | Specific (step, fault) beats generic line; a wrong-but-plausible line works as well as a right one (so the content is just focus). | S5 | [S]/[C] | K14, K23; c07, d03, d16 |
| T4 | Free-text line beats a fixed menu of error types. | S5 | [S] | K10; b16, b03 |
| T5 | Anticipate-then-compare on worked examples before use. | S2/S3 memory use | [S] | a28, b04 |
| T6 | Explain each step of a stored solved example before reusing it (derivation storing, Cascade). | memory, O7 | [S] model only | a09; K01 |
| T7 | Explaining the stored lesson in own words vs verbatim copy. | memory | [S] | a23 |
| T8 | Model-strength gate: skip S5 explanation above some pass rate. | G12 | [S] | K13; c27 |
| T9 | Explanation at S4/S5 for a failing candidate compared with hypothesis generation of several alternatives. | S5, S6 | [C] | K20; b25 |
| T10 | Separate verifier flags a wrong line before the revise; flag-trigger revise vs always revise. | S5, G5 | [S] | a20, b19, d14 |

## 8. Concrete tests on our bench

All arms get the same total token budget (including setup). Equal-token control arms use extra samples or a second attempt, never an empty baseline. Report per task family, not pooled (K19).

| Test | Items | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 S5 line vs extra sample | ARC-style and code items with a check where plain pass rate is 20-70% | A: plain; B: plain + one extra sample, pick by check; C: failing-output revise with no line; D: failing-output + one-line naming then fix | Held-out pass rate (G3); tokens per solved item | D vs C: 0 to +3 points; D vs B: about 0 (K05, K22). Meta-analysis prior g=.4 will shrink |
| T2 Difficulty gate | Items binned by plain pass rate from 5 pilot draws | Uniform S5 vs uniform extra samples vs routed | Pass rate at equal tokens | Routed wins by a few points; S5 helps on medium items, loses on hard ones (Snell) |
| T3 Content of line | Same items as T1 | Specific (step + fault) / generic ("something is wrong") / wrong-but-plausible specific / none | Pass rate | Specific > generic (+1.5 as in Self-Refine code); wrong-but-plausible close to right if Zhao and Wang transfer (K14). If wrong-but-plausible is worse, error location matters (Tyen) |
| T4 Free text vs menu | Code or math repair items | Free line vs fixed menu of 6 error types vs none | Pass rate; line quality graded by separate model plus code check | Free text >= menu (Chen: +11.9 vs +4.7 ns) |
| T5 Anticipate-then-compare | Items with stored worked examples (rule-based sequences) | A: read example; B: predict next step, code compares, write line on mismatch | Held-out items solved using the example | B > A by a small margin; unknown |
| T6 Explain stored example before reuse | Memory retrieval items | Store solution only vs store solution + per-step derivation lines vs store 1-line lesson | Transfer to a near and a far variant | Derivation helps far variants if analogy search is done (Cascade); near variants equal |
| T7 Own words vs copied | Lesson-store items | Self-written vs verbatim vs externally written | Pass rate on later items | Small edge for own words (Zhao +2 to +4); likely noise |
| T8 Strength ladder | Same 100 items on 3 or more model sizes | S5 line vs revise-no-line vs none | Gain per model | Inverted U; no gain above 90% plain pass rate (Spider +0.4 for GPT-4) |
| T9 Alternatives vs explanation | Diagnosis-like items with several plausible causes | Explain the top cause vs list 3 hypotheses and test each | Accuracy | Hypothesis list wins by a few points (Mahzari .22 vs .17); still contested |
| T10 Flag-then-revise | Items with imperfect verifier | Always revise vs revise only on separate-model flag vs code flag | Pass rate; harmful flip rate (right to wrong) | Gating on flag removes most harm (Huang: right to wrong more than wrong to right); needs finder accuracy above about 65% |

Report for every test: change in right-to-wrong flips, tokens per item, false-flag rate of the grader.

## 9. What does not transfer, and why

- **Time-on-task as the cost.** In humans the issue is minutes. For the agent it is tokens. The matching control is different; a human cannot take 100 samples.
- **Spontaneous differences between learners (Chi 1989).** There is no stable "good explainer" trait in one model. Correlation between explanation count and outcome (N=8) says nothing about prompting.
- **Repair by later correct text.** Humans tolerate wrong explanations because the text they read next is correct. In an LLM loop there is no such source unless code supplies it (a06 limits). So the 25%-wrong tolerance is not safe to import.
- **Prior knowledge integration.** The main human benefit is linking text to prior knowledge (at least 30% of explanations). An LLM's "prior knowledge" is fixed and always available; the integration step may be free, so the effect may be smaller.
- **Real-time learning.** The effect is learning that persists (delayed tests, mental models). The agent does not learn in weights. Only lessons in memory persist, so the benefit must go through stored text.
- **Faithfulness.** A human's explanation is partly the process. A model's written line is a generated text that often does not reflect the cause (Turpin, Lanham). It can focus attention, but is not evidence (G10).
- **Region, age, subject moderators.** Not meaningful for a model.
- **Training results** (ExP-GRPO, STaR). Weights change; our scaffold does not.
- **Classroom outcomes** (McGinn 2025, Scheitz 2025). Uptake and motivation failures have no agent counterpart.
- **Dialogue-comprehension gains** (Gao 2023). "Explain the utterance" is comprehension of the input, not the Chi mechanism, and GPT-3.5 specific.

## 10. Open questions

1. At equal tokens, does a one-line per-step explanation beat spending the same tokens on extra samples or a second attempt, on a current-generation model? (Not directly tested anywhere; Snell and Sprague say the answer depends on difficulty and task.)
2. Is there a model strength above which explanation adds nothing? No clean ladder exists.
3. What is the useful content: error naming, error location, or any relevant text? (Wang says relevance, Tyen says location, Zhao says correctness barely matters.)
4. Does the line help the revise (S5) the same way it helps the first attempt (S3)?
5. Exact Chi 1989 and 1994 numbers and conditions from the primary texts. Wiley 403, ASU login. Open (K27).
6. Effect sizes and controls in McEldoon 2013, Matthews and Rittle-Johnson 2009, Schworm and Renkl 2006. Only abstracts read.
7. How to score explanation quality without self-grading bias, calibrated against tutor-study kappas (.32 to .78).
8. Free text vs menu outside calculus.
9. Does step-level explanation help on long multi-step tasks, or only on short transfer items? Bisra: transfer g=.53, problem solving g=.45. Lightman supports step-level checking for formal chains.
10. Does the Chi mechanism work for an LLM-as-learner (few-shot with explained worked examples)? Four searches found none.
11. Whether Cascade's derivation-storing has an LLM analogue that beats storing the answer.
12. Whether self-explanation before reading an external checker result (Fu 2026) transfers from human oversight to agent decisions.

## 11. Sources

[V] opened (full text or page read); [M] snippet or abstract only, or second-hand.

**Founding and human studies**
- [M] Chi, Bassok, Lewis, Reimann, Glaser (1989). Self-explanations. https://education.asu.edu/lcl/publications/chi-m-t-h-bassok-m-lewis-m-reimann-p-glaser-r-1989-self-explanations-how-students (scanned; read via 1994 and VanLehn 1992). Wiley: https://onlinelibrary.wiley.com/doi/pdf/10.1207/s15516709cog1302_1 (403)
- [V] Chi, de Leeuw, Chiu, LaVancher (1994). Eliciting self-explanations improves understanding. Cognitive Science 18. (opened by first agent; not re-opened in critique)
- [V] VanLehn, Jones, Chi (1992). A model of the self-explanation effect. J. Learning Sciences 2.
- [M] Renkl (1997). Learning from worked-out examples (abstract and summaries).
- [M] Schworm and Renkl (2006). https://www.sciencedirect.com/science/article/pii/S0360131505000667 (403; via Bisra)
- [V] Bisra, Liu, Nesbit, Salimi, Winne (2018). Inducing self-explanation: a meta-analysis. https://www.gwern.net/doc/psychology/spaced-repetition/2018-bisra.pdf
- [M] McEldoon, Durkin, Rittle-Johnson (2013). Is self-explanation worth the time? (abstract via Europe PMC; https://www.ebi.ac.uk/europepmc/webservices/rest/search)
- [M] Matthews and Rittle-Johnson (2009). In pursuit of knowledge (abstract via Europe PMC).
- [V] Lawson and Mayer (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC7985227/
- [M] Fiorella and Mayer (2015) via Lawson and Mayer.
- [M] Bichler et al. (2026). Worked examples, cognitive aptitudes (abstract via Europe PMC).
- [M] Scheitz et al. (2025). Interleaving subtraction strategies (abstract).
- [M] McGinn, Booth, Huyghe (2025). Preparing 4th and 5th graders (abstract).
- [V] Yip et al. (2026). Example-based or self-explanation-based teaching (ophthalmology).
- [V] Mahzari group (2018). Hypothetico-deduction vs self-explanation. https://pmc.ncbi.nlm.nih.gov/articles/PMC5889380/
- [V] Feedback after self-explanation in diagnostic reasoning (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6558772/
- [M] Scoping reviews of explanation in mathematics and statistics (arXiv 2508.14417 and companion).
- [M] Aleven and Koedinger (2002) via Chen 2026.

**Models of self-explanation**
- [V] Lee, MacLellan, Weitekamp (2026). Structure-mapping-guided self-explanation.

**LLM and AI studies**
- [V] Chen et al. (2026). Practice Less, Explain More. https://arxiv.org/abs/2604.00142 ; https://arxiv.org/pdf/2604.00142 ; https://arxiv.org/html/2604.00142v1
- [V] Lekshmi-Narayanan et al. (2026). ESSE tutor. https://arxiv.org/abs/2608.25180
- [V] Lekshmi-Narayanan, Hassany, Brusilovsky (2026). LLMs for judging code explanations.
- [M] Lekshmi-Narayanan et al. (2024). Explaining code examples. https://par.nsf.gov/biblio/10518252
- [M] Engaging LLM to explain worked examples for Java (2024). https://par.nsf.gov/biblio/10613692
- [M] Oli et al. RCT, scaffolded self-explanation tutor (2024). https://par.nsf.gov/servlets/purl/10561388
- [V] Oli, Banjade, Olney, Rus (2024). Gaps and misconceptions in code explanations. https://arxiv.org/pdf/2501.10365
- [V] Fu, Ramasubbu, Galletta (2026). Knowing is not enough.
- [V] Eleftheriou, Pallis, Constantinides (2026). Confidence without competence (abstract and framing).
- [V] Gao et al. (2023). Self-explanation prompting. https://arxiv.org/abs/2309.12940
- [V] Zhao et al. (2024). In-context teachers. https://arxiv.org/pdf/2311.06985
- [V] Lampinen et al. (2022). https://arxiv.org/abs/2204.02329
- [V] Ye and Durrett (2022). https://arxiv.org/abs/2205.03401
- [V] Wang et al. (2023). Towards understanding CoT prompting. https://arxiv.org/abs/2212.10001
- [V] Zelikman et al. (2022). STaR. https://arxiv.org/abs/2203.14465
- [V] Zhou, Li, Zhang, Leqi (2025). ExPO.  https://arxiv.org/abs/2507.02834
- [V] Shinn et al. (2023). Reflexion. https://arxiv.org/pdf/2303.11366
- [V] Chen et al. (2023). Self-Debug. https://arxiv.org/pdf/2304.05128
- [V] Huang et al. (2024). LLMs cannot self-correct reasoning yet. https://arxiv.org/pdf/2310.01798
- [V] Madaan et al. (2023). Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Tyen et al. (2024). https://arxiv.org/abs/2311.08516
- [V] Kamoi et al. (2024). https://arxiv.org/abs/2406.01297
- [V] Turpin et al. (2023). https://arxiv.org/pdf/2305.04388
- [V] Lanham et al. (2023). https://arxiv.org/pdf/2307.13702
- [V] Snell et al. (2024). https://arxiv.org/abs/2408.03314
- [V] Sprague et al. (2025). To CoT or not to CoT. https://arxiv.org/abs/2409.12183
- [V] Lightman et al. (2023). Let's verify step by step. https://arxiv.org/abs/2305.20050
- [V] Panickssery, Bowman, Feng (2024). https://arxiv.org/abs/2404.13076
- [V] Zheng et al. (2023). LLM-as-a-judge. https://arxiv.org/abs/2306.05685
- [M] ProcessBench (2024), abstract only.
