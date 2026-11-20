# Critique: C08.03 Deployed CBR (cross-check)

## Re-checked numbers (PDF text re-opened this session)
Confirmed: CLAVIER costs ($1000 inspection, $2000 average scrap, $20-50K), two person-years, daily use since Sep 1990, "virtually eliminated ... thousands of dollars each month" (Hinkle 1994); SMART under 50% vs 87% and about 600 cases (Acorn and Walden 1992); FormTool 4.2 to 2.7 chips and cheaper formulas for 64 of 100 colours (Cheetham 2005); Memento 87.88 Pass@3, 79.40 test, 4.7-9.6 points; CBR-RAG 0.8967 vs 0.9141 (1.94%); Sourati 27.7% label match and 10% case base; Re4 DCN FF1 64.67 vs 70.11, SP 55.83 vs 61.92, about 6,000 online samples, +2.75% and +10.08%; Atzeni 6% vs 35% drop and 24 of 33 Jericho games; DS-Agent ranks 2.08/2.58/3.41 and 85%/99%; CBR-KBQA CWQ 67.1 strict, CFQ MCD1 87.8; Watson "over 130 companies by 1997" (Cheetham and Watson 2006). ExpeL ALFWorld 59.0 only partly re-found (binary text); b19-b22 rely on the earlier read.

## Corrections and cautions
- c11: the "-78.65% / -69.22%" for Re4 without Retain are figure axis labels. 78.65 also equals a Memento PM value, so do not cross-cite. The size of the Retain-removal drop is unverified: say "large, magnitude unclear".
- a21 and c04: "20 layouts at start, hundreds later, valid over 90%" comes only from lecture slides, not the paper. Not a founding number.
- a16 vs a13: 95% (review) vs 87% (primary paper). Use 87%.
- a02 "few dozen cases" for the ML argument: not re-verified.

## Contradictions
- SMART 87% vs over 95%.
- Insights vs raw cases: ExpeL favours insights on HotpotQA and cases on ALFWorld; DS-Agent favours executable cases over text insights.
- Memento offline vs online gap (-18.0 F1); authors suspect contamination.

## Weak spots
- All 1990s deployment numbers are builder self-reports: no control group, no N.
- Mark 1989 and Hennessy and Hinkle 1992 never read (a22, a23, b29, c09, c23 opened:false).
- c22 FinQA row labels lost. c18 and c20 small samples. c15 only four seeds.
- Memento ablations mix CBR with planner changes.
- Seen only in snippets or not at all: Hennessy and Hinkle 1992, Review of CBR for LLM Agents (2504.06943), Mark 1989.

## GAPS
1. Does case memory still help when matched in tokens against plain summaries or random cases, on a non-agentic reasoning task (our setting)?
2. Is storing failed cases (CLAVIER style) better than successes only for an LLM agent, at equal tokens?
3. What is the true size of the Retain (write-back) effect in Re4 and similar systems?
4. Why did retrieved cases hurt (random 1-shot below zero-shot, NOMAD)? What retrieval-quality threshold makes cases net positive?
5. Raw cases versus distilled insights: which wins per task type, and is the split predictable?
6. Is there any controlled before/after study of a 1990s deployed CBR system with N and a baseline?
7. What do Mark 1989 and Hennessy and Hinkle 1992 say about case count and accuracy?
8. Do Memento gains survive once contamination is removed (offline vs online -18 F1)?
9. Does a context filter (same load, different autoclave) help LLM case retrieval?
10. Case-base scaling: is "10% best" in fallacy work general or a noise artefact?

## Gap search results (evidence_d.jsonl d01-d18)
Tools: WebSearch budget was used up, Semantic Scholar and OpenAlex returned 429 or no budget, arXiv export API returned 429. Sources were opened by direct arxiv.org PDF download and pdftotext. No email was sent anywhere.

1. Case memory vs plain summaries or random cases on a non-agentic task: PARTLY CLOSED. Dynamic Cheatsheet (d06, d07) has no-memory, raw retrieval (DR), full history and curated memory on AIME, GPQA, Game of 24: curated usually wins, raw can fall below baseline (GPT-4o Game of 24 6 vs 10). Evo-Memory (d08) finds raw ExpRAG a strong baseline. Not token-matched and no random-case arm anywhere. Still open as our own test.
2. Failed cases vs successes only: PARTLY CLOSED. ReasoningBank (d02): raw failures hurt AWM (44.4 to 42.2), distilled failures help (46.5 to 49.7). Evo-Memory (d09) agrees. Memento stores failures but has no success-only arm (d13). Not matched at equal tokens.
3. Size of the Retain effect: PARTLY CLOSED. Re4 direction is certain, magnitude still unverified (figure annotations -78.65 and -69.22 only; no image renderer). Xiong (d04) gives a measured analogue: add-all 55.48 vs frozen 67.53 vs gated 70.95 (RegAgent). Write-back pays only when verified.
4. Why cases hurt, retrieval-quality threshold: PARTLY CLOSED. Mechanism found (experience-following, d05): similar wrong cases are copied. Similarity-gain correlation r 0.717 and 0.563 (d09). No numeric threshold exists in any source; stays open.
5. Raw cases vs insights per task type: STILL CONTESTED. Distilled wins in ReasoningBank (d01), Agent KB refine (d11), Dynamic Cheatsheet (d06); raw wins or ties in Evo-Memory (d08) and ExpeL ALFWorld. ACE (d10) warns of brevity bias. Not predictable from task type yet.
6. Controlled 1990s before/after study: OPEN. None found (d17); search was limited.
7. Mark 1989 and Hennessy and Hinkle 1992: OPEN. Paywalled, unread (d16).
8. Memento contamination: MOSTLY CLOSED on the narrow point. CBR gain is same-pipeline (+3.7 to +6.7 F1; d12), so the -18.0 F1 offline-online step is not its cause. A leak through the case bank is not excluded, and nobody has replicated.
9. Context filter for LLM retrieval: OPEN. No direct study found (d18).
10. 10 percent best in fallacy work: CLOSED as weak. Only four ratios, no variance, abstract and body disagree (d15). Treat as a noise-prone result.

Corrections to earlier text: K04 is now contested, K07 text narrowed, six new claims K16-K21.
