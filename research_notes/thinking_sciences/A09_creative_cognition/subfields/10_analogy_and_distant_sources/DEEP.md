# Analogy and distant sources: deep document

*Subfield A09.10. Schema part: O7 (map an analogue). Evidence ids (a01-d17) and claim ids (A09.10-K01 to K23) refer to evidence_a-d.jsonl and claims.jsonl in this folder. Status tags: [E] established, [S] single-source, [C] contested. Read the weak-spots paragraph at the end of section 10 before trusting any number marked [M] in section 11.*

## 1. What it is

Analogy is using a known case (the source) to solve or explain a new case (the target) by matching the relations between parts, not the parts themselves. "Distant sources" are sources from a different domain than the target. The creativity claim is that far sources give novel ideas that near sources cannot, because near sources only repeat what the domain already holds.

Three separate skills are involved. Most confusion in the literature comes from mixing them.

1. **Retrieval.** Finding a useful source in memory or in a corpus. Humans do this badly across domains. They retrieve by surface likeness.
2. **Mapping.** Aligning source and target by relational structure, then carrying over the solution. Humans and large models do this well once both are in view and the domain is familiar.
3. **Evaluation and adaptation.** Checking that the carried-over solution fits the target's constraints. A far analogy can satisfy most constraints and fail one hidden one (a05).

For our agent, O7 in the schema is "a distant problem and a typed mapping, checked by code". This document asks which parts of that are backed by evidence, which are not, and what the LLM studies say about each skill.

## 2. History and theories in depth

**Duncker's radiation problem and Gick and Holyoak (1980, 1983).** The founding experiments gave people Duncker's tumour problem. A ray strong enough to kill the tumour also kills healthy tissue. How do you destroy the tumour? The convergence solution is to fire weak rays from many directions. The source was a fortress story in which an army splits and converges. The 1980 paper was not opened by us (403). It is recapped in the 1983 paper (d05). The 1983 paper was opened in full (d03-d07). Key results: about 10% of controls solve the problem. About 30% solve it after memorising the story, with no hint. About 75% to 80% solve it once told to use the story. So the source sits in memory and is not noticed. The bottleneck is noticing, not mapping.

**Schema induction (Gick and Holyoak 1983).** Two analogous stories, compared by the learner, give a general schema and more transfer than one story (45% vs 21% before a hint, Exp 4). The quality of the written schema tracks transfer: good schemas gave 91% unprompted success. Giving the abstract principle or a diagram on top of one story did not help (Exp 2, 3). The learner has to build the abstraction from cases.

**Structure-mapping theory (Gentner 1983; Gentner, Rattermann and Forbus 1993).** Analogy is the alignment of relational structure with one-to-one mapping and systematicity (higher-order relations preferred). Surface (object) similarity drives retrieval from memory. Structural match drives judged soundness. People remember surface matches and rate structural matches as better (a24, recalled, not opened). This explains why far sources are not retrieved unaided.

**Constraint-satisfaction models (Holyoak and Thagard 1989, ACME).** Mapping is a soft balance of structural, semantic and pragmatic constraints. "Pragmatic" means goal relevance. This paper was not opened (a26 recalled).

**Dunbar's in vivo work (1995, 1997, 2001).** Recordings of four molecular biology labs. Analogies were common, but most were local (same organism) or regional (neighbouring field). Distant analogies were rare and mostly explanatory. The only numbers we have are second-hand: 98% local or regional (d15). Christensen and Schunn (2007) set this against product design meetings, where 45% of analogies were between-domain (a01).

**Structured imagination (Ward 1994) and design fixation.** People tend to copy the standard properties of the category they know, the path of least resistance (a27, recalled). An example in view pulls ideas toward itself. Christensen and Schunn found fewer analogies when a prototype was at hand (a03). The fixation literature is in the earlier document 06_fixation_and_structured_imagination and is not repeated here.

**Design-by-analogy research (2002-2017).** Dahl and Moreau (2002, not opened), Chan et al. (2011), Fu et al. (2013), Song et al. (2017) and Hope et al. (2017) test whether the distance of examples changes novelty and quality. The picture is mixed (section 5). Chan, Dow and Schunn (2015, snippet only) say support for far sources is mixed and most cells had N <= 12 (b11).

**Computational analogy (1980s to 2020s).** Mapping engines (SME, ACME) work on hand-built structures. Analogy mining (Hope 2017, 2021; Sultan and Shahaf 2023) extracts purpose and mechanism, or entity-relation graphs, from text. LLM work after 2022 treats analogy as a prompt-level skill (Webb 2023; Yasunaga 2024) or as a benchmark target (ARN, AnaloBench, KidsARC, counterfactual letter strings).

