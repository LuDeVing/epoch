# Peer review and replication: deep document

Subfield F03.09 (sociology of knowledge). Focus: biases in publication; replication is rare; contradicted results persist. Key works: Ioannidis 2005; Lee et al. Why it matters for our agent: G3 (held-out checks work as replication).

Evidence ids (a01 to d20) refer to evidence_a-d.jsonl in this folder. Claim ids (F03.09-K01 to K27) refer to claims.jsonl. Calibration, social epistemology, epistemic diversity and conformity are parallel subfields; they are linked here, not repeated.

## 1. What it is

Science has two filters. Peer review decides what gets published. Replication decides what stays believed. This subfield asks how well each filter works, and what that teaches a single reasoning agent that must filter its own claims.

Three facts frame everything.

- A positive result is weaker evidence than it looks. Whether it is true depends on power, prior odds, analytic flexibility and how many teams tried (a01, a03, b01).
- Independent re-runs shrink effects and often fail. Psychology, economics, top-journal experiments and preclinical cancer biology all show it (d01, d04, d05, b02).
- The system does not clean itself. Failed results are cited more, not less. Only 12% of later citations of a non-replicable paper mention the failure (a04, a05, b04). Review itself is noisy: two committees disagree on about a quarter of papers (a14, b06).

For an agent, the mapping is direct. A first pass that fits the given examples is a published finding. A held-out check is a replication. A model judge is a reviewer. What the field learned about reviewers, replications and citation chains has a counterpart in the schema: G3 (pass only on unfitted data), G5 (code selects, blind judges), G9 (no debate), and a memory that records refuted claims.

Two kinds of repeat must be kept apart.

- Reproduction: same data, same code, same answer. Tests the pipeline.
- Replication: new data or new sample, same claim. Tests the claim.

Most AI-agent benchmarks here (CORE-Bench, SocSci-Repro-Bench) test reproduction. Only a few (PaperBench re-implementation, ReplicatorBench) touch replication.

## 2. History and theories in depth

**Ioannidis (2005).** A Bayesian model, not a count. Let R be the prior ratio of true to false relationships tested, alpha the false-positive rate (0.05) and beta the miss rate. The chance a claimed finding is true (PPV) is (1-beta)R / (R - beta R + alpha). A finding is more likely true than false only if (1-beta)R > alpha. Six corollaries: small studies, small effects, many tested relationships, flexible designs, financial or other interests, and hot fields all lower PPV. Table 4 simulations: an adequately powered RCT with 50% prior is true about 85% of the time; an underpowered early-phase trial about 1 in 4; exploratory epidemiology at R=1:10 about 1 in 5; massive testing (30,000 genes, 30 true) extremely low. Box example: R=1e-4, power 60%, PPV about 12e-4; with bias u=0.10, 4.4e-4; ten independent teams and one hit, 1.5e-4 (a01 to a03, b01). The inputs are assumed, so the paper shows a mechanism, not an actual false-paper rate. Later empirical projects support the direction (K01).

**Smaldino and McElreath (2016).** Selection on output. A 60-year review of statistical power finds mean power 0.24 for small effects (d=0.2) with no trend (R squared 0.00097). In an agent-based model of competing labs that copy the methods of high-output labs, power and false-positive rate drift to 1 and effort falls. Replication slows the decline but does not stop it. The evolved replication rate settled near 0.08. Forcing 25% or 50% replication still let effort fall to its floor, later. A positive replication paid half a novel result (a11 to a13, c23). Lesson: the reward counts output, not truth.

**The replication projects.**
- Open Science Collaboration (2015): 100 psychology studies. 97% of originals significant, 36% of replications significant; 47% of original effect sizes inside the replication 95% CI; 39% subjectively rated as replicated; mean effect about half the original (d01).
- Gilbert et al. (2016) argued the data fit high reproducibility given sampling error; Anderson et al. replied that both optimistic and pessimistic readings fit (d02, d03; abstracts only).
- Camerer et al. (2018): 21 Nature/Science experiments, preregistered, samples about 5 times larger, original authors reviewed protocols. 13 of 21 (62%) significant in the same direction, mean effect about 50% of original (d04).
- Many Labs 2: 28 findings, 125 samples, 15,305 participants, 36 countries. 15 of 28 (54%) at p<.05, median d 0.60 original vs 0.15 replication, 9 of 28 in the opposite direction (d05).
- Preclinical cancer biology (Errington et al. 2021): 193 planned experiments, 50 completed, median effect 0.43 vs 2.96, 85% smaller (b02).
- Begley and Ellis (2012) is widely cited (6 of 53) but never opened here. Do not cite its number (d20).

