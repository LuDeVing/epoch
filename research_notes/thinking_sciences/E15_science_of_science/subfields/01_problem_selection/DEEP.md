# Problem selection: deep document

*Subfield E15.01 (science of science). Built from evidence_a-d.jsonl (a01-a25, b01-b34, c01-c27, d01-d18), claims.jsonl (K01-K29) and critique.md in this folder. Ids like a05 point to evidence lines; K12 points to claims. The critique corrections are applied (for example per-idea novelty 4.86/5.62/5.78, not the excitement numbers).*

## 1. What it is

Problem selection is the choice of which question to work on. In human science it is the choice of a research question, topic, hypothesis or direction. The field asks four things.

1. What do scientists pick? Mostly safe, repeated links (Foster et al. 2015 [b08]).
2. What does the pick cost or pay? Novel and pivoting work pays later and with more variance, and is penalised early (Wang 2017 [b13-b16], Hill 2025 [b19-b22]).
3. Can anyone tell good questions from bad ones before the work is done? Barely. Experts agree on 56% of pairs [a02]. Prompted LLMs are near chance [K05]. Models trained on outcomes do better [K06].
4. Can a machine generate and choose questions? It can generate ones that look novel. It cannot reliably tell which are good, and many are rewrites [K01, K07, K08].

Fortunato et al. 2018 (Science, abstract only [a20]) lists topic choice among the open topics of the field. Foster, Rzhetsky and Evans 2015 is the key quantitative study.

For our agent this is the S0 gate and the "open" mode. When the task is open (no single exact answer, no check), the agent must decide what to work on, whether the question is already answered, and whether it is worth the tokens. The schema says S0 is "[S] every field asks for it, none supplies one". This document supplies what the literature has.

Scope note. Almost all LLM evidence is about NLP and AI research ideas. Nothing was found for debugging, engineering or business problem choice, except one product-idea study [d07]. Transfer to our agent's tasks is untested.

## 2. History and theories in depth

### 2.1 Philosophy of science: the essential tension
- Kuhn 1959, "The Essential Tension" [a22, from memory, not opened]: science needs tradition (work inside an accepted paradigm) and innovation (break from it). Too much of either stalls the field.
- Kitcher 1990, "The division of cognitive labor" [a22, not opened]: the community is best served when scientists spread across approaches, even if each alone would pick the best-looking one. Selfish choice and collective optimum differ.
- No numbers from either. They frame the later work: the portfolio question (what mix of safe and risky bets) is the core of problem selection.

### 2.2 Contest and funding models
- Gross and Bergstrom 2019 [a21, opened]: model of funding as a contest. When awards are scarce, effort spent on proposals can equal the value of the funded work. Faculty spend about 19% of research time on proposals. Lesson: deliberation about what to do is itself a cost. Cap it (analogy only).
- Packalen and Bhattacharya 2020 [b17, b18, opened]: NIH funds over 60% of papers built on 10-25-year-old ideas, against about 50% for the newest ideas or only well-established ones. Funding favours matured ideas over edge science.

### 2.3 Tradition and innovation as a measured strategy (Foster, Rzhetsky, Evans 2015)
- Data: MEDLINE chemistry network to 2008. 181,078 nodes (chemicals), 84,709,977 links [b08].
- Each statement is a repeat of a known link (85.8%), a new link between known chemicals (new bridge or consolidation, 12.4%), or a jump to a new chemical (1.8%). So 14.2% are new or jump [b08, b11].
- The strategy mix does not follow where opportunity lies. Scientists crowd known links.
- Citation return: mean citations 8.38 (repeat), 11.00 (new), 12.90 (jump). Rarer strategies pay more on average and with higher variance. Surprisal explains 29.2% of variation in mean citations across 100 strategy-year points (R2 = 0.2916) [b09, b10].
- Break-even: from equal expected citations, p(new) must be at least 0.76 p(repeat) and p(jump) at least 0.65 p(repeat). The paper calls this unlikely to hold, so risky strategies are a poor bet for a career [b10, d12]. (Critique fix: these are derived ratios, not "needed odds of 24%/35%".)
- Model fit to the data: Pearson R = 0.983 [b08].
- Only the arXiv version was opened. The ASR 2015 version is unread [a18].

### 2.4 Choosing experiments to speed up collective discovery (Rzhetsky et al. 2015)
- PNAS 2015, full text opened via PMC [b12, d11]. A model of discovery on a network of claims. Scientists pick safe (near known) or risky (far) experiments.
- Human choices are near-optimal only while up to about 10% of the network is explored. Beyond about 30% explored, human strategy is increasingly inefficient. The best mix shifts toward risk as coverage rises [K11, K27].
- Consequence: a fixed safe-heavy portfolio is right early and wrong late.

