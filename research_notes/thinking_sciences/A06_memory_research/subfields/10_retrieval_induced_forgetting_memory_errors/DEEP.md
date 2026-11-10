# Retrieval-induced forgetting; memory errors: deep document

*Subfield A06.10. Sources: evidence_a-d.jsonl (ids a01-a27, b01-b28, c01-c26, d01-d20), claims.jsonl (A06.10-K01 to K35), critique.md. All in this folder. Evidence ids below are the short ids (a03, d02 and so on). Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Two linked topics. Both ask: what does a memory system do to related items when it works on one item?

**Retrieval-induced forgetting (RIF).** A person studies a set of related items, for example fruit names. They then practise recalling some of them. Later, the unpractised items from the same set are recalled worse than items from a set that was never practised. The practised items get better. The related unpractised ones get worse. The cost is selective: items from unpractised categories are unaffected.

Standard design (a01, a02):
- Study 48 category-exemplar pairs, 8 categories of 6.
- Practise some exemplars of some categories with a category cue plus a letter stem (about 5 s per item).
- Wait about 20 minutes.
- Test all items.
- Rp+ = practised items. Rp- = unpractised items from practised categories. Nrp = items from unpractised categories.
- RIF = Nrp minus Rp-.

**Memory errors and misinformation.** Memory is rebuilt at recall, so wrong post-event information can overwrite or compete with the original. Loftus and Palmer (1974): the verb in a leading question shifted speed estimates and later reports of broken glass (numbers in section 3 are unverified). Loftus (2005, a24) reviews 30 years of this work. A 2026 meta-analysis (b19) puts the average effect at g=0.694 with huge spread.

**Why it matters for our agent.** The agent keeps lessons by problem class. Two questions follow:
1. Does working on, quizzing, or elaborating one lesson make its sibling lessons less available later? (the RIF risk)
2. Does a wrong or stale item in context or memory get adopted and survive? (the misinformation and supersession risk)

The evidence says the second risk is measured and large in LLMs. The first has been tested once, in one model family, at workshop level.

**Scope note.** Related subfields (Working memory, Calibration, Belief updating, Social epistemology, Debiasing, Conformity) are covered in parallel documents. This one only links to them.

## 2. History and theories in depth

**1974: Loftus and Palmer.** Leading-question wording changed speed estimates. Figures recalled from memory, not opened: smashed about 40.8 mph, hit 34.0, contacted 31.8; a week later 32% vs 14% said they saw broken glass when none was present (b18, c24; unverified). This started the misinformation tradition. Loftus (2005, a24) lists the later findings: warnings sometimes work, the original trace may survive, and rich false events can be implanted.

**1994: Anderson, Bjork and Bjork.** Founding RIF study. Retrieval practice impairs unpractised siblings. Original sizes come from small samples: Exp 2 n=36, and the 1994 paper does not give enough data to compute an effect size (a03, a04; the 1994 PDF itself was not opened).

**1995: Anderson and Spellman.** Cue-independent forgetting: related items tested with a different cue are also impaired. This was taken as the strongest evidence that the trace itself is inhibited, since a new cue should not matter if the problem is only interference at the old cue. Exp 2 n=54 (a27).

**2000-2001: inhibition builds out.** Anderson, Bjork and Bjork (2000) found RIF only when practice needed competitive retrieval. Anderson and Green (2001, a09) added the think/no-think task: repeatedly avoiding a memory makes it harder to recall later. This is a sibling paradigm (suppression), not selective retrieval.

**Rival account: strength-based competition.** Raaijmakers and Jakab built models (SAM) where no inhibition exists. Items just lose in the competition because practised items grow stronger. This account claims:
- the correlation test used as inhibition evidence (practised gain should not predict sibling loss) is not diagnostic: SAM also predicts near-zero between-subject correlation (a06, simulation: mean r=.020, SD .181, only 6.4% significant);
- the restudy dissociation is reproduced if retrieval strengthens much more than a study trial (a07);
- RIF appeared even when practice recalled the category name, so no item competition (a05).

**Other rival: context change.** Jonker, MacLeod and Seli (2013) said practice shifts mental context, and people then search the wrong one. A 2016 replication found context change alone does not cause forgetting (b10, abstract only). Racsmany and Keresztes (2015, a13) found initial full-set retrieval shields siblings, which they read as context support.

**Neural and network models.** Norman, Newman and Detre (2007, a16): oscillating feedback inhibition strengthens weak target parts and weakens competitors. Ritvo et al. and Midler and McClelland (2023, a17): a non-monotonic (U-shaped) plasticity hippocampal network produces RIF; a monotonic one does not; it cannot produce reverse RIF. Wimber et al. (2015, a11): fMRI claimed targeted competitor suppression. A 2018 Cortex reanalysis showed the key interaction depended on coding missing responses as errors, and two behavioural replications found no forgetting (b08).

**2014: the reliability checks.** Rowland, Bates and DeLosh replicated the classic effect but small (d about 0.3 to 0.4) and failed to replicate cue-independence (uninformative, not a refutation). Murayama et al. (2014) pooled 512 samples: g=0.35. Output interference at the final test explains about half of the classic size.

