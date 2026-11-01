# Critiques of encoding specificity: deep document

*Subfield A06.02. Evidence: evidence_a.jsonl (a01-a26, founding studies and AI memory), evidence_b.jsonl (b01-b33, match versus discrimination, context meta-analysis, machine cue studies), evidence_c.jsonl (c01-c23, retrieval and long-context studies), evidence_d.jsonl (d01-d36, gap search). Claims: A06.02-K01 to K42 (claims.jsonl, cited below as K01...). Cross-check: critique.md. Status marks: [E] established (two or more independent sources agree), [S] single source, [C] contested. Evidence ids are the short ids (a05, d28). Sections 1 to 6 describe the science; sections 7 to 10 say what to do about it.*

**Corrections carried over from the cross-check (critique.md).**
- The RippleMem ablation (a18) is mislabelled in the evidence line. Use only "removing a component costs 3.2 to 4.6 percent relative". The 83.83 figure is the "w/o Structural" row and also happens to be RF-Mem's score.
- "Postman found recall lower than recognition in all eight Tulving-Wiseman conditions" (a09, a20) is unverified. The text read supports only "recall was not found to be superior to recognition".
- The r=.27 in a25 is printed with a CI (.06 to .55) that excludes zero, although the authors call it nonsignificant. Cite as printed, with that caveat.
- The Cuconasu -25% and -67% are peaks. The +35% random-document gain is +0.07 absolute on a base near 0.2.
- NoLiMa and HippoRAG: cite the tables, not the prose (row mix-up of Llama 3.1 vs 3.3; HippoRAG text and table disagree on which dataset gains).

---

## 1. What it is

The **encoding specificity principle** (Tulving and Thomson 1973) says: what is stored depends on how the item was encoded, and a retrieval cue works only if information about it was stored with the item. A cue is not good in itself. It is good for a trace.

The **popular reading** is stronger and simpler: the more a retrieval cue matches the study context, the better the recall. This is the **encoding-retrieval match principle**. Most textbooks and many AI memory papers use this reading.

This subfield is the set of critiques of that popular reading. Five matter.

1. **Match is correlational, not causal** (Nairne 2002 [d01, abstract only]). Match and recall usually rise together because both follow from a third thing: how specifically the cue points to one target. Raising match can help, do nothing, or hurt.
2. **Diagnostic value predicts recall** (memory as discrimination). The chance of recalling a target from a cue is roughly the cue-target similarity divided by the summed similarity of the cue to all candidates (b05). Match is the numerator. Rival items sharing the cue are the denominator. This is the ratio rule, also found in the SAM model and in Luce choice.
3. **Strong cues that "fail" are a reporting artefact** (Higham 2002 [b11, d02]). The classic result that strong extralist cues do not beat no cue came from people withholding correct answers.
4. **Outshining.** Context (a room, a background, a scene) helps mostly when no better cue exists. When a strong associative or semantic cue is present, context adds little (Smith and Vela 2001 [b19]; Isarida 2012 [a13]).
5. **The founding recognition-failure law is partly an aggregate artefact.** The Tulving-Wiseman function (c=.50, r=.95) fits pooled data, but failures live in a minority of items whose cue and target are linked outside the study episode (Duan 1998 [a05, a25]).

**Why it matters for our agent.** Our agent writes notes to a store and later queries it. The popular reading says: make the query look like the stored note. The critique says four things instead.
- Give each note a key that points to it and few others.
- Count how many rivals share each key (cue overload).
- Keep more than one retrieval route per note, because routes fail independently (a02, a06).
- Add a distinguishing line at write time only where the plain key is weak, and only if it is true to the note.

In one phrase from the brief: use distinctive keys, not only matching ones. The human evidence for this is strong. The evidence that it works on language-model agents is thin and mostly indirect (section 6).

---

## 2. History and theories in depth

Items marked [M] below come from background knowledge or from papers whose full text was not opened. Section 11 lists which sources were opened.

### 2.1 The founding studies (1970 to 1975)

- **Thomson and Tulving (1970)** [M, paywalled]. Cued recall with weakly or strongly associated extralist cues. The widely quoted result: a weak cue studied with the word helps; a strong cue never studied with the word does not. Higham (2002) re-ran it (section 2.4). No numbers from the original are used in this document (K24).
- **Tulving and Thomson (1973)** [M, paywalled; d03 not retrieved]. States the principle. Recognition of a word can fail although the same word is recalled from its list cue. Their percentages are NOT quoted here (K24, critique gap 10).
- **Watkins and Tulving (1975)** [second-hand only]. Quoted via Tulving and Wiseman (1975) (a01): Exp 3, subject-made test. Recognised and recalled .26. Recognised only .06. Recalled only .37. Neither .31. Overall recognition .32, recall .63, recognition given recall .41. So recall (.63) beat recognition (.32), which is the "recognition failure of recallable words".
- **Tulving and Wiseman (1975)** [a01, a02, a03, opened]. The function: P(Rn|Rc) = P(Rn) + c[P(Rn) - P(Rn)^2], with c = .50 fitted by least squares over 40 data points from 40 conditions in 12 experiments; r = .95 with the data; standard error of estimate .028. Old theory (recognition is the easier access route, so every recalled word is recognised) predicts a flat line at 1.00. Full independence predicts the diagonal. The data sit between: partial independence. The authors flag that the recognition test may change the trace, so test order is a possible confound (a03, K36).

### 2.2 The rival: generate-recognize

- **Bahrick's generate-recognize theory** [M, background]. Recall is two stages. The person generates candidates from the cue, then recognises the right one. If so, anything recalled should be recognised.
- **Kintsch (1978)** [cited in a04]. Offered response-criterion differences as a rescue.
- **Gardiner (1988)** [a04]. Tested the theory on its own terms using free-recall failures. Exp 1: recognition .732, cued recall .662; recognition given recall observed .838 vs expected .830; free-recall failures .721 vs .735. Exp 2 (strict scoring): .561 observed vs .668 expected in one cell. No extra dependency; the law held in all three replications. The theory predicted values near 1.00; they did not occur.
- **Guynn, McDaniel and colleagues (2014)** [a16]. A revised generate-recognize model (Jacoby and Hollingshead 1990) survives if recognition is optional. Item-specific encoding boosts the recognition component; relational encoding boosts generation. Exp 1: category production .25 (read) vs .24 (anagram), category-cued recall .18 vs .25, recognition of produced items .78 vs .94 (K35).

### 2.3 Early challenges to the principle

- **Humphreys and Galbraith (1975)** [cited in a11]. Said the supporting evidence rested on paired-associate instructions.
- **Ley (1977)** [a11]. Silent study replicated the H and G pattern: strong-elicitor A words worked as extralist cues, weak ones did not (cue-to-target strength 38.8% for A to B vs 2.5% for B to A). With associative encoding both directions worked. Exp 2 (100 subjects, 25 per cell): cued recall 12.39 for A-word targets vs 12.76 for B-word targets; cued total 25.15 vs free total 18.40; combined type effect F(1,192)=13.4. So what happens at study decides which keys work.
- **Postman (1975)** [a09, a10, b13, b14, b15]. Two failures to replicate. Exp 1 crossed cue strength at input and at output: strong output cues beat weak ones whatever the input cue was (output strength F(1,92)=94.68; output by input F(1,92)=11.78). Stringent scores per cell: same-cue S-S 4.29, W-S 3.04, W-W 2.33; new-cue S-S 4.00, W-S 3.17, W-W .17. With strong cues same-cue and new-cue recall were almost equal. Exp 2: recall was not found superior to recognition. He offers rival readings: a novel cue may fail because it is novel, not because it changes meaning; the pairwise contingency may reflect the instructions. He cannot say why his results differ from Watkins and Tulving.
- **Reder, Anderson and Bjork (1974)** [cited in a01]. Recall superiority reverses for low-frequency words.
- **Epstein, Dupree and Gronikowski (1979)** [a12]. Category headings crossed at input and output. Exp 1, 22 subjects: categorised at input 62.78% vs uncategorised 35.80%, F(1,21)=103.14; heading at recall only 57.10% vs uncued 26.14%, t(21)=8.23; cued-cued 73.58% vs uncategorised-cued 57.10%, t(21)=5.70. A cue helped though it was absent at input. A strict copy-match version of the principle fails. Tulving (personal communication) weakened the principle in response.
- **Fisher (1979)** [a07]. Pre-existing link direction matters. 48 students. Recall rose with cue-to-target association F(1,23)=51.7 (target-to-cue F(1,23)=1.1). Recognition rose with target-to-cue association F(1,23)=53.0 (cue-to-target F(1,23)=1.3). Overall hit .72 recognition vs .55 recall; for Hi-Lo pairs recall .68 beat recognition .61.
- **Wells and Hryciw (1984)** [a08]. Crossover for faces, N=80. Trait judgment gave 55% vs 25% recognition (Z=2.03). Feature judgment gave better feature reconstruction, mean 28.6 vs 19.2 (Z=2.4). So the best encoding for one test is the worst for another.
- **Stein (1977)** [b16, b17]. Unique relation per pair: Exp 1 (N=40) cued recall 14.31 (simile rating) vs 5.24 of 24 (hard-soft rating), t(38)=8.9; yes-rated 78% vs 36%; intrusions .5 vs 1.9. Exp 2 pair recognition 11.2 vs 9.3 of 12, false positives .40 vs 1.7. Exp 3 single-item recognition 42.0 vs 43.3 of 48, not significant. So uniqueness of the relation drives cue power for pairs, not for item recognition (K04).

