# Force dynamics: deep document

*Subfield F01.07 of cognitive linguistics. Focus: causal push and resistance patterns (Talmy). Built from evidence_a-d.jsonl (ids a01-a28, b01-b28, c01-c26, d01-d18), claims.jsonl (K01-K18) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested. Main result: the human science is real but small and mostly from one lab, and no study tests Talmy's scheme on an LLM or as a prompt scaffold (K14).*

## 1. What it is

Force dynamics is a semantic category proposed by Leonard Talmy (1981, then 1988 in Cognitive Science 12:49-100). It says that many words and grammatical forms (can, cannot, make, let, keep, despite, because of, prevent, help, refrain, urge, persuade) encode how two force-bearing entities interact.

The parts of the scheme:

- **Agonist**: the entity in focus. Its force is the one we track.
- **Antagonist**: the entity that opposes (or helps) the Agonist.
- **Intrinsic force tendency**: each entity tends toward action or toward rest.
- **Balance**: which entity is stronger.
- **Outcome**: the Agonist ends in action or in rest.

Two steady-state patterns (a01, a02):

- Agonist stronger: "X happened despite Y".
- Antagonist stronger: "X happened because of Y" (extended causation).
- Causing and letting both fall out of balance plus outcome. "The door cannot open" means the door tends to open but a stronger Antagonist holds it shut. "The door is closed" is force-dynamically neutral.

Talmy files the category with closed-class grammar (aspect, mood, evidentiality). It is a grammar-level concept, not only a word-level one.

Why it matters to an agent: it gives a small slot template for a causal claim (focal entity, opposing entity, tendency, balance, outcome) that code can check. It also gives a typed vocabulary for causal links (cause, allow or enable, prevent, help) and a way to say that absences can act as forces.

Honest status: the scheme itself has no experiments in Talmy's own text. The experiments come from Wolff and colleagues, who turned it into a quantitative "force theory" of causation. Direct LLM tests do not exist (K14).

## 2. History and theories in depth