**2020s: applied and AI work.**
- Field-like RIF: campus tours, scavenger hunts (Cinel et al. 2018, a20), autobiographical memory (Matsumoto et al. 2021, a21).
- Moderators: working memory (a22), closure motivation (a19), reward (b12), mPFC stimulation (a12).
- LLM work. Only one study tests RIF directly: Li and Wang 2026 (b25, d08). The rest is analogy: proactive and retroactive interference (Chattaraj and Raj, b23), stale memory (STALE, Supersede, MINTEval), social contagion (Xu et al.), and AI as misinformation source for people (Sim et al., Chan et al.).

**The theoretical state in one line.** Both inhibition and strength competition fit most data. The decisive tests (cue independence, strength independence, neural pattern suppression) have each failed, been undermined, or been shown non-diagnostic. For an engineer this does not matter much: the behavioural effect is real and small, and any cure should be tested directly.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Classic RIF replicates, small | Exp 1 N=72: Nrp .45 vs Rp- .41, t(71)=2.59, p=.01, d=0.31; Rp+ .79. Exp 2 N=140 (online): Rp- .42 vs Nrp .50, t(139)=4.51, d=0.38; Rp+ .63. Original benchmark d33%=0.26 (n=36) | Rowland et al. 2014 (a03, b01, b02) | [E] |
| Originals were small-sample | Anderson 1994 Exp 2 n=36 (d33% 0.26); Anderson and Spellman 1995 Exp 2 n=54 (d33% 0.21) | Rowland 2014 (a04) | [E] |
| Pooled human RIF | 143 papers, k=512 samples, g=0.35 [0.32, 0.38], Q(511)=1381.2, I2=63%; fail-safe N 56,111. Raw: 8.5% overall [7.4, 9.6], 10.9% uncontrolled, 4.5% controlled (3.3 to 5.6) | Murayama et al. 2014 (d01, d03) | [E] |
| Output interference is about half of the effect | Uncontrolled k=256 g=0.50 [0.45, 0.55]; controlled k=280 g=0.22 [0.19, 0.26]; Q(1)=77.0. Text with control g=0.08 [-0.04, 0.21] | Murayama 2014 (d02) | [E] |
| Restudy does not cause RIF | Restudy k=17: g=0.07 [-0.03, 0.17], I2=0. Racsmany: retest RIF t(28)=-3.13, p=.004; restudy t(29)=1.43, p=.16. Contrary: a 2022 paper says restudy of the hurt items removes RIF | d04, a13, b11 | [E] (retrieval act matters); relearn effect [S] |
| Cue-independent RIF is small and failed once | Pooled k=67 g=0.16 [0.09, 0.24]. Rowland Exp 3 N=67: Rp- .56 vs Nrp-similar .52, t(66)=0.92, p=.36; d=-0.05, CI [-0.36, 0.27] (uninformative) | d07, b03, a27 | [C] |
| Competition and strength | Strong exemplars g=0.51 vs weak 0.18 (0.00 once controlled). Rp+ gain vs RIF slope B=0.19 all, B=0.02 [-0.12, 0.16] controlled | d06, d04 | [E] size; [C] meaning |
| Test and design moderators | Category-cued recall k=230 g=0.47 vs cue+stem k=112 g=0.27, Q(1)=26.4. Recognition k=58 g=0.32. Implicit k=42 g=0.18. Between-subject k=37 g=0.51 vs within k=479 g=0.34 | d06 | [E] |
| Delay | >=24 h k=38 g=0.09 [-0.07, 0.25]; without text materials k=21 g=0.40 [0.20, 0.61] vs same-day 0.35 | d06 | [E] |
| Populations | Older adults k=13 g=0.42; children k=10 g=0.56; executive-deficit patients (controlled) k=5 g=-0.03 | d06 | [S] small k |
| Integration removes RIF in text | High integration k=7 g=0.01 [-0.15, 0.17]; low k=7 g=0.25 [0.09, 0.42]; Q(1)=4.71 | d05 | [S] |
| Retrieval-induced facilitation (opposite sign) | Meta k=12 experiments, 4% (CI 2 to 6%) vs 7 to 11% earlier; no delay effect | Oliva and Storm 2022 (b05) | [E] small |
| Initial full retrieval shields siblings | Exp 2 N=30 within-subject: no decrease in related items | Racsmany 2015 (a13) | [C] (context change alone fails, b10) |
| Strong competition and low WM capacity raise RIF | Lowest-WMC: practice recall overlapping 28.6% vs distinct 51.2% (p<.0001); highest-WMC 44.0% vs 43.2% (p=.84). Overall distinct 45.5% vs overlap 34.1%, F(1,122)=22.23 | Mall and Morey 2013 (a22) | [E] direction |
| Closure need raises RIF | High need for closure gave larger RIF in three witness studies (sizes not captured) | Pica et al. 2018 (a19) | [S] |
| mPFC stimulation reduces RIF | N=50: RIF 6.25% (SD 7.36) vs sham 12.83% (SD 7.81); group x item F(1,48)=9.07, p=.004; target accuracy unchanged | Khan et al. 2024 (a12) | [S] |
| Exercise preserves RIF: failed | N=372, five groups; RIF shrank at the second test in all groups; no exercise benefit. Earlier N=158 claim not replicated | Loprinzi 2026 (b06, b07) | [E] null |
| Neural competitor suppression: undermined | Original N=24, recognition 75.2% vs 82.1%, interaction p=.041; reanalysis and two replications found no forgetting | a11, b08 | [C] |
| No single general inhibition process | N=87: RIF (about 8% possible, 10% impossible practice), think/no-think (d=0.55 to 1.02) and Stroop/Go-NoGo did not correlate | Noreen and MacLeod 2015 (a23) | [S] |
| Think/no-think suppression | Pooled g about 0.28 [0.14, 0.43] (search snippet only) | Stramaccia 2020 (b16) | [S] |
| RIF in field-like and autobiographical memory | Campus tour and scavenger hunt: practised raised, unpractised same-location lowered (Exp 1, replicated Exp 2). General autobiographical retrieval lowered specific recall | a20, a21 | [S] |
| Misinformation effect, human | 480 studies, 1,998 effect sizes, N=59,079: g=0.694 [0.259, 1.128], I2=92.21%; warnings after misinformation reduce it | b19 | [E] (preprint, huge spread) |
| Loftus and Palmer 1974 | Smashed about 40.8 mph, hit 34.0, contacted 31.8; 32% vs 14% broken glass a week later | b18, c24 | Unverified (recalled, not opened) |
| Rich false autobiographical memories | 30 studies; lower bound of 80% credibility value d=1.13 | b20 | [S] abstract |
| Corrections of science misinformation | 205 effect sizes, 74 reports, N=60,861: d=0.19, CI -0.06 to 0.43 | b21 | [S] abstract |
| AI summary with one wrong detail distorts people | N=328: correct 83.6% (consistent) vs 44.8% (misleading), chi2=53.9, p<.001; AI vs human label no difference; stop-sign chi2=37.995, yield chi2=25.002 | Sim et al. 2026 (c01, c03) | [S] |
| LLM summaries lose and add detail | 20 summaries of 2 videos: central details omitted 51.6%, 95% omitted the collision, 60% had at least one hallucinated addition | c02 | [S] small |
| Chatbot misleading questions | N=200: over 3x control false memories, 1.7x survey; 36.4% of responses misled | Chan et al. 2024 (b26) | [S] |
| **LLM RIF analogue** | Qwen-2.5-7B -11.2 pp (N=150, p<1e-6); 72B -24.9 pp; list-all-items after: 100% recovery (7B), 98% (72B); same list before elaboration about half (7B), -5% (72B); late-layer attention to targets 0.42x | Li and Wang 2026 (b25, d08) | [S] Qwen only, judge-scored, workshop poster |
| LLM proactive vs retroactive interference | 39 LLMs: proactive worse in 39/39, d=1.73; r=0.21 between the two; params R2=0.491 for retroactive, 0.06 for proactive; accuracy 96.0% at 50 updates, 24.6% at 300; o1 186.4 vs 22.0 | Chattaraj and Raj 2026 (b23, b24, c18, c19) | [S]; authors say not RIF |
| Stale values served | Without update resolution 70.3% of prompts expose a superseded value; keyed memory 92.9% vs keyless 70.4% current-value (diff 0.225, CI 0.161 to 0.296) | Deng and Sinchaisri 2026 (c15) | [S]; the line as a whole [E] with d09, d10, d13, d14 |
| Memory-update gap | gpt-5.4 LongMemEval knowledge-update 92% (full context) to 77% (bounded memory), p<0.005; MINTEval mean accuracy 27.9% | d10, d09 | [S] each |
| Models know it is stale, still use it | Gemini-3.1-pro (label uncertain) State Resolution 92.0% vs Premise Resistance 30.0%; best overall 55.2%; memory frameworks 5.1 to 17.8%; CUPMEM 68.0% | STALE (c10, c12, d11) | [S] |
| Read-time same-slot suppression | Dropping forgetting costs 23.26, 33.33, 23.00 points on three suites; dropping query conditioning costs 11.5 to 18 | Li and Li 2026 (c08, c09) | [S] |
| Wrong hints from memory adopted | Compliance 63% to 72% across five LLMs; success after complying 17% to 31%; placement irrelevant | Compliance Trap (d12) | [S] aggregator page |
| Lossy memory worse than empty | Lossy reclaim 0.00 at the wall; source-first up to 1.0; deployed benchmark lossy about 0.14 at every scale vs 0.60 to 1.00 | Kwon 2026 (c13, c14) | [S] single author |
| Social contagion in agent groups | GPT-5 17.63% to 41.59%; Qwen-235B 25.48% to 74.75%; GPT-5 31.03% to 1.67% long-term; anchoring cuts 46.0% to 17.8%, source scrutiny to 26.5% | Xu et al. 2026 (c04 to c07) | [S] |
| Embedding retrieval reproduces human forgetting | Power-law b=0.460 with competitors vs about 0.009 without; DRM false alarm 0.583 vs human 0.55 | Barman et al. 2026 (c17) | [S] |
| Premature closure in LLMs | 53% to 82% false-action rates when the right option is removed; concision prompts shorten traces 12 to 17% with small, mixed accuracy change | d16, d17 | [S] |

