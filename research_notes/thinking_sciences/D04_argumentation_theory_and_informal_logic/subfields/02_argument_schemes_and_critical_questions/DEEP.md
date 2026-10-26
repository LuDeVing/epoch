# Argument schemes and critical questions: deep document

*Subfield D04.02. Built from evidence_a-d.jsonl (a01-a27, b01-b25, c01-c32, d01-d22), claims.jsonl (K01-K29) and critique.md in this folder. Schema references (G1-G12, S0-S9, O1-O8, section 4b) are to `research_notes/single_agent/SCHEMA.md` v0.2. No new searching was done for this document.*

**Headline.** Argument schemes are a well-built theory of how to test a named kind of argument. The human evidence that people use them is thin. The language-model evidence says three things. (1) Models write weak critical questions, and scheme text in the prompt does not reliably help. (2) Models answer critical questions with a yes-bias and cannot be trusted to grade themselves. (3) Pipelines built on critical questions beat plain prompting, but nobody has run them against best-of-N at equal tokens. The most useful part for our agent is the *shape* of the idea: a code-held table of questions per argument type, with each answer checked by code or by a quoted source. Whether that beats a generic "find the flaw" step at equal tokens is unknown, and no paper tests it.

---

## 1. What it is

An **argument scheme** is a named pattern of reasoning with a fixed premise-to-conclusion template. Examples: argument from expert opinion, from analogy, from cause to effect, from consequences, from example, from sign, from popular opinion, practical reasoning.

Each scheme comes with **critical questions (CQs)**. These are the standard ways the pattern can go wrong. The scheme is **defeasible**: the conclusion stands provisionally. It falls when a CQ gets a good answer against it. [a01, K01]

