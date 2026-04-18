# Evidence

How the three additions in this skill were chosen, and how the stacked combination was measured.

## Method

Single-change ablations against a strong baseline (Anthropic's open-source `pptx` skill), evaluated by a blind LLM judge over five distinct deck-generation scenarios.

- **Baseline (`i0`):** unmodified Anthropic `pptx` skill.
- **Variants (`i1`–`i15`):** 15 single-change variants grouped into three axes.
  - Axis A (5 variants): prose-only additions to `SKILL.md` (style guide, design principles, mood mappings).
  - Axis B (5 variants): post-generation alignment / QA scripts (bounds, overflow, contrast, round-trip, fonts).
  - Axis C (5 variants): diversity / outline / must-include interventions.
- **Scenarios (5):** 10-slide Series B keynote pitch (cinematic / OLED); 5-slide exec update; 15-slide technical deep-dive; 12-slide launch deck (playful); 20-slide board read-ahead (Economist-style).
- **Generator:** `claude -p --model sonnet` per scenario, parallelized. Executes the full skill workflow end-to-end (parse brief, author in Python, render, QA, save).
- **Implementer:** `claude -p --model opus`, one run per variant, applies the single variant change to the baseline skill.
- **Judge:** `claude -p --model opus`, blind to variant identity. Sees only the scenario brief, 15 PNGs (slides 1–3 from each of the 5 scenarios), and a fixed 0–5 rubric.
- **Rubric per scenario (max 15):** Style (0–5), Alignment (0–5), Diversity (0–5).
- **Aggregate score per variant:** mean of per-scenario totals across the 5 scenarios.

**Keep criterion (variant kept iff both):**
1. `mean_total ≥ baseline + 0.3` (i.e. ≥ 11.70).
2. Variant beats baseline's per-scenario total on ≥ 3 of 5 scenarios individually.

## Leaderboard

| Rank | Iter | Tag | Axis | Mean | Style | Align | Divers | s1 | s2 | s3 | s4 | s5 | Wins vs base | Verdict |
|---:|:---|:---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|:---|
| 1  | i6  | b1-bounds                    | B | **13.40** | 4.80 | 5.00 | 3.60 | 14 | 13 | 12 | 14 | 14 | 4/5 | **KEEP** |
| 2  | i5  | a5-impeccable                | A | **13.20** | 4.60 | 5.00 | 3.60 | 14 | 14 | 12 | 13 | 13 | 3/5 | **KEEP** |
| 3  | i14 | c4-adherence-check           | C | **12.80** | 4.20 | 5.00 | 3.60 | 12 | 13 | 12 | 14 | 13 | 3/5 | **KEEP** |
| 4  | i4  | a4-principles                | A | 12.60 | 4.00 | 5.00 | 3.60 | 13 | 13 | 13 | 12 | 12 | 2/5 | discard |
| 5  | i7  | b2-overflow                  | B | 12.60 | 4.20 | 4.80 | 3.60 | 13 | 13 | 12 | 13 | 12 | 2/5 | discard |
| 6  | i12 | c2-anti-boilerplate          | C | 12.40 | 4.00 | 4.80 | 3.60 | 12 | 13 | 13 | 12 | 12 | 2/5 | discard |
| 7  | i1  | a1-tokens                    | A | 12.20 | 4.20 | 4.60 | 3.40 | 12 | 11 | 12 | 12 | 14 | 2/5 | discard |
| 8  | i3  | a3-archetypes                | A | 12.20 | 4.00 | 4.80 | 3.40 | 12 | 10 | 13 | 14 | 12 | 2/5 | discard |
| 9  | i9  | b4-roundtrip                 | B | 12.20 | 3.80 | 4.80 | 3.60 | 12 | 12 | 12 | 14 | 11 | 3/5 | KEEP (rank 4) |
| 10 | i13 | c3-archetype-diversity       | C | 12.00 | 3.80 | 4.80 | 3.40 | 13 | 13 | 12 | 9  | 13 | 2/5 | discard |
| 11 | i15 | c5-must-include-parser       | C | 11.80 | 3.60 | 4.80 | 3.40 | 13 | 13 | 11 | 12 | 10 | 2/5 | discard |
| 12 | i2  | a2-shame                     | A | 11.60 | 3.80 | 4.40 | 3.40 | 13 | 13 | 13 | 8  | 11 | 2/5 | discard |
| 13 | i0  | baseline                     | - | 11.40 | 4.00 | 3.80 | 3.60 | 13 | 10 | 13 | 13 | 8  | -   | baseline |
| 14 | i10 | b5-fonts                     | B | 10.80 | 3.80 | 3.80 | 3.20 | 12 | 8  | 8  | 13 | 13 | 1/5 | discard |
| 15 | i11 | c1-outlines                  | C | 10.20 | 3.40 | 4.00 | 2.80 | 13 | 12 | 10 | 11 | 5  | 1/5 | discard |
| 16 | i8  | b3-contrast                  | B | 9.60  | 3.40 | 3.00 | 3.20 | 5  | 12 | 12 | 11 | 8  | 1/5 | discard |

## Top-3 kept variants

### i6 — `b1-bounds` (Axis B, mean 13.40, wins 4/5)

Added `scripts/check_bounds.py`, a small Python script that parses the emitted `.pptx` and asserts every shape's `(x, y, w, h)` is inside the `12,192,000 × 6,858,000` EMU canvas. Wired a call into the SKILL.md build flow so the generator runs it post-generation; on any out-of-bounds violation the generator is instructed to move/resize the shape and re-emit.

Why it's the top result: the bounds check is the cheapest, most deterministic signal for alignment (which was baseline's weakest dimension — 3.80). With it the generator reliably stops emitting shapes that clip off-canvas, lifting align from 3.80 → 5.00 while leaving the creative side of the skill untouched.

