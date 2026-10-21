# Wason selection task and hypothesis testing: deep document

*Subfield 02 of A01 (cognitive psychology of thinking and reasoning). Written from evidence_a-d.jsonl (ids a01-a30, b01-b35, c01-c25, d01-d21), claims.jsonl (K01-K25) and critique.md. No new searching. Schema refs are to SINGLE_AGENT SCHEMA.md v0.2 (G1-G12, S0-S9, O1-O8, section 4b, memory).*

Status marks: **[E]** established (two or more independent sources), **[S]** single source, **[C]** contested. Evidence ids in brackets. Source marks in section 11: **[V]** opened this research, **[M]** snippet or second-hand only.

---

## 1. What it is

This subfield asks how a thinker picks tests for a hypothesis, and why people pick tests that cannot show the hypothesis is wrong. It has two classic tasks. In Wason's 1960 **2-4-6 task** the person sees the triple 2, 4, 6, proposes their own triples, hears yes or no from an oracle, and must name the hidden rule (true rule: any ascending triple). In Wason's 1966 **selection task** the person sees four cards (p, not-p, q, not-q) and a rule "if p then q", and picks the cards to turn over to check the rule (correct: p and not-q). People mostly pick tests that fit their current idea. Under 10 percent give the logical answer on the abstract selection task. The field then split on why: a wish to confirm (Wason), a heuristic called the positive test strategy (Klayman and Ha), a rational search for information (Oaksford and Chater), content and social-contract effects (Cosmides, Cheng and Holyoak), relevance (Sperber), or task misreading and matching bias (Evans, Stahl). Since 2024 the same tasks are used to test language models. For our agent the question is narrow and practical: how does code make the agent pick the test that can actually separate two live rules?

---

## 2. History and theories in depth

**2.1 Wason 1960: the 2-4-6 task** [a01, a02, a03]. 29 psychology undergraduates, tested alone, 45 minute cap. The true rule was "any three numbers in increasing order". The universe of triples is infinite, and many obvious narrower rules fit 2-4-6 (increase by 2, even numbers, multiples of the first). Subjects tested triples that fit their own narrower rule, always got yes, and announced wrong rules. Results: 6 found the rule with no wrong announcement, 13 had one wrong rule first, 9 had two or more, 1 never announced. Told a rule was wrong, subjects kept the same rule in over half of cases and reworded it (3 subjects repeated one rule in new words, 3 reworded right after a no). Wason's claim: people use "enumerative induction" and fail to eliminate hypotheses. Wason also noted that earlier concept tasks (Bruner et al.) used finite stimulus sets, which hid the problem. He linked the rewording to poor insight into one's own thinking.

**2.2 Wason 1966 and the selection task baseline** [a11, a21, b01]. The abstract task gives a fixed answer profile. First four studies: p and q 46 percent, p alone 33 percent, p, q and not-q 7 percent, p and not-q (correct) 4 percent. Other sources give 5 to 10 percent correct. Pooled over 34 abstract tasks (845 subjects), card counts were p 754, q 522, not-q 215, not-p 137 [a11]. Wason (1969) cited via Ragni: when people were made to imagine what could be on the other side, partial insight rose to 53 percent and correct to 31 percent in the last block [b04, second-hand]. In the repeated selection task (Johnson-Laird and Wason 1970b), nearly everyone starts with q cards, then with feedback learns to pick the not-q cards [b05, second-hand].

**2.3 Wetherick 1962 and Nickerson 1998: is it really a wish to confirm?** [a23, a24]. Wetherick argued you cannot say a person wants to eliminate or keep a hypothesis unless you know what each test was for. Nickerson separates logical from psychological confirmation. A yes to a triple chosen to fit your guess feels strongly confirming but is logically weak. He also notes the selection task has two readings: which of these four cards to turn (answer p and not-q) versus which evidence type best tests the rule in general (where p may be the only informative one and not-q nearly pointless when it is rare). Choosing p is not avoiding falsification, since p can falsify the rule. Wason (1962, 1968) answered that even intelligent people hold to hypotheses with remarkable tenacity.

**2.4 Klayman and Ha 1987: positive test strategy (PTS)** [a04-a09, b07-b10]. Much of "confirmation bias" is one heuristic: test cases you expect to have the target property. They separate +Htest (an instance the hypothesis says is a target) from +Ttest (an instance known to be a target). Key results:
- If the hypothesis H lies inside the true target set T (the 2-4-6 case), a +Htest can never falsify, since every such instance is in T. Only a -Htest (an instance outside H) can show the rule is too narrow. If H is wider than T, positive tests are the only way to find a falsifier. If they overlap, both can [a05, b08].
- PTS is often the better choice. When H is about as big as T and the target is a minority (p(t) below .5), a positive test is more likely to falsify than a negative one. Approximate false-positive rate z+ = 1 - p(t)/p(h) [a06].
- In the four-card task PTS gives the p and q answer. The rule "if p then q" has one falsifier (p and not-q), so PTS is the wrong strategy there. A one-sided conditional and a two-sided rule need different strategies [a08].
- People default to PTS when detail is missing or load is high. With a small listable hypothesis set, the optimal "focusing" strategy exists but costs memory [a09].
- Tweney et al. (1980) DAX/MED: feedback was recast as DAX (true rule) versus MED (everything else). People tested each positively, which fixed the problem [a07, b09, second-hand].

**2.5 Oaksford and Chater 1994 and 2003: optimal data selection** [a10-a15, b11-b14]. The selection task is not a deduction task. It is choosing data to tell two hypotheses apart: dependence (if p then q) versus independence. Score each card by expected reduction in Shannon uncertainty (expected information gain, EIG). With the **rarity assumption** (p and q are rare), EIG orders cards p > q > not-q > not-p, which is the observed order. The not-p card has EIG zero always. The model has three free parameters P(p), P(q), P(MI). The 2003 revision gives both hypotheses the same marginals and adds an exceptions parameter. Supporting predictions: raising P(q) raises not-q picks and lowers q picks (Oaksford, Chater, Grainger, Larkin 1997; 1999). Criticism: Laming 1996, Evans and Over 1996, Oberauer et al. 1999 (no probability effects found), Gebauer and Laming 1997, Green 2000, Hardman 1998. Authors concede that probability manipulations with real-world content were only partly successful because prior beliefs interfere.

**2.6 Content and social exchange** [a16-a19, a25]. Cosmides (1989): if a rule has a cost-benefit structure, people check for cheaters, even on unfamiliar rules. Cheng and Holyoak (1985): pragmatic reasoning schemas such as permission. Griggs and Cox (1982): the drinking-age rule gives about 74 percent correct [b26, b33 second-hand]. Cognitive accounts differ on why: a cheater-detection module (Cosmides), permission and obligation schemas (Cheng and Holyoak), relevance (Sperber), or a general counterexample-search driven by perspective (Staller, Sloman, Ben-Zeev 2000).

