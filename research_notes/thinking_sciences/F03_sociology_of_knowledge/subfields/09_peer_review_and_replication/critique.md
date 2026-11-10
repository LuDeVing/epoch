# Critique: F03.09 Peer review and replication (cross-check)

## Numbers re-opened this session (full text)
Confirmed: Cortes and Lawrence (166 papers, 43 disagreements, 22/43 and 22/44, r=0.55, SE 0.065); Beygelzimer 2021 (203/882 = 23.0%, 35.1% random baseline, 22.7% accept, 50.6%, r=0.575); Serra-Garcia and Gneezy (153 fewer cites, N=80; 12%); Greenberg (sevenfold, 777-fold, 636 citations, 220,553 paths); Smaldino and McElreath (power 0.24, R2=0.00097, replication rate 0.08); Errington et al. (85% smaller, 92%, 42/97 = 43%, 17/97 = 18%); PaperBench (21.0%, 41.4% vs 26.6%, 8,316, F1 0.83); CORE-Bench (60.00/57.78/21.48 for CORE-Agent GPT-4o; 44.44/32.59/16.30 mini); Liang et al. (30.85, 28.58, 39.23, 35.25, 43.80); Si et al. (4.84, 5.64, 5.81; 56.1%; overall 4.68/4.85/5.34); Lu et al. (0.65 vs 0.66, human FNR 0.52 FPR 0.17); Ye et al. (5.34 to 7.99; 90%; 12%; "4.5 times" present, split across lines).

## Corrections
1. Cortes and Lawrence: the main text says "25.0%" but 43/166 = 25.9%. The appendix prints 0.259 and Pineau cites 25.9%. Use 25.9% (a14, a15 carry the 25.0% typo from the paper).
2. a21 says novelty p<0.05 for AI vs human. The table gives p<0.01 for AI ideas (b13 is right) and p=0.04 only for the overall score of AI+rerank (4.68 vs 5.34).
3. Si et al. reports reviews (119 human, 109 AI per condition) alongside 49 ideas; "N" is ideas, not reviews.
4. a27 and c12: the 60/57.78/21.48 row is CORE-Agent GPT-4o (the extracted table is misaligned but it reads as CORE-Agent); AutoGPT GPT-4o is 35.56/37.78/6.67. a27 is fine; a28 column labels stay garbled.
5. c03: rejected-paper overlap is 43.80% in the abstract; the 47.09% in another breakdown is not reconciled. Use 43.80%.
6. Greenberg: "four of ten most authoritative papers had data" is from the text; fine.
7. Errington: the median effect size ratio is for positive effects; the 26% completion rate counts 50 of 193 planned experiments.

## Contradictions and tensions
- Judge validity is task dependent: an LLM reviewer reaches human-level accuracy on ICLR accept/reject (0.65) but a pairwise ranker is 53.3% on idea pairs, below human split-half 56.1%. Low human agreement caps what any judge can show.
- Review consistency numbers differ by metric: 23-26% disagreement (decision level), r of 0.55-0.58 (score level), and 56.1-71.9% top/bottom agreement (Si). They are not interchangeable.
- LLM feedback helps (Thakkar, Liang) while LLM-assisted reviews also inflate scores (Latona) and can be manipulated (Ye). No study measures net accuracy gain.
- Scaffold effects differ by model (IterativeAgent helps o1, hurts Claude 3.5 Sonnet).

## Weak spots
- Foundational replication numbers (OSC 2015, Camerer 2018, Begley and Ellis, Many Labs 2, Gundersen) were never opened; they appear only second-hand (b20 to b24, a18). Pier 2018 (a17) not opened. K02 rests on Serra-Garcia's summary of other projects.
- Ioannidis is a model with assumed inputs; no direct measure of the false-paper rate.
- No source on how well replication prediction (markets, surveys) transfers to LLM judges, and no study of an LLM agent checking its own result by held-out rerun against its own prior claim.
- Benchmarks (PaperBench, CORE-Bench) are 2024-25 models; newer results (SocSci-Repro-Bench, ReplicatorBench) are single-lab and recent.
- Several claims are single-source (K03, K04, K05, K08, K10, K11, K16, K19, K20).

