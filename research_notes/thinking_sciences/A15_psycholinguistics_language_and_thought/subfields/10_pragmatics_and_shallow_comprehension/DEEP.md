# Pragmatics and shallow comprehension: deep document

*Subfield A15.10. Written 2026-11-10 from evidence_a-d.jsonl (ids a01-a25, b01-b28, c01-c28, d01-d16), claims.jsonl (K01-K37) and critique.md. Evidence ids are cited in brackets. Status tags: [E] established, [S] single-source, [C] contested. Overlap with `A15/subfields/04_question_wording_and_presupposition` (Moses and false premises in survey questions) is only noted, not repeated.*

## 1. What it is

Two linked ideas.

**Pragmatics** is the study of how a listener gets from what was said to what was meant. "Did you leave fingerprints?" "I wore gloves." means no. The words do not say no. The listener adds it by assuming the speaker is cooperative and relevant (Grice 1975 [a14, not opened]).

**Good-enough (shallow) comprehension** is the finding that people often build a meaning only as detailed as the task needs. They use heuristics (the first noun is the doer; the sentence is probably sensible) and skip a full parse. Sometimes the result is wrong in a way the person would catch if they looked. The classic traps:

- **Garden-path sentences.** "While the man hunted the deer ran into the woods." Many people still say the man hunted the deer after reading the whole sentence [a01].
- **Non-canonical sentences.** "The dog was bitten by the man" is often read as the dog biting the man [a06, b26; second-hand].
- **Moses illusion.** "How many animals of each kind did Moses take on the ark?" Most people answer "two" and do not notice it was Noah [a07, b17].
- **Implicature.** The speaker means more than they say.
- **Ambiguity.** One sentence, several readings; the reader silently picks one.
- **False presupposition.** The question assumes something false, and the answerer accepts it.

Why this matters for our agent. In the schema this is state S1 (UNDERSTAND): "restate the task in its own words; say what makes an answer correct." A wrong reading at S1 makes every later state work on the wrong problem. Code at S4 can check an answer against a check, but a check built from a misread task passes the wrong thing. So S1 is where a cheap early fix pays most, if one exists. The evidence below says: language models share the human failure on some traps, are worse than humans on others, and the few tested fixes are weak or carry costs.

## 2. History and theories in depth

**Grice (1975).** The cooperative principle with four maxims: quantity (be as informative as needed), quality (be truthful), relation (be relevant), manner (be clear). Listeners derive implicatures from apparent violations. "Some of the students passed" implicates "not all." Not quantitative; it is the base of every later implicature test [a14].

**Default vs context accounts.** Neo-Griceans said scalar implicature (some means not all) is a default made fast and cancelled if needed. Relevance theory said it is built on demand. Degen and Tanenhaus (2015) offered a constraint-based view: "some" becomes "not all" more slowly when exact numbers are available as rival words [b28; not opened]. A 2022 study found implicature about 200 ms faster after the stronger alternative "all" was shown first (SD about 420-470 ms; target error 24% and 14% in two experiments). The 200 ms figure was not re-found in the full text in the cross-check, so treat it as unconfirmed [b18]. Reading: part of the implicature cost is how salient the alternative is.

**Rational Speech Act (RSA), Frank and Goodman (2012).** The listener uses Bayes: the posterior for a referent is proportional to how likely an informative speaker would be to use that word for it, times the referent's prior salience. Speaker condition vs model r = .98; model vs listener bets r = .99 (r = .87 with 0 and 100 predictions removed); salience alone vs listener r = .19, not significant. 745 MTurk participants in total (listener 263, speaker 206, salience group of 20 in the paper text; the supplement counts more). No free parameters [a13, b21]. Limit: a tiny reference game with one-word utterances.

**Good-enough processing, Ferreira and colleagues (2001-2007).**
- Christianson et al. (2001): five experiments on garden paths. Exp 1a, 36 students, 134 sentences. Wrong "yes" to "did the man hunt the deer" was 47.4% with a long ambiguous region vs 32.1% with a short one; plausible 47.6% vs implausible 32.0%; plausible garden path 47.6% vs control 26.2%. Subordinate-clause questions drew 55.6% wrong "yes"; matrix-clause questions only 9.4%. So the reader held both the new and the old role at once. Reflexive absolute transitive verbs gave 39.1% vs 62.0% for optionally transitive verbs, but clause order still mattered (70.3% vs 30.7%), so the effect is about parsing, not only world knowledge [a01-a03; re-opened in the cross-check].
- Patson et al. (2009) answered the objection that the yes/no probe causes the error. 50 participants, 96 sentences, paraphrase task. Partial-reanalysis paraphrases: 72% for ambiguous sentences vs 29% with a disambiguating comma. Full reanalysis: 21% vs 62% [a04].
- Ferreira (2003): unambiguous passives get the wrong agent often; clefts ("It was the man who bit the dog") are understood though rarer. The authors link this to a first-noun-is-agent heuristic (Bever 1970). Exact percentages were never read [a06, b26].
- Ferreira and Patson (2007), the review: comprehension builds a representation as detailed as the task requires. "While Katie fixed the car hit a fire hydrant" was judged grammatical on about one third of trials [a05].
- Swets et al. (2008): depth follows task. Ambiguous relative-clause sentences are read faster than disambiguated ones only when readers expect shallow questions; with deep questions the advantage disappears. Tan and Foltz (2020) saw the same in Chinese learners of English [a09, second-hand].