### 2.5 Bias against novelty (Wang, Veugelers, Stephan 2017)
- Web of Science, 2001 cohort, 15-year window [b13-b16]. Novelty = a new combination of cited journals.
- 89% of papers make no new journal combination. 11% make some. 54% of those make exactly one.
- Highly novel papers: citation dispersion +18%; top 1% odds +57% (moderately novel +13%); top 10% vs middle 80% odds +18%; lowest 10% odds +15%.
- With windows under 3 years, novel papers underperform. They appear in journals with 10-17% lower impact factor. Later they win.
- One definition of novelty, one cohort year.

### 2.6 The pivot penalty (Hill et al. 2025, Nature)
- 25.8 million papers 1970-2015, 154 fields. Pivot = distance of a paper's references from the author's own earlier references. Hit = top 5% of citations [b19].
- Lowest-pivot papers: 7.4% hit rate (48% above baseline). Highest-pivot: 2.2% (56% below).
- Within the same author: lowest pivot 2.1% more likely to hit, highest 1.8% less likely.
- Holds in 93% of fields, in patents (patent citations fall 43% from lowest to highest pivot vigintile), for large and small teams, new and old co-authors, and COVID-19 pivots (premium largely offset) [b20-b22, d10].
- Reputation and audience explain only about 26% (holding journal fixed makes the slope about 26% less steep). The rest looks like lost local knowledge. The penalty grows about 1.6% per year of career age but is present very early [d10].

### 2.7 Predicting the next question with networks
- Krenn and Zeilinger 2020 [a15]: semantic network of physics concepts. Link prediction AUC 0.85 over a 5-year horizon.
- Krenn et al. 2022 [b29]: AI-literature benchmark, link prediction AUC 93-99%.
- Sourati and Evans 2023 [a17, b26-b28]: adding author information raises precision by up to 400%.
- Swanson 1986 (fish oil, Raynaud) and Tshitoyan 2019 (word embeddings predict materials) are the classic hidden-link cases [c17, c18, not opened].
- Boundary: Gu and Krenn [a16] found predicted impact is not interest (section 3).

