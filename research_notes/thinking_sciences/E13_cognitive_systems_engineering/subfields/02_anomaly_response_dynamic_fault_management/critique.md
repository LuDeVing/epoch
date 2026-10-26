# E13.02 Anomaly response: cross-check critique

Cross-checker pass. Ten sources were re-opened (arXiv PDFs read as text; PubMed records via Europe PMC). 22 claims written to claims.jsonl (K01 to K22).

## Corrections made (checked against the source text)

1. AIOpsLab (arXiv 2501.06706), Table 3 and 4. Overall accuracy confirmed: GPT-4-w-shell 49.15%, GPT-3.5-w-shell 15.25%, ReAct 55.93%, FLASH 59.32% (a15 right). Detection confirmed: FLASH 100%, ReAct 76.92%, GPT-4 69.23%, GPT-3.5 23.07%; classic MKSMC 15.38%. RCA confirmed: ReAct 45.45, GPT-4 40.90, FLASH 36.36, GPT-3.5 9.09.
   - CORRECTION to c01: mitigation is FLASH 54.55%, ReAct 36.36%, GPT-4 27.27%, GPT-3.5 0%. c01 had ReAct and FLASH swapped (b10 had it right).
   - Localization: GPT-4 is best at Acc@1 (61.54%); ReAct is best at Acc@3 (69.23%) but 53.85% at Acc@1. The "14 times in 20 steps" repeat is GPT-3.5-w-shell (confirmed).
2. Huang et al. (2310.01798). Intrinsic self-correction numbers confirmed (GPT-4 GSM8K 95.5, 91.5, 89.0; GPT-3.5 CSQA 75.8 to 38.1 to 41.8).
   - CORRECTION to b15: the oracle-label figures "GPT-3.5 GSM8K 75.9 to 95.5; HotpotQA 26.0 to 49.0" are wrong. 95.5 and 49.0 are GPT-4 standard-prompt scores. Table 2: GPT-3.5 oracle 84.3 / 89.7 / 29.0 (GSM8K / CSQA / HotpotQA); GPT-4 oracle 97.5 / 85.5 / 59.0. c10 had this right.
3. Schwid and O'Donnell (1992), Anesthesiology 76:495, PMID 1550273. 63% fixation errors, 40% anaphylaxis diagnosed, 27% ischemia, 30% ACLS, N=30 confirmed from the abstract.
   - CORRECTION to b05: the authors are Schwid HA and O'Donnell D, not "Howard, Gaba et al." (Howard et al. 1992 is a different paper, on crisis resource management training). Still abstract-only, truncated at 250 words.
4. Koers et al. (2020) JAMA Surg (PMID 31774483): 25 teams, 75 scenarios per arm, omitted steps 33% to 10%, OR 0.63, usability median 8.7. Confirmed. CORRECTION to b27: first author is Koers (Boer is a later author).
5. Arriaga et al. (2013) NEJM: 17 teams, 106 scenarios, 6% vs 23% missed steps, adjusted RR 0.28 (0.18 to 0.42). The "from memory" numbers in b26 are now CONFIRMED. CORRECTION: the PMID in b26 (23574138) is a commentary by Maruthappu and Shalhoub; the trial is PMID 23323901. b26 should be treated as opened (abstract).
6. ITBench (2502.05352). 13.8 / 25.2 / 0% and 94 scenarios confirmed. Difficulty splits (36, 7.73, 5.0 diagnosis; 21, 12.27, 0.0 mitigation) confirmed. 9.52% without traces and 2.86% mitigation confirmed.
   - CONTRADICTION INSIDE THE PAPER: the main text says diagnosis falls from 13.81% with traces; the appendix says 18.10% with traces. Unresolved. Cite 13.81% with a flag.
7. Roy et al. (2403.04123). 39 vs 35%, 28 of 97 solved by all three, hallucination 4 / 12 / 40% (ReAct / CoT / retrieval), 66% / 32% / 18% give-up among wrong answers, Other 12 / 45 / 32%: all confirmed. Note a second figure: among incorrect predictions only, hallucinations are 49% retrieval, 18% CoT, 6% ReAct. Do not mix the two bases.
8. MAST (2503.13657): 1642 traces, kappa 0.88 and 0.77, step repetition 15.7%, FM-1.5 12.4%, FM-2.6 13.2%, +9.4%, +15.6%, group shares 41.8 / 36.9 / 21.3: all confirmed. FM-1.5 is labelled "not recognizing task completion" in this version; a21 and b22 called it "unaware of stop condition". Same item, naming differs by version.
9. RCAgent (2310.16340). 99.38 vs 86.33 pass, 7.93 vs 22.82 invalid, sampling 70.19 / 44.80, SQL tools 65.84 / 70.94 confirmed.
   - CORRECTION to a19: the 33.54% drop with 70.95% invalid is the SQL-tools substitution, not removal of a JSON regeneration step. c14 had this right.
10. Who&When (53.5% agent, 14.2% step, 127 systems), Laban et al. (39% average drop, 200,000+ conversations, 15 to 20% recovery), Reflexion (repeat more than 3 cycles or more than 30 actions; 130 of 134; 22% hallucination plateau), TRAIL (148 traces, best about 11% headline): confirmed from abstract or text.