**Competing accounts of the lingering misreading** [a08, a10, a11]:
1. Partial reanalysis (Christianson, Patson).
2. Memory traces of the old parse (Kaschak and Glenberg 2004).
3. Plain difficulty: garden paths raise all errors, including on unrelated misreadings (Chromy 2022).
4. Noisy-channel reading (Qian, Levy): readers repair toward the likely intended message. In ERP work, P600 reanalysis effort did not differ for right and wrong answers (against lazy reanalysis), yet the likelihood of the wrong reading predicted accuracy.

Frances (2024) reviewed about 20 direct tests among 500+ citing papers: 11 on "ambiguity stays unresolved", 8 on "depth depends on task". Evidence is mixed. Main criticism: the principle is too vague to falsify, because any deep processing can be called task-required. Logacev and Vasishth (2016): partial-specification models affected answers on 17% of trials, and non-specification models fit better [a08].

**Moses illusion.** Erickson and Mattson (1981) reported most people answer "two", even with a warning, and detection rises when the wrong word is less related to the right one [a07, b23; not opened]. Reder and Kusbit (1991) argued for partial matching to memory (not poor encoding); warnings lower but do not remove it; literal-task rates 33%, 35%, 35%, 32% [b24, d14]. Hannon and Daneman (2001): working memory and reading ability predict detection; close impostors are missed more [b22]. Sanford et al. (2011) and Sturt et al. (2004): easy anomalies give an N400; hard ones that fit the context give only a late positivity near 800 ms; an unfocused word swapped for a related word is the hardest to notice in change detection [a12].

**Noisy-channel comprehension.** Readers treat the input as possibly corrupted and repair toward the likely intended message. A 2026 study: agreement slips are repaired in line with how often speakers make each kind of slip. Trials not resolving the mismatch: 6.5% (Study I) and 9.9% (Study II). Non-literal reading of subject number: about 22%, 35-45% and about 15% by condition [b19].

**Ambiguity in NLP.** Task ambiguity (Tamkin et al. 2022), ambiguity modelling (Liu et al. 2023) and clarifying questions (Zhang and Choi 2023; Kobalczyk et al. 2025; Pu et al. 2026) are the AI side of "infer what is meant."

## 3. Core findings with exact numbers

