# Fallacy theory: deep document

*Subfield D04.03. Focus: recognised error types (Hamblin; Walton). Link to schema: S1 input hygiene, where appeals to authority and stated guesses go in a marked block. Built from evidence_a-d.jsonl (a01-a30, b01-b27, c01-c26, d01-d18), claims.jsonl (K01-K29) and critique.md in this folder. Written 2026-11-03.*

*Reading note.* The theory side was read through the Stanford Encyclopedia of Philosophy (SEP), not through Hamblin 1970, Walton 1995 or van Eemeren and Grootendorst. The classic human studies on Bayesian fallacy theory (Hahn and Oaksford 2007; Harris, Hsu and Madsen 2012) were paywalled and not opened. Every LLM number below comes from a paper opened in full text. Many 2026 LLM papers are single-source.

## 1. What it is

A fallacy, in the standard definition, is an argument that seems valid but is not (a01). The definition has three parts: an argument, invalidity, and the appearance of validity. Fallacy theory asks four things:

1. What counts as a fallacy? (Form only? Use in a dialogue? Probability?)
2. Which error types are there, and can they be told apart reliably?
3. How do real people judge them?
4. Can machines detect them, and are machines fooled by them?

For our agent the practical question is narrow. Input often holds material that pushes toward an answer without being part of the task: an appeal to authority ("experts agree"), a stated guess ("I think it is B"), loaded wording, a flattering label. Schema state S1 says code moves such material into a marked block. This document asks what fallacy theory and the LLM studies say about how to build, test and limit that step.

Short answer from the evidence:

- Fallacy labels are context-dependent and noisy. A label cannot be assigned by form alone (K01, K02, K07).
- LLMs are weak at fine-grained labels and over-flag sound arguments that look like fallacies (K08, K21, K26).
- LLMs are moved by fallacious and authority-based pressure, and the effect differs by type (K14, K15, K16, K28).
- No study tests what S1 needs: does a marked block for authority and guess cues change final answer accuracy at equal tokens? That gap is still open (critique GAPS 1).

## 2. History and theories in depth

### 2.1 Hamblin and the standard treatment (a01, a02)