## Contradictions between sources

- c01 vs b10 on AIOpsLab mitigation (resolved above).
- b15 vs c10 on Huang oracle numbers (resolved above; c10 correct).
- a19 vs c14 on what the RCAgent ablation was (c14 correct).
- ITBench main text vs appendix on GPT-4o diagnosis with traces (13.81 vs 18.10%). Open.
- TRAIL: b24 gives joint 0.183 (GAIA) and 0.050 (SWE) for Gemini-2.5-Pro, and a headline 11%. The headline is an average; these are not in conflict but the "11%" should not be quoted with the split numbers.
- Tension, not error: AgentDebug (b20, LLM locates the root-cause step and gains 24.3 vs 0.3% all-correct) versus Who&When, Tyen and TRAIL (LLM location is poor). Marked contested (K21). Likely reconcilable by task setup (AgentErrorBench has short, structured trajectories) but no source says so.

## Weak spots

- All four founding human studies were never opened: Woods 1994 chapter, Roth, Woods and Pople 1992, NUREG/CR-6208 (only the catalogue page), De Keyser and Woods 1990. The central human claims (three failure patterns: decompensation, working at cross purposes, getting stuck in outdated behaviour; fixation rates) rest on secondary summaries. The three-pattern list is from the project note, not from a read source.
- Nine "opened" records (a01 to a03, a07 to a13) were read through one blog's summaries, not the papers. They are labelled so but counted as opened; treat as secondhand. All claims resting on them are single-source.
- b06 (DeAnda and Gaba 20.5%) is a search snippet. b05's 63% has no per-group breakdown. Only one fixation rate from a primary source exists in the whole folder, and it is 1992, on a PC simulator, N=30, no control.
- Not a single study measures fixation or impasse detection in an LLM directly with a detector. Closest analogues (Laban, Reflexion trigger) are indirect. Reflexion's trigger was not ablated against no trigger in a fault task.
- LLM fault benchmarks are 2024-era models (GPT-3.5, GPT-4, GPT-4o). No 2025-2026 reasoning model is tested on AIOpsLab or ITBench in the files. Absolute numbers will be out of date.
- AIOpsLab cells are small (about 11 to 13 problems per task); one problem is about 8 to 9 points. Differences like ReAct 45.45 vs GPT-4 40.90 on RCA are one problem.
- Automation-bias and cognitive-aid evidence is human and abstract-level (b07 to b09); it argues by analogy only.
- SWE-agent numbers (c19) and AgentBench Table 4 (c17, column-to-task mapping inferred) were not re-opened.
- Status of "established" for K03 rests on Huang (and Kamoi, which reviews the same literature, so only partly independent). Kept at 2 sources.

## Only seen in snippets or catalogue pages

b06 (DeAnda and Gaba), a04, a05, a14, a23, a24, a25, c24, c25, NUREG/CR-6208 (a06), c23 (BiasBuster effect sizes), b21 (AgentDebug ablation numbers).

## GAPS (most decision-relevant first)

1. Does a code-run impasse detector (repeat count, step cap, no-new-evidence counter) beat no detector and beat a model-judged "am I stuck" at equal tokens, on a fault-injection set? No source tests this directly; Reflexion uses the trigger but never ablates it.
2. What are the actual rates and the exact definitions of the three Woods failure patterns (decompensation, working at cross purposes, stuck in outdated behaviour) from the founding human studies (Woods 1994; Roth, Mumaw and Lewis 1994 NUREG/CR-6208 counts per failure type; De Keyser and Woods 1990)? Needed to map each to a distinct detector rule.
3. Does a fresh-context re-derivation (given the evidence, not the old reasoning) break LLM fixation better than same-context reflection? Human evidence is only incident review (Woods 1987 via Woods and Cook); the LLM evidence is indirect (Kamoi, Laban).
4. What is the right switching rate? Fixation versus thematic vagabonding has no measured optimum for humans or LLMs. Is there any study that sweeps trigger frequency?
5. How do current reasoning models (o3, Claude, Gemini 2.5 and later, 2025-2026) score on AIOpsLab and ITBench, and do the detect-to-fix gap and the repeat-failure pattern persist? Any newer benchmark of fault management with step-level logs?
6. Why does AgentDebug's LLM-located root-cause step work while Who&When, Tyen and TRAIL show LLM step location failing? Is it trajectory length, structured taxonomy, or benchmark design? Independent replication of AgentDebug?
7. Is there any measurement of false-alarm rate (detector fires when nothing is wrong) for LLM agents, including the cost of unnecessary interruptions? AIOpsLab has two no-fault problems only.
8. Do replications of Schwid and O'Donnell's 63% fixation rate exist (later anaesthesia simulation work by Gaba, Howard and others), and how much does the rate depend on how "failure to revise" is scored?
9. Does summarising tool output in code (fixed-size record) beat raw dumps at equal tokens in fault tasks? AIOpsLab's raw-telemetry finding is correlational only.
10. Do rules that stop a stall (switch strategy, ask a human for missing information) recover more than they cost? Roy et al.'s Azure case suggests asking helps but the data are qualitative.

