# Analogy and precedent in legal theory: deep document

*Subfield E11.07. Question: what makes a past case "like" this one? Key works: Levi (1949), Sunstein (1993). Sources: evidence_a-d.jsonl (ids a01-a25, b01-b25, c01-c28, d01-d17), claims.jsonl (K01-K28), critique.md. Evidence ids are cited in brackets. A source is "opened" only if the page or PDF text was read. Levi (1949), Sunstein (1993), Horty (2011), Ashley (1990), Alexander (1996) and Marchant et al. (1993) were not opened, so their content is second-hand.*

## 1. What it is

Legal reasoning by analogy means deciding a new case by comparing it with earlier decided cases. A court asks: is this case like that one in the ways that matter? If yes, it gives the same result. If no, it "distinguishes" the earlier case and may decide differently.

Three words need to be kept apart.

- **Precedent** is a constraint. In many systems a court must follow a prior decision even if it disagrees. [d06]
- **Analogy** is a method. The decider picks the most useful past case and argues that the new case is like it. Nothing forces the choice. [d06, K28]
- **Likeness** is the open question. Two cases are never alike in everything. Which similarities count? That is the subfield.

The core answer from legal theory is that likeness is not raw resemblance. It is resemblance relative to a rule, a reason or a set of relevant features. The court has to say which features matter and why. Every formal model in the field is an attempt to make that "which features matter" step explicit. [a01, a02, a05, a07]

Why it matters for our agent. The agent has operator O7 "Map an analogue" and a memory of solved items (S9). Both need a rule for what makes a stored item "like" a new problem. Law has 75 years of worked-out theory, and since 2025 a small set of tests of how language models do it. The most useful lessons:

1. Likeness is relative to a stated rule. Name the rule first.
2. Surface overlap is easy for models. Integrating relevance through a hierarchy is not. Code should do the second part.
3. Judges are moved by irrelevant sympathy when the precedent is weak. Models mostly are not. Selection of analogues is the step where outcome-driven bias enters.
4. Models cite relations between cases (overruled, followed) poorly. Verify such relations in code.

## 2. History and theories in depth

### 2.1 Levi (1949): reasoning by example

Edward Levi's *An Introduction to Legal Reasoning* is the founding account. [a01, not opened; read through Shapiro 1997 and Chorley and Bench-Capon 2003]

Three steps:
1. Find a similarity between the earlier case and the new one.
2. Announce the rule that the earlier case seems to stand for.
3. Apply that rule to the new case.

Two points set Levi apart from a simple "match the nearest case" view. First, the rule is not fixed in advance. It is read out of the earlier case by the court that cites it, and each new case can reshape it. Second, the court decides which similarities count. Later writers complain that Levi gives no test for which similarity counts. That gap drove everything after.

### 2.2 Hart: rules and precedent, and the no-vehicles example

Hart used a park rule "no vehicles" to show that a rule's meaning in new cases comes from examples applied by analogy. A longer rule text cannot settle bicycles, ambulances or toy cars in advance. [a25] Rules take content from cases; cases need rules to say which facts matter. [a04, Caputo 2026, a legal essay with no experiments]

### 2.3 Sunstein (1993): analogy as the core method, with low-level principles

Cass Sunstein's *On Analogical Reasoning* (Harvard Law Review 106:741) argues that analogy is the central mode of legal reasoning and needs no grand theory behind it. Features usually listed [a02, a03; full text not opened]:

- principled consistency (like cases treated alike),
- focus on particulars,
- incompletely theorised agreements (people with different deep theories agree on the result),
- low-level principles (a principle of middle height that covers the two cases),
- tentativeness (the principle stays revisable).

Cases A and B are alike if a low-level principle covers both. Shapiro (1997) reads the book as a Rawlsian "method of avoidance": settle cases with principles people of different deep views can accept. He doubts pluralism is the real cause of incomplete theorising. [a03] This is a reviewer's reading, not a test.

### 2.4 The skeptic and the separators

- **Alexander (1996), "Bad beginnings".** Analogy adds nothing beyond rules or principles. Seen only as a snippet. [b12] Schauer (1991) is named as an earlier critic.
- **Schauer.** Precedent and analogy are different kinds of constraint. Precedent binds even when the decider disagrees. Analogy is a free choice of the best analogue. Abstract only. [d06, K28]
- **Schauer and Spellman (2017).** Analogy begins with a perceived similarity, but that perception depends on the reasoner's knowledge, training and experience. Neither pure rule-making nor disguised lawmaking. [b10, abstract only]
- **Spellman and Schauer (2012).** Review chapter. No data that lawyers or judges are better general analogical reasoners. Their edge looks content-based. Legal categories are relational, and relations matter more than attributes in analogical retrieval. [b08, b09]

### 2.5 Formal models of precedential constraint

These make "likeness" exact enough to code.

**Factor and dimension models (HYPO, CATO).** Rissland and Ashley's HYPO (1987; Ashley 1990) represents a case as a set of factors, each pushing for the plaintiff or the defendant. It builds a three-step argument: cite the most on-point case (most shared factors), distinguish it (point to unshared factors), rebut. [a14, c25; not opened] Aleven's CATO (1994, 2003) adds a hierarchy that links 26 base-level factors to abstract legal issues. A difference can then be argued to be irrelevant to the issue ("downplaying") or important ("emphasizing"). [a12, a14, c26]

**Result model (Horty 2011).** A precedent binds if the new case is at least as strong for the same side as the precedent. Only the outcome and the factor sets matter. [a13, not opened; via Prakken]

**Reason model (Horty).** The court's stated reason, a rule with a priority, binds. Stricter about what a precedent says. [a13]

**Flat vs hierarchical result model (Prakken and van Woerkom 2025).** Flat: a case base forces outcome s on fact situation F if some precedent (G, s) exists where F has at least all of G's pro-s factors and at most G's con-s factors (Definition 2.1). Hierarchical: apply the same test recursively over intermediate factors (Definition 2.3). A factor hierarchy has exactly one maximal element, the decision. [a05]

