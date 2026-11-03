# Critique: C09.04 Hitting-set tree search (cross-check)

## Corrections made (numbers re-opened this session)
Confirmed against the source text: Greiner et al. 1989 counterexample {{a,b},{b,c},{a,c},{b,d},{b}} loses {a,b} (PDF text, Figure 1, "interaction of the pruning rule ... and the closing rules"); DynamicHS 99.4% of scenarios, median/max saving 52%/75%, HS-Tree up to 4x average time (arXiv 2012.11078); hard reasoner calls "at least four times and up to more than 100 times" costlier (matches a12); Sztyber-Betley et al. DX 2025: o3-mini F1 0.917 +/- 0.249 (conflicts) and 0.784 +/- 0.322 (diagnoses), 10 repeats for 4o-mini and o3-mini, o1 once, "one iteration cost around 30$", authors say LLMs "do not provide an alternative to diagnosis algorithms"; survey (arXiv 1601.02939): HER2+.SHORT 122 elements, 534 sets, 128,833,310 minimal hitting sets, MHS2 2.33x parallel gain, 3600 s limit.
Corrections / notes:
1. a03 and b06 point to arXiv 1601.02939, which is the Gainer-Dewar survey, not the Greiner paper. a03 is correctly flagged as survey-derived; the Greiner paper itself was opened under b01 (cse.sc.edu PDF). Treat a03 as secondary.
2. Another DynamicHS passage says hard calls are a median of 19x and up to 120x costlier than easy calls; a12 gives "at least 4x, up to over 100x". Both appear in the same paper family (different sections/versions); do not quote one number without the other.
3. Evidence lines a10/b15, a11/b16/c07, a13/b18, a17/b21/b22, a18/b19/b20/c01-c05 are duplicates of the same papers. Independent sources in claims.jsonl were counted by paper, not by line. The DynamicHS and LLM-pipeline claims are therefore single-source.
4. b01/c20 vs a03: a03 says Greiner trigger is non-minimal conflicts; b01 (opened) confirms this. c20 was "background knowledge, not opened" but is consistent. Use b01.
5. c18 "76.0% at least one correct service" came from a search summary; only the 14.5 pp gap was seen in text. Not used in a claim number.
6. b24 and c26 are the same Delta1 paper; only the first page was read.

## Contradictions between sources
- MergeXplain gain: up to 54% (a13, CSP and spreadsheets) vs 15% to 45% (b18, DXC synthetic) vs slight losses (-5% to -11%) when one conflict exists. Not a contradiction, a range by problem type.
- HST vs HS-DAG: Wotawa's variant is faster for size-1 hitting sets, slower and more memory-hungry for disjoint conflicts above about 20 components (a05) and loses at size 3 (b09). Result depends on cardinality bound and Python implementation.
- Tree search vs rivals: a06/b06 say Reiter-style trees are far from fastest; b10 argues they are kept because they allow on-the-fly conflict computation. Different goals, not conflict.
- Prompt knowledge: c04 says domain knowledge did not help conflict generation; c17 says hypothesis-driven prompts widened coverage but not accuracy. Consistent: prompts change breadth, not correctness.

## Weak spots
- No source tests a tree/DAG search inside an LLM. Everything about our agent is by analogy (K01-K03 are the transferable core).
- The only LLM-pipeline test (DX 2025) gave each step the gold output of the previous step, used tiny hand-built circuits, OpenAI models only, and put the hitting-set algorithm in the prompt as pseudo-code.
- DX 2026 study (Plank and Wotawa): manual scoring by the authors, own weights, free models only, no hitting-set method.
- DynamicHS, RBF-HS and Inv-HS-Tree are all from one research group (Rodler, Shchekotykhin, Friedrich), on ontology debugging with random fault probabilities. No outside replication seen.
- Benchmarks of hitting-set speed (a06, a08) use pre-computed conflicts or non-diagnosis data; neither measures conflict-finding cost, which dominates in practice.
- RCA evidence (c14 to c18) is about telemetry agents, not about hitting sets; it is only relevant to the "symptom vs cause" suspect-selection weakness.

## Seen only in snippets or second-hand
Reiter 1987 (read via Wassermann, Greiner and Rodler restatements), Wotawa 2001 (403), GDE 1987, Lin and Jiang 2003, Staccato, Pill 2011 (a09), Grastien et al. 2023 (b25), AgentLocate and the TU Delft thesis (b26, b27), Stern et al. 2012, SAFARI, SIR-M, SafeMin 42.1% figure (c25, snippet, unverified), Delta1 (first page).