### 2.4 The modern critiques (2001 to 2016)

- **Nairne (2001, 2002)** [d01, b05; 2002 abstract only]. "The myth of the encoding-retrieval match." Memory as discrimination.
- **Poirier, Nairne and colleagues (2012)** [b01-b06, d27]. Four cued-recognition experiments. Adding a shared (non-diagnostic) cue to a unique cue increased match but slowed retrieval, about 200 to 300 ms. Accuracy was above 90% (Exp 1) and above 98% (Exp 4) after training, so the effect is in speed.
- **Goh and Lu (2012)** [b07-b10, d06]. Independent lab (NUS). Exp 1 (N=40): low overload high-match .37 vs low-match .24, F(1,39)=17.14; high overload .28 vs .28, F<1; interaction F(1,39)=13.89. Exp 2 (N=43): .31 vs .20, F(1,41)=12.15; high overload .24 vs .23; interaction F(1,41)=5.23. Exp 3 (N=40, the Thomson-Tulving design with overload held constant): intralist .32, strong extralist .25, weak extralist .09, F(2,78)=38.33. Match still helps when overload is equated. The authors showed two of Nairne's three outcomes (better, none), not "worse".
- **Higham (2002)** [b11, b12, d02]. Re-ran Thomson and Tulving with a two-stage test. Free report: weak-cue .26, strong-cue .07, no-cue .08. Forced report: strong-cue .26, weak-cue .28. Cue type by report type F(1,30)=97.22. Monitoring was worse with strong extralist cues and the criterion more conservative, so correct answers were withheld. Only the abstract was re-opened in the cross-check; the figures are from the b-file text.
- **Smith and Vela (2001)** [b18-b21]. Meta-analysis of environmental context-dependent memory. See section 3.
- **Duan, Glass and Raanaas (1998)** [a05, a25]. See sections 3 and 5.
- **Badham, Poirier and colleagues (2016)** [b22-b25, d05]. Extends memory as discrimination to aging. Exp 2 (30 young, 31 older): higher match helped only when the reinstated background was unique. They note that Goh and Lu left the overloaded cue untrained.
- **Craik and Tulving; Raaijmakers and Shiffrin (1981, SAM)** [b06 second-hand; c20 not opened]. Cue overload: success falls as the number of targets per cue rises; recall chance is cue strength to the item relative to its strength to all items.

### 2.5 Context reinstatement as the applied test (1975 to 2026)

- **Godden and Baddeley (1975)** [M]. Land vs underwater divers. **Murre (2021)** [d07] failed to replicate with N=16 divers, four combinations within subject, 4-minute retention: same-context recall was not better.
- **Fernandez and Glenberg (1985)** [cited in b21]. "Changing environmental context does not reliably affect memory." Smith and Vela later showed 7 of the 8 cases used associative processing at input.
- **Hammond et al. (2019)** [d11]. Standing vs walking as context cue: no context effect, walking lowered location memory. Authors point to outshining.
- **Shin et al. (2021)** [a14, a23] and **Koch and Coutanche (2024)** [d08]: VR context effects, needing schema fit.
- **Isarida et al. (2012)** [a13, d09]: the direct human outshining test.
- **Choi et al. (2025)** [a15, a22]: the real-world test with GPS.
- **Ensor et al. (2023)** [d12]: three experiments favour an item-context-integration account over cue overload and suggest context is not a retrieval cue in recognition.
- **Yuvruk (2026)** [d10]: narrative review. Reinstatement seems to help when context is semantically rich, the item unfamiliar, cue load low, encoding interactive, and the retention interval long. Response bias may explain conflicts.

### 2.6 Machine analogues

SAM and IDF are the oldest machine forms of the ratio rule and distinctiveness (c20, c21, both not opened). Section 6 covers LLM studies.

