# Beautiful Slides

**A Claude Code skill for producing high-quality, editable PowerPoint decks (`.pptx`) via `python-pptx` and LibreOffice.** Measured uplift over a strong baseline on blind multi-scenario evaluation.

`beautiful-slides` teaches an LLM-driven authoring agent how to build a slide deck that looks intentional — not pretty-by-accident, but the kind of deck where every slide's palette, type, spacing, and pattern are predictable from the brief.

The skill packages three load-bearing disciplines:

1. **An explicit mood -> mode classifier.** Before any slides exist, the generator picks exactly one visual mode and commits to it for every slide. Consistency beats optimality.
2. **A canvas-bounds check.** After saving the `.pptx`, a Python script walks every shape and asserts it lives inside the 16:9 canvas. Silent clipping is the single most common slop signal; this catches it deterministically.
3. **A must-include self-audit.** After saving, the generator verifies each brief requirement is COVERED / MENTIONED / MISSING in the emitted deck, then patches until everything is COVERED.

---

## Install

```bash
npx skills add bassimeledath/beautiful-slides -g     # user-level (all projects)
npx skills add bassimeledath/beautiful-slides        # project-level (team-shared)
```

### System dependencies (install once)

```bash
# macOS
brew install --cask libreoffice
brew install poppler
pip install python-pptx markitdown
```

On Linux, install `libreoffice`, `poppler-utils`, and the same pip packages from your package manager.

## Updating

```bash
npx skills update
```

## Evidence

Ablation study over 5 scenarios (10/5/15/12/20 slides, 5 distinct moods), blind Opus judge, rubric of Style + Alignment + Diversity (each 0-5, per scenario; max total 15).

| Variant | Mean (0-15) | Style | Align | Divers | Delta vs baseline |
|---|---:|---:|---:|---:|---:|
| Anthropic baseline | 11.40 | 4.00 | 3.80 | 3.60 | -- |
| + mood -> mode only | 13.20 | 4.60 | 5.00 | 3.60 | +1.80 |
| + bounds check only | 13.40 | 4.80 | 5.00 | 3.60 | +2.00 |
| + self-audit only | 12.80 | 4.20 | 5.00 | 3.60 | +1.40 |
| **All three stacked** (this skill) | **13.60** | **4.60** | **5.00** | **4.00** | **+2.20** |

Full methodology, rubric, per-variant per-scenario scores: see [`skills/beautiful-slides/EVIDENCE.md`](skills/beautiful-slides/EVIDENCE.md).

## Layout

```
beautiful-slides/
  README.md                          # this file
  LICENSE                            # MIT
  CLAUDE.md                          # development guide
  skills/
    beautiful-slides/
      SKILL.md                       # the skill itself (~500 lines)
      EVIDENCE.md                    # ablation-study methodology + results
      scripts/
        check_bounds.py              # canvas-bounds enforcer (run after save)
        render_preview.py            # soffice + pdftoppm convenience wrapper
      charts/                        # five themed chart templates
        INDEX.md                     # shared signature + picker guide
        INTERFACE.md                 # authoritative interface reference
        MODE_TOKENS.md               # per-mode token dicts
        tokens.py                    # shared MODES dict
        bar/  line/  kpi/  funnel/  heatmap/
```

## License

MIT. See [`LICENSE`](./LICENSE).
