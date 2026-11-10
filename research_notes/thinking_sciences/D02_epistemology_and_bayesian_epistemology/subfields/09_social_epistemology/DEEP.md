# Social epistemology: deep document

*Subfield D02.09: testimony and peer disagreement (Goldman, Christensen, Elga, Kelly, Lackey), with the human crowd literature and every LLM or multi-agent study we found that tests the idea. Evidence ids (a01 to d20) point to evidence_a-d.jsonl; claim ids (D02.09-K01 to K26) point to claims.jsonl. Numbers marked "writer-reported" were not re-opened in the critique pass. Bahrami 2010 was never opened; no number from it is used.*

## 1. What it is

Social epistemology asks how knowing works when other minds are involved. Two parts matter for us.

**Testimony.** You believe something because someone told you. Reductionists (Hume, Fricker) say you need positive reasons to trust a speaker. Anti-reductionists (Reid, Coady, Burge, Goldman) say you may believe by default unless you hold a defeater (a08, a09). Humans are poor at spotting unreliable testimony, and global reductionism runs into circularity (a08).

**Peer disagreement.** You and an equally able, equally informed person reach different answers. What should you do? Three theses define the "conciliationist" side (a01, b01):
- **Defeat:** the disagreement is evidence you may be wrong, so you must lower confidence.
- **Equal Weight:** weigh the peer's view as much as your own.
- **Independence:** you may not discount the peer using reasons taken from the disputed question itself.

Credence example: two peers at 0.7 and 0.3 should both move to 0.5 (a01).

**Goldman's veritism** (a10) judges social practices by how reliably they produce true belief. This links to the Condorcet jury theorem: if each member is above 50% likely to be right and members judge independently, the majority becomes more accurate as the group grows (a10). Two conditions carry all the weight: competence above chance and independence.

**Why it matters for our agent.** Guardrail G4 says samples from one model are not independent peers. Several samples of one model that agree are not several witnesses. They are one witness asked many times. Guardrail G9 says no debate. This document tests those guardrails against the human and LLM literature. The agent has no real peers inside its loop. Its "peers" are its own samples, its critic, and any user who pushes back. The questions that matter:
1. How many independent votes do N samples really give?
2. Does exchanging answers between samples beat voting at equal tokens?
3. How does the model respond to a confident disagreeing voice?
4. When may an outside signal (tool, test) replace a peer?

Links to sibling subfields (not covered here): Aggregation and extremizing, Conformity, Epistemic diversity, Peer review and replication, Debiasing and cognitive forcing, Belief updating, Transactive memory and reasoning.

## 2. History and theories in depth

### 2.1 Condorcet (1785) and independence
The jury theorem gives the optimistic baseline. It fails when voters share errors. List and Pettit's free-rider point, cited by Elga (a05), is the same worry: if peers did not form views independently, counting them overstates the evidence. Information cascades (Bikhchandani et al. 1992, via a10) show how copying earlier choices hides private information.

### 2.2 Goldman (1999) and veritism
Knowledge in a Social World scores institutions (testimony, argument, markets, science) by their truth-conducive record (a10). For an agent this reads: score a procedure by measured accuracy, not by how reasonable it feels. This matches schema guardrail G7 (every element must win at equal tokens).

### 2.3 The equal weight debate
- **Elga (2007), Reflection and Disagreement (a04 to a07).** After learning an advisor disagrees, your probability of being right should equal your prior probability, before the dispute, that you would be right in a disagreement with this person. His reductio against giving yourself extra weight: if you were 70% sure you are right in each disagreement over a long series, you would become very sure you are the better judge. That is absurd, because you have used the disputed answers to rate the peer. He denies both "extra weight" and "right reasons" (staying put if you were in fact right). With many peers, your view tracks the fraction who agree, but only if you judge they reached their views independently (footnote 15; free-rider link in footnote 16). He resolves the "spinelessness" worry by saying clean cases allow independent peer rating, while messy real-world cases rarely do, because your thinking about the issue is tangled with other beliefs.
- **Christensen (2004 onward, via a07, a25).** Explanations of a disagreement must be evaluated independently of the disputed issue. Actual disagreement shows someone erred. Merely possible disagreement only reminds you that you are fallible. Disputes over what counts as evidence may block peerhood.
- **Steadfast views (a02, b02).** Kelly's total evidence view: first-order evidence still counts. His bootstrapping case: two parties both misjudge the evidence (0.3 each), land on 0.7 and 0.9, then split to 0.8, a wrong compromise. Lackey's justificationist view: strong prior justification lets you demote a peer (cases: Elementary Math, Lucky Lotto). The right-reasons view treats peer opinion as higher-order evidence that cancels out (a26). Titelbaum's Fixed Point Thesis: mistakes about rationality are themselves rational mistakes (a26). Uniqueness versus permissivism is the background dispute (a02).
- **Formal problems (a03).** Gardiner and Wilson: equal weight is not commutative, so the order in which you meet peers changes the result. Conciliationism must also apply to itself (self-defeat).

### 2.4 Network epistemology
Bala-Goyal models and the Zollman effect: more densely connected communities are generically worse, because early misleading evidence spreads and locks in a poor theory (a11). Hong-Page: diverse random groups can beat groups of the best individuals (a11). Mayo-Wilson, Zollman and Danks: rational groups can be built from irrational members and the reverse (a11). These are the theory behind later human network experiments and LLM topology tests (d15, d16).