**Links to other subfields in this run (not covered here):** Analogical prompting for LLMs; Comparison and relational language; Vector-space relational similarity; Creative problem solving; Novelty measurement; Knowledge networks. Conceptual blending was done earlier (03). Where they overlap, those documents govern.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Spontaneous transfer is rare in humans | About 10% of controls solve the radiation problem. About 30% after memorising the analogous story, no hint. About 75-80% when hinted. Pendulum problem (N=69): 71% before hint vs 20% control; 98% vs 30% total | Gick and Holyoak 1983 (d03-d07) | [E] |
| Two cases plus an induced schema beat one case | 45% vs 21% before hint; 80% vs 53% total (Exp 4). Good written schema 91% (10 of 11) before hint; poor schema 30% | Gick and Holyoak 1983 (d03, d04) | [S] |
| A stated principle or diagram adds nothing | Exp 2: analog+principle 32% before hint, analog only 29%, principle only 28%. Exp 3: analog+diagrams 23%, analog only 40% | Gick and Holyoak 1983 (d07) | [S] |
| In vivo design: analogy is frequent and 45% between-domain | 102 analogies in 7 meetings, 11.3 per hour. 55% within, 45% between domain | Christensen and Schunn 2007 (a01, a02) | [S] |
| Distance depends on function | 28% problem-identifying (mostly near), 40% solving (mixed), 32% explaining (mostly far). chi2(2)=20.93, p<.001 | Christensen and Schunn 2007 (a04) | [S] |
| A prototype in hand reduces analogy | Idea segments (N=1,616) had more analogies than prototype segments (N=1,383). chi2(1)=7.88, p=.006. The gap came entirely from between-domain analogies | Christensen and Schunn 2007 (a03) | [S] |
| Dunbar: distant analogies rare in labs | 98% local or regional (secondary, no counts) | Dunbar via review (d15, a06) | [C] against C&S |
| Far examples raise novelty, lower quantity | Novelty far vs near d=0.56. Quantity d=-0.30 (about one concept fewer). Quality SD d=0.64. No mean quality change. Only far + uncommon beat control (novelty d=1.14, max d=1.29). N=153 | Chan et al. 2011 (b01-b07) | [S] |
| Opposite pattern in patent stimuli | Far-only and home+far gave higher quality. Near-containing sets gave higher novelty. 138 concepts | Song et al. 2017 (b08-b10) | [C] |
| Purpose-matched, mechanism-distant sources help ideation | Good ideas 46% vs 37% random vs 30% TF-IDF (nine shared seeds). Judge k=2: 0.71 vs 0.28 vs 0.27. 38 workers, 749 ideas | Hope et al. 2017 (a17, b13, b14) | [S] |
| Surface-similar sources equal random | 0.28 vs 0.27 (k=2); 0.16 vs 0.14 (k=3) | Hope et al. 2017 (b14) | [S] |
| Structured representations retrieve analogues better than text | Precision at top 1%: mechanism-only 0.739, concat 0.696, TF-IDF 0.630, LSA 0.413, LDA 0.435. Sultan and Shahaf: 87% correct mapping (procedural texts), 94% (psychology stories) | Hope 2017 (a18); Sultan and Shahaf 2023 (c23) | [E] (3 sources) |
| LLM beats humans on near analogy formats | Digit matrices OR 1.88 (p=.005), N=40. Letter strings OR 1.76 (p=6.3e-5), N=57. Verbal analogies at or above SAT average | Webb et al. 2023 (a07, c01-c03) | [E] |
| LLM fails far stories | GPT-3 near p=.0039; far p=.065 (n.s.). Human advantage OR 0.37, p=.0003. Humans N=54 | Webb et al. 2023 (a09) | [E] |
| ARN: far analogies fail, surface lures hurt | GPT-4 near analogy 94.0 or 92.5; far analogy with far distractor 57.1; far analogy with near distractor 29.1 (chance 50). Mean over models: near 75.0, far 39.6. Humans 97.9 and 94.1 | Sourati et al. 2024 (a15, b25) | [E] |
| Counterfactual letter strings break models | Mean accuracy over alphabets: humans 0.753 (136 people), GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 | Lewis and Mitchell 2024 (a10, c10) | [C] |
| Rebuttal: code execution restores GPT-4 | GPT-4 + code vs humans P=0.496. GPT-4 alone below humans P=8.9e-13 | Webb et al. 2024 (a11) | [C] |
| Symbol-domain transfer drops in models | Latin/Greek/Symbol: adults .88/.91/.89; GPT-4o .85/.63/.48; Claude-3.5 .68/.62/.46; Llama-3.1 405B .79/.74/.27 | Stevenson et al. 2024 (c12) | [S] |
| Long-story analogy gap grows | GPT-4 89.1 / 66.5 / 60.7 at 1/10/30 sentences; human 96.0 / 72.5 / 73.3. Gap 6.9 to 28.8 points | Ye et al. 2024 AnaloBench (b23, b24) | [S] |
| Analogical prompting: small gain | GSM8K GPT-3.5: 0-shot CoT 75.8, 5-shot CoT 76.7, analogical 77.8. MATH 33.9 / 34.9 / 37.3. text-davinci-003 GSM8K 50.3 / 54.0 / 61.0 | Yasunaga et al. 2024 (a13, c06) | [S] |
| Relevance of self-generated examples doubted | Average GSM8K+MATH: relevant 52.4, no instruction 55.8, random biology 54.9. Relevant-example similarity to query 0.48 | Qin et al. 2024 (c08, c09) | [C] |
| Knowledge step before exemplars | Codeforces Acc@1 GPT-3.5: exemplars 13, plus knowledge 15. GPT-4 17 vs 19 | Yasunaga 2024 (a14, c25) | [S] |
| LLM analogy quality scales with size | Meaningful analogies 1.90% (0.3B), 15.61%, 48.29%, 70.05% (175B) vs human 66.67%. Given a source, 175B falls to 53.79% | Bhavya et al. 2022 (a16, c14, c15) | [S] |
| One-shot example improves analogy usefulness | Potentially useful 80% (one-shot) vs 40% (zero-shot). About 26% flagged potentially harmful | Ding et al. 2023 (c16, c17) | [S] |
| LLMs produce infeasible creative solutions | GPT-4 18.9% efficient, 37.5% infeasible (MacGyver, 1,600+ problems). Self-reflection cut infeasible solutions by 9.7 points on 180 solvable problems | Tian et al. 2024 (a21) | [S] |
| Strong LLMs gain from a source only if it is far | o3 and Claude-Sonnet-4 effect 0.02 (all pairs), 0.12 (farthest 50%), 0.24 (farthest 10%). Originality rises with distance, no inverted U. 140 humans, 7 LLMs, 2,800 ideas | Liu et al. 2026 (d08, d09) | [S] |
| Human top ideas lose usefulness; LLM ideas do not | Top 10% human originality: usefulness lower by 0.81, p<.001 | Liu et al. 2026 (d10) | [S] |
| Analogy pipeline raises diversity, lowers reasonableness | Vendi +90 to 173%. AR judged more novel in 78% of pairs. Reasonable 67% vs 86% for plain cross-domain | Shen et al. 2026 (d11, d12) | [S] |
| LLM idea pools collapse to duplicates | About 5% unique of 4,000 seeds. Novelty 5.64 vs 4.84 for experts | Si et al. 2024 (b29) | [S] |
| Reasoning models still fail under noise | o3-mini 86.6 to 17.0. 3.4x more tokens. Hardest cell 31.0% at 53,596 tokens | Camposampiero et al. 2025 (d01, d02, d14) | [S] |
| Rewrite against nearest prior work raises novelty about half the time | 46.7-55.6% of ideas gained novelty (first iteration) | SciMON (b27, b28) | [S] |
| Step-back abstraction | GPT-4 Physics 69.4 to 84.5 (CoT 82.9). Adds 11.9% new errors | Zheng et al. 2023 (d13) | [S] |

