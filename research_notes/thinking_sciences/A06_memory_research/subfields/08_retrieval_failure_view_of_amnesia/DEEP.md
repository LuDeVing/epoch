# Retrieval failure view of amnesia: deep document

*Series A06 (memory research), subfield 08. Evidence ids (a01 to d20) point to evidence_a-d.jsonl. Claim ids (K01 to K27) point to claims.jsonl. Known weak points are in critique.md. Overlap with earlier documents: encoding specificity and cue-dependent forgetting (see 01_encoding_specificity in this series), interference, reconsolidation. Parallel subfields noted only as links: Semantic networks and spreading activation, Dynamic memory (early CBR), Working-memory limits and chunking, Confidence and metacognition.*

## 1. What it is

The retrieval failure view says this. Many memory losses are not losses of the stored trace. They are losses of access. The trace is still there. The cues at test do not reach it. Change the cue, and the memory comes back.

The recent statement is Alfei, Miller, Ryan and Urcelay (Psychological Review 2025, vol 133 issue 2, pp 411-449, doi 10.1037/rev0000538) [a01, c01]. It is a review. It has no new data. Its claim: amnesic treatments given after training or after reactivation (protein synthesis blockers, electroconvulsive shock, new learning) do not erase memory. They add new learning that competes with the original. The original is then expressed only with the right cues. The abstract says most such deficits can be reversed. The text says "most if not all" (K01). That strong form is advocacy and is not proven [a01, d01].

The review makes a map (its Table 1). The same few recovery manipulations are said to work across many phenomena: extinction, counterconditioning, retrieval-induced forgetting, cue interference, cue competition (overshadowing, blocking), post-training amnesia, cue-induced amnesia. The manipulations are: time passing, the original physical context, the original state context (including re-giving the drug), a retrieval cue (the CS or a part of it), a reminder of the outcome (the US), and, in mice, light on tagged engram cells [a02, d04].

Why it matters for our agent. A failed answer is not proof the knowledge is gone. A thinking scaffold should try more than one cue before it says "unknown". It should also know when this idea does not hold: a fact never stored cannot be cued back.

What the evidence supports, in one paragraph. Mouse engram rescue is real and repeated, but by related labs and with artificial light cues [K02]. Rat reminder and re-dosing effects are real but come from one lab family [K04]. Human erasure by reminders is weak or contested [K05, K06, K18]. In language models, five lines of work show lost access is not lost storage [K10 to K13, K21]. No study tests the exact human cue-reinstatement idea in a language model [K19]. The link between the two literatures is ours, not the authors'.

## 2. History and theories in depth

**Availability versus accessibility (1960s).** Tulving and Pearlstone (1966): people learn categorised word lists, try free recall, then get category cues. Words missed in free recall come back with cues. So many failures are of accessibility, not availability [a26, not opened; described by Alfei et al.]. No numbers are recorded from the primary. Tulving and Thomson (1973) added encoding specificity: recall depends on the match between encoding and retrieval conditions [a27, not opened]. Tulving et al. (1983) brought back Semon's "ecphory", the interaction of trace and cue. Nairne (2002) added a limit: what matters is the diagnostic value of a cue, how well it separates the target from competitors, not raw overlap. A school uniform cue works among adults and not in a cafeteria of schoolboys [a07].

**Amnesic patients (1970).** Warrington and Weiskrantz (1970), Nature 228: amnesic patients kept verbal material when tested with partial-information cues. Retention depended more on the test method than on the learning method. Long-term memory showed when the test removed wrong and interfering responses [a25, abstract only]. This was later split into spared implicit memory versus impaired explicit memory.

**The storage (consolidation) view.** Muller and Pilzecker (1900): recall of syllable pairs suffered when a new list followed within about a minute. Duncan (1949): electroconvulsive shock (ECS) up to 15 minutes after rat avoidance training gave amnesia; beyond 1 hour it did not. Protein synthesis inhibitors (puromycin, anisomycin, cycloheximide) later gave the same time gradient [a08]. The gradient is the main evidence for permanent loss.

**Reconsolidation.** Nader, Schafe and LeDoux (2000): anisomycin in the amygdala after reactivation of a tone-shock fear memory caused later amnesia. No reactivation: no amnesia. A 6 hour delay: no amnesia. Reactivation at 1 or 14 days gave the same result [a24, a09]. Duvarci and Nader (2004) saw no spontaneous recovery (test 23 days later), no renewal and no reinstatement. The review argues that non-recovery may reflect narrow test parameters and the use of an intermediate test, which can itself act as a reminder (Wheeler and Miller 2007) [a09, d02].

**The 1960s to 1980s recovery work.** Spontaneous recovery over time (Cooper and Koppenaal 1964; Zinkin and Miller 1967; Quartermain 1970, 1972). US reinstatement (Misanin, Miller and Lewis 1968). CS reminder (Deweer and Sara 1981). Re-giving the amnesic agent as a state cue. Miller and Springer (1973), Psychological Review 80: "at least some experimental amnesia is retrieval failure" [a28, b24; quoted second-hand]. Miller and ECS: ECS 0.3 s after one training session left performance intact at 15 min but poor at longer delays. Prior familiarisation with the apparatus reduced the ECS deficit (Lewis, Miller, Misanin 1969). A usable memory formed, then was impaired [a10, a11]. Most of this is small-group rodent work with varied parameters and no numbers in the review.