**Talmy 1981 and 1988.** Started as a finer split of the traditional causative. The 1988 paper (read as chapter 7 on Talmy's site, d01, d02) works by examples only. It covers:

- Physical force interplay (the ball kept rolling despite the grass).
- Psychological forces: urge, persuade, relent, give in, refuse, peer pressure (d01).
- Social forces and argumentation. Words like "yes but", "granted", "after all" act as force-dynamic logic gates that push or block a conclusion, and discourse can reverse vectors (d02).
- Gaps: no data, and no operationalisation for agents or dialogue systems found (K15).

**Critique and defence (a04, via Wikipedia only).** Goddard (1998) argued that causation is defined circularly and that the diagrams need verbal captions. Deane (1996) defended the scheme. We did not open either paper.

**Siskind 2001 (a05, a06, c01, c02).** An early AI use. LEONARD recognises verbs in video by tracking changes in force-dynamic relations (support, contact, attachment) with an event logic, not by motion profile. Siskind uses "force dynamics" in a narrower sense than Talmy (support and attachment, not allowing and preventing).

**Wolff and colleagues (2003 to 2017).** The core experimental line.

- Wolff and Song 2003 (a14, abstract only): five experiments. In focal-set models CAUSE is closer to ENABLE and PREVENT than those are to each other. In the force model the three are about equally similar. Sorting and rating of causal verbs favoured the force view (read as abstract).
- Wolff 2007 (a13, abstract only): six experiments with 3-D animations whose paths come from physics-engine force vectors. Judgments depend on several forces, people compute a qualitative resultant, and the account extends to social causation.
- Wolff, Barbey and Hausknecht 2010 (d03, full text): absences cause events when a force is removed (double prevention) or a virtual force is not realised.
- Wolff and Barbey 2015 (a07-a12, b01-b06, full text): composition of causal chains.
- Wolff and Thorstad 2017 (a23): Oxford Handbook chapter, read only via citing pages.

**Rivals.**

- Mental model theory (Goldvarg and Johnson-Laird 2001; Khemlani, Barbey and Johnson-Laird 2014, a17, b10): cause means "given A, B occurs"; enable means "given A, B is possible". The authors say force theory adds forces to model theory.
- Causal model theory (Sloman, Barbey and Hotaling 2009, a18): graph links; enable adds necessity plus an alternative cause; prevent adds reduced likelihood.
- Counterfactual and probabilistic accounts, including the focal-set model (a14).
- All three agree on most compositions (a17). Wolff and Barbey 2015 found causal model theory ties force theory (K03).

**Extensions.**

- Gardenfors and Warglien (2012), Gardenfors 2020 (a19), Gardenfors, Jost and Warglien 2018 (a20), Gardenfors and Lombard 2018 (a21), Gardenfors 2021 (a22), 2025 (b25): conceptual-space version. An event needs a force vector and a result vector; resultant force is agent force plus counterforces; categories are convex regions. Conceptual, no new experiments (K08).
- Developmental: Goksun et al. 2013 and George et al. 2019 (b16, b17; abstracts and second-hand): 3 to 5 year olds manage single-force events and use a second force only when it acts in the same direction (K07).
- Perception: Ju and Kim 2024 (b19, b20, preprint): speed profile alone flips perceived push versus pull and rigid versus elastic.
- Corpus: BECauSE 2.0 (c03, c04) has a FACILITATE vs INHIBIT degree, a two-way force-like split. 5380 sentences, 1803 causal instances; connective F1 0.77; relation-type kappa about 0.7; nearly 45% of causal instances are MOTIVATION or PURPOSE.

**New in 2025-2026 on responsibility.** Cheung, Qiao, Brown and Lagnado 2026 (a24): in an instigator A to executor B to victim chain, B is judged more responsible than A. Xiang et al. 2025 (d04) compared LLMs to humans on a force-style versus effort-style model of blame.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Force-dynamic frame is a qualitative scheme; Talmy extends it to psychological and social forces and argumentation, by example | No numbers | Talmy 1988 (a01-a04, d01, d02) | [S] K01, K15 |
| Force profile predicts the verb chosen for a single causal link: CAUSE = no tendency / no concordance / end state approached; HELP = yes/yes/yes; PREVENT = yes/no/no | Exp 1a N=24: 17 of 18 modal choices matched; C/A first link cause modal but at chance, chi2(3)=3.25, p=.355 | Wolff and Barbey 2015 (a07, a09) | [S] K02 |
| Chain composition by rule (affector of link 1, end state of last link, vector sum of other forces) | Exp 3 N=40: force 30/32, causal model 30/32, mental model 26/32. Exp 4 N=24: force 23/25, causal model 23/25, mental model 14/25 (chance, p=.69) | Wolff and Barbey 2015 (a11, a12, b03-b05) | [C] K03 |
| Double prevention is ambiguous | Predicted ALLOW 62% / CAUSE 38%. Observed about 50/50 (Exps 1a/1b), ALLOW modal only 39% (Exp 3), abstract text PREVENT 65%. Description chosen 97/73/80% for P/P animations vs 3/17% for controls (Exp 1, N=30) | Wolff and Barbey 2015; Wolff et al. 2010 (a08, b02, b06, d03) | [C] K04 |
| People deny the double preventer is a cause; order effects reproduced by a counterfactual model | No figures extracted; model parameter e.g. s=.53, 95% CI [.18,.85] | Henne and O'Neill 2022, Lombrozo 2010, Thanawala and Erb 2024, Quillien et al. 2025 (d05, d18; second-hand) | [C] K04 |
| Absences are treated like presences | Omissive vs orthodox cause accepted 35% vs 37% (p=.22), N=50 per experiment; cause-before-effect 64% vs 8% (unverified); listing omissive possibilities slower: 15.68 s vs 10.24 s for "causes" (enables 16.28 vs 10.91 s); 66% spontaneously gave an omissive conclusion; 1/2/3 possibilities listed 26/35/31%. Wolff 2010 Ns 30, 75, 36, 48 | Khemlani et al. 2020 (a16, b07-b09); Wolff et al. 2010 (d03) | [E] K05 |
| Speed profile alone flips perceived force and material | Exp 1 N=77: push 80.0% vs 12.5% (accelerate vs decelerate); pull 70.3% vs 16.2%; rigid 62.5% vs 5.4%; elastic 25.0% vs 73.0%; causal vs material r=.96. Pause detection d' 2.45 vs 1.60 (N=30, d=0.80), reverses in 3b | Ju and Kim 2024 (b19, b20) | [S] preprint |
| Children use one force at a time | 3 to 5 year olds use a second force only if same direction; older children do better | Goksun 2013; George 2019 (a19, b16, b17) | [S] K07 |
| Executable force logic in video | 7 event types, 35 movies (5 each), one subject: 6 false negatives (4 on assemble, 1 move, 1 unstack), 0 false positives | Siskind 2001 (a05, c01) | [S] K09 |
| Human responsibility follows chain structure | Later agent B rated more blameworthy than A in all Study 2 conditions; intent outweighed proximity; high-intent A lowered blame for B; four studies, two preregistered | Cheung et al. 2026 (a24) | [C] K06 |
| LLM blame follows actual force, humans follow effort plus counterfactual effort | LLM Force-model fit failure r=.35 (4o-mini), .70 (4o), .71 (GPT-4); success r=.80, .58, .82; humans Ensemble r=.92 failure, .90 success; 55 scenarios | Xiang et al. 2025 (d04) | [S] K16 |
| GPT-4 alone matches human causal ratings on a norm-by-structure design | r(14)=.68 [.28,.88], p=.004 over 16 cells; other LLMs n.s.; LLM SD 1.2-1.7 vs human 1.8-2.1 | Almeida et al. 2024 (d08) | [S] |
| Encoder NLI models blind to neo-Gricean M-heuristic with causatives | DeBERTa-v3-large 0/188, RoBERTa-large 5/188, BART-large 0/188 matching gold; probe control 87.5% at layer 4; 29/30 wrong grouping | Butnaru et al. 2026 (c05-c08, d14) | [S] K10 |
| Same paper, Gemini Flash-Lite by prompt regime | 0/188 direct; 41/188 (21.8%) with chain-of-thought; 188/188 with a prompt stating the heuristic | Butnaru et al. 2026 (c06-c08) | [S] K10 |
| LLMs weak at human-like causal selection | MoCa discrete agreement GPT-4 43.1, 41.3, Claude-v1 36.1, 35.4; Kiciman: GPT-4 86.6% vs GPT-3.5 46.6% on 15 vignettes; CLadder 70.40% with CausalCoT (+8.37) | Nie 2023; Kiciman 2023; Jin 2023 (c10-c12) | [E] K11 |
| Actual causality is hard | CaLM AC: GPT-4 65.6% (68.2% with manual CoT), text-davinci-003 57.2%, GPT-3.5-Turbo 56.5%; enablement and disablement not evaluated | Chen et al. 2024 (d07) | [E] K11, K17 |
| Structured scaffolds can hurt | 5-step scaffold cut mean CLadder normal-condition accuracy of five 3.8B-14B models 62.6% to 57.2%; CausalCoT left 48.1% unparseable; placeholder variable names cost 7.6-29.6 pp | Yu and Zhou 2026 (d09) | [S] K18 |
| Caused-motion construction is hard for LLMs | 765 sentences: Mixtral-8x7b-IT 69.75, Mistral-7b-IT 68.12, GPT-4 57.07, GPT-3.5 43.20, Gemini Pro 43.43; Llama2-7b base 9.54, 13b chat 5.59 | Weissweiler et al. 2024 (c09) | [S] adjacent |
| Illusion of causality in LLMs | 1000 null-contingency items: GPT-4o-mini median 75.7, Claude-3.5-Sonnet 50.0, Gemini-1.5-Pro 45.0 (normative 0); zero ratings 0%, 4.6%, 20.5% | Carro et al. 2025 (c13) | [S] K12 |
| Vision-language models fail physical force reasoning | GRASP/IntPhys 2 up to about 54% vs human about 80%; Flip Test best 18.3% vs 25% chance; Physion humans 0.71 | c15, c18, c19, c24 | [E] K13 |
| CoT lets GPT-4o match humans on affordance reasoning | 85% accuracy, 0.8 points below humans; GPT-3.5 30% vs 80% on one item | Gjerde et al. 2025 (d13) | [S] analogy only |
| Physics engine in the loop lifts LLM physical reasoning | UTOPIA 39 sub-tasks: GPT-3 175B 24% zero-shot; Mind's Eye +27.9 points zero-shot, +46.0 few-shot; 1.3B + engine 29.8% vs 175B vanilla 29% | Liu et al. 2022 (c17) | [S] |
| No direct LLM test of Talmy force dynamics found | search logs only | c25, d14-d17 | [E] as a gap (weak: APIs rate-limited) |

## 4. Mechanisms and models

### 4.1 Force-slot record (Talmy)

Represent each causal claim as a record:

```
claim = {
  focal:      entity whose behaviour we explain   (Agonist)
  opposer:    the other force-bearing entity      (Antagonist; may be absent)
  tendency:   focal's own tendency: action | rest
  balance:    stronger | weaker  (focal vs opposer)
  outcome:    action | rest
  type:       derived (see 4.2)
}
```

Checks code can run:

- "Because of" vs "despite": if opposer is stronger and outcome follows opposer, "because of"; if focal is stronger and outcome follows focal, "despite".
- Every slot filled, or marked unknown.
- Outcome equals what the balance predicts. A mismatch means the claim is wrong or a force is missing.

### 4.2 Wolff and Barbey force model (what an engineer would implement)

Each link has three binary features, from the patient's point of view (a07, Table 3):

| Relation | Patient tendency for end state | Concordance (affector agrees with patient) | End state approached |
|---|---|---|---|
| CAUSE | No | No | Yes |
| HELP / ALLOW | Yes | Yes | Yes |
| PREVENT | Yes | No | No |

Example: "High winds caused the tree to fall": the tree has no tendency to fall, wind acts against its rest, the fall occurs.

Composition rule for a chain of links (a08):

1. The affector of the summary is the affector of link 1.
2. The end state is the end state of the last link.
3. The patient force is the vector sum of all remaining forces.
4. In transmission chains the resultant of link 1 becomes the affector of link 2.

Predicted compositions across nine chain types: C then C gives CAUSE; C then P gives PREVENT; A then C gives ALLOW (76%) or CAUSE (24%); P then P gives ALLOW (62%) or CAUSE (38%). Those percentages are model outputs. Mental model theory predicts PREVENT for P/P.

Implementation sketch: a lookup table of the nine composed relations, with an "ambiguous" flag for A/C and P/P. Do not force a single answer in ambiguous cells (K04).

### 4.3 Absence as force

Per d03: an absence is causal when a force is removed (double prevention, release) or when a virtual force (anticipated, never realised) fails. Implementation: when listing factors, add an explicit "what was expected but did not happen" entry, and give it a type (removed-prevent, missing-help).

### 4.4 Blame by counterfactual effort (K16)

LLMs fit actual force produced; humans fit effort plus counterfactual effort (d04). The fix to test: add a step "if each agent had tried harder or less, would the outcome change?" before assigning responsibility.

### 4.5 Blocker typing for arguments (K15, Talmy section 8)

Treat each objection as either a blocker (opposes the focal conclusion) or a reinforcer. Talmy's logic gaters ("yes but", "granted") map to concession moves. Not operationalised anywhere; this is our own extension.

### 4.6 Verification by state change (Siskind)

Define an action by the force-dynamic state changes it must produce (support lost, contact made, attachment formed). Check a claimed action against required changes, not appearance. Gave 0 false positives on 35 movies (K09). Transfer idea: in tool use or planning, specify the state change that must occur before accepting "step done".

### 4.7 External engine (Mind's Eye)

Giving the model physics-engine output raised accuracy by 27.9 to 46.0 points (c17). Physical force reasoning is better computed than guessed.

## 5. What holds up

**Replications.**

- No independent replication of Wolff and Barbey 2015 composition was found (d15). All composition and absence experiments come from one lab, with 20 to 75 undergraduates per experiment, 3-D car or collision animations and forced choice among verbs. Treat as single-lab.
- Absences: Khemlani et al. 2020 (mental model camp, N=50 per experiment) independently find that people accept omissive causes as readily (35% vs 37%). This is the one point two labs agree on, so K05 is [E]. Their time cost (15.68 s vs 10.24 s) is a representation cost, not rejection.
- The perceptual force effect (Ju and Kim) has its own controls: the pause-detection pattern reverses once the rubber-band percept is removed (b20).

**Failures and ties.**

- Force theory ties causal model theory in Exp 4 (23/25 each) and in Exp 3 (30/32 each). Mental model theory lags only on composition (26/32; 14/25), not on listing tasks. The data do not separate force from causal model.
- Double prevention: the theory's 62/38 split is only loosely met (about 50/50; ALLOW 39% in Exp 3; the authors admit one result differed from prediction). Others (Henne and O'Neill 2022; Lombrozo 2010) find that people deny the double preventer is a cause. Thanawala and Erb 2024 find order effects, which a counterfactual model reproduces (Quillien et al. 2025).
- First link C/A was at chance (p=.355) in Exp 1a.
- Butnaru 2026: probe results at 100% were mostly syntactic confounds (control 87.5%). The 100% metalinguistic result used item-specific traces, so it may reflect leakage of the gold rule.

