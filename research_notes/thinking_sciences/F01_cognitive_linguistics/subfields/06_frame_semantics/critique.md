# Critique: Frame semantics (F01.06)

## Corrections made
Re-opened: arXiv HTML 2509.19540v1, 2507.23082v1, 2502.12516v1; Rai et al. 2026 PDF; Edwards and Schuster abstract.

1. Chundru et al. Table 3 (FN1.7): "names plus LU defs" is 76.5 / 80.9 (b07 correct). c09 gave 76.2 / 79.8, which is the "names and frame defs" row. Use b07. Direct-QA 80.1/81.3 (names), 80.8/83.5 (LU defs) confirmed.
2. Devasier et al.: the v1 Table 4 lists prior best as Ai and Tu 0.755 (AGED 0.751, KAF-SPA 0.751). a20/c01 give 0.771 and KAF-SPA 0.813 (probably a later version). The "+3.9 over SOTA" claim is version-dependent. Qwen 72B 0.794, Phi-4 0.785, 4o-mini 0.768, XML 0.342 vs JSON-exist 0.471, -27.0 on unseen FEs all confirmed.
3. Garat et al. confirmed: Sonnet 3.5 82.9 (250 shots) and GPT-4o 80.2 (400) are for the Killing frame only (100 examples); FI best 94.3 (DeepSeek Chat); FSRL gold-frame 77.4. Zero-shot 4o-mini 3.9 / 36.4 / 39.3 confirmed. Do not mix the Killing numbers with the FSRL headline. Detected-frame FSRL: Sonnet 68.6, DeepSeek Chat 68.6.
4. Chundru YAGS 80.7 (fine-tuned; zero-shot 65.4), Artifacts 25.6 to 49.6, and error counts 519/538/320/296/24 confirmed.
5. Rai et al. 2026: base 0.52 zero / 0.39 few; adapted 0.55 / 0.75; 917-item slice; 0.36 gain over GPT-OSS-20B confirmed.
6. Edwards and Schuster: only the 69.40% headline confirmed (abstract). UA-Single 61.20, FULL 70.80, p=0.458 and costs not re-checked.
7. b01-b05 list authors as "not confirmed". They are Garat, Moncecchi, Wonsever (same paper as a17-a19, c05-c07). Duplicates, not independent.

## Contradictions and duplicates
- The same three papers (Garat, Chundru, Devasier) appear in files a, b and c. Independent counts in claims.jsonl count papers, not rows.
- Gold-frame FSRL (67-77) vs Killing full parse (69-83) are different tasks.
- Gildea and Jurafsky 2002: abstract thematic roles (82.1) beat frame-specific roles (80.4).
- Human framing/wording evidence is mixed: Steen null vs Thibodeau and Boroditsky small effect (w=.14); Loftus-Palmer main effect not replicated, only a moderated one.
- The WordNet control in Iwamoto and Ohara matches the FrameNet gain, against a frame-specific benefit.

## Weak spots
- No study tests "write the task as a frame, find empty roles" as a scaffold for general reasoning. All LLM evidence is annotation, role labelling or fine-tuning.
- Three Rai/Croce/Basili papers come from one group and are training-based.
- Small evaluation sets (100 examples in Garat) and older models (Sonnet 3.5, GPT-4o).
- Role-omission detection is measured only indirectly (Ambig-SWE, UA scaffolds).

## Seen only in snippets or second hand (opened:false)
a03, a04, a05 (Fillmore 1976/77/82/85, citation facts only; the founding texts were never read), a26, a27, a28, b24 (Many Labs 1), c23, c24, c25 (blocked), c26, c27.

## GAPS
1. Does a "write the task as a frame, list roles, flag blanks" step improve accuracy on underspecified or multi-constraint tasks at equal tokens? (No direct study found.)
2. Does a missing-role check beat a generic "what information is missing" prompt?
3. How well do 2026 frontier models list peripheral roles (means, instrument, cause) that 2025 models missed at 0-50 F1?
4. Is the FrameNet prompt gain frame-specific or generic structure (WordNet matched it)? Needs a plain role-list control.
5. What do Fillmore's primary papers and human experiments on frames and scripts show, with numbers, about completing missing roles?
6. Ambig-SWE and UA scaffolds: exact detection accuracy, false-positive rate and cost of asking at equal tokens.
7. Does a neutral re-framing step reduce framing flips in frontier models (DeFrame covers only 3B-14B)?
8. Does frame decomposition help on agent planning or requirements elicitation benchmarks (c25 unread)?
9. Does the Devasier prior-SOTA comparison (0.755 vs 0.771) hold in the latest paper version?

## Gap search results (evidence_d.jsonl, d01-d17)

Closed:
- Gap 9 (Devasier prior SOTA): closed. Only one arXiv version exists (v2-v4 return 404). 0.771 and KAF-SPA 0.813 are in Table 3 (in-context comparison); 0.755 is in Table 4 (fine-tuning). The +3.0 and +3.9 claim is against 0.755. (d01, d02)
- Gap 6 (Ambig-SWE and UA detail): closed. Ambig-SWE detection accuracy, false positive and false negative rates per prompt and model are in d03 (Sonnet 4 strong prompt 0.89/0.03/0.18; Llama FPR up to 0.95; Qwen 3 Coder never asks). UA: Sonnet 4.5 Full 70.8, Hidden 54.8, Interactive 70.4, UA-Single 61.2, UA-Multi 69.4; asked 344 vs 369 tasks; 3.06 vs 1.84 queries; cost about $3.50 vs $2.03 per task (row mapping of the cost table inferred, garbled PDF). (d04-d07)

Partly closed:
- Gap 7 (neutral re-framing): FRAGILE shows text-level anchors fail or amplify flips on 7-8B models (28.6% average flip); only a hidden-state method works. Still no test of a neutral re-framing step on frontier models. (d08, d09)
- Gap 8 (planning and requirements benchmarks): c25 is now read (Kundi et al.): five requirements, Llama 3.2, counts only, no accuracy. OntoAgent (slot ontology, not FrameNet) gives IRE 0.13 to 0.41 to 0.69 on 101 scenarios. NoisyToolBench read: asking prompts help A1 much more than final answers. No FrameNet decomposition on an agent planning benchmark. (d10-d12)
- Gap 5 (Fillmore primary and human data): Petruck 1996 review read; Bower, Black and Turner 1979 only second-hand (PDF blocked, 403). Fillmore 1976-1985 originals still unread; he ran no numbered human experiments. (d14, d15)
- Gaps 1 and 2 (frame step vs plain restatement, role check vs generic missing-info prompt): still no direct study. Indirect support: separate gate beats inline reminder (+8.2 points, d05); slot ontology beats free-form (d11); ranking gaps by information gain beats plain question generation (d13). All use generic or domain slots, not frames, and none is at equal tokens.

Still open:
- Gap 3 (2026 frontier models on peripheral roles): nothing found; the Semantic Scholar, arXiv search and OpenAlex APIs were rate limited (429) so the search was web-search only. (d16)
- Gap 4 (plain role-list control): nothing found beyond the WordNet control. (d17)

New caveats: the Ambig-SWE and UA numbers are Claude Sonnet 4 / 4.5 and Kimi K2.6 on simulated users; cost ratios are not equal-token comparisons.
