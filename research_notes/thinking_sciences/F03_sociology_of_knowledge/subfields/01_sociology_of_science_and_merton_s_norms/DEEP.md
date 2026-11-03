# Sociology of science and Merton's norms: deep document

*Subfield F03.01. Evidence ids (a01-a28, b01-b26, c01-c26, d01-d16) refer to evidence_a-d.jsonl in this folder. Claim ids (K01-K27) refer to claims.jsonl. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Read critique.md for the corrections applied here.*

## 1. What it is

The sociology of science asks how the social rules of a research community make knowledge reliable. Robert Merton (1942) argued that science runs on four institutional norms, later called CUDOS:

- **Communism (communalism):** findings are common property. The scientist keeps only credit.
- **Universalism:** a claim is judged by impersonal criteria, not by who makes it.
- **Disinterestedness:** the institution controls motives. Scientists are not saints. Peer scrutiny makes fraud costly.
- **Organised scepticism:** every claim is open to detached, structured doubt before it is accepted.

Ian Mitroff (1974) interviewed Apollo moon scientists and said each norm has a counter-norm that scientists also hold: secrecy, particularism, self-interestedness, organised dogmatism (committed advocacy). His point: real science runs on both.

Two kinds of evidence matter to us.

1. **Human studies of the norms.** Do scientists believe them? Do they follow them? Does universalism hold in peer review? Does scepticism (replication) confirm published claims?
2. **LLM studies.** LLMs now act as reviewers, judges, idea generators and "sceptics". Their failure modes match the human breaches of Merton's norms: prestige bias, conformity, self-preference, flattery of long text, injection by interested authors.

Why this matters for our single agent. The agent has no community. But its scaffold contains roles that copy the norms: a judge (universalism, G5), a doubter (organised scepticism, G3), a generator that must not select its own ideas (disinterestedness, G8), and shared memory (communism). This subfield tells us which of those copies work, and where the copy fails because the "community" is one model.

Links to other subfields (not covered here): Research programmes, Falsificationism, Consensus and premature agreement, Red teaming as alternative analysis, Surprisingly popular method, Good Judgment Project, Debiasing by structure, Distributed cognition, Heuristics and biases, Problem selection. Earlier documents in this series on judge bias, debate and self-correction overlap with section 6; this document only adds the sociological framing and the peer-review evidence.

## 2. History and theories in depth

### 2.1 Merton 1942: the four norms (a01-a03, opened)
Merton wrote "Science and Democratic Social Structure" against totalitarian attacks on science (Nazi "Aryan science", Soviet 1948). The paper is a conceptual essay. It has no sample and no statistics. Evidence is historical cases.

- **Communism:** the Newton-Leibniz priority fight and Cavendish's withholding are cases. Patents by Einstein, Millikan, Compton and Langmuir are cited as efforts to keep work public. Open sharing is paid for in recognition. This is why priority disputes are fierce (a03).
- **Universalism:** claims are judged by pre-set impersonal criteria. Nationality, race and class are irrelevant.
- **Disinterestedness:** the near absence of fraud is explained by structure (experts can check results), not by better morals (a02). Later questionable-practice surveys challenge "virtual absence of fraud".
- **Organised scepticism:** judgment is suspended until facts are in hand, and beliefs are examined by empirical and logical criteria.

Limit: norms are claimed from illustration, not measured (a01). Ziman later renamed communism "communalism" (a05).

### 2.2 Merton 1968: the Matthew effect (a09, b08; not opened)
Eminent scientists get disproportionate credit for the same work; unknowns get too little. This is a built-in breach of universalism. It is cumulative: advantage compounds.

### 2.3 Early tests of universalism
- Peters and Ceci (1982): published papers resubmitted under changed names and institutions were mostly rejected, mostly for method flaws (a13, from memory, numbers not verified; do not cite).
- Blank (1991): randomised double vs single blind at the American Economic Review (a12, b22; second-hand only).
- Budden et al. (2008) claimed double-blind review raised female first authorship (b06, abstract); Webb et al. (2008) disputed it (b07, title only, direction not verified).
- Snodgrass (2006) surveyed 600+ items: large literature, few controlled studies (b23, second-hand).

### 2.4 Mitroff 1974: counter-norms (a04, a05, b03, d08, d09)
The American Sociological Review paper (39(4), doi 10.2307/2094423) was **not opened** in any session. What we know:

- Secondary sources give the four pairs: secrecy vs communism, particularism vs universalism, interestedness vs disinterestedness, organised dogmatism vs organised scepticism.
- The companion NASA report (Mitroff 1973, opened, d08, d09) says: over 40 scientists, each interviewed four times over three years (between Apollo 11/12, 12/14, 14/15, 15/16). A typology of three types refined to six. A 10-scale semantic differential. Virtually the whole sample "derided the dispassionate observer". Mitroff argues progress comes from committed advocates testing their discoveries against each other. Three Type I (bold, theory-first) scientists were named again and again as most committed to pet hypotheses.
- The "42 scientists over 3.5 years" figure comes from a search snippet and does not match the report (critique.md). Treat as unverified.
- No per-norm numbers have been seen. Do not quote any.

