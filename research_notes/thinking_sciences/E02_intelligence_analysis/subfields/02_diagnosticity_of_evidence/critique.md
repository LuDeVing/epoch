# Cross-check: E02.02 Diagnosticity of evidence

Cross-checker pass over evidence_a/b/c.jsonl (82 lines). 25 claims written to claims.jsonl (K01-K25). PDFs were fetched to D:/research_scratch/E02.02/ and read as text.

## 1. Numbers re-opened (10 sources)

| # | Source (lines) | Result |
|---|---|---|
| 1 | BED-LLM, arXiv 2508.21184 v3, Table 1 (a17, b22, b23, c16, c17) | Confirmed. Animals GPT-4o-mini 44/78/55/88 (Prompt-Only/Split/CoT/BED-LLM), GPT-4o 45/83/62/93, Llama-3.1-8B 8/49/19/63; Things GPT-4o 34/40/49/64; ICL-Beliefs ablation Animals GPT-4o 25. "+37.4 points, never decreased" is in the text. |
| 2 | Batista and Griffiths 2602.14270 (c08, c09) | Confirmed: N=557, 504 gave a hypothesis; 29.5/14.1/11.8/8.4/5.9%; difference 23.6 points. Clarification: the +5.4 and -56.8 are confidence change in points (Round 1 to 3), and p=.009 is a one-sample test for Default GPT. Default GPT vs Rule Confirming is statistically equivalent (TOST). |
| 3 | Uncertainty of Thoughts 2402.03271 (a16, c15) | DX 97.0, MedDG 88.0 and 81.4, troubleshooting 43.7 to 67.3, "38.1%", "46.6%", CoT-SC 33.8, Reflexion 29.9, adapted ToT 12.4 are all in the text. CORRECTION: the paper writes "38.1%" with no "points" and the tables are garbled in extraction. a16 limits says gains are relative; I could not confirm relative vs absolute. 43.7 to 67.3 is 23.6 points absolute, so the 38.1 is not a simple points figure. Treat "38.1%" as unit-ambiguous. |
| 4 | WILT 2410.10998 (b21, c12, c13) | Confirmed. Claude 3.5 Sonnet 14/50, o1-mini 13, o1-preview 12, GPT-4o 9, Llama 405B 8; GPT-4o-mini 6/50 with 27.22 guesses and 9.78 repeats; Flash 8b 0/50. The "Approx. Correct" column is a second measure that sometimes exceeds the accuracy column, so "solved" counts are the first column only. |
| 5 | Ling 2610.18605 (a20) | Confirmed: 33.1 vs 73.5, gap 40.3 [32.6, 48.6], N=181, 58.7/25.3/16.0%, 91.0 and 74.2. CORRECTION and ADDITION: a20 omits that count-matched hindsight is 63.0% (gap 29.8 points; 28.7 at k=6). So about a quarter of the gap is simply fewer facts; about 30 points are about which facts. Also a continuation cohort has N=140, so "N=181" applies to the primary cohort only. |
| 6 | Karvetski and Mandel 2020 (a05, a06, b07) | Confirmed N=227, mean age 40.7, intercept .233, slope .502, 32% and 30%, method F=3.86 p=.05. CORRECTION: the regression is of the ACH consistency score (delta C) on scaled uncertainty terms. "Non-diagnostic" there means evidence linked to non-diagnostic reliability/credibility ratings, not "same consistency for both hypotheses" as a06 says, and not the final probability. a06 should be read that way. |
| 7 | Mandel, Karvetski, Dhami 2018 (b03-b06) | Confirmed: MAE .26 vs .21 (d=.43, p=.14), r(24) -.10 and -.42, sum 1.54 and 1.77, MAE .09 and 61%. CLARIFICATIONS: (a) .68 vs .17 is the MEAN of within-person correlations, d=1.59. (b) The 61% cut is mostly variance reduction: the paper says aggregation gain was "comparable" in random-response data and "should not be attributed to crowd wisdom". b06 reports the 61% without this. (c) Coherentised analysts (.15) were still worse than coherentised random guesses (.21 is the chimp value; .15 is better, p<.001), so analysts retain some skill. |
| 8 | FalsifyBench 2606.04751 v1 (b17, b18, c10, c11) | Confirmed: 41%, 75%, 68%, rho -0.779 p=.003, 66-82%, falsification rates 59.2 and 18.0, rho -0.937. It is v1 only; numbers may change. |
| 9 | Dhami et al. 2024 (a08) | Confirmed: 61.8/39.2/67.3%, chi2(2)=9.43 p=.009, 66.1/19.4/14.5%, 15.42 mean absolute deviation, 91.9% nonadditive. Note the layout that reduced confirmation bias was hypotheses in ROWS, not Heuer's hypotheses-in-columns matrix. |
| 10 | Heuer ch. 4/5 text (a03, a04) | Confirmed: 6 of 29, 0 of 51; nurses study (Smedslund 1963), 18 of 19 saw at least a weak relation, more than half used the A-and-F cell. The "86 subjects, none showed intuitive understanding" figure was not re-checked. |