H means human data, L means LLM data.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| H: wrong role lingers after garden-path reanalysis | Exp 1a: 47.4% wrong "yes" long vs 32.1% short region; 47.6% plausible vs 32.0% implausible; 55.6% subordinate vs 9.4% matrix questions; 36 students | Christianson 2001 [a01, a02] | [E] K01 |
| H: lingering is not caused by the probe question | paraphrase: partial reanalysis 72% ambiguous vs 29% comma; full reanalysis 21% vs 62%; N=50, 96 items | Patson 2009 [a04] | [E] K02 |
| H: mechanism of lingering | partial reanalysis vs memory trace vs plain difficulty vs noisy channel | Frances 2024 [a08, a11] | [C] K03 |
| H: passives read with wrong agent | "large proportion"; clefts fine; exact figures not read | Ferreira 2003 via 2007 [a05, a06] | [S] K04 |
| H: Moses illusion robust | 52.3% (Erickson and Mattson, as quoted); 49% (Exp 1, d=0.71) and 52.6% (Exp 2, d=0.83) in multiple choice; literal condition 32-35% (Reder and Kusbit); knew the term 73.2%; N=914 over four experiments; money cut it about 16% and needed about 300 people to show | Speckmann and Unkelbach 2021 [b17, d14] | [E] K05 |
| H: closer impostor missed more | ChatGPT strong 0.14 vs weak 0.17 (p=.036, not robust without exemplar items); humans show it more clearly | Cai 2024; Hannon and Daneman 2001 [a21, b04, b22] | [E] K06 (LLM part fragile) |
| L: older LLMs fall for Moses-type | davinci-003 72% fell, 18% correct; ChatGPT-3.5 74% and GPT-4 88% correct on 50 illusions; humans 64% intuitive | Hagendorff 2023 [b01] | [S] K07 |
| L: one-line warning fixes it | "Think carefully and check the question for invalid assumptions": 18% to 54% correct, intuitive 72% to 28%; 10+ solved examples over 64%; davinci-003 only | Hagendorff [b02] | [S] K08 |
| L: ChatGPT flags few Moses errors | baseline 0.00; strong 0.14, weak 0.17 (z=12.55, 13.27); Vicuna 0.002/0.022/0.018; far under humans | Cai 2024 [a21, b04] | [E] K09 |
| L: unstated inferences not drawn | ChatGPT yes: explicit 0.95, bridging 0.49, elaborative 0.23 (23 items); Vicuna 0.79/0.24/0.20 | Cai 2024 [a22] | [S] K10 |
| L: base models near chance on implicature | humans 86.2% (best 89.8%; text also says 92%); base about 60% zero-shot; GPT-3-175B best 68.7% at 5-shot; 600 items | Ruis 2023 [a15, c01] | [E] K11 |
| L: example-level instruction tuning lifts implicature | 0-shot to 5-shot: GPT-4 81.8 to 82.0; ChatGPT 72.1 to 73.9; davinci-003 71.2 to 79.7; Cohere-52B 60.2 to 75.4; T0 72.3 to 74.5 | Ruis [c02] | [E] K12 |
| L: CoT effect on implicature varies by model | 5-shot to CoT: GPT-4 82.0 to 86.5 (+4.5; human 86.2); davinci-003 +4.0; ChatGPT +3.3; davinci-001 74.5 to 67.3 (-7.2); Cohere -0.1 | Ruis [c03] | [E] K13 |
| L: gain concentrated on context-heavy items | particularised GPT-4 71.97 (30-shot) to 81.63 (CoT) vs humans 83.18; generalised 86.23 to 88.66; 47 generalised, 94 particularised labelled of 600 | Ruis [a16, c04] | [E] K14 |
| L: few-shot gain partly format learning | random labels did not hurt Cohere-52B | Ruis [a17] | [S] K15 |
| L: pragmatic errors look human-like | wrong answers favour literal over overlap distractors; worst on humor, irony, maxims; text-davinci-002 55% on punchlines; removing context hurts irony most | Hu 2023 [a18, c06-c08] | [E] K16 |
| L: scale slow for implicature | 0.04% per billion (GPT-3 6.7B to 175B); 0.15% per billion (Cohere 6B to 52B) | Ruis [c05] | [S] K17 |
| L: Chinese multi-turn implicature | GPT-4 94% vs humans 93.1% (p=.802); 200 questions; open models 43-78.5% | [b15] | [S] K18 |
| H and L: garden-path questions | humans 95.4% simple (92.4-98.7) vs 37.0% GP; o1-preview 78%, Gemma-27B 74%; CoT no significant change; plausibility p=4.1e-16 | Amouyal 2025 [a23, c09, c10] | [E] K19, K20 |
| L: thinking helps GP less | absolute gain 0.17 GP vs 0.35 others; GPT-5 46.8% GP vs 93.7% non-GP; weak models hurt; o3 74.5% no thinking, GPT-5 88.9% thinking overall | Amouyal 2025b [b10, d13] | [S] K21 |
| L: illusion profile differs from humans | NPI (structural) illusion tricks LMs more than humans; comparative and depth-charge (meaning) illusions trick them little | Zhang 2024 [b06, c12] | [C] K22 |
| L: ambiguity modelled poorly | AmbiEnt 1,645 pairs, 35.2% ambiguous; crowd agreement 89.7%; GPT-4 EDIT-F1 18.0, correct disambiguation 32.0%; self-contradiction 76% of pairs; recognition 63.0%; NLI exact label set 43.6%; fact-check recall 88.8%, precision 12.4% | Liu 2023 [c13-c15] | [S] K23 |
| L: ask by information gain | INTENT-SIM about doubles gain at 10% question budget; EIG picks better questions in 20 questions and code | [c18-c20] | [E] K24 |
| L: RSA | RSA reranking helps production, adds nothing to comprehension on top of CoT; best models r>0.9 with human means; 708 humans | Qiu 2025 [c21-c23, d11] | [E] K26 |
| H: depth follows task expectation | ambiguity advantage only under shallow-question expectation | Swets 2008 [a09] | [S] K27 |
| H: noisy-channel repair | repair rates track speaker error rates | [b19] | [S] K28 |
| H: GP recovery predicts insight | 9% extra variance beyond working memory, 5% beyond fluid intelligence; N about 100 | [b20] | [S] K29 |
| L: false-premise flag rates 2025-26 | reasoning models fail to challenge 26-42% of false presuppositions (37-70% at strongest wording); Cancer-Myth 585 items: GPT-5 42.1%, Gemini-2.5-Pro 41.4%, Claude-4-Sonnet 40.0%, GPT-4o 5.8%; MultiHoax best 0.46 (others 0.18-0.22); GPT-4o 84.08% on German political questions | [d01, d02, d05, d06] | [E] K30 |
| L: precaution prompts cost false alarms | Cancer-Myth up to 80%, but 41% of 150 clean questions flagged and about 10% loss on other medical benchmarks; abstain-list system prompt: no significant precision loss | [d03, d04] | [C] K31 |
| L: more reasoning does not fix premises | reasoning +2 to +11 points accuracy but more decisive; abstention -24% on average vs instruct bases (4k thinking + 4k answer) | [d01, d04] | [E] K32 |
| L: models assume, do not ask | clarifying question at most about 5% of answers (10 models); GPT-4 about 90% unambiguous vs 15-27% ambiguous | Su and Cardie 2026 [d07] | [S] K33 |
| L: asking helps in agent tasks | Opus-4.5 47% to 78% pass@3 (MCP-Atlas); Ask% 73% (Opus) vs 63% (GPT-5.2); gain per question 0.11 vs 0.05 | Pu 2026 [d08, d15] | [S] K34 |
| L: context-heavy implicature gap persists | GPT-4o 76% vs humans 89% on hard subset (400 items); gpt-5-nano 41 to 73, gpt-5-mini 71 to 81 with scaffold; gpt-4o ceiling 82 | Arai and Ren 2026 [d10] | [C] K35 |
| L: unstable answers | item stability 0.66 for lowest model; ChatGPT-4 accuracy 0.83, Llama2 0.66; 26,680 data points; sceptic authors | Dentella 2024 [a20, d12] | [S] K36 |