### 2.5 Formal models of credit and division of labour (a14, a15; not opened)
Kitcher (1990) and Strevens (2003) model scientists who seek credit. A winner-take-all priority rule pushes selfish scientists to spread effort over rival programmes, in a way that can match the social optimum. Everyone following the single best-looking method is worse. Summaries here are from memory only. The agent-side lesson (diversity needs different priors) is tested in d10-d12, not in these models.

### 2.6 Modern human tests (2007-2022)
- Anderson, Martinson, De Vries (2007), normative dissonance: scientists see colleagues as more counter-normative than normative; competitive fields more so (b01, abstract; a08 record only).
- Anderson et al. (2010) extended the norms with surveys (a06, a07, b02, opened). Section 3.
- Tomkins, Zhang, Heavlin (2017): WSDM 2017 controlled experiment (a11, b05, opened).
- Huber et al. (2022): Nobel vs novice field experiment (a10, b04, d07, opened).
- Bol, de Vaan, van de Rijt (2018): Matthew effect in funding by regression discontinuity (b08, abstract).
- Camerer et al. (2018) and Errington et al. (2021): organised scepticism applied at scale (d05, d06, opened).

### 2.7 The LLM turn (2023-2025)
Once LLMs began to review papers, judge answers and propose ideas, every Merton breach reappeared in a new form (sections 3 and 6). Two additional lines matter. First, simulations of whole review systems with LLM agents (AgentReview). Second, "AI scientist" pipelines that contain a built-in sceptic (novelty check, reflection agent, tournament).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Scientists endorse Mertonian norms | 73-91% endorse (quality 91%, governance 80%). Survey of 3,600 mid-career NIH R01 grantees (52% response) and 4,160 postdocs (43%); 6 focus groups, 51 scientists | Anderson 2010 (a06, b02) | [E] for self-report of "should" |
| Scientists reject Mitroff counter-norms | 18-23% endorse; self-interestedness 33% mid-career, 25% early. Only 7 of 32 discipline chi-square tests significant | Anderson 2010 (a06, b02) | [E] |
| Normative dissonance | Others seen as more counter-normative than normative. N=3,247 | Anderson 2007 (b01, abstract) | [E] with 2010 |
| Early-career scientists endorse scepticism more | Per-item gaps only in a figure, not read | Anderson 2010 (a07) | [S] |
| Universalism fails: same paper, three names | Reject 22.6-23% (Nobel), 48.2% (anonymous), 65.4% (junior). Accept or minor revision 58.8 / 23.6 / 9.9%. Invitation accepted 38.5 / 30.7 / 28.5% (3,299 invitations, 2,611 replies; anon vs prominent p=0.0031) | Huber 2022 (a10, b04, d07) | [S] one paper, one field |
| Single-blind reviewers favour fame and rank | Odds 1.63 famous author, 1.58 top university (p=0.012), 2.10 top company (p=0.002); female 0.78 not significant alone (significant in the paper's meta-analysis); 0.57-0.92 SD quality shift; single-blind reviewers bid for 22% fewer papers | Tomkins 2017 (a11, b05, b26) | [E] with Huber and Blank |
| Matthew effect in funding | Winners just above threshold got more than twice later funding in 8 years (about 180,000 euro); part of the gap is losers applying less | Bol 2018 (b08, abstract) | [S] |
| Organised scepticism: social science | 13 of 21 (62%) replicated, range 12-14 by indicator; replication effect about 50% of original; samples about 5x larger; Bayesian true-positive rate 67% | Camerer 2018 (d05) | [E] |
| Organised scepticism: cancer biology | 50 experiments, 23 papers, 158 effects (136 positive, 22 null). Median effect 85% smaller; 92% smaller. Success: positive effects 40% (39/97), null 80% (12/15), combined 46% (51/112) | Errington 2021 (d06) | [E] |
| LLM judge leaks prestige (preprint) | Positive-rating share 36.8% to 40.8% (famous university), 41.6% (company), 41.2% (named authors); 500 papers | Ye 2024 (a19, c13) | [E] with Pataranutaporn |
| LLM judge leaks prestige (economics) | GPT-4o: top male authors +0.39 points (SE 0.042). Over 29,000 evaluations of 1,220 papers (110 journals); 8,910 evaluations on 330 papers. 3 of 4 models biased; Claude 3.5 not listed as biased | Pataranutaporn 2025 (a20, d04) | [E] |
| LLM prestige: size depends on measure (hard score) | 10 PNAS papers, 402,500 responses. Identity shown: reviewer reject 6.7% to 5.0% (-1.7 pp, about -25% relative); quality +1.0% (reviewer), +2.4% (editor). Only prestige survives Holm correction | Howell 2025 (a21, d01, d02) | [S], one model |
| LLM prestige: size depends on measure (soft score) | 252 ICLR 2025 papers, 7 models. Strong-ranked-university win rate 66.0-94.2% on token-probability ratings, all p<0.01. Ministral 8B: 4.3% on hard rating, 68.6% on soft rating | Vasu 2025 (d03) | [S] |
| Order flips LLM verdict | ChatGPT judge: Vicuna-13B beats ChatGPT on 66/80 queries by reorder. Win rate 2.5% first vs 82.5% second (ChatGPT), GPT-4 51.3% vs 23.8% | Wang 2023 (a26, b12) | [E] |
| Position consistency | GPT-4 65.0%, GPT-3.5 46.2%, Claude-v1 23.8% (75.0% favour first); few-shot GPT-4 to 77.5%. GPT-4 vs human agreement 85% (no ties) vs human-human 81% | Zheng 2023 (a27, b11) | [E] |
| Judge remedies | Math grading failures 14/20 default, 6/20 chain-of-thought, 3/20 with reference | Zheng 2023 (a27) | [E] (10 questions only) |
| Self-preference | GPT-4 self-win bias +10%, Claude-v1 +25%, GPT-3.5 none. Self-recognition linear with self-preference; over 90% after fine-tuning on 500 examples (GPT-3.5, Llama 2). The "73.5% GPT-4" figure is not verified from the abstract | Zheng 2023 (b11); Panickssery 2024 (a25, b14, c16) | [E] |
| Verbosity and attack | Repetitive-list attack failure: Claude-v1 91.3%, GPT-3.5 91.3%, GPT-4 8.7% | Zheng 2023 (a27) | [S] |
| LLM committee conformity (simulation) | SD of ratings -27.2% after rebuttal; one lazy reviewer cuts others' commitment 18.7%; 37.1% of decisions vary with reviewer bias; known identity on 10% of papers changes decisions 27.7%; Jaccard vs baseline 0.364, 0.154, 0.008 for 1, 2, 3 informed reviewers; authoritarian chair kappa 0.266 | Jin 2024 AgentReview (a22, b19, c01-c03) | [S] simulation |
| Hidden-text injection | Mean rating 5.34 to 7.99; agreement with human reviews 53% to 16%; agreement with injected content about 90%; 5% of reviews manipulated pushes 12% of papers out of top 30%; LLMs 4.5x more consistent with author-disclosed limitations | Ye 2024 (a19, b18, c14, c20) | [E] |
| Injection (second study) | 26 bioRxiv preprints, 3 LLMs: +20% acceptance. A caution prompt reverts it but lowers all scores. Detection Gemini 96.6% vs Llama 18.3% (from claims K13) | OSF preprint 2025 (d14) | [S] |
| Optimised injection on pairwise judges | Success 88-98.9% by model and setting; perplexity detectors miss 70% | Shi 2024 JudgeDeceiver (d13) | [S] |
| Empty-paper acceptance | Title-only paper rated at or above 42% of full papers; introduction only reaches over 95% of full-paper rating | Ye 2024 (c14, c20) | [S] |
| AI-assisted reviewing is widespread | 6.5-16.9% of review text LLM-modified: ICLR 2024 10.6%, NeurIPS 2023 9.1%, CoRL 2023 6.5%, EMNLP 2023 16.9%. Before ChatGPT about 1.6-2.4% | Liang 2024 (a17, c11, c26) | [E] |
| AI-assisted reviews are lenient | At least 15.8% of ICLR 2024 reviews. AI-assisted review scored higher in 53.4% of discordant pairs (p=0.002; +14.4%). Borderline papers +4.9 pp acceptance (p=0.024) | Latona 2024 (a18, b15, c10) | [E] |
| GPT-4 feedback overlap | 30.85% vs human-human 28.58% (3,096 Nature-family papers); 39.23% vs 35.25% (1,709 ICLR papers); 43.80% for rejected ICLR; 308 researchers at 110 institutions, 57.4% helpful, 82.4% better than at least some human reviews | Liang 2023 (a16, b16, c12) | [C] overlap is not quality |
| Expert annotation of LLM reviews | More deficient segments than human reviews; low diversity; summaries are an LLM strength (0.19% vs 0.36% inaccurate summary segments) | Du 2024 ReviewCritique (c18) | [S] |
| LLM reviewer near human | GPT-4o with 5 reflections, 5-review ensemble, 1-shot: accuracy 70%, balanced 0.65 vs human 0.66, F1 0.57 vs 0.49, AUC 0.65 both. Human FNR 0.52, FPR 0.17 | Lu 2024 (c06, c22) | [S] |
| LLM ideas judged more novel | Novelty human 4.84, AI 5.64, AI reranked 5.81 (79 reviewers, 49 ideas per arm; p<0.05). Overall: 4.68, 4.85 (n.s.), 5.34 (p=0.04). Novelty r=0.725 with overall score; feasibility r=0.097 | Si 2024 (a23, c04) | [S] |
| LLM idea diversity and judges | About 200 of 4,000 seed ideas (5%) non-duplicate at similarity 0.8. Reviewer agreement 56.1% (NeurIPS 2021 66.0%, ICLR 2024 71.9%). LLM judges 43-53% pairwise; Claude-3.5 zero-shot ranker 71.4% on ICLR accepted-vs-rejected, GPT-4o 61.1% | Si 2024 (c05, c25, b21) | [S] |
| Automated science without real sceptic | 5/12 experiments (42%) failed; median 5 citations; 5 of 34 recent; micro-batching labelled novel; up to 10 keyword search rounds then default novel=True | Beel 2025 (a24, c07, c21) | [E] with c09 |
| Search makes the novelty sceptic work | Reflection agent without search rated known non-novel ideas 6.14/10; with search 2.38/10. Correctness 7.4 to 8.46 | Gottweis 2025 co-scientist (c09) | [S] |
| Agent replication of papers | 20 ICML 2024 papers, 8,316 gradable tasks: Claude 3.5 Sonnet (New) 21.0%, o1 13.2%, others under 10%; human PhD baseline 41.4% on 3 papers | PaperBench (c17) | [S] |
| AI workshop paper | 1 of 3 AI-written papers scored 6.33 (about top 45%) at an ICLR workshop | AI Scientist v2 (c08) | [S] |
| Gated reviewer feedback | Over 20,000 reviews randomised; 27% of reviewers updated; over 12,000 suggestions incorporated; +80 words vs +2; over 96% of feedback passed all tests; score edits 8.1% vs 7.5% | Thakkar 2025 (a28, b20, c15, c24) | [S] |
| Self-critique without tools | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0; HotpotQA 49.0 to 43.0 | Huang 2024 (d15) | [E] |
| Critique with tools | AmbigNQ EM CoT 44.2, CRITIC 50.0, CRITIC without tool 42.0; TriviaQA 72.7 vs 67.3; HotpotQA 38.7 vs 34.9; math 72.2 vs 68.3 | CRITIC (d16) | [E] |
| Debate vs vote | Qwen2.5-7B: single 0.7205, vote 0.7691, decentralised debate T=2 0.7377, T=5 0.7050, centralised T=2 0.6551. Arithmetic single 0.8140, vote 0.9900 | Choi 2025 (d11) | [S] |
| Debate rarely beats CoT | 36 configs: debate beats CoT in about 15%; self-consistency usually best. Heter-MAD (two models) +6.4% over single-model debate average | Zhang 2025 (d10) | [S] |
| Model diversity in debate | 91% GSM-8K for three different models vs 82% for three Gemini-Pro copies; ASDiv 94% | Diversity of Thought (d12) | [S] |

## 4. Mechanisms and models

Each mechanism is written so an engineer can code it. All move Merton's social controls into code around one model.

### 4.1 Universalism as input stripping plus swap tests
**Mechanism.** A judge's score should be a function of the content only. Identity cues (author, institution, "renowned", a stated prior verdict, order position, length) are nuisance inputs.

- **Strip in code.** Remove names, affiliations, links, "as I said", stated guesses and prior scores from the text before the judge sees it. Use regex and a fixed list; do not ask a model to strip.
- **Swap test (audit).** Take N items. For each, build variants: identity added, identity swapped, order reversed, length padded, injection sentence added. Score each variant. Report mean shift in score points and flip rate of the verdict. This is how Huber, Tomkins, Ye, Pataranutaporn and Howell measure bias.
- **Use soft scores.** Howell found a 1.7 pp reject shift on hard integer ratings; Vasu found 66-94% preference on token-probability ratings with the same family of models. If the API gives logprobs, audit on probabilities, not on integers (d03).
- **Both orders.** For pairs, run A-B and B-A in code and accept only a verdict that holds in both. Otherwise call it a tie or a hard case (Wang b25 flags hard cases by balanced-position entropy).

### 4.2 Organised scepticism as a separate, tooled check
**Mechanism.** The doubter must have something the author lacks: a tool, an executed test, a held-out input, retrieval, or a different model.

- **Sceptic with tools.** CRITIC: the critique step calls search or code and revises from the output (d16). Without the tool the same loop is flat or harmful (d15).
- **Search-backed novelty.** The co-scientist reflection agent with search dropped the novelty of known ideas from 6.14 to 2.38 (c09). The AI Scientist's keyword loop with a default "novel=True" failed (c21, a24).
- **Shrinkage prior.** A confirmed claim is not a true claim. Human single studies replicate at 62% (effect halves) and 46% (effect 85% smaller) (d05, d06). Keep a per-class record of how often the agent's own "confirmed" answers survive a fresh check, and shrink confidence by that rate.

### 4.3 Disinterestedness as role separation
**Mechanism.** The party who produces an answer must not choose it. The disinterest is structural: code, a different model, or a stripped judge selects. LLM evidence: self-preference grows linearly with self-recognition (c16), self-win bias +10% (GPT-4) and +25% (Claude-v1) (b11). A generator-as-judge is interested by construction.

### 4.4 Committee dynamics to avoid (conformity, authority, fatigue)
AgentReview (c01-c03) models reviewers as LLM personas. After seeing each other, rating SD falls 27.2%. Informed reviewers shift the accepted set (Jaccard 0.364 with one informed reviewer). A lazy reviewer cuts others' effort 18.7%. Engineering rule: collect independent verdicts first, aggregate in code, never show earlier verdicts to later judges. Debate adds conformity cost (centralised debate 0.6551 vs single 0.7205, d11).

### 4.5 Counter-norm as advocacy phase (Mitroff)
**Idea.** Mitroff's committed advocate is a feature: a strong case for one hypothesis, then attack by others. In code: stage 1, for each candidate, a role writes the best case and the test that would show it wrong; stage 2, a different context runs the tests. Untested on LLMs (K26, d08, d09). It conflicts with G1 (doubt only on a signal) only if the attack stage runs on a schedule; it can run on a signal (disagreement among candidates).

### 4.6 Credit and diversity (Kitcher/Strevens)
Effort should spread over rival programmes. For the agent: assign untried directions in code (already in S3 open mode). The LLM-side question is whether diversity of prompts counts as diversity of priors. Evidence says role prompts did not help debate (d11) while different models did (d12, d10). Cost-matched tests are missing.

### 4.7 Gating output through reliability tests
Thakkar's pipeline sent feedback only if it passed tests (96% did) (c24). Principle: a critique goes to the next step only after code checks that it cites real output, is specific, and is not an instruction to accept.

### 4.8 Prompt injection as an "interested author"
A candidate answer or document can carry text that addresses the judge (c14, d13, d14). Sanitise in code: remove imperative text aimed at graders, hidden characters and formatting tricks, and present candidate text inside a quoted data block. Prompt-only caution reverted the effect but lowered all scores (d14).

## 5. What holds up

### 5.1 Replications and agreement
- **Prestige bias in human review** is shown in several designs: Huber (field, finance), Tomkins (WSDM, 1.58-2.10 odds), Blank (AER, second-hand), Bol (funding, Matthew effect). Direction agrees. Sizes differ. Tomkins' famous-author effect is smaller than the aggregate of six other studies (b05). [E] for direction; magnitude not portable.
- **LLM prestige bias** is shown by Ye (500 papers), Pataranutaporn (3 of 4 models), Howell (one model), Vasu (7 models, soft scores). Direction agrees (K07, K08). [E] for direction.
- **Position bias, self-preference, verbosity** are replicated across at least Wang, Zheng and Panickssery with different models (K09, K11). [E].
- **Self-critique without tools fails, with tools works:** Huang and CRITIC agree (K24). [E].

### 5.2 Failures, conflicts and boundary conditions
- **Claude and author prominence.** Claude 3.5 not listed as biased in the economics audit (a20, d04). A bias found in GPT does not transfer to our judge.
- **Hard vs soft scores.** The same bias looks small (1.7 pp, about 1% quality) in one design and large (66-94%) in another. Neither is "the" size (K08).
- **Gender.** Tomkins' female effect is not significant alone but significant in meta-analysis; do not cite "no gender effect". Howell: gender and race mostly vanish after Holm correction (d02). Budden vs Webb is disputed; Webb's direction not verified (b06, b07).
- **Camerer 2018** replicated 62% with half-size effects. **Errington 2021** replicated 46% (40% positive). Replication difficulty included unclear methods (b10). Selected high-profile papers; not a base rate for all science.
- **Anderson surveys** measure what scientists say they should do, not what they do; US biomedical only; response rates 43-52%; only 7 of 32 discipline tests significant (b02). Mitroff and Anderson are not in true conflict: ought vs practice (critique).
- **LLM review parity.** Liang's overlap parity (30.85 vs 28.58) is overlap of comment points. Du's expert annotation finds LLM reviews more deficient and less diverse (K15 [C]). Human consistency is itself low (FNR 0.52, c22), so "human-level" is a low bar.
- **Simulation validity.** AgentReview is checked against sociological theory only, not real decisions (K12). One source.
- **Ideas.** Si's novelty gain is by blind human judgment, not execution; 5% non-duplicates; LLM judges near chance (K16).
- **Debate.** Debate often equals sampling plus vote (d11) and rarely beats CoT (d10). Heterogeneous models help (d10, d12), but no equal-token test against N copies of the best model exists.
- **Code-level sanitising** of injections is untested; prompt defences cost score level (d14).

### 5.3 Interventions that worked
- Swapping order and averaging; evidence before score; a reference answer (14/20 to 3/20 grading failures) (a27, b25).
- Few-shot examples for judge consistency (65.0% to 77.5%, GPT-4) (b11).
- Tool-backed critique (CRITIC) and search-backed novelty (6.14 to 2.38).
- Majority vote over independent samples (0.7205 to 0.7691) (d11).
- Gating feedback by automated tests (27% of reviewers updated) (c15).
- Anonymisation (double-blind) removes the visible-cue bias in humans by design (Tomkins), though the Budden claim is disputed.

### 5.4 Interventions that did not work
- Self-critique without external information (d15).
- Persona or role-prompt diversity inside debate (d11).
- Centralised debate (0.6551, below single agent) (d11).
- Caution prompt against injection: reverts the effect, lowers all ratings (d14).
- LLM judges as idea selectors (43-53% pairwise) (c05).
- Keyword novelty search with default-pass (c21).

## 6. Language models

### 6.1 As judges and referees
- **Order.** ChatGPT judge flips on order alone (Vicuna-13B beats ChatGPT 66/80). Position consistency: Claude-v1 23.8%, GPT-3.5 46.2%, GPT-4 65.0%. Few-shot lifts GPT-4 to 77.5%. These are 2023 models; newer models are not measured here (older models only).
- **Self-preference.** GPT-4 +10%, Claude-v1 +25% self-win in MT-Bench. Linear with self-recognition. Fine-tuning for recognition raises preference (causal evidence).
- **Verbosity and list attack.** Repetitive-list attack failed Claude-v1 and GPT-3.5 91.3%, GPT-4 8.7%.
- **Accuracy.** GPT-4 agrees with humans 85% (no ties) vs human-human 81% on MT-Bench. Humans changed their choice in 34% of disagreements when shown GPT-4's view (b24), a sign of anchoring.

### 6.2 As reviewers
- **Prestige.** +4 points in positive share (Ye); +0.39 rating (GPT-4o, Pataranutaporn); -1.7 pp reject (Howell, GPT-4o-mini); 66-94% preference in soft scores (Vasu).
- **Manipulation.** Hidden text raises mean rating 5.34 to 7.99. Agreement with humans drops 53% to 16%. Optimised injections succeed 88-98.9% on open pairwise judges. Detection: Gemini 96.6% vs Llama 18.3% (K13).
- **Leniency.** AI-assisted reviews score higher in 53.4% of discordant pairs; +4.9 pp acceptance near the threshold.
- **Weak reading.** A title-only paper is rated at or above 42% of full papers; introduction-only reaches over 95% of the full rating.
- **Useful but not equal.** Overlap of points with humans equals human-human (30.85 vs 28.58). Expert annotation finds more deficient and less diverse reviews (c18).

### 6.3 As committees (simulated)
Conformity (SD -27.2%), authority bias (27.7% decision change with 10% informed), fatigue (-18.7%), amplification of bias (0.17 and 0.25 drops). Simulation only.

### 6.4 As idea generators and sceptics
- Ideas judged more novel by blind experts (5.64 vs 4.84, rerank 5.81) but 5% unique among 4,000, and LLM selectors near chance. G8 stands.
- A sceptic without search fails (6.14/10 novelty for known ideas). With search 2.38.
- Replicating papers is hard: 21.0% for the best model on PaperBench vs 41.4% human baseline (3 papers).
- Self-critique alone makes things worse (GPT-3.5 75.8 to 38.1).

### 6.5 What changed behaviour, by how much
| Change | Effect |
|---|---|
| Reference answer in math judging | failures 14/20 to 3/20 |
| Chain-of-thought in judging | 14/20 to 6/20 |
| Few-shot examples in judge prompt | GPT-4 consistency 65.0% to 77.5% |
| Different models in debate vs copies | 91% vs 82% (GSM-8K) |
| Vote over debate | 0.7691 vs 0.7377 |
| Search for the novelty sceptic | 6.14 to 2.38 |
| Tools in critique | AmbigNQ 42.0 to 50.0 |
| Caution prompt vs injection | removes +20% acceptance, lowers all scores |
| Gating by tests | 27% of reviewers updated; 96% pass rate |

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Evidence ids are from the evidence files.

### Add now (established)
1. **[E] G5 / S7: judges and selectors see content only.** Strip names, affiliations, stated guesses and prior scores in code before any model judge. Both orders for pairs; accept only verdicts that hold in both. Evidence: a10, a11, a19, a20, a26, a27, b11, b12, d03 (K03, K04, K07, K08, K09). G5 already says this in part; the additions are explicit identity stripping, the both-order check and soft scores where available.
2. **[E] G5 / G8: the generator never judges its own output.** Selection by code, by execution, or by a different model on stripped text. Evidence: a25, b11, c16, c05 (K11, K16).
3. **[E] G3 / S4 / S7: a doubting step needs an outside source.** A critique step must call code, a test or retrieval, or come from a different model; same-model doubt without new information is dropped. Evidence: d15, d16, c09 (K24, K17). Consistent with G2 and section 4b (self-reflection).
4. **[E] G4 / G9: collect independent judgments before any aggregation; do not show earlier verdicts.** A vote over independent samples is the baseline any debate or committee must beat. Evidence: c01-c03, d10, d11 (K22, K23 are [S], but G9 is already [E]).
5. **[E] G5 / S1: sanitise input for text addressed to the judge.** Candidate text goes in a quoted data block; imperative sentences aimed at graders and hidden characters are removed in code. Evidence: a19, c14, d13, d14 (K13). The harm is [E]; the effect of sanitising is untested.
6. **[E] M / G3: shrinkage for confirmed claims.** The class record keeps the rate at which "confirmed" answers survive a fresh check and lowers confidence by that rate. Human anchors: 62% and 46%. Evidence: d05, d06 (K06). The mechanism is [E]; the value for LLM claims is untested.
7. **[E] G5: calibrate LLM-grader leniency against a code-checked label.** AI-assisted reviews score higher (53.4% of discordant pairs). Evidence: a18, c10 (K14).

### Test first
1. **[S] G5: swap-test our exact judge.** Add or swap identity and prestige text; measure shift in points and in logprob. Evidence: d01-d04 (K08). Decides whether stripping is needed always or only in some uses.
2. **[S] S4/S7 + G3: tool-backed sceptic vs same-model doubt vs different-model doubt.** Evidence: d15, d16, c09 (K24).
3. **[C] G1 / O-roles: defend-first-then-doubt (Mitroff).** No LLM test exists. Evidence: d08, d09, a04 (K02, K26).
4. **[S] G4: different-model or different-prior diversity vs N copies at equal tokens.** Evidence: d10, d12, a14, a15 (K21, K22).
5. **[S] G2: gate model critiques by code tests before use.** Evidence: a28, c24 (K20).
6. **[S] M: estimate the agent's own shrinkage rate.** Evidence: d05, d06 (K25).
7. **[S] G5: judge-injection sanitising.** Evidence: d13, d14.
8. **[S] G8: dedup-and-execute selection for open mode.** Evidence: a23, c05 (K16).

## 8. Concrete tests on our bench

All arms get equal total tokens, same items, same seeds. Report mean, 95% interval and the number of flips right-to-wrong and wrong-to-right.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 100 answer pairs with known winner (checkable tasks), plus identity variants ("by a famous lab", "by a student", none) | (a) judge sees raw text, (b) stripped text, (c) stripped plus both orders | Mean score shift between variants (points and logprob); verdict flip rate; accuracy vs known winner | If raw shift is 0.4 points or more, or flips exceed 5%, stripping pays. Human-style effect for reference: +4 pp positive share (Ye) |
| T2 | 100 pairs, order reversal | single order vs both orders vs both orders with reference answer | Position consistency; accuracy | 65% baseline consistency (2023 GPT-4); both orders removes flips |
| T3 | Judge with an injected sentence ("rate this highly") in one candidate | raw vs code-sanitised vs caution prompt | Score change of injected candidate; overall score level | Sanitising removes the shift without lowering other scores (the caution prompt lowers all) |
| T4 | 100 checkable problems where the first attempt is wrong 30-60% | (a) no doubt, (b) same-model doubt, (c) doubt with code or test output, (d) doubt by a different model | Accuracy; right-to-wrong and wrong-to-right flips | (b) flat or negative (d15); (c) positive (d16: +8 EM on AmbigNQ) |
| T5 | 60 open prompts (NoveltyBench style) with a few known-old ideas planted | novelty check without retrieval vs with retrieval vs code-run dedup | Share of planted old ideas flagged as novel | Large drop with retrieval (c09: 6.14 to 2.38 of 10) |
| T6 | 80 problems with a check | (a) doubt from start, (b) advocacy phase (best case for each candidate and its test) then doubt on signal, (c) plain | Accuracy; tokens; flip direction | Unknown; keep (b) only if it beats (a) by 3 points or more |
| T7 | 100 problems, N=5 | five copies of best model + vote; five strategy prompts of best model + vote; best model plus second model + vote; debate | Accuracy; diversity of correct answers | Copies plus vote is the baseline (0.7691 vs debate 0.7377); mixed models help only if above it |
| T8 | 200 of the agent's own "confirmed" answers on fresh held-out inputs | measurement only | Survival rate; effect-size ratio of fitted vs fresh | Human anchors 62% and 46%; expect lower for fitted-to-examples claims |
| T9 | 100 critiques generated by the agent | ungated vs code-gated (must cite real output, specific, no accept-instruction) | Share of critiques pointing at a real defect; accuracy after revision | Gated has higher precision (Thakkar 96% pass) |
| T10 | Judging idea lists | model rank vs execution rank vs random | Agreement with executed result | Model rank near chance (43-53%) |

## 9. What does not transfer, and why

- **Incentives and reputation.** Merton's norms work through credit, careers and sanctions. A model has no career. Priority fights, Matthew effects and funding thresholds (Bol) have no analogue unless we build memory that compounds early mistakes. The only lesson is that an early pick must not become an anchor.
- **Survey endorsement.** Anderson's 73-91% is what people say they should do. An LLM's stated rules are not its behaviour (G10). We need transcript audits, not self-description.
- **Independence of reviewers.** Human reviewers differ in training and priors. Copies of one model share errors (G4). Sociology's "many scientists" is not "many samples".
- **Meaning of prestige.** A laureate's name carries real information about quality (b04 limits). An LLM judge's prestige bias is mostly pretraining statistics. Human effect sizes do not give our judge's effect size.
- **Mitroff's advocacy.** Commitment in humans comes from ego and sunk cost. A model can be told to defend, but its defence is not a stake. The benefit of commitment (persistence under test) may need another mechanism.
- **Replication rates.** 62% and 46% are for published human experiments with selection and publication bias. They are anchors for a prior, not predictions for LLM output.
- **Peer-review simulations.** AgentReview is persona-driven and validated against theory only. Do not size our committee effects from it.
- **Formal credit models** (Kitcher, Strevens) assume agents that choose programmes by payoff; our code assigns directions. Only the diversity lesson carries.
- **Venue-specific data.** Almost all LLM numbers are ICLR, NLP or economics, often preprints, often an LLM judge of an LLM reviewer (critique).

## 10. Open questions

1. What does Mitroff 1974 report per norm? Is "42 scientists, 3.5 years" real? (needs the full ASR paper)
2. Does our exact judge shift under identity cues, and how does that compare to the roughly 4-point human-style effect? Hard vs soft scores?
3. Does a defend-first phase help or hurt vs doubting from the start at equal tokens?
4. Is the co-scientist drop (6.14 to 2.38) due to search alone? A controlled ablation is missing.
5. Do independent models reduce conformity and self-preference vs N copies of one model in a real task at equal tokens?
6. What is the shrinkage rate for LLM-generated "confirmed" claims?
7. Does the Huber result hold outside finance, or replicate with a second paper?
8. How big is injection harm for non-review judges, and does code-level sanitising remove it?
9. Do the Strevens and Kitcher models have an LLM analogue: prompt diversity vs model diversity?
10. Are there post-2025 replications of the 15.8% AI-assisted review rate or the 12% top-30% displacement?
11. Do newer models (post-2024) keep the 2023 position and self-preference numbers?
12. Can any benefit be shown for the "communism" norm (shared memory of lessons across runs), as opposed to the "scepticism" norm?

## 11. Sources

[V] opened (page or text read). [M] snippet, abstract, record or second-hand only.

**Merton and norms**
- [V] Merton (1942) Science and Democratic Social Structure, reprint. https://www.panarchy.org/merton/science.html (a01-a03)
- [M] Mitroff (1974) Norms and counter-norms in a select group of the Apollo moon scientists, ASR 39(4). https://doi.org/10.2307/2094423 (a04)
- [V] Mitroff (1973) NASA technical report, social psychology of science. https://ntrs.nasa.gov/citations/19730009395 (d08, d09)
- [V] Wikipedia, Mertonian norms (naming only). https://en.wikipedia.org/wiki/Mertonian_norms (a05)
- [V] Anderson et al. (2010) Extending the Mertonian norms. https://pmc.ncbi.nlm.nih.gov/articles/PMC2995462 (a06, a07, b02, b03)
- [M] Anderson, Martinson, De Vries (2007) Normative dissonance. https://doi.org/10.1525/jer.2007.2.4.3 (a08, b01)
- [M] Merton (1968) The Matthew effect in science (via Wikipedia, Huber). https://en.wikipedia.org/wiki/Matthew_effect (a09)
- [M] Bol, de Vaan, van de Rijt (2018) The Matthew effect in science funding. https://pmc.ncbi.nlm.nih.gov/articles/PMC5948972/ (b08)
- [M] Strevens (2003) The role of the priority rule in science (a14, memory); Kitcher (1990) The division of cognitive labor (a15, memory). No URL opened.

**Human peer review and replication**
- [V] Huber et al. (2022) Nobel and novice. https://doi.org/10.1073/pnas.2205779119 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9564227/ (a10, b04, d07)
- [V] Tomkins, Zhang, Heavlin (2017) Single versus double blind reviewing at WSDM 2017. https://arxiv.org/abs/1702.00502 (a11, b05, b22, b23, b26)
- [M] Blank (1991) AER double-blind study (a12), via Tomkins. Peters and Ceci (1982) (a13), memory. Budden et al. (2008) https://doi.org/10.1016/j.tree.2007.07.008 (b06). Webb et al. (2008) https://doi.org/10.1016/j.tree.2008.03.003 (b07, title only).
- [V] Camerer et al. (2018) https://doi.org/10.1038/s41562-018-0399-z (d05; b09 abstract)
- [V] Errington et al. (2021) https://doi.org/10.7554/eLife.71601 (d06; b10 https://pmc.ncbi.nlm.nih.gov/articles/PMC8651293/)

**LLM peer review and judging**
- [V] Liang et al. (2023) https://arxiv.org/abs/2310.01783 (a16, b16, c12)
- [V] Liang et al. (2024) https://arxiv.org/abs/2403.07183 (a17, b17, c11, c26)
- [V] Latona et al. (2024) https://arxiv.org/abs/2405.02150 (a18, b15, c10)
- [V] Ye et al. (2024) Are we there yet? https://arxiv.org/abs/2412.01708 (a19, b18, c13, c14, c20)
- [V] Pataranutaporn et al. (2025) https://arxiv.org/abs/2502.00070 (a20, d04)
- [V] Howell et al. (2025) Prestige over merit. https://arxiv.org/abs/2509.15122 (a21, d01, d02)
- [V] Vasu et al. (2025) Justice in Judgment. https://arxiv.org/abs/2509.13400 (d03)
- [V] Jin et al. (2024) AgentReview. https://arxiv.org/abs/2406.12708 (a22, b19, c01-c03)
- [V] Thakkar et al. (2025) https://arxiv.org/abs/2504.09737 (a28, b20, c15, c24)
- [V] Du et al. (2024) ReviewCritique. https://arxiv.org/abs/2406.16253 (c18)
- [V] Tyser et al. (2024) https://arxiv.org/abs/2408.10365 (c19)
- [V] Wang et al. (2023) Large language models are not fair evaluators. https://arxiv.org/abs/2305.17926 (a26, b12, b25)
- [V] Zheng et al. (2023) MT-Bench and Chatbot Arena. https://arxiv.org/abs/2306.05685 (a27, b11, b24)
- [V] Ye et al. (2024) CALM. https://arxiv.org/abs/2410.02736 (b13; intro and method only, per-bias numbers not extracted)
- [V] Panickssery et al. (2024) https://arxiv.org/abs/2404.13076 (a25, b14, c16)
- [V] Shi et al. (2024) JudgeDeceiver. https://arxiv.org/abs/2403.17710 (d13)
- [V] Defenses against LLM prompt injections in academic peer review (2025, OSF preprint; abstract read). https://doi.org/10.31234/osf.io/zxuwf_v2 (d14)

**AI scientist, ideas, scepticism, debate**
- [V] Si, Yang, Hashimoto (2024) https://arxiv.org/abs/2409.04109 (a23, b21, c04, c05, c25)
- [V] Lu et al. (2024) The AI Scientist. https://arxiv.org/abs/2408.06292 (c06, c22)
- [V] Beel and Baumgart (2025) https://arxiv.org/abs/2502.14297 (a24, c07, c21)
- [V] Yamada et al. (2025) AI Scientist-v2. https://arxiv.org/abs/2504.08066 (c08)
- [V] Gottweis et al. (2025) Towards an AI co-scientist. https://arxiv.org/abs/2502.18864 (c09, c23)
- [V] Starace et al. (2025) PaperBench. https://arxiv.org/abs/2504.01848 (c17)
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788 (d10)
- [V] Choi, Zhu, Li (2025) Debate or Vote. https://arxiv.org/abs/2508.17536 (d11)
- [V] Diversity of Thought elicits stronger reasoning in multi-agent debate. https://arxiv.org/abs/2410.12853 (d12)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d15)
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (d16)
