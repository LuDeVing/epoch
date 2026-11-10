# Critique: A11.07 Category learning, rule / prototype / exemplar (cross-check)

## Corrections made (sources re-opened this session as arXiv PDFs)
Re-checked and confirmed: Jagadish 2024 (BIC 38722.13 vs 39816.90; 41207.20 vs 42401.42; MSE 0.18 vs 0.05; slope -0.01 +/- 0.004, z=-2.54; Type 2 harder than 3-5); Russin 2025 (Llama 2 rule-like blocked 601/640 = 93.91%, interleaved 478/576 = 82.99%, rotated 23.59% / 24.48%; GPT-3.5 curriculum p=0.63; human p=0.04, d=0.47 / 0.33); Wang 2024 (83% to 66%, 90% to 74%, four r values); Xu 2025 (90.64%, 90.87%, 92.37%, 87.46%, 88.63%, 52.41%, 67.67%, rho 0.776); Chan 2022 (1B near exact exemplar, BX equally AX or BW); Fu 2026 (+0.178 rules, -0.024 examples); Lian 2024 (0.768 / 0.713 / 0.166 / 0.130); Xiong 2026 (prototype-like best match, amplification insufficient).

Corrections:
1. a05 (Lian 2024): "Type IV 0.910" is the LEAF-level value. At basic level Type IV is N/A (constant model accuracy). Type III basic is 0.751 and was missing. Claim K05 uses the corrected set.
2. a05 said "V 0.984 (both levels)": confirmed. "VI -0.375" is basic; leaf is 0.884.
3. c06/c07 (Chan 2022): the exemplar-based in-context result for BX is for transformers trained from scratch; the size result (1B exact exemplar, larger more rule-based) is for pretrained LMs. The two lines should not be merged. K06 now separates them.
4. c13 (Fu 2026): the size gaps "+0.213 base, +0.063 instruct" were read from a figure whose text layer is garbled (a third value "+0.064" appears). Treat as approximate.
5. a10, b07, b08, c01, c02, a11 are one paper (Jagadish 2024) counted six times. Independent-source count for K03/K04 is 1.

## Contradictions and tensions
- Humans (Smith and Minda 1998) move prototype to exemplar; Claude-v2 prompted is exemplar-based from block 2 (c03). Opposite stage pattern.
- Xiong 2026 says LLM in-context classification is prototype-like; Chan 2022 says small LMs are exemplar-like; Russin says ICL is rule-like when a rule exists. These differ by model size, task and measure. No single "LLM style" exists.
- Fu 2026: rules beat examples in instruct models, yet ExpeL/ERL results show distilled insights and raw trajectories are close (ALFWorld retrieval beats insights, 55% vs 50%). Rule-first is not uniformly better.
- Nosofsky 2000 disputes Smith and Minda 2000's meta-analysis; we have only abstracts of both.

## Weak spots
- The founding studies (Shepard 1961, Medin and Schaffer 1978, Rouder and Ratcliff 2004/2006, Goodman 2008, Nosofsky 1986/1992) have no numbers read; many are second hand via Lian 2024 or Jagadish 2024.
- Most LLM evidence is on small or open models (Gemma, Qwen, Llama 2, 1B-70B) or an old model (Claude-v2). Nothing tests a current frontier model on Shepard types.
- Many human-model fits come from a single lab (Jagadish et al.) and one paper.
- Several LLM results are on artificial or tiny tasks (Number Game, Boolean concepts); transfer to agent problem classes is untested.
- ExpeL/ERL are agent-memory studies, only loosely category learning; their prototype/exemplar reading is ours, not theirs.

## Only seen in snippets or abstracts
a18, a19, a20, b01-b05, b14-b16, b19, c09 (conference abstract), c21, c22, c23 (read from tables or figures not rechecked here), c24-c27, and all unopened classics (a01-a03, b24-b27).

