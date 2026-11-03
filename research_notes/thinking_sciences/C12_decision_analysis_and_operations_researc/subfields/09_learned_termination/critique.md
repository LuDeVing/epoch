# C12.09 Learned termination: cross-check critique

Checked 2026-11-03 against the CaRT PDF text (arXiv 2510.08517, re-downloaded and read) and arXiv abstract pages for nine other papers.

## Corrections made

1. CaRT training-set size. Evidence a04 says 1,233 diagnosis problems; b01 says 1,133. Both are right but mean different things. Section 5.2 says 1,233 problems; the appendix says that after filtering the final sets are 1,133 train, 121 in-distribution holdout, 93 out-of-distribution. The main text says the test sets are 100 in-distribution and 200 dermatology. So the test sets actually used after filtering may be 121 and 93, not 100 and 200. Use "1,233 before filtering, 1,133 after" and flag the test-set mismatch inside the paper itself.
2. CaRT Table 1 (102 held-out counterfactual conversations, 70/30 probe split). Confirmed from the PDF. Base: direct 0.567, probe test 0.581 (CI 0.408-0.736). CaRT minus reasoning: direct 0.849, probe test 0.645 (0.469-0.789). Full CaRT: direct 0.663, probe test 0.774 (0.602-0.886). Probe train accuracy 1.000, 1.000 and 0.986. So reasoning raises probe accuracy but LOWERS direct accuracy versus CaRT minus reasoning. The paper says SFT+CF has the highest direct accuracy. Evidence a08 ("reasoning-trained CaRT separates better") is true only for the probe, not direct classification. The probe test set is about 31 conversations, so the probe CIs overlap heavily; the "reasoning gives more generalizable representations" claim is weak.
3. Other numbers confirmed from abstracts: Adaptive-Consistency up to 7.9x and under 0.1% drop; ESC percentages (MATH -33.8, GSM8K -80.1, StrategyQA -76.8, CSQA -78.5, Coin Flip -84.2, Last Letters -67.4); DeepConf 99.9% and 84.7%; probing paper 24% tokens; Hassid 34.5% and 40% and 33%; DEER 19.1-80.1% length and +0.3 to +5.0 accuracy; Answer Convergence 60% and over 40% on NQ; AdaptThink 53% and 2.4%. Chen et al. abstract confirmed, but the 92% and 1,953% figures were not re-checked (in the paper body).
4. Evidence a18 says Hassid beats random by up to 18.8%; the abstract only gives 34.5% vs longest. The 18.8% is not verified.
5. Three files reuse the same sources (a15/b08/c13, a16/b06/c14, a13/b10/c11, a12/b12/c06, a14/b14/c12). Their agreement is NOT independent evidence. In claims I counted independent_sources by distinct papers, not by evidence lines.

## Contradictions and tensions

- Early-exit papers pull in two directions: "answers converge early, stop sooner" (Chen, Liu and Wang, DEER) versus "models stop too early on hard problems" (Wang underthinking). Both can hold if difficulty drives it. No paper tests one stop rule on both easy and hard items.
- Path-deviation paper (2026) argues answer-confidence exit over-truncates, against DEER. It compares mainly with DEER and vanilla; no independent head-to-head.
- Shorter-is-better (Hassid) conflicts in spirit with s1 budget forcing ("Wait" extension helps, 50 to 57 on AIME24). Boundary: s1 extends a model that stopped too soon; Hassid compares samples within one question.
- Liu and Wang's own taxonomy says most learned stops are late (63.6% late, 18.2% perfect). So even a learned stopper is not close to optimal.

## Weak spots

