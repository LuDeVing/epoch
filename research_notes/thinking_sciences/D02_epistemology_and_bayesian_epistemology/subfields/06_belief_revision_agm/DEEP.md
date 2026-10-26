# Belief revision (AGM): deep document

*Subfield D02.06. Built from evidence_a-d.jsonl (a01-a27, b01-b28, c01-c28, d01-d22), claims.jsonl (K01-K28) and critique.md in this folder. No new search was done for this document. Evidence ids are in brackets. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Belief revision is the study of how an agent should change what it believes when new information arrives. The classic theory is AGM (Alchourron, Gardenfors, Makinson, 1985). It treats a belief state as a set K of sentences closed under logical consequence. It defines three operations [a01].

- **Expansion**: add a sentence p to K, with no check for conflict.
- **Contraction**: remove p from K and also remove whatever would bring p back.
- **Revision**: add p and keep the set consistent. Revision is defined from contraction by the Levi identity: revise by p = contract by not-p, then expand by p [a02].

AGM is a normative theory. It lists rationality postulates. It does not say which belief to give up. That choice comes from an outside ordering, called epistemic entrenchment or a selection function [a03, c26]. This is the point that matters for us. Our Revise state (S5) must decide what to drop when a check contradicts the current answer. AGM tells us the shape of a good answer. It does not tell us the ordering. The ordering is an engineering choice, and the evidence on which ordering works is thin (section 5, section 10).

The field has three parts that matter here.

1. **Formal theory** (1985-2026): postulates, representation theorems, iterated revision, belief bases.
2. **Human data**: do people revise minimally? (No.)
3. **Language-model data** (2021-2026): do models revise when they should, and hold when they should? (Mostly no, in both directions, for different causes.)

Links to other subfields in this run (not covered here): Non-monotonic and default logic; Anomaly response; Reflective reasoning and second look; Bias and debiasing; Diagnosticity of evidence; Alternative-explanation controls.

## 2. History and theories in depth

### 2.1 Founding AGM (1985) and the postulates

Source for all of this section: the Stanford Encyclopedia entry by Hansson [a01-a08, b01-b04, opened]. The founding 1985 paper itself was not opened. This is a known weak spot (critique.md).

**Revision postulates.** Six basic: Closure, Success, Inclusion, Vacuity, Consistency, Extensionality. Two supplementary: Superexpansion and Subexpansion [a01, b01].

- *Success*: the new input is always accepted.
- *Inclusion*: revising adds nothing beyond K plus p. This is the minimal-change idea.
- *Vacuity*: if p is consistent with K, revision is just expansion. Nothing is dropped.

**Contraction postulates.** Six basic: Closure, Success, Inclusion, Vacuity, Extensionality, Recovery. Two supplementary: Conjunctive inclusion and Conjunctive overlap [a01].

**Recovery** says that contracting by p and then adding p back restores the old set. Three named counterexamples exist [a05, b02]. In Hansson's Cleopatra case you learn she had a child, give that up, then relearn it. You should not get back the belief that she had a child with Caesar. The fix is withdrawal operators that drop Recovery.

### 2.2 Epistemic entrenchment and the other equivalent constructions

Epistemic entrenchment (Gardenfors 1988; Gardenfors and Makinson 1988) is a preference order over beliefs. It decides what is dropped [a03, b03].

- Five postulates: Transitivity, Dominance, Conjunctiveness, Minimality, Maximality.
- Rule: q survives contraction by p if q is in K and p is strictly less entrenched than (p or q). Otherwise q goes. A tautology is never dropped.
- Entrenchment-based contraction coincides with transitively relational partial meet contraction.
- Grove (1988) gave a semantic version: a system of spheres around the current worlds. Revision by p takes the narrowest sphere that touches the p-worlds. The postulates hold if and only if the operator comes from a total preorder over worlds [a04].
- Georgatos showed that Gabbay-style nonmonotonic consequence relations reduce to "entrenchment relations", which ties revision to default reasoning [a13].

**What this means for an engineer.** All of these are the same idea in different clothes: a ranking over beliefs (or worlds) plus a rule "drop the lowest-ranked things that clash". The theorems say any operator that obeys the postulates has such a ranking. They do not say how to compute it.

### 2.3 Belief bases instead of closed sets

Hansson's belief bases revise a finite list of stated beliefs, not the closure [a06, b04]. {p, q} and {p, p iff q} have the same closure but revise differently when not-p arrives. Base postulates are Success, Inclusion, Relevance and Uniformity. **Relevance replaces Recovery**: only things that help produce the clash get removed. Kernel and partial-meet base contractions exist.

Agent-memory builders follow this. Park's Kumiho memory uses immutable versioned revisions, rejects Recovery on purpose, and proves basic postulates at belief-base level plus Relevance and Core-Retainment [a23, c09]. Chowdhury's plan-revision work also uses a base, not a closed set [c27]. This is claim K02, [E] for the design choice. It is not [E] that bases improve scores. No ablation exists.

### 2.4 Iterated revision: Darwiche and Pearl (1997)

AGM says nothing about what happens on the second revision. Darwiche and Pearl (DP) added four postulates (DP1-DP4, called C1-C4 elsewhere) [a07, b04, b05].

- C1: if the later input q implies the earlier p, revising by p then q equals revising by q. A more specific later input makes the earlier one redundant.
- C2: two contradictory inputs in a row: the later one prevails.
- C3: evidence entailed by later evidence is kept.
- C4: no input defeats itself.

The core idea [a07]: revising by p leaves the order among p-worlds and among not-p worlds unchanged. It only moves one block relative to the other.

Booth and Meyer (2006) [a09, b05] showed that C1-C4 rule out Boutilier's natural revision once the penultimate input must not be ignored. They defined **admissible revision** (C1-C4 plus one postulate, P). Within that class:

| Operator | Where it sits | Plain behaviour |
|---|---|---|
| Nayak lexicographic | least conservative admissible operator | every p-world becomes strictly more plausible than every not-p world. Latest evidence always wins over all earlier evidence |
| Restrained revision (Booth and Meyer) | most conservative admissible operator | moves as little as the postulates allow |
| Natural revision (Boutilier) | most conservative of all, but breaks DP | moves the single best p-world to the top |

Which operator to use is open [K03, E that the choice is open]. Two further theory results:

- Iterated revision is Turing complete, even with DP holding [a14]. So postulates do not bound the behaviour of a loop.
- Chopra, Ghose and Meyer argue that epistemic states (preference structures), not belief sets, are the right object for iteration [a12].

### 2.5 Critiques

- **Success and Vacuity** (Friedman and Halpern 2001) [a11, K04, contested]. A scientist who believes heavy objects fall faster drops a 5 kg book and a 500 mg novel and sees them land together. One observation need not force acceptance of "weight does not matter". Success and Vacuity were once called beyond controversy. They are under-specified about what the agent models. For an agent: a single noisy check should not always force acceptance.
- **Gardenfors impossibility** (1986, 1987) [a08, b04]: the Ramsey test for conditionals is incompatible with plausible revision postulates. Responses: drop the Ramsey test, or exclude conditionals from the belief set. This matters little for a scaffold.
- **Recovery** (above).
- **Logical omniscience.** AGM assumes closed sets. Real agents hold finite lists.
- **Hofweber et al. (2025)** argue coherence norms apply to some language models and not others, and define model credence from next-token probabilities [a20]. Conceptual only.

