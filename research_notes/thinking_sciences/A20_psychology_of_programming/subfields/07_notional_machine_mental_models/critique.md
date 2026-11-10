# Critique: A20.07 Notional machine, mental models (cross-check)

## Numbers re-opened this session (PDF text)
Confirmed: CRUXEval (GPT-4 67/63 direct; 74.8/81.9 CoT; 0/10 on 54 output and 65 input tasks; 22 on both). Nye 2021 (11% to 26.5% few-shot, 20% to 41.5% fine-tuned; 8.8 to 20.1 and 31.8 to 50.7 polynomial; 26.6% and 24.6% on CodeNet+single-line). NExT (+26.1, +14.3; CoT -7.8; trace removal -4.8 and -4.3; about 30% rationale quality). REval (44.4 avg, IC 10.3; GPT-4-Turbo 75.0 and 42.5; EPP 10.8 to 21.4 with CoT; output -6.8). CodeMind (14.76, 11.35, 9.26; +5.36, 9.78, 0.94; 45.00% and 39.58%). La Malfa (GPT-4 skips the trace in more than 95% of cases). Chain of Code (84%, +12 over CoT). Self-Debug Table 3 MBPP (61.4, 57.6, 64.4, 66.2).

## Corrections
1. a18 labels the polynomial figures (8.8/20.1/31.8/50.7) "tracing table". In Nye 2021 they are polynomial evaluation. The b06 label is correct.
2. Nye 26.5% few-shot scratchpad carries an asterisk (modified scoring criterion). Treat the few-shot gain as softer than the fine-tuned one.
3. CodeMind text says "14.76%" etc.; a22, b10 and c09 call these "points". Unit is ambiguous in the paper; kept as relative gains over GPT-4 in IER.
4. Self-Debug: the model-written trace beats explanation by only 1.8 points on MBPP (66.2 vs 64.4), and with unit tests the same row is 69.2 vs 68.2 for one dataset. Do not read c18 as a strong trace effect.
5. REval row labels in the PDF text are scrambled by layout; the 44.4/10.3 average and the GPT-4-Turbo 75.0/42.5 are confirmed by text and abstract, the per-model assignment of 55.7 (GPT-3.5) and 51.0 (best open) is confirmed by prose.
6. CRUXEval confusion counts (159 lost, 340 gained) for GPT-3.5 output: numbers are in the figure, but row/column direction could not be fully resolved from text extraction. Direction is consistent with the prose that CoT helped GPT-3.5 on output.

## Contradictions between sources
- CoT on execution: helps GPT-4 on CRUXEval (+19 output) but hurts untuned code models on repair (NExT -7.8) and cut EPP-unrelated output prediction by 6.8 in REval. Resolution: it depends on model strength and task (output prediction vs repair).
- Trace-based debugging: NExT, Chen Self-Debug and Zhong all say traces help only some models; Haque 2025 says GPT-4 yes, GPT-3.5 no. Consistent, but all rely on model-written or short traces, so real-execution-trace evidence is mostly from trained models.
- CodeMind says repair is uncorrelated with reasoning except at the frontier; NExT says trace training helps repair. Different setups (prompting vs training).
- Human side: Ma 2008 found visualisation alone failed for execution flow; Nelson 2017 found a tutorial built around the machine worked. Different learners, N tiny in both.

## Weak spots
- Almost all human intervention studies have small N (18, 24, 60, 18+19) and no replications. No failed replication of the notional-machine teaching claim was found; also none of a successful independent replication.
- The Dehnadi and Bornat result was retracted; a17 (Caspersen) was only a search snippet.
- The origin papers (du Boulay 1981, 1986; Sorva 2013) were not opened; definitions come through Fincher 2020.
- LLM studies measure output prediction; very few test whether an explicit notional-machine description (rules of the machine in the prompt) helps a model, which is the real question for S2.
- Many 2026 numbers come from versions (v6) that change over time and from model names we cannot independently check (Spiess GPT-5.2, Yeltekin 2026 model list, STEPWISE-CODEX, LongReasonArena); these were read but not cross-opened.
- Only snippet-level: a17, a01, b26, b27, b28, c23.

## Not re-opened (single reading)
Lister 2004 doodle percentages, Xie 2018 effect size, Crichton 2021, Spiess 2026, Yang 2025, Markosyan 2025, Abdollahi 2025.