**2.7 Relevance theory** [a20]. Sperber, Cara, Girotto (1995): people infer consequences of the rule in order of accessibility and stop when expected relevance is met. Raise the expected relevance of the not-q card and correct answers appear in any domain, even abstract ones. Oaksford and Chater (1995) replied that relevance and information gain are compatible, not rival, and that Sperber's own data are fit by EIG (r(14) = .89) [b14]. So those data do not discriminate the two.

**2.8 Matching bias and misreading** [a21, a22, a28, b27]. Evans and Lynch (1973): people choose cards named in the rule regardless of negation, so "if p then not q" looks easier (about 60 percent correct in a negated-consequent version). Stahl, Klauer, Erdfelder (2008) found matching bias reduced but not eliminated by explicit negations. A rival view: people misread the task (reading "other side" as "underside", or the conditional as a biconditional), so the "bias" is a different question answered correctly [b27].

**2.9 Dependence and model theory** [a27, b01-b06, d18]. Ragni, Kola, Johnson-Laird (2018): meta-analysis of 228 experiments comparing 16 theories. Selections inside an experiment depend on each other. Salient counterexamples raise the correct selection. Mental model theory fit best. Kellen and Klauer (2020) say the model comparison is not identifiable. Klauer et al. (2007) offer a rival 10-parameter processing tree with about 25 percent guessing. Each side is the author of its own model.

**2.10 How the theories differ in one table**

| Theory | What it says drives test choice | Predicts for abstract task | Predicts a fix |
|---|---|---|---|
| Wason: verification wish | wish to confirm | p and q | make people face falsifiers |
| Klayman and Ha: PTS | positive-test default, which is rational at times | p and q | choose test type by H vs T size and base rates |
| Oaksford and Chater: EIG | information gain with rare p and q | p > q > not-q > not-p | give true frequencies |
| Cosmides / Cheng: content | domain schema or module | poor abstract, good social | frame as violation |
| Sperber: relevance | accessibility and relevance | poor abstract | raise relevance of the not-q case |
| Evans: matching | lexical match with the rule | poor, negations flip | reword with explicit negations |
| Ragni: model theory | mental models, counterexample salience | canonical sets | make counterexamples salient |

For the scaffold the five accounts agree on a practical rule [a30, our synthesis]: the best test is the one most likely to split the live hypotheses, given how big each is and how rare the target is. Where one hypothesis sits inside another, only a test outside the smaller one can tell them apart.

---

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| 2-4-6: most people announce wrong rules first | N=29: 6 no wrong rule, 13 one wrong, 9 two or more, 1 never | Wason 1960 [a01] | [E] pattern; Wason count itself single study |
| Reworded rule kept after "no" | kept same rule in over half of cases; 3 + 3 protocols | Wason 1960 [a02, a03] | [S] |
| Abstract selection task: logical answer rare | p and q 46%, p 33%, p+q+not-q 7%, p+not-q 4%; other sources 5 to 10% | [a11, a21, b01, b26] | [E] (K01) |
| Pooled card counts, 34 tasks, 845 subjects | p 754, q 522, not-q 215, not-p 137 | O and C 1994 [a11] | [E] |
| EIG model fit, negations | rho(16) = .92; 19 vs 5 pairwise agreements, p < .005 | O and C 1994 [b12] | [C] |
| EIG model fit, 34 studies | G2(68) = 88.37, mean P(p) .22, P(q) .27 | O and C 2003 [a13] | [C] |
| Probability manipulations | 28 conditions, mean G2(2) = 3.15; not-q never passed q in Exp 1 with real content | O, C, Grainger 1999 [a14] | [C] |
| Selection pattern dependence | 99 of 228 experiments more redundant than 10,000 simulated independent runs | Ragni et al. [a27, b02] | [C] (K05) |
| Social contract vs descriptive | 75% vs 21% (Exp1), 71% vs 25% (Exp2); switched contracts 65% vs 0%, 80% vs 10% | Cosmides 1989 [a16, a17] | [C] |
| Social contract replication | precaution 50, social contract 45, obligation 30, permission 20, situation control 15, action control 10 (n=20 each); deontic not above matched controls | Fiddick 2003 [a18] | [C] |
| Relevance manipulation | 78% vs 26% (Exp1, n=27 per cell); 70% vs 25% (Exp3); 57% abstract (Exp4) | Sperber et al. 1995 [a20] | [S] |
| Perspective instruction | Exp3: 50% and 58% p+not-q vs 3% and 0% in other perspective | Staller et al. 2000 [b28] | [S] |
| Negated consequent | about 60% correct | Evans 1972 via [a21] | [E] pattern, mechanism [C] |
| Matching bias with explicit negations | reduced not removed; about 75% inference / 25% guessing model fit; groups of 200-360 | Stahl et al. 2008 [a22] | [S] |
| Experts still fail | Dutch judges 22.2% correct, 40% confirming only (n=27); maths majors and mathematicians under 50% on arbitrary rules | [b31, b17] | [E] (K17) |
| Slow humans do better only on realistic rules | slowest 15% (over 80 s) above chance only on realistic; time z = 4.44 | Dasgupta [b16] | [S] |
| Confirmatory question choice in social tests | certain testers ask mostly confirming questions; F(1,47) = 4.161 | Swann and Giuliano 1987 [b29] | [S] |
| Confirmatory choice in clinical hypothesis tests | N=206; numeric group: confirm 25%, disconfirm 17.5%, both 45%, none 12.5%, chi2(3) = 9.80 | Godoy Avila et al. 2008 [b30] | [S] |
| Tutoring | consequent logical choices about 37% to 66% (garbled table); transfer not shown | Osman 2007 [b25] | [S] (K18) |
| Logic course alone fails | 12-week course no help; logic helps abstract only, permission examples deontic only, both help all | Cheng et al. 1986 [b26, b34 second-hand] | [S] |
| Dual-goal DAX/MED (humans) | about 20% standard vs over 60% dual-goal | Gale and Ball 2006 [a26, abstract read] | [E] direction (with Tweney, Rossi) |
| Contrast pair choice | 2-4-6/6-4-2 about 75%; 4-4-4 about 20%; 9-8-1 about 34% | Gale and Ball 2012 via Branchini [b24, d08] | [S] second-hand (K08) |
| Counterexample framing | Rossi 2001: about 2x test triples, over 4x negative feedback, over 50% first-attempt solutions | via Branchini [b24, d08] | [S] second-hand |
| Thinking in opposites | 78.33% vs 38.33% (properties only) vs 36.66% (control); N=180, 60 per cell; chi2(2) = 27.986, p < .001 | Branchini et al. 2025 [b22, d07] | [S] (K07 marks as established through the family of contrast results) |
| Opposites gain mechanism | fewer repeated hypotheses, no more triples; solution earlier, F(2,89) = 5.702, p = .004 | [b23, d07] | [S] |