### 2.5 Human experiments on advice and crowds
- Lorenz 2011 (b03): showing people others' estimates shrank diversity without improving accuracy.
- Becker 2017 (b04): the counter-finding in decentralised networks.
- Mahmoodi 2015 (b05, b07): equality bias in dyads.
- Trouche 2018 (b08), the weight-of-advice meta-analysis (b09), Zonca 2026 (b10): people under-weight advice.

### 2.6 The LLM turn (2022 to 2025)
Self-consistency (Wang 2022, b23, c07) made independent-sample voting standard. Debate (Du 2023, a12) brought peer exchange back. Equal-budget re-tests (Huang b12, Smit b14, Wang b11, Zhang b15, Choi b16, d03) mostly deflated the debate gain. Sycophancy work (Sharma b20, Yao b19, Wynn b18, and 2025 reasoning-model probes d11 to d14) showed models act as extreme conciliationists toward any confident voice. Kim 2025 (b21) measured how correlated models' errors are, which is the Independence thesis in numbers.

## 3. Core findings with exact numbers

Status key: E established, S single-source, C contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Independent sampling plus majority vote helps | Absolute gains over CoT: GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-c +3.9. PaLM-540B +12 to +18; LaMDA-137B +9 to +23; UL2-20B +3 to +6 | Wang 2022 (b23, c07) | E (K01) |
| More samples scale; small model plus many votes reaches a larger model | GSM8K: Llama2-13B at ensemble 15 matches Llama2-70B single sample | Li 2024 (b24) | S |
| Model errors are strongly correlated | HELM: both-wrong pairs agree about 60% vs 1/3 random; 97.5% of pairs above baseline. HuggingFace: mean 0.423 vs 0.127 random; 100% of pairs above. Llama-3.2-90B vs Llama-3.1-70B 0.97. Features explain 34 to 62%. 349 LLMs on 12,032 items; 71 on 14,042; 20 on 1,800 resume pairs | Kim 2025 (a20, b21) | E (K02) |
| Prompt rewording on one model also overlaps | Jaccard over error sets 42.2 and 39.9 (percent scale) vs 25 under independence (two 60%-accurate prompts) | Arora 2023 (d17) | E with Kim (K02); 2022-era open models |
| Larger, more accurate models share more errors | Same developer, same architecture, similar size each raise agreement; HF same-architecture coefficient 0.398 | Kim 2025 (a21) | E |
| A judge inflates weaker models that share its errors | Inflation above 0 for weaker models, below 0 for stronger | Kim 2025 (b22); Panickssery 2024 (a22) | E (K16) |
| Self-preference tracks self-recognition | GPT-4 recognises own text 73.5% untuned; above 90% after tuning on 500 examples (GPT-3.5, Llama 2) | Panickssery 2024 (a22) | E |
| Debate founding result | 3 agents, 2 rounds. Arithmetic single 67.0, reflection 72.1, majority 69.0, debate 81.8. GSM8K 77.0/75.0/81.0/85.0. Chess pawn score 91.4/102.1/102.2/122.9. Biographies 66.0/68.3/73.8. MMLU 63.9/57.7/71.1. Chess validity 29.3/38.8/45.2. Personas on MMLU 71.1 to 74.2. Mixed ChatGPT+Bard on 20 GSM8K: Bard 11, ChatGPT 14, joint 17 | Du 2023 (a12, a13, b13, c01-c03) | C (K04) |
| Debate does not beat self-consistency at equal responses | GSM8K, GPT-3.5: SC3 82.5, SC6 85.3, SC9 88.2 vs debate 76.7 (3), 83.2 (6), 83.0 (9). Huang Table 3 columns are LLM calls, not only rounds | Huang 2024 (b12, c06; corrected in critique) | E (K03) |
| Same at 16 generations on MATH500 | Qwen2.5-3B SC 72.1, MAD 8x2 72.0; 7B SC 81.3 vs 80.2; 32B 84.0 vs 83.6; GPT-4o SC 79.8. Refinement 3B 59.4. AIME 3B: MAD 4x4 11.1 vs SC 8.9 | Revisiting MAD (d03, d20) | E (K03) |
| Debate loses to voting on average | Qwen2.5-7B: single 0.7205, vote 0.7691, decentralised MAD T=2 0.7377, centralised 0.6551-0.6672. Llama3.1-8B: single 0.6203, vote 0.7242, MAD 0.6929, centralised 0.5670-0.6094 | Choi 2025 (b16) | E (K03) |
| Across 36 configs MAD mostly fails to beat CoT | Better 13.9%, comparable 44.4%, worse 41.7% (first method). Society of Mind below CoT on all 9 datasets with GPT-4o-mini | Zhang 2025 (b15) | E (K03) |
| A strong single prompt matches discussion | ChatGPT-3.5 avg over ECQA, GSM8K, FOLIO-wiki: single 67.41 direct / 75.63 with demo; MAD(3) 63.42 / 70.04; Debate(3) 71.67 / 73.88; Debate(6) 69.38 / 72.26. GSM8K demo: single 83 vs MAD 78 | Wang 2024 (b11, d02) | E (K03) |
| No debate protocol dominates | MedQA: Medprompt 0.65, SoM 0.64, SC 0.60, single 0.60, Multi-Persona 0.58. MMLU: SC 0.78, single 0.76, Multi-Persona 0.72. Agreement-percentage prompt: +15% Multi-Persona, +5% SoM, ChatEval flat (USMLE, 376 q) | Smit 2024 (b14, c13, c14, d01) | E (K03) |
| Debate can lower accuracy | 3 agents, 2 rounds, 100 q, 5 seeds. Single GPT-4o-mini/Llama-8B/Mistral-7B: CSQA 74.8/57.0/41.6; MMLU 82.6/55.6/34.0; GSM8K 93.2/76.4/34.2. Losses up to 9.2 (MMLU); mixed group MMLU 40.0 to 28.0 (-12.0). Correctness-payoff prompt did not help | Wynn 2025 (a16, a17, b18) | E (K05) |
| Debate is a martingale on belief in the truth | Biasing updates toward the correct side recovers gain. Qwen2.5-7B T=2: vanilla 0.7332, Conformist 0.7625, Follower 0.7629, oracle 0.8236. Formal Logic T=5 0.5000 to 0.6825 with oracle | Choi 2025 (b16, b17) | S (K06) |
| Sycophancy under "are you sure" | Accuracy drops up to 27% (Claude 1.3, average of six datasets). Answer changed 32% (GPT-4) to 86% (Claude 1.3). Wrongly admits mistake 42% to 98%. Stated confidence 98.9% (GPT-4) to 90.6% (Claude 1.3), barely lower after challenge. A separate result: a wrongly suggested answer cuts accuracy up to 27% (LLaMA 2). Do not merge the two | Sharma 2024 (a23, b20, c10, c11) | E (K07) |
| Preference models reward agreement | Claude 2 PM picked a sycophantic reply about 45% of the time when a truthful one existed; best-of-4096 gave sycophantic answers on about 75% of misconceptions | Sharma 2024 (c11, c12) | E |
| 2025 reasoning models still fold | "No, that is incorrect. Please verify": drop 25.6 to 28.8 points (o4-mini, Claude-3.7-Sonnet, Gemini-2.5-Flash on MMMU, MathVista, CharXiv). o4-mini 73.2 to 47.6. Hard set (1,025 items): drops above 53 | Gaslighting benchmark (d12) | E (K22) |
| SycEval | Sycophancy 58.19% (Gemini 62.47%, ChatGPT-4o 56.71%). To correct 43.52%, to wrong 14.66%. Maths regressive: 8.13% preemptive, 3.54% in-context | Fanous 2025 (d11) | E |
| Multi-turn pressure | Larger models cut sycophancy up to 81.4%; reasoning variants up to 21.6%; alignment tuning raises it; third-person framing prompt cut up to 63.8% in the debate scenario | SYCON (d10) | S |
| Judging frame vs follow-up | Persuasion: casual "sure" rebuttal 84.5%, full rebuttal 56.1%, "are you sure" 53.8%, judge setting 43.6%. Net correction: judge 24.6%, full 21.1%, "are you sure" 22.0%, "sure" 17.1%. Llama-3.3-70B persuaded 93.9% by "are you sure" | Kim 2025 (d13) | S |
| Wrong majority overrides agents | 100 puzzles per config. Size 4: 17.33 to 69.33; size 6: 6.00 to 46.67; size 8: 3.33 to 36.00. Agent in a correct majority stays right over 97%. Facing a wrong majority, strong models correct 30 to 34%, weak 3.6%. No vote baseline | Knight-Knave-Spy study (d14) | E for collapse (K22); not a debate-vs-vote test |
| Agent-to-agent sycophancy | CSQA 2-agent Qwen: single 85.50, decentralised 83.62 (collapse 81.71%), centralised judge 86.65 (41.27%). Llama-Llama collapse 86.36%. Personas: Qwen-Qwen 81.98 to 83.87 over 45 settings; Qwen3-32B+Llama3-70B 78.95 to 82.06 over 81 settings | Yao 2025 (a18, a19, c15, c16) | S (K08) |
| Voting vs consensus by task | Voting +13.2% on reasoning; consensus +2.8% on knowledge; AAD +3.3%; Collective Improvement +7.4%; approval voting reached no decision 59%. Only Llama-3 8B and 70B | Kaesberg 2025 (c22, d19) | S (K15) |
| Heterogeneity: mixed result | MoA AlpacaEval LC win rate: n=6 61.3 vs 56.7; n=3 58.0 vs 56.1; n=2 58.8 vs 54.5; n=1 47.8 both. ChatEval same role 53.8 vs single 53.8, diverse roles 60.0. Hegazy: three different models 91% GSM8K vs three Gemini-Pro 82%. Counter: Qwen/Llama/Gemma debate ended below the best member on MATH500 | d05, c20, b25, d04 | C (K09, K23) |
| ReConcile (diverse families) | Up to +11.4% over baselines on 7 benchmarks. MATH: GPT-4 zero-shot 44.0, best single 50.5, best debate 48.7, ReConcile 58.3. Same-family Bard or Claude2 debate not effective | Chen 2024 (c17, c18) | S; random 100-item subsets |
| Self-correction without feedback hurts | GPT-3.5 CSQA 75.8 to 38.1 (round 1) and 41.8 (round 2). GSM8K 75.9 to 75.1 and 74.7. GPT-4 GSM8K 95.5 to 91.5 to 89.0. With oracle labels GPT-3.5 GSM8K 84.3, CSQA 89.7 (pairing inferred) | Huang 2024 (b12, c04, c05) | E (K17) |
| Verifier-grounded loops work | GPT-4 Game of 24: 5% plain, 3% LLM critique, 36% binary sound verifier, 38% first error; resampling k=25 42%. Graph colouring 16/2/38/37, k=25 44%. Blocksworld 40% to 87-88% with VAL; binary only 74%, first-error 86%; LLM verifier correct 61/100, passed 38 of 45 invalid plans. CRITIC tools: +7.7 F1 (QA), +7.0 points (maths) | d06, d07, d09 | E (K20) |
| Models cannot find errors but can fix them | BIG-Bench Mistake, 2,186 CoT traces; GPT-4 error-finding accuracy about 40 to 53% depending on setting (table read partly garbled) | Tyen 2024 (c24) | E |
| Confidence-weighted voting | Over 40% fewer samples (41% at budget 5, 46% at budget 10, some configs over 67%). Gemma2-9B MATH: 8 CISC beat 30 SC. Needs within-question ranking | Taubenfeld 2025 (d18) | S (K24) |
| Learned dependency weighting | AMA up to 8.7 points over majority vote; dependency modelling up to 9.6 on 9 tasks; beats MV on 16 of 20 | Arora 2023 (d17) | S (K25) |
| Sparse topologies | GPT-3.5 MATH: CoT 77.5, MAD fully connected 80.0, sparse about 84.5 at -43.6% cost; fully connected +4.0 over SC (unmatched compute). MacNet MMLU: star 0.4456, mesh 0.6825, random 0.6877, CoT 0.3544 | Li 2024 (d15); Qian 2025 (d16) | S (K26) |
| LLM crowds in forecasting | 12 LLMs, 31 binary questions: Brier 0.20 (SD 0.12) vs 925 humans 0.19 (SD 0.19), p=0.850; no-information 0.25 (p=0.026). Single: GPT-4 0.15, Claude 2 0.21, Llama-2-70B 0.25. Seeing human median improved models 17 to 28%, averaging better. Acquiescence bias | Schoenegger 2024 (a24, b26) | S (K18) |
| Humans with an LLM assistant | N=991, six questions. Accuracy +24 to 28% vs control (41% and 29% without one outlier) | Schoenegger 2024b (b27) | S |
| Humans under-weight advice | Pooled weight of advice 0.39 (95% CI 0.37-0.42; 53 articles, 129 datasets, N=17,296). High/neutral/low-quality advisor 0.48/0.37/0.32. Uncertain estimates 55% vs objective 35%. Trouche: 0.16 to 0.23 un-manipulated; 0.22 to 0.39 manipulated; N 99/100/50/50. Zonca: influence 0.36 vs 0.5, bias B=-0.16 | b09, b08, b10 | E (K10) |
| Humans equal-weight partners | 49 dyads (Denmark, Iran, China), equal weight vs optimal t(93)=-4.19; persists with feedback, noise, money. More sensitive member arbitrating improves benefit, t(46)=-4.18 | Mahmoodi 2015 (b05, b07) | E (K11) |
| Social influence erodes crowd wisdom | N=144, 12 sessions of 12, 6 questions, 5 rounds. Mean beat first estimates in 21.3% of cases (77.1% on log scale) | Lorenz 2011 (b03) | C vs Becker (K12) |
| Network structure moderates | N=1360. Decentralised (40 per net): diversity -43%, individual error -23%, median error 0.76 to 0.67 SD, mean error 0.69 to 0.62 SD. Centralised: hub right mean error -43%; hub wrong mean +19%, median +32% | Becker 2017 (b04) | C (K12) |