---

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Recognition fails for recallable words (founding case) | Watkins-Tulving Exp 3: recognised and recalled .26, recognised only .06, recalled only .37, neither .31; recognition .32, recall .63 | a01 (second-hand) | [S] original not verified |
| Tulving-Wiseman function | c=.50, 40 data points, 12 experiments, r=.95, SE .028 | a02 | [E] fits pooled data (but see item-level rows) |
| Law holds for a rival-theory test | recognition .732, cued recall .662; given recall .838 observed vs .830 expected; free-recall failures .721 vs .735 | a04 Gardiner 1988 | [E] |
| Law holds for melodies | Exp 1 recognition .76, recall .75, expected .85, observed .81; Exp 2 .52, .74, .64, .59 | a06 | [E] |
| Pooled law hides item effects | with recognition r=.90, with recall r=.06 (CI -.05 to .17); partialled recall r about -.50 to -.56 | a05 Duan 1998 | [E] |
| Subject-wise dependence inflated | subject-wise r=.59 (CI .32-.77) vs item-wise r=-.03 (CI -.31 to .26) | a25 | [E] |
| Recall over recognition not stable | Postman: recall not superior; reverses for low-frequency words (Reder et al.) | a09, a01 | [C] |
| Cue strength beats original match | output strength F(1,92)=94.68; S-S 4.29 vs 4.00 new-cue | a09, b13, b14 | [E] |
| Generic category cue at test still helps | heading at recall only 57.10% vs 26.14% uncued, t(21)=8.23 | a12 | [E] |
| Direction of the pre-existing link | recall: cue-to-target F=51.7 vs 1.1; recognition: target-to-cue F=53.0 vs 1.3 | a07 | [E] with a11 |
| Encoding operation sets which query works | faces 55% vs 25% recognition; features 28.6 vs 19.2 | a08 | [S] (with a11, b16 supports the type) |
| Unique relation raises cued recall | 14.31 vs 5.24 of 24; pair recognition 11.2 vs 9.3 of 12; item recognition 42.0 vs 43.3 of 48 n.s. | b16, b17 | [S] |
| Shared cue slows retrieval | +200-300 ms; Exp 1 N=25 F(2,46)=5.53; Exp 4 N=21 F(2,40)=10.58 | b01-b03 Poirier 2012 | [E] direction; effects in RT near ceiling |
| Match helps when overload equal | low-overload .37 vs .24; high-overload .28 vs .28; interaction F(1,39)=13.89 | b07 Goh and Lu | [E] |
| Intralist beats strong extralist at equal overload | .32 vs .25 vs .09 | b09 | [E] |
| Strong-cue failure is report bias | free: weak .26, strong .07, none .08; forced: strong .26, weak .28 | b11 Higham | [E] |
| Environmental context effect, overall | d=.28 (CI +/-.05), 93 effect sizes; QT=193.22 | b18 Smith and Vela | [E] |
| Reinstatement subtype | d=.23 (n=66); interference reduction d=.68 (n=10); multiple contexts d=.45 (n=7) | b18 | [E] |
| Outshining moderator | associative processing at input d=.13 (n=29) vs nonassociative d=.33 (n=12); chi2=6.67 | b19 | [C] test-type prediction failed (QB=.21) |
| Outshining in a lab recognition test | 1.5 s: d' 1.466 vs 0.738; 4.0 s: 1.901 vs 1.972; nonwords at 4 s 1.126 vs 0.441 (F(1,38)=18.18) | a13 | [S] direct, recognition only |
| Longer delay increases context effect | longest delays (1 day to 1 week) larger | b20 | [C] (d13 shows opposite sign for interference) |
| Context effect needs item-context binding | VR: .32 vs .26, beta .349; useful items beta .521, harmful .177 (p=.359) | a14, a23 | [S] |
| Rare places give the context benefit | d=.44 (rare) vs .15 (common); overall d=.49 (CI .42-.55); 47 analysed | a15, a22 | [S] no power analysis |
| Classic land-underwater not replicated | N=16, same-context not better | d07 | [S] small |
| Cue overload in humans | fan 1/2/4: 91.2/82.4/71.8%, slope .41 (N=112) | b28, d14 | [S] preprint |
| Cue overload in dense retrieval | DPR 94.1/76.3/58.2/44.7% at fan 1/2/4/8, slope .67; HippoRAG slope .44 | b28 | [S] preprint |
| Rare tokens beat learned similarity on entity lookups | BM25 72.0 vs DPR 49.7 top-20 on EntityQuestions; DPR wins on a common pattern (capital: 80.1 vs 64.4) | c04 | [E] |
| Node-specificity weighting | R@2/R@5 57.4/72.9 vs 54.4/67.8 without | c18, c19 | [E] modest |
| Embedding capacity limits and BM25 synonym collapse | LIMIT: under 20% recall@100; BM25 drops over 89% under synonyms; Qwen3 embedding -38.9% | c09, c10 | [E] |
| Literal match is a crutch | Llama 3.3 70B two-hop 57.4/42.7/25.9 (8K/16K/32K) vs 96.3/94.6/87.2 with literal match; GPT-4o 99.3 to 69.7 at 32K; 11 of 13 models at half or less | c01, c02 | [S] (format confounded) |
| Related distractors hurt, random ones do not | gold + one distractor: up to -25%; more: up to -67%; random docs +35% peak (+0.07 absolute, base about 0.2) | b30, b31, d18 | [C] random-doc gain unreplicated |
| Junk text helps a little | Llama3-8B 86.57 to 89.89 (+3.32); Qwen2-7B 86.46 to 88.11 (+1.65) | d19 | [C] |
| Attention dilution by hard distractors | gold-document attention 97% to 21% with 10% hard distractors (128K, 100 docs) | d20 | [S] |
| Write-time distinguishing line, vendor | top-20 failure 5.7% to 3.7% (embeddings), 2.9% (+BM25), 1.9% (+rerank) | b33, c13 | [C] vendor, no filler arm |
| Metadata prefix on repetitive chunks | Context@5 33.33 to 55.00 (prefix), 63.33 dual encoder; bge-m3 26.67 to 61.67 | d16 | [S] |
| Wrong tags worse than none | GT Recall@10 .8066 full, .5708 no session context, .2358 shuffled (GPT-4.1-mini); Qwen3-8B .7217/.4245/.1840 | d15 RaMem | [S] |
| Dual-trace scene at write time | 73.7% vs 53.5% (+20.2 pp, CI 12.1 to 29.3) on 99 questions; single-session 75 vs 75; 156,430 vs 159,211 tokens per teach | a17, a24 | [S] one run per arm |
| Raw plus extracted fact as key | LongMemEval_M round Recall@10 .692 to .784; session .783 to .862; keyphrase alone .392 | d28 | [S] no filler arm |
| Extra-key gain biggest for weakest retriever | round Recall@5: BM25 +.082, Contriever +.023, Stella -.016; session +.049/+.039/+.012 | d29 | [S] retriever confounded |
| Separate index worse than merged key | rank merging below key merging (Table 10) | d29 | [S] |
| Semantic disconnect collapses all methods | LoCoMo-Plus: embedding RAG 15.55, Mem0 15.80, A-Mem 17.20, gpt-4o full context 21.05, gemini-2.5-pro 26.06 | d31 | [S] |
| Hypothetical-question keys | SQuAD top-1 90.03 vs 79.31 naive; HyDE 76.60; relative gain from about 8% to over 20% as contexts grow | d32 | [S] no length control |
| Generated keys must be supported | Doc2Query RR@10 .277; drop 30% least relevant .316; BM25 .185 | d33 | [E] with d15 |
| Cosine beats BM25 on conversational memory | 73.4 vs 57.1; hybrid + reranker 77.2; write strategy 3-8 pts, retrieval 14-23 | d17 | [S] |
| Associative re-cueing | LoCoMo judge 87.14; ablations cost 3.2-4.6% relative; about 1,472 answer tokens | a18, a26 | [S] |
| Position as cue | below closed-book (56.1%) with 20 and 30 docs; start/end best | b32 | [E] with c14, c15 |
| Under-abstention with retrieved text | Claude 3.5 Sonnet 84.1% to 52%; GPT-4o 34.4 to 31.2; Gemini 1.5 Pro 100 to 18.6 | d22 | [C] opposite over-refusal in d34, d35 |
| Over-abstention exists too | Claude-Sonnet-4 .259; Gemini-2.5-Pro .046; GPT-5 .065 | d35 | [C] |

---

## 4. Mechanisms and models

Each model is written so an engineer can implement it on a note store.

### 4.1 The ratio (discrimination) rule

P(retrieve note i | cue q) = sim(q, i) / sum over all notes j of sim(q, j).

- Match to the target (the numerator) raises the chance. Every other note that also fits the cue raises the denominator.
- A cue that fits one note well and nothing else beats a cue that fits it a bit better but also fits twenty others.
- Implementation: for each query, take the top-N similarities, divide the top one by the sum. Call it the **key margin**. A small margin means a crowded key. Use the margin to trigger a second key, a merge, or a disambiguating check.
- Weak points. It does not say how bindings are formed (Badham et al., b05). The softmax in an LLM's attention behaves similarly (d20, 97% to 21% attention on the gold document with 10% hard distractors) but that is an analogy, not a test (K25).

### 4.2 Cue overload and fan

- Retrieval success falls as the number of targets per cue rises (Craik and Tulving; Goh and Lu .28 vs .28 at high overload).
- Implementation: keep a count per key (tag, entity, topic word) of notes carrying it. When a count passes a limit, split the key by adding a second, discriminating word, or merge duplicate notes.
- Machine data: DPR 94.1 to 44.7% from fan 1 to 8 (b28); key-value updates per key, 3 to 400, give a log-linear decline toward 0 (c16, d25); related distractors cost up to 25 to 67% (b30).

### 4.3 Diagnostic value and IDF

- A term that appears in few notes points to them. IDF (Sparck Jones 1972, c21 not opened) and HippoRAG node specificity (1 over the number of passages that contain the entity; c18) are working forms.
- Implementation: weight each key term by log(N / df). Ablation: node specificity gave 72.9 vs 67.8 R@5 (c19).

### 4.4 Report bias and two-stage retrieval (Higham)

- Retrieval, monitoring and reporting are separate. A strong cue can retrieve correctly while monitoring makes the person withhold.
- Implementation: return top-k candidates by force. Verify each candidate against a check. Do not drop candidates on stated confidence. This matches SCHEMA G6 and S4 harvesting.
- For LLMs the problem runs both ways: models under-abstain with retrieved text (d22) and over-refuse when only irrelevant chunks are given (d34, d35). So "forced listing" must be tested, not assumed (K22).

### 4.5 Two access routes and the Tulving-Wiseman function

- If route A finds an item with probability p, route B finds it with p + c(p - p^2) given that A found it, c about .5. So two routes are partly independent.
- Implementation: for a second key route that finds each note with probability p2 on its own, expect P(B | A) = p2 + .5 * (p2 - p2^2) if the human law carried over. This is a planning formula, not tested on LLM stores.
- Item-level caveat: failures concentrate in a minority of items whose cue and target are linked outside the episode (a05). Score per item.