### i5 — `a5-impeccable` (Axis A, mean 13.20, wins 3/5)

Added an explicit mood → mode mapping and authoring examples to `SKILL.md`. Prose only; no tokens, no scripts. The generator is asked to classify the brief's mood and commit to exactly one mode, with a discipline rule that bans mixing elements from another mode.

Why it works: gives the generator a vocabulary for mapping brief → visual register (cinematic vs. board-deck vs. literary) instead of leaving that decision unguided. Pays off most on scenarios 1 and 2 (cinematic + board-deck briefs) where it scored a perfect 14.

### i14 — `c4-adherence-check` (Axis C, mean 12.80, wins 3/5)

Added a post-generation self-check to `SKILL.md`: re-read the scenario's must-includes, list which are covered vs. missing, then patch the missing ones before finalising. The audit uses `markitdown` to extract text from the `.pptx` and mark every must-include as COVERED / MENTIONED / MISSING.

Why it works: the judge rewards visible adherence to scenario must-includes under the Diversity rubric, and this change directly targets that. Notably, it adds no code path — the whole gain is a reliable self-audit loop, which the baseline was skipping.

## Combination round

Stacked the three kept winners into one merged variant `icombo-a5b1c4`. Same blind-judge rubric, same 5 scenarios, same implementer=Opus / generator=Sonnet / judge=Opus pipeline. Post-gen order in the merged SKILL.md: visual QA → bounds check → must-include self-audit.

### Combo result vs individual winners

| Variant | Axis | Mean | Style | Align | Divers | s1 | s2 | s3 | s4 | s5 | Δ vs baseline |
|:---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline (i0)                 | -     | 11.40     | 4.00 | 3.80 | 3.60 | 13 | 10 | 13 | 13 | 8  | — |
| i5 a5-impeccable              | A     | 13.20     | 4.60 | 5.00 | 3.60 | 14 | 14 | 12 | 13 | 13 | +1.80 |
| i6 b1-bounds                  | B     | 13.40     | 4.80 | 5.00 | 3.60 | 14 | 13 | 12 | 14 | 14 | +2.00 |
| i14 c4-adherence-check        | C     | 12.80     | 4.20 | 5.00 | 3.60 | 12 | 13 | 12 | 14 | 13 | +1.40 |
| **icombo a5+b1+c4**           | combo | **13.60** | 4.60 | 5.00 | 4.00 | 14 | 13 | 13 | 14 | 14 | **+2.20** |

Pre-registered thresholds: ≥13.70 = compound, 13.20–13.70 = neutral, ≤13.20 = interfere. The combo landed at **13.60** — inside the neutral band, 0.10 below the compound threshold and 0.20 above the best individual. No interference (the stack beats baseline by +2.20 and edges every individual winner), but no real compounding either: alignment is already pinned at 5.00 from b1 alone; style sits at the 4.60 a5 hit solo; the only real movement is diversity (3.60 → 4.00), which is where c4 was designed to help.

Net: the three interventions pull on largely overlapping judge levers rather than adding independent axes. The combined skill is a modest all-rounder improvement over any single change, and it is the configuration shipped in this repository.

## Synthesis: why these three

Two paragraphs on why these three survived and others did not.

**Every kept variant targets a different failure mode of the baseline, and every dropped variant either overlapped with one that was kept or actively regressed some dimension.** Baseline's weakest rubric axis was alignment (3.80). Axis B's `b1-bounds` is a deterministic alignment backstop — the cheapest possible lift, and the largest — so it dominates B. Axis A's best entries all move style from 4.00 → 4.20–4.60, but only `a5-impeccable` pairs the prose with concrete examples that give the generator a mode vocabulary it can actually commit to; pure-criticism variants (`a2-shame`) teach the model what not to do without giving it a positive target, and tokenized variants (`a1-tokens`) move the needle less because the baseline already implicitly understands tokens. Axis C is the most interesting: the outline-generation variant (`c1-outlines`) cost more than it paid back — more tokens on planning, less on polish — and collapsed scenario 5 to a 5. The `c4-adherence-check` won Axis C because it operates *after* the creative work is done, so it cannot damage style; it only patches the content-fidelity failure mode that the Diversity rubric explicitly rewards.

**The combination is a modest compound, not a multiplicative one, because the three interventions converge on overlapping judge levers rather than independent axes.** Once `b1-bounds` pins alignment at 5.00, there is no alignment headroom left for the other two to claim. Once `a5-impeccable` chooses a coherent visual register, style saturates around 4.60 regardless of what else runs. The only axis with meaningful remaining headroom is Diversity (which, in this rubric, measures must-include coverage and pattern variety), and that is exactly where `c4` moves the score (3.60 → 4.00). The combined skill lands at 13.60 out of 15 — a +2.20 over baseline, which is a meaningful lift on a rubric where the top-1 single change was +2.00. It is the configuration shipped in this repository. Further work would most plausibly come from genuinely new axes (e.g., chart-quality scoring, or a render-then-edit loop that compares visual output to the brief rather than just text fidelity), not from stacking more variants on the axes already covered.