## GAPS
1. Does a current frontier model reproduce the Shepard difficulty order (Types I-VI) when tasks are run as text with permuted labels? Claude-v2's Type 2 anomaly may be fixed or not.
2. Does a "state the rule, then test it" step beat few-shot examples at equal tokens on rule-structured problem classes, and does it hurt on non-rule (rotated, family-resemblance) classes? Fu 2026 and Russin 2025 suggest both directions.
3. What do Rouder and Ratcliff (2004/2006) and Goodman et al. (2008) report numerically (model fit, which stimulus designs favour rules vs exemplars)? None read.
4. Is prototype-style (distilled class summary) or exemplar-style (stored case) memory better for S0 problem-class retrieval at equal tokens, and does the answer flip with number of stored cases?
5. What are the Smith and Minda (2000) and Nosofsky (2000) numbers: how many of the 30 data sets favour each model, and which were disputed?
6. Does Boolean/structural complexity (Feldman 2000) predict agent failure well enough to serve as an S0 routing signal? Wang 2024 shows r near -0.9 on four small models only.
7. Do blocked vs interleaved few-shot orders matter for frontier models on rule vs non-rule tasks? Llama 2 shows it; GPT-3.5 does not.
8. Do the order and strength of the early-prototype / late-exemplar drift hold for LLM agents across a long session, and is there a measurable switch point?
9. What do Davidson 2026 and Liu 2024 (rule vs example learning, function vectors) report? Cited in Fu 2026 but unread.
10. Does working-memory load (small context) push an LLM agent towards exemplar-style behaviour, as it shifts humans? Lewandowsky 2011 and Hoffmann 2014 effect sizes need reading.

## Gap search results

Evidence is in evidence_d.jsonl (d01-d17; 14 opened, 3 from summaries only). Claims K02, K04, K08, K09, K13, K18 were edited and K20-K24 added. Access note: arXiv, Semantic Scholar and OpenAlex APIs were rate-limited, the WebSearch budget ran out after three calls, and most founding-study PDFs were behind bot walls or 404.

1. Frontier model on Shepard types: STAYED OPEN (no study found, none run). Reframed: Pape et al. 2015 (d01) show the order Claude-v2 produced (Type II harder than III-V) is the "general" human order seen with integral stimuli, children and monkeys. So K04 is no longer an anomaly claim. Next test must compare against both orders.
2. Rule-then-test vs few-shot at equal tokens: PARTLY CLOSED. Liu 2024 (d09, d10): true rule 30% to 96% (GPT-4-turbo), self-stated rules unreliable (r=0.0013; Kalamang 22-28%). Fu 2026 (d12): rules win on algebraic tasks, smaller or non-significant on linguistic and non-rule tasks, no clear harm, but examples were minimum-coverage, not token-matched. Fu and Russin do not truly conflict: rules help when correct and rule-structured; rotated categories fail for examples too.
3. Rouder/Ratcliff and Goodman numbers: STAYED OPEN for numbers. Qualitative result read from the Rouder 2004 abstract (rule model wins with confusable stimuli, exemplar model with few distinct ones; d05). Goodman not opened (d08).
4. Prototype vs exemplar memory for S0: PARTLY CLOSED. Four agent-memory studies (d13-d15, plus K13) agree that distilled memory beats raw stored cases, and more retrieved cases hurt (ReasoningBank 1 case 49.7, 4 cases 44.4). Many-shot ICL (d16) shows exemplar-like (k-NN) behaviour with thousands of cases, so a crossover at large case counts is plausible but not measured on problem-class retrieval.
5. Smith and Minda / Nosofsky numbers: STAYED OPEN (d06, d07 are summaries only: 29-30 data sets; Nosofsky and Vanpaemel & Pattyn disputed it). K02 downgraded to contested.
6. Boolean complexity as a routing signal: PARTLY CLOSED, negatively. Boolean complexity predicts only the classic Shepard order; an entropy measure gets R2 .829 and .970; Boolean rank correlation drops on larger structures (d02, d03). Use as a soft prior. No frontier-model test yet.
7. Blocked vs interleaved for frontier models: STAYED OPEN. No new source.
8. Prototype-to-exemplar drift in LLM agents over a session: STAYED OPEN. No source found.
9. Davidson 2026 and Liu 2024: CLOSED. Davidson (d11) is a function-vector mechanism study on about 50 simple tasks in 3B-8B models, not a category-learning study; Liu (d09) as above. The behavioural claim about Davidson comes from Fu, who says it is marginal in Davidson.
10. Working-memory load and exemplar behaviour in agents: STAYED OPEN. Human effect sizes (Lewandowsky 2011, Hoffmann 2014) not obtained. Indirect hint only: with very many cases a frontier model acts like k-NN (d16), the opposite direction to the human pattern.

Still needed: PDFs of Rouder and Ratcliff 2004/2006, Goodman 2008, Smith and Minda 2000, Nosofsky 2000, Feldman 2000, Lewandowsky 2011, Hoffmann 2014; and an actual run of the six Shepard types on a current model.