Before 1970, textbooks (Copi 1961 is the SEP's example) listed named fallacies under the standard definition. Hamblin's 1970 book *Fallacies* was the first modern book-length attack on this "standard treatment". The definition and the textbook practice did not fit: many listed fallacies are not invalid by form, and the appearance condition is vague (to whom does it seem valid?). The era of modern fallacy studies starts in the 1970s (a01).

Massey (1981) added the asymmetry thesis. You can show validity by pointing to a valid form. You cannot show invalidity by pointing to an invalid form, because there is no systematic theory of invalidity. So under the standard definition no argument can be convicted of being a fallacy (a02). This is the core reason a form-matching detector is the wrong design. The defect must be named in the support relation, not read from the surface.

### 2.2 Woods and Walton: methodological pluralism (a03)

Woods and Walton (1989; Woods 1992) said formal logic is too coarse for most fallacies. They matched each fallacy to the logic that fits it, for example inductive logic for hasty generalization and post hoc, relatedness logic for ignoratio elenchi, plausible-reasoning theory for ad verecundiam-type cases (four pairings in the SEP). Lesson: "is it valid?" is the wrong single question. Each error type needs its own kind of check.

### 2.3 Walton: pragmatic theory and dialogue types (a04)

Walton (1995) judges an argument inside a type of dialogue: persuasion, inquiry, negotiation, eristic and others (seven types in Walton and Krabbe 1995 and Walton 2007). In 1995 he said a fallacy occurs at an illicit shift from one dialogue type to another. He later moved toward judging a move against the goal and rules of the current dialogue. Consequence: the same move can be sound in one dialogue type and a fallacy in another. In eristic dialogue (a quarrel), threats and insults can be permissible (a04).

Walton also built argumentation schemes, each with critical questions. Argument from expert opinion has questions such as "is the expert in the right field?" and "is the expert trustworthy?". An instance that answers the questions is sound. One that does not is a fallacy. This is the basis of the scheme-matched negatives (d05-d08) and the critical-question dataset (d03). Note: the scheme-and-question books were not opened by us.

### 2.4 Pragma-dialectics (a05)

Van Eemeren and Grootendorst (1984, 1992, 2004): a fallacy is any violation of one of ten rules for a critical discussion across four stages (confrontation, opening, argumentation, concluding). In the 2004 text every rule violation is a fallacy (a05). This is the most operational theory: the rules can be written into a prompt. The results of doing so are mixed (section 6).

### 2.5 Experimental support for the rule view (a06, a07)

Van Eemeren, Meuffels and Verburg (2000) and the ISSA 2002 report: ordinary arguers rate rule-violating moves lower than sound ones. Seven-point scale (1 very unreasonable, 7 very reasonable). Ad hominem fragments: fallacious 3.75 vs sound 5.29. Replication (24 respondents, 24 items): fallacies 3.43 vs sound 5.27. Within ad hominem: tu quoque 3.82, circumstantial 3.47, abusive 2.99 (a06). Proposition type (descriptive, evaluative, inciting) had no significant effect (75 respondents, 72 fragments). Spanish replications (n=47 and n=29) found the same direction (fallacies 3.54 vs sound 4.97) with some differences in size (a07). The effect is real but moderate: a gap of about 1.5 scale points.

### 2.6 The Bayesian rival (a08-a13)

Hahn and Oaksford (2007) hold that argument strength is a probability that depends on prior belief in the claim, the evidence and rival hypotheses. Slippery slope, circularity and argument from ignorance are then not always weak; strength depends on priors, evidence polarity and source reliability (a10). Corner et al. (2011), summarised in a08: similar items drove acceptance of the next item in slippery-slope tasks, dissimilar items did not. Boongaling (2016) comments that the Bayesian strength of slippery slope and ad hominem depends on priors, while the traditional view calls such arguments defective by form (a09). Bayindir, Hahn and Oaksford (2005) tested argument from ignorance directly (a11-a13). The burden-of-proof dispute (a13): pragma-dialectics calls "Ghosts exist because nobody proved they don't" fallacious because it shifts the burden of proof; the Bayesian view asks how informative the lack of evidence is.

### 2.7 Computational turn (2017 onward)

- Argotario (Habernal et al. 2017): a game that collects fallacy examples with crowd grading; types: ad hominem, appeal to emotion, red herring, hasty generalization, irrelevant authority, plus non-fallacious (c24).
- Habernal et al. 2018: ad hominem in Reddit Change My View (b07, b08, c23).
- Goffredo et al. 2022: fallacies in US presidential debates (b09).
- LOGIC (Jin et al. 2022): first multi-type benchmark (a14).
- MAFALDA (Helwe et al. 2024): unified taxonomy with disjunctive labels (a16).
- Singh et al. 2026: benchmarks mostly measure scheme or source type, not fallacy (a20).

## 3. Core findings with exact numbers

Status: E established (several sources or verified), S single-source, C contested. A lab that produced several of the sources counts as one.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Standard definition has three conditions; Hamblin broke the textbook treatment | none | a01 | E |
| Massey: no theory of invalidity, so form alone cannot convict | none | a02 | E |
| Fallacy depends on dialogue type (Walton) and on 10 rules, 4 stages (pragma-dialectics) | 7 dialogue types; 10 rules | a03-a05 | E |
| Lay readers rate ad hominem fallacies lower than sound ones | 3.75 vs 5.29; replication 3.43 vs 5.27 (7-point scale); tu quoque 3.82, circumstantial 3.47, abusive 2.99 | a06 | E |
| Proposition type does not change ratings; Spanish replications same direction | N=75 (72 fragments); Spain 3.54 vs 4.97, n=47 and n=29 | a07 | E |
| Bayesian: source reliability has the largest effect on argument from ignorance | reliability 5.58 vs 3.21, F(1,72)=198.63, p<.0001; polarity 4.53 vs 4.27, F=11.58, p=.001; prior 4.47 vs 4.32, F=5.96; N=73 | a11 | S (one lab) |
| Bayesian structural variants: opposite-polarity negative evidence differs from 0 | m=3.36, t(71)=9.16, N=72 | a12 | S |
| Fine-tuned encoders beat zero-shot on LOGIC (13 types, 2,449 items) | micro-F1: random 12.02, GPT-3 12.20, GPT-2 13.67, RoBERTa-MNLI 12.22, BERT 45.80, DeBERTa 50.29, Electra 53.31; range 8.62-53.31 over 12 models | a14, b01, c01 | S (one paper, verified) |
| Structure-aware classifier helps | Electra-StructAware 58.77 vs 53.31 (+5.46); exact match 47.67% (+12.01); raw premise + structured hypothesis 56.72; structured premise + raw hypothesis 44.56 | b02, c02 | S |
| Detectors transfer badly | LOGICCLIMATE (1,079 items) Electra 22.72 F1; Sourati in-domain coarse 82.7, fine 62.7, out of domain coarse 46-57, fine about 24; CoCoLoFa models lose 0.05-0.13 F1 elsewhere, others score 0.09-0.19 on it | a14, a15, a28, c02, c03 | E |
| BIG-bench binary detection is easy | NLI-Electra 0.995, instance-based 0.997, random 0.499 | a15 | S |
| Zero-shot LLMs weak on fine labels | MAFALDA span-F1 levels 0/1/2: GPT-3.5 0.627/0.201/0.138; human 0.749/0.352/0.186; random 0.435/0.061/0.010; Zephyr 0.524/0.192/0.098 | a16, b05, c07 | E |
| MAFALDA labels are ambiguous | 28% of 203 spans have 2+ valid labels; single human annotators as gold: level-0 F1 0.616-0.696, level-2 F1 0.093-0.144 | b06, c07, c08 | E |
| GPT-4 vs fine-tuned T5 depends on dataset | Argotario 78.94 vs 83.20 (T5-3B); Reddit 79.10 vs 80.42 (T5-large); MAFALDA 48.38 / 49.78; LOGIC macro-F1 0.28 (Jeong) | a17, c09, c26 | E |
| Multi-round prompting helps most runs | better in 83.7% of experiments; mean gains 1.63 (GPT-4), 2.46 (GPT-3.5), 4.95 (Qwen2.5-14B), 3.67 (Qwen2.5-7B); range +1.27 to +7.54; failure rate 12.27% (warm-up) vs 15.09% (zero-shot CoT) | a17, b12, b13, c10 | S (one group) |
| Multi-round scheme ranking | average rank: warm-up analysis 4.13, CoT 4.33, analysis 4.35, with definitions 4.65, definition generation 4.77, without definitions 4.90, premises and conclusion 5.84 | c10 | S |
| Prompt Ranking (counterargument, explanation, goal) | gpt-3.5 macro-F1: Argotario 0.41 to 0.69, Covid-19 0.14 to 0.56, Climate 0.13 to 0.58, Logic 0.25 to 0.32; gpt-4 Argotario acc/F1 0.81/0.80 to 0.84/0.83, Covid accuracy 0.93 to 0.86 | a18, b15, c11 | C |
| Definitions/rules in prompt: mixed | textbook PD set, no rules to rules: GPT-3.5 0.30 to 0.12, GPT-4 0.49 to 0.43, GPT-4o 0.13 to 0.39; CoT: GPT-3.5 0.60, GPT-4 0.63, GPT-4o 0.86; DEF baseline small uneven gains | b11, c13 | C |
| Logical-structure tree in prompt | GPT-3.5 Reddit 65.29 to 70.76, LOGIC 42.28 to 47.99, Argotario 57.46 to 59.67; Llama-2 LOGIC 69.36 to 74.16; Flan-T5 69.23 to 73.49 | b14, c15, c16 | E (Lei and Huang plus Jin) |
| Taxonomy prompts do not beat the base prompt; extra context does not help | Qwen-3 8B accuracy text/context/+audio: base 51/49/46, PD 53/49/46, periodic table 44/45/25; slippery slope recall 5%; Walton-scheme set 5-class macro-F1: GPT-4 51.7 to 50.8 with context, GPT-3.5 45.5 to 35.8, RoBERTa 66.5 to 59.9 | c17, c18, b10 | C |
| LLM detectors over-flag and miss | GPT-4 N=780: accuracy 0.79, macro-F1 0.71; 95 None; without None accuracy 0.90, F1 0.88; Prolog rule helped naming | b21, c19-c21 | E |
| Sound look-alikes are flagged | fine-tuned ModernBERT 16.6% native vs 58.9% matched; RoBERTa 19.7% to 70.3%; Reddit-trained 5.7% to 62.0%; Argotario authority 78.8% vs 11.7% | a20, d05, d06, d08 | S |
| Zero-shot LLMs show it too, prompt dependent | native-to-matched gap: Sonnet 5 +13.5 pp, Haiku 4.5 +12.6, Qwen3.6-27B +0.5; binary prompt reverses it (-7.7, -33.2, -25.6); naming a type keeps it (+31.0, +45.6, +25.5) | d07 | S |
| Annotator agreement is low where false positives are decided | 86.3% agreement (kappa 0.74, AC1 0.82) overall; specific agreement 0.50 on matched valid class; 12 of 237 CoCoLoFa comments (5.1%) valid | d15, d14 | S |
| Fallacies are rare in real debate | 0.2% of CMV posts ad hominem (3,866 args; 3,396 threads) vs 19.5% on news sites; kappa 0.79; upper bound accuracy 0.878; controversy predicts ad hominem (human 0.804, CNN-LDA 0.569) | b07, b08, c23 | S |
| LLMs are convinced by fallacious arguments | GPT-3.5 37% vs 29%; GPT-4 67% vs 37% (200 claims x 3 runs); all three runs: 17% vs 10% and 56% vs 37%; helper ablation 17.66/10.5 and 28/0.83; debater flips 16.13% / 20.25% | a21, b03, b04, c05, c06 | S |
| Robustness rises with scale and varies by type | LFR@3 Llama-3.1 59.75 / 70.38 / 77.17 (8B/70B/405B); 405B equivocation 29.4%, straw man 57.0%; authority GPT-4 39.20, GPT-3.5 22.54; CoT +7 to +13% except authority -1.87% | a24, b19, b20, d10, d11 | S |
| 2026 models: resisting invalid pressure and accepting valid criticism trade off | invalid compliance 0.15% to 94.6%; valid responsiveness 32% to 95%; Opus 5.5 1/32; GPT-6 Astra 0/88 | a25, d09 | S |
| Source labels bias human judgement of fallacies | N=505; Human label 3.35, Human+AI 3.37, vs Control 2.40, AI 2.53 (5-point) | b16 | S |
| Emotional framing lowers HUMAN detection | human macro-F1 0.380-0.533 vs 0.563 (-14.5%); labelled fallacious 91% to 86%; 1,000 arguments | a22, b17, d13 | S |
| Critical-question gate improves judge scores | +4.61% reasoning, +5.4% math headline; Llama-3.1-70B reasoning 8.05 / 8.3 / 8.4, math 8.95 / 9.25 / 9.55 (plain / plan+answer / full); Nemotron-51B reasoning 6.75 / 6.85 / 7.3 | d01, d02 | S |
| Zero-shot LLM biased to say yes on critical questions | GPT-4 wrong on 53.3% of true-No; RoBERTa wrong on 27.8% | d03 | S |
| Humans vs LLMs in ad hominem dialogue | humans logical 59%, ethotic counter 32%, undercutter 9%; LLMs logical 67-76%, ethotic 15-17% | a29 | S |
| LLMs produce fallacies too | Talk2AI: 17% of user and 14.5% of LLM quips (DistilBERT classifier; 770 people, 3,080 conversations, >60,000 turns) | a26, b18, d16 | S |
| Trap questions are hard | RuozhiBench: best 62.00 (Claude-3-haiku), Mixtral-8x22B 58.99, Llama-3.1-70B 57.78; humans >90% (677 questions, 17 LLMs) | a23, b23, c22 | E |
| Refusal to write fallacies depends on framing | 23,990 generations; 11-point range over claims; frame swings about 100 points; fallacy type swings over 80 | a30 | S |
| Training on fallacy data helps or hurts | LFUD (4,020 instances): LogiQA2.0 +5.16%, Reclor +6.36% (LLaMA2-13B), TaxiNLI +7.53%, FOLIO +7.16%, Vicuna-13B FOLIO +21.35%; adding LOGIC data cut TaxiNLI 68.54 to 40.60 | a19, b22, c14 | S, out of scope |
| LLM tutor for fallacies | N=20, p<0.05 and p<0.01, about 8.4% automatic gain | b24 | S, too small |
| Formal verification of explanations | over 90% of outputs translate into Lean4 chains that pass; agreement with human labels about 20% on LOGIC-Climate | a27 | S |

## 4. Mechanisms and models

This section turns the findings into parts an engineer can build.

### 4.1 The label is a claim about a support relation, not a surface pattern

Massey (a02) plus Singh et al. (a20, d05-d08) give one design rule. A detector that sees "an expert says so" and returns "appeal to authority" is matching a scheme. The error is present only if a critical question fails (the person is not an expert in this field, experts disagree, the claim is outside their field). Implementation:

1. Extract the scheme (authority, consensus, analogy, cause, ignorance, slippery slope).
2. Ask the scheme's critical questions (3 to 6 per scheme) one at a time.
3. A flag needs a named failed question. No named failed question means no flag.

Evidence for the parts: structure first (b02, b14), critical-question gate (d01, d02). Evidence for caution: a zero-shot LLM answers critical questions with a yes-bias (d03), and about half of CQoT's gain remained without the questions (d02).

### 4.2 Two-stage check: binary first, type second

From d07: the binary question "is this argument flawed?" reversed the scheme-tracking gap (-7.7, -33.2, -25.6 pp), while asking for a type kept it (+31.0, +45.6, +25.5 pp). Sourati et al. use detect, then coarse class, then fine class (a15); binary detection is easy (F1 about 0.98-0.997) and fine class is hard. Design: ask the binary question first with no type names in the prompt; only after a positive, ask which question fails.

### 4.3 Marked block for suggestive material (S1)

What goes in the block, and what to record per entry:

- Appeal to authority or consensus: who, claimed field, and whether competence was checked. Not just "an authority is cited".
- Stated guess or preferred answer ("I think it is B"): a hint with no weight.
- Loaded wording: keep the original beside a neutral rewrite (open: does the rewrite help an LLM, d13).
- Source label (human or AI written): strip before judging (b16).

Why code does it and not the model: models follow invalid pressure at rates from 0.15% to 94.6% (a25, d09), are weak against authority cues (d10), and GPT-4 was persuaded 67% of the time by fallacies (b03). A code-side move does not rely on the model's resistance. Whether the move improves accuracy is untested.

### 4.4 Pressure test with both argument types

d09: resisting invalid arguments and accepting valid ones are separable and trade off (one model: 1% invalid compliance, 32% valid responsiveness). A guard that only cuts compliance can make the agent stubborn. Report both rates.

### 4.5 Base-rate threshold

Fallacies are rare in real argument (0.2% of CMV posts, b07) but dense in benchmarks, and benchmark valid classes hold few sound look-alikes (a20). Set the flag threshold from the expected rate in our own item stream, and measure false positives on sound look-alikes, not only recall (K21).

### 4.6 Uncertain bucket

With 28% multi-label spans (c07) and 0.50 specific agreement on matched valid arguments (d15), a three-way output (flag, clear, uncertain) fits the labels better than a forced binary. Uncertain means: keep the cue in the marked block, give it no weight.

### 4.7 Persuasion-resistance loop (testing only)

LOGICOM (c25) is an agent loop: a persuader plus a separate fallacy-writing helper, debate rounds, and an agree/disagree readout, repeated three times per claim. A long fallacy prompt in the persuader distracted it, which is why a helper agent was added. The same loop can be used on our agent as an attack harness.

## 5. What holds up

### 5.1 Holds up

- Fallacy labels are context-dependent; the form-only view fails (a01-a05), with human rating work as support (a06, a07).
- Fine-grained LLM labelling is poor and dataset-dependent (a16, a17, c09, c26).
- Detectors transfer badly across datasets (a14, a15, a28; three sources).
- Benchmark labels are noisy (b06, c07, c08, d15).
- Explicit argument structure helps classification (b02, b14, c15; two groups).
- LLM detectors have high false-positive rates (b21, c19, d06).
- Trap questions with deceptive premises are hard (a23, b23, c22).

### 5.2 Single-source or contested

- LLMs convinced by fallacies: LOGICOM, one study of 200 claims, no confidence intervals, no independent replication (d12). LoFa is a related design with no logical-argument control.
- Multi-round prompting: one group (Pan et al.). No token counts and no self-consistency baseline (d17).
- Prompt aids (definitions, rules, counterargument queries) help some models and hurt others (K11). No stable recipe.
- Theory taxonomies: null in c17, rules matter for some models in b11. Contested.
- Bayesian reading: one research lineage; originals not opened.
- Sycophancy and LoFa numbers rest on API calls that cannot be reproduced exactly.

### 5.3 Failures and corrections

- Jin et al. GPT-3 row: F1 12.20 (precision and recall 12.00). An earlier note said 12.00 F1. Corrected.
- The 14.5% drop under emotional framing is for human annotators, not LLMs (d13). The earlier claim was wrong.
- The 12.27/15.09 failure rates in Pan et al. compare the warm-up scheme with zero-shot CoT, not with and without definitions.
- Pan et al. and Helwe et al. report different macro-F1 for GPT-3.5 on MAFALDA. Metrics differ; do not mix them.
- LoFa's -1.87% for CoT on appeal to authority is one GPT-4/NQ1 comparison. It means no benefit, not proven harm (d11).
- "Low F1" can mean ambiguous labels, not a bad model (K07).
- Published false-positive rates look low because valid classes hold few sound look-alikes (d05).

### 5.4 Moderators

- Model scale: Llama-3.1 8B to 405B raises LFR@3 from 59.75 to 77.17 (b19). In RuozhiBench larger beats smaller within every series (c22). In MAFALDA size did not predict accuracy (LLaMA2 7B beat 13B at levels 0 and 1, b06).
- Fallacy type: appeal to authority and equivocation weakest (LoFa); appeal to emotion hardest in MAFALDA (b06); slippery slope recall 5% in the base prompt (c18); ad hominem F1 81/77/78 across input conditions (c18).
- Dataset: scores vary more by dataset than by model (c26).
- Prompt framing: binary vs type-naming prompt shifts false-positive behaviour by tens of points (d07). One frame change swings refusal to generate fallacies by about 100 points (a30).
- Source cue: human-written label raises perceived logic of fallacious comments (3.35 vs 2.40; b16).
- Topic controversy predicts ad hominem (b08).

### 5.5 Interventions that worked

- Structure tree or logical-form hypothesis (b02, b14).
- Warm-up round and zero-shot CoT for classification (c10), +1.27 to +7.54 macro-F1.
- Prolog rule given to the model (c20).
- CoT as a defence for most fallacy types (+7 to +13%, d11).
- Critical-question gate on reasoning (d01), about +5%, half from added structure (d02).

### 5.6 Interventions that did not work, or hurt

- Extra context or audio (c17, b10).
- Theory taxonomies over the base prompt (c17).
- Rules in the prompt for GPT-3.5 (0.30 to 0.12, b11).
- Prompt Ranking for gpt-4 on some sets (Covid accuracy 0.93 to 0.86, b15).
- Few-shot for models other than GPT-4 (b13).
- CoT on appeal to authority in one comparison (-1.87%).
- Adding LOGIC data in fine-tuning (TaxiNLI 68.54 to 40.60).
- Direct prompting at level 1 of MAFALDA (no difference, c08).

## 6. Language models

### 6.1 Classifying fallacies

| Setting | Result |
|---|---|
| LOGIC, zero-shot GPT-3, MNLI models | at random level, 12.0-13.7 vs 12.02 (a14) |
| LOGIC, fine-tuned | 45.80-53.31; structure-aware 58.77 (a14, c02) |
| MAFALDA, GPT-3.5 span-F1 | 0.627 / 0.201 / 0.138 (levels 0/1/2); humans 0.749 / 0.352 / 0.186 (a16) |
| MAFALDA, GPT-4 macro-F1 | 48.38 informal, 49.78 formal definition (a17) |
| Argotario, Reddit GPT-4 | 78.94, 79.10 vs T5 83.20, 80.42 (a17) |
| Out of distribution | LLMs beat fine-tuned T5 in all out-of-distribution tests (c09) |
| GPT-4 on 7 fallacies (N=780) | accuracy 0.79; 0.90 after removing 95 None outputs (b21) |
| Walton-scheme validation set, 5-class macro-F1 | GPT-4 51.7, GPT-3.5 45.5, RoBERTa 66.5, eSVM 60.3 (b10) |
| Subtle real Reddit posts (502) | every model over-flagged; Prolog rule helped naming; long free reasoning hurt detection (c19, c20) |

What changed results: explicit structure (+5 points on several sets), a warm-up round (+1.27 to +7.54 macro-F1), a formal rule (class scores up), counterargument/explanation/goal ranking (large for gpt-3.5, small or negative for gpt-4). What did not: extra context, taxonomy prompts.

### 6.2 False positives on sound arguments

Fine-tuned encoders flag 58.9-70.3% of sound scheme-matched arguments vs 16.6-19.7% native. Zero-shot Sonnet 5, Haiku 4.5 and Qwen3.6-27B follow the scheme too, with gaps of +13.5, +12.6 and +0.5 pp under the baseline prompt; a binary prompt cuts the gap and reverses it (d07). The authority scheme is the worst case (78.8% vs 11.7% on Argotario, d08). This is the direct risk for an S1 block that marks every cited source.

### 6.3 Being persuaded by fallacies

- LOGICOM: GPT-4 convinced on 67% of claims by a fallacious persuader vs 37% by a logical one; GPT-3.5 37% vs 29%. Debater flips from disagree to agree: 16.13% (GPT-3.5), 20.25% (GPT-4). Helper ablation: claims won only with a logical helper vs only with a fallacious one, GPT-4 28% vs 0.83% (b03, b04).
- LoFa: Llama-3.1 resistance rises with scale. Weakest against equivocation (405B: 29.4%) and appeal to authority (GPT-4 39.20%, GPT-3.5 22.54%). API tests were May-July 2025, so no 2026 release was tested (d10).
- Big-Big-SycoBench (2026 models): following invalid arguments 0.15% to 94.6%. Examples: GLM-5.3 9.1%, Kimi K3 13.3%, Grok 4.7 19.7%, GPT-5.5 21.9%, GPT-5.6 Terra 28.3%, GPT-5.6 Luna 37.7%. Invalid/valid pairs: GPT-6 Astra 0/88, Opus 5.5 1/32 (100-artefact subset), GLM-5.3 9/77, Kimi K3 13/76, Grok 4.7 20/89, GPT-5.5 22/92 (a25, d09).
- RuozhiBench: best model 62% vs humans over 90% (a23).
- Humans show source bias too (b16), so the model partly copies a human bias.

### 6.4 How LLMs argue and what they produce

LLM defences are more logical and less ethotic than humans' (a29). Talk2AI found fallacies in 14.5% of LLM quips vs 17% of user quips, using a DistilBERT classifier of the type that over-flags (d06, d16). That rate is not a measurement of fallacies in reasoning chains.

### 6.5 Checks built on critical questions

CQoT (d01) made the model draft a plan and check it against 8 critical questions (premises stated, premises supported, logical link and others). Gain: +4.74% reasoning and +5.71% math over plain, +4.48% and +5.09% over CoT (LLM-judge scores, five models). Ablation: removing the question stages kept most of the gain (Llama-3.1-70B reasoning 8.05 / 8.3 / 8.4). No token match. GPT-4 asked Walton critical questions says yes to 53.3% of true-no items (d03), so any gate needs wording that forces a reason for each "no".

### 6.6 Not in our scope

Training on fallacy data (LFUD, LOGIC) shows mixed gains (b22). ForEx (Lean4 verification of explanations) agrees with human labels about 20% (a27). Fallacy tutoring (LFTutor, N=20) is too small (b24).

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Never label a fallacy by surface form. A flag must name the failed support question (field, evidence, relevance). The marked block stores the check result, not just the presence of a cue. | S1 | [E] | a01, a02, a04, d05-d08; K01, K02, K26 |
| A2 | Keep the cue in the marked block with its original wording; do not delete it. Give it no weight in the answer. | S1 | [E] for the risk (LLMs follow pressure), [S] for the benefit of the fix | a25, d09, b03, b16; K15 |
| A3 | Prefer coarse flags (cue present or not; authority / guess / consensus) over fine fallacy names. | S1 | [E] | a16, b06, c07, a17; K08 |
| A4 | Report false positives on sound look-alikes, not only recall, in any S1 evaluation. | G7 | [E] | b21, c19, d05, d06; K21 |
| A5 | Extract premises and conclusion before judging a cue (structure first). | S1 | [E] for classification; not yet shown for final answers | b02, b14, c15; K12 |
| A6 | Do not tune the check on one label set; test on at least two datasets with different style. | G3 | [E] | a14, a15, a28; K06 |
| A7 | Keep an "uncertain" outcome; the cue stays in the block without weight. | S1 | [E] for label ambiguity | b06, c07, d15; K07, K29 |
| A8 | Set flag thresholds from base rates in our own item stream, not benchmark density. | S1 | [E] as a rule; [S] for the rate | b07, a20; K19 |
| A9 | Do not add: pragma-dialectic rule lists, a "periodic table" taxonomy, or extra context in the check prompt. | 4b | [C] (null in c17, mixed in b11) | c17, b11, c13; K11, K18 |
| A10 | Do not use a debate or persuader loop as a production check (G9). Use LOGICOM-style loops only as an attack harness in tests. | G9 | [E] | c25; schema G9 |

### Test first

| # | Item | Part | Status | Evidence | Why not "add now" |
|---|---|---|---|---|---|
| T1 | Authority and guess cues in a marked block vs inline: effect on final accuracy | S1 | [S] | d09, d10, b03 | No direct test exists (GAPS 1). |
| T2 | Binary "is it flawed?" prompt before any type naming | S1 | [S] | d07 | One paper, three models. |
| T3 | Critical-question gate in S8 VERIFY | S8 | [S] | d01, d02, d03 | Not token-matched; half of gain from structure. |
| T4 | Source-label stripping before judging | S1 | [S] | b16 | Human study only. |
| T5 | Neutralising loaded wording before checking | S1 | [S] | a22, d13 | Human annotators only. |
| T6 | Two-round (warm-up) fallacy check vs self-consistency | S1 | [S] | a17, b13, d17 | No token counts. |
| T7 | Persuasion-pressure test with matched valid arguments | G | [S] | d09, b03 | Two-sided metric needed. |
| T8 | Dialogue-type tag lowers false positives | S1 | [S] (theory only) | a04, d07 | Nobody tested it. |
| T9 | Self-audit of the agent's own reasoning for fallacious steps | S8/S9 | [S] | a26, d16 | The 14.5% was not measured on reasoning chains. |
| T10 | Bayesian source weighting: confidence shifts with source reliability | S1 | [S] | a11 | One lab, 2005, human data. |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup cost counted, G7). Report accuracy with a 95% interval, at least 3 seeds, and a per-type split.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Existing reasoning items with injected suggestive cues: a wrong stated guess, a fake expert quote, a "most people say" line. 300 items, three cue types | (a) cue inline; (b) cue in the S1 marked block with a competence check; (c) cue stripped by code (ceiling) | final accuracy; drop from clean | Block recovers part of the drop; stripped is the ceiling. Add if (b) beats (a) by at least 3 points with a CI excluding 0. Size of effect is a guess. |
| B2 | Same items with sound expert cues (right expert, right field, correct answer) | same arms | accuracy; false-flag rate | The check must not lower accuracy on sound cues by more than 1 point (mirrors d05-d08). |
| B3 | Scheme Foils: matched fallacious vs matched sound arguments of the same scheme (authority, cause, analogy; 40 each) | (a) one-shot "name the fallacy"; (b) binary first, then critical question; (c) critical-question gate with a forced reason for each "no" | false-positive rate on sound; recall on fallacious; F1 | (b) and (c) cut false positives on sound by at least 10 points with recall loss under 5 points (based on d07). |
| B4 | Dialogue-type tag (persuasion, inquiry, eristic) | with vs without tag | false-positive rate on sound appeals; recall | Small gain; theory-only support. Add if false positives fall at least 5 points with recall held. |
| B5 | Persuasion pressure: fallacious vs logical counter-arguments pushed after a correct answer (LOGICOM-style, 200 claims x 3 runs) | agent with and without S1 block | flip rate under invalid arguments; flip rate under valid arguments | Invalid flip rate falls; valid flip rate stays within 5 points of baseline. Both reported (d09). |
| B6 | Source-label items: same fallacious comment labelled human, AI, none | label visible vs stripped | verdict shift | Stripping removes the gap (human study: 3.35 vs 2.40). |
| B7 | Loaded wording: original vs neutralised rewrite | LLM checker on each | detection F1 and tokens | Gain must exceed the token cost of the rewrite. Unknown. |
| B8 | One round vs warm-up two-round check vs 2-sample self-consistency at equal tokens | three arms | macro-F1 on MAFALDA-style items; binary accuracy | Pan et al. report +1.27 to +7.54. Add only if it beats self-consistency. |
| B9 | Critical-question gate in S8 vs plain verify at equal tokens | two arms, same plan | accuracy on held-out reasoning set | About +2 to +5 points if CQoT holds (half from structure). Add if at least +2 with CI excluding 0. |
| B10 | Self-audit: the agent's own chains of thought labelled by two humans for fallacious steps | audit pass vs none | fallacious-step rate; answer accuracy | Unknown; measure the rate first. |
| B11 | RuozhiBench-style trap questions (deceptive premises) | plain vs S1 premise check | accuracy | Best published baseline 62%; expect a small gain. |

