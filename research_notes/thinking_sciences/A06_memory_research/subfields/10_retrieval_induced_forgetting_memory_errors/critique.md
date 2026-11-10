# Critique: A06.10 Retrieval-induced forgetting; memory errors (cross-check)

## Numbers re-opened this session (10)
1. Rowland et al. 2014 Exp 1 (Europe PMC full text): Nrp .45 vs Rp- .41, t(71)=2.59, p=.01, d=0.31. CONFIRMED.
2. Rowland Exp 2: Rp- .42 vs Nrp .50, t(139)=4.51, d=0.38. CONFIRMED.
3. Rowland Exp 3: Rp- .56 vs Nrp-similar .52, t(66)=0.92, p=.36. CONFIRMED.
4. Rowland d33% = 0.26 from Anderson 1994 Exp 2, n=36. CONFIRMED. CORRECTION: a03 says Rowland Exp 1 replicates Anderson Exp 1; the text says Rowland Exp 1 is benchmarked on Anderson Exp 2 (n=36) and Rowland Exp 2 on Anderson Exp 1. b01 is right.
5. Sim, Eiger & Kohno 2026 (arXiv 2609.28820): 83.6% vs 44.8%, chi2=53.937, N=328, 51.6% central details omitted. CONFIRMED.
6. Chattaraj & Raj 2026 (arXiv 2603.00270): 39 LLMs, d=1.73, r=0.21, o1 186.4, 24.6% at N=300. CONFIRMED.
7. Xu et al. 2026 (arXiv 2602.00428): GPT-5 17.63% to 41.59%, Qwen 25.48% to 74.75%, GPT-5 31.03% to 1.67%, 74.40% average reduction. CONFIRMED. CORRECTION to c05: the 15.45% to 35.21% pair sits in the Claude 3.5 Haiku row of Table 3 (Claude 4 Sonnet row: 37.94, 30.25, 47.37, 28.31), yet the paper text (line 408) attributes 15.45% to Claude 4 Sonnet. The paper contradicts itself; do not cite either model for those two numbers without checking the table.
8. STALE (arXiv 2605.06527): Gemini-3.1-pro 92.0% vs 30.0%, CUPMEM 68.0% overall, memory frameworks 17.8% best, best model 55.2%. CONFIRMED. CORRECTION to c10: the 92.0/30.0 row in the table is labelled Gemini-3.1-flash-lite in one line; the text says Gemini-3.1-pro. Model label uncertain.
9. Li & Wang 2026 (ICML workshop page): 98% vs -5%, 103 pp, 11.2 pp on 7B, N=150. CONFIRMED from the abstract. CORRECTION: it is a poster in the workshop "Failure Modes in Agentic AI", not the main track; full paper not read. b25's 24.9 pp, 100% and 0.42x attention numbers were not on the page I saw (abstract truncated); treat as unverified.
10. Loftus and Palmer 1974 numbers (smashed 40.8, hit 34.0, contacted 31.8; 32% vs 14% broken glass): NOT re-opened; consistent between b18 and c24 and with my recall, but both are memory-sourced. Murayama 2014 effect sizes: not obtained (paywalled).

## Duplicates and double counting
- b23, b24, c18, c19 are one paper (Chattaraj & Raj). b06 and c22 are one paper (Loprinzi 2026). b01-b03, a03, a04, a27 are one paper (Rowland). b05 and Oliva & Storm count once. b09 equals a06 (Raaijmakers 2016); b09 labels it "Raaijmakers & Jakab". c23 (Raaijmakers & Jakab "2011") equals a05 (2012). b14 equals a12 (Khan 2024). b17/c25 duplicate a01; b18/c24 duplicate each other; b04/c26 duplicate a08.
- Independent-source counts in claims.jsonl were set after removing these.

## Contradictions
- Wimber 2015 (a11) is reported as a result; b08 shows a reanalysis and two failed behavioural replications. Treat the neural finding as contested.
- a05 (RIF without competition) vs a18 (retrieval-specific, strength-independent RIF with novel shapes, N=87).
- a13 (initial retrieval shields) vs b10 (context change not sufficient).
- b07 (acute exercise preserves RIF, one experiment, N=158) vs b06 (N=372, not replicated).
- Retrieval-induced facilitation (b05, b28) vs RIF: opposite sign for related material under integration and delay.

## Weak spots
- No effect sizes from the Murayama 2014 meta-analysis. The robustness of RIF across about 100 studies is unquantified here.
- The only real LLM RIF test (Li & Wang) is one family (Qwen), judge-scored, abstract only, workshop-level. It has no independent replication.
- "RIF" in the other LLM papers is analogy: proactive/retroactive interference, stale memory, and social contagion are not selective-retrieval suppression. Chattaraj & Raj state their result is not RIF.
- Misinformation meta-analysis (b19) is a preprint with I2=92%; the mean g=0.694 has a CI [0.259, 1.128], so it says little about any single setting.
- Human RIF effects are small (4 to 8 points in replications, 10 to 13 in the originals); transfer to an LLM agent is untested apart from Li & Wang.
- Failed or null ones seen only as snippets or abstracts: a09, a16, a18, a24, b04, b10 to b14, b16 to b22, b27.