The dispute is live. In their "MaxMonday" ice-cream example one ruling can be read two ways: "folded clothes beat inattentive in class" (flat, MMF) or "behaved at home beat misbehaved at school" (hierarchical, MMH). The reading changes which new cases are bound. The authors say it depends on whether the ruling recorded the intermediate factors. A dimension-based version answers Bench-Capon's criticism. Purely formal, no empirical test. [a06]

**Issues (Bench-Capon and Atkinson 2021).** Whole-case matching is wrong. Split cases into issues. Two stages: map facts to factors, then reason with factors. Three precedent types: framework (structure cases into issues), preference (resolve conflicts inside an issue), ascription (constrain the facts-to-factors mapping). IBP adds outcome prediction. [a07]

**Theory construction (Bench-Capon and Sartor; Chorley and Bench-Capon 2003).** Cases plus factors plus values give a theory. The tool emits Prolog with the rule priorities the theory needs, applied to Aleven's CATO trade-secret analysis. Open issues: CATO links several factors to one value; cumulative strength of factors. [a12]

### 2.6 Cognitive accounts of legal analogy

- **Structure mapping and MAC/FAC (Gentner, Forbus).** Retrieval is two stages: a cheap content-vector dot product, then structure mapping on up to three candidates. The mapping returns an alignment, candidate inferences and a score. Relations count more than attributes. [a11, b09]
- **Motivated analogical perception (Braman and Nelson 2007).** People call a source case analogous when its outcome fits their policy view. Strongest when cases are moderately similar. Two experiments (undergraduates; undergraduates plus law students). Legal training did not remove the bias (this last point is from a page summary, not verified). N and effect sizes not obtained. [b07, d05]
- **Knowledge and framing account (Spellman and Schauer; Schauer and Spellman).** Choice of analogy follows prior knowledge and how the question is framed, not only wanted outcomes. [b09, b10]
- **Expertise.** Marchant et al. (1993) on tax cases: experts and novices relied on the structurally matched analogue over the surface one once pragmatic concerns were held constant. Pragmatic goals override similarity. Sample sizes (Study 1: 63 students and 38 professionals; Study 2: 128 professionals and 146 students) come from a search summary only. A 1991 companion found facilitating treatments cut transfer for experts and raised it for novices. [b11, not opened]
- **Lehman, Lempert and Nisbett (1988)**, via Spellman and Schauer: first-year law students beat medical and graduate students on verbal reasoning. After three years the law gain was not significant while others improved more. [b08, secondary]
- **Standard biases in judges.** Anchoring and hindsight appear in judges (Guthrie, Rachlinski and Wistrich 2001), but in non-legal tasks. [b24, secondary]

## 3. Core findings with exact numbers