**Citation and authority.** Greenberg (2009) mapped one claim (beta amyloid in inclusion body myositis): 242 papers, 675 citations, 220,553 citation paths. Supportive citations grew sevenfold to 636 and supportive paths 777-fold between 1996 and 2007; the critical view reached 21 citations. Of the 10 most authoritative papers only 4 had data, all from one lab. Three mechanisms: citation bias (ignore the critical data), amplification (repeat without new data), invention (a hypothesis restated as fact) (a08 to a10). Serra-Garcia and Gneezy (2021): papers that failed replication are cited more, about 16 more times a year; replicable papers are cited 153 fewer times in total (N=80); only 12% of post-replication citations acknowledge the failure (a04, a05, b04). Their account: reviewers trade interest against rigor (a07).

**Peer review noise.** Cortes and Lawrence (2021) re-examined the NeurIPS 2014 experiment: two committees, 166 papers, 43 disagreements (25.9%; the paper text prints 25.0% but 43/166 is 25.9%). Of 43 accepted by committee 1, committee 2 accepted 22. Score correlation 0.55 (SE 0.065). About half of a reviewer's calibrated score is subjective. Among about 400 accepted papers, quality score did not predict citations; among 680 rejected papers it did (a14 to a16, b05). NeurIPS 2021 repeat: 882 papers, 203 inconsistent (23.0%), random baseline 35.1%, 50.6% of accepted papers would be rejected by the other committee, r=0.575 (b06). Pier et al. (2018): 43 reviewers, 25 NIH applications, no agreement (a17; not opened).

**Reproducibility in ML.** Raff (2019): 255 papers reimplemented without author code, 63.5% reproduced; readability was the strongest predictor; author reply (52% replied) predicted success, p=0.004 (b07, b25). Henderson et al. (2018): two sets of 5 seeds of the same RL algorithm differed, t=-9.09, p=0.0016 (b09). Pineau et al. (2021): checklist and code-submission policies, 173 papers claimed in the reproducibility challenge (b08).