Note on the ARN row. The full GPT-4 columns are (analogy, distractor) near/far 94.0, near/near 92.5, far/far 57.1, far/near 29.1 (critique correction 2). The "below chance" statement holds for GPT-4 only in the last cell.

## 4. Mechanisms and models

**4.1 Three-stage model (the one to implement).** Retrieve, map, audit.

- *Retrieve.* Index every stored case (a past solved task, a stored problem) by two descriptions: a surface description (domain, objects) and an abstract description (purpose, mechanism, relation pattern, constraints). Hope et al. 2017 learn two vectors per item, purpose and mechanism, then query for the same purpose and a different mechanism. Mechanism-only vectors reached precision 0.739 at top 1%, TF-IDF 0.630 (a18). Implementation: ask the model once per stored item for a one-line purpose and a one-line mechanism with domain words removed. Embed those. Retrieve on purpose similarity while penalising mechanism similarity. The ideation payoff of this policy comes from a human crowd, N=38 (K03, single source). The retrieval-quality finding has three sources (K04).
- *Map.* Write a typed mapping: source object to target object, source relation to target relation, source constraint to target constraint. Sultan and Shahaf extract entities and relations from both texts, then align by structure mapping (87% correct on procedural texts). In our scaffold, code can check the mapping is one-to-one and that every mapped relation exists on both sides. Code cannot check that the relation is the right one. That is a hole (section 10, question 3).
- *Audit.* Before a mapped solution goes to the test state, list each target constraint and mark whether the transferred solution satisfies it. This targets a known failure: a far analogy meets several constraints and fails a hidden one (a05, Venetian blinds were not water soluble). Evidence that a reflection step lowers infeasibility: MacGyver self-reflection cut infeasible solutions by 9.7 points on solvable items (a21). A direct test of an audit is in UNKNOWNS.md.

**4.2 Why spontaneous transfer fails (noticing).** Gick and Holyoak show the source can be in memory and unused. About 30% solved unprompted after memorising the story, and about 75-80% once hinted. The hint does not teach the mapping. It triggers retrieval. For an agent, the context window already holds a source if we put it there, so noticing is not the problem. When the agent must pull from memory, retrieval triggers matter more than mapping. An explicit analogue-search step at an impasse (O7) is more defensible than hoping the model notices.

**4.3 Schema induction from two cases.** Give two sources and ask what they share, then apply. 45% vs 21% before a hint (Exp 4). Comparing cases drops surface detail and leaves the relation. Writing the schema matters: 91% unprompted success with a good written schema, 30% with a poor one. Implementation: when two analogues exist, require a written shared-structure statement. Then check it with a second call that does not see the source text (does the statement still make sense alone?). Do not supply a principle on its own (Exp 2, 3 show no benefit).

