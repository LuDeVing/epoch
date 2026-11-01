# Interference: deep document

*Subfield A06.03. Sources: evidence_a-d.jsonl (a01-a33, b01-b28, c01-c29, d01-d19), claims.jsonl (K01-K30), critique.md. Status marks: [E] established, [S] single-source, [C] contested. Search was incomplete at the end (web quota ran out), so the sweep for 2026 LLM papers may have gaps.*

## 1. What it is

Interference is forgetting caused by other, similar memories, not by time.

- **Proactive interference (PI):** old material blocks new material. You learned list A, and now list B is harder to recall.
- **Retroactive interference (RI):** new material blocks old material. You learned list B, and now list A is harder to recall.
- **Strength depends on similarity.** Related items interfere most. Unrelated items barely do.
- **Release from PI.** PI builds across successive trials of the same category. When the category changes, recall jumps back (Wickens release).

Three reasons it matters for us.

1. The agent's memory is a store of similar entries (lessons, past attempts, notes). Similar entries may compete at retrieval.
2. The human literature says damage grows with the number of prior similar items and falls when the category changes. That suggests two levers: cap similar entries per class, and vary the class shown.
3. LLMs have a direct analogue. When a context holds many old values for the same key, the model often returns an old one. This has been measured on dozens of models (K01).

Key claim in one line: relation matters more than count. Related, conflicting or near-duplicate entries do the harm (K09, K13). Unrelated entries do almost none.

## 2. History and theories in depth

**Muller and Pilzecker (1900).** A second list learned soon after the first impaired it. This did not happen when the second list came later (list A: six syllable pairs; list X after 17 s or 6 min; cued recall 1.5 h later; impaired only in the 17 s case) (a22). They explained it by consolidation: traces need time to settle. This is the root of the "interference vs consolidation" argument that is still open. Source is second-hand (Wixted 2004); the monograph has no English translation.

**Skaggs (1925).** RI appeared even after dissimilar interpolated work (algebra, chess positions, words, syllables), and was larger with more similarity (a22). Not all subjects showed it.

**Jenkins and Dallenbach (1924).** More recall after sleep than after waking. Read as less RI during sleep. Ekstrand (1967) tested this with A-B then A-C lists, learned at night with 8 h sleep or in the morning with 8 h awake: both lists were better after sleep (a21). Wixted reads sleep as consolidation, a competing account.

**McGeoch (1932).** Three factors: response competition, change of situation between learning and test, and wrong set (a25). The classic statement.

**Melton and Irwin (1940).** Added unlearning: learning a competing response weakens the first one directly (a25).

**Underwood (1957), "Interference and forgetting."** He asked why one-day forgetting of a list learned to one perfect recall differed so much between studies. The number of earlier lists learned in the lab explained nearly all the spread: roughly 20% to nearly 80% forgetting (a18, second-hand via Wixted). A search summary of the abstract quotes forgetting falling from about 75% to about 25% over 24 h when this interference is removed (a19, not opened). He concluded PI is the main cause of laboratory forgetting. Wixted notes he included only studies with massed prior learning.

**Greenberg and Underwood (1950).** Same people, lists learned in sequence (ten paired adjectives, criterion 8 correct). Recall after two days was about 70% for the first list, about 40% for the next, about 25% for the third (a29, b22: Wikipedia summary, not opened).

**Underwood and Ekstrand (1966, 1967).** PI appeared with massed prior trials but not when prior learning was spread over four days (a20). Underwood and Postman (1960) found the same one-week forgetting for 3-letter words and 3-letter trigrams, against the unlearning prediction (a20).

**Barnes and Underwood (1959), MMFR.** Modified modified free recall: the subject recalls both A-B and A-C responses. A-C outnumbered A-B after delay, read as unlearning. Briggs (1954): B responses recovered spontaneously after 24 h and exceeded C (12 paired associates, 100% criterion) (a30). Later work found spontaneous recovery unreliable: Koppenaal (1963) no recovery on MMFR; Postman, Stark and Fraser (1968) recovery only in special conditions. Postman and Underwood (1973) replaced unlearning with response-set suppression (a25).

**Peterson and Peterson (1959) / Brown (1958).** One consonant trigram, counting backward by 3 or 4, then recall after 3 to 18 s. Recall fell fast. Exp I: 24 students, 48 trigrams, 8 trials per interval; Exp II: 48 students (a15). The authors fitted a stimulus-fluctuation (Estes) model. They tested for PI by splitting trials into four blocks and found none: 3 and 6 s combined went .57, .66, .70, .74 (an improvement, p=.02); 15 and 18 s stayed .08 to .15 (a16). Their own data did not show PI. Items were chosen to be dissimilar.

**Keppel and Underwood (1962).** On Trial 1 there is little or no forgetting over 3 to 18 s. Forgetting builds over the first few trials. Read as PI, not decay. Second-hand numbers: asymptote .99 on Trial 1, .58 on Trial 3 (d15, via Loftus and Patterson; a27 and b24 are snippets). Turvey, Mosher and Katz (1971): five successive 18-s tests, N=90, country-name triads; later recognition of non-recalled items was .58 to .76 (mean .68) vs .92 to .98 for recalled, false-positive rate .09. So non-recalled items were still stored: retrieval and discrimination failure (a17).

**Wickens, Born and Allen (1963); Wickens (1970).** Repeated same-category trials lower recall trial by trial. A new category on trial 4 restores recall. Content shift released 91% in the first study; a time shift released 74% (Kincaid and Wickens 1970) (d16, via a thesis). Release grows with category distance (fruits to professions more than fruits to vegetables, Wickens, Dalezman and Eggemeier 1976). Primary tables not opened.

**Mensink and Raaijmakers (1988).** SAM plus a context-fluctuation process. One parameter set reproduces RI and PI, spontaneous recovery, independence of list 1 and list 2 recall, Osgood's transfer surface, forgetting curves and the accuracy-latency link (a24, a26). The formal "competition at retrieval" account (section 4).