## 4. Mechanisms and models

Each is written so it can be built as code plus short prompts.

**4.1 First-parse-plus-leftover (good-enough).** The reader builds a role assignment fast from heuristics (first noun is agent; plausible noun-verb pairs). If later words contradict it, a second assignment is built. The old one is not erased. A later question about the old proposition is answered from the leftover.
*Engineering reading:* do not trust a first reading to be overwritten by a correction in the same context. After any correction, passive or reversal in the prompt, extract "agent / action / patient" as three fields from the original wording and compare to the first restatement. Disagreement is the signal (G1). This is the behavioural fix only; no mechanism claim is needed (K03).

**4.2 Partial matching (Moses).** The question word is matched to memory by overlap, not identity. "Moses" matches "Noah" closely enough to pass. Closeness (semantic and in the discourse focus) sets the miss rate.
*Engineering:* a presupposition extractor lists every definite entity and attached fact in the question ("the animals Moses took on the ark"). Each is checked by a separate short question: "Is it true that X? Who actually did?" Run entity by entity so a close substitute cannot ride on the global match.

**4.3 Implicature as inference to the best speaker intent.** Steps: (1) literal meaning; (2) what a cooperative speaker would have said if they meant the literal yes or no; (3) why they said this instead; (4) the meaning. The DRInQ three-step prompt (surface, evidence, speaker intent) is this form [d10]. Ruis's hand-written CoT is similar [c03].

**4.4 RSA.** For each candidate meaning m and utterance u: P(m|u) is proportional to P(u|m) times prior(m), where P(u|m) is a softmax of speaker utility (informativeness minus cost) over alternative utterances [a13]. Cheap form: ask the model to list 2-4 alternatives the speaker could have said and which meaning each would signal. Qiu et al. found this adds nothing over CoT in comprehension, because chains already list alternatives [c23]. Keep RSA for output wording only.

**4.5 Noisy channel.** Posterior over intended message = prior over messages times likelihood of corruption. Readers repair slips at rates tracking how common the slip is [b19]. Engineering reading: a "likely speaker error" check is the mirror image of a literal reading. Not tested on LLMs (gap 10). It could also hurt, since over-repair is a misread too.

**4.6 Information-gain clarification.** Sample K candidate readings or solutions; pick the question whose answers split the candidates most evenly (expected information gain). INTENT-SIM estimates entropy over simulated intents to decide when to ask [c18, c19]. For an agent: ask only when the readings lead to different outputs and the difference matters to the outcome (LHAW [d08, d15]).

**4.7 Premise gate with a false-alarm limit.** Detection and false alarm trade off (Cancer-Myth: 41% false alarms at up to 80% detection) [d03]. A gate needs a firing rule (a stated reason: "claim X conflicts with fact Y I can name") and a cost on clean items.

**4.8 Depth follows expected check.** A reader expecting shallow questions reads shallow (Swets 2008). Engineering reading: S0 could tell the agent what kind of check S8 will run. Untested on LLMs, and a risk of gaming the checker (K27).

## 5. What holds up