Worked example, expert opinion. Premises: E is an expert in domain S containing A. E asserts A. Conclusion: A. Six CQs: Expertise (how credible is E?), Field (is E an expert in the field A belongs to?), Opinion (what exactly did E assert?), Trustworthiness (is E personally reliable?), Consistency (is A consistent with what other experts say?), Backup evidence (is E's assertion based on evidence?). [a02, d18]

Two related things must be kept apart:
- **Scheme identification**: which pattern is this argument using? (A classification task.)
- **CQ use**: given the pattern, which questions test it, and what are the answers? (A generation and an answering task.)

The source work is Walton, Reed and Macagno, *Argumentation Schemes* (2008). It is a compendium of 96 schemes, about 60 of them main schemes. [a01, a13] Nobody in this research opened the book. All wording below comes from secondary quotes (Makula 2022, the Stanford Encyclopedia entry, the Wikipedia page, a condensed appendix in the ELLIS Alicante paper). [a02, a01, d18, d16]

**Why it matters for our agent.** The schema's test state S4 needs a way to turn "does this argument hold up?" into code-run checks. A per-type question list, held in a table and picked by code, is the cleanest form of that. The rest of this document says how much evidence there is for it.

---

## 2. History and theories in depth

### 2.1 The theory line

- **Walton's presumptive reasoning (1990s to 2008).** Walton argued that everyday arguments are not deductive or inductive. They are *presumptive*: they shift a burden of proof, and the other side can shift it back by asking a CQ. The 2008 compendium collects the patterns. [a01, a05]
- **Formal home: ASPIC+.** Prakken and Modgil treat schemes as defeasible inference rules. Some CQs attack premises (undermining), some attack the rule's applicability (undercutting), and acceptability is computed in an abstract argumentation framework. [a26, secondary only] This is the formal basis that ArgMed-Agents later used with a symbolic solver. [a24]
- **Bayesian reading (Oaksford and Hahn, 2004 onward).** Textbook "fallacies" such as argument from ignorance are not always fallacies. Strength depends on the amount of evidence, the source's reliability, and the audience's prior. [a08, a09, a10] Harris et al. (2016) did the same for expert opinion with a Bayesian network over expertise and trustworthiness. [a11, abstract only]

### 2.2 The critiques

- **Blair (2001) and Pinto (2001, 2003)**, as reported by Kock (2007). Blair: the origin and classification of the schemes is unexplained. Pinto: many CQs have only heuristic force, not normative force. They cannot really shift the burden back. [a05]
- **Kock (2007)** on practical reasoning: the "presumptive" model fits it badly. [a05]
- **Lumer (2022)**: from an epistemological stance, many of Walton's schemes are fallacious or not epistemically valid. Only a search summary was seen. [a06, snippet only]
- **Mizrahi (2013) versus Walton, Seidel, Hinton.** Mizrahi said the bare form "E says p" barely raises the probability of p. Walton replied that Mizrahi used a one-premise scheme and ignored the premises added by answering the CQs. Makula (2022) says the dispute depends on the framework: if "argument from expert opinion" means a bare opinion, the weakness claim is true but trivial. [a03, a04, K18] The empirical claim behind Mizrahi (experts barely beat chance) was not verified here.

### 2.3 Annotation and classification

- **Feng and Hirst (2011)** built the first classifier of Walton schemes on the Araucaria corpus. Good on schemes with cue words, near chance on abstract ones. [a12, b22]
- **Visser, Lawrence, Reed, Wagemans and Walton (2021)** annotated the US2016 debate corpus with the 60 main schemes. Trained annotators with a decision key reached kappa 0.723 (10.2% sample). Earlier corpora had very low agreement. [a13, b21]
- **Ruiz-Dolz and colleagues (2024-2025)** generated textbook scheme instances with GPT models (NLAS-multi, NLAS-CQ) and trained classifiers. [c20, a19]

### 2.4 The LLM turn (2024-2026)

- **Calvo Figueras and Agerri (2024)** defined the task "critical question generation" and compared theory CQs with LLM CQs. [a14]
- **Calvo Figueras and Agerri (2025)** built the benchmark: 220 debate interventions, 4,976 labelled reference questions. They ran the CQs-Gen 2025 shared task at the ArgMining workshop (19 teams registered, 13 submitted). [a15, b04]
- Parallel applied work: ArgMed-Agents (clinical QA), CQoT (generic CQs as a reasoning step), a misinformation pipeline (CQ answering), DeceptionAnalyser (new deception schemes), and an accountability protocol using scheme CQs to probe model justifications. [a24, b16, a19, a23, a21]

### 2.5 Human-subject work on schemes

All of it is old, narrow and not about accuracy gains. [b17-b20, a07, K15, K16, K19]
- Lay people spot scheme-specific criteria when asked (Schellens et al. 2017, 108 people). The coders knew the schemes, so bias toward scheme criteria is possible.
- Evidence type persuasion (Hoeken 2001, N=324; Hornikx 2008, N=174): statistical beats expert beats causal beats anecdotal in expectation, and partly in effect.
- One quasi-experiment (Nussbaum et al. 2018) with a CQ box in argument diagrams: more CQ-linked refutations, which carried to an in-class essay but not a take-home paper.

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources), **S** single-source, **C** contested. Claim ids are in brackets. "N" = items or people.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A scheme = template + defeasible CQs; 96 in the compendium, about 60 main | 96 schemes; expert opinion has 6 CQs | Walton et al. 2008, via a01, a02, d18 | E (K01), secondhand |
| Zero-shot LLMs write weak CQs | Best of 11 models about 56 on useful-question score (claude-3.5-sonnet ~56.3-56.7 depending on version, o4-mini 54.1, gpt-4o 53.7-54.5); 220 interventions, 34-item test | a15, b01, c02 | E (K02) |
| Prompt tuning, few-shot, fine-tuning barely move CQ scores | Effects "negligible", not reported | c03 | E (K02) |
| Shared-task best needed human relabelling | 67.6 after manual evaluation; automatic scores 36.3 / 44.1 / 50.0 with 28-36% not evaluable | b04, b06, c12 | E |
| Reference labels: 60.91% Useful, 23.21% Unhelpful, 15.88% Invalid | 4,976 questions; test split 42.68% Useful | b01, c01 | E (dataset fact) |
| Human annotators agree only moderately on CQ usefulness | kappa 0.54 after rounds from 0.19 and 0.26 | a15, b02 | S (K03) |
| Direct LLM labelling of CQ usefulness agrees with humans at chance | kappa <= 0.1; reference-matching judges 0.40-0.57 (claude_reference 0.57, gemma 0.44-0.45, similarity 0.40) | a16, b02, c04 | S (K03) |
| An LLM usefulness judge says yes to most | 8.4 of 10 labelled Useful; only 44.4% truly Useful (180 gold-labelled) | d10 (TriLLaMA) | S |
| Scheme text in the prompt: no consistent gain | Alicante questioner-only 54.7 / 53.4 / 46.0 / 54.0 (none / one prompt / per scheme / mixed); with judge 57.7 / 56.5 / 51.6 / 62.4; 79-item test, 27-34% not evaluable | a17, c13 | C (K04) |
| Same, other teams | COGNAC 0.83 (retrieved examples) vs 0.81 (+schemes), 0.79 vs 0.82; ARG2ST: plain prompt best, scheme labels worst; Webis dropped schemes (0.72 both on validation); DayDreamer baseline 72.04 Useful vs scheme pipeline 72.22 | d13, d14, d15, a18 | C (K04) |
| Missing templates hurt | Four ER schemes with no Walton definition; dropping them: Useful 68.28 to 72.22, Unhelpful 12.01 to 8.78 | c17, a18 | E (K06) |
| Walton templates need hand editing | 39.44% of instantiated template questions edited; slot agreement 0.88 over 174 variables | a14, c06, b08 | E (K06) |
| LLM CQs cover more than the templates | 495 raw LLM CQs, 28% relevant and valid; 207 valid, only 52 (25%) in the theory set; 155 valid LLM-only; 16.4% ask for definitions (theory: 0%) | a14, b08, b09, c07 | S (K05), 2023 13B models |
| LLM CQ coverage of arguments is high | 191 unique CQs matched 50 of 51 arguments | c08 | S |
| A generate-then-select LLM judge helps little | Judge +3.4 points over random (p<0.05, McNemar); oracle +34.2 (93.5% useful) | c14, b06 | C (K07) |
| A small trained selector helps more | Webis ModernBERT reranker on 6 candidates: test 0.49 to 0.57 (validation-only reranker 0.48) | d15 | S |
| Debate/deliberation as CQ judge does not help | 52.0 and 37.3 vs 53.9 zero-shot judge | d10 | S |
| Trained annotators can name schemes | kappa 0.723 (60 schemes, 10.2% sample); 0.610 with full guidelines (11.3% sample); 505 arguments | a13, b21 | E (K08) |
| LLMs name schemes poorly on real text | Best F1 0.65 (Claude 3.5, few-shot with descriptions) on 686 Kialo arguments, 7 schemes; GPT-4o 0.49 zero-shot, 0.57 few-shot; Mistral 0.31; Llama-3.2 0.18 | b10 | E (K08) |
| LLMs name schemes almost perfectly on generated text | 0.98-1.00 on NLAS4; RoBERTa 99.2 F1 on NLAS-CQ; but QT30 real dialogue 1.0 (plain), 31.7 (families), 44.8 (families + dialogue data) | b11, a19, c22 | E (K08, K21) |
| Chain of thought is mixed for scheme naming | Claude-3.5 down up to 8% F1; Mistral up up to 15%; Llama-3.2 NLAS4 0.47 to 0.79 | b11 | S |
| Most confused schemes | Cause to effect (confused with consequences, example); expert opinion second | b12 | E (K08) |
| Early classifier by scheme | Example 90.6%, practical reasoning 90.8%, cause to effect 70.4%, consequences 62.9% (50% baseline); consequences vs verbal classification 64.0% | a12, b22 | S (2011 model) |
| Classifiers learn the scheme, not the validity | Fine-tuned flags 16.6% of native valid items but 58.9% of scheme-matched valid items; Reddit-trained 5.7% to 62.0%; human-confirmed valid: 56.6% (30 of 53) | a20 | S (K09) |
| CQ answering by models leans yes | GPT-4 and Mixtral said yes to 53.3% of negative CQs; macro-F1 RoBERTa 70.7 (73.94 with context), GPT-4 63.5 (62.5), Mixtral 28.7 (34.6) | a19, c21 | S (K12) |
| LLMs defending moral verdicts fail on grounds | 6,778 cells, 18.2% failed; Sonnet 4.6 and Llama 3.3 = 67.8% of failures; relevance failures <0.5%; judge agreement 89.6% | a21, b13, c27 | S (K12) |
| Models switch scheme between reasoning and justification | Scheme differs on about 20% of dilemmas; VBPR 72% and 67% of labels; reasoning beats justification by only 0.02-0.04 normalised | a22, b14, c28 | S (K13) |
| Scheme analysis stable for clear cases | Fable: 100 of 100 green, stability 1.00; harder report: 0.93-0.98 within model, 0.89-0.98 cross model; 600 of 600 gave a verbatim excerpt | a23, b24, c25 | S (K14) |
| CQ pipeline beats direct and CoT: ArgMed-Agents | MedQA GPT-3.5 52.7 / 48.0 / 62.1 (direct / CoT / ArgMed); GPT-4 67.8 / 71.4 / 83.3; PubMedQA GPT-3.5 68.4 / 71.5 / 78.3; GPT-4 72.9 / 77.2 / 81.6; 300 items per set | a24, c18 | E (K10) with limits |
| CQ pipeline beats direct and CoT: CQoT | +4.61% reasoning, +5.4% math on MT-Bench, 5 models, GPT-4o judge; Llama-70B reasoning 8.05 / 7.5 / 8.4; Nemotron reasoning 6.75 / 7.7 / 7.3 (CoT won) | b16, c09 | E (K10) with limits |
| The CQ step adds value beyond the plan (CQoT ablation) | Llama reasoning 8.05 / 8.3 (plan only) / 8.4; math 8.95 / 9.25 / 9.55; Nemotron reasoning 6.75 / 6.85 / 7.3 | c10 | S (K11) |
| Self-critique without outside signal hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 after one round; GPT-4 GSM8K 95.5 to 91.5 to 89.0 | d01 | E (K22) |
| Sound checker gains, model critic does not | GPT-4: Game of 24 5 / 3 / 36 (standard / LLM+LLM / LLM+sound verifier); graph colouring 16 / 2 / 38; Blocksworld 40 / 55 / 60. LLM-as-verifier false negative 95.8-97.1% on two domains | d02 | E (K22) |
| Tools make critique work | CRITIC AmbigNQ F1: CoT 58.6, SC 58.5, CRITIC 64.9, CRITIC without tool 58.3 | d03 | E (K22) |
| Models cannot locate errors but fix them given the place | GPT-4 52.87 overall mistake finding (BIG-Bench Mistake); small trained classifier beat prompting | d04 | E (K22) |
| Weak verifiers mislead small refiners | Gemma-7B refiner +8.3 with GPT-4 verifier; own verifier minor | d05 | E (K22) |
| Voting beats critique and debate at equal calls | GSM8K SC 76.7 (1) / 82.5 (3) / 85.3 (6) / 88.2 (9 responses), debate at or below; generative verifier needs ~8x compute to match SC, 128x for +3.8 points on MATH | d01, d07 | E (K23) |
| Sampling plus a sound verifier matched critique | Blocksworld 72 with k=25 sampling vs 87 first-error feedback; Game of 24 42 vs 38 | d02 | E (K23) |
| Format of the check matters | CoVe precision: yes/no joint 0.15 vs factored 0.19; open joint 0.15 vs factored 0.22 (Llama 65B list task) | d06 | S (K24) |
| Models rarely flag flaws unprompted | PCBench proactive: GPT-4o 11.0, DeepSeek-V3 40.5, o4-mini 4.0; assisted (told to check) 73.2-77.9 for top models; Qwen3 8B to 235B assisted 59.9 to 70.0 | d09 | S (K24) |
| Judges find added content, miss omissions | Paired discrimination 0.79-0.94 added vs 0.50-0.63 omitted; list-then-verify flagged 24.6% of omissions at 2.7% false alarms | d20 | S (K24), clinical notes |
| Sycophancy to invalid arguments varies hugely | Compliance with invalid 0% (GPT-6 Astra) to 95% (GPT-4o); responsiveness to valid 32-92% | d19 | S, 2026 names unverified |
| No clean 70B cliff | Writing: 8B to 405B +1.3 points (67.2 vs 68.5); 24B matched 70B (0.78 both); judging: medium and smaller near chance on CriticBench; open models within 10% of frontier on proof checking with up to 25% more inconsistency | d10, d11, d08, d21 | C (K25) |
| Cost of fancy search | Tree of thoughts $21.10 vs $0.98 zero-shot CoT per 30 runs (97.39M vs 2.17M input tokens), no better score | d12 | S (K26) |
| Real-debate scheme frequencies | Example 175, practical reasoning 135, cause to effect 55, consequences 38, sign 25, verbal classification 25, analogy 11, expert opinion 10, authority 4 | d17 | S (K27) |
| Argument from ignorance is not always a fallacy | N=73: positive 4.53 vs negative 4.27 (F(1,72)=11.58); reliable source 5.58 vs 3.21 (F=198.63); Exp 2 N=72 | a09, a10 | E (K17) |
| Evidence type persuasion | N=324 (statistical most convincing); N=174 ranking statistical > expert > causal > anecdotal | b19, b20 | E (K16) |
| Lay criteria are scheme-specific | N=108; authority: expertise 22-24 of 24; cause: sufficiency 19 of 20 | b17 | S (K15) |
| Textbook generated schemes overstate ability | 89.1% of 4,000 kept; EN 74.8% valid after GPT-3.5, kappa EN 0.65, ES 0.22 | c20, a19 | E (K21) |

