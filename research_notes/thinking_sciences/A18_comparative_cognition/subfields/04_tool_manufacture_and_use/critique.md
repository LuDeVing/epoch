# A18.04 Tool manufacture and use: cross-check critique

## Numbers re-opened this session (full text in D:/research_scratch/A18.04)
1. LATM Table 2 (a19, b17, c01, c02): confirmed (GPT-3.5 CoT to LATM 66.4/79.7, 61.6/99.6, 20.4/92.2, 59.2/98.3, 0/100, 18.9/100; GPT-4 88.8/86.6 Logical). Dyck explanation (GPT-4 over-edits the argument) and "2 of 60" repair figure confirmed.
2. LATM Table 4 (a20): confirmed. The printed row labels are offset by one in the PDF text; matching by value to Table 2 gives the order Logical, Tracking, Dyck, Word Sorting, CRT, Schedule.
3. MacGyver error shares (b21, c11): CORRECTION. The paper gives wrong tool usage 42.4, not achieving goal 17.7, unfaithful to constraints 16.9, wrong spatial 10.8, unavailable tools 9.5 (text: "16.9% + 9.5% = 26.4%" for constraints plus unavailable). b21 is right. c11 swapped unavailable (16.9) and unfaithful (9.5) and its own note flagged this. Use b21. Also 18.9% efficient, 37.5% infeasible, humans 79.3 vs GPT-4 73.3 confirmed.
4. Voyager (a25, b20, c08, c09): 3.3x items, 15.3x/8.5x/6.4x, 2.3x distance, random curriculum -93%, no self-verification -73% confirmed in text. Per-run table (iron 21 vs 135) not re-read.
5. Gruber 2019 (a15, b08, b27): confirmed: criterion 16/20; stone problem 2 birds within 40 trials, others at 43 and 46; exp 2 criterion in 25, 26, 39 trials and one at 69; exp 3 stick 18, 17, 16 of 20; strict test Aretha 12/14 (p=0.013), Freddie 14/18.
6. Bird and Emery 2009 (a12): confirmed 35 +/- 2.9% retrieval, 100 +/- 8.5 vs 75 +/- 4.5 degrees, 3 of 4 first trial, fourth on trial 4. Note a12 says "functional-hook choice 3 of 4 on trial 1, fourth from trial 3": the manufacture trial for the fourth rook is trial 4.
7. Taylor 2012 (a14): humans 49/50 and 42/50 confirmed; crows' pooled p=0.037 confirmed; "only one crow completed experiment 1" confirmed.
8. Lomekwi (c23): confirmed all Qwen3.5 values (0.29, 0.10, 0.05, 0.02; win rate 0.46 to 0.88; tool calls 3.1, 1.0, 0.5, 0.2; no-call 61 to 154 of 180; by hand 35 to 157; Qwen3 peak 0.93 at 8B to 0.06 at 32B). The models named in the paper include Haiku 4.5, Sonnet 4.6, Opus 4.8.
9. SkillCraft (c21, c22): 109/126 to 114/126, 1.23M to 0.26M tokens, hierarchical 90% to 79% confirmed.
10. Not re-confirmed: von Bayern 2018 (b07) figures 70.8% vs 20.8% and Fisher p values (the local text file did not contain them); keep as "from evidence line, not re-verified".

## Contradictions between sources
- a04/a05 say wild bending is routine, while a01/b02 call Betty's act first novel manufacture. Both are consistent only if Betty's act is read as a normal predisposition (claim K02 contested).
- Gruber 2019 calls its result the first conclusive evidence of multi-step planning; Taylor 2012 and Hennefield 2018 favour feedback and learning accounts. The designs differ (out-of-sight stages versus visible feedback), so both may hold.
- a02 (Kacelnik interview) reports Betty took the wire away and made the hook elsewhere; the Oxford summary (a01) does not. Interview is recollection.
- c23 (recognition falls with size) conflicts in spirit with Voyager and SkillCraft where stronger models use tools better; c24 says Voyager hides recognition because GPT-4 already knows the recipes.
- LATM: GPT-3.5 as user beats GPT-4 on Dyck; CRAFT: LATM scores below vanilla on VQA (LATM 29.4 vs 35.0 GQA). Library benefit is task-type dependent.

## Weak spots
- Most LLM results use older models (GPT-3.5, GPT-4, ChatGPT, 2023). None test current reasoning models with extended thinking at equal tokens.
- LATM and CREATOR report accuracy, not equal-token comparisons; making cost is amortised over n samples, not counted.
- Crow data are N=1 to N=14 per study with wild-caught birds of unknown history.
- Toolformer and STE involve finetuning, so they are outside our no-training constraint.
- Lomekwi is a July 2026 preprint, single group, no replication.