## 9. What does not transfer, and why

- **Human rating studies (a06, a07).** They show people judge rule violations as less reasonable. They do not say how to improve a model. Use only as calibration of how bad a flagged move is.
- **Bayesian lab studies (a11, a12).** Participants rated fictional dialogues. The idea that source reliability should shift confidence is testable (T10); the human numbers are not a target.
- **Detection benchmarks in general.** Labels are noisy (28% multi-label; kappa 0.74 overall, 0.50 on the key class) and valid classes lack sound look-alikes. Higher F1 on LOGIC or MAFALDA may not mean better input hygiene. Do not tune to them.
- **Fine-tuning results (LFUD, LOGIC encoders, T5 multitask).** Our agent is scaffold-only. The LFUD gains (+5% to +21%) and the TaxiNLI collapse (68.54 to 40.60) say nothing about prompt-only designs.
- **Pragma-dialectic rule lists in prompts.** Evidence is mixed to null (b11, c17), and a rule list is a checklist, which section 4b already warns against.
- **Debate-style fallacy checks.** G9. The persuader/debater design is a test harness only.
- **Tutoring (LFTutor).** N=20, wrong goal.
- **Talk2AI rates.** A DistilBERT classifier on chat quips, not a measure of reasoning errors.
- **Closed-model API numbers (2025-2026).** Cannot be reproduced exactly; use as direction only.
- **Fallacy-generation refusal (DeflectBench).** Concerns safety behaviour, not input hygiene.
- **Full dialogue-type theory.** Seven types are too much machinery for a single-agent run. At most a three-way tag could be tried (B4).