Status key: Est = established (two or more independent sources). Sing = single source. Cont = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| US federal judges follow defendant sympathy, not a weak precedent | N=32 judges, 2x2 between-subject, about 55 min each. Affirmance 87% (13/15) with unsympathetic defendant vs 41% (7/17) with sympathetic one; Boschloo p<.01. Precedent: 64% (9/14) vs 61% (11/18) | Spamann and Klohn 2016 [b01] | Cont |
| Legal experts mispredicted this | 102 law professors: 66 expected precedent to matter more, 13 expected the defendant effect to. Informative cell (19 obs): 75% vs 39%, p<0.11. Bayes factor 8.7 for defendant over precedent; posterior odds 13/89 x 8.7 = 1.27 | [b02] | Sing |
| Conflict did not slow judges significantly | About 2 minutes more on legal materials when trait and precedent conflicted; about 1 SD; not significant | [b03] | Sing |
| Chinese judges move with a strong precedent | N=48. Affirmance 86% (Sainovic) and 82% (Vasiljevic) vs 40% under the strongly favourable Besic precedent; Fisher p=0.020 (all three), 0.015 and 0.039 (pairwise). Defendant-trait gap 23 points | Liu, Klohn, Spamann [b04] | Cont |
| Judges use precedent in process, rarely cite it | Precedent 13% of time (2.93 min) vs statute 4% (0.81 min), p<1%; 68% consulted precedent first; only 29% mentioned it in reasons | [b05] | Sing |
| Citing a sister court's case shifts reading of a vague standard, not sentence length | Significant effect per abstract; N not read; law students moved about as much as judges | Chen and Li 2018 [b06] | Sing |
| Attitude-congruent outcomes make a source look more analogous | Two experiments; strongest at moderate similarity; no N or effect size | Braman and Nelson 2007 [b07, d05] | Cont |
| GPT-3 matches or beats students on digit matrices and letter strings, loses on story analogies | Digit matrices (human N=40): OR 1.88, p=0.005. Letter strings (N=57): OR 1.76, overall p=6.3e-5 (zero-generalisation p=0.0007). Story analogies (N=54): OR 0.37, p=0.0003; GPT-3 not above chance on far analogy p=0.065; 15 of 54 students picked the causal match every trial | Webb, Holyoak, Lu 2023 [a22] | Cont |
| Counterfactual variants break LLM analogy, not humans | Letter-string zero-generalisation pooled: humans 0.754, GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452. Digit matrices original vs alt-blank: humans 0.715 vs 0.771; GPT-3.5 0.813 vs 0.480; GPT-4 0.810 vs 0.477. Alternate-rule errors: 38.59% of GPT-3.5 errors, 22% GPT-4, 5.81% GPT-3 | Lewis and Mitchell 2024 [a23, d07] | Est |
| LLM distinction-finding: surface perfect, hierarchy weak | n=253 per task, 6 models. Task 1 100% all. Task 2 64.82% (gemini-flash) to 92.09% (gpt-5). Task 3 11.46% to 33.99% (gemini-pro 21.74, gpt-oss-120b 22.53, gpt-5 23.32, qwen3-thinking 33.99, qwen3 non-thinking 0.00) | Zhang, Grabmair, Gray, Ashley 2026 [a15, c01, d13] | Sing |
| Thinking mode helps Task 2 | Qwen3-235b thinking 78.66% vs non-thinking 30.04% (2.6x); Task 3 33.99% vs 0.00% | [a17, c02] | Sing |
| More tokens, not better | gpt-5 Task 2: 4,456 tokens when wrong vs 3,081 when right (+45%). gpt-5 per task about 487 (T1), 3,189 (T2), 7,025 (T3), 14.4x. Qwen3-thinking 9,596 tokens on T2 (3.0x gpt-5) at 78.66% vs 92.09% | [c03] | Sing |
| Abstention when no shared factor | N=30 per model, one prompt: GPT-4o 86.67%, Qwen-QWQ-32B 56.67%, Llama-4-Maverick 50.00%, R1-Distill-Llama-70B 23.33%, Llama-3-70B 3.33%, Llama-3-8B, Llama-4-Scout, GPT-4o-mini 0.00%. Hallucination accuracy Test 1: GPT-4o 99.64%, Llama-3-8B 92.39%, R1-Distill 91.38%; Test 3 84.91-99.16% | Zhang, Gray, Savelka, Ashley 2025 [c06, c07, d14] | Sing |
| Naming the overruled precedent | 236 US Supreme Court pairs. Task 1: Gemini-Pro 73.31% (173/236), GPT-5 71.19% (168/236), Gemini-Flash 33.47%, Qwen3 2.12%. Task 2 verify: GPT-5 75.42% (178/236) vs Gemini-Pro 42.37% (100/236, 131 "unknown"); GPT-5 said False in 55. Task 3 reversed control: GPT-5 100%, Gemini-Pro 100%, Qwen3 97.46%, Flash-Lite 91.95%, Flash 62.71% | Zhang, Savelka, Ashley 2025 [b15, c08, c09, d15] | Est (K11, with c14) |
| Era sensitivity | Task 1 earliest / middle / modern: GPT-5 35.29 / 53.85 / 82.47; Gemini-Pro 64.71 / 72.31 / 74.68; Gemini-Flash 17.65 / 24.62 / 38.96; Qwen3 0.00 / 1.54 / 2.60. Earliest cell about 17 cases; confounded with length and archaic language | [b16, c09] | Sing |
| Precedent treatment labels | 239 expert-annotated citations. Gemini 2.5 Flash 79.1% (high-level); GPT-5-mini 67.7% (fine). Largest class (156) F1 0.864; NEUTRAL (10) F1 0.400; 7 of 15 fine labels F1 0.000; over 19% of items have more than one valid label | Demir and Canbaz 2026 [b23, c14, c15] | Sing |
| Rule induction from 5-10 analogous cases | 5,121 case sets (38,088 Chinese cases) for tuning; 216 expert gold sets. Direct Mic-F1: Claude-3.7-Sonnet 66.67, Gemini-2.5-Flash 60.51, GPT-4o 55.50. Llama-3.2-3B 19.21 to 70.96 after LoRA; Ministral-8B+LoRA 73.18 (Mac-F1 70.73). CoT: GPT-4o precision 71.81 to 80.95 but explicit-rule recall 55.56 to 41.63. Explicit recall above implicit in every row read (e.g. 73.00 vs 37.77). More input cases lower precision, raise recall | Fan et al. 2025 [a19, b17, b18, c10-c13] | Sing |
| Structure mapping on 100 Illinois tort cases | 17 assault, 40 battery, 43 trespass. RRLG (rule learning) 47% P@1. PAPR strict 17% P@1, 46% P@6; partial 28% P@1, 72% P@6. ARPG strict 28% P@1, 35% P@6. Of 17 PAPR P@1 solves, 11 came from an ungeneralised outlier | Blass and Forbus 2023 [a08-a11] | Sing |
| Tax-law analogy near chance | SARA: 176 entailment samples become 15,400 analogy samples. GPT zero-shot 49-59%; 6-shot 49-56%; hand CoT 53-59%; best retrieval plus voting 57% (not significant); majority baseline 50%; one gpt-4-0613 cell about 68 +/- 3 | Zou et al. 2024 [a18, c20, c21] | Sing |
| Reasoning-based retrieval beats lexical | Recall@10 BM25 vs E5-large-v2: Bar Exam QA 5.03 vs 7.00. Structured legal-reasoning query expansion beats CoT by +3.09 (Bar) and +8.97 (Housing). COLIEE 2022 F2 0.8449 vs 0.8200 (+2.49) | Zheng et al. 2025; Nguyen et al. 2024 [c16, c17, c19] | Est (K10) |
| AALawyer analogical precedent retrieval | Versus DeepSeek-7B base: hallucination risk -37.6%, informativeness +41.9%, explainability +43.4%, mean +34.1%; symbolic retrieval precision 89.67%, recall 84.26% on 200 samples | Huang et al. 2026 [a20, b22] | Sing |
| Case grounding of subjective decisions | Humans +16.0 to +23.3 points in 4 of 5 groups (p 0.010-0.045); LLM +20.8 to +32.9 in 4 of 5 (p 0.004-0.011); AmItheAsshole +10.6, p=0.229 | Chen and Zhang 2025 [a21] | Sing |
| Deep-research agents write weak judicial reasoning | Over 60% invalid arguments, over 53% irrelevant citations. Citation relevance with most important fact deleted 2.07 vs 2.80 least important; opposite-side 2.42 vs 3.33 default (GPT-4o Deep Research) | Han et al. 2025 [b19, b20] | Est (K13, with c23) |
| LLM graders uneven | Spearman up to 75 and 81 for Claude grading; some graders zero or negative on retrieval-augmented outputs | [b21] | Sing |
| Law-school IRAC scores out of 56 | Claude 50.5 (90%), Copilot 46.4 (83%), GPT-3.5 43.0 (77%), Gemini 41.6 (74%), Lexis+ AI 40.9 (73%). Step-by-step helped on 1 of 3 statutory exercises | Peoples 2025 [c23, c24] | Sing |
| LLM as Spamann-Klohn judge | GPT-4o follows precedent, ignores sympathy. Press: GPT over 90%, students 85%, judges swayed 65%. Choice of law, 61 judges: GPT-5 and Gemini 3 Pro 100% law-following, Gemini 2.5 Pro 92%, o4-mini 79%, Maverick 75%, Scout 50%, GPT-4.1 50%, judges 52% | Posner and Saran 2025, 2026 [d01-d03] | Cont (press figures) |
| Self-generated analogues | GSM8K GPT-3.5: 0-shot CoT 75.8, 5-shot CoT 76.7, analogical 77.8. MATH: 33.9, 34.9, 37.3. Codeforces Acc@1: 9, 11, exemplars 13, knowledge+exemplars 15. Word sorting 67.6, 68.4, 75.2. Diverse vs non-diverse 77.8 vs 75.9 (GSM8K) and 37.3 vs 35.2 (MATH). K=1/3/5 GSM8K 76.1/77.5/77.8. With self-consistency 85.3/46.0 | Yasunaga et al. 2024 [d10, d11] | Sing |
| Transformers match cases, not rules, out of distribution | GPT-3.5 trained on 1-5 digit addition: over 95% at 12 digits with rules in input (RFFT), over 40 points above scratchpad. Llama-2-7B RFFT about 91.1% at 9 digits vs scratchpad under 40%. Untrained GPT-3.5 direct 46.2% at 15 digits | Hu et al. 2024 [d12] | Sing |
| LLMs induce factor lists | 173 drug-interdiction cases, 103 expert-annotated. Human-refined list moderate; LLM-refined weakest | Gray et al. 2024 [c22] | Sing |

