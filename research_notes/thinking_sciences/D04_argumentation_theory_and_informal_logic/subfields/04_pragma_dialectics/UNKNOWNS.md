# Pragma-dialectics: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D04.04-U1 | Does a rule-based self-audit (burden, relevance, starting point, closure) beat a generic "find errors" critique? | Short rule checklist at the final audit step | S8, G2 | K01, K21; d07 (53 vs 51 on 120 items, 8B model); single-source, no direct test | Seeded flawed drafts (6 flaw types plus clean controls), 3 arms: no audit, generic critique, 10-rule checklist; flaw found and fixed; false alarms | Checklist beats generic by 3 points or more with 95% CI above 0 and false alarms not higher | High |
| D04.04-U2 | Does a burden-of-proof gate (revise only on new verified evidence) cut wrong flips without causing stubbornness? | Evidence-gated revision rule | G2 | K10, K24; d10, d11, d17 (72% to 12%, code smells), d18; single-source, narrow tasks | Correct answers then pushback of 4 kinds (bare, real evidence, fabricated citation, wrong correction); plain vs gate vs gate plus evidence check | Regressive flips down 30% relative or more and progressive flips not down more than 2 points | High |
| D04.04-U3 | Does a critical-question audit lower false alarms on valid arguments that share a fallacy's scheme? | Critical-question step in any fallacy or flaw check | S8 | K07, K23; a23, d08 (gap +13.5 and +12.6pp; no chain of thought tested) | Scheme Foils items; arms: name the fallacy, binary, critical-question audit; false-positive gap and recall | Gap down 5pp or more with recall loss under 3pp | High |
| D04.04-U4 | Do source-qualification and term-definition checks fix the weak spots (authority, equivocation)? | These two checks first in the audit | S8 | K25; d12, d13 (GPT-4 authority 39.2%; CoT no help); single-source, older models | LoFa-style items for authority and equivocation; plain vs targeted audit; resistance rate | Plus 5 points or more on those types, no loss elsewhere | Med |
| D04.04-U5 | Does a fallacy-aware critique pass lower the fallacy rate in our own final answers, and at what cost? | One critique pass at S9 | S9 | K18, K27; a22 (training, not a scaffold), no scaffold test | Open questions answered with and without critique pass; blind code-plus-judge fallacy count; tokens | Fallacy rate down 20% relative at under 1.3x tokens | Med |
| D04.04-U6 | Does stripping emotional framing at input stop verdict drift? | Framing-strip step at S1 | S1 | K08; a25 (human F1 -14.5%), a13; human data, 8B LLM only | 1,000 argument pairs, neutral vs framed; plain vs strip; verdict change rate | Change rate down by half, accuracy not down | Med |
| D04.04-U7 | Is internal two-sided debate better than self-consistency at equal tokens? | Nothing (it would overturn G9); otherwise confirm G9 | G9 | K13 contested; K14 and K16 established; K27 no direct test | Our task mix; N votes vs two-sided debate then adjudicate at the same tokens; accuracy | Debate wins by 3 points or more on 2 task types with CI above 0 (otherwise G9 stands) | Low |
| D04.04-U8 | Does third-person framing of pushback reduce flips on current models? | Rewrite user pushback in third person | G2 | d11 (up to 63.8% reduction; frontier models already near ceiling under bare pressure) | Pushback set including false presuppositions; first person vs third person; flip count | Flips down 20% relative on presupposition items | Low |
| D04.04-U9 | Does extracting argument structure before critique help? | Structure extraction step | S2 | K06; a17 (0.61 to 0.84 with gold labels), c02 (+5.46, fine-tuned); inflated, not zero-shot | Same drafts; direct critique vs extract premises and conclusion then critique | Flaw detection +4 points at under 1.3x tokens | Low |
| D04.04-U10 | Does an LLM's own audience adaptation derail into fallacies that detectors miss? | Guard on persuasive output | G2, G5 | K26; d14, d16 (rhetoric moves human judges; deflection on request only) | Ask for persuasive text to named audiences; blind human plus code check for derailments; plain vs audit | Derailment rate of 10% or more in plain arm and halved by audit | Low |
| D04.04-U11 | Do frontier models with deliberate reasoning still show the scheme-recognition gap? | Whether to rely on any model fallacy verdict | G5, G10 | K07, d08 (thinking off, 64-token cap) | Scheme Foils with thinking on vs off; false-positive gap | Gap under 5pp with thinking on (then relax the "noisy labels" rule) | Med |

## Open questions we cannot test on our bench yet

- Per-study sample sizes and effect sizes for the 2009 Amsterdam book and 2012 paper. Needs full text (paywalled).
- Any independent replication of the lay-judgment findings. Needs a new human study; our bench has no human raters.
- Whether following the ten rules yields correct conclusions (problem-solving validity). Needs a bench with ground truth for open argument, which we lack.
- Multi-party use (the real setting of the theory). G9 excludes it, so no bench exists.
- Journal-only PD and Periodic Table LLM work (Argumentation, ISSA proceedings). Needs library access.
- Rule tests beyond rules 1, 2, 8, 9. No data exist.

## Order to run

1. **U2 (burden-of-proof gate).** Cheapest, closest to a measured effect (72% to 12%), and attacks a known failure (flips under pressure).
2. **U1 (rule audit vs generic critique).** The central untested question for this subfield. Decides whether any PD material enters the schema.
3. **U3 (critical-question audit on scheme foils).** Tests the best-documented LLM weakness (false alarms) with a cheap prompt change.