**Replicated and solid.**
- Lingering garden-path misinterpretation: original (2001), paraphrase replication (2009), eye-tracking support (Slattery 2013, second-hand), and LLM mirrors (Amouyal 2025). The effect is real; the cause is disputed.
- Moses illusion: Erickson and Mattson 1981; Reder and Kusbit 1991 (32-35%); Speckmann and Unkelbach 2021 (49%, 52.6%). It survives a multiple-choice format with the right answer on screen and a financial incentive (money cut it only about 16%). That rules out the simple "cooperative speaker" and "low effort" explanations.
- Plausibility of the wrong reading is the best predictor of the garden-path error in humans (p=4.1e-16), and models rank the six conditions in the same order as humans [a23, a24].
- Context-heavy implicature is harder than context-free for humans and models (Ruis; Arai and Ren 2026).
- LLM false-premise flag rates remain low in 2025-26 models [K30].

**Failed, fragile or contested.**
- Cai's "ChatGPT detects weak impostors more" (p=.036) vanishes without exemplar items [b04].
- LLM illusion profile: NPI trips models more than humans, meaning illusions less (Zhang 2024); Paape (2023) says transformers look more literal on depth-charge, but that source was not read [c26]. [C]
- RSA on comprehension adds nothing on top of CoT.
- Dentella's instability: sceptic authors, unvalidated benchmark; voting never tried [d12].
- The good-enough principle itself: too vague to falsify (Frances 2024).
- Lingering-misreading mechanism: four accounts, none ruled out.
- Few-shot gains in implicature: partly format learning [a17].

**Moderators.**
- Human: question type (subordinate vs matrix 55.6% vs 9.4%); ambiguous-region length (47.4 vs 32.1); verb class (39.1 vs 62.0); plausibility; comma; task expectation (shallow vs deep questions); semantic closeness of the swapped word; working memory and reading skill (Hannon and Daneman). The Moses error occurs even though the person knew the right name 73.2% of the time.
- LLM: model strength. CoT lifts GPT-4, ChatGPT and davinci-003 on implicature (+3.3 to +4.5) but lowers davinci-001 (-7.2). Scaffolds lift gpt-5-nano from 41% to 73% and gpt-5-mini 71% to 81% but not gpt-4o [d10]. Thinking tokens help GP items only half as much (0.17 vs 0.35). Forceful wording of a false claim raises agreement (37-70% at the strongest level) [d16].

**Interventions that worked.**
- Warning suffix on davinci-003 (18% to 54%) [b02]; one weak model only.
- 10+ solved examples (over 64%).
- CoT for strong aligned models on implicature.
- Abstain-list system prompt: more abstention, no significant precision loss [d04].
- Clarifying questions in agent tasks (47% to 78%).
- Three-step pragmatic scaffold for small models [d10].
- Neutral wording of the user's claim ("can you verify whether...") gave the best behaviour [d16].

**Interventions that did not work or backfired.**
- CoT on garden-path questions (no significant change) [c10].
- Thinking on weak models for garden-path items (hurt) [d13].
- Precaution prompts: 41% false alarms, about 10% loss elsewhere [d03].
- Reasoning fine-tuning: -24% abstention [d04].
- CoT and few-shot on ambiguity identification: marginal gains only (CLAMBER) [d09].
- RSA over CoT in comprehension [c23].
- Multi-agent MDAgents with GPT-4o: no better than plain GPT-4o on hidden premises [d02] (consistent with G9).
- Alternatives-only pragmatic prompt can worsen magnitude error (Gemini 1.572 to 2.470) [c24].

## 6. Language models

**Timeline.**
- 2022-23, base and early chat models: near chance on yes/no implicature (about 60% zero-shot; best 68.7%); aligned models 72-82% zero-shot; GPT-4 81.8% to 86.5% with CoT against a human mean of 86.2% [c01-c03]. Moses: davinci-003 18% correct, ChatGPT-3.5 74%, GPT-4 88% [b01]. Cai found ChatGPT flagged only 0.14-0.17 on a different, instruction-primed item set [a21]. Two item sets and two measures, so no direct comparison.
- 2023-24: ambiguity: GPT-4 writes a correct disambiguation 32.0% of the time and contradicts itself on 76% of reading pairs [c13, c14]. Comprehension questions: ChatGPT-4 0.83, unstable across repeats [d12].
- 2025: garden-path questions: best 78% (o1-preview) vs humans 37.0% on the GP set. Humans were timed (400 ms per word, 5 s answer) and models saw the whole text, so this is not like for like [a23, b08]. With thinking, GPT-5 gets 46.8% on a harder garden-path set (93.7% on non-GP) [b10]. False premises: 26-42% not challenged by reasoning models; hidden premises: under half [d01, d02, d05].
- 2026: context-heavy implicature GPT-4o 76% vs humans 89% [d10]. Models almost never ask (at most about 5%) [d07]. Agents ask too much or too little, and gain per question varies about 3x [d08]. No 2026 top-tier model appears in most of these studies.

**What changed it, by how much.**