**Time and context in interference.** Sissons and Miller (2009): A+ then B+/BA- training versus the reverse order. Tested right after phase 2, behaviour follows the latest training. After a 27-day gap, the first-learned association dominates. Second-learned information is what depends on time and context [a03]. Escobar, Matute and Miller (2001): X+ in one context, Y+ in another. Testing X in Y's context gave strong interference; in X's own context, little. Same logic as ABA renewal after extinction [a04]. Cue competition also recovers with time (overshadowing: Miller, Jagielo and Spear 1990; blocking: Batsell 1997) and with retrieval cues (Cole 1999; Schachtman 1983) [a05]. Retrieval-induced forgetting (Anderson, Bjork and Bjork 1994) has an inhibition account and two interference accounts. It vanished after a 24 h delay in some studies and with context change (Jonker 2013), not in others (Maxcey 2021; Soares 2016) [a06]. The authors lean on the positive cases.

**Memory integration account (Gisquet-Verrier and Riccio).** During an active memory (new or reactivated), salient information, including the internal state caused by the drug, is bound into the memory. At test that state is missing, so retrieval fails. Prediction: re-give the drug before the test, and amnesia reverses. Also: the time gradient reflects how active the memory is, not consolidation speed [a14, a29, b22]. It is a close rival of the "new learning" account, not the same thing.

**Modern engram work.** Ryan et al. (2015, Science): see section 3. Roy et al. (2016) early-Alzheimer mice. Roy et al. (2017, PNAS) silent engrams and spine density. Guskjolen et al. (2018) infant memories. Abdou et al. (2018) a counter-case. Sarma et al. (2026) sleep loss [a15 to a17, b02, b03, b05, d05, d06].

**Prediction error as a gate.** The review proposes that a prediction error at reactivation opens the memory to change. Rescorla-Wagner: learning scales with the gap between outcome and summed expectation. Mackintosh uses stimulus-specific error. Pearce-Hall uses unsigned error to set attention. The link from error to destabilisation is itself contested [a13]. Stout and Miller (2007) SOCR model: a retrieval-stage comparison turns associative strength into performance [a30, not opened].

**Adaptive forgetting.** Miller (2021) argues impaired retrieval of tangential information beats erasure, because what is tangential today may matter tomorrow (William James, 1890, as cited). Autore et al. (2023): retroactive interference in mice made the original engram less likely to reactivate; an interference engram dominated [a31].

**Competing views.** (1) Consolidation / erasure. (2) Reconsolidation blockade. (3) Memory integration. (4) Retrieval failure (new learning). (5) Cue overload / diagnostic cue value. Human reconsolidation critiques: Psychonomic Bulletin 2023 says the theory and its boundary conditions are vague enough to be close to unfalsifiable [a22]. The same critique applies to the retrieval view: "narrow parameters" can explain any non-recovery [a01 limits, d02].

## 3. Core findings with exact numbers