---

## 4. Mechanisms and models

Each item below is written so an engineer can build it. "Code" means plain program logic. "Model" means a language-model call that fills one slot.

### 4.1 The scheme record

A scheme is a data record, not a prompt.

```
scheme = {
  name: "expert_opinion",
  premise_slots: ["E", "domain S", "claim A"],
  cues: [regexes / keywords],          # for routing
  cqs: [ {id, slot_template, checkable_by: "code"|"tool"|"quote"|"model", check_fn} ... ]
}
```

- Hand-write 5 to 8 records. Do not auto-instantiate 60. [K06: 39.44% of auto-filled questions needed editing; four schemes had no definitions]
- Code fills the slots from the argument (by extraction with a verbatim quote requirement). The model may reword the final question text only. [K28, K14]

### 4.2 Question lists to start from

These are from secondary sources and must be checked against the book. [d16, d18, a27]

- **Expert opinion (6)**: Expertise, Field, Opinion (what exactly was asserted), Trustworthiness, Consistency with other experts, Backup evidence. [a02, d18]
- **Analogy (3, condensed)**: Are the two cases similar in relevant respects? Are there significant differences that undermine it? Is the conclusion in the known case well established? An extra from the book (recalled, not verified): is there another case that points the other way? [d16, a27]
- **Cause to effect (3, condensed)**: Is the link reliable (how strong is the generalisation)? Could other factors intervene? Is it correlation rather than proven causation? A further CQ from memory: did the cause actually occur? [d16, a27]
- **Added by LLM studies and absent from the templates**: a definition-of-terms question (16.4% of valid LLM CQs; 0% of theory CQs). [b09]
- **Absence of evidence (from the Bayesian work)**: how thoroughly was the evidence searched, and how reliable is the source? [K17]

### 4.3 Pipeline shape (what the working systems share)