Two label warnings from the critique. In Xu et al., the 15.45% to 35.21% pair sits in the Claude 3.5 Haiku row of Table 3 while the text gives it to Claude 4 Sonnet; do not cite a model for it. In STALE, the 92.0/30.0 row is labelled Gemini-3.1-flash-lite in one place and Gemini-3.1-pro in the text.

## 4. Mechanisms and models

Each is written so it can be coded.

**4.1 Inhibition (Anderson).**
- State: each item i has an accessibility a_i.
- When a cue is presented, all items linked to the cue are candidates. The target competes with competitors.
- Each time a competitor intrudes during practice, a control process lowers its a_i. The cost lands on the competitor, not on the target.
- Predictions: loss grows with competitor strength and the number of intrusions, and shows under other cues (cue independence). Low WM capacity raises RIF (a22), consistent with weaker control being replaced by more interference.
- Weak spots: cue independence failed in one replication (b03); neural pattern suppression undermined (b08); correlation test non-diagnostic (a06).

**4.2 Strength-based competition (SAM, Raaijmakers and Jakab).**
- Recall probability of item i under cue c: s(i,c) divided by the sum of s(j,c) over all items linked to c.
- Practice raises s(target, c) a lot (successful retrieval strengthens far more than a study trial). No weight of any other item changes.
- Rp- items lose only because the practised target now takes a bigger share of the cue's probability mass. Restudy strengthens less, so there is less competition.
- Implement: a softmax over cue-linked item strengths. This alone gives RIF with no inhibition term (a06, a07). It predicts that independent cues should show less loss.

