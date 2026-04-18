# Charts — index

Native python-pptx chart templates. Theme-aware via `tokens`. Five templates share one signature.

## Shared signature — load-bearing

Every chart exposes EXACTLY one public function:

```python
def render(slide, data, tokens, bounds):
    """Draw the chart onto `slide` inside `bounds`, styled by `tokens`."""
```

- `slide` — a `pptx.slide.Slide` instance. Shapes are added to `slide.shapes`.
- `data` — chart-type-specific dict. See each chart's `docs.md` for its shape.
- `tokens` — theme dict; keys below.
- `bounds` — `(x_emu, y_emu, w_emu, h_emu)`. Chart fits inside.

## Token contract

All colors are hex strings like `"#RRGGBB"`. All fonts are family-name strings.

| Key | Type | Role |
|---|---|---|
| `primary` | str | main series / hero color |
| `accent` | str | secondary series / highlights |
| `text` | str | foreground / labels |
| `muted` | str | axes, gridlines, secondary labels |
| `bg` | str | background fill |
| `font_display` | str | titles and hero numbers |
| `font_body` | str | labels |
| `font_mono` | str | numeric alignment (may equal body) |
| `font_size_base_pt` | int | body size in points |
| `radius_px` | int | optional corner radius in px |

Never hardcode a color or font in a chart file. Read everything from `tokens`.

## EMU coordinate system

python-pptx works in English Metric Units. Handy:

- `914400` EMU per inch
- `12700` EMU per point
- Use `pptx.util.Emu(n)`, `pptx.util.Inches(n)`, `pptx.util.Pt(n)` helpers

`bounds` is always `(x, y, w, h)` in EMUs. A common 16:9 slide is `12192000 × 6858000` EMU.

## Picker guide

- **bar** — discrete comparisons across categories (revenue by segment, satisfaction by team). Use when the story is "which bucket wins." Supports grouped 2-series.
- **line** — trends over ordered x (time, months, cohort age). Use for cohort retention, trajectories, forecasts. Supports 1–N series; final series can be emphasized.
- **kpi** — hero-number tile with label, value, delta. The single most-used element. Compose 2–4 tiles in a row to build a scorecard.
- **funnel** — conversion / narrowing stages (lead → closed-won). Best for pipeline, signup flows, drop-off stories. 4–7 stages.
- **heatmap** — grid of colored cells, intensity interpolates between `bg` and `primary`. Use for density patterns (hour × weekday, segment × month). Best at ≥ 4×4 cells.

## Import pattern (inside render.py)

Every chart sticks to this small set:

```python
from pptx.util import Emu, Pt, Inches
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
```

No external styling libraries. No rasterizers. No embedded Excel charts.

## Using a chart from a deck script

```python
from pptx import Presentation
from pptx.util import Inches, Emu

import sys; sys.path.append("/path/to/charts")
from bar.render import render as render_bar

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

tokens = {
    "primary": "#0F4C81", "accent": "#05603A", "text": "#101828",
    "muted": "#475467", "bg": "#FFFFFF",
    "font_display": "Public Sans", "font_body": "Public Sans", "font_mono": "Public Sans",
    "font_size_base_pt": 14, "radius_px": 0,
}

data = {"orientation": "vertical",
        "categories": ["Enterprise", "Mid-market", "SMB", "Startup"],
        "series": [{"name": "Q1 Actual", "values": [12.4, 8.1, 4.3, 1.8]}],
        "value_suffix": "M", "show_values": True}

bounds = (Inches(0.8), Inches(0.8), Inches(11.7), Inches(5.9))
bounds = tuple(int(x) for x in bounds)
render_bar(slide, data, tokens, bounds)
prs.save("deck.pptx")
```

## Directory layout

```
charts/
  INDEX.md       ← this file
  bar/     render.py  docs.md  example.py  example-<mode>.pptx×5  renders/<mode>.png×5
  line/    render.py  docs.md  example.py  example-<mode>.pptx×5  renders/<mode>.png×5
  kpi/     render.py  docs.md  example.py  example-<mode>.pptx×5  renders/<mode>.png×5
  funnel/  render.py  docs.md  example.py  example-<mode>.pptx×5  renders/<mode>.png×5
  heatmap/ render.py  docs.md  example.py  example-<mode>.pptx×5  renders/<mode>.png×5
```

The five modes are: `sv-keynote`, `editorial-magazine`, `playful-marketing`, `consulting-boardroom`, `craft-minimal`. Each mode has a distinct palette, type system, and spacing temperament — see `MODE_TOKENS.md` at the project root for exact token dicts.