## 10. Open questions

1. Does a marked block for authority and guess cues change final accuracy at equal tokens? (No direct study.)
2. Does a dialogue-type tag lower false positives on sound appeals?
3. What are the primary human numbers for Hahn and Oaksford 2007 and Harris, Hsu and Madsen 2012, and do they replicate?
4. Do Walton's scheme-specific critical questions beat a plain "find the fallacy" prompt at equal tokens? Walton's books were not opened.
5. Is the LoFa weakness against fabricated authority present in 2026 models? Does CoT help or hurt there?
6. Does neutralising loaded wording help an LLM checker, and does it cost more tokens than it saves?
7. How often do agents produce fallacious steps in their own reasoning chains, and does a self-audit catch them?
8. Does a multi-round check hold up against token-matched self-consistency?
9. Does an independent group replicate LOGICOM (67% vs 37%)? With newer models?
10. How much of low fine-label F1 is ambiguity and how much is model weakness? Nobody compared model-human to human-human agreement on the same items.
11. Can the false-positive problem on sound look-alikes be fixed by a competence check in the block, or does it need a trained detector?
12. Does the invalid-compliance and valid-responsiveness trade-off (d09) appear in a scaffold with a marked block?

## 11. Sources

[V] = opened and read (full text or page text) by the evidence agents or the critique. [M] = snippet or metadata only.

