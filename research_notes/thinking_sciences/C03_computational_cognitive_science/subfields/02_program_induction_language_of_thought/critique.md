# Critique: C03.02 Program induction, language of thought

## Numbers re-opened this session (PDF text read)
Confirmed: Qiu et al. Table 1 (ACRE 28.0 to 59.0; MiniSCAN 0.0 to 70.0; List Functions 39.6 to 52.4; MiniARC IO 13.8, refinement worse); Wang et al. Hypothesis Search (17/23/30/33%, human-written 45, Icecuber 43, 49 correct hypotheses, 33 of them correct programs); Ellis 2023 (number game R2=0.95, shape concepts R2=.81 with 100 proposals); LILO (+33.14, +20.42, +2.26, +32.20 / -5.83); Li et al. (56.75% vs 60.2% human, 97.8% best human, 9% false positives, 61.9% by later work); DreamCoder (3.7% to 79.6%; CVC4 82.4%; 84.3% with more compute); ARC Prize 2024 (Greenblatt 42%, ARChitects 53.5%, MindsAI 55.5%, o1-preview 18/21, Sonnet 3.5 14/21); Johnson et al. (95 people, 83.8% per task, SD 16.7); Piantadosi 2016 (1,596 people, 108 concepts, 78% vs chance 56%, about 88% variance, exemplar about half); Rule et al. 2024 (392 people, mean 0.521, range 0.042-0.868).

## Corrections and clarifications
- Qiu: b14 gave ACRE refinement as 45-48 and MiniSCAN 46.0. Those are the T=1 and T=3,N=1 cells. The best cells are 59.0 and 70.0 (T=3, N=5), as in c05/a22. Not an error, but quote the cell.
- Ellis 2023: R2=.81 is the shape-concept task; the number game is R2=0.95. Do not mix them (b18 abbreviates).
- b07 says Goodman 2008 was "not opened"; a07/a08 did open it. Treat b07 as stale and a07/a08 as the record.
- Li et al. Table: the PDF text layout is garbled for the ARC-Potpourri rows (56.75 sits beside a transduction row). The 56.75% ensemble figure is stated in prose and is right; the per-row mapping of the table was not rechecked.
- Independence: a, b and c re-read the same ~10 papers (Hypothesis Search, Qiu, LILO, Li, DreamCoder, Ellis 2023, Piantadosi 2012/2016). Duplicated ids are not independent sources. Claims count papers, not lines.

## Contradictions and tensions
- Hypothesis Search says the language step matters only when code is hard; Qiu finds refinement helps on three of four sets but hurts MiniARC. Both agree on a task-dependent benefit; neither tests why.
- Library learning: DreamCoder/LILO show big gains in closed domains; Berlot-Attwell finds near-zero reuse in LLM prover/code systems. Not reconciled (different domains, different measure of "gain").
- Induction vs transduction: induction wins on exact, compositional tasks; transduction on fuzzy perceptual tasks (Li). So "concepts as programs" is not universal even on ARC.
- Number-word bootstrapping (Piantadosi 2012) is a model with a free parameter; alternative accounts stand.

## Weak spots
- Almost no study here uses a modern frontier model: GPT-4, text-davinci-003, Codex, GPT-4o. Results for 2025-2026 reasoning models are missing. ARC Prize 2024 baselines (o1-preview, Sonnet 3.5) are the newest.
- Token cost is rarely reported. Equal-token comparisons (our rule) are mostly unavailable: Hypothesis Search uses 8 programs times 3 rounds per hypothesis.
- Subsets are small (100 ARC tasks; 50-task human comparisons).
- Human-model links (Goodman 2008, Piantadosi 2016) fit labelled shape/Boolean sets, far from open-ended reasoning.

## Seen only in snippets / not opened
Feldman 2000, Lafond et al. 2007 (b08, b09), Fodor 1975, Carey 2009 and Wynn (a30, a31, secondhand), Shepard-Hovland-Jenkins 1961, Bruner et al. Piantadosi & Jacobs 2016 review, Chain of Code, HtT, Lee 2025, Xu 2024, Mirchandani 2023, Kumar 2023 and ConceptARC numbers were taken from the evidence files, not re-opened.