## 4. Mechanisms and models

Each is written so an engineer could build it.

### 4.1 Levi loop (rule-relative likeness)

```
given target T, memory M of solved items
1. candidates = retrieve(T, M)               # cheap, wide (top 3 to 6)
2. for each candidate C:
     rule_C = model writes "the rule C stands for" in one sentence (conditions -> result)
3. for each rule_C:
     check rule_C on T: does every condition hold in T? (typed list of conditions; code compares)
     check rule_C on C itself and on 1 other solved item (consistency; held-out, G3)
4. keep candidates whose rule passes; apply; if none pass -> typed "no valid analogue" (see 4.5)
```

The model writes the rule. Code does the condition check. This is Levi's three steps with a check. Nobody has tested it against plain retrieval at equal tokens (gap 1 open). [a01, K01]

### 4.2 Flat result model as a check (code only)

Represent each case as: outcome side s, set of pro-s factors, set of con-s factors. A precedent (G, s) forces s on F if F's pro-s factors include all of G's pro-s factors and F's con-s factors are a subset of G's con-s factors. This is a subset test. [a05, Definition 2.1] Use it as the "is it at least as strong" gate once the facts are mapped to factors.

### 4.3 Hierarchical result model

Factors sit in a DAG under issues, with one top node (the decision). Apply the flat test at each intermediate node, using intermediate factors that are themselves established by lower factors. Differences between cases are significant only if they reach the top through the DAG. [a05, a07, a15]

Implementation: store the DAG as data. Write a function `significant_distinctions(T, P, dag)` that returns the set of unshared factors whose effect survives to the top. The Zhang benchmark is exactly this function. A symbolic solver gives ground truth, and models score 11-34% when asked to compute it in text. [a16, c01, d13] This is the strongest argument for G5 "code selects".

### 4.4 HYPO/CATO three-ply argument

Ply 1: cite the most on-point case (most shared factors). Ply 2: distinguish it (unshared factors that make it a weaker analogy) or note it can be downplayed through the hierarchy. Ply 3: cite a counterexample and rebut. [a14, a16] Distinction is a set difference. "Emphasizing a distinction" (Definition 10) needs the hierarchy.

Models wrote 3-ply arguments faithfully when an argument existed (99.64% hallucination accuracy for GPT-4o). They dropped available factors (GPT-4o recall over 85%, GPT-4o-mini about 42-50%) and failed to abstain. [c06, c07]

### 4.5 Typed no-analogue outcome

Compute shared relevant factors in code. If zero, return `NO_ANALOGUE(reason)` and route to plain solve. Do not ask the model to decide that. Abstention by instruction alone ranged 0% to 86.67% across eight models. [c07, d14]

This conflicts in letter with G6 (never abstain on first pass). It does not conflict in spirit: it is an analogue-level fallback to the plain attempt, not an answer-level abstention.

### 4.6 MAC/FAC retrieval

Two stages. MAC: dot product on content vectors, cheap, returns up to three. FAC: structure mapping on those three, returns alignment, candidate inferences and a score. Reject inferences that need unbound entities. [a11] Our S2/S9 memory could use a cheap embedding pass followed by a code-side structural comparison. It needs cases in structured form (predicate logic or typed slots).

### 4.7 Rule induction with verification (SILVER pattern)

Induce a rule from 5-10 analogous cases. Verify each rule against every case (it must apply to over half the set; explicit rules to 100%). Iterate. SILVER beat direct, CoT and long-CoT, at the highest token cost. [c10, c11, c13] More input cases raise recall and lower precision (overgeneralisation), so cap the set. [c12]

### 4.8 Blind selection

To test outcome-driven similarity, hide the outcomes of candidate analogues while selecting, then reveal them. Compare with outcome-visible selection. [K17] Not tested on models.

### 4.9 Relation verification in code

Store for each remembered item: id, date, relation links (superseded by, derived from). Never trust the model's claim that item A overrules or refines item B. Check the link. Models pass a reversed-direction control at 97-100% and fail the real task, so they use chronology as a shallow heuristic. [c09, b15]

## 5. What holds up

**Replicated or multi-source.**
- Likeness is rule-relative (K01). Levi, Sunstein, Hart, Bench-Capon and Atkinson, and Spellman and Schauer agree on the principle. None tested it on models. This is theory consensus, not experiment. [a01, a02, a07, a25, b09, b10]
- Counterfactual fragility of LLM analogy (K26). Lewis and Mitchell, Hodel and West, and Wu et al. agree that performance drops on altered stimuli while humans stay stable. [a23, a24, d07, d08, d09] Established for 2023-era models.
- Reasoning-aware retrieval beats lexical retrieval for legal material (K10). Four independent sources. [c16, c17, c19, a20, b22]
- LLMs are weak on relations between cases (K11). Zhang-Savelka-Ashley and Demir-Canbaz, different groups. [b15, c08, c09, b23, c14]
- Deep-research and chat agents write weak judicial reasoning (K13). CourtReasoner and Peoples. [b19, b20, c23]