Status as in claims.jsonl: established, single-source, contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Light on tagged dentate gyrus engram cells restores freezing after anisomycin amnesia | Natural recall: ANI < SAL, p<0.005 (Test 1), p<0.05 (Test 2). Light: SAL p<0.01, ANI p<0.05, no group difference. DG n=10 ANI / 12 SAL; CA1 n=9/10; amygdala n=9/9; reconsolidation design n=11/11 | Ryan 2015 [a16, b02] | established (K02), rodent only |
| CA1 engram needs a 4 Hz protocol, not 20 Hz | CA1 light freezing SAL p<0.01, ANI p<0.001 (n=10, 9). Chance overlap CA3 0.76, BLA 0.42 | Ryan 2015 [b23] | single-source, protocol-sensitive |
| Rescue after reactivation plus anisomycin too | Reconsolidation DG: SAL p<0.001, ANI p<0.003, n=11 per group, day 4 | Ryan 2015 [b23] | single-source |
| Silent engram persists 2, 5, 8 days; needs strong light | n: 2 d 10/12, 5 d 9/10, 8 d 9/8. Anisomycin 150 mg/kg. Laser 25% power (1.5-2.5 mW) fails (n=8); 50% and 75% work. DG spines saline 7,045 (7 mice) vs ani 5,789 (6 mice). PAK1 rescue of natural recall, n=15 per group | Roy 2017 [b03] | single-source |
| Early-Alzheimer mice: engram light rescues memory | APP/PS1 at 7 and 9 months. Spines 7,032 (AD) vs 9,437 (control), n=4 mice per group. Rescue n=10, F(1,36)=4.95 P<0.05. Inhibitory avoidance F(1,27)=25.22. Novel object F(1,56)=5.87 | Roy 2016 [a17] | single-source (K03) |
| Sleep loss: engram light restores social recognition | n=9 to 12 per group. Exploration at test not reduced. Roflumilast rescue only transient | Sarma 2026 [b05, b06] | single-source, same lineage |
| Counter-case: light on auditory inputs fails after complete amnesia | Abstract only; n not read | Abdou 2018 [d05] | single-source dissent |
| Infant memory returns with DG stimulation up to 3 months after training | Abstract only | Guskjolen 2018 [d06] | single-source, other lab |
| Reminder or re-dosing reverses cycloheximide amnesia in rats | Cyclo 2.8 mg/kg. Amnesia F(1,15)=28.39 p<.001; reminder reversal F(1,15)=8.40 p<.01. Reactivation: amnesia F(1,17)=8.78; reversal F(1,18)=7.945. ICV reinfusion F(1,11)=5.86 p<.05. Protein synthesis cut 72% at 30 min. Groups 5 to 11 | Gisquet-Verrier 2015 [a18, b04, b22] | single-source (K04) |
| LiCl (no protein synthesis block) gives the same pattern | 300 mg/kg: amnesia F(1,18)=72.39; re-injection reversal F(1,16)=7.43 p=.014. Protein synthesis up 3-5% | Gisquet-Verrier 2015 [a18, b04] | single-source; malaise confound |
| Midazolam amnesia generalises to a similar context, recovers in the original | Exp1 N=32 (8/group) F(3,28)=8.11 eta2p=.46. Exp3 N=48 AAB d=1.90, ABB d=1.72, ABA d=0.08. Exp4 N=16 d=1.96. Exp5 N=56 | Alfei 2020 [a19] | single-source (K20) |
| Walker 2003 motor-sequence reminder amnesia fails to replicate | Original about -57% accuracy (group of 16). 4 direct replications n=16 each, N=64: +3.13, +0.08, -1.98, -2.64 %; BF01 8.97, 5.38, 1.90, 1.85; pooled BF01 5.74 (accuracy), 36.0 (speed). 3 conceptual, N=48: t(26.59)=-1.409 | Hardwicke 2016 [a20] | established (K05) |
| Reminder raises intrusions, not erasure, in humans | Exp1 groups of 12; U=20.00, p<0.01. Exp3 N=24; intrusion about 5.4% (about 1 of 20 items) | Hupbach 2007 [d07] | contested (K27) |
| Propranolol reconsolidation blockade, meta-analysis | Healthy g=-0.51 (p=0.002; 14 studies, n=478). Clinical g=-0.42 (p=0.010; 12 studies, n=446). The "618 vs 527" figure in b07 is unverified | Pigeon 2022 [b07]; critique item 3 | contested (K06) |
| Same studies, restricted | Low-risk-of-bias RCTs: not significant; interval wider with new trials. Pooled g in forest plots only | Steenen 2022 [b08, d09] | contested |
| Healthy-human propranolol replication fails | N=44; 40 mg; no effect on fear-potentiated startle; BP effect t(43)=10.54 d=1.59 | b10 (2014) | single-source |
| Schiller 2010 depends on exclusions | 7 analysis sets; with principled exclusions fear recovery similar | Verification report 2020 [a23] | single-source |
| Post-retrieval extinction meta-analysis | 63 comparisons. Humans fear g=0.40; animal appetitive g=0.89; animal fear g=0.21 (ns) | Kredlow 2016 [a21] | single-source (K07) |
| Cued recall still impaired in bvFTD | Cued delayed recall -1.25 (CI -1.51 to -0.98), 209 vs 235, 8 studies; free immediate -1.98, 271 vs 520, 7 studies | FCSRT meta-analysis 2024 [b11] | single-source (K09) |
| Review has no tally of failed reversals | About 8 failure citations in human section; no pooled effect; Table 1 shows noteworthy examples only | Alfei 2025 preprint [d01 to d03] | established (K22) |
| LLM spurious forgetting | Task 0 accuracy about 100% to about 10% in 150 steps; recovery probe 100% falling to 96%. Safety 100% to 0% then about 99% after 10 safety instances | Zheng 2025 [c02, c03] | established (K10) |
| Unlearned knowledge returns with 10 unrelated samples | WMDP-Bio base 64.4; RMU/NPO/DPO 29.9/29.5/27.9 to 61.6/52.7/57.0. MMLU drop under 2 points. 1000 samples: full recovery | Lucki 2025 [b17, c05 to c07] | established (K11) |
| Prompt-only recovery of unlearned knowledge | WMDP-Bio prefix: RMU 29.9 to 53.9; NPO 29.5 to 46.0; DPO 27.9 to 49.0. Cyber (base 42.6): 27.7 to 35.3; 32.7 to 37.0; 33.5 to 36.7 | Lucki 2025 [d10] | established (K21) |
| Format changes recovery | RMU ablation 53.7% with chat template, 34.1% without. Prefix 31.2% without vs 51.4% with template | Lucki 2025 [b18] | single-source |
| Recovery from disjoint facts | At least 88% of pre-unlearning accuracy for pretraining-era facts. Fine-tuned-in facts: GD and RIA under 35% | Deeb and Roger 2025 [b13] | established (K11) |
| Benign relearning | Keyword attack success above 70% on shallow unlearning. Relevance: text ending in the answer 100%, female names 20%, Japanese 9%, gibberish 9%, none 0% | Hu 2025 [b15] | established (K11) |
| Depth and repetition on a toy task | 7 pairs: shallow 8%, medium 48%, deep 100%; 3 pairs 1%, 1%, 23%; 1 pair 0% (column mapping inferred) | Hu 2025 [b16] | single-source |
| Who's Harry Potter resurfaces | Familiarity 77% below baseline; 800 sentences (1% of corpus) partial; 8,000 sentences (10%) close to baseline | Lynch 2024 [b19, d11] | single-source |
| Models encode answers they do not say | 40% relative gap; 56% of questions: all 1000 samples wrong; 9%: probe ranks never-sampled gold first. Probe 23.7 vs majority vote 22.0 vs greedy 21.2; oracle 44.3 | Gekhman 2025 [c09, d17] | established (K12) |
| Probes detect errors, do not transfer | AUC TriviaQA probe 0.85/0.83 vs logit 0.75/0.79; consistently-incorrect error-type AUC 0.59 to 0.67; no transfer after logit baseline | Orgad 2025 [c10, d18] | established |
| Reversal curse | Fine-tune 96.7% description-to-name, about 0% reversed. GPT-4 parent 79% vs child 33% | Berglund 2023 [c11, c12] | established (K13) |
| Extraction needs varied paraphrase | No augmentation: held-out QA near 0%. Mixed training 86.6% (bioS), 77.7% (bioR) | Allen-Zhu and Li 2023 [c14, c15] | established (K13) |
| Position as cue | GPT-3.5 drops over 20 points; at 20 and 30 documents below 56.1% closed-book | Liu 2024 [c16, c17] | single-source (K14) |
| Proactive interference in context | 35 variants; log-linear fall; forget instruction under 10 points gain at 100 updates; mock QA reset helps most; size predicts endurance t=3.03 p=0.005 N=30; context length p=0.886 | Wang and Sun 2025 [b20, c18, c19, d16] | single-source (K15, K25) |
| Deleted info stays in hidden states | White-box 38% (budget 20); black-box paraphrase 29%; defence 38% to 2.4% | Patil 2023 [b21] | single-source (K16) |
| Write-time cue enrichment | LongMemEval round recall@5 0.582 to 0.644; session 0.706 to 0.732; +9.4% recall, +5.4% QA | Wu 2025 [d12] | single-source (K23) |
| Read-side query expansion | Temporal subset round recall@5 0.421 (K=V), 0.489 (+fact), 0.526 (+GPT-4o expansion), 0.481 (Llama 8B). Session: Llama 8B 0.624 vs 0.639 | Wu 2025 [d13] | single-source |
| Single query rewrite | HotpotQA EM 30.47 to 32.80 (LLM), 34.38 (trained); AmbigNQ 45.80 to 46.40; PopQA 43.20 to 46.00 | Ma 2023 [d14] | single-source (K24) |
| Memory design on LoCoMo | Mem0 J 66.88 at 1764 tokens; Mem0g 68.44; best RAG 60.97; Zep 65.99; A-Mem 48.38; full context 72.90 at 26031 tokens | Chhikara 2025 [d15] | single-source |
| Self-search paging | Deep retrieval GPT-4 32.1% to 92.5%; GPT-3.5 38.7 to 66.9; GPT-4 Turbo 35.3 to 93.4 | MemGPT [c22] | established (K17) |
| Feeling-of-knowing analogue | P(IK) AUROC 0.864 TriviaQA (52B); trained TriviaQA only: 0.606 (LAMBADA), 0.687 (Python), 0.624 (GSM8K) | Kadavath 2022 [d19] | established (K26) |