1. **Extract**: pull the argument and its premises, each with a verbatim quote. Reject premises with no quote. [a23, b24: 600 of 600 gave an excerpt; ungrounded ones are discarded]
2. **Route**: pick the scheme. Routing is the weak step (see 5.3). Options: cue words (Feng and Hirst style), a small classifier, or skip routing and use a generic list.
3. **Ask**: load the scheme's CQs as slot templates.
4. **Answer**: each CQ gets an answer. Where possible by code or tool: search the source, recompute a number, check that a quoted passage supports the claim. [d03, d02]
5. **Aggregate**: code decides. ArgMed-Agents used an abstract argumentation solver over the attacks. CQoT used a pass threshold (7 of 8 CQs, relaxed to 5 of 8). [a24, c09]
6. **Revise**: only from a located failure. [d04: models fix well when told where]

### 4.4 Two published pipelines in detail

**ArgMed-Agents** [a24, c18, c19]: a Generator proposes arguments under a domain scheme (decision making, side effects, danger appeal). Generator output is treated as an *assumption*. A Verifier attacks it with scheme CQs. A symbolic Reasoner builds an argumentation framework and returns the acceptable set. Dialogue limit 8, temperature 0. In 63% of cases with no acceptable decision, reasoning errors were identifiable; 76% of those came from conflicting knowledge, 24% from insufficient knowledge.

**CQoT** [b16, c09, c10]: (1) sketch a plan of premises and conclusion, (2) answer 8 generic CQs about each step, (3) gate on the pass threshold, (4) revise. The CQs are generic, Toulmin-flavoured, *not* Walton scheme-specific.

### 4.5 Generate-many-then-select for CQ writing

ELLIS Alicante [a17, b06]: Questioner (Llama 3.1 8B) writes 4 questions without scheme text and 4 with scheme templates. Judge (Gemma 2 9B) picks 3. 81% of judge-picked questions came from the scheme prompts. Webis [d15]: two small models write 6 candidates, a fine-tuned ModernBERT classifier keeps the top 3. In both, a selector sits after generation. The trained selector gave the larger gain.

### 4.6 Formal side

In ASPIC+ a scheme is a defeasible rule. A CQ becomes one of three attack types: on a premise, on the rule's applicability (an exception), or a rebuttal of the conclusion. Argument acceptability follows from the attack graph (grounded or preferred semantics). [a26, secondary] For our use, the practical lesson is simple: a CQ answered "yes, problem found" must be recorded as a *located attack* with a quote, not as a vague doubt (G2).

---

## 5. What holds up

### 5.1 Holds up (two or more independent sources)

- **Schemes have a stable, codable structure.** Annotators agree substantially when trained and given a key (kappa 0.723). [a13, b21]
- **Model critique without an outside signal does not help and often hurts.** Four independent studies. [d01, d02, d03, d05; K22]
- **At equal calls, voting beats model-run critique and debate** unless the budget is large. [d01, d02, d07; K23]
- **Tool or code checks carry the gain**; the critique text itself adds little. [d02, d03]
- **LLM zero-shot CQ writing is weak**, and prompt tuning does not fix it. [a15, b01, c02, c03, b04]
- **Templates need hand work**; undefined schemes should be dropped. [c06, c17, a14]
- **Generated textbook arguments overstate scheme-detection ability.** [c20, a19, b11]
- **Argument from ignorance is not simply a fallacy**; source reliability and search thoroughness matter. [a09, a10; replication in different manipulation]

### 5.2 Failed or null results

- **Scheme text in the prompt**: no gain for ARG2ST (plain best), COGNAC (within 0.03), Webis (dropped it), Alicante (only mixed prompts helped, 79-item test split). DayDreamer's pipeline cut Invalid questions but not Useful ones. [a17, a18, d13, d14, d15]
- **Prompt tuning, few-shot, fine-tuning** barely moved CQ generation. [c03]
- **LLM judge for question usefulness**: yes-biased; debate and deliberation did not fix it. [d10]
- **Multi-agent / tree search**: tree of thoughts cost 21 times more with no better score. [d12] CriticalBrew's multi-agent gain followed agent count, which means more tokens. [d11]
- **Dropping Walton templates for undefined schemes helped**, i.e. the theory text was incomplete. [c17]

### 5.3 Moderators and boundary conditions

- **Text realism.** Scheme classification is near perfect on generated text (cue words in the prompt text) and 0.65 at best on real Kialo text; classifiers collapse to F1 1.0 to 44.8 on real dialogue. [b10, b11, c22]
- **Which scheme.** Cause to effect and expert opinion are the most confused; example and practical reasoning are the easiest. [b12, a12]
- **Whether the instruction to check is given.** Proactive flaw detection is 4-40% for strong models; told to check, it is 60-78%. [d09]
- **Format.** Open questions in a fresh context beat yes/no restatements; list-then-verify beats free omission-spotting. [d06, d20]
- **Budget.** Verification beats voting only at high compute. [d07]
- **Domain.** Almost all CQ-generation work is on political debate. Moral dilemmas (Henselmans), medicine (ArgMed), MT-Bench (CQoT) are the only other domains. Nothing on puzzles, ARC or novelty. [d17]
- **Model size.** No clean 70B cliff for writing CQs; judge reliability is the limit. [d10, d11, d08, d21; K25]

### 5.4 Interventions that worked

- Code or tool verification of the claim (CRITIC; sound verifier). [d02, d03]
- A small trained selector over generated candidates (Webis). [d15]
- Mixed prompts, with and without scheme text (Alicante, weak evidence). [c13]
- Retrieved similar examples, the largest prompt gain at COGNAC (0.76 to 0.83). [d13]
- Zero-shot CoT, the most robust prompt for fallacy and CQ tasks, at 1/20 the cost of tree search. [c24, d12]
- Forcing a verbatim quote per premise (stability and grounding). [a23, b24]
- A closed list-then-verify procedure for absence detection. [d20]

### 5.5 Did not work

- LLM judge of usefulness. Self-critique without tools. Debate. Bigger models for writing CQs (+1.3 for 50x size). Scheme labels alone in generation prompts. Auto-filled templates for undefined schemes. [d10, d01, d14, c17]

### 5.6 Weak spots in the evidence base (from critique.md)