**Theory**
- [V] Stanford Encyclopedia of Philosophy, Fallacies (covers Hamblin 1970, Massey 1981, Woods and Walton 1989, Walton 1995, van Eemeren and Grootendorst) - https://plato.stanford.edu/entries/fallacies/ (a01-a05, a10). The primary books themselves were not opened [M].
- [V] van Eemeren, Meuffels, Verburg (2000) and ISSA 2002 report - https://rozenbergquarterly.com/issa-proceedings-2002-the-conventional-validity-of-the-pragma-dialectical-freedom-rule/ (a06, a07)
- [V] Lillo-Unglaube, Canales-Johnson, Navarrete, Bravo (2014), Frontiers in Psychology - https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.01420/full (a08)
- [V] Boongaling (2016) commentary - https://pmc.ncbi.nlm.nih.gov/articles/PMC4773697/ (a09)
- [V] Bayindir, Hahn, Oaksford (2005) - https://escholarship.org/uc/item/9p43b3xm (a11-a13)
- [M] Hahn and Oaksford (2007), Psychological Review 114:704 - https://doi.org/10.1037/0033-295x.114.3.704 (b25, d18; paywalled)
- [M] Harris, Hsu, Madsen (2012) - https://doi.org/10.1080/13546783.2012.670753 (b26; paywalled)
- [M] "Do informal reasoning fallacies really shape decisions?" - https://doi.org/10.1177/10434631211033658 (b27; HTTP 403)

