# Working-memory-limited mapping: deep document

*Subfield C10.07. Sources: evidence_a to d.jsonl (ids a01 to d17), claims.jsonl (K01 to K24), critique.md. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Human numbers are from one lab (Holyoak group) unless stated. The subfield's named key work, Keane and Brayshaw 1988, was never opened; see section 5.*

## 1. What it is

Analogical mapping aligns a base situation with a target. It pairs objects, relations and roles so that the structure matches. "Working-memory-limited mapping" is the family of theories that say this alignment is bounded by a small working memory. The mapper cannot hold the whole match at once. It builds the match in small pieces, one after another, and extends it.

Three kinds of claim sit under the name:

- **Serial, incremental mapping.** The mapper takes a seed group of base facts, builds one interpretation, and backtracks if it fails. Input order then changes the result. The model is IAM (Keane and Brayshaw 1988).
- **Capacity-limited binding.** Only a few role-filler bindings can be active at the same time. The models are LISA (Hummel and Holyoak 1997) and relational complexity (Halford, Wilson, Phillips 1998, about four related variables).
- **Load effects in people.** A memory or attention load makes people drop relational matches and take surface (attribute) matches. This is the best-measured part (Waltz et al. 2000; Tohill and Holyoak 2000).

For our agent the question is narrow. Does an LLM show a comparable limit when it maps? And do small mapping steps, an external binding table, distractor removal or a code tool raise accuracy at equal tokens? The honest answer today: the human load effect is solid but from one lab. LLM data are indirect proxies. No study tests a mapping-size cap on an LLM (K21).

## 2. History and theories in depth

**Parallel versus serial.** Structure-mapping engines such as SME build all local matches first and then merge them into global mappings. In the Keane, Ledgeway, Duff report SME returns all 32 mappings for the attribute-mapping problem in every condition (d02). ACME (constraint satisfaction network) settles in parallel. IAM is serial. It picks the group of base predicates with the most higher-order connectivity as a seed, maps that group, then extends, and backtracks if it fails (d01). IAM also carries "behavioural" constraints (a working-memory limit, background knowledge) that the other two lack. IAM does not use a fixed relation-count cap (d05). Its serial order comes from a first-encountered tie-break.

**Keane, Ledgeway, Duff 1994** (read from the 1993 technical report, a revised preprint, not the journal text; d01 to d05). Two human experiments, both with tiny cells and no replication:

- Similarity: time to a correct mapping fell as attribute similarity rose. 210.9 s, 164.9 s, 69.7 s, F(2,12)=12.02, p<.01. N=21, 7 per cell, between subjects. ACME and IAM predicted this, SME did not.
- Order: Singleton-First 178.0 s versus Singleton-Last 363.1 s, Mann-Whitney U=7, p<.005 one-tailed. N=20, 10 per cell. IAM predicted it (model: 1 versus 2.9 mappings needed, t(18)=-4.67). SME and ACME predict no order effect.

**Capacity accounts.** Halford et al. say difficulty tracks relational complexity, the number of unique relations processed in parallel, about four for adults. Hummel and Holyoak say binding is by time. Only a few role-filler pairs can fire out of phase, so the limit falls out of the architecture. Waltz et al. 2000 cite both for the prediction that any capacity cut should shift mapping from relations to attributes (a05). Cowan (2010) puts the core store at 3 to 5 chunks when rehearsal and chunking are blocked (a09). Neither Halford 1998, Hummel and Holyoak 1997/2003, nor Cowan 2001 was opened here. Their content is from memory and from how others cite them.

**Rival accounts.** Chuderski (2022) says fluid reasoning depends on valid, robust role-filler bindings, not on how many relations fit at once (b21). Richland and Morrison (2010) and Doumas, Morrison, Richland (2018) stress inhibition of featural distractors and lateral inhibition in DORA/LISA (b23, b24). So the limit may be count, binding quality or interference control. This is unresolved [C] (K06).

**Neural link.** Waltz et al. 1999 (prefrontal patients worse once two relations must be integrated) was not opened; memory only (a30).