### 2.8 LLMs enter (2023-2026)
- 2023-24: idea generators (SciMON [a12, b34], ResearchAgent [a13], AI Scientist [a14], MOOSE-Chem [c11], Co-Scientist [b31]), judged mostly by LLMs.
- 2024: Si et al., the first large blind human study [a01].
- 2025: Gupta and Pruthi on plagiarism [a10]; Si et al. ideation-execution gap [a05]; Wen et al. outcome prediction [a07].
- 2026: trained "scientific taste" (Tong [c14], Gong [c15]); prompt-only selection with pilots (Meta FAIR [d01, d02]); novelty benchmarks (RINoBench [d04], OpenNovelty [d05]); Ideation Arena [d08]; execution-grounded RL [d18]. These use newer models than the 2024 studies, so numbers are not directly comparable.

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLM questions rated more novel than human by blind experts | Per review: Human 4.84 (N=119), AI 5.64 (N=109), AI+rerank 5.81 (N=109). Per idea N=49 each: 4.86 / 5.62 / 5.78 (p 0.03, 0.00). Feasibility not significantly lower. 79 reviewers, 298 reviews | Si 2024 [a01, b01, c01] | S |
| Excitement per idea (not novelty) | 4.56 / 5.18 / 5.45; AI-alone vs human p=0.08 | Si 2024 [c01] | S |
| Experts disagree on question quality | 56.1% pairwise agreement (NeurIPS 2021: 66.0%, ICLR 2024: 71.9%); Ideation Arena 56.8% on 1,675 queries; rubric rho 0.745 | Si 2024; Chen 2026; Gottweis 2025 [a02, d08, d15, d09] | E (K29: 3 sources) |
| Prompted LLMs near chance at ranking ideas or papers | 45-53% (Si pool ranking); GPT-4.1 51.9% (Wen, 1,585 pairs); 31.1% frontier mean on 4 tiers (chance 25%); extra reasoning no gain | Si, Wen, Gong [a03, a07, c05, c15] | E |
| Same LLM ranker on ICLR review pairs | Claude-3.5-Sonnet 71.4% (different task; do not mix) | Si 2024 [a03] | S |
| Trained judges beat prompted and sometimes experts | Wen fine-tuned 77% (63.6% on unpublished ideas incl. AI-agent ideas); Gong management: Qwen3-4B 59.2% vs 48 expert gatekeepers 41.6% vs frontier 31.1%; fine-tuned range 55.0% (public admin) to 85.5% (psychology); Tong in-domain 64.7 to 80.9 (4B), 71.7 to 83.1 (30B), 720,341 pairs from 2.1M arXiv papers | Wen, Gong, Tong [a07, c15, c14, d03] | E (weights, not scaffold) |
| Execution reverses the LLM advantage | Ideation (Human/AI) novelty 4.91/5.78, excitement 4.40/5.65, effectiveness 4.83/6.00, overall 4.60/5.38. After execution 4.90/4.73, 4.48/3.90, 4.78/4.13, 3.97/3.41 (no sig diff). Drops: Human -0.010/+0.078/-0.052/-0.628; AI -1.049/-1.760/-1.879/-1.976 (p 0.025/0.001/0.003/0.004). N=19 human, 24 AI projects, 58 reviewers, 100+ h each | Si 2025 [a05, b05, b06, c04] | S |
| Direct post-execution comparison per idea not significant | N=43, FDR p 0.18-0.59; paper says it lacks power for its preregistered hypothesis | Si 2025 [c22] | S |
| Pre-run ratings barely predict outcome | Pearson r -0.32 to 0.21, N=43 | Si 2025 [a06, b07] | S |
| Retrieval is the novelty bottleneck | Known ideas scored 6.14/10 without search, 2.38/10 with. Source finding from parametric memory 1.3-32.7% vs 88.8-89.0% with oracle access. Turnitin and OpenScholar found 0 of 36 | Gupta 2025; Beel 2025; Mostafa 2026 [a10, a11, c07, c08, d06] | E |
| Many LLM ideas are rewrites | 24.0% verified plagiarism (36.0% with unverified) in 50 proposals, 13 experts | Gupta and Pruthi [a10, a23] | S |
| Related works do not fix scalar novelty scoring | RINoBench, 1,381 ideas, 5 classes: best macro-F1 17.2 (GPT-5). Retrieval adds about +0.03 on a trained judge (metric label 0.73 vs 0.76 unconfirmed) | Schopf 2026; Mostafa 2026 [d04, d06] | S |
| Generation saturates | 4000 seeds per topic; at cosine 0.8 about 5% (about 200) are non-duplicates | Si 2024 [a03, b02] | S |
| RL on execution reward narrows ideas | 51 of 128 ideas in 2 common types at epoch 0; 119 of 128 at epoch 68. Reward 0.253 to 0.343 (GRPO) | arXiv 2601.14525 [d18] | S |
| Agent novelty filters unreliable | AI Scientist uses model-run keyword search; independent test: known ideas called novel; 5 of 12 experiments (42%) failed | Beel 2025; Lu 2024 [c06, c07, c23, a25] | E |
| Humans mostly repeat | 85.8% repeat, 12.4% new links, 1.8% jumps; R=0.983 | Foster 2015; Rzhetsky 2015 [b08, b11, b12] | E |
| Rare strategies pay more but not enough | Citations 8.38 repeat, 11.00 new, 12.90 jump; surprisal explains 29.2% of mean-citation variation (100 points) | Foster 2015 [b09, b10] | S |
| Human portfolio optimal only early | Near-optimal to about 10% explored, inefficient beyond about 30% | Rzhetsky 2015 [b12, d11] | S (model) |
| Novel papers: more variance, delayed payoff | Dispersion +18%; top 1% odds +57%; top 10% +18%; bottom 10% +15%; under-3-year windows underperform; journal IF 10-17% lower | Wang 2017 [b13-b16] | S |
| Pivot penalty | Hit rate 7.4% vs 2.2%; 93% of fields; within-author +2.1%/-1.8%; 26% explained by journal; patents -43% | Hill 2025 [b19-b22, d10] | S |
| Funders favour matured ideas | Over 60% for 10-25-year-old ideas vs about 50% | Packalen 2020 [b17, b18] | S |
| Concept-link prediction works | AUC 0.85 (5 years); 93-99% (AI benchmark); +400% precision with author data | Krenn, Sourati [a15, a17, b29] | E |
| Predicted impact is not interest | Mean interest 2.350 (high-citation predicted) vs 2.446 random vs 2.414 titles-only. Overall mean 2.40; 24.9% rated 4-5 (1,107 of 4,451); 36.7% rated 1. Interest is predictable: AUC 67.4% zero-shot GPT-4o, 63.2% graph NN | Gu and Krenn [a16, a24, b23-b25, c10] | S |
| Human rerank differs from LLM rerank | Only 17 of 49 picks overlap | Si 2024 [a04] | S |
| Cheap pilots help selection | Reasoning-only 60.7-65.0%; frontier singles 64.66-67.44%; majority 68.04%; arbiter ensemble 69.35%; with pilots 78.52% (5 min), 82.78% (30 min), 84.02% (4 h); score-oracle baseline 66.73% | Meta FAIR 2026 [d02] | S |
| Prompt-only selector on a real agent | AIRS-Bench 0.684 baseline to 0.711 (inference-only), 0.729 (with 5-min pilots); oracle 0.748; recovers about 42% and 70% of the oracle gain | [d01, d17] | S |
| Boldness beats plan-reading judges | Best judge 70.8%; nine-judge majority 67.1%; best-of-ten 36% vs 10% chance. Conference abstract only; unverified | BoLeBench [c16] | S, unverified |
| LLMs beat experts at forecasting results | 81.4% vs 63.4% (neuroscience results) | Luo 2024 [b30] | S |
| Outside NLP: product ideas | Purchase intent human 40.4%, GPT-4 zero-shot 46.4%, few-shot 49.3%; top 40 of 400: 5 human, 15, 20. Novelty human 40.6% vs LLM 36.7/36.1% (p=.008). Novelty vs purchase intent r=-0.078 | Terwiesch 2026 [d07] | S |
| Tournaments are self-judged | Co-Scientist top-Elo 78.4% on GPQA diamond; Ideation Arena: frameworks from +177 Elo to nothing | [d08, d09] | C |