### 2.6 Computational and engineering lineage

- Doyle's truth maintenance (1979) and de Kleer's ATMS (1986) are the older engineering line. An ATMS can implement partial-meet revision by enumerating maximal consistent assumption sets [c26]. Almeida and Casals (2026) give a survey and roadmap from Doyle to AGM. They note AGM presupposes entrenchment or selection functions but says little on building them [c26].
- Aravanis (2026) recasts training of binary neural nets as iterated belief change. Full-meet change is too crude. Lexicographic revision and moderate contraction satisfy DP. Worked examples include an MNIST case where accuracy rises step by step to 100% [a10, c25]. Theory plus toy examples.
- Thielscher and Son (2026) generalise AGM and iterated postulates to multi-agent Kripke models. Theory only [c24].

### 2.7 Human belief revision

- **Elio and Pelletier (1997)** [d16, opened; b10 earlier was not]: five experiments, independent lab. Conditionals were abandoned more readily than ground facts in Experiments 1 to 3 (more so with story content than with symbols). In Experiments 4 and 5 none of four model-theoretic minimal-change definitions matched. Sample sizes were not in the abstract.
- **Walsh and Johnson-Laird (2009)** [b06-b08]. Told that a fact contradicts a pair of beliefs, people explain the clash by revising the general conditional.
  - Exp 1, N=20: 17 revised the generalisation more, 2 the opposite, 1 tie (binomial p<.01). The categorical fact was revised in 30% of explanations when the clash involved both generalisations, 15% (one of two) and 14% (single).
  - Exp 2, N=31: minimal change was violated on 84% of trials (Wilcoxon z=3.62). Asking for an explanation lowered rejection of the other inference, 23% vs 44%.
  - Exp 3, N=40: violations on 91% of trials (z=4.88). The second inference was rejected 51% vs accepted 15%. After a consistent fact only 1% rejected.
  - Exp 4, N=25: when the contradicted rule had many known exceptions (disablers), people kept the other rule's consequence 57% of the time, vs 21% when it had few. Mann-Whitney U=22.5, p<.01. This is the test that separates minimal change from an explanation account: ease of explaining moderates revision.
- **Frosch and Johnson-Laird (2006)** [b09]: causes and enablers are revised differently. After consistent information, enablers were kept 88% (switched to cause 12%); causes were kept 58% (switched 42%). After inconsistent information, enabler 43% kept vs 57% switched, not significant in the text.
- **Vasileiou, Rago, Martinez and Yeoh (2025)** [d17]: Prolific, Exp 1 N=62, Exp 2 N=60, Exp 3 N=60, nine scenarios. Non-minimal revisions 83.37%, 85.51% (91.36% on two-rule problems), 67.16%. Mean changes per problem 2.14, 2.87 and 3.81 where two were needed. Even after being shown a disabling condition, people still revised broadly.
- **Belief-R's human basis**: the Belief-R items follow Byrne's (1989) suppression experiments, using human majority choices as targets [a27].

### 2.8 Posterior view: Bayesian gold standard

Hase et al. (2024) frame model editing as belief revision and build a Wikidata-based testbed where an ideal Bayesian agent gives the correct updated beliefs. They say AGM-like theory handles only part of the problem [a18, b15]. Probabilistic coherence, not minimal change, is their standard. Singh's Nous memory is a Bayesian per-claim reliability approach for agent memory [a24, d01].

## 3. Core findings with exact numbers