### 4.6 Generate-recognize, revised

- Stage one (relational, broad): produce candidates from a broad key. Stage two (item-specific, distinct detail): confirm each candidate.
- Implementation: retrieve with a broad key, then compare each candidate on a detail that separates it from neighbours. Evidence for the split: a16 (relational vs item-specific encoding). The old strict pipeline failed (a04).

### 4.7 Outshining

- When a good cue is present, context adds little. Model as a max, not a sum: effective cue strength = max(content cue, context cue), plus a small context term.
- Implementation: apply a tag or scene line only to notes whose content key is weak (low margin, short, generic). Measured in people: d=.13 when associative processing was present vs .33 when not; d' gain only at 1.5 s study, not at 4 s (a13).
- In LLM stores the pattern is only suggested: dual-trace gain was zero in single-session lookup (a24), and extra fact keys helped BM25 most, a strong dense retriever least (d29).

### 4.8 Item-bound vs free-floating context

- A context cue works if it is bound to the item: useful items beta .521 vs harmful .177 (a23); rare places d=.44 vs .15 (a15); more dwell time helped only for rare places (a22).
- Implementation: a tag must say something specific about this note and its use. A session id applied to every note is a common place and carries almost nothing. Wrong tags are worse than none (d15).

### 4.9 Direction of the key

- A key built from the item helps queries that arrive as the item or as a link toward the item. A key built from likely questions helps question-shaped queries (a07, d32).
- Implementation: store, for each note, the raw text plus a short likely-question line. Index both in one key (d29: merged key beat separate index).

### 4.10 Transformer keys (white-box)

- In attention, queries are the retrieval context, keys index traces, values hold content (b26). Swapping keys only leaves facts present but unretrievable (accuracy 30-40%). Swapping keys and values gives 100% counterfactual answers (Dinh et al. 2026, seven open models). Not testable on a black-box agent (K14).

---

## 5. What holds up

### 5.1 Replications that held

- Recognition failure of recallable words: 12 experiments and 40 conditions (a02); the generate-recognize rival test (a04); melodies (a06). Established as a general effect (K26).
- Cue overload and the diagnostic account: Goh and Lu (independent lab, recall accuracy, three experiments) and Badham et al. (accuracy, young and older adults). No failure and no preregistered replication found (K23, d27).
- Environmental context effect on average: d=.28 over 93 effect sizes (b18), repeated in real-world GPS data (d=.49, a15) and VR (.32 vs .26, a14).
- Strong cues work with forced report (b11), and Postman's strong output cues worked with forced scoring too (a09), so two methods agree that cue strength counts.

### 5.2 Failures and null results

- **Postman 1975**: recall not superior to recognition; strong extralist cues worked (a09). Not resolved by Postman himself.
- **Godden and Baddeley replication** (Murre 2021, N=16): no land-water advantage (d07).
- **Hammond 2019**: no context effect of activity (d11).
- **Fernandez and Glenberg 1985**: context change does not reliably matter. Smith and Vela explain this: associative processing at input.
- **Ensor 2023**: context is not a retrieval cue in recognition (d12).
- **Outshining test-type prediction**: outshining predicted a recall-recognition difference; none appeared (QB=.21) (b19). Smith and Vela's own note: the recall-recognition comparison used highly associable lists.
- **Choi 2025 and Shin 2021 caveats**: no power analysis; cells of 16 subjects; overall accuracy only about .29.
- **Generate-recognize original form**: failed, because recognition of recalled items was nowhere near 1.00 (a04).

### 5.3 Moderators

| Moderator | Direction | Evidence |
|---|---|---|
| Overload (rivals per cue) | match helps only at low overload | b07, b08 |
| Uniqueness of the shared cue | match helps only if the reinstated cue is unique | b23, d05 |
| Associative processing at input | context effect shrinks (d=.13 vs .33) | b19 |
| Study time and meaningfulness | context effect only at 1.5 s or for nonwords | a13 |
| Item-context fit (schema) | needed in VR | a14, a23, d08 |
| Cue rarity | rare places carry d=.44 vs .15 | a15 |
| Retention interval | longer interval, larger effect | b20; contested by d13 |
| Report bias | hides strong-cue benefit | b11 |
| Scoring: pooled vs item-level | pooled data inflate dependence | a05, a25 |
| Age | older adults get more from match, credited to fewer competitors | d05 |
| Link direction | cue-to-target helps recall; target-to-cue helps recognition | a07 |
| Scoring rule for Postman | hit rates fell when false alarms were subtracted | critique.md |

### 5.4 Interventions that worked and that did not (machine side)

Worked:
- Merged key of raw text plus extracted fact: Recall@10 .692 to .784 (round), .783 to .862 (session) (d28).
- Metadata prefix on repetitive chunks: Context@5 33.33 to 55.00 (d16).
- Contextual retrieval prefix: failure 5.7% to 1.9% with BM25 and rerank (b33, vendor).
- Hypothetical-question keys: SQuAD top-1 79.31 to 90.03 (d32).
- Filtering unsupported generated queries: RR@10 .277 to .316 (d33).
- Dual-trace write-time scene: 53.5% to 73.7% (a17).
- Associative re-cueing: judge 87.14 vs 83.83 (a18).
- Hybrid retrieval over either route alone (c09, c10, d17: hybrid + rerank 77.2).
- Sampling and voting against distractors: at least one of 20 samples correct in 99.7% (c07).
- Focused short context over full context (c14: 306 prompts, about 113k vs about 300 tokens; every model better on focused).

Did not work or hurt:
- Condensed key alone (summary, fact, keyphrase): lost to raw text (d28; keyphrase .392).
- Keyphrase added to a round key: .636 vs .692.
- Separate index merged by rank: worse than key merging (d29).
- Shuffled or wrong tags: Recall@10 .2358 vs .5708 none (d15).
- Unfiltered Doc2Query queries (d33).
- HyDE: 76.60 vs 79.31 naive at about 10 times the query cost (d32).
- "Ignore irrelevant information" and "forget" prompts: limited or inconsistent (c07, c17).
- Refusal tuning raised over-refusal (d34).
- Embedding search alone for chaining evidence: 6% vs 44% (d23).
- Fine-tuning for one question pattern (c05).

### 5.5 Contradictions that stay open

- Match: "helps at equal overload" (Goh and Lu) vs "diagnostic value, not match" (Poirier). Verdict: match alone is not enough [E]; "match is a myth" is [C].
- Higham vs Postman: both say strong output cues work; they differ on cause (report bias vs generate-recognize and novelty).
- Gardiner 1988 (no extra dependence) vs Duan 1998 (dependence is item-specific): both can be true, since the law fits pooled data and failures sit in few items.
- Random documents: +35% (Cuconasu) while related distractors cost 25 to 67%. Unexplained. No 2025 to 2026 replication found (K08).

---

## 6. Language models

There is no direct LLM test of the central critique claim (Nairne-style distinctiveness vs match, or outshining) that crosses distinctiveness with a strong-key condition at equal tokens (K18, K42). Everything below is indirect. The scale of each effect is given so it can be weighed.

### 6.1 Cue overload and fan in models