**4.4 Distance as a dial, not a switch.** Distance can be measured by embedding distance of abstract descriptions, by a Wikipedia-based semantic distance (Liu 2026, beta .1 for humans, .18 for LLMs), by patent-network position (Song 2017), or by a surface-feature count (Christensen and Schunn: 3.82 vs 0.52 shared features, t(100)=17.21). Implementation: compute cosine distance between target and source embeddings of the abstract descriptions, bin into thirds, and log the bin with the outcome. This lets a distance floor be learned from data. Liu et al. found strong models gain only above a distance floor.

**4.5 Self-generated exemplars (analogical prompting).** One call: "recall 3 related problems, solve each, then solve the target". Diversity of the three and enough of them (K >= 3) matter. It needs a model large enough to write valid problems. Small models do better with retrieved real exemplars (b17, c07). Qin et al. showed the benefit may come from example correctness and extra sampling, not relevance.

**4.6 Explicit analogy pipeline for diversity (Shen 2026).** Three steps: extract the relational structure of the problem, search other domains for that structure, map back. Compared with a plain cross-domain prompt at the same 2 calls, solution diversity (Vendi) rose 90 to 173%. Claude's binary novelty went from 21.6 to 50.4%. Cost: humans judged fewer solutions reasonable (67% vs 86%). It is a diversifier and needs a feasibility audit after it.

**4.7 Abstraction first (step-back, ARN CoT).** Ask for the high-level principle or story message before mapping. Far ARN analogies gained up to +30 points while near accuracy fell (c22). Step-back lifted GPT-4 Physics from 69.4 to 84.5, but plain CoT reached 82.9, so most of that gain is CoT. It also adds 11.9% new errors (d13).

## 5. What holds up

**Established (several independent sources).**
- Unaided noticing of distant analogues is rare in humans (Gick and Holyoak 1980 recap and 1983, replicated on the pendulum problem, d06). [E]
- Retrieval by surface similarity misses analogues. Structured (purpose, mechanism, relation) representations retrieve better than TF-IDF, LSA and LDA (Hope 2017, 2021; Sultan and Shahaf 2023; AnalogyKB). [E]
- LLMs handle near, familiar analogy formats and fall on far and counterfactual ones (Webb far stories, ARN, Stevenson, Lewis and Mitchell, KidsARC, AnaloBench by length). Six independent papers. [E]
- Surface-similar lures hurt models more than humans (ARN, GPT-4 29.1% on far analogy with near distractor). [E]
- Far analogies can break on a hidden constraint, and LLMs produce infeasible creative solutions (a05, a21). [E]

**Contested.**
- Do far examples help human ideation? Chan 2011: far raises novelty, but only with uncommon examples. Song 2017: near-containing sets raise novelty, far raises quality. Fu 2013 as reported by Song: near or middle gave higher max novelty and quality. Wilson 2010: no difference. Chan, Dow and Schunn 2015 (snippet): N <= 12 per cell in most studies. No meta-analysis exists. Net: far sources add spread. A mean gain is not reliable.
- Distance in real settings. Christensen and Schunn 45% between-domain (design meetings) vs Dunbar 98% local or regional (labs, second-hand). Setting and function (explain vs solve) differ. Not resolved.
- Emergent analogical reasoning in GPT-class models. Lewis and Mitchell: permuted alphabets, models far below humans, and below Webb's own letter-string numbers. Webb et al. 2024: GPT-4 with code execution matches humans (P=0.496). In Lewis and Mitchell GPT-3 (0.488) beats GPT-4 (0.452) overall. The dispute is partly about whether code use counts.
- Relevance of self-generated exemplars. Yasunaga: relevant exemplars help. Qin: random biology 54.9 vs relevant 52.4, and example correctness mattered. Not run on reasoning models.
- An explicit abstraction step. +30 points on far ARN analogies but a cost on near. Gick and Holyoak Exp 2-3: a given principle gave no gain.

**Failures and nulls to remember.**
- A principle or diagram without cases: no transfer gain (Gick and Holyoak Exp 2, 3).
- Strong LLMs gain nothing on average from a random cross-domain source (effect 0.02, p=.64). They gain only far out (0.24 on the farthest 10%).
- Longer reasoning did not rescue analogy under noise. o3-mini medium to high used 5,445 to 9,867 tokens on the clean set (86.6 to 92.6) but still scored 17.0 on the hardest noisy cell. The hardest condition used 53,596 tokens for 31.0%.
- Giving a source to the largest model hurt analogy generation (70.05 to 53.79, Bhavya 2022).
- Self-generated exemplars did nothing for the smallest models (curie 2-3% on GSM8K).

**Moderators.**
- Model size: self-generated exemplars help more with larger models (davinci-003 GSM8K 61% vs 5-shot retrieved 54-57%). Retrieved exemplars help smaller ones.
- Story length: the LLM-human gap grows from 6.9 to 28.8 points between 1 and 30 sentences.
- A prototype in hand: fewer analogies (K06, single source).
- Function: far analogies mostly explain. Near ones identify problems.
- Commonness of the source: far helps novelty only if uncommon (Chan 2011).
- Tools: code execution closes the letter-string gap (a11).

**Interventions that worked.**
- Purpose-matched, mechanism-distant retrieval (humans): good-idea rate 46% vs 30% and 37%.
- Two cases plus a written shared schema (humans).
- A one-shot example when generating analogies (80% vs 40% useful). Abstraction CoT on ARN (+30 far).
- The analogy pipeline for diversity (Vendi +90 to 173%).
- Divergent-then-convergent prompting (+6.5 points efficient solutions) and step-wise self-reflection (-9.7 points infeasible) on MacGyver.

