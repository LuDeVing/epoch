# Logic and philosophy of analogical arguments: deep document

*Subfield A11.06. Evidence: evidence_a-d.jsonl (ids a01-a25, b01-b25, c01-c26, d01-d18), claims K01-K25, critique.md, all in this folder. Hesse 1966 and Bartha 2010 were never opened; the philosophy side comes from the Stanford Encyclopedia of Philosophy (SEP, Bartha) and Norton's draft chapter. Read that as one weak spot throughout.*

## 1. What it is

An analogical argument says: source S and target T share some features, S has a further feature Q, so T probably has Q too. The philosophy question is when such an argument is strong. The logic question is whether a rule can score it.

Three families of answer exist.

- **Criteria lists.** Aristotle, Mill, Keynes, Hesse (1966), textbook guidelines. They name features of a good argument.
- **Formal rules.** Carnapian inductive logic, Bayesian conditioning, determination rules (Davies and Russell 1987). They give a calculus.
- **Local or modal accounts.** Norton's material theory (each inference rests on a local fact), Bartha's articulation model (2010): the argument is plausible if the source link can be carried over.

No accepted formal logic of analogical strength exists (K03). What exists is a set of checks that catch bad analogies. That is what a scaffold can use.

Why it matters for our agent: O7 (map an analogue) needs a guardrail that says when a mapping may be trusted. The hope was a code check on "causal link" and "no essential difference". Finding of this study: the checks exist on paper, none has been tested on an LLM (K19, K24), and the philosophy itself says they cannot be fixed code rules (K23). They can be required fields that code counts.

## 2. History and theories in depth

**Aristotle.** Gave criteria close to Hesse's later ones (b25). Mill (a05): analogy is a contest of known agreements against known differences plus vast ignorance. Nine of ten shared properties gives 0.9 only if both property sets are random samples. Reid's argument for life on other planets: Stebbing calls it suggestive because the conclusion is weak; Mill rejects it because ignorance is vast (a03, b04).

**Keynes.** In his measure, one negative analogy kills learning from the positive analogy (a06). Not usable as a scoring rule (K07).

**Hesse 1966** (a01, b01). Three requirements for a good scientific analogy:

1. Material analogy: pre-theoretic, observable similarity, not just formal.
2. Causal condition: the vertical relations in the source are causal in an acceptable scientific sense.
3. No essential difference: essential source properties and causal relations are not in the negative analogy.

Hesse aims at modal plausibility, not degrees of probability. SEP judges all three on the right track but too restrictive. Formal analogy drives maths and physics (Steiner). Franklin's 12-point lightning list (1749) persuaded without a known cause. The rectangle-to-box analogy has many "essential" differences and is still good. Hesse gives no definition of "essential" beyond "causally closely related to the known positive analogy"; it depends on the use of the analogy (d16).

**Textbook guidelines** (a03, b04). Eight: more similarities strengthen; more differences weaken; more ignorance weakens; a weaker conclusion is more plausible; causal beats non-causal; structural beats superficial; weigh relevance; multiple analogies strengthen. They pull apart (Reid case). Counting similarities is ill defined. The relevance guideline carries all the weight and is not operational (K04).

**Failure of simple inductive logic** (a04, b24). Achinstein's swan and line-segment case shows that "n shared properties raise probability" over-justifies. Carnapian rules, Bayesian conditioning and liberal Bayesianism leave unconstrained room.

**Structure mapping versus causal relevance** (a09, b05). Gentner's systematicity is neither necessary nor sufficient. McKay (1993): Antarctica to present Mars is more systematic than Antarctica to ancient Mars, yet weaker, because freezing is a preventive cause (microbes in frozen Antarctic lakes; Mars 3.5 billion years ago was warmer). Causal direction matters: generative versus preventive. Schlimm (2008): in object-rich maths, maximal systematicity is trivial. Surface matches still matter in some fields (Moche pot marks, ethnographic analogy).