| Change | Effect | Source |
|---|---|---|
| Example-level instruction tuning | +12 to +21 points zero-shot over base | [c02] |
| Few-shot (5) | +0.2 (GPT-4) to +15.2 (Cohere) | [c02] |
| CoT, strong aligned | +3.3 to +4.5; weak model -7.2 | [c03] |
| CoT on GP questions | no significant change | [c10] |
| Thinking, GP vs other | gain 0.17 vs 0.35 | [d13] |
| Warning suffix (davinci-003) | 18% to 54% | [b02] |
| Precaution prompt (frontier) | up to 80% detect; 41% false alarms | [d03] |
| Abstain-list system prompt | more abstention, no significant precision loss | [d04] |
| Scaffold, small model | 41 to 73 (nano), 71 to 81 (mini); none on gpt-4o | [d10] |
| Ask-user tool in agent tasks | 47% to 78% pass@3 | [d08] |
| Scale (GPT-3 family) | 0.04% per billion | [c05] |

**Pattern.** Models share human error patterns: plausible wrong readings win, context-heavy implicatures are hardest, errors favour literal readings. They differ in three ways. They under-flag false premises, they under-ask, and extra reasoning makes them more decisive rather than more careful. Almost all of this is on models from 2022-2025. No study tests a scaffold (as opposed to a prompt tweak) on these traps at equal tokens.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Tags [E]/[S]/[C].

### Add now (established)

1. **S1: carry speaker, goal and setting into the restatement for context-heavy tasks.** The gap is on particularised items; the fix in the data is giving the model the situation plus a stepwise read (GPT-4 71.97 to 81.63). [E] K14; ids a16, c04.
2. **S0/S1: gate the "write what the speaker meant" step by model strength.** It lifts strong aligned models (+3.3 to +4.5) and can hurt weak ones (-7.2); scaffolds lift gpt-5-nano and mini but not gpt-4o. [E] K13, [C] K35; ids c03, d10. Gate it, do not make it universal (G7).
3. **G11 reinforcement: extra thinking is not the premise fix.** More thinking made models more confident on false claims (reasoning -24% abstention; 26-42% unchallenged). [E] K32; ids d01, d04. Premise handling must be structural (code lists the presuppositions), not a longer chain.
4. **G7 measurement rule: any premise or ambiguity step is scored on clean items too.** Reason: the Cancer-Myth 41% false-alarm cost. [E] for the cost, [C] for the step itself, K31; id d03.
5. **S1: clarify only when readings lead to different outputs that matter.** Information-gain choice of questions beats random about 2x at a 10% budget. [E] K24; ids c18-c20, d08. The ask must be a code-decided event, since models default to assuming [S] K33.

### Test first (single-source or contested)

| Item | Part | Tag | Ids |
|---|---|---|---|
| Presupposition extractor: list each definite entity and attached claim, check each separately | S1 | [S] K07, K08; [C] K31 | b01, b02, d03 |
| Role listing (agent / action / patient) vs plain restatement for passives and corrections | S1 | [S] K04, K37 | a05, a06, d13 |
| Paraphrase-first then compare | S1 | [E] for the human effect K02; untested on agents | a04 |
| Premise check with a stated-reason firing rule vs a generic "be careful" line | S1 / G | [C] K31 | d03, d04 |
| Abstain-list system line ("say cannot tell if the task lacks X") | S1 | [S] | d04 |
| Ask only if outcome-critical vs always-assume vs always-ask | S1 | [S] K34 | d08, d15 |
| Neutral rewording of the user's claim by code before reasoning | S1 input hygiene | [S] | d16 |
| Self-consistency vote over 5 samples on pragmatic traps | S8 / G4 | [S] K36 | d12 |
| Tell the agent what the checker will ask | S0 | [S] K27 | a09 |
| "Likely speaker error?" check (noisy channel) | S1 | [S] K28 | b19 |
| Mark load-bearing words in long prompts | S1 | no direct evidence | a12 |
| Ambiguity enumeration (list 2-3 readings, test consistency) | S1 / O8 | [S] K23 | c13, c14 |

Memory note [M]: a lesson line of the form "this task class had a presupposition trap" is cheap (S9), shown after the first attempt. Not tested.

## 8. Concrete tests on our bench

All arms at equal total tokens (thinking plus answer plus any extra check calls). Report accuracy and cost per item, by item type.