**Did not work or not shown.**
- A principle or diagram alone.
- Supplying a source to the biggest model for generation.
- Relevance of the self-generated example (not shown to matter in Qin).
- Extra reasoning effort for analogy robustness.

## 6. Language models

**Near analogy: at or above the human average.** GPT-3 (text-davinci-003, zero-shot) beat UCLA undergraduates on Digit Matrices (OR 1.88 generation, 6.27 multiple choice, N=40) and on letter strings (OR 1.76, N=57). It matched them on verbal analogies. Its item difficulty followed human item difficulty (r(30)=0.39). Hu et al. (a12) show how much problem description matters: the same Raven problem scored 77.2% with numeric attribute names and as low as 28.2% with quasi-image naming (GPT-3 175B, Center sub-task).

**Far or counterfactual analogy: below humans.**
- Stories: GPT-3 far p=.065 (n.s.). Humans (N=54) did near and far well, 15 of 54 perfect. A GPT-4 pilot was stronger on near.
- ARN: GPT-4 94.0 near, 57.1 far, 29.1 when a surface-similar distractor sits next to a far analogy. Models average 57.3 overall vs humans 96.0.
- Letter-string counterfactuals: GPT-4 0.452 vs humans 0.753. Alternate-rule errors were 22.00% of GPT-4 errors (humans seldom). Comprehension checks were mostly 0.9-1.0, so it is not a failure to read the new alphabet.
- Symbol domain: GPT-4o .85 Latin, .63 Greek, .48 Symbol. Adults .88, .91, .89.
- AnaloBench: the GPT-4 gap to humans grows with story length (6.9 to 28.8 points).
- KidsARC: LLM average 33.2% on simple items (children 9-11: 73.9%) and 11.9% on concept items (children 6-8: 56.2%). 76% of classified fallback errors were exact copies.
- Reasoning models: on symbolic Raven-style tests o3-mini reached 86.6 and fell to 17.0 (chance 12.5) with confounders and noise. More reasoning effort did not fix it (d01, d14). R1 went from 80.6 to about 23. Under perceptual uncertainty reasoning models lose 61.8 points on average (d02). No 2025-2026 reasoning-model rerun of ARN, Stevenson or Lewis and Mitchell was found. This is the main hole.

**What changed behaviour, and by how much.**
- Analogical prompting: +2.0 on GSM8K (75.8 to 77.8) and +3.4 on MATH (33.9 to 37.3) for GPT-3.5 over 0-shot CoT. +10.7 for davinci-003 (50.3 to 61.0). On Codeforces a knowledge step added about 2 (13 to 15 for GPT-3.5, 17 to 19 for GPT-4). Gains are small and depend on model size.
- But Qin et al. found random same-domain (55.7) and random biology (54.9) examples beat the relevant condition (52.4) on the GSM8K+MATH average, and the plain baseline was 55.8. The gain from analogical prompting may come from extra samples or correct examples. No equal-token control against plain extra sampling exists.
- Abstraction CoT demos on ARN: up to +30 on far, with a cost on near.
- Code execution on letter strings: human parity (a11, P=0.496).
- Thought Propagation: +12% shortest-path, +13% human preference in creative writing, +15% task completion in agent planning. These are averages over baselines, use near analogues, and are not equal-token tests (c18).
- A one-shot example for design analogies: 80% useful vs 40% zero-shot (GPT-3).
- Analogy pipeline (Claude Sonnet 4.5, GPT-5.2, Gemini 3 Flash): Vendi +90 to 173%. Domain Distance 6.99 / 6.83 / 7.53 vs 2.29 / 3.08 / 3.37 without a domain. Humans rate fewer solutions as reasonable.
- Liu 2026: LLM originality is already high with no source (o3 3.83), and a random source helps only far out. This study is closest to our case because it uses current-generation models.

**Quality of LLM analogies.** Bhavya et al.: 70.05% meaningful at 175B, above the human reference 66.67%. About 26% of design analogies potentially harmful (Ding 2023). 37.5% of GPT-4's MacGyver solutions infeasible. Shen 2026: analogy solutions judged reasonable in 67% of pairs.