**Determination rules** (a08, b07, d17). If background knowledge says Q is fixed by P1..Pm, and S and T agree on all Pi, then Q transfers deductively (Davies and Russell; Weitzenfeld). Works for used-car value. Fails where relevant factors are unknown (morphine to meperidine; animal drug testing). This is the one analogy form code can verify fully, but real tasks rarely have a known determinant set (no frequency data).

**Bartha's articulation model (2010)** (a02, a12, b02, b03). Classify the analogy by the vertical relations inside each domain, not by overall similarity.

- Four relation types: predictive, explanatory, functional, correlative. The first two can be deductive or inductive; the last two inductive only.
- Two conditions. Prior Association: a clear link in the source between the shared features P and the projected feature Q. Potential for Generalization: no critical disanalogy in the target.
- Test by listing each assumption used in the source proof and asking if it has an analogue in the target. Worked example: the square has maximum area at fixed perimeter, so the cube has maximum volume at fixed surface; check each proof step in 3D.
- Two stages: prima facie plausibility (positive analogy relevant to the prior association, no critically relevant factor in the negative analogy), then qualitative strength (strength of prior association, extent of positive analogy, multiple analogies).
- Predictive case (Bartha pp.120-21), five determinants: strength of prior association, extent of correspondence, multiple favourable analogues, only non-defeating completing analogues, only non-defeating counteracting causes. Multiple analogies need a partial order "is superior than".
- Justification: van Fraassen's symmetry principle. If problems might be essentially the same, they might have the same solution. This gives "worth investigating", not a probability.
- Critic (Norton): the model needs an inference schema per relation type, so it must solve induction as a whole.

**Norton's material theory** (a11, a13, b06). The warrant is a local "fact of analogy". Galileo: moon shadows and earth shadows are both formed by straight sunlight, so the moon has mountains. Joyce (1936) said analogy works only if M and P are causally linked. Norton: even that is not enough. Water causally relates to seas and canals, yet the moon has no seas and Mars no canals. Heat as a conserved fluid failed after Joule. Successes: Galileo's moon mountains; Reynolds analogy; the liquid-drop model of the nucleus (checked empirically, Blatt and Weisskopf 1979). Failures: lunar seas, Martian canals, fish and whales, caloric. A causal link in the source is necessary but not sufficient. Norton's approach cannot be coded as a general rule.

**Analogue confirmation** (b08). Dardashti et al.: lab analogues (Hawking radiation in dumb holes) can confirm predictions about inaccessible systems given an exact formal analogy. SEP calls it controversial. Background only.

**Net state.** The criteria are accepted as screens (does the source have a causal link to Q; is there a known disanalogy that matters). Nobody has a validated scoring function. Hesse's own evidence is a few worked cases, not a systematic test (K23).

## 3. Core findings with exact numbers