## 4. Mechanisms and models

**4.1 Three-part trace model (what an engineer can build).** Treat memory as: trace T (stored content), cue set C (what the query contains), and a competition rule (which stored items match C best). Retrieval returns the item with the best match given C, discounted by competitors. Failure types:

1. Not stored (no trace). No cue helps. Control: a never-seen item.
2. Stored, cue mismatch. A different cue helps. Encoding specificity [a27].
3. Stored, cue overloaded. Many items match the same cue. Need a cue with diagnostic value [a07].
4. Stored, but a newer competing trace wins. Proactive or retroactive interference. Time and original context shift the balance toward the old trace [a03, a04].
5. Stored, but the state at test differs from the state bound at encoding. Re-instate the state [a14].

Implementation: log, per item, the encoding context (task framing, time, source, state line) as metadata. At retrieval, issue the query once in the plain form and once with the encoding context fields added. Rank by match to both.

**4.2 Interference with time (Sissons and Miller pattern).** Score for item i at test = strength_i x context_match_i minus the sum over competitors. Recent items have high context match to the present context. Old items win after long gaps because the recent item's context fades more. So recency is not a stable preference. For an agent: do not hard-code "latest wins" without checking whether the latest note was written in a context unlike the query [a03, K20]. Single-source, rat data.

**4.3 Memory integration / state matching.** The state (drug) is part of the trace. The test needs the same state. LLM analogue: the framing text in the prompt at write time is part of the stored item's key. At read time, restore the framing. Not tested in LLMs [K19].

**4.4 Prediction-error gate.** Update size proportional to (outcome minus expectation). Use as a rule for memory edits: rewrite a note only when new evidence contradicts the note's prediction; do not rewrite on agreement. Design analogy only [a13].

**4.5 Engram rescue logic.** Two cue routes to one trace: the natural route (broken) and a direct artificial route (works). Test: if the direct route works and the natural does not, the trace exists. Agent analogue: query the memory store by direct id or exact string when the semantic query fails. If the exact lookup finds it, the fault is in the retrieval query, not the store [K02 analogue].

**4.6 Spurious forgetting probe (Zheng).** To tell lost knowledge from lost alignment: train briefly on half the old-task data and test the other half. Near 100% means the knowledge is intact; near 0 means lost [c25]. Needs training access. Prompt-only equivalent: put a few old-task examples in context and measure recovery. Untested at equal tokens [K10].

**4.7 Internal-score reranking.** Sample N candidates. Score each with a hidden-state probe or an internal confidence. Pick the top score instead of the majority [d17]. Gain: 23.7 vs 22.0 (majority) at N=1000. Needs weights access. API substitute: cross-paraphrase agreement (untested) [K26].

**4.8 Cue-rewrite pipelines.** Write time: key = value + extracted facts [d12]. Read time: query expansion with a strong rewriter [d13]. Paging and self-search: the model issues several searches in a loop [c22]. Reflection notes as later cues [c23]. Linked tagged notes [c24]. Scored retrieval: recency (exponential decay) + importance (1 to 10, model-rated) + relevance (embedding cosine), min-max normalised, weights all 1 [c21].

## 5. What holds up

**Holds up well.**
- Mouse engram rescue after anisomycin, in the original lab and in related labs (Roy 2016, 2017; Guskjolen 2018; Sarma 2026). It needs strong enough stimulation (25% laser power failed) and the right protocol (CA1 4 Hz) [b03, b23]. Group sizes are small (3 to 15).
- Human encoding specificity and cued recall of items missed in free recall (see the earlier encoding-specificity document).
- In LLMs: suppressed or fine-tuned-away ability returns cheaply (Zheng, Lucki, Deeb and Roger, Hu, Lynch). Five separate lines agree [K10, K11].

**Failed or contested.**
- Walker 2003 reminder amnesia: 4 direct and 3 conceptual replications failed (N=64 and N=48; pooled BF01 5.74). In the conceptual set, retrieval helped keep sequence knowledge [a20, critique item 1].
- Propranolol blockade: Pigeon 2022 robust; Steenen 2022 no significant benefit once low-bias RCTs are used; a healthy N=44 replication failed; Schiller 2010 results depend on exclusions [b07 to b10, a23].
- The review itself lists about 8 failed human or animal replications (Luyten 2021, Schroyens 2017 and 2019, Stemerding 2022, Chalkia 2020, Hardwicke 2016) [d03].
- Abdou 2018: no rescue after complete amnesia by light on auditory inputs [d05].
- Post-retrieval extinction: animal fear g=0.21 not significant [a21].
- Weakness of reconsolidation does not prove retrieval failure. Both could be wrong or partly right (critique).

