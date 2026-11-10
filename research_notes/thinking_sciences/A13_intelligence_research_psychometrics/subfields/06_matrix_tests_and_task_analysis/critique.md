# Critique: A13.06 Matrix tests and task analysis (cross-check)

## Numbers re-opened this session (all from the PDF text)
Confirmed: Little et al. 2014 (57% of variance from rule tokens; N=126, r=0.56, t(34)=2.87, r2=0.20); Zhang et al. 2019 RAVEN (human 84.41, ResNet 53.43, ResNet+DRT 59.56, rule loss 59.56 to 20.71, structure loss to 56.86); Webb et al. 2023 (OR 1.88, CI 1.21-2.91, r(30)=0.39, p=0.027); Gendron et al. (GPT-4 open 0.410/0.330, MC 0.697/0.535, fine-tune 0.977); Hu et al. 2021 SRAN (context-blind ResNet 71.9 vs 12.2; CoPINet 94.2 vs 14.2; CoPINet 91.4 to 46.1; SRAN 60.8); Camposampiero et al. 2025 (o3-mini 86.6 to 17.0; R1 80.6 to 23.2; neuro-symbolic 98.6 to 88.0); MARVEL (humans 68.86, SD 9.74; closed models 25.7; best consistency 5.97); NeuroCognition (human RAPM 0.430/0.444 text vs 0.814 image; GPT-5 0.540 to 0.605).

## Corrections and additions
1. NeuroCognition human text figures come from a pilot of N = 9 per format, and the image figure (0.814) is borrowed from the RAVEN paper (different sample, different test). The "humans find text harder" claim is weak. a24/b20 should carry this caveat.
2. Zhang 2019 labels the 0.814 as a RAVEN human figure on a subset of "easily perceptible" items. It is not RAPM.
3. a01-a03 (Carpenter, Just, Shell 1990) stay opened:false. The 57% figure is now confirmed through Little et al. (opened), but the original 1990 sample sizes, fixation data and FAIRAVEN/BETTERAVEN fit statistics are still not read.
4. b04/c07/a16: the "symbolic" and "text" columns of Gendron were once swapped in some summaries; values above match Table rows (GPT-4 open 0.410 text, 0.330 symbolic).

## Contradictions between sources
- CoPINet on I-RAVEN: 22.84 (Zhang 2021, trained on 2x2Grid only) vs 46.1 (Hu 2021, full training). Different training regimes; both agree it falls sharply from RAVEN.
- Auxiliary rule supervision: Barrett 2018 +13.9 points on PGM; Zhang 2019 found it hurt on RAVEN (59.56 to 20.71). Dataset-dependent; unresolved.
- Mitchell et al. GPT-4 on ConceptARC: 25% (zero-shot) vs 33% (one-shot, richer prompt) vs "GPT-4 33%" in a24. Same study, different prompt settings; not a real conflict, but the label matters.
- Chain of thought: Gendron says it hurts MC; GPT-3.5 open-ended rose 0.226 to 0.302 (b05) while c08 says only GPT-3.5 improved; consistent. But Ahrabian and VCog report CoT demos helping GPT-4V/GPT-4o. Task format and model decide the sign.
- Lewis and Mitchell vs Webb: generalisation to counterfactual alphabets. Reply paper partly rebuts with code execution. Not resolved.
- Text vs image: models better on text (NeuroCognition) but Mitchell finds GPT-4V far worse than text GPT-4. Agrees direction; humans opposite.

## Weak spots
- Almost all LLM evidence is 2023 era models (GPT-3, GPT-4, GPT-4V). Only b15, b18, b19, b20-22, c23 touch 2025-26 reasoning models, and mostly with different tasks.
- No direct test of a scaffold on matrix items at equal tokens; every gain here (decomposition, execution check) is a prompt or tool change with its own token cost, which is rarely reported.
- Memorisation: Raven is public; Gendron suspects GPT-4 saw it. Digit Matrices and counterfactual tasks reduce this but not fully.
- Woodcock-Johnson Concept Formation and Analysis-Synthesis: nothing opened (a29). The assigned focus is half uncovered.
- Human eye-tracking evidence (b24-b26) is correlational; b25/b26 titles/authors incomplete, only snippets-level detail.

## Only seen in snippets or secondary
a01-a03, a28 (Little 2012 Bayesian model, abstract only), b29-b31 (Carpenter abstract, DeShon, Gignac), c26-c27.