| Item type | Arms | Metric | Expected effect |
|---|---|---|---|
| Moses and false-presupposition items (50 swapped, 50 clean twins; close and distant swaps) | plain; plain plus same-length neutral line; generic "check for invalid assumptions" line; presupposition extractor with per-entity check | flag rate on false items; false-alarm rate on clean items; net accuracy | extractor beats generic line on flag rate; false alarms under 10% on clean items (Cancer-Myth precaution prompts reached 41%) |
| Passives and corrected statements (implausible passives, mid-text retractions, reversed roles) | plain; role-listing step; paraphrase-first | wrong-agent rate | role listing lowers errors; size unknown, guess 5-15 points on weaker models |
| Garden-path questions (Amouyal-style, six conditions) | thinking budget X; same tokens split into role listing plus short answer | accuracy by condition | little gain from thinking (0.17); role listing may help |
| Implicature (Ruis 600 items; tag particularised) | direct; three-step read; CoT | accuracy overall and on particularised | gain concentrated on particularised; none on strong models |
| Ambiguous tasks (AmbiEnt-style, or our tasks with two readings that give different outputs) | always-assume; ask-when-critical (code gate); always-ask | outcome score; questions per task; tokens | ask-when-critical wins; always-ask loses on tokens |
| Strongly worded false claims (five levels, Sathyanathan style) | raw; neutral reword by code | false-claim agreement | reword lowers agreement at levels 3-4 |
| All pragmatic traps, repeated 5 times | single sample; majority of 5 at matched tokens | accuracy; item stability | small gain; stability shows whether noise is the issue |
| Check-type disclosure | S0 says "deep check" vs says nothing | detail retention on long prompts | uncertain; may be null |

## 9. What does not transfer, and why

- **Working-memory and speed limits.** Humans read at 400 ms per word with a 5 s limit in Amouyal's study, which inflates human errors. A model sees the whole text. The human effect size does not carry over; only the item-difficulty ordering does.
- **Eye-tracking and ERP findings.** Reanalysis timing, P600, N400 describe the human parser. No agent state maps to them [a11, a12].
- **The "lazy human" explanation.** For humans good-enough saves effort. Model failures come from training and tuning, not effort saving. Hagendorff's strong models answered illusions with no visible reasoning [b03].
- **Moses rates from humans.** For the model the failure is a premise under-flag; the mechanism is unknown, so the human partial-matching story is not a model of it.
- **RSA as a comprehension scaffold.** Chains already list alternatives; no gain [c23].
- **Few-shot gains in implicature.** Partly format learning [a17], so they do not show better pragmatics.
- **Scaling claims** (0.04% per billion) are for the GPT-3 family only.
- **Debate-style pragmatic agents** (NLPSI semantic and pragmatic agent debate [c27]) conflict with G9.
- **Telling a model to be careful** is already in section 4b as a non-fix; the Hagendorff suffix worked on one weak model only.
- **Garden-path recovery predicts insight** (9%) is correlational, N about 100, human only; no agent action follows.

## 10. Open questions

1. Does a presupposition-extractor step beat a generic warning on current frontier models at equal tokens, and what is its false-alarm rate? (Gaps 1, 2.)
2. What are 2026 flag rates on classic Moses word swaps? Nobody has run them; our numbers are from 2023 (K07, K09).
3. Does role listing or paraphrase-first fix garden-path and passive errors in reasoning models? (Gaps 3, 37.)
4. Does ask-when-critical beat always-assume at equal tokens, not just per question? (Gap 4.)
5. What are the real passive-misreading rates (Ferreira 2003) and the original Moses rate (Erickson and Mattson 1981)? Primary texts not opened. (Gap 5.)
6. Does CoT still help mainly on particularised implicatures in reasoning models? (Gap 6.)
7. Does telling the agent the check type change reading depth, and can that be used without gaming? (Gap 7.)
8. Does marking load-bearing words help? (Gap 8.)
9. Does self-consistency voting fix unstable pragmatic answers? (Gap 9.)
10. Does a "likely speaker error" check help or hurt? (Gap 10.)
11. Which account of the lingering misreading is right? It decides which fix to expect.
12. Is the NPI vs meaning illusion profile of LMs stable across studies (Zhang vs Paape)?

## 11. Sources

[V] opened, [M] snippet or second-hand only.