**Anderson and Neely (1996); Anderson (2003).** Forgetting is not only passive blocking. Control processes can suppress competitors during retrieval (retrieval-induced forgetting). Not opened (a33, b27). Kliegl and Baeuml (2021) contrast this with the blocking account (a31).

**Working-memory PI (Monsell 1978; Jonides and Nee 2006).** Recent-probes task: a probe from the previous trial's set but not the current one (a "recent negative") is rejected slower and less accurately. About 75 ms and 7% accuracy cost (Monsell). Left inferior frontal gyrus (BA45) resolves it. Patient M.L. (left frontal lesion): effect 5.9 SD above controls, almost 400 ms outside the control range, accuracy effect 25%. Older adults show a larger effect. Directed-forgetting probes cost 136 ms and 2.6% accuracy (Zhang et al. 2003) (b17, b18).

**Where theory stands.** Competition at retrieval (a search set contaminated by similar items) is the main account. Pure unlearning has weak support. Consolidation (Muller and Pilzecker; Wixted) and active inhibition (Anderson) are live rivals. The practical result is stable under all of them: similar items compete, and old items stay reachable by cues (K19, [C] on mechanism).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Forgetting depends on number of prior lists | one-day forgetting about 20% to nearly 80% across studies | Underwood 1957 via Wixted (a18); K17 | [E], second-hand |
| Stage of practice | recall after 2 days about 70%, 40%, 25% for lists 1, 2, 3 | Greenberg and Underwood 1950 via Wikipedia (a29) | [S] unverified |
| PI absent in Peterson and Peterson's own data | 3 and 6 s accuracy rose .57 to .74 over 4 blocks, p=.02 | a16 | [E] (primary opened) |
| PI explains short-term forgetting | Trial 1 asymptote .99; Trial 3 .58 | Keppel and Underwood 1962 via Loftus and Patterson (d15) | [E] by many reviews; numbers second-hand |
| Non-recalled items still stored | recognition .58 to .76 (mean .68) vs .92 to .98 recalled; N=90 | Turvey et al. 1971 (a17) | [S] |
| Release from PI by category change | 91% (content shift), 74% (time shift); grows with category distance | Wickens et al. 1963; Kincaid and Wickens 1970 via thesis (d16) | [E] qualitatively; numbers second-hand |
| Release in a modern replication | forget vs remember +11.27%, t(23)=3.491, d=1.069; no-PI vs remember +14.58%, t(23)=4.263, d=1.342; no-PI vs forget n.s. (p=.173) | Baeuml and Kliegl 2013 Exp 1A, N=24 (a32) | [E] |
| Release not always found | no release after a category switch in two experiments | Hubbard et al. 2018 (b21, snippet) | [C] |
| Spacing removes PI | PI with massed prior learning, none when spread over 4 days | Underwood and Ekstrand 1966-67 (a20) | [C] primary not opened |
| RI time gradient is weak | Archer and Underwood quadratic F(1,74)=2.83, p<.10; Newton and Wickens F(1,54)=5.91, p<.05 | a23 | [C] |
| Familiarity modulates PI | repeating non-words .19, repeating words .12, unique words .13, unique non-words .06; unique vs repeating non-words d=1.12; N=192 | Mercer 2025 (b19) | [S] |
| Working-memory PI cost | recent negatives about 75 ms, 7% accuracy | Monsell 1978 via Jonides and Nee (b17) | [E] |
| LLM: latest value falls log-linearly with old values | 46 keys, 3 to 400 updates; mid-size tier about 0% at 400; 30+ models | Wang and Sun 2025 (a01, c01) | [E] (2 sources, one paradigm family) |
| LLM: interference, not length | fixed input length, more tracked keys: llama4-maverick near 100% at 2 tracked keys, below 5% at 46 | a02 | [S] |
| LLM: value length is the strongest driver | 10-word values: under 40% for all models; 40 words: under 5% | a02, c04 | [S] |
| LLM: size predicts endurance, window does not | N=30: size t=3.03, p=0.005; context t=-0.144, p=0.886; R2=0.261 | Wang and Sun (a03) | [C] |
| LLM: size vs PI disputed | RI R2=0.491; PI R2=0.06, p=0.14; N=39 | Chattaraj and Raj (b06) | [C] |
| LLM: PI harder than RI | 39 of 39 models; gap 69.5 points; t(38)=10.71, d=1.73 | Chattaraj and Raj (a04, c07) | [S] same lab only |
| LLM: RI curve | 93.9, 96.0, 72.9, 45.5, 24.6% at N=3, 50, 100, 200, 300 | a04 | [S] |
| LLM: frontier models (RIES / PIES) | GPT-5 186.4 / 99.2; o3 185.8 / 76.0; Gemini-2.5-pro 162.5 / 123.6; Claude-4.5-opus 178.4 / 170.3 | d01 | [S] |
| LLM: error types | PI: 56.1% same-key intrusion, 42.5% retrieval failure, 0.2% hallucination, 8.6% of failures refusals. RI: 50.8% retrieval failure, 46.0% intrusion, 0.9% hallucination. Over 97% of wrong retrievals carry no doubt signal. 5,409 RI and 9,753 PI errors | c09, b07 | [E] (Wang and Sun also find old same-key values) |
| LLM: reasoning models | RIES 178.0 vs 150.3 (d=1.76); PI accuracy 0 at N>=50 for 6 reasoning models vs 53.6% and 10.9% at N=50, 100 for non-reasoning; o1 RIES 186.4, PIES 22.0 | b08, d02 | [S] |
| LLM: forget instructions | under 10 points at 100 updates; per-key forget prompt anchored errors at the instruction; negative for gpt-4.1-mini | Wang and Sun (c05, d03) | [S] |
| LLM: mock QA reset | Gemini Flash 2.0 at 150 updates matched its no-reset score at 30-45 updates | d03 | [S] |
| LLM: chain of thought | worse or equal in 3 of 4 pairs; DeepSeek-R1 below V3 beyond 12 updates | a03 | [S] |
| LLM: quantization | Qwen2.5-7B 81.0% to 68.3% (INT4), McNemar p<=2.6e-6; same-key intrusions 21.5% to 24.6% | a06, b09 | [S] |
| LLM: GPT-J interference vs decay | conflicting facts about the same people cut recall much more than added neutral text; numbers in figures only | Janik 2023 (c11) | [S] |
| LLM: fan effect | fan 1 to 2 at list size 32: accuracy .991 to .915; no serial-position curve | Cao et al. 2025 (c12) | [S] |
| LLM: fan effect in probabilities | present in Mistral and SOLAR for absent items only; none in RoBERTa, GPT-2, Llama-2 | Roberts et al. 2024 (c13, d13) | [C] weak |
| Context rot: similar distractors hurt | 18 LLMs; 0, 1, 4 distractors; four worse than one; lower needle-question similarity degrades faster | Chroma 2025 (a09) | [E] (K13, 3 sources) |
| Focused vs full prompt | about 300 vs about 113k tokens, 306 prompts; focused better for all models | a10 | [S] |
| Outdated knowledge | outdated response rate 23-54%; accuracy drop 6-31%; MCQ 53-76% vs open 12-51%; 12 LLMs | Nakshatri et al. 2025 (c20) | [E] with STALE and TRACK |
| STALE | best model 55.2% on 400 scenarios, 1,200 queries; Qwen3.5-27B 31.3%; CUPMem (GPT-4o-mini) 68.0% vs 8.7% plain | Chao et al. 2026 (c29, d04) | [S] |
| TRACK | Qwen-3 1.7B 83.6% at 1 updated fact to 22.2% at 500; 8B 73.6% to 11.2%; GPT-4.1-mini stable | Feng et al. 2026 (c21) | [S] |
| MINTEval | six systems average about 28% (27.7 or 27.9 in the same paper), best 33.4%; evidence in retrieved pool 58.3% | Lee et al. 2026 (c18) | [S] |
| Date tags | lookback drop Full 13.22 to 5.48; RAG 31.43 to 10.45 | MINTEval (d06) | [S] |
| Bare date hint | AWS 26.95 to 28.40; Azure 22.95 to 22.40; WHO 50.64 to 46.15 | evolveQA (d07) | [S], different setting from tags |
| Hide superseded revisions | AMB-Text 91.86 vs 68.60; LME-KU 93.59 vs 60.26; MAB-FC 74.00 vs 51.00 at 2,048 tokens | Li and Li 2026 (d05) | [S] |
| Add-all memory hurts agents | RegAgent 55.48 vs 70.95 strict; EHRAgent 13.05 vs 38.50; AgentDriver 32.32 vs 51.00; CIC-IoT 59.90 vs 85.40 | Xiong et al. 2025 (c14, d11) | [E] |
| Relation, not count | count 8, lexical retrieval: unrelated -0.02, repeated -0.34, same-slot -0.50 plasticity (baseline 0.84) | Ding et al. 2026 (c16) | [S] |
| Dedup | M-tier 200K tokens 70.1 vs raw RAG 71.2; S-tier aggressive consolidation 48.4 vs raw 78.4 | Kerestecioglu et al. 2026 (a13, c22) | [S] |
| Distractor pruning by model size (BABILong) | Haiku 4.5 +0.083, Sonnet 4.6 +0.104, Opus 4.7 +0.008, GPT-5.5 +0.017 | Arjmandi 2026 (d10) | [S] |
| Retrieval dominates agent-memory errors | retrieval failure 11.4-46.3% vs utilization failure 3.9-8.1% | LoCoMo study (a14) | [E] |
| Trained fixes | Sculptor 13B 22.5 to 99.4 with RL; SleepGate 97.0% at depth 10, 16.5% at depth 30 | a08, a07 | [S], not for a scaffold |

