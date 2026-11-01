# Critique and cross-check: E07.09 Empirical design research (metrics of ideation)

## Corrections made (sources re-opened this session)
Re-opened full text of: Si et al. 2024 (2409.04109), Si et al. 2025 ideation-execution gap (2506.20803), Jiang et al. 2025 Artificial Hivemind (2510.22954), Anderson et al. 2024 (2402.01536), Wan and Kalman 2025 (2504.13868), Schaeffer et al. 2026 (2609.33936), Terwiesch et al. 2026 (2607.27553), Doshi and Hauser 2024 (2312.00506), Meincke et al. 2024 (2402.01727).

Confirmed exactly: Si 2024 novelty 4.84 / 5.64 / 5.81, N=119/109/109 reviews, 79 reviewers, 49 ideas per condition, 56.1% agreement, 4000 seeds to about 200 non-duplicates at 0.8; Excitement 4.55/5.19/5.46; feasibility 6.61/6.34/6.44. Execution gap: N=43, 19 human and 24 AI ideas, gaps 1.039/1.835/1.827/1.348 with FDR p .025/.001/.003/.004. Hivemind: 81% above 0.7 and 61.2% above 0.8 under min-p; DeepSeek-V3 vs qwen-max 0.82, vs gpt-4o 0.81; 31,250 annotations, 25 raters. Anderson: all t, p, d values match. Wan and Kalman: F(2,94)=0.573 p=.57, power 55.4%, about 165 needed. Terwiesch: 40.4/46.4/49.3% intent, novelty 40.6/36.7/36.1%, B=0.193 and 0.207, humans 0.773 and zero-shot 0.585. Doshi: +5.4% (b=.207, p=.021) and +8.1% (b=.311); similarity b=.871 and .718. Meincke: 0.243 vs 0.255; 3700 vs 4700 unique ideas.

Corrections and flags:
1. a09 and a17 say Doshi and Hauser report cosine similarity "up 10.7% and 8.9%". This is Wan and Kalman's own sentence. The Doshi text does NOT contain those figures: its 10.7% is the novelty gain of low-DAT writers with 5 AI ideas (and 6.3% with 1). Drop the 10.7/8.9% figures for Doshi; use b=0.871 and 0.718 only. (Wan and Kalman likely mis-cite.)
2. Execution-gap numbers differ between lines: b09 1.039 (difference of gaps) vs c13 -1.049 (the AI gap itself, human gap -0.010). They agree: -1.049 minus -0.010 gives 1.039. Not a conflict, but name which one is used. A robustness table (AI ideas that involved human evaluation removed) gives 1.097/1.921/1.870/1.381, same direction.
3. Ashkinaze: b19 writes "beta=0.31" and c22 writes "Cliff's delta 0.31". These are different statistics. Not re-opened; unresolved. Treat the effect as direction-only.
4. Terwiesch b14 "refine-twice agent 0.575" is measured on older GPT-4, March 2023 era; the "refinement hurts diversity" claim (K09) should not be generalised to current models. Si and MUTATE use different models and show Self-Refine below base on one model only.
5. a02 (tree level weights 10/6/3/1) remains from memory and is unverified. The Shah 2003 paper was never read by any agent (a01, a03, a04, a05, a29 are not opened). It is the keystone source of this subfield.

## Contradictions between sources
- Human homogenization: Doshi/Hauser, Anderson, Dong/Yakura say AI lowers collective diversity; Wan/Kalman null (underpowered, 55%); Ashkinaze finds diversity up with exposure. Cause may be task (story vs uses vs metaphor), embedding model, and comparison arm (Anderson compared with Oblique Strategies cards, not no-aid).
- Cross-model homogeneity size: Jiang (0.71-0.82) vs Schaeffer (harder null reproduces 20-32% of pairs above 0.8). Both opened; Schaeffer is a reanalysis, not a rerun on new human data.
- Novelty: Si 2024 says AI beats humans on novelty; Terwiesch finds humans more novel (40.6 vs 36.7); execution study says the AI advantage vanishes after execution. Different judges (experts vs LLM-classifier/crowd), domains, and model years.
- LLM judges: Si shows judges at or below chance; Doudkin uses an LLM judge that scores humans 10.22 on a 1-10 scale (optimism bias), so its +5.69 gain is not trustworthy.

