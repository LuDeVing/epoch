# Critique: C04.03 Combinational creativity (cross-check)

## Numbers re-opened (PDF text from arXiv, this session)
Confirmed exactly: Gu et al. 2412.14141 (DR 0.85/0.78, UP 0.83/0.75, KM 0.87/0.77); Si et al. 2409.04109 (novelty 4.84/5.64/5.81, N=49 per condition, best LLM judge 71.4%, human consistency 56.1%); Si et al. 2506.20803 (gaps: novelty -0.010 vs -1.049, excitement 0.078 vs -1.760, effectiveness -0.052 vs -1.879, overall -0.628 vs -1.976); Schapiro et al. 2509.21043 (59.0, 53.4, 43.4, 97.1%, 19.9% = 412/2,070; humans 22.1/32.9/12.8); Lewis and Mitchell 2402.08955 (0.753, 0.488, 0.350, 0.452; 38.59% alternate-rule errors; table labels are shifted by one line in the extracted text but the order Humans, GPT-3, GPT-3.5, GPT-4 fits); Hodel and West 2308.16118 (synthetic alphabet GPT-3 accuracy below 0.1); AnaloBench 2402.12370 (GPT-4 89.1/66.5/60.7 vs human 96.0/72.5/73.3; gaps 6.9 and 28.8); Webb et al. 2212.09196 (OR 1.88, p=.005; OR 0.37, p=.0003; semantic distance OR 3.24, p=.0165, CI 1.24-8.5).

## Corrections
1. b14 (Hope et al. 2017): the B coefficient vs TF-IDF at k=2 is -1.81 (vs random -1.88), not "about -1.9". At k=3 it is -1.94 vs TF-IDF and -2.05 vs random. Pr(good) numbers (0.71/0.28/0.27; 0.56/0.16/0.14) and kappa 0.51 confirmed.
2. c24 (Webb semantic distance): OR=3.24 was confirmed as printed but its direction was flagged as unverified; the sentence in the paper is about a semantic-distance effect on GPT-3 and its CI is wide [1.24, 8.5]. Quote the CI with it.
3. a16 vs c12: a16 gives per-model accuracies, c12 says they were figure-only. The numbers are in Table 2 of the paper; c12 is incomplete, not wrong.
4. The three evidence files overlap heavily (the same 8 papers appear 2-4 times). Evidence count is not source count. Claims below count independent papers.

## Contradictions and tensions
- Gu et al. frame abstraction-level retrieval as the gain; Chan and Schunn field data show distance itself has zero effect and only iteration helps. Different outcomes (similarity to a known idea vs shortlist), so not directly comparable.
- Si 2024 says LLM ideas are more novel; Si 2025 says that advantage disappears after execution. Both are by the same group, so this is one source family.
- Webb (emergent analogy) vs Lewis and Mitchell, Hodel and West (not robust). Contested, not refuted: only the letter-string family was re-tested, and later models were not.
- Lab studies: novelty up with distance, quality mixed (second-hand through Chan and Schunn).

## Weak spots
- Gu et al. (the key work in the brief): baseline lacks the paper's own references; no judge, no ablation, no variance, one backbone, N=87. Treat as a design, not a result.
- No study isolates "distant" from "near" for LLM combination at equal tokens. Scideator is self-report, N=22.
- Schapiro judges are LLMs; humans were a screened online sample with skips scored zero.
- Uzzi 2013 (a21) and Shi and Evans 2023 (a28), and the lab studies (b24, b25, b26) were seen only second-hand. Do not quote their numbers.
- Wikipedia secondary sources (a22-a26) give theory only.
- Several numbers read from flattened tables (b17, b20, c09).
- Not done: Hope et al. replications, Kumar et al. 2409.06185, Wang et al. SciMON per-iteration numbers beyond abstract-level, Krenn AUC.

## GAPS
1. At equal tokens, does retrieving far-domain sources help an LLM agent at all vs near-domain or none, when scored by execution or a held-out check rather than similarity or LLM judgment? (No study found.)
2. Does extracting a shared abstraction first (the Schapiro bottleneck) raise valid combination, and does it beat simply sampling more candidates?
3. What distance (abstraction level) is best? Is there an inverted U for LLMs, as lab work hints for humans? Gu et al. never ablate L1-L4.
4. Do replications of Gu et al. exist, with the baseline given the same references and a blind judge?
5. How large is the Hope et al. purpose/mechanism effect when replicated, and does an LLM-based purpose/mechanism index reproduce it?
6. Does the iteration finding (Chan and Schunn: only iterated far combinations pay) hold for LLM agents, and how many rounds (2-4?) at equal tokens?
7. What does the original Uzzi 2013 paper actually report (top-5% hit rates), and does the atypical-combination result replicate with newer data?
8. How to measure validity of a combination cheaply without an LLM judge (r=0.159 with humans), e.g. via execution or unit tests?
9. Do Webb-style analogy results survive on GPT-4/Claude-class and reasoning models with counterfactual items?
10. How do we prevent homogeneity (19.9% shared concepts, similarity above 0.8) when forcing distant sources: does source forcing raise diversity at equal tokens?

## Gap search results
Method note: the web search quota ran out, and the arXiv, OpenAlex and Semantic Scholar APIs were rate-limited. Papers were reached by known arXiv id and read from PDF text (evidence_d.jsonl, d01-d16). "Open" below means no study found, not that none exists.

- Gap 7 (Uzzi 2013): CLOSED for the original numbers. Read: top-5% hit rate 9.11 per 100 (high conventionality + high tail novelty), 5.82, 5.33, 2.05, background 5 (d01). Replication on newer data: not found, open.
- Gap 9 (Webb-style analogy): PARTLY CLOSED. Counterfactual and robustness tests on GPT-3, 3.5, 4 show sharp drops while humans hold (d02, d03, d05); far narrative analogy is below chance, 39.6% vs 94.1% humans (d04). Claude-class and reasoning models: open.
- Gap 8 (cheap validity without LLM judge): PARTLY CLOSED. Execution/fitness-scored systems exist (d10, d11, d12) and the human execution study shows LLM-judged novelty fades (d14). No study ties execution score to far-vs-near combination.
- Gap 6 (iteration): PARTLY. Nova shows gains from planned iterative retrieval, saturating after about 3 rounds (d06); AlphaEvolve shows evolution beats resampling at equal compute (d11). Neither tests Chan and Schunn's distance-by-iteration interaction, nor equal tokens. 2-4 rounds is a plausible range, not a measured optimum.
- Gap 5 (Hope et al.): PARTLY. A same-group 2022 follow-up with a learned extractor finds 51% useful inspirations vs under 30% for the best baseline (d09). Not independent, and the authors say far-domain matching is unsolved. 2017 numbers re-read (d08). Independent replication: open.
- Gap 10 (diversity): PARTLY. An embedding near-duplicate filter raises score at equal proposal count (d12); LMX shows more parents in the prompt gives more diverse offspring (d10). Source forcing vs diversity: open.
- Gaps 1, 2, 3, 4: OPEN. No far-vs-near, abstraction-first-vs-more-samples, distance-curve, or matched-baseline Gu replication was found. Gu et al. full text re-searched: no ablation, no matched-reference baseline (d16).

Corrections: Hope 2017 k=3 coefficient printed as B=-1.94 (p<.01) in the text; k=2 B=-1.81 is the critique's figure. The file 2310.20384 is Stevenson et al., not Hodel and West.
Net: the 5 open gaps (1-4 and the equal-token part of 6/10) are best answered by our own ablation (none / near / far sources, equal tokens, unit-test score).