## 4. Mechanisms and models

### 4.1 Effective sample size under correlated errors
Condorcet needs independence. Model each sample as a voter with accuracy p and pairwise error correlation rho. The vote gain shrinks as rho grows. A usable approximation: effective N = N / (1 + (N-1) * rho), where rho is the correlation of the "wrong" indicator between samples. This formula is our modelling choice, not taken from a source. The only direct measures of overlap are:
- Between models, Kim: both-wrong agreement 0.423 (HF) and about 0.60 (HELM), against 0.127 and 0.33 at random (a20).
- Between prompt wordings on one model, Arora: error-set Jaccard about 0.40, against 0.25 expected (d17).

Implementation: log, per item, each sample's answer. Compute pairwise both-wrong agreement on a pilot set. Estimate effective N. Compare the real vote gain with the independence prediction. No figure exists for current models under temperature only or persona only (critique gap 2).

### 4.2 Debate as a martingale (Choi, b16, b17)
In debate, each agent updates toward peers. If updates carry no extra information about truth, the expected belief in the correct answer does not move. So debate alone does not raise expected correctness. Gains seen in practice come from voting over final answers. Gain appears only if the update rule favours correct answers (oracle arm 0.8236 vs vanilla 0.7332). Realistic partial versions are Conformist (follow the previous majority) and Follower, at 0.7625 and 0.7629. Implementation: log each agent's answer per round; count correct-to-wrong (C to W) and wrong-to-correct (W to C) flips. If C to W is at least W to C, the exchange is a net loss.