- **Dense retrieval** (Guo, Wu and Yiu 2026, b28, d14, preprint, arXiv id 2606.28327 stamped 9 May 2026): humans N=112 recognised 91.2/82.4/71.8% at fan 1/2/4 (slope .41, d=1.12). DPR 94.1/76.3/58.2/44.7% at fan 1/2/4/8 (slope .67), ColBERTv2 .53, HippoRAG .44. System by fan beta=-.12. Serial position: DPR 89.2/61.4/68.3 at positions 1/10/20. Not preregistered; human task is recognition, RAG task top-1 retrieval; the authors say the mechanism is "a research programme rather than a finding". Single source (K17).
- **Fan in uncertainty** (Roberts et al. 2024, d26): appears in token-probability uncertainty, in some models only (Mistral, SOLAR).
- **Key-value interference** (Wang and Sun 2025, c16, d25): log-linear decline toward 0 with 3 to 400 updates per key; at 400 updates the M group fell to 0% with one exception; larger models decline more slowly; errors shift from the update just before the target to far upstream to never-shown values. Prompts to forget did not change the trend (c17).
- **RAG prompts with related distractors** (Cuconasu 2024, b30): gold only to one distractor, up to -0.24 (-25%); more distractors up to -0.38 (-67%). Llama2 with 18 distractors: 0.37, 0.23, 0.17 by gold position. Closed-book baselines 0.11, 0.12, 0.05, 0.11. Models were 2024 small open models.
- **Irrelevant sentences** (Shi 2023, c06, c07): at most 18% of baseline-solved problems solved under every distractor type; lexical overlap raises harm. Fewer than 30% of base problems solved consistently. 2022 models.
- **Hard distractors** (Gao 2026, d20): attention on gold 97% to 21% with 10% hard distractors; Llama-3.1-8B, Qwen2.5-7B, Qwen3-Next-80B; 200 examples per setting. Filtering gains come mostly from shorter context.
- **Distracting effect** (Amiraz 2025, d21): per-passage effect stable across LLMs; stronger-retriever passages distract more; fine-tuning on hard distractors up to +7.5%.
- **Long-context models** (Chroma 2025, c14, c15; RULER c08): lower needle-question similarity makes performance fall faster; 18 models, 194,480 calls; needles that blend into the haystack are harder; shuffled haystacks beat coherent ones in all 18 models. RULER: only about half of models claiming 32K or more keep satisfactory performance at 32K.
- **Position** (Liu 2023, b32): middle position worse; 20 or 30 documents fell below closed-book 56.1%. 2023 models.

### 6.2 Literal match vs latent link

- **NoLiMa** (Modarressi 2025, c01-c03): 13 LLMs claiming 128K+ context. 11 of 13 reach half or less of their short-context score at 32K. GPT-4o 99.3% to 69.7%. Llama 3.1 70B 94.3% to 42.7%, effective length 2K (vs 32K on RULER). For Llama 3.3 70B at 8K/16K/32K: direct 98.3/98.5/98.5; one-hop without literal match 84.1/73.2/56.2; one-hop with literal match 98.7/97.4/93.1; two-hop without 57.4/42.7/25.9; two-hop with 96.3/94.6/87.2. The multiple-choice format also shrinks the search, so the gain mixes match and format. Literal overlap with an irrelevant passage also lowers accuracy on the lexically distant needle.
- **LoCoMo-Plus** (Li 2026, d31): when the later trigger shares no wording with the stored cue, all methods fall to 12 to 26 percent: RAG text-embedding-large 45.32 to 15.55; Mem0 57.24 to 15.80; SeCom 57.53 to 14.90; A-Mem 59.64 to 17.20; gpt-4o full context 62.99 to 21.05; gemini-2.5-pro 71.78 to 26.06; gpt-5-nano 54.96 to 14.84. The gap column mixes metrics (string metrics vs a constraint judge).
- **Tool-based search** (LongHarness d23; LongMemEval-V2 d24): best harness 68% macro; embedding-search ReAct 6% vs direct inference 44% on one task; coding agent storing trajectories as files 72.5% vs 48.5% best RAG (abstract only). Neither varies word overlap.

### 6.3 Distinctive keys for retrieval

- **Rare entity tokens** (Sciavolino 2021, c04, c05): BM25 72.0 vs DPR 49.7 top-20; DPR trained on four datasets 56.7%; REALM 19.6%; gap up to 60 points. "Where was [E] born?": BM25 ahead by 49.9. Fine-tuning only the passage encoder: 72.8/84.2/78.0 vs BM25 75.3/85.0/72.6 on three templates. These are pre-LLM retrievers.
- **Atomic propositions** (Dense X, c12): +25% relative Recall@5 on EntityQuestions with weak retrievers; downstream QA +2.7 to +2.8 EM@500; gain shrinks as entity frequency rises.
- **HippoRAG** (c18, c19): node specificity ablation 57.4/72.9 vs 54.4/67.8.
- **Embedding limits** (Weller 2026, c09, c10): under 20% recall@100 on LIMIT; fine-tuning lifted recall@10 only to at most 2.8; BM25 drops over 89% under synonyms.
- **BEIR** (c11): BM25 a strong zero-shot baseline; 18 datasets, 10 systems.
- **Conversational memory** (Yuan 2026, d17): 1,540 questions, k=5, GPT-5-mini reader. Cosine 73.4, BM25 57.1, hybrid pool + GPT-5.2 rerank 77.2. Raw chunks: cosine 77.9, BM25 59.2, hybrid 81.1. Retrieval precision vs accuracy r=0.98. Write strategy spread 3 to 8 points, retrieval spread 14 to 23.

### 6.4 Write-time distinguishing context

- **Anthropic contextual retrieval** (b33, c13, vendor blog): 50 to 100 token context. Failure 5.7% to 3.7% (-35%) with embeddings, 2.9% (-49%) with BM25, 1.9% (-67%) with rerank. About $1.02 per million document tokens one-time. No filler arm.
- **Yousuf 2026** (d16): Context@5 33.33 plain, 55.00 prefix, 48.33 suffix, 63.33 unified dual encoder; bge-m3 26.67 to 61.67; average rank 21.61 to 10.22. Dropping company and year hurts most, section titles little. 60 questions per type; repetitive corpus.
- **RaMem** (Yang 2026, d15): session, time and participant context stored with each memory. Temporal subset GPT-4.1-mini GT Recall@10: 0.8066 full, 0.5708 without session context, 0.2358 shuffled. Qwen3-8B: 0.7217, 0.4245, 0.1840. All questions GPT-4.1-mini: F1 0.5291 to 0.5004 under shuffle; GT R@10 0.7550 to 0.6744. The method has several parts; no filler arm; no removal of a strong semantic key.
- **Dual-trace** (Stern and Nadel 2026, a17, a24): Claude Sonnet 4.6 under Letta; 99 questions: 73.7% vs 53.5% (+20.2 pp, CI +12.1 to +29.3, p<0.0001). Temporal 25% to 65% (+40, p=.002); knowledge update 55% to 80% (+25, p=.003); multi-session 20% to 50% (+30, p=.001); single-session 75% vs 75% (CI -15 to +15, p=.657, 0 discordant questions). Of 22 questions where the scene mattered: 9 temporal, 6 multi-session, 5 knowledge update. Tokens per teach session 156,430 vs 159,211; per recall query 244,385 vs 252,750. One run per arm, 20 questions per category, GPT-4o judge, no same-length filler arm, and the authors state the write-versus-read ablation was not run.
- **LongMemEval key design** (Wu 2025, d28, d29): Table 3 (LongMemEval_M). Value=round, Recall@10: K=V .692; fact .654; keyphrase .392; V+fact .784; V+keyphrase .636. Value=session: K=V .783; summary .648; fact .814; keyphrase .576; V+summary .749; V+fact .862; V+keyphrase .768. End-to-end GPT-4o round: .670 vs .720 for V+fact. Session K=fact beat K=V on recall (.814 vs .783) but GPT-4o accuracy fell (.512 vs .676). Table 9 (Recall@5): session BM25 .634 to .683, Contriever .723 to .762, Stella .720 to .732; round BM25 .472 to .554, Contriever .589 to .612, Stella .660 to .644. Summary expansion with Stella -.031. Key merging beat rank merging (Table 10). One run per cell; differences of .01 to .02 are noise.
- **History length** (d30): oracle sessions vs full 115k-token history: GPT-4o .870 to .606 (30.3% drop), Llama 3.1 70B .710 to .454 (36.1%), Llama 3.1 8B .660 to .342 (48.1%). Date-tag time-aware indexing: temporal subset round Recall@10 .550 to .722 with GPT-4o expansion, only .570 with Llama 3.1 8B; session .721 to .797.
- **QuOTE** (d32): hypothetical-question keys. SQuAD top-1/top-5 naive 79.31/95.88, HyDE 76.60/92.63, QuOTE 90.03/98.48 (index 10.36 s vs 170.32 s). Natural Questions 32.92/89.23, 33.23/90.46, 38.00/92.15. MultiHop-RAG full match at 5/20 docs 7.00/23.00, 6.00/23.50, 8.00/29.00. Relative gain on SQuAD about 8% to over 20% with many contexts; NQ 6 to 18.3%. Diminishing beyond 10 to 15 questions per chunk.
- **Doc2Query-- (d33)**: BM25 .185; Doc2Query (n=40) .277; ELECTRA filter (drop 30%) .316; MonoT5 (40%) .308; TCT (50%) .287; TREC DL'19 nDCG@10 .626 to .667; index 1.17 GB to 0.89 GB; response 30 to 23 ms.