**4.3 Context change (Jonker et al.).** Retrieval practice changes the encoding context vector. At test, the system searches with the old context and finds Rp- items less well. Shielding by initial full retrieval fits (a13); context change alone was not sufficient (b10). Implement as context-vector drift per practice event.

**4.4 Non-monotonic plasticity (Ritvo, Midler and McClelland).** Weight change is a U-shaped function of activation. Moderately active competitors are pushed down; strongly active ones up. Threshold at hidden-unit percentile rank 0.6, each hidden unit linked to 50% of inputs. Produces RIF and pulls competitor representations apart. Fails on reverse RIF (a17, preprint).

**4.5 Embedding-neighbour competition (Barman et al.).** In a vector store, items with near neighbours lose retrievability through interference. Power-law exponent b=0.460 with competitors vs about 0.009 without. Retrieval of a lesson in a crowded neighbourhood may cost its neighbours rank. This is the most direct implementable RIF-like mechanism for our memory, because top-k retrieval is a competition (c17). It tests interference forgetting, not RIF; the link is a hypothesis.

**4.6 Output interference.** The first items recalled in a test displace later ones. About half of the classic effect (d02). Engineer's reading: if you ask the model to recall all siblings in one answer, ordering effects look like forgetting. Probe each item in a separate call.

**4.7 Misinformation as source confusion.** Post-event information competes with the original at retrieval. Source monitoring decides which wins. LLM analogues: leading-premise errors (STALE), stale values (Deng), wrong hints (Compliance Trap), lossy summaries that drop the source (Kwon). In code: no provenance is attached, so old and new items are retrieved with equal weight and nothing adjudicates (c11: old evidence in the top-3 in 60.5% of cases, only 3.3% of these judged to need an update).

**4.8 Attention story for LLMs (Li and Wang).** After elaborating on one item, late-layer attention to the other target tokens falls to 0.42x baseline; masking elaboration positions cuts recovery 21%. One paper's mechanistic claim, abstract level (b25).

## 5. What holds up

**Holds.**
- RIF is real and small. Direct replications d=0.31 and 0.38 (b01, b02). Pooled g=0.35, k=512 (d01). It holds in online samples, shorter designs, field-like material (a20), and autobiographical memory (a21).
- The retrieval act, not mere re-exposure, drives it: restudy g=0.07 (d04).
- About half of the headline size is output interference (g=0.50 vs 0.22; d02). Original claims of 10 to 13 points shrink to 4.5 to 5 raw points once controlled.
- Moderators with decent k: strong competitors, cued category recall, between-subject design, low WM capacity (d06, a22).
- Retrieval practice can help related integrated material by about 4% (b05).

**Failed, contested or weak.**
- Cue-independent RIF: failed once, uninformative; pooled g=0.16 (b03, d07). Counted [C].
- Wimber 2015 neural suppression: reanalysis and two failed behavioural replications (b08).
- Exercise preserving RIF: N=158 claim not reproduced at N=372 (b06, b07).
- Strength independence as inhibition evidence: not diagnostic (a06). Holds only when output interference is controlled (d04).
- Delay: appears to remove RIF (g=0.09) only because text materials are included; without them g=0.40 (d06). Do not read as decay.
- One general inhibition process: not supported (a23, N=87).
- Reward removes RIF (b12): small samples, single lab, abstract only.

**Interventions that reduced RIF in humans** (all [S] or weak): reward (b12), relearning of hurt items (b11), integration of items (d05), initial full-set retrieval (a13, [C]), mPFC stimulation (a12), practising in study order and time pressure on recognition (a15, second-hand).

**Interventions that did not work:** exercise (b06); context change alone (b10); corrections of science misinformation average d=0.19 with a CI that includes 0 (b21); warnings only sometimes (a24).

**Misinformation.** Average g=0.694 with I2=92%, so any single setting can be near zero or very large (b19). Warnings after the misinformation reduce it. Control accuracy is positively linked to effect size. Post-event testing is not a significant moderator.

**Gaps in this record.** Murayama's meta-analysis was read in full (d01 to d07), but no post-2014 meta-analysis was found. The only LLM RIF test has no independent replication. Many null or failed items were seen as abstracts only (a09, a16, a18, a24, b04, b10 to b14, b16 to b22, b27).

## 6. Language models

**How to read this section.** Only Li and Wang test RIF directly. Everything else is a neighbouring failure (interference, staleness, contagion). The authors of the 39-model study say their result is not RIF (b23).

