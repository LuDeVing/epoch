# Critique: Complexity of expert troubleshooting (E08.08)

## Corrections and confirmations (sources re-opened this session)
Ten numbers were re-checked against the arXiv PDFs.
1. AIOpsLab overall accuracy (GPT-4 shell 49.15, GPT-3.5 shell 15.25, ReAct 55.93, FLASH 59.32): confirmed. The PDF table is garbled in text extraction; the row order is as in the evidence. Detection 69.23 / 76.92 and localisation Acc@1 61.54 / 53.85 / 46.15 confirmed. RCA 40.90 for GPT-4 and mitigation 27.27 confirmed.
2. ITBench 13.8% SRE, 25.2% CISO, 0% FinOps: confirmed. GPT-4o diagnosis 36 / 7.73 / 5.0 and mitigation 21 / 12.27 / 0.0 by difficulty: confirmed. 13.81% falling with traces removed: confirmed.
3. MAI-DxO (Nori): physicians 20% at $2,963; o3 78.6% at $7,850; MAI-DxO 81.9% at $4,735 (no budget); 85.5% at $7,184; 79.9% at $2,397: confirmed. Note: 79.9% at $2,397 is a budgeted variant, not the standard setting; evidence b09 lists it without saying so.
4. Olausson: human vs GPT-4 feedback 33.30 -> 52.60 overall, 42.64 -> 62.21, 19.33 -> 45.67, 3.67 -> 14.67: confirmed. The 1.05x and 0.97x values appear in the pass-rate grids; they match.
5. Huang: GPT-3.5 CommonSenseQA 75.8 -> 38.1 -> 41.8; GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; oracle GPT-3.5 GSM8K 75.9 -> 95.5, HotpotQA 26.0 -> 49.0, GPT-4 29.0 -> 59.0: confirmed. Caveat: in the paper the intrinsic table is indexed by number of LLM calls (1, 3, 5), so "round 1/round 2" correspond to 3 and 5 calls.
6. Laban: average drop 39%, aptitude -15%, unreliability +112%: confirmed.
7. Uncertainty of Thoughts: FloDial GPT-4 43.7 -> 67.3 and 7.8 questions confirmed from the text. Correction: the "+38.1%" average is stated as improvement over direct prompting across 5 datasets and 5 LLMs; its relative or absolute reading is not stated clearly, whereas 43.7 -> 67.3 is in absolute points. Claim K13 keeps both.

Not re-opened (taken from the evidence files as written): FaulT-Bench, SREGym, Kim et al. RCA failure analysis, NIKA, RCAgent, Flow-of-Action, DebugBench, the Sabuncu and Daly ASEE papers. Treat their numbers as one-read.

## Contradictions and tensions
- Sabuncu poster says 22 interviews; the ASEE 2026 paper says 18; both say 6 think-aloud. Unexplained (a08 vs a01).
- AIOpsLab: detection is "easiest" in one reading, but a15 says most agents did not solve detection. Only FLASH got 100%; GPT-3.5 got 23%. Both are true; ordering by stage holds only for stronger models.
- AIOpsLab says more than about 5 steps do not help; FLASH is reported as best at the highest limit (20). Not contradictory for one agent but the "plateau" is agent-specific.
- Self-correction: Huang and Kamoi say intrinsic correction fails; MAI-DxO and Flow-of-Action show gains from structured critique and procedure. The reconciling reading is that gains come from external tools, roles with different information, or retrieved procedure, not from re-reading one's own answer. This is inference, not a tested result.
- Nori adds a challenger role and gains; the same paper compares systems that differ in more than that role, so the effect of the challenger alone is not isolated.
- FaulT-Bench: confident wrong tickets barely hurt, while vague tickets hurt a lot. Opposite to a human-anchoring story; this is single-paper.

## Weak spots
- The core human evidence (Sabuncu 2026, Daly 2024) is 9 to 18 interviews, no statistics, no outcome test. Sabuncu's five manifolds are a theory proposal. Nothing shows complexity type predicts success or that the mapped scaffolds help.
- Schaafstal et al. (2000) is known from an abstract only. The "twice as many" figure has no N or times in hand. Jonassen and Hung (2006) and Gugerty (2007) were not read.
- Most LLM evidence is on cloud and network operations. Mechanical, electronic and medical device troubleshooting (the interview domains) has almost no LLM measurements (Hu and Ash 2026 not opened).
- Agent studies mostly vary the model, not the scaffold, so few results speak to scaffold operators at equal tokens.
- Benchmarks use LLM judges in places (SREGym kappa 0.90 vs human; RCAgent G-correctness); judge bias is untested.
- Run-to-run variance is large (ITBench 1/10 to 8/10 on one scenario); many comparisons use 1 to 3 passes.