## Seen only in snippets or abstracts (opened:false or abstract-only)
a06, a09, a17, a18 (second-hand), b01 to b06, b10, b15, a29 (TroVE: abstract and intro only), a08 (abstract page), a27 (narrative only, no table). Claims resting on these: K01, K05, K06 (metatool 4 of 7), K22.

## GAPS (most decision-relevant first)
1. At equal total tokens (making cost included), does a make-once maker/user split beat a single pass of a current reasoning model on held-out items of the same task family? LATM never charged for making.
2. Does the "recognition inverts with model size" effect (Lomekwi) replicate for current frontier models with extended thinking, and does a forced "could a tool help" step fix it?
3. How much of a library's value comes from verification-before-storage versus retrieval? Voyager ablated verification and curriculum, but no study separates stored-tool testing on fresh items from the library itself at equal tokens.
4. Where does library size turn harmful (context cost, retrieval errors)? TroVE says trim 79-98%, CRAFT says more tools help; no study sweeps size with fixed budget on a modern model.
5. Do flat skills beat nested skills in general or only in SkillCraft? Error propagation in hierarchical tools needs a second benchmark.
6. Does a feasibility check per action (MacGyver reflection) still help for current models, and does it lower the 37.5% infeasible rate at equal tokens?
7. Is there any direct LLM test on crow-style tasks (compound tool construction, out-of-sight metatool stages, Aesop's fable) with the null model of Hennefield and Ghirlanda (first-trial versus learned success)? A search found none.
8. Are standard tool templates (the stepped-tool analogy) better than free-form tool generation for an LLM? No study isolates fixed-template versus freeform making.
9. Verify von Bayern 2018 numbers and the primary Chappell and Kacelnik tool-selection papers (b07, a18).

## Gap search results (evidence_d.jsonl, d01 to d20)
Search note: the WebSearch budget was spent by other agents after one query, and the arXiv, Semantic Scholar and OpenAlex APIs were rate-limited. Work was done from full PDFs already in D:/research_scratch/A18.04, new PDFs (AllocBench, ReGAL, TroVE) and Europe PMC.

1. Equal tokens, make-once split vs single pass: PARTLY CLOSED for in-run reuse, OPEN for held-out streams. SkillCraft (d04) charges skill making inside the task: GPT-5.2 tokens -79%, success 87 to 90%; Claude 4.5 Sonnet -71%; one model only -11%. But the baseline is a plain tool agent, not a reasoning model at matched thinking tokens, and reuse is inside one task. AllocBench (d01) shows models also decide badly when to make (builds on first sight 88 to 100% in the code frame). No LATM-style maker/user test with a current reasoning model was found.
2. Recognition inversion with size, forced check: PARTLY CLOSED. Opus builds less than Haiku (d16), so the effect is not Qwen-only. A prompt that says exactly one tool solves the task restores it (Qwen3.5 27B 0.02 to 0.60; d15). Still open: extended thinking on frontier models, and the claim is one group, July 2026.
3. Verification before storage vs retrieval: OPEN. Voyager's ablation mixes storage and progression (d07). ReGAL ablates edit and prune (d08, d09), not the verify gate. A relayed claim (Berlot-Attwell 2024, d03, not opened) says library gains are mostly self-correction.
4. Where size turns harmful: PARTLY CLOSED. TroVE INSTANCE hurts at hundreds of functions (d10); CRAFT improves through 525 behind retrieval (d12). Reading: retrieval and trimming decide it. No sweep above 525 on a modern model. Correction to K22: the 79-98% figure is versus other systems; own trimming is 74-90% with a small accuracy cost.
5. Flat vs nested: CLOSED as "model dependent inside SkillCraft" (d05): nested helped DeepSeek-V3.2 (87 to 92), tied for Claude 4.5 Sonnet (121 and 121), hurt GPT-5.2 (114 to 100). Nested used more tokens in all three. A second benchmark is still missing. Claim K15 is now contested.
6. Feasibility check at equal tokens: STAYS OPEN. Only 2023 models tested; reflection helped GPT-4 only (d17). No equal-token control.
7. LLM test on crow-style tasks: STAYS OPEN. No study found in three more queries (d20); limited search tools.
8. Fixed templates vs free-form: STAYS OPEN, with indirect support: interface hints gave +11.9 points in CREATOR (d14); abstraction and names matter in CRAFT (d13).
9. von Bayern 2018 numbers: CLOSED (d18); 70.8% vs 20.8% and Fisher p 0.037, 0.001, 0.100, 0.193 are in the paper text. Chappell and Kacelnik: PARTLY, only the 2004 abstract was opened (d19); the 2002 paper stays unverified.

Other new finding: AllocBench (d01, d02) is the strongest new item for the schema: a "has this recurred?" gate before making a tool, because models skip it in code-writing mode and a trained fix did not transfer.
Claims changed: K06 (add d18), K15 (rewritten, contested), K19 and K20 (boundaries added), K22 (corrected). Added K24 to K29.