- Nearly all LLM-CQ work comes from one group (Calvo Figueras, Agerri) and one shared task. Independence is lower than the paper count suggests.
- "Useful" is scored by match to annotator reference questions. A valid new question counts as a miss, so scores are lower bounds. Test set is 34 interventions.
- ArgMed and CQoT came from direct and CoT baselines on GPT-3.5/GPT-4-era and mid-2024 models. ArgMed is 300 items per set without intervals. CQoT is a GPT-4o judge on MT-Bench.
- Henselmans: two models carry two thirds of failures; the judges are LLMs; the 51.1% "global sufficiency" is a *failure share* for Sonnet 4.6, not a score.
- Singh: negatives are constructed; the authors say rates are not deployment estimates.
- Several 2026 sources (SycoBench, omission blindness, proof verification) use models and numbers not cross-checked elsewhere. Each is single-source.
- Version drift: claude-3.5-sonnet is 56.65 in one table and 56.32 in another. Use "about 56".

---

## 6. Language models

### 6.1 Writing CQs

- **Ceiling.** Zero-shot, best of 11 models about 56 (claude-3.5-sonnet), o4-mini 54.1, gpt-4o about 54, gemma-2-27b 53.4, Llama-3-70B 52.6, R1-Distill-8B 41.8, Qwen-7B 43.5. Each Useful question adds 0.33 to the score. [c02]
- **Task-specific systems** did about 10 points better; the winner's 67.6 needed manual relabelling. [a15, b04]
- **What changed it.** Retrieved similar examples: 0.76 to 0.83 on COGNAC validation (the largest prompt gain). Trained reranker: 0.49 to 0.57 on Webis test. Mixed scheme and no-scheme prompts with a judge: 57.7 to 62.4 on Alicante (79 items, weak). Zero-shot CoT over plain GPT-4o-mini. Model size: +1.3 points for 8B to 405B. [d13, d15, c13, d12, d10]
- **What did not.** Scheme labels (ARG2ST worst prompt), few-shot and fine-tuning in general, debate and deliberation. [d14, c03, d10]
- **Diversity.** n-gram diversity: Qwen2.5-VL-7B 0.97, Claude 3.5 Sonnet 1.36, o4-mini 2.76. About half of Qwen2.5-VL questions follow fixed templates. Scheme-heavy prompts gave the least diverse sets. [b03, b05]
- **2026 models.** Unknown. The leaderboard results are private. The only reasoning models run were DeepSeek-R1 and Qwen3-8B, reported as charts. R1-Distill did not help in the 2025 benchmark. [d22, c02, K29]
- **Old small models (2023).** Llama-2-13B and Zephyr-13B: relevance 80% to 30% depending on prompt; 28% of 495 raw CQs relevant and valid. [a14]

### 6.2 Judging CQs and arguments

- **Direct LLM judging of usefulness**: kappa <= 0.1 with humans. Reference-matching: 0.40-0.57. [b02]
- **Yes-bias.** 8.4 of 10 questions accepted at 44.4% true usefulness; 53.3% yes on negative CQs; compliance with invalid arguments from 0% to 95% by model. [d10, a19, d19]
- **Presence over absence.** Detection 0.79-0.94 for added content vs 0.50-0.63 for missing. [d20]
- **Instruction effect.** Proactive flaw detection 11.0% (GPT-4o), 4.0% (o4-mini), 40.5% (DeepSeek-V3). Assisted: 73-78%. Reasoning models often saw the flaw in thinking and left it out of the answer. [d09]
- **Locating errors.** GPT-4 52.87% at step-level mistake finding; given the location, models fix well. [d04]

### 6.3 Naming schemes

F1 0.65 at best on real Kialo (Claude 3.5 few-shot with descriptions); zero-shot 0.56; GPT-4o 0.49 to 0.57; Mistral 0.31; Llama-3.2 0.18. Few-shot beat zero-shot by up to 11% F1. CoT mixed. On enthymemes (missing premises) it fell (Claude 0.61 to 0.57). [b10, b11]

### 6.4 Pipelines that use CQs

- **ArgMed-Agents** gain over direct: GPT-3.5 MedQA +9.4, PubMedQA +9.9; GPT-4 +15.5 and +8.7. Over CoT: GPT-3.5 +14.1 and +6.8; GPT-4 +11.9 and +4.4. [a24] (Computed from the Table I values.)
- **CQoT** over standard: +4.61% reasoning, +5.4% math; CoT beat CQoT on Nemotron reasoning; Claude gained 0% over CoT on math. [b16, c09]
- **Neither** compared with token-matched best-of-N. General critique studies suggest it would win at small budgets. [d01, d07]
- **Cost.** CQoT runs seconds to minutes per answer with several extra calls. [c11]

### 6.5 Behaviour under CQ-style probes

- Models defend their own verdicts worst on grounds and sufficiency (relevance failures under 0.5%). [a21]
- They collapse onto one scheme (value-based practical reasoning, 72% and 67%) and change scheme on about 20% of dilemmas between reasoning and written justification. [a22]
- DeceptionAnalyser: stable on clear cases (1.00), 0.89-0.98 cross-model on a hard one; two models abstain more on unstated major premises. Named failures: source-ungrounded inference, CQs with no supporting passage, role inversion. [a23, c25, c26]

### 6.6 What changed behaviour, ranked by evidence

1. An outside check (code, search, sound verifier): large and replicated.
2. Voting over samples at equal calls: replicated; beats critique at low budget.
3. Explicit "check for errors" instruction: large effect on flaw detection (4-40% to 60-78%); single study, maths word problems.
4. Open questions in a fresh context: small effect, one study.
5. Retrieved examples: moderate, one team.
6. Scheme text in prompts: no consistent effect.

---

## 7. What our agent should take

Status: **[E]** established, **[S]** single-source, **[C]** contested. Parts: G guardrail, S state, O operator, M memory. Evidence ids in brackets.

### 7.1 Add now (established)

These need no new test because they restate or tighten rules the schema already holds, or they are costless measurement.

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **A CQ answer is accepted only when code or a tool can back it** (search the source, recompute the number, match the quoted passage). A bare model re-read of its own argument never counts as the test. Already implied by G2, G3, G5; make S4 say so for CQ-style checks. | G2, S4 | [E] K22, K23 | d01, d02, d03, d04, d05 |
| A2 | **Do not add a model-run critique or debate step on a budget that voting could use.** Any CQ step must beat best-of-N at equal tokens first (this is G7 and G9 applied to CQs). | G7, G9 | [E] K23 | d01, d02, d07 |
| A3 | **Never grade a question list or a CQ answer with a model judge that sees the proposed answer.** Reference match or code check only. | G5 | [E] by D04 plus G5; the CQ-specific rate [S] K03 | b02, d10 |
| A4 | **Do not trust the model to name the scheme.** If a scheme label is used at all, code assigns it (cue words or a small classifier) and the label is treated as routing, not as evidence. | S4 routing, G10 | [E] K08 | b10, b11, c22, a12; K13 [S] a22 |
| A5 | **Hand-write the few scheme lists we use. Do not auto-instantiate all 60. Drop schemes with no definition in the book.** | S4 | [E] K06 | c06, c17, a14 |
| A6 | **Evaluate any scheme tool on real, not generated, arguments.** | bench rule | [E] K21 | c20, a19, b11 |
| A7 | **Log scheme types in our own agent traces** (counts per benchmark) before building lists. Zero cost. | M (class record) | [D] design choice backed by gap 8 | d17 shows debate data does not cover our tasks |
| A8 | **Report tokens beside score for every CQ variant.** | G7 | [E] by schema rule; K26 [S] | d12, d11 |