Status key: [E] established (two or more independent sources), [S] single source, [C] contested. "Claim" ids are from claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| AGM says what a revision must satisfy, not which belief to drop; an ordering must come from outside | 6 basic revision + 2 supplementary postulates; 6 basic contraction postulates; 5 entrenchment postulates | Hansson SEP [a01-a03, b01, b03]; Almeida and Casals [c26]; K01 | [E] |
| Bases with Relevance replace closed sets and Recovery in practice | Kumiho: 49 scenarios, 7 postulates, 100% pass; Chowdhury and Park both use bases | [a05, a06, a23, c09, c27]; K02 | [E] (design); no score ablation |
| Iterated revision needs DP postulates; operator choice is open | C1-C4; lexicographic least conservative, restrained most conservative admissible | Booth and Meyer [a09, b05]; K03 | [E] (theory) |
| Success and Vacuity are contestable for uncertain input | thought experiment, no numbers | Friedman and Halpern [a11]; K04 | [C] |
| People do not revise minimally; drop the general conditional first | W&JL: 17/20 (p<.01); 84% and 91% violations; Vasileiou 83.37/85.51/67.16% non-minimal | [b06-b08, d16, d17]; K05 | [E] |
| Explanation drives the choice of what to drop | Exp 4: 57% vs 21% keep consequence, U=22.5, N=25 | Walsh and Johnson-Laird [b08]; K22 | [S] (one lab) |
| LLMs under-update on defeaters (Belief-R) | about 30 models; 1744 three-premise items (1074 update, 670 maintain); small/open models near 0% update; best large at most about 50% BREU | Wilie et al. [a15-a17, b11, c01]; K06 | [S] |
| Update/maintain trade-off by model | GPT-4 Turbo 19.65 / 82.69 / 51.17; Claude 3 Sonnet 9.40 / 88.66 / 49.03; Llama-3 70B 10.99 / 92.09 / 51.54; Mixtral 8x22B 35.38 / 36.57 / 35.98 (BU / BM / BREU, direct prompt) | [a16, b11, c02]; critique confirms | [S] |
| CoT and plan-and-solve do not fix revision | mean gain about 1 BREU point; Mixtral 8x22B and Command R +10 on BU; Claude-3 Sonnet and GPT-4 Turbo lost | [b12, c03]; K07 | [S] |
| Stale answers survive a premise edit (inertia) | Qwen3-1.7B 0.667 to 0.467, inertia 0.600 (n=30); Qwen3-4B 0.650 to 0.450, inertia 0.600 (n=20); Phi-4-mini 0.950 to 0.850, inertia 0.200 (n=20); Qwen3-4B 0.000 on ProofWriter support-removal | DeltaLogic [a21, b13, c04, c05]; also DERELAB, STALE, BeliefShift, ClawArena | [E] across benchmarks (K08); DeltaLogic alone is tiny |
| Defeasible reasoning bias: accept congruent, resist incongruent | GPT-5.1 BiasGap 0.935 (accuracy on weakening updates 3.5%, OR 891, CI 586-1498); 17 of 19 cells significant after Holm; anchoring GPT-5.1 0.433, Qwen3-32B 0.483 | DERELAB [c15, c16] | [S] (one benchmark; supports K08) |
| Models recognise staleness better than they act on it | GPT-5-mini labels weakening turns right 95.4%, entailment accuracy 20.3%; Llama-3.1-70B 85.1% vs 14.9%; STALE Qwen3.5-27B State Resolution 76.0% vs Policy Adaptation 39.0% | [c15, c10]; K09 | [E] |
| STALE overall | 400 scenarios, 1,200 queries; best Gemini-3.1-pro 55.2%; Qwen3.5-27B 31.3%; GPT-4o-mini 8.7%; Zep, A-mem, mem0, LightMem under 18%; premise resistance mostly under 5% | Chao et al. [c10] (abstract-level check) | [S] |
| Write-time adjudication lifts a weak backbone | GPT-4o-mini overall 8.7% to 68.0%; premise resistance 78.0% / 75.0%; policy adaptation only 32.0% / 43.0%; about $0.37 per instance | CUPMem in STALE [c11] | [S] |
| Self-revision without outside signal fails; with an oracle it helps | GPT-3.5 GSM8K 75.9 to 84.3; CSQA 75.8 to 89.7; HotpotQA 26.0 to 29.0; GPT-4 95.5 to 97.5, 82.0 to 85.5, 49.0 to 59.0; intrinsic GPT-3.5 GSM8K 74.7 | Huang et al. [b19]; Kamoi [b21]; K10 | [E] |
| At equal budget self-repair barely beats resampling | 10 initial + 1 repair each = 1.05x of pass@20; second setting 0.97x (GPT-4, APPS, 300 tasks) | Olausson et al. [d05] | [E] (with b19-b21) |
| Located error is what makes repair work | human feedback 52.6% vs GPT-4 own feedback 33.3% repair success (16 participants, 40 failing programs); inaccurate feedback GPT-4 32/80 vs human 7/80 | [d06] | [E] (K23) |
| True error location gives large gains | BIG-Bench Mistake (2,186 traces): gains +18.0 to +43.9 with true location; +5.2 to +21.6 with random location; losses on right traces 0 to -11.4 (true) and -6.7 to -15.9 (random); finding the mistake is poor, best 52.87 | Tyen et al. [b20] | [E] |
| Unit-test output is the main driver of code repair | TransCoder Codex 80.4 to 91.6 (test), 92.5 (test + explanation); GPT-4 77.3 to 88.8 and 90.4; MBPP GPT-4 72.8 to 80.6 and 80.4 | Self-Debugging [d07] | [E] |
| Model-made location hints can hurt | detection 56.7/81.5/10.1%; intrinsic correction 16.7/26.8/29.1%; with model hint 26.7/15.5/12.8% (DeepSeek, GPT-3.5, Claude-3-Haiku; 500 problems each) | Li [d08] | [S] (supports K23) |
| Locating the culprit in long traces is hard | Who&When exact step 48.9 to 52.7%; within 3 steps about 70%; 33-130 step trajectories 17.2% exact; premise links add 3 to 14 points (PARC, 607 chains) | DeFA [d09], PARC [d10] | [E] for the difficulty |
| Bare challenge flips answers | 10 LLMs, 7 tasks: flip 46%, mean accuracy drop 17%, seven models lose 10+ points | FlipFlop [b22]; also [b26, b27, c20]; K11 | [E] |
| Pressure and evidence updating share internals | unsupported yielding 17.1 to 73.6%; rational updating 53.7 to 64.1%; anti-pressure DPO yielding down 32.9 points but rational updating down 48.9 to 53.7; r=0.87 (four 2026 frontier models), 0.90 (open) | Ma et al. [d14]; Shapira et al. [d15]; K24 | [E] |
| Source label and stated reliability change adoption | Opus 5 vs Sonnet 5: user-claim adoption 21% vs 78%; source adoption 27% vs 98% | [d15] | [S] (one paper; part of K24) |
| Memory vs counter-evidence | GPT-4 about 80% memorisation ratio on popular items; Llama2-7B PopQA 33.3 vs 82.8 by order; ChatGPT keeps memory 30.0% at 1 of 3 sources vs 86.2% at 2 of 3 | Xie et al. [b18]; K12 | [E] |
| Weight edits do not propagate | downstream accuracy 0.97 to 0.01 where it should change; MAE downstream 0.34 to 0.59; edited fact 0.90 to 1.00 | Hase et al. [a19, b15]; Cohen et al. [b16]; Zhong et al. [b17]; K13 | [E] (toy 83M model for Hase) |
| In-context or external edits beat weight edits | in-context beats ROME by 10 (GPT-Neo) to 29 (LLaMA) points; MeLLo with GPT-3.5 over 1-4 edits: 52.1, 35.3, 31.8, 30.9 (CF); 91.1, 87.4, 86.2, 85.5 (MQuAKE-T) | [b16, b17] | [E] |
| Classify the revision once, propagate by code | CostBench 1,080 instances: per-node judge 0.44 of oracle savings; structured 1.00 (60/60), paraphrased 0.90 [0.86, 0.95] (140/150); keep-all reuses stale results on all 360 full-swap revisions; synthetic DAG per-node 0.28 / 0.00 / 0.04 vs structured 1.00 | Chowdhury [c06, c07]; K14 | [S] |
| Reset context to done-and-remaining | STT-Arena gpt-5 n=120: full history 0.11, restart 0.11, state kept with reset context 0.52; 41% fewer tool calls (n=12) | Chowdhury [c08]; K15 | [S] |
| Agents rarely revise on refutation | more than 25,000 runs, 8 domains: evidence ignored 68%; beliefs never updated 71%; refutation-driven revision 26%; base model 41.4% of variance, scaffold 1.5% | Ríos-García et al. [a22, b23]; K17 | [C] (abstract-level check) |
| Falsifying tests beat confirming tests | 12 LLMs, 100 games each: GPT-5.2-Chat 75%, GPT-OSS-120B 68%, best instruction-tuned 41%, others 33-35%, Qwen3.5-9B 21%, GPT-5-Nano 12%; confirmation bias odds ratio 0.016 | FalsifyBench [b24]; K18 | [S] |
| Removing belief update or reselection hurts an agent | MOIRA GPT-4.1-mini Beta return 30.6% to 23.4% (no update) and 2.8% (no reselection); GPT-5.4-mini 24.3% to 2.7% and 15.4% | [c23]; K19 | [S] |
| Showing a prior assessment anchors without improving | 4,580 snapshots: error up in 46.20%, down in 30.28%; AUROC 0.545 vs 0.541; evidence-first prompt cut shift 1.41 points, error +0.07; anti-anchoring prompt raised error 0.39; EVLU-2 kept 258 of 3,503 revisions and cut harmful fraction 13.51 points | Zeng and Zhang [c17, c18]; K20 | [E] with [c16] |
| A one-line provenance rule fixed stale-file following | 320 runs, 2 agents, 40 projects: 90.1% (649/720) followed the stale file, 4.2% the code; Claude Code named the conflict in 79 of 80 runs yet followed the file in 86.2%; after the sentence 91.4% matched the code, 160/160 passed tests vs 89.4% | Xu and Wu [d13]; K25 | [S] |
| Failed revision loops get stuck | 19 models, 27,360 trajectories, budget 8: output recurrence 78.7 to 90.2%; fixed point or cycle 57.6 to 79.5%; prior recurrence adjusted OR 0.047; history reset: next-step escape +42.2 / +49.2 points, final success only +10.8 / +5.0 | Jiang et al. [d11, d12]; K26 | [S] |
| Entrenchment signals compared (synthetic) | reliability-weighted 100, last-write-wins 67, frequency 46, LLM over raw memory 90; inverted confidence: weighted 0, last-write 42, frequency 50, append 17; provenance-capped poison success 0% at 1/3/10/50 poison vs 100% for last-write-wins | Singh Nous [d01, d02, a24]; K16, K27 | [S] |
| Memory benchmark scores are fragile | same outputs 59.97 (generous judge) vs 32.45 (token-F1); judge accepts up to 63% of wrong answers (secondhand); typed provenance tested on 24 hand-written cases | [d03, d04]; K28 | [S] |
| LLMs and AGM postulates directly | AGM-Bench: 2,400 scenarios, 7 models; Success and Consistency high; Inclusion and Preservation often broken; reasoning models better in one step, degrade faster over iterations. No per-postulate numbers | Jenkins [b14, d19]; K21 | [S] (abstract only) |
| Models handle another person's false belief better than their own | first-person false 54.4% vs true 92.1%; third-person false 80.7%; GPT-4 22.0% on first-person false confirmation | KaBLE [d18] | [S] |
| Update difficulty depends on the type of update | ClawArena: 337 rounds, 45 dynamic updates, 18 models; model spread 29 points, framework up to 24; hardest scenario under 30% for every configuration | [b25] | [S] |
| Every goal-intervention type lowers agent performance | InterventionBench: 2,250 instances, 12 agents, 9 intervention types; additions hardest | [d20] (abstract) | [S] |

