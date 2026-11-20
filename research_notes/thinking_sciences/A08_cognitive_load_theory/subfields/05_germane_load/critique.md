# Critique: A08.05 Germane load (cross-check)

## Sources re-opened this session and checked
- Krieglstein 2022 meta-analysis (Springer PDF): alpha ICL .823, ECL .773, GCL .860 (k=42); GCL-retention r=.188 (k=15), GCL-transfer r=.173 (k=12). Confirmed.
- Leutner and Biele 2025: comprehension g=0.04 SE .11 p=.738; transfer g=-0.10; moderators Q=0.00 / 0.92 / 7.90; g=0.35 with integration, -0.15 without. Confirmed.
- Kaiser 2025 CogniLoad: .89 to .66, .71 to .40, d=1 to 3 o3 .96 to .93, N=250 gpt-5 .76 and o3 .68. Confirmed.
- Shang 2025/26 CoThinker: Flash-8B Math 33.8 to 37.7, Language 16.1 to 29.4, Instruction 84.3 to 68.1, Pro Math 60.9 to 75.3, GPT-5 reasoning 68.38 to 81.88, Holm tests, three significant losses. Confirmed from tables (column pairing read from layout text, so slightly uncertain).
- Adapala 2025: .85/.82/.78/.72, slope -0.003 [-.004,-.002], 32% to 12% missing answers. Confirmed.
- He 2025 AdaptMI: 4% easy-question drop, gains up to 3.6% and 6%, table cells -10.3 and -8.7. Confirmed.
- Debue 2014: F(2,91)=5.605, eta2=.112, means .65/.52/.50. Confirmed.
- Bastani 2025 (previously unopened): abstract read via Crossref. +48% and +127% practice, -17% exam for GPT Base. Confirmed for the abstract only; GPT Tutor exam stats not read.
- Not re-opened: Klepsch 2017 (download failed; numbers rest on the first run), Jiang and Kalyuga, ToolLoad, CLAI, Kosmyna, Taneja.

## Corrections
- Debue prints "p = 0.05" next to F(2,91)=5.605; that p is too loose for that F (about .005). Treat as a typo in the paper; the effect stands.
- Many evidence lines are duplicates of one paper (a21/c01/a22; b16/b17/a16; a15/b18; a20/c05-c08; b24/c11). Independent-source counts in claims.jsonl count papers, not lines.
- c20 is a pointer and c26 a search note, not evidence. c24 stays opened:false in the file (abstract only now verified).
- a13 (Leppink 2014) was never opened: do not cite its numbers.

## Contradictions
- Sweller 2023 says no germane-specific effects arose; the 2019 paper still reads variability and self-explanation as germane-style effects. Only the 2019 redefinition (redistribution) reconciles them, and it makes the construct hard to falsify (de Jong 2010, Kalyuga 2011).
- Variability: de Croock 1998 (better transfer without higher rated load) vs the germane reading (higher load, better transfer).
- Leutner and Biele: the "increase germane load" moderator is ns but "facilitates integration" is significant; the two codings overlap and were author coded.
- CoThinker: gains on reasoning but a large loss on instruction following; removing TMS raised GPT5-Nano (62.36 vs 55.97) and lowered Qwen3-30B.

## Weak spots
- No LLM study manipulates germane load. LLM papers manipulate length, distractors, tool count or presentation; the germane labels are the authors' mapping.
- Most LLM claims are single-source, single-lab, often preprints; frontier models have only 10 puzzles per config in CogniLoad.
- CoThinker and CLAI show no verified token-matched control; the CLAI accuracy differences are within noise.
- Leutner and Biele pools drawing only, mostly science text, small k (transfer k=7).
- Human AI-learning studies are small (Taneja N=124; Kosmyna 18 completers).

## Seen only in snippets or abstract
Sweller 2010, Kalyuga 2011 (abstract and references), Gupta 2026 CogLoadBench (no numbers), Bastani (abstract), Chen 2023 (intro only), Prism (reported figures only), Leppink 2014.