Not re-checked: D'Addario and Macchi 2012 (b13; the scirp link returned an HTML page I could not parse), and Feeney (b14). Their numbers stay second-hand.

## 2. Other corrections found while reading

- c16 and c17 name the BED-LLM first author "Bickford Smith"; the paper lists Choudhury, Williamson, Golinski, Miao, Bickford Smith, Kirchhof, Zhang, Rainforth. a17 and b22 are right.
- Duplicates: the same paper appears under several ids (BED-LLM a17/b22/b23/c16/c17; Qiu a21/b26/c01-c03; UoT a16/c15; FalsifyBench b17/b18/c10/c11; WILT b21/c12/c13; Lampinen a22/b27; AgentCDM a24/c28; Mandel 2018 b03-b06 and Karvetski 2020 a05-a07/b07-b08). Claims count papers, not lines, in "independent_sources".
- b05 says ACH raised the probability sum "worse with ACH"; the paper gives 1.54 vs 1.77 with both p<.001 against 1 but the ACH-vs-control difference itself is small; I did not verify its test.

## 3. Contradictions between sources

- Pseudodiagnosticity: Doherty (1979) found a strong tilt toward same-hypothesis requests; Feeney reported 43% correct with a rare feature; D'Addario and Macchi found 30-31% and no rarity effect; Crupi et al. 2009 argue the norm is mis-set. No source here settles this (K02 contested).
- ACH: Lehner 2008 (N=24, via the Wilcox and Mandel review) reports less confirmation bias for novices; every later randomised test is null or negative. The review has no pooled estimate.
- Reasoning models and falsification: FalsifyBench and Jhaveri say thinking models test better; WILT (2024) shows o1 models no better than Claude 3.5 Sonnet. Different tasks (semantic vs numeric) and model generations.
- Structure helps or not: hypothesis table +4.4 top-1 (AgentRCA) and counterfactual critique (Investigator) vs CoT failing in Qiu. Different tasks; no single test compares them.

## 4. Weak spots

- Almost all human ACH evidence is hypothetical, two-hypothesis or four-category tasks with stated numbers. No real analytic task, no ground truth beyond the lab.
- Per-study samples are small (50, 39, 24). Wilcox and Mandel give no pooled effect.
- Strongest LLM result (BED-LLM, UoT, Battleship) needs a closed or sampleable hypothesis set and an LLM answerer. Gains shrink with stronger models (Kobalczyk, Battleship GPT-5).
- Only open-weight or 2024-2025 models for belief-updating studies; the newest frontier models are untested there.
- Several 2026 items are single preprints under review (Ling, FalsifyBench, Investigator, AgentRCA, AdaptFuse).
- "Established" for K03, K11, K12, K15 rests on different tasks sharing a theme, not on exact replication.

## 5. Only seen in snippets, or not opened