## GAPS (most decision-relevant first)
1. Does an LLM that is told to reopen pruned suspect sets when a later, smaller contradiction appears (HS-DAG rule) keep more valid minimal diagnoses than one that prunes early? No measurement exists.
2. When the agent writes its own contradictions, how often are they non-minimal (supersets of earlier ones)? This is the trigger for the Greiner bug and is untested for LLM output.
3. At equal tokens, does offloading the exact minimal-hitting-set step to a code tool beat the LLM doing it in-context, and where does LLM accuracy break (DX 2025 shows decline toward 165 diagnoses, but with gold inputs)?
4. Does a size cap (single, double, triple faults) on the suspect list improve end accuracy for LLM agents, as it does for HS-DAG and HST runtime?
5. Does carrying and editing the suspect list across probes (DynamicHS idea) beat restating it each turn for an LLM agent, and does it replicate outside the Rodler group?
6. Do 2026 multi-agent failure-attribution papers (AgentLocate, TU Delft thesis) use or beat a hitting-set style formulation? Only snippets were seen.
7. Conflict-then-hit versus direct candidate generation (SAT or Inv-HS-Tree style): which maps better to an LLM, which finds contradictions poorly (b23)?
8. Is there any 2024-2026 neuro-symbolic work using MARCO/MUS enumeration plus hitting sets as an LLM verifier (SafeMin figure needs checking)?
9. Which probe-selection rule (entropy, split-in-half, most probable singleton) helps an LLM choose the next test, given LLMs cannot compute entropy reliably?

## Gap search results (2026-11-03)
Search APIs (arXiv export, Semantic Scholar, OpenAlex) were rate-limited this session; 6 WebSearch calls plus direct PDF reads were used. Evidence is in evidence_d.jsonl (d01 to d18); claims K23 to K29 added.

1. Reopen pruned suspects (HS-DAG rule) in an LLM: STAYS OPEN. No measurement found (d17). Related: Waterloo RCA study names anchoring and failure to update belief as top predictors of wrong answers (d13), so the rule targets a real failure, but is untested.
2. How often LLM-written contradictions are non-minimal: STAYS OPEN. Negative search (d15). Replay-based conflicts are unstable per AgentLocate authors (d18), a hint that they are often wrong or non-minimal. Needs our own solver-checked test.
3. Code tool vs in-context hitting set at equal tokens: STAYS OPEN, partly informed. DX 2025 has only one tool arm, and it was the weakest model and worst (d07). F1 on diagnoses falls with size even with gold conflicts (d08). No head-to-head (d09). Claim K26 marked open.
4. Size cap on suspects for LLM agents: STAYS OPEN. RCA work assumes single fault (d13); D-Bot says multi-cause is hard (d14), no controlled test. K28 open.
5. Carried vs restated suspect list; DynamicHS replication outside the Rodler group: STAYS OPEN (d17).
6. AgentLocate, TU Delft thesis and hitting sets: CLOSED for AgentLocate and Famas (read in full): neither uses a hitting set (d01, d03, d04). AgentLocate is propose-then-verify, 3 evaluators lift agent-level accuracy 35.71% to 69.05% (d02); Famas is spectrum counting, 29.35% action-level (d03). TU Delft thesis not found again; still unresolved.
7. Conflict-then-hit vs direct generation for an LLM: STAYS OPEN. No LLM data. The attribution papers (AgentLocate, Famas) both skip conflict sets and go direct to a ranked or verified suspect, which is weak indirect support for direct generation.
8. MARCO/MUS plus hitting sets as an LLM verifier: MOSTLY CLOSED as "not found". Delta1-LLM builds MUS by construction (d05); HyMUSE is a learned chooser for MARCO, not an LLM (d06). SafeMin 42.1% not re-found, still unverified (d16).
9. Probe-selection rule for an LLM: PARTLY CLOSED. UoT (d10 to d12) computes entropy in code from candidate-set sizes the LLM simulates; +38.1% mean success over direct prompting, 97.0% DX, 67.3% vs 43.7% troubleshooting; reward form matters little. No head-to-head of entropy vs split-in-half vs most-probable-singleton for LLMs. K27 single-source.