**Mixed or contested.**
- Judges and precedent. No clean contradiction, but no common effect size. Spamann and Klohn: weak precedent null in the US (N=32). Liu et al.: strongly favourable precedent works in China (N=48); the two weak ones again did little (86% vs 82%). The authors say a weak precedent is easy to dismiss. [b01, b04, b25]
- Emergent analogy in GPT-3 (Webb) versus counterfactual failure (Lewis and Mitchell; Hodel and West). Same task, different stimuli. The dispute is about contamination. [a22-a24]
- Realist reading (outcome drives similarity) vs knowledge-and-framing reading. Not tested head to head. [b07, b09]
- Flat vs hierarchical result model. Formal dispute, no empirical test. [a05, a06, a07]
- Skeptic vs defenders on whether analogy adds anything. [b12, a02, d06]
- LLM judges. GPT-4o ignores sympathy like students, unlike judges (Posner and Saran), but the newer numbers are press reports. Katz and Zamir (2026) reportedly find that asking models to consider sympathy lowers formalism somewhat (search summary only, not opened). [d01-d04, d16, d17]

**Failures and null results.**
- Weak precedent had no effect on US judges. [b01]
- Tax-law analogy: GPT models near chance. Retrieval plus voting 57%, not significant. CoT often did not help. [a18, c21]
- Chain-of-thought on rule induction: precision up, recall down, no clear net gain (Gemini Mic-F1 +2.45, Claude -0.89). [b17, b18, c11]
- Legal training showed no general analogical-skill edge. Law students' gain after three years was not significant. [b08]
- Thinking longer did not help on integration. Task 3 stays 11-34%. [c01, c05]
- Prompts toward legal realism barely moved GPT-4o. [d01, d02]
- Better retrieval did not always help the answer. A gold passage lifted Llama 3 8B only about 20%. [c17]

**Moderators.**
- Strength of precedent: weak gives null, strong gives an effect. [b04, b25]
- Moderate similarity maximises motivated perception. [b07]
- Task type: precedent moves interpretation of vague standards, not sentence length. [b06]
- Set size: more cases, lower precision and higher recall. [c12]
- Model strength: Claude-3.7 and DeepSeek-V3 stay stable, GPT-4o-mini and Maverick degrade. [c12] Choice-of-law law-following climbs from 50% (Scout, GPT-4.1) to 100% (GPT-5). [d03]
- Age of the precedent: GPT-5 35.29% earliest vs 82.47% modern, confounded with length. [b16]
- Explicit vs implicit rules: explicit recalled far more. [b18]

**Interventions that worked.**
- Structured legal-reasoning query expansion (+3.09 to +8.97 Recall@10). [c17]
- Thinking mode on hierarchical roles (30.04% to 78.66%). [c02]
- Verify-each-rule pipeline (SILVER) over direct and CoT. [c11]
- Fine-tuning a small model on analogous-case rule induction (3B: 19.21 to 70.96). [c11]
- Analogical precedent retrieval plus symbolic constraint (hallucination risk -37.6%). [b22]
- Case grounding for subjective decisions (+16 to +33 points). [a21]
- Self-generated analogues (+1 to +3 points on math, +7 on word sorting). [d10]
- Rule-following fine-tuning (arithmetic, over 40 points). [d12]

**Interventions that did not work.**
- Step-by-step prompting for statutory analogy. [a18, c24]
- Long-CoT for rule recall. [b17]
- Realism prompts. [d01]
- More thinking tokens within a task (wrong answers were longer). [c03]
- LLM-refined factor lists (weakest). [c22]

**Weak spots in this evidence base.**
- One research group (Ashley, Savelka, Zhang) produced most legal-LLM results, so independent_sources is often 1. [critique]
- The founding human studies are small (N=32, N=48; 19 informative cells; p<0.11 on the key comparison). [b01, b02]
- Zhang 2026: one run per cell, temperature 0.3, no confidence intervals. Task 3 may partly test the CATO hierarchy convention. [c05, d13]
- Zhang abstention: one prompt, N=30 per model. [d14]
- Several numbers rest on press or page-summariser reads (d02, d03, d13-d15). Correction from d15: GPT-5 Task 2 is 75.42% (178/236). The 73.31% (173/236) figure is Gemini-Pro on Task 1.
- No study compares a scaffold against plain prompting at equal tokens.

## 6. Language models

**Surface overlap is solved. Integrated relevance is not.** On the CATO benchmark all six models score 100% on finding factual distinctions. On the argumentative role of each distinction they score 64.82% to 92.09%. On finding all significant distinctions they score 11.46% to 33.99%, most under 25%. [c01] Trace analysis shows models miss that a factor supports an issue through an intermediate concern, mark the wrong factor significant, and loop. [c04]

**Reasoning helps, then stops.** Qwen3 thinking 78.66% vs 30.04% non-thinking on Task 2; 33.99% vs 0.00% on Task 3. The authors conclude that math-and-logic reasoning training does not give hierarchical legal skill. [c02, c05] Tokens grow 14.4x from Task 1 to Task 3 for gpt-5, and gpt-5 spends 45% more tokens on wrong Task 2 answers. [c03] Difficulty may drive both. This supports G11 (think briefly; prefer several short attempts).

**Zero-shot analogy is fragile.** GPT-3 reached or beat students on digit matrices and letter strings. It lost on story analogies, the type closest to legal likeness. [a22] On counterfactual stimuli GPT-3.5 and GPT-4 fall from about 0.81 to about 0.48 on digit matrices while humans hold at 0.72-0.77. [d07] No reasoning-trained model has been run on that design (gap 10).

**Analogy prompts give small gains.** Self-generated exemplars: +1.1 (GSM8K) and +3.4 (MATH) over 5-shot CoT for GPT-3.5; Codeforces Acc@1 15 vs 11; word sorting 75.2 vs 68.4. Diverse beats non-diverse by 1.9 and 2.1 points. About 3 exemplars saturate. No token-matched arm. [d10, d11]

**Rules beat nearest cases out of distribution, but only when trained.** Plain transformers match cases. Putting the rule in context and training the model to recite it step by step gives over 95% at 12 digits. This is fine-tuning on arithmetic. [d12]