## 4. Mechanisms and models

Each is written so it can be coded.

### 4.1 Strategy mix with break-even (Foster)
- Inputs: for each candidate question, class it as repeat, new link, or jump relative to a store of known links between concepts.
- Payoff per class: mean outcome M_repeat, M_new, M_jump, estimated from the agent's own past runs (the paper used 8.38, 11.00, 12.90 citations).
- Break-even: a risky class is worth trying when p_success(class) / p_success(repeat) is at least M_repeat / M_class. Ratios: new 8.38/11.00 = 0.76; jump 8.38/12.90 = 0.65.
- Code computes the class by lookup in the concept store. The model is not asked "is this bold".
- Caveat: citations are a proxy. The agent needs its own payoff (probe score).

### 4.2 Explore share by coverage (Rzhetsky)
- State: coverage c = fraction of the relevant claim network already explored.
- Rule of thumb: safe-heavy while c is under about 0.10, shifting to risky as c passes about 0.30. No budgeted optimum exists [K27]. Treat as a qualitative schedule to fit.
- For an agent: c = distinct concepts or claims touched in memory divided by an estimate of the space. Crude but codable.

### 4.3 Novelty by combination (Wang)
- Novelty = a new pair of sources never combined before. Code: take the set of source pairs used, check each against a store. Novel if at least one unseen pair.
- Expect higher variance and lower short-run value. Score on a short and a long horizon.

### 4.4 Pivot distance (Hill)
- Pivot = 1 minus overlap between the question's reference set and the agent's own history (for example cosine over concept vectors).
- Prediction: payoff falls as pivot rises, mostly through lost local knowledge. Mitigation to test: a context-loading step before a switch.

### 4.5 Link prediction on a concept graph (Krenn, Sourati)
- Graph: nodes = concepts, edges = co-occurrence in a source or in an earlier solved task. Score unlinked pairs. Candidates are high-score pairs (likely to be studied) or low-score plausible pairs (new). Adding who-works-on-what raised precision up to 400%.
- Warning: high score means "will be studied", not "interesting" [a16].

### 4.6 Judge trained on outcomes (Wen, Tong, Gong)
- Data: pairs with a known outcome difference (citation, tier, benchmark gain), matched by field and time. Train a pairwise preference model (Tong: GRPO on 720,341 pairs; Wen: 6,000 training pairs). Test with position swap.
- Scaffold analogue (untested at equal tokens): store past pairs with outcomes in memory, retrieve the nearest, show them to the judge as precedents. Meta FAIR [d01] did a form of this with executed history: 0.684 to 0.711.

### 4.7 Pilot-run selection (Meta FAIR)
- Candidates, then a short real pilot for each (reduced CV, fewer epochs; full data beat subsampling), then compare pilot scores, then pick. Up to 30 pilots per decision; 15 suggestions per selection. Accuracy 65% -> 78.5% (5 min) -> 82.8% (30 min) -> 84.0% (4 h). Most gain comes in the first minutes.
- Same idea as G8 (novelty judged by running) and the S0 probe.

### 4.8 Retrieval-based novelty check
- Extract claims. Retrieve top-k related works (OpenNovelty design: top-50, then top-10 per claim, full text; no ablations). List the closest prior works and the overlap, not a scalar. A different model checks the overlap list.
- Why a list: scalar novelty scores are poor even with related works given (F1 17.2), while written justifications match human reasoning [d04].

### 4.9 Diversity seeding
- Generation saturates (5% unique at cosine 0.8). Change the inputs, not the sample count: personas, vendors, topic seeds, retrieved contexts. Terwiesch [d07] shows pooling sources partly restores diversity. Code dedupes by embedding similarity.

## 5. What holds up