Status: E established, S single-source, C contested, G gap (no study).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Hesse's three criteria are on the right track but too restrictive | 3 criteria; counterexamples: Franklin 12-point list, rectangle-box, formal analogy | a01, b01, d16 (SEP) | E (philosophy) |
| Bartha: Prior Association + Potential for Generalization; 4 relation types; 5 determinants in predictive case | list-the-proof-assumptions test | a02, a12, d16, d18 | E (2 sources, both secondary) |
| No accepted formal logic of analogical strength | Carnap, Bayes, liberal Bayes all under-constrain | a04, a10, b24 | E |
| Guidelines conflict; cannot be summed | Reid case: Stebbing "suggestive" vs Mill "reject" | a03, b04 | S |
| Systematicity not sufficient; causal direction matters | McKay Antarctica to Mars | a09, b05 | S |
| Determination rules transfer deductively but are rarely available | used-car value works; morphine/meperidine fails | a08, d17 | S |
| Zero-shot GPT-3 matches UCLA students on standard analogy sets | digit matrices N=40, generative OR=1.88 (p=0.005, CI 1.21-2.91), multiple choice OR=6.27 (p=2.3e-8, CI 3.28-11.99) | a14, c01 | C |
| Counterfactual letter strings break GPT, not humans | mean accuracy humans 0.753 (136), GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452; extended study 263 humans, GPT-4 0.078 at hardest cell | a17, b12, c03 | E |
| Hodel and West: synthetic alphabets | 121 undergraduates, 50 GPT-3 instances; accuracy under 0.1 on four problem types | a16 | E (replicates above) |
| Children and adults transfer, GPT-4o does not | adults N=62 0.88/0.91/0.89; children N=41 0.62/0.66/0.67; GPT-4o 0.85/0.63/0.48; Llama-3.1 405B 0.79/0.74/0.27; Claude-3.5 0.68/0.62/0.46 (N=54 each) | c12, c24 | E |
| GPT-4 with code execution matches humans on counterfactual strings | P=0.496; 23/50 (46%) of GPT-4 errors used a valid alternate rule vs 39% for humans | c05 | S (original authors) |
| Causal story analogies: humans choose the causal match; GPT-3 fails far analogies | humans N=54, t(53)=21.3; 15/54 always correct; GPT-3 near p=0.0039, far p=0.065; OR=0.37, p=0.0003, CI 0.21-0.63 | a15, b10, c02 | C |
| GPT-4 answer-order bias in story analogy | Webb data 0.89 (16/18) first vs 0.61 (11/18) second; own run 1.00 vs 0.72, total 0.86 (31/36); humans 0.78 in both orders | b14, d15 | S (18 stories) |
| Paraphrase lowers accuracy | GPT-4 0.86 to 0.72; humans 0.78 to 0.70; 18 stories, not clearly significant | b14 | S |
| Far narrative analogies hard for LLMs | ARN far: humans 94.1 vs models 39.6; near 97.9 vs 75.0; overall 96.0 vs 57.3; GPT-4 overall 68.1; chance 50 | b16, c07, d01 | E |
| AnaloBench: pick the analogous story among 4 | GPT-4 89.1/66.5/60.7; GPT-3.5 65.3/46.4/30.8; Claude 68.2/30.2/25.9; humans 96.0/72.5/73.3 at 1/10/30 sentences; chance 25 | a23, b23 | E |
| 2026 frontier models still weak on far analogy | ARCANA pass@3: GPT 5.2 48-51%, Gemini 3 Pro 29-43%, Grok 4.1 Fast 19-25%, Claude Opus 4.5 7-9%; humans pass@1 58-69% | d08 | S |
| Matching, not generation, is the failure | GPT-4 with hint found the right source 15/15 but accepted the wrong one too: precision about 0.50-0.52; humans precision 0.67, recall 0.26 (n=199) | d06 | S |
| Causal transfer fails in 2026 models | OpenLock: humans +33.0% (p<.001); GPT-5.2 -10.5% (p=.266); Claude-4.5 +17.9% (p=.090); Gemini-3-Flash +19.3% (p=.003); DeepSeek-V3.2 +10.5% (p=.089); GPT-5.2 common cause 11.8 vs common effect 19.7 attempts | d07 | S |
| Analogical prompting gain | about +4% over 0-shot CoT on GSM8K, MATH, Codeforces, BBH; GSM8K diverse 77.8 vs 75.9 | a19, b18, c09 | C |
| Relevance of self-generated examples is not the driver on math | MATH share correct: relevant 62.0, N/A 72.0, random 86.0; fixed verified examples 56.3 avg vs relevant 52.4; BBH relevant +1.3 over no-example | c10, d03, d04 | C |
| Self-generation needs a strong base model | retrieved beats self-generated for curie-001, davinci-001; reverses from davinci-002/003 | a20, b19 | S |
| Concept vectors are invariant for verbal relations, not abstract ones | Llama-3.1 70B 98% vs 62% abstract previous/next; steering: function vectors 50%/58% vs concept vectors 14%/2% | a21, b21 | E |
| Patching relational information fixes failures | up to 38.4% of failures fixed | a22 | S |
| Irrelevant context hurts | GSM-IC; instruction to ignore: 73.5 to 79.0 on one split | c15 | C |
| Generated critical questions are weak | no model above 57% Useful (220 interventions); best open gemma-2-27b-it 54.03; template systems about 10 points higher | a24, d05 | S |
| Thought Propagation | +12% shortest paths, +13% creative writing preference, +15% ALFWorld (134 tasks) | c16 | S |
| LLM test of Hesse/Bartha criteria | 0 papers found | a25, c22, d10 | G |