**Related subfields covered elsewhere in this run.** Constraint satisfaction; Cognitive load (Germane load, Measurement of load); Dual-process accounts; Working memory training transfer. Linked, not covered here.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Verbal 7-digit load cuts relational mapping on cross-mapped pictures | .35 load vs .64 no load, F(1,41)=12.48, p<.01. N=45, 2x2 between subjects | Waltz et al. 2000 Exp 1 (a01, b01) | [S] one lab; reopened and confirmed |
| Asking for 3 mappings at once raises relational mapping | .60 vs .39, F(1,41)=6.64, p<.05; no load x instruction interaction (F<1) | Waltz 2000 Exp 1 (a01) | [S] |
| Failures under load are attribute matches, not noise | 7.5% of mappings neither relational nor attribute (Exp 1); 5% (Exp 2); full digit recall about .50 | Waltz 2000 (a02, b03) | [S] |
| Phonological and executive loads both hurt, equally | No load .45 vs loads .24, F(1,103)=23.70; phonological .23 vs random-digit .25, F<1. N=109; 3-map .37 vs 1-map .25, F(1,103)=9.61 | Waltz 2000 Exp 2 (a03, a04) | [S] |
| Induced anxiety cuts relational mapping | Exp 1 N=22: 45% vs 68%, F(1,20)=5.78, p=.026; attribute 51% vs 24%. Exp 2 N=22 with relational instruction: 72% vs 84%, F(1,20)=5.09, p=.04 | Tohill and Holyoak 2000 (a06, a07) | [S] small N; not re-opened |
| Core capacity is 3 to 5 chunks | verbal chunks recalled 3 or 4; groups of about 3.5 search best | Cowan 2010 (a09) | [S] review; slot vs resource debated |
| Order of base items changes human mapping time | 178.0 s vs 363.1 s, U=7, p<.005 (one-tailed), N=20 | Keane et al. 1994 TR (d04) | [S] tiny cells |
| Similarity speeds human mapping | 210.9 / 164.9 / 69.7 s, F(2,12)=12.02, N=21 | Keane et al. 1994 TR (d03) | [S] tiny cells |
| Working-memory training does not transfer to analogy | Trained tasks d=1.93 to 3.16; verbal analogy .55 to .54, d=0.10 (N=25 trained, 29 control); visual analogy .77 vs .76, d=0.05 | Richey et al. 2014 (b04, b05) | [S] small N, not re-opened this session |
| WM correlates with analogy | Kyllonen and Christal 1990 (N=399): digit span r about .30 to .40; secondhand | Richey 2014 review (b06) | [S] correlational |
| GPT-3 matched or beat students on digit matrices | N=40. Generative OR 1.88 [1.21, 2.91]; multiple choice OR 6.27 [3.28, 11.99]; item profile r(30)=0.39 | Webb, Holyoak, Lu 2023 (a13, c05) | [C] training overlap; reopened |
| Difficulty rises with distinct rules, in people and GPT-3 | Progression vs none: GPT-3 OR 0.07, humans OR 0.41 | Webb 2023 (c06) | [S] not proof of a bottleneck |
| GPT-3 letter strings: beats humans overall, falls with generalisations | OR 1.76 [1.34, 2.31]; per extra generalisation OR 0.51; story analogies humans better OR 0.37 | Webb 2023 (a14) | [C] |
| Counterfactual letter strings collapse GPT-3 | Generative accuracy under 0.1 on 4 of 6 problem types; comprehension check stays at 30% or more of original | Hodel and West 2023 (c08, a20) | [E] with Lewis and Mitchell |
| Humans beat GPT on counterfactual letter strings | Overall: humans .753 [.734, .773] (134 kept of 136 recruited); GPT-3 .488; GPT-3.5 .350; GPT-4 .452 | Lewis and Mitchell 2024 (b09) | [E] |
| Code execution closes most of the gap | Humans N=99/97. GPT-4 vs humans P=8.9e-13; GPT-4+code vs humans P=0.496. Interval effect P=0.066 with code | Webb et al. 2024 (a16, b11) | [S] one lab, one task |
| Error types differ | Alternative valid rule: GPT-3 5.81%, GPT-4 22.00%, humans 38.59%; incorrect rule 30.97 / 32.67 / 14.67%. Webb reply: 46% (23/50) of GPT-4 errors vs 39% of human errors valid alternatives | Lewis and Mitchell; Webb 2024 (a17, a19) | [C] |
| Story-answer order bias in GPT-4, none in humans | GPT-4 89% (16/18) correct-first vs 61% (11/18) second; humans 78% both | Lewis and Mitchell 2024b (d06) | [S] 2023 models, small n |
| LLM n-back limit | gpt-3.5-turbo d' about 1 at 3-back; noise variant lower; CoT helps; GPT-4 far above 7 small open models | Gong, Wan, Wang (arXiv 2305.03731, v4 2024; one paper) (a10 to a12) | [S] proxy task |
| Scale does not remove n-back limit | 7 OpenAI models below human; BBH category ii GPT-3.5: 44.4% answer-only vs 67.6% advanced prompts mean; small models lose with advanced prompts. GPT-4 answer-only is 72.8, so the gain vanishes | Zhang et al. 2024 EMNLP (b16 to b18) | [S] |
| Reasoning models collapse on long noisy Raven items | o3-mini 86.6% to 17.0%; R1 80.6% to 23.2%; chance 12.5%; 3.4x more reasoning tokens | Camposampiero et al. 2025 (d07) | [S] early-2025 models |
| Operand/rule length hurts LLMs most | Arithmetic accuracy: reasoning models 80.5% to 63.0%; LLMs 59.3% to 4.4% | I-RAVEN-X (d08) | [S] |
| One irrelevant sentence cuts math accuracy | code-davinci-002: under 30% of base problems consistently solved with distractors | Shi et al. 2023 (d09) | [S] math, 2023 model |
| Input length alone hurts | Mean accuracy 0.92 (250 tokens) to 0.68 (3000 tokens), task fixed | Levy, Jacoby, Goldberg 2024 (d10) | [S] not analogy |
| Distractor condition hurts humans and LLMs | About -0.25 for all four subject types | Musker et al. 2025 (a21, c18) | [S] |
| Newer models strong on simple relations, weaker on analogy | Same/different: GPT OSS 120B 99.8%, Llama 3.1 405B 83.2%; analogy block GPT OSS about 83%, Llama near chance; 1 to 5 premises barely hurt | Raemaekers et al. 2025 (b19, b20) | [S] 4 models, no human baseline |
| Frontier late-2025 models below humans on far-analogy grids | Humans 68.96% (58.35% strict). GPT 5.2 51.20/48.33; Gemini 3 Pro 43.06/29.19; Claude Opus 4.5 8.61/7.18; best 10.13 points under humans (strict) | ARCANA (d14) | [S] no code tool; union over 12 attempts for models |
| Models hold entity-attribute binding vectors | Over 97% with joint entity and attribute interventions; tested n=2, 3 | Feng and Steinhardt 2024 (d12) | [S] mechanism, not analogy |
| Self-generated analogs help big models | GSM8K GPT-3.5 75.0 to 75.8-77.8; text-davinci-003 14.8 to 50.3-61.0; MATH 33.0 to 33.9-37.3. With self-consistency 77.8 to 85.3 | Yasunaga et al. 2024 (c16, d17) | [S] more output tokens; no equal-token run |
| Relational-bottleneck networks generalise | ESBN 95%+ rule generalisation; Slot Abstractor V-PROM 67.7 vs 51.2 | Webb 2021; Mondal 2024 (c19, c20) | [S] trained models |