## GAPS
1. Does any LLM experiment, at equal tokens, show that forcing an explicit integration or self-explanation step beats prompts that only add length? (Humans: g=0.35 with integration.)
2. Does an adaptive gate (scaffold only when the item is hard) beat always-on scaffolding for frontier reasoning models, not just small ones (AdaptMI)?
3. Is there an expertise-reversal effect for LLMs: does a scaffold help weak models and hurt strong ones at equal tokens, and where is the crossover?
4. Does CoThinker's gain survive a token-matched single-agent baseline with the same schema?
5. Can element interactivity be scored per task and predict LLM failure better than token length (CogniLoad confounds N with load)?
6. Is the CogniLoad drop from N=20 to 50 a working-memory-like limit that chunking removes in frontier models?
7. Do Klepsch 2017 and Leppink 2014 numbers hold on re-reading, and do 2023-2026 scale validations replicate the weak GCL validity?
8. Do self-generated intermediate structures (Stull and Mayer organisers) help or hurt LLM reasoning at equal tokens?
9. What are the Bastani GPT Tutor exam numbers, and what is the agent analogue of preventing offloading of the learning step?
10. Are there 2024-2026 human CLT replications of the variability by problem-format interaction with cell means (original numbers still unread)?

## Gap search results (2026-11-19)
Search budget note: arXiv API, Semantic Scholar and OpenAlex were rate-limited or out of budget, and WebSearch ran out after one call, so sources were found from known arXiv ids and read as PDF text or HTML. New evidence is in evidence_d.jsonl (d01-d16); claims K08, K12, K13, K14 updated, K18-K21 added.

1. Integration vs length at equal tokens: STAYS OPEN. No study found that pits an explicit integration or self-explanation step against length-matched elaboration. Related: same-length filler gives no gain (Lanham, d06); 5-word drafts match CoT (Chain of Draft, d13); longer demonstration steps help GPT-3.5-era models (Jin, d08). Net: content matters, length alone does not, but the integration step itself is untested.
2. Adaptive gate on frontier models: PARTLY OPEN. Support for gating (DiffAdapt d01-d02, cascade d12, CoT meta-analysis d09), all on 1.5B-8B models or older/mid models. No frontier-model adaptive-vs-always-on test found. Cascade (try cheap, verify, escalate) is the best-supported form.
3. Expertise reversal for LLMs: PARTLY CLOSED as a pattern, open as a crossover. Benefit of multi-agent scaffolding fell from about 10% to 3% with a stronger model (d12); CoT hurt top models on some tasks (d10); plain models beat reasoning models at low complexity (d11, abstract only). Not measured at equal tokens with one scaffold and a model ladder.
4. CoThinker token-matched baseline: STAYS OPEN for CoThinker itself (not found or opened). Analogous studies show debate systems lose to self-consistency at equal calls (d03, d05), so the control is needed.
5. Element interactivity scored per task: STAYS OPEN. No LLM paper with a validated per-task element-interactivity score was found in this session (search tools were unavailable).
6. CogniLoad N 20 to 50 as chunking limit: STAYS OPEN. Only indirect support (d11 complexity collapse); no chunking test.
7. Klepsch and Leppink re-read: Klepsch CLOSED (d14: CFI .612 vs .970, GCL alpha .67 with three items). Leppink 2014 and 2023-2026 scale replications NOT checked.
8. Self-generated structures at equal tokens: STAYS OPEN. Nothing new found.
9. Bastani: CLOSED (d15, d16): exam -0.054 (17%) for GPT Base, -0.004 for GPT Tutor (ns), practice +0.137 and +0.361, about 1,000 students. Agent analogue stated: keep the integration step with the main loop.
10. Human variability-by-format replications: STAYS OPEN (not searched; no budget).
Corrections: none to earlier evidence. Note d08 (Jin) zero-shot baseline numbers look odd; treat as unverified table reading.
