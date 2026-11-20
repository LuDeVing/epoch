# Instruments, institutions, social history: deep document

*Subfield D07.07. Focus: who and what made science possible. Key work: Shapin and Schaffer, Leviathan and the Air-Pump. Role for our agent: background, with a few usable machine-side findings. Evidence ids (a01..d17) point to evidence_a-d.jsonl; claim ids (K01..K30) point to claims.jsonl. Honest caveat up front: the history half rests on Wikipedia, one Boyle primary text and two Stanford Encyclopedia pages. The books by Shapin and Schaffer, Shapin, Collins and Schaffer were never opened. The numbers half (peer review, AI scientists, LLM judges) was read from full arXiv text.*

## 1. What it is

This subfield asks a plain question: what made a claim count as a scientific fact? History and sociology of science answer that facts need more than an instrument reading. They need:

- **Instruments.** The air pump, telescope and microscope. They produce results no one could get with the naked senses.
- **Institutions.** The Royal Society (1660, charter 1662), Philosophical Transactions (1665), blind peer review, journals, conferences. They decide what is recorded, who is believed and what is passed on.
- **Social rules.** Who is a credible witness, how disputes end, what counts as a successful replication.

For an LLM agent this maps onto three things we already build. The code runner is the instrument. The check, the ledger and the judge are the institution. The rule "a claim stands when an independent check passes" is the social rule. The field gives us (a) a vocabulary for why replication and independent witnesses matter, (b) hard numbers on how noisy human gatekeeping is, and (c) a growing set of studies in which LLM agents play scientists, reviewers and authors. The third set is the most useful part for the schema. It says where LLM judges can be trusted and where they cannot.

Scope notes. Neighbouring subfields covered in parallel runs (links only): Strong Programme and SSK; Kuhn and paradigm crisis; Social epistemology of discovery; Automated discovery; Values and inductive risk; Team science; Judicial bias and noise; Debiasing; Retrieval and ensembles for LLM forecasts. This file does not repeat them.

## 2. History and theories in depth

### 2.1 Boyle, the pump and the Royal Society (1657-1665)

- Von Guericke's pump (1657) needed two strong men working for hours. Boyle read of it in 1657. With Robert Hooke he built an improved "Pneumatical Engine" by 1659 (receiver 28.4 litres, a 36 cm brass pumping cylinder). [a03]
- Hooke was a paid instrument maker and curator (Curator of Experiments from Nov 1663). Hidden technicians did much of the hands-on work. [a03, a04]
- Boyle's book, New Experiments Physico-Mechanicall (1660), reported the trials. Boyle's law (1662) came while answering the Jesuit Francis Line. [a03]
- The Society began 28 Nov 1660 with 12 natural philosophers at Gresham College. Motto: Nullius in verba. First charter 15 July 1662, second charter April 1663, 98 original Fellows. Philosophical Transactions began in 1665 under Oldenburg, the first journal devoted only to science. [a04]
- Hooke's Micrographia (Jan 1665) was the Society's first major publication and a best-seller. It coined "cell". Its fold-out louse engraving worked as a portable witness for readers who had no microscope. Specimens needed heavy preparation. [a05]
- Galileo's Sidereus Nuncius (13 Mar 1610) is the earlier case of the same problem. His 20x telescope showed 4 Jupiter moons, 35 Pleiades stars against 6 by eye, and 80 in Orion against 9. Good telescopes were scarce. Kepler endorsed it in April 1610 but had no independent confirmation until August. Belief spread as others got the same sight with their own copies. [a06]

### 2.2 Shapin and Schaffer (1985): three technologies

- The book (440 pages, 8 chapters; 2nd ed 2011) argues that Boyle won the dispute with Hobbes through three bundled technologies. [a01, c23]
  1. **Material**: the pump.
  2. **Literary**: reports with circumstantial detail that let absent readers "witness virtually".
  3. **Social**: rules for how experimenters treat each other, and a community whose assent makes a fact.