**Moderators.**
- Time since the amnesic event (spontaneous recovery) [a10].
- Test context: original vs new [a19, a04].
- State: same drug state at test [a18].
- Stimulation strength, cell population (DG vs CA1) [b03, b23].
- Trace strength, memory age, prediction error (admitted by the authors as piled-up boundary conditions) [a12].
- Amnesia route: complete amnesia is not rescued (Abdou) [d05].
- LLM: method of unlearning, depth, format (chat template), origin of the fact (pretraining vs fine-tuned-in) [b13, b15, b18].
- Cue form: direction (reversal), paraphrase variety, position in context [c11, c14, c16].
- Model strength for read-side rewriting (Llama 8B can hurt) [d13].

**Interventions that worked.**
- Restoring encoding framing/state in rats (reminder, re-dosing) [a18].
- LLM: ten safety instances, ten unrelated retain samples, an optimised prefix, summaries or first lines in context, a mock QA reset, write-time fact keys, paging with self-search [c03, b17, d10, d11, d16, d12, c22].

**Interventions that did not work.**
- Telling a model to forget or ignore old values: under 10 points (and worse on gpt-4.1-mini at times) [d16].
- Replay of 20% old data in spurious forgetting [c04].
- Longer context windows against lost-in-the-middle [c17].
- Cross-dataset probe transfer once a logit baseline is subtracted [d18].
- Deep unlearning resists relearning (1 pair 0% at all depths) [b16].
- Weak, loosely related relearning data (gibberish 9%) [b15].

**Evidence quality.** The core paper is an advocate review with selected positives. There is no count of failed reversals, and none can be built from it [d01]. Human evidence is thin. Rodent group sizes are small. Replications are mostly by related labs.

## 6. Language models

No paper tests the human claim directly. What exists are parallels [c26, K19].

**Fine-tuning forgetting is often loss of alignment.** Zheng et al. (ICLR 2025): accuracy on old tasks fell from about 100% to about 10% in 150 steps. Training on half of the old data brought the other half back to 96% to 100%. Safety fell 100% to 0% and returned to about 99% after 10 safety instances; irrelevant tasks also restored old behaviour (only the ten-instance case was checked in detail). Replay of 20% old data barely helped. Freezing bottom layers raised accuracy from 11% to 44% (others peaked at 22%) [c02 to c04]. Caveat: the probe retrains, so it shows savings, not cue-only access (critique 5). Kotha et al. (2024): fine-tuning makes the model infer the wrong task. Conjugate prompting (making the prompt unlike the fine-tuning data, e.g. translation) brings back suppressed capability. In-context learning dropped 56.75% (Alpaca vs LLaMa-7b), 40.00% (Vicuna-7b), 21.00% (OPT-IML-1.3b). English code fine-tuning cost 8.36% on English XNLI but under 2% in French, Spanish and German [b12]. This is the closest prompt-only analogue of context change.

**Unlearning hides, does not erase.** WMDP-Bio: base 64.4%, unlearned about 30%. Ten unrelated samples bring it to 52.7 to 61.6% (Lucki). At least 88% recovery for pretraining-era facts with disjoint retraining (Deeb and Roger; 157 items per split, 4 splits for retraining). More than 70% keyword success with benign text (Hu). Harry Potter familiarity comes back with 1% to 10% of the corpus (Lynch). Prompt-only: adversarial prefix lifts 29.9 to 53.9 (RMU); Harry Potter in-context relearning gives modest gains [d10, d11]. Boundaries: RMU does remove some residual-stream information (logit lens could not decode answers) [c05]; fine-tuned-in facts recover less (under 35% for GD and RIA) [b13]; deep unlearning resists [b15, b16]; chat template changes the result by up to 20 points [b18]. Patil et al.: GPT-J edited to delete an answer still leaks it in hidden states, 38% white-box, 29% black-box paraphrase [b21].

**Hidden knowledge not output.** Gekhman et al.: 40% relative gap between internal scoring and output probability; 56% of questions had all 1000 samples wrong; in 9% the probe ranked the never-sampled gold answer first. Probe 23.7 vs majority 22.0 vs greedy 21.2 vs oracle 44.3 [c09, d17]. Orgad et al.: truthfulness signals sit in the exact-answer tokens, do not transfer across datasets [c10, d18]. Kadavath et al.: P(IK) AUROC 0.864 in distribution and 0.606 to 0.687 out of it [d19].

**Cue direction and form.** Reversal curse: GPT-4 79% (parent) vs 33% (child); fine-tuned 96.7% vs about 0%. With the fact in context the curse disappears [c11 to c13]. Allen-Zhu and Li: without paraphrase variety in training, held-out QA near 0% even with perfect memorisation, at 7000x scale as well; with variety 86.6% / 77.7% [c14, c15].

**Position and interference.** Lost in the middle: over 20-point drop; below closed-book at 20 and 30 documents; longer-context variants no fix (2023 models) [c16, c17]. Proactive interference: log-linear decline over 35 variants; model size predicts endurance, context length does not; forget instructions give under 10 points; mock QA reset best [d16].

