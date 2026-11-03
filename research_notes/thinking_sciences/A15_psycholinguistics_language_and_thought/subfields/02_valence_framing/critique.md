# A15.02 Valence framing: cross-check critique

## Re-opened sources (numbers checked)
Confirmed against full text this session:
- Bizer and Petty 2005 Study 1: M 2.42 vs 3.69, F(1,59)=3.99, p=.05 (a01). Study 3 F=5.40, p=.03 (a03). Study 2 interaction F(1,86)=15.45 (a02).
- Echterhoff 2024: 13,465 prompts; GPT-4 baseline framing delta -0.405, "admits 40.5% more students" (c14/b16); self-help -0.010, awareness -0.470, contrastive -0.410, counterfactual -0.570 (c15, c16).
- Wang and Zhang 2026: 82 models, 11 families, 3,280 responses, 4.3% vs 68.8%, 64.5-point shift (c21).
- Tjuatja 2024: allow/forbid Llama2-7b -60.4, 70b -42.2, GPT-3.5 +25.3; question counts (c05, c04).
- WildFrame: r=0.52 / 0.57 / 0.61 and about 55% instance flips under paraphrase (b21, c02, c03).

## Corrections
1. c01 says WildFrame evaluates "eight LLMs". The paper text says eleven (b21 is right). Eight is the number of graduate-student annotators. Use eleven.
2. c04 omits the allow/forbid question count; the paper gives 40 for allow/forbid (176 acquiescence, 271 order, 126 float, 126 odd/even). Small allow/forbid set (40) limits the -60 figure.
3. c05 gives -60.35; the paper table rounds to -60.4. Same value.
4. c02 and b21 are the same WildFrame paper (arXiv 2502.17091), as are c01 and c03; they are not independent. Counted once.
5. b13/b16/c14 overlap: b16 and c14 are the same Echterhoff paper. Counted once.
6. b05 (2023 preprint) and a22 (2024 paper) are the same Siev/Rovenpor/Petty work; b04/a12/a23 all describe Bizer, Zezelj, Luguri 2013. Their agreement is not independent evidence.

## Contradictions between sources
- a07 (certainty mediates, 2011) vs a16 (no moderated mediation via confidence, 2026) vs a20 (certainty only weakly changed in 2025, ambivalence strongly). The mechanism is unsettled; the original two-step "certainty" account is weakened.
- a19 says framing does not change preference extremity; a02/a03 imply strength differences appear only after an attack message. These agree, but both rest on one lab.
- b24 (CogBias) cites Echterhoff and Itzhak as showing framing effects; the Itzhak text does not test framing (b17). Mis-citation risk.
- a24 (Dubois): models differ in sign (GPT-4o 0.90, Sonnet-4.5 -0.24, GPT-5 -0.66), so sycophancy to framing is model-specific.
- c23: the effect appears only when the experiment is named, which conflicts with reading b13/b14 as pure wording sensitivity (contamination alternative).

## Weak spots
- All human support/oppose evidence comes from the Petty/Bizer group plus one thesis (Taylor 2018). The first study had p=.05 and Study 3 had N=22.
- No direct LLM replication of the support/oppose manipulation (a29). LLM evidence is adjacent: gain/loss, reject/admit, allow/forbid, sycophancy.
- Several effects were measured on older models (GPT-3, GPT-3.5, Llama2); results for current models differ in sign (a24).
- Single-source claims: K06, K10, K16, K17.

## Only seen in snippets or unopened
a13 (Zezelj 2007), a12 (press release only, no numbers), a28, a29, b01, b03, b04, b05, b06, b12, b25, c28, c29. Teeny and Petty 2025 (a18-a21) and Rovenpor 2026 (a15, a16) were opened but not re-checked this session (no arXiv copy located); Dubois 2026 and Payne 2025 not re-opened.