## 4. Mechanisms and models

This section is written so that an engineer can build each part. The pieces map onto S5 (Revise) and the memory ledger.

### 4.1 The AGM core as code

State: a finite **base** B of claims. Each claim has an id, text, source type, a pointer to the check or output that produced it, and a list of claims it depends on.

- **Expand(B, p)**: append p. No check.
- **Contract(B, p)**: remove p, and remove the minimal set of other claims needed so p is no longer derivable. On a base, use the kernel idea. Find all minimal subsets of B that entail p. Remove at least one claim from each. The claim to remove from each subset is the lowest-ranked one by the entrenchment order. This is "incision" in kernel contraction [a06, b04].
- **Revise(B, p)**: Contract(B, not-p), then Expand(B, p). This is the Levi identity [a02].
- **Relevance** (Hansson): never remove a claim that played no part in producing the clash [a06]. In code: only the claims in the clash set (the kernel) are candidates.
- **Recovery**: do not implement. Keep removed claims in a log, flagged superseded, so re-adding is a new decision, not an automatic restore [a05, a23].

For an LLM agent no theorem prover is available. Practical substitution: a clash is declared by code when a check output contradicts a claim's prediction. The "kernel" is the set of claims the candidate answer was derived from (the dependency list). This is a pragmatic reading. It is not AGM-proper.

### 4.2 Entrenchment as a ranking in code

Entrenchment must be supplied. Evidence from the head-to-head [d01, d02, K27]:

- **Provenance first.** Trust = min(provenance of the channel, content signal). Executed output and tool output rank above the model's own statements. This held poison success at 0% against 1 to 50 injected observations. Last-write-wins went to 100% [d02].
- **Do not read trust from wording.** Reliability inferred from hedging scored 100 on realistic data and 0 when confidence was inverted. A confident poison earned reliability 0.96 vs 0.25 hedged [d01, d02, c12].
- **Cost.** Provenance capping blocked true corrections from low-tier sources (100% to 54%) and fails under laundering unless taint tracking is added [d02, K16].
- **Recency** (last-write-wins) scored 67 on realistic data, **frequency** 46 [d01].

Proposed ordering for S5 (tested nowhere as a whole, see UNKNOWNS): (1) came from executed output, (2) number of independent supports, (3) recency, with stated confidence only as a tie-breaker [K27 agent_test].

Singh's results are synthetic and single-author. Treat the ordering as a hypothesis.

### 4.3 Evidence gate (when to revise at all)

Three results define the gate.

- A bare challenge is not evidence. Flip rate 46%, accuracy drop 17% [b22].
- Self-critique without an external signal does not help [b19, b21, d05].
- Training or steering against pressure damages updating on real evidence (shared internals) [d14, d15].

So the gate lives in the scaffold. Rule: a held claim may change only if the challenge carries new executed or retrieved evidence. Code checks that the revision cites an output item (this is G2). A one-sentence prompt rule ("follow the code when it disagrees with the notes") reversed 90.1% stale-file following to 91.4% code-matching in tools-using agents [d13].

Noisy input is a boundary case (Friedman and Halpern [a11], K04). Option: accept only after a re-run confirms. Not tested.

### 4.4 Locating the faulty belief

The bottleneck is location, not rewriting [b20, d06, d07, d08].

- Code supplies the location when a test or stack trace names it. Unit-test output gave 80.4 to 91.6 (Codex) and 77.3 to 88.8 (GPT-4) [d07].
- Model self-diagnosis is weak and model-made hints can hurt (26.8 to 15.5, 29.1 to 12.8) [d08].
- In long traces exact blame is 17.2% [d09].
- Mechanism that helps: premise links. Giving the checker each step's premises raised step error identification by 3 to 14 points [d10]. Dependency graph over steps raised failure attribution by 4 to 10 points [d09].

Implementation: when a check fails, code marks the failing claim and all its dependents as suspect. The model only picks among suspects.

### 4.5 Propagation by code

Chowdhury's design [c06, c07, c27]. Treat the plan or reasoning chain as a DAG. When the input changes, classify the revision once by type (for example, full swap, partial change, no change). Then code applies a fixed rule per node: keep, patch or discard. Results: 1.00 of oracle savings (templated), 0.90 paraphrased, versus 0.44 for a model judging each node. Keep/discard-only with perfect labels recovers only 0.76, so "patch" matters. Theorem: no policy that sees only a node's local view can be both safe (no stale reuse) and cost-optimal [c07]. One author-built benchmark.

### 4.6 State rebuild instead of append

After a revision, rebuild the prompt from the ledger (what is done, what remains, current claims) and reset the context. Appending the whole history gave 0.11; rebuilding gave 0.52 (n=120) [c08]. Clearing history at a recurrent state raised next-step escape a lot but final success only a little (+10.8, +5.0) [d12]. In-context or external visible edits beat weight edits [b16, b17].

### 4.7 Write-time adjudication

Memory papers do the work at write time. CUPMem consolidates the state when a new fact arrives, searches for dependent slots, and blocks stale premises at read time. GPT-4o-mini went from 8.7% to 68.0% overall, but implicit policy adaptation stayed at 32% and 43% [c11]. Kumiho uses a Supersedes edge: retrieval excludes superseded revisions [c09]. TOKI shows four common conflict rules (last-writer-wins, evidence-weighted, await-confirmation, per-rule policy) each admit named write anomalies [c13].