**Moderators.**

- Wording and order change double-prevention answers.
- Force direction and acceleration profile change perceived causal type.
- Age: children use one force at a time.
- Agent intent outweighs proximity in chain blame; a high-intent first agent reduces blame for later ones.

**What worked as an intervention for models.**

- Stating the principle in the prompt: Gemini Flash-Lite 0 to 188/188 on the M-heuristic set (but see leakage caveat).
- Chain-of-thought: Gemini 0 to 41/188; CLadder CausalCoT +8.37 to 70.40%; GPT-4o on affordances reaches 85%.
- External physics engine: +27.9 to +46.0 points (c17).

**What did not work.**

- 5-step structured scaffold on small models: 62.6% to 57.2% mean on CLadder normal condition; 48.1% of CausalCoT answers unparseable (d09).
- Manual CoT on CaLM actual causality: 65.6% to 68.2% only.
- Encoder-only NLI models: no sensitivity.
- Probing encoders looks good only because of syntax confounds.

**Weak spots in our own record.** Talmy's own text is now read (chapter 7), but Goddard and Deane only via Wikipedia. Wolff 2003 and 2007 were abstract-only (2010 was later read in full). Snippet-only items: a13, a14, a15, a18, a23, b12-b18, b22, c25, c26.

## 6. Language models