## GAPS
1. Does giving the agent an explicit written rule sheet for the language's semantics (a notional machine in the prompt) raise trace and output accuracy on edge-case programs at equal tokens, versus plain CoT?
2. Does feeding a real execution trace (from running the code) into the revision slot beat feeding only the error message, for untuned frontier models, at equal tokens?
3. At what model strength does a model-written trace stop being worse than answering directly (the CoT crossover), and can a cheap pilot detect it per task?
4. Does a structured per-line state table beat free-form tracing for LLMs the way a synchronized trace beat doodles for students (77% vs 50 to 70%)?
5. Does the human finding that cognitive conflict (prediction vs real output) repairs wrong models transfer to an agent: does showing its own wrong prediction next to the true output reduce repeat errors?
6. How large are LLM errors on reference, aliasing and mutation semantics (the human weak point, only 17% viable) compared with simple value assignment?
7. Is there any independent replication of notional-machine teaching effects (PLTutor, Ma 2008) with N above 100?
8. Do perturbation-robustness results (Spiess, Yang) hold for the agent's own scaffolded tracing, i.e. does S2 trace plus mutated-input check catch lucky correct answers?
9. How much of the tracing gain is cost: what is the token price of a full state-table trace versus running code, and when is code-run strictly better?
10. Does a misconception checker (McMining-style) improve or harm the agent's own trace review, given a 27% fabrication rate on correct input?

## Gap search results

Evidence added in evidence_d.jsonl (d01 to d16). Search APIs (Semantic Scholar, OpenAlex, arXiv export) and WebSearch were rate-limited or out of budget; sources were found by known id, Crossref and arXiv PDFs and opened as full text. Gaps below are marked closed, partly closed, or open.

1. Rule sheet in the prompt vs plain CoT: OPEN. Nearest data: one sentence about exceptions took GPT-5.2 from 15% to 81% on exception cases but cost about 5 points on normal cases (Spiess, d13). No test of a full semantics sheet at equal tokens. New claim K25.
2. Real trace vs error message only: PARTLY CLOSED. DebugRepair ablation (d05): symptoms only lost 26.3% of correct fixes (224 to 165), GPT-3.5, Java. CRITIC (d07) and Huang (d06) agree that real tool output helps and self-review does not. No equal-token test on untuned frontier models. K13 updated, K26 added.
3. CoT crossover and a cheap detector: PARTLY CLOSED. Direction is clear (Sprague d01; Olausson d03, d16: only GPT-4 gained from revision on APPS). No paper tests a per-task pilot detector. K28 added (single-source).
4. Structured table vs free-form: OPEN for prompted models. Only fine-tuned comparison: compact diff trace 77.4% vs full state dump 64.5% on nested-loop MBPP, equal on CRUXEval (Markosyan d08). No free-form arm.
5. Cognitive conflict transfer to an agent: PARTLY CLOSED on the mechanism. The outside signal (true result) is what works; the model's own judgement does not (Huang d06: GPT-4 GSM8K 95.5 to 89.0). No study shows a repeat-error reduction from prediction-next-to-truth specifically. K26.
6. Alias, reference, mutation errors: OPEN. Taxonomy of reasoning-model trace errors (Abdollahi d10) has no such category; computation errors dominate. Absence of evidence only. K29 added with status open.
7. Independent replication N above 100: OPEN, with a null instead. One independent tutor study (N=48, Carleton thesis, abstract only, d14) found no benefit from explicit notional machine. K05 changed to contested.
8. Perturbation robustness for the scaffold: OPEN for scaffolds. Cross-opened Spiess (d12): GPT-5.2 99.24% to about 76.4% under renaming and transformation; Gemini 3 Pro barely moves. Tested only for plain prompting. Abdollahi (d10) shows edge inputs raise error counts.
9. Token cost, trace vs code-run: PARTLY CLOSED. Sprague d02 and Abdollahi d11 (439 to 181 computation errors, 58.8%) support code-run for execution steps; trace length grows with executed lines (d09). No head-to-head token table. K27 added.
10. Misconception checker on own traces: OPEN. Not searched successfully; no new source beyond the 27% fabrication figure already recorded (K21).

New caveats from this pass: Spiess and Abdollahi tables came from garbled text extraction, headline figures were cross-checked with abstracts; CRITIC cell values partly reconstructed (prose figures preferred); the Carleton thesis page gave only an abstract; Hundhausen 2002 meta-study was targeted but the page could not be opened, so it is not cited.
