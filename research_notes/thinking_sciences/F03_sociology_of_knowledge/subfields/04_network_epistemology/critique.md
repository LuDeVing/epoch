# F03.04 Network epistemology: cross-check critique

## Corrections and checks (sources re-opened this session, text read via pdftotext)
Confirmed exactly against the paper text:
- Ann et al 2026: 0.315 to 0.229; Chain +0.051/-0.024 (97%); Debate +0.012/-0.078 (88%); diversity +0.188 [+0.073,+0.299]; 10/10 vs 2/10; drops to +0.014 without the Erdos task.
- Li et al 2024: +4.0% MATH, +4.5% GSM8K, sparse +3.0 to +7.5, tokens -41.5% and -43.5%.
- Pappu et al 2026: gap 6.3/14.4/18.1/41.1/20.3; HLE 29.0 / 28.0 / 36.0 / 47.5.
- Tran and Kiela 2026: 100 tokens single 0.290, sequential 0.364, debate 0.370, ensemble 0.280; 500 tokens 0.390 / 0.376 / 0.380 / 0.310.
- Weatherall and O'Connor: 96% true consensus at k=0; 55% / 44% at k=0.1; consensus about 16%; 10,016 sims.
- Du et al 2023: 67.0, 72.1, 81.8 (arithmetic); 77.0, 75.0, 85.0 (GSM8K); 91.4, 102.1, 122.9 (chess).
- Choi et al 2025: martingale theorem (Theorem 2); voting on par with debate.

Flags and corrections:
- Du et al (a24): the "majority 69.0" and "81.0" cells were not located in my check; only the single, reflection and debate columns were confirmed. Treat the majority cells as unverified.
- Han et al 2026 (a21): "0.70 ring to 0.75 complete" was NOT found in the paper text (its tables show cells from 0.58 to 0.87 by weight and model). Treat the number as unverified. The qualitative claim (denser converges faster, wrong-but-sure cascades) matches the abstract.
- Duplicated ids: Zollman 2025 handbook = a06-a08, a25, b09, b10 (one review; b09/b10 lack year). Li 2024 = a19, b19-b21, c06, c24 (one paper). Zheng 2026 = a28/b28/b29/c04 (one paper). Rosenstock 2017 = a09-a12 and b04-b08 (one paper opened by two agents). Independent-source counts in claims.jsonl count papers, not ids, except where noted.
- Rosenstock et al 2017 could NOT be re-opened (author PDF link dead; archive copy removed). The only cross-check is that agents a and b report identical numbers (gap 0 for pB>=0.525, under 2 points at 0.51, 99.12% vs 100%, 20 vs 1,977 rounds). K03 is therefore marked single-source.

## Contradictions between sources
- Zollman 2007/2010 (cycle > complete, called robust) vs Rosenstock 2017 (only at hard parameters). Rosenstock wins on generality; Zollman holds in the hard regime.
- Kummerfeld and Zollman 2016 (complete beats cycle with exploratory agents) vs Zollman 2007.
- Lazer and Friedman 2007 vs Mason and Watts 2012: reconciled by copying rule (Barkoczi and Galesic), a simulation reconciliation, not a human replication.
- LLM debate: Du 2023 (debate helps) vs Choi 2025, Zhang 2025, Wang 2024, Tran and Kiela 2026 (gain mostly voting or single agent). Han 2026: denser slightly better. Li 2024: sparser equal or better. Zheng 2026: more links needed than theory. No LLM study reproduces the Zollman reliability-for-speed trade-off on a real bandit.

## Weak spots
- No LLM study uses the actual Bala-Goyal bandit. All LLM tests are indirect (debate accuracy, token cost).
- Many LLM studies use older or small models (GPT-3.5, 7B-8B), 100-500 items, 3-5 seeds. Strong reasoning models show herding (Zheng, Hirota), so effects may differ.
- Network-model speed is counted in rounds; our agent pays tokens. Token-matched comparisons exist only in Tran and Kiela, Choi, Ann.
- Several foundations were not opened (Bala and Goyal 1998, Lazer and Friedman 2007, Mason and Watts 2012, Derex and Boyd 2016, Mayo-Wilson et al 2011).
- Some numbers in Zollman 2007 are read from figures; Zollman's own text says absolute values should not be taken seriously.
- Seen only in snippets or abstracts: a16-a19, b03, b14-b18, b31, c14, c19-c23.