**LLMs enter the loop (2023 to 2026).** LLMs as reviewers (Liang, Lu, Si, Ye), as review assistants (Thakkar), as silent review writers (Liang 2024, Latona), as replicators (PaperBench, CORE-Bench, SocSci-Repro-Bench, ReplicatorBench), and as autonomous analysts (Many AI analysts). Section 6 covers these.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| PPV of a positive result depends on power, prior, bias | PPV=(1-b)R/(R-bR+a); true only if (1-b)R>0.05; RCT with 50% prior about 85%; underpowered early trial about 25% | Ioannidis 2005 (a01, a03, b01) | Established as a model; sizes assumed |
| Psychology replications | 97% of originals significant vs 36% of 100 replications; 47% of original effects in replication CI; 39% subjective; effects about half | OSC 2015 (d01) | Established; Gilbert critique unresolved (d02, d03) |
| Nature/Science social experiments | 13 of 21 (62%); mean effect about 50% of original; 71% for estimated true positives | Camerer 2018 (d04) | Established |
| Many Labs 2 | 15 of 28 (54%) p<.05; 14 at p<.0001; median d 0.60 to 0.15; 9 of 28 opposite direction; setting and WEIRD explained little | Klein 2018 (d05) | Established |
| Decision market forecasts | 12 highest-priced replicated 83%, 12 lowest 33%; overall 54% of 41; replicated effects 45% of original | Dreber 2025 (d06) | Supported; humans only |
| Preclinical cancer | 50 of 193 experiments done; median ES 0.43 vs 2.96; 42/97 (43%) significant same direction; 17/97 (18%) in original CI; 5 moderators explained nothing | Errington 2021 (b02, b03) | Single-source |
| Failures are cited more | about 16 more cites per year; 153 fewer total for replicable (N=80); 12% of later citations note failure | Serra-Garcia 2021 (a04, a05, b04) | Single-source |
| Citation distortion | 242 papers, 675 citations, 220,553 paths; support x7 to 636; critical 21; 4 of 10 top papers had data | Greenberg 2009 (a08, a09) | Single-source (one case) |
| Low power, no trend | mean power 0.24 for d=0.2; R2=0.00097 over 60 years; evolved replication rate 0.08 | Smaldino and McElreath 2016 (a11, a13) | Single-source; model |
| Committee disagreement | 43 of 166 (25.9%) 2014; 203 of 882 (23.0%) 2021; random 35.1%; 50.6% of accepts rejected by other committee; r 0.55 and 0.575 | Cortes and Lawrence; Beygelzimer (a14, b05, b06) | Established |
| Subjective share of score | about 50% of a calibrated score; no quality-to-citation link among accepted | Cortes and Lawrence (a15, a16) | Single-source |
| ML reimplementation | 162 of 255 (63.5%); author reply p=0.004; seeds t=-9.09 | Raff 2019; Henderson 2018 (b07, b09) | Established |
| LLM review overlap with humans | Nature 30.85% vs human-human 28.58%; ICLR 39.23% vs 35.25%; rejected papers 43.80%; shuffled 0.43% and 3.91% | Liang 2023 (a19, c01, c03) | Single-source |
| LLM reviewer accept/reject | balanced accuracy 0.65 vs human 0.66; FPR 0.31 vs 0.17; raw Sonnet 3.5 0.52 (FPR 0.95) | Lu 2024 (c04) | Contested |
| Idea ranking by LLM judge | 53.3% pairwise vs inter-reviewer 56.1%; NeurIPS 2021 66.0% | Si 2024 (c06) | Contested |
| LLM ideas, before vs after execution | novelty 4.84 human vs 5.64 AI (p<0.01); after execution AI dropped 1.05 novelty, 1.88 effectiveness; human -0.01, -0.05 | Si 2024; Si 2025 (b13, b14) | Established (same lab) |
| LLM reviewers are manipulable | rating 5.34 to 7.99; agreement with injected text 90%; title-only at or above 42% of full papers | Ye 2024 (a23, a24) | Single-source |
| LLM use in review | 6.5% (CoRL 2023) to 16.9% (EMNLP 2023) of text; at least 15.8% of ICLR 2024 reviews; +4.9 points acceptance for borderline | Liang 2024; Latona 2024 (c10, b12) | Established |
| Review feedback agent | 44,831 reviews, 18,946 got feedback, 26.6% updated, 12,222 suggestions, +80 words | Thakkar 2025 (b11) | Single-source |
| Agents replicating ML papers | PaperBench 21.0% best vs ML PhD 41.4% (3 papers, o1 26.6%); SciReplicate 39% | Starace; Xiang (a25, a26, b17) | Established |
| CORE-Bench | CORE-Agent GPT-4o 60.00 / 57.78 / 21.48 (Easy/Medium/Hard); mini 44.44 / 32.59 / 16.30 | Siegel 2024 (c12) | Established |
| Scaffold beats budget | Easy 35.6% to 60% with task hints; cost limit 26% to 31%; IterativeAgent o1 13.2% to 24.4%, Sonnet 21.0% to 16.1% | c13, c15 | Established |
| Confirmation prompt hides failure | Codex overall 62.1% to 74.1% but non-reproducible 90% to 60%; Claude 100% to 70% | Alizadeh 2026 (c20) | Supported (N=10 tasks) |
| Social-science reproduction | Claude Code 93.4% task accuracy; Codex 62.1%; pre vs post cutoff 93.3 vs 96.2 | c17, c18 | Established |
| Judges favour their own text | GPT-4 recognizes own summaries 73.5%; self-preference score 0.749 | d07, d08, d09 | Supported (3 sources) |
| Self-critique without oracle | GPT-3.5 CommonSenseQA 75.8 to 41.8; GSM8K 75.9 to 74.7; oracle labels 95.5 | Huang 2024 (d10) | Single-source |
| External verifier converts samples | SWE-bench Lite 15.9% to 56% at 250 samples; voting plateaus near 100 | Brown 2024 (d13) | Supported |
| LLM judge self-inconsistency | alpha 0.27 to 0.79; 61.3% identical on 3 runs (MT-Bench best model) | Haldar 2025 (d15, d16) | Single-source |
| Many AI analysts | 4,946 runs; confirmation personas +34 to +66 points support rate | PNAS 2026 (d18, d19) | Single-source |
| AI tools on retracted papers | best 8 of 15 (53.3%); research tools 0 fully correct | d17 | Single-source |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

**M1. PPV update (Ioannidis).** Inputs: prior odds R, power 1-b, alpha. Output: posterior that a hit is true. Agent form: keep a per-item-type prior of how often a first-pass answer holds up on a held-out check. A lone positive result then has a posterior, not a status of true. Take R from our own bench history, not a guess. With bias u (a share of analyses reported positive regardless), PPV drops further. The agent analogue of u is the number of candidate programs or specs tried before one fits. Rule: log how many candidates were tried before the one that passed; discount by that count (corollaries 3 and 6).

**M2. Selection on output (Smaldino and McElreath).** If the loop that keeps or evolves scaffold parts is rewarded for solved count on the fitting set, it selects for lax checks. Fix: reward on held-out pass only. Replication in their model slows the drift but does not stop it, so the held-out set must be fresh each round, not reused.

**M3. Two-committee consistency test.** Run the judge twice on the same candidates with different seeds. Compute d = (items where verdicts differ) / N. Compare with the random baseline for the same accept rate (at 22.7% accept, random is 2p(1-p) = 35.1%). Human committees sit at 23 to 26%. Also compute score correlation. The judge has signal if d is well below random.

**M4. Calibration decomposition (Cortes and Lawrence).** Reviewer score = shared quality part + reviewer-specific part. About 50% of variance is reviewer-specific. With k independent judges the shared part is estimated with variance reduced by k, but only if the judges are independent. G4 says same-model samples are not, so a same-family judge adds less than the formula says (d07 to d09).