### 4.8 Loop guard (iterated revision in practice)

DP theory says choose between lexicographic (latest always wins) and restrained (move minimally). Empirically, failed loops repeat: 78.7 to 90.2% of failed runs recur [d11]. A practical guard: log (claim id, failing check id). If the same pair appears twice, force a different candidate or reset. G-level overlap with S6 impasse triggers ("same error twice"). Whether lexicographic or restrained oscillates less in a free-running agent is untested.

### 4.9 Falsify before accepting

Models that test to falsify win; confirmers lose (odds ratio 0.016 for confirmation bias) [b24]. Hook: before accepting a leading candidate, run the one input that would break it. This is already S7 in the schema; the new part is making the same step part of S5.

## 5. What holds up

### 5.1 Replications and agreements

- **Human non-minimal revision**: three labs and 28 years. Elio and Pelletier 1997 [d16], Walsh and Johnson-Laird 2009 [b06-b08], Vasileiou et al. 2025 [d17]. All find conditionals dropped before ground facts and revision broader than minimal. [E].
- **Staleness and inertia in LLMs**: Belief-R, DeltaLogic, DERELAB, STALE, BeliefShift, ClawArena, Hase-style edits. Different authors, different tasks, same pattern [K08]. [E] for the pattern. No single number is stable across them.
- **Self-correction without an outside signal does not help**: Huang [b19], Kamoi's survey [b21], Olausson [d05], Li [d08], Zeng and Zhang for anchoring [c17]. Six sources. [E].
- **Real feedback and error location help**: Tyen [b20], Olausson human arm [d06], Self-Debugging [d07], Observability Gap [d21]. [E].
- **Pressure flips**: FlipFlop [b22], MEDLEY-BENCH [b26], Wang and Koch [b27], BeliefScope [c20]. [E].
- **Weight editing fails to propagate**: Hase [b15], RippleEdits [b16], MQuAKE [b17]. [E].

### 5.2 Failures, weak points and contested results

- **No outside replication** of Walsh and Johnson-Laird's explanation effect. Elio and Pelletier and Vasileiou did not test explanation as a cause. Vasileiou found that giving an explanation still led to broad revision [d17]. Explanation causality stays [S] [K22].
- **Belief-R** is the only large test of delta reasoning. Single source [K06]. Authors list its limits: logic-driven change only, new premises as trigger, no re-evaluation of old knowledge without new input [a27].
- **DeltaLogic** n=20 to 30 episodes, 0.6B to 4B models. Not usable as a ranking [critique].
- **AGM-Bench** is the only direct postulate test on LLMs. Abstract only; per-postulate numbers missing after two attempts [b14, d19].
- **Ríos-García et al.**: scaffold explains 1.5% of variance, base model 41.4%. This is contested for scaffold design: a variance share across many tasks does not show that a targeted scaffold cannot help. Chowdhury and Park show structure helping on their own benchmarks. These measure different things [critique, K17]. The PDF would not download; only the abstract was re-checked.
- **Memory-framework papers** (Park, Singh, Chowdhury, CUPMem, MOIRA, TOKI) use self-built benchmarks with self-reported scores. Several are single-author preprints. Park notes an independent reproduction by the benchmark authors at mid-80s% [c09]. LoCoMo judge scores can differ by 27.5 points with the judge [d03]. [K28].
- **Dependency propagation** has no outside replication. PARC and DeFA are related, not replications. Qian et al. audited 15 agent protocols and found none covering stale-state handling under all four conditions [d22].
- **Most LLM results** use 2024 and 2025 models and zero-shot prompts without tools. Frontier 2026 models appear in DERELAB, STALE, FalsifyBench, MEDLEY, Shapira, Xu and Wu [critique].

### 5.3 Moderators

- **Type of update.** Adding support is easy; defeaters and support removal are hard [c05, b25]. Qwen3-4B: 0.000 on ProofWriter support-removal vs Phi-4-mini 0.667.
- **Inference type.** Modus tollens is harder than modus ponens; mental-state effects harder than event effects [a17, b12].
- **Popularity of the fact.** Popular facts get defended more [b18]. ROME Logical Generalization: 53.8 on random facts vs 5.5 on popular facts [b16].
- **Order of evidence.** Llama2-7B 33.3 vs 82.8 by order [b18].
- **Source, attribution and distance.** Opus 5 vs Sonnet 5 [d15]; Sonnet 4.5 had probability exactly zero of moving toward an opposing view at distance 4 to 6 across 157 trials, while views shown as its own earlier judgments moved it more [b27].
- **Scale.** Not a fix for inertia in the 1.7B to 4B range [c05]. Belief-R: models over 6B exceed 75% on the basic step; revision does not follow [a15].
- **Control choice, decoding and response channel** change model rankings in BeliefScope [c20].
- **Distractor premise.** Lowers basic logic accuracy on the same items [b12, c02].

### 5.4 What worked and what did not

| Worked | Did not work |
|---|---|
| Oracle label or true error location [b19, b20] | Intrinsic self-correction [b19, d05] |
| Unit-test output [d07] | Model-made location hints (2 of 3 models worse) [d08] |
| Classify once, propagate by code [c06] | Per-node model judgement [c06, c07] |
| In-context or external memory for edits [b16, b17] | Weight editing (ROME, MEMIT) for implied facts [b15-b17] |
| Provenance-capped trust [d02] | Trust from wording or confidence [d01, d02] |
| One-sentence provenance rule in tool-using agents [d13] | Anti-anchoring prompts (reduce pull, error not lower) [c18] |
| Evidence-backed-only revision rule EVLU-2 [c18] | CoT and plan-and-solve for belief revision (about 1 point) [b12] |
| Context reset keeping state [c08] | Training against sycophancy (damages rational updating) [d14] |
| Write-time adjudication [c11] | Appending full failed history [c08, d12] |
| Fine-tuning on FlipFlop dialogues: effect 9.5% to 3.8% (Mistral-7B) [b22] | Reset history at the end of a loop (small final effect) [d12] |

Note the FlipFlop fine-tune is a training result and, by Ma et al. [d14], may cost updating on real evidence.

## 6. Language models

### 6.1 How they behave

Two failures coexist.

1. **Under-revision on evidence.** Belief-R update accuracy: small and open models near 0%, large models roughly 10 to 35% (Llama-3 70B 10.99, Claude-3 Sonnet 9.40, GPT-4 Turbo 19.65, Mixtral 8x22B 35.38) [a16]. DeltaLogic inertia 0.60 in 1.7B and 4B Qwen3 [c04]. DERELAB GPT-5.1 3.5% on weakening updates [c15]. STALE premise resistance mostly under 5% [c10]. BeliefShift: up to 42% of cross-session contradictions unresolved across seven model families (cited in TOKI) [c13]. Agents ignore evidence in 68% of 25,000 runs [b23].
2. **Over-revision under pressure.** FlipFlop 46% flips [b22]. Unsupported yielding 17.1 to 73.6% in four 3B to 8B models [d14]. MEDLEY adversarial shifts +11.6 and +7.3 points for two models, near zero for others [b26]. Irrelevant additions change some models' answers (Llama-3.1-8B intrudes on 36.2% of easy off-path turns) [c16].