## Seen only in snippets or memory
a17, a18, b19 (keyword search only), b20 to b24.

## GAPS
1. Does a held-out recheck (G3) change an LLM agent's accuracy at equal tokens more than spending the same tokens on extra samples or self-critique? No study isolates this.
2. What are the real figures for OSC 2015, Camerer 2018, Many Labs 2 and Begley and Ellis from the primary papers, including heterogeneity and the Gilbert et al. critique?
3. How often do LLMs keep citing retracted or non-replicated claims, and does a refutation tag in memory fix it (extending the 12% finding)?
4. How do LLM judges behave when the answer is unverifiable: do they say "cannot be verified" (cf. the confirmatory-nudging drop from 100% to 70%)?
5. Can prediction markets or forecasting surveys of replication be mimicked by LLM ensembles, and with what accuracy?
6. How much of the PaperBench and CORE-Bench gap is scaffold versus model, tested with recent (2026) models?
7. What is the test-retest consistency of an LLM judge on the same item (self-disagreement rate), compared with the 23-26% human committee figure?
8. Does preregistration or a registered-report style (commit the check before running) reduce an agent's analytic flexibility as Ioannidis corollary 3 predicts?
9. Do LLM authors and LLM reviewers sharing a model family inflate agreement (judge-self-preference), with measured size?

## Gap search results (2026-11-10)
Search budget: WebSearch was exhausted by other agents, arXiv API and Semantic Scholar and OpenAlex returned 429, so sources came from direct arXiv PDFs, Europe PMC and the Nature page. Evidence is in evidence_d.jsonl (d01-d20); claims K02, K11, K12, K16 updated and K21-K27 added.

1. Held-out recheck vs extra samples vs self-critique at equal tokens: STAYED OPEN. No study isolates it. Related evidence: self-critique without an outside signal fails (d10), external verifiers turn samples into accuracy while voting plateaus (d13), and the gain depends on difficulty (d12). Needs our own experiment (K23 agent_test).
2. Primary figures for OSC, Camerer, Many Labs 2: MOSTLY CLOSED. Abstracts opened (d01, d04, d05). Two earlier errors fixed: OSC 36% significant (39% is the subjective rating) and Camerer effect size about 50% of original (not 75%); Many Labs 2 is 15 of 28 at p<.05. Gilbert critique and reply read as abstracts only (d02, d03); Begley and Ellis still unopened (d20, do not cite 6 of 53).
3. Retracted claims and refutation tags: PARTLY CLOSED. Nine AI tools fail on retracted papers (d17, best 8 of 15). No study tests a refutation tag; open.
4. Judges on unverifiable answers: STAYED OPEN. Only indirect support: confirmation-framed prompts shift conclusions 34-66 points (d19) and judge self-inconsistency (d15, d16). No study found on "cannot be verified" abstention.
5. LLM ensembles forecasting replication: STAYED OPEN. Human benchmark found (d06: 83% vs 33%); no LLM study located.
6. PaperBench/CORE-Bench scaffold vs model with 2026 models: STAYED OPEN. Nothing new found.
7. Test-retest of LLM judge: CLOSED for LLMs (d15, d16: alpha 0.27-0.79; 61.3% identical on 3 runs). No human intra-rater figure, so the comparison with 23-26% stays indirect.
8. Preregistration for agents: PARTLY CLOSED. Many AI analysts (d18, d19) shows large analytic dispersion and an auditor helps in part; no preregistration arm tested.
9. Shared model family inflation: PARTLY CLOSED. Self-preference measured for judges and descriptions (d07, d08, d09); no author-reviewer study of scientific papers with a measured size.

Caveats: d02, d03, d04, d05 and d01 rest on abstracts; d11 table was interleaved in extraction.