**6.1 Direct RIF test (Li and Wang, 2026; b25, d08).**
- Task: several related items in context. Elaborate on one. Then ask about the others.
- Result: later recall of the unelaborated items drops. Qwen-2.5-7B by 11.2 pp (judge-scored, N=150, p<1e-6). Qwen-2.5-72B by 24.9 pp. The larger model is hurt more.
- Fix: one extra turn after the work saying "list every item by name". Recovery 100% at 7B, 98% at 72B.
- Cue timing: the same list placed before the elaboration recovers about half at 7B and is harmful at 72B (98% vs -5%, a 103 pp gap).
- Mechanism claim: late-layer attention to the other items 0.42x baseline; masking elaboration positions cuts recovery 21%.
- Limits: open-weight Qwen only, no second family, no agentic multi-step run, no arXiv version, a poster in a workshop on failure modes (not main track), judge-scored, token cost not reported (the list is short).

**6.2 Interference between versions of one slot (the measured harm).**
- 39 LLMs (1B to 2.5T): proactive interference (old values block new) far worse than retroactive; d=1.73; opposite to humans. Scale helps retroactive (R2=0.491) but not proactive (R2=0.06, n.s.). Accuracy 96.0% at 50 updates to 24.6% at 300. Proactive accuracy falls from 94% to 3%. Reasoning models 178.0 vs 150.3 on retroactive. o1 first on retroactive (186.4), 35th on proactive (22.0). Intrusions are same-key old values (56.1%); hallucination under 1% (b23, b24, c18, c19).
- Latest-state accuracy falls with the number of updates; earliest-state stays high; heuristic fixes modest (d13). Accuracy falls log-linearly as overwritten values accumulate; "ignore earlier input" helps little (d14).
- MINTEval: mean accuracy 27.9% over 15.6k QA pairs, contexts up to 1.8M tokens; earlier revised facts are hardest (d09).

**6.3 Stale memory in agent stores.**
- 70.3% of prompts expose a superseded value without update resolution; keyed memory 92.9% vs 70.4% (c15).
- Bounded self-maintained memory on gpt-5.4: 92% to 77% on knowledge updates; 24x longer conversation 68% to 28% (n=25 cell) (d10).
- STALE: models can state a belief is outdated but still answer from it when the question presupposes it (Premise Resistance 30% vs State Resolution 92% in one model); memory frameworks 5.1 to 17.8%; write-time labels (CUPMEM) 68.0%, about $0.37 per instance; no ablation, no false-stale rate (c10 to c12, d11).
- Read-time same-slot suppression (RD-Forget): dropping forgetting costs 23 to 33 points; recency alone cannot tell competing from complementary facts (c08, c09). This is a deliberate, curated analogue of RIF. Its risk is the human-RIF risk: hiding still-valid siblings.

**6.4 Context contamination and wrong hints.**
- Wrong memory or tool-block advice followed 63% to 72% of the time across five LLMs; success after complying 17% to 31%; placement does not matter; showing memory only after a failed attempt is safer (d12, aggregator page).
- Peer-claim contagion: GPT-5 error 17.63% to 41.59%; Qwen-235B 25.48% to 74.75%; long-term shifts much smaller for GPT-5 (31.03% to 1.67%). Model size does not protect (max shift 89.3% at 8B to 92.2% at 235B). Defences: state own prior then check claims (46.0% to 17.8%), source scrutiny (to 26.5%) (c04 to c07).
- Lossy compression that keeps the conclusion and drops the source makes the model re-emit the error; source-first memories reclaim (c13, c14).
- LLM summaries omit central details 51.6% of the time and 60% add at least one hallucination (c02). Summarising a lesson is itself a lossy, error-adding step.

**6.5 Neighbour competition in retrieval.** Embedding spaces produce power-law forgetting (b=0.460) and DRM false alarms (0.583 vs 0.55) from neighbour competition alone (c17). This suggests top-k lesson retrieval has a built-in competition cost when lessons are near-duplicates. Untested for our store.

**6.6 What we looked for and did not find (d20).** No RIF test on a Claude-family or other frontier model. No test of retrieval from a memory store causing sibling loss. No restudy-vs-apply test. No integration-as-shield test. No think/no-think analogue measuring collateral loss. No collateral-loss measurement for write-time stale labels. No closure-pressure test on rejected alternatives. The search was rate-limited, so a fresh run could find newer papers.

**6.7 Related, not RIF.** ICF-Bench: models struggle to drop interfering information while keeping useful context (d15). Premature closure: 53% to 82% false actions when the correct option is removed (d16). Concision prompts: 12 to 17% shorter traces, small mixed accuracy changes; early-answer instruction +3.8 points on MMLU-Pro at 512 tokens (d17). Drift after about 2,000 tokens on relational recovery (c20). Refusal inertia: models stay consistent with their own earlier output (c21).

## 7. What our agent should take

Schema parts: G = guardrails, S = states, O = operators, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Probe sibling lessons one at a time (G, test design, [E]).** In any harness check of lesson interaction, probe each sibling lesson in a separate call, random order, never as one free-recall answer. Output interference is about half of the classic RIF size. Evidence: d02, K29.
2. **Set sibling-damage thresholds at replication scale (G, [E]).** Expect 0.2 to 0.35 sd, about 5 raw points, not 10 to 13. A check that flags less is chasing noise. Evidence: d01, d02, d03, a04, b01, K02, K28.
3. **Slot-keyed lesson store, newest version wins, old versions kept but tagged and hidden from default retrieval (memory, [E] as a principle).** Same-slot supersession is the measured harm: keyed memory 92.9% vs 70.4% current-value (c15), 92% to 77% (d10), proactive interference d=1.73 (b23), latest-state accuracy falls with updates (d13, d14). Specific numbers are each single-source; the direction is consistent across five independent sources. Evidence: c15, d09, d10, d13, d14, c10, K16, K33.