## GAPS
1. Does a Zollman-style effect appear in LLM agents on a real two-armed-bandit or hard-signal task, with equal tokens, comparing independent attempts against shared results?
2. Does the isolation benefit scale with task hardness (signal gap) for LLMs, as Rosenstock predicts, and vanish on easy items?
3. For a single agent running sequential attempts, is a fresh attempt without seeing earlier answers better than revising with them, at equal tokens, per task type?
4. Does sharing negative results (failed attempts) fix the cascade problem, as Zheng et al suggest, and what is its token cost?
5. How does diversity among independent samples from one model change with reasoning effort and temperature (herding), and do persona or prompt differences restore it?
6. What do the unopened foundations (Bala and Goyal 1998, Mason and Watts 2012, Derex and Boyd 2016, Mayo-Wilson et al 2011) report in exact numbers, and do human experiments replicate the Zollman effect at all?
7. Is the Kummerfeld-Zollman reverse effect (exploratory agents prefer dense networks) mirrored in LLMs at high temperature?
8. Do verifier-based selection or confidence-weighted aggregation avoid expert dilution (Pappu) better than averaging, at equal tokens?
9. Where is the break-even between independent voting (plateau near 8 samples) and one limited-visibility revision round?

## Gap search results (evidence_d.jsonl, d01-d20; claims K24-K32 added, K09, K15, K21 updated)
Web search quota was used up. Sources were reached through PubMed Central, arXiv and a university repository, and read as full text. No LLM study was found that runs the Zollman design on a real bandit.

1. Zollman-style effect in LLMs on a real bandit: OPEN. Closest is Krishnamurthy et al. 2024 (d07): one GPT-4 agent in a 5-arm bandit (gap 0.2) never retries the best arm in over 60% of runs, so the failure exists inside one agent. No independent-vs-shared comparison exists. Kim et al. 2025 (d13): independent unchecked runs amplify errors 17.2x vs 4.4x with a validator.
2. Isolation benefit grows with hardness: PARTLY SUPPORTED, indirectly. Snell 2024 (d08): easy MATH items favour sequential revision, hard ones favour parallel samples. Kim 2025: negative returns above about 45% single-agent accuracy. Zheng 2026 (d15): herding mattered little where the clue was obvious. No study varies the signal gap directly (K32 contested).
3. Fresh attempt vs revising at equal tokens: MOSTLY CLOSED for code and math without feedback. Olausson (d10): more initial samples beat more repairs. Huang (d11): intrinsic self-correction lowers accuracy. Snell (d09): tuned reviser narrowly ahead on average. Madaan (d12): refinement beat one long chain, but that is not fresh sampling. K28 contested; no per-task-type table for modern reasoning models.
4. Sharing negative results: PARTLY CLOSED. Zheng (d14): sending every verdict, failures included, automatically brings agents near theory; self-chosen reports disclosed negatives only 35-53% (Qwen) and 69-84% (GPT); r = -0.91 with excess links needed. Token cost: not measured in the paper. Still open.
5. Diversity vs effort, temperature, persona: PARTLY CLOSED. Effort lowers diversity (d15: 25.5 to 11.3 unique literals). Within-prompt similarity above 0.8 at T=1 and 81% of pairs above 0.7 at T=2 (d16). Verbalized sampling raises diversity 1.6-2.1x on creative tasks (d17). Persona prompts: no direct measurement found. Open for reasoning tasks.
6. Unopened foundations: MOSTLY CLOSED. Bala and Goyal (d01-d02, 1996 working-paper version): Royal Family lock-in, incomplete learning up to 0.2. Mason and Watts (d03-d04): efficient networks won (beta -4.63); networked beat independent 68 vs 39. Derex and Boyd (d05): both 3rd-level innovations 58.3% vs 0%. Becker et al. (d06): diversity fell 43% yet accuracy rose in decentralised networks. Human replication of the Zollman effect: not clean (K09 contested). Mayo-Wilson et al. 2011/2013 (d20): not opened; stays open. Note Bala-Goyal 1998 is not the Zollman bandit model; do not cite it for speed-vs-reliability.
7. Kummerfeld-Zollman reverse effect at high temperature: OPEN. Only hint is Zheng: higher temperature plus communication was beneficial; not a test of the reverse effect.
8. Verifier or confidence weighting vs averaging: PARTLY CLOSED for voting. Brown 2024 (d19): voting and reward models plateau (40.50% to 41.41% from 100 to 10,000 samples) while coverage reaches 98.44%. CISC (d18): confidence weighting needs about 41-46% fewer samples. Expert dilution (Pappu) vs these methods: not tested, open.
9. Break-even between voting plateau and one limited-visibility round: OPEN as a number. Evidence points to a design: independent drafts, then one bounded, checked merge (PDR, d12: 76.9 / 81.5 / 86.7). Anchoring on wrong drafts is the risk (d12). No equal-total-token comparison found.

Corrections to note: d16 states the 0.8 similarity as the typical value, not the 79% figure sometimes quoted. Several of these sources use 2023-2024 models; 2026 reasoning models may differ.