**M5. Citation-path dedup (Greenberg).** Build a graph: claim, supporting documents, each document's cited sources. Count independent primary sources, not paths. In Greenberg's case 220,553 paths traced to few data papers. Agent form: for a claim retrieved from several documents, trace each to its primary data source, count distinct primaries and report that number. Flag claims whose support is only review citations.

**M6. Refutation tag in memory.** Store each claim with fields: status (open, held-out-passed, held-out-failed, retracted), source, date. On retrieval, a failed or retracted claim is returned with its status first. Without the tag, the 12% finding (a05) and the retracted-paper finding (d17: best tool 8 of 15) predict stale claims keep being used. No study tests the tag (K27 open).

**M7. Held-out replication step (G3 / S8).** Candidate answer c is fitted on set F. Check c on held-out H (not seen at generation time), a mutated input, or a symmetry. Pass only if c passes on H. Cost: one extra run. The comparison that matters is against spending the same tokens on more samples plus voting. Evidence: an external verifier turns samples into accuracy (SWE-bench Lite 15.9% to 56%, d13); voting and reward models plateau near 100 samples; self-critique without an external signal can lower accuracy (d10). The held-out check is an external signal when it runs code or compares with data. It is not external when it is the model re-reading its own answer.

**M8. Preregistration (registered-report form).** Before running, write the analysis spec: hypothesis, test, exclusion rule. Then run. Log any deviation. Prediction from corollary 3: fewer free choices, lower bias u. Evidence: autonomous analysts show large dispersion (d18) and confirmation personas shift support by 34 to 66 points (d19), but no arm with a preregistered spec was run.

**M9. Prediction market / forecast.** Humans trading on replication picked 83% replicators in the top 12 vs 33% in the bottom 12 (d06). Agent form: P(holds up) from an ensemble, then spend the held-out check budget on items near 0.5 (compare G12). Not tested for LLMs.

**M10. Judge blinding.** From Ye et al. and the self-preference work: judges respond to length, author prestige, injected text and their own style. Blind the judge to authorship and the proposed answer, normalise for length, and let code select (G5).

## 5. What holds up

**Replications of the main claim.** The direction of Ioannidis is supported by every large project: OSC (36% vs 97%), Camerer (62%), Many Labs 2 (54%), economics (61% of 18), preclinical (43%). Effect shrinkage is the robust part: about half in OSC and Camerer, 0.60 to 0.15 in Many Labs 2, 85% smaller in cancer biology, 45% in the market sample. The exact false-paper rate is not established. Counts differ by criterion (Camerer 57 to 67%; OSC 36% to 68% when pooled), so quote the criterion with the number.

**Moderators.**
- Many Labs 2: replicability depended more on the effect than on sample or setting; lab vs online and WEIRD vs non-WEIRD explained little (d05).
- Preclinical: five candidate moderators did not explain failure; animal studies replicated less mainly because their original effects were smaller (b03).
- ML: readability, pseudo-code, stated hyper-parameters and author reply predicted reproduction (b07).
- OSC: strength of the original evidence predicted replication better than team traits (d01).

**Failures and disputes.**
- Gilbert et al. versus OSC: unresolved; each side said the other misread sampling error (d02, d03).
- Earlier errors fixed in this study: OSC 36% is significance and 39% a subjective rating; Camerer effect about 50% not 75%; Many Labs 2 is 15 of 28 at p<.05.
- Not opened: Begley and Ellis, Pier 2018, Gundersen and Kjensmo.
- Cortes and Lawrence print 25.0% in the text; the correct share is 25.9%.
- Judge validity is task dependent: near-human on accept/reject (0.65 vs 0.66) but 53.3% on idea pairs. Low human agreement caps what any judge can show.
- Review consistency metrics are not interchangeable: decision-level disagreement 23 to 26%; score-level r 0.55 to 0.58; top/bottom agreement 56.1 to 71.9%.

**Interventions that worked.**
- Task-specific scaffold: CORE-Bench Easy 35.6% to 60% (c13).
- Forced persistence for one model: IterativeAgent lifted o1 13.2% to 24.4% (c15).
- External verifier with many samples: 15.9% to 56% (d13).
- Compute-optimal allocation: matches best-of-N with about 4 times less compute (d12).
- LLM feedback to reviewers: 26.6% updated; reviews 80 words longer (b11).
- Checklists and code submission raised uptake (b08); no accuracy effect measured here.
- An LLM auditor narrowed the analyst steering gap (d19).