### 6.5 Re-cueing and query rewriting

- **RippleMem** (Ji 2026, a18, a26): first-recalled units become new cues. LoCoMo F1 52.49, BLEU-1 44.05, judge 87.14 (relative gains: 3.98% F1 and 3.62% BLEU-1 over SimpleMem, 3.95% judge over RF-Mem, up to 11.87% on LongMemEval-S); about 1,471.93 answer tokens per question; ablation removal costs 3.2 to 4.6 percent relative. GPT-4.1-mini judge.
- **MemoCue** (Zhao 2025, a19): query rewriting into a cue-rich form; 5,805 samples; 17.74% LLM-judged gain. Aimed at human recall; not re-checked.

### 6.6 Withholding and abstention

- **Sufficient context** (Joren 2025, d22): abstention on insufficient context without vs with RAG: Claude 3.5 Sonnet 84.1% to 52%; GPT-4o 34.4% to 31.2%; Gemini 1.5 Pro 100% to 18.6%. Over 35% correct with insufficient context on HotpotQA. Selective generation raises the correct fraction among answered by 2 to 10%.
- **Opposite risk**: with irrelevant chunks only, 7 to 8B models over-refuse (d34, Table 3 vanilla .579/.191/.759/.738); LIT-RAGBench over-abstention Claude-Sonnet-4 .259 avg, Llama-3.1-8B .213, Llama-3.3-70B .157, Gemma-3-27B .120, GPT-4.1 .083, GPT-5 .065, Gemini-2.5-Pro .046, o3 .046, GPT-4.1 mini .028 (114 questions, d35).
- No source tests Higham's forced-listing recovery on an agent's candidates (critique gap 5).

### 6.7 Internal mechanism

- **Dinh 2026** (b26, b27): seven open models (Llama 2-7b and 13b, Llama 3.1-8b, Olmo 2-13b, Qwen 2.5-14b, Phi-4, GPT-NeoX-20b). Swapping V gave counterfactual answers (50% in Olmo 2 to 90% in Qwen 2.5). Swapping K and V: 100%. Swapping K only: factual accuracy about 30 to 40%. Keyword-bearing neurons: perturbing them lowers verbatim recall of memorised books.

### 6.8 Net reading for LLMs

- Match matters: removing literal overlap collapses long-context recall (NoLiMa) and cross-wording memory (LoCoMo-Plus).
- Distinctiveness matters: crowded keys lose (fan, PI-LLM, hard distractors), rare tokens help (EntityQuestions, HippoRAG), distinguishing prefixes help on repetitive text (d16, b33).
- Both are needed, which is the "numerator and denominator" picture. A tag alone is not enough (d28), a wrong tag is worse than none (d15), an unsupported tag hurts (d33).
- Whether a distinguishing line beats a same-length neutral line is not known anywhere (K13, K42).
- Most machine studies use 2022 to 2024 models; the 2026 agent-memory studies are mostly single-run, single-lab preprints.

---

## 7. What our agent should take

Schema part names: G (guardrail), S (state), O (operator), memory (SCHEMA section 5). The schema has no key-design rule yet.

### Add now (established [E])

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Score a retrieval key by how few notes it fits, not only by how well it fits the target. Keep a rival count per key and flag crowded keys (key margin small). | memory | [E] | K01, K02, K07; b01-b03, b07-b09, a09, b28, c16, b30 |
| A2 | Keep an exact-term route (names, ids, rare words) beside the semantic route. Do not rely on either alone. | memory | [E] | K10, K11, K12; c04, c05, c09, c10, c18, c19 |
| A3 | Keep the original wording of a note beside any summary or fact. A condensed key never replaces the raw text (the schema already keeps original wording in S1; extend that to stored notes). The finer claim "raw plus fact beats raw" is [S] (T7). | memory | [E] direction | K30, K37; a08, a11, b16, d28 |
| A4 | Build keys in the direction the query will arrive from: include item-shaped and question-shaped wording. Design rule only; the best form is a test item (T6). | memory | [E] direction | K29; a07, a11 |
| A5 | Never gate candidate retrieval on a stated confidence. Return a forced top-k and filter by checks. Reinforces G6 and S4 harvesting. | G6/S4 | [E] for humans, [C] for LLMs | K03, K22; b11, b12, d22, d34, d35 |
| A6 | A tag or context line is allowed only if it is specific to the note. A generic line that is the same for many notes is not a key. Generated keys must be checked against the note (unsupported ones dropped). | memory/G | [E] | K32, K41; a15, a22, a23, d15, d33 |
| A7 | Put the retrieved note in a short focused context, not a long one. | S/memory | [E] | K15; b32, c14, c15, d17 |
| A8 | When evaluating memory design, score per item and randomise probe order. Averages hide where keys fail. | harness | [E] (K27); [S] (K36 order) | K27, K36; a05, a25, a03 |
| A9 | Guard: do not pad context with random documents, and do not depend on "ignore irrelevant text" instructions. Pre-filter instead. | G | [C] but cheap | K08, K16; b31, d18, d19, c07, c17 |

### Test first ([S] or [C])

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | A write-time distinguishing line (50 to 100 tokens) per note vs a same-length neutral filler line | memory/O | [C] | K13, K33; b33, c13, d16, d15, a17, a24, d28 |
| T2 | Apply the line only to notes with a weak content key (outshining) | memory | [C] | K05, K18, K38; b19, a13, d09, d29, a24 |
| T3 | Dual-trace scene beside each fact for temporal, update and multi-session recall; skip for single-session lookup | memory/O | [S] | K33; a17, a24 |
| T4 | Ratio score (target similarity over summed rival similarity) vs cosine vs IDF-weighted cosine | memory | [S] | K20, K25; b05, d17, d20 |
| T5 | Intent-level second key (how someone would ask) to survive wording shifts | memory/O | [S] | K09, K39; c02, d31 |
| T6 | Question-shaped vs item-shaped vs both keys | memory/O | [S] | K29, K40; a07, d32, d28 |
| T7 | Raw plus extracted-fact key vs raw alone vs fact alone | memory | [S] | K37; d28, d29 |
| T8 | Tag validation at write time (wrong tags cost more than none) | memory/G | [S] | K19, K41; d15, d33 |
| T9 | Rival-count rekey/merge rule when a key passes N notes | memory/G | [S] for the remedy; [E] for the loss | K07; c16, b28, b30 |
| T10 | Associative second hop: use the first hit as a new cue | O/memory | [S] | K34; a18, a26 |
| T11 | Forced candidate listing vs confidence gate on the agent's own store | G6/S4 | [C] | K22, K03; d22, d34, d35, b11 |
| T12 | Probe each note with a copy-style probe and an original-context cue; count one-route-only finds | memory | [S] | K26, K27; a01, a05, a06 |
| T13 | Tag benefit by number of intervening writes | memory | [C] | K06; b20, d13, d30 |
| T14 | Broad key to produce candidates plus a distinct-detail check | memory | [C] | K35; a16, a04 |

---

## 8. Concrete tests on our bench

