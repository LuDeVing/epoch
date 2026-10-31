# Critique: E12.01 Course-of-action development and analysis

## Checks made (sources re-opened this session)
Re-opened full arXiv PDFs: COA-GPT (2402.01786), Lamparth (2403.03407), Rivera (2401.03408), Shrivastava (2410.13204), COA-Bench (2609.26059), Elbaum and Panter (2508.01056), IFPV (2605.14851), WGSR-Bench (2506.10264), Huang self-correction (2310.01798), Valmeekam o1 (2409.13373), Big-Muddy (2508.01545), Kambhampati LLM-Modulo (2402.01817).

Confirmed exactly: COA-GPT 3.4% gap, 112k battles / 70M timesteps; Lamparth 214 experts, 48 teams, 16/10/9 of 21 actions; Rivera 10 simulations per model, 14 days, 10.15 to 26.02; COA-Bench .516/.498/.490/.485/.479, .920 to .820, .509 [.504,.514], .488/.800, 56%, 76%, .014; Elbaum 6.37/3.96/3.33/4.61/2.76 and 8%; IFPV .72 to .86, 2.28 to 1.33, 19.4%, 41.7%, 31.8%, ACSE 4.00%/1.33%; WGSR 79.9/58.2/21.7, 85.9/37.5, 77.9/85.7/49.1, 92.3/60.0/45.0; Huang table values; Valmeekam 587/600, 317/600, 23.63%, 62.6%; Big-Muddy 99.2%, 46.2% (115/249), 68.95%, 97.45%, N=6,500; LLM-Modulo 12%, 82%, 70%; Shrivastava 0.73 pair.

## Corrections
1. Rivera "+256%": 10.15 to 26.02 is a 2.56x ratio, so +156%. The paper itself says "by 256%". Affects a13, b07, c08. We cite it as 2.56x.
2. Huang debate table (b14): debate round 2 at 6 responses is 83.2; self-consistency at 6 responses is 85.3 (9 responses: 88.2). The "82.5 to 88.2" range in b14 is self-consistency across 3 to 9 responses. Debate does not win at matched counts.
3. Shrivastava (a17): paper says temperature 1.0 for most runs but T=1.05 in one experiment (line 362). Minor.
4. IFPV (c15): the 41.7% is a drop in platform attrition (operational cost) from 2.28 to 1.33, not mission success. Mission success 0.72 to 0.86 compares single-step LLM with the full multi-agent system (MPHA), so the gain mixes several changes.
5. a10 and c12/c13/c14 are one paper (COA-Bench); counted once. a04/a05/b01/b02/b03/c01-c04 are one paper (COA-GPT). b16 and c22 are one paper (Valmeekam). Several "independent sources" counts in evidence lines overstate independence.
6. b21 (Johnson and Raab 2003) is labelled replication; it is a conceptual extension to handball, not a replication of Klein et al. 1995. Also unopened.
7. Provenance warning: COA-Bench arXiv id 2609 and IFPV 2605 are 2026 preprints; neither peer reviewed as far as seen.

## Contradictions
- Debate vs self-consistency: Huang (no gain at matched counts) vs Liang (debate 26.0 to 37.0 on Counter-Intuitive Arithmetic). Different tasks, so not a direct clash.
- Councils: COA-Bench says a role council helps little; Sun et al. (c20) and IFPV say multi-agent planners help. IFPV compares to a single-step LLM, a weaker baseline than best-of-k at equal tokens.
- Option generation: doctrine wants 2+ COAs; the recognition-primed work (unopened) says take the first workable one and more options may hurt. Never tested for LLMs.
- Persona/role prompts: no effect on LLM actions (Lamparth), yet COA-Bench builds role-specialised proposers. Different measures.

## Weak spots
- No source measures COA development vs single plan at equal tokens. Every LLM study here uses a fixed, usually generous, token budget or does not report it.
- COA-GPT: one StarCraft II scenario, 50 rollouts, GPT-4-Turbo, exact means only in figures; casualties worse than baselines.
- COA-Bench is offline and synthetic with a heuristic rubric; the authors themselves found a framing bug.
- Wargame escalation papers measure agent tendencies, not plan quality; scores are LLM-judged or rule-coded.
- WGSR is one benchmark; human groups differ in size and expertise.
- The doctrine itself (FM 5-0, JP 5-0) was never opened; the only doctrine source is a secondary practitioner article.

## Seen only in snippets or from memory (not opened)
a22, a23, a24, b19, b20, b21, b22, b23, b24, b25 (Klein 1986, Klein 1995, Johnson and Raab, Thunholm, Pounds and Fallesen, Mitchell, Schwenk, Cheikes). Their numbers (156 decisions, 80%, 30% more reasons) are from memory and must not be cited. c19 (Mil-SCORE) and c20 (Sun) have garbled tables; c24 Kader and Lee only abstract-level.