**Interventions that did not work or backfired.**
- Raising a cost limit: GPT-4o 26% to 31% only (c13). A 36-hour limit moved o1 to 26.0% only (c15).
- IterativeAgent hurt Claude 3.5 Sonnet, 21.0% to 16.1% (c15).
- Self-critique without an oracle: GPT-3.5 CommonSenseQA 75.8 to 41.8 (d10).
- Debate at equal responses: no better than voting (d11).
- Showing the paper PDF: non-reproducible accuracy for Claude Code fell 100% to 63.3% (c19).
- A confirmatory prompt: non-reproducible accuracy fell 100% to 70% (Claude), 90% to 60% (Codex) (c20).
- Auditor on analyst transcripts: narrows but does not remove the gap (d19).
- Forced replication share in the evolutionary model: only delays decline (a13).

## 6. Language models

**LLMs as reviewers.**
- Overlap with human comments: GPT-4 30.85% vs human-human 28.58% (Nature family, 3,096 papers); 39.23% vs 35.25% (ICLR, 1,709 papers). Shuffled control 0.43% and 3.91%. Overlap is higher on weak papers (43.80%), which may reflect generic complaints (c01, c03). 308 researchers: 57.4% helpful, 82.4% more useful than at least some human reviewers (c02). Early comments match better than late (c25). Matching used a GPT-4 step, so overlap is not correctness.
- Accept/reject: best configuration (GPT-4o, 5 reflections, 5 ensembled reviews, 1-shot) gets balanced accuracy 0.65 vs human 0.66, but FPR 0.31 vs 0.17. Plain GPT-4o zero-shot 0.61. Raw Sonnet 3.5 0.52, accepts nearly everything (FPR 0.95) (c04). The human baseline came from a different dataset.
- Pairwise accepted vs rejected ICLR: Claude 3.5 Sonnet 71.4%, GPT-4o 61.1%, Claude 3 Opus 63.5% (c07).
- Ideas: Claude 3.5 pairwise ranker 53.3%, below human 56.1% (c06).
- Self-inconsistency: alpha 0.33 to 0.79 on SummaC, 0.27 to 0.56 on MT-Bench; best model identical on all 3 runs for only 61.3% of MT-Bench items; 5 runs did not change it (d15, d16). Do not equate the roughly 39% non-identical items with the 23 to 26% committee figure.
- Bias and attack surface: hidden text moved mean rating 5.34 to 7.99 and agreement with injected text to 90%; title-only papers scored at or above 42% of full papers; longer input and famous authors raised ratings (a23, a24, c09). LLM reviews are 4.5 times more consistent with author-stated limitations than human reviews.
- Self-preference: GPT-4 recognizes its own summaries 73.5%; fine-tuning for self-recognition raises self-preference (d07). GPT-4 self-preference score 0.749 among 8 judges, tied to low perplexity (d08). LLM-written descriptions preferred over human-written, more than humans prefer them, smaller for paper abstracts (d09). The AI Scientist reviewer scores papers its own family wrote (c05).

**LLMs inside real review.**
- 6.5% to 16.9% of review text at 2023-24 conferences was LLM-modified; share higher when confidence low, near the deadline, and for reviewers who rarely answer rebuttals (c10, c11).
- At least 15.8% of ICLR 2024 reviews were AI-assisted; those scored higher in 53.4% of same-paper pairs (p=0.002) and raised acceptance by 4.9 points for borderline papers (p=0.024) (b12).
- A feedback agent at ICLR 2025: 42.3% of reviews received feedback, 26.6% updated (b11).

**LLMs as idea generators and judges.** Ideation: 79 reviewers, novelty human 4.84, AI 5.64, AI plus rerank 5.81; feasibility human 6.61 vs AI 6.34, not significant (b13). Execution: after 43 experts ran the ideas, AI ideas dropped novelty by 1.05, excitement by 1.76 and effectiveness by 1.88 points; human ideas stayed flat (b14). Pre-execution scores overstate quality. This is the clearest AI-side demonstration of why a held-out check matters. Sakana AI Scientist: 5 of 12 experiments (42%) failed, median 5 citations per paper, 57% of manuscripts with figure errors, wrong novelty calls (b18).

**LLMs as replicators.**
- PaperBench (20 ICML 2024 papers, 8,316 tasks): Claude 3.5 Sonnet 21.0%, o1-high 13.2%, DeepSeek-R1 6.0%, Gemini 2.0 Flash 3.2%; humans 41.4% vs o1 26.6% on 3 papers; Code-Dev o1 43.4%; best judge F1 0.83 (c14, c16).
- CORE-Bench (270 tasks, 90 papers): 60.00 / 57.78 / 21.48 for CORE-Agent GPT-4o; AutoGPT GPT-4o 35.56 / 37.78 / 6.67 (critique); mini 44.44 / 32.59 / 16.30 (c12).
- SciReplicate-Bench: 39% best (b17).
- SocSci-Repro-Bench (2026, 221 tasks): Claude Code 93.4% task accuracy, 78.0% paper-level; Codex 62.1%, 35.8%; Python 100%, Stata 94.4%, R 91.9%; memorisation not the driver (93.3 vs 96.2) (c17, c18).
- Read the Paper, Write the Code (48 papers): best system completed 92 to 100% of papers; coefficients inside the original 95% CI over 80% of the time; human audit confirmed 92% of flagged divergences but only 67% of error-source labels (c21, c26).
- ReplicatorBench (19 claims): interpretation score 94.54 (o3) to 82.25 (GPT-4o); outcome classification macro F1 47.86 (GPT-5-mini); agents design and run well but fail at finding new data and at judging replicability (c22).
- Pattern: with code and data supplied, 2026 agents reproduce well. Reproduction from scratch and judging replicability stay weak. Scaffold choice moves results as much as the model (K15).

