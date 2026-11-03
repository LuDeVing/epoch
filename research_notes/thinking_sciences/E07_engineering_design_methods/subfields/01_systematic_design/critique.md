# E07.01 Systematic design: cross-check and critique

## Corrections made (sources re-opened this session from PDF text)
Confirmed exactly: ChatDev table (0.5600/0.8800/0.8021/0.3953; arXiv 2307.07924), MAST (41-86.7% failure, +9.4%, +15.6%; arXiv 2503.13657), Massoudi and Fuge table (62.9, 94.7, 38.6 s, 20% coverage max, about 650 s; arXiv 2507.08619), Ma et al. (0.804, 0.266; arXiv 2306.01779), AutoTRIZ (7 of 10 match or half-match in top 3; arXiv 2403.13002), Sobek and Ruder (0.584/0.853, 0.433/0.740, p values, group A +26% p=.142, group B +97% p=.004), Daalhuizen et al. (4.03 vs 3.23, t(211)=4.27, d=.59, N=213), Motte (2015) (about 540 designers, 43% and 31% material cost).
Corrections and cautions:
1. a25 cites arXiv 2407.00396 as "Bhattacharya SAPPhIRE"; the PDF text at that id shows a SAPPhIRE retrieval study with F-tests (F(1,16)=21.87 etc.) but no accuracy table matching the stated finding was checked; the record stays abstract-level. Treat as weak.
2. Massoudi and Fuge: the two-agent loop's 100% executability (R1, T=0) comes with 1 node and 38.6 s, i.e. a collapsed trivial design. Evidence lines a24/c04 should not be read as "simple loop beats staged on quality". The record c03 says this; claim K10 states it.
3. Sobek and Ruder compares different teams between conditions on each problem (crossover groups A and B), n=7 per group. The headline +46% and +71% are between-team pooled comparisons; the within-group effect was n.s. for group A. Treat as suggestive.
4. Chen et al. (2024) p values (1.7e-9) look inflated (a22 limits note this). Only the ordering FBS > fixed > free > search is safe; the baseline is human plus ChatGPT, not the model alone.

## Contradictions between sources
- Birkhofer/Pahl lever (large gain from staging) vs Bender, Rueckert, Motte (no link between method adherence and quality). Reconciled: gains appear in task-specific demos on new design; controlled student comparisons show none.
- ChatDev (staged beats single-step) vs Massoudi/MAST (staged pipelines lose requirements and fail 41-86.7%). ChatDev compares against weak single-step baselines and does not control tokens; MAST shows the staged pipeline fails mostly in specification and verification, not in staging itself.
- Kannengiesser and Gero: model matched early requirement/function focus but not structure timing; the method describes an idealised sequence, not behaviour.

## Weak spots
- Almost all human evidence is second-hand through Motte (2015); the original German papers (Pahl 1990/92, Fricke, Ehrlenspiel and Dylla, Rueckert) were not opened. Numbers on N=15, 16 groups, 79 students are as relayed.
- Positive industrial cases (about 30) are non-independent and from proponents; counted as one source.
- Pahl and Beitz book itself never opened (b23 secondhand).
- LLM evidence is mostly one-task, small seed counts, 70B open models (Massoudi) or old GPT-3/4 (Ma, Egea). No frontier-model staged test.
- No LLM paper compares a Pahl-and-Beitz staged prompt to a plain prompt at equal tokens (a28; searches only, not exhaustive).

## Seen only in snippets or unread
b21 (Otten 2026, body unreadable), b26 (three-team brake study), b27 (Diamond of Thought), c24 (DRS 2024 LLM morphological analysis). Not used in claims except b21 as a gap note.

## GAPS
1. Does a Pahl-and-Beitz-style staged prompt (clarify, abstract, function structure, principle search, evaluate) beat a plain prompt on a frontier LLM at equal tokens, and on which task types?
2. Is the gain from staging, or from the generic extra steps (verification, alternatives, requirement-checking code)? An ablation of stage order versus stage content is missing.
3. Why do staged LLM pipelines lose requirements (coverage under 20%), and does a code-based requirements tracker fix it?
4. Does flexible, agent-chosen ordering beat a fixed S1-S9 order for LLMs, as it does for human designers (Fricke, Rueckert)?
5. Does the staged gain depend on base-model strength, as expertise did for humans (Pahl, Ehrlenspiel)? Test weak vs strong models.
6. Is the gain larger for novel than for variant design (Birkhofer), mapped to novel vs routine benchmark items?
7. What do the original German studies (Fricke 1993/1999, Ehrlenspiel and Dylla, Bender 2004) report in effect sizes, which Motte only summarises?
8. Do early-structure sketches (Kannengiesser and Gero) help or hurt LLMs if allowed inside the clarify and function stages?
9. How should stage cost be bounded (Daalhuizen found time pressure and lower motivation) so that stage tokens pay for themselves?
10. Do frontier-model replications of Egea et al. (concept abandonment, fixation) exist, and does a persistence rule help?

## Gap search results
Sources opened this pass (evidence_d.jsonl, d01-d16). Search APIs (OpenAlex, Semantic Scholar, arXiv) returned HTTP 429, so the search is not exhaustive.

1. OPEN. No study runs a Pahl-and-Beitz style staged prompt against a plain prompt on a frontier model at equal tokens (d11). Indirect: structure helps formal tasks (d03, d05), not open ones.
2. OPEN. No stage-order vs stage-content ablation found (d11). Proposed arms: plain, generic extra steps, staged in order, staged shuffled.
3. MOSTLY CLOSED. Massoudi and Fuge audit: empty linked_reqs and ID drift (SR01 vs SR-01) under an exact-match checker (d01, d16). Whether a code-based tracker fixes it is untested (new claim K25, conjecture).
4. PARTLY ANSWERED. Self-Discover (d06): model-chosen structure beats fixed CoT and plan-and-solve. Order flexibility within one problem is untested.
5. PARTLY ANSWERED, MIXED. Gains shrink with strength (d04, d14), model too weak breaks the pipeline (d15), but a rich scaffold lifted o1 most on formal planning (d05). Claim K22.
6. PARTLY ANSWERED. Task type matters: gains concentrate in formal, verifiable work (d03). No novel vs variant design benchmark found.
7. OPEN. Original German studies not reachable; numbers stay second-hand via Motte (d12).
8. OPEN. No LLM study of early sketches in clarify and function stages (d13); only indirect anchoring evidence (d09).
9. PARTLY ANSWERED. Stage cost measured as 35-600% extra time (d04, d07). No token-budget rule tested.
10. OPEN. No frontier replication of Egea and no persistence-rule test (d10); GPT-4o fixation shown in a small study (d08).