## 4. Mechanisms and models

### 4.1 Retrieval competition (SAM with context, Mensink and Raaijmakers)

An engineer can model it like this.

- Memory is a set of images. Each image stores item, associative and context elements.
- A retrieval cue is matched to every image. Retrieval strength is the overlap of the cue with each image.
- Recovery probability for an image: 1 - exp[-S(I,C) - S(I,Si)] (context cue plus item cue strengths).
- Sampling picks an image in proportion to its strength share. More or stronger competitors sharing the cue lower the chance of the target.
- Search stops after Lmax failed attempts (fitted Lmax = 4.90 in one fit).
- Context elements flip on and off (rates .0035 active to inactive, .0001 inactive to active). This is why a context change gives release and why time since study matters.
- Parameters in the paper: conditioning rate .6, context scale .3, b1=b2=.05, residual d=.01. One parameter set fits all simulations (a24, a26).

What it predicts for an agent. If a lesson store is searched by cue similarity, the chance of returning the right entry falls as the number of entries that match the cue equally well rises. A cap on entries per class is the direct lever. A different context cue (a category label) shrinks the competitor set.

### 4.2 Release as search-set shrinkage

Baeuml and Kliegl (2013): three methods release PI (forget cue, testing the earlier list, context change). All work by reducing the set that retrieval has to search (a32). Latency supports this: prior lists slow later responses, release restores speed. The forget condition was 1.55 s faster than remember (p=.035) and 0.11 s from no-PI (ns). Implementation view: partition candidates by class tag, then retrieve within the tagged partition first.

Caveat: release depends on retrieval cues, not on change of material alone. Gardiner et al.: switching subcategory released PI only when participants were told which subcategory to retrieve (b20, second-hand).

### 4.3 LLM version: competition among same-key values

Stated by the authors, not proven.

- Wang and Sun: interference acts on a shared "anti-interference" resource. Tracked keys, updated keys and value length produce the same log-linear drop. Value length hurts most (c04). Sequential collapse is step-like at a model-specific threshold (a02).
- Chattaraj and Raj: a winner-take-all attention pattern with a primacy bias. PI errors are confident intrusions of earlier values, with no doubt signal (c09). Claims about superposition and attention sinks are post hoc and untested (a04).
- Error stages (Wang and Sun, c02): at low load, wrong answers are adjacent old updates; then far-earlier updates; then values never shown (hallucination) with primacy bias.
- Decay shapes: PI log-linear, near-universal. RI shapes vary: exponential 35% of models, polynomial 30%, log-quadratic 26%, power-law 9% (c10). At N>=200 PI is bimodal across sessions (above 85% or below 5%) (b07).