## GAPS
1. Does a Claude-family or other frontier model show RIF at all? Test: elaborate on 1 of K sibling lessons in context, then probe the other K-1 at equal tokens, with a no-elaboration control and a different-set control.
2. Does the Li & Wang fix (a one-turn "list every item" after the work) hold on a second model family and in agentic multi-step runs, and what does it cost in tokens?
3. Does storing a lesson and quizzing/using it later (retrieval) hurt sibling lessons in a retrieved-memory store, as opposed to in-context items? Which loads more: same-slot supersession or sibling suppression?
4. Does re-reading (restudy) a lesson vs applying it in a task differ in sibling damage for LLMs, mirroring the restudy dissociation?
5. What is the pooled human RIF effect size and its moderators (Murayama 2014 full text, plus any post-2014 meta-analysis)? Needed to set expected damage.
6. Can integration (linking siblings, shared schema) protect them in an agent, as it does in humans (retrieval-induced facilitation, k=12, about 4%)?
7. Does "stop thinking about the wrong idea" (suppression operator) lower later access to related correct ideas in LLMs (the think/no-think analogue)?
8. Which prompt defence works best against misleading context at equal tokens: warning-after, own-prior anchoring, or source scrutiny (Xu et al.: 46.0% to 17.8% or 26.5%)? Does it hold for non-peer sources such as a wrong hint in a tool result?
9. Does a write-time keep/stale/replace label (CUPMEM) generalise beyond its benchmark, and does it hide complementary facts (a RIF-like side effect)?
10. Does closure pressure (high need for closure raised RIF in humans) have an analogue: do "answer quickly" prompts reduce retention of rejected alternatives in an agent?

## Gap search results (2026-11-10)
Evidence in evidence_d.jsonl (d01 to d20). Murayama 2014 full text was read; the APIs for arXiv, OpenAlex and Semantic Scholar were rate-limited, so most LLM papers were read as abstract pages only.

1. Frontier-model RIF (Claude family): STAYED OPEN. No test found (d20). Only Li and Wang (Qwen 7B/72B) exists.
2. Li and Wang fix on a second family / agentic runs / token cost: STAYED OPEN. Page re-read (d08): Qwen only, one extra turn listing item names, no arXiv version. The earlier doubt about the 24.9 pp, 98% and 0.42x numbers is settled: they are on the ICML page. Still unreplicated.
3. Sibling suppression in a retrieved-memory store vs supersession: PARTLY CLOSED. Supersession is the measured harm (Supersede: 92% to 77% on gpt-5.4; MINTEval: 27.9% mean accuracy, worse as updates grow; Qiao: latest-state accuracy falls; d09, d10, d13, d14). No sibling-suppression measurement in stores exists. Verdict: guard supersession first.
4. Restudy vs apply for LLMs: STAYED OPEN. Human prediction firmer (restudy g=0.07, k=17; d04). No LLM data.
5. Pooled human effect size and moderators: CLOSED (d01 to d07). g=0.35 [0.32,0.38], k=512, I2=63%; output interference halves it (0.50 vs 0.22); about 5 raw points when controlled. No post-2014 meta-analysis found in the search, so this is dated 2014.
6. Integration as a shield for agents: PARTLY CLOSED for humans (text, high vs low integration g=0.01 vs 0.25, k=7 each; d05). Untested in LLMs. The earlier retrieval-induced facilitation figure (k=12, about 4%) was not re-opened.
7. Suppression operator (think/no-think analogue): STAYED OPEN. ICF-Bench and Unable to Forget show models struggle to drop content and that ignore-prompts help little (d14, d15); none measures collateral loss to related correct ideas.
8. Best prompt defence vs misleading context: PARTLY CLOSED. Compliance Trap (d12): wrong memory adopted 63 to 72%, placement does not matter, retry-on-fail gating safer. No equal-token comparison of warning-after, own-prior anchoring and source scrutiny found; Xu et al. numbers stand as before.
9. CUPMEM labels generalise / hide complementary facts: STAYED OPEN. The paper reports no label ablation, no other benchmark and no false-stale rate (d11); only part of the page was read.
10. Closure pressure analogue: STAYED OPEN. Premature closure is common (d16) and concision prompts shift accuracy little (d17); neither measures loss of rejected alternatives.

Net: gap 5 closed; gaps 3, 6, 8 partly closed; gaps 1, 2, 4, 7, 9, 10 open and need our own experiments. claims.jsonl gained K28 to K35 and K01, K02, K03, K05, K07, K08, K13, K14, K16, K18 were updated (K02 moved to established).