**There is no direct test.** No 2020-2026 paper tests Talmy's scheme on an LLM or uses it as a scaffold (K14). Sang 2025 (c22) cites Talmy for a driving planner with no ablation, so it is not evidence. Absence of results is weak because OpenAlex and arXiv were rate-limited.

**Adjacent results, by task.**

1. *Pragmatic causatives.* Butnaru et al. 2026: encoder NLI models score 0/188, 5/188, 0/188 against gold; Gemini Flash-Lite 0/188 direct, 41/188 with CoT, 188/188 with the heuristic stated. Single paper, one model family for the prompt arms. It concerns the neo-Gricean M-heuristic, not force dynamics proper.
2. *Constructional meaning.* Weissweiler et al. 2024: GPT-4 57.07% on the caused-motion construction, GPT-3.5 43.20%, Mixtral 69.75%. CxMP 2026 (d12): constructional meaning is learned gradually and stays limited even in large models; per-model numbers not extracted.
3. *Causal selection and vignettes.* MoCa 43.1 (GPT-4) down to 35.4; Kiciman 86.6% vs 46.6%; CLadder 70.40% with CausalCoT; CaLM actual causality 65.6%. CoT gains vary: large on formal tasks (CaLM top pairs 90-97%), small on actual causality.
4. *Verb causal direction.* Implicit-causality bias correlates with humans in 6 older PLMs on 305 data points (Spearman p<0.001); bidirectional models are stronger (c14). In German, only the largest monolingual BLOOM (6.4B) was human-like, and none showed the explanation bias (d11).
5. *Responsibility.* LLMs follow production force, not counterfactual effort (d04). GPT-4 alone matched human causal ratings on a 16-cell design, r=.68 (d08). LLM answers are less variable than human ones.
6. *Biases.* Illusion of causality on null contingency (c13).
7. *Physics.* VLMs fail: GRASP/IntPhys 2 up to about 54% vs human 80%; Flip Test 18.3% vs 25% chance (c18, c19, c24). Physics-engine tool loops help (c17).
8. *Annotation of causal links.* Newer LLMs agree 88-91% with each other on causal links vs human inter-annotator agreement of 30-70% (b27). Agreement is not accuracy, and no cause/enable/prevent split was tested.
9. *Scaffold cost.* Structured causal scaffolds lowered accuracy on small models (d09).
10. *Enable and disable.* No LLM benchmark covers them (K17). CRAFT (d06) covers cause/enable/prevent but only with 2020-era video models (neural baselines about 40-55%, humans 76.6%).

