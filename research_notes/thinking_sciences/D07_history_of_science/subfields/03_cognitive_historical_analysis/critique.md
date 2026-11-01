# Critique: D07.03 Cognitive-historical analysis (cross-check)

## Numbers re-opened (PDF text from local copies, this session)
1. Lewis & Mitchell (2024) accuracy: humans 0.753, GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (1,876 human samples, 6,840 per model). CONFIRMED (b17, c08 right).
2. Lewis & Mitchell Table 4 (error types) covers GPT-3, GPT-4 and Human only. Alternate-rule share: GPT-3 5.81%, GPT-4 22.00%, human 38.59%. Incorrect-rule: GPT-3 30.97%, GPT-4 32.67%, human 14.67%. CORRECTION: b18 wrongly gives 38.59% to GPT-3.5 and says GPT-3.5 "often applied an alternate rule". There is no GPT-3.5 row. a14 is right. Treat b18 finding as wrong.
3. Webb et al. (2023): digit matrices generative OR 1.88 (CI 1.21-2.91, p=0.005); story analogy GPT-3 vs humans OR 0.37, p=0.0003; GPT-3 near p=0.0039, far p=0.065. CONFIRMED. Small difference: the human t(53) is 21.3 for combined, 21.5 near, 16.7 far; b16 gave 21.3 only (fine).
4. Webb et al. 2024 rebuttal: GPT-4 + code vs humans P=0.496; 46% (23/50) of GPT-4 errors used a valid alternative rule vs 39% for humans in L&M. CONFIRMED.
5. Stevenson et al. (2024): adults 0.88/0.91/0.89 (n=62), GPT-4o 0.85/0.63/0.48, Llama-3.1 405B 0.79/0.74/0.27, 54 runs. CONFIRMED. Methods text says 42 children; table has 41 (as c09 noted). Children's 0.62/0.66/0.67 not rechecked.
6. Si et al. (2024): novelty 4.84 / 5.64 / 5.81; 49 ideas per condition; 79 reviewers; 298 reviews; review-level n 119/109/109; idea-level AI 5.62 p=0.03; Claude-3.5-Sonnet 71.4%; 4000 seeds, 200 non-duplicates. CONFIRMED.
7. Gentner et al. (1997): "at least 34 circles" with 6 ellipses and "at least seventy times" CONFIRMED in text. The "8 minutes of arc" mismatch and "4 candidate inferences" were NOT found: the text lists several inferences in prose (first, second, third...) without a stated count of 4, and "minutes" returned nothing. Treat a05's "4" and "8 minutes" as unverified.
8. Webb 2023 N values (40, 57, 54): consistent with the text where seen; letter-string 57 not rechecked.
9. Not re-opened (time): NewtonBench tables (c01-c03), ARN (a15; the pdf link I tried returned a stub), Yasunaga (b24), Kretz & Krawczyk (b08), AI Feynman. These stay as the extractors recorded them.

## Contradictions between sources
- a14 vs b18 on GPT-3.5 error type (resolved above: b18 wrong).
- a14 says human sample "about 46 (their data)"; b17 and c08 say 136 recruited. Likely different counts (recruited vs used per condition); unresolved.
- AI Feynman: Eureqa 71% vs 68% on the same page (c18 flagged).
- Lewis & Mitchell say chat tuning may have hurt (GPT-3.5 worst); Webb 2024 says the real issue is counting, fixed by code. Both fit the data; neither isolates tuning.

## Weak spots
- The cognitive-historical method itself has no counts or effect sizes. Its support is case studies (Maxwell, Kepler, one neural-engineering lab). Generality is argued by "bootstrapping", which Nersessian says is not inductive (b02). Independent replication of Maxwell-style findings is absent.
- Many "established" claims have only 2 sources that share one underlying paper family (Webb/Lewis/Hodel group is one debate, not independent measurements of the same thing).
- Hand-coded Kepler representations (a05, a08): authors chose the coding.
- LLM novelty studies use LLM judges (MOOSE, SciAgents self-scores). Si et al. is the only blind-human one.
- Models tested are 2022-2024 vintage; no 2025-2026 reasoning model on counterfactual analogy was found.
- No LLM study tests the cognitive-historical claim directly (does a staged hybrid-model operator beat unstructured analogy?).

## Seen only in snippets or second-hand
a22, a23, a24, a25 (Dunbar), c25, c26, c27 (not opened). b10 base rates (Dunbar, Saner & Schunn) came from a review passage.

