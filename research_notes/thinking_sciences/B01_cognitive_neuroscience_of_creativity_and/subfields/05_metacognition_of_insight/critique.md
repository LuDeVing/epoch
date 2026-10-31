# Critique, B01.05 Metacognition of insight (cross-check)

## Numbers re-opened this session (10 checks)
1. Metcalfe and Wiebe 1987 (a03-a05): FOK insight .08 vs algebra .40, F(1,46)=6.46; predicted/actual .59/.34 and .73/.55; normative gamma .77 vs .60, F(1,46)=10.13; t(18)=2.02 and 1.63. CONFIRMED from the PDF text.
2. Hedne 2016 (a09/b03): accuracy .57 vs .37, t(506.9)=5.78, d=.51; differential warmth 2.92 vs 0.30, t(210)=0.79, d=.12; Az noninsight .64, t(41)=5.43. CONFIRMED.
3. Laukkonen and Tangen 2018 (a12/b06): r=.61 (n=51) per person, r=.08 (n=182) per problem. CONFIRMED. The number of problems with 2+ warmth ratings is 180 in one place and 182 in the correlation text; the paper itself uses both.
4. Danek and Wiley 2017 (a21/b07): Aha 66.50 vs 52.34, t(69)=10.21; 417 of 1124 = 37 percent. CONFIRMED. CORRECTION: the number of magic tricks is inconsistent inside the paper itself (abstract says 37, methods say 35; 2450 trials = 70 x 35). Use 35 and note the discrepancy. Evidence b07 says 37 and should be read as 35.
5. Salvi 2016 (a23): 93.7 vs 78.3 percent, t(37)=5.66, d=.99; last-5-s errors 29.4 vs 4.7. CONFIRMED.
6. d'Aliberti and Ribeiro 2026 (a28/c05): 6.31 percent pooled, about 7.6 percent for Qwen-1.5B, 2.57 vs 16.44 (N=723,200), formal Aha 1.79 percent. CONFIRMED. Note the 6.31/7.6 difference is pooled vs single model, not a conflict.
7. Same paper (a29/c06): 0.3221 to 0.4062, +8.41 pp, 50,574 vs 23,500, crosswords +0.45, Rush Hour +0.01. CONFIRMED (crosswords wins 5,380 vs losses 5,004, near balanced).
8. Mizumoto 2025 (a25/c01): 7.6 vs 17.6 on 120-item subset; human 52.9 (CI 46.6-59.2, n=126); full set 9.42 vs 19.25, OR 2.29 (1.99-2.64). CONFIRMED. The d=.946 in a25 was not found in the text I grepped; treat as UNVERIFIED.
9. Mizumoto verification-failure shares (c02): 30.57 (DeepSeek-R1), 5.23 (Gemini Flash), 25.00 (Opus 4), 39.34 (Grok 4). CONFIRMED in Table 2. Caveat: counted on small numbers of cases (9 to 48), by models that answered only a subset.
10. GPT-5 inside the human CI: CONFIRMED, but the authors warn it is descriptive, not equivalence.

## Contradictions between sources
- Warmth: Metcalfe and Wiebe and Chein 2010 (a15) show the step pattern; Hedne 2016 finds no difference once insight is defined by Aha; Kizilirmak 2018 finds a partial effect (d=.82). Insight defined by problem type vs by solver report gives different answers.
- Accuracy of insight: Salvi 2016 and Hedne find insight more accurate; Metcalfe 1986, Danek and Wiley and the FIAT work show many wrong insights. Resolution partly by task (convergent vs open: McGuinness 2026) and by error type (omission vs commission).
- Webb 2016: insight is solver-dependent, so Metcalfe and Wiebe's problem-based labels are suspect.