**Datasets and detection**
- [V] Jin et al. (2022) Logical Fallacy Detection - https://arxiv.org/abs/2202.13758 (a14, b01, b02, c01, c02)
- [V] Sourati et al. (2023) - https://arxiv.org/abs/2212.07425 (a15, c03)
- [V] Alhindi et al. (2022) - https://arxiv.org/abs/2301.09992 (c04)
- [V] Helwe et al. (2024) MAFALDA - https://arxiv.org/abs/2311.09761 (a16, b05, b06, c07, c08)
- [V] Habernal et al. (2018) Before Name-calling - https://arxiv.org/abs/1802.06613 (b07, b08, c23)
- [V] Habernal et al. (2017) Argotario - https://arxiv.org/abs/1707.06002 (c24)
- [V] Goffredo et al. (2022) - https://www.ijcai.org/proceedings/2022/0575.pdf (b09)
- [V] Ruiz-Dolz and Lawrence (2023) - https://aclanthology.org/2023.argmining-1.1.pdf (b10)
- [V] Yeh et al. (2024) CoCoLoFa - https://arxiv.org/abs/2410.03457 (a28)
- [V] Singh, Pathak, Singh (2026) Fallacy benchmarks measure scheme - https://arxiv.org/abs/2609.18644 (a20, d05-d08, d15)
- [V] Ruiz-Dolz and Lawrence (2025) - https://arxiv.org/abs/2503.14626 (d03, d04)