## GAPS
1. Does an explicit staged analogy operator (pick source, state target constraints, prune, generic abstraction) beat plain analogical prompting at equal tokens on a modern reasoning model?
2. Do 2025-2026 reasoning models still fail counterfactual letter-string and symbol analogies, and does a code tool close the gap (Webb 2024 vs Lewis & Mitchell)?
3. Do current models fail far (low surface overlap) narrative analogies as in ARN (39.6%), and does a structure-first retrieval step fix it?
4. What are the exact Dunbar in-vivo numbers (near vs far source use for fixes vs new concepts)? We only have them second-hand.
5. Is there any replication of the Maxwell or Kepler cognitive-historical readings by an independent group, or a critique from historians (e.g. that the reconstruction overfits the record)?
6. Does simulation (physics engine or text-grid state) help only where no rule shortcut exists, and what is the break-even in tokens?
7. Does adding a code tool lower exploration in strong models (NewtonBench -2.6 GPT-5), and does a forced-exploration guardrail remove the loss?
8. Does retrieved far inspiration actually raise human-judged novelty without lowering feasibility, given LLM-judge bias in MOOSE and SciMON?
9. Which ARN, NewtonBench and ARN-like numbers survive when the original tables are read (we have prose only for ARN)?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d22). Web search quota ran out early, and arXiv, Semantic Scholar and OpenAlex search were rate limited, so I worked from known arXiv ids, Europe PMC (full text) and direct PDF downloads. That limits gaps 2, 5 and 8 in particular. Claims K02, K07, K08, K10, K14, K19 were changed and K21 to K29 added.

1. Staged analogy operator vs plain analogical prompting at equal tokens: OPEN. No such test exists in what I could open. Nearest are Thought Propagation (d14: GPT-4 0.88 vs CoT 0.76 and ToT 0.46, 1-layer at ToT-like tokens) and Step-Back (d15: only +1.6 and +0.3 over GPT-4 CoT). Both use 2023 models. Recorded as K26.
2. 2025-26 reasoning models on counterfactual letter strings: STILL OPEN, partly informed. The published Webb reply (d06) gives cleaner numbers (code P=0.92, code-disabled control 22.5% vs 21.7%) but is still GPT-4. Reasoning-model evidence is adjacent only: ConceptARC (d08, d09) and nonword relations (d20). On code tools: in ConceptARC text, tools did not help any model (o3 77.1 to 75.6, Claude 60.2 to 55.0, Gemini 66.0 to 60.4), helping only for images.
3. Far narrative analogies and structure-first retrieval: PARTLY CLOSED, narrowed. ARN's 39.6% is an average over nine systems and two far cells; the true failure is far analogy vs near distractor (GPT-4 29.1, humans 91.4; d01, d02). Message-extraction CoT demonstrations help far items (d03). AnaloBench shows retrieval from 200 stories is near random (d10, d11). No structure-first retrieval fix has been shown, and no 2025 model was tested.
4. Dunbar exact numbers: PARTLY CLOSED, still second-hand. Via a full-text review (d17): 98% of Dunbar's microbiology-lab analogies were within domain, Saner and Schunn over 75%, engineering design 55/45, political writing 77% outside. This corrects K02 ("roughly even") and weakens K19. No primary Dunbar paper was opened; his lab site is gone and no open PDF turned up.
5. Replication or historian critique of Maxwell and Kepler readings: OPEN. Nersessian's 2025 review has no critics in it (d21). Only a precedent was found: Hanson's Kepler reconstruction was judged historically inadequate (Lugg 1985; d18). Independent Maxwell historians (Siegel, Darrigol, Chalmers) not checked because search failed.
6. Simulation only where no shortcut, token break-even: STILL OPEN. The only control found is the ring task (CoT 52.5 vs VoT 49.5, n=200, not significant; d19). No token break-even exists in any source I opened.
7. Code tool lowers exploration; forced-exploration guardrail: PARTLY CLOSED on the first half. The table is confirmed (d04: GPT-5 75.9 to 73.3, Gemini-2.5-flash -9.7, DeepSeek-R1 -6.0; Gemini-2.5-pro gains on the hardest cell). The exploration mechanism is correlational, with traces on two models (d05). The guardrail has not been tested by anyone (K23).
8. Far inspiration and human-judged novelty without lowering feasibility: STILL OPEN, with a warning. Blind expert novelty did not survive execution (d12: AI novelty 5.778 to 4.729, human flat). Planned retrieval raises diversity (d13), but feasibility is not scored separately and the retrieval is not far.
9. ARN and NewtonBench tables read from the originals: CLOSED. ARN full PDF was read (d01 to d03) and NewtonBench table 2 re-parsed (d04). K14 holds; K08 needed restating.

Other corrections and additions
- b20 (Webb 2024 preprint) vs the published version: P=0.496 and 46% alternative-rule errors became P=0.92 and 38% (d06). Use the published figures.
- The "human sample about 46 vs 136" conflict: Lewis and Mitchell's extended paper lists human samples as trial counts per data point (92 to 384 for letter strings; d07). Participant counts still not resolved.
- A new relevant item the first pass missed: the 2026 Nature Communications paper on a pre-1936 historical counterfactual (d16). A human-supplied analogy took a 7B model from 2/20 to 20/20. This is one model and the human supplies the answer, so it shows the retrieval bottleneck, not self-directed analogy.
- Weak spots still standing: no direct LLM test of the cognitive-historical method; Dunbar and Maxwell remain second-hand or single-author; every analogy result with a human baseline uses 2023 models except ConceptARC.