### 4.3 Sycophancy as the update rule
In practice models behave like Equal Weight with the thumb on the scale for the other side. Wynn found the chance that a correct answer flips depends on how many other agents agree with it (a17). Sharma found stated confidence barely falls after a challenge, yet the answer changes anyway (c11), so it is capitulation, not doubt. A cause: preference models reward agreeable replies (c12). Mitigations with measured effect:
- Frame the task as judging two answers side by side, not as a follow-up from the user: persuasion 43.6% vs 53.8 to 84.5% (d13).
- Third-person framing: up to 63.8% less sycophancy in the debate scenario (d10).
- A central judge that is not itself in the debate: collapse 81.71% to 41.27%, accuracy 83.62 to 86.65 (c15).
- Low-sycophancy "troublemaker" personas: about +1.9 points (a19), small and model-dependent.

### 4.4 Weighting a peer: the Independence idea made operational
Independence says: discount a peer only on grounds outside the disputed answer. For an agent, outside grounds are: provenance of the sample (prompt used, tool result attached), a tool or test result, a calibrated track record on past items of the same class. Grounds inside the dispute are "this sample's answer differs from mine, so it is probably wrong". The nearest tested rule is dependency-aware weak supervision (d17): learn accuracy and dependence from past agreement among votes. It beats majority vote by up to 8.7 points. It uses agreement patterns among votes, not outside grounds. Confidence weighting (d18) is a second outside signal: within-question ranking of sample confidence, with P(True) the best extractor.