Common design: a store built from the agent's own notes (or a fixed synthetic note set with known gold). Every pair of arms uses equal tokens in the key, the stored text and the prompt (a filler arm pads to the same length). Report hit rate at 5 and 10 plus end answer accuracy. Score per item (A8). 100+ queries per condition. Preregister the "add if" rule (UNKNOWNS.md).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 filler control | notes on similar topics (repetitive structure), query asks for one | plain; plain + context line; plain + same-length neutral filler; plain + shuffled line | hit@5, answer accuracy | context line beats filler by about 4+ points; filler within 2 points of plain; shuffled worse than plain (d15) |
| T2 outshining | notes with strong content key (specific term) vs weak (generic wording); tag yes/no | 2x2 | hit@5, interaction | tag gain mostly where key is weak (d29: +.082 BM25 vs -.016 Stella; human d .13 vs .33) |
| T3 dual-trace | multi-session, update and temporal questions vs single-session lookup | fact only; fact + scene; fact + same-length neutral | accuracy by category, 40+ questions per category | gain in temporal, update, multi-session; none in single-session (a24) |
| T4 scoring rule | queries on crowded vs unique keys | cosine; BM25; ratio score; IDF-cosine; hybrid | hit@5 by crowded/unique | ratio helps crowded keys, equal on unique |
| T5 intent key | verbatim vs paraphrase vs no-word-overlap queries | plain; plain + likely-query line; plain + same-length filler | hit@5; verbatim-minus-paraphrase gap | gap shrinks with intent line (baselines in d31 are 12 to 26%) |
| T6 key shape | question-form vs task-need-form queries | raw; raw + summary; raw + question line; all, key length matched | hit@5 | question key helps question queries, summary does not (d28, d32) |
| T7 key composition | session-level and round-level notes | raw; fact only; raw + fact; raw + neutral | Recall@10, accuracy | raw + fact above raw by about 5 to 9 points; fact alone below on accuracy |
| T8 tag validation | store with 0, 10, 30% wrong tags | clean; none; wrong 10%; wrong 30%; stale | Recall@10 | wrong tags cost more than none (d15: .2358 vs .5708 at 100% shuffle) |
| T9 rival count | keys carried by 1, 4, 16 notes | plain; rekey; merge duplicates | hit@5 slope vs log rivals | slope falls by a third or more with rekey |
| T10 two hop | questions where a second fact is linked to the first hit | single hop; re-cue from first hit | accuracy at same answer tokens | gain of several points (a18: 87.14 vs 83.83 judge) |
| T11 gate vs list | top-10 retrieval with a gold candidate present or absent | confidence gate; forced listing then check; no filter | correct candidates withheld; final accuracy; false-answer rate when gold absent | listing recovers withheld candidates; watch false answers when gold absent (d22 shows over-answering) |
| T12 copy vs cue | each note probed by restated copy and by original-context cue | copy; cue; both | one-route-only share per item | sizeable one-route-only share, concentrated in notes with outside links (a05) |
| T13 delay | tag on/off at 0, 50, 500 intervening writes | tag vs none | tag gain by gap | sign unknown; human delay effect positive (b20) |
| T14 two-stage | candidate generation by broad key + detail check | broad only; distinct only; broad then check | accuracy | broad-then-check best on crowded stores (a16) |

---

## 9. What does not transfer, and why