## GAPS
1. Does an LLM given "what do you think about X being rejected" vs "chosen" (equal preference) resist a counter-argument more? Run the Bizer-Petty design directly, with answer-flip and verbalised confidence.
2. At equal total tokens, does a neutral-restatement step (S1) cut framing flips more than an "avoid bias" instruction or extended thinking alone, and does it add or lose accuracy on unframed items?
3. What is the exact cost: how many tokens does restatement add, and does it ever distort the problem (loss of constraints)?
4. Do current frontier models (2026) show the reject/admit and allow/forbid shifts, and are effects in older models still present (sign differs by model in Dubois)?
5. How much of LLM framing sensitivity is contamination of the named paradigm (c23) vs real wording sensitivity? Which blind tests exist beyond gpt-oss-120B?
6. What is the true mechanism for humans: certainty, ambivalence reduction, or basis of preference (a16, a20)? Which would have an agent analogue?
7. Is there independent (non-Petty-lab) replication of the 2005 and 2011 results with preregistration and larger N?
8. Do multi-turn agent settings (repeated challenge, DuET-PD style) show opposition-style entrenchment, and does neutral restatement of the challenge reduce capitulation?
9. Does structured output (JSON) keep framing drift while free-form reasoning cuts it (Shafiei), and does that hold for restated problems?

## Gap search results (2026-11-03)
Evidence: evidence_d.jsonl (d01-d16, all opened). Method limits: WebSearch was refused (shared budget used up), OpenAlex and Semantic Scholar were rate-limited, so only known papers were re-opened in full text. No new LLM experiment could be run here (no model API).

1. Bizer-Petty design on an LLM: STILL OPEN. No study found. Nearest: Yun 2026 (positive vs negative question framing, agreement 76.2% vs 72.0%, 6,614 pairs, includes GPT-5.1 and Sonnet 4.5; d08). The test itself is still to be run.
2. S1 vs "avoid bias" instruction vs extended thinking at equal tokens: PARTLY CLOSED. Dubois 2026: question rewrite (-0.55 / 0.16) beats an explicit no-sycophancy instruction (0.51) vs control 1.13 (d06). Thinking helps but does not remove drift (Wang and Zhang, d11). Nothing is token-matched, and accuracy on unframed items was not measured for the framing fix. Open.
3. Restatement cost and distortion: PARTLY CLOSED. Rephrase-and-Respond: GPT-4 64.95 to 89.77 on ambiguous tasks, and documented distortion on weaker models (wrong constraint, "rephrase" loops; d12). Token counts not reported anywhere opened. Open.
4. Frontier 2026 models: MOSTLY CLOSED. The "sign differs" worry from Dubois was a misreading: model terms are baseline levels, not opposite framing effects (d07). Yun 2026 (GPT-5.1, Sonnet 4.5) and Wang and Zhang 2026 (82 models) show framing effects persist. Allow/forbid on 2026 models is still untested.
5. Contamination vs wording: PARTLY CLOSED. Bose 2026 blind vs named on gpt-oss-120B: framing 0.020 blind vs 0.619 named; the Asch gate is absent for Llama 8B/70B (d01, d02). The blind ceiling weakens the blind result, and Yun 2026 shows effects in an unlabelled task. No other blind test found; closed frontier models untested.
6. Human mechanism: STILL OPEN, narrowed. Rovenpor 2026: effect only at equal extremity (d13); Teeny and Petty 2025 preregistered Study 5: ambivalence moderates (d14). The certainty account is weakened. No agent analogue identified.
7. Independent preregistered replication: STILL OPEN. All newer work is from the Petty group; Rovenpor 2026 was not preregistered (d13, d16). Search incomplete.
8. Multi-turn entrenchment and restating the challenge: PARTLY CLOSED. DuET-PD shows capitulation (GPT-4o 27.32% accuracy after 3 turns; d04) and that repetition suffices (d05); Yun 2026 shows the framing gap grows in multi-turn. No paper tests neutral restatement of the challenge or opposition-style entrenchment. Open.
9. JSON vs free-form: PARTLY CLOSED. Shafiei 2025: free-form CoT cuts drift more than JSON (d09). Not tested on restated problems.

Corrections to earlier notes: a24 "sign differs by model" should read "baseline sycophancy level differs by model". Claims K18-K23 added; K03, K05, K10, K11, K13, K16 extended; K03 and K10 now contested.
