# Beautiful Slides

A Claude Code skill for producing high-quality, editable PowerPoint decks (`.pptx`) via `python-pptx` and LibreOffice. MIT-licensed. Measured uplift over a strong baseline on blind multi-scenario evaluation.

## What it is

`beautiful-slides` is a self-contained skill directory (`SKILL.md` + helper scripts) that teaches an LLM-driven authoring agent how to build a slide deck that looks intentional — not pretty-by-accident, but the kind of deck where every slide's palette, type, spacing, and pattern are predictable from the brief.

The skill packages three load-bearing disciplines that measurably beat a strong baseline on a blind 5-scenario evaluation:

1. **An explicit mood → mode classifier.** Before any slides exist, the generator picks exactly one mode (`sv-keynote`, `consulting-boardroom`, `editorial-magazine`, `craft-minimal`, `playful-marketing`) and commits to it for every slide. Consistency beats optimality.
2. **A canvas-bounds check.** After saving the `.pptx`, a small Python script walks every shape and asserts it lives inside the 16:9 canvas. Silent clipping is the single most common slop signal; this catches it deterministically.
3. **A must-include self-audit.** After saving, the generator extracts the brief's must-include list and verifies each item is COVERED / MENTIONED / MISSING in the emitted deck (via markitdown), then patches until everything is COVERED.

The rest of the SKILL.md is a synthesized design discipline — modes with full type + color tokens, a slide-pattern grammar (Marquee, Verdict, Number Hammer, Counterweight, Triptych, Proof Plot, Dossier, Resolution, etc.), a canvas/grid system in EMU, and a named anti-pattern list (Bullet Brigade, Gradient Industrial Complex, Cardocalypse, Period Piece, Geist Everywhere, ...).

## What it adds vs. plain python-pptx

Plain `python-pptx` gives you an API. `beautiful-slides` gives you a system:

- **Mode tokens.** Concrete hex/font values per mode so the generator does not invent a palette mid-deck.
- **Pattern grammar.** 14 named slide patterns, each with composition bounds and copy limits — so the generator never asks "what goes on this slide?" without a structural answer.
- **Canvas rigour.** All dimensions expressed in EMU; a bundled `check_bounds.py` enforces them post-generation.
- **Brief fidelity.** A post-gen must-include audit prevents the generator from producing a beautiful deck that forgot to mention the $45M raise.
- **Anti-pattern taxonomy.** Named slop so the generator refuses to produce it.

## Install

Clone into your Claude Code skills directory:

```bash
cd ~/.claude/skills
git clone https://github.com/bassimeledath/beautiful-slides.git
```

Or into a project-local skills directory, wherever your agent loads skills from. The skill root is the `beautiful-slides/` directory — it contains `SKILL.md` at the top level, with helper scripts in `scripts/`.

System dependencies (install once):

```bash
# macOS
brew install --cask libreoffice
brew install poppler
pip install python-pptx markitdown
```

On Linux, install `libreoffice`, `poppler-utils`, and the same pip packages from your package manager.

## Evidence

Ablation study over 5 scenarios (10/5/15/12/20 slides, 5 distinct moods), blind Opus judge, rubric of Style + Alignment + Diversity (each 0–5, per scenario; max total 15).

| Variant | Mean (0–15) | Style | Align | Divers | Δ vs baseline |
|---|---:|---:|---:|---:|---:|
| Anthropic baseline | 11.40 | 4.00 | 3.80 | 3.60 | — |
| + mood → mode only | 13.20 | 4.60 | 5.00 | 3.60 | +1.80 |
| + bounds check only | 13.40 | 4.80 | 5.00 | 3.60 | +2.00 |
| + self-audit only | 12.80 | 4.20 | 5.00 | 3.60 | +1.40 |
| **All three stacked** (this skill) | **13.60** | **4.60** | **5.00** | **4.00** | **+2.20** |

The stacked combination is the configuration shipped here. Per-scenario: combo scored 14 / 13 / 13 / 14 / 14 vs. baseline's 13 / 10 / 13 / 13 / 8.

Full methodology, rubric, per-variant per-scenario scores, and a 2-paragraph synthesis of why these three interventions were selected: see [`EVIDENCE.md`](./EVIDENCE.md).

## Layout

```
beautiful-slides/
  README.md           # this file
  LICENSE             # MIT
  SKILL.md            # the skill itself (~470 lines)
  EVIDENCE.md         # ablation-study methodology + results
  scripts/
    check_bounds.py   # canvas-bounds enforcer (run after save)
    render_preview.py # soffice + pdftoppm convenience wrapper
  charts/             # five themed chart templates (bar, line, kpi, funnel, heatmap)
```

## License

MIT. See [`LICENSE`](./LICENSE).