## Weak spots
- Almost all numbers are for text ideation with embeddings. Few studies measure engineering artefacts (Egea dart: N=6 teams; Wadinambiarachchi N=60 sketches).
- Several 2026 results come from single groups with no replication (MUTATE, IDEAFix, Dong/Yakura, Schaeffer).
- Embedding choice (MiniLM, USE, SBERT, others) and the 0.7/0.8 thresholds are arbitrary; no study ties cosine to human-judged "same idea" with a reported error rate except partly Sankar/Sen (30 designers).
- The Shah novelty/variety metrics themselves are rarely checked for reliability (Fiorineschi: reliability tests rare, no industry use).
- c24 to c29 and parts of a15, a16, a25 are small-evidence lines; c29 is search summary only.

## Seen only in snippets / not opened
a01 (metadata page only), a02 (memory), a03, a04, a05, a29, c29. Fiorineschi review figures (b01-b05) were read by the evidence agent but not re-opened here; counts (739/686/61) are single-source.

## GAPS
1. What are the exact Shah 2003 formulas, level weights and reported results (genealogy tree, a-priori vs a-posteriori novelty, variety score) and the 2000 method-comparison numbers? The founding paper is unread.
2. Do the Shah metrics (or a cheap embedding stand-in) agree with each other and with expert ratings on LLM-generated ideas? Is there any published validation of embedding cosine against genealogy-tree variety?
3. Does an LLM scaffold with a forced-divergence operator raise cluster count at equal tokens versus best-of-N sampling, on current models (2025-2026)? Only MUTATE and IDEAFix test this, single-group.
4. Does ideation diversity or novelty predict downstream task success when the output is executed or tested (beyond the N=43 research-idea study)? Any engineering-design equivalent?
5. Does self-refinement / critique reduce diversity on current frontier models, and by how much at equal tokens? Evidence is old GPT-4 and one Claude result.
6. What is the human-baseline replication record for fixation, example effects (Jansson and Smith, Linsey) and brainstorming blocking, and do LLMs show the same fixation on a provided example (the 2024 Wadinambiarachchi N=60 result is the only direct test)?
7. What embedding model and threshold best match human "same idea" judgements, and how much do conclusions change across them (Schaeffer shows large sensitivity)?
8. Can LLM judges be made reliable for novelty (ensemble, pairwise with references, rubric)? Current results are at or below chance against expert consensus.
9. Which published engineering-design human studies (Nelson 2009, Linsey 2011, Sarkar and Chakrabarti) replicate the Shah quantity-quality relationship, and does more ideas lead to better best idea hold for LLM samples?
10. How large are the effects of the number of samples N on set novelty (saturation curve), and where is the break-even for an agent at fixed token budget?


## Gap search results

Evidence is in evidence_d.jsonl (d01-d24). Claims K01, K07, K09, K10, K12, K14, K15, K16 updated; K21-K27 added. Tool note: the shared web-search quota ran out partway; the rest used arXiv, Semantic Scholar and arXiv PDFs. Paywalled human studies (Sio 2015, Nelson 2009, Shah 2000, Girotra 2010) were not readable.

### Corrections to earlier lines
- K09 / b14 "refine-twice 0.575" is NOT an older-GPT-4 number. The Bold-Ideas agent in Terwiesch et al. ran on GPT-4o, so the right comparison is GPT-4o zero-shot 0.679, a drop of 0.104 (d07). The earlier note that it should not be generalised to newer models still stands, but the size of the drop is bigger than 0.575 vs 0.585 suggested.
- Ashkinaze: the 0.31 is Cliff's delta (disclosed high exposure; 0.26 undisclosed), not beta (d17). b19 should be read as delta.
- The 10.7% / 8.9% similarity rise is Wan and Kalman's own wording about Doshi and Hauser (d18); confirmed.
- K14: Wadinambiarachchi tests human fixation helped by AI images, not LLM fixation (d22).

### Gap 1 (exact Shah formulas): CLOSED for the 2003 paper, OPEN for 2000
Opened the full 2003 paper. Weights 10/6/3/1 confirmed. Novelty, variety, quality and quantity formulas, worked examples and the 0.944 / 0.624 / 0.591 correlations are in d01-d03. The 2000 method-comparison numbers (Shah, Kulkarni, Vargas-Hernandez) are still unread. The paper itself gives no inter-rater number for tree placement and no sensitivity test of the weights.

### Gap 2 (do Shah metrics or embeddings agree with experts / each other?): PARTLY OPEN
No published check of embedding variety against genealogy-tree variety was found, even in Ma et al. (d23) which used both families. Embedding clusters agree with 30 experts on coarse same / near / far cluster comparisons (10 of 12, d14), but on mechanism-level calls whole-text cosine is at 0.51-0.56 vs chance 0.5 and a structure graph reaches 0.871 (d13). Direct test still missing: have two raters build genealogy trees on an LLM idea set and correlate M3 with cluster count and mean cosine.