**What changed results, by how much.** Principle prompt vs CoT (188/188 vs 41/188, one paper); CoT on CLadder +8.37; engine +27.9 to +46.0; placeholder names -7.6 to -29.6; 5-step scaffold -5.4 pp on small models (62.6 to 57.2).

**Conflict check.** Butnaru finds LLMs blind to pragmatic causative forms under default NLI; Kiciman finds GPT-4 strong on vignettes. Different tasks, not a real conflict.

## 7. What our agent should take

Evidence ids refer to the jsonl files. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Do not drop absent factors. When listing causes, name what was expected and missing (a removed blocker, a missing helper). People treat absences as causes about as readily as presences (35% vs 37%), so a model that ignores them errs where people do not. | G (note under S2 represent) | [E] K05 | a16, b07-b09, d03 |
| Treat any force-dynamic scaffold as a cost like any other: it must not lower the plain baseline; log parse failures and tokens. | G7 (already) | [E] K11 / [S] K18 | d09, c12 |
| Do not take model agreement on causal links as accuracy (88-91% model agreement is not accuracy). | G4 (already) | [E] | b27 |

Nothing else here is established enough to enter the schema as a new element. The rest needs tests (UNKNOWNS.md).

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Force-slot record (focal, opposer, tendency, balance, outcome) on causal claims in S2 | S2 / O6 change representation | [S] K02 | a07, a09, a10 |
| Cause / allow / prevent typing of links, with an "ambiguous" flag for A/C and P/P compositions | S2 and O3 | [C] K03, K04 | a08, a11, a12, d03 |
| Principle-stated prompt for a known pragmatic trap (M-heuristic) | S1 / G | [S] K10 | c06-c08 |
| Counterfactual-effort step before assigning blame | O attribution | [S] K16 | d04, d08 |
| Blocker vs reinforcer typing of objections; blocker identification at an impasse | S6 / O4 variant | [S] K15 | d01, d02 |
| Required state-change check for "step done" in tool use | S8 verify | [S] K09 | a05, c01 |
| Name absences as forces on double-prevention cases | G / S2 | [C] K04 | a08, b02, d03, d05 |
| Calibration guard for illusion of causality | G | [S] K12 | c13 |
| Physics engine for physical force questions | tool, not schema | [S] | c17 |