- Opened:false lines: a12 (Crupi 2009), a13 (Doherty 1979), a14 (Wolf 1988), a26 (Wason 1960 / Klayman and Ha), a27 (Oaksford and Chater; Nelson), a28 (Good; Fischhoff), b15, b16 (Nelson 2005). Nothing from these should be quoted with numbers.
- Second-hand: b11, b12 (via Wilcox and Mandel), b14, a11, c09 sycophancy rates.
- Tables garbled in extraction: a19 (QuestBench), a24/c28 (AgentCDM), c21 (AgentRCA prompt arms), c27 (no numbers).
- c25 (Agarwal): abstract and method only.

## GAPS

1. Does a matrix or rating step on equal-token cost beat a plain model at picking between rival hypotheses when the decisive item is a single evidence item among many? No LLM test of ACH alone exists (only the trained AgentCDM); this is the direct test of S7.
2. Does a code-side information-gain pick (or simply the Split rule) win at equal tokens for hypothesis lists that the model generates itself, on tasks that are not guessing games (analytic cases, diagnosis, ARC-like rule choice)? What does it cost in extra calls?
3. How often does the agent request duplicate, null or same-hypothesis evidence (the Ling 25.3% and 16.0% pattern, pseudodiagnosticity), and does a code block on repeats help?
4. Where exactly does the ~30-point Foresight/hindsight gap come from once fact count is matched: which facts are chosen, or how they are read? Needs the case-level breakdown.
5. Can the model supply usable likelihood ratios per evidence item (numbers for P(E|H)), and are they better than its direct posterior? Calibration of elicited likelihoods vs logit and verbalised confidence (AUROC about 50) is unmeasured on current models.
6. Does a prompt-only negative-test instruction (Think-in-Opposites style) survive at equal tokens on thinking vs non-thinking modes, and does it transfer outside numeric triples?
7. Does a stated user hypothesis in context bias the agent evidence search the way it biases a human (Batista and Griffiths), and does removing it at the search step fix it?
8. How much of the coherentise-and-average gain is real skill vs variance reduction toward the uniform answer, for our agent (random-response control)?
9. Does evidence layout (rows by hypothesis vs by evidence vs prose) change the agent choice, as it does for people?
10. Pseudodiagnosticity and the original Doherty, Kern and Doherty, and Wolf (1988, competing-hypotheses heuristic) data were never opened; the exact choice percentages and training effects are still unknown.

## Gap search results

Gap searcher pass. 19 new evidence lines in evidence_d.jsonl (d01-d19, all opened; Europe PMC records for d15-d17 are abstract-only). claims.jsonl now has 31 claims (K26-K31 added; K02, K03, K12, K13, K18, K19, K22 amended; K12 moved from established to contested). Search limits: the shared WebSearch budget was exhausted, and OpenAlex, Semantic Scholar and arXiv were rate limited (429) for most of the run, so searching used arXiv listing pages and Europe PMC. Some numbers come from figures that were not readable in the PDF text and are marked as such.