### 4.4 Mitigations that have been measured

1. **Structural reset (mock QA turn).** Insert a fake finished user turn asking for all keys, a fake assistant reply, and a new task start, about 120 updates before the end. It cuts the influence of everything before it. It was the only prompt-level fix that worked substantially (b03, d03). Unusable when the task needs selective access to history.
2. **Supersession link plus hidden view.** Keep an archive. Link a new fact to the old one by slot. Show only the current revision to current-state questions; show old ones for history questions (c23, d05). Training-free; needs an LLM curator.
3. **Write-time stale handling (CUPMem).** Mark stale states at write time, archive not delete. 68.0% vs 8.7% for the plain backbone; no component ablation (d04).
4. **Selective add and delete.** Add only runs judged good; delete records whose retrievals led to poor results. Needs a reliable utility signal; with noisy evaluators history deletion is unstable (c14, c15).
5. **Interference score and forgetting.** Pairwise similarity among stored items, weighted retroactive 0.6 and proactive 0.4; forget high-interference, low-value items. Thresholds: P90 of within-session similarity = 0.542 (interference), P99 = 0.559 (near-duplicate), with text-embedding-3-large (a12). Weights are asserted from the human literature, not fitted.
6. **Context edit tools (Sculptor).** Fragment, fold and search. Prompt-only: Claude-4-Sonnet 84.04 to 89.94 (+5.90), GPT-4.1 73.29 to 79.87 (+6.58), DeepSeek-V3 57.39 to 57.27. Unguided Claude used search for 90.7% of tool calls and did not filter (a08). The big gains came from training.
7. **Distractor-aware truncation.** Keep the signal, drop distractors (d10). Needs a known signal/distractor split, which a live agent lacks.
8. **Salient restatement of constraints.** For instruction loss under load, salient formatting restored 90-100% of compliance (a11). Task-load interference; the link is by analogy only.

## 5. What holds up

**Replications and strong results.**
- PI builds over trials in short-term recall and is released by a category change. Baeuml and Kliegl (2013) replicated Wixted and Rohrer (1993) with d=1.07 to 1.34, and found release by three methods (a32).
- Adding all experiences to agent memory degrades agents. Four agent types agree: add-all below strict selective add on all four, and below a fixed small memory on all four (c14, d11).
- Outdated facts hurt answers in three independent LLM studies (Nakshatri, STALE, TRACK) (K12).
- Similar distractors hurt long-context retrieval beyond length (Chroma, Wang and Sun fixed-length control, MINTEval, Arjmandi) (K13).
- Reasoning and prompts do not fix LLM PI (Wang and Sun CoT; Chattaraj reasoning models at 0% for N>=50) (K03, K07, d02).

**Failures and contested points.**
- Peterson and Peterson did not find PI in their own data (a16). The PI account of short-term forgetting came afterwards. Do not cite them as PI evidence.
- Hubbard et al. (2018) found no release in its paradigm (b21, snippet only). Release depends on retrieval cues (b20).
- The RI time gradient is weak (F=2.83 p<.10; F=5.91 p<.05) (a23).
- Unlearning predictions (spontaneous recovery) did not replicate reliably (a25).
- Size and PI in LLMs: Wang and Sun R2=0.26 significant vs Chattaraj R2=0.06 ns (b10). Different model sets (30 mostly dense open vs 39 with MoE and closed) and metrics (IES vs PIES). Context-window length predicts nothing in either (R2=0.003 in Chattaraj).
- A bare date hint does not help (evolveQA), but date tags on facts and questions do (MINTEval). Different tasks, so both can hold.
- Dedup: moderate dedup is safe (70.1 vs 71.2), aggressive consolidation hurts (48.4 vs 78.4) (K10). At small scale, forgetting did not beat raw RAG (c22).
- Raw chunks (77.9 cosine) beat extracted facts (72.2) on LoCoMo (a14). Compressing memory is not free.
- Internal inconsistency in MINTEval (27.7 vs 27.9) and a squared rho in Wang and Sun (rho squared = 0.673, p=0.0016, not rho) were found in the audit (critique).

**Moderators.**
- Similarity and relation (K09). Lexical retrieval: damage complete by 2 related entries, then flat (plasticity .84 to .50 repeated, .34 same-slot). Dense retrieval: keeps falling to 8 (repeated .84/.58/.40/.38; same-slot .84/.60/.44/.40; same-slot stability .92/.78/.62/.54) (d08, d09). Dense repeated-history loss (-0.46) is not smaller than same-slot (-0.44), so "same-slot is worse" holds for lexical only (critique).
- Item length (K06).
- Familiarity (K21).
- Model size at the top: pruning distractors gives +0.008 to +0.017 for Opus 4.7 and GPT-5.5, +0.083 to +0.104 for Haiku 4.5 and Sonnet 4.6 on BABILong (d10). On MRCR v2 results were mixed (Haiku +0.198, Sonnet -0.112, Opus -0.060).
- Spacing (human): massed prior learning gives PI, spaced does not.
- Quantization: INT4 raises same-key intrusions with similar distractors, reverses with numeric ones (K14).
- Age and frontal damage (human): larger PI (K20).

**Interventions that worked.** Mock QA reset. Supersession plus hidden view (+23.3, +33.3, +23.0). Strict selective add (+10 to +25 points). Date tags (drop cut by more than half). Focused prompt over full history. Trained context management (not available to us).

**Interventions that did not.** "Forget" and "focus" prompts (under 10 points). Chain of thought. Reasoning models on PI. Bare date hint. Larger declared context window. Prompt-only context tools without guidance (DeepSeek-V3: no gain). Aggressive consolidation.

## 6. Language models

