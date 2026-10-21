# Content effects: why reasoning changes with content

Subfield 03 of A01 (cognitive psychology of thinking and reasoning). Deep document. Written 2026-10-21 from `evidence_a.jsonl` to `evidence_d.jsonl` (a01-a32, b01-b25, c01-c35, d01-d35), `claims.jsonl` (K01-K41) and `critique.md`.

Reading guide. Evidence ids (a01, b05, d20 ...) point to lines in the evidence files. Claim ids (K01 ...) point to `claims.jsonl`. Status marks follow the schema: **[E]** established (two or more independent sources), **[S]** single source, **[C]** contested. A line from the Cosmides group, from the Sperber group, or from the Fiddick chapter is one lab speaking about its own work, so many "agreements" below are weaker than they look. Where a number is second hand, this is said.

---

## 1. What it is

Content effects are changes in reasoning accuracy when the logical form stays the same and only the content, wording, goal or setting changes. The classic case is the Wason selection task. Four cards show P, not-P, Q, not-Q. The rule is "if P then Q". The correct choice is P and not-Q. On abstract letter-and-number rules fewer than 10 percent choose that pair (a01, a29, b10). On a drinking-age rule or a social-exchange rule, a majority do (d03, d05). The same split appears in syllogisms (believable conclusions are accepted even when invalid) and in language models, which show these patterns too (c01). The field asks two questions. First, which property of the content does the work: familiarity, a social contract with a cheater, a permission or obligation, relevance, the goal in the final question, or the wording of the rule? Second, can a thinker separate form from content on purpose? For our agent the second question is the useful one. The first question matters because it tells us what to restate and what not to build.

---

## 2. History and theories in depth

### 2.1 Baseline and the first content results

- Wason's abstract task (1966, 1968) gave very low correct rates. Wason (1968), as tabulated by Oaksford and Chater: P chosen 100 percent, not-P 17, Q 78, not-Q 28. Evans and Lynch (1973) control: P 100, not-P 6, Q 69, not-Q 12 (a17). Johnson-Laird and Wason (1970): 96 percent chose a wrong pattern (a10, as cited). "Not even 10 percent" solve it (a29).
- Early thematic versions: Wason and Shapiro (1971) and Johnson-Laird (1972) seemed to show that realistic content helps. Manktelow and Evans (1979) did not replicate. Griggs and Cox (1982) found the drinking-age rule ("if a person is drinking beer, then the person must be over 19") easy and blamed prior experience (a01). Cosmides (1989) later argued familiarity could not be the cause (d03). The failure of the early thematic studies is why "adding realism" is not a rule (K02 [E]).
- Evans and Lynch (1973) showed that abstract "if P then NOT Q" rules are routinely solved, and Evans (1989) explained this as matching bias: people pick the cards named in the rule (a07).

### 2.2 The main theories

| Theory | Who and when | Claim | What it predicts | Main weakness |
|---|---|---|---|---|
| Pragmatic reasoning schemas | Cheng and Holyoak 1985; Holyoak and Cheng 1995 | People hold abstract, goal-linked schemas (permission, obligation) built from experience. A rule that fits a schema triggers four production rules and the right cards follow. | Good performance on any permission or obligation rule, familiar or not. "Must" vs "may" is part of the mechanism (d30). | Predicts equal results across permission rules. Cosmides Exps 1-2 show 80, 52, 44 percent for three permission-like rules (a12). Fiddick's abstract permission (20) and obligation (30) did not beat controls (10, 15) (a04). |
| Social contract theory (cheater detection) | Cosmides 1989; Cosmides and Tooby 1992; Cosmides, Barrett, Tooby 2010 | An evolved algorithm looks for cheaters. A cheater takes the benefit and does not pay the cost. | Good on standard and on switched contracts (not-P and Q when the roles flip). Poor on matched rules without a cost-benefit structure. Intentional violations matter more than accidental ones. | Neutral categories do as well or better (b03). The final question carries the framing (b04, d29). Rule needs a cheating cue to work (d07). |
| Precaution / hazard management | Fiddick, Cosmides, Tooby 2000; Cosmides 2010 | A second evolved system for hazards: "if hazardous activity then protection". | Precaution violations are detected even when accidental. | Same lab; relevance theory reads the same data as a goal change (d29). |
| Perspective theory | Gigerenzer and Hug 1992 | Social contracts work through the point of view: you test the cases through which your party could be cheated. | Same rule gives P and not-Q from one side and not-P and Q from the other. | Authors say the issue is "not semantic but pragmatic" (d07). Does not need an evolved module. |
| Flexible deontic logic | von Sydow, Hagmayer, Metzner, Waldmann 2005 | Prescriptive rules are checked against an "ought table", not a truth table. The tester can look for rule breakers or rule followers. | Card choice follows rule type (obligation/prohibition) times goal (cheater/cooperator). | One short paper, 20 per cell, garbled table (a08). |
| Relevance theory | Sperber, Cara, Girotto 1995; Sperber and Girotto 2002, 2003 | Comprehension is guided by expected cognitive effect and effort. People pick the cards that the context makes seem able to violate the rule. The task tests comprehension more than reasoning. | Descriptive rules can be made easy and deontic rules made hard by story context alone. | Cosmides group: benefit-plus-intention should be most relevant but scored lower than the full cheater case (a15). |
| Information gain / rational analysis | Oaksford and Chater 1994, 2003 | In the descriptive task people pick cards by expected information gain about "rule holds" vs "no dependency", assuming P and Q are rare. | Why P and Q cards are chosen far more than not-Q. Needs a separate utility account for deontic rules. | Oberauer et al. 1999 failed to replicate probability effects (a19). |
| Model theory / inference-guessing | Johnson-Laird; Ragni, Kola, Johnson-Laird 2018; Klauer, Stahl, Erdfelder 2007 | Responses come from a small mental model of the rule plus independent guessing. Counterexample salience is the one effect reported as corroborated. | 228-experiment meta-analysis kept model theory and eliminated all but one of 15 rivals (b08). | Kellen and Klauer: non-identifiable. Authors of the winner wrote the reply (b08, b24). |
| Dual process | Stanovich and West 1998 | About 10 percent of students use System 2 on the abstract task (a18). Cognitive ability predicts abstract performance. | Weak link between ability and deontic tasks. | Full text not read; a later review says "mostly the same direction" (d18). |
| Context-dependent control in one network | Lampinen, Dasgupta et al. 2024 | One transformer shows biased and consistent behaviour depending on prompt and difficulty, so no separate symbolic system is needed (a24). | Content effects in LMs resemble the human pattern. | Speculative reading (a24). |

### 2.3 Who disagrees with whom, in one view

Three separate debates run at once.

1. Is the cheater result about cheaters or about the question? Cosmides' group says cheater detection is a specialized system (a11, a13). Sperber and Girotto say the cheater instruction names the target category and its two traits, which turns the Wason task into a categorization task; a neutral category does as well (b03, b07). Gigerenzer and Hug sit between: social contract plus a cheating cue plus perspective (d07, d08). All three sides have data the other side explains in its own way (K05 [C]).
2. Is there one general permission/deontic schema or several domain-specific systems? Cheng and Holyoak say schema; Cosmides says several systems and cites Exps 1-2 (a15). Kroger et al. 1993 (the schema group) show permission rules gain only with a violation-checking frame plus explicit negatives (d06) (K07 [C]).
3. What causes the abstract-task error? Matching bias, probability effects, mental models or shallow reading? Fits exist for each (a16, b08, b10) and none is settled (K09 [C]).

What most sources do agree on, from different sides: the answer depends on how the reader takes the rule and what the final question asks, and not only on its logical form (K01, K04 [E]).

---

## 3. Core findings with exact numbers

Status marks: [E] established, [S] single source, [C] contested. "Human" rows are small lab samples; read the N.

| # | Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|---|
| 1 | Abstract Wason: few choose P and not-Q | under 10 percent usually; 5 to 30 percent across studies; Klauer: "typically fewer than 10 percent", about 75 percent inference and 25 percent guessing, 16 of 18 data sets fit, six online experiments of about 300 each | Wikipedia, Cosmides 2010, Klauer 2007 (a29, a11, b10) | [E] K01 |
| 2 | Unfamiliar social contract with cheater cue beats abstract and descriptive | Cosmides 1989 Exp 1/2 (n=24 each): social contract 75 / 71 percent, unfamiliar descriptive 21 / 25, abstract 25 / 29, familiar descriptive 46 / 38. Exps 5-6 (n=40): 75 and 80 vs permission without cost-benefit 30 and 45 | Cosmides 1989 (d03, d04) | [E] K03 |
| 3 | Switched contracts flip the choice to not-P and Q | Exps 3-4 (n=24): 67 and 75 percent. Exps 8-9 (n=40): 65 and 80 percent vs 0 and 10 for the switched non-social-contract rule | d04 | [E] K03, one lab for the n |
| 4 | An independent lab finds the same direction, larger | Gigerenzer and Hug (n=93): cheating 94 percent vs no-cheating 44. Permission rules +33 points, obligation rules +44 with a cheating cue. Social contract without the cue about 45 percent, the same as non-social rules (44) | d07 | [E] K03 |
| 5 | Perspective flips the cards | Day-off rule: employee view P and not-Q 75 percent, employer view not-P and Q 61. Pension rule (n=93): P and not-Q 70 vs 11; not-P and Q 0 vs 64. Subsidy: 81 vs 17 and 59 vs 0 | Gigerenzer and Hug (d08, a09, b02) | [E] K04 |
| 6 | The final question steers the choice | Sperber and Girotto Exp 2 (N=120, 30 per cell): "see whether anyone cheated you" 33 and 43 percent P and not-Q vs "made an exchange with you" 10 and 0. Fiddick Exp 3 (N=120): same poison-dart rule 70 percent P and not-Q when asked about risk, 5 when asked about abusing a privilege | b04, b01 | [E] K04 |
| 7 | Same descriptive rule, goal changed to precaution | 16.7 vs 50.0 percent P and not-Q (n=30 per cell), rule text identical | Fiddick et al. 2000 (d29) | [S] K23, K31 (advocate lab) |
| 8 | A neutral target category does as well as cheaters | Sperber and Girotto Exp 1 (N=100, 35/35/30): cheater 68 percent, arbitrary category ("Wason's selection") 91, glider 73. Cheater vs arbitrary chi2(1,N=70)=4.37, p<.05. Replication of glider group N=20: 65 | b03 | [C] K05 |
| 9 | Cheater detection needs three factors (Cosmides' reading) | Exp 4 (2x2x2): 64 percent with benefit, intention and ability; 46 with two; 26 with one; 26 with none. F(1,342)=7.30, 10.22, 4.87. Exp 1 (N=25 per rule): 80, 52, 44; precautionary garbage 72. Exp 2: 72 vs 48, 32. Exp 3: 68, 45, 27 | Cosmides et al. 2010 (a12, a13, critique) | [S] (additive factors from one paper) |
| 10 | Abstract permission schema (second hand) | 61 percent vs 19 for a nondeontic rule (Cheng and Holyoak 1985 Exp 2, first problem only, N unknown; read via Cosmides) | d05, a03 | [C] K07 |
| 11 | Permission schema needs frame and negatives | Kroger et al. Exp 1A: violation-checking plus explicit negatives: permission 47 percent (n=38) vs arbitrary 5 (n=40), chi2(1)=18.35. Without negatives: 18 (n=45) vs 8 (n=40) n.s. Hypothesis-testing frame: 16 vs 6. Exp 2 (131 students): 22 vs 6 | d06 | [C] K07 |
| 12 | Abstract deontic rules are hard | Fiddick (n=20 per group): precaution 50, social contract 45, obligation 30, permission 20, situation control 15, action control 10. Adaptive pooled 48 vs deontic 25. h=.83 (social contract vs action control), h=.93 (precaution) | a04 | [S] K08 |
| 13 | Relevance manipulations move descriptive rules | Exp 1 (n=27 within): 78 vs 26 percent. Exp 2 (17 / 19): 65 vs 16. Exp 3 (20 per cell): 70 vs 25. Exp 4 (n=21 per cell): effect+/effort- 57, effect+/effort+ 38, effect-/effort- 38, effect-/effort+ 5 | Sperber, Cara, Girotto (d09, d10) | [S] K06, K23 (authors of the theory) |
| 14 | Deontic rule "no longer in force" gives the descriptive error | Cholera rule: 62 percent P and not-Q in force; 15 percent when not in force, 71 percent P and Q | b06 (cited) | [S] K06 |
| 15 | Spelling out necessity and sufficiency helps | Ahn and Graham (n=22): 50 percent P and not-Q for unnecessary-but-sufficient vs 18 control; abstract rules 50.0 percent normative over explicated conditions vs social 57.1 | d11 | [E] K19 (with d06, d12) |
| 16 | "Necessarily follows" cuts belief bias in people | Macchi et al. (N=130): invalid-believable correct 4 percent (untrained), 10 (trained) with "follow"; 66 and 77 with "necessarily"; 41 and 67 with "criteria of logic" | d12 | [E] K19 |
| 17 | Goal framing alone | Same descriptive rule 16.7 vs 50.0 (row 7). Trade problem with no if-then and no modal: 50.0 percent (want) vs 66.7 (conditional), n=30 each, Z=1.31 n.s. | d28, b01 | [S] K31 |
| 18 | Slow responders show the realistic advantage | N=625 plus 360. Slowest 15 percent (over 80 s) above chance on realistic rules, near chance on others. z=4.44 for time vs accuracy. A bonus changed nothing | a22, b13 | [S] K15 |
| 19 | Fast belief, slow logic in humans | Modus ponens, conflict vs no conflict: belief judgments .63 vs .93, logic judgments .73 vs .97; MT .67 vs .91 and .69 vs .86; overall .68 vs .92. For three-term complex syllogisms belief interfered more with validity | Trippas 2017 (d33) | [S] K32 |
| 20 | Cognitive ability and selection | Over 800 participants; abstract tasks tied to ability; two deontic tasks not (abstract only; later review says "mostly same direction") | d18, b21, a18 | [S] K17 |
| 21 | Hidden-possibility hints | A hint to consider every hidden side lowered the irreversibility parameter; correct selections rose "modestly" | Klauer 2007 (b11) | [S] K10 |
| 22 | LLM content effects (old models) | Syllogisms: significant belief advantage in humans and all five models (z>=2.25). Wason: realistic > arbitrary for Chinchilla, PaLM 2-L, GPT-3.5 (z>2.2) and humans; PaLM 2-M and Flan-PaLM 2 marginal (p about .08). NLI: no content effect (all p>.2) | Lampinen et al. (a20, c01) | [E] K11 |
| 23 | Item-level match to humans | Items humans got right are the items models got right: NLI t(832)=3.49, syllogisms t(345)=4.98 | a21 | [E] K11 (one paper) |
| 24 | Belief-inconsistent items are hardest | NeuBAROCO GPT-3.5: symbol 61.05, consistent 56.89, inconsistent 31.37 (95/167/102 items). LLaMA-3 8B valid believable 70.74 vs unbelievable 52.59 | b17, a25 | [E] K11 |
| 25 | Belief gap in 2025-2026 models is uneven | Congruent minus incongruent: Llama 3.2 3B +46.9, Llama 3.3 70B +31.6, Qwen3-Next Thinking +28.0, Gemini 2.5 Pro +1.4, Gemini 2.5 Flash +0.9, GPT-OSS-20B +0.8, Qwen3-Next Instruct -7.9. Mean +10.81, d=0.66, 12 of 14 positive | Poddar (d01) | [C] K21 |
| 26 | LLM deontic advantage on Wason | +5 to +45 points over descriptive, every model and prompt. Zero-shot deontic: gpt-oss-120b 100.0, qwen3-32b 98.8, qwen3-14b 97.5 (+45), gemma3-4b 17.5 (+5) | Abe et al. (a28, d02) | [S] K14; confounded (K22) |
| 27 | Few-shot does not fix it | Chinchilla 5-shot: syllogism effect weakened slightly, Wason effect grew. 14 models: few-shot mean 79.1 vs zero-shot 82.7 (paired t41=2.50, p=.0165) | a23, d01 | [E] K12 |
| 28 | Zero-shot CoT cuts the effect in strong open models | Qwen2.5-32B CE 0.348 to 0.096; Qwen3-14B 0.213 to 0.014. Weak LLaMA still loses on unbelievable valid items | b15, a25 | [E] K12 |
| 29 | Counterfactual and symbol versions cost accuracy | FOLIO (81 items) GPT-4 93.8 vs 74.1 no CoT; 98.8 vs 82.7 with CoT. Symbolic Tree ChatGPT/GPT-4 semantics 71.8/90.0 vs symbols 53.7/67.6. Base 10 100.0 vs base 9 23.4 | Wu, Tang (c03, c04, c06) | [E] K36, K25 |
| 30 | Irrelevant clauses and renaming | GSM-NoOp up to 65 percent drop (Phi-3-mini); o1-preview -17.5; best-worst gap over 12 percent (Gemma2-9B) | Mirzadeh (c31) | [E] K16, K25 |
| 31 | Premise order | Shuffled premises: 20-30 points (GPT-4-turbo, PaLM 2-L), over 40 for Gemini 1.0 Pro and GPT-3.5-turbo; R-GSM GPT-4-turbo 94.1 to 85.0 | Chen et al. (c32, d32) | [S] K28 |

---

## 4. Mechanisms and models, written so an engineer could implement them

Each model below is described as a procedure. Items marked "from memory" were not opened in this research and should be checked before they are built.

### 4.1 Permission schema as a violation-finder (Cheng and Holyoak 1985; a03)

Four production rules for a permission rule "if action A is taken, precondition P must be satisfied":

- P1: action taken implies precondition must be satisfied.
- P2: action not taken implies precondition need not be satisfied.
- P3: precondition satisfied implies action may be taken.
- P4: precondition not satisfied implies action must not be taken.

P1 selects the "action taken" card (the P card). P4 selects the "precondition not satisfied" card (not-Q). Code version:

```
def violation_finder(rule):             # rule has: action, precondition, modality in {must, may}
    if rule.modality != "must": return []   # a 'may' rule marks no case as a definite violation (d30)
    return [
      Case("action taken", check="precondition satisfied?"),          # could violate
      Case("precondition not satisfied", check="action taken?"),      # could violate
    ]
```
The test is: for every card or case, can the hidden side make a violation? Select exactly those. This is the same as the material-conditional answer when the rule is a "must" rule, which is why the schema is not separable from logic by accuracy alone (a07).

### 4.2 Social contract and perspective (Cosmides 1989; Gigerenzer and Hug 1992)

Parse the rule as `if you take benefit B then you must pay cost C`. Then:

```
def cheater_cases(rule, perspective):
    # perspective: the party whose interests are checked
    if perspective == rule.benefit_taker_is_checked_against:   # e.g. employer checks employee
        return [Case("took benefit"), Case("did not pay cost")]       # P, not-Q
    else:                                                       # the other side checks
        return [Case("did not take benefit"), Case("paid cost")]      # not-P, Q  (switched)
```
Evidence says three inputs matter: benefit to the violator, intention, ability to pay (a13: 64, 46, 26, 26 percent), and a cue naming whose cheating is checked (d07: 94 vs 44; d08). For the agent this means one fixed slot: *whose violation is checked*. Without it the same rule gives opposite answers (d08: 70 vs 11 and 0 vs 64).

### 4.3 Flexible deontic logic (von Sydow et al. 2005)

Prescriptive rule type (obligation, prohibition) times goal (find breakers, find followers) gives a 2x2 that fixes which cards matter. Reported q-card picks (N=20 per cell): obligation-cheater 20, obligation-cooperator 70, prohibition-cheater 80, prohibition-cooperator 45; not-q: 70, 15, 20, 55 (a08; garbled table, labels matched to the text's predictions). Implementation: a lookup from (rule type, goal) to the card set. A prescriptive rule is never falsified by counterexamples (a10): a law remains a law if many break it. So for "ought" rules the test is violation, not truth.

### 4.4 Relevance theory as two scores (Sperber, Cara, Girotto 1995)

Two factors, separable and additive in the data (d10, n=21 per cell, z=2.5 each, no interaction):

- **Effect**: does the rule suggest a denial, so that a violating case looks worth finding?
- **Effort**: is the not-Q case easy to represent (explicit negative on the card)?

Prompt-side use: write the denial in plain words ("the rule is false if there is a P that is not Q"), and write the not-Q case in positive terms. Gains in the original: 57 vs 5 percent between the best and worst cell (z'=3.6, p<.001). From memory: the theory says people stop at the first reading that is relevant enough; the model of the "violating case" is the stopping point.

### 4.5 Information gain (Oaksford and Chater 1994, 2003; a16)

From memory, standard form. Two hypotheses: M_D (P implies Q, with a small exception rate) and M_I (P and Q independent). Rarity assumption: p=P(P) and q=P(Q) are small. For each card, expected information gain = prior entropy of {M_D, M_I} minus the expected posterior entropy after turning the card. Choose cards by that gain. Fit reported: 34 meta-analysis studies, mean G2(2)=2.60 (SD 2.55), p>.20; not rejected in 28 conditions of Oaksford et al. 1999, mean G2(2)=3.15; pooled rejection of mental logic and mental models, G2(68)=110.99 (a16). This is a computation the code can do, but it models what people do on descriptive rules, which is not our target (a18 note: "check against logic by code, not against a human norm"). Deontic rules need an expected-utility account, per the authors (a16).

### 4.6 Inference-guessing model (Klauer et al. 2007; b10)

Each response pattern (16 in all) arises either from inference (about 75 percent) or from independent guessing per card (about 25 percent). Inside inference, only about 10 percent is "reversible" (the hidden side is considered). Targeted fix: ask the solver to consider the hidden side for each card. Reported effect is small (K10).

### 4.7 mReasoner (Eisape et al. 2024; c10; from Khemlani and Johnson-Laird, not opened)

Four parameters: LEN (entities built, range 2.0 to 4.5), BROAD (width of the sampled set, 0 to 0.9), SYSTEM2 (chance of searching for a counterexample, 0 to 0.9), WEAKEN (chance of weakening a too-strong conclusion, 0 to 0.9). Procedure: build a small model, draw a quick conclusion, then with probability SYSTEM2 search for a counterexample, then with probability WEAKEN weaken the conclusion. The counterexample search is an operator we can run in code.

### 4.8 Pipeline models used with LLMs

- **Form extraction then judge** (Proofbusters, ITLC): normalise the syllogism to canonical form, then judge by rule or prover. Set-notation reached 98.95 percent accuracy with CE 2.13 against Gemma3-7B direct 71.70 (d19); a strong model asked directly already scores 98.43 with CE 2.13 (d21).
- **Logic-LM** (c25, c26): the LLM translates, a solver (Prover9, Z3, python-constraint, pyke) infers, solver errors feed a refinement loop. GPT-4 FOLIO 78.92 vs CoT 70.58; ProofWriter 79.66 vs 68.11; but PrOntoQA 83.20 vs CoT 98.79. Gain over CoT grows with depth: +7.1 at depth 0 to +39.4 at depth 5.
- **FregeLogic tiebreaker** (c23, c24, d20): five LLM classifiers vote; only on 3-2 splits (7.9 percent of items, 76 of 960) a Z3 call breaks the tie. 94.3 vs 93.4 percent; CE 2.85 vs 3.39; Z3 overrode 30 votes, 19 correct, 11 wrong; about 4,300 tokens and 6 calls per item. Z3 as a veto fell to 74.1.
- **Step-Back** (c30, d31): ask what principle applies, then answer. Over zero-shot CoT: PaLM-2L +8.2 Physics, +6.5 Chemistry; GPT-4 +1.6 and +0.3 (sd 0.5-1.5); StrategyQA -0.9.
- **QuaSAR** (d15): name variables and predicates, rewrite in quasi-symbols, explain, answer. GPT-4o over CoT: GSM8K 94.5 to 96.5; SVAMP 90.3 to 97.0; GPQA 50.2 to 55.4. Hurts 1B-8B models. No token count.
- **Faithful CoT** and **SatLM** (c29, c28): the chain is code or constraints that a solver runs, so the shown chain is the cause of the answer. Gains over CoT +6.3 percent math, +3.4 planning, +5.5 multi-hop, +21.4 relational (c29). SatLM GSM-SYS 69.4 greedy, 80.9 with self-consistency.

### 4.9 Inside the model (not reachable by a text scaffold)

Validity and plausibility are aligned linear directions (cosine 0.48-0.64 vs 0.10-0.17 for controls); the more aligned, the bigger the content effect. A debias vector cut CE from 0.348 to 0.072 (Qwen2.5-32B) (a27, b15, c17). A conditional steering method (K-CAST) gives up to 15 points (c18). Steering toward the "abstract version" activation lifted bias-penalised accuracy from an average 58.1 to 97.0, while zero-shot CoT reached only 72.0 (d25). The circuit for abstract syllogisms works on symbolic data and fails when world-knowledge heads inject beliefs (c19). Use: this explains why "ignore plausibility" prompts leave a residual, and why removing plausibility from the input is the text-side equivalent. It cannot be done through an API.

---

## 5. What holds up

### 5.1 Replications and independent labs

- **Cosmides 1989 social contract effect.** Cosmides' own range 65 to 80 percent over Exps 1-9 (n=24 or 40) is one lab (d04). The independent Konstanz replication (Gigerenzer and Hug, n=93) found 94 vs 44 percent, in the same direction and larger (d07). Fiddick, Cosmides, Tooby claim "scores of replications" without listing numbers (advocate source, d30/critique). Seals and Shalin reproduce the switched-contract drop in 7B models (d27). Verdict: the direction replicates [E]; the exact size (65-80) is not a cross-lab estimate.
- **Cheng and Holyoak 1985.** The 61 vs 19 figure was never read in the primary paper; it comes via Cosmides (d05). Kroger et al. (same group) show a fragile effect: it needs a violation-checking frame and explicit negatives, and gives 47 vs 5 only then (d06). Jackson and Griggs (1990) and Noveck and O'Brien (1996) called the effect fragile (a03).
- **Sperber and Girotto vs Fiddick, Cosmides, Tooby.** The conditional-version cheater cell did not replicate: 33 percent vs Fiddick's 66, "no confident explanation" (b04). Not independent: same Trieste lab across 2002 and 2003 (b07).
- **Relevance results** come from the theory's authors (Paris, Trieste, Padua students, n=17 to 27 per cell, d09, d10). The cross-lab check is Fiddick's 16.7 vs 50.0 goal change, which the Cosmides group reads as hazard management (d29).
- **Oaksford and Chater probability effects**: Oberauer et al. (1999) report failed replication; the original authors answer that realistic materials bring priors that override the manipulation (a19).
- **Lampinen et al.** (the LLM paper): humans overall near chance on Wason (forced two-card choice online); the realistic advantage lives in the slowest 15 percent. A bonus sample showed no difference (a22, b13). The paper's NLI result is a null (all p>.2).

### 5.2 Meta-analyses

- Ragni, Kola, Johnson-Laird (2018): 228 selection-task experiments, 16 theories; model theory kept, 14 of 15 rivals eliminated; counterexample salience corroborated; "no findings so large or so robust" (b08). Original abstract selections pq 46 percent, p 33, pq-bar 7, other 4. Online studies (N=3787) more idiosyncratic. Effect sizes (Table 4) not obtained. Contested by Kellen and Klauer (b24, snippet only).
- Oaksford and Chater (2003): fit over 34 studies (a16).
- Klauer et al. (2007): fits 16 of 18 data sets (b10).

### 5.3 Boundary conditions and moderators

- **Content must make a violation salient.** Realistic content alone is not enough (K02). The permission schema works only in a regulation-like context (d05, Holyoak and Cheng 1995).
- **Explicit negatives and a violation frame** matter together (d06); the same tricks do nothing for arbitrary rules (Kroger: 5 and 8 percent).
- **Violation instructions are not universal.** They helped a thematic permission rule but not obligation or abstract rules (Valina et al., instruction by content interaction, d17). Platt and Griggs' roughly 80 percent abstract result needed an explained rule and a request for reasons (second hand); the schema authors dispute how Platt and Griggs read their cost-benefit result (d30, d17).
- **Complexity.** Belief wins over logic mainly on the most complex syllogisms (d33).
- **Ability.** Strong in abstract tasks, weak in deontic (abstract only, d18).
- **Familiar vs unfamiliar.** Cosmides: no difference between familiar and unfamiliar contracts (a11). Familiar descriptive rules score 46 / 38 (d03).
- **Modal word and if-then.** In humans, the effect survived with no rule and no modal (66.7 vs 50.0, n.s., d28), but schema theory treats must vs may as a mechanism (d30).
- **Accidental vs intentional.** Social-contract detection falls for accidental violations; precaution detection does not (a14).

### 5.4 Interventions: what worked and what did not (humans)

Worked: make the logical relation explicit (50 vs 18, d11); "necessarily follow" wording (4-10 to 66-77 percent, d12); violation frame plus explicit negatives (47 vs 5, d06); goal change (16.7 to 50.0, d29); relevance story (78 vs 26, d09); perspective cue (94 vs 44, d07).
Did not or only partly worked: considering all hidden possibilities (modest, b11); "judge only logic" left a conflict cost of .17 to .24 (d33); violation instructions on abstract rules (d17); logic training alone without the key phrase (4 and 10 percent, d12); a performance bonus (a22).

---

## 6. Language models

### 6.1 Core pattern

LLMs reproduce the human content effects on three tasks (c01, a20): NLI (no content effect, all p>.2), syllogisms (belief effect in all five models and humans, z>=2.25), Wason (realistic > arbitrary for Chinchilla, PaLM 2-L, GPT-3.5, z>2.2; marginal for PaLM 2-M and Flan-PaLM 2). New stimuli were written to avoid contamination (12 realistic, 12 arbitrary, 12 nonsense Wason rules, c01). Item-level human-model match is significant (a21). Instruction tuning made no consistent difference (a22). Scoring was prior-corrected log-probability over fixed answers, not free generation (c01); PaLM 2-L is above 75 percent in every Wason condition under that scoring (a23). Exact accuracies appear only in figures.

### 6.2 How large is the effect now

| Model class | Belief or deontic gap | Source |
|---|---|---|
| GPT-3.5 on NeuBAROCO | consistent 56.89 vs inconsistent 31.37 | b17 |
| LLaMA-3 8B (base) valid syllogisms | believable 70.74 vs unbelievable 52.59 | a25 |
| LLaMA-2-inst 7B | 32.22 vs 19.26 | a25 |
| LLaMA-3 70B-inst | 54.44 vs 57.41 (no loss) | a25 |
| Llama 3.3 70B | congruent minus incongruent +31.6 | d01 |
| Qwen3-Next 80B Thinking | +28.0 (86.3 vs 58.3) | d01 |
| Gemini 2.5 Pro / Flash | +1.4 / +0.9 | d01 |
| GPT-OSS-20B | +0.8 | d01 |
| GPT-4o on BIS (valid, belief-inconsistent only) | 79.54; GPT-5-mini 99.72; GPT-5-nano medium 98.84 vs minimum 69.22 | d13 |
| SemEval baselines (CE in points) | Qwen3 14B 97.38 / 4.23; Qwen3 8B 95.81 / 4.23; Phi-4 15B 83.33 / 14.89; Qwen2.5 14B 67.50 / 44.54; Gemma3 7B 71.70 / 29.75; Llama 3.1 8B 64.17 / 32.15 | d23 |
| Strong model direct (Gemini 3 Flash) | 98.43, CE 2.13 (n=192); after normalise+parse 100, CE 0.0 | d21 |

Reading: the effect is large in old and mid-size models and near zero in the best current models on plain syllogisms. It does not follow size or the word "thinking": Qwen3-Next Thinking is at +28.0 while its Instruct sibling is at -7.9 (d01; different checkpoints; majority-vote adaptive stopping). Model generation and reasoning training seem to matter more than size (d23, K21 [C]). Poddar's formal accuracy (81.7 mean) far exceeds believability judging (56.2), and top models give the same answer on natural and nonsense versions (consistency 99.2, Gemini 2.5 Flash) (c20).

### 6.3 What changed it, and by how much

| Lever | Result | Source | Verdict |
|---|---|---|---|
| Few-shot examples | Chinchilla 5-shot: syllogism effect only slightly weaker, Wason effect larger. 14 models: 79.1 vs 82.7 zero-shot. Llama 4 Maverick CE 3.83 to 10.11 with few-shot CoT | a23, d01, d20 | does not fix; can hurt [E] K12, K40 |
| Simple instruction | On NLI "substantially reduced" bias; Chinchilla near ceiling with a few examples | a24, d35 | works on easy tasks |
| Zero-shot CoT | Qwen2.5-32B CE 0.348 to 0.096; Qwen3-14B 0.213 to 0.014. BPA average 58.1 to 72.0 for 7B-14B models (Qwen-2.5-7B 50.8 to 81.7; Gemma-2-9B 51.8 to 69.9; Mistral-7B 30.2 to 34.3) | b15, d25 | cuts a lot in strong open models; residual in weak ones [E] K12, [S] K33 |
| Thinking effort | GPT-5-nano 69.2 (minimum) vs 98.8 (medium). Qwen3-32B 99.58 without thinking vs 99.12 with | d13, d24 | two-level contrast only; no sweep [S] K15 |
| Logic-focus prompt that names the conflict | Of 100 GPT-4o failures: basic 5, casual 3, polite 65, focus-logic 76, CoT 87 percent recovered | d14, c22 | errors-only, unequal length [S] K20 |
| Human-style debiasing instruction (counterexamples) | Rule-discovery task: success 42 to 56 percent, but Qwen3-32B thinking tokens per turn about 1,030 to 1,450 | d34 | helps but costs tokens |
| SFT | LLaMA-3 8B reaches about 96 percent, CE 4.68 percent | a25, c16 | training; outside our scheme |
| Activation steering | CE 0.348 to 0.072; BPA 97.0 average; up to +15 points | c17, d25, c18 | needs weights |
| Extract the form (small and mid models) | Qwen3 4B Thinking FOL plus prover 95.83 vs 84.17 direct; LLM-as-prover on the same formulas 79.22 (CE 20.21) | d22 | helps weak models [C] K18 |
| Z3 as tiebreaker | +0.9 accuracy, net +8 of 960 items, inside one sd | d20 | tiny [S] K29 |
| Z3 veto or Z3 alone | 74.1 and 74.7 vs 93.4 ensemble | d20, c24 | harmful [E] K37 |
| Translate to logic then explain (GPT-4) | translation 96.67 correct; final 77.78 to 83.33 (predicate), 80.00 (set); GPT-3.5 no gain | c12 | small |
| Binary validity format | 'nothing follows' accuracy from near 0 to markedly higher | c09 | [E] K34 |
| Step-Back / QuaSAR | small over CoT on strong models; hurts small ones | d31, d15 | [S] K26 |

### 6.4 Wason with current open models (Abe et al., a28, d02, d26)

Nine open models, 160 problems (80 deontic, 80 descriptive; 20 per polarity), temperature 0 for non-reasoning models, exact-match multi-select. Zero-shot deontic accuracy (gain): gpt-oss-20b 67.5 (+27.5), gpt-oss-120b 100.0 (+30), qwen3-14b 97.5 (+45), qwen3-32b 98.8 (+38.8), gemma3-4b 17.5 (+5), gemma3-12b 58.8 (+30.1), gemma3-27b 77.5 (+38.7), llama-3.3-70b 62.5 (+10), olmo-2-32b 36.2 (+15). Few-shot: gpt-oss-20b 91.2 (+41.2). CoT: llama-3.3-70b 83.8 (+38.8). Errors on deontic rules fit matching bias better than confirmation bias. Selection rates for gpt-oss-20b zero-shot on deontic rules (TA/FA/TC/FC): pos-pos 100/0/45/55; pos-neg 100/0/5/95; neg-pos 80/20/60/40; neg-neg 90/10/10/90. The text says the gain range is 5.0 to 41.2; Table 2 shows +45 (critique correction).

The comparison is not a paired rewrite. Deontic items are everyday norms with "must / must not / need to / not allowed"; descriptive items are arbitrary if-then rules with no modal. Content, modal word and format change together (d02, d26). Permission and "need not" rules were left out. So the LLM deontic advantage cannot be split into content vs "must" (K22).

### 6.5 Other LLM findings

- Macmillan-Scott and Musolesi: the facilitated Wason did not help seven models like it helps people; highly inconsistent over ten runs; one Bard answer reasoned correctly and stated the wrong letter (c13). Reasoning text and final answer can disagree (supports G10).
- Seals and Shalin (7B-class, 70 social and 70 non-social problems): realistic vs shuffled OR 1.30 [1.05-1.62]; social rule x content interaction OR 1.59 [1.26-2.02]; switched social rules below standard; models solve social problems about 30 percent vs 70 for people (c14, d27).
- Eisape et al.: PaLM 2 more logical than people but best about 75 percent; nearly 0 on "nothing follows" under CoT; Llama 2 similar to humans (c09, b16).
- Bertolazzi et al. 2024: pretrained models almost never say "nothing follows"; ICL raises accuracy on valid forms but makes answers more contradictory (c16).
- Wu et al. and Tang et al. show the same family of effects outside syllogisms: counterfactual worlds and symbols cost accuracy (K36, K39).
- BIS Reasoning: Claude 3 Sonnet 20.34 and Opus 7.18 on belief-inconsistent Japanese syllogisms but 78.44 and 61.07 on NeuBAROCO (c21). Deprecated models; a 7 percent score on a binary task implies format failure or systematic error.
- Search note: no LLM study of cheater detection, Cheng-Holyoak schema prompts or relevance theory was found in about 8 + 3 targeted searches (c35, d-pass). Absence is not proof.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory, H harness. Status marks as in the schema. "Evidence" lists claim ids and evidence ids.

### 7.1 Add now (established)

| # | Item | Schema part | Mark | Evidence |
|---|---|---|---|---|
| A1 | **Fix answer format, scoring code and seeds before comparing any two arms.** Direction of content effects is stable across scoring; size is not. Report spread with every gap. | H, G7 | [E] | K41; c02, c09, c13, d01 |
| A2 | **Test the final answer on a renamed or counterfactual copy** of the item and flag any flip. Models lean on stored knowledge and on familiar surface. | G3, S8 | [E] | K36, K25, K16; c03, c04, c06, c08, c31, b19 |
| A3 | **Ask categorical validity as a binary check per candidate conclusion, scored in code**, instead of "what follows". Always include the "nothing follows" option. | S3/S4, G5 | [E] | K34; c09, b16, c16 |
| A4 | **Never make step-by-step or few-shot the default.** Add reasoning only on a signal (this restates G1, G11). Few-shot lowered accuracy and raised content effect in several tests. | G1, G11 | [E] | K40, K12; c05, c07, d20, d01 |
| A5 | **Gate any belief-debias step on a measured gap for the model in use.** For strong models the headroom on plain syllogisms is about two points (98.43, CE 2.13). Do not add it as a default. | S0 gate, G7, G12 | [E] | K30, K21 [C]; d21, d19, d22, d23 |
| A6 | **If a solver is used, never as a veto and never alone.** Translation is the weak link; solver-only fell to 74.1-74.7 percent. Keep fallback to the plain answer (G6). | O (formalise-and-check) | [E] | K37; c12, c24, c27, d20, d22 |
| A7 | **Do not build a cheater-detection module or a permission-schema operator.** The theories are contested; they depend on the question and on rule reading. This matches 4b (do not hard-code a theory). | none | [C] negative | K05, K07, K08, K09; b03, d06, a15 |
| A8 | **S1 restate slot: put the goal and whose violation is checked into the one-sentence restatement.** Fixing perspective and final question is established in humans (K04, K19). This costs no extra call because S1 already restates. It stays only if A/B test T1 passes (G7). | S1 | [E] in humans, [S] for LLMs | K04, K19, K20, K23, K31; b04, d07, d08, d11, d12, d29 |

Check against 4b. The schema says "do not add debiasing instructions or bias checklists" [E]. A8 is a task restatement (name the violation case, the goal, what is needed vs enough), not a debias reminder, and its human evidence is strong (K19 [E]). But the only LLM evidence is single-source and unequal in tokens (K20). So A8 is allowed only as wording inside S1, and it must be tested against a "be logical" control arm and a plain arm (T1). If it ties, drop it.

### 7.2 Test first (single-source, contested, or untested for LLMs)

| # | Item | Schema part | Mark | Evidence |
|---|---|---|---|---|
| B1 | **Violation-naming restatement vs "be logical" vs CoT vs plain**, equal tokens, congruent and incongruent items. Human support is strong; LLM support is one errors-only test. | S1, O | [S] | K19 [E] human, K20 [S]; d14, d29, d11, d12 |
| B2 | **Rule typing before the violation step.** Sort the rule as descriptive (test truth, look for counterexample) or prescriptive (look for violators) and apply the step only to prescriptive or exchange-like rules. Not tested anywhere; violation framing helps only some rule types. | S1 | [S] | K24, a08, a10, d17 |
| B3 | **Hidden-side enumeration and falsifier search.** "For each case, what could be on the other side; which case would show the rule false." Human gain modest; relevance gains large (57 vs 5). | O (enumerate), S7 counterexample | [S] | K10, K23; b11, d10, b09 |
| B4 | **Form extraction (canonical form or placeholders, then map back).** Contested: big gain for small and mid models, about 2 points for strong ones, can hurt small models with prompts only. | O6 change representation | [C] | K18, K39, K26; d19, d21, d22, d15, c06 |
| B5 | **Formalise-and-check as a tie-break** when two independent passes disagree. Gain was +0.9 points at about 4,300 tokens per item. | S7 select | [S] | K29, K27; d20, c23 |
| B6 | **Premise reordering into dependency order.** Order matters 20 to over 40 points; no reorder step has been tested. | S1 | [S] | K28; c32, d32 |
| B7 | **Complexity-scaled checking.** Belief gains ground on complex problems in humans. Scale the check with item complexity. | S0, G12 | [S] | K32, K15; d33 |
| B8 | **Thinking-budget sweep on belief items with congruent controls.** Only two-level contrasts exist. | S3, G11, G12 | [S] | K15; d13, d24 |
| B9 | **Deontic rewrite**: restate an indicative rule as an obligation or prohibition before testing. Large LLM deontic gaps exist, but they are confounded with wording and format. | S1, O6 | [S] | K14, K22; a28, d02, d26 |
| B10 | **Consistency over repeated runs as the doubt signal.** Content-driven low confidence is not an error signal on valid-unbelievable items. | G1, G4 | [S] | a21, c13 |

### 7.3 Do not take

Representation steering, SFT, and the Bertolazzi/Valentino/Maraia methods (K13, K38, K18): they need weights. Human "ability moderation" (K17) until the full paper is read. The 5-factor cheater result (K03 factors) as a design target (single source).

---

## 8. Concrete tests on our bench

Common rules. Use the `bench` harness. Each test has arms at equal total tokens (count all calls, setup included, G7). Fix the answer format and scorer (A1). At least 3 seeds. Report the gap with a spread. Run on one weak, one mid and one frontier model (the critique calls for this, and the gap differs by model). Free-text final answer parsed by code; no log-probability scoring.

**T1. Violation-naming restatement (B1, A8).**
- Items: 40 abstract conditional-test (Wason-style) items, written as 4 polarity patterns x 10 contents (abstract, arbitrary-but-concrete, realistic-neutral, deontic). Add 100 syllogisms congruent and 100 incongruent (valid x believable cells balanced).
- Arms (same token budget, matched by padding or by capping): plain; "be logical" instruction; CoT; violation-naming restatement (name the violating case, whose violation, what is needed vs enough) with a short answer; the restatement plus CoT.
- Metric: exact card set (Wason); accuracy and CE = acc(congruent) - acc(incongruent) (syllogisms).
- Expected: human data say +30 to +50 points on abstract rules (d11, d29). For a frontier model, little headroom (K30). The restatement arm should beat "be logical" on abstract Wason items and tie CoT at fewer tokens (d14: 76 vs 87). If it does not beat "be logical", drop A8.

**T2. 2x2 content x modal word (B9, K22).**
- Items: the same four-card logic written as norm content vs arbitrary content, each with "must / must not" or plain "is / is not", plus one cell that changes only the final question (look for violations vs test the rule), plus a switched-contract item and a "may" rule. 20 problems per cell.
- Arms: plain; CoT.
- Metric: exact card set; matching-bias rate (cards named in the rule).
- Expected: if the deontic gain (+5 to +45) is content, the content main effect survives with no "must"; if it is wording, the modal main effect carries it. Humans: the content effect survived with no rule (66.7 vs 50.0, n.s., d28).

**T3. Belief gap and thinking budget (B8, A5).**
- Items: 160 syllogisms from the Poddar design (40 base x natural/nonsense x order-switched; d01): congruent and incongruent, valid and invalid.
- Arms: direct; budgets at 4 levels (e.g. 0, 256, 1k, 4k thinking tokens) on one mid model; the same on one frontier model.
- Metric: CE vs total tokens; also flip rate natural vs nonsense.
- Expected: gap near 0 on frontier at any budget; mid-size gap falls with budget (GPT-5-nano 69.2 to 98.8 shows a lever; Qwen3-Next Thinking at +28.0 warns it is not guaranteed).

**T4. Natural vs nonsense-renamed copy (A2, B4).**
- Items: 100 syllogisms and 100 FOLIO-style items, each with a renamed copy (nonsense nouns) and a counterfactual copy.
- Arms: plain; plain + "answer on the renamed copy and compare" check; form-extraction then answer.
- Metric: accuracy by copy; flip rate; tokens.
- Expected: flip rate near 0 on strong models (consistency 99.2, c20); larger on weak ones; symbol-only rewriting may lower accuracy for weak models (c06: 71.8 to 53.7).

**T5. Binary check vs "what follows" (A3).**
- Items: 64 syllogism forms x 3 content triples.
- Arms: generative "what follows?"; binary "does conclusion X follow?" for each of the 9 candidate conclusions plus "nothing follows", scored in code.
- Metric: accuracy overall and on "nothing follows" forms.
- Expected: near-0 vs markedly higher on "nothing follows" (c09).

**T6. Tie-break by solver vs by second pass vs more thinking (B5).**
- Items: 960 syllogisms (balanced, as in FregeLogic) or a 200-item subset.
- Arms: 5-vote ensemble; ensemble + Z3 tie-break on 3-2 splits; ensemble + one more LLM pass on 3-2 splits; one strong pass with a thinking budget equal to the ensemble's token total (about 4,300 per item).
- Metric: accuracy, CE, tokens.
- Expected: tie-break +0.9 inside one sd (d20); the single strong pass at equal tokens may match or beat it. This is the comparison that is missing.

**T7. Premise reorder (B6).**
- Items: 100 deductive items with the proof order known; shuffled version.
- Arms: shuffled plain; shuffled + "list premises in dependency order first" step; original order (ceiling).
- Metric: accuracy; tokens.
- Expected: shuffling costs 20 to 40 points on older models (d32); a reorder step recovers part of it only if the model finds the proof order (the hard part).

**T8. Rule typing gate (B2).**
- Items: 60 mixed rules: descriptive generalisations, obligations, exchange rules, precautions, with the same question.
- Arms: always apply the violation step; apply it only if the model labels the rule prescriptive; never apply it.
- Metric: accuracy by rule type; rate of mis-typing.
- Expected: the violation step helps prescriptive rules and may hurt descriptive ones (d17, a10).

**T9. Seeds and stability (A1).**
- 10 runs per item on the Wason set (as Macmillan-Scott), report agreement. Expected: free-text answers vary; the schema should reduce variance if it helps.

---

## 9. What does not transfer, and why

- **Evolutionary claims** (domain-specific modules for cheating, hazards) concern human adaptation. A language model has no such history; the cheater result can be re-read as a question-reading effect (b03). We use only the practical part: state the goal and the party.
- **Cheater, contract and social factors** (benefit, intention, ability, K03) were measured with n=25 per cell by one lab. No LLM test exists (c35). Do not code them.
- **Permission schema production rules** are equivalent to the logical answer for "must" rules. They do not add a new operator beyond "find the violating cases" (4.1).
- **Human response-time effects** (slow responders) do not map to token count one to one (a22). In LLMs, adding tokens did not remove the gap in the one mid-size contrast (Qwen3-Next Thinking, d01).
- **Student sample sizes and tasks.** Most human cells are 17 to 35 people (critique). Effect sizes are suggestive, not planning numbers.
- **Old-model LLM results.** Chinchilla, PaLM 2, GPT-3.5, Llama 2 and 7B models (a20, c14, b17) were scored by log-probability. Current reasoning models are near ceiling on deontic Wason (97.5 to 100, a28) and near zero belief gap at the top (d01). The content effect on current frontier models on classic tasks may be small; the practical risk has moved to mid-size models and to messy real tasks.
- **Weight-level methods** (steering, SFT, circuit edits) cannot run through an API (K13, K38).
- **Absolute scores** across papers cannot be compared: scoring, languages, prompts and item sets differ (K41). BIS is Japanese, valid-unbelievable only. SemEval scores are participant-reported under different prompts (d23).
- **Math and logic benchmarks** (GSM-Symbolic, PrOntoQA, FOLIO) are form-sensitivity tests, not human-style belief effects. They support the rename-and-recheck test but not a claim of human-like bias.
- **Self-reported reasoning.** Reasoning and final answer can disagree (c13); G10 says decide from outputs.
- **Human "think harder" instructions.** "Judge only logic" left a conflict cost (d33); the schema already says not to add careful-thinking prompts (4b). Only wording that names the violation or "necessarily follows" is a candidate.

---

## 10. Open questions

Ordered by value (from the critique's second pass, with additions).

1. Does a violation-naming restatement beat plain CoT and a "be logical" control at equal tokens on current LLMs? No equal-token test exists (K20, K30). This is the one run that would change the schema.
2. Is the LLM deontic advantage content, the word "must", or format? Needs the 2x2 plus a question-only cell and a switched-contract item (K22). Seals and Shalin did not vary the modal word.
3. Does the belief gap shrink with thinking budget on one mid-size model, with congruent controls? Only two-level contrasts exist (K15).
4. What are the Ragni et al. 2018 Table 4 effect sizes, and do relevance manipulations transfer to LLMs? Paywalled; three searches found no LLM study (K23).
5. What did Cheng and Holyoak 1985 (N per cell), Cosmides and Tooby 1992, Platt and Griggs 1993, Fiddick and Rutherford 2006 and Stanovich and West 1998 actually report? Not read.
6. Is "abstract, solve, map back" worth its tokens against plain CoT on current models? QuaSAR and Step-Back give small gains and no token counts (K26).
7. Is there any evidence that sorting rules as descriptive or prescriptive before reasoning helps, in humans or models? None found (K24).
8. Why does Qwen3-Next Thinking have a +28.0 belief gap while its Instruct sibling is at -7.9 (d01)? One pair of checkpoints, adaptive voting.
9. Does cognitive ability map to model size or reasoning mode as a moderator? Indirect fit only (d18, d23).
10. Is the cheater result mostly a question-reading effect? Both camps have data the other explains (K05).
11. Can a solver beat one strong pass with more thinking at equal tokens? Missing comparison (K29, d20).
12. Do results hold with free-text output and reasoning models on the classic tasks? Most studies use log-probability or exact-match with fixed formats (K41).
13. Duplicate-number caution: ITLC Table 1 "syllogism notation" (98.95 / 2.13 / 46.23) equals the Proofbusters official row; count as one source until clarified (critique).

---

## 11. Sources

Mark: [V] opened and read this session; [M] snippet, abstract, or second hand only. Evidence ids in brackets point to the files. Some papers have several evidence lines.

- [V] Fiddick (2003) Is there a faculty of deontic reasoning? A critical re-evaluation of abstract deontic versions of the Wason selection task. https://researchonline.jcu.edu.au/9921/2/9921_Fiddick_2003.pdf (evidence: a01, a02, a03, a04, a05, a06, a07)
- [V] von Sydow, Hagmayer, Metzner, Waldmann (2005) Cooperation detection and deontic reasoning in the Wason selection task. https://www.psych.uni-goettingen.de/de/cognition/publikationen-dateien-waldmann/2005_cooperation_detection.pdf (evidence: a08, a09, a10)
- [V] Cosmides, Barrett, Tooby (2010) Adaptive specializations, social exchange, and the evolution of human intelligence. https://pmc.ncbi.nlm.nih.gov/articles/PMC3024027/ (evidence: a11, a12, a13, a14, a15)
- [V] Oaksford and Chater (2003) Optimal data selection: Revision, review, and reevaluation. https://link.springer.com/content/pdf/10.3758/BF03196492.pdf (evidence: a16, a17, a18, a19)
- [V] Lampinen, Dasgupta, Chan, et al. (2024) Language models show human-like content effects on reasoning tasks. https://arxiv.org/abs/2207.07051 (evidence: a20, a21, a22, a23, a24, c01, c02, d35)
- [V] Bertolazzi, Gatt, Bernardi (2024) A systematic analysis of large language models as soft reasoners: the case of syllogistic inferences. https://arxiv.org/abs/2406.11341 (evidence: a25, c16)
- [V] Valentino et al. (2026) Mitigating content effects on reasoning in language models through fine-grained activation steering. https://arxiv.org/abs/2505.12189 (evidence: a26, c18)
- [V] Bertolazzi, Pezzelle, Bernardi (2026) How language models conflate logical validity with plausibility: a representational analysis of content effects. https://arxiv.org/abs/2510.06700 (evidence: a27, b15, c17)
- [V] Abe, Ozeki, Ando, Morishita, Mineshima, Okada (2026) Evaluation of deontic conditional reasoning in large language models: the case of Wason's selection task. https://arxiv.org/abs/2603.06416 (evidence: a28, b18, c15, d02, d26)
- [V] Wikipedia: Wason selection task. https://en.wikipedia.org/wiki/Wason_selection_task (evidence: a29)
- [M] Cosmides (1989) The logic of social exchange: Has natural selection shaped how humans reason? Studies with the Wason selection task. https://doi.org/10.1016/0010-0277(89)90023-1 (evidence: a30)
- [M] Cheng and Holyoak (1985) Pragmatic reasoning schemas. https://doi.org/10.1016/0010-0285(85)90002-0 (evidence: a31)
- [M] Sperber, Cara and Girotto (1995) Relevance theory explains the selection task. https://doi.org/10.1016/0010-0277(95)00666-M (evidence: a32)
- [V] Fiddick, Cosmides & Tooby (2000) No interpretation without representation: domain-specific representations and inferences in the Wason selection task. https://cep.ucsb.edu/wp-content/uploads/2023/05/socexrelevance2000-1.pdf (evidence: b01, b02, d28, d29)
- [V] Sperber & Girotto (2002) Use or misuse of the selection task? Rejoinder to Fiddick, Cosmides, and Tooby. http://www.dan.sperber.fr/wp-content/uploads/2002_girotto_use-or-misuse-of-the-selection-task.pdf (evidence: b03, b04, b05)
- [V] Sperber & Girotto (2003) Does the selection task detect cheater-detection?. http://www.dan.sperber.fr/wp-content/uploads/2003_girotto_does-the-selection-task-detect-cheater-detection.pdf (evidence: b06, b07)
- [V] Ragni & Johnson-Laird (2020) Explanation or modeling: a reply to Kellen and Klauer. https://doi.org/10.1007/s42113-020-00077-9 (evidence: b08, b09)
- [V] Klauer, Stahl & Erdfelder (2007) The abstract selection task: new data and an almost comprehensive model. https://methexp.uni-koeln.de/files/Klauer-Stahl-Erdfelder-2007.pdf (evidence: b10, b11)
- [V] Lampinen, Dasgupta et al. (2024) Language models show human-like content effects on reasoning tasks. https://pmc.ncbi.nlm.nih.gov/articles/PMC11250216/ (evidence: b12, b13, b14)
- [V] Eisape et al. (2024) A systematic comparison of syllogistic reasoning in humans and language models. https://arxiv.org/pdf/2311.00445 (evidence: b16, c09, c10)
- [V] Ando et al. (2023) Evaluating large language models with NeuBAROCO: syllogistic reasoning ability and human-like biases. https://arxiv.org/pdf/2306.12567 (evidence: b17, c11)
- [V] Mirzadeh et al. (2024) GSM-Symbolic: understanding the limitations of mathematical reasoning in large language models. https://arxiv.org/pdf/2410.05229 (evidence: b19, c31)
- [V] Wu et al. (2023) Reasoning or reciting? Exploring the capabilities and limitations of language models through counterfactual tasks. https://arxiv.org/pdf/2307.02477 (evidence: b20, c03, c04, c05)
- [M] Stanovich & West (1998) Cognitive ability and variation in selection task performance. https://www.researchgate.net/publication/228580834 (evidence: b21, d18)
- [M] Cosmides (1989) The logic of social exchange; Cheng & Holyoak (1985) Pragmatic reasoning schemas; Griggs & Cox (1982). https://pubmed.ncbi.nlm.nih.gov/1617917 (evidence: b22)
- [M] Sperber, Cara & Girotto (1995) Relevance theory explains the selection task. https://www.dan.sperber.fr/?p=91 (evidence: b23)
- [M] Kellen & Klauer (2020) critique of Ragni et al. 2018, Computational Brain & Behavior. https://link.springer.com/article/10.1007/s42113-020-00077-9 (evidence: b24)
- [M] Cheater-detection critiques: Fiddick & Rutherford (2006); a 2005 study of cheater-detection contexts; altruism-detection study (2010). https://researchonline.jcu.edu.au/3913/ (evidence: b25)
- [V] Tang, Zheng, Li, Meng, Zhu, Liang, Zhang (2023) Large Language Models are In-Context Semantic Reasoners rather than Symbolic Reasoners. https://arxiv.org/abs/2305.14825 (evidence: c06, c07)
- [V] Saparov and He (2023) Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought (ICLR 2023). https://arxiv.org/abs/2210.01240 (evidence: c08)
- [V] Ozeki, Ando, Morishita, Abe, Mineshima, Okada (2024) Exploring Reasoning Biases in LLMs Through Syllogism: Insights from the NeuBAROCO Dataset (Findings ACL 2024). https://arxiv.org/abs/2408.04403 (evidence: c12)
- [V] Macmillan-Scott and Musolesi (2024) (Ir)rationality and Cognitive Biases in Large Language Models (arXiv 2402.09193). https://arxiv.org/abs/2402.09193 (evidence: c13)
- [V] Seals and Shalin (2024) Evaluating the Deductive Competence of Large Language Models (NAACL 2024). https://arxiv.org/abs/2309.05452 (evidence: c14, d27)
- [V] Kim, Valentino, Freitas (2025) Reasoning Circuits in Language Models: A Mechanistic Interpretation of Syllogistic Inference (Findings ACL 2025; arXiv 2408.08590). https://arxiv.org/abs/2408.08590 (evidence: c19)
- [V] Poddar, Sahoo, Ghosh (2025) Understanding Syllogistic Reasoning in LLMs from Formal and Natural Language Perspectives (v3 Dec 2025). https://arxiv.org/abs/2512.12620 (evidence: c20, d01)
- [V] Nguyen, Tachibana, Liu, Liu, Noe, Takeda, Kurohashi (2026) BIS Reasoning 1.0: The First Large-Scale Japanese Benchmark for Belief-Inconsistent Syllogistic Reasoning (v5, March 2026). https://arxiv.org/abs/2506.06955 (evidence: c21, c22, d13, d14, d24)
- [V] Akinfaderin and Diallo (2026) FregeLogic at SemEval-2026 Task 11: A Hybrid Neuro-Symbolic Architecture for Content-Robust Syllogistic Validity Prediction. https://arxiv.org/abs/2604.18328 (evidence: c23, c24, d20)
- [V] Pan, Albalak, Wang, Wang (2023) Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning (Findings EMNLP 2023). https://arxiv.org/abs/2305.12295 (evidence: c25, c26)
- [V] Olausson, Gu, Lipkin, Zhang, Solar-Lezama, Tenenbaum, Levy (2023) LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers (EMNLP 2023). https://arxiv.org/abs/2310.15164 (evidence: c27)
- [V] Ye, Chen, Dillig, Durrett (2023) SatLM: Satisfiability-Aided Language Models Using Declarative Prompting (NeurIPS 2023). https://arxiv.org/abs/2305.09656 (evidence: c28)
- [V] Lyu, Havaldar, Stein, Zhang, Rao, Wong, Apidianaki, Callison-Burch (2023) Faithful Chain-of-Thought Reasoning (IJCNLP-AACL 2023). https://arxiv.org/abs/2301.13379 (evidence: c29)
- [V] Zheng, Mishra, Chen, Cheng, Chi, Le, Zhou (2024) Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models (ICLR 2024). https://arxiv.org/abs/2310.06117 (evidence: c30, d31)
- [V] Chen, Chi, Wang, Zhou (2024) Premise Order Matters in Reasoning with Large Language Models (ICML 2024). https://arxiv.org/abs/2402.08939 (evidence: c32, d32)
- [V] Saparov, Pang, Padmakumar, Joshi, Kazemi, Kim, He (2023) Testing the General Deductive Reasoning Capacity of LLMs Using OOD Examples (NeurIPS 2023). https://arxiv.org/abs/2305.15269 (evidence: c33)
- [M] Oaksford and Chater (1994) A rational analysis of the selection task as optimal data selection (Psychological Review 101). https://doi.org/10.1037/0033-295X.101.4.608 (evidence: c34)
- [M] Search note (2026-10-20): no LLM study found of Cosmides-Tooby cheater detection, Cheng-Holyoak schemas, or relevance theory. n/a (evidence: c35)
- [V] Cosmides (1989) The logic of social exchange: Has natural selection shaped how humans reason? Studies with the Wason selection task. Cognition 31, 187-276 (Experiments 1-2). https://cep.ucsb.edu/wp-content/uploads/2023/05/socexcog89.pdf (evidence: d03, d04, d05)
- [V] Kroger, Cheng, Holyoak (1993) Evoking the permission schema: the impact of explicit negation and a violation-checking context. Q J Exp Psychol 46A, 615-635. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/kroger_cheng_holyoak_1993.pdf (evidence: d06)
- [V] Gigerenzer and Hug (1992) Domain-specific reasoning: Social contracts, cheating, and perspective change. Cognition 43, 127-171 (Part 1: replication and cueing). https://www.cse.iitk.ac.in/users/se367/11/se367/jaysha/project/gigerenzer.pdf (evidence: d07, d08)
- [V] Sperber, Cara, Girotto (1995) Relevance theory explains the selection task. Cognition 57, 31-95 (Experiments 1-3). https://www.dan.sperber.fr/wp-content/uploads/2009/09/SperberCaraGirotto.pdf (evidence: d09, d10)
- [V] Ahn and Graham (1999) The impact of necessity and sufficiency in the Wason four-card selection task. Psychological Science 10(3), 237-242. https://ahnthinkinglab.yale.edu/sites/default/files/files/Papers/1999-2.pdf (evidence: d11)
- [V] Macchi, Poli, Caravona, Vezzoli, Franchella, Bagassi (2019) How to get rid of the belief bias: boosting analytical thinking via pragmatics. Europe's J Psychol 15(3), 595-613. https://doi.org/10.5964/ejop.v15i3.1794 (evidence: d12)
- [V] Ranaldi, Valentino, Freitas (2025) Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions (QuaSAR), ACL 2025. https://arxiv.org/abs/2502.12616 (evidence: d15)
- [V] Gao, Bosselut, Bengio, Abbe (2026) AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking. ICLR 2026. https://arxiv.org/abs/2506.07751 (evidence: d16)
- [V] Valina, Seoane, Ferraces, Martin (1996) Wason's selection task: content effect, instruction effect or both? (Third International Conference on Thinking). https://minerva.usc.gal/bitstreams/dd5f185b-b5be-4ba1-bb2a-152f8c8f3e46/download (evidence: d17)
- [V] Ayman, Marzouk, Mashaly, Hereiz (2026) Proofbusters at SemEval-2026 Task 11: Neuro-Symbolic Syllogistic Reasoning via LLM-Guided Structure Extraction and Deterministic Validation. https://aclanthology.org/2026.semeval-1.182.pdf (evidence: d19)
- [V] Muhamad, Lopo, Wong, Habibi, Cahyawijaya (2026) ITLC at SemEval-2026 Task 11: Normalization and Deterministic Parsing for Formal Reasoning in LLMs. https://arxiv.org/pdf/2603.02676 (evidence: d21)
- [V] Kartac, Onderkova, Bronec, Kasner, Lango, Dusek (2026) UFAL-CUNI at SemEval-2026 Task 11: An Efficient Modular Neuro-symbolic Method for Syllogistic Reasoning. https://arxiv.org/pdf/2605.04941 (evidence: d22)
- [V] Valentino et al. (2026) SemEval-2026 Task 11: Disentangling Content and Formal Reasoning in Large Language Models (overview), Table 2 and Sec. 4. https://aclanthology.org/2026.semeval-1.450.pdf (evidence: d23)
- [V] Maraia, Valentino, Zanzotto, Ranaldi (2026) Abstract Activation Spaces for Content-Invariant Reasoning in Large Language Models. https://arxiv.org/pdf/2602.02462 (evidence: d25)
- [V] Holyoak, Cheng (1995) Pragmatic reasoning with a point of view. Thinking and Reasoning 1(4), 289-313. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Holyoak_Cheng_1995_PragmaticReasoning.pdf (evidence: d30)
- [V] Trippas, Thompson, Handley (2017) When fast logic meets slow belief: Evidence for a parallel-processing model of belief bias. Memory and Cognition 45, 539-552. https://link.springer.com/article/10.3758/s13421-016-0680-1 (evidence: d33)
- [V] Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models. https://arxiv.org/pdf/2604.02485 (evidence: d34)

Background names used in section 2 without an evidence line (not opened, from general knowledge, not relied on for any number): Wason 1966; Johnson-Laird 1972; Wason and Shapiro 1971; Griggs and Cox 1982 (named in a01); Evans and Lynch 1973 (numbers via a17); Cosmides and Tooby 1992; Platt and Griggs 1993; Fiddick and Rutherford 2006; Jackson and Griggs 1990; Noveck and O'Brien 1996.