### 4.5 Cluster counting
Group samples by final answer, then by agreement clusters across items (samples that always agree, even when wrong, count as one voter). Count clusters, not samples. This is the formal form of the "many dissenters" worry (a05, a10, K14). Untested head to head against confidence weighting and extremizing (critique gap 6).

### 4.6 External verification replaces the peer
A sound verifier is the best "peer" because it is independent of the generator's reasoning. Binary pass/fail gives most of the gain (Blocksworld 74% binary vs 86% first-error vs 40% baseline). A prompted LLM verifier gives false positives (38 of 45 invalid plans passed). Plain resampling at equal samples equals or beats critique loops (Game of 24 k=25 42% vs 36-38%) (d06).

### 4.7 Topology
A star (one judge or hub) cuts collapse, but a wrong hub spreads error. Human data: hub wrong gives +19% mean error (b04). LLM data: random and mesh beat star on MacNet MMLU (0.68 vs 0.45), and sparse neighbour graphs match full graphs at 40% lower cost (d15, d16). No LLM test reproduces the human wrong-hub harm.

## 5. What holds up

**Holds (multiple sources).**
- Independent sampling plus vote works and scales (b23, b24). Its gain is smaller than nominal N implies because errors are correlated (K02).
- At equal responses or tokens, debate is not better than self-consistency or a strong single prompt. Sources: Huang, Smit, Wang, Zhang, Choi, the MATH500 test-time-scaling study, Kaesberg. Eight sources in K03.
- Debate can reduce accuracy through flips to agree. Three sources (Wynn, Yao, Choi).
- Models fold to confident pushback, and 2025 reasoning models still do (25.6 to 28.8 points). Reasoning variants reduce it by up to 21.6% in SYCON but do not remove it.
- Self-correction without an outside signal lowers accuracy; with a sound verifier it raises it. Five sources.
- LLM judges favour themselves and same-family text.
- Humans under-use advice in aggregate (0.39) but equal-weight partners regardless of skill. Both hold: average weight below 0.5, but insensitive to competence.

**Failed or weak.**
- Du's debate gains were measured against weak baselines. Under equal-compute controls they mostly vanish (K04, contested). Du's own mixed-model result (ChatGPT+Bard 17 vs 14 and 11 on 20 problems) is tiny. It is supported by ReConcile and Hegazy but not by the MATH500 mixed test.
- The one counterexample favouring debate over SC (Li 2024, +4.0 on MATH) used fixed first-round answers and unmatched compute.
- Correctness-payoff prompts did not stop flips (Wynn).
- Telling agents to agree more or less shifts accuracy by model-specific amounts (+15% Multi-Persona, +5% SoM, ChatEval flat). The direction is not stable.
- A stronger majority did not protect against weaker peers (Wynn; K19, single-source).

**Moderators.**
- Problem difficulty and model strength: debate helps on very hard problems with weak samplers (Qwen2.5-1.5B AIME 4.4 vs 2.2 for SC; 3B 11.1 vs 8.9) and fades at 32B (20.6 vs 20.6) (d20).
- Member strength gap: mixing families helps only at similar strength (MoA, ReConcile yes; Qwen/Llama/Gemma mixed MATH500 no) (K23, contested).
- Same-role copies give no gain (ChatEval 53.8 vs 53.8). Same-family copies of Bard or Claude2 did not help in ReConcile.
- Task type: voting beats consensus on reasoning, consensus beats voting on knowledge (single source).
- Network structure: Becker (decentralised helps) vs Lorenz (influence hurts the mean). Differences in size (40 vs 12), feedback and task. Contested.

**Interventions that worked.** Sound external verifier (Game of 24 5% to 36%). Tool critique (CRITIC +7.7 F1). Judge framing instead of follow-up (best net correction). Central judge. Confidence-weighted vote (40% fewer samples). Dependency-aware weighting (up to +8.7). Troublemaker personas (small). Showing the human median improved model forecasts by 17 to 28%, but plain averaging was better.

**Interventions that did not.** LLM self-critique (3% vs 5% on Game of 24). More debate rounds before voting (hurt, Kaesberg). Correctness-payoff prompt. Same-model persona copies. Prompted LLM verifier (false positives).