**Diversity.** LLM idea pools collapse: only about 5% of generated domains were unique (Shen 2026) and about 5% of ideas of 4,000 seeds were unique (Si 2024). An explicit analogy step breaks the domain collapse.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Keep O7 only at an impasse (S6), never on a schedule. Unaided analogy is rare in humans. Make the analogue search an explicit step. Do not rely on the model to notice. | G1 / O7 | [E] rarity; [S] prototype effect | a22, d05, d06, a03 (K17, K06) |
| 2 | Retrieve analogues by abstract role (purpose, mechanism, constraint pattern), not by surface text. Store a surface and an abstract description for each memory entry. | M / O7 | [E] retrieval quality (3 papers); [S] ideation payoff | a17, a18, a19, c23, c20 (K03, K04) |
| 3 | After any analogical proposal run an explicit constraint audit before S4 tests it. | G / O7 | [E] far analogies hide failed constraints; [S] audit lowers infeasibility | a05, a21 (K07) |
| 4 | Guard against surface lures. When sources are in context, check the relational match first. Never choose a source on surface likeness. Log the distractor drop. | G (surface lure) / O7 | [E] | a15, b25, b26, b21, c05 (K10) |
| 5 | Do not credit the model with far-domain mapping competence. Near, familiar analogy is fine. Far or counterfactual mapping must be checked by code or tool execution, not by the model's say-so. | G3 / G8 / O7 | [E] | K08; a11 (K09 contested for tools) |
| 6 | Do not use extra reasoning effort as the fix for analogy robustness. Longer thinking did not rescue accuracy and cost 3.4x tokens. | G11 | [S], consistent with G11 | d01, d14 (K21) |
| 7 | Treat far analogy as a source of spread for impasses. It raises variance. A mean gain is not shown. | O7 / G12 | [E] in schema (F05); [C] on novelty direction | b01-b06, b08-b10 (K01, K02) |

### Test first (not yet established; each has a row in UNKNOWNS.md)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 8 | Two analogues plus a written shared schema, then apply. | O7 | [S], human only | d03, d04 (K22) |
| 9 | Abstraction first before mapping on far problems. | O7 | [C] | c22, d13, d07 (K11) |
| 10 | Distance floor: drop sources below a distance floor; sweep near, mid, far. | O7 / S6 | [S] | d08, d09 (K18, K02) |
| 11 | Analogy pipeline as a diversifier with a feasibility audit after it. | O7 / S3 | [S] | d11, d12 (K20) |
| 12 | Self-generated analogues vs a plain extra-sampling control and a random-exemplar control. | O7 | [C] | a13, c08, c09 (K12, K13) |
| 13 | Analogue retrieval from the agent's own past tasks by abstract role. | M | open, no direct study | d16 (K23) |
| 14 | A one-shot worked example when asking the model to generate analogies. | O7 | [S] | c16 (K15) |
| 15 | For small models, retrieved verified exemplars instead of self-generated ones. | O7 | [S] | b17, c07 (K14) |
| 16 | Log analogy distance by function (identify, solve, explain) in agent traces. | S9 log | [C] | a04, a06 (K05) |

## 8. Concrete tests on our bench

All arms use equal total tokens, including retrieval and setup cost (G7). Use at least 3 seeds. Report mean and SD, not only the mean. Judge outputs by running where possible (G8).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Hard ARC and brainteaser items that failed a plain pass | (a) plain resample, (b) O7 with self-generated analogues, (c) O7 with random exemplars of the same size, (d) extra sample, no analogue | Solve rate on held-out checks at equal tokens | If (b) beats both (c) and (a) by 3 points, relevance matters. Qin predicts (b) <= (c). Yasunaga predicts (b) about +2 over (a) |
| T2 | ARN-style far-analogy items, plus our own relation-preserving rewrites | (a) zero-shot, (b) abstraction-first demos, (c) plain CoT, (d) near-only demos | Far accuracy, near accuracy, far-with-near-distractor accuracy | (b) +10 to +30 on far, a few points lost on near |
| T3 | Counterfactual letter-string and symbol-alphabet items | Tools off vs code execution; low vs high reasoning effort at equal tokens | Accuracy against the human 0.753 reference | Tools close most of the gap (Webb 2024). High effort alone does not |
| T4 | Open design problems with objective constraints (MacGyver style) | (a) O7 without audit, (b) O7 with constraint audit, (c) plain | Infeasible rate, unique ideas, efficient-solution rate | Audit cuts infeasible by about 10 points and keeps diversity |
| T5 | Idea tasks seeded 50 times | (a) no source, (b) near, (c) mid, (d) far, (e) analogy pipeline | Duplicate rate, Vendi score, blind-judged novelty, feasibility | Vendi up with far and with the pipeline. Feasibility down. Effect only above a distance floor for strong models |
| T6 | Tasks with 100+ past solved items in memory | (a) text-embedding retrieval, (b) purpose/mechanism retrieval, (c) random | Useful-analogue hit rate at top 5, downstream solve rate | (b) beats (a) by 5 to 10 points precision. Downstream effect unknown |
| T7 | Impasse items with 2 retrieved analogues | (a) one analogue, (b) two analogues plus written shared schema, (c) two analogues, no schema | Solve rate, schema quality score | (b) above (a) by a few points. Schema quality predicts solve, as in G&H |
| T8 | Items with and without a draft in context | (a) analogy step with draft present, (b) with draft absent | Analogy count, solve rate | Fewer analogies with a draft (C&S). Check whether solve rate suffers |

## 9. What does not transfer, and why