## 8. Concrete tests on our bench

All arms get equal total tokens (reasoning plus answer; setup counted, G7). Report accuracy, parse-failure rate and tokens per item (K18).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 50 hand-labelled causal vignettes (cause/allow/prevent), plus MoCa and CLadder rungs 2-3 subsets | (a) plain CoT; (b) force-slot tagging then answer | accuracy; parse failures | Small gain at best (0 to +5 pp); a loss would match d09 |
| T2 | 188-item M-heuristic set (Butnaru) | (a) direct; (b) CoT; (c) one-line principle; (d) long item-specific trace | match to gold | (c) near (d) if the principle is what matters; only (d) high means leakage |
| T3 | Wolff-Barbey nine chain types as text vignettes | (a) unaided; (b) lookup-table composition prompt | share matching modal human answer; use of "ambiguous" on A/C and P/P | (b) raises match on C/C, C/P; no gain on P/P |
| T4 | Double prevention and omissive cause items (Wolff 2010 style) with matched orthodox variants | (a) plain; (b) prompt to name absences as forces | error on omissive vs orthodox; verdict shift | Smaller omissive-minus-orthodox gap in (b) |
| T5 | BoxLifters-style responsibility vignettes (d04) | (a) plain; (b) counterfactual-effort step | correlation with human Ensemble model | r rises from about .35-.71 toward .9 if the step works |
| T6 | Chain-of-agents blame vignettes (Cheung) | plain vs chain-structure prompt | does the model rate B above A; intent vs proximity | tests whether LLMs show the human pattern |
| T7 | 40 arguments needing rebuttal (own set) | (a) free list of objections; (b) blocker/reinforcer typing then rebut | blind rubric score, length-normalised | modest gain; none if noise dominates |
| T8 | Planning or tool-use tasks with a hidden blocker | (a) plain obstacle list; (b) name the opposer and test if it is stronger than the goal's tendency | task success | unknown; gap 7 |
| T9 | CRAFT-style symbolic scenes (cause/enable/prevent) | plain vs typed | accuracy vs human 71.3% (causal) | fills gap K17 |