**What changed behavior, and by how much.**
- Prompt framing: confirmation prompts cut non-reproducible accuracy by 30 points (c20); confirmation personas lift analyst support by 34 to 66 points (d19).
- Scaffold: up to +25 points on CORE-Bench Easy; -5 points for Sonnet under IterativeAgent.
- External verifier: +40 points at 250 samples on SWE-bench Lite (d13).
- Oracle feedback in self-correction: GSM8K 75.9 to 95.5 for GPT-3.5, against no gain without it (d10).
- Retracted literature: best of 9 tools fully correct on 53.3% of 15 papers (d17).

## 7. What our agent should take

Status codes: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Pass only on an unfitted check (G3 stays, reinforced).** Fitting the given examples is a published-but-unreplicated result; a held-out check is the replication. Schema part: G3, S4, S8. [E] Evidence: a01, a03, b01, d01, d04, d05, K01, K02, K07, K09. The principle is supported; the equal-token comparison against extra samples is untested (U1).
2. **Discount first-pass strength before reporting it.** Expect held-out performance below fitted performance. Report the held-out number only. Schema part: G3, S8. [E] Evidence: d01, d04, d05 (effects about half or less), b14 (ideation to execution loss), K13.
3. **Selection by code on a held-out signal, with a blind judge (G5 stays).** Judges favour their own style, length, authority and injected text. Schema part: G5. [E] for the principle: c08, c09, d07 to d09, K11, K21. Do not let a scorer see authorship or a stated answer.
4. **Do not use self-critique or same-family judges as the replication.** Without an external signal it did not help or hurt (GPT-3.5 CommonSenseQA 75.8 to 41.8). Schema part: G2, G9. [E] direction (d10, d11, d13); exact sizes are single-source.
5. **Treat a lone positive from a flexible search as weak.** Log how many candidates were tried before one passed; more tries means a weaker claim. Schema part: S4 harvest and S8. [E] (model plus empirical shrinkage): a02, b01, d05.
6. **Reward held-out truth, not solved count, in any loop that tunes the scaffold.** Schema part: G7. [S] as evidence (a11 to a13) but already implied by G7. Keep as a design rule.
7. **Do not trust a verdict from one run of a judge.** Best model identical on 3 runs for 61.3% of MT-Bench items. Aggregate in code and report disagreement. Schema part: G5, O7 variance note. [S] (d15, d16); costs nothing.
8. **Count independent primary sources, not citing documents.** Schema part: memory, S1 input hygiene. [S] (a08 to a10, K05). Cheap; keep as a rule and test in U8.

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Held-out recheck beats equal-token extra samples plus vote | G3 / S8 / G12 | [C] no study isolates it | d10, d12, d13, K23 |
| Refutation tag in memory stops reuse of failed claims | memory | [S] | a05, d17, K04, K27 |
| "Cannot be verified" abstention under confirmatory prompt | G3 / G9 | [S] | c20, d19, K16 |
| Preregistered spec cuts analytic flexibility | S0 / S4 | [S] | d18, d19, K25 |
| Shrinkage factor on first-pass confidence | G3 / S8 | [S] | d01, d04, K02 |
| Different-family checker vs same-family checker | G5 | [S] | d07 to d09, K21 |
| Ensemble forecast of P(holds up) to route check budget | G12 | [S] human only | d06, K26 |
| Judge self-disagreement rate vs 23-26% | G5 | [S] | d15, d16, K24 |
| Independent-source count in retrieval | S1 | [S] | a08 to a10, K05 |
| Prior-art or novelty check before claiming a result | G8 | [S] | b14, b18, K20 |
| Scaffold per model family | S0 | [S] | c15, K15 |

## 8. Concrete tests on our bench