## 4. Mechanisms and models

Written so an engineer can build each one. None of these has been shown to improve an LLM at equal tokens.

**A. Serial seed-and-extend mapper (IAM style).**
1. Score base predicates by higher-order connectivity (count of nested relations they head).
2. Pick the top group as the seed. Break ties by the first one met.
3. Map seed predicates to target predicates, matching relation names and argument roles. Keep one interpretation.
4. Extend to neighbours of mapped items. Check one-to-one consistency in code.
5. If a clash appears, backtrack to the last choice and try the next.
6. Stop when the base is covered or the budget ends. Order of base items affects the result (178.0 vs 363.1 s in people), so run two orders and compare.

**B. Capacity-capped batches (LISA / Halford style).** Chunk the correspondences into groups of 3 to 4 (Cowan, Halford). Map one group per model call. Carry forward only the finished bindings in a table, not the prose. The cap is a design guess. IAM has no fixed cap, and no LLM test of a cap exists.

**C. Explicit role-filler binding table (Chuderski, ESBN style).** Keep a table in code: rows are relation roles, columns are base filler and target filler. Each model call reads and writes only the rows it names. Code checks that each filler is used once. This mirrors the relational bottleneck in ESBN and Slot Abstractors, where binding memory is kept apart from content.

**D. Joint mapping prompt.** Ask for all pairs at once ("map all three objects") rather than one pair. In people this raised relational answers .39 to .60 (Exp 1) and .25 to .37 (Exp 2) (a01, a03). LLM effect unknown.