## 9. What does not transfer, and why

- **Physical vectors.** Wolff's model sums physical vectors in an engine. Text has none; the "vector sum" becomes a qualitative lookup. Animation results (17/18 modal matches) do not carry to prose.
- **Human sample results.** 20 to 75 undergraduates per experiment, one lab, forced choice among four verbs. Not a validity test for LLM output.
- **Ambiguity is not an error.** Humans split about 50/50 on double prevention. A scaffold that forces one "right" type may be wrong there.
- **Siskind's system** is hand-built, one subject, 35 movies, and uses "force dynamics" narrowly (support, contact). It shows definitions can be made executable, not that LLMs gain from them.
- **Vision and physics benchmarks** (Physion, CLEVRER, GRASP, Flip Test) measure perception, not force-dynamic language.
- **Gardenfors's conceptual spaces** are theory with no experiments; Lynn 2026 (b26) is assertion with a toy demo.
- **Sang 2025** cites Talmy loosely; not evidence.
- **Developmental data** (children use one force at a time) is not an agent test; at most it supports single-force-first decomposition (O3).
- **Voters.** Nothing here supports a "force-dynamics voter"; G4 and G9 stand.
- **Models.** Most LLM evidence uses 2023-era models (GPT-3.5, GPT-4, Claude 2). Do not assume current behaviour.

## 10. Open questions

1. Does force-slot tagging beat plain CoT at equal tokens (K14, gap 1)? No study.
2. Does the Butnaru M-heuristic result replicate with other LLMs and with a short principle prompt vs a long one?
3. Has anyone independent of Wolff replicated chain composition? How do LLMs fare on composed relations (gap 3)?
4. How do LLMs treat double prevention and omissive causes vs the human 50/50 (K04, K17)?
5. Do force-dynamic scaffolds help tool-use or planning agents with a blocker (gap 7)?
6. Does the Cheung B-over-A pattern hold for LLM blame at equal tokens (gap 8)?
7. Is the "64% vs 8%" figure for cause-before-effect right? It was not re-found in the page text.
8. Are there LLM studies on force-dynamic verbs (prevent, let, help, despite) in the ACL Anthology that arXiv and Europe PMC missed (gap 6)? CxMP per-model caused-motion accuracy was not extracted.
9. Could Talmy's psychological and social forces (urge, persuade, relent) be operationalised for dialogue agents? No operationalisation found.
10. Do the older-model results hold on current models?

## 11. Sources

[V] = opened and read. [M] = snippet or abstract only, or read only through a secondary page.