- **Hint effects.** The Gick and Holyoak jump from 30% to 75-80% with a hint is a memory-retrieval effect. An agent whose context already holds the source does not have this problem. The hint becomes "use the source". We cannot assume the same number.
- **Human novelty ratings.** Human studies (Chan, Song) rate student designs for rural power harvesters or spherical robots. Their novelty scales are not our bench metric. Higher human-rated novelty does not mean a passed test.
- **Crowd retrieval (Hope).** The 46% vs 30% result comes from crowd workers reading inspirations. An LLM reads a source with no fatigue and a different fixation pattern. The result tells us about retrieval quality, not about LLM idea payoff.
- **Fixation.** Part of the human distance effect is fixation on near examples. Strong LLMs are already very original, and far sources help only at large distance (Liu 2026).
- **In vivo findings.** Distance distributions from lab and design meetings (Dunbar, C&S) describe humans in social settings, often explaining to colleagues. They say little about what an agent should do in S6.
- **Schema induction.** Two-case schema induction was shown with students on a few problems (radiation, pendulum). Transfer to LLM agents is a hypothesis.
- **2022-2024 model numbers.** Almost all LLM tests use GPT-3 to GPT-4o and Claude 3.5. The near-far gaps may shrink for 2025-2026 reasoning models. We have no verbal far-analogy test of them.
- **Structure-mapping theory.** The theory predicts what is hard for people. LLM "mapping" is not an alignment engine. LLM errors (alternate rules, exact copies in KidsARC) differ from human errors.

## 10. Open questions

1. Do 2025-2026 reasoning models close the far-analogy and counterfactual gap on ARN, Stevenson, Lewis and Mitchell? No rerun found. Only symbolic Raven-style tests exist.
2. Does an analogy step beat extra sampling at equal tokens? No study found (d17).
3. Can code check a mapping? Code can check one-to-one structure and that relations exist. Whether the relation is the right one is open.
4. Is there an inverted U in distance for quality and feasibility? Liu 2026 found none for originality. Quality by distance bin is not reported.
5. Does abstraction-first help far analogy without hurting near? ARN says it costs near accuracy.
6. Does purpose/mechanism retrieval work on an agent's own task memory? Only snippet-level memory papers found.
7. What do Dunbar's original in vivo counts say? Only the secondary 98%.
8. Does a feasibility audit cut the roughly 25% harmful or 33% unreasonable rate at equal tokens?
9. Do Gentner 1993 numbers hold? Not opened.
10. Does varying distance restore idea-pool diversity for research ideas (Si 2024 setting)? Tested only for biomedical solutions (Shen 2026).

**Weak spots.** Gick and Holyoak 1980, Gentner 1993, Dunbar 1997, Holyoak and Thagard 1989, Ward 1994 and Dahl and Moreau 2002 were not opened. Their points here come from memory or recaps. Chan 2011 effect sizes, Hope 2017 percentages and Christensen and Schunn counts were read by earlier evidence agents and not re-verified in the critique pass. Many evidence lines are re-extractions of one paper (Webb x4, Yasunaga x4, ARN x3, Lewis and Mitchell x3, Hope x4), so independent-paper counts are what count. Yasunaga Table 1 was corrected (use a13, c06, not b15). There is no meta-analysis of far-source effects. Thought Propagation uses near analogues. Si 2024 is not an analogy test.

## 11. Sources