**Agent memory as cue design.** Generative Agents: scored retrieval; TrueSkill 25.64 (no reflection or planning) vs 21.21 (no memory, planning, reflection); believability, not accuracy [c20, c21]. MemGPT deep retrieval GPT-4 32.1 to 92.5 [c22]. Reflexion: 130 of 134 ALFWorld tasks; HumanEval 91 vs 80 [c23]. A-MEM: margins not extracted [c24]. Mem0: 66.88 J at 1764 tokens vs RAG 60.97 vs full context 72.90 at 26031 tokens [d15]. LongMemEval: fact keys +5.4% QA; query expansion helps only with a strong rewriter [d12, d13]. Ma 2023: single rewrite 0 to 3 points [d14]. These tasks and baselines differ, so margins are not comparable (K17).

**What is missing.** A natural test: store a fact under one framing, probe under another, restore the framing, measure recovery without weight updates. Multi-paraphrase vs single query at equal tokens: not found. Overwrite vs append at equal tokens: not found [critique gaps 3, 4, 8].

## 7. What our agent should take

Status marks as in SCHEMA.md: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **"No answer" is not "not known" in a memory-using step.** Before the agent writes "not in memory" or "unknown", the program must have tried at least one alternative cue: reversed direction, a paraphrase, or a direct exact-string lookup. Schema part: memory + O (query rewrite). [E] K13, K21 (c11 to c15, d10, d11). Cost control: only when a memory store exists and the first query returned nothing useful. This is doubt on a signal (an empty or low-score result), so it fits G1.
2. **Do not claim a hit rate for cue rescue.** No source gives one. Use the rule as a cheap retry, not as a promise. Schema part: G7 (must pay for itself). [E] K22 (d01, d02).
3. **Reversal and paraphrase are separate cues.** Store key facts in both directions or with varied phrasings; query in both directions. Schema part: memory + O. [E] K13 (c11, c12, c14).
4. **Suppressed is not erased.** Any scaffold step that "forgets" or hides content (for safety or to prevent anchoring) must not be assumed to remove it from the model. Do input hygiene in code (S1 moves suggestive material into a marked block), not model-side forgetting. Schema part: S1. [E] K11, K16 (b13 to b17, b21).
5. **Do not build a reactivate-then-overwrite edit step expecting clean edits.** Schema part: memory design. [E] K05 (a20, d03, d07).
6. **Do not rely on "ignore old information" instructions.** The finding that they help under 10 points is solid for the models tested (d16, c18); stale values should be handled in code. Schema part: G5 (code selects) + memory. Status [S] K15, K25; the "deletion beats append" half is untested and goes to Test first.
7. **Position is a cue.** Put key evidence at the start or end of the prompt, not the middle. Schema part: S0/S1 input layout. [S] K14 (older 2023 models); the layout rule is free, so keep it.
8. **Keep source tags on notes (which context wrote this).** A reminder can mix new content into old recall (Hupbach: intrusions, U=20, p<0.01). Schema part: memory. [C] K27, but the tag is free.

### Test first

1. Multi-cue retrieval (3 paraphrases + reverse) vs one query, equal tokens [S, gap 3]. Part: O/memory. Evidence: d12 to d14, K24.
2. Write-time fact key per note [S] K23 (d12). Part: memory.
3. Overwrite stale notes vs append with a "latest wins" rule [S] K15, K25 (b20, d16). Part: memory.
4. Context reinstatement: restore encoding framing at read time [S/C] K04, K19, K20 (a14, a18, a19). Part: memory/S1.
5. Reminder cue (short topic summary in context) vs no cue on a buried or dropped skill [S] K21, K10 (d11, c03). Part: S3 prompt.
6. Re-score candidates by cross-paraphrase agreement instead of plain majority [S] K12, K26 (d17, d18, d19). Part: S7 (code selects, G5). Note G4: samples from one model are not independent, so paraphrase agreement may be correlated.
7. Recency vs primacy after long gaps in agent memory [S] K20 (a03). Part: memory.
8. Stored-but-inaccessible detector (cheap feeling-of-knowing) [S] K26 (d19). Part: S6/S8.
9. Memory-retrieval signal ablation (recency/relevance/importance) on one task [K17 is established as a design, weights untested] (c20, c21). Part: memory.

## 8. Concrete tests on our bench

All tests: both arms spend the same total tokens (count retrieval calls, rewrites and the answer). The control is the plain model with the plain memory prompt. Report setup cost (G7).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Fact-recall items from a stored note set (50 to 100 notes; query in reverse direction or paraphrased) | A: one query. B: reverse + 2 paraphrases, budget matched by shrinking top-k or note text | Exact-match hit rate; recall@k | +3 to +10 points on reversed or paraphrased queries; about 0 on same-form queries |
| T2 | Same item set, notes written with and without a one-line fact key | A: key = note. B: key = note + fact line | recall@5 and answer accuracy | About +3 to +6 points (LongMemEval: +5.4% QA) |
| T3 | Key-value update stream (3 to 150 updates per key), query latest value | A: append all, "latest wins" instruction. B: delete stale in code, keep latest. C: mock QA reset | Accuracy vs updates | B and C beat A at 100+ updates by over 10 points |
| T4 | Facts written under a framing (role, task label, date line), probed under another | A: probe without framing. B: probe with encoding framing restored. C: probe with a neutral reminder of the same length | Correct recall | B > A by 5+ points if state matching works; B = C means length, not match |
| T5 | Buried-skill items: a behaviour the model shows at baseline but not after a long distractor or style prompt | A: no cue. B: 2 to 3 worked examples in context. C: different cue (translated or restyled prompt) | Task accuracy | B and C recover part (target half the gap); compare with Kotha conjugate prompting |
| T6 | Closed-book QA, sampled candidates | A: majority vote over N samples. B: pick by cross-paraphrase agreement (3 paraphrases x N/3) | Accuracy | +1 to +2 points at best (probe gain was 1.7 with weights); may be 0 |
| T7 | Notes written in order A, B vs B, A with simulated time gaps (stale logs added) | A: recency ranking. B: context match plus recency | Correct note choice | B better when query context matches the older note |
| T8 | Mix of stored and never-stored facts | Retry-with-alternative-cue loop vs single query | False-find rate on never-stored items | Near 0 false finds; if above 5%, the retry harms |
| T9 | Key evidence at start, middle, end in a 10 to 20 document prompt (current models) | Position arms, same tokens | Accuracy by position | Smaller U-shape than 2023 models; measure |
| T10 | Memory ablation on one agent task | Full scoring vs drop recency / importance / relevance | Task success | Relevance matters most; the rest unknown |