All arms use equal token budgets (setup counted, G7), the same items and the same seeds. Report held-out accuracy, false-pass rate and tokens.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style items and brain teasers with a hidden held-out example | A: one answer plus held-out check, retry once on fail. B: N samples plus vote. C: self-critique. D: mixed (half tokens each). Split by difficulty tertile | Held-out accuracy; false-pass rate (passes shown examples, fails held-out) | A above B on items with a checkable unfitted part, by at least 3 points; B or D wins on hard items with no foothold (G12) |
| T2 | Items with known prior odds (seed 10% vs 50% first-pass correct) | Confidence on a lone pass vs after one recheck vs raw shrunk by factor | Brier score vs held-out truth | Recheck arm lower Brier; shrunk (0.5 to 0.7) beats raw |
| T3 | Plant a refuted claim in retrieved context | Tag [failed on held-out] vs no tag; plus a decoy "cited by 5 documents" | Rate the claim is still used | Tag cuts reuse by at least 30 points |
| T4 | Mix of solvable and unsolvable items | Neutral vs confirmatory prompt vs neutral with explicit "cannot verify" option | Accuracy on unsolvable items; score on solvable | Confirmatory loses 20 to 30 points as in c20; the option plus held-out check recovers most |
| T5 | Same candidates, judge run 5 times, 100 items | Own-family vs other-family judge; blind vs author-labelled; length-normalised vs not | Self-disagreement; approval gap vs execution truth; FPR | Own-family gap positive; blinding and normalising shrink it |
| T6 | Analysis-style tasks with free choices | Free analysis vs preregistered spec with deviation log, 30 runs per item | Spread of estimates; false positive rate on null data | Preregistered arm lower spread and fewer false positives |
| T7 | Same claim in 5 retrieved documents tracing to 1 vs 5 primary sources | Path counting vs primary-source counting | Confidence calibration; echo treated as independent | Primary-source arm better calibrated |
| T8 | Studies with known replication outcomes (OSC, Camerer, Many Labs 2 lists) | Ensemble of LLM samples gives P(replicates) | AUC; top-12 vs bottom-12 split vs human 83% vs 33% | AUC above 0.6 justifies routing by it; else drop |
| T9 | Plans scored before and after a held-out run | Agent's own pre-run score | Drop from pre-score to post-run score | Replicates b14; if the drop shows, keep G8 |

## 9. What does not transfer, and why

- **Journal incentives and career pressure** (Smaldino and McElreath). The agent has no career. What transfers is the optimisation target: if we tune the scaffold on solved count, the same selection happens. This is a design warning, not an agent mechanism.
- **Citation counts as a fitness signal.** The agent does not cite for status. What transfers is the retrieval-time analogue: repeated mention mistaken for independent evidence.
- **Human sampling error in psychology.** Human replications are noisy through populations and heterogeneity. LLM variance is across seeds and prompts. The shrinkage size (about 50%) must not be used as a number for agent claims; measure it on our bench.
- **Committee disagreement (23 to 26%) as a target.** Human noise comes from different reviewers, expertise and time pressure. A judge's noise is seed, temperature and order. The human number is a reference only (see d15, d16 limits).
- **Prediction markets.** The 83% vs 33% result needs people with money at stake and domain knowledge. An LLM ensemble is correlated (G4) and may not behave like a market. Untested.
- **Field replication rates.** They are population statistics about human fields. They justify the mindset, not a threshold.
- **Author reply (Raff).** Predictive for human reimplementers; the agent has no authors to email.
- **Reviewer prestige and single-blind bias.** Relevant only if the judge sees author names; the schema removes that (G5).
- **Reproduction benchmarks at 93%.** SocSci-Repro-Bench tests rerunning code on given data, not replication on new data. ReplicatorBench shows weakness at finding new data.
- **2023 to 2025 models.** Many LLM numbers (Huang, Lu, Liang, Starace) are from older models. Reasoning models may differ.

## 10. Open questions

1. Does a held-out recheck beat extra samples plus voting at equal tokens? No study isolates it.
2. How much of the OSC dispute (Gilbert et al.) is statistical and how much substantive? Only abstracts were read.
3. Does a refutation tag in memory stop reuse of failed claims in an LLM? Untested.
4. Do LLM judges abstain when the answer cannot be verified? Only indirect support (c20, d19).
5. Can LLM ensembles forecast replication? No study found.
6. How much of the PaperBench and CORE-Bench gap is scaffold and how much model, with 2026 models? Nothing new found.
7. What is human intra-rater consistency, so LLM self-disagreement (alpha 0.27 to 0.79) can be compared with committee disagreement?
8. Does preregistration reduce analytic flexibility in agents (corollary 3)? No arm run.
9. Do LLM authors and reviewers of one family inflate agreement on scientific papers, and by how much? Self-preference is measured on summaries and chat, not on papers.
10. What is the true false-finding rate? Ioannidis is a model; replication projects give lower bounds under specific designs.
11. Does the human shrinkage (about 50%) have an agent analogue, and is it stable across item types?
12. Net effect of LLMs in peer review: feedback helps (b11, c02) while LLM-assisted reviews inflate scores (b12) and can be manipulated (a23). No study measures net accuracy.

## 11. Sources

[V] means the page or PDF text was opened this session. [M] means snippet or memory only.