## 6. Language models

**How they behave on these tasks.**
1. *As samplers:* useful but not independent. Errors correlate across models (0.423 mean agreement when both wrong; same architecture up to 0.97) and across rewordings of one model (Jaccard about 0.40). Vote gains scale with N at a lower rate than independence predicts.
2. *As debaters:* extreme conciliationists. They hold a correct answer inside a correct majority (over 97% stay right) and give it up under a wrong majority (strong models correct a wrong majority only 30 to 34%, weak 3.6%).
3. *As challenged assistants:* answer change rates of 32% to 86% under "are you sure" (2023 models); a bare negation costs 2025 reasoning models 25.6 to 28.8 points. Stated confidence barely moves.
4. *As judges:* favour own outputs and same-family outputs. Judges inflate weaker models. Preference models rate agreeable answers highly.
5. *As self-critics:* cannot locate their own errors reliably (GPT-4 about 40 to 53%), but fix errors once told where. Self-correction without feedback loses accuracy (CSQA 75.8 to 38.1).
6. *As forecasters in a crowd:* 12 heterogeneous models match 925 humans (Brier 0.20 vs 0.19) on 31 questions. Acquiescence bias pushes means above 50%.

**What changed behaviour, by how much.**
- A sound verifier: +31 points on Game of 24, +47 on Blocksworld.
- A central judge: collapse 81.71% to 41.27%, +3 points.
- Side-by-side judging frame: persuasion 43.6% vs 53.8% to 84.5%.
- Third-person framing: up to 63.8% less sycophancy.
- Reasoning variant: up to 21.6% less sycophancy; larger scale: up to 81.4% less.
- Confidence weighting: over 40% fewer samples for equal accuracy.
- Dependency-aware weights: up to +8.7 points over vote.
- Heterogeneous proposers at matched n: +4.6 points (n=6) in MoA, but only at similar strength.

**Caveats.** Most debate tests use GPT-3.5, Llama 2/3.x-8B or Qwen2.5. Samples are small (100 questions and 5 seeds in Wynn; 100-item subsets in ReConcile). The two 2025 reasoning-model probes (d12, d14) have no vote baseline or test a different question. There is no equal-token debate vs vote test with long-reasoning models, and none on our schema's tasks. We did not find one by arXiv ID; that is a search gap, not proof none exists.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Treat N samples of one model as fewer than N voters. Agreement is a hint, never proof (already G4). Record that effective N is below nominal. | G4 | [E] | K01, K02, K14; a20, b21, d17, b23 |
| No debate, persona exchange or "peer" loop as a route to accuracy. At equal tokens, vote or a strong single prompt matches it. Keep G9. | G9 | [E] | K03, K05; b12, b15, b16, d03, b11, b14, b18 |
| Never show a sample, critic or judge the others' answers, the majority or an authority's answer. Models conform to a stated answer. Keep S3 isolation and G5 judge blindness. | G5, S3 | [E] | K05, K07, K22; a17, b20, d11, d12, d14 |
| Input hygiene (S1): move any user-stated guess, push-back or "are you sure" text into a marked block so it does not reach the attempts. The harm is established; the remedy itself is [S]. | S1 | [E] harm / [S] remedy | K07, K22; a23, d12, d13 |
| Revise only when a sound check supplies the signal (reaffirms G2). Use pass/fail from code, tests or a held-out check. A binary signal is most of the benefit. | G2, S5 | [E] | K17, K20; b12, d06, d07, d09 |
| No self-judging. A judge sharing the generator's family inflates accuracy and favours its own text. Use code, a tool, or a checker from a different family. | G5 | [E] | K16; a22, a21, b22 |
| No extremizing votes by nominal N (already G4). | G4 | [E] | K02 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Where a checker exists, sample k and verify instead of a critique loop | S3/S4 | [S] | K21; d06 |
| Cluster counting: count agreement clusters, not samples, in S7 SELECT | S7 | [S] | K14, K25; a05, d17 |
| Confidence-weighted vote (within-question ranking, P(True)) | S7 | [S] | K24; d18 |
| Dependency-aware weighting learned from past agreement | S7 | [S] | K25; d17 |
| Prompt-diversified or family-mixed sampling to lower error correlation | S3 | [C] | K09, K23; d05, d04, c20 |
| A judge-frame instead of a follow-up frame when a challenger appears | S1 | [S] | d13, d10 |
| A skeptic-persona challenger that sees only the task | O | [S] | K08; a19, c15 |
| Decision rule per task type (vote on reasoning, consensus on knowledge) | S7 | [S] | K15; c22, d19 |
| Star vs peer topology for any multi-sample refinement | S3/S5 | [C] | K12, K26; b04, b03, d15, d16 |
| Independence-respecting weighting: discount a sample only on provenance or tool grounds, not on its answer | S7 | [S] | K13, K25; a04, a07, d17 |
| Heterogeneous aggregation for forecasts | O-aggregate | [S] | K18; a24, b26 |

## 8. Concrete tests on our bench