**Paradigm.** Mostly synthetic key-value update streams. Ask for the latest value of a key (PI-like) or the first value (RI-like).

**Wang and Sun (2025), PI-LLM** (a01-a03, b01-b04, c01-c06, d03).
- 46 keys, 3 to 400 updates per key, 0.6B to 637B parameters.
- Accuracy falls log-linearly toward 0. The mid-size tier reaches about 0% at 400 updates. Larger models stay relatively high.
- Errors: old values of the same key; spreading to far values and then invented values as load rises.
- Fixed total input length with more tracked keys still hurts (llama4-maverick near 100% at 2 tracked keys, below 5% at 46).
- Value length 10 words: under 40%. 40 words: under 5%.
- Parameter size class predicts endurance (t=3.03, p=0.005), context length does not (p=0.886), R2=0.261, N=30. MoE models score below dense at similar total size.
- Prompts: forget, focus, soft reset, relevance meta-prompt give under 10 points. The mock QA reset helps most.

**Chattaraj and Raj (2026), AB-AC logic** (a04, a05, b05-b08, c07-c10, d01, d02).
- 39 of 54 models with full data, 1B to 2.5T parameters, up to 50 sessions at temperature 0.
- PI worse than RI in all 39. Gap 69.5 points, d=1.73. RI and PI endurance are nearly uncorrelated (r=0.21, CI -0.11 to 0.49).
- Frontier gap: GPT-5 186.4 vs 99.2, o3 185.8 vs 76.0, Gemini-2.5-pro 162.5 vs 123.6, Claude-4.5-opus 178.4 vs 170.3 (almost closed). One lab, one paradigm; proprietary parameter counts are estimates.
- Reasoning models gain on RI (178.0 vs 150.3) but fall to 0 PI accuracy at N>=50. o1: RIES 186.4 (rank 1), PIES 22.0 (rank 35).
- Errors are confident: over 97% of wrong retrievals have no uncertainty signal.

**Memory-agent and RAG studies.**
- MINTEval: about 28% average accuracy across six systems. Simple (latest-value) questions 47.5%; History 21.0%; multi-target 26.5%. Evidence is in the retrieved pool only 58.3% of the time, and answer errors add a further 25.2% drop. Insert is 87.6% (AtomMem) and 65.9% (Mem-) of memory operations, so stores grow fast. Out-of-domain distractors hurt RAG most (d06), which cuts against pure similarity as the only driver.
- CMI (Ding): see section 5. A selector trained on interference-labelled cases raised noisy-update success .386 to .686 (+.300, CI .129 to .486) in-domain, +.114 on LongMemEval. Poisoning depends more on update-authority wording than on recency (c17).
- Xiong et al.: agents copy the output of the most similar stored experience ("experience following"). Errors propagate (b15).
- Janik (2023): GPT-J recall falls more from conflicting facts about the same people than from added neutral text (c11).
- Cao et al. (2025): fan effect in recognition (.991 to .915), no serial-position curve (c12). Roberts et al. (2024): fan effect in probabilities for two models only (c13).
- Hong et al. (2025): 18 LLMs; four similar distractors worse than one; a focused 300-token prompt beats the full 113k-token history on LongMemEval for all models (a09, a10).

**What changed the results, by how much.**

| Change | Effect | Source |
|---|---|---|
| Mock QA reset | 150 updates scores like 30-45 updates without it | d03 |
| Hide superseded revisions | +23.3, +33.3, +23.0 points | d05 |
| Strict selective add vs add-all | +15.5 (RegAgent), +25.5 (EHRAgent), +18.7 (AgentDriver), +25.5 (CIC-IoT) | d11 |
| Date tags | lookback drop 13.22 to 5.48 (Full), 31.43 to 10.45 (RAG) | d06 |
| Distractor pruning, smaller models | +0.083, +0.104 | d10 |
| Distractor pruning, largest models | +0.008, +0.017 | d10 |
| Forget prompt | under 10 points | c05 |
| Chain of thought | worse or equal | a03 |
| Prompt-guided context tools | +5.9, +6.6, 0 | a08 |
| Trained context tools (RL) | 22.5 to 99.4 | a08 |
| INT4 quantization | -12.7 points (Qwen2.5-7B) | a06 |

**Weak spots.** Almost all evidence is synthetic key-value or QA benchmarks. No study uses an agent doing real multi-step work with interfering memories. Several 2026 items are single-paper arXiv preprints with garbled tables. Mitigation numbers for the mock reset and timestamps exist only in figures or as anchor comparisons.

## 7. What our agent should take

Each item: schema part | status | evidence ids.

### Add now (established)

1. **Do not add every experience to memory. Add only entries that pass a check; delete entries whose retrievals led to poor results.** Memory. [E]. Evidence c14, d11, b15, c15, a12 (K08). Caveat: needs a reliable utility signal; Xiong sizes are record counts, not tokens.
2. **Hide superseded versions of the same fact from the working view. Keep them in an archive.** Memory. The idea that outdated facts hurt answers is [E] (c20, c21, c29; K12). The size of the hide-vs-keep gap is [S] (d05). Add the hide rule now; test the size (UNKNOWNS).
3. **Give the model less, and more focused, context rather than the whole history. Strip distractors that are similar to the question and not needed.** G / memory. [E]. Evidence a09, a10, b16, c18, d10 (K13).
4. **Do not rely on "ignore the old stuff" instructions to handle stale or conflicting entries. Remove them structurally instead.** G / memory. [S] on size (K03: a03, b03, c05, d03), but the direction is consistent and following it costs nothing.
5. **Measure retrieval hit rate separately from answer correctness in our logs.** Memory. [E]. Evidence a14, c18 (K25). Retrieval failure was 11-46% vs utilization failure 4-8%.
6. **Assume old similar entries stay reachable by cue. Do not treat "deleted in the prompt" as forgotten.** Memory. Mechanism [C] (K19), but the practical consequence holds under all accounts.

### Test first

All of these are in UNKNOWNS.md with tests.