Everything else is held back. In particular, do not add a "sibling-protection" step to the schema yet: it rests on one Qwen-only workshop poster.

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Does elaborating or quizzing one lesson lower use of its siblings on our model? (the RIF guardrail) | G | [S] | b25, d08, K13 |
| T2 | A post-work "list every lesson by name" turn restores sibling use; place it after, not before | O / S | [S] | b25, d08, K13, K14 |
| T3 | Retrieval from a store (top-k) lowers retrieval of near-duplicate neighbours | memory | [S] | c17, K24 |
| T4 | Source plus conclusion in lesson summaries beats conclusion-only | memory | [S] | c13, c14, K19 |
| T5 | Write-time keep/stale/replace labels, and their false-stale rate | memory / G | [S] | c10 to c12, d11, K17, K18 |
| T6 | Own-prior anchoring and source scrutiny against wrong hints; gate hints behind a first failed attempt | G | [S] | c07, d12, K23, K32 |
| T7 | Linking sibling lessons in one schema protects them | O / memory | human [S], LLM untested | d05, b05, K30, K11 |
| T8 | Apply vs re-read a lesson: does sibling damage differ | O | human [E], LLM untested | d04, a13, K03 |
| T9 | Full-set recall pass before selective practice protects siblings | S / O | [C] | a13, b10, K06 |
| T10 | A "drop the wrong idea" step lowers later access to related correct ideas | O | untested | a09, b16, d14, d15, K12 |
| T11 | Closure pressure ("answer fast") lowers retention of rejected alternatives | G | untested | a19, d16, d17, K08, K35 |
| T12 | Warning-after step against misleading context (human warnings work, b19) | G | human [E], LLM untested | b19, a24, K20 |

Full test designs are in section 8 and in UNKNOWNS.md.

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens (count extra turns and extra lesson text against the treated arm, and pad control arms with neutral filler). Items: 6 to 8 problem classes, 4 lessons per class, 20 to 40 problem sets per class. Use the benchmark mix we already run (ARC portfolio, BRAINTEASER) plus a synthetic lesson set where every lesson has one checkable fact.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 sibling damage | In-context lesson set (K=4 siblings). Treated: elaborate on or quiz 1 lesson | A: elaborate one, probe other 3 separately. B: no elaboration, equal-length filler. C: elaborate a lesson from an unrelated set | Accuracy on siblings, each probed in its own call; RIF = B minus A | Li and Wang: -11 pp (7B) to -25 pp (72B). Human scale: 5 points. Add guardrail if drop >=5 pp with CI excluding 0 |
| T2 list-all fix | Same as T1 | A: elaborate then list-all turn. B: list-all before elaboration. C: no list-all | Sibling accuracy recovery; tokens added | Recovery 90%+ after; near zero or harmful before (98% vs -5% on 72B) |
| T3 store competition | Retrieved-memory store with near-duplicate lessons (density 1, 3, 8 neighbours) | A: retrieve and use lesson X n times. B: no uses. Then query siblings | Recall@k of siblings; correct use rate | Neighbour density raises loss (c17). Human scale about 5% |
| T4 source-first | Lesson summaries: conclusion only vs conclusion plus source | Equal-length summaries | Rate of re-asserting a corrected error; reclaim rate after correction | Kwon: reclaim near 1.0 vs near 0.14 |
| T5 stale labels | Lesson updates (same-slot) mixed with complementary lessons | A: write-time keep/stale/replace labels. B: append-only. C: keyed overwrite | Current-value accuracy; false-stale rate (complementary lessons wrongly hidden) | CUPMEM 68% vs 8.7 to 17.8% baselines; unknown is false-stale rate. Reject if false-stale >5% |
| T6 wrong-hint defence | Tasks with a planted wrong hint in a tool result or memory block | A: anchor own prior first. B: source scrutiny. C: hint shown only after first failed attempt. D: plain | Hint adoption rate; final accuracy | 46.0% to 17.8% anchoring; compliance 63 to 72% baseline |
| T7 integration | Siblings stored unlinked vs one linked schema; apply one, probe others | Equal total lesson text | Sibling accuracy after apply | Human: integration removes RIF (g=0.01 vs 0.25); LLM unknown |
| T8 apply vs re-read | One lesson re-read in context vs applied to a task | Equal tokens (padded re-read arm) | Sibling accuracy | Human: re-read g=0.07. LLM unknown |
| T9 shield | Full-set recall before selective practice | A: full-set list then practice. B: practice only | Sibling accuracy | Human small-n [C]; likely overlaps T2 |
| T10 drop idea | After a failed attempt, instruct "drop this idea" vs silence | Equal tokens | Accuracy on later related correct approach | Unknown; ICF-Bench suggests ignore-prompts help little |
| T11 closure | "Answer fast" vs neutral prompt | Equal tokens | Retention of 2 rejected alternatives in a later probe | Human: high closure raises RIF |
| T12 warning-after | Context with one planted wrong claim | A: warning step after. B: no warning. C: warning before | Adoption of the wrong claim | Human: warnings reduce effect; Compliance Trap: placement did not matter |