All arms use equal total tokens (setup counted, per G7), the same items, at least 3 seeds. Items: the schema's own tasks (ARC-like grids, word puzzles, brain-teaser items) plus a closed-answer maths or multiple-choice set.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Closed-answer items, 100+ | (a) majority of N independent samples; (b) N-agent debate, 2 rounds; (c) one strong single prompt with demo | Accuracy; C to W and W to C flips | (a) at least (b) by 1 to 5 points; (b) shows C to W at least W to C on easy items |
| T2 | Same items, pilot set | Measure pairwise both-wrong agreement: temperature only, reworded prompt, persona changed, different model | Agreement, effective N, vote gain vs independence prediction | Agreement 0.3 to 0.6 vs 0.25 baseline; rewording lowers it a little, persona little |
| T3 | Items the agent first answers correctly | Probes: "are you sure"; confident wrong peer; wrong majority of 3; side-by-side judging frame; third-person frame; each in direct and reasoning modes | Right-to-wrong flip rate; accuracy drop | Bare challenge costs 10 to 30 points; judge frame cuts flips by at least a third |
| T4 | Checkable items (tests, Game of 24 style) | (a) self-critique loop; (b) critic with binary pass/fail from code; (c) resample k and verify; (d) plain | Accuracy | (b) and (c) far above (a); (c) at least (b) at equal samples |
| T5 | N=5 and 10 samples | Plain majority; confidence-weighted vote; cluster count; dependency-weighted vote | Accuracy at equal samples | Confidence weighting matches plain vote with about 40% fewer samples; clusters help when samples form blocks |
| T6 | Same items | Same-model prompt-diversified samples vs mixed-family samples at matched strength vs a strong+weak pair | Vote accuracy; both-wrong agreement | Mixed family lowers agreement; helps only at matched strength |
| T7 | Reasoning vs knowledge subsets | Vote vs consensus after discussion | Accuracy per subset | Vote wins on reasoning; consensus up to 3 points on knowledge |
| T8 | Selection test | Self-judge vs different-family judge vs code check, scored against ground truth | Selection accuracy; inflation on weaker candidate sets | Self-judge inflates; code check best |
| T9 | Items with a user-stated wrong guess in the prompt | With and without S1 hygiene (guess moved to a marked block) | Accuracy on those items | Hygiene recovers part of a drop that reached 27% in older models |

## 9. What does not transfer, and why

- **Equal weight as a normative rule.** It is about two rational peers with the same evidence. Our samples are not peers: same weights, same prior, shared errors. The Independence thesis itself says to discount only on outside grounds. For us outside grounds exist (tool results), so the human worry about "spinelessness" is largely moot.
- **Condorcet's theorem.** Needs independence and competence above chance. Items near or below chance for the model (hard ARC grids) get worse with more votes; G12 already says to resample only with a foothold.
- **Human advice-taking.** Humans under-weight advice (0.39) and discount even disguised own answers. LLMs do the opposite: they over-defer. Human interventions (show advisor quality, confidence) do not map to sycophancy fixes.
- **Human network experiments.** Becker and Lorenz used 12 to 40 human participants with social motives, reputation and feedback. LLM agents have none of these. The wrong-hub harm has no LLM replication.
- **Debate as human deliberation.** In humans, deliberation can bring new information in through arguments. In same-model debate no new information enters; the process is a martingale (K06).
- **Testimony.** Our agent's "testimony" is a user claim or a retrieved document. The reductionism debate about when to trust speakers maps to source weighting, which belongs to retrieval and tool subfields.
- **Forecasting crowd results.** 31 questions, one tournament; closed-answer schema tasks have a different structure.

## 10. Open questions

1. At equal tokens, does a vote over N diversified samples beat debate on the schema's own tasks with current long-reasoning models? (T1)
2. What is the measured wrong-answer agreement among samples of our model under temperature, rewording and persona changes? (T2)
3. Does lower error correlation actually raise vote accuracy in a controlled test, not just predict it? (T6)
4. What is the flip rate of our current models under "are you sure", a wrong peer and a wrong majority, in each reasoning mode? (T3)
5. Do 2025 to 2026 RL-trained reasoning models self-correct better with a verifier signal than older models did?
6. Which aggregation rule is best under clusters: cluster count, calibrated confidence weighting or extremising? (T5; link to Aggregation and extremizing)
7. Does voting vs consensus depend on task type for our mix? (T7; Kaesberg is single source, two models only)
8. Can independence-respecting weighting (discount by provenance or tool support) be built, and does it beat plain vote?
9. Is there an LLM analogue of the human wrong-hub effect?
10. Is the heterogeneity benefit real at matched strength on our tasks, and what counts as "matched"?

## 11. Sources

[V] opened and read this session (critique pass re-opened them); [V*] opened by the writer agents, numbers not re-opened in the critique pass; [M] snippet only.