- [V] Talmy (1988) Force dynamics in language and cognition, ch. 7: https://www.acsu.buffalo.edu/~talmy/talmyweb/Volume1/chap7.pdf
- [V] Force dynamics (Wikipedia summary of Talmy, Goddard, Deane): https://en.wikipedia.org/wiki/Force_dynamics
- [V] Wolff and Barbey (2015) Causal reasoning with forces: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301188/ and https://www.frontiersin.org/articles/10.3389/fnhum.2015.00001/full
- [V] Wolff, Barbey and Hausknecht (2010) For want of a nail: https://www.cs.utexas.edu/~mhauskn/papers/Wolff_et_al_2010.pdf
- [M] Wolff (2007) Representing causation: https://doi.org/10.1037/0096-3445.136.1.82
- [M] Wolff and Song (2003) Models of causation and the semantics of causal verbs: https://doi.org/10.1016/s0010-0285(03)00036-7
- [M] Wolff and Thorstad (2017) Force dynamics (cited via): https://pmc.ncbi.nlm.nih.gov/articles/PMC13752550/
- [V] Khemlani et al. (2020) Much ado about nothing: https://pmc.ncbi.nlm.nih.gov/articles/PMC7888478/
- [V] Khemlani, Barbey and Johnson-Laird (2014) Causal reasoning with mental models: https://pmc.ncbi.nlm.nih.gov/articles/PMC4211462/ and https://www.frontiersin.org/articles/10.3389/fnhum.2014.00849/full
- [M] Sloman, Barbey and Hotaling (2009): https://doi.org/10.1111/j.1551-6709.2008.01002.x
- [M] Mayrhofer and Waldmann (2014): https://doi.org/10.1016/j.cognition.2014.05.013
- [M] Goksun et al. (2013): https://doi.org/10.1111/cdev.12035
- [M] George et al. (2019): https://doi.org/10.1016/j.jecp.2018.08.002
- [V] Ju and Kim (2024) preprint: https://osf.io/8n9vj/
- [V] Gardenfors (2020): https://pmc.ncbi.nlm.nih.gov/articles/PMC7179668/
- [V] Gardenfors, Jost and Warglien (2018): https://pmc.ncbi.nlm.nih.gov/articles/PMC6102470/
- [V] Gardenfors and Lombard (2018): https://pmc.ncbi.nlm.nih.gov/articles/PMC5816055/
- [V] Gardenfors (2021): https://pmc.ncbi.nlm.nih.gov/articles/PMC8305407/
- [V] Gardenfors (2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC11792772/
- [V] Lynn (2026): https://pmc.ncbi.nlm.nih.gov/articles/PMC13461484/
- [V] Siskind (2001) LEONARD: https://arxiv.org/abs/1106.0256
- [V] Dunietz, Levin, Carbonell (2017) BECauSE 2.0: https://aclanthology.org/W17-0812.pdf
- [V] Butnaru, Creanga, Dinu (2026): https://arxiv.org/abs/2609.37497
- [V] Weissweiler, Koksal, Schutze (2024): https://arxiv.org/abs/2403.06965
- [V] Nie et al. (2023) MoCa: https://arxiv.org/abs/2310.19677
- [V] Kiciman et al. (2023): https://arxiv.org/abs/2305.00050
- [V] Jin et al. (2023) CLadder: https://arxiv.org/abs/2312.04350
- [V] Carro et al. (2025): https://arxiv.org/abs/2510.13985
- [V] Kementchedjhieva et al. (2021): https://arxiv.org/abs/2106.01060
- [V] Bear et al. (2021) Physion: https://arxiv.org/abs/2106.08261
- [V] Yi et al. (2020) CLEVRER: https://arxiv.org/abs/1910.01442
- [V] Liu et al. (2022) Mind's Eye: https://arxiv.org/abs/2210.05359
- [V] Ballout et al. (2025): https://arxiv.org/abs/2507.16572
- [V] Schulze Buschoff et al. (2026): https://arxiv.org/abs/2602.06033
- [V] Li et al. (2026): https://arxiv.org/abs/2604.03302
- [V] Gillman et al. (2025) Force Prompting: https://arxiv.org/abs/2505.19386
- [V] Sang (2025): https://arxiv.org/abs/2511.05540
- [V] Wu and Lu (2026) CauProphet: https://arxiv.org/abs/2610.32477
- [V] Luo et al. (2026) Flip Test: https://arxiv.org/abs/2611.19822
- [V] Zadrozny (2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12840315/
- [V] Xiang et al. (2025): https://journalpub.escholarship.org/cognitivesciencesociety/article/49778/galley/37740/download
- [V] Quillien, O'Neill and Henne (2025): https://quillienlab.github.io/Quillien%20O%27Neill%20&%20Henne%202025.pdf
- [M] Henne and O'Neill (2022), Lombrozo (2010), Thanawala and Erb (2024), via the above and https://doi.org/10.1111/cogs.13127
- [V] Ates et al. CRAFT: https://arxiv.org/pdf/2012.04293
- [V] Chen et al. (2024) CaLM: https://arxiv.org/pdf/2405.00622
- [V] Almeida et al. (2024): https://arxiv.org/pdf/2308.01264
- [V] Yu and Zhou (2026) Caliper: https://arxiv.org/pdf/2606.04915
- [V] Carro and Lagnado (2026): https://arxiv.org/pdf/2603.13236
- [V] Kankowski et al. (2025): https://arxiv.org/pdf/2501.12980
- [V] Oba and Sugawara (2026) CxMP: https://arxiv.org/pdf/2602.21978
- [V] Gjerde, Cheung and Lagnado (2025): https://arxiv.org/pdf/2502.16606
- [M] Cheung, Qiao, Brown and Lagnado (2026), read via citing text (a24)
- [M] Search logs: https://garden.causalmap.app/llm-detect-claims/ (untraceable web note), https://arxiv.org/pdf/2505.19683, https://api.crossref.org/works?query=force+dynamics+language+models
