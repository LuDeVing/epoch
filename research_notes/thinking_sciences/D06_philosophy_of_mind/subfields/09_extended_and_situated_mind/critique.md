# D06.09 Extended and situated mind: cross-check critique

Checked 2026-11-19 against re-extracted PDF text (arXiv PDFs, Sparrow text, Camerer text, Kosmyna text).

## Numbers re-opened (10)
1. Sparrow et al. 2011 Exp 1 (712 vs 591 ms, t(68)=3.26; 603 vs 559, t(68)=2.98): confirmed.
2. Sparrow Exp 2 recall (erase .31, erase+remember .29, save .22, save+remember .19, F(3,56)=2.80, p<.05): confirmed. Note the paired comparisons inside erased and inside saved conditions were not significant.
3. Sparrow Exp 3/4: "what vs where" figures a10 (0.49 vs 0.23) not re-read; the saved/erased accuracy (0.61, 0.66 vs 0.51 for erased) is confirmed. a10 line "0.93 recognition" not found in the text and should be treated as unverified.
4. Camerer 2018: text confirms the original authors gave no materials and noted design differences afterwards. This weakens the "failed replication" claim somewhat (design differences possible).
5. ReAct HotpotQA table (PaLM-540B): Standard 28.7, CoT 29.4 (FEVER 56.3), CoT-SC 33.4, Act 25.7, ReAct 27.4 (FEVER 60.9), CoT-SC to ReAct 34.2 (64.6), ReAct to CoT-SC 35.1 (62.0). CORRECTION: a20 garbled the rows. ReAct alone is WORSE than CoT on HotpotQA EM; it wins on FEVER (60.9 vs 56.3). Best FEVER is CoT-SC to ReAct 64.6; best HotpotQA is ReAct to CoT-SC 35.1.
6. ReAct failure table: CoT hallucination 56%, ReAct 0%; ReAct reasoning error 47% (CoT 16%), search result error 23%: confirmed. b18 and a21 agree.
7. ReAct ALFWorld 71 / 45 / 37, worst ReAct 48, relative gain 33-90% mean 62%: confirmed.
8. MemGPT 38.7/66.9, 32.1/92.5, 35.3/93.4: confirmed (the 35.3 baseline for GPT-4 Turbo not shown in extracted line but 93.4 is).
9. Toolformer 33.8/11.5/53.5 and 40.4/29.4/44.0, 97.9%, 54.8%: confirmed in text. WARNING: in the extracted layout the 33.8 and 40.4 rows sit next to a "GPT-3 (175B)" label; the first listed value belongs to Toolformer in the paper table, but the column alignment is ambiguous in pdftotext output. Other entries (a18) give the same split, so keep it.
10. Extended Mind Transformers: 38.59/37.95/36.00/33.54 (7B) and 42.74/41.96/33.50/17.68 (Chat Llama2); 70B+RAG 59.34/53.13/53.00/50.00 vs GPT-4 52.28/50.00/46.00/43.29; "6%": confirmed. CORRECTION: b15 said baselines are 33-43% at 2k-16k; the plain model falls to 17.68% at 16k. The extended-mind model is worse than plain at 2k and 4k and better only at 8k and 16k.
11. Nye 2021 (8.8 vs 20.1; 31.8 vs 50.7; 26.5 vs 41.5): confirmed. Note the 26.5% has an asterisk in the table.
12. Cognitive Workspace: d=195.66, t(18)=69.60, 54.52% and 57.1% reuse, 17-18% net, 3.3x operations: confirmed. CORRECTION: b16 says d about 190; correct is 195.66 (text also says d = 23-196, and 23.20 in one place). Test corpus tiny (counts 99 vs 30 items), so the effect size is meaningless.
13. Kosmyna: 15/18 (83.3%) vs 2/18 (11.1%): confirmed. Same sample is tiny; Stankovic 2026 critique is stated in b11.

## Contradictions between sources
- b15 vs c03 on Extended Mind baselines (above).
- b16 vs c02 on Cognitive Workspace d (190 vs 195.66).
- Sparrow: a12 and b04 meta-analysis supports the Google effect; Camerer and Hesselmann do not. The meta-analysis pools media-use studies (intensive internet use), not the memory-for-saved-items design, so it does not rescue Sparrow Exp 2.
- Ward 2017 brain drain: replications (a15, b06) null; Skowronek 2023 (a16, N=42) positive. Small N on both sides. Meta-analyses (b07, b08) not read.
- b12 (N=704) found no unaided deficit while b13 (n=52) found d=0.738; different tasks and measures.

## Weak spots
- Most LLM evidence is authors own benchmarks from 2022-2023 on old models (PaLM-540B, GPT-3.5, GPT-4). No 2024-2026 head-to-head at equal tokens with a no-tool control. Tokens are rarely matched.
- No source tests the philosophical claim (parity, constitution vs causation) on an LLM. The extended mind link is by analogy.
- K03 is labelled established but rests on Nye 2021 plus an indirect ToT result; treat as moderately supported.
- Human cognitive-offloading evidence is weak (replication failures, tiny N), so it should not drive design.