**E. Distractor pruning.** Remove or mark any base or target content not needed for the mapping before the map step. Evidence: load and distractors shift people to attribute matches; LLM math and length results (d09, d10) agree in direction.

**F. Tool offload.** Do counting, index and position work in code and leave relations to the model. Webb 2024 reached human level with code on shuffled alphabets (P=0.496).

**G. Scoring rule.** Score by relational versus attribute match and by structure, not one answer key. 46% of GPT-4 errors and 39% of human errors were valid alternative rules.

**H. Two-order check.** Run candidates and base items in two orders (answer-order bias: 89% vs 61%). Disagreement flags an unreliable mapping.

## 5. What holds up

**Holds up.**
- Load shifts people from relational to attribute mapping. Two papers from one lab (Waltz 2000, N=45 and N=109; Tohill and Holyoak 2000, N=22 and 22). Related human work on relational matching under load (d16) and distraction (d15) points the same way but was seen as abstracts only, so it is not a replication (K24).
- Counterfactual letter-string fragility of GPT-3 to GPT-4. Hodel and West and two Lewis and Mitchell papers agree.
- Counting and position bookkeeping explains much of that failure (Webb 2024), though only for counting.
- Distractors and input length hurt LLM reasoning (d09, d10, d07). Not yet shown on mapping scored relational versus attribute.

**Failed, mixed or missing.**
- No independent replication of Waltz 2000 or Tohill and Holyoak 2000. Waltz cells are between subjects and small.
- Keane et al. 1994 rests on 7 to 10 per cell; one-tailed test; one task. No replication found. Keane and Brayshaw 1988 itself was never opened.
- Storage versus executive source of the limit cannot be separated in people (phonological and random-digit loads equal) (K02).
- Training working memory raised trained tasks (d up to 3.16) and left analogy flat (d=0.10, d=0.05) (Richey 2014). The causal link from WM to analogy is not proven [C].
- Webb 2023 versus Lewis and Mitchell disagree on humans versus GPT. Causes: their humans scored higher, the prompt listed the alphabet, and counting failures were fixed by code. Webb 2024 says no alphabet effect between original and synthetic alphabets (with code). Hodel/West and Lewis/Mitchell see collapse without code. Conditions differ.
- Capacity count versus binding quality versus inhibition: unresolved.

**Moderators.** Cross-mapped items (force a relation-versus-attribute choice). Instruction to match relations (shrinks the gap from 23 to 12 points, does not close it). Similarity (speeds mapping). Item order. Model size (small models lose with heavy prompts). Code access.

**Interventions that worked (single-source each).** Code offload (Webb 2024). Chain of thought on n-back (Gong). Advanced prompts on mid-size models (Zhang, BBH category ii GPT-3.5). Self-generated analogs on GPT-3.5, davinci and PaLM2 (Yasunaga). Language encoding choice for Raven items (Hu et al.: about 14% to 95.6% by configuration).

**Did not work.** Working-memory training for analogy (people). Newer chat models on counterfactual letter strings (GPT-3.5 .350 below GPT-3 .488). Heavy prompts on small models. Reasoning tokens on long noisy items (3.4x more tokens, 17.0%). Advanced prompts at GPT-4 level (gain gone: 72.8 answer-only).

**Corrections carried from critique.** Lewis and Mitchell human N is 136 recruited, 134 kept (not 46). Webb authors are Webb, Holyoak, Lu. Hodel and West's "at least 30%" refers to the counterfactual comprehension check, not task accuracy. Gong et al. is one paper, counted once. Yasunaga Codeforces ablation numbers (c25) are unverified and left out of the table.

## 6. Language models

**Capacity proxies.** gpt-3.5-turbo shows d' about 1 at 3-back; noise lowers capacity; CoT raises it; GPT-4 is far higher but was not tested beyond n=3; seven open 6B to 13B models were all very low (a10 to a12). Across seven OpenAI models n-back stayed under human level (Zhang). n-back is a rough measure of complex WM (Jaeggi 2010, as cited by Zhang). It is not a mapping test.