At least 100 items per cell to see a 5-point effect. Use paired items.

## 9. What does not transfer, and why

- **Optogenetic rescue.** The agent has no engram cells. A direct exact-string lookup is only an analogue. The rodent work shows the trace is present; it says nothing about how to cue a model.
- **Drug state and protein synthesis.** No LLM analogue. State matching must be rebuilt as prompt framing, and that is untested.
- **Human reconsolidation erasure.** Weak or contested, and our agent has no reconsolidation window. Do not build it [K05, K06].
- **Weight-update recovery.** Most LLM recovery results (Zheng, Lucki, Deeb and Roger, Hu, Lynch) use fine-tuning. Our scaffold changes prompts, not weights. Only the prefix attack and in-context relearning are prompt-only, and the prefix is an optimised adversarial string, not a natural cue [d10, d11].
- **Probes on hidden states.** Need white-box access. API-only agents cannot use them [d17, d18, d19].
- **Time gradient and spontaneous recovery.** A prompt has no time decay. "Time passing" means nothing unless the memory store has decay rules.
- **Rat contextual fear.** Room context is not task framing. Rough analogy only.
- **Unlearning attacks.** Their goal is extraction. Ours is honest recall. The numbers show suppression, not a method we want.
- **Believability scores (Generative Agents).** Not an accuracy measure [c20].
- **2023 model results** (lost in the middle, GPT-4 reversal curse) may be weaker on current models. Re-measure.
- **Adaptive forgetting idea.** The agent usually wants fewer stale items. Keeping everything and suppressing in retrieval costs tokens at the context limit.

## 10. Open questions

1. How many reversal attempts failed vs succeeded in the Psychological Review paper? The preprint has no tally [d01]. Full published text not obtained [b25].
2. Does context reinstatement (restoring encoding framing) help LLM recall without weight updates?
3. At equal tokens, does multi-paraphrase or reverse re-querying beat one query?
4. Does overwriting stale notes beat append-only? (Wang and Sun test instructions, never deletion.)
5. Do internal-score methods beat majority vote at equal tokens, and do they transfer across datasets?
6. Which human cue-induced amnesia results besides Walker work, and with what effect size? Kindt 2009 effect size not obtained.
7. What is the Steenen restricted pooled propranolol effect with CI? Forest plots only.
8. Does state or context matching improve LoCoMo or LongMemEval scores?
9. How many independent labs replicated Ryan 2015? The 16 citations in the optogenetic column are mostly related labs; Abdou 2018 failed in a different design.
10. Can an API-only agent detect a stored-but-inaccessible item cheaply?
11. Does the "narrow parameters" defence make the retrieval view unfalsifiable, as critics say of reconsolidation?
12. Does the lost-in-the-middle U shape persist on current long-context models?

## 11. Sources

[V] opened (page, PDF or abstract page read; "abstract" marks abstract only). [M] snippet only or described second-hand.