## GAPS
1. At equal tokens, does generating 3 distinct COAs and comparing them beat one plan plus a self-check, or best-of-N sampling, on any measured planning task? (Core decision for the schema; no source tests it.)
2. Does adversarial wargaming against a simulated or LLM opponent beat static LLM ranking when the opponent is not fine-tuned? (IFPV used a fine-tuned world model; COA-Bench is synthetic.)
3. What is the real size of the recognition-primed finding (Klein 1986: N commanders, share of single-option decisions) and the "first option is best" result (Klein 1995, Johnson and Raab 2003)? Open the originals.
4. Does the doctrinal five-test screen (feasible, acceptable, suitable, distinguishable, complete), or its equivalent, change outcomes? Is there any validity data in FM 5-0, JP 5-0 or ARI reports (Pounds and Fallesen; Thunholm)?
5. Does a premortem or devil's advocate step improve LLM plans (Mitchell 1989, Schwenk 1990 originals; any 2023-2026 LLM test)?
6. Does enemy-course-of-action modelling ("most likely" and "most dangerous") improve a plan, and can an LLM opponent model reach human level (WGSR gap near 30 to 40 points)?
7. How much does candidate diversity matter: do LLM-generated COAs collapse to near-duplicates, and does forced diversity (GenCOA-style pools) raise final success?
8. Do the LLM wargame biases (escalation, harmonious dialog, persona insensitivity) carry over to plan-selection tasks that are not geopolitical?
9. Can an LLM adjudicate (judge outcome of a COA against an enemy move) reliably enough to replace a simulator? Matlin finds only 20 of 223 studies try it.
10. Are there replications of COA-GPT, or other LLM COA-generation results on different simulators, with token cost reported?


## Gap search results

Date: 2026-10-31. New evidence: evidence_d.jsonl (d01 to d20). Claims updated: K01, K25, K27, K28; added K30 to K36.

Opened this pass: Klein 1986 abstract (Crossref), Mitchell 1989 abstract (Crossref), Raab et al. 2026 chess replication (full PDF), Ross/Klein/Thunholm 2004 Military Review (full), Peabody 2017 thesis abstract, and full arXiv texts for InvThink, anticipatory reflection, conformity, Ke et al., PlanSearch, Snell et al., Wang et al. world simulators, SAP, SPIN-Bench, BiasBuster. Not opened (paywall or 403): Klein 1995, Johnson and Raab 2003, Schwenk 1990, Klein 1986 full text, DTIC ARI-TR-796, Thunholm primary, Pounds and Fallesen, Cheikes.

1. Equal-token test of 3 COAs vs plan plus self-check vs best-of-N: OPEN. No source tests it. Nearest are Snell (revision wins on easy problems, parallel or tree search on hard ones) and PlanSearch (diverse plans beat resampling). New claim K30.
2. Adversarial wargaming with a non-fine-tuned opponent vs static ranking: OPEN. SAP used a trained evaluation network (K34). No prompted-opponent test found.
3. Real size of the recognition-primed and first-option findings: PARTLY CLOSED. Klein 1986 abstract: comparison in under 12% of decision points. The commonly quoted 80% is per incident from a trade article (different unit). N=26 and 156 decision points are secondary only. Klein 1995 and Johnson and Raab 2003 could not be opened. A 2026 replication (N=92) found no clear first-option edge at lower ratings (F(3,992)=1.73, p=.159). K27 rewritten.
4. Validity of the five-test screen: OPEN. No validity data in anything opened. The Military Review article says research support is weak for the multi-COA assumption (K36). Pounds and Fallesen and the ARI reports are still unopened.
5. Premortem or devil's advocate for LLM plans: PARTLY CLOSED. Mitchell 1989 abstract does not contain the quoted 30% gain, so do not cite it. Human premortem data is a small thesis. LLM tests are indirect (InvThink, anticipatory reflection, conformity); none tests plan quality with a premortem vs a plain risk prompt at equal tokens. K28 rewritten.
6. Enemy "most likely / most dangerous" modelling and LLM opponent level: OPEN. Structured opponent modules help (K34); LLMs are weak at look-ahead against engines.
7. Candidate diversity: PARTLY CLOSED. PlanSearch gives measured evidence that near-duplicate candidates cap search gains, with a verifier (K31). Not shown for COAs.
8. Bias carry-over: PARTLY CLOSED. Framing and anchoring biases carry to admissions decisions (K33). Escalation and harmonious-dialog carry-over to plan selection untested. The conformity paper explains harmonious agreement and shows one dissenter reduces it.
9. LLM adjudication replacing a simulator: CLOSED toward no. GPT-4 59.9% on non-trivial transitions, errors compound (K32). Newer models untested.
10. COA-GPT replications and token cost: OPEN. None found, no token cost. Citation APIs were rate-limited, so the citing list is incomplete (K35).

Corrections to earlier lines: the Mitchell '30%' and Klein '80%' numbers in memory are unverified; use the units given above.