**Analogy tasks, 2023 models.** GPT-3 beat students on digit matrices (OR 1.88 / 6.27, N=40) and on verbal and story analogies in familiar formats. On counterfactual letter strings GPT-3 fell under 0.1 (generative) on 4 of 6 types; across all alphabets Lewis and Mitchell found humans .753 vs GPT-4 .452. GPT-4 with code reached human level (P=0.496). Story answers show an order bias (89% vs 61%). Digit matrices with a moved blank dropped GPT from about .81 to .48 (row assignment inferred from scrambled table text, d06).

**Newer models.** GPT OSS 120B 99.8% on same/different, about 83% on analogy; Llama near chance (Raemaekers 2025). o3-mini and R1 fell to 17.0% and 23.2% on long noisy Raven-style items despite 3.4x more reasoning tokens (d07, d08). On ARCANA far-analogy grids, with no code, GPT 5.2 reached 48.33 strict, Gemini 3 Pro 29.19, Claude Opus 4.5 7.18, humans 58.35 strict (d14). No 2025-2026 rerun of counterfactual letter strings was found.

**What changed results, by how much.**

| Change | Effect | Source |
|---|---|---|
| Code execution (GPT-4, letter strings) | from clearly worse than humans (P=8.9e-13) to no difference (P=0.496) | Webb 2024 |
| Chain of thought (gpt-3.5 n-back) | "significantly improved"; no number recorded | Gong |
| Advanced prompts (GPT-3.5, BBH cat. ii) | 44.4% to 67.6% | Zhang |
| Same prompts on GPT-4 | answer-only 72.8; gain gone | critique |
| Self-generated analogs | GSM8K +0.8 to +2.8 (GPT-3.5); about +35 to +46 (davinci); MATH +0.9 to +4.3 | Yasunaga |
| Self-consistency on top | GSM8K 77.8 to 85.3; MATH 37.3 to 46.0 (extra samples, not token-matched) | Yasunaga (d17) |
| Alphabet listed in prompt | best format across models; lift not extracted | Hodel and West |
| Distractor sentence (math) | under 30% consistently solved | Shi |
| Padding 250 to 3000 tokens | 0.92 to 0.68 | Levy |
| Ten confounders (Raven items) | o3-mini -11.2 task points; R1 -5.8 | I-RAVEN-X |

**Mechanism hints.** Open models carry binding ID vectors (over 97% with joint interventions, n=2 and 3) (Feng and Steinhardt). Analogy information sits in mid-upper layers when the model succeeds and is absent when it fails (Lee 2025, abstract only). No test of a cap at n of 4 or more.

**Does this show a human-like bottleneck?** No. Difficulty rises with rule count in both people and GPT-3, which is the load signature, but the cause in the model is unknown. Webb itself says the mechanism may differ from the human one.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Clutter degrades relational answers: strip irrelevant content from the context before the O7 map step (extends S1 input hygiene to the analogy step) | S1 / O7 | [E] for the human effect (Waltz and Tohill, 2 sources) and for LLM distraction cost (Musker, Shi, Levy); no LLM mapping test | a01 to a07, a21, d09, d10 (K01, K19) |
| A2 | Do not trust surface fit: test any analogy success on a counterfactual or novel-symbol variant (already G3; add the counterfactual check to O7 evaluation) | G3 / O7 | [E] | a18, b08, b09, c08 (K09) |

Honest note: A1 rests on human data from one lab plus indirect LLM proxies. It enters as a hygiene step because it is cheap and consistent with G11. Under rule 8.2 any further element enters as [S] with a test.

### Test first (single-source or contested)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Cap correspondences per map call at 3 to 4 | O7 | [S] human count only (Cowan; Halford unopened); no LLM test (K21) | a09, d08 (K04, K21) |
| T2 | Explicit role-filler binding table kept in code | memory / G | [C] count vs binding vs inhibition | b21, d12, c19, c20 (K06, K16, K22) |
| T3 | Joint mapping prompt (all pairs at once) | O7 | [S] human only | a01, a03 (K03) |
| T4 | Code tool for counting and position work | O | [S] | a16, b11 (K10) |
| T5 | Two-order check on candidates and base items | G | [S] | d04, d06 (K17, K20) |
| T6 | Self-generated analog step before solving | O7 | [S] needs strong model, not token-matched | a22, c16, d17 (K13, K23) |
| T7 | Score by structure, accept valid alternative rules | G | [C] | a17, a19 (K09) |
| T8 | Recap or rehearsal cue for long item lists | S2 | [S] | b17 (K12) |
| T9 | Scale prompt weight to model strength | S0 | [S] small models lose | b16, b18 (K12) |