## GAPS
1. Does forcing the agent to predict the missing cell before seeing the options (constructive matching gate) beat options-first at equal tokens, on a leak-free (I-RAVEN style) item set with a context-blind control?
2. What do the Woodcock-Johnson Concept Formation and Analysis-Synthesis subtests measure (rule discovery from feedback, sequential rule application), what are their factor loadings, and do LLMs run on them, with numbers?
3. How do 2025-26 reasoning and tool-using models score on text-attribute RAVEN/I-RAVEN with and without code execution of the stated rule, with token counts?
4. Why does auxiliary rule labelling help on PGM and hurt on RAVEN; does naming the rule type in a prompt help an LLM at all (NeuroCognition pattern hints were null)?
5. What are the original Carpenter, Just, Shell 1990 numbers (sample sizes, fixation statistics, FAIRAVEN/BETTERAVEN fit) and Vodegel Matzen error-type frequencies, read from primary text?
6. How much of the LLM Raven score is memorisation: performance on novel rule combinations and counterfactual symbol sets for current models (Webb, Lewis and Mitchell follow-ups, 2025-26)?
7. Does keeping several candidate rules alive (Bayesian posterior idea from Little 2012) reduce the collapse under perceptual uncertainty seen in I-RAVEN-X?
8. Is the arithmetic-rule weakness a number-handling failure fixable by tools, or a rule-induction failure; what does a calculator tool do at ranges 100 and 1000?
9. How does format (multiple choice vs generative) interact with reasoning on/off across current models, with run-to-run variance measured over at least 5 seeds?

## Gap search results (evidence_d.jsonl d01-d16; claims K20-K26 added, K06/K07/K17/K19 updated)
Tool limits this session: web search budget ran out after 2 calls; Semantic Scholar, OpenAlex and arXiv query APIs were rate limited. Papers were opened by direct arXiv PDF. Carpenter 1990, Vodegel Matzen and Little 2012 full text were not reachable.

1. Constructive matching vs options first: PARTLY CLOSED. Hersche et al. (d01) compare predict-first (options hidden, match by code) with options-visible on leak-free I-RAVEN: GPT-4 74.8 vs 56.0-60.0, Llama-3 70B 79.0 vs 22.4-22.8. Not token matched, no options-only control, 2024 models. Still needs our own run (K20).
2. Woodcock-Johnson: PARTLY CLOSED. Task descriptions and one-factor CFA (loadings above .65, N=69; d09), WJ IV Schmid-Leiman g loadings .50-.56 (d10), Gf factor not clean in the norm data. No LLM result found (d12). K19 rewritten.
3. 2025-26 reasoning models with token counts: PARTLY CLOSED. o3-mini and R1 token counts per item in d03 (5-19k tokens). No code-execution arm for any model on text RAVEN. ConceptARC (d13) shows tools help images, not text.
4. Rule labelling: PARTLY CLOSED. Zhang 2019 gives no cause for the drop (d08); my explanation (shortcut disturbed by the rule loss) is untested. LLM rule hints null across 10 models. K24 marked contested.
5. Carpenter, Just, Shell 1990 and Vodegel Matzen primary numbers: STAYS OPEN (d16). The 57% figure remains second-hand.
6. Memorisation on matrices: STAYS OPEN. Only letter-string follow-ups were found (d14); trained-model rule omission in d15. No 2025-26 counterfactual Raven test. K26.
7. Several candidate rules alive: STAYS OPEN for LLMs. Only ARLC (non-LLM) supports it and its ablation does not isolate the multi-rule part (d06). The authors of I-RAVEN-X say the models cannot hold outcomes in superposition (d05).
8. Calculator for arithmetic rules: STAYS OPEN. No tool arm exists. Evidence is mixed: 32 of 68 GPT-4 arithmetic errors fit a last-row-only rule (rule-induction failure), while accuracy also falls with range (d02).
9. Format by reasoning interaction with 5+ seeds: STAYS OPEN. NeuroCognition ran RAPM once per model (d07). The human pilot was 9 people who each did both formats. Only ConceptARC has a 3-run check, on 48 tasks (d13).

New corrections
- The "86.6% to 17.0%" drop mixes settings. The matched clean baseline for the 17.0% cell is 81.0% (range 1000, 3x10). Confounders alone give 69.8%, smoothing alone 75.6% (d04). K07 corrected.
- Human text pilot wording: "N=9 per format" means the same 9 people did both; no consistent format direction per person.
- The two labelled "discriminative" rows in Hersche Table III differ by a setting lost in the PDF layout; treat the 56-60 range as two conditions.