## 4. Mechanisms and models

### 4.1 Hesse screen as required fields

Per candidate analogue the agent writes a record. Code checks it is complete, not that it is true.

```
analogue = {
  source, target,
  shared: [features],                 # positive analogy
  projected: Q,                       # what we want to carry over
  link: {from: shared, to: Q,         # prior association
         kind: predictive|explanatory|functional|correlative,
         direction: generative|preventive|common_cause|common_effect,
         why: one line},
  source_proof: [step_1 ... step_n],  # why Q holds in the source
  target_check: [ {step_i, target_analogue, status: carried|not_carried|unknown} ],
  differences: [ {feature, essential: yes|no|unknown, touches_step, why} ]
}
```

Code rules (soft):

- Reject the record if `link` is empty or has no direction (Hesse 2, causal condition).
- Count `not_carried` and `unknown` in `target_check`. A `not_carried` on a step the proof depends on gives the flag "critical disanalogy". Unknowns cap confidence.
- Any difference marked essential=yes gives a flag. Essential is defined by use (d16), so the model must say which proof step the difference touches.
- Never output a number from similarity counts (K03).

This is the Bartha test turned into a schema. Hesse's "no essential difference" becomes: list differences, tie each to a proof step. A flag stays a flag. A hard reject would kill good formal and correlational analogies (a01).

### 4.2 Causal direction field (McKay)

Store whether the shared causal relation is generative or preventive. Code refuses to map a preventive source relation onto a generative target relation, and the reverse. Cheap. Untested (K05, K22). Reason to expect value: GPT-5.2 treated common cause and common effect differently while humans did not (d07).

### 4.3 Determination check (the only fully codable form)

If the task has a known determinant set {P1..Pm} for Q: code compares source and target values. Transfer is allowed only if all agree; otherwise it is blocked and the differing Pi is reported. If no determinant set is known, skip this path. How often real tasks have a known set is unknown (K23).

### 4.4 Retrieval-first sourcing

Models fail to find far analogues (AnaloBench, ARN, ARCANA) and fail to reject wrong sources (d06, precision about 0.5). So: sources come from a fixed bank or from memory of solved problems; the model proposes mappings; code checks the record of 4.1. The Hesse check targets the false-accept rate, which is the failure that was measured.

### 4.5 Order-swap and surface-variant checks

For any analogy choice: run both answer orders in code, accept only agreeing answers, count flips as a failure signal (K25). Run a mutated surface version (renamed entities, permuted symbols) and require the same mapping (G3). With code execution available, let code apply the inferred rule to the mutated input (c05).

### 4.6 Fixed critical-question list

Use a human-written Walton checklist for argument from analogy: are the cases similar in the relevant respects; are there differences that undercut the inference; does another analogy point the other way? Do not let the model generate the questions (a24, d05).

## 5. What holds up

**Holds.**

- LLMs fail counterfactual letter-string analogies where humans do not. Independent groups: Lewis and Mitchell (two papers; 136 and 263 humans), Hodel and West (121), Stevenson (62 adults, 41 children), with partial agreement from Musker et al. (b20). Established.
- Far analogies are hard. ARN, AnaloBench, ARCANA and story analogies all show a gap; the 2026 ARCANA result shows it persists in frontier models.
- Moving the check to code helps: GPT-4 with code execution reaches human level (c05; original authors, not independently replicated).
- No accepted formal logic of strength; guidelines conflict.

**Failed or weakened.**