- [V] Ioannidis (2005) Why most published research findings are false. https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC1182327/
- [V] Open Science Collaboration (2015) Estimating the reproducibility of psychological science (abstract via Europe PMC). https://www.science.org/doi/10.1126/science.aac4716
- [V] Gilbert, King, Pettigrew, Wilson (2016) Comment (abstract only). https://www.science.org/doi/10.1126/science.aad7243
- [V] Anderson et al. (2016) Response to Comment (abstract only). https://www.science.org/doi/10.1126/science.aad9163
- [V] Camerer et al. (2018) Nature and Science replications (abstract). https://www.nature.com/articles/s41562-018-0399-z
- [V] Klein et al. (2018) Many Labs 2 (abstract via Europe PMC). https://osf.io/9654g
- [V] Dreber et al. (2025) Decision market on online experiments. https://pmc.ncbi.nlm.nih.gov/articles/PMC11860227/
- [V] Errington et al. (2021) Preclinical cancer biology replication. https://elifesciences.org/articles/71601
- [V] Serra-Garcia and Gneezy (2021) Nonreplicable publications are cited more. https://pmc.ncbi.nlm.nih.gov/articles/PMC8139580/
- [V] Greenberg (2009) How citation distortions create unfounded authority. https://pmc.ncbi.nlm.nih.gov/articles/PMC2714656/
- [V] Smaldino and McElreath (2016) The natural selection of bad science. https://arxiv.org/abs/1605.09511
- [V] Cortes and Lawrence (2021) Inconsistency in conference peer review. https://arxiv.org/abs/2109.09774
- [V] Beygelzimer et al. (2023) The NeurIPS 2021 consistency experiment. https://arxiv.org/abs/2306.03262
- [M] Pier et al. (2018) Low agreement among reviewers of the same NIH application. https://pmc.ncbi.nlm.nih.gov/articles/PMC5866547/
- [M] Begley and Ellis (2012) Raise standards for preclinical cancer research (number not verified). https://www.nature.com/articles/483531a
- [M] Gundersen and Kjensmo (2018) State of the art: reproducibility in AI. https://ojs.aaai.org/index.php/AAAI/article/view/11503
- [V] Raff (2019) A step toward quantifying independently reproducible ML research. https://arxiv.org/abs/1909.06674
- [V] Pineau et al. (2021) Improving reproducibility in ML research. https://arxiv.org/abs/2003.12206
- [V] Henderson et al. (2018) Deep RL that matters. https://arxiv.org/abs/1709.06560
- [V] Liang et al. (2023/24) Can LLMs provide useful feedback on research papers? https://arxiv.org/abs/2310.01783
- [V] Liang et al. (2024) Monitoring AI-modified content in peer reviews. https://arxiv.org/abs/2403.07183
- [V] Thakkar et al. (2025) Randomized study of LLM feedback at ICLR 2025. https://arxiv.org/abs/2504.09737
- [V] Latona et al. (2024) The AI Review Lottery. https://arxiv.org/abs/2405.02150
- [V] Lu et al. (2024) The AI Scientist (reviewer numbers read; one earlier pass was keyword-only). https://arxiv.org/abs/2408.06292
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto, Yang (2025) The ideation-execution gap. https://arxiv.org/abs/2506.20803
- [V] Ye et al. (2024) Are we there yet? Risks of LLMs in peer review. https://arxiv.org/abs/2412.01708
- [V] Siegel et al. (2024) CORE-Bench. https://arxiv.org/abs/2409.11363
- [V] Starace et al. (2025) PaperBench. https://arxiv.org/abs/2504.01848
- [V] Xiang et al. (2025) SciReplicate-Bench. https://arxiv.org/abs/2504.00255
- [V] Beel, Kan, Baumgart (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297
- [V] Alizadeh et al. (2026) SocSci-Repro-Bench. https://arxiv.org/abs/2606.11447
- [V] Kohler et al. (2026) Read the Paper, Write the Code. https://arxiv.org/abs/2604.21965
- [V] Nguyen et al. (2026) ReplicatorBench. https://arxiv.org/abs/2602.11354
- [V] Panickssery, Bowman, Feng (2024) LLM evaluators recognize and favor their own generations. https://arxiv.org/abs/2404.13076
- [V] Wataoka, Takahashi, Ri (2025) Self-preference bias in LLM-as-a-judge. https://arxiv.org/abs/2410.21819
- [V] Laurito et al. (2025) AI-AI bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC12337326/
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Snell et al. (2024) Scaling test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787
- [V] Haldar and Hockenmaier (2025) Rating roulette. https://arxiv.org/abs/2510.27106
- [V] Performance of AI tools in citing retracted literature (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13134821/
- [V] Many AI analysts, one dataset (PNAS 2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13393493/

Links to parallel subfields (not covered here): Calibration and overconfidence; Social epistemology; Epistemic diversity; Conformity; Reproducibility and methods; Debiasing and cognitive forcing; Scientific discovery systems; Methodologies of discovery.