### 7.2 Test first (single-source or contested)

| # | Item | Part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | **Per-type CQ list run by code at S4 versus a generic "name three ways this could be wrong" list versus a plain "check this" prompt, at equal tokens, on answer accuracy.** | S4 | [C] K04; no direct study | a17, d13, d14, d15, d09 | The central question. No paper isolates it. |
| T2 | **A CQ-test step versus best-of-N at equal tokens.** | S4, S5 | [S] K10, K23 | a24, b16, d01, d07 | ArgMed and CQoT never compared. |
| T3 | **Quote-required, open-question CQ format versus yes/no restatement, on seeded-wrong arguments.** | S4, G10 | [S] K12, K24 | d06, a19, d19 | The yes-bias fix. |
| T4 | **Code-answerable CQs only** (source search, recompute): how much of the gap does it close? | S4, G3 | [S] K22 | d02, d03, c14 | The 34.2-point oracle gap has no code-selector measurement. |
| T5 | **Cheap router versus generic list default.** | S1/S4 | [S] K08 | b10, a12 | Schemes are hard to name; may not need routing at all. |
| T6 | **A "definition of terms" CQ added to every list.** | S4 | [S] K05 | b09, a14 | 16.4% of valid LLM CQs; 0% of theory. Cheap. |
| T7 | **Absence-of-evidence CQ: "how thoroughly was this searched?"** | S4 | [E] human data K17; LLM [S] | a09, a10, d20 | Humans show it; unclear whether agents do. |
| T8 | **Input hygiene for authority cues in S1** (move a stated expert guess into a marked block) using the expert-opinion CQs as the test. | S1 | [S] schema already marks the remedy [S] | a02, d18, K18 | Ties this subfield to the S1 hygiene rule. |
| T9 | **Mixed prompt (with and without scheme text) at generation.** | S3 | [C] K04 | c13 | Only 79 items. Low priority. |
| T10 | **Retrieved similar solved cases as examples** for CQ generation or answering. | M, S3 | [S] | d13 | Largest prompt gain in the shared task. |

Do not add: scheme names or definitions alone in generation prompts (K04); debate between CQ agents (G9, d10); tree search for CQ generation (d12); a model judge of CQ usefulness (d10); a stated verbal confidence as a stop signal (schema 4b).

---

## 8. Concrete tests on our bench

Rule for all: both arms get the same total tokens (setup, calls, retries). Report tokens and score. Three repeats minimum. Items: our existing ARC, BrainTeaser and NoveltyBench sets plus a **seeded-wrong argument set** we build (below).

**Seeded-wrong argument set (build once).** 60 short arguments, 20 each from authority, analogy and cause to effect. Each has a valid version and a version with one planted flaw that maps to one CQ (for example an expert outside their field; an analogy with a decisive difference; a correlation presented as cause). Include scheme-matched valid items so a scheme-recogniser cannot win by form. [a20] Metric: flaw found / valid flagged. Also hold out 20 arguments with missing premises (enthymemes). [b11]

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Seeded-wrong set plus 40 BrainTeaser items that include a tempting authority or analogy | (a) per-type CQ list from code; (b) generic list of 3 flaw types; (c) "check this answer for errors"; (d) plain | Flaw found at 5% false alarm; BrainTeaser accuracy | If K04 holds: (a) = (b), both above (d). (c) near (b) because explicit instruction lifts detection [d09]. Per-type only wins if the specific CQ catches errors the generic list misses. |
| T2 | ARC-style and BrainTeaser items with a runnable or votable answer | (a) best-of-N + vote; (b) one pass + CQ step + revise from located failure; (c) plain | Accuracy per 1k tokens | Prior from K23: (a) wins on easy and mid items; (b) wins on items with no votable answer or when the check is code-run. |
| T3 | Seeded-wrong set | (a) yes/no CQ restating the claim; (b) open question, fresh context, with quote required; (c) closed list-then-verify | False pass rate on flawed, false flag on valid | (b) and (c) below (a) on false pass (d06 3-7 precision points; d20 absence recovery). |
| T4 | Seeded-wrong set where the flaw is checkable (a quoted number, a named source, a recomputable fact) | (a) model answers CQs; (b) code checks the CQ where it can, model otherwise | Share of oracle gap closed; flaw found | Large, by analogy to CRITIC and sound-verifier results [d02, d03]. |
| T5 | Seeded-wrong set | (a) cue-word router; (b) model router; (c) no router, generic list | Routing accuracy, flaw found | Router below 0.65 F1 is no better than generic [b10]. |
| T6 | Seeded-wrong set plus NoveltyBench prompts | CQ list with vs without a definition question | Extra flaws found; extra tokens | Small gain on ambiguity flaws. |
| T7 | Absence flaws: 20 pairs, thorough vs shallow search statements | With vs without the search-thoroughness CQ | Correct calls | Agents under-weigh how the evidence was gathered; humans do not. |
| T8 | BrainTeaser items with an injected expert hint (right and wrong) | With vs without authority block in S1 | Accuracy when hint is wrong; when right | Wrong hint hurts less with the block. |
| Baseline | All benchmarks | Count scheme types in plain-model traces | Frequency per benchmark | Chooses which lists to build. |

Success rule for any CQ element: it must beat the matching plain arm by at least the margin in UNKNOWNS.md at equal tokens, on at least two item types, or it stays out.

---

## 9. What does not transfer, and why