- Webb 2023 "emergent analogy" holds for standard, familiar surface forms and fails when the surface changes. Webb's reply: digit matrices already included counterfactual reordering, and code closes the gap. Unresolved: pattern matching on familiar forms plus weak rule inference.
- Analogical prompting's mechanism. Yasunaga: +4% from relevant self-generated examples. Qin: on GSM8K and MATH, random examples match or beat relevant ones; no-example is best on average. This is a partial replication failure, not total: on BBH relevant helps (+1.3). Example accuracy explains the math gain (relevant 62.0% correct vs random 86.0%). Boundary: GPT-3.5, math.
- Hesse's criteria as hard code rules: SEP itself says they are too restrictive and "essential" depends on use.
- Generated critical questions: capped at 57% Useful.

**Moderators.**

- Model scale: self-generated analogues help only from davinci-002/003 up.
- Rule generality: accuracy falls as the number of generalisations rises (GPT-4 0.078 at the hardest cell).
- Answer order and paraphrase (18 stories only).
- Context length: AnaloBench GPT-4 falls from 89.1 to 60.7, and Claude falls to chance (25.9) at 30 sentences.
- Code access.

**Conflicts to remember.** Qin finds irrelevant examples harmless on math; Shi finds irrelevant sentences in the problem hurt. These are different manipulations (example text vs problem text), but it weakens a simple "filter irrelevance" rule.

**Interventions.** Worked: code execution (c05); few-shot plus CoT on ARN (halves the gap at best); retrieval over self-generation for small models; fixed verified examples on math; permutation debiasing for multiple choice (d14, snippet only). Did not work: relevant self-generation on math; unaided search of an analogue bank (retrieval near random, a23); model-generated critical questions.

**Evidence-base caveats.** All human samples are Western students or Prolific workers; the children data is one lab (K09). Several numbers come from abstracts only (b22, b23, c04, c23, c26).

## 6. Language models

What they do on analogy tasks, from easy to hard:

1. **Standard text analogies.** Strong. GPT-3 at or above student level (OR 1.88 and 6.27). 2026 models handle standard letter strings (advice correct 84.6% across four models, d11).
2. **Surface-changed analogies.** Weak. GPT-3.5 0.350, GPT-4 0.452 vs humans 0.753. GPT-4o 0.85 to 0.48 and Llama-3.1 405B 0.79 to 0.27 on far alphabets while adults stay near 0.89. No 2025-2026 reasoning-model run of the counterfactual variants was found (d09). Gap.
3. **Causal story matching.** Near fine, far weak for GPT-3. GPT-4 is better but order-biased (0.89 vs 0.61 in Webb data; 1.00 vs 0.72 in the authors' run).
4. **Far narrative analogy.** Models 39.6 vs chance 50 on ARN far; AnaloBench Claude at chance for 30 sentences; ARCANA Claude Opus 4.5 7-9%.
5. **Judging strength by a philosophical criterion.** Untested. Closest: GPT-4 accepts wrong sources (precision about 0.5, d06) and fixed-question critics reach 57% Useful.
6. **Causal transfer by structure.** Mixed in 2026: only Gemini-3-Flash significant.

Inside the model (a21, a22, b21): relations can be encoded correctly and still not reach the output. Patching a correct pair into a failing case fixes up to 38.4% of failures. So the model's self-report of its mapping is unreliable, and code-side checks beat introspection (also G10).

What changed performance, and by how much:

| Change | Effect | Source |
|---|---|---|
| Code execution (GPT-4) | from below humans to P=0.496 vs humans (no difference) | c05 |
| Few-shot + CoT on ARN | gap to humans halved at best | c08, d02 |
| Self-generated relevant examples | +4% avg (Yasunaga); not better than random on math (Qin) | a19, c10 |
| Fixed verified examples vs per-query relevant | 56.3 vs 52.4 avg on GPT-3.5 | d03 |
| Ignore-irrelevant instruction | 73.5 to 79.0 (one GSM-IC split) | c15 |
| Template-guided questions | about +10 points over the 57% zero-shot ceiling | d05 |
| Thought Propagation | +12% / +13% / +15% (single source) | c16 |
| Activation patching | up to 38.4% of failures fixed (needs open weights) | a22 |

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested. Parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **O7 mapping is a typed record that code checks for completeness** (link, direction, source proof steps, target analogue per step, listed differences). Basis: models fail the matching step, not generation (d06), and relational content can be present but unused inside the model (a21, a22). Part O7/G5. [E] for the failure; the record's benefit is untested, so this is a form change, not a claimed gain. Ids: K01, K02, K09, K11; a01, a02, a12, a21, a22, d06, d16.
2. **Far analogues are never trusted unaided.** Take sources from a fixed bank or from memory of solved problems. Part O7/memory. [E]. Ids: K11; b16, c07, a23, d01, d08.
3. **Every analogy-dependent answer passes a mutated-surface check (G3).** Rename entities or symbols and require the same mapping; where possible let code apply the inferred rule. Part G3/S4. [E]. Ids: K09; a17, b12, a16, c12, c05.
4. **No numeric analogy-strength score from similarity counts.** Candidate for section 4b: "more shared features, higher confidence" over-justifies (Achinstein) and Keynes and Mill show it does not sum. Part G5. [E]. Ids: K03; a04, a06, b24.
5. **Hesse and Bartha criteria enter only as soft flags**, never hard rejects, because a hard reject kills good formal and correlational analogies. Part O7. [E] as philosophy. Ids: K01, K23; a01, d16.

### Test first (not yet allowed in the schema)

- Hesse/Bartha record versus no record on judging classic analogies (K19, K24). [S, gap]
- Causal-direction field on McKay-type items (K05, K22). [S]
- Determination-rule code check where determinants are known (K06). [S]
- Order-swap accept-if-agree for analogy choice (K10, K25). [C/S]
- Self-generated analogues versus accurate-but-irrelevant examples (K12). [C]
- Model-size gate for self-generation (K13). [S]
- Fixed Walton question list for analogy arguments (K17). [S]
- Thought Propagation (K16). [S]
- Known essential difference in a retrieved exemplar lowers O7 accuracy (K21). [S]

Full list with thresholds: UNKNOWNS.md.

## 8. Concrete tests on our bench

All arms get equal tokens, with setup counted (G7). Report accuracy with a paired bootstrap interval over items.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Record | 30 classic analogies (Reid, McKay, Franklin, rectangle-box, Galileo moon, caloric) with philosopher verdicts, plus 30 held-out new ones | plain judge; judge + Hesse/Bartha record; judge + unstructured "think about differences" | agreement with verdict; false-accept rate | record cuts false accepts by about 10 points; plain and unstructured about equal (cf. 4b) |
| T2 Causal direction | 40+ McKay-type pairs where a preventive cause flips the verdict | typed mapping with direction vs without | accuracy on flipped items | gain concentrated on preventive items |
| T3 Surface variants | counterfactual letter strings (permuted, symbol, longer interval) and 20 renamed story analogies | text-only reasoning; code-applied rule | accuracy by number of generalisations | code arm closes most of the gap (c05) |
| T4 Order swap | story analogy choice, 60+ stories (not 18) | single order; both orders accept-if-agree | accuracy of accepted answers; flip rate | accepted accuracy rises; flip rate 10-30% on weaker models |
| T5 Relevance vs accuracy | GSM8K/MATH-style and BBH-style items | no example; relevant self-generated; random self-generated; verified fixed; accurate-irrelevant | accuracy | accuracy of examples explains the gain; relevant not above random on math |
| T6 Source acceptance | 30 source/decoy pairs (d06 style) | free choice; record with differences listed | decoy false-accept rate | falls from about 0.5 |
| T7 Determination | tasks with known determinant sets (pricing, units) | model judgement; code compares determinants | wrong-transfer rate | near zero on the code arm |
| T8 Model gate | O7 self-generation vs retrieved exemplars | across model sizes available | accuracy | crossover where davinci-002 sat |

## 9. What does not transfer, and why

- **Hesse's observable "material" similarity** is a notion for scientists; the agent works on text and puzzles where the surface is symbols. There, surface similarity is often a trap.
- **Probability of the conclusion.** Hesse and Bartha aim at plausibility ("worth investigating"), not probability. Do not turn it into a score.
- **Norton's local facts** need domain knowledge per case; there is no general rule to code.
- **Analogue confirmation** (Hawking radiation) needs an exact formal analogy; not our setting.
- **Human-lab data.** Western students and Prolific workers; one lab for children. Do not set thresholds from these.
- **Interpretability results** (concept vectors, patching) need open weights and activations; a black-box scaffold cannot use them. They are an argument for code-side checks.
- **Thought Propagation and similar task gains** come from specific tasks and one group; do not assume carry-over.

## 10. Open questions

1. Does a Hesse/Bartha record improve an LLM's judgement of analogical arguments? No study (K19, K24).
2. Does a typed causal-direction field help (K22)?
3. Is the analogical-prompting gain due to relevance or to example accuracy and length? Closed for math; open elsewhere.
4. Do 2025-2026 reasoning models still fail the counterfactual letter-string variants? Not tested.
5. How often do real tasks have a known determination set (K23)?
6. Do order and paraphrase biases hold on large story sets (18 now)?
7. What is Hesse's and Bartha's own evidence beyond worked cases? Needs the books or Norton's full chapter to build a labelled case set.
8. Does a known essential difference in a retrieved exemplar lower accuracy?
9. Does a human-written Walton list lift argument-from-analogy judging above 57%?
10. Per-model ARN far-analogy values are unchecked (only the means are confirmed, d01).

## 11. Sources

[V] opened, [M] snippet or abstract only.

- [V] Bartha, Analogy and Analogical Reasoning, SEP (a01-a10, b01-b08, b24, b25, c18, d16-d18). https://plato.stanford.edu/entries/reasoning-analogy/ (part read through a summariser)
- [V] Norton (2011 draft), Analogy chapter (a11-a13). https://sites.pitt.edu/~jdnorton/papers/Analogy.pdf
- [V] Webb, Holyoak, Lu (2023), Emergent analogical reasoning in LLMs (a14, a15, b09-b11, c01, c02, c25). https://arxiv.org/abs/2212.09196
- [V] Hodel and West (2023), Response (a16; c04 was marked [M] earlier but a16 opened it). https://arxiv.org/abs/2308.16118
- [V] Lewis and Mitchell (2024), counterfactual tasks (a17, b15, c03). https://arxiv.org/abs/2402.08955
- [V] Lewis and Mitchell (2024/2025), robustness (a18, b12-b14, d09, d15). https://arxiv.org/abs/2411.14215
- [V] Webb et al. (2024), counterfactual reply (c05). https://arxiv.org/abs/2404.13070
- [V] Yasunaga et al. (2024), LLMs as analogical reasoners (a19, a20, b18, b19, c09). https://arxiv.org/abs/2310.01714
- [V] Opielka, Rosenbusch, Stevenson (2025), concept vectors (a21, b21, c13). https://arxiv.org/abs/2503.03666
- [V] Lee et al. (2025), Curious Case of Analogies (a22). https://arxiv.org/abs/2511.20344 ([M] d12)
- [V] AnaloBench (a23). https://arxiv.org/abs/2402.12370
- [V] Calvo Figueras and Agerri (2025), critical questions (a24, d05). https://arxiv.org/abs/2505.11341
- [V] Sourati et al. (2024), ARN (b16, b17, c07, c08, d01, d02). https://arxiv.org/abs/2310.00996
- [V] Musker et al. (2025) (b20, c06). https://arxiv.org/abs/2406.13803 ; https://doi.org/10.1016/j.jml.2025.104676
- [V] Hu et al. (2023), in-context analogical reasoning (b22, c17; abstract level per critique). https://arxiv.org/abs/2305.17626
- [V] Wijesiriwardene et al. (2023), ANALOGICAL (b23; abstract level per critique). https://arxiv.org/abs/2305.05050
- [V] Qin et al. (2025), Relevant or Random (c10, c11, d03, d04). https://arxiv.org/abs/2404.12728
- [V] Stevenson et al. (2025), children vs LLMs (c12, c24). https://arxiv.org/abs/2411.02348
- [V] Lampinen et al. (2024), content effects (c14). https://arxiv.org/abs/2207.07051
- [V] Shi et al. (2023), GSM-IC (c15). https://arxiv.org/abs/2302.00093
- [V] Yu, He, Ying (2024), Thought Propagation (c16). https://arxiv.org/abs/2310.03965
- [V] Puranam, Sen, Workiewicz (2025) (d06). https://arxiv.org/abs/2505.00603
- [V] Xiang et al. (2026), OpenLock transfer (d07). https://arxiv.org/abs/2604.24062 (summariser)
- [V] Chen, Wang, Wang (2026), ARCANA (d08). https://arxiv.org/abs/2610.29271
- [V] Available but Unclaimed (2026), letter-string subset (d11). https://arxiv.org/abs/2609.16793
- [V] arXiv search results, Nov 2026 (d10, c22). https://arxiv.org/search/?query=%22argument+from+analogy%22+language+models&searchtype=all
- [M] Hesse (1966), Models and Analogies in Science (c20). https://www.ndpress.nd.edu/
- [M] Bartha (2010), By Parallel Reasoning (c19). https://global.oup.com/academic/product/by-parallel-reasoning-9780195325539
- [M] Davies and Russell (1987), IJCAI-87 (c21). https://www.ijcai.org/Proceedings/87-1/
- [M] Mitchell (2021), Abstraction and analogy-making in AI (c23). https://arxiv.org/abs/2102.10717
- [M] Gentner and Toupin (1986) (c26). https://doi.org/10.1207/s15516709cog1003_3
- [M] McGovern et al. (2026), probing analogical reasoning (d13). https://arxiv.org/abs/2604.03877
- [M] Zheng et al. (2024), LLMs are not robust multiple choice selectors (d14). https://arxiv.org/abs/2309.03882

Links to parallel subfields (not covered here): Analogical problem solving; Connectionist and hybrid mapping models; Incremental mapping; Fallacy theory; Argument standardisation and diagramming; Surface-cue heuristics; Dynamic memory, early CBR.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 6 established claims: 4 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A11.06-K01** (reworded: the sources support less). SEP says the causal and no-essential-difference conditions are 'on the right track' but too restrictive, whereas for the material-analogy (observable similarity) requirement it says there are good reasons not to accept it in Hesse's narrow sense (formal analogies drive maths and physics). Corrected claim: Hesse (1966) gave three requirements for a good scientific analogy: material analogy (observable similarities), a causal condition on the source's vertical relations, and no essential difference in the negative analogy; she sharpened Aristotle's earlier account. SEP judges the causal and no-essential-difference conditions on the right track but too restrictive (they exclude correlational cases such as Franklin's lightning list and good analogies like rectangle/box), and rejects the narrow material-analogy requirement because formal analogies drive inference in mathematics and physics.
- **A11.06-K09** (number corrected). In Lewis and Mitchell (TMLR 2025) Table 1 the 0.078 at three generalisations belongs to GPT-3.5 (GPT-4 is 0.195, humans fall to 0.260 too, so humans also degrade with more generalisations but stay above the GPT models); all other numbers check out. Corrected claim: Counterfactual letter-string analogies (permuted, symbol or longer-interval alphabets) break GPT models far more than humans. Lewis and Mitchell: mean accuracy over all alphabets, humans 0.753, GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (136 humans); extended study with 263 humans shows accuracy falling with more generalisations for all (at three generalisations humans 0.260, GPT-4 0.195, GPT-3.5 0.078). Hodel and West (121 humans) find the same for GPT-3; Stevenson et al. find children (7-9) and adults transfer to Greek and symbol alphabets while GPT-4o falls from 0.85 to 0.48 and Llama-3.1 405B to 0.27. Boundary: Webb et al. reply that GPT-4 with code execution matches humans (P=0.496).