- **Recognition vs recall labels.** Most founding studies separate recognition from recall; an agent's retrieval step has no recognition test of its own. The Tulving-Wiseman function describes two human access routes; no LLM study shows the same c=.5 independence (K26 is human-only).
- **Reaction time at ceiling accuracy.** Poirier's effects are about 200 to 300 ms in trained, near-perfect conditions with N 21 to 25. An agent has no RT. Only a count effect (hit rate) can be borrowed.
- **Environmental context (rooms, GPS, VR).** These are physical states that cue reinstatement. A session id in a text note is a different thing. The VR and GPS evidence says context works only when item-bound, rare and useful, which argues against generic session tags (a15, a23).
- **Time-scale of forgetting.** Human context effects grow over hours or days (b20; contested by d13). A store does not forget; its keys do not fade. Delay in an agent store is intervening writes, not time (K06).
- **Report bias as a social criterion.** Humans withhold because errors were penalised (Higham's point system). An LLM gate is driven by training and prompt. LLMs both under-abstain and over-refuse (section 6.6), so Higham's remedy cannot be copied blind.
- **Dual-trace as imagery.** In people it is a mental image. In Stern and Nadel it is a text scene. Whether it works because it is a scene, a distinct line or extra text is unknown (K33).
- **Transformer key swaps.** They tell us attention keys index traces, but a black-box agent cannot manipulate K and V (K14).
- **Random-document padding.** The only machine evidence is 2024 small models with a weak base. It should not be copied (K08).
- **Age results.** Older adults' larger match benefit is a human feature (d05).
- **Fan slope comparison.** Preprint with an id/date oddity, mixed paradigms (K17).
- **Founding percentages.** Do not cite the original 1970 and 1973 numbers; they were not verified (K24).

---

## 10. Open questions

1. Does a write-time distinguishing line beat a same-length neutral filler, and does the gain exist only when the plain key is weak? (critique gap 1; nobody has run the crossed design.)
2. How much of Stern and Nadel's +20.2 pp is from the write-time scene, the read-time scene, or extra text? (gap 2; ablation not run; only 20 questions per category.)
3. Which scoring rule is best on agent memory: cosine, BM25, IDF, or the Nairne ratio? (gap 3; only retriever comparisons exist.)
4. How often does a copy probe miss facts that an original-context cue finds, and are they notes with outside-episode links? (gap 4; LoCoMo-Plus gives only the aggregate collapse.)
5. How many correct candidates does confidence gating withhold in an agent, and does forced listing recover them? (gap 5; models both under-abstain and over-refuse.)
6. Are question-shaped keys better than summaries on non-extractive queries, with length controlled? (gap 6.)
7. Does tag benefit grow with intervening writes? (gap 7; only history-length loss, 30.3% to 48.1%.)
8. Why did random documents raise RAG accuracy in 2024, and does it hold on 2025 to 2026 models? (gap 8.)
9. Has Poirier 2012 been replicated in accuracy, preregistered, outside its network, including failures? None found (gap 9).
10. What are the real figures in Tulving and Thomson 1973 and Watkins and Tulving 1975? (gap 10; paywalled.)
11. Is the Guo 2026 human slope (.41) replicable, and is the preprint sound? (id 2606 stamped 9 May 2026; no data or code link.)
12. Does the generate-recognize split (broad key for candidates, detail for confirmation) help agents at equal tokens? (K35.)
13. Is the outshining pattern across retrievers (d29) due to key strength or retriever family? (confounded.)
14. Do Terranova 2025 (arXiv 2510.23730, memory types in long-context QA) and Pink 2026 (arXiv 2607.22575, a temporal-context reinstatement head) add direct evidence? Both were only skimmed.

---

## 11. Sources

[V] = opened and read (full text unless noted). [M] = snippet, abstract, or second-hand only.

**Founding and human studies**
- [M] Thomson and Tulving (1970) Associative encoding and retrieval. (paywalled; not retrieved; no URL verified)
- [M] Tulving and Thomson (1973) Encoding specificity and retrieval processes in episodic memory. https://doi.org/10.1037/h0020071 (paywalled; d03)
- [M] Watkins and Tulving (1975) Episodic memory: when recognition fails. (not located; d04; figures taken from a01)
- [V] Tulving and Wiseman (1975) Relation between recognition and recognition failure of recallable words. https://link.springer.com/content/pdf/10.3758%2FBF03333153.pdf (a01, a02, a03)
- [V] Postman (1975) Tests of the generality of the principle of encoding specificity. https://doi.org/10.3758/BF03198232 (a09, a10, b13-b15)
- [V] Fisher (1979) Retrieval operations in cued recall and recognition. https://link.springer.com/content/pdf/10.3758/BF03197542.pdf
- [V] Ley (1977) Encoding specificity and unidirectional associates. https://link.springer.com/content/pdf/10.3758/BF03197395.pdf
- [V] Epstein, Dupree and Gronikowski (1979). https://link.springer.com/content/pdf/10.3758/BF03329437.pdf
- [V] Wells and Hryciw (1984) Memory for faces. https://link.springer.com/content/pdf/10.3758/BF03198293.pdf
- [V] Stein (1977) Cue-target uniqueness. https://doi.org/10.3758/BF03197577
- [V] Gardiner (1988) Recognition failures and free-recall failures. https://link.springer.com/content/pdf/10.3758/BF03214225.pdf
- [V] Gardiner et al. (1990) Tulving-Wiseman law and music. https://link.springer.com/content/pdf/10.3758/BF03197105.pdf
- [V] Duan, Glass and Raanaas (1998) Item-specific effects in recognition failure. https://link.springer.com/content/pdf/10.3758/BF03211390.pdf
- [V] Hanley (1984) Dual processes in recognition and recognition failure. https://link.springer.com/content/pdf/10.3758/BF03213346.pdf (d36)
- [V] Guynn et al. (2014) Relational and item-specific influences on generate-recognize. https://link.springer.com/content/pdf/10.3758/s13421-013-0341-6.pdf
- [M] Nairne (2002) The myth of the encoding-retrieval match. https://pubmed.ncbi.nlm.nih.gov/12396651/ (abstract only)
- [V] Poirier et al. (2012) Memory as discrimination. https://openaccess.city.ac.uk/id/eprint/2519/ (abstract also at https://pubmed.ncbi.nlm.nih.gov/21823814/); figures from the b-file, not re-opened in the cross-check
- [V] Goh and Lu (2012) Testing the myth of the encoding-retrieval match. https://doi.org/10.3758/s13421-011-0133-9 (abstract at https://pubmed.ncbi.nlm.nih.gov/21830162/); figures from the b-file, not re-opened
- [M] Higham (2002) Strong cues are not necessarily weak. https://doi.org/10.3758/BF03195266 and https://pubmed.ncbi.nlm.nih.gov/11958356/ (abstract re-opened; figures from the b-file)
- [V] Badham et al. (2016) Aging and memory as discrimination. https://openaccess.city.ac.uk/id/eprint/15433/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC5104237/
- [V] Smith and Vela (2001) Environmental context-dependent memory. https://doi.org/10.3758/BF03196157
- [V] Isarida, Isarida and Sakai (2012). https://link.springer.com/content/pdf/10.3758/s13421-012-0234-0.pdf
- [V] Shin et al. (2021) VR context. https://link.springer.com/content/pdf/10.3758/s13423-020-01835-3.pdf
- [V] Choi et al. (2025) Context-dependent memory in the real world. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1489039/pdf
- [M] Murre (2021) Godden and Baddeley replication. https://pubmed.ncbi.nlm.nih.gov/34760281/
- [M] Koch and Coutanche (2024). https://pubmed.ncbi.nlm.nih.gov/38429590/
- [M] Hammond et al. (2019). https://pubmed.ncbi.nlm.nih.gov/30076514/
- [M] Ensor et al. (2023). https://pubmed.ncbi.nlm.nih.gov/36227292/
- [M] Antony and Bennion (2023). https://pubmed.ncbi.nlm.nih.gov/36548092/
- [M] Yuvruk (2026) review. https://pubmed.ncbi.nlm.nih.gov/42550362/
- [M] Raaijmakers and Shiffrin (1981) SAM. https://doi.org/10.1037/0033-295X.88.2.93 (not opened)
- [M] Sparck Jones (1972) IDF. https://doi.org/10.1108/eb026526 (not opened)

**Language-model and retrieval studies**
- [V] Stern and Nadel (2026) Dual-trace encoding. https://arxiv.org/pdf/2604.12948
- [V] Ji et al. (2026) RippleMem. https://arxiv.org/pdf/2608.13334
- [V] Zhao et al. (2025) MemoCue. https://arxiv.org/pdf/2507.23633 (LLM-judged gain not re-checked)
- [V] Dinh et al. (2026) Memory retrieval in transformers. https://arxiv.org/abs/2601.20282
- [V] Guo, Wu and Yiu (2026) The interference gap. https://arxiv.org/abs/2606.28327
- [V] Cuconasu et al. (2024) The power of noise. https://arxiv.org/abs/2401.14887
- [V] Liu et al. (2023) Lost in the middle. https://arxiv.org/abs/2307.03172
- [V] Anthropic (2024) Contextual retrieval. https://www.anthropic.com/news/contextual-retrieval
- [V] Modarressi et al. (2025) NoLiMa. https://arxiv.org/abs/2502.05167
- [V] Sciavolino et al. (2021) EntityQuestions. https://arxiv.org/abs/2109.08535
- [V] Shi et al. (2023) Easily distracted. https://arxiv.org/abs/2302.00093
- [V] Hsieh et al. (2024) RULER. https://arxiv.org/abs/2404.06654
- [V] Weller et al. (2026) Limits of embedding retrieval. https://arxiv.org/abs/2508.21038
- [V] Thakur et al. (2021) BEIR. https://arxiv.org/abs/2104.08663
- [V] Chen et al. (2024) Dense X Retrieval. https://arxiv.org/abs/2312.06648
- [V] Chroma (2025) Context rot. https://www.trychroma.com/research/context-rot
- [V] Wang and Sun (2025) Unable to forget (PI-LLM). https://arxiv.org/abs/2506.08184
- [V] Gutierrez et al. (2024) HippoRAG. https://arxiv.org/abs/2405.14831
- [V] Yang et al. (2026) RaMem. https://arxiv.org/abs/2606.22844
- [V] Yousuf et al. (2026) Metadata for RAG. https://arxiv.org/abs/2601.11863
- [V] Yuan, Su and Yao (2026) Retrieval vs utilization. https://arxiv.org/abs/2603.02473
- [V] Wu et al. (2025) Pandora's box or Aladdin's lamp. https://arxiv.org/abs/2408.13533
- [V] Gao, Chen and Huang (2026) The first drop of ink. https://arxiv.org/abs/2605.10828
- [V] Amiraz et al. (2025) The distracting effect. https://arxiv.org/abs/2505.06914
- [V] Joren et al. (2025) Sufficient context. https://arxiv.org/abs/2411.06037
- [V] Pham et al. (2026) LongHarness Bench. https://arxiv.org/abs/2609.38137
- [M] Wu et al. (2026) LongMemEval-V2 (abstract and header only). https://arxiv.org/abs/2605.12493
- [V] Roberts et al. (2024) Fan effect in LLM recall. https://arxiv.org/abs/2407.06349
- [V] Wu et al. (2025) LongMemEval. https://arxiv.org/abs/2410.10813
- [V] Li et al. (2026) Locomo-Plus. https://arxiv.org/abs/2602.10715
- [V] Neeser et al. (2025) QuOTE. https://arxiv.org/abs/2502.10976
- [V] Gospodinov, MacAvaney and Macdonald (2023) Doc2Query--. https://arxiv.org/abs/2301.03266
- [V] Zhou, Huang et al. (2025) Do retrieval augmented models know when they do not know? https://arxiv.org/abs/2509.01476
- [V] Itai et al. (2026) LIT-RAGBench. https://arxiv.org/abs/2603.06198
- [M] Terranova et al. (2025), arXiv 2510.23730, and Pink et al. (2026), arXiv 2607.22575 (skimmed, not used as evidence)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 16 established claims: 14 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A06.02-K27** (reworded: the sources support less). Numbers match Duan et al., but 'is an aggregate artefact' states one paper's conclusion (Exp 1 of 48 pairs plus a database meta-analysis) as settled; the .59 vs -.03 is the P(RN)-P(RC) correlation in subject-wise vs item-wise tabulation, offered as an explanation for differing results rather than proof of inflation. Corrected claim: Duan, Glass and Raanaas (1998) argue the clean Tulving-Wiseman function (c=.50, r=.95) results from collapsing across items: in their data recognition failure concentrated in items whose cue and target are related outside the study episode, and the P(RN)-P(RC) correlation differed between subject-wise (r=.59) and item-wise (r=-.03) tabulations; this rests on one paper (a database meta-analysis and two experiments) and has not been independently replicated in the sources reviewed.
- **A06.02-K41** (number corrected). Gospodinov et al. say p=0.3 keeps only the top 30 percent of generated queries (drops 70 percent), not drops 30; unfiltered Doc2Query beat BM25 (.277 vs .185), so it hurt only relative to filtered; the index shrank 24 percent at n=40 (1.17 to 0.89 GB) and 33 percent only at n=80. Corrected claim: Generated index keys must be supported by the item: Doc2Query's hallucinated queries limit it, and keeping only the 30 percent of generated queries that an ELECTRA relevance filter scores highest raised MS MARCO dev RR@10 from .277 to .316 (n=40; unfiltered Doc2Query still beat plain BM25 at .185) while shrinking the index by 24 percent at n=40 and about a third at n=80.