**Legal tasks with no exact test.** Statutory entailment recast as analogy: near chance. [a18] Rule induction: frontier models over-generalise and hallucinate; explicit rules are recalled more than implicit ones; CoT trades recall for precision; SILVER and tuning help. [c10, c11]

**Abstention is erratic.** On no-shared-factor items, abstention runs from 0% to 86.67% (one prompt, N=30 each). [c07, d14] In the overruling benchmark Gemini-Pro answered "unknown" on 131 of 236 verification items, and its headline accuracy fell to 42.37% because of that. [d15]

**Case relations are weak.** Naming the overruled case: best 73.31%. The reversed control is passed at 97-100%, so success is partly chronology. [c08, c09] Treatment labels: 79.1% coarse, 67.7% fine, 7 of 15 fine labels at F1 0.000. [c14] Older cases are recalled worse (GPT-5 35.29% earliest vs 82.47% modern). [b16]

**Judges versus models.** GPT-4o as the judge in the Spamann-Klohn setup follows precedent and ignores sympathy, as law students do and federal judges do not. [d01] On a choice-of-law task GPT-5 and Gemini 3 Pro applied the correct rule 100% of the time vs 52% for judges. Scout and GPT-4.1 managed only 50%. [d03] These are press figures and a rule-application task, not an analogy task. The formalism depends on the model.

**Agents writing legal reasoning.** Deep-research agents: invalid arguments in over 60% of outputs and irrelevant citations in over 53%. [b19] Removing the key fact lowers citation relevance (2.07 vs 2.80). [b20] LLM graders of this work are uneven. [b21]

**Retrieval.** Plain lexical retrieval misses analogy-driven relevance. Structured reasoning expansion, analogical precedent retrieval and term generation beat plain retrievers. [c16, c17, c19, a20]

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Treat likeness as relative to a named rule, not whole-item resemblance.** The typed mapping in O7 should state the rule or feature set that makes the analogue relevant. Part: O7. [E] (K01; a01, a02, a07, a05, b09, b10, a25, a12). The evidence is theory plus formal models. The "name the rule" step as a measured gain is untested, so adopt it as a description of the mapping, not as a promised gain.
2. **Code, not the model, does the factor comparison.** Subset checks, set differences and hierarchy propagation are exact. Models score 100% on the surface step and 11-34% on the integrative one. Part: G5, O7. [E] that HYPO/CATO moves can be coded (K03; a14, a16, c25, c26, a12). The benchmark numbers are [S] (K04).
3. **Verify claimed relations between remembered items in code.** Models pass reversed-direction controls and fail the real relation task (73%, 79%, F1 0 on 7 of 15 labels). Part: G10, memory. [E] (K11; b15, c08, c09, b23, c14, c15).
4. **Do not accept cited-analogue reasoning as evidence.** Invalid arguments over 60%, irrelevant citations over 53%. Part: G10. [E] (K13; b19, b20, c23). Judges cited what they used only 29% of the time, which is [S] (K16; b05).
5. **Retrieve analogues by more than surface overlap.** Key retrieval on the stated rule or structure, not only text similarity. Part: O7, S2, memory. [E] (K10; c16, c17, c19, a20, b22). Caveat: the evidence is on legal statute and case retrieval.
6. **Test every analogy step on a counterfactual variant.** LLM analogy drops sharply under relabelling while humans do not. Part: G7, G3. [E] (K26; d07, d08, d09, a23). Evidence is on 2023-era models. Recheck on current ones.

### Test first

| Item | Part | Status | Evidence ids |
|---|---|---|---|
| Rule-naming step: name the rule the analogue stands for, then check it on the target, vs plain retrieval | O7 | [S] | K01, K24, a01, d10 |
| Code-side hierarchy or typed lookup for relevance in place of in-text integration | G5, O7 | [S] | K04, c01, d13 |
| Typed `NO_ANALOGUE(reason)` fallback scored apart from errors | G6, S0 | [S] | K06, K27, c07, d14, d15 |
| Blind, outcome-hidden analogue selection | G4, O7 | [C] | K17, b07, b09, d05 |
| Cue-invariance test for analogue choice (sympathy-like cue, wording) | G4, S1 | [C] | K15, K23, b01, d01-d03 |
| Verify-each-rule induction (SILVER pattern) over CoT rule writing | O2, S4 | [S] | K07, c11, b17 |
| Several short analogue attempts over one long trace; log tokens vs correctness | G11 | [S] | K05, c03 |
| Retrieved solved items vs written rules at equal tokens for judgement-type tasks | memory | [S] | K19, a21, d12, d10 |
| Age of a memory item vs recall reliability (S9) | memory | [S] | K12, b16 |
| Domain-specific memory vs a generic analogy prompt, per problem class | memory | [S] | K18, b08, b10 |
| Several candidate analogues, then code selection on fresh inputs | O7, S7 | [S] | K20, a09 |
| Keep "follow a binding rule" and "choose an analogue" as separate operators | O7 | [S] | K28, d06 |
| Model proposes features, code or humans fix the feature list | S2 | [S] | K21, c22 |
| Model graders for analogy quality: avoid, use code or held-out checks | G8 | [S] | K14, b21 |

## 8. Concrete tests on our bench