### 5.1 Replicated or multi-source
- Prompted LLMs are poor judges of research quality: Si, Wen, Gong all agree (K05).
- Training on outcomes beats prompting: Wen, Gong, Tong (K06), in AI, management and arXiv. All are fine-tuning.
- Novelty needs retrieval: Gupta, Beel, Mostafa, Schopf (K07).
- Self-judged novelty inside agent pipelines is unreliable: Lu, Beel (K10).
- Human research is conservative: Foster and Rzhetsky agree on direction (K11).
- Concept-network link prediction works: Krenn 2020, Krenn 2022, Sourati (K17).

### 5.2 Single study (needs replication)
- LLM ideas more novel than human (Si 2024): one field, 7 topics, one LLM family.
- Execution reverses it (Si 2025): N=43 projects; direct comparison not significant; the paper says it lacks power for its main hypothesis.
- Pivot penalty (Hill): one large observational study; cause not shown.
- Pilot-run gain (Meta FAIR): one lab, ML tasks with numeric proxies.

### 5.3 Contradictions and how they resolve
- Prompted vs trained judges: not a conflict, different supervision. But trained ones are weights; what transfers to a scaffold is unknown.
- Citation prediction vs interest (Gu and Krenn): predicting what will be studied or cited is not predicting what experts find interesting. (The 1.94 in that paper is a test statistic, not a mean rating.)
- Pivot penalty (Hill) vs rare-strategy payoff (Foster) vs long-run novelty (Wang): all show a short-run penalty for novelty, with three different novelty measures (own-work distance, chemical link type, journal combinations).
- Si 2024 (more novel) vs Gupta (24% rewrites) vs Si 2025 (advantage gone after execution): blind novelty ratings do not survive retrieval or execution checks.

### 5.4 Moderators
- Horizon: novel work loses under 3 years and wins later (Wang).
- Coverage: the best safe/risky mix depends on how much is explored (Rzhetsky).
- Reading depth: full papers beat abstracts for outcome prediction (53.0% vs 38.8%, Wen) [c05].
- Judge supervision: prompted vs trained.
- Pilot cost: longer pilots help with diminishing returns; subsampled pilots are less reliable.
- Raters: with 56% pairwise agreement, 3 to 5 raters per item are needed for a trustworthy label [K29].

### 5.5 Interventions that worked
- Training a judge on outcome pairs (K06).
- Cheap pilot runs before choosing (K23, K24).
- Retrieval before a novelty verdict (K07).
- Human rerank of the AI pool raised novelty 5.64 to 5.81 (K19, small).
- Pooling idea sources to restore diversity (d07).

### 5.6 Interventions that did not work
- Extra reasoning for judging (Gong; GPT-5.5 high no better than chat) [c15].
- Giving related works to a prompted judge for scalar scoring (F1 17.2) [d04].
- Citation-predicted pairs as a proxy for interest [a16].
- Sampling more ideas (saturation) [a03].
- RL on effectiveness alone (diversity collapse) [d18].
- Turnitin and OpenScholar for plagiarism: 0 of 36 [a11].
- RL with chain-of-thought plateaued below direct fine-tuning [c15].

## 6. Language models

### 6.1 Generating
- Blind experts rate LLM ideas higher on novelty (+0.80 per review, +0.76 per idea) and about equal on feasibility [a01]. Human rerank adds +0.17.
- Output saturates: about 200 unique per topic from 4000 [a03].
- After RL on execution reward, variety collapses (119 of 128 in two types) [d18].
- Outside NLP (products), LLM ideas beat humans on purchase intent (+6.0 and +8.9 points) and filled 15 and 20 of the top 40 vs 5, but were less novel (36.1-36.7% vs 40.6%) [d07].

### 6.2 Judging
- Prompted: 45-53% on idea pairs [a03]; 51.9% GPT-4.1 on outcome pairs [a07]; 31.1% (chance 25) on tiers [c15].
- Trained: 77% (Wen); 59.2% for a 4B model vs 41.6% for expert gatekeepers [c15]; 80.9 (4B) and 83.1 (30B) in-domain [c14]. Altmetric transfer 82.6% (4B), 86.3% (30B). Tong's text is ambiguous on in-domain vs temporal; flagged.
- Forecasting results: LLMs 81.4% vs experts 63.4% [b30]. Outcome forecasting may be a better target than "is this idea good".
- Best prompted judge against expert pairs: 72.56% soft accuracy [K29].
- History-reading selector with no training: 60.7 to 65.0% as history grows; with agentic pilots 78.5% [d02].

### 6.3 Checking novelty
- Without search known ideas scored 6.14/10; with search 2.38/10 [c07].
- Parametric recall of sources 1.3-32.7%; with oracle access 88.8-89.0% [a11].
- 24.0% of 50 proposals are verified rewrites [a10].
- Scalar scores fail even with related works (F1 17.2) [d04].

### 6.4 Whole agents
- AI Scientist: model-run keyword novelty check; 42% of experiments failing in an independent test [c06, c07].
- Co-Scientist and Ideation Arena: Elo tournaments are LLM-judged; framework effect ranges from +177 Elo to none [d08, d09]. Contested.
- Execution-grounded runs: the executor matters (over 90% execution rate with Claude self-executing vs 42-78% with a GPT-5 executor) [d18].

