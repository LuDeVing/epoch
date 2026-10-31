# Critique and cross-check: A16.02 Embedded cognition

## Corrections made (sources re-opened this session, text extracted from PDF/HTML)
1. SWE-agent (arXiv 2405.15793). Table 1: Shell-only GPT-4 Turbo = 11.00% on Lite; SWE-agent = 18.00% (54/300), a 64% relative gain. The abstract's "10.7 points" is against Shell-only WITHOUT demonstration (7.33%); against the default shell baseline the gap is 7.0 points. So a20's "10.7 points over plain shell" is right only for the no-demo shell. HumanEvalFix pass@1 is 88.3%, not 87.7% (c01 corrected). Claude 3 Opus: 10.46% full set, 13.00% Lite. Full set 12.47% (286/2,294).
2. Toolformer (b12): garbled table checked against the PDF. Toolformer disabled 14.8/6.3/15.0; Toolformer with tools 40.4/29.4/44.0; GPT-J 7.5/5.2/9.9; GPT-3 175B 14.0/10.0/19.8. b12 confirmed.
3. Huang et al. (b15): confirmed. GPT-3.5 GSM8K 75.9 to 75.1 to 74.7; CommonSenseQA 75.8 to 38.1 to 41.8; HotpotQA 26.0 to 25.0 to 25.0. GPT-4 GSM8K 95.5 to 91.5 to 89.0. Oracle GPT-3.5 CommonSenseQA 89.7. Retention 74.7% confirmed.
4. Nye et al. (a19): 8.8 vs 20.1 (few-shot) and 31.8 vs 50.7 (fine-tuned), polynomial evaluation, confirmed. c09 said no figures were found; a19 stands.
5. PAL (b11): GSM-Hard CoT 65.6 to 20.1 (almost 70% relative), PAL 61.5 confirmed. The "+15 on GSM8K" is the abstract claim; the paper text also contains a 14.1-point figure for another set, so say "about 15".
6. Voyager (a22/b16/c12): -73% without self-verification and -93% random curriculum confirmed.
7. Kosmyna (b18): 15/18 (83.3%) vs 2/18 (11.1%) confirmed. Preprint, session subsets, tiny N.
8. Wei et al. (b09): 46% nearly correct vs 54% major errors confirmed (27 of 50 need substantial edits).
9. Brain-drain meta (b03): 22 studies, 43 effects confirmed. Sign of g not re-checked (extraction lost minus signs).
10. ReAct (a18/b13): best ReAct 71% vs best Act 45% on ALFWorld confirmed.

## Contradictions between sources
- Illusion of Thinking (a26, c07) vs Lawsen (c08): "algorithm in the prompt does not help" is disputed; critics blame output length and grading. Contested. The design lesson (the program executes long procedures) is supported on both sides.
- CoThinker (c04, c06) shows big gains from splitting load on hard tasks but a loss on instruction following. c05: removing shared memory raised GPT5-Nano (55.97 to 62.36) and GPT-OSS-20B (57.15 to 58.37) but lowered Qwen3-30B (81.87 to 76.41), so shared memory is model dependent. Role styles helped all three.
- MAST (b17) says multi-agent systems often fail; CoThinker says they help. Different tasks and models, no equal-compute control in either.
- Google-effect meta (b06): pooled d about 1.0 is implausibly large; Sparrow 2011 reportedly failed to replicate (a12, b07). Unresolved.
- Dates: c13 labels ReAct 2022 (arXiv) while a18/b13 say 2023 (ICLR). Same paper, one source.

## Weak spots
- Founding studies: Martin and Schwartz 2005 never opened (403). Hutchins 1995 only through reviews. Kirsh and Maglio 1994 read, but timing comes from 3 pilot subjects and Fig 15 has no inferential test. Zhang and Norman 1994 PDF was garbled; exact p values missing.
- No LLM study measures load. All "environment reduces load" LLM claims are about accuracy.
- Most LLM evidence: one model, single-run ablations (SWE-agent N=300, a few points of noise), usually not at equal tokens. Cognitive Workspace (c03) reports absurd effect sizes (d up to 196) and no accuracy.
- Voyager: three runs, one game.
- c20, c22, c23 seen only as snippets or structure; do not cite for numbers.

## Only snippets (not opened)
a12, a13, a17, b01, b02, b04, b05, b07, b19, b20, b21, b22, c20, c21, c22, c23, c24, c25.

## Independence note
Many LLM lines repeat one paper (ReAct a18/b13/c13; SWE-agent a20/b14/b25/c01/c02; PAL a21/b11/c10; Voyager a22/b16/c11/c12). Each counts as one source. Five claims are marked established (K01, K02, K05, K06, K10); K05, K06 and K10 rest on related papers, so treat them as moderate.

## Environment note
Drive C was full during this step; reads and file writes worked only with the dedicated tools, and re-checks were extracted to D:/research_scratch/A16.02/.