The two are not opposite ends of one dial. Reducing one by training or steering damages the other (r=0.87 and 0.90) [d14, d15]. A model that is strong at maintaining is weak at updating and the reverse (GPT-4 Turbo 82.69 maintain vs 19.65 update; Mixtral 36.57 vs 35.38) [a16].

### 6.2 Recognise versus act

Models notice. GPT-5-mini labels weakening turns correctly 95.4% of the time and gets entailment right 20.3%. Claude Code names the conflict in 79 of 80 runs and follows the stale file in 86.2% [c15, d13]. Conflict mentions peak in the first 10% of a trajectory, then agents drop the conflict [c19]. This is the strongest argument for a forced write step after detection.

### 6.3 Memory and anchoring

- With memory plus counter-evidence, models favour memory; with only counter-evidence, they mostly accept it [b18].
- Showing the model its own earlier assessment shifts the next estimate by 9.50 points on average without improving AUROC (0.545 vs 0.541) [c17].
- Models handle third-person false beliefs (80.7%) far better than first-person (54.4%) [d18].

### 6.4 What changed behaviour, and by how much

| Intervention | Effect | Source |
|---|---|---|
| Oracle correctness label | +8.4 (GPT-3.5 GSM8K), +14 (CSQA), +10 (GPT-4 HotpotQA) | [b19] |
| True error location (backtracking) | +18.0 to +43.9 on wrong traces | [b20] |
| Unit-test feedback | +11.2 (Codex TransCoder), +11.5 (GPT-4) | [d07] |
| Test plus explanation over test alone | +0.9 and +1.6 (TransCoder); about 0.4 to 2.8 across settings | [d07], K22 |
| Human diagnosis over GPT-4 own feedback | 33.3% to 52.6% | [d06] |
| Classify once and propagate by code | 0.44 to 1.00 of oracle savings | [c06] |
| Context reset with state kept | 0.11 to 0.52 pass | [c08] |
| One-sentence "follow the code" rule | 4.2% to 91.4% code-matching | [d13] |
| Write-time adjudication (CUPMem) | 8.7% to 68.0% | [c11] |
| CoT or plan-and-solve | about +1 BREU point, sign differs by model | [b12] |
| Anti-pressure DPO | yielding -32.9 points, rational updating -48.9 to -53.7 | [d14] |
| Evidence-first prompt | prior pull -1.41 points, error +0.07 | [c18] |
| EVLU-2 keep-only-evidence-backed rule | harmful fraction -13.51 points, kept 258 of 3,503 revisions | [c18] |
| Humility prompt (GPT-5) | Escalate rises; details limited | [c19] |
| History reset at recurrent state | final success +10.8 and +5.0 | [d12] |
| Model choice vs framework (ClawArena) | 29-point vs up to 24-point range | [b25] |

Caveat: these come from different tasks and are not comparable on one scale.

## 7. What our agent should take

Tags: schema part (G/S/O/memory), status [E] [S] [C], evidence ids.

### Add now (established)

These are consistent with existing guardrails. G7 still applies: each part must win at equal tokens once built, but the evidence base for the rule itself is [E].

1. **G2 reinforced: the trigger for revision is a located, executed or retrieved output, never a bare challenge.** [E] [b19, b20, b21, d05, d06, d07, b22, d14, d15]. Practical form: S5 receives the failing output from code. A content-free "are you sure" inside a loop must not change the held answer (K11).
2. **S5: do not rely on the model to find the faulty claim from its own text.** Code locates the failing check; the model rewrites. Roll back the dependents of the flagged claim, not only the claim. [E] for "location is the limit and execution output supplies it" [K23: b20, d06, d07, d08, d09, d10]. The dependents rollback by code is [S] (K14); see Test first.
3. **S5: keep a base of stated claims with provenance, no closure, no Recovery.** [E] for the design choice [a05, a06, c27]. Keep removed claims in a log marked superseded.
4. **S5 and memory: keep the current accepted claims in a visible ledger re-read each step.** Do not rely on the model to carry an edit across steps. [E] [b15, b16, b17, a19]. (The weight-edit evidence is about weights. We have no weight edits, so the transfer is the lesson that implied facts do not follow by themselves.)
5. **S5: do not hard-code minimal change as the drop rule.** [E] for human data [d16, d17, b06]. This is a negative rule: human non-minimality tells us what people do, not what is best for an agent (section 9).
6. **G2/S5: do not show the model its own earlier assessment as a prior unless it is needed.** Prior assessments anchor the next judgement and do not improve it. [E] [c17, c18, c16]. Gate any revision on a stated evidence item.
7. **S5: do not treat longer thinking, chain of thought or plan-and-solve as a fix for revision.** [E in effect, single-source for Belief-R numbers] [b12, c03; with G11].
8. **S5: after detecting that a claim is stale, force an explicit write step.** Detection alone does not change the answer (95.4% vs 20.3%; 76.0% vs 39.0%). [E for the gap] [K09: c15, c10, c11, c19]. The write-step remedy itself is [S]; see Test first.

### Test first (single-source or contested)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Candidate-list Revise state ranked by provenance, against the one-sentence "executed output outranks notes and your own earlier statements" rule alone, at equal tokens | S5, G2 | [S] | K25, K27, d13, d01, d02 |
| T2 | Entrenchment order: executed output, then number of independent supports, then recency; confidence only as tie-break. Compare with confidence alone and recency alone | S5, G2, memory | [S] | K27, d01, d02 |
| T3 | Propagate by code through a dependency graph vs ask the model per claim | S5, memory | [S] | K14, c06, c07, d09, d10 |
| T4 | One-line failure explanation before choosing the claim to drop vs direct drop | S5 | [S] | K22, b08, d07 |
| T5 | Rebuild prompt from ledger after revision vs append | S5, memory | [S] | K15, c08, d12 |
| T6 | Loop guard: same (claim, check) pair twice forces a different candidate or reset; lexicographic vs restrained policy | S5, S6 | [S] / [E] only that the choice is open | K26, K03, d11, d12, a09 |
| T7 | Falsifying check on the leading candidate before accepting | S5, S7 | [S] | K18, b24 |
| T8 | Ablate the replace-failing-hypothesis step | S5 | [S] | K19, c23 |
| T9 | Accept a failing check only after a re-run confirms it | G2, S5 | [C] | K04, a11 |
| T10 | One gate that fixes both pressure-flipping and evidence-ignoring | G2, S5 | [E] for the coupling; remedy untested | K24, d14, d15, d13 |
| T11 | Scaffold effect on a planted refutation | S5, G2 | [C] | K17, a22 |
| T12 | Shuffled order of conflicting items in the revise prompt | S1, S5 | [E] for order effect; remedy untested | K12, b18 |

## 8. Concrete tests on our bench