### Gap 3 (forced-divergence vs best-of-N at equal tokens): PARTLY OPEN, leaning yes
Independent single-idea sessions (best-of-N analogue) scored 0.452 diversity vs 0.679 for one session that sees its own earlier ideas (d07). A theme-then-write chain of thought raised category combinations 39 to 55 (d12); recoding-decoding gave 244 clusters from 250 vs 35 (d06). Heuresis found diversity-forcing archives top the spread ranking (d04). None of these equalise tokens against best-of-N and all are single-group. Still unmeasured: an equal-token head-to-head on 2026 models.

### Gap 4 (does ideation novelty/diversity predict executed success?): OPEN, with new negative evidence
Heuresis: spread did not predict quality or novelty over 3,222 executed runs; novel ideas rarely reach top quality (d04). Together with the N=43 study this says the link is weak for research ideas. No engineering-design equivalent was found.

### Gap 5 (does self-refinement reduce diversity on current models?): PARTLY CLOSED
Refine-twice on GPT-4o: 0.679 to 0.575 (d07). Uniform refinement of a pool raised duplicate rate 0.022 to 0.238 (d05). Counter-case: refining a person's own idea preserved human diversity (d19). Frontier 2026 models at equal tokens remain untested.

### Gap 6 (LLM design fixation; human replication record): OPEN
New: GPT-4o sessions fixate as much as humans across 10 ideas and human seeds do not change later diversity (d11). But this is not an example-exposure test. The Sio et al. meta-analysis (d20) and Nelson could not be read, and the two citing-paper summaries of Sio conflict, so the human baseline stays unverified.

### Gap 7 (embedding model and threshold vs human 'same idea'): PARTLY CLOSED
Best data: d13 (accuracy by embedding model: text-embedding-3-small 0.524 / 0.562 with keyphrase, MiniLM 0.511 / 0.524, BERTScore 0.481), d14 (coarse clusters match experts), d09 (style-neutral rewrite keeps 80-90% of the gap), d10 (category-based measure confirms gap). No study gives an error rate for a cosine threshold such as 0.8. Practical rule: dedup on tagged mechanism, cosine only as pre-filter (K27).

### Gap 8 (making LLM judges reliable): PARTLY CLOSED
Few-shot examples with expert scores plus reasoning let a VLM judge reach expert-level agreement for uniqueness and drawing quality (d15). Expert agreement itself is low on fine-grained novelty (alpha 0.33-0.47) and much better on top-half selection (d16). Not found: ensembles or pairwise-with-reference tests on novelty. Two LLM-judge papers cited Shah and were not opened (d24).

### Gap 9 (quantity leads to quality; engineering human studies): OPEN for human, PARTLY CLOSED for LLM
Human engineering studies (Nelson 2009, Linsey, Sarkar and Chakrabarti) were paywalled and unread (d21). For LLM samples: best-idea logic restated and coverage grows slowly with N (d08), top-10% share 7x for GPT-4 ideas on purchase intent.

### Gap 10 (saturation curve; break-even): PARTLY CLOSED
Plain sampling: mean nearest distance falls 0.546 to 0.478 from N=100 to 1,000 with no plateau (d08); naive repeated sampling saturates in cluster count (35 clusters from 250, d06). No fixed-token break-even curve exists.

### Task-list gap 10 (why do homogenization findings conflict; not in the critique list above): PARTLY CLOSED
Strongest explanation: source variety and task. One shared AI answer homogenizes (Doshi and Hauser, Terwiesch, Dong and Yakura ideation arm); diverse personas keep diversity (Wan and Kalman, d18; Terwiesch personas 0.757 vs 0.679); a chain where each person sees different AI items raised diversity (Ashkinaze delta 0.31, d17); AI refinement of the person's own idea preserved diversity (d19). Embedding style artefacts explain at most 10-20% of the LLM-human gap (d09).

### Still open after this pass
1. Equal-token head-to-head: forced-divergence operator vs best-of-N on 2025-2026 models.
2. Correlation of embedding variety with genealogy-tree variety on one idea set.
3. Engineering-design test of whether ideation variety predicts tested prototype performance.
4. Human baselines (Sio meta-analysis, Nelson, Linsey, Shah 2000, Girotra) need paywalled reads.
5. LLM fixation on a provided design exemplar (Jansson-Smith paradigm run on an LLM).
