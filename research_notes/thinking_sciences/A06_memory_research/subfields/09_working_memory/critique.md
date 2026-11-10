# A06.09 Working memory: cross-check critique

## Re-opened sources (this session, full arXiv text via pdftotext)
Confirmed exactly: Wang and Sun 2025 (t=3.03, p=0.005, N=30; context length p=0.886; rho 0.673, p=0.0016; R2 26.1%; llama4-maverick about 5% at 46 keys); Xiong et al. 2026 Table 3 (MMLU-Pro .78/.70, GPQA .88/.72, IFEval .69/.82; log parameters not predictive; 10 models); Gong 2026 (median d' 2.57 at N=1, 0.91 at N=4, 0.52 at N=6; Qwen2.5-14B 4.28 to 1.15; 79% on N-1 lures; +0.44, +0.11, -1.54); WMIP (31.7% vs 84.9%, 44.4% at K=3, 0.8%, 90.0% vs 54.1%, 88.0% = 475/540 per table row); Hu and Lewis (0.99 and 0.62 sd .31; 75.25/66.08/57.1; ladder 79.83/80.17/71.67 and 90.08/90.08/84.75); Gong and Zhang (H=38.517, eta2 0.248, over 95%); Gong et al. 2024 (temperature 1, 50 blocks per n).
Not re-opened: Cowan 2001 ignored-speech means, Soveri 2017 and Sala and Gobet 2017 effect sizes, Rouder 2008 (taken from the earlier agents' opened:true lines; Soveri g values match my recollection).

## Corrections and notes
1. a19 attaches the human range r=.31-.78 to Carpenter/Engle; it is a human figure quoted in Xiong, not an LLM result. The LLM correlations rest on 10 models only, with no confidence intervals.
2. Evidence a03-a05 and a24 carry year 2025 in the id field while the source says 2024; and a24 comes from Wikipedia, not Baddeley (2000). Treat as secondary.
3. b07 says table column labels were "not fully readable"; c09/a18 give the mapping. Used the latter, with the unlabelled "transition statistics .36 / -.62" sign split flagged as odd (a positive r for transition statistics is not explained).
4. WMIP "88.0% (950/1,080)" in c17 is pooled over two settings; the table row shows 475 (88.0%) each. Same percentage, so no change to the claim.
5. c19 table order (GPT-4 vs GPT-3.5) was assumed from pdftotext, not verified; claim K16 should be read as direction only.
6. Several arXiv ids in the evidence (2610.21176, 2605.30343) are dated late 2026; I confirmed 2610.21176 text exists and matches the numbers. 2605.30343 was not re-opened.
7. b02, b12, c15, c23, c24, c26 contain no exact numbers; claims built on them are marked single-source and weak.

## Contradictions
- Hu and Lewis (instruct tiers: 70B does 2-back at .99, 3-back .62) versus Gong 2024 (ChatGPT d' about 1 at n=3): same direction, different metrics, not directly comparable.
- Hu and Lewis argue some failures are task misunderstanding; Gong 2026 finds the model's applied k-back rule differs from the instructed N in only 14 of 90 cases (N>=4, small models). Mostly compatible, but the two never test the same model.
- Xiong's suppression gain (+0.44 pattern) versus Gong's held-out +0.11: selection effect.
- Wang and Sun: size predicts interference resistance, context length does not; Dsouza (SWiM) frames distractor share as the driver. Compatible, but each uses different tasks.
- WM training: Soveri (g .16 far) versus Sala and Gobet (g .12 far, .03 in randomized active control) versus Au et al. reply (g .24 vs .13): unresolved.

## Weak spots
- Almost all LLM n-back work uses letter streams; the link to agent task performance is a single correlation over 10 models.
- No study here tests a scaffold (notes, overwrite, focus step) against a baseline at equal tokens on n-back or key-value tasks. Everything in the agent_test column is untested.
- Human classics (Baddeley-Hitch dual-task numbers, Daneman-Carpenter, Engle, Barrouillet) were seen only as secondary or not opened (a25, a26, a27, b26 opened:false).
- Many LLM papers are 2026 preprints without peer review.
- Slot versus resource debate was only covered by reviews (Ma et al. 2014) and Rouder 2008.

## GAPS
1. Does an overwrite-in-place or retire-stale-value state (versus append-only notes) beat the PI-LLM decline at equal tokens, for current frontier models with reasoning?
2. Does the instruction "write the full state after each update" (WMIP) retain its gain at equal total tokens on non-arithmetic tasks, such as our own benchmarks?
3. What are the numbers for frontier reasoning models (2026) on n-back and PI-LLM; are the cited 2023-2025 open models representative?
4. Is the n-back-to-reasoning correlation (Xiong, 10 models) reproduced with more models and controlling for training compute?
5. Does a distractor-suppression or "restate only the relevant item" step reduce lure false alarms by prompt alone, and what is the effect on held-out trials?
6. How many live items can the agent track before accuracy falls (an agent-level span), and does it match the roughly 3-4 chunk human prior?
7. Do human classical dual-task and individual-difference findings (Daneman-Carpenter span correlation with comprehension, Engle executive attention) have any LLM replication with measured effects?
8. Does chunking (renaming groups of items into one label) raise agent span the way Smith's octal recoding raised human span?
9. Is multi-agent load splitting (b12) measurably better than a single agent with structured notes at equal tokens?
10. Which of the unopened classic sources (Baddeley-Hitch 1974 numbers, Barrouillet TBRS) should be opened to settle the refreshing versus interference debate for the schema?


## Gap search results (evidence_d.jsonl, d01-d17)

Search limits: the arXiv, OpenAlex and Semantic Scholar APIs were rate-limited, and the shared WebSearch budget ran out after 5 calls. So several gaps stayed open.

1. Overwrite or retire-stale state versus append-only at equal tokens: OPEN (direct test not found). New partial evidence: prompt-only forget gives under 10 pp (d01), a restated current-state Q-and-A partly helps (d02), and models implement deletion by a fragile global remove tag (d12), so rewriting the state without the old value is the safer design. Reasoning models are absent from the PI curve (d03).
2. WMIP gain at equal tokens on non-arithmetic tasks: OPEN. Nothing new found. Latent-persistence work (d05) agrees that written variables are what carry state.
3. 2026 frontier reasoning models on n-back and PI-LLM: PARTLY ANSWERED, still open for numbers. o-series and R1 reach 36-100% on hidden-variable persistence only via the trace (d05). CogBattery: only 3 of 32 gate-passing open models, all thinking models, reach .80 on n-back (d07). PI authors claim GPT-5, Grok-4 and Gemini 2.5 Pro still decline, with no numbers (d04).
4. n-back to reasoning correlation with more models and compute control: PARTLY ANSWERED. With 54 models, scores share one scale-related dimension and cognitive-construct groupings add nothing over random groups (d08). Not a replication of Xiong's specific correlations; compute was not controlled. K12 downgraded to contested.
5. Prompt-only distractor suppression on held-out trials: PARTLY ANSWERED. Natural-language suppression fails on PI-LLM (d01); lure false alarms are a general weakness (d07). A restate-only-the-relevant-item prompt was not tested anywhere found.
6. Agent-level span versus 3-4 chunks: OPEN. Wang and Sun already show about 5% at 46 keys for one model; no clean span measure found. Human dual-task retention numbers added (d13).
7. LLM replication of Daneman-Carpenter, Engle, Barrouillet individual-difference effects: OPEN. Only CogBattery's across-model structure (d08) and a dual-task paradigm (d09) found; a backward-digit-span versus fluid-intelligence paper and a December 2025 classic-WM-tasks study were reported in a search snippet but could not be opened, so they are not counted.
8. Chunking raising agent span: OPEN. No LLM study found; Smith/Ericsson classics could not be opened (PubMed blocked).
9. Multi-agent load splitting versus single agent at equal tokens: CLOSED in the negative for general use (d10, d11). Not tested against single agent with structured notes.
10. Unopened classics: PARTLY CLOSED. Barrouillet 2004 abstract opened (d14), the 2024 TBRS dual-task quantification (d13), and Oberauer-group refresh and removal papers (d15-d17). Baddeley-Hitch 1974 numbers, Daneman-Carpenter 1980 and full TBRS text remain unopened. For the schema: refreshing in LLMs equals reselecting the item in the written state; decay has no analogue, so TBRS timing does not transfer, and interference is the live mechanism.

New claims K25-K32 added; K12 set to contested; K23 upgraded to established with numbers.