All arms get equal total tokens (setup cost counted, G7). Report update and maintain accuracy separately, never only the mean (K06). Run at least 3 seeds. Item types below use ARC and BRAINTEASER style items from the HTSA bench plus small Belief-R style logic items.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1, T2) | ARC items where the first rule fits all given examples but fails a held-out check (planted defeater) | (a) plain re-prompt with the failing output; (b) re-prompt plus the one-line outranks rule; (c) full candidate list ranked by provenance | wrong-belief retentions; final accuracy; tokens | (b) beats (a) by a large margin on stale-note items (Xu and Wu: 4.2% to 91.4%); (c) over (b) is unknown, expect small |
| B2 (K11, K24) | Same items plus a content-free "are you sure" turn | always-hold; always-update; evidence gate | flips on correct answers; updates on planted defeaters | gate keeps both; others each lose one side (Ma et al.: -32.9 vs -48.9 to -53.7 trade) |
| B3 (T3) | Multi-step items where an early claim fails and later claims depend on it | model asks per claim vs code rolls back dependents | stale-claim reuse; final accuracy; tool calls | code propagation better; Chowdhury 0.44 vs 1.00 is an upper bound from one author-built benchmark |
| B4 (T4) | Items with a failing check | one-line explanation then choose vs direct choice | wrong-claim retentions | a few points at most when real test output is supplied (self-debug +0.4 to 2.8) |
| B5 (T5) | Three-round revise tasks | ledger rebuild vs append history | pass rate; tokens | rebuild better, magnitude unknown (0.52 vs 0.11 on a different task) |
| B6 (T6) | Tasks with repeated failing checks, 4+ rounds | unlimited retries; same-pair guard; lexicographic vs restrained candidate policy | repeats of same claim; oscillation count; final accuracy | guard cuts repeats; final gain small (d12: +5 to +11 points) |
| B7 (T7) | Rule-discovery items (Wason style) | confirm-first vs falsify-first check | success rate | falsify-first better (FalsifyBench 75% vs 33-41% across model classes) |
| B8 (T9) | Items with one noisy failing check | accept at once vs confirm by re-run | false revisions; true revisions delayed | fewer false revisions at a small token cost |
| B9 (K09) | Items with a stale claim the model can name | detect only vs detect plus forced dependents write | downstream correctness | closes part of the 95.4 vs 20.3 gap |
| B10 (K21) | Small private postulate check on our own Revise step | Inclusion and Preservation checks over 50 generated cases | violation rate | diagnostic only; no arm contest |
| B11 (T12) | Conflicting-item prompts | fixed order vs code-shuffled order, averaged | decision variance | variance drops; accuracy neutral |

## 9. What does not transfer, and why

- **Closed belief sets and logical omniscience.** An agent holds a finite list. Closure is not computed. Use a base (section 4.1).
- **Recovery.** Rejected on purpose by builders and counter-exampled [a05, b02, a23].
- **Success as always-accept.** Contested for noisy or uncertain input [a11].
- **Human non-minimality as a target.** People violate minimal change. That says what people do. W&JL's account (explanation drives the drop) was not tested on LLMs. Do not copy human behaviour as if it were best practice [critique].
- **Weight-edit literature.** ROME, MEMIT, MEND fix the edited fact but not its implications. Our agent does not edit weights. Only the lesson carries over [b15-b17].
- **Memory-benchmark gains.** LoCoMo rarely contains contradictions. Bayesian memory is inert there [d03]. Scores depend on the judge (59.97 vs 32.45).
- **Small-model results.** DeltaLogic's 0.6B to 4B models and Hase's 83M toy model do not predict frontier-model behaviour [critique].
- **Zero-shot no-tool results.** Belief-R and similar tests lack executable checks, the setting least like our agent. Our agent has code-supplied outputs (G2, G3). Expect the real update gap to be smaller when a check names the failure [d07, d13].
- **Synthetic provenance results.** Singh's 0% poison success is synthetic and single-author; laundering breaks it [d02].
- **Theory that postulates bound loops.** Iterated revision is Turing complete even under DP [a14]. Postulates do not prevent oscillation.
- **Pressure-resistance training.** Not available to us (no training) and, per Ma et al., damages updating [d14].

## 10. Open questions

From critique.md GAPS, updated with evidence_d (status after gap search):

1. Does a forced, evidence-gated, ranked Revise state beat plain re-prompting at equal tokens on planted-defeater tasks? Still open. Nearest is d13 (no equal-token arm).
2. Which entrenchment signal works on a free-running agent: executed-output provenance, stated confidence, recency, or number of dependents? Partly closed, synthetic only [d01, d02]. "Number of dependents" never tested.
3. AGM-Bench per-postulate numbers for frontier models. Still open [b14, d19].
4. Does explanation-first revision help LLMs, and does the human effect replicate outside one lab? Human side partly closed (rule-first, non-minimal pattern replicates); causal role of explanation still one lab; no LLM test [K22].
5. How accurate is error location from stack traces on ARC-style or coding tasks? Closed enough to act on for coding; ARC-style not measured [K23].
6. Is the pressure-versus-evidence asymmetry stable for 2026 frontier models with tools, and can one gate fix both ends? Partly closed: training does not; a prompt rule worked in tool-using agents [K24, K25]. A single gate tested on both ends is open.
7. Lexicographic versus restrained iterated revision in agent loops. Open; indirect evidence of fixed points [d11, d12].
8. Independent replication of dependency propagation. Open [d20, d22].
9. Break-even of revise versus restart-with-summary at equal tokens. Open [d05, d12].
10. Independent reproduction of Kumiho, CUPMem, MOIRA, TOKI numbers. Open [K28].
11. Does the Walsh and Johnson-Laird "ease of explanation" moderator (many vs few disablers) predict which belief an LLM drops?
12. Does a revise state that is helpful in a zero-shot logic task still help when executed checks already supply the location?

## 11. Sources

[V] = opened and read this session (by the research agents). [M] = snippet, abstract or secondary only. Notes follow the cross-check in critique.md.

**Theory**
- [V] Hansson (2022) Logic of Belief Revision, Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/logic-belief-revision/ [a01-a08, b01-b04]
- [V] Booth and Meyer (2006) Admissible and Restrained Revision, JAIR 26. https://arxiv.org/abs/1109.6344 ; https://jair.org/index.php/jair/article/view/10455 [a09, b05]
- [V] Friedman and Halpern (2001) Belief Revision: A Critique. https://arxiv.org/abs/cs/0103020 [a11]
- [V] Chopra, Ghose and Meyer (2002) Iterated revision and the axiom of recovery. https://arxiv.org/abs/cs/0207038 [a12]
- [V] Georgatos (2000) Entrenchment Relations. https://arxiv.org/abs/cs/0007040 [a13]
- [V] Sauerwald and Beierle (2022) Iterated Belief Change, Computationally. https://arxiv.org/abs/2202.08856 [a14]
- [V] Aravanis (2026) Machine Learning as Iterated Belief Change a la Darwiche and Pearl. https://arxiv.org/abs/2506.13157 [a10, c25]
- [V] Almeida and Casals (2026) From Doyle to AGM. https://arxiv.org/abs/2608.14567 [c26]
- [V] Thielscher and Son (2026) Belief Revision Postulates in Multi-Agent Systems. https://arxiv.org/abs/2605.02249 [c24]
- [V] Hofweber et al. (2025) Are Language Models Rational? https://arxiv.org/abs/2406.03442 [a20]
- [M] Alchourron, Gardenfors and Makinson (1985), Darwiche and Pearl (1997), Gardenfors (1988), Grove (1988), Levi: read only through the SEP entry and the papers above; the originals were not opened.