- Per-class cap on similar entries (3 to 5). Memory. [S]. Evidence d08, d09, c16, d11 (K27). No cap arm has ever been run.
- Category-label rotation for release from PI in LLM retrieval. Memory. Human [E] (K15, K29), LLM open (K30, d19). Choose far classes.
- Version/date tags on every entry. Memory. [S] (c19, d06; a bare hint failed in d07).
- Hide-superseded vs delete-superseded vs keep-with-tags, head to head. Memory. [S] (d05, d04).
- Short normalized entries instead of verbose ones. Memory. [S] (K06: a02, c04, d03).
- Structural reset (summarize-and-restart, fresh context) vs prompt. G / memory. [S] (K03: a03, b03, d03).
- Near-duplicate merge above a similarity threshold, never merging conflicting updates. Memory. [S] (K10: a13, c22, a12).
- Per-item interference ledger (AIM). Memory. [S] (d18, numbers unread).
- Reasoning tokens before retrieval: expect no help (K07). O / G. [S] (d02). Low priority.
- Whether a strong model makes the cap unnecessary. Memory. [S] (K28: d01, d10).
- Salient, last-position placement for critical constraints. G. [S] (K22: a11). Analogy only.

## 8. Concrete tests on our bench

For all tests: both arms at equal tokens (context or retrieved tokens fixed, not record counts). At least 3 seeds. Report confidence intervals.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Same-key update stream (our synthetic, plus PI-LLM format), 3 to 300 superseded versions | (a) keep all, (b) hide superseded with archive, (c) delete superseded, (d) keep all with version tags | accuracy on latest value; stale-answer rate | (b) and (c) beat (a) by 20+ points at high counts (d05: 23-33); (d) in between |
| T2 | Agent tasks with a lesson library, classes known (problem type), 1 to 30 lessons per class | cap per class at 1, 2, 3, 5, 8, uncapped, same total tokens | task pass rate | Knee at 2 to 4 for near-duplicates; flat for unrelated lessons |
| T3 | Same library with runs of same-class near-duplicates | (a) top-k by similarity, (b) top-k with at most m per class, (c) one per class across 3 classes | task pass rate | (b) and (c) beat (a) |
| T4 | Memory at fixed count, vary relation | unrelated, near-duplicate, conflicting update (CMI-style) | plasticity (adopts valid update), stability | Unrelated about 0 effect; conflicting update large (d08: -0.50 lexical) |
| T5 | Verbose vs short normalized entries | same total tokens, so the verbose arm holds fewer entries | latest-value recall; task pass rate | Short entries win at high counts (a02) |
| T6 | Long update stream, reset methods | (a) none, (b) "forget old" prompt, (c) mock QA reset, (d) summarize-and-restart, (e) fresh context with current state only | latest-value accuracy at 100 and 300 updates | (c), (d), (e) beat (b); (b) gains under 10 points |
| T7 | Paired RI and PI items | first-value vs latest-value queries on our model | accuracy gap | PI worse than RI by a large gap, unless the model is Claude-4.5-opus class (gap about 8) |
| T8 | Near-duplicate dedup | similarity threshold sweep (P90, P95, P99 of within-store similarity) | pass rate; store size | Moderate dedup within 1 point of raw; aggressive loses 10+ |
| T9 | Dose-response with realistic entries | 0, 1, 2, 3, 5, 8, 16 similar entries per cue | answer accuracy; retrieval hit rate | Locate the knee |
| T10 | Model-size check | run T2 on a small and a large model | cap gain per model | Gain larger for small and mid models (d10) |
| T11 | Reasoning tokens | with and without extra reasoning before retrieval | latest-version accuracy | No gain (d02) |
| T12 | Category rotation (release) | retrieval from same class run vs forced rotation to a far class vs near class | task pass rate | Far-class rotation restores accuracy after runs of same-class entries |

## 9. What does not transfer, and why

- **Time-based decay and consolidation (Muller and Pilzecker, sleep, Jenkins and Dallenbach).** An LLM context has no sleep. A persisted store has time stamps, but no biology.
- **Unlearning (Melton and Irwin).** Nothing in a context is weakened by new learning. Old entries stay fully present.
- **Neural findings (left IFG, TMS, EEG theta and alpha, aging, frontal patients).** No agent lever (K20).
- **Human RI vs PI strength pattern.** Humans: RI usually exceeds PI for paired associates. Current LLMs: PI is harder (K05). Do not carry human ratios over.
- **Human plateau.** Humans appear to plateau because they unbind outdated associations (Oberauer and Vockenberg 2009, cited by Wang and Sun). LLM curves keep falling (c06). Do not assume graceful saturation.
- **Quantization, SleepGate and Sculptor RL.** Training or deployment features a scaffold cannot change (K14, K23, K24).
- **Directed-forgetting instructions.** Work in humans (a cost of 136 ms, but effective); weak in LLMs (K03).
- **Parameter-count effect.** Not agent-controllable (K04). It only sets expectations: a bigger declared context window buys no resistance.
- **Peterson and Peterson as PI proof.** Their own data show no PI (K16).
- **Synthetic key-value results to real agent memory.** The target sits right before the query, entries are tiny and share one key. Real memory is varied and fuzzy in relation. Treat effect sizes as upper bounds.
- **Fan-effect probabilities.** Measure token probability, not accuracy, and are absent for present items (c13).

## 10. Open questions

1. Does capping similar entries per class (3 to 5) improve agent task performance at equal tokens in a real multi-step agent, against add-all and selective-add? (no paper tests it)
2. Does a category change release PI for an LLM? Does labelling or rotating entries by category and retrieving from a different class restore accuracy? (nothing found)
3. Does PI-harder-than-RI replicate outside the same lab and with retrieval memory?
4. How big is the benefit of tags vs deletion vs hiding, head to head?
5. What is the dose-response curve and knee for near-duplicates in real entries? CMI has only counts 0, 2, 4, 8 on synthetic transformations.
6. Which structural reset works best at equal tokens?
7. Does shortening entries cut interference?
8. Is there a similarity threshold that decides what to merge or cap? Kerestecioglu's 0.542 and 0.559 are for one embedder, and MINTEval shows out-of-domain distractors also hurt RAG.
9. Human numbers (Wickens 1963/70, Underwood and Ekstrand, Keppel and Underwood tables) are second-hand. Primary tables not opened.
10. Why does a Claude-4.5-opus class model nearly close the PI/RI gap? Training, architecture or test artifact?
11. Why is PI bimodal at N>=200 (above 85% or below 5%)? Sampling or format?
12. Does AIM's per-item ledger (ICLR 2026) hold up, and by how much? Numbers not read.