1. [V] Alfei, Miller, Ryan, Urcelay (2025) Rethinking memory impairments: Retrieval failure. Psychol Rev 133(2):411-449. Preprint https://osf.io/download/zjxvu/ ; record https://researchconnect.suny.edu/en/publications/rethinking-memory-impairments-retrieval-failure/ ; doi 10.1037/rev0000538 (published full text [M], not obtained).
2. [V] Ryan, Roy, Pignatelli, Arons, Tonegawa (2015) Engram cells retain memory under retrograde amnesia. Science. https://pmc.ncbi.nlm.nih.gov/articles/PMC5583719/
3. [V] Roy et al. (2016) Memory retrieval by activating engram cells in mouse models of early Alzheimer's disease. https://pmc.ncbi.nlm.nih.gov/articles/PMC4847731/
4. [V] Roy et al. (2017) Silent memory engrams as the basis for retrograde amnesia. PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC5699085/
5. [V] Sarma et al. (2026) Restoring access to long-term social recognition memories disrupted by sleep deprivation. https://pmc.ncbi.nlm.nih.gov/articles/PMC13251821/
6. [V, abstract] Abdou et al. (2018) Synapse-specific representation of the identity of overlapping memory engrams. Science. https://doi.org/10.1126/science.aat3810
7. [V, abstract] Guskjolen et al. (2018) Recovery of lost infant memories in mice. Curr Biol. https://europepmc.org/search?query=Recovery%20of%20lost%20infant%20memories
8. [V] Gisquet-Verrier et al. (2015) Integration of new information with active memory accounts for retrograde amnesia. https://pmc.ncbi.nlm.nih.gov/articles/PMC6605236/
9. [V] Gisquet-Verrier and Riccio (2018) Memory integration as a challenge to the consolidation/reconsolidation hypothesis. https://pmc.ncbi.nlm.nih.gov/articles/PMC6337075/
10. [V] Alfei, De Gruy, De Bundel, Luyten, Beckers (2020) Generalization and recovery of post-retrieval amnesia. https://pmc.ncbi.nlm.nih.gov/articles/PMC7116269/
11. [V] Hardwicke, Taqi, Shanks (2016) Postretrieval new learning does not reliably induce human memory updating via reconsolidation. PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC4868433/
12. [V] Hupbach, Gomez, Hardt, Nadel (2007) Reconsolidation of episodic memories. https://pmc.ncbi.nlm.nih.gov/articles/PMC1838545/
13. [V, abstract] Kindt, Soeter, Vervliet (2009) Beyond extinction. https://pubmed.ncbi.nlm.nih.gov/19219038/
14. [V, abstract] Kredlow, Unger, Otto (2016) Harnessing reconsolidation to weaken fear and appetitive memories. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMC4760909&format=json&resultType=core
15. [V, abstract] Appraising reconsolidation theory and its empirical validation (2023) Psychon Bull Rev. https://pmc.ncbi.nlm.nih.gov/articles/PMC7614440/
16. [V, abstract] Verification report of Schiller et al. (2010), Cortex 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7115860/
17. [V, abstract] Nader, Schafe, LeDoux (2000) Nature. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/35021052&format=json&resultType=core
18. [V, abstract] Warrington and Weiskrantz (1970) Nature 228. https://www.nature.com/articles/228628a0
19. [M] Tulving and Pearlstone (1966). https://www.sciencedirect.com/science/article/pii/S0022537166800483
20. [M] Tulving and Thomson (1973). https://doi.org/10.1037/h0020071
21. [M] Miller and Springer (1973) Psychol Rev 80. https://doi.org/10.1037/h0033897 ; (1974) https://researchconnect.suny.edu/en/publications/implications-of-recovery-from-experimental-amnesia/
22. [M] Stout and Miller (2007) SOCR, via the Alfei review.
23. [V] Pigeon et al. (2022) propranolol meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC8979654/
24. [V] Steenen et al. (2022) rectified meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC9640173/
25. [V] Noradrenergic blockade of memory reconsolidation: a failure to reduce conditioned fear responses (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4246921/
26. [V] FCSRT in behavioural variant frontotemporal dementia meta-analysis (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11473568/
27. [V] Zheng et al. (2025, ICLR) Spurious forgetting in continual learning of language models. https://arxiv.org/pdf/2501.13453
28. [V] Kotha, Springer, Raghunathan (2024) Understanding catastrophic forgetting in language models via implicit inference. https://arxiv.org/abs/2309.10105
29. [V] Lucki et al. (2025) An adversarial perspective on machine unlearning for AI safety. https://arxiv.org/abs/2409.18025
30. [V] Deeb and Roger (2025) Do unlearning methods remove information from language model weights? https://arxiv.org/abs/2410.08827
31. [V] Hu, Fu, Wu, Smith (2025) Unlearning or obfuscating? https://arxiv.org/abs/2406.13356
32. [V] Lynch et al. (2024) Eight methods to evaluate robust unlearning in LLMs. https://arxiv.org/abs/2402.16835
33. [V] Patil, Hase, Bansal (2023) Can sensitive information be deleted from LLMs? https://arxiv.org/abs/2309.17410
34. [V] Gekhman et al. (2025) Inside-out: hidden factual knowledge in LLMs. https://arxiv.org/abs/2503.15299
35. [V] Orgad et al. (2025) LLMs know more than they show. https://arxiv.org/abs/2410.02707
36. [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221
37. [V] Berglund et al. (2023) The Reversal Curse. https://arxiv.org/pdf/2309.12288
38. [V] Allen-Zhu and Li (2023) Physics of language models 3.1. https://arxiv.org/pdf/2309.14316
39. [V] Liu et al. (2024) Lost in the middle. https://arxiv.org/pdf/2307.03172
40. [V] Wang and Sun (2025) Unable to forget: proactive interference. https://arxiv.org/abs/2506.08184
41. [V] Park et al. (2023) Generative Agents. https://arxiv.org/pdf/2304.03442
42. [V] Packer et al. (2023) MemGPT. https://arxiv.org/pdf/2310.08560
43. [V] Shinn et al. (2023) Reflexion. https://arxiv.org/pdf/2303.11366
44. [V] Xu et al. (2025) A-MEM. https://arxiv.org/pdf/2502.12110
45. [V, via fetch summary] Wu et al. (2025) LongMemEval. https://arxiv.org/abs/2410.10813
46. [V] Ma et al. (2023) Query rewriting for retrieval-augmented LLMs. https://arxiv.org/abs/2305.14283
47. [V] Chhikara et al. (2025) Mem0. https://arxiv.org/abs/2504.19413

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 10 established claims: 8 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A06.08-K02** (reworded: the sources support less). Sarma et al. 2026 rescued social recognition memory after sleep deprivation, not freezing; the wording 'restores freezing ... and after sleep loss' wrongly extends the freezing result to a different behavior. Corrected claim: In mice, light on tagged dentate gyrus engram cells restores freezing after anisomycin amnesia (Ryan 2015, Roy 2017) and restores social recognition memory after sleep deprivation (Sarma 2026); natural cues fail. Rodent only, specific cell populations and stimulation protocols. Dissent: Abdou 2018 found light on auditory inputs to the lateral amygdala failed to induce recall after complete amnesia. Replications are by related labs; strict count unknown.
- **A06.08-K26** (reworded: the sources support less). Kadavath et al. Table 1 shows trained-on-TriviaQA P(IK) AUROC out of distribution of 0.606 (LAMBADA), 0.687 (Python), 0.624 (GSM8K) but 0.928 on Mixed-Arithmetic, so the stated 0.606-0.687 range omits the strongest transfer case. Corrected claim: A feeling-of-knowing analogue exists for LLMs but needs training or hidden states: P(IK) AUROC 0.864 on TriviaQA (52B), and when trained on TriviaQA only 0.606 to 0.687 on LAMBADA, Python and GSM8K (0.928 on Mixed-Arithmetic); probes on exact-answer tokens give AUC 0.83 to 0.95 but do not transfer across datasets once a logit baseline is subtracted.
- **A06.08-K22** (now single-source: only one opened source, code check).
