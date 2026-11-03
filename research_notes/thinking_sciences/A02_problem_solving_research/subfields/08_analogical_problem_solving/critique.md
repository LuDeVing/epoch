# A02.08 Analogical problem solving: cross-check critique

Checker run 2026-11-03. Sources re-opened as full PDF text this session: Lewis & Mitchell 2025 (arXiv 2411.14215), Lewis & Mitchell 2024 (2402.08955, table only), Yasunaga et al. 2024 (2310.01714), Puranam et al. 2025 (2505.00603), AnaloBench (2402.12370), Webb et al. 2023 (2212.09196), ARN (2308.16118 / 2310.00996 text), StoryAnalogy (2310.12874), Stevenson et al. (2411.02348), Step-back (2310.06117). The 1980s human numbers (a01-a23, b01-b07) were not re-opened here; they rest on the earlier agents' reading and on cross-agreement between files a and b.

## Corrections and confirmations (10 key numbers)

1. Lewis & Mitchell story analogies (b15, c05): CONFIRMED. Table 4 has three rows: GPT-4 (Webb data) 0.89 / 0.61 / 0.75 (27/36); GPT-4 (their run) 1.0 / 0.72 / 0.86 (31/36); humans 0.78 (564/720). Paraphrase table: GPT-4 0.86 to 0.72, humans 0.78 to 0.70. Note: c05 lists GPT-4 totals ambiguously; b15 is the right reading. Authors say 18 items are too few to test significance.
2. Puranam et al. (a28, c11, c28): CONFIRMED. Human radiation recall 6.25% (3/48), precision .42; dolphin precision 1.0, recall 22%. GPT-4 no hint P=R=0 (0/0), accuracy .50. Hinted recall 1.0, precision about .50. The accuracy column for GPT-4 is garbled in the PDF text (.50/.54/.57 appear scrambled); ignore it.
3. Yasunaga et al. (b19, b20, c12, c13): CORRECTION NEEDED. Table 3 (text-davinci-003 GSM8K): 0-shot 14.8, 0-shot CoT 50.3, 5-shot CoT 54.0, self-generated 61.0 (confirmed). Table 4 (scale table) gives fixed 5-shot CoT as 43 (d-002) and 50 (d-003), which conflicts with 54.0 in Table 3; retrieved 5-shot is 47 and 54 or 57 (PDF layout ambiguous), self-generated 9 / 48 / 61 and 2 at curie. Use "self-generated 61.0 vs best fixed or retrieved exemplars 54 to 57" and treat b20's "0-shot CoT 50" as the Table 3 value. The paper itself is inconsistent here. c13 is wrong to call the fixed 5-shot value "43 and 50" the same as b19's 54.0. The scale boundary (self-generation wins only at davinci-002/003) is confirmed.
4. ARN (c07): CONFIRMED. GPT-4 zero-shot 94.0, 92.5, 57.1, 29.1, mean 68.1 (second set in parentheses 63.4 etc. is a different scoring mode).
5. AnaloBench (c09): CONFIRMED. GPT-4 89.1 / 66.5 / 60.7 and humans 96.0 / 72.5 / 73.3 at 1 / 10 / 30 sentences.
6. StoryAnalogy (c08): CONFIRMED text-davinci-003 37.1%, random 25%, humans 85.7%. The table labels the 37.1 row "GPT-3.5", so "ChatGPT about 30 to 35" is a looser reading.
7. Lewis & Mitchell alphabets (b13, c04): CONFIRMED human 0.753 (CI .734-.773), GPT-3 .488, GPT-3.5 .350, GPT-4 .452. The PDF text prints the rows in scrambled order, but the model order matches the paper's figure legend. Counts 1,876 human and 6,840 per model were not re-found in the extracted text.
8. Webb et al. story analogies (a26, b11, c02): CONFIRMED near p=.0039, humans OR vs GPT-3 0.37, p=.0003. Human t(53)=21.5 for near confirmed; the combined t=21.3 and far values were not re-read.
9. Stevenson et al. (b16, c10): CONFIRMED. Adults .88/.91/.89, children .62/.66/.67, GPT-4o .85/.63/.48, Claude-3.5 .68/.62/.46, Gemma-2 27B .60/.39/.14, Llama-3.1 405B .79/.74/.27. The paper is in Journal of Memory and Language 145 (2025); c10 dates it 2026 (year mismatch in the evidence file; arXiv 2411.02348).
10. Step-back (c17): CONFIRMED abstract numbers (Physics +7, Chemistry +11, TimeQA +27, MuSiQue +7).