## 11. Sources

[V] opened by the evidence agents; [M] snippet or secondary only.

**Human literature**
- [V] Peterson and Peterson (1959). https://labs.la.utexas.edu/gilden/files/2016/03/1545ca4cdad4f480f2fab8fd505a5b7f7603.pdf (a15, a16)
- [V] Turvey, Mosher and Katz (1971). https://link.springer.com/content/pdf/10.3758/BF03335908.pdf (a17)
- [V] Wixted (2004), covers Underwood 1957, Muller and Pilzecker 1900, Jenkins and Dallenbach, Ekstrand 1967, Archer and Underwood 1951, Newton and Wickens. https://cenl.ucsd.edu/Jclub/Wixted_2004.pdf (a18, a20-a23)
- [M] Underwood (1957) abstract. https://scilit.com/publications/75be16396a7f3298a4cdaed925ea45ba (a19); https://psycnet.apa.org/record/1957-05013-001 (b25)
- [M] Keppel and Underwood (1962). https://scilit.com/publications/ce0519a398bb6fdfdcc13ede946306a2 (a27); https://link.springer.com/article/10.3758/BF03328941 (b24)
- [V] Loftus and Patterson (1975), quoting Keppel and Underwood. https://faculty.washington.edu/gloftus/MiscMissingArticles/Loftus.Patterson.1975.pdf (d15)
- [V] Lindsey thesis, release from PI. https://repository.gatech.edu/server/api/core/bitstreams/e7ad3e58-b524-40af-b2f3-167a7cacc (d16)
- [V] Wikipedia, Delos Wickens. https://en.wikipedia.org/wiki/Delos_Wickens (a28)
- [V] Wikipedia, Interference theory (secondary; Greenberg and Underwood 1950, Briggs 1954, Barnes and Underwood 1959). https://en.wikipedia.org/wiki/Interference_theory (a29, a30, b22; b23 the Wickens entry not opened)
- [V] Mensink and Raaijmakers (1988). https://raaijmakers.edu.fmg.uva.nl/PDFs/Mensink%20and%20Raaijmakers.pdf (a24-a26)
- [V] Kliegl and Baeuml (2021). https://baeuml.app.uni-regensburg.de/paper/papers_open/KB_BrainSciences.pdf (a31)
- [V] Baeuml and Kliegl (2013). https://baeuml.app.uni-regensburg.de/paper/papers_open/BK%282013%29_JML.pdf (a32)
- [M] Anderson (2003); Anderson and Neely (1996). https://www.bohrium.com/paper-details/rethinking-interference-theory-executive-control-and-the-mechanisms-of-forgetting/812381492796719104-10178 (a33); https://doi.org/10.1016/b978-012102570-0/50010-0 (b27)
- [V] Jonides and Nee (2006). https://www.ocf.berkeley.edu/~denee/assets/jonidesneeneurosci2006.pdf (b17, b18)
- [V] Mercer (2025). https://doi.org/10.1177/17470218251317191 (b19, b20, b28)
- [M] Hubbard et al. (2018). https://www.tandfonline.com/doi/full/10.1080/09658211.2018.1428349 (b21, d17)
- [M] Feredoes, Tononi and Postle (2006). https://pmc.ncbi.nlm.nih.gov/articles/PMC1748259 (b26)

**LLM and AI studies**
- [V] Wang and Sun (2025). https://arxiv.org/abs/2506.08184 ; https://arxiv.org/html/2506.08184v3
- [V] Chattaraj and Raj (2026). https://arxiv.org/abs/2603.00270 ; https://arxiv.org/html/2603.00270v2
- [V] Shahrabi-Farahani and Rahmati (2026), abstract only. https://arxiv.org/abs/2608.18578
- [V] SleepGate / Xie (2026). https://arxiv.org/abs/2603.14517
- [V] Sculptor (2025). https://arxiv.org/abs/2508.04664
- [V] Hong, Troynikov and Huber (2025), Context Rot. https://www.trychroma.com/research/context-rot
- [M] Context Rot secondary write-up. https://www.prompthub.us/blog/why-long-context-windows-still-dont-work (c25)
- [V] Mittal (2026), abstract only. https://arxiv.org/abs/2603.23530
- [V] Kerestecioglu et al. (2026). https://arxiv.org/pdf/2605.08538 ; https://arxiv.org/abs/2605.08538
- [V] LoCoMo retrieval vs utilization study. https://arxiv.org/html/2603.02473v1
- [V] Janik (2023). https://arxiv.org/abs/2311.03839
- [V] Cao, Schooler and Zafarani (2025). https://arxiv.org/abs/2509.17138
- [V] Roberts et al. (2024). https://arxiv.org/abs/2407.06349 ; https://arxiv.org/html/2407.06349
- [V] Xiong et al. (2025). https://arxiv.org/abs/2505.16067 ; https://arxiv.org/html/2505.16067
- [V] Ding et al. (2026), CMI. https://arxiv.org/abs/2608.07622 ; https://arxiv.org/html/2608.07622
- [V] Arjmandi (2026). https://arxiv.org/abs/2608.03297 ; https://arxiv.org/html/2608.03297
- [V] Lee et al. (2026), MINTEval. https://arxiv.org/abs/2605.18565
- [V] Nakshatri et al. (2025). https://arxiv.org/abs/2510.19172 ; https://arxiv.org/html/2510.19172
- [V] Feng et al. (2026), TRACK. https://arxiv.org/abs/2601.15495
- [V] Li and Li (2026). https://arxiv.org/abs/2609.10263 ; https://arxiv.org/html/2609.10263
- [V] Chao et al. (2026), STALE. https://arxiv.org/abs/2605.06527 ; https://arxiv.org/html/2605.06527
- [V] Li, Ding and Hu (2026), abstract only. https://arxiv.org/abs/2605.28705
- [V] Zhu et al. (2026), HyMem. https://arxiv.org/abs/2603.10291
- [V] Decocted Experience (2026). https://arxiv.org/abs/2604.04373 ; https://arxiv.org/html/2604.04373
- [V] AIM, ICLR 2026, abstract page only. https://iclr.cc/virtual/2026/10022406