**Run rules.** At least 3 seeds. Pre-register the threshold. Report per-model results; never pool model families. Use judge-free checks (exact fact match) wherever possible, since Li and Wang is judge-scored. Run T1 and T2 on at least two model families including ours.

## 9. What does not transfer, and why

- **Human size and mechanism.** Human RIF is 4.5 to 5 raw points controlled. The Li and Wang LLM drop is 11 to 25 pp in a different setup. They are not comparable. An LLM has no inhibition control process; if it shows RIF it is attention dilution or context contamination, not inhibition.
- **Cue independence and fMRI.** Neither has an LLM counterpart, and both are shaky in humans (b03, b08).
- **Time and sleep.** Delay and sleep effects (b28, d06) have no analogue inside one in-context run.
- **Exercise, tDCS, reward, closure as a trait.** Biological or motivational moderators (a12, b06, b12). Only closure has a prompt-level analogue and it is untested.
- **Misinformation on people.** Sim et al. and Chan et al. (c01, b26, K21) are about human users. They inform summary quality, not agent design.
- **The 39-model interference result.** It is proactive and retroactive interference on key-value updates, not selective retrieval. The authors say so (b23). Do not cite it as RIF evidence.
- **Group contagion.** Xu et al. uses simulated peers in multiple choice. The false memory is injected, not self-generated. Our single agent has no peers, but wrong tool outputs and hints have the same shape.
- **Word-list percentages.** Human raw points are for word-list recall (d03); text materials show g=0.08 when controlled. Our lessons are closer to text, so human damage may be smaller still.
- **Generalising Qwen.** Open-weight Qwen only. That the larger model was hurt more is unexplained and could be Qwen-specific.

## 10. Open questions

1. Does a Claude-family or other frontier model show RIF at all? (d20: no test found.)
2. Does the Li and Wang fix hold on a second family and in multi-step agent runs? What does it cost in tokens? Is the result judge-dependent?
3. Does retrieving a lesson from a store hurt near-duplicate siblings, and which loads more: same-slot supersession or sibling suppression?
4. Does apply vs re-read differ for LLMs, as the restudy dissociation says for humans?
5. Does linking siblings in one schema protect them in an agent? (Human evidence: 7 text samples per cell.)
6. Do write-time stale labels hide complementary facts? What is the false-stale rate?
7. Does a "stop thinking about the wrong idea" step harm related correct ideas?
8. Does closure pressure reduce retention of rejected alternatives? (Concision prompts changed accuracy little.)
9. Which defence beats misleading context at equal tokens: warning-after, own-prior anchoring, source scrutiny, hint gating? Does it hold for tool-output hints?
10. Is the pooled human RIF still g=0.35 after 2014? No post-2014 meta-analysis was found.
11. Is LLM RIF an attention effect (Li and Wang, 0.42x) or a context-contamination effect, and does the distinction change the fix?
12. Why was the 72B model hurt more than the 7B?

## 11. Sources

[V] = opened and read this session (full text or full page; abstract-page-only reads are noted). [M] = snippet or abstract only, or numbers from memory.