## Seen only in snippets or not opened
b01, b03, b05-b09, b14, b24, a14 (secondary), a17, a27-a29, c23-c25; Hesselmann 2020, Bastani 2025 (PNAS), Smart/Clowes/Clark 2025, Clark 2025, Adams and Aizawa, Rupert, Hutchins, Wegner, Risko and Gilbert.

## GAPS
1. At equal total tokens, does a persistent external notes file plus search beat full-context for multi-step reasoning with a modern model (2025-2026)? Need a clean head-to-head.
2. How often do stale or wrong notes mislead an agent that trusts them (Clark and Chalmers automatic endorsement), and what verification rule keeps the gain without the error?
3. Does a purpose-built tool interface (trimmed, linted output) generalise beyond code (SWE-agent) to reasoning tasks, and by how much at equal tokens?
4. What are the actual pooled values in the 2023 and 2024 brain-drain meta-analyses, and the Hesselmann Stroop numbers, to settle the human offloading evidence?
5. Do the Smart, Clowes and Clark 2025 and Clark 2025 papers give a testable criterion for when an LLM plus store counts as extended, and do critics (Adams and Aizawa, Rupert) offer a rival prediction?
6. Does ReAct-style tool loop plus self-consistency (best result in the paper) still beat pure self-consistency on current models when tokens are matched?
7. Does Bastani 2025 (PNAS) final-paper effect (guardrailed vs plain GPT tutor) replicate, and what is the exact size?
8. Is there independent replication of MemGPT and Cognitive Workspace gains outside the authors benchmarks?
9. Do repeat-step failures in ReAct (23% empty search, repeated actions) fall with a simple repeat guard, and at what token cost?
10. Which of Hutchins (distributed cognition) and Wegner (transactive memory) results with numbers apply to multi-agent LLM setups?


## Gap search results (2026-11-19, evidence_d.jsonl d01-d20)

Closed or mostly closed
- Gap 4 (brain-drain pooled values): CLOSED. Hartanto 2024 (166 effects, 33 studies, N=4,368): d=-0.02, CI [-0.06, 0.01]. OSPAN alone d=-0.13 but publication-biased (adjusted d=-0.04). Boettger 2023 (22 studies, use and presence pooled): g=-0.14, memory g=-0.23. K16 rewritten. Hesselmann Stroop numbers were NOT found; the human offloading evidence stays weak.
- Gap 2 (stale or wrong notes): MOSTLY CLOSED. Xiong 2025 shows error propagation and experience-following; MERIT 2026 measures stale harm (hybrid +0.25, p=.030 after Holm) and shows agents act on a correctly retrieved value only 55% of the time. Rule that held: verify before writing, overwrite on update, keep timestamps. No study tested a read-time re-verification rule. New claims K21, K22.
- Gap 9 (repeat guard): CLOSED against a simple guard. DeLoop 2026: exact-duplicate blocker leaves repeat proposals at 71.3% vs 69.8%; action log cuts repeats to 3.3% from 48.8%. Token cost of a guard not measured. K24.
- Gap 5 (testable criterion): PARTLY CLOSED. Smart, Clowes and Clark 2025 give no formal criterion, but name redundancy and agency problems that can be tested (K25). Adams and Aizawa, Rupert, and Clark 2025 were not opened, so no rival prediction was found. Perrier 2025 offers a reliability-threshold metric but only the abstract was read.

Partly answered
- Gap 1 (equal-token notes vs full context): MERIT shows replay is the accuracy ceiling but costs 2.7x tokens and overwriting stores match it. Pollertlam 2026 shows full context far more accurate on recall (92.85 vs 57.68 on LoCoMo) when it fits; memory wins on cost after about 10 turns. Terranova 2025 shows over 90% token cut with competitive F1. No clean 2026 head-to-head on multi-step reasoning with a notes file plus search. K23.
- Gap 6 (ReAct plus SC at matched tokens): PruneTIR 2026 ties SC at matched tokens on Qwen3-8B math (AIME25 60.9 vs 56.7). Not ReAct, not search, small model. Still OPEN for modern ReAct.
- Gap 7 (Bastani 2025): headline numbers confirmed only from a Wharton summary (+48%, +127% practice; -17% exam for the unrestricted tutor; guarded tutor equal to control). No replication found. PNAS text and SEs not read. Partly confirmed, not replicated.
- Gap 10 (Hutchins, Wegner): only MATM 2026 (K26) found; no numeric result from Hutchins or Wegner opened. OPEN.

Stayed open
- Gap 3 (tool interface beyond code): no non-code study with numbers found. Only a coding-adjacent format-tool ablation (44 to 35 successes, snippet only). OPEN.
- Gap 8 (independent replication of MemGPT and Cognitive Workspace): none found. Rival-author tables put Letta near full context on LoCoMo (74.0 vs 72.9, snippet only). OPEN.

Opened:false lines in evidence_d: d04, d18, d19, d20 (search snippets only; do not cite their numbers).