## GAPS
1. Equal-token test: does an agent-editable scratch workspace (Martin and Schwartz's manipulation) beat a fixed scratch template? No LLM study exists and the original paper is unread.
2. Which SWE-agent features (lint guardrail, bounded view, summarised search) carry the gain when replicated by other groups and models, with variance and equal tokens?
3. Do epistemic (probe) actions improve LLM answers at equal tokens, and when does probing cost more than it saves? Annese et al. 2025 suggests models choose probes badly; no measured fix.
4. One chain vs split contexts vs self-consistency at equal compute (CoThinker has no such control).
5. Does a harness help weak or current small models at all? c18 shows flat results for non-reasoning models.
6. Does a program-held log of verified results beat the model re-reading its own prose, and does the Kosmyna memory cost have an agent analogue?
7. Open Ward 2017 and its 2022 replication and Camerer 2018's Sparrow result, record effect sizes, and close the human offloading-harm family.
8. Does the Hanoi collapse survive correction when the model emits a program and the harness runs it, at 8 to 15 disks?
9. Does Hutchins's calculator-in-emergency-fixes claim hold in the book, and is there any measured error rate for the navigation team?
10. Boundary: when does a tool call or multi-voice step lower accuracy on easy tasks (instruction following 0.95 vs 1.03), and what simple gate predicts it?

## Gap search results (evidence_d.jsonl, d01 to d22; claims K20 to K24 added)

Tools: WebSearch quota was used up; I used arXiv PDFs, PubMed Central, Crossref and OSF APIs, and fetched pages. Several search APIs were rate limited. Drive C was full; downloads and extracts stayed on D.

Closed or mostly closed
- Gap 4 (one chain vs split vs voting at equal compute): mostly closed for pure reasoning. Tran and Kiela 2026 (d03, d04): at equal thinking tokens the single chain wins from 1000 tokens up (mean 0.418 vs 0.379 sequential, 0.388 debate; 0.426 vs 0.387 at 10000). Multi-agent wins only at 100 tokens (0.290 vs 0.364) or when the context is heavily corrupted. Zhang 2025 (d07): debate beats chain-of-thought in about 15% of 36 configurations and rarely beats self-consistency. Kim 2026 (d05): planning -39% to -70%. CoThinker still has no such control.
- Gap 10 (when voices or tools hurt, and a gate): partly closed. Kim 2026 gives a usable gate: skip extra agents when the single-agent score is above about 45% or the task is a sequential chain (beta=-0.236, p=0.004). The think tool is no help on simple tasks (d10). A prompted tool-need check is a weak gate (d15: 61.9% vs 50.0% for always-call). The 0.95 vs 1.03 instruction-following loss in CoThinker is still not explained by a measured gate.
- Gap 7 (human offloading-harm family): mostly closed as 'weak'. Ward 2017 Experiment 2 replication N=383, OSpan location F(2,377)=0.10, p=.91 (d18). Sparrow Experiment 1 failed twice (Camerer 2018 N=104 then 234; Hesselmann 2020 N=89, BF01=5.07, d16). Camerer overall 13 of 21 replicated at about half the original effect (d17). A 2023 meta-analysis (k=56, n=7093) finds only working memory significant (d19). Not read: Ward's original effect sizes and Sparrow's own per-study row, so original-versus-replication effect-size pairs are still missing. Note the Camerer replication tested Sparrow's Stroop-type Experiment 1, not the memory experiments.

Partly addressed
- Gap 2 (which SWE-agent features carry the gain): not closed. Another group (Agentless, d08) shows a fixed program-owned pipeline reaching 32.00% on SWE-bench Lite vs SWE-agent 18.33% to 23.00%, and the SWE-agent team's own bash-only agent is reported above 74% on Verified (d09). So the 2024 interface gains look era-specific, but there is no feature ablation with variance and equal tokens from any group. K04 changed to contested.
- Gap 3 (epistemic probes): not closed. Annese 2025 (d13) confirms models pick probes badly (5 trials per cell); Uncertainty of Thoughts (d14) reports +38.1% for a program-side information-gain rule, abstract only and not at equal tokens.
- Gap 5 (weak models): not closed. Only indirect support (d05 capability ceiling, d09). No weak-model harness-on/off test at equal tokens found.
- Gap 6 (program-held log vs prose): not closed. Closest: Laban 2025 (d12), a fresh consolidated message removes a 39% multi-turn loss, restating recovers 15-20%; Anthropic memory plus context editing +39% (d11, vendor, internal). No agent analogue of the Kosmyna memory cost found.
- Gap 8 (Hanoi with emitted program): not closed. Lawsen (d01) says a 15-disk Lua function works in under 5,000 tokens but gives no counts; Shojaee's reply (d02) shows first errors at about 15% of an N=8 solution and no change at temperature 0, but that is for move lists, not programs. Needs a run: model emits program, harness executes, N=8 to 15, several models, counted.
- Gap 1 (editable scratch vs fixed template): not closed. Martin and Schwartz 2005 full paper still unread; only the abstract (d20): adapting unstructured material gave better transfer in Experiments 4-5. The think tool (d10) is a fixed scratch template: airline pass^1 0.404 alone vs 0.584 with an example prompt, retail 0.812 vs 0.783 baseline, and Anthropic now prefers extended thinking. No editable-vs-fixed LLM test.

Still open
- Gap 9 (Hutchins calculator claim and navigation error rate): the book text is not open to read (401, lending library); not worked around. K18 stays qualitative and unverified.

Corrections to earlier lines
- d10 note: the Anthropic page's table (0.584 vs 0.332) and text (0.570 vs 0.370) disagree; cite neither without saying so.
- Camerer's Sparrow replication was Experiment 1, so the claim 'Sparrow failed to replicate' applies to the Stroop-type result only.

Tests the agent still needs (all at equal tokens, 3+ seeds): editable vs fixed scratch; program-held log vs transcript; model-chosen vs information-gain probes; gate on the voice step at a 45% single-pass threshold; code-emitting Hanoi at 8 to 15 disks.

Environment note: cp to the project folder failed several times with 'No space left on device' on drive C; evidence_d.jsonl and the claims and critique edits were applied when space appeared. Backups of the earlier claims.jsonl and critique.md are in D:/research_scratch/A16.02/out/.