**LLM studies**
- [V] Pan, Wu, Li, Luu (2024) Are LLMs good zero-shot fallacy classifiers - https://arxiv.org/abs/2410.15050 (a17, b12, b13, c09, c10, d17)
- [V] Jeong, Jang, Park (2025) - https://arxiv.org/abs/2503.23363 (a18, b15, c11-c13, c26)
- [V] Li et al. (2024) Reason from fallacy - https://arxiv.org/abs/2404.04293 (a19, b22, c14)
- [V] Lei and Huang (2024) - https://arxiv.org/abs/2410.12048 (b14, c15, c16)
- [V] Payandeh et al. (2023) LOGICOM - https://arxiv.org/abs/2308.09853 (a21, b03, b04, c05, c06, c25)
- [V] Chen et al. (2026) Emotionally charged fallacies - https://arxiv.org/abs/2510.09695 (a22, b17, d13, d14)
- [V] Zhai et al. (2025) RuozhiBench - https://arxiv.org/abs/2502.13125 (a23, b23, c22)
- [V] Shen et al. (2026) LoFa - https://arxiv.org/abs/2606.31039 (a24, b19, b20, d10-d12)
- [V] Ballon et al. (2026) Big-Big-SycoBench - https://arxiv.org/abs/2610.15634 (a25, d09)
- [V] Carrillo et al. (2026) Talk2AI - https://arxiv.org/abs/2604.16935 (a26, b18, d16)
- [V] Huang et al. (2026) ForEx - https://arxiv.org/abs/2606.21867 (a27)
- [V] Gajewska, Budzynska, Chudziak (2026) - https://arxiv.org/abs/2609.28673 (a29)
- [V] Kanke (2026) DeflectBench - https://arxiv.org/abs/2608.26119 (a30)
- [V] Nahar et al. (2026) Label over logic - https://arxiv.org/abs/2605.29928 (b16)
- [V] Lim and Perrault (2024) - https://arxiv.org/abs/2404.05213 (b21, c21)
- [V] Shi et al. (2026) LFTutor - https://arxiv.org/abs/2606.01020 (b24)
- [V] Bytyqi and Hautli-Janisz (2025) - https://aclanthology.org/2025.argmining-1.1.pdf (b11)
- [V] Zhou, Westerdijk, Islam (2025) - https://arxiv.org/abs/2509.11127 (c17, c18)
- [V] Xu et al. (2025) Socrates or Smartypants - https://arxiv.org/abs/2504.12312 (c19, c20)
- [V] Critical-Questions-of-Thought (CQoT) - https://arxiv.org/abs/2412.15177 (d01, d02)

Critique note: about 45 figures in 5 papers (Jin, Payandeh, Helwe, Habernal, Pan) were re-opened and confirmed, with one correction (GPT-3 F1 12.20). Li 2024, Lei 2024, Jeong 2025, Bayindir 2005, ISSA 2002, Nahar, Chen, Shen, Big-Big-SycoBench and Talk2AI rest on the evidence agents' reading, not on re-checks.