All arms at equal total tokens (count generation and setup, per G7). Items have exact labels. Report accuracy with a 95% interval. Use at least 200 items per arm, or paired items.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Rule-naming | Analogy-style puzzles with exact labels (ARC-like mapping, BrainTeaser, word patterns with an earlier solved example) | A plain retrieval of solved analogue; B name the rule then check on target in code; C direct answer | Exact-match accuracy | B above A by about 2 to 4 points. Analogical prompting alone gave 1 to 3 points on math [d10] |
| T2 Code-side hierarchy | Synthetic factor items with a DAG (CATO-style, built from the Zhang task definitions) | A model integrates in text; B code propagates the hierarchy, model fills only the factor mapping; C thinking mode | Exact-set accuracy on significant distinctions | B far above A (Task 3 baseline 11-34%) |
| T3 Typed fallback | Mixed set: items with a valid analogue and items with none | A forced mapping; B typed NO_ANALOGUE then plain solve; C instruction-only abstention. Three prompt wordings each | Accuracy overall; abstention precision and recall; spread over wordings | B above A on no-analogue items; spread under 15 points |
| T4 Cue invariance | Weak-precedent analogue items with a legally irrelevant cue toggled | A plain; B scaffold; weak and strong model | Shift in answer rate between cue and no-cue | Small model shows a shift; scaffold reduces it |
| T5 Blind selection | Items whose candidate analogues carry outcomes that fit a stated view | A outcome-visible selection; B outcome-hidden selection then reveal | Rate of picking the outcome-congruent analogue; final accuracy | B lowers congruent bias; accuracy up or equal |
| T6 Verify-each-rule | Rule induction from 5-10 solved items with exact held-out labels | A direct; B CoT rule writing; C induce then verify each rule in code, iterate | Held-out accuracy of the induced rule; tokens | C above B at equal tokens |
| T7 Counterfactual variant | Same analogy items in standard and relabelled form | Plain model; scaffold; reasoning model | Accuracy drop from standard to relabelled | Scaffold drop smaller than plain drop |
| T8 Short vs long | Distinction-style items | A one long trace; B 3 short attempts plus code vote at the same total tokens | Accuracy; tokens vs correctness | B above A (G11) |
| T9 Memory age | S9 lessons from early and late batches applied to new items | Retrieve by recency; retrieve uniformly; verify lesson in code | Recall of the correct lesson by lesson age | If older lessons are recalled worse, add age-aware lookup |
| T10 Case memory vs written rule | Judgement-type items with labels | A retrieved solved items; B written rules; C both | Accuracy at equal tokens | A or C above B on judgement tasks |

## 9. What does not transfer, and why

- **Binding force of precedent.** Legal precedent binds because of institutional hierarchy. Our solved items bind nothing. The memory is advisory. [d06]
- **Sympathy and policy motives.** The realist finding is about human judges' motives. A model has no policy view, only training-data tendencies. The cue-invariance test checks for it, but the motive does not transfer. [b01, d01]
- **Common-law vs civil-law data.** Rule induction and AALawyer use Chinese criminal law linked to statutes. That is not common-law stare decisis. [a19, a20, c10]
- **The CATO hierarchy.** It is a domain model of US trade-secret law. We would build our own hierarchy per problem class. Task 3 scores partly reflect that convention. [c01, c05]
- **Citation practice.** Judges cite or omit cases for institutional reasons. Our agent should log what changed its answer, not what looks good. [b05]
- **Human-length reasoning.** Judges spent about 55 minutes. Our budget is tokens. [b01]
- **Subjective moderation tasks.** Case-grounding gains were on labelling Reddit comments, not on exact-answer problems. [a21]
- **Fine-tuning results.** RFFT and LoRA gains need training, which we do not do. [d12, c11]
- **Arithmetic rule-following.** Not analogy. It only shows the rule-versus-nearest-case contrast. [d12]
- **Old formal systems (HYPO, CATO, SME).** They need cases in structured form. We have free text unless code builds the structure. [a08, a11]

## 10. Open questions

1. Does "name the rule, then check on the target" beat plain retrieval at equal tokens on exact-label tasks? The closest result (analogical prompting) has no rule-naming arm and no token match. [gap 1]
2. Can code-side hierarchy lookup close the 11-34% gap on integrative relevance, and at what token cost? [gap 2]
3. What do models do with a typed fallback instead of forced abstention? Is the 0-87% spread stable across prompts? [gap 3]
4. Do LLM judges follow irrelevant cues when the precedent is weak and the model is small? Does blind selection help? Only press figures so far. Katz and Zamir and the SAGE rerun are unopened. [gap 4]
5. What are the exact N and effect size of Braman and Nelson (2007)? Is there any LLM test of outcome-driven similarity? [gap 5]
6. Is there an independent replication of Zhang 2026 and of SILVER by another group, on common-law data? [gap 6]
7. Do retrieved solved items beat written rules for LLMs at equal tokens outside moderation? [gap 7]
8. Is the era effect a general recency bias that would also hit our lesson memory? Neither Zhang paper dates its items. [gap 8]
9. What do the full texts of Levi and Sunstein add on features of analogy? This needs a full-text pass. [gap 9]
10. Do reasoning-trained models survive the Lewis-Mitchell counterfactual design in 2025-2026? No test found. [gap 10]
11. Is the Spamann-Klohn precedent null a weak-precedent effect or a general one? Two experiments, N=32 and N=48.
12. Does the flat or the hierarchical result model predict real court behaviour better? No empirical test.
13. Does legal training reduce motivated analogical perception? A page summary says no. Not verified.

## 11. Sources

[V] opened (page or PDF text read this session, some only as an abstract page, noted). [M] snippet, summary or second-hand only.

**Theory**
- [M] Levi (1949) An Introduction to Legal Reasoning. https://press.uchicago.edu/ucp/books/book/chicago/I/bo3640065.html (a01; read through secondary sources)
- [M] Sunstein (1993) On Analogical Reasoning, 106 Harv. L. Rev. 741. https://www.jstor.org/stable/1341816 (a02, c27)
- [V] Shapiro (1997) Fear of Theory, 64 U Chicago L Rev 389. https://openyls.law.yale.edu/server/api/core/bitstreams/053b2870-3815-4d24-abff-a7ef42e85a47/content (a03)
- [V] Caputo (2026) Alignment as Jurisprudence. https://arxiv.org/pdf/2605.08416 (a04, a25)
- [V] Prakken and van Woerkom (2025) Defending the Hierarchical Result Models of Precedential Constraint. https://arxiv.org/pdf/2512.13505 (a05, a06)
- [V] Bench-Capon and Atkinson (2021) Precedential Constraint: The Role of Issues. https://cgi.csc.liv.ac.uk/~katie/icail21b.pdf (a07)
- [V] Chorley and Bench-Capon (2003) Developing Legal Knowledge Based Systems Through Theory Construction. https://cgi.csc.liv.ac.uk/~tbc/publications/2alisonICAIL03.pdf (a12)
- [M] Horty (2011) Rules and reasons in the theory of precedent. https://www.umiacs.umd.edu/~horty/articles/2011-rulesreasons.pdf (a13)
- [M] Rissland and Ashley (1987); Ashley (1990); Aleven (2003) HYPO and CATO. https://doi.org/10.1016/S0004-3702(03)00080-8 and https://mitpress.mit.edu/9780262011624/ (a14, c25, c26)
- [M] Alexander (1996) Bad beginnings. https://core.ac.uk/download/151686058.pdf (b12)
- [V] Spellman and Schauer (2012) Legal reasoning. https://faculty.weber.edu/eamsel/Classes/Directed%20Readings%20(4830)/Legal%20Reasoning/Spellman%20&%20Schauer%20(2012).pdf (b08, b09, b24)
- [V, abstract only] Schauer and Spellman (2017) Analogy, expertise, and experience, 84 U Chi L Rev 249. https://chicagounbound.uchicago.edu/uclrev/vol84/iss1/12/ (b10)
- [V, abstract only] Schauer, Why precedent in law is not totally about analogy. https://www.hks.harvard.edu/publications/why-precedent-law-and-elsewhere-not-totally-or-even-substantially-about-analogy (d06)