- CaRT is one paper, one group, small models (3B, 1.7B), a GPT-4o-simulated patient, and labels from a success-rate oracle that needs many rollouts. Main results are in figures only; no tabled means. No replication found by any of three searchers.
- Stop quality is judged against a fixed question-asking policy; question quality and stopping are not co-optimised (authors' own limit).
- Oracle labels rely on one external diagnostic model (Llama-3.1-8B); low absolute success (about 0.24-0.37).
- Token-saving numbers in most early-exit papers are on math with open reasoning models. Little on agentic or open-ended tasks, and nothing on closed API models without hidden-state access.
- False-stop rate is almost never reported; savings are reported against accuracy only on average.
- No paper in this set measures LLM stopping against human optimal-stopping tasks (secretary problem and similar); that gap is real, not only a search miss.

## Seen only in snippets or abstracts

c05, c13, c14, c16, c17, c18, c19, c20, c21, c22, c25 (BLADE: search snippet only), a09/c23 (classical theory, from memory). Claims K15 and K18 rest on these.

## GAPS

1. Does a CaRT-style stop judge hold up when trained and tested on a different base model and a different domain (code, planning, tool use), and does it beat a fixed budget at equal mean tokens? (Only one paper; no replication.)
2. What is the false-stop rate (stopped, but more thinking would have fixed the answer) of confidence, probe and prompted-judge stop rules, split by problem difficulty?
3. Can a text-only stop judge on a closed API model (no hidden states) match probe-based stopping? What does a prompted sufficiency check cost and gain?
4. How much of CaRT's gain comes from counterfactual hard negatives alone, and can we build them cheaply without a success-rate oracle (for example from the agent's own answer-change history)?
5. Do stop rules and question selection need to be learned jointly (the authors' own claim)? Any evidence beyond UoT and MediQ?
6. How do stop rules interact with multi-trace voting (DeepConf, ESC, short-m@k): is stopping a trace, stopping the vote, or both the right unit at equal tokens?
7. What does an LLM do on classic human optimal-stopping tasks (secretary problem, sampling cost), and how does it compare with measured human thresholds?
8. Does RL on the stop decision ever work? CaRT's RL variant drifted long; do other reward designs (token-cost-discounted) avoid this?
9. Is the OOD collapse of base and SFT models below a fixed-count baseline a general property of learned stoppers, or specific to the dermatology shift?
10. Does the stop point from "answer stabilises" match the stop point from "information sufficient" in interactive tasks, or do they disagree (the two framings in this folder)?

## Gap search results

Evidence in evidence_d.jsonl (d01-d19). Claims K03, K07, K08, K11, K16, K17, K18 updated; K19-K24 added. Search tools were limited (WebSearch budget ran out; arXiv and Semantic Scholar APIs refused or rate-limited), so many items are abstract-level and are marked in the evidence limits.

1. Closed? Partly. No CaRT replication. Independent stop-learners exist in other domains (ESTAR on medical QA and math with transfer to GPQA; Hammar et al. on code, abstract only), but none is a CaRT-style counterfactual judge, and none compares to a fixed budget at equal mean tokens except Pandora's Box (d10, preference rewards). Still open.
2. Partly. Premature-stop 0.083-0.092 and sufficient-but-wrong 13.2-22.7% (d06); a threshold-sweep proxy (d05); Qwen3-8B answers before real evidence on 55% when a source recovers (d02). Nothing is split by problem difficulty. Open on the split.
3. Mostly closed. Text-only rules work on closed API models (d01, Haiku 4.5 and Sonnet 5), and embedding convergence beats a per-round judge on cost (d07). Prompted judges are inflated and need screening (d16). The judge-vs-probe head-to-head is still missing.
4. Open. CaRT needs a success-rate oracle (d19); no paper builds counterfactuals from answer-change history.
5. Open. Joint learning is future work in CaRT (d19); no new evidence found.
6. Partly. Pandora's Box and BEACON give equal-compute stop rules for sampling (d09, d10); PeerConf and MARS claim stacking but were not opened (d11). No strict equal-token trace-vs-vote comparison.
7. Open, with a negative result: no LLM-vs-human optimal-stopping study found (d15). Only arXiv search and web search covered; behavioural venues not checked.
8. Mostly closed. Other reward designs worked in math (S-GRPO, JET, ESTAR; d03-d05). All were math-first and abstract-heavy; failures at steep length penalties (d03).
9. Partly. ESTAR transferred to GPQA with 98.9-100% accuracy retained (d05); feature-based decider transferred with calibration (d17). So the collapse is not general, but it is untested for base and SFT models in those papers.
10. Open. Stability stop (d18) and sufficiency stop (d03, d05, d19) are used separately; no paper counts disagreements.

New cautions: ids from web-search summaries can be wrong (d14); PeerConf and MARS numbers are second-hand (d11); a 5-in-a-row stop rule is hand-set, not learned (d01).