**Human RIF**
- [V] Rowland, Bates and DeLosh (2014) On the reliability of retrieval-induced forgetting. https://europepmc.org/article/PMC/PMC4240037 (also https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4240037/) (a03, a04, a27, b01 to b03)
- [V] Murayama, Miyatsu, Buchli and Storm (2014) meta-analysis, Psychological Bulletin. https://centaur.reading.ac.uk/37052/1/Murayama%20et%20al_2014_PB.pdf (d01 to d07). DOI https://doi.org/10.1037/a0037505 [M] (a08, b04)
- [M] Anderson, Bjork and Bjork (1994) Remembering can cause forgetting. https://doi.org/10.1037/0278-7393.20.5.1063 (a01, b17, c25; paradigm known from secondary sources only)
- [V] Raaijmakers and Jakab (2012) RIF without competition. https://europepmc.org/article/PMC/PMC3246582 (a05, c23)
- [V] Raaijmakers (2016) strength independence. https://europepmc.org/article/PMC/PMC5050235 (a06, a07; b09 is the same paper, [M])
- [V] Anderson and Hanslmayr (2014) review. https://europepmc.org/article/PMC/PMC4045208 (a10)
- [V] Wimber et al. (2015). https://europepmc.org/article/PMC/PMC4394359 (a11)
- [V] Reanalysis and failure to replicate Wimber et al., Cortex 2018. https://doi.org/10.1016/j.cortex.2018.03.026 (b08, abstract read in full)
- [V] Khan et al. (2024) mPFC stimulation. https://europepmc.org/article/PMC/PMC11391495 (a12, b14)
- [V] Racsmany and Keresztes (2015). https://europepmc.org/article/PMC/PMC4440349 (a13)
- [V] Spitzer (2014). https://europepmc.org/article/PMC/PMC4179646 (a14)
- [V] Wikipedia, Retrieval-induced forgetting. https://en.wikipedia.org/wiki/Retrieval-induced_forgetting (a02, a15, a25, a26; tertiary, second-hand)
- [M] Norman, Newman and Detre (2007). https://doi.org/10.1037/0033-295x.114.4.887 (a16)
- [V] Midler and McClelland (2023) preprint. https://doi.org/10.1101/2023.08.25.544249 (a17)
- [M] Kovacs and Harris (2022). https://doi.org/10.1080/09658211.2021.2013504 (a18)
- [V] Pica et al. (2018). https://europepmc.org/article/PMC/PMC6206073 (a19)
- [V] Cinel, Cortis Mack and Ward (2018). https://europepmc.org/article/PMC/PMC5944391 (a20)
- [V] Matsumoto et al. (2021). https://europepmc.org/article/PMC/PMC8667590 (a21)
- [V] Mall and Morey (2013). https://europepmc.org/article/PMC/PMC3543406 (a22)
- [V] Noreen and MacLeod (2015). https://europepmc.org/article/PMC/PMC4536050 (a23)
- [V] Oliva and Storm (2022) retrieval-induced facilitation. https://pmc.ncbi.nlm.nih.gov/articles/PMC9425789/ (b05)
- [V] Loprinzi, Shopeju and Storm (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13461884/ (b06, c22). Earlier 2023 paper [M] https://doi.org/10.1007/s00426-022-01758-9 (b07)
- [M] Context change not sufficient (2016). https://doi.org/10.1080/17470218.2015.1076866 (b10)
- [M] Relearning eliminates RIF (2022). https://doi.org/10.1007/s00426-021-01601-7 (b11)
- [M] Reward eliminates RIF (PNAS 2014). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4260611/ (b12)
- [M] WMC and task type (2016). https://doi.org/10.1080/09658211.2015.1117640 (b13)
- [V] Think/No-Think methods guide (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11133138/ (b15)
- [M] Anderson and Green (2001). https://doi.org/10.1038/35066572 (a09); Stramaccia et al. 2020 meta-analysis https://pure.mpg.de/pubman/item/item_3173315_2/component/file_3173317/Stramaccia_2019.pdf (b16)
- [V] Resurrected memories, sleep (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8642353/ (b28)

**Misinformation**
- [M] Loftus and Palmer (1974). https://doi.org/10.1016/S0022-5371(74)80011-3 (b18, c24; numbers from recall)
- [M] Loftus (2005). https://doi.org/10.1101/lm.94705 (a24)
- [V] Misinformation meta-analysis 2026 preprint. https://doi.org/10.31234/osf.io/m68kf_v6 (b19, abstract)
- [M] Rich false memory meta-analysis (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10126919/ (b20); science misinformation correction meta-analysis https://pmc.ncbi.nlm.nih.gov/articles/PMC12397989/ (b21); bypassing vs correcting https://pmc.ncbi.nlm.nih.gov/articles/PMC12085712/ (b22)
- [V] Chan et al. (2024). https://arxiv.org/abs/2408.04681 (b26)
- [V] Sim, Eiger and Kohno (2026). https://arxiv.org/abs/2609.28820 (c01 to c03)

**LLM and AI**
- [V] Li and Wang (2026) RIF in LLMs, ICML workshop poster page. https://icml.cc/virtual/2026/77864 (b25, d08; full paper not read)
- [V] Chattaraj and Raj (2026). https://arxiv.org/abs/2603.00270 (b23, b24, c18, c19)
- [V] Xu et al. (2026) Mandela effect. https://arxiv.org/abs/2602.00428 (c04 to c07)
- [V] Li and Li (2026) RD-Forget. https://arxiv.org/abs/2609.10263 (c08, c09)
- [V] Chao et al. (2026) STALE. https://arxiv.org/abs/2605.06527 (c10 to c12); page re-read https://arxiv.org/html/2605.06527 (d11, first 100k characters)
- [V] Kwon (2026) Reclaim evaluation. https://arxiv.org/abs/2606.25449 (c13, c14)
- [V] Deng and Sinchaisri (2026). https://arxiv.org/abs/2610.10265 (c15, c16)
- [V] Barman et al. (2026) Geometry of forgetting. https://arxiv.org/abs/2604.06222 (c17)
- [V] Yousuf et al. (2025). https://arxiv.org/abs/2510.03611 (c20)
- [V] Cai (2026). https://arxiv.org/abs/2609.16777 (c21)
- [V] Cao et al. (2023). https://arxiv.org/abs/2305.09144 (b27, abstract, no numbers)
- [V] MINTEval, Lee et al. (2026). https://arxiv.org/abs/2605.18565 (d09, abstract page)
- [V] Supersede, Patel (2026). https://arxiv.org/abs/2606.27472 (d10)
- [V] Compliance Trap, Chen, Bai and Yuille (2026). https://www.alphaxiv.org/abs/2607.10608v1 (d12, aggregator overview)
- [V] Qiao et al. (2026). https://arxiv.org/abs/2603.12271 (d13, abstract)
- [V] Wang and Sun (2025) Unable to Forget. https://arxiv.org/abs/2506.08184 (d14, abstract)
- [V] ICF-Bench, Qian et al. (2026). https://mlanthology.org/iclr/2026/qian2026iclr-llms/ (d15, abstract)
- [V] Handler, Bedi and Shah (2026). https://arxiv.org/abs/2605.15000 (d16, abstract)
- [V] Carlon, Ginis and Algaba (2026). https://arxiv.org/abs/2608.03401 (d17, abstract)
- [M] Hybrid think/no-think snippets https://arxiv.org/html/2510.12680v1 (d18); FadeMem https://arxiv.org/pdf/2601.18642 and OBLIVION arXiv 2604.00131 (d19)
- Negative search result for frontier-model RIF: d20 (APIs rate-limited; coverage incomplete).