**Human studies**
- [V] Walsh and Johnson-Laird (2009) Changing your mind, Memory and Cognition 37. http://www.modeltheory.org/papers/2009changing-your-mind.pdf [b06-b08]
- [V] Frosch and Johnson-Laird (2006) The revision of beliefs about causes and enabling conditions. http://www.modeltheory.org/papers/2006beliefrevision.pdf [b09]
- [M] Elio and Pelletier (1997) Belief change as propositional update, Cognitive Science 21. https://doi.org/10.1207/s15516709cog2104_2 [b10 not read; d16 abstract-level, no sample sizes]
- [V] Vasileiou, Rago, Martinez and Yeoh (2025) How Do People Revise Inconsistent Beliefs? https://arxiv.org/abs/2506.09977 [d17]

**LLM belief revision and staleness**
- [V] Wilie et al. (2024) Belief-R, EMNLP. https://arxiv.org/abs/2406.19764 [a15-a17, a27, b11, b12, c01-c03]
- [V] Dhanda (2026) DeltaLogic. https://arxiv.org/abs/2604.02733 [a21, b13, c04, c05; over-flip and abstain cells for Phi-4-mini not re-verified]
- [M] Jenkins (2026) AGM-Bench, ICLR 2026 workshop. https://www.iclr.cc/virtual/2026/10017503 [b14, d19; abstract only]
- [V] Sadhu et al. (2026) DERELAB. https://arxiv.org/abs/2608.30413 [c15, c16; only BiasGap 0.935 re-derived]
- [M] Chao et al. (2026) STALE. https://arxiv.org/abs/2605.06527 [c10, c11; abstract only in cross-check]
- [M] Ríos-García et al. (2026) AI scientists produce results without reasoning scientifically. https://arxiv.org/abs/2604.18805 [a22, b23; abstract only in cross-check; the author list in a22 was wrong]
- [V] Myakala et al. (2026) BeliefShift. https://arxiv.org/abs/2603.23848 [c14; table cells unreadable]
- [V] Ji et al. (2026) ClawArena. https://arxiv.org/abs/2604.04202 [b25]
- [V] Abtahi et al. (2026) MEDLEY-BENCH. https://arxiv.org/abs/2604.16009 [a25, b26, c21]
- [M] Guo and Cui (2026) BeliefScope. https://arxiv.org/abs/2610.11305 [c20; per-model effects not checked]
- [M] Wang and Koch (2026) Beyond sycophancy. https://arxiv.org/abs/2607.21558 [b27; first page only]
- [V] Zeng and Zhang (2026) Unreliable updating of clinical judgment. https://arxiv.org/abs/2610.02684 [c17, c18]
- [V] Sun et al. (2026) Accurate but Not Humble. https://arxiv.org/abs/2610.12360 [c19]
- [V] Xie et al. (2024) Adaptive chameleon or stubborn sloth. https://arxiv.org/abs/2305.13300 [b18]
- [V] Suzgun et al. (2024) KaBLE. https://arxiv.org/abs/2410.21195 [d18]
- [V] Bertolazzi et al. (2026) FalsifyBench. https://arxiv.org/abs/2606.04751 [b24; a26 was abstract only]
- [V] Ma et al. (2026) Sycophancy Suppression Can Impair Rational Updating. https://arxiv.org/abs/2608.26511 [d14]
- [V] Shapira, Cheng and Orgad (2026) Is Sycophancy a Form of In-Context Updating? https://arxiv.org/abs/2610.28325 [d15]
- [V] Laban et al. (2024) FlipFlop. https://arxiv.org/abs/2311.08596 [b22]

**Self-correction, error location**
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 [b19]
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516 [b20]
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 [b21]
- [V] Olausson et al. (2023/2024) Is Self-Repair a Silver Bullet? https://arxiv.org/abs/2306.09896 [d05, d06]
- [V] Chen et al. (2023) Teaching LLMs to Self-Debug. https://arxiv.org/abs/2304.05128 [d07]
- [V] Li (2026) Decomposing LLM Self-Correction. https://arxiv.org/abs/2601.00828 [d08]
- [V] Deng et al. (2026) DeFA. https://arxiv.org/abs/2610.01256 [d09]
- [V] Mukherjee et al. (2025) Premise-Augmented Reasoning Chains. https://arxiv.org/abs/2502.02362 [d10]
- [V] Wang and Wang (2026) The Observability Gap. https://arxiv.org/abs/2603.26942 [d21]

**Model editing**
- [V] Hase et al. (2024) Fundamental Problems With Model Editing. https://arxiv.org/abs/2406.19354 [a18, a19, b15]
- [V] Cohen et al. (2023) RippleEdits. https://arxiv.org/abs/2307.12976 [b16]
- [V] Zhong et al. (2023) MQuAKE. https://arxiv.org/abs/2305.14795 [b17; table text partly garbled]
- [V] Hase et al. (2021) Do Language Models Have Beliefs? https://arxiv.org/abs/2111.13654 [c22]

**Agent memory and revision**
- [V] Park (2026) Kumiho. https://arxiv.org/abs/2603.17244 [a23, c09]
- [V] Singh (2026) Nous. https://arxiv.org/abs/2606.22030 [a24, b28, c12, d01-d03]
- [V] Chowdhury (2026) Commitment Hierarchies. https://arxiv.org/abs/2609.37453 [c06-c08, c27]
- [V] Wang (2026) TOKI. https://arxiv.org/abs/2606.06240 [c13]
- [V] Giannouris et al. (2026) MOIRA. https://arxiv.org/abs/2605.01954 [c23]
- [V] He and Yu (2026) Stored Is Not Supported. https://arxiv.org/abs/2609.02127 [d04]
- [V] Xu and Wu (2026) Stale Instruction Files Override the Code. https://arxiv.org/abs/2610.30571 [d13]
- [V] Jiang et al. (2026) Exact Feedback Is Not Control. https://arxiv.org/abs/2609.28150 [d11, d12]
- [M] Lee et al. (2026) InterventionBench. https://aclanthology.org/2026.findings-emnlp.698/ [d20; abstract only]
- [V] Qian et al. (2026) Toward User-Conditioned Evaluation of Personal LLM Agents. https://arxiv.org/abs/2607.21635 [d22]

Not independent evidence: c28 (an editorial roll-up) was dropped. Duplicates in the evidence files were merged: Belief-R (a15/a16/a17/a27/b11/b12/c01/c02/c03), DeltaLogic (a21/b13/c04/c05), Hase editing (a18/a19/b15), MEDLEY (a25/b26/c21), Singh (a24/b28/c12), Ríos-García (a22/b23), Park (a23/c09). Ids 2606.22030, 2607.21558 and 2610.* were not all re-resolved in the cross-check.
