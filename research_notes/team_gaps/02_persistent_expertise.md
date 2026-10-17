# Persistent, cumulative, per-part memory for HTSA agents

Date: 2026-10-17. Plain English. "Verified" means I read the abstract or page text (or a search summary of it) in this session. "Memory" means from my own prior knowledge, not re-checked today.

## Bottom line

Persistent memory helps. It helps most when it holds reusable procedures and checked facts, and when bad entries get removed. It hurts when everything is added blindly, when old records get copied back, and in search-style agents where it narrows exploration. For HTSA: keep a small, curated, source-tagged file per part, read whole, with a separate "failed framings" section, and a rule that every round also tries one thing the memory does not suggest.

## Claim -> evidence table

| # | Claim | Evidence and numbers | Source URL | Status |
|---|---|---|---|---|
| 1 | Memory stream + reflection + retrieval makes agents more believable; each part matters | Generative Agents ablation (TrueSkill, higher is better): full 29.89; no reflection 26.88; no reflection+planning 25.64; no observation/reflection/planning 21.21; human crowdworker 22.95. Retrieval scores recency, importance, relevance. | https://arxiv.org/html/2304.03442 | Verified (ablation). Scoring formula from memory |
| 2 | Tiered memory (in-context vs external, agent moves data itself) helps long documents and multi-session chat | MemGPT: virtual context management, OS-style tiers. Abstract gives no numbers. Letta is the productised successor. | https://arxiv.org/abs/2310.08560 | Verified (abstract, no numbers) |
| 3 | Linked, self-updating notes beat plain stores | A-MEM (Zettelkasten notes with keywords, tags, links; new notes can rewrite old ones). Abstract: gains over baselines on six models, no figures. | https://arxiv.org/abs/2502.12110 | Verified (abstract, no numbers) |
| 4 | A skill library of verified code compounds | Voyager vs prior best: 3.3x more unique items, 2.3x longer distance, tech-tree milestones up to 15.3x faster. Skills stored only after self-verification. Ablation (no library plateaus) from memory. | https://arxiv.org/abs/2305.16291 | Verified (abstract numbers) |
| 5 | Verbal self-reflection stored as episodic text helps | Reflexion: 91% pass@1 HumanEval vs 80% prior GPT-4 result. Memory is a short list of reflections per task. | https://arxiv.org/abs/2303.11366 | Verified |
| 6 | Distilled insights + retrieved examples learn without weight updates | ExpeL: HotpotQA ReAct 28% -> 39%; ALFWorld 40% -> 59%; WebShop score 0.666 -> 0.701. Ablation: insights only 36/50%, retrieve only 31/55% (HotpotQA/ALFWorld); both together best. Example selection by task similarity 59.0% vs random 42.5%. Trained on half of each dataset (four-fold); exact task count not stated. Hand-written insights 32% vs learned 39%. | https://arxiv.org/html/2308.10144v3 | Verified |
| 7 | Guidelines tied to the situation beat generic insights | AutoGuide: ALFWorld 79.1% vs ReAct 54.5%, ExpeL 59.0%; WebArena 47.1% vs ReAct 8.0%, ExpeL 21.8%; WebShop reward 73.4 vs 66.4 and 60.9. Guidelines retrieved by current state. | https://arxiv.org/abs/2403.08978 | Verified (search summary) |
| 8 | Reusable workflows induced from past runs help, more as tasks drift | Agent Workflow Memory: +24.6% relative on Mind2Web, +51.1% relative on WebArena; absolute gain 8.9 to 14.0 points as train/test gap widens. Works online and offline. | https://arxiv.org/abs/2409.07429 | Verified |
| 9 | Template "thoughts" reused across problems cut cost | Buffer of Thoughts: about +11% on Game of 24 vs prior best; cost about 12% of multi-query methods on average. | https://arxiv.org/abs/2406.04271 | Verified (search summary) |
| 10 | A living cheat-sheet can jump a lot, mainly by storing working code | Dynamic Cheatsheet: GPT-4o Game of 24 about 10% -> 99% (by reusing a stored Python solver); Claude 3.5 Sonnet AIME more than doubled; GPQA-Diamond +9%, MMLU-Pro Eng/Phys +8%. Depends on code execution. | https://arxiv.org/abs/2504.07952 | Verified (search summary; tables unchecked) |
| 11 | Rewriting a whole memory loses detail; append small deltas | ACE names "brevity bias" and "context collapse". Third-party report: context shrank 18,282 -> 122 tokens in one rewrite, accuracy 66.7% -> 57.1%. ACE uses incremental structured deltas: +10.6% on agent tasks, +8.6% on finance. | https://arxiv.org/abs/2510.04618 | Verified abstract; collapse numbers secondary, check paper |
| 12 | Blind "add everything" memory is worse than none | Xie et al. (ACL 2026): add-all lost to a fixed-memory baseline on all 4 agents (e.g. EHRAgent 13.05 vs 16.75). Strict quality-gated addition: 38.50. History-based deletion: CIC-IoT 85.4 -> 89.6, EHRAgent 38.67 -> 42.06; memory cut by up to ~3-5x. About +10% absolute over naive growth. | https://arxiv.org/abs/2505.16067 | Verified |
| 13 | Agents copy retrieved records; errors propagate | Same paper: "experience-following": high input similarity -> similar output; bad records get replayed and amplified; "misaligned replay" (relevant-looking but harmful records) exists. | https://arxiv.org/abs/2505.16067 | Verified |
| 14 | Memory can narrow search in tree-style agents | ACL Findings 2026 paper on memory in code agents: helps chain agents (fewer repeated errors); in tree/parallel search it constrains diversity and gives safer but worse final answers. Closest direct evidence for the fixation worry. Exact numbers not read. | https://aclanthology.org/2026.findings-acl.525.pdf | Verified via search summary only |
| 15 | LLM ideation is already low-diversity | Si et al.: of 4,000 seed ideas per topic about 200 (5%) were non-duplicates (cosine > 0.8 = duplicate). Later work finds LLM samples show fixation like humans. | https://arxiv.org/abs/2409.04109 ; https://arxiv.org/pdf/2602.20408 | Verified (search summary) |
| 16 | Memory is an attack surface | MINJA: an attacker with ordinary query access plants records that later mislead other users' queries. Defences suggested: isolation, authentication, secure memory management, filtering. Success rates not read. | https://arxiv.org/abs/2503.03704 | Verified (summary, no rates) |
| 17 | Science agents mostly persist little of their own | ResearchAgent: entity-centric store built from concepts recurring across papers, plus reviewer-agent feedback loops. Store is literature-based, not the agent's own findings. | https://arxiv.org/abs/2404.07738 | Verified (summary) |
| 18 | Persistence in multi-agent labs is in transcripts and the human | Virtual Lab: PI agent + scientist agents + critic hold meetings; a human gives feedback; 92 nanobodies designed and tested, 2 improved binders on JN.1/KP.3. Persistence via meeting summaries and code, not a memory database (from memory). | https://www.nature.com/articles/s41586-025-09442-9 | Verified (outcome); mechanism from memory |
| 19 | The AI Scientist: still weak on novelty | v1 needed a human template per topic, shallow linear experiments. v2 (tree search, no template): 1 of 3 autonomous papers above the average human acceptance threshold at an ICLR workshop; authors say it still struggles with novel high-impact hypotheses. | https://arxiv.org/abs/2504.08066 | Verified (summary) |
| 20 | Coscientist and ChemCrow: tools and documentation lookup, no cumulative personal memory | Knowledge does not grow across sessions. | https://arxiv.org/abs/2304.05332 ; https://arxiv.org/abs/2304.05376 | Memory |
| 21 | Experts organise knowledge by deep structure, novices by surface | Chi, Feltovich, Glaser (1981): experts sort physics problems by principle, novices by surface objects. | https://doi.org/10.1207/s15516709cog0502_2 | Memory |
| 22 | Expertise = domain chunks + many hours of feedback-rich practice | Ericsson, Krampe, Tesch-Roemer (1993): deliberate practice with immediate feedback; Chase and Simon chess chunks. | https://doi.org/10.1037/0033-295X.100.3.363 | Memory |
| 23 | Put knowledge in the world to cut load | Norman, The Design of Everyday Things (1988). A memory file is knowledge in the world for a fresh agent. | book | Memory |