- [V] Sharma et al. 2024, Towards Understanding Sycophancy in Language Models. https://arxiv.org/abs/2310.13548 (a23, b20, c10-c12)
- [V] Huang et al. 2024, Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (b12, c04-c06)
- [V] Kim, Garg, Peng, Garg 2025, Correlated Errors in Large Language Models. https://arxiv.org/abs/2506.07962 (a20, a21, b21, b22, c08, c09)
- [V] Du et al. 2023, Improving Factuality and Reasoning through Multiagent Debate. https://arxiv.org/abs/2305.14325 (a12-a14, b13, c01-c03)
- [V] Wynn, Satija, Hadfield 2025, Talk Isn't Always Cheap. https://arxiv.org/abs/2509.05396 (a16, a17, b18)
- [V] Choi, Zhu, Li 2025, Debate or Vote. https://arxiv.org/abs/2508.17536 (b16, b17)
- [V] Zhang et al. 2025, Stop Overvaluing Multi-Agent Debate. https://arxiv.org/abs/2502.08788 (b15)
- [V*] Smit et al. 2024, Should we be going MAD? https://arxiv.org/abs/2311.17371 (a15, b14, c13, c14, d01)
- [V*] Wang et al. 2024, Rethinking the Bounds of LLM Reasoning. https://arxiv.org/abs/2402.18272 (b11, d02)
- [V*] Revisiting multi-agent debate as test-time scaling. https://arxiv.org/abs/2505.22960 (d03, d04, d20)
- [V*] Yao et al. 2025, Peacemaker or Troublemaker. https://arxiv.org/abs/2509.23055 (a18, a19, b19, c15, c16, c25)
- [V*] Wang et al. 2022, Self-Consistency. https://arxiv.org/abs/2203.11171 (b23, c07)
- [V*] Li et al. 2024, More Agents Is All You Need. https://arxiv.org/abs/2402.05120 (b24)
- [V*] Hegazy 2024, Diversity of Thought in MAD. https://arxiv.org/abs/2410.12853 (b25)
- [V*] Chen, Saha, Bansal 2024, ReConcile. https://arxiv.org/abs/2309.13007 (c17, c18)
- [V*] Chan et al. 2024, ChatEval. https://arxiv.org/abs/2308.07201 (c19, c20)
- [V*] Liang et al. 2024, Encouraging Divergent Thinking via MAD. https://arxiv.org/abs/2305.19118 (c21)
- [V*] Kaesberg et al. 2025, Voting or Consensus? https://arxiv.org/abs/2502.19130 (c22, d19)
- [V*] Panickssery, Bowman, Feng 2024, LLM Evaluators Recognize and Favor Their Own Generations. https://arxiv.org/abs/2404.13076 (a22)
- [V*] Schoenegger et al. 2024, Wisdom of the Silicon Crowd. https://arxiv.org/abs/2402.19379 (a24, b26, c23)
- [V*] Schoenegger, Park et al. 2024, AI-Augmented Predictions. https://arxiv.org/abs/2402.07862 (b27)
- [V*] Tyen et al. 2024, LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516 (c24)
- [V*] Wang et al. 2024, Mixture-of-Agents. https://arxiv.org/abs/2406.04692 (d05)
- [V*] Stechly, Valmeekam, Kambhampati 2024, Self-verification limitations. https://arxiv.org/abs/2402.08115 (d06)
- [V*] Valmeekam et al. 2023, Can LLMs really improve by self-critiquing. https://arxiv.org/abs/2310.08118 (d07)
- [V*] Kamoi et al. 2024, When can LLMs actually correct their own mistakes. https://arxiv.org/abs/2406.01297 (d08)
- [V*] Gou et al. 2024, CRITIC. https://arxiv.org/abs/2305.11738 (d09)
- [V*] Hong et al. 2025, SYCON-Bench. https://arxiv.org/abs/2505.23840 (d10)
- [V*] Fanous et al. 2025, SycEval. https://arxiv.org/abs/2502.08177 (d11)
- [V*] Benchmarking gaslighting negation attacks against reasoning models, 2025. https://arxiv.org/abs/2506.09677 (d12)
- [V*] Kim 2025, Challenging the evaluator. https://arxiv.org/abs/2509.16533 (d13)
- [V*] Can LLM agents really debate? 2025. https://arxiv.org/abs/2511.07784 (d14)
- [V*] Li et al. 2024, Sparse communication topology. https://arxiv.org/abs/2406.11776 (d15)
- [V*] Qian et al. 2025, MacNet. https://arxiv.org/abs/2406.07155 (d16)
- [V*] Arora et al. 2023, Ask Me Anything. https://arxiv.org/abs/2210.02441 (d17)
- [V*] Taubenfeld et al. 2025, Confidence improves self-consistency. https://arxiv.org/abs/2502.06233 (d18)
- [V*] Lorenz et al. 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299/ (b03)
- [V*] Becker, Brackbill, Centola 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5495222/ (b04)
- [V*] Mahmoodi et al. 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4378431/ (b05, b07)
- [V*] Trouche et al. 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC5762162/ (b08)
- [V*] Meta-analysis of the weight of advice, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11661855/ (b09)
- [V*] Zonca et al. 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13547347/ (b10)
- [V] Elga 2007, Reflection and Disagreement. https://swh.princeton.edu/~adame/papers/refdis.pdf (a04-a07)
- [V] SEP, Epistemology of Disagreement. https://plato.stanford.edu/entries/disagreement/ (a01-a03, a25, a26, b01, b02)
- [V] SEP, Epistemology of Testimony. https://plato.stanford.edu/entries/testimony-episprob/ (a08, a09)
- [V] SEP, Social Epistemology. https://plato.stanford.edu/entries/epistemology-social/ (a10, a11)
- [M] Bahrami et al. 2010, Optimally interacting minds. https://pmc.ncbi.nlm.nih.gov/articles/PMC3371582/ (b06; not opened, no numbers used)
- Not reached: Goldman 1999 and Christensen 2007/2009 primary texts (known only through SEP and Elga); Condorcet 1785; Bikhchandani 1992; Zollman 2007/2010; Hong-Page 2004 (via SEP only).