## Only seen in snippets or secondary summaries
- OpenRCA (c14): search summary only.
- Hu and Ash 2026 (b19, c23): known only from SUBFIELDS note.
- Schaafstal 2000 (a13): Crossref abstract.
- Jonassen and Hung 2006 (a14): secondary notes.
- Gugerty 2007 (b21), Daly b20 duplicate: not read.

## GAPS
1. Does a complexity-type triage at S0 (representation, ambiguity, situational, stakeholder) change the downstream path and improve RCA accuracy at equal tokens on SREGym or AIOpsLab? No study tests it.
2. Which scaffold operator carries the gain in MAI-DxO (hypothesis tracking, challenger, cost checker, ensembling)? Needs an ablation at equal cost.
3. What are the exact N, times and solve rates in Schaafstal et al. (2000) and later Structured Troubleshooting replications, and do they survive outside Dutch radar and air-defence technicians?
4. Do expert-versus-novice differences in order of work (system understanding first vs root-cause first) predict success in larger samples than 2 think-aloud cases? Hu and Ash 2026 and the other four Sabuncu think-aloud sessions may help.
5. How well do LLM agents do on non-IT fault domains (electronics, mechanical, medical device) where Sabuncu's experts work? Any benchmark with measured results?
6. Does a no-fault gate (verify a fault exists before diagnosing) cut over-diagnosis without lowering detection? FaulT-Bench shows the problem; no fix has been measured.
7. Does enforced grounding (quote the raw data before interpreting) reduce hallucinated readings, given that prompt-level warnings did not (Kim et al.)?
8. Can retrieved similar past incidents and SOPs be combined (Flow-of-Action plus Zhang 2024) and does the gain hold on unseen fault families rather than repeated ones?
9. What is the right step and token budget by difficulty level, given the AIOpsLab plateau near 5 steps and ITBench hard-scenario 0% mitigation?
10. How much of the reported agent gain is judge or benchmark artefact? Needs a re-score of a sample by humans across SREGym, RCAgent and TN-AutoRCA.

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d16). Semantic Scholar, OpenAlex and the arXiv export API were rate-limited and the WebSearch budget ran out after one call, so searching was narrow. "Stayed open" below means not found, not proven absent.

1. Complexity-type triage at S0: stayed open. No study found (d16).
2. Which MAI-DxO operator carries the gain: stayed open. The Nori PDF has no role ablation. It has variants (Instant, Question Only, Budgeted, Unconstrained, Ensemble) and one single-versus-batched check (83.9% both; $3,991 vs $5,084). Ensemble gain (85.5% vs 81.9%) may be sampling (d01 to d04). Also corrects b09: 79.9% at $2,397 is a budgeted variant.
3. Schaafstal 2000 numbers: stayed open. Two more repository pages give the same abstract, no N or times; no replication found (d14).
4. Order-of-work in larger samples: stayed open. Hu and Ash (2026) was opened: it is 17 student chat logs, not think-aloud, so it does not test order of work (d11). The other four Sabuncu think-aloud sessions are not public.
5. Non-IT fault domains: partly closed. Hu and Ash gives only qualitative LLM evidence on analog circuits (17 logs; one 99%-confident wrong reading) and a 1-student WIP (d11 to d13). No measured benchmark found (d15).
6. No-fault gate: stayed open (d16).
7. Enforced grounding: stayed open as a fix. Cai et al. (2026) gives a way to measure it (evidence checkpoints, deterministic scoring) but no agent results were read (d09, d10).
8. Combining past incidents with SOPs on unseen families: partly closed. Flow-of-Action measured SOP effect (GPT-4-Turbo 64.01 vs ReAct 35.50; w/o SOP knowledge 15.39 vs 54.06 on GPT-3.5) but on one system, 90 incidents, 9 fault types, with no unseen-family split (d06 to d08).
9. Step and token budget by difficulty: stayed open. Flow-of-Action action-set size had little effect and used a 20-step cap; no difficulty-by-budget curve found.
10. Judge or benchmark artefact: partly closed. Cai et al. avoid an LLM judge for most scoring and argue outcome-only scoring can reward luck, but no human re-score of any agent benchmark was found (d09, d10).

Net: 0 gaps fully closed, 4 partly closed (5, 8, 10 and 7 as a metric), 6 stayed open. Claims K25 to K29 were added; K05, K06, K12, K15, K24 gained evidence links and caveats.