## GAPS
1. At equal tokens, does propose-K-hypotheses plus execution check beat plain extended reasoning on a current frontier model (2025-2026) for ARC-style and list-function items? Which K is best?
2. Where is the knee of accuracy vs number of proposals when the cost of verification is included, and is diversity prompting (Lee 2025) worth its cost?
3. How often does a passing-on-examples hypothesis fail on held-out cases for modern models, and what cheap held-out check cuts the 9% false accepts?
4. Do any 2025-2026 studies test reasoning models (o-series, Claude, Gemini thinking) on ARC-AGI-1/2 with program induction vs direct output, with measured tokens?
5. Does a library or memory of named abstractions help an LLM agent on a later batch (reuse rate), given the conflicting LILO vs Berlot-Attwell results?
6. Can the "one rule at a time" finding (Goodman 2008, Piantadosi 2016) be used to improve sampling vs blending in an LLM, and is there any LLM study of it?
7. Why does refinement hurt on MiniARC and perceptual tasks, and can a router choose induction vs transduction per item from cheap signals?
8. Are LM-induced rules faithful to the answers they give (raw vs task accuracy gap in Qiu), and does executing rules in code remove it?
9. What did the primary Feldman (2000) and Lafond (2007) papers actually measure, and does shortest-formula length predict LLM difficulty?
10. Does an object-structured input (S2 representation) give gains on strong modern models, or do these only help weak text-grid readers?

## Gap search results (evidence_d.jsonl d01-d18, claims K21-K28)
Web search quota ran out early; sources were opened through arXiv PDFs (pdftotext), a PubMed abstract, and the fetch tool (Greenblatt blog and ARC Prize blog came back summarised, so their numbers are as relayed). Scratch PDFs were kept on D: only.

1. Equal-token comparison on a frontier model: STAYS OPEN. Same-harness propose-and-run numbers exist (ArcMemo: o4-mini 55.17, Claude Sonnet 4 thinking-16k 54.17, ARC-AGI-1 100-puzzle val, 2 attempts) and direct-grid leaderboard numbers exist (o3-high 60.8% at $0.50, Sonnet 4 thinking 40%), but they are different sets, harnesses and no token counts. No paper compares them at equal tokens. Best K unknown.
2. Knee and diversity: PARTLY CLOSED. No sharp knee up to K=256 (Lee 2025, GPT-4o-mini: 36.1 at K=4 to 55.0 at K=256, +0.6 from 128 to 256); Greenblatt about +3 per doubling to 2048. Diversity prompting gains +3.6 to +4.5 at K=4-16, +0.3 at K=128. Verification cost and concept-stage tokens are not reported; no reasoning-model test.
3. Held-out failures: PARTLY CLOSED. 9% (Li) confirmed in prose, for fine-tuned 8B models; majority vote over passing programs fixes about half of affected problems. No 2025-26 number. Holding out a demonstration was not tested by anyone found.
4. Reasoning models on ARC-AGI with program induction vs direct: PARTLY CLOSED. Survey and leaderboard give scores and cost (token counts only for o3: 5.7B vs 33.5M tokens per 100 tasks). ArcMemo/SOAR give program-synthesis numbers for o4-mini, Sonnet 4, o3-mini. No paired induction-vs-direct study with tokens.
5. Library/memory reuse: PARTLY CLOSED. Conflict explained as different reuse definitions: literal reuse near zero (1 reuse in LEGO-Prover logs; 3 in 3,201 TroVE questions) vs ArcMemo concept hints giving +4.2 points official that shrink with compute and do not cut tokens. Pang library cut calls 36 to 10 on same-distribution tasks, second-hand.
6. One-rule-at-a-time in LLMs: OPEN. No LLM study found (search quota limited). Nearest: commit to passing programs and vote.
7. Refinement hurting MiniARC; router: PARTLY CLOSED. Qiu's explanation (pattern-matching items, weak grid reading) is a guess. A free router exists (induction first, transduction fallback; stable per-problem complementarity across seeds, Li). Not tested as a router on frontier models.
8. Faithfulness (raw vs task gap): CLOSED for the mechanism. Code execution removes LM-as-interpreter failure (MiniSCAN task 0.0 with LM interpreter vs 46.0 to 70.0 with symbolic); remaining ACRE gap (78.2 raw vs 45.0 task) is a wrong rule plus strict metric, not unfaithfulness.
9. Feldman and Lafond: HALF CLOSED. Feldman 2000 abstract confirmed (41 types, 6 families, difficulty proportional to shortest-formula length; N and r not read, full text paywalled). Lafond 2007 not retrievable. No LLM-difficulty vs formula-length study found.
10. Object input on strong models: OPEN. Only GPT-4-era (13/50 to 23/50). Survey's 20-30 point multi-representation advantage is uncontrolled.

Caveats: ArcMemo, SOAR and Lee tables were partly garbled by text extraction; numbers quoted match prose or consistent rows. Greenblatt and ARC Prize pages were read via a summarising fetch tool. d02, d03, d18 all come from one survey (second-hand).