[V] = opened and read this session or an earlier evidence session. [M] = snippet or memory only.
- [V] Christensen & Schunn (2007). https://link.springer.com/content/pdf/10.3758/BF03195939.pdf (ids a01, a02, a03, a04, a05, a06)
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/pdf/2212.09196 (ids a07, a08, a09)
- [V] Lewis & Mitchell (2024). https://arxiv.org/pdf/2402.08955 (ids a10)
- [V] Webb, Holyoak, Lu (2024). https://arxiv.org/pdf/2404.13070 (ids a11)
- [V] Hu, Storks, Lewis, Chai (2023) In-context analogical reasoning with pre-trained language models. https://arxiv.org/pdf/2305.17626 (ids a12)
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners (analogical prompting). https://arxiv.org/pdf/2310.01714 (ids a13, a14)
- [V] Sourati et al. (2023) ARN: Analogical reasoning on narratives. https://arxiv.org/pdf/2310.00996 (ids a15)
- [V] Bhavya, Xiong, Zhai (2022) Analogy generation by prompting large language models: a case study of InstructGPT. https://arxiv.org/pdf/2210.04186 (ids a16)
- [V] Hope, Chan, Kittur, Shahaf (2017) Accelerating innovation through analogy mining. https://arxiv.org/pdf/1706.05585 (ids a17, a18)
- [V] Hope et al. (2021) Scaling creative inspiration with fine-grained functional aspects of ideas. https://arxiv.org/pdf/2102.09761 (ids a19)
- [V] Mitchell (2021) Abstraction and analogy-making in artificial intelligence. https://arxiv.org/pdf/2102.10717 (ids a20)
- [V] Tian et al. (2024) MacGyver: are large language models creative problem solvers?. https://arxiv.org/pdf/2311.09682 (ids a21)
- [M] Gick & Holyoak (1980) Analogical problem solving. https://doi.org/10.1016/0010-0285(80)90013-4 (ids a22)
- [M] Gick & Holyoak (1983) Schema induction and analogical transfer. https://doi.org/10.1016/0010-0285(83)90002-6 (ids a23)
- [M] Gentner, Rattermann, Forbus (1993). https://doi.org/10.1006/cogp.1993.1002 (ids a24)
- [M] Dunbar (1997) How scientists think: on-line creativity and conceptual change in science. https://doi.org/10.1037/10227-017 (ids a25)
- [M] Holyoak & Thagard (1989) Analogical mapping by constraint satisfaction (ACME). https://doi.org/10.1207/s15516709cog1303_1 (ids a26)
- [M] Ward (1994) Structured imagination: the role of category structure in exemplar generation. https://doi.org/10.1006/cogp.1994.1004 (ids a27)
- [M] Dahl & Moreau (2002) The influence and value of analogical thinking during new product ideation. https://doi.org/10.1509/jmkr.39.1.47.18930 (ids a28)
- [V] Chan, Fu, Schunn, Cagan, Wood & Kotovsky (2011). https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/2011-jmd-distancecommonness.pdf (ids b01, b02, b03, b04, b05, b06, b07)
- [V] Song, Srinivasan & Luo (2017). https://www.cambridge.org/core/product/FEF38F74C12C2213C0F12AE91E7FD692/core-reader (ids b08, b09, b10)
- [M] Chan, Dow & Schunn (2015). https://www.lrdc.pitt.edu/Schunn/papers/Chan-Dow-Schun-desstudies-nearfar-inpress.pdf (ids b11)
- [V] Hope, Chan, Kittur & Shahaf (2017) Accelerating innovation through analogy mining, KDD: method. https://arxiv.org/abs/1706.05585 (ids b12, b13, b14)
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners, ICLR: main result. https://arxiv.org/abs/2310.01714 (ids b15, b16, b17, b18, c06, c07, c25)
- [V] Webb, Holyoak & Lu (2023). https://arxiv.org/abs/2212.09196 (ids b19, b20, b21, c01, c02, c03, c04, c05, c24)
- [V] Lewis & Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning in LLMs. https://arxiv.org/abs/2402.08955 (ids b22, c10, c11)
- [V] Ye et al. (2024) AnaloBench: benchmarking the identification of abstract and long-context analogies. https://arxiv.org/abs/2402.12370 (ids b23, b24)
- [V] Sourati et al. (2024) ARN: Analogical reasoning on narratives. https://arxiv.org/abs/2310.00996 (ids b25, b26, c21, c22)
- [V] Wang, Downey, Ji & Hope (2024). https://arxiv.org/abs/2305.14259 (ids b27, b28)
- [V] Si, Yang & Hashimoto (2024) Can LLMs generate novel research ideas? Large-scale human study. https://arxiv.org/abs/2409.04109 (ids b29)
- [V] Qin et al. (2024) Relevant or Random: can LLMs truly perform analogical reasoning?. https://arxiv.org/abs/2404.12728 (ids c08, c09, d17)
- [V] Stevenson, Pafford, van der Maas, Mitchell (2024). https://arxiv.org/abs/2411.02348 (ids c12)
- [V] Opielka, Rosenbusch, Vijverberg, Stevenson (2024) Do LLMs solve ARC visual analogies like people do?. https://arxiv.org/abs/2403.09734 (ids c13)
- [V] Bhavya, Xiong, Zhai (2022) Analogy generation by prompting LLMs: a case study of InstructGPT. https://arxiv.org/abs/2210.04186 (ids c14, c15)
- [V] Ding, Srinivasan, MacNeil, Chan (2023) Fluid Transformers and creative analogies. https://arxiv.org/abs/2302.12832 (ids c16, c17)
- [V] Yu et al. (2024) Thought Propagation: an analogical approach to complex reasoning with LLMs. https://arxiv.org/abs/2310.03965 (ids c18)
- [V] Kang et al. (2022) Augmenting scientific creativity with retrieval across knowledge domains. https://arxiv.org/abs/2206.01328 (ids c19)
- [V] Yuan et al. (2024) AnalogyKB: a million-scale analogy knowledge base. https://arxiv.org/abs/2305.05994 (ids c20)
- [V] Sultan and Shahaf (2023). https://arxiv.org/abs/2210.12197 (ids c23)
- [V] Camposampiero et al. (2025) Can Large Reasoning Models do Analogical Reasoning under Perceptual Uncertainty?. https://arxiv.org/abs/2503.11207 (ids d01, d14)
- [V] Camposampiero et al. (2025). https://arxiv.org/abs/2510.17496 (ids d02)
- [V] Gick & Holyoak (1983) Schema induction and analogical transfer, Exp 4. https://gwern.net/doc/psychology/1983-gick.pdf (ids d03, d04, d05, d06, d07)
- [V] Liu, Dubova, Conklin, Harada & Griffiths (2026). https://arxiv.org/abs/2603.19087 (ids d08, d09, d10)
- [V] Shen, Druckmann & Zou (2026) Unlocking LLM Creativity in Science through Analogical Reasoning. https://arxiv.org/abs/2605.11258 (ids d11, d12)
- [V] Zheng et al. (2023) Take a Step Back: Evoking Reasoning via Abstraction. https://arxiv.org/abs/2310.06117 (ids d13)
- [V] Dunbar via Frontiers/PMC review (secondary) on in vivo analogy distance. https://pmc.ncbi.nlm.nih.gov/articles/PMC4244599 (ids d15)
- [M] Search for agent-memory analogical retrieval (xMemory 2602.02007, Co-Need Index, GAAMA 2603.27910). https://arxiv.org/abs/2602.02007 (ids d16)