**Links to parallel subfields (note only):** Relevance-based fate of memories; Retention policy; Case-base maintenance; Retrieval and similarity; Schemas; Complementary learning systems; Prioritised memory access; Retrieval as a bandit; Desirable difficulties; Critiques of encoding specificity.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 3 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A06.03-K02** (reworded: the sources support less). Chattaraj and Raj numbers verified (PI errors 56.1% same-key intrusion, 42.5% retrieval failure, 0.2% hallucination; RI hallucination 0.9%), but Wang and Sun report the opposite trend at high interference (a three-stage progression ending in hallucinated values never shown plus primacy bias), so 'not hallucination' rests on one study's classifier and the sources disagree. Corrected claim: In one 54-model study (Chattaraj and Raj 2026, 9,753 proactive-interference errors), 56.1% of errors were same-key intrusions of earlier values and 42.5% were retrieval failures (no value returned), with only 0.2% hallucinated values absent from the sequence (0.9% for retroactive errors); an earlier study (Wang and Sun 2025) instead reports a growing share of hallucinated values and a primacy bias toward the first updates at the highest interference loads, so the hallucination share depends on load and classifier.
- **A06.03-K08** (reworded: the sources support less). Xiong et al. numbers verified (add-all vs strict: EHRAgent 13.05 vs 38.50, RegAgent 55.48 vs 70.95, AgentDriver 32.32 vs 51.00, CIC-IoT 59.90 vs 85.40; fixed memory 16.75/67.53/40.11/71.50), but this is one study with GPT-4o-mini agents on four tasks, the comparison is to a small fixed memory (50-180 records), and Kerestecioglu et al. measure retention precision and on LongMemEval find forgetting does not beat plain retrieval (70.1 vs 71.2), so 'in agents' is wider than the evidence. Corrected claim: In one study of four GPT-4o-mini agents (Xiong et al. 2025), adding every experience to memory scored below a small fixed memory (e.g. EHRAgent accuracy 13.05 vs 16.75), while adding only experiences passing a strict evaluator scored above it (38.50 for EHRAgent; 70.95 vs 67.53 RegAgent), with history-based deletion helping further when the evaluator is reliable; a separate memory-architecture study found forgetting only matched, not beat, plain retrieval on LongMemEval (70.1% vs 71.2%).
- **A06.03-K13** (reworded: the sources support less). Chroma technical report supports distractor harm and the focused (~300 token) vs full (~113k) gain, but Arjmandi's distractor removal helped only Haiku 4.5 (+0.083) and Sonnet 4.6 (+0.104) on BABILong, was neutral for Opus 4.7 (+0.008, ns) and GPT-5.5 (+0.017), and was negative on MRCR v2 for Sonnet (-0.112) and Opus (-0.060); the focused-vs-full comparison also changes length and distractors together. Corrected claim: Distractors similar to the needle or question lower long-context accuracy beyond length (Chroma technical report: more distractors, lower needle-question similarity and longer inputs all degrade accuracy across 18 LLMs, and ~300-token focused prompts beat ~113k-token full histories on LongMemEval), and removing distractors while keeping the evidence raised accuracy for smaller models on BABILong (Haiku 4.5 +0.083, Sonnet 4.6 +0.104) but not for the strongest models (Opus 4.7 +0.008, GPT-5.5 +0.017) and was mixed on MRCR v2 (Sonnet -0.112, Opus -0.060) in a single-author preprint.
- **A06.03-K15** (reworded: the sources support less). Baeuml and Kliegl 2013 study list-learning release via a forget cue, testing the earlier list or an internal context change (not a category change), report 'almost complete' release for the forget cue only as a non-significant difference (no-PI vs forget p=.173, N=24), and conclude release reflects a smaller memory search set; PI build-up and category-shift release come from secondary pages (Wikipedia, a thesis), and Peterson and Peterson found no PI build-up in their own check. Corrected claim: In list-learning experiments (Baeuml and Kliegl 2013), proactive interference lowered recall and slowed responses, and three release methods (a forget cue, testing the earlier list, an internal context change) restored recall and speed, with the forget cue giving almost complete release (14.58% lower recall with remember cue vs no-PI, n.s. difference to forget, p=.173), consistent with a smaller search set; the classic buildup over trials and release by a category change (Wickens paradigm) are documented here only through secondary sources.
- **A06.03-K25** (reworded: the sources support less). Numbers verified (LoCoMo retrieval failure 11.4-46.3% vs utilization failure 3.9-8.1%; MINTEval evidence in pool 58.3%), but MINTEval also finds that answering errors add a 25.2% drop even when evidence is present, far above LoCoMo's 4-8% utilization failure, and the 41.7% loss is attributed to memory construction as well as retrieval, so 'retrieval quality dominates' holds in LoCoMo but is weaker in MINTEval. Corrected claim: On LoCoMo (GPT-5-mini, 1,540 questions) retrieval failures were 11.4-46.3% of questions versus 3.9-8.1% utilization failures; on the multi-target interference benchmark MINTEval the needed evidence reached the retrieved pool in only 58.3% of cases (a 41.7% loss from memory construction and retrieval), but even with evidence present answering errors added a further 25.2% drop, so utilization is a smaller but not negligible bottleneck there.
- **A06.03-K17** (now single-source: only one opened source, code check).