## Gap search results

Gap searcher pass. 24 evidence lines in evidence_d.jsonl (d01 to d24; 17 opened, 7 abstract or summary only). claims.jsonl now has 30 claims: K01, K05, K07, K14, K15, K16, K20, K21 revised; K23 to K30 added. Downloads were kept under D:/research_scratch/E13.02/ only.

### Closed or mostly closed

- Gap 5 (current reasoning models): mostly closed. Three 2026 sources: ITBench-AA (Claude Opus 4.7 47%, GPT-5.5 46%, Gemini 3.1 Pro 30%), SREGym (diagnosis 38.1 to 72.6%, new failure types 15.4 to 28.2% end-to-end), Cloud-OpsBench (best JRA 0.76, evidence closure 0.15 to 0.46). The detect-to-fix gap and the outcome-versus-evidence gap persist. The repeat-failure pattern does NOT persist for strong models: Redundant Action Rate is about 0.00 for GPT-5, Claude-Sonnet-4, Gemini-2.5-Pro (Cloud-OpsBench); only weak models loop. AIOpsLab itself was not re-run on reasoning models in any source found. Step-level logs: Cloud-OpsBench (evidence graphs, milestone coverage) is the closest.
- Gap 3 (fresh context vs same-context reflection): partly closed, answer is "fresh alone is weak". FailFast-RestartSmart: cold restart +0.2 to +2.6 points, loses 27.5 to 36.4% of runs that would have passed; fresh start plus carried-over partial work +3.0 to +5.2. Gumaan: clean restart raised repeats from 31% to 80% for 0.5B models under greedy decoding (small models, 24 tasks). No same-token head-to-head of "fresh re-derivation from the evidence list" against "same-context reflection" exists. Yang's context-contamination model was seen only as a summary.
- Gap 6 (AgentDebug vs Who&When): partly closed. AgentDebug's own numbers are weak in absolute terms (step accuracy 45.0% vs 28.0%, kappa 0.55). Who&When shows accuracy falling with log length (5 to 130 steps) to near 0%. Length is the most plausible reconciler but no source tests it, and no independent replication of AgentDebug was found. K21 stays contested.
- Gap 4 (switching rate): partly closed. No optimum exists for humans or LLMs, but two LLM sweeps exist: fixed intervals k = 3, 5, 7 lose to event-driven checks, and a false-positive budget sweep of 5 to 25% shows the trade (recall 30.5 to 68.3%, precision 76.1 to 58.8%; resolve gain peaks at 10% FPR for one model).
- Gap 7 (false-alarm rate): partly closed. FailFast reports precision and wrongly-aborted runs at 5 to 25% FPR; Ambig-SWE reports false-positive and false-negative rates of a model-judged trigger (0.00 to 1.00 by model and prompt). Still no test of a code counter's false-alarm rate in a fault-management task.
- Gap 10 (stall rules that ask a human): partly closed. Ambig-SWE gives up to 74% relative gain from interaction and Sonnet 4 reaches 89% of full-spec performance. This is underspecification, not a stalled fault diagnosis, so it only supports the idea. The Azure case from Roy et al. stays qualitative.
- Gap 2, provenance part: closed. The three patterns come from a conceptual 2011 chapter (Woods and Branlat) and have no measured rates. Fixation has a stated two-part definition (persistence plus available revision cues; Woods and Cook). See K30.

### Still open

- Gap 1 (code-run impasse detector vs none vs model-judged at equal tokens): open. Nearest data: FailFast's step-count-only control caught 19.8% of failing runs at 5% FPR vs 30.5% for the learned monitor (Qwen3.6-27B). The Stuck Monitor study compares against the small model alone, not a same-model recovery. No repeat-action or no-new-evidence counter has been tested.
- Gap 2, counts part: open. NUREG/CR-6208, Woods 1994 and De Keyser and Woods 1990 could not be opened (nrc.gov denied access; OSTI unreachable; DTIC returned an HTML page). Do not cite any per-failure-type rate.
- Gap 8 (replication of the 63%): open. Found DeAnda and Gaba (1990), 20.5% of 132 incidents, which is a different unit (incidents, not people). No later study re-using the Schwid and O'Donnell scoring was found, and the coding rule for "failure to revise" is not visible in the abstracts. A search summary mentioned Rudolph work with 23% and 28% figures; it could not be traced and is not used.
- Gap 9 (code-side summaries at equal tokens): open. SREGym gives a confounded comparison (Stratus used 1.81x fewer tokens than Claude Code with the same model but diagnosed less often).

### New cautions found

- Cloud-OpsBench and SREGym both show agents that get the answer right without closing the evidence. Score the evidence, not only the answer.
- ITBench main text vs appendix contradiction (13.81 vs 18.10%) still unresolved; not re-checked here.
- d13 (Yang 2026), d22, d23, d24 are abstract or summary level. Treat claims resting on them as unconfirmed.