Do not take: any claim that working-memory training would help the agent; any use of IAM numbers as capacity numbers.

## 8. Concrete tests on our bench

All arms run at equal total tokens (generation cost counted, G7). Report relational and attribute scores, not one key.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| 1 | Cross-mapped pair mapping items (Markman and Gentner style, text form), 60 items | plain vs filler-heavy vs trimmed context | relational proportion; attribute proportion | filler lowers relational share; trimmed recovers part; size unknown |
| 2 | Same items, 3 to 8 correspondences needed | uncapped vs 3 to 4 per call vs binding table | relational accuracy; one-to-one violations | cap or table helps at 5+ correspondences, none at 2 to 3 |
| 3 | Single-pair vs joint-mapping prompt on cross-mapped pairs | A/B | relational share | joint higher, as in people (.39 to .60); maybe smaller in LLMs |
| 4 | Counterfactual letter strings (shuffled alphabet, symbols), 100 items | plain vs code tool vs listed alphabet | accuracy; alternative-valid-rule share | code closes most of the gap, as in Webb |
| 5 | Story analogies, both candidate orders | single order vs two-order agreement | accuracy; flip rate | position bias (89 vs 61 on GPT-4) may persist on ours |
| 6 | Long noisy Raven-style items | plain vs pruning step | accuracy | pruning recovers part of a 17% floor |
| 7 | Analogy items needing a far source | self-generated analog vs none (token-matched with longer plain CoT) | accuracy | small gain on a strong model; gone at equal tokens is plausible |
| 8 | Order shuffle of base items | order 1 vs order 2 | accuracy | an order effect appears only if the model works serially |

## 9. What does not transfer, and why

- **Human capacity numbers (3 to 5 chunks).** An LLM has no rehearsal buffer. Its limit is attention over context, and the n-back proxy is rough.
- **Digit-load dual task.** There is no secondary task to run in parallel in a single forward pass. Filler context is the nearest analogue and is a different mechanism.
- **Anxiety.** No counterpart in the model.
- **WM training.** Not applicable. The null result warns only that more capacity may not mean better mapping.
- **IAM order effects as a capacity proof.** The effect comes from a first-met tie-break (d05), not a slot count.
- **n-back as a mapping test.** It measures hold and update, not alignment.
- **Code offload as human-like.** The authors say it is not. For our agent that does not matter, since we want accuracy.
- **Self-generated analogs as serial mapping.** This is retrieval of examples, a sibling idea (a22).

## 10. Open questions

1. What do Keane and Brayshaw 1988 and the journal version of Keane 1994 report? Not opened.
2. Does a 3 to 4 relation cap per step beat no cap at equal tokens (K21)? Untested.
3. Do 2025-2026 frontier and reasoning models still fail counterfactual letter strings, with and without code?
4. Does a joint mapping prompt raise relational answers in LLMs?
5. Is there an independent, larger-N replication of Waltz 2000 or Tohill and Holyoak 2000?
6. Does context length or distractor load shift LLM mapping from relational to attribute, as in people?
7. Does an explicit binding table beat a count cap?
8. Which structured-prompt gains (Yasunaga, Zhang) survive at equal tokens?
9. Is the code-offload fix general beyond counting?
10. Is the human limit count, binding or inhibition, and which is it in models?
11. Is there a cap at 4 or more entities in the internal binding mechanism?

## 11. Sources

[V] opened, [M] snippet or abstract only.