Note: pooled effect sizes are almost absent in this field. The meta-analyses give pattern frequencies, not effect sizes (critique).

---

## 4. Mechanisms and models, for an engineer

**4.1 Test types (Klayman and Ha).** Given a hypothesis H (a predicate over inputs) and an oracle for the true rule T:
- +Htest: input where H(x) is true. -Htest: input where H(x) is false.
- If H is a subset of T: +Htest always returns yes, so it cannot falsify. -Htest returns yes exactly when H is too narrow, which is conclusive falsification.
- If H is a superset of T: +Htest returns no on the surplus, which falsifies. -Htest returns no, which only verifies weakly.
- Overlap: both types can falsify.
Implementation: keep the live hypothesis list as executable predicates. For a candidate input x, label it by which hypotheses predict yes and which no. A test is discriminating if the predictions split.

**4.2 Positive vs negative test by size.** From a06: with H about as large as T and T a minority, positive tests falsify more often. Estimate p(h) as the share of sampled inputs H accepts, p(t) from oracle answers on random probes. Rule of thumb for code: if H accepts a small fraction of the input space (narrow guess), force a -Htest; if H is broad, positive tests are the main route. A fixed "always seek the negative case" is wrong in general [b08].

**4.3 Expected information gain (Oaksford and Chater; BED-LLM; Piriyakulkij).** Keep a set of hypotheses h_i with weights w_i (prior, updated). For a candidate test x with outcomes y in {yes, no}:
- P(y|x) = sum_i w_i * P(y|x, h_i).
- Posterior w_i' = w_i P(y|x,h_i) / P(y|x).
- EIG(x) = H(w) - sum_y P(y|x) H(w'_y), with H Shannon entropy.
For noiseless deterministic hypotheses, EIG is highest for the input that splits the surviving weight closest to half and half. The not-p card has zero EIG because both hypotheses predict the same thing for it. Pick x = argmax EIG. Entropy of the outcome alone is not enough: it confuses noise with information [c21]. LLM role: propose candidate hypotheses and candidate tests, and supply likelihoods. Code role: weight update and argmax. The Oaksford and Chater parameters (P(p), P(q), prior P(MI)) become in our agent the measured set sizes, which code can tell the model [a14, b13].

**4.4 Caution on self-generated hypothesis sets.** If the same LLM generates the hypotheses, EIG choice was no better than random on easy rules and worse than the positive-test strategy; it was better where falsification mattered, and all methods failed when the generator never proposed the true rule (one-run table, Gemini 2.5 Flash, 13 number-game rules) [d05]. Use EIG as a tie-break over valid candidates and refresh the set.

**4.5 Contrast operators (human interventions as procedures).**
- Think in opposites [b22, c03]: pick a property of the last test triple, build a triple with the opposite value of that property, test it. Code-checkable: the new input must differ from the old one on exactly the named property (a minimal pair).
- Dual goal [a07, c03]: keep two rules, A (the hypothesis) and not-A (its complement), and give feedback as A or not-A. Each test then becomes a positive test of one of two rules.
- Counterexample framing [b24]: present the seed as a counterexample of the experimenter's rule.
- The contrast must lie along the dimension that matters; a wrong contrast gave 20 to 34 percent [b24, second-hand].

**4.6 Rewording check.** Run old and new hypothesis on the same held-out inputs. If no prediction changes, the revision is a rewording and is rejected (derived from a02, d13, d16; not yet measured for LLMs, K24).

**4.7 Test-budget bookkeeping (WILT).** Dedupe exact repeated tests in code (weak models repeat 6.7 to 9.8 tests per rule). Count how many of a random pool of 2000 candidate rules each test crosses off [c06]. Count distinct hypotheses, not tests [b23].

**4.8 Selection-task logic.** For "if p then q": the only falsifier is p and not-q. In code, enumerate each option's possible hidden side and ask whether any hidden value would violate the rule. This turns the selection task into a mechanical check (modus tollens as an explicit operator, a25).

**4.9 Sequential falsification with error control (POPPER).** One agent proposes a measurable implication of the hypothesis as a null test. Another runs it with code. P-values become e-values and combine by sequential testing under a Type-I budget. Power 0.61 vs 0.38 for ReAct on DiscoveryBench at Type-I 0.1; a relevance checker was needed to keep Type-I control [c18, c19]. Fits open scientific hypotheses, not ARC-like items.

---

## 5. What holds up

**5.1 Replicates well.**
- The abstract selection task has a stable, small set of answers and the correct one is rare (many studies, 4,230 face-to-face people in 89 experiments plus 3,787 online in 10) [a11, b01]. [E]
- Positive testing in rule discovery is replicated across many tasks (Klayman and Ha 1985, Mahoney, Mynatt, Taplin, Tweney) [b09, second-hand citations]. [E]
- Thematic content raises performance (drinking-age about 74 percent; social contract 45 to 80 percent depending on study). [E] for the effect, [C] for the cause.
- Experts do not escape: judges 22.2 percent, mathematicians under 50 percent [b31, b17]. [E]
- Contrast-based help on the 2-4-6 task (Tweney DAX/MED, Rossi counterexample, Gale and Ball dual goal, Branchini opposites). Four separate human lines point the same way, but three of the four are known to us only through Branchini or Klayman and Ha [a26 abstract read]. [E] on direction.

**5.2 Disputed or failed.**
- Information gain model: authors fit 34 studies; Oberauer et al. found no probability effects; Ragni et al. say nine theories including it fail to predict dependence; Kellen and Klauer say Ragni's comparison is not identifiable. [C]
- Size and cause of content effects: Cosmides 70 to 80 percent vs 20 to 25 percent; Fiddick 45 vs 15 to 25, with deontic not above matched controls [a18]. [C]
- Positive testing as a "bias": Klayman and Ha say it often works; FalsifyBench shows it hurts when H is narrower than T [c08]. Both true; cost depends on set relations.
- Matching bias: explicit negations reduce, not remove [a22]. Whether it is shallow or relevance-based is open.

**5.3 Moderators.**
- Certainty: bias grows with certainty (Swann and Giuliano) [b29].
- Time and test chances: more tests and no time pressure give wider testing [a07]. Slower humans do better, only on realistic content [b16].
- Base rates and set sizes: card choice shifts with set size and with P(q) (Kirby 1994; O and C) [b13, a14].
- Layout and wording: layout alone moves LLM results with odds ratios of 1.2 to 1.5 [b21].
- Feedback: with immediate feedback people find the not-q cards fast [b05].
- Perspective instruction decides which counterexample is searched for [b28].

**5.4 Interventions that worked (humans).** Thinking in opposites (78 vs 37 percent, N=180) [b22]. Dual goal (about 20 to over 60 percent) [a26]. Counterexample framing [d08]. Imagining the hidden side (Wason 1969) [b04]. Socratic tutoring (modest, task-specific) [b25]. Concrete context with violation framing [a16, a18]. Salient counterexamples [b03].

**5.5 Interventions that did not work.** Listing properties of the seed without opposites (38 vs 37 percent) [b22]. Telling people to be careful or stressing importance (chi2(3) = 3.187, p = .364) [b30]. Logic course alone (12 weeks) [b26]. Performance bonus (no difference) [b16]. Wrong-dimension contrast (20 to 34 percent) [b24]. Teaching modus tollens in the abstract without concrete examples [b26]. Distilling a falsification habit into weights: small transfer, below prompting [c04].

**5.6 Gaps in the human evidence (critique).** Branchini's opposites result has no independent replication found and is from one group; country not stated; the opposites arm has one extra training step so some of the gain may be elaboration; training time was not equalised [d07]. Rossi 2001 and Gale and Ball 2012 are not read in the original. Pooled effect sizes are absent.

---

## 6. Language models

**6.1 Selection task, forced choice.**
- Dasgupta et al. (Chinchilla, PaLM 2, GPT-3.5): realistic rules beat arbitrary ones, as in humans (all z > 2.2, p < .03; marginal z about 1.78, p about .08 for PaLM 2-M and Flan-PaLM 2). Humans were not above chance overall. Models gave more correct responses than humans and different error patterns [b15, b18, c11, c12]. One source (the journal version and arXiv are the same paper).
- Seals and Shalin: seven-billion-scale open models mostly 0.06 to 0.29 (chance 1/6). Realistic over shuffled: OR 1.30. Classic vs front format OR 1.34; front vs back OR 1.29. Social-rule status not significant; LLMs solve social-rule problems about 30 percent vs about 70 percent for humans [b21, c13]. Conflicts with Dasgupta (different models, scoring: option likelihood vs forced two cards).
- Abe et al. 2026 (160 problems, 80 deontic, 80 descriptive; nine open models): every model better on deontic by 5.0 to 45 points. Zero-shot deontic: gpt-oss-120b 100.0 (+30), qwen3-32b 98.8 (+38.8), qwen3-14b 97.5 (+45), gemma3-27b 77.5, llama-3.3-70b 62.5, gemma3-12b 58.8, gemma3-4b 17.5, gpt-oss-20b 67.5 (91.2 few-shot) [b19, c14].
- Chain of thought (cap 6,000 tokens vs 10 for zero-shot) was not safe: llama-3.3-70b 62.5 to 83.8; olmo-2-32b 36.2 to 57.5; gemma3-4b 17.5 to 38.8; but gemma3-12b 58.8 to 43.8 (few-shot 78.7 to 43.8) and gemma3-27b 77.5 to 62.5. Reasoning models 98 to 100 percent without CoT [c25, d09]. Single study.
- Error type: gpt-oss-20b zero-shot deontic p to q: true antecedent 100%, true consequent 45%, false consequent 55%. p to not-q: false consequent 95%, true consequent 5%. Errors fit matching bias better than confirmation bias [b20, c15]. Deontic rules only, so right answers and matching can coincide.
- Early ChatGPT claims (Alsagheer et al. 2024) are weak and should not be used [c16]. Macmillan-Scott and Musolesi: the press figure (GPT-4 90 percent vs GPT-3.5 and Bard 0 percent) is not in the paper text; it is in a figure; keep out of the schema case [d17, c17]. Their GPT-4 overall was 69.2 percent correct with correct reasoning; the same model gave different answers to the same prompt.

**6.2 Rule discovery games (2-4-6 style).**
- **Jhaveri et al. 2026**, eleven LLMs, 45 turn cap. Baseline success 6 to 78 percent. Non-thinking: Qwen3-8B 0.06, Qwen3-14B 0.23, GPT-4o 0.11, Llama-3.3-70B 0.21, Qwen3-32B 0.33. Gemini-2.5-Pro (thinking) 0.73. Success correlates with I:C, the ratio of incompatible (could falsify) to compatible tests [c01, c02].
- Think-in-Opposites: non-negative in all 11 settings (equal for Qwen3-8B non-thinking, 0.062 both). Averaged: thinking models +0.123 success (p < 2e-5), I:C +0.168; non-thinking +0.063 success (p = 0.0033), I:C change not significant (+0.020, p = 0.60). Abstract: discovery rate 42 to 56 percent. Llama-3.3-70B 0.21 to 0.38; GPT-4o 0.11 to 0.16; Qwen3-32B thinking I:C 0.14 to 0.54. 80 episodes per model per cell [c03, d01].
- Dual-Goal: thinking +0.148 (p < 2e-5), I:C +0.375; non-thinking -0.060 (p = 0.0065). Hurt Qwen3-14B (0.225 to 0.125), Qwen3-32B (0.325 to 0.100), Llama slightly (0.212 to 0.200) [c03, d01, critique].
- Tokens: thinking-model tokens per turn rose with TiO (Qwen3-8B 1088 to 1716, +58%; Qwen3-32B 1030 to 1450, +41%; Qwen3-14B +13%; R1-distill-Llama-70B +12%; read from garbled table). Non-thinking tokens about equal (8.4 vs 8.4). No matched-budget run [d02]. Some of the thinking-model gain may be more thinking.
- Transfer: Blicket detector baseline Qwen3-8B 0.32, Qwen3-32B 0.57; with TiO 0.40 and 0.86. Wason-distilled 8B student 0.34, below prompting [c04].
- **WILT (Banatt et al. 2024)**, 50 hidden rules, up to 30 tests then a lambda guess. Claude 3.5 Sonnet 14/50, o1-mini 13/50, o1-preview 12/50, chatgpt-4o-latest 11/50, Mistral Large 2 11/50, GPT-4o 9/50, Llama 3.1 405B 8/50, GPT-4o-mini 6/50, Claude 3 Haiku 1/50. Best 28 percent. Repeats per rule: GPT-4o-mini 9.78, Claude 3 Haiku 8.00, Gemma 2 9B 7.72, Llama 3.1 8B 6.68, GPT-4o 2.84, o1-preview 0.06. Role split: o1-mini given chatgpt-4o-latest's tests guessed 19 of 50, above any single-model run; o1-mini did worse with its own tests (number only in a figure). Looks like a stronger-tester effect, not a role-split effect [c05-c07, d03, d04].
- **FalsifyBench (Bertolazzi et al. 2026)**, 12 models, 100 games each, 20 turn cap, WordNet categories, model is its own oracle (85 to 95 percent oracle accuracy). Success: GPT-5.2-Chat 75, GPT-OSS-120B 68, DeepSeek-V3.1 41, Qwen3.5-9B 21, GPT-5-Nano 12, other instruction-tuned 33 to 35. Positive-test share vs success rho = -0.779 (p = .003); positive share vs conclusive falsification rate rho = -0.937. Conclusive falsification: GPT-OSS-20B 59.2, GPT-OSS-120B 53.4, GPT-5.2-Chat 49.5, GPT-5-Nano 26.6, Llama-4-Maverick 18.0. Positive-test share 39.0 (GPT-5-Mini), 27.3, 24.2 vs 66 to 82 for instruction-tuned. Within a model, failed games have more positive tests: GPT-5.2-Chat 20 vs 50 percent; GPT-OSS-20B 17 vs 53 percent. Mixed-effects logistic regression n = 1,200: confirmation bias posterior mean -4.15 (OR 0.016); oracle error -0.12 (OR 0.885, interval spans zero). H narrower than R in over 50 percent of turns for almost every model. Failed games also drift into disjoint or partly overlapping hypotheses [c08-c10, d12]. Hypothesis-target relations labelled by GPT-5-Mini.

**6.3 Why first guesses are narrow.** LLMs assume examples are drawn from the target set (strong sampling), preferring narrower hypotheses; thinking mode pulls toward the prior. Judging a given rule is easier than generating one [d15, abstract and intro only].

**6.4 Machine "optimal data selection".**
- BED-LLM: 20 Questions success up 37.4 points on average over direct prompting; more than doubled in over half the setups, never decreased [c21].
- Grand et al. Battleship: Captain EIG up to 0.227 bits; Llama-4-Scout win rate 8 to 82 percent, beating humans and GPT-5 at about 1 percent of GPT-5 cost; zero-information questions Llama-4-Scout 18.5%, GPT-4o 14.6%; Guess Who +42.4 points for Llama-4-Scout [c22].
- Piriyakulkij 2024: Zendo score out of 8: human 5.26, direct LLM 4.60, online fuzzy 6.01 to 6.18, batch hard 6.55 [c20]. Piriyakulkij 2026: same recipe, figures only [d06].
- BoxingGym: experiment design stays weak even with tools; adding statistical modelling did not significantly help [c23].
- Chari and Pattanaik: EIG over the LLM's own hypothesis set not reliably better (section 4.4) [d05].

**6.5 Where the bottleneck is.** Producing the right hypothesis. Refinement rescued 4.3 percent of semantically wrong hypotheses (GPT-4o, 100 list-function tasks x 11 trials = 5,500; hypothesis search 0.487 test accuracy, direct 0.359, human 0.521; 45.4 percent of programs that passed the single held-out example still failed the true rule) [d13]. On ARC-AGI-1 (400 tasks, non-thinking DeepSeek V3.2): one-shot 15.5 percent ($0.002), structured CoT 30.0, explorer-definer pipeline 57.5 pass@2 ($0.25), reflective orchestrator 67.25 pass@2 ($0.62); explorer count N is the dominant lever (N=1 never above 45.5). Cost 125x and 310x one-shot, so not token-matched; Qwen3-235B orchestrator lift +6.06 with CI including zero [d14].

**6.6 Chain of thought and induction.** CoT cut accuracy where verbal deliberation hurts people. GPT-4o artificial grammar direct 87.5 vs CoT 64.4 (-23.1, p < 0.0001); o1-preview 36.3 points lower than GPT-4o on a subset; Claude 3.5 Sonnet no drop (65.9 vs 67.7) [d10]. Jin et al. (NeurIPS 2025) report CoT can hurt induction on hidden-rule games [d11, snippet only].

---

## 7. What our agent should take

Status marks: [E] established, [S] single source, [C] contested.

### 7A. Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | When the hypothesis could be narrower than the truth, include at least one test that the hypothesis predicts will FAIL (a -Htest). Positive-only testing cannot expose a too-narrow rule. Reason it as set relation, not as a blanket "try to disprove". | S7 and S4 | [E] (theory plus 3 LLM benchmarks; the code-enforced version is untested, see 7B) | a04, a05, a06, b08, c08, c09, K02 |
| A2 | Log in code the share of tests that could falsify the current hypothesis (I:C or positive-test share) per run. It predicts success. Use a stale-run signal (many positive tests in a row) as the trigger for a forced outside-the-hypothesis test, since G1 allows doubt on a signal. | section 6 logging, G1 | [E] as a correlate (correlational only) | c01, c08, c09, c10, d12, K09 |
| A3 | Distrust stated reasoning and stated "I checked it". Domain experts and trained judges keep the confirming default. Judge by tests actually run. | G10 | [E] | b17, b31, b29, a03, K17 |
| A4 | Block exact repeated tests in code. Weak models repeat 6.7 to 9.8 tests per rule; strong ones about 0.06. Count distinct hypotheses, not tests. | S4 | [E] on the pattern (mechanism is a symptom, not a proven cause) | c06, d04, b23 |
| A5 | Make the counterexample explicit: state what a falsifying instance looks like before choosing tests. Perspective ("look for a violation of X") sets which counterexample is searched. | S2, S7 | [E] directionally (Ragni salience, Staller, Wason 1969, Sperber) | b03, b04, b28, a20 |
| A6 | Do not rely on instructions to "be careful" or on importance framing, a bonus, or abstract logic teaching. Keep section 4b as is. | 4b | [E] | b30, b16, b26, K18 |
| A7 | Do not assume a chain-of-thought lever is safe. Cap it per model and measure. CoT helped some models and hurt others by 15 to 20 points on the same task. | G11 | [C] on direction, [E] that it varies | d09, d10, d11, c25, K20 |
| A8 | Generation of the right hypothesis is the bottleneck. Several independent hypothesis sets beat refining one set. Refinement rarely fixes a wrong idea. | S3 | [E] (3 sources) | d13, d05, d14, K21 |
| A9 | A code-computed discriminating test between two surviving rules (the input where they disagree) is the right form of S7's counterexample search. Do not leave test choice to the model's opinion. | S7, G5 | [E] that LLM-proposed plus code-scored tests help on games with closed sets (3 sources); [S] on our task classes | c20, c21, c22, a10, K15 |
| A10 | Tell the model true set sizes and base rates from code, since test value depends on them. | S1, S7 | [S] | a14, b13, a06 |

### 7B. Test first

| # | Item | Schema part | Status | Evidence | What is unknown |
|---|---|---|---|---|---|
| T1 | **Code-gated falsification:** code rejects any round whose tests all fit the current hypothesis. | S4 | [S]/open | d20, K25 | No study compares code-enforced vs prompt-only at matched tokens. |
| T2 | **Think-in-Opposites step:** for one property of the last test, build the opposite and test it (minimal pair). | S2 or O6 | [S] | c03, d01, b22, K11 | Jhaveri gain unmatched on tokens (+12 to 58 percent for thinking models). Human result has no independent replication. |
| T3 | **Dual-goal (hypothesis plus complement):** keep rule A and not-A. | S2 | [C] | a26, c03, d01, K07 | Helps thinking models (+0.148), hurts non-thinking (-0.060). Per-model test only. |
| T4 | **Role split:** test proposal separate from rule inference; inferer sees only outcomes. | S3 | [S] | c07, d03, K12 | Gain looks like a stronger-tester effect. Same-model split untested. |
| T5 | **EIG tie-break among candidates** over an explicit hypothesis set, set refreshed each round. | S7, G5 | [C] | c21, c22, d05, K15 | When the same LLM builds the set, EIG gain disappeared on easy rules. |
| T6 | **Rewording check:** a revision that changes no held-out prediction is rejected. | S5, G2 | open | a02, d13, d16, K24 | Not measured for LLMs. |
| T7 | **Concrete re-expression (O6):** rewrite an abstract rule as a "who breaks the rule?" case. | O6, S2 | [C] | b15, b21, c14, K06 | Dasgupta vs Seals and Shalin conflict; no re-expression intervention study. |
| T8 | **Negated-wording probe in S1:** reword the same logic with negations; a flip means matching, not reasoning. | S1 | [C] on mechanism | a22, b20, c15, K19 | One LLM study. |
| T9 | **Explorer breadth and re-exploration at an impasse:** k independent hypothesis sets vs one refined k times. | S3, S6, O3 | [S] | d14, K22 | Gains at 125x to 310x cost; need token-matched best-of-n CoT arm. |
| T10 | **Lessons for test choice (S9):** one-line lessons shown after the first attempt; test transfer to a differently worded item of the same class. | memory | [S] | b25, K18 | Human tutoring transfer not shown. |
| T11 | **Sequential falsification gate (POPPER) for open scientific hypotheses.** | S8 | [S] | c18, c19, K16 | Not for ARC-like items. |

**Recommended ordering for the schema.** Put A1, A2, A4 and A9 in S4/S7 as code rules now. A5 goes in S2 as a one-line step. Everything in 7B stays out of the schema until it wins at equal tokens (G7).

---

## 8. Concrete tests on our bench

Common rules: each arm gets the same total token budget (count setup and all sampled attempts; G7). At least 80 episodes per arm per model, because Jhaveri used 80 per cell and the effects were +0.06 to +0.15. Run on one thinking and one non-thinking model, since prompt effects reverse by model class. Fresh context per attempt (G4). Log per run: falsifying-test share, repeated tests, hypotheses tried, tokens per state.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 Code-gated falsification (T1) | Hidden-rule discovery: model proposes inputs, a code oracle answers yes/no, then a final rule guess is scored on held-out inputs. Include items whose first natural guess is a strict subset of the truth. | (a) plain; (b) prompt-only "include a test your hypothesis predicts will fail"; (c) code-gated (reject a round where all tests are in H) | success on held-out inputs; falsifying-test share | (c) > (b) > (a) on subset items; no effect where H is broad. A positive result on thinking models only would match Jhaveri. |
| B2 Opposites vs plain (T2) | Same suite | plain vs TiO prompt; add a plain arm with extra sampled attempts to match TiO's extra tokens | success; success per token | Jhaveri: +0.06 non-thinking, +0.12 thinking, before token matching. Expect the gain to shrink at matched tokens. |
| B3 Dual-goal (T3) | Same suite | plain vs dual-goal feedback | success per model class | Hurts non-thinking, helps thinking (Jhaveri). Keep only for models where it wins. |
| B4 Wrong-dimension contrast control | Same suite | opposites on relevant property vs opposites on an irrelevant property | success | Relevant contrast wins (humans: 78 vs 38). Tests that "any contrast" is not enough (K08). |
| B5 Role split on one model (T4) | Same suite | combined call vs proposer/inferer split (same model both roles) vs split with a stronger tester | success | If gain comes only with a stronger tester, drop the same-model split. |
| B6 EIG tie-break (T5) | Two or more live rules from a small enumerated hypothesis set (e.g. ARC-like transformations or number rules) | model-chosen test vs code-scored EIG test vs random | tests to converge; failures | Closed set: EIG wins (+37 points in 20 Questions). Self-generated set: EIG may tie random (Chari). Report both. |
| B7 Rewording rate (T6) | Same suite, revise after a "no" | count revisions that change no held-out prediction; compare plain with a code gate that rejects them | rewording rate; success | A high rate in the plain arm would confirm the Wason 1960 pattern for LLMs; gate should reduce it. |
| B8 Abstract vs concrete re-expression (T7) | Selection-task items (conditional, find the violating cases), abstract and deontic matched pairs; also negated variants | abstract vs concrete re-expression (code verifies meaning unchanged) | exact-match accuracy; flip rate under negation | Deontic gap 5 to 45 points for open models (Abe). Re-expression gain unknown. |
| B9 Short vs long reasoning (A7) | Selection and rule-discovery | short budget vs long budget, per model | accuracy | Direction varies by model (llama +21, gemma3-12b -15 on Wason). Keep the winner per model. |
| B10 Breadth vs refinement (T9) | Rule induction with code oracle | one set refined k times vs k independent sets, matched tokens | pass rate | d13/d14 suggest breadth wins. |
| B11 Lesson transfer (T10) | Same class, new wording | no lesson vs one-line lesson shown after first attempt | success on reworded item | Human transfer unproven; expect small. |
| B12 Sample dependence | Rule discovery | sample correlation of hypotheses across independent attempts | hypothesis diversity | Tests G4 directly; Ragni's dependence result does not transfer (d18). |

---

## 9. What does not transfer, and why

- **Human motives.** Wason's "wish to verify" is probably not the mechanism in models. Abe et al. find matching bias fits LLM errors better than confirmation bias [c15]; Bertolazzi finds failed games also drift into disjoint hypotheses [c09]. Human bias lists are not LLM bias lists (Dasgupta: error patterns differ) [c12].
- **Content and social-contract effects.** The cheater-detection account is about evolved human psychology. In LLMs the advantage is a content or deontic effect that varies by study (Dasgupta yes; Seals and Shalin social-rule not significant, 30 vs 70 percent). Treat as a prompt-framing question, not a module.
- **Selection task as a test of the agent.** It is a one-shot four-item problem. Our agent faces multi-step discovery with a code oracle. Reasoning models reach 98 to 100 percent on deontic selection [c14], so it does not discriminate strong models.
- **Ragni dependence.** The finding is about which cards one person picks together. No link to independence between repeated agent attempts was found [d18].
- **Human time effects.** Slow humans do better on realistic rules [b16]. This is correlational and does not show that more reasoning tokens help. It sits next to the CoT evidence that more reasoning can hurt [d09, d10].
- **Human training effects.** Tutoring, a logic course and classroom opposites training use short-lived human learning. The nearest analogue is a prompt step. Weight-level transfer was weak (Wason-distilled 8B student 0.34 on Blicket vs 0.40 with TiO prompt) [c04].
- **Single-oracle designs.** FalsifyBench uses the same model as player and oracle (85 to 95 percent oracle accuracy), WILT has 50 simple boolean rules, Jhaveri has a synthetic number-triple rule set. None tests a scaffold at equal tokens against a plain model.
- **Mere "falsify" instructions.** Section 4b already lists bias prompts as not working. Klayman and Ha show a blanket "falsify" is wrong when the hypothesis is broad. Only the set-relation rule transfers.
- **POPPER's statistical gate.** Needs a data-driven hypothesis and permutation nulls; does not fit ARC-like items.

---

## 10. Open questions

1. Does a code-enforced falsifying test beat a prompt-only one at matched tokens, for thinking and non-thinking models? (K25, d20: no study found.)
2. Does the Think-in-Opposites gain survive when the plain arm gets the same tokens? Thinking-model tokens rose 12 to 58 percent.
3. Is the WILT role-split gain a stronger-tester effect or a split effect? Needs a same-model, both-roles control.
4. How much of the +37 point EIG gain survives when the hypothesis set is generated by the same model? Chari: not reliably.
5. How often is an LLM revision only a rewording? (K24: unmeasured.)
6. Does a concrete re-expression help abstract rule discovery? Dasgupta and Seals and Shalin conflict.
7. Does longer reasoning help or hurt falsification in rule discovery? Wason evidence is mixed (llama up, gemma3-12b down).
8. Is there an independent replication of thinking in opposites (Branchini N=180, country unstated, one group)? Rossi 2001 and Gale and Ball 2012 are known only second-hand.
9. Do Ragni's dependence results predict anything for resampling independent attempts?
10. Do the LLM results hold when the oracle is a programmatic rule on grids (ARC-like) rather than a number triple? No falsifying-probe study on ARC exists (d14).
11. What is the real size of the information-gain model's fit advantage? Kellen and Klauer say Ragni's comparison is not identifiable; the authors fit their own model.
12. Which test types best separate wrong-hypothesis paths in LLMs that drift into disjoint hypotheses rather than narrow ones? (FalsifyBench shows drift beyond confirmation.)
13. Is a model's stale-run signal (many positive tests in a row) a good enough trigger for G1 doubt, or too noisy?

---

## 11. Sources

**[V] = opened and read this research (full text, or abstract plus the parts quoted). [M] = snippet or second-hand only.**

| Mark | Source | URL |
|---|---|---|
| [V] | Wason (1960) On the failure to eliminate hypotheses in a conceptual task | https://bear.warrington.ufl.edu/brenner/mar7588/Papers/wason-qjep1960.pdf |
| [V] | Klayman and Ha (1987) Confirmation, disconfirmation, and information in hypothesis testing | https://pages.ucsd.edu/~mckenzie/KlaymanHaPsychReview1987.pdf |
| [V] | Oaksford and Chater (1994) A rational analysis of the selection task as optimal data selection | https://pages.ucsd.edu/~mckenzie/OaksfordChaterPsychReview1994.pdf |
| [V] | Oaksford and Chater (1995) Information gain explains relevance which explains the selection task | https://www.dectech.co.uk/publications/LinksNick/ReasoningAndDecisionMaking/information%20gain%20explains%20relevance%20which%20explains%20the%20selec.pdf |
| [V] | Oaksford and Chater (2003) Optimal data selection: Revision, review, and reevaluation | https://link.springer.com/content/pdf/10.3758/BF03196492.pdf |
| [V] | Cosmides (1989) The logic of social exchange | https://cep.ucsb.edu/wp-content/uploads/2023/05/socexcog89.pdf |
| [V] | Fiddick (2003) Is there a faculty of deontic reasoning? | https://researchonline.jcu.edu.au/9921/2/9921_Fiddick_2003.pdf |
| [M] | Cheng and Holyoak (1985) Pragmatic reasoning schemas (PDF did not download; figures via Fiddick) | https://deepblue.lib.umich.edu/bitstream/handle/2027.42/25556/0000098.pdf?sequence=1 |
| [V] | Sperber, Cara and Girotto (1995) Relevance theory explains the selection task | https://www.dan.sperber.fr/wp-content/uploads/2009/09/SperberCaraGirotto.pdf |
| [V] | Stahl, Klauer and Erdfelder (2008) Matching bias in the selection task is not eliminated by explicit negations | https://methexp.uni-koeln.de/files/Stahl-Klauer-Erdfelder-2008.pdf |
| [V] | Nickerson (1998) Confirmation bias: A ubiquitous phenomenon in many guises | https://pages.ucsd.edu/~mckenzie/nickersonConfirmationBias.pdf |
| [V] | Gale and Ball (2006) Dual-goal facilitation in Wason's 2-4-6 task (abstract confirmed in cross-check) | https://eprints.lancs.ac.uk/id/eprint/3551/ |
| [M] | Ragni, Kola and Johnson-Laird (2018) On selecting evidence to test hypotheses | https://www.modeltheory.org/?p=954 |
| [M] | Evans and Lynch (1973) Matching bias in the selection task | https://journals.sagepub.com/doi/abs/10.1080/713755639 |
| [M] | Evans and Over (1996) Rationality in the selection task | https://wrap.warwick.ac.uk/id/eprint/18863 |
| [V] | Ragni and Johnson-Laird (2020) Explanation or Modeling: a Reply to Kellen and Klauer | https://doi.org/10.1007/s42113-020-00077-9 |
| [M] | Kellen and Klauer (2020) critique; Ragni 2018 and critique as seen in snippets | https://link.springer.com/article/10.1007/s42113-020-00077-9 |
| [V] | Dasgupta et al. (2022/2024) Language models show human-like content effects on reasoning tasks | https://arxiv.org/pdf/2207.07051 and https://arxiv.org/abs/2207.07051 |
| [V] | Abe et al. (2026) Evaluation of Deontic Conditional Reasoning in LLMs | https://arxiv.org/abs/2603.06416 |
| [V] | Seals and Shalin (2023/2024) Evaluating the Deductive Competence of LLMs | https://arxiv.org/abs/2309.05452 |
| [V] | Branchini, Bianchi and Burro (2025) Thinking in opposites improves hypothesis testing performance in Wason's rule-discovery task | https://doi.org/10.3758/s13421-025-01691-3 and https://pmc.ncbi.nlm.nih.gov/articles/PMC12402026/ |
| [V] | Osman (2007) Can tutoring improve performance on a reasoning task under deadline conditions? | https://doi.org/10.3758/BF03193455 |
| [V] | Staller, Sloman and Ben-Zeev (2000) Perspective effects in nondeontic versions of the Wason selection task | https://doi.org/10.3758/BF03198555 |
| [V] | Swann and Giuliano (1987) Confirmatory search strategies in social interaction | https://labs.la.utexas.edu/swann/files/2016/10/SwannGiuliano1987.pdf |
| [V] | Godoy Avila et al. (2008) Estrategias de comprobacion de hipotesis clinicas, Psicothema 20:188-192 | https://www.psicothema.com/pdf/3446.pdf |
| [V] | Maegherman (2021) Facilitating falsification in legal decision making (thesis) | https://cris.maastrichtuniversity.nl/ws/files/60865138/c6940.pdf |
| [V] | Wikipedia, Wason selection task (accessed 2026-10-20; used only to place headline numbers) | https://en.wikipedia.org/wiki/Wason_selection_task |
| [M] | Griggs and Cox (1982) The elusive thematic-materials effect (as cited by Osman 2007) | https://doi.org/10.3758/BF03193455 |
| [M] | Cheng, Holyoak, Nisbett and Oliver (1986) training study (as cited by Osman 2007) | https://doi.org/10.3758/BF03193455 |
| [M] | Gale and Ball (2009, 2012) contrast-class studies (as cited by Branchini) | https://doi.org/10.3758/s13421-025-01691-3 |
| [M] | Rossi et al. (2001), Tweney et al. (1980), Wason (1969), Johnson-Laird and Wason (1970), Kirby (1994), Evans (1972): all second-hand via the sources above | (no direct URL) |
| [V] | Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to Falsify | https://arxiv.org/abs/2604.02485 |
| [V] | Banatt, Cheng, Vaidyanath, Hwu (2024) WILT | https://arxiv.org/abs/2410.10998 |
| [V] | Bertolazzi, Tentori, Bernardi (2026) FalsifyBench | https://arxiv.org/abs/2606.04751 |
| [V] | Alsagheer, Karanjai, Shi (2024) Comparing Rationality Between LLMs and Humans (weak; do not use) | https://arxiv.org/abs/2403.09798 |
| [M] | Macmillan-Scott and Musolesi (2024), UCL press release (press figures) | https://www.ucl.ac.uk/news/2024/jun/ais-are-irrational-not-same-way-humans-are |
| [V] | Macmillan-Scott and Musolesi (2024) (Ir)rationality and cognitive biases in LLMs, arXiv text (Wason numbers only in a figure) | https://arxiv.org/abs/2402.09193 |
| [V] | Huang et al. (2025) POPPER | https://arxiv.org/abs/2502.09858 |
| [V] | Piriyakulkij, Langenfeld, Le, Ellis (2024) Doing Experiments and Revising Rules | https://arxiv.org/abs/2402.06025 |
| [V] | Choudhury et al. (2026) BED-LLM | https://arxiv.org/abs/2508.21184 |
| [V] | Grand, Pepe, Tenenbaum, Andreas (2026) Shoot First, Ask Questions Later? | https://arxiv.org/abs/2510.20886 |
| [V] | Gandhi et al. (2025) BoxingGym | https://arxiv.org/abs/2501.01540 |
| [V] | Chari and Pattanaik (2026) Wild Guesses and Mild Guesses in Active Concept Learning | https://arxiv.org/abs/2602.06818 |
| [V] | Piriyakulkij et al. (2026) Induction and Inquiry via Probabilistic Reasoning over Language and Code | https://arxiv.org/abs/2609.01815 |
| [V] | Liu et al. (2024) Mind Your Step (by Step) | https://arxiv.org/abs/2410.21333 |
| [M] | Jin, Zhang, Luo, Wang (2025) Evaluating the Inductive Abilities of LLMs (NeurIPS 2025) | https://papers.neurips.cc/paper_files/paper/2025/hash/94f087ae1cc87511d7b098359fc4eaae-Abstract-Conference.html |
| [V] | Analysis of Error Sources in LLM-based Hypothesis Search for Few-Shot Rule Induction (2025) | https://arxiv.org/abs/2509.01016 |
| [V] | Cost-Effective Agent Harnesses for ARC-AGI-1 (2026) | https://www.alphaxiv.org/abs/2607.06764 |
| [V] | Xiong (2026) Hypothesis generation and updating in LLMs (number game; abstract and intro only) | https://arxiv.org/abs/2605.05851 |
| [V] | Dobrowolska et al. (2026) Tiny Moves (abstract and sampled sections) | https://arxiv.org/abs/2602.09801 |
| [M] | Qiu et al. (2024) Phenomenal Yet Puzzling (ICLR 2024) | https://iclr.cc/virtual/2024/poster/18334 |
| [M] | Search for code-enforced falsification ablations (Baby-AIGS 2411.11910; DiscoPER 2607.01131; 2604.22080), negative result from summaries | https://arxiv.org/abs/2411.11910 |

**Counting notes (from critique).** Dasgupta appears three times in the evidence (b15, c11, c12) and is one source. Seals and Shalin appears twice (b21, c13) and is one source. Stanovich and West and Sperber appear second-hand in a15 and a21. Many LLM "established" results are correlations (I:C vs success, positive-test share vs success). Only Jhaveri's prompt runs and Branchini's human training are causal. Several 2026 arXiv items are not peer reviewed (Jhaveri, Bertolazzi; Abe is an EACL short paper). The Jhaveri per-model success and token cells are garbled in the PDF text; only the Table 15 averages are clean.