- The authors also argue that the pump leaked, and that leakage meant the pump alone could not settle anything. Failures could always be blamed on leaks.
- Huygens built his own pump and saw water stay suspended in an evacuated tube. Boyle's group could not reproduce it for over 18 months, until Huygens came to London. [a02, c23, c24]
- Critics: Principe (Boyle is read anachronistically), Horstmann (errors in the Hobbes chapters), Malcolm and Leijenhorst (Hobbes's anti-void view had no political motive), Latour (nature also shapes politics). [a01]
- Checked against Boyle himself (d14, d15): his 1660 text admits the pump leaks ("our Receiver leak'd too fast"). It says it is useful to recite experiments that miscarry as well as those that succeed. It cites repeats before named witnesses (Wallis, Ward, Wren). Mercury stood about 29.5 inches and fell 18.5 and 19.5 inches in two small-vessel trials. Stanford's Boyle entry quotes him that many experiments "do not succeed, while others do succeed once but are then unable to be replicated". So Boyle knew replication was not automatic. That weakens any reading in which failure was hidden. It does not refute the claim that the pump could not settle disputes alone.
- Not opened: the book itself, Shapin 1994 (A Social History of Truth: gentlemen's testimony counted most), Schaffer 1989 (Newton's prism results did not travel to others' prisms). Treat a23-a26 as recall only.

### 2.3 Sociological theories

| Theory | Claim | Critique | Ids |
|---|---|---|---|
| Hessen (1931) | Newton's Principia answered technical and economic needs, with ballistics central. Opened externalist history. | Called vulgar Marxism. Hessen was shot 20 Dec 1936, rehabilitated 1956. | a10 |
| Merton thesis (1936/38) | Puritan and Pietist values fed English science. | Cannot define the right Protestant. Cannot explain Catholic scientists (Copernicus, Descartes, Galileo). Merton: helped, not necessary. | a08 |
| Merton norms (1942) | Four imperatives: communism, universalism, disinterestedness, organized scepticism. Peer scrutiny explains low fraud. | Mitroff (1974, Apollo scientists) found counter-norms: secrecy, particularism, self-interest, organized dogmatism. CUDOS adds Originality (Ziman 2000). | a09 |
| Latour and Woolgar (1979) | Lab as inscription factory. Statements climb a five-level facticity scale. Credibility runs in a cycle that funds careers. | Reductive; later reframed as actor-network theory. 1986 edition dropped "social". | a11 |
| Collins (1985) experimenter's regress | A good experiment is one that gives the right result; the right result is known only from a good experiment. Replication cannot end disputes; negotiation does. | Franklin: critics of Weber had independent anchors (calibration pulses, shared data, a found programming error), so the critics were "far more credible". The regress is not vicious. | a12, d16 |

The Weber gravity-wave case (d16): six negative experiments. Critics shared data and programs, injected pulses of known energy, and Weber's group "could not detect such calibration pulses". The way out of the regress was an independent calibration, not more replication of the same kind.

### 2.4 Quantitative social history of science

- **Peer review noise.** Cortes and Lawrence reran the 2014 NeurIPS two-committee analysis (b01-b03, b21). Detail in section 3.
- **Team size.** Wu, Wang and Evans (2019): small teams disrupt, large teams develop (b16, d12). Park, Leahey and Funk (2023) report broad decline in disruption (d13, b17). The CD index has known flaws (b19) and a critique called the decline an artifact (b18).
- **Matthew effect.** LLMs reproduce and amplify it in citations (a22, c12).

## 3. Core findings with exact numbers

Status key: E established (2+ independent sources), S single source, C contested, H human-only or simulation-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Two independent committees disagree on accept decisions | 166 papers; disagree on 43 (25.0%). Of 43 accepted by committee 1, committee 2 accepted 22 (51%). Of 44 accepted by committee 2, committee 1 accepted 22 (50%). Calibrated score correlation r=0.55, SE 0.065 | Cortes and Lawrence 2021 (b01, b21) | S (one conference, 2014) |
| About half of reviewer score variance is subjective | 50% estimated | same (b02) | S, model-based |
| Accepted-paper scores do not predict citations | about 400 papers, no significant correlation with log10(1+citations); rejected-then-published papers did show one | same (b03) | S |
| Idea-review agreement is low | split-half 56.1% vs 66.0% (NeurIPS 2021) vs 71.9% (ICLR 2024) | Si et al 2024 (b11, a13) | E (K07, 3 sources) |
| LLM ideas rated more novel, before execution | novelty human 4.84 (n=119 reviews) vs AI 5.64 (n=109), Bonferroni p<0.01; AI + human rerank 5.81; feasibility 6.61 vs 6.34 (p=1.00). 49 writers, 79 reviewers (104 people), 298 reviews | Si et al 2024 (a13, b10, b24) | S |
| Novelty gap vanishes after execution | N=43, over 100 hours each. Score change human vs AI: novelty -0.010 vs -1.049; excitement +0.078 vs -1.760; effectiveness -0.052 vs -1.879 (FDR p<0.05) | Si et al 2025 (b12) | S |
| Pre-execution scores barely predict post-execution | AI ideas r: novelty -0.019, excitement -0.321, effectiveness 0.172, overall -0.092; human r: -0.084, 0.205, 0.022, 0.158 | same (b13) | S |
| LLM idea generation is mostly duplicates; LLM ranker is weak | about 5% non-duplicate at cosine 0.8; best ranker (Claude-3.5-Sonnet) 71.4% pairwise vs 61-64% others | Si et al 2024 (a14, b11) | S |
| GPT-4 review comments overlap like a second human | Nature family 3,096 papers 30.85% vs 28.58% human-human; ICLR 1,709 papers 39.23% vs 35.25%; range 15.58% to 39.16% by journal; 308 researchers: 57.4% helpful, 82.4% better than some human reviews | Liang et al 2023 (b04, b05, b22) | S |
| LLM reviewer matches humans only after calibration | balanced acc 0.65 vs 0.66; F1 0.57 vs 0.49; AUC 0.65; accuracy 0.66 vs human 0.73 (imbalanced). Uncalibrated: Sonnet 3.5 acc 0.40, FPR 0.95; GPT-4o-mini FNR 0.94; always-reject acc 0.59. Two random human reviewers correlate 0.14, LLM vs mean human 0.18 | Lu et al 2024 (a16, b06, b23, c14) | E (K09) |
| LLM reviewers are lenient and prestige-biased | Agent Laboratory automated 6.1 vs human 3.8 out of 10. Economics: 29,000+ evaluations of 1,220 papers, bias test 8,910 evaluations on 330 papers; top male authors and elite affiliations rated higher | Schmidgall 2025; Pataranutaporn 2025 (a19, b14, b15) | E (K10) |
| Judge panel beats single big judge | Cohen kappa vs humans NQ/TQA/HPQA: GPT-4 0.627/0.841/0.830; PoLL (3 small judges, different families) 0.763/0.906/0.867; 7-8 times cheaper | Verga 2024 (d10) | E with d11 (K29) |
| Single judges have position bias | GPT-4 consistency after order swap 65.0% (few-shot 77.5%); GPT-3.5 46.2%; Claude-v1 23.8% (75.0% favour first); self-preference GPT-4 +10% win rate, Claude-v1 +25% (authors: too small to conclude) | Zheng 2023 (d11) | E |
| Simulated review panels show conformity and authority bias | rating spread -27.2% after discussion; review length -18.7% (195.5 to 159.0 words) after one low-effort reviewer; 27.7% decisions change when identities known for 10% of papers; Jaccard 0.364/0.154/0.008 for 1/2/3 informed reviewers (weaker papers); no-rebuttal Jaccard 0.622; no-rating 0.20; 53,800 documents; GPT-4 only | Jin et al 2024 AgentReview (a17, a18, c03-c06) | S, H (simulation) |
| Automated research pipelines are cheap and fail often | $10-15 per paper, $0.25-0.50 per review; independent test: 5 of 12 experiments (42%) failed on code errors, median 5 citations, 5 of 34 from 2020+, 8% more characters per iteration, known ideas called novel | Lu 2024; Beel and Baumgart 2025 (a15, b07, b08, c15) | E (K14) |
| One AI-written paper cleared a workshop bar | 3 submitted, scores 6, 6, 7 (mean 6.33, top 45% of 43), withdrawn; best paper per idea picked from seeds | Yamada 2025 (b09, d05) | S |
| Shared prior reports help research agents | MATH-500 base 70.2%; with prior papers best 78.2% (+8.0 points, quoted as +11.4%); isolated plateau 73.4% and 73.8%; 3 labs sharing best 79.8%, mean 78.7% vs 77.4% three sequential runs; compute 3x (+$187.6, +203.9%); tracked number is best test accuracy | AgentRxiv (a20, d03, d04) | S |
| Agents replicate papers poorly | PaperBench 20 ICML 2024 papers, 8,316 tasks: best BasicAgent Claude 3.5 Sonnet 21.0%, o1 IterativeAgent 24.4%; humans (3-paper subset, 48 h) 41.4% vs o1 26.6%; CORE-Bench best 21% on hardest level (270 tasks, 90 papers); ScienceAgentBench 32.4% (102 tasks, 44 papers) | c19, c20, c21 | E (K21) |
| Executed check converts samples to accuracy; votes plateau | SWE-bench Lite 15.9% to 56% at 250 samples with tests; MATH voting 40.50% to 41.41% from 100 to 10,000 samples while coverage rises 82.9% to 98.44% | Brown 2024 (d06) | S |
| Debate rarely beats CoT or self-consistency | SoM below CoT on 9 of 9 datasets (GPT-4o-mini); more agents (3 to 9) or rounds (2 to 4) stagnate or decline; mixing two model families +6.4% (Heter-SoM) and +8.2% (Heter-EoT) over averages | Zhang 2025; Smit 2024 (d07, d08) | E (K27) |
| LLM outputs are homogeneous | within-prompt similarity usually above 0.8; 42 models 0.821; between models 0.71-0.82; 26K queries, 31,250 human annotations | Jiang 2025 (d09) | S |
| LLMs cite with heightened Matthew effect | no effect size read | Algaba 2024 (a22, c12) | S (abstract only) |
| LLM feedback to reviewers gets used | ICLR 2025 RCT: 44,831 reviews, 18,946 received feedback; 26.6% updated vs 9.4% control (2,103 of 22,364); updated reviews +80.3 words vs +2.1; 89% of 100 pairs preferred updated (two annotators); mean score change no different | Thakkar 2025 (d01, d02) | S |
| LLM text in real reviews | 6.5% to 16.9% of reviews substantially modified, linked to lower confidence and near-deadline reviews | Liang 2024 (c10) | S (abstract) |
| Larger teams are less disruptive | 1 to 50 members: -70% papers, -30% patents, -50% software; solo authors 72% more likely than 5-person teams in top 5% disruption; two thirds of the effect within the same scientists; 86% of journals negative slope; over 50M teams | Wu et al 2019 (b16, d12) | C (index disputed) |
| Broad decline in disruptiveness | 105 studies, mostly decline; disruptive papers 50% to 25% (1965-2020, 41M papers); Holst critique rebutted (decline holds on 6 of 7 measures) | b17, b18, d13 | C |
| Boyle recorded failures and witnesses | primary 1660 text: leaks admitted, failures recommended for recording, named witnesses | d14, d15 | E (K30) |
| Replication failed for 18+ months (Huygens) | over 18 months, resolved by on-site demonstration | a02, c24 (Wikipedia) | S |

Note: the 43 papers disagreed on and the 43 accepted by committee 1 in Cortes and Lawrence are two different counts. Do not merge them.

## 4. Mechanisms and models

Each mechanism is stated so it can be coded.

**M1. Witnessed claim ledger (Boyle).** A claim is stored as a record: statement, procedure, raw output, instrument and version, setting, who or what ran it, failed trials, and every independent re-run. Status rises only when an independent re-run passes. Failures and instrument defects are logged, not dropped. Boyle did exactly this (d14). Latour and Woolgar's facticity scale (a11) is the same idea: a statement gains status as qualifiers are stripped by checks. This maps to our [E]/[S]/[D] marks.

**M2. Matched-instrument replication.** A re-run is comparable only if instrument and setting match. Before treating a failed re-run as a refutation, code diffs the two runs (tool version, seed, prompt, data, environment). Huygens's anomalous suspension is the cautionary case (a02). Rule: failed re-run, then diff, then validate the check, then verdict.

**M3. Regress breaker.** When the claim and the checker disagree, add a different kind of check (a calibration input of known answer, a symmetry, a held-out example). Do not add more copies of the same check. This is Franklin's reading of the Weber case (d16) and matches G3.

**M4. Noisy gate model.** A single reviewer is a noisy measurement. Cortes and Lawrence model reviewer score as quality plus personal opinion, with about 50% of variance being opinion (b02). Implication: average independent judges to cut noise; the gain is limited by shared bias. Review is better at rejecting weak work than at ranking the best (b21, b03). Use gates to reject, not to pick winners.

**M5. Agreement versus independence.** Judge panels help only when members are independent. PoLL used three different families (d10). Same-family samples are over 0.8 similar (d09). Debate adds correlated conformity (a17, d07). A panel of different families, scored separately, with code doing the vote, is the working pattern.

**M6. Executed check as the real instrument.** The ideation-execution result (b12, b13) says judged plausibility is nearly uninformative about run outcome. Large Language Monkeys (d06) shows the same from another side: with a verifier, more candidates become more solved items; without one, voting plateaus. The executable test is the pump; the judge is the committee. Select with the pump.

**M7. Calibrated judge.** Uncalibrated LLM reviewers lean to accept (FPR 0.95) or reject (FNR 0.94) (b23). Fix: tune the decision threshold on a held-out labelled set, swap answer order, ensemble 5 reviews, reflect 5 times (b06). Position bias: GPT-4 is only 65.0% consistent after a swap (d11).

**M8. Blinding.** Universalism as code: strip author, model name, affiliation and fame cues before judging. LLM judges copy prestige bias (b15). In AgentReview, identity knowledge changed 27.7% of decisions in simulation (c05).

**M9. Shared memory between runs (AgentRxiv).** Runs publish short reports to a server. Later runs read them. Isolated runs plateaued at 73.4-73.8%, shared runs reached 78.2% (d03). Caveats: the metric is best test accuracy, there are two isolated curves, MATH-500 only.

**M10. Diversity as a resource.** Same-model samples are near duplicates (about 5% unique at cosine 0.8, a14; similarity above 0.8, d09). Diversity must come from different model families, forced frames, or retrieved sources. Heter-MAD with two families gained +6.4% to +8.2% over averages (d07).

## 5. What holds up

**Holds (2+ sources or primary text)**
- Human review is noisy: 56.1% to 71.9% split-half agreement for idea and paper review, 25% decision disagreement, r=0.55 (b01, b11). [K07]
- LLM judges are biased and lenient: overrate (6.1 vs 3.8), prestige bias, position bias, self-preference (a19, b15, d11). [K10]
- Calibration is required before an LLM reviewer matches human accuracy (a16, b23). [K09]
- A diverse small-judge panel beats one big judge (d10, d11). [K29]
- Debate does not beat self-consistency; model mixing helps (d07, d08). [K27]
- Automated research pipelines fail on code and novelty checks (b07, b08, b25). [K14]
- Replicating papers from scratch is still hard for agents (c19-c21). [K21]
- Boyle documented failures and witnesses (d14, d15). [K30]

**Fails, contested or weak**
- Pre-execution novelty advantage for LLM ideas did not survive execution in a later, smaller study from the same group (b12 vs b10). Treat novelty-before-execution as unreliable. [K11, K12]
- The disruption decline is contested. The index has inconsistency and time dependence (b19). A data-artifact critique exists (b18). The figures come from a 2026 review summary, plus Wu 2019 re-opened (d12). [K22]
- Merton's norms and the Puritan thesis are contested, with weak numbers (a08, a09). [K04]
- Collins's regress is contested by Franklin (d16). [K03]
- AI Scientist-v2 workshop paper: 1 of 3, selected from seeds, authors' own review said below main-track bar, no independent replication found (d05). [K15]
- AgentReview effects come from GPT-4 agents only and were never compared to real review outcomes (c02, a17). The 37.1% variation figure was not explained in the text. [K18]
- Thakkar: the older "27% of 20,000" was a conflation. Right figures: 26.6% of 18,946 recipients vs 9.4% control. It measures engagement and length, not correctness (d01, d02). [K19]

**Moderators and boundary conditions**
- Liang overlap varied 15.58% to 39.16% across Nature journals (b22). Overlap is not correctness.
- Debate gains appear only with an execution step (AgentVerse on HumanEval) or mixed model families (d07).
- The verifier advantage needs an automatic verifier. For MATH, voting and reward models plateau near 100 samples (d06).
- LLM judges track humans less well when answers are of similar quality (d09).
- Authority cues hurt lower-quality papers more in AgentReview (c05), so blinding matters most for weak items.
- PaperBench: an iterative scaffold helped o1 (24.4%) but hurt Claude (16.1% vs 21.0%) (c19). Scaffold gains are model-specific.

**Interventions that worked**
- Human reranking of LLM ideas (excitement 4.85 to 5.34, p=0.04) (b24).
- Reflection plus ensembling plus a tuned threshold for the reviewer (b06).
- Shared prior reports (d03, with caveats).
- LLM feedback agent raised reviewer update rate 9.4% to 26.6% (d01).

**Interventions that did not work**
- LLM self-ranking of ideas (71.4% at best, a14).
- Adding agents or rounds to debate (d07).
- Removing numeric ratings (scrambled outcomes, Jaccard 0.20, c06).
- LLM reviewer feedback did not change mean score (d02).

## 6. Language models

How LLMs behave on tasks this field defines:

1. **As reviewers.** Overlap with a human reviewer matches human-human overlap (30.85% vs 28.58%; 39.23% vs 35.25%) (b04). Accuracy 0.66 vs human 0.73 on the imbalanced set; balanced accuracy 0.65 vs 0.66 after calibration (a16). Uncalibrated: accept bias (FPR 0.95, acc 0.40) or reject bias (FNR 0.94) (b23). They overrate versus humans by 2.3 points (a19). Prestige bias appears in GPT, Gemma and Llama (b15). Claude and Gemma tracked journal gradients best; GPT was best at spotting AI-written submissions (b27).
2. **As idea generators.** Judged more novel than expert humans (5.64 vs 4.84) (a13), but only about 5% unique after dedup (a14). After execution, AI ideas fell about 1.0 to 1.9 points on all metrics while human ideas stayed flat (b12). Human reranking helped; LLM self-ranking did not.
3. **As scientists.** Pipelines cost $10-15 per paper (a15), but 42% of runs failed on code (b08) and numbers were hallucinated (b25). Replication from papers: best 21.0% (PaperBench, Claude 3.5 Sonnet basic agent); humans 41.4% on a subset vs o1 26.6% (c19). CORE-Bench 21% (c20). ScienceAgentBench 32.4% (c21).
4. **As a community.** Agents sharing reports improve more than isolated ones (d03). Simulated reviewer groups converge (-27.2% spread), copy authority, and lose effort after a lazy peer (a17, a18). These are simulations (K18).
5. **As citers.** LLMs cite more famous work than humans do (a22).
6. **What changed results, and by how much.**
   - Executed verifier: 15.9% to 56% (d06).
   - Panel of 3 families vs one GPT-4 judge: kappa 0.627 to 0.763 on NQ (d10).
   - Few-shot prompt for GPT-4 position consistency: 65.0% to 77.5% (d11).
   - Mixed model families in debate: +6.4% to +8.2% (d07).
   - Human rerank of ideas: excitement +0.49 (b24).
   - Shared agent memory: 73.4-73.8% to 78.2% (d03).
   - Feedback agent: reviewer update rate +17 points (d01).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory (section 5), log (section 6). Status: [E] established, [S] single-source, [C] contested. Many items confirm existing guardrails (G2, G3, G5, G8, G9). For those the item is "confirm, with a new number", not new text.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Log judge agreement (repeat or paired judging) beside accuracy in every eval. Human split-half agreement is 56% to 72%, so a judge below that is noise | log, G5 | [E] | b11, b01, a16; K07 |
| A2 | Calibrate any LLM judge threshold on a held-out labelled set before it is used in a loop. Uncalibrated judges accept almost all or reject almost all | G5 | [E] | a16, b06, b23; K09 |
| A3 | Blind judges to author, model name and prestige. Swap answer order and score both. Keep scores length-normalised (already G5) | G5 | [E] | b15, a18, d11; K10 |
| A4 | If a judge is used at all, use three judges from different families, scored independently, with code taking the vote. Evidence is for QA grading, not for our ideas | G5, G4 | [E] | d10, d11, d09; K29 |
| A5 | Keep G9 (no debate). New numbers: SoM below CoT on 9 of 9; more rounds or agents do not help | G9 | [E] | d07, d08; K27 |
| A6 | Run log lists failed trials, tool defects and who or what ran each check (Boyle's rule) | log, memory | [E] primary text | d14, d15; K30 |
| A7 | Require executed evidence for any numeric claim and run a claims-versus-numbers consistency check (generated reports had hallucinated numbers and contradicted their own tables) | G2, G3 | [E] | b07, b08, b25, c14; K14 |
| A8 | Do not cite agent simulations (AgentReview, CABAL, Elo) as evidence about humans | process | [E] | c02, c07, c08; K18 |
| A9 | Use "replicate a result from a written description" as a held-out reasoning test | bench | [E] (hard for all agents) | c19-c21; K21 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Gate candidates by a cheap executed test, not by judged plausibility; compare at equal tokens | S4/S7, G8 | [S] | b12, b13, d06, d07; K12, K26 |
| T2 | Independent first round then code vote versus a discussion round: does answer spread fall, and does accuracy change? | S3, G4, G9 | [S] | a17, d07, d09; K17 |
| T3 | When a re-run fails, diff instrument and settings before declaring failure (matched-instrument rule) | S5/S8 | [S] | a02, d14; K02 |
| T4 | Mixed model families or forced frames for candidates; measure embedding similarity and unique-answer yield | S3, G4 | [S] | d09, a14, d07; K13, K28 |
| T5 | Shared memory of prior failed attempts across runs versus isolated runs | memory | [S] | d03, d04; K16 |
| T6 | Repeated judge sampling: how many judge samples before agreement passes about 70%? | G5 | open | no curve exists (d10, d11) |
| T7 | Dedup step at S3 (cosine 0.8) before testing | S3 | [S] | a14; K13 |
| T8 | Does our judge shift when a prestige or source cue is added? | G5 | [S] | b15; K10 |
| T9 | Popularity-skew check on retrieved or cited sources | S3 (grounding) | [S] | a22; K20 |
| T10 | Larger same-family ensembles give less novel answers than small mixed ones | G5, G12 | [C] | d12, d09; K22 |
| T11 | Seed a case where claim and checker disagree; does the agent add a different kind of check or loop? | S6, G3 | [C] | a12, d16; K03 |

## 8. Concrete tests on our bench

All arms get equal total tokens, with setup counted (G7). Items come from our existing suites (ARC portfolio, brainteasers, NoveltyBench open items) unless noted.

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Items with an executable check (ARC programs, code tasks) | (a) generate N, select by executed held-out test; (b) generate N, select by LLM judge; (c) generate N, select by vote | solved rate on hidden test | (a) beats (b) and (c); (b) near (c). Large Language Monkeys suggests at least several points |
| B2 (T2) | Single-answer items with spread (brainteasers) | (a) independent answers + code vote; (b) same answers + one discussion round | accuracy; distinct-answer count after the step | (b) shows lower spread, accuracy not higher (expect -5 to 0 points) |
| B3 (T3) | Tasks where a check can fail for instrument reasons (planted tool-version mismatch) | (a) agent diffs setting before verdict; (b) agent declares failure on first failed re-run | wrong-refutation rate | (a) lowers wrong refutations |
| B4 (T4) | NoveltyBench open items | (a) same model N samples; (b) mixed families; (c) forced frames | unique-answer count after dedup at cosine 0.8 | (b) and (c) above (a); similarity below 0.8 |
| B5 (T5) | Repeated task class over 10 to 20 runs | (a) isolated; (b) shared lessons from prior failed attempts (shown after first attempt, per section 5) | held-out accuracy (not best-so-far) | (b) +2 to +5 points; if no gain, drop |
| B6 (T6) | 200 pairs of answers with human or code labels | judge sampled 1, 3, 5, 9 times, mixed families | agreement with label; curve vs number of judges | plateau by 3 to 5; find where agreement passes 70% |
| B7 (T8) | Same answers with and without a prestige or source label | blind vs unblind judge | score shift (points) and flip rate of pairwise verdict | unblinded shifts; blinded flat |
| B8 (T9) | Source-citing tasks | agent ranks by fame vs agent weights by check | share of top-decile-cited sources | fame ranking skews |
| B9 (T10) | Open ideas | ensemble sizes 3, 10, 30 same-family vs 3 mixed | unique-answer yield per token | same-family yield flattens beyond about 10 |
| B10 (T11) | Planted conflict between checker and claim | (a) agent adds a different kind of check; (b) agent repeats same check | rounds to resolution; correct resolution | (a) resolves in fewer rounds |
| B11 (A1) | Every eval | report judge agreement next to accuracy | present or absent | process; no effect size |

## 9. What does not transfer, and why

- **Social authority as source of truth.** Shapin's gentlemanly trust (a24, recall) is the opposite of our need. Source trust for the agent must come from checks, not status.
- **The claim that credibility is only social.** Critics (Latour, Franklin) say nature pushes back, and calibration can end a regress (d16). We do not adopt it.
- **Merton's norms as a measured effect.** No numbers, and counter-norms exist (a09). Only universalism transfers, as blinding.
- **Disruption and team size.** Observational, index contested, about human careers. Only the loose analogy to ensemble size stays (T10).
- **Reviewer-committee dynamics.** AgentReview shows what GPT-4 agents do, not humans (K18). Our agent is not a committee, so conformity matters only if we add discussion, which G9 forbids.
- **Peer review of papers.** Our items are not papers. Review noise numbers set expectations for judge noise, not for our tasks.
- **Autonomous labs (Adam, Eve, Coscientist).** No numbers verified (c25, c13). Wet-lab instruments do not exist in our loop.
- **Workshop acceptance of AI papers.** 1 of 3, selected from seeds, low bar (d05).
- **LLM-reviewer overlap as validity.** Overlap with a human reviewer is not correctness (b04).

## 10. Open questions

1. What did Shapin and Schaffer and Collins actually argue about replication failure? The books were never opened. Huygens's suspension and the TEA laser case are unverified from primary text.
2. How many independent judge samples are needed before agreement passes about 70%? No agreement-versus-judges curve exists.
3. Does multi-agent discussion collapse diversity by about a quarter, as AgentReview reports? Only simulated evidence exists.
4. Does shared memory of failed attempts help beyond MATH-500, on held-out scores, at equal compute?
5. Does an executed cheap test beat judge selection at equal tokens on our agent? Evidence is by analogy across three task types (d17).
6. Does our own judge show prestige or affiliation bias? Pataranutaporn 2025 was read (b15) but no test on our judge exists.
7. Is there an independent replication of the AI Scientist-v2 workshop result? None found.
8. Are the disruption trends real? The original Holst and Park papers were not opened in full.
9. Why did Si 2024 and Si 2025 differ on novelty? Same group; the later study is smaller (N=43) and the only one that executes ideas.
10. Does the Thakkar feedback agent improve correctness, not just length and engagement? No ground truth was available.

## 11. Sources

[V] opened this session (full text or page text read). [M] snippet, abstract only, or recall.

- [V] Wikipedia, Leviathan and the Air-Pump. https://en.wikipedia.org/wiki/Leviathan_and_the_Air-Pump (a01, a02, c23, c24)
- [V] Wikipedia, Robert Boyle. https://en.wikipedia.org/wiki/Robert_Boyle (a03)
- [V] Wikipedia, Royal Society. https://en.wikipedia.org/wiki/Royal_Society (a04)
- [V] Wikipedia, Micrographia. https://en.wikipedia.org/wiki/Micrographia (a05)
- [V] Wikipedia, Sidereus Nuncius. https://en.wikipedia.org/wiki/Sidereus_Nuncius (a06)
- [V] Wikipedia, Christiaan Huygens. https://en.wikipedia.org/wiki/Christiaan_Huygens (a07; first 100k characters only)
- [V] Wikipedia, Merton thesis. https://en.wikipedia.org/wiki/Merton_thesis (a08)
- [V] Wikipedia, Mertonian norms. https://en.wikipedia.org/wiki/Mertonian_norms (a09)
- [V] Wikipedia, Boris Hessen. https://en.wikipedia.org/wiki/Boris_Hessen (a10)
- [V] Wikipedia, Laboratory Life. https://en.wikipedia.org/wiki/Laboratory_Life (a11)
- [V] Wikipedia, Experimenter's regress. https://en.wikipedia.org/wiki/Experimenter%27s_regress (a12)
- [V] Wikipedia, Robot Scientist. https://en.wikipedia.org/wiki/Robot_Scientist (c25)
- [V] Boyle (1660) New Experiments Physico-Mechanicall, OCR. https://archive.org/details/bim_early-english-books-1641-1700_new-experiments-physico-_boyle-robert_1660 (d14)
- [V] Stanford Encyclopedia, Robert Boyle. https://plato.stanford.edu/entries/boyle/ (d15)
- [V] Stanford Encyclopedia, Experiment in Physics. https://plato.stanford.edu/entries/physics-experiment/ (d16)
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109 (a13, a14, b10, b11, b24)
- [V] Si, Hashimoto, Yang (2025) The Ideation-Execution Gap. https://arxiv.org/abs/2506.20803 (b12, b13)
- [V] Lu et al (2024) The AI Scientist. https://arxiv.org/abs/2408.06292 (a15, a16, b06, b07, b23, c14)
- [V] Jin et al (2024) AgentReview. https://arxiv.org/abs/2406.12708 (a17, a18, c02-c06; the c-lines wrongly say "Li et al")
- [V] Schmidgall et al (2025) Agent Laboratory. https://arxiv.org/abs/2501.04227 (a19, b14, c17)
- [V] Schmidgall and Moor (2025) AgentRxiv. https://arxiv.org/abs/2503.18102 (d03, d04; a20 was abstract only)
- [V] Cortes and Lawrence (2021) Inconsistency in conference peer review. https://arxiv.org/abs/2109.09774 (b01-b03, b21)
- [V] Liang et al (2023) Can LLMs provide useful feedback on research papers? https://arxiv.org/abs/2310.01783 (b04, b05, b22, c09)
- [V] Beel and Baumgart (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297 (b08, b25, c15)
- [V] Yamada et al (2025) AI Scientist-v2. https://arxiv.org/abs/2504.08066 (b09, c16, d05)
- [V] Pataranutaporn et al (2025) Can AI solve the peer review crisis? https://arxiv.org/abs/2502.00070 (b15, b27)
- [V] Wu, Wang, Evans (2019) Large teams develop and small teams disrupt. https://arxiv.org/abs/1709.02445 (b16, b26, d12)
- [V] Wu et al (2026) Is innovation becoming less disruptive? https://arxiv.org/abs/2602.05140 (b17, b18; Holst second-hand)
- [V] Leibel and Bornmann (2023) What do we know about the disruption index? https://arxiv.org/abs/2308.02383 (b19)
- [V] Starace et al (2025) PaperBench. https://arxiv.org/abs/2504.01848 (c19; first 100k of 137k characters)
- [V] Thakkar et al (2025) LLM feedback in peer review, ICLR 2025. https://arxiv.org/abs/2504.09737 (d01, d02, c11)
- [V] Brown et al (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787 (d06)
- [V] Zhang et al (2025) Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788 (d07)
- [V] Smit et al (2024) Should we be going MAD? https://arxiv.org/abs/2311.17371 (d08; numeric table not extracted)
- [V] Jiang et al (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954 (d09)
- [V] Verga et al (2024) Replacing judges with juries. https://arxiv.org/abs/2404.18796 (d10)
- [V] Zheng et al (2023) Judging LLM-as-a-judge. https://arxiv.org/abs/2306.05685 (d11)
- [M] Park, Leahey, Funk (2023) Nature 613:138. https://doi.org/10.1038/s41586-022-05543-x (d13; abstract only)
- [M] Park et al (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (c01)
- [M] Modeling LLM agent reviewer dynamics in Elo-ranked review (2026). https://arxiv.org/abs/2601.08829 (c07)
- [M] CABAL (2026). https://arxiv.org/abs/2609.05227 (c08)
- [M] Liang et al (2024) Monitoring AI-modified content at scale. https://arxiv.org/abs/2403.07183 (c10)
- [M] Algaba et al (2024) LLMs reflect human citation patterns. https://arxiv.org/abs/2405.15739 (a22, c12)
- [M] Boiko et al (2023) Coscientist. https://arxiv.org/abs/2304.05332 (c13)
- [M] Gottweis et al (2025) AI Co-Scientist. https://arxiv.org/abs/2502.18864 (a21)
- [M] Siegel et al (2024) CORE-Bench. https://arxiv.org/abs/2409.11363 (c20)
- [M] Chen et al (2024) ScienceAgentBench. https://arxiv.org/abs/2410.05080 (c21)
- [M] Wang et al (2025) ReviewAgents. https://arxiv.org/abs/2503.08506 (c22)
- [M] Shapin and Schaffer (1985), recall. https://press.princeton.edu/books/paperback/9780691178165/leviathan-and-the-air-pump (a23)
- [M] Shapin (1994) A Social History of Truth, recall. https://press.uchicago.edu/ucp/books/book/chicago/S/bo3641985.html (a24)
- [M] Collins (1985) Changing Order, recall. https://press.uchicago.edu/ucp/books/book/chicago/C/bo3637962.html (a25)
- [M] Schaffer (1989) Glass works, recall. https://en.wikipedia.org/wiki/Simon_Schaffer (a26)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 8 established claims: 5 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D07.07-K10** (reworded: the sources support less). Agent Laboratory's 6.1 vs 3.8 out of 10 is for automated reviews of its own generated papers (human reviewers 3.8), not LLM reviewers in general; Pataranutaporn et al. find prestige and elite-affiliation bias only for GPT, Gemma and LLaMA (not Claude), and Lu et al. report near-human reviewer accuracy. Corrected claim: In Agent Laboratory, automated LLM reviewers rated the system's own generated papers 6.1/10 versus 3.8/10 from human reviewers, and in an economics-paper experiment GPT, Gemma and LLaMA (not Claude) gave higher ratings to top male authors and elite institutions, so LLM reviewers can overrate self-generated work and reproduce prestige and affiliation bias.
- **D07.07-K21** (reworded: the sources support less). The 21.0% agent score is the average over all 20 PaperBench papers; the 41.4% human score is best-of-3 on a 3-paper subset at 48 h, where the best agent (o1) scored 26.6%, so the two are not like-for-like. Corrected claim: Agents replicate papers poorly: best PaperBench agent 21.0% averaged over 20 papers; on the 3-paper subset humans (ML PhDs, best of 3 after 48 h) scored 41.4% vs 26.6% for o1; CORE-Bench best agent 21% on the hardest level; ScienceAgentBench best agent solves 32.4% independently.
- **D07.07-K30** (reworded: the sources support less). OCR confirms leaks, failed trials and the recommendation to recite failed experiments (Exp. 15), and SEP supports awareness of non-replication, but neither source shows named witnesses (the 1660 text I read only has unnamed ingenious persons). Corrected claim: Boyle's 1660 text itself records air-pump leaks and failed trials and says it is useful to recite experiments that miscarry as well as those that succeed; the SEP notes Boyle knew some results could not be replicated.
- **D07.07-K09** (now single-source: only one opened source, code check).