- [V] Christianson, Hollingworth, Halliwell, Ferreira (2001) Thematic roles assigned along the garden path linger. https://ferreiralab.faculty.ucdavis.edu/wp-content/uploads/sites/222/2015/05/Christianson-et-al.-2001_LingeringInterpretationsGP_Cog-Psych.pdf (a01-a03); b25 DOI https://doi.org/10.1006/cogp.2001.0752 [M]
- [V] Patson et al. (2009) Lingering misinterpretations ... paraphrasing task. https://ferreiralab.faculty.ucdavis.edu/wp-content/uploads/sites/222/2015/05/Patson-et-al.-2009_GardenPathParaphrasing_JEPLMC.pdf
- [V] Ferreira and Patson (2007) The Good Enough approach. https://ferreiralab.faculty.ucdavis.edu/wp-content/uploads/sites/222/2015/05/Ferreira-Patson-2007_GoodEnoughApproach_Lang-Ling-Compass.pdf
- [M] Ferreira (2003) The misinterpretation of noncanonical sentences. https://doi.org/10.1016/S0010-0285(03)00005-7
- [M] Erickson and Mattson (1981) From words to meaning. https://doi.org/10.1016/S0022-5371(81)90165-1
- [M] Reder and Kusbit (1991). https://doi.org/10.1016/0749-596X(91)90016-I
- [M] Hannon and Daneman (2001). https://doi.org/10.3758/BF03195363
- [V] Frances (2024) Good enough processing: 20 years since. https://doi.org/10.3389/fpsyg.2024.1323700 (carries second-hand Swets 2008, Tan and Foltz 2020, Slattery 2013, Qian 2018, Chromy 2022, Nakamura and Arai 2016, Sanford 2011, Sturt 2004 [M])
- [M] Karimi and Ferreira (2016). https://doi.org/10.1080/17470218.2015.1053951
- [M] Degen and Tanenhaus (2015). https://doi.org/10.1111/cogs.12171
- [M] Grice (1975) Logic and conversation. https://en.wikipedia.org/wiki/Cooperative_principle
- [V] Frank and Goodman (2012). https://web.stanford.edu/~ngoodman/papers/FrankGoodman-Science2012.pdf ; https://doi.org/10.1126/science.1218633
- [V] Speckmann and Unkelbach (2021) Moses, money, and multiple-choice. https://pmc.ncbi.nlm.nih.gov/articles/PMC7751745/
- [V] Salient alternatives facilitate implicatures (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8970470/
- [V] Comprehenders' error correction mechanisms ... production statistics (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13721780/
- [V] Garden-path recovery and creative problem solving (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13412464/
- [V] Ruis et al. (2023) The Goldilocks of pragmatic understanding. https://arxiv.org/abs/2210.14986
- [V] Hu, Floyd, Jouravlev, Fedorenko, Gibson (2023). https://arxiv.org/abs/2212.06801
- [V] Dentella et al. (2024) Testing AI on language comprehension tasks. https://arxiv.org/abs/2302.12313
- [V] Cai et al. (2024) Do LLMs resemble humans in language use? https://arxiv.org/abs/2303.08014
- [V] Amouyal et al. (2025) When the LM misunderstood, the human chuckled. https://arxiv.org/abs/2502.09307
- [V] Amouyal et al. (2025) Comparing human and LM sentence processing difficulties, thinking models. https://arxiv.org/abs/2510.07141
- [V] Li et al. (2024) Incremental comprehension of garden-path sentences (b11 small read; a25 snippet [M]). https://arxiv.org/abs/2405.16042
- [V] Hagendorff, Fabi, Kosinski (2023) Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206
- [V] Zhang, Gibson, Davis (2024) Can language models be tricked by language illusions? https://arxiv.org/abs/2311.01386
- [V] SwordsmanImp (2024) Chinese conversational implicature. https://arxiv.org/abs/2404.19509
- [V] Askari et al. (2025) Are BabyLMs deaf to Gricean maxims? https://arxiv.org/abs/2510.04764
- [V] Liu et al. (2023) We're afraid language models aren't modeling ambiguity. https://arxiv.org/abs/2304.14399
- [V] Tamkin et al. (2022) Task ambiguity in humans and language models. https://arxiv.org/abs/2212.10711
- [V] Zhang and Choi (2023) Clarify when necessary. https://arxiv.org/abs/2311.09469
- [V] Kobalczyk et al. (2025) Active task disambiguation with LLMs. https://arxiv.org/abs/2502.04485
- [V] Qiu et al. (2025) On the same wavelength? https://arxiv.org/abs/2509.06952
- [V] Muhlenbernd (2026) Social meaning in LLMs. https://arxiv.org/abs/2604.02512
- [M] Cong and Rayz, LLMs and good-enough processing (CogSci). https://escholarship.org/content/qt2tb5m7p6/qt2tb5m7p6.pdf
- [M] Paape (2023) Depth-charge illusion. https://www.experimentsinlinguisticmeaning.org/
- [M] NLPSI 2025 debate for scalar implicature. https://aclanthology.org/2025.nlpsi-1.7.pdf
- [M] Stanford CS224N RSA report. https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1234/final-reports/final-report-169845842.pdf
- [V] Sathyanathan et al. (2026) Reasoning models and presuppositions. https://arxiv.org/abs/2605.03050
- [V] Zhu et al. (2025) Cancer-Myth. https://arxiv.org/abs/2504.11373
- [V] Kirichenko et al. (2025) AbstentionBench. https://arxiv.org/abs/2506.09038
- [V] Shafiei et al. (2025) MultiHoax. https://arxiv.org/abs/2506.00264
- [V] Sieker et al. (2025) LLMs struggle to reject false presuppositions. https://arxiv.org/abs/2505.22354
- [V] Su and Cardie (2026) Knowing but not showing. https://arxiv.org/abs/2605.25284
- [V] Pu et al. (2026) LHAW. https://arxiv.org/abs/2602.10525
- [V] Zhang et al. (2024) CLAMBER. https://arxiv.org/abs/2405.12063
- [V] Arai and Ren (2026) DRInQ. https://arxiv.org/abs/2605.24267