| Gap | Status | What was found |
|---|---|---|
| 1 ACH-style matrix vs plain model, decisive item among many | OPEN | No LLM test of an ACH matrix alone was found. Indirect: Ling rescue +38.8 points from one top-ranked fact (d09); WORTH pilot shows suspicion sentences chosen 25 times and exoneration 0 (d14); Split the Labor gives the design pattern but no measurement (d10). The direct test still has to be built (K30 agent_test). |
| 2 Code-side info-gain or Split rule at equal tokens, self-generated hypotheses, non-guessing tasks | PARTLY CLOSED, answer is "not reliably" | Wild Guesses: EIG beats random and positive-test only on compound rules and loses on simple ones (support-mismatch trap) (d04). Prompts to Posteriors: a one-prompt in-context EIG recipe matched BED-LLM on three current reasoning models (d05). No equal-token study on analytic or diagnosis tasks found. K12 downgraded to contested; new K26. |
| 3 Duplicate / null / same-hypothesis requests and a code block | PARTLY CLOSED | Ling gives the rates: 25.3% repeats, 16.0% no match, 58.7% new (d08). Recovery depends on failure type (switch after duplicate 49.7% vs 17.1% stay; reverse after no-match). No intervention test of a hard block. New K27. |
| 4 Source of the ~30-point gap once fact count is matched | CLOSED (single preprint) | Mostly which facts: set swap +26.7, reordering same set +9.3, hindsight reversed -26.0, critical-evidence recall 16.0% at k=3 (d07). Menu vs free-form identical (31.7%), so it is not text matching (d08). K22 rewritten. Caveat: reference facts chosen by an LLM with hindsight. Case-level category breakdown still only in figures. |
| 5 Usable likelihood ratios per item vs direct posterior; calibration | PARTLY CLOSED | Internal likelihoods are directionally right 64-76% of the time but update with slope 0.30-0.48 (d11); elicited probabilities incoherent across chats (>50%) and mostly coherent within one dialogue (d06); reasoning and code close the arithmetic gap on synthetic worlds (d06). Still unmeasured: the quality of model-supplied P(E|H) for real analytic evidence against ground truth, and calibration of elicited likelihoods vs logit confidence on current models. New K28. |
| 6 Prompt-only negative-test instruction, thinking vs non-thinking, outside numeric triples | CLOSED for the stated question | TiO helped all 11 model-mode pairs on Wason; Dual-Goal hurt non-thinking Qwen3-14B and 32B (23% to 13%, 33% to 10%); Blicket transfer positive for thinking, mixed for non-thinking (Qwen3-32B 64% to 56%) (d02, d03). No equal-token control; thinking tokens per turn rose 20-100%. K19 rewritten. |
| 7 Stated hypothesis biasing the agent's evidence search | PARTLY CLOSED | Belief entrenchment shown (Martingale score; prior-conforming prompt worse) (d13); pro-user bias under active engagement vs passive reading (d12). Neither tested the evidence-request step, and no study tested removing the stance as a fix. New K29. |
| 8 Real skill vs variance reduction in coherentise-and-average, for the agent | OPEN | Nothing new on the random-response control for LLMs. The within-dialogue vs cross-chat coherence result (d06) suggests that coherence in code is cheap, but says nothing about the skill component. |
| 9 Evidence layout (rows vs columns vs prose) for the agent | OPEN | No LLM study of hypothesis-table layout was found. Only second-hand statements that models weight evidence by position and are Bayesian only on average over orderings (d19). Practical advice: shuffle and average over evidence orders. |
| 10 Original Doherty, Kern and Doherty, Wolf data | PARTLY CLOSED | Kern and Doherty 1982: 65 senior medical students, 83% chose non-required same-hypothesis information (abstract) (d15). Wolf et al. 1988: n=119 vs 89, p<.001 after a short training (abstract) (d16). Anderson and Doherty 2024: bias persists with no percentages shown (d17). Crupi and Girotto 2014 confirms the norm dispute (d18). Doherty et al. 1979 percentages and the Wolf effect size remain unobtained (paywalled; not opened as full text). K02 and new K31. |

### Corrections and cautions from this pass

- Jhaveri et al. Table 2 was partly garbled in text extraction; only values that were unambiguous or confirmed by Table 3 are quoted. Dual-Goal numbers for small Qwen thinking runs are not quoted.
- d11 (Bayesian Coherence Coefficient) values were taken from a summarised HTML page, not the PDF text. d05 and d12 report results that exist only as figures.
- K12 was marked established on 2024-25 models; the Prompts to Posteriors re-run on current reasoning models is a counter-result, so it is now contested. The paper itself calls the harness a moving target.
- The Jhaveri result that thinking raised success without consistently raising I:C means K18 (reasoning models succeed because they test more outside their hypothesis) is only partly right.

### Still open after this pass

Gaps 1, 8 and 9 (no direct measurement found), the Doherty 1979 numbers, an equal-token comparison on non-guessing tasks, and any intervention test of a repeat-block. Searches should be retried when API limits lift: OpenAlex and Semantic Scholar for ACH and layout studies, and arXiv for LLM ACH, hypothesis-table layout and likelihood-elicitation work.