## Weak spots
- The founding data are tiny (19 and 39 usable subjects, one-tailed tests, only correct solutions analysed). No large preregistered warmth replication exists.
- Metcalfe 1986 (a07, a08), MacGregor 2001, Ohlsson 1992, Weisberg 1992 were not opened; their numbers come second-hand. Salvi press-release numbers (b09) unverified.
- Evidence a09/b03/b04/c12 are the same Hedne paper counted several times; independent source counts in claims.jsonl treat them as one.
- LLM studies are mostly single-lab, single-benchmark (NazoNazo in Japanese; small models Qwen-1.5B for d'Aliberti). Whether results hold for frontier models is not shown. Stumpers and ChatGPT insight studies (c17, c18) are tiny (n=20 humans; 5 items; r=-.63 on 4 points).
- Snippet-only: b12, b24, b25, c16, c21, c22, c23, a14, a17, a18.
- Evidence a24, b19 (abstract and headings only), b28 (a gap record, not a source).
- No LLM study found that tests human-style warmth ratings by an LLM on insight problems directly; the guardrail rests on analogy (human warmth fails, LLM verbal confidence is weak on hard items).

## GAPS
1. Does an LLM's self-reported progress or warmth, sampled mid-trace, predict eventual success on insight riddles better than token entropy or trace length? (No direct study found; decides the guardrail.)
2. At equal tokens, does a code-triggered reconsideration (entropy gate) beat self-consistency voting on insight-style items for frontier reasoning models, not only Qwen-1.5B?
3. How often do frontier models write the correct answer in the trace and not commit (verification failure), outside Japanese riddles, and does forced candidate check recover it?
4. What is the false-insight rate in LLMs (confident commit to a lure) on FIAT-type items, and does an independent verifier reduce it?
5. Is there a large preregistered replication of Metcalfe and Wiebe warmth with solver-defined insight (N > 200)?
6. Does the Aha-accuracy advantage survive in LLM traces: are answers after a reframe more accurate on convergent items and less accurate on open-ended items?
7. Does confidence in a separate call beat same-call confidence on insight items (Miao and Ungar found corruption on MATH)?
8. Does the spillover of an Aha onto later truth judgments (Laukkonen 2020) have an analog in long agent contexts?
9. Which impasse detector (entropy burst, trace length, action loop, repeated-candidate) has the best AUROC for stuck-vs-progressing at low false-alarm cost?
10. Do metacognitive prompts (Bai 2025) help beyond CoT at equal tokens once sample-and-vote is the baseline?

## Gap search results (evidence_d.jsonl d01-d20, claims K22-K28 added)
Method note: the web search quota ran out after four queries; the rest was done by opening papers found through arXiv listing pages. Absence of a paper below is not proof that none exists.

ANSWERED AS FAR AS THE EVIDENCE ALLOWS (gap 5 closed as none-found; gaps 3 and 8 only in part)
- Gap 5 (large preregistered warmth replication): answered as "none found". Largest related human data are Webb 2016 (about 400 recruited, post-solution feelings, no warmth; d02) and Laukkonen 2022 (about 1250 per sample, spillover, not warmth; d01). Claim K26 marked unresolved; decision unchanged: do not build on warmth.
- Gap 8 (Aha spillover analog in agents): human side sharpened, LLM side still untested. 2022 preregistered replication gives d=.23 and .25 (smaller than the 2020 d=.32), and a 10-second delay removes it (p=.447; d01). K09 downgraded from established to single-source (same lab). Treat as human-only; the agent control is a context reset.
- Gap 3 (verification failure outside Japanese riddles): partly closed. Correct-then-lost answers are measured on math: oracle stop +8 percent accuracy, -72 percent tokens (d10); stop at first correct prefix about +10 percent, up to 21; harmful overthinking .11 multiple choice vs .24 free-form; fixed early stopping makes it worse, 10.1 to 18.4 (d11). New claim K23 established. Forced candidate check was not tested.

PARTLY ANSWERED
- Gap 9 (best impasse detector): no head-to-head. Reported AUROC: uncertainty-slope 0.73-0.81 GSM8K but 0.52-0.80 ProntoQA (d07); instability score 0.66-0.74, 0.605 in the first 50 steps (d08); repetition features 0.80-0.91 on the full trace but 0.51-0.57 before the answer (d06); strong length baselines absorb gains (d09); a snippet warns entropy AUROC is inflated by per-problem direction (d19, unopened). K19 downgraded to contested; K25 added as unresolved. Needs our own bench with trace length as the null.
- Gap 7 (separate-call confidence): Kumaran (d03) shows a later stage reflects commitment (residual correctness AUROC .473), not correctness; Ghosh (d04) and Yang (d05) show verbal confidence is unstable and trajectory-blind. No same-call vs separate-call test on insight items. K17 widened, K27 added (single-source).
- Gap 6 (accuracy after a reframe, convergent vs open): Rahmani (d16) and Caldarella (d11) point to higher risk of drift in free-form; Kim (d15) shows model-chosen doubt has 24.4 percent precision. No test on insight items. Stays open.
- Gap 4 (false-insight rate in LLMs): Riddle Riddle (d14) is the best analog: 84.9 vs 50.7 percent, 90.8 percent of errors over-inventive. No confidence measure and no verifier arm. K22 added; the verifier half stays open.

STILL OPEN (no direct study found)
- Gap 1 (LLM self-reported warmth vs entropy or length): only indirect evidence (d03, d04, d05, d07). Guardrail stands by analogy.
- Gap 2 (entropy-gated reconsideration vs self-consistency at equal tokens, frontier models): none. The nearest results compare gates with other gates (d12) or prefix consensus with SC (d13, up to 60 percent fewer tokens) on math. K28 says the baseline to beat is cheap voting.
- Gap 10 (metacognitive prompts vs sample-and-vote at equal tokens): none. Only d15: a code-injected doubt cue recovers about 15 percent of failed math rollouts, no vote baseline.

Corrections to earlier notes
- Evidence a25's d=.946 stays unverified (see check 8 above).
- d19 and d20 are not sources (snippet and a log). Do not count them as independent evidence; they sit in claims only to mark uncertainty.