Other flags from reading the evidence files (not re-opened):
- Alfieri et al.: b08 gives d=.60 (conference version); published article is reported as d=.50 by secondary sources. Cite both, do not choose.
- Gick & Holyoak 1980 baseline: b23 notes secondary sources report 76% to 92% hinted success; b01 and a01 use about 75%. Use 75% as the central, with the range.
- a02's "about a third noticed spontaneously" depends on an assumed 10% base rate; Bearman et al. (b26) found 8% and 1.3% pre-hint with an analogue present, which is far below the original 30%.
- a28/a29 vs b/c duplicates: Puranam, Yasunaga, Webb and Lewis appear in two or three files. Counting them as independent sources would inflate "established"; claims count each study once.

## Contradictions between sources

- Pre-hint solution rate with an analogue available: about 30% (Gick & Holyoak), 21-32% (their Exp 2-5), 47% with two analogues (Catrambone & Holyoak), but 8% (Bearman Exp 1) and 1.3% (Exp 2). Differences in distractor load and instruction probably explain it, not yet tested.
- Evaluate vs summarise (Bearman) goes against the schema-induction story that active comparison helps; the likely reconciliation is that criticism of one source blocks encoding of its key idea. Single study.
- Human spontaneous transfer: Holyoak & Koh Exp 1 gives 81 to 86% days later, versus Catrambone & Holyoak 7 to 23% after one week. The difference is surface similarity and class-room context, as Holyoak & Koh Exp 2 predicts.
- LLM analogy: Webb 2023 says "emergent" human-level analogy; Lewis & Mitchell, Hodel & West, Stevenson and ARN show collapse on counterfactual or far items. Webb 2024 reply and Musker 2025 say the drop reflects task demands. Unresolved (K15).
- Mapping vs retrieval: Puranam shows GPT-4 never retrieves unaided but over-applies when prompted; Webb shows it can map once the source is adjacent. These agree, but with different models and different paradigms.

## Weak spots

- All 1980s human studies are college students with Duncker's radiation problem or close variants; the problem is ill-defined and the "right" answer is unusually famous. No ecologically valid test of problem-solving analogy.
- No LLM study measures retrieval of a true analogue from a large memory at equal tokens against a no-retrieval baseline on real problem sets. Closest are AnaloBench (200-story bank, retrieval near chance), Yasunaga (self-generated), Thought Propagation and Buffer of Thoughts (author-reported).
- Analogical prompting gains are small (+1 to +4 points) and vary with model scale; no studies on current frontier or reasoning models of the specific Gick-Holyoak paradigm.
- Most LLM studies use GPT-3, GPT-3.5, GPT-4 era models. Only Stevenson (Claude-3.5, GPT-4o) and Musker (Claude 3) touch newer models. No o1/o3/R1-class model tested on far analogy except a snippet (c24).
- Letter-string results mix analogy with alphabet knowledge and tokenisation.
- Gentner's own SME and systematicity work (e.g. Gentner 1983, Markman & Gentner 1993, Clement & Gentner 1991 systematicity preference) is thinly covered: only Gentner & Toupin 1986 and MAC/FAC were read. Systematicity as a "preference" for relational over surface match in adults is covered mostly through proxies.

## Only seen in snippets or not opened

- Gick & Holyoak 1980 (b23), Reeves & Weisberg 1994 (b24), Webb et al. 2024 reply (b25, c25), Camposampiero et al. 2025 (c24, snippet: R1 80.6 to 23.2 with 3.4x reasoning tokens), Copycat reimplementation (c26). Do not rely on these.
- c23 (ANALOGICAL) has no extracted scores.
- a17: ACME Table 5 cycle counts unreadable.
- Human numbers in a21 (Karla literal 58, mere appearance 45, true analogy 18, false 8%) were read from a graph by the ARCS authors.

