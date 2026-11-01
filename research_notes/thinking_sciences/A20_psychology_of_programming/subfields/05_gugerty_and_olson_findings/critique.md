# Critique: Gugerty and Olson findings (A20.05)

## Re-opened sources (this session, pdftotext of arXiv or scratch copies)
Confirmed exactly: Huang 2024 (GSM8K 75.9/75.1/74.7; CSQA 75.8/38.1/41.8; GPT-4 GSM8K 95.5/91.5/89.0; 74.7% unchanged);
Olausson 2024 (human vs GPT-4 feedback 62.21/45.67/14.67/52.60 vs 42.64/19.33/3.67/33.30; heat-map cells 1.05, 0.97);
SWE-agent (51.7% = 1185/2294; 90.5% and 57.2%; linting 18.0 vs 15.0; 12.47% full, 18.00% Lite);
Adnan and Kuhn (llama3.1:8b 72.56 -> 82.82; deepseek-coder-v2 84.1 -> 92.1);
Agentless (32.00%, $0.70); Tyen (2186 traces, 52.87, 11.11%, 92.8%); Ko and Uttl (1.00/1.65/2.00 bugs, experience 2.52/1.20/3.59);
Vessey (15m40s vs 28m03s; 20m24s vs 23m19s; P=0.003).

## Corrections
1. Vessey 73.7% (b04): the chunking classification TOGETHER WITH bug level explained 73.7% of debug time variance, not classification alone. Manager rating explained 36.1%.
2. Vessey's "novices" were defined by chunking seen in the same protocols, so "novices make more errors" is partly circular. Evidence b05 says "incorrect repairs"; the paper says "mistakes/errors", not necessarily new bugs added.
3. Huang CSQA round 2 is 41.8 (c07 omits it). HotpotQA GPT-4: 49, 49, then 43.
4. a26 says Agentless "matched or beat open agents"; the paper says best among open-source, not top overall on Lite.
5. Adnan and Kuhn phi4 decay constant: table 0.60/0.76 vs text 0.591/0.711 (paper inconsistent). The reasoning model started LOWER (59.1 vs 83.5).

## Contradictions and weak spots
- THE CORE PAPER WAS NEVER READ. G&O 1986 numbers (18 experts, 6 novices, 3 programs, 1 bug) are from a snippet only (a06, opened:false). No effect sizes, no bug-addition rate. "Novices add bugs" rests on the abstract word "frequently" plus Vessey.
- Ko and Uttl (n=75): reading strategy did not predict success; experience confounded. Weakens "less reading = better".
- Human-to-LLM mapping is by analogy. No study found testing "less reading, better hypothesis" on an LLM directly.
- Chen Self-Debug and Reflexion gain with tests; Huang and Kamoi find none without outside signal. Consistent once the external signal is named, but few studies hold tokens equal.
- Decay result is HumanEval, small open models, single preprint; fresh start not tested on strong models (Claude hit 100% in two attempts).
- Many sources are preprints on old models (GPT-3.5/4).

## Seen only in snippets or metadata
G&O sample sizes (a06). Katz and Anderson 1987, McCauley 2008, Vessey metadata (a11-a13).

## GAPS
1. What were G&O 1986 sample sizes, times, accuracy and bug-addition counts? (Need the full CHI paper or later journal version.)
2. At equal tokens, does a capped-read-then-hypothesis step beat full read-then-hypothesis for an LLM debugger?
3. What is the regression rate (new failing tests) per edit for LLM agents, and do an edit cap plus keep-best-so-far reduce it?
4. Does a fresh start after 2 failed rounds replicate on 2025-2026 strong and reasoning models and on SWE-bench-level tasks?
5. Does separating diagnosis (stronger model or bigger budget) from repair beat joint repair at equal tokens?
6. Katz and Anderson 1987: do forward vs backward search strategies differ in success, and does it apply to agents?
7. Are there replications of "experts form hypotheses from less code" with eye tracking or modern cohorts (2015-2026)?
8. How does blind-rated hypothesis quality correlate with final fix rate in LLM agent traces?
9. Do current reasoning models still show Huang-style harm from intrinsic self-correction?

## Gap search results (evidence_d.jsonl, d01-d20; claims K19-K26 added)

Search limits: WebSearch quota ran out early; arXiv API, OpenAlex and Semantic Scholar returned 429. Papers were found through arXiv abs pages by known IDs and Crossref. Coverage of 2025-2026 work is therefore partial (d20).

Closed or partly closed:
- Gap 9 (reasoning models and Huang-style harm): PARTLY CLOSED. Self-Correction Bench (d04, d05) shows reasoning models have a small blind spot and "Wait" lifts base models to near reasoning level. But o1-mini still overturned 34.0% of correct Yes/No answers, o1-preview 15.6% (d06). No 2026 models tested. Claims K19, K20.
- Gap 3 (new bugs per edit): PARTLY CLOSED at patch level. 11 of 22 confirmed-incorrect plausible patches were regressive; 7.8% of plausible patches fail full developer tests; 29.6% diverge from gold (d11, d12, d18). Claim K23. Per-edit rate and the effect of an edit cap plus keep-best are still unmeasured.
- Gap 8 (hypothesis quality vs fix rate): PARTLY CLOSED at system level. Localization F1 order matches resolve order across six systems (d10); failure taxonomy points to localization and stalling (d13). Claims K22, K24. No blind-rated per-trace study found.
- Gap 5 (separate diagnosis from repair): PARTLY CLOSED. Expert-Executor rescued 24 of 108 failed tasks (d14) but used the same model and no matched-token control. Claim K25. Still open for stronger-model-diagnosis at equal tokens.
- Gap 4 (fresh start on strong models): STILL OPEN. CodeMonkeys (d08) supports fresh starts over extra iterations at equal cost, indirectly. No replication of the Adnan and Kuhn decay result found.

Still open:
- Gap 1 (G&O 1986 numbers): OPEN. Full text not reachable (d01). Keep the 18/6/3/1 figures marked unverified. A library copy or the Ablex 1986 chapter is needed.
- Gap 2 (capped reading then forced hypothesis, equal tokens): OPEN. CodeMonkeys (d07) shows reading everything is cheap when amortized, which is an argument against a hard reading cap as a cost saver. Claim K21.
- Gap 6 (Katz and Anderson 1987): OPEN. Only DOI confirmed (d03).
- Gap 7 (eye tracking or modern cohorts): OPEN. Two titles seen, none opened (d19).

Status changes: no claim changed status. K06 now has 5 sources with a boundary note (reasoning models). K02 gets an LLM analogue note. K10 gets indirect support. K23 and K22 rest on two sources each but stay "single-source" because the sources test the same benchmark.