## What this means

1. The gain is real but modest on hard open tasks. Big numbers (AutoGuide, DC) come from benchmarks with repeated task types or storable code. HTSA parts are open research; expect AWM/ExpeL-sized gains at best.
2. Quality control beats volume. Row 12 is the strongest warning: unfiltered growth lost to a fixed memory.
3. Fixation is documented (rows 13, 14, 15). It is worst with similarity retrieval and a search-style agent. HTSA is a search-style system.
4. Do not let one LLM rewrite the whole file (row 11).
5. Most science-agent systems hold little cumulative memory (rows 17-20). There is no published recipe to copy. Treat the design as untested.

## Ranked: what to adopt for per-part memory

1. **Content: five sections, short entries.**
   - Facts: one line each, with source (run id, file, URL), date measured, and how. Tag: measured / read / inferred.
   - Tried and result: what, the number, why it failed or won. Include nulls and failures; the ledger drops the "why".
   - Calibrated priors: "approaches of type X win about 1 in 6 here". These mimic an expert's base rates (rows 21-22).
   - Tacit cues: "when you see Y, check Z first". Condition -> action, like AutoGuide guidelines (row 7).
   - Open questions and untested directions, ranked.
2. **Format: structured markdown with fixed headers, one bullet per entry with id, tags, date.** Not free prose. Reusable procedures (scripts, check functions) live as files linked from memory, Voyager-style (row 4). Free text only in the "why" field.
3. **Retrieval: read the whole file, no top-k.** Similarity retrieval is what drives copying (row 13). Cap at about 2,500-4,000 words (roughly 4-6k tokens; my estimate, not from a paper). Over cap, retire entries; do not summarise the whole file. If a part outgrows it, split the part.
4. **Write-back: agent proposes, a separate curator commits.** The part agent ends its round with a "memory delta". The curator checks each item against run artefacts, drops anything unsourced, merges duplicates, flags contradictions, and appends. It edits entry by entry and never regenerates the file (row 11). Admit only items backed by a measurement or citation (row 12).
5. **Anti-fixation guard.**
   - Put "Failed framings" and "Unexplored" beside "What works", so memory carries the map of dead ends, not just the winning story.
   - Each round, require one proposal labelled "ignores memory". Score its hit rate separately.
   - Present memory as evidence ("prior results say"), not instructions.
   - Run some agents with no memory (control arm) and compare novelty and win rate. This also tests whether memory helps at all (row 14).
   - Record the conditions on each failure; a failure under old settings is not a ban.
6. **Decay and re-measurement.** Each fact has a date and a re-check round. Decision-critical facts are re-measured every N rounds (suggest 5). Entries not cited for K rounds move to an archive file, not deleted (row 12).
7. **Contradictions.** Keep both versions with dates and run ids, flag "disputed" until re-measured. Never silently overwrite.
8. **Provenance and safety.** Only the curator writes. Web text never enters memory unmarked (row 16).

## Avoid

- Add-everything memory (row 12).
- Whole-file LLM rewrites or "compress the memory" passes (row 11).
- Top-k similarity retrieval of past proposals for ideation (rows 13, 15).
- Storing only successes, or conclusions without the measurement behind them.
- Memory written as rules; agents follow it literally.
- Hand-written "expert" insights alone: in ExpeL they scored below learned ones (32% vs 39%). Seed from data and verify.
- Treating benchmark gains as forecasts for open research.

## Caveats

- Rows 7, 9, 10, 11, 14, 15, 16, 17, 18, 19 rest on search summaries. Check the full papers before quoting numbers.
- Rows 20-23 are from memory.
- I found no paper testing per-topic cumulative memory for open-ended research agents. Plan to measure it in HTSA (memory arm vs no-memory arm).