- [V] Waltz, Lau, Grewal, Holyoak (2000) The role of working memory in analogical mapping. https://link.springer.com/content/pdf/10.3758/BF03211821.pdf
- [V] Tohill and Holyoak (2000) The impact of anxiety on analogical reasoning. https://sites.lifesci.ucla.edu/psych-reasoninglab/wp-content/uploads/sites/273/2021/04/Tohill_Holyoak.2000.pdf
- [V] Cowan (2010) The magical mystery four. https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/
- [V] Gong, Wan, Wang (2023/2024) Working memory capacity of ChatGPT. https://arxiv.org/abs/2305.03731
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196
- [V] Webb, Holyoak, Lu (2024/2025) Evidence from counterfactual tasks supports emergent analogical reasoning in LLMs. https://arxiv.org/abs/2404.13070
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning in LLMs. https://arxiv.org/abs/2402.08955
- [V] Lewis and Mitchell (2024) Evaluating the robustness of analogical reasoning in LLMs. https://arxiv.org/abs/2411.14215
- [V] Hodel and West (2023) Response: Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2308.16118
- [V] Musker, Duchnowski, Milliere, Pavlick (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Richey, Phillips, Schunn, Schneider (2014) Is the link from working memory to analogy causal? https://pmc.ncbi.nlm.nih.gov/articles/PMC4154731
- [V] Zhang, Jian, Ouyang, Vosoughi (2024) Working memory identifies reasoning limits in language models. https://aclanthology.org/2024.emnlp-main.938
- [V] Raemaekers, Finn, De Houwer et al. (2025) Assessing the relational abilities of LLMs and large reasoning models. https://pmc.ncbi.nlm.nih.gov/articles/PMC12837307
- [V] Chuderski (2022) Fluid intelligence emerges from representing relations. https://pmc.ncbi.nlm.nih.gov/articles/PMC9396997
- [V] Richland and Morrison (2010) Is analogical reasoning just another measure of executive functioning? https://pmc.ncbi.nlm.nih.gov/articles/PMC2948449
- [V] Doumas, Morrison, Richland (2018) Individual differences in relational learning and analogical reasoning. https://pmc.ncbi.nlm.nih.gov/articles/PMC6095010
- [V] Keane, Ledgeway, Duff (1994; 1993 TCD technical report) Constraints on analogical mapping. https://www.cs.tcd.ie/publications/tech-reports/reports.93/TCD-CS-93-24.ps.gz
- [V] Camposampiero et al. (2025) Can large reasoning models do analogical reasoning under perceptual uncertainty? https://arxiv.org/abs/2503.11207
- [V] Camposampiero et al. (2025) I-RAVEN-X. https://arxiv.org/abs/2510.17496
- [V] Shi et al. (2023) Large language models can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093
- [V] Levy, Jacoby, Goldberg (2024) Same task, more tokens. https://arxiv.org/abs/2402.14848
- [V] Feng and Steinhardt (2024) How do language models bind entities in context? https://arxiv.org/abs/2310.17191
- [V] Chen et al. (2026) ARCANA. https://arxiv.org/abs/2610.29271
- [V] Mondal, Cohen, Webb (2024) Slot Abstractors. https://arxiv.org/abs/2403.03458
- [V] Webb, Sinha, Cohen (2021) Emergent symbols through binding in external memory. https://arxiv.org/abs/2012.14601
- [V] Hu et al. (2023) In-context analogical reasoning with pre-trained language models. https://arxiv.org/abs/2305.17626
- [V] Huang et al. (2025) On the failure of latent state persistence in LLMs. https://arxiv.org/abs/2505.10571
- [V] Zhang et al. (2026) United minds or isolated agents? https://arxiv.org/abs/2506.06843
- [M] Lee et al. (2025) The curious case of analogies. https://arxiv.org/abs/2511.20344
- [M] McGovern et al. (2026) When models know more than they can explain. https://arxiv.org/abs/2604.03877
- [M] Various sources of distraction during analogical reasoning (2022). https://www.semanticscholar.org/paper/866d215de3a892513d2e68fd854adf14ebf408b7
- [M] Breaking the perceptual-conceptual barrier: relational matching and working memory. https://www.semanticscholar.org/paper/5124e763962d2f706a17b7c80bf32710ad16a691
- [M] Altabaa et al. (2024) Abstractors and relational cross-attention. https://arxiv.org/abs/2304.00195
- Not opened (cited only): Keane and Brayshaw (1988) IAM https://en.wikipedia.org/wiki/Structure-mapping_theory ; Halford, Wilson, Phillips (1998) https://doi.org/10.1017/S0140525X98001769 ; Hummel and Holyoak (1997) https://doi.org/10.1037/0033-295X.104.3.427 ; Hummel and Holyoak (2003) https://doi.org/10.1037/0033-295X.110.2.220 ; Cowan (2001) https://doi.org/10.1017/S0140525X01003922 ; Markman and Gentner (1993) https://doi.org/10.1006/cogp.1993.1011 ; Waltz et al. (1999) https://doi.org/10.1111/1467-9280.00167
