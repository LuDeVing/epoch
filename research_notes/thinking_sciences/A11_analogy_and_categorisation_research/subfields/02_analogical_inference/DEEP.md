# Analogical inference: deep document

*Subfield A11.02. Written 2026-11-01 from evidence_a-d.jsonl (a01-a26, b01-b27, c01-c25, d01-d21), claims.jsonl (A11.02-K01 to K29) and critique.md. Evidence ids below are the ids in those files. Where the cross-checker corrected a line, the correction is used here (c03 is not used; StoryAnalogy best model is about 48%; Yasunaga's headline is not equal-token).*

## 1. What it is

Analogical inference is the step after a source and a target have been aligned. The agent has a source case it understands (water flow, an earlier solved problem, a known rule) and a target it does not. It carries a conjecture from source to target. "Pressure difference makes water flow, so a temperature difference may make heat flow."

In the Structure-Mapping Engine (SME) this output is called a **candidate inference**. SME makes three outputs per mapping: correspondences, candidate inferences and a structural score (a01). The authors call candidate inferences "surmises", not valid conclusions. SME has no domain knowledge and no logic. Testing truth is left to other modules (a01, a26).

Three separate jobs hide under the one name. Keep them apart.

1. **Select** which source facts to project (a structural question: which facts hang off what is already mapped).
2. **Project** them with substitution (which target element stands in for which source element).
3. **Test** whether the projected claim is true in the target (a truth question).

SME does 1 and 2. It does almost nothing for 3. Humans do 1 well and 3 only partly. LLMs do 1 and 2 loosely and often skip 3.

Why it matters for our agent: this is operator O7 ("Map an analogue ... checked by code") and guardrail G3 (a pass must be on something the answer was not fitted to). The research here says what "checked" must mean.

Scope note. This document does not repeat analogical retrieval (MAC/FAC), conceptual blending, candidate-inference selection in design, case-based reasoning or transfer of learning. Those are other subfields in the same run. Links are noted in section 9.

## 2. History and theories in depth

**Gentner structure-mapping (1983) and SME (Falkenhainer, Forbus, Gentner 1989) [V a01-a06, a26].** The theory says an analogy maps relations, not object attributes, and prefers mappings with deep, connected relational structure (the systematicity principle). SME turns this into an algorithm.

- Match rules produce local matches. Structural consistency keeps them coherent: one-to-one mapping and parallel connectivity (arguments of matched relations must match).
- Matches are merged into global mappings ("gmaps"), scored by structural evaluation.
- For each gmap, candidate inferences are made. A base statement is projected only if (i) it is consistent with the gmap's substitutions and (ii) it is **structurally grounded**: it connects to something already matched. For each base root that is an ancestor of a matched root, every descendant not yet in the gmap becomes a candidate inference (a02).
- Worked example (a03): GREATER-THAN(DIAMETER(coffee), DIAMETER(ice-cube)) is NOT inferred in the pressure-to-temperature mapping, because it does not connect to the mapped causal structure. Only the CAUSE link from temperature difference to heat flow is projected. Three gmaps: weights 6.99 (one inference), 3.94 (none), 2.44 (none).
- Unmatched base entities get a "skolem" placeholder in the target (a04). In the heat-flow case this produced (:skolem pipe), later resolved to physical contact or immersion by another module. Carryover analogies (building a model by analogy when the target is nearly empty) are almost all candidate inferences.
- The only built-in consistency check is thin (a05): drop a candidate if the predicate is non-commutative and the candidate is a permuted copy of a known target fact (GREATER(MASS planet, MASS sun) is dropped if the reverse is known).
- Cost: worst case about O(N^2), typical about O(N) (a02).
- The authors suggest a tuning idea (a06): a conservative strategy might prefer gmaps with some candidate inferences but not too many.
- Authors flag a risk (a26): hand-translating stimuli into formal form can leak the answer. The algorithm does not address it.

**Rival: the pragmatic/causal tradition (Holyoak and Thagard, ACME, 1989; Lee and Holyoak 2008; Holyoak, Lee, Lu 2010).** Relevance to the goal and a causal model drive mapping and inference (a06 gives the SME side's three objections: no account of soundness through systematicity, only works in problem-solving contexts, ignores that access follows surface similarity). The ACME paper itself was not opened (host refused). Lee and Holyoak 2008 and Holyoak, Lee, Lu 2010 were read at abstract level only (d17, d19). Their claim: analogical inference is mediated by building and running a causal model, and inference strength can separate from overall mapping quality.

**Philosophy of analogical argument (Bartha; Hesse; Norton; Davies and Russell) [V a11-a14].** Four accounts of when an analogical inference is licensed.

- Hesse: material similarities, causal vertical relations in the source, no essential difference between source and target. Called too narrow by the review.
- Bartha's articulation model: **Prior Association** (the source's known similarities are tied to the projected feature by a clear link) and **Potential for Generalisation** (that link plausibly holds in the target, with no critical disanalogy).
- Norton's material theory: no universal form; each inference is licensed by a local fact about the domain. Fails when the uniformity is what the inference is trying to show.
- Davies and Russell determination rules: valid if the property is a function of factors P1..Pm and source and target agree on all of them. The justification problem returns as justifying the rule.
- Systematicity does not guarantee truth (a14): in the Antarctica-to-Mars example the more systematic mapping gave the weaker inference, because freezing temperatures act as preventive causes.

**Human experiments on which facts get carried over.**

- Clement and Gentner 1991 (3 experiments) and Markman 1997 (4 studies): people prefer facts that hang off a shared causal system (details in section 3).
- Lassaline 1996 (abstract only, d20): shared attributes raise similarity and inductive strength; binding causal relations that connect a shared attribute to the candidate inference raise inductive strength. Salience: causal beats temporal.
- Spellman and Holyoak 1996 (second hand, b09): plot extensions nearly always kept character correspondences.
- Colhoun and Gentner 2009 replicated Lee and Holyoak's preventer result and argued for SME plus a later causal calculation (two steps). Lee and Holyoak argue one causal-model process. This dispute is unresolved (K07, contested).
- Day and Gentner 2007 (abstract only, d18): readers used a similar earlier passage without being aware, and the effect depended on structural mapping, not priming. Reading-time data suggest it happened while encoding the target.

**LLM era.** From 2022 the question became: do language models do analogical inference? Webb, Holyoak and Lu (2023) claimed emergent analogical reasoning in GPT-3. Hodel and West (2024), Lewis and Mitchell (2024) and Stevenson et al. (2025) challenged this with counterfactual (permuted or symbol alphabet) letter strings. Webb et al. (2024) replied that failures come from counting and that GPT-4 with code is near human. Parallel lines: narrative analogy benchmarks (ARN, StoryAnalogy), analogical prompting (Yasunaga et al.), Thought Propagation, case-memory agents (Memento, MemRL), and 2025-26 studies of relational complexity (REL), noisy Raven (I-RAVEN-X) and verifier quality (REFUTE).

## 3. Core findings with exact numbers

Status key: **established** = two or more independent sources; **single-source**; **contested**. "Human" means undergraduates in written-passage studies. Status for each row follows claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| SME outputs correspondences, candidate inferences, a score; inferences are surmises | Example gmap weights 6.99 / 3.94 / 2.44; only the top gmap has an inference | Falkenhainer et al. 1989 (a01, a03) | established (model description) |
| Grounding rule: project only facts connected to matched structure | Worst case O(N^2), typical O(N); ungrounded diameter fact not projected | a02, a03 | established (K03, with b05, d20) |
| SME's own validity check is thin | Drops only permuted copies of known non-commutative facts | a05 | established (K01) |
| Humans prefer shared-causal-system facts: Exp 1 ratings | N=48. Analogy group 6.28 vs 4.89; target-only control 5.22 vs 5.31; F'(1,44)=13.99, p<.001. Choice 3.17 vs 2.0 of 4, F(1,44)=18.43. Per passage 67-92% vs 42-54% | Clement and Gentner 1991 (a07, b01) | established (K02) |
| Same, Exp 2: predicting new target facts (the candidate-inference test) | N=32. Shared minus different per subject 1.63 vs 0, F(1,28)=20.05. Free prediction: shared .53, different .12, other .27 (analogy) vs .12, .12, .74 (control). Choice 2.9 vs 1.8, F(1,28)=16.43. Holds with one possibly biased passage removed, F(1,28)=13.03 | a08, b02 | established |
| Same, Exp 3: base out of view | N=48. Shared minus different 0.92 vs 0.13, F(1,44)=5.15, p<.05. Choice 1.875 vs 1.0 of 3, F(1,44)=13.15. One passage failed, poor memory of base | a09, b03 | single-source (same lab; K08) |
| Markman 1997 Exp 1: people list more shared-system inferences | N=32. Per item: shared .52, nonshared .22 (t(31)=3.97), other (not in base) .56. Shared vs other not reliable | b05 | established (K02) |
| Markman Exp 2 | N=60. Per trial shared 1.26, nonshared .30 (t(59)=7.32), other .58. Type F(2,116)=30.49. Facts from mapped departments 0.77 vs 0.50 | b06 | established |
| Markman Exp 3 and 3a (base in memory) | Exp 3, N=48: 1.45 vs .39 (t(46)=6.23). Exp 3a, N=78: 1.41 vs .36 (t(77)=7.20); right department pair mapped by 85% (66/78), no-shared-facts pair by 12% (9/78). Chain-valence effect flipped between 3 and 3a, unexplained | b07 | established |
| Humans keep one-to-one in inference | Zero inconsistent substitutions in 4 studies. Chains kept separate: 46 of 50 (92%) in Exp 2; mixed 5 of 24 (21%) in Exp 3, 5 of 44 (11%) in Exp 3a | b08 | single-source (K04) |
| Humans also invent inferences not in the source | Markman Exp 1: other .56 vs shared .52 | b05, b06 | single-source (K05) |
| Free-prediction summary from other studies | 53% shared-system, 22% unshared base facts, 18% other; controls named a key fact 18% | b09 (second hand) | single-source |
| Shared preventer: similarity up, effect inference down | N=70. Similarity GGP 7.53, GG 6.35, GP 5.01. Effect rating GG 89.4, GGP 74.4, GP 46.1 (F(2,270)=164.6). Study 1B N=22 endorsed: effect GGP .65, GG .86, GP .18 | Colhoun and Gentner 2009 (b11, b12) | single-source; replicates Lee and Holyoak direction (K06) |
| Causal facts stated in base or target make no difference to effect ratings | N=32 in 4 groups of 9-11. Group F(2,56)=.55 n.s., target type F(2,56)=56.1 | b13 | single-source, tiny groups |
| Is inference one causal process or two? | SME plus later causal calculation fit Lee and Holyoak data "closely" (authors' own, not blind) | b14, d17 | contested (K07) |
| Systematicity is not a truth guarantee | Antarctica to Mars: more systematic mapping gave weaker inference | a14 | single-source (K23) |
| GPT-3 vs students on analogy tasks (2023) | Digit matrices N=40: generative OR 1.88 (CI 1.21-2.91, p=.005), multiple choice OR 6.27 (p=2.3e-8), item correlation r(30)=.39. Letter strings N=57, OR 1.76 (p=6.3e-5). Stories N=54: OR 0.37 (CI .21-.63, p=.0003); 15/54 perfect. Far stories GPT-3 p=.065 | Webb et al. 2023 (a15, b17, c01, c02) | contested (K09, K10) |
| Letter-string transfer collapses on changed alphabets | Humans .753 (1,876 samples), GPT-3 .488, GPT-3.5 .350, GPT-4 .452 (6,840 each). Errors by wrong rule: GPT-3 30.97%, GPT-4 32.67%, humans 14.67%. Alternative valid rule: GPT-3 5.81%, GPT-4 22.00%, humans 38.59% | Lewis and Mitchell 2024 (a18, b19, critique) | established (K09) |
| Same, children and symbol alphabets | Latin/Greek/Symbol: adults .88/.91/.89 (n=62); children .62/.66/.67 (n=41); GPT-4o .85/.63/.48; Claude-3.5 .68/.62/.46; Llama-3.1 405B .79/.74/.27; Gemma-2 27B .60/.39/.14 (54 runs each) | Stevenson et al. 2025 (a20) | established |
| Hodel and West | N=121 students vs GPT-3 averaged over 50 instances; only 2 of 6 problem types (remove redundant letter, sort) not hurt | c05, a17 | established (K09) |
| Counting reply | GPT-4 + self-written code about human level; 46% of GPT-4 errors valid alternative rule vs 39% humans. Human N=99 and 97. Code sample 60 per interval, hand scored. Interval 2: GPT-4 P<2e-16, GPT-4+code P=.066 | Webb et al. 2024 (a19, c04) | contested (K10) |
| Far-domain narrative analogy is hard | Near: humans 97.9, models 75.0. Far: humans 94.1, models 39.6 (chance 50). GPT-4 mean 68.1, SBERT 42.3. Far analogy against near distractor: models 33.9. Humans over partitions 98.6/97.2/96.8/91.4 | ARN, Sourati et al. 2024 (a22, b22, c08) | established (K11) |
| StoryAnalogy | 4-way choice: random 25%, humans 85.7%, ChatGPT about 30%, other cells up to 44.2 (GPT-3.5), best about 48%, best LLM 37.7 points below humans. Fleiss kappa 47% entity, 42% relation | Jiayang et al. 2023 (a23, c20, critique) | established (K11) |
| Order and wording sensitivity | GPT-4 stories: answer first 1.0 (18/18) vs second 0.72 (13/18); humans .78 both. Paraphrase .86 to .72. Permuted Pairs coef -1.78 (Claude 3), -1.68 (GPT-4), -2.34 (Llama-405B), all p<.001, humans unaffected. Prompt wording alone moved accuracy about 20% to about 100%. Typos cost 3-7% relative | b20, b21, c06, c21 | established (K12) |
| Analogical prompting gain | About +4% average. Codeforces Acc@1/Acc@10, GPT-3.5: 8/24, 9/27, 11/27, 13/25, 15/29 (0-shot, 0-CoT, 3-shot CoT, self-gen exemplars, exemplars+knowledge). GPT-4: 16/30, 16/29, 17/31, 17/32, 19/37 | Yasunaga et al. 2024 (a21, b24, c11) | contested (K13) |
| ...but relevance is not what helps | GPT-3.5 average: relevant 52.4, no-example 55.8, random same-type 55.7, random different 55.2, random biology 54.9. GPT-4o-mini GSM8K: relevant 90.7, no-example 91.9, random 92.6/92.3/93.2. BBH average relevant 63.2 (best), random-same 61.9, random-biology 60.4. Cosine relevance: relevant .48, oracle .64 | Qin et al. 2025 (d10) | single-source; makes K13 contested |
| Self-generated sources only help strong models | Retrieved labelled exemplars beat self-generated for text-curie-001 and davinci-001; from text-davinci-002 up self-generation passes. GSM8K strongest column: 5-shot CoT 50, retrieved 54, self-generated 57-61 (rows partly garbled; trust text direction) | b25, c12 | single-source (K14) |
| Failure audit of analogical prompting | n=100. Of 50 wrong: 10 irrelevant exemplar, 12 relevant but wrong, 28 relevant and correct yet failed (12 generalisation gap, 8 over-reliance on exemplar, 8 other). Of 50 right: 6 irrelevant, 9 relevant wrong, 35 relevant correct | c13 | single-source (K15) |
| Thought Propagation | +12 points optimal shortest paths, +13% human preference creative writing, +15% agent planning. ALFWorld: Reflexion 79.1, TP variants about 83.7-94.8, best used real environment trials. 1 layer gets most of the gain. 5-shot no better than 1-shot | Yu et al. 2024 (c14-c16) | single-source (K16) |
| Re-representation helps | Raven centre: number naming 77.2% (GPT-3 175B) vs at most 51.8% others. Decomposition +2.8 (GPT-3 175B), OPT 125M 22.2 to 45.6, OPT 1.3B 47.2 to 72.0; about +20 on multi-component | Hu et al. 2023 (c17) | single-source (K17) |
| Rationale does not track choice | GPT-4 rationales often name the right message and pick wrong, or follow keywords. Human justifications post hoc too | c10, a10, b04 | established (K18) |
| Far demos help far, hurt near | About +10 points for GPT-3.5 and Llama-2 on far; GPT-4 stable. Best model still halfway between chance and humans | b23, c09 | single-source (K19) |
| Case memory helps out of distribution | +4.7 to 9.6 points (Memento); confounded by GPT-4.1 planner, o4-mini executor | c23, d13 | single-source (K20) |
| Verifiers: counterexample search is weak | o3-mini (high) with execution feedback finds a counterexample for under 9% of wrong solutions though it solves up to 48% from scratch. Oracle solution supplied: DeepSeek V3 15.1, R1 9.9. 35% of random-search attempts end in an incorrect counterexample; 86% from wrong brute-force code, 14% from test-case validation errors. Execution feedback removed all validation failures (R1 45, V3 36 at zero shot) | REFUTE, Sinha et al. 2025 (d06) | established with d07-d09 (K24) |
| Verification vs more samples at equal compute | Llama-3.1-8B, MATH: generative verification first matches self-consistency after up to 8x compute, +3.8% at 128x. Selective verification (Qwen3-4B) 76.3 vs always 75.5, harmful flips 2.2 to 1.0%, but an 8,192-token first solve got 76.0 with 28% fewer tokens | d07, d08 | established (K24) |
| Same-model self-check is conditional | Beats likelihood baseline on ARC-Challenge for some models, unreliable on TruthfulQA-MC, worse for DeepSeek-R1-Distill-8B (abstract and intro only) | d09 | single-source |
| Reasoning models have not closed the gap on related tasks | I-RAVEN to I-RAVEN-X with noise: o3-mini 86.6 to 17.0, R1 80.6 to 23.2 (chance 12.5), 3.4x more reasoning tokens; o3-mini high 31.0 at 53,596 tokens. A2RBench: top 39.8 vs humans 68.5. REL: Claude Opus 4.5 and Gemini 3 Pro fall to about 12% (chance 12.5), GPT-5.2 drops about 40%; 4k-16k more thinking tokens +2 to 3 points | d02, d03, d04 | established (K25) |
| Toolkit did not remove the relational-complexity drop | GPT-5.4 + RDKit recall 0.109/0.094/0.079 by molecule count; precision 0.638/0.428/0.470. Not paired (different model without tools) | d05 | single-source |
| Correct sources gate transfer | Retrieved labelled cases: GPT-4o F1 43.27 to 75.37; flipped labels 59.17. DeepSeek-V3 46.07/81.82/70.49. Qwen3-8B 50.48/65.81/46.33 (below baseline). Claude 3.7 Sonnet 75.36/77.04/85.33 (exception). Similarity-only retrieval plateaus; utility re-ranking +3.8 avg; learned Q r=.861 with success (21.5% to 88.1%) | d12, d13 | established (K26) |
| Unrequested transfer from a metaphor | APPS, metaphorical vs literal skill, per-sample steering: Qwen-Coder-Next 80B 23.3 vs 9.6; DeepSeek-Coder-33B 34.5 vs 4.4; Gemma-4-31B 23.6 vs 2.9. Detector macro F1 86.6% (270 examples). Adversarially searched, so upper bound | d15, d18 | single-source (K27) |
| Surface decoys win when relations are weakly encoded | 7-14B models: failures align as much with the noun-similar distractor as with the target; patching fixed up to 38.4% (and 38.1% more); overall 49.8 / 61.9 / 55.3% (Llama-2-13B / Gemma-7B / Qwen2.5-14B). Probe accuracy 82.9% middle layers. One irrelevant sentence: at most 18% of GSM8K problems still solved under every distractor type; 20-sample vote +11 micro | d14, d16 | single-source (K28) |
| Analogy-then-solve boosts novelty, not correctness | 150 generations x 50 problems. Binary novelty 50.4 / 58.8 / 68.8% (Claude / GPT / Gemini) vs cross-domain 21.6 / 27.2 / 37.9 and no-domain 1.6 / 8.8 / 8.6. Vendi diversity +90 to 173%. Same call count (2), tokens not compared | d11 | single-source (K29) |
| Copy training lets a small model learn letter-string analogy | Small 3-layer model: 96.7 seen / 93.9 new alphabets with copy tasks and 200 alphabets; 60.9 / 26.5 with 20 alphabets, no copy; new transformations 3-13%. Gemini 2.5 Flash and Llama 3.3 70B improved with 1-5 examples; GPT OSS got worse with 2 or more | Hellwig et al. 2026 (d01) | single-source (training result) |

## 4. Mechanisms and models

### 4.1 The SME inference pipeline (what an engineer would build)

Input: a source description and a target description, each as typed statements: entities, attributes, first-order relations, higher-order relations (CAUSE(x, y) over relations).

1. **Local matches.** For each pair (source statement, target statement) with the same predicate and compatible argument types, create a match hypothesis. Relations match on predicate identity, not on the names of their arguments.
2. **Structural consistency.** Two hypotheses are compatible only if they keep one-to-one mapping (no source element to two target elements and vice versa) and parallel connectivity (if two relations match, their arguments must match).
3. **Merge into gmaps.** Grow maximal compatible sets of hypotheses.
4. **Score.** Reward matches that sit under matched higher-order relations (systematicity). Rough rule: a match inherits evidence from the match above it. Pick the best gmap, or keep a few. (This step and steps 1 to 3 are the standard SME description; the files here document step 5 in detail.)
5. **Candidate inferences.** For the chosen gmap: take every base statement that is (a) a descendant of a base root already matched, and (b) not itself matched. Substitute mapped entities. For unmapped base entities create a placeholder (skolem) entity. Drop a candidate if it is a permuted copy of a known target fact for a non-commutative predicate (a02, a04, a05).
6. **Output** the candidate list with a pointer to the supporting matched chain.

Pseudocode for step 5:

```
for root in base_roots_matched(gmap):
    for stmt in descendants(root):
        if stmt in gmap.matched: continue
        cand = substitute(stmt, gmap.entity_map, skolem_for_unmapped)
        if non_commutative(cand.pred) and permuted_copy_in_target(cand): continue
        out.append((cand, support=path(root, stmt)))
```

SME stops here. Everything below is what the research says has to be added.

### 4.2 Additions the research supports

**Ranking by attachment (Clement and Gentner; Markman).** Humans pick candidates whose antecedent matches the base. Score = length or depth of the matched causal chain under the candidate. Use it to order candidates for testing, not to accept them (a14, K23).

**One-to-one enforcement (Markman, K04).** Cheap code check: build the entity map implied by all accepted conjectures. Reject any conjecture that sends one source element to two targets or two sources to one target.

**Provenance tags (K05).** Tag each conjecture "copied from source" or "invented by model". Humans invent about as often as they copy. Test whether invented ones are less often true before trusting either class.

**Separate conjecture score from mapping score (K06).** Overall mapping similarity is a poor stand-in for trust in a single inference. A shared preventer in the target raises similarity (7.53 vs 6.35) and lowers the effect inference (74.4 vs 89.4). Implement: for each conjecture, ask a separate question, "does anything in the target block the link that justified this in the source?" That is Bartha's Potential for Generalisation.

**Bartha checklist (a11, K22).** For each conjecture write (1) the link: the named relation tying the shared source features to the projected feature (Prior Association); (2) a search for a target feature that breaks the link (critical disanalogy). Never tested on an agent; test first.

**Determination-rule view (a13).** If the agent can name the factors that determine the property and source and target agree on them, the inference is valid. Needs a justified rule; that is the same problem as before.

### 4.3 The check step must be executable

What the literature says about checking transferred content is summarised by K24.

- Model-written counterexample search is weak (REFUTE: under 9% for the best agent; 86% of its failed attempts are wrong brute-force code).
- Model-judged verification loses to extra sampling plus vote at equal compute until about 8x budget (d07).
- Same-model self-audit is conditional on task and model (d09).
- Execution against a validator removes validation errors (d06).
- A gate that verifies only some answers cut harmful flips from 2.2% to 1.0% but a longer first attempt matched its accuracy with 28% fewer tokens (d08).

So the O7 test must be code: run the conjecture on held-out cases, a simulator, a type or unit check, a checkable invariant. A model's "this seems consistent" is not a test (G5, G10).

### 4.4 Analogical prompting and Thought Propagation as procedures

- **Analogical prompting (a21).** Prompt: "Recall relevant problems and solutions, then solve." K=5 for GSM8K, K=3 for MATH and BIG-Bench. Output tokens rise. The accuracy of the self-written example matters, not relevance (d10).
- **Thought Propagation (c14-c16).** Propose analogous problems, solve each, aggregate into a plan for the input, optionally verify by running in the environment. One layer is enough. The best ALFWorld variant used real environment trials rather than a model judge. Other variants use model self-evaluation.
- **Case-memory agent (c23, d13).** Store past (task, trajectory, outcome). Retrieve by similarity, then re-rank by learned utility from outcomes. Similarity alone plateaus because it cannot filter functional distractors.

### 4.5 Why LLMs fail: current mechanistic picture

- Surface similarity wins when the relation is weakly encoded (d14). A noun-similar distractor draws as much alignment as the true target.
- Binding many entities at once is the limit (REL, d04): accuracy falls with relational complexity, not input size.
- Letter-string failure may be counting (a19) or structure transfer (a17, a18, a20). Not settled.
- Training on copy tasks first lets a small model learn letter-string analogy (d01). A training result, not a prompt fix.

## 5. What holds up

**Holds (two or more independent sources).**

- Humans prefer facts attached to a shared causal system when projecting (Clement and Gentner 1991, Markman 1997; Lassaline 1996 same rule in abstract). Sample sizes 32 to 78. Caveat below.
- Letter-string rule transfer in LLMs falls when the alphabet is changed, and humans do not lose much. Sources: Lewis and Mitchell, Hodel and West, Stevenson et al.; Hellwig et al. (2026) report some frontier models still struggle.
- Far-domain narrative analogy is below humans (ARN, StoryAnalogy, plus 2025-26 related tasks).
- Order, wording and distractor sensitivity in LLM analogy (several sources).
- Counterexample search and model verification are weak checks (REFUTE, compute-optimal verification, SEVRA, same-model audit).
- Source correctness matters more than source similarity (Qin, ARISE, MemRL).

**Fails or does not hold up.**

- Relevance as the active ingredient of analogical prompting: random correct examples match relevant ones on GPT-3.5 and GPT-4o-mini (d10). K13 contested.
- "GPT-3 matches students on letter strings" under permuted alphabets (Hodel and West; Lewis and Mitchell). Disputed by Webb et al. (a19, d21).
- Extra reasoning tokens as a cure on related tasks (3.4x tokens with o3-mini did not prevent collapse to 17%; 4k to 16k more thinking tokens added 0 to 3 points on REL).
- Toolkit as cure for structure binding (d05, not paired).
- Telling the model to attend to system mappings did not fix the near-distractor case in ARN (b22).
- Near-analogy demonstrations are harmful in places (b23, c09).

**Moderators.**

- Distance: near beats far (ARN 75.0 vs 39.6).
- Model size: self-generated sources help only strong models (b25, c12).
- Base visible or remembered: effect 1.63 vs 0 (visible) falls to 0.92 vs 0.13 (memory) in humans (b03).
- Chain valence in Markman Exp 3 vs 3a flipped; no explanation (b07).
- Preventer present or absent (Colhoun and Gentner).
- Prompt wording: about 20% to about 100% in one task (c06).
- Answer order: 1.0 vs 0.72 for GPT-4 stories (b20).
- Number of examples: GPT OSS models got worse with 2 or more examples; Gemini 2.5 Flash and Llama 3.3 70B improved (d01).

**Weak points of the human evidence (critique).**

- All of the direct candidate-inference evidence comes from two labs and one theory family. Short written passages, undergraduates, few items. Same-lab "replications" are not independent.
- Lee and Holyoak 2008, Lassaline 1996, Day and Gentner 2007, Holyoak, Lee, Lu 2010: abstracts only. Independence of Lassaline not checked.
- Markman's other-inference rate (.56) equals the shared-system rate (.52), so the "systematicity bias" shows up against nonshared base facts, not against all alternatives.

**Interventions that worked.**

- Recoding the problem as structured text: number naming 77.2% vs at most 51.8% (c17).
- Decomposition: about +20 on multi-component tasks; small models gain most.
- Retrieved verified analogous cases (ARISE): F1 43.27 to 75.37 for GPT-4o.
- Execution feedback removed validation errors in counterexample search (d06).
- Self-consistency (20 samples) against irrelevant context (d16).
- Thought Propagation with real environment trials (best ALFWorld variant).
- Code execution for letter strings (a19), if the counting account is right.
- Utility re-ranking of retrieved cases +3.8 points (d13).

**Interventions that did not.**

- Attention instruction for system mappings (ARN).
- Extra thinking tokens (d02, d04).
- Model-judged verification at equal compute (d07).
- Relevance-matching of self-generated examples (d10).
- One-shot ICL and token caps on REL: the relational-complexity trend stayed (d04).

## 6. Language models

All scores below are single-task zero-shot unless stated.

**Letter-string transfer (rule applied to a new target).**

- GPT-3 (2023, Webb): above students on standard alphabet (OR 1.76).
- Same task with changed alphabets (Lewis and Mitchell): humans .753, GPT-3 .488, GPT-3.5 .350, GPT-4 .452. Newer models are not better than GPT-3 overall. On the standard alphabet GPT accuracy was generally below human accuracy (unlike Webb).
- 2025 (Stevenson): GPT-4o .85 on Latin, .63 Greek, .48 symbol. Humans flat at about .89.
- With code (Webb 2024): GPT-4 near human on shuffled alphabets (60 problems per interval, hand scored). Interval-size effect not significant (P=.066).
- 2026 (Hellwig): frontier models (GPT 5.2, GPT 4.1, Claude Sonnet 4, Gemini 2.5 Flash, GPT OSS 120B, Llama 70B and 17B) still struggle on some transformations easy for humans. Per-model numbers are only in figures; the text gives none.

**Story and narrative analogy (identify the analogous case).**

- GPT-3: near above chance (p=.0039), far p=.065. GPT-4 preliminary: near perfect, far robust (no exact value).
- ARN: near 75.0 vs far 39.6 for the average model; GPT-4 mean 68.1.
- StoryAnalogy: ChatGPT about 30%, best about 48%, humans 85.7%.
- Order effect: GPT-4 1.0 first vs 0.72 second.
- No result for 2025-26 reasoning models on ARN or StoryAnalogy. This is the largest hole.

**Relational reasoning with distractors and noise (related tasks, 2025-26).**

- o3-mini 86.6 to 17.0; R1 80.6 to 23.2 on I-RAVEN-X with noise.
- A2RBench top 39.8 vs humans 68.5.
- Claude Opus 4.5 and Gemini 3 Pro at chance when relational complexity grows.

**Analogy as a prompting scheme.**

- Analogical prompting about +4% on average (2023 models). Qin et al. show the gain is not tied to relevance.
- Thought Propagation +12, +13, +15 in three domains (model self-evaluation in most variants).
- Analogy-then-solve gives novelty gains on Claude Sonnet 4.5, GPT-5.2 and Gemini 3 Flash (binary novelty 50.4 to 68.8% vs 21.6 to 37.9%), not correctness.

**What changed things, by how much.**

- Source quality: flipping labels cut F1 by about 16 points for GPT-4o (75.37 to 59.17) and went below baseline for Qwen3-8B.
- Encoding: number naming 77.2% vs at most 51.8% (about 25 points).
- Example count: mixed, model-dependent (d01).
- Tool: code for letter strings, near human (small sample).
- Scale: bigger helps on Raven-text via decomposition, but 2025 reasoning models still collapse under noise.

**Verification of transferred content.** No study measures false-conjecture rate before and after a verifier. Nearest: Yasunaga's audit (28 of 50 wrong answers had a good source and still failed), REFUTE (under 9% counterexamples), SEVRA (harmful flips 2.2 to 1.0%).

**LLMs and the human systematicity preference.** No study runs the Clement and Gentner design on LLMs. This is a clean gap.

**Unrequested transfer.** In code models, benign metaphor text steered algorithm choice in 23 to 35% of samples vs 3 to 10% for literal text (d15; adversarial search, so an upper bound).

## 7. What our agent should take

Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Evidence ids are claim ids (K) and evidence ids.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | A transferred conjecture is a surmise. O7 must end in an executable test (held-out cases, simulator, type or unit check, invariant), never in model judgement of the mapping. | O7, G3 | [E] | K01, K24; a01, a05, b10, d06-d09 |
| 2 | Do not use a model critic or counterexample-writer as the only check. Where a model-judged check is used at all, count harmful flips (right to wrong) as well as caught errors, and compare it to extra samples. | O7, G5 | [E] | K24; d06, d07, d08 |
| 3 | Grounding rule. Project only source facts connected to relations already mapped; tag and downweight ungrounded surface-similar facts. | O7 | [E] | K03; a02, a03, a07, b05, d20 |
| 4 | Rank candidate conjectures for testing by attachment to the mapped causal chain. Rank, do not accept: systematic mappings can still be false (Antarctica to Mars). | O7 | [E] for the human preference; the benefit to the agent is a test (T4) | K02, K23; a07-a09, b05-b07, a14 |
| 5 | Test every inferred rule on a mutated surface variant (shuffled alphabet, renamed symbols, reordered options) as well as the original. Report pass rate on both. | G3 | [E] | K09; a17, a18, a20, c05 |
| 6 | Randomise option order and paraphrase the mapping prompt; treat variance across variants as noise to be measured. | G3, G4 | [E] | K12; b20, b21, c06, c21 |
| 7 | Rationale text for accepting an analogy is not evidence. Accept on test pass only. | G10, G2 | [E] | K18; c10, a10, b04 |
| 8 | Far analogues are unreliable and run at impasse or in open mode only (the existing O7 note stands). Add: measure the near-decoy error rate, because surface-similar distractors are the main failure. | O7, G12 | [E] | K11, K25; a22, b22, c08, a23, d02-d04 |
| 9 | A source is only as good as its correctness. Prefer verified or outcome-checked sources over fluent ones; log source provenance and the outcome of using it. Similarity alone is not a ranking. | O7, memory | [E] | K26; d10, d12, d13 |

### Test first (single-source, contested or untested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 10 | One-to-one check in code: no source element mapped to two targets or reverse. | O7 | [S] | K04, b08 |
| 11 | Provenance tag (copied vs invented) and compare truth rates. | O7 | [S] | K05, b05, b06 |
| 12 | Score each conjecture separately from the whole mapping; look for a blocking target feature (Bartha). | O7, G3 | [S] | K06, K22, b11, b12, a11 |
| 13 | Keep the source verbatim in context while projecting, rather than a summary. | S2, context | [S] | K08, b03, a09 |
| 14 | Analogical prompting (self-written related problems) at equal tokens. Expect the gain to shrink or vanish. | O7, G4 | [C] | K13, a21, d10 |
| 15 | Retrieved verified sources vs self-generated sources, by model strength. | O7, memory | [S] | K14, K20, b25, c12, d13 |
| 16 | Test the transfer step itself: correct source plus wrong conjecture occurred in 28 of 50 failures. | O7 | [S] | K15, c13 |
| 17 | Thought Propagation with execution rather than a model judge. | O7, G2 | [S] | K16, c14-c16 |
| 18 | Re-represent source and target as structured relational text before mapping (naming attributes, decomposing by component). | S2 | [S] | K17, c17 |
| 19 | Far-analogy solved demonstrations for mixed near and far items. | O7 | [S] | K19, b23, c09 |
| 20 | Route index and counting steps in letter-string-like tasks to code. | G5, O7 | [C] | K10, a19, d05 |
| 21 | CoT vs direct answer vs rule-testing on mutated analogy items. | O7 | [S] | K21, c07 |
| 22 | Run O7 whenever a source schema or skill text is in context, even if no analogy was requested, and check for unrequested procedure import. | O7, S1 | [S] | K27, d15, d18 |
| 23 | Relation-level check against surface decoys. | O7, G3 | [S] | K28, d14, d16 |
| 24 | Analogy-first generation for open mode, scored by test not judge. | S3, O7 | [S] | K29, d11 |
| 25 | Two-step design (map, then a separate causal check), ablating the second step. The one-process vs two-process dispute is not decidable from text. | O7 | [C] | K07, b13, b14, d17 |

## 8. Concrete tests on our bench

All arms get equal total tokens, setup cost counted (G7). Report errors kept, right answers flipped to wrong, and tokens per state (SCHEMA.md section 6).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Conjecture check | Source case plus target with a checkable hidden fact (code behaviour, small simulator, rule table). 30-60 items, half with a planted true-looking but false conjecture. | (a) free transfer, (b) transfer then model-judged check, (c) transfer then executable test | False conjectures kept; true conjectures wrongly rejected; harmful flips | (c) beats (a) clearly; (b) near (a) and below extra samples. Matches K24. |
| T2 Decoy source | Target problem with two candidate sources: a surface-similar but structurally wrong one and a structurally right but surface-distant one | (a) model picks, (b) model picks then relation-only check (relation names, no entity names), (c) code ranks by shared mapped chain | Proportion of conjectures copied from the wrong source; final accuracy | (b) and (c) lower decoy error. Direction from d14, a22, b22; size unknown. |
| T3 Mutated transfer | Letter-string and digit-matrix rules on original vs shuffled or symbol alphabets, plus one new family (list ops, date arithmetic) | (a) model only, (b) model with code tool, (c) model with rule-testing loop | Accuracy original vs mutated; gap | Gap shrinks in (b) if the counting account is right. Gap persists if the structure account is right. Settles K10. |
| T4 Attachment ranking | Candidate conjectures from a source, with ground truth known; half grounded in a causal chain, half isolated | (a) random order testing, (b) testing ordered by chain attachment | Tests needed to find the true conjectures at a fixed test budget | (b) finds true ones sooner; check the correlation between structure score and truth (K23). |
| T5 Analogical prompting at equal tokens | Math and code items where plain CoT has 40-70% accuracy | (a) CoT, (b) analogical prompting, (c) best-of-N CoT at the same tokens, (d) random correct example | Accuracy | (b) not above (c) or (d). Follows d10. |
| T6 Source quality | Items with a labelled retrieved case bank | (a) no source, (b) self-generated source, (c) verified retrieved source, (d) retrieved source with one planted error | Accuracy | (c) > (b) > (a) for weaker models; (d) falls below (a) for some models (ARISE flip cost about 16 points for GPT-4o). |
| T7 Order and paraphrase variance | Any analogy-choice items | Single wording vs 5 paraphrases and both orders | Spread of accuracy across variants | Spread of 10+ points on some items. Use to set how many variants O7 needs. |
| T8 Verbatim vs summary source | Projection items with long sources | (a) full source, (b) summary of the same length cap | Conjecture accuracy | (a) higher, as in the human memory result (0.92 vs 1.63). |
| T9 Unrequested transfer | Task with a plausible wrong-domain procedure in context and no analogy request | (a) no check, (b) O7 check on procedure import | Rate of wrong-procedure import | Import in a minority of runs; check lowers it. Upper-bound rates from d15 were 23-35%. |
| T10 Systematicity preference in LLMs | Clement and Gentner passages; two plausible facts, one chain-attached | Model picks which fact to project; human data as reference | Share choosing the shared-system fact | Unknown. If under about 67% (human low) the model needs the rank rule in T4; if high, the rank is redundant. |

## 9. What does not transfer, and why

- **Human systematicity evidence is about preference, not accuracy.** The studies show what people choose, not that the choice is true. Antarctica to Mars is a counterexample. Use it as a ranking prior, not a verdict.
- **SME assumes a clean symbolic input.** Our agent works on natural language. The step of building typed statements (relations, higher-order relations) is where leakage and noise enter (a26 tailorability warning). Building that representation is itself a model call that can be wrong.
- **Written-passage experiments with undergraduates** (N 22 to 78, a few passages) do not carry to a model that reads long contexts. The only LLM evidence on this exact choice is missing.
- **Letter-string results are about one narrow task family.** They are used here as a test for rigid surface dependence, not as a model of the tasks our bench contains. Counting may explain part of them (a19).
- **Analogical prompting results are 2023 models.** The gain depends on the model writing correct examples; modern models may already do this implicitly. Qin et al. suggest relevance does not matter.
- **Novelty gains (d11) do not carry to correctness.** They are for open mode only, and G8 says novelty is judged by running.
- **Thought Propagation's gains rest on self-evaluation in most variants** (G5 forbids model-only judging).
- **Verifier studies (REFUTE, SEVRA, compute-optimal verification) are math, code and QA.** They bound what a model can check; they do not measure checks on analogical conjectures.
- **Case-memory results (Memento, MemRL, ARISE)** are agent and safety tasks with strong planners and tools; the analogical mapping step was not ablated.
- **Training results (Hellwig copy tasks)** cannot be used: we do not train.
- **Debate-style or multi-persona analogical voters** are ruled out by G4 and G9.
- **Links to other subfields in this run (not covered here):** analogical retrieval (MAC/FAC), candidate inferences, case-based reasoning, conceptual blending, transfer of learning, analogy in design, counterexample finding, retrieval and similarity, relevance-based fate of memories, computational blending, Bayesian and causal learning.

## 10. Open questions

1. Does a separate executable check on LLM-transferred conjectures lower the wrong-conjecture rate at equal tokens? No study measures it (K24 gives only neighbours).
2. Do current reasoning models still fail ARN-type far-domain, near-decoy analogy and mutated letter strings? Only related tasks have been re-run.
3. Does analogical prompting or Thought Propagation still beat plain CoT or best-of-N at equal tokens on 2025-26 models?
4. Do LLMs show the human systematicity preference when choosing which source fact to project? Would the rank rule improve accuracy?
5. What is the false-conjecture rate when a model copies from a surface-similar but structurally wrong source, and does a relation-only check remove it?
6. What do the paywalled and scanned papers actually report (Lee and Holyoak 2008, Day and Gentner 2007, Lassaline 1996, Holyoak, Lee, Lu 2010)? Cell values unread.
7. Is the letter-string failure counting or structure transfer? No larger paired with/without-code test on several mutated task families.
8. Do verified retrieved sources beat self-generated ones for strong models, with same-model equal-token control?
9. Do independent labs replicate systematicity-in-inference with larger or non-student samples?
10. Does keeping the source verbatim in context change conjecture accuracy in LLMs?
11. Are invented conjectures (not in the source) less often true than copied ones, for models and for humans?
12. One-process vs two-process account (Lee and Holyoak vs Colhoun and Gentner): only the second side was read in full.

## 11. Sources

[V] = opened and read this run (full text or enough to extract numbers). [M] = abstract, snippet or second-hand only. Ids refer to the evidence files.

**Structure mapping and models**
- [V] Falkenhainer, Forbus, Gentner (1989) The Structure-Mapping Engine: algorithm and examples. https://groups.psych.northwestern.edu/gentner/newpdfpapers/FalkenhainerForbusGentner89.pdf (a01-a06, a26)
- [V] Markman (1997) Constraints on analogical inference. https://web-archive.southampton.ac.uk/cogprints.org/628/1/markman.html (b05-b10)
- [V] Colhoun and Gentner (2009) Inference processes in causal analogies. https://groups.psych.northwestern.edu/gentner/papers/Colhoun_Gentner_SOFIA_042709.pdf (b11-b14)
- [M] Holyoak and Thagard (1989) ACME. Host refused; known only through a06.

**Human experiments**
- [V] Clement and Gentner (1991) Systematicity as a selection constraint in analogical mapping. https://groups.psych.northwestern.edu/gentner/papers/ClementGentner91.pdf (a07-a10, b01-b04)
- [M] Lee and Holyoak (2008) The role of causal models in analogical inference. https://doi.org/10.1037/a0012581 (b15, d17; abstract only)
- [M] Holyoak, Lee, Lu (2010) Analogical and category-based inference. https://doi.org/10.1037/a0020488 (d19; abstract only)
- [M] Lassaline (1996) Structural alignment in induction and similarity. https://doi.org/10.1037/0278-7393.22.3.754 (b16, d20; abstract only)
- [M] Day and Gentner (2007) Nonintentional analogical inference in text comprehension. https://doi.org/10.3758/BF03195940 and https://groups.psych.northwestern.edu/gentner/papers/DayGentner07.pdf (b27, d18; scanned PDF, abstract only)
- [M] Spellman and Holyoak (1996), via Markman (b09).

**Philosophy**
- [V] Bartha / Stanford Encyclopedia of Philosophy: Analogy and Analogical Reasoning. https://plato.stanford.edu/entries/reasoning-analogy/ (a11-a14)

**LLM analogy studies**
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (a15, a16, b17, b18, c01, c02)
- [V] Hodel and West (2024) Response: Emergent analogical reasoning in large language models. https://arxiv.org/abs/2308.16118 (a17, c05)
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning in LLMs. https://arxiv.org/abs/2402.08955 (a18, b19; c03 not used)
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks supports emergent analogical reasoning. https://arxiv.org/abs/2404.13070 (a19, c04; d21 abstract page only)
- [V] Lewis and Mitchell (2024) Evaluating the robustness of analogical reasoning in LLMs. https://arxiv.org/pdf/2411.14215 (b20)
- [V] Stevenson, Pafford, van der Maas, Mitchell (2025) Can LLMs generalize analogy solving like children can? https://arxiv.org/abs/2411.02348 (a20)
- [V] Musker, Duchnowski, Milliere, Pavlick (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803 (b21, c06, c07)
- [V] Sourati, Ilievski, Sommerauer, Jiang (2024) ARN: Analogical Reasoning on Narratives. https://arxiv.org/abs/2310.00996 (a22, b22, b23, c08-c10)
- [V] Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/abs/2310.12874 (a23, c20)
- [V] Bhavya, Xiong, Zhai (2022) Analogy generation by prompting LLMs. https://arxiv.org/abs/2210.04186 (a24, c21)
- [M] Sultan and Shahaf (2023) Life is a circus and we are the clowns. https://arxiv.org/abs/2210.12197 (a25; abstract and intro only)
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714 (a21, b24, b25, c11-c13)
- [V] Yu, He, Ying (2024) Thought Propagation. https://arxiv.org/abs/2310.03965 (c14-c16)
- [V] Hu, Storks, Lewis, Chai (2023) In-context analogical reasoning with pre-trained language models. https://arxiv.org/abs/2305.17626 (c17)
- [V] Ushio et al. (2022) BERT is to NLP what AlexNet is to CV. https://arxiv.org/abs/2105.04949 (c18)
- [M] Wijesiriwardene et al. (2023) ANALOGICAL benchmark. https://arxiv.org/abs/2305.05050 (b26, c19; abstract and skim)
- [V] Yuan et al. (2024) AnalogyKB. https://arxiv.org/abs/2305.05994 (c22)
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153 (c23)
- [M] Brown et al. (2020) Language models are few-shot learners. https://arxiv.org/abs/2005.14165 (c24; via Ushio)
- [M] Wu et al. (2023) Reasoning or reciting? https://arxiv.org/abs/2307.02477 (c25; via citations)

**2025-26 gap-search sources**
- [V] Hellwig, Zuidema, Stevenson, Lewis (2026) Transformer See, Transformer Do. https://arxiv.org/abs/2604.06501 (d01; per-model numbers only in figures)
- [V] Camposampiero et al. (2025) Can Large Reasoning Models do Analogical Reasoning under Perceptual Uncertainty? https://arxiv.org/abs/2503.11207 (d02)
- [V] Ma et al. (2026) A2RBench. https://arxiv.org/abs/2605.17278 (d03; per-model table cells not used)
- [V] Fesser et al. (2026) Evaluating Relational Reasoning in LLMs with REL. https://arxiv.org/abs/2604.12176 (d04, d05)
- [V] Sinha et al. (2025) Can Language Models Falsify? (REFUTE). https://arxiv.org/abs/2502.19414 (d06)
- [V] Singhi et al. (2025) When To Solve, When To Verify. https://arxiv.org/abs/2504.01005 (d07)
- [V] Dip, Zhou, Zhang (2026) Think Again or Think Longer? https://arxiv.org/abs/2606.19808 (d08)
- [M] Phalod (2026) When Should a Language Model Trust Itself? https://arxiv.org/abs/2605.02915 (d09; abstract and intro only)
- [V] Qin et al. (2025) Relevant or Random: Can LLMs Truly Perform Analogical Reasoning? https://arxiv.org/abs/2404.12728 (d10)
- [V] Shen, Druckmann, Zou (2026) Unlocking LLM Creativity in Science through Analogical Reasoning. https://arxiv.org/abs/2605.11258 (d11)
- [V] Zhang and Zhu (2026) Enhancing Agent Safety Judgment (ROME, ARISE). https://arxiv.org/abs/2605.03242 (d12)
- [V] Zhang, Wang et al. (2026) MemRL. https://arxiv.org/abs/2601.03192 (d13)
- [V] Lee et al. (2026) The Curious Case of Analogies. https://arxiv.org/abs/2511.20344 (d14)
- [V] Hu et al. (2026) Metaphor-Induced Algorithmic Steering. https://arxiv.org/abs/2607.28683 (d15)
- [V] Shi et al. (2023) Large Language Models Can Be Easily Distracted by Irrelevant Context. https://arxiv.org/abs/2302.00093 (d16)

*Cross-checker corrections applied: c03 not used (38.59% belongs to humans, not GPT-3.5); StoryAnalogy "about 30%" is ChatGPT only, best about 48%; Yasunaga's 15 vs 16 headline compares the best GPT-3.5 variant with plain GPT-4, not at equal tokens. SME numbers (6.99, 3.94, 2.44; O(N^2)), Colhoun and Gentner, Musker coefficients, Thought Propagation, Hu et al. and Memento were not re-checked by the cross-checker.*

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 10 established claims: 6 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A11.02-K02** (now single-source: the sources are not independent). Clement and Gentner 1991 numbers verified in the PDF (3 experiments); Markman 1997 full text was blocked (only a search summary of four studies seen), and Markman worked in the same structure-mapping tradition as Gentner, so 'two labs' overstates independence.
- **A11.02-K03** (reworded: the sources support less). The grounding rule (consistent with substitutions and structurally grounded; coffee-diameter example excluded) is verified in the SME paper, but no source shows that ungrounded surface-similar facts are the main error source. Corrected claim: SME's grounding rule: a base fact is carried over only if it is consistent with the mapping's substitutions and structurally grounded in the mapped relations; ungrounded facts, such as the coffee/ice-cube diameter comparison in the heat-flow example, are not projected as candidate inferences.
- **A11.02-K18** (reworded: the sources support less). ARN error analysis (right high-level message but wrong pick; keyword-driven) is confirmed, but neither Clement and Gentner nor ARN says human justifications are post hoc; C&G treat them as evidence of explicit awareness of causal structure. Corrected claim: GPT-4's written rationales in ARN often name the right high-level message while the choice is wrong, follow keywords, or fail to map the message back to the query narrative; a written rationale is therefore not evidence of a checked mapping.
- **A11.02-K26** (number corrected). In Zhang and Zhu Table (avg over seed + 3 challenge sets) Claude 3.7 Sonnet flipped is 77.04 vs ARISE 88.48 (and zero-shot 75.36), so flipping cuts all six models and the paper says performance 'consistently degrades'; the 'Claude exception' came from reading the Unsafe-only row (85.33) as flipped. Corrected claim: Source correctness gates transfer more than relevance does. Self-generated examples that are random but right can match or beat relevant ones on math (accuracy of the example is the key factor; GPT-3.5 and GPT-4o-mini), though on BBH relevant examples were best. Retrieving labelled analogous cases lifts F1 for all six models tested (GPT-4o 43.3 to 75.4), and flipping the labels of the retrieved cases cuts the result for all six (GPT-4o 59.2; Qwen3-8B 46.3, below its 50.5 zero-shot baseline; Claude 3.7 Sonnet 77.0 vs 88.5 standard). Similarity-only case retrieval plateaus; outcome-based utility re-ranking added 3.8 points on average over the strongest baseline (MemRL vs MemP).