### 6.5 What changed it, by how much
- Training on outcomes: 51.9% to 77% (+25 points).
- Pilots: 65% to 78.5% at 5 minutes (+13.5 points).
- Retrieval: known-idea novelty score 6.14 to 2.38 [c07].
- Extra reasoning: no gain.
- Caveat: 2026 studies use newer models than 2024 studies. Differences may partly reflect model change.

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. **The model that wrote a question never makes the final pick among its own questions.** G8/G5 (already in the schema). [E] K05, K10; a04, a03, c15. Only 17 of 49 picks overlapped between LLM and human rerank.
2. **Novelty is checked by retrieval, in a different call from the one that wrote the question.** S0 novelty check, memory. [E] K07 (a10, a11, c07, c08, d06). The list-of-closest-prior-works form is [S] (d04) and sits in Test first.
3. **A model's self-score of a question is not a filter and not proof of value.** S0, G8. [E] K05, K10 (c06, c07, c23, a25).
4. **Keep question-outcome pairs in memory with a result label.** Memory. [E] that trained judges beat prompted ones (K06: a07, c14, c15, d03). Use as a store now; the retrieval-as-substitute effect is untested.
5. **Bench labels are numeric outcomes, or rubric scores averaged over 3 to 5 raters.** Evaluation design. [E] K29 (d08, d13, d15). Single-rater labels are noise.

### Test first

6. **Cheap probe before commit.** S0 probe. [S] K23, K24 (d01, d02, d17). ML tasks only.
7. **Precedent-retrieval judge** (prompt-only analogue of Wen/Tong/Gong). Memory/S0. [S] K23; [E] K06 for weights.
8. **Overlap list vs scalar novelty; retrieval depth; abstract vs full text.** S0. [S] K25 (d04, d05, d06, c05).
9. **Diverse seeds instead of more samples.** O1/G4. [S] K09, K26 (a03, d07, d18).
10. **Risk-class tag and fixed risky share.** S0 portfolio rule. [S] K12, K27 (b09, b10, d11, d12).
11. **Stay with accumulated context vs switch; context-loading step on a switch.** Memory/S0 switch rule. [S] K14, K28 (b19, d10).
12. **Boldness rule vs plan-reading judge.** S0. [S, unverified] K21 (c16).
13. **Outcome forecasting before running (calibration).** S0. [S] K22 (b30).
14. **Concept-graph link prediction to propose questions.** O1/memory. [E] for prediction (K17); [S] that it helps choice; K18 warns impact is not interest.
15. **Tournament selection vs single pass at equal tokens, outcome-judged.** O1/O6. [C] K20.
16. **Short and long horizon scoring of a question.** S0. [S] K13.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, setup and probe tokens included (G7). Report mean, spread and item count.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 60-100 pairs of past tasks with known outcomes, withheld from memory | (a) plain pairwise pick; (b) pick with retrieved precedent pairs from a separate pool; (c) best-of-N of the plain pick | Pairwise accuracy vs actual outcome | (a) near 50-55%; (b) +5 to +10 points if a scaffold can mimic trained judges (Meta FAIR got +4 to +5 points of score gain) |
| T2 | 40-60 open items with a numeric outcome and a cheap probe | (a) reasoning-only choice among 4-8 candidates; (b) short probe on each, then choose; (c) one long run on a single guess | Final score; pairwise accuracy | (b) beats (a) by 8 to 15 points of accuracy (d02: 65 to 78.5) |
| T3 | 50 known-published questions plus 50 invented controls | (a) scalar novelty, no search; (b) scalar with search; (c) overlap list with search at depth 3, 10, 30, abstract vs full text | Known items flagged non-novel; false-flag rate on controls | (a) calls known items novel; (c) at least as good as (b), cost curve plotted |
| T4 | 100 agent-proposed questions | Self novelty filter vs separate-model plus retrieval filter | Agreement with a 3-rater check; share of rewrites passed | Rewrites passed falls from about 24% to under 10% |
| T5 | 30 long open tasks | Safe-only vs 20% vs 40% risky share (class by code) | Best outcome found; top-tail rate; mean | Higher variance with risk; best share falls as coverage rises; mean may fall |
| T6 | 30 sequences with history on A and a new task B | Stay on A; switch cold; switch with context loading | Outcome per token on B | Cold switch loses; loading recovers part |
| T7 | 100 questions with known long-run outcome | Short probe vs long probe vs both | Rank correlation with final value | Short horizon underrates novel questions |
| T8 | 200 questions | Frequency (citation-like) prediction vs interest-aware rerank | Interest by 3 raters | Frequency proxy no better than random (2.350 vs 2.446) |
| T9 | Pool of 20 candidates per item | Generator picks; code picks by probe; LLM Elo tournament; cross-model tournament | Outcome by probe or held-out check, not LLM | Tournament gain mostly extra samples; probe pick best |
| T10 | Bold vs cautious paired attempts | Boldness rule vs plan-reading judge | Executed outcome | Bold rule wins (verify BoLeBench first) |
| T11 | 50 prompts | 1 x 4000 samples vs 4 seed sources x 1000 | Unique count at cosine 0.8 | Seed variation gives at least 2x unique questions |