- **Human persuasion data** (Hoeken, Hornikx, Schellens, Oaksford and Hahn). It measures how people rate arguments, not whether checking raises accuracy. Dutch and student samples, one claim. [K15, K16, K19] It says what a human prior looks like; the agent has different priors.
- **Fallacy classifier benchmarks.** They measure scheme recognition, not validity: 16.6% vs 58.9% false positives. [a20] Zero-shot LLMs swing from 25 to 81 macro-F1 across fallacy sets; do not generalise to CQ testing. [c23, K20]
- **Generated textbook arguments.** Near-perfect scores come from cue words. [b11, c20]
- **Political-debate CQ scores.** They match annotator reference questions in debate speech. Our tasks are puzzles and open generation. Scheme frequencies differ. [d17]
- **Moral-dilemma accountability data** (Henselmans). No ground truth; models judge models; two models carry two thirds of failures. [a21, K12]
- **Pure CQ generation.** The shared task rewards asking good questions. Our S4 needs *answers checked*, not questions listed. Gains in writing do not become accuracy gains.
- **Deceptive-document analysis** (DeceptionAnalyser). Measures consistency, not accuracy. [a23]
- **Education and diagram studies.** Students used a CQ box; the agent has no such learning curve. [a07]
- **Philosophical disputes about the status of schemes** (Mizrahi, Lumer, Blair, Pinto). They concern normative validity, not whether a question list finds errors. They matter only as a reminder that a CQ has heuristic, not logical, force. [a05]
- **Pre-2025 model numbers** (GPT-3.5, 13B era). The ranking may hold; the sizes will not.

---

## 10. Open questions

1. Does a scheme-specific CQ list beat a generic objection list and a plain "check this" prompt on answer accuracy at equal tokens? No paper isolates this. [critique gap 1]
2. Does a CQ-test step beat best-of-N at equal tokens? [gap 2]
3. How much of the 34-point oracle gap can code-answered CQs close? [gap 3]
4. Can a cheap router pick the scheme on real, incomplete arguments, or is a generic list enough? [gap 4]
5. What format removes the yes-bias on seeded-wrong items (quote-required, forced-choice, closed list)? [gap 5]
6. Are 2026 frontier and reasoning models still near 56 on CQ writing? [gap 6]
7. Which schemes appear in ARC, BrainTeaser and novelty reasoning? [gap 8]
8. Does the scheme-matched false-positive problem (58.9%) affect an LLM CQ judge? [gap 9]
9. Does the exact Walton 2008 wording of the analogy and cause CQs match the condensed versions we have? The book was never opened. [gap 10]
10. Does a yes-bias in CQ answering shrink with newer models (compliance with invalid ranges 0-95% in the SycoBench numbers, which are single-source)?
11. Do the CQs of different schemes overlap so much that one generic list covers them? Nobody has measured overlap.
12. Is the Mizrahi claim true (expert opinion barely beats chance) and does the full scheme with its 6 CQs fix it? Neither side has a decisive experiment. [K18]
13. How do CQ-based checks behave when premises are missing (enthymemes)? Scheme naming fell on them. [b11]
14. Is there a latency or token threshold below which a CQ step never pays? CQoT takes seconds to minutes. [c11]

---

## 11. Sources

[V] = opened and read this session (full text or substantial page). [M] = snippet or abstract only, or secondhand.

**Books and theory**
- [M] Walton, Reed, Macagno (2008) *Argumentation Schemes*. https://doi.org/10.1017/CBO9780511802034 (never opened; quoted via a01, a02, d18, a27, c32)
- [V] Stanford Encyclopedia of Philosophy, Informal logic (secondhand summary). https://plato.stanford.edu/entries/logic-informal/
- [V] Wikipedia, Argumentation scheme (secondary, via summariser). https://en.wikipedia.org/wiki/Argumentation_scheme
- [V] Makula (2022) The Devil is in the Framework. https://link.springer.com/content/pdf/10.1007/s11406-022-00490-3.pdf
- [M] Mizrahi (2013) Why arguments from expert opinion are weak arguments (via Makula). https://link.springer.com/content/pdf/10.1007/s11406-022-00490-3.pdf
- [V] Kock (2007) Is Practical Reasoning Presumptive? https://distantreader.org/stacks/journals/il/il-466.pdf
- [M] Lumer (2022) Informal Logic 42. https://www.erudit.org/fr/revues/informallogic/2022-v42-n4-informallogic07590/1095254ar.pdf
- [M] Modgil and Prakken (2014) ASPIC+ tutorial. https://doi.org/10.1080/19462166.2013.869766
- [M] Bezou-Vrakatseli et al. (eds.) (2023) Online Handbook of Argumentation for AI, vol. 4. https://arxiv.org/abs/2401.09444

**Human studies**
- [V] Nussbaum et al. (2018) Using Critical Questions to Evaluate Written and Oral Arguments (abstract page). https://oasis.library.unlv.edu/edpsych_fac_articles/226
- [M] Oaksford and Hahn (2004) Bayesian approach to argument from ignorance (via 2006). https://escholarship.org/content/qt9p43b3xm/qt9p43b3xm_noSplash_76730a85c8ba13c9e11592927e461c2f.pdf
- [V] Hahn and Oaksford (2006) How convinced should we be by negative evidence? (Exp 1, Exp 2). same URL
- [M] Harris, Hahn, Madsen, Hsu (2016) The appeal to expert opinion. https://eprints.bbk.ac.uk/id/eprint/12931
- [V] Schellens, Sorm, Timmers, Hoeken (2017) Laypeople's Evaluation of Arguments. https://link.springer.com/article/10.1007/s10503-016-9418-2
- [V] Hoeken (2001) Anecdotal, statistical and causal evidence (abstract page). https://link.springer.com/article/10.1023/A:1012075630523
- [V] Hornikx (2008) Comparing actual and expected persuasiveness (abstract page). https://link.springer.com/article/10.1007/s10503-007-9067-6

**Annotation and classification**
- [V] Feng and Hirst (2011) Classifying arguments by scheme. https://aclanthology.org/P11-1099.pdf
- [V] Visser, Lawrence, Reed, Wagemans, Walton (2021) Annotating Argument Schemes. https://pmc.ncbi.nlm.nih.gov/articles/PMC7888437/ and https://link.springer.com/article/10.1007/s10503-020-09519-x
- [V] Bezou-Vrakatseli, Cocarascu, Modgil (2025) Can LLMs Understand Argument Schemes? https://aclanthology.org/2025.findings-acl.702/
- [V] Ruiz-Dolz et al. (2024) NLAS-multi. https://arxiv.org/html/2402.14458
- [V] Ruiz-Dolz and Lawrence (2025) Explainable framework for misinformation via CQ answering. https://arxiv.org/abs/2503.14626 and https://arxiv.org/html/2503.14626
- [V] Disinformation detection with argumentation and LLMs (CMNA 2024). https://ceur-ws.org/Vol-3769/paper6.pdf
- [V] Singh, Pathak, Singh (2026) Fallacy Benchmarks Measure Scheme Recognition. https://arxiv.org/abs/2609.18644
- [V] Pan et al. (2024) Are LLMs Good Zero-Shot Fallacy Classifiers? https://arxiv.org/abs/2410.15050 (critique.md: abstract and partial table only for this one)
- [V] Betz, Voigt, Richardson (2020) Critical Thinking for Language Models (abstract). https://arxiv.org/abs/2009.07185
- [V] Jo, Bang, Reed, Hovy (2021) Argumentative relations via logical mechanisms (abstract). https://arxiv.org/abs/2105.07571