## GAPS (most decision-relevant first)

1. At equal tokens, does a forced "which known problem has this structure?" retrieval step (O7) improve a current frontier model on real problem sets (not Duncker stories), and by how much compared with plain CoT and best-of-N?
2. Does a second explicit comparison (two analogues, write the shared schema) give gains in LLMs like the +24 to +31 point pre-hint effect in humans, or is a single self-generated analogue enough?
3. How often do LLMs accept a surface-similar false friend after a structural check step, and does a code-run or consistency check on the mapping (one-to-one, goal constraints covered) cut the over-application seen in Puranam (precision about .50)?
4. Do reasoning models (o1/o3/R1/Claude extended thinking) retrieve the deep analogue unaided on Puranam-style or AnaloBench-style tasks, and does extra thinking time help or hurt (c24 snippet suggests a drop)?
5. Is the counterfactual-alphabet failure (K14, K15) a lack of abstraction or a task-demand artefact? A direct test: give the rule in plain words with the alphabet and see whether the gap closes.
6. What retrieval index works for the agent's analogue memory: embeddings (surface bias), predicate or relational summaries, or LLM-written abstractions? Closed-set results (a30) show only a few points between options.
7. Does restating the target in schema vocabulary (Catrambone & Holyoak Exp 5) transfer to LLM retrieval, and is the gain from the wording or from the three analogues?
8. Do evaluate-versus-summarise instructions (Bearman) change an LLM's use of retrieved cases, or is that effect human-only memory interference?
9. How much does the known answer-order and paraphrase bias in story-analogy tests (K16) distort other LLM analogy benchmarks (ARN, StoryAnalogy), and do published far-analogy numbers hold after order swapping?
10. Where are adult human replications of Gentner's systematicity preference (relational over surface match in mapping, Clement & Gentner, Markman & Gentner) with exact effect sizes, and how well do LLMs match them on the same materials?

## Gap search results

Gap-search run 2026-11-03. WebSearch budget was exhausted by other agents (both attempts refused), and the arXiv, Semantic Scholar and OpenAlex search APIs returned 429 or empty replies, so only papers with known arXiv ids could be fetched. Opened as full PDF text: Camposampiero et al. 2025 (2503.11207), Webb et al. 2024 reply (2404.13070), Musker et al. 2025 (2406.13803), Hodel and West (2308.16118), Thought Propagation (2310.03965), Hu and Frank 2024 (2404.02418). Evidence: evidence_d.jsonl (d01-d15).

- Gap 5 (counterfactual alphabet): MOSTLY CLOSED. GPT-4 with spontaneous code execution equals humans on the shuffled alphabet (P=0.496); without code it is worse (P=8.9e-13). So the failure is largely counting/indexing, not missing abstraction. Still open: no run gave the rule in plain words with the alphabet. K15 stays "contested" but narrowed.
- Gap 4 (reasoning models): PARTLY CLOSED. o3-mini and R1 collapse on noisy matrix analogy (86.6 to 17.0; 80.6 to 23.2) and extra tokens do not help. Still open: no test of unaided retrieval of a deep analogue (Puranam or AnaloBench style) with a reasoning model.
- Gap 9 (order bias): PARTLY CLOSED. Musker 2025 confirms order sensitivity in GPT-4, Claude 3 and Llama-405B (coef -1.7 to -2.3). No order-swap rerun of ARN or StoryAnalogy was found.
- Gap 3 (false friends): PARTLY. Musker shows models keep trusting an uninformative source; no test of a code or consistency check reducing Puranam's over-application.
- Gap 2 (two analogues): PARTLY. Thought Propagation says one layer gives most of the gain; no direct two-analogue schema test.
- Gap 1 (equal-token retrieval step on real problems): STAYS OPEN. Thought Propagation is the only new data (synthetic graphs, token cost not matched).
- Gaps 6, 7, 8, 10: STAY OPEN. No source was found or opened for them (retrieval index choice, schema-vocabulary restatement, evaluate vs summarise in LLMs, Clement and Gentner / Markman and Gentner systematicity effect sizes).

New claims K25-K27 added; K12, K14, K15, K16 got extra evidence ids; K15 text narrowed.