**Human experiments**
- [V] Spamann and Klohn (2016) Justice is less blind. https://lawcat.berkeley.edu/record/1127566/files/fulltext.pdf (b01-b03, b25)
- [V] Liu, Klohn, Spamann, Precedent and Chinese judges. https://laweconcenter.law.harvard.edu/wp-content/uploads/2024/11/Spamann_997.pdf (b04, b05)
- [V, abstract only] Chen and Li (2018) Judicial diffusion in China. https://econpapers.repec.org/RePEc:bpj:rlecon:v:14:y:2018:i:3:p:27:n:6 (b06)
- [V, abstract only] Braman and Nelson (2007) AJPS 51(4). https://ideas.repec.org/a/wly/amposc/v51y2007i4p940-956.html (b07, d05)
- [M] Marchant et al. (1993) The use of analogy in legal argument. https://ideas.repec.org/a/eee/jobhdp/v55y1993i1p95-119.html (b11)

**LLM and AI studies**
- [V] Zhang, Grabmair, Gray, Ashley (2026) Thinking Longer, Not Always Smarter. https://arxiv.org/abs/2510.08710 and https://arxiv.org/html/2510.08710 (a15-a17, b13, b14, c01-c05, d13)
- [V] Zhang, Gray, Savelka, Ashley (2025) Measuring Faithfulness and Abstention. https://arxiv.org/abs/2506.00694 and https://arxiv.org/html/2506.00694 (c06, c07, d14)
- [V] Zhang, Savelka, Ashley (2025) Do LLMs truly understand when a precedent is overruled? https://arxiv.org/abs/2510.20941 and https://arxiv.org/html/2510.20941 (b15, b16, c08, c09, d15)
- [V] Fan et al. (2025) Legal Rule Induction. https://arxiv.org/abs/2505.14104 (a19, b17, b18, c10-c13)
- [V] Blass and Forbus (2023) ICAIL. https://doi.org/10.1145/3594536.3595121 (a08-a11)
- [V] Zou et al. (2024) Reasoning by analogy for tax-law entailment. https://arxiv.org/html/2401.06715v1 (a18, c20, c21)
- [V] Huang et al. (2026) AALawyer. https://aclanthology.org/2026.acl-long.633.pdf (a20, b22)
- [V] Chen and Zhang (2025) Case Law Grounding. https://arxiv.org/abs/2310.07019 (a21)
- [V] Han et al. (2025) CourtReasoner. https://aclanthology.org/2025.emnlp-main.1787.pdf (b19-b21)
- [V] Demir and Canbaz (2026) Validate Your Authority. https://arxiv.org/abs/2605.17691 (b23, c14, c15)
- [V] Zheng et al. (2025) Reasoning-Focused Legal Retrieval Benchmark. https://arxiv.org/abs/2505.03970 (c16-c18)
- [V] Nguyen et al. (2024) Implicit Concepts in Legal IR. https://arxiv.org/abs/2410.12154 (c19)
- [V] Gray et al. (2024) Using LLMs to Discover Legal Factors. https://arxiv.org/abs/2410.07504 (c22)
- [V] Peoples (2025) AI and Legal Analysis. https://arxiv.org/abs/2502.03487 (c23, c24)
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning. https://arxiv.org/pdf/2212.09196 (a22)
- [V] Lewis and Mitchell (2024) Counterfactual tasks. https://arxiv.org/abs/2402.08955 and https://arxiv.org/html/2411.14215 (a23, d07)
- [V, abstract only] Hodel and West (2024) Response. https://arxiv.org/abs/2308.16118 (a24, d08)
- [V, abstract only] Wu et al. (2024) Reasoning or Reciting? https://arxiv.org/abs/2307.02477 (d09)
- [V] Yasunaga et al. (2024) LLMs as Analogical Reasoners. https://arxiv.org/html/2310.01714v3 (d10, d11)
- [V] Hu et al. (2024) Case-Based or Rule-Based. https://arxiv.org/html/2402.17709v2 (d12)
- [V, abstract only] Posner and Saran (2025) Judge AI. https://chicagounbound.uchicago.edu/law_and_economics/1044 (d01)
- [V, press] Tech.co report. https://tech.co/news/study-ai-judges-influenced-by-legal-precedent-not-sympathy (d02)
- [V, press] The Register on Silicon Formalism. https://www.theregister.com/2026/02/15/gpt5_bests_human_judges_in/ (d03)
- [V, press] UChicago News. https://news.uchicago.edu/story/how-do-ai-judges-compare-human-ones-its-complicated-says-uchicago-scholar (d04)
- [M] Katz and Zamir (2026) vignette decisions. https://sites.biu.ac.il/en/ori-katz/page/9270 (d16)
- [M] SAGE 2026 LLM rerun of Spamann and Klohn. https://sage.cnpereading.com/doi/10.1177/2755323X261433614 (d17)

*Note on read depth.* Several [V] lines were read through a page summariser (d13-d15) or only as abstracts (b06, b07, b10, d01, d05, d06, d08, d09). The critique file lists the numbers re-opened from full PDF text: Spamann and Klohn, Liu et al., Zhang 2026, Webb, Lewis and Mitchell, Zhang-Savelka-Ashley, Zhang-Gray, Fan.