## 9. What does not transfer, and why

- Citation counts as value. They measure attention and network, not truth [c14 limits]. The agent needs probe outcomes.
- Career and reputation effects (funding contest, pivot reputation, journal prestige). An agent has no career. Only about 26% of the pivot penalty is reputation [d10]; the rest may transfer as lost context.
- Funding contests (Gross and Bergstrom). Only the analogy of a deliberation cap.
- Peer-review tiers (Gong). A prestige signal with survivorship bias.
- Fine-tuned weights (Wen, Tong, Gong). We do no training. Transfer only through memory and retrieval, which is unproven.
- NLP-only ideas. No debugging, engineering or business evidence.
- 100-hour human execution. Our agent has tokens and minutes.
- LLM-judged "AI scientist" results (Co-Scientist, ResearchAgent, SciMON). The judge is not independent.
- Expert-rater labels. Expensive; use numeric outcomes.
- Human conservatism as a norm. The 85.8% repeat rate partly reflects incentives; for an agent the right mix is set by budget.

## 10. Open questions

1. Does a prompt-only scaffold (precedent retrieval plus probe) match fine-tuned judges at equal tokens? No study tests it.
2. How much of the ideation-execution gap does a cheap pilot recover on open research questions? Only ML tuning tested [K24].
3. What is the cost curve of novelty checking (depth, full text, separate judge)? [K25]
4. Do results hold outside NLP and for non-paper questions? [K26]
5. What is the best risky share under a token budget? No model with numbers [K27].
6. Does tournament selection beat single-pass under an independent outcome measure? [K20]
7. What does BoLeBench measure, and does it replicate? Figures unverified [K21].
8. Has Wen et al. replicated on newer cutoffs or other fields? None found; weak evidence of absence.
9. Is the pivot penalty really lost local knowledge? Only partly shown [K28].
10. Do the 2024-era LLM results hold with 2026 models?

## 11. Sources

[V] = opened; [M] = abstract or snippet only.