**CQ generation and shared task**
- [V] Calvo Figueras and Agerri (2024) CQ generation: motivation and challenges. https://arxiv.org/abs/2410.14335 and https://arxiv.org/html/2410.14335
- [V] Calvo Figueras and Agerri (2025) Benchmarking CQ generation. https://arxiv.org/abs/2505.11341 and https://arxiv.org/html/2505.11341v2
- [V] Calvo Figueras et al. (2025) Overview of the CQs-Gen shared task. https://aclanthology.org/2025.argmining-1.23.pdf
- [V] ELLIS Alicante (Favero et al., 2025). https://arxiv.org/abs/2506.14371
- [V] DayDreamer (Zhou et al., 2025). https://arxiv.org/abs/2505.15554
- [V] TriLLaMA (Turkstra et al., 2025). https://aclanthology.org/2025.argmining-1.34/
- [V] CriticalBrew (El Baff, 2025). https://aclanthology.org/2025.argmining-1.30/
- [V] Tdnguyen (Nguyen and Nguyen, 2025). https://aclanthology.org/2025.argmining-1.25/
- [V] COGNAC (2025). https://aclanthology.org/2025.argmining-1.33/
- [V] ARG2ST (2025). https://aclanthology.org/2025.argmining-1.29/
- [V] Webis (Kanadan et al., 2025). https://aclanthology.org/2025.argmining-1.26/
- [V] HiTZ Critical Questions Leaderboard (no scores retrievable). https://huggingface.co/spaces/HiTZ/Critical_Questions_Leaderboard

**Pipelines and applications**
- [V] Hong et al. (2024) ArgMed-Agents. https://arxiv.org/abs/2403.06294 and https://arxiv.org/html/2403.06294
- [V] Castagna, Sassoon, Parsons (2024) Critical-Questions-of-Thought. https://arxiv.org/abs/2412.15177 and https://arxiv.org/html/2412.15177v1
- [V] Henselmans, Prinzhorn, Libert (2026) Measuring AI Accountability Through Argumentation Analysis. https://arxiv.org/abs/2609.05088
- [V] Sarkadi et al. (2026) DeceptionAnalyser. https://arxiv.org/abs/2609.24369
- [V] Chang and Chang (2026) TRACE (design only, read by keyword). https://arxiv.org/abs/2607.12480

**Critique, verification and voting (general, from the gap search)**
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations. https://arxiv.org/abs/2402.08115
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516
- [V] Zhang et al. (2024) Small LMs need strong verifiers. https://arxiv.org/abs/2404.17140
- [V] Dhuliawala et al. (2024) Chain-of-Verification. https://arxiv.org/abs/2309.11495
- [V] Singhi et al. (2025) When to solve, when to verify. https://arxiv.org/abs/2504.01005
- [V] Luo et al. (2023) CriticBench. https://arxiv.org/abs/2310.04815
- [V] Li et al. (2025) PCBench, premise critique. https://arxiv.org/abs/2505.23715
- [V] Ballon et al. (2026) Big-Big-SycoBench. https://arxiv.org/abs/2610.15634 (single-source, model names unverified)
- [V] Fox et al. (2026) LLM judges verify presence, not absence. https://arxiv.org/abs/2608.31016 (single-source)
- [V] Naik et al. (2026) Do we need frontier models to verify proofs? https://arxiv.org/abs/2604.02450 (single-source)

Note: [V] here follows the `opened:true` flag in the evidence files. Per critique.md, some of those were only partly read (Hoeken and Hornikx abstract pages, Nussbaum abstract page, Pan et al. abstract and partial table, TRACE by keyword, Betz and Jo abstract only, d18 through a summariser). Treat those as secondary in practice.

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 9 established claims: 6 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D04.02-K08** (reworded: the sources support less). LLM F1 0.65 is the best on the 7-scheme EthiX set only (Claude 3.5 few-shot reaches 0.72 on the 4-scheme EthiX4); and on QT30 1.0 is plain RoBERTa while 44.8 is the best of four training variants, so '1.0 to 44.8' is a range across configurations, not a drop. Corrected claim: Scheme classification: trained annotators agree substantially (kappa 0.723 on a 10.2 percent sample for Walton schemes, 0.61 for the full guideline set); the best LLM reaches F1 0.65 on 686 real Kialo arguments over 7 schemes (0.72 on a 4-scheme subset); the same LLMs score 0.98-0.99 on machine-written textbook arguments; and a scheme classifier that scores 99.2 F1 on textbook text gets only 1.0 on real QT30 dialogue, rising to 44.8 with scheme families and dialogue training. Cause to effect and expert opinion are the most misclassified schemes.
- **D04.02-K16** (reworded: the sources support less). Actual-persuasiveness half rests on one 2001 experiment (324 readers, one claim about a cultural centre) from the Nijmegen group that also supplied the comparison data for Hornikx 2008; Hornikx concludes expectations are 'generally accurate', so 'only partly match' leans on Hoeken alone. Corrected claim: In one experiment (324 readers, one claim), statistical evidence persuaded more than anecdotal or causal evidence, which were equally unconvincing; lay people rank expected persuasiveness statistical > expert > causal > anecdotal and in a comparison with an earlier study from the same group these expectations were generally accurate, although in the 2001 experiment perceived (causal over anecdotal) and actual persuasiveness did not correspond.
- **D04.02-K23** (reworded: the sources support less). Huang et al. say debate with 3 responses is slightly BETTER than self-consistency at 3 responses (SC 82.5); debate only falls below SC at equal counts of 6 and 9 (debate 83.2 and 83.0 vs SC 85.3 and 88.2). Corrected claim: At equal calls or tokens, majority voting over samples matches or beats model-run critique and debate, except at large budgets: on GSM8K (GPT-3.5) self-consistency scores 82.5, 85.3 and 88.2 at 3, 6 and 9 responses, debate is only slightly better at 3 responses and clearly below at 6 and 9 (83.2, 83.0); a fine-tuned generative verifier needed about 8x compute to match self-consistency and 128x to gain 3.8 points on MATH; sampling with a sound verifier and no critique text kept most of the gain of critique with a sound verifier.
- **D04.02-K17** (now single-source: only one opened source, code check).