- [V] Si, Yang, Hashimoto (2024) Can LLMs Generate Novel Research Ideas? https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto, Yang (2025) The Ideation-Execution Gap. https://arxiv.org/abs/2506.20803
- [V] Wen et al. (2025) Predicting Empirical AI Research Outcomes with Language Models. https://arxiv.org/abs/2506.00794
- [V] Gupta and Pruthi (2025) All That Glitters is Not Novel. https://arxiv.org/abs/2502.16487
- [V] Wang et al. (2023) SciMON. https://arxiv.org/abs/2305.14259
- [V] Baek et al. (2024) ResearchAgent. https://arxiv.org/abs/2404.07738 (human-eval table not extracted)
- [V] Lu et al. (2024) The AI Scientist. https://arxiv.org/abs/2408.06292
- [V] Krenn and Zeilinger (2020) Predicting research trends. https://arxiv.org/abs/1906.06843
- [V] Gu and Krenn (v4, 2026) Generating Interesting Scientific Ideas using Knowledge Graphs and LLMs. https://arxiv.org/abs/2405.17044
- [V] Sourati and Evans (2023) Accelerating science with human-aware AI. https://arxiv.org/abs/2306.01495
- [M] Foster, Rzhetsky, Evans (2015) Tradition and Innovation, ASR. https://doi.org/10.1177/0003122415601618
- [V] Foster, Rzhetsky, Evans arXiv version. https://arxiv.org/abs/1302.6906
- [M] Rzhetsky et al. (2015) PNAS DOI. https://doi.org/10.1073/pnas.1509757112
- [V] Rzhetsky et al. (2015) PMC full text. https://pmc.ncbi.nlm.nih.gov/articles/PMC4664375/
- [M] Fortunato et al. (2018) Science of science. https://doi.org/10.1126/science.aao0185
- [V] Gross and Bergstrom (2019) Contest models. https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000065
- [M] Kuhn (1959); Kitcher (1990), from memory, no URL.
- [V] Wang, Veugelers, Stephan (2017) Bias against novelty. https://lirias.kuleuven.be/retrieve/465817
- [V] Packalen and Bhattacharya (2020) NIH funding and edge science. https://pmc.ncbi.nlm.nih.gov/articles/PMC7275727/
- [V] Hill et al. (2025) The pivot penalty. https://pmc.ncbi.nlm.nih.gov/articles/PMC12222024/
- [V] Krenn et al. (2022) Predicting the Future of AI with AI. https://arxiv.org/abs/2210.00881
- [V] Luo et al. (2024) LLMs surpass human experts in predicting neuroscience results. https://arxiv.org/abs/2403.03230
- [V] Gottweis et al. (2025) Co-Scientist. https://arxiv.org/abs/2502.18864
- [V] Beel et al. (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297
- [V] Yang et al. (2025) MOOSE-Chem. https://arxiv.org/abs/2410.07076
- [V] Qiu et al. (2025) AI Idea Bench 2025 (benchmark description only). https://arxiv.org/abs/2504.14191
- [V] Tong et al. (2026) AI Can Learn Scientific Taste. https://arxiv.org/abs/2603.14473
- [V] Gong, Li, Zhou (2026) LLMs learn scientific taste. https://arxiv.org/abs/2603.16659
- [M] BoLeBench (2026), conference listing abstract only. https://openreview.net/forum?id=A6wSfv3yoE
- [M] Swanson (1986). https://doi.org/10.1353/pbm.1986.0087
- [M] Tshitoyan et al. (2019). https://doi.org/10.1038/s41586-019-1335-8
- [M] Krenn and Zeilinger PNAS (2020). https://doi.org/10.1073/pnas.1914370116
- [V] Meta FAIR (2026) AI Research Preference Models. https://arxiv.org/abs/2608.13940
- [V] Schopf and Farber (2026) RINoBench. https://arxiv.org/abs/2603.10303
- [V] Zhang et al. (2026) OpenNovelty. https://arxiv.org/abs/2601.01576
- [V] Mostafa, Nguyen, Ahmadi (2026) Are We Truly Innovating? https://arxiv.org/abs/2602.06054
- [V] Terwiesch et al. (2026) AI and its impact on creativity (product ideas). https://arxiv.org/abs/2607.27553
- [V] Chen et al. (2026) Ideation Arena. https://arxiv.org/abs/2608.29696
- [M] Liu et al. (2025) Idea-level retrieval for novelty detection. https://arxiv.org/abs/2505.24615
- [V] Towards Execution-Grounded Automated AI Research (2026), first 100,000 of 203,000 characters. https://arxiv.org/abs/2601.14525

Links to other subfields in this run (not covered here): Theory comparison; Research programmes; Experimental practice; Sociology of science and Merton's norms; Novelty search and open-endedness; Atypicality versus disruption; Monte Carlo tree search; Count-based exploration; Good Judgment Project; Executive function, exploration vs exploitation.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 6 established claims: 3 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E15.01-K06** (reworded: the sources support less). Numbers check (Wen 77% on 1,585 test pairs; Gong 59.2% vs expert majority 41.6%; Tong 80.9/83.1), but in Tong's in-domain table the prompted GPT-5.4 Thinking scores 81.6, above the 4B SciJudge (80.9) and only 1.5 points below the 30B (83.1), so trained models do not clearly beat the best prompted LLMs there. Corrected claim: Models fine-tuned on outcome data beat prompted LLMs and sometimes experts at pairwise judging of research: Wen 77% on 1,585 test pairs (vs GPT-4.1 51.9%, o3 about random), Gong 59.2% vs expert majority 41.6% and frontier mean 31.1% (management), but Tong's in-domain citation-pair gains (64.7 to 80.9 and 71.7 to 83.1) only match the strongest prompted model (GPT-5.4 Thinking 81.6). These are weights, not a scaffold.
- **E15.01-K07** (number corrected). Co-Scientist 6.14 vs 2.38 and Gupta's 1.3/32.7% vs 88.8/89.0% are verified, but Turnitin and OpenScholar were run only on documents with verified similarity score 4 or higher (not on 36), and the text says OpenScholar surfaced the source in one case (Table 3 lists 0%) while Turnitin found none. Corrected claim: Retrieval of related work is the novelty bottleneck: Co-Scientist's auto-evaluation scored known (non-novel) ideas 6.14/10 without search vs 2.38/10 with search; in Gupta and Pruthi plagiarism detection accuracy was 1.3% (Claude 3.5 Sonnet) and 32.7% (GPT-4o) from parametric knowledge vs 88.8-89.0% with oracle access to the source paper; on documents with verified similarity scores of 4 or more, Turnitin found the source in none and OpenScholar in at most one case.
- **E15.01-K11** (now single-source: the sources are not independent). Numbers verified (85.8% repeat, 1.8% jumps, MEDLINE strategy near-optimal only for ~10% and increasingly inefficient beyond ~30%, though the paper says 'may have been'), but both sources are by the same group (Foster, Rzhetsky, Evans) using the same MEDLINE data and model.
